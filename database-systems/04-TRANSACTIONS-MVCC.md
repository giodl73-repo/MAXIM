---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:transactions-mvcc
kind: guide
module: database-systems
section: computing-software
title: Transactions and MVCC - ACID, 2PL, Snapshot Mechanics
status: source-custody
source_custody: partial
current_path: database-systems/04-TRANSACTIONS-MVCC.md
canonical_path: database-systems/04-TRANSACTIONS-MVCC.md
backsource_ids: [proof-backfill:database-systems:04-transactions-mvcc, git-history:database-systems:04-transactions-mvcc]
concepts: [transaction, ACID, MVCC, two-phase locking, snapshot isolation, version chain, concurrency control]
root_concepts: [concurrency control]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Transactions and MVCC — Letting Many Writers and Readers Coexist

A transaction is a unit of work that the database makes **atomic, consistent, isolated, and
durable** even while thousands of other transactions run concurrently. This guide covers the
*mechanisms* — ACID, two-phase locking, and especially multi-version concurrency control
(MVCC). Guide 05 then covers the *guarantees* (isolation levels) those mechanisms produce.

```
+=====================================================================================+
|                       CONCURRENCY CONTROL — THE TWO FAMILIES                         |
+=====================================================================================+
|                                                                                     |
|   GOAL: run T1, T2, ... T_n concurrently but produce a result EQUIVALENT to some     |
|         SERIAL order. (Serializability is the gold-standard correctness criterion.)  |
|                                                                                     |
|   +---------------------------------+     +-------------------------------------+   |
|   |  PESSIMISTIC: LOCK FIRST (2PL)  |     |  OPTIMISTIC: VERSION + DETECT (MVCC) |   |
|   +---------------------------------+     +-------------------------------------+   |
|   | acquire lock BEFORE touching a  |     | readers see a consistent SNAPSHOT;   |   |
|   | row. Conflicting txns BLOCK.    |     | writers create NEW versions; never   |   |
|   |                                 |     | block readers. Conflicts detected at |   |
|   | + simple correctness            |     | commit (abort the loser).            |   |
|   | - readers block writers,        |     | + reads never block / never blocked  |   |
|   |   writers block readers         |     | - storage for versions, GC/vacuum,   |   |
|   | - deadlocks                     |     |   write-skew anomaly at SI            |   |
|   +---------------------------------+     +-------------------------------------+   |
|                                                                                     |
|   MODERN REALITY: a HYBRID. MVCC for reads (no read locks) + locks or optimistic     |
|   detection for WRITE-WRITE conflicts. Postgres, Oracle, InnoDB, SQL Server RCSI/SI. |
+=====================================================================================+
```

The single most important sentence in this directory: **MVCC removes read locks but does not
remove the need to resolve write-write conflicts.** Everything below elaborates that.

---

## ACID — what the transaction promises

These are familiar; stated precisely because the rest builds on them.

| Property | Precise meaning | Implemented by |
|----------|-----------------|----------------|
| **Atomicity** | All-or-nothing: a transaction's effects are fully applied or fully absent. A crash/abort mid-way leaves no partial state. | WAL + undo (rollback), guide 06 |
| **Consistency** | A transaction moves the DB from one valid state to another, preserving declared invariants (constraints, FKs). *This C is the application's invariants, not the C in CAP.* | Constraints + the txn body |
| **Isolation** | Concurrent transactions don't see each other's uncommitted/intermediate state; the result is *as if* some serial order ran (at SERIALIZABLE). Weaker levels relax this. | 2PL or MVCC — this guide; guide 05 |
| **Durability** | Once COMMIT returns, the effects survive crashes. | WAL flush before COMMIT ack, guide 06 |

> Note the two different C's: ACID's *Consistency* = application invariants hold. CAP's
> *Consistency* (guide 09, `distributed-systems/`) = every read sees the latest write
> (linearizability). They are unrelated despite the shared letter. Do not conflate them.

---

## Pessimistic Concurrency: Two-Phase Locking (2PL)

2PL is the classic locking protocol that **guarantees serializability**. The rule is about the
*shape* of lock acquisition over time, not about two commits.

```
   TWO PHASES of a transaction's lock set:

   locks
   held    GROWING PHASE         SHRINKING PHASE
     |     (acquire only)        (release only)
     |          ____________________
     |         /                    \
     |        /                      \
     |       /                        \
     |______/                          \________
            t0                  (peak)          commit
            |                                     |
   RULE: once you RELEASE any lock, you may NEVER acquire another.
   => guarantees a serializable schedule.

   STRICT 2PL (what real systems use): hold ALL locks until COMMIT/ABORT, then release together.
   => also guarantees recoverability (no cascading aborts).
```

Lock modes and the conflict matrix:

```
            held: NONE   SHARED(read)   EXCLUSIVE(write)
   want:
   SHARED        ok          ok              BLOCK
   EXCLUSIVE     ok         BLOCK            BLOCK

   => readers (S) share; a writer (X) excludes everyone. In PURE 2PL a long read blocks writers
      and a writer blocks readers. This is why classic locking databases have "blocking" pain.
```

