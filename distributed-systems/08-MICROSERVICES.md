# Microservices Patterns: Service Mesh, Circuit Breaker, Bulkhead, Backpressure

## The Big Picture

Microservices decompose a system into independently deployable services. The distributed systems problems that arise — service discovery, traffic management, fault isolation, observability — are solved either at the application layer or delegated to infrastructure via a service mesh.

```
MICROSERVICES INFRASTRUCTURE LAYERS
+-----------------------------------------------------------------------+
|                    CLIENT / API CONSUMERS                             |
+-----------------------------------------------------------------------+
|                    API GATEWAY                                        |
|   Rate limiting, auth, routing, SSL termination, API versioning      |
+-----------------------------------------------------------------------+
|                    SERVICE MESH (CONTROL PLANE)                      |
|   Traffic policies, mTLS, circuit breaking, canary routing           |
|   No application code change required                                |
+-----------------------------------------------------------------------+
|                    DATA PLANE (SIDECAR PROXIES)                      |
|   Envoy (Istio/Dapr) or Linkerd proxy per pod                       |
|   Intercepts all network traffic in/out of service                   |
+-----------------------------------------------------------------------+
|    SVC A    |    SVC B    |    SVC C    |    SVC D    |  SVC E       |
|  [app][proxy]  [app][proxy]  [app][proxy]  [app][proxy]  [app][proxy] |
+-----------------------------------------------------------------------+
|                    SERVICE REGISTRY / DISCOVERY                      |
|   DNS (Kubernetes service DNS) or Consul / etcd                      |
+-----------------------------------------------------------------------+
|                    INFRASTRUCTURE                                     |
|   Kubernetes (AKS), container runtime, CNI networking                |
+-----------------------------------------------------------------------+
```

---

## Service Mesh: Istio and Linkerd

A service mesh moves networking concerns (TLS, retries, circuit breaking, observability) out of application code and into infrastructure.

### The Sidecar Pattern

```
WITHOUT MESH:
  Service A code:
    - Manual retry logic
    - Manual circuit breaker (Polly in .NET, Resilience4j in Java)
    - Manual mutual TLS certificate management
    - Manual metric emission for all calls
    - Manual distributed tracing instrumentation

WITH MESH (sidecar proxy):
  Service A code:
    - Just HTTP/gRPC call to "http://service-b/"
    - Proxy intercepts, handles retry/circuit break/TLS/metrics
    - Code is unaware of the mesh

  [Service A] → [Envoy sidecar] → network → [Envoy sidecar] → [Service B]
       (all traffic routed through proxies, not directly)
```

### Istio Architecture

```
ISTIO COMPONENTS

CONTROL PLANE (istiod):
  Pilot:    Service discovery, traffic management, sidecar config push
  Citadel:  Certificate authority (issues mTLS certs, rotates them)
  Galley:   Config validation and distribution

DATA PLANE:
  Envoy proxies (one per pod, as sidecar container)
  Handle: L4/L7 traffic, retries, timeouts, circuit breaking,
          mTLS termination, metrics emission, tracing spans

TRAFFIC POLICIES (defined in YAML, enforced by proxies):
  VirtualService: routing rules (header-based, weight-based canary)
  DestinationRule: load balancing, connection pool, circuit breaker
  PeerAuthentication: mTLS policy (PERMISSIVE vs. STRICT mode)
  AuthorizationPolicy: who can call what (RBAC on service calls)
```

### Canary Routing Without App Changes

```
ISTIO CANARY ROUTING
  VirtualService for "product-service":
    - 95% traffic → version v1
    - 5% traffic  → version v2 (canary)

  Both versions deployed in Kubernetes.
  Envoy enforces the split — no code change in product-service.
  Gradually shift weight: 5% → 20% → 50% → 100% as confidence grows.

HEADER-BASED ROUTING:
  - Route traffic with header "x-user-id: 12345" to v2 (beta testing)
  - All other traffic to v1
  - Useful for internal testing on production traffic
```

---

## Circuit Breaker Pattern

Prevents cascading failures by stopping calls to a service that is failing.

### Circuit States

```
CIRCUIT BREAKER STATE MACHINE

                  failure threshold
CLOSED ──────────────────────────────────> OPEN
(normal)    N failures in time window      (stop calling)
    ^                                           |
    |                                           | reset timeout
    |                                    (e.g., 30s)
    |                                           v
    |              success threshold       HALF-OPEN
    +<──────────────────────────────────── (probe request)
                 probe succeeded                |
                                           failure
                                               v
                                           back to OPEN
```

