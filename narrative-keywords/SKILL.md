---
name: "narrative-keywords"
description: "Identify and analyze key terms and concepts in your writing using William Germano's keyword framework to track conceptual threads and ensure consistent deployment of important ideas"
---

# Narrative Keywords

This skill helps writers identify, track, and analyze keywords in their draft text using William Germano's framework from *On Revision*. Keywords are the powerful terms and concepts that carry the energy and significance of writing—the words that readers should see as key to the study.

## Purpose

The keyword exercise helps writers find significant points or themes in their project, see how concepts and words are distributed across text, determine if key terms appear where intended, assess whether the text says what was hoped about important concepts, decide if keywords should be threaded throughout or isolated within chapters, track frequency and placement of crucial terminology, and keep energy flowing through writing.

## When to Invoke This Skill

Invoke this skill when writers need to:
- Analyze the conceptual structure of a completed draft
- See how key terms are distributed across chapters or sections
- Determine if important concepts appear where they should
- Identify which terms are doing "key work" in the text
- Decide whether to thread concepts throughout or isolate them
- Strengthen conceptual threads and continuities during revision
- Ensure readers will see certain terms as key to the study

## Bundled Resources

**References:**
- `references/germano-framework.md` - Detailed explanation of keywords concept, distribution principles, strategic deployment strategies, and examples from Germano (polar environmental crisis, evasive behavior study)

**Assets:**
- `assets/keywords-template.md` - Template for keyword analysis output

## Task Instructions

When this skill is invoked, follow these steps to create a keyword analysis.

### Step 1: Detect Environment & Understand Context

**Determine the environment:**
- With access to project directory and file system tools (Read, Write, Edit, Glob, Grep): Claude Code environment
- With uploaded files or chat without direct project access: Claude Desktop/Web environment

**Understand the writing context:**
1. Ask which draft or section to analyze for keywords
2. In Claude Code: If not specified, search for main writing files in the project
3. In Claude Desktop: Ask to share the draft text (upload file or paste text)
4. Read the draft text to understand scope and content

### Step 2: Identify Candidate Keywords

Work with the writer to identify potential keywords. Use one or both approaches:

**A. Writer-Supplied List:**
Ask: "What terms are key to what has been written? What powerful words are central to this study?"

Create a list based on:
- The writer's stated intentions
- Terms they believe are important to their argument
- Concepts they want readers to recognize as central

**B. Text-Derived List:**
Analyze the draft to identify:
- Discipline-specific terminology that appears multiple times
- Conceptual terms that seem to carry theoretical weight
- Words that cluster around the writer's apparent argument
- Terms that seem to be doing important work in the text

**Recommend 8-15 candidate keywords** for analysis. Present this list to the writer and ask them to confirm, modify, or prioritize which terms to search for.

### Step 3: Search and Analyze Keywords

For each confirmed keyword:

1. **Search the text** to find all occurrences
2. **Record locations**: Note which chapters/sections contain each term
3. **Count frequency**: How many times does each keyword appear overall and per section?
4. **Analyze distribution**: Is the term threaded throughout or concentrated in specific areas?
5. **Assess context**: When looking at actual usage, does the writer say what they hoped to say?

Create a keyword distribution analysis showing:
```
KEYWORD: [term]
Total occurrences: [number]
Distribution:
  - Chapter/Section 1: [count] occurrences
  - Chapter/Section 2: [count] occurrences
Pattern: [threaded throughout / concentrated in X / appears early then disappears / etc.]
```

### Step 4: Evaluate Deployment Strategy

For each keyword, help the writer consider deployment strategy. Consult `references/germano-framework.md` for detailed principles on threading vs. isolation.

**Threading vs. Isolation:**
- Will the text read better if this keyword appears across chapters?
- Or would it be more effective isolated within individual chapters?
- Does current distribution match the writer's intentions?

**Frequency and Placement:**
- Do keywords occur where the writer thought they did?
- Are there unexpected gaps or concentrations?
- Does the distribution support the argument?

**Intentionality:**
- If a keyword appears in only one section, is there a good reason?
- Are there terms that should appear more consistently?
- Are any keywords overused or underused?

### Step 5: Provide Recommendations

Based on the analysis, suggest:

**Strengthening Threads:**
- Keywords that could be introduced earlier
- Terms that appear late but might benefit from earlier grounding
- Concepts that could create stronger continuity if threaded throughout

**Adjusting Frequency:**
- Keywords that may be overused (losing impact)
- Important terms that are underdeployed
- Opportunities to adjust placement for better effect

**Strategic Isolation:**
- Terms that might work better concentrated in specific sections
- Reasons why isolating certain keywords could strengthen focus

### Step 6: Optional Advanced Analysis

If the writer is interested in more sophisticated analysis:

**Text Mining Techniques:**
- Use word cluster analysis to visualize relationships between keywords
- Create frequency visualizations showing distribution patterns
- Identify co-occurrence patterns (which keywords appear together)
- Generate heat maps showing keyword density across the text

**Comparative Analysis:**
- Compare keyword usage in different chapters
- Identify which sections are keyword-rich vs. keyword-poor
- Analyze whether keyword distribution aligns with structural divisions

### Step 7: Save or Present the Analysis

**If in Claude Code (project directory access):**
1. Get current date using `date +%Y-%m-%d` command
2. Ask where to save keyword analyses (suggest `keywords/` or `process/keywords/`)
3. Create the chosen directory if it doesn't exist
4. Save with descriptive filename using actual date: `YYYY-MM-DD-[draft-name]-keywords.md`
5. Use the structure from `assets/keywords-template.md`
6. Include both the keyword list and distribution analysis
7. Confirm the save location to the user

**If in Claude Desktop/Web (no project directory):**
1. Create the keyword analysis as a formatted markdown artifact or downloadable file
2. Present it in the chat for review
3. Suggest saving with filename using current date: `YYYY-MM-DD-[draft-name]-keywords.md`
4. Use the structure from `assets/keywords-template.md`
5. Offer to create visualizations or additional formats if requested

## Important Reminders

- **Start with intentions**: Begin with what the writer believes is important
- **Distribution matters**: It's not just whether keywords appear, but where and how often
- **No fixed formula**: The goal is intentional deployment that serves the purpose
- **Keywords build continuity**: Strategic deployment helps readers track the argument
- **Use technology**: Simple electronic search is powerful for analysis
- **Be willing to adjust**: If keywords don't appear where expected, that's valuable information

**Reference**: See `references/germano-framework.md` for detailed principles, strategic deployment guidance, and examples.

## What This Skill Does NOT Do

- Prescribe specific keyword frequencies or distributions
- Impose external standards about what terms should be keywords
- Replace the writer's judgment about what's important
- Automatically "fix" keyword problems (it identifies patterns for evaluation)
- Create keywords where none exist (it works with the text that exists)

## Integration with Other Skills

This skill works alongside:
- **narrative-inventory** - identifies themes and topics; keywords shows their distribution
- **narrative-maps** - visualizes structure; keywords shows conceptual threads
- Structural analysis tools (used later in revision)
- Text analysis and visualization tools (for advanced users)

---

*Based on William Germano's "Keywords" section in the "Know What You've Got" chapter of On Revision: The Only Writing That Counts*
