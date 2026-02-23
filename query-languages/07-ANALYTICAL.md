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

## 2. PLATFORM COMPARISON

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

---

## 3. PARTITIONING AND CLUSTERING

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

## 4. QUALIFY — Window Function Filter

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

## 5. PIVOT AND UNPIVOT

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

## 6. SEMI-STRUCTURED DATA

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

## 7. TIME TRAVEL

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

## 8. MERGE INTO / UPSERT

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

## 9. MATERIALIZED VIEWS AND CONTINUOUS AGGREGATION

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

## 10. DBT INTEGRATION — The Standard Transformation Layer

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

---

## 11. EXTERNAL TABLES AND QUERYING FILES DIRECTLY

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

## 12. MEDALLION ARCHITECTURE

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

---

## 13. ANALYTICAL FUNCTIONS BEYOND ANSI SQL

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

## 14. GOTCHAS FROM T-SQL

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

## 15. DECISION CHEAT SHEET

| Choose            | When                                                                                          |
|-------------------|-----------------------------------------------------------------------------------------------|
| **BigQuery**      | Google Cloud shop; largest-scale serverless; no cluster sizing; `ML.PREDICT` integration; Looker native |
| **Snowflake**     | Multi-cloud required; cleanest SQL UX; data sharing / marketplace features; 90-day time travel; Cortex AI |
| **Databricks**    | Python/ML-heavy team; streaming + batch unified; Unity Catalog governance; Delta Lake open format |
| **Synapse**       | Azure-native; T-SQL muscle memory; Power BI Direct Lake; Purview governance; existing Azure investment |
| **dbt + any**     | SQL-first transformation layer; replaces stored proc ETL on all four platforms                |

---

## 16. COMMON CONFUSION POINTS

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
