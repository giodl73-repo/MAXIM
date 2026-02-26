# Cloud Analytical SQL — BigQuery, Snowflake, Databricks, Synapse

Cloud data warehouses replaced on-prem Hadoop clusters and SQL Server Analysis Services. The query language is SQL with analytical extensions — but the execution model is distributed columnar at petabyte scale. These four dominate: BigQuery (Google), Snowflake (AWS/Azure/GCP), Databricks (Delta Lake), Synapse Analytics (Azure). All speak SQL. All have proprietary extensions.

---

## 1. BIG PICTURE — The Cloud DW Landscape

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Data Warehouse Evolution                             │
│                                                                              │
│  ON-PREM ERA (the old world)                                                │
│  ──────────────────────────                                                  │
│  SQL Server DW ──► SSIS (ETL) ──► SSAS (cubes/tabular) ──► SSRS / Excel    │
│  Fixed capacity. Scale up (bigger box). MOLAP cubes pre-aggregate.          │
│                                                                              │
│  HADOOP ERA                                                                  │
│  ──────────                                                                  │
│  HDFS ──► MapReduce ──► Hive ──► Impala / Presto                            │
│  Cheap commodity hardware. Disk-based. Slow. Good for raw archive.          │
│                                                                              │
│  CLOUD DW ERA (now)                                                          │
│  ──────────────────                                                          │
│  Object Storage (S3 / ADLS Gen2 / GCS)                                      │
│       │                                                                      │
│       ├──► BigQuery (Google)       ─ serverless, on-demand                  │
│       ├──► Snowflake                ─ virtual warehouses, multi-cloud        │
│       ├──► Databricks (Delta Lake) ─ Spark + SQL unified                    │
│       └──► Synapse Analytics       ─ Azure-native, T-SQL familiar           │
│                                                                              │
│  KEY SHIFT: Storage and compute are SEPARATED and scaled independently.     │
│  No more "buy bigger SQL Server." Pay for compute when you use it.          │
│                                                                              │
│  MODERN DATA PATTERN (Medallion Architecture)                               │
│  ─────────────────────────────────────────────                              │
│  Raw Sources ──► BRONZE (raw) ──► SILVER (clean) ──► GOLD (biz layer)      │
│                                                            │                 │
│                                              Power BI / Tableau / Looker    │
│                                              ML / AI / Feature Stores       │
└──────────────────────────────────────────────────────────────────────────────┘
```

Bridge: SSIS → ADF/dbt for ingestion. SSAS tabular → Gold layer in cloud DW. SSRS → Power BI Direct Lake.

---

## 2. WHY COLUMNAR STORAGE IS FAST

SQL Server stores rows contiguously on 8 KB pages. Analytical reads that touch 3 columns from a 200-column table must still read every page — all 200 columns. Columnar storage inverts this: each column is stored in its own contiguous chunk. Reading 3 columns reads 3 chunks, proportional to columns not rows.

```
ROW-ORIENTED (SQL Server heap / clustered index page)
─────────────────────────────────────────────────────
Page: [id|name|email|addr|dob|dept|salary|hire_date|mgr_id|...]
      [id|name|email|addr|dob|dept|salary|hire_date|mgr_id|...]
      ...

Query: SELECT dept, SUM(salary) FROM employees GROUP BY dept
 ► Must read EVERY column on EVERY page even though only 2 columns needed
 ► I/O = O(rows × row_width)

COLUMNAR (Parquet / cloud DW internal format)
─────────────────────────────────────────────
Column chunk "dept":   [Sales|Eng|Sales|Eng|HR|Sales|...]   ← compressed RLE
Column chunk "salary": [80000|120000|85000|...]              ← delta-encoded
Column chunks skipped: name, email, addr, dob, hire_date, mgr_id, ...

 ► I/O = O(rows × 2_columns_wide)   — read only what you touched
 ► This is projection pushdown.
```

### Parquet Encoding Tricks

Parquet applies multiple compression passes within each column chunk:

| Technique | What it does | Benefit |
|---|---|---|
| Dictionary encoding | Replace repeated string values with small int codes | "United States" → 2 bytes instead of 13 |
| RLE (Run-Length Encoding) | Repeated consecutive values: `[Sales, Sales, Sales, Sales]` → `(Sales × 4)` | Sorted data compresses 10–50x |
| Bit-packing | Store small-range integers in fewer bits (status enum 0–3 needs 2 bits not 32) | Dense integer columns shrink dramatically |
| Delta encoding | Store differences between consecutive sorted values | Timestamps and IDs: store deltas, not absolutes |
| Snappy / Zstd | Final byte-level compression on top | 3–5x additional |

### Row Group Skipping (Predicate Pushdown)

Parquet files are split into row groups (~128 MB). Each row group stores per-column min/max statistics:

```
Row group 0: order_date min=2023-01-01, max=2023-03-31   ← skip (query asks for 2024)
Row group 1: order_date min=2023-04-01, max=2023-06-30   ← skip
Row group 2: order_date min=2024-01-01, max=2024-03-31   ← READ
Row group 3: order_date min=2024-04-01, max=2024-12-31   ← skip (no match)

Query: WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31'
 ► Engine reads min/max from footer (tiny) before touching column data
 ► Skips 3 of 4 row groups — reads 25% of the file
 ► Predicate pushed down into the file reader, not evaluated row-by-row after full read
