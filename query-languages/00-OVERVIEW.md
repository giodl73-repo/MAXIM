# Query Languages — Taxonomy & Landscape

---

## 1. The Full Landscape

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                     QUERY LANGUAGE LANDSCAPE (2024)                            ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  RELATIONAL (SQL FAMILY)                    ANALYTICAL / CLOUD DW               ║
║  ┌─────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  ANSI SQL (standard)                │   │  BigQuery      — SQL dialect      │  ║
║  │    ├─ PostgreSQL  (most ANSI-close) │   │  Snowflake     — SQL + JS UDFs   │  ║
║  │    ├─ T-SQL       (SQL Server)      │   │  Databricks    — Spark SQL/Delta  │  ║
║  │    ├─ MySQL/MariaDB                 │   │  Synapse Analytics — T-SQL+Spark  │  ║
║  │    ├─ SQLite      (embedded)        │   │  Redshift      — PostgreSQL fork  │  ║
║  │    └─ DuckDB      (in-process OLAP) │   │  Athena        — Trino/Presto SQL │  ║
║  └─────────────────────────────────────┘   └──────────────────────────────────┘  ║
║                                                                                  ║
║  BIG DATA / DISTRIBUTED                    PIPE-BASED / FUNCTIONAL              ║
║  ┌─────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  Spark SQL   — SQL over RDDs/DFs    │   │  KQL (Kusto)   — pipe chains     │  ║
║  │  Hive HQL    — SQL over MapReduce   │   │    events | where ts > ago(1d)   │  ║
║  │  Presto/Trino — federated SQL       │   │    | summarize count() by host   │  ║
║  │  Flink SQL   — streaming SQL        │   │                                  │  ║
║  │  Hudi/Iceberg — table format + SQL  │   │  PRQL     — compiles to SQL      │  ║
║  └─────────────────────────────────────┘   │  jq       — JSON query + filter  │  ║
║                                            └──────────────────────────────────┘  ║
║  DOCUMENT                                  KEY-VALUE                            ║
║  ┌─────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  MongoDB MQL  — find({...})         │   │  Redis commands — GET/SET/HGET   │  ║
║  │  MongoDB Agg  — aggregation pipeline│   │  DynamoDB PartiQL — SQL-ish      │  ║
║  │  Elasticsearch DSL — JSON queries   │   │  Memcached — GET key             │  ║
║  │  Firestore    — collection queries  │   └──────────────────────────────────┘  ║
║  └─────────────────────────────────────┘                                         ║
║                                                                                  ║
║  GRAPH                                     TIME-SERIES                          ║
║  ┌─────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  Cypher   — Neo4j, memgraph         │   │  InfluxDB Flux — functional pipe │  ║
║  │    MATCH (a)-[:KNOWS]->(b) RETURN a │   │  InfluxQL      — SQL-like        │  ║
║  │  SPARQL   — RDF triple stores       │   │  TimescaleDB   — PostgreSQL ext  │  ║
║  │  Gremlin  — Apache TinkerPop        │   │  OpenTSDB      — HBase-backed    │  ║
║  │  GQL      — ISO standard (2024)     │   └──────────────────────────────────┘  ║
║  │  SQL/PGQ  — SQL:2023 graph queries  │                                         ║
║  └─────────────────────────────────────┘                                         ║
║                                                                                  ║
║  API QUERY                                 SEARCH                               ║
║  ┌─────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  GraphQL  — schema-typed API query  │   │  Elasticsearch Query DSL         │  ║
║  │  OData    — REST + query params     │   │  OpenSearch DSL                  │  ║
║  │  SPARQL   — also RDF HTTP endpoints │   │  Solr Query Language             │  ║
║  └─────────────────────────────────────┘   └──────────────────────────────────┘  ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Relational Algebra Bridge

You know the math — this is the mapping to SQL syntax:

| RA Symbol | Operation | SQL Equivalent | Notes |
|-----------|-----------|----------------|-------|
| σ (sigma) | Selection | `WHERE` clause | Row filter — before aggregation |
| π (pi) | Projection | `SELECT col1, col2` | Column filter — eliminates others |
| ⋈ (bowtie) | Natural join | `JOIN ... ON` | Natural join (on matching names) = rare in SQL; use explicit ON |
| × | Cartesian product | `CROSS JOIN` | All n×m combinations |
| ∪ | Union | `UNION` | SQL UNION removes duplicates (set semantics) |
| ∩ | Intersection | `INTERSECT` | Rows in both result sets |
| − | Set difference | `EXCEPT` (ANSI) / `MINUS` (Oracle) | Rows in first but not second |
| ρ (rho) | Rename | `AS alias` | Column or table alias |
| γ (gamma) | Aggregation | `GROUP BY` + aggregate functions | Extended RA — not in Codd's original |
| δ | Duplicate elimination | `DISTINCT` | SQL is multiset by default; DISTINCT forces set |

