#!/bin/bash
# Basic Obsidian Vault Workflow Examples
#
# Prerequisites:
# 1. Obsidian running with Local REST API plugin enabled
# 2. OBSIDIAN_API_KEY environment variable set
# 3. Python requests library installed: pip install requests

SKILLS_DIR="$HOME/.claude/skills/obsidian/scripts"

echo "=== Obsidian Vault Workflow Examples ==="
echo

# 1. List files in vault root
echo "1. Listing files in vault root..."
python "$SKILLS_DIR/list_files.py"
echo

# 2. List files in slipbox
echo "2. Listing files in slipbox..."
python "$SKILLS_DIR/list_files.py" --path "_Slipbox/"
echo

# 3. Search for a term
echo "3. Searching vault for 'example'..."
python "$SKILLS_DIR/search_vault.py" "example" --context 50
echo

# 4. Create a test note
echo "4. Creating test note..."
python "$SKILLS_DIR/write_note.py" "Test Note.md" \
  --content "# Test Note

This is a test note created via the Obsidian skill.

## Features
- Automated note creation
- API integration
- Slipbox awareness

Created: $(date)"
echo

# 5. Read the note back
echo "5. Reading test note..."
python "$SKILLS_DIR/read_note.py" "Test Note.md"
echo

# 6. Append to the note
echo "6. Appending to test note..."
python "$SKILLS_DIR/append_note.py" "Test Note.md" \
  --content "

## Update
Added content at $(date)"
echo

# 7. Read updated note
echo "7. Reading updated note..."
python "$SKILLS_DIR/read_note.py" "Test Note.md"
echo

# 8. Get today's daily note
echo "8. Getting today's daily note..."
python "$SKILLS_DIR/periodic_notes.py" daily
echo

echo "=== Workflow complete ==="
echo
echo "To clean up test note, run:"
echo "python $SKILLS_DIR/delete_note.py 'Test Note.md' --force"
