---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:information-retrieval
kind: guide
module: library-information-science
section: language-communication
title: Information Retrieval - Boolean, Ranked, Precision and Recall
status: source-custody
source_custody: partial
current_path: library-information-science/05-INFORMATION-RETRIEVAL.md
canonical_path: library-information-science/05-INFORMATION-RETRIEVAL.md
backsource_ids: [proof-backfill:library-information-science:05-retrieval, git-history:library-information-science:05-retrieval]
concepts: [information retrieval, Boolean retrieval, ranked retrieval, precision, recall, relevance, TF-IDF, BM25, inverted index, vector space model]
root_concepts: [information retrieval]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Information Retrieval — Finding and Ranking

Everything upstream — classify, describe, control, index — exists so this step can
work: take a query, return the documents that satisfy the user's need, best first.
Information retrieval (IR) is the information-science half of LIS made quantitative,
and it is the direct ancestor of the search engine. The two retrieval paradigms split
on one question: does a document **match** (set membership) or **score** (a ranking)?

```
+========================================================================================+
|                       TWO RETRIEVAL PARADIGMS                                          |
+========================================================================================+
|                                                                                        |
|   BOOLEAN (exact-match, set)             RANKED (best-first, scored)                   |
|   --------------------------             ----------------------------                  |
|                                                                                        |
|   query: cats AND dogs NOT fish          query: cats dogs                              |
|        |                                      |                                        |
|        v                                      v                                        |
|   .------------------.                  .---------------------------.                  |
|   | postings sets:   |                  | score every doc by a       |                 |
|   | cats = {1,4,7}   |                  | similarity/weight model:   |                 |
|   | dogs = {4,9}     |                  |   TF-IDF, BM25, vector      |                |
|   | INTERSECT -> {4} |                  | sort DESC, return top-k     |                |
|   '------------------'                  '---------------------------'                  |
|                                                                                        |
|   RESULT: an unordered SET             RESULT: a ranked LIST                           |
|   (in or out -- no degree)            (every doc has a relevance score)                |
|                                                                                        |
|   = set algebra on inverted lists      = a scoring function over the same lists        |
+========================================================================================+
```

Both paradigms run over the same data structure — the **inverted index** (term ->
postings list of document IDs), the human-built version of which is file 04. The
difference is purely in what you do with the postings: Boolean intersects/unions
them into a set; ranked retrieval weights and sums them into a score.

---

## The Inverted Index

The substrate of all retrieval. For each term, store the list of documents
containing it (the postings list). A query touches only the terms it mentions, not
the whole corpus — the reason search is sublinear in collection size.

```
+---------------------------------------------------------------------------+
|  INVERTED INDEX (term -> postings)                                        |
+---------------------------------------------------------------------------+
|   term        postings (docID : term-frequency, positions)                |
|   --------    --------------------------------------------                |
|   "cat"   ->  [ d1:3 , d4:1 , d7:2 ]                                      |
|   "dog"   ->  [ d4:5 , d9:1 ]                                             |
|   "fish"  ->  [ d2:1 , d7:4 ]                                             |
+---------------------------------------------------------------------------+
|   Boolean AND  =  intersect postings sets.                                |
|   Ranked        =  combine per-term weights across postings.              |
+---------------------------------------------------------------------------+
```

This is the same structure a search engine, a database full-text index (the GIN
index in PostgreSQL, FULLTEXT in MySQL, see `database-systems/`), and a card-catalog
subject index all use. The card catalog *was* an inverted index maintained by hand:
one drawer per subject heading, cards (document surrogates) filed under it.

---

## Boolean Retrieval

The classic library/database model: a query is a logical expression over terms, and
a document either satisfies it or not. Exact, predictable, and the model behind every
professional database search interface (legal, medical, patent).

```
   Operators:   AND (intersect)   OR (union)   NOT (difference)
   Proximity:   "machine NEAR/3 learning"   (within 3 words)
   Truncation:  comput*    (computer, computing, computation, ...)
   Phrase:      "information retrieval"     (adjacent, in order)

   ( cat OR feline ) AND ( disease OR illness ) NOT veterinary
```

| Strength | Weakness |
|---|---|
| Exact, transparent, reproducible | No ranking — 5 or 5,000 hits, all "equal" |
| Expert control over the set | Feast-or-famine (too many / zero results) |
| Auditable (you can prove coverage) | Requires query-construction skill |
| Deterministic | No notion of "more relevant" |

Boolean's fatal flaw at web scale is the lack of ranking: a two-term AND over a
billion documents returns millions of equally-ranked hits, which is useless to a
human who reads the first page. That is what ranked retrieval solves.

