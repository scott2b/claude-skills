---
name: obsidian
description: PROACTIVELY use for Obsidian vault operations. Fast search using ripgrep, direct file operations (read/write/delete). Works with slipbox in _Slipbox directory. 4-7x faster than API. Use obsidian-api skill ONLY for Dataview queries, periodic notes, or patch operations.
---

# Obsidian Vault Operations

Fast vault operations using ripgrep and direct filesystem access.

**No Obsidian process required. No API plugins required.**

## Overview

This is the **default skill** for Obsidian vault operations. It provides direct filesystem access for maximum speed and simplicity.

**Performance**: 4-7x faster than API for search, 50x faster for file operations.

## When to Use This Skill

**PROACTIVELY use this skill when:**
- User mentions "Obsidian", "vault", "slipbox", or "notes"
- User asks to search, read, create, or modify notes
- User wants to work with the slipbox (located in `_Slipbox/`)
- User needs fast operations on markdown files

**This is the PRIMARY Obsidian skill.** Only use `obsidian-api` for specialized features (Dataview, periodic notes, patch operations).

## Prerequisites

- **ripgrep** installed (`brew install ripgrep` on macOS)
- **Vault path** set via `OBSIDIAN_VAULT_PATH` env var (or auto-detected)

## Core Operations

### Search Vault
```bash
python scripts/search_vault.py "search term" --path "_Slipbox/"
```

### Read Notes
```bash
python scripts/read_note.py "Note.md" [--metadata]
```

### Write Notes
```bash
python scripts/write_note.py "Note.md" --content "Content"
```

### Other Operations
- `append_note.py` - Append to files
- `list_files.py` - List directory contents
- `delete_note.py` - Delete files

## Key Features

✅ Supported:
- YAML frontmatter parsing
- Inline tags (#tag)
- Wikilinks ([[link]])
- Fast full-text search
- Direct file operations

❌ Not Supported (use obsidian-api skill):
- Dataview queries
- Periodic notes
- Complex metadata queries

## Examples

**Search slipbox:**
```python
python scripts/search_vault.py "emergence" --path "_Slipbox/" --context 2
```

**Read with metadata:**
```python
python scripts/read_note.py "Note.md" --metadata
```

**Batch operations:**
Use vault_ops.py as a library for scripting.

## Performance

- Search: 7x faster than API
- Read: 50x faster than API
- Write: 50x faster than API
- No HTTP overhead
- No Obsidian process required

