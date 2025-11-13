---
name: slipbox-integration
description: PROACTIVELY identify and link relevant slipbox notes into narrative project structural documents. Use automatically when working on narrative projects to surface relevant research and arguments. Maintains project-specific tracking of which slipnotes are integrated where.
---

# Slipbox Integration Skill

## Purpose

Automatically identify relevant slipbox notes and integrate them into narrative project structural documents. This skill bridges the slipbox (research repository) and active writing projects, ensuring relevant research surfaces at the right moments without manual searching.

## When to Use This Skill

Use this skill AUTOMATICALLY when:

1. **Working on narrative projects** - Any project involving writing, research, or argument development
2. **Creating/editing structural documents** - Outlines, plans, chapter structures, section frameworks
3. **User mentions themes/concepts** - When discussion touches on topics that likely have slipbox coverage
4. **Beginning work sessions** - Check for newly relevant notes since last session
5. **After slipbox updates** - When new notes added that might be relevant to active project

## When NOT to Use This Skill

Do NOT use when:
- Working on programming/technical projects (slipbox is for narrative/research)
- Editing final prose/narrative drafts (links go in structure, not prose)
- User explicitly requests not to use slipbox
- SLIPBOX-INDEX.md doesn't exist or is inaccessible

## Core Principles

### 1. Link into Structure, Not Prose

**CORRECT LOCATIONS for slipnote links:**
- Project plans and outlines
- Chapter structure documents
- Section frameworks
- Research notes and planning docs
- Integration tracking documents

**WRONG LOCATIONS for slipnote links:**
- Final narrative prose drafts
- Published/publishable text
- Reader-facing content

### 2. Index Before Claiming

**NEVER** claim a slipnote exists without verifying in SLIPBOX-INDEX.md. The previous failure (falsely claiming notes existed) MUST NOT be repeated.

**Workflow:**
1. Read SLIPBOX-INDEX.md
2. Search for relevant notes by keyword/argument
3. Verify note IDs actually exist
4. Only then suggest linking

### 3. Track Integration

Maintain project-specific tracking of:
- Which slipnotes are linked into this project
- Where each note is linked (which files)
- Why each note is relevant (the connection)
- When notes were integrated

---

## Operational Workflow

### Phase 1: Initialization

**On first use in a project:**

1. **Verify slipbox access**
   - Check `$SLIPBOX_DIR` environment variable is set
   - Verify SLIPBOX-INDEX.md exists at `$SLIPBOX_DIR/SLIPBOX-INDEX.md`
   - If missing: inform user to set SLIPBOX_DIR or generate index

2. **Check project structure**
   - Read PROJECT-INDEX.md to understand project organization
   - Identify structural documents (plans, outlines, chapter structures)
   - Look for existing slipnote integration tracking file

3. **Create integration tracking document**
   - If doesn't exist: create `SLIPNOTE-INTEGRATION.md` in project root
   - Structure:
     ```markdown
     # Slipnote Integration Tracking

     **Project:** [Name]
     **Last Updated:** [Date]

     ## Integrated Notes Summary
     - Total notes linked: X
     - Categories represented: [list]
     - Most used: [top 3-5 notes]

     ## Notes by Project Location

     ### [Document Name]
     - [[ID Title]] - Why relevant: [explanation]
     - [[ID Title]] - Why relevant: [explanation]

     ### [Another Document]
     - [[ID Title]] - Why relevant: [explanation]

     ## Notes by Slipbox Category

     ### 1000 ➥ Existence, Knowledge & Belief
     - [[ID Title]] → Used in: [document], [document]

     ### 2000 ➥ Language, Narrative, Story & Myth
     - [[ID Title]] → Used in: [document]
     ```

### Phase 2: Relevance Analysis

**When user is working on content:**

1. **Identify current context**
   - What document are they editing/creating?
   - What themes/concepts are being discussed?
   - What arguments are being developed?

2. **Query slipbox index**
   - Read SLIPBOX-INDEX.md
   - Search keyword mapping for relevant terms
   - Check hierarchical note map for related argument threads
   - Identify 3-10 potentially relevant notes

3. **Rank by relevance**
   - **High relevance**: Directly addresses current argument/theme
   - **Medium relevance**: Provides supporting context or parallel argument
   - **Low relevance**: Tangentially related, might be useful later

