#!/usr/bin/env python3
"""
Read one or more notes from Obsidian vault.

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
from obsidian_api import get_api, ObsidianAPIError


def read_notes(filepaths: list, output_format: str = 'text'):
    """Read and display note contents"""
    api = get_api()
    results = {}

    try:
        for filepath in filepaths:
            try:
                content = api.get_file_content(filepath)
                results[filepath] = content

                if output_format == 'text':
                    print(f"{'='*80}")
                    print(f"File: {filepath}")
                    print(f"{'='*80}")
                    print(content)
                    print()

            except ObsidianAPIError as e:
                if output_format == 'text':
                    print(f"ERROR reading {filepath}: {e}", file=sys.stderr)
                results[filepath] = None

        if output_format == 'json':
            print(json.dumps(results, indent=2))

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Read notes from Obsidian vault',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('files', nargs='+', metavar='FILE',
                       help='Note file(s) to read (relative to vault root)')
    parser.add_argument('--format', choices=['text', 'json', 'markdown'],
                       default='text', help='Output format (default: text)')

    args = parser.parse_args()
    read_notes(args.files, args.format)


if __name__ == '__main__':
    main()
