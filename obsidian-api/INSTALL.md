# Obsidian Skill Installation Guide

## Step 1: Install Obsidian Local REST API Plugin

1. Open Obsidian
2. Go to **Settings → Community Plugins**
3. Click **Browse** and search for "**Local REST API**"
4. Install the plugin by **coddingtonbear**
5. Enable the plugin
6. Go to plugin settings and **copy the API key**
7. Note the server URL (default: `https://127.0.0.1:27124`)

## Step 2: Check Python Version

The skill requires Python 3.6 or later (uses built-in libraries only):

```bash
python3 --version
```

**No external dependencies required!** The skill uses Python's standard library (`urllib`, `ssl`, `json`).

## Step 3: Set Environment Variables

### Option A: Temporary (Current Session Only)

```bash
export OBSIDIAN_API_KEY=your_api_key_here
export OBSIDIAN_HOST=https://127.0.0.1:27124  # Optional, this is the default
```

### Option B: Persistent (Recommended)

Create a `.env.obsidian` file in your home directory or project:

```bash
# ~/.env.obsidian
export OBSIDIAN_API_KEY=your_api_key_here
export OBSIDIAN_HOST=https://127.0.0.1:27124
```

Then load it when needed:
```bash
source ~/.env.obsidian
```

### Option C: Add to Shell Profile

Add to your `~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`:

**Bash/Zsh:**
```bash
export OBSIDIAN_API_KEY=your_api_key_here
export OBSIDIAN_HOST=https://127.0.0.1:27124
```

**Fish:**
```fish
set -x OBSIDIAN_API_KEY your_api_key_here
set -x OBSIDIAN_HOST https://127.0.0.1:27124
```

## Step 4: Verify Installation

Test the connection:

```bash
python3 ~/.claude/skills/obsidian/scripts/obsidian_api.py
```

Expected output:
```
✓ Connected to Obsidian vault (N files in root)
```

## Step 5: Test Basic Operations

List files in your vault:
```bash
python3 ~/.claude/skills/obsidian/scripts/list_files.py
```

Search your vault:
```bash
python3 ~/.claude/skills/obsidian/scripts/search_vault.py "your search term"
```

## Troubleshooting

### "Cannot connect to Obsidian"
- Verify Obsidian is running
- Check Local REST API plugin is enabled
- Confirm plugin is running (check plugin settings)

### "401 Unauthorized"
- Verify `OBSIDIAN_API_KEY` is set correctly
- Check API key hasn't changed in plugin settings
- Test: `echo $OBSIDIAN_API_KEY` (should show your key)

### "404 Not Found"
- File path must be relative to vault root
- Include `.md` extension
- Use forward slashes in paths

### SSL Certificate Errors
The plugin uses a self-signed certificate by default. If you get SSL errors:
```bash
export OBSIDIAN_VERIFY_SSL=false
```

## Using with Claude Code

Once installed, Claude Code will automatically detect and use this skill when you:
- Mention "Obsidian", "vault", or "slipbox" in your requests
- Ask to search, read, or create notes
- Request operations on your knowledge base

The skill is **proactive** and will invoke automatically when appropriate.

## Example Workflows

See the `examples/` directory for complete workflow scripts:
- `basic_workflow.sh` - Basic vault operations
- `slipbox_workflow.sh` - Slipbox-specific workflows

Run them:
```bash
~/.claude/skills/obsidian/examples/basic_workflow.sh
```

## Security Notes

- Your API key grants **full access** to your vault
- Store it securely (environment variables, not in code)
- The API is only accessible on localhost by default
- Treat the API key like a password

## Need Help?

- Check the plugin docs: https://github.com/coddingtonbear/obsidian-local-rest-api
- Review the skill README: `~/.claude/skills/obsidian/README.md`
- Check Claude Code docs: https://docs.claude.com/claude-code
