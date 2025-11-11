---
name: skill-api-conversion
description: Convert an existing skill to an API-friendly version by removing procedural bloat, file operations, and bash commands while preserving analytical depth. Creates new skill with -api suffix.
---

# Skill API Conversion

Convert existing skills to API-friendly versions optimized for Anthropic API usage where file operations and shell commands cause token bloat and completion budget exhaustion.

## Purpose

When skills designed for Claude Code (local environment with file access) are used via the Anthropic API, they often fail because:
1. **Token bloat**: Procedural multi-step instructions trigger bash commands, heredocs, and intermediate file writes that consume the 8K completion token budget before returning actual output
2. **Tool availability**: Write, Edit, Bash tools may not be available in API context
3. **Execution model**: API needs immediate response output, not file artifacts

This skill converts existing skills to API-optimized versions that:
- Return output immediately in response (not as files)
- Avoid all bash commands, date commands, heredocs, and file operations
- Preserve analytical depth, quality checks, and domain knowledge
- Include explicit "DO NOT" instructions to prevent token-burning behaviors
- Provide clear output templates for consistent results

## When to Invoke

Use this skill when:
- An existing skill works in Claude Code but fails or produces empty output via API
- Token usage analysis shows completion budget exhausted (finishReason: "length") with minimal output
- A skill needs to work in API context where Write/Bash tools unavailable
- Creating API version of a skill that writes files or uses shell commands

## Conversion Process

### Step 1: Read Existing Skill

Read the complete SKILL.md of the skill to be converted. If skill path not provided, ask user which skill to convert.

Also check for bundled resources (references/, assets/, scripts/) that may contribute to token bloat.

### Step 2: Analyze Current Structure

Identify elements causing API issues:

**Token bloat sources to remove:**
- Multi-step procedural workflows ("Step 1: Do X, Step 2: Do Y, Step 3: Do Z")
- Bash command instructions (especially `date`, `mkdir`, `cat`, heredocs)
- File operation workflows (Write tool, Edit tool, directory creation)
- Conditional file-saving logic ("If Claude Code... If Desktop...")
- Commands that echo content (printing intermediate drafts, templates, outlines)
- Questions-then-actions patterns that delay output

**Elements to preserve:**
- Core framework/methodology (step names, principles, key concepts)
- Analytical depth (quality checks, assessment criteria, verification steps)
- Domain knowledge (critical distinctions, best practices)
- Output structure/template (what analysis should contain)
- Integration with other skills
- "What This Skill Does NOT Do" sections

### Step 3: Create API-Optimized Skill Structure

Transform the skill using these patterns:

#### Remove Procedural Multi-Step Workflows

**Before:**
```markdown
### Step 1: Detect Environment & Context
**Determine environment:**
- Claude Code: Has Read/Write/Edit/Glob/Grep
- Claude Desktop/Web: Ask user to share materials

### Step 2: Ask Questions
Ask which story to analyze...

### Step 3: Choose Approach
Ask writer which approach fits...

### Step 4: Work Through Analysis
For each element, ask questions...

### Step 5: Create Documentation
If Write tool available:
  1. Get date using `date +%Y-%m-%d`
  2. Ask where to save
  3. Create directory
  4. Save file
```

**After:**
```markdown
## Analysis Approach

Determine analysis type:
- **Forward Development**: New work - analyze systematically
- **Reverse Engineering**: Existing work - identify present/missing elements
- **Diagnosis**: Specific problem - focus on issue

## Output Instructions

**IMMEDIATELY return the complete analysis directly in your response using this structure:**

[Include complete output template here]

**CRITICAL - DO NOT:**
- Use bash commands or date command
- Create files or use heredocs
- Execute code or print intermediate drafts
- Ask follow-up questions before providing analysis
- Reference file paths or directories
```

#### Consolidate Quality Checks as Reference

Keep quality checks and analytical guidance, but format as reference checklist rather than procedural steps:

**Pattern:**
```markdown
## Quality Checks - Ensure Analysis Covers:

**[Category Name]:**
- [Check 1]
- [Check 2]
- [Key question to address]

**[Next Category]:**
- [Checks...]
```

This preserves analytical depth without triggering step-by-step execution behaviors.

#### Add Explicit Output Template

Provide complete output template in markdown format so Claude knows exactly what to return:

```markdown
## Output Instructions

**IMMEDIATELY return the complete [analysis/report/structure] directly in your response using this structure:**

```markdown
# [Output Title]

**[Metadata fields]**: [Values]

## [Section 1]
[Detailed template showing all fields to fill]

## [Section 2]
[Template continued...]

## ASSESSMENT
**Strengths**: [What works]
**Weaknesses**: [What needs work]
**Recommendations**: [Next steps]
```
```

#### Add Critical "DO NOT" Section

Always include explicit prohibitions:

```markdown
**CRITICAL - DO NOT:**
- Use bash commands or date command
- Create files or use heredocs
- Execute code or print intermediate drafts
- Ask follow-up questions before providing analysis
- Reference file paths or directories

**Just return the complete analysis immediately in your response.**
```

### Step 4: Preserve Essential Domain Knowledge

