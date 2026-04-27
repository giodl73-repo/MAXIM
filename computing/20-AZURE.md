# 20 — Azure Services Map

## The Big Picture

```
Azure at a Glance — Service Categories
========================================

  ┌──────────────────────────────────────────────────────────────────────┐
  │  COMPUTE          CONTAINERS        SERVERLESS                       │
  │  Virtual Machines AKS               Functions                        │
  │  VM Scale Sets    Container Apps    Logic Apps                       │
  │  App Service      Container Inst.   Event Grid                       │
  ├──────────────────────────────────────────────────────────────────────┤
  │  STORAGE          DATABASES         MESSAGING                        │
  │  Blob Storage     Azure SQL         Service Bus                      │
  │  Files            Cosmos DB         Event Hubs                       │
  │  Disks            PostgreSQL        Storage Queues                   │
  │  Data Lake        Redis Cache       Event Grid                       │
  ├──────────────────────────────────────────────────────────────────────┤
  │  NETWORKING       SECURITY          IDENTITY                         │
  │  VNet             Key Vault         Entra ID (AAD)                   │
  │  Load Balancer    Defender          Managed Identity                 │
  │  App Gateway      DDoS Protection   RBAC                             │
  │  Front Door       Firewall          Conditional Access               │
  │  DNS              Sentinel                                           │
  ├──────────────────────────────────────────────────────────────────────┤
  │  DEVOPS           MONITORING        AI & ML                          │
  │  Azure DevOps     Monitor           OpenAI Service                   │
  │  Container Reg.   App Insights      AI Search                        │
  │  Bicep / ARM      Log Analytics     ML Studio                        │
  │  Chaos Studio     Workbooks         AI Foundry                       │
  └──────────────────────────────────────────────────────────────────────┘
```

```
How Services Nest in Practice
================================

  Internet → Front Door (global CDN + WAF)
               ↓
           App Gateway (regional LB + WAF)
               ↓
           AKS / App Service / Container Apps
               ↓
       ┌───────┴────────┐
   Azure SQL          Cosmos DB
   PostgreSQL         Redis Cache
       └────────────────┘
               ↓
           Key Vault   (secrets, certs)
           Entra ID    (auth/authz)
           Service Bus (async messaging)
               ↓
           Monitor + App Insights + Log Analytics
```

---

## The Delta: What Changed Since ~2014

You know the foundational services from the inside. What follows is a structured briefing on what's new, what was renamed, and what patterns flipped — the delta from ~2014 to 2026.

### New Services (didn't exist when you were hands-on)

```
Service                  GA      What It Is
══════════════════════════════════════════════════════════════════════

Azure Container Apps     2022    Serverless K8s abstraction. Scale to zero,
                                 built-in Dapr and KEDA. The sweet spot
                                 between App Service and AKS. Microsoft's
                                 preferred target for new microservices.

Azure OpenAI Service     2023    GPT-4o, o1, o3, DALL-E, Whisper — same
                                 models as OpenAI API, through Azure's
                                 infrastructure with private endpoints,
                                 Entra auth, and data residency.

Azure AI Foundry         2024    Unified platform for building AI apps:
(was AI Studio)                  model catalog, prompt flow, evaluations,
                                 fine-tuning, deployment. Superset of
                                 Azure ML for GenAI workloads.

Azure Arc                2020    Hybrid/multi-cloud control plane. Project
                                 Azure management (RBAC, Policy, Monitor)
                                 onto on-prem VMs, K8s clusters, and
                                 non-Azure clouds. Single pane of glass.

Flexible Server          2020    Managed Postgres and MySQL that replaced
(Postgres/MySQL)                 Single Server (now deprecated). Zone-
                                 redundant HA, built-in PgBouncer, VNet
                                 integration, pgvector extension support.

Azure AI Search          2023    Formerly Cognitive Search. Vector + hybrid
(formerly Cognitive)             search with integrated vectorization.
                                 The standard RAG retrieval layer on Azure.

Azure Chaos Studio       2021    First-party chaos engineering. Inject
                                 faults into VMs, AKS, SQL, networking.
                                 Game day tooling built into the portal.
```

### Rebrands and Renames

```
Old Name                        New Name                    When
══════════════════════════════════════════════════════════════════

Azure Active Directory (AAD)    Microsoft Entra ID          2023
VSTS                            Azure DevOps                2018
Azure Cognitive Search          Azure AI Search             2023
Azure ML Studio (classic)       Azure Machine Learning      2019
Azure Container Registry        Matured significantly —     ongoing
                                geo-replication, Tasks,
                                vulnerability scanning added
Azure Monitor                   Absorbed: Log Analytics,    2019–2022
                                App Insights, Metrics,
                                Alerts, Workbooks
```

