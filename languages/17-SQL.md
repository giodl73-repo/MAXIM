# Language: SQL

> Declarative relational data manipulation — set-based logic, relational algebra in practice, three-valued logic (NULL), and window functions. You tell it WHAT, not HOW.

---

## Type System Snapshot

| Axis | SQL |
|------|-----|
| Binding | N/A — query planner decides execution |
| Typing | Static (schema-defined), strong within a query |
| Strength | Strong within types; casting required across types |
| Type system | Nominal (by column definition) |
| Type inference | Minimal — expressions infer from operands |
| Memory model | Server-managed (MVCC, buffer pool, WAL) |

---

## SQL Execution Pipeline & Relational Model Landscape

```
QUERY EXECUTION PIPELINE
─────────────────────────────────────────────────────────────────────────

  SQL text           "SELECT u.name, COUNT(o.id)
  (your query)        FROM users u JOIN orders o ON u.id = o.user_id
                       WHERE u.active = true GROUP BY u.name"
       │
       ▼
   Parser              Validates syntax; builds parse tree
       │               Fails fast: syntax errors caught here
       ▼
   Binder /            Resolves names to schema objects
   Name Resolution     (table refs → actual tables, column names → types)
       │               Fails: "column does not exist", "ambiguous column"
       ▼
   Logical Plan        Relational algebra tree
                       σ(active=true) ⋈ (users, orders) → π(name) → γ(COUNT)
       │               Abstract — no physical decisions yet
       ▼
   Optimizer           The planner's job: find the cheapest physical plan
   ┌────────────────────────────────────────────────────────────────┐
   │  • Index selection: can we seek instead of scan?               │
   │  • Join reordering: smaller table on the outer loop            │
   │  • Predicate pushdown: filter early to reduce row count        │
   │  • Join algorithm: nested loop vs hash join vs merge join      │
   │  • Materialization: should a CTE be computed once or inlined?  │
   └────────────────────────────────────────────────────────────────┘
       │
       ▼
   Physical Plan       Concrete operators: IndexScan, HashJoin, Sort, Agg
       │               EXPLAIN / EXPLAIN ANALYZE shows this tree
       ▼
   Executor            Runs the plan; pulls rows through operator tree
       │
       ▼
   Result Set          Rows returned to client

─────────────────────────────────────────────────────────────────────────
C# / LINQ PARALLEL:

  C# LINQ:  IQueryable<T> expression tree
                │
                ▼
            EF Core / LINQ provider
                │
                ▼
            SQL text generated  ──►  Same pipeline above
                                     (you're writing logical intent;
                                      provider + optimizer do the rest)

  Key insight: IQueryable defers execution exactly like SQL defers HOW.
  Both are declarative transformations over sets. The "query object" in
  LINQ is the same as the logical plan — not yet physical.

─────────────────────────────────────────────────────────────────────────
RELATIONAL MODEL FOUNDATION:

  Relation  = table (set of tuples with named attributes)
  Tuple     = row
  Attribute = column (has a domain / type)
  Key       = minimal set of attributes that uniquely identifies a tuple
  Foreign key = attribute(s) referencing a key in another relation

  Relational algebra operators → SQL surface syntax:
    σ (selection)     → WHERE
    π (projection)    → SELECT col1, col2
    ⋈ (join)          → JOIN
    γ (grouping/agg)  → GROUP BY + aggregate functions
    ∪ (union)         → UNION
    − (difference)    → EXCEPT
    ∩ (intersection)  → INTERSECT
```

## Dialect Note

SQL is a standard (ANSI/ISO) but every database adds extensions. This file covers:
- **Standard SQL** (ANSI) — marked `STANDARD`
- **PostgreSQL** — marked `PG` (most complete SQL implementation)
- **T-SQL** (SQL Server) — marked `TSQL` (your likely context)
- **MySQL/MariaDB** — noted where different

---

## Syntax Reference Card

### Data Types

