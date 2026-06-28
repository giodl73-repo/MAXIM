---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:cataloging-and-metadata
kind: guide
module: library-information-science
section: language-communication
title: Cataloging and Metadata - MARC, RDA, FRBR, BIBFRAME, Dublin Core
status: source-custody
source_custody: partial
current_path: library-information-science/02-CATALOGING-AND-METADATA.md
canonical_path: library-information-science/02-CATALOGING-AND-METADATA.md
backsource_ids: [proof-backfill:library-information-science:02-cataloging, git-history:library-information-science:02-cataloging]
concepts: [cataloging, metadata, MARC 21, AACR2, RDA, FRBR, BIBFRAME, Dublin Core, bibliographic description, authority control]
root_concepts: [bibliographic metadata]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Cataloging & Metadata — Describing the Item

If classification (file 01) decides *where* an item goes, cataloging decides *how
we describe it* — the metadata record. This is the schema-design half of LIS, and
its history is a textbook schema-evolution arc: a flat binary record (MARC) gains a
normalized entity model (FRBR), gets a modern content standard (RDA), and is
finally re-expressed as a graph (BIBFRAME). A lightweight competitor (Dublin Core)
runs alongside for the cases where the heavy record is overkill.

```
+=======================================================================================+
|                THE CATALOGING STACK: CONTENT RULES vs ENCODING vs MODEL               |
+=======================================================================================+
|                                                                                       |
|   WHAT to record (content rules)        HOW to encode it        Conceptual MODEL      |
|   ------------------------------        ----------------        ---------------       |
|                                                                                       |
|   AACR2 (1978) --> RDA (2010)           MARC 21 (the           FRBR (1998) -->        |
|   "rules for choosing & forming         binary serialization)  LRM. Work /            |
|    the description"                      |                      Expression /          |
|        |                                 |                      Manifestation /       |
|        |    content standard             |   record format     Item entities          |
|        v                                 v                          |                 |
|   .---------------------.        .------------------.               v                 |
|   | which fields, how   |  ==>   | fields 245, 100, |        BIBFRAME (2011)          |
|   | to transcribe a     |        | 260, 650 ... in  |        re-encodes the model     |
|   | title, name, date   |        | tagged subfields |        as RDF triples           |
|   '---------------------'        '------------------'                                 |
|                                                                                       |
|   LIGHTWEIGHT ALTERNATIVE:  Dublin Core -- 15 elements, web-native, "good enough"     |
+=======================================================================================+
```

Keep three axes separate or you will conflate them: **content rules** (what to put
in a field — AACR2/RDA), **encoding** (the wire format — MARC, then RDF), and the
**conceptual model** (the entities and relationships — FRBR). They are orthogonal,
the way a coding style guide, a serialization format, and a data model are
orthogonal in software.

---

## MARC 21 — The Record Format (1968)

MARC (MAchine-Readable Cataloging), developed at the Library of Congress under
Henrietta Avram, was the first standard for putting catalog records into a
computer. MARC 21 is the harmonized US/Canadian version. Structurally it is a
**flat record of numbered fields**, each field carrying indicators and
letter-coded subfields — essentially a tag-length-value serialization of a catalog
card.

```
+----------------------------------------------------------------------------+
|  ANATOMY OF A MARC FIELD                                                   |
+----------------------------------------------------------------------------+
|                                                                            |
|   245  1 0  $a The Lord of the Rings / $c J.R.R. Tolkien.                  |
|   ---  | |  |--------------------------|---------------------|             |
|    |   | |        subfield $a                  subfield $c                 |
|    |   | |        (title proper)               (statement of resp.)        |
|    |   | '--- 2nd indicator (0 = no chars to skip in filing)               |
|    |   '----- 1st indicator (1 = add a title-added entry)                  |
|    '--------- TAG 245 = "Title Statement"                                  |
+----------------------------------------------------------------------------+
```

A handful of tags carry most of the weight:

| MARC tag | Field |
|----------|-------|
| 001 | Control number (record ID) |
| 020 | ISBN |
| 100 | Main entry — personal author |
| 245 | Title statement |
| 250 | Edition |
| 260 / 264 | Publication (place, publisher, date) |
| 300 | Physical description (pages, size) |
| 650 | Subject — topical (links to a controlled vocabulary, file 03) |
| 700 | Added entry — additional author/contributor |
| 856 | Electronic location (URL) |

MARC's strength is interoperability: a record cataloged once at the Library of
Congress is downloaded and reused by thousands of libraries (copy cataloging). Its
weakness is that it is a **flat, pre-relational schema** that hard-codes the
assumptions of the catalog card. It cannot natively express that ten editions and
a film adaptation are all the same *work* — there is no Work entity, only repeated
near-duplicate records. That limitation is exactly what FRBR was created to fix.

```
   OLD WORLD -> here
   A MARC record is a fixed-schema row with tagged columns and a
   binary directory at the front pointing to each field's offset.
   Think: a TLV-serialized struct whose field IDs are three-digit
   tags and whose nested members are letter-keyed subfields.
```

