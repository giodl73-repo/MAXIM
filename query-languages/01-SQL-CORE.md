# SQL Core — The 30-Year Refresh

> What you knew from ADO.NET/T-SQL circa 2000–2003 is still valid. The SELECT/JOIN/GROUP BY model is unchanged.
> What changed is everything *above* that — CTEs, window functions, JSON, temporal tables, modern DML,
> and two decades of syntax ergonomics. This file is those additions plus a complete reference card.
> PostgreSQL syntax is used as the baseline (most ANSI-compliant); T-SQL divergences are called out inline.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           SQL LANGUAGE SURFACE                                      │
├──────────────────┬──────────────────┬──────────────────┬──────────────────────────── │
│  DDL             │  DML             │  DCL             │  TCL                        │
│  ─────────────── │  ─────────────── │  ─────────────── │  ───────────────            │
│  CREATE TABLE    │  SELECT          │  GRANT           │  BEGIN                      │
│  ALTER TABLE     │  INSERT          │  REVOKE          │  COMMIT                     │
│  DROP TABLE      │  UPDATE          │  ─────────────── │  ROLLBACK                   │
│  CREATE INDEX    │  DELETE          │  Row-Level Sec.  │  SAVEPOINT                  │
│  CREATE VIEW     │  MERGE           │  Column priv.    │  SET ISOLATION LEVEL        │
│  CREATE SEQUENCE │  TRUNCATE        │                  │                             │
│  ─────────────── │  ─────────────── │                  │                             │
│  Schema          │  Query Exprs:    │                  │                             │
│  Constraints     │  ─────────────── │                  │                             │
│  Types           │  FROM / JOIN     │                  │                             │
│  Partitioning    │  WHERE / HAVING  │                  │                             │
│                  │  GROUP BY        │                  │                             │
│                  │  Window OVER()   │                  │                             │
│                  │  CTEs (WITH)     │                  │                             │
│                  │  Set ops         │                  │                             │
│                  │  Subqueries      │                  │                             │
└──────────────────┴──────────────────┴──────────────────┴─────────────────────────────┘

QUERY EXECUTION PIPELINE (what happens after you press F5 / submit the query):

  ┌────────────┐   ┌────────────┐   ┌────────────────────┐   ┌──────────────────────┐
  │  PARSE     │   │  BIND      │   │  OPTIMIZE          │   │  EXECUTE             │
  │ ────────── │   │ ────────── │   │ ────────────────── │   │ ──────────────────── │
  │ Lex/parse  │──▶│ Resolve    │──▶│ Cost-based         │──▶│ Iterator model:      │
  │ SQL text   │   │ names →    │   │ optimizer:         │   │ plan tree of nodes   │
  │ → AST      │   │ OIDs /     │   │  - Stats from      │   │ each node: open/     │
  │            │   │ column     │   │    pg_statistic    │   │ next/close           │
  │ Syntax     │   │ metadata   │   │  - Cardinality est │   │                      │
  │ errors     │   │ Type check │   │  - Join order      │   │ SeqScan, IndexScan,  │
  │ caught     │   │ Security   │   │    (dynamic prog.) │   │ HashJoin, Gather...  │
  │ here       │   │ check      │   │  - Access path     │   │                      │
  └────────────┘   └────────────┘   └────────────────────┘   └──────────────────────┘
        │                                     │
        │  T-SQL equivalent stages:           │  T-SQL: "Algebraizer" (bind) →
        │  Parser → Algebrizer →              │  Query Optimizer → Execution Engine
        │  Query Optimizer → Storage Engine   │  Cached in plan cache (procedure cache)
        │                                     │  PG: plan cached per session (prepared stmts)
        └─────────────────────────────────────┘

  EXPLAIN ANALYZE shows you the Execute stage: actual plan tree, actual vs estimated rows.
  The Optimize stage is the black box you influence with indexes, statistics, and hints.
```

---

## 1. SQL in 2024 vs SQL in 2000

```
SQL Server 2000 era (your baseline)          What was added since
─────────────────────────────────────────    ──────────────────────────────────────────
SELECT / FROM / WHERE / JOIN                 ✅ still the same
GROUP BY / HAVING                            ✅ still the same
Subqueries (correlated + uncorrelated)       ✅ still the same
Basic transactions (BEGIN/COMMIT/ROLLBACK)   ✅ still the same
Stored procedures / triggers                 ✅ still the same (more features added)
TOP n (T-SQL)                                → FETCH FIRST n ROWS ONLY (ANSI SQL:2008)
                                             → LIMIT n (PostgreSQL/MySQL shorthand)

─── SQL:1999 additions ───────────────────────────────────────────────────────────────
WITH cte AS (...)                            ← Common Table Expressions (huge)
WITH RECURSIVE cte AS (...)                  ← Tree/graph traversal
BOOLEAN type                                 ← true/false as first-class type

─── SQL:2003 additions ───────────────────────────────────────────────────────────────
fn() OVER (PARTITION BY ... ORDER BY ...)    ← Window functions (biggest feature gap)
MERGE INTO target USING source ON ...        ← Upsert on steroids
GENERATED ALWAYS AS IDENTITY                 ← Standard identity columns

─── SQL:2008 additions ───────────────────────────────────────────────────────────────
FETCH FIRST n ROWS ONLY                      ← ANSI pagination (replaces TOP/LIMIT)
TRUNCATE TABLE                               ← Officially standardized

─── SQL:2011 additions ───────────────────────────────────────────────────────────────
FOR SYSTEM_TIME AS OF timestamp              ← System-versioned temporal tables
PERIOD FOR SYSTEM_TIME (start, end)          ← Bi-temporal tracking built into schema

─── SQL:2016 additions ───────────────────────────────────────────────────────────────
JSON_VALUE / JSON_QUERY / JSON_TABLE         ← First-class JSON in relational SQL
MATCH_RECOGNIZE                              ← Row pattern recognition (event sequences)