```sql
-- Numeric
INTEGER / INT           -- 4 bytes, -2B to 2B
BIGINT                  -- 8 bytes
SMALLINT               -- 2 bytes
DECIMAL(precision, scale)  -- exact numeric, e.g. DECIMAL(10,2)
NUMERIC(p,s)           -- same as DECIMAL
FLOAT / REAL           -- approximate (IEEE 754)
FLOAT(n)               -- n-bit precision

-- String
CHAR(n)                -- fixed-width, padded with spaces
VARCHAR(n)             -- variable-width, max n chars
TEXT / CLOB            -- unlimited text
NVARCHAR(n)            -- Unicode (T-SQL)

-- Binary
BYTEA                  -- PG
VARBINARY(n)           -- T-SQL/MySQL
BLOB                   -- MySQL

-- Date/Time
DATE                   -- date only
TIME                   -- time only
TIMESTAMP              -- date + time (no timezone)
TIMESTAMPTZ            -- with timezone (PG: TIMESTAMP WITH TIME ZONE)
INTERVAL               -- duration (PG)

-- Boolean
BOOLEAN / BOOL         -- true/false/null (PG, ANSI)
BIT                    -- 0/1 (T-SQL/MySQL)

-- Other
UUID                   -- PG: uuid type
JSON / JSONB           -- PG: json (text) / jsonb (binary, indexed)
ARRAY                  -- PG: int[], text[]
ENUM                   -- MySQL/PG (PG: CREATE TYPE)
```

### Equality & Comparison

```sql
-- THE critical SQL rule: NULL is not equal to anything, including NULL
NULL = NULL     -- UNKNOWN (not TRUE!)
NULL != NULL    -- UNKNOWN (not TRUE!)
NULL = 5        -- UNKNOWN

-- Always use IS NULL / IS NOT NULL for null checks
WHERE col IS NULL
WHERE col IS NOT NULL

-- Regular comparisons
=   <>  (or !=)   <   >   <=   >=

-- Null-safe equality (PG)
col IS NOT DISTINCT FROM value   -- true if both NULL, or both equal
col IS DISTINCT FROM value       -- true if different, treating NULLs as equal

-- Pattern matching
LIKE 'prefix%'         -- % = any chars, _ = any one char
ILIKE 'prefix%'        -- case-insensitive (PG)
SIMILAR TO 'a(b|c)%'   -- SQL regex (PG)
~ 'pattern'            -- POSIX regex (PG: ~ case-sensitive, ~* case-insensitive)

-- Range
BETWEEN 1 AND 10       -- inclusive (1 <= x <= 10)
NOT BETWEEN 1 AND 10

-- Set membership
IN (1, 2, 3)
NOT IN (1, 2, 3)       -- WARNING: NOT IN with NULL = always unknown!
IN (SELECT id FROM t)  -- subquery form

-- Exists
EXISTS (SELECT 1 FROM t WHERE cond)
NOT EXISTS (SELECT 1 FROM t WHERE cond)
```

### Logical Operators

```sql
-- Three-valued logic: TRUE, FALSE, UNKNOWN (NULL propagates)
AND     -- TRUE AND NULL = UNKNOWN; FALSE AND NULL = FALSE
OR      -- TRUE OR NULL = TRUE; FALSE OR NULL = UNKNOWN
NOT     -- NOT NULL = UNKNOWN

-- Truth table for AND with NULL
-- T AND T = T
-- T AND F = F
-- T AND NULL = NULL (UNKNOWN)
-- F AND NULL = FALSE (short-circuit!)

-- Bitwise (T-SQL / MySQL)
&   |   ^   ~   <<   >>

-- Bitwise (PG standard functions)
col & mask          -- bitwise AND
col | mask          -- bitwise OR
```

### Queries

