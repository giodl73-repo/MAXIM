# Observability in Distributed Systems: Tracing, Correlation IDs, Chaos Engineering

## The Big Picture

Observability is the ability to understand the internal state of a system from its external outputs. In distributed systems, no single node has global visibility — observability must be engineered from day one.

```
THE THREE PILLARS OF OBSERVABILITY
+-----------------------------------------------------------------------+
|                                                                       |
|   LOGS              METRICS              TRACES                       |
|   +------------+    +------------+       +------------------+         |
|   | Discrete   |    | Aggregated |       | Request journey  |        |
|   | events at  |    | measurements|      | across services  |        |
|   | a point in |    | over time  |       | (spans, timing,  |        |
|   | time       |    | (counters, |       | causality)       |        |
|   |            |    | gauges,    |       |                  |        |
|   | ECS format |    | histograms)|       | W3C TraceContext  |        |
|   | structured |    | Prometheus |       | Jaeger, Zipkin   |        |
|   | JSON       |    | model      |       | OpenTelemetry    |        |
|   +------------+    +------------+       +------------------+        |
|         |                 |                       |                  |
|         +─────────────────+───────────────────────+                  |
|                           |                                           |
|                  CORRELATION ID threads through all three            |
|                  → single request traceable end-to-end               |
|                                                                       |
+-----------------------------------------------------------------------+

TOOL LANDSCAPE
+-----------------------------------------------------------------------+
| LOGS:     ELK Stack, Splunk, Azure Monitor Logs, Loki               |
| METRICS:  Prometheus + Grafana, Azure Monitor Metrics, Datadog      |
| TRACES:   Jaeger, Zipkin, Azure Monitor (App Insights), Tempo       |
| STANDARD: OpenTelemetry (OTEL) — collector + SDKs, replacing all   |
+-----------------------------------------------------------------------+
```

---

## Structured Logging

Logs are the most primitive observability signal. Structured logs are machine-parseable (JSON/NDJSON) rather than free-form strings.

```
UNSTRUCTURED LOG (terrible for distributed systems):
  2026-02-25 10:23:45 ERROR Payment failed for user 12345 amount 99.99

STRUCTURED LOG (ECS format — Elastic Common Schema):
  {
    "@timestamp": "2026-02-25T10:23:45.123Z",
    "log.level": "error",
    "message": "Payment failed",
    "event.category": "payment",
    "user.id": "12345",
    "transaction.amount": 99.99,
    "trace.id": "abc123def456",       ← correlation ID
    "span.id": "789xyz",
    "service.name": "payment-service",
    "service.version": "1.2.3",
    "error.type": "InsufficientFunds",
    "error.message": "Account balance below required amount"
  }
```

**Why structure matters**: In a system with 100 microservices emitting millions of logs per minute, you cannot grep through free text. You query: `service.name=payment-service AND log.level=error AND trace.id=abc123def456`.

### Log Levels in Practice

```
DEBUG   Development only. Never in production (volume/noise/cost).
        "Entering method processPayment with args [...]"

INFO    Normal operational events. "Payment processed successfully"
        Filtered out in most production alerting.

WARN    Unusual but handled. "Retry attempt 2/3 for payment API"
        Investigate if frequency rises. Not necessarily a problem.

ERROR   Something failed that requires attention.
        "Payment failed after 3 retries"
        Should trigger alert review.

CRITICAL/FATAL  System cannot continue. "Database connection pool exhausted"
                Wake-up-at-3am alert.
```

**Azure Monitor Logs (Log Analytics)**: Kusto Query Language (KQL). You know ADF's expression language; KQL is similar in spirit but far more powerful for log analytics. `AppTraces | where SeverityLevel == 3 | where Properties.TraceId == "abc123"`.

---

## Metrics: The Prometheus Model

Metrics are aggregated measurements over time — not individual events.

### Metric Types

```
COUNTER: Monotonically increasing value
  http_requests_total{method="POST", status="200"} = 42389
  Use: request count, error count, bytes sent
  Query: rate(http_requests_total[5m]) → requests per second

GAUGE: Current value (can go up or down)
  active_connections = 142
  memory_usage_bytes = 2147483648
  Use: current state, pool sizes, queue depth
  Query: just the current value, or min/max over time window

HISTOGRAM: Distribution of values in configurable buckets
  http_request_duration_seconds_bucket{le="0.1"} = 8342   ← ≤100ms
  http_request_duration_seconds_bucket{le="0.5"} = 9981   ← ≤500ms
  http_request_duration_seconds_bucket{le="1"}   = 10000  ← ≤1s
  http_request_duration_seconds_count = 10000
  http_request_duration_seconds_sum = 1234.5
  Use: latency percentiles (p50, p95, p99)
  Query: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
         → p99 latency over last 5 minutes

SUMMARY: Pre-computed client-side quantiles
  http_request_duration_seconds{quantile="0.99"} = 0.943
  Use: when you want quantiles without histogram overhead
  Limitation: cannot aggregate across instances (already aggregated)
  → Prefer HISTOGRAM for distributed systems (aggregate server-side)
```

