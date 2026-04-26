# Distributed Systems — Engineering Reference

## The Big Picture

Distributed systems are fundamentally about **coordinating processes that can fail independently**. Every interesting property you want — consistency, availability, fault tolerance — trades off against something else. Nancy Lynch's "Distributed Algorithms" is the theory bedrock; this guide bridges that theory to Paxos, Raft, CRDTs, and the systems that run at scale today.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DISTRIBUTED SYSTEMS PROBLEM SPACE                                          │
│                                                                             │
│  Core Challenges             Fundamental Impossibilities                    │
│  ────────────────────────    ─────────────────────────────────────          │
│  Partial failures            FLP: No consensus in async with 1 crash        │
│  Network partitions          CAP: Choose 2 of: C, A, P                      │
│  Message delays/reordering   Impossibility of 2PC in failures               │
│  Node crashes (fail-stop)    Byzantine generals require n > 3f nodes        │
│  Byzantine faults                                                           │
│                                                                             │
│  Core Protocols              Modern Systems                                 │
│  ────────────────────────    ─────────────────────────────────────          │
│  Paxos (consensus)           etcd/ZooKeeper: Raft + distributed config      │
│  Multi-Paxos (replication)   Spanner: TrueTime + Paxos per shard            │
│  Raft (understandable)       CockroachDB: Raft + MVCC + distributed SQL     │
│  Viewstamped Replication     DynamoDB: eventual consistency + versioning    │
│  Zab (ZooKeeper)             Kafka: log replication + leader election       │
│                                                                             │
│  Consistency Models (strongest to weakest):                                 │
│  Linearizability > Sequential > Causal > PRAM > Eventual                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Fundamental Impossibility Results

### FLP Impossibility (Fischer-Lynch-Paterson 1985)

**Theorem**: No deterministic consensus algorithm can guarantee termination in an asynchronous system where even one process may crash.

```
Model:
  - Asynchronous network: message delays unbounded (but messages eventually delivered)
  - Processes communicate only by messages
  - At most 1 process may crash (fail-stop)
  - All processes start with {0, 1}; must agree on one value

Proof sketch (bivalent configurations):
  A configuration is bivalent if both outcomes (0 and 1) are still possible.
  - Initial configuration must be bivalent (since any value is reachable).
  - Show: can always delay messages to stay bivalent forever.
  - Hence: no algorithm terminates in all runs with 1 crash.
```

**Practical implication**: All practical consensus protocols either:
1. Assume eventual synchrony (Paxos, Raft): progress guaranteed when network behaves
2. Use randomization (Ben-Or, Algorand): probabilistic termination even in async model
3. Give up on termination guarantee in favor of safety (2PC is safe but not live)

### CAP Theorem (Brewer 2000, Gilbert-Lynch 2002 proof)

**Theorem**: A distributed system cannot simultaneously provide all three of:
- **Consistency** (C): Every read sees the most recent write (linearizability)
- **Availability** (A): Every request receives a response (no timeout/error)
- **Partition tolerance** (P): System operates despite message loss

```
Why you must choose:
  Network partition occurs (P is unavoidable in reality — networks do partition).

  During partition, two nodes have diverged state.
  → Either refuse requests until partition heals (sacrifice A, keep C)
  → Or serve requests with potentially stale data (sacrifice C, keep A)

CA systems (no partitions): single-node RDBMS — not distributed
CP systems: ZooKeeper, etcd, HBase — refuse writes during partition
AP systems: Cassandra, CouchDB, DynamoDB — serve stale reads during partition
```

**PACELC** (more nuanced than CAP): Even without partitions, there's a tradeoff: Latency vs Consistency. Low-latency responses require not waiting for quorum confirmation.

### Two-Phase Commit (2PC) — Safe But Not Live

```
Phase 1 (Prepare):
  Coordinator → all participants: "Prepare to commit"
  Each participant: acquire locks, log "prepared", respond Yes/No

Phase 2 (Commit/Abort):
  If all Yes → Coordinator → all: "Commit"
  If any No  → Coordinator → all: "Abort"
  Participants execute and release locks.

Failure scenarios:
  Coordinator crashes after Phase 1 but before Phase 2:
  → Participants are blocked (holding locks) waiting for coordinator.
  → Can't safely commit or abort without coordinator decision.
  → System is live-locked.

This is why 2PC is not partition-tolerant for liveness.
```

**Three-Phase Commit (3PC)**: Adds a pre-commit phase so participants can unilaterally abort if coordinator crashes before pre-commit. BUT 3PC is not safe under network partitions (can have split-brain commits). Almost never used in production.

**Modern alternative**: Paxos-based transaction commit (as in Spanner). Coordinator runs Paxos round to make commit decision durable before any participant commits.

---

## 2. Consensus Protocols

### Paxos (Lamport 1998, published after 9-year delay)