**Deadlock** is intrinsic to locking: T1 holds A waits B; T2 holds B waits A. Databases detect
it (a wait-for graph cycle) and **abort a victim**, or use timeouts. This is normal, not a bug —
the loser retries.

> Bridge: classic SQL Server (READ COMMITTED *without* RCSI) uses this locking model — your
> "blocking chains" and deadlock victims come straight from 2PL. Turning on Read Committed
> Snapshot Isolation (RCSI) switches reads to MVCC and eliminates the reader/writer blocking.

---

## Optimistic Concurrency: MVCC mechanics

MVCC keeps **multiple versions of each row**. A write doesn't overwrite — it creates a new
version stamped with the writing transaction's id. A reader sees the version that was committed
as of *its* snapshot, ignoring anything newer. Readers therefore never block and are never
blocked.

```
   VERSION CHAIN for one logical row (key = 42), newest first:

   +----------------------------------------------------------------------------------+
   | v3  value=300  created_by=T9 (uncommitted)   ----.                               |
   | v2  value=200  created_by=T7 (committed)      <--+-- a reader at snapshot S sees  |
   | v1  value=100  created_by=T3 (committed)          |   the NEWEST version COMMITTED |
   +---------------------------------------------------+   and <= S; ignores v3, v2 if  |
                                                          they're newer than S.         |
   VISIBILITY RULE (essence): a version is visible to txn T iff
     - it was created by a transaction that COMMITTED before T's snapshot, AND
     - it was not superseded by another such committed version, AND
     - it was not deleted by a transaction committed before T's snapshot.
```

How two real engines implement the version chain (both correct, different mechanics):

```
   POSTGRES — versions live IN the heap                ORACLE / SQL SERVER — versions in a
   --------------------------------------              separate area
   Each tuple has xmin (creating txn) and xmax         Oracle: UNDO segments hold prior images;
   (deleting/superseding txn). An UPDATE writes a       a read reconstructs the old version by
   NEW tuple and sets the old tuple's xmax. Old         applying undo. SQL Server RCSI/SI: the
   versions accumulate in the table -> VACUUM           VERSION STORE in tempdb holds prior
   reclaims dead tuples. Visibility checked via         row versions, pointed to by a 14-byte
   xmin/xmax against the txn's snapshot.                versioning tag on the row.
```

The cost of MVCC is **garbage**: old versions must be cleaned up. Postgres's autovacuum, Oracle's
undo retention, and SQL Server's version-store cleanup all exist to reclaim space and prevent
bloat. A long-running read transaction holds back cleanup (it might still need old versions) —
the classic "long transaction bloats the table / fills the version store" operational hazard.

---

## Snapshot Isolation (SI) — the mechanism MVCC most naturally provides

When a transaction starts (or at its first statement, depending on the level), it takes a
**snapshot**: a consistent point-in-time view. Every read in the transaction sees that snapshot,
regardless of concurrent commits. This is **snapshot isolation**.

```
   SNAPSHOT ISOLATION timeline

   T1: --[snapshot @ s1]------------ reads x (sees value @ s1) ------- reads x (STILL @ s1) --commit
   T2:           --------- writes x, COMMITS ------------------^
                                                   T1 never sees T2's write -> repeatable, no
                                                   non-repeatable read, no phantom for T1's reads.

   WRITE-WRITE rule under SI: "FIRST COMMITTER WINS."
   If two txns both update the same row from the same snapshot, the first to commit succeeds;
   the second gets a serialization/write-conflict error and must retry (or, with locking, blocks).
```

What SI gives you (precise — guide 05 expands the full table):

| Anomaly | Prevented by SI? |
|---------|------------------|
| Dirty read | YES — you only see committed versions |
| Non-repeatable read | YES — your snapshot is stable |
| Phantom read | YES — new rows committed after your snapshot are invisible to you |
| Lost update (same row) | YES — first-committer-wins aborts the second writer |
| **Write skew** | **NO** — SI does NOT prevent it (see below) |

### Write skew — the anomaly SI does NOT prevent (the famous gap)

This is the precision point that trips up most engineers. **Snapshot isolation prevents the
single-object anomalies but allows write skew**, where two transactions read an overlapping set,
each makes a decision based on that read, and write to *different* rows — so first-committer-wins
never fires, yet the combined result violates an invariant.

```
   CLASSIC: two on-call doctors, invariant "at least one must remain on call."
   Both rows currently "on call". Both doctors try to go off call simultaneously.

   snapshot @ s: {Alice=on, Bob=on}
   T1 (Alice): reads "Bob is on, so I may go off" -> sets Alice = off
   T2 (Bob):   reads "Alice is on, so I may go off" -> sets Bob = off

   Different rows updated -> NO write-write conflict -> BOTH COMMIT under SI.
   Result: nobody on call. Invariant violated. This is WRITE SKEW.
```

