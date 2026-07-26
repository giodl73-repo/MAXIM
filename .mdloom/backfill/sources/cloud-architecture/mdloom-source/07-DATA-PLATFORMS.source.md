---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-DATA-PLATFORMS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:cloud-architecture:data-platforms
kind: guide
module: cloud-architecture
section: cloud-architecture
title: Cloud Data Platforms: Synapse, Databricks, ADF, Delta Lake, Lakehouse
status: source-custody
source_custody: partial
current_path: cloud-architecture/07-DATA-PLATFORMS.md
canonical_path: cloud-architecture/07-DATA-PLATFORMS.md
backsource_ids: [mdloom-backfill:cloud-architecture:07-data-platforms, git-history:cloud-architecture:07-data-platforms]
concepts: [data, platforms]
root_concepts: [data, platforms]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Cloud Data Platforms: Synapse, Databricks, ADF, Delta Lake, Lakehouse

## The Big Picture

The lakehouse pattern combines a data lake (cheap, scalable storage) with data warehouse capabilities (ACID transactions, schema enforcement, query performance) on top of the same storage.

```
DATA PLATFORM ARCHITECTURE EVOLUTION

  TRADITIONAL (2000s) — Data Warehouse:
    Teradata, Netezza, SQL DW.
    Structured only; expensive storage; schema on write; good query perf.

  DATA LAKE ERA (2010s):
    HDFS, S3, ADLS Gen2.
    Schema on read; unstructured OK; cheap storage; no transactions;
    Spark/Hive query.

  LAKEHOUSE (2020s):
    Delta Lake / Iceberg / Hudi.
    ACID transactions on object storage; schema + transactions;
    good query performance.

  AZURE SERVICES:
    ADLS Gen2:        storage.
    Delta Lake:       table format on top of ADLS Gen2.
    Synapse Analytics + Databricks: query and compute.
    Azure Data Factory: orchestration / ETL-ELT.
```

---

## Medallion Architecture (Bronze/Silver/Gold)

The standard pattern for organizing data in a lakehouse:

```
RAW DATA SOURCES → [Bronze] → [Silver] → [Gold] → CONSUMERS

BRONZE LAYER (raw, immutable):
  Exact copy of source data, as received
  No transformation, no cleaning
  Format: often Parquet or Delta (preserves source schema)
  Append-only: never overwrite, never delete
  Use: reprocessing from scratch when logic changes
  Location: ADLS Gen2 / bronze container

SILVER LAYER (cleansed, conformed):
  Validated, cleaned, deduped data
  Common data types, column names normalized
  Joins across source systems (e.g., customer from CRM + from ERP)
  Filtering of invalid records
  PII tokenization applied
  Format: Delta Lake (ACID, schema enforcement, time travel)
  Location: ADLS Gen2 / silver container

GOLD LAYER (business-ready, aggregated):
  Star schema or flat aggregates for specific use cases
  Pre-computed metrics (daily sales by region, weekly user cohort)
  Optimized for query performance (partitioning, Z-ordering, clustering)
  Multiple gold tables for different domains (Marketing Gold, Finance Gold)
  Consumed by: Power BI, Synapse dedicated pool, ML feature stores
  Format: Delta Lake

PIPELINE FLOW:
  ADF ingests from source → writes Bronze
  Databricks/Synapse Spark job → reads Bronze, cleans → writes Silver
  Databricks/Synapse → aggregates Silver → writes Gold
  Power BI / Synapse dedicated pool → reads Gold
```

---

## Azure Synapse Analytics

Synapse is Azure's unified analytics service — part data warehouse, part Spark platform, part data integration.

### Compute Engines in Synapse

```
SYNAPSE ENGINES

1. DEDICATED SQL POOL (formerly SQL DW):
   Massively Parallel Processing (MPP) SQL engine
   Data: stored in Synapse-managed distributed storage (not ADLS)
   Architecture: 60 distributions (shards) across DWUs
   Best for: complex analytical queries over large structured datasets
   Pricing: pay per DWU-hour (pause when idle!)
   Scale: 100 DWUs to 30,000 DWUs
   Limitations: no ACID (no row-level locks), batch loads only,
                not Spark-compatible natively

2. SERVERLESS SQL POOL (built-in, always on):
   Query ADLS Gen2 files directly with SQL (no data loading)
   Supports: Parquet, Delta (preview→GA), CSV, JSON
   Pricing: per TB scanned
   Best for: ad hoc exploration, schema discovery, light analytics
   Limitations: no updates/deletes, reads from lake only
   Use: "show me the schema of this parquet file" or "what's in this folder"

3. APACHE SPARK POOL:
   Managed Spark clusters (auto-start, auto-terminate)
   Spark 3.x, Delta Lake support
   Languages: Scala, PySpark, Spark SQL, .NET Spark
   Use: data transformation (Bronze→Silver), ML, streaming
   vs. Databricks: Synapse Spark has tighter Azure integration;
     Databricks has more features (MLflow native, Unity Catalog, DLT)
```