**Single-decree Paxos**: Agree on one value.

```
Roles: Proposers, Acceptors, Learners (often same processes)

Phase 1a (Prepare):
  Proposer chooses ballot number n > any previously used.
  Sends Prepare(n) to quorum of acceptors.

Phase 1b (Promise):
  Acceptor: if n > max_prepare_seen:
    Set max_prepare = n
    Respond: Promise(n, (max_accepted_ballot, max_accepted_value) or null)

Phase 2a (Accept):
  If proposer receives promises from quorum:
    v = value from promise with highest ballot (or own value if all null)
    Send Accept(n, v) to quorum.

Phase 2b (Accepted):
  Acceptor: if n ≥ max_prepare:
    Accept (n, v), send Accepted(n, v) to learners.

Consensus: Learner sees Accepted from quorum → value is decided.
```

**Why it works**: Any two quorums overlap in at least one acceptor. That shared acceptor ensures the same value propagates across ballot changes.

**Paxos safety invariant**: Once a value v is decided, no future ballot can decide a different value. The "pick the value from highest previous ballot" rule in Phase 2a enforces this.

### Multi-Paxos (state machine replication)

Single-decree Paxos → log of commands → replicated state machine:
```
Optimization: elect a stable leader. Leader skips Phase 1 for each slot.
  Only needs Phase 2 (Accept + Accepted) per log slot.
  Phase 1 only on leader change.

Leader election: highest-ballot proposer wins.
Stable leader: Ω(1) per slot (just 2 message delays).
Pipelined: leader can have k outstanding accepts simultaneously.

What Multi-Paxos doesn't specify (Lamport intentionally left vague):
  - How to detect leader failure
  - How to garbage collect log
  - How to handle membership changes
  - How to learn decisions efficiently
→ Different implementations (Chubby, Zab, Raft) fill these gaps differently.
```

### Raft (Ongaro-Ousterhout 2014 — "Understandable Paxos")

Raft explicitly addresses everything Multi-Paxos leaves open, in a single coherent protocol:

```
Three subproblems:
  1. Leader election
  2. Log replication
  3. Safety

Key properties:
  - At most one leader per term
  - Leaders never overwrite logs — only append
  - Committed entries never change

Leader election:
  Terms numbered 1, 2, 3, ... (logical time)
  Candidate increments term, requests votes.
  Vote granted if: term ≥ own term AND log ≥ candidate's log (at least as up-to-date).
  Candidate wins if majority votes.
  Split votes: random election timeout triggers retry.

Log replication:
  Leader receives client request, appends to own log.
  Sends AppendEntries RPC to all followers.
  Committed when majority acknowledge.
  Leader notifies clients, applies to state machine.

Safety (Log Matching Property):
  If two logs contain entry with same index and term, all preceding entries are identical.
  Proof: Leader only creates one entry per slot; followers accept only leader's entries.

Cluster membership changes:
  Joint consensus: transition through configuration containing both old and new members.
  Single-server changes: safe to add/remove one server at a time.
```

**Raft implementations**: etcd (etcd uses its own Raft implementation), CockroachDB, TiKV (TiDB), Consul.

### Viewstamped Replication (Liskov-Cowling 2012)

Precursor to Paxos and Raft (1988). Explicitly view-based: each view has a primary. Nearly identical to Multi-Paxos and Raft at the protocol level. Introduced the concept of "view change" that maps directly to Raft's leader election.

### Zab (ZooKeeper Atomic Broadcast)

ZooKeeper's consensus protocol. Two modes:
- **Recovery mode**: elect leader, establish consistent state across replicas
- **Broadcast mode**: leader sends proposals; replicas acknowledge; commit when quorum acks

Key difference from Paxos: Zab ensures primary order — transactions from old leader are completed before new leader proposes new transactions. ZooKeeper linearizable reads require `sync()` first (otherwise stale from follower).

### Modern Consensus — Beyond Raft

**Multi-Paxos vs Raft trade-off**:
- Raft's strong leader simplifies implementation and reduces the bug surface — the full protocol fits in a single paper. The cost: the leader is a bottleneck; all writes go through one node.
- Multi-Paxos allows any node to propose (no single leader required), which reduces latency in WAN deployments where clients are geographically distributed.
- **Single-datacenter**: Raft wins (implementation simplicity, mature tooling in etcd/CockroachDB/Consul).
- **Geo-distributed**: EPaxos or variants win (leader bottleneck is too expensive at cross-region RTT).

**EPaxos** (Egalitarian Paxos — Moraru et al. 2013): Leaderless consensus. Each replica can commit commands directly without routing through a leader.

