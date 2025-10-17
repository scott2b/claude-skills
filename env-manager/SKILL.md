---
name: env-manager
description: PROACTIVELY use when environment variables are missing, scripts fail with "environment" or "variable not set" errors, or tasks require configuration (testing, API calls, deployment). Intelligently detects missing variables, finds .env files in project, analyzes formats (shell/simple/fish), and provides exact shell-specific commands to load configuration. Supports bash, zsh, fish. Use automatically at task start for any work requiring environment setup.
---

# Environment Manager

This skill provides intelligent environment variable management for Claude Code. It handles detection of missing variables, parsing of various .env file formats, and provides appropriate commands for different shells.

## When to Use This Skill

**AUTOMATICALLY use this skill when:**
- User asks to **test** anything (web pages, APIs, etc.) - testing ALWAYS needs environment
- User asks to **run** tests, **check** functionality, or **verify** pages work
- Starting tasks that need configuration (deployment, API integration, database work)
- Any script or command fails with environment-related errors
- You detect phrases like "missing", "not set", "required", "environment" in error messages
- User mentions specific pages to test (e.g., "test the billing page", "check the login form")
- Beginning work on web applications, APIs, or services

**CRITICAL: If the user says "test the X page" or similar, invoke this skill FIRST before writing any test code.**

**DO NOT wait for the user to ask** - proactively invoke this skill when environment issues are likely. DO NOT check for .env files or write environment loading code - that's what THIS skill does.

## Key Features

- **Shell Detection**: Automatically detects user's shell (bash, zsh, fish)
- **Format Recognition**: Understands multiple .env file formats:
  - Shell format: `export VAR=value`
  - Simple format: `VAR=value`
  - Commented files with `#` comments
- **Smart Loading**: Recommends the right tool for the job:
  - `source` for shell-formatted files
  - `export` for inline variable setting
  - `dotenv` command for simple format files (if available)
- **Project Awareness**: Searches project directory for .env files
- **Frictionless UX**: Provides copy-paste commands for users

## Helper Scripts

- `scripts/check_env.py` - Check if required environment variables are set
- `scripts/detect_env_files.py` - Find and analyze .env files in project
- `scripts/load_env.sh` - Shell script to load environment variables

## Usage Patterns

### Pattern 1: Check for Required Variables

```python
import subprocess
import json

result = subprocess.run(
    ['python', '~/.claude/skills/env-manager/scripts/check_env.py',
     '--required', 'VAR1,VAR2,VAR3'],
    capture_output=True,
    text=True
)
info = json.loads(result.stdout)

if not info['all_present']:
    # Handle missing variables
    print(f"Missing: {info['missing']}")
```

### Pattern 2: Find and Suggest .env Files

```python
result = subprocess.run(
    ['python', '~/.claude/skills/env-manager/scripts/detect_env_files.py'],
    capture_output=True,
    text=True
)
files = json.loads(result.stdout)

for file_info in files:
    print(f"Found: {file_info['path']}")
    print(f"Format: {file_info['format']}")
    print(f"Load command: {file_info['load_command']}")
```

## Environment File Formats

### Shell Format (Recommended)
```bash
# .env file
export DATABASE_URL=postgres://localhost/db
export API_KEY=secret123
export DEBUG=true
```
Load with: `source .env`

### Simple Format
```bash
# .env file
DATABASE_URL=postgres://localhost/db
API_KEY=secret123
DEBUG=true
```
Load with: `dotenv` command or manually set with `export`

### Fish Shell Format
```fish
# .env.fish file
set -x DATABASE_URL postgres://localhost/db
set -x API_KEY secret123
set -x DEBUG true
```
Load with: `source .env.fish`

## Integration with Other Skills

Other skills should delegate environment management to this skill:

```python
# In another skill's script
from pathlib import Path
import subprocess
import sys

# Check for required environment variables
check_cmd = [
    'python',
    str(Path.home() / '.claude/skills/env-manager/scripts/check_env.py'),
    '--required', 'VAR1,VAR2',
    '--role', 'user'
]

result = subprocess.run(check_cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("Environment not configured. Run env-manager skill first.")
    sys.exit(1)
```

## Best Practices

1. **Always check environment before running tasks** that require specific variables
2. **Provide clear feedback** about which variables are missing
3. **Suggest concrete commands** for users to run
4. **Respect user's shell choice** - don't assume bash
5. **Don't modify environment files** - only read and suggest

## Shell Compatibility

| Shell | Detection | .env Loading | Variable Setting |
|-------|-----------|--------------|------------------|
| bash  | ✓         | `source`     | `export VAR=val` |
| zsh   | ✓         | `source`     | `export VAR=val` |
| fish  | ✓         | `source`     | `set -x VAR val` |
| sh    | ✓         | `.`          | `export VAR=val` |
