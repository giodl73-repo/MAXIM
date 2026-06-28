---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-INDEXING-AND-ABSTRACTING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:indexing-and-abstracting
kind: guide
module: library-information-science
section: language-communication
title: Indexing and Abstracting - Subject Access, Coordination, Abstracts
status: source-custody
source_custody: partial
current_path: library-information-science/04-INDEXING-AND-ABSTRACTING.md
canonical_path: library-information-science/04-INDEXING-AND-ABSTRACTING.md
backsource_ids: [proof-backfill:library-information-science:04-indexing, git-history:library-information-science:04-indexing]
concepts: [subject indexing, pre-coordination, post-coordination, abstracting, exhaustivity, specificity, aboutness, indexing language]
root_concepts: [subject indexing]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Indexing & Abstracting — Building the Access Points

Classification places an item (file 01); cataloging describes it (file 02);
controlled vocabularies fix the terms (file 03). **Indexing** is the act that ties
them together: deciding what a document is *about* and assigning the terms that will
make it findable. **Abstracting** is its companion — writing the condensed surrogate
that lets a searcher judge relevance without the full text. Together they are the
human construction of the **inverted index** that retrieval (file 05) will query.

```
+======================================================================================+
|              FROM DOCUMENT TO ACCESS POINTS (the indexing pipeline)                  |
+======================================================================================+
|                                                                                      |
|   .----------.   .------------.   .--------------.   .---------------.               |
|   | DOCUMENT |-->| ABOUTNESS  |-->| TRANSLATE to |-->| ACCESS POINTS |               |
|   |          |   | analysis   |   | indexing     |   | (postings)    |               |
|   | full     |   | "what is   |   | language     |   | term -> doc   |               |
|   | text     |   |  this for?"|   | (the         |   | term -> doc   |               |
|   |          |   |            |   |  vocabulary) |   | ...           |               |
|   '----------'   '------------'   '--------------'   '---------------'               |
|                       |                 |                                            |
|         two knobs:    | EXHAUSTIVITY    | controlled (file 03) OR derived            |
|                       | (how many terms)| (extracted from the text itself)           |
|                       | SPECIFICITY     |                                            |
|                       | (how precise)   |                                            |
|                                                                                      |
|   In parallel:  ABSTRACT  -- a condensed surrogate of the content                    |
|                 (informative / indicative / structured)                              |
+======================================================================================+
```

The deep parallel: a search engine's indexer reads a document, extracts terms, and
writes postings lists (term -> document IDs). A human indexer does the same job by
judgment instead of tokenization — reads for *aboutness*, picks terms from a
controlled vocabulary, and produces postings. Everything in IR theory (file 05) has
a pre-computational analog here.

---

## Aboutness — The Hard Part

The central, irreducibly hard problem of indexing is determining **aboutness**: what
is this document actually about, as opposed to what words happen to appear in it? A
paper that mentions "Paris" in one example is not *about* Paris. Aboutness is a
semantic judgment that keyword frequency approximates but does not capture — which
is exactly why purely term-frequency retrieval has a ceiling and why human subject
indexing still adds value over full-text search.

```
   WORDS PRESENT  !=  ABOUTNESS

   A document can be ABOUT a concept it never names (a paper "about inflation"
   that only ever says "rising prices").
   A document can NAME a concept it is not ABOUT (a novel mentioning "quantum"
   once in dialogue).

   Human indexing assigns the ABOUT concept regardless of surface vocabulary.
   This is the recall/precision gap that controlled vocabularies (file 03) close.
```

---

## The Two Knobs: Exhaustivity and Specificity

Every indexing policy is a setting of two independent dials. They are the indexing-
language tuning parameters, and they trade off precisely against retrieval metrics.

```
+---------------------------------------------------------------------------+
|  EXHAUSTIVITY  (how MANY concepts you index)                              |
+---------------------------------------------------------------------------+
|   LOW  ----[ index only the 2-3 main topics ]----  HIGH                   |
|         index every minor concept the doc touches                         |
|                                                                           |
|   High exhaustivity  -> higher RECALL  (more doors into the doc)          |
|                      -> lower PRECISION (doc surfaces on marginal topics) |
+---------------------------------------------------------------------------+
|                                                                           |
+---------------------------------------------------------------------------+
|  SPECIFICITY  (how PRECISE each term is)                                  |
+---------------------------------------------------------------------------+
|   LOW (broad)  ----[ "Dogs" vs "Border Collies" ]----  HIGH (narrow)      |
|                                                                           |
|   High specificity   -> higher PRECISION (exact-match retrieval)          |
|                      -> lower RECALL if searcher uses a broader term      |
+---------------------------------------------------------------------------+
```

