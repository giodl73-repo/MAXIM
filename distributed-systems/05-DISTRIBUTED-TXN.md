# Distributed Transactions: 2PC, Sagas, CRDTs, Conflict Resolution

## The Big Picture

Distributed transactions are the problem of executing operations across multiple nodes atomically — all succeed or all fail. The challenge: you cannot have both fault tolerance and synchronous coordination simultaneously.

```
DISTRIBUTED TRANSACTION PROBLEM SPACE
+---------------------------------------------------------------+
|                                                               |
|  REQUIREMENT: Atomic update across nodes A, B, C             |
|  CONSTRAINT: Any node can fail at any time                    |
|  CONSTRAINT: Network can partition at any time                |
|                                                               |
|  APPROACH          GUARANTEE           COST                   |
|  +---------------+ +-----------------+ +-------------------+  |
|  | 2PC           | | Atomic, but     | | Blocking on       |  |
|  | (coordinator) | | coordinator     | | coordinator       |  |
|  |               | | failure blocks  | | failure           |  |
|  +---------------+ +-----------------+ +-------------------+  |
|  | 3PC           | | Reduces          | | Still not         |  |
|  | (pre-commit)  | | blocking, not   | | partition-tolerant|  |
|  |               | | partition-safe  | |                   |  |
|  +---------------+ +-----------------+ +-------------------+  |
|  | Sagas         | | Eventually       | | Requires           |  |
|  | (compensating | | consistent,     | | compensating       |  |
|  | transactions) | | not isolated    | | transaction design |  |
|  +---------------+ +-----------------+ +-------------------+  |
|  | CRDTs         | | Always mergeable | | Limited to        |  |
|  | (conflict-free| | no coordination | | CRDT-shaped        |  |
|  | data types)   | | needed          | | data models        |  |
|  +---------------+ +-----------------+ +-------------------+  |
|  | Spanner       | | Externally       | | Requires           |  |
|  | TrueTime      | | consistent, full | | atomic clocks /    |  |
|  |               | | SQL transactions | | GPS hardware       |  |
|  +---------------+ +-----------------+ +-------------------+  |
+---------------------------------------------------------------+
```

---

## Two-Phase Commit (2PC)

The classic protocol for distributed atomic commit. Used inside databases; explicit in distributed middleware (DTC — Microsoft Distributed Transaction Coordinator, which you would know from ADO.NET `System.Transactions`).

### Protocol

```
PHASE 1: VOTING (Prepare)

Coordinator                    Participants
     |                         A    B    C
     |-- PREPARE -----------> [A]  [B]  [C]
     |
     |   Each participant:
     |   - Writes transaction to durable log
     |   - Locks all resources needed
     |   - Votes YES or NO
     |
     |<-- VOTE-YES/NO -------- [A]  [B]  [C]
     |   (must receive all YES to proceed)

PHASE 2: COMMIT (or Abort)

Coordinator                    Participants
     |   (if all YES)          A    B    C
     |-- COMMIT ------------> [A]  [B]  [C]
     |   (if any NO)
     |-- ABORT ------------->  [A]  [B]  [C]
     |
     |   Each participant:
     |   - Applies or rolls back
     |   - Releases locks
     |   - Sends ACK
     |
     |<-- ACK ---------------- [A]  [B]  [C]
     Transaction complete
```

### The Blocking Problem

```
COORDINATOR FAILURE SCENARIO

Phase 1 complete: all participants voted YES
Coordinator crashes BEFORE sending COMMIT/ABORT
                |
                v
Each participant is now STUCK:
  - Has locks held
  - Cannot commit (no COMMIT received)
  - Cannot abort (coordinator might be about to send COMMIT)
  - Must WAIT for coordinator to recover
  - Holds locks indefinitely → all other transactions blocked

This is the fundamental flaw of 2PC: it is not fault-tolerant.
In systems like MSDTC, coordinator failure required manual intervention
to resolve in-doubt transactions.
```

**ADO.NET System.Transactions bridge**: The `TransactionScope` class in .NET uses either a local transaction (fast, no 2PC) or MSDTC (slow, 2PC) depending on whether multiple connections enlist. You've seen this: the surprise escalation from local to distributed when a second connection is opened — this is 2PC kicking in.

