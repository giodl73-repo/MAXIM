# MySQL / MariaDB

MySQL is the most widely deployed RDBMS on the planet by install count (LAMP stack legacy). MariaDB is its community fork post-Oracle acquisition. MySQL 8.0 (2018) finally added full window function support, CTEs, and enforced CHECK constraints — closing most of the gap with PostgreSQL/SQL Server.

---

## Ecosystem Position

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MySQL / MariaDB Architecture                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  CONNECTION LAYER                                                            │
│  Thread-per-connection model (or thread pool with ProxySQL / MariaDB TP)   │
│  Authentication · SSL/TLS · Connection cache                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  SQL LAYER                                                                  │
│  ┌──────────────┐  ┌─────────────────────────┐  ┌─────────────────────┐     │
│  │   Parser      │  │   Query Optimizer        │  │  Query Cache        │   │
│  │  ─────────── │  │  ───────────────────────│  │  ─────────────────  │   │
│  │  Lexer+parser│  │  Cost-based (index dives │  │  REMOVED in 8.0     │   │
│  │  AST → plan  │  │  + InnoDB stats)         │  │  Was a severe        │   │
│  │  Privilege   │  │  Execution plan cache     │  │  scalability        │   │
│  │  check here  │  │  (prepared stmt cache)   │  │  bottleneck         │   │
│  └──────────────┘  └─────────────────────────┘  └─────────────────────┘   │
├─────────────────────────────────────────────────────────────────────────────┤
│  STORAGE ENGINE API (pluggable interface)                                   │
│  ── This is architecturally unlike SQL Server, which has one storage engine │
│  ── The SQL layer calls engine API: ha_write_row(), ha_read_next(), etc.    │
├─────────────────────────────────────────────────────────────────────────────┤
│  InnoDB (USE THIS)                    │  Other engines (mostly avoid)       │
│  ┌────────────────────────────────┐   │  MyISAM — no transactions, legacy   │
│  │  Buffer Pool (default 128MB;   │   │  Memory — RAM-only, no persistence  │
│  │  set innodb_buffer_pool_size   │   │  CSV — flat file, no indexes        │
│  │  to 70-80% of RAM)             │   │  Archive — append-only, compressed  │
│  ├────────────────────────────────┤   │  NDB — MySQL Cluster (shared-nothing│
│  │  Change Buffer                 │   │        distributed; niche)          │
│  │  Defers writes to secondary    │   │                                     │
│  │  index pages not in buffer     │   │                                     │
│  │  pool — merged on read         │   │                                     │
│  ├────────────────────────────────┤   │                                     │
│  │  Redo Log (iblogfile0/1)       │   │                                     │
│  │  WAL — sequential write before │   │                                     │
│  │  data pages; crash recovery    │   │                                     │
│  │  Single circular log file      │   │                                     │
│  │  (cf. SQL Server: multiple VLFs│   │                                     │
│  │  in .ldf, grows/shrinks)       │   │                                     │
│  ├────────────────────────────────┤   │                                     │
│  │  Undo Log (in tablespace)      │   │                                     │
│  │  Row versions for MVCC         │   │                                     │
│  │  NOT in tempdb — in-file       │   │                                     │
│  │  Purge thread reclaims space   │   │                                     │
│  │  (cf. SQL Server: version store│   │                                     │
│  │  in tempdb, cleared on restart)│   │                                     │
│  ├────────────────────────────────┤   │                                     │
│  │  Data Files (.ibd per table)   │   │                                     │
│  │  Every table = clustered B+tree│   │                                     │
│  │  NO HEAP option exists         │   │                                     │
│  │  (cf. SQL Server: heap or CI)  │   │                                     │
│  └────────────────────────────────┘   │                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────┐  ┌──────────────────────────────────┐
│  SQL Server Table Storage Options    │  │  InnoDB Table Storage (always)   │
│  ──────────────────────────────────  │  │  ──────────────────────────────  │
│  Option A: Heap                      │  │  Every table IS a clustered      │
│  No clustered index                  │  │  B+ tree on the primary key.     │
│  NCI stores 8-byte RID               │  │  No heap option.                 │
│  (file:page:slot pointer)            │  │                                  │
│  Direct row fetch from RID           │  │  No PK defined?                  │
│                                      │  │  → InnoDB generates hidden       │
│  Option B: Clustered Index           │  │    6-byte rowid as PK.           │
│  Table sorted by CI key              │  │                                  │
│  NCI stores CI key value             │  │  Secondary index stores PK       │
│  Lookup = NCI seek + CI seek         │  │  value, not a row pointer.       │
│  (bookmark lookup)                   │  │  Secondary lookup always costs   │
│                                      │  │  2 B-tree traversals unless      │
│  Developer CHOOSES heap or CI.       │  │  index is covering.              │
│  Escape hatch exists.                │  │  No escape hatch.                │
└──────────────────────────────────────┘  └──────────────────────────────────┘
```

---

## 1. Dialect Snapshot

| Attribute | Value |
|-----------|-------|
| Origin | MySQL AB (1995) → Sun Microsystems (2008) → Oracle (2010); MariaDB fork by Monty Widenius (2009) |
| License | MySQL: GPL v2 + commercial / MariaDB: GPL v2 |
| Current versions | MySQL 8.0, 8.4 (LTS); MariaDB 11.x |
| ACID compliance | Full with InnoDB (default engine) |
| Strengths | Read-heavy OLTP, replication simplicity, ubiquity, LAMP/LEMP stack, AWS Aurora |
| Weaknesses | Weaker analytics than PostgreSQL, older optimizer, Oracle stewardship concerns |
| Cloud managed | AWS RDS MySQL, AWS Aurora (MySQL-compatible), Azure Database for MySQL, GCP Cloud SQL, PlanetScale |

---

## 2. InnoDB — The Only Engine You Should Use

```
MySQL Storage Engines
├── InnoDB (USE THIS)  — ACID, row-level locking, FK constraints, MVCC
├── MyISAM (AVOID)     — no transactions, table-level locks, no FK, legacy only
├── MEMORY             — hash/btree in RAM, lost on restart (use Redis instead)
├── CSV                — flat CSV files, no indexes (special use only)
└── ARCHIVE            — compressed append-only (log archival)

