---
maxim_schema: maxim.frontmatter.v1
id: maxim:distributed-systems:consistency-models
kind: guide
module: distributed-systems
section: distributed-systems
title: Consistency Models: Linearizability, Sequential, Causal, Eventual
status: source-custody
source_custody: partial
current_path: distributed-systems/02-CONSISTENCY-MODELS.md
canonical_path: distributed-systems/02-CONSISTENCY-MODELS.md
backsource_ids: [mdloom-backfill:distributed-systems:02-consistency-models, git-history:distributed-systems:02-consistency-models]
concepts: [consistency, models]
root_concepts: [consistency, models]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Consistency Models: Linearizability, Sequential, Causal, Eventual

## The Big Picture

Consistency models define what a distributed system promises about the order and visibility of operations. They form a hierarchy — stronger models are safer but more expensive; weaker models are faster but require application-level reasoning.

```
CONSISTENCY MODEL HIERARCHY (strongest to weakest)
+-----------------------------------------------------------+
|  STRICT SERIALIZABILITY                                   |
|  (Linearizability + Serializability)                      |
|  All transactions appear to execute one at a time,        |
|  in real-time order. Spanner, FoundationDB.               |
+-----------------------------------------------------------+
           |
           v
+-----------------------------------------------------------+
|  LINEARIZABILITY (Herlihy 1990)                           |
|  Equivalent to single shared copy. Real-time order.       |
|  CAP's "C". Expensive: requires global coordination.      |
|  CosmosDB "Strong", ZooKeeper reads.                      |
+-----------------------------------------------------------+
           |
           v
+-----------------------------------------------------------+
|  SEQUENTIAL CONSISTENCY (Lamport 1979)                    |
|  All processes see same order. Not necessarily            |
|  real-time. Cheaper than linearizability.                 |
|  Some GPU memory models; x86-TSO is close but             |
|  strictly weaker (allows store→load reordering).          |
+-----------------------------------------------------------+
           |
           v
+-----------------------------------------------------------+
|  CAUSAL CONSISTENCY (Causal+)                             |
|  Causally related operations seen in order.               |
|  Concurrent operations may appear in any order.           |
|  CosmosDB "Consistent Prefix", COPS system.               |
+-----------------------------------------------------------+
           |
           v
+-----------------------------------------------------------+
|  PRAM (FIFO) CONSISTENCY                                  |
|  Within a single process, operations seen in order.       |
|  Between processes, no ordering guarantee.                |
+-----------------------------------------------------------+
           |
           v
+-----------------------------------------------------------+
|  EVENTUAL CONSISTENCY (Vogels 2009)                       |
|  Given no new writes, all replicas converge.              |
|  No ordering guarantee between nodes.                     |
|  DynamoDB default, Cassandra default, DNS.                |
+-----------------------------------------------------------+
```

---

## Lamport Clocks and the Happens-Before Relation

Lamport (1978) introduced a logical clock that captures causal ordering without synchronized physical clocks.

### The Happens-Before Relation (→)

Event a happens-before event b (a → b) if:
1. a and b are in the same process, and a occurs before b in program order
2. a is a send of a message and b is the receipt of that same message
3. Transitively: if a → c and c → b, then a → b

Events that are neither a → b nor b → a are **concurrent**.

### Lamport Clock Rules

```
Each process maintains a counter L
  - Increment L before each event
  - When sending a message, include L in the message
  - When receiving a message with timestamp t:
      L = max(L, t) + 1

GUARANTEE: If a → b, then L(a) < L(b)
CONVERSE NOT GUARANTEED: L(a) < L(b) does not imply a → b
```

Lamport clocks give a total order consistent with happens-before, but cannot detect concurrency.

---

## Vector Clocks

Vector clocks solve Lamport's limitation: they can detect concurrency.

```
Setup: N processes, each maintains vector V[N]
  - V[i] is process i's logical time
  - Initialize all to 0

Rules:
  - Before event in process i: V[i]++
  - Send message: include current V
  - Receive message with V':
      V[j] = max(V[j], V'[j]) for all j
      V[i]++

COMPARISON:
  - a → b iff V(a)[i] <= V(b)[i] for ALL i, and strict for at least one
  - concurrent iff neither a → b nor b → a
```

