#!/usr/bin/env python3
"""
Core vault operations using ripgrep and direct filesystem access.

This replaces the Obsidian REST API with faster, simpler operations:
- ripgrep for searching
- Direct filesystem for file operations
- Simple parsing for frontmatter

No dependencies on Obsidian running or API plugins.
"""

import os
import subprocess
import json
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple


class VaultError(Exception):
    """Base exception for vault operations"""
    pass


def get_vault_path() -> str:
    """
    Get vault path from environment or Obsidian config.

    Priority:
    1. OBSIDIAN_VAULT_PATH environment variable
    2. Auto-detect from obsidian.json

    Returns:
        Absolute path to vault

    Raises:
        VaultError: If vault path cannot be determined
    """
    # Try environment variable first
    vault_path = os.environ.get('OBSIDIAN_VAULT_PATH')
    if vault_path and os.path.exists(vault_path):
        return os.path.abspath(vault_path)

    # Try to detect from Obsidian config
    obsidian_config = os.path.expanduser(
        "~/Library/Application Support/obsidian/obsidian.json"
    )

    if os.path.exists(obsidian_config):
        try:
            with open(obsidian_config) as f:
                config = json.load(f)

            vaults = config.get('vaults', {})
            if vaults:
                # Get first vault (or the open one)
                for vault_id, vault_info in vaults.items():
                    vault_path = vault_info.get('path')
                    if vault_path and os.path.exists(vault_path):
                        return os.path.abspath(vault_path)
        except Exception as e:
            pass

    raise VaultError(
        "Cannot determine vault path. Set OBSIDIAN_VAULT_PATH environment variable "
        "or ensure Obsidian config exists at ~/Library/Application Support/obsidian/obsidian.json"
    )


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, Any]], str]:
    """
    Parse YAML frontmatter from markdown text.

    Simple parser that handles:
    - String values: key: value
    - List values: key:\n  - item1\n  - item2

    Args:
        text: Markdown content

    Returns:
        Tuple of (metadata dict or None, content without frontmatter)
    """
    lines = text.split('\n')

    # Check for frontmatter
    if not lines or lines[0].strip() != '---':
        return None, text

    # Find closing ---
    try:
        end_idx = lines[1:].index('---') + 1
    except ValueError:
        return None, text

    frontmatter_lines = lines[1:end_idx]
    content = '\n'.join(lines[end_idx + 1:])

    # Parse frontmatter
    metadata = {}
    current_key = None
    current_list = []

    for line in frontmatter_lines:
        line = line.rstrip()

        # New key-value pair
        if line and not line.startswith(' ') and ':' in line:
            # Save previous list if any
            if current_key and current_list:
                metadata[current_key] = current_list
                current_list = []

            # Parse new key
            key, value = line.split(':', 1)
            current_key = key.strip()
            value = value.strip()

            if value:
                metadata[current_key] = value

        # List item
        elif line.startswith('  - ') or line.startswith('- '):
            item = line.lstrip('- ').strip()
            current_list.append(item)

    # Save last list
    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata, content


def format_frontmatter(metadata: Dict[str, Any]) -> str:
    """
    Format metadata dict as YAML frontmatter.

    Args:
        metadata: Dictionary of metadata

    Returns:
        Formatted YAML frontmatter with --- delimiters
    """
    if not metadata:
        return ""

    lines = ['---']

    for key, value in metadata.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")

    lines.append('---')
    return '\n'.join(lines)


# File Operations

def list_files(path: str, vault_path: Optional[str] = None) -> List[str]:
    """
    List markdown files in a directory.

    Args:
        path: Directory path (relative to vault or absolute)
        vault_path: Vault root path (auto-detected if not provided)

    Returns:
        List of file paths relative to vault
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Make absolute path
    if not os.path.isabs(path):
        path = os.path.join(vault_path, path)

    if not os.path.exists(path):
        raise VaultError(f"Path does not exist: {path}")

    if not os.path.isdir(path):
        raise VaultError(f"Path is not a directory: {path}")

    files = []
    for item in os.listdir(path):
        if item.endswith('.md'):
            full_path = os.path.join(path, item)
            rel_path = os.path.relpath(full_path, vault_path)
            files.append(rel_path)

    return sorted(files)


def read_file(filepath: str, vault_path: Optional[str] = None) -> str:
    """
    Read file content.

    Args:
        filepath: File path (relative to vault or absolute)
        vault_path: Vault root path (auto-detected if not provided)

    Returns:
        File content as string
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Make absolute path
    if not os.path.isabs(filepath):
        filepath = os.path.join(vault_path, filepath)

    if not os.path.exists(filepath):
        raise VaultError(f"File does not exist: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath: str, content: str, vault_path: Optional[str] = None) -> None:
    """
    Write content to file.

    Args:
        filepath: File path (relative to vault or absolute)
        content: Content to write
        vault_path: Vault root path (auto-detected if not provided)
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Make absolute path
    if not os.path.isabs(filepath):
        filepath = os.path.join(vault_path, filepath)

    # Create directory if needed
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def append_file(filepath: str, content: str, vault_path: Optional[str] = None) -> None:
    """
    Append content to file.

    Args:
        filepath: File path (relative to vault or absolute)
        content: Content to append
        vault_path: Vault root path (auto-detected if not provided)
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Make absolute path
    if not os.path.isabs(filepath):
        filepath = os.path.join(vault_path, filepath)

    if not os.path.exists(filepath):
        raise VaultError(f"File does not exist: {filepath}")

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)


