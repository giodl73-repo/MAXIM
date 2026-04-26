# Distributed Databases: Spanner, CockroachDB, DynamoDB — Design Choices

## The Big Picture

Distributed databases make different trade-offs across the same dimensions: consistency model, availability, query model, sharding strategy, and operational complexity.

```
DISTRIBUTED DATABASE LANDSCAPE
+-----------------------------------------------------------------------+
|                                                                       |
|  CONSISTENCY AXIS                                                     |
|  Strong ──────────────────────────────────────── Eventual             |
|     |                                                 |               |
|  Spanner        CockroachDB   CosmosDB   CosmosDB  DynamoDB           |
|  (TrueTime)     (HLC)         (Strong)   (Eventual) (AP default)      |
|  FoundationDB                 Azure SQL                               |
|                                                                       |
|  QUERY MODEL AXIS                                                     |
|  SQL ──────────────────────────────── Document/KV/Graph               |
|     |                                          |                      |
|  Spanner        CockroachDB   CosmosDB(SQL)  DynamoDB   Cassandra     |
|  FoundationDB                 CosmosDB(Mongo)            Redis        |
|                                                                       |
|  SCALE AXIS                                                           |
|  Single-DC ──────────────────────────── Globally distributed          |
|     |                                          |                      |
|  PostgreSQL     CockroachDB   CosmosDB         Spanner                |
|  (single node)  (multi-region) (multi-region)  (global)               |
+-----------------------------------------------------------------------+
```

---

## Google Spanner

**Origin**: Google (2012 paper, Cloud Spanner GA 2017)
**Consistency**: External consistency (strict serializability globally)
**Model**: Globally distributed SQL

### Architecture

```
SPANNER ARCHITECTURE
+----------------------------------------------------------+
|                    GLOBAL                                |
|  +-------------------+   +-------------------+           |
|  | Zone A (US-East)  |   | Zone B (EU-West)  |  ...     |
|  +-------------------+   +-------------------+           |
|  |  Tablet servers   |   |  Tablet servers   |           |
|  |  (data shards)    |   |  (data shards)    |           |
|  +-------------------+   +-------------------+           |
|          |                        |                       |
|          +----------+-------------+                       |
|                     |                                     |
|          Paxos groups (per shard)                         |
|          (majority = cross-zone quorum)                   |
|                     |                                     |
|         TrueTime API (atomic clock + GPS)                 |
|         provides bounded timestamp uncertainty            |
+----------------------------------------------------------+

WRITE PATH
  Client → any zone → route to Paxos leader for that shard
  Leader proposes → quorum acks → commit with TrueTime timestamp
  Commit wait: 2ε (~2-14ms) before returning to client
  → External consistency guaranteed

READ PATH (strong)
  Read at current TrueTime → waits for safe time
  → guaranteed to see all commits before read timestamp

READ PATH (stale)
  Read at timestamp T (seconds ago)
  → served from any replica (no quorum needed)
  → lower latency for analytics
```

### TrueTime Revisited

Spanner's TrueTime uses GPS receivers and atomic clocks in each datacenter. The uncertainty window ε is typically 1–7ms. Commit wait blocks for 2ε per transaction. This is the hardware investment that enables external consistency at global scale — no other system does this without hardware.

**Cloud Spanner product**: Available as Google Cloud Spanner. External consistency is maintained. Typical write latency single-region ~5ms, multi-region ~20ms+.

### When to Use Spanner

- Global SQL transactions that must be serializable
- Financial systems where stale reads are unacceptable
- You have budget for Cloud Spanner pricing
- You need SQL (complex queries, joins, indexes)

---

## CockroachDB

**Origin**: Cockroach Labs (open source, 2015; inspired by Spanner)
**Consistency**: Serializable (not externally consistent, but very close)
**Model**: Distributed SQL (PostgreSQL wire-compatible)

### Architecture

```
COCKROACHDB ARCHITECTURE
+----------------------------------------------------------+
| Nodes (any number, add for scale)                        |
+----------------------------------------------------------+
| SQL Layer   (standard PostgreSQL-compatible SQL)         |
+----------------------------------------------------------+
| Transaction Layer (serializable isolation, 2PC-like)     |
+----------------------------------------------------------+
| Distribution Layer (range-based sharding)                |
|   Key space split into ~64MB ranges                      |
|   Each range: Raft group (3 replicas by default)         |
+----------------------------------------------------------+
| Replication Layer (Raft per range)                       |
+----------------------------------------------------------+
| Storage Layer (RocksDB/Pebble, LSM-tree)                 |
+----------------------------------------------------------+

SHARDING: Ranges are contiguous key ranges, automatically split/merged
CONSENSUS: Each range has its own Raft group
CLOCK: Hybrid Logical Clocks (HLC) instead of TrueTime
```