InnoDB is the default since MySQL 5.5 (2010).
If you see ENGINE=MyISAM in old code, treat it as technical debt.
```

### InnoDB Key Behaviors

| Behavior | Detail |
|----------|--------|
| MVCC | Readers don't block writers (same model as SQL Server snapshot isolation) |
| Row-level locking | Not table-level like MyISAM — concurrent DML scales |
| Clustered index | EVERY InnoDB table IS a clustered B+ tree on the primary key — not the same as SQL Server's optional clustered index. SQL Server allows heaps (no CI); InnoDB does not. No PK defined → InnoDB synthesizes a hidden 6-byte rowid. |
| Secondary index storage | Stores PK value as row pointer — not a physical RID. Every non-covering secondary lookup traverses two B-trees: secondary index seek → PK B-tree seek. In SQL Server terms: it always does a bookmark lookup, even on a CI table, unless the index is covering. |
| Secondary index size | Wide PKs bloat every secondary index — each secondary index entry embeds the full PK value. UUID PK = 16 bytes per secondary index entry. SQL Server stores the CI key in NCIs too, but you can choose a narrow surrogate. In InnoDB, you're stuck with whatever the PK is. |
| Foreign key enforcement | InnoDB enforces; MyISAM silently ignores FK declarations |
| Auto-increment gaps | Gaps occur on rollback and crash recovery — never assume sequence continuity |
| UUID as PK | Random-write fragmentation: InnoDB must maintain physical sort order, so UUID PKs cause page splits on every insert. SQL Server has this too for clustered indexes, but you can use a heap as escape hatch. InnoDB has no escape hatch. Use `UUID_TO_BIN(UUID(), 1)` (version 1, time-sorted) or an AUTO_INCREMENT surrogate instead. |

```
InnoDB B-Tree Layout vs SQL Server Index Structures
─────────────────────────────────────────────────────────────────────────────

  InnoDB — table with PK (id INT)
  ┌─────────────────────────────────────────────────────────────────────┐
  │  PK Clustered Index (the table itself)                              │
  │  Leaf pages: id=1 | email | name | ...all columns...                │
  │              id=2 | email | name | ...all columns...                │
  │              id=3 | email | name | ...all columns...                │
  └─────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Secondary Index on email                                           │
  │  Leaf pages: 'a@b.com' → PK=1    ← PK value, NOT a row pointer      │
  │              'c@d.com' → PK=3    ← must go back to PK tree          │
  └─────────────────────────────────────────────────────────────────────┘
  Query: SELECT name FROM users WHERE email = 'a@b.com'
  Step 1: secondary index seek on 'a@b.com' → returns PK=1
  Step 2: PK clustered index seek on id=1 → returns full row
  (2 B-tree traversals unless index covers all needed columns)

  SQL Server — heap table (no clustered index)
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Heap (IAM pages → data pages, unordered)                           │
  │  Row at RID=(file=1, page=73, slot=4): email | name | ...           │
  │  Row at RID=(file=1, page=73, slot=5): email | name | ...           │
  └─────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Nonclustered Index on email                                        │
  │  Leaf pages: 'a@b.com' → RID=(1,73,4)  ← 8-byte physical pointer    │
  │              'c@d.com' → RID=(1,73,5)  ← direct fetch, no 2nd seek│
  └─────────────────────────────────────────────────────────────────────┘
  Query: SELECT name FROM users WHERE email = 'a@b.com'
  Step 1: NCI seek on 'a@b.com' → RID=(1,73,4)
  Step 2: direct heap fetch by RID (single page, O(1))

  SQL Server — clustered index table (CI on id)
  ┌─────────────────────────────────────────────────────────────────────┐
  │  NCI on email: 'a@b.com' → CI key (id=1)  ← CI key, not RID         │
  └─────────────────────────────────────────────────────────────────────┘
  → same 2-lookup pattern as InnoDB secondary: NCI seek + CI seek

  Bottom line: InnoDB always behaves like "SQL Server with a CI on every table
  and no heap option." Every NCI is a bookmark lookup unless covering.
  Optimize for covering indexes aggressively in MySQL.
