#!/usr/bin/env python3
"""
Get recent periodic notes.

Usage:
    python recent_notes.py PERIOD [--limit N] [--include-content] [--format FORMAT]

Examples:
    # Get last 7 daily notes
    python recent_notes.py daily --limit 7

    # Get last 4 weekly notes with content
    python recent_notes.py weekly --limit 4 --include-content

    # Get recent monthly notes as JSON
    python recent_notes.py monthly --format json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def get_recent_notes(period: str, limit: int = 10, include_content: bool = False,
                    output_format: str = 'text'):
    """Get recent periodic notes"""
    api = get_api()

    try:
        notes = api.get_recent_periodic_notes(period, limit, include_content)

        if output_format == 'json':
            print(json.dumps(notes, indent=2))
            return

        # Text output
        if not notes:
            print(f"No recent {period} notes found")
            return

        print(f"Recent {period} notes ({len(notes)}):\n")

        for i, note in enumerate(notes, 1):
            filename = note.get('filename', note.get('path', 'Unknown'))
            print(f"[{i}] {filename}")

            if include_content and 'content' in note:
                print("-" * 40)
                print(note['content'])
                print("-" * 40)

            print()

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Get recent periodic notes from Obsidian',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('period',
                       choices=['daily', 'weekly', 'monthly', 'quarterly', 'yearly'],
                       help='Period type')
    parser.add_argument('--limit', type=int, default=10,
                       help='Number of notes to retrieve (default: 10)')
    parser.add_argument('--include-content', action='store_true',
                       help='Include note content in results')
    parser.add_argument('--format', choices=['text', 'json'],
                       default='text', help='Output format (default: text)')

    args = parser.parse_args()
    get_recent_notes(args.period, args.limit, args.include_content, args.format)


if __name__ == '__main__':
    main()
