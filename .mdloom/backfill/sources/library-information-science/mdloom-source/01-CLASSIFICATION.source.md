---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-CLASSIFICATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:classification
kind: guide
module: library-information-science
section: language-communication
title: Classification - Dewey, LC, UDC, and Faceted Schemes
status: source-custody
source_custody: partial
current_path: library-information-science/01-CLASSIFICATION.md
canonical_path: library-information-science/01-CLASSIFICATION.md
backsource_ids: [mdloom-backfill:library-information-science:01-classification, git-history:library-information-science:01-classification]
concepts: [classification, Dewey Decimal Classification, Library of Congress Classification, Universal Decimal Classification, Colon Classification, faceted classification, call number, notation]
root_concepts: [library classification]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Classification — Where Knowledge Goes on the Shelf

Classification is the **ontology design** problem of LIS: partition the entire
universe of recorded knowledge into a structure where every item has a place, the
place is computable from the item's subject, and the structure sorts so that
related things sit together. The output is a **notation** (a call number) — a
sortable key that encodes the item's position in the scheme.

Four schemes dominate, and they split cleanly along the tree-vs-facet axis from
the overview. Read this landscape left (oldest/most enumerative) to right (most
faceted/synthetic).

```
+=======================================================================================+
|                    THE FOUR MAJOR CLASSIFICATION SCHEMES                              |
+=======================================================================================+
|                                                                                       |
|   ENUMERATIVE  <------------------------------------------------>  FACETED            |
|   (pre-built tree, pick a node)              (axes you combine on demand)             |
|                                                                                       |
|   .------------.    .------------.    .------------.    .--------------------.        |
|   |   DEWEY    |    |     LC     |    |    UDC     |    |  COLON (Ranganathan)|       |
|   |   (DDC)    |    |   (LCC)    |    |            |    |                     |       |
|   |            |    |            |    |            |    |                     |       |
|   | 10 classes |    | 21 letter  |    | Dewey base |    | Pure facets: P,M,E, |       |
|   | 000-999    |    | classes    |    | + facet    |    | S, T (Personality,  |       |
|   | decimal    |    | A-Z (5     |    | connectors |    | Matter, Energy,     |       |
|   | fractions  |    | unused)    |    | : + ( ) =  |    | Space, Time)        |       |
|   |            |    |            |    |            |    |                     |       |
|   | public     |    | research / |    | European,  |    | rarely deployed;    |       |
|   | libraries  |    | academic,  |    | scientific |    | theoretically       |       |
|   | worldwide  |    | US LoC     |    | bibliog.   |    | foundational        |       |
|   '------------'    '------------'    '------------'    '---------------------'       |
|        1876             1897              1905                  1933                  |
|                                                                                       |
+=======================================================================================+
```

A useful first cut: **Dewey** is a fixed 10-way numeric tree tuned for browsing in
public libraries; **LC** is a broader, deeper alphanumeric tree tuned for the
literary-warrant collections of a giant research library; **UDC** bolts faceted
connectors onto a Dewey-like base; **Colon** is pure facet theory, the schema-
design idea that influenced everything after it even though it is rarely the actual
shelving system.

---

## Dewey Decimal Classification (DDC, 1876)

Melvil Dewey's insight: use the **decimal fraction** as the notation so the scheme
is infinitely subdividable. The top level is exactly **10 main classes**; each
splits into 10 divisions, each into 10 sections — a base-10 tree where the digits
of the number *are* the path from root to leaf.

```
+---------------------------------------------------------------------------+
|  THE TEN DEWEY MAIN CLASSES (the 100s)                                    |
+---------------------------------------------------------------------------+
|  000  Computer science, information & general works                       |
|  100  Philosophy & psychology                                             |
|  200  Religion                                                            |
|  300  Social sciences                                                     |
|  400  Language                                                            |
|  500  Pure science (mathematics & natural sciences)                       |
|  600  Technology (applied sciences)                                       |
|  700  Arts & recreation                                                   |
|  800  Literature                                                          |
|  900  History & geography                                                 |
+---------------------------------------------------------------------------+
```

The digits read like a path expression:

```
   500  Science
   |
   510  Mathematics            <- second digit narrows
   |
   516  Geometry               <- third digit narrows
   |
   516.3  Analytic geometries  <- decimal point: keep subdividing forever
   |
   516.375  ...                <- depth is unbounded by design
```

This is a **radix tree on the subject path**. The number 516.375 *is* the route
root -> Science -> Math -> Geometry -> Analytic -> .... Because it is a decimal
fraction, sorting the strings sorts the tree in-order, so the shelf order *is* a
depth-first traversal. That is the same trick a materialized-path or
lexicographically-sortable key uses to make hierarchy queryable by string compare.

Dewey adds **auxiliary tables** (standard subdivisions, geographic areas,
languages) that you append to a base number — an early dose of faceting inside an
enumerative scheme. DDC is maintained today by OCLC and exists in 200+ language
editions; it is the default for public libraries worldwide.

