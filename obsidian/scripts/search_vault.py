#!/usr/bin/env python3
"""
Search vault for notes containing specific text.

Usage:
    python search_vault.py "search term" [--path PATH] [--context N] [--format FORMAT]

Examples:
    # Search entire vault
    python search_vault.py "emergence"

    # Search only in slipbox
    python search_vault.py "systems thinking" --path "_Slipbox/"

    # Search with more context
    python search_vault.py "complex" --context 200

    # JSON output for scripting
    python search_vault.py "theory" --format json
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path to import obsidian_api
sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def search_vault(query: str, path: str = None, context_length: int = 100, output_format: str = 'text'):
    """Search vault and display results"""
    api = get_api()

    try:
        # Perform search
        results = api.simple_search(query, context_length)

        if output_format == 'json':
            print(json.dumps(results, indent=2))
            return

        # Text output
        # Handle both list and dict responses from API
        if isinstance(results, list):
            matches = results
        elif isinstance(results, dict) and 'results' in results:
            matches = results['results']
        else:
            print(f"No matches found for: {query}")
            return

        if not matches:
            print(f"No matches found for: {query}")
            return

        # Filter by path if specified
        if path:
            matches = [m for m in matches if m.get('filename', '').startswith(path)]

        if not matches:
            print(f"No matches found in path: {path}")
            return

        print(f"Found {len(matches)} match(es) for: {query}\n")

        for i, match in enumerate(matches, 1):
            filename = match.get('filename', 'Unknown')
            print(f"[{i}] {filename}")

            # Show context matches
            if 'matches' in match:
                for m in match['matches']:
                    # Try both possible locations for context
                    context = m.get('context', '') or m.get('match', {}).get('context', '')
                    if context:
                        # Indent and show context
                        lines = context.split('\n')
                        for line in lines:
                            if line.strip():
                                print(f"    {line}")
                    print()

            print("-" * 80)

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Search Obsidian vault for text',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('query', help='Search term or phrase')
    parser.add_argument('--path', help='Limit search to specific directory (e.g., "_Slipbox/")')
    parser.add_argument('--context', type=int, default=100,
                       help='Characters of context around match (default: 100)')
    parser.add_argument('--format', choices=['text', 'json', 'markdown'],
                       default='text', help='Output format (default: text)')

    args = parser.parse_args()
    search_vault(args.query, args.path, args.context, args.format)


if __name__ == '__main__':
    main()
