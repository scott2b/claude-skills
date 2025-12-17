---
name: story-structure-crime
description: Analyze and develop crime genre story structure using John Truby's Crime framework to create morally complex narratives about justice, legality vs morality, and the thin line between cop and criminal (user)
---

# Story Structure: Crime Genre

**PRIMARY DELIVERABLE: This skill creates timestamped reference documents saved to files.**

This skill helps writers analyze and develop crime story structure using John Truby's framework from *The Anatomy of Genres* chapter 7. Crime is fictional moral philosophy—stories about restoring fairness and justice when fundamental human law is violated, exploring the difference between what is legal and what is moral.

## Critical: File Output is MANDATORY

**This skill MUST save analysis to a timestamped file.** Conversational output alone is an incomplete task.

Writers need persistent artifacts they can:
- Reference throughout the drafting process
- Update as the story evolves
- Share with collaborators
- Compare with future iterations

**Success = A dated file exists (e.g., `2025-12-16-story-name-crime-structure.md`)**
**Failure = Only conversational output with no saved file**

## Purpose

Crime is fictional moral philosophy. The Crime story is about people who break the law and those who catch them, based on the starting principle that everyone in society has equal rights as human beings. Crime stories help writers explore the arts of morality and justice, distinguish between legality and morality (what the law allows vs what is good and right), create moral accounting systems (what one owes vs what one is owed), develop opponents who are master criminals with brilliant plans, build cat-and-mouse conflict where both sides are equally matched, sequence moral decisions that build in complexity, achieve poetic justice through karmic reckoning, and transcend into Epic Crime Tragedy or Crime Black Comedy.

## When to Invoke This Skill