### Pattern Changes (the stuff that matters most)

```
Old Pattern (pre-2019)                 New Default (2024)
══════════════════════                 ══════════════════

Auth: Service Principal +              Managed Identity
      client secret in KeyVault        No credentials to manage.
      Rotate every 90 days.            System-assigned (tied to resource
      Leak risk on every rotation.     lifecycle) or User-assigned
                                       (shared, persists independently).

IaC: ARM JSON templates                Bicep
     Verbose, painful to read.         Same ARM model underneath.
     Error messages reference          First-class VS Code support.
     internal resource IDs.            Modules, loops, conditions.
                                       Compiles to ARM.

App Environment:                       App Service Environment v3
ASEv1 / ASEv2                          (ASEv3). Zone redundancy,
                                       better scaling, lower base cost.

Compute default:                       Container Apps for new
VMs or App Service                     microservices; AKS for complex
                                       K8s workloads.

Network access to PaaS:                Private Endpoint
Service Endpoint (traffic on           Service gets a private IP inside
MS backbone but service                your VNet. Truly private.
retains public IP)                     Use Private Endpoint by default
                                       for SQL, Blob, Key Vault, etc.

Cost commitment:                       Azure Savings Plans (2022)
Reserved Instances only                Flexible across compute types,
(VM-specific commitment)               not tied to a specific VM SKU.
                                       Reserved Instances still valid
                                       for predictable VM workloads.
```

---

## Compute

### Virtual Machines

The VM series naming table is useful reference — generations have evolved. Current-gen is v5/v6 depending on series. For new workloads, evaluate Container Apps or AKS first; VMs are now primarily for legacy lift-and-shift, specialized hardware requirements, or workloads that need full OS control.

```
VM Series (the naming makes sense once you know it)
====================================================

  B-series     Burstable — cheap, for dev/test, not sustained load
  D-series     General purpose — balanced CPU/memory (most apps)
  E-series     Memory optimized — databases, in-memory analytics
  F-series     Compute optimized — CPU-heavy workloads
  N-series     GPU — ML training, rendering, HPC
  M-series     Massive memory — SAP HANA, very large DBs

  v3, v4, v5 suffix = hardware generation (newer = faster/cheaper)
  s suffix = Premium SSD support (e.g. D4s_v5)
  a suffix = AMD CPU (cheaper, similar perf)

  Standard_D4s_v5 = General purpose, 4 vCPUs, 16 GB RAM, v5 gen, Premium SSD
```

```
VM vs App Service vs AKS
=========================

  VM                     App Service              AKS
  ══                     ═══════════              ═══
  You manage OS          Microsoft manages OS     You manage workloads
  You patch              Auto-patching            Microsoft manages control plane
  Full control           Limited control          Full K8s control
  Any workload           Web apps / APIs          Containerized workloads
  Expensive at scale     Simple scaling           Complex but powerful
  Good for: legacy       Good for: web apps       Good for: microservices
  lift-and-shift         without containers       at scale
```

### App Service

The deployment slots model and the tier hierarchy are still current. Premium v3 (P0v3–P3v3) is the recommended production tier — Ev3-based hardware, better VNet integration, zone redundancy support. Isolated v2 (I1v2–I3v2) replaced ASEv2.

```
App Service Hierarchy
======================

  App Service Plan (the VM underneath)
  ├── Web App 1 (your Node.js API)
  ├── Web App 2 (your React SSR app)
  └── Function App (shares the plan)

  Plan SKUs:
    F1 / B1    Free / Basic — dev/test only
    S1-S3      Standard — production, autoscale, slots
    P1v3-P3v3  Premium v3 — better perf, VNet integration
    I1v2-I3v2  Isolated — dedicated infra (compliance)

  Deployment Slots:
    Production slot  (live traffic)
    Staging slot     (deploy here, test, then swap)
    Swap = instant traffic cut-over + rollback capability
```

```bash
# Deploy to App Service
az webapp up --name myapp --resource-group myRG --runtime "NODE:20-lts"

# Deploy container
az webapp config container set \
  --name myapp \
  --resource-group myRG \
  --container-image-name myregistry.azurecr.io/myapp:v1.2

# Slot swap
az webapp deployment slot swap \
  --name myapp --resource-group myRG \
  --slot staging --target-slot production
```

### Azure Kubernetes Service (AKS)

Managed Kubernetes. Control plane is free; you pay for nodes. Covered deeply in 12-KUBERNETES.md — key Azure specifics here.