These are the same knobs you tune on any retrieval system: index more fields/terms
and you raise recall at the cost of precision; index narrower terms and you raise
precision at the cost of recall. The indexer is setting the operating point on the
precision/recall curve (file 05) by hand, document by document.

---

## Pre-Coordination vs. Post-Coordination

This is the central structural decision in subject access, and it is the same
decision as **"compose the compound key at write time or at query time?"**

```
+======================================================================================+
|                    PRE-COORDINATION  vs  POST-COORDINATION                           |
+======================================================================================+
|                                                                                      |
|   PRE-COORDINATION (combine at INDEX time)   POST-COORDINATION (combine at SEARCH)   |
|   ----------------------------------------   --------------------------------------  |
|                                                                                      |
|   The indexer builds the compound heading:   The indexer assigns single terms:       |
|                                                                                      |
|     "Children -- Diseases -- Treatment"        Children                              |
|     (one ordered string, fixed at index)       Diseases                              |
|                                                Treatment                             |
|                                                                                      |
|   The searcher must enter (or browse to)     The searcher COMBINES them with         |
|   the heading in the catalog's order.        Boolean AND at query time:              |
|                                                                                      |
|     [walk the heading hierarchy]               Children AND Diseases AND Treatment   |
|                                                                                      |
|   = a materialized composite key,            = independent indexed columns,          |
|     order baked in at write time               combined by the query planner         |
|                                                                                      |
|   LCSH subdivisions, traditional indexes     UNITERM (Taube, 1950s), Boolean DBs,    |
|                                              every modern search engine              |
+======================================================================================+
```

```
   OLD WORLD -> here

   PRE-COORDINATION   ==  a precomputed / materialized composite key.
                          Fast to look up the exact compound; rigid; the
                          combinations and their order are fixed at write time.
                          (Like a covering composite index built for one query
                          shape -- great if you query that shape, useless otherwise.)

   POST-COORDINATION  ==  separate single-term indexes ANDed/ORed at query time.
                          Flexible -- any combination the searcher invents -- at the
                          cost of doing the combination work per query.
                          (Like indexing each column and letting the optimizer
                          intersect postings lists on demand.)
```

The historical arc runs from pre- to post-coordination because computers made
query-time Boolean combination cheap. Mortimer Taube's **Uniterm** system (1950s)
was the pivot: assign atomic single terms and let the search combine them, rather
than pre-building every compound heading. Every modern search engine is post-
coordinate — it intersects postings lists at query time. Pre-coordination survives
in LCSH subdivisions and printed back-of-book indexes, where there is no query
engine to do the combining.

| | Pre-coordination | Post-coordination |
|---|---|---|
| When combined | At indexing time | At search time |
| Notation | One compound heading string | Independent single terms |
| Flexibility | Fixed combinations + order | Any Boolean combination |
| Searcher effort | Find the exact heading | Build the query |
| False drops | Few (combo is curated) | More (terms may co-occur unrelated) |
| CS analog | Materialized composite key | Indexed columns intersected at query |
| Examples | LCSH subdivisions, book indexes | Uniterm, Boolean DBs, web search |

---

## Derived vs. Assigned Indexing

Where do the index terms come from? Two sources, and the distinction maps to the
controlled-vs-free axis from file 03.

```
+----------------------------------------------------------------------------+
|  DERIVED (extraction)              |  ASSIGNED (controlled)                |
+----------------------------------------------------------------------------+
|  Terms taken FROM the text itself  |  Terms drawn from a controlled        |
|  (title words, keywords, full      |  vocabulary (LCSH, MeSH) by an        |
|  text tokenized).                  |  indexer's judgment.                  |
|                                    |                                       |
|  Cheap, automatic, scales.         |  Costly, human, precise.              |
|  Suffers synonymy/homonymy.        |  Resolves synonymy/homonymy.          |
|                                    |                                       |
|  = automatic tokenization /        |  = a human assigning enum values      |
|    keyword extraction              |    after reading for aboutness        |
+----------------------------------------------------------------------------+
```

