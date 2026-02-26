# Consensus: Paxos, Raft, Viewstamped Replication — Algorithm Internals

## The Big Picture

Consensus is the problem of getting N nodes to agree on a single value, even when some nodes fail. It underlies leader election, replicated logs, and distributed transactions.

```
CONSENSUS PROBLEM
+-----------------------------------------------------------+
|                                                           |
|  N nodes, each proposes a value.                         |
|  Agreement required: all decide on the same value.       |
|  Validity required: the decided value was proposed.      |
|  Termination required: all non-faulty nodes decide.      |
|                                                           |
|  Fault model: crash-stop (nodes halt silently)           |
|  FLP (1985): impossible with >= 1 crash in async model   |
|  Solution: partial synchrony (Dwork-Lynch-Stockmeyer)    |
|                                                           |
|  ALGORITHM LANDSCAPE                                      |
|  +---------------+  +-------------+  +-----------------+ |
|  | Paxos (1989)  |  | Raft (2014) |  | Viewstamped Rep | |
|  | Consensus     |  | Consensus   |  | (VR, 1988)      | |
|  | via quorums   |  | via leader  |  | View changes    | |
|  | Hard to impl  |  | Explicit    |  | Liskov et al.   | |
|  +---------------+  +-------------+  +-----------------+ |
|          |                |                  |            |
|          v                v                  v            |
|     Chubby          etcd, CockroachDB    MongoDB repl    |
|     CosmosDB        TiKV, ConsulDB                       |
|     internally      Kubernetes control                   |
|                                                           |
+-----------------------------------------------------------+
```

---

## FLP Impossibility (Fischer-Lynch-Paterson, 1985)

The foundational negative result in distributed systems.

**Statement**: In a fully asynchronous message-passing system, there is no deterministic algorithm that can solve consensus if even one process can fail by crashing.

**Why it matters**: You cannot tell the difference between a slow node and a crashed node in an asynchronous system. If you wait for a response from a crashed node, you wait forever (no termination). If you proceed without it, you might violate agreement.

**The proof intuition**:
- Start in a "bivalent" initial configuration (both 0 and 1 are still possible outcomes)
- Show that from any bivalent configuration, there exists a sequence of steps that maintains bivalency
- Therefore termination can always be deferred — the algorithm can be kept in limbo forever by adversarial scheduling
- Therefore no algorithm can guarantee termination

**The escape hatch**: FLP assumes fully asynchronous network (no timing bounds). Real systems use **partial synchrony** (Dwork-Lynch-Stockmeyer, 1988): assume the network is eventually synchronous — it may be asynchronous for a while, but eventually message delays are bounded. Under partial synchrony, consensus is solvable. Paxos and Raft operate under this assumption.

---

## Paxos: Single-Decree Consensus

Lamport's Paxos (1989, published 1998) solves consensus for a single value.

### Roles

```
PROPOSER: Initiates the protocol, drives agreement
ACCEPTOR: Votes on proposals (quorum = majority)
LEARNER: Learns the decided value (reads it)
```

A node can play multiple roles simultaneously.

### Single-Decree Paxos: Two-Phase Protocol

**Phase 1: Prepare / Promise**

```
Proposer                         Acceptors
   |                             |   |   |
   |-- PREPARE(n) -------------> |   |   |  (broadcast)
   |   n = proposal number,      |   |   |
   |   unique and increasing     |   |   |
   |                             |   |   |
   |   Each acceptor:            |   |   |
   |   If n > maxSeen:           |   |   |
   |     maxSeen = n             |   |   |
   |     reply PROMISE(n, v_a)   |   |   |
   |     where v_a = previously  |   |   |
   |     accepted (value, round) |   |   |
   |   Else: ignore or NACK      |   |   |
   |                             |   |   |
   |<-- PROMISE(n, v_a) -------- |   |   |  (from quorum)
```

**Phase 2: Accept / Accepted**

```
Proposer                         Acceptors
   |  (if quorum of promises)    |   |   |
   |  choose value v:            |   |   |
   |    if any promise carried   |   |   |
   |    v_a, use highest-round v_a|  |   |
   |    else use own proposed v  |   |   |
   |                             |   |   |
   |-- ACCEPT(n, v) -----------> |   |   |  (broadcast)
   |                             |   |   |
   |   Each acceptor:            |   |   |
   |   If n >= maxSeen:          |   |   |
   |     accept (n, v)           |   |   |
   |     notify Learners         |   |   |
   |                             |   |   |
   |<-- ACCEPTED(n, v) --------- |   |   |  (quorum acks)
   |                             |   |   |
   CONSENSUS REACHED: v is decided
```

