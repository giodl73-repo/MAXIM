---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-INDEXING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:indexing
kind: guide
module: database-systems
section: computing-software
title: Indexing - B+tree, Hash, Covering, Composite, Bitmap, Inverted
status: source-custody
source_custody: partial
current_path: database-systems/02-INDEXING.md
canonical_path: database-systems/02-INDEXING.md
backsource_ids: [mdloom-backfill:database-systems:02-indexing, git-history:database-systems:02-indexing]
concepts: [index, b+tree index, hash index, covering index, composite index, bitmap index, inverted index, index selection]
root_concepts: [index]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Indexing — Data Structures That Avoid the Scan

An index is a **secondary data structure** that lets the engine find rows without scanning the
whole table. Indexing is the single biggest lever on read performance — and the most common
place real systems go wrong, because an index that the optimizer can't or won't use is pure
write-time cost with zero read-time benefit.

```
+=====================================================================================+
|                              THE INDEX LANDSCAPE                                     |
+=====================================================================================+
|                                                                                     |
|                          What access pattern are you serving?                       |
|                                                                                     |
|   EQUALITY +     |   EQUALITY      |   LOW-CARDINALITY  |   FULL-TEXT /              |
|   RANGE + SORT   |   ONLY          |   ANALYTICS        |   MULTI-VALUE              |
|        |         |        |        |        |           |        |                  |
|        v         |        v        |        v           |        v                  |
|   +----------+   |   +----------+  |   +-----------+    |   +-----------+            |
|   |  B+TREE  |   |   |  HASH    |  |   |  BITMAP   |    |   | INVERTED  |            |
|   +----------+   |   +----------+  |   +-----------+    |   +-----------+            |
|   point + range  |   O(1) point,   |   one bitmap per   |   term -> list of         |
|   + ORDER BY +    |   NO range,     |   distinct value;  |   doc/row ids;            |
|   prefix scans   |   NO sort       |   AND/OR by bitwise|   text search, arrays,    |
|                  |                 |   ops; OLAP/DW     |   JSON, GIN (Postgres)     |
|   The default.   |   In-memory     |   Oracle/columnar  |                           |
|   95% of indexes |   engines, hash |   warehouses       |   Lucene/Elasticsearch    |
|   you create.    |   joins (g.03)  |                    |   are inverted indexes    |
|   +----------+                                                                       |
+=====================================================================================+
        |
        |  Orthogonal modifiers you layer ON TOP of the above:
        v
   COMPOSITE (multi-column, order matters) | COVERING (includes all needed columns)
   PARTIAL/FILTERED (index only some rows)  | UNIQUE (also a constraint)
```

**Read it as: pick the base structure by access pattern, then apply modifiers.** Most of the
art is in B+tree composite/covering design; the exotic structures (bitmap, inverted) solve
specific shapes.

---

## The B+tree Index — the default, and why

Structurally identical to the B+tree storage of guide 01: routing keys in internal nodes, data
at linked leaves. The difference is what the leaf holds.

```
   CLUSTERED INDEX               NON-CLUSTERED (SECONDARY) INDEX
   ----------------              -------------------------------
   leaf = the actual ROW         leaf = index key + a POINTER to the row
   (the table IS the tree)       pointer is either:
                                   (a) the primary key  (InnoDB, SQL Server clustered table)
   InnoDB: always on PK            (b) a physical RID/ctid (SQL Server heap, Postgres)
   SQL Server: optional, one
   per table                     => secondary lookup may need a SECOND descent ("bookmark
   Postgres: no clustered          lookup" / "key lookup") to fetch non-indexed columns.
   index concept; tables are
   heaps, all indexes secondary
```

This is the crux of two universal phenomena:

- **The bookmark/key lookup.** A non-clustered index finds matching keys fast, but if your
  query needs columns *not in the index*, the engine does a second random I/O per row to fetch
  the full row. Past a few percent of the table, the optimizer abandons the index and just
  scans (the "tipping point").
