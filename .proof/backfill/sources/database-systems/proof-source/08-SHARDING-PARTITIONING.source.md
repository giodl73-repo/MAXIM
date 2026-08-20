---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-SHARDING-PARTITIONING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:sharding-partitioning
kind: guide
module: database-systems
section: computing-software
title: Sharding and Partitioning - Hash/Range, Rebalancing, 2PC
status: source-custody
source_custody: partial
current_path: database-systems/08-SHARDING-PARTITIONING.md
canonical_path: database-systems/08-SHARDING-PARTITIONING.md
backsource_ids: [proof-backfill:database-systems:08-sharding-partitioning, git-history:database-systems:08-sharding-partitioning]
concepts: [sharding, partitioning, hash partitioning, range partitioning, rebalancing, distributed transaction, two-phase commit, consistent hashing]
root_concepts: [sharding]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Sharding and Partitioning — Splitting Data Across Machines

Replication (guide 07) makes **copies** of the data; it scales reads and availability but every
write still hits the leader, and the whole dataset must fit on one machine. **Partitioning**
(a.k.a. **sharding** when across machines) splits the data into disjoint pieces so writes and
storage scale horizontally. The cost is that operations spanning shards — joins, transactions,
secondary-key lookups — get hard.

```
+=====================================================================================+
|                  PARTITIONING vs REPLICATION — orthogonal axes                      |
+=====================================================================================+
|                                                                                     |
|              REPLICATION (copies)  ------------------------------>                   |
|        (availability, read scale; every node has the SAME data)                     |
|        |                                                                            |
|        |   +---------+   +---------+   +---------+                                   |
|   P    |   | shard A |   | shard B |   | shard C |   <- each shard is a disjoint     |
|   A    |   | replica1|   | replica1|   | replica1|      SLICE of the keyspace        |
|   R    |   +---------+   +---------+   +---------+                                   |
|   T    |   | shard A |   | shard B |   | shard C |   <- and each shard is itself     |
|   I    v   | replica2|   | replica2|   | replica2|      REPLICATED for availability  |
|   T        +---------+   +---------+   +---------+                                   |
|   I        | shard A |   | shard B |   | shard C |                                   |
|   O        | replica3|   | replica3|   | replica3|                                   |
|   N        +---------+   +---------+   +---------+                                   |
|   (storage + write scale; each node has DIFFERENT data)                              |
|                                                                                     |
|   PRODUCTION = BOTH: shard for scale, replicate each shard for availability.         |
+=====================================================================================+
```

The key decision is the **partition key** (shard key) and the **partitioning scheme** that maps
a key to a shard. Get this wrong and you get hotspots, cross-shard transactions everywhere, and
painful rebalancing.

---

## Partitioning schemes

### Range partitioning

Assign contiguous key ranges to shards.

```
   key space:  [A........F][G........M][N........S][T........Z]
   shard:          S1          S2          S3          S4

   + RANGE SCANS are efficient (a range often lives in one or few shards)
   + ordered iteration is natural
   - HOTSPOTS: monotonically increasing keys (timestamps, auto-increment IDs) -> all new
     writes land on the LAST shard. The classic time-series hotspot.
```

### Hash partitioning

Apply a hash to the key, partition by the hash value.

```
   shard = hash(key) mod N    (naive)   OR   hash ranges assigned to shards

   + EVEN distribution -> no hotspot from sequential keys
   - RANGE SCANS are scattered (adjacent keys hash to different shards) -> a range query
     fans out to ALL shards
   - "mod N" is fragile: changing N (adding a shard) remaps ALMOST EVERY key -> see
     consistent hashing below.
```

### Consistent hashing — rebalancing without remapping everything

The fix for "`mod N` remaps everything when N changes." Map both keys and nodes onto a hash ring;
a key belongs to the next node clockwise. Adding/removing a node only moves the keys in **one
arc**, not all keys.

```
                    0 / 2^k
                      *  nodeA
            keyX *         \
                            \      * nodeB
       nodeD *               \    /
              \               \  /
               \               */  keyY -> belongs to nodeB (next clockwise)
                \             /
                 *-----------*  nodeC

   Add nodeE between A and B -> only keys in the A..E arc move (to nodeE). The rest stay put.

   VIRTUAL NODES (vnodes): each physical node owns MANY points on the ring -> smoother balance
   and finer-grained rebalancing. Used by Cassandra, DynamoDB-style systems.
```