```
Non-conflicting commands (operating on different keys):
  Commit in 1 RTT fast path (2 message delays).
  Compare: Raft requires 2 RTTs via leader.

Conflicting commands (same key, must be ordered):
  Fast path: 2 RTT if <F replicas are slow (F = floor((n-1)/2) failures tolerated).
  Slow path: 3 RTT (similar to Paxos Phase 1 + Phase 2 + explicit ordering round).

Dependency tracking: each command records which earlier commands it depends on.
  Replicas execute in dependency order, not arrival order.

Used in: CockroachDB (EPaxos-inspired follower reads), some Google internal systems.
```

EPaxos's guarantee: in a 5-node cluster spanning 3 datacenters, non-conflicting writes to different keys commit in 1 cross-datacenter RTT — each replica acts as local leader for its clients.

**Flexible Paxos** (Howard et al. 2016): Generalization that separates Phase 1 (leader election) quorum from Phase 2 (commit) quorum. The only constraint is Q1 ∩ Q2 ≠ ∅ (the two quorums must share at least one node).

```
Classic Paxos: Q1 = Q2 = majority → both phases require n/2 + 1 nodes.

Flexible Paxos example (5-node cluster, 1 leader datacenter + 4 followers):
  Phase 1 (election): Q1 = 4 nodes  → tolerates 1 failure during election
  Phase 2 (commit):   Q2 = 2 nodes  → only leader + 1 follower needed per write

  This works because any 4-node set intersects any 2-node set.
  Result: fast commits (leader + 1 follower, 1 RTT) at cost of slower elections.

WAN use case: place leader in one datacenter, use small Q2 for fast local commits,
  large Q1 to ensure a new leader sees all committed values during failover.
```

Flexible Paxos makes explicit what Multi-Paxos always implied but never formalized: quorum sizes are a knob, not fixed at majority.

### Byzantine Fault Tolerance

**Byzantine failure**: Process can send arbitrary/contradictory messages (network attacker, hardware fault, software bug).

**Lower bound**: BFT consensus requires n > 3f nodes to tolerate f Byzantine failures. Proof: with ≤ 3f, you can't distinguish Byzantine nodes from slow honest ones.

**PBFT** (Practical BFT — Castro-Liskov 1999):
```
3-phase protocol: pre-prepare, prepare, commit.
O(n²) messages per consensus round.
Leader rotation on timeout.
Works for f < n/3.
```

**Modern BFT** (Tendermint, HotStuff, etc.):
- HotStuff: O(n) per phase via linear view change. Used in Libra/Diem, Aptos.
- Tendermint: Deterministic leader, O(n²) messages. Used in Cosmos.
- **PBFT vs Raft**: PBFT tolerates Byzantine faults, O(n²) messages. Raft tolerates crash failures, O(n) messages. Choose based on threat model.

---

## 3. Consistency Models

### Formal Hierarchy

```
Strongest                                                 Weakest
    │
    ▼
Linearizability (atomic consistency, "C" in CAP)
    │  Every operation appears to take effect instantaneously at some point
    │  between its invocation and response.
    │  Sequential spec: each op has a single linearization point.
    │
    ▼
Sequential Consistency (Lamport 1979)
    │  All processors see operations in the same total order.
    │  Order within each processor preserved.
    │  Does NOT require real-time order across processors.
    │
    ▼
Causal Consistency
    │  Causally related operations seen in order everywhere.
    │  Concurrent (causally unrelated) operations may be seen in different order.
    │  Vector clocks implement causality tracking.
    │
    ▼
PRAM (Pipeline RAM / FIFO) Consistency
    │  Each processor's writes seen in order by all others.
    │  Writes from different processors may be seen in different orders.
    │
    ▼
Eventual Consistency
       Eventually, in the absence of updates, all replicas converge to same state.
       No ordering guarantees. Captures "read your own writes" only sometimes.
```

**Linearizability vs Serializability**:
- Linearizability: single-object operations appear atomic in real-time order
- Serializability: multi-object transactions appear to execute in some serial order
- Strict Serializability = Linearizability + Serializability (real-time order for transactions)
- Most databases: Snapshot Isolation (not serializable) or Serializable (varies in implementation)

### Implementation Techniques

**Quorum reads/writes** (achieving linearizability without consensus):
```
n replicas, write quorum W, read quorum R, where R + W > n

Write: send to all, wait for W acks, return
Read:  read from R replicas, return highest-timestamped value

Example: n=3, W=2, R=2 (majority quorum)
  Any read quorum overlaps any write quorum → reads see latest write.

Cassandra: tunable consistency (ONE/QUORUM/ALL per operation)
DynamoDB: eventually consistent reads (R=1) vs strongly consistent (R=quorum)
```

**Read repair**: When read detects stale replicas, asynchronously update them.
**Hinted handoff**: Write to available replica with hint; deliver when target recovers.

---

## 4. Time and Causality

### Logical Clocks

