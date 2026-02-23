# 17 — Cloud-Native Patterns

## The Big Picture

```
Cloud-Native: What It Actually Means
======================================

Not: "runs in a cloud"
Yes: "designed for the properties of cloud infrastructure"

  Cloud properties:              Cloud-native design response:
  ─────────────────              ─────────────────────────────
  Instances fail                 Design for failure (expect crashes)
  Scale horizontally             Stateless services
  Elastic capacity               Auto-scaling + load shedding
  Network is unreliable          Retry with backoff, circuit breakers
  Deployments are frequent       Zero-downtime deploys, feature flags
  Many services                  Service discovery, async messaging
  Teams are autonomous           Loose coupling, independent deploys
```

```
The Architecture Spectrum
==========================

  Monolith               Modular Monolith          Microservices
  ────────               ────────────────          ─────────────
  One deployable         One deployable            Many independent
  unit                   unit, internal            deployable units
                         modules/domains

  Simple to deploy       Good middle ground        Maximum autonomy
  Easy to debug          Easier than micro         Operational complexity
  Hard to scale parts    Can extract later         Complex distributed sys
  Team coupling          Reduced coupling          Team independence

  Start here             Often the right answer    When you need it
  (most apps)            (medium/large teams)      (large orgs, FAANG scale)
```

---

## Microservices

### What Makes a Good Service Boundary

```
Bad boundary (technical layer)    Good boundary (business capability)
================================  ===================================

  UserController                    OrderService
  UserRepository                    InventoryService
  UserService                       PaymentService
  ProductController                 NotificationService
  ProductRepository                 UserService
  ...

  Same team touches all of them     Each owned by one team
  Every feature touches all layers  Deploy independently
  Shared database = tight coupling  Own their data store
```

```
Conway's Law (still true):
  System architecture ≡ communication structure of the org that builds it.
  If 4 teams work on one monolith → 4 modules that don't integrate cleanly.
  If each team owns a service → services are well-bounded.
```

### The Distributed Systems Tax

Microservices trade one set of problems for another. Know what you're buying:

```
Monolith gives you free:           Microservices require you to build:
════════════════════════           ══════════════════════════════════
  In-process function call           Network call (latency + failures)
  ACID transaction across tables     Distributed transaction / saga
  Single log stream                  Distributed tracing (15-OBSERVABILITY)
  One deploy artifact                Many CI/CD pipelines (13-CICD)
  Simple local dev                   docker compose / service mesh / local K8s
  One database schema                Data ownership across services
```

Only pay this tax when the organizational benefits outweigh the operational costs.

---

## Event-Driven Architecture

### Synchronous vs Asynchronous

```
Synchronous (request/response)     Asynchronous (event-driven)
==============================     ===========================

  A calls B, waits for response      A publishes event, continues
                                     B consumes event later

  A ──────────► B                    A ──► Queue/Topic ──► B
     ◄──────────                                           C
                                                           D

  Tight temporal coupling            Temporal decoupling
  A fails if B is down               A succeeds even if B is down
  A slows if B is slow               B processes at its own pace
  Simple to reason about             Harder to trace / debug
  Good for: reads, queries           Good for: writes, fan-out, spikes
```

### Message Patterns

```
Queue (point-to-point)             Topic / Pub-Sub (fan-out)
======================             =========================

  Producer → Queue → Consumer        Publisher → Topic → Consumer A
                                                        → Consumer B
  Each message consumed once                             → Consumer C

  Good for: work distribution,       Good for: event broadcast,
  background jobs, rate limiting     audit log, multiple reactions
                                     to one business event

  Azure Service Bus (Queue)          Azure Service Bus (Topic)
  AWS SQS                            Azure Event Grid
  RabbitMQ                           AWS SNS + SQS
                                     Kafka (both, at scale)
```

### Kafka

Apache Kafka is the dominant event streaming platform for high-throughput, durable event logs.

```
Kafka vs Traditional Message Queues
=====================================

  Traditional Queue              Kafka
  ═════════════════              ═════
  Message deleted on consume     Message retained (days/weeks)
  One consumer per message       Multiple consumer groups, each reads all
  No replay                      Replay from any offset
  Push to consumer               Consumer pulls at own pace
  Good for: tasks                Good for: event log, stream processing,
                                  audit trail, multiple downstream systems

  Order
  ┌──────────────────────────────────────────────────────────┐
  │  Topic: orders                                           │
  │                                                          │
  │  Partition 0: [order:1] [order:4] [order:7] →            │
  │  Partition 1: [order:2] [order:5] [order:8] →            │
  │  Partition 2: [order:3] [order:6] [order:9] →            │
  │                                                          │
  │  Consumer group A (analytics):  reads all partitions     │
  │  Consumer group B (fulfillment): reads all partitions    │
  │  Consumer group C (audit):      reads all partitions     │
  └──────────────────────────────────────────────────────────┘

  Ordered within a partition (by key: e.g., customerId)
  Parallelism = partition count
```