```
AKS Key Integrations
=====================

  ACR pull          Attach registry → nodes pull private images automatically
  Managed Identity  Workload Identity → pods get Azure RBAC, no stored secrets
  Azure Monitor     Container Insights → node/pod metrics + logs auto-collected
  AGIC              Application Gateway as K8s Ingress Controller
  Azure CNI         VNet-native pod IPs (pods are first-class VNet citizens)
  AAD integration   K8s RBAC tied to Entra ID groups
  Node pools        Mix CPU/GPU/spot VMs in one cluster
  Virtual Nodes     Serverless burst capacity via ACI
```

### Azure Container Apps (ACA)

The sweet spot between App Service (too simple) and AKS (too complex). Serverless containers with built-in Dapr, KEDA scaling, and service discovery.

```
ACA vs AKS
===========

  ACA                              AKS
  ═══                              ═══
  Serverless (scale to zero)       Always-on nodes
  No cluster management            Full K8s control
  Built-in Dapr, KEDA              DIY everything
  HTTP + event-driven scaling      Any scaling
  Good for: APIs, workers,         Good for: complex workloads,
  microservices, scale-to-zero     specialized requirements,
                                   existing K8s expertise
```

```bash
az containerapp create \
  --name myapi \
  --resource-group myRG \
  --environment myEnv \
  --image myregistry.azurecr.io/myapi:latest \
  --target-port 3000 \
  --ingress external \
  --min-replicas 0 \
  --max-replicas 10 \
  --scale-rule-name http-rule \
  --scale-rule-type http \
  --scale-rule-http-concurrency 100
```

### Azure Functions

Event-driven serverless compute. Pay per execution. Scale to zero.

```
Trigger Types
==============

  HTTP trigger         → REST API endpoint
  Timer trigger        → cron job (0 */5 * * * * = every 5 min)
  Queue trigger        → process Service Bus / Storage Queue messages
  Event Hub trigger    → process Kafka-compatible stream
  Blob trigger         → react to file upload
  Cosmos DB trigger    → react to DB change feed
  SignalR              → push real-time to browser clients
```

```typescript
// HTTP trigger (Node.js)
import { app, HttpRequest, HttpResponseInit, InvocationContext } from "@azure/functions";

app.http("getOrder", {
  methods: ["GET"],
  authLevel: "anonymous",
  route: "orders/{id}",
  handler: async (req: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> => {
    const id = req.params.id;
    const order = await db.orders.findById(id);
    if (!order) return { status: 404, jsonBody: { error: "not found" } };
    return { jsonBody: order };
  },
});
```

```
Hosting Plans
==============

  Consumption   Scale to zero. Pay per execution. 5-min timeout limit.
                Cold start latency. Good for: infrequent/bursty workloads.

  Premium       Pre-warmed instances (no cold start). VNet integration.
                Good for: latency-sensitive, private network access.

  Dedicated     Runs on App Service Plan. Predictable cost.
                Good for: always-on with existing App Service.

  Container     Functions in a custom container. Full control.
```

---

## Storage

### Blob Storage

The tier structure, lifecycle policies, and ADLS Gen2 are the post-2014 additions worth knowing.

```
Blob Storage Tiers
===================

  Hot     Frequently accessed. Higher storage cost, low access cost.
  Cool    Infrequently accessed (30+ days). Lower storage cost.
  Cold    Rarely accessed (90+ days). Very low storage cost.    ← added ~2023
  Archive Rarely accessed (180+ days). Lowest cost. Hours to rehydrate.

  Lifecycle policies: auto-tier blobs as they age
  → uploaded as Hot, auto-moves to Cool after 30 days, Archive after 180

Storage Account → Container → Blob

  Container = folder (flat, no real hierarchy — / in name is cosmetic)
  Blob types:
    Block blob   — files (most common: images, videos, documents)
    Append blob  — log files (append-only, efficient)
    Page blob    — VHD files (VM disks)
```

**Data Lake Storage Gen2.** Enable hierarchical namespace on a standard Blob Storage account and it becomes ADLS Gen2 — real directory semantics, atomic rename, POSIX-style ACLs. This is the current storage layer for ADF pipelines and Synapse Analytics; the Gen1 → Gen2 migration is complete for most teams. The convergence means you're not choosing between object storage and a data lake anymore — one account serves both patterns depending on whether HNS is enabled. ADF connectors treat ADLS Gen2 as a first-class source/sink with partition discovery and format inference.

**Immutability policies.** WORM (Write Once Read Many) support via time-based retention or legal hold. Required for SEC 17a-4 compliance scenarios.

```bash
# Upload
az storage blob upload \
  --account-name mystorage \
  --container-name images \
  --name profile/user123.jpg \
  --file ./local-image.jpg \
  --auth-mode login

# Generate SAS URL (time-limited access)
az storage blob generate-sas \
  --account-name mystorage \
  --container-name images \
  --name profile/user123.jpg \
  --permissions r \
  --expiry 2026-03-01T00:00:00Z
```

### Azure Files