**What relational algebra doesn't cover (SQL extensions):**

```
Classic RA: operates on sets (no duplicates, no ordering)
SQL reality: operates on multisets (bags) — duplicates exist until eliminated

Extensions beyond classic RA:
  - Window functions   — ordered aggregation without collapsing rows
  - Recursive queries  — iterative fixpoint (not expressible in first-order RA)
  - NULLS              — three-valued logic (TRUE/FALSE/UNKNOWN) — Codd added later
  - ORDER BY           — RA has no notion of ordering
  - LIMIT/OFFSET       — positional access (not relational)
  - DML                — INSERT/UPDATE/DELETE (RA is read-only)
```

**Three-valued logic (NULL semantics):**
```
TRUE  AND UNKNOWN = UNKNOWN
FALSE AND UNKNOWN = FALSE
TRUE  OR  UNKNOWN = TRUE
FALSE OR  UNKNOWN = UNKNOWN
NOT UNKNOWN       = UNKNOWN

Consequence: WHERE col = NULL  → always UNKNOWN, never selects any rows
             WHERE col IS NULL → correct
             IN (list_with_null) can produce surprising UNKNOWN results
```

---

## 3. SQL Standards History

| Standard | Year | Key Additions | T-SQL circa 2000 had it? |
|----------|------|---------------|--------------------------|
| SQL-86 (SQL-87) | 1986 | SELECT, basic JOINs, basic DDL, WHERE | Yes |
| SQL-89 | 1989 | Integrity constraints, minor fixes | Yes |
| SQL-92 | 1992 | FULL OUTER JOIN, CASE, CAST, string functions, schema DDL, dynamic SQL | Mostly yes |
| SQL:1999 (SQL3) | 1999 | **Recursive CTEs (WITH RECURSIVE)**, triggers, UDTs, BOOLEAN type, OO extensions | Partial (WITH existed as proprietary in SQL Server 2005+; not in 2000) |
| SQL:2003 | 2003 | **Window functions (OVER)**, MERGE, SEQUENCE, XML type, identity columns, multiset types | No — major gap |
| SQL:2008 | 2008 | TRUNCATE, **FETCH FIRST n ROWS ONLY** (ANSI pagination), INSTEAD OF triggers | No (T-SQL used TOP n) |
| SQL:2011 | 2011 | **Temporal tables** (system-versioned + application-time), PERIOD FOR | No |
| SQL:2016 | 2016 | **JSON** (JSON_VALUE, JSON_QUERY, JSON_TABLE), row pattern recognition (MATCH_RECOGNIZE) | No |
| SQL:2023 | 2023 | **SQL/PGQ** (property graph queries in SQL), UNIQUE predicate, improved JSON, PIPE syntax (preview) | No |

**Your reference point (T-SQL / SQL Server 2000):**
```
Had:           SELECT, JOIN, GROUP BY, HAVING, subqueries, TOP n,
               basic transactions, stored procedures, triggers, cursors

Did NOT have:  CTEs (WITH), window functions (OVER / PARTITION BY),
               MERGE, FETCH FIRST, temporal tables, JSON, recursive queries,
               LATERAL, FILTER on aggregates, GROUPING SETS/CUBE/ROLLUP
```

Everything from SQL:1999 onward is what this series is filling in.

---

## 4. Data Model Taxonomy

| Model | Structure | Query Paradigm | Strengths | Example Systems |
|-------|-----------|----------------|-----------|-----------------|
| **Relational** | Tables, rows, columns — normalized | SQL (set-based, declarative) | Complex joins, ACID, ad-hoc queries | PostgreSQL, SQL Server, MySQL, Oracle, SQLite |
| **Document** | JSON/BSON trees — schema-flexible | MQL / aggregation pipeline / SQL-ish | Flexible schema, nested data, app-natural shape | MongoDB, Firestore, CouchDB, DynamoDB (partial) |
| **Key-Value** | Flat key → value (opaque or typed) | GET/SET/HGET/SCAN commands | Extreme speed, cache, sessions, counters | Redis, Memcached, DynamoDB, etcd |
| **Column-family** | Rows → sparse column families | CQL (Cassandra Query Language) | Write-heavy, time-series, wide rows, horizontal scale | Cassandra, HBase, ScyllaDB |
| **Graph** | Nodes + edges + properties | Cypher, SPARQL, Gremlin, GQL | Relationship traversal, social graphs, fraud detection | Neo4j, Neptune, TigerGraph, ArangoDB |
| **Time-series** | Measurements + timestamps + tags | Flux, InfluxQL, TSQ | IoT, metrics, downsampling, retention policies | InfluxDB, TimescaleDB, Prometheus (query: PromQL), VictoriaMetrics |
| **Search / Inverted Index** | Tokenized documents | Query DSL (JSON), Lucene syntax | Full-text search, fuzzy match, facets, relevance scoring | Elasticsearch, OpenSearch, Solr, Typesense |
| **Analytical / OLAP** | Columnar storage + cloud-native | SQL dialects (BigQuery/Snowflake SQL) | Aggregation at PB scale, vectorized execution, partitioning | BigQuery, Snowflake, Databricks, Redshift, DuckDB |

