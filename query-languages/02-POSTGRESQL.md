# PostgreSQL

PostgreSQL is the de facto standard for open-source relational databases. It extends ANSI SQL more aggressively than any other RDBMS. If you're coming from SQL Server, the syntax is 90% the same — the gaps are mostly in proprietary T-SQL extensions vs PostgreSQL extensions.

---

## DIALECT SNAPSHOT

| Attribute | Value |
|-----------|-------|
| Origin | UC Berkeley POSTGRES (1986) → PostgreSQL (1996) |
| License | PostgreSQL License (MIT-like, permissive) |
| Current version | PostgreSQL 17 (September 2024) |
| ACID compliance | Full |
| Isolation model | MVCC — readers never block writers; no dirty reads possible |
| Strengths | JSONB, full-text search, extensions ecosystem, standards compliance, complex queries |
| Weaknesses | Write scaling vs NoSQL; no built-in sharding (Citus extension adds it) |
| Cloud managed | AWS RDS/Aurora, Google Cloud SQL/AlloyDB, Azure Database for PostgreSQL, Supabase, Neon |

---

## LANDSCAPE

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         PostgreSQL Feature Surface                       │
├─────────────────────────────────────────────────────────────────────────┤
│  RELATIONAL CORE         │  EXTENDED TYPES           │  SEARCH           │
│  ─────────────────────── │  ────────────────────────  │  ─────────────── │
│  ANSI SQL (very strict)  │  JSONB (binary JSON)       │  tsvector/tsquery │
│  CTEs (WITH)             │  Arrays (multi-dim)        │  GIN indexes      │
│  Window functions        │  hstore (k/v)              │  pg_trgm (fuzzy)  │
│  LATERAL JOINs           │  Range types               │                   │
│  RETURNING clause        │  Custom types / domains    │  EXTENSIONS       │
│  FILTER on aggregates    │  Composite types           │  ─────────────── │
│  NAMED WINDOWS           │  Enum types                │  pgvector (AI)    │
│                          │                            │  PostGIS (geo)    │
│  PARTITIONING            │  INDEXING                  │  TimescaleDB      │
│  ─────────────────────── │  ────────────────────────  │  pg_cron          │
│  Range / List / Hash     │  B-Tree (default)          │  pg_partman       │
│  Declarative (PG 10+)    │  GIN (JSONB, arrays, FTS)  │  pg_stat_stmts    │
│  Partition pruning       │  GiST (geo, ranges)        │                   │
│  Cross-partition queries │  BRIN (time-series)        │                   │
│                          │  Hash (equality only)      │                   │
├─────────────────────────────────────────────────────────────────────────┤
│  PROCEDURAL              │  SECURITY                  │  REPLICATION      │
│  PL/pgSQL, PL/Python     │  Row-Level Security (RLS)  │  Streaming (WAL)  │
│  PL/V8 (JavaScript)      │  Column-level privileges   │  Logical decoding │
│  Custom aggregates       │  pg_crypto                 │  Logical replica  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## CORE SYNTAX: T-SQL vs PostgreSQL

Side-by-side for every common divergence from your T-SQL muscle memory.

| Operation | T-SQL (SQL Server) | PostgreSQL |
|-----------|-------------------|------------|
| String concatenation | `'a' + 'b'` | `'a' \|\| 'b'` or `concat('a','b')` |
| Limit rows | `SELECT TOP 10 ...` | `SELECT ... LIMIT 10` |
| Current timestamp | `GETDATE()` | `NOW()` or `CURRENT_TIMESTAMP` |
| NULL coalesce | `ISNULL(x, 0)` | `COALESCE(x, 0)` (also works in T-SQL) |
| Date difference | `DATEDIFF(day, d1, d2)` | `(d2 - d1)` or `EXTRACT(epoch FROM d2-d1)` |
| Date parts | `DATEPART(year, d)` | `EXTRACT(year FROM d)` or `date_part('year', d)` |
| Type cast | `CONVERT(INT, x)` or `CAST(x AS INT)` | `CAST(x AS INT)` or `x::INT` (shorthand) |
| Auto-increment | `IDENTITY(1,1)` | `GENERATED ALWAYS AS IDENTITY` or `SERIAL` (old) |
| String length | `LEN(str)` | `LENGTH(str)` or `char_length(str)` |
| Find in string | `CHARINDEX('x', str)` | `POSITION('x' IN str)` or `strpos(str, 'x')` |
| Substring | `SUBSTRING(str, 1, 5)` | `substring(str, 1, 5)` — identical |
| Unlimited string | `VARCHAR(MAX)` | `TEXT` (no length limit, same storage) |
| Temp table | `#temp_name` | `CREATE TEMP TABLE temp_name (...)` |
| Table variable | `DECLARE @t TABLE (...)` | CTE or `CREATE TEMP TABLE` |
| Dynamic SQL | `EXEC sp_executesql @sql, @params` | `EXECUTE format(...)` or `EXECUTE sql_string` |
| Unicode string | `NVARCHAR` | `TEXT` or `VARCHAR` — always UTF-8 |
| Dirty read hint | `WITH(NOLOCK)` | No equivalent — MVCC prevents dirty reads |
| Correlated subquery in FROM | `CROSS APPLY` | `JOIN LATERAL ... ON TRUE` |
| Left outer correlated | `OUTER APPLY` | `LEFT JOIN LATERAL ... ON TRUE` |
| Rows to XML/JSON | `FOR XML PATH` | `json_agg()`, `array_agg()`, `jsonb_build_object()` |
| Boolean literals | `1` / `0` (context-dependent) | `TRUE` / `FALSE` |
| Schema default | `dbo` | `public` |

---

## JSONB — The Killer Feature

PostgreSQL's JSONB stores parsed binary JSON with full operator support and GIN indexing. This is not the watered-down JSON support in SQL Server 2016 — it's a first-class type.

```sql
-- JSONB (binary) vs JSON (text): always use JSONB
-- JSON preserves whitespace and key order. JSONB parses on insert, enables operators/indexes.
CREATE TABLE events (
    id      BIGSERIAL PRIMARY KEY,
    payload JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ── EXTRACTION OPERATORS ─────────────────────────────────────────────────
payload -> 'user'                -- returns JSONB (object or array)
payload ->> 'user'               -- returns TEXT (scalar; cast for math)
payload -> 'user' -> 'name'      -- chain for nested objects
payload #> '{user,name}'         -- path array → JSONB
payload #>> '{user,name}'        -- path array → TEXT

-- ── CONTAINMENT (highly indexable with GIN) ──────────────────────────────
payload @> '{"status": "active"}'     -- payload contains this JSON fragment
'{"a":1}' <@ payload                  -- left-contained-by-right

-- ── KEY EXISTENCE ────────────────────────────────────────────────────────
payload ? 'email'                -- key exists at top level
payload ?| ARRAY['email','phone']-- any of these keys exist
payload ?& ARRAY['email','phone']-- all of these keys exist

-- ── MODIFICATION (returns new JSONB — JSONB is immutable) ────────────────
payload || '{"processed": true}'             -- merge objects
payload - 'sensitive_field'                  -- remove key
payload #- '{nested,key}'                    -- remove nested key
jsonb_set(payload, '{user,name}', '"Alice"') -- set value at path

-- ── INDEXES ──────────────────────────────────────────────────────────────
-- GIN: supports @>, ?, ?|, ?& operators — the containment/existence operators
CREATE INDEX idx_events_payload ON events USING GIN (payload);

-- Partial GIN on a sub-object
CREATE INDEX idx_events_user ON events USING GIN ((payload -> 'user'));

-- B-tree on extracted scalar (for =, <, > comparisons on a known field)
CREATE INDEX idx_events_user_id ON events ((payload ->> 'user_id'));

-- ── QUERYING ─────────────────────────────────────────────────────────────
SELECT payload ->> 'user_id'       AS user_id,
       payload #>> '{meta,source}' AS source
FROM   events
WHERE  payload @> '{"type": "purchase"}'     -- uses GIN index
  AND  (payload ->> 'amount')::numeric > 100; -- cast TEXT → numeric for comparison

-- ── JSON AGGREGATION ─────────────────────────────────────────────────────
SELECT user_id,
       jsonb_agg(payload ORDER BY created_at) AS all_events,
       jsonb_object_agg(payload->>'event_type', payload->>'value') AS by_type
FROM   events
GROUP BY user_id;

-- ── EXPANDING JSONB ARRAY TO ROWS ────────────────────────────────────────
SELECT id, elem
FROM   events, jsonb_array_elements(payload->'tags') AS elem;
```

**Key gotcha:** `->>` always returns `TEXT`. Cast explicitly for any numeric/date comparison.

---

## ARRAYS

Native array types — not JSON arrays, actual typed arrays with operators and indexes.

```sql
CREATE TABLE articles (
    id    SERIAL PRIMARY KEY,
    title TEXT,
    tags  TEXT[],              -- 1-D text array
    scores INT[]               -- 1-D integer array
);

INSERT INTO articles (title, tags)
VALUES ('Postgres rocks', ARRAY['postgresql', 'database', 'sql']);
-- Alternative literal syntax:
INSERT INTO articles (title, tags) VALUES ('Redis intro', '{"redis","cache"}');

-- ── ARRAY OPERATORS ──────────────────────────────────────────────────────
WHERE 'postgresql' = ANY(tags)          -- element membership (most common)
WHERE tags @> ARRAY['sql']              -- array contains element(s)
WHERE tags && ARRAY['sql','cache']      -- arrays overlap (any element in common)
WHERE cardinality(tags) > 2             -- element count (PG 9.4+; use array_length before)
WHERE array_length(tags, 1) > 2         -- array_length(arr, dimension)

-- IMPORTANT: Arrays are 1-indexed. arr[1] is the first element.

-- ── ARRAY AGGREGATION ────────────────────────────────────────────────────
SELECT user_id,
       array_agg(tag ORDER BY tag)   AS sorted_tags,
       array_agg(DISTINCT tag)       AS unique_tags
FROM   user_tags
GROUP BY user_id;

-- ── UNNEST: explode array to rows ─────────────────────────────────────────
SELECT id, unnest(tags) AS tag FROM articles;

-- WITH ORDINALITY: keep position index
SELECT id, tag, ord
FROM   articles,
       unnest(tags) WITH ORDINALITY AS t(tag, ord);
-- Returns: (1, 'postgresql', 1), (1, 'database', 2), (1, 'sql', 3)

-- ── ARRAY CONSTRUCTION ───────────────────────────────────────────────────
SELECT ARRAY(SELECT name FROM users WHERE active)  -- subquery → array
SELECT ARRAY[1, 2, 3] || ARRAY[4, 5]              -- concatenation
SELECT tags[1:2] FROM articles                      -- slice (1-indexed)
```

---

## FULL-TEXT SEARCH

Built-in, no external engine required — viable up to tens of millions of rows.

**SQL Server FTS → PostgreSQL bridge:**
```
SQL Server full-text search                  PostgreSQL full-text search
─────────────────────────────────────────    ──────────────────────────────────────────
Full-Text Catalog (separate storage)         tsvector column (stored in the table itself)
Full-Text Index (managed by FTS engine)      GIN index on the tsvector column

CONTAINS(col, 'term')                        col @@ to_tsquery('term')
FREETEXT(col, 'phrase match')                col @@ plainto_tsquery('phrase match')
FREETEXTTABLE(t, col, 'phrase')              ... ORDER BY ts_rank(vec, query) DESC
CONTAINSTABLE(t, col, 'NEAR(a,b)')           col @@ to_tsquery('a <-> b')  (phrase/proximity)

CREATE FULLTEXT INDEX ON articles(title,body) ALTER TABLE ... ADD COLUMN search_vec TSVECTOR
  KEY INDEX pk_articles                          GENERATED ALWAYS AS (
  ON ft_catalog;                                   setweight(to_tsvector('english', title), 'A') ||
                                                   setweight(to_tsvector('english', body), 'B')
                                                 ) STORED;
                                               CREATE INDEX ON articles USING GIN (search_vec);

Stemming / stopwords: controlled by the       Controlled by the TEXT SEARCH CONFIGURATION
Full-Text Catalog language settings           (default: 'english' — configurable per column)

SQL Server keeps the FTS index in a           PostgreSQL: tsvector lives in your table,
separate catalog; schema changes can          GIN index lives alongside it — no separate
desync the catalog from the table.            catalog to manage or rebuild.

Ranking: RANK() column in CONTAINSTABLE       ts_rank(vec, query) — returns float, ORDER BY it
```

```sql
-- tsvector: preprocessed document (stemmed, stopwords removed, lexeme positions)
-- tsquery:  search query with operators: & (AND), | (OR), ! (NOT), <-> (phrase/proximity)

-- One-off test
SELECT to_tsvector('english', 'PostgreSQL databases are fast and reliable') @@
       to_tsquery('english', 'postgresql & fast');  -- TRUE

-- ── GENERATED STORED COLUMN (preferred pattern) ───────────────────────────
ALTER TABLE articles
    ADD COLUMN search_vector TSVECTOR
        GENERATED ALWAYS AS (
            setweight(to_tsvector('english', COALESCE(title, '')),  'A') ||
            setweight(to_tsvector('english', COALESCE(body,  '')),  'B')
        ) STORED;

CREATE INDEX idx_articles_fts ON articles USING GIN (search_vector);

-- ── QUERY WITH RANKING ────────────────────────────────────────────────────
SELECT
    title,
    ts_rank(search_vector, query)    AS rank,       -- frequency-based rank
    ts_headline('english', body, query,             -- highlighted excerpt
                'MaxWords=30, MinWords=15') AS snippet
FROM
    articles,
    to_tsquery('english', 'database & performance') AS query
WHERE
    search_vector @@ query
ORDER BY rank DESC
LIMIT 20;

-- ── PHRASE SEARCH (proximity operators) ──────────────────────────────────
to_tsquery('english', 'query <-> performance')   -- immediately adjacent
to_tsquery('english', 'query <2> performance')   -- exactly 2 words apart
to_tsquery('english', 'query <-> plan | query <-> optimizer')

-- ── WEBSEARCH SYNTAX (PG 11+) ─────────────────────────────────────────────
websearch_to_tsquery('english', 'database performance -slow')
-- more forgiving than to_tsquery; handles quoted phrases, - negation
```

---

## LATERAL JOINS (= CROSS APPLY / OUTER APPLY)

`LATERAL` is the ANSI standard; T-SQL calls it `APPLY`. Semantically identical.

```sql
-- ── CROSS APPLY equivalent: inner lateral ─────────────────────────────────
SELECT c.name, o.order_date, o.total
FROM   customers c
JOIN LATERAL (
    SELECT order_date, total
    FROM   orders
    WHERE  customer_id = c.id        -- correlates to outer row
    ORDER BY order_date DESC
    LIMIT 3
) o ON TRUE;

-- ── OUTER APPLY equivalent: left join lateral ─────────────────────────────
-- Keeps customers even if no matching orders
SELECT c.name, o.order_date
FROM   customers c
LEFT JOIN LATERAL (
    SELECT order_date
    FROM   orders
    WHERE  customer_id = c.id
    ORDER BY order_date DESC
    LIMIT 1
) o ON TRUE;

-- ── LATERAL with function ─────────────────────────────────────────────────
SELECT e.name, stats.avg_salary
FROM   employees e
JOIN LATERAL fn_dept_stats(e.department_id) AS stats ON TRUE;

-- ── LATERAL with UNNEST (very common pattern) ─────────────────────────────
SELECT u.id, pref
FROM   users u,
       LATERAL unnest(u.preferences) AS pref;
-- Implicit LATERAL: comma-separated FROM items can reference left side directly
```

---

## RETURNING CLAUSE

Get rows back from DML without a separate SELECT. Simpler syntax than T-SQL's `OUTPUT`.

```sql
-- INSERT ... RETURNING
INSERT INTO orders (customer_id, total, status)
VALUES (42, 199.99, 'pending')
RETURNING id, created_at, status;
-- Returns the newly inserted row immediately — no separate SELECT needed

-- UPDATE ... RETURNING (new values by default)
UPDATE products
SET    price = price * 1.1
WHERE  category = 'electronics'
RETURNING id, name, price AS new_price;

-- To get OLD values in UPDATE, capture in a CTE:
WITH updated AS (
    UPDATE products SET price = price * 1.1
    WHERE category = 'electronics'
    RETURNING id, name, price
)
SELECT * FROM updated;
-- Note: price in RETURNING shows the NEW value; no deleted.price like T-SQL OUTPUT

-- DELETE ... RETURNING
DELETE FROM sessions
WHERE  expires_at < NOW()
RETURNING user_id, session_token, expires_at;
```

**T-SQL bridge:** Equivalent to `OUTPUT inserted.*` / `OUTPUT deleted.*` but without the `INTO @table` requirement. PostgreSQL returns a result set directly.

---

## WINDOW FUNCTIONS — PostgreSQL Additions

Full ANSI window functions plus two PostgreSQL-specific extensions.

```sql
-- ── NAMED WINDOWS: define once, reference multiple times ──────────────────
SELECT
    id, dept, salary,
    AVG(salary) OVER w          AS dept_avg,
    RANK()      OVER w          AS dept_rank,
    NTILE(4)    OVER w          AS dept_quartile
FROM employees
WINDOW w AS (PARTITION BY dept ORDER BY salary DESC);
-- T-SQL requires repeating the full OVER() clause each time

-- ── FILTER CLAUSE on aggregates (PG 9.4+) ────────────────────────────────
-- Applies a WHERE condition to the aggregate without a CASE expression
SELECT dept,
       COUNT(*)                              AS total,
       COUNT(*) FILTER (WHERE status = 'active')   AS active_count,
       AVG(salary) FILTER (WHERE level > 3)         AS senior_avg_salary
FROM employees
GROUP BY dept;
-- T-SQL equivalent: SUM(CASE WHEN status='active' THEN 1 ELSE 0 END)
```

---

## MATERIALIZED VIEWS

Stored query results — fast reads, point-in-time data. Not in T-SQL (indexed views are different).

```sql
-- Create
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT
    date_trunc('month', order_date) AS month,
    SUM(total)                      AS revenue,
    COUNT(*)                        AS order_count
FROM   orders
GROUP BY 1;

-- Refresh blocks reads until complete
REFRESH MATERIALIZED VIEW monthly_sales;

-- Refresh CONCURRENTLY: no read lock, but requires a unique index
CREATE UNIQUE INDEX ON monthly_sales (month);
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales;
-- Computes new data in background, swaps atomically — safe for live production

-- Query just like a table
SELECT * FROM monthly_sales WHERE month >= '2024-01-01';
```

**T-SQL bridge:** SQL Server indexed views are auto-maintained synchronously. Materialized views are manually refreshed — you control when (via pg_cron for scheduling).

---

## EXPLAIN ANALYZE

Reading query plans is the same diagnostic skill as SQL Server execution plans, different vocabulary.

**SSMS execution plan → EXPLAIN ANALYZE bridge:**
```
SQL Server (SSMS graphical plan)              PostgreSQL (EXPLAIN ANALYZE text/JSON)
─────────────────────────────────────────    ──────────────────────────────────────────
Clustered Index Seek                          Index Scan
Clustered Index Scan                          Seq Scan (if full scan) or Index Scan
Nonclustered Index Seek                       Index Scan
Nonclustered Index Scan                       Seq Scan or Bitmap Index Scan
Key Lookup (RID Lookup)                       (second) Index Scan or Bitmap Heap Scan
Table Scan                                    Seq Scan
Hash Match (aggregate)                        Hash Aggregate
Hash Match (join)                             Hash Join
Nested Loops                                  Nested Loop
Merge Join                                    Merge Join
Sort                                          Sort
Parallelism (Gather Streams)                  Gather / Gather Merge
Compute Scalar                                (inlined into parent node cost)
Filter                                        Filter (explicit node if not pushed down)

Actual / Estimated rows:                      actual rows vs rows estimate
  shown as "Estimated Rows" tooltip             (large gap → ANALYZE needed)

SET STATISTICS IO ON                          EXPLAIN (ANALYZE, BUFFERS)
  logical reads / physical reads               Buffers: hit=N read=N

Query Store: query_store_runtime_stats        pg_stat_statements (extension)
  avg_duration, total_worker_time              mean_exec_time, total_exec_time

Estimated Subtree Cost                        cost=X..Y  (relative units, not ms)

COST MODEL DIFFERENCE:
  SQL Server: costs in estimated CPU + I/O units, calibrated to real hardware
  PostgreSQL: costs in abstract "page fetch" units
    seq_page_cost   = 1.0  (baseline — sequential page read)
    random_page_cost = 4.0  (random page read costs 4× sequential by default)
    cpu_tuple_cost   = 0.01 (per-row CPU cost)
  On SSDs: lower random_page_cost to 1.1–2.0 to reduce over-weighting of sequential scans.
  The absolute numbers are meaningless; relative costs within a plan matter.

QUERY STORE EQUIVALENT:
  SQL Server: Query Store built-in, accessible via SSMS
  PostgreSQL: pg_stat_statements extension — CREATE EXTENSION pg_stat_statements;
    SELECT query, calls, mean_exec_time, total_exec_time, rows
    FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 20;

  auto_explain extension: logs slow query plans automatically (like Query Store capture):
    SET auto_explain.log_min_duration = 1000;   -- log plans for queries > 1s
    SET auto_explain.log_analyze = on;
```

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE customer_id = 42 AND status = 'pending';
-- ANALYZE: actually runs the query, shows actual vs estimated rows
-- BUFFERS: shows cache hits vs disk reads
-- FORMAT JSON available for tooling consumption
```

### Plan Node Reference

| Node | Meaning | When to worry |
|------|---------|---------------|
| `Seq Scan` | Full table scan | Missing index, or table is small (fine) |
| `Index Scan` | Index lookup + heap fetch per row | Good for low selectivity |
| `Index Only Scan` | All needed cols in index — no heap | Best case |
| `Bitmap Heap Scan` | Batches index hits, then heap | Moderate selectivity — normal |
| `Hash Join` | Builds hash table on smaller side | Good for large unsorted inputs |
| `Merge Join` | Both sides sorted, zipper merge | Good when inputs pre-sorted |
| `Nested Loop` | Outer × inner row | Best when inner side is tiny/indexed |

### Key Numbers

| Field | What it means | Action if wrong |
|-------|--------------|----------------|
| `actual rows` vs `rows` estimate | Large gap = stale stats | `ANALYZE table_name` |
| `actual time=X..Y` | X = first row ms, Y = last row ms | High Y = full scan |
| `Buffers: hit=N` | Pages served from shared_buffers | More hits = better |
| `Buffers: read=N` | Pages read from disk | High = cache miss |

```sql
-- Force stats refresh (usually handled by autovacuum, but can force)
ANALYZE orders;
VACUUM ANALYZE orders;  -- also reclaims dead tuples from MVCC
```

---

## VACUUM AND AUTOVACUUM

**No SQL Server equivalent — this is a genuine operational difference.**

PostgreSQL's MVCC model keeps old row versions ("dead tuples") in the heap after UPDATE or DELETE.
Readers need those old versions for snapshot isolation. VACUUM reclaims the space once no
transaction needs the old versions anymore.

```
WHY DEAD TUPLES EXIST (MVCC model):

  UPDATE employees SET salary = 110000 WHERE id = 42;

  Before:  heap page contains:
    tuple (xmin=100, xmax=0,   id=42, salary=100000)  ← visible to all txns after 100

  After:   heap page contains BOTH:
    tuple (xmin=100, xmax=500, id=42, salary=100000)  ← dead (deleted by txn 500)
    tuple (xmin=500, xmax=0,   id=42, salary=110000)  ← live (inserted by txn 500)

  The dead tuple stays in the page until VACUUM reclaims it.
  A table with heavy UPDATE/DELETE traffic accumulates dead tuples → table bloat.

SQL Server comparison:
  SQL Server (with RCSI / READ_COMMITTED_SNAPSHOT) keeps old row versions in tempdb.
  Old versions are discarded from tempdb when no active snapshot needs them.
  No per-table maintenance required — tempdb cleanup is automatic.
  PostgreSQL keeps old versions in the table itself → requires per-table maintenance.
```

### VACUUM vs VACUUM FULL vs VACUUM ANALYZE

```
┌──────────────────┬──────────────────────────────────────────┬────────────────────────┐
│ Command          │ What it does                             │ Lock acquired          │
├──────────────────┼──────────────────────────────────────────┼────────────────────────┤
│ VACUUM t         │ Marks dead tuples as reusable space.      │ ShareUpdateExclusive   │
│                  │ Does NOT return space to OS.              │ (non-blocking — normal │
│                  │ Updates visibility map. Updates freeze    │ reads/writes continue) │
│                  │ map. Updates pg_class.relpages stats.     │                        │
├──────────────────┼──────────────────────────────────────────┼────────────────────────┤
│ VACUUM FULL t    │ Rewrites the entire table to a new file.  │ ACCESS EXCLUSIVE       │
│                  │ Returns space to OS. Equivalent to        │ (table fully locked — │
│                  │ REBUILD on a SQL Server table.            │ blocks all queries)    │
│                  │ Use after extreme bloat only.             │                        │
├──────────────────┼──────────────────────────────────────────┼────────────────────────┤
│ VACUUM ANALYZE t │ VACUUM + updates planner statistics       │ ShareUpdateExclusive   │
│                  │ (same as running ANALYZE separately).     │ (non-blocking)         │
├──────────────────┼──────────────────────────────────────────┼────────────────────────┤
│ ANALYZE t        │ Updates planner statistics only.          │ ShareUpdateExclusive   │
│                  │ No dead tuple reclaim.                    │ (non-blocking)         │
└──────────────────┴──────────────────────────────────────────┴────────────────────────┘

VACUUM FULL is rarely the right answer:
  - It holds an exclusive lock for the duration (minutes on large tables)
  - Use pg_repack extension instead: rewrites table online, minimal locking
  - Or: if you can afford a maintenance window, VACUUM FULL is fine
```

### Visibility Map and Freeze Map

```
VISIBILITY MAP (one bit per heap page):
  If a page's bit is set → all tuples on that page are visible to all active transactions.
  VACUUM can skip scanning fully-visible pages → much faster VACUUM on stable data.
  Index Only Scans check the visibility map to avoid heap fetches.

FREEZE MAP (a second bit per heap page):
  Transaction IDs are 32-bit integers — they wrap around after ~2 billion transactions.
  "Frozen" tuples have their XID replaced with a special FrozenTransactionId constant,
  making them permanently visible regardless of XID wrap-around.

  VACUUM freezes old tuples automatically.
  If autovacuum doesn't keep up, PostgreSQL forces an aggressive VACUUM before XID
  approaches the wraparound horizon (default: vacuum_freeze_min_age = 50M txns before now).

  XID wraparound catastrophe: if a table is never vacuumed and the XID counter wraps,
  PostgreSQL will refuse to accept new transactions and set the DB to read-only.
  This is an operational emergency with no SQL Server analog — your monitoring must
  track pg_database.datfrozenxid age.
```

### Autovacuum

Autovacuum runs VACUUM and ANALYZE automatically based on table activity thresholds.

```sql
-- Check autovacuum activity on your tables
SELECT
    schemaname,
    relname,
    n_dead_tup,
    n_live_tup,
    ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 1) AS dead_pct,
    last_autovacuum,
    last_autoanalyze
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC
LIMIT 20;
```

**Key autovacuum tunables** (set per-table via `ALTER TABLE ... SET (...)` or globally in `postgresql.conf`):

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `autovacuum_vacuum_scale_factor` | 0.2 (20%) | Trigger VACUUM when dead tuples exceed 20% of live tuples |
| `autovacuum_vacuum_threshold` | 50 | Minimum dead tuples before scale_factor kicks in |
| `autovacuum_analyze_scale_factor` | 0.1 (10%) | Trigger ANALYZE when modified rows exceed 10% |
| `autovacuum_analyze_threshold` | 50 | Minimum modified rows before analyze triggers |
| `autovacuum_vacuum_cost_limit` | 200 | Throttle: cost units autovacuum can use before sleeping |
| `autovacuum_vacuum_cost_delay` | 2ms | Sleep duration between cost-limit bursts |

```sql
-- Override autovacuum settings per table (large, high-churn tables need aggressive settings)
ALTER TABLE orders SET (
    autovacuum_vacuum_scale_factor = 0.01,   -- trigger at 1% dead tuples (not 20%)
    autovacuum_vacuum_threshold = 100        -- minimum 100 dead tuples
);

-- Check if autovacuum is keeping up (high dead_pct = autovacuum is behind)
SELECT relname, n_dead_tup, n_live_tup, last_autovacuum
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
```

### When to Run Manual VACUUM

```
Scenario                                  Action
────────────────────────────────────────  ──────────────────────────────────────────────
After bulk DELETE or UPDATE of many rows  VACUUM ANALYZE table_name
  (autovacuum may not trigger fast enough  (reclaim space, refresh stats)
   before your next big query)

Before REINDEX or CREATE INDEX            VACUUM table_name
  (reduces index build time — fewer        (clean up dead tuples first)
   heap pages to scan)

After initial bulk load                   ANALYZE table_name
  (planner stats needed for good plans;    (no dead tuples yet, just need stats)
   autovacuum may not have run yet)

Table bloat detected (dead_pct > 20%,     VACUUM ANALYZE table_name
high actual rows vs relpages estimate)     then check if VACUUM FULL needed

XID age approaching wraparound horizon    VACUUM FREEZE table_name
  (check: SELECT age(datfrozenxid)         (freezes all tuples, resets age)
   FROM pg_database)                       -- schedule during maintenance window

Severe bloat, need to reclaim disk space  pg_repack (online) or VACUUM FULL (locked)
```

### Table Bloat Diagnosis

```sql
-- Estimate bloat using pgstattuple (requires the extension)
CREATE EXTENSION IF NOT EXISTS pgstattuple;
SELECT * FROM pgstattuple('orders');
-- Returns: table_len, live_tuples, dead_tuples, free_space, free_percent

-- Quick bloat estimate without extension
SELECT
    pg_size_pretty(pg_total_relation_size(oid)) AS total_size,
    pg_size_pretty(pg_relation_size(oid))       AS table_size,
    relpages,
    reltuples::bigint                           AS estimated_rows
FROM pg_class
WHERE relname = 'orders';
-- If table_size >> estimated_rows × avg_row_width → bloat

-- Monitor XID age (prevent wraparound catastrophe)
SELECT datname,
       age(datfrozenxid)          AS xid_age,
       2000000000 - age(datfrozenxid) AS xids_until_wraparound
FROM pg_database
ORDER BY xid_age DESC;
-- Alert if xid_age > 1.5 billion (autovacuum aggressive threshold is ~200M)
```

---

## PARTITIONING (PG 10+)

Declarative partitioning — child tables inherit structure from parent.

```sql
-- ── RANGE: typical for time-series ───────────────────────────────────────
CREATE TABLE orders (
    id         BIGINT       NOT NULL,
    order_date DATE         NOT NULL,
    total      NUMERIC(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2023 PARTITION OF orders
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');  -- upper bound is exclusive
CREATE TABLE orders_2024 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- Default partition catches everything else
CREATE TABLE orders_default PARTITION OF orders DEFAULT;

-- ── LIST: categorical distribution ───────────────────────────────────────
CREATE TABLE accounts (
    id     BIGINT, region TEXT
) PARTITION BY LIST (region);

CREATE TABLE accounts_us PARTITION OF accounts FOR VALUES IN ('US', 'CA');
CREATE TABLE accounts_eu PARTITION OF accounts FOR VALUES IN ('EU', 'UK', 'DE');

-- ── HASH: even distribution when no natural partition key ─────────────────
CREATE TABLE users (
    id BIGINT, email TEXT
) PARTITION BY HASH (id);

CREATE TABLE users_0 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE users_1 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE users_2 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE users_3 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 3);

-- Partition pruning happens automatically on WHERE clauses that filter on the key
-- Index on parent table creates indexes on all partitions
CREATE INDEX ON orders (order_date, customer_id);
```

---

## ROW-LEVEL SECURITY

Column and row-level access control. More expressive than SQL Server RLS.

```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Policy: users only see their own orders
CREATE POLICY orders_per_user ON orders
    FOR ALL                                              -- applies to SELECT, INSERT, UPDATE, DELETE
    USING (user_id = current_setting('app.current_user_id')::int);

-- Separate read vs write policies
CREATE POLICY orders_read  ON orders FOR SELECT USING (user_id = current_user_id());
CREATE POLICY orders_write ON orders FOR INSERT WITH CHECK (user_id = current_user_id());

-- App sets session variable before each request
SET LOCAL app.current_user_id = '42';
SELECT * FROM orders;   -- automatically filtered; user sees only their rows

-- BYPASSRLS: superusers and roles with BYPASSRLS skip policies
-- For admin access: ALTER ROLE admin BYPASSRLS;
```

---

## EXTENSIONS ECOSYSTEM

```sql
CREATE EXTENSION IF NOT EXISTS vector;        -- pgvector
CREATE EXTENSION IF NOT EXISTS postgis;       -- PostGIS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";   -- UUID functions
CREATE EXTENSION IF NOT EXISTS pg_trgm;       -- trigram similarity
```

| Extension | Capability | Notes |
|-----------|-----------|-------|
| `pgvector` | Vector similarity search (cosine, L2, inner product) | AI/ML embedding storage; IVFFlat and HNSW indexes |
| `PostGIS` | Geospatial types, `ST_Distance`, `ST_Within`, coordinate transforms | Industry standard; used in every GIS context |
| `TimescaleDB` | Hypertables, continuous aggregates, data retention policies | Time-series on PostgreSQL; auto-partitions by time |
| `pg_cron` | Cron scheduler inside PostgreSQL | Run `REFRESH MATERIALIZED VIEW`, maintenance jobs |
| `pg_stat_statements` | Per-query execution statistics | Essential for identifying slow queries in production |
| `pg_partman` | Automates partition creation and maintenance | Set-and-forget partition management |
| `uuid-ossp` | `uuid_generate_v4()`, etc. | PG 13+ has `gen_random_uuid()` built-in |
| `pg_trgm` | Trigram similarity, `%` operator, fuzzy `LIKE` indexes | LIKE/ILIKE with GIN/GiST index support |
| `hstore` | Key-value storage | Largely superseded by JSONB |
| `Citus` | Distributed PostgreSQL (horizontal sharding) | Used in Azure Database for PostgreSQL Flexible Server |

---

## UPSERT

```sql
-- INSERT ... ON CONFLICT (PostgreSQL 9.5+)
INSERT INTO products (sku, name, price)
VALUES ('ABC-1', 'Widget', 19.99)
ON CONFLICT (sku) DO UPDATE
    SET name  = EXCLUDED.name,
        price = EXCLUDED.price,
        updated_at = NOW();
-- EXCLUDED refers to the row that would have been inserted

-- ON CONFLICT DO NOTHING: silently skip duplicates
INSERT INTO idempotent_log (event_id, data)
VALUES ('uuid-here', '{}')
ON CONFLICT (event_id) DO NOTHING;

-- Conflict on a partial index or expression
INSERT INTO reservations (slot_id, user_id)
VALUES (1, 42)
ON CONFLICT ON CONSTRAINT reservations_slot_user_unique DO NOTHING;
```

**T-SQL bridge:** SQL Server uses `MERGE` for this. PostgreSQL's `ON CONFLICT` is simpler, safer (no MERGE concurrency bugs), and easier to read.

---

## CTE BEHAVIOR — Important Difference

```sql
-- PostgreSQL materializes CTEs by default (optimization fence)
-- Optimizer CANNOT push predicates through a CTE
WITH active_users AS (
    SELECT * FROM users WHERE active = TRUE  -- this query runs fully, result stored
)
SELECT * FROM active_users WHERE email LIKE '%@corp.com';
-- Two passes: first get all active users, then filter

-- Force inlining (PG 12+) — let optimizer treat it like a subquery
WITH active_users AS NOT MATERIALIZED (
    SELECT * FROM users WHERE active = TRUE
)
SELECT * FROM active_users WHERE email LIKE '%@corp.com';
-- Optimizer can now combine both WHERE clauses

-- Force materialization explicitly (useful when CTE is referenced multiple times)
WITH expensive_calc AS MATERIALIZED (
    SELECT ...complex aggregation...
)
SELECT * FROM expensive_calc WHERE ... UNION ALL SELECT * FROM expensive_calc WHERE ...;
```

**T-SQL bridge:** SQL Server inlines CTEs by default (treats them as view substitutions). PostgreSQL materializes by default — opposite behavior. Add `NOT MATERIALIZED` when porting T-SQL CTEs.

---

## GOTCHAS FROM T-SQL

| T-SQL habit | PostgreSQL reality |
|-------------|-------------------|
| `WITH(NOLOCK)` for performance | No equivalent. MVCC means readers never block writers — dirty reads are impossible. Remove all NOLOCK hints. |
| `IDENTITY(1,1)` | Use `GENERATED ALWAYS AS IDENTITY` (ANSI SQL). `SERIAL` is old shorthand — still works but deprecated. |
| `SELECT TOP 10 * FROM t` | `SELECT * FROM t LIMIT 10` — LIMIT goes at the end, TOP goes after SELECT |
| `'a' + 'b'` string concat | `'a' \|\| 'b'` or `concat('a','b')` — `+` on strings is a type error in PG |
| `DATEDIFF(day, d1, d2)` | `(d2::date - d1::date)` returns integer days; `age(d2, d1)` returns interval |
| `GETDATE()` | `NOW()` or `CURRENT_TIMESTAMP` |
| `VARCHAR(MAX)` | `TEXT` — no length limit, same storage, same performance |
| `NVARCHAR(200)` | `VARCHAR(200)` or `TEXT` — PostgreSQL is always UTF-8 |
| `#temp` table | `CREATE TEMP TABLE t (...)` — auto-dropped at session end |
| `@table TABLE (...)` | CTE (`WITH t AS (...)`) or `CREATE TEMP TABLE` |
| `CROSS APPLY` | `JOIN LATERAL ... ON TRUE` |
| `OUTER APPLY` | `LEFT JOIN LATERAL ... ON TRUE` |
| `FOR XML PATH('')` aggregation | `string_agg(col, ',')` or `jsonb_agg(col)` |
| `ISNULL(x, default)` | `COALESCE(x, default)` — ANSI, works in both |
| `dbo.TableName` | `public.table_name` — schemas real namespaces; `public` is default |
| `sp_executesql` | `EXECUTE format('... %I ...', identifier)` or `EXECUTE sql_string` |
| `1` / `0` for booleans | `TRUE` / `FALSE` literals — `BOOLEAN` is a real type |
| `arr[0]` first element | `arr[1]` — PostgreSQL arrays are 1-indexed |
| `TIMESTAMP` (assume UTC) | Use `TIMESTAMPTZ` always — stores UTC, displays in session timezone |
| CTE optimization | CTEs are materialized by default — add `NOT MATERIALIZED` to match SQL Server inlining behavior |

---

## ECOSYSTEM / TOOLING

| Tool | Category | Notes |
|------|---------|-------|
| `psql` | CLI client | `\d table`, `\dt`, `\timing`, `\copy` — powerful once learned |
| pgAdmin 4 | GUI admin | Open source, browser-based, official PostgreSQL tool |
| DBeaver | Cross-DB GUI | Free, supports everything including PG, SQL Server, MySQL |
| DataGrip | Cross-DB GUI | JetBrains, best SQL intelligence, paid |
| TablePlus | Cross-DB GUI | Mac/Windows, fast native UI |
| Prisma | Node.js ORM | Type-safe, schema-first, migrations built-in |
| Drizzle | Node.js ORM | Lightweight, SQL-like, TypeScript-first |
| TypeORM | Node.js ORM | Decorator-based, more traditional ActiveRecord style |
| SQLAlchemy | Python ORM | Industry standard Python ORM |
| `pg` (node-postgres) | Node.js driver | Low-level, battle-tested, direct SQL |
| asyncpg | Python async driver | Fastest Python PG driver |
| Npgsql | .NET driver | ADO.NET provider for PostgreSQL — drop-in for your ADO.NET knowledge |
| pgBouncer | Connection pooler | Transaction-mode pooling — essential for high-concurrency apps |
| Supabase | PG-as-a-service | Auto-generated REST/GraphQL API, Auth, Realtime, Storage |
| Neon | Serverless PG | Branching (like git for DB), scale-to-zero, instant DB copies |
| AWS RDS / Aurora | Managed cloud | Aurora PG is wire-compatible PG with AWS clustering |
| Azure DB for PostgreSQL | Managed cloud | Flexible Server is current offering; has Citus extension |

---

## DECISION CHEAT SHEET

| Need | Why PostgreSQL wins |
|------|-------------------|
| JSONB + relational queries | Best of both — indexed JSON operators, JOIN with relational tables, no document DB needed |
| Full-text search (moderate scale) | `tsvector`/`tsquery` + GIN — cheaper than Elasticsearch for < ~50M docs |
| Geospatial | PostGIS is the industry standard for spatial queries |
| Time-series | TimescaleDB extension — hypertables auto-partition by time, continuous aggregates |
| AI/ML embedding storage | pgvector — HNSW/IVFFlat indexes for ANN search, stays in your relational DB |
| ANSI SQL compliance | Most standards-compliant open-source RDBMS — porting from Oracle easier than MySQL |
| Open-source / no license cost | PostgreSQL License (permissive) — zero cost at any scale |
| Audit / row history | Temporal tables not built-in (use `pg_audit` + trigger pattern or temporal extension) |
| ETL / analytics | Good for moderate scale; for TBs, consider Synapse or BigQuery externally |
| High-concurrency OLTP | pgBouncer for connection pooling; Citus for sharding; excellent at high read concurrency |

---

## COMMON CONFUSION POINTS

**`json` vs `jsonb`:** Always use `jsonb`. `json` stores text verbatim (preserves key order, whitespace). `jsonb` parses on insert into binary format. Only use `json` if you need exact round-trip fidelity of whitespace/key order, which you essentially never do.

**`SERIAL` vs `GENERATED ALWAYS AS IDENTITY`:** `SERIAL` is PostgreSQL shorthand for creating a sequence and setting a default. It's not SQL standard and has edge cases (sequences aren't owned properly). `GENERATED ALWAYS AS IDENTITY` (PG 10+) is the SQL:2003 standard — use it.

**CTE materialization fence:** PostgreSQL 12 and earlier always materialized CTEs. PG 12+ materializes by default but respects `NOT MATERIALIZED`. This is the opposite of SQL Server, which inlines CTEs. Performance-sensitive queries coming from T-SQL need this audit.

**`::`casting:** `value::type` is PostgreSQL shorthand for `CAST(value AS type)`. Identical semantics, PostgreSQL-only syntax. Common in production code — you'll see it everywhere.

**Arrays are 1-indexed:** `arr[1]` is the first element. `arr[0]` returns NULL, not an error. Will silently give wrong results if you assume 0-based indexing from your C#/Python habits.

**`TEXT` = `VARCHAR` without a limit:** No performance difference. PostgreSQL stores both the same way. Use `TEXT` for any string without a meaningful length constraint.

**`TIMESTAMP` vs `TIMESTAMPTZ`:** `TIMESTAMP` stores no timezone info — it's a naive datetime. `TIMESTAMPTZ` stores UTC, converts to/from session timezone on display. Use `TIMESTAMPTZ` for everything unless you have a specific reason (e.g., storing event times in their "local" time for display purposes only).

**MVCC means no need for NOLOCK:** T-SQL developers reach for `WITH(NOLOCK)` to avoid blocking. In PostgreSQL, MVCC guarantees that readers never block writers and writers never block readers. You get snapshot isolation by default. There is no equivalent hint because there is no need for one.
