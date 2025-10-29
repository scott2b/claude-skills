---
name: delegate
description: Intelligently analyzes tasks and delegates them to the most appropriate AI system when delegation adds value (project, gitignored)
config:
  alwaysAllow: false
  dangerous: false
---

You are running the delegation skill. Your job is to analyze tasks and determine if delegation to another AI system would provide value, and if so, delegate appropriately.

## MANDATORY: All Delegations Must Use tmux

**Non-negotiable rule:** Every delegation to another AI system MUST be executed inside a tmux session. This applies to ALL tools (Gemini, OpenCode, Codex, etc.) regardless of whether they have "batch mode" or non-interactive flags.

**Why this is mandatory:**
- Delegation commands can take 2+ minutes to complete
- Running directly blocks the terminal and wastes context
- User cannot interact with Claude Code while blocked
- Violates the core principle of asynchronous delegation

**Enforcement:** Before executing ANY delegation command, verify it starts with:
```bash
tmux new-session -d -s delegate-[name]
```

If you catch yourself about to run a delegation tool directly (e.g., `opencode run`, `gemini -p`, `codex`), STOP and wrap it in tmux first.

## Critical: When NOT to Delegate

**DO NOT delegate if any of these apply:**
- Simple conversational requests (greetings, questions, explanations)
- Tasks that can be answered immediately without tools
- Trivial tasks that take less effort to do than to delegate
- Tasks where the current AI (Claude Code) is already optimal
- Tasks that don't involve coding, analysis, or content generation
- Single-file reads or simple searches

**Examples of tasks to handle directly:**
- "say hello" → Just respond "Hello!"
- "what time is it?" → Check and respond directly
- "explain what X does" → Explain directly
- "read file.py" → Use Read tool directly

## When Delegation Makes Sense

Delegate when:
1. Task requires specialized capabilities not available here
2. Task benefits from a different model's strengths
3. Task involves substantial work better suited to another system
4. User explicitly requests a specific AI system

## Available AI Systems

### Claude Code (`claude-code`)
**When to delegate:**
- RARELY - You ARE Claude Code
- Only if user explicitly requests a fresh Claude Code session
- Complex multi-session workflows where isolation is needed

**Invocation:** Interactive CLI only
**Note:** Not suitable for batch automation

### Codex (`codex`)
**When to delegate:**
- Quick code generation when you need fast iteration
- User specifically requests Codex
- Simple scripts/utilities where speed > sophistication

**Check availability first:**
```bash
codex --help
```

**Invocation for batch mode:**
Currently not reliable for tmux automation due to:
- Interactive approval prompts
- Model availability varies by account
- No stable non-interactive mode

**Recommendation:** Only delegate if you can verify batch mode works

### Gemini (`gemini`)
**When to delegate:**
- Tasks requiring current web data/search
- Image generation or multimodal work
- Document analysis with visual components
- User specifically requests Gemini

**Check availability:**
```bash
gemini --help
```

**Invocation for batch mode:**
```bash
gemini -m gemini-2.5-pro -p "your prompt here"
```

**Flags:**
- `-m MODEL`: Specify model (gemini-2.5-pro, gemini-2.0-flash-exp)
- `-p PROMPT`: Prompt text (required for batch mode)
- `-y` or `--yolo`: Skip confirmations for autonomous operation

### OpenCode (`opencode`)
**When to delegate:**
- Ultra-fast code generation
- User specifically requests OpenCode/Grok
- Rapid prototyping where speed is critical

**Path:** `/Users/sbb/.opencode/bin/opencode`

**Check availability:**
```bash
/Users/sbb/.opencode/bin/opencode --help
```

**Important:** OpenCode expects to work with files/directories, not conversational queries. Only delegate actual coding tasks.

## Delegation Process

### Step 1: Task Classification

**Analyze the task:**
- What is the actual request?
- Can I handle this directly right now?
- Does delegation add real value?
- What type of work is required?

**Decision tree:**
1. Is it conversational/trivial? → Handle directly, DO NOT delegate
2. Is it a coding task and I'm already optimal? → Handle directly
3. Does it need special capabilities (web search, image gen)? → Consider delegation
4. Did user request specific AI? → Delegate to that system

### Step 2: Verify Tool Availability

Before delegating, verify the tool exists and supports batch mode:

```bash
# Check if tool exists
command -v gemini >/dev/null 2>&1 && echo "Available" || echo "Not found"

# Check help/usage
gemini --help
```

If tool isn't available or doesn't support batch mode, inform user and offer alternatives.

### Step 3: Validate Task Suitability

For each AI system, verify the task type matches:
- **Gemini**: Has `-p` flag for prompts, supports `-y` for auto-approval
- **OpenCode**: Expects directory/file context, not conversational
- **Codex**: May require interactive mode, check before delegating

### Step 4: Execute Delegation (if appropriate)

**CRITICAL RULE: ALL DELEGATIONS MUST USE TMUX - NO EXCEPTIONS**