**Lamport timestamps** (Lamport 1978):
```
Rules:
  1. Increment clock before each event.
  2. On send: include current clock value.
  3. On receive: clock = max(local, received) + 1

Property: a happens-before b  →  L(a) < L(b)
Converse false: L(a) < L(b) does NOT imply a → b.

Used for: causal ordering, distributed mutual exclusion (Lamport's mutex algorithm).
```

**Vector clocks** (Fidge/Mattern 1988):
```
n processes, each with vector V[1..n]
  - Process i increments V[i] before event.
  - Send: include own V.
  - Receive: V[j] = max(local[j], received[j]) for all j; V[i]++.

Property: VC(a) < VC(b) iff a → b (causally precedes b)
Concurrent events: neither VC(a) ≤ VC(b) nor VC(b) ≤ VC(a).

Conflict detection: Amazon DynamoDB uses vector clocks to detect write conflicts.
Space: O(n) per event — problematic for large n.
```

**Version vectors** vs **vector clocks**: Version vectors track object versions across replicas; vector clocks track events across processes. Distinction matters in practice (Git uses DAG of commits, not pure vector clocks).

**Hybrid Logical Clocks (HLC)** (Kulkarni et al. 2014):
```
Combine physical and logical time.
HLC = (physical_timestamp, logical_counter)

Rules:
  - If physical time advances: HLC = (physical_time, 0)
  - Otherwise: HLC = (max(own_HLC, received_HLC).physical, counter + 1)

Property: HLC ≥ NTP_time always. Causally related events have strict HLC order.
Used in: CockroachDB MVCC timestamps, YugabyteDB.
```

**TrueTime** (Google Spanner):
```
GPS + atomic clocks → bounded uncertainty interval [earliest, latest].
TrueTime.Now() returns interval [T_earliest, T_latest] with guarantee:
  T_earliest ≤ true_time ≤ T_latest.
Uncertainty: ~1-7ms typically.

External consistency (linearizability for transactions):
  Commit wait: transaction t1 must wait until TrueTime.Now().earliest > t1.commit_timestamp.
  This ensures t1's commit time is in the past by the time another transaction reads it.
```

### Clock Approach Comparison

The practical choice when building a globally distributed database:

| Approach | Mechanism | Uncertainty | Consistency achieved | Used by |
|----------|-----------|-------------|---------------------|---------|
| TrueTime | GPS receivers + atomic clocks in each datacenter; hardware-bounded ε | ε ≈ 7ms avg (wait this out before commit) | External consistency (linearizability across datacenters) | Google Spanner |
| Hybrid Logical Clocks (HLC) | Wall clock + logical counter; no hardware; software-only monotonicity | ~1ms typical (clock skew detection + uncertainty bumps on skew) | Causal consistency; serializable via SSI | CockroachDB, YugabyteDB |
| NTP + causal metadata | NTP drift ±100ms+; rely on vector clocks or causal tokens for ordering | High — cannot trust timestamps for ordering | Causal consistency (with tokens); eventual without | Most distributed DBs (Cassandra, DynamoDB default) |

**The practical consequence**:
- **Spanner's external consistency** (linearizability across datacenters) requires GPS/atomic clock hardware. No hardware = no guarantee. The "commit wait" is what makes cross-datacenter linearizability possible — Spanner literally sleeps through the uncertainty window.
- **HLC achieves causal consistency without hardware**. CockroachDB's "uncertainty bumps" (re-read transactions when clock skew is detected) can cause cascading retries under heavy skew — the software complexity Spanner avoids by hardware.
- **NTP-based systems** cannot use timestamps for ordering decisions; they must layer vector clocks or session tokens on top.

---

## 5. Replication Protocols

### Primary-Backup (PB) Replication

```
Primary receives writes, applies, forwards to backups, waits for acks.
Reads from primary (strong consistency) or backups (eventual).

Single primary: no split-brain possible.
Failover: if primary fails, promote backup.
Problem: manual failover or automated failover races → potential split-brain.

Solutions:
  STONITH (Shoot The Other Node In The Head): fence failed primary before promotion.
  Lease-based: primary holds timed lease; must not serve after lease expires.
```

**Chain Replication** (van Renesse-Schneider 2004):
```
Chain: head → node₂ → node₃ → ... → tail

Writes: enter at head, propagate to tail in order.
Reads: served from tail (always sees committed writes).

Throughput: write bandwidth distributed across chain.
Latency: O(chain length) for writes.
Used in: Azure Storage, CRAQ variant for scale-out reads.
```

### Quorum-Based Replication

```
Dynamo (DeCandia et al. 2007 — Amazon):
  n=3, W=2, R=2 typical.
  Eventual consistency. Versioning via vector clocks.
  Conflict resolution: last-write-wins or application-specific.
  Anti-entropy: Merkle trees for background sync.
  Gossip protocol for membership.

Cassandra (extends Dynamo):
  Tunable consistency: ANY/ONE/TWO/THREE/QUORUM/LOCAL_QUORUM/EACH_QUORUM/ALL.
  Lightweight transactions via Paxos for compare-and-set.
  Tombstones for deletes (must GC carefully).
```

