---
name: skill-distill
description: Distills existing skills to their essential form by leveraging the model's self-awareness of semantic recall capabilities. Creates token-efficient distilled versions that preserve capabilities while reducing token consumption by identifying necessary lexical context and generalizing aspects the model already knows.
---

# Skill Distill

## Purpose

This skill addresses the challenge of large, comprehensive skills consuming excessive tokens when invoked. While detailed skills are valuable, they often contain extensive lexical detail (examples, comprehensive explanations, references) that may already exist in the model's semantic memory.

**Core function:** Create distilled versions of existing skills that preserve the same capabilities while dramatically reducing token consumption by providing only the essential lexical context needed to activate the model's latent semantic knowledge.

## When to Invoke This Skill

Use this skill when:
- An existing skill consumes excessive tokens (>10,000 tokens) when invoked
- A skill contains extensive examples, detailed explanations, or comprehensive references
- The skill's domain is based on well-known frameworks, methodologies, or systems that the model was likely trained on
- Token efficiency is critical for the skill's practical usage
- Evaluation shows high token costs per skill invocation
- The skill needs optimization without losing core capabilities

**Do NOT use for:**
- Skills with truly proprietary information unknown to the model
- Skills relying on company-specific schemas, APIs, or internal systems
- Skills where the detail is unique procedural knowledge
- Very small skills (<2,000 tokens) where distillation provides minimal benefit

## Theory: Lexical vs. Semantic Recall Awareness

### Foundation

LLMs have different capabilities for different types of recall:
- **Semantic recall** (strong): General concepts, patterns, frameworks, methodologies the model was trained on
- **Lexical recall** (weak): Exact quotes, specific exhaustive lists, verbatim details

### Application to Skill Distillation

Large skills often contain extensive lexical detail about topics the model already has semantic knowledge of. By identifying:
1. **Essential lexical triggers** - Specific terminology, framework names, key concepts that activate latent knowledge
2. **Generalizable content** - Aspects the model already knows semantically that can be referenced rather than detailed
3. **True unique knowledge** - Genuinely novel information that must be preserved

The model can create a distilled version that provides minimum lexical context to "unlock" existing semantic knowledge, achieving the same capability with a fraction of the tokens.

### Self-Awareness Approach

The model creating the distilled version relies on self-understanding:
- "What do I already know about this topic/framework/methodology?"
- "What specific terms or concepts would trigger my existing knowledge?"
- "What is truly unique in this skill versus what I already know?"
- "What minimum context would I need to activate the right knowledge domain?"

## Bundled Resources

**References:**
- `references/distillation-strategies.md` - Detailed strategies for identifying essential vs. generalizable content
- `references/preservation-checklist.md` - Checklist to ensure distilled version preserves capabilities

**Assets:**
- `assets/distilled-skill-template.md` - Template structure for distilled skills

## Distillation Process

### Step 1: Analyze the Baseline Skill

**Read the baseline skill completely:**
1. Read the full SKILL.md of the skill to be distilled
2. Read all bundled resources (references, assets, scripts)
3. Count approximate tokens (rough estimate: ~750 characters = 1000 tokens)
4. Identify the skill's core capabilities and functions

**Assess token consumption:**
- Total tokens in SKILL.md body (excluding frontmatter)
- Tokens in bundled resources that would be loaded into context
- Identify the largest token consumers (verbose sections, extensive examples, detailed explanations)

### Step 2: Identify the Knowledge Domain

**Determine what the skill is based on:**
- Well-known framework or methodology? (e.g., "John Truby's 22-step story structure")
- Published system or process? (e.g., "William Germano's narrative mapping")
- Technical specification or standard? (e.g., "PDF/A format specification")
- Industry practice or convention? (e.g., "agile sprint planning")
- Proprietary or unique system? (e.g., company-specific workflow)

**Assess model's existing knowledge:**
Ask yourself (the model): "How much do I already know about this domain?"
- If well-known published framework: High existing knowledge
- If niche but documented methodology: Moderate existing knowledge
- If proprietary internal system: Little to no existing knowledge

**For high existing knowledge:** Distillation will be most effective
**For little/no existing knowledge:** Distillation may not be appropriate; detail is necessary

### Step 3: Extract Essential Lexical Triggers

Identify the minimum lexical context needed to activate semantic knowledge:

**Essential lexical triggers include:**
1. **Specific terminology**: Unique terms that define the domain
   - Example: "John Truby's twenty-two steps", "William Germano's narrative keywords"

2. **Framework structure**: Names of key components or steps
   - Example: "weakness and need, desire, opponent, plan, battle, self-revelation, new equilibrium"

3. **Critical distinctions**: Unique concepts that differentiate this approach
   - Example: "opponent must want the SAME goal as hero", "revelations must build in intensity"

4. **Key principles**: Core rules or guidelines that govern application
   - Example: "organic plot vs. mechanical plot", "lexical recall vs. semantic recall"

5. **Procedural anchors**: Specific workflow steps unique to this skill
   - Example: "separate reveals from plot and examine as one unit"

**Extract from baseline skill:**
- Create a list of terms, concepts, and phrases that are essential triggers
- Focus on what is UNIQUE and SPECIFIC to this framework/methodology
- Exclude general examples that illustrate concepts the model already understands

### Step 4: Identify Generalizable Content

Determine what can be reduced or referenced rather than detailed:

**Generalizable content includes:**
1. **Explanatory examples** where the concept is already known
   - If the skill explains "protagonist wants a goal" with extensive examples, the concept is known

2. **Background theory** available in the model's training
   - General storytelling principles, common methodology explanations