- **Why InnoDB secondary indexes store the PK:** because the table is clustered on the PK, a
  secondary index can't store a physical pointer (rows move on page splits), so it stores the
  PK and does a second B+tree descent into the clustered index. A fat PK therefore bloats every
  secondary index.

| Operation | B+tree cost | Notes |
|-----------|-------------|-------|
| Point lookup `WHERE k = ?` | O(log_b n) | One descent |
| Range `WHERE k BETWEEN a AND b` | O(log_b n) + scan of matching leaves | Sequential via leaf links |
| `ORDER BY k` | Free if scanning the index | Index is already sorted |
| Prefix of composite `(a,b,c)` on `a` or `a,b` | Usable | Leftmost-prefix rule (below) |
| `WHERE b = ?` on index `(a,b)` | NOT usable as a seek | No leading column → scan |

---

## Composite Indexes — order is everything

A composite (multi-column) index sorts rows by the columns **in order**: first by col1, ties
broken by col2, then col3. This is exactly a phone book sorted by (last name, first name).

```
   INDEX ON (last_name, first_name, city)

   sorted as:  Adams, Ada,   Boston
               Adams, Ben,   Reno
               Adams, Ben,   Tulsa
               Brown, Cleo,  Miami
               ...

   LEFTMOST-PREFIX RULE — the index can SEEK on a prefix of the key columns:

   WHERE last_name = 'Adams'                              -> SEEK (uses col1)
   WHERE last_name = 'Adams' AND first_name = 'Ben'       -> SEEK (uses col1,col2)
   WHERE last_name = 'Adams' AND first_name='Ben'
         AND city = 'Tulsa'                               -> SEEK (full key)
   WHERE first_name = 'Ben'                               -> NO SEEK (col1 missing) -> scan
   WHERE last_name = 'Adams' AND city = 'Tulsa'           -> SEEK on col1, then FILTER city
                                                              (col2 gap breaks the seek on city)
```

Design rule: put **equality predicates first, then the range/sort column last**. An index on
`(status, created_at)` serves `WHERE status='open' ORDER BY created_at` perfectly; the reverse
order does not. This single principle resolves most "why isn't my index used" tickets.

---

## Covering Indexes — answer the query from the index alone

A **covering index** includes every column the query touches, so the engine never visits the
base table — no bookmark lookup, no second random I/O.

```
   QUERY:  SELECT order_id, total FROM orders WHERE customer_id = 42;

   Plain index on (customer_id):
       seek customer_id=42  ->  for each match, KEY LOOKUP into table for order_id,total
                                (random I/O per row)

   Covering index on (customer_id) INCLUDE (order_id, total):
       seek customer_id=42  ->  order_id,total are AT THE LEAF  ->  DONE. No table access.
```

| Mechanism | Where the extra columns go | Engines |
|-----------|----------------------------|---------|
| `INCLUDE` clause | Stored at the leaf, NOT in the key (no sort cost) | SQL Server, Postgres (`INCLUDE`) |
| Append to the key | Part of the sort key (wider, but enables prefix seeks) | Any engine; cruder |

> Bridge: SQL Server's `CREATE INDEX ... INCLUDE (col)` and Postgres 11+'s `INCLUDE` are the
> same idea — non-key payload columns at the leaf. A covering index is the single most reliable
> fix for a hot read query, at the cost of a wider index and slower writes.

---

## Hash Indexes — O(1) equality, no range

A hash index maps `hash(key) -> bucket -> row pointer`. Lookups are O(1) average, but the hash
**destroys order**, so:

```
   WHERE k = 42        ->  O(1)  great
   WHERE k > 42        ->  USELESS (hash has no order)  -> falls back to scan
   ORDER BY k          ->  USELESS
```

Where hash indexes actually appear:

- **In-memory engines** where the whole index is RAM-resident (SQL Server In-Memory OLTP /
  Hekaton hash indexes; Redis is essentially a giant hash table — see `query-languages/11-REDIS`).
- **Hash joins** (guide 03) build a transient in-memory hash table — the same structure, used
  per-query rather than persisted.
- Postgres has hash indexes but B+tree is almost always preferred because it also serves ranges
  and is well-optimized.