> Consistent hashing is treated as a distributed-systems primitive in
> `distributed-systems/04`; here it is specifically the *rebalancing* mechanism for shards.

---

## Rebalancing — moving partitions as the cluster grows

```
   STRATEGY                        BEHAVIOR
   -----------------------------   ----------------------------------------------------------
   hash mod N (DON'T)              adding a node remaps almost all keys -> mass data movement
   FIXED number of partitions      create many more partitions than nodes up front (e.g. 1000
   (e.g. Cassandra-ish, Riak)      partitions over 10 nodes); rebalancing just MOVES whole
                                   partitions between nodes. Count fixed; assignment flexible.
   DYNAMIC partitioning            split a partition when it grows past a threshold, merge when
   (HBase, range systems)         small. Adapts to data volume; like a B-tree split at the
                                   shard level.
   CONSISTENT HASHING + vnodes     adding a node steals a fair share of vnodes from others.

   RULE: do NOT tie the partition count to the NODE count. Decouple them so adding hardware
   moves partitions, not every row.
```

---

## The hard part: operations that span shards

Single-shard operations are easy — they're just a normal local database operation on one node.
Everything that crosses shards is where distributed databases earn their complexity.

```
   CROSS-SHARD JOIN      data for the join lives on different nodes -> must move data over
                         the network (broadcast the small side, or repartition both sides on
                         the join key). Expensive. Co-locate related data to avoid it.

   SECONDARY INDEX       partitioned by the PRIMARY key, but you query by a DIFFERENT column:
                           - LOCAL (document-partitioned) index: each shard indexes its own
                             rows -> a secondary-key query must SCATTER to all shards, GATHER.
                           - GLOBAL (term-partitioned) index: the index itself is partitioned
                             by the indexed term -> a query hits one shard, but WRITES must
                             update a remote index partition (cross-shard write).

   CROSS-SHARD TRANSACTION  a transaction touching rows on multiple shards needs an ATOMIC
                            COMMIT protocol across nodes -> 2PC (below). This is the expensive,
                            availability-reducing operation you design to avoid.
```

**Design principle:** choose the shard key so that the data accessed *together* lives *together*
(co-location). E.g. shard by `customer_id` so a customer's orders, addresses, and payments are
all on one shard → most transactions stay single-shard. This is the highest-leverage decision in
a sharded design.

---

## Two-Phase Commit (2PC) — atomic commit across shards

To make a transaction touching multiple shards atomic (all commit or all abort), you need a
distributed atomic-commit protocol. The canonical one is **two-phase commit**.

```
   ROLES: a COORDINATOR + multiple PARTICIPANTS (the shards in the transaction).

   PHASE 1 - PREPARE (voting)
     coordinator -> all participants: "PREPARE to commit txn T"
     each participant: do the work, write it to its log durably, lock the rows, reply VOTE-COMMIT
        (it now PROMISES it can commit even across a crash) OR VOTE-ABORT.

   PHASE 2 - COMMIT/ABORT (decision)
     if ALL voted commit: coordinator logs "COMMIT", -> tells all participants COMMIT.
     if ANY voted abort:  coordinator logs "ABORT",  -> tells all participants ABORT.
     participants apply the decision, release locks, ack.

           coordinator                         participants (shards)
                |  --- PREPARE ----------------->  |   (do work, fsync, lock, vote)
                |  <-- VOTE-COMMIT / VOTE-ABORT --  |
        decision logged
                |  --- COMMIT / ABORT ----------->  |   (apply, unlock, ack)
                |  <-- ACK ----------------------- |
```

### Why 2PC is feared: the blocking problem

```
   If the COORDINATOR CRASHES after participants voted COMMIT but before sending the decision,
   participants are STUCK in the "prepared" state: they've locked rows and promised to commit,
   but don't know the outcome. They CANNOT unilaterally commit or abort -> they BLOCK, holding
   locks, until the coordinator recovers. 2PC is a BLOCKING protocol; the coordinator is a SPOF.
```

| Property | 2PC | Why it matters |
|----------|-----|----------------|
| Atomicity across nodes | Yes | The whole point |
| Blocking on coordinator failure | **Yes** | Participants hold locks, stall, until coordinator recovers |
| Availability under partition | Reduced | A partitioned participant blocks the commit |
| Latency | 2 round-trips + 2 log fsyncs | Slower than a local commit |

