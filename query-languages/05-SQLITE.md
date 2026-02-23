# SQLite

SQLite is in every smartphone, every browser, and every Python installation. It is not a client-server database — it is a C library that reads and writes a single file. The design constraints are completely different from SQL Server: no separate server process, no network, no users/permissions, one writer at a time. But it is full SQL, ACID-compliant, and the right tool for an enormous number of use cases.

---

## Ecosystem Position

```
Database Architectures
──────────────────────────────────────────────────────────────────────────
Client-Server (SQL Server, MySQL, PostgreSQL)
  App ──[TCP/socket]──► Server process ──► OS files
  Multiple apps, concurrent writers, network access control, user auth

Embedded / Serverless (SQLite)
  App ──[in-process library call]──► OS file
  Single application, one writer, zero configuration, zero network

DuckDB (for comparison — also embedded, OLAP)
  Similar to SQLite in deployment model but columnar, analytics-first
  SQLite: OLTP row-store / DuckDB: OLAP columnar analytics

SQLite's niche: everywhere a database belongs but a server would be overkill
```

---

## 1. Dialect Snapshot

| Attribute | Value |
|-----------|-------|
| Created by | D. Richard Hipp, 2000 — originally for U.S. Navy destroyers (no server to crash) |
| License | Public domain — no copyright, no attribution required, no license to manage |
| Current version | SQLite 3.x (continuous point releases, stable ABI) |
| Architecture | Serverless, file-based, zero-config, embedded C library |
| ACID compliance | Full — WAL mode enables concurrent reads + single writer |
| Deployment surface | iOS, Android, macOS, Chrome, Firefox, Python stdlib, .NET, Node.js, R, every browser |
| Binary size | ~600KB compiled |

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Application                         │
│   Python   /   Node.js   /   C#   /   Swift   /   C        │
└────────────────────────┬────────────────────────────────────┘
                         │  in-process API call (no network)
┌────────────────────────▼────────────────────────────────────┐
│                    SQLite Library (~600KB)                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  SQL Tokenizer                                       │   │
│  │       ↓                                              │   │
│  │  Parser (LALR)                                       │   │
│  │       ↓                                              │   │
│  │  Code Generator → VDBE bytecode                      │   │
│  │       ↓                                              │   │
│  │  Virtual Machine (VDBE) — executes bytecode          │   │
│  │       ↓                                              │   │
│  │  B-Tree layer                                        │   │
│  │       ↓                                              │   │
│  │  Pager (page cache, WAL, locking)                    │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │  OS file I/O (pread/pwrite)
┌────────────────────────▼────────────────────────────────────┐
│              database.db  (single file)                     │
│    ┌──────────┬──────────┬──────────┬──────────────────┐    │
│    │ header   │ page 1   │ page 2   │ ...  │  page N   │    │
│    │ (100B)   │ B-tree   │ B-tree   │      │           │    │
│    └──────────┴──────────┴──────────┴──────────────────┘    │
│    Table data in B-tree leaf pages                          │
│    Index data in separate B-tree                            │
└─────────────────────────────────────────────────────────────┘

WAL mode adds:
  database.db-wal   (write-ahead log — pending writes)
  database.db-shm   (shared memory index for WAL)
```

---

## 3. When to Use SQLite

```
Is this a single application with a single concurrent writer?
│
├── Yes — Is the dataset > 1TB, or do many separate processes write simultaneously?
│   │
│   ├── No  → SQLite is probably the right choice ✅
│   │         Mobile app, desktop app, test harness, config storage,
│   │         edge device, CLI tool, single-user web app, prototyping
│   │
│   └── Yes → Use PostgreSQL or MySQL
│             Multi-tenant SaaS, microservices, shared data store
│
└── No (multiple unrelated processes writing concurrently)
    └── Use a client-server DB
        SQLite's WAL allows concurrent readers + one writer per file,
        but concurrent writers from separate processes serialize and contend

Sweet spots:
  Mobile apps      — iOS Core Data wraps SQLite; Android Room targets SQLite
  Desktop apps     — VS Code, Slack, Firefox, Chrome all use SQLite internally
  Test harnesses   — in-memory DB per test, zero teardown, fast
  Config / state   — ~/.config/app/state.db instead of JSON or INI
  Edge / IoT       — no server overhead, file is the deployment unit
  Data analysis    — personal-scale datasets; step up to DuckDB for analytics > a few GB
  Offline-first    — local source of truth, sync to server separately