```sql
-- Full SELECT syntax
SELECT DISTINCT TOP 10 col1, col2, expr AS alias
FROM table1 t1
    INNER JOIN table2 t2 ON t1.id = t2.fk_id
    LEFT JOIN table3 t3 ON t1.id = t3.fk_id
WHERE cond1 AND cond2
GROUP BY col1, col2
HAVING COUNT(*) > 5
ORDER BY col1 ASC, col2 DESC
LIMIT 100 OFFSET 50     -- PG/MySQL
FETCH FIRST 100 ROWS ONLY  -- ANSI standard
OFFSET 50 ROWS FETCH NEXT 100 ROWS ONLY  -- ANSI
;

-- JOIN types
INNER JOIN      -- only matching rows from both
LEFT JOIN       -- all from left, matching from right (NULL if no match)
RIGHT JOIN      -- all from right, matching from left
FULL JOIN       -- all from both, NULL where no match
CROSS JOIN      -- cartesian product
LATERAL JOIN    -- PG: reference columns from left side in right subquery
```

### Collections / Aggregation

```sql
-- Aggregate functions
COUNT(*)                -- count all rows (including NULLs)
COUNT(col)              -- count non-NULL values
COUNT(DISTINCT col)     -- count unique non-NULL values
SUM(col)
AVG(col)
MAX(col)  MIN(col)
STRING_AGG(col, ',')    -- PG: aggregate to string
ARRAY_AGG(col)          -- PG: aggregate to array
JSON_AGG(col)           -- PG: aggregate to JSON array

-- GROUP BY
SELECT dept, COUNT(*), AVG(salary)
FROM employees
GROUP BY dept
HAVING COUNT(*) > 5

-- ROLLUP / CUBE (hierarchical grouping)
GROUP BY ROLLUP(dept, team)    -- subtotals and grand total
GROUP BY CUBE(dept, team)      -- all combinations

-- Window functions (don't collapse rows — unlike GROUP BY)
SELECT
    id,
    salary,
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank,
    RANK()       OVER (PARTITION BY dept ORDER BY salary DESC),
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC),
    SUM(salary)  OVER (PARTITION BY dept) AS dept_total,
    AVG(salary)  OVER (PARTITION BY dept) AS dept_avg,
    LAG(salary)  OVER (ORDER BY hire_date) AS prev_salary,
    LEAD(salary) OVER (ORDER BY hire_date) AS next_salary,
    SUM(salary)  OVER (ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

### Control Flow

```sql
-- CASE expression (SQL's conditional expression)
SELECT
    CASE status
        WHEN 'A' THEN 'Active'
        WHEN 'I' THEN 'Inactive'
        ELSE 'Unknown'
    END AS status_label
FROM users;

-- Searched CASE
SELECT
    CASE
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 50000  THEN 'Mid'
        ELSE 'Low'
    END AS band
FROM employees;

-- COALESCE — first non-NULL value
COALESCE(col1, col2, 'default')

-- NULLIF — returns NULL if two values are equal
NULLIF(col, 0)      -- returns NULL if col = 0, else returns col

-- GREATEST / LEAST (PG, MySQL)
GREATEST(a, b, c)   -- max of args (ignores NULLs — use with care)

-- IIF (T-SQL shorthand)
IIF(cond, true_val, false_val)  -- T-SQL only

-- Procedural (T-SQL stored procedures / PL/pgSQL)
-- T-SQL:
IF @x > 0
BEGIN
    SELECT 'positive';
END
ELSE
BEGIN
    SELECT 'non-positive';
END;

WHILE @i < 10
BEGIN
    SET @i = @i + 1;
END;

-- PL/pgSQL (PostgreSQL):
DO $$
DECLARE
    v_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM users;
    IF v_count > 0 THEN
        RAISE NOTICE 'Has users';
    END IF;
END;
$$;
```

### Strings

```sql
-- String literals: single quotes only (double quotes = identifiers in ANSI/PG)
'hello'
'it''s escaped'         -- double the quote to escape
E'escape \n here'       -- PG: escape string
$$dollar quoted$$       -- PG: no escaping needed

-- Concatenation
'hello' || ' ' || 'world'  -- ANSI / PG
CONCAT('hello', ' ', 'world')  -- MySQL / T-SQL (handles NULL as empty)
'hello' + ' world'          -- T-SQL

-- String functions
UPPER(s)  LOWER(s)
LENGTH(s) / LEN(s)          -- PG uses LENGTH; T-SQL uses LEN
SUBSTRING(s, start, length) -- ANSI (1-indexed!)
SUBSTR(s, start, length)    -- MySQL/PG alias
LEFT(s, n)  RIGHT(s, n)
TRIM(s)  LTRIM(s)  RTRIM(s)
REPLACE(s, old, new)
POSITION('sub' IN s)        -- ANSI
CHARINDEX('sub', s)         -- T-SQL
STRPOS(s, 'sub')            -- PG
SPLIT_PART(s, ',', 2)       -- PG: split and get nth part
REGEXP_REPLACE(s, pattern, replacement)  -- PG
FORMAT('%s is %d', name, age)   -- PG: printf-style
CAST(x AS VARCHAR)
x::VARCHAR                  -- PG shorthand cast
```

### NULL Handling

```sql
-- NULL is pervasive — every operation with NULL returns NULL
-- Three-valued logic: result of comparison with NULL = UNKNOWN
-- UNKNOWN in WHERE clause = row excluded (treated as false)

-- Checking for NULL
WHERE col IS NULL
WHERE col IS NOT NULL

-- Providing defaults for NULL
COALESCE(col, 0)            -- first non-null
ISNULL(col, 0)              -- T-SQL
IFNULL(col, 0)              -- MySQL
NVL(col, 0)                 -- Oracle

-- NULL in aggregates
SUM(col)                    -- ignores NULL
COUNT(col)                  -- ignores NULL
COUNT(*)                    -- counts NULLs (all rows)
AVG(col)                    -- ignores NULL (denominator is non-null count)

-- NULL in joins
-- LEFT JOIN: right side columns are NULL for unmatched left rows
-- INNER JOIN: rows with NULL in join key are excluded

-- NULL in NOT IN — classic trap
SELECT * FROM a WHERE id NOT IN (SELECT id FROM b)
-- If b contains any NULL, the result is EMPTY (UNKNOWN propagates)
-- Use NOT EXISTS instead:
SELECT * FROM a WHERE NOT EXISTS (SELECT 1 FROM b WHERE b.id = a.id)
```

### CTEs and Subqueries

```sql
-- Common Table Expression (CTE)
WITH active_users AS (
    SELECT * FROM users WHERE status = 'active'
),
recent_orders AS (
    SELECT user_id, MAX(created_at) AS last_order
    FROM orders
    GROUP BY user_id
)
SELECT u.name, o.last_order
FROM active_users u
LEFT JOIN recent_orders o ON u.id = o.user_id;

-- Recursive CTE (for hierarchical data)
WITH RECURSIVE employee_tree AS (
    SELECT id, name, manager_id, 0 AS depth
    FROM employees
    WHERE manager_id IS NULL          -- root
    UNION ALL
    SELECT e.id, e.name, e.manager_id, t.depth + 1
    FROM employees e
    JOIN employee_tree t ON e.manager_id = t.id
)
SELECT * FROM employee_tree ORDER BY depth, name;

-- Subquery types
SELECT * FROM (SELECT ...) AS sub                    -- derived table
WHERE id IN (SELECT id FROM ...)                     -- subquery
WHERE EXISTS (SELECT 1 FROM ...)                     -- exists
SELECT (SELECT COUNT(*) FROM t2 WHERE t2.fk = t1.id) -- scalar subquery
FROM t1
```

### DML

```sql
-- Insert
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email)
    SELECT name, email FROM import_table WHERE valid = true;

