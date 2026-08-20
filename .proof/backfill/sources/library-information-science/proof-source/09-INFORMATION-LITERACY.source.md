---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-INFORMATION-LITERACY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:information-literacy
kind: guide
module: library-information-science
section: language-communication
title: Information Literacy - Search Skills, Evaluation, Information Ethics
status: source-custody
source_custody: partial
current_path: library-information-science/09-INFORMATION-LITERACY.md
canonical_path: library-information-science/09-INFORMATION-LITERACY.md
backsource_ids: [proof-backfill:library-information-science:09-literacy, git-history:library-information-science:09-literacy]
concepts: [information literacy, search strategy, source evaluation, lateral reading, information ethics, copyright, information economics, ACRL Framework]
root_concepts: [information literacy]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Information Literacy — Finding, Judging, and Using Information Well

Every prior file built the system; this one is about the **user standing in front of
it**. Information literacy is the set of competencies to find information efficiently,
**evaluate** its credibility, use it ethically, and understand the economic and power
structures that govern who can access it at all. In an era of abundant, weaponized, and
machine-generated content, evaluation has shifted from a soft skill to a core
competency — the human layer that no retrieval engine replaces.

```
+======================================================================================+
|                       THE INFORMATION-LITERATE WORKFLOW                              |
+======================================================================================+
|                                                                                      |
|   .---------.   .---------.   .-----------.   .--------.   .------------------.      |
|   | DEFINE  |-->| SEARCH  |-->| EVALUATE  |-->|  USE   |-->| ACT ETHICALLY    |      |
|   | the need|   | (strat- |   | (credibil-|   | (synth-|   | (cite, respect   |      |
|   |         |   |  egy)   |   |  ity)     |   |  esize)|   |  IP, privacy)    |      |
|   '---------'   '---------'   '-----------'   '--------'   '------------------'      |
|        ^                                                          |                  |
|        |              iterate: results reshape the question        |                 |
|        '----------------------------------------------------------'                  |
|                                                                                      |
|   WRAPPED BY THE STRUCTURAL CONTEXT:                                                 |
|   .---------------------------------------------------------------------.            |
|   | ETHICS (privacy, intellectual freedom)  +  ECONOMICS (who pays,     |            |
|   | who is excluded -- the access divide, copyright, the attention      |            |
|   | economy)                                                            |            |
|   '---------------------------------------------------------------------'            |
+======================================================================================+
```

The standard professional framework is the **ACRL Framework for Information Literacy
for Higher Education** (2016), which reframed literacy from a checklist of skills into
six *threshold concepts* — ideas that, once grasped, change how you see the whole
information landscape. The two most load-bearing are "Authority Is Constructed and
Contextual" (credibility depends on context and is not intrinsic) and "Information Has
Value" (information is an economic and political good, not free-floating). The rest of
this file develops the workflow and those structural concepts.

---

## Search Strategy — Querying as Engineering

A skilled searcher treats a search like query optimization: model the need, build a
structured query, read the result set as signal, and iterate. This is file 05's
machinery operated deliberately.

```
+---------------------------------------------------------------------------+
|  BUILDING A QUERY (the searcher as query planner)                         |
+---------------------------------------------------------------------------+
|                                                                           |
|   1. CONCEPTS   break the need into independent concept blocks            |
|                 (each block = one facet, file 01/04)                      |
|                                                                           |
|   2. SYNONYMS   OR within a block   (car OR automobile OR vehicle)        |
|                 -> raises RECALL                                          |
|                                                                           |
|   3. COMBINE    AND across blocks   (block1) AND (block2)                 |
|                 -> raises PRECISION                                       |
|                                                                           |
|   4. REFINE     phrase "..", truncation comput*, proximity, field limits  |
|                 (date, peer-reviewed, language)                           |
|                                                                           |
|   5. ITERATE    read results -> adjust terms -> re-run (relevance         |
|                 feedback by hand)                                         |
+---------------------------------------------------------------------------+
```

The "OR your synonyms, AND your concepts" pattern is post-coordinate Boolean retrieval
(file 04) applied by a human, and it directly tunes the precision/recall operating
point (file 05). A database/legal/scholarly searcher does this explicitly; a web
searcher does a compressed version, leaning on the engine's ranking instead of strict
Boolean. Knowing *which* tool to query is itself a skill — a controlled scholarly
database (with its controlled vocabulary, file 03) versus a web engine versus a
specialized index are different instruments with different precision/recall profiles.

---

## Source Evaluation — Credibility as a Verdict

The hardest and most important competency. The old "CRAAP" checklist (Currency,
Relevance, Authority, Accuracy, Purpose) treats a source in isolation — and research
on how professional fact-checkers actually work showed that approach is weak against
sophisticated misinformation, which is engineered to *pass* a surface checklist.