```

---

## 4. Type System — Type Affinity

SQLite uses dynamic typing with **type affinity** — not strict column types (unless you add `STRICT`).

```
Declared column type → Storage class affinity
────────────────────────────────────────────────────────
INT, INTEGER, TINYINT, BIGINT, etc. → INTEGER affinity
REAL, FLOAT, DOUBLE                 → REAL affinity
TEXT, VARCHAR, CHAR, CLOB           → TEXT affinity
BLOB, (no type declared)            → BLOB affinity (no conversion)
NUMERIC, DECIMAL, DATE, BOOLEAN     → NUMERIC affinity (int > real > text)

SQLite storage classes (the 5 actual types):
  NULL     — null value
  INTEGER  — signed integer, 1/2/3/4/6/8 bytes (auto-sized)
  REAL     — 8-byte IEEE 754 float
  TEXT     — UTF-8 or UTF-16 string
  BLOB     — raw bytes, stored as-is
```

```sql
-- Without STRICT mode: affinity is a suggestion, not enforcement
CREATE TABLE loose (x INTEGER, y TEXT, z REAL);
INSERT INTO loose VALUES ('hello', 42, 'not a number');  -- all succeed
SELECT typeof(x), typeof(y), typeof(z) FROM loose;
-- text, integer, text  (stored as what you gave, not the declared type)

-- STRICT tables (SQLite 3.37.0, 2021): actual type enforcement
CREATE TABLE strict_t (
    id   INTEGER NOT NULL,
    name TEXT    NOT NULL,
    val  REAL
) STRICT;
INSERT INTO strict_t VALUES ('hello', 'Alice', 3.14);  -- ERROR: 'hello' is not INTEGER
INSERT INTO strict_t VALUES (1, 'Alice', '3.14');       -- ERROR: '3.14' is TEXT not REAL

-- STRICT allowed types: INT, INTEGER, REAL, TEXT, BLOB, ANY
-- ANY: accepts any storage class (flexible column in otherwise strict table)
```

Comparison behavior without STRICT: `'123' = 123` can be TRUE (coercion). Use STRICT on new tables to eliminate this class of bug.

---

## 5. WAL Mode — Enabling Concurrent Reads

```sql
-- Default mode: DELETE journal
-- Writer acquires EXCLUSIVE lock — blocks ALL readers during write
-- Bad for concurrent read workloads

-- WAL mode: Writer-Ahead Logging
-- Writers append to -wal file
-- Readers read from main db file + visible WAL entries
-- Readers and writers do NOT block each other

-- Enable WAL (persists in the db file header — set once)
PRAGMA journal_mode = WAL;
PRAGMA journal_mode;         -- check: returns 'wal'

-- WAL side files (normal, do not delete while db is open):
--   database.db-wal   — in-flight write log
--   database.db-shm   — shared memory index

-- Checkpoint: moves committed WAL entries back to main file
PRAGMA wal_checkpoint;              -- passive (non-blocking)
PRAGMA wal_checkpoint(FULL);        -- wait for all readers to finish, then checkpoint
PRAGMA wal_checkpoint(TRUNCATE);    -- FULL + truncate WAL file to zero

-- Tune checkpoint frequency
PRAGMA wal_autocheckpoint = 1000;   -- auto-checkpoint every 1000 pages (default)
```

### Critical PRAGMAs

```sql
-- Foreign key enforcement — OFF by default, must set per connection
PRAGMA foreign_keys = ON;

-- Synchronous mode
PRAGMA synchronous = FULL;     -- fsync on every write — safest (default for DELETE mode)
PRAGMA synchronous = NORMAL;   -- fsync on WAL checkpoint — good balance with WAL
PRAGMA synchronous = OFF;      -- no fsync — fastest, data loss on OS crash

-- Page cache size (negative = kibibytes)
PRAGMA cache_size = -64000;    -- 64MB page cache

-- Page size (must set before any tables are created)
PRAGMA page_size = 4096;       -- default 4096; powers of 2 from 512 to 65536

-- Temp storage
PRAGMA temp_store = MEMORY;    -- temp tables and indices in RAM