**The quorum requirement**: A majority of acceptors must participate in each phase. With 2F+1 nodes, F failures are tolerated. The overlap guarantee: any two majorities share at least one node — ensuring a new proposer always learns about previously accepted values.

### Multi-Paxos: Replicating a Log

Single-decree Paxos agrees on one value. Multi-Paxos extends this to an ordered log of values (commands).

```
MULTI-PAXOS OPTIMIZATION
  - Elect a distinguished leader (run single-decree Paxos for leader)
  - Leader runs Phase 1 once (not per-entry)
  - Each new log entry: leader runs only Phase 2 (accept/accepted)
  - Leader failure → new Paxos election → new leader inherits log

RESULT: Normal-case operation requires only 1 round-trip to a quorum
        Leader election requires 2 round-trips
```

**Why Paxos is hard to implement**: The paper describes single-decree Paxos. Multi-Paxos is described informally. Dozens of engineering decisions are left open: leader election, log gaps, snapshots, membership changes. Diego Ongaro's 2014 thesis documented 43 separate implementation questions not answered by the Paxos literature.

---

## Raft: Understandable Consensus

Diego Ongaro designed Raft (2014) specifically to be understandable — decomposing consensus into three relatively independent subproblems: leader election, log replication, and safety.

### Structure

```
RAFT CLUSTER (5 nodes, F=2 fault tolerance)
+--------+    +--------+    +--------+    +--------+    +--------+
| Node 1 |    | Node 2 |    | Node 3 |    | Node 4 |    | Node 5 |
| LEADER |    |FOLLOWER|    |FOLLOWER|    |FOLLOWER|    |FOLLOWER|
+--------+    +--------+    +--------+    +--------+    +--------+
    |              |              |              |              |
    |<- heartbeat  |              |              |              |
    |   (AppendEntries RPC, empty)|              |              |
    |              |              |              |              |
Client writes to leader only.
Followers redirect clients to leader.
```

### Terms

```
TIME
----+------+--------+--------+------+----+------+----->
   election election  normal  elec  split normal
    term 1   term 2  term 2  fail  vote  term 4
         |        |
       leader   leader
       elected  elected

- Time is divided into terms (monotonically increasing integers)
- Each term begins with an election
- At most one leader per term
- Terms act as logical clocks — stale leaders have old term numbers
```

### Leader Election

```
All nodes start as FOLLOWERS
  |
  | election timeout expires (150–300ms, randomized)
  v
Become CANDIDATE
  |
  | increment term, vote for self
  | send RequestVote RPC to all nodes
  v
  Receive votes from quorum? ──Yes──> Become LEADER
        |                               Send heartbeats
        No (split vote or
            higher term seen)
        |
        v
  Return to FOLLOWER, wait for next timeout
```

Randomized timeouts prevent split votes: nodes don't all time out simultaneously.

**Vote granting rule**: A node votes for a candidate only if:
1. Candidate's term >= my term
2. Candidate's log is at least as up-to-date as mine (safety property)

### Log Replication

```
CLIENT REQUEST
     |
     | write to leader
     v
LEADER appends entry to local log (uncommitted)
     |
     | AppendEntries RPC (new entry + previous entry info)
     v
FOLLOWERS append entry to their logs
     |
     | acknowledgment from quorum
     v
LEADER commits entry (advances commitIndex)
     |
     | next AppendEntries tells followers about commit
     v
FOLLOWERS commit entry → apply to state machine
     |
     | applied → respond to client
```

**Log Matching Property**: If two logs contain an entry with the same index and term, then the logs are identical in all entries up through that index. This is the key safety invariant.

### Safety Guarantee

A leader will never overwrite or delete committed entries. A new leader always has all committed entries. This is guaranteed by the vote-granting rule: a candidate cannot win without a vote from a node that has the latest committed entries.

### Membership Changes

Raft uses a joint consensus approach for adding/removing nodes — the cluster operates in both old and new configurations simultaneously during the transition, requiring majorities from both configurations.

