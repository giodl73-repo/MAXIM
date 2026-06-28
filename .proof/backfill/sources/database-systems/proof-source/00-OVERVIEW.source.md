---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:overview
kind: guide
module: database-systems
section: computing-software
title: Anatomy of a Database Engine - Landscape
status: source-custody
source_custody: partial
current_path: database-systems/00-OVERVIEW.md
canonical_path: database-systems/00-OVERVIEW.md
backsource_ids: [proof-backfill:database-systems:00-overview, git-history:database-systems:00-overview]
concepts: [database engine, storage engine, query processor, transaction manager, recovery, replication, sharding]
root_concepts: [database engine]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Anatomy of a Database Engine — The Landscape

A database is not one thing. It is a **stack of cooperating subsystems**, each solving a
different hard problem, nested so that the guarantees of the top layer rest on the mechanisms
of the layers below. The query language you write (`SELECT ... WHERE ...`) sits at the very
top. This directory is everything *underneath* that line.

```
+===================================================================================+
|                          A DATABASE ENGINE, TOP TO BOTTOM                          |
+===================================================================================+
|                                                                                   |
|   CLIENT / WIRE PROTOCOL        SQL text, parameters, result rows over a socket    |
|   (TDS, PostgreSQL fe/be, etc.)                                                    |
|         |                                                                         |
|         v                                                                         |
|   +---------------------------------------------------------------------------+   |
|   |  QUERY PROCESSOR                                  [ guide 03 ]             |   |
|   |  parse -> bind -> logical plan -> COST-BASED OPTIMIZER -> physical plan    |   |
|   |  -> executor (iterators / vectorized). Uses STATISTICS to pick joins.      |   |
|   +---------------------------------------------------------------------------+   |
|         |                            ^                                            |
|         | reads/writes rows          | "give me rows matching X, fast"           |
|         v                            |                                            |
|   +---------------------------------------------------------------------------+   |
|   |  ACCESS METHODS / INDEXES                         [ guide 02 ]             |   |
|   |  B+tree, hash, bitmap, covering, composite, inverted. The data structures |   |
|   |  that turn O(n) scans into O(log n) lookups.                              |   |
|   +---------------------------------------------------------------------------+   |
|         |                                                                         |
|         v                                                                         |
|   +---------------------------------------------------------------------------+   |
|   |  TRANSACTION & CONCURRENCY CONTROL                [ guides 04, 05 ]        |   |
|   |  ACID. MVCC version chains, 2PL locks, snapshot isolation. Decides what    |   |
|   |  one transaction is allowed to SEE while others run concurrently.          |   |
|   +---------------------------------------------------------------------------+   |
|         |                                                                         |
|         v                                                                         |
|   +---------------------------------------------------------------------------+   |
|   |  STORAGE ENGINE                                   [ guide 01 ]             |   |
|   |  Pages, the BUFFER POOL (cache), heap files, B-tree files OR LSM-trees.    |   |
|   |  How a logical row becomes bytes on a block device.                       |   |
|   +---------------------------------------------------------------------------+   |
|         |                                                                         |
|         v                                                                         |
|   +---------------------------------------------------------------------------+   |
|   |  DURABILITY & RECOVERY                            [ guide 06 ]             |   |
|   |  Write-Ahead Log (WAL), ARIES, checkpoints, crash recovery. Makes the "D"  |   |
|   |  in ACID true across power loss.                                           |   |
|   +---------------------------------------------------------------------------+   |
|                                                                                   |
+===================================================================================+
|         |                                                                         |
|         v   (the WAL is also the thing we SHIP to other machines)                 |
|   +---------------------------------------------------------------------------+   |
|   |  REPLICATION  [07]  ->  SHARDING/PARTITIONING [08]  ->  DISTRIBUTED SQL [09] |
|   |  One node's durable log becomes many nodes' shared state. CAP enters here. |   |
|   +---------------------------------------------------------------------------+   |
+===================================================================================+
```

**Read it top-down for a query, bottom-up for a guarantee.** A `SELECT` enters at the
processor and descends to fetch bytes. A durability or isolation *promise* is built from the
bottom: the WAL guarantees durability, the storage engine guarantees a row exists somewhere,
MVCC guarantees what you see, the optimizer guarantees it found the rows efficiently.

---

## The One Idea That Organizes Everything: Nesting of Guarantees

The reason databases are hard to reason about is that each guarantee is **implemented in terms
of a weaker mechanism one layer down**. You cannot understand isolation levels without MVCC.
You cannot understand MVCC durability without the WAL. You cannot understand the WAL's payoff
without the buffer pool. Here is the dependency chain made explicit.

```
   "SERIALIZABLE isolation"           <- the promise (guide 05)
        depends on
   MVCC version chains + SSI or 2PL   <- the concurrency mechanism (guide 04)
        depends on
   tuple versions stored on pages     <- the storage layout (guide 01)
        depends on
   pages cached in the buffer pool    <- the cache (guide 01)
        made durable by
   the write-ahead log + checkpoints  <- durability (guide 06)
        shipped over the network as
   a replication stream               <- replication (guide 07)
        partitioned across nodes by
   a sharding key + 2PC/consensus      <- scale-out (guides 08, 09)
```

