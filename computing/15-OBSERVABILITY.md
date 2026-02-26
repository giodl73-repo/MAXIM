# 15 — Observability

## The Big Picture

```
Monitoring vs Observability
============================

  Monitoring (old world)             Observability (new world)
  ======================             =========================

  "Is it up?"                        "Why is it slow for users in Brazil?"
  Predefined dashboards              Ask arbitrary questions of system state
  Known failure modes only           Debug novel failures you didn't anticipate
  Alert on thresholds                Understand causality

  Nagios / SCOM / pager              Prometheus + Grafana + Jaeger + OpenTelemetry
  "The server is down"               "Request 7a3f took 4.2s — 3.8s was in the DB
                                      query on the orders table from pod api-6d8b"
```

```
The Three Pillars
==================

  LOGS                    METRICS                  TRACES
  ====                    =======                  ======

  What happened           How much / how fast      Where did time go

  Discrete events         Numeric measurements     Request journey
  Text (structured JSON)  aggregated over time     across services
  High cardinality        Low cardinality           Distributed context

  "Error: order 4821     "p99 latency = 340ms"    "POST /checkout
   not found at 14:32"   "error rate = 0.3%"        → order-svc: 12ms
                         "DB connections: 47"        → inventory-svc: 8ms
                                                      → payment-svc: 280ms
  ELK / Loki             Prometheus / Datadog          → Stripe API: 261ms"
  CloudWatch Logs        Grafana / CloudWatch       Jaeger / Tempo / Zipkin
  Azure Monitor Logs     Azure Monitor Metrics      Azure Monitor + App Insights
```

> **App Insights → three pillars mapping**
>
> Application Insights covers all three pillars in a single vertically integrated product. The OSS stack disaggregates those same concerns:
>
> | App Insights concept | OSS equivalent |
> |---|---|
> | Log Analytics workspace (traces/events table) | Loki |
> | Azure Monitor Metrics / custom metrics | Prometheus |
> | Application Map + distributed traces (requests + dependencies tables) | Jaeger / Tempo |
> | Workbooks (unified dashboards) | Grafana |
>
> If you've used App Insights, you already understand the three-pillar model — you just knew it under different names. Every new tool in this guide has a direct App Insights analog. Use that as your primary anchor.

```
Full Observability Stack
=========================

  Your services
  ┌──────────────────────────────────────────────────────────┐
  │  API   Worker   Auth   DB Proxy   ...                    │
  │  │       │       │        │                              │
  │  └───────┴───────┴────────┘                              │
  │          OpenTelemetry SDK (instrument once)             │
  │          emits: logs + metrics + traces                  │
  └────────────────────────┬─────────────────────────────────┘
                           │
           OpenTelemetry Collector (optional gateway)
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
    Loki (logs)     Prometheus (metrics)  Tempo (traces)
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
                    Grafana (unified UI)
```

---

## Logs

### Structured vs Unstructured

```
Unstructured (bad)                 Structured JSON (good)
==================                 ======================

[14:32:11] ERROR order 4821        {
not found in database                "timestamp": "2026-02-22T14:32:11Z",
                                     "level": "error",
                                     "message": "order not found",
                                     "orderId": 4821,
                                     "userId": "usr_9x3k",
                                     "service": "order-svc",
                                     "traceId": "7a3f8b2c..."
                                   }

Hard to query                      Queryable by any field
Regex required                     Filter: level=error AND service=order-svc
No context                         Correlate with trace ID
```

> **Serilog → Pino bridge**
>
> In .NET you have `Serilog` / `NLog` / `Microsoft.Extensions.Logging` for structured logging. You write `Log.Information("Order {OrderId} placed by {UserId}", orderId, userId)` and a sink forwards enriched JSON to App Insights, Seq, or a file.
>
> Node.js equivalent is **Pino** (fastest; JSON-first) or Winston (more configurable). Same concept: log as structured JSON, configure a transport/sink to route output.
>
> ```
> Serilog                          Pino (Node.js)
> ───────                          ──────────────
> Log.Information("{K}", v)        logger.info({ k: v }, "msg")
> LogContext.PushProperty(...)     logger.child({ k: v })
> .WriteTo.ApplicationInsights()   transport: pino-applicationinsights
> .WriteTo.Seq()                   transport: pino-seq
> .Enrich.WithTraceIdentifier()    automatic via OTel pino transport
> ```
>
> JSON written to stdout is what Promtail scrapes and ships to Loki — same as Serilog's App Insights sink forwarding to Log Analytics.