-- Upsert (insert or update on conflict)
-- PG:
INSERT INTO users (id, name) VALUES (1, 'Alice')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name;

-- T-SQL MERGE:
MERGE users AS target
USING (VALUES (1, 'Alice')) AS src(id, name)
ON target.id = src.id
WHEN MATCHED THEN UPDATE SET target.name = src.name
WHEN NOT MATCHED THEN INSERT (id, name) VALUES (src.id, src.name);

-- Update
UPDATE users SET name = 'Bob', updated_at = NOW()
WHERE id = 42;

UPDATE users u
SET tier = 'gold'
FROM orders o                   -- PG: update with join
WHERE u.id = o.user_id
  AND o.total > 10000;

-- Delete
DELETE FROM users WHERE status = 'inactive';

TRUNCATE TABLE temp_data;      -- fast delete all (no WHERE, minimal logging)
```

### Transactions

```sql
BEGIN;              -- or START TRANSACTION
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;             -- or ROLLBACK;

-- Savepoints
SAVEPOINT sp1;
-- ... do work ...
ROLLBACK TO SAVEPOINT sp1;  -- undo to savepoint
RELEASE SAVEPOINT sp1;      -- discard savepoint

-- Isolation levels (higher = more isolation, more contention)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;     -- default most DBs
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;    -- no non-repeatable reads
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;       -- strongest, slowest
```

### Indexes & Performance

```sql
-- Create index
CREATE INDEX idx_users_email ON users(email);
CREATE UNIQUE INDEX idx_users_email ON users(email);
CREATE INDEX idx_partial ON orders(user_id) WHERE status = 'active';  -- partial
CREATE INDEX idx_covering ON orders(user_id) INCLUDE (total, created_at);  -- covering