Delegation commands can take minutes to complete. Running them directly blocks the terminal and violates the core purpose of delegation. ALWAYS use tmux, even if the tool has a "batch mode" flag.

**Standard tmux delegation pattern:**
```bash
# 1. Create descriptive tmux session
tmux new-session -d -s delegate-[descriptive-name]

# 2. Send command to session
tmux send-keys -t delegate-[name] 'COMMAND_HERE' C-m

# 3. Wait briefly for startup
sleep 3

# 4. Check initial output for errors
tmux capture-pane -t delegate-[name] -p -S -50

# 5. Poll periodically until complete
# Then capture full output
```

**Per-tool delegation commands:**

**Gemini:**
```bash
tmux new-session -d -s delegate-gemini
tmux send-keys -t delegate-gemini 'gemini -m gemini-2.5-pro -y -p "task description"' C-m
sleep 3
tmux capture-pane -t delegate-gemini -p -S -50
```

**OpenCode:**
```bash
tmux new-session -d -s delegate-opencode
tmux send-keys -t delegate-opencode 'cd /path/to/project && /Users/sbb/.opencode/bin/opencode run "task description"' C-m
sleep 3
tmux capture-pane -t delegate-opencode -p -S -50
# Note: OpenCode can take 2+ minutes, check periodically
```

**Codex:**
```bash
tmux new-session -d -s delegate-codex
tmux send-keys -t delegate-codex 'cd /path/to/project && codex "task description"' C-m
sleep 3
tmux capture-pane -t delegate-codex -p -S -50
```

### Step 5: Monitor and Report

**After launching in tmux, you must monitor the delegation:**

1. **Initial check (after 3-5 seconds):**
   ```bash
   tmux capture-pane -t delegate-[name] -p -S -50
   ```
   - Verify it started without immediate errors
   - Check if tool is responding

2. **Periodic polling (every 10-15 seconds):**
   ```bash
   # Check if still running
   tmux list-panes -t delegate-[name] -F "#{pane_pid}" 2>/dev/null

   # Capture recent output
   tmux capture-pane -t delegate-[name] -p -S -100
   ```
   - For quick tasks (Gemini): Poll 2-3 times
   - For long tasks (OpenCode): Poll 5-10 times or until completion indicators appear

3. **Completion detection:**
   - Look for shell prompt return
   - Look for "Done", "Completed", or error messages
   - If uncertain, capture full scrollback:
     ```bash
     tmux capture-pane -t delegate-[name] -p -S -10000
     ```

4. **Report to user:**
   - Session name for manual inspection: `delegate-[name]`
   - Summary of what was accomplished
   - Any errors or issues encountered
   - Command to attach: `tmux attach -t delegate-[name]`

**DO NOT:**
- Assume completion without checking output
- Kill sessions immediately (let user inspect if needed)
- Report success if errors occurred

## Error Handling

**If delegation fails:**
1. Capture the error message
2. Determine if it's a:
   - Tool availability issue → Inform user, suggest alternatives
   - Syntax/flag issue → Try corrected syntax once
   - Task unsuitability issue → Handle directly instead
3. DO NOT retry more than once with the same approach
4. Fall back to handling directly if delegation isn't working

## Examples

### Example 1: Trivial Task (Do NOT Delegate)
**Task:** "say hello"

**Analysis:** This is trivial conversational response.

**Action:** Respond directly with "Hello!"

**DO NOT:** Create tmux sessions, invoke other AIs, etc.

---

### Example 2: Image Generation (Delegate to Gemini)
**Task:** "Generate an image of a sunset over mountains"

**Analysis:**
- Requires image generation capability
- Gemini supports this, Claude Code doesn't
- Clear value in delegation

**Action:**
1. Verify gemini is available
2. Check if it supports image generation
3. Use tmux to delegate with proper flags
4. Return result to user

---

### Example 3: Code Refactoring (Handle Directly)
**Task:** "Refactor this component to use hooks"

**Analysis:**
- This is a coding task
- Claude Code (me) is excellent at this
- No special capabilities needed
- Delegation adds no value

**Action:** Handle directly using Edit/Read tools

---

### Example 4: Web Research (Delegate to Gemini)
**Task:** "What are the latest features in React 19?"

**Analysis:**
- Requires current web data
- Gemini has web search capability
- Claude Code has knowledge cutoff

**Action:** Delegate to Gemini with web search enabled

## Key Principles

1. **Efficiency first**: Don't delegate trivial tasks
2. **Validate before executing**: Check tools exist and support needed mode
3. **Fail fast**: One retry max, then fall back
4. **User transparency**: Explain why delegating or not delegating
5. **Clean execution**: Use correct flags, proper escaping, error handling
6. **Know your limits**: Be honest when you're the best tool for the job

## Cleanup

After delegation completes:
```bash
# Kill session when done
tmux kill-session -t delegate-[name]
```

Or inform user how to access session:
```bash
# User can attach to see full interaction
tmux attach -t delegate-[name]
```
