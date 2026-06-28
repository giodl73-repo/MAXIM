# database-systems/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Anatomy of a database engine — the landscape | ✅ |
| 01-STORAGE-ENGINES.md | Heap/B-tree vs LSM-tree, pages, buffer pool, the amplification triangle | ✅ |
| 02-INDEXING.md | B+tree, hash, covering, composite, bitmap, inverted; index selection | ✅ |
| 03-QUERY-PROCESSING.md | Parse→plan→optimize→execute, join algorithms, cost-based optimization, statistics | ✅ |
| 04-TRANSACTIONS-MVCC.md | ACID, MVCC, 2PL, snapshot isolation mechanics | ✅ |
| 05-ISOLATION-LEVELS.md | The 4 SQL levels, the anomalies each does/does not prevent, serializable vs SSI | ✅ |
| 06-WAL-AND-RECOVERY.md | Write-ahead logging, ARIES, checkpoints, crash recovery | ✅ |
| 07-REPLICATION.md | Sync/async, leader-follower, quorum, conflict resolution | ✅ |
| 08-SHARDING-PARTITIONING.md | Hash/range partitioning, rebalancing, distributed transactions, 2PC | ✅ |
| 09-DISTRIBUTED-SQL.md | NewSQL — Spanner/CockroachDB/Cosmos, CAP tradeoffs, the consistency spectrum | ✅ |

## Coverage Notes

The database *internals* layer that sits below `query-languages/`. Where `query-languages/`
teaches SQL and dialect *syntax* (SELECT, window functions, T-SQL vs PostgreSQL), this
directory teaches how the engine *underneath* the syntax actually works: how rows are laid
out on pages, how the buffer pool fakes infinite memory, how the optimizer turns a declarative
query into a physical plan, how MVCC lets readers and writers coexist without blocking, what
each isolation level genuinely guarantees, how the WAL makes a crash survivable, and how the
whole thing scales out across machines.

The spine is the **nesting of concurrency control inside durability inside storage**: a
transaction's isolation guarantee is built on MVCC version chains, which live on pages, which
are made durable by the WAL, which is the thing replication ships to followers. Every guide
states precise guarantees — especially isolation levels, the most error-prone topic in
databases. Snapshot isolation prevents dirty/non-repeatable/phantom reads but
NOT write skew; that distinction is load-bearing and stated exactly.

Bridges are kept universal first (heap vs index-organized, pessimistic vs optimistic
concurrency, sync vs async replication) with SQL Server / Cosmos DB / Azure SQL as additive
familiarity for this reader. Cross-references: `query-languages/` (the syntax layer above),
`distributed-systems/` (CAP, consensus, Paxos/Raft — the theory `07`–`09` build on),
`data-science/` (columnar/OLAP analytics engines), `os/` (page cache, fsync, scheduling, the
memory hierarchy the buffer pool exploits).
