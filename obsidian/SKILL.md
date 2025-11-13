---
name: obsidian
description: PROACTIVELY use when work is required in Obsidian, the vault, or the slipbox. Provides comprehensive vault operations via Obsidian Local REST API including search, file operations, and slipbox-aware workflows. The slipbox is located in the _Slipbox directory within the vault.
---

# Obsidian Vault Manager

This skill provides comprehensive access to your Obsidian vault via the Obsidian Local REST API. It enables searching, reading, writing, and managing notes programmatically while maintaining awareness of special directories like the slipbox.

## Prerequisites

**REQUIRED**: Install and configure the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin:

1. In Obsidian: Settings → Community Plugins → Browse
2. Search for "Local REST API" and install
3. Enable the plugin
4. Copy the API key from plugin settings
5. Note the server URL (default: https://127.0.0.1:27124)

**No Python dependencies required** - uses only Python standard library (urllib, ssl, json).

**Environment Variables**:
```bash
export OBSIDIAN_API_KEY=your_api_key_here
export OBSIDIAN_HOST=https://127.0.0.1:27124  # Optional, defaults to this
```

Store these in a `.env` file for persistence:
```bash
# .env or .env.obsidian
export OBSIDIAN_API_KEY=your_api_key_here
export OBSIDIAN_HOST=https://127.0.0.1:27124
```

Then load with: `source .env`

## When to Use This Skill

**AUTOMATICALLY use this skill when:**
- User mentions "Obsidian", "vault", "slipbox", or "notes"
- User asks to search, read, create, or modify notes
- User wants to work with the slipbox (located in `_Slipbox/`)
- User asks about note content, connections, or metadata
- User requests periodic notes (daily, weekly, monthly, etc.)
- User wants to find recently modified notes
- User asks to append content or update existing notes

**DO NOT wait for explicit requests** - if the user is clearly working with their Obsidian vault, invoke this skill proactively.

## Vault Structure Awareness

- **Main vault**: Root directory contains all notes
- **Slipbox**: Located at `_Slipbox/` within the vault
- All paths are relative to vault root
- Directories use trailing slashes: `_Slipbox/`, `Projects/`

## Helper Scripts

All operations are performed through Python helper scripts that interact with the Obsidian REST API:

- `scripts/obsidian_api.py` - Core API wrapper (don't call directly)
- `scripts/search_vault.py` - Search notes by content or metadata
- `scripts/read_note.py` - Read one or more note files
- `scripts/write_note.py` - Create or update notes
- `scripts/append_note.py` - Append content to existing notes
- `scripts/patch_note.py` - Insert content relative to headings/blocks
- `scripts/list_files.py` - List files in vault or directory
- `scripts/delete_note.py` - Delete notes (use with caution)
- `scripts/periodic_notes.py` - Get daily/weekly/monthly notes
- `scripts/recent_notes.py` - Find recently modified notes

## Common Operations

### Search the Vault

Search all notes (including slipbox):
```bash
python ~/.claude/skills/obsidian/scripts/search_vault.py "search term" --context 100
```

Search only in slipbox:
```bash
python ~/.claude/skills/obsidian/scripts/search_vault.py "search term" --path "_Slipbox/"
```

### Read Notes

Read a single note:
```bash
python ~/.claude/skills/obsidian/scripts/read_note.py "Note Title.md"
```

Read multiple notes:
```bash
python ~/.claude/skills/obsidian/scripts/read_note.py "Note 1.md" "Note 2.md" "Note 3.md"
```

Read from slipbox:
```bash
python ~/.claude/skills/obsidian/scripts/read_note.py "_Slipbox/concept.md"
```

### Create or Update Notes

Create a new note:
```bash
python ~/.claude/skills/obsidian/scripts/write_note.py "New Note.md" --content "# New Note\n\nContent here"
```

Create in slipbox:
```bash
python ~/.claude/skills/obsidian/scripts/write_note.py "_Slipbox/new-concept.md" --content "# Concept\n\nDetails..."
```

### Append to Notes

Add content to end of note:
```bash
python ~/.claude/skills/obsidian/scripts/append_note.py "Daily Note.md" --content "\n## New Section\n\nAdded content"
```

### Insert Content at Specific Location

Insert after a heading:
```bash
python ~/.claude/skills/obsidian/scripts/patch_note.py "Note.md" \
  --content "New content" \
  --heading "Section Title"
```

Insert after a block reference:
```bash
python ~/.claude/skills/obsidian/scripts/patch_note.py "Note.md" \
  --content "New content" \
  --block "block-id"
```

### List Files

List all files in vault:
```bash
python ~/.claude/skills/obsidian/scripts/list_files.py
```

List files in slipbox:
```bash
python ~/.claude/skills/obsidian/scripts/list_files.py --path "_Slipbox/"
```

List specific directory:
```bash
python ~/.claude/skills/obsidian/scripts/list_files.py --path "Projects/Active/"
```

### Periodic Notes

Get today's daily note:
```bash
python ~/.claude/skills/obsidian/scripts/periodic_notes.py daily
```

Get this week's weekly note:
```bash
python ~/.claude/skills/obsidian/scripts/periodic_notes.py weekly
```

Get recent daily notes:
```bash
python ~/.claude/skills/obsidian/scripts/recent_notes.py daily --limit 7
```

### Delete Notes

Delete a note (prompts for confirmation):
```bash
python ~/.claude/skills/obsidian/scripts/delete_note.py "Old Note.md"
```

Force delete without confirmation:
```bash
python ~/.claude/skills/obsidian/scripts/delete_note.py "Old Note.md" --force
```

## Slipbox-Specific Workflows

The skill is aware that `_Slipbox/` is special and contains your Zettelkasten/slip-box notes.

### Search slipbox for concepts:
```bash
python ~/.claude/skills/obsidian/scripts/search_vault.py "emergence" --path "_Slipbox/" --context 200
```

### Create new slipbox note:
```bash
python ~/.claude/skills/obsidian/scripts/write_note.py "_Slipbox/202501131045-emergence-in-systems.md" \
  --content "# Emergence in Systems\n\nEmergence occurs when...\n\n## References\n- [[complex-systems]]\n- [[self-organization]]"
```

### List all slipbox notes:
```bash
python ~/.claude/skills/obsidian/scripts/list_files.py --path "_Slipbox/"
```

## Integration with Other Skills

This skill works well with:
- **slipbox-integration** - Links slipbox notes into narrative projects
- **narrative-inventory** - Can read/write inventories to vault
- **narrative-maps** - Can store spatial maps in vault
- **project-indexer** - Can maintain project indexes in vault

## Best Practices

1. **Always check environment first** - Use `env-manager` skill if API key is not set
2. **Use relative paths** - All paths are relative to vault root
3. **Include file extensions** - Always use `.md` for markdown files
4. **Respect slipbox structure** - Slipbox notes are in `_Slipbox/`
5. **Search before creating** - Check if note exists before creating new ones
6. **Use descriptive titles** - Especially for slipbox notes (e.g., `202501131045-concept-name.md`)
7. **Preserve links** - Maintain `[[wikilinks]]` when modifying notes
8. **Handle errors gracefully** - API may fail if Obsidian is closed

## Error Handling

Common issues:
- **Connection refused**: Obsidian is not running or REST API plugin is disabled
- **401 Unauthorized**: OBSIDIAN_API_KEY is incorrect or not set
- **404 Not Found**: File path doesn't exist in vault
- **SSL errors**: Set `OBSIDIAN_VERIFY_SSL=false` if using self-signed cert

## API Endpoints Reference

For transparency, here are the underlying REST API endpoints used:

| Operation | Endpoint | Method |
|-----------|----------|--------|
| List vault files | `/vault/` | GET |
| List directory | `/vault/{path}/` | GET |
| Read file | `/vault/{filepath}` | GET |
| Create/Update | `/vault/{filepath}` | POST |
| Patch content | `/vault/{filepath}` | PATCH |
| Delete file | `/vault/{filepath}` | DELETE |
| Simple search | `/search/simple/` | POST |
| Advanced search | `/search/` | POST |
| Get periodic note | `/periodic/{period}/` | GET |
| Recent periodic | `/periodic/{period}/recent` | GET |

All requests require `Authorization: Bearer {API_KEY}` header.

## Security Notes

- API key grants full vault access - treat as sensitive credential
- Store in environment variables, not in code
- Default server uses self-signed SSL certificate
- API only accessible on localhost by default
- No authentication beyond API key

## Troubleshooting

1. **Skill not working**: Check if REST API plugin is enabled in Obsidian
2. **Can't find notes**: Verify paths are relative to vault root, not filesystem
3. **SSL errors**: Add `--no-verify-ssl` flag to scripts if needed
4. **Empty results**: Obsidian may need to finish indexing vault
5. **Changes not visible**: Obsidian auto-reloads, but may need manual refresh

## Advanced Usage

### Complex Searches with JSONLogic

The API supports JSONLogic queries for advanced filtering:
```python
# Example: Find notes modified in last 7 days with tag #important
query = {
    "and": [
        {">=": [{"var": "mtime"}, 1704672000]},
        {"in": ["#important", {"var": "tags"}]}
    ]
}
```

See scripts source code for implementation details.

### Batch Operations

Read multiple files at once:
```bash
python ~/.claude/skills/obsidian/scripts/read_note.py \
  "Note1.md" "Note2.md" "Note3.md" \
  --format json
```

### Working with Templates

Store templates in vault and copy when creating notes:
```bash
# Read template
template=$(python ~/.claude/skills/obsidian/scripts/read_note.py "Templates/Note Template.md")

# Create note from template
python ~/.claude/skills/obsidian/scripts/write_note.py "New Note.md" --content "$template"
```

## Script Output Formats

Most scripts support `--format` flag:
- `text` (default) - Human-readable output
- `json` - Machine-readable JSON for scripting
- `markdown` - Formatted markdown

Example:
```bash
python ~/.claude/skills/obsidian/scripts/search_vault.py "term" --format json | jq
```
