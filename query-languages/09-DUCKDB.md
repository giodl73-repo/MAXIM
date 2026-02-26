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

Bridge: think of SQLite → DuckDB as same deployment model (in-process, single file,
no server), opposite workload orientation (OLTP row-store vs OLAP column-store).
```

### Bridges to Known Territory

**SQLite vs DuckDB — deployment model is identical, workload orientation is opposite.**
SQLite: in-process, single `.db` file, row-oriented, OLTP. DuckDB: in-process, single `.duckdb` file (or in-memory), column-oriented, OLAP. You don't install a server process for either. DuckDB is the right answer whenever SQLite is the right deployment model but the workload is analytical.

**SQL Server vs DuckDB — server process vs embedded library.**
SQL Server is a Windows/Linux service with a network port. You connect to it over TDS from a separate process. DuckDB is a library you link directly into your application — same process, no network, no service account, no server management. The DuckDB engine lives inside your Python/C#/Node process the same way the CLR JIT lives inside a .NET process.

**ADF + ADLS Gen2 → DuckDB — inspect pipeline outputs without spinning up a cluster.**
ADF Data Flows and Copy Activities routinely sink Parquet files to ADLS Gen2 container paths. Once those files land, you can point DuckDB directly at them for ad-hoc validation, schema inspection, and exploratory queries — no Spark cluster, no Synapse, no import step. This is the fastest feedback loop for pipeline debugging: `SELECT * FROM read_parquet('az://container/output/*.parquet') LIMIT 100`. See Section 4 for ADLS Gen2 setup.

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

vs pandas: pandas iterates over NumPy arrays at Python interpreter speed (one
          operation dispatched per Python bytecode); DuckDB executes compiled
          C++ SIMD loops that process 2048 values per CPU instruction. The
          10–100× advantage over pandas on aggregation workloads comes from
          eliminating the Python dispatch overhead, not from columnar layout alone.
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

### ADF + ADLS Gen2 Integration — Querying Pipeline Output Directly

ADF Copy Activities and Data Flows typically sink Parquet to ADLS Gen2 container paths like `abfss://container@account.dfs.core.windows.net/output/year=2024/month=01/`. DuckDB's `azure` extension reads those files directly via the Blob REST API — no Spark, no Synapse Analytics SQL pool, no import.

```sql
-- One-time setup per session
INSTALL azure;
LOAD azure;

-- Option 1: connection string (dev/local use)
SET azure_storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=myadls;AccountKey=...';

-- Option 2: service principal (CI / production scripts)
SET azure_tenant_id             = '<tenant-guid>';
SET azure_client_id             = '<app-registration-client-id>';
SET azure_client_secret         = '<secret>';

-- Query ADF pipeline output — glob picks up all Parquet files in the sink path
SELECT * FROM read_parquet('azure://container/output/year=2024/month=01/*.parquet') LIMIT 100;

-- Hive-style partition pruning: DuckDB reads partition columns from directory names
-- If ADF wrote year=2024/month=01/day=15/*.parquet, DuckDB surfaces year/month/day as columns
SELECT year, month, COUNT(*), SUM(amount)
FROM read_parquet('azure://container/output/**/*.parquet', hive_partitioning = true)
WHERE year = 2024 AND month = 1
GROUP BY year, month;

-- Schema validation: confirm ADF output has expected columns and types
DESCRIBE SELECT * FROM read_parquet('azure://container/output/latest/*.parquet');

-- Row count check after pipeline run (milliseconds — no cluster required)
SELECT COUNT(*) FROM 'azure://container/output/latest/*.parquet';
```

**DuckDB vs ADF Copy Activity for reading Parquet:** ADF Copy Activity is the right tool for pipeline orchestration and data movement at scale. DuckDB is the right tool for the engineer validating that the pipeline produced the right output — interactive SQL directly on the sink files, no provisioning, results in seconds.

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

### DuckDB-WASM — In-Browser Deployment

DuckDB compiles to WebAssembly. The same columnar execution engine that runs in Python or C# runs inside a browser tab — no server, no backend query service, no network round-trip for query execution. This is architecturally distinct from every other SQL engine: a full OLAP engine executing client-side in the browser's WASM sandbox.

```javascript
// DuckDB-WASM via npm
// npm install @duckdb/duckdb-wasm

import * as duckdb from '@duckdb/duckdb-wasm';

const JSDELIVR_BUNDLES = duckdb.getJsDelivrBundles();
const bundle = await duckdb.selectBundle(JSDELIVR_BUNDLES);

const worker_url = URL.createObjectURL(
    new Blob([`importScripts("${bundle.mainWorker!}");`], { type: 'text/javascript' })
);
const worker = new Worker(worker_url);
const logger = new duckdb.ConsoleLogger();
const db     = await duckdb.createDuckDB(bundle, logger, new duckdb.AsyncDuckDB(logger, worker));
await db.instantiate(bundle.mainModule, bundle.pthreadWorker);

const conn = await db.connect();

// Query a local File object dropped by the user — no upload, no server
await db.registerFileHandle('uploaded.parquet', fileObject, duckdb.DuckDBDataProtocol.BROWSER_FILEREADER, true);
const result = await conn.query(`SELECT * FROM 'uploaded.parquet' LIMIT 10`);
```