```javascript
// Kafka producer (kafkajs)
import { Kafka } from "kafkajs";

const kafka = new Kafka({ brokers: ["kafka:9092"] });
const producer = kafka.producer();

await producer.connect();
await producer.send({
  topic: "orders",
  messages: [
    {
      key: order.customerId,           // same customer → same partition → ordered
      value: JSON.stringify(order),
      headers: { "event-type": "order.created" },
    },
  ],
});

// Kafka consumer
const consumer = kafka.consumer({ groupId: "fulfillment-service" });
await consumer.connect();
await consumer.subscribe({ topic: "orders", fromBeginning: false });

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    const order = JSON.parse(message.value.toString());
    await fulfillOrder(order);
    // Offset committed automatically after eachMessage returns
  },
});
```

---

## Resilience Patterns

### Circuit Breaker

```
Without circuit breaker            With circuit breaker
════════════════════               ════════════════════

  Every request to failing           Closed → Open → Half-open
  service hangs for timeout
                                     CLOSED: requests pass through
  100 concurrent requests              (normal operation)
  × 10s timeout                      OPEN: requests fail fast
  = 1000s of blocked threads           (service is known-bad)
                                     HALF-OPEN: probe request
  Cascading failure →                  (is it recovered?)
  whole system slow
                                     Prevents cascade, fast failure
```

```javascript
// Opossum — circuit breaker for Node.js
import CircuitBreaker from "opossum";

const breaker = new CircuitBreaker(callPaymentService, {
  timeout: 3000,              // fail if > 3s
  errorThresholdPercentage: 50, // open if >50% fail
  resetTimeout: 30000,        // try again after 30s
});

breaker.on("open", () => logger.warn("Payment service circuit open"));
breaker.on("halfOpen", () => logger.info("Payment service probing"));
breaker.on("close", () => logger.info("Payment service recovered"));

// Use it
const result = await breaker.fire(paymentData);
```

### Retry with Exponential Backoff

```
Naive retry (bad)                  Exponential backoff + jitter (good)
═════════════════                  ══════════════════════════════════

  retry immediately                  attempt 1: wait 1s ± jitter
  retry immediately                  attempt 2: wait 2s ± jitter
  retry immediately                  attempt 3: wait 4s ± jitter
  ...                                attempt 4: wait 8s ± jitter
                                     max attempts: give up + dead letter

  Thundering herd:                   Jitter spreads the load:
  1000 clients all retry             not all clients retry at t=1.0s
  simultaneously → DDoS              spread across 0.8–1.2s window
  your own service
```

```javascript
async function withRetry(fn, { maxAttempts = 4, baseDelayMs = 1000 } = {}) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt === maxAttempts) throw err;
      const delay = baseDelayMs * 2 ** (attempt - 1) * (0.5 + Math.random() * 0.5);
      await new Promise(r => setTimeout(r, delay));
    }
  }
}
```

### Bulkhead

Isolate failures so one slow dependency can't consume all resources.

```
Without bulkhead                   With bulkhead
════════════════                   ══════════════

  Shared thread pool                 Separate thread pool per downstream
  ┌──────────────────┐               ┌──────────────┐  ┌──────────────┐
  │ 100 threads      │               │ 30 threads   │  │ 30 threads   │
  │                  │               │ payment-svc  │  │ inventory    │
  │ payment-svc slow │               └──────────────┘  └──────────────┘
  │ → fills all 100  │               ┌──────────────┐
  │ → auth blocked   │               │ 40 threads   │
  └──────────────────┘               │ auth/other   │
                                     └──────────────┘
  One slow dep = system down         payment pool fills → auth still works
```

### Saga Pattern (Distributed Transactions)

No distributed ACID transactions in microservices. Sagas coordinate multi-service operations using compensating actions on failure.

```
Order Saga (Choreography)
==========================

  OrderService                InventoryService           PaymentService
  ════════════                ════════════════           ══════════════
  order.created ──────────►
                              inventory.reserved ──────►
                                                         payment.captured
                                                                │
                                    ◄─────────────────── order.fulfilled
  ◄────────────────────────── order.completed

  On failure at any step → compensating events published:
    payment.failed → inventory.released → order.cancelled
```

