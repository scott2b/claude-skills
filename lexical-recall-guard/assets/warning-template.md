# Lexical Recall Warning Template

This template provides consistent, clear warning messages when high lexical precision is required but source material is unavailable.

## Standard Warning Structure

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for [SPECIFIC_TYPE], but I cannot
reliably provide this without access to the source material.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact
information. This means I may generate plausible-sounding but incorrect
details when precise lexical accuracy is required.

**Risk:** [SPECIFIC_RISK]

**Recommended alternatives:**
[MITIGATION_OPTIONS]
```

## Template Variables

### [SPECIFIC_TYPE]

Choose based on request:
- "exact quotes"
- "verbatim text"
- "chapter titles"
- "complete lists"
- "specific attributions"
- "technical specifications"
- "word-for-word lyrics"
- "precise historical text"

### [SPECIFIC_RISK]

Tailor to request type:

**For quotes:**
"I may misquote, paraphrase incorrectly, or attribute words inaccurately."

**For chapter/structural info:**
"I may confuse titles, misnumber chapters, or list incorrect structure."

**For exhaustive lists:**
"I may omit items, include incorrect items, or provide incomplete enumeration."

**For attributions:**
"I may misattribute quotes, get wording wrong, or conflate different statements."

**For technical specs:**
"I may provide outdated, version-specific, or incorrect technical details."

### [MITIGATION_OPTIONS]

Provide 2-3 specific, actionable alternatives from mitigation-strategies.md

**Example format:**
```
1. **WebSearch**: I can search for authoritative sources to find the exact text
2. **Share source**: Upload or paste the relevant section for accurate extraction
3. **Proceed with caveat**: I can provide my best recollection marked as uncertain
```

## Full Examples

### Example 1: Quote Request

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for exact quotes, but I cannot reliably
provide this without access to the source material.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact
information. This means I may generate plausible-sounding but incorrect
details when precise lexical accuracy is required.

**Risk:** I may misquote, paraphrase incorrectly, or attribute words
inaccurately.

**Recommended alternatives:**
1. **WebSearch**: I can search for verified quotes from authoritative sources
2. **Share source**: Upload the document or paste the relevant passage for
   accurate quotation
3. **Proceed with caveat**: I can provide my best recollection with explicit
   uncertainty marking

How would you like to proceed?
```

### Example 2: Chapter Listing

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for chapter titles, but I cannot reliably
provide this without access to the source material.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact
information. This means I may generate plausible-sounding but incorrect
details when precise lexical accuracy is required.

**Risk:** I may confuse titles, misnumber chapters, or list incorrect structure.

**Recommended alternatives:**
1. **WebSearch**: I can search for the official table of contents from the
   publisher or reliable sources
2. **Share source**: Upload or photograph the table of contents for accurate
   extraction
3. **General structure**: I can describe the approximate structure with
   uncertainty caveats

How would you like to proceed?
```

### Example 3: Exhaustive List

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for a complete list, but I cannot reliably
provide this without access to authoritative sources.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact
information. This means I may generate plausible-sounding but incorrect
details when precise lexical accuracy is required.

**Risk:** I may omit items, include incorrect items, or provide incomplete
enumeration.

**Recommended alternatives:**
1. **WebSearch**: I can search for authoritative complete lists from official
   sources
2. **Partial list**: I can provide well-known examples while explicitly noting
   incompleteness
3. **Direct to source**: I can guide you to the authoritative source where
   the complete list exists

How would you like to proceed?
```

### Example 4: Technical Specification

```
⚠️ Lexical Recall Limitation Detected

Your request requires high precision for technical specifications, but I
cannot reliably provide this without access to official documentation.

**Why:** LLMs reconstruct text from patterns rather than retrieving exact
information. This means I may generate plausible-sounding but incorrect
details when precise lexical accuracy is required.

**Risk:** I may provide outdated, version-specific, or incorrect technical
details that could cause implementation errors.

**Recommended alternatives:**
1. **WebSearch**: I can search for the official documentation and current
   specifications
2. **Share docs**: Provide your specific version's documentation for accurate
   details
3. **General guidance**: I can provide general information with strong
   recommendation to verify against official docs

How would you like to proceed?
```

## Concise Warning (for repeated requests)

After the first full warning in a session, subsequent warnings can be more concise:

```
⚠️ Note: This requires high lexical precision that I cannot guarantee without
source access.

Options:
- WebSearch for authoritative source
- Share the source document
- Proceed with uncertainty caveats

Preferred approach?
```

## Warning with Immediate WebSearch Offer

For cases where WebSearch is clearly the best option:

```
⚠️ Lexical Recall Limitation Detected

This request for [SPECIFIC_TYPE] requires precision I cannot guarantee from
memory. I may generate plausible but incorrect details.

I recommend searching for authoritative sources to ensure accuracy. Would you
like me to perform a WebSearch for [specific information]?
```

## Warning When Source is Partially Available

When user has provided some context but not the specific part needed:

```
⚠️ Lexical Precision Note

You've shared [WHAT_THEY_PROVIDED], but this specific request about
[SPECIFIC_REQUEST] requires access to [SPECIFIC_SECTION_NEEDED].

Options:
1. Share [specific section] for accurate extraction
2. I can search the web for this information
3. I can provide my best knowledge with uncertainty caveats

How would you like to proceed?
```

## No Warning Needed (Source Available)

When source IS available in context, proceed directly without warning but note the source:

```
Based on [SOURCE_DESCRIPTION] you've provided, [ANSWER WITH EXACT INFORMATION].

[If quoting] The exact text reads: "[QUOTE]"
```

## Key Principles for Warnings

1. **Be specific**: Tailor warning to the exact type of precision needed
2. **Explain clearly**: User should understand WHY this is a limitation
3. **Provide alternatives**: Always offer 2-3 actionable options
4. **Stay helpful**: Frame as collaborative problem-solving, not blocking
5. **Be concise**: Clear but not overly verbose
6. **Empower choice**: Let user decide how to proceed

## When NOT to Use Warning

Skip warning when:
- Source material is available in context
- Request is semantic/conceptual, not lexical
- Approximation is explicitly acceptable
- Question is within general knowledge domain where precision is reliable