-- Explain (PostgreSQL)
EXPLAIN SELECT * FROM users WHERE email = 'alice@example.com';
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;  -- actually runs the query

-- Explain (T-SQL)
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- or use: Display Estimated Execution Plan (Ctrl+L in SSMS)

-- Key patterns for performance
-- 1. Avoid functions on indexed columns in WHERE:
WHERE UPPER(email) = 'ALICE@EXAMPLE.COM'    -- can't use index on email!
WHERE email = LOWER('ALICE@EXAMPLE.COM')    -- CAN use index [OK]

-- 2. N+1 problem — use JOINs not loops
-- 3. SELECT only needed columns — avoid SELECT *
-- 4. Use EXISTS over IN for correlated queries
-- 5. ANALYZE (PG) / UPDATE STATISTICS (T-SQL) to keep planner current
```

---

## What Makes It Distinct

1. **Set-based thinking** — SQL operates on sets of rows, not individual records. The query optimizer finds the execution plan. You declare WHAT you want; the engine decides HOW.
2. **Three-valued logic** — NULL is neither TRUE nor FALSE; it's UNKNOWN. Every comparison with NULL returns UNKNOWN. `NOT IN` with a NULL in the list = always empty. This bites everyone eventually.
3. **Window functions** — `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` — compute aggregates across related rows WITHOUT collapsing them. Indispensable for ranking, running totals, gaps-and-islands.
4. **MVCC (Multi-Version Concurrency Control)** — PostgreSQL and others give each transaction a snapshot of the database. Readers don't block writers. Snapshot isolation means transactions see consistent state.
5. **Declarative + no variables (in standard SQL)** — SQL has no variables, no loops, no assignment (in standard SELECT). Pure transformation. Procedural extensions (T-SQL, PL/pgSQL) add them.

---

## Common Query Patterns

```sql
-- Top N per group
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
    FROM employees
)
SELECT * FROM ranked WHERE rn <= 3;

-- Gaps and islands (find consecutive sequences)
WITH numbered AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM active_records
)
SELECT MIN(id), MAX(id)
FROM numbered
GROUP BY id - rn   -- constant for consecutive sequences

-- Pivot (rows to columns) — PG
SELECT
    MAX(CASE WHEN month = 1 THEN revenue END) AS jan,
    MAX(CASE WHEN month = 2 THEN revenue END) AS feb
FROM monthly_revenue;

-- Running total
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) AS running_total
FROM transactions;