### Hybrid Logical Clocks (HLC)

Without atomic clocks, CockroachDB uses HLC: a combination of physical wall clock time and a logical counter. HLC allows CockroachDB to achieve serializability across nodes with normal commodity hardware.

The trade-off vs. Spanner: HLC has unbounded clock skew (mitigated by NTP, typically ~500ms in worst case). CockroachDB handles this with uncertainty intervals — any transaction is aware of the clock skew bound and reads "around" it. This means CockroachDB's transactions are serializable but not externally consistent in the strict Spanner sense.

### When to Use CockroachDB

- PostgreSQL-compatible SQL at scale
- Self-hosted (no Google Cloud dependency)
- Strong consistency without Spanner pricing
- Horizontal scaling of relational workloads

---

## Amazon DynamoDB

**Origin**: Amazon (2007 Dynamo paper, DynamoDB product 2012)
**Consistency**: Eventual (AP by default), strong available with cost
**Model**: Key-value / document

### Architecture

```
DYNAMODB ARCHITECTURE
+----------------------------------------------------------+
| Table = collection of items (no schema except PK)        |
| Item = up to 400KB, JSON-like attributes                 |
+----------------------------------------------------------+
| PRIMARY KEY:                                             |
|   Partition key only (hash)     → single-attribute PK   |
|   Partition key + sort key      → composite PK          |
+----------------------------------------------------------+
| STORAGE:                                                 |
|   3 AZ replicas per table region (sync replication)      |
|   Consistent hash ring → auto-sharding                   |
+----------------------------------------------------------+
| CONSISTENCY OPTIONS:                                     |
|   Eventually consistent reads (default) → read 1 replica |
|   Strongly consistent reads (2x read units) → read quorum|
+----------------------------------------------------------+
| GLOBAL TABLES:                                           |
|   Multi-region, multi-master replication                 |
|   Conflict resolution: last-write-wins                   |
+----------------------------------------------------------+
```

### Single-Table Design

DynamoDB performance depends heavily on access pattern design. The schema must be designed around access patterns upfront (unlike SQL where you normalize and add indexes later).

```
TRADITIONAL (SQL approach)       DYNAMODB SINGLE-TABLE DESIGN
Users table                      Single table with GSI/LSI overloading:
Orders table                     PK           SK              type
OrderItems table                 USER#123     PROFILE#123     user
                                 USER#123     ORDER#456       order
JOIN on query                    ORDER#456    ITEM#1          item
                                 ORDER#456    ITEM#2          item

Query users and orders:          Query PK=USER#123, SK begins with ORDER#
  SELECT * FROM users            → returns all orders for user in one query
  JOIN orders ON id=user_id      → no cross-partition scan
```

Access patterns drive the schema. The Dynamo single-table model is optimal for known, high-throughput access patterns and suboptimal for ad hoc query exploration.

---

## Azure Cosmos DB

**Origin**: Microsoft Azure (DocumentDB 2014, CosmosDB 2017)
**Consistency**: 5 levels, tunable per request
**Model**: Multi-model (document, key-value, column-family, graph, table)

### Architecture

```
COSMOSDB ARCHITECTURE
+----------------------------------------------------------+
| Account (globally distributed resource)                  |
|   Regions: write region(s) + read regions                |
|   Multi-master: optional (multiple write regions)        |
+----------------------------------------------------------+
| Database → Containers (collections)                      |
|   Container = partitioned collection                     |
|   Partition key determines shard placement               |
+----------------------------------------------------------+
| Physical partitions                                      |
|   Each physical partition: ~50GB max                     |
|   Replicated 4 times within a region (quorum)            |
|   Replicated across regions via async log replication    |
+----------------------------------------------------------+
| Consistency level per request (5 options)                |
|   Default: set at account, override per read             |
+----------------------------------------------------------+

STRONG: Linearizability. Single-write-region only.
        Cross-region reads wait for replication.
        Highest latency, but reads never stale.

BOUNDED STALENESS: Reads lag by at most K operations or T seconds.
                   Good for globally distributed apps needing order.

SESSION: Read-your-writes within a session token.
         Most apps use this. Balance of consistency and performance.

CONSISTENT PREFIX: Reads see operations in order, but may lag.
                   No isolated stale reads; causal ordering maintained.

EVENTUAL: Fastest reads. No ordering guarantee. Reads may be stale.
          Maximum throughput and availability.
```

### Azure DevOps and CosmosDB