The trade is stark: a hash index does *one* thing (equality) maximally fast and *nothing* else.
A B+tree does equality slightly slower but also ranges and sorts. Default to B+tree.

---

## Bitmap Indexes — low cardinality, analytic AND/OR

A bitmap index stores, for each distinct value, a **bit vector** with one bit per row: 1 if the
row has that value. Predicates become bitwise operations.

```
   COLUMN region (4 distinct values), 8 rows:

   row:        r1 r2 r3 r4 r5 r6 r7 r8
   region=NA:   1  0  0  1  0  0  1  0
   region=EU:   0  1  0  0  1  0  0  0
   region=APAC: 0  0  1  0  0  1  0  1
   region=LATAM:0  0  0  0  0  0  0  0   ... etc

   QUERY: WHERE region='NA' OR region='EU'
        =>  NA_bitmap OR EU_bitmap  =  1 1 0 1 1 0 1 0   (one bitwise OR, blazing fast)

   QUERY: WHERE region='NA' AND status='paid'
        =>  NA_bitmap AND paid_bitmap   (bitwise AND across two bitmap indexes)
```

| Good for | Bad for |
|----------|---------|
| **Low-cardinality** columns (region, status, flags) | High-cardinality columns (a million distinct values → a million sparse bitmaps) |
| Data warehouse / OLAP, mostly read-only | OLTP with frequent updates (updating one row flips bits across many bitmaps → contention) |
| Combining many predicates with AND/OR | Point inserts/updates |

Bitmaps are an OLAP/data-warehouse structure (Oracle has explicit bitmap indexes; columnar
engines and `data-science/` analytic stores build bitmap-like structures internally). They are
*not* an OLTP tool — bitmap maintenance under concurrent writes locks too coarsely.

---

## Inverted Indexes — full-text and multi-value

An inverted index maps **each term → the list of documents/rows containing it** (a *postings
list*). It is the structure behind every search engine.

```
   DOCUMENTS:                    INVERTED INDEX (term -> postings):
   doc1: "the quick fox"           the   -> [1, 2]
   doc2: "the lazy dog"            quick -> [1]
   doc3: "quick brown fox"         fox   -> [1, 3]
                                   lazy  -> [2]
                                   dog   -> [2]
                                   brown -> [3]

   QUERY: "quick fox"
       postings(quick)=[1,3]  INTERSECT  postings(fox)=[1,3]  =>  [1,3]
```

Where they appear:

- **Lucene / Elasticsearch / OpenSearch / Azure AI Search** are inverted indexes plus ranking
  (TF-IDF, BM25). Bridge to `data-science/` for the ranking math.
- **Postgres GIN** (Generalized Inverted Index) indexes arrays, `jsonb`, and full-text
  (`tsvector`) — the same term→rows postings idea generalized.