-- Analyze statistics (updates query planner)
PRAGMA optimize;               -- run ANALYZE on tables that need it (call before close)
```

---

## 6. Core Syntax Differences from T-SQL

| Operation | T-SQL | SQLite |
|-----------|-------|--------|
| Top N rows | `SELECT TOP 10 *` | `SELECT * ... LIMIT 10` |
| Top N with offset | `OFFSET 20 ROWS FETCH NEXT 10` | `LIMIT 10 OFFSET 20` |
| Identity column | `IDENTITY(1,1)` | `INTEGER PRIMARY KEY` (implicit rowid alias) |
| Auto-increment strict | `IDENTITY` (no reuse) | `INTEGER PRIMARY KEY AUTOINCREMENT` (no rowid reuse) |
| Current timestamp | `GETDATE()` | `datetime('now')` / `CURRENT_TIMESTAMP` |
| String concat | `'a' + 'b'` | `'a' \|\| 'b'` (pipe concat) |
| Date difference | `DATEDIFF(unit, s, e)` | No DATEDIFF — use `julianday()` arithmetic |
| Date add | `DATEADD(unit, n, d)` | `date('now', '+7 days')` |
| Stored procedures | Full T-SQL procs | No stored procedures (SQL only) |
| User-defined functions | T-SQL or CLR functions | Register via host language API (Python/C/etc.) |
| Boolean type | `BIT` | `INTEGER` (0/1); `TRUE`/`FALSE` = aliases |
| Identifier quoting | `[column]` | `"column"` (ANSI) or `` `column` `` (MySQL-compatible) |
| Schema prefix | `database.schema.table` | `schema.table` (ATTACH DATABASE for multi-file) |
| Permissions / users | Full grant/revoke | None — file system controls access |
| ALTER COLUMN | `ALTER TABLE t ALTER COLUMN` | NOT SUPPORTED — recreate table |
| FULL OUTER JOIN | Native | Not supported natively (3.39+ has RIGHT JOIN; emulate FULL with UNION) |

---

## 7. JSON Functions (Built-in Since 3.38)

```sql
-- JSON functions are built-in, no extension needed (SQLite 3.38+, 2022)

-- ── Extraction ──────────────────────────────────────────────────────────────
SELECT json_extract('{"user":{"name":"Alice","age":30}}', '$.user.name');
-- → 'Alice'
SELECT json_extract('[10,20,30]', '$[1]');
-- → 20

-- Shorthand -> operator (SQLite 3.38+): same as json_extract
SELECT data -> '$.user.name' FROM events;        -- returns JSON (quoted)
SELECT data ->> '$.user.name' FROM events;       -- returns text (unquoted)

-- ── Construction ────────────────────────────────────────────────────────────
SELECT json_object('name', 'Alice', 'age', 30);
-- → '{"name":"Alice","age":30}'
SELECT json_array(1, 'two', null, true);
-- → '[1,"two",null,1]'  (true → 1 in SQLite)

