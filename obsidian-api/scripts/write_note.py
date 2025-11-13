#!/usr/bin/env python3
"""
Create or update a note in Obsidian vault.

Usage:
    python write_note.py FILE --content CONTENT [--stdin]

Examples:
    # Create note with content
    python write_note.py "New Note.md" --content "# New Note\n\nContent here"

    # Create in slipbox
    python write_note.py "_Slipbox/concept.md" --content "# Concept\n\nDetails..."

    # Read content from stdin
    echo "# Note\nContent" | python write_note.py "Note.md" --stdin

    # Update existing note (overwrites)
    python write_note.py "Existing.md" --content "# Updated\n\nNew content"
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def write_note(filepath: str, content: str):
    """Create or update note"""
    api = get_api()

    try:
        api.create_or_update_file(filepath, content)
        print(f"✓ Note written: {filepath}")

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Create or update note in Obsidian vault',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('file', help='Note file path (relative to vault root)')
    parser.add_argument('--content', help='Note content')
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

    write_note(args.file, content)


if __name__ == '__main__':
    main()
