---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-DIGITAL-LIBRARIES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:digital-libraries
kind: guide
module: library-information-science
section: language-communication
title: Digital Libraries - Repositories, Linked Data, Persistent Identifiers
status: source-custody
source_custody: partial
current_path: library-information-science/08-DIGITAL-LIBRARIES.md
canonical_path: library-information-science/08-DIGITAL-LIBRARIES.md
backsource_ids: [proof-backfill:library-information-science:08-digital, git-history:library-information-science:08-digital]
concepts: [digital libraries, institutional repository, linked data, RDF, SPARQL, persistent identifiers, DOI, ARK, ORCID, OAI-PMH]
root_concepts: [digital library]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Digital Libraries — Knowledge Organization on the Network

A digital library carries the whole apparatus of the preceding files — classify,
describe, control, retrieve, preserve — onto the network. Three things change at that
boundary and define this file: content lives in **repositories**, metadata is exposed
as **linked data** so catalogs join across institutions, and every object needs a
**persistent identifier** because a raw URL is not a stable key. This is the LIS world
re-platformed onto the web's primitives.

```
+======================================================================================+
|                        THE DIGITAL LIBRARY STACK                                     |
+======================================================================================+
|                                                                                      |
|   .-----------------------------------------------------------------.                |
|   | ACCESS LAYER     discovery UI, search (file 05), APIs           |                |
|   '-----------------------------------------------------------------'                |
|                              ^                                                       |
|   .-----------------------------------------------------------------.                |
|   | INTEROP LAYER    LINKED DATA (RDF) + SPARQL  |  OAI-PMH harvest  |               |
|   |                  catalogs join across institutions               |               |
|   '-----------------------------------------------------------------'                |
|                              ^                                                       |
|   .-----------------------------------------------------------------.                |
|   | IDENTITY LAYER   PERSISTENT IDENTIFIERS  DOI / ARK / Handle      |               |
|   |                  ORCID (people)  +  resolver indirection         |               |
|   '-----------------------------------------------------------------'                |
|                              ^                                                       |
|   .-----------------------------------------------------------------.                |
|   | REPOSITORY LAYER  the objects + metadata: DSpace, Fedora, etc.  |                |
|   |                   (an OAIS-conformant store, file 06)            |               |
|   '-----------------------------------------------------------------'                |
+======================================================================================+
```

Read bottom-up: a repository holds objects, each gets a persistent identifier, the
metadata is published as linked data and harvested, and an access layer searches and
serves it. Each layer maps onto infrastructure a senior engineer already runs.

---

## Repositories — The Object Store

A **repository** is a managed store of digital objects with their metadata, access
control, and (ideally) OAIS-conformant preservation (file 06). The dominant kinds:

| Repository type | Holds | Examples |
|---|---|---|
| Institutional repository (IR) | An institution's own output (papers, theses, data) | DSpace, EPrints |
| Disciplinary / preprint | A field's literature | arXiv, bioRxiv, SSRN |
| Data repository | Research datasets | Zenodo, Dryad, Figshare |
| Digital asset / object store | Images, A/V, complex objects | Fedora, Samvera, Islandora |

Functionally an IR is a **self-hosted artifact store with metadata, access policy, and
a retention/preservation guarantee** — the same role an internal package registry or
artifact repository plays for build outputs, applied to scholarship. The collection-
management value-chain move from file 07 (library as *operator of repositories* rather
than mere *buyer of access*) lands here: running an IR is running your own platform
instead of consuming a vendor's.

---

## Persistent Identifiers — Why a URL Is Not a Key

The web's native identifier, the URL, is a *location*. Locations move and die; the
average URL rots within years ("link rot"). A scholarly or cultural record needs an
identifier that is a **stable, resolvable primary key independent of current location**
— a layer of indirection between "what this thing is" and "where it currently lives."

```
+----------------------------------------------------------------------------+
|  URL  (a location -- fragile)                                              |
|     https://uni.edu/repo/2019/papers/file42.pdf                            |
|     |__ breaks when the server, path, or org structure changes             |
+----------------------------------------------------------------------------+
|                                                                            |
|  PERSISTENT IDENTIFIER  (an identity -- stable)                            |
|     doi:10.1000/xyz123                                                     |
|        |                                                                   |
|        | RESOLVER (indirection)                                            |
|        v                                                                   |
|     https://...current-location...   <- the target can change; the         |
|                                          PID stays the same forever        |
+----------------------------------------------------------------------------+
```

