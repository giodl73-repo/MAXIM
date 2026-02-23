# T-SQL — SQL Server + Azure SQL

T-SQL is your home base. This file isn't a tutorial — it's a bridge from the SQL Server 2000–2008 era to modern T-SQL (2012–2022+), plus the Azure SQL and Synapse additions. Covers what changed, the power features you may have missed in the leadership decade, and where T-SQL still wins.

---

## DIALECT SNAPSHOT

| Attribute | Value |
|-----------|-------|
| Origin | Sybase SQL Server (1987) → Microsoft SQL Server (1989) |
| License | Commercial / Azure subscription |
| Current versions | SQL Server 2022, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse Analytics |
| ACID compliance | Full |
| Isolation model | Lock-based (default) + snapshot isolation (opt-in per-database) |
| Strengths | Windows/.NET integration, enterprise features, Azure ecosystem, BI stack (SSRS/SSAS/Power BI), temporal tables, query store, DMVs |
| Related services | Azure Synapse Analytics (distributed T-SQL, MPP), Azure SQL Edge (IoT/embedded) |

---

## LANDSCAPE

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      SQL Server / Azure SQL Surface                        │
├───────────────────────────────────────────────────────────────────────────┤
│  DEPLOYMENT TARGETS                                                        │
│  ──────────────────────────────────────────────────────────────────────── │
│  SQL Server 2022 (on-prem/VM)                                             │
│  Azure SQL Database (PaaS, DTU or vCore)                                  │
│  Azure SQL Managed Instance (PaaS, near-100% compat, VNet)                │
│  Azure SQL Hyperscale (vCore, read replicas, 100TB+)                      │
│  Azure Synapse Analytics (MPP, 60 nodes, analytics workloads)             │
├───────────────────────────────────────────────────────────────────────────┤
│  LANGUAGE FEATURES BY ERA                                                  │
│  ──────────────────────────────────────────────────────────────────────── │
│  Pre-2005 (your home base)    │ 2005–2008                                  │
│  ─────────────────────────── │ ──────────────────────────────────────────  │
│  SELECT/INSERT/UPDATE/DELETE  │ CTEs (WITH), APPLY, ROW_NUMBER()           │
│  Stored procs, cursors, UDFs  │ PIVOT/UNPIVOT, TRY/CATCH, DMVs            │
│  SET-based + cursor patterns  │ Table-valued parameters (TVPs)             │
│                               │ GEOGRAPHY / GEOMETRY types                  │
│                               │ MERGE, GROUPING SETS, DATE/TIME types       │
│  2012–2014                    │ 2016–2017                                   │
│  ─────────────────────────── │ ──────────────────────────────────────────  │
│  Full window functions        │ JSON, Row-Level Security                    │
│  THROW, sequences             │ Temporal tables (system-versioned)          │
│  IIF, CHOOSE, CONCAT          │ STRING_SPLIT, COMPRESS/DECOMPRESS           │
│  In-memory OLTP (Hekaton)     │ R/Python extensibility services            │
│                               │ STRING_AGG, CONCAT_WS, TRIM                 │
│  2019–2022                    │                                             │
│  ─────────────────────────── │                                             │
│  UTF-8 native support         │                                             │
│  APPROX_COUNT_DISTINCT        │                                             │
│  IS [NOT] DISTINCT FROM       │                                             │
│  LEAST / GREATEST             │                                             │
│  GENERATE_SERIES              │                                             │
│  DATE_BUCKET                  │                                             │
│  JSON improvements (2022)     │                                             │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## THE 25-YEAR REFRESH — What Changed

```
 2005 ──── CTEs · APPLY · ROW_NUMBER() · PIVOT/UNPIVOT · TRY/CATCH · DMVs
           XML data type · Service Broker · Snapshot isolation (RCSI)
           Table-valued functions (multi-statement + inline)

 2008 ──── MERGE · GROUPING SETS · DATE / TIME / DATETIME2 / DATETIMEOFFSET
           GEOGRAPHY / GEOMETRY types · Table-valued parameters (TVPs)
           Filtered indexes · Sparse columns · Change Data Capture

 2012 ──── Full ANSI window functions (ROWS/RANGE BETWEEN, LEAD/LAG)
           THROW · SEQUENCES · IIF() · CHOOSE()
           CONCAT() · EOMONTH() · FORMAT()
           AlwaysOn Availability Groups

 2014 ──── In-memory OLTP ("Hekaton") · Incremental statistics
           Buffer pool extension · Delayed durability

 2016 ──── JSON (JSON_VALUE, JSON_QUERY, OPENJSON, FOR JSON)
           Row-Level Security · Temporal tables (system-versioned)
           Dynamic Data Masking · Query Store · Always Encrypted
           STRING_SPLIT() · COMPRESS() / DECOMPRESS() · R Services
           Stretch Database (deprecated)

 2017 ──── STRING_AGG() · CONCAT_WS() · TRIM()
           Graph tables (NODE/EDGE, MATCH()) · Python Services
           Automatic plan correction (Query Store integration)

 2019 ──── UTF-8 collation support · APPROX_COUNT_DISTINCT()
           Accelerated Database Recovery (ADR) · Java extensibility
           Intelligent Query Processing (Adaptive Joins, Batch Mode for rowstore)

 2022 ──── IS [NOT] DISTINCT FROM · LEAST() / GREATEST()
           GENERATE_SERIES() · DATE_BUCKET() · DATETRUNC()
           JSON_ARRAY() · JSON_OBJECT() · ISJSON improvements
           Azure Synapse Link · Ledger tables (tamper-evident)
           Parameter Sensitive Plan optimization
```

---

## CROSS APPLY / OUTER APPLY

