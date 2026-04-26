# Consensus Theory: Impossibility Results, Byzantine Faults, and Protocol Internals

## Sentinel Context

This guide is the theoretical spine of the Sentinel triad. Where `03-CONSENSUS.md` covers Paxos, Raft, and Zab at the protocol level, this guide goes underneath: the impossibility results that bound what any protocol can achieve, the Byzantine fault model that bridges into security engineering, and the formal safety/liveness arguments that separate correct protocols from plausible-looking broken ones.

The Sentinel principle --- *no single point of truth, no single point of trust, no single point of failure* --- is ultimately a claim about what consensus can and cannot guarantee. This guide makes that claim precise.

---

## The Big Picture

```
CONSENSUS THEORY — THE CONSTRAINT STACK
═══════════════════════════════════════════════════════════════════════

  IMPOSSIBILITY RESULTS (what you CANNOT do)
  ┌─────────────────────────────────────────────────────────────┐
  │ FLP (1985)     No deterministic async consensus             │
  │                with even 1 crash fault                      │
  │                                                             │
  │ CAP (2002)     No simultaneous C + A + P                    │
  │                                                             │
  │ BFT bound      Need 3f+1 nodes for f Byzantine faults       │
  │                (Lamport-Shostak-Pease 1982)                 │
  └─────────────────────────┬───────────────────────────────────┘
                            │
                   "Given these constraints..."
                            │
                            ▼
  PROTOCOL DESIGN (how you WORK WITHIN the constraints)
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  CRASH FAULT TOLERANT (f crashes, 2f+1 nodes)               │
  │  ┌───────────┐  ┌──────────┐  ┌──────────────────┐        │
  │  │ Paxos     │  │ Raft     │  │ Viewstamped Rep  │        │
  │  │ (1989)    │  │ (2014)   │  │ (1988)           │        │
  │  └───────────┘  └──────────┘  └──────────────────┘        │
  │                                                             │
  │  BYZANTINE FAULT TOLERANT (f Byzantine, 3f+1 nodes)        │
  │  ┌───────────┐  ┌──────────┐  ┌──────────────────┐        │
  │  │ PBFT      │  │ Tendermint│  │ HotStuff         │       │
  │  │ (1999)    │  │ (2014)   │  │ (2019)           │        │
  │  └───────────┘  └──────────┘  └──────────────────┘        │
  │                                                             │
  └─────────────────────────┬───────────────────────────────────┘
                            │
                   "Deployed in practice as..."
                            │
                            ▼
  PRODUCTION SYSTEMS
  ┌─────────────────────────────────────────────────────────────┐
  │ ZooKeeper (ZAB)   etcd (Raft)    Spanner (Paxos+TrueTime) │
  │ CockroachDB (Raft+MVCC)  TiKV (Raft)  Consul (Raft)      │
  │ Hyperledger (PBFT)  Cosmos SDK (Tendermint)                 │
  └─────────────────────────────────────────────────────────────┘
```

---

## Part I: Impossibility Results

### FLP Impossibility (Fischer, Lynch, Paterson — 1985)

The FLP result is arguably the most important negative result in distributed computing. It stands in the same tradition as the Halting Problem (Turing 1936) and Goedel's incompleteness theorems --- a proof that a seemingly natural goal is provably unachievable under stated assumptions.

**Formal Statement**: There is no deterministic protocol that solves consensus in an asynchronous message-passing system if even one process can fail by crashing.

**The three properties of consensus:**

| Property | Meaning |
|----------|---------|
| **Agreement** | All non-faulty processes decide the same value |
| **Validity** | The decided value was proposed by some process |
| **Termination** | Every non-faulty process eventually decides |

FLP says: you cannot have all three simultaneously in an asynchronous system with crash faults. Any deterministic algorithm that guarantees Agreement and Validity can be prevented from Terminating by an adversarial scheduler.

#### Proof Sketch

The proof proceeds in three stages. Each uses a carefully chosen adversarial scheduling of message deliveries.

**Stage 1: Bivalent initial configurations exist.**

A configuration is *bivalent* if both decision values (0 and 1) are still reachable from it. A configuration is *0-valent* (resp. *1-valent*) if only 0 (resp. 1) is reachable.

```
CONFIGURATION SPACE
                    ┌─────────────┐
                    │  Initial    │
                    │  configs    │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
         ┌─────────┐ ┌─────────┐ ┌─────────┐
         │0-valent │ │BIVALENT │ │1-valent │
         │(only 0  │ │(both 0  │ │(only 1  │
         │reachable)│ │and 1    │ │reachable)│
         └─────────┘ │reachable)│ └─────────┘
                      └─────────┘
```

Claim: at least one initial configuration is bivalent. Proof by contradiction: if all initial configurations were univalent (either 0-valent or 1-valent), then because initial configurations differ only in which process proposes which value, there must be two adjacent initial configurations C0 (0-valent) and C1 (1-valent) that differ only in one process p's proposed value. If p crashes immediately (before sending any message), the remaining processes see the same state in both C0 and C1. But C0 must decide 0 and C1 must decide 1 --- contradiction, since the remaining processes cannot distinguish the two cases.

**Stage 2: From any bivalent configuration, you can reach another bivalent configuration.**

Given a bivalent configuration C and a pending message m (to process p), consider all configurations reachable from C by delivering m (possibly after other messages). Call this set D.

Claim: D contains a bivalent configuration. Proof by contradiction: suppose all configurations in D are univalent. Then D contains both 0-valent and 1-valent configurations (since C is bivalent). There must exist two configurations d0 (0-valent) and d1 (1-valent) in D that are "adjacent" --- they differ by one step. Either:

- **Case 1**: The differing step involves a process other than p. Then one configuration is reachable from the other by delivering a single additional message. But a 0-valent configuration cannot reach a 1-valent one --- contradiction.

