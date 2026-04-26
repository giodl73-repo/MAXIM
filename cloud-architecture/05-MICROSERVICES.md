# Microservices at Scale: AKS, Service Mesh, API Management, Event Grid

## The Big Picture

Microservices in Azure are typically orchestrated by AKS (or Container Apps for managed simplicity), connected via API Management for external traffic, and integrated through Event Grid/Event Hubs/Service Bus for asynchronous workflows.

```
AZURE MICROSERVICES REFERENCE ARCHITECTURE
+-----------------------------------------------------------------------+
|                                                                       |
|  INTERNET / CLIENTS                                                   |
|       |                                                               |
|       v                                                               |
|  Azure Front Door (global WAF + CDN + routing)                        |
|       |                                                               |
|       v                                                               |
|  Azure API Management (auth, rate limit, policy pipeline)             |
|       |                                                               |
|       v                                                               |
|  AKS Ingress (nginx or AGIC - App Gateway Ingress Controller)       |
|       |                                                               |
|  +----+----+----+----+                                                |
|  |    |    |    |    |                                               |
|  Svc  Svc  Svc  Svc  (microservices in pods, service mesh mTLS)     |
|  A    B    C    D                                                     |
|  |                                                                    |
|  +── Service Bus (reliable messaging)                               |
|  +── Event Hubs  (streaming)                                        |
|  +── Event Grid  (reactive events)                                  |
|                                                                       |
|  Data layer:                                                          |
|  Azure SQL / Cosmos DB / Redis / Blob                               |
|  (each service has its own data store — polyglot persistence)       |
+-----------------------------------------------------------------------+
```

---

## AKS Deep-Dive: Beyond the Basics

### Control Plane Architecture

```
AKS CONTROL PLANE (managed by Azure, free):

API Server:
  Your kubectl, CI/CD pipelines, operators talk to this
  Authentication: Azure AD (Entra ID OIDC) + Kubernetes RBAC
  REST API endpoint, WebSocket (kubectl exec/attach)

etcd:
  All cluster state: nodes, pods, services, deployments, configmaps, secrets
  Raft consensus (3-node or 5-node depending on tier)
  AKS Uptime SLA tier: 99.95% or 99.99% control plane SLA

Scheduler:
  Watches for unscheduled pods
  Scores nodes by: resource requests/limits, node affinity,
  pod anti-affinity, taints/tolerations, topology spread
  Assigns pod to optimal node

Controller Manager:
  Runs reconciliation loops:
    Deployment controller: ensures desired replicas running
    Node controller: watches node health
    Endpoints controller: updates service endpoint lists
    Job controller: runs batch jobs to completion
```

### Node Pools

```
SYSTEM NODE POOL:
  Required: at least one system pool
  Runs: CoreDNS, metrics-server, tunnel-front, CSI drivers, kube-proxy
  Taint: CriticalAddonsOnly=true:NoSchedule
    → Your workload pods don't land here unless tolerated
  Recommendation: 3+ nodes across 3 AZs; VM: Standard_D4s_v5 or similar
  Do NOT schedule application workloads here

USER NODE POOLS:
  Run your application workloads
  Can create multiple with different SKUs:
    General: Standard_D8s_v5 (web APIs, microservices)
    Memory: Standard_E16s_v5 (Redis, Java services with high heap)
    GPU: Standard_NC4as_T4_v3 (ML inference)
    Spot: low cost, interruptible (batch processing)

POOL AUTOSCALING:
  cluster-autoscaler watches pending pods
  Scale out: pod pending because no node has enough resources → add node
  Scale in: node CPU/memory utilization below threshold for 10min → remove
  Config: min/max node count per pool
```

### Kubernetes Objects Reference

```
POD: One or more containers, shared network namespace (same IP)
     Ephemeral: pods die, get rescheduled, different IP each time
     Never talk to pods directly (IP changes); talk to Services

SERVICE: Stable virtual IP (ClusterIP) for a set of pods
  Types:
    ClusterIP: internal only (default)
    NodePort: exposes on each node at static port (avoid in production)
    LoadBalancer: creates Azure Load Balancer (external access)
    ExternalName: DNS alias to external service

INGRESS: L7 routing rules for HTTP/HTTPS → Service mapping
  Requires ingress controller (nginx, AGIC, Traefik)
  AGIC (Application Gateway Ingress Controller):
    Provisions Azure Application Gateway based on Ingress resources
    Native WAF, TLS termination, autoscaling App Gateway

DEPLOYMENT: Desired state for a set of pods
  Rolling update: update one pod at a time
  Rollback: kubectl rollout undo deployment/name
  Resource requests/limits: CPU milliCPU, memory bytes

STATEFULSET: Like Deployment but for stateful apps
  Stable network identity (pod-0, pod-1, ...)
  Ordered startup/shutdown
  Per-pod PersistentVolumeClaims

DAEMONSET: One pod per node (logging agents, node monitoring)
```