The most underused feature from 2005. Correlate a subquery or TVF against each outer row.

```sql
-- ── CROSS APPLY: inner lateral ─────────────────────────────────────────────
-- Returns only outer rows that produce at least one row from the subquery
SELECT c.name, o.order_date, o.total
FROM   customers c
CROSS APPLY (
    SELECT TOP 3 order_date, total
    FROM   orders
    WHERE  customer_id = c.id      -- correlated to outer row c
    ORDER BY order_date DESC
) AS o;
-- PostgreSQL equivalent: JOIN LATERAL ... ON TRUE

-- ── OUTER APPLY: left lateral ──────────────────────────────────────────────
-- Keeps all outer rows; NULLs if subquery returns nothing
SELECT c.name, last_order.order_date
FROM   customers c
OUTER APPLY (
    SELECT TOP 1 order_date
    FROM   orders
    WHERE  customer_id = c.id
    ORDER BY order_date DESC
) AS last_order;

-- ── APPLY with inline TVF ──────────────────────────────────────────────────
SELECT e.name, dept_stats.avg_salary, dept_stats.headcount
FROM   employees e
CROSS APPLY dbo.fn_dept_stats(e.department_id) AS dept_stats;
-- TVF is called once per employee row — not possible with a JOIN

-- ── APPLY to parse comma-separated values (pre-STRING_SPLIT) ──────────────
SELECT p.id, s.value AS tag
FROM   products p
CROSS APPLY STRING_SPLIT(p.tags, ',') AS s;
```

**Use APPLY when:** you need TOP N per group, you're calling a TVF per row, or when a correlated subquery would need to appear in SELECT multiple times.

---

## MERGE

The definitive UPSERT in T-SQL. More expressive than `INSERT ... ON CONFLICT` in PostgreSQL, but also more footguns.

```sql
-- ── FULL MERGE: insert + update + delete ───────────────────────────────────
MERGE INTO dbo.Products AS target
USING (
    SELECT product_id, name, price, updated_at
    FROM   dbo.StagingProducts
) AS source
ON target.product_id = source.product_id

WHEN MATCHED AND target.price <> source.price THEN
    UPDATE SET
        target.name       = source.name,
        target.price      = source.price,
        target.updated_at = GETDATE()

WHEN NOT MATCHED BY TARGET THEN
    INSERT (product_id, name, price, created_at)
    VALUES (source.product_id, source.name, source.price, GETDATE())

WHEN NOT MATCHED BY SOURCE THEN
    DELETE

-- OUTPUT: capture what happened (like trigger-level CDC)
OUTPUT
    $action                 AS action_taken,   -- 'INSERT', 'UPDATE', or 'DELETE'
    inserted.product_id     AS new_id,
    deleted.product_id      AS old_id,
    inserted.price          AS new_price,
    deleted.price           AS old_price
INTO @ChangeLog (action_taken, new_id, old_id, new_price, old_price);
```

**MERGE gotchas:**
- Historical race condition bug: concurrent MERGEs on same target can deadlock or duplicate-insert. Mitigate with `HOLDLOCK` hint on the target: `MERGE INTO dbo.Products WITH (HOLDLOCK)`.
- A MERGE statement requires a semicolon terminator if the previous statement didn't have one. Put `;` before `MERGE` to be safe.
- `NOT MATCHED BY SOURCE` deletes from target rows absent from source — confirm this is intentional.

---

## OUTPUT CLAUSE

Capture rows from DML without a separate query. More explicit than PostgreSQL's `RETURNING`.

```sql
-- ── INSERT with OUTPUT ─────────────────────────────────────────────────────
DECLARE @Inserted TABLE (
    id         INT,
    name       VARCHAR(100),
    created_at DATETIME2
);

INSERT INTO dbo.Products (name, price, category)
OUTPUT inserted.id, inserted.name, inserted.created_at
INTO @Inserted
SELECT name, price, category FROM dbo.StagingProducts;

SELECT * FROM @Inserted;  -- all the new IDs and timestamps

-- ── UPDATE with OUTPUT: before AND after ──────────────────────────────────
-- deleted.col = value BEFORE update; inserted.col = value AFTER update
UPDATE dbo.Orders
SET    status = 'shipped', shipped_at = GETDATE()
OUTPUT
    deleted.status  AS old_status,
    inserted.status AS new_status,
    inserted.id,
    inserted.shipped_at
WHERE  fulfillment_confirmed = 1 AND status = 'pending';

-- ── DELETE with OUTPUT ─────────────────────────────────────────────────────
DELETE FROM dbo.ExpiredSessions
OUTPUT
    deleted.session_id,
    deleted.user_id,
    deleted.expires_at
WHERE expires_at < GETDATE();
-- PostgreSQL equivalent: DELETE ... RETURNING (simpler syntax, same semantics)
```

---

## JSON SUPPORT (SQL Server 2016+)

Less capable than PostgreSQL's JSONB, but sufficient for many use cases. JSON stored as `NVARCHAR`/`VARCHAR` — no dedicated type, no native JSON indexes.

