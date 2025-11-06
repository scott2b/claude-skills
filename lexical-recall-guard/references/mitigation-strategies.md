# Mitigation Strategies for Lexical Recall Requests

When lexical recall precision is required but source material is unavailable, these strategies provide actionable alternatives.

## Strategy Selection by Request Type

### 1. Quote/Exact Text Requests

**User wants:** Verbatim text from a source

**Mitigation options:**

**A. WebSearch for verified quotes**
- Use WebSearch to find authoritative sources
- Look for quote databases, scholarly sites, official publications
- Verify across multiple sources when possible
- Present with source attribution

**Example response:**
```
I'll search for the exact quote to ensure accuracy.
[Performs WebSearch]
According to [source], the exact quote is: "[quote]"
```

**B. Request source material from user**
- Ask user to upload/paste the relevant section
- Explain this enables accurate quotation
- Offer to analyze once provided

**Example response:**
```
To provide the exact quote accurately, could you share the relevant
passage or upload the document? I can then give you the precise wording.
```

**C. Provide with strong uncertainty caveat**
- Acknowledge inability to guarantee exactness
- Offer best recollection with explicit warning
- Recommend verification

**Example response:**
```
I cannot guarantee the exact wording without access to the source,
but to the best of my knowledge it's approximately: "[text]"

⚠️ Please verify this against the original source as I may have the
wording slightly wrong.
```

### 2. Structural Information (Chapters, Sections, TOC)

**User wants:** Chapter titles, section headings, table of contents

**Mitigation options:**

**A. WebSearch for table of contents**
- Search for official TOC from publisher or reliable source
- Look for "table of contents" + book title
- Check multiple sources for consistency

**Example response:**
```
I'll search for the official table of contents.
[Performs WebSearch on "[book title] table of contents"]
Based on [source], here are the chapter titles: [list]
```

**B. Ask user to share the document**
- Request they share front matter/TOC
- Can extract structure accurately once provided

**Example response:**
```
To give you the exact chapter structure, could you share a photo of
the table of contents or upload the document? That way I can provide
the precise titles.
```

**C. Provide general structure with uncertainty**
- Give rough structure from memory
- Mark as uncertain and approximate
- Recommend verification

**Example response:**
```
From what I recall, the book has approximately [X] chapters covering
topics like [general themes], but I cannot guarantee the exact titles
or count. I recommend checking the actual table of contents for
precision.
```

### 3. Exhaustive Lists/Enumerations

**User wants:** Complete list of all items in a category

**Mitigation options:**

**A. WebSearch for authoritative lists**
- Find official/canonical lists
- Verify source authority
- Present with source citation

**Example response:**
```
I'll search for an authoritative list.
[Performs WebSearch for official source]
According to [source], here is the complete list: [items]
```

**B. Provide partial list with explicit incompleteness**
- Give well-known examples
- Clearly state list is incomplete
- Suggest how to find complete list

**Example response:**
```
I can name several prominent examples: [items]

However, I cannot guarantee this is complete. For a comprehensive
list, I recommend:
- WebSearch for "[category] complete list"
- Consulting [specific authoritative source]
```

**C. Redirect to primary source**
- Identify where complete list exists
- Guide user to access it
- Explain why that's more reliable

**Example response:**
```
For a complete and accurate list, the best source would be [specific
resource]. I cannot reliably enumerate all items from memory without
risk of omission or error.
```

### 4. Specific Attributions

**User wants:** What a specific person said/wrote

**Mitigation options:**

**A. WebSearch for verified attribution**
- Search for the quote + attribution
- Verify from reliable sources
- Present with sourcing

**Example response:**
```
I'll search for verified quotes from [person] on this topic.
[Performs WebSearch]
According to [source], [person] said: "[quote]"
```

**B. Paraphrase with uncertainty + offer to verify**
- Give the general meaning/idea
- Mark as paraphrase not quote
- Offer to search for exact words

**Example response:**
```
I believe [person] expressed the idea that [paraphrase], but I cannot
provide the exact wording without verification. Would you like me to
search for the precise quote?
```

**C. Request context from user**
- Ask where they encountered this
- User may have the source
- Can then verify together

