---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-STORAGE-ENGINES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:database-systems:storage-engines
kind: guide
module: database-systems
section: computing-software
title: Storage Engines - Heap, B-tree, LSM, Buffer Pool, Amplification
status: source-custody
source_custody: partial
current_path: database-systems/01-STORAGE-ENGINES.md
canonical_path: database-systems/01-STORAGE-ENGINES.md
backsource_ids: [mdloom-backfill:database-systems:01-storage-engines, git-history:database-systems:01-storage-engines]
concepts: [storage engine, page, buffer pool, heap file, b-tree, lsm-tree, write amplification, read amplification, space amplification]
root_concepts: [storage engine]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Storage Engines — How a Row Becomes Bytes on Disk

The storage engine is the bottom of the stack: it owns the question "where do the actual bytes
live, and how do I get them in and out of memory efficiently?" Everything above it — indexes,
transactions, the optimizer — assumes this layer just works.

```
+=========================================================================================+
|                        THE STORAGE ENGINE, FROM ROW TO BLOCK DEVICE                     |
+=========================================================================================+
|                                                                                         |
|   LOGICAL ROW   (id=42, name='Ada', balance=100)                                        |
|        |                                                                                |
|        v   serialized into a tuple/record format (header + column values)               |
|   +---------------------------------------------------------------------------------+   |
|   |  PAGE  (a.k.a. block)  — the fixed-size unit of I/O. 8 KB Postgres/SQL Server,    |  |
|   |  16 KB InnoDB default. The DB NEVER reads a single row from disk; it reads a page.|  |
|   |  +--------+-------------------------------+----------------------+-------------+  |   |
|   |  | header | slot array -> -> ->           |   free space        |  <- tuples  |  |   |
|   |  +--------+-------------------------------+----------------------+-------------+  |   |
|   |  (slotted page: slots grow down, tuples grow up, meet in the middle)             |  |
|   +---------------------------------------------------------------------------------+   |
|        |                                                                                |
|        v   pages are cached in RAM by...                                                 |
|   +---------------------------------------------------------------------------------+   |
|   |  BUFFER POOL  — the DB's own page cache. Hot pages live here; cold pages get      |  |
|   |  evicted (LRU/clock). A "hit" = page already in RAM. A "miss" = read from disk.   |  |
|   |  Dirty pages (modified) must be flushed before eviction, AFTER the WAL is durable.|  |
|   +---------------------------------------------------------------------------------+   |
|        |                                                                                |
|        v   pages laid out on disk in one of two grand strategies...                      |
|   +---------------------------------+   +-----------------------------------------+       |
|   |  IN-PLACE FILES                 |   |  LOG-STRUCTURED FILES (LSM)             |       |
|   |  heap files + B-tree files      |   |  memtable + immutable SSTables          |       |
|   |  mutate the page in place       |   |  append-only, merge in background       |       |
|   +---------------------------------+   +-----------------------------------------+       |
|                                                                                         |
+=========================================================================================+
```

**The whole game is the memory hierarchy.** RAM is ~100,000x faster than a random disk seek
(less extreme on NVMe, but still 100x+). The buffer pool's job is to keep the working set in
RAM. The storage layout's job is to minimize how many pages you must touch and how randomly.

---

## Layer 1: The Page

Bridge to `os/`: a database page is to the buffer pool what an OS page is to virtual memory —
the unit of caching and I/O. The DB deliberately manages its own buffer pool *instead of*
relying on the OS page cache because it knows access patterns (which page a B-tree descent will
touch next) the OS cannot.

```
   SLOTTED PAGE LAYOUT  (used by Postgres, SQL Server, InnoDB, most engines)

   +------+----+----+----+--------------------------------+------+------+------+
   |HEADER|slot|slot|slot| -------- FREE SPACE -------->   |tuple3|tuple2|tuple1|
   +------+----+----+----+--------------------------------+------+------+------+
            |    |    |                                       ^      ^      ^
            |    |    +---------------------------------------+      |      |
            |    +----------------------------------------------------+     |
            +----------------------------------------------------------------+

   - Slots are a small array of (offset, length) pointers near the page header.
   - Tuples are packed from the END of the page backward.
   - To find row N: read slot N -> get offset -> read tuple. O(1) within a page.
   - DELETE = mark the slot dead (tuple becomes garbage, reclaimed later).
   - VARIABLE-LENGTH rows are why we need the slot indirection at all.
```

