---
name: lexical-recall-guard
description: PROACTIVELY detect when user requests require high lexical recall precision (exact quotes, specific chapter titles, verbatim text, exhaustive lists) and warn that LLM limitations may cause hallucinations. Check if source material is available in context before warning. Provide alternative mitigation strategies (WebSearch, requesting sources, reading files).
---

# Lexical Recall Guard

## Purpose

This skill addresses a fundamental limitation of LLMs: the tendency to hallucinate when tasks depend heavily on precise lexical recall rather than semantic understanding. LLMs excel at semantic reasoning but struggle with verbatim recall because they reconstruct plausible text from patterns rather than retrieving exact information from a database.

**Core function:** Proactively detect user requests that require high lexical precision and either warn about hallucination risk or provide mitigation strategies before responding.

## When to Invoke This Skill

**AUTOMATICALLY and PROACTIVELY invoke when detecting these patterns:**

### High-Risk Lexical Recall Indicators

**Exact/verbatim content requests:**
- "exact quote from..."
- "verbatim text of..."
- "word-for-word..."
- "quote exactly..."
- "what does [source] say exactly..."
- "the precise wording of..."

**Structural/organizational requests:**
- "list all chapter titles in..."
- "what chapters are in..."
- "table of contents for..."
- "section headings in..."
- "all episodes of [series]..."

**Exhaustive enumeration:**
- "list all 50..."
- "name every..."
- "all [items] in [category]..."
- "complete list of..."
- "enumerate all..."

**Specific attributions:**
- "what does [author] say in chapter [X]..."
- "the opening lines of [work]..."
- "the lyrics to [song]..."
- "[Person]'s exact words about..."

### DO NOT Trigger (Semantic/Conceptual Questions)

**General understanding:**
- "what themes appear in..."
- "explain the main argument..."
- "summarize..."
- "what is the significance of..."

**Reasoning and analysis:**
- "why did [person] do..."
- "how does [concept] work..."
- "compare [X] and [Y]..."
- "what are the implications of..."

**Approximations accepted:**
- "around how many..."
- "roughly what does..."
- "generally speaking..."
- "the gist of..."

## Core Detection Process

### Step 1: Analyze the User Request

Parse the user message for lexical recall indicators:

1. **Keyword detection**: Check for trigger phrases from references/trigger-patterns.md
2. **Context clues**: Look for words like "exact," "verbatim," "specific," "all," "list every"
3. **Source specificity**: Requests about specific chapters, verses, lines, sections
4. **Enumeration language**: "List all," "name every," "complete list"

### Step 2: Check Source Availability

**CRITICAL: Before warning, verify whether source material is available in context.**

Source material IS available when:
- User has uploaded files containing the source
- User has pasted relevant text in the conversation
- Files have been read using the Read tool that contain the source
- Source is in project directory and accessible

Source material is NOT available when:
- Request references external works not in context
- No files uploaded or read
- Asking about general knowledge sources

**If source IS available:** Proceed with high confidence using lexical recall from the available material. No warning needed.

**If source is NOT available:** Proceed to warning and mitigation.

### Step 3: Provide Contextual Warning

When source is unavailable and lexical precision is required, provide a clear warning:

**Warning structure** (use template from assets/warning-template.md):

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for [exact quotes/chapter titles/verbatim text/etc.],
but I cannot reliably provide this without access to the source material.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact information.
This means I may generate plausible-sounding but incorrect details when precise lexical
accuracy is required.

**Risk:** [Specific risk for this request type]

**Recommended alternatives:**
[Provide 2-3 specific mitigation strategies from references/mitigation-strategies.md]
```

### Step 4: Offer Mitigation Strategies

Based on the request type, suggest appropriate alternatives from references/mitigation-strategies.md:

**For quote/text requests:**
- Use WebSearch to find the actual source
- Ask user to provide/upload the source document
- Offer to analyze if user shares the text

**For structural info (chapters, sections):**
- WebSearch for table of contents
- Ask user to share the document
- Provide general structural knowledge with uncertainty caveat

**For exhaustive lists:**
- WebSearch for authoritative lists
- Provide partial list with explicit uncertainty
- Suggest verification from primary sources

**For attributions:**
- WebSearch for verified quotes
- Offer paraphrased meaning with uncertainty
- Request source material from user

### Step 5: Proceed with Appropriate Confidence

**If warning was given:**
- Offer to proceed with best effort if user acknowledges limitations
- Clearly mark any provided information as uncertain
- Emphasize verification is needed

**If source was available:**
- Proceed with high confidence
- Use Read tool to access exact text
- Quote directly from available material

## Integration Patterns

### Pattern 1: Proactive Detection (Preferred)

Like env-manager, trigger automatically without waiting for failure:

```
User: "What's the exact quote from chapter 5 of To Kill a Mockingbird?"