Every guide in this directory is one rung of that ladder.

---

## Two Foundational Forks

Before the details, two architectural forks decide most of a database engine's personality.

### Fork 1 — How is the storage engine organized? (guide 01)

```
                    +---------------------------+
                    |  How do we lay out data?  |
                    +---------------------------+
                       /                      \
                      v                        v
        +--------------------------+   +--------------------------+
        |  IN-PLACE (B-tree / heap)|   |  LOG-STRUCTURED (LSM)    |
        +--------------------------+   +--------------------------+
        | Mutate the page where    |   | Never mutate in place.   |
        | the row lives. Random    |   | Append to a memtable,    |
        | writes. Read-optimized.  |   | flush sorted runs, merge |
        |                          |   | them in the background.  |
        | Postgres, InnoDB (MySQL),|   | Write-optimized.         |
        | SQL Server, SQLite, all  |   |                          |
        | classic OLTP engines.    |   | RocksDB, LevelDB,        |
        |                          |   | Cassandra, ScyllaDB,     |
        |                          |   | the storage under many   |
        |                          |   | NewSQL engines.          |
        +--------------------------+   +--------------------------+
```

### Fork 2 — How do concurrent transactions avoid stepping on each other? (guide 04)

```
        +-----------------------------+   +-----------------------------+
        |  PESSIMISTIC (locking, 2PL) |   |  OPTIMISTIC (MVCC, versions)|
        +-----------------------------+   +-----------------------------+
        | Acquire a lock BEFORE you   |   | Let everyone read a         |
        | touch a row. Writers block  |   | consistent SNAPSHOT. Writers|
        | readers (in classic 2PL).   |   | create new versions; readers|
        | "Assume conflict."          |   | never block. "Assume no     |
        |                             |   | conflict; detect at commit."|
        | Classic SQL Server (without |   |                             |
        | RCSI), DB2.                 |   | Postgres, Oracle, InnoDB,   |
        |                             |   | SQL Server RCSI/SI, Cosmos. |
        +-----------------------------+   +-----------------------------+
```

Almost every modern OLTP engine has converged on **MVCC for reads** (optimistic for readers)
while still using **locks for write-write conflicts**. That hybrid is the dominant design and
guide 04 dissects it.

---

## Where Each Real System Sits

Factual anchors you can trust throughout this directory:

| System | Storage engine | Concurrency / default isolation | Notes |
|--------|----------------|----------------------------------|-------|
| **PostgreSQL** | Heap + B-tree, in-place | MVCC; default **Read Committed** | MVCC by tuple versioning; old versions vacuumed |
| **MySQL / InnoDB** | Clustered B+tree (index-organized) | MVCC; default **Repeatable Read** | RR uses gap locks → blocks many phantoms |
| **SQL Server** | Heap or clustered B+tree | Locking default **Read Committed**; RCSI/SI add MVCC | Snapshot isolation is opt-in per DB |
| **SQLite** | B-tree, single file | Database-level locking; WAL mode | Serializable-ish via coarse locking |
| **Oracle** | Heap + B-tree | MVCC via undo segments; **Read Committed** default | "Serializable" is actually snapshot isolation |
| **RocksDB / LevelDB** | LSM-tree | Library; pluggable | Storage engine *inside* other databases |
| **Cassandra / Scylla** | LSM-tree | Tunable consistency, no cross-row txn (classic) | AP-leaning, quorum reads/writes |
| **Spanner** | Colossus + tablets | External consistency via **TrueTime** + Paxos | The NewSQL gold standard (guide 09) |
| **CockroachDB** | Pebble (LSM, RocksDB-like) | Serializable via Raft + MVCC | Spanner-inspired, no TrueTime hardware |
| **Cosmos DB** | Multi-model, partitioned | **5 consistency levels** (Strong→Eventual) | Tunable per-request (guide 09) |

> Precision note: Oracle and PostgreSQL both implement their `SERIALIZABLE`-named or default
> levels on snapshot machinery, but they differ — PostgreSQL's `SERIALIZABLE` is true
> **Serializable Snapshot Isolation (SSI)** and prevents write skew; Oracle's `SERIALIZABLE`
> is plain snapshot isolation and does **not**. Guide 05 makes this exact.

---

## Old World → New World Bridges

These hold for any senior engineer regardless of stack; the SQL Server / Azure column is
additive context for this reader.

