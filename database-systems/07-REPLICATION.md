---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:replication
kind: guide
module: database-systems
section: computing-software
title: Replication - Sync/Async, Leader-Follower, Quorum, Conflicts
status: source-custody
source_custody: partial
current_path: database-systems/07-REPLICATION.md
canonical_path: database-systems/07-REPLICATION.md
backsource_ids: [proof-backfill:database-systems:07-replication, git-history:database-systems:07-replication]
concepts: [replication, leader-follower, synchronous replication, asynchronous replication, quorum, conflict resolution, replication lag]
root_concepts: [replication]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Replication — One Node's Log Becomes Many Nodes' State

Replication copies data across machines for **availability** (survive a node loss),
**read scaling** (serve reads from followers), and **locality** (read near the user). The
database-engine angle: replication is, mechanically, **shipping the WAL** (guide 06) from a
leader to followers and having them apply it. This guide is the database-mechanics view;
the *theory* of consensus, linearizability, and CAP lives in `distributed-systems/`
(02 consistency models, 03 consensus, 04 replication) and we defer to it explicitly.

```
+=====================================================================================+
|                       THE REPLICATION DESIGN SPACE (database view)                  |
+=====================================================================================+
|                                                                                     |
|   WHO can accept WRITES?                                                             |
|                                                                                     |
|   +----------------------+   +----------------------+   +------------------------+   |
|   |  SINGLE-LEADER       |   |  MULTI-LEADER        |   |  LEADERLESS (quorum)   |   |
|   |  (primary/replica)   |   |  (multi-primary)     |   |  (Dynamo-style)        |   |
|   +----------------------+   +----------------------+   +------------------------+   |
|   | one leader takes all |   | several nodes take   |   | any replica takes a    |   |
|   | writes; followers    |   | writes; changes      |   | write; client writes   |   |
|   | replay its log.      |   | replicated both ways.|   | to W replicas, reads   |   |
|   |                      |   | CONFLICTS arise.     |   | from R; W+R>N => overlap|   |
|   | + simple, no write   |   | + write locality,    |   | + no leader bottleneck, |   |
|   |   conflicts          |   |   multi-region active|   |   highly available      |   |
|   | - leader is a write  |   | - conflict resolution|   | - read repair, eventual |   |
|   |   bottleneck/SPOF    |   |   is HARD            |   |   consistency, tuning   |   |
|   |                      |   |                      |   |                        |   |
|   | Postgres, MySQL, SQL |   | active-active geo,   |   | Cassandra, DynamoDB,    |   |
|   | Server AG, most OLTP |   | CRDT systems         |   | Riak (classic Dynamo)  |   |
|   +----------------------+   +----------------------+   +------------------------+   |
+=====================================================================================+
```

Bridge: SQL Server Always On Availability Groups are **single-leader** (one primary, readable
secondaries) with a choice of synchronous or asynchronous commit per replica. That maps exactly
to the leader-follower model below.

---

## How the WAL becomes a replica: what gets shipped

```
   PHYSICAL / STREAMING REPLICATION         LOGICAL REPLICATION
   --------------------------------         --------------------
   ship the raw WAL (page-level changes).   decode the WAL into row-level events
   Follower replays byte-for-byte; it is    (INSERT/UPDATE/DELETE on table T, values ...).
   an exact physical copy.                  Follower applies the logical operations.

   + low overhead, exact replica            + cross-version, selective tables, different
   - same major version + page layout         schema/index on the target, DBs can differ
   - whole-cluster, can't filter tables     - higher overhead, conflict potential

   Postgres: streaming (physical) WAL       Postgres: logical decoding / pub-sub
   MySQL: ROW-based binlog (logical-ish)    MySQL: binlog is the replication stream
   SQL Server AG: log block shipping        SQL Server: transactional/logical replication
```

```
   STATEMENT vs ROW based logical replication (the MySQL binlog distinction):
     STATEMENT-based   ship the SQL text; replica re-executes it.
                       BREAKS on non-determinism: NOW(), RAND(), AUTO_INCREMENT races,
                       triggers, non-deterministic UDFs -> replica diverges.
     ROW-based         ship the actual before/after row images. Deterministic, larger.
                       The modern default (MySQL ROW format) for correctness.
```