### Logging in Node.js — Pino

```javascript
import pino from "pino";

const logger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  // In prod: output JSON. In dev: pretty-print
  transport: process.env.NODE_ENV !== "production"
    ? { target: "pino-pretty" }
    : undefined,
});

// Log with structured context
logger.info({ orderId: 4821, userId: "usr_9x3k" }, "order not found");
logger.error({ err, orderId }, "payment failed");

// Child logger — all entries inherit these fields
const reqLogger = logger.child({ requestId: req.id, userId: req.user.id });
reqLogger.info("checkout started");
```

Output in production (JSON, one line per event — Loki/ELK can ingest directly):
```json
{"level":30,"time":1740232331000,"requestId":"abc","userId":"usr_9x3k","msg":"checkout started"}
```

### Log Aggregation — Loki

Loki (from Grafana Labs) indexes log metadata (labels) but not log content — dramatically cheaper than Elasticsearch for storage.

```
Loki Architecture
==================

  Pods → Promtail (agent, reads log files) → Loki → Grafana

  Labels (indexed, low cardinality):
    {service="order-svc", env="production", pod="order-6d8b-abc"}

  Log content (not indexed — full text search via grep-like LogQL):
    {"level":"error","orderId":4821,...}

LogQL query examples:
  {service="order-svc"} |= "error"              -- filter by label + content
  {env="production"} | json | level="error"     -- parse JSON, filter field
  rate({service="api"}[5m])                     -- log rate metric
```

> **KQL → LogQL contrast**
>
> If you query Log Analytics daily with KQL, be aware: **LogQL is not KQL**. KQL is a columnar query language — SQL-like, with `join`, `summarize`, computed columns, time-series math. LogQL is a log filter language optimized for label-based stream filtering.
>
> ```
> KQL                                     LogQL equivalent
> ───                                     ────────────────
> where ResultCode >= 500                 {app="myapp"} | json | status >= 500
> where timestamp > ago(5m)              [5m] range selector on stream
> summarize count() by bin(timestamp,5m) rate({app="myapp"}[5m])  (LogQL metric query)
> join (other table) on ...              No JOIN — use Grafana correlation instead
> summarize percentile(duration, 99) by  histogram_quantile() in PromQL, not LogQL
> ```
>
> LogQL has no JOINs, no computed columns, no time-series math (that's PromQL's domain). For SQL-like log analysis, Log Analytics + KQL remains more expressive. LogQL is optimized for high-volume label-based filtering and rate metrics — it scales cheaply because Loki doesn't index content.

---

## Metrics

### Prometheus Data Model

Prometheus scrapes HTTP endpoints (`/metrics`) on a schedule and stores time-series data.

```
Metric types:
  Counter     — ever-increasing number (requests, errors)
                http_requests_total{method="POST", status="200"} 1247

  Gauge       — can go up or down (current connections, queue depth)
                db_connections_active 47

  Histogram   — bucketed observations (request duration)
                http_request_duration_seconds_bucket{le="0.1"} 9823
                http_request_duration_seconds_bucket{le="0.5"} 14201
                http_request_duration_seconds_bucket{le="1.0"} 14687
                → used to calculate percentiles (p50, p95, p99)

  Summary     — pre-calculated percentiles (less flexible than histogram)
```

### Exposing Metrics in Node.js

