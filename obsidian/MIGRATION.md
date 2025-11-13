# Migration from API to Direct Filesystem

## Summary

The Obsidian skill has been redesigned to use **ripgrep + direct filesystem** instead of the Obsidian REST API.

## Changes

### ✅ Benefits

- **4-7x faster** search operations
- **50x faster** file operations
- **No Obsidian process required**
- **No API plugin required**
- **Simpler code** - no HTTP, auth, or API dependencies
- **More portable** - works anywhere with Python + ripgrep

### 📦 Core Library

**New:** `scripts/vault_ops.py`
- `search()` - Fast ripgrep-based search
- `read_file()`, `write_file()`, `append_file()`, `delete_file()`
- `parse_frontmatter()`, `format_frontmatter()`
- `search_by_tag()`, `get_vault_path()`

**Replaced:** `scripts/obsidian_api.py` (preserved in `obsidian-api` skill)

### 📝 Updated Scripts

- ✅ `search_vault.py` - Uses ripgrep
- ✅ `read_note.py` - Direct file reading
- ✅ `write_note.py` - Direct file writing
- ✅ `append_note.py` - Direct file appending
- ✅ `list_files.py` - Direct directory listing
- ✅ `delete_note.py` - Direct file deletion

### 🗄️ Deprecated Scripts

Moved to `scripts/deprecated/` (require API):
- `patch_note.py` - Insert after heading/block
- `periodic_notes.py` - Daily/weekly notes
- `recent_notes.py` - Recent notes query

## Backup

The original API-based skill is preserved as:
```
~/.claude/skills/obsidian-api/
```

Use it for features requiring Obsidian's API:
- Dataview aggregation queries
- JSONLogic metadata queries
- Periodic notes management

## Migration Guide

### For Users

**Before:**
```bash
# Required Obsidian running + REST API plugin
export OBSIDIAN_API_KEY="your-key"
```

**After:**
```bash
# Just set vault path (or auto-detects)
export OBSIDIAN_VAULT_PATH="/path/to/vault"
```

### For Scripts/Tools

**Before:**
```python
from obsidian_api import get_api
api = get_api()
results = api.simple_search("query")
```

**After:**
```python
from vault_ops import search
results = search("query", files_only=True)
```

## Testing

All core operations tested and working:
- ✅ Search (4x faster)
- ✅ Read files
- ✅ Write files
- ✅ Append to files
- ✅ List directories
- ✅ Delete files
- ✅ Parse frontmatter
- ✅ Search by tags

## Performance

See `SEARCH_BENCHMARK_RESULTS.md` for detailed benchmarks.

| Operation | Before (API) | After (Direct) | Improvement |
|-----------|--------------|----------------|-------------|
| Search | 0.15s | 0.02s | **7x faster** |
| Read | 0.05s | 0.001s | **50x faster** |
| Write | 0.05s | 0.001s | **50x faster** |

