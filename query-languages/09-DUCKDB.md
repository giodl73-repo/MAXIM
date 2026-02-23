# DuckDB

DuckDB is SQLite for analytics — an in-process OLAP database. Single binary, no server, embeds into Python/Node/R/.NET. But unlike SQLite (row-oriented, OLTP), DuckDB uses vectorized columnar execution designed for aggregations over millions of rows. The killer feature: query Parquet, CSV, and JSON files directly without loading them first. It's rapidly replacing pandas for local data analysis.

---

## 1. Ecosystem Position

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    DuckDB vs SQLite vs Spark — Positioning                   │
│                                                                              │
│  SQLite ──── row-oriented ──── OLTP/transactional ──── tiny data (KB-GB)   │
│                                                                              │
│  DuckDB ──── column-oriented ── OLAP/analytical ──── local data (GB-TB)    │
│                                                                              │
│  Spark ───── distributed ────── OLAP/batch ────────── cluster data (TB-PB) │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Your Application                             │   │
│  │    Python  /  Node.js  /  R  /  C#  /  Java  /  CLI               │   │
│  └───────────────────────────────┬─────────────────────────────────────┘   │
│                                  │  in-process call (no network)           │
│  ┌───────────────────────────────▼─────────────────────────────────────┐   │
│  │                        DuckDB Engine                                │   │
│  │  ┌──────────────────────────────────────────────────────────────┐  │   │
│  │  │  SQL Parser → Binder → Optimizer → Physical Planner          │  │   │
│  │  │  → Vectorized Execution (SIMD, batch = 2048 rows)            │  │   │
│  │  └──────────────────────────────────────────────────────────────┘  │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌─────────────┐  │   │
│  │  │  .duckdb   │  │  Parquet   │  │    CSV     │  │    JSON     │  │   │
│  │  │  (file or  │  │   files    │  │   files    │  │   files     │  │   │
│  │  │  in-memory)│  │ (local/S3) │  │(local/S3)  │  │(local/HTTP) │  │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └─────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────┘

Bridge: think of it as SSAS running inside your Python process — but reads open file
formats instead of proprietary cubes, and writes Parquet instead of .bim files.
```

---

## 2. Dialect Snapshot

| Attribute | Value |
|-----------|-------|
| Created by | CWI Amsterdam (Mark Raasveldt, Hannes Mühleisen), 2019 |
| License | MIT |
| Current version | DuckDB 1.x (2024) |
| Architecture | In-process, single file or in-memory, multi-threaded |
| Execution model | Vectorized columnar — SIMD batches of 2048 rows |
| SQL dialect | PostgreSQL-compatible (mostly) + DuckDB extensions |
| Unique strengths | Direct file query (Parquet/CSV/JSON), PIVOT auto-detect, lambdas, nested types |
| Python | `duckdb.sql("...").df()` → pandas, `.pl()` → Polars, zero-copy DataFrame query |
| Concurrency | Single writer, multiple readers — same constraint as SQLite |
| Best fit | Local analytics, ETL pre-processing, data exploration, pipeline testing |

---

## 3. Why It's Fast — Execution Model

```
Row-oriented store (SQLite / SQL Server heap):
  Row 1: [id=1 | name="Alice" | dept="Eng" | salary=90000 | email="a@b.com" | ...]
  Row 2: [id=2 | name="Bob"   | dept="Eng" | salary=85000 | email="b@b.com" | ...]
  ...
  SELECT AVG(salary) → must read every byte of every row to get salary column

Column-oriented store (DuckDB / Parquet):
  id col:     [1, 2, 3, 4, 5, ...]
  name col:   ["Alice", "Bob", ...]
  salary col: [90000, 85000, 72000, ...]   ← only this column is read from disk

  SELECT AVG(salary) → reads ONLY the salary column, skips all others

Vectorized execution:
  Row-at-a-time (SQLite, row-store):   loop { process one row; advance cursor }
  Vectorized (DuckDB):                 load 2048 salary values into CPU registers
                                       execute SIMD AVG across all 2048 at once
                                       → single CPU instruction for 2048 values

Result: GROUP BY / aggregation on millions of rows → 10–100× faster than SQLite
```

---

## 4. Direct File Queries — The Killer Feature

No `CREATE TABLE`, no `LOAD DATA`. Just query the file.

```sql
-- Parquet — single file
SELECT * FROM 'data/orders.parquet' LIMIT 10;