### Synapse Link

```
SYNAPSE LINK:
  Zero-ETL: analytical query against Cosmos DB or Azure SQL
  Change feed replicates data to ADLS Gen2 (near-real-time)
  Synapse Serverless SQL or Spark reads it
  No impact on operational database performance
  Use: avoid extracting operational data into separate ETL pipeline
```

---

## Azure Databricks

Databricks is a managed Spark platform with additional capabilities (MLflow, Unity Catalog, Delta Live Tables).

```
DATABRICKS ARCHITECTURE

WORKSPACE:
  Notebooks (collaborative, like Jupyter, with revision history)
  Jobs: scheduled notebook or JAR execution
  Clusters: interactive (notebooks) or job (automated)
  Libraries: shared libraries per cluster or per notebook

CLUSTER TYPES:
  All-purpose: interactive development, collaborative notebooks
  Job: automated, isolated, terminated after job completion
  SQL Warehouse: Databricks SQL endpoint for BI tools (JDBC/ODBC)

DELTA LIVE TABLES (DLT):
  Declarative pipeline framework (like DBT but for Spark)
  Define: @dlt.table decorator + transformation SQL/Python
  DLT manages: ordering, retry, schema evolution, data quality
  Medallion enforcement: declare table quality expectations as constraints

UNITY CATALOG:
  Centralized governance for all Databricks assets
  Catalogs → Schemas → Tables (3-level namespace)
  Cross-workspace access: one catalog, multiple workspaces
  Column-level security, row-level security, data lineage
  vs. Synapse: Purview for governance (different product)

MLFLOW INTEGRATION:
  Experiment tracking: log params, metrics, artifacts per run
  Model registry: version models, promote to staging/production
  Auto-logging: sklearn, TF, PyTorch auto-log hyperparams + metrics
  Azure ML can use MLflow as tracking server
```

### Databricks vs. Synapse Spark

| Dimension | Databricks | Synapse Spark |
|-----------|-----------|---------------|
| Unity Catalog | Yes (centralized governance) | No (Purview separate) |
| Delta Live Tables | Yes | No |
| MLflow native | Yes | Via Azure ML |
| Azure AD integration | Yes | Tighter Azure RBAC |
| Cost | Add-on cost to Azure Spark | Included in Synapse |
| Collaborative notebooks | Better (real-time collab) | Basic |
| Ecosystem | Leading OSS Spark distrib | Azure-integrated |
| Best for | ML + analytics, heavy Spark | Azure-native analytics + SQL DW |

---

## Delta Lake

Delta Lake is an open-source storage layer that adds reliability to data lakes.

```
DELTA LAKE FEATURES

ACID TRANSACTIONS:
  Write-ahead log (_delta_log/ directory)
  Each commit = JSON file listing file additions + deletions
  Readers always see a consistent snapshot
  Concurrent writers: optimistic concurrency, conflict resolution

TIME TRAVEL:
  SELECT * FROM table TIMESTAMP AS OF '2024-01-01'
  SELECT * FROM table VERSION AS OF 42
  Each version = a snapshot of the table at that commit
  Retention: configurable (default 7 days of logs preserved)
  Use: auditing, reproducing historical model training data, debugging

SCHEMA ENFORCEMENT:
  Inserts with extra/missing columns → rejected by default
  Schema evolution: MERGE SCHEMA option to evolve when needed
  DDL changes logged: ALTER TABLE ADD COLUMN tracked in log

UPSERT (MERGE):
  MERGE INTO target USING source ON condition
  WHEN MATCHED THEN UPDATE
  WHEN NOT MATCHED THEN INSERT
  Full SQL MERGE support (not available in plain Parquet/CSV lakes)

Z-ORDER (OPTIMIZE):
  OPTIMIZE table ZORDER BY (date, user_id)
  Co-locates related data in same files
  Reduces data scan for filters on those columns
  Equivalent: clustering in traditional DW
  Should run periodically (daily/weekly) on large tables

DELETION VECTORS:
  Delta 3.0: soft-delete (mark deleted rows without rewriting files)
  Faster DELETEs and UPDATEs on large tables
```

---

## Azure Data Factory (ADF)

You know ADF deeply — you worked on it. This is context for how it fits the modern data platform:

