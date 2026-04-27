# Cloud Models: IaaS/PaaS/SaaS/FaaS, Shared Responsibility, Deployment Models

## The Big Picture

The cloud service model spectrum defines how much of the stack you manage vs. what the cloud provider manages.

```
CLOUD SERVICE MODEL SPECTRUM
+-----------------------------------------------------------------------+
|                                                                       |
  Stack from top to bottom:
    App, Data, Runtime, OS, VM, Hardware, Datacenter, Network, Storage.

  ON-PREMISES:   You manage everything.
  IaaS:          You manage App + Data + Runtime + OS.
                 Cloud manages VM + HW + DC + Network + Storage.
  PaaS:          You manage App + Data.
                 Cloud manages everything below.
  CaaS:          You manage container images.
                 Cloud manages the cluster.
  FaaS:          You manage function code only.
                 Cloud manages everything else.
  SaaS:          You use the application; cloud manages everything.

  EXAMPLES:
    IaaS:   Azure VM, Amazon EC2, GCP Compute Engine
    PaaS:   Azure App Service, Azure SQL, Google App Engine
    CaaS:   AKS, Amazon EKS, Google GKE
    FaaS:   Azure Functions, AWS Lambda, Cloud Functions
    SaaS:   Microsoft 365, Salesforce, GitHub
```

---

## Shared Responsibility Model

The shared responsibility model defines who is accountable for security at each layer. In many security breaches, the root cause is the customer's failure to meet their responsibilities (misconfiguration, unpatched code, weak credentials).

```
SHARED RESPONSIBILITY BY SERVICE TYPE

LAYER                 | ON-PREM | IaaS   | PaaS   | SaaS
----------------------|---------|--------|--------|-------
Data                  | You     | You    | You    | You
Identity & Access     | You     | You    | You    | You
Applications          | You     | You    | You    | Cloud
Operating System      | You     | You    | Cloud  | Cloud
Network Controls      | You     | You    | Cloud  | Cloud
Physical Hosts        | You     | Cloud  | Cloud  | Cloud
Physical Network      | You     | Cloud  | Cloud  | Cloud
Physical Datacenter   | You     | Cloud  | Cloud  | Cloud

"You" = Customer responsibility
"Cloud" = Cloud provider responsibility

ALWAYS YOUR RESPONSIBILITY (in any cloud model):
  - Data classification and protection
  - Identity (who has access, how they authenticate)
  - Application code security (OWASP Top 10, your bugs)
  - Access control configuration (who has access to what)
  - Endpoint security (devices accessing your cloud resources)

COMMON CUSTOMER FAILURES:
  Storage account set to public: misconfigured, not provider failure
  Weak passwords on VM admin: customer failure
  SQL database open to 0.0.0.0/0: customer NSG misconfiguration
  Outdated container base image: customer responsibility to update
  Secrets in application code: customer failure
```

---

## IaaS: Infrastructure as a Service

You get raw compute, storage, and networking. You manage everything above the hypervisor.

```
AZURE IaaS COMPONENTS

VIRTUAL MACHINES:
  Sizes: D-series (general), E-series (memory-optimized),
         F-series (compute-optimized), N-series (GPU),
         B-series (burstable/cheap)
  SLA: 99.9% single VM with Premium SSD
       99.95% with Availability Set (2+ VMs in different fault domains)
       99.99% with Availability Zones (2+ VMs in different zones)

VIRTUAL MACHINE SCALE SETS (VMSS):
  Group of identical VMs with autoscaling
  Manual, scheduled, or metric-based scaling
  Load balancer distributes traffic
  Rolling upgrades: update 20% at a time

STORAGE (Managed Disks):
  HDD (Standard): cheap, high-latency, backup/archival
  SSD (Standard): balanced cost/perf
  SSD (Premium): low-latency, production databases
  SSD (Ultra): extreme IOPS (10k-160k), mission-critical latency

NETWORKING:
  Virtual Network (VNet): your private network space
  Network Interface: binds VM to VNet/subnet
  Public IP: optional; assign when direct internet access needed
  NSG: stateful firewall rules per NIC or subnet
```

**When IaaS is right**: Legacy applications that cannot be containerized, licensed software requiring specific OS configuration, workloads with unusual hardware requirements (GPU, InfiniBand), applications needing OS-level configuration.

---

## PaaS: Platform as a Service

You deploy application code. The platform manages OS, runtime, scaling, patching.

```
AZURE PAAS EXAMPLES

AZURE APP SERVICE:
  Deploy web apps (ASP.NET, Node, Python, Java, PHP, Ruby)
  SKUs: Free, Shared, Basic, Standard, Premium, Isolated
  Built-in: custom domain + SSL, deployment slots (staging),
            autoscaling, Azure AD auth, deployment from GitHub/ADO
  App Service Plan: the underlying VM pool (scale up/out the plan)
  One plan → multiple apps (cost sharing)

AZURE SQL DATABASE:
  Managed SQL Server (PaaS): automatic patching, backup, HA
  vCore model: General Purpose, Business Critical, Hyperscale
  Business Critical: in-memory OLTP, local SSD, replicated
  Hyperscale: up to 100TB, fast snapshot backups, read scale-out
  DTU model: legacy, pre-bundled compute+I/O units
  Elastic Pool: multiple DBs share a pool of DTUs or vCores
    → Good for SaaS multi-tenant where DBs have uneven load

AZURE CACHE FOR REDIS:
  Managed Redis cluster with HA (replication, failover)
  C0-C6: basic cache sizes; P-tiers: Premium with cluster/geo-replication
  Used for: session cache, distributed cache, Pub/Sub, rate limiting
```