```javascript
import { collectDefaultMetrics, Counter, Histogram, register } from "prom-client";

// Auto-collect Node.js process metrics (heap, event loop lag, etc.)
collectDefaultMetrics();

// Custom metrics
const httpRequests = new Counter({
  name: "http_requests_total",
  help: "Total HTTP requests",
  labelNames: ["method", "route", "status"],
});

const httpDuration = new Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request latency",
  labelNames: ["method", "route"],
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
});

// Middleware
app.use((req, res, next) => {
  const end = httpDuration.startTimer({ method: req.method, route: req.path });
  res.on("finish", () => {
    httpRequests.inc({ method: req.method, route: req.path, status: res.statusCode });
    end();
  });
  next();
});

// Scrape endpoint — Prometheus hits this
app.get("/metrics", async (req, res) => {
  res.set("Content-Type", register.contentType);
  res.send(await register.metrics());
});
```

> **Push vs pull model**
>
> App Insights uses **push**: the SDK calls `trackMetric()` and data flows to Azure. Your app sends; Azure receives.
>
> Prometheus uses **pull**: Prometheus server scrapes your service's `/metrics` endpoint on a configurable schedule (default 15s). Your app exposes; Prometheus comes to collect.
>
> Consequence: Prometheus requires your service to expose a metrics HTTP endpoint. App Insights does not — it just needs outbound HTTPS to Azure. For **short-lived functions or batch jobs** that exit before Prometheus can scrape them, use the **Prometheus Pushgateway** (a buffer that accepts push and holds metrics for scraping) or stick with App Insights / Azure Monitor custom metrics (which are push-friendly by design).
>
> Azure Monitor Container Insights running on AKS scrapes a Prometheus-compatible `/metrics` endpoint under the hood — so the two models are converging, but the conceptual default is inverted.

### PromQL — Prometheus Query Language

```promql
# Request rate over last 5 minutes
rate(http_requests_total[5m])

# Error rate (proportion of 5xx)
rate(http_requests_total{status=~"5.."}[5m])
  / rate(http_requests_total[5m])

# p99 latency
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# By service — group the above
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (service, le)
)

# Alert: error rate > 1% for 5 minutes
- alert: HighErrorRate
  expr: |
    rate(http_requests_total{status=~"5.."}[5m])
      / rate(http_requests_total[5m]) > 0.01
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "Error rate {{ $value | humanizePercentage }} on {{ $labels.service }}"
```

---

## Traces

### The Problem Traces Solve

```
Monolith (easy to debug)           Microservices (where did the time go?)
========================           =======================================

  Single process                     POST /checkout → 4.2 seconds total
  Stack trace shows everything         Where was it?
  One log stream                       api-gateway?  order-svc?
                                       inventory-svc?  payment-svc?
                                       Stripe?  DB?

  → Traces answer this question
```

### OpenTelemetry Tracing

```
Trace anatomy
==============

  Trace ID: 7a3f8b2c...          (one per request, propagated across services)

  Spans:
  ├── POST /checkout              [api-gateway]  0ms → 4200ms
  │   ├── validate session        [api-gateway]  2ms → 15ms
  │   ├── HTTP POST /orders       [order-svc]    15ms → 310ms
  │   │   ├── DB SELECT products  [order-svc]    16ms → 89ms
  │   │   └── DB INSERT order     [order-svc]    90ms → 308ms
  │   └── HTTP POST /payment      [payment-svc]  310ms → 4198ms
  │       └── Stripe API call     [payment-svc]  312ms → 4195ms ← SLOW
```

```javascript
// Instrument with OpenTelemetry (auto + manual)
import { NodeSDK } from "@opentelemetry/sdk-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";

// SDK setup (usually in a separate tracing.ts, loaded first)
const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: "http://otel-collector:4318/v1/traces",
  }),
  instrumentations: [
    getNodeAutoInstrumentations(),   // auto: HTTP, Express, pg, redis, etc.
  ],
});
sdk.start();

// Manual spans for business logic
import { trace } from "@opentelemetry/api";
const tracer = trace.getTracer("order-service");

async function processOrder(orderId: string) {
  return tracer.startActiveSpan("processOrder", async (span) => {
    span.setAttribute("order.id", orderId);
    try {
      const result = await doWork();
      span.setStatus({ code: SpanStatusCode.OK });
      return result;
    } catch (err) {
      span.recordException(err);
      span.setStatus({ code: SpanStatusCode.ERROR });
      throw err;
    } finally {
      span.end();
    }
  });
}
```