4. **Verify notes exist**
   - Cross-check all candidate note IDs against inventory
   - NEVER suggest notes not in the index
   - If uncertain, err on side of not suggesting

### Phase 3: Integration Suggestions

**Present opportunities proactively:**

1. **Identify insertion points**
   - Find natural locations in structural documents where notes would fit
   - Look for existing research sections, argument lists, outline points

2. **Suggest with context**
   - Don't just list notes - explain WHY each is relevant
   - Show the argumentative connection
   - Example:
     ```
     For Chapter 7's section on reading transformation, consider:

     - [[2560.c Writing restructures consciousness]]
       → Ong's argument about literacy transformation parallels
         AI-assisted reading transformation you're developing

     - [[1100.b Extended Mind Thesis]]
       → Clark's framework provides theoretical grounding for
         reading-as-cognitive-technology argument
     ```

3. **Offer batch linking**
   - "I found 5 relevant notes for this chapter structure. Should I add them?"
   - Show full list with reasoning
   - Let user approve/reject specific notes

### Phase 4: Linking and Tracking

**When user approves integration:**

1. **Add wikilinks to structural documents**
   - Use proper Obsidian wikilink format: `[[ID Title]]`
   - Place in contextually appropriate locations
   - Add brief inline explanation if needed

2. **Update SLIPNOTE-INTEGRATION.md**
   - Add note to "Notes by Project Location" section
   - Add note to "Notes by Slipbox Category" section
   - Update summary counts
   - Record why note is relevant

3. **Update PROJECT-INDEX.md**
   - Add section "Slipnote Integration" if not present
   - Track high-level integration stats
   - Reference SLIPNOTE-INTEGRATION.md for details

### Phase 5: Maintenance

**Ongoing responsibilities:**

1. **Monitor for new relevant notes**
   - Check SLIPBOX-INDEX.md modification date
   - If updated since last check, scan for newly relevant notes
   - Suggest integration of new notes

2. **Identify gaps**
   - Note concepts/arguments in project that lack slipbox coverage
   - Mark as `⚠️ NEEDS RESEARCH` in project documents
   - Do NOT invent placeholder slipnotes

3. **Update integration tracking**
   - When project documents change, verify slipnote links still relevant
   - Remove links that no longer fit
   - Update tracking document to reflect current state

---

## Critical Rules

### Rule 1: Never Claim False Existence

**NEVER** suggest or link a slipnote without verifying it exists in SLIPBOX-INDEX.md.

This rule is ABSOLUTE. The previous failure violated this principle and destroyed trust.

**Verification workflow:**
1. Identify candidate note by keyword/concept
2. Check SLIPBOX-INDEX.md for exact ID and title
3. Only if found → suggest for integration
4. If not found → mark as research gap, do NOT invent

### Rule 2: Structure Only, Never Prose

**ONLY** link slipnotes into:
- Outlines
- Plans
- Chapter structure documents
- Research notes
- Integration tracking documents

**NEVER** link slipnotes into:
- Final narrative prose
- Draft narrative paragraphs
- Reader-facing text

### Rule 3: Explain the Connection

**NEVER** just dump wikilinks. Always explain WHY each note is relevant.

**Bad:**
```
Relevant notes:
- [[1100.b Extended Mind]]
- [[2560.c Writing restructures consciousness]]
```

**Good:**
```
Relevant notes:
- [[1100.b Extended Mind Thesis]]
  → Provides theoretical foundation for your argument that
    AI tools become part of cognitive system

- [[2560.c Writing restructures consciousness]]
  → Ong's historical precedent: writing transformed thought,
    just as you argue AI-assisted reading does now
```

### Rule 4: Track Everything

**ALWAYS** maintain SLIPNOTE-INTEGRATION.md showing:
- Which notes are integrated
- Where they're integrated
- Why they're relevant
- When they were added

This tracking serves multiple purposes:
- Prevents duplicate suggestions
- Shows integration coverage
- Aids later review/revision
- Documents research foundation

### Rule 5: Respect User Decisions

If user rejects a suggestion:
- Don't suggest that same note again for same context
- Note the rejection in tracking (optional)
- Learn from pattern of acceptances/rejections