─── Cross-version ergonomics ─────────────────────────────────────────────────────────
FILTER (WHERE ...) on aggregates             ← Cleaner than CASE WHEN inside SUM()
LATERAL joins                                ← Correlated subquery in FROM clause
GROUPING SETS / CUBE / ROLLUP                ← Multi-level aggregation without UNION ALL
INSERT ... ON CONFLICT ... DO UPDATE         ← PostgreSQL upsert (not ANSI but universal)
```

---

## 2. SELECT — Execution Order vs Write Order

This is the single most important mental model shift. SQL is **declarative** — you write in one order,
the engine executes in a different order.

```
Write order (how you type it):      Execution order (how the engine runs it):

  SELECT                              1. FROM          ← build the row source
  FROM                                2. JOIN / ON     ← combine tables
  WHERE                               3. WHERE         ← filter rows (before aggregation)
  GROUP BY                            4. GROUP BY      ← partition into groups
  HAVING                              5. HAVING        ← filter groups (after aggregation)
  ORDER BY                            6. SELECT        ← evaluate expressions, aliases
  LIMIT                               7. DISTINCT      ← deduplicate if present
                                      8. ORDER BY      ← sort (can use SELECT aliases here)
                                      9. LIMIT/OFFSET  ← truncate result set
```

**Consequence**: You cannot use a SELECT alias in WHERE or GROUP BY (those run before SELECT):
```sql
-- WRONG: alias not yet defined when WHERE executes
SELECT salary * 1.1 AS adjusted
FROM   employees
WHERE  adjusted > 100000;       -- ERROR: column "adjusted" does not exist

-- CORRECT: repeat the expression, or wrap in a subquery/CTE
SELECT salary * 1.1 AS adjusted
FROM   employees
WHERE  salary * 1.1 > 100000;

-- ALSO CORRECT via CTE:
WITH base AS (SELECT *, salary * 1.1 AS adjusted FROM employees)
SELECT * FROM base WHERE adjusted > 100000;
```

### Full SELECT Reference Card

```sql
SELECT [DISTINCT]
    column_name,
    table.column,
    expression AS alias,
    aggregate_fn(col),
    window_fn() OVER (...),
    (SELECT scalar_subquery)
FROM   table_name [AS alias]
       [CROSS JOIN other_table]
       [INNER | LEFT | RIGHT | FULL OUTER] JOIN other_table
           ON join_condition
       [LATERAL (SELECT ...) AS lateral_alias]
WHERE  row_filter_expression          -- applies before GROUP BY
GROUP BY grouping_cols
         | GROUPING SETS ((a,b),(a),(b),())
         | ROLLUP (a,b,c)
         | CUBE (a,b,c)
HAVING aggregate_filter_expression    -- applies after GROUP BY
ORDER BY col [ASC | DESC] [NULLS FIRST | NULLS LAST]
LIMIT  n  OFFSET m                    -- PostgreSQL / MySQL / SQLite / DuckDB
FETCH  FIRST n ROWS ONLY              -- ANSI SQL:2008 / Oracle / DB2
-- T-SQL: SELECT TOP n ... (at the top, before columns)
```

---

## 3. JOINs

```
INNER JOIN                      LEFT OUTER JOIN
  ┌──────┐   ┌──────┐             ┌──────┐   ┌──────┐
  │  A   │░░░│   B  │             │  A   ███████   B  │
  │      │███│      │             │      ░░░│       │
  └──────┘   └──────┘             └──────┘   └──────┘
  Only matching rows              All of A + matched B (NULLs where no match)

RIGHT OUTER JOIN                FULL OUTER JOIN
  ┌──────┐   ┌──────┐             ┌──────┐   ┌──────┐
  │  A   │░░░███████│             ███████████████████│
  │      │   │      │             │  A   ░░░│   B   │
  └──────┘   └──────┘             └──────┘   └──────┘
  All of B + matched A            All of A + all of B (NULLs on both sides where no match)

CROSS JOIN                      SELF JOIN
  ┌──────┐ × ┌──────┐             ┌──────┐
  │  A   │   │   B  │             │  A   │ JOIN │  A  │
  │ n rows│  │ m rows│            employees e1 JOIN employees e2
  └──────┘   └──────┘             ON e1.manager_id = e2.id
  n × m rows — every combination  Used for: hierarchies, adjacency lists, comparisons
```

```sql
-- INNER JOIN: only rows with a match in both tables
SELECT o.id, c.name
FROM   orders o
JOIN   customers c ON o.customer_id = c.id;

-- LEFT JOIN: all orders, NULLs for customers with no matching order
SELECT c.name, o.id AS order_id
FROM   customers c
LEFT JOIN orders o ON c.id = o.customer_id;
-- c.name rows without orders still appear; o.id will be NULL

-- Find customers with NO orders (NULL trick):
SELECT c.name
FROM   customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE  o.id IS NULL;

-- FULL OUTER JOIN
SELECT c.name, o.id
FROM   customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id;

-- CROSS JOIN: useful for generating combinations or test data
SELECT a.size, b.color
FROM   sizes a CROSS JOIN colors b;

-- SELF JOIN: employee → manager hierarchy
SELECT e.name AS employee, m.name AS manager
FROM   employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**Old-world bridge:**
```sql
-- SQL Server 2000 "comma join" style — implicit cross join, filter in WHERE
-- DO NOT USE THIS:
SELECT o.id, c.name
FROM   orders o, customers c
WHERE  o.customer_id = c.id       -- this is an INNER JOIN in disguise

-- Modern explicit syntax — always use this:
SELECT o.id, c.name
FROM   orders o
JOIN   customers c ON o.customer_id = c.id
```

The old comma-join syntax is still valid SQL, but it's error-prone (forgotten WHERE clause = accidental CROSS JOIN).

---

## 4. Aggregation