```

SQL Server equivalent: partition elimination + column store segment elimination. Parquet row group skipping is the same concept — statistics-driven I/O avoidance — but at the file format level rather than the index level.

SSAS MOLAP pre-aggregated so queries never hit raw data. Cloud DWs skip raw data via statistics — no pre-aggregation required. You get ad-hoc query performance without defining cubes.

## 3. PLATFORM COMPARISON

| Attribute            | BigQuery               | Snowflake                    | Databricks SQL          | Synapse Analytics          |
|----------------------|------------------------|------------------------------|-------------------------|----------------------------|
| Creator              | Google                 | Snowflake Inc                | Databricks              | Microsoft                  |
| Pricing model        | Serverless on-demand   | Virtual warehouse (credits)  | SQL warehouse (DBUs)    | DWU / serverless DPU       |
| Storage              | Google Cloud Storage   | Internal (S3/ADLS/GCS)       | Delta Lake on ADLS / S3 | ADLS Gen2                  |
| SQL dialect          | Standard SQL (ANSI)    | Snowflake SQL                | Spark SQL / Delta       | T-SQL subset               |
| Streaming ingest     | Pub/Sub, Storage Write | Snowpipe (S3/Event Grid)     | Delta Streaming / Kafka | Event Hubs / Synapse Link  |
| Ecosystem            | dbt, Looker native     | dbt, Sigma, Cortex AI        | dbt, MLflow, Unity Cat  | Power BI native, Purview   |
| Unique strength      | Petabyte serverless, ML.PREDICT | Time travel, data sharing | Python + SQL unified, ML | Azure-native, T-SQL, Purview |
| Multi-cloud          | No (GCP only)          | Yes (AWS, Azure, GCP)        | Yes                     | No (Azure only)            |

### How Each Platform Actually Executes a Query

All four platforms use Massively Parallel Processing (MPP) — the query is split across many nodes that work in parallel. The details of how nodes are sized, allocated, and priced differ:

**Snowflake Virtual Warehouses**
A virtual warehouse is a cluster of EC2/VM nodes. Sizing doubles node count:

```
XS = 1 node   S = 2 nodes   M = 4 nodes   L = 8 nodes   XL = 16 nodes   2XL = 32 nodes
```

Doubling warehouse size halves wall-clock time for compute-bound queries — but only if the query has enough parallelism to use extra nodes. A sequential query (forced ORDER BY on a tiny dataset) gets no benefit from XL vs XS. Bottleneck: I/O-bound queries benefit from more nodes (more network bandwidth to storage). Compute-bound queries (heavy aggregations, complex joins) benefit from larger nodes. The "right" size is workload-dependent; Snowflake multi-cluster mode auto-scales for concurrent user load.

**BigQuery Slot Allocation**
BigQuery has no cluster to size. A "slow query" is a slot-starved query. Slots are vCPUs in Google's shared pool:

- On-demand: dynamic slot allocation, no reservation — competing with other GCP customers
- Capacity (flat-rate): reserved slots guarantee minimum parallelism
- A query that should take 10 seconds at 2000 slots takes 100 seconds at 200 slots — not a data problem, a compute allocation problem

This is the opposite mental model from SQL Server where compute is always available if the server is up.

**Synapse Dedicated Pool — Distribution**
Synapse dedicated pool distributes table rows across compute nodes at table creation. The distribution strategy determines whether joins shuffle data across the network:

```sql
-- HASH distribution: rows with same key → same node
-- Eliminates shuffle if the join partner is on the same distribution key
CREATE TABLE orders (
    order_id    BIGINT,
    customer_id BIGINT,
    total       DECIMAL(12,2)
) WITH (DISTRIBUTION = HASH(customer_id));  -- co-locate with customers table

-- ROUND_ROBIN: rows spread evenly, no key affinity
-- Good for staging tables; bad for joins (always shuffles)
CREATE TABLE stage_orders WITH (DISTRIBUTION = ROUND_ROBIN);

-- REPLICATE: entire table copied to every node
-- Use for small dimension tables (avoids shuffle in star-schema joins)
CREATE TABLE dim_product WITH (DISTRIBUTION = REPLICATE);
```

Data skew on HASH distribution is the Synapse equivalent of SQL Server partition skew: if 80% of orders have customer_id=1 (a test account), one node holds 80% of the data. All queries against that customer serialize on one node while others sit idle. Fix: choose a high-cardinality, evenly distributed key.

---

## 4. PARTITIONING AND CLUSTERING

The performance foundation. Without it, full table scans at every query.

### BigQuery

```sql
-- PARTITION BY: limits bytes scanned (BigQuery charges per byte)
CREATE TABLE sales.orders
PARTITION BY DATE(order_timestamp)           -- date partition (most common)
-- alternatives:
-- PARTITION BY RANGE BUCKET(customer_id, 10) -- integer range (10 buckets)
-- PARTITION BY _PARTITIONDATE               -- ingestion time (implicit)
OPTIONS (
    partition_expiration_days = 365           -- auto-delete old partitions
)
AS SELECT ...;

-- CLUSTER BY: sorts data within partitions (co-locate similar values)
-- Up to 4 columns. Applied after partitioning.
CREATE TABLE sales.orders
PARTITION BY DATE(order_timestamp)
CLUSTER BY customer_id, product_id
AS SELECT ...;

-- Only scans the matching partition → fewer bytes → lower cost + faster
SELECT * FROM sales.orders
WHERE DATE(order_timestamp) = '2024-01-15';  -- partition pruning

-- Inspect partition metadata
SELECT * FROM sales.INFORMATION_SCHEMA.PARTITIONS WHERE table_name = 'orders';
```

### Snowflake

```sql
-- Snowflake uses automatic micro-partitioning (~50–500 MB chunks, compressed)
-- Explicit CLUSTER BY for frequently filtered columns (when auto-clustering is insufficient)

CREATE TABLE orders (
    order_id    BIGINT,
    order_date  DATE,
    customer_id BIGINT,
    total       FLOAT
) CLUSTER BY (order_date, customer_id);

-- Check clustering quality (returns overlap %, depth info)
SELECT SYSTEM$CLUSTERING_INFORMATION('orders', '(order_date, customer_id)');

-- Reclustering when new data disrupts clustering depth
ALTER TABLE orders RECLUSTER;