```sql
-- ── SCALAR EXTRACTION ─────────────────────────────────────────────────────
SELECT JSON_VALUE(metadata, '$.user.name')    AS username,    -- returns NVARCHAR scalar
       JSON_VALUE(metadata, '$.amount')       AS amount_str   -- always text — cast manually
FROM   events;

-- ── OBJECT/ARRAY EXTRACTION ───────────────────────────────────────────────
SELECT JSON_QUERY(metadata, '$.tags')         AS tags_json,   -- returns JSON fragment
       JSON_QUERY(metadata, '$.address')      AS address_json
FROM   events;
-- JSON_VALUE for scalars; JSON_QUERY for objects/arrays — mixing them silently returns NULL

-- ── MODIFICATION ──────────────────────────────────────────────────────────
UPDATE events
SET    metadata = JSON_MODIFY(metadata, '$.processed', CAST(1 AS BIT))
WHERE  JSON_VALUE(metadata, '$.type') = 'purchase';

-- Append to array
SET metadata = JSON_MODIFY(metadata, 'append $.tags', 'reviewed');

-- ── OPENJSON: shred JSON to relational rows ────────────────────────────────
-- Without schema (key/value/type columns)
SELECT [key], [value], [type]
FROM   OPENJSON('["alpha","beta","gamma"]');
-- 0  alpha  1 (1=string)
-- 1  beta   1
-- 2  gamma  1

-- With explicit schema (typed result set)
SELECT id, name, email, city
FROM   OPENJSON(@users_json, '$.users')
WITH (
    id    INT            '$.user_id',
    name  NVARCHAR(100)  '$.display_name',
    email NVARCHAR(200)  '$.contact.email',
    city  NVARCHAR(100)  '$.address.city'
);

-- ── FOR JSON: serialize rows to JSON ──────────────────────────────────────
-- PATH mode: explicit nesting via dot notation in column aliases
SELECT
    u.id                     AS [user.id],
    u.name                   AS [user.name],
    o.id                     AS [orders.id],
    o.total                  AS [orders.total]
FROM   users u
LEFT JOIN orders o ON u.id = o.user_id
FOR JSON PATH, ROOT('result');

-- AUTO mode: nesting inferred from JOIN structure
SELECT u.id, u.name, o.order_date, o.total
FROM   users u LEFT JOIN orders o ON u.id = o.user_id
FOR JSON AUTO;

-- SQL Server 2022: JSON_ARRAY() and JSON_OBJECT() as expressions
SELECT JSON_OBJECT('id': id, 'name': name, 'active': is_active) AS json_row
FROM   users;

SELECT JSON_ARRAY(1, 'two', TRUE, NULL) AS arr;   -- [1,"two",true,null]
```

**PostgreSQL comparison:** SQL Server JSON is stored as text (`NVARCHAR`), no binary format, no `@>` containment operator, no native GIN index. For JSON-heavy workloads at scale, PostgreSQL's JSONB wins significantly. SQL Server JSON is best for occasional shredding/serialization, not as a primary storage format.

---

## TEMPORAL TABLES (SQL:2011, SQL Server 2016+)

Automatic history tracking — the database maintains a full audit trail without trigger code.

```sql
-- ── CREATE A TEMPORAL TABLE ───────────────────────────────────────────────
CREATE TABLE dbo.Products (
    ProductID   INT              NOT NULL PRIMARY KEY,
    Name        NVARCHAR(100)    NOT NULL,
    Price       DECIMAL(10, 2)   NOT NULL,
    CategoryID  INT              NOT NULL,
    -- System-managed period columns: SQL Server maintains these
    ValidFrom   DATETIME2 (7)    GENERATED ALWAYS AS ROW START NOT NULL,
    ValidTo     DATETIME2 (7)    GENERATED ALWAYS AS ROW END   NOT NULL,
    PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH (
    SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.ProductsHistory)
);
-- ProductsHistory is auto-created and auto-maintained

-- ── TIME TRAVEL QUERIES ───────────────────────────────────────────────────
-- Current state (normal query)
SELECT * FROM dbo.Products WHERE ProductID = 42;

-- State as of a specific point in time
SELECT * FROM dbo.Products
FOR SYSTEM_TIME AS OF '2023-06-15 12:00:00.000';

-- All versions within a time range (ValidFrom, ValidTo overlap the range)
SELECT * FROM dbo.Products
FOR SYSTEM_TIME BETWEEN '2023-01-01' AND '2023-12-31'
WHERE ProductID = 42
ORDER BY ValidFrom;

-- Entire history ever
SELECT * FROM dbo.Products
FOR SYSTEM_TIME ALL
WHERE ProductID = 42
ORDER BY ValidFrom;

-- FROM/TO variant: rows whose period overlaps [start, end)
SELECT * FROM dbo.Products
FOR SYSTEM_TIME FROM '2023-06-01' TO '2023-07-01';

-- ── TURN OFF VERSIONING (for bulk loads) ──────────────────────────────────
ALTER TABLE dbo.Products SET (SYSTEM_VERSIONING = OFF);
-- ... bulk operations ...
ALTER TABLE dbo.Products SET (
    SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.ProductsHistory, DATA_CONSISTENCY_CHECK = ON)
);
```

**PostgreSQL comparison:** PostgreSQL does not have built-in temporal tables (as of PG 16). Extensions exist (`temporal_tables`) but it's not native. This is a genuine T-SQL/SQL Server advantage.

---

## TRY/CATCH AND ERROR HANDLING

Structured exception handling added in SQL Server 2005 — finally replacing the `@@ERROR` check-after-every-statement pattern.

```sql
BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO dbo.Orders (customer_id, total, status)
    VALUES (42, 199.99, 'pending');

    UPDATE dbo.Inventory
    SET    quantity -= 1
    WHERE  product_id = 7;

    IF @@ROWCOUNT = 0
        THROW 50001, 'Product 7 not found in inventory', 1;

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    -- Capture error context
    SELECT
        ERROR_NUMBER()    AS ErrorNumber,
        ERROR_SEVERITY()  AS Severity,     -- 1-10: informational; 11-16: user; 17+: resource/server
        ERROR_STATE()     AS State,
        ERROR_PROCEDURE() AS Procedure,
        ERROR_LINE()      AS Line,
        ERROR_MESSAGE()   AS Message;

    -- Re-throw (SQL Server 2012+): preserves original error number/message/line
    THROW;

    -- Old way: RAISERROR — loses original error info
    -- RAISERROR (ERROR_MESSAGE(), ERROR_SEVERITY(), ERROR_STATE());
END CATCH;

-- ── USER-DEFINED ERRORS ───────────────────────────────────────────────────
-- THROW: simpler syntax, always severity 16, re-throwable
THROW 50001, 'Custom business rule violated', 1;

-- RAISERROR: more control over severity, can log to Windows event log
RAISERROR ('Custom error: %s failed at step %d', 16, 1, @step_name, @step_num) WITH LOG;
```

