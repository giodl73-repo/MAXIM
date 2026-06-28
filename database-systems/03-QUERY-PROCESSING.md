---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:query-processing
kind: guide
module: database-systems
section: computing-software
title: Query Processing - Parse, Plan, Optimize, Execute
status: source-custody
source_custody: partial
current_path: database-systems/03-QUERY-PROCESSING.md
canonical_path: database-systems/03-QUERY-PROCESSING.md
backsource_ids: [proof-backfill:database-systems:03-query-processing, git-history:database-systems:03-query-processing]
concepts: [query processing, parser, query optimizer, cost-based optimization, join algorithms, statistics, cardinality estimation, query execution]
root_concepts: [query optimizer]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# Query Processing — From Declarative Text to Physical Plan

SQL is **declarative**: you state *what* you want, not *how* to get it. The query processor's
job is to bridge that gap — turn one query string into an efficient sequence of physical
operations over the storage and index layers below. For an MIT-TCS reader this is a compiler:
front-end (parse/bind), a middle-end optimizer (cost-based, over a huge plan space), and a
back-end executor (the iterator/vectorized runtime).

```
+=====================================================================================+
|                         THE QUERY PROCESSING PIPELINE                               |
+=====================================================================================+
|                                                                                     |
|  SQL TEXT                                                                           |
|  "SELECT c.name, SUM(o.total) FROM customers c JOIN orders o                        |
|   ON c.id=o.cust_id WHERE o.region='EU' GROUP BY c.name"                            |
|        |                                                                            |
|        v   (1) PARSE  — lex + grammar -> abstract syntax tree (AST)                  |
|        v   (2) BIND   — resolve names to tables/columns, type-check, expand *        |
|   +-----------------------------------------------------------------------------+   |
|   |  (3) LOGICAL PLAN  — a tree of relational-algebra operators                   |  |
|   |        sigma (filter region='EU')                                            |  |
|   |          |                                                                   |  |
|   |        join (c.id = o.cust_id)                                               |  |
|   |        /        \                                                            |  |
|   |   scan customers  scan orders                                                |  |
|   +-----------------------------------------------------------------------------+   |
|        |                                                                            |
|        v   (4) OPTIMIZE  — apply REWRITES + enumerate PHYSICAL plans, COST each,     |
|        |                   pick the cheapest. Uses STATISTICS for cardinality.       |
|   +-----------------------------------------------------------------------------+   |
|   |  (5) PHYSICAL PLAN  — concrete algorithms chosen:                             |  |
|   |        HashAggregate                                                          |  |
|   |          |                                                                   |  |
|   |        HashJoin (build on customers, probe with orders)                      |  |
|   |        /            \                                                         |  |
|   |   IndexScan        IndexSeek orders ON (region) [pushed-down filter]          |  |
|   +-----------------------------------------------------------------------------+   |
|        |                                                                            |
|        v   (6) EXECUTE  — iterator (Volcano) or VECTORIZED engine pulls rows         |
|   RESULT ROWS                                                                       |
+=====================================================================================+
```

---

## Stage 1–2: Parse and Bind

```
   PARSE   text -> tokens -> AST.  Pure syntax. Rejects malformed SQL.
   BIND    AST + CATALOG -> resolved tree.
           - resolve "orders" -> table OID, "o.total" -> column + type
           - expand SELECT *  -> explicit column list
           - type-check expressions, resolve overloads, fold constants
           - check permissions
```

Nothing performance-relevant happens yet — this is the front-end. Errors here are "no such
column," "ambiguous name," "type mismatch." Output is a **logical plan** in relational algebra:
selections (σ), projections (π), joins (⋈), aggregations (Γ), sorts.

---

## Stage 4: Optimization — the hard part

The optimizer transforms the logical plan and chooses physical operators to minimize estimated
cost. It has two halves: **rule-based rewrites** (always-good transformations) and **cost-based
enumeration** (search the plan space, cost each, pick the cheapest).

### Rule-based rewrites (heuristic, always applied)

```
   PREDICATE PUSHDOWN     push filters down toward the scans so fewer rows flow up
                          sigma(region='EU') applied at the orders SCAN, not after the join

   PROJECTION PUSHDOWN    read only the columns you need (huge for column stores)

   JOIN REORDERING        (A join B) join C  vs  A join (B join C) — associativity gives
                          equivalent results but wildly different intermediate sizes

   CONSTANT FOLDING /     WHERE 1=1, WHERE price > 10*5  -> simplified
   SUBQUERY UNNESTING     turn correlated subqueries into joins where possible
```

### Cost-based optimization — the core algorithm

The optimizer assigns each candidate physical plan a **cost** (a unitless estimate of I/O + CPU)
and searches for the minimum. The classic algorithm is **System R / Selinger dynamic
programming** for join ordering (IBM, 1979) — it builds optimal join sub-plans bottom-up,
pruning dominated ones. Modern engines (SQL Server, Postgres) use cost-based optimizers in this
lineage, with Postgres switching to a **genetic algorithm (GEQO)** when the join count is large
because the plan space explodes super-exponentially.

