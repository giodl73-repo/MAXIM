# Replication: Single-Leader, Multi-Leader, Leaderless — Trade-offs

## The Big Picture

Replication means keeping copies of the same data on multiple nodes. The three architectures differ in how they handle writes and where the complexity goes.

```
REPLICATION TOPOLOGY COMPARISON
+----------------------------------------------------------+
|                                                          |
|  SINGLE-LEADER          MULTI-LEADER         LEADERLESS |
|  (Master-Replica)       (Multi-Master)        (Dynamo)  |
|                                                          |
|  Client                Client               Client      |
|    |                   / \                 / | \        |
|    | writes           /   \               /  |  \       |
|    v                 v     v             v   v   v      |
|  Leader            Leader Leader       N1  N2   N3      |
|  (strong           A       B           (write to any)   |
|  consistency)      \       /            \   |   /       |
|    |                \ sync/              \  |  /        |
|    | replicates      \   /               Read Repair    |
|    |                  \ /                Anti-entropy   |
|    v                  Merge             (eventual sync) |
|  R1  R2  R3          conflict                          |
|  (read replicas)                                        |
+----------------------------------------------------------+

WRITE PATH     Single: one node    Multi: nearest DC    Leaderless: any node
READ PATH      Any replica         Any replica          Any W+R>N nodes
CONSISTENCY    Strong (sync rep)   Eventual (conflicts) Tunable (quorum W+R)
CONFLICT PATH  None (one writer)   Resolution required  Read repair
USE CASE       Most OLTP DBs       Multi-DC active-     DynamoDB, Cassandra
                                   active (Lotus Notes)
```

---

## Single-Leader Replication

One node is the leader (primary). All writes go to the leader. Reads can go to any replica.

### Write and Replication Flow

```
CLIENT
  |
  | write (INSERT/UPDATE/DELETE)
  v
LEADER
  |  writes to local WAL (Write-Ahead Log)
  |  applies to local state
  |
  +----------+----------+
  |          |          |
  | async    | async    | async
  v          v          v
Follower1  Follower2  Follower3
  (read      (read      (read
  replica)   replica)   replica)
```

**Synchronous vs. Asynchronous Replication**:

```
SYNCHRONOUS: Leader waits for follower ack before responding to client
  + Zero replication lag on that follower
  - Write latency = leader + follower round-trip
  - If follower is slow/down, writes stall
  - In practice: "semi-sync" — wait for 1 follower, rest async

ASYNCHRONOUS: Leader responds to client immediately
  + Minimal write latency
  - Follower may lag by seconds/minutes
  - If leader fails before follower catches up: data loss
  - Default in most systems (MySQL, PostgreSQL streaming replication)
```

**Azure SQL Database replication**: Uses synchronous replication to at least one secondary replica (the "primary" and one "HA" replica in same zone). Geo-replication is asynchronous. This is the typical semi-sync pattern.

### Replication Lag Effects

When replication is asynchronous, followers may serve stale reads:

```
REPLICATION LAG ANOMALIES

1. READ-YOUR-OWN-WRITES VIOLATION
   User updates profile picture at t=0
   User immediately views profile (hits different replica)
   Replica has not yet received the update
   User sees old picture
   FIX: Route reads-after-writes to leader, or track last-write
        timestamp and route to up-to-date replicas

2. MONOTONIC READS VIOLATION
   User issues query at t=1: gets result from Replica1 (lag: 1s)
   User issues query at t=2: gets result from Replica2 (lag: 5s)
   Second query shows data that appears older than the first
   FIX: Route each user's reads to the same replica consistently

3. CONSISTENT PREFIX VIOLATION
   Replica receives operations out of order due to network jitter:
   Write X=5 (received at replica at t=10)
   Write X=3 (received at replica at t=5, though happened after X=5)
   Reader sees X=3 then X=5 — causal order violated
   FIX: Use logical timestamps; don't apply until causal dependencies met
```