Managed SMB / NFS file shares. Mount as a network drive on VMs or containers.

```
When to use Azure Files vs Blob
=================================

  Azure Files                        Blob Storage
  ═══════════                        ════════════
  SMB/NFS mount (like a share)       REST API / SDK access
  Lift-and-shift shared drives       New apps, web assets
  Legacy apps expecting file path    CDN-servable content
  Container persistent volumes       Object storage at scale
  \\server\share equivalent          s3-compatible workflows
```

### Azure Disk Storage

Block storage for VM OS and data disks.

```
Disk Types
===========

  Standard HDD    Dev/test, backup. Cheapest.
  Standard SSD    Web servers, light production.
  Premium SSD     Production databases, I/O intensive.
  Ultra Disk      Highest IOPS/throughput. SAP, SQL Server.
```

---

## Databases

### Azure SQL Database

The post-2014 additions are the interesting parts: Hyperscale, Serverless tier, and Ledger.

```
Azure SQL Family
=================

  Azure SQL Database        Single database. Serverless or provisioned.
  Azure SQL Managed Inst.   Near 100% SQL Server compat. Lift-and-shift.
  SQL Server on VM          Full SQL Server on a VM. Complete control.

  DTU vs vCore pricing:
    DTU    — bundled CPU/memory/IO unit. Simpler. Less control.
    vCore  — choose CPU + memory separately. Easier to size.
             Can use Azure Hybrid Benefit (existing SQL Server license).
```

```
Post-2014 Additions
====================

  Hyperscale tier:
    Log-based architecture with distributed storage layer.
    Scales to 100 TB. Compute and storage scale independently.
    Near-instant backup (log snapshot, not full copy).
    Near-instant restore — reads from the distributed log, not a backup file.
    Read replicas spin up in minutes. Named replica feature for workload isolation.

  Serverless tier:
    Auto-pauses after inactivity (dev/test use case)
    Scales compute automatically 0.5–40 vCores
    Pay only when active — per-second billing during active periods
    Resume latency: ~15s on first connection after auto-pause

  Elastic Pools:
    Share compute across multiple databases.
    Right-size when databases have non-overlapping peak times.
    Per-pool pricing, not per-database.

  Ledger tables (2021):
    Tamper-evident audit trail built into the table.
    Cryptographically verifiable history — SHA-256 hash chain.
    No separate audit log to trust. The table itself is the evidence.
    Append-only ledger tables vs updatable ledger tables.
```

### Azure Database for PostgreSQL

Managed Postgres. Flexible Server is the current option (Single Server is deprecated).

```
Flexible Server
================

  Fully managed Postgres 11–16
  Zone-redundant HA (primary + standby in different zones)
  Read replicas for scale-out reads
  Point-in-time restore (up to 35 days)
  VNet integration (private endpoint)
  Burstable / General Purpose / Memory Optimized compute tiers

  Connection pooling: built-in PgBouncer (enable in portal)
  Extensions: pgvector, PostGIS, uuid-ossp all available
```

### Cosmos DB

Microsoft's globally distributed, multi-model NoSQL database. The key pitch: single-digit millisecond reads anywhere in the world, multiple consistency levels.

```
Cosmos DB APIs (one engine, multiple interfaces)
=================================================

  NoSQL (Core)   JSON documents. Native. Most features.
  MongoDB        Wire-compatible with MongoDB drivers
  Cassandra      Wide-column. Cassandra CQL compatible.
  Gremlin        Graph database
  Table          Key-value. Azure Table Storage compatible.
  PostgreSQL     Distributed Postgres (Citus)

  Pick NoSQL API for new projects unless you're migrating.
```

```
Consistency Levels (the spectrum)
===================================

  Strong          Linearizable. Reads always see latest write.
                  Highest latency. Lowest availability.

  Bounded Staleness  Reads lag behind writes by K versions or T time.

  Session         Default. Within a session: read your own writes.
                  Across sessions: eventual.

  Consistent Prefix  Reads never see out-of-order writes.

  Eventual        Lowest latency. Highest availability.
                  Reads might return stale data.

  Most apps: Session consistency is the right default.
```

```
Partitioning
=============

  Every container has a partition key (e.g., /customerId)
  All items with the same partition key → same logical partition
  Logical partitions → physical partitions (transparent)

  Hot partition = one customer generates 90% of traffic
                = performance cliff, hard to fix after design
  Good partition key: high cardinality, even distribution
```

### Azure Cache for Redis

Managed Redis. Sub-millisecond in-memory data store.

