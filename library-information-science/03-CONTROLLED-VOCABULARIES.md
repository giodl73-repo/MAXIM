---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:controlled-vocabularies
kind: guide
module: library-information-science
section: language-communication
title: Controlled Vocabularies - LCSH, Thesauri, Taxonomies, Ontologies
status: source-custody
source_custody: partial
current_path: library-information-science/03-CONTROLLED-VOCABULARIES.md
canonical_path: library-information-science/03-CONTROLLED-VOCABULARIES.md
backsource_ids: [proof-backfill:library-information-science:03-vocabularies, git-history:library-information-science:03-vocabularies]
concepts: [controlled vocabulary, LCSH, thesaurus, taxonomy, ontology, authority control, ISO 25964, SKOS, subject heading]
root_concepts: [controlled vocabulary]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Controlled Vocabularies — A Type System for Subjects

Natural language is ambiguous: "car" and "automobile" mean the same thing; "java"
means a language, an island, and a drink. If subject terms were free text, the same
concept would scatter across synonyms and the same string would collapse distinct
concepts. A **controlled vocabulary** fixes this by mandating one canonical term per
concept and recording the relationships between concepts. It is, precisely, a **type
system for the subject field** — a closed set of legal values with declared
sub/super relations and synonym aliases.

The family runs from a flat list to a full logical model, gaining structure at each
step. Read left (least expressive) to right (most expressive).

```
+======================================================================================+
|              THE CONTROLLED-VOCABULARY SPECTRUM (expressiveness ->)                  |
+======================================================================================+
|                                                                                      |
|   CONTROLLED      TAXONOMY          THESAURUS          ONTOLOGY                      |
|   LIST            (hierarchy)       (semantic net)     (logical model)               |
|   ----------      -----------       --------------     --------------                |
|   .--------.      .--------.        .--------.         .------------.                |
|   | flat   |      |  tree  |        | tree + |         | classes +  |                |
|   | enum   | ===> | BT/NT  |  ===>  | RT,USE,|  ===>   | properties,|                |
|   | of legal|     | only   |        | UF, SN |         | axioms,    |                |
|   | terms  |      |        |        | (ISO   |         | inference  |                |
|   |        |      |        |        | 25964) |         | (OWL/RDF)  |                |
|   '--------'      '--------'        '--------'         '------------'                |
|                                                                                      |
|   = a string      = an enum with    = a graph of      = a typed schema with          |
|     enum            a parent FK       semantic edges     relations + reasoner        |
|                                                                                      |
|   examples: a      Dewey-as-tree,    LCSH, MeSH,       Schema.org, FOAF,             |
|   fixed picklist   library taxon.    Getty AAT, ERIC   Wikidata, domain OWL          |
+======================================================================================+
```

The jump from taxonomy to thesaurus is the jump from "parent links only" to "a
typed graph of relationships." The jump from thesaurus to ontology is the jump from
"controlled human-readable terms" to "machine-reasonable logical statements." Each
step trades simplicity for inferential power, exactly as a type system gains power
going from an enum to a hierarchy to a system with parametric relations.

---

## Authority Control — The Master-Data Problem

Before the vocabulary structure, the foundational mechanism: **authority control**.
For any name or term that can be written multiple ways, the library maintains one
**authority record** declaring the authorized form and listing the variants that
map to it. This is master-data management / canonical-entity resolution, full stop.

```
+---------------------------------------------------------------------------+
|  AN AUTHORITY RECORD (master record for one entity)                       |
+---------------------------------------------------------------------------+
|  AUTHORIZED FORM:   Twain, Mark, 1835-1910                                |
|  variants (mapped to the authorized form):                                |
|     - Clemens, Samuel Langhorne, 1835-1910   (the real name)              |
|     - Snodgrass, Quintus Curtius              (a pseudonym)               |
|     - "Mark Twain"                                                        |
+---------------------------------------------------------------------------+
|  Every catalog record's author field POINTS to this authorized form.      |
|  Change it once here; every record that references it stays consistent.   |
+---------------------------------------------------------------------------+
```

This is the foreign-key-to-a-canonical-row pattern. Catalog records do not store
the author string redundantly; they reference the authority record, so a single
update propagates and search retrieves all of an author's work under one heading
regardless of how a given book printed the name. The shared international service
is **VIAF** (Virtual International Authority File), which links national libraries'
authority records for the same person — entity resolution across organizations.

---

## LCSH — Library of Congress Subject Headings

LCSH is the dominant subject vocabulary in the English-speaking world: a controlled
list of subject headings maintained by the Library of Congress, attached to catalog
records (MARC field 650) so that everything about a topic files under one heading.