---

## DYNAMIC SQL — Safe Patterns

The only safe way to build SQL strings at runtime.

```sql
-- ── BAD: SQL injection vector ─────────────────────────────────────────────
EXEC('SELECT * FROM ' + @tableName + ' WHERE status = ''' + @status + '''');
-- @tableName = '; DROP TABLE orders; --' works here

-- ── GOOD: sp_executesql with parameters ───────────────────────────────────
DECLARE @sql    NVARCHAR(MAX);
DECLARE @status NVARCHAR(20) = N'active';
DECLARE @cutoff DATETIME2    = '2024-01-01';

SET @sql = N'
    SELECT id, name, created_at
    FROM   dbo.Users
    WHERE  status  = @status_param
      AND  created_at >= @cutoff_param
';

EXEC sp_executesql
    @sql,
    N'@status_param NVARCHAR(20), @cutoff_param DATETIME2',  -- param definition
    @status_param = @status,                                   -- param binding
    @cutoff_param = @cutoff;

-- ── DYNAMIC TABLE/COLUMN NAMES: can't parameterize — use QUOTENAME ─────────
DECLARE @schema    SYSNAME = N'dbo';
DECLARE @tableName SYSNAME = N'Orders';

SET @sql = N'SELECT TOP 100 * FROM '
         + QUOTENAME(@schema) + N'.' + QUOTENAME(@tableName);
-- QUOTENAME wraps in [] and escapes embedded brackets
-- dbo.Orders → [dbo].[Orders]
-- dbo.O]rders → [dbo].[O]]rders]  (safe)

EXEC sp_executesql @sql;

-- ── DYNAMIC PIVOT ─────────────────────────────────────────────────────────
DECLARE @cols NVARCHAR(MAX);

SELECT @cols = STRING_AGG(QUOTENAME(quarter), ', ')
               WITHIN GROUP (ORDER BY quarter)
FROM (SELECT DISTINCT quarter FROM dbo.Sales) q;

SET @sql = N'
    SELECT *
    FROM (SELECT product_id, quarter, revenue FROM dbo.Sales) src
    PIVOT (SUM(revenue) FOR quarter IN (' + @cols + N')) pvt
';
EXEC sp_executesql @sql;
```

---

## WINDOW FUNCTIONS (Full Support: SQL Server 2012+)

SQL Server 2005 had only `ROW_NUMBER()`. Full ANSI window function support arrived in 2012.

```sql
SELECT
    employee_id,
    department,
    hire_date,
    salary,

    -- Ranking
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC)  AS row_num,
    RANK()       OVER (PARTITION BY department ORDER BY salary DESC)  AS rank_with_gaps,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC)  AS dense_rank,
    NTILE(4)     OVER (ORDER BY salary)                               AS salary_quartile,
    PERCENT_RANK() OVER (ORDER BY salary)                             AS pct_rank,

    -- Navigation
    LAG(salary,  1, 0) OVER (PARTITION BY department ORDER BY hire_date) AS prev_salary,
    LEAD(salary, 1, 0) OVER (PARTITION BY department ORDER BY hire_date) AS next_salary,
    FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary)   AS min_in_dept,
    LAST_VALUE(salary)  OVER (
        PARTITION BY department
        ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING        -- needed for LAST_VALUE
    ) AS max_in_dept,

    -- Running aggregates
    SUM(salary) OVER (PARTITION BY department)                           AS dept_total,
    AVG(salary) OVER (PARTITION BY department)                           AS dept_avg,
    SUM(salary) OVER (
        ORDER BY hire_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW                -- running total
    ) AS running_total,
    SUM(salary) OVER (
        ORDER BY hire_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW                        -- 3-row moving sum
    ) AS moving_3_sum

FROM dbo.Employees;

-- ROWS vs RANGE
-- ROWS BETWEEN: physical rows — deterministic
-- RANGE BETWEEN: logical values — includes ties; default for ORDER BY without ROWS/RANGE
-- Always use ROWS BETWEEN for running totals to avoid including tie rows unexpectedly
```

---

## PIVOT / UNPIVOT

```sql
-- ── STATIC PIVOT ──────────────────────────────────────────────────────────
SELECT product_id, [Q1], [Q2], [Q3], [Q4]
FROM (
    SELECT product_id, quarter, revenue
    FROM   dbo.Sales
) AS src
PIVOT (
    SUM(revenue)
    FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS pvt;

-- ── DYNAMIC PIVOT (column values not known at compile time) ────────────────
DECLARE @cols NVARCHAR(MAX);
DECLARE @sql  NVARCHAR(MAX);

SELECT @cols = STRING_AGG(QUOTENAME(quarter), ', ')
               WITHIN GROUP (ORDER BY quarter)
FROM (SELECT DISTINCT quarter FROM dbo.Sales) q;

SET @sql = N'
    SELECT product_id, ' + @cols + N'
    FROM (SELECT product_id, quarter, revenue FROM dbo.Sales) src
    PIVOT (SUM(revenue) FOR quarter IN (' + @cols + N')) pvt
';
EXEC sp_executesql @sql;

-- ── UNPIVOT: wide-to-long ─────────────────────────────────────────────────
SELECT product_id, quarter, revenue
FROM (
    SELECT product_id, [Q1], [Q2], [Q3], [Q4]
    FROM   dbo.SalesPivoted
) AS src
UNPIVOT (
    revenue FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS unpvt;

-- Alternative: CROSS APPLY VALUES (more flexible, handles NULLs better)
SELECT p.product_id, v.quarter, v.revenue
FROM   dbo.SalesPivoted p
CROSS APPLY (VALUES
    ('Q1', p.Q1),
    ('Q2', p.Q2),
    ('Q3', p.Q3),
    ('Q4', p.Q4)
) AS v(quarter, revenue)
WHERE v.revenue IS NOT NULL;
```