```
Use Cases
==========

  Session store         Store JWT sessions, user state
  Cache-aside           Cache DB query results, API responses
  Rate limiting         Sliding window counters per user/IP
  Pub/Sub               Lightweight messaging between services
  Leaderboards          Sorted sets for rankings
  Distributed locks     SETNX pattern for concurrency

  Tiers:
    Basic   — single node, dev/test
    Standard — primary + replica, 99.9% SLA
    Premium — clustering, persistence, VNet, geo-replication
    Enterprise — Redis Stack (search, JSON, time series)
```

---

## Messaging

### Azure Service Bus

Enterprise messaging: queues and topics. Guaranteed delivery, ordering, dead-lettering, transactions.

```
Queue vs Topic
===============

  Queue                              Topic + Subscriptions
  ═════                              ════════════════════
  One sender → one receiver          One sender → many receivers
  Competing consumers                Each subscription gets all messages
  Work distribution                  Fan-out / pub-sub

  Service Bus Queue    →   Dead-letter queue (failed messages)
                       →   Scheduled messages (deliver at time)
                       →   Message sessions (ordered processing)
                       →   Transactions (atomic send/receive)

  vs Azure Storage Queue:
    Storage Queue: simple, cheap, 64KB msg limit, 7-day TTL
    Service Bus:   enterprise, 256KB-100MB, long TTL, ordering, DLQ
```

### Azure Event Hubs

High-throughput event streaming. Kafka-compatible. The Azure equivalent of Kafka.

```
Event Hubs vs Service Bus
==========================

  Event Hubs                         Service Bus
  ══════════                         ═══════════
  Streaming (telemetry, logs)        Messaging (commands, events)
  Millions of events/sec             Thousands/sec
  Retention: 1–90 days               Retention: until consumed
  Consumer groups (like Kafka)       Competing consumers (queues)
  Kafka protocol compatible          AMQP / HTTP
  Good for: IoT, clickstreams,       Good for: order processing,
  analytics, audit logs              reliable workflows

  Event Hubs is Kafka.
  If your code uses Kafka client libraries, point at Event Hubs endpoint.
```

### Azure Event Grid

Reactive eventing. React to Azure resource changes or publish custom events.

```
Event Grid
===========

  Sources:                           Handlers:
  ════════                           ════════
  Azure Blob (file uploaded)    →    Azure Functions
  Azure SQL (record changed)    →    Logic Apps
  Container Registry (image)    →    Event Hubs
  Custom topics (your events)   →    Service Bus
  Azure subscription events     →    Webhooks

  Push model (not pull like Service Bus/Event Hubs)
  Near real-time (<1s latency)
  Good for: triggering reactions to events across Azure services
  Not for: high-throughput streams or guaranteed-once processing
```

---

## Networking

### Virtual Network (VNet)

The core VNet model (subnets, NSGs, peering, VPN Gateway, ExpressRoute) is unchanged from the architecture you know. The material delta: Private Endpoint, Virtual WAN, and Azure Firewall Premium.

```
VNet Concepts
==============

  VNet: 10.0.0.0/16 (your CIDR block)
  ├── Subnet: 10.0.1.0/24  (web tier)
  ├── Subnet: 10.0.2.0/24  (app tier)
  └── Subnet: 10.0.3.0/24  (data tier)

  NSG (Network Security Group): firewall rules on subnet/NIC
    Inbound: allow port 443 from internet, deny everything else
    Outbound: allow port 5432 to DB subnet only

  VNet Peering: connect two VNets (same or different regions)
  VPN Gateway: connect on-premises network to Azure VNet
  ExpressRoute: dedicated private circuit to Azure (not over internet)
  Private Endpoint: bring an Azure service (Blob, SQL) into your VNet
                    → service gets a private IP in your subnet
                    → traffic never leaves Microsoft network
```

**Private Endpoint vs Service Endpoint.**
Service Endpoint was the first attempt: traffic to the PaaS service is routed on the Microsoft backbone (not the public internet) but the service retains its public IP. You're restricting traffic source, not eliminating the public surface. Private Endpoint (2019) is qualitatively different: the PaaS service gets a private NIC with a private IP inside your VNet. The public endpoint can be disabled entirely. Traffic is fully private; DNS resolves to the private IP via Private DNS Zone. For SQL, Key Vault, Blob, and similar services, Private Endpoint is now the default recommendation in regulated or security-sensitive environments.

**Azure Virtual WAN.** Hub-and-spoke networking at scale — managed by Microsoft. Replaces the DIY pattern of peering dozens of VNets through a transit hub. Virtual WAN automates peering, routing, and gateway connectivity. Worth evaluating when you're managing more than ~10 VNets or need automated any-to-any connectivity across regions.

**Azure Firewall Premium vs NSG.**
NSGs are stateful L4 packet filters on subnets/NICs — the right tool for controlling intra-VNet traffic. Azure Firewall is a managed, stateful L7 firewall at the VNet boundary — FQDN filtering, TLS inspection, threat intelligence. The decision: NSGs handle east-west (service to service within VNet); Azure Firewall handles north-south (internet egress, cross-VNet, forced tunneling) and scenarios requiring application-layer inspection.