To prevent write skew you need **Serializable Snapshot Isolation (SSI)** (Cahill/Fekete, used by
PostgreSQL's `SERIALIZABLE` since 9.1) or explicit locking (`SELECT ... FOR UPDATE` to
materialize the conflict, or `SERIALIZABLE` via 2PL). Plain SI — Oracle's `SERIALIZABLE`, SQL
Server's `SNAPSHOT`, and most engines' snapshot mode — does not. Guide 05 is the full treatment.

---

## How the families combine in real engines

```
   ENGINE              READS                 WRITE-WRITE conflicts
   ----------------    ------------------    ---------------------------------
   PostgreSQL          MVCC snapshot         row locks on UPDATE; SERIALIZABLE adds SSI
   Oracle              MVCC (undo)           row locks; "SERIALIZABLE" = SI (no SSI)
   MySQL/InnoDB        MVCC snapshot         row + GAP locks (Repeatable Read default)
   SQL Server (default)2PL locking reads     2PL write locks (blocking, deadlocks)
   SQL Server RCSI     MVCC (version store)  2PL write locks
   SQL Server SNAPSHOT MVCC snapshot         optimistic; first-committer-wins (5xxx error)
   SQLite              coarse db/page locks   single-writer (WAL mode allows readers + 1 writer)
```

> InnoDB's **gap locks** are why its Repeatable Read prevents phantoms that plain SI elsewhere
> would too — InnoDB locks the *gaps* between index keys so no one can insert a phantom into the
> range your `SELECT` scanned. This is a real, distinguishing detail (guide 05).

---

## Old World → New World Bridges

| You already know | Concurrency concept | SQL Server / Azure anchor |
|------------------|---------------------|----------------------------|
| Pessimistic vs optimistic locking | 2PL (lock first) vs MVCC (version + detect) | RCSI/SNAPSHOT vs default locking |
| A `rowversion`/`timestamp` column you check before update | Optimistic concurrency = a hand-rolled MVCC for one row | `rowversion`, `WHERE rowver = @old` |
| A `lock` statement / mutex | Exclusive (X) lock in 2PL | `UPDLOCK`, `HOLDLOCK` hints |
| Detecting a cycle in a wait graph | **Deadlock detection** → abort victim | Deadlock graph, victim selection |
| Garbage collection of old objects | MVCC version cleanup | autovacuum (PG); version store cleanup |
| "First write wins" optimistic concurrency in app code | SI **first-committer-wins** | SNAPSHOT isolation conflict (error 3960) |

---

## Decision Cheat Sheet

| Situation | Mechanism / setting |
|-----------|---------------------|
| Want readers to never block writers | MVCC — Postgres default, SQL Server RCSI, Oracle |
| Need a stable point-in-time view for a long report | SNAPSHOT / repeatable read on MVCC |
| Two txns racing to update the SAME row | Lost update prevented by first-committer-wins or row lock |
| Two txns reading an overlap, writing DIFFERENT rows, must keep an invariant | **Write skew risk** → need SERIALIZABLE (SSI) or explicit lock |
| Classic SQL Server blocking/deadlock pain | Turn on **RCSI** to move reads to MVCC |
| Bloat / table growth / tempdb pressure | MVCC version cleanup — kill long-running transactions; tune autovacuum |
| Absolute correctness, accept some aborts | SERIALIZABLE (SSI in Postgres, or 2PL serializable) — guide 05 |

---

## Common Confusion Points

### "MVCC means lock-free"

MVCC means **read-lock-free**. Two transactions writing the *same* row still conflict — resolved
by a row lock (Postgres/InnoDB) or by abort at commit (SI first-committer-wins). And SI does
*not* prevent write skew across *different* rows. "Lock-free reads," not "lock-free everything."

### "Snapshot isolation is serializable"

It is **not**. SI prevents dirty reads, non-repeatable reads, phantoms, and lost updates, but
**allows write skew** (and read-only anomalies). Oracle's and SQL Server's snapshot levels named
or marketed near "serializable" are SI. Only **SSI** (PostgreSQL `SERIALIZABLE`) or 2PL
serializable are truly serializable. Guide 05 nails the distinctions.

### "Two-phase locking is the same as two-phase commit"

Completely different. **2PL** (this guide) is a *concurrency* protocol about lock acquire/release
shape within one node. **2PC** (guide 08) is an *atomic commit* protocol across multiple nodes.
Same "two-phase" name, unrelated problems.

### "Longer transactions are just slower"

Under MVCC they are *operationally dangerous*: a long read holds back version cleanup
(vacuum/undo/version store) for the whole database, causing bloat and tempdb pressure far beyond
the one transaction. Keep transactions short — this is an MVCC-specific hazard, not generic
advice.

### "Read Committed gives me a consistent snapshot"

Not for the whole transaction. Under Read Committed (the Postgres / SQL Server / Oracle default),
each *statement* gets a fresh snapshot, so two SELECTs in one transaction can see different data
(a non-repeatable read). You need REPEATABLE READ / SNAPSHOT for a transaction-stable view.
Guide 05 details exactly which level gives what.