### State Machine Replication (SMR)

The general model behind Paxos/Raft:
```
Inputs → [ Consensus Protocol ] → Ordered log of commands
                                         ↓
                              [ Deterministic State Machine ]
                              (same log → same state on all replicas)

Property: All non-faulty replicas execute same commands in same order → identical state.
This is how etcd, ZooKeeper, CockroachDB, and TiKV work.
```

---

## 6. CRDTs — Conflict-Free Replicated Data Types

**The problem**: In an AP system (available during partition), concurrent updates to the same object create conflicts. Resolution strategies:
- Last-Write-Wins (LWW): discard older update → loses data
- Multi-value (DynamoDB): return all versions, let application merge → complex
- **CRDTs**: design data types where concurrent updates always have a unique merge result

### State-based CRDTs (CvRDTs)

```
Each replica maintains state s. Merge operation ⊔ must form a semilattice:
  - Commutative: s₁ ⊔ s₂ = s₂ ⊔ s₁
  - Associative: (s₁ ⊔ s₂) ⊔ s₃ = s₁ ⊔ (s₂ ⊔ s₃)
  - Idempotent:  s ⊔ s = s

Propagation: periodically broadcast full state; replicas merge.
Convergence: all replicas that received same set of states converge to same state.
```

**Common CRDTs**:

| CRDT | Operations | Merge rule | Used in |
|------|-----------|------------|---------|
| G-Counter | Increment only | max per-replica count | Distributed counters |
| PN-Counter | Inc/Dec | pair of G-Counters | Shopping cart quantities |
| G-Set | Add only | set union | Tag sets |
| 2P-Set | Add/Remove | add-set ∪, remove-set ∪; add wins | Distributed sets |
| OR-Set (Observed-Remove) | Add/Remove | tag each add; remove only removes tagged copies | Most set CRDTs |
| LWW-Element-Set | Add/Remove | timestamp; last-write-wins per element | Casual apps |
| LWW-Register | Assign | max timestamp wins | Single-value registers |
| MV-Register | Assign | multi-value; all concurrent kept | DynamoDB versioning |
| RGA / Logoot | Insert/Delete | sequence CRDTs | Collaborative text editing |

**Op-based CRDTs (CmRDTs)**: Propagate operations instead of state. Operations must be:
- Delivered exactly once (reliable delivery)
- Commutative for concurrent operations

### Sequence CRDTs (Collaborative Editing)

**OT (Operational Transformation)**: Transform concurrent operations to maintain intent. O(n²) transform functions. Used in Google Docs (Jupiter algorithm), original Etherpad.

**CRDT sequences** (Attiya et al., Roh et al., Preguiça et al.):
- RGA (Replicated Growable Array): each element has unique ID; insert-after semantics
- LSEQ: adaptive allocation of unique identifiers in sequence space
- Used in: Automerge library, Yjs (used in many collaborative editors), xi-editor (originally)

### Production CRDT Reality

The theory is clean; production deployment surfaces three problems the papers don't emphasize.

**Yjs vs Automerge**:
- **Yjs** uses a linked-list CRDT (based on YATA — Yet Another Transformation Approach) where each character has a unique ID referencing its left and right neighbors at insertion time. Concurrent insertions at the same position are resolved by ID comparison. Result: fast for text editing, especially large documents; used in real-time editors (Hocuspocus, y-websocket, TipTap).
- **Automerge** uses an operation-based CRDT with Lamport timestamp ordering (similar to RGA). More general — supports JSON-like nested structures, not just sequences. Slower for pure text operations (~10x vs Yjs on large docs), but handles arbitrary JSON document merge.
- **Rule of thumb**: rich text or code editing → Yjs; JSON document sync → Automerge.

**Tombstone GC problem**: Sequence CRDTs (RGA, Yjs, Automerge) mark deleted elements as tombstones rather than removing them. A client that inserted character X and then deleted it still keeps X's tombstone so late-arriving operations can correctly resolve position relative to it.

```
Consequence: the in-memory/on-disk size of the CRDT grows monotonically.
  A document with 10,000 characters that underwent 100,000 edits
  accumulates ~100,000 tombstones, not 10,000 live chars.

GC requires knowing all clients have seen the deletion (no client holds
  a reference to the tombstoned element). This requires coordination:
  - Yjs: periodic snapshotting with a "checkpoint" that collapses history.
    The snapshot + awareness protocol requires a brief consensus moment.
  - Automerge: explicit compaction via "save/load" (offline GC).
  Both solutions weaken the "pure AP, no coordination needed" story.
```