---

## MODERN STRING FUNCTIONS

Functions added after your ~2008 T-SQL era.

```sql
-- ── SQL Server 2017+ ──────────────────────────────────────────────────────
STRING_AGG(name, ', ')
    WITHIN GROUP (ORDER BY name)          -- GROUP_CONCAT equivalent; NULL-safe
    -- note: max output is limited by NVARCHAR(MAX) = 2GB

CONCAT_WS(', ', first_name, last_name, email)  -- concat with separator, skips NULLs
-- Old pattern: ISNULL(first,'') + ', ' + ISNULL(last,'') — fragile

TRIM('  hello  ')             -- strips leading + trailing (was LTRIM + RTRIM separately)
TRIM('.' FROM '...hello...')  -- trim specific characters

-- ── SQL Server 2016+ ──────────────────────────────────────────────────────
STRING_SPLIT('alpha,beta,gamma', ',')  -- returns single-column table with [value]
-- SQL Server 2022 adds ordinal column:
STRING_SPLIT('alpha,beta,gamma', ',', 1)  -- 3rd arg enables ordinal column [ordinal]

COMPRESS(N'large text')          -- GZIP → VARBINARY
DECOMPRESS(compressed_col)       -- VARBINARY → VARBINARY (cast to VARCHAR after)
CAST(DECOMPRESS(col) AS NVARCHAR(MAX))

-- ── SQL Server 2022+ ──────────────────────────────────────────────────────
GREATEST(a, b, c)               -- max of N values (was IIF or CASE)
LEAST(a, b, c)                  -- min of N values

DATETRUNC(month, GETDATE())     -- truncate to month start (was DATEADD trickery)
DATE_BUCKET(WEEK, 2, order_date) -- floor to N-week bucket

GENERATE_SERIES(1, 10)          -- returns rows 1..10 (was recursive CTE)
GENERATE_SERIES(0.0, 1.0, 0.1)  -- decimal steps

-- IS [NOT] DISTINCT FROM (SQL:1999, finally in 2022)
-- NULL-safe equality: NULL IS NOT DISTINCT FROM NULL → TRUE
-- Replaces: (a = b OR (a IS NULL AND b IS NULL))
WHERE col1 IS NOT DISTINCT FROM col2;
```

---

## QUERY HINTS — Use Sparingly

```sql
-- ── TABLE HINTS ───────────────────────────────────────────────────────────
FROM orders WITH (NOLOCK)       -- dirty read (READ UNCOMMITTED); avoid for correctness
FROM orders WITH (UPDLOCK)      -- shared → update lock; prevents update deadlocks
FROM orders WITH (HOLDLOCK)     -- shared lock held to end of transaction (= SERIALIZABLE)
FROM orders WITH (ROWLOCK)      -- prefer row granularity over page/table locks
FROM orders WITH (PAGLOCK)      -- prefer page locks
FROM orders WITH (TABLOCK)      -- table lock for bulk insert scenarios
FROM orders WITH (INDEX(ix_customer_date))  -- force specific index

-- ── QUERY HINTS (OPTION clause, end of statement) ─────────────────────────
OPTION (RECOMPILE)                     -- generate new plan each execution; bypasses param sniffing
OPTION (MAXDOP 1)                      -- force single-threaded (for OLTP in high-CPU contention)
OPTION (MAXDOP 0)                      -- use all available CPUs
OPTION (OPTIMIZE FOR (@id = 42))       -- plan optimized for this specific value
OPTION (OPTIMIZE FOR (@id UNKNOWN))    -- plan using average density, not sniffed value
OPTION (FORCE ORDER)                   -- join in FROM order; overrides optimizer
OPTION (USE HINT ('ENABLE_PARALLEL_PLAN_PREFERENCE'))
OPTION (USE HINT ('DISABLE_OPTIMIZED_NESTED_LOOP'))
OPTION (HASH JOIN)                     -- force hash join for all joins in query
OPTION (LOOP JOIN)
OPTION (MERGE JOIN)

-- ── JOIN HINTS (inline) ───────────────────────────────────────────────────
FROM a INNER HASH  JOIN b ON a.id = b.id
FROM a INNER LOOP  JOIN b ON a.id = b.id
FROM a INNER MERGE JOIN b ON a.id = b.id

-- NOLOCK WARNING: WITH(NOLOCK) = READ UNCOMMITTED
-- Returns uncommitted data. Can return the same row twice or skip rows during page splits.
-- Safe only for coarse approximations (e.g., COUNT(*) on a reporting table where ±1% is acceptable).
-- NEVER use for financial, inventory, or correctness-sensitive queries.
```

---

## QUERY STORE (SQL Server 2016+)

Built-in query performance history. Replaces the "plan disappeared and I don't know what it was" problem.