This is a level of indirection — a symbolic name resolved through a registry to the
current concrete address, exactly like a DNS name in front of a changing IP, or a
stable artifact coordinate (group:name:version) resolved to whatever URL currently
serves it. The maintainer updates the *target* when the object moves; the identifier
never changes. The major schemes:

| Identifier | For | Resolves via | Governance / note |
|---|---|---|---|
| **DOI** | Articles, datasets, objects | doi.org (built on Handle) | Registries: Crossref, DataCite. The scholarly default. |
| **Handle** | Any digital object | Handle System | The substrate DOIs are built on |
| **ARK** | Any object (incl. physical) | A NAAN + resolver | Decentralized, free, no central authority; cultural heritage favorite |
| **ORCID** | Researchers (people) | orcid.org | Disambiguates author identity (an authority record, file 03, for living scholars) |
| **PURL** | Web resources | A redirect service | Persistent URL via a maintained redirect |

```
   DOI  vs  ARK -- the same idea, different governance models:

   DOI   centralized, registry fees, strong commercial backing, ubiquitous
         in scholarly publishing (Crossref/DataCite). A managed, paid registry.

   ARK   decentralized, free, no central registration authority, designed so any
         institution can mint and resolve its own. Favored by libraries, archives,
         and museums that want no dependency on a paid central registry.

   Choosing between them is a governance/control decision, not a technical one --
   like a managed naming service vs. self-operated naming.
```

**ORCID** deserves its own note: it is authority control (file 03) for *people*,
solving the same disambiguation problem (two researchers named J. Smith; one
researcher who changed institutions and surnames) with a stable identifier instead of
a name string. It is a canonical-entity ID for humans.

---

## Linked Data — The Catalog as a Graph

The interoperability layer. Recall from file 02 that BIBFRAME re-expresses catalog
records as **RDF triples**. Linked data is the principle that those triples should use
**resolvable URIs as identifiers** and **link to each other across institutions**, so
the world's catalogs form one queryable graph rather than millions of islands. This is
the realization of FRBR's entities and file 03's vocabularies as web-native data.

```
+----------------------------------------------------------------------------+
|  THE RDF TRIPLE -- the atom of linked data                                 |
+----------------------------------------------------------------------------+
|                                                                            |
|     SUBJECT  ----  PREDICATE  ---->  OBJECT                                |
|   <work#1>         dc:creator        <person#42>                           |
|   <person#42>      orcid:id          "0000-0002-1825-0097"                 |
|   <person#42>      rdfs:label        "Tolkien, J.R.R."                     |
|                                                                            |
|   URIs (not local IDs) mean <person#42> can be the SAME node another       |
|   institution -- or Wikidata -- references. Joins span the web.            |
+----------------------------------------------------------------------------+
```

```
   The four linked-data principles (Berners-Lee):
   1. Use URIs as names for things.
   2. Use HTTP URIs so they can be looked up.
   3. Return useful RDF when someone looks one up.
   4. Include links to other URIs so they can discover more.

   = a globally-distributed graph database with HTTP as the access protocol
     and URIs as foreign keys that work across organizational boundaries.
```

The query language for this graph is **SPARQL** — pattern-matching over triples, the
graph analog of SQL. The full syntax lives in `query-languages/`; here SPARQL is
simply the read interface to the linked-data catalog. The shared backbone vocabularies
— **Dublin Core** (file 02), **SKOS** (file 03, for thesauri), **FOAF** (people),
**schema.org** (general), and **Wikidata** (a vast open identifier hub) — are the
agreed predicates and entity IDs that make cross-institution joins meaningful. Without
shared vocabularies, two graphs cannot be joined even if both are RDF; the vocabulary
is the shared schema.

---

## Metadata Harvesting — OAI-PMH

How do millions of repositories become collectively searchable without one giant
central database? **OAI-PMH** (Open Archives Initiative Protocol for Metadata
Harvesting) lets a service provider *pull* (harvest) metadata records from many
repositories on a schedule, aggregate them, and offer unified search.