---

## Integration Patterns

### Pattern 1: Chapter Structure Enrichment

When user has chapter structure document with beats/sections:

1. Analyze each beat for themes/arguments
2. Find slipnotes matching those themes
3. Add wikilinks in relevant sections with explanations
4. Update tracking document

Example:
```markdown
## Beat 3: The Cognitive Transformation

[User's original content...]

**Relevant slipnotes:**
- [[1100.b.a.b More than any technology, writing transforms consciousness]]
  → Historical parallel: Ong on writing's cognitive impact
- [[1100.b.4 Arguments for meaningful transformation?]]
  → Theoretical grounding for transformation claims
```

### Pattern 2: Argument Thread Discovery

When user develops argument that has slipbox precedent:

1. Identify the argument's core claim
2. Search slipbox for related argument threads
3. Surface notes that develop/support/challenge that argument
4. Show argumentative relationships

Example:
```
You're arguing that AI serves as "threshold guardian" - testing
readiness for cognitive transformation.

Related argument threads in slipbox:
- [[2610.e Campbell's threshold guardian archetype]]
  → Mythic pattern matches your metaphor
- [[6300.a.4 Key benefit of slipbox is slowing down]]
  → Parallel: gatekeeping as beneficial friction
```

### Pattern 3: Research Gap Identification

When user needs concept/argument without slipbox coverage:

1. Recognize the gap
2. Mark in project document as `⚠️ NEEDS RESEARCH`
3. Do NOT create placeholder slipnote
4. Track in integration document's "Research Gaps" section

Example:
```markdown
## Research Gaps

- **Verification practices in academic writing**: No slipnotes yet
  on scholarly verification standards. Need to research for Chapter 8.

- **Community knowledge practices**: Some coverage in 6000 series
  but needs expansion for Chapter 11 community section.
```

---

## Environment Requirements

**Required:**
- `$SLIPBOX_DIR` environment variable set to slipbox location
- `$SLIPBOX_DIR/SLIPBOX-INDEX.md` exists and is current
- PROJECT-INDEX.md exists in current project

**Optional but recommended:**
- SLIPNOTE-INTEGRATION.md in project (skill will create if missing)
- Regular updates to SLIPBOX-INDEX.md as slipbox grows

---

## Success Criteria

This skill succeeds when:

✅ Relevant slipnotes surface at natural moments during writing
✅ Integration happens proactively, not reactively
✅ All suggested notes actually exist (verified in index)
✅ Links appear only in structural documents, never in prose
✅ Each link has clear explanation of relevance
✅ Integration tracking stays current
✅ Research gaps identified, not papered over with invented notes

This skill fails when:

❌ Suggesting notes that don't exist
❌ Linking into prose/narrative drafts
❌ Dumping links without explanation
❌ Failing to track what's integrated where
❌ Creating placeholder slipnotes to fill gaps
❌ Reactive searching instead of index consultation

---

## Example Session

**Context:** User is working on Chapter 7 structure document about syntopical reading.

**Skill activates:**

1. Reads PROJECT-INDEX.md → identifies this is narrative project
2. Reads current document → sees "syntopical reading" theme
3. Reads SLIPBOX-INDEX.md → searches keywords: "reading", "synthesis", "multiple sources"
4. Finds candidates:
   - 6200 series (reading methods)
   - 2560 series (literacy transformation)
   - 6300 series (PKM/zettelkasten)

**Skill suggests:**

"Working on syntopical reading section. Found 4 relevant slipnotes:

**High relevance:**
- [[6200.b.1 Adler's syntopical reading method]]
  → Direct precedent for your framework

**Medium relevance:**
- [[6300.a.b Slip-box as world building]]
  → Parallel: building understanding from multiple sources
- [[2560.c Writing restructures consciousness]]
  → Foundation: literacy as cognitive transformation

Should I add these to the chapter structure?"

**User approves → Skill:**
1. Adds wikilinks to appropriate sections in chapter doc
2. Updates SLIPNOTE-INTEGRATION.md
3. Updates PROJECT-INDEX.md integration stats

**Result:** Chapter structure now references relevant research, user can click through to read notes, integration is tracked for later review.
