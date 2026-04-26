# Distributed Systems — Landscape

## Sentinel Context

This directory is one of three in the Sentinel triad (K-Spade C-IV). The thesis: *no single point of truth, no single point of trust, no single point of failure.*

```
THE SENTINEL TRIAD — Distributed Systems View
═══════════════════════════════════════════════════════════════════

              FLP Impossibility (1985)
              "No deterministic async consensus with 1 crash."
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ╔════════════╗   ┌───────────┐   ┌──────────────┐
  ║ DISTRIBUTED║   │ SECURITY  │   │ CLOUD        │
  ║ SYSTEMS    ║   │ ENG.      │   │ ARCHITECTURE │
  ║            ║   │           │   │              │
  ║ "Who has   ║   │ "Who do   │   │ "Where do    │
  ║  the       ║   │  you      │   │  you put     │
  ║  truth?"   ║   │  trust?"  │   │  the truth?" │
  ╚═════╤══════╝   └─────┬─────┘   └──────┬───────┘
        │                │                │
        └────────────────┴────────────────┘
                         │
              Consensus as unifying abstraction
```

Distributed systems provides the **theoretical floor** for the entire volume. FLP impossibility, CAP, and Byzantine fault tolerance are the constraints that security engineering and cloud architecture must work within. Every consistency model, every quorum, every replication strategy covered here sets the bounds on what can be achieved in the other two domains. When security engineering asks "how do we verify trust across nodes?" and cloud architecture asks "how do we survive AZ failure?", the answers begin with the consensus protocols and consistency guarantees defined here.

**See also:**
- `../computing/00-SENTINEL-THESIS.md` — Volume thesis: the Sentinel principle and constraint stack
- `../security-engineering/00-OVERVIEW.md` — Trust: the adversary model that consensus must survive
- `../cloud-architecture/00-OVERVIEW.md` — Infrastructure: where consensus protocols run at scale

---

## The Big Picture

A distributed system is a collection of independent computers that appears to its users as a single coherent system. The appearance of coherence is hard. The following diagram shows the fundamental landscape of problems.

```
+---------------------------------------------------------------------+
|                   DISTRIBUTED SYSTEMS PROBLEM SPACE                 |
+---------------------------------------------------------------------+
|                                                                      |
|   FUNDAMENTAL IMPOSSIBILITIES        FUNDAMENTAL PROBLEMS           |
|   +---------------------------+       +---------------------------+  |
|   | FLP (1985): No async      |       | Consensus                 |  |
|   | system can guarantee      |       | How do N nodes agree?    |   |
|   | consensus with 1 failure  |       +---------------------------+  |
|   +---------------------------+       | Consistency               |  |
|   | CAP Theorem: You cannot   |       | What does "read" return? |   |
|   | have C + A + P together   |       +---------------------------+  |
|   +---------------------------+       | Availability              |  |
|   | Einstein/SR: Speed of     |       | Does every request get    |  |
|   | light bounds coordination |       | a response?               |  |
|   +---------------------------+       +---------------------------+  |
|                                       | Partition Tolerance       |  |
|                                       | Works when network splits |  |
|                                       +---------------------------+  |
|                                                                      |
+---------------------------------------------------------------------+

THEORY LAYER                    ALGORITHM LAYER
+------------------+            +------------------+
| CAP Theorem      |            | Paxos            |
| PACELC           |            | Raft             |
| FLP Result       |            | Viewstamped Rep  |
| Consistency      |            | 2PC / 3PC        |
| Model Spectrum   |            | Sagas / CRDTs    |
+------------------+            +------------------+
         |                               |
         v                               v
SYSTEMS LAYER
+-------------------------------------------------------------+
| Spanner (Google)   | External consistency via TrueTime      |
| DynamoDB (Amazon)  | Eventual consistency, tunable quorums  |
| Kafka              | Ordered log, partition-level ordering  |
| ZooKeeper / etcd   | CP coordination services               |
| CosmosDB (Azure)   | 5 consistency levels, tunable          |
| CockroachDB        | Serializable SQL, Paxos per range      |
| Cassandra          | AP, tunable quorums, ring topology     |
+-------------------------------------------------------------+
```

