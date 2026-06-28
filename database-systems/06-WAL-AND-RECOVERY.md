---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:wal-and-recovery
kind: guide
module: database-systems
section: computing-software
title: WAL and Recovery - Write-Ahead Logging, ARIES, Checkpoints
status: source-custody
source_custody: partial
current_path: database-systems/06-WAL-AND-RECOVERY.md
canonical_path: database-systems/06-WAL-AND-RECOVERY.md
backsource_ids: [proof-backfill:database-systems:06-wal-and-recovery, git-history:database-systems:06-wal-and-recovery]
concepts: [write-ahead logging, WAL, ARIES, checkpoint, crash recovery, redo, undo, durability]
root_concepts: [write-ahead logging]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# WAL and Recovery — Making "Durable" True Across a Crash

The "D" in ACID — durability — is the promise that once `COMMIT` returns, your data survives a
power loss. The mechanism that delivers it, and also delivers atomic rollback, is **write-ahead
logging (WAL)**. This guide covers the WAL, the **ARIES** recovery algorithm that virtually every
relational engine descends from, checkpoints, and exactly what happens when the machine reboots
after a crash.

```
+=====================================================================================+
|                  WHY THE WAL EXISTS: THE FUNDAMENTAL PROBLEM                         |
+=====================================================================================+
|                                                                                     |
|   A COMMIT must be durable INSTANTLY, but flushing the actual modified PAGES to      |
|   their home locations is SLOW and RANDOM (scattered across the file).              |
|                                                                                     |
|   SOLUTION: don't flush the pages at commit. Flush a small, SEQUENTIAL LOG of what   |
|   changed. The log is the source of truth; pages catch up lazily.                   |
|                                                                                     |
|        +-------------+        append-only, SEQUENTIAL writes (fast on any media)     |
|        |    WAL      |  <-----  log record per change: "page P, before X, after Y"   |
|        +-------------+                                                               |
|              |  (fsync'd before COMMIT returns)                                      |
|              v                                                                       |
|        +-------------+        random writes, deferred to checkpoint / lazy writer    |
|        | DATA PAGES  |  <-----  the buffer pool flushes dirty pages LATER            |
|        +-------------+                                                               |
|                                                                                     |
|   THE TWO RULES (the WAL protocol):                                                  |
|   1. WAL rule:   the log record for a change must hit stable storage BEFORE the      |
|                  data page is written to its home location.                          |
|   2. Commit rule:the COMMIT log record must be durable BEFORE COMMIT is acknowledged.|
+=====================================================================================+
```

Bridge: this is the SQL Server transaction log (`.ldf`) and the Postgres WAL — same artifact.
Your `WRITELOG` waits are COMMIT blocking on rule 2 (the log fsync). The data file (`.mdf`) lags
behind the log on purpose; that lag is normal and is what makes commits fast.

---

## The Log Record and the LSN

```
   Every log record carries a LOG SEQUENCE NUMBER (LSN) — a monotonically increasing id
   (usually the byte offset in the log). LSNs order all changes in the system.

   A typical UPDATE log record (ARIES-style):
   +-------+--------+--------+---------+------------+-----------------+-------------+
   | LSN   | TxnID  | type   | pageID  | prevLSN    | BEFORE image    | AFTER image |
   +-------+--------+--------+---------+------------+-----------------+-------------+
        |                                   |             |                 |
        |                                   |             |                 +-- for REDO
        |                                   |             +-------------------- for UNDO
        |                                   +---------------------------------- back-link to
        |                                                                       this txn's
        |                                                                       previous record
        +----- orders all changes globally; each DATA PAGE stores the LSN of the last log
               record applied to it (pageLSN) so recovery knows if a change is already there.
```

Two images per record is what lets ARIES do both jobs:
- **REDO** uses the AFTER image to re-apply committed changes the crash lost.
- **UNDO** uses the BEFORE image to roll back uncommitted changes the crash left behind.

The **pageLSN** stored on each data page is the keystone: during recovery, compare the log
record's LSN to the page's pageLSN to decide "is this change already reflected on this page?"
This makes redo **idempotent** — you can replay the log safely even if some changes already made
it to disk before the crash.

---

## ARIES — the recovery algorithm everything descends from