Two features make LCSH more than a flat list:

```
+---------------------------------------------------------------------------+
|  LCSH FEATURE 1: SUBDIVISIONS (a heading is a string you build)           |
+---------------------------------------------------------------------------+
|   World War, 1939-1945 -- Campaigns -- France -- Normandy                 |
|   |                       |            |         |                        |
|   topic                   topical sub  geo sub   geo sub                  |
|                                                                           |
|   Subdivision types: --topical  --geographic  --chronological  --form     |
+---------------------------------------------------------------------------+
```

This subdivided string is **pre-coordination** (covered in depth in file 04): the
compound subject is assembled by the cataloger *before* search time, in a fixed
order. It is, again, Ranganathan's faceting (topic + place + time + form) flattened
into one ordered heading string.

```
+----------------------------------------------------------------------------+
|  LCSH FEATURE 2: THE REFERENCE STRUCTURE (relationships)                   |
+----------------------------------------------------------------------------+
|   Authorized heading:   Cooking                                            |
|     UF  Cookery            (Use For -- "Cookery" is a non-preferred term)  |
|     BT  Food preparation   (Broader Term -- the parent)                    |
|     NT  Baking             (Narrower Term -- a child)                      |
|     RT  Gastronomy         (Related Term -- associative, not hierarchical) |
|     SN  ...                (Scope Note -- how to apply the term)           |
+----------------------------------------------------------------------------+
```

Those abbreviations — UF, BT, NT, RT, SN — are the standard relationship types of a
thesaurus, which brings us to the formal standard.

---

## The Thesaurus and ISO 25964

A **thesaurus** is a controlled vocabulary with a defined set of semantic
relationships. The international standard is **ISO 25964** ("Thesauri and
interoperability with other vocabularies," Part 1: 2011, Part 2: 2013), which
superseded the older ISO 2788 and ISO 5964. It codifies exactly three relationship
types plus the synonym-control and scope mechanisms:

```
+----------------------------------------------------------------------------+
|  THE THREE THESAURUS RELATIONSHIPS (ISO 25964)                             |
+----------------------------------------------------------------------------+
|                                                                            |
|   1. EQUIVALENCE   USE / UF      synonym control                           |
|      "automobiles" USE "cars"    one preferred term per concept            |
|                                                                            |
|   2. HIERARCHICAL  BT / NT       generic, partitive, or instance           |
|      vehicles (BT) -> cars (NT)  parent/child (the "is-a" / "part-of")     |
|                                                                            |
|   3. ASSOCIATIVE   RT            related but not hierarchical              |
|      cars  RT  traffic           "see also," a non-tree cross-link         |
+----------------------------------------------------------------------------+
```

The associative (RT) relationship is what makes a thesaurus a **graph, not a
tree**: BT/NT form a hierarchy, but RT edges cross branches arbitrarily. ISO 25964
Part 2 specifically addresses *interoperability* — mapping one thesaurus's terms to
another's (exact match, broader/narrower match, related match), which is schema
mapping / ontology alignment by another name.

```
   OLD WORLD -> here
   USE/UF      ==  an alias / synonym table mapping variants to a canonical key
   BT/NT       ==  a self-referencing parent_id hierarchy (an enum tree)
   RT          ==  a many-to-many "related" join table (arbitrary cross-links)
   the whole    ==  a typed property graph over concepts
```

---

## Taxonomy vs. Ontology — The Critical Distinction

These two words are used loosely in industry; LIS keeps them precise.

| | Taxonomy | Ontology |
|---|---|---|
| Structure | Hierarchy (mostly is-a) | Classes + arbitrary typed relations |
| Relationships | Broader/narrower | Any number of named, typed properties |
| Formality | Human-readable labels | Machine-reasonable logic (OWL/RDF) |
| Inference | None | A reasoner can derive new facts |
| Example | A product category tree | Schema.org, Gene Ontology, Wikidata |
| CS analogy | An enum with a parent FK | A typed schema with constraints + a solver |

```
   TAXONOMY (one relationship: is-a)        ONTOLOGY (many typed relations)

       Animal                                Person --worksFor--> Organization
        |  is-a                                |                       |
       Mammal                                  | bornIn                | locatedIn
        |  is-a                                v                       v
       Dog                                    City  ----partOf---->  Country

   A pure tree of categories.               A graph with NAMED, TYPED edges and
   You can only ask "what is X under?"      axioms a reasoner can chain over.
```

The practical line: a taxonomy lets you *navigate*; an ontology lets you *reason*.
If you state `worksFor` is transitive and that an Organization `locatedIn` a Country,
a reasoner can infer a Person's country from their employer. Taxonomies cannot infer
anything — they only classify. This maps onto the difference between a simple
category enum and a full type system with relations and a constraint solver.

The encoding standard that lets a thesaurus live on the web as data is **SKOS**
(Simple Knowledge Organization System), a W3C RDF vocabulary that expresses exactly
the thesaurus relationships — `skos:broader`, `skos:narrower`, `skos:related`,
`skos:prefLabel`, `skos:altLabel` — so LCSH, MeSH, and the Getty vocabularies all
publish as linked data (file 08). SKOS is the bridge from the human thesaurus to the
machine ontology.

---

## Controlled Vocabulary as Type System (the bridge)

This file's organizing claim, made explicit:

```
+----------------------------------------------------------------------------+
|  CONTROLLED VOCABULARY  ==  TYPE SYSTEM FOR SUBJECT TERMS                  |
+----------------------------------------------------------------------------+
|                                                                            |
|   free-text subject       ~  stringly-typed field (any value, no checks)   |
|   controlled list         ~  enum (closed set of legal values)             |
|   authority record        ~  canonical instance / interned symbol          |
|   USE / UF synonym         ~  type alias (two names, one type)             |
|   BT / NT hierarchy        ~  subtype / supertype relation                 |
|   RT associative           ~  a related-type reference (non-subtype)       |
|   scope note (SN)          ~  documentation / contract on the term         |
|   ontology + reasoner      ~  type system with inference (typeclasses,     |
|                              constraint solving)                           |
|                                                                            |
|   "uncontrolled keyword"  ~  a magic string; works until it doesn't        |
+----------------------------------------------------------------------------+
```

A cataloger assigning a term from LCSH is doing what a compiler does checking a
value against an enum: rejecting the illegal, interning the legal to a canonical
symbol, and recording its place in the type hierarchy. Folksonomies (free user
tags, like a social bookmarking site) are the dynamically-typed counterpart —
flexible, emergent, and prone to the exact synonym/homonym sprawl that controlled
vocabularies exist to prevent.

---

## Decision Cheat Sheet

| Situation | Use |
|---|---|
| One canonical form for a name with many variants | Authority control / VIAF |
| English-language general subject headings | LCSH |
| Medical/biomedical subject indexing | MeSH (a thesaurus) |
| Education research indexing | ERIC Thesaurus |
| Art & architecture terms | Getty AAT (a thesaurus) |
| Build a structured term list with relationships | Thesaurus per ISO 25964 |
| Need only a parent/child category tree | Taxonomy |
| Need machine inference over concepts | Ontology (OWL/RDF) |
| Publish a vocabulary as linked data | SKOS |
| Let users tag freely, accept the sprawl | Folksonomy (uncontrolled) |

---

## Common Confusion Points

### "Taxonomy vs. ontology — people use them interchangeably"

They should not. A taxonomy is a hierarchy with one relationship type (broader/
narrower) — you can navigate but not infer. An ontology has many named, typed
relationships and supports machine inference. Taxonomy = enum with a parent FK;
ontology = typed schema with a reasoner. If a system *derives* new facts, it is an
ontology; if it only *classifies*, it is a taxonomy.

### "Why not just let people search full text — why control the vocabulary?"

Because synonyms scatter a concept across terms (car/automobile/motorcar) and
homonyms collapse distinct concepts under one string (mercury the metal / the
planet / the god). Free text trades recall and precision for convenience.
Controlled vocabularies are the cost you pay up front to get reliable retrieval —
the same trade as static typing: more discipline now, fewer surprises later.

### "LCSH vs. classification — both organize by subject, right?"

Different jobs. Classification (file 01) gives an item *one* call number — a single
shelf location. Subject headings give an item *many* access points — all the topics
it is about. One place to stand, many ways to be found. They are complementary, not
redundant.

### "Is a thesaurus just a synonym list?"

No — that is only its equivalence (USE/UF) layer. A thesaurus per ISO 25964 also
encodes hierarchy (BT/NT) and associative (RT) relationships, making it a typed
graph of concepts. A plain synonym list is just the alias table without the
hierarchy or the cross-links.

### "Where does this connect to vector search and embeddings?"

It is the symbolic ancestor. Controlled vocabularies resolve synonymy and homonymy
*explicitly* via human-curated relationships; embedding models (see
`ai-engineering/`) resolve them *statistically* by placing similar meanings near
each other in vector space. Same problem — sameness of meaning — solved by a curated
type system here versus a learned geometry there.
