#!/usr/bin/env python3
"""
Delete a note from Obsidian vault.

Usage:
    python delete_note.py FILE [--force]

Examples:
    # Delete with confirmation prompt
    python delete_note.py "Old Note.md"

    # Force delete without confirmation
    python delete_note.py "Temp.md" --force

    # Delete from slipbox
    python delete_note.py "_Slipbox/obsolete.md" --force
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def delete_note(filepath: str, force: bool = False):
    """Delete note with optional confirmation"""
    api = get_api()

    if not force:
        # Prompt for confirmation
        response = input(f"Delete '{filepath}'? (y/N): ")
        if response.lower() not in ('y', 'yes'):
            print("Cancelled")
            return

    try:
        api.delete_file(filepath)
        print(f"✓ Deleted: {filepath}")

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Delete note from Obsidian vault',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('file', help='Note file path to delete (relative to vault root)')
    parser.add_argument('--force', action='store_true',
                       help='Delete without confirmation prompt')

    args = parser.parse_args()
    delete_note(args.file, args.force)


if __name__ == '__main__':
    main()
