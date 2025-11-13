---
name: project-indexer
description: PROACTIVELY maintain systematic project knowledge indexes to eliminate constant searching and grepping. Use at start of multi-day projects, when working with existing codebases, or whenever systematic knowledge would prevent reactive searching. Creates and maintains PROJECT-INDEX.md as single source of truth about what exists, what's complete, and how components relate. Critical for long-running projects to build institutional knowledge instead of rediscovering everything every session.
---

# Project Indexer

## Purpose

Stop searching and grepping constantly. Build systematic knowledge about projects that persists across sessions. Maintain PROJECT-INDEX.md as single source of truth about project state, file registry, cross-references, and completion status.

## When to Use This Skill

Use this skill PROACTIVELY when:

1. **Starting any multi-day project** - Before making claims about what exists
2. **Working with existing codebases** - Before searching for files/functions
3. **User criticizes constant searching** - "You keep searching/grepping"
4. **Writing project involving notes/chapters** - Especially with slipbox notes
5. **After initial exploration** - Once project structure is understood
6. **Beginning each session** - Read index before working

## Core Principle

**INDEX BEFORE CLAIMING** - Never claim something exists without verifying it in the index. Never search/grep before consulting the index.

---

## Creating a Project Index

### Step 1: Generate Initial Index

Use the indexing script to create initial file registry:

```bash
python scripts/create_index.py /path/to/project [output-filename]
```

This creates PROJECT-INDEX.md with:
- File registry (all files with sizes, modification dates)
- Template sections for content summary
- Template sections for cross-references
- Template sections for completion tracking

### Step 2: Enrich the Index

The generated index is a starting point. Immediately enrich it with:

1. **Content Summary**
   - What each key file contains and its purpose
   - Current state of each component
   - Completion status

2. **Cross-References**
   - Which files reference which other files
   - Dependencies between components
   - Chapter → Note mappings (for writing projects)

3. **Project Knowledge**
   - Important decisions made
   - Patterns identified
   - Known issues

### Step 3: Verify Against Reality

Before using the index:
- Spot-check that indexed files actually exist
- Verify cross-references are accurate
- Confirm completion statuses reflect reality

---

## Maintaining the Index

### When to Update

Update PROJECT-INDEX.md:
- ✅ After reading new files (add to content summary)
- ✅ After creating/modifying files (update file registry)
- ✅ After discovering relationships (add cross-references)
- ✅ After completing work (update completion status)
- ✅ At end of each session (ensure current)

### What to Track

