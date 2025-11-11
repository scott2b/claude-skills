# Distillation Strategies

This reference provides detailed strategies for identifying essential vs. generalizable content when distilling skills.

## Core Strategy: Lexical Trigger Identification

The foundation of distillation is identifying the **minimum lexical context** needed to activate the model's semantic knowledge.

### What Makes a Good Lexical Trigger?

**Essential characteristics:**
1. **Specificity** - Uniquely identifies the framework/methodology
2. **Semantic activation** - Triggers broader knowledge domain in the model
3. **Irreplaceable** - Cannot be inferred from general knowledge
4. **Terminologically precise** - Uses exact terms from the source framework

**Examples of strong lexical triggers:**
- "John Truby's twenty-two-step story structure" (specific framework + author)
- "opponent must want the SAME goal as hero" (critical unique principle)
- "revelations sequence" (specific technique with precise term)
- "weakness and need, desire, opponent, plan, battle, self-revelation, new equilibrium" (the seven key steps)

**Examples of weak lexical triggers (too general):**
- "story structure" (too broad, doesn't activate specific knowledge)
- "character development" (universal concept, not unique to framework)
- "plot points" (generic term, lacks specificity)

### Framework Attribution Pattern

Always include the originator when distilling framework-based skills:

**Pattern:** `[Author/Creator]'s [Specific Framework/Methodology Name]`

**Examples:**
- John Truby's story structure
- William Germano's narrative mapping
- Donald Knuth's literate programming
- Marie Kondo's organization method

**Why this works:** The attribution serves as a powerful lexical anchor that activates the model's knowledge of that specific person's body of work and methodology.

## Content Classification System

Use this system to classify every section of the baseline skill:

### Category 1: Essential Lexical (KEEP)

**Identification markers:**
- Specific terminology unique to the framework
- Critical distinctions that differentiate this approach
- Key principles that govern application
- Precise names of steps/components/elements
- Unique procedural sequences

**Preservation level:** Keep verbatim or minimally condensed

**Examples:**
- "The opponent must want the SAME goal as the hero (not just oppose the hero)"
- "Step 14: Apparent Defeat - occurs two-thirds to three-quarters through the story"
- "Progressive disclosure: metadata → SKILL.md → bundled resources"

### Category 2: Unique Procedural (KEEP)

**Identification markers:**
- Novel workflows not standard in general knowledge
- Non-obvious sequences or approaches
- Specific tool usage patterns
- Critical warnings or constraints
- Proprietary information

**Preservation level:** Keep in detail, potentially condensing explanations but maintaining substance

**Examples:**
- "Get current date using `date +%Y-%m-%d` command" (specific instruction)
- "Check if source IS available in context before warning" (unique to lexical-recall-guard)
- "Separate the reveals from the rest of the plot and examine them as one unit" (unique technique)

### Category 3: Illustrative Examples (CONDENSE)

**Identification markers:**
- Examples of concepts the model already understands
- Multiple examples illustrating the same point
- Detailed walkthroughs of standard procedures
- Extended case studies

**Reduction strategy:**
- Keep 1 illustrative example, remove redundant ones
- Condense detailed examples to brief references
- Replace verbose walkthroughs with concise summaries
- Reference well-known examples by name only

**Before distillation:**
```
For example, in Casablanca, Rick's weakness is cynicism and isolation...
[500 words of detailed analysis]

Another example: In Tootsie, Michael's weakness is his inability to...
[500 words of detailed analysis]

A third example: In Alien, Ripley's weakness initially appears to be...
[400 words of detailed analysis]
```

**After distillation:**
```
Examples: Rick's cynicism (Casablanca), Michael's self-centeredness (Tootsie),
Ripley's initial deference to authority (Alien).
```

### Category 4: Background Theory (CONDENSE)

**Identification markers:**
- General explanations of common concepts
- Background context available in model's training
- Definitions of standard terms
- Broad theoretical foundations

**Reduction strategy:**
- Replace detailed explanations with concise references
- Assume model knows general concepts
- Keep only what's unique to this framework

**Before distillation:**
```
A protagonist is the main character in a story who drives the action forward.
The protagonist typically wants something (a goal or desire) and faces obstacles
in pursuing that goal. Throughout classic story structure, the protagonist
undergoes a transformation or character arc...
[300 words explaining basic protagonist concept]
```

**After distillation:**
```
In Truby's framework, the protagonist's weakness and need establish the transformation arc.
```

### Category 5: Verbose Explanations (CONDENSE)

**Identification markers:**
- Repetitive phrasing
- Overly detailed step-by-step of known procedures
- Extensive elaboration on simple concepts
- Multiple ways of saying the same thing

**Reduction strategy:**
- Condense to single clear statement
- Use concise imperative language
- Remove redundant explanations

**Before distillation:**
```
When you begin working on distilling a skill, the first thing you should do is
read through the entire skill completely from start to finish. This means reading
the SKILL.md file in its entirety, and also reading all of the bundled resources
that are included with the skill, such as the references directory, the assets
directory, and the scripts directory. By reading everything thoroughly, you'll
get a complete understanding of what the skill does and how it works.
```

**After distillation:**
```
Read the complete skill: SKILL.md and all bundled resources (references, assets, scripts).
```

## Domain-Specific Strategies

### Well-Known Published Frameworks

**Characteristics:**
- Based on published books, papers, or methodologies
- Author/creator is well-known in the field
- Likely included in model's training data

**Strategy:**
- Maximum distillation potential
- Focus on author attribution and specific terminology
- Assume model knows general theory
- Preserve unique techniques and critical distinctions

**Distillation ratio target:** 50-70% reduction

**Examples:**
- John Truby's story structure
- William Germano's academic writing framework
- Donald Knuth's algorithms
- Martin Fowler's refactoring patterns

### Niche Documented Methodologies

**Characteristics:**
- Published but less widely known
- Model may have partial knowledge
- Some unique aspects may need more detail

**Strategy:**
- Moderate distillation
- Provide more context for niche concepts
- Preserve more examples and explanations
- Keep critical procedural details

**Distillation ratio target:** 30-50% reduction

**Examples:**
- Specialized technical frameworks
- Domain-specific methodologies
- Recent publications (post-training cutoff)

### Proprietary/Company-Specific Content

**Characteristics:**
- Internal systems or processes
- Not publicly documented
- Model has no existing knowledge

**Strategy:**
- Minimal to no distillation appropriate
- Detail is necessary, not redundant
- Focus only on condensing verbose language
- Preserve all substantive content

**Distillation ratio target:** 0-20% reduction (primarily language tightening)

**Examples:**
- Company-specific APIs
- Internal database schemas
- Proprietary workflows
- Custom tool integrations

## Red Flags: When NOT to Distill

**Stop and reconsider if:**

1. **Proprietary knowledge dominates**
   - The skill is primarily about internal/unique systems
   - Little to no published framework foundation

2. **Already concise**
   - Skill is under 3,000 tokens
   - Content is already tightly written

3. **Detail serves critical function**
   - Examples are essential for complex concepts
   - Step-by-step detail is non-obvious
   - Warnings and constraints are extensive

4. **High risk of capability loss**
   - Procedural knowledge is intricate and unique
   - Removal of detail would compromise functionality
   - Skill's value is in the comprehensive detail

5. **Post-training knowledge**
   - Framework/methodology published after model's training cutoff
   - Model has no existing knowledge to activate

## Progressive Reduction Technique

When uncertain about how much to reduce, use progressive reduction:

### Phase 1: Conservative Distillation (20-30% reduction)
- Remove only obviously redundant content
- Condense verbose language
- Eliminate repetitive examples
- Test capability preservation

### Phase 2: Moderate Distillation (40-50% reduction)
- Assume model knows general concepts
- Replace detailed explanations with references
- Keep minimal illustrative examples
- Verify capability preservation

### Phase 3: Aggressive Distillation (60-70% reduction)
- Rely heavily on semantic activation
- Preserve only essential lexical triggers
- Minimal examples (or reference by name only)
- Rigorous capability verification required

**Recommendation:** Start with Phase 1, validate, then proceed to Phase 2 if appropriate. Only attempt Phase 3 for very well-known frameworks with high confidence in model's existing knowledge.

## Validation Through Self-Querying

Before finalizing distillation, use self-awareness validation:

**Ask yourself (the model):**

1. "If I encountered this distilled skill, would I know what to do?"
2. "Do the lexical triggers activate the right knowledge domain in my memory?"
3. "Are there any procedures here that would be unclear without more detail?"
4. "What specific information is truly unique that I wouldn't know otherwise?"
5. "Would a fresh instance of me (without conversation context) have the same capabilities with this distilled version?"

**If answers reveal gaps:** Add back necessary detail

**If answers confirm sufficiency:** Distillation is appropriate

## Token Estimation Guidelines

**Rough token conversion:**
- 750 characters ≈ 1,000 tokens
- 1 word ≈ 1.3 tokens (average)
- 1 line of code ≈ 15-25 tokens

**Measuring sections:**
- Copy section text to character counter
- Divide character count by 750
- Multiply by 1,000 for approximate tokens

**Targeting reduction:**
- Identify highest token sections first
- Focus distillation effort on large sections
- Small sections (<500 tokens) may not warrant detailed analysis

---

*Use these strategies systematically during the distillation process to achieve optimal token reduction while preserving capabilities.*