**Why Figma chose OT over CRDTs**: Undo semantics. In a CRDT, "undo" means generating a new operation that reverses the effect of an earlier one. But if other users have made edits that depend on the undone operation, the undo cascades in complex ways — there is no standard CRDT undo primitive. In OT (particularly the Jupiter/Google Docs model), undo transforms through the operation history in a well-defined way. Figma's multiplayer (2019 blog post) chose OT specifically because their users expected undo to "feel right" — undoing your last stroke shouldn't revert other users' concurrent changes. This is the production trade-off the CRDT papers don't surface.

---

## 7. Coordination Services

### ZooKeeper (Yahoo! 2010)

```
Data model: hierarchical namespace (like filesystem) of znodes.
Znodes: persistent, ephemeral (auto-delete on session end), or sequential.

Guarantees:
  - Sequential consistency: all writes in client session in order.
  - Atomicity: all or nothing.
  - Single system image: client sees same view regardless of which server it connects to.
  - Durability: committed updates survive failures.
  - Timeliness: clients see updates within ε of true time.

Watch mechanism: register one-time watch on znode; notified on change.

Distributed primitives built on ZooKeeper:
  Lock: create ephemeral-sequential child; lowest-numbered holds lock.
  Leader election: lowest-numbered ephemeral sequential znode wins.
  Queue: producer creates sequential znodes; consumer reads lowest.
  Barrier: create znode; delete when ready; watchers unblock.

Consistency: reads may be stale (follower served). Use sync() for linearizable read.
Used by: Kafka (topic metadata, initially; now KIP-500 replaced with KRaft),
         HBase (region server assignment), Hadoop HDFS NameNode HA.
```

### etcd (CoreOS → CNCF)

```
Key-value store with Raft consensus. Linearizable by default.
gRPC API. Watch on key ranges.

Used by Kubernetes as its backing store for all cluster state.
  - All objects (Pods, Deployments, Services) stored in etcd.
  - Watch for controller loops (informers).
  - Leases for leader election (scheduler, controller manager).

Differences from ZooKeeper:
  - gRPC vs custom protocol
  - Raft vs Zab (similar in practice)
  - Simpler data model: flat key-value with range queries
  - Better Kubernetes integration
  - Watch is range-based, not path-based
```

---

## 8. Distributed Databases

### Google Spanner

```
Architecture:
  - Universe → Zones → Servers
  - Data sharded into tablets across Paxos groups
  - Each Paxos group has 5 replicas across 3+ datacenters

Transactions:
  - Read-write: Two-phase locking + two-phase commit across shards
  - 2PC coordinated by transaction coordinator (one shard's Paxos leader)
  - Read-only: lock-free using TrueTime snapshot reads

TrueTime:
  GPS + atomic clocks → bounded uncertainty [T_earliest, T_latest] ~7ms
  Commit wait: sleep until committed timestamp is in the past
  → External consistency: if T1 commits before T2 starts, T1's timestamp < T2's

SQL layer: F1 SQL (full external SQL)
Used for: Google Ads backend, many Google services.
```

### CockroachDB

```
Open-source Spanner-inspired.
  - Raft per range (64MB partitions)
  - MVCC (Multi-Version Concurrency Control)
  - HLC timestamps (no GPS/atomic clocks → ~1ms uncertainty vs Spanner's ~7ms)
  - Distributed SQL (DistSQL): query pushdown to data nodes
  - Serializable isolation by default (SSI: Serializable Snapshot Isolation)
  - PostgreSQL-compatible wire protocol

Trade-off vs Spanner: less hardware, more software complexity.
No TrueTime → uses HLC + uncertainty bumps on clock skew detection.
```

### Amazon DynamoDB

```
Architecture: consistent hashing ring, virtual nodes.
Consistency: eventual by default; strongly consistent reads available.
Data model: key-value + limited secondary indexes.
Operations: GetItem, PutItem, UpdateItem, DeleteItem.

Design choices (Dynamo paper, Werner Vogels):
  - Always writable (AP): partition won't block writes.
  - Versioning: vector clocks detect conflicts; client resolves.
  - Sloppy quorum: write to any n healthy nodes (hinted handoff for unavailable nodes).
  - Anti-entropy: Merkle tree per replica for background repair.

DynamoDB (2012) vs Dynamo (2007 paper):
  - DynamoDB service: fully managed, added strong consistency, DAX (cache layer),
    transactions (2018), global tables (multi-region active-active).
  - Dynamo paper: white paper; many concepts copied into Cassandra, Riak, Voldemort.
```

### Apache Kafka — Distributed Log

```
Kafka is not a database but a distributed commit log:
  - Topic → Partitions → Ordered sequence of messages (offsets)
  - Producers append to partitions (single leader per partition)
  - Consumers track offset (durable cursor)

Replication (ISR — In-Sync Replicas):
  Leader handles all reads/writes.
  Followers replicate from leader.
  ISR = set of replicas fully caught up to leader.
  Committed = all ISR acks.
  Leader election: ZooKeeper (pre-3.x) or KRaft (3.x: internal Raft).

Strong durability: acks=all → all ISR must commit before producer gets ack.
High throughput: sequential disk writes, zero-copy sendfile(), batch compression.
Used for: event streaming, CDC, log aggregation, activity tracking.
```

