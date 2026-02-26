# Search Algorithms: PageRank, Query Understanding, Featured Snippets

## The Big Picture

```
SEARCH SYSTEM ARCHITECTURE
============================

QUERY -> QUERY UNDERSTANDING -> RETRIEVAL -> RANKING -> RESULTS

+------------------------------------------------------------------+
|  QUERY UNDERSTANDING         RANKING SIGNALS                    |
|                                                                  |
|  Named entity recognition     RELEVANCE:                        |
|  Intent classification         Keyword match                    |
|  Query rewriting               Semantic similarity               |
|  Spell correction              Topic modeling                    |
|  Language detection                                             |
|                                AUTHORITY:                        |
|                                 Backlink graph (PageRank)        |
|                                 E-E-A-T signals                  |
|                                 Brand mentions                   |
|                                                                  |
|                                FRESHNESS:                        |
|                                 Last modified date               |
|                                 Query freshness need             |
|                                                                  |
|                                UX SIGNALS:                       |
|                                 Click-through rate (CTR)         |
|                                 Dwell time / pogo-sticking       |
|                                 Core Web Vitals                  |
+------------------------------------------------------------------+
```

---

## PageRank: The Original Algorithm

PageRank was the mathematical foundation of Google when it launched in 1998 (Page & Brin, Stanford 1996 paper "The Anatomy of a Large-Scale Hypertextual Web Search Engine"):

```
PAGERANK CONCEPT
=================

INSIGHT: The web is a citation network.
  Academic papers: a paper cited by many important papers
    is more authoritative than one cited by few.
  Web pages: a page linked to by many important pages
    is more authoritative.

FORMULATION:
  PR(A) = (1-d) + d * (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))

  Where:
  PR(A) = PageRank of page A
  d = damping factor (typically 0.85)
  T1...Tn = pages that link to A
  C(Ti) = number of outbound links from Ti

  Intuition:
  A link from a high-PageRank page is worth more
  A page with many outbound links passes less value per link
  The damping factor represents the probability a random
  surfer continues clicking (vs. starting a new URL)

ITERATIVE COMPUTATION:
  Initialize all pages to PR=1
  Iterate: each page's PR = sum of incoming link contributions
  Repeat until convergence (usually ~50 iterations)
  Result: steady-state distribution (random walk stationary dist.)

ANALOGY (for a graph theory audience):
  PageRank = stationary distribution of a random walk
  on the directed web graph
  The "damping factor" prevents the walk from getting stuck
  in sink nodes (pages with no outbound links)
```

### Why PageRank Was Revolutionary

Pre-Google search (AltaVista, Yahoo! early): ranked purely by on-page keyword frequency. Easy to spam: add "buy cheap mortgage" 1,000 times in invisible text -> rank #1.

PageRank required external validation — links from other sites — which are harder to manufacture at scale. The fundamental insight was that the web's link structure was itself quality signal.

---

## Modern Ranking: Beyond PageRank

```
GOOGLE RANKING SIGNAL EVOLUTION
=================================

1998-2000: PageRank + keyword match
  -> Easily gamed with link farms

2003: Florida Update
  -> Penalized excessive keyword optimization
  -> Anchor text manipulation targeted

2011: Panda Update
  -> Targeted thin content, duplicate content, content farms
  -> Quality of the page's content matters

2012: Penguin Update
  -> Targeted manipulative link schemes
  -> Quality of inbound links matters, not just quantity

2013: Hummingbird
  -> Semantic understanding of queries
  -> Can interpret "what's the capital of the country
     Napoleon was exiled to?" -> synonym/concept inference

2015: RankBrain (first ML ranking factor)
  -> Machine learning to interpret ambiguous queries
  -> Learns from click behavior to improve query interpretation

2019: BERT (Bidirectional Encoder Representations from Transformers)
  -> Deep language understanding for long-tail queries
  -> Context within the query ("not" matters)

2021: MUM (Multitask Unified Model)
  -> Understands text, images, video simultaneously
  -> Can answer complex multi-step information needs

Current state: ~200+ ranking signals
  Machine learning decides their relative weights
  Google does not publish the exact formula
```

---

## Query Understanding

Before ranking documents, Google has to understand what the user wants:

```
QUERY CLASSIFICATION
=====================

NAVIGATIONAL:
  User wants a specific website
  Signal: brand name in query
  Example: "github.com", "azure portal login"
  Response: rank the target site #1; no alternatives needed

INFORMATIONAL:
  User wants to learn
  Signal: question words (how, what, why, who)
  Example: "how does TLS handshake work"
  Response: comprehensive explanation; featured snippet eligible

COMMERCIAL INVESTIGATION:
  User is comparing before buying
  Signal: "best", "vs.", "review", "comparison"
  Example: "best cloud database 2025"
  Response: comparison content; sometimes ads alongside

TRANSACTIONAL:
  User wants to complete an action
  Signal: action verbs, brand + "buy/price/free trial"
  Example: "azure subscription pricing"
  Response: pricing page or product page; ads likely

LOCAL:
  User wants something near them
  Signal: "near me", city name, or geographic intent inferred
  Example: "coffee shop" (Google infers: near current location)
  Response: map pack + local results

FRESH:
  User wants recent information
  Signal: news events, named entities + recent activity
  Example: "Microsoft earnings Q4 2025"
  Response: news articles; freshness heavily weighted
```

### Named Entity Recognition and Query Rewriting