```sql
-- Basic aggregates
SELECT
    COUNT(*)                        AS total_rows,       -- counts all rows including NULLs
    COUNT(shipped_at)               AS rows_with_value,  -- skips NULLs
    COUNT(DISTINCT customer_id)     AS unique_customers,
    SUM(amount)                     AS total_revenue,
    AVG(amount)                     AS avg_order,
    MIN(created_at)                 AS first_order,
    MAX(created_at)                 AS last_order
FROM orders
WHERE status = 'completed';

-- FILTER clause (SQL:2003 — cleaner than CASE WHEN inside aggregate)
SELECT
    COUNT(*)                                        AS total,
    COUNT(*) FILTER (WHERE status = 'completed')    AS completed,
    COUNT(*) FILTER (WHERE status = 'cancelled')    AS cancelled,
    SUM(amount) FILTER (WHERE amount > 1000)        AS large_order_rev
FROM orders;
-- T-SQL equivalent (no FILTER): SUM(CASE WHEN status = 'completed' THEN amount END)

-- STRING_AGG (SQL:2017 — replaces GROUP_CONCAT / FOR XML PATH)
SELECT customer_id,
       STRING_AGG(product_name, ', ') ORDER BY product_name AS products
FROM   order_items
GROUP BY customer_id;
-- T-SQL: STRING_AGG works in SQL Server 2017+
-- MySQL: GROUP_CONCAT(product_name ORDER BY product_name SEPARATOR ', ')

-- GROUPING SETS — multiple aggregation levels in one pass
SELECT dept, job_title, SUM(salary) AS total
FROM   employees
GROUP BY GROUPING SETS (
    (dept, job_title),   -- subtotal by dept + job
    (dept),              -- subtotal by dept
    ()                   -- grand total
);

-- ROLLUP — hierarchical subtotals (right-to-left)
GROUP BY ROLLUP (dept, job_title)
-- produces: (dept, job_title), (dept), ()

-- CUBE — all combinations
GROUP BY CUBE (dept, job_title)
-- produces: (dept, job_title), (dept), (job_title), ()
```

---

## 5. CTEs — Common Table Expressions

**What they are**: named subqueries defined at the top of a query. Replaced deeply nested subqueries.
**Scope**: visible only within the query that defines them. Can reference earlier CTEs in the same WITH block.

```sql
-- Basic CTE — a named subquery
WITH recent_orders AS (
    SELECT customer_id, order_date, total
    FROM   orders
    WHERE  order_date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT c.name,
       COUNT(*)        AS order_count,
       SUM(o.total)    AS revenue
FROM   customers c
JOIN   recent_orders o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY revenue DESC;

-- Multiple CTEs — chain them (each can reference prior CTEs)
WITH
  active_customers AS (
      SELECT id, name FROM customers WHERE status = 'active'
  ),
  customer_revenue AS (
      SELECT o.customer_id, SUM(o.total) AS revenue
      FROM   orders o
      WHERE  o.status = 'completed'
      GROUP BY o.customer_id
  ),
  ranked AS (
      SELECT ac.name,
             COALESCE(cr.revenue, 0)                          AS revenue,
             ROW_NUMBER() OVER (ORDER BY cr.revenue DESC)     AS rn
      FROM   active_customers ac
      LEFT JOIN customer_revenue cr ON ac.id = cr.customer_id
  )
SELECT * FROM ranked WHERE rn <= 10;    -- top 10 customers

-- Recursive CTE — tree / graph traversal (SQL:1999)
-- Classic use: org chart, BOM explosion, category hierarchy
WITH RECURSIVE org_tree AS (
    -- Anchor member: starting point (termination condition)
    SELECT id, name, manager_id, 0 AS depth, ARRAY[id] AS path
    FROM   employees
    WHERE  manager_id IS NULL           -- root: CEO / top of tree

    UNION ALL

    -- Recursive member: join children to current frontier
    SELECT e.id, e.name, e.manager_id, t.depth + 1, t.path || e.id
    FROM   employees e
    JOIN   org_tree t ON e.manager_id = t.id
    WHERE  NOT e.id = ANY(t.path)       -- cycle guard (important for graphs)
)
SELECT depth, REPEAT('  ', depth) || name AS indented_name, id
FROM   org_tree
ORDER BY path;
```

**T-SQL note**: SQL Server uses `WITH cte AS (...)` — same syntax. The `RECURSIVE` keyword is
optional in T-SQL (recursion is always allowed in CTEs). PostgreSQL requires the keyword.

**Materialization behavior** — matters for performance:
```
PostgreSQL (pre-14):  CTEs are an optimization fence — always materialized
                      (query planner cannot push predicates through them)
PostgreSQL 14+:       inline by default unless MATERIALIZED keyword used
SQL Server:           always inline (treated as a view, not a temp table)
Oracle:               inline by default; WITH ... AS MATERIALIZED forces mat.

WITH my_cte AS MATERIALIZED (SELECT ...)    -- force materialization (PostgreSQL)
WITH my_cte AS NOT MATERIALIZED (SELECT ...) -- force inline
```

---

## 6. Window Functions

The biggest feature addition since SQL:2003. Aggregate without collapsing rows.

### OVER Clause Anatomy

```
  function_name() OVER (
      PARTITION BY col1, col2    ← reset context at each partition boundary
                                   (like GROUP BY but doesn't collapse rows)
      ORDER BY col3 [ASC|DESC]   ← ordering within each partition
      ROWS | RANGE BETWEEN       ← frame: which rows within the partition
          start_bound            ←   UNBOUNDED PRECEDING
          AND                    ←   n PRECEDING
          end_bound              ←   CURRENT ROW
  )                              ←   n FOLLOWING
                                 ←   UNBOUNDED FOLLOWING
```

**Default frame behavior — the most common window function gotcha:**

