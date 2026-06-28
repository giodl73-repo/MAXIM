---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:distributed-sql
kind: guide
module: database-systems
section: computing-software
title: Distributed SQL - Spanner, CockroachDB, Cosmos, CAP, Consistency Spectrum
status: source-custody
source_custody: partial
current_path: database-systems/09-DISTRIBUTED-SQL.md
canonical_path: database-systems/09-DISTRIBUTED-SQL.md
backsource_ids: [proof-backfill:database-systems:09-distributed-sql, git-history:database-systems:09-distributed-sql]
concepts: [distributed sql, newsql, spanner, cockroachdb, cosmos db, CAP theorem, consistency spectrum, external consistency, truetime]
root_concepts: [distributed sql]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Distributed SQL (NewSQL) — Scale-Out Without Giving Up Transactions

For two decades the trade was forced: choose **SQL + ACID on one big machine** (vertical scale,
a ceiling) or **NoSQL + eventual consistency** that scales horizontally but drops transactions
and joins. **NewSQL / Distributed SQL** is the class of systems (Spanner, CockroachDB, YugabyteDB,
TiDB, Cloud Spanner, and to a degree Cosmos DB) that aim to deliver horizontal scale **and**
strong consistency **and** the SQL/transaction model — by composing the machinery from guides
06–08 (WAL, replication, sharding, 2PC) on top of a **consensus** core
(`distributed-systems/03`).

```
+=====================================================================================+
|                 THE THREE ERAS, AND WHAT EACH GAVE UP                                |
+=====================================================================================+
|                                                                                     |
|   "OLD SQL" (single-node RDBMS)   NoSQL (Dynamo/Cassandra/Mongo)   NewSQL / Dist-SQL  |
|   -----------------------------   ----------------------------    ----------------    |
|   + ACID, SQL, joins, txns        + horizontal scale              + horizontal scale  |
|   + strong consistency            + high availability             + ACID + SQL + txns |
|   - scales UP only (a ceiling)    - eventual consistency          + strong consistency|
|   - SPOF without HA add-ons       - no multi-row txn (classic)    - latency cost for   |
|                                   - no joins / limited queries      cross-region commit|
|                                                                    - operational depth |
|                                                                                     |
|   Postgres, MySQL, SQL Server,    Cassandra, DynamoDB, MongoDB,    Spanner, CockroachDB|
|   Oracle (single-node)            Riak (classic)                  YugabyteDB, TiDB     |
+=====================================================================================+
```

The thesis of NewSQL: the CAP "you must give up consistency to scale" framing was about
*specific designs*, not a law forcing eventual consistency. By paying a **latency** cost (not a
consistency cost) you can keep strong guarantees while scaling out — within the limits CAP and
PACELC actually impose.

---

## CAP — stated precisely (the part everyone gets wrong)