```csharp
// This stays local (no 2PC):
using (var scope = new TransactionScope()) {
    // single connection ops
}

// This escalates to MSDTC (2PC):
using (var scope = new TransactionScope()) {
    using (var conn1 = new SqlConnection(cs1)) { ... }
    using (var conn2 = new SqlConnection(cs2)) { ... }  // ← escalation
}
```

### 3PC: Reducing Blocking

Three-phase commit adds a pre-commit phase to avoid the blocking problem:

```
PHASE 1: CanCommit (same as 2PC Prepare, but no locks yet)
PHASE 2: PreCommit (coordinator sends tentative commit; participants prepare locks)
PHASE 3: DoCommit (actual commit)

KEY ADDITION:
  If coordinator fails after PreCommit, participants can proceed
  by contacting each other (they know coordinator was going to commit)
  → no infinite blocking

LIMITATION:
  3PC assumes synchronous network (no partition)
  Under partition, 3PC can still violate atomicity
  → 3PC does not solve the fundamental problem, just reduces blocking
  → Not widely adopted in production systems
```

---

## The Saga Pattern

Sagas (Hector Garcia-Molina, 1987; rediscovered in microservices era ~2015) solve distributed transactions by decomposing them into a sequence of local transactions with compensating transactions for rollback.

### Structure

```
SAGA: Book travel (flight + hotel + car)

FORWARD PATH (all succeed):
  T1: Book flight    → success
  T2: Book hotel     → success
  T3: Book car       → success
  → DONE: Trip booked

COMPENSATING PATH (T3 fails):
  T1: Book flight    → success
  T2: Book hotel     → success
  T3: Book car       → FAIL
  C2: Cancel hotel   ← compensation for T2
  C1: Cancel flight  ← compensation for T1
  → DONE: Trip cancelled, all resources freed

EACH Ti has a corresponding Ci (compensating transaction)
  Ci undoes the semantic effect of Ti
  Ti and Ci are local transactions (no 2PC needed)
```

**Critical property**: Sagas provide ACD (Atomicity, Consistency, Durability) but NOT Isolation. Between T2 and C2, other users may see the booked hotel — temporary inconsistency is visible. This is the fundamental trade-off vs. 2PC.

### Orchestration vs. Choreography

```
ORCHESTRATION (central saga orchestrator)
  Orchestrator
      |
      | call T1 → await result
      | call T2 → await result
      | call T3 → FAIL
      | call C2 (compensate T2)
      | call C1 (compensate T1)

  + Clear single source of truth
  + Easier to monitor and debug
  - Orchestrator is a single point of coupling
  - Risk of "smart orchestrator" anti-pattern (put logic in services, not orchestrator)
  Used by: Azure Durable Functions, Camunda, Conductor

CHOREOGRAPHY (event-driven, no central orchestrator)
  Service A completes T1 → emits "flight-booked" event
  Service B listens → executes T2 → emits "hotel-booked" event
  Service C listens → tries T3 → FAIL → emits "car-booking-failed" event
  Service B listens to failure → executes C2 → emits "hotel-cancelled" event
  Service A listens → executes C1

  + No central coordinator
  + Services are more independent
  - Saga flow is implicit in event chains → hard to understand
  - Compensating logic is distributed across services
  Used by: Kafka-based microservices, EventBridge
```

---

## CRDTs: Conflict-Free Replicated Data Types

CRDTs are data structures designed so that any two replicas can be merged deterministically, without coordination, and the result is correct.

**Mathematical foundation**: The merge function must form a **join-semilattice** — there must be a least upper bound for any two states, and merge must be commutative, associative, and idempotent (CCI properties).

### CRDT Types

```
G-COUNTER (Grow-only counter)
  Each node has its own counter slot: [N1: 5, N2: 3, N3: 2]
  Increment: only increment your own slot
  Merge: take max of each slot across replicas
  Value: sum of all slots = 10
  GUARANTEE: Total count is eventually accurate; no coordination needed

PN-COUNTER (Positive-Negative counter, supports decrement)
  Two G-counters: P (increments) and N (decrements)
  Value = sum(P) - sum(N)
  Merge: merge P and N independently
  Used by: Riak counters, shopping cart total

OR-SET (Observed-Remove Set, supports add and remove)
  Problem with naive sets: concurrent add and remove is ambiguous
  OR-Set: each element tagged with unique ID on add
  Remove: marks the specific unique ID as removed
  Merge: union of all IDs, remove marked IDs
  Add-wins: concurrent add and remove → element is present
  Used by: collaborative document editors, shopping carts

LWW-REGISTER (Last-Write-Wins Register)
  Each write tagged with timestamp
  Merge: higher timestamp wins
  Problem: clock skew; tied timestamps need tiebreaker
  Used by: Cassandra cells (with caution)

SEQUENCE (for ordered lists / text)
  RGA, LSEQ, Logoot algorithms
  Each character assigned a globally unique position identifier
  Concurrent insertions always resolve to same order
  Used by: Google Docs (Operational Transform, not CRDT, but similar goal)
```