---

## CaaS: Containers as a Service

You provide container images. The platform manages the container runtime, scheduling, and networking.

```
AKS (Azure Kubernetes Service):
  Azure manages: control plane (API server, etcd, scheduler, controllers)
    → Free (you pay only for agent nodes)
  You manage: node pools, workload deployment, RBAC
  Integration: Azure AD auth, Azure CNI networking, Azure Monitor, ACR

AZURE CONTAINER APPS:
  Serverless containers (no cluster management)
  Based on Kubernetes + KEDA (event-driven autoscaling)
  Scale to zero: no cost when idle
  Ideal: event-driven microservices, background jobs, APIs
  vs. AKS: less control, less complexity, scale-to-zero, no cluster management

AZURE CONTAINER INSTANCES (ACI):
  Single container, on-demand (seconds to start)
  No orchestration overhead
  Ideal: batch jobs, one-off tasks, burst compute
  Pricing: per-second billing while running
```

---

## FaaS: Functions as a Service (Serverless)

You provide function code. The platform manages instances, scaling, and execution context.

```
AZURE FUNCTIONS:
  Trigger types: HTTP, Timer, Blob, Queue, Service Bus, Event Hub,
                 Cosmos DB change feed, Event Grid, Custom
  Hosting plans:
    Consumption: scale to zero, per-execution billing, cold start
    Elastic Premium: pre-warmed, VNet integration, no cold start
    Dedicated (App Service): always on, predictable billing
  Durable Functions: stateful orchestration on top of Functions
  Function App: the deployment unit (contains multiple functions)

AWS LAMBDA EQUIVALENTS:
  Lambda + API Gateway = Azure Functions HTTP trigger + API Management
  Lambda + SQS = Azure Functions Queue trigger
  Lambda + S3 events = Azure Functions Blob trigger
  Step Functions = Azure Durable Functions orchestrator
```

---

## Deployment Models

```
PUBLIC CLOUD:
  Shared infrastructure, managed by Azure/AWS/GCP
  Multi-tenant (logical isolation)
  Maximum scale, global reach, lowest management overhead

PRIVATE CLOUD:
  Azure Stack Hub: Azure software running in your datacenter
    → Same Azure APIs, same portal experience, disconnected mode possible
    → Regulatory: data must stay on-premises (air-gapped)
    → Latency: manufacturing systems needing sub-1ms response
  Azure Stack Edge: Azure AI/ML capabilities at the edge (no full cloud)

HYBRID CLOUD:
  Public cloud + on-premises connected (VPN or ExpressRoute)
  Consistent identity: Azure AD extends to on-premises via AD Connect
  Consistent management: Azure Arc manages on-premises VMs and K8s
  Most enterprise architectures are hybrid during migration

MULTI-CLOUD:
  Using Azure + AWS and/or GCP simultaneously
  See 09-MULTI-CLOUD.md for trade-offs
```

---

## Azure Service Taxonomy

Azure organizes services into categories. As someone who worked on Azure, this is familiar territory — but the taxonomy has grown significantly:

```
COMPUTE:
  VM, VMSS, AKS, App Service, Container Apps, ACI, Functions, Batch

STORAGE:
  Blob, Data Lake Gen2, Queue, Table, Files, Managed Disks

DATABASE:
  SQL Database, SQL Managed Instance, Cosmos DB, Database for PostgreSQL/MySQL,
  Cache for Redis, Synapse Analytics

NETWORKING:
  VNet, Load Balancer, Application Gateway (WAF), Front Door, Traffic Manager,
  VPN Gateway, ExpressRoute, Private DNS, CDN, DDoS Protection

ANALYTICS:
  Synapse Analytics, Databricks, Stream Analytics, Data Factory, HDInsight, Purview

AI + ML:
  Azure OpenAI, Cognitive Services, Machine Learning, Bot Service

INTEGRATION:
  Service Bus, Event Hubs, Event Grid, API Management, Logic Apps

DEVOPS:
  Azure DevOps, GitHub (GitHub Actions), Container Registry, Monitor, Key Vault,
  Policy, Blueprints, Cost Management
```

---

## Common Confusion Points

**"PaaS is always less control"**
PaaS reduces operational control (good: less to manage) but increases developer productivity (faster deployment, no OS management). For most web workloads, App Service or Container Apps is the right abstraction.

**"Serverless means no server"**
Serverless means you don't see or manage the server. The server exists. "No server" describes the developer experience, not the infrastructure.

**"VMs in the cloud = same as VMs on-prem"**
Cloud VMs benefit from: elastic scaling (resize in minutes), managed backups, image-based deployment (immutable infra), automated patching options, integration with managed identity, Azure networking (no VLANs to configure). The experience is significantly different from maintaining physical servers.

**"PaaS is more expensive than IaaS"**
PaaS pricing includes managed overhead. But the total cost of ownership includes: engineer time to patch OS, configure HA, manage backups, handle failover. When you include operational cost, PaaS is often cheaper at moderate scale.
