# KQL — Kusto Query Language

KQL is Microsoft's pipe-based query language for log analytics and telemetry at scale. It powers Azure Monitor, Log Analytics, Application Insights, Azure Data Explorer (ADX), and Microsoft Sentinel. If you've used App Insights, you've used KQL. The mental model shift from SQL: rows flow left-to-right through operators via the pipe character, like Unix. No SELECT...FROM...WHERE — instead: `table | where | project | summarize`.

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
  Log Analytics : workspace-scoped, retention policies, data collection rules
  App Insights  : auto-instrumented telemetry tables, smart detection
  Sentinel      : security analytics, hunting queries, detection rules, playbooks
  ADX           : dedicated analytics cluster, external tables, ingestion
                  pipelines, streaming ingestion, massive scale

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

## 2. MENTAL MODEL SHIFT — SQL vs KQL

```
SQL (set-based, declarative — clause order ≠ execution order):

  SELECT   columns           ← what to return
  FROM     table             ← source
  JOIN     other ON ...      ← combine
  WHERE    condition         ← filter rows (pre-aggregate)
  GROUP BY columns           ← aggregate
  HAVING   condition         ← filter groups (post-aggregate)
  ORDER BY columns           ← sort
  TOP n                      ← limit

KQL (pipe-based, left-to-right data flow — written order = execution order):

  table                      ← source
  | where condition          ← filter rows  (= SQL WHERE)
  | join kind=inner (...)    ← combine      (= SQL JOIN)
  | extend newcol = expr     ← add computed column
  | summarize agg by col     ← aggregate    (= SQL GROUP BY)
  | where agg_condition      ← filter after aggregation  (= SQL HAVING)
  | order by col             ← sort
  | take n                   ← limit        (= SQL TOP / LIMIT)
  | project col1, col2       ← SELECT columns (can also rename)

The pipe passes a "result table" through each operator.
Each operator receives a table and outputs a table.
Order matters — unlike SQL clause execution order.

Key difference: in SQL you can write clauses in any order and the engine
figures out execution. In KQL, the written order IS the execution order.
Put expensive filters (where) as early as possible.
```

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

---

## 12. RENDER — Visualization

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

## 13. COMMON APP INSIGHTS PATTERNS

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

## 14. COMMON AZURE MONITOR LOG ANALYTICS PATTERNS

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

## 15. SENTINEL HUNTING PATTERNS

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

## 16. SQL → KQL TRANSLATION TABLE

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

## 17. DECISION CHEAT SHEET

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

## 18. COMMON CONFUSION POINTS

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

**Log Analytics vs ADX — same syntax, different features**
Log Analytics (Azure Monitor) uses the same KQL parser but lacks some ADX features: no external tables, no streaming ingestion, no update policies, no row-level security. ADX has all of those plus cross-cluster queries. If you need analytics-at-scale with custom ingestion pipelines, ADX is the right tier.

**dcount is approximate**
`dcount(col)` uses HyperLogLog and is accurate to within ~2%. For exact distinct counts use `count(distinct col)` syntax (supported in some contexts) or `summarize make_set(col) | extend count = array_length(make_set_col)` — though this is expensive on large cardinality.

**TimeGenerated vs timestamp**
Log Analytics uses `TimeGenerated` as the primary time column. App Insights uses `timestamp`. When writing queries that run in both contexts, parameterize the time column or use `ingestion_time()` as a fallback.