### CRDTs vs. 2PC

| Dimension | 2PC | CRDT |
|-----------|-----|------|
| Atomicity | Yes (all-or-nothing) | No (individual ops) |
| Isolation | Yes (locks during txn) | No (concurrent merges) |
| Coordination required | Yes (coordinator + participants) | No (commutative merge) |
| Available during partition | No (blocked) | Yes (operate independently, merge later) |
| Data model | Arbitrary SQL | CRDT-shaped (counters, sets, sequences) |
| Use case | Financial transactions | Counters, carts, collaborative docs |

---

## Google Spanner and TrueTime

Spanner (2012) achieves external consistency (strict serializability) globally without sacrificing availability by using hardware clocks with known uncertainty bounds.

### TrueTime API

```
TrueTime provides:
  TT.now() → interval [earliest, latest]
  (real time is guaranteed to be within this interval)
  Typical uncertainty: ε = 1–7ms (atomic clocks + GPS)

  TT.before(t) → true if t has definitely not arrived
  TT.after(t)  → true if t has definitely passed
```

### Commit Wait

```
EXTERNAL CONSISTENCY GUARANTEE
  Transaction T1 commits with timestamp s1
  Transaction T2 starts after T1 completes
  → s2 > s1 (guaranteed, despite clock skew)

HOW: Before returning commit to client for T1 at timestamp s1:
  WAIT until TT.after(s1) is guaranteed true
  (wait for the uncertainty window to pass)

  Commit wait ≈ 2ε ≈ 2–14ms per transaction
  This is the price of external consistency
```

### What Makes Spanner Unique

Without TrueTime (in systems like CockroachDB using hybrid logical clocks): the uncertainty bound is higher and commit wait is longer, or external consistency is approximated rather than guaranteed.

Without any commit wait (in systems like conventional distributed DBs): you can have transactions that read stale data even after a committed write, requiring snapshot-level isolation workarounds.

---

## When to Use Which Approach

| Scenario | Approach | Rationale |
|----------|----------|-----------|
| All resources in one SQL DB | Local ACID transaction | No distribution needed |
| Resources in one DB, multiple tables | Local ACID transaction | SQL handles this |
| Resources in two different DBs or services | Saga | 2PC is fragile across service boundaries |
| Counters that must not block | G-Counter CRDT | Coordination-free, AP |
| Shopping carts | OR-Set CRDT or Saga | Both work; CRDT is simpler |
| Financial ledger (debit/credit atomicity) | Saga with careful compensation | or: co-locate in one DB |
| Global SQL with external consistency | Spanner / CockroachDB | Hardware cost justified |
| Cross-microservice ordering workflow | Saga (orchestration) | Durable Functions, etc. |
| In-process coordination | 2PC (MSDTC) if you must | Avoid — migrate to Saga |

---

## Common Confusion Points

**"2PC is safe for microservices"**
2PC between microservices couples them through the coordinator. If the coordinator fails, both services are blocked. Sagas are the correct pattern for cross-service atomicity.

**"Sagas provide ACID"**
Sagas provide ACD but not I (Isolation). Other operations may see intermediate state during a saga. Design compensating transactions accordingly.

**"CRDTs solve everything"**
CRDTs solve a specific shape of problem: commutative, idempotent operations on mergeable data. They do not support arbitrary SQL semantics. A "transfer $100 from A to B" cannot be a CRDT because it requires reading A and B atomically.

**"Compensating transactions undo the original"**
Compensating transactions undo the semantic effect, not the operation. If T1 sent an email, C1 might send a cancellation email — you cannot unsend the original. Design for semantic reversibility, not operational undo.