```sql
-- ── ENABLE ────────────────────────────────────────────────────────────────
ALTER DATABASE [YourDB] SET QUERY_STORE = ON (
    OPERATION_MODE          = READ_WRITE,
    CLEANUP_POLICY          = (STALE_QUERY_THRESHOLD_DAYS = 30),
    DATA_FLUSH_INTERVAL_SECONDS = 900,
    MAX_STORAGE_SIZE_MB     = 1024,
    QUERY_CAPTURE_MODE      = AUTO    -- AUTO skips trivial queries; ALL captures everything
);

-- ── FIND TOP CPU CONSUMERS ────────────────────────────────────────────────
SELECT TOP 20
    qt.query_sql_text,
    qrs.avg_cpu_time        / 1000.0   AS avg_cpu_ms,
    qrs.avg_duration        / 1000.0   AS avg_duration_ms,
    qrs.avg_logical_io_reads           AS avg_logical_reads,
    qrs.count_executions,
    q.query_id,
    p.plan_id
FROM sys.query_store_query_text  qt
JOIN sys.query_store_query       q   ON qt.query_text_id = q.query_text_id
JOIN sys.query_store_plan        p   ON q.query_id       = p.query_id
JOIN sys.query_store_runtime_stats qrs ON p.plan_id      = qrs.plan_id
ORDER BY qrs.avg_cpu_time DESC;

-- ── QUERIES WITH MULTIPLE PLANS (plan instability) ────────────────────────
SELECT q.query_id, COUNT(DISTINCT p.plan_id) AS plan_count,
       qt.query_sql_text
FROM sys.query_store_query q
JOIN sys.query_store_plan p ON q.query_id = p.query_id
JOIN sys.query_store_query_text qt ON q.query_text_id = qt.query_text_id
GROUP BY q.query_id, qt.query_sql_text
HAVING COUNT(DISTINCT p.plan_id) > 1
ORDER BY plan_count DESC;

-- ── FORCE A PLAN (regression fix without code change) ─────────────────────
EXEC sys.sp_query_store_force_plan @query_id = 42, @plan_id = 7;
-- Plan forced immediately; survives service restarts

-- ── UNFORCE A PLAN ────────────────────────────────────────────────────────
EXEC sys.sp_query_store_unforce_plan @query_id = 42, @plan_id = 7;
```

---

## DYNAMIC MANAGEMENT VIEWS (DMVs)

Your operational visibility into a running SQL Server instance.

```sql
-- ── WHAT'S RUNNING RIGHT NOW ──────────────────────────────────────────────
SELECT
    r.session_id,
    r.status,
    r.blocking_session_id,
    r.wait_type,
    r.wait_time / 1000.0    AS wait_sec,
    r.cpu_time / 1000.0     AS cpu_sec,
    r.logical_reads,
    t.text                  AS sql_text,
    qp.query_plan
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle)   AS t
CROSS APPLY sys.dm_exec_query_plan(r.plan_handle) AS qp
WHERE r.session_id <> @@SPID;

-- ── BLOCKING CHAIN ────────────────────────────────────────────────────────
SELECT
    blocking_session_id, session_id, wait_type, wait_time / 1000.0 AS wait_sec,
    (SELECT text FROM sys.dm_exec_sql_text(sql_handle)) AS blocked_sql
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0;

-- ── INDEX USAGE STATS (since last restart) ────────────────────────────────
SELECT
    OBJECT_NAME(i.object_id)   AS table_name,
    i.name                     AS index_name,
    ius.user_seeks,
    ius.user_scans,
    ius.user_lookups,
    ius.user_updates,
    ius.last_user_seek
FROM sys.dm_db_index_usage_stats ius
JOIN sys.indexes i
     ON i.object_id = ius.object_id
     AND i.index_id = ius.index_id
WHERE ius.database_id = DB_ID()
ORDER BY ius.user_seeks + ius.user_scans DESC;

-- ── MISSING INDEX SUGGESTIONS ─────────────────────────────────────────────
SELECT TOP 20
    mid.statement                           AS table_name,
    mid.equality_columns,
    mid.inequality_columns,
    mid.included_columns,
    migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks + migs.user_scans)
        AS improvement_measure,
    migs.user_seeks,
    migs.user_scans
FROM sys.dm_db_missing_index_details     mid
JOIN sys.dm_db_missing_index_groups      mig  ON mid.index_handle = mig.index_handle
JOIN sys.dm_db_missing_index_group_stats migs ON mig.index_group_handle = migs.group_handle
WHERE mid.database_id = DB_ID()
ORDER BY improvement_measure DESC;

-- ── WAIT STATISTICS: what is SQL Server waiting on ────────────────────────
SELECT
    wait_type,
    waiting_tasks_count,
    wait_time_ms / 1000.0       AS wait_sec,
    max_wait_time_ms / 1000.0   AS max_wait_sec,
    (wait_time_ms - signal_wait_time_ms) / 1000.0 AS resource_wait_sec
FROM sys.dm_os_wait_stats
WHERE wait_type NOT IN (
    'SLEEP_TASK','SLEEP_SYSTEMTASK','SQLTRACE_BUFFER_FLUSH','WAITFOR',
    'LAZYWRITER_SLEEP','SLEEP_TEMPDBSTARTUP','SNI_HTTP_ACCEPT',
    'DISPATCHER_QUEUE_SEMAPHORE','XE_DISPATCHER_WAIT','XE_TIMER_EVENT',
    'HADR_WORK_QUEUE','ONDEMAND_TASK_QUEUE','REQUEST_FOR_DEADLOCK_SEARCH',
    'RESOURCE_QUEUE','SERVER_IDLE_CHECK','SLEEP_DBSTARTUP'
)
ORDER BY wait_time_ms DESC;
-- High CXPACKET → parallelism waits (check MAXDOP)
-- High LCK_M_* → locking/blocking
-- High PAGEIOLATCH_* → disk I/O, buffer cache pressure
-- High ASYNC_NETWORK_IO → client not consuming results fast enough
```

