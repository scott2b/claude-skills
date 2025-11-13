# Obsidian Vault Manager Skill

Comprehensive Obsidian vault integration for Claude Code via the Obsidian Local REST API.

## Quick Start

### Prerequisites

1. **Install Obsidian Local REST API Plugin**:
   - In Obsidian: Settings → Community Plugins → Browse
   - Search for "Local REST API" and install
   - Enable the plugin
   - Copy API key from plugin settings

2. **No External Dependencies Required**:
   - Uses Python's built-in `urllib` library
   - No need to install `requests` or other packages
   - Works with Python 3.6+

3. **Set Environment Variables**:
   ```bash
   export OBSIDIAN_API_KEY=your_api_key_here
   export OBSIDIAN_HOST=https://127.0.0.1:27124  # Optional, this is the default
   ```

   Or create a `.env` file:
   ```bash
   # .env.obsidian
   export OBSIDIAN_API_KEY=your_api_key_here
   export OBSIDIAN_HOST=https://127.0.0.1:27124
   ```

   Then load with: `source .env.obsidian`

### Verify Installation

```bash
python ~/.claude/skills/obsidian/scripts/obsidian_api.py
```

Should output: `✓ Connected to Obsidian vault (N files in root)`

## Features

- **Search**: Find notes by content with context
- **Read**: Read single or multiple notes
- **Write**: Create or update notes
- **Append**: Add content to end of notes
- **Patch**: Insert content at specific locations (headings/blocks)
- **List**: Browse vault directories
- **Delete**: Remove notes (with confirmation)
- **Periodic Notes**: Access daily/weekly/monthly notes
- **Recent Notes**: Find recently modified periodic notes
- **Slipbox Awareness**: Special support for `_Slipbox/` directory

## Common Operations

### Search Vault
```bash
# Search entire vault
python ~/.claude/skills/obsidian/scripts/search_vault.py "search term"

# Search only in slipbox
python ~/.claude/skills/obsidian/scripts/search_vault.py "emergence" --path "_Slipbox/"

# More context around matches
python ~/.claude/skills/obsidian/scripts/search_vault.py "theory" --context 200
```

### Read Notes
```bash
# Single note
python ~/.claude/skills/obsidian/scripts/read_note.py "My Note.md"

# Multiple notes
python ~/.claude/skills/obsidian/scripts/read_note.py "Note1.md" "Note2.md"

# From slipbox
python ~/.claude/skills/obsidian/scripts/read_note.py "_Slipbox/concept.md"
```

### Create Notes
```bash
# New note
python ~/.claude/skills/obsidian/scripts/write_note.py "New Note.md" \
  --content "# New Note\n\nContent here"

# In slipbox
python ~/.claude/skills/obsidian/scripts/write_note.py "_Slipbox/new-concept.md" \
  --content "# Concept\n\n## Details\n\nExplanation..."
```

### Append to Notes
```bash
python ~/.claude/skills/obsidian/scripts/append_note.py "Daily Note.md" \
  --content "\n## Evening\n\nNew thoughts..."
```

### List Files
```bash
# List vault root
python ~/.claude/skills/obsidian/scripts/list_files.py

# List slipbox
python ~/.claude/skills/obsidian/scripts/list_files.py --path "_Slipbox/"

# List specific directory
python ~/.claude/skills/obsidian/scripts/list_files.py --path "Projects/Active/"
```

### Periodic Notes
```bash
# Today's daily note
python ~/.claude/skills/obsidian/scripts/periodic_notes.py daily

# This week's weekly note
python ~/.claude/skills/obsidian/scripts/periodic_notes.py weekly

# Last 7 daily notes
python ~/.claude/skills/obsidian/scripts/recent_notes.py daily --limit 7
```

## Usage from Claude Code

When you work with Obsidian in Claude Code, the skill will be automatically invoked for operations like:

- "Search my vault for notes about emergence"
- "Read the note on systems thinking"
- "Create a new slipbox note about complexity"
- "List all notes in my Projects folder"
- "Show me today's daily note"
- "What's in my slipbox?"

## Script Reference

| Script | Purpose | Key Options |
|--------|---------|-------------|
| `search_vault.py` | Search notes | `--path`, `--context`, `--format` |
| `read_note.py` | Read notes | `--format` |
| `write_note.py` | Create/update | `--content`, `--stdin` |
| `append_note.py` | Append content | `--content`, `--stdin` |
| `patch_note.py` | Insert at location | `--heading`, `--block` |
| `list_files.py` | List directory | `--path`, `--format` |
| `delete_note.py` | Delete notes | `--force` |
| `periodic_notes.py` | Get periodic note | Period type |
| `recent_notes.py` | Recent periodic | `--limit`, `--include-content` |

## Integration with Other Skills

- **slipbox-integration**: Links slipbox notes into projects
- **narrative-inventory**: Can store inventories in vault
- **narrative-maps**: Can store spatial maps in vault
- **project-indexer**: Can maintain indexes in vault

## Troubleshooting

### Connection Refused
- Check if Obsidian is running
- Verify Local REST API plugin is enabled
- Check `OBSIDIAN_HOST` matches plugin settings

### 401 Unauthorized
- Verify `OBSIDIAN_API_KEY` is correct
- Copy fresh API key from plugin settings
- Ensure environment variable is set: `echo $OBSIDIAN_API_KEY`

### 404 Not Found
- Check file path is relative to vault root
- Include `.md` extension
- Verify file exists: use `list_files.py` first

### SSL Errors
- Default plugin uses self-signed certificate
- Set `OBSIDIAN_VERIFY_SSL=false` if needed
- Or pass `--no-verify-ssl` to scripts (if implemented)

## Security

- API key grants full vault access - treat as sensitive
- Store in environment variables, not in code
- Default server only accessible on localhost
- No authentication beyond API key

## Development

Core API wrapper: `scripts/obsidian_api.py`

All scripts use this wrapper and follow consistent patterns:
- Import from `obsidian_api import get_api`
- Handle `ObsidianAPIError` exceptions
- Support `--format json` for scripting
- Provide `--help` for usage info

## License

See LICENSE file in parent directory.