```
When ORDER BY is present but no frame clause specified:
  Default: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

  RANGE (not ROWS) means: all rows with the same ORDER BY value as CURRENT ROW
  are included in the frame — even rows "after" the current row physically.

  Consequence: if multiple rows share the same order_date, SUM() OVER (ORDER BY order_date)
  gives them ALL the same running total (the sum up to the last row with that date).
  This is almost never what you want for a true running total.

  ┌─────────────────┬────────────────────────────────────────────────────────────────┐
  │ Frame clause    │ Behavior                                                       │
  ├─────────────────┼────────────────────────────────────────────────────────────────┤
  │ (none, no OVER  │ ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING        │
  │  ORDER BY)      │ = entire partition — same value for all rows in partition       │
  ├─────────────────┼────────────────────────────────────────────────────────────────┤
  │ (none, with     │ RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW              │
  │  ORDER BY)      │ = all rows up to and including ties at CURRENT ROW             │
  │                 │ DANGER: ties get same cumulative total, not incremental one    │
  ├─────────────────┼────────────────────────────────────────────────────────────────┤
  │ ROWS BETWEEN    │ Physical row count — always deterministic                       │
  │ UNBOUNDED       │ Best for running totals, moving averages                        │
  │ PRECEDING AND   │ Explicit — no surprises with ties                              │
  │ CURRENT ROW     │                                                                 │
  └─────────────────┴────────────────────────────────────────────────────────────────┘

  Fix: always write the frame explicitly when ORDER BY is present:
    SUM(amount) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)

  RANGE has a performance cost too: the engine cannot simply increment a running value;
  it must identify all peer rows (same ORDER BY value) before emitting any of them.
  ROWS is streamable; RANGE on ties requires buffering.
```

### Ranking Functions

```sql
SELECT
    name,
    dept,
    salary,
    ROW_NUMBER()   OVER (PARTITION BY dept ORDER BY salary DESC) AS row_num,
    RANK()         OVER (PARTITION BY dept ORDER BY salary DESC) AS rank,
    DENSE_RANK()   OVER (PARTITION BY dept ORDER BY salary DESC) AS dense_rank,
    NTILE(4)       OVER (PARTITION BY dept ORDER BY salary DESC) AS quartile
FROM employees;

-- For same salary (ties):
-- ROW_NUMBER:  1, 2, 3, 4, 5   (arbitrary tiebreak — always unique)
-- RANK:        1, 2, 2, 4, 5   (gaps after ties)
-- DENSE_RANK:  1, 2, 2, 3, 4   (no gaps)
-- NTILE(4):    1, 1, 2, 2, 3   (divides into n equal buckets)
```

### Value / Analytic Functions

```sql
SELECT
    order_date,
    amount,
    LAG(amount, 1, 0)   OVER (PARTITION BY customer_id ORDER BY order_date)
        AS prev_order_amount,
    LEAD(amount, 1, 0)  OVER (PARTITION BY customer_id ORDER BY order_date)
        AS next_order_amount,
    FIRST_VALUE(amount) OVER (PARTITION BY customer_id ORDER BY order_date
                               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
        AS first_order_amount,
    LAST_VALUE(amount)  OVER (PARTITION BY customer_id ORDER BY order_date
                               ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
        AS last_order_amount
FROM orders;
```

### Aggregates as Windows

```sql
SELECT
    customer_id,
    order_date,
    amount,

    -- Running total (cumulative sum)
    SUM(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,

    -- 7-day rolling average
    AVG(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7day_avg,

    -- Dept average without collapsing rows (unlike GROUP BY)
    AVG(amount) OVER (PARTITION BY dept_id)             AS dept_avg,

    -- Total count in every row
    COUNT(*) OVER ()                                     AS total_rows,

    -- What fraction of dept revenue is this order?
    amount / SUM(amount) OVER (PARTITION BY customer_id) AS pct_of_customer_rev

FROM orders;
```

### ROWS vs RANGE Frame

```
ROWS BETWEEN:   physical rows — counts N rows before/after
RANGE BETWEEN:  logical value range — includes all rows with same ORDER BY value

Example: ORDER BY order_date
  ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    → always exactly 2 rows (prev + current)
  RANGE BETWEEN INTERVAL '1' MONTH PRECEDING AND CURRENT ROW
    → all rows within 1 month back (could be many rows on same date)
```

### Top-1-Per-Group (the most common window function pattern)

```sql
-- Get the most recent order per customer
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY order_date DESC, id DESC    -- tiebreak on id
           ) AS rn
    FROM orders
)
SELECT customer_id, order_date, amount
FROM   ranked
WHERE  rn = 1;

-- Alternative: DISTINCT ON (PostgreSQL-specific, cleaner syntax)
SELECT DISTINCT ON (customer_id)
    customer_id, order_date, amount
FROM orders
ORDER BY customer_id, order_date DESC, id DESC;
```

---

## 7. Subqueries

```sql
-- Scalar subquery: returns exactly one row, one column
SELECT name,
       salary,
       (SELECT AVG(salary) FROM employees)  AS company_avg,
       salary - (SELECT AVG(salary) FROM employees) AS diff_from_avg
FROM   employees;

-- Row subquery: returns one row, multiple columns
SELECT * FROM employees
WHERE (dept, level) = (SELECT dept, level FROM employees WHERE id = 42);

-- Table subquery in FROM (derived table / inline view)
SELECT dept, avg_sal
FROM   (SELECT dept, AVG(salary) AS avg_sal FROM employees GROUP BY dept) AS dept_avg
WHERE  avg_sal > 80000;

-- Correlated subquery: references outer query — re-executes for each outer row
SELECT e.name, e.salary
FROM   employees e
WHERE  e.salary > (SELECT AVG(salary) FROM employees WHERE dept = e.dept);
-- "find employees earning above their department's average"
-- Runs the inner SELECT once per row in e — can be expensive on large tables
-- Often replaceable with a window function

-- EXISTS / NOT EXISTS
SELECT c.name
FROM   customers c
WHERE  EXISTS (
    SELECT 1 FROM orders o
    WHERE  o.customer_id = c.id
    AND    o.status = 'completed'
    AND    o.amount > 1000
);
-- EXISTS short-circuits on first match — often faster than IN for large sets
-- SELECT 1 / SELECT * in EXISTS doesn't matter — optimizer ignores the select list

-- IN vs EXISTS — NULL behavior difference
WHERE id IN (1, 2, NULL)     -- NULL branch → UNKNOWN, silently drops rows
WHERE id IN (SELECT ...)     -- if subquery returns NULL, any non-matching row → UNKNOWN
WHERE EXISTS (SELECT ...)    -- no NULL issue: exists is purely TRUE/FALSE
```

---

## 8. Set Operations

