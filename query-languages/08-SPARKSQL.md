# Spark SQL + Delta Lake

Apache Spark replaced MapReduce as the standard distributed compute engine for big data. Spark SQL is the SQL interface on top — same RDD/DataFrame computation model, different surface. You can write SQL or the DataFrame API and get identical execution plans. Delta Lake adds ACID transactions, time travel, and schema enforcement on top of Parquet files — making Spark suitable for data warehouse workloads, not just batch ETL.

---

## 1. ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        Apache Spark Architecture                             │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                   Spark SQL / DataFrame API                          │   │
│  │   spark.sql("SELECT ...")    df.filter(...).groupBy(...)             │   │
│  │   Python (PySpark)  /  Scala  /  Java  /  R (SparkR)               │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │  identical execution plan                 │
│  ┌──────────────────────────────▼───────────────────────────────────────┐   │
│  │                   Catalyst Query Optimizer                           │   │
│  │   Parse → Analyze → Optimize → Physical Plan → Codegen (JVM)       │   │
│  │   Rule-based + cost-based optimizations (column pruning, pushdown)  │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                           │
│  ┌──────────────────────────────▼───────────────────────────────────────┐   │
│  │             Distributed Execution (Driver + Executors)               │   │
│  │   Stage 1 ──shuffle──► Stage 2 ──shuffle──► Stage 3                │   │
│  │   Each stage = DAG of tasks (1 task per partition)                  │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                           │
│  ┌──────────────────────────────▼───────────────────────────────────────┐   │
│  │      Storage Layer                                                   │   │
│  │      Delta Lake / Parquet / ORC / JSON / CSV / Avro                 │   │
│  │      HDFS  /  S3  /  ADLS Gen2  /  GCS                             │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────┘

MapReduce bridge:
  MapReduce: disk write between EVERY step (Map → disk → Reduce → disk)
  Spark:     in-memory between steps; disk spill only when memory exhausted
  Both:      distributed partitioning, shuffle concept, fault tolerance via lineage
  Speedup:   10–100x for iterative jobs (ML, graph traversal); ~3–5x for single-pass ETL
```

---

## 2. DIALECT SNAPSHOT

| Attribute           | Value                                                              |
|---------------------|--------------------------------------------------------------------|
| Origin              | UC Berkeley AMPLab (2009), Apache top-level (2013)                |
| License             | Apache 2.0                                                         |
| Current version     | Apache Spark 3.5.x (2024); Databricks Runtime 14.x                |
| SQL dialect         | HiveQL-compatible + ANSI SQL extensions                            |
| Execution runtime   | JVM (Scala/Java core) + Python (PySpark) + R (SparkR)              |
| Managed services    | Databricks, AWS EMR, Azure HDInsight, GCP Dataproc                 |
| Delta Lake          | Open-source; default format on Databricks; Linux Foundation project |
| Metastore           | Hive Metastore (legacy) or Unity Catalog (Databricks, 2022+)       |

---

## 3. SQL API VS DATAFRAME API — IDENTICAL EXECUTION

```python
# These two produce the same physical execution plan (verify with .explain())

# SQL API — familiar to any SQL writer
result = spark.sql("""
    SELECT   dept,
             AVG(salary) AS avg_salary,
             COUNT(*)    AS headcount
    FROM     employees
    WHERE    status = 'active'
    GROUP BY dept
    ORDER BY avg_salary DESC
""")

# DataFrame API (PySpark) — composable, conditional logic possible
from pyspark.sql import functions as F

result = (
    spark.table("employees")
         .filter(F.col("status") == "active")
         .groupBy("dept")
         .agg(
             F.avg("salary").alias("avg_salary"),
             F.count("*").alias("headcount")
         )
         .orderBy(F.desc("avg_salary"))
)

result.show()
# Both produce the same SparkPlan — Catalyst optimizes either form equally.
```

Use SQL for: ad-hoc queries, dbt models, reporting transformations.
Use DataFrame API for: conditional branching, loops, reusable functions, mixing Python logic with SQL.

---

## 4. READING AND WRITING DATA

```python
# --- READS ---