-- Automatic clustering (Snowflake-managed, incurs compute cost)
ALTER TABLE orders ENABLE AUTOMATIC CLUSTERING;
```

---

## 5. QUALIFY — Window Function Filter

Not in ANSI SQL. Not in PostgreSQL. Not in T-SQL. BigQuery, Snowflake, Databricks all support it.

```sql
-- The problem: window function results are not available in WHERE
-- Old pattern (subquery required):
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM orders
) WHERE rn = 1;

-- QUALIFY (cloud DW extension — eliminates the outer query):
SELECT *,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
FROM orders
QUALIFY rn = 1;

-- More QUALIFY patterns:
-- Top 3 earners per department
QUALIFY RANK() OVER (PARTITION BY dept ORDER BY salary DESC) <= 3

-- Deduplicate: keep only rows where status changed from previous
QUALIFY LAG(status) OVER (PARTITION BY user_id ORDER BY ts) != status

-- Latest record per key (most common use case)
QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
```

---

## 6. PIVOT AND UNPIVOT

```sql
-- BigQuery PIVOT (added 2021)
SELECT *
FROM sales
PIVOT (
    SUM(revenue)  AS revenue,
    COUNT(*)      AS orders
    FOR quarter IN ('Q1', 'Q2', 'Q3', 'Q4')
);
-- Generates columns: Q1_revenue, Q1_orders, Q2_revenue, Q2_orders, ...

-- Snowflake PIVOT
SELECT *
FROM (SELECT product, quarter, revenue FROM sales)
PIVOT (SUM(revenue) FOR quarter IN ('Q1', 'Q2', 'Q3', 'Q4'))
    AS p (product, q1_rev, q2_rev, q3_rev, q4_rev);

-- Databricks PIVOT
SELECT *
FROM sales
PIVOT (SUM(revenue) FOR quarter IN ('Q1' AS q1_rev, 'Q2' AS q2_rev, 'Q3' AS q3_rev, 'Q4' AS q4_rev));

-- UNPIVOT — wide → tall (all four platforms)
SELECT product, quarter, revenue
FROM sales_wide
UNPIVOT (revenue FOR quarter IN (q1_revenue, q2_revenue, q3_revenue, q4_revenue));
```

---

## 7. SEMI-STRUCTURED DATA

### BigQuery — ARRAY and STRUCT (native, not JSON strings)

```sql
-- BigQuery stores nested/repeated fields natively — no JSON parsing overhead
-- UNNEST explodes ARRAY column to rows (= LATERAL JOIN)
SELECT
    order_id,
    item.product_id,
    item.quantity
FROM orders
CROSS JOIN UNNEST(line_items) AS item;    -- line_items is ARRAY<STRUCT<...>>

-- STRUCT field access (dot notation)
SELECT customer.address.city,
       customer.address.state
FROM orders;

-- Aggregate into arrays
SELECT
    customer_id,
    ARRAY_AGG(product_id ORDER BY order_date) AS product_history,
    ARRAY_AGG(STRUCT(product_id, total)) AS order_structs
FROM orders
GROUP BY customer_id;

-- Inline array construction
SELECT ARRAY[1, 2, 3] AS nums;
SELECT STRUCT('Alice' AS name, 30 AS age) AS person;
```

### Snowflake — VARIANT type

```sql
-- VARIANT: any JSON/XML/Avro stored natively
CREATE TABLE events (
    id   BIGINT,
    data VARIANT
);

-- Path notation with :: cast operator
SELECT
    data:user:name::STRING         AS username,
    data:user:id::INTEGER          AS user_id,
    data:items[0]:price::FLOAT     AS first_item_price,
    data:metadata:created_at::TIMESTAMP AS created_at
FROM events;

-- FLATTEN: lateral explode for nested arrays (= UNNEST for VARIANT)
SELECT
    e.id,
    f.value:product_id::STRING  AS product_id,
    f.value:quantity::INTEGER   AS quantity
FROM events e,
     LATERAL FLATTEN(input => e.data:items) f;

-- PARSE_JSON for inline construction
SELECT PARSE_JSON('{"name":"Alice","score":99}'):name::STRING;

-- Object construction
SELECT OBJECT_CONSTRUCT('name', username, 'email', email) AS user_json FROM users;
```

---

## 8. TIME TRAVEL

### Snowflake (up to 90 days, configurable per table)

```sql
-- Query historical state
SELECT * FROM orders AT (OFFSET => -3600);                  -- 1 hour ago (seconds)
SELECT * FROM orders AT (TIMESTAMP => '2024-01-15 10:00');  -- specific timestamp
SELECT * FROM orders BEFORE (STATEMENT => '8e5d0ca9-005b-...');  -- before a query ran

-- Diff current vs 24 hours ago
SELECT id FROM orders
EXCEPT
SELECT id FROM orders AT (OFFSET => -86400);                -- records added in last 24h

-- Zero-copy cloning (only stores delta from source)
CREATE TABLE orders_backup CLONE orders;                        -- current state
CREATE TABLE orders_jan CLONE orders AT (TIMESTAMP => '2024-01-31 23:59:59');

-- Restore dropped table (within retention window)
UNDROP TABLE orders;

-- Configure retention
ALTER TABLE orders SET DATA_RETENTION_TIME_IN_DAYS = 30;    -- max 90 for Enterprise
```

### Databricks Delta Lake

```sql
-- OPTIMIZE + Z-ORDER: compact small files and co-locate related data
-- Run after streaming/micro-batch ingest creates many small files
OPTIMIZE orders;                                    -- compact only
OPTIMIZE orders ZORDER BY (customer_id, order_date); -- compact + spatial sort