```sql
-- UNION ALL — multiset union (keeps all rows, including duplicates)
-- Use by default: no sort/hash cost
SELECT id, name FROM current_employees
UNION ALL
SELECT id, name FROM archived_employees;

-- UNION — set union (deduplicates via sort or hash — costs extra)
-- Column count and compatible types must match
-- Column names taken from first query
SELECT id FROM table_a
UNION
SELECT id FROM table_b;

-- INTERSECT — rows present in both result sets
SELECT customer_id FROM orders_2023
INTERSECT
SELECT customer_id FROM orders_2024;
-- "customers who ordered in both years"

-- EXCEPT (ANSI) / MINUS (Oracle) — rows in first but not in second
SELECT customer_id FROM customers
EXCEPT
SELECT customer_id FROM orders WHERE order_date >= '2024-01-01';
-- "customers who have NOT placed an order in 2024"

-- Ordering applies to the final combined result (put ORDER BY at the end)
SELECT id, name FROM a
UNION ALL
SELECT id, name FROM b
ORDER BY name;    -- applies after union
```

---

## 9. DDL Reference

```sql
-- CREATE TABLE with modern constraints
CREATE TABLE orders (
    id              BIGINT          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    -- T-SQL equiv: id BIGINT IDENTITY(1,1) NOT NULL PRIMARY KEY
    customer_id     INT             NOT NULL
                                    REFERENCES customers(id) ON DELETE CASCADE,
    status          VARCHAR(20)     NOT NULL DEFAULT 'pending'
                                    CHECK (status IN ('pending','processing','shipped','delivered','cancelled')),
    amount          NUMERIC(12,2)   NOT NULL CHECK (amount > 0),
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    -- TIMESTAMPTZ = timestamp with time zone — always use this, not TIMESTAMP
    shipped_at      TIMESTAMPTZ,    -- nullable: no NOT NULL = allows NULL
    metadata        JSONB,          -- PostgreSQL binary JSON; use NVARCHAR(MAX) in T-SQL
    CONSTRAINT uq_customer_date UNIQUE (customer_id, created_at)
);

-- Alter table
ALTER TABLE orders ADD COLUMN tracking_number VARCHAR(100);
ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'new';
ALTER TABLE orders ALTER COLUMN amount TYPE NUMERIC(14,2);  -- widen
ALTER TABLE orders DROP COLUMN tracking_number;
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount >= 0);
ALTER TABLE orders RENAME COLUMN status TO order_status;

-- Indexes
CREATE INDEX       idx_orders_customer     ON orders (customer_id);
CREATE INDEX       idx_orders_status_date  ON orders (status, created_at DESC);
CREATE UNIQUE INDEX uq_users_email         ON users (LOWER(email));  -- expression index
CREATE INDEX       idx_orders_jsonb        ON orders USING GIN (metadata); -- JSONB search

-- Partial index: only index rows matching a condition (smaller, faster)
CREATE INDEX idx_active_orders ON orders (customer_id, created_at)
    WHERE status NOT IN ('delivered', 'cancelled');

-- Covering / INCLUDE index: store extra columns in leaf node to avoid heap fetch
CREATE INDEX idx_orders_covering ON orders (customer_id)
    INCLUDE (status, amount, created_at);
-- T-SQL: CREATE INDEX idx ON orders (customer_id) INCLUDE (status, amount, created_at)
```

---

## 10. DML Reference

```sql
-- INSERT
INSERT INTO products (name, price, category) VALUES ('Widget', 9.99, 'hardware');

-- Multi-row INSERT (one round trip)
INSERT INTO products (name, price) VALUES
    ('Widget A', 9.99),
    ('Widget B', 14.99),
    ('Widget C', 4.99);

-- INSERT from SELECT
INSERT INTO order_archive
SELECT * FROM orders WHERE created_at < '2020-01-01';

-- RETURNING clause (PostgreSQL / SQLite 3.35+) — get back the inserted row
INSERT INTO orders (customer_id, amount) VALUES (42, 99.99)
RETURNING id, created_at;
-- T-SQL equiv: OUTPUT INSERTED.id, INSERTED.created_at

-- UPDATE
UPDATE orders
SET    status = 'shipped',
       shipped_at = NOW()
WHERE  id = 123;

-- UPDATE with JOIN (PostgreSQL FROM syntax)
UPDATE orders o
SET    discount_pct = p.discount
FROM   customers c
JOIN   pricing_tiers p ON c.tier_id = p.id
WHERE  o.customer_id = c.id
  AND  o.status = 'pending';
-- T-SQL uses the same FROM syntax

-- DELETE
DELETE FROM orders WHERE created_at < '2020-01-01';

-- DELETE with JOIN (PostgreSQL USING syntax)
DELETE FROM order_items oi
USING  orders o
WHERE  oi.order_id = o.id
  AND  o.status = 'cancelled';

-- TRUNCATE — DDL-level, much faster than DELETE * (skips WAL logging per row)
TRUNCATE TABLE session_tokens;
TRUNCATE TABLE session_tokens RESTART IDENTITY; -- reset sequence too
TRUNCATE TABLE session_tokens CASCADE;          -- also truncate dependent tables

-- ON CONFLICT (PostgreSQL upsert — very commonly used)
INSERT INTO user_stats (user_id, login_count, last_login)
VALUES (42, 1, NOW())
ON CONFLICT (user_id)
DO UPDATE SET
    login_count = user_stats.login_count + 1,
    last_login  = EXCLUDED.last_login;
-- EXCLUDED refers to the row that was proposed for insertion
-- T-SQL uses MERGE for this (see below)
-- MySQL uses: INSERT ... ON DUPLICATE KEY UPDATE
```

---

## 11. MERGE (SQL:2003)

```sql
-- MERGE: atomically handle insert/update/delete based on a join condition
-- T-SQL has had MERGE since SQL Server 2008
MERGE INTO inventory AS target
USING (
    SELECT product_id, quantity_delta FROM incoming_shipment
) AS source
ON target.product_id = source.product_id

WHEN MATCHED AND target.quantity + source.quantity_delta <= 0 THEN
    DELETE                          -- remove if stock drops to zero or below

WHEN MATCHED THEN
    UPDATE SET
        target.quantity    = target.quantity + source.quantity_delta,
        target.updated_at  = NOW()

WHEN NOT MATCHED BY TARGET THEN     -- exists in source, not in target
    INSERT (product_id, quantity, updated_at)
    VALUES (source.product_id, source.quantity_delta, NOW());

-- WHEN NOT MATCHED BY SOURCE  -- (T-SQL extension) exists in target, not in source
```

