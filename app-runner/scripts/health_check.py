#!/usr/bin/env python3
"""
Health check script to verify if a URL is accessible.

Usage:
    python health_check.py --url http://localhost:3000
    python health_check.py --url http://localhost:3000 --timeout 30

Returns JSON with status and exit code 0 if accessible, 1 if not.
"""

import sys
import json
import argparse
import time
from urllib.parse import urlparse


def health_check(url: str, timeout: int = 30, verbose: bool = False) -> dict:
    """
    Check if a URL is accessible.

    Args:
        url: URL to check
        timeout: Maximum time to wait in seconds
        verbose: Print progress messages

    Returns:
        Dict with 'accessible', 'status_code', 'time_taken', 'error' keys
    """
    try:
        import requests
    except ImportError:
        return {
            'accessible': False,
            'error': 'requests library not installed',
            'time_taken': 0
        }

    start_time = time.time()
    delay = 0.5
    last_error = None

    if verbose:
        print(f"🔍 Checking {url}...", file=sys.stderr)

    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)

            # Consider 2xx and 3xx as accessible
            # 4xx client errors also mean the server is up
            # Only 5xx server errors are considered inaccessible
            if response.status_code < 500:
                time_taken = time.time() - start_time
                if verbose:
                    print(f"✓ Accessible (HTTP {response.status_code}) after {time_taken:.1f}s", file=sys.stderr)

                return {
                    'accessible': True,
                    'status_code': response.status_code,
                    'time_taken': time_taken,
                    'url': url
                }
            else:
                last_error = f"HTTP {response.status_code}"

        except requests.exceptions.ConnectionError as e:
            last_error = "Connection refused"
        except requests.exceptions.Timeout as e:
            last_error = "Timeout"
        except requests.exceptions.RequestException as e:
            last_error = str(e)

        if verbose:
            elapsed = time.time() - start_time
            print(f"  Retrying... ({elapsed:.1f}s elapsed, last error: {last_error})", file=sys.stderr)

        time.sleep(delay)
        delay = min(delay * 1.5, 5)  # Exponential backoff, max 5s

    # Timeout reached
    time_taken = time.time() - start_time
    if verbose:
        print(f"✗ Not accessible after {time_taken:.1f}s", file=sys.stderr)

    return {
        'accessible': False,
        'error': last_error or 'Timeout',
        'time_taken': time_taken,
        'url': url
    }


def main():
    parser = argparse.ArgumentParser(description='Health check for application URL')
    parser.add_argument('--url', required=True, help='URL to check')
    parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds (default: 30)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print progress messages')

    args = parser.parse_args()

    # Validate URL
    parsed = urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        print(json.dumps({
            'accessible': False,
            'error': 'Invalid URL format'
        }))
        return 1

    result = health_check(args.url, timeout=args.timeout, verbose=args.verbose)

    # Output JSON to stdout
    print(json.dumps(result, indent=2))

    # Return exit code
    return 0 if result['accessible'] else 1


if __name__ == '__main__':
    sys.exit(main())