This is a real, classic footgun: statement-based replication of a query using `NOW()` or a
non-deterministic function makes the replica drift from the leader. Row-based avoids it by
shipping concrete values.

---

## Synchronous vs Asynchronous — the durability/latency knob

The central trade in single-leader replication: **when does the leader acknowledge a commit
relative to the followers receiving it?**

```
   ASYNCHRONOUS                              SYNCHRONOUS
   ------------                              -----------
   leader commits + acks the client,         leader waits for >=1 follower to confirm it has
   THEN streams to followers (lag).          the log record, THEN acks the client.

   write -> [leader durable] -> ACK          write -> [leader durable] -> wait follower ACK -> ACK
                  \                                              ^
                   `--> follower (later)                         |
                                                         follower has it too

   + lowest write latency                    + no data loss if leader dies (a follower has it)
   - DATA LOSS window: if the leader dies     - higher write latency (a network round-trip)
     before a follower got the last commits,  - if the sync follower is down/slow, writes
     those commits are LOST on failover.        STALL unless you fall back (semi-sync)
   - followers serve STALE reads (lag)
```

```
   SEMI-SYNCHRONOUS (the common compromise):
     ONE synchronous follower (no-data-loss guarantee for the acked write) + the rest async
     (read scaling without paying sync latency to every replica). If the sync follower fails,
     promote another or temporarily degrade to async. Postgres synchronous_commit + a sync
     standby; MySQL semi-sync; SQL Server AG "synchronous-commit" replicas behave this way.
```

> Precision: synchronous replication that waits for a follower to **receive/persist the log**
> still does not, by itself, give you linearizable reads from that follower — the follower may
> have the log but not yet *applied* it. True strong consistency across replicas needs consensus
> on a commit point. That is the consensus story in `distributed-systems/03`.

---

## Replication lag — the consequence and its anomalies

Async followers lag the leader. Reading from a lagging follower produces user-visible anomalies
that have standard fixes:

```
   ANOMALY                         FIX (read-your-writes etc., from distributed-systems/02)
   ----------------------------    ---------------------------------------------------------
   Read-your-own-writes violation  route a user's reads to the leader for a window after they
   ("I posted but don't see it")   write; or track the write's LSN and read a replica >= that LSN.

   Monotonic-reads violation       pin a session to one replica so it never goes "back in time"
   ("comment appears then vanishes")by hopping to a less-current replica.

   Consistent-prefix violation     ensure causally related writes apply in order (matters in
   ("see reply before the question") partitioned/multi-leader systems).
```

These are exactly the **consistency models** treated formally in `distributed-systems/02`. The
database mechanism is the same: bounded staleness, session pinning, or LSN/version tracking.

---

## Failover and the split-brain hazard

```
   Leader dies -> a follower must be PROMOTED. Three hard problems:

   1. DETECTION   how do you know the leader is dead vs slow? (timeout -> false positives)
   2. PROMOTION   pick the most up-to-date follower (highest applied LSN) to minimize loss.
   3. FENCING     ensure the OLD leader cannot keep accepting writes if it comes back ->
                  otherwise SPLIT-BRAIN: two leaders, divergent histories, data corruption.

   STONITH / fencing tokens / a consensus-based leader lease prevent split-brain. Automatic
   failover REQUIRES a fencing mechanism; otherwise a network partition gives you two leaders.
```

Split-brain is the single most dangerous replication failure: two nodes each believe they are
leader and accept conflicting writes. The robust fix is to gate leadership through a
**consensus protocol** (Raft/Paxos) or a quorum lease — which is why production single-leader
clusters lean on a consensus-backed controller (`distributed-systems/03`).

---

## Leaderless / quorum replication (Dynamo-style)

No leader. The client (or a coordinator) writes to **W** replicas and reads from **R** of **N**
total. Overlap gives consistency.

```
   N = replicas per key,  W = write quorum,  R = read quorum

   IF W + R > N  ->  every read quorum OVERLAPS every write quorum
                     -> a read sees at least one replica with the latest write
                     (a "strict quorum" — but see the caveats)

   common: N=3, W=2, R=2 (W+R=4 > 3)  -> tolerate 1 node down, still consistent-ish

   STALE COPIES are repaired by:
     - READ REPAIR:    on a read, detect divergent replicas, push the newest to the stale ones
     - ANTI-ENTROPY:   background process (e.g. Merkle-tree comparison) reconciles replicas