---

## Ranked Retrieval and Term Weighting

Ranked retrieval scores every document for the query and sorts. The score rests on
two intuitions formalized in the 1970s, combined into **TF-IDF**:

```
+----------------------------------------------------------------------------+
|  TF-IDF  (the foundational term weight)                                    |
+----------------------------------------------------------------------------+
|                                                                            |
|   TF  Term Frequency        a term appearing more often in a document      |
|                             signals that document is more about it.        |
|                                                                            |
|   IDF Inverse Document       a term appearing in FEW documents is more     |
|       Frequency             discriminating. "the" is in everything ->      |
|                             near-zero weight. "quasispecies" is rare ->    |
|                             high weight.                                   |
|                                                                            |
|   weight(term, doc) = TF * IDF                                             |
|     -> rare terms that are frequent in THIS doc score highest              |
+----------------------------------------------------------------------------+
```

In the **vector space model** (Gerard Salton, the SMART system, 1960s-70s) each
document and the query become vectors in term space; relevance is the **cosine
similarity** between them. This is the conceptual grandparent of dense-vector
search — same geometry (vectors, cosine), but sparse term-count dimensions instead
of learned dense embeddings.

The production-standard refinement is **BM25** (Okapi BM25, Robertson and Sparck
Jones, 1990s): TF-IDF with two corrections that matter in practice —

```
   BM25 fixes two TF-IDF problems:

   1. TERM-FREQUENCY SATURATION
      The 50th occurrence of a word adds less than the 2nd. BM25 caps the TF
      contribution with a saturating function (parameter k1) instead of letting
      it grow linearly.

   2. DOCUMENT-LENGTH NORMALIZATION
      Long documents trivially contain more term occurrences. BM25 normalizes by
      length (parameter b) so a long doc is not unfairly favored.
```

BM25 is still the default lexical ranker in Elasticsearch, OpenSearch, Lucene, and
most full-text engines in 2026. It is what "keyword search" means in production, and
it is the baseline every neural retrieval system is measured against.

```
   THE RETRIEVAL LINEAGE (sparse -> dense)

   Boolean  ->  TF-IDF  ->  BM25  ->  dense / vector retrieval (embeddings)
   set        weighted    length-     learned semantic similarity
   match      sum         normalized  (see ai-engineering/)
              cosine      saturated

   Modern systems run HYBRID: BM25 for lexical precision + vectors for semantic
   recall, fused (e.g. reciprocal rank fusion). This file owns everything left
   of "dense"; ai-engineering/ owns the embedding layer.
```

---

## Precision and Recall — The Core Metrics

How good is a retrieval result? Two complementary measures, predating IR theory
(librarians used them informally for decades), now the standard evaluation of any
classifier or retriever you will ever build.

```
+-----------------------------------------------------------------------------+
|  THE RELEVANCE CONFUSION MATRIX                                             |
+-----------------------------------------------------------------------------+
|                                                                            |
|                       |  RELEVANT        |  NOT RELEVANT                    |
|   ----------------------------------------------------------------------     |
|   RETRIEVED           |  True Positive   |  False Positive (noise)          |
|   NOT RETRIEVED       |  False Negative  |  True Negative                   |
|                       |  (a miss)        |                                  |
|                                                                            |
|   PRECISION = TP / (TP + FP)   "of what I returned, how much was right?"    |
|   RECALL    = TP / (TP + FN)   "of all that was right, how much did I get?" |
+-----------------------------------------------------------------------------+
```

```
   The fundamental tension:

   PRECISION up  <-------------------->  RECALL up
   (return only sure things)            (return everything possibly relevant)

   Return ONE perfect doc:   precision = 1.0, recall ~ 0
   Return the WHOLE corpus:  recall = 1.0, precision ~ 0

   You trade one for the other; the operating point is a policy choice.
```

| Measure | Question it answers | When it dominates |
|---|---|---|
| **Precision** | Are my results clean? | Web search (page 1 must be good) |
| **Recall** | Did I miss anything? | Legal discovery, systematic reviews, patents |
| **F1** | Balanced single number | Harmonic mean of P and R |
| **P@k** | Precision in the top k | Ranked results (what the user sees) |
| **MAP** | Mean Average Precision | Averaged precision across queries/ranks |
| **nDCG** | Graded relevance, position-discounted | When relevance is not binary |

The precision/recall split is the same dial as exhaustivity/specificity from file 04
— the indexer sets the corpus-side operating point, the retriever sets the query-
side one. A high-recall need (a patent attorney who cannot miss prior art) calls for
exhaustive indexing *and* recall-favoring queries; a high-precision need (a web user)
calls for the opposite. The single most expensive mistake in IR is optimizing the
wrong one for the task.