Invoke this skill when writers are creating:
- Stories about criminals and law enforcement in moral conflict
- Narratives exploring the thin line between cop and criminal
- Master criminal characters who think they're above society
- Cat-and-mouse games between equally matched opponents
- Stories where legality and morality come into conflict
- Moral accounting over a lifetime (what you owe vs what you're owed)
- Complex moral codes and the consequences of breaking them
- Stories about poetic justice and karmic reckoning
- Epic Crime Tragedies or Crime Black Comedies
- Courtroom dramas, heist films, noir, gangster stories

**Note**: Crime structure layers on top of basic story structure. Writers should have the seven key steps or twenty-two steps established before adding Crime-specific elements. Use **story-structure-7-steps** or **story-structure-22-step** skills first if basic structure is undefined.

## The Crime Mind-Action Story View

Life is a constant attempt at moral accounting. In trying to reach one's desires in a society, each of us uses others and occasionally harms them. On the ledger between two individuals, each action is recorded, along with what is owed. In a social world, the moral accounting must always be balanced. An action must be paid for. If I use or transgress you, I must pay for it in kind. If I do not pay, there will be conflict.

**Key Point**: Crime is about the contest between a criminal who thinks he's above society and a defender of society's rules and values. The transcendent Crime story questions whether the illegal act is immoral, and whether true justice has been done.

**Central theme**: Being human is a daily effort to live fairly with others, but we are doomed to fail. When we fail, everyone pays. We must live within the law, even when the law limits our freedom. Being is a constant balance between the self and others, between what we want versus what we're allowed, between what is valuable versus what is just.

## Bundled Resources

**References:**
- `references/crime-beats.md` - Comprehensive explanation of all Crime story beats, moral argument beats, transcendent forms, examples (*The Dark Knight*, *Breaking Bad*, *In Bruges*, *Crime and Punishment*), and detailed guidance

**Assets:**
- `assets/crime-structure-template.md` - Comprehensive template for documenting crime structure
- `assets/moral-code-template.md` - Template for developing character moral codes
- `assets/moral-argument-template.md` - Template for tracking moral decisions and argument sequence
- `assets/opponent-plan-template.md` - Template for developing the opponent's intricate plan

## Task Instructions

When this skill is invoked, follow these steps to analyze or develop crime story structure.

### Step 1: Establish Output Location FIRST

**Before beginning analysis**, establish where the final document will be saved:

**Determine the environment:**
- With access to project directory and file system tools (Read, Write, Edit, Glob, Grep): Claude Code environment
- With uploaded files or chat without direct project access: Claude Desktop/Web environment

**In Claude Code:**
1. Get current date: `date +%Y-%m-%d`
2. Ask where to save structure analyses (suggest `structure/` or `process/structure/`)
3. Make note of the filename format: `YYYY-MM-DD-[story-name]-crime-structure.md`

**In Claude Desktop/Web:**
1. Note that output will be provided as formatted markdown artifact
2. Remind user to save with timestamped filename: `YYYY-MM-DD-[story-name]-crime-structure.md`

This ensures the file creation is not forgotten and sets the proper context.

### Step 2: Understand Story Context

**Understand the story context:**
1. Ask which story to analyze or develop
2. In Claude Code: If not specified, search for story files in the project (narrative drafts, outlines, structure documents, character notes)
3. In Claude Desktop: Ask to describe the story or share existing materials
4. Understand whether this is:
   - A new crime story idea needing full structure
   - An existing draft with moral argument or plot problems
   - A story in development needing crime-specific layer added
   - A genre diagnosis (determining if Crime is the right genre)

**Genre check**: Confirm this is actually a Crime story. Crime characteristics:
- Someone breaks the law (crime as inciting event or ongoing action)
- A cop or criminal serves as hero
- Focus on the contest between criminal and law enforcer
- Moral accounting and justice are central themes
- Less emphasis on detection/investigation, more on contest and moral conflict
- Question of whether illegal act is immoral

### Step 3: Assess Basic Structure Foundation

Before building Crime-specific elements, determine what structural foundation exists:

**Seven-step or twenty-two-step check**: Has the writer established:
- Weakness and need
- Desire
- Opponent
- Plan
- Battle
- Self-revelation
- New equilibrium

**If basic structure is undefined**: **STRONGLY RECOMMEND** using the **story-structure-7-steps** or **story-structure-22-step** skill FIRST to establish the foundation, then return to layer on Crime-specific elements.

**If basic structure exists**: Proceed to add Crime beats and moral argument elements.

**Important**: Crime beats don't replace basic structure—they enhance it with genre-specific moral requirements.

**Reference**: See `references/crime-beats.md` for how Crime beats relate to general story structure.

### Step 4: Determine Crime Variation

Crime stories come in different forms with distinct approaches. Work with the writer to determine which variations fit their story:

#### A. Hero Type

**Cop as Hero (Enforcer)**
Characteristics:
- Hero is law enforcement, detective, investigator, or defender of society
- Desire: catch a criminal
- Master cop—regular person but especially good at the job
- Lives at deeper level than others in society
- Moral code: the law is holy and must be enforced
- Examples: *The Dark Knight* (Batman), *Fargo* (Marge Gunderson), *The French Connection*, *Training Day*

**Criminal as Hero (Outlaw)**
Characteristics:
- Hero is the criminal breaking the law
- Desire: commit crime, gain wealth/power, win the game, escape capture
- Make criminal at least partially justified in breaking law
- Feels superior individual should live by own rules
- May have twisted but logical moral code
- Examples: *The Usual Suspects* (Verbal), *Breaking Bad* (Walter White), *The Thomas Crown Affair*, *Ocean's Eleven*

**Key Point**: The fact that hero can be either cop or outlaw means we're exploring the mirror image of the person on either side of the law.

#### B. Story Form

**Standard Crime Story**
- Linear plot: crime → investigation/pursuit → battle → justice
- Opponent is master criminal
- Emphasis on cat-and-mouse conflict
- Cop crosses moral line to catch criminal
- Ends with violent battle or clever reveal
- Examples: *Heat*, *Lethal Weapon*, *The Departed*

**Epic Crime Tragedy**
- Master criminal hero with extraordinary intelligence and potential
- Commits crime to prove superiority or escape oppression
- Detailed moral accounting over a lifetime
- What one owes vs what one is owed, life-or-death stakes
- Tragedy of lost potential, what might have been
- May use moral system rigid and resistant to change
- Examples: *Crime and Punishment*, *The Dark Knight*, *The Wire*, *Touch of Evil*, *Three Billboards Outside Ebbing, Missouri*

**Crime Black Comedy**
- Moral code becomes destructive system
- Extreme passion + lack of knowledge = deadly world
- Downward cycle where even love kills
- Playing out of karma on vast scale through comedy of errors
- Often involves moral accounting gone absurdly wrong
- Examples: *Breaking Bad*, *Fargo*, *In Bruges*, *No Country for Old Men*, *Blood Simple*, *Parasite*

Ask the writer which variations best fit their story vision. This will determine which beats to emphasize.

**Reference**: See `references/crime-beats.md` for detailed explanation of each variation.

### Step 5: Define the Moral Universe and Story World

#### Step 5.1: Story World - Slavery of Superficial Society

Crime stories focus on how people live together in society. Specifically, how do people get what they want when others say they cannot or should not want it?

**The Crime story world can take one of two extremes** (both dystopias):
1. **World of no crime**: All desires and actions are permitted. Result: chaotic state of nature with total power taken by those with money and guns.
2. **Fascist police state**: Almost everything a person does to realize desire is a crime.

Modern culture tries to walk the line between these extremes to produce the best overall society.

**Questions:**
- Where is your story world on this spectrum?
- Is this a world where people live on surface reality or "lives of quiet desperation"?
- Is there extreme wealth and poverty?
- Has possibility of moving up social ladder through hard work almost disappeared?
- What drives people to turn to crime?

#### Step 5.2: The Moral Universe

**Key Point**: In our social world, individual action always occurs in a moral universe to the extent that all actions have consequences for others. A moral universe doesn't mean people act morally. It means all actions between people have moral consequences.

**Questions about responsibility:**
- How does your story world define responsibility?
- Who is considered responsible for their actions?
- What excuses or exceptions exist?
- Is there a view of fate/destiny vs. personal responsibility?

**Questions about choice:**
- What choices are available to characters?
- What constraints limit choice (social, legal, economic)?
- When do characters become conscious of their choices?
- What is the opportunity cost of choices?

**Key Point**: Without choice, there is no responsibility and no morality, and vice versa. Once we are willing to take responsibility, we have choice.

### Step 6: Work Through Crime Story Beats

Work through each Crime beat systematically. Consult `references/crime-beats.md` for detailed explanation of each beat.

#### Crime Beat 1: Inciting Event - Crime

The criminal commits a crime that catapults them to a new level of wealth or power.

**Technique: Ingenious Crime**
Because the story often tracks the master criminal, whether hero or opponent, make the crime ingenious. The crime is the expression in action of the brilliance of the criminal's mind and artistry.

**Questions:**
- What crime occurs as the inciting event?
- How is it ingenious or artful?
- What does the crime reveal about the criminal's intelligence?
- What level of wealth or power does it provide?
- How does it set the story in motion?

**Key Point**: The more deception the criminal uses, the better the Crime story will be.

#### Crime Beat 2: Hero Strengths and Weakness-Need

**If hero is cop:**
- What makes them regular but especially good at their job (master cop)?
- What strong weakness-need do they have (may be poor, average, lonely)?
- How do they not fit in with society?
- How do they live according to best values of society with stronger faith than anyone else?

**If hero is criminal:**
- What makes them brilliant and/or master at beating system?
- Why do they feel superior enough to live by own rules?
- What justification (if any) exists for breaking law?
- What is their psychological weakness despite brilliance?

**Thematic implication**: The truly great individual is not the person with most power, money, or status, but the person who does great work within the rules, who wins the game not by cheating but by playing straight.

#### Crime Beat 3: Values and Moral Code

In every genre the hero begins believing in a set of values that will be challenged over the course of the story.

**Cop's Moral Code:**
- The law is holy and must be enforced at all costs
- Brotherhood among police force (code of silence—won't turn in fellow cop even if breaks law)

**Criminal's Moral Code:**
- Honor among thieves (or lack thereof—more likely no honor)
- Code of silence (in organized crime like mafia's omertà—success of organization over individual)

**Questions:**
- What is the hero's moral code at the beginning?
- What specific values guide their actions?
- What rules will they not break?
- How does this code differ from opponent's code?
- Will this code be tested and evolve?

**Technique: Write Out Detailed Moral Code**
Create a written moral code for your hero. Include specific rules, values, and guidelines for action in the three pivotal moments:
1. Values present from the beginning
2. Right and wrong actions during the Drive (middle)
3. Final moral decision at the end

**Use template**: Offer to create moral code document using `assets/moral-code-template.md`.

#### Crime Beat 4: Desire

**With cop hero**: Desire is to catch a criminal. Different from Detective form (find truth). Crime genre blends Detective and Action: cop figures out fairly easily who did it, then emphasis shifts to battle of wits as cop tries to catch criminal.

**With criminal hero**: Desire is money, power, or to win the game and prove superiority.

**Questions:**
- What is the hero's specific desire in this story?
- Is it focused enough to provide spine for plot?
- How does it start at low enough level to build?
- How will the stakes escalate?

**Technique: Criminal Hero Partially Justified**
Make the criminal at least partially justified in breaking the law to get what they want. Benefits:
1. Criminal hero becomes more complex and appealing
2. Cop is torn between desire to catch criminal and desire for criminal to succeed

#### Crime Beat 5: Opponent/Mystery - Super Criminal

**The opponent can be criminal or cop** (mirror image on either side of law).

**Whether hero or opponent, the criminal is usually**:
- Brilliant and/or master at beating the system
- Feels superior enough to live by own rules
- Can play game of life deeper or faster than others
- Goal: money, power, or win the game and prove superiority

**Questions:**
- Who is the main opponent?
- What goal do they want? (MUST be the SAME goal as hero)
- What makes them a master criminal or master cop?
- How are they brilliant at their craft?
- What is hidden about the opponent?
- How are hero and opponent mirror images?

**Technique: Iceberg Opponent**
- Is there a hierarchy of opponents with alliances?
- How is the hierarchy hidden from hero and audience?
- How will information be revealed in pieces at increasing pace?

**Mystery (if applicable)**:
- If opponent is hidden early in story, what mystery compensates?
- How does mystery replace ongoing hero-opponent conflict until reveal?

#### Crime Beat 6: Drive - Cat and Mouse

The middle of the Crime story is a series of conflicts where cop and criminal match wits and force. This is the cat and mouse struggle, one-on-one, master cop versus master criminal.

**Key Point**: In the top Crime stories, both cop and criminal are the best at their respective jobs, and both are equal in ability. This is essential to creating a heavyweight fight between the combatants.

**Questions:**
- How do cop and criminal match wits in the middle?
- What attacks and counterattacks occur?
- How are they equally matched?
- How does intensity build through the Drive?
- What mini-battles occur before final confrontation?

**Technique: Obsessive Cop**
During the Drive, show the cop becoming obsessed and going too far to catch the criminal, thus acting like the criminal. This technique blends two characters the audience thinks are opposites. Instead of good cop vs bad criminal, we see they are in many ways similar.

**Questions:**
- How does the cop cross moral lines?
- What immoral actions does cop take?
- How does this make cop similar to criminal?
- How does this explore thin line between inside and outside law?

#### Crime Beat 7: Opponent's Plan and Main Counterattack

**This beat is crucial and often missing.**

**Key Point**: The more intricate the opponent's plan, and the better it's hidden, the better the plot will be.

**Questions:**
- What is the opponent's strategy to get the goal?
- What hidden attacks has the opponent devised?
- How will these attacks be sprung on the hero (each is a revelation)?
- What is the main counterattack?
- How does opponent's plan drive the middle of the story?

**Technique: Deceptive Attack**
Make both cop and criminal masters of the game by using deception where each surprises the other and the audience. This includes where and how an attack will be made. It is especially important that each character hides their overall campaign of attack.

**Use template**: Offer to create opponent's plan document using `assets/opponent-plan-template.md`.

#### Crime Beat 8: Revelation - Criminal Uncovered

The crime reveal is usually about the trickery the criminal uses to escape the cop. Think of the criminal as an artist of crime.

**Questions:**
- What hidden attacks cause the most trouble for hero?
- What deceptions has the criminal constructed?
- How is information revealed in pieces?
- What explosive revelations pop the story?
- Do revelations build in intensity?

**Technique: Plan Reveals at Beginning**
Plan your reveals at the beginning of the story. Make each part of the opponent's overall, interconnected campaign of attack against the hero.

#### Crime Beat 9: Drive - Moral Argument

Crime emphasizes the moral argument, which focuses on the immoral and illegal actions the hero takes to win. To prevent theme from being heavy-handed, express moral argument through plot.

**Plot carries moral argument**:
1. Hero commits an illegal act
2. To hide responsibility and avoid punishment, commits another illegal act
3. Police or criminals respond, putting hero into tighter moral bind
4. Hero makes another mistake
5. And so on...

**Questions:**
- What illegal/immoral actions does hero take?
- How does each action lead to worse situation?
- How does hero justify actions?
- What is the moral accounting (what hero owes vs is owed)?
- How does the ledger become increasingly unbalanced?

#### Crime Beat 10: Apparent Defeat - The Criminal Escapes

The apparent defeat occurs when the criminal escapes or wins a major victory. The hero believes they've lost the fight.

**Questions:**
- What happens that makes hero believe they've lost?
- How does criminal escape or win major victory?
- What is hero's emotional state at lowest point?
- How explosive and devastating is this defeat?

#### Crime Beat 11: Gate-Gauntlet-Visit to Death - Chase

The Crime version of this beat is often a big chase. Crime borrows from Action: the chase is cat and mouse at top speed.

**Gate/Gauntlet:**
- How does conflict intensify to unbearable pressure?
- How does space constrict?
- How do hero's options narrow?

**Visit to Death:**
- How does hero have sudden realization of mortality?
- How does this spur them to fight rather than flee?

**Chase:**
- What is the big chase sequence?
- How does it build to battle?
- How does it function as cat and mouse at top speed?

#### Crime Beat 12: Violent Battle or Big Revelation

Since Crime story desire is to catch a criminal, the battle is the final violent confrontation between criminal and cop. Usually in pitched gunfight deep in bowels of city (though avoid cliché of creepy warehouse).

**This beat is the final legal accounting in the story, almost always enforced with a gun.**

**In transcendent Crime stories, this beat may be a big reveal** (moves Crime closer to Detective). The crime reveal is usually based on the trickery the criminal uses to escape the cop. The closer you push the big reveal to the end, the better.

**Questions:**
- What is the final confrontation?
- Is it violent battle or big reveal (or both)?
- Where does it occur?
- How is it the final legal accounting?
- What values are fighting (not just who is stronger)?
- Who wins the goal?

**Technique: Final Reveal**
If using a big reveal, ensure:
- It's planned from the beginning
- It's part of opponent's interconnected campaign
- It recontextualizes everything that came before
- It occurs as close to the end as possible

#### Crime Beat 13: Self-Revelation - Society Reaffirmed

**Normal self-revelation**: Cop reaffirms the values of living in society and within the law, even if citizens are relatively shallow and don't appreciate them.

**Negative version**: Society loses. Criminal defeats law. Artist in game of life beats system (but may be Pyrrhic victory—alone, having spurned love or community).

**Mixed version**: Hero lets someone else die as hero so people have hope in justice. True hero takes role of scapegoat. Society reaffirmed through lying.

**Questions:**
- What does hero learn about themselves?
- How do they see themselves honestly for first time?
- Do they reaffirm society or reject it?
- Is revelation positive, negative, or mixed?
- How is revelation shown through action, not statement?

#### Crime Beat 14: Moral Argument Conclusion - Poetic Justice

**Basic moral accounting**: The criminal is punished and the law is upheld. But while justice system enforces legal accounting, it doesn't necessarily produce justice. Laws are only rough estimate of moral accounting.

**Key Point**: "An eye for an eye" is not just about finding punishment to fit crime. It is the symbol of deeper desire to close the wound and equal the books. Only then can victim feel that justice has been done.

**Poetic Justice**: Payment in kind, payment unique to that crime, karmic reckoning, or payment by offender's own hand. Crime stories give outcome rarely found in life.

**Questions:**
- How is justice served (or not served)?
- Is there poetic justice (payment appropriate to crime)?
- Does offender bring about own downfall?
- Are the moral books balanced?
- What is the karmic reckoning?

### Step 7: Work Through Morality Story Beats (For Transcendent Crime)

For writers creating transcendent Crime (Epic Crime Tragedy or Crime Black Comedy), work through the eight morality story beats. These provide the advanced moral argument that elevates Crime to its highest form.

**Key Point**: The most important technique for creating finest transcendent Crime stories is to set up a moral universe that constantly tests the moral fiber of every character in the story.

#### Morality Beat 1: Story World - The Moral Universe

**Covered in Step 5.2 above.** Ensure moral universe is defined with:
- Clear view of responsibility (who is responsible for what)
- Clear view of choice (what choices exist, what constraints)
- Moral consequences for all actions

#### Morality Beat 2: Character Web - Moral Code

**Covered in Crime Beat 3 above.** Ensure detailed moral code is written for hero (and ideally for opponent and major allies).

**Key Point**: The crucial question in any moral code is how much of your values are about helping yourself versus how much you care how your actions will affect others.

**Technique: Executing the Moral Code**
Embed the moral code over the course of the plot in three main places:
1. Values of the hero present from the beginning
2. In the middle, hero takes right and wrong actions while trying to get goal
3. Hero's final moral decision determines whether moved to higher moral level

#### Morality Beat 3: Opposition - The Good vs. the Right

**The internal opposition in any moral code and moral argument is: ends = the good vs. means = the right**

- **The good** (ends): What the individual perceives as valuable. Improves their state of being.
- **The right** (means): Relational. Balance between two or more entities in social whole. Wrong action harms someone else.

**Questions:**
- What does hero perceive as good (valuable to them)?
- What is right action (doesn't harm others)?
- How do good and right come into opposition?
- When must hero choose between what's good for them vs right for others?

**Key Point**: The right depends on the good. Before we can decide what is right vs wrong action, we must first make an assessment of value.

#### Morality Beat 4: Plan - Values and Right and Wrong Action

A moral code is a game plan for how to act in various situations when seeking a goal. Relative moral codes allow for different situations, circumstances, and exceptions.

**The plan in moral code is concerned with two major activities:**
1. Assessing what makes a goal valuable (ends)
2. Assessing right and wrong actions used to reach goal (means)

**Key Point**: A moral code is a game plan for how to win only desirable goals using only proper actions.

**Questions:**
- What is hero's plan for achieving desire?
- How does plan align with or violate moral code?
- What actions does hero deem acceptable?
- What actions does hero rule out?
- How will plan be tested?

#### Morality Beat 5: Drive - Assessing Ends vs. Means

Because opponent is initially too strong, hero becomes desperate and begins to take immoral actions to get the goal.

**Key Point**: When values and action, the good and the right, come into opposition, the central question of the moral argument is: Should the individual put the right above the good, others above the self?

**Questions:**
- What immoral actions does hero take during Drive?
- How does hero justify each immoral action?
- How does hero assess ends vs means?
- Does hero question their own means or rationalize?
- How does moral pressure build?

**Freedom vs. Justice: The False Distinction**
On simple level, freedom and justice conflict (if you regulate my actions for the group, I can't do anything I want). But:

**Key Point**: Justice is basically optimizing freedom for everyone.

**The Story Code tracks a human being chasing value ("the good") and using questionable means ("the right") to get it.**

#### Morality Beat 6: Attack by Ally - Shame and Guilt

During middle of story, hero's ally attacks them by saying they share hero's goal but believe hero's actions to get goal are immoral and must stop. Ally gives reasons why hero's actions are wrong and will cause harm. But hero does not listen and instead tries to justify each act.

**This is both moral attack from without and attack from within in form of shame and guilt.**

**Key Point**: When individual attacks themselves through shame and guilt, it is never enough no matter how hard they try.

**Questions:**
- Which ally confronts hero about immoral actions?
- What criticism does ally offer?
- How does hero justify actions?
- Does hero feel shame or guilt?
- How does hero's mind punish itself?

#### Morality Beat 7: Battle, Moral Self-Revelation, and Moral Decision

**The battle** is the vortex point of plot and makes plot speed up. The hero's **final moral decision** is vortex point of theme and clarifies which way of life is best.

**Moral Self-Revelation:**
If negative, individual realizes: "I have wronged them. I can't do whatever I want. I must make amends to balance the moral accounts."

**Questions:**
- What does hero learn about effect of their actions on others?
- How do they see themselves honestly for first time?
- What do they realize about how they've hurt others?

**Moral Decision:**
No matter how complex the conflict of values, funnel it down to a single decision at the end. All possible ways of living come down to choice between two.

**Key Point**: A moral decision must have two elements to be moral: (1) it must affect others, and (2) it must involve personal sacrifice by the individual, no matter which choice they make.

**Questions:**
- What two courses of action does hero choose between?
- What values does each represent?
- What way of living does each stand for?
- How does choice affect others?
- What does hero choose?
- How does this prove what they learned in self-revelation?

**Technique: Final Decision**
Funnel all complexity down to single decision between two clear choices at the end.

#### Morality Beat 8: Thematic Revelation

A thematic revelation is where the moral code rises to another level of understanding. No longer limited to self-revelation of one individual, the moral code grows and becomes guideline for all people in how to live morally.

**Key Point**: In stories with thematic revelation, the balancing of accounts may involve poetic justice, which is payment appropriate to that crime.

**Questions:**
- What does audience learn about how people in general should act?
- How is this drawn from specific of characters to general?
- What particular gesture or action has symbolic impact?
- Is there poetic justice in the resolution?

**Use template**: Offer to create moral argument sequence document using `assets/moral-argument-template.md`.

### Step 8: Track Revelations and Moral Decisions Sequence

#### Step 8.1: Revelations Sequence

Separate the reveals from the rest of the plot and examine them as one unit.

**Create revelations list**: Extract all major revelations (target: 7-10 for average story; more for complex crime/thriller).

**Assess the sequence:**
1. **Logical order**: Do they occur in order hero would most likely learn them?
2. **Build in intensity**: Does each reveal get stronger (general buildup)?
3. **Increasing pace**: Do reveals get closer together as story progresses?

**Quality check:**
- How many reveals are about the opponent? (These are the best kind)
- Are any revelations not explosive enough?
- Do any breaks in buildup cause plot to stall?
- Is there reversal reveal where audience's understanding changes in instant?

#### Step 8.2: Moral Decisions Sequence

For transcendent Crime, track the sequence of moral decisions the hero makes.

**Create moral decisions list**: Extract all major moral decisions in order.

**Assess the sequence:**
1. **Build in difficulty**: Do moral choices become progressively harder?
2. **Build in stakes**: Do consequences of choices increase?
3. **Show character change**: Do choices show hero's moral decline or growth?

**Questions:**
- How many moral decisions does hero face?
- Do they get progressively worse (Crime Black Comedy) or better (redemption)?
- How far can you push hero toward darkness without losing audience?
- Does final moral decision integrate everything learned?

### Step 9: Assess Organic Connections

Verify that Crime elements connect organically with basic structure:

**Connection tests:**
- **Story World ↔ Weakness**: Does superficial society express and exacerbate hero's weakness?
- **Crime ↔ Desire**: Does crime set hero's desire in motion?
- **Desire ↔ Opponent**: Are they competing for SAME goal?
- **Opponent ↔ Weakness**: Is opponent the necessary opponent (best able to attack hero's great weakness)?
- **Moral Code ↔ Actions**: Do hero's actions test and challenge their stated moral code?
- **Cat and Mouse ↔ Equal Ability**: Are hero and opponent equally matched in ability?
- **Revelations ↔ Opponent's Plan**: Do revelations show pieces of opponent's intricate plan?
- **Moral Decisions ↔ Theme**: Do moral decisions express theme through structure?
- **Self-Revelation ↔ Society**: Does hero reaffirm society, reject it, or find mixed answer?
- **Conclusion ↔ Poetic Justice**: Is there appropriate karmic reckoning?

**Identify weak connections** and suggest how to strengthen them.

### Step 10: Provide Structural Analysis and Recommendations

Based on the analysis:

**For new crime stories:**
- Is moral universe defined?
- Are hero and opponent equally matched?
- Is opponent's plan intricate and hidden?
- Is hero's moral code detailed?
- Are Crime beats present and connected?
- Does cat-and-mouse conflict build?
- Is this cop hero or criminal hero?
- Is this standard Crime, Epic Tragedy, or Black Comedy?
- For transcendent: are morality beats tracked?

**For existing drafts:**
- Which Crime beats are present and working well?
- Which beats are missing or underdeveloped?
- Is opponent's plan detailed enough (most common weakness)?
- Does cat-and-mouse conflict maintain intensity?
- Are revelations building or stalling?
- Are moral decisions tracked and building?
- What revisions would strengthen crime structure?
- Is moral argument expressed through plot (not heavy-handed)?

**For genre diagnosis:**
- Is this truly Crime or another genre (Detective, Thriller, Action)?
- Which Crime variation does it fit?
- What would make Crime elements stronger?
- Should this be transcendent or standard Crime?

### Step 11: Save Structure Documentation (REQUIRED)

**MANDATORY: Do not consider the task complete until file is saved.**

**If in Claude Code (project directory access):**
1. Create the chosen directory if it doesn't exist using Bash (e.g., `mkdir -p structure`)
2. Use Write tool to save file with the filename established in Step 1: `YYYY-MM-DD-[story-name]-crime-structure.md`
3. Use the structure format from `assets/crime-structure-template.md`
4. Include complete analysis from Steps 5-10
5. Offer to create supplementary documents:
   - Moral code detail: `YYYY-MM-DD-[story-name]-moral-code.md` using `assets/moral-code-template.md`
   - Opponent's plan detail: `YYYY-MM-DD-[story-name]-opponent-plan.md` using `assets/opponent-plan-template.md`
   - Moral argument sequence: `YYYY-MM-DD-[story-name]-moral-argument.md` using `assets/moral-argument-template.md`
6. Confirm save location to user with full file path

**Validation Checklist - Before Completing:**
- [ ] Date obtained via Bash in Step 1
- [ ] Save location confirmed with user in Step 1
- [ ] Analysis completed in Steps 2-10
- [ ] File written using Write tool
- [ ] File path confirmed to user
- [ ] Supplementary documents offered

**If in Claude Desktop/Web (no project directory):**
1. Create the analysis as a formatted markdown artifact
2. Present it in the chat for review
3. Remind user to save with timestamped filename: `YYYY-MM-DD-[story-name]-crime-structure.md`
4. Use the structure format from `assets/crime-structure-template.md`
5. Offer to create supplementary documents separately
6. Offer to explore any specific Crime element in more depth if requested

**If any Claude Code checklist item is unchecked, the task is incomplete.**

## Important Reminders

- **Moral argument is paramount**: Crime is fictional moral philosophy. Advanced moral argument is what makes Crime transcendent.
- **Layer on basic structure**: Crime beats enhance seven steps or twenty-two steps, they don't replace them.
- **Opponent's plan crucial**: Most writers miss this. The more intricate the opponent's plan and the better it's hidden, the better the plot.
- **Cop and criminal as mirror images**: Hero can be either, and they should be similar in key ways.
- **Equal ability essential**: Both cop and criminal must be best at their jobs and equal in ability for heavyweight fight.
- **Deception improves plot**: The more deception criminal uses, the better the Crime story.
- **Same goal required**: Opponent must want SAME goal as hero (not just oppose hero).
- **Moral code must be detailed**: Write out specific rules and values for hero (and ideally opponent).
- **Cop crosses line**: Standard technique—cop goes too far and acts like criminal. So common it's expected; overcome through deception.
- **Plan reveals early**: Plan reveals at beginning of story. Make each part of opponent's interconnected campaign.
- **Poetic justice**: Payment in kind, unique to that crime, karmic reckoning, by offender's own hand.
- **Show moral argument through plot**: Don't be heavy-handed. Hero takes illegal action, then another to cover it up, leading to moral bind.
- **Moral decisions build**: In transcendent Crime, sequence moral decisions so they build in difficulty.
- **Character is destiny**: "Character is destiny" (Heraclitus) means we are responsible for results of our life and moral effects on others.
- **Freedom = Justice**: Justice is basically optimizing freedom for everyone.
- **The good vs the right**: Internal opposition in moral code—ends (the good) vs means (the right).
- **Attack by ally**: During middle, ally criticizes hero's immoral actions; hero justifies.
- **Final moral decision**: Funnel all complexity to single decision between two choices at end.

**Reference**: See `references/crime-beats.md` for all detailed principles, examples, and techniques.

## What This Skill Does NOT Do

- Replace the writer's creative vision or moral instincts
- Guarantee a "good" Crime story (execution still matters)
- Work for Detective stories (different genre with different focus)
- Work for Thriller stories (different genre with different focus)
- Provide scene-by-scene dialogue or prose (it establishes structural foundation)
- Eliminate the need for other story elements (character depth, world-building, theme, symbol)
- Work as a mechanical formula (must be adapted to unique story)
- Replace basic story structure (must be layered on top of seven steps or twenty-two steps)

## Integration with Other Skills

This skill works alongside:
- **story-structure-7-steps** - Establishes basic foundation; Crime builds on it
- **story-structure-22-step** - For complex Crime stories, use 22 steps first
- **symbol-web** - Deepens symbolic elements in Crime's moral argument
- **narrative-inventory** - Catalogues what exists; Crime skill shows if genre elements are present
- **narrative-keywords** - Identifies themes of justice, morality, responsibility
- **narrative-maps** - Shows spatial structure; Crime skill shows moral structure
- Character development tools
- Scene planning tools
- Genre-specific tools (Detective, Thriller, Gangster)

---

*Based on John Truby's "Crime: Morality and Justice" from The Anatomy of Genres: How Story Forms Explain the Way the World Works*
