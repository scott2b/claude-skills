---
name: "narrative-inventory"
description: "Create writing inventories using William Germano's framework to help writers understand what they have, identify gaps, and maintain focus during revision"
---

# Narrative Inventory

This skill helps writers inventory their draft text using William Germano's framework from *On Revision*. Inventories are "lists of things" that help writers understand what they have, what they're trying to do, and what might be missing or overemphasized.

## Purpose

An inventory at the draft stage is a reminder, a "to-do-or-at-least-don't-forget-about" list. Inventories help writers keep fresh in mind what's important about their subject, remember what's driving them, identify what they want to share, see where the draft is heading, find significant points and themes, and understand what belongs and what doesn't.

## When to Invoke This Skill

Invoke this skill when writers need to:
- Begin revision of a draft
- Understand what's actually been written vs. what was intended
- Identify gaps or overemphasized areas
- Refocus on the core purpose and direction of the piece
- Plan what still needs to be developed
- Feel lost in the prose of their own draft

## Bundled Resources

**References:**
- `references/germano-framework.md` - Detailed explanation of inventory types (Simple Topic, Topic with Concerns, Objectives/Ambitions, Memoranda), principles, and examples from Germano's framework

**Assets:**
- `assets/inventory-template.md` - Template for inventory output
- `assets/example-inventory.md` - Complete example based on Germano's liquorice essay illustration

## Task Instructions

When this skill is invoked, follow these steps to create an inventory.

### Step 1: Detect Environment & Understand Context

**Determine the environment:**
- With access to project directory and file system tools (Read, Write, Edit, Glob, Grep): Claude Code environment
- With uploaded files or chat without direct project access: Claude Desktop/Web environment

**Understand the writing context:**
1. Ask which draft or section to inventory
2. In Claude Code: If not specified, search for main writing files in the project
3. In Claude Desktop: Ask to share the draft text (upload file or paste text)
4. Read the draft text to understand scope and content

### Step 2: Assess Current State

Analyze the draft for:
- Main themes and topics already present
- Apparent objectives or ambitions
- What seems emphasized vs. underdeveloped
- Gaps or areas that seem to need attention
- The writer's apparent driving question or purpose

### Step 3: Recommend Inventory Type(s)

Based on the draft's state and writing stage, recommend appropriate inventory types. Consult `references/germano-framework.md` for detailed descriptions of each type:

- **Simple Topic/Theme Inventory**: Early/exploratory drafts
- **Topic Inventory with Concerns**: Mid-revision when direction is emerging
- **Objectives/Ambitions Inventory**: Drafts with unclear direction
- **Memoranda Inventory**: Capturing curiosities and things not to forget

Present options to the writer explaining why each might be helpful. **Always ask the writer to confirm which type(s) they want before proceeding.**

### Step 4: Generate the Inventory

Based on writer selection:
1. Create the appropriate inventory type(s)
2. Format as an unstructured list (NOT an outline - see principles in `references/germano-framework.md`)
3. Use the writer's language and concepts where possible
4. Include items that:
   - Are already in the draft
   - Seem to be intended but underdeveloped
   - Logically connect to what's there
   - The writer might want to remember
5. Keep items brief, sometimes fragmentary, in the writer's thinking voice

### Step 5: Provide Comparative Analysis

Show the writer:
- **What's present and emphasized** in the current draft
- **What's mentioned but underdeveloped**
- **What's in the inventory but not yet in the draft**
- **What might be overemphasized** relative to stated goals

This comparative view helps identify gaps, priorities, and where to focus revision energy.

### Step 6: Save or Present the Inventory

**If in Claude Code (project directory access):**
1. Get current date using `date +%Y-%m-%d` command
2. Ask where to save inventories (suggest `inventories/` or `process/inventories/`)
3. Create the chosen directory if it doesn't exist
4. Save with descriptive filename using actual date: `YYYY-MM-DD-[draft-name]-[type]-inventory.md`
5. Use the structure from `assets/inventory-template.md`
6. Confirm the save location to the user

**If in Claude Desktop/Web (no project directory):**
1. Create the inventory as a formatted markdown artifact or downloadable file
2. Present it in the chat for review
3. Suggest saving with filename using current date: `YYYY-MM-DD-[draft-name]-[type]-inventory.md`
4. Use the structure from `assets/inventory-template.md`
5. Offer to create a formatted version for download if requested

## Important Reminders

- **NOT a structure**: Inventories are explicitly NOT outlines or structures - they're "barely a set of notes"
- **Expect change**: Some items will develop, others will fall away
- **Writer-centered**: Focus on what's important to the writer, not external expectations
- **No thesis required**: The writer may have no central question yet - that's fine
- **Multiple iterations**: Create new inventories as the draft evolves

**Reference**: See `references/germano-framework.md` for detailed principles and examples.

## What This Skill Does NOT Do

- Create outlines or hierarchical structures
- Impose external organization on the writer's material
- Judge quality or make value judgments about content
- Provide comprehensive analysis (that's for other skills/tools)
- Replace the writer's own thinking process

## Integration with Other Skills

This skill works alongside:
- **narrative-keywords** - finding significant themes
- **narrative-maps** - visualizing spatial relationships
- Structural analysis tools (used later in revision)
- Project-specific revision workflows

---

*Based on William Germano's "Know What You've Got" chapter in On Revision: The Only Writing That Counts*
