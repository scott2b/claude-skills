#!/usr/bin/env python3
"""
Read one or more notes from vault.

Usage:
    python read_note.py FILE [FILE ...] [--format FORMAT]

Examples:
    # Read single note
    python read_note.py "My Note.md"

    # Read from slipbox
    python read_note.py "_Slipbox/concept.md"

    # Read multiple notes
    python read_note.py "Note1.md" "Note2.md" "Note3.md"

    # JSON output
    python read_note.py "Note.md" --format json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_ops import read_file, parse_frontmatter, VaultError, get_vault_path


def read_notes(filepaths: list, output_format: str = 'text', show_metadata: bool = False):
    """Read and display note contents"""

    try:
        vault_path = get_vault_path()
    except VaultError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    results = []

    for filepath in filepaths:
        try:
            content = read_file(filepath, vault_path=vault_path)

            if show_metadata:
                metadata, body = parse_frontmatter(content)
                results.append({
                    'filename': filepath,
                    'metadata': metadata,
                    'content': body
                })
            else:
                results.append({
                    'filename': filepath,
                    'content': content
                })

        except VaultError as e:
            print(f"ERROR reading {filepath}: {e}", file=sys.stderr)
            if len(filepaths) == 1:
                sys.exit(1)
            continue

    # Output
    if output_format == 'json':
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            if len(filepaths) > 1:
                print("=" * 80)
                print(f"File: {result['filename']}")
                print("=" * 80)

            if show_metadata and result.get('metadata'):
                print("Metadata:")
                print(json.dumps(result['metadata'], indent=2))
                print("\nContent:")

            print(result['content'])

            if len(filepaths) > 1:
                print()


def main():
    parser = argparse.ArgumentParser(
        description='Read notes from vault',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('files', nargs='+', metavar='FILE',
                       help='Note file(s) to read (relative to vault root)')
    parser.add_argument('--format', choices=['text', 'json'],
                       default='text', help='Output format (default: text)')
    parser.add_argument('--metadata', action='store_true',
                       help='Parse and show frontmatter metadata separately')

    args = parser.parse_args()
    read_notes(args.files, args.format, args.metadata)


if __name__ == '__main__':
    main()
