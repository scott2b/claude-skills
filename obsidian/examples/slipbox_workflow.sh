#!/bin/bash
# Slipbox-Specific Workflow Examples
#
# Demonstrates working with the _Slipbox directory

SKILLS_DIR="$HOME/.claude/skills/obsidian/scripts"

echo "=== Slipbox Workflow Examples ==="
echo

# 1. List all slipbox notes
echo "1. Listing all slipbox notes..."
python "$SKILLS_DIR/list_files.py" --path "_Slipbox/"
echo

# 2. Search within slipbox
echo "2. Searching slipbox for concepts..."
python "$SKILLS_DIR/search_vault.py" "system" --path "_Slipbox/" --context 100
echo

# 3. Create a new slipbox note with timestamp
TIMESTAMP=$(date +%Y%m%d%H%M)
SLIPNOTE="_Slipbox/${TIMESTAMP}-api-integration.md"

echo "3. Creating new slipbox note: $SLIPNOTE"
python "$SKILLS_DIR/write_note.py" "$SLIPNOTE" --content "# API Integration

## Context
Exploring integration between Obsidian vault and external tools via REST API.

## Key Points
- Local REST API plugin enables programmatic access
- Bearer token authentication
- Full CRUD operations on notes
- Search capabilities across vault

## Related Concepts
- [[automation]]
- [[knowledge-management]]
- [[zettelkasten]]

## References
- Obsidian Local REST API: https://github.com/coddingtonbear/obsidian-local-rest-api

## Metadata
Created: $(date)
Tags: #api #obsidian #automation"
echo

# 4. Read it back
echo "4. Reading new slipbox note..."
python "$SKILLS_DIR/read_note.py" "$SLIPNOTE"
echo

# 5. Append references
echo "5. Adding backlinks..."
python "$SKILLS_DIR/append_note.py" "$SLIPNOTE" --content "

## Backlinks
Referenced in:
- [[project-notes]]
- [[technical-setup]]"
echo

# 6. Search for the new note
echo "6. Verifying note is searchable..."
python "$SKILLS_DIR/search_vault.py" "API Integration" --path "_Slipbox/"
echo

echo "=== Slipbox workflow complete ==="
echo
echo "To clean up, run:"
echo "python $SKILLS_DIR/delete_note.py '$SLIPNOTE' --force"