- **Case 2**: The differing step involves p itself. If p crashes after delivering m, both d0 and d1 become indistinguishable to remaining processes (p is silent in both). But one must decide 0 and the other 1 --- contradiction.

**Stage 3: The adversary can keep the system bivalent forever.**

By Stage 2, the adversary can always find a message delivery schedule that moves from one bivalent configuration to another. Repeating ad infinitum, the adversary prevents the system from ever reaching a univalent (decided) configuration. Termination is violated.

```
ADVERSARY STRATEGY
  Bivalent ──deliver m──> Bivalent ──deliver m'──> Bivalent ──> ...
     C₀                     C₁                      C₂

  The adversary picks which pending message to delay or deliver
  to maintain bivalency at each step. Because the system is
  asynchronous, there is no timeout to force a decision.
```

#### Why FLP Matters for MIT TCS Context

FLP is a computability result, not a complexity result. It says the *problem is unsolvable* in the stated model --- the same strength of negative result as the Halting Problem. Just as Rice's theorem generalizes the Halting Problem to all non-trivial semantic properties, FLP generalizes to show that no non-trivial distributed agreement problem is solvable in fully async systems with crash faults.

The connection is formal:

| Computability Result | Domain | Statement |
|---------------------|--------|-----------|
| Halting Problem | Sequential computation | No TM decides halting for all TMs |
| Rice's Theorem | Sequential computation | No non-trivial semantic property is decidable |
| FLP Impossibility | Distributed computation | No deterministic protocol solves consensus in async + crash |
| CAP Theorem | Distributed computation | No protocol achieves C + A + P simultaneously |

#### The Escape Hatches

FLP assumes: (1) fully asynchronous (no timing bounds), (2) deterministic protocols, (3) at least one crash fault. Violate any assumption and consensus becomes solvable:

```
FLP ESCAPE ROUTES
┌──────────────────────────┬───────────────────────────────────┐
│ Violate Assumption       │ How It Enables Consensus          │
├──────────────────────────┼───────────────────────────────────┤
│ Partial synchrony        │ Timeouts detect crashes.          │
│ (DLS 1988)               │ Paxos, Raft use this.             │
│                          │ Safety always holds; liveness     │
│                          │ holds when network stabilizes.    │
├──────────────────────────┼───────────────────────────────────┤
│ Randomization            │ Ben-Or (1983): randomized async   │
│                          │ consensus terminates w.p. 1.      │
│                          │ Expected O(2^n) rounds. Impractical│
│                          │ alone; useful combined with       │
│                          │ partial synchrony.                │
├──────────────────────────┼───────────────────────────────────┤
│ Failure detectors        │ Chandra-Toueg (1996): weakest     │
│                          │ failure detector ◇W that solves   │
│                          │ consensus. Equivalent to partial  │
│                          │ synchrony in practice.            │
├──────────────────────────┼───────────────────────────────────┤
│ No faults (0 crashes)    │ Trivially solvable — broadcast    │
│                          │ and wait. Not useful in practice. │
└──────────────────────────┴───────────────────────────────────┘
```

**Partial synchrony (Dwork-Lynch-Stockmeyer, 1988)**: The network is asynchronous for some unknown but finite period, after which message delays are bounded by some unknown but finite delta. Under partial synchrony, consensus is solvable. All practical consensus protocols (Paxos, Raft, PBFT) operate under this assumption.

---

### CAP Theorem — Formal Treatment

`01-CAP-THEOREM.md` covers CAP at the systems level. Here is the formal result.

**Theorem (Gilbert & Lynch, 2002)**: It is impossible for a distributed read/write storage system to simultaneously provide all three of:
- **Consistency (C)**: Linearizability --- every read returns the most recent write
- **Availability (A)**: Every request to a non-failing node receives a response
- **Partition Tolerance (P)**: The system operates despite arbitrary message loss

**Formal proof**: Consider two nodes G1, G2 separated by a partition. Client writes v=1 to G1 (availability requires G1 to ack). Client reads v from G2 (availability requires G2 to respond). G2 cannot have received the write (partition). G2 returns stale v=0. Consistency (linearizability) is violated. QED.

The theorem is tight: 2-of-3 is achievable. CP systems (ZooKeeper) refuse reads during partition. AP systems (DynamoDB default) return stale data during partition. CA systems exist only as single-node systems where P is vacuously satisfied.

**CAP is not a design knob you set once.** Different operations in the same system can make different CAP trade-offs. A single database can offer linearizable reads (CP) on the primary and eventually-consistent reads (AP) on replicas. The choice is per-operation, not per-system.

---

### The 3f+1 Byzantine Bound (Lamport, Shostak, Pease — 1982)

#### The Byzantine Generals Problem

Lamport's original formulation: a group of Byzantine generals, each commanding a division, must agree on a common battle plan. Some generals may be traitors who send inconsistent messages to different generals. The loyal generals must all agree on the same plan, and if the commanding general is loyal, the plan must be the commanding general's plan.

```
THE BYZANTINE GENERALS — 4 GENERALS, 1 TRAITOR

  Scenario A: General 3 is the traitor
  ┌─────────┐     "attack"     ┌─────────┐
  │General 1│────────────────> │General 2│
  │(loyal)  │<────────────────│(loyal)   │
  └────┬────┘    "attack"      └────┬────┘
       │                            │
  "attack"                     "attack"
       │    ┌─────────┐            │
       └───>│General 3│<───────────┘
            │(TRAITOR)│
            └────┬────┘
                 │
        Sends "attack" to Gen 1
        Sends "retreat" to Gen 2
        → Gen 1 thinks: 3 votes attack  (attack, attack, attack) → attack
        → Gen 2 thinks: 2 votes attack, 1 retreat → attack (majority)
        WORKS: loyal generals still agree

  Scenario B: 3 generals, 1 traitor — FAILS
  ┌─────────┐     "attack"     ┌─────────┐
  │General 1│────────────────> │General 2│
  │(loyal)  │<────────────────│(loyal)   │
  └────┬────┘    "attack"      └────┬────┘
       │                            │
       │    ┌─────────┐            │
       └───>│General 3│<───────────┘
            │(TRAITOR)│
            └─────────┘
        Sends "attack" to Gen 1
        Sends "retreat" to Gen 2
        → Gen 1 sees: (attack, attack, attack) → attack
        → Gen 2 sees: (attack, attack, retreat) → attack? or retreat?
        Gen 2 cannot tell if Gen 1 or Gen 3 is lying.
        With 3 nodes, 1 traitor → no solution exists.
```

