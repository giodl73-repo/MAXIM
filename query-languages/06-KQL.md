# KQL — Kusto Query Language

KQL is Microsoft's pipe-based query language for log analytics and telemetry at scale. It powers Azure Monitor, Log Analytics, Application Insights, Azure Data Explorer (ADX), and Microsoft Sentinel. This guide focuses on what matters for practitioners who already write KQL daily: ADX-specific features (materialized views, update policies, partitioning, cross-cluster federation), the behavioral differences between LA and ADX that affect query design, the optimizer's rewrite rules and when pipe order matters vs when it doesn't, and the advanced operators that distinguish expert KQL from intermediate KQL.

---

## 1. BIG PICTURE — KQL in the Azure Ecosystem

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       KQL-Powered Azure Services                           │
├───────────────────┬───────────────────┬────────────────┬───────────────────┤
│  Azure Monitor    │  Application      │   Microsoft    │   Azure Data      │
│  Log Analytics    │  Insights         │   Sentinel     │   Explorer (ADX)  │
│                   │                   │                │                   │
│  • AzureActivity  │  • requests       │  • Security-   │  • Custom tables  │
│  • AzureDiag-     │  • dependencies   │    Event       │  • IoT telemetry  │
│    nostics        │  • exceptions     │  • SignIn-      │  • Clickstream    │
│  • Heartbeat      │  • traces         │    Logs        │  • Time series    │
│  • SecurityEvent  │  • customEvents   │  • Defender    │  • Parquet import │
│  • Perf           │  • availResults   │    alerts      │                   │
│  • ContainerLog   │  • pageViews      │                │                   │
│  • KubeEvents     │  • browser-       │                │                   │
│                   │    Timings        │                │                   │
└───────────────────┴───────────────────┴────────────────┴───────────────────┘

All use the same KQL syntax. Differences:
Per-context behavioral differences — same KQL syntax, different capabilities:

  Feature                      | Log Analytics | App Insights | Sentinel | ADX
  -----------------------------|---------------|--------------|----------|-----
  Query timeout                | 10 min        | 10 min       | 30 min   | configurable (default 10 min, up to 1h)
  Cross-scope functions        | workspace()   | app()        | workspace() + app() | cluster() + database()
  cluster() function           | No            | No           | No       | Yes (ADX-only)
  External tables              | No            | No           | No       | Yes
  Streaming ingestion          | No            | No           | No       | Yes (<10s latency)
  Materialized views           | No            | No           | No       | Yes
  Update policies              | No            | No           | No       | Yes
  Partitioning policies        | No            | No           | No       | Yes
  Stored functions             | Yes (portal)  | Yes (portal) | Yes      | Yes (.create function)
  externaldata() operator      | No            | No           | Yes      | Yes
  datatable() operator         | Yes           | Yes          | Yes (heavy use in detections) | Yes
  Row-level security           | No            | No           | No       | Yes
  Ingestion time (latency)     | ~1-5 min      | ~1-5 min     | ~5 min   | batch ~5 min, streaming <10s

