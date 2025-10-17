#!/usr/bin/env python3
"""
Login helper for webapp testing with role-based authentication.

Supports multiple user roles (user, admin) with automatic credential loading,
auth state caching, and intelligent re-authentication when needed.

Environment Variables:
    TEST_BASE_URL: Base URL of the application (REQUIRED)
    TEST_EMAIL: Regular user email (REQUIRED for user role)
    TEST_PASSWORD: Regular user password (REQUIRED for user role)
    TEST_ADMIN_EMAIL: Admin user email (REQUIRED for admin role)
    TEST_ADMIN_PASSWORD: Admin user password (REQUIRED for admin role)

Usage:
    from login_helper import get_authenticated_page

    # Get page as regular user
    page = get_authenticated_page(playwright)

    # Get page as admin
    page = get_authenticated_page(playwright, role="admin")
"""

import os
from pathlib import Path
from typing import Literal, Optional
from playwright.sync_api import Page, Browser, BrowserContext, Playwright

Role = Literal["user", "admin"]


def check_required_env_vars(role: Role) -> tuple[bool, list[str], Optional[str]]:
    """
    Check if required environment variables are set using env-manager skill.

    Args:
        role: User role to check credentials for

    Returns:
        Tuple of (all_present, missing_vars, suggestion)
    """
    import subprocess
    import json

    required = ['TEST_BASE_URL']
    if role == 'user':
        required.extend(['TEST_EMAIL', 'TEST_PASSWORD'])
    elif role == 'admin':
        required.extend(['TEST_ADMIN_EMAIL', 'TEST_ADMIN_PASSWORD'])

    # Try to use env-manager skill if available
    env_manager_script = Path.home() / '.claude/skills/env-manager/scripts/check_env.py'

    if env_manager_script.exists():
        try:
            result = subprocess.run(
                ['python', str(env_manager_script), '--required', ','.join(required)],
                capture_output=True,
                text=True,
                timeout=5
            )
            info = json.loads(result.stdout)
            return (info['all_present'], info['missing_required'], info.get('suggestion'))
        except Exception:
            pass  # Fall back to simple check

    # Fallback: simple check
    missing = [var for var in required if not os.environ.get(var)]
    suggestion = "Set variables with: export VAR=value" if missing else None
    return (len(missing) == 0, missing, suggestion)