---

## Viewstamped Replication (VR)

Liskov and Cowling (1988, republished 2012). Developed independently from Paxos, arrived at similar structure.

**Key differences from Raft**:
- Views instead of terms
- View changes (equivalent to Raft leader election) are more explicit
- Historically important: predates Paxos publication

The VR protocol is structurally very similar to Multi-Paxos and Raft. The academic consensus is that these three protocols are equivalent; they differ in presentation and engineering emphasis.

---

## Zab: ZooKeeper Atomic Broadcast

ZooKeeper uses Zab (ZooKeeper Atomic Broadcast), which is Paxos-like but optimized for a primary-backup architecture.

```
ZAB KEY PROPERTIES
  - Primary processes all writes, broadcasts to backups
  - Total order: all replicas process transactions in same order
  - Prefix property: if replica delivers transaction T, it has
    delivered all transactions before T
  - Leader election on failure (Zab phase: discovery + synchronization)

ZAB vs. RAFT
  - Both are leader-based commit protocols
  - Zab uses transaction IDs (epoch + counter) not log indices
  - Zab recovery is more complex (multi-phase sync)
  - Raft is more influential for new systems
```

---

## etcd: Kubernetes Control Plane

etcd uses Raft. The entire Kubernetes control plane state (API server, scheduler state, controller state) lives in etcd.

```
KUBERNETES CONTROL PLANE
+----------------------------------------------------------+
| API Server | Scheduler | Controller Manager              |
+----------------------------------------------------------+
                         |
                    reads/writes
                         |
                         v
              +---------------------+
              |        etcd         |
              |   (Raft cluster,    |
              |   typically 3 or 5) |
              +---------------------+
              Leader handles writes.
              Followers handle reads (by default via leader forwarding).
              etcd MUST have quorum — losing majority = cluster down.
```

**Production lesson**: etcd is the single most critical component in a Kubernetes cluster. Operators routinely run etcd on dedicated nodes with local NVMe storage and isolated networks.

---

## When Consensus Is and Is Not Used

| Need | Use Consensus | Avoid Consensus |
|------|--------------|-----------------|
| Leader election | Yes (always) | N/A |
| Replicated log (append-only) | Yes | N/A |
| Distributed lock | Yes | Use lease-based (reduce consensus ops) |
| Incrementing a counter | No — use CRDT | Consensus is too expensive |
| Appending to a queue | Often no — Kafka uses in-sync replicas | |
| Key-value store reads | Only if linearizable | Use eventual for low-latency |
| Metadata storage | Yes — ZooKeeper, etcd | Don't put data plane in consensus |
| User data (large scale) | No — too expensive | Use quorum-based replication |

**The meta-principle**: Consensus is expensive (multiple round-trips, quorum requirements). Use it for control plane, coordination, and metadata. Keep data plane operations out of consensus paths.

---

## Common Confusion Points

**"Paxos is impractical"**
The original paper describes single-decree Paxos. Multi-Paxos works fine in practice — Google uses it in Chubby. It's hard to implement correctly, but not impractical. Raft exists because Paxos is hard to teach and implement, not because it's wrong.

**"Raft is more correct than Paxos"**
Raft and Paxos are equivalent in their safety and liveness properties under the same fault model. Raft is more pedagogically accessible and has more complete specification of engineering decisions.

**"FLP means consensus is impossible"**
FLP says consensus is impossible in a *fully asynchronous* system. All real systems use timeouts, which introduce partial synchrony. Paxos and Raft work in practice because real networks are eventually synchronous.

**"3 nodes tolerates 2 failures"**
No. With N=3 nodes, quorum is 2. You can tolerate 1 failure (3 - 2 = 1). To tolerate F failures, you need 2F+1 nodes. 5 nodes tolerates 2 failures.

---

## Decision Cheat Sheet

| Algorithm | When to Choose | Trade-off |
|-----------|---------------|-----------|
| Multi-Paxos | Existing Paxos infrastructure; Google-style | Complex to implement correctly |
| Raft | New systems requiring replicated log | Cleaner implementation; more library support |
| Zab | ZooKeeper integration | ZooKeeper-specific; not general-purpose |
| etcd/Raft | Kubernetes coordination, config store | Do not use for data plane at scale |
| Custom | Performance-critical, specific failure model | Requires deep expertise |