# Parquet (most common in production)
df = spark.read.parquet("abfss://container@account.dfs.core.windows.net/data/orders/")

# Explicit schema — DO THIS in production (avoids full scan for inference)
from pyspark.sql.types import StructType, StructField, LongType, StringType, DecimalType, DateType

schema = StructType([
    StructField("order_id",    LongType(),           nullable=False),
    StructField("customer_id", LongType(),           nullable=False),
    StructField("order_date",  DateType(),           nullable=True),
    StructField("total",       DecimalType(12, 2),   nullable=True),
    StructField("status",      StringType(),         nullable=True),
])
df = spark.read.schema(schema).parquet("/data/orders/")

# CSV
df = (spark.read
          .option("header", True)
          .option("inferSchema", True)        # OK for small dev data; avoid in prod
          .option("sep", ",")
          .csv("/data/file.csv"))

# JSON (one JSON object per line = JSONL/NDJSON)
df = spark.read.json("/data/events/*.json")

# Delta Lake
df = spark.read.format("delta").load("/delta/orders/")
df = spark.table("catalog.schema.orders")    # Unity Catalog registered table

# --- WRITES ---

# Overwrite Parquet with partitioning
(df.write
   .mode("overwrite")
   .partitionBy("year", "month")             # physical directory partition
   .parquet("/output/orders/"))

# Append to existing Delta table
(df.write
   .format("delta")
   .mode("append")
   .save("/delta/orders/"))

# Write as managed table (Delta, registered in catalog)
(df.write
   .format("delta")
   .mode("overwrite")
   .option("overwriteSchema", "true")        # allow schema change on overwrite
   .saveAsTable("gold.orders"))
```

---

## 5. REGISTERED VIEWS AND TEMP TABLES

```python
# Temporary view — session-scoped (lives until session/cluster restart)
df.createOrReplaceTempView("orders_temp")
spark.sql("SELECT COUNT(*) FROM orders_temp WHERE status = 'active'")

# Global temp view — shared across sessions within same Spark application
df.createOrReplaceGlobalTempView("orders_global")
spark.sql("SELECT * FROM global_temp.orders_global")   # note: global_temp prefix required

# Permanent table in Unity Catalog (persists across sessions/clusters)
df.write.format("delta").saveAsTable("catalog.schema.orders")

# Create view in catalog (SQL DDL)
spark.sql("""
    CREATE OR REPLACE VIEW gold.v_active_customers AS
    SELECT customer_id, name, email
    FROM silver.customers
    WHERE is_active = true
""")
```

---

## 6. SPARK SQL — KEY SYNTAX

```sql
-- Type casting
SELECT
    CAST(order_date AS DATE),
    CAST(amount     AS DECIMAL(12, 2)),
    CAST(quantity   AS INT),
    TRY_CAST(bad_column AS INT)   -- returns NULL on failure (vs. error)
FROM raw_orders;

-- Struct field access (dot notation)
SELECT address.city, address.state FROM customers;

-- EXPLODE — array → rows (HiveQL name; ANSI SQL uses UNNEST)
SELECT EXPLODE(tags) AS tag FROM articles;
SELECT POSEXPLODE(tags) AS (pos, tag) FROM articles;  -- with zero-based position index

-- Array functions
SELECT
    SIZE(tags)                         AS tag_count,
    ARRAY_CONTAINS(tags, 'database')   AS has_db_tag,
    ARRAY_DISTINCT(tags)               AS unique_tags,
    ARRAY_SORT(tags)                   AS sorted_tags,
    SLICE(tags, 1, 3)                  AS first_3_tags,   -- 1-based index
    FLATTEN(nested_arrays)             AS flat
FROM articles;

-- Map operations
SELECT
    properties['color']                AS color,
    MAP_KEYS(properties)               AS prop_keys,
    MAP_VALUES(properties)             AS prop_vals
FROM products;

-- LATERAL VIEW EXPLODE (HiveQL syntax — common in legacy code)
SELECT id, tag
FROM articles
LATERAL VIEW EXPLODE(tags) t AS tag;