```
   COST(plan) ~= f( rows processed at each operator,         <- from STATISTICS
                    per-operator CPU + I/O cost,
                    whether inputs are sorted / indexed,
                    memory available for hash tables / sorts )

   The optimizer's accuracy is bounded by its CARDINALITY ESTIMATES.
   Garbage estimates -> garbage plans. This is the #1 cause of real-world bad plans.
```

> Bridge: this is exactly the SQL Server "estimated vs actual rows" discrepancy you've seen in
> a query plan. A large gap means the cardinality estimate was wrong (stale statistics, a
> correlation the optimizer assumed away), and the chosen physical operators are mismatched to
> the real data volume.

---

## Statistics and Cardinality Estimation

The optimizer never looks at the data during planning — it looks at **statistics**: compact
summaries of column distributions, refreshed periodically or on a row-change threshold.

```
   PER-COLUMN STATISTICS (typical)
   - row count, number of distinct values (NDV)
   - a HISTOGRAM of value distribution (equi-height/equi-depth buckets)
   - most-common-values (MCV) list + their frequencies
   - null fraction, average column width

   HISTOGRAM (equi-depth): each bucket holds ~the same NUMBER of rows
   value:   0----10----50----200----1000
   rows:    [ 25% ][ 25% ][  25% ][  25% ]
   => estimate rows for WHERE x BETWEEN 10 AND 50 by interpolation within buckets
```

Where estimation goes wrong (all real, all common):

| Failure | Why | Symptom |
|---------|-----|---------|
| **Stale statistics** | Data changed since last `ANALYZE`/stats update | Estimates lag reality; wrong join algo |
| **Correlation** | Optimizer assumes columns independent; `city='Seattle' AND state='WA'` are not | Underestimates AND-of-predicates |
| **Parameter sniffing** | Plan cached for one parameter reused for a skewed other | A plan great for value A, terrible for value B |
| **Out-of-histogram** | Querying a value beyond the stats' range (e.g. "today") | Ascending-key problem in time-series |

Multi-column / extended statistics (Postgres `CREATE STATISTICS`, SQL Server multi-column stats)
exist specifically to capture the correlation case.

---

## Stage 5: Join Algorithms — the heart of the physical plan

Three join algorithms, each optimal for a different shape. The optimizer picks among them by
cost. Getting these right is most of what "reading a query plan" means.

```
+--------------------+   +---------------------+   +-------------------------+
|  NESTED LOOP JOIN  |   |  HASH JOIN          |   |  MERGE (SORT-MERGE) JOIN|
+--------------------+   +---------------------+   +-------------------------+
| for r in outer:    |   | build hash table on |   | sort BOTH inputs on the |
|   for s in inner:  |   |  the smaller input  |   |  join key, then walk     |
|     if match emit  |   | probe it with the   |   |  them in lockstep        |
|                    |   |  larger input       |   |  (merge step)            |
+--------------------+   +---------------------+   +-------------------------+
| O(M * N) naive;    |   | O(M + N) after build|   | O(M log M + N log N) to  |
| O(M * log N) if    |   | (build is O(small)) |   | sort, then O(M+N) merge; |
| inner is INDEXED   |   |                     |   | free if already sorted   |
| (index nested loop)|   |                     |   | (e.g. from an index)     |
+--------------------+   +---------------------+   +-------------------------+
| BEST: small outer, |   | BEST: large, no     |   | BEST: both inputs sorted |
| indexed inner;     |   | useful index, equi- |   | on key (clustered idx),  |
| selective queries  |   | join, plenty of RAM |   | or need sorted output    |
| OLTP point reads   |   | for the hash table  |   | merge of two sorted runs |
+--------------------+   +---------------------+   +-------------------------+
| equality OR range  |   | EQUALITY join only  |   | equality (and some       |
| or any predicate   |   | (it hashes the key) |   | inequality) on sort key  |
+--------------------+   +---------------------+   +-------------------------+
```

Decision logic the optimizer applies:

```
   Small outer + indexed inner ............... INDEX NESTED LOOP   (OLTP sweet spot)
   Two big unsorted inputs, equi-join, RAM .... HASH JOIN          (DW/analytics sweet spot)
   Both inputs already sorted on the key ...... MERGE JOIN         (or need sorted output)
   Hash table won't fit in memory ............. GRACE / hybrid hash join (spills to disk)
```

> The hash join's "build smaller side" matters: you want the hash table to fit in RAM. If it
> spills to disk (grace hash join), cost rises. This is why bad cardinality estimates hurt —
> the optimizer may build the hash on the side it *thinks* is smaller and be wrong.

---

## Aggregation and Sort operators