-- Z-ordering explained:
-- After OPTIMIZE, data files covering related (customer_id, order_date) pairs
-- are physically co-located. The data skipping index (min/max per file) then
-- eliminates files during predicate evaluation before any column data is read.
--
-- Partition vs Z-order (these are complementary, not competing):
--   Partition: directory-level elimination (year=2024/month=01/)
--   Z-order:   file-level elimination WITHIN a partition
--
-- Use partition for: low-cardinality, query-critical columns (date, region)
-- Use Z-order for:   high-cardinality columns (customer_id, product_id)
--
-- Analogy: partition = bookshelf section (Fiction / NonFiction)
--          Z-order   = sorted arrangement within the section

-- VACUUM: permanently delete data files no longer referenced by the log
-- This is the only way to reclaim storage from old versions
VACUUM orders;                 -- uses table default (7 days = 168 hours)
VACUUM orders RETAIN 168 HOURS; -- explicit 7-day retention

-- VACUUM + time travel tradeoff:
-- Not vacuuming: time travel works arbitrarily far back, but storage grows unbounded
-- Vacuuming aggressively: storage is clean, but time travel limited to retention window
-- Default 7-day retention is the right balance for most operational tables
-- Audit/compliance tables: increase retention (ALTER TABLE SET TBLPROPERTIES 'delta.deletedFileRetentionDuration')
```

```sql
-- Time travel via version or timestamp
SELECT * FROM orders VERSION AS OF 5;
SELECT * FROM orders TIMESTAMP AS OF '2024-01-15 00:00:00';

-- Restore to a previous version
RESTORE TABLE orders TO VERSION AS OF 5;
RESTORE TABLE orders TO TIMESTAMP AS OF '2024-01-15 10:00:00';

-- Full history of all operations
DESCRIBE HISTORY orders;
-- Columns: version, timestamp, userId, operation, operationParameters,
--          operationMetrics (numFiles, numOutputRows, etc.)
```

---

## 9. MERGE INTO / UPSERT

The critical pattern for CDC (Change Data Capture) pipelines. All four platforms support ANSI MERGE.

```sql
-- Databricks / Delta Lake MERGE (most feature-complete)
MERGE INTO gold.customers AS target
USING (
    SELECT customer_id, name, email, MAX(updated_at) AS updated_at
    FROM silver.customer_updates
    GROUP BY customer_id, name, email
) AS source
ON target.customer_id = source.customer_id
WHEN MATCHED AND source.updated_at > target.updated_at THEN
    UPDATE SET
        name       = source.name,
        email      = source.email,
        updated_at = source.updated_at
WHEN NOT MATCHED THEN
    INSERT (customer_id, name, email, created_at, updated_at)
    VALUES (source.customer_id, source.name, source.email, NOW(), source.updated_at)
WHEN NOT MATCHED BY SOURCE THEN    -- rows in target with no source match
    DELETE;                         -- supported in Delta Lake; also Snowflake

-- BigQuery MERGE (same ANSI core, limited NOT MATCHED BY SOURCE)
MERGE INTO `project.dataset.customers` AS target
USING `project.dataset.updates` AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN
    UPDATE SET name = source.name, email = source.email
WHEN NOT MATCHED THEN
    INSERT VALUES(source.customer_id, source.name, source.email);

-- Snowflake MERGE (+ WHEN NOT MATCHED BY SOURCE for soft deletes)
MERGE INTO customers AS target
USING updates AS source
ON target.id = source.id
WHEN MATCHED THEN
    UPDATE SET name = source.name
WHEN NOT MATCHED THEN
    INSERT (id, name) VALUES (source.id, source.name)
WHEN NOT MATCHED BY SOURCE THEN
    UPDATE SET is_deleted = TRUE, deleted_at = CURRENT_TIMESTAMP();
```

---

## 10. MATERIALIZED VIEWS AND CONTINUOUS AGGREGATION

```sql
-- BigQuery materialized view — auto-refreshed incrementally, zero query overhead
CREATE MATERIALIZED VIEW sales.daily_revenue
OPTIONS (
    enable_refresh = true,
    refresh_interval_minutes = 30
)
AS
SELECT
    DATE(order_timestamp)  AS order_date,
    SUM(total)             AS revenue,
    COUNT(*)               AS order_count
FROM sales.orders
GROUP BY 1;
-- BQ rewrites queries against the base table to use this MV automatically

-- Snowflake dynamic tables (2023+) — declarative continuous pipelines
CREATE DYNAMIC TABLE gold.daily_revenue
    TARGET_LAG = '1 hour'           -- how stale is acceptable
    WAREHOUSE  = compute_wh
AS
SELECT order_date, SUM(total) AS revenue
FROM silver.orders
GROUP BY order_date;
-- Snowflake manages refresh scheduling; handles base table changes

-- Databricks materialized views (Unity Catalog)
CREATE MATERIALIZED VIEW gold.daily_revenue
AS
SELECT order_date, SUM(total) AS revenue
FROM silver.orders
GROUP BY order_date;

