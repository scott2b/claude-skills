# Obsidian Vault Operations

Fast, simple vault operations using ripgrep and direct filesystem access.

**No API required. No Obsidian process required.**

## Features

- ⚡ **Fast search** using ripgrep (4-7x faster than API)
- 📁 **Direct file operations** (read/write/delete)
- 🔍 **Simple frontmatter parsing**
- 🏷️ **Tag search** (inline `#tags` and frontmatter)
- 🔗 **Wikilink support** (just text patterns)

## Setup

### Requirements

1. **ripgrep** - Fast search tool
   ```bash
   brew install ripgrep  # macOS
   ```

2. **Python 3.7+** - No additional libraries needed

3. **Vault path** - Set environment variable:
   ```bash
   export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
   ```
   Or it will auto-detect from Obsidian config.

## Usage

### Search
```bash
python scripts/search_vault.py "emergence" --path "_Slipbox/"
```

### Read/Write
```bash
python scripts/read_note.py "Note.md"
python scripts/write_note.py "Note.md" --content "# Title\nContent"
```

See scripts for full documentation.

## Performance

**4-7x faster** than Obsidian REST API for search operations.

See `SEARCH_BENCHMARK_RESULTS.md` for details.