Why slotted pages matter for the layers above: a row's physical address is a **(page id, slot
number)** pair — Postgres calls it a `ctid`, SQL Server a RID, Oracle a ROWID. Indexes point at
these. When MVCC creates a new version of a row (guide 04), it often writes a new tuple in the
same or another page and the old slot points forward — the version chain lives in this layout.

---

## Layer 2: The Buffer Pool

```
   READ PATH                                WRITE PATH
   ---------                                ----------
   1. Want page P                           1. Modify page P in the pool (now "dirty")
   2. In buffer pool? --YES--> return       2. Write the change to the WAL first  <-- KEY
   3. --NO--> evict a victim (clock/LRU)    3. Acknowledge COMMIT once WAL is durable
   4. If victim dirty, flush it first       4. Page stays dirty in RAM; flushed LATER
   5. Read P from disk into the frame          by a background writer / at a checkpoint
   6. return P
```

Two rules of the buffer pool are load-bearing for the rest of the database:

1. **WAL before page (Write-Ahead Logging).** A dirty page may NOT be written to its home
   location on disk until the log record describing the change is durable. This is what makes
   crash recovery possible (guide 06). The page on disk can lag arbitrarily far behind RAM
   because the WAL is the source of truth.
2. **Eviction needs a clean target.** Evicting a dirty page forces a flush. Checkpoints
   (guide 06) bound how much dirty state accumulates so recovery stays fast.

> Bridge: SQL Server's buffer pool and lazy writer behave exactly this way — `WRITELOG` waits
> are the COMMIT blocking on log flush; checkpoint + lazy writer flush dirty pages. This is the
> universal design, not a Microsoft quirk.

---

## Layer 3a: In-Place Storage — Heap and B-tree Files

### Heap files

A **heap** is an unordered pile of pages. Rows go wherever there is free space. To find a
specific row without an index you must scan every page — a **sequential / table scan**, O(n).
Heaps are cheap to insert into (append to a page with room) but terrible to search.

```
   HEAP TABLE                INDEX-ORGANIZED TABLE (clustered)
   ----------                ---------------------------------
   page1: rows (any order)   The TABLE *is* a B+tree keyed on the primary key.
   page2: rows (any order)   Rows are stored AT the leaves, sorted by key.
   page3: rows (any order)   Range scans on the key are sequential and fast.
                             InnoDB and SQL Server clustered indexes work this way.
   + cheap inserts
   - every lookup = scan      + fast PK lookups and range scans
   (needs separate indexes)   - secondary indexes store the PK, not a row pointer
```

Bridge: in SQL Server a table with no clustered index is literally a *heap*; adding a clustered
index turns it into an index-organized table. InnoDB has no heap option — every table is
clustered on its primary key. This is a real, observable difference between engines.

### B+tree files — the workhorse index/storage structure

```
                         B+TREE (order shown small for clarity)

                              +-------------------+
                              |    [ 30 | 70 ]    |   <- internal node: keys + child ptrs
                              +----+----+----+----+
                            <30 |    |30-70|   |>=70
                                v         v        v
                  +----------+      +----------+      +----------+
                  | [10|20]  |      | [40|55]  |      | [80|95]  |   <- internal
                  +--+--+--+-+      +--+--+--+-+      +--+--+--+-+
                     ...                ...               ...
                  +----+----+----+   leaf level (all keys live here, sorted)
   ... <-LEAF[10|15]<->LEAF[20|25]<->LEAF[40|50]<->LEAF[55|60]<->LEAF[80|90]-> ...
            ^------ leaves are LINKED -> a range scan walks the linked list ------^
```

Properties that matter (these are correct, do not let anyone confabulate them):