---

## The 8 Fallacies of Distributed Computing (Peter Deutsch, 1994)

Every engineer who has built a distributed system has re-learned these. You built VSTS at scale — you've lived each one.

| # | Fallacy | Reality | VSTS Analogue |
|---|---------|---------|----------------|
| 1 | The network is reliable | Networks drop packets, TCP connections reset, VMs disappear | TFS agent drops mid-build; work item API times out |
| 2 | Latency is zero | Even in one datacenter: ~0.1–1ms. Cross-region: ~100ms | P2 build queries from West US to East US |
| 3 | Bandwidth is infinite | You cannot stream unlimited data; TCP backpressure kicks in | Git clone of a large mono-repo saturates bandwidth |
| 4 | The network is secure | Man-in-the-middle, TLS downgrade, DNS hijack | VSTS service-to-service calls inside Azure still need mTLS |
| 5 | Topology doesn't change | IPs change, VMs migrate, AZs fail, DNS propagates slowly | Azure maintenance events move VMs; your IP changes |
| 6 | There is one administrator | Multiple teams own different segments; no single change window | DB team, network team, app team all operate independently |
| 7 | Transport cost is zero | Serialization, deserialization, header parsing all cost CPU | ADO protobuf vs. REST JSON performance difference |
| 8 | The network is homogeneous | Your clients run on wildly different OS/runtime versions | VSTS web, VS IDE client, REST API, and CLI all talk to same svc |

---

## The Taxonomy of Distributed System Challenges

```
DISTRIBUTED SYSTEM CHALLENGES
│
├── SAFETY (what must never happen)
│   ├── Consistency violations (stale reads, lost writes)
│   ├── Ordering violations (causality broken)
│   └── Security violations (unauthorized access, MITM)
│
├── LIVENESS (what must eventually happen)
│   ├── Availability (every request gets a response)
│   ├── Progress (operations complete — no deadlock)
│   └── Termination (algorithms finish — no livelock)
│
├── FAULT TOLERANCE
│   ├── Crash failures (node stops, silent)
│   ├── Omission failures (messages lost)
│   ├── Timing failures (too slow, not crash)
│   ├── Byzantine failures (arbitrary / malicious)
│   └── Network partitions (split brain)
│
├── COORDINATION
│   ├── Leader election
│   ├── Distributed locking (lease-based)
│   ├── Barrier synchronization
│   └── Atomic broadcast
│
└── DATA MANAGEMENT
    ├── Replication (durability, read scaling)
    ├── Sharding / partitioning (write scaling)
    ├── Distributed transactions (atomicity across nodes)
    └── Schema evolution (rolling deploys)
```

---

## Theory Meets Practice: Key Papers → Production Systems

| Paper | Year | Key Idea | Production Use |
|-------|------|----------|----------------|
| Lamport Clocks | 1978 | Happens-before ordering without synchronized clocks | Causally ordered logs everywhere |
| Vector Clocks | 1988 | Per-process logical clocks, detect causality violations | DynamoDB, Riak conflict detection |
| Paxos | 1989/1998 | Consensus in asynchronous system with crash failures | Chubby (Google), CosmosDB internally |
| FLP Impossibility | 1985 | Consensus impossible with 1 crash in fully async system | Motivation for Raft's design choices |
| CAP Theorem | 2000/2002 | C + A + P not simultaneously achievable | Every distributed DB design trade-off |
| Dynamo | 2007 | Eventual consistency, vector clocks, sloppy quorum | DynamoDB, Cassandra, Riak |
| Bigtable | 2006 | Sorted string tables, LSM-tree, column families | HBase, Cassandra, RocksDB, LevelDB |
| Spanner | 2012 | External consistency via TrueTime (atomic clocks) | Cloud Spanner, CockroachDB |
| Raft | 2014 | Understandable consensus (vs. Paxos complexity) | etcd (Kubernetes), CockroachDB, TiKV |
| Kafka | 2011 | Distributed commit log, consumer group model | Kafka everywhere; Event Hubs compatible |