3. **Standard procedures** the model already knows
   - "Read the file", "analyze the structure", "provide recommendations"

4. **Verbose explanations** of concepts already understood
   - Instead of 500 words explaining "character arc", reference "character transformation arc"

**Reduction strategies:**
- Replace extensive explanations with concise references
- Remove redundant examples (keep 1 illustrative example instead of 5)
- Condense background theory to essential points
- Generalize standard procedures instead of step-by-step detail

### Step 5: Preserve Unique Procedural Knowledge

**Critical preservation:** Ensure truly unique aspects are NOT reduced:

**Must preserve in detail:**
1. **Novel procedures** not standard in the model's knowledge
   - Unique workflows specific to this skill
   - Non-obvious sequences or approaches

2. **Proprietary information** or unique schemas
   - Company-specific APIs, database schemas, internal systems

3. **Specific tool usage** patterns unique to this skill
   - When to use Read vs. Grep for this particular workflow
   - Unique file naming conventions or output formats

4. **Critical warnings** or important constraints
   - Common pitfalls specific to this methodology
   - Essential "do not" instructions

**Use the preservation checklist:** Consult `references/preservation-checklist.md` to verify nothing critical is lost.

### Step 6: Create the Distilled Skill

**Structure the distilled version:**

1. **Frontmatter**: Same name with "-distilled" suffix, update description to note it's distilled
   ```yaml
   ---
   name: original-skill-name-distilled
   description: [Concise version of original description] Token-optimized distilled version.
   ---
   ```

2. **Purpose section**: Condense to 2-3 sentences capturing core function

3. **When to Invoke**: Keep concise, focus on key scenarios

4. **Core methodology**: Replace extensive explanations with:
   - Essential lexical triggers identified in Step 3
   - Concise procedural steps
   - References to framework/methodology by name
   - Critical distinctions and principles only

5. **Procedural instructions**: Streamline to essential steps
   - Remove verbose explanations
   - Keep unique procedural knowledge (Step 5)
   - Use concise imperative language
   - Reference known concepts rather than explaining them

6. **Bundled resources**:
   - Remove or condense references that contain generalizable content
   - Preserve references with truly unique information
   - Keep essential assets (templates, scripts)

**Create the new skill file:**
- Create directory: `[original-skill-name]-distilled/`
- Write the distilled SKILL.md
- Copy/condense necessary bundled resources

### Step 7: Validate Capability Preservation

**Test that the distilled version preserves capabilities:**

**Capability checklist:**
1. **Core function**: Does the distilled skill achieve the same primary purpose?
2. **Key features**: Are all essential capabilities still present?
3. **Unique procedures**: Is unique procedural knowledge intact?
4. **Critical distinctions**: Are important differentiators preserved?
5. **Workflow completeness**: Can the user achieve the same outcomes?

**Quality checks:**
- Read the distilled version as if encountering it fresh
- Mentally simulate using it for the skill's primary use cases
- Verify essential lexical triggers are sufficient to activate semantic knowledge
- Confirm nothing critical was lost in reduction

**Use the preservation checklist:** Consult `references/preservation-checklist.md` systematically.

### Step 8: Measure Token Reduction

**Calculate the improvement:**
1. Baseline skill total tokens (approximate)
2. Distilled skill total tokens (approximate)
3. Reduction percentage
4. Tokens saved per invocation

**Assess effectiveness:**
- Target: 40-70% token reduction for well-known frameworks
- If reduction is minimal (<20%): Skill may not be suitable for distillation
- If reduction is extreme (>80%): Verify capabilities are preserved

**Report to user:**
- Token reduction achieved
- Key changes made
- Any capabilities that required preservation of detail
- Recommended testing approach

### Step 9: Package the Distilled Skill

**Validate and package:**
1. Validate the distilled skill structure (YAML, naming, description)
2. Create proper directory structure with bundled resources
3. Package using the packaging script if available
4. Provide both the distilled skill and comparison summary

**Deliverables:**
- Distilled skill directory/package
- Comparison document showing:
  - Token reduction achieved
  - What was distilled (generalizable content removed)
  - What was preserved (unique knowledge retained)
  - Capability verification checklist

## Key Principles

1. **Semantic activation over lexical detail**: Provide triggers that activate existing knowledge rather than re-teaching known concepts
2. **Self-aware distillation**: Use the model's understanding of what it knows to guide reduction
3. **Preserve the unique**: Never reduce truly novel or proprietary information
4. **Lexical precision where essential**: Keep specific terminology and critical distinctions
5. **Capability preservation**: The distilled version must achieve the same outcomes
6. **Appropriate targets**: Best for skills based on well-known published frameworks/methodologies
7. **Measure and validate**: Always verify token reduction and capability preservation

## What This Skill Does NOT Do

- Create skills from scratch (use skill-creator for new skills)
- Improve or enhance skill capabilities (only distills existing capabilities)
- Work for all skills (proprietary/unique content needs the detail)
- Eliminate all examples (keeps essential illustrative examples)
- Replace testing and validation (distilled skills still need verification)
- Guarantee exact same output (optimizes for same capabilities, not identical behavior)

## Integration with Other Skills

This skill works alongside:
- **skill-creator** - Creates new skills; skill-distill optimizes existing skills
- **lexical-recall-guard** - Uses same lexical/semantic recall awareness theory
- Domain-specific skills - Any comprehensive skill based on known frameworks can be distilled

---

*This skill implements token optimization through lexical/semantic recall awareness, creating efficient skill versions that leverage the model's existing knowledge.*
