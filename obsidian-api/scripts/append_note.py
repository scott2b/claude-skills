#!/usr/bin/env python3
"""
Append content to an existing note.

Usage:
    python append_note.py FILE --content CONTENT [--stdin]

Examples:
    # Append to note
    python append_note.py "Daily Note.md" --content "\n## New Section\n\nAdded content"

    # Append from stdin
    echo "\n## Update\n\nNew info" | python append_note.py "Note.md" --stdin

    # Append to slipbox note
    python append_note.py "_Slipbox/concept.md" --content "\n\n## Related\n- [[other-concept]]"
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def append_to_note(filepath: str, content: str):
    """Append content to note"""
    api = get_api()

    try:
        api.append_to_file(filepath, content)
        print(f"✓ Content appended to: {filepath}")

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Append content to Obsidian note',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('file', help='Note file path (relative to vault root)')
    parser.add_argument('--content', help='Content to append')
    parser.add_argument('--stdin', action='store_true',
                       help='Read content from stdin instead of --content')

    args = parser.parse_args()

    # Get content from stdin or argument
    if args.stdin:
        content = sys.stdin.read()
    elif args.content:
        content = args.content
    else:
        parser.error("Must provide either --content or --stdin")

    append_to_note(args.file, content)


if __name__ == '__main__':
    main()
