# Lexical Recall Trigger Patterns

This reference provides comprehensive patterns for detecting when user requests require high lexical precision that may exceed LLM capabilities.

## Primary Trigger Categories

### 1. Exactness Indicators

**Direct exactness requests:**
- "exact quote"
- "exactly what"
- "verbatim"
- "word-for-word"
- "precise wording"
- "what exactly does [source] say"
- "the exact text"
- "quote exactly"
- "literal text"

**Precision modifiers:**
- "the specific phrase"
- "the actual words used"
- "what [source] literally says"
- "the original text"
- "as written in"
- "the authentic version"

### 2. Structural/Organizational Requests

**Chapter and section enumeration:**
- "list all chapters in"
- "what chapters are in"
- "table of contents for"
- "chapter titles of"
- "all sections of"
- "the structure of [book]"
- "how many chapters"
- "what chapter is titled"

**Episode/installment lists:**
- "all episodes of [series]"
- "list the episodes"
- "season X episode titles"
- "episode guide for"

**Document structure:**
- "section headings in"
- "all subsections of"
- "the outline of"
- "parts and chapters"

### 3. Exhaustive Enumeration

**Complete lists:**
- "list all"
- "name every"
- "all [items] in [category]"
- "complete list of"
- "enumerate all"
- "each of the"
- "every single"
- "the full set of"

**Specific counts:**
- "all 50 [items]"
- "the 7 [specific things]"
- "each of the 12"
- "all [number] [items]"

### 4. Specific Attribution Requests

**Quotes and statements:**
- "what does [author] say in chapter [X]"
- "what did [person] say about"
- "[Person]'s exact words"
- "how does [author] phrase"
- "what does [source] call this"

**Opening/closing lines:**
- "the opening line of"
- "how does [work] begin"
- "the first sentence of"
- "the last words of"
- "how does [work] end"

**Lyrics and poetry:**
- "the lyrics to"
- "words of [song]"
- "the text of [poem]"
- "verses of [hymn]"

### 5. Location-Specific Requests

**Page/chapter references:**
- "what's on page [X]"
- "page [X] says"
- "in chapter [X], what does"
- "the quote from page [X]"

**Verse/line references:**
- "verse [X] of [text]"
- "line [X] reads"
- "stanza [X] says"

## Context-Dependent Patterns

### High Risk When Combined

Multiple weak signals can create high risk:
- Request mentions specific source + wants quotation
- Request mentions specific location + wants exact wording
- Request wants enumeration + specific count

**Examples:**
- "What does chapter 5 of [book] say about [topic]?" (moderate risk)
- "Give me the exact quote from chapter 5 of [book] about [topic]" (high risk)

### Edge Cases Requiring Judgment

**May or may not trigger depending on context:**

1. **"What does X say about Y?"**
   - High risk if: User wants exact wording
   - Low risk if: Paraphrase/summary acceptable

2. **"List the main [items]"**
   - High risk if: "List ALL" or complete enumeration expected
   - Low risk if: Representative examples sufficient

3. **"The [chapter/section] about [topic]"**
   - High risk if: Asking for exact title
   - Low risk if: Asking which chapter covers topic

## Patterns That Should NOT Trigger

### Semantic Understanding Requests

**Thematic analysis:**
- "What themes appear in"
- "What is the meaning of"
- "How does [work] explore"
- "The significance of"

**Conceptual questions:**
- "Why did [author] write"
- "How does [concept] work"
- "What is the purpose of"
- "Explain the argument in"

**Comparative analysis:**
- "Compare [X] and [Y]"
- "How are [X] and [Y] similar"
- "Differences between"

**Summary requests:**
- "Summarize"
- "What happens in"
- "Give me an overview"
- "The gist of"
- "Broadly speaking"

### Approximation-Accepting Requests

**Quantitative approximations:**
- "around how many"
- "roughly"
- "approximately"
- "about how long"
- "estimate"

**General characterizations:**
- "generally"
- "typically"
- "usually"
- "often"
- "tends to"

## Detection Heuristics

### Confidence Scoring

**High confidence triggers (90%+ likelihood):**
- Contains "exact" or "verbatim" + quote request
- "List all [specific number]" enumeration
- "Opening/closing line of [work]"
- "What does page [X] say exactly"

**Medium confidence triggers (60-90% likelihood):**
- "What chapters are in [book]"
- "Quote from [specific location]"
- "[Author]'s words about [topic]"
- "All episodes of [series]"

**Low confidence triggers (30-60% likelihood):**
- "What does [source] say about [topic]" (depends on exactness expected)
- "The main [items] in [category]" (depends on completeness expected)
- "How does [author] describe [X]" (could be paraphrase or exact)

### Disambiguation Questions

When confidence is medium/low, consider asking:
- "Do you need the exact wording, or would a paraphrase work?"
- "Are you looking for a complete list, or examples?"
- "Should this be verbatim, or is the general idea sufficient?"

## Special Considerations

### Technical Specifications

**May require high precision BUT can be verified:**
- API documentation
- Technical specifications
- Code syntax
- Mathematical formulas

These still trigger warnings if source unavailable, but with different mitigation (WebSearch for official docs).

### Historical/Legal Texts

**Often require exactness:**
- Constitutional/legal text
- Historical documents
- Religious texts
- Treaties and agreements

Strong candidates for triggering unless source is available.

### Common Knowledge

**Low risk even with exactness language:**
- Very famous quotes that are universally known
- Common phrases or expressions
- Well-established facts

Use judgment: "E pluribus unum" vs. "the third sentence of the Federalist Papers #10"

## Pattern Matching Best Practices

1. **Look for combinations**: Single keywords are weak signals; combinations are strong
2. **Consider source accessibility**: Same request, different risk if source is/isn't available
3. **Understand user intent**: Sometimes "exact" means "accurate" not "verbatim"
4. **Err toward warning**: False positive (unnecessary warning) better than false negative (hallucination)
5. **Provide context**: Explain WHY the pattern triggered
6. **Remain helpful**: Always offer alternatives, not just warnings