---

## Service Mesh in Azure: Istio, Linkerd, OSM

### Azure Service Mesh Add-on (Istio)

AKS has a managed Istio add-on (GA 2023):

```
ENABLE ISTIO ON AKS:
  az aks mesh enable --resource-group myRG --name myAKS

ISTIO CONTROL PLANE (managed by Azure):
  istiod runs as a managed component (Azure patches/upgrades it)
  Automatic sidecar injection: add label "istio-injection: enabled" to namespace

WHAT ISTIO GIVES YOU (without code changes):
  mTLS: all pod-to-pod traffic automatically encrypted + authenticated
  Traffic policies: weighted routing, circuit breaking, retries
  Observability: telemetry automatically collected (Prometheus, Jaeger, Kiali)
  Authorization: RBAC at service-call level

PEER AUTHENTICATION (mTLS enforcement):
  PERMISSIVE: both plain text and mTLS accepted (migration mode)
  STRICT: only mTLS accepted (production mode)
  Namespace-level or global policy

AUTHORIZATION POLICY (who can call what):
  Allow only payment-service to call fraud-detection-service:
    source.principals: ["cluster.local/ns/default/sa/payment-service"]
```

### Linkerd (lighter weight alternative)

Linkerd v2 is a CNCF graduated project. Lighter than Istio:
- Less CPU/memory overhead (~10x less resource usage than Istio)
- Simpler — does not have all Istio features
- Rust-based data plane (linkerd-proxy)
- Good for: production environments where resource efficiency matters; teams that find Istio too complex

**Choice guide**: New setup → start with Istio add-on (Azure managed). Istio too heavy → Linkerd. Need advanced traffic management (per-route retries, fault injection, flexible auth) → Istio.

---

## Azure API Management (APIM)

APIM is Azure's fully managed API gateway with developer portal, policy pipeline, and product catalog.

```
APIM CORE CONCEPTS

PRODUCTS:
  A product is a bundle of APIs
  Developers subscribe to products to get access
  Products can be: public (anyone), protected (subscription key), admin

APIs:
  Import from: OpenAPI spec, WSDL (SOAP), Azure Functions, Logic Apps, App Service
  Each API has operations (GET /users, POST /orders)

SUBSCRIPTIONS:
  Key-based access: developer subscribes → gets subscription key
  Include key in header: Ocp-Apim-Subscription-Key
  Or: override with OAuth 2.0 (validate-jwt policy preferred for new APIs)

POLICY PIPELINE:
  XML-based declarative pipeline applied per operation
  Four sections:
    <inbound>  → transform/validate incoming request
    <backend>  → configure backend call
    <outbound> → transform response before returning to caller
    <on-error> → handle errors

COMMON POLICIES:
  rate-limit-by-key: 10 calls per 60 seconds per client IP
  validate-jwt: verify JWT token, extract claims
  set-header: add/remove headers
  rewrite-uri: transform URL before forwarding to backend
  cache-lookup / cache-store: response caching
  return-response: mock or short-circuit
  mock-response: return test data without hitting backend
  quota: lifetime or period-based quota per subscription
  cors: set CORS headers

TIERS:
  Developer: no SLA, testing only
  Basic: 99.9% SLA, 1 unit
  Standard: 99.9%, autoscale
  Premium: 99.99%, multi-region, VNet integration, private endpoints
  Consumption: serverless, per-call billing, scale to 0
```

---

## Azure Event Grid vs. Event Hubs vs. Service Bus

This is one of the most frequently confused topics in Azure integration.