---

## Security & Identity

### Key Vault

The right place for secrets, certificates, and encryption keys. Nothing sensitive in code or config files.

```
Key Vault stores:
  Secrets      → connection strings, API keys, passwords
  Keys         → RSA/EC keys for encryption (HSM-backed option)
  Certificates → TLS certs, auto-renewal via DigiCert/Let's Encrypt

Access pattern (the right way):
  App has Managed Identity
    → assigned Key Vault Secrets User role
    → fetches secret at startup
    → no secret in code, config, or environment variable

  az keyvault secret show --vault-name myVault --name DatabaseUrl
```

### Managed Identity

**This replaced service principals + client secrets as the default Azure-to-Azure auth pattern.**

The old pattern (pre-2019 standard):
```
1. Create Service Principal in AAD
2. Generate client secret (or certificate)
3. Store secret in Key Vault (or worse, app config)
4. App retrieves secret at runtime → exchanges for access token
5. Set a calendar reminder: rotate secret every 90 days
6. Miss the rotation → service outage or security incident
```

The new pattern (Managed Identity):
```
1. Enable Managed Identity on the resource (checkbox in portal / one CLI flag)
2. Assign an RBAC role: az role assignment create \
     --assignee <managed-identity-client-id> \
     --role "Storage Blob Data Reader" \
     --scope /subscriptions/.../storageAccounts/mystorage
3. App calls Azure service — Azure handles token exchange transparently
4. No secret. No rotation. No leak surface.
```

```
System-assigned vs User-assigned
==================================

  System-assigned                    User-assigned
  ══════════════                     ════════════
  Tied to resource lifecycle         Standalone resource
  Deleted when resource is deleted   Persists independently
  One identity per resource          Assign to multiple resources
  Good for: single-purpose           Good for: shared identity across
  resources                          fleet of identical services

  Both: no credentials to manage
  Both: identity visible in Entra ID as a service principal
  Both: RBAC roles assigned like any other principal
```

```
Supported by:
  VMs, VM Scale Sets
  App Service, Functions
  AKS pods (via Workload Identity extension — OIDC federation)
  Container Apps
  Logic Apps
  Azure Data Factory
```

The one remaining use case for service principals: external systems (CI/CD runners, on-prem services) that need to call Azure but can't use Managed Identity because they're not Azure resources. In that case: use a service principal with a federated credential (OIDC) rather than a client secret — GitHub Actions, Azure DevOps, and most CI systems support this, eliminating the secret rotation problem even for external callers.

### Entra ID (formerly Azure Active Directory)

Microsoft's cloud identity platform. B2B (employee auth), B2C (customer auth), and machine-to-machine auth.

```
Key Concepts
=============

  Tenant         Your organization's Entra directory
  App Reg.       Register an app to get client_id + configure permissions
  Service Princ. The identity a registered app gets in a tenant
  Managed Id.    Auto-managed service principal for Azure resources
  RBAC           Role assignments: who can do what on which resource
  Conditional    MFA, location, device compliance requirements on sign-in
  Access

  OAuth2 / OIDC flows (see 10-AUTH.md):
    Auth Code + PKCE → SPA / mobile
    Client Credentials → service-to-service (no user)
    On-Behalf-Of → API calling downstream API on user's behalf
```

---

## DevOps & Management

### Azure Container Registry (ACR)

Private Docker registry. Geo-replication, vulnerability scanning, build tasks.

```
ACR Features
=============

  Geo-replication    Mirror registry to multiple regions (pull from nearest)
  Tasks              Build images in ACR on git push (no local Docker needed)
  Vulnerability scan Defender for Containers scans images on push
  Retention policy   Auto-delete old untagged images
  Token auth         Fine-grained access per repository

az acr build --registry myregistry --image myapp:latest .
# Builds in the cloud, no Docker daemon needed locally
```

### Azure Monitor (recap from 15-OBSERVABILITY.md)

```
Monitor Stack
==============

  Data sources → Log Analytics Workspace → Grafana / Workbooks / Alerts

  Application Insights   APM: requests, dependencies, exceptions, traces
  Container Insights     AKS pod/node metrics + stdout logs
  VM Insights            VM performance + dependencies map
  Azure Monitor Metrics  Platform metrics (built-in, 93-day retention)
  Azure Monitor Logs     Log Analytics: KQL query against all log sources
  Alerts                 Metric/log/activity alerts → Action Groups
  Action Groups          Email, SMS, webhook, ITSM, PagerDuty, Logic App
```

### Azure DevOps

You built VSTS. Here's the delta since the 2018 rebrand.