```
+======================================================================================+
|              VERTICAL READING  vs  LATERAL READING                                   |
+======================================================================================+
|                                                                                      |
|   VERTICAL (the weak default)            LATERAL (what fact-checkers do)             |
|   ----------------------------           ------------------------------              |
|   Stay ON the page. Judge it by          LEAVE the page immediately. Open new        |
|   its own look: does it seem             tabs and ask what OTHERS say about          |
|   professional? cite sources?            this source. Who is behind it? What         |
|   have an "About" page?                  is their reputation/funding/agenda?         |
|                                                                                      |
|   FAILS: a polished site engineered      WORKS: cross-checks against the wider       |
|   to look authoritative passes.          record before trusting -- triangulation.    |
|                                                                                      |
|   = trusting a record's self-report      = verifying against independent sources     |
+======================================================================================+
```

**Lateral reading** — leaving a source to investigate it from outside, the way a
fact-checker opens new tabs — is the current best practice and the core update to
evaluation pedagogy. The engineering parallel is sharp: you do not assess a service's
trustworthiness only from its own marketing page (self-reported), you check independent
reputation, incidents, and third-party signals (triangulation against external
evidence). "Authority is constructed and contextual": a physician is an authority on
medicine, not on climate modeling; credibility is domain- and context-bound, never a
global property of a name.

This competency is now existential because of two forces:

```
   FORCE 1: MIS/DISINFORMATION
   misinformation = false, spread without intent to deceive.
   disinformation = false, spread DELIBERATELY to deceive.
   Filter bubbles and engagement-optimized feeds amplify both.

   FORCE 2: GENERATIVE AI
   fluent, confident, plausible text and media at zero marginal cost,
   including fabricated "facts" (hallucinations) and synthetic media.
   Surface fluency NO LONGER signals reliability -- which guts the
   vertical-reading heuristic entirely. Provenance > polish.
```

When generation is free and fluent, fluency stops being evidence of care or truth. The
only durable signals are provenance, corroboration, and source track record — i.e.
lateral verification. This is the same shift as moving from "the binary looks signed,
trust it" to "verify the signature and the chain independently."

---

## Information Ethics — Privacy, Freedom, Integrity

Using information well carries obligations. LIS has a strong professional ethics
tradition built on a few principles a technologist should weigh seriously.

```
+---------------------------------------------------------------------------+
|  PILLARS OF INFORMATION ETHICS                                            |
+---------------------------------------------------------------------------+
|  INTELLECTUAL    the right to seek and receive information freely; the    |
|  FREEDOM         professional stance against censorship.                  |
|                                                                           |
|  PRIVACY /       what a person reads is confidential. (US libraries       |
|  CONFIDENTIALITY resist disclosing borrowing records -- a stance tested   |
|                  by post-9/11 surveillance law.) A reader-data-           |
|                  minimization ethic, decades before "privacy by design."  |
|                                                                           |
|  ATTRIBUTION /   cite sources; do not plagiarize; respect the chain of    |
|  INTEGRITY       provenance. (Same lineage discipline as file 06.)        |
|                                                                           |
|  EQUITY OF       everyone deserves access regardless of means -- the      |
|  ACCESS          ethical root of the public library and of open access.   |
+---------------------------------------------------------------------------+
```

The privacy stance is notable: libraries adopted reader-record confidentiality and
data minimization as professional ethics long before the tech industry arrived at
"privacy by design" and data-minimization principles. Patron borrowing data is treated
as something to *not* retain and *not* disclose — a deliberately small data footprint
as an ethical default. That is a posture worth importing.

---

## Information Economics — Who Pays, Who Is Excluded

Information has economic properties that make it behave unlike physical goods, and
those properties drive access policy, copyright, and the attention economy.

```
+---------------------------------------------------------------------------+
|  WHY INFORMATION IS A STRANGE ECONOMIC GOOD                               |
+---------------------------------------------------------------------------+
|  NON-RIVAL      my using it does not deplete your copy (unlike bread).    |
|                 Marginal cost of an extra copy ~ 0.                       |
|  HIGH FIXED,    expensive to produce the first copy, ~free to reproduce.  |
|  LOW MARGINAL                                                             |
|  EXPERIENCE     you often cannot judge its value until you consume it.    |
|  GOOD                                                                     |
+---------------------------------------------------------------------------+
|  CONSEQUENCES:                                                            |
|   - Markets need artificial scarcity (COPYRIGHT) to fund creation,        |
|     trading off access against incentive.                                 |
|   - When CONTENT is abundant and free, the scarce resource becomes        |
|     ATTENTION -> the attention economy (bridge: media-studies/,           |
|     behavioral-economics/, digital-media/).                               |
|   - Access splits by ability to pay -> the DIGITAL DIVIDE and the         |
|     access motive behind OPEN ACCESS (file 07).                           |
+---------------------------------------------------------------------------+
```