-- Parquet — glob: all .parquet files in directory
SELECT * FROM 'data/orders/*.parquet';

-- Parquet — multiple files with potentially different schemas (union)
SELECT * FROM read_parquet('data/*.parquet', union_by_name = true);

-- CSV — auto-detect schema
SELECT * FROM 'data/users.csv' LIMIT 5;

-- CSV — explicit schema
SELECT * FROM read_csv('data/users.csv',
    header      = true,
    columns     = {'id': 'BIGINT', 'name': 'VARCHAR', 'email': 'VARCHAR'},
    dateformat  = '%Y-%m-%d'
);

-- JSON — array of objects, auto-detect schema
SELECT * FROM read_json_auto('data/events.json');

-- JSON — explicit schema
SELECT * FROM read_json('data/events.json',
    columns = {'event_id': 'BIGINT', 'ts': 'TIMESTAMP', 'payload': 'JSON'}
);
```

### Remote Files — httpfs extension

```sql
-- Install once per machine (downloads from DuckDB extension repo)
INSTALL httpfs;
LOAD httpfs;

-- S3
SET s3_region          = 'us-east-1';
SET s3_access_key_id   = 'AKIA...';
SET s3_secret_access_key = '...';
SELECT * FROM 's3://my-bucket/data/orders.parquet';

-- ADLS Gen2 (Azure)
SET azure_storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=...';
SELECT * FROM 'azure://container/path/data.parquet';

-- Raw HTTP(S) — e.g. GitHub raw files, public datasets
SELECT * FROM 'https://raw.githubusercontent.com/user/repo/main/data.csv';
```

---

## 5. Core SQL — PostgreSQL-Compatible Extensions

```sql
-- SUMMARIZE: descriptive statistics for every column in one shot
SUMMARIZE SELECT * FROM 'data/orders.parquet';
SUMMARIZE orders;
-- Returns per column: column_name, min, max, approx_unique, avg, std,
--                     q25, q50, q75, count, null_percentage

-- DESCRIBE: schema
DESCRIBE SELECT * FROM orders;
DESCRIBE orders;

-- SHOW TABLES
SHOW TABLES;
SHOW ALL TABLES;   -- includes all schemas

-- SAMPLE: statistical sampling — avoids full-scan for exploration
SELECT * FROM orders USING SAMPLE 10%;             -- Bernoulli, 10% of rows
SELECT * FROM orders USING SAMPLE 1000 ROWS;       -- exactly 1000 rows
SELECT * FROM orders USING SAMPLE 10% (BERNOULLI); -- row-by-row probabilistic
SELECT * FROM orders USING SAMPLE 10% (SYSTEM);    -- page-level, faster for large tables
```

---

## 6. PIVOT

DuckDB's PIVOT auto-detects the distinct values of the pivot column. No explicit column list required — unlike T-SQL PIVOT which requires a hard-coded `IN ([Q1],[Q2],[Q3])`.

```sql
-- Auto-detect quarters from data, create one column per distinct value
PIVOT orders
ON quarter
USING SUM(revenue);

-- Multiple aggregate expressions
PIVOT orders
ON quarter
USING SUM(revenue) AS revenue, COUNT(*) AS order_count
GROUP BY product_id;

-- UNPIVOT: columns → rows
UNPIVOT wide_table
ON (q1, q2, q3, q4)
INTO NAME quarter VALUE revenue;

-- T-SQL bridge: what DuckDB does automatically
-- T-SQL equivalent (verbose, requires knowing values at query-write time):
SELECT product_id, [Q1], [Q2], [Q3], [Q4]
FROM   orders
PIVOT (SUM(revenue) FOR quarter IN ([Q1],[Q2],[Q3],[Q4])) AS pvt;
-- DuckDB scans data to discover ['Q1','Q2','Q3','Q4'] — no IN list needed
```

---

## 7. Nested Types — LIST, STRUCT, MAP

DuckDB has first-class nested types with lambda support. No equivalent in T-SQL.

```sql
-- LIST (like PostgreSQL ARRAY / BigQuery ARRAY)
SELECT [1, 2, 3] AS nums;

SELECT list_transform([1,2,3,4,5], x -> x * x)       AS squares;   -- map
SELECT list_filter([1,2,3,4,5],   x -> x % 2 = 0)    AS evens;     -- filter
SELECT list_aggregate([10,20,30], 'sum')               AS total;     -- reduce
SELECT list_sort([3,1,2])                              AS sorted;
SELECT unnest([1,2,3])                                 AS val;       -- explode to rows

