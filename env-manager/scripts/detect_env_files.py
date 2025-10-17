#!/usr/bin/env python3
"""
Detect and analyze .env files in the project.

Usage:
    python detect_env_files.py [--dir /path/to/project]

Returns JSON list of found .env files with metadata.
"""

import sys
import json
import argparse
from pathlib import Path


# Import shared functions from check_env
sys.path.insert(0, str(Path(__file__).parent))
from check_env import find_env_files


def main():
    parser = argparse.ArgumentParser(description='Detect .env files')
    parser.add_argument('--dir', help='Directory to search (default: current directory)', type=Path)

    args = parser.parse_args()

    start_dir = args.dir or Path.cwd()
    env_files = find_env_files(start_dir)

    print(json.dumps(env_files, indent=2))

    return 0


if __name__ == '__main__':
    sys.exit(main())