**Dialect comparison:**

| Operation | PostgreSQL | T-SQL | MySQL |
|-----------|-----------|-------|-------|
| Upsert | `INSERT ... ON CONFLICT DO UPDATE` | `MERGE` | `INSERT ... ON DUPLICATE KEY UPDATE` |
| Insert or ignore | `INSERT ... ON CONFLICT DO NOTHING` | `INSERT OR IGNORE` | `INSERT IGNORE` |
| Full upsert with complex logic | CTE + `INSERT ... ON CONFLICT` | `MERGE` | `REPLACE INTO` (delete+insert, not update) |

---

## 12. Transactions

```sql
BEGIN;                                  -- or: START TRANSACTION
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Explicit rollback on error
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- discover error condition
ROLLBACK;                               -- all changes undone

-- Savepoints — partial rollback within a transaction
BEGIN;
INSERT INTO orders (customer_id, amount) VALUES (42, 99.99);
SAVEPOINT sp_order_inserted;

INSERT INTO order_items (order_id, product_id, qty) VALUES (LASTVAL(), 7, 2);
-- LASTVAL() = last sequence value in this session (PostgreSQL)
-- T-SQL: SCOPE_IDENTITY()

-- something went wrong with items only
ROLLBACK TO SAVEPOINT sp_order_inserted;   -- undo items insert, keep order insert
-- fix the problem, retry items insert
COMMIT;

-- Isolation level for a specific transaction
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
...
COMMIT;
-- T-SQL: SET TRANSACTION ISOLATION LEVEL SERIALIZABLE (session-level setting)
```

### Isolation Levels vs Anomalies

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Notes |
|-----------------|-----------|---------------------|--------------|-------|
| READ UNCOMMITTED | possible | possible | possible | Reads uncommitted data; almost never appropriate |
| READ COMMITTED | prevented | possible | possible | **Default**: PostgreSQL, SQL Server, Oracle |
| REPEATABLE READ | prevented | prevented | possible | **Default**: MySQL InnoDB; re-read rows = same values |
| SERIALIZABLE | prevented | prevented | prevented | Appears as if transactions ran serially; highest lock contention |

```
Dirty read:          Txn A reads Txn B's uncommitted changes; B rolls back; A has phantom data
Non-repeatable read: A reads row, B updates+commits it, A reads same row — different value
Phantom read:        A queries range, B inserts row in range+commits, A re-queries — extra row appears
```

---

## 13. JSON Support

SQL:2016 standardized JSON. Dialects differ significantly — ANSI for reference, then the reality:

```sql
-- ANSI SQL:2016 (standard functions)
SELECT
    JSON_VALUE(metadata, '$.user.name')          AS username,        -- scalar value
    JSON_QUERY(metadata, '$.tags')               AS tags_json,       -- JSON fragment
    JSON_VALUE(metadata, '$.address.city')       AS city
FROM events;

-- JSON_TABLE: shred a JSON array into rows (ANSI SQL:2016)
SELECT e.id, t.tag
FROM   events e,
LATERAL JSON_TABLE(
    e.metadata,
    '$.tags[*]'
    COLUMNS (tag VARCHAR(100) PATH '$')
) AS t;
```

**PostgreSQL JSON operators (different from ANSI — very common):**
```sql
-- -> returns JSON, ->> returns text
SELECT metadata -> 'user' -> 'name'             AS name_json,   -- JSON type
       metadata -> 'user' ->> 'name'            AS name_text,   -- TEXT
       metadata #> '{address,city}'             AS city_json,   -- path array → JSON
       metadata #>> '{address,city}'            AS city_text;   -- path array → TEXT

-- JSONB operators (binary JSON — use JSONB not JSON in PostgreSQL)
SELECT * FROM events WHERE metadata @> '{"status": "active"}';  -- containment
SELECT * FROM events WHERE metadata ? 'user';                   -- key exists
SELECT * FROM events WHERE metadata ?| ARRAY['user','admin'];   -- any key exists
SELECT * FROM events WHERE metadata ?& ARRAY['user','admin'];   -- all keys exist

-- Index on JSONB
CREATE INDEX idx_events_metadata ON events USING GIN (metadata);
-- Supports @>, ?, ?|, ?& operators
```

**T-SQL JSON (SQL Server 2016+):**
```sql
SELECT
    JSON_VALUE(metadata, '$.user.name')     AS username,
    JSON_QUERY(metadata, '$.tags')          AS tags

-- OPENJSON: shred JSON into a rowset
SELECT *
FROM   OPENJSON(@json_var, '$.orders')
WITH (
    order_id   INT            '$.id',
    amount     DECIMAL(10,2)  '$.amount',
    status     NVARCHAR(50)   '$.status'
);

-- FOR JSON: turn rows into JSON
SELECT id, name, amount
FROM   orders
FOR JSON PATH, ROOT('orders');
```

---

## 14. Indexes

| Index Type | Data Structure | Good For | Bad For | Notes |
|------------|---------------|----------|---------|-------|
| B-tree (default) | Balanced tree | Equality, range, ORDER BY, LIKE 'prefix%' | Full-text, multi-value elements | Default for most columns |
| Hash | Hash table | Equality only (`=`) | Range, ORDER BY | In-memory often; PostgreSQL disk hash index available |
| GIN | Inverted index | Arrays, JSONB, tsvector full-text | Point lookups | High write cost; use for multi-value types |
| GiST | Generalized search tree | Geometric, full-text (tsvector), exclusion constraints | Simple equality | Supports `&&` overlap, `<->` distance |
| BRIN | Block range index | Very large tables with natural ordering (time-series append) | Random inserts, updates | Tiny index; trades I/O for accuracy |
| SP-GiST | Space-partitioned GiST | Non-balanced structures (quadtrees, tries) | General use | Specialized |