Ensure these elements remain intact:

**Core Framework**: All step names, principles, key concepts from original methodology
**Critical Distinctions**: Unique aspects that differentiate this framework
**Quality Standards**: Benchmarks, industry standards, best practices
**Assessment Criteria**: How to evaluate quality, completeness, correctness
**Integration Notes**: How skill works with other skills

### Step 5: Handle Bundled Resources

**Templates (assets/)**: Keep minimal, condensed versions. Reference them in output template but don't instruct to use Write tool.

**References**: Evaluate if needed. Large reference files add token cost. If essential domain knowledge can be summarized in SKILL.md, do so.

**Scripts**: Remove entirely. API version cannot execute scripts and shouldn't reference them.

### Step 6: Create New Skill Directory

Create new skill with `-api` suffix and assets directory if needed for condensed templates.

### Step 7: Write API-Optimized SKILL.md

Create the new SKILL.md with:

**Frontmatter:**
```yaml
---
name: [original-name]-api
description: [Concise description]. Returns complete [output] directly in response.
---
```

**Structure:**
1. Title and brief purpose (2-3 sentences)
2. Core framework/methodology (condensed - just the essentials)
3. Critical principles (key concepts, distinctions)
4. Analysis approach (types of use, not step-by-step procedure)
5. Quality checks (ensure analysis covers X, formatted as reference checklist)
6. **Output Instructions** (with complete template and "CRITICAL - DO NOT" section)
7. Integration notes (if applicable)

**Target length**: Aim for 1,200-1,800 words (~1,600-2,400 tokens) for complex analytical skills. Simpler skills can be even shorter.

### Step 8: Copy Condensed Templates (if needed)

If original skill has templates in assets/:
1. Read original templates
2. Create condensed versions (remove verbose prompts, consolidate fields)
3. Save to new skill's assets/ directory

### Step 9: Package API Skill

Use packaging script to create distributable zip:

```bash
python3 /Users/scott/.claude/skills/skill-creator/scripts/package_skill.py /Users/scott/.claude/skills/[skill-name]-api
```

### Step 10: Provide Comparison Summary

Report to user:

**Token Reduction:**
- Original skill: [word count] (~[token estimate])
- API skill: [word count] (~[token estimate])
- Reduction: [percentage]%

**What Was Removed:**
- [List major removals: procedural steps, bash commands, file operations, etc.]

**What Was Preserved:**
- [List core capabilities: framework, quality checks, analytical depth]

**Usage:**
- Original skill path: [path]
- API skill path: [path]
- API skill package: [zip path]

## Conversion Best Practices

**Balance depth and brevity:**
- Preserve analytical guidance (what to check, assess, verify)
- Remove procedural bloat (how to execute, step-by-step workflows)
- Keep critical distinctions and domain knowledge
- Remove verbose examples if core concept is clear

**Output template completeness:**
- Include ALL sections the analysis should contain
- Show exact field structure with placeholder text
- Make it clear what needs to be filled in
- Provide examples inline if helpful for clarity

**Explicit prohibitions:**
- Always include "CRITICAL - DO NOT" section
- List specific problem behaviors discovered during testing
- Be explicit about bash, date, files, heredocs, code execution

**Test token efficiency:**
- After conversion, check word count and estimate tokens
- Original skill ~4K+ tokens → API should be ~1.5-2.5K tokens
- If still high, identify remaining verbose sections

**Validate preservation:**
- Core framework/methodology intact?
- Quality checks and assessment criteria present?
- Critical distinctions and principles preserved?
- Output structure complete and clear?

## Common Patterns by Skill Type

### Analytical/Framework Skills
(e.g., story-structure, code-review, research-analysis)

**Keep:**
- Framework steps/principles
- Quality assessment criteria
- Analytical checklist
- Output template with all sections

**Remove:**
- File-saving workflows
- Date/directory commands
- Multi-step "ask then do" procedures
- Environment detection

### Generative/Template Skills
(e.g., document-generator, report-builder)

**Keep:**
- Template structure in output instructions
- Content requirements
- Quality standards

**Remove:**
- Template file writing
- Heredoc examples
- File path management

**Pattern:** Show complete template inline in output instructions, not as separate file.

### Research/Investigation Skills
(e.g., codebase-explorer, documentation-finder)

**Keep:**
- Search strategies
- Assessment criteria
- Synthesis approach

**Remove:**
- Tool-specific workflows (Grep/Read procedures)
- Report file writing
- Directory creation

**Pattern:** Return findings directly in structured response.

## What This Skill Does NOT Do

- Modify the original skill (creates new -api version)
- Test the converted skill automatically
- Handle skills that fundamentally require file access to function
- Convert skills that execute scripts (scripts cannot run in API)
- Guarantee identical output quality (optimizes for API constraints)

## Integration with Other Skills

- **skill-creator**: Creates new skills; skill-api-conversion optimizes for API
- **skill-distill**: Reduces token usage via semantic recall; skill-api-conversion removes procedural bloat
- Original skills: Work in Claude Code; API versions work via Anthropic API

---

*This skill captures lessons from converting story-structure-22-step to API-optimized version*