---

## Service Mesh

When you have many services, cross-cutting concerns (retries, mTLS, observability) get duplicated in every service. A service mesh moves them to the infrastructure layer.

```
Without service mesh               With service mesh (Istio / Linkerd)
════════════════════               ═══════════════════════════════════

  Each service implements:           Sidecar proxy injected alongside
    - retry logic                    each pod (Envoy / linkerd-proxy)
    - circuit breaker
    - mTLS                           Proxy handles:
    - distributed tracing              - retry + circuit breaker
    - rate limiting                    - mTLS (zero-trust between services)
                                       - distributed tracing
  100 services = 100 copies          - rate limiting
  of the same plumbing               - traffic splitting (canary)

                                     Your service just makes plain HTTP calls
                                     Mesh handles the rest transparently
```

```
Service Mesh Architecture
==========================

  Pod A                              Pod B
  ┌─────────────────────┐            ┌─────────────────────┐
  │  App container      │            │  App container      │
  │  ┌───────────────┐  │            │  ┌───────────────┐  │
  │  │  your service │  │            │  │  your service │  │
  │  └───────┬───────┘  │            │  └───────┬───────┘  │
  │          │          │            │          │          │
  │  ┌───────▼───────┐  │  mTLS     │  ┌───────▼───────┐  │
  │  │  Envoy sidecar│◄─┼───────────┼─►│  Envoy sidecar│  │
  │  └───────────────┘  │           │  └───────────────┘  │
  └─────────────────────┘            └─────────────────────┘
            │                                  │
            └──────────── Control Plane ───────┘
                          (Istiod / linkerd)
                          configures all proxies
```

---

## API Gateway

Entry point for all external traffic. Centralizes auth, rate limiting, routing, and protocol translation.

```
API Gateway Pattern
====================

  Clients                        Internal Services
  ───────                        ─────────────────

  Mobile App ─────┐              ┌──► OrderService
                  │              │
  Web App ────────┼─► API        ├──► UserService
                  │   Gateway    │
  Third-party ────┘   │          ├──► InventoryService
                      │          │
                       └─────────┴──► PaymentService

  Gateway handles:
    Authentication (validate JWT)
    Rate limiting (100 req/min per client)
    Request routing (path → service)
    Protocol translation (REST → gRPC)
    Response aggregation (BFF pattern)
    SSL termination
    Logging + tracing injection
```

Azure API Management, AWS API Gateway, Kong, Traefik, nginx — all play this role.

---

## Deployment Patterns

### Blue/Green

```
Blue/Green Deployment
======================

  Before:                            After cutover:
  ┌─────────────────┐                ┌─────────────────┐
  │ Load Balancer   │                │ Load Balancer   │
  │ → Blue (v1) ✅  │                │ → Green (v2) ✅ │
  │ → Green (v2) 💤│                │ → Blue (v1) 💤  │
  └─────────────────┘                └─────────────────┘

  Green tested while Blue serves     Switch is instant (LB route change)
  traffic                            Rollback = switch back to Blue
  Zero downtime                      Requires 2× resource capacity
```

### Canary Release

```
Canary Deployment
==================

  Stage 1:   1% → v2,  99% → v1    (watch error rates, latency)
  Stage 2:  10% → v2,  90% → v1    (if healthy, continue)
  Stage 3:  50% → v2,  50% → v1
  Stage 4: 100% → v2                (full rollout)

  At any stage: metrics cross threshold → automatic rollback to 0%

  Kubernetes: Argo Rollouts or Flagger automate this
  Feature flags: route % of users to new code path (LaunchDarkly, etc.)
```

### Feature Flags

```javascript
// LaunchDarkly / Unleash / custom
const enabled = await featureFlags.isEnabled("new-checkout-flow", {
  userId: user.id,
  attributes: { plan: user.plan, country: user.country },
});

if (enabled) {
  return newCheckoutFlow(cart);
} else {
  return legacyCheckoutFlow(cart);
}
```

Decouple deployment from release. Ship code to prod dark; enable for 1% of users; ramp up; kill the flag. No redeploy needed to roll back.

---

## The 12-Factor App

The foundational checklist for cloud-native services. Originally from Heroku (2011), still the canonical reference.