-- ── Modification ────────────────────────────────────────────────────────────
SELECT json_set  ('{"a":1}', '$.b', 2);          -- → '{"a":1,"b":2}'
SELECT json_insert('{"a":1}', '$.a', 99);         -- → '{"a":1}'  (won't overwrite)
SELECT json_replace('{"a":1}', '$.b', 99);        -- → '{"a":1}'  (won't insert)
SELECT json_remove('{"a":1,"b":2}', '$.b');       -- → '{"a":1}'
SELECT json_patch('{"a":1,"b":2}', '{"b":null,"c":3}'); -- RFC 7396 merge patch

-- ── Iteration ───────────────────────────────────────────────────────────────
SELECT key, value FROM json_each('{"a":1,"b":2,"c":3}');
-- rows: (a,1), (b,2), (c,3)

SELECT value FROM json_each('[10,20,30]');
-- rows: 10, 20, 30

-- json_tree: recursive walk of nested JSON
SELECT path, type, value FROM json_tree('{"a":{"b":1},"c":[2,3]}');

-- ── Validation ──────────────────────────────────────────────────────────────
SELECT json_valid('{"a":1}');     -- → 1
SELECT json_valid('bad json');    -- → 0

-- Use CHECK to enforce valid JSON on insert
CREATE TABLE events (
    id   INTEGER PRIMARY KEY,
    data TEXT NOT NULL CHECK(json_valid(data))
);
```

---

## 8. Full-Text Search — FTS5

```sql
-- FTS5 virtual table (built-in, no extension)
CREATE VIRTUAL TABLE articles_fts USING fts5(
    title,
    body,
    content='articles',       -- external content table (avoids data duplication)
    content_rowid='id'        -- rowid column in the content table
);

-- Populate from content table
INSERT INTO articles_fts(articles_fts) VALUES('rebuild');

-- Keep in sync via triggers
CREATE TRIGGER articles_ai AFTER INSERT ON articles BEGIN
    INSERT INTO articles_fts(rowid, title, body) VALUES (new.id, new.title, new.body);
END;
CREATE TRIGGER articles_ad AFTER DELETE ON articles BEGIN
    INSERT INTO articles_fts(articles_fts, rowid, title, body) VALUES('delete', old.id, old.title, old.body);
END;
CREATE TRIGGER articles_au AFTER UPDATE ON articles BEGIN
    INSERT INTO articles_fts(articles_fts, rowid, title, body) VALUES('delete', old.id, old.title, old.body);
    INSERT INTO articles_fts(rowid, title, body) VALUES (new.id, new.title, new.body);
END;

-- ── Search ──────────────────────────────────────────────────────────────────
-- Basic match
SELECT * FROM articles_fts WHERE articles_fts MATCH 'database performance';

-- Phrase search
SELECT * FROM articles_fts WHERE articles_fts MATCH '"query optimization"';

-- Boolean operators (AND, OR, NOT)
SELECT * FROM articles_fts WHERE articles_fts MATCH 'database AND (fast OR performance)';

-- Column-specific
SELECT * FROM articles_fts WHERE articles_fts MATCH 'title:postgresql body:index';

-- Prefix search
SELECT * FROM articles_fts WHERE articles_fts MATCH 'optim*';

-- ── Snippets and ranking ─────────────────────────────────────────────────────
SELECT
    snippet(articles_fts, 1, '<b>', '</b>', '...', 10) AS excerpt,
    bm25(articles_fts) AS rank
FROM articles_fts
WHERE articles_fts MATCH 'performance'
ORDER BY rank;   -- bm25() returns negative values — ORDER BY rank (asc) = most relevant first
```

---

## 9. Virtual Tables

```sql
-- Virtual tables: SQL interface over arbitrary data sources

-- ── R-Tree: geospatial proximity / bounding box queries ─────────────────────
CREATE VIRTUAL TABLE locations USING rtree(
    id,
    min_lat, max_lat,
    min_lon, max_lon
);
INSERT INTO locations VALUES (1, 40.70, 40.70, -74.01, -74.01);  -- point: min=max
SELECT id FROM locations
WHERE min_lat >= 40.0 AND max_lat <= 41.0
  AND min_lon >= -74.5 AND max_lon <= -73.5;

-- ── CSV: query CSV files as tables ──────────────────────────────────────────
CREATE VIRTUAL TABLE raw USING csv(
    filename='data.csv',
    header=YES
);
SELECT * FROM raw WHERE col1 > 100;

-- ── dbstat: page-level statistics ───────────────────────────────────────────
SELECT name, path, pageno, pagetype, ncell, payload, unused
FROM dbstat
ORDER BY name;

-- ── sqlite_schema: schema introspection (replaces sqlite_master) ─────────────
SELECT type, name, tbl_name, sql
FROM sqlite_schema
WHERE type IN ('table', 'index', 'view', 'trigger')
ORDER BY type, name;
```

---

## 10. WITHOUT ROWID Tables

```sql
-- Normal SQLite table: implicit integer rowid (64-bit) is the clustering key
-- A separate B-tree exists for each declared index (including the PK index)
-- PK lookup = PK index B-tree lookup → rowid → row data B-tree lookup (two B-trees)

-- WITHOUT ROWID: uses PRIMARY KEY as the sole clustering key
-- Data and PK are in ONE B-tree — no rowid at all
-- Analogous to SQL Server clustered index on the PK (which is also the default)

CREATE TABLE session_data (
    session_id TEXT    NOT NULL,
    key        TEXT    NOT NULL,
    value      TEXT,
    PRIMARY KEY (session_id, key)
) WITHOUT ROWID;

-- When WITHOUT ROWID wins:
--   Composite PK tables (composite PKs are awkward as secondary rowid refs anyway)
--   Tables with small rows and frequent PK lookups
--   Tables where ALL access is via PK or PK prefix

-- When to stick with normal rowid tables:
--   PK is a large blob or very long string
--   Table has many secondary indexes (secondary indexes include full PK — can be large)
--   You use sqlite_sequence or other rowid-dependent behavior
```

---

## 11. Window Functions and CTEs (SQLite 3.25+, 2018)

Syntax is ANSI-standard — identical to SQL Server and PostgreSQL.

```sql
-- Window functions (SQLite 3.25+)
SELECT
    name, dept, salary,
    ROW_NUMBER()   OVER (PARTITION BY dept ORDER BY salary DESC) AS rank,
    SUM(salary)    OVER (PARTITION BY dept)                      AS dept_total,
    AVG(salary)    OVER (PARTITION BY dept)                      AS dept_avg,
    LAG(salary, 1) OVER (ORDER BY hire_date)                     AS prev_salary,
    NTILE(4)       OVER (ORDER BY salary)                        AS quartile
FROM employees;

-- Recursive CTE: org hierarchy
WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 0 AS depth
    FROM employees
    WHERE manager_id IS NULL           -- root (CEO)
    UNION ALL
    SELECT e.id, e.name, e.manager_id, o.depth + 1
    FROM employees e
    JOIN org o ON e.manager_id = o.id
)
SELECT depth, name FROM org ORDER BY depth, name;

-- Recursive CTE: date series (no generate_series in SQLite)
WITH RECURSIVE dates(d) AS (
    SELECT '2024-01-01'
    UNION ALL
    SELECT date(d, '+1 day') FROM dates WHERE d < '2024-01-31'
)
SELECT d FROM dates;
```

---

## 12. In-Memory Databases — Testing Pattern

```python
import sqlite3

# Pure in-memory: lives only as long as the connection object
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
# Destroyed when conn is closed or GC'd — perfect for unit tests

# Shared in-memory: multiple connections to the same in-memory database
# Requires URI mode + cache=shared
conn1 = sqlite3.connect("file:testdb?mode=memory&cache=shared", uri=True)
conn2 = sqlite3.connect("file:testdb?mode=memory&cache=shared", uri=True)
# conn1 and conn2 share the same in-memory database named "testdb"
```

```csharp
// .NET / C# — Microsoft.Data.Sqlite (NuGet: Microsoft.Data.Sqlite)
// Replaces System.Data.SQLite for modern .NET

using Microsoft.Data.Sqlite;

// In-memory: perfect for unit tests, EF Core integration tests
var conn = new SqliteConnection("Data Source=:memory:");
conn.Open();

// With Entity Framework Core
services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite("Data Source=:memory:"));
// Each test class gets a fresh database — no teardown, no test isolation issues

// Shared in-memory (keep alive across connections)
var keepAlive = new SqliteConnection("Data Source=TestDb;Mode=Memory;Cache=Shared");
keepAlive.Open();  // keep this open to prevent the in-memory DB from being destroyed
```

---

## 13. Date and Time

SQLite has no native date/time type. Store as `TEXT` (ISO 8601), `INTEGER` (Unix epoch), or `REAL` (Julian day number). The built-in date functions work with all three representations.

```sql
-- Current time
SELECT datetime('now');                          -- UTC: '2024-01-15 10:30:45'
SELECT datetime('now', 'localtime');             -- Local time zone
SELECT strftime('%Y-%m-%dT%H:%M:%fZ', 'now');   -- ISO 8601 with milliseconds (e.g. '2024-01-15T10:30:45.123Z')

-- Unix epoch
SELECT unixepoch('now');                         -- integer seconds (SQLite 3.38+)
SELECT unixepoch('now', 'subsec');               -- real seconds with fractional (3.42+)
SELECT strftime('%s', 'now');                    -- also works — returns text

-- Date arithmetic (modifier strings)
SELECT date('now', '+7 days');                   -- one week forward
SELECT date('now', '-1 month');                  -- one month back
SELECT date('now', 'start of month');            -- first of current month
SELECT date('now', '-1 month', 'start of month'); -- first of prior month
SELECT date('now', 'weekday 1');                 -- next Monday

-- Components
SELECT strftime('%Y', 'now');    -- year
SELECT strftime('%m', 'now');    -- month (01-12)
SELECT strftime('%d', 'now');    -- day (01-31)
SELECT strftime('%H', 'now');    -- hour (00-23)
SELECT strftime('%W', 'now');    -- week number (00-53)

