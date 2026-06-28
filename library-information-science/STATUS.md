# library-information-science/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | The LIS landscape; Ranganathan's Five Laws; organize→describe→retrieve pipeline | ✅ |
| 01-CLASSIFICATION.md | Dewey Decimal, Library of Congress, UDC, Colon/faceted classification | ✅ |
| 02-CATALOGING-AND-METADATA.md | MARC 21, AACR2→RDA, FRBR, BIBFRAME, Dublin Core | ✅ |
| 03-CONTROLLED-VOCABULARIES.md | LCSH, thesauri, taxonomies, ontologies; bridge to type systems | ✅ |
| 04-INDEXING-AND-ABSTRACTING.md | Subject indexing, pre/post-coordination, abstracting | ✅ |
| 05-INFORMATION-RETRIEVAL.md | Boolean vs ranked, precision/recall, relevance; bridge to search engines | ✅ |
| 06-ARCHIVES-AND-PRESERVATION.md | Provenance, original order, digital preservation, OAIS | ✅ |
| 07-COLLECTION-MANAGEMENT.md | Acquisition, deselection, scholarly communication, open access | ✅ |
| 08-DIGITAL-LIBRARIES.md | Repositories, linked data, persistent identifiers (DOI/ARK) | ✅ |
| 09-INFORMATION-LITERACY.md | Search skills, source evaluation, ethics/economics of information | ✅ |

## Coverage Notes

Library & information science is the discipline of **organizing, describing, and
retrieving recorded knowledge**. It is, at heart, a set of data-modeling problems
solved a century before the database: classification is a tree/ontology design
problem, controlled vocabularies are type systems for subject terms, MARC is a
schema, FRBR is an entity-relationship model, and retrieval is ranking under a
relevance measure. This directory treats LIS as the intellectual ancestor of the
modern data stack rather than as a clerical craft.

The spine runs left to right across the information lifecycle: **classify** (01)
→ **describe/catalog** (02) → **control the vocabulary** (03) → **index for
subjects** (04) → **retrieve** (05), with three orthogonal concerns layered on
top — **preserve** the record over time (06), **manage** the collection as an
economic asset (07), and **carry the whole apparatus onto the network** as
digital libraries and linked data (08). The capstone (09) is information literacy:
the user-facing skill of finding and judging information, plus the ethics and
economics that govern who can access it.

Cross-references are deliberate and non-duplicating. `database-systems/` owns
B-trees, the buffer pool, and MVCC; this directory borrows its index vocabulary
but does not re-teach storage engines. `query-languages/` owns SQL and SPARQL
syntax; here SPARQL appears only as the query layer over linked-data catalogs.
`ai-engineering/` owns vector databases and embedding retrieval; this directory
covers the Boolean/TF-IDF/BM25 lineage those systems descend from and stops at
the embedding boundary. `linguistics/` owns morphology and semantics; controlled
vocabularies borrow its sense/reference distinction. `epigraphy/` owns the
material study of inscriptions; archives here govern how such records are kept.
