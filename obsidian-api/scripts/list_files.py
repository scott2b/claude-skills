#!/usr/bin/env python3
"""
List files in Obsidian vault.

Usage:
    python list_files.py [--path PATH] [--format FORMAT] [--recursive]

Examples:
    # List all files in vault root
    python list_files.py

    # List files in slipbox
    python list_files.py --path "_Slipbox/"

    # List files in specific directory
    python list_files.py --path "Projects/Active/"

    # JSON output
    python list_files.py --format json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from obsidian_api import get_api, ObsidianAPIError


def list_files(path: str = None, output_format: str = 'text', recursive: bool = False):
    """List files in vault or directory"""
    api = get_api()

    try:
        if path:
            files = api.list_directory_files(path)
            location = path
        else:
            files = api.list_vault_files()
            location = "vault root"

        if output_format == 'json':
            print(json.dumps(files, indent=2))
            return

        # Text output
        if not files:
            print(f"No files found in {location}")
            return

        print(f"Files in {location} ({len(files)} total):\n")

        # Separate files and directories
        dirs = [f for f in files if f.get('type') == 'folder' or f.get('folder', False)]
        docs = [f for f in files if f.get('type') == 'file' or not f.get('folder', False)]

        # Show directories first
        if dirs:
            print("Directories:")
            for d in sorted(dirs, key=lambda x: x.get('path', x.get('name', ''))):
                name = d.get('name', d.get('path', 'Unknown'))
                print(f"  📁 {name}/")
            print()

        # Show files
        if docs:
            print("Files:")
            for f in sorted(docs, key=lambda x: x.get('path', x.get('name', ''))):
                name = f.get('name', f.get('path', 'Unknown'))
                print(f"  📄 {name}")

    except ObsidianAPIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='List files in Obsidian vault',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--path', help='Directory path (default: vault root)')
    parser.add_argument('--format', choices=['text', 'json'],
                       default='text', help='Output format (default: text)')
    parser.add_argument('--recursive', action='store_true',
                       help='List files recursively (not yet implemented)')

    args = parser.parse_args()

    if args.recursive:
        print("WARNING: --recursive not yet implemented", file=sys.stderr)

    list_files(args.path, args.format, args.recursive)


if __name__ == '__main__':
    main()