[Lexical-recall-guard triggers]
→ Analyze: "exact quote" + "chapter 5" = high lexical precision needed
→ Check context: No source file available
→ Warn: Cannot provide reliable exact quotes without source
→ Suggest: WebSearch, ask user to share relevant passage
```

### Pattern 2: Source-Available Bypass

```
User: "What's the exact quote from page 23?"
[User has uploaded the PDF]

[Lexical-recall-guard triggers]
→ Analyze: "exact quote" = high lexical precision needed
→ Check context: PDF available in context
→ Bypass warning: Proceed with Read tool to get exact text
→ Respond: [Exact quote from page 23]
```

### Pattern 3: Semantic Request Bypass

```
User: "What are the main themes in To Kill a Mockingbird?"

[Lexical-recall-guard evaluates]
→ Analyze: "main themes" = semantic understanding, not lexical precision
→ No trigger: This is within LLM capabilities
→ Proceed normally: Answer based on semantic knowledge
```

## Bundled Resources

### references/trigger-patterns.md
Comprehensive list of phrases and patterns indicating lexical recall requests, with examples of edge cases and context-dependent triggers.

### references/mitigation-strategies.md
Detailed alternative approaches organized by request type: quotes, structural info, lists, attributions, technical specs.

### assets/warning-template.md
Template for consistent, clear warning messages that explain the limitation, specific risk, and actionable alternatives.

## Key Principles

1. **Proactive over reactive**: Detect and warn BEFORE hallucinating
2. **Context-aware**: Don't warn if source material is available
3. **Actionable**: Always provide concrete mitigation strategies
4. **Honest**: Clearly explain the LLM limitation
5. **Helpful**: Still offer to proceed with appropriate caveats if user wants

## What This Skill Does NOT Do

- Block all responses about books, documents, or historical texts
- Prevent semantic discussion and analysis
- Replace WebSearch or file reading capabilities
- Guarantee 100% accuracy even when source is available (reading errors can occur)
- Apply to mathematical proofs or logical reasoning (different type of precision)

## Examples

### Example 1: Quote Request Without Source

**User:** "What's the exact opening line of Pride and Prejudice?"

**Skill triggers:**
- Detected: "exact opening line" = high lexical precision
- Source check: No text available
- Action: Warn + suggest WebSearch or acknowledge uncertainty
- Outcome: User gets honest assessment before potential hallucination

### Example 2: Quote Request With Source

**User:** "What's the exact quote on page 5?" [PDF uploaded]

**Skill triggers:**
- Detected: "exact quote" = high lexical precision
- Source check: PDF available in context
- Action: Use Read tool, extract exact text
- Outcome: Accurate quote provided without warning

### Example 3: Semantic Question (No Trigger)

**User:** "What are the major themes in Pride and Prejudice?"

**Skill evaluates:**
- Detected: "themes" = semantic understanding
- Assessment: Within LLM capabilities
- Action: No trigger, proceed normally
- Outcome: Thoughtful thematic analysis provided

### Example 4: Chapter Listing

**User:** "List all the chapter titles in On Writing Well"

**Skill triggers:**
- Detected: "list all chapter titles" = structural/enumeration request
- Source check: No book available
- Action: Warn + suggest WebSearch or partial list with uncertainty
- Outcome: User understands limitations, can choose to verify elsewhere

## Best Practices

1. **Trigger early**: Detect patterns in initial request before generating response
2. **Be specific**: Tailor warning to the exact type of lexical precision needed
3. **Offer solutions**: Never just warn—always provide actionable alternatives
4. **Check thoroughly**: Always verify source availability before warning
5. **Stay helpful**: Make it easy for user to get accurate information through alternatives
6. **Acknowledge uncertainty**: If proceeding despite limitations, mark information as uncertain

---

*This skill implements proactive hallucination prevention by detecting when user requests exceed LLM lexical recall capabilities and providing transparent warnings with actionable mitigation strategies.*
