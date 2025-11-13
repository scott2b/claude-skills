# Project Index Structure Guide

This document provides templates and examples for creating effective project knowledge indexes.

## Core Principles

1. **Index before claiming** - Never claim something exists without verifying it in the index
2. **Update as you work** - Keep index current, don't let it become stale
3. **Use instead of searching** - Consult index first before grepping/searching
4. **Systematic over reactive** - Build knowledge systematically, not reactively

---

## Template: General Project Index

```markdown
# [Project Name] - Project Knowledge Index

**Generated:** YYYY-MM-DD HH:MM
**Last Updated:** YYYY-MM-DD HH:MM
**Status:** [Active/Complete/Paused]

---

## File Registry

### Source Files
- `path/to/file.ext` - Purpose, size, modified date, current state

### Configuration Files
- `path/to/config.ext` - Purpose, what it configures

### Documentation Files
- `path/to/doc.md` - What it documents, current completeness

---

## Content Summary

### Key Components
- Component Name - What it does, current state, completion status

### Cross-References
- File A → File B: Relationship type and purpose
- Module X imports Module Y: Why and what for

---

## Completion Tracking

### Done
- [x] Task that's complete
- [x] Another completed task

### In Progress
- [ ] Task being worked on
- [ ] Another active task

### Planned
- [ ] Future task
- [ ] Another planned task

---

## Project Knowledge

### Important Decisions
- **Date**: Decision made: Rationale and implications

### Patterns Identified
- Pattern Name: Description and where it appears

### Dependencies
- External: What's required from outside project
- Internal: What depends on what within project

### Known Issues
- Issue description: Current status and blocking factors
```

---

## Template: Writing/Research Project Index

For projects involving research notes, slipbox notes, chapters, or other narrative content:

```markdown
# [Project Name] - Project Knowledge Index

**Generated:** YYYY-MM-DD HH:MM
**Last Updated:** YYYY-MM-DD HH:MM

---

## File Registry

### Chapter/Section Files
- `01-CHAPTER-01.md` - Title, word count, completion status
  - Summary: What this chapter covers
  - State: [Draft/In Progress/Complete]

### Research Notes
- `slipbox/1234.md` - Title, topic, connections
  - Referenced by: [List of chapters/sections]

### Planning Documents
- `PLAN.md` - What it plans, current status

---

## Content Inventory

### Slipbox Notes
Total: N notes

#### By Topic
- **Topic A** (N notes): 1234.md, 1235.md, 1236.md
- **Topic B** (N notes): 2345.md, 2346.md

#### By Status
- ✅ EXISTS (N notes): List of IDs
- ⚠️ NEEDS CREATION (N notes): List of IDs

### Chapter Integration Status
- Chapter 1: Which notes integrated, which needed
- Chapter 2: Which notes integrated, which needed

---

## Cross-References

### Note → Chapter Mapping
- Note 1234 → Chapters 1, 3, 5: How it's used in each
- Note 2345 → Chapter 2: Integration details

### Chapter → Chapter References
- Chapter 1 → Chapter 3: What's referenced and why
- Chapter 4 → Chapter 7: Callback or foreshadowing

---

## Completion Status

### Structural Work
- [x] Framework defined
- [x] Chapter outlines complete
- [ ] All chapters drafted

### Integration Work
- [ ] Slipbox notes integrated: N of M complete
- [ ] Cross-references verified: N of M checked

---

## Project Knowledge

### Key Concepts
- Concept Name: Definition and where it appears

### Recurring Patterns
- Pattern: How it manifests across chapters

### Open Questions
- Question: What needs resolution
```

---

## Template: Code Project Index

For software projects:

```markdown
# [Project Name] - Project Knowledge Index

**Generated:** YYYY-MM-DD HH:MM
**Last Updated:** YYYY-MM-DD HH:MM

---

## File Registry

### Source Code
- `src/module/file.ts` - Purpose, exports, imports, LOC
  - Key Functions: List with brief description
  - Dependencies: What it imports

### Tests
- `tests/module.test.ts` - What it tests, coverage status

### Configuration
- `package.json` - Dependencies, scripts, metadata

---

## Architecture Map

### Module Structure
```
src/
├── core/ - Core functionality
│   ├── module1.ts - Does X
│   └── module2.ts - Does Y
├── utils/ - Utility functions
└── types/ - Type definitions
```

### Dependency Graph
- Module A depends on: Module B, Module C
- Module B depends on: Module C
- Module C depends on: (none - leaf)

---

## API Reference

### Public Functions
- `functionName(args): returnType` - What it does
  - Location: path/to/file.ts:lineNumber
  - Used by: List of modules

### Data Structures
- `TypeName` - What it represents
  - Location: path/to/types.ts:lineNumber
  - Used by: List of modules

---

## Implementation Status

### Core Features
- [x] Feature A implemented
- [ ] Feature B in progress

### Tests
- [x] Unit tests: N% coverage
- [ ] Integration tests needed

---

## Technical Decisions

### Architecture Choices
- **Date**: Decision: Why chosen over alternatives

### Patterns Used
- Pattern Name: Where and why it's used

### Known Issues
- Issue: Description, impact, planned fix
```

---

## Usage Guidelines

### When to Create Index

Create PROJECT-INDEX.md when:
- Starting work on any multi-day project
- User mentions "you keep searching/grepping"
- Working with existing codebase that needs tracking
- After initial exploration phase of new project

### When to Update Index

Update the index:
- After reading new files
- After creating/modifying files
- After discovering key relationships
- After making important decisions
- At end of each work session

### How to Use Index

Before working:
1. Read PROJECT-INDEX.md first
2. Check what exists before claiming existence
3. Identify what needs updating

While working:
4. Note changes needed to index
5. Track new knowledge discovered

After working:
6. Update index with new information
7. Verify index reflects current reality

### What NOT to Do

❌ Never claim something exists without checking index
❌ Never search/grep before consulting index
❌ Never let index become stale (update as you work)
❌ Never create duplicate tracking (use index as single source of truth)

---

## Example: Slipbox Integration

**WRONG Approach:**
```
Working on Chapter 1, need slipbox notes.
Let me grep for notes matching this topic...
Found some, I'll mark them as ✅ EXISTS.
```

**RIGHT Approach:**
```
Working on Chapter 1, need slipbox notes.
Checking PROJECT-INDEX.md > Slipbox Notes section...
Index shows notes 1234, 1235 exist on this topic.
Index shows notes 2345, 2346 need creation.
Using this information to mark status correctly.
After integrating, updating index with integration details.
```