```
Factor          What It Means
──────────────────────────────────────────────────────────────────
I.   Codebase   One repo, many deploys. Not one repo per env.
II.  Deps       Explicitly declare deps (package.json). No implicit system deps.
III. Config     Config in env vars. Not in code, not in files checked into git.
IV.  Backing    Treat backing services (DB, cache) as attached resources.
     Services   Swap Postgres URL → point at different DB. No code change.
V.   Build/Run  Strictly separate build → release → run stages.
VI.  Processes  Stateless. Shared state in backing services (DB/Redis), not memory.
VII. Port       Export via port binding. Service IS the server (no app server needed).
     Binding
VIII.Concurrency Scale out via processes, not threads. Add pods, not heap.
IX.  Disposable Fast startup. Graceful shutdown. Crash-only design.
X.   Dev/Prod   Keep dev, staging, prod as similar as possible. Docker helps.
     Parity
XI.  Logs       Treat logs as event streams. Write to stdout. Platform aggregates.
XII. Admin      Run admin tasks as one-off processes. Not cron in app. Not manual.
     Processes
```

---

## Common Confusion Points

**Microservices ≠ cloud-native.**
You can have a cloud-native monolith (stateless, 12-factor, containers, CI/CD). Microservices are one architectural pattern within cloud-native, not the definition of it.

**Event-driven doesn't mean Kafka.**
A simple job queue (Azure Service Bus, AWS SQS, BullMQ on Redis) is event-driven. Kafka is warranted when you need high throughput, replay, or multiple independent consumer groups on the same event stream. Most apps don't need Kafka.

**Service mesh is not for small teams.**
Istio especially has significant operational complexity. Linkerd is lighter. If you have fewer than ~20 services, implement resilience patterns in-process or via a shared library. The mesh pays off at scale with large teams.

**Saga != two-phase commit.**
2PC (two-phase commit) is a distributed transaction protocol that locks resources — it doesn't work at scale or across independent services. A saga is a sequence of local transactions with compensating actions. It trades ACID atomicity for availability.

**Circuit breaker state is per-instance.**
If you have 10 pods of your API, each has its own circuit breaker state. Pod A might have an open circuit while Pod B's is closed. That's fine — eventual convergence. Don't try to share circuit state across instances.

**Feature flags are not only for incomplete features.**
They're also for kill switches (disable a component under load), A/B testing, gradual rollouts, and operational toggles. Having a flag for every major new behavior is good practice regardless of completeness.

---

## Old World Bridge

| WCF / SOA / .NET Enterprise Patterns | Cloud-Native Equivalent |
|---|---|
| WCF service host | Containerized HTTP service (Kestrel / Express) |
| ESB (Enterprise Service Bus) | Event broker (Kafka, Azure Service Bus) + choreography |
| MSMQ | Azure Service Bus Queue / AWS SQS |
| WCF reliable sessions | Retry + idempotent consumers |
| Distributed Transaction Coordinator (DTC) | Saga pattern with compensating actions |
| IIS Application Pool recycling | K8s pod restart on liveness probe failure |
| Web farm (manual scaling) | HPA on AKS (auto-scale pods) |
| Azure Traffic Manager (weighted routing) | Canary deployments via Istio / Argo Rollouts |
| Azure APIM | API Gateway pattern (same tool, same concept) |
| Deployment slots (App Service) | Blue/green deployments on K8s |
| App.config / web.config | Environment variables (Factor III) |
| Windows Service (background worker) | K8s Deployment with no ingress / CronJob |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Build a new product with a small team | Modular monolith first |
| Split a monolith into services | Extract by business capability, not tech layer |
| Decouple services so they don't need to be up simultaneously | Async messaging (Service Bus / SQS / Kafka) |
| Fan out one event to many consumers | Pub-Sub topic (Event Grid / SNS / Kafka topic) |
| High-throughput durable event log with replay | Kafka |
| Prevent cascading failures | Circuit breaker (Opossum) + timeouts |
| Handle transient network errors | Retry with exponential backoff + jitter |
| Coordinate a multi-service write without 2PC | Saga pattern |
| Handle cross-cutting concerns (mTLS, retry, tracing) centrally | Service mesh (Linkerd for simplicity, Istio for power) |
| Route external traffic, enforce auth + rate limits | API Gateway (Azure APIM, Kong, Traefik) |
| Deploy with zero downtime and instant rollback | Blue/green |
| Gradually roll out to real users, auto-rollback on errors | Canary (Argo Rollouts / Flagger) |
| Ship code dark, release when ready | Feature flags (LaunchDarkly, Unleash) |
| Know if my service is cloud-native | 12-Factor checklist |
