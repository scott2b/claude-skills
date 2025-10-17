#!/usr/bin/env python3
"""
Check if required environment variables are present.

Usage:
    python check_env.py --required VAR1,VAR2,VAR3
    python check_env.py --required VAR1,VAR2 --optional VAR3,VAR4

Returns JSON with status and missing variables.
"""

import os
import sys
import json
import argparse
from pathlib import Path


def detect_shell() -> str:
    """Detect the user's current shell."""
    shell = os.environ.get('SHELL', '')
    if 'fish' in shell:
        return 'fish'
    elif 'zsh' in shell:
        return 'zsh'
    elif 'bash' in shell:
        return 'bash'
    else:
        return 'sh'


def find_env_files(start_dir: Path = None) -> list[dict]:
    """
    Find .env files in the project directory.

    Returns list of dicts with file info.
    """
    if start_dir is None:
        start_dir = Path.cwd()

    env_files = []

    # Common .env file names
    candidates = [
        '.env',
        '.env.local',
        '.env.test',
        '.env.development',
        '.env.production',
        '.env.fish',
    ]

    # Search current directory and parent directories
    current = start_dir
    searched = set()

    while current != current.parent and current not in searched:
        searched.add(current)

        for candidate in candidates:
            env_file = current / candidate
            if env_file.exists():
                # Analyze file format
                file_format = analyze_env_file_format(env_file)
                load_command = get_load_command(env_file, file_format)

                env_files.append({
                    'path': str(env_file),
                    'name': candidate,
                    'format': file_format,
                    'load_command': load_command,
                })

        # Stop at git root or when we find .env files
        if (current / '.git').exists() or env_files:
            break

        current = current.parent

    return env_files


def analyze_env_file_format(file_path: Path) -> str:
    """
    Analyze an env file to determine its format.

    Returns: 'shell' (export VAR=val), 'simple' (VAR=val), 'fish' (set -x VAR val)
    """
    try:
        with open(file_path) as f:
            lines = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

        if not lines:
            return 'empty'

        # Check first few lines for format indicators
        sample_lines = lines[:10]

        # Fish format
        if any(line.startswith('set -x ') or line.startswith('set -gx ') for line in sample_lines):
            return 'fish'

        # Shell format (export)
        if any(line.startswith('export ') for line in sample_lines):
            return 'shell'

        # Simple format (VAR=value)
        if any('=' in line and not line.startswith('export ') for line in sample_lines):
            return 'simple'

        return 'unknown'
    except Exception:
        return 'error'


def get_load_command(file_path: Path, file_format: str) -> str:
    """Get the appropriate command to load an env file."""
    shell = detect_shell()

    if file_format == 'fish':
        return f'source {file_path}'
    elif file_format == 'shell':
        return f'source {file_path}'
    elif file_format == 'simple':
        # For simple format, suggest different approaches
        if shell == 'fish':
            return f'# Convert to fish format or use: while read line; set -gx (echo $line | string split "="); end < {file_path}'
        else:
            # Check if dotenv is available
            return f'set -a; source {file_path}; set +a  # Or use: dotenv -f {file_path} <command>'
    else:
        return f'# Unknown format: {file_path}'


def check_required_vars(required: list[str], optional: list[str] = None) -> dict:
    """
    Check if required and optional environment variables are set.

    Returns dict with status info.
    """
    optional = optional or []

    missing_required = [var for var in required if not os.environ.get(var)]
    missing_optional = [var for var in optional if not os.environ.get(var)]
    present_required = [var for var in required if os.environ.get(var)]
    present_optional = [var for var in optional if os.environ.get(var)]

    all_present = len(missing_required) == 0

    result = {
        'all_present': all_present,
        'missing_required': missing_required,
        'missing_optional': missing_optional,
        'present_required': present_required,
        'present_optional': present_optional,
        'shell': detect_shell(),
    }

    # If variables are missing, suggest env files
    if not all_present:
        env_files = find_env_files()
        result['env_files_found'] = env_files

        if env_files:
            result['suggestion'] = f"Found .env files. Try loading one:\n" + "\n".join(
                f"  {f['load_command']}" for f in env_files
            )
        else:
            shell = detect_shell()
            if shell == 'fish':
                result['suggestion'] = "Set variables with: set -x VAR value"
            else:
                result['suggestion'] = "Set variables with: export VAR=value"

    return result


def main():
    parser = argparse.ArgumentParser(description='Check environment variables')
    parser.add_argument('--required', help='Comma-separated list of required variables')
    parser.add_argument('--optional', help='Comma-separated list of optional variables')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    required = args.required.split(',') if args.required else []
    optional = args.optional.split(',') if args.optional else []

    result = check_required_vars(required, optional)

    if args.json or True:  # Always output JSON for easy parsing
        print(json.dumps(result, indent=2))
    else:
        if result['all_present']:
            print("✓ All required environment variables are set")
        else:
            print("✗ Missing required environment variables:")
            for var in result['missing_required']:
                print(f"  - {var}")

            if result.get('suggestion'):
                print(f"\n{result['suggestion']}")

    return 0 if result['all_present'] else 1


if __name__ == '__main__':
    sys.exit(main())