> **App Insights SDK → OTel SDK bridge**
>
> The App Insights SDK pattern you know:
> ```javascript
> appInsights.setup(connectionString)
>   .setAutoCollectRequests(true)
>   .setAutoCollectDependencies(true)   // HTTP, DB, Redis
>   .setAutoCollectExceptions(true)
>   .start();
> client.trackDependency({ ... });
> ```
>
> The OTel equivalent:
> ```javascript
> new NodeSDK({
>   instrumentations: [getNodeAutoInstrumentations()],  // HTTP, DB, Redis, etc.
>   traceExporter: new OTLPTraceExporter({ url: "..." }),
> }).start();
> tracer.startActiveSpan("name", span => { span.setAttribute(...); });
> ```
>
> Concept mapping:
>
> | App Insights SDK | OTel SDK |
> |---|---|
> | `setAutoCollectRequests(true)` | `getNodeAutoInstrumentations()` HTTP server instrumentation |
> | `setAutoCollectDependencies(true)` | `getNodeAutoInstrumentations()` HTTP client / DB instrumentation |
> | `client.trackDependency(...)` | manual span with `span.setAttribute("db.statement", ...)` |
> | `client.trackRequest(...)` | auto-instrumented HTTP server span |
> | App Insights correlation headers | W3C `traceparent` header (OTel standard) |
> | Connection string → App Insights backend | `OTLPTraceExporter` URL → any OTLP-compatible backend |
>
> Key value: OTel is vendor-neutral. Swap the exporter URL; your instrumentation code doesn't change. See the Azure Monitor Exporter note below for keeping App Insights as the backend while adopting the OTel SDK.

### Context Propagation

Trace IDs cross service boundaries via HTTP headers (`traceparent`). Every downstream HTTP call automatically carries the parent span ID so traces stitch together across services.

```
Service A                          Service B
─────────                          ─────────
fetch("http://order-svc/...")
  Headers:
    traceparent: 00-7a3f8b2c...-abc123-01
                                   Auto-extracted by OTel middleware
                                   Span created as child of abc123
```

---

## OpenTelemetry

The unifying standard. One SDK, any backend.

```
OpenTelemetry Architecture
===========================

  Your app
  ┌────────────────────────────────────────────┐
  │  OTel SDK                                  │
  │  - Auto-instrumentation (HTTP, DB, etc.)   │
  │  - Manual spans + attributes               │
  │  - Metrics API                             │
  │  - Logs bridge                             │
  └────────────────────┬───────────────────────┘
                       │  OTLP protocol
                       ▼
          OTel Collector (optional but recommended)
          ┌────────────────────────────────────────┐
          │  Receivers: OTLP, Jaeger, Zipkin, ...  │
          │  Processors: batch, filter, enrich     │
          │  Exporters: Tempo, Jaeger, Datadog,    │
          │             Azure Monitor, Honeycomb   │
          └────────────────────────────────────────┘
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
          Tempo      Jaeger    Datadog    (or any OTLP-compatible backend)
```

OTel is vendor-neutral. Instrument once. Swap backends without changing application code. This is the key value: you don't lock yourself to Datadog's SDK.

---

## Grafana Stack

The standard open-source observability UI. One UI, all three pillars.

```
Grafana Data Sources
=====================

  Loki      → logs      (LogQL)
  Prometheus → metrics  (PromQL)
  Tempo      → traces   (TraceQL)

  Grafana correlates them:
  → Click a spike in a metrics graph
  → Jump to logs at that timestamp
  → Jump to trace that caused the spike
```

> **Azure Monitor → Grafana bridge**
>
> Grafana is to the OSS stack what **Azure Monitor Workbooks** is to the Azure stack — a unified dashboard layer over heterogeneous data sources. You've used Workbooks to combine Log Analytics queries, metric charts, and App Insights data in one view; Grafana does the same with Loki, Prometheus, and Tempo.
>
> The two worlds are not mutually exclusive: Azure has a first-party **Grafana data source plugin** for Azure Monitor, and **Azure Managed Grafana** is a fully managed Grafana service (GA). If your team runs on Azure but adopts OSS tooling, you can point Grafana at Azure Monitor as a data source and keep all dashboards in one place.