-- Date difference: no DATEDIFF — use Julian day arithmetic
SELECT CAST(julianday('now') - julianday('2024-01-01') AS INTEGER) AS days_since;

-- Comparison: ISO 8601 sorts lexicographically — range queries on TEXT dates work correctly
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'
```

---

## 14. Performance Tuning

```sql
-- Query plan inspection
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 42;
-- Good: "SEARCH orders USING INDEX idx_customer (customer_id=?)"
-- Bad:  "SCAN orders"  — full table scan, needs index

-- Full VDBE bytecode (not usually needed unless deep debugging)
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;

-- Update planner statistics
ANALYZE;              -- all tables
ANALYZE orders;       -- single table
PRAGMA optimize;      -- smart ANALYZE — only updates tables that need it (call at connection close)

-- Statistics inspection (populated by ANALYZE)
SELECT * FROM sqlite_stat1;   -- table and index stats used by query planner
```

```sql
-- Bulk insert — wrap in explicit transaction
-- Without transaction: each INSERT auto-commits (one fsync per row — catastrophically slow)
-- With transaction: 100-1000x faster on rotating disk, ~10x on SSD

BEGIN TRANSACTION;
INSERT INTO log_entries (ts, level, msg) VALUES ('2024-01-01T00:00:01Z', 'INFO', 'start');
-- ... thousands more inserts ...
COMMIT;

-- Parameterized INSERT (avoid re-parsing on every call)
-- In Python:
-- cursor.executemany("INSERT INTO t VALUES (?, ?)", data_list)

-- Check index coverage
CREATE INDEX idx_orders_customer ON orders (customer_id);
CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date);  -- covering for date range queries by customer
```

---

## 15. Common Use Patterns

```sql
-- ── App configuration storage (replaces JSON/INI) ─────────────────────────
CREATE TABLE config (
    key   TEXT PRIMARY KEY,
    value TEXT
) WITHOUT ROWID;

INSERT OR REPLACE INTO config VALUES ('theme', 'dark');
INSERT OR REPLACE INTO config VALUES ('last_sync', '2024-01-15T10:30:00Z');
SELECT value FROM config WHERE key = 'theme';

-- ── Append-only event log ────────────────────────────────────────────────────
CREATE TABLE events (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    ts         TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    event_type TEXT    NOT NULL,
    payload    TEXT    CHECK(payload IS NULL OR json_valid(payload))
);
CREATE INDEX idx_events_ts   ON events (ts);
CREATE INDEX idx_events_type ON events (event_type, ts);

INSERT INTO events (event_type, payload) VALUES ('user.login', '{"user_id":42,"ip":"1.2.3.4"}');

-- ── Session store ────────────────────────────────────────────────────────────
CREATE TABLE sessions (
    id         TEXT    PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    data       TEXT    CHECK(json_valid(data)),
    created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    expires_at TEXT    NOT NULL
) WITHOUT ROWID;

CREATE INDEX idx_sessions_user    ON sessions (user_id);
CREATE INDEX idx_sessions_expires ON sessions (expires_at);

-- Expiry cleanup (run periodically)
DELETE FROM sessions WHERE expires_at < strftime('%Y-%m-%dT%H:%M:%fZ', 'now');