```
   HASH AGGREGATE      build a hash table keyed on GROUP BY columns; accumulate per group.
                       No ordering required on input. Default for GROUP BY on unsorted data.

   STREAM/SORT         input sorted on GROUP BY key -> aggregate in one pass, emit per group
   AGGREGATE           as the key changes. Free if an index already provides the order.

   TOP-N SORT          ORDER BY ... LIMIT k -> keep a bounded heap of k, don't sort everything.
```

The same "is it already sorted?" question drives aggregation choice as drives merge vs hash
join. An index that provides order can turn a hash aggregate into a cheap stream aggregate.

---

## Stage 6: Execution models

```
   VOLCANO / ITERATOR MODEL (classic, row-at-a-time)
   ------------------------------------------------
   Every operator exposes open() / next() / close().
   next() pulls ONE row from its child, which pulls from ITS child, ... a pull-based pipeline.
   Simple, composable; but one function call per row per operator = high CPU overhead.
   Used by classic OLTP engines (Postgres historically, SQL Server row mode).

   VECTORIZED MODEL (modern analytics)
   -----------------------------------
   next() returns a BATCH (e.g. 1024 rows / a column chunk), not one row.
   Amortizes call overhead, fills SIMD lanes, cache-friendly over columnar data.
   Used by analytic engines: DuckDB, SQL Server batch mode / columnstore, ClickHouse, Spark.
```

Bridge to `data-science/`: the vectorized/columnar execution model is *why* analytic engines
(DuckDB, columnstore, Spark SQL — see `query-languages/07`–`09`) crush OLAP queries a row-store
optimizer would choke on. Same SQL, radically different executor. This is the OLTP↔OLAP divide
made concrete at the execution layer.

---

## Old World → New World Bridges

| You already know | Query-processing concept | SQL Server / Azure anchor |
|------------------|--------------------------|----------------------------|
| A compiler: parse → IR → optimize → codegen | parse → logical plan → cost-based optimize → executor | Showplan stages |
| Estimated vs actual in a profiler | Cardinality estimate vs real row count | "Estimated/Actual rows" in the plan |
| A `Dictionary` for a join in app code | **Hash join** build/probe | Hash Match operator |
| Walking two sorted lists to merge | **Merge join** | Merge Join operator |
| Nested `for` loops over collections | **Nested loop join** (index nested loop if inner indexed) | Nested Loops operator |
| SIMD / batch processing | **Vectorized execution** | Batch mode, columnstore |
| `OPTION (RECOMPILE)` to fix a bad cached plan | Defeating **parameter sniffing** | `RECOMPILE`, plan guides, Query Store |

---

## Decision Cheat Sheet

| Symptom / question | Likely answer |
|--------------------|---------------|
| Plan estimated 10 rows, processed 10M | Stale/missing statistics or correlation → update stats, add multi-column stats |
| Hash join spilling to tempdb/disk | Memory grant too small or wrong build side → bad cardinality estimate |
| Same query fast for one param, slow for another | **Parameter sniffing** → `RECOMPILE`, optimize-for, or query hints |
| OLTP point lookup chose a scan | Selectivity too high or non-sargable predicate (guide 02) |
| Analytic GROUP BY over millions slow on a row store | Wrong engine — want vectorized/columnar execution |
| `ORDER BY` adds a big sort | Provide order via an index (composite, range column last) |
| Join of two huge tables on equality | Expect (and want) a **hash join** if no useful index |
| Small driving table, indexed lookup table | Expect (and want) an **index nested loop** |

---

## Common Confusion Points

### "SQL is declarative so the order I write clauses matters"

It mostly doesn't — the optimizer reorders joins and pushes predicates regardless of textual
order. `FROM A, B WHERE ...` and an explicit `JOIN` produce the same plan space. What matters is
*what's expressible*, statistics, and indexes — not clause order. (Exceptions: `LIMIT`,
windowing, and optimizer hints.)

### "A hash join is always best for big tables"

Only for **equi-joins** with enough memory. Hash join can't do `a.x < b.y`; that needs a nested
loop or merge variant. And if the build side doesn't fit in RAM it spills (grace hash) and gets
slower. A merge join can beat it when both sides are already sorted by an index.

### "The optimizer reads my data to plan the query"

It reads **statistics**, not data. That's why stale stats produce bad plans even though the data
is fine — the optimizer is working from an out-of-date summary. `ANALYZE` / `UPDATE STATISTICS`
refreshes the summary.

### "Adding a hint to force the plan is the fix"

Hints (force-order, force-index, recompile) treat the symptom. The root cause is almost always a
cardinality estimate (stale stats, correlation, parameter sniffing). Fix the estimate and the
optimizer usually finds the good plan on its own — and keeps finding it as data evolves, which a
hardcoded hint will not.

### "More memory always makes joins faster"

It helps hash joins and sorts up to the point where they fit in RAM without spilling. Beyond
that, more memory does nothing for a nested-loop OLTP point read — that's I/O- and index-bound,
not memory-bound.