ARIES (Algorithms for Recovery and Isolation Exploiting Semantics; Mohan et al., IBM, 1992) is
*the* reference crash-recovery algorithm. SQL Server, DB2, and the broad lineage of relational
engines implement ARIES or close variants. Its three governing principles:

```
   1. WRITE-AHEAD LOGGING        log the change before the page is overwritten on disk.
   2. REPEATING HISTORY ON REDO  on restart, REDO ALL changes (even uncommitted ones) to
                                 reconstruct the EXACT state at the moment of the crash...
   3. LOGGING CHANGES DURING UNDO ...then UNDO the uncommitted ones, and LOG those undo
                                 actions too (as "compensation log records") so a crash
                                 DURING recovery is itself recoverable.
```

Recovery runs in **three passes** over the log:

```
   +-----------+   +-----------+   +-----------+
   |  ANALYSIS |-->|   REDO    |-->|   UNDO    |
   +-----------+   +-----------+   +-----------+

   1) ANALYSIS  start from the last checkpoint. Scan forward. Rebuild:
        - the TRANSACTION TABLE  (which txns were in-flight, and were they committed?)
        - the DIRTY PAGE TABLE   (which pages were dirty, and from which LSN onward)
      Determines where REDO must start (the oldest recLSN in the dirty page table).

   2) REDO  "repeat history." Replay log forward from that start point, re-applying EVERY
        logged change whose effect isn't already on the page (pageLSN < record LSN),
        regardless of whether its transaction committed. State now == moment of crash.

   3) UNDO  roll back every transaction that was IN-FLIGHT (not committed) at crash time,
        applying BEFORE images in reverse, writing COMPENSATION LOG RECORDS (CLRs) so the
        undo work is itself durable and idempotent if recovery crashes again.
```

The counterintuitive genius is pass 2: **redo replays even uncommitted transactions**, exactly
reconstructing the pre-crash state, and only *then* does pass 3 cleanly undo the losers. This
"repeat history" design is what makes ARIES robust to crashes during recovery.

```
   TIMELINE OF A CRASH

   ----[checkpoint]----[T1 commits]----[T2 still running]----X CRASH----reboot----
                                                              |
       ANALYSIS: T1 committed, T2 in-flight; pages P,Q dirty since LSN n
       REDO:     replay from LSN n -> P and Q reflect both T1 and T2 changes
       UNDO:     roll back T2 (it never committed); T1's changes stay (durable)
       => result: T1 durable, T2 gone, atomicity + durability both preserved.
```

---

## Checkpoints — bounding recovery time

If recovery had to replay the *entire* log from the beginning of time, restart could take hours.
A **checkpoint** periodically records a consistent reference point so recovery only scans from
there.

```
   A FUZZY CHECKPOINT (ARIES, non-blocking — the practical kind):
     - write a BEGIN_CHECKPOINT record
     - snapshot the transaction table + dirty page table into an END_CHECKPOINT record
     - (optionally) start flushing dirty pages in the background
     - the system keeps running THROUGHOUT — no global quiesce

   Effect: ANALYSIS starts at the last checkpoint; REDO starts at the oldest dirty-page LSN
   recorded there. The further behind your dirty pages, the longer the redo.

   TRADE-OFF:
     frequent checkpoints  -> short recovery, more steady-state flush I/O
     rare checkpoints      -> less steady-state I/O, longer recovery after a crash
```

Bridge: SQL Server's `CHECKPOINT` and `RECOVERY INTERVAL` / indirect checkpoint target, and
Postgres's `checkpoint_timeout` / `max_wal_size`, are exactly this knob — they trade ongoing
flush cost against crash-recovery duration.

---

## Group commit and the COMMIT latency story

The commit rule (log fsync before ack) means COMMIT latency is bounded by a disk flush. To
amortize it, engines use **group commit**: batch the fsyncs of many concurrent transactions into
one disk flush.

```
   Without group commit: each COMMIT = its own fsync (slow under load)
   With group commit:    many txns' commit records accumulate, ONE fsync flushes them all
                         -> throughput scales; individual latency rises slightly under load
```

This is why a write-heavy workload can sustain far more commits/sec than the raw fsync rate
suggests, and why a single trickle of commits sees higher per-commit latency than a busy system.