### Dashboard as Code

```yaml
# Grafonnet / JSON — dashboards in git
panels:
  - title: "Request Rate"
    type: graph
    targets:
      - expr: rate(http_requests_total[5m])
        legendFormat: "{{service}}"

  - title: "p99 Latency"
    type: graph
    targets:
      - expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

### Alerting

```yaml
# Grafana alert rule (UI or YAML)
- alert: HighLatency
  condition: p99 > 1s for 5 minutes
  notifications:
    - PagerDuty
    - Slack #oncall
```

---

## Azure Monitor + Application Insights

The Azure-native equivalent of the full Grafana stack.

```
Azure Monitor
=============

  Application Insights    ← APM: requests, dependencies, exceptions, traces
  Log Analytics           ← centralized logs (KQL query language)
  Azure Monitor Metrics   ← platform metrics (VM CPU, App Service requests)
  Alerts                  ← threshold/smart detection alerts → Action Groups
  Workbooks               ← Grafana-equivalent dashboards
  Container Insights      ← AKS pod/node metrics + logs

  All data → Log Analytics Workspace (unified store)
```

```javascript
// Application Insights SDK (Node.js)
import appInsights from "applicationinsights";

appInsights
  .setup(process.env.APPLICATIONINSIGHTS_CONNECTION_STRING)
  .setAutoCollectRequests(true)
  .setAutoCollectDependencies(true)    // HTTP, DB, Redis calls
  .setAutoCollectExceptions(true)
  .start();

// Custom events + metrics
const client = appInsights.defaultClient;
client.trackEvent({ name: "OrderPlaced", properties: { orderId, userId } });
client.trackMetric({ name: "CheckoutDuration", value: durationMs });
```

```kusto
// KQL — Log Analytics query language (similar to SQL + pipe syntax)
requests
| where timestamp > ago(1h)
| where resultCode >= 500
| summarize count() by bin(timestamp, 5m), cloud_RoleName
| render timechart

// P99 latency per operation
requests
| where timestamp > ago(24h)
| summarize percentile(duration, 99) by name
| order by percentile_duration_99 desc
```

> **OTel SDK → App Insights backend**
>
> You can instrument with the vendor-neutral OTel SDK and still land data in App Insights / Log Analytics. The OTel Collector has an `azuremonitor` exporter, and the Azure Monitor OpenTelemetry Distro packages this for .NET, Node.js, Python, and Java:
>
> ```javascript
> // Node.js — OTel SDK + Azure Monitor exporter
> import { NodeSDK } from "@opentelemetry/sdk-node";
> import { AzureMonitorTraceExporter } from "@azure/monitor-opentelemetry-exporter";
>
> new NodeSDK({
>   traceExporter: new AzureMonitorTraceExporter({
>     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING,
>   }),
>   instrumentations: [getNodeAutoInstrumentations()],
> }).start();
> ```
>
> Same App Insights backend, standard OTel SDK. The Application Map, distributed traces, and KQL queries all work as before — you just swapped the proprietary SDK for a vendor-neutral one. Best of both: portable instrumentation code, Azure-native storage and alerting.

---

## SLIs, SLOs, SLAs

The language of production reliability — you built SLAs at VSTS, this is the modern framing:

```
SLI  Service Level Indicator   — the metric you're measuring
     "availability" = successful_requests / total_requests

SLO  Service Level Objective   — the target you set internally
     "99.9% of requests return 2xx over 30-day rolling window"
     "p99 latency < 500ms"

SLA  Service Level Agreement   — contractual commitment to customers
     "99.9% uptime per month, or credits issued"

Error Budget
     SLO = 99.9% → allowed failure = 0.1% = 43.2 min/month
     Budget governs how much risk you can take with deployments
     Budget exhausted → freeze risky changes until next period