**Row-store vs column-store — the core OLTP/OLAP split:**
```
Row-store (PostgreSQL, SQL Server):
  ┌─────┬──────┬───────┬──────────┐
  │ id  │ name │ dept  │ salary   │  ← each row stored contiguously
  │ 1   │ Alice│ Eng   │ 120000   │    good for: point reads, OLTP writes
  │ 2   │ Bob  │ Mktg  │ 95000    │    bad for:  "SUM(salary) for 10M rows"
  └─────┴──────┴───────┴──────────┘

Column-store (BigQuery, Snowflake, DuckDB):
  id:     [1, 2, 3, ...]            ← each column stored contiguously
  name:   [Alice, Bob, ...]         good for: aggregate queries (read 1 column, skip rest)
  salary: [120000, 95000, ...]      bad for:  point reads (must reconstruct row)
                                    also:     vectorized SIMD ops on column arrays
```

---

## 5. ACID vs BASE vs SAGA

### ACID (relational default)

```
Atomicity   — transaction commits entirely or rolls back entirely
              "the A and B transfer either both happen or neither"

Consistency — each transaction transitions the DB from one valid state to another
              foreign keys, CHECK constraints, triggers all fire within the transaction

Isolation   — concurrent transactions don't see each other's partial work
              (degree configurable — see isolation levels below)

Durability  — committed transactions survive crashes
              WAL (write-ahead log) / redo log ensures this
```

### ACID Isolation Levels

| Level | Dirty Read | Non-Repeatable Read | Phantom Read | Notes |
|-------|-----------|---------------------|--------------|-------|
| READ UNCOMMITTED | possible | possible | possible | Sees uncommitted data from other txns; almost never use |
| READ COMMITTED | prevented | possible | possible | Default in PostgreSQL, SQL Server, Oracle |
| REPEATABLE READ | prevented | prevented | possible | Default in MySQL InnoDB; re-read same rows = same values |
| SERIALIZABLE | prevented | prevented | prevented | Transactions appear to run serially; highest cost |

```
Dirty read:          you read data another transaction hasn't committed yet
Non-repeatable read: you read a row twice; another txn committed a change between reads
Phantom read:        you run the same query twice; another txn inserted rows that now appear
```

PostgreSQL uses MVCC (multiversion concurrency control) — readers don't block writers.
SQL Server also uses MVCC when READ_COMMITTED_SNAPSHOT is on (default in Azure SQL).

### BASE (NoSQL default)

```
Basically Available  — system always responds (may be stale or inconsistent)
Soft state           — state may change over time even without input (replicas converging)
Eventually consistent — all replicas converge to the same value given enough time
```

### CAP Theorem

```
                        Consistency
                           /\
                          /  \
                         /    \
                        /  CP  \
                       /        \
                      /──────────\
                     /  CA   | AP \
                    /________|_____\
              Availability   Partition Tolerance

You can have at most 2 of 3 during a network partition:
  CP: consistent + partition-tolerant (sacrifice availability) — HBase, Zookeeper, etcd
  AP: available + partition-tolerant (sacrifice consistency)   — Cassandra, CouchDB, DynamoDB (default)
  CA: consistent + available (sacrifice partition tolerance)   — single-node SQL (no partitions to tolerate)

Modern framing: PACELC — also considers latency vs consistency when no partition
```

### SAGA Pattern (distributed transactions)

```
Problem: ACID spans one DB. Microservices have multiple DBs.

SAGA: sequence of local transactions, each publishing events to trigger the next step
      compensating transactions undo completed steps if a later step fails

Choreography SAGA:         Orchestration SAGA:
  Svc A → event → Svc B     Orchestrator → Svc A
  Svc B → event → Svc C                  → Svc B
  failure: Svc B fires                   → Svc C
  compensating event                     controls the flow
```

---

## 6. SQL vs NoSQL vs NewSQL — Decision Tree