def delete_file(filepath: str, vault_path: Optional[str] = None) -> None:
    """
    Delete file.

    Args:
        filepath: File path (relative to vault or absolute)
        vault_path: Vault root path (auto-detected if not provided)
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Make absolute path
    if not os.path.isabs(filepath):
        filepath = os.path.join(vault_path, filepath)

    if not os.path.exists(filepath):
        raise VaultError(f"File does not exist: {filepath}")

    os.remove(filepath)


# Search Operations

def search(
    query: str,
    path: Optional[str] = None,
    vault_path: Optional[str] = None,
    case_sensitive: bool = False,
    files_only: bool = False,
    context_lines: int = 0
) -> List[Dict[str, Any]]:
    """
    Search vault using ripgrep.

    Args:
        query: Search term or regex pattern
        path: Directory to search (relative to vault or absolute)
        vault_path: Vault root path (auto-detected if not provided)
        case_sensitive: Whether search is case-sensitive
        files_only: Return only filenames (not matches with context)
        context_lines: Number of context lines to include

    Returns:
        List of matches. Each match is a dict with:
        - filename: Path relative to vault
        - line_number: Line number (if files_only=False)
        - line: Matching line (if files_only=False)
        - context_before: Lines before match (if context_lines > 0)
        - context_after: Lines after match (if context_lines > 0)
    """
    if vault_path is None:
        vault_path = get_vault_path()

    # Determine search path
    if path:
        if not os.path.isabs(path):
            search_path = os.path.join(vault_path, path)
        else:
            search_path = path
    else:
        search_path = vault_path

    if not os.path.exists(search_path):
        raise VaultError(f"Search path does not exist: {search_path}")

    # Build ripgrep command
    cmd = ['rg', '--type', 'md']

    if not case_sensitive:
        cmd.append('-i')

    if files_only:
        cmd.append('-l')
    else:
        cmd.append('-n')  # Show line numbers
        if context_lines > 0:
            cmd.extend(['-C', str(context_lines)])

    cmd.extend([query, search_path])

    # Run ripgrep
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
    except subprocess.TimeoutExpired:
        raise VaultError("Search timed out after 30 seconds")
    except FileNotFoundError:
        raise VaultError("ripgrep (rg) not found. Please install ripgrep.")

    # Parse results
    if result.returncode == 1:
        # No matches found (normal)
        return []
    elif result.returncode != 0:
        raise VaultError(f"ripgrep error: {result.stderr}")

    matches = []

    if files_only:
        # Just filenames
        for line in result.stdout.strip().split('\n'):
            if line:
                filepath = os.path.relpath(line, vault_path)
                matches.append({'filename': filepath})
    else:
        # Parse line-by-line results
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue

            # Format: filename:line_number:content
            parts = line.split(':', 2)
            if len(parts) >= 3:
                filepath = os.path.relpath(parts[0], vault_path)
                line_number = int(parts[1])
                content = parts[2]

                matches.append({
                    'filename': filepath,
                    'line_number': line_number,
                    'line': content
                })

    return matches


def search_by_tag(
    tag: str,
    path: Optional[str] = None,
    vault_path: Optional[str] = None
) -> List[str]:
    """
    Search for files containing a specific tag.

    Searches both:
    - Inline tags: #tagname
    - Frontmatter tags

    Args:
        tag: Tag name (without #)
        path: Directory to search (relative to vault or absolute)
        vault_path: Vault root path (auto-detected if not provided)

    Returns:
        List of file paths relative to vault
    """
    # Search for inline tag
    tag_pattern = f"#{tag}\\b"
    matches = search(
        tag_pattern,
        path=path,
        vault_path=vault_path,
        files_only=True
    )

    filenames = set(m['filename'] for m in matches)

    # Also search frontmatter (basic - looks for "tags:" then the tag name)
    frontmatter_matches = search(
        f"tags:.*{tag}",
        path=path,
        vault_path=vault_path,
        files_only=True
    )

    filenames.update(m['filename'] for m in frontmatter_matches)

    return sorted(list(filenames))


if __name__ == '__main__':
    # Quick test
    try:
        vault_path = get_vault_path()
        print(f"✓ Found vault: {vault_path}")

        # Test search
        results = search("test", files_only=True)
        print(f"✓ Search works ({len(results)} files found)")

    except VaultError as e:
        print(f"✗ Error: {e}")
