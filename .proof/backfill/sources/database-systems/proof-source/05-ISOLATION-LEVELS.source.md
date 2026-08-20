---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-ISOLATION-LEVELS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:isolation-levels
kind: guide
module: database-systems
section: computing-software
title: Isolation Levels - The Four Levels, Their Anomalies, SSI
status: source-custody
source_custody: partial
current_path: database-systems/05-ISOLATION-LEVELS.md
canonical_path: database-systems/05-ISOLATION-LEVELS.md
backsource_ids: [proof-backfill:database-systems:05-isolation-levels, git-history:database-systems:05-isolation-levels]
concepts: [isolation level, read uncommitted, read committed, repeatable read, serializable, snapshot isolation, write skew, phantom, SSI]
root_concepts: [isolation level]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Isolation Levels — Exactly What Each One Guarantees

Isolation levels are the **contract** the database offers about what concurrent transactions may
observe of each other. This is the most error-prone topic in databases because the SQL standard's
levels are defined by *which anomalies they forbid*, and real engines implement them with
different mechanisms (locking vs MVCC) that prevent *different additional* anomalies. This guide
states each guarantee precisely, because this is exactly where imprecise mental models cause
production bugs.

```
+=====================================================================================+
|              ISOLATION = "WHICH ANOMALIES CAN I SEE?"  (weaker -> stronger)          |
+=====================================================================================+
|                                                                                     |
|  READ UNCOMMITTED   READ COMMITTED   REPEATABLE READ   SNAPSHOT       SERIALIZABLE   |
|       |                  |                |              |                 |          |
|       v                  v                v              v                 v          |
|  +----------+      +-----------+    +-----------+   +----------+    +-------------+   |
|  | sees     |      | sees only |    | stable    |   | full     |    | TRUE serial |   |
|  | UNCOMMIT |      | committed |    | re-reads  |   | snapshot |    | equivalence |   |
|  | dirty    |      | per stmt  |    | of read   |   | (SI):    |    | no write    |   |
|  | data     |      |           |    | rows      |   | no       |    | skew,       |   |
|  |          |      |           |    |           |   | phantom  |    | no anomaly  |   |
|  +----------+      +-----------+    +-----------+   +----------+    +-------------+   |
|  allows:           allows:          allows (std):   allows:         allows:          |
|   dirty read        non-repeat       phantom         WRITE SKEW      NOTHING          |
|   non-repeat        phantom          (lost upd in    + read-only                     |
|   phantom           write skew        std model)      anomaly                        |
|   ...                                                                                |
+=====================================================================================+
   NOTE: SNAPSHOT (SI) is NOT one of the 4 ANSI SQL levels — it is a separate, widely
   implemented level that sits "beside" REPEATABLE READ. It is the source of most confusion.
```

---

## The anomalies — define them precisely first

