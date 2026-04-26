# Web Writing: Scanability, Hypertext, SEO, Readability

## The Big Picture

```
HOW PEOPLE READ ON THE WEB
===========================

PRINT READING                  WEB READING
  Linear                         Non-linear
  Full sentences/paragraphs      Scanning, jumping
  Committed (chosen the book)    Evaluating (still deciding)
  Silent + focused               Interrupted environment
  Long attention span            Short attention span
  Sustained engagement           Looking for exit points

+------------------------------------------------------------------+
|  F-PATTERN (Nielsen Norman Group, 2006)                          |
|                                                                  |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- Horizontal sweep #1 (top)        |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- Horizontal sweep #2              |
|  XXXXXX                      <- Vertical scan down left          |
|  XXXXXX                      <- Left column continuation         |
|  XXXXXX                                                          |
|                                                                  |
|  LAYER CAKE PATTERN (subsequent research, 2017):                 |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- heading stripe                   |
|  x                           <- first word / few words only      |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- heading stripe                   |
|  x                                                               |
|                                                                  |
|  Z-PATTERN (landing pages, ad-heavy layouts):                    |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- left to right (top)              |
|                          X   <- diagonal to bottom right         |
|  XXXXXXXXXXXXXXXXXXXXXXXXX   <- left to right (bottom)           |
+------------------------------------------------------------------+
```

**The operative fact**: web readers do not read web pages. They scan them. They are looking for whether the page is worth reading. Your writing has to survive the scan before it gets read.

---

## Eye Tracking Research (Nielsen Norman Group)

Nielsen Norman Group (Jakob Nielsen + Don Norman) produced the foundational research on how people read web pages, starting in the 1990s and continuing through the 2010s:

```
KEY FINDINGS FROM EYE TRACKING STUDIES
========================================

1. F-PATTERN (2006, 232 users):
   - First horizontal scan: top of content area
   - Second shorter horizontal scan: further down
   - Vertical scan: down the left side
   Result: left column dominates; right column gets minimal attention
   Implication: critical information must be in top-left

2. LAYER CAKE PATTERN (2017 update):
   Users scan headings as visual anchors
   Between headings: only first word or two of each line
   Headings become the document; body text is secondary
   Implication: headings must communicate content, not label sections
     BAD: "Introduction"
     GOOD: "New search algorithm reduces click-through by 40%"

3. HOW MUCH DO PEOPLE READ?:
   Average page visit: 20-28 seconds (Nielsen 2008)
   Average page: 593 words (content sites)
   At 200 wpm: 593 words = ~3 minutes
   At 20 seconds: ~67 words read
   Users actually read: ~20-28% of words on average page
   -> Write for the scan; make the 20% count

4. COMMITMENT GRADIENT:
   If a page satisfies the scan test (correct answer visible),
   users WILL read more
   Scanning is not final behavior -- it is a gate
```

---

## Scanability Rules

```
SCANABILITY MECHANICS
======================

1. HEADERS AND SUBHEADERS:
   Break content into sections with descriptive headers
   Headers = the text users read even when skimming
   Use question format for how-to content:
     "How do I reset my password?" (conversational, specific)
   Use outcome format for informational:
     "Search algorithms prioritize mobile-first indexing"
   Never use label-style headers for scanned content:
     "Password Reset" (label) vs "Reset your password in 3 steps" (outcome)

2. BULLET LISTS:
   Convert any series of 3+ parallel items to a list
   Each bullet: start with the key word (information first)
     WRONG: "When you're ready to submit, click the button"
     RIGHT:  "Click Submit when ready"
   Maximum: 7 bullets (Miller's Law: 7+/-2 chunks)
   Lists fail for: sequential steps (use numbered list)
   Lists fail for: complex argument (use prose)

3. SENTENCE LENGTH:
   Average: 15-20 words per sentence for web content
   Vary length: short sentences create rhythm and emphasis
   Long sentences: fine for qualifying or complex argument
   BUT: topic sentence of each paragraph must be scannable
     (first sentence carries the paragraph's meaning)

4. PARAGRAPH LENGTH:
   Web paragraphs: 3-5 sentences typically
   One-sentence paragraphs: acceptable and sometimes powerful
   Long paragraphs: appropriate for specialist content
     where the reader has already committed

5. BOLD AND EMPHASIS:
   Bold: use for key terms, critical information, action items
   NOT for decoration; NOT for entire sentences
   Italics: titles, technical terms, emphasis
   ALL CAPS: sparingly; can read as shouting
   Underline: do NOT use (web convention: underline = link)
```