---

## Relevance — The Slippery Foundation

All of the above assumes we know which documents are "relevant." Relevance is the
field's deepest unsolved concept: it is **user-, task-, and time-dependent**, not an
intrinsic property of a document.

```
+---------------------------------------------------------------------------+
|  DIMENSIONS OF RELEVANCE                                                  |
+---------------------------------------------------------------------------+
|  TOPICAL     Is it about the subject?        (what TF-IDF/BM25 estimates) |
|  COGNITIVE   Does it match what THIS user already knows / needs?          |
|  SITUATIONAL Is it useful for the task at hand, right now?                |
|  AFFECTIVE   Does it satisfy the user (trust, novelty, format)?           |
+---------------------------------------------------------------------------+
|  Algorithms estimate TOPICAL relevance well and the rest poorly --        |
|  which is why ranking signals (clicks, recency, authority) and learning-  |
|  to-rank exist: to approximate the dimensions the text alone cannot.      |
+---------------------------------------------------------------------------+
```

Test collections (Cranfield methodology, 1960s; the modern **TREC** evaluations) make
IR measurable by fixing a corpus, a query set, and human relevance judgments, then
scoring systems against them. This is the held-out labeled test set of search — the
same discipline as a benchmark suite for a model. Without it, "better ranking" is
unfalsifiable.

---

## Old World → New World

| IR concept | Modern equivalent |
|---|---|
| Inverted index | Lucene/Elasticsearch index, DB full-text (GIN/FULLTEXT) |
| Boolean retrieval | Database `WHERE` / advanced search filters |
| TF-IDF / vector space | Sparse keyword scoring; ancestor of vector search |
| BM25 | Default lexical ranker in production search |
| Cosine similarity (sparse) | Cosine over dense embeddings (`ai-engineering/`) |
| Precision / recall | The same metrics in ML classification |
| Test collection / TREC | Held-out benchmark with labeled judgments |
| Relevance feedback | Click-through learning, learning-to-rank |

---

## Decision Cheat Sheet

| Need | Use |
|---|---|
| Exact, auditable, expert search (legal/patent) | Boolean retrieval |
| Best-first results for a general user | Ranked retrieval (BM25) |
| Production lexical ranking baseline | BM25 |
| Catch every relevant doc (cannot miss any) | Optimize recall |
| Keep results clean (page 1 matters most) | Optimize precision |
| Single balanced metric | F1 |
| Score ranked lists with graded relevance | nDCG |
| Compare retrieval systems rigorously | Test collection / TREC-style eval |
| Semantic match beyond keywords | Add dense vectors (`ai-engineering/`) |
| Best of both | Hybrid: BM25 + vectors, fused |

---

## Common Confusion Points

### "Precision vs. recall — which do I optimize?"

It depends entirely on the cost of the two error types. If a miss is catastrophic
(legal discovery, systematic medical review, prior-art search), optimize recall and
tolerate noise. If the user reads only the top few results (web search), optimize
precision. They trade against each other; picking the wrong one for the task is the
classic IR failure.

### "Boolean vs. ranked — is Boolean obsolete?"

No. Boolean is exact, auditable, and reproducible — indispensable where you must
*prove* coverage (legal, patent, regulatory). Ranked retrieval wins at web scale
because it solves Boolean's lack of ordering. Many professional systems offer both:
Boolean to define the set, ranking to order it.

### "Is BM25 obsolete now that we have embeddings?"

No — it remains the production-default lexical ranker in 2026 and the baseline every
neural system is compared against. It is strong on exact terms, rare words, and
names, where embeddings can blur. The state of the art is *hybrid*: BM25 for lexical
precision plus vectors for semantic recall, fused together.

### "Isn't the vector space model already 'vector search'?"

Same geometry, different vectors. Salton's vector space model uses sparse term-count
dimensions (one per vocabulary word). Modern vector search (`ai-engineering/`) uses
dense learned embeddings (a few hundred to a few thousand dimensions capturing
meaning). Both rank by cosine similarity; the 1970s version is the sparse,
interpretable ancestor of the dense, learned one.

### "Why is relevance 'unsolved' — a document is either about the topic or not"

Topical aboutness is only one dimension. A topically-perfect document can still be
irrelevant because the user already knows it (cognitive), it does not fit the
current task (situational), or they distrust the source (affective). Algorithms
estimate topical relevance well and the rest poorly, which is the entire reason
ranking uses behavioral and authority signals beyond the text.