**What changed:**

- **Services are now independently usable.** Boards, Repos, Pipelines, Artifacts, and Test Plans can each be enabled or disabled per organization. A team can use ADO Boards for work tracking while hosting code on GitHub. Artifacts can be used as a NuGet/npm feed without using Pipelines.

- **YAML pipelines replaced classic GUI pipelines.** The drag-and-drop pipeline editor still exists but YAML is the recommended approach for everything new. Pipelines-as-code: versioned with the repo, reviewable in PRs, reusable via templates. Classic pipelines are in maintenance mode — no new features.

- **GitHub coexistence.** Microsoft acquired GitHub in 2018. The current positioning: GitHub for open-source and developer-centric workflows (Actions, Codespaces, Copilot); ADO for enterprise teams that need Boards-centric planning, Test Plans, or Artifacts. Many teams run hybrid: GitHub for code + GitHub Actions for CI, ADO Boards for sprint planning. The Boards ↔ GitHub integration (link commits/PRs to work items) makes this practical.

- **Azure DevOps Server** (on-prem) is still actively maintained for regulated industries that can't use the cloud service. Feature parity lags the cloud service by roughly one release cycle.

```
ADO Services
=============

  Boards      Agile planning (epics, stories, tasks, sprints)
              Azure Boards ↔ GitHub Issues integration
  Repos       Git hosting (or use GitHub + connect)
  Pipelines   CI/CD (YAML — use this; classic GUI is legacy)
  Test Plans  Manual test case management + exploratory testing
  Artifacts   NuGet, npm, Maven, Python feed hosting
              Upstream sources: proxy public feeds through your feed
```

```
GitHub vs ADO — when to use which
====================================

  GitHub Actions                     Azure Pipelines (YAML)
  ══════════════                     ══════════════════════
  Simpler syntax                     More mature enterprise features
  Marketplace: 20k+ actions          Templates + task library
  Free for public repos              Better compliance audit trails
  Copilot integration                Test Plans integration
  Better for: OSS, greenfield,       Better for: regulated industries,
  developer-centric teams            large enterprises, ADO Boards users

  Both → GitHub for code + ADO Boards for work tracking is a common
  and well-supported hybrid pattern.
```

---

## AI Services

### Azure OpenAI Service

Access to GPT-4o, o1, o3, DALL-E, Whisper, etc. through Azure's infrastructure. Same models as OpenAI, with Azure compliance, private networking, and data residency.

```
Azure OpenAI vs OpenAI API
===========================

  Azure OpenAI                       OpenAI API
  ════════════                       ══════════
  Data stays in your Azure region    Data processed by OpenAI
  Private endpoint (no public net)   Public API
  Azure RBAC + Entra auth            API key auth only
  Content filtering configurable     Content filtering configurable
  Enterprise SLA + support           Consumer SLA
  Same models (GPT-4o, etc.)         Same models

  For enterprise / regulated → Azure OpenAI
  For prototyping / personal → OpenAI API directly
```

```typescript
import { AzureOpenAI } from "openai";
import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";

const credential = new DefaultAzureCredential();   // Managed Identity
const azureADTokenProvider = getBearerTokenProvider(
  credential, "https://cognitiveservices.azure.com/.default"
);

const client = new AzureOpenAI({
  azureADTokenProvider,
  endpoint: process.env.AZURE_OPENAI_ENDPOINT,
  apiVersion: "2024-10-21",
  deployment: "gpt-4o",
});

const response = await client.chat.completions.create({
  messages: [{ role: "user", content: "Explain AKS in one paragraph." }],
  model: "gpt-4o",
});
```

### Azure AI Search

Enterprise search with vector, full-text, and hybrid search. The standard retrieval layer for RAG (retrieval-augmented generation) on Azure.

```
AI Search Capabilities
=======================

  Full-text search    BM25 ranking, linguistic analysis, faceting
  Vector search       Embed + search by semantic similarity
  Hybrid search       Combine keyword + vector (RRF fusion) — best accuracy
  Semantic ranking    LLM reranking of top results
  Integrated vectorization  Auto-embed on document ingestion (AOAI embeddings)
  Skillsets           Cognitive enrichment pipeline: OCR, entity extraction, etc.

  Typical RAG pattern on Azure:
    Documents → Blob Storage
             → AI Search indexer (chunking + embedding)
             → Index (vectors + text)
    Query → Embed query → Hybrid search → Top K chunks
          → AOAI GPT-4o → Grounded response
```

---

## Pricing Mental Models