#### Proof of the 3f+1 Bound

**Theorem**: Byzantine agreement requires at least 3f+1 nodes to tolerate f Byzantine faults.

**Proof by contradiction (f=1, 3 nodes):**

Assume a correct protocol P exists for 3 nodes, tolerating 1 Byzantine fault. Consider three processes: A, B, C.

```
IMPOSSIBILITY WITH 3 NODES, 1 BYZANTINE FAULT

Scenario 1: C is Byzantine.
  A proposes 0. B proposes 1. C sends 0 to A, 1 to B.
  A sees (0, ?, 0) — cannot distinguish from Scenario 2.
  B sees (?, 1, 1) — cannot distinguish from Scenario 3.

Scenario 2: B is Byzantine.
  A proposes 0. C proposes 0. B sends contradictory messages.
  A's view is identical to Scenario 1.
  → If protocol decides 0 in Scenario 2 (validity: both loyal propose 0)...

Scenario 3: A is Byzantine.
  B proposes 1. C proposes 1. A sends contradictory messages.
  B's view is identical to Scenario 1.
  → If protocol decides 1 in Scenario 3 (validity: both loyal propose 1)...

But in Scenario 1, A expects decision 0 (same view as Scenario 2)
and B expects decision 1 (same view as Scenario 3).
Agreement is violated. Contradiction.
```

**Generalization**: For f Byzantine faults, you need:
- **3f+1 nodes** total (for agreement)
- **2f+1 honest nodes** must form a quorum (to outvote the f Byzantine nodes)
- Quorum size: at least `(n + f + 1) / 2` where n = 3f+1

| Byzantine faults (f) | Nodes required (3f+1) | Quorum size |
|----------------------|----------------------|-------------|
| 1 | 4 | 3 |
| 2 | 7 | 5 |
| 3 | 10 | 7 |
| 10 | 31 | 21 |
| 33% of n | n | 2n/3 + 1 |

#### Why 3f+1 and Not 2f+1?

Crash faults need only 2f+1 nodes because a crashed node is *silent* --- it stops sending messages. A Byzantine node is *actively malicious* --- it sends conflicting messages to different nodes. The extra f nodes are needed to "outvote" the Byzantine nodes in every scenario. With 2f+1 nodes and f Byzantine faults, the remaining f+1 honest nodes cannot distinguish whether the conflicting messages come from the other f honest nodes or the f Byzantine ones.

```
CRASH vs. BYZANTINE — WHY THE BOUND DIFFERS

Crash model:    Silent failure. Honest nodes get no message from crashed node.
                Quorum = majority of alive nodes. 2f+1 total suffices.

Byzantine model: Active deception. Byzantine node sends DIFFERENT values
                 to different honest nodes.
                 Need enough honest nodes to cross-check:
                 2f+1 honest nodes needed → 3f+1 total.

                 INTUITION: you need f+1 agreeing honest reports to
                 outvote f potentially-conflicting Byzantine reports.
                 f+1 honest who agree + f who might disagree + f Byzantine
                 = 3f+1.
```

---

## Part II: Paxos — Safety Proof and Multi-Paxos Engineering

`03-CONSENSUS.md` describes the Paxos protocol. Here we prove why it works.

### Paxos Safety: Why the Chosen Value Cannot Change

The key invariant is: **once a value v is chosen (accepted by a quorum), no different value v' can ever be chosen.**

**Proof sketch** (by induction on proposal numbers):

Define: value v is *chosen at proposal number n* if a quorum of acceptors accepted (n, v).

**Claim**: If v is chosen at proposal number n, then for every proposal number m > n, the value proposed with m is also v.

**Base case**: v is chosen at n. Consider the smallest m > n for which a proposal is issued.

**Inductive step**: The proposer for m must complete Phase 1, collecting promises from a quorum Q_m. Since v was chosen at n, a quorum Q_n accepted (n, v). Quorums overlap (both are majorities), so Q_m and Q_n share at least one acceptor, say a. Acceptor a accepted (n, v) and promised to m. In its promise, a reports (n, v) as the highest-numbered accepted proposal. The proposer for m must adopt v (it uses the value from the highest-numbered accepted proposal among promises). Therefore, the proposal for m is (m, v).

```
PAXOS SAFETY PROOF — QUORUM OVERLAP

   Quorum Q_n (accepted v at n)     Quorum Q_m (promised to m)
   ┌───────────────────────┐       ┌───────────────────────┐
   │  a₁  a₂  a₃          │       │       a₃  a₄  a₅     │
   │                       │       │                       │
   │ All accepted (n, v)   │       │ All promised to m>n   │
   └───────────────────────┘       └───────────────────────┘
                    │                │
                    └────────┬───────┘
                             │
                         OVERLAP: a₃
                         a₃ accepted (n, v) AND promised to m
                         → Proposer for m learns about (n, v)
                         → Proposer for m must use v
                         → Safety preserved
```

**Liveness**: Paxos does NOT guarantee liveness. Two competing proposers can livelock:

```
PAXOS LIVELOCK (dueling proposers)

  Proposer A                    Proposer B
  PREPARE(1) ──────────────>
                                PREPARE(2) ──────────────>
  ACCEPT(1,v) ─── REJECTED ──  (acceptors promised 2)
  PREPARE(3) ──────────────>
                                ACCEPT(2,w) ── REJECTED ── (acceptors promised 3)
                                PREPARE(4) ──────────────>
  ... ad infinitum ...

  SOLUTION: Elect a distinguished leader. Only the leader proposes.
  If the leader fails, elect a new one. This is Multi-Paxos.
```

Multi-Paxos solves this by using a stable leader who runs Phase 1 once and then runs only Phase 2 for each new log entry. Leader failure triggers a new election (which is itself a Paxos instance).

### Multi-Paxos: From Single Value to Replicated Log

```
MULTI-PAXOS ARCHITECTURE

  Leader (elected via Paxos)
  ┌──────────────────────────────────────────────────┐
  │ Log slot 1:  value=X   (Phase 2 only — decided)  │
  │ Log slot 2:  value=Y   (Phase 2 only — decided)  │
  │ Log slot 3:  value=Z   (Phase 2 in progress)     │
  │ Log slot 4:  (empty — awaiting client request)   │
  └──────────────────────────────────────────────────┘
       │              │              │
       ▼              ▼              ▼
  ┌─────────┐   ┌─────────┐   ┌─────────┐
  │Acceptor1│   │Acceptor2│   │Acceptor3│
  │ Log:    │   │ Log:    │   │ Log:    │
  │ 1:X ✓  │   │ 1:X ✓  │   │ 1:X ✓  │
  │ 2:Y ✓  │   │ 2:Y ✓  │   │ 2:Y ✓  │
  │ 3:Z ?  │   │ 3:Z ✓  │   │ 3:Z ?  │
  └─────────┘   └─────────┘   └─────────┘

  OPTIMIZATION: Leader runs Phase 1 once per term.
  Each new log entry: only Phase 2 (1 RTT to quorum).
  Normal-case latency: 1 round-trip.
```