```sql
-- Composite index: column ORDER matters — leftmost prefix rule
CREATE INDEX idx_orders_cust_date ON orders (customer_id, created_at DESC);
-- Supports: WHERE customer_id = 42
--           WHERE customer_id = 42 AND created_at > '2024-01-01'
-- Does NOT support: WHERE created_at > '2024-01-01'  (customer_id missing)

-- Partial index: only index a subset of rows
CREATE INDEX idx_pending_orders ON orders (customer_id, created_at)
WHERE status = 'pending';
-- Smaller index; only consulted for queries that include WHERE status = 'pending'

-- Covering index (INCLUDE columns): avoids heap fetch for covered queries
CREATE INDEX idx_orders_covering ON orders (customer_id)
    INCLUDE (status, amount, created_at);
-- "Index Only Scan" possible: all needed columns are in the index leaf node
-- Without INCLUDE: Index Scan fetches the index, then fetches each heap page

-- Expression index: index on computed value
CREATE UNIQUE INDEX uq_users_email ON users (LOWER(email));
-- Query MUST use the same expression: WHERE LOWER(email) = 'alice@example.com'
-- WHERE email = 'alice@example.com'  does NOT use this index
```

---

## 15. Query Plan Basics

```sql
-- Show the plan without running the query
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;

-- Run the query and show actual vs estimated stats
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE customer_id = 42;

-- T-SQL equivalent:
-- SET STATISTICS IO ON; SET STATISTICS TIME ON;
-- or: query → "Include Actual Execution Plan" in SSMS
```

**Key plan nodes:**

| Node | Meaning | When it appears |
|------|---------|-----------------|
| Seq Scan | Full table scan | No usable index, or table too small to bother with index |
| Index Scan | Use index + heap fetch per matching row | Index found, low selectivity (few matching rows) |
| Index Only Scan | Use index, skip heap entirely | Covering index satisfies all needed columns |
| Bitmap Index Scan | Phase 1: scan index, build bitmap of matching heap pages | Moderate selectivity — too many hits for Index Scan, too few for Seq Scan |
| Bitmap Heap Scan | Phase 2: use bitmap to fetch heap pages in physical order | Always paired with Bitmap Index Scan above it in the plan |
| Nested Loop | For each outer row, probe inner | Small inner set, indexed inner lookup |
| Hash Join | Build hash table on smaller side, probe with larger | Large unsorted sets |
| Merge Join | Merge two sorted inputs | Both inputs already sorted on join key |
| Sort | Explicit sort | ORDER BY, GROUP BY without index, Merge Join setup |
| Hash Aggregate | Aggregate via hash table | GROUP BY on unsorted data |
| GroupAggregate | Aggregate pre-sorted stream | GROUP BY on sorted data |

**Bitmap Heap Scan — the two-phase pattern (no SQL Server equivalent):**
```
SQL Server approach:     index seek → key lookup per matching row (individual heap fetches)
PostgreSQL approach:     Bitmap Index Scan → collect ALL matching row locations first
                         Bitmap Heap Scan  → fetch heap pages in physical order (one pass)

Why it matters: random I/O (key lookup per row) vs sequential I/O (sorted heap page reads).
For 5,000 matching rows spread across 50,000 heap pages, the bitmap approach is far cheaper.

Plan appearance:
  ->  Bitmap Heap Scan on orders  (cost=142..8921 rows=4821 width=64)
        Recheck Cond: (customer_id = 42)
        ->  Bitmap Index Scan on idx_orders_customer  (cost=0.00..140 rows=4821 width=0)
              Index Cond: (customer_id = 42)

"Recheck Cond" appears because the bitmap is lossy at high row counts (page-level not row-level).
If you see high Recheck Cond filtering, the index selectivity is low — consider a partial index.

SQL Server analogy: closest is "Index Seek + RID Lookup" but the bitmap batching is unique.
T-SQL Query Store will show similar plan shapes differently — no direct 1:1 mapping.
```

**Reading cost estimates:**
```
Seq Scan on orders  (cost=0.00..4521.00 rows=200000 width=64)
                          ─────┬─────  ─────┬────── ───┬──── ─┬──
                    startup cost│  total cost│    est rows│  row width│
                    (first row)   (all rows)  (planner)   (bytes)

EXPLAIN ANALYZE adds:
  actual time=0.052..189.4 rows=197342 loops=1
                             ─────┬──────
                         actual rows returned
```

Significant deviations between estimated and actual rows → stale statistics → run `ANALYZE`.

---

## 16. Temporal Tables (SQL:2011)

```sql
-- System-versioned temporal table: database automatically tracks row history
CREATE TABLE employees (
    id          INT             NOT NULL PRIMARY KEY,
    name        VARCHAR(100)    NOT NULL,
    salary      NUMERIC(10,2)   NOT NULL,
    dept_id     INT             NOT NULL,
    sys_start   TIMESTAMPTZ     GENERATED ALWAYS AS ROW START,
    sys_end     TIMESTAMPTZ     GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME (sys_start, sys_end)
) WITH (SYSTEM VERSIONING);   -- MariaDB syntax; PostgreSQL needs pg_temporal extension

-- T-SQL (SQL Server 2016+):
CREATE TABLE employees (
    id          INT             NOT NULL PRIMARY KEY,
    name        NVARCHAR(100)   NOT NULL,
    salary      DECIMAL(10,2)   NOT NULL,
    dept_id     INT             NOT NULL,
    ValidFrom   DATETIME2       GENERATED ALWAYS AS ROW START NOT NULL,
    ValidTo     DATETIME2       GENERATED ALWAYS AS ROW END   NOT NULL,
    PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.employees_history));

-- Query historical data (T-SQL):
SELECT * FROM employees FOR SYSTEM_TIME AS OF '2023-06-01';
SELECT * FROM employees FOR SYSTEM_TIME BETWEEN '2023-01-01' AND '2023-12-31';
SELECT * FROM employees FOR SYSTEM_TIME ALL;   -- all versions, current + historical
```

---

## 17. Decision Cheat Sheet