**Weakness:** the 10-way fan-out and 19th-century worldview are baked in.
Religion (200) is overwhelmingly Christianity; the rest of the world's religions
are crammed into 290s. Computing had to be wedged into 000 (general works)
because Dewey had no slot for it. A fixed-arity enumerative tree ages badly — the
schema cannot be migrated without renumbering the whole shelf.

---

## Library of Congress Classification (LCC, 1897)

The Library of Congress could not use Dewey: a 10-way tree is too shallow for tens
of millions of volumes. LCC uses **21 letter classes** (A–Z, with I, O, W, X, Y
unused as top-level classes), giving a much wider top-level fan-out, and combines
letters with numbers for depth. It is built on **literary warrant** — categories
exist because the collection actually contains books on them, not because a
theorist drew the tree top-down.

```
+---------------------------------------------------------------------------+
|  LC LETTER CLASSES (top level)                                            |
+---------------------------------------------------------------------------+
|  A  General works         |  N  Fine arts                                 |
|  B  Philosophy, psych,    |  P  Language & literature                     |
|     religion              |  Q  Science                                   |
|  C  Auxiliary sciences    |  R  Medicine                                  |
|     of history            |  S  Agriculture                               |
|  D  World history         |  T  Technology                                |
|  E  History of the Americas |  U  Military science                        |
|  F  History (US local /   |  V  Naval science                             |
|     Americas)             |  Z  Bibliography, library science             |
|  G  Geography, anthro.    |                                               |
|  H  Social sciences       |  (I, O, W, X, Y left open for expansion)      |
|  J  Political science     |                                               |
|  K  Law                   |                                               |
|  L  Education             |                                               |
|  M  Music                 |                                               |
+---------------------------------------------------------------------------+
```

A call number reads as a compound sortable key:

```
   QA  76 . 73 . P98  R67  2024
   ||  ||   ||  |||||  |||  ||||
   ||  ||   ||  |||||  |||  '--- year
   ||  ||   ||  |||||  '-------- second Cutter (author/title)
   ||  ||   ||  '--------------- first Cutter: .P98 = "Python"
   ||  ||   '------------------- subclass refinement
   ||  '----------------------- topic number within QA
   '--------------------------- class QA = Mathematics (incl. computer science)
```

The **Cutter number** (.P98) is an alphanumeric hash of an author or topic name
designed to file alphabetically — a deterministic short code so that two items at
the same topic still get a stable, unique, sortable position. It is, functionally,
a tie-breaking key appended to the subject key.

| | Dewey (DDC) | Library of Congress (LCC) |
|---|---|---|
| Notation | Pure decimal numbers | Letters + numbers (alphanumeric) |
| Top-level arity | 10 classes | 21 letter classes |
| Built by | Top-down theory (Dewey's outline) | Literary warrant (the collection) |
| Depth | Unbounded via decimals | Deep via letter+number combos |
| Best for | Public libraries, browsing | Large research/academic collections |
| Granularity | Coarse at top, fine via decimals | Very fine throughout |
| Governance | OCLC | Library of Congress |

---

## Universal Decimal Classification (UDC, 1905)

UDC started as a French/Belgian extension of Dewey (by Otlet and La Fontaine, who
also dreamed of a universal documentation network — a paper-era hyperlink vision).
It keeps a Dewey-like numeric base but adds **connecting symbols** that let you
*synthesize* compound subjects on the fly. This is where enumerative meets faceted.

```
+---------------------------------------------------------------------------+
|  UDC AUXILIARY CONNECTORS (the synthesis operators)                       |
+---------------------------------------------------------------------------+
|   +   addition / coordination   621+622    (two subjects together)        |
|   /   consecutive range         592/599    (a span of classes)            |
|   :   relation                  17:7       (ethics in relation to art)    |
|   ( ) place / form / common     (410)      (Great Britain)                |
|   =   language                  =111       (in English)                   |
|   " " time                      "19"       (the 20th century)             |
+---------------------------------------------------------------------------+
```

So `622(410)"19"=111` reads as "mining, in Great Britain, in the 20th century, in
English" — a query expressed in the call number itself. These connectors are
**operators in a little algebra of subjects**: the colon is a relation, the
parentheses are a place/form facet, the `=` is a language facet. You are composing
a key from orthogonal dimensions instead of choosing a single tree node. UDC is
favored in European special and scientific libraries and in bibliographic
databases where this expressive compounding pays off.

---

## Colon Classification & Faceted Theory (Ranganathan, 1933)

Ranganathan rejected the premise of enumerative schemes — that you can enumerate
every compound subject in advance. Instead, classify a subject **analytically**
(break it into facets), then **synthesize** the notation by combining facet values
in a fixed citation order. He named exactly **five fundamental categories**, the
PMEST facets:

```
+---------------------------------------------------------------------------+
|  RANGANATHAN'S FIVE FUNDAMENTAL CATEGORIES (PMEST)                        |
+---------------------------------------------------------------------------+
|   P  Personality  the focal "thing" / main subject (the entity)           |
|   M  Matter       the material / substance                                |
|   E  Energy       the action / process / operation                        |
|   S  Space        the place / geography                                   |
|   T  Time         the period                                              |
+---------------------------------------------------------------------------+
|   Citation order is fixed: P  M  E  S  T                                  |
|   Facets are joined by punctuation (the ":" gave the scheme its name).    |
+---------------------------------------------------------------------------+
```

```
   A subject is a TUPLE, not a node:

   ( Personality , Matter , Energy , Space , Time )
        |            |        |        |       |
        v            v        v        v       v
     "literature"  "Hindi"  "criticism" "India" "1950s"

   Synthesized notation strings these facets together in citation order.
```

This is **analytico-synthetic** classification, and it is exactly relational
decomposition. PMEST is a five-column composite key; the citation order is the
declared sort order of the columns; "synthesis" is building the key from the parts.
A senior data modeler will see a star schema: one fact (the document) joined to
five conformed dimensions (P/M/E/S/T). Colon Classification is almost never the
actual shelving system in production libraries — its contribution was the *theory*.
Faceted navigation in every catalog, every e-commerce filter sidebar, and every
multi-axis tagging system is Ranganathan's idea industrialized.

```
   OLD WORLD (enumerative)            NEW WORLD (faceted, Ranganathan)
   ----------------------            -------------------------------
   ONE category column,              MANY orthogonal facet columns,
   pick the nearest leaf.            combine values at query time.

   = a single category FK            = a star schema / tag dimensions
   = rigid tree, hard to migrate     = composable, evolves without renumber
```

---

## Notation as a Sortable Key

The deep idea uniting all four schemes: the call number is a **lexicographically
sortable key whose sort order reproduces the intended browse order**. Shelving is
just sorting; the scheme designer's job is to encode the subject tree (or facet
tuple) into a string that string-compares into the right sequence.