| Property | Value | Why it matters |
|----------|-------|----------------|
| Height | O(log_b n), b = keys per page (large, ~hundreds) | A billion rows is ~3–4 levels deep |
| Point lookup | O(log_b n) page reads | 3–4 page touches, often all cached but the leaf |
| Range scan | O(log_b n) to find start + sequential leaf walk | Leaves are linked → sequential I/O |
| Insert/Delete | O(log_b n), with page **splits/merges** | Splits cause write amplification + fragmentation |
| Fill factor | Pages kept partly empty (e.g. 70%) | Leaves room for in-place inserts; trades space |

**B-tree vs B+tree:** in a classic B-tree, keys (and data) live in *all* nodes; in a **B+tree**,
all data/keys live at the **leaves** and internal nodes hold only routing keys, with leaves
linked for range scans. Real databases use B+trees (or close variants); people loosely say
"B-tree." Guide 02 covers the index side of this structure.

---

## Layer 3b: Log-Structured Storage — the LSM-tree

The LSM-tree (Log-Structured Merge-tree, O'Neil et al., 1996) inverts the design: **never
mutate a page in place.** All writes append. This trades read cost for hugely cheaper, more
sequential writes — the right call for write-heavy and SSD/flash workloads.

```
   LSM-TREE WRITE/READ FLOW

   WRITE  -> append to WAL (durability) -> insert into MEMTABLE (sorted in RAM, e.g. skiplist)
                                                  |
                          memtable full ----------+
                                                  v
                          FLUSH to disk as an immutable, sorted SSTable (Level 0)
                                                  |
                   background COMPACTION merges SSTables across levels, dropping
                   overwritten/deleted keys (tombstones), keeping each level sorted
                                                  |
                                                  v
            L0  [sst][sst][sst]        (recently flushed, may overlap key ranges)
            L1  [----- sorted, non-overlapping runs -----]
            L2  [--------------- larger sorted runs ---------------]
            L3  [------------------------ even larger -------------------------]

   READ   -> check memtable -> check each level newest-first -> stop at first hit
             (a key may exist in several levels; the NEWEST version wins)
             Bloom filters per SSTable skip levels that definitely lack the key.
```

Two structures make LSM reads survivable:

- **Bloom filter** per SSTable: a probabilistic set membership test. "Definitely not here" lets
  a read skip an SSTable without touching it; false positives only cost a wasted probe. This is
  what keeps point reads from degrading to "search every level."
- **Sparse index / fence pointers** per SSTable: maps key ranges to block offsets so a read
  within an SSTable is a binary search, not a scan.

**Deletes are tombstones.** You cannot erase a key from an immutable file; you append a
*tombstone* marker. The key (and its tombstone) only physically disappear during compaction.
Until then a delete can *increase* space — a real operational gotcha in Cassandra/RocksDB.

> Where LSMs live: **RocksDB** and **LevelDB** are libraries — they are the storage engine
> *inside* other systems (CockroachDB's Mdport is a RocksDB-family engine; MyRocks is InnoDB
> swapped for RocksDB under MySQL). **Cassandra** and **ScyllaDB** are LSM-native databases.

---

## The Amplification Triangle — the universal trade-off

Every storage engine pays in three currencies. You cannot minimize all three; you pick a corner.

```
                          WRITE AMPLIFICATION
                          (bytes written to disk
                           per byte of logical write)
                                   /\
                                  /  \
                                 /    \
                                /  B+  \        B-tree: low write-amp on point inserts
                               / tree   \       but page splits + full-page rewrites; in-place
                              /          \      updates rewrite a whole 8-16KB page per change.
                             /------------\
            READ            /              \           SPACE
        AMPLIFICATION      /     LSM         \      AMPLIFICATION
   (extra reads per       /      tree         \   (disk used per byte
    logical read)        /____________________\   of live data)

   LSM-tree:  HIGH read-amp (a key may live in several levels) and tunable space-amp
              (tombstones + un-compacted overwrites), but LOW, SEQUENTIAL write-amp.
   B+tree:    LOW read-amp (one descent), MODERATE write-amp (page rewrites/splits),
              MODERATE space-amp (fill-factor slack + fragmentation).
```

| Amplification | Definition | B+tree (in-place) | LSM-tree |
|---------------|------------|-------------------|----------|
| **Write** | physical bytes written ÷ logical bytes written | Moderate (page splits, full-page writes, WAL) | Low at ingest, but **compaction** rewrites data many times over its life |
| **Read** | pages touched ÷ pages of answer | Low — one root-to-leaf descent | Higher — check memtable + multiple levels (Bloom filters mitigate) |
| **Space** | disk used ÷ live data | Moderate — fill-factor slack, fragmentation | Tunable — tombstones + stale versions until compaction; leveled vs tiered changes this |

Compaction strategy is the LSM tuning knob: **leveled** compaction (RocksDB default for lower
levels) minimizes space and read amp at the cost of higher write amp; **tiered/size-tiered**
(Cassandra option) minimizes write amp at the cost of more space and read amp. This is a pure
trade, not a bug.

---

## Old World → New World Bridges

| You already know | Storage-engine concept | SQL Server / Azure anchor |
|------------------|------------------------|----------------------------|
| OS page cache / mmap | The **buffer pool**, but DB-managed with knowledge of access patterns | SQL Server buffer pool |
| A table with no index = full scan | **Heap file** sequential scan | SQL Server heap (no clustered index) |
| The PK *is* the storage order | **Index-organized / clustered** table | Clustered index = the table; InnoDB always |
| Log-append then compact (like a GC'd allocator) | **LSM-tree** memtable → SSTable → compaction | Azure Cosmos/Cassandra-API uses LSM under the hood |
| Defragmenting a disk | **B-tree fragmentation** from splits; index rebuild/REORGANIZE | `ALTER INDEX REBUILD` |
| A `.ldf` you fsync | **WAL** that gates dirty-page flush (guide 06) | Transaction log flush before COMMIT ack |

---

## Decision Cheat Sheet

| Situation | Pick / expect |
|-----------|---------------|
| Read-heavy OLTP, point + range lookups on indexed keys | **B+tree** in-place engine (Postgres, InnoDB, SQL Server) |
| Write-heavy ingest, time-series, log/event data, SSD | **LSM-tree** (RocksDB-backed, Cassandra) |
| You need cheap, predictable point reads above all | B+tree — single descent, no Bloom-filter misses |
| You need maximum sustained write throughput | LSM with size-tiered compaction (accept space + read amp) |
| Disk space is the binding constraint | LSM **leveled** compaction (low space amp) or compress B-tree pages |
| "Why did my delete not free space?" | LSM tombstones — space reclaimed only at compaction |
| "Why is COMMIT slower than the write?" | WAL flush gating COMMIT (guide 06), not the page write |
| Range scans dominate | B+tree — linked leaves give sequential I/O |

---

## Common Confusion Points

### "A B-tree and a B+tree are the same thing"

Practically every database uses a **B+tree** (data only at linked leaves) but everyone says
"B-tree." The B+tree's linked leaves are *why* range scans are fast — a detail that matters when
you reason about why `WHERE id BETWEEN x AND y` is cheap but `WHERE name LIKE '%foo%'` is not.

### "LSM-trees are just faster"

They are faster for **writes** and pay for it in **read** and sometimes **space** amplification.
A point lookup in an LSM may probe a memtable plus several SSTable levels; Bloom filters hide
most of that cost but not all. For read-dominated indexed lookups, a B+tree usually wins.

### "The data on disk is always current"

No. With WAL + buffer pool, the page on disk can be *older* than RAM — the WAL holds the truth
until a checkpoint flushes dirty pages. After a crash, recovery replays the WAL to reconcile
(guide 06). With an LSM, the "current" value of a key may be split across the memtable and
multiple SSTable levels, newest wins.

### "Bigger pages are always better"

Bigger pages amortize I/O for scans but waste buffer-pool RAM and increase write amplification
(a one-byte change rewrites the whole page). 8–16 KB is the empirical sweet spot for OLTP;
analytics engines (guide 03, `data-science/`) use much larger columnar blocks because they scan.

### "The OS cache and the buffer pool are redundant"

They overlap, and databases often advise bypassing or shrinking the OS cache (direct I/O)
precisely to avoid double-caching. The buffer pool wins because it understands the access
pattern — it can pin a B-tree root, prefetch leaves for a range scan, and coordinate flushes
with the WAL. The OS cache cannot.