-- STRUCT (named fields — like a record type)
SELECT {'name': 'Alice', 'age': 30}                    AS person;
SELECT person.name
FROM   (SELECT {'name': 'Alice', 'age': 30} AS person);

SELECT struct_pack(name := 'Alice', age := 30)         AS person;

-- MAP (dictionary)
SELECT map(['a','b'], [1,2])                            AS m;
SELECT m['a']
FROM   (SELECT map(['a','b'], [1,2]) AS m);

-- Practical: nested line_items in an orders table
SELECT
    order_id,
    list_transform(line_items, li -> li.quantity * li.unit_price)      AS item_totals,
    list_aggregate(
        list_transform(line_items, li -> li.quantity * li.unit_price),
        'sum'
    )                                                                   AS order_total
FROM orders_with_nested_items;
```

---

## 8. COPY — Import / Export

```sql
-- Export to Parquet (columnar, Snappy compressed by default)
COPY orders TO 'output/orders.parquet'  (FORMAT parquet);
COPY (SELECT * FROM orders WHERE year = 2024)
  TO 'output/orders_2024.parquet'       (FORMAT parquet, COMPRESSION zstd);

-- Export to CSV
COPY orders TO 'output/orders.csv'      (FORMAT csv, HEADER true);

-- Export to JSON
COPY orders TO 'output/orders.json'     (FORMAT json, ARRAY true);

-- Import CSV into existing table
COPY orders FROM 'input/orders.csv'     (FORMAT csv, HEADER true);

-- Export / import entire database
EXPORT DATABASE 'backup_dir' (FORMAT parquet);
IMPORT DATABASE 'backup_dir';
```

---

## 9. Python Integration

```python
import duckdb
import pandas as pd

# In-memory (nothing persisted after process exits)
con = duckdb.connect()

# Persistent file
con = duckdb.connect('analytics.duckdb')

# Query file → pandas DataFrame
df = con.sql("SELECT * FROM 'data.parquet'").df()

# Query file → Polars DataFrame
pl_df = con.sql("SELECT * FROM 'data.parquet'").pl()

# Query a pandas/polars DataFrame DIRECTLY — zero-copy
# DuckDB reads the Python variable's memory, no data movement
orders_df = pd.read_parquet('orders.parquet')
result = duckdb.sql(
    "SELECT customer_id, SUM(total) AS revenue FROM orders_df GROUP BY 1"
).df()

# Register a DataFrame as a named table
con.register('orders', orders_df)
con.sql("SELECT * FROM orders WHERE total > 100")

# DDL / DML
con.execute("CREATE TABLE orders AS SELECT * FROM 'data/orders.parquet'")
con.execute("INSERT INTO orders VALUES (?, ?, ?)", [1, 2, 99.99])

# Relation API — lazy evaluation (like Spark DataFrame / SQLAlchemy Core)
rel = (
    con.table('orders')
       .filter('total > 100')
       .project('id, customer_id, total')
       .order('total DESC')
       .limit(10)
)
rel.show()    # execute and print
rel.df()      # execute → pandas DataFrame
```

---

## 10. Window Functions and QUALIFY

Full ANSI window function support. `QUALIFY` is a DuckDB/BigQuery/Snowflake extension that filters on window function results without a subquery.

```sql
-- Running total + row number
SELECT
    customer_id,
    order_date,
    total,
    SUM(total) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    )                                                AS running_total,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id ORDER BY order_date DESC
    )                                                AS rn
FROM orders
QUALIFY rn = 1;    -- latest order per customer — no subquery needed

-- T-SQL bridge: without QUALIFY you need:
-- SELECT * FROM (SELECT ..., ROW_NUMBER() OVER (...) AS rn FROM ...) t WHERE t.rn = 1

-- Recursive CTE — full support
WITH RECURSIVE fib(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b FROM fib WHERE n < 10
)
SELECT n, a AS fibonacci FROM fib;
```

---

## 11. Extensions

```sql
-- Extensions are loadable at runtime (downloaded from DuckDB extension repo)
INSTALL httpfs;   LOAD httpfs;    -- remote files: S3, ADLS Gen2, GCS, HTTP
INSTALL spatial; LOAD spatial;   -- geospatial: ST_Distance, ST_Within, etc. (PostGIS-like)
INSTALL fts;     LOAD fts;       -- full-text search (basic — not Lucene-grade)
INSTALL iceberg; LOAD iceberg;   -- Apache Iceberg table format
INSTALL delta;   LOAD delta;     -- Delta Lake tables (read Delta tables from ADLS/S3)
INSTALL azure;   LOAD azure;     -- Azure storage (ADLS Gen2, Blob)
INSTALL json;    LOAD json;      -- extended JSON support (usually auto-loaded)
INSTALL parquet; LOAD parquet;   -- Parquet support (usually auto-loaded)