---

## AACR2 → RDA — The Content Rules

MARC says *where* to put the title; **content standards** say *how to form* it —
how to transcribe an author's name, how to handle multiple authors, what counts as
an edition. *Anglo-American Cataloguing Rules, 2nd ed.* (AACR2, 1978) governed
this for decades. Its successor, **RDA — Resource Description and Access** (2010),
was built deliberately to align with the FRBR model and to work for digital and
networked resources, not just print.

| | AACR2 (1978) | RDA (2010) |
|---|---|---|
| Worldview | Card-and-print era | FRBR/digital, any medium |
| Underlying model | Implicit, flat | Explicit FRBR entities |
| Abbreviations | Heavy (p., ill., s.l.) | Spelled out ("take what you see") |
| "Rule of three" authors | Truncate after 3 | Record all if desired |
| Encoding-agnostic | Tied to print conventions | Designed for MARC *and* linked data |

RDA is a **content standard, not an encoding** — you can express an RDA-conformant
description in MARC today and in BIBFRAME/RDF tomorrow. That separation of content
rules from serialization is the same discipline as keeping validation/business
rules independent of your wire format.

---

## FRBR — The Entity Model (1998)

FRBR (*Functional Requirements for Bibliographic Records*) is the moment cataloging
got a proper data model. It introduces the **WEMI** hierarchy — four Group 1
entities that finally distinguish the abstract creation from the physical object on
the shelf.

```
+----------------------------------------------------------------------------+
|  FRBR GROUP 1 ENTITIES (WEMI) -- one diagram, one outer box                |
+----------------------------------------------------------------------------+
|                                                                            |
|   .--------------------.                                                   |
|   |  WORK              |  the abstract intellectual creation               |
|   |  "Hamlet"          |  (no language, no format yet)                     |
|   '---------+----------'                                                   |
|             | is realized through                                          |
|             v                                                              |
|   .--------------------.                                                   |
|   |  EXPRESSION        |  a specific intellectual form                     |
|   |  "Hamlet, in       |  (this translation, this edition's text,          |
|   |   English text"    |   a particular performance)                       |
|   '---------+----------'                                                   |
|             | is embodied in                                               |
|             v                                                              |
|   .--------------------.                                                   |
|   |  MANIFESTATION     |  a published form / edition                       |
|   |  "Penguin 2005     |  (this ISBN, this print run)                      |
|   |   paperback"       |                                                   |
|   '---------+----------'                                                   |
|             | is exemplified by                                            |
|             v                                                              |
|   .--------------------.                                                   |
|   |  ITEM              |  a single physical or digital copy                |
|   |  "the copy on      |  (barcode 31234..., this exact object)            |
|   |   shelf, barcode"  |                                                   |
|   '--------------------'                                                   |
+----------------------------------------------------------------------------+
```

This is a clean **ER normalization**, and the cardinalities are the point:

```
   WORK  1 ----< many  EXPRESSION  1 ----< many  MANIFESTATION  1 ----< many  ITEM

   One Work (Hamlet) has many Expressions (English text, German translation,
   audiobook), each Expression has many Manifestations (Penguin ed., Norton ed.),
   each Manifestation has many Items (the physical copies on shelves).
```

FRBR also defines **Group 2** entities (Person and Corporate Body — the
agents responsible; the Family entity was added later, in FRAD 2009) and **Group 3** (concepts, objects, events, places — the
*subjects*, which is where controlled vocabularies in file 03 attach). The 2017
consolidation, the **IFLA Library Reference Model (LRM)**, unified these three
models into one.

For a data modeler, WEMI is the answer to "why is my catalog full of near-
duplicate rows?" — MARC stored Manifestations and Items but had no Work or
Expression entity to factor out the shared abstraction. FRBR is the normalization
pass MARC skipped: pull the repeating title/author/subject facts up into a Work
row and join.

---

## BIBFRAME — The Graph Re-encoding (2011)

BIBFRAME (Bibliographic Framework Initiative, led by the Library of Congress) is
the planned successor to MARC as the **encoding**. It re-expresses the FRBR-style
model as **RDF**: every entity (work, instance, item, person, subject) becomes a
resource with a URI, and the catalog becomes a graph of triples instead of a stack
of flat records.

```
   MARC (flat record)                 BIBFRAME (RDF triples)
   ------------------                 ----------------------
   100 $a Tolkien, J.R.R.             <work#1>  bf:title    "The Lord of the Rings"
   245 $a The Lord of the Rings       <work#1>  bf:creator  <person#42>
   650 $a Fantasy fiction             <person#42> rdfs:label "Tolkien, J.R.R."
                                      <work#1>  bf:subject  <concept#fantasy>
   one self-contained record          subject-predicate-object, joinable
   that repeats author text            across the entire web of data
```

BIBFRAME's core classes are **Work**, **Instance** (close to FRBR's Manifestation),
and **Item**, plus Agents and Subjects. Because everything is a URI-addressed node,
a library's catalog stops being an island: an author node can resolve to the same
identity used by Wikidata or a publisher, and the catalog becomes queryable with
SPARQL (see `query-languages/` for the syntax, and file 08 for linked data). This
is the same move you would make replacing a denormalized export with a proper
graph where shared entities are referenced, not copied.