-- Percentile
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM employees;
```

---

## T-SQL vs PostgreSQL Quick Differences

| Feature | T-SQL (SQL Server) | PostgreSQL |
|---------|-------------------|-----------|
| Top N | `SELECT TOP 10 *` | `LIMIT 10` |
| String concat | `+` | `||` or `CONCAT()` |
| If/else | `IF ... BEGIN END` | `DO $$ IF ... END IF; $$` |
| Identity column | `IDENTITY(1,1)` | `SERIAL` or `GENERATED ALWAYS AS IDENTITY` |
| String interpolation | None | None (use `format()` in PL/pgSQL) |
| GUID | `UNIQUEIDENTIFIER` | `UUID` |
| JSON | `JSON` (text) | `JSON` (text) + `JSONB` (binary, indexed) |
| Regex | `LIKE` only | `~` (POSIX), `SIMILAR TO`, `regexp_match()` |
| Array type | `TABLE` type | `integer[]`, `text[]`, etc. |
| CTE | `WITH cte AS (...)` | Same — both support recursive CTEs |

---

## Decision Cheat Sheet

### Query structure: CTE vs subquery vs temp table

| Approach | Use when | Trade-off |
|----------|----------|-----------|
| CTE (`WITH`) | Query is complex; intermediate step needs a readable name; recursive traversal | Optimizer may inline it (not always materialized) — same performance as subquery in most engines |
| Subquery (`SELECT ... FROM (SELECT ...)`) | Simple one-off derivation; no reuse needed | Can be harder to read when nested 3+ levels deep |
| Temp table (`CREATE TABLE #t` / `CREATE TEMP TABLE`) | Result set is large and reused multiple times in the same session; need an index on the intermediate result | Explicit materialization — always written to disk/memory; can add indexes; ideal for multi-step ETL |
| CTE with `MATERIALIZED` hint (PG) | Force CTE to be computed once even if optimizer would inline it | Use when CTE has side effects or when re-execution is expensive |

### Existence check: `JOIN` vs `EXISTS` vs `IN`

| Pattern | Use when | NULL behavior |
|---------|----------|--------------|
| `WHERE id IN (SELECT id FROM b)` | Small, static list; subquery has no NULLs | Dangerous if subquery can return NULL — NOT IN becomes empty |
| `WHERE EXISTS (SELECT 1 FROM b WHERE b.id = a.id)` | Correlated existence check; subquery may return NULLs | Safe — EXISTS returns TRUE/FALSE, not UNKNOWN |
| `INNER JOIN` | You also need columns from the joined table | Produces duplicates if b has multiple matches per a.id — use DISTINCT or EXISTS instead |
| `LEFT JOIN ... WHERE b.id IS NULL` | Anti-join (rows in a NOT in b) | Explicit; works reliably; common pattern |

**Default rule**: Use `EXISTS` / `NOT EXISTS` for existence checks. It's NULL-safe and the optimizer usually handles it as well as IN.

### Aggregation: window function vs `GROUP BY`

| Approach | Use when | What you get |
|----------|----------|-------------|
| `GROUP BY` + aggregate | You want one summary row per group | Collapses rows — you lose individual row data |
| Window function `OVER (PARTITION BY ...)` | You want the aggregate value AND the individual row | Retains all rows; aggregate is a new column alongside originals |

**Example**: "Show each employee's salary and their department's average salary" — requires a window function. GROUP BY would collapse to one row per department.

### Set operations: `UNION` vs `UNION ALL`

| Operator | Behavior | Use when |
|----------|----------|----------|
| `UNION` | Deduplicates rows (implicit DISTINCT) | You genuinely need unique rows across two sets; accept sort/hash cost |
| `UNION ALL` | Returns all rows including duplicates | Default — use unless dedup is required; significantly faster |

**Rule**: Always use `UNION ALL` unless you explicitly need deduplication. The sort/hash step for `UNION` is expensive on large sets.

### Filter placement: `HAVING` vs `WHERE`

| Clause | Filters | Runs after | Use when |
|--------|---------|-----------|----------|
| `WHERE` | Individual rows | Row scan (before GROUP BY) | Filtering on base column values; can use indexes |
| `HAVING` | Groups / aggregates | GROUP BY + aggregation | Filtering on aggregate results (`HAVING COUNT(*) > 5`) |