---

## 9. Distributed Algorithms — Core Techniques

### Leader Election

**Bully algorithm** (Chang-Roberts for rings):
```
When a process suspects leader failure:
  Initiates election with its own ID.
  Forwards highest-seen ID around ring.
  Process with globally highest ID wins.
O(n) messages in ring. O(n²) in fully connected (bully).
```

**Raft leader election**: timeout → increment term → request votes with log metadata → win with quorum. Safe: log-at-least-as-up-to-date check prevents overwriting committed entries.

### Distributed Mutual Exclusion

**Lamport's mutex**: Use totally-ordered timestamps. Request to all; wait for replies from all; CS when in front of queue. O(3(n-1)) messages per CS entry/exit. Requires reliable message delivery.

**Ricart-Agrawala**: Optimization of Lamport. O(2(n-1)) messages. Defer replies when requesting CS with higher priority.

**Token ring**: Pass token; hold CS while holding token. O(1) messages for CS when token nearby; O(n) worst case.

**Distributed lock via consensus** (etcd/ZooKeeper): Create sequential ephemeral node; watch predecessor. O(1) watches regardless of n. Preferred in practice.

### Failure Detectors

**Perfect failure detector (P)**: Eventually suspects every crashed process and never suspects correct process. Requires synchronous system.

**Eventual perfect (◇P)**: After some time, suspects exactly crashed processes. Sufficient for consensus in eventually synchronous systems.

**Heartbeat-based**: Timeout = suspect. Phi-accrual (Cassandra, Akka): adaptive suspicion based on historical heartbeat intervals.

---

## 10. Read-Path Optimization and Production Patterns

### Read Consistency Implementation

**Read-your-writes** (a client must see its own writes): Three implementation approaches:

```
1. Sticky sessions (routing-level):
   Route all reads from a client to the replica they wrote to.
   Simple. Breaks if that replica fails or client reconnects elsewhere.
   Used in: MySQL replication with ProxySQL, read replicas.

2. Session tokens (timestamp-based):
   On write, server returns a "write token" (HLC timestamp or log sequence number).
   Client includes token in subsequent reads.
   Read replica waits until it has applied through that token before responding.
   Used in: CockroachDB follower reads, Azure Cosmos DB session consistency.

3. Bounded staleness:
   Accept reads from any replica within X ms/bytes of the leader.
   No token needed; replicas self-report their lag.
   Used in: Spanner "bounded staleness" reads, Azure SQL readable secondaries.
```

### Multi-Region Write Conflict Resolution

Active-active multi-region (multiple regions accept writes to the same data):

| Strategy | Mechanism | Risk | When to use |
|----------|-----------|------|-------------|
| Last-Write-Wins (LWW) | Compare timestamps; highest wins | Clock skew can silently discard writes | Immutable records, events, logs |
| Compare-and-Swap (CAS) / optimistic locking | Version counter; reject stale writes | Higher retry rate under contention | Low-contention mutable records |
| CRDTs | Commutative merge; no conflict possible | Limited to CRDT-compatible types | Counters, sets, presence indicators |
| Application-level merge | Return all conflicting versions; client merges | Requires client-side merge logic | Shopping carts, rich documents |