-- Inline values table
SELECT * FROM VALUES (1, 'alice'), (2, 'bob'), (3, 'charlie') AS t(id, name);

-- TRANSFORM (functional map over array)
SELECT TRANSFORM(amounts, x -> x * 1.1) AS inflated FROM orders;

-- FILTER (functional filter over array)
SELECT FILTER(tags, t -> t != 'deprecated') AS active_tags FROM articles;

-- AGGREGATE (functional fold/reduce over array)
SELECT AGGREGATE(amounts, 0.0, (acc, x) -> acc + x) AS total FROM orders;

-- EXISTS / FORALL
SELECT EXISTS(tags, t -> t = 'urgent') AS has_urgent FROM tasks;
SELECT FORALL(scores, s -> s >= 60)    AS all_passing FROM exams;
```

---

## 7. PARTITIONING — Critical for Performance

```sql
-- Partition on write: creates physical directory structure
-- /table/year=2024/month=01/day=15/part-00000-*.parquet

CREATE TABLE orders
USING DELTA
PARTITIONED BY (year INT, month INT)
LOCATION 'abfss://container@account.dfs.core.windows.net/delta/orders'
AS
SELECT
    *,
    YEAR(order_date)  AS year,
    MONTH(order_date) AS month
FROM raw_orders;

-- Partition pruning: WHERE on partition columns scans only matching dirs
SELECT * FROM orders WHERE year = 2024 AND month = 1;
-- Reads: /orders/year=2024/month=01/ only — skips all other partitions
```

```python
# In-memory repartitioning (DataFrame API)

# Redistribute into N partitions (full shuffle — expensive)
df = df.repartition(100)

# Reduce partition count without shuffle (only valid for reducing, not increasing)
df = df.coalesce(10)                          # fast: no shuffle, used before write

# Co-locate rows by key (co-locate before join = avoid shuffle in join)
df = df.repartition(F.col("customer_id"))    # all rows for same customer_id → same partition

# Check partition count
print(df.rdd.getNumPartitions())

# Rule of thumb: target ~128 MB per partition
# Too few partitions → idle cores; too many → scheduler overhead + small files
# spark.sql.shuffle.partitions default = 200 (tune down for small data, up for large)
spark.conf.set("spark.sql.shuffle.partitions", "400")
```

---

## 8. BROADCAST JOINS — Avoiding Shuffle for Small Tables

```python
from pyspark.sql.functions import broadcast

# Without broadcast: both sides shuffled by join key across network (expensive)
result = fact_orders.join(dim_products, "product_id")

# With broadcast: small table replicated to every executor (zero shuffle)
result = fact_orders.join(broadcast(dim_products), "product_id")

# SQL hint equivalent
spark.sql("""
    SELECT /*+ BROADCAST(dim_products) */ *
    FROM   fact_orders
    JOIN   dim_products ON fact_orders.product_id = dim_products.id
""")

# Configure auto-broadcast threshold (default: 10 MB)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", str(50 * 1024 * 1024))  # 50 MB

# Disable auto-broadcast (use explicit hints instead)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1")
```

MapReduce bridge: This is the "replicated join" / "map-side join" from MapReduce — same concept, now automated with size-based heuristics.

---

## 9. WINDOW FUNCTIONS

```sql
-- Full ANSI window function support — same semantics as SQL Server
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
    ) AS cumulative_spend,

    -- Previous order date per customer
    LAG(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date)
        AS prev_order_date,

    -- Days between orders (using LAG inside DATEDIFF)
    DATEDIFF(
        order_date,
        LAG(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date)
    ) AS days_since_last_order,

    -- Running rank (resets per customer)
    RANK() OVER (PARTITION BY customer_id ORDER BY total DESC) AS order_rank,

    -- 7-row rolling average
    AVG(total) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7_avg

FROM orders;
```

---

## 10. DELTA LAKE — ACID ON TOP OF PARQUET

```
Delta table structure on disk:
  /delta/orders/
  ├── _delta_log/                       # transaction log
  │   ├── 00000000000000000000.json     # commit 0: initial CREATE TABLE
  │   ├── 00000000000000000001.json     # commit 1: first INSERT
  │   ├── 00000000000000000002.json     # commit 2: MERGE upsert
  │   └── 00000000000000000010.checkpoint.parquet  # log compaction every 10 commits
  ├── part-00000-abc123.snappy.parquet  # data files
  └── part-00001-def456.snappy.parquet