```
Key concepts that affect every bill
=====================================

  Reserved Instances    Commit 1 or 3 years → up to 72% off vs pay-as-you-go
                        Worth it for steady-state production workloads.
                        VM-SKU specific commitment.

  Azure Savings Plans   Commit to $/hour spend (not a specific SKU).
  (2022)                Applies across compute types (VMs, ACI, Functions).
                        More flexible than Reserved Instances.
                        Lower discount ceiling (~65%) vs RIs (~72%) for VMs.
                        Right tool when your compute mix varies.

  Spot VMs              Unused capacity at 60–90% discount.
                        Can be evicted with 30s notice.
                        Good for: batch jobs, dev/test, stateless workers.

  Azure Hybrid Benefit  Bring existing Windows Server / SQL Server licenses.
                        Can halve the compute cost of SQL databases.

  Dev/Test pricing      MSDN / Visual Studio subscribers get significantly
                        discounted rates on most compute.
                        Not for production — check the terms.

  Egress costs          Data leaving Azure costs money.
                        Data between regions: costs money.
                        Data between VNet resources same region: free.
                        CDN (Front Door) reduces egress by caching at edge.

  Cost Management       Always set a budget alert.
                        Tag resources with environment/team/project.
                        Azure Advisor gives cost recommendations.
```

---

## Common Confusion Points

**App Service vs Container Apps vs AKS vs Functions.**
The most common "which one?" question. Rule of thumb: stateless web app with no container expertise → App Service. Containerized microservices that need to scale to zero → Container Apps. Complex workloads needing full K8s control → AKS. Event-triggered short-lived execution → Functions.

**Service Bus vs Event Hubs vs Event Grid.**
Service Bus = reliable message delivery for workflows (queue/topic). Event Hubs = high-throughput streaming, Kafka-compatible. Event Grid = reactive eventing, push-based reactions to Azure resource changes. All three solve different problems; they're often used together.

**Azure AD is now Entra ID.**
Microsoft rebranded Azure Active Directory to Microsoft Entra ID in 2023. Same product. Docs are still mixed. Azure AD = Entra ID.

**Cosmos DB consistency levels are not what you expect.**
"Session" is not eventual. It guarantees you read your own writes within your session — which is what most apps actually need. Default to Session; only drop to Eventual if you have a specific throughput/latency reason.

**Managed Identity vs Service Principal vs App Registration.**
App Registration = register the application identity in Entra. Service Principal = the instance of that registration in your tenant. Managed Identity = a special service principal auto-managed by Azure, no credentials to handle. For Azure-to-Azure auth: always Managed Identity. For external apps calling Azure: App Registration + Service Principal, preferably with federated credentials (OIDC) rather than client secrets.

**Private Endpoint vs Service Endpoint.**
Service Endpoint: traffic stays on Microsoft backbone but the service still has a public IP. Private Endpoint: the service gets a private IP inside your VNet — truly private, no public IP path. Use Private Endpoint for sensitive services.

**ARM vs Bicep.**
Bicep is not a replacement for ARM — it compiles to ARM. Same resource model, same deployment engine, same portal visibility. Bicep is syntactic sugar that makes ARM authoring tractable. If you have existing ARM templates, they work as-is; migrate to Bicep incrementally using `az bicep decompile`.

---

## Decision Cheat Sheet

| I want to run... | Use |
|---|---|
| A web app / API, no containers | App Service |
| Containers, scale to zero | Azure Container Apps |
| K8s workloads with full control | AKS |
| Short event-triggered functions | Azure Functions |
| Legacy app on a VM | Azure Virtual Machines |
| Object storage (files, images, backups) | Blob Storage |
| Shared file system for VMs | Azure Files |
| SQL Server workloads | Azure SQL Database / SQL Managed Instance |
| Postgres | Azure Database for PostgreSQL Flexible Server |
| Global, low-latency NoSQL | Cosmos DB |
| Session cache / rate limiting / pub-sub | Azure Cache for Redis |
| Reliable messaging, queues, pub-sub | Azure Service Bus |
| High-throughput event streaming (Kafka) | Azure Event Hubs |
| Trigger reactions to Azure resource events | Azure Event Grid |
| Secrets, keys, certificates | Azure Key Vault |
| Azure-to-Azure auth without credentials | Managed Identity |
| Employee / B2B identity | Entra ID (corporate tenant) |
| Customer identity (B2C) | Entra External ID |
| Private Docker registry | Azure Container Registry |
| Global HTTP routing + CDN + WAF | Azure Front Door |
| Regional HTTP routing + WAF | Application Gateway |
| GPT-4o / o1 in Azure with private networking | Azure OpenAI Service |
| Semantic / hybrid search for RAG | Azure AI Search |
| Cost savings on steady workloads | Reserved Instances or Savings Plans |
| Cost savings on existing SQL licenses | Azure Hybrid Benefit |
| Hybrid / multi-cloud unified management | Azure Arc |
| IaC for Azure resources | Bicep (compiles to ARM) |