Mitigations and successors:
- **3PC** adds a phase to reduce blocking but assumes synchronous networks and is rarely used.
- **Consensus-based commit**: replace the single coordinator with a **Paxos/Raft** group so the
  commit decision is itself replicated and survives coordinator failure. This is how **Spanner**
  and **CockroachDB** do distributed transactions — 2PC *over* Paxos groups, removing the SPOF
  (guide 09, `distributed-systems/03` and `05`).
- **Sagas**: avoid distributed atomicity entirely — a long-lived sequence of local transactions
  with **compensating** transactions to undo on failure. Trades atomicity for availability;
  you get eventual consistency and must write compensations. Detailed in
  `distributed-systems/05`.

> Bridge: **MSDTC** (Microsoft Distributed Transaction Coordinator) is textbook 2PC — the
> coordinator/participant/prepare/commit you may have used across SQL Server + MSMQ is exactly
> this protocol, with exactly this blocking hazard. Modern distributed databases push the
> coordinator's durability onto a consensus group to escape the SPOF.

---

## Old World → New World Bridges

| You already know | Sharding concept | SQL Server / Azure anchor |
|------------------|------------------|----------------------------|
| Partitioned tables across filegroups | **Partitioning** (single node) vs sharding (across nodes) | Table partitioning |
| Federation / scale-out across DBs | **Sharding** by a partition key | Elastic database / sharding tools |
| Cosmos partition key choice | The shard-key co-location decision | Cosmos logical partition key |
| MSDTC distributed transaction | **Two-phase commit** (and its blocking) | MSDTC; `BEGIN DISTRIBUTED TRAN` |
| A hash ring for cache nodes | **Consistent hashing** for rebalancing | (general) Cosmos physical partitions |
| Compensating workflow on failure | **Saga** pattern | Durable Functions / saga orchestration |

---

## Decision Cheat Sheet

| Need | Choice |
|------|--------|
| Even write distribution, no sequential hotspot | **Hash** partitioning |
| Efficient range scans / ordered access | **Range** partitioning (watch the trailing-shard hotspot) |
| Add/remove nodes without remapping all keys | **Consistent hashing** + virtual nodes, or fixed-partition-count |
| Keep related rows together (avoid cross-shard txn) | Shard by a key that co-locates them (e.g. `customer_id`) |
| Query by a non-shard column | Local index (scatter-gather) or global index (cross-shard write) |
| Atomic transaction across shards | **2PC** (accept blocking) or 2PC-over-consensus (Spanner/Cockroach) |
| Avoid distributed-transaction blocking | **Saga** with compensations (eventual consistency) |
| Scale WRITES | **Shard** (replication only scales reads) |

---

## Common Confusion Points

### "Partitioning and sharding are different things"

Same idea at different scope. **Partitioning** usually means splitting within one server (e.g.
partitioned tables); **sharding** means partitioning across multiple servers. The scheme
(hash/range) and the trade-offs are identical; only the blast radius differs.

### "Hash partitioning kills hotspots, so always use it"

Hash partitioning destroys **ordering**, so range queries and ordered scans fan out to every
shard. If your workload is range-heavy (time-series dashboards, "last N events"), range
partitioning is right despite the hotspot risk — which you mitigate by prefixing the key with
something high-cardinality (a bucket or hash prefix), not by switching to pure hash.

### "Adding a shard is easy"

Only if you didn't shard by `hash mod N`. Plain `mod N` remaps almost every key when N changes —
a full data reshuffle. **Consistent hashing** or a **fixed large partition count** (decoupled
from node count) is what makes adding capacity cheap. Decide this before you shard.

### "2PC gives me distributed ACID for free"

2PC gives atomicity but is a **blocking** protocol with a single-point-of-failure coordinator: a
coordinator crash leaves participants stuck holding locks. It also adds latency (two round-trips
+ fsyncs) and reduces availability under partitions. Modern systems either run 2PC *over* a
consensus group (Spanner/CockroachDB) or avoid it with sagas.

### "A secondary index on a sharded table works like on a single node"

No — you must choose **local** (each shard indexes its own data; queries scatter-gather across
all shards) or **global** (index partitioned by the indexed term; point queries hit one shard
but every write may update a remote index partition). Both have costs a single-node index
doesn't. This often dominates the shard-key choice.