```
Start
  │
  ▼
Is data structure well-defined (schema stable, normalized)?
  ├─ NO  → semi-structured / schemaless
  │         Is it nested/hierarchical JSON-shaped?
  │           ├─ YES → Document DB (MongoDB, Firestore)
  │           └─ NO  → depends on access pattern (see below)
  │
  └─ YES → structured data
             │
             ▼
           What is the primary query pattern?
             │
             ├─ Complex joins / ad-hoc queries / OLTP
             │    ├─ Single node or moderate scale → PostgreSQL / SQL Server
             │    └─ Planet-scale writes needed → NewSQL (CockroachDB, Spanner, YugabyteDB)
             │
             ├─ Aggregation over large datasets (analytics / reporting)
             │    ├─ Cloud-native / managed → BigQuery / Snowflake / Synapse
             │    ├─ On-prem or local OLAP  → DuckDB / ClickHouse
             │    └─ Spark workloads        → Databricks / Spark SQL
             │
             ├─ Graph traversal (social, fraud, knowledge graphs)
             │    └─ Graph DB (Neo4j, Neptune, memgraph)
             │
             ├─ Time-series / IoT metrics
             │    ├─ Need PromQL for metrics alerting → Prometheus + Thanos
             │    ├─ Need SQL + time funcs           → TimescaleDB
             │    └─ Need dedicated TSDB             → InfluxDB
             │
             ├─ Full-text search / relevance ranking
             │    └─ Elasticsearch / OpenSearch / Typesense
             │
             ├─ Cache / session / rate limiting (low latency, simple access)
             │    └─ Redis
             │
             └─ Observability / logs / traces
                  └─ KQL (Azure Monitor / ADX) / Loki LogQL / OpenSearch
```

---

## 7. Common Confusion Points

**"NoSQL means no SQL"**
Wrong. MongoDB has a full aggregation pipeline query language. DynamoDB has PartiQL (SQL subset).
CockroachDB is "NoSQL" scale but uses PostgreSQL-compatible SQL.
"NoSQL" = "not only SQL" or "non-relational" — it says nothing about query language syntax.

**SQL dialects vs SQL standard**
ANSI SQL is the spec. Every database adds proprietary extensions and omits parts of the spec.
`TOP n` (T-SQL) vs `LIMIT n` (PostgreSQL/MySQL) vs `FETCH FIRST n ROWS ONLY` (ANSI) vs `ROWNUM` (Oracle) — all do the same thing, none are portable.
Code written for SQL Server 2000 will not run on PostgreSQL without changes.

**OLTP vs OLAP — different optimization targets**
```
OLTP (Online Transaction Processing):
  - Many small reads/writes (point lookups, single-row updates)
  - Row-store: good for fetching one row across all columns
  - Indexes on primary keys and FK columns
  - SQL Server / PostgreSQL in production apps

OLAP (Online Analytical Processing):
  - Few large scans (aggregate millions of rows, few columns)
  - Column-store: skip irrelevant columns, vectorized arithmetic
  - Partitioning by date range; clustering keys
  - BigQuery / Snowflake / DuckDB / Synapse
```
Trying to run OLAP queries on an OLTP database causes table scans and contention.
Trying to run OLTP patterns on a columnar warehouse causes excessive I/O.

**NULL semantics: NULL != NULL**
```sql
NULL = NULL    → UNKNOWN (not TRUE)
NULL != NULL   → UNKNOWN (not TRUE)
NULL IS NULL   → TRUE    ← correct check
NOT (NULL = 1) → UNKNOWN (not TRUE — rows filtered out!)

-- Gotcha with IN:
WHERE id IN (1, 2, NULL)
-- is: WHERE id = 1 OR id = 2 OR id = NULL
-- id = NULL → UNKNOWN → no rows match via the NULL branch
-- Rows where id IS NULL are NOT returned
```

**Set semantics vs multiset semantics**
```
Relational algebra: operates on sets (no duplicates)
SQL tables:         are multisets (bags) — duplicates exist unless eliminated

UNION     → set union     (removes duplicates, costs a hash/sort)
UNION ALL → multiset union (keeps all rows, no dedup cost)
INTERSECT → set intersection (dedup implied)
EXCEPT    → set difference  (dedup implied)

Use UNION ALL by default; only use UNION when dedup is semantically required.
```

**KQL is not SQL (Azure Monitor, ADX)**
```sql
-- SQL:
SELECT host, COUNT(*) AS errors
FROM   logs
WHERE  timestamp > DATEADD(day,-1,GETDATE())
  AND  level = 'ERROR'
GROUP BY host

-- KQL (pipe-based, left-to-right data flow):
logs
| where timestamp > ago(1d)
| where level == "ERROR"
| summarize errors=count() by host
```
KQL reads like a pipeline (each `|` stage transforms the dataset).
Used in: Azure Monitor, Azure Data Explorer, Microsoft Sentinel, Application Insights.
You probably already know KQL from the Azure side — it's the query language behind Log Analytics.