-- Synapse — materialized views with distribution
CREATE MATERIALIZED VIEW gold.daily_revenue
WITH (DISTRIBUTION = ROUND_ROBIN)   -- or HASH(order_date) for colocation
AS
SELECT order_date, SUM(total) AS revenue
FROM silver.orders
GROUP BY order_date;
```

---

## 11. DBT INTEGRATION — The Standard Transformation Layer

### Power Query M → Analytical SQL Bridge

Power Query M and SQL express the same transformations with radically different evaluation models. M is a functional, lazy, step-chained language where each step is a named transformation applied to a table value. SQL is declarative and set-theoretic — you describe the result shape, not the steps.

| Power Query M | SQL equivalent | Mental model shift |
|---|---|---|
| `Table.Group(tbl, {"dept"}, {{"count", each Table.RowCount(_), type number}})` | `SELECT dept, COUNT(*) FROM tbl GROUP BY dept` | M folds a function over each group; SQL declares the aggregation |
| `Table.AddColumn(tbl, "adjusted", each [salary] * 1.1)` | `SELECT *, salary * 1.1 AS adjusted FROM tbl` | M applies a row function; SQL computes a column expression |
| `Table.AddColumn(tbl, "rank", each ...)` with partition logic | `SELECT *, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank` | M has no native window functions — you'd write a nested group; SQL window functions are idiomatic here |
| `Table.NestedJoin(orders, {"cust_id"}, customers, {"id"}, "cust", JoinKind.LeftOuter)` | `SELECT * FROM orders LEFT JOIN customers ON orders.cust_id = customers.id` | M returns a column of tables; SQL returns a flat result |
| `List.Accumulate(amounts, 0, (acc, x) => acc + x)` | `SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING AND CURRENT ROW)` | M fold = SQL running aggregate window function |
| `Table.SelectColumns(tbl, {"id", "name"})` | `SELECT id, name FROM tbl` | Identical — projection |
| `Table.SelectRows(tbl, each [status] = "active")` | `WHERE status = 'active'` | Identical — filter predicate |

The key shift: M processes rows one at a time through a step chain. SQL processes sets. When you catch yourself writing M-style logic (loop over a group, accumulate into a variable), stop — there's a window function for that. SQL's set semantics let the engine parallelize across nodes; M-style sequential thinking produces single-threaded scans.

dbt (data build tool) is the dominant pattern for SQL-based transformations across all cloud DWs. Write SELECT statements; dbt generates the DDL and handles incremental logic.

```sql
-- models/silver/orders.sql
{{ config(
    materialized = 'incremental',
    unique_key   = 'order_id',
    on_schema_change = 'merge'
) }}

SELECT
    order_id,
    customer_id,
    order_date,
    SUM(quantity * unit_price) AS total,
    CURRENT_TIMESTAMP()        AS dbt_updated_at
FROM {{ ref('bronze_orders') }}     -- ref() resolves to the correct table in catalog
{% if is_incremental() %}
WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
{% endif %}
GROUP BY 1, 2, 3
```

### dbt Materializations

| Type               | Creates                        | When to use                                 |
|--------------------|--------------------------------|---------------------------------------------|
| `table`            | `CREATE TABLE` each run        | Small-medium; needs re-computation each run |
| `view`             | `CREATE VIEW`                  | Fast, always fresh, no storage cost         |
| `incremental`      | `MERGE` / `INSERT` new rows    | Large tables; append or upsert pattern      |
| `ephemeral`        | CTE inlined into caller        | Intermediate logic; no storage needed       |
| `materialized view`| DB-managed auto-refresh        | Automatic freshness without full rebuild    |

Bridge: dbt replaces stored proc-based ETL. The `ref()` DAG replaces SSIS package dependencies.

### ADF → dbt Concept Mapping

| ADF concept | dbt equivalent | Note |
|---|---|---|
| Pipeline | dbt job / `dbt run` | The orchestration unit — triggers execution |
| Activity | dbt model | A single step in the pipeline |
| Dataset | `source()` or `ref()` | Data contract (schema + location) |
| Data Flow (visual transform) | dbt SQL model (`.sql` file) | Paradigm shift: visual canvas → SELECT statement |
| Integration Runtime | dbt adapter + `profiles.yml` | Compute connection config |
| Incremental copy (watermark) | `is_incremental()` filter | `WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})` |
| Linked Service | dbt target connection | Credential/endpoint config |
| Trigger (schedule / tumbling window) | dbt Cloud schedule / Airflow DAG | dbt itself has no scheduler |

Critical: **dbt is not a scheduler.** It executes SQL; someone else triggers it. Common Azure pattern: ADF pipeline calls dbt Cloud API (HTTP Activity → dbt Cloud REST endpoint) to trigger a dbt job, then polls for completion. ADF handles orchestration (dependencies, retries, monitoring); dbt handles transformation logic. This is the right division of labor — don't try to replace ADF scheduling with dbt.

The paradigm shift from Data Flows to dbt models: a Data Flow is a GUI that generates a Spark execution plan. A dbt model is a SELECT statement that generates DDL. Both are declarative transformation definitions — but dbt's are text, version-controlled, diffable, and reviewable in a pull request.

---

## 12. EXTERNAL TABLES AND QUERYING FILES DIRECTLY

```sql
-- BigQuery — query GCS files directly (no load required)
SELECT * FROM `project.dataset.external_table`;

-- Ad-hoc file query (BigQuery 2024)
SELECT * FROM READ_CSV('gs://bucket/path/*.csv',
    skip_leading_rows => 1,
    schema => [('id', 'INT64'), ('name', 'STRING')]);

-- Snowflake — external stage + query
CREATE STAGE my_s3_stage
    URL = 's3://bucket/data/'
    CREDENTIALS = (AWS_KEY_ID='...' AWS_SECRET_KEY='...');

-- Query files directly from stage
SELECT $1::INTEGER AS id, $2::STRING AS name
FROM @my_s3_stage/orders.parquet (FILE_FORMAT => my_parquet_fmt);

-- External table (schema on read, auto-refreshed)
CREATE EXTERNAL TABLE ext_orders
    WITH LOCATION = @my_s3_stage
    FILE_FORMAT = (TYPE = PARQUET)
    AUTO_REFRESH = true;

-- Databricks — Unity Catalog external location
SELECT * FROM delta.`abfss://container@account.dfs.core.windows.net/path/`;

-- Or read files with explicit format
SELECT * FROM read_files(
    'abfss://container@account.dfs.core.windows.net/path/',
    format => 'parquet',
    schema => 'id BIGINT, name STRING'
);

