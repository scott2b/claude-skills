---
name: "narrative-keywords"
description: "Identify and analyze key terms and concepts in your writing using William Germano's keyword framework to track conceptual threads and ensure consistent deployment of important ideas"
---

# Narrative Keywords

This skill helps writers identify, track, and analyze the keywords in their draft text using William Germano's framework from *On Revision*. Keywords are the powerful terms and concepts that carry the energy and significance of your writing—the words that readers should see as key to your study.

## Purpose

The keyword exercise helps you:
- Find the significant points or themes in your project
- See how concepts and words are distributed across your text
- Determine if key terms appear where you thought they did
- Assess whether you're saying what you hoped to say about important concepts
- Decide if keywords should be threaded throughout or isolated within chapters
- Track the frequency and placement of crucial terminology
- Keep energy flowing through your writing

As Germano notes: "Keywords can help you to keep the energy flowing through your writing. Think electricity. At the very least, knowing where your keywords are located will tell you where the sockets are."

## When to Invoke This Skill

Invoke this skill when:
- You've completed a draft and want to analyze its conceptual structure
- You need to see how key terms are distributed across chapters or sections
- You're unsure if your most important concepts appear where they should
- You want to identify which terms are doing "key work" in your text
- You need to decide whether to thread concepts throughout or isolate them
- You're revising and want to strengthen conceptual threads and continuities
- You want to ensure readers will see certain terms as key to your study

## The Keyword Concept (from Germano)

### What Keywords Are

Keywords are the powerful words and concepts central to your work. Inspired by Raymond Williams's *Keywords: A Vocabulary of Culture and Society* (1976), they are terms that carry cultural meaning and valence—the terminology that makes your discipline tick.

In your writing, keywords are:
- Concepts and words you want to carry through the entirety of your text
- Terms that do "key work" in your argument
- Ideas that readers should recognize as central to your study
- Threads that build reminders and continuities for readers

### Keywords Are About Distribution

The keyword exercise isn't just about identifying important terms—it's about seeing **how you've distributed your ingredients**. A keyword search reveals:
- Where powerful words occur in your text
- Whether they appear where you thought they did
- If you're saying what you hoped to say about them
- How frequency and placement support (or undermine) your argument

### Strategic Deployment

There's no rule that keywords must appear regularly throughout your text. The question is whether your deployment is **intentional**:
- Some keywords may thread throughout, creating continuity
- Others may be crucial in only one portion of the text
- If you plan to discuss a term in only one section, know why
- Take the opportunity to see what concepts you want to carry through

## Task Instructions

When this skill is invoked, follow these steps:

### Step 1: Detect Environment & Understand Context

**First, determine your environment:**
- If you have access to a project directory and file system tools (Read, Write, Edit, Glob, Grep): You are in **Claude Code**
- If the user uploaded files or you're working in a chat without direct project access: You are in **Claude Desktop/Web**

**Then understand the writing context:**
1. Ask the user which draft or section they want to analyze for keywords
2. In Claude Code: If not specified, search for main writing files in the project
3. In Claude Desktop: Ask the user to share the draft text (upload file or paste text)
4. Read the draft text to understand its scope and content

### Step 2: Identify Candidate Keywords

Work with the writer to identify potential keywords. There are two approaches:

**A. Writer-Supplied List:**
Ask the writer: "What terms do you think are key to what you've written? What powerful words are central to your study?"

Create a list of candidates based on:
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
5. **Assess context**: When you look at actual usage, does the writer say what they hoped to say?

Create a keyword distribution analysis showing:
```
KEYWORD: [term]
Total occurrences: [number]
Distribution:
  - Chapter/Section 1: [count] occurrences
  - Chapter/Section 2: [count] occurrences
  - etc.
Pattern: [threaded throughout / concentrated in X / appears early then disappears / etc.]
```

### Step 4: Evaluate Deployment Strategy

For each keyword, help the writer consider:

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
1. Ask where to save keyword analyses (suggest `keywords/` or `process/keywords/`)
2. Create the chosen directory if it doesn't exist
3. Save with descriptive filename: `YYYY-MM-DD-[draft-name]-keywords.md`
4. Include both the keyword list and distribution analysis
5. Confirm the save location to the user

**If in Claude Desktop/Web (no project directory):**
1. Create the keyword analysis as a formatted markdown artifact or downloadable file
2. Present it in the chat for the user to review
3. Suggest the user save it with filename: `YYYY-MM-DD-[draft-name]-keywords.md`
4. Offer to create visualizations or additional formats if requested