**Use cases:** Observable notebooks (DuckDB-WASM is built-in), embedded analytics dashboards that process user-uploaded files entirely client-side, data exploration tools that need zero backend infrastructure. The constraint: WASM runs single-threaded in most browsers (no SIMD parallelism across threads), so performance is lower than native DuckDB on equivalent hardware — but it is still orders of magnitude faster than JavaScript-based alternatives for analytical queries.

---

## 12. Azure / BI Bridges

### Power BI DirectQuery → DuckDB

Power BI has two data access modes: Import (data loaded into VertiPaq in-memory) and DirectQuery (query sent live to the source on every visual interaction). DuckDB fits into the BI tool conversation at two levels:

**DuckDB as a local query engine under a BI tool.** DuckDB exposes an ADBC (Arrow Database Connectivity) driver and an ODBC/JDBC driver. A BI tool that supports ODBC can connect to DuckDB — but since DuckDB is in-process and single-file, "connecting" means the BI tool opens the `.duckdb` file directly within its own process. Power BI Desktop does not natively support a DuckDB connector today, but the Python/R script visual and Power Query custom connectors can invoke DuckDB queries and return results as Arrow or pandas DataFrames.

**MotherDuck — DuckDB with cloud storage.** MotherDuck is a managed cloud service (SaaS) that extends DuckDB with a shared catalog and remote storage. You attach a MotherDuck database to a local DuckDB session: `ATTACH 'md:my_database'`. Queries can reference both local files and MotherDuck-hosted tables in the same SQL statement. This is the closest DuckDB analog to a DirectQuery source — a lightweight cloud-hosted query engine you can point a BI tool at, without a full data warehouse.

**The practical pattern — DuckDB + local Parquet as Power BI Desktop alternative.**
For ad-hoc analysis where you have Parquet files (from ADF, Synapse, or any export) and no Azure connection:

```python
import duckdb, pandas as pd

# Load directly into pandas for Power BI-style pivot analysis
result = duckdb.sql("""
    SELECT
        YEAR(order_date)  AS year,
        MONTH(order_date) AS month,
        region,
        SUM(revenue)      AS total_revenue,
        COUNT(*)          AS order_count
    FROM read_parquet('data/orders/*.parquet', hive_partitioning = true)
    WHERE YEAR(order_date) = 2024
    GROUP BY 1, 2, 3
    ORDER BY 1, 2, 3
""").df()

# result is a pandas DataFrame — pipe to matplotlib, seaborn, or plotly
# for ad-hoc analysis that would otherwise require Power BI + a connected dataset
```

The pattern replaces the Power BI Import workflow (load → model → visualize) with a script that runs in seconds on local files, with no licensing, no gateway, and no scheduled refresh cycle.

---

### SSAS VertiPaq (Columnar/In-Memory) → DuckDB Columnar Execution

Both SSAS Tabular (VertiPaq) and DuckDB are columnar engines. The architecture is similar in some dimensions and diverges sharply in others.

```
VertiPaq (SSAS Tabular / Power BI Import):
  Source DB / ADLS / ...
       │
       ▼  full data refresh
  VertiPaq in-memory store
  ┌──────────────────────────────────────────────────────┐
  │  Column segments, compressed, dictionary-encoded     │
  │  Run-length encoding on sorted segments              │
  │  All data in RAM — queries read from memory, not disk│
  └──────────────────────────────────────────────────────┘
       │
       ▼  DAX / MDX query
  Formula Engine → Storage Engine → result

DuckDB:
  Parquet / CSV / ADLS / S3 files (on disk or remote)
       │
       ▼  query-time column read, no persistent cache
  ┌──────────────────────────────────────────────────────┐
  │  Vectorized columnar execution (SIMD, 2048-row batch)│
  │  Lightweight compression on columnar data in Parquet │
  │  Data NOT fully loaded into RAM — streaming reads    │
  └──────────────────────────────────────────────────────┘
       │
       ▼  SQL query
  Optimizer → Physical Plan → result
```

**What they share:** dictionary encoding, run-length encoding on sorted data, vectorized operations that process multiple values per CPU instruction. Both use compression aggressively to reduce memory bandwidth.

**Key difference — persistent cache vs direct file reads.**
VertiPaq is an in-memory cache layer that sits between the source and the query engine. The data is materialized into VertiPaq on import/refresh; subsequent queries read entirely from memory (no disk I/O during query execution). DuckDB reads from files at query time — there is no persistent in-memory cache. VertiPaq is faster on repeated queries against the same dataset because the data is already decompressed in RAM. DuckDB is faster for queries against data that changes frequently, because the files are always current — no refresh cycle.