### Failover: Manual vs. Automatic

```
FAILOVER DECISION TREE

Leader health check fails
        |
        v
    Is it dead or just slow?  ──────────────────────────────+
        |                                                   |
   detection timeout expires                           Cannot tell!
   (typically 30s–5min)                                Split-brain risk
        |
        v
    Elect new leader (consensus or highest-replication-lag-wins)
        |
        v
    Reconfigure clients and followers to point to new leader
        |
        v
    Old leader comes back — must rejoin as FOLLOWER, not leader
        (old leader may have accepted writes; these must be discarded
         or reconciled — this is where data loss can occur)
```

**Split-brain**: Both old leader and new leader believe they are the leader and accept writes. This creates divergence that is very difficult to resolve. Prevention: require quorum (2 out of 3) to acknowledge leadership; old leader must be fenced (STONITH — Shoot The Other Node In The Head) before new leader accepts writes.

---

## Multi-Leader Replication

Multiple nodes accept writes simultaneously. Each is a leader; they replicate to each other.

### When It Makes Sense

```
MULTI-LEADER USE CASES
+--------------------------------------------+
| Multi-datacenter writes                    |
|   WestUS Leader ←──sync──→ EastUS Leader  |
|   User in WestUS writes locally (low lat) |
|   User in EastUS writes locally (low lat) |
|   Async replication between DCs           |
|   Conflict resolution on divergence       |
+--------------------------------------------+
| Offline-capable clients                    |
|   Each device is its own "leader"          |
|   Calendar app: edit offline, sync later   |
|   Google Docs: CRDT-based conflict merge   |
+--------------------------------------------+
| Collaborative real-time editing            |
|   Multiple writers on same document        |
|   Operational transforms / CRDTs           |
+--------------------------------------------+
```

### Conflict Resolution Strategies

All conflict resolution strategies have trade-offs:

```
WRITE CONFLICT: Two leaders both update the same record before sync

Strategy 1: LAST-WRITE-WINS (LWW)
  - Each write gets a timestamp
  - On conflict, higher timestamp wins
  - Problem: clock skew means "later" is unreliable
  - Problem: silently discards the losing write
  - Used by: Cassandra (tunable), DynamoDB (when enabled)

Strategy 2: MERGE SEMANTICS
  - Concatenate conflicting values
  - Works for sets (add-only) and counters
  - Breaks for scalar updates (cannot merge X=5 and X=3 meaningfully)
  - Used by: CRDTs (designed for this)

Strategy 3: APPLICATION-LEVEL RESOLUTION
  - Store all conflicting versions
  - Return all to application on read
  - Application decides which to use
  - Used by: Amazon shopping cart (Dynamo), Riak
  - Problem: application complexity; most apps get it wrong

Strategy 4: CUSTOM MERGE FUNCTION
  - Application provides conflict resolver callback
  - Couchbase, Riak allow this
  - Problem: hard to write correctly; hard to test
```

---

## Leaderless Replication (Dynamo-Style)

Any node can accept any write. Reads contact multiple nodes and reconcile. Popularized by Amazon's Dynamo paper (2007).

### The Quorum Model

```
N = total replicas per key
W = write quorum (must ack before write succeeds)
R = read quorum (must respond before read returns)

RULE FOR STRONG CONSISTENCY: W + R > N
  (read quorum and write quorum overlap on at least one node)

COMMON CONFIGURATIONS:
  N=3, W=2, R=2  ← balanced: tolerates 1 failure for both
  N=3, W=3, R=1  ← write-heavy consistency, fast reads
  N=3, W=1, R=3  ← write-fast, consistent reads (rare)
  N=3, W=1, R=1  ← maximum availability (AP, eventual)

CLIENT WRITE (W=2, N=3):
  write to all 3 → wait for 2 acks → return success
  if 1 node is down: still succeeds (2/3 ack)
  if 2 nodes are down: fails (cannot get 2/3)

CLIENT READ (R=2, N=3):
  read from all 3 → return after 2 respond → resolve conflicts
  version vectors or timestamps used to pick "latest"
  stale response discarded or scheduled for read repair
```

