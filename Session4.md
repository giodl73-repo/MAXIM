# Session 4 — Query Languages

## Purpose

A **cross-dialect reference series** covering SQL and its major variants, analytical cloud DW platforms,
big data engines, and adjacent query languages (KQL, MongoDB, Redis, GraphQL).
Same peer-level format as Sessions 1–3. Not tutorials. Dense reference cards with T-SQL as the home base.

---

## Series Structure

```
query-languages/
├── 00-OVERVIEW.md      — data model taxonomy, relational algebra map, SQL standards history,
│                         ACID/BASE/SAGA, when SQL vs NoSQL decision tree
├── 01-SQL-CORE.md      — ANSI SQL: the 30-year refresh — CTEs, window functions, JSON,
│                         recursive queries, temporal tables, modern syntax
│
├── 02-POSTGRESQL.md    — PostgreSQL: JSONB, arrays, LATERAL, full-text, EXPLAIN ANALYZE,
│                         extensions (pgvector, PostGIS, TimescaleDB), partitioning, RLS
├── 03-TSQL.md          — T-SQL: SQL Server + Azure SQL — APPLY, MERGE, OUTPUT, JSON,
│                         temporal tables, Query Store, DMVs, Synapse Analytics
├── 04-MYSQL.md         — MySQL/MariaDB: InnoDB, window functions (8.0+), utf8mb4 trap,
│                         JSON, generated columns, fulltext, MariaDB differences
├── 05-SQLITE.md        — SQLite: embedded/serverless, WAL mode, STRICT tables, JSON1,
│                         FTS5, in-memory testing pattern, date handling
│
├── 06-KQL.md           — Kusto Query Language: Azure Monitor/Log Analytics/App Insights/ADX,
│                         pipe syntax, time functions, SQL→KQL translation table, Sentinel hunting
│
├── 07-ANALYTICAL.md    — Cloud DW SQL: BigQuery, Snowflake, Databricks, Synapse —
│                         QUALIFY, PIVOT, time travel, MERGE INTO, medallion architecture, dbt
├── 08-SPARKSQL.md      — Spark SQL + Delta Lake: DataFrame vs SQL API, partitioning,
│                         broadcast joins, MERGE INTO, OPTIMIZE/ZORDER/VACUUM, streaming
├── 09-DUCKDB.md        — DuckDB: OLAP in-process, direct Parquet/CSV/JSON query,
│                         PIVOT auto-detection, LIST/STRUCT lambdas, Python zero-copy
│
├── 10-MONGODB.md       — MongoDB MQL + aggregation pipeline: $match/$group/$lookup/$unwind,
│                         indexes (TTL, partial, 2dsphere), Atlas Search + Vector Search
├── 11-REDIS.md         — Redis: String/Hash/List/Set/ZSet/Stream commands, MULTI/EXEC,
│                         Lua scripting, RediSearch (full-text + KNN vector), distributed lock
└── 12-GRAPHQL.md       — GraphQL: SDL schema, query/mutation/subscription syntax,
                          N+1 + DataLoader, federation, Hasura, REST vs GraphQL decision
```

---

## Per-Dialect Template

Every file covers the same sections in the same order:

| Section | Content |
|---------|---------|
| **Dialect Snapshot** | Origin, license, version, ACID, strengths, cloud options |
| **Core Syntax Reference Card** | Actual code examples, dialect-specific patterns |
| **What Makes It Distinct** | Key differentiators vs ANSI SQL or the "standard" |
| **Advanced / Killer Features** | The power features that make this dialect worth knowing |
| **Gotchas from T-SQL** | Traps for someone coming from SQL Server / ADO.NET |
| **Ecosystem / Tooling** | Clients, ORMs, cloud hosting, monitoring |
| **Decision Cheat Sheet** | When to reach for this vs alternatives |
| **Common Confusion Points** | Named gotchas, common mental model errors |

---

## Cross-Reference Index

