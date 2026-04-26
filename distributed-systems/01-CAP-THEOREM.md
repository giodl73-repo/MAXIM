# CAP Theorem: Consistency, Availability, Partition Tolerance

## The Big Picture

```
+---------------------------------------------------------------------+
|                         CAP THEOREM                                 |
|                                                                     |
|   Brewer's Conjecture (2000): You cannot build a web service that   |
|   simultaneously provides all three of:                             |
|                                                                     |
|         C — Consistency: every read receives the most recent        |
|              write or an error                                      |
|         A — Availability: every request receives a non-error        |
|              response (no guarantee it's the latest data)           |
|         P — Partition Tolerance: system continues to operate        |
|              despite arbitrary network message loss                 |
|                                                                     |
|   Gilbert-Lynch formal proof (2002): proved in asynchronous         |
|   network model with crash failures                                 |
|                                                                     |
|   The critical insight: P is not optional. Partitions happen.       |
|   So the real choice is: what do you sacrifice during a partition?  |
|                                                                     |
|             C ──────────────── A                                    |
|              \                /                                     |
|               \   impossible /                                      |
|                \  to achieve /                                      |
|                 \   all 3   /                                       |
|                  \         /                                        |
|                   \       /                                         |
|                    \     /                                          |
|                     \   /                                           |
|                      \ /                                            |
|                       P                                             |
|                                                                     |
|   CA: no partitions → only single-datacenter systems qualify        |
|   CP: sacrifice availability during partition → return errors       |
|   AP: sacrifice consistency during partition → return stale data    |
+---------------------------------------------------------------------+
```

---

## Formal Definitions

### Consistency (the C in CAP)

This is **linearizability** — not to be confused with ACID consistency.

> A read operation that returns a value v is guaranteed to reflect the result of the most recently completed write of value v, or some later write.

In plain terms: if you write X=5, the next read anywhere in the system must return 5 (or the result of an even later write). No node may return a stale value after a write is acknowledged.

**Note**: This is stronger than "eventual consistency" (which allows stale reads temporarily) and is what the CAP theorem refers to.

### Availability (the A in CAP)

> Every request received by a non-failing node in the system must result in a response. The response must eventually terminate.