| You need to... | Use |
|----------------|-----|
| Running total / cumulative sum | `SUM(col) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)` |
| Rank rows within a group | `ROW_NUMBER() / RANK() / DENSE_RANK() OVER (PARTITION BY ...)` |
| Compare a row to the previous/next | `LAG(col) / LEAD(col) OVER (ORDER BY ...)` |
| Department average alongside each row (no collapse) | `AVG(col) OVER (PARTITION BY dept)` |
| Top-1 record per group | `ROW_NUMBER() OVER (PARTITION BY g ORDER BY ...)` in CTE, `WHERE rn = 1` |
| Reuse a subquery expression multiple times | CTE (`WITH name AS (...)`) |
| Traverse a tree / hierarchy | Recursive CTE (`WITH RECURSIVE`) |
| Pivot rows into columns | `CASE WHEN + GROUP BY` or `PIVOT` (T-SQL / BigQuery) |
| Multi-level subtotals (dept + region + total) | `GROUP BY GROUPING SETS / ROLLUP / CUBE` |
| Count distinct without full scan (approximate) | `approx_count_distinct()` (BigQuery) / `HLL_COUNT` (Snowflake) |
| Upsert (insert or update) | PostgreSQL: `INSERT ... ON CONFLICT DO UPDATE` / T-SQL: `MERGE` |
| Delete or update rows matching another table | `DELETE USING` / `UPDATE FROM` (PostgreSQL) / `UPDATE JOIN` |
| Conditional aggregation | `SUM(col) FILTER (WHERE condition)` or `SUM(CASE WHEN ... END)` |
| Avoid nested subqueries for readability | CTE — always prefer over nested `(SELECT ... FROM (SELECT ...))` |
| Find rows that exist in A but not B | `EXCEPT` / `NOT EXISTS (SELECT ...)` |
| Find customers with no matching orders | `LEFT JOIN ... WHERE right_side.id IS NULL` |
| Check if a JSON key exists | PostgreSQL: `metadata ? 'key'` with GIN index |
| Track row history automatically | System-versioned temporal table |

---

## 18. Common Confusion Points

**SELECT execution order vs write order**
WHERE runs before SELECT — you cannot use a SELECT alias in WHERE or GROUP BY.
HAVING runs after GROUP BY — can filter on aggregate expressions. WHERE cannot.
ORDER BY runs last — can use SELECT aliases here (special exception).

**NULL behavior in comparisons**
```
NULL = NULL  → UNKNOWN (not TRUE)
NULL != 5    → UNKNOWN (not FALSE)
NOT UNKNOWN  → UNKNOWN
```
`WHERE col = NULL` never returns rows. Always use `IS NULL` / `IS NOT NULL`.
`WHERE col IN (1, NULL)` — the NULL arm produces UNKNOWN, no extra rows selected.
`WHERE col NOT IN (SELECT ... that returns NULL)` — returns zero rows (trap).

**COUNT(*) vs COUNT(col)**
`COUNT(*)` counts all rows including those with NULLs in every column.
`COUNT(col)` counts only rows where `col IS NOT NULL`.
`COUNT(DISTINCT col)` counts distinct non-NULL values.

**UNION vs UNION ALL**
`UNION ALL`: multiset union, keeps all rows. No extra cost. Use by default.
`UNION`: deduplicates via sort or hash. Measurable cost. Use only when semantically required.

**HAVING vs WHERE**
`WHERE`: filters individual rows before grouping. Cannot reference aggregate functions.
`HAVING`: filters groups after aggregation. Can reference aggregate functions.
```sql
-- WRONG: aggregate in WHERE
WHERE COUNT(*) > 5

-- RIGHT: aggregate in HAVING
GROUP BY customer_id
HAVING COUNT(*) > 5
```

**CTE materialization**
CTEs are not always a performance barrier. PostgreSQL 14+ inlines them by default.
SQL Server always inlines (treats as a view). Pre-14 PostgreSQL materializes (optimization fence).
A CTE is not a temp table — do not expect it to be physically stored unless explicitly materialized.

**ROW_NUMBER vs RANK vs DENSE_RANK with ties**
```
salary: 100, 90, 90, 80
ROW_NUMBER:  1, 2, 3, 4    ← arbitrary tiebreak, always unique
RANK:        1, 2, 2, 4    ← gap after tied positions
DENSE_RANK:  1, 2, 2, 3    ← no gap
```
For deduplication (top-1-per-group), use ROW_NUMBER — RANK can return multiple rows at rank 1.

**ROWS vs RANGE frame in window functions**
`ROWS BETWEEN n PRECEDING AND CURRENT ROW` — exactly n physical rows.
`RANGE BETWEEN n PRECEDING AND CURRENT ROW` — all rows within n value units; multiple rows can share
the same ORDER BY value and all fall within the range.
Default when ORDER BY is present but no frame specified: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
Default with no ORDER BY: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` (entire partition).

**Correlated subquery vs JOIN performance**
A correlated subquery executes once per outer row — O(n) executions.
Equivalent JOIN (or window function) executes once — O(1) with proper indexes.
Replacing correlated subqueries with CTEs + JOINs or window functions is a standard tuning technique.

**TIMESTAMP vs TIMESTAMPTZ (PostgreSQL)**
`TIMESTAMP`: no timezone — stores exactly what you give it; dangerous for apps in multiple timezones.
`TIMESTAMPTZ`: stores in UTC, displays in session timezone. Always use `TIMESTAMPTZ`.
T-SQL `DATETIME2` has no timezone; use `DATETIMEOFFSET` for the equivalent.

**T-SQL TOP vs ANSI LIMIT**
```sql
-- T-SQL (before FETCH FIRST):
SELECT TOP 10 * FROM orders ORDER BY created_at DESC;
SELECT TOP 10 PERCENT * FROM orders ORDER BY created_at DESC;

-- ANSI SQL:2008 (PostgreSQL, Oracle 12c+, DB2):
SELECT * FROM orders ORDER BY created_at DESC FETCH FIRST 10 ROWS ONLY;

-- PostgreSQL shorthand (non-standard but universal):
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10 OFFSET 20;
```