---

## Hypertext Structure

Tim Berners-Lee's original web design: documents linked to documents. This changes the writing unit:

```
HYPERTEXT WRITING PRINCIPLES
==============================

1. EVERY PAGE MUST STAND ALONE:
   Users arrive via search, social, or link -- not from beginning
   Do not assume they have read any prior page
   "Chunked writing" vs. "chapter writing"

2. LINK AS ARGUMENT:
   A link is a claim: "there is related information here"
   Link text must describe destination (not "click here")
     WRONG: "For more information click here"
     RIGHT:  "PageRank algorithm documentation"
   Screen reader users navigate by links alone
   (Accessibility intersects with clarity here)

3. DESTINATION WRITING:
   The first sentence of a page must confirm it is the right page
   Users who click a link are verifying a prediction
   If the first sentence doesn't match what they expected:
     they click back within 2-3 seconds

4. INTERNAL LINKING STRATEGY:
   Deep links (to specific sections): more useful than top-level
   Contextual links (in body text): outperform navigation links
   Link density: too few = missed opportunities;
                 too many = destination ambiguity ("which one?")

5. NON-LINEAR PATHS:
   Different users enter the same content at different points
   Navigation must support any entry sequence
   Table of contents on long pages = progressive navigation
   This is fundamentally different from book design
   where the author controls the reading sequence
```

---

## SEO Writing: Search-Intent Alignment

Modern SEO is not keyword stuffing. It is matching content to what users are actually trying to accomplish:

```
SEARCH INTENT TAXONOMY (Google's framework)
=============================================

NAVIGATIONAL:
  User wants a specific website
  Example: "microsoft azure portal"
  Content response: homepage or direct-access page
  Writing implication: brand name in title, fast load

INFORMATIONAL:
  User wants to learn something
  Example: "how does PageRank work"
  Content response: comprehensive explanation
  Writing implication: full coverage, structured, cited

COMMERCIAL INVESTIGATION:
  User is comparing options before buying
  Example: "best project management software 2025"
  Content response: comparison, reviews, criteria
  Writing implication: structured comparison table

TRANSACTIONAL:
  User wants to complete an action
  Example: "buy azure certification exam"
  Content response: product/service page with clear CTA
  Writing implication: friction-free, conversion-focused

MATCHING CONTENT TO INTENT:
  Informational query -> put information first (not a sales pitch)
  Transactional query -> put the purchase action first
  Getting this wrong is the most common SEO error:
  -> Informational content on a transactional page loses both
```

### E-E-A-T (Google's Quality Framework)

Google evaluates content on Experience, Expertise, Authoritativeness, Trustworthiness:

```
E-E-A-T (formerly E-A-T, "Experience" added 2022)
===================================================

EXPERIENCE: Has the author personally experienced this topic?
  Medical: "I had this condition and this is what worked"
  Travel: "I stayed at this hotel in March 2024"
  Product: "I used this tool for 6 months on a production system"

EXPERTISE: Does the author know the domain technically?
  Credentials, citations, technical accuracy
  "Your Money or Your Life" (YMYL) topics: medical, financial,
  legal -- require higher expertise signals

AUTHORITATIVENESS: Do others cite/reference this source?
  Backlinks from authoritative sites (industry publications)
  Citations, reviews, mentions from known sources

TRUSTWORTHINESS: Is the site technically secure and transparent?
  HTTPS, contact information, privacy policy, author bylines
  Consistent with factual accuracy
  No misleading ads, no hidden commercial intent

Implication for writing:
  Show who you are (byline, bio, credentials)
  Cite sources
  Update content (indicate freshness)
  Be transparent about commercial relationships
```