Key subtleties:
- A response is required — not "eventually" — but now
- The response need not contain the latest data
- Failed nodes are excluded (you're not promising a response from crashed nodes)
- There is no timeout bound specified — but practically you cannot wait forever

### Partition Tolerance (the P in CAP)

> The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

Key subtleties:
- "Arbitrary" means: any message may be lost, not just some messages
- This includes delayed messages — a delayed message is indistinguishable from a lost one
- You cannot tell if a node is slow or crashed (no shared clock)

---

## Why P is Not Optional

In any system spanning more than one machine, the network between them can fail. This is not theoretical:

```
PARTITION FREQUENCY (approximate, production experience)
+----------------------------------------------------------+
| Intra-datacenter (same AZ)     | minutes/month           |
| Cross-AZ (same region)         | hours/year              |
| Cross-region (e.g., US to EU)  | several times/year      |
| Multi-cloud                    | days/year per provider  |
+----------------------------------------------------------+

When a partition occurs, your system MUST choose:
  - Stop accepting writes (sacrifice A, maintain C) → CP
  - Accept writes and risk divergence (sacrifice C, maintain A) → AP
```

A "CA" system (no partition tolerance) is only achievable if all nodes are in a single node — which means it's not distributed. A single-node SQL Server is CA. Once you add a replica, you've introduced P as a possibility.

---

## The Real Choice: CP vs. AP During Partition

```
PARTITION OCCURS
        |
        v
 Your system must decide:
        |
   +----+----+
   |         |
   v         v
  CP         AP
   |         |
   v         v
Return     Accept
errors     writes,
(no        risk
stale      staleness
data)
   |         |
   v         v
Correct,   Available,
unavailable inconsistent
during     during
partition  partition
```

**CP behavior example (ZooKeeper):**
- Client writes to leader
- Partition splits leader from followers
- ZooKeeper refuses reads from isolated followers
- Returns errors until quorum re-establishes
- Clients must retry with backoff

**AP behavior example (DynamoDB default):**
- Client writes to any node
- Partition occurs — some nodes don't get the write
- DynamoDB still serves reads (may be stale)
- Convergence happens when partition heals via anti-entropy
- Client eventually reads the latest value

---

## PACELC: The Extension That Adds Latency

Eric Brewer and Daniel Abadi (2012) pointed out that CAP only addresses the partition case. Even when there's no partition, there's a latency vs. consistency trade-off.

```
PACELC Model:
                    IF Partition                ELSE (no partition)
                   /            \              /                   \
                  /              \            /                     \
            sacrifice         sacrifice  sacrifice              sacrifice
           Availability     Consistency  Latency               Consistency
              (AP)              (CP)      (EL)                    (EC)
```

The full designation for a system: PA/EL, PC/EC, etc.

| System | Partition Behavior | Else Behavior | PACELC |
|--------|-------------------|---------------|--------|
| DynamoDB (default) | AP | EL (low latency) | PA/EL |
| Cassandra | AP | EL (tunable) | PA/EL |
| CosmosDB Strong | CP | EC | PC/EC |
| CosmosDB Eventual | AP | EL | PA/EL |
| Spanner | CP | EC (commit-wait latency) | PC/EC |
| ZooKeeper | CP | EC | PC/EC |
| MySQL async replication | AP | EL | PA/EL |

---

## CAP Examples Table

| System | CAP | During Partition | Notes |
|--------|-----|-----------------|-------|
| HBase | CP | Returns error or times out | Relies on ZooKeeper for coordination |
| Cassandra | AP | Returns potentially stale data | Tunable: QUORUM pushes toward CP |
| ZooKeeper | CP | Refuses service without quorum | Coordination service for Kafka, Hadoop |
| etcd | CP | Refuses service without quorum | Kubernetes control plane |
| DynamoDB | AP (default) | Returns stale data | Strong consistency option available |
| MongoDB | CP (since v3) | Returns error if no primary | Previously was AP by default |
| Redis (standalone) | CP | Single node, no partition | Sentinel is CP; cluster is AP |
| CosmosDB Strong | CP | Returns errors | Cross-region strong consistency |
| CosmosDB Eventual | AP | Returns stale data | Highest availability tier |
| Azure SQL | CP | Failover (seconds/minutes) | Primary only handles writes |
| Kafka (replication) | CP | Unclean leader election trades A | unclean.leader.election.enable=false |

---

## Gilbert-Lynch Proof Sketch

The formal proof proceeds by constructing a scenario where C + A + P cannot all hold simultaneously:

```
Scenario setup:
  - Two nodes: G1, G2
  - Initial state: variable v = v0
  - Network partition between G1 and G2

Step 1: Client writes v = v1 to G1
  - Partition means G1 cannot propagate to G2
  - Availability requires G1 to acknowledge the write
  - G1 accepts: v = v1

Step 2: Client reads v from G2
  - Availability requires G2 to respond (cannot wait for partition to heal)
  - G2 responds with v = v0 (it has not received the write)

Contradiction:
  - Write v1 was acknowledged (A satisfied for write)
  - Read returned v0 (C violated: v0 is not the most recent write)
  - Partition was present and system operated (P satisfied)
  - Therefore C + A + P cannot all hold
```

The proof assumes:
- Asynchronous network (no bound on message delay)
- Crash-stop failures (nodes can stop, not send arbitrary messages)
- Atomic operations (reads and writes are instantaneous at each node)

---

## Common Misunderstandings

**"CAP means you pick two at all times"**
No. CAP applies only during partitions. When the network is healthy, you have both C and A. The trade-off only manifests when a partition occurs — which is why the real question is "what does your system do during a partition?"

**"Consistency in CAP = Consistency in ACID"**
These are different concepts. CAP consistency is linearizability (a distributed systems concept). ACID consistency means transaction constraints are preserved (a database concept). You can have ACID consistency with eventual consistency in the CAP sense.

**"Partition tolerance is optional"**
Only if you run on a single node, which is not a distributed system. Once you distribute, partitions are inevitable. You cannot design them away. You can make them rare (InfiniBand, dedicated network links) but not eliminate them.

**"AP systems are inconsistent"**
AP systems provide eventual consistency — not chaos. Reads may be transiently stale. The system will converge. "Inconsistent" implies data corruption; "eventually consistent" means temporary staleness, which is often acceptable.

**"You should always prefer CP"**
Depends entirely on the application. For a bank ledger: CP is mandatory. For a shopping cart (Amazon's Dynamo paper example): AP is preferable — it is worse to refuse a cart update than to show briefly stale inventory.

**"CAP is the only theorem that matters"**
CAP describes what you lose during a partition. PACELC describes what you trade even without one. FLP describes what is impossible in async consensus. All three matter for a complete picture.

---

## Decision Cheat Sheet

```
DECIDING CP VS. AP
+-----------------------------------------------+
| What happens if a user gets stale data?       |
|                                               |
|  "Data loss / incorrect charge / safety risk" |
|       → CP (accept unavailability)            |
|                                               |
|  "Slightly stale UI / recommendation mismatch" |
|       → AP (accept staleness)                 |
+-----------------------------------------------+
```

| Domain | Choice | Rationale |
|--------|--------|-----------|
| Bank ledger | CP | Lost writes = wrong money |
| Inventory management | AP | Oversell handled with refund |
| Configuration service | CP | Wrong config causes outage |
| Social media feed | AP | Stale feed is acceptable |
| Shopping cart | AP | Dynamo's original use case |
| Distributed lock | CP | Correctness requires it |
| DNS (cache) | AP | TTL-bounded staleness OK |
| Kubernetes control plane | CP | Wrong state causes cascading failures |
| Metrics counters | AP | Approximate counts acceptable |