A title-word index (KWIC — KeyWord In Context — Hans Peter Luhn, 1958, was an early
mechanized derived index) is fast and free but inherits all the ambiguity of natural
language. Assigned indexing from a controlled vocabulary is expensive human labor
but delivers the synonym/homonym control of a type system. Modern systems do both:
full-text derived indexing for recall, plus controlled assigned terms for precision.

---

## Abstracting — The Surrogate

An **abstract** is a condensed representation of a document, written so a searcher
can judge relevance without retrieving the full text. It is the document
*surrogate* — the snippet in the result list, scaled up to a paragraph.

```
+---------------------------------------------------------------------------+
|  TYPES OF ABSTRACT                                                        |
+---------------------------------------------------------------------------+
|  INFORMATIVE   Summarizes findings/results -- a substitute for the doc.   |
|                "The study found X increased Y by 30%."                    |
|                Used for: experimental/technical reports.                  |
|                                                                           |
|  INDICATIVE    Describes scope/topic -- tells you IF you want the doc,    |
|  (descriptive) not what it concluded. "This paper examines X."            |
|                Used for: reviews, essays, less structured works.          |
|                                                                           |
|  STRUCTURED    Labeled sections (Objective / Methods / Results /          |
|                Conclusions). Standard in biomedical literature.           |
|                = a schema-validated surrogate, parseable by machines.     |
|                                                                           |
|  CRITICAL      Adds evaluation of the work's quality/significance         |
|                (rare; closer to a review).                                |
+---------------------------------------------------------------------------+
```

The structured abstract is, in effect, a typed surrogate record — its labeled
fields are machine-extractable, which is why biomedical databases can parse and
filter on them. An informative abstract is lossy compression that preserves the
conclusion; an indicative one preserves only the topic signature. The choice is a
fidelity-vs-cost decision identical to choosing how much of a document to store in a
search snippet versus the index.

---

## Decision Cheat Sheet

| Goal | Approach |
|---|---|
| Maximize recall (find everything on a topic) | High exhaustivity, broader terms |
| Maximize precision (only exact-topic hits) | High specificity, fewer terms |
| Let searchers combine concepts freely | Post-coordinate (single terms) |
| Curated, browseable compound subjects | Pre-coordinate (LCSH subdivisions) |
| Cheap, automatic subject access | Derived indexing (keywords/full text) |
| Synonym/homonym-proof subject access | Assigned indexing (controlled vocab) |
| Let a searcher judge relevance fast | Write a good abstract (surrogate) |
| Machine-parseable summary | Structured abstract |
| Capture aboutness the words miss | Human assigned indexing |

---

## Common Confusion Points

### "Pre- vs. post-coordination — which is better?"

Post-coordination won for digital systems because query-time Boolean combination is
cheap and flexible — any combination the searcher invents works. Pre-coordination
persists where there is no query engine to combine terms (printed indexes) or where
curated, ordered compound headings aid browsing (LCSH). It is the materialized-key-
vs-query-time-join trade: pre-coordination is fast for the anticipated query and
rigid for everything else.

### "Isn't full-text search just better than human indexing now?"

Full-text search has higher recall and zero labor, but it indexes *words present*,
not *aboutness* — it misses documents about a concept they never name and surfaces
documents that merely mention a term. Human assigned indexing from a controlled
vocabulary closes that semantic gap. The best systems layer both.

### "Exhaustivity vs. specificity — aren't these the same dial?"

No. Exhaustivity is *how many* concepts you index (breadth); specificity is *how
narrow* each term is (depth/precision). You can index a document exhaustively with
broad terms, or sparsely with very specific ones. They are orthogonal knobs, and
each pushes precision/recall in different directions.

### "Abstract vs. summary — distinction?"

In LIS an abstract is a formal *surrogate* with a known type (informative,
indicative, structured, critical) and a defined function — to support a relevance
decision. "Summary" is the looser everyday word. The type matters: an informative
abstract can substitute for the document; an indicative one cannot.

### "Why does aboutness matter to a search engineer?"

Because it is the ceiling on any bag-of-words approach. Term frequency approximates
aboutness but conflates "mentions" with "is about." Every advance past plain
keyword matching — controlled vocabularies, link analysis, and later semantic
embeddings — is an attempt to estimate aboutness more faithfully than word counts
allow.