**LWW + clock skew risk**: In a 5-region deployment with NTP, clocks can differ by 100ms+. A write from region A at T=100 and a write from region B at T=101 (but B's clock is 50ms behind) means A's write (which happened later in real time) loses. This is not hypothetical — it's the reason Spanner exists.

### Split-Brain Detection Patterns

```
Primary-backup split-brain: both nodes think they're primary.
Result: divergent writes, data loss on failover.

Detection and prevention approaches:

1. Fencing tokens (Martin Kleppmann's approach):
   Each time a lock/lease is granted, increment a monotone fencing token.
   Include token with every write operation to storage.
   Storage server rejects writes with stale token (lower than latest seen).
   → Old primary's writes are rejected even if it doesn't know it's demoted.
   Used in: distributed lock services, Kubernetes lease-based leader election.

2. STONITH (Shoot The Other Node In The Head):
   When a node is suspected dead, physically fence it (cut power, reset via IPMI/iDRAC)
   before promoting the new primary.
   Guarantees old primary is dead before new one writes.
   Used in: Pacemaker/Corosync clusters, classical HA database setups.

3. Raft/Paxos term staleness:
   Old leader cannot commit writes after it loses quorum.
   A new leader in a higher term rejects communication from old leader.
   The protocol itself enforces the invariant — no external fence needed.
   → Why Raft-based systems (etcd, CockroachDB) don't need STONITH.

4. Lease-based fencing:
   Primary holds a timed lease (e.g., 10s). Must renew before expiry.
   If network partitions and primary cannot renew → stops serving at lease expiry.
   New primary waits for old lease to expire before accepting writes.
   Used in: Chubby (Google), Azure Storage's blob leases.
```

---

## 11. Modern Distributed Patterns

### Saga Pattern (distributed long-running transactions)

```
Problem: 2PC is not practical across microservices.
Solution: Sequence of local transactions, each with compensating transaction.

Choreography saga: each service publishes events; others react.
Orchestration saga: central orchestrator coordinates.

On failure: execute compensating transactions in reverse order.
Limitation: no isolation (intermediate states visible).
Used in: e-commerce order fulfillment, travel booking.
```

### Gossip Protocol

```
Each node periodically picks random peer and exchanges state.
Convergence: O(log n) rounds for message to reach all nodes.
Properties: decentralized, fault-tolerant, self-healing.

Used in:
  Cassandra: membership, failure detection
  Dynamo: membership
  Consul: health checking
  SWIM protocol (Scalable Weakly-consistent Infection-style Membership)
```

### Anti-Entropy / Merkle Trees

```
Merkle tree: hash tree where each leaf = hash of data block;
             each internal node = hash of children.

Comparison: O(log n) messages to find differing blocks between two trees.
Used in:
  DynamoDB: detect which partitions are out of sync
  Bitcoin: SPV proofs (Merkle proofs)
  Git: object graph (each commit is Merkle DAG root)
  Cassandra: anti-entropy repair
```

---

## Consistency Decision Cheat Sheet

```
Application needs:                           Choose:
──────────────────────────────────────────   ─────────────────────────────────────────
Strong consistency, SQL, ACID transactions   CockroachDB, Spanner, PostgreSQL + Patroni
Strong consistency, key-value                etcd, ZooKeeper
Eventual consistency, massive write scale    Cassandra, DynamoDB (eventually consistent)
Event streaming, ordered log                 Kafka
Distributed config/coordination              etcd, ZooKeeper, Consul
Multi-region active-active                   DynamoDB Global Tables, Cassandra multi-DC
Collaborative real-time editing              CRDTs (Yjs for text, Automerge for JSON)
High-availability distributed counter        PN-Counter CRDT
Conflict-free sets                           OR-Set CRDT

Consistency model needed?
  Reads must reflect writes you just made     Linearizability (strong consistency)
  Reads can tolerate brief lag, same order    Sequential consistency
  Related writes must be seen together        Causal consistency
  Performance over correctness, SLA OK       Eventual consistency

Clock approach needed?
  Linearizability across datacenters          TrueTime (requires GPS/atomic clocks)
  Causal consistency, no hardware             HLC (CockroachDB approach)
  Casual ordering only                        Vector clocks + NTP
```

---

## Common Confusion Points

**CAP is not "pick two of three"**: Network partitions are inevitable in any distributed system. The real choice is CP (consistency) or AP (availability) **during a partition**. Outside of partitions, you can have both C and A — this is where PACELC's latency-consistency tradeoff matters more.

**Eventual consistency doesn't mean "usually consistent"**: Without specific consistency protocols, you may read very stale data for arbitrarily long. "Eventual" means "if no new updates, eventually converge." DynamoDB with default reads can return seconds-old data.

**Linearizability ≠ Serializability**: Linearizability is about single-object operations being atomic in real-time order. Serializability is about multi-object transactions appearing in some serial order. You can have one without the other. **Strict Serializability** = both = what most people actually want.

**Paxos vs Raft**: Same safety guarantees. Raft is Paxos + specified leader election + membership change + log matching. Raft is easier to understand and implement correctly; Paxos is more flexible.

**2PC is not consensus**: 2PC solves atomic commitment (all-or-nothing), not consensus (agree on a value). 2PC can deadlock (coordinator failure). Paxos/Raft solve consensus and can be used to make 2PC coordinator fault-tolerant.

**ZooKeeper is not strongly consistent by default**: Reads from followers are NOT linearizable. You must call `sync()` before reading if you need the latest data. etcd IS linearizable by default.

**Vector clocks detect concurrency, not causality ordering alone**: If VC(a) and VC(b) are incomparable, it means a and b are concurrent — neither caused the other. This is a conflict that needs resolution, not just a reordering.

**Leader election ≠ consensus**: Any process can declare itself leader. Consensus-based leader election (Paxos/Raft) ensures only one leader wins per term. Without consensus, split-brain is possible (two nodes think they're leader).

**HLC uncertainty bumps can cascade**: CockroachDB's response to detecting clock skew is to "bump" a transaction's timestamp forward and potentially retry. Under heavy skew (network instability, VM migration), these cascades can cause significant latency spikes — the software penalty for not having GPS clocks.