### Sloppy Quorum and Hinted Handoff

When the intended N nodes are unavailable (partition), the system uses nearby nodes as temporary homes:

```
SLOPPY QUORUM
  Normal home nodes for key K: [N1, N2, N3]
  N1 is unreachable
  Write goes to [N2, N3, N4]  ← N4 is a "hint" node, not a home node
  N4 stores the write with a hint: "this belongs to N1"

HINTED HANDOFF
  N1 comes back online
  N4 notices N1 is healthy
  N4 transfers the hinted write to N1
  N4 deletes its copy

EFFECT:
  + Higher availability during partitions
  - Quorum is "sloppy" — W+R>N no longer guarantees overlap
  - Potential for stale reads even with quorum
```

### Anti-Entropy and Read Repair

```
READ REPAIR (synchronous)
  Client reads from R nodes
  Node A returns version 5
  Node B returns version 3
  Client detects divergence
  Client (or coordinator) writes version 5 back to node B
  Repairs on every read → accurate but adds latency

ANTI-ENTROPY (background, asynchronous)
  Background process compares data between replicas
  Uses Merkle trees to detect divergence efficiently:
    Build tree where leaves = hashes of individual records
    Parents = hash of children
    Compare root hashes → if equal, no divergence
    If different, descend tree to find differing subtree
    Sync only the differing records
  DynamoDB, Cassandra use Merkle tree anti-entropy
```

---

## Replication Comparison Table

| Dimension | Single-Leader | Multi-Leader | Leaderless |
|-----------|--------------|--------------|-----------|
| Write consistency | Strong (sync) or eventual (async) | Eventual (conflict resolution) | Tunable (W+R>N) |
| Write availability | Limited by leader health | High — any DC accepts writes | High — any node accepts writes |
| Read scalability | High — distribute to followers | High | High — R can be small |
| Conflict handling | None (one writer) | Required | Read repair, anti-entropy |
| Failover complexity | Moderate (leader election) | Complex (dual-leader coordination) | Low (no failover concept) |
| Typical use case | OLTP, most relational DBs | Multi-DC active-active, offline clients | DynamoDB, Cassandra, Riak |
| Azure example | Azure SQL, CosmosDB Strong | Cosmos multi-region writes | Cosmos eventual, Table Storage |

---

## Common Confusion Points

**"Replication = higher availability"**
Replication improves read availability and durability. For writes, single-leader replication may reduce availability (leader must be healthy for writes). Leaderless replication improves write availability.

**"More replicas = more consistency"**
More replicas does not improve consistency unless W is adjusted. More replicas with W=1 is still eventually consistent. Consistency comes from quorum settings, not replica count.

**"Async replication is safe"**
Async replication can lose acknowledged writes if the leader crashes before replicating. PostgreSQL's `synchronous_commit=off` can lose the last N transactions. This is a deliberate trade-off (performance vs. durability), not a bug.

**"Leaderless systems avoid split-brain"**
Leaderless systems avoid the leader-election split-brain problem, but can have write conflicts (multiple nodes accept conflicting writes for the same key simultaneously). The problem is not eliminated — it is moved to the read/reconciliation phase.

---

## Decision Cheat Sheet

| Use Case | Replication Strategy |
|----------|---------------------|
| OLTP with strong consistency | Single-leader, synchronous replication |
| Read-heavy workload | Single-leader, multiple read replicas |
| Multi-region active-active | Multi-leader with CRDT or application-level merge |
| Maximum availability, tunable consistency | Leaderless (DynamoDB/Cassandra style) |
| Coordination / metadata | Consensus-based (etcd/ZooKeeper — not replication) |
| Global SQL with external consistency | Spanner / CockroachDB (Paxos per shard) |