-- ── Upsert pattern ────────────────────────────────────────────────────────────
INSERT INTO user_prefs (user_id, key, value)
VALUES (42, 'theme', 'dark')
ON CONFLICT (user_id, key) DO UPDATE SET value = excluded.value;
-- 'excluded' references the proposed-insert row (ANSI syntax, same as PostgreSQL)
```

---

## 16. Gotchas from T-SQL

| T-SQL Assumption | SQLite Reality |
|-----------------|----------------|
| `ALTER TABLE t ALTER COLUMN` | NOT SUPPORTED in SQLite. Workaround: `CREATE TABLE t_new (...); INSERT INTO t_new SELECT ...; DROP TABLE t; ALTER TABLE t_new RENAME TO t;` (or use `pragma writable_schema` — avoid) |
| FK constraints enforced | `PRAGMA foreign_keys = OFF` by default. Must `SET PRAGMA foreign_keys = ON` per connection |
| `DATEDIFF(unit, start, end)` | No `DATEDIFF`. Use `julianday(d1) - julianday(d2)` for days |
| `DATEADD(unit, n, date)` | No `DATEADD`. Use `date(d, '+7 days')` / `datetime(d, '+1 hour')` |
| Stored procedures | No stored procedures. Logic lives in application code |
| User permissions / GRANT | No permission system. File system ACLs are the only access control |
| `FULL OUTER JOIN` | Not supported. Emulate with `LEFT JOIN UNION ALL LEFT JOIN with tables swapped WHERE first_table.id IS NULL` |
| `IDENTITY` reuses no values | `INTEGER PRIMARY KEY` reuses deleted max rowid. Add `AUTOINCREMENT` to prevent reuse (slower, rarely needed) |
| Type-safe columns | Dynamic typing by default — `'hello'` inserts into `INTEGER` column without error. Use `STRICT` tables (3.37+) |
| `BOOLEAN` type | Stored as `INTEGER` — 0 is false, 1 is true. `TRUE`/`FALSE` are aliases |
| Multiple databases per connection | SQLite opens one file per connection; use `ATTACH DATABASE 'other.db' AS other` for cross-file queries |

---

## 17. Decision Cheat Sheet

| Use SQLite when | Do NOT use SQLite when |
|-----------------|------------------------|
| Single application, single writer | Multiple unrelated processes writing concurrently |
| Mobile app local storage | Need fine-grained user/role permissions |
| Desktop application state | Horizontal scaling or replication required |
| Unit/integration test harness | High-throughput concurrent write workloads |
| < ~35GB local data file | Dataset exceeds local storage capacity |
| Offline-first with sync-to-server | Need stored procedures or server-side triggers at scale |
| Config / cache / queue / log storage | Need complex user-defined functions in pure SQL |
| Prototyping (zero setup) | Network-accessible shared database required |
| IoT / edge / embedded devices | HTAP or analytics workloads > a few GB (use DuckDB instead) |

---

## 18. Common Confusion Points

**SQLite is not "lite" in features.** Full SQL, full ACID, full window functions, CTEs, JSON, FTS5, R-Tree. The "lite" is in deployment complexity — no server, no config, no users. Used inside Firefox, Chrome, iOS, Android, macOS.

**`INTEGER PRIMARY KEY` vs `AUTOINCREMENT`.** `INTEGER PRIMARY KEY` is an alias for `rowid`. SQLite picks the next rowid as `max(rowid) + 1`. Deleted max rowid slots can be reused after the table is emptied and repopulated. `AUTOINCREMENT` adds a check against `sqlite_sequence` to guarantee never reusing a previous max — slightly slower, rarely actually needed.

**Transactions are mandatory for bulk inserts.** Without an explicit transaction, every single `INSERT` is auto-committed with its own `fsync`. On mechanical disk: single-digit inserts/second. With an explicit `BEGIN`/`COMMIT`: 50,000-500,000 inserts/second.

**Foreign keys are OFF by default — every connection.** This is for backward compatibility with legacy databases that have invalid FK data. Set `PRAGMA foreign_keys = ON` in your connection setup code. It is not a global setting; it must be set each time a connection opens.

**WAL side files are normal.** `database.db-wal` and `database.db-shm` appear in WAL mode. They are part of the database — do not delete them while the database is open. They are incorporated back into the main file at checkpoint or connection close.

**No RIGHT JOIN before SQLite 3.39 (2022).** Older SQLite (common in system Python, older mobile OS versions) has no `RIGHT JOIN`. Check the SQLite version in your runtime: `SELECT sqlite_version()`.

**STRICT mode is new and not in old tutorials.** SQLite 3.37 (2021) added `STRICT` table creation. Documentation written before 2022 won't mention it. Add `STRICT` to all new table definitions to get sane type enforcement.

**Type affinity with comparisons.** Without `STRICT`, `WHERE id = '42'` where `id` is `INTEGER` affinity works — SQLite coerces `'42'` to `42`. But `WHERE id = '42abc'` does not coerce — it compares text `'42abc'` against integer `42` as different types and returns false. The coercion rules are in the SQLite spec but non-obvious. `STRICT` eliminates this class of issue.

**No network protocol.** There is no host/port/password to configure. The database is a file. Two separate machines cannot share the same SQLite database over a network share (concurrent writes over NFS/SMB are unsafe — file locking is unreliable over network file systems). For networked use, use a client-server database.