-- Synapse Serverless — query ADLS without loading (no cluster required)
SELECT *
FROM OPENROWSET(
    BULK 'https://account.dfs.core.windows.net/container/data/*.parquet',
    FORMAT = 'PARQUET'
) WITH (
    id   BIGINT,
    name NVARCHAR(200)
) AS rows;
```

---

## 13. MEDALLION ARCHITECTURE

The standard pattern for organizing data in a cloud DW or data lakehouse. Replaces the SSIS → star schema → SSAS pipeline.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    Medallion Architecture (Delta Lake / All DWs)            │
│                                                                              │
│  Raw Sources                                                                 │
│  ─────────────────────────────────────────────────────────────────────────  │
│  App Databases │ REST APIs │ Event Streams │ File Drops │ CDC (Debezium)    │
│                │                                                             │
│                ▼                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │    BRONZE        │    │     SILVER       │    │      GOLD        │        │
│  │  (Raw / Ingest)  │───►│  (Clean / Valid) │───►│  (Biz / Serve)   │       │
│  │                  │    │                  │    │                  │        │
│  │ • Raw as-landed  │    │ • Validated      │    │ • Aggregated     │        │
│  │ • No transforms  │    │ • Deduped        │    │ • Joined dims    │        │
│  │ • Full history   │    │ • Typed/cast     │    │ • KPI-ready      │        │
│  │ • Parquet/Delta  │    │ • Conformed      │    │ • Star / flat    │        │
│  │ • Append-only    │    │ • Schema enforced│    │ • SLA: < 1 hr    │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│                                                          │                   │
│                                                          ▼                   │
│                                      BI Tools: Power BI / Looker / Tableau  │
│                                      ML/AI: Feature Store / RAG pipeline     │
└──────────────────────────────────────────────────────────────────────────────┘
```

Bridge:
- Bronze = SSIS raw landing zone (staging tables)
- Silver = SSIS transformations + DQ rules (the integration layer)
- Gold = SSAS star schema (the presentation layer)
- dbt handles Bronze → Silver → Gold in SQL instead of SSIS packages

### SSAS → Modern Semantic Layer Bridge

| SSAS concept | Modern equivalent | Notes |
|---|---|---|
| MOLAP cube (pre-aggregated) | Materialized views / BigQuery MV / Snowflake dynamic tables | Same idea: pre-compute aggregates so query time is fast. Engine rewrites base-table queries to use the pre-compute automatically. |
| Tabular model (VertiPaq in-memory columnar) | Power BI semantic model (Import mode) | Same engine: VertiPaq / xVelocity. Same DAX. Different deployment topology. |
| SSAS Tabular + Direct Query | Power BI Direct Lake (Fabric) | Direct Lake reads Delta Parquet files from OneLake directly — no import, no DirectQuery overhead. Columnar reads at storage layer, not row-by-row SQL passthrough. |
| MDX tuple navigation (`[Date].[Year].[2024]`) | DAX `CALCULATE(SUM(Revenue), YEAR(Date[Date]) = 2024)` | MDX thinks in tuples and coordinates. DAX thinks in filter contexts. Functionally equivalent for most aggregations; DAX is more compositional. |
| MDX `NON EMPTY`, `CROSSJOIN` | DAX `SUMMARIZECOLUMNS`, `FILTER` | The "which cells have data" pruning is automatic in DAX via filter context; in MDX you had to be explicit. |
| Calculated measures in `.bim` | dbt metrics layer / Looker LookML measures | The "single definition of a metric" problem. SSAS solved it in the cube. dbt metrics + semantic layer (dbt Cloud) or Looker LookML solve it in the transformation layer. The metric travels downstream to any BI tool, not locked to SSAS. |
| SSAS role-based security (dimension security, cell security) | Unity Catalog row/column filters + Power BI RLS | Unity Catalog enforces at query time; Power BI RLS enforces at the semantic model layer. Both are token-based identity propagation. |
| Processing a dimension (full / incremental) | dbt incremental model run | Incremental processing = `is_incremental()` filter + MERGE. Full processing = `dbt run --full-refresh`. |

The structural shift: SSAS was a monolithic semantic layer tightly coupled to the Microsoft BI stack. The modern equivalent is layered: dbt (metrics definitions in SQL) + Unity Catalog (governance + access control) + Power BI semantic model or Looker (DAX/LookML presentation layer). Any layer can be replaced independently.

---

## 14. WINDOW FUNCTIONS

Window functions are the core of analytical SQL. They compute a value for each row using a set of rows defined by a window — without collapsing rows the way GROUP BY does. You get the detail rows AND the aggregated result in the same output.

### Logical Processing Order

```
FROM → JOIN
    ↓
WHERE
    ↓
GROUP BY + HAVING
    ↓
Window functions (OVER clause)   ← computed AFTER GROUP BY/HAVING, sees the post-filter set
    ↓
SELECT list evaluation           ← window function results are now available as aliases
    ↓
QUALIFY (cloud DW only)          ← filter on window function results (= WHERE for windows)
    ↓
ORDER BY
    ↓
LIMIT / FETCH FIRST
```

Window functions are not available in WHERE or HAVING (computed too late). They ARE available in QUALIFY. In standard SQL you must wrap in a subquery to filter on window results; QUALIFY eliminates the wrapper.

### OVER() Clause Anatomy

```
function_name() OVER (
    PARTITION BY col1, col2      -- optional: scope each window to a group of rows
    ORDER BY col3 DESC           -- optional: defines row order within each partition
    ROWS BETWEEN                 -- optional: frame clause
        UNBOUNDED PRECEDING      --   start: beginning of partition
        AND CURRENT ROW          --   end:   the current row
)
```

All three clauses are optional. Omit all three (`OVER ()`) = entire result set is one partition.

### Frame Clause: ROWS vs RANGE

This is the most commonly misunderstood part of window functions.

```sql
-- ROWS: counts physical rows — unambiguous, generally what you want
SUM(total) OVER (
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
-- For each row: sum of all rows from start of partition up to and including THIS ROW.
-- Two rows with identical order_date are treated separately.

-- RANGE: counts all rows with ORDER BY value <= current row's value
SUM(total) OVER (
    ORDER BY order_date
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
-- For rows with TIED order_date: RANGE buffers ALL tied rows before writing results.
-- All rows with the same date get the same sum (the sum INCLUDING all tied rows).
-- This creates the "tie-buffering" gotcha: a running total using RANGE gives
-- every row in a tie group the sum of the ENTIRE tie group, not a sequential subtotal.
```