| You already know (old world) | The internals concept (new world) | SQL Server / Azure anchor |
|------------------------------|-----------------------------------|----------------------------|
| A filesystem block cache | The **buffer pool** — the DB's own page cache, bypassing the OS cache | SQL Server buffer pool, `max server memory` |
| `fsync()` to guarantee a write hit disk | WAL flush + group commit before acknowledging COMMIT | `WRITELOG` waits, log flush |
| A clustered index = the table itself | **Index-organized / clustered** storage (InnoDB, SQL Server) | Clustered index IS the table |
| Optimistic concurrency (a version/rowversion column you checked) | **MVCC** — the engine does this for every row automatically | `rowversion`/`timestamp`, RCSI |
| A query plan you read in a profiler | The **physical plan** the cost-based optimizer chose | `SET SHOWPLAN_XML`, Query Store |
| A transaction log you backed up | The **WAL** — same artifact, also drives replication | SQL Server transaction log, AG log shipping |
| Read replicas behind a load balancer | **Leader-follower replication** with async/sync lag | Always On readable secondaries |
| A partitioned table across filegroups | **Sharding / horizontal partitioning** by key | Elastic pools, Cosmos partition keys |
| Two-phase commit across resource managers (MSDTC) | **2PC** for distributed transactions — same protocol | MSDTC, distributed transactions |

---

## How To Read This Directory

```
   START  ->  00 OVERVIEW (you are here)
                 |
   STORAGE  ->  01 STORAGE-ENGINES   (pages, buffer pool, B-tree vs LSM, amplification)
                 |
   ACCESS   ->  02 INDEXING          (B+tree, hash, covering, composite, bitmap, inverted)
                 |
   QUERY    ->  03 QUERY-PROCESSING  (parse->plan->optimize->execute, joins, statistics)
                 |
   CONCURR  ->  04 TRANSACTIONS-MVCC (ACID, MVCC, 2PL, snapshot mechanics)
                 |
   CORRECT  ->  05 ISOLATION-LEVELS  (the 4 levels + anomalies, serializable vs SSI)
                 |
   DURABLE  ->  06 WAL-AND-RECOVERY  (WAL, ARIES, checkpoints, crash recovery)
                 |
   SCALE    ->  07 REPLICATION       (sync/async, quorum, conflict resolution)
                 |
                 08 SHARDING-PARTITIONING (hash/range, rebalancing, 2PC)
                 |
                 09 DISTRIBUTED-SQL   (Spanner/CockroachDB/Cosmos, CAP, consistency spectrum)
```

Read 01→06 in order: each builds on the last. 07→09 form the scale-out arc and lean heavily on
`distributed-systems/` (CAP, consensus, Paxos/Raft).

---

## What This Directory Is NOT

```
   query-languages/  =  the SYNTAX above the line  (SELECT, window fns, T-SQL, PL/pgSQL)
   database-systems/ =  the ENGINE below the line  (pages, MVCC, WAL, optimizer, sharding)
```

If your question is "how do I phrase this query," that is `query-languages/`. If your question
is "*why* did the engine choose a hash join, and how does it keep my read consistent while
someone else updates the row," that is here.

---

## Decision Cheat Sheet

| The question is really about... | Go to guide |
|---------------------------------|-------------|
| Why is my write-heavy table slow / what is write amplification? | 01 Storage Engines |
| Should this be a B-tree or LSM workload? | 01 Storage Engines |
| Why isn't my index being used / what is a covering index? | 02 Indexing |
| Why did the optimizer pick a bad plan / stale statistics? | 03 Query Processing |
| Why are two transactions deadlocking / blocking? | 04 Transactions & MVCC |
| "Is Read Committed safe enough here?" / phantom reads / write skew | 05 Isolation Levels |
| "Will I lose data on a crash?" / why is COMMIT slow? | 06 WAL & Recovery |
| Replica lag, failover, split-brain | 07 Replication |
| "How do I shard this 10 TB table?" / 2PC | 08 Sharding & Partitioning |
| "Strong vs eventual consistency across regions" / Spanner vs Cosmos | 09 Distributed SQL |

---

## Common Confusion Points

### "Isn't the database just a B-tree on disk?"

That is the *storage engine* — one of six layers. The B-tree knows nothing about transactions,
isolation, the optimizer, or replication. Treating the whole DB as "a B-tree" is like treating
a compiler as "a parser."

### "MVCC means no locks, right?"

No. MVCC removes **read locks** (readers don't block writers and vice versa) but write-write
conflicts still need locking or abort-and-retry. Postgres takes row locks on `UPDATE`; SQL
Server SI uses optimistic conflict detection and aborts the loser. Guide 04 details this.

### "The transaction log and the WAL are different things"

They are the same artifact under different names. SQL Server calls it the transaction log;
Postgres calls it the WAL; the academic protocol is ARIES write-ahead logging (guide 06). The
log that makes you durable is also the stream you replicate (guide 07).

### "Distributed SQL gives me everything for free"

CAP still applies. Spanner achieves external consistency by paying a latency cost (commit-wait
on TrueTime bounds); Cosmos lets you *dial* consistency vs latency per request. There is no
free lunch — guide 09 shows exactly what you trade.
