---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

**IMPORTANT: Before writing any test script, ALWAYS use the `env-manager` skill to check if required environment variables (TEST_BASE_URL, TEST_EMAIL, TEST_PASSWORD, etc.) are set. DO NOT write environment loading code in test scripts.**

To test local web applications, write native Python Playwright scripts.

**Helper Scripts Available**:
- `scripts/login_helper.py` - Handles authentication with role-based login (user/admin)

**Important Integration Points**:
- **Environment Management**: Use `env-manager` skill to check/load environment variables
- **Application Lifecycle**: Use `app-runner` skill if application is not accessible
- Scripts exist to be called directly as black-box tools - DO NOT read source code unless absolutely necessary to avoid context pollution.

## Decision Tree: Testing Workflow

```
User asks to test → Check environment variables (use env-manager skill)
                        │
                        ↓
                   Check if app is accessible at TEST_BASE_URL
                        │
                        ├─ No → Invoke app-runner skill to start application
                        │       │
                        │       └─ Wait for health check to pass
                        │
                        ↓
                   Is authentication required?
                        │
                        ├─ Yes → Use login_helper.py for auth
                        │
                        ↓
                   Write Playwright test:
                        1. Navigate and wait for networkidle
                        2. Take screenshot or inspect DOM
                        3. Identify selectors from rendered state
                        4. Execute actions with discovered selectors
                        5. Assert expected behavior
```

## Example: Basic Test Script Pattern

Test scripts should assume the application is already running (managed by app-runner skill):

```python
from playwright.sync_api import sync_playwright
import os
import sys

# Get application URL from environment
base_url = os.environ.get('TEST_BASE_URL')
if not base_url:
    print("ERROR: TEST_BASE_URL not set. Run env-manager skill first.")
    sys.exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to application
    page.goto(base_url)
    page.wait_for_load_state('networkidle')  # CRITICAL: Wait for JS to execute

    # Your test logic here
    page.screenshot(path='/tmp/screenshot.png')

    browser.close()
```

## Authenticated Testing with login_helper.py

For applications requiring authentication, use the login helper to manage user sessions.

**Prerequisites:**

The login helper uses the `env-manager` skill to intelligently handle environment variables. It will automatically detect missing variables and suggest the appropriate commands for your shell.

Required environment variables:

```bash
# Application endpoint (REQUIRED)
export TEST_BASE_URL=<your_application_url>

# Regular user credentials (required for role="user")
export TEST_EMAIL=user@example.com
export TEST_PASSWORD=user_password

# Admin user credentials (required for role="admin")
export TEST_ADMIN_EMAIL=admin@example.com
export TEST_ADMIN_PASSWORD=admin_password
```

**Tip:** You can create a `.env.test` file with these variables and source it:
```bash
# In .env.test file:
export TEST_BASE_URL=http://localhost:3000
export TEST_EMAIL=user@example.com
export TEST_PASSWORD=user_password
export TEST_ADMIN_EMAIL=admin@example.com
export TEST_ADMIN_PASSWORD=admin_password

# Then in your shell:
source .env.test
```

The skill uses REAL environment variables - no fake environment management libraries.

**Usage:**
```python
from playwright.sync_api import sync_playwright
import sys
import os
from pathlib import Path

# Add skill scripts to path
sys.path.append(str(Path.home() / ".claude/skills/webapp-testing/scripts"))
from login_helper import get_authenticated_page

with sync_playwright() as p:
    # Get authenticated page as regular user (uses TEST_BASE_URL from env)
    page = get_authenticated_page(p, role="user")

    # Or specify a custom base URL explicitly
    page = get_authenticated_page(p, base_url="https://staging.example.com", role="admin")

    # Page is now authenticated - navigate and test using TEST_BASE_URL
    base_url = os.environ['TEST_BASE_URL']
    page.goto(f'{base_url}/dashboard')
    page.wait_for_load_state('networkidle')

    # ... perform tests

    page.context.browser.close()
```

**Features:**
- Reads credentials from REAL environment variables (no fake environment libraries)
- Integrates with `env-manager` skill for intelligent environment detection
- Automatically finds .env files and suggests appropriate load commands for your shell
- Configurable base URL via `TEST_BASE_URL` environment variable
- Caches auth state per role (`/tmp/auth_state_user.json`, `/tmp/auth_state_admin.json`)
- Validates auth state and re-authenticates if expired
- Supports `force_reauth=True` to bypass cache
- Works seamlessly with code changes and auth secret cycling

**Note:** If environment variables are missing, the skill will provide shell-specific commands to load them. The `env-manager` skill handles bash, zsh, and fish shells.

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- **Use bundled scripts as black boxes** - To accomplish a task, consider whether one of the scripts available in `scripts/` can help. These scripts handle common, complex workflows reliably without cluttering the context window. Use `--help` to see usage, then invoke directly.
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`
- **Screenshots**: After saving screenshots, ALWAYS open them in the user's image viewer using `open <path>` (via Bash tool). DO NOT use the Read tool for screenshots - terminal may not support inline image display. Opening in system viewer (Preview on macOS) is more reliable.

## Anti-Patterns (DO NOT DO THIS)

❌ **NEVER load .env files in Python scripts**:
```python
# BAD - Don't do this!
with open('.env.test') as f:
    for line in f:
        key, value = line.split('=')
        os.environ[key] = value
```

✅ **INSTEAD**: Scripts should only READ from environment. If variables are missing, use the `env-manager` skill to help the user load them in their actual shell:
```python
# GOOD - Just read from environment
base_url = os.environ['TEST_BASE_URL']  # Will fail if not set

# If it fails, invoke env-manager skill to help user set up environment
```

**Environment loading happens in the SHELL, not in Python code.**

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation
