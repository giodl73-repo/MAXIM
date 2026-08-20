---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:overview
kind: guide
module: library-information-science
section: language-communication
title: Library and Information Science - The Landscape
status: source-custody
source_custody: partial
current_path: library-information-science/00-OVERVIEW.md
canonical_path: library-information-science/00-OVERVIEW.md
backsource_ids: [proof-backfill:library-information-science:00-overview, git-history:library-information-science:00-overview]
concepts: [library science, information science, Ranganathan Five Laws, classification, cataloging, controlled vocabulary, information retrieval, bibliographic control]
root_concepts: [library and information science]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Library & Information Science — The Landscape

Library & information science (LIS) is the discipline of **organizing, describing,
and retrieving recorded knowledge**. Strip away the wood-panelled connotations and
it is a stack of data-modeling problems solved decades before the relational
database existed: a classification scheme is an ontology, a controlled vocabulary
is a type system for subjects, a MARC record is a schema instance, FRBR is an
entity-relationship model, and retrieval is ranking under a relevance measure.

The whole field is one pipeline. Knowledge arrives as an undifferentiated pile of
documents; LIS turns it into a system you can query. Read this diagram left to
right — it is the spine of every file in this directory.

```
+======================================================================================+
|                THE INFORMATION LIFECYCLE  (organize -> describe -> retrieve)         |
+======================================================================================+
|                                                                                      |
|   .-----------.   .-----------.   .-----------.   .-----------.   .-----------.      |
|   | CLASSIFY  |-->| DESCRIBE  |-->|  CONTROL  |-->|   INDEX   |-->| RETRIEVE  |      |
|   |   (01)    |   |   (02)    |   |   (03)    |   |   (04)    |   |   (05)    |      |
|   | where on  |   | who/what/ |   | which     |   | subject   |   | query +   |      |
|   | the shelf |   | when meta |   | words are |   | access    |   | rank by   |      |
|   | (the tree)|   | (a schema)|   | canonical |   | points    |   | relevance |      |
|   '-----------'   '-----------'   '-----------'   '-----------'   '-----------'      |
|        |                |               |               |               |            |
|        | Dewey/LC/UDC   | MARC/RDA      | LCSH/         | pre- vs       | Boolean/   |
|        | Colon          | FRBR/         | thesauri/     | post-         | TF-IDF/    |
|        | (faceted)      | BIBFRAME/DC   | ontologies    | coordination  | BM25       |
|        '----------------'---------------'---------------'---------------'            |
|                                       |                                              |
|        ORTHOGONAL CONCERNS that wrap the whole pipeline:                             |
|        .------------------.  .------------------.  .------------------.              |
|        | PRESERVE  (06)   |  | MANAGE   (07)    |  | NETWORK  (08)    |              |
|        | archives, OAIS,  |  | acquisition,     |  | digital libs,    |              |
|        | digital pres.    |  | open access      |  | linked data, DOI |              |
|        '------------------'  '------------------'  '------------------'              |
|                                       |                                              |
|        .--------------------------------------------------------------.              |
|        | LITERACY (09): the user finds, evaluates, and acts ethically |              |
|        '--------------------------------------------------------------'              |
+======================================================================================+
```

**Library science** historically meant the institutional craft (run a library).
**Information science** emerged mid-20th century as the formal study of how
information is represented, stored, and retrieved — closer to a quantitative,
algorithmic discipline. The two fused into LIS. The split still matters: the
left of the diagram is library-science heritage, the retrieval engine on the
right is information-science heritage.

---

## Ranganathan's Five Laws — The Field's Axioms

S. R. Ranganathan, an Indian mathematician-turned-librarian, published the *Five
Laws of Library Science* in 1931. Treat them the way you would treat the axioms of
a design discipline: terse, deceptively simple, and generative of everything that
follows. He was a mathematician; the laws are stated like a small axiom set, and
the whole field can be derived from them.

```
+-----------------------------------------------------------------------------+
|  RANGANATHAN'S FIVE LAWS (1931)                                             |
+-----------------------------------------------------------------------------+
|  1. Books are for use.            -> access beats preservation-as-hoarding. |
|  2. Every reader his/her book.    -> coverage: serve every user's need.     |
|  3. Every book its reader.        -> findability: each item must surface.   |
|  4. Save the time of the reader.  -> efficiency: latency is a design goal.  |
|  5. The library is a growing      -> the system must scale and evolve.      |
|     organism.                                                               |
+-----------------------------------------------------------------------------+
```

These read like the design principles of a modern search system. "Save the time
of the reader" is a latency SLA. "Every book its reader" is recall. "Every reader
his book" is coverage. "A growing organism" is a scalability and schema-evolution
requirement. Ranganathan also invented **faceted (analytico-synthetic)
classification** — the idea that a subject is a *composition* of independent
facets rather than a single point in a fixed tree, which is exactly multi-axis
tagging and the relational decomposition you would reach for today.

---

## The Two Mental Models: Tree vs. Facet

Every classification and description decision in LIS is a fight between two data
structures you already know.

```
   ENUMERATIVE (a tree)                  FACETED (a composition / cross-product)

   Pre-built hierarchy. Every            Independent axes. Build the class
   class is a node already in the        on demand by combining facet values.
   tree. You walk down to a leaf.

        ROOT                             SUBJECT  x  PLACE  x  TIME  x  FORM
       /    \                            -------     -----     ----     ----
   Science  History                      Cooking     India     1900s    Manual
    /  \      /  \                        |           |         |        |
  Bio  Phys Anc  Mod                      '-----> "Indian cooking manuals,
   |                                              early 1900s" (synthesized)
  Leaf = call number

   Dewey, LC are mostly enumerative.     Colon Classification, UDC's auxiliaries,
   Pick the nearest existing node.       and every modern tag system are faceted.
```

A senior engineer will recognize this immediately: enumerative is a single
fixed-schema table with a category foreign key; faceted is a star schema or a set
of orthogonal tag dimensions you combine at query time. The 20th-century shift in
LIS from enumerative toward faceted thinking is the same shift you lived through
from rigid hierarchies to composable, multi-axis metadata.

---

## The Catalog: From Card to Schema to Graph

The catalog is the database of the library. Its history is a clean schema-evolution
story, and it maps almost one-to-one onto a progression you know.

```
+----------------+   +----------------+   +----------------+   +----------------+
|  CARD CATALOG  |-->|   MARC (1968)  |-->|  FRBR / RDA    |-->| BIBFRAME / LD  |
|  (paper)       |   |  flat record   |   |  entity model  |   |  RDF graph     |
+----------------+   +----------------+   +----------------+   +----------------+
| One physical   |   | A fixed-field  |   | Work/Express./ |   | Triples; URIs  |
| card per entry,|   | binary schema  |   | Manifest./Item |   | for every      |
| filed by rule. |   | for computers. |   | as an ER model.|   | entity. Joins  |
|                |   |                |   |                |   | across the web.|
| = index cards  |   | = a row with   |   | = normalized   |   | = a knowledge  |
|   in a drawer  |   |   tagged fields |   |   ER schema    |   |   graph        |
+----------------+   +----------------+   +----------------+   +----------------+
   1870s-1960s          1968-present         2010s-present       2011-present
```

The card catalog was a denormalized, manually-maintained index. MARC (MAchine-
Readable Cataloging, 1968) was the first move to a machine schema — and like many
first schemas, it baked in the assumptions of its medium (it is essentially a
serialization format for a catalog card). FRBR (1998) finally normalized the
model: it separates the abstract **Work** from its **Expressions**, **Manifest-
ations**, and physical **Items** — the data modeling the flat MARC record never
did. BIBFRAME re-expresses all of this as RDF so the catalog becomes a node in the
web of linked data instead of an island.

---

## Old World → New World Bridges

| LIS concept | Data / CS equivalent | Where it lives |
|-------------|----------------------|----------------|
| Classification scheme | Ontology / class hierarchy | 01 |
| Call number | A sortable primary key encoding category | 01 |
| Faceted classification | Multi-axis tagging / star schema | 01, 03 |
| MARC record | A schema instance (binary serialization) | 02 |
| FRBR Work/Expression/Manifestation/Item | A normalized ER model | 02 |
| BIBFRAME | RDF knowledge graph | 02, 08 |
| Controlled vocabulary | Type system / enum for subject terms | 03 |
| Authority record | A canonical-entity / master-data record | 03 |
| Subject indexing | Inverted index construction (by humans) | 04 |
| Precision / recall | The same metrics, predating IR theory | 05 |
| Persistent identifier (DOI) | A stable, resolvable primary key (vs. a URL) | 08 |
| Provenance / original order | Lineage / immutable audit trail | 06 |

---

## What This Directory Is — and Is Not

```
+---------------------------------------------------------------------------+
|  THIS DIRECTORY (library-information-science/)                            |
|  Organizing, describing, retrieving RECORDED KNOWLEDGE.                   |
|  The human and conceptual systems: schemes, schemas, vocabularies,        |
|  relevance, preservation, access.                                         |
+---------------------------------------------------------------------------+
        |                |                  |                               |
        | borrows from   | borrows from     | borrows from                  |
        v                v                  v                   v
+--------------+ +----------------+ +-----------------+ +------------------ +
| database-    | | query-         | | ai-engineering/ | | linguistics/      |
| systems/     | | languages/     | | (vector DBs,    | | (sense/reference, |
| (B-trees,    | | (SQL, SPARQL   | |  embeddings,    | |  morphology that  |
| MVCC, the    | |  syntax — the  | |  semantic       | |  vocabularies     |
| engine)      | |  query layer)  | |  search)        | |  must handle)     |
+--------------+ +----------------+ +-----------------+ +------------------ +
```

We do **not** re-teach storage engines (that is `database-systems/`), SQL/SPARQL
syntax (`query-languages/`), or embedding-based semantic search (`ai-engineering/`).
We cover the lineage those systems descend from and the human apparatus they
automate.

---

## Decision Cheat Sheet

| I want to understand... | Read |
|---|---|
| The whole field and its axioms | This file |
| How items get a shelf location / how schemes are built | 01-CLASSIFICATION |
| How a record describes an item (MARC, FRBR, Dublin Core) | 02-CATALOGING-AND-METADATA |
| Why subject terms are standardized; LCSH, thesauri | 03-CONTROLLED-VOCABULARIES |
| How subjects become searchable; pre/post-coordination | 04-INDEXING-AND-ABSTRACTING |
| Boolean vs ranked retrieval; precision/recall | 05-INFORMATION-RETRIEVAL |
| Keeping records authentic over time; OAIS | 06-ARCHIVES-AND-PRESERVATION |
| Building/pruning a collection; open access economics | 07-COLLECTION-MANAGEMENT |
| Repositories, linked data, DOIs and ARKs | 08-DIGITAL-LIBRARIES |
| Finding and judging information as a user | 09-INFORMATION-LITERACY |

---

## Common Confusion Points

### "Isn't this all just databases now?"

The storage *is* a database. But LIS owns the layer the database does not model:
which words count as the same subject, what makes one result more relevant than
another to a human need, and how to keep a record trustworthy for a century. A
B-tree does not know that "automobiles" and "cars" are one concept; an authority
file does. The engine is solved; the semantics are the field.

### "Library science vs. information science — same thing?"

Overlapping but not identical. Library science is the institutional craft
(collections, service, the building). Information science is the formal study of
representation, storage, and retrieval — the quantitative, algorithmic half. The
modern degree is "LIS" because the two became inseparable once catalogs became
machine-readable.

### "Classification vs. cataloging — which is which?"

Classification answers *where does it go* (one location, a call number — file 01).
Cataloging answers *how do we describe it* (the metadata record — file 02). An
item is classified once but described with many access points. Think: partitioning
key vs. the full row.

### "Why Ranganathan? He was a librarian from 1931."

He was a mathematician first, and the Five Laws plus faceted classification are a
small, generative axiom set that predicts modern search-system design with eerie
accuracy. Reading him is like reading a design doc for a relevance-ranked,
scalable, multi-axis retrieval system written before the computer existed.
