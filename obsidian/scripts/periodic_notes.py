#!/usr/bin/env python3
"""
Get current periodic note (daily, weekly, monthly, etc.).

Usage:
    python periodic_notes.py PERIOD [--format FORMAT]

Examples:
    # Get today's daily note
    python periodic_notes.py daily

    # Get this week's weekly note
    python periodic_notes.py weekly

    # Get this month's monthly note
    python periodic_notes.py monthly

    # Get as JSON
    python periodic_notes.py daily --format json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def get_periodic_note(period: str, output_format: str = 'text'):
    """Get current periodic note"""
    api = get_api()

    try:
        content = api.get_periodic_note(period)

        if output_format == 'json':
            print(json.dumps({'period': period, 'content': content}, indent=2))
        else:
            print(f"{'='*80}")
            print(f"{period.capitalize()} Note")
            print(f"{'='*80}")
            print(content)

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Get current periodic note from Obsidian',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('period',
                       choices=['daily', 'weekly', 'monthly', 'quarterly', 'yearly'],
                       help='Period type')
    parser.add_argument('--format', choices=['text', 'json'],
                       default='text', help='Output format (default: text)')

    args = parser.parse_args()
    get_periodic_note(args.period, args.format)


if __name__ == '__main__':
    main()