```
   THE COPYRIGHT BALANCE (the core tension)

   too STRONG <----------------------------------------> too WEAK
   locks up knowledge,                          no incentive to create,
   blocks access & reuse                        underproduction

   Mechanisms in between: FAIR USE / fair dealing (limited use without
   permission), the PUBLIC DOMAIN (term expiry), and CREATIVE COMMONS
   (standardized author-granted reuse licenses -- like open-source
   licenses for content). Open access (file 07) routes around the toll.
```

Copyright is the deliberate, time-limited artificial scarcity society imposes on a
non-rival good to fund its creation — the perennial access-vs-incentive tradeoff, the
same one open-source licensing navigates for code. When content itself becomes
abundant and near-free, the binding constraint moves to **attention**, and the
business model becomes capturing it (the attention economy — see `media-studies/`,
`behavioral-economics/`, `digital-media/`). And because access still tracks ability to
pay, the **digital divide** persists as the equity problem that animates both the
public library and the open-access movement (file 07). For a VP, this is the political
economy underneath every "information wants to be free" debate.

---

## Old World → New World

| Literacy concept | Engineering / familiar parallel |
|---|---|
| Boolean search strategy | Query construction; tuning precision/recall |
| Lateral reading | Verify reputation via independent signals, not self-report |
| Authority is contextual | Trust is domain-scoped, not a global property |
| Reader-record confidentiality | Data minimization / privacy by design |
| Attribution / provenance | Lineage and citation discipline (file 06) |
| Non-rival good + high fixed cost | Software economics (copy cost ~ 0) |
| Copyright balance | Access-vs-incentive; like open-source licensing |
| Creative Commons | Standardized reuse licenses, content edition of OSS licenses |
| Attention economy | Engagement optimization as the real product |

---

## Decision Cheat Sheet

| Goal | Approach |
|---|---|
| Find scholarly material precisely | Controlled database + Boolean + controlled vocab |
| Cast a wide first net | Web engine, broad terms, then narrow |
| Judge an unfamiliar source | Lateral reading — investigate it from outside |
| Detect engineered/AI-generated content | Trust provenance and corroboration, not fluency |
| Decide who is an "authority" | Scope to the relevant domain and context |
| Reuse someone's work legally | Check license/fair use; prefer CC or public domain |
| Protect patrons'/users' reading data | Minimize and do not disclose (privacy by default) |
| Understand why journals cost so much | Information economics + the serials crisis (file 07) |
| Widen access | Open access, public provision, address the digital divide |

---

## Common Confusion Points

### "Isn't search a solved skill — everyone can Google?"

Finding *something* is easy; finding the *right* thing efficiently and knowing whether
to trust it is not. Skilled searching means picking the right tool (a controlled
database vs. a web engine), constructing queries that tune precision/recall, and
reading results as signal. The gap between a casual and an expert searcher is as wide
as between writing any SQL and writing a query that uses the indexes well.

### "Why is the CRAAP checklist not enough anymore?"

Because checklists evaluate a source by its own surface (does it look professional,
cite things, have an About page) — and sophisticated misinformation is engineered to
pass exactly those tests. Lateral reading (leave the page, check what independent
sources say about it) is what professional fact-checkers actually do and what survives
adversarial content. You verify against external evidence, not the source's self-report.

### "Does generative AI make information literacy obsolete or essential?"

Essential. When fluent, confident, plausible text and media are free to generate,
surface fluency stops signaling reliability — which destroys the vertical-reading
heuristic of "it reads well, so trust it." The durable signals become provenance,
corroboration, and source track record: precisely the lateral-verification skills this
file teaches. The engine got stronger; the human judgment layer got more important.

### "Information ethics — isn't that just 'don't plagiarize'?"

Attribution is one pillar. The tradition also covers intellectual freedom (anti-
censorship), reader privacy/confidentiality (a data-minimization ethic the field
adopted decades before the tech industry), and equity of access. These are
professional commitments with real stakes — libraries have resisted surveillance
demands for borrowing records on exactly these grounds.

### "Why should a technologist care about information economics?"

Because it is the political economy under every access decision you touch. Information
is non-rival with near-zero copy cost, so markets impose artificial scarcity
(copyright) to fund creation; when content is abundant, attention becomes the scarce
good and the product; and access tracks ability to pay, producing the digital divide.
Open access, content licensing, and the attention economy are all consequences of
these properties — the same economics that govern software.