Default when ORDER BY is present: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
Default when no ORDER BY: entire partition (equivalent to `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`)

**Rule of thumb**: use `ROWS` explicitly. `RANGE` is only useful when you intentionally want tied rows to share the same aggregate value.

### Ranking Functions

```sql
SELECT
    employee_id,
    dept,
    salary,

    -- ROW_NUMBER: unique sequential integer, no ties
    -- Arbitrary tie-breaking (which tied row gets which number is non-deterministic)
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn,

    -- RANK: same rank for ties, then gaps
    -- Salary: 100k, 90k, 90k, 80k → ranks: 1, 2, 2, 4
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk,

    -- DENSE_RANK: same rank for ties, no gaps
    -- Salary: 100k, 90k, 90k, 80k → ranks: 1, 2, 2, 3
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS drnk,

    -- NTILE(n): distribute rows into n roughly-equal buckets
    -- NTILE(4) = quartiles; NTILE(10) = deciles
    NTILE(4) OVER (PARTITION BY dept ORDER BY salary DESC) AS quartile

FROM employees;
```

T-SQL bridge: identical syntax. SQL Server has had these since 2005. The cloud DW versions behave identically.

### Offset Functions (Navigation)

```sql
SELECT
    order_id,
    customer_id,
    order_date,
    total,

    -- LAG: value from N rows before the current row (within partition)
    LAG(total, 1) OVER (PARTITION BY customer_id ORDER BY order_date)       AS prev_order_total,
    LAG(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date)  AS prev_order_date,

    -- LEAD: value from N rows after the current row
    LEAD(total, 1) OVER (PARTITION BY customer_id ORDER BY order_date)      AS next_order_total,

    -- LAG with default (3rd arg: value when no prior row exists)
    LAG(total, 1, 0.0) OVER (PARTITION BY customer_id ORDER BY order_date)  AS prev_or_zero,

    -- FIRST_VALUE: value from the first row in the window frame
    FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)           AS first_order_date,

    -- LAST_VALUE: value from the last row — MUST extend frame to UNBOUNDED FOLLOWING
    -- Default frame stops at CURRENT ROW, so LAST_VALUE without frame = current row value
    LAST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)           AS last_order_date,

    -- NTH_VALUE(col, n): value from the n-th row in the frame (1-indexed)
    NTH_VALUE(total, 2) OVER (PARTITION BY customer_id ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)           AS second_order_total

FROM orders;
```

### Aggregate Window Functions

```sql
SELECT
    order_id,
    customer_id,
    order_date,
    total,

    -- Running total (ordered cumulative sum)
    SUM(total) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,

    -- Customer total (no ORDER BY = entire partition frame)
    SUM(total) OVER (PARTITION BY customer_id) AS customer_lifetime_total,

    -- % of customer lifetime value
    total / SUM(total) OVER (PARTITION BY customer_id) * 100 AS pct_of_customer_ltv,

    -- 3-row centered rolling average (1 before, current, 1 after)
    AVG(total) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS rolling_3_avg,

    -- Count of orders per customer (uses full partition, same for every row)
    COUNT(*) OVER (PARTITION BY customer_id) AS orders_per_customer,

    -- Max total in the same month (RANGE on a date expression — careful with dialect support)
    MAX(total) OVER (PARTITION BY customer_id, DATE_TRUNC('month', order_date)) AS max_in_month

FROM orders;
```

### Ordered-Set Aggregates (T-SQL WITHIN GROUP)

```sql
-- PERCENTILE_CONT: interpolated percentile (returns a value that may not exist in the data)
SELECT
    dept,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary,  -- linear interp
    PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary_actual  -- actual row value
FROM employees
GROUP BY dept;

-- T-SQL exact syntax: WITHIN GROUP makes these ordered-set aggregates, not window functions
-- Use as GROUP BY aggregates (not in OVER clause) for per-group statistics
```

### Dialect Notes

| Feature | T-SQL (SQL Server 2012+) | BigQuery | Snowflake | Databricks | MySQL 8+ | DuckDB |
|---|---|---|---|---|---|---|
| ROW_NUMBER / RANK / DENSE_RANK | Yes | Yes | Yes | Yes | Yes | Yes |
| LAG / LEAD | Yes | Yes | Yes | Yes | Yes | Yes |
| FIRST_VALUE / LAST_VALUE | Yes | Yes | Yes | Yes | Yes | Yes |
| NTH_VALUE | Yes (2012+) | Yes | Yes | Yes | 8.0.2+ | Yes |
| IGNORE NULLS (LAG/LEAD) | No | Yes | Yes | Yes | No | Yes |
| QUALIFY | No | Yes | Yes | Yes | No | Yes |
| Frame clause (ROWS/RANGE) | Yes | Yes | Yes | Yes | Yes (8.0) | Yes |
| GROUPS frame mode (ANSI) | No | No | No | No | No | Yes |

T-SQL bridge: SQL Server 2012 added the full ANSI window function suite. If you know T-SQL window functions, the cloud DW behavior is identical. The differences are: cloud DWs add QUALIFY (no subquery needed for filtering), some add IGNORE NULLS on LAG/LEAD (skip NULL rows in offset), and DuckDB is the most complete ANSI implementation.

## 15. ANALYTICAL FUNCTIONS BEYOND ANSI SQL