Each log entry records: which files were added, which removed, schema, metadata.
ACID: readers see consistent snapshots; concurrent writers serialize via optimistic locking.
```

```sql
-- CREATE TABLE (Delta format)
CREATE TABLE orders (
    order_id    BIGINT       NOT NULL,
    customer_id BIGINT       NOT NULL,
    order_date  DATE         NOT NULL,
    total       DECIMAL(12,2) NOT NULL,
    status      STRING
) USING DELTA
PARTITIONED BY (order_date)
LOCATION 'abfss://container@account.dfs.core.windows.net/delta/orders';

-- MERGE INTO — the core Delta operation for CDC upserts
MERGE INTO orders AS target
USING order_updates AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.updated_at > target.updated_at THEN
    UPDATE SET
        total      = source.total,
        status     = source.status,
        updated_at = source.updated_at
WHEN NOT MATCHED THEN
    INSERT *
WHEN NOT MATCHED BY SOURCE THEN   -- target rows with no source match
    UPDATE SET status = 'deleted'; -- or: DELETE

-- OPTIMIZE: compact small files (critical for streaming ingest)
OPTIMIZE orders;

-- OPTIMIZE with Z-ordering: multi-dimensional file-level co-location
-- Analogy: like a composite covering index, but at file granularity
OPTIMIZE orders ZORDER BY (customer_id, order_date);
-- Z-order interleaves bits of column values → files covering related (customer, date) pairs
-- are physically co-located → fewer files scanned for multi-column filters

-- VACUUM: permanently delete data files no longer referenced by the log
VACUUM orders RETAIN 168 HOURS;   -- 7-day retention (default)
VACUUM orders;                     -- uses table retention setting
-- WARNING: After VACUUM, time travel before retention window is impossible

-- Time travel
SELECT * FROM orders VERSION AS OF 10;
SELECT * FROM orders TIMESTAMP AS OF '2024-01-15 00:00:00';
RESTORE TABLE orders TO VERSION AS OF 5;
RESTORE TABLE orders TO TIMESTAMP AS OF '2024-01-15 10:00:00';

-- Full audit history
DESCRIBE HISTORY orders;
-- Columns: version, timestamp, userId, userName, operation,
--          operationParameters, operationMetrics, userMetadata

-- Schema evolution
ALTER TABLE orders ADD COLUMNS (discount DECIMAL(5,2));
ALTER TABLE orders CHANGE COLUMN status COMMENT 'Order lifecycle status';
```

```python
# Schema evolution on write (auto-merge new columns)
(df.write
   .format("delta")
   .mode("append")
   .option("mergeSchema", "true")      # adds new columns from df to table schema
   .save("/delta/orders/"))

# Full overwrite including schema change
(df.write
   .format("delta")
   .mode("overwrite")
   .option("overwriteSchema", "true")  # replaces schema entirely
   .save("/delta/orders/"))
```

---

## 11. STRUCTURED STREAMING

```python
# Spark Structured Streaming: continuous processing on an unbounded table
# Same SQL/DataFrame API — source and sink become streaming

# --- KAFKA SOURCE ---
stream_df = (
    spark.readStream
         .format("kafka")
         .option("kafka.bootstrap.servers", "broker1:9092,broker2:9092")
         .option("subscribe", "orders")              # or "subscribePattern" for regex
         .option("startingOffsets", "latest")        # or "earliest" for full replay
         .load()
)
# Kafka schema: key, value, topic, partition, offset, timestamp

# Parse JSON payload
from pyspark.sql.functions import from_json, col

parsed = (
    stream_df
    .select(from_json(col("value").cast("string"), order_schema).alias("d"))
    .select("d.*")
)

