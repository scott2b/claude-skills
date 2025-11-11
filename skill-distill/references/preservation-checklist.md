# Preservation Checklist

Use this checklist to verify that the distilled skill preserves all essential capabilities of the baseline skill.

## Pre-Distillation Assessment

Before beginning distillation, document the baseline skill's capabilities:

### Core Capabilities Inventory

- [ ] **Primary purpose**: What is the skill's main function?
- [ ] **Key features**: List 3-5 essential capabilities
- [ ] **Unique procedures**: What workflows are specific to this skill?
- [ ] **Critical distinctions**: What makes this approach different/unique?
- [ ] **Expected outcomes**: What should users be able to achieve?

**Document these** before distillation to use as a reference point.

## During Distillation: Section-by-Section Check

As you distill each section, verify:

### Frontmatter
- [ ] Name updated to `[original-name]-distilled`
- [ ] Description remains accurate and complete
- [ ] Description notes it's a distilled/token-optimized version

### Purpose Section
- [ ] Core function is clearly stated
- [ ] Primary purpose is unchanged from baseline
- [ ] Condensed but not oversimplified

### When to Invoke Section
- [ ] Key trigger scenarios are preserved
- [ ] Important constraints (when NOT to use) are included
- [ ] Sufficient for users to know when to invoke

### Core Methodology/Instructions
- [ ] Essential lexical triggers are present
- [ ] Framework/methodology attribution is included
- [ ] Critical distinctions are preserved
- [ ] Unique principles are stated
- [ ] Key terminology is intact

### Procedural Steps
- [ ] All essential steps are present (even if condensed)
- [ ] Unique/non-obvious procedures are detailed
- [ ] Step sequence is preserved
- [ ] Critical warnings are included
- [ ] Tool usage instructions are clear

### Examples
- [ ] At least one illustrative example per major concept (if needed)
- [ ] Examples that clarify unique/complex concepts are kept
- [ ] Redundant examples are removed
- [ ] Well-known examples are referenced (not detailed)

### Bundled Resources
- [ ] Essential scripts are preserved
- [ ] References with unique information are kept
- [ ] Critical assets/templates are included
- [ ] Generalizable references are condensed or removed

## Post-Distillation Validation

After completing distillation, perform these validation checks:

### Capability Preservation Test

**For each core capability from the baseline:**

#### Capability 1: [Name]
- [ ] Present in distilled version
- [ ] Sufficiently detailed to execute
- [ ] Lexical triggers adequate to activate semantic knowledge
- [ ] Unique procedural knowledge preserved
- [ ] **Status**: ☐ Fully preserved ☐ Partially preserved ☐ Lost

#### Capability 2: [Name]
- [ ] Present in distilled version
- [ ] Sufficiently detailed to execute
- [ ] Lexical triggers adequate to activate semantic knowledge
- [ ] Unique procedural knowledge preserved
- [ ] **Status**: ☐ Fully preserved ☐ Partially preserved ☐ Lost

#### Capability 3: [Name]
- [ ] Present in distilled version
- [ ] Sufficiently detailed to execute
- [ ] Lexical triggers adequate to activate semantic knowledge
- [ ] Unique procedural knowledge preserved
- [ ] **Status**: ☐ Fully preserved ☐ Partially preserved ☐ Lost

*(Add more capabilities as needed)*

### Critical Elements Check

- [ ] **Framework attribution**: Author/source is clearly stated
- [ ] **Terminology**: All unique/specific terms are present
- [ ] **Distinctions**: Critical differentiators are preserved
- [ ] **Principles**: Key governing rules are stated
- [ ] **Warnings**: Important constraints/pitfalls are included
- [ ] **Workflow**: Unique procedural sequences are intact
- [ ] **Tool usage**: Specific tool instructions are clear
- [ ] **Output format**: Expected deliverables are defined

### Semantic Activation Test

**Self-query validation** (ask yourself as the model):

- [ ] Do the lexical triggers successfully activate relevant knowledge?
- [ ] Can I mentally execute the skill with the distilled instructions?
- [ ] Are there procedures that would be unclear without more context?
- [ ] Would a fresh model instance have the same capabilities?
- [ ] Is any truly unique information missing?

### Comparison Analysis

**Side-by-side assessment:**