---

## Logical vs physical logging (and why it matters for replication)

```
   PHYSICAL / PHYSIOLOGICAL LOG   records byte/page-level changes ("page P bytes 40-48 -> Y").
        - ARIES is physiological. Fast to redo. Tied to the exact page layout.
        - This is what SQL Server's log and Postgres's WAL fundamentally are.

   LOGICAL LOG                    records the operation ("UPDATE accounts SET ... WHERE id=5").
        - smaller, layout-independent, but replaying requires re-running logic deterministically.

   MySQL keeps BOTH: the InnoDB REDO LOG (physical, for crash recovery) and the BINLOG
   (logical/row or statement, for replication + point-in-time recovery). Postgres ships the
   WAL itself for physical replication, and decodes it logically for logical replication (g.07).
```

This split is the hinge to the next guide: the same log that recovers a crash is the stream you
replicate. Physical log → physical/streaming replication; logical decoding → logical replication.

---

## Old World → New World Bridges

| You already know | WAL / recovery concept | SQL Server / Azure anchor |
|------------------|------------------------|----------------------------|
| `fsync()` before acknowledging a write | The **commit rule** — log durable before COMMIT ack | `WRITELOG` waits; log flush |
| A `.ldf` transaction log you back up | The **WAL** itself | Transaction log; log backups |
| Append-only journal then apply (like a journaling FS) | Write-ahead log → lazy page flush | Same protocol |
| A redo log + undo log | ARIES **redo** (AFTER image) + **undo** (BEFORE image) | Recovery on startup / restore |
| Tuning how often dirty buffers flush | **Checkpoint** frequency knob | `RECOVERY INTERVAL`, indirect checkpoints |
| Point-in-time restore from log | Replay WAL/log to a target LSN/time | Log shipping; PITR |
| Batching fsyncs for throughput | **Group commit** | Delayed durability (an explicit SQL Server option) |

---

## Decision Cheat Sheet

| Situation / question | Answer |
|----------------------|--------|
| "Will COMMIT survive a power cut?" | Yes — commit record is fsync'd before ack (commit rule) |
| "Why is COMMIT slower than the UPDATE?" | COMMIT waits on the **log fsync**, not the page write |
| Crash recovery taking too long on restart | Checkpoint more often / lower recovery interval (shorter redo) |
| Steady-state write I/O too high | Checkpoint less often / raise `max_wal_size` (more redo on crash) |
| Need point-in-time restore | Keep WAL/log + base backup; replay to target LSN/time |
| Need replication off the same machinery | Ship physical WAL (streaming) or decode logical (g.07) |
| High commit throughput needed | **Group commit** / delayed durability (accept tiny loss window) |
| "Can I lose committed data?" | Only if you disable durable commit (delayed durability) and crash |

---

## Common Confusion Points

### "The data file is always up to date"

It is routinely *behind* the log. The WAL is the source of truth; data pages are flushed lazily
at checkpoints. After a crash, the data file is an old, possibly inconsistent snapshot that
recovery reconciles by replaying the log. This is by design — it's what makes commits fast.

### "Redo only replays committed transactions"

ARIES redo **repeats history** — it replays *all* logged changes, including those of
transactions that never committed, to exactly reconstruct the pre-crash state. The *undo* pass
then rolls back the uncommitted ones. Replaying only-committed would not reproduce the correct
on-disk state the undo pass needs to operate on.

### "A checkpoint blocks the database"

Modern (fuzzy/ARIES) checkpoints are **non-blocking** — they record the transaction and dirty
page tables and let work continue. Old "sharp" checkpoints that quiesced the system are largely
historical. The cost of a checkpoint is the background flush I/O, not a stall.

### "The transaction log and the WAL are separate features"

They are the same thing under different vendor names — SQL Server "transaction log," Postgres
"WAL," the academic "write-ahead log." If you understand one, you understand the others.

### "Undo and redo are about the same kind of failure"

**Redo** recovers committed work the crash hadn't yet flushed to data pages (durability).
**Undo** removes uncommitted work the crash left half-applied (atomicity). One crash needs both
passes — they fix opposite halves of the same inconsistent post-crash state.