# --- WINDOWED AGGREGATION WITH WATERMARK ---
aggregated = (
    parsed
    .withWatermark("event_time", "10 minutes")   # max late arrival tolerance
    .groupBy(
        F.window("event_time", "5 minutes"),      # tumbling 5-min window
        "product_id"
    )
    .agg(
        F.sum("quantity").alias("total_qty"),
        F.count("*").alias("order_count")
    )
)

# --- WRITE TO DELTA LAKE ---
query = (
    aggregated
    .writeStream
    .format("delta")
    .outputMode("append")                         # append | update | complete
    .option("checkpointLocation", "/checkpoints/order_agg/")   # required for fault tolerance
    .trigger(processingTime="1 minute")           # or trigger(availableNow=True) for once
    .start("/delta/order_aggregates/")
)

query.awaitTermination()
query.status        # current status dict
query.recentProgress  # list of recent batch metrics

# --- DELTA AS SOURCE (Delta table change feed) ---
stream_df = (
    spark.readStream
         .format("delta")
         .option("readChangeFeed", "true")        # reads inserts, updates, deletes as rows
         .option("startingVersion", "0")
         .table("silver.orders")
)
```

Output modes:
| Mode       | What is written each trigger                     | When to use                         |
|------------|--------------------------------------------------|-------------------------------------|
| `append`   | Only new rows (immutable; no update to past rows)| Append-only sinks (Kafka, Delta)    |
| `update`   | Only rows that changed since last trigger        | Aggregation with no late data       |
| `complete` | Full aggregation result every trigger            | Small result sets; global top-N     |

---

## 12. EXPLAIN — READING THE EXECUTION PLAN

```python
df.explain()              # physical plan only (quickest check)
df.explain("extended")    # logical + optimized logical + physical
df.explain("cost")        # with cardinality/size statistics
df.explain("formatted")   # tree format with node IDs — best for reading (Spark 3.x)
```

### Key operations to recognize

| Operation            | What it means                                      | Performance signal        |
|----------------------|----------------------------------------------------|---------------------------|
| `FileScan`           | Reading source files                               | Look for `PartitionFilters` — means pruning is working |
| `Filter`             | WHERE predicate applied                            | Should be pushed down before Scan |
| `Exchange`           | Network shuffle                                    | Expensive — minimize; each wide transformation adds one |
| `HashAggregate`      | GROUP BY via hash table                            | Check `partial` vs `final` (two-phase agg) |
| `SortMergeJoin`      | Join requiring sort + merge phase                  | Shuffle-heavy; replace with BroadcastHashJoin for small tables |
| `BroadcastHashJoin`  | Small table replicated, join in memory             | Cheap — no shuffle; what you want |
| `WholeStageCodegen`  | JVM bytecode generated for multiple operations     | Good — means vectorized execution |
| `AQE`                | Adaptive Query Execution (Spark 3+)                | Runtime optimization (skew handling, join strategy changes) |

---

## 13. ADAPTIVE QUERY EXECUTION (AQE — Spark 3+)

```python
# AQE enabled by default in Spark 3.2+
spark.conf.set("spark.sql.adaptive.enabled", "true")        # default: true
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")  # merge small post-shuffle partitions
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")  # detect + mitigate data skew automatically