**Example with 3 processes:**

```
P1: V=[1,0,0]  writes X=1
P2: V=[0,1,0]  writes X=2   ← concurrent with P1's write (neither → other)
P3: receives from P1: V=[1,0,1]
P3: receives from P2: V=[1,1,2]  ← P3 has seen both writes; must resolve conflict
```

DynamoDB uses vector clocks (or similar version vectors) to detect conflicting writes. The application (or last-write-wins policy) must resolve them.

---

## Formal Definitions: The Model Spectrum

### Linearizability

The strongest non-transaction consistency model.

**Formal**: A history is linearizable if there exists a legal sequential execution of all operations (in real-time order) such that:
1. Each operation appears to take effect instantaneously at some point between its invocation and response
2. The sequential execution is consistent with the specification

**Cost**: Every read must check the most up-to-date value across all replicas. In a geo-distributed system, this means round-trips to the leader — ~100ms+ latency between regions. This is why Google Spanner's externally-consistent reads are expensive.

**When you need it**: Distributed locking, leader election, financial ledgers, any "compare-and-swap" primitive.

### Sequential Consistency

**Formal**: A history is sequentially consistent if all operations appear to execute in some sequential order that respects each process's program order — but not necessarily real-time order.

**Difference from linearizability**: Two different clients might see writes in different orders, as long as each client's own write order is preserved.

```
Process 1: writes X=1, then reads Y
Process 2: writes Y=1, then reads X

Sequential consistency allows:
  - P2 reads X=0 (sees P1's write late)
  - P1 reads Y=0 (sees P2's write late)
  This is allowed: no global real-time ordering required.

Linearizability does NOT allow this: if P1's write completed before
P2's read, P2 must see X=1.
```

**Used by**: x86 provides TSO (Total Store Order), which is *weaker* than sequential consistency — it permits store→load reordering, so SC needs explicit fences.

### Causal Consistency

**Formal**: All processes must agree on the order of causally related operations. Concurrent operations may be seen in different orders by different processes.

```
P1 writes X=1
P2 reads X=1, then writes Y=2   ← causal: Y=2 depends on X=1

Causal consistency guarantees: any process that reads Y=2
  MUST already see X=1.

But if P3 writes Z=5 with no causal relation to X or Y,
  different processes may see Z=5 before or after X=1.
```

**Why it matters**: Causal consistency is the strongest model achievable without coordination overhead proportional to the number of nodes. It is achievable in an AP system (no partition-induced unavailability).

**CosmosDB "Consistent Prefix"**: Reads never see out-of-order writes — but you might see a lag behind the latest write. This is close to causal but not identical.

### PRAM (Pipeline RAM) / FIFO Consistency

**Formal**: Writes from a single process are seen by all other processes in the order they were issued. Writes from different processes may be seen in any order.

Within a connection: in-order. Across connections: unordered.

**Example**: A message queue where a single producer's messages are delivered in-order to all consumers, but messages from different producers interleave unpredictably.

### Eventual Consistency

**Formal**: If no new updates are made to a given data item, eventually all accesses will return the last updated value.

This is the weakest useful model. It provides only a convergence guarantee — no ordering, no real-time constraint.

**Variants**:
- **Strong Eventual Consistency (SEC)**: All replicas that have received the same updates have the same state. No coordination required. CRDTs achieve SEC.
- **Monotonic Read Consistency**: Once you read a value, you will never read an older value.
- **Read-Your-Writes**: After writing a value, your subsequent reads will reflect it.
- **Monotonic Write Consistency**: Writes from a single process appear in order.

---

## CosmosDB Consistency Levels (Concrete Example)

CosmosDB exposes the consistency spectrum as a first-class product feature. Azure built the distribution; the consistency level is how you tune the C vs. A vs. L trade-off:

```
COSMOSDB CONSISTENCY LEVELS
+------------------+----------------------------------+---------------------+
| Level            | Guarantee                        | Latency Impact      |
+------------------+----------------------------------+---------------------+
| Strong           | Linearizability across all       | Highest: waits for  |
|                  | replicas. Reads never stale.     | all replicas to ack |
+------------------+----------------------------------+---------------------+
| Bounded Staleness| Reads lag by at most K versions  | Lower than Strong,  |
|                  | or T time interval.              | bounded latency     |
|                  | Good for globally distributed    |                     |
|                  | scenarios that need order.       |                     |
+------------------+----------------------------------+---------------------+
| Session          | Read-your-writes, monotonic      | Low: scoped to      |
|                  | reads, consistent prefix —       | single session      |
|                  | within a single client session.  |                     |
+------------------+----------------------------------+---------------------+
| Consistent Prefix| Reads never see out-of-order     | Low                 |
|                  | writes. No guarantee of          |                     |
|                  | recency — just order.            |                     |
+------------------+----------------------------------+---------------------+
| Eventual         | No ordering or recency           | Lowest latency,     |
|                  | guarantee. Maximum availability. | highest throughput  |
+------------------+----------------------------------+---------------------+
```

**Azure DevOps consistency choices**: Work item updates use session-level consistency — you see your own writes immediately, eventual propagation to other users. This is the correct trade-off: user sees their changes instantly (read-your-writes), other users see it soon (eventual).

---

## Why Linearizability is Expensive

The cost of linearizability comes from the requirement to synchronize across all replicas before acknowledging a write:

```
LINEAR WRITE PATH
Client
  |
  | write X=5
  v
Leader node
  |
  fan out to replicas
  v       v       v
Replica1 Replica2 Replica3
   ack     ack     ack
  acks fan back in
  |
  v
Leader acks to Client
  (only after all replicas ack)

In a 3-region deployment:
  US East → West Europe → Southeast Asia round trip = ~200ms
```

Compare to eventual consistency: leader acks immediately, replicates asynchronously. Latency is local (~1ms), not global (~200ms).

---

## Cross-References

- `03-CONSENSUS.md` shows how strong consistency is implemented under failure.
- `04-REPLICATION.md` explains the data-copying mechanisms that expose consistency tradeoffs.
- `07-CAP-THEOREM.md` frames consistency choices under partitions and availability pressure.

## Common Confusion Points

**"Linearizability" vs. "Serializability"**
Serializability is a transaction isolation level — multiple operations appear to execute atomically in some serial order. Linearizability is a single-object, single-operation consistency model — each operation appears to take effect at a single instant. Strict serializability = both together (Spanner achieves this).

**"Eventual consistency" means "any garbage"**
No — it means convergence is guaranteed. All replicas will agree on the final value. The uncertainty is about timing, not correctness of the final state.

**"Session consistency" is per-user**
CosmosDB Session consistency is per-session token, not per-user account. A single user on two different devices gets two different sessions, potentially seeing different values until convergence.

**"Causal consistency" requires no coordination"**
Causal consistency can be achieved without global coordination, but it does require tracking causality vectors (which adds overhead). It is coordination-light, not coordination-free.

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether linearizability is required | Ask if correctness depends on real-time order: locks, leader election, money movement, uniqueness, or compare-and-set. | Linearizability is expensive across regions; do not buy it for data that only needs convergence. |
| Whether sequential consistency is enough | Check whether all clients need one common order but not real-time recency. | Sequential consistency can surprise users because a later real-time operation may appear earlier. |
| Whether causality matters | Track happens-before relationships, messages, user actions, and conflict resolution semantics. | Causal consistency orders related operations, not concurrent ones. |
| Whether session consistency is enough | Focus on per-user read-your-writes and monotonic reads. | Session guarantees do not protect other users from seeing stale or differently ordered state. |
| Whether eventual consistency is safe | Confirm commutativity/idempotence, conflict policy, convergence requirement, and user tolerance for stale reads. | "Eventually" gives no bound on when readers see the latest value. |
| Whether a vendor level matches your model | Map the vendor term to real-time order, prefix order, session guarantees, bounded staleness, and conflict behavior. | Product labels often bundle multiple guarantees; test the anomaly you care about. |