**The 43 questions Paxos does not answer** (from Ongaro's 2014 thesis):
- How is the leader elected? (Paxos says "run another Paxos" --- circular)
- What happens with log gaps? (Leader crashes mid-replication)
- How are snapshots taken? (Log grows unbounded)
- How are membership changes handled? (Add/remove nodes)
- What is the wire protocol? (Paxos describes abstract messages)
- How is the leader's log reconciled with divergent followers?

These gaps are why Raft was created.

---

## Part III: Raft — Safety Proof and Why It Succeeded

`03-CONSENSUS.md` describes Raft's mechanics. Here we prove its safety property and explain the design philosophy.

### Raft's Key Safety Property: Leader Completeness

**Leader Completeness Property**: If a log entry is committed in a given term, then that entry will be present in the logs of all leaders for all higher-numbered terms.

This is the single most important safety property. It guarantees that no committed data is ever lost, even across leader changes.

**Proof**:

Suppose entry e is committed at index i in term T. We show by contradiction that every leader of term U > T has e at index i.

1. e is committed → a majority of nodes have e at index i.
2. Leader of term U wins election → a majority of nodes voted for it.
3. Any two majorities overlap → at least one node (call it voter) has e at index i AND voted for the leader of U.
4. The voter would only vote for the leader of U if the leader's log is at least as up-to-date as the voter's log (Raft's RequestVote restriction).
5. "At least as up-to-date" means: the leader of U's last log entry has a term >= voter's last log entry's term, or same term and >= length.
6. Since voter has e (committed in term T), and the leader of U's log is at least as up-to-date, the leader of U must also have e.

```
RAFT LEADER COMPLETENESS — WHY COMMITTED ENTRIES PERSIST

  Term T: Entry e committed (majority has it)
  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
  │ N1  │  │ N2  │  │ N3  │  │ N4  │  │ N5  │
  │ e ✓ │  │ e ✓ │  │ e ✓ │  │     │  │     │
  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘
     majority has e

  Term U > T: New leader must get majority vote
  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
  │ N1  │  │ N2  │  │ N3  │  │ N4  │  │ N5  │
  │ e ✓ │  │ e ✓ │  │ e ✓ │  │     │  │     │
  │vote?│  │vote?│  │vote?│  │vote?│  │vote?│
  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘

  Any majority of voters MUST include at least one of {N1, N2, N3}.
  That voter has e, and will only vote for a candidate whose log
  is at least as up-to-date → candidate must have e too.
  → New leader has e. QED.
```

### Why Raft Succeeded Where Paxos Confused

Ongaro and Ousterhout designed Raft explicitly for understandability, not for novelty. Their key design decisions:

```
RAFT vs. PAXOS — DESIGN PHILOSOPHY

  PAXOS APPROACH                    RAFT APPROACH
  ┌────────────────────────┐       ┌────────────────────────┐
  │ Symmetric roles        │       │ Strong leader          │
  │ Any node can propose   │       │ Only leader proposes   │
  │ No distinguished leader│       │ Followers passive      │
  │ in single-decree       │       │                        │
  ├────────────────────────┤       ├────────────────────────┤
  │ Log entries independent│       │ Log entries flow       │
  │ Each slot: separate    │       │ left-to-right from     │
  │ Paxos instance         │       │ leader to followers    │
  ├────────────────────────┤       ├────────────────────────┤
  │ Gaps possible in log   │       │ No gaps: Log Matching  │
  │ Slots filled out of    │       │ Property ensures       │
  │ order                  │       │ prefix consistency     │
  ├────────────────────────┤       ├────────────────────────┤
  │ Membership change:     │       │ Joint consensus:       │
  │ left as exercise       │       │ fully specified         │
  ├────────────────────────┤       ├────────────────────────┤
  │ Snapshotting:          │       │ Snapshotting:          │
  │ not discussed          │       │ fully specified        │
  └────────────────────────┘       └────────────────────────┘

  RESULT: Raft's TLA+ spec is complete enough to implement from.
  Paxos requires reading 5+ papers and still making engineering
  decisions not covered in any of them.
```

**Ongaro's user study** (Stanford, 2014): 43 students learned Paxos and Raft. On comprehension tests, students scored significantly higher on Raft. On implementation exercises, students produced more correct implementations of Raft. The difference was not in difficulty of the underlying problem --- it was in the presentation and decomposition of the protocol into understandable subproblems.

---

## Part IV: Practical BFT (PBFT) — Castro & Liskov, 1999

PBFT was the first practical Byzantine fault tolerant protocol. Before PBFT, BFT protocols had exponential message complexity. PBFT brought it to O(n^2), making BFT feasible for small clusters.

### System Model

```
PBFT SYSTEM MODEL
  - N = 3f+1 replicas (tolerates f Byzantine faults)
  - One primary (leader), others are backups
  - Asynchronous network with eventual delivery
  - Cryptographic assumptions: MACs and digital signatures unforgeable
  - Client authenticates with all replicas (cannot be Byzantine)
```

### The Three-Phase Protocol

```
PBFT PROTOCOL — NORMAL CASE OPERATION

Client   Primary(0)   Replica(1)   Replica(2)   Replica(3)
  │          │             │             │             │
  │─REQUEST─>│             │             │             │
  │          │             │             │             │
  │          │──PRE-PREPARE(v,n,d)──────────────────>  │  Phase 1
  │          │  "I assign sequence n     │             │
  │          │   to request with         │             │
  │          │   digest d in view v"     │             │
  │          │             │             │             │
  │          │<──PREPARE(v,n,d,i)────────────────────  │  Phase 2
  │          │  Each backup verifies:    │             │
  │          │  - valid view number      │             │
  │          │  - sequence n not reused  │             │
  │          │  - digest matches request │             │
  │          │  Then broadcasts PREPARE  │             │
  │          │             │             │             │
  │          │  PREPARED = received 2f   │             │
  │          │  matching PREPAREs        │             │
  │          │  (from different replicas)│             │
  │          │             │             │             │
  │          │<──COMMIT(v,n,d,i)─────────────────────  │  Phase 3
  │          │  Each replica that has    │             │
  │          │  PREPARED broadcasts      │             │
  │          │  COMMIT                   │             │
  │          │             │             │             │
  │          │  COMMITTED-LOCAL =        │             │
  │          │  received 2f+1 COMMITs    │             │
  │          │             │             │             │
  │<─────────REPLY(v,t,i,result)─────────────────────  │
  │  Client waits for f+1                              │
  │  matching REPLYs                                   │
  │  (guarantees at least                              │
  │   one honest replica                               │
  │   agrees on result)                                │
```

### Why Three Phases?

Two phases are not enough for BFT. The PRE-PREPARE establishes a total order (the primary assigns a sequence number). The PREPARE phase ensures that 2f+1 replicas agree on this ordering *within the current view*. The COMMIT phase ensures the ordering survives view changes (primary failure).

```
WHY PREPARE IS NOT ENOUGH (need COMMIT)

  View v: Primary orders request as n=5.
  2f+1 replicas PREPARE → everyone agrees: n=5 maps to request R.

  Now the primary fails. New view v+1.
  Problem: Not all replicas may have received all PREPARE messages.
  Some replicas only saw 1 or 2 PREPAREs (not the full 2f).
  Without the COMMIT phase, these replicas do not know that n=5
  was agreed upon. They might accept a different request at n=5
  in the new view.

  COMMIT fixes this: a replica only executes after 2f+1 COMMITs,
  which means 2f+1 replicas PREPARED, which means any new primary
  in view v+1 will find at least f+1 honest replicas who committed.
```

### Message Complexity

```
PBFT MESSAGE COMPLEXITY PER REQUEST

  Phase           Messages                    Complexity
  ─────────────   ─────────────────────────   ──────────
  PRE-PREPARE     Primary → all backups       O(n)
  PREPARE         Each backup → all others    O(n²)
  COMMIT          Each replica → all others   O(n²)
  REPLY           All replicas → client       O(n)
                                              ──────────
  TOTAL                                       O(n²)

  For n=4 (f=1):   ~48 messages per request
  For n=7 (f=2):   ~147 messages per request
  For n=31 (f=10): ~2,883 messages per request

  THIS IS WHY PBFT DOES NOT SCALE:
  O(n²) per operation means throughput degrades quadratically
  with cluster size. Practical limit: ~10-20 replicas.
```

### View Change (Primary Failure Recovery)

```
VIEW CHANGE PROTOCOL (simplified)

1. Backup suspects primary is faulty (timeout or inconsistent messages)
2. Backup broadcasts VIEW-CHANGE(v+1, ..., prepared-proofs)
   Contains proof of all requests that were PREPARED in previous views
3. When new primary collects 2f VIEW-CHANGE messages:
   Broadcasts NEW-VIEW(v+1, ..., pre-prepares-for-pending)
   Re-proposes all requests that were prepared but not committed
4. Normal protocol resumes in new view v+1

COST: View changes are expensive — O(n³) messages in worst case.
The system is unavailable during view changes.
```

### PBFT and Blockchain

PBFT was largely academic until blockchain revived BFT interest:

```
PBFT IN BLOCKCHAIN CONTEXT

  PERMISSIONED BLOCKCHAINS (known validators)
  ┌────────────────────────────┬─────────────────────────────┐
  │ System                     │ BFT Protocol                │
  ├────────────────────────────┼─────────────────────────────┤
  │ Hyperledger Fabric         │ PBFT (original, now pluggable)│
  │ Tendermint / Cosmos SDK    │ Tendermint BFT (PBFT variant)│
  │ Zilliqa                    │ PBFT + PoW committee election│
  │ Diem (Meta, discontinued)  │ HotStuff (linear BFT)       │
  └────────────────────────────┴─────────────────────────────┘

  PERMISSIONLESS BLOCKCHAINS (unknown validators)
  ┌────────────────────────────┬─────────────────────────────┐
  │ System                     │ Consensus Mechanism         │
  ├────────────────────────────┼─────────────────────────────┤
  │ Bitcoin                    │ Nakamoto consensus (PoW)     │
  │ Ethereum (post-Merge)      │ Gasper (Casper FFG + LMD)   │
  │ Solana                     │ Tower BFT (PoH + PBFT-like) │
  └────────────────────────────┴─────────────────────────────┘

  KEY DIFFERENCE:
  PBFT: O(n²), works for small n (10-100 validators)
  Nakamoto: O(n) messages, works for large n (thousands of miners)
            but probabilistic finality (not deterministic)
```

### HotStuff: Linear BFT (2019)

HotStuff reduces PBFT's O(n^2) normal-case to O(n) by using a threshold signature scheme and pipelining.

```
HOTSSTUFF vs. PBFT

  PBFT:  All-to-all communication in PREPARE and COMMIT phases
         → O(n²) messages

  HOTSTUFF: Star topology — all messages go through the leader
            Leader collects votes, forms threshold certificate
            → O(n) messages per phase

  3-PHASE HOTSTUFF:
    Phase 1 (PREPARE):  Leader proposes → collects n-f votes → QC₁
    Phase 2 (PRE-COMMIT): Leader sends QC₁ → collects n-f votes → QC₂
    Phase 3 (COMMIT):  Leader sends QC₂ → collects n-f votes → QC₃
    DECIDE: Leader sends QC₃ → replicas execute

  View change: single-phase (leader sends highest QC, nodes vote)
  → O(n) view change cost (vs. PBFT's O(n³))

  USED BY: Diem (LibraBFT), Aptos, Flow blockchain
```

---

## Part V: Consensus in Production

### ZooKeeper (ZAB — ZooKeeper Atomic Broadcast)

```
ZAB PROTOCOL DETAILS

  MODEL: Primary-backup with ordered broadcast
  NODES: 2f+1 (typically 3 or 5)
  LEADER: Elected via Fast Leader Election (FLE)

  NORMAL OPERATION:
    Client → Leader: write(path, data)
    Leader assigns zxid (epoch, counter)
    Leader → Followers: PROPOSAL(zxid, txn)
    Followers: write to disk → ACK
    Leader: received quorum ACKs → COMMIT(zxid)
    Followers: apply to in-memory tree

  ZAB GUARANTEES:
    - Total order: all replicas deliver in same zxid order
    - Prefix property: if txn T is delivered, all T' < T are delivered first
    - Primary integrity: if primary broadcasts T, it has delivered all T' < T
    - Reliable delivery: if any replica delivers T, all eventually deliver T

  ZAB vs. RAFT DIFFERENCES:
  ┌──────────────────────┬──────────────────────────┐
  │ ZAB                  │ Raft                     │
  ├──────────────────────┼──────────────────────────┤
  │ zxid = (epoch, ctr)  │ (term, log index)        │
  │ 2-phase: propose+ack │ AppendEntries + commit   │
  │ Recovery: discovery + │ Recovery: leader sends   │
  │ sync + broadcast      │ missing entries          │
  │ Followers catch up via│ Followers catch up via   │
  │ SNAP + DIFF           │ snapshot + log replay    │
  └──────────────────────┴──────────────────────────┘
```

### etcd (Raft)

```
ETCD RAFT IMPLEMENTATION DETAILS

  LIBRARY: etcd uses the etcd/raft Go library
  DESIGN: Raft logic is a state machine (no I/O in raft library)
          Application (etcd) handles:
          - Network I/O (gRPC between nodes)
          - Disk I/O (WAL writes, snapshot storage)
          - State machine application (boltdb/bbolt)

  THIS IS UNUSUAL: Most Raft implementations bundle networking.
  etcd separates Raft logic from I/O for testability.

  ETCD PERFORMANCE CHARACTERISTICS:
  ┌─────────────────────────────┬──────────────────────────┐
  │ Metric                      │ Typical Value            │
  ├─────────────────────────────┼──────────────────────────┤
  │ Write latency (3-node)      │ 2-10ms (fsync bound)     │
  │ Read latency (leader)       │ <1ms (in-memory)         │
  │ Read latency (linearizable) │ 2-10ms (quorum read)     │
  │ Max key-value size           │ 1.5MB per value          │
  │ Max database size            │ 8GB recommended          │
  │ Max watchers                 │ ~10,000 per node         │
  │ Write throughput             │ ~10,000 writes/sec       │
  └─────────────────────────────┴──────────────────────────┘

  CRITICAL LESSON: etcd is a COORDINATION service, not a database.
  Do not store application data in etcd.
  Kubernetes control plane state: hundreds of MB, thousands of keys.
  Application data: terabytes, millions of keys → use a real database.
```

### CockroachDB (Raft + MVCC)

```
COCKROACHDB CONSENSUS ARCHITECTURE

  CockroachDB uses Raft PER RANGE (not one global Raft group).

  ┌──────────────────────────────────────────────────┐
  │                 TABLE DATA                       │
  │  key range [a, m)  │  key range [m, z)           │
  │  ┌──────────────┐  │  ┌──────────────┐           │
  │  │ Raft Group 1 │  │  │ Raft Group 2 │           │
  │  │ Leader: N1   │  │  │ Leader: N3   │           │
  │  │ Replicas:    │  │  │ Replicas:    │           │
  │  │  N1, N2, N3  │  │  │  N2, N3, N4  │           │
  │  └──────────────┘  │  └──────────────┘           │
  └──────────────────────────────────────────────────┘

  TRANSACTION PROTOCOL:
  1. Client starts txn → coordinator node
  2. Reads: MVCC reads at txn timestamp (no locks for reads)
  3. Writes: buffered at coordinator
  4. Commit: parallel Raft consensus on all affected ranges
     - Each range's Raft group independently replicates the write
     - Coordinator uses 2PC across ranges (Raft within each range)
  5. If any range rejects → abort → MVCC garbage collect

  SERIALIZABLE ISOLATION:
  CockroachDB achieves serializable isolation by:
  - MVCC: every value has a timestamp
  - Write intents: provisional writes visible to coordinator only
  - Read refreshes: if read timestamp advances, re-validate reads
  - Commit wait: bounded by clock uncertainty (not TrueTime)
```

### Google Spanner (TrueTime + Paxos)

```
SPANNER — THE TRUETIME APPROACH

  PROBLEM: Distributed transactions need globally ordered timestamps.
  SOLUTION: TrueTime — hardware-backed global time with bounded uncertainty.

  TRUETIME API:
    TT.now() → [earliest, latest]   ← interval, not point
    TT.after(t) → bool               ← is t definitely in the past?
    TT.before(t) → bool              ← is t definitely in the future?

  UNCERTAINTY BOUND (ε):
    GPS receivers + atomic clocks in every datacenter
    ε typically 1-7ms (average ~4ms)
    Compare to NTP: ~100ms uncertainty

  COMMIT PROTOCOL (externally consistent):
    1. Coordinator picks commit timestamp s
    2. s must be >= TT.now().latest at all participants
    3. Coordinator waits until TT.after(s) is true (commit-wait)
    4. THEN commits → guaranteed that s is in the past everywhere
    5. Any subsequent transaction gets timestamp s' > s

  THE COMMIT-WAIT TAX:
    Every write transaction waits ~2ε (7-14ms)
    This is the price of external consistency without lock contention
    Read-only transactions: NO wait (use consistent snapshot)

  SPANNER vs. COCKROACHDB:
  ┌──────────────────────────┬─────────────────────────────┐
  │ Spanner                  │ CockroachDB                 │
  ├──────────────────────────┼─────────────────────────────┤
  │ TrueTime (hardware)      │ HLC (Hybrid Logical Clocks) │
  │ ε ~ 4ms (GPS + atomic)  │ ε ~ 250-500ms (NTP)         │
  │ Commit-wait: ~7ms       │ Read-refresh / retry         │
  │ External consistency     │ Serializable (weaker)       │
  │ Google-only hardware     │ Commodity hardware           │
  └──────────────────────────┴─────────────────────────────┘

  CockroachDB cannot achieve Spanner's external consistency
  because NTP uncertainty is too large. Instead, it uses
  read-restarts: if clock skew is detected during a transaction,
  the transaction is transparently restarted at a higher timestamp.
```

---

## Part VI: The Consensus Landscape — Unified View

```
CONSENSUS PROTOCOLS — TAXONOMY

                    CRASH FAULT                    BYZANTINE FAULT
                    TOLERANT                       TOLERANT
                    (2f+1 nodes)                   (3f+1 nodes)
                    │                              │
        ┌───────────┼───────────┐       ┌──────────┼──────────┐
        │           │           │       │          │          │
    SINGLE-VALUE  REPLICATED   STATE   CLASSICAL  LINEAR    NAKAMOTO
                    LOG        MACHINE            (O(n))    (probab.)
        │           │           │       │          │          │
    ┌───┴───┐   ┌───┴───┐   ┌──┴──┐   ┌┴────┐  ┌─┴────┐   ┌┴───────┐
    │Paxos  │   │Multi- │   │Raft │   │PBFT │  │Hot-  │   │Nakamoto│
    │single │   │Paxos  │   │     │   │     │  │Stuff │   │(PoW)   │
    │decree │   │       │   │     │   │     │  │      │   │        │
    └───────┘   └───────┘   └─────┘   └─────┘  └──────┘   └────────┘
        │           │           │       │          │          │
    Academic    Chubby      etcd    Hyper-     Diem/      Bitcoin
    (1989)      (Google)    K8s     ledger     Aptos      Ethereum
                                    Cosmos               (pre-merge)

  PROPERTIES COMPARISON:
  ┌──────────────────┬─────────┬─────────┬─────────┬──────────┐
  │                  │ Paxos/  │ PBFT    │ HotStuff│ Nakamoto │
  │                  │ Raft    │         │         │          │
  ├──────────────────┼─────────┼─────────┼─────────┼──────────┤
  │ Fault model      │ Crash   │Byzantine│Byzantine│Byzantine │
  │ Nodes for f faults│ 2f+1  │ 3f+1   │ 3f+1   │ >50% hash│
  │ Msg complexity   │ O(n)   │ O(n²)  │ O(n)   │ O(n)     │
  │ Finality         │ 1 RTT  │ 3 RTT  │ 3 RTT  │ Probab.  │
  │ Deterministic    │ Yes    │ Yes    │ Yes    │ No       │
  │ Leader required  │ Yes*   │ Yes    │ Yes    │ No       │
  │ Throughput       │ High   │ Medium │ Medium │ Low      │
  │ Scalability      │ ~5-7   │ ~10-20 │ ~100+  │ ~1000s+  │
  └──────────────────┴─────────┴─────────┴─────────┴──────────┘
  * Paxos single-decree does not require a leader; Multi-Paxos does.
```

---

## Old World → New World Bridges

### For Any Senior Distributed Systems Engineer

| Old Concept | New Concept | Key Difference |
|-------------|-------------|----------------|
| 2PC (distributed transactions) | Consensus (replicated log) | 2PC decides commit/abort; consensus decides value. 2PC blocks on coordinator failure; consensus tolerates leader failure. |
| Primary-backup replication | Raft/Paxos leader-based replication | Primary-backup has no formal safety proof; Raft has provably correct leader election and log matching. |
| Manual failover (DBA promotes replica) | Automatic leader election | Consensus-based election guarantees no split-brain without human intervention. |
| NTP time synchronization | TrueTime / HLC | NTP gives a point estimate with ~100ms error. TrueTime gives an interval with ~4ms error. HLC combines logical and physical clocks. |
| Single-master SQL | Consensus-based NewSQL (CockroachDB, Spanner) | Same SQL interface; underneath is Raft/Paxos per shard with automatic failover. |

### For the Microsoft / Azure Background

| VSTS / Azure Concept | Distributed Systems Theory |
|----------------------|---------------------------|
| SQL Server Always On (synchronous commit) | Paxos-like quorum commit (2 of 3 replicas must ack) |
| Azure Service Fabric reliable services | Replicated state machine on top of Paxos-variant |
| CosmosDB 5 consistency levels | Direct exposure of the consistency hierarchy from `02-CONSISTENCY-MODELS.md` |
| Azure Event Hubs (Kafka-compatible) | Ordered log with consumer group consensus (ZAB-like internally) |
| DTC / System.Transactions | 2PC coordinator --- the blocking problem that consensus protocols solve for the control plane |

---

## Common Confusion Points

**"FLP means consensus is impossible"**
FLP says consensus is impossible *in a fully asynchronous system with crash faults*. Every practical system uses timeouts (partial synchrony), which makes consensus solvable. FLP tells you WHY your system needs timeouts, not that your system cannot work.

**"Byzantine fault tolerance is only for blockchain"**
BFT existed 17 years before Bitcoin. Any system where a compromised node could send conflicting messages needs BFT reasoning --- including security-critical infrastructure, aerospace systems, and multi-tenant cloud services where a compromised VM could corrupt shared metadata.

**"Paxos is obsolete because Raft exists"**
Paxos and Raft are equivalent in safety and liveness under the same model. Paxos allows more flexible configurations (e.g., non-voting learners, flexible quorums). Google still uses Paxos variants internally. Raft is preferred for new implementations because of its understandability, not because Paxos is wrong.

**"CAP says distributed databases must be inconsistent"**
CAP says you cannot have linearizability AND availability during a network partition. Most of the time, there is no partition, and you can have both. Systems like Spanner provide external consistency (stronger than linearizability) in the normal case, degrading to CP behavior only during actual partitions.

**"More replicas = more fault tolerance"**
More replicas increases the quorum size, which increases latency. 5 nodes (f=2) is the sweet spot for most production systems. 7 nodes (f=3) is unusual. 3 nodes (f=1) is common for non-critical coordination. Adding nodes beyond 7 rarely helps and always costs latency.

**"Raft leader is a single point of failure"**
The leader is a single point of *availability* for a bounded time (election timeout, typically <1 second). It is never a single point of *safety* --- committed data survives leader failure. The distinction between safety and liveness is fundamental: safety properties are never violated, even during leader failure. Only liveness (ability to make progress) is temporarily lost.

---

## Decision Cheat Sheet

| Situation | Protocol Family | Why |
|-----------|----------------|-----|
| Replicated log, crash faults only | Raft | Understandable, complete spec, excellent library support |
| Existing Google infrastructure | Multi-Paxos | Mature, deployed at Google scale for 20+ years |
| Untrusted participants (permissioned) | PBFT / Tendermint | BFT with deterministic finality, O(n^2) acceptable for small n |
| Untrusted participants (permissionless) | Nakamoto / Gasper | Scales to thousands of validators, probabilistic finality |
| High-throughput BFT (100+ validators) | HotStuff / DiemBFT | Linear message complexity, pipelined phases |
| Globally distributed SQL | Spanner (TrueTime) or CockroachDB (HLC) | External consistency (Spanner) or serializable (CRDB) |
| Kubernetes coordination | etcd (Raft) | Purpose-built for K8s; do not use for application data |
| Configuration/metadata store | ZooKeeper (ZAB) or etcd (Raft) | CP semantics, small data, coordination primitives |
| Formal verification required | TLA+ spec of Raft or Paxos | Raft's TLA+ spec is more complete; Paxos variants need custom specs |

---

## Further Reading — The Essential Papers

| Paper | Year | Pages | Key Contribution |
|-------|------|-------|-----------------|
| Lamport, "Time, Clocks, and the Ordering of Events" | 1978 | 11 | Happens-before, logical clocks |
| Fischer, Lynch, Paterson, "Impossibility of Distributed Consensus..." | 1985 | 7 | FLP impossibility |
| Lamport, "The Part-Time Parliament" (Paxos) | 1998 | 16 | Consensus algorithm |
| Dwork, Lynch, Stockmeyer, "Consensus in the Presence of Partial Synchrony" | 1988 | 32 | Partial synchrony model |
| Lamport, Shostak, Pease, "The Byzantine Generals Problem" | 1982 | 20 | BFT formulation and bound |
| Castro, Liskov, "Practical Byzantine Fault Tolerance" | 1999 | 14 | PBFT protocol |
| Gilbert, Lynch, "Brewer's Conjecture and the Feasibility of C, A, P..." | 2002 | 10 | CAP formal proof |
| Ongaro, Ousterhout, "In Search of an Understandable Consensus Algorithm" | 2014 | 18 | Raft |
| Yin et al., "HotStuff: BFT Consensus with Linearity and Responsiveness" | 2019 | 18 | Linear BFT |
| Corbett et al., "Spanner: Google's Globally-Distributed Database" | 2012 | 14 | TrueTime + Paxos |