CAP (Brewer's conjecture; Gilbert–Lynch 2002 proof) says: when a network **partition (P)**
occurs, a distributed system must choose between **consistency (C, linearizability)** and
**availability (A, every request gets a non-error response)**. It cannot have both *during a
partition*.

```
   CAP IS A CHOICE THAT ONLY APPLIES DURING A PARTITION:

        partition happens
              |
        +-----+-----+
        |           |
        v           v
     keep C       keep A
     (refuse/      (answer
      block        from one
      writes on    side ->
      minority     may serve
      side)        stale/diverge)
     => CP system   => AP system

   WHEN THERE IS NO PARTITION (the normal case), you can have BOTH C and A.
   So CAP does NOT say "pick 2 of 3 always" — it says "during a partition, C xor A."
```

Common misreadings to avoid (all corrected here):
- **CA is not a real category** for a distributed system — you cannot "give up partition
  tolerance"; partitions happen whether you planned for them or not. The meaningful choice is
  CP vs AP.
- The **C in CAP is linearizability**, not ACID consistency (guide 04) — different thing, same
  letter.
- CAP only constrains behavior **during a partition**; it says nothing about the (common)
  no-partition case.

### PACELC — the more complete statement

CAP ignores the cost in the normal case. **PACELC** (Abadi 2012) extends it:

```
   IF (P)artition:  choose (A)vailability or (C)onsistency
   ELSE (no partition):  choose (L)atency or (C)onsistency

   PA/EL  = available under partition, low-latency normally (Dynamo, Cassandra default)
   PC/EC  = consistent under partition, consistent (higher-latency) normally (Spanner-like)
   PA/EC, PC/EL ... other combinations exist.
```

PACELC is the better lens for NewSQL: even with no partition, strong consistency across regions
costs **latency** (a cross-region round trip / commit-wait). NewSQL systems are generally
**PC/EC** — they keep consistency and pay latency.

---

## The consistency spectrum

A single axis from "every read sees the latest write" to "reads may be arbitrarily stale,"
treated formally in `distributed-systems/02`. The NewSQL-relevant landmarks:

```
   STRONGEST  ----------------------------------------------------------->  WEAKEST
   linearizable   sequential   bounded     causal      session    eventual
   (external                   staleness   consistency consistency
    consistency)
       |             |            |           |            |          |
   read sees      a single    reads lag    causally    your own    converges
   the latest     global      by <= T or   related     reads/      eventually;
   committed      order, not  K versions   writes seen  writes      no ordering
   write          real-time                in order     consistent  guarantee
   (Spanner)      (some        (Cosmos)     (Cosmos)    (Cosmos     (Dynamo,
                  systems)                              default)    Cassandra)
```

Stronger consistency = more coordination = more latency and less availability under partition.
The whole game is choosing the weakest level that still satisfies correctness.

---

## How the marquee systems actually achieve it

### Google Spanner — external consistency via TrueTime

```
   SPANNER (Corbett et al., OSDI 2012)
   - data sharded into "splits"; each split replicated by a PAXOS group across zones/regions.
   - transactions across splits use 2PC, with each participant a Paxos group (no coordinator
     SPOF -> the 2PC-over-consensus pattern from guide 08).
   - GUARANTEE: "external consistency" (= linearizability for transactions): if txn T1 commits
     before T2 starts, T1's commit timestamp < T2's. The strongest practical guarantee.

   THE TRICK — TrueTime: a clock API that returns an INTERVAL [earliest, latest] with a BOUNDED
   uncertainty (epsilon, a few ms), backed by GPS + atomic clocks in every datacenter.
   On commit, Spanner waits out the uncertainty ("COMMIT-WAIT": sleep until the timestamp is
   guaranteed in the past everywhere) so timestamp order == real-time commit order.

        choose commit timestamp s = TT.now().latest
        COMMIT-WAIT until TT.now().earliest > s   (a few ms)
        => no other txn can have committed "before" with a later-looking timestamp.

   COST: that commit-wait latency, plus cross-region Paxos round-trips. Pays LATENCY for
   external consistency. Classic PC/EC.
```

> Spanner's reliance on **specialized GPS/atomic-clock hardware** for TrueTime is the detail
> that makes it Google-specific; the bounded-uncertainty clock is the load-bearing idea.

### CockroachDB — Spanner's ideas without the atomic clocks

```
   COCKROACHDB
   - inspired by Spanner; uses RAFT (not Paxos) per range, MVCC, 2PC across ranges.
   - storage engine: PEBBLE (an LSM-tree, RocksDB-family) -> guide 01.
   - DEFAULT isolation: SERIALIZABLE (SSI lineage) -> strongest, no write skew (guide 05).
   - NO TrueTime hardware: uses HLC (hybrid logical clocks) + a configured max clock OFFSET;
     on uncertainty it may RESTART a transaction rather than commit-wait. Linearizable per key;
     not globally external-consistent like Spanner, but serializable.
   - speaks the PostgreSQL wire protocol -> drop-in-ish for Postgres clients.
```

### Azure Cosmos DB — tunable consistency as a product knob

```
   COSMOS DB
   - globally distributed, multi-model; partitioned by a logical partition key (guide 08).
   - FIVE well-defined consistency levels, selectable per account and overridable per request:
       STRONG        linearizable (single-region writes; no stale reads). Highest latency.
       BOUNDED       staleness bounded by K versions OR T time; reads lag by at most that.
       SESSION       (DEFAULT) read-your-writes, monotonic reads/writes WITHIN a session.
       CONSISTENT    reads never see out-of-order writes (consistent prefix), may be stale.
        PREFIX
       EVENTUAL      replicas converge; no ordering guarantee. Lowest latency, highest avail.
   - backed by SLAs on latency, availability, throughput, AND the consistency guarantee.
   - multi-region WRITE mode uses conflict resolution (LWW or custom) -> guide 07.
```

Cosmos's contribution is making the consistency↔latency trade an explicit, **per-request**
dial with five precisely-defined points, rather than a fixed architectural choice.

### Comparison

| System | Consensus | Storage | Default isolation/consistency | Distinguishing mechanism |
|--------|-----------|---------|-------------------------------|--------------------------|
| **Spanner** | Paxos per split | Colossus/tablets | External consistency (linearizable txns) | **TrueTime** (GPS+atomic clocks) + commit-wait |
| **CockroachDB** | Raft per range | Pebble (LSM) | **SERIALIZABLE** | HLC + clock-offset + txn restarts; PG wire |
| **YugabyteDB** | Raft per tablet | DocDB (RocksDB) | Serializable / snapshot | PG-compatible (YSQL) |
| **TiDB** | Raft (per region) | TiKV (RocksDB) | Snapshot / serializable opt-in | MySQL-compatible; Percolator-style txns |
| **Cosmos DB** | (internal) | LSM-family | **Session** (5 tunable levels) | Per-request consistency dial + SLAs |

---

## What you give up, precisely

NewSQL is not magic; it pays real costs that drive design:

```
   CROSS-REGION WRITE LATENCY   strong consistency needs a quorum/consensus round-trip
                                across regions -> tens of ms minimum (speed of light).
                                Keep writes region-local where possible.

   2PC LATENCY ON CROSS-SHARD   multi-shard transactions still pay prepare+commit round-trips
   TRANSACTIONS                 (over consensus). Co-locate to keep txns single-shard (guide 08).

   AVAILABILITY UNDER PARTITION CP systems (Spanner, Cockroach default) refuse writes on the
                                minority side of a partition to preserve consistency.

   OPERATIONAL COMPLEXITY       clock sync, consensus group membership, rebalancing, hotspot
                                management -> more to run than a single Postgres.
```

The right framing for a VP: distributed SQL trades **latency and operational complexity** for
**linear scale + strong consistency**. You do not trade away correctness — you pay for it in
milliseconds and ops headcount. Reach for it when you've genuinely outgrown a replicated
single-leader Postgres/SQL Server, not before.

---

## Old World → New World Bridges

| You already know | Distributed-SQL concept | Azure / SQL Server anchor |
|------------------|-------------------------|----------------------------|
| Scale-up SQL Server hitting a ceiling | Horizontal scale-out without losing ACID | Azure SQL Hyperscale (scale-out storage), Cosmos |
| "Pick 2 of 3" CAP slogan | The corrected CAP: **C xor A only during a partition**; PACELC | Cosmos consistency levels embody PACELC |
| ACID consistency (constraints) | CAP consistency = **linearizability** (different!) | — |
| MSDTC / 2PC | 2PC **over a consensus group** (no coordinator SPOF) | Spanner/Cockroach distributed txns |
| Read replicas with lag | Bounded-staleness / session consistency | Cosmos Bounded Staleness / Session |
| Always On AG failover | Consensus-driven leader election per shard | Raft/Paxos leader per range |
| Cosmos "strong vs eventual" toggle | The consistency spectrum, dialed per request | The five Cosmos levels |

---

## Decision Cheat Sheet

| Situation | Reach for |
|-----------|-----------|
| Single-node RDBMS hitting write/storage ceiling, need ACID + SQL | **Distributed SQL** (Spanner / CockroachDB / Yugabyte) |
| Need strongest cross-region guarantee, have the budget | **Spanner** (external consistency) |
| Want Postgres compatibility + serializable, no special hardware | **CockroachDB** / **YugabyteDB** |
| Need MySQL compatibility at scale | **TiDB** |
| Want to dial consistency vs latency per request | **Cosmos DB** (five levels) |
| Workload tolerates eventual consistency, max availability | **NoSQL** (Cassandra/DynamoDB) — not NewSQL |
| Reads can be slightly stale but must be ordered | **Bounded staleness** / consistent-prefix |
| Must read your own writes in a session | **Session** consistency |
| Still fits one big replicated leader | **Don't** go distributed-SQL yet — keep Postgres/SQL Server |

---

## Common Confusion Points

### "CAP says pick 2 of 3"

The accurate statement: **during a network partition** you must choose Consistency *or*
Availability; with no partition you can have both. "Partition tolerance" isn't optional (you
can't wish partitions away), so the real, meaningful choice is **CP vs AP**, and only while
partitioned. **PACELC** adds the missing else-branch: even without a partition, consistency
costs latency.

### "The C in CAP is the same as the C in ACID"

No. ACID's C = the database preserves declared invariants/constraints (guide 04). CAP's C =
**linearizability**, i.e. every read reflects the latest completed write across the distributed
system. Two unrelated guarantees that share a letter.

### "NewSQL beats CAP / gives strong consistency for free"

It does not beat CAP. Spanner is a **CP** system — during a partition it sacrifices availability
on the minority side. What NewSQL buys back is the *latency-vs-consistency* trade in the
no-partition case: by paying latency (TrueTime commit-wait, cross-region consensus) it keeps
strong consistency at scale. Correctness is paid for in milliseconds, not given up.

### "Spanner is just sharded Postgres with magic clocks"

TrueTime is real and load-bearing but it's not magic — it's a clock API with **bounded
uncertainty** (GPS + atomic clocks), and Spanner **waits out** that uncertainty on commit
(commit-wait) to make timestamps respect real-time order. CockroachDB achieves serializability
without that hardware by using hybrid logical clocks and **restarting** transactions on clock
uncertainty instead of waiting.

### "Cosmos 'Strong' consistency is the same as 'Serializable'"

Different axes again. Cosmos's five levels describe **distributed read consistency** (what a read
sees across replicas/regions), not transaction **isolation** (anomalies between concurrent
transactions, guide 05). A system can be linearizable on the consistency axis while offering a
particular isolation level on the transaction axis — they're orthogonal guarantees.

### "Distributed SQL is always the right modern choice"

It carries real latency and operational costs (clock sync, consensus, rebalancing, cross-shard
2PC). For most workloads a single-leader Postgres/SQL Server with read replicas is simpler,
cheaper, and fast enough. Adopt distributed SQL when you've genuinely outgrown that — not as a
default.