```

### InnoDB vs SQL Server Storage Internals

| Dimension | InnoDB | SQL Server |
|-----------|--------|-----------|
| Page size | 16 KB default (configurable: 4/8/16/32/64 KB) | 8 KB (fixed) |
| Clustered index | Always — every table is a B+ tree on PK | Optional — developer chooses CI or heap |
| No PK defined | Hidden 6-byte rowid synthesized | Heap (RID-based NCI pointers) |
| Secondary index pointer | PK value embedded in every secondary index entry | CI key (if CI table) or 8-byte RID (if heap) |
| Undo log location | Undo tablespace within the data directory (undo001, undo002) | tempdb version store (shared across all databases) |
| Undo persistence | Persistent across restarts; purge thread reclaims space | Cleared on SQL Server restart; new version store starts empty |
| Redo log | Circular ib_logfile0 / ib_logfile1 (WAL) | Sequential .ldf with VLF segments; grows/shrinks |
| MVCC row versions | Undo log in tablespace (not in row) | Version store in tempdb (or PVS in user DB with ADR) |
| Change buffer | Yes — defers writes to secondary index pages not in buffer pool | No direct equivalent; write-ahead log + async checkpoint |
| Version store bloat symptom | Undo tablespace grows; purge thread falls behind | tempdb grows (RCSI/SI); ADR PVS grows in user DB |

---

## 3. Core Syntax Differences from T-SQL

| Operation | T-SQL (SQL Server) | MySQL |
|-----------|-------------------|-------|
| Top N rows | `SELECT TOP 10 * FROM t` | `SELECT * FROM t LIMIT 10` |
| Top N with offset | `OFFSET 20 ROWS FETCH NEXT 10` | `LIMIT 10 OFFSET 20` |
| Identity column | `IDENTITY(1,1)` | `AUTO_INCREMENT` |
| Current timestamp | `GETDATE()` / `SYSDATETIME()` | `NOW()` / `CURRENT_TIMESTAMP` |
| Null coalesce | `ISNULL(a, b)` | `IFNULL(a, b)` or `COALESCE(a, b)` |
| String length (chars) | `LEN(str)` | `CHAR_LENGTH(str)` |
| String length (bytes) | `DATALENGTH(str)` | `LENGTH(str)` |
| String concat | `'a' + 'b'` or `CONCAT()` | `CONCAT(a, b, c)` (+ is addition) |
| Find in string | `CHARINDEX(needle, hay)` | `LOCATE(needle, hay)` |
| Substring replace | `STUFF(str, pos, len, rep)` | `INSERT(str, pos, len, rep)` |
| Date diff | `DATEDIFF(unit, start, end)` | `DATEDIFF(date1, date2)` (days only!) |
| Date add | `DATEADD(unit, n, date)` | `DATE_ADD(date, INTERVAL n unit)` |
| Aggregate to string | `STRING_AGG(col, ',')` | `GROUP_CONCAT(col ORDER BY col SEPARATOR ',')` |
| XML output | `FOR XML PATH(...)` | `JSON_ARRAYAGG()` or `GROUP_CONCAT` |
| Lateral join | `CROSS APPLY` | `LATERAL` (MySQL 8.0+) |
| Full outer join | Native `FULL OUTER JOIN` | No native — emulate (see below) |
| Identifier quoting | `[column_name]` | `` `column_name` `` (backticks) |
| Boolean type | `BIT` | `TINYINT(1)` (TRUE/FALSE = aliases for 1/0) |

```sql
-- FULL OUTER JOIN emulation in MySQL
SELECT l.*, r.*
FROM left_table l
LEFT JOIN right_table r ON l.id = r.id

UNION ALL

SELECT l.*, r.*
FROM left_table l
RIGHT JOIN right_table r ON l.id = r.id
WHERE l.id IS NULL;   -- right-only rows not already in LEFT JOIN results
```

---

## 4. UPSERT — MySQL Style

```sql
-- ON DUPLICATE KEY UPDATE (MySQL-specific, not ANSI)
-- Triggers on any UNIQUE or PRIMARY KEY constraint violation
INSERT INTO user_stats (user_id, login_count, last_login)
VALUES (42, 1, NOW())
ON DUPLICATE KEY UPDATE
    login_count = login_count + 1,      -- reference existing column value
    last_login  = VALUES(last_login);   -- VALUES() references the proposed new value
-- WARNING: VALUES() deprecated in MySQL 8.0.20+

-- Modern form (8.0.20+): use row alias
INSERT INTO user_stats AS new_row (user_id, login_count, last_login)
VALUES (42, 1, NOW())
ON DUPLICATE KEY UPDATE
    login_count = login_count + 1,
    last_login  = new_row.last_login;   -- alias replaces VALUES()

-- REPLACE INTO — do NOT use for upsert
-- Mechanism: DELETE old row + INSERT new row
-- Consequences: triggers fire for DELETE, auto_increment increments, all unspecified cols reset to DEFAULT
REPLACE INTO orders (id, status) VALUES (42, 'shipped');  -- BAD: col3..colN become NULL/DEFAULT
```

---

## 5. Window Functions (MySQL 8.0+)

Added in MySQL 8.0 (2018). Syntax is ANSI-standard — same as SQL Server and PostgreSQL.

```sql
SELECT
    id, dept, salary,
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank,
    RANK()       OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank_with_gaps,
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank_no_gaps,
    SUM(salary)  OVER (PARTITION BY dept)                      AS dept_total,
    AVG(salary)  OVER (PARTITION BY dept)                      AS dept_avg,
    LAG(salary, 1)  OVER (ORDER BY hire_date)                  AS prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date)                  AS next_salary,
    FIRST_VALUE(salary) OVER (PARTITION BY dept ORDER BY hire_date) AS first_hire_salary,
    NTILE(4) OVER (ORDER BY salary)                            AS salary_quartile
FROM employees;

-- Named window (avoids repeating the OVER clause)
SELECT salary,
       AVG(salary)    OVER w AS dept_avg,
       MAX(salary)    OVER w AS dept_max
FROM employees
WINDOW w AS (PARTITION BY dept);

-- Running total with frame
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM orders;
```

MySQL 5.7 and earlier: zero window function support. Variable-based hacks (`@rank := @rank + 1`) were the workaround — those are now obsolete and should be rewritten.

---

## 6. CTEs (MySQL 8.0+)

```sql
-- Basic CTE
WITH high_value_customers AS (
    SELECT customer_id, SUM(total) AS lifetime_value
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total) > 10000
),
recent_orders AS (
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders
    WHERE order_date >= DATE_SUB(NOW(), INTERVAL 90 DAY)
    GROUP BY customer_id
)
SELECT c.name, h.lifetime_value, r.order_count
FROM customers c
JOIN high_value_customers h ON c.id = h.customer_id
LEFT JOIN recent_orders r   ON c.id = r.customer_id;