```
EVENT GRID (reactive routing):
  Publisher → Topic → Subscriptions → Subscriber endpoints
  At-most-once delivery (retries for up to 24h, then drops)
  Event size: up to 1MB
  Source events: Azure resource changes (VM created, Blob uploaded),
                 custom publishers
  Subscriber endpoints: Azure Functions, Logic Apps, webhooks, Event Hubs, Service Bus
  Schema: EventGrid schema or CloudEvents 1.0
  Pricing: per million events
  USE: "Something happened in Azure → trigger a reaction"
       Blob uploaded → trigger processing function
       Resource created → update CMDB
       Custom application events → fan out to multiple handlers

EVENT HUBS (streaming log):
  Producers → Partitioned Log → Consumer Groups
  Retention: 1–7 days (Standard), up to 90 days (Premium)
  Ordering: per partition (Kafka partition ordering)
  Consumer groups: multiple independent consumers read same stream
  Kafka-compatible API: migrate Kafka workloads with minimal code change
  Throughput units: scale independently (now auto-inflate available)
  USE: High-throughput event streams, telemetry ingestion, streaming analytics
       IoT devices → Event Hubs → Stream Analytics → Power BI
       Application metrics → Event Hubs → Azure Monitor

SERVICE BUS (reliable messaging):
  Queues: point-to-point, message guaranteed to be delivered once
  Topics + Subscriptions: pub/sub with filter rules
  Features:
    Dead-letter queue (DLQ): failed messages go here after max retries
    Message sessions: ordered delivery per session ID
    Duplicate detection: dedup by MessageId within time window
    Scheduled delivery: send at specific time
    Transactions: atomic queue operations
    Long TTL: messages survive days (unlike Event Grid 24h)
  Message size: up to 256KB (Standard) / 100MB (Premium)
  USE: Reliable business process messaging, ordered workflows, retry with DLQ
       Order placed → queue → payment service + fulfillment service

DECISION MATRIX:
+----------------------------------+-------------+-------------+--------+
| Need                             | Event Grid  | Event Hubs  | Svc Bus|
+----------------------------------+-------------+-------------+--------+
| React to Azure resource changes  | ✓ YES       | ✗           | ✗      |
| High-throughput (millions/sec)   | ✗           | ✓ YES       | ✗      |
| Replay events (stream history)   | ✗           | ✓ YES       | ✗      |
| Kafka compatibility              | ✗           | ✓ YES       | ✗      |
| At-least-once reliable delivery  | ~           | ✓ YES       | ✓ YES  |
| Dead-letter queue                | ✗           | ✗           | ✓ YES  |
| Ordered delivery per session     | ✗           | Per partition| ✓ YES  |
| Long message retention (days)    | ✗           | 1-90 days   | TTL    |
| Transactional message ops        | ✗           | ✗           | ✓ YES  |
+----------------------------------+-------------+-------------+--------+
```

---

## Dapr: Distributed Application Runtime

Dapr is a CNCF project (originally from Microsoft) that provides standardized building blocks for microservices via a sidecar.

```
DAPR BUILDING BLOCKS:

State management:
  app → Dapr sidecar HTTP/gRPC → Dapr state store (Redis, Cosmos DB, SQL)
  App code: POST /v1.0/state/statestore {"key":"session","value":"..."}
  → Dapr handles connection to Redis, TTL, consistency options
  → Swap state store: change config, no code change

Pub/Sub:
  app → Dapr → Service Bus / Kafka / Redis Streams
  Standardized: same API regardless of broker
  CloudEvents envelope: automatic

Service invocation:
  app → Dapr → target app (by app-id, not IP/hostname)
  mTLS automatic between Dapr sidecars
  Service discovery via Dapr name resolution

Bindings (input/output):
  Output: app → Dapr → Blob, Queue, Kafka, HTTP, PostgreSQL, etc.
  Input: Trigger app when event occurs in external system

Secrets:
  app → Dapr → Key Vault / Kubernetes secrets
  Uniform API to access secrets from different stores

VALUE PROPOSITION:
  Same app code works on multiple clouds/infrastructure
  Infrastructure concerns (retry, mTLS, tracing) handled by Dapr sidecar
  Simplification vs. Istio: Dapr focuses on app-level building blocks;
  Istio focuses on network-level policies
  Can use both: Istio for network security, Dapr for app plumbing
```

---

## Common Confusion Points

**"AKS manages everything"**
AKS manages the control plane. You manage: node pools, pod resource limits, autoscaling configuration, security contexts, RBAC, ingress, storage classes, monitoring, certificate rotation. AKS reduces the infrastructure burden significantly but does not eliminate it.

**"Kubernetes is just for microservices"**
Kubernetes is a general container orchestration platform. It runs batch jobs (Job, CronJob), stateful applications (StatefulSet), daemon processes (DaemonSet), and event-driven workloads (KEDA). It is not exclusively a microservices platform.

**"APIM replaces the service mesh"**
APIM manages north-south traffic (external clients to internal services). Service mesh manages east-west traffic (service-to-service calls inside the cluster). They are different layers of the same architecture.

**"Event Grid is just pub/sub"**
Event Grid provides reactive routing of small events. It is not a message queue (no DLQ, no long retention) or a stream processor (no consumer groups, no offset tracking). Choose based on whether you need reactive routing (Event Grid), stream processing with replay (Event Hubs), or reliable business messaging (Service Bus).

---

## Decision Cheat Sheet

| Scenario | Azure Service |
|----------|--------------|
| Container orchestration (full control) | AKS |
| Containerized apps without cluster ops | Container Apps |
| External API gateway + developer portal | API Management |
| Service-to-service mTLS and traffic policies | Istio (AKS add-on) |
| React to Azure resource events | Event Grid |
| High-throughput telemetry/IoT streaming | Event Hubs |
| Reliable business process messaging | Service Bus |
| Cross-language microservice plumbing | Dapr |
| Multi-region HTTP routing + WAF + CDN | Azure Front Door |
