#!/usr/bin/env python3
"""
Insert content at a specific location in a note.

Usage:
    python patch_note.py FILE --content CONTENT [--heading HEADING | --block BLOCK]

Examples:
    # Insert after heading
    python patch_note.py "Note.md" --content "New paragraph" --heading "## Section"

    # Insert after block reference
    python patch_note.py "Note.md" --content "Addition" --block "block-id"

    # Insert from stdin
    echo "New content" | python patch_note.py "Note.md" --stdin --heading "## Intro"
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def patch_note(filepath: str, content: str, heading: str = None, block: str = None):
    """Insert content at specific location"""
    api = get_api()

    if not heading and not block:
        print("ERROR: Must specify either --heading or --block", file=sys.stderr)
        sys.exit(1)

    try:
        api.patch_file(filepath, content, heading=heading, block=block)
        target = f"heading '{heading}'" if heading else f"block '{block}'"
        print(f"✓ Content inserted after {target} in: {filepath}")

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Insert content at specific location in Obsidian note',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('file', help='Note file path (relative to vault root)')
    parser.add_argument('--content', help='Content to insert')
    parser.add_argument('--stdin', action='store_true',
                       help='Read content from stdin instead of --content')
    parser.add_argument('--heading', help='Insert after this heading (e.g., "## Section")')
    parser.add_argument('--block', help='Insert after this block reference (e.g., "block-id")')

    args = parser.parse_args()

    # Get content from stdin or argument
    if args.stdin:
        content = sys.stdin.read()
    elif args.content:
        content = args.content
    else:
        parser.error("Must provide either --content or --stdin")

    patch_note(args.file, content, args.heading, args.block)


if __name__ == '__main__':
    main()