**Performance rule**: Push as much filtering as possible into WHERE. The optimizer can use indexes on WHERE predicates; HAVING runs on the already-aggregated result.

### Index type selection

| Index type | Use when | Notes |
|------------|----------|-------|
| B-tree (default) | Equality, range, ORDER BY, LIKE 'prefix%' | Default in every DB; handles most cases |
| Hash index (PG) | Equality-only lookups; no range queries needed | Faster for pure equality; no range support; smaller |
| Partial index | Only a subset of rows is queried (e.g., `WHERE status = 'active'`) | Much smaller index; high selectivity gains |
| Covering index (`INCLUDE`) | Query reads only indexed columns — avoids heap fetch | Index-only scans; reduces I/O significantly for frequent queries |
| GIN (PG) | Full-text search, JSONB containment (`@>`), array membership | Inverted index — multiple keys per row |
| GiST (PG) | Geometric types, range types, full-text (tsvector) | Generalized search tree |

---

## Bridge: SQL → Power Query M

You know both T-SQL and Power Query M from ADF pipelines. They're both relational algebra in different surface syntax — the conceptual mapping is direct.

```
SQL Operation          Power Query M Equivalent        Notes
─────────────────────────────────────────────────────────────────────────

SELECT col1, col2      Table.SelectColumns(           Projection — pick columns
FROM t                   t, {"col1", "col2"})

SELECT *               t                              No-op in M — table is already all columns
FROM t

WHERE col > 5          Table.SelectRows(              Filter — row predicate
                         t, each [col] > 5)

SELECT col1,           Table.Group(                   Grouping + aggregation
  COUNT(*) AS n          t,
FROM t                   {"col1"},
GROUP BY col1            {{"n", each Table.RowCount(_),
                              Int64.Type}})

JOIN (INNER)           Table.Join(                    Join two tables
                         t1, "key_col",
                         t2, "key_col",
                         JoinKind.Inner)
                       -- or Table.NestedJoin + Table.ExpandTableColumn

LEFT JOIN              Table.Join(... JoinKind.LeftOuter)

ORDER BY col ASC       Table.Sort(                    Sort
                         t, {{"col", Order.Ascending}})

SELECT TOP 10          Table.FirstN(t, 10)            Limit rows

SELECT DISTINCT        Table.Distinct(t)              Deduplication

UNION ALL              Table.Combine({t1, t2})        Append tables

WITH cte AS (...)      let cte = ... in ...           Named intermediate step — M's let..in
SELECT * FROM cte        (M's let block is the CTE pattern)

CASE WHEN ... THEN     if ... then ... else ...       M uses functional if expression
  ELSE END               (inside Table.AddColumn or Table.TransformColumns)

```

**Key conceptual bridge**: Both SQL and Power Query M are declarative transformations over tabular data — you describe the shape of the output, not the iteration. The difference is surface syntax and evaluation model:

| Dimension | SQL | Power Query M |
|-----------|-----|---------------|
| Evaluation | Set-based; optimizer chooses physical plan | Lazy functional pipeline; evaluated top-to-bottom |
| State | Stateless queries; transactions handle state | Immutable steps — each `let` binding is a new table |
| Extensibility | UDFs, stored procedures | Custom functions, `List.Accumulate` |
| Streaming | Cursor / row-by-row in procedural | M folds steps into source query pushdown where possible |
| Null handling | Three-valued logic (UNKNOWN) | `null` propagates; use `Value.ReplaceErrorWith` |

**ADF context**: When you write a Data Flow in ADF, the transformation steps are M-like logical operations that ADF compiles down to Spark. The SQL you write in ADF SQL activities bypasses this layer and goes directly to the engine's query pipeline above. Understanding both lets you choose: SQL activity (full engine power, T-SQL syntax) vs. Data Flow (visual pipeline, M-style operations on Spark).