┌──────────────────────────────────────────────────────────────┐
│  Query Entry Points                                          │
│                                                              │
│  Azure Portal → Log Analytics workspace → Logs blade        │
│  Azure Portal → App Insights resource  → Logs / Metrics     │
│  Azure Portal → Sentinel               → Hunting / Analytics│
│  ADX Web UI   → cluster.region.kusto.windows.net            │
│  Grafana       → Azure Monitor data source (KQL queries)    │
│  VS Code       → Kusto extension                            │
│  SDK/API       → kusto-ingest / Azure.Data.Kusto (C#/Python)│
└──────────────────────────────────────────────────────────────┘
```

---

## 2. QUERY OPTIMIZER — When Pipe Order Matters (and When It Doesn't)

The pipe model looks sequential, but the ADX query optimizer rewrites pipe chains. Knowing what the optimizer will and won't reorder tells you where to spend effort structuring queries.

**What the optimizer rewrites automatically:**

```
// Predicate pushdown past summarize — optimizer pushes this filter before aggregation
T | summarize count() by Region | where Region == "eastus"
// Rewritten as: T | where Region == "eastus" | summarize count() by Region

// Filter hoisting past join — a filter on the left table is pushed before the join
T | join kind=inner (U) on key | where T.timestamp > ago(1h)
// Optimizer pushes T.timestamp > ago(1h) to before the join

// Materialized view serving — if a matching materialized view exists,
// a query against the source table is automatically routed to the MV delta + precomputed result
T | summarize count() by bin(timestamp, 1h)
// If a materialized view covers this pattern, the optimizer serves from the MV
```

**Where pipe order DOES matter (optimizer cannot reorder):**

```kusto
// Time filter must be first on timestamp — uses the datetime index
// The optimizer will NOT hoist a time filter past operators that transform timestamp
T
| extend ts2 = timestamp + 1h       // transforms timestamp
| where ts2 > ago(1d)               // CANNOT be pushed past extend — late filter
// Correct pattern: filter on original timestamp first
T
| where timestamp > ago(1d)         // early time filter uses partition index
| extend ts2 = timestamp + 1h

// summarize discards non-aggregated columns — a where after summarize
// filters on aggregated results, not raw rows. Expensive if the aggregation is large.
// Pattern: push all possible filters before summarize.

// parse_json() is expensive — do not call it before a where filter
T
| extend parsed = parse_json(RawData)       // parses ALL rows
| where parsed.level == "error"             // then filters
// Better:
T
| where RawData contains "error"            // cheap string check first
| extend parsed = parse_json(RawData)       // parse only candidates
| where parsed.level == "error"             // precise filter on parsed result

// mv-expand multiplies rows — always filter before mv-expand, not after
T | mv-expand items | where items.type == "critical"   // expensive: expands then filters
T | where RawItems has "critical" | mv-expand items | where items.type == "critical"  // better
```

**Forcing optimizer behavior with hints:**

```kusto
// hint.strategy=broadcast — force right table to be broadcast to all nodes
// Use when right side is small and join is hitting distribution overhead
T | join hint.strategy=broadcast kind=inner (U | where active == true) on key

// hint.shufflekey — force hash-based distributed join on specific key
// Use for large-to-large joins where the default strategy causes data skew
T | join hint.shufflekey=TenantId kind=inner (U) on TenantId

// hint.materialized=true — explicit materialization of an expression
let expensive = materialize(T | where condition | summarize ...);
// materialize() evaluates once and caches; without it, a let referencing T twice
// scans T twice

// summarize hint.shufflekey — distribute summarize across nodes on a key
// Critical for high-cardinality group-by on large tables
T | summarize hint.shufflekey=TenantId count() by TenantId, bin(timestamp, 1h)
```

Full SQL → KQL operator mapping in section 16.

---

## 3. DATA TYPES

| KQL Type   | SQL Equivalent              | Notes                                                   |
|------------|-----------------------------|---------------------------------------------------------|
| `string`   | NVARCHAR                    | UTF-8, always Unicode                                   |
| `int`      | INT (32-bit)                | 32-bit signed                                           |
| `long`     | BIGINT (64-bit)             | Default for integer literals                            |
| `real`     | FLOAT                       | 64-bit IEEE 754                                         |
| `decimal`  | DECIMAL                     | High-precision, slower than real                        |
| `bool`     | BIT                         | `true` / `false` (lowercase)                            |
| `datetime` | DATETIME2 (UTC)             | Always UTC, ISO 8601                                    |
| `timespan` | No direct equivalent        | Duration: `1d`, `2h`, `30m`, `45s`, `100ms`             |
| `guid`     | UNIQUEIDENTIFIER            | GUID/UUID                                               |
| `dynamic`  | JSON / NVARCHAR + JSON path | JSON-like bag — arrays and objects. Very powerful.      |

Type conversion functions: `toint()`, `tolong()`, `toreal()`, `tostring()`, `tobool()`, `todatetime()`, `totimespan()`, `toguid()`, `todynamic()` / `parse_json()`

---

## 4. CORE OPERATORS — Reference Card

### where (= SQL WHERE)

```kusto
Requests
| where timestamp > ago(24h)                              // time filter — always first, uses index
| where ResultCode == 200
| where Name startswith "GET /api"
| where Name contains "user"                              // case-insensitive substring
| where Name matches regex @"^GET /api/v\d+"
| where isnotempty(ClientIP)                              // NOT NULL + NOT ''
| where ClientIP in ("10.0.0.1", "10.0.0.2")             // IN list
| where not (Name startswith "HEAD")                     // NOT predicate
| where ResultCode between (400 .. 499)                  // inclusive range
```

### project (= SQL SELECT with column list)

```kusto
Requests
| project timestamp, Name, ResultCode, Duration          // keep only these columns

| project-away Password, SensitiveField                  // keep all EXCEPT these

| project-rename                                          // rename without dropping others
    ResponseTime = Duration,
    StatusCode   = ResultCode

| project                                                 // rename + select in one
    ts       = timestamp,
    endpoint = Name,
    status   = ResultCode
```

### extend (= SQL computed columns, but ADDS — does not replace)

```kusto
Requests
| extend
    IsError      = ResultCode >= 400,
    DurationSec  = Duration / 1000.0,
    Hour         = bin(timestamp, 1h),
    UrlPath      = tostring(parse_url(Url)["Path"]),
    Bucket       = case(
                       Duration < 100,  "fast",
                       Duration < 1000, "normal",
                                        "slow")
```

`project` replaces column set. `extend` adds to existing set. After `extend`, all original columns are still present.

### summarize (= SQL GROUP BY + aggregates)

```kusto
Requests
| where timestamp > ago(7d)
| summarize
    RequestCount = count(),
    ErrorCount   = countif(ResultCode >= 400),
    AvgDuration  = avg(Duration),
    P95Duration  = percentile(Duration, 95),
    P99Duration  = percentile(Duration, 99),
    UniqueUsers  = dcount(UserId),                       // HyperLogLog approximate distinct count
    MaxDuration  = max(Duration),
    MinDuration  = min(Duration),
    TotalBytes   = sum(ResponseSize)
  by bin(timestamp, 1h), Name                           // GROUP BY
| order by timestamp asc
```

**Aggregate functions:**

| Function              | Description                                      |
|-----------------------|--------------------------------------------------|
| `count()`             | Row count                                        |
| `countif(pred)`       | Conditional count                                |
| `sum(col)`            | Sum                                              |
| `avg(col)`            | Average                                          |
| `min(col)` / `max()`  | Min / max                                        |
| `percentile(col, p)`  | Single percentile                                |
| `percentiles(col, ...)` | Multiple percentiles in one pass               |
| `dcount(col)`         | Approximate distinct count (fast, HyperLogLog)   |
| `dcountif(col, pred)` | Conditional approximate distinct count           |
| `stdev(col)`          | Standard deviation                               |
| `variance(col)`       | Variance                                         |
| `any(col)`            | Any value from group (arbitrary, not random)     |
| `make_list(col)`      | Aggregate column values into dynamic array       |
| `make_set(col)`       | Aggregate distinct values into dynamic array     |
| `arg_max(col, *)`     | Row where col is max (returns whole row)         |
| `arg_min(col, *)`     | Row where col is min                             |

After `summarize`, auto-named aggregate is `count_` (not `count`). Reference it as `count_` in downstream `where`.

### order by / sort by (= SQL ORDER BY)

```kusto
| order by timestamp desc               // most recent first
| sort by Duration desc                 // sort is alias for order by
| order by Name asc, Duration desc      // multi-column sort
```

### take / limit / top (= SQL TOP / LIMIT)

```kusto
| take 100                              // first 100 rows (non-deterministic without order by)
| limit 100                             // alias for take
| top 10 by Duration desc              // ORDER BY + LIMIT in one operator
| top-nested 3 of Name by count() ...  // hierarchical top-N
```

### distinct (= SQL SELECT DISTINCT)

```kusto
| distinct ClientIP, Country
Requests | distinct Name | count         // count unique endpoint names
```

### count

```kusto
Requests | count
Requests | where ResultCode >= 500 | count
```

---

## 5. TIME FUNCTIONS — KQL's Strength

```kusto
// Time literals and arithmetic
ago(1d)                                  // 1 day ago from now()
ago(2h)                                  // 2 hours ago
ago(30m)                                 // 30 minutes ago
now()                                    // current UTC datetime
now() - 1h                               // datetime arithmetic — 1 hour ago
datetime(2024-01-15 00:00:00)            // literal datetime (UTC)
datetime(2024-01-15T00:00:00Z)           // ISO 8601 format

// Timespan literals
1d                                       // 1 day
2h                                       // 2 hours
30m                                      // 30 minutes
2h30m                                    // 2 hours 30 minutes
1.5h                                     // 1.5 hours
1ms                                      // 1 millisecond

// bin(): truncate to nearest bucket — the GROUP BY time key
bin(timestamp, 1h)                       // truncate to hour
bin(timestamp, 5m)                       // truncate to 5-minute bucket
bin(timestamp, 1d)                       // truncate to day
bin(timestamp, 15m)                      // every 15 minutes

// Date/time extraction
hourofday(timestamp)                     // 0–23
dayofweek(timestamp)                     // 0=Sunday, 6=Saturday (timespan, not int)
toint(dayofweek(timestamp))             // 0–6 as int
dayofmonth(timestamp)                    // 1–31
dayofyear(timestamp)                     // 1–366
monthofyear(timestamp)                   // 1–12
getyear(timestamp)                       // year as int
startofday(timestamp)                    // floor to start of day
startofweek(timestamp)                   // floor to start of week
startofmonth(timestamp)                  // floor to start of month
endofday(timestamp)                      // end of day (23:59:59.999...)

// Time range patterns
| where timestamp between (datetime(2024-01-01) .. datetime(2024-02-01))
| where timestamp > ago(7d) and timestamp < ago(1d)
| where timestamp >= startofday(ago(1d)) and timestamp < startofday(now())

// Duration arithmetic — SQL DATEDIFF equivalent
| extend AgeDays = (now() - CreatedAt) / 1d
| extend AgeHours = (now() - CreatedAt) / 1h
| where (EndTime - StartTime) > 5m       // filter on computed duration
```

---

## 6. STRING OPERATORS

```kusto
// Case-insensitive by default (unlike SQL)
| where Name contains "error"            // substring match, case-insensitive
| where Name !contains "health"          // not contains
| where Name startswith "GET"            // prefix
| where Name endswith ".json"            // suffix
| where Name has "api"                   // whole-word match (faster — uses inverted index)
| where Name has_all ("api", "user")     // all words present
| where Name has_any ("error", "fail", "exception")   // any word present

// Case-sensitive variants (_cs suffix)
| where Name contains_cs "Error"         // case-sensitive contains
| where Name startswith_cs "GET"         // case-sensitive prefix
| where Name has_cs "API"                // case-sensitive word match

// Regex
| where Message matches regex @"Exception.*NullReference"
| where Message !matches regex @"^health"

// String functions
| extend Domain   = split(Email, "@")[1]               // split → dynamic array
| extend Parts    = split(Path, "/")                   // array of path segments
| extend Host     = tostring(split(Url, "/")[2])
| extend Upper    = toupper(Name)
| extend Lower    = tolower(Name)
| extend Trimmed  = trim(" \t", Message)               // trim chars from both ends
| extend Short    = substring(Name, 0, 50)             // SQL LEFT(Name, 50)
| extend Len      = strlen(Message)
| extend Replaced = replace_string(Message, "old", "new")
| extend Replaced = replace_regex(Message, @"\d+", "N")
| extend Found    = indexof(Message, "error")          // -1 if not found
| extend Concat   = strcat(FirstName, " ", LastName)   // SQL + or CONCAT()
| extend Padded   = strcat_array(array_sort_asc(Tags), ", ")  // join array to string
```

`has` vs `contains`: `has` matches whole words and uses the inverted index (fast). `contains` matches any substring but cannot use the index efficiently (full scan on the column). Prefer `has` when matching on word boundaries.

---

## 7. DYNAMIC TYPE — JSON-like Bags

```kusto
// dynamic is KQL's JSON bag — nested arrays and objects
// App Insights customDimensions and customMeasurements are dynamic

// Parse JSON string into dynamic
| extend d = parse_json(JsonColumn)
| extend d = todynamic(JsonColumn)                    // alias

// Access fields
| extend Username  = d.user.name                      // dot notation
| extend Tags      = d["tags"]                        // bracket notation
| extend FirstTag  = d.tags[0]                        // array index (0-based)
| extend Nested    = d.metadata.region                // nested path

// Always tostring() / toint() / todouble() when extracting from dynamic
| extend UserId    = tostring(customDimensions.userId)
| extend PageLoad  = todouble(customMeasurements.loadTime)
| extend Count     = toint(d.count)

// Dynamic array operations
| extend TagCount  = array_length(d.tags)
| where d.tags has "critical"                         // has works on dynamic arrays
| extend Sorted    = array_sort_asc(d.tags)

// mv-expand: explode array to multiple rows (= SQL UNNEST / LATERAL JOIN)
| mv-expand Tags = d.tags                             // one row per tag
| mv-expand with_itemindex=idx Tags = d.tags          // with index

// Build dynamic value
| extend Meta   = bag_pack("host", Computer, "level", toint(Level))
| extend Keys   = bag_keys(CustomDimensions)          // get all keys
| extend Values = bag_values(CustomDimensions)        // get all values

// Check for key existence
| where isnotnull(customDimensions.userId)

// App Insights pattern
customEvents
| where timestamp > ago(24h)
| extend UserId      = tostring(customDimensions.userId)
| extend PageLoad    = todouble(customMeasurements.loadTime)
| extend Environment = tostring(customDimensions.environment)
| where Environment == "production"
| summarize AvgLoad = avg(PageLoad) by bin(timestamp, 5m)
| render timechart
```

---

## 8. LET STATEMENTS (= SQL CTEs + Variables)

```kusto
// let: bind a name to a scalar value, tabular expression, or inline function
// let statements must be followed by the body query, separated by semicolons

// Scalar variable
let lookback      = 7d;
let threshold     = 0.05;       // 5% error rate threshold
let slow_ms       = 2000;       // 2 second SLO

// Tabular expression (= SQL CTE)
let error_requests =
    Requests
    | where ResultCode >= 400
    | where timestamp > ago(lookback);

// Inline function
let parse_url_path = (url: string) {
    tostring(parse_url(url)["Path"])
};

let classify_duration = (ms: real) {
    case(ms < 100,  "fast",
         ms < 1000, "normal",
                    "slow")
};

// Compose them
let lookback  = 7d;
let slow_ms   = 2000;

let slow_requests =
    Requests
    | where timestamp > ago(lookback)
    | where Duration > slow_ms
    | extend UrlPath = tostring(parse_url(Url)["Path"]);

slow_requests
| summarize SlowCount = count() by bin(timestamp, 1h), UrlPath
| order by timestamp asc
| render timechart
```

`let` is scoped to the query — not persisted. For persistent named functions, use ADX stored functions or Log Analytics functions (Save as function in portal).

---

## 9. JOIN

```kusto
// KQL join kinds:
//   inner      matched rows from both sides (deduplicates right side on join key)
//   leftouter  all left rows + matched right   (= SQL LEFT JOIN)
//   rightouter all right + matched left
//   fullouter  all rows from both sides
//   leftanti   left rows with NO match in right  (= SQL WHERE right.id IS NULL)
//   rightanti  right rows with no match in left
//   leftsemi   left rows that HAVE a match in right (= SQL WHERE EXISTS)
//   rightsemi  right rows that have a match in left

// Standard inner join: correlate requests with exceptions
Requests
| where timestamp > ago(1d)
| join kind=inner (
    Exceptions
    | where timestamp > ago(1d)
    | project operation_Id, ExceptionType = type, ExceptionMsg = outerMessage
  ) on operation_Id
| project timestamp, Name, ResultCode, ExceptionType, ExceptionMsg

// Left outer join — find requests without exceptions
Requests
| where timestamp > ago(1h)
| join kind=leftouter (
    Exceptions
    | where timestamp > ago(1h)
    | project operation_Id, ExceptionType = type
  ) on operation_Id
| where isempty(ExceptionType)            // requests with no associated exception

// leftanti — find requests with no corresponding dependency call
Requests
| where timestamp > ago(1h)
| join kind=leftanti (
    Dependencies
    | where timestamp > ago(1h)
    | distinct operation_Id
  ) on operation_Id

// IMPORTANT: KQL join deduplicates the right table on the join key.
// This is different from SQL — the right table acts like it has been DISTINCT'd.
// For SQL-style many-to-many join: use hint.strategy=broadcast or materialize().

// Materialize pattern (cache right side for large right tables):
let right_side = materialize(
    Dependencies
    | where timestamp > ago(1d)
    | project operation_Id, DepName = name
);
Requests
| where timestamp > ago(1d)
| join kind=inner right_side on operation_Id
```

---

## 10. UNION

```kusto
// Union multiple tables (= SQL UNION ALL — duplicates preserved)
union Table1, Table2, Table3
| where timestamp > ago(1d)

// Union with wildcard (all tables matching pattern)
union App*                               // all tables starting with "App"

// Union with source column
union withsource=TableName Requests, Exceptions, Traces
| summarize count() by TableName

// Cross-workspace query
union
    workspace("workspace-A").Requests,
    workspace("workspace-B").Requests
| where timestamp > ago(1h)

// Cross-resource query (App Insights)
union
    app("appinsights-prod").requests,
    app("appinsights-staging").requests
| extend env = iif(app("appinsights-prod").requests, "prod", "staging")
```

---

## 11. MAKE-SERIES — Time Series Analysis

```kusto
// make-series: produces array of metric values aligned on a time grid.
// Unlike summarize (one row per bucket), make-series produces one row per
// group with arrays — enabling time-series ML functions.

Requests
| where timestamp > ago(7d)
| make-series RequestCount = count() default=0
    on timestamp                         // time axis
    from ago(7d) to now()               // range
    step 1h                              // bucket size
    by Name                              // group by
// Result: each row = Name + array[168] of hourly counts

// Apply time series analytics
| extend (anomalies, score, baseline) = series_decompose_anomalies(RequestCount)
| mv-expand
    timestamp   to typeof(datetime),
    RequestCount to typeof(long),
    anomalies    to typeof(int),
    score        to typeof(real),
    baseline     to typeof(real)
| where anomalies != 0                  // only anomalous points
| project timestamp, Name, RequestCount, baseline, score

// Forecast next 24 hours
| extend forecast = series_decompose_forecast(RequestCount, 24)

// Moving average smoothing
| extend smoothed = series_fir(RequestCount, repeat(1, 5))  // 5-point moving average

// Correlation between two series
| extend corr = series_pearson_correlation(Series1, Series2)
```

### Advanced Operators — partition, bag_unpack, evaluate

```kusto
// ── partition: run a sub-query independently per partition value ──────────────
// Critical for per-tenant or per-host analysis: avoids cross-partition aggregation
// Each partition runs as an independent query; results are unioned

T
| partition by TenantId
(
    top 5 by Duration desc
)
// Returns top 5 slowest operations per tenant, independently ranked
// Without partition: | top 5 by Duration desc gives the global top 5

// Partition with summarize — each partition summarized independently
Requests
| where timestamp > ago(1d)
| partition hint.strategy=native by AppName
(
    summarize P99 = percentile(Duration, 99), Total = count()
    | extend App = AppName
)

// hint.strategy options:
//   native    — ADX-native partitioned sub-query (preferred for ADX; not in LA)
//   legacy    — older shuffle-based strategy
//   shuffle   — explicit shuffle join semantics


// ── bag_unpack: promote dynamic bag keys to first-class columns ───────────────
// customDimensions in App Insights is dynamic — key set varies per event type
// bag_unpack pivots it out, one column per key

customEvents
| where timestamp > ago(1h)
| evaluate bag_unpack(customDimensions)
// Each key in customDimensions becomes a column in the result
// Sparse keys get null in rows that don't have them

// Combine with project-away to drop the original dynamic column after unpacking
customEvents
| evaluate bag_unpack(customDimensions, outputColumnPrefix="dim_")
| project-away customDimensions


// ── evaluate: plugin framework — ADX-specific analytical plugins ──────────────
// evaluate calls plugins that go beyond what pure KQL can express

// basket: find frequent itemsets (association rule mining)
T
| evaluate basket()
// Returns rows showing which column value combinations appear frequently together
// Useful for finding correlated failure patterns

// autocluster: find common patterns in a dataset — like automatic WHERE clause suggestions
Exceptions
| where timestamp > ago(1d)
| evaluate autocluster()
// Returns: which attribute combinations explain clusters of exceptions

// diffpatterns: find what's different between two subsets
Requests
| where timestamp > ago(1d)
| evaluate diffpatterns(
    where ResultCode >= 500,    // "interesting" set: failed requests
    where ResultCode < 500      // "baseline" set: successful requests
  )
// Returns: which column value combinations appear disproportionately in failures

// narrow: unpivot wide table to (row, col, value) triples — exploratory analysis
T | evaluate narrow()

// python / r plugins (ADX only, requires enabled sandbox)
T
| evaluate python(typeof(result: double),
    'result = df["Value"].rolling(7).mean()',
    pack('Value', Value)
  )
```

### Persisted Functions — ADX Stored Functions and Log Analytics Saved Functions

`let` bindings are query-scoped and disappear when the query ends. For reusable, shareable logic, both ADX and Log Analytics support persisted functions.

```kusto
// ── ADX stored functions ──────────────────────────────────────────────────────
// Stored at cluster/database level — callable like a table or UDF

// Create
.create function
    with (docstring = "P99 latency per operation over a lookback window",
          folder = "SLO")
    OperationP99(lookback: timespan = 1d) {
    Requests
    | where timestamp > ago(lookback)
    | summarize P99 = percentile(Duration, 99) by Name
    | order by P99 desc
}

// Alter (update body while keeping name)
.alter function OperationP99(lookback: timespan = 1d) {
    Requests
    | where timestamp > ago(lookback)
    | summarize P99 = percentile(Duration, 99), P50 = percentile(Duration, 50) by Name
    | order by P99 desc
}

// Call — exactly like a table reference
OperationP99()
OperationP99(7d)

// Show all functions in current database
.show functions

// Drop
.drop function OperationP99


// ── Log Analytics / Sentinel saved functions ──────────────────────────────────
// Saved via: portal → Log Analytics workspace → Logs → Save as function
// Callable in queries as a table reference (no parameter support in portal-saved functions)

// In a query:
workspace("my-workspace").MyFunctionName
// or within the same workspace:
MyFunctionName

// Programmatic creation via REST API (Log Analytics supports parameterized functions via API):
// PUT /workspaces/{workspaceId}/savedSearches/{id}
// body: { "category": "Functions", "displayName": "...", "query": "...", "functionAlias": "MyFunc" }
```

Key distinction: ADX stored functions support typed parameters with defaults and are first-class database objects with full DDL. LA saved functions are closer to named queries — lightweight, portal-managed, and not directly parameterizable from the portal UI (only via API).

---

## 12. ADX MATERIALIZED VIEWS

Materialized views precompute aggregations over a source table and keep the result current as new data is ingested. Queries against the source that match the view pattern are automatically routed to the view.

```kusto
// ── Create ────────────────────────────────────────────────────────────────────
.create materialized-view with (backfill=true) RequestsByHour on table Requests
{
    Requests
    | summarize RequestCount = count(), AvgDuration = avg(Duration)
      by bin(timestamp, 1h), Name
}
// backfill=true: processes existing data in the source table (runs as background job)
// Without backfill: view starts from the time of creation (delta only)

// ── Syntax constraints ────────────────────────────────────────────────────────
// - Source table must NOT be partitioned (ADX limitation)
// - The view query must start directly from the source table — no joins or union
// - Supported aggregations: count, sum, avg, min, max, dcount, make_set, make_list, arg_max, arg_min
// - The view query must have a summarize as the final operator

// ── Query behavior ────────────────────────────────────────────────────────────
// Queries against the source table that match the MV pattern are served from the MV:
Requests
| summarize count() by bin(timestamp, 1h), Name
// ADX optimizer: detects match with RequestsByHour MV, serves from precomputed result + delta

// Explicit MV query using materialized_view() function:
materialized_view("RequestsByHour")
| where timestamp > ago(7d)
| order by RequestCount desc

// Lookback pattern: combines precomputed MV data with recent delta not yet materialized
let MVCutoff = materialized_view("RequestsByHour") | summarize max(timestamp);
union
    materialized_view("RequestsByHour"),
    (
        Requests
        | where timestamp > toscalar(MVCutoff)   // only the delta since last materialization
        | summarize RequestCount = count(), AvgDuration = avg(Duration)
          by bin(timestamp, 1h), Name
    )
| summarize RequestCount = sum(RequestCount), AvgDuration = avg(AvgDuration)
  by timestamp, Name

// ── Management ────────────────────────────────────────────────────────────────
.show materialized-views                          // list all MVs in database
.show materialized-view RequestsByHour details    // freshness, lag, row count, materialized rows
.alter materialized-view RequestsByHour autoUpdateSchema=true
.disable materialized-view RequestsByHour
.enable  materialized-view RequestsByHour
.drop    materialized-view RequestsByHour
```

**Monitoring freshness:**
```kusto
.show materialized-view RequestsByHour details
// Returns: MaterializedTo (last fully materialized timestamp), IsHealthy, RowCount
// MaterializedTo lagging behind now() by more than a few minutes means the background
// materialization process is falling behind ingest rate — scale the cluster or simplify the view
```

---

## 13. ADX PARTITIONING POLICIES

Partitioning policies control how ADX physically organizes extents (data shards) on disk. Applied asynchronously by background processes, not at ingest time.

```kusto
// ── Hash partitioning: for high-cardinality string columns ────────────────────
// Dramatically improves filter performance on the partition key:
// TenantId, DeviceId, UserId, AccountId — columns you always filter by
// ADX collocates rows with the same hash value into the same extents
// Queries with equality or IN filters on the partition key skip most extents entirely

.alter table Telemetry policy partitioning
```
```json
{
  "PartitionKeys": [
    {
      "ColumnName": "TenantId",
      "Kind": "Hash",
      "Properties": {
        "Function": "XxHash64",
        "MaxPartitionCount": 256,
        "Seed": 1
      }
    }
  ]
}
```
```kusto
// MaxPartitionCount: number of hash buckets — higher = better distribution for large tenants
// Rule of thumb: 128–512 for large tables, start at 128

// ── Uniform range partitioning: for datetime sharding ────────────────────────
// Ensures rows in a time range land in the same extents
// Used with timestamp columns when you always query by time range
.alter table Telemetry policy partitioning
```
```json
{
  "PartitionKeys": [
    {
      "ColumnName": "timestamp",
      "Kind": "UniformRange",
      "Properties": {
        "Reference": "1970-01-01T00:00:00",
        "RangeSize": "1.00:00:00",
        "OverrideCreationTime": false
      }
    }
  ]
}
```
```kusto
// RangeSize: partition granularity — "1.00:00:00" = 1 day per partition
// Combine hash + uniform range for TenantId + time:
// partition key = (TenantId hash) — time index already handled by extent datetime range

// ── Operational implications ──────────────────────────────────────────────────
// Partitioning is NOT applied at ingest time — background process reshuffles extents
// Time to see effect: hours to days depending on data volume and cluster load
// Monitor progress:
.show table Telemetry extents
| summarize count() by ShardId = tostring(ExtentId)
// Or via the ADX Diagnostics blade in Azure Portal

// Combined hash + range (two partition keys):
// Supported: one hash key + one uniform range key per table
// Most common: TenantId (hash) + timestamp (range)

// Show current partitioning policy:
.show table Telemetry policy partitioning

// Delete policy:
.delete table Telemetry policy partitioning
```

---

## 14. CROSS-CLUSTER AND CROSS-DATABASE QUERIES

Cross-cluster KQL is the ADX equivalent of SQL Server linked servers and `OPENQUERY` — but the syntax is explicit and first-class rather than a configuration layer.

```kusto
// ── Cross-database (same cluster) ────────────────────────────────────────────
// Access a table in a different database on the same cluster
database("OtherDatabase").TableName
database("OtherDatabase").TableName | where timestamp > ago(1h)

// Function call in another database
database("SharedUtils").MyFunction(arg)

// ── Cross-cluster ─────────────────────────────────────────────────────────────
// cluster() is ADX-only — not available in Log Analytics
cluster("clustername").database("DatabaseName").TableName
cluster("clustername.region.kusto.windows.net").database("DatabaseName").TableName

// Full example: query a prod cluster from a dev cluster
cluster("mycluster-prod.eastus.kusto.windows.net").database("Telemetry").Requests
| where timestamp > ago(1h)
| summarize count() by Name

// ── Federation — union across clusters ───────────────────────────────────────
union
    cluster("mycluster-prod.eastus.kusto.windows.net").database("Telemetry").Requests,
    cluster("mycluster-eu.westeurope.kusto.windows.net").database("Telemetry").Requests
| where timestamp > ago(1h)
| summarize count() by bin(timestamp, 5m), Name
| render timechart

// Wildcard union across databases on the same cluster:
union database("*").Requests
| where timestamp > ago(1h)

// ── Cross-workspace in Log Analytics (not ADX cluster()) ─────────────────────
union
    workspace("workspace-prod").Requests,
    workspace("workspace-staging").Requests

// app() for App Insights within the same LA workspace scope:
union
    app("myapp-prod").requests,
    app("myapp-staging").requests

// ── Performance implications ──────────────────────────────────────────────────
// Cross-cluster joins are expensive: data must travel across cluster boundaries
// Rule: push ALL filters before the cross-cluster reference — reduce rows in transit

// BAD: join first, then filter
cluster("prod").database("Telemetry").Requests
| join kind=inner (
    cluster("other").database("Dim").Users
  ) on UserId
| where timestamp > ago(1h)     // filter arrives after cross-cluster join — too late

// GOOD: filter at source before join
cluster("prod").database("Telemetry").Requests
| where timestamp > ago(1h)     // push filter to source side
| join kind=inner (
    cluster("other").database("Dim").Users
    | where IsActive == true    // filter right side too
  ) on UserId

// For large cross-cluster joins: use hint.strategy=broadcast if right side is small
cluster("prod").database("Telemetry").Requests
| where timestamp > ago(1h)
| join hint.strategy=broadcast kind=inner (
    cluster("other").database("Dim").Users | where IsActive == true
  ) on UserId
// hint.strategy=broadcast: right side is replicated to all prod cluster nodes
// avoids sending prod data across the wire — only the small dimension travels
```

**vs SQL Server linked servers:** SQL Server linked servers hide the remote address in server configuration; the KQL syntax makes the cluster address explicit in the query. Cross-cluster KQL respects AAD RBAC — the identity running the query must have read access on the remote cluster. No equivalent of SQL Server's linked server service account delegation.

---

## 15. ADX UPDATE POLICIES

Update policies implement ingest-time transformation: when data lands in a source (raw) table, a query runs automatically and writes results to a target (processed) table. Both the ingest and the update run in the same transaction — either both commit or both fail.

```kusto
// ── Pattern: raw table → processed table via update policy ───────────────────

// Step 1: Create the raw (landing) table
.create table RawEvents (RawData: string, IngestTime: datetime)

// Step 2: Create the target (processed) table
.create table ParsedEvents
(
    Timestamp:   datetime,
    EventType:   string,
    TenantId:    string,
    UserId:      string,
    Properties:  dynamic
)

// Step 3: Define the transformation function
.create function ParseRawEvents() {
    RawEvents
    | extend parsed = parse_json(RawData)
    | project
        Timestamp  = todatetime(parsed.timestamp),
        EventType  = tostring(parsed.eventType),
        TenantId   = tostring(parsed.tenantId),
        UserId     = tostring(parsed.userId),
        Properties = parsed.properties
}

// Step 4: Attach the update policy to the target table
.alter table ParsedEvents policy update
```
```json
[
  {
    "IsEnabled": true,
    "Source": "RawEvents",
    "Query": "ParseRawEvents()",
    "IsTransactional": true,
    "PropagateIngestionProperties": false
  }
]
```
```kusto
// IsTransactional: true — both raw ingest and parsed write commit together
// PropagateIngestionProperties: forward ingest tags/extent tags to target table

// ── Fan-out pattern: one raw event → multiple target tables ──────────────────
// Attach multiple update policies to different targets, each reading from RawEvents
// Common: one policy per event type, routing to type-specific tables

.alter table MetricEvents policy update
```
```json
[{ "IsEnabled": true, "Source": "RawEvents", "Query": "FilterMetrics()", "IsTransactional": true }]
```
```kusto
.alter table AuditEvents policy update
```
```json
[{ "IsEnabled": true, "Source": "RawEvents", "Query": "FilterAudit()", "IsTransactional": true }]
```
```kusto

// ── Show / manage ─────────────────────────────────────────────────────────────
.show table ParsedEvents policy update
.alter table ParsedEvents policy update @'[]'   // remove all policies (disable)

// ── Performance gotcha ────────────────────────────────────────────────────────
// The update policy query runs SYNCHRONOUSLY in the ingestion path
// If your transformation function is expensive (regex parse, complex extend, lookup join),
// it will slow down every ingest batch — throughput drops proportionally
// Rules:
//   - Keep update policy queries simple: parse_json + project is fine
//   - Avoid joins in update policies — they block ingestion
//   - If you need a lookup, pre-materialize the dimension as a static table
//   - Monitor: .show commands | where CommandType == "TableUpdatePolicies"
//     and watch ingestion latency in the ADX diagnostics blade

// ── Transaction semantics ─────────────────────────────────────────────────────
// IsTransactional=true: if the update policy query fails, the source ingest also rolls back
// This ensures raw and processed tables stay in sync — no orphaned raw records
// IsTransactional=false: source ingest succeeds even if transformation fails
//   — useful if you want raw data to always land and fix processing failures separately
```

---

## 16. RENDER — Visualization

```kusto
// render: display as chart in Azure Portal, ADX UI, Grafana
// Has no effect in code/SDK queries — purely a UI hint

| render timechart                       // time-based line chart (timestamp on X axis)
| render barchart                        // horizontal bar chart
| render columnchart                     // vertical bar chart
| render piechart                        // pie chart
| render scatterchart                    // scatter plot
| render areachart                       // filled area chart
| render ladderchart                     // timeline/Gantt for event ranges
| render pivotchart                      // pivot table
| render table                           // tabular (default)

// Options
| render timechart with (
    title  = "Request Rate by Endpoint",
    xtitle = "Time",
    ytitle = "Requests/min",
    legend = visible
  )

// Multi-series timechart: one line per distinct value of the by column
Requests
| where timestamp > ago(24h)
| summarize count() by bin(timestamp, 5m), Name
| render timechart                       // one line per endpoint
```

---

## 17. COMMON APP INSIGHTS PATTERNS

```kusto
// ── Request failure rate over time ─────────────────────────────────────────
requests
| where timestamp > ago(24h)
| summarize
    Total    = count(),
    Failed   = countif(success == false),
    FailRate = round(100.0 * countif(success == false) / count(), 2)
  by bin(timestamp, 5m)
| render timechart

// ── P50 / P95 / P99 latency ────────────────────────────────────────────────
requests
| where timestamp > ago(1h)
| summarize percentiles(duration, 50, 95, 99) by bin(timestamp, 5m)
| render timechart

// ── Top slowest operations ─────────────────────────────────────────────────
requests
| where timestamp > ago(1h)
| top 20 by duration desc
| project timestamp, name, duration, resultCode, url

// ── Exception count by type ────────────────────────────────────────────────
exceptions
| where timestamp > ago(24h)
| summarize Count = count() by type, outerMessage
| order by Count desc
| take 20

// ── Dependency failures (downstream service calls) ─────────────────────────
dependencies
| where timestamp > ago(1h)
| where success == false
| summarize Count = count() by name, type, target
| order by Count desc

// ── User journey — trace end-to-end operation ──────────────────────────────
let operation_id = "abc123def456";
union requests, dependencies, exceptions, traces
| where operation_Id == operation_id
| order by timestamp asc
| project timestamp, itemType, name, duration, success, message

// ── Availability by operation ──────────────────────────────────────────────
requests
| where timestamp > ago(7d)
| summarize
    Total    = count(),
    OK       = countif(resultCode < 400),
    Avail    = round(100.0 * countif(resultCode < 400) / count(), 3)
  by name
| where Total > 100                      // ignore low-traffic endpoints
| order by Avail asc                     // worst first

// ── Custom event funnel ────────────────────────────────────────────────────
customEvents
| where timestamp > ago(7d)
| where name in ("signup_start", "signup_email", "signup_complete")
| extend UserId = tostring(customDimensions.userId)
| summarize Steps = make_set(name) by UserId
| extend
    Started   = array_index_of(Steps, "signup_start")   >= 0,
    Emailed   = array_index_of(Steps, "signup_email")   >= 0,
    Completed = array_index_of(Steps, "signup_complete") >= 0
| summarize
    StartCount    = countif(Started),
    EmailCount    = countif(Emailed),
    CompleteCount = countif(Completed)
```

---

## 18. COMMON AZURE MONITOR LOG ANALYTICS PATTERNS

```kusto
// ── VM CPU spike detection ─────────────────────────────────────────────────
Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| where TimeGenerated > ago(1h)
| summarize AvgCPU = avg(CounterValue), MaxCPU = max(CounterValue)
    by bin(TimeGenerated, 5m), Computer
| where MaxCPU > 90
| render timechart

// ── Failed login brute-force detection ────────────────────────────────────
SecurityEvent
| where EventID == 4625                  // Windows failed logon
| where TimeGenerated > ago(24h)
| summarize FailCount = count() by Account, IpAddress, Computer
| where FailCount > 10
| order by FailCount desc

// ── Kubernetes pod crash loop detection ───────────────────────────────────
KubeEvents
| where TimeGenerated > ago(1h)
| where Reason == "BackOff"
| summarize RestartCount = count() by Name, Namespace, bin(TimeGenerated, 5m)
| where RestartCount > 3

// ── AKS container log errors ──────────────────────────────────────────────
ContainerLog
| where TimeGenerated > ago(1h)
| where LogEntry contains_cs "ERROR" or LogEntry contains_cs "FATAL"
| project TimeGenerated, ContainerID, LogEntry
| order by TimeGenerated desc

// ── Azure resource health summary ─────────────────────────────────────────
AzureActivity
| where TimeGenerated > ago(24h)
| where ActivityStatusValue == "Failure"
| summarize FailCount = count() by ResourceGroup, OperationNameValue
| order by FailCount desc

// ── Cross-workspace query ──────────────────────────────────────────────────
union
    workspace("prod-logs").Perf,
    workspace("staging-logs").Perf
| where TimeGenerated > ago(1h)
| where CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m), Computer
| render timechart
```

---

## 19. SENTINEL HUNTING PATTERNS

```kusto
// ── Impossible travel detection ────────────────────────────────────────────
SigninLogs
| where TimeGenerated > ago(1d)
| where ResultType == 0                  // successful signins
| project TimeGenerated, UserPrincipalName, Location, IPAddress
| order by UserPrincipalName asc, TimeGenerated asc
| serialize                              // required before next/prev functions
| extend PrevLocation = prev(Location, 1)
| extend PrevTime     = prev(TimeGenerated, 1)
| extend PrevUser     = prev(UserPrincipalName, 1)
| where UserPrincipalName == PrevUser    // same user
| where Location != PrevLocation        // different location
| where (TimeGenerated - PrevTime) < 1h // within 1 hour

