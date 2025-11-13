#!/usr/bin/env python3
"""
Create or update a project knowledge index.

This script scans a project directory and creates a comprehensive index
of files, content, and relationships to prevent constant searching/grepping.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

def scan_directory(root_path, extensions=None):
    """Scan directory and return file inventory."""
    if extensions is None:
        extensions = {'.md', '.py', '.js', '.ts', '.jsx', '.tsx', '.txt', '.json'}

    inventory = []
    root = Path(root_path)

    for path in root.rglob('*'):
        if path.is_file() and path.suffix in extensions:
            rel_path = path.relative_to(root)

            # Skip hidden files and common ignore patterns
            if any(part.startswith('.') for part in rel_path.parts):
                continue
            if 'node_modules' in rel_path.parts or '__pycache__' in rel_path.parts:
                continue

            inventory.append({
                'path': str(rel_path),
                'size': path.stat().st_size,
                'modified': datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                'extension': path.suffix
            })

    return sorted(inventory, key=lambda x: x['path'])

def generate_index_markdown(inventory, project_name):
    """Generate markdown index from inventory."""
    lines = [
        f"# {project_name} - Project Knowledge Index",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Total Files:** {len(inventory)}",
        "",
        "---",
        "",
        "## Purpose",
        "",
        "This index prevents constant searching and grepping by maintaining systematic knowledge",
        "of what exists in the project. UPDATE THIS INDEX as work progresses.",
        "",
        "---",
        "",
        "## File Registry",
        "",
    ]

    # Group by extension
    by_extension = {}
    for item in inventory:
        ext = item['extension']
        by_extension.setdefault(ext, []).append(item)

    for ext in sorted(by_extension.keys()):
        lines.append(f"### {ext} files ({len(by_extension[ext])})")
        lines.append("")
        for item in by_extension[ext]:
            size_kb = item['size'] / 1024
            lines.append(f"- `{item['path']}` - {size_kb:.1f}KB - Modified: {item['modified'][:10]}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Content Summary",
        "",
        "**TODO**: Fill this section as you work with files:",
        "",
        "### Key Files",
        "- File: Purpose and current state",
        "- File: Purpose and current state",
        "",
        "### Cross-References",
        "- File A references File B for reason X",
        "- File C depends on File D",
        "",
        "### Completion Status",
        "- [ ] Component A",
        "- [ ] Component B",
        "",
        "---",
        "",
        "## Project-Specific Notes",
        "",
        "**TODO**: Add project-specific knowledge:",
        "",
        "### Important Decisions",
        "- Decision: Rationale",
        "",
        "### Patterns Identified",
        "- Pattern: Description",
        "",
        "### Known Issues",
        "- Issue: Status",
        "",
    ])

    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_index.py <project_directory> [output_file]")
        sys.exit(1)

    project_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "PROJECT-INDEX.md"

    if not os.path.isdir(project_dir):
        print(f"Error: {project_dir} is not a directory")
        sys.exit(1)

    print(f"Scanning {project_dir}...")
    inventory = scan_directory(project_dir)
    print(f"Found {len(inventory)} files")

    project_name = Path(project_dir).name
    markdown = generate_index_markdown(inventory, project_name)

    output_path = Path(project_dir) / output_file
    output_path.write_text(markdown)
    print(f"Index created at: {output_path}")

if __name__ == '__main__':
    main()