**CLOSED**: All requests flow normally. Failure counter tracking.

**OPEN**: All requests immediately fail-fast (do not call downstream). Error returned instantly to caller. Downstream gets recovery time.

**HALF-OPEN**: After reset timeout, allow one probe request. If it succeeds: close the circuit. If it fails: re-open.

### Implementation Examples

```
.NET (Polly library):
  var circuitBreaker = Policy
    .Handle<HttpRequestException>()
    .CircuitBreakerAsync(
        exceptionsAllowedBeforeBreaking: 3,
        durationOfBreak: TimeSpan.FromSeconds(30));

Istio (DestinationRule):
  outlierDetection:
    consecutive5xxErrors: 5
    interval: 1s
    baseEjectionTime: 30s
    maxEjectionPercent: 50  # Don't eject more than 50% of endpoints

Key difference:
  Polly: circuit breaker per-service-instance (in-process)
  Istio: circuit breaker at proxy level (per endpoint, mesh-wide)
```

---

## Bulkhead Pattern

Isolate failure by partitioning resources so one service's problems cannot exhaust resources needed by others.

### Thread Pool Isolation

```
WITHOUT BULKHEAD:
  Single shared thread pool (e.g., 200 threads for HTTP handling)
  Service B starts failing → all 200 threads waiting on B timeouts
  Service A, C, D calls queued → entire system degraded

WITH BULKHEAD (per-service thread pools):
  Service B pool: 50 threads → B failure consumes only these 50
  Service A pool: 50 threads → A still healthy
  Service C pool: 50 threads → C still healthy
  System pool:    50 threads → admin/health checks still work

ISOLATION SCOPE:
  Thread pool: limits concurrent calls to a dependency
  Semaphore:   limits concurrent calls but on same threads (lighter)
  Process:     complete isolation (microservices themselves are bulkheads)
  Pod:         Kubernetes resource limits per pod (CPU/memory)
```

**The ships analogy**: Bulkheads in a ship partition the hull so water in one compartment does not sink the whole ship. Thread pool bulkheads partition the system so one dependency's failure does not sink the whole application.

---

## Backpressure

Backpressure signals a producer to slow down when the consumer cannot keep up. Without backpressure, a slow consumer fills buffers until the system runs out of memory.

```
WITHOUT BACKPRESSURE:
  Producer (fast) ──────> unbounded queue ──────> Consumer (slow)
  Queue fills → OutOfMemoryError → crash

WITH BACKPRESSURE:
  Producer (fast) ──x── bounded queue ← "full" signal ── Consumer (slow)
  Producer: slow down, retry, or apply back-off

REACTIVE STREAMS SPECIFICATION (Java/JVM):
  Publisher.subscribe(Subscriber)
  Subscriber.onSubscribe(Subscription)
  Subscription.request(n) ← consumer requests N items
  Publisher emits at most n items → respects consumer capacity
  Implemented by: RxJava, Reactor (Spring WebFlux), Akka Streams

HTTP/2 FLOW CONTROL:
  TCP backpressure: receiver advertises window size
  HTTP/2: per-stream flow control on top of TCP
  gRPC (on HTTP/2): inherits flow control → natural backpressure

KAFKA CONSUMER BACKPRESSURE:
  Consumer pulls at its own rate (consumer lag grows temporarily)
  Producer continues writing to Kafka (durable buffer)
  Consumer catches up when capacity is available
  → Kafka log acts as a durable backpressure buffer
```

---

## Saga Orchestration vs. Choreography

Revisited from the distributed transactions perspective, applied to microservices:

```
ORCHESTRATION PATTERN
  Central orchestrator service drives the saga:

  Orchestrator
       |── T1: call Payment Service ─→ success
       |── T2: call Inventory Service ─→ success
       |── T3: call Shipping Service ─→ FAIL
       |── C2: call Inventory to rollback
       |── C1: call Payment to rollback

  + Clear workflow visible in one place
  + Easy to add monitoring, alerting on saga state
  + Retry/resume logic in one service
  - Orchestrator becomes coupled to all participating services
  - Risk: orchestrator becomes too smart (domain logic leakage)

  Tool: Azure Durable Functions (orchestrator = orchestrator function,
        activities = activity functions)

CHOREOGRAPHY PATTERN
  No central coordinator; services react to events:

  Payment Service:
    receives "OrderPlaced" event
    processes payment → emits "PaymentCompleted"

  Inventory Service:
    receives "PaymentCompleted"
    reserves stock → emits "StockReserved"

  Shipping Service:
    receives "StockReserved"
    fails → emits "ShippingFailed"

  Inventory Service:
    receives "ShippingFailed"
    releases stock → emits "StockReleased"

  Payment Service:
    receives "StockReleased"
    refunds payment

  + Services are decoupled (only know about events, not each other)
  + Easier to add new participants (subscribe to existing events)
  - Flow is implicit in event chains → hard to visualize end-to-end
  - Debugging cross-service failures requires tracing correlation IDs
  - Compensating logic is distributed across services

WHEN TO USE:
  Orchestration: complex workflows with many conditions and rollbacks
  Choreography: simple flows, high decoupling required, streaming pipelines
```