### Prometheus Pull vs. Push

```
PROMETHEUS (pull model):
  Scrapes /metrics endpoint on each service
  Service exposes metrics in text format
  Prometheus stores time series
  Grafana queries Prometheus for dashboards
  AlertManager handles alerting rules

PUSH GATEWAY (for short-lived jobs):
  Batch job pushes metrics to Pushgateway
  Prometheus scrapes Pushgateway

AZURE MONITOR METRICS (push model):
  Azure services push metrics automatically
  Custom metrics pushed via REST API or SDKs
  Queried via Azure Metrics Explorer or KQL
```

---

## Distributed Tracing

Traces show the complete journey of a single request through multiple services.

### Trace Anatomy

```
TRACE: Single request (trace-id: abc123)
+---------------------------------------------------------------+
| SPAN: api-gateway (duration: 250ms)                           |
|   |                                                           |
|   +-- SPAN: auth-service (duration: 15ms)                     |
|   |      JWT validation                                       |
|   |                                                           |
|   +-- SPAN: product-service (duration: 200ms)                 |
|          |                                                    |
|          +-- SPAN: product-db (duration: 45ms)                |
|          |      SELECT * FROM products WHERE id=123           |
|          |                                                    |
|          +-- SPAN: recommendation-service (duration: 120ms)   |
|                 async call, parallel with db query            |
+---------------------------------------------------------------+

Each SPAN has:
  trace-id:    same for all spans in this request (abc123)
  span-id:     unique per span (xyz789)
  parent-id:   id of parent span (enables tree reconstruction)
  service:     which service emitted this span
  operation:   what operation (HTTP GET /products/123)
  start_time:  wall clock
  duration:    milliseconds
  status:      OK or ERROR
  attributes:  key-value tags (http.method, db.statement, user.id)
  events:      log-like annotations within the span
```

### W3C TraceContext Header

The industry standard for propagating trace context across service boundaries:

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             |  |                                |              |  |
             |  trace-id (128-bit, 32 hex chars) |              |  |
             version                          span-id           flags
                                              (64-bit)         (sampled)

tracestate: vendor-specific additional context
  e.g., tracestate: ms=abc123 (Microsoft-specific extensions)