For all projects:
- File registry (what exists, where, when modified)
- Content summary (what each file contains)
- Cross-references (how components relate)
- Completion tracking (what's done, in progress, planned)

For writing projects, also track:
- Slipbox note inventory (ID, title, topic, status: EXISTS vs. NEEDS CREATION)
- Note → Chapter mappings (which chapters use which notes)
- Chapter completion status (what's integrated, what's needed)

For code projects, also track:
- Module dependencies (what imports what)
- Function locations (where key functions live)
- API surface (public interfaces)

---

## Using the Index

### Before Starting Work

**ALWAYS read PROJECT-INDEX.md first:**

```
Before working on Chapter 5, read PROJECT-INDEX.md:
- Check which slipbox notes exist
- Check which notes Chapter 5 needs
- Check what's already integrated
- Check cross-references to other chapters
```

### While Working

**Check the index, don't search:**

❌ WRONG:
```
Need to find slipbox notes on topic X.
Let me grep for files matching this pattern...
```

✅ RIGHT:
```
Need to find slipbox notes on topic X.
Checking PROJECT-INDEX.md > Slipbox Notes > By Topic section...
Index shows notes 1234, 1235 cover topic X and exist.
```

### After Working

**Update the index with new knowledge:**

```
Just integrated notes 1234, 1235 into Chapter 5.
Updating PROJECT-INDEX.md:
- Mark notes 1234, 1235 as integrated in Chapter 5
- Add to Chapter 5's integration status
- Update completion tracking
```

---

## Critical Rules

### 1. Index Before Claiming

**NEVER** mark something as ✅ EXISTS without verifying in index:

❌ WRONG:
```
This chapter needs slipbox note 1234.
✅ EXISTS `1234.md` - About topic X
(Never checked if it actually exists!)
```

✅ RIGHT:
```
This chapter needs slipbox note 1234.
Checking PROJECT-INDEX.md > Slipbox Notes section...
Note 1234 is NOT in index.
⚠️ NEEDS CREATION `1234.md` - About topic X
```

### 2. Consult Before Searching

**ALWAYS** check index before grepping/searching:

❌ WRONG:
```
What files are in src/components/?
Let me grep for component files...
```

✅ RIGHT:
```
What files are in src/components/?
Checking PROJECT-INDEX.md > File Registry > Components section...
Index shows: ComponentA.tsx, ComponentB.tsx, ComponentC.tsx
```

### 3. Update After Changes

**ALWAYS** update index after modifying project:

❌ WRONG:
```
Created new Chapter 6 file.
(Doesn't update index)
Later: Searching for chapter files...
```

✅ RIGHT:
```
Created new Chapter 6 file.
Updating PROJECT-INDEX.md:
- Add to File Registry
- Add to Content Summary
- Add to Completion Tracking
```

### 4. Single Source of Truth

**NEVER** maintain duplicate tracking:

❌ WRONG:
```
Tracking completion in PROJECT-INDEX.md
Also tracking completion in TODO.md
Also tracking completion in PLAN.md
(Three sources of truth that will diverge)
```

✅ RIGHT:
```
Tracking completion in PROJECT-INDEX.md only
Other documents reference the index
```

---

## Special Case: Slipbox Integration

When working with slipbox notes and chapters:

### Initial Setup

1. **Create slipbox inventory:**
   ```
   Scanning slipbox directory...
   Adding to PROJECT-INDEX.md > Slipbox Notes:
   - Note 1234: Title, topic, EXISTS
   - Note 1235: Title, topic, EXISTS
   - Note 2345: Title, topic, NEEDS CREATION
   ```

2. **Map notes to chapters:**
   ```
   Checking chapter requirements...
   Chapter 1 needs: 1234, 1235 (both exist)
   Chapter 2 needs: 2345 (needs creation)
   ```

### During Integration

3. **Before claiming EXISTS:**
   ```
   Chapter 3 needs note 3456.
   Checking PROJECT-INDEX.md > Slipbox Notes...
   Note 3456 NOT in index.
   Marking as ⚠️ NEEDS CREATION.
   ```

4. **After integration:**
   ```
   Integrated note 1234 into Chapter 3.
   Updating PROJECT-INDEX.md:
   - Note 1234 → Referenced by: Chapter 1, Chapter 3
   - Chapter 3 status: 1 of 5 notes integrated
   ```

---

## Templates and Examples

Consult `references/index-structure.md` for:
- Full template structures for different project types
- Example indexes for code, writing, and research projects
- Detailed usage guidelines
- More specific examples of right vs. wrong approaches

---

## Troubleshooting

### "You keep searching and grepping"

If user says this, it means:
1. INDEX DOES NOT EXIST → Create one immediately
2. INDEX EXISTS BUT STALE → Update it before continuing
3. INDEX EXISTS BUT NOT CONSULTING → Change workflow to check index first

### "You claimed X exists but it doesn't"

This means:
1. Didn't check index before claiming
2. Index is wrong (verify and fix)
3. Skipped verification step

Fix:
- Read actual directory to verify what exists
- Update index with reality
- Never claim existence without index verification

### "Index is outdated"

This means:
1. Not updating index during work
2. Not updating index after changes

Fix:
- Update index immediately
- Make index updates part of every change workflow

---

## Success Criteria

Index is successful when:

✅ Can answer "what files exist?" without searching
✅ Can answer "what's the state of X?" without reading files
✅ Can answer "what depends on Y?" without grepping
✅ Never claim something exists without verifying in index
✅ Index stays current with project reality
✅ Searching/grepping is rare exception, not default behavior

Index has failed when:

❌ Constantly searching for files/content
❌ Claiming things exist that don't
❌ Can't answer basic questions about project state
❌ Index is stale and not maintained
❌ Index exists but never consulted