```
NER AND QUERY REWRITING
========================

NER: Google identifies entities in queries
  "Satya Nadella Microsoft CEO" ->
  Entities: [person: Satya Nadella], [org: Microsoft], [role: CEO]
  Connects to Knowledge Graph entries for each entity

QUERY REWRITING:
  "capital of France" -> "Paris"
  (Google can answer without leaving results page)
  "Paris" with geographic intent -> Paris, France (not Paris, Texas)
  "Apple" -> disambiguation: fruit or company? (context decides)

SYNONYM EXPANSION:
  "car repair" -> "auto repair", "vehicle maintenance"
  "heart attack" -> "myocardial infarction"
  Google understands synonyms; doesn't require exact match

SPELL CORRECTION:
  "googel" -> "google"
  "microsooft" -> "microsoft"
  "Did you mean" for less confident corrections
```

---

## Featured Snippets and Zero-Click Search

```
FEATURED SNIPPETS (Position Zero)
===================================

What: A box above organic results answering the query directly
Types:
  PARAGRAPH: 40-50 words answering "what is" or "how to" questions
  LIST: numbered or bulleted (steps, rankings)
  TABLE: comparative data
  VIDEO: YouTube clip answering the query

HOW GOOGLE SELECTS:
  Takes content from a ranking page in the top ~10
  Identifies the text that best directly answers the query
  Reformats (sometimes truncates) for the snippet box

SEO IMPLICATION:
  You can rank #1 AND have the featured snippet taken
  from a lower-ranking competitor
  The snippet is the answer to the question -- it may replace
  the #1 click because users get the answer without clicking

ZERO-CLICK SEARCHES:
  SparkToro (2022): ~65% of Google searches end without a click
  Featured snippets, Knowledge Graph panels, direct answers
  all contribute to zero-click
  Implication: traffic from informational queries is declining
  Brand searches ("Microsoft" -> Knowledge Panel): rarely clicked

STRUCTURED SNIPPETS FOR FEATURED SNIPPET ELIGIBILITY:
  Format content to answer questions directly:
    "What is [X]? [X] is ..."
    Use the question as a header
    Follow immediately with a direct answer
    FAQPage schema increases featured snippet likelihood
```

---

## Google Algorithm Updates: Major History

| Year | Update | Target |
|------|--------|--------|
| 2011 | Panda | Thin/duplicate content, content farms |
| 2012 | Penguin | Manipulative link schemes, anchor text spam |
| 2013 | Hummingbird | Semantic query understanding |
| 2014 | Pigeon | Local search quality improvement |
| 2015 | RankBrain | ML for query interpretation |
| 2015 | Mobilegeddon | Mobile-friendliness as ranking factor |
| 2018 | Medic | E-A-T emphasis for health/finance/legal |
| 2019 | BERT | Transformer-based language understanding |
| 2021 | Core Web Vitals | Page speed and UX metrics as ranking |
| 2022 | Helpful Content | Penalize AI-generated unhelpful content |
| 2023 | SGE (Search Generative Experience) | AI-generated search summaries |
| 2024 | HCU rollout | Large-scale penalty for AI spam sites |

---

## Core Web Vitals (Technical Ranking Factors)

```
CORE WEB VITALS (2021+ ranking factor)
========================================

LCP (Largest Contentful Paint):
  Time for the largest visible content element to load
  Target: < 2.5 seconds
  Measures: perceived load speed (when does it look ready?)

FID (First Input Delay) / INP (Interaction to Next Paint):
  Time from first user interaction to browser response
  Target FID: < 100ms
  Target INP (2024 replacement): < 200ms
  Measures: interactivity responsiveness

CLS (Cumulative Layout Shift):
  Unexpected layout shifts while loading
  Target: < 0.1
  Problem: content loads and pushes other content (ads injecting)
  Measures: visual stability

WHY THESE MATTER:
  Google's hypothesis: fast, stable, interactive pages
  produce better user experience -> better user signals
  -> better for search users -> should rank better

MEASUREMENT:
  Google Search Console (free): shows CWV data for your site
  PageSpeed Insights: per-URL analysis
  Chrome User Experience Report (CrUX): real-user data
```

---

## Decision Cheat Sheet

| Ranking factor category | Key signals |
|------------------------|------------|
| Relevance | Keyword match, semantic similarity, BERT/MUM understanding |
| Authority | PageRank (backlinks), E-E-A-T, brand mentions |
| Freshness | Last modified date, query freshness demand |
| UX | Core Web Vitals, mobile-friendliness, CTR, dwell time |
| User intent match | Query classification alignment, content format match |

| Query type | Content response |
|-----------|-----------------|
| Navigational | Homepage or direct destination page |
| Informational | Comprehensive, structured, citable |
| Commercial | Comparison tables, reviews, criteria |
| Transactional | Product/service page, clear CTA, friction-free |
| Local | Location-optimized page, Google Business Profile |

---

## Common Confusion Points

**PageRank is not how Google ranks pages today.** PageRank was the original core algorithm. Modern Google uses 200+ signals with machine learning weighting. PageRank remains one factor, but it is one of hundreds.

**Backlinks are not dead.** Despite constant "backlinks don't matter anymore" claims, they remain a significant authority signal. What has changed: quality matters enormously; quantity alone is not positive (and can be negative if low-quality). One link from a relevant authoritative source >> 100 links from spam sites.

**Zero-click is increasing.** Google's business interest is to answer queries without clicking away. Featured snippets, Knowledge Panels, and AI Overviews (SGE) all reduce traffic to content creators. Understanding this changes the ROI calculation for informational SEO.

**"Google penalized my site" is usually an algorithm update, not a manual action.** Manual penalties require a human reviewer at Google. Algorithm updates (especially Panda/Penguin/Helpful Content) hit millions of sites automatically. Check Google Search Console for manual action notifications to distinguish.

**Core Web Vitals are a tiebreaker, not a primary ranking factor.** For a given query, content relevance and authority dominate. CWV matters when relevance is approximately equal between competing pages. It is not a path to ranking improvement for poor-quality content.