**Example response:**
```
Could you share where you encountered this quote? If you have access
to the source, I can help analyze the exact wording. Otherwise, I
risk misquoting.
```

### 5. Technical Specifications

**User wants:** API docs, technical specs, formulas

**Mitigation options:**

**A. WebSearch official documentation**
- Find official docs, API references
- Link to authoritative technical sources
- Quote from verified documentation

**Example response:**
```
I'll search for the official documentation.
[Performs WebSearch for official API docs]
According to the official documentation at [URL], the specification
is: [details]
```

**B. Request user share their version**
- Specs may vary by version
- Ask user to share their specific docs
- Can then reference accurately

**Example response:**
```
Technical specifications can vary by version. Could you share which
version you're using, or share the documentation you're working with?
This ensures I provide the exact correct details.
```

**C. Provide with verification recommendation**
- Give general knowledge of spec
- Strongly recommend verification
- Explain risks of inaccuracy

**Example response:**
```
Based on general knowledge, I believe the specification is [details],
but for technical implementation you should ALWAYS verify against the
official documentation to ensure exact correctness.
```

## General Mitigation Principles

### 1. WebSearch First for Public Information

For publicly available information (published books, famous quotes, historical documents):
- WebSearch is often the fastest, most accurate solution
- Look for authoritative sources
- Cross-reference when possible
- Always cite sources

### 2. Request Source for Private/Specific Information

For user-specific documents, unpublished work, or context-dependent material:
- Ask user to provide/upload
- Explain this enables precision
- Offer to help once material is available

### 3. Provide with Caveats When Proceeding

When user wants to proceed despite limitations:
- Give best effort response
- Mark clearly as uncertain/approximate
- Recommend verification steps
- Don't overstate confidence

### 4. Combine Strategies

Often most effective to use multiple approaches:
1. Offer to WebSearch
2. Also ask if they can share source
3. Provide preliminary answer with caveats
4. Let user choose approach

**Example combined response:**
```
I can help in a few ways:

1. Search the web for verified sources (most reliable)
2. You could share the document and I'll extract the exact text
3. I can provide my best recollection with the caveat that it may not
   be perfectly accurate

Which approach would you prefer?
```

## Response Templates

### Template A: WebSearch Offer
```
To ensure accuracy for this request, I recommend searching for [specific info]
from authoritative sources. Would you like me to perform a WebSearch to find
the exact [quote/list/specification]?
```

### Template B: Source Request
```
I can provide the exact [information] if you share [document/passage].
This ensures precision rather than relying on potentially imperfect recall.
Would you be able to upload or paste the relevant section?
```

### Template C: Caveat + Proceed
```
I cannot guarantee perfect accuracy without the source material, but I can
offer my best knowledge with the understanding that you should verify:

[Provide information]

⚠️ Recommended verification: [specific verification method]
```

### Template D: Multiple Options
```
For this request requiring high precision, here are your options:

**Most accurate:** I can search the web for authoritative sources
**Also accurate:** You could share the source document with me
**Less certain:** I can provide from memory with verification recommended

How would you like to proceed?
```

## Mitigation Selection Guide

**Choose WebSearch when:**
- Information is publicly available
- Official sources likely exist online
- Speed and accuracy both important
- User hasn't indicated they have the source

**Choose source request when:**
- Information is user-specific or private
- User likely has access to the material
- Precision is critical
- No reliable public sources available

**Choose caveat + proceed when:**
- User insists on immediate answer
- WebSearch unlikely to help
- User cannot provide source
- Acknowledging limitations is acceptable

**Choose multiple options when:**
- Unclear which approach user prefers
- Several viable paths exist
- User sophistication level unknown
- Collaborative decision appropriate

## Special Cases

### Already Have Partial Context

If user has shared some but not all relevant material:
- Note what you do/don't have access to
- Explain which parts you can answer precisely
- Request missing pieces for complete accuracy

### User Pushes Back on Warning

If user dismisses the warning and insists you answer:
- Comply but maintain caveats
- Mark uncertain elements clearly
- Reiterate verification recommendation
- Document that you provided warning

### Repeated Requests

If user makes multiple lexical recall requests:
- After first warning, can be more concise
- Still maintain accuracy standards
- Consider suggesting they provide source documents proactively
