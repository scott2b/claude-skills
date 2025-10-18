---
name: "narrative-inventory"
description: "Create writing inventories using William Germano's framework to help writers understand what they have, identify gaps, and maintain focus during revision"
---

# Narrative Inventory

This skill helps writers inventory their draft text using William Germano's framework from *On Revision*. Inventories are "lists of things" that help writers understand what they have, what they're trying to do, and what might be missing or overemphasized.

## Purpose

An inventory at the draft stage is a reminder, a "to-do-or-at-least-don't-forget-about" list. It helps writers:
- Keep fresh in mind what's important about their subject
- Remember what's driving them
- Identify what they want to share (new knowledge, ideas)
- See where their draft is heading
- Find significant points and themes
- Understand what belongs and what doesn't

As Germano notes: "Tell a story. As you revise, work to keep fresh in mind what's driving you, and how you want to share both some form of new knowledge and some idea of that drive."

## When to Invoke This Skill

Invoke this skill when:
- Beginning revision of a draft
- Feeling lost in the prose of your own draft
- Needing to understand what you've actually written vs. what you intended
- Identifying gaps or overemphasized areas
- Refocusing on the core purpose and direction of the piece
- Planning what still needs to be developed

## Inventory Types (from Germano)

### 1. Simple Topic/Theme Inventory
A basic list of components, topics, or themes you want to make sure you've covered. Like a shopping list - no structure, just items to remember.

**Example:**
```
competing histories of American whiteness
Baldwin's understanding of white self-illusion
histories of failed activism as anti-activism
```

This is "barely a set of notes" - points of interest to consider as you compose.

### 2. Topic Inventory with Concerns
A list of topics and concerns, showing more clearly where the essay might be heading. Still not a structure, but "a place from which to see a structure. A set of concerns, a point of view."

**Example (Flint water crisis):**
```
incidence of childhood illnesses prior to 2000
incidence of childhood illnesses in 2014-15
lead poisoning
race and the allocation of state resources
the EPA's failure to intervene
the Flint River as industry's dumping ground
children's health initiatives in Flint
Concerned Pastors for Social Action
```

### 3. Objectives/Ambitions Inventory
Used to "tick off a set of ambitions for your draft." Lists what the writer wants to accomplish, objectives to achieve.

**Example (Valdivia Blackwell article):**
```
make a case for Valdivia Blackwell as an important figure in plant genetics

locate Blackwell's career within a tradition of female researchers
whose contribution was subsumed into the achievements of the (male) team leader

organize the evidence linking Blackwell to the development of the rot-resistant cranberry

tell her story!
```

This includes both materials and tasks - an objective reminding what's important.

### 4. Memoranda Inventory
"Things not to be forgotten" (Latin: memoranda = "things to be remembered"). A reminder to write such things down. Details and materials for further study - things you're interested in but haven't yet fully developed.

This type captures:
- Curiosities to pursue
- Details that may or may not make it into the final text
- Points that will be developed or fall away as writing progresses

## Task Instructions

When this skill is invoked, follow these steps:

### Step 1: Detect Environment & Understand Context

**First, determine your environment:**
- If you have access to a project directory and file system tools (Read, Write, Edit, Glob, Grep): You are in **Claude Code**
- If the user uploaded files or you're working in a chat without direct project access: You are in **Claude Desktop/Web**

**Then understand the writing context:**
1. Ask the user which draft or section they want to inventory
2. In Claude Code: If not specified, search for main writing files in the project
3. In Claude Desktop: Ask the user to share the draft text (upload file or paste text)
4. Read the draft text to understand its scope and content

### Step 2: Assess Current State

Analyze the draft for:
- Main themes and topics already present
- Apparent objectives or ambitions
- What seems emphasized vs. underdeveloped
- Gaps or areas that seem to need attention
- The writer's apparent driving question or purpose

### Step 3: Recommend Inventory Type(s)

