#!/usr/bin/env python3
"""
Search vault for notes containing specific text using ripgrep.

Usage:
    python search_vault.py "search term" [--path PATH] [--context N] [--format FORMAT]

Examples:
    # Search entire vault
    python search_vault.py "emergence"

    # Search only in slipbox
    python search_vault.py "systems thinking" --path "_Slipbox/"

    # Search with more context
    python search_vault.py "complex" --context 5

    # JSON output for scripting
    python search_vault.py "theory" --format json
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))
from vault_ops import search, VaultError, get_vault_path


def search_vault(query: str, path: str = None, context_lines: int = 0, output_format: str = 'text'):
    """Search vault and display results"""

    try:
        vault_path = get_vault_path()
    except VaultError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        # Perform search
        if output_format == 'files':
            # Just list matching files
            results = search(query, path=path, vault_path=vault_path, files_only=True)
            filenames = [r['filename'] for r in results]

            if output_format == 'json':
                print(json.dumps(filenames, indent=2))
            else:
                for filename in filenames:
                    print(filename)

        elif output_format == 'json':
            # Full results as JSON
            results = search(query, path=path, vault_path=vault_path, context_lines=context_lines)
            print(json.dumps(results, indent=2))

        else:
            # Text output with context
            results = search(query, path=path, vault_path=vault_path, context_lines=context_lines)

            if not results:
                print(f"No matches found for: {query}")
                return

            # Group by filename
            by_file = {}
            for match in results:
                filename = match['filename']
                if filename not in by_file:
                    by_file[filename] = []
                by_file[filename].append(match)

            print(f"Found matches in {len(by_file)} file(s) for: {query}\n")

            for i, (filename, matches) in enumerate(by_file.items(), 1):
                print(f"[{i}] {filename}")

                if context_lines > 0:
                    # Show matches with context
                    for match in matches[:5]:  # Limit to first 5 per file
                        print(f"  Line {match['line_number']}: {match['line']}")

                    if len(matches) > 5:
                        print(f"  ... and {len(matches) - 5} more matches")
                else:
                    # Just show count
                    print(f"  {len(matches)} match(es)")

                print()

    except VaultError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Search Obsidian vault for text using ripgrep',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('query', help='Search term or phrase')
    parser.add_argument('--path', help='Limit search to specific directory (e.g., "_Slipbox/")')
    parser.add_argument('--context', type=int, default=0,
                       help='Lines of context around match (default: 0)')
    parser.add_argument('--format', choices=['text', 'json', 'files'],
                       default='text', help='Output format (default: text)')
    parser.add_argument('--case-sensitive', action='store_true',
                       help='Case sensitive search')

    args = parser.parse_args()
    search_vault(args.query, args.path, args.context, args.format)


if __name__ == '__main__':
    main()
