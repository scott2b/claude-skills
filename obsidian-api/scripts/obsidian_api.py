#!/usr/bin/env python3
"""
Core Obsidian REST API wrapper.

Handles authentication, requests, and error handling for all Obsidian operations.
Based on: https://github.com/docker/mcp-obsidian
"""

import os
import sys
import urllib.parse
import urllib.request
import urllib.error
import ssl
import json
from typing import Optional, Dict, Any, List


class ObsidianAPIError(Exception):
    """Base exception for Obsidian API errors"""
    pass


class HTTPResponse:
    """Wrapper for urllib response to provide requests-like interface"""
    def __init__(self, response):
        self._response = response
        self._content = None

    def json(self) -> Dict[str, Any]:
        """Parse response as JSON"""
        if self._content is None:
            self._content = self._response.read()
        return json.loads(self._content.decode('utf-8'))

    @property
    def text(self) -> str:
        """Get response as text"""
        if self._content is None:
            self._content = self._response.read()
        return self._content.decode('utf-8')


class ObsidianAPI:
    """
    Wrapper for Obsidian Local REST API.

    Requires environment variables:
    - OBSIDIAN_API_KEY (required)
    - OBSIDIAN_HOST (optional, defaults to https://127.0.0.1:27124)
    - OBSIDIAN_VERIFY_SSL (optional, defaults to false)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        host: Optional[str] = None,
        verify_ssl: Optional[bool] = None
    ):
        """Initialize Obsidian API client"""
        self.api_key = api_key or os.environ.get('OBSIDIAN_API_KEY')
        if not self.api_key:
            raise ObsidianAPIError(
                "OBSIDIAN_API_KEY environment variable required. "
                "Get it from Obsidian → Settings → Community Plugins → Local REST API"
            )

        self.host = host or os.environ.get('OBSIDIAN_HOST', 'https://127.0.0.1:27124')
        self.verify_ssl = verify_ssl if verify_ssl is not None else \
                         os.environ.get('OBSIDIAN_VERIFY_SSL', 'false').lower() == 'true'

        # Setup SSL context
        if not self.verify_ssl:
            self.ssl_context = ssl._create_unverified_context()
        else:
            self.ssl_context = ssl.create_default_context()

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Build request headers with auth"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        if extra:
            headers.update(extra)
        return headers

    def _request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
        params: Optional[Dict[str, str]] = None,
        timeout: int = 10
    ) -> 'HTTPResponse':
        """Make HTTP request to Obsidian API"""
        url = f"{self.host}{endpoint}"

        # Add query parameters to URL
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"

        # Prepare request
        req = urllib.request.Request(
            url,
            data=data if isinstance(data, bytes) else None,
            headers=self._headers(headers),
            method=method
        )

        try:
            response = urllib.request.urlopen(req, context=self.ssl_context, timeout=timeout)
            return HTTPResponse(response)
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                raise ObsidianAPIError(
                    f"Cannot connect to Obsidian at {self.host}. "
                    "Is Obsidian running and is the Local REST API plugin enabled?"
                ) from e
            raise ObsidianAPIError(f"Request failed: {e}") from e
        except urllib.error.HTTPError as e:
            # Try to extract error message from response
            try:
                error_data = json.loads(e.read().decode('utf-8'))
                message = error_data.get('message', str(e))
                code = error_data.get('errorCode', e.code)
                raise ObsidianAPIError(f"API Error {code}: {message}") from e
            except (json.JSONDecodeError, UnicodeDecodeError):
                raise ObsidianAPIError(f"HTTP Error {e.code}: {e.reason}") from e
        except TimeoutError as e:
            raise ObsidianAPIError(f"Request timeout after {timeout}s") from e

    # Vault file operations

    def list_vault_files(self) -> List[Dict[str, Any]]:
        """List all files in vault root"""
        response = self._request('GET', '/vault/')
        return response.json().get('files', [])

    def list_directory_files(self, dirpath: str) -> List[Dict[str, Any]]:
        """List files in a specific directory"""
        # Ensure trailing slash
        if not dirpath.endswith('/'):
            dirpath += '/'
        # URL encode the path to handle special characters and spaces
        encoded_path = urllib.parse.quote(dirpath, safe='/')
        response = self._request('GET', f'/vault/{encoded_path}')
        return response.json().get('files', [])

    def get_file_content(self, filepath: str) -> str:
        """Read content of a file"""
        # URL encode the path to handle special characters and spaces
        encoded_path = urllib.parse.quote(filepath, safe='/')
        response = self._request('GET', f'/vault/{encoded_path}')
        return response.text

    def create_or_update_file(self, filepath: str, content: str) -> None:
        """Create or overwrite a file"""
        headers = {'Content-Type': 'text/markdown'}
        # URL encode the path to handle special characters and spaces
        encoded_path = urllib.parse.quote(filepath, safe='/')
        self._request('POST', f'/vault/{encoded_path}', headers=headers, data=content.encode('utf-8'))

    def patch_file(
        self,
        filepath: str,
        content: str,
        heading: Optional[str] = None,
        block: Optional[str] = None
    ) -> None:
        """
        Insert content at a specific location in file.

        Args:
            filepath: Path to file in vault
            content: Content to insert
            heading: Insert after this heading (e.g., "## Section")
            block: Insert after this block reference (e.g., "^block-id")
        """
        headers = {
            'Content-Type': 'text/markdown',
            'Operation': 'insert'
        }

        if heading:
            headers['Target-Type'] = 'heading'
            headers['Target'] = urllib.parse.quote(heading)
        elif block:
            headers['Target-Type'] = 'block'
            headers['Target'] = urllib.parse.quote(block)
        else:
            raise ValueError("Must specify either heading or block for patch operation")

        # URL encode the path to handle special characters and spaces
        encoded_path = urllib.parse.quote(filepath, safe='/')
        self._request('PATCH', f'/vault/{encoded_path}', headers=headers, data=content.encode('utf-8'))

    def append_to_file(self, filepath: str, content: str) -> None:
        """Append content to end of file"""
        headers = {'Content-Type': 'text/markdown'}
        current_content = self.get_file_content(filepath)
        new_content = current_content + content
        self.create_or_update_file(filepath, new_content)

    def delete_file(self, filepath: str) -> None:
        """Delete a file"""
        # URL encode the path to handle special characters and spaces
        encoded_path = urllib.parse.quote(filepath, safe='/')
        self._request('DELETE', f'/vault/{encoded_path}')

    # Search operations

    def simple_search(self, query: str, context_length: int = 100) -> Dict[str, Any]:
        """
        Simple text search across vault.

        Args:
            query: Search term
            context_length: Number of characters of context around match
        """
        params = {
            'query': query,
            'contextLength': str(context_length)
        }
        response = self._request('POST', '/search/simple/', params=params)
        return response.json()

    def jsonlogic_search(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Advanced search using JSONLogic query.

        Example query:
        {
            "and": [
                {">=": [{"var": "mtime"}, 1704672000]},
                {"in": ["#tag", {"var": "tags"}]}
            ]
        }
        """
        headers = {'Content-Type': 'application/vnd.olrapi.jsonlogic+json'}
        response = self._request('POST', '/search/', headers=headers, data=json.dumps(query))
        return response.json()

    def dataview_search(self, dql_query: str) -> Dict[str, Any]:
        """
        Search using Dataview Query Language.

        Args:
            dql_query: DQL query string
        """
        headers = {'Content-Type': 'application/vnd.olrapi.dataview.dql+txt'}
        response = self._request('POST', '/search/', headers=headers, data=dql_query.encode('utf-8'))
        return response.json()

    # Periodic notes

    def get_periodic_note(self, period: str) -> str:
        """
        Get current periodic note.

        Args:
            period: One of 'daily', 'weekly', 'monthly', 'quarterly', 'yearly'
        """
        valid_periods = ['daily', 'weekly', 'monthly', 'quarterly', 'yearly']
        if period not in valid_periods:
            raise ValueError(f"Invalid period: {period}. Must be one of {valid_periods}")

        response = self._request('GET', f'/periodic/{period}/')
        return response.text

    def get_recent_periodic_notes(
        self,
        period: str,
        limit: int = 10,
        include_content: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Get recent periodic notes.

        Args:
            period: One of 'daily', 'weekly', 'monthly', 'quarterly', 'yearly'
            limit: Number of notes to return
            include_content: Whether to include note content
        """
        valid_periods = ['daily', 'weekly', 'monthly', 'quarterly', 'yearly']
        if period not in valid_periods:
            raise ValueError(f"Invalid period: {period}. Must be one of {valid_periods}")

        params = {
            'limit': str(limit),
            'includeContent': 'true' if include_content else 'false'
        }
        response = self._request('GET', f'/periodic/{period}/recent', params=params)
        return response.json()


def get_api() -> ObsidianAPI:
    """Get configured Obsidian API instance"""
    try:
        return ObsidianAPI()
    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        print("\nTo configure:", file=sys.stderr)
        print("1. Install 'Local REST API' plugin in Obsidian", file=sys.stderr)
        print("2. Enable the plugin in Settings → Community Plugins", file=sys.stderr)
        print("3. Copy API key from plugin settings", file=sys.stderr)
        print("4. Set environment variable: export OBSIDIAN_API_KEY=your_key", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    # Quick test
    try:
        api = get_api()
        files = api.list_vault_files()
        print(f"✓ Connected to Obsidian vault ({len(files)} files in root)")
    except ObsidianAPIError as e:
        print(f"✗ Connection failed: {e}", file=sys.stderr)
        sys.exit(1)