Based on the draft's state and the writing stage:
- **Early/exploratory draft**: Suggest simple topic inventory or memoranda
- **Draft with unclear direction**: Suggest objectives inventory
- **Mid-revision**: Suggest topic inventory with concerns
- **Complex draft**: May suggest multiple inventory types

Present options to the user explaining why each might be helpful. **Always ask the user to confirm which type(s) they want before proceeding.**

### Step 4: Generate the Inventory

Based on user selection:
1. Create the appropriate inventory type(s)
2. Format as an unstructured list (NOT an outline)
3. Use the writer's language and concepts where possible
4. Include items that:
   - Are already in the draft
   - Seem to be intended but underdeveloped
   - Logically connect to what's there
   - The writer might want to remember

### Step 5: Provide Comparative Analysis

Show the writer:
- **What's present and emphasized** in the current draft
- **What's mentioned but underdeveloped**
- **What's in the inventory but not yet in the draft**
- **What might be overemphasized** relative to stated goals

### Step 6: Save or Present the Inventory

**If in Claude Code (project directory access):**
1. Ask where to save inventories (suggest `inventories/` or `process/inventories/`)
2. Create the chosen directory if it doesn't exist
3. Save with descriptive filename: `YYYY-MM-DD-[draft-name]-[type]-inventory.md`
4. Confirm the save location to the user

**If in Claude Desktop/Web (no project directory):**
1. Create the inventory as a formatted markdown artifact or downloadable file
2. Present it in the chat for the user to review
3. Suggest the user save it with filename: `YYYY-MM-DD-[draft-name]-[type]-inventory.md`
4. Offer to create a formatted version for download if requested

## Important Principles

### NOT a Structure
Inventories are explicitly NOT outlines or structures. As Germano emphasizes, they're "barely a set of notes," "like a shopping list or a set of points of interest," NOT "a structure, much less an outline."

### Expect Change
Some items "will be developed and others will fall away." The inventory is a working document, not a contract.

### Writer-Centered
Focus on what's important TO THE WRITER, not what an external reader might expect. The inventory "lays out components and emphases so that you can find them to build or rebuild your text."

### No Central Question Yet
At the inventory stage, the writer may have "no central question, much less a thesis." That's fine. Inventories help you discover direction.

### Multiple Iterations
Inventories can be created multiple times throughout revision as the work develops and changes.

## Output Format

When presenting an inventory to the user:

```markdown
# [Type] Inventory for [Draft Name]
**Date**: [YYYY-MM-DD]
**Draft analyzed**: [file path or description]

## Your Inventory

[The actual inventory items, unstructured list]

## Analysis

### Already Emphasized in Your Draft
- [items that are clearly present and developed]

### Present but Underdeveloped
- [items mentioned but needing more attention]

### In Your Inventory but Not Yet in Draft
- [items to potentially add]

### Observations
[Any patterns, suggestions, or insights about direction]

---
*This inventory is a reminder tool, not a structure. Some items will develop, others will fall away as your revision progresses.*
```

## Examples of Good Inventory Items

From Germano's examples:
- "character of liq—the root is the important piece"
- "what about monks or Crusaders—link of P with liquorice?"
- "tell her story!"
- "organize the evidence linking Blackwell to the development of the rot-resistant cranberry"
- "concerns about abuse of"
- "the role of ammonium chloride in the final preparation"

Note: These are brief, sometimes fragmentary, in the writer's thinking voice.

## What This Skill Does NOT Do

- Create outlines or hierarchical structures
- Impose external organization on the writer's material
- Judge quality or make value judgments about content
- Provide comprehensive analysis (that's for other skills/tools)
- Replace the writer's own thinking process

## Integration with Other Tools

This skill can work alongside:
- **Keywords skill** (related Germano concept - finding significant themes)
- **Mapping skill** (another Germano tool - visualizing relationships)
- **Structural analysis tools** (used later in revision)
- Project-specific revision workflows

---

*Based on William Germano's "Know What You've Got" chapter in On Revision: The Only Writing That Counts*