-- Recursive CTE (also MySQL 8.0+)
WITH RECURSIVE org_tree AS (
    -- Anchor: root nodes
    SELECT id, name, manager_id, 0 AS depth
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive: join children to already-found nodes
    SELECT e.id, e.name, e.manager_id, ot.depth + 1
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY depth, name;
```

---

## 7. JSON Support (MySQL 5.7.8+)

```sql
-- JSON column type: validates on insert, stored as binary optimized format
CREATE TABLE events (
    id   INT AUTO_INCREMENT PRIMARY KEY,
    data JSON NOT NULL
);

INSERT INTO events (data) VALUES ('{"user":{"id":42,"name":"Alice"},"action":"login"}');

-- ── Extraction ──────────────────────────────────────────────────────────────
data->'$.user.name'              -- JSON_EXTRACT() shorthand — returns JSON (quoted string)
data->>'$.user.name'             -- JSON_UNQUOTE(JSON_EXTRACT()) — returns unquoted string
JSON_VALUE(data, '$.user.name')  -- SQL:2016 standard syntax (MySQL 8.0.21+), returns scalar

-- Example
SELECT data->>'$.user.name' AS name FROM events WHERE data->>'$.action' = 'login';

-- ── Modification ────────────────────────────────────────────────────────────
JSON_SET(data, '$.status', 'active')     -- set (insert if missing, replace if exists)
JSON_INSERT(data, '$.new_key', 'value')  -- insert only (won't overwrite existing key)
JSON_REPLACE(data, '$.key', 'value')     -- replace only (won't insert missing key)
JSON_REMOVE(data, '$.key')               -- remove key

UPDATE events SET data = JSON_SET(data, '$.status', 'processed') WHERE id = 1;

-- ── Array operations ─────────────────────────────────────────────────────────
JSON_ARRAY(1, 'two', true)                    -- build array
JSON_ARRAYAGG(col ORDER BY col)               -- aggregate column to JSON array
JSON_OBJECTAGG(key_col, val_col)              -- aggregate to JSON object
JSON_CONTAINS(data, '"active"', '$.status')   -- returns 1/0
JSON_OVERLAPS(json1, json2)                   -- any values in common (MySQL 8.0)
JSON_SEARCH(data, 'one', 'Alice')             -- find path to value

-- ── Generated columns: index into JSON ───────────────────────────────────────
ALTER TABLE events
    ADD COLUMN user_id INT GENERATED ALWAYS AS (data->>'$.user.id') VIRTUAL;
CREATE INDEX idx_events_user_id ON events (user_id);
-- VIRTUAL: computed on read, no extra storage
-- STORED:  computed on write, takes storage, can be indexed directly
```

### JSON: MySQL vs SQL Server vs PostgreSQL

| Dimension | MySQL 5.7.8+ | SQL Server 2016+ | PostgreSQL (JSONB) |
|-----------|-------------|-----------------|-------------------|
| Storage format | Binary (internal optimized binary format) | NVARCHAR text — no binary type | Binary (JSONB), decomposed and indexed |
| Dedicated type | Yes — `JSON` column type, validated on insert | No — stored as `NVARCHAR(MAX)` or `VARCHAR(MAX)` | Yes — `JSON` (text) and `JSONB` (binary) |
| Native JSON index | No GIN/GiST equivalent — workaround: generated column + B-tree index | Computed column + index (same workaround as MySQL) | Yes — `CREATE INDEX ON t USING GIN(data)` enables containment queries |
| Containment query | `JSON_CONTAINS(data, '{"key":"val"}')` | No containment operator — must use `JSON_VALUE()` predicates | `data @> '{"key":"val"}'` — GIN-accelerated |
| Array aggregation | `JSON_ARRAYAGG(col ORDER BY col)` | `FOR JSON PATH` or `JSON_ARRAY()` (2022+) | `json_agg(col)` / `jsonb_agg(col)` |
| Shred JSON to rows | `JSON_TABLE(data, '$[*]' COLUMNS (...))` (8.0+) | `OPENJSON(data) WITH (...)` | `jsonb_to_recordset(data)` |
| Modify in place | `JSON_SET`, `JSON_INSERT`, `JSON_REPLACE`, `JSON_REMOVE` | `JSON_MODIFY(col, path, value)` | `jsonb_set(col, path, value)` |
| Path syntax | JSONPath `$.key.nested` | JSONPath `$.key.nested` (same style) | `{key,nested}` (different syntax) |

**Key bridges from SQL Server:**
- MySQL actually has a binary JSON type — unlike SQL Server's text storage. This means `data->>'$.key'` in MySQL is doing a binary parse, not a string scan. It is faster than SQL Server's equivalent `JSON_VALUE(col, '$.key')` at scale.
- The generated column index pattern (`ADD COLUMN x AS (data->>'$.key') VIRTUAL; CREATE INDEX ON t(x)`) is MySQL's answer to SQL Server's computed column + index pattern. Conceptually identical.
- `JSON_TABLE` (MySQL 8.0+) is the equivalent of `OPENJSON ... WITH (...)` — shreds a JSON array into relational rows with a typed schema.

---

## 8. Generated Columns

```sql
CREATE TABLE orders (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    subtotal   DECIMAL(10,2) NOT NULL,
    tax_rate   DECIMAL(5,4)  NOT NULL DEFAULT 0.0875,
    -- STORED: written to disk, can be indexed
    total      DECIMAL(10,2) GENERATED ALWAYS AS (subtotal * (1 + tax_rate)) STORED,
    -- VIRTUAL: recomputed on every read, no disk storage
    year_month CHAR(7)       GENERATED ALWAYS AS (DATE_FORMAT(order_date, '%Y-%m')) VIRTUAL,
    order_date DATE          NOT NULL
);

-- Index on STORED generated column — normal index
CREATE INDEX idx_order_total ON orders (total);

-- Can reference generated columns in queries normally
SELECT * FROM orders WHERE total > 100;
SELECT year_month, SUM(total) FROM orders GROUP BY year_month;
```

---

## 9. Fulltext Indexes

```sql
-- InnoDB supports FULLTEXT since MySQL 5.6
CREATE TABLE articles (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT    NOT NULL,
    body  LONGTEXT NOT NULL,
    FULLTEXT INDEX ft_article (title, body)
) ENGINE=InnoDB;

-- Add FULLTEXT index to existing table
ALTER TABLE articles ADD FULLTEXT INDEX ft_article (title, body);

-- ── Natural language mode (default) ──────────────────────────────────────────
-- Returns results ranked by relevance; common words (stopwords) ignored
SELECT id, title,
       MATCH(title, body) AGAINST ('database performance tuning') AS relevance
FROM articles
WHERE MATCH(title, body) AGAINST ('database performance tuning')
ORDER BY relevance DESC;

-- ── Boolean mode ──────────────────────────────────────────────────────────────
-- +word: required  -word: excluded  "phrase": exact  word*: prefix  ~word: lower rank
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST (
    '+database -slow "query optimization" index*'
    IN BOOLEAN MODE
);

-- ── Query expansion ───────────────────────────────────────────────────────────
-- First pass: find top results. Second pass: expand using words from those results.
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST ('database' WITH QUERY EXPANSION);
```

---

## 10. EXPLAIN

```sql
-- Basic
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;

-- JSON format — more detail (partitions, filtered, cost estimates)
EXPLAIN FORMAT=JSON SELECT * FROM orders WHERE customer_id = 42;

-- ANALYZE — actually executes query, shows actual vs. estimated rows (MySQL 8.0.18+)
EXPLAIN ANALYZE SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.region = 'US';
```

### Key EXPLAIN Columns

| Column | What to Look For |
|--------|-----------------|
| `type` | `system` > `const` > `eq_ref` > `ref` > `range` > `index` > **`ALL`** — ALL = full table scan, bad |
| `key` | Which index was used (`NULL` = no index used) |
| `key_len` | Bytes used of the index — shorter may mean partial composite index usage |
| `rows` | Estimated rows examined (not returned) |
| `filtered` | Estimated percentage of rows that pass the WHERE filter |
| `Extra` | `Using filesort` = ORDER BY not satisfied by index; `Using temporary` = temp table; `Using index` = covering index (fast) |

### SQL Server Performance Tooling → MySQL Equivalents

| SQL Server Tool | MySQL Equivalent | Gap |
|----------------|-----------------|-----|
| SSMS graphical execution plan (estimated) | `EXPLAIN FORMAT=JSON` + MySQL Workbench Visual Explain | No operator cost %/bars; must read cost fields in JSON |
| SSMS graphical execution plan (actual) | `EXPLAIN ANALYZE` (MySQL 8.0.18+) — executes query, shows actual vs. estimated rows + loop times | ANALYZE runs the query; no dry-run option |
| `SET STATISTICS IO ON` (logical reads per table) | No direct equivalent — `EXPLAIN ANALYZE` shows rows, not page reads. Use `SHOW STATUS LIKE 'Handler_%'` for handler call counts | No page-read counter exposed per statement |
| `SET STATISTICS TIME ON` | `EXPLAIN ANALYZE` includes execution time per node | Less granular than SQL Server's compile + execute split |
| Query Store — plan history, regressed queries | `slow_query_log` + Percona `pt-query-digest` — aggregates slow log into query digests with stats | No built-in plan history; no plan forcing. pt-query-digest is a separate tool |
| Query Store plan forcing (`sp_query_store_force_plan`) | No equivalent — MySQL has no plan forcing mechanism. Use index hints or query rewrites | This is a genuine MySQL gap vs SQL Server |
| Missing index DMVs (`sys.dm_db_missing_index_details`) | `sys.schema_unused_indexes` (unused indexes); no "missing index" advisor built-in. pt-query-digest surfaces slow queries for manual index analysis | No automated index recommendation |
| Extended Events / SQL Trace | Performance Schema (`performance_schema.events_statements_*`) — fine-grained but complex to query | More verbose than XE; no GUI equivalent to SSMS XE sessions |

**Critical operational difference:** MySQL has no Query Store. There is no built-in plan history, no plan forcing, and no automatic plan correction. The MySQL DBA workflow for a plan regression is: slow query log → `pt-query-digest` to identify the query → `EXPLAIN` to see the current plan → index hint or `USE INDEX` / `FORCE INDEX` to steer the optimizer → potentially rewrite the query. This is significantly more manual than the SQL Server workflow.

---

## 11. Replication and Binlog

### SQL Server HA/DR Topology → MySQL Equivalents

| SQL Server Concept | MySQL Equivalent | Key Differences |
|-------------------|-----------------|-----------------|
| Log Shipping (async, manual failover) | Async binlog replication (primary → replica, one-directional) | MySQL uses binlog events (logical or row-level); SQL Server ships log blocks (physical). Both are async with potential data loss on failover. |
| Always On AG (synchronous commit, automatic failover) | MySQL Group Replication / InnoDB Cluster (Paxos-based) | SQL Server AG uses WSFC (Windows Server Failover Cluster) as the membership/quorum layer. MySQL Group Replication is built-in Paxos — no external cluster dependency. |
| AG readable secondary (ApplicationIntent=ReadOnly) | MySQL async read replica — `ApplicationIntent` not a concept; use separate connection string to replica host | MySQL read replicas have replication lag (typically <1s on fast hardware); SQL Server synchronous AG secondaries have near-zero lag. |
| Distributed AG (async, spans regions/domains) | MySQL async replica chain or replication from replica to replica | Both are async fan-out. MySQL's equivalent is simpler operationally but lacks the listener/DNS abstraction. |
| WSFC quorum (cluster votes) | InnoDB Cluster uses MySQL Router + Group Replication Paxos quorum | No external quorum service needed in MySQL 8.0+ InnoDB Cluster. |

```
MySQL Replication Topologies
─────────────────────────────────────────────────────────────────────────────

Async Replication (SQL Server log shipping equivalent):
┌──────────────┐  binlog stream  ┌──────────────┐  ┌──────────────┐
│   Primary    │ ──────────────► │  Replica 1   │  │  Replica 2   │
│  (binlog ON) │                 │ (read-only)  │  │ (read-only)  │
└──────────────┘                 └──────────────┘  └──────────────┘
  - ROW format binlog: safest, default since 5.7
  - STATEMENT format: compact, dangerous with non-deterministic functions (NOW(), UUID())
  - Replica applies via SQL thread; lag is real and measurable
  - GTID-based: replica self-positions, no MASTER_LOG_FILE/MASTER_LOG_POS bookkeeping

Group Replication / InnoDB Cluster (SQL Server Always On AG equivalent):
┌──────────────┐   Paxos      ┌──────────────┐   ┌──────────────┐
│  Member 1    │◄────────────►│  Member 2    │◄─►│  Member 3    │
│  (primary or │  consensus   │  (secondary  │   │  (secondary  │
│   multi-prim)│              │   or primary)│   │   or primary)│
└──────────────┘              └──────────────┘   └──────────────┘
       │                             │
       └──── MySQL Router ───────────┘
             (connection routing, AG listener equivalent)

  Single-primary mode: one writer, others read-only (like SQL Server AG)
  Multi-primary mode:  all members accept writes; conflicts detected + rolled back
                       (no SQL Server AG equivalent — SQL Server AG is always single-writer)
  Quorum: majority (2 of 3, 3 of 5) — same majority quorum as SQL Server WSFC
  Difference from AG: no shared storage; each node has a full copy; no Windows dependency

Binlog Format Decision:
  STATEMENT → compact log, replicates SQL text; unsafe with: NOW(), RAND(), UUID(),
              non-deterministic stored procs — replicas may diverge silently
  ROW       → replicates actual before/after row images; larger binlog but deterministic;
              use this for any production system
  MIXED     → engine chooses STATEMENT for safe queries, ROW for unsafe — good default
              but harder to reason about
```

**GTID-based vs position-based replication:**

| | Position-based (classic) | GTID-based (MySQL 5.6+) |
|---|---|---|
| Replica positioning | Must specify `MASTER_LOG_FILE` + `MASTER_LOG_POS` | Auto — replica tracks `@@gtid_purged` |
| Failover complexity | Manual: find new primary's log position, reconfigure replicas | Automatic: `CHANGE MASTER TO MASTER_AUTO_POSITION=1` |
| Error recovery | Complex — mismatched positions cause silent divergence | Easier — GTID gaps are detectable |
| Recommendation | Legacy systems only | All new deployments |

**Key difference from SQL Server AG readable secondaries:** MySQL async replicas always have replication lag. Reads from a replica may return stale data — there is no synchronous replica in standard MySQL async replication (Group Replication single-primary mode does provide synchronous commit to a quorum, but reads from non-primary members still replay the applied log, not a live shared state). SQL Server AG with synchronous commit + ALLOW_CONNECTIONS=READ_ONLY gives you zero-lag reads. MySQL does not, unless you use AWS Aurora (shared storage layer, no lag by design).

---

## 12. Charset / Collation Gotchas

```sql
-- THE CLASSIC MISTAKE: MySQL's 'utf8' is NOT real UTF-8
-- utf8 in MySQL: 3-byte max — cannot store emoji, some CJK, supplementary characters
-- utf8mb4: true 4-byte UTF-8 — ALWAYS use this

-- Wrong (silently truncates or errors on emoji):
CREATE TABLE messages (content TEXT CHARACTER SET utf8);

-- Correct:
CREATE TABLE messages (content TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci);

-- Set at database level:
CREATE DATABASE myapp CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- Set at server level (my.cnf):
-- [mysqld]
-- character-set-server = utf8mb4
-- collation-server = utf8mb4_0900_ai_ci
```

### Collation Reference

| Collation | Behavior | Use When |
|-----------|----------|----------|
| `utf8mb4_unicode_ci` | Case+accent insensitive, Unicode 5.2 rules | Good default for MySQL 5.7 and earlier |
| `utf8mb4_0900_ai_ci` | Case+accent insensitive, Unicode 9.0 rules, faster | Default in MySQL 8.0 — use this |
| `utf8mb4_0900_as_cs` | Case+accent sensitive | Need exact case matching |
| `utf8mb4_bin` | Binary comparison | Maximum strictness, case-sensitive |

Mixing collations in a JOIN triggers implicit conversion and disables index usage — causes full scans.

---

## 13. Gotchas from T-SQL

| T-SQL Assumption | MySQL Reality |
|-----------------|---------------|
| `FULL OUTER JOIN` | Not supported — emulate with `LEFT JOIN UNION ALL RIGHT JOIN WHERE IS NULL` |
| `DATEDIFF(unit, start, end)` | MySQL `DATEDIFF(d1, d2)` returns **days only** — no unit parameter |
| `STRING_AGG(col, sep)` | MySQL: `GROUP_CONCAT(col ORDER BY col SEPARATOR ',')` |
| `[column]` quoting | MySQL uses `` `column` `` backticks |
| Brackets for reserved words | Backticks: `` `order` ``, `` `select` `` |
| `BIT` boolean | MySQL: `TINYINT(1)`; `TRUE`/`FALSE` = aliases for 1/0 |
| `DATETIME2` accuracy | MySQL `DATETIME(6)` for microseconds; default `DATETIME` = seconds only |
| `DATETIME` stores UTC | MySQL `DATETIME` stores literal — no timezone conversion. `TIMESTAMP` converts to UTC |
| Non-aggregate GROUP BY rejected | MySQL 5.6 allowed non-aggregate cols in SELECT with GROUP BY (non-ANSI). 5.7+ enforces `ONLY_FULL_GROUP_BY` |
| String + number type safety | `'123abc' = 123` evaluates TRUE — implicit coercion, dangerous in WHERE |
| `AUTO_INCREMENT` = IDENTITY | Gaps occur on rollback — never rely on continuity |
| `CROSS APPLY` | Use `LATERAL` in MySQL 8.0+ |

---

## 14. MariaDB Differences

MariaDB started as a drop-in replacement but has diverged. MySQL wire-protocol compatible for most workloads, but not 100% API-identical.

| Feature | MariaDB | MySQL |
|---------|---------|-------|
| Sync replication | Galera Cluster (synchronous multi-master) | Group Replication (Paxos-based) |
| Extra engines | Aria (crash-safe MyISAM), ColumnStore (HTAP), Spider (sharding) | InnoDB, NDB (MySQL Cluster) |
| Sequence objects | `CREATE SEQUENCE s START WITH 1 INCREMENT BY 1` | AUTO_INCREMENT only |
| System-versioned tables | Built-in temporal table syntax (SQL:2011) | No native equivalent |
| JSON | Some function naming differences from MySQL JSON | MySQL JSON (binary format, different internals) |
| PCRE regex | `REGEXP_REPLACE`, `REGEXP_SUBSTR` with Perl-compatible regex | Limited regex support |
| Thread pooling | Built-in, production-ready | Enterprise license only |
| Oracle ABI | Does not track MySQL 8.0 exactly — diverged in 10.x | Oracle-controlled |

---

## 15. Ecosystem

| Tool | Purpose |
|------|---------|
| `mysql` CLI | Official CLI client — `mysql -u root -p dbname` |
| MySQL Workbench | Official GUI: ER diagrams, visual query explain, schema designer |
| DBeaver / TablePlus / DataGrip | Cross-database GUI clients |
| Prisma | Node.js ORM with type-safe query builder, migrations |
| Drizzle | Lightweight TypeScript ORM, SQL-first |
| TypeORM / Sequelize | Node.js ORMs (older, more verbose) |
| SQLAlchemy | Python ORM — full MySQL/MariaDB support |
| Eloquent (Laravel) | PHP ORM — MySQL-native heritage |
| MySQL Connector/NET | ADO.NET driver — `MySql.Data` NuGet package |
| MySqlConnector (NuGet) | Alternative .NET driver — fully async, more active development |
| ProxySQL | Connection proxy, query routing, load balancing |
| MaxScale (MariaDB) | Smart proxy with read/write splitting |
| Percona Toolkit | DBA tools: `pt-query-digest` (slow query analysis), `pt-online-schema-change` (zero-downtime ALTER) |
| Percona XtraBackup | Hot physical backup without locking |
| Atlas / Flyway / Liquibase | Schema migration management |

---

## 16. Decision Cheat Sheet

**MySQL vs SQL Server (the axis that matters for you):**

| Choose MySQL over SQL Server when | Keep SQL Server when |
|-----------------------------------|---------------------|
| Cost/licensing is the driver — open-source GPL with no per-core licensing | You need Query Store (plan history, regression detection, plan forcing) |
| The stack is PHP/Laravel/WordPress and the team owns MySQL | Temporal tables (system-versioned, native AS OF queries) — MySQL has none |
| Deploying on AWS and want Aurora MySQL (managed, no replication ops) | Always On AG with synchronous secondary + readable replica + automatic failover |
| Read-heavy OLTP with simple query patterns, no analytics | SSRS / SSAS / Power BI integration — the BI stack is SQL Server-native |
| Linux-first deployment without Windows licensing overhead | ADO.NET / Entity Framework workloads already deeply invested in SQL Server types |
| Team is migrating away from Microsoft stack entirely | Columnstore indexes (HTAP — OLTP + analytics on same table) |
| The workload is pure OLTP with well-defined PKs and covering indexes | In-memory OLTP (Hekaton) for extreme-throughput scenarios |
| You want AWS Aurora MySQL for near-zero read replica lag at scale | Ledger tables (tamper-evident audit trail) |
| Operator expertise: team is MySQL-native and SQL Server ops is a cost | Full-text search integrated with SQL — MySQL FTS is limited vs SQL Server |

| Choose MySQL when | Choose PostgreSQL instead when |
|-------------------|-------------------------------|
| WordPress / Laravel / PHP stack | Complex analytics, JSONB queries |
| AWS Aurora (MySQL-compatible) | Extensions needed (pgvector, PostGIS) |
| Read-heavy OLTP, simple queries | Strict ANSI SQL compliance required |
| PlanetScale (global distributed) | Full OUTER JOINs are common |
| Existing MySQL operational expertise | Need advanced window/analytical functions |
| Team knows MySQL replication patterns | Geospatial (PostGIS) data |

| Choose MySQL 8.0+ when | Avoid MySQL 5.7 and earlier when |
|------------------------|----------------------------------|
| Window functions needed | CTEs are in the query patterns |
| CTEs in the codebase | Recursive queries required |
| LATERAL joins needed | utf8mb4 charset is uncertain |

---

## 17. SQL Server Developer Gotchas in MySQL

Beyond the syntax differences table, these are the conceptual traps that catch SQL Server developers.

### Schemas Are Databases — There Is No Namespace Separator

In SQL Server, schemas are namespace containers within a database: `dbo.Orders`, `sales.Orders`, `audit.Orders` — all in the same database, different schemas.

In MySQL, **databases ARE schemas**. `USE myapp;` selects the schema. There is no two-level namespace within a connection. The `information_schema` table `TABLE_SCHEMA` column contains the database name. `CREATE SCHEMA` is a synonym for `CREATE DATABASE` — they are identical.

Implication: the SQL Server pattern of organizing objects within one database into logical groups by schema does not exist in MySQL. The MySQL equivalent is separate databases, or naming conventions (`orders_`, `audit_`, etc.). This affects cross-"schema" queries: in SQL Server you `JOIN dbo.t1 ON sales.t2`; in MySQL you `JOIN db1.t1 ON db2.t2` — which means separate databases that may have separate users/permissions.

### Case Sensitivity Is Collation-Dependent — and Differs by OS

SQL Server identifier case sensitivity is always collation-dependent on the instance but defaults to case-insensitive on most Windows installs (`SQL_Latin1_General_CP1_CI_AS`). Object names (`Orders` vs `orders`) are treated as equivalent.

MySQL on Linux: **table names are file names** — the OS filesystem determines case sensitivity. On ext4/XFS (case-sensitive), `Orders` and `orders` are different tables. On macOS HFS+ (case-insensitive by default), they are the same. This is controlled by `lower_case_table_names`:
- `0` = preserve case, case-sensitive comparisons (Linux default) — `Orders` ≠ `orders`
- `1` = store lowercase, case-insensitive (Windows/macOS default) — `Orders` = `orders`
- `2` = preserve case, case-insensitive comparisons (macOS only)

**Operational trap:** Code developed on a developer's Mac (`lower_case_table_names=2`) deploys to a Linux server (`lower_case_table_names=0`) and breaks because table names were mixed-case. Always set `lower_case_table_names=1` (case-insensitive, store as lowercase) in production, and set it consistently across all environments. You cannot change this setting after database creation.

Column names are always case-insensitive in MySQL — only table/schema names are affected.

### No `DISTINCT` in Window Function Aggregates

SQL Server supports `COUNT(DISTINCT col) OVER (...)` in some contexts. MySQL 8.0+ has most window functions but does not support `DISTINCT` inside window function aggregates:

```sql
-- SQL Server: works
SELECT COUNT(DISTINCT product_id) OVER (PARTITION BY customer_id) AS distinct_products
FROM orders;

-- MySQL 8.0: ERROR — DISTINCT not supported in window function aggregates
-- Workaround: subquery or dense_rank pattern
SELECT customer_id,
       MAX(rn) OVER (PARTITION BY customer_id) AS distinct_products
FROM (
    SELECT customer_id, product_id,
           DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY product_id) AS rn
    FROM orders
) t;
```

### Stored Procedure Delimiter Syntax

MySQL stored procedures require changing the statement delimiter because the `;` inside the procedure body would be interpreted as the end of the `CREATE PROCEDURE` statement by the MySQL CLI.

```sql
-- SQL Server: no delimiter change needed
CREATE PROCEDURE dbo.MyProc
AS
BEGIN
    SELECT 1;
    SELECT 2;
END;

-- MySQL: must change delimiter before defining multi-statement procs
DELIMITER //

CREATE PROCEDURE MyProc()
BEGIN
    SELECT 1;
    SELECT 2;
END //

DELIMITER ;   -- restore normal delimiter
```

This is a client-side convention (MySQL CLI / MySQL Workbench). In application code (ADO.NET, JDBC, Python), you pass the full `CREATE PROCEDURE` body as a single string without delimiter changes — the driver handles it.

### `INFORMATION_SCHEMA` Is Slower Than SQL Server's

SQL Server's `sys.*` catalog views are fast metadata queries. MySQL's `INFORMATION_SCHEMA` is notoriously slow on large schemas because it rebuilds metadata for each query — querying `TABLES` or `COLUMNS` across a schema with thousands of tables can take seconds. Use `SHOW TABLES`, `SHOW COLUMNS FROM t`, and `SHOW INDEX FROM t` for operational metadata queries; reserve `INFORMATION_SCHEMA` for tooling/migration scripts.

### `LIMIT` Without `ORDER BY` Is Non-Deterministic

SQL Server's `TOP N` without `ORDER BY` also gives arbitrary results, but SQL Server will warn you. MySQL silently returns any N rows from the result set without guaranteeing which ones. In SQL Server, you got used to pagination with `OFFSET-FETCH` requiring `ORDER BY`. Same requirement in MySQL — `LIMIT 10 OFFSET 20` without `ORDER BY` is undefined behavior.

### No `OUTPUT` Clause — Use `LAST_INSERT_ID()`

SQL Server's `OUTPUT inserted.id` after an INSERT returns the new identity value inline. MySQL does not have an OUTPUT clause. After an INSERT with AUTO_INCREMENT, call `LAST_INSERT_ID()` to get the generated key:

```sql
INSERT INTO orders (customer_id, total) VALUES (42, 199.99);
SELECT LAST_INSERT_ID();   -- returns the new AUTO_INCREMENT id

-- In ADO.NET with MySqlConnector: connection.LastInsertedId after ExecuteNonQuery()
-- In JDBC: getGeneratedKeys() on the PreparedStatement
```

For bulk INSERTs of multiple rows, `LAST_INSERT_ID()` returns the ID of the *first* row inserted in the batch (MySQL 5.7+), not the last. Retrieve all generated IDs by knowing the first ID and the row count.

---

## 18. Common Confusion Points

**`utf8` is NOT UTF-8.** MySQL's `utf8` charset is 3-byte max. Emoji, some CJK, and supplementary Unicode characters silently fail or error. Always use `utf8mb4`. Always.

**`REPLACE INTO` is not UPSERT.** It is `DELETE` + `INSERT`. All columns not listed in the INSERT revert to `DEFAULT` or `NULL`. Auto-increment counter advances. Delete trigger fires. Use `ON DUPLICATE KEY UPDATE` instead.

**`DATEDIFF` signature is completely different.** T-SQL: `DATEDIFF(unit, start, end)`. MySQL: `DATEDIFF(date1, date2)` — returns days only, no unit argument. `DATE_ADD(date, INTERVAL 7 DAY)` for date arithmetic.

**`GROUP BY` strictness changed.** MySQL 5.6 with `ONLY_FULL_GROUP_BY` disabled allowed non-aggregate columns in SELECT — this returned arbitrary (first-found) values, not deterministic. MySQL 5.7+ defaults to strict mode (correct behavior). Code written for 5.6 lax mode will break.

**`DATETIME` vs `TIMESTAMP`:**
- `DATETIME`: stores literal date/time — no timezone awareness, no conversion. Range: 1000-01-01 to 9999-12-31.
- `TIMESTAMP`: stores UTC internally, converts to/from session timezone on read/write. Range: 1970-01-01 to 2038-01-19 (Unix epoch limit).
- New code: use `DATETIME` and handle timezone in application, or use `DATETIME(6)` + store UTC explicitly.

**`ON DUPLICATE KEY UPDATE` `VALUES()` is deprecated.** The `VALUES(col)` function inside the UPDATE clause is deprecated as of MySQL 8.0.20. Use a row alias: `INSERT INTO t AS new_row (...) VALUES (...) ON DUPLICATE KEY UPDATE col = new_row.col`.

**`AUTO_INCREMENT` guarantees uniqueness, not sequence continuity.** Gaps occur on transaction rollback, server restart (pre-8.0 behavior for in-memory counter), or failed INSERT. Do not use the PK as an externally visible sequence number if gaps are unacceptable — use a sequence table or UUID.

**`LATERAL` requires MySQL 8.0+.** The SQL Server `CROSS APPLY` / `OUTER APPLY` equivalent in MySQL is `[INNER] JOIN LATERAL` / `LEFT JOIN LATERAL`. Not available in MySQL 5.7 or MariaDB before 10.2.
