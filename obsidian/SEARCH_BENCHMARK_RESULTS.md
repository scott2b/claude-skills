# Obsidian Search Benchmark Results

**Date**: 2025-11-13
**Benchmark Script**: `benchmark_search.py`

## Summary

Comparison of Obsidian Local REST API search vs ripgrep (rg) for searching markdown files in an Obsidian vault.

## Test Results

### Test 1: "Campbell" (Slipbox only)
- **API**: 0.1539s, 4 files
- **ripgrep**: 0.0218s, 4 files
- **Speedup**: 7.05x faster with ripgrep
- **Results**: Identical

### Test 2: "dialogism" (Entire vault)
- **API**: 0.0801s, 44 files
- **ripgrep**: 0.0733s, 44 files
- **Speedup**: 1.09x faster with ripgrep
- **Results**: Identical

### Test 3: "extended mind" (Slipbox only)
- **API**: 0.1066s, 12 files
- **ripgrep**: 0.0157s, 10 files
- **Speedup**: 6.80x faster with ripgrep
- **Results**: API found 2 extra files (false positives - files containing "extended" and "mind" separately, not as phrase)

### Test 4: "Bakhtin" (Slipbox only)
- **API**: 0.0843s, 8 files
- **ripgrep**: 0.0196s, 8 files
- **Speedup**: 4.30x faster with ripgrep
- **Results**: Identical

## Key Findings

### Performance
- **ripgrep is 1.09x - 7.05x faster** than the Obsidian API for content search
- Average speedup: ~4.8x faster
- Most dramatic speedup on smaller search scopes (slipbox-only searches)

### Accuracy
- Results are **identical or nearly identical** in most cases
- API may occasionally return false positives for multi-word phrases (searches for words independently rather than as phrase)
- ripgrep provides **more precise** phrase matching by default

### Reliability
- Both methods are highly reliable
- ripgrep is a mature, battle-tested tool (written in Rust)
- API requires Obsidian to be running

## Recommendations

### Use ripgrep for:
1. **Content search** - Finding files containing specific text
2. **Fast queries** - When speed matters (4-7x faster)
3. **Phrase matching** - Exact phrase searches ("extended mind" as one phrase)
4. **Offline work** - Doesn't require Obsidian to be running
5. **Scripting** - Simple subprocess calls, no HTTP overhead

### Use Obsidian API for:
1. **Metadata queries** - Searching by tags, properties, frontmatter
2. **Complex queries** - JSONLogic or Dataview queries
3. **When Obsidian is already running** - No additional overhead
4. **Context snippets** - API returns surrounding context automatically

### Hybrid Approach (RECOMMENDED)

**For `/slipnote` workflow and similar tools:**

```python
# Fast content search with ripgrep
import subprocess

def search_slipbox(query, slipbox_dir):
    result = subprocess.run(
        ['rg', '-l', '--type', 'md', '-i', query, slipbox_dir],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return result.stdout.strip().split('\n')
    return []

# Direct filesystem operations for file ops
def read_note(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def write_note(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

# Use API only for metadata/tag queries (when needed)
```

## Implementation Impact

### Current Obsidian Skill
The current skill uses the API for all operations. Based on these benchmarks:

**Should change:**
- Search operations → Use ripgrep (4-7x speedup)
- File read/write → Use direct filesystem (eliminates HTTP overhead)
- File listing → Use `os.listdir()` or `glob.glob()`

**Should keep API for:**
- Tag/metadata queries (when Obsidian's parser is needed)
- Dataview queries (specialized functionality)
- Complex JSONLogic queries

### Expected Performance Improvement

For a typical `/slipnote` workflow that does:
- 3-5 searches
- 5-10 file reads
- 2-3 file writes

**Current (all API)**:
- ~0.5-1.0 seconds in API overhead

**Optimized (ripgrep + filesystem)**:
- ~0.1-0.2 seconds
- **4-5x faster overall**

## Technical Details

### Why ripgrep is faster

1. **No HTTP overhead** - Direct filesystem access
2. **Optimized C/Rust code** - Highly optimized binary
3. **Parallel processing** - Multi-threaded by default
4. **Memory mapped files** - Efficient file reading
5. **No parsing** - Just searches raw text

### Why API is sometimes useful

1. **Access to Obsidian's index** - Pre-parsed metadata
2. **Tag resolution** - Knows about Obsidian's tag system
3. **Link resolution** - Understands wikilinks
4. **Dataview integration** - Access to Dataview queries

## Conclusion

**The Obsidian Local REST API is valuable but not necessary for most operations.**

For optimal performance:
- Use **ripgrep** for content search (4-7x faster)
- Use **direct filesystem** for file operations (faster, simpler)
- Reserve **API** for metadata/tag queries and specialized functionality

This hybrid approach provides the best of both worlds: speed and simplicity from ripgrep/filesystem, specialized capabilities from the API when needed.