---

## ROW-LEVEL SECURITY (SQL Server 2016+)

Transparent predicate-based filtering — the application doesn't change, the database filters.

```sql
-- ── FILTER PREDICATE (read filtering) ────────────────────────────────────
CREATE SCHEMA Security;
GO

-- Inline TVF that returns 1 (allow) or 0 (deny)
CREATE FUNCTION Security.fn_OrdersAccessPredicate(@user_id INT)
RETURNS TABLE
WITH SCHEMABINDING
AS RETURN
    SELECT 1 AS access_result
    WHERE @user_id = CONVERT(INT, SESSION_CONTEXT(N'CurrentUserID'))
       OR IS_MEMBER('db_owner') = 1;    -- admins bypass
GO

-- Attach as filter predicate on the table
CREATE SECURITY POLICY Security.OrdersPolicy
    ADD FILTER PREDICATE Security.fn_OrdersAccessPredicate(user_id)
        ON dbo.Orders,
    ADD BLOCK PREDICATE Security.fn_OrdersAccessPredicate(user_id)
        ON dbo.Orders AFTER INSERT,    -- prevent inserting rows for other users
    ADD BLOCK PREDICATE Security.fn_OrdersAccessPredicate(user_id)
        ON dbo.Orders AFTER UPDATE
WITH (STATE = ON);

-- Application sets context at the start of each request
EXEC sys.sp_set_session_context N'CurrentUserID', 42, @read_only = 1;
SELECT * FROM dbo.Orders;   -- automatically filtered to user 42; user can't see other rows
```

---

## AZURE SQL SPECIFICS

### Deployment Tiers

| Tier | What it is | Key difference |
|------|-----------|---------------|
| Azure SQL Database | Fully managed PaaS | No SA access, no SQL Agent (Basic/Standard), auto-backup |
| Azure SQL Managed Instance | Managed PaaS + VNet injection | Near-100% SQL Server compat; SQL Agent, linked servers, CLR |
| Azure SQL Hyperscale | vCore tier of Azure SQL DB | Read scale-out replicas; near-instant backup/restore up to 100TB |
| Azure SQL Serverless | Compute tier of Azure SQL DB | Auto-pause + auto-resume; bill per vCore-second; cold start ~1s |
| Elastic Pools | Shared resource pool | Multiple databases share DTUs/vCores; cost optimization |

### Azure SQL-Only Features

```sql
-- ── LEDGER TABLES (SQL Server 2022 + Azure SQL) ───────────────────────────
-- Append-only with cryptographic verification — tamper-evident audit trail
CREATE TABLE dbo.AccountBalances (
    AccountID  INT          NOT NULL,
    Balance    DECIMAL(15,2) NOT NULL,
    UpdatedBy  NVARCHAR(100)
)
WITH (LEDGER = ON);
-- Each INSERT/UPDATE/DELETE gets a hash; chain of hashes is verifiable
-- Useful for financial, compliance, and audit scenarios

-- ── ELASTIC QUERY: query across databases ─────────────────────────────────
-- Define external data source (another Azure SQL DB)
CREATE EXTERNAL DATA SOURCE RemoteDB WITH (
    TYPE = RDBMS,
    LOCATION = 'myserver.database.windows.net',
    DATABASE_NAME = 'OtherDB',
    CREDENTIAL = cred_remote
);

CREATE EXTERNAL TABLE dbo.RemoteCustomers (
    id   INT, name NVARCHAR(100)
) WITH (DATA_SOURCE = RemoteDB);

SELECT * FROM dbo.RemoteCustomers;  -- transparent cross-database query

-- ── ACTIVE GEO-REPLICATION ────────────────────────────────────────────────
-- Readable secondary in different region (not HADR — this is async replication)
-- Failover groups add automatic failover with DNS alias endpoint
```

---

## AZURE SYNAPSE ANALYTICS — Distributed T-SQL

Synapse Dedicated SQL Pool = massively parallel processing (MPP). Same T-SQL dialect, different execution model across 60 compute nodes.

```sql
-- ── TABLE DISTRIBUTION (how rows are sharded across 60 nodes) ────────────
CREATE TABLE dbo.FactSales (
    SaleID     BIGINT        NOT NULL,
    CustomerID INT           NOT NULL,
    ProductID  INT           NOT NULL,
    SaleDate   DATE          NOT NULL,
    Amount     DECIMAL(15,2) NOT NULL
)
WITH (
    DISTRIBUTION = HASH(CustomerID),    -- rows with same CustomerID on same node
    -- DISTRIBUTION = ROUND_ROBIN,       -- even spread; no join optimization
    -- DISTRIBUTION = REPLICATE,         -- full copy on all nodes; for small dims only
    CLUSTERED COLUMNSTORE INDEX         -- default for Synapse analytics workloads
);

-- HASH distribution: pick the column used in most JOINs
-- REPLICATE: only for small dimension tables (< ~2GB after compression)
-- ROUND_ROBIN: when no JOIN column exists; staging tables

-- ── CTAS: CREATE TABLE AS SELECT ─────────────────────────────────────────
-- Parallelized — most efficient way to transform large data in Synapse
CREATE TABLE dbo.CustomerSummary
WITH (
    DISTRIBUTION = HASH(CustomerID),
    CLUSTERED COLUMNSTORE INDEX
)
AS
SELECT
    CustomerID,
    COUNT(*)        AS order_count,
    SUM(Amount)     AS lifetime_value,
    MAX(SaleDate)   AS last_order_date
FROM dbo.FactSales
GROUP BY CustomerID;

-- ── STATISTICS (CRITICAL — Synapse doesn't auto-create) ───────────────────
CREATE STATISTICS stat_CustomerID ON dbo.FactSales (CustomerID);
CREATE STATISTICS stat_SaleDate   ON dbo.FactSales (SaleDate);
-- Without stats, query optimizer makes poor join/distribution decisions

-- ── EXTERNAL TABLES (PolyBase — query files in ADLS directly) ─────────────
CREATE EXTERNAL FILE FORMAT parquet_fmt
WITH (FORMAT_TYPE = PARQUET);

CREATE EXTERNAL DATA SOURCE adls_source
WITH (
    LOCATION = 'abfss://container@storageaccount.dfs.core.windows.net',
    CREDENTIAL = adls_credential
);

CREATE EXTERNAL TABLE dbo.ExtRawSales (
    SaleDate   DATE,
    CustomerID INT,
    Amount     DECIMAL(15,2)
)
WITH (
    LOCATION     = '/data/raw/sales/',
    DATA_SOURCE  = adls_source,
    FILE_FORMAT  = parquet_fmt
);

-- Load into Synapse from external table
CREATE TABLE dbo.FactSales WITH (DISTRIBUTION = HASH(CustomerID), CLUSTERED COLUMNSTORE INDEX)
AS SELECT * FROM dbo.ExtRawSales;
-- Synapse Serverless (on-demand): can query ExtRawSales directly without loading
```