**Power BI Import mode mental model:**
- Import = VertiPaq in memory = fast queries, data staleness = time since last refresh
- DuckDB = query files directly = always current, speed = file I/O bound (fast on local NVMe or Parquet on ADLS with azure extension)

For a 50 GB dataset: VertiPaq (Power BI Import) requires a machine with 50+ GB RAM. DuckDB streams the relevant columns and can process a 50 GB Parquet file on a 16 GB machine because it never materializes the full dataset.

---

### Parquet + ADLS Gen2 — Full Integration Reference

DuckDB is a first-class citizen in an Azure data engineering stack. The `azure` extension wraps the Azure Blob Storage REST API and exposes it as a DuckDB virtual filesystem.

```sql
-- First-time setup
INSTALL azure;
LOAD azure;

-- Auth option 1: connection string (development)
SET azure_storage_connection_string =
    'DefaultEndpointsProtocol=https;AccountName=myadls;AccountKey=<key>;EndpointSuffix=core.windows.net';

-- Auth option 2: service principal (CI / automated scripts)
SET azure_tenant_id     = '<tenant-guid>';
SET azure_client_id     = '<app-registration-client-id>';
SET azure_client_secret = '<secret>';

-- Auth option 3: managed identity (when running on Azure VM / ACI / AKS)
-- No explicit credentials — uses the VM's assigned identity
SET azure_use_managed_identity = true;

-- ── Basic reads ──────────────────────────────────────────────────────────────

-- Single file
SELECT * FROM read_parquet('azure://mycontainer/exports/orders_2024.parquet');

-- Glob: all Parquet files in directory
SELECT * FROM read_parquet('azure://mycontainer/exports/*.parquet');

-- ── Hive-style partitioned directories (ADF standard sink layout) ────────────

-- ADF typically writes: container/pipeline-output/year=2024/month=01/day=15/*.parquet
-- hive_partitioning = true surfaces year/month/day as virtual columns
SELECT year, month, SUM(revenue)
FROM read_parquet(
    'azure://mycontainer/pipeline-output/**/*.parquet',
    hive_partitioning = true
)
WHERE year = 2024
GROUP BY year, month
ORDER BY year, month;

-- DuckDB pushes the year/month predicates into the file scan — it reads only the
-- matching partition directories, skipping the rest entirely (partition pruning).
-- Same behavior as Spark partition pruning or Synapse serverless predicate pushdown.

-- ── Practical ADF workflow integration ──────────────────────────────────────

-- 1. Confirm ADF pipeline wrote expected row count
SELECT COUNT(*) AS row_count
FROM 'azure://mycontainer/pipeline-output/year=2024/month=01/**/*.parquet';

-- 2. Schema check — did ADF output the right column types?
DESCRIBE SELECT * FROM 'azure://mycontainer/pipeline-output/latest/*.parquet';

-- 3. Data quality spot check
SELECT customer_id, COUNT(*) AS cnt
FROM 'azure://mycontainer/pipeline-output/latest/*.parquet'
GROUP BY customer_id
HAVING COUNT(*) > 1   -- check for duplicates
ORDER BY cnt DESC
LIMIT 20;

-- 4. Cross-partition delta — rows in Jan but not Feb (disappeared records)
SELECT a.customer_id
FROM read_parquet('azure://mycontainer/output/year=2024/month=01/*.parquet') a
LEFT JOIN read_parquet('azure://mycontainer/output/year=2024/month=02/*.parquet') b
    ON a.customer_id = b.customer_id
WHERE b.customer_id IS NULL;
```

**Comparison to ADF Copy Activity reading Parquet:** ADF Copy Activity is orchestrated, monitored, lineage-tracked, and integrated into Data Factory pipelines — the right tool for moving data between systems at scale. DuckDB with the azure extension is the right tool for the data engineer running ad-hoc SQL directly on those same files — validation, debugging, and exploration without provisioning compute.

---

## 13. DuckDB vs SQLite vs Spark

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

## 14. Decision Cheat Sheet

| Use DuckDB when | Use something else when |
|-----------------|------------------------|
| Replacing pandas `.groupby().agg()` chains | Need multi-user concurrent writes → PostgreSQL |
| Local ETL: read CSV/Parquet → transform → write Parquet | Data doesn't fit on a single machine → Spark |
| Testing data pipelines without spinning up Spark | Need a network-accessible server → PostgreSQL |
| Data exploration in Jupyter notebooks | Multi-tenant app with row-level security → PostgreSQL |
| Querying S3/ADLS Parquet without a running cluster | OLTP with many small writes → SQLite or PostgreSQL |
| Lightweight analytics feature inside a Python app | Production web app backend → PostgreSQL |
| Inspecting / validating ADF pipeline Parquet output on ADLS Gen2 | Orchestrated multi-stage pipeline movement → stay in ADF |
| Benchmarking / profiling a new dataset | |

---

## 15. Common Confusion Points

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