---

## Dublin Core — The Lightweight Alternative (1995)

Not everything needs a full MARC record. Dublin Core is a deliberately minimal
metadata standard — **exactly 15 elements** — designed to describe *any* web
resource with the smallest useful schema. It emerged from a 1995 workshop in
Dublin, Ohio (hence the name; nothing to do with Ireland).

```
+----------------------------------------------------------------------------+
|  THE 15 DUBLIN CORE ELEMENTS                                               |
+----------------------------------------------------------------------------+
|   1. Title         6. Contributor   11. Source                             |
|   2. Creator       7. Date          12. Language                           |
|   3. Subject       8. Type          13. Relation                           |
|   4. Description    9. Format        14. Coverage                          |
|   5. Publisher    10. Identifier     15. Rights                            |
+----------------------------------------------------------------------------+
|   All 15 are OPTIONAL and REPEATABLE. Schema-on-read, not schema-on-write. |
+----------------------------------------------------------------------------+
```

| | MARC 21 | Dublin Core |
|---|---|---|
| Field count | Hundreds of tags/subfields | 15 elements |
| Audience | Professional catalogers | Anyone, web-wide |
| Granularity | Very high | Coarse, "good enough" |
| Typical use | Library catalogs, full bibliographic control | Web resources, repositories, harvesting |
| Encoding | MARC binary / MARCXML | XML, RDFa, JSON, HTML `<meta>` |
| Mindset | Strict schema, rich description | Minimal common denominator |

Dublin Core is the "just enough metadata" tier — the JSON-with-15-optional-keys to
MARC's exhaustive enterprise schema. It powers metadata *harvesting* across
repositories (file 08) precisely because the schema is small enough that everyone
can produce it. The tradeoff is exactly the one you know: a tiny permissive schema
buys interoperability and loses descriptive precision.

---

## The Whole Stack, One View

```
+----------------------------------------------------------------------------------+
| Standard           | Layer            | Era                  | Equivalent        |
+----------------------------------------------------------------------------------+
| AACR2              | content rules    | 1978                 | print-era style   |
| RDA                | content rules    | 2010                 | model-aware rules |
| FRBR / LRM         | conceptual model | 1998 / 2017          | normalized ER     |
| MARC 21            | encoding         | 1968                 | binary TLV record |
| BIBFRAME           | encoding         | 2011                 | RDF graph         |
| Dublin Core        | lightweight all  | 1995                 | 15-key JSON-ish   |
+----------------------------------------------------------------------------------+
```

---

## Decision Cheat Sheet

| I need to... | Use |
|---|---|
| Exchange full bibliographic records between libraries | MARC 21 |
| Follow current cataloging content rules | RDA (AACR2 is legacy) |
| Model why editions/translations share an abstract work | FRBR / LRM (WEMI) |
| Put the catalog on the web as linked data | BIBFRAME (RDF) |
| Describe a web resource with minimal effort | Dublin Core (15 elements) |
| Harvest metadata across many repositories | Dublin Core via OAI-PMH (file 08) |
| Attach a subject to a record | MARC 650 / FRBR Group 3 + a vocabulary (file 03) |
| Distinguish "the book" from "this copy" | FRBR Manifestation vs. Item |

---

## Common Confusion Points

### "MARC vs. Dublin Core — which one do I use?"

Different tiers, not competitors. MARC is the heavyweight professional record for
full bibliographic control (hundreds of fields, exchanged between libraries).
Dublin Core is the lightweight 15-element schema for describing arbitrary web
resources and for harvesting. Use MARC when you need precision and interoperate
with libraries; use Dublin Core when you need "good enough" metadata at web scale.

### "Is RDA a replacement for MARC?"

No — this is the most common conflation. RDA is *content rules* (how to form the
data); MARC is the *encoding* (how to store it). RDA-conformant data is routinely
encoded in MARC today and can be encoded in BIBFRAME tomorrow. They live on
different axes.

### "Work vs. Expression vs. Manifestation vs. Item — give me the test"

Work = the idea (Hamlet). Expression = a specific intellectual realization (the
English text, a German translation, a particular recorded performance).
Manifestation = a published edition (a specific ISBN/print run). Item = one
physical or digital copy (a barcode). Going down the chain, you add successively:
form, then publication, then a single object.

### "BIBFRAME replaces FRBR?"

No. FRBR/LRM is the *model* (the entities and relationships); BIBFRAME is an
*encoding* that expresses that model as RDF. BIBFRAME is the planned replacement
for MARC, not for FRBR. Model and serialization, again, on different axes.

### "Why is there a Work entity at all — isn't a record per book enough?"

Because without it, all knowledge that ten editions and three translations are
"the same thing" is duplicated across ten records and stays uncomputable. The Work
entity is the normalized parent that lets a search collapse them, recommend across
them, and reason about them as one creation. It is the join key MARC never had.
