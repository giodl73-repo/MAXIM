# MySQL / MariaDB

MySQL is the most widely deployed RDBMS on the planet by install count (LAMP stack legacy). MariaDB is its community fork post-Oracle acquisition. MySQL 8.0 (2018) finally added full window function support, CTEs, and enforced CHECK constraints — closing most of the gap with PostgreSQL/SQL Server.

---

## Ecosystem Position

```
Query Languages Landscape
─────────────────────────────────────────────────────────────────────
                        SQL Dialects
                             │
        ┌────────────────────┼─────────────────────────┐
        │                    │                         │
  T-SQL (SQL Server)   MySQL / MariaDB           PostgreSQL
  ├── Enterprise OLTP   ├── LAMP/LEMP stack       ├── ANSI-strictest
  ├── Azure SQL DB      ├── WordPress default      ├── Extensions ecosystem
  ├── Synapse           ├── Laravel/PHP native     ├── Analytics-capable
  └── Your background   ├── AWS Aurora compat      └── PostGIS / pgvector
                        └── PlanetScale (MySQL)

MySQL's position: ubiquitous, operationally simple, read-heavy OLTP king
MariaDB: MySQL-compatible fork with extra engines + Galera cluster sync
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
| Clustered index | Data stored in PK order on disk — identical to SQL Server's clustered index model |
| Secondary index storage | Contains PK value — secondary lookup requires PK fetch if not covering |
| Foreign key enforcement | InnoDB enforces; MyISAM silently ignores FK declarations |
| Auto-increment gaps | Gaps occur on rollback and crash recovery — never assume sequence continuity |

```
InnoDB B-Tree Layout (compare to SQL Server clustered index)

PK Clustered Index (data pages):
┌──────────────────────────────────────────┐
│  id=1 | col1 | col2 | col3 | ...         │  ← leaf pages store actual row data
│  id=2 | col1 | col2 | col3 | ...         │
│  id=3 | col1 | col2 | col3 | ...         │
└──────────────────────────────────────────┘

Secondary Index (non-clustered):
┌──────────────────────────────────────────┐
│  email='a@b.com' → PK=1                  │  ← stores PK, not full row
│  email='c@d.com' → PK=3                  │  ← fetch row = second B-tree lookup
└──────────────────────────────────────────┘
Covering index: include all needed cols so second lookup is skipped
```

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

---

## 11. Replication and Binlog

```
MySQL Replication Architecture
────────────────────────────────────────────────────────────────
Primary                           Replica(s)
┌────────────────┐                ┌────────────────┐
│  InnoDB Engine │                │  InnoDB Engine │
│       │        │                │       │        │
│  Binary Log    │──── async ────►│  Relay Log     │
│  (binlog)      │                │  SQL Thread    │
└────────────────┘                └────────────────┘

Binlog formats:
  STATEMENT — logs the SQL text (compact, but non-deterministic functions = drift)
  ROW       — logs the actual row changes (default MySQL 5.7+, safest)
  MIXED     — STATEMENT for safe queries, ROW for unsafe ones

GTID (Global Transaction IDs, MySQL 5.6+):
  Every transaction gets a globally unique ID: source_uuid:sequence_number
  Replicas use GTIDs to self-position — no more MASTER_LOG_FILE/MASTER_LOG_POS

Group Replication (MySQL 5.7.17+):
  Multi-primary with Paxos-based conflict detection
  Basis for InnoDB Cluster (high-availability topology)

AWS Aurora (MySQL-compatible):
  Proprietary shared distributed storage layer
  Replicas read from same storage as writer — no replication lag
  Up to 15 read replicas with sub-10ms lag
```

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

## 17. Common Confusion Points

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