# What AQE does at runtime:
# 1. Coalesces shuffle partitions: if post-shuffle partitions are small, merges them
# 2. Switches join strategy: downgrades SortMergeJoin to BroadcastHashJoin if one side is small
# 3. Handles skew: splits oversized partitions automatically
```

---

## 14. GOTCHAS FROM T-SQL AND MAPREDUCED

| Habit / expectation                          | Spark reality                                                                               |
|----------------------------------------------|---------------------------------------------------------------------------------------------|
| SQL executes immediately on submit           | Spark is **lazy**: builds a plan, executes only on action (`.show()`, `.write()`, `.count()`) |
| All joins shuffle (MapReduce default)        | Broadcast joins avoid shuffle for small tables — use them aggressively                      |
| Partition = database partition concept       | Spark partitions = in-memory/file chunks, not keyed ranges; different abstraction           |
| 200 shuffle partitions is fine               | `spark.sql.shuffle.partitions=200` default is often wrong; tune to data size              |
| Schema is always known                       | `inferSchema=True` reads all files to guess types — expensive and sometimes wrong in prod   |
| OOM = need more RAM                          | Often caused by data skew (one partition 100x larger); fix by salting or repartitioning     |
| EXPLODE = UNNEST                             | Same operation; Spark uses `EXPLODE` (HiveQL), ANSI SQL uses `UNNEST`                       |
| Dropping a table removes only catalog entry  | Managed Delta tables: drop = **deletes data**. External tables: drop = catalog entry only   |
| OPTIMIZE runs automatically                  | No. Must be scheduled. Streaming writes create small files; OPTIMIZE compacts them           |
| Z-ordering is like an index                  | It's file-level co-location, not row-level. Still a scan, just fewer files scanned          |
| Watermarks optional in streaming             | Required for stateful aggregations; without watermark Spark keeps all state → OOM           |

---

## 15. DECISION CHEAT SHEET

| Use Spark SQL when                                         | Use something else when                                  |
|------------------------------------------------------------|----------------------------------------------------------|
| Data > several GB (where a single-node DW struggles)       | Small data (< 10 GB): DuckDB or PostgreSQL is faster    |
| Need Python + SQL mixed in the same pipeline               | Pure SQL transformation: dbt on Snowflake/BigQuery       |
| ML pipeline (MLlib, Pandas UDFs, MLflow) alongside SQL     | Real-time OLTP queries (Spark has high startup latency)  |
| Streaming + batch unified (Structured Streaming)           | Interactive BI (Spark cold-start; use Databricks SQL WH) |
| Delta Lake ACID on top of open object storage              | True serverless pay-per-query: BigQuery or Synapse       |
| You need MERGE, time travel, schema evolution on files     | Simple ad-hoc CSV exploration: DuckDB                   |

---

## 16. COMMON CONFUSION POINTS

**Spark is not a database**
Spark is a compute engine. Data lives in files (Delta/Parquet) or a metastore catalog. There's no persistent server to connect to like SQL Server. Every Spark job spins up a cluster (or reuses a Databricks interactive cluster), runs, and releases resources.

**DataFrame vs Dataset vs RDD**
- RDD: low-level, untyped, no Catalyst optimization — avoid in modern Spark
- Dataset: typed, compile-time type safety — Scala/Java only
- DataFrame: `Dataset[Row]` — what everyone actually uses; Catalyst-optimized; Python and Scala
Use DataFrame (or Spark SQL). Forget RDD exists.

**EXPLODE vs UNNEST**
Same operation. `EXPLODE` is HiveQL (Spark's SQL heritage). `UNNEST` is ANSI SQL (PostgreSQL, BigQuery, Snowflake). Spark SQL uses `EXPLODE`. Don't mix them.

**Managed table vs external table**
Managed: `df.write.saveAsTable("orders")` — Spark owns the storage path. `DROP TABLE orders` deletes the files.
External: `df.write.format("delta").save("/delta/orders/")` then `CREATE TABLE orders LOCATION '/delta/orders/'` — you own the path. `DROP TABLE` removes only the catalog entry. In production, prefer external tables for safety.

**OPTIMIZE and VACUUM are separate operations**
`OPTIMIZE` compacts small Parquet files into larger ones (improves read performance). `VACUUM` deletes the old Parquet files that are no longer referenced by the Delta log (frees storage). Both are maintenance; neither is automatic. Schedule both.

**Watermarks are required for streaming aggregation**
Without a watermark, Spark must maintain state for every event time value it has ever seen, growing unbounded → eventual OOM. Watermark = "discard state for event times older than now - threshold."

**Z-ordering is not a row-level index**
There is no B-tree or hash index in Spark/Delta. Z-ordering is file-level: it sorts and co-locates rows with related values into the same physical files. Reads still scan files (with `PartitionFilters` and `DataFilters` skipping non-matching files). Not the same as SQL Server's clustered index.

**Checkpoint location is mandatory for fault tolerance**
If a streaming job fails and restarts without a checkpoint, it reprocesses from the beginning (or loses progress). The checkpoint stores offsets and aggregation state. Put it on durable storage (ADLS, S3), not local disk.