## Important Principles

### Start with Writer's Intentions

The keyword list should begin with what the writer believes is important. The analysis then shows whether the text matches those intentions.

### Distribution Matters

It's not just about whether keywords appear, but **where** they appear and **how often**. Distribution reveals the actual structure of your argument.

### No Fixed Formula

There's no rule about how often keywords should appear. The goal is **intentional deployment** that serves your purpose.

### Keywords Build Continuity

Readers appreciate threads built out of reminders and continuities. Strategic keyword deployment helps readers track your argument.

### Use Technology

Simple electronic search is powerful. Use it to call up each occurrence, see exactly where terms occur, and adjust frequency and placement.

### Be Willing to Adjust

If the analysis reveals that keywords don't appear where you thought, or that you're not saying what you hoped—that's valuable information for revision.

## Output Format

When presenting a keyword analysis:

```markdown
# Keyword Analysis for [Draft Name]
**Date**: [YYYY-MM-DD]
**Draft analyzed**: [file path or description]

## Candidate Keywords

The following keywords were identified for analysis:
[list of keywords and why they were selected]

## Keyword Distribution Analysis

### [KEYWORD 1]
- **Total occurrences**: [number]
- **Distribution pattern**: [description]
- **Locations**:
  - [Section 1]: [count] occurrences (pages X-Y)
  - [Section 2]: [count] occurrences (pages X-Y)
- **Assessment**: [Does this match writer's intentions? Should it be threaded more/less?]

### [KEYWORD 2]
[repeat format]

## Strategic Observations

### Keywords Threaded Throughout
- [List keywords that successfully create continuity across the text]

### Keywords Concentrated in Specific Sections
- [List keywords that appear primarily in isolated sections]
- [Assess whether this isolation is intentional and effective]

### Keywords with Unexpected Distribution
- [List keywords that don't appear where expected]
- [Note gaps or surprising concentrations]

## Recommendations

### To Strengthen Conceptual Threads
- [Suggestions for threading keywords more consistently]
- [Terms that could be introduced earlier]
- [Concepts that need more consistent deployment]

### To Improve Strategic Focus
- [Keywords that might work better isolated in specific sections]
- [Terms that may be overused]
- [Concepts that need more prominence]

### Questions for the Writer
- [Are there keywords missing from this analysis?]
- [Should certain terms appear more/less frequently?]
- [Are the current distribution patterns intentional?]

---
*Remember: Knowing where your keywords are located tells you where the sockets are. Use this information to keep energy flowing through your writing.*
```

## Examples from Germano

### Example: Polar Environmental Crisis

A writer summarizes their project:
> "I'm writing a history of the polar environmental crisis that considers global warming as a means of reconfiguring how we understand and measure time."

**Key terms identified**: *polar, environmental, crisis, time*

These keywords "name two enormous and very different geographic areas; *environmental* and *crisis*, which are now unfortunately inseparable, gesture toward large concepts in our modernity. Then there's *time*."

**Analysis question**: "How will the terms be deployed in the draft? Will they appear throughout, or only in two of seven chapters? Are these keywords threads that run throughout the work?"

### Example: Evasive Behavior Study

In working notes, *depression* is a keyword, and the writer makes a strong case for its importance in chapter 1. Chapter 2 focuses on *misdirection*. Chapter 3 uses *denial* and *self-esteem* a lot.

**Analysis questions**:
- Will the text read better if you draw keywords across chapters?
- Or more successful if you isolate concepts within individual chapters?
- Use the technology: simple electronic search shows exactly where terms occur
- Adjust frequency and placement based on your intentions

## What This Skill Does NOT Do

- Prescribe specific keyword frequencies or distributions
- Impose external standards about what terms should be keywords
- Replace the writer's judgment about what's important
- Automatically "fix" keyword problems (it identifies patterns for the writer to evaluate)
- Create keywords where none exist (it works with the text you have)

## Integration with Other Tools

This skill works alongside:
- **Inventory skill** (identifies themes and topics; keywords shows their distribution)
- **Mapping skill** (visualizes structure; keywords shows conceptual threads)
- **Structural analysis tools** (used later in revision)
- Text analysis and visualization tools (for advanced users)

---

*Based on William Germano's "Keywords" section in the "Know What You've Got" chapter of On Revision: The Only Writing That Counts*