---

## API Gateway

```
API GATEWAY RESPONSIBILITIES
+----------------------------------------------------------+
|                     API GATEWAY                          |
+----------------------------------------------------------+
| SSL/TLS termination  | Single HTTPS endpoint to clients  |
| Auth/AuthZ           | JWT validation, OAuth token verify |
| Rate limiting        | Per client, per endpoint limits   |
| Request routing      | Route /users → user-service       |
| Load balancing       | Distribute within a service pool  |
| API versioning       | /v1/, /v2/ routing               |
| Request/response     | Transform, validate, enrich       |
| transformation                                           |
| Response caching     | Cache GET responses               |
| Observability        | Centralized access logging        |
+----------------------------------------------------------+

AZURE API MANAGEMENT (APIM):
  Products: logical group of APIs (e.g., "Partner APIs")
  Subscriptions: key-based access to products
  Policies: XML pipeline applied per operation:
    inbound → backend → outbound → on-error
  Built-in: JWT validation, rate limiting, IP filtering,
            OpenAPI import, developer portal, analytics

ALTERNATIVES:
  Kong (open source, Nginx-based, plugin ecosystem)
  AWS API Gateway
  Nginx/Envoy as gateway (more raw, less managed)
```

---

## Service Discovery

```
DNS-BASED (Kubernetes default):
  Service "payment-service" created in Kubernetes
  kube-dns creates: payment-service.namespace.svc.cluster.local
  Consumers call this DNS name → auto-resolved to current pods
  Simple, no client-side library needed
  Updates: when pods change, DNS TTL propagates (near-instant for kube-dns)

REGISTRY-BASED (Consul, etcd):
  Services register on startup with name, address, health check endpoint
  Consumer queries registry: "give me instances of payment-service"
  Registry returns list → client-side load balancing
  More control (weighted routing, metadata filtering)
  Used by: Consul service catalog, Netflix Eureka (legacy)

CLIENT-SIDE vs. SERVER-SIDE LOAD BALANCING:
  Client-side: client has registry, picks instance, calls directly
    + No extra hop
    - Every service needs registry client library (language proliferation)
  Server-side: client calls a proxy/gateway, proxy picks instance
    + Language-agnostic
    - Extra network hop
    - Service mesh uses server-side (proxy in sidecar)
```

---

## Common Confusion Points

**"Service mesh replaces the API gateway"**
No. Service mesh (Istio/Linkerd) handles east-west traffic (service-to-service inside the cluster). API gateway handles north-south traffic (external clients to cluster). They serve different layers.

**"Circuit breaker = retry logic"**
They are complementary but different. Retries try the same operation again (useful for transient failures). Circuit breakers stop calling a failing service entirely (useful for sustained failures). Retries without circuit breakers amplify load on a struggling service.

**"Bulkheads are about performance"**
Bulkheads are about fault isolation, not performance. They limit the blast radius of a failure to a subset of resources. Performance may be similar with or without bulkheads under normal conditions.

**"Sagas are weaker than 2PC"**
Sagas provide different guarantees. 2PC provides isolation (other readers don't see in-progress state). Sagas do not. For many business workflows, the lack of isolation is acceptable (users tolerate seeing intermediate states). For financial transactions, design compensating transactions carefully.

---

## Decision Cheat Sheet

| Problem | Pattern |
|---------|---------|
| Downstream service is flaky | Circuit Breaker |
| One service's failures cascade | Bulkhead (thread pool isolation) |
| Fast producer overwhelms consumer | Backpressure (reactive streams, Kafka as buffer) |
| Multi-service atomic workflow | Saga (orchestration or choreography) |
| Service-to-service TLS, retries, routing | Service Mesh (Istio / Linkerd) |
| External traffic ingress, auth, rate limit | API Gateway (APIM, Kong) |
| Service location resolution | DNS-based (Kubernetes) or Registry (Consul) |
| A/B testing in production | Canary routing via service mesh VirtualService |
