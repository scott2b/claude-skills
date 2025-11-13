# Obsidian Skills Comparison

You have **two Obsidian skills** with different purposes:

## obsidian (Primary - Fast & Simple)

**Purpose:** Standard vault operations  
**Method:** Direct filesystem + ripgrep  
**Requirements:** ripgrep installed, vault path configured  
**Obsidian:** Does NOT need to be running  

**Use for:**
- ✅ Search notes (7x faster)
- ✅ Read files (50x faster)
- ✅ Write/create files (50x faster)
- ✅ Append to files
- ✅ List directories
- ✅ Delete files
- ✅ Parse YAML frontmatter
- ✅ Search by tags
- ✅ Work with slipbox

**Performance:**
- Search: 0.02s (vs 0.15s with API)
- File ops: 0.001s (vs 0.05s with API)

**This is the DEFAULT skill for Obsidian operations.**

## obsidian-api (Advanced - API Features Only)

**Purpose:** API-specific advanced features  
**Method:** Obsidian Local REST API  
**Requirements:** Obsidian running + REST API plugin + API key  
**Obsidian:** MUST be running  

**Use ONLY for:**
- 📊 Dataview DQL queries (aggregation, calculations)
- 📅 Periodic notes (daily/weekly/monthly management)
- 📝 Patch operations (insert after heading/block)
- 🔍 JSONLogic metadata queries

**Do NOT use for:**
- ❌ Regular search (use `obsidian` skill)
- ❌ Read/write files (use `obsidian` skill)
- ❌ List files (use `obsidian` skill)

## Decision Tree

```
User wants to work with Obsidian vault?
│
├─ Standard operations (search, read, write, list)?
│  └─→ Use: obsidian skill ⚡ (fast, simple)
│
└─ Advanced API features (Dataview, periodic notes, patch)?
   └─→ Use: obsidian-api skill 🔌 (requires Obsidian running)
```

## Migration Note

If you were using `obsidian-api` before, **switch to `obsidian`** for all standard operations. You'll see dramatic speed improvements:

- **7x faster search**
- **50x faster file operations**
- **No Obsidian process required**
- **Simpler setup** (just ripgrep + vault path)

Keep `obsidian-api` available for the rare cases when you need Dataview queries or other API-specific features.

## Examples

### ✅ Use obsidian skill:
```bash
# Search slipbox
python scripts/search_vault.py "emergence" --path "_Slipbox/"

# Read note
python scripts/read_note.py "My Note.md"

# Write note
python scripts/write_note.py "New.md" --content "# Title\nContent"
```

### 🔌 Use obsidian-api skill:
```bash
# Dataview query
python scripts/dataview_query.py "TABLE rating FROM #books"

# Get today's daily note
python scripts/periodic_notes.py daily

# Insert after heading
python scripts/patch_note.py "Note.md" --heading "Section" --content "New"
```

## Summary

- **99% of the time:** Use `obsidian` skill (fast, simple, always works)
- **1% of the time:** Use `obsidian-api` skill (API features only)