Azure DevOps services use CosmosDB (and Azure SQL) internally. Work item queries typically use Session consistency — you see your own writes immediately, other team members' writes propagate within seconds. The consistency level is a product decision that affects user-visible behavior.

---

## Apache Cassandra

**Origin**: Facebook (2008), Apache project
**Consistency**: AP by default, tunable toward CP
**Model**: Wide-column store

### Architecture

```
CASSANDRA RING TOPOLOGY
+----------------------------------------------------------+
|                                                          |
|        Node1 ────── Node2                                |
|       /                    \                             |
|    Node5                  Node3                          |
|       \                    /                             |
|        Node4 ────── (Node4)                              |
|                                                          |
| Consistent hashing: each node owns a token range         |
| Replication factor: each key replicated to RF nodes      |
| (adjacent in ring by token)                              |
|                                                          |
| WRITE:                                                   |
|   Client → coordinator (any node) → W replica nodes      |
|   Coordinator waits for W acks (W = quorum setting)      |
|                                                          |
| READ:                                                    |
|   Client → coordinator → R replica nodes                 |
|   Coordinator returns latest (by timestamp), repairs     |
|   stale replicas (read repair)                           |
+----------------------------------------------------------+
```

### Tunable Consistency in Cassandra

```
CONSISTENCY LEVELS (per operation):
  ONE: 1 replica must ack. Fast, AP.
  QUORUM: majority must ack. Balanced CP/AP.
  ALL: all replicas must ack. Slow, CP.
  LOCAL_QUORUM: quorum in local DC only. Good for multi-DC.
  EACH_QUORUM: quorum in each DC. Strong cross-DC.

QUORUM MATH:
  RF=3, W=QUORUM(2), R=QUORUM(2): W+R=4 > RF=3 → strong consistency
  RF=3, W=ONE(1), R=ONE(1): W+R=2 <= RF=3 → eventual consistency
```

---

## FoundationDB

**Origin**: Apple acquisition 2015; previously independent
**Consistency**: ACID, serializable
**Model**: Ordered key-value; higher-level models as layers

### Why FoundationDB Is Unusual

FoundationDB is strictly serializable (ACID transactions) on a distributed KV store. Its design insight: keep the core simple (ordered KV with transactions), build everything else as layers (document model, table model, SQL) on top.

**Simulation testing**: FoundationDB uses a deterministic discrete-event simulation for testing — the entire distributed system is run inside a simulator with controlled fault injection. This is arguably the most rigorous testing approach in distributed databases. Engineers at FoundationDB famously found bugs in this simulator that would have caused data corruption in production.

**Used by**: Snowflake (metadata), Apple (iCloud backend), many internal Apple services.

---

## Selection Criteria Table

| Criterion | Spanner | CockroachDB | DynamoDB | CosmosDB | Cassandra | FoundationDB |
|-----------|---------|-------------|----------|----------|-----------|-------------|
| SQL support | Full | Full (Postgres compat) | None | SQL API (partial) | CQL (SQL-like) | None (layered) |
| Global consistency | External | Serializable | Eventual/Strong | 5 levels | Tunable | Serializable |
| Operational model | Fully managed (GCP) | Self-hosted or managed | Fully managed (AWS) | Fully managed (Azure) | Self-hosted or managed | Self-hosted |
| Scale model | Horizontal (shards + Raft) | Horizontal (ranges + Raft) | Serverless/provisioned | Serverless/provisioned | Ring (manual) | Horizontal |
| Write multi-region | Yes (Paxos across zones) | Yes | Yes (Global Tables) | Yes (multi-master) | Yes (multi-DC) | Limited |
| Best for | Global financial SQL | Multi-region PostgreSQL | High-throughput KV/doc | Azure-native, any model | Write-heavy, time-series | Metadata, layer-based |

---

## Common Confusion Points

**"CosmosDB is just a document store"**
CosmosDB is multi-model: it supports document (MongoDB API), key-value (Table API), graph (Gremlin API), column-family (Cassandra API), and SQL API. The underlying storage engine is the same; the APIs are protocol translators.

**"DynamoDB is slow"**
DynamoDB single-digit millisecond reads are extremely fast for its access pattern model. It is slow for ad hoc queries and table scans — it was not designed for those. Know your access patterns before choosing.

**"CockroachDB = Spanner"**
CockroachDB is inspired by Spanner but does not use TrueTime. The result is serializable (not externally consistent) and uses commodity hardware. The practical difference matters for cross-region transactions.

**"Cassandra is unreliable"**
Cassandra is AP — it trades consistency for availability and write throughput. For the use cases it was designed for (time-series, write-heavy, high throughput), it is extremely reliable. Using it for transactional data is the misuse, not the tool.