- The DB-internal version of the inverted index underlies `LIKE '%term%'`-style search done
  *properly* (a B+tree can't seek a leading wildcard; an inverted/trigram index can).

---

## Index Selection — the engine's decision and yours

The optimizer (guide 03) chooses whether to use an index based on **estimated selectivity** from
**statistics** (histograms of value distribution). Your job is to provide an index whose shape
matches the query's access pattern.

```
                       +-----------------------------------+
                       |  Query has WHERE / JOIN / ORDER BY |
                       +-----------------------------------+
                                       |
              equality only? --YES--> hash (if in-mem) or B+tree
                   | NO
              range or sort? --YES--> B+tree, range/sort column LAST in a composite
                   | NO
              low-cardinality analytic AND/OR? --YES--> bitmap (DW only)
                   | NO
              text / array / json membership? --YES--> inverted / GIN
                   |
              does the query read few extra columns? --YES--> add them as INCLUDE (covering)
```

The estimated **selectivity** decides usage:

| Selectivity (fraction of rows matched) | Optimizer choice |
|----------------------------------------|------------------|
| Very low (e.g. < ~1–5%) | **Index seek** + lookups — random I/O worth it |
| High (e.g. > ~20–30%, varies) | **Table/index scan** — sequential I/O beats many random lookups |
| In between | Cost-based; depends on row width, clustering, cached state |

This "tipping point" is why an index on a column where 90% of rows are `status='active'` is
useless for `WHERE status='active'` — too many matches, the scan wins. It *is* useful for
`WHERE status='cancelled'` if that's rare. Selectivity, not the column, decides.

---

## Old World → New World Bridges

| You already know | Index concept | SQL Server / Azure anchor |
|------------------|---------------|----------------------------|
| A `Dictionary<K,V>` (hash map) | **Hash index** — O(1) equality, no ordering | In-Memory OLTP hash index; Redis |
| A `SortedDictionary` / balanced tree | **B+tree index** — ordered, range + sort | The default clustered/nonclustered index |
| Phone book sorted by (last, first) | **Composite index**, leftmost-prefix rule | Multi-column index column order |
| A column-store you only filter, never seek | **Bitmap** index for low-cardinality OLAP | Columnstore index (related idea) |
| A search engine over your text | **Inverted index** (term→docs) | Azure AI Search, Postgres GIN, Lucene |
| Including extra columns to avoid a join back | **Covering index** (`INCLUDE`) | `CREATE INDEX ... INCLUDE (...)` |
| Filtering an index to active rows only | **Partial / filtered index** | `CREATE INDEX ... WHERE is_active` |

---

## Decision Cheat Sheet

| I want to... | Use |
|--------------|-----|
| Speed up `WHERE k = ?` and `WHERE k BETWEEN ...` | **B+tree** on `k` |
| Speed up `WHERE a=? AND b=? ORDER BY c` | **Composite** B+tree `(a, b, c)` — equality then sort |
| Avoid a key lookup on a hot read query | **Covering** index — `INCLUDE` the SELECTed columns |
| Index only the small set of "active" rows | **Partial / filtered** index with a `WHERE` |
| Fast equality in an in-memory table, no ranges | **Hash** index |
| OLAP AND/OR over status/region/flag columns | **Bitmap** index (data warehouse only) |
| Full-text search, JSON/array containment | **Inverted** index (GIN / Lucene / Azure AI Search) |
| Enforce uniqueness AND get the lookup | **Unique** B+tree index (constraint + index in one) |
| Fix "index not used" | Match index column order to the predicate; check selectivity & statistics |

---

## Common Confusion Points

### "I added an index but the query got slower"

Every index is a **write tax**: each `INSERT`/`UPDATE`/`DELETE` must maintain it. An index used
by *no* query is pure overhead. And on writes, more indexes = more pages to lock and log. Drop
indexes nothing reads.

### "I have indexes on a, b, and c separately but the AND query is slow"

Three single-column indexes ≠ one composite index. The engine can sometimes *intersect* them
(bitmap-style index merge) but a single composite `(a, b, c)` matching the predicate is almost
always faster. Single-column indexes on `a`, `b`, `c` cannot seek `WHERE a=? AND b=? AND c=?`
the way `(a,b,c)` can.

### "The optimizer ignores my perfectly good index"

Two usual causes: (1) **selectivity** — the predicate matches too many rows, so a scan is
genuinely cheaper; (2) **non-sargable** predicates — wrapping the column in a function
(`WHERE YEAR(d) = 2026`, `WHERE col + 0 = 5`, implicit type conversion) defeats the seek
because the index is on `col`, not `f(col)`. Rewrite to `WHERE d >= '2026-01-01' AND d < '2027-01-01'`.

### "Leading wildcard search should use my index"

`WHERE name LIKE '%smith'` cannot use a B+tree — the tree is sorted left-to-right and a leading
`%` provides no prefix to seek. `LIKE 'smith%'` *can* (it's a prefix range). Leading-wildcard
and substring search need an **inverted/trigram** index, not a B+tree.

### "More columns in the index is always more covering"

Wider indexes cost more to store and maintain and fit fewer entries per page (shallower fan-out,
more I/O). Cover exactly what the hot query needs via `INCLUDE` — don't index every column "just
in case."