---

## The Fundamental Triangle: Consistency vs. Availability vs. Partition Tolerance

```
            Consistency
               /\
              /  \
             /    \
            /  ?   \
           /        \
          +----------+
   Availability    Partition
                   Tolerance

CAP says: pick 2. But partitions WILL happen.
So the real choice is: CP or AP during a partition.
```

Full CAP analysis in `01-CAP-THEOREM.md`. Consistency model spectrum in `02-CONSISTENCY-MODELS.md`.

---

## Where VSTS/Azure DevOps Sits in This Landscape

VSTS (now Azure DevOps) is a large-scale distributed system. The problems you solved daily map directly to distributed systems theory:

```
AZURE DEVOPS / VSTS                    DISTRIBUTED SYSTEMS CONCEPT
+----------------------------------+   +----------------------------------+
| Work item IDs are globally       |   | Sequence numbers require         |
| unique and monotonically         | → | consensus or coordination        |
| increasing                       |   | (Snowflake IDs, or a sequencer)  |
+----------------------------------+   +----------------------------------+
| Git repositories replicated     |   | Replication with strong          |
| across datacenters for reads     | → | consistency for writes (leader), |
| with geo-failover                |   | eventual for reads (followers)   |
+----------------------------------+   +----------------------------------+
| Build queue: multiple agents,   |   | Distributed job scheduling,       |
| at-least-once delivery,         | → | idempotent execution, poison      |
| retry with backoff               |   | message handling                 |
+----------------------------------+   +----------------------------------+
| Service Bus for inter-service   |   | Reliable messaging, at-least-    |
| communication between ADO       | → | once delivery, consumer groups,  |
| microservices                    |   | offset tracking                  |
+----------------------------------+   +----------------------------------+
| SQL Azure with retry logic for  |   | Network transience, partial       |
| transient failures               | → | failure handling, idempotent     |
|                                  |   | writes                           |
+----------------------------------+   +----------------------------------+
```

CosmosDB (the database underlying many Azure services) uses Paxos internally for replica agreement, and exposes 5 consistency levels as a product decision — the theory is the product feature.

---

## Guide Map

```
00-OVERVIEW.md         ← you are here
01-CAP-THEOREM.md      ← formal bounds: what's provably impossible
02-CONSISTENCY-MODELS.md ← the spectrum from strict to eventual
03-CONSENSUS.md        ← Paxos, Raft, Zab — how algorithms achieve agreement
04-REPLICATION.md      ← single-leader, multi-leader, leaderless patterns
05-DISTRIBUTED-TXN.md  ← 2PC, Sagas, CRDTs, TrueTime
06-DISTRIBUTED-DB.md   ← Spanner, DynamoDB, Cassandra, CosmosDB
07-MESSAGE-QUEUES.md   ← Kafka internals, exactly-once, Azure Event Hubs
08-MICROSERVICES.md    ← service mesh, circuit breakers, bulkheads
09-OBSERVABILITY.md    ← traces, metrics, logs, chaos engineering
```

---

## Common Confusion Points

**"Distributed system" vs. "microservices"**
Microservices is an architectural style. Distributed systems is the broader category. A microservices system is a distributed system, but Kafka, Spanner, and HDFS are also distributed systems that aren't microservices.

**"Partitioning" has two meanings**
Network partition = the failure mode (split brain). Data partitioning/sharding = splitting data across nodes for scalability. Both appear constantly; context determines meaning.

**"Eventual consistency" is not broken consistency**
It means reads may return stale data but will eventually converge to the latest written value. It is a deliberate trade-off (higher availability, lower latency) not a bug.

**"Distributed system" vs. "parallel system"**
Parallel systems (multi-core, GPU) share memory and a clock. Distributed systems do not. The absence of shared memory and synchronized clocks is what makes distributed systems hard.