// ── Rare process execution ─────────────────────────────────────────────────
SecurityEvent
| where EventID == 4688                  // process creation
| where TimeGenerated > ago(7d)
| summarize ExecutionCount = count() by Process, Computer
| where ExecutionCount < 5               // rare executions
| join kind=inner (
    SecurityEvent
    | where EventID == 4688
    | where TimeGenerated > ago(1h)      // recent execution
    | distinct Process, Computer
  ) on Process, Computer

// ── TI feed enrichment ─────────────────────────────────────────────────────
let malicious_ips = externaldata(IP: string) [@"https://example.com/threat-feed.csv"]
    with (format="csv", ignoreFirstRecord=true);
SigninLogs
| where TimeGenerated > ago(1h)
| where IPAddress in (malicious_ips)
| project TimeGenerated, UserPrincipalName, IPAddress, Location
```

---

## 20. SQL → KQL TRANSLATION TABLE

| SQL                                      | KQL                                          |
|------------------------------------------|----------------------------------------------|
| `SELECT col1, col2 FROM T`              | `T \| project col1, col2`                   |
| `SELECT * FROM T`                        | `T` (or `T \| take 1000` to limit)          |
| `SELECT col, expr AS alias FROM T`       | `T \| extend alias = expr \| project col, alias` |
| `WHERE condition`                        | `\| where condition`                         |
| `AND` / `OR` / `NOT`                    | `and` / `or` / `not` (lowercase)            |
| `LIKE '%text%'`                          | `contains "text"`                            |
| `LIKE 'text%'`                           | `startswith "text"`                          |
| `IS NULL`                                | `isnull(col)`                                |
| `IS NOT NULL`                            | `isnotnull(col)` or `isnotempty(col)`        |
| `NOT (col IN (...))`                    | `col !in (...)`                              |
| `GROUP BY col, SUM(val)`                | `\| summarize sum(val) by col`               |
| `COUNT(*)`                               | `count()`                                    |
| `COUNT(DISTINCT col)`                    | `dcount(col)` (approximate)                  |
| `HAVING count > 5`                       | `\| where count_ > 5` (after summarize)     |
| `ORDER BY col DESC`                      | `\| order by col desc`                       |
| `TOP 10`                                 | `\| take 10` (or `\| top 10 by col`)        |
| `INNER JOIN ... ON`                      | `\| join kind=inner (...) on key`            |
| `LEFT JOIN ... ON`                       | `\| join kind=leftouter (...) on key`        |
| `WHERE NOT EXISTS (...)`                | `\| join kind=leftanti (...) on key`         |
| `UNION ALL`                              | `union T1, T2`                               |
| `WITH cte AS (...)`                      | `let cte = ...;`                             |
| `CAST(x AS INT)`                         | `toint(x)`                                   |
| `CAST(x AS VARCHAR)`                     | `tostring(x)`                                |
| `CAST(x AS FLOAT)`                       | `toreal(x)` or `todouble(x)`                |
| `GETDATE()` / `NOW()`                    | `now()`                                      |
| `DATEPART(hour, ts)`                     | `hourofday(ts)`                              |
| `DATEPART(day, ts)`                      | `dayofmonth(ts)`                             |
| `DATEDIFF(day, d1, d2)`                 | `(d2 - d1) / 1d`                            |
| `GETDATE() - INTERVAL '1 day'`          | `ago(1d)`                                    |
| `FLOOR(val / bucket) * bucket`          | `bin(val, bucket)`                           |
| `CASE WHEN ... THEN ... END`            | `case(pred1, val1, pred2, val2, default)`    |
| `COALESCE(a, b)`                         | `coalesce(a, b)`                             |
| `NULLIF(a, b)`                           | `iff(a == b, null, a)`                       |
| `IIF(pred, a, b)` (T-SQL)               | `iff(pred, a, b)` or `iif(pred, a, b)`      |
| `STRING_AGG(col, ',')`                  | `make_list(col)` then `strcat_array(...)`    |
| `SUBSTRING(s, 1, 5)` (1-indexed)        | `substring(s, 0, 5)` (0-indexed)            |
| `LEN(s)`                                 | `strlen(s)`                                  |
| `UPPER(s)` / `LOWER(s)`                 | `toupper(s)` / `tolower(s)`                  |
| `TRIM(s)`                                | `trim(" ", s)`                               |
| `CHARINDEX(find, s)`                     | `indexof(s, find)` (-1 if not found)        |
| `REPLACE(s, old, new)`                  | `replace_string(s, old, new)`               |
| `ROW_NUMBER() OVER (ORDER BY ...)`      | `row_number()` after `serialize`            |
| `LAG(col, 1) OVER (...)`                | `prev(col, 1)` after `serialize`            |
| `LEAD(col, 1) OVER (...)`               | `next(col, 1)` after `serialize`            |

---

## 21. DECISION CHEAT SHEET

| Scenario                                          | Use KQL?  | Notes                                                 |
|---------------------------------------------------|-----------|-------------------------------------------------------|
| App Insights telemetry analysis                   | Yes       | Native — requests, exceptions, dependencies, traces   |
| Azure Monitor log analysis                        | Yes       | Native — Perf, SecurityEvent, AzureActivity, etc.    |
| Sentinel security hunting                         | Yes       | Detection rules, hunting queries, playbooks           |
| Grafana dashboards on Azure logs                  | Yes       | Azure Monitor data source uses KQL                    |
| ADX time-series analytics at scale                | Yes       | ADX is purpose-built for this                         |
| Transactional OLTP queries                        | No        | Use T-SQL / PostgreSQL                                |
| Relational data with FK constraints               | No        | KQL has no FK model                                   |
| Sub-millisecond latency from application code     | No        | KQL queries have cold-start overhead                  |
| Data needing ACID guarantees                      | No        | Use a transactional store                             |
| SQL Server or Azure SQL analytics                 | No        | Use T-SQL, Query Store, DMVs                          |
| Anything outside Azure/ADX ecosystem              | No        | KQL engines are Microsoft-specific                    |

---

## 22. COMMON CONFUSION POINTS

**KQL vs SQL execution order**
SQL clauses are declarative — the optimizer picks execution order. KQL is sequential — the written pipe order is the execution order. Always put `where` on `timestamp` first; it uses the time index and dramatically reduces scanned data. Putting a `where` after a `summarize` is expensive because you are filtering aggregated results, not raw rows.

**project vs extend**
`project` replaces the entire column set — only the listed columns survive. `extend` adds computed columns while keeping all existing ones. A common mistake: using `extend` when you wanted to drop columns, then passing a wide row through expensive downstream operators.

**summarize auto-naming**
`count()` inside `summarize` produces a column named `count_`, not `count`. `sum(Duration)` produces `sum_Duration`. Either accept the auto-name or alias it: `summarize RequestCount = count()`. Referencing the auto-name in a downstream `where` without the underscore causes a silent "column not found" or unexpected behavior.

**Case sensitivity**
String comparisons (`has`, `contains`, `startswith`, `==`) are case-insensitive by default in KQL. This is the opposite of SQL Server with a case-sensitive collation. Use the `_cs` suffix for case-sensitive: `contains_cs`, `has_cs`, `startswith_cs`. The `==` operator is case-insensitive for strings.

**has vs contains**
`has "word"` matches whole words and uses the inverted full-text index — fast on large tables. `contains "sub"` matches any substring but requires a column scan. Use `has` whenever your search term is a complete word or token.

**join deduplication**
KQL `join kind=inner` silently deduplicates the right table on the join key before joining. If the right side has multiple rows per key, only one is used. This is not SQL behavior. For a many-to-many join without dedup, use `join hint.strategy=broadcast` or `materialize()` the right side and use `join hint.remote=left`.

**bin() not floor()**
To group timestamps into buckets, use `bin(timestamp, 1h)`. Do not try to compute this manually with `datetime` arithmetic — `bin` handles DST edge cases and ensures consistent bucket alignment.

**0-indexed strings and arrays**
`substring(s, 0, 5)` returns the first 5 characters. T-SQL `SUBSTRING(s, 1, 5)` is 1-indexed. KQL arrays are 0-indexed: `d.tags[0]` is the first element.

**serialize required for row functions**
`prev()`, `next()`, `row_number()`, `row_cumsum()` require `| serialize` before them to guarantee row ordering. Without `serialize`, the results are undefined.

**render is UI-only**
`| render timechart` only works in the Azure Portal log query editor, ADX Web UI, or Grafana. In SDK calls, it is silently ignored. Do not rely on `render` in programmatic queries.

**Log Analytics vs ADX — architectural and operational differences**

Same KQL syntax, fundamentally different operational models. The decision of where to land data is an architecture decision, not a query syntax decision.

```
┌─────────────────────────────────────┬─────────────────────────────────────────┐
│  Log Analytics (Azure Monitor)      │  Azure Data Explorer (ADX)              │
├─────────────────────────────────────┼─────────────────────────────────────────┤
│  Managed, serverless                │  Dedicated cluster — you size it        │
│  No cluster management              │  SKU, node count, auto-scale            │
│                                     │                                         │
│  INGESTION                          │  INGESTION                              │
│  DCR-based (Data Collection Rules)  │  Multiple paths:                        │
│  Batch ~1–5 min latency             │    Batch ingestion: ~5 min latency      │
│  No streaming ingestion             │    Streaming: <10 sec latency           │
│                                     │    Event Hub, IoT Hub, ADF, SDK         │
│  RETENTION                          │  RETENTION                              │
│  Interactive: 30 days (default)     │  Hot cache: configurable (days)         │
│  Total: up to 2 years               │  Cold cache: Azure Blob (low cost)      │
│  Commitment tiers (pay-per-GB or    │  Table-level retention policies         │
│  capacity reservation)              │  Per-table hot/cold boundary            │
│                                     │                                         │
│  QUERY SCOPE                        │  QUERY SCOPE                            │
│  workspace() for cross-workspace    │  cluster() + database() federation      │
│  app() for App Insights             │  Cross-cluster joins                    │
│  No cluster() function              │  External tables (ADLS, blob, SQL)      │
│                                     │                                         │
│  ADVANCED FEATURES                  │  ADVANCED FEATURES                      │
│  No materialized views              │  Materialized views                     │
│  No update policies                 │  Update policies (ingest-time ETL)      │
│  No partitioning policies           │  Partitioning policies (hash/range)     │
│  No row-level security              │  Row-level security                     │
│  No streaming ingestion             │  Streaming ingestion                    │
│  No external tables                 │  External tables (query parquet/csv     │
│                                     │    in ADLS without ingestion)           │
│  ACCESS CONTROL                     │  ACCESS CONTROL                         │
│  Workspace-level RBAC               │  Database and table-level RBAC          │
│  Table-level read permissions (LA)  │  Column-level security                  │
│                                     │  Row-level security policies            │
│  COST MODEL                         │  COST MODEL                             │
│  Pay-per-GB ingested + retention    │  Cluster compute (hourly) + storage     │
│  Commitment tiers: 100–5000 GB/day  │  Cost dominates at low volume;          │
│  Break-even vs ADX: ~100 GB/day     │  more cost-effective at high volume     │
└─────────────────────────────────────┴─────────────────────────────────────────┘
```

**Where to land data — decision rule:**
- Azure Monitor / Log Analytics: platform telemetry, VM logs, AKS logs, security events, App Insights. Managed, zero cluster overhead, DCR pipeline, fits Azure Monitor ecosystem.
- ADX: custom telemetry at scale, IoT/clickstream, multi-tenant analytics requiring tenant isolation (partitioning + RLS), workloads needing streaming ingestion (<10s latency), ingest-time transformation (update policies), or cost optimization at high volume (>100 GB/day cluster amortizes quickly).
- Both: ADX clusters can be linked as a data source in Azure Monitor, so you can write KQL in LA workspace that federates to ADX via `cluster()` — but `cluster()` is resolved at ADX endpoints, not native LA.

**dcount is approximate**
`dcount(col)` uses HyperLogLog and is accurate to within ~2%. For exact distinct counts use `count(distinct col)` syntax (supported in some contexts) or `summarize make_set(col) | extend count = array_length(make_set_col)` — though this is expensive on large cardinality.

**TimeGenerated vs timestamp**
Log Analytics uses `TimeGenerated` as the primary time column. App Insights uses `timestamp`. When writing queries that run in both contexts, parameterize the time column or use `ingestion_time()` as a fallback.
