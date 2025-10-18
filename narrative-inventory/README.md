# Narrative Inventory Skill

A writing skill based on William Germano's inventorying framework from *On Revision*.

## Installation

### For Claude Code
1. This skill is already in the correct location: `.claude/skills/narrative-inventory/`
2. Reload skills if needed with `/reload-skills`
3. Invoke with: `/narrative-inventory` or use the Skill tool

### For Claude Desktop/claude.ai
1. Create a ZIP file of this entire folder (narrative-inventory/)
2. In Claude Desktop or claude.ai:
   - Go to Settings > Capabilities
   - Click "Upload skill"
   - Upload the ZIP file
3. Enable the skill in your Capabilities settings
4. Claude will automatically invoke it when you ask for help inventorying your writing

## How to Use

Simply ask Claude to help you inventory your draft. For example:
- "Help me inventory my draft on [topic]"
- "I need to create an inventory of what I've written so far"
- "Can you analyze my draft and create a memoranda inventory?"

The skill will:
1. Ask for or locate your draft text
2. Analyze what you've written
3. Recommend appropriate inventory type(s)
4. Generate the inventory
5. Provide comparative analysis
6. Save it (Claude Code) or present it for download (Desktop)

## What is Inventorying?

From Germano's framework, inventories are "lists of things" that help writers:
- Understand what they have
- Identify what's missing or overemphasized
- Maintain focus on core purposes
- Remember what's driving them

Inventories are NOT outlines or structures - they're working reminders, "barely a set of notes."

## Inventory Types

1. **Simple Topic/Theme** - Basic list of components to cover
2. **Topic with Concerns** - Topics showing where you're heading
3. **Objectives/Ambitions** - What you want to accomplish
4. **Memoranda** - Things not to forget, details for further study

## Examples

See `resources/example-inventory.md` for a sample inventory output.

## Source

Based on Chapter 3 "Know What You've Got" from William Germano's *On Revision: The Only Writing That Counts*.