| Element | Baseline Skill | Distilled Skill | Status |
|---------|---------------|-----------------|---------|
| Core function | [Describe] | [Describe] | ☐ Same ☐ Different |
| Key feature 1 | [Describe] | [Describe] | ☐ Same ☐ Different |
| Key feature 2 | [Describe] | [Describe] | ☐ Same ☐ Different |
| Unique procedure | [Describe] | [Describe] | ☐ Same ☐ Different |
| Critical distinction | [Describe] | [Describe] | ☐ Same ☐ Different |

**Result:**
- [ ] All elements marked "Same" → Capabilities preserved
- [ ] Any elements marked "Different" → Review for necessary restoration

### Token Reduction Assessment

**Calculate reduction:**
- Baseline tokens: _______
- Distilled tokens: _______
- Reduction: _______ tokens (______%)

**Evaluate effectiveness:**
- [ ] Reduction ≥ 40%: Excellent distillation
- [ ] Reduction 20-40%: Moderate distillation
- [ ] Reduction < 20%: Minimal distillation (consider if worthwhile)
- [ ] Reduction > 80%: High reduction (verify capabilities carefully)

### Red Flag Check

**Stop and review if any are true:**

- [ ] Core capability is compromised or unclear
- [ ] Unique procedural knowledge is lost
- [ ] Critical distinctions are removed or diluted
- [ ] User couldn't achieve expected outcomes
- [ ] Distilled version is confusing or ambiguous
- [ ] Essential terminology is missing
- [ ] Framework attribution is unclear or absent

**If red flags are present:** Add necessary detail back to restore capabilities.

## Use Case Simulation

Test the distilled skill against real-world scenarios:

### Scenario 1: [Typical Use Case]
**Task**: [Describe task]
- [ ] Distilled skill provides sufficient guidance
- [ ] Outcome achievable with distilled instructions
- [ ] No critical steps or information missing

### Scenario 2: [Complex Use Case]
**Task**: [Describe task]
- [ ] Distilled skill handles complexity adequately
- [ ] Unique procedures are clear enough to execute
- [ ] Outcome achievable with distilled instructions

### Scenario 3: [Edge Case]
**Task**: [Describe task]
- [ ] Distilled skill addresses edge case
- [ ] Constraints/warnings are sufficient
- [ ] Outcome achievable with distilled instructions

## Final Approval Checklist

Before finalizing the distilled skill:

### Quality Gates

- [ ] **Capability preservation**: All core capabilities fully preserved
- [ ] **Clarity**: Instructions are clear and unambiguous
- [ ] **Completeness**: All essential elements present
- [ ] **Conciseness**: Verbose content reduced without losing substance
- [ ] **Correctness**: No errors introduced during distillation
- [ ] **Token efficiency**: Meaningful reduction achieved (≥20%)

### Documentation

- [ ] Comparison summary created
- [ ] Token reduction documented
- [ ] Changes enumerated (what was removed, what was kept)
- [ ] Validation results recorded
- [ ] Testing recommendations provided

### Deliverables Ready

- [ ] Distilled skill directory created
- [ ] SKILL.md written and validated
- [ ] Bundled resources included (if any)
- [ ] Proper naming convention followed (`[name]-distilled`)
- [ ] YAML frontmatter correct
- [ ] Ready for packaging

## Restoration Guidance

If validation reveals capability loss, restore detail for:

### Always Restore
1. **Unique procedural sequences** - Non-obvious workflows
2. **Critical distinctions** - What makes this approach different
3. **Essential terminology** - Specific framework terms
4. **Key principles** - Governing rules and guidelines
5. **Important warnings** - Critical constraints or pitfalls

### Selectively Restore
1. **Examples** - Add back if concept is complex or unique
2. **Explanations** - Restore if procedure is non-obvious
3. **Context** - Add if lexical triggers prove insufficient
4. **Details** - Restore if semantic activation doesn't work

### Rarely Need to Restore
1. **Redundant examples** - One example is usually sufficient
2. **Verbose explanations** - Concise versions typically adequate
3. **General theory** - Model usually has semantic knowledge
4. **Standard procedures** - Model knows common workflows

## Version Control

Track distillation iterations:

### Version Log

**v1.0 - [Date]**
- Initial distillation
- Reduction: ____%
- Issues: [List any problems]

**v1.1 - [Date]**
- Restored: [What was added back]
- Reason: [Why restoration was needed]
- Reduction: ____%

**Final Version: v[X.X]**
- Final reduction: ____%
- Capabilities: All preserved
- Validation: Complete

---

*Use this checklist systematically to ensure distilled skills maintain the full capabilities of their baseline versions while achieving significant token reduction.*