| Function                              | BigQuery          | Snowflake         | Databricks        | Purpose                              |
|---------------------------------------|-------------------|-------------------|-------------------|--------------------------------------|
| Approx distinct count                 | `HLL_COUNT.MERGE` | `APPROX_COUNT_DISTINCT` | `APPROX_COUNT_DISTINCT` | HyperLogLog — fast ~1% error      |
| Exact percentile                      | `PERCENTILE_CONT` | `PERCENTILE_CONT` | `PERCENTILE_CONT` | Linear interpolation                 |
| Nearest-value percentile              | `PERCENTILE_DISC` | `PERCENTILE_DISC` | `PERCENTILE_DISC` | Returns actual row value             |
| Statistical correlation               | `CORR`            | `CORR`            | `CORR`            | Pearson correlation coefficient      |
| Covariance                            | `COVAR_POP/SAMP`  | `COVAR_POP/SAMP`  | `COVAR_POP/SAMP`  | Covariance (population/sample)       |
| Linear regression                     | `REGR_SLOPE/INTERCEPT` | `REGR_SLOPE/INTERCEPT` | `REGR_SLOPE/INTERCEPT` | In-SQL regression        |
| Date truncation                       | `DATE_TRUNC`      | `DATE_TRUNC`      | `DATE_TRUNC`      | Truncate to year/month/week/day/hour |
| Date series generation                | `GENERATE_DATE_ARRAY` | `DATEADD` + recursive CTE | `SEQUENCE` + `EXPLODE` | Generate date spine         |
| Statistical sampling                  | `TABLESAMPLE`     | `SAMPLE`          | `TABLESAMPLE`     | Random % sample of table             |
| ML inference                          | `ML.PREDICT`      | `SNOWFLAKE.CORTEX.COMPLETE` | `ai_query()` | LLM/ML model inference in SQL  |

---

## 16. GOTCHAS FROM T-SQL

| T-SQL habit                          | Cloud DW reality                                                                |
|--------------------------------------|---------------------------------------------------------------------------------|
| `SELECT TOP 10`                      | Use `LIMIT 10` (BigQuery/Snowflake/Databricks) or `FETCH FIRST 10 ROWS ONLY`  |
| Nested subquery for window filters   | Use `QUALIFY` — it's cleaner and exists for this exact reason                  |
| Case sensitivity (SQL Server = CI)   | BigQuery: CI columns; Snowflake: CI by default, CS if quoted; Databricks: CS   |
| Semicolons optional                  | BigQuery requires `;` between statements; Snowflake/Databricks: required in scripts |
| `database.schema.table`              | BigQuery: `project.dataset.table`; Snowflake: `db.schema.table`; Databricks: `catalog.schema.table` |
| Stored procedures for ETL            | Replaced by dbt models (SQL) or Databricks notebooks (Python + SQL)            |
| Fixed compute cost (license + HW)   | BigQuery: per byte scanned; Snowflake: per second of warehouse uptime; costs real money per bad query |
| `GETDATE()` / `SYSDATETIME()`        | `CURRENT_TIMESTAMP()` (ANSI), or platform-specific: `NOW()`, `CURRENT_DATE()`  |
| `ISNULL(x, default)`                 | `COALESCE(x, default)` (ANSI — works everywhere)                                |
| `DATEDIFF(day, start, end)`          | BigQuery: `DATE_DIFF(end, start, DAY)`; Snowflake: `DATEDIFF('day', start, end)` |

---

## 17. DECISION CHEAT SHEET

| Choose            | When                                                                                          |
|-------------------|-----------------------------------------------------------------------------------------------|
| **BigQuery**      | Google Cloud shop; largest-scale serverless; no cluster sizing; `ML.PREDICT` integration; Looker native |
| **Snowflake**     | Multi-cloud required; cleanest SQL UX; data sharing / marketplace features; 90-day time travel; Cortex AI |
| **Databricks**    | Python/ML-heavy team; streaming + batch unified; Unity Catalog governance; Delta Lake open format |
| **Synapse**       | Azure-native; T-SQL muscle memory; Power BI Direct Lake; Purview governance; existing Azure investment |
| **dbt + any**     | SQL-first transformation layer; replaces stored proc ETL on all four platforms                |

---

## 18. COMMON CONFUSION POINTS

**"Cloud DW" vs "data lake"**
Data lake = files (Parquet/Delta/Iceberg) on object storage. Cloud DW = SQL query engine on top. The line is blurring fast: Databricks is both. Snowflake now reads external Iceberg tables. BigQuery reads GCS files directly. The term "lakehouse" means "Delta/Iceberg files + SQL DW engine."

**QUALIFY is not ANSI SQL**
It won't work in PostgreSQL, MySQL, or SQL Server. Don't use it in portable SQL. It's a cloud DW convenience — treat it as such.

**"Snowflake warehouse" ≠ data warehouse building**
In Snowflake, "warehouse" = a compute cluster (virtual machine pool). You size it XS to 6XL. It costs credits per second when running. You can have many warehouses pointing at the same data. This is the decoupled compute model.

**BigQuery on-demand vs capacity pricing**
On-demand: $6.25/TB scanned (as of 2024). Capacity: flat monthly rate for reserved slots (vCPUs). Heavy users switch to capacity; occasional users use on-demand. Partitioning + clustering reduce scanned bytes = lower on-demand bill.

**Delta vs Parquet**
Parquet is a columnar file format. Delta = Parquet files + `_delta_log/` transaction log. The log enables ACID transactions, time travel, schema evolution, and concurrent writes. Delta IS Parquet — plus a sidecar log.

**dbt is not a compute engine**
dbt generates SQL and submits it to the warehouse. Compute happens in BigQuery/Snowflake/Databricks. dbt itself is a thin CLI/orchestrator. Confusion comes from the term "dbt runs" — what runs is the SQL, inside the warehouse.

**Materialized view vs dynamic table vs incremental dbt model**
Three different mechanisms for the same goal (pre-computed aggregates):
- MV = database-managed, automatic, query-rewrite eligible
- Dynamic table (Snowflake) = declarative, target lag based, pipeline-oriented
- Incremental dbt = developer-managed MERGE logic, explicit schedule via dbt Cloud/Airflow