```
   Dewey:   516.375   -> decimal fraction, string-sorts as tree depth-first
   LC:      QA76.73   -> letter(s) + number + Cutter, multi-segment sort
   UDC:     622(410)  -> base + facet connectors, structured compound
   Colon:   PMEST     -> fixed citation order = declared column sort order

   In all four: SORT THE KEYS  ==  WALK THE INTENDED ORDER.
```

This is the same reason a well-designed clustered index key or a ULID puts related
or time-ordered rows physically adjacent: the encoding makes range scans and
ordered traversal fall out of plain comparison.

---

## Decision Cheat Sheet

| Situation | Use / expect |
|---|---|
| Public library, browsing patrons | Dewey (DDC) |
| Large academic / research collection | Library of Congress (LCC) |
| US national / federal collection | LCC (it is LoC's own scheme) |
| European scientific / special library | UDC |
| Compound multi-axis subjects in a bibliography | UDC connectors or facets |
| Designing a *new* subject scheme today | Faceted (Ranganathan), not enumerative |
| Need infinite subdivision in pure numbers | Dewey decimals |
| Need wide top-level fan-out for huge corpus | LCC letter classes |
| Modeling subjects as a star schema | Colon / PMEST is your conceptual ancestor |

---

## Common Confusion Points

### "Dewey has 10 classes but I see hundreds of numbers"

Ten *main* classes, each subdivided 10 ways into divisions, each into 10 sections
(1000 three-digit base numbers), then unbounded decimal subdivision after that. The
"10" is only the top-level arity of the radix tree.

### "Why does LC use letters and Dewey use numbers — is one better?"

Different tradeoffs. Letters give LC a wider top-level fan-out (good for huge,
deep collections); decimals give Dewey infinite in-place subdivision and a simpler
mental model (good for browsing). Neither is universally better — it is a fan-out
vs. depth schema decision, the same one you make choosing a partitioning strategy.

### "Is a call number the same as a subject heading?"

No, and this is the key split. A call number (this file) is **one** location — the
partitioning key that puts the item on a shelf. A subject heading (file 03) is one
of **many** access points describing what the item is about. One classification,
many subjects.

### "UDC and Dewey look identical"

UDC's *base* is Dewey-derived, but UDC adds the connector algebra (`: + ( ) = " "`)
that lets you synthesize compound subjects. Plain Dewey can only append a few
auxiliary tables; UDC turns synthesis into a first-class operation. UDC is Dewey
with composition operators.

### "Colon Classification — why learn a scheme nobody shelves with?"

Because its *theory* (PMEST, analytico-synthetic classification) is the
intellectual source of faceted search, multi-axis tagging, and star-schema subject
modeling. You will rarely see a Colon call number, but you use Ranganathan's idea
every time you filter by several independent dimensions at once.