---

## DECISION CHEAT SHEET

| Scenario | T-SQL Pattern |
|----------|-------------|
| UPSERT — guaranteed atomic | `MERGE ... WITH (HOLDLOCK)` or `INSERT ... ON CONFLICT` (Azure SQL 2022+) |
| Audit trail / row history | Temporal tables — zero application code change |
| ETL: stage → target with change tracking | `MERGE` with `OUTPUT` to log `$action` |
| Correlated top-N per group | `CROSS APPLY (SELECT TOP n ... WHERE correlated) ` |
| Parameterized dynamic SQL | `sp_executesql` — always; never `EXEC(string)` |
| Dynamic identifiers (table/column names) | `QUOTENAME()` + `sp_executesql` |
| Performance regression | Query Store: find old plan, `sp_query_store_force_plan` |
| What's blocking right now | `sys.dm_exec_requests` + `blocking_session_id` |
| Index recommendations | `sys.dm_db_missing_index_details` |
| Per-user row filtering | Row-Level Security + `SESSION_CONTEXT` |
| Cross-database analytics on Azure | Synapse Serverless pool + External Tables over ADLS |
| Large analytics transforms | Synapse Dedicated pool + CTAS |
| Full JSON document storage | Consider PostgreSQL; T-SQL JSON is text-based, no native indexes |
| Tamper-evident audit log | Ledger tables (SQL Server 2022 / Azure SQL) |

---

## COMMON CONFUSION POINTS

**`NOLOCK` is not safe for correctness.** It is `READ UNCOMMITTED` — you can see uncommitted rolled-back data, miss rows that moved during a page split, or see the same row twice. It avoids blocking at the cost of correctness. Only acceptable for very rough approximations (e.g., gauge cardinality of a large table). Production financial, inventory, or any correctness-sensitive query must not use it.

**`MERGE` and concurrent inserts.** MERGE does not atomically serialize against concurrent inserts by default. Under high concurrency, two sessions can both pass the "NOT MATCHED" check and both try to insert, causing a duplicate key violation. Fix: `MERGE INTO target WITH (HOLDLOCK)`.

**`OUTPUT` with `MERGE`.** `$action` returns `'INSERT'`, `'UPDATE'`, or `'DELETE'` as a string. `inserted.*` has the new row state; `deleted.*` has the old row state. Both are populated for UPDATE; only `inserted.*` for INSERT; only `deleted.*` for DELETE.

**CTE recursion and `MAXRECURSION`.** Recursive CTEs default to 100 iterations. Increase: `OPTION (MAXRECURSION 1000)`. Disable limit: `OPTION (MAXRECURSION 0)` — use with care.

**`APPLY` vs `JOIN`.** A `JOIN` cannot produce a different number of columns per outer row based on that row's data. `APPLY` can — the subquery is re-evaluated per outer row and can be correlated. Also, `APPLY` is the only way to call a TVF per row.

**`VARCHAR` vs `NVARCHAR`.** `VARCHAR` stores 1 byte per character (collation-dependent). `NVARCHAR` stores 2 bytes per character (UTF-16). Any column holding user-entered text, names, or international data must be `NVARCHAR`. Mixing `VARCHAR` and `NVARCHAR` in joins causes implicit conversion and index scan instead of seek.

**`sp_executesql` N-prefix.** The `@params` definition string and all string literals in it must be `NVARCHAR`. Always use the `N'...'` prefix. `EXEC sp_executesql @sql, '@p VARCHAR(20)', ...` will silently work in some cases but cause character conversion issues with extended characters.

**`IDENTITY` vs `SEQUENCE`.** `IDENTITY` is per-table — can't share across tables, can't pre-allocate or step backwards. `CREATE SEQUENCE` (SQL Server 2012+) is independent and shareable: `NEXT VALUE FOR dbo.MySeq`. Sequences can be used for distributing IDs across partitioned tables.

**Azure SQL vs SQL Server feature gaps.** Azure SQL Database lacks: linked servers, `xp_cmdshell`, SQL Agent (on Basic/Standard tiers), CLR, `BACKUP/RESTORE` (use automated backups instead). Azure SQL Managed Instance supports all of these and is the migration target for SQL Server on-prem apps that need them.

**Query Store and plan forcing survive failovers.** Forced plans in Query Store are persisted in the database and survive service restarts, failovers, and even restores (if you restore the database with Query Store data intact). This is the preferred regression mitigation over hints in code.