class LoginHelper:
    """Helper class for managing authenticated browser sessions."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        auth_state_dir: Optional[Path] = None,
        role: Role = "user"
    ):
        """
        Initialize login helper.

        Args:
            base_url: Base URL of the application (uses TEST_BASE_URL env var if not provided)
            auth_state_dir: Directory to store auth state files (defaults to /tmp)
            role: User role for checking required credentials
        """
        # Check for missing environment variables using env-manager skill
        all_present, missing, suggestion = check_required_env_vars(role)
        if not all_present and not base_url:
            # Provide helpful error message with env-manager's suggestions
            error_msg = f"\nMissing required environment variables for '{role}' role:\n"
            for var in missing:
                error_msg += f"  - {var}\n"
            if suggestion:
                error_msg += f"\n{suggestion}\n"
            else:
                error_msg += "\nSet these variables in your environment:\n"
                error_msg += f"   export {' '.join(missing)}=<value>\n"
            raise ValueError(error_msg)

        # Get base URL from parameter or env var (REQUIRED)
        self.base_url = base_url or os.environ.get('TEST_BASE_URL')
        if not self.base_url:
            raise ValueError(
                "Base URL is required. Set TEST_BASE_URL environment variable or pass base_url parameter."
            )
        self.base_url = self.base_url.rstrip('/')
        self.auth_state_dir = Path(auth_state_dir or "/tmp")
        self._load_credentials()

    def _load_credentials(self):
        """Load credentials from environment variables."""
        self.credentials = {}

        # Load user credentials
        user_email = os.environ.get('TEST_EMAIL')
        user_password = os.environ.get('TEST_PASSWORD')
        if user_email and user_password:
            self.credentials['user'] = {
                'email': user_email,
                'password': user_password
            }
        else:
            print("⚠️  Warning: User credentials not found (TEST_EMAIL, TEST_PASSWORD)")

        # Load admin credentials
        admin_email = os.environ.get('TEST_ADMIN_EMAIL')
        admin_password = os.environ.get('TEST_ADMIN_PASSWORD')
        if admin_email and admin_password:
            self.credentials['admin'] = {
                'email': admin_email,
                'password': admin_password
            }
        else:
            print("⚠️  Warning: Admin credentials not found (TEST_ADMIN_EMAIL, TEST_ADMIN_PASSWORD)")

    def _get_auth_state_path(self, role: Role) -> Path:
        """Get path to auth state file for a role."""
        return self.auth_state_dir / f"auth_state_{role}.json"

    def _perform_login(self, page: Page, role: Role) -> bool:
        """
        Perform login flow for the specified role.

        Args:
            page: Playwright page object
            role: User role to login as

        Returns:
            True if login successful, False otherwise
        """
        if role not in self.credentials:
            raise ValueError(f"No credentials found for role: {role}")

        creds = self.credentials[role]
        if "email" not in creds or "password" not in creds:
            raise ValueError(f"Incomplete credentials for role: {role}")

        try:
            print(f"🔐 Logging in as {role}: {creds['email']}")

            # Navigate to login page
            page.goto(self.base_url)
            page.wait_for_load_state('networkidle', timeout=10000)

            # Fill login form
            page.fill('input[type="email"]', creds['email'])
            page.fill('input[type="password"]', creds['password'])

            # Submit and wait for redirect
            # Based on LoginForm.svelte, successful login redirects to /codebooks
            page.click('button[type="submit"]:has-text("Login")')
            page.wait_for_url('**/codebooks', timeout=10000)

            print(f"✓ Successfully logged in as {role}")
            return True

        except Exception as e:
            print(f"❌ Login failed for {role}: {e}")
            return False

    def _is_authenticated(self, page: Page) -> bool:
        """
        Check if page is currently authenticated.

        Args:
            page: Playwright page object

        Returns:
            True if authenticated, False otherwise
        """
        try:
            # Try to navigate to a protected page
            page.goto(f"{self.base_url}/codebooks", wait_until="networkidle", timeout=5000)

            # Check if we got redirected to login page
            current_url = page.url
            if 'login' in current_url or current_url == f"{self.base_url}/":
                return False

            return True
        except:
            return False

    def get_authenticated_page(
        self,
        playwright: Playwright,
        role: Role = "user",
        headless: bool = True,
        force_reauth: bool = False
    ) -> Page:
        """
        Get an authenticated browser page for the specified role.

        This method will:
        1. Try to load saved auth state if available
        2. Validate the auth state is still valid
        3. Re-authenticate if needed
        4. Save new auth state for future use

        Args:
            playwright: Playwright instance
            role: User role ("user" or "admin")
            headless: Run browser in headless mode
            force_reauth: Force re-authentication even if auth state exists

        Returns:
            Authenticated Page object
        """
        auth_state_path = self._get_auth_state_path(role)
        context = None

        # Try to use existing auth state
        if not force_reauth and auth_state_path.exists():
            print(f"📂 Loading saved auth state for {role}")
            try:
                browser = playwright.chromium.launch(headless=headless)
                context = browser.new_context(storage_state=str(auth_state_path))
                page = context.new_page()

                # Verify auth state is still valid
                if self._is_authenticated(page):
                    print(f"✓ Auth state valid for {role}")
                    return page
                else:
                    print(f"⚠️  Auth state expired for {role}, re-authenticating...")
                    page.close()
                    context.close()
                    browser.close()
                    context = None
            except Exception as e:
                print(f"⚠️  Failed to load auth state: {e}")
                if context:
                    context.close()
                context = None

        # Perform fresh login
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        if not self._perform_login(page, role):
            raise RuntimeError(f"Failed to authenticate as {role}")

        # Save auth state
        context.storage_state(path=str(auth_state_path))
        print(f"💾 Saved auth state for {role} to {auth_state_path}")

        return page


def get_authenticated_page(
    playwright: Playwright,
    base_url: Optional[str] = None,
    role: Role = "user",
    headless: bool = True,
    force_reauth: bool = False
) -> Page:
    """
    Convenience function to get an authenticated page.

    Args:
        playwright: Playwright instance
        base_url: Base URL of the application (uses TEST_BASE_URL env var if not provided)
        role: User role ("user" or "admin")
        headless: Run browser in headless mode
        force_reauth: Force re-authentication even if auth state exists

    Returns:
        Authenticated Page object

    Example:
        import os
        with sync_playwright() as p:
            # Use TEST_BASE_URL from environment
            page = get_authenticated_page(p, role="user")

            # Or pass base_url explicitly
            page = get_authenticated_page(p, base_url="https://app.example.com", role="admin")

            # Navigate to pages using environment variable
            base_url = os.environ['TEST_BASE_URL']
            page.goto(f'{base_url}/dashboard')
            # ... perform tests
            page.context.browser.close()
    """
    helper = LoginHelper(base_url=base_url, role=role)
    return helper.get_authenticated_page(
        playwright=playwright,
        role=role,
        headless=headless,
        force_reauth=force_reauth
    )


if __name__ == "__main__":
    """Test the login helper."""
    from playwright.sync_api import sync_playwright

    print("Testing login helper...")

    with sync_playwright() as p:
        # Test user login
        print("\n=== Testing user login ===")
        page = get_authenticated_page(p, role="user")
        print(f"Current URL: {page.url}")
        page.context.browser.close()

        # Test admin login
        print("\n=== Testing admin login ===")
        try:
            page = get_authenticated_page(p, role="admin")
            print(f"Current URL: {page.url}")
            page.context.browser.close()
        except Exception as e:
            print(f"Admin login not configured: {e}")

        print("\n✅ Login helper tests complete!")