---

## Readability Scores: Tools and Limits

```
READABILITY METRICS
====================

FLESCH-KINCAID READING EASE (1948):
  Score: 0-100 (higher = easier to read)
  Formula: 206.835 - (1.015 * words/sentences)
                    - (84.6 * syllables/words)

  Score ranges:
  90-100: Very easy (5th grade)
  60-70:  Standard (8th-9th grade; most journalism)
  30-50:  Difficult (college)
  0-30:   Very difficult (professional)

FLESCH-KINCAID GRADE LEVEL:
  Estimates US school grade level
  (.39 * words/sentences) + (11.8 * syllables/words) - 15.59

Plain language target for government/consumer content: grade 8
Web content general target: grade 8-10

LIMITS OF READABILITY SCORES:
  They measure: sentence length + syllable count
  They do NOT measure: idea complexity, structure, coherence
  A complex idea in short sentences = high score, hard to understand
  A simple idea in long sentences = low score, still simple
  Use as a rough sanity check; not as an optimization target

GUNNING FOG INDEX:
  Similar to F-K; uses "complex words" (3+ syllables)
  Grade level estimate
  Used in business writing training

SMOG INDEX:
  Common in healthcare writing
  Based only on polysyllabic word count
```

---

## Structured Data Markup (Schema.org)

```
SCHEMA.ORG MARKUP
==================

What it is: machine-readable metadata in HTML
  Tells Google what kind of content is on the page
  Enables rich results in search (stars, prices, FAQs, etc.)

How it works:
  Add JSON-LD (JavaScript Object Notation for Linked Data)
  in a <script> tag to any page
  Describes the content type and key properties

Example: Article schema
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "PageRank Algorithm Explained",
    "author": {"@type": "Person", "name": "Jane Smith"},
    "datePublished": "2025-01-15",
    "dateModified": "2025-02-01"
  }

Key schema types for content:
  Article, BlogPosting, NewsArticle: editorial content
  FAQPage: FAQ format (gets accordion rich result)
  HowTo: step-by-step instructions
  Recipe: cooking content
  Product: e-commerce
  BreadcrumbList: navigation hierarchy
  Organization, Person: identity

Google uses schema for:
  Featured snippets, rich results, Knowledge Graph
  Not a ranking factor directly but enables rich display
  -> Higher click-through rate -> indirect ranking signal
```

---

## Decision Cheat Sheet

| Writing goal | Key principle |
|-------------|---------------|
| Page people will scan | Descriptive headers, front-loaded paragraphs, bullet lists |
| SEO for informational query | Match search intent; full coverage; E-E-A-T signals |
| SEO for transactional query | Clear CTA; product schema; conversion path |
| Accessible hyperlinks | Link text describes destination; not "click here" |
| Reading level check | Target grade 8-10 for general audience; use F-K as sanity check |
| Machine-readable content | JSON-LD schema.org markup for relevant content types |

---

## Common Confusion Points

**SEO is not keyword stuffing.** Modern Google understands semantic relationships. Exact keyword frequency is a minor signal; semantic relevance, E-E-A-T, and user satisfaction signals are dominant. "Writing for the algorithm" by loading keywords produces content that ranks poorly.

**The F-pattern is descriptive, not prescriptive.** The F-pattern describes how users scan badly designed pages. The goal is to design pages so users DON'T have to use the F-pattern — clear headers, front-loaded content, good visual hierarchy. You are not designing for the F-pattern; you are designing against it.

**Readability scores are not quality scores.** A piece can have grade 8 reading level and be excellent journalism. It can have grade 12 reading level and be excellent technical documentation. Match the audience, not a target score.

**Hypertext is not linear print.** The assumption that readers arrive at the beginning and proceed to the end is wrong for the web. Every page is a potential entry point; every paragraph must be evaluable in isolation.

**First page ≠ first result.** Ranking first for a query only helps if users search that query. Search volume, search intent alignment, and click-through rate all matter. A page ranking #1 for a zero-volume query serves no one.