-- List installed extensions
SELECT * FROM duckdb_extensions();
```

---

## 12. DuckDB vs SQLite vs Spark

| Attribute | DuckDB | SQLite | Spark |
|-----------|--------|--------|-------|
| Orientation | Columnar (OLAP) | Row-based (OLTP) | Columnar (OLAP) |
| Deployment | In-process, single file | In-process, single file | Distributed cluster |
| Data scale | GB–TB (single node) | KB–GB | TB–PB |
| Direct file query | Parquet / CSV / JSON / S3 | No | Yes (with catalog) |
| SQL dialect | PostgreSQL-like + extensions | Most ANSI | Spark SQL (HiveQL base) |
| Concurrent writers | 1 (same as SQLite) | 1 (WAL: 1W + N readers) | Many (Spark partitions) |
| Python integration | Native, zero-copy | Built-in | PySpark (serialization overhead) |
| PIVOT | Auto-detect values | No native PIVOT | Manual CASE/pivot UDF |
| Lambdas in SQL | `list_transform(x, x -> ...)` | No | `transform(array, x -> ...)` |
| Startup overhead | Milliseconds | Microseconds | Seconds to minutes (cluster) |
| Typical use case | Local analytics, ETL, notebook | Embedded OLTP, test fixtures | Big data batch pipelines |

---

## 13. Decision Cheat Sheet

| Use DuckDB when | Use something else when |
|-----------------|------------------------|
| Replacing pandas `.groupby().agg()` chains | Need multi-user concurrent writes → PostgreSQL |
| Local ETL: read CSV/Parquet → transform → write Parquet | Data doesn't fit on a single machine → Spark |
| Testing data pipelines without spinning up Spark | Need a network-accessible server → PostgreSQL |
| Data exploration in Jupyter notebooks | Multi-tenant app with row-level security → PostgreSQL |
| Querying S3/ADLS Parquet without a running cluster | OLTP with many small writes → SQLite or PostgreSQL |
| Lightweight analytics feature inside a Python app | Production web app backend → PostgreSQL |
| Benchmarking / profiling a new dataset | |

---

## 14. Common Confusion Points

**In-process means no remote connections.** You cannot connect from SSMS, a remote app, or a separate process. DuckDB is a library, not a server. If you need a network-accessible database, use PostgreSQL.

**Single writer.** Like SQLite — only one writer at a time. Fine for analytics workloads. Not fine for concurrent write-heavy transactional workloads.

**No user permissions.** No concept of users, roles, or grants. It's single-user. Not for multi-tenant applications.

**PIVOT auto-detection requires a full scan.** DuckDB's `PIVOT ON col` scans the entire dataset to discover distinct values before pivoting. On large files, this is two passes. SQL Server/BigQuery require an explicit `IN` list precisely to avoid this scan.

**QUALIFY is not T-SQL.** T-SQL has no `QUALIFY` clause. The equivalent requires a subquery or CTE with `ROW_NUMBER()`.

**Lambda syntax `x -> expr` is DuckDB-specific.** Not standard SQL. Spark has `transform(array, x -> ...)` with similar syntax. T-SQL has no array lambdas.

**File path strings are single-quoted.** `SELECT * FROM 'file.parquet'` — the single-quoted string is interpreted as a file path. DuckDB detects the extension to choose the reader.

**Zero-copy pandas interop caveat.** When DuckDB queries a pandas DataFrame, it reads the Python object's memory directly — no copy. Modifying the DataFrame while a DuckDB query is running against it is undefined behavior.

**SUMMARIZE is a DuckDB convenience operator**, not standard SQL. It does the equivalent of running `MIN`, `MAX`, `COUNT`, `AVG`, `STDDEV`, `PERCENTILE_CONT` for every column in one pass.

**DuckDB is not a replacement for PostgreSQL.** No replication, no network server, no multi-user access, no row-level security. It is the right tool for analytics and exploration; PostgreSQL is the right tool for a production application database.