You cannot reason about levels without crisp anomaly definitions. The first three are the ANSI
SQL-92 anomalies; the rest come from Berenson et al. (1995, "A Critique of ANSI SQL Isolation
Levels"), the paper that exposed the standard's gaps.

| Anomaly | Definition | Example |
|---------|------------|---------|
| **Dirty read (P1)** | T2 reads a row written by T1 *before* T1 commits; T1 may roll back | Read a balance from an uncommitted, later-aborted transfer |
| **Non-repeatable read (P2)** | T1 reads a row, T2 updates+commits it, T1 re-reads and sees a *different value* | Two reads of the same account differ within one transaction |
| **Phantom (P3)** | T1 runs a predicate query, T2 inserts/deletes a row matching that predicate+commits, T1 re-runs and the *set of rows changes* | `COUNT(*) WHERE region='EU'` changes between two reads |
| **Lost update (P4)** | T1 and T2 both read a value, both update based on it; one update overwrites the other | Two `balance = balance - 10` racing, only one decrement survives |
| **Read skew (A5A)** | T1 reads x, T2 updates x and a related y, T1 reads y — sees an inconsistent x/y pair | Read account A before transfer, account B after |
| **Write skew (A5B)** | T1 and T2 read an overlapping set, each writes a *different* row; combined result breaks an invariant no single transaction broke | The two-doctors-off-call example (guide 04) |

```
   PHANTOM vs NON-REPEATABLE READ — the distinction people miss:

   NON-REPEATABLE: an EXISTING row you read CHANGES value when re-read.   (about a row)
   PHANTOM:        the SET of rows matching a PREDICATE changes (new rows  (about a predicate /
                   appear / disappear) when the predicate is re-run.        a range of rows)
```

---

## The canonical guarantee table (ANSI definition)

By the **ANSI/SQL-92 definition** (anomaly-prevention), the four standard levels forbid:

| Level | Dirty read | Non-repeatable read | Phantom |
|-------|:----------:|:-------------------:|:-------:|
| READ UNCOMMITTED | allowed | allowed | allowed |
| READ COMMITTED | **prevented** | allowed | allowed |
| REPEATABLE READ | **prevented** | **prevented** | allowed |
| SERIALIZABLE | **prevented** | **prevented** | **prevented** |

This is the table everyone memorizes. The Berenson critique's point: it is **underspecified** —
it says nothing about lost update or write skew, and real engines using MVCC behave differently
from the lock-based model the standard implicitly assumed. The next sections give the *real*
behavior of real engines.

---

## Level by level — real engine behavior

### READ UNCOMMITTED

Reads may see **uncommitted** ("dirty") data that might be rolled back. In MVCC engines this
level is often meaningless or unsupported because there's no cheap way to read a dirty version
(Postgres treats READ UNCOMMITTED as READ COMMITTED). In SQL Server, `READ UNCOMMITTED` (the
infamous `WITH (NOLOCK)`) skips shared locks → fast but can read dirty data, miss rows, or read
rows twice during page splits. Use only for rough monitoring counts.

### READ COMMITTED — the default almost everywhere

You only ever read **committed** data, but the read snapshot is taken **per statement**, not per
transaction. So within one transaction, two identical SELECTs can return different results
(non-repeatable read) and different row sets (phantom). This is the default in **PostgreSQL,
Oracle, and SQL Server**.

```
   READ COMMITTED, MVCC flavor (Postgres / Oracle / SQL Server RCSI):
   each STATEMENT gets a fresh snapshot of committed data; readers never block.

   READ COMMITTED, lock flavor (classic SQL Server):
   short shared locks held only during the read, released immediately -> readers block writers
   briefly; this is where blocking comes from.
```

### REPEATABLE READ — and the engine divergence

Standard guarantee: re-reading a *row* you already read gives the same value (no non-repeatable
read). Standard *allows* phantoms. **But real engines diverge sharply:**

```
   PostgreSQL REPEATABLE READ  == SNAPSHOT ISOLATION (a transaction-wide snapshot).
        => prevents non-repeatable reads AND phantoms (snapshot hides new rows),
           but ALLOWS write skew. (PG's RR is stronger than the ANSI minimum.)

   MySQL/InnoDB REPEATABLE READ (the default) uses MVCC snapshot for plain reads AND
        GAP LOCKS / next-key locks for locking reads, which prevents phantoms in the
        ranges it locks. Plain SELECT sees a stable snapshot. (Stronger than ANSI RR.)
        Still allows write skew on non-locked reads.

   SQL Server REPEATABLE READ (lock-based) holds SHARED locks on read rows until commit,
        preventing non-repeatable reads but NOT phantoms (no range locks) -> matches ANSI.
```

The lesson: "REPEATABLE READ" names different real behaviors across engines. Know your engine.

### SNAPSHOT ISOLATION (SI) — the separate level

Not in the ANSI four. The transaction takes one **consistent snapshot** at start; all reads see
it. Writers use **first-committer-wins**. SI prevents dirty reads, non-repeatable reads,
phantoms, and lost updates — but **allows write skew and the read-only anomaly.**

```
   SI guarantee set (PRECISE):
     dirty read .............. prevented
     non-repeatable read ..... prevented
     phantom ................. prevented (new rows are not in your snapshot)
     lost update ............. prevented (first-committer-wins)
     WRITE SKEW .............. ALLOWED   <-- the defining gap
     read-only anomaly ....... ALLOWED   (a read-only txn can observe a non-serializable state)
```

Implemented as: PostgreSQL `REPEATABLE READ`; Oracle `SERIALIZABLE` (yes — Oracle's
SERIALIZABLE is actually SI and permits write skew); SQL Server `SNAPSHOT`; Cosmos DB's
session/bounded-staleness sit in a different (distributed) consistency framework (guide 09).

### SERIALIZABLE — the only fully safe level

Guarantees the result is **equivalent to some serial execution** of the transactions — *no*
anomaly of any kind, including write skew. Two ways to implement it:

```
   (A) LOCK-BASED SERIALIZABLE (Strict 2PL + range/predicate locks)
       - shared locks held to commit + locks on the GAPS/ranges a predicate scanned
       - prevents phantoms by locking the range so no phantom can be inserted
       - SQL Server SERIALIZABLE; DB2. Cost: blocking, deadlocks, low concurrency.

   (B) SERIALIZABLE SNAPSHOT ISOLATION (SSI)  [Cahill, Fekete, Roehm 2008]
       - runs on top of SI (no read locks, full concurrency) PLUS tracks read/write
         DEPENDENCIES between concurrent transactions; detects "dangerous structures"
         (rw-antidependency cycles) and ABORTS one transaction to break the cycle.
       - prevents write skew that plain SI allows, at the cost of some false-positive aborts.
       - PostgreSQL SERIALIZABLE (since 9.1) is SSI. CockroachDB is serializable by default.
```

> The clean statement: **plain SI prevents everything except write skew; SSI adds write-skew
> prevention by aborting transactions involved in a dangerous read-write dependency cycle.**
> SSI gives serializable correctness with SI-like concurrency, paying in occasional retries.

---

## The master comparison table (real-engine semantics)

```
  ANOMALY        | READ      | READ      | REPEATABLE | SNAPSHOT  | SERIALIZABLE
                 | UNCOMMIT  | COMMITTED | READ (std) | ISOLATION | (incl. SSI)
  ---------------+-----------+-----------+------------+-----------+-------------
  dirty read     | ALLOWED   | prevented | prevented  | prevented | prevented
  non-repeatable | ALLOWED   | ALLOWED   | prevented  | prevented | prevented
  phantom        | ALLOWED   | ALLOWED   | ALLOWED*   | prevented | prevented
  lost update    | ALLOWED   | ALLOWED** | prevented  | prevented | prevented
  WRITE SKEW     | ALLOWED   | ALLOWED   | ALLOWED    | ALLOWED   | PREVENTED
  ---------------+-----------+-----------+------------+-----------+-------------
  * ANSI allows phantoms at RR; Postgres RR (=SI) and InnoDB RR (gap locks) prevent them.
  ** Read Committed allows lost update unless you use SELECT ... FOR UPDATE / atomic UPDATE.
```

The single most important row is **WRITE SKEW**: only SERIALIZABLE prevents it. If your
correctness depends on a multi-row invariant ("at least one X must remain true," "sum must stay
non-negative across rows," booking the last seat), snapshot isolation is *not enough*.

---

## Choosing and defending against anomalies

```
   You have a multi-row invariant -> SERIALIZABLE, or materialize the conflict:
        SELECT ... FOR UPDATE     (lock the rows you read so the conflict becomes write-write)
        SELECT ... FOR SHARE      (block conflicting writers)
        a sentinel/lock row both txns must update (forces first-committer-wins to fire)

   You only race on one row (lost update) -> use an atomic UPDATE, or SNAPSHOT/SERIALIZABLE,
        or optimistic rowversion check.

   You need a stable report over many tables -> SNAPSHOT / REPEATABLE READ.

   You just need committed data, max concurrency -> READ COMMITTED (the default; usually right).
```

---

## Old World → New World Bridges

| You already know | Isolation concept | SQL Server / Azure anchor |
|------------------|-------------------|----------------------------|
| `WITH (NOLOCK)` for fast dirty reads | READ UNCOMMITTED (its hazards) | `NOLOCK`, READ UNCOMMITTED |
| The default that "just reads committed rows" | READ COMMITTED (per-statement snapshot) | Default level; RCSI variant |
| Optimistic concurrency with `rowversion` | Lost-update prevention | `WHERE rowver=@old`, SNAPSHOT |
| SERIALIZABLE causing blocking/deadlocks | Lock-based serializable + range locks | SQL Server SERIALIZABLE |
| "Snapshot gives me a consistent read view" | SNAPSHOT ISOLATION (and its write-skew gap) | `SET TRANSACTION ISOLATION LEVEL SNAPSHOT` |
| Cross-region "strong vs eventual" knobs | Distributed consistency (different axis) | Cosmos consistency levels (guide 09) |

---

## Decision Cheat Sheet

| I need... | Use |
|-----------|-----|
| Maximum throughput, only committed data | **READ COMMITTED** (the default) |
| Stable re-reads of the same rows in a txn | **REPEATABLE READ** (know your engine's exact semantics) |
| A consistent point-in-time view across tables, non-blocking | **SNAPSHOT** (SI) |
| Protection against a multi-row invariant violation (write skew) | **SERIALIZABLE** (SSI in Postgres/Cockroach) |
| Prevent a lost update on a single row | atomic `UPDATE`, `SELECT ... FOR UPDATE`, or SNAPSHOT+ |
| Prevent phantoms specifically | SNAPSHOT, SERIALIZABLE, or InnoDB RR (gap locks) |
| Eliminate SQL Server reader/writer blocking | turn on **RCSI** (moves reads to MVCC) |

---

## Common Confusion Points

### "REPEATABLE READ prevents phantoms"

By the **ANSI standard it does not** — phantoms are explicitly allowed at REPEATABLE READ. But
**PostgreSQL's** REPEATABLE READ is actually snapshot isolation and *does* prevent phantoms, and
**InnoDB's** uses gap locks and prevents them in locked ranges. SQL Server's lock-based
REPEATABLE READ does *not*. The name promises less than some engines deliver — always check the
engine.

### "SNAPSHOT isolation is the same as SERIALIZABLE"

No — and this is the trap. SI permits **write skew** and the read-only anomaly; SERIALIZABLE does
not. Oracle's `SERIALIZABLE` keyword is in fact SI (so Oracle "serializable" allows write skew).
PostgreSQL's `SERIALIZABLE` is real SSI and prevents it. Same word, different guarantee.

### "Higher isolation is always safer, so just use SERIALIZABLE"

Correctness-wise yes; operationally it costs concurrency. Lock-based SERIALIZABLE causes blocking
and deadlocks; SSI causes transaction **aborts** (serialization failures) you must catch and
**retry**. Code that runs at SERIALIZABLE must have retry loops. Most workloads use READ
COMMITTED and only escalate the specific transactions with multi-row invariants.

### "Read Committed prevents lost updates"

It does not, by itself. Two transactions doing read-modify-write on the same row at READ
COMMITTED can lose an update. Prevent it with an atomic single-statement `UPDATE`, `SELECT ...
FOR UPDATE`, an optimistic rowversion check, or a higher isolation level.

### "These levels also describe distributed consistency"

Different axis. Isolation levels are about *concurrent transactions on one logical database*.
Distributed **consistency** models (linearizability, causal, eventual; Cosmos's five levels) are
about *what a read sees across replicas/regions* (guide 09, `distributed-systems/02`). A system
can be SERIALIZABLE locally yet eventually consistent across regions, or vice versa.