```

Caveat (precision): `W+R>N` gives quorum overlap but is **not** linearizable in the presence of
concurrent writes, sloppy quorums/hinted handoff, or in-flight failures — Dynamo-style systems
are eventually consistent. The formal treatment is `distributed-systems/01` (CAP) and `04`.

---

## Conflict resolution (multi-leader / leaderless)

When two nodes accept writes to the same key independently, you get a conflict. Strategies:

| Strategy | Mechanism | Trade-off |
|----------|-----------|-----------|
| **Last-write-wins (LWW)** | Keep the write with the highest timestamp | Simple; **silently drops** the loser's write; clock skew hazard |
| **Version vectors** | Track per-replica version counters; detect concurrent vs causal | Detects true conflicts; needs app-level merge |
| **CRDTs** | Conflict-free replicated data types: merges are commutative/associative/idempotent by construction | No coordination needed; limited to CRDT-expressible types |
| **Application merge** | Surface both versions (siblings); app decides (e.g. shopping-cart union) | Correct; pushes work to the app |

CRDTs and version vectors are detailed in `distributed-systems/05` (distributed transactions /
conflict resolution). LWW is the easy default and the easy way to lose data.

---

## Old World → New World Bridges

| You already know | Replication concept | SQL Server / Azure anchor |
|------------------|---------------------|----------------------------|
| Read replicas behind a load balancer | Single-leader leader-follower | Always On readable secondaries |
| Log shipping a `.ldf` to a standby | Physical WAL/log streaming | AG synchronous/async-commit, log shipping |
| "Mirror" with witness for failover | Promotion + fencing | Database mirroring (legacy), AG failover |
| Active-active multi-region | Multi-leader, conflict resolution | Cosmos multi-region writes (guide 09) |
| Eventual consistency you tuned | Quorum W/R, read repair | Cosmos consistency levels (guide 09) |
| "Last write wins" you set on a sync | LWW conflict resolution | Cosmos LWW conflict policy |

---

## Decision Cheat Sheet

| Need | Choice |
|------|--------|
| No data loss on failover | **Synchronous** (or semi-sync) replication to >=1 follower |
| Lowest write latency, tolerate small loss window | **Asynchronous** replication |
| Read scaling | Async **followers**; route reads off the leader |
| Read-your-writes after a write | Route to leader briefly, or read a replica at >= the write's LSN |
| Multi-region writes (active-active) | **Multi-leader** + a real conflict policy (not naive LWW) |
| Maximum availability, accept eventual consistency | **Leaderless quorum** (Dynamo-style), tune W/R |
| Automatic failover safely | Single-leader + **fencing/consensus** to prevent split-brain |
| Replica drifting from primary | Use **row-based** logical replication, not statement-based |

---

## Common Confusion Points

### "Synchronous replication means strongly consistent reads from the replica"

Not automatically. Synchronous usually means the follower has **received/persisted** the log
record before commit ack — but it may not have **applied** it yet, so a read there can still be
stale. Linearizable reads across replicas need a consensus commit point or reading at the
leader. See `distributed-systems/02`–`03`.

### "More replicas = more write throughput"

The opposite for writes. Followers scale **reads**. Writes still funnel through the leader (or,
in quorum systems, must reach W replicas), so adding replicas adds replication work, not write
capacity. Sharding (guide 08) scales writes; replication scales reads and availability.

### "Last-write-wins is a safe default for conflicts"

LWW **silently discards** the losing write and depends on synchronized clocks — clock skew can
drop the wrong write. It's fine only when losing a concurrent write is acceptable. For
correctness use version vectors, CRDTs, or application merge.

### "W+R>N gives me strong consistency"

It gives quorum **overlap**, not linearizability. Concurrent writes, sloppy quorums, hinted
handoff, and failures during the operation all break strict consistency. Dynamo-style quorum
systems are eventually consistent by design — `distributed-systems/01` (CAP) is the rigorous
account.

### "Replication and the WAL are different systems"

The replication stream **is** the WAL (physical) or a decode of it (logical). The same log that
recovers a crash (guide 06) is what followers replay. Understanding the WAL is understanding
replication's payload.