HTTP HEADER PROPAGATION:
  Service A calls Service B:
    → include traceparent header with A's trace-id and A's span-id as parent
  Service B receives:
    → extracts trace-id (same throughout) and parent-id (A's span-id)
    → creates new span with same trace-id, new span-id, parent=A's span-id
    → propagates to any downstream calls
```

**App Insights / Azure Monitor**: Uses W3C TraceContext natively. If you're already using Application Insights SDK (.NET, Java, Node), distributed tracing across services is automatic as long as all services use it.

---

## OpenTelemetry: The Emerging Standard

OpenTelemetry (OTEL) is a CNCF project that unifies observability signals into one set of APIs, SDKs, and a collector.

```
BEFORE OTEL (pre-2019):
  Datadog agent + SDK
  Jaeger client library
  Zipkin client library
  App Insights SDK
  All vendor-specific → lock-in, multiple SDKs in same codebase

AFTER OTEL:
  One SDK (OpenTelemetry SDK) per language
  Instruments: logs, metrics, traces
  Exports to any backend:
    → Azure Monitor
    → Datadog
    → Jaeger
    → Prometheus
    → Honeycomb
    → Any OTLP-compatible backend

OTEL ARCHITECTURE:
  App (with OTEL SDK)
       |
       | OTLP protocol (over gRPC or HTTP/protobuf)
       v
  OTEL Collector (sidecar or standalone service)
       |
       | fan out to multiple backends
       +── Azure Monitor
       +── Prometheus (metrics)
       +── Jaeger (traces)
       +── Log sink

STATUS (2026): OTEL is the dominant standard for new instrumentation.
  Vendor SDKs are now OTEL-compatible (App Insights uses OTEL internally).
```

---

## Correlation IDs

The mechanism that threads all three pillars together for a single request:

```
REQUEST ENTERS SYSTEM:
  If no correlation ID: generate UUID at gateway
  If correlation ID exists: extract from header (X-Correlation-ID or W3C traceparent)

PROPAGATE TO EVERY DOWNSTREAM CALL:
  HTTP: add as header
  gRPC: add as metadata
  Message queue: add in message headers
  Database calls: add to log context (not to DB itself)

INCLUDE IN EVERY LOG ENTRY:
  {"trace.id": "abc123", "message": "Payment processed", ...}

INCLUDE IN EVERY METRIC LABEL (use sparingly):
  High-cardinality labels (unique per request) explode metric series count
  → Do NOT add trace-id to metric labels
  → OK to add service, method, status code

SEARCH ACROSS ALL SYSTEMS:
  Given trace-id=abc123:
    → Query logs: find all log entries for this request
    → Query traces: find all spans for this trace tree
    → Reconstruct full request journey across 15 services in 3 minutes
```

---

## Chaos Engineering

Deliberately introduce failures into production to find weaknesses before users do.

```
CHAOS ENGINEERING PRINCIPLES (Netflix, 2014)

1. Build a hypothesis about steady-state behavior
   "99.9% of homepage loads complete in < 500ms"

2. Vary real-world events
   Instance failure, network latency injection, CPU pressure,
   DNS failure, AZ outage, clock skew

3. Run experiments in production (or production-like)
   Staging environments don't have the same traffic patterns

4. Automate experiments continuously
   Not a one-time exercise — run regularly as the system evolves

5. Minimize blast radius
   Start small: 1% of traffic, one region, one service
   Scale up as confidence grows

TOOLS:
  Chaos Monkey (Netflix OSS): randomly terminates VMs
  Chaos Kong: terminates entire AWS regions
  Chaos Mesh (CNCF): Kubernetes-native fault injection
  Azure Chaos Studio: managed chaos experiments on Azure
  Gremlin: commercial chaos platform

TYPES OF EXPERIMENTS:
  Instance termination: kill random VMs/pods
  Network latency: add 100ms-1s delay to service calls
  Network partition: block traffic between services/zones
  Resource exhaustion: fill disk, exhaust CPU, memory pressure
  Dependency failure: return errors from specific downstream APIs
  Clock skew: advance/regress clock on specific nodes
```

### GameDays

A GameDay is a structured chaos exercise where a team runs fault scenarios in a controlled setting:

```
GAMEDAY STRUCTURE
  1. Define scenario: "What if our payment service becomes unavailable?"
  2. Hypothesis: "Circuit breakers will open, users see degraded mode"
  3. Execute: inject the failure in staging or low-traffic production
  4. Observe: monitor dashboards, alerts, customer impact
  5. Review: did the system behave as expected?
     If yes: add to regression suite
     If no: fix the gap, add to runbooks
  6. Document: update disaster recovery playbooks
```

---

## SRE Error Budgets and SLO/SLA/SLI

Observability ultimately serves reliability targets. The SRE framework gives these precise definitions:

```
SLI (Service Level Indicator): what you measure
  "The fraction of HTTP requests that complete in < 300ms"
  "The fraction of requests that return HTTP 2xx"

SLO (Service Level Objective): your internal target
  "99.9% of requests complete in < 300ms over 30-day rolling window"
  "99.99% of requests return HTTP 2xx"
  SLO is the internal commitment. NOT a customer promise yet.

SLA (Service Level Agreement): contractual commitment to customers
  "We guarantee 99.9% uptime or we credit your bill"
  SLA = SLO minus safety margin (you'd set SLO at 99.95% to stay above 99.9% SLA)

ERROR BUDGET:
  99.9% SLO over 30 days = 0.1% budget = 43.8 minutes/month of failure
  99.99% SLO = 4.38 minutes/month

  If budget is consumed:
    → Freeze feature work, focus on reliability
    → Post-mortem on what consumed budget

  If budget is healthy:
    → Proceed with feature work, experiments, deployments
    → Budget remaining = indicator that reliability investment is sufficient

AZURE DEVOPS / VSTS ANALOGY:
  You had service health metrics, on-call rotations, postmortems.
  The SRE framework formalizes this: SLI=your health metric,
  SLO=your internal uptime target, SLA=your published SLA to customers.
  Error budget is the enforcement mechanism that makes the trade-off
  between reliability and velocity explicit rather than political.
```

---

## Common Confusion Points

**"Logs are enough for observability"**
Logs lack aggregation (you can't easily compute p99 latency from logs) and request flow (correlating 50 service logs manually is impractical). All three pillars serve different purposes.

**"Adding more logging = better observability"**
Unstructured high-volume logs with no correlation IDs provide less value than structured low-volume logs with correlation IDs. Noise drowns signal. Structured logging at INFO with trace IDs beats verbose DEBUG.

**"Sampling loses important data"**
Head-based sampling (sampling the decision at trace entry) does risk losing rare events. Tail-based sampling (decide after the trace completes based on outcome) retains errors and slow traces. Use tail-based sampling or 100% sampling for error spans, sampled for success.

**"Chaos engineering is dangerous"**
Netflix runs Chaos Monkey in production daily. The philosophy: better to find failures in controlled experiments than from user complaints. The key is: blast radius control, monitoring in place, rollback procedures ready.

---

## Decision Cheat Sheet

| Scenario | Tool / Approach |
|----------|----------------|
| Why did request X fail? | Distributed trace (trace-id lookup) |
| Is p99 latency increasing? | Metrics (histogram query) |
| What happened at 3am? | Structured logs with correlation ID |
| Is service A talking to service B? | Service mesh telemetry |
| Find all errors in the last hour | Log query (KQL / Elasticsearch) |
| Measure if new deploy degraded latency | Before/after metric comparison |
| Test resilience of circuit breaker | Chaos experiment (inject failure) |
| Validate SLO compliance | Error budget dashboard |
| Standardize instrumentation across 10 services | OpenTelemetry SDK |