```
   .-----------.   harvest    .-----------.   harvest   .--------------------.
   | Repo A    |<------------ | AGGREGATOR | ----------->| Repo B, C, D, ...  |
   | (exposes  |   (OAI-PMH)  | (e.g.      |  (OAI-PMH)  | each exposes        |
   |  Dublin   |              |  BASE,     |             | Dublin Core via     |
   |  Core)    | ------------>|  CORE)     |<----------- | the same protocol   |
   '-----------'   records    '-----------'   records    '--------------------'
                                   |
                                   v
                       one unified search index over all sources
```

The lowest-common-denominator schema OAI-PMH mandates is unqualified **Dublin Core** —
precisely why DC's 15-element minimalism (file 02) matters: a small schema everyone can
produce is what makes federation possible. This is incremental metadata replication via
a pull protocol with a shared minimal schema — the pattern behind any feed-aggregation
or change-data-capture pipeline that unifies heterogeneous sources.

---

## Old World → New World

| Digital-library concept | Infrastructure equivalent |
|---|---|
| Institutional repository | Self-hosted artifact/package registry |
| Persistent identifier (DOI/ARK) | Stable coordinate resolved through a registry |
| Resolver indirection | DNS-style name -> current address indirection |
| ORCID | Canonical entity ID for a person |
| RDF triple store | Graph database |
| Linked-data URIs | Foreign keys that work across organizations |
| SPARQL | Graph query language (see `query-languages/`) |
| Shared vocabularies (DC/SKOS/schema.org) | Agreed schema enabling joins |
| OAI-PMH harvesting | Pull-based replication / feed aggregation / CDC |

---

## Decision Cheat Sheet

| Need | Use |
|---|---|
| Host an institution's scholarly output | Institutional repository (DSpace/Fedora) |
| Share a research dataset citably | Data repository (Zenodo) + a DOI |
| A stable citation for an article/dataset | DOI (Crossref / DataCite) |
| Identifiers with no central authority / free | ARK |
| Disambiguate a researcher across name changes | ORCID |
| Publish catalog metadata for cross-institution joins | Linked data (RDF) + shared vocabularies |
| Query a linked-data catalog | SPARQL (`query-languages/`) |
| Make a repository's metadata harvestable | Expose OAI-PMH (unqualified Dublin Core) |
| Build a union catalog over many repositories | Harvest via OAI-PMH into one index |

---

## Common Confusion Points

### "Why not just use a URL — why DOIs and ARKs?"

A URL is a *location*, and locations rot: servers move, orgs restructure, paths change,
and the link dies. A persistent identifier is an *identity* resolved through a registry
to the current location, so the citation stays valid even as the object moves. It is
the same reason you put a stable name in front of a changing address — a DNS name over
an IP, an artifact coordinate over a download URL. The indirection is the whole point.

### "DOI vs. ARK — which should I use?"

A governance choice, not a technical one. DOIs are centralized, ubiquitous in
scholarly publishing, and carry registry fees and commercial backing (Crossref,
DataCite). ARKs are decentralized, free, and require no central registration authority,
so an institution controls its own minting and resolution — favored by libraries,
archives, and museums that want no paid central dependency. Both deliver stable,
resolvable identifiers.

### "Linked data vs. just having an API?"

An API exposes *your* data in *your* schema; linked data exposes data as a graph using
*shared* URIs and *shared* vocabularies so it joins with everyone else's. The
difference is global join-ability: with linked data, your author node can be literally
the same node Wikidata and a publisher reference, and a query can traverse across all
of them. It is the difference between a private endpoint and participating in one
distributed graph.

### "Is a digital library just a website with PDFs?"

No — that misses every layer above the files. A digital library adds managed
preservation (OAIS, file 06), persistent identifiers, controlled metadata, linked-data
interoperability, and structured retrieval. A folder of PDFs has none of the identity,
durability, or interoperability guarantees; it is storage, not a library.

### "Where does this stop and ai-engineering/'s vector search begin?"

This file owns the *organizational* network layer — repositories, identifiers, linked
data, harvesting — and the symbolic/lexical retrieval of file 05. Embedding-based
semantic search over digital collections lives in `ai-engineering/`. A modern digital
library increasingly runs both: structured linked-data + BM25 for precision and exact
identifiers, plus vector search for semantic recall, fused at the access layer.