```
ADF POSITION IN DATA PLATFORM:
  ADF is the orchestration + ingestion layer
  It is NOT for complex transformation (use Spark/SQL for that)
  ADF is best for: moving data, scheduling pipelines, connecting to
                   100+ source connectors

MODERN PATTERN (ADF vs. Databricks Jobs vs. Synapse Pipelines):
  ADF:         Ingest from 100+ external sources (SAP, Salesforce, REST APIs)
               Orchestrate across services (trigger ADB job after ingest)
               Simple transformations in Mapping Data Flows (visual Spark)
               Good for non-engineer built pipelines
  Databricks:  Complex transformations (Spark code), ML, medallion
               Prefer when code control matters
  Synapse:     Pipelines (ADF-identical UI/runtime), Spark, SQL DW together
               Good for Azure-only shops preferring single pane of glass

ADF DATA FLOW:
  Mapping Data Flows: visual ETL with Spark backend
  No code needed for most transformations
  Generates Spark code; runs on ADF-managed cluster
  Debug mode: runs on live cluster with sample data

INTEGRATION RUNTIME TYPES:
  Azure IR: cloud-hosted, no management
  Self-hosted IR: on-premises or other clouds, installed on VM
  Azure-SSIS IR: lift-and-shift SSIS packages to Azure
```

---

## BigQuery and Snowflake (Cross-Cloud Context)

```
BIGQUERY (Google):
  Serverless (no cluster management): query any size, pay per TB scanned
  Columnar storage: Capacitor format internally
  Dremel query engine: petabyte-scale interactive SQL
  Built-in ML: BQML, create ML models in SQL
  Separation of storage + compute: always-on, no pausing clusters
  Best for: GCP-native, serverless analytics, extreme ad hoc scale

SNOWFLAKE (cloud-agnostic, runs on Azure/AWS/GCP):
  Multi-cloud, multi-account data sharing (Snowflake Marketplace)
  Near-zero copy data sharing: share live data across accounts
  Time travel + cloning: zero-copy table clones for dev/test
  Semi-structured: VARIANT type for JSON/Avro/Parquet natively
  Separate compute + storage: virtual warehouses (X-Small to 6X-Large)
  Best for: multi-cloud organizations, data sharing externally,
            enterprise SQL DW with JSON/semi-structured needs

AZURE EQUIVALENT:
  Synapse Dedicated SQL Pool ≈ Snowflake (managed MPP SQL DW)
  Synapse Serverless SQL ≈ BigQuery (scan files in lake, pay per scan)
  Databricks ≈ Databricks (same product on Azure/AWS/GCP)
```

---

## Common Confusion Points

**"ADF and Synapse Pipelines are different"**
Synapse Pipelines is ADF embedded inside Synapse. The pipeline authoring experience, activities, connectors, and integration runtimes are identical. If you're in Synapse workspace and need pipelines, use Synapse Pipelines (no context switch needed).

**"Delta Lake = Databricks proprietary"**
Delta Lake is an open-source project (under the Linux Foundation Delta Lake project). It runs on any Spark distribution — Synapse, open-source Spark, Amazon EMR, and Databricks. Databricks created it and maintains it, but it is not proprietary.

**"Dedicated SQL Pool is always running"**
Dedicated SQL Pool must be paused when not in use — otherwise you pay even when idle. A common cost mistake: forgetting to pause dev/test pools overnight. Use ADF pipeline or PowerShell to auto-pause.

**"Serverless SQL Pool = Dedicated SQL Pool"**
They are fundamentally different engines. Serverless SQL: query files in ADLS, pay per scan, no loading required. Dedicated SQL Pool: load data into distributed storage, fast for repeated queries, pay per DWU-hour. Use Serverless for exploration; Dedicated for production high-performance queries.

---

## Cross-References

- `cloud-architecture/05-MICROSERVICES.md` — service data ownership and integration.
- `data-science/01-NUMPY.md` — analytical compute context downstream of data platforms.
- `query-languages/01-SQL.md` — query interface foundations.

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether ingestion breadth is the hard part | Azure Data Factory | Connectors and scheduling help, but schema drift and integration runtime ownership remain. |
| Whether transformations need complex Spark ecosystem | Databricks or Synapse Spark | Databricks usually has stronger ecosystem; Synapse may fit Azure-integrated estates. |
| Whether lake data needs ad hoc SQL | Synapse Serverless SQL | Pay-per-scan rewards partitioning and file pruning; sloppy layout becomes cost. |
| Whether repetitive SQL needs predictable performance | Synapse Dedicated SQL Pool | Dedicated capacity should pause when idle or it burns money. |
| Whether ML needs training plus experiment tracking | Databricks MLflow plus Azure ML | Split ownership carefully: notebooks, registry, deployment, and governance can fragment. |
| Whether sharing crosses clouds or companies | Snowflake, or Azure Data Share for simpler Azure cases | Data sharing is also contract, lineage, and access governance. |
| Whether lineage/governance is the missing layer | Microsoft Purview | Scanning tools need naming, ownership, and stewardship processes to be useful. |
| Whether the lake needs ACID table semantics | Delta Lake | ACID helps reliability but does not fix bad partitioning or modeling. |
| Whether streams should land in the lake in near-real time | Event Hubs plus Spark Streaming, or Stream Analytics to ADLS | Streaming pipelines need replay, watermarking, and backpressure design. |