| What you want | Where to look |
|---------------|---------------|
| SQL since 2000 — what changed? | `01-SQL-CORE.md` — the 30-year refresh |
| Window functions | `01-SQL-CORE.md` sections 6 + dialect files |
| JSONB operators (->, ->>, @>) | `02-POSTGRESQL.md` |
| CROSS APPLY / OUTER APPLY | `03-TSQL.md` or `02-POSTGRESQL.md` (LATERAL) |
| SQL Server temporal tables | `03-TSQL.md` |
| utf8 vs utf8mb4 | `04-MYSQL.md` — it's a trap |
| SQLite in tests (in-memory) | `05-SQLITE.md` |
| Azure Monitor log queries | `06-KQL.md` |
| App Insights performance analysis | `06-KQL.md` — Common App Insights Patterns |
| Cloud DW comparison (BigQuery/Snowflake/Databricks) | `07-ANALYTICAL.md` |
| QUALIFY (filter window functions) | `07-ANALYTICAL.md` or `09-DUCKDB.md` |
| Delta Lake MERGE + time travel | `08-SPARKSQL.md` |
| MapReduce → Spark SQL bridge | `08-SPARKSQL.md` — Architecture section |
| Query Parquet without a server | `09-DUCKDB.md` |
| MongoDB aggregation as SQL | `10-MONGODB.md` — SQL→MQL translation table |
| Atlas Vector Search (for RAG) | `10-MONGODB.md` — Atlas Search section |
| Redis data structures | `11-REDIS.md` |
| Redis vector search (RediSearch KNN) | `11-REDIS.md` — Redis Stack Modules |
| GraphQL vs REST decision | `12-GRAPHQL.md` |
| N+1 problem | `12-GRAPHQL.md` — DataLoader section |

---

## Key Themes

### SQL never lost to NoSQL
Every time a new compute paradigm arrived, SQL climbed on top of it:
- MapReduce (2004) → Hive adds SQL (2008)
- Distributed in-memory → Spark SQL (2014)
- Cloud object storage → BigQuery, Snowflake (2010s)
- Vector embeddings → pgvector extends PostgreSQL (2021)
- LLM RAG pipelines → SQL is still the retrieval query language

### The 30-year gap (2000 → 2024)
T-SQL in 2000 had basic SELECT/JOIN/GROUP BY. What changed since ADO.NET era:
- `CTEs` (SQL:1999) — recursive queries, readability
- `Window functions` (SQL:2003) — ranking, LAG/LEAD, running totals
- `MERGE` (SQL:2003) — UPSERT semantics
- `Temporal tables` (SQL:2011) — system-versioned row history
- `JSON` (SQL:2016) — JSON_VALUE, JSON_QUERY, JSON_TABLE
- `QUALIFY` (BigQuery/Snowflake) — filter on window function results
- `GENERATE_SERIES`, `DATE_BUCKET`, `IS NOT DISTINCT FROM` (SQL:2023)

### RAG pipeline ↔ query languages
```
Documents → chunk → embed                (Python)
Vectors stored in pgvector               → SQL: ORDER BY embedding <=> $1 LIMIT k
Vectors stored in MongoDB Atlas          → $vectorSearch aggregation stage
Vectors stored in Redis                  → RediSearch FT.SEARCH with KNN
Telemetry / eval results                 → KQL in App Insights / Log Analytics
```

---

## Learner Context

MIT Math + TCS — already knows:
- Relational algebra (σ, π, ⋈, ×, ∪, ∩, −) — `00-OVERVIEW.md` bridges to SQL syntax
- Set semantics — explains UNION vs UNION ALL, NULL three-valued logic
- Distributed systems theory — explains CAP, BASE, partition tolerance tradeoffs
- MapReduce execution model — explains Spark's DAG vs MR's disk-between-steps
- Type theory — explains SQL's type coercion rules and NULL propagation

What this series delivers:
- 30 years of SQL evolution since the ADO.NET era
- T-SQL-to-modern bridges throughout
- Exact syntax differences between dialects (not just "they're similar")
- When each tool wins vs alternatives

---

## Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `query-languages/00-OVERVIEW.md` | Landscape, relational algebra, SQL standards, ACID/BASE | ✅ Complete |
| `query-languages/01-SQL-CORE.md` | ANSI SQL — the 30-year refresh | ✅ Complete |
| `query-languages/02-POSTGRESQL.md` | PostgreSQL | ✅ Complete |
| `query-languages/03-TSQL.md` | T-SQL (SQL Server + Azure SQL + Synapse) | ✅ Complete |
| `query-languages/04-MYSQL.md` | MySQL / MariaDB | ✅ Complete |
| `query-languages/05-SQLITE.md` | SQLite | ✅ Complete |
| `query-languages/06-KQL.md` | Kusto Query Language | ✅ Complete |
| `query-languages/07-ANALYTICAL.md` | BigQuery + Snowflake + Databricks + Synapse | ✅ Complete |
| `query-languages/08-SPARKSQL.md` | Spark SQL + Delta Lake | ✅ Complete |
| `query-languages/09-DUCKDB.md` | DuckDB | ✅ Complete |
| `query-languages/10-MONGODB.md` | MongoDB MQL + Aggregation Pipeline | ✅ Complete |
| `query-languages/11-REDIS.md` | Redis commands + modules | ✅ Complete |
| `query-languages/12-GRAPHQL.md` | GraphQL query language | ✅ Complete |