```

---

## Common Confusion Points

**Logs and traces are not the same thing.**
A log is a discrete event with a timestamp. A trace is a structured record of a request's path through the system, composed of spans. You can correlate them via trace ID in log fields.

**Prometheus `rate()` requires a counter, not a gauge.**
`rate()` calculates per-second change. Calling it on a gauge (which can go down) gives meaningless results. Use `rate()` on counters; use raw values or `delta()` for gauges.

**High-cardinality labels destroy Prometheus.**
Labels like `userId` or `orderId` create millions of time series — one per unique value. Prometheus stores all series in memory. Label values should be bounded: `method`, `route`, `status_code`, `service`. Never put user IDs or request IDs in labels.

**OpenTelemetry is not a backend — it's an instrumentation standard.**
You still need a backend (Tempo, Jaeger, Zipkin, Honeycomb, Datadog). OTel defines how to collect and ship telemetry. The Collector is a process that receives and forwards telemetry — it's optional but recommended for decoupling your app from backend choice.

**Application Insights vs Azure Monitor.**
Application Insights is a feature of Azure Monitor (not a separate product). They share the same Log Analytics workspace. Application Insights adds APM-specific features (request tracking, dependency maps, live metrics stream) on top of Azure Monitor's storage and alerting.

---

## Old World Bridge

| App Insights / Azure Monitor | Modern Observability |
|---|---|
| App Insights requests table | Distributed trace root spans (Tempo / Jaeger) |
| App Insights dependencies table | Child spans — external HTTP/DB/Redis calls |
| App Insights exceptions table | Span error events (`span.recordException()`) |
| App Insights customMetrics table | Prometheus Counter / Gauge / Histogram |
| App Insights traces table (KQL) | Loki logs (LogQL label filter) |
| Application Map (distributed view) | Jaeger / Tempo trace waterfall |
| App Insights SDK auto-collect | OTel `getNodeAutoInstrumentations()` |
| `client.trackDependency()` | Manual OTel span with `span.setAttribute()` |
| App Insights connection string → Azure | OTel exporter URL → any OTLP backend |
| Log Analytics Workbooks | Grafana dashboards |
| KQL (Log Analytics) | LogQL (Loki) — not a direct equivalent; KQL is more expressive |
| Azure Monitor Metrics (push) | Prometheus (pull — scrapes `/metrics` endpoint) |
| SCOM agent on every server | OTel SDK in every service |
| SCOM Management Pack per app | Auto-instrumentation for HTTP/DB/etc. |
| Custom perf counters (Windows) | Prometheus metrics / OTel metrics |
| Event log (Windows) | Structured JSON logs → Loki / Log Analytics |
| SCOM correlation rules | Distributed traces (spans, trace IDs) |
| SCOM dashboards | Grafana dashboards |
| SCOM alert → pager | Grafana alert → PagerDuty / Slack |
| Azure Data Factory pipeline monitoring | OTel spans on each pipeline step |
| Availability tests (App Insights) | Synthetic monitors / uptime checks |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Record what happened (events, errors) | Structured logs → Loki / Log Analytics |
| Measure how fast / how many | Metrics → Prometheus / Azure Monitor Metrics |
| Find where a slow request spent its time | Distributed traces → Tempo / Jaeger / App Insights |
| Instrument a Node.js service once, pick backend later | OpenTelemetry SDK |
| Visualize all three pillars in one UI | Grafana (OSS) or Azure Monitor Workbooks |
| Set an alert when error rate spikes | Prometheus Alertmanager / Grafana Alerts / Azure Alerts |
| Query logs with SQL-like syntax (Azure) | Log Analytics (KQL) |
| Query logs (OSS) | Loki (LogQL) |
| Calculate p99 latency | Prometheus Histogram + `histogram_quantile()` |
| Track user journeys and business events | App Insights custom events / OTel custom spans |
| Define "what does healthy mean" | SLOs on key SLIs with error budgets |
| Avoid Datadog/Honeycomb vendor lock-in | OpenTelemetry SDK → OTel Collector → any backend |
| Keep App Insights backend, adopt OTel SDK | Azure Monitor OpenTelemetry Distro / `azuremonitor` exporter |
| Short-lived function/job push metrics to Prometheus | Prometheus Pushgateway |
