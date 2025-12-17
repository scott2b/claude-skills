---
name: story-structure-crime-distilled
description: Analyze and develop crime genre story structure using John Truby's Crime framework to create morally complex narratives about justice, legality vs morality, and the thin line between cop and criminal. Token-optimized distilled version. (user)
---

# Story Structure: Crime Genre (Distilled)

**PRIMARY DELIVERABLE: This skill creates timestamped reference documents saved to files.**

This skill helps writers analyze and develop crime story structure using John Truby's framework from *The Anatomy of Genres* chapter 7.

## Critical: File Output is MANDATORY

**Success = A dated file exists (e.g., `2025-12-16-story-name-crime-structure.md`)**
**Failure = Only conversational output with no saved file**

## Purpose

Crime is fictional moral philosophy. Stories about people who break the law and those who catch them, exploring the difference between what is legal and what is moral. The hero can be cop or criminal—mirror images on either side of the law.

**Central theme**: Life is constant moral accounting. What one owes vs what one is owed. In a social world, the books must balance. If not, conflict follows.

## When to Invoke This Skill

Use when creating:
- Stories about criminals and law enforcement in moral conflict
- Master criminal characters who think they're above society
- Cat-and-mouse games between equally matched opponents
- Stories where legality and morality diverge
- Moral accounting over a lifetime (Epic Crime Tragedy or Crime Black Comedy)
- Narratives exploring the thin line between cop and criminal

**Note**: Layers on top of basic structure. Use **story-structure-7-steps** or **story-structure-22-step** first if foundation undefined.

## Bundled Resources

**References:**
- `references/crime-beats-distilled.md` - Concise beat explanations and key principles

**Assets:**
- `assets/crime-structure-template.md` - Structure analysis template
- `assets/moral-code-template.md` - Character moral code template
- `assets/opponent-plan-template.md` - Opponent's intricate plan template

## Task Instructions

### Step 1: Establish Output Location FIRST

**In Claude Code:**
1. Get date: `date +%Y-%m-%d`
2. Ask where to save (suggest `structure/`)
3. Note filename: `YYYY-MM-DD-[story-name]-crime-structure.md`

**In Claude Desktop/Web:**
1. Note output as markdown artifact
2. Remind user to save with timestamp

### Step 2: Understand Story Context

1. Which story to analyze
2. Search project files (Claude Code) or ask user (Desktop)
3. Is this:
   - New crime story needing structure
   - Existing draft with problems
   - Genre diagnosis

**Genre check**: Crime characteristics—someone breaks law, focus on contest (not detection), moral accounting central, questions if illegal = immoral.

### Step 3: Assess Basic Structure Foundation

**Check if established:**
- Weakness/need, desire, opponent, plan, battle, self-revelation, new equilibrium

**If undefined**: Recommend **story-structure-7-steps** or **22-step** FIRST, then return.

**If exists**: Proceed with Crime layer.

### Step 4: Determine Crime Variation

**Hero Type:**
- [ ] Cop as Hero (Enforcer) - Desire: catch criminal. Master cop, regular but especially good.
- [ ] Criminal as Hero (Outlaw) - Desire: money/power/win game. Make partially justified.

**Story Form:**
- [ ] Standard Crime - Linear, cat-and-mouse, violent battle/reveal
- [ ] Epic Crime Tragedy - Lost potential, moral accounting over lifetime, rigid moral system
- [ ] Crime Black Comedy - Moral code as destructive system, extreme passion + lack of knowledge

### Step 5: Work Through Crime Story Beats (15 Beats)

Apply Truby's Crime beats:

1. **Story World** - Superficial society, slavery. Extremes: no crime (chaos) or police state.
2. **Inciting Event - Crime** - Ingenious crime catapults criminal to wealth/power. More deception = better.
3. **Hero Strengths/Weakness-Need** - Cop: master cop, doesn't fit society. Criminal: brilliant, feels superior.
4. **Values and Moral Code** - Write detailed code. Cop: law holy, brotherhood. Criminal: honor among thieves, omertà.
5. **Desire** - Cop: catch criminal (not find truth). Criminal: money/power/game.
6. **Opponent - Super Criminal** - Master criminal/cop. SAME goal as hero. Mirror image. Equal ability.
7. **Drive - Cat and Mouse** - Series of wits and force conflicts. Obsessive cop goes too far, acts like criminal.
8. **Opponent's Plan** - **CRUCIAL, OFTEN MISSING**. Intricate hidden attacks. More intricate + hidden = better plot.
9. **Revelation - Criminal Uncovered** - Trickery, deception. Artist of crime.
10. **Drive - Moral Argument** - Illegal actions lead to tighter moral bind. Express through plot, not heavy-handed.
11. **Apparent Defeat** - Criminal escapes or wins major victory.
12. **Gate-Gauntlet-Visit to Death - Chase** - Cat and mouse at top speed.
13. **Violent Battle or Big Revelation** - Final confrontation or big reveal (closer to end = better).
14. **Self-Revelation** - Society reaffirmed, society loses, or mixed.
15. **Poetic Justice** - Payment in kind, unique to crime, karmic reckoning, by offender's own hand.

### Step 6: Work Through Morality Beats (For Transcendent Crime)

For Epic Crime Tragedy or Crime Black Comedy, add 8 morality beats:

1. **Story World - Moral Universe** - Responsibility and choice defined. All actions have moral consequences.
2. **Character Web - Moral Code** - Detailed code in 3 pivotal moments: beginning, middle, end.
3. **Opposition - Good vs Right** - Ends (what's valuable) vs means (doesn't harm others).
4. **Plan - Values and Actions** - Game plan for desirable goals using only proper actions.
5. **Drive - Ends vs Means** - Hero takes immoral actions. Should individual put right above good?
6. **Attack by Ally - Shame/Guilt** - Ally confronts hero. Mind punishes itself.
7. **Battle, Moral Self-Revelation, Moral Decision** - Two choices. Must affect others + involve sacrifice.
8. **Thematic Revelation** - What audience learns about how people should act.

**Key technique**: Never-ending moral challenge—constantly test moral fiber. Each episode/section has unique moral challenge.

### Step 7: Track Sequences

**Revelations Sequence:**
- Extract all major reveals (target 7-10)
- Logical order? Build in intensity? Increase in pace?
- Best reveals are about opponent

**Moral Decisions Sequence (Transcendent):**
- Extract all moral decisions
- Build in difficulty? Build in stakes?
- Show character change (decline or growth)?
- How far pushed toward darkness?

### Step 8: Assess Organic Connections

Verify connections:
- Story World ↔ Weakness
- Crime ↔ Desire
- Desire ↔ Opponent (SAME goal?)
- Opponent ↔ Weakness (necessary opponent?)
- Moral Code ↔ Actions
- Cat and Mouse ↔ Equal Ability
- Revelations ↔ Opponent's Plan
- Moral Decisions ↔ Theme
- Self-Revelation ↔ Society
- Conclusion ↔ Poetic Justice

### Step 9: Provide Analysis and Recommendations

**For new stories:**
- Moral universe defined?
- Hero and opponent equally matched?
- Opponent's plan intricate and hidden? (Most common weakness)
- Moral code detailed?
- Crime beats present?
- Which variation?

**For existing drafts:**
- Which beats present/missing?
- Is opponent's plan detailed enough?
- Do revelations build or stall?
- Are moral decisions tracked?
- Moral argument expressed through plot?

### Step 10: Save Documentation (REQUIRED)

**MANDATORY: Task incomplete until file saved.**

**If in Claude Code:**
1. Create directory: `mkdir -p structure`
2. Write file: `YYYY-MM-DD-[story-name]-crime-structure.md`
3. Use `assets/crime-structure-template.md` format
4. Offer supplementary docs (moral-code, opponent-plan)
5. Confirm save location

**Validation before completing:**
- [ ] Date obtained
- [ ] Save location confirmed
- [ ] Analysis completed
- [ ] File written
- [ ] Path confirmed

**If in Claude Desktop/Web:**
1. Create markdown artifact
2. Remind to save with timestamp
3. Offer supplementary docs

## Key Principles

- **Moral argument paramount**: Crime is fictional moral philosophy
- **Opponent's plan crucial**: Most writers miss this. More intricate + hidden = better
- **Cop and criminal as mirrors**: Can be either; should be similar in key ways
- **Equal ability essential**: Both best at their jobs for heavyweight fight
- **Deception improves plot**: More deception = better
- **Same goal required**: Opponent wants SAME goal as hero
- **Moral code detailed**: Write specific rules and values
- **Cop crosses line**: Standard technique—overcomes through deception
- **Plan reveals early**: At beginning; make each part of interconnected campaign
- **Poetic justice**: Payment appropriate to crime
- **Plot carries moral argument**: Not heavy-handed—action leads to cover-up leads to bind
- **Moral decisions build**: Sequence so they build in difficulty
- **Character is destiny**: Responsible for results and moral effects
- **Freedom = Justice**: Justice optimizes freedom for everyone
- **Good vs Right**: Ends (valuable) vs means (doesn't harm others)
- **Final decision**: Funnel complexity to single choice between two

## Examples Reference

- **Breaking Bad** - Crime Black Comedy, moral accounting over lifetime, how far push toward darkness
- **In Bruges** - Crime Black Comedy, moral code as destructive system, poetic justice masterclass
- **The Dark Knight** - Epic Crime Tragedy, Joker as Dark Philosopher, moral conundrums sequence
- **Crime and Punishment** - Foundational Epic Crime Tragedy, guilt is punishment, mind as courtroom
- **Fargo** - Crime Black Comedy, passion + ignorance = deadly world
- **The Usual Suspects** - Greatest reveal in Crime history, deception mastery

## Important Reminders

- Layer on basic structure (7-step or 22-step)
- Hero can be cop OR criminal
- Opponent's plan is the most important and most often missing beat
- Express moral argument through plot, not statement
- Poetic justice: payment in kind, by offender's own hand
- "Character is destiny" (Heraclitus)
- Justice optimizes freedom for everyone
- Attack by ally during middle
- Final moral decision must affect others + involve sacrifice

## Integration with Other Skills

- **story-structure-7-steps** - Foundation; Crime builds on it
- **story-structure-22-step** - For complex Crime, use 22 steps first
- **symbol-web** - Deepens moral argument symbolism
- **narrative-inventory** - Catalogues; Crime shows genre elements
- **narrative-keywords** - Identifies justice, morality, responsibility themes

---

*Based on John Truby's "Crime: Morality and Justice" from The Anatomy of Genres: How Story Forms Explain the Way the World Works*
