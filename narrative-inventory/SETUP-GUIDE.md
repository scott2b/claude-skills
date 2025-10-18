# Narrative Inventory Skill - Setup Guide

This guide explains how to use the narrative-inventory skill in both Claude Code and Claude Desktop/claude.ai.

## Skill Overview

The narrative-inventory skill helps you create writing inventories based on William Germano's framework from *On Revision*. It analyzes your draft text and creates "lists of things" to help you understand what you have, identify gaps, and maintain focus during revision.

## Using in Claude Code (This Environment)

The skill is already installed and ready to use!

### How to Invoke
1. Simply ask Claude to help inventory your draft:
   - "Help me inventory my framework document"
   - "Create a memoranda inventory for my TeachX presentation"
   - "I need an objectives inventory for my dialogic principle chapter"

2. Or use a slash command (if configured): `/narrative-inventory`

### What Happens
- Claude will ask which draft to analyze
- It will read the file(s) from your project
- Recommend appropriate inventory type(s)
- Generate the inventory
- **Save it to your project** (you'll choose the location, e.g., `inventories/` or `process/inventories/`)

### Benefits in Claude Code
- Direct access to your project files
- Automatic saving to your chosen directory
- Can analyze multiple files at once
- Comparative analysis against your file structure

## Using in Claude Desktop/claude.ai

You can upload this same skill to Claude Desktop or claude.ai for use when you're not in Claude Code.

### Installation Steps

1. **Locate the ZIP file**: `~/.claude/skills/narrative-inventory.zip`

2. **Open Claude Desktop or claude.ai**:
   - Go to **Settings > Capabilities**
   - Find the **Skills** section (marked as "Preview")
   - Click **"Upload skill"**

3. **Upload the ZIP**:
   - Click the upload button or drag `narrative-inventory.zip` into the upload area
   - Claude will validate and install the skill
   - Enable it in your Capabilities settings

4. **Verify Installation**:
   - You should see "narrative-inventory" listed in your Skills
   - Toggle it on to activate

### How to Use in Desktop
1. Upload or paste your draft text into a chat
2. Ask Claude to help inventory it:
   - "Can you create an inventory of this draft?"
   - "Help me inventory this using the narrative-inventory skill"

3. Claude will:
   - Analyze your draft
   - Recommend inventory type(s)
   - Generate the inventory
   - **Present it as a downloadable markdown file** for you to save

### Benefits in Desktop
- Works when you're not in a project directory
- Portable across devices
- Can analyze uploaded documents or pasted text
- Great for quick inventories on the go

### Limitations in Desktop
- Cannot automatically save to a specific project directory
- You'll need to manually save the generated inventory
- Cannot search your project directory for draft files
- Each session requires uploading/pasting the draft

## Recommended Workflow

**For serious project work**: Use Claude Code
- Best for ongoing writing projects
- Automatic file management
- Full project context

**For quick reviews**: Use Claude Desktop
- Good for analyzing individual documents
- Works on any device
- No need to open full project

**Hybrid approach**:
- Generate inventories in Desktop when traveling/mobile
- Save them to your project directory when back at your computer
- Use Code for final integration and comparative analysis

## Inventory Types Available

The skill supports four types of inventories from Germano:

1. **Simple Topic/Theme**: Basic list of components to cover
2. **Topic with Concerns**: Shows where your writing is heading
3. **Objectives/Ambitions**: What you want to accomplish
4. **Memoranda**: Things not to forget, details for further study

Claude will recommend the appropriate type(s) based on your draft's state.

## File Structure

**Skill files** (in your home directory, available globally):
```
~/.claude/skills/narrative-inventory/
├── SKILL.md                          # Main skill definition
├── README.md                         # Quick reference
├── resources/
│   └── example-inventory.md          # Example output
└── narrative-inventory.zip           # Package for Desktop upload
```

**Inventory outputs** (saved in your project directory):
```
your-project/
├── inventories/                      # Suggested location
│   ├── 2025-10-17-chapter1-topics-inventory.md
│   ├── 2025-10-17-chapter1-objectives-inventory.md
│   └── ...
└── process/inventories/              # Alternative location
    └── ...
```

The skill asks where you want inventories saved in each project.

## Troubleshooting

### In Claude Code
- **Skill not found**: Try `/reload-skills`
- **Can't find draft files**: Specify the exact path or paste the text
- **Permission errors**: Check file permissions in your project directory

### In Claude Desktop
- **Upload failed**: Ensure file is under 10MB, try re-zipping
- **Skill not activating**: Make sure it's toggled on in Settings > Capabilities
- **Can't save output**: Copy the markdown and save manually to your project

## Examples

See `narrative-inventory/resources/example-inventory.md` for a complete example showing:
- What an inventory looks like
- How the comparative analysis works
- The informal, fragmentary style of inventory items

## Source Material

Based on Chapter 3 "Know What You've Got" from William Germano's *On Revision: The Only Writing That Counts*.

Key principle: Inventories are NOT outlines. They're "barely a set of notes" - working reminders to keep you focused on what matters.

## Next Steps

1. **Try it in Claude Code first** (easiest):
   - Just ask: "Help me inventory the dialogic principle document"

2. **Upload to Desktop** (for mobile use):
   - Follow the installation steps above
   - Test with a sample document

3. **Save your inventories**:
   - Decide where to keep them in your project (suggestion: `process/inventories/`)
   - Date them so you can track evolution over time

4. **Iterate**:
   - Create new inventories as your draft evolves
   - Compare earlier inventories to see how your thinking has developed

## Questions?

The skill includes detailed instructions for Claude, so it should guide the process automatically. Just ask for an inventory and let Claude walk you through the options!
