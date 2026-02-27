# Cloud Architecture: Models, Patterns, and Trade-offs — Landscape

## Sentinel Context

This directory is one of three in the Sentinel triad (K-Spade C-IV). The thesis: *no single point of truth, no single point of trust, no single point of failure.*

```
THE SENTINEL TRIAD — Cloud Architecture View
═══════════════════════════════════════════════════════════════════

              CAP Theorem (2000)
              "Every design choice picks a point
               on the C-A-P trade-off surface."
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌────────────┐   ┌───────────┐   ╔══════════════╗
  │ DISTRIBUTED│   │ SECURITY  │   ║ CLOUD        ║
  │ SYSTEMS    │   │ ENG.      │   ║ ARCHITECTURE ║
  │            │   │           │   ║              ║
  │ "Who has   │   │ "Who do   │   ║ "Where do    ║
  │  the       │   │  you      │   ║  you put     ║
  │  truth?"   │   │  trust?"  │   ║  the truth?" ║
  └─────┬──────┘   └─────┬─────┘   ╚══════╤═══════╝
        │                │                │
        └────────────────┴────────────────┘
                         │
              Infrastructure as the execution layer
```

Cloud architecture is the **execution layer** for the entire volume. The consensus protocols from distributed systems and the trust models from security engineering are theoretical until they run on actual infrastructure --- AZs, regions, load balancers, managed services. Cloud architecture answers the question of *where* and *how*: multi-AZ for partition tolerance, managed Kubernetes for consensus (etcd runs Raft), mTLS between services for zero-trust enforcement, health probes for failure detection. Every CAP trade-off, every quorum configuration, every security control from the other two domains materializes here as an infrastructure decision with cost, latency, and blast-radius consequences.

**See also:**
- `../computing/00-SENTINEL-THESIS.md` — Volume thesis: the Sentinel principle and constraint stack
- `../distributed-systems/00-OVERVIEW.md` — Consensus: the theory that cloud services implement internally
- `../security-engineering/00-OVERVIEW.md` — Trust: the controls that cloud infrastructure must enforce

---

## The Big Picture

Cloud architecture is the discipline of designing systems that run on cloud infrastructure — exploiting the economics of shared, elastic infrastructure while managing the distributed systems complexity it introduces.

```
CLOUD ARCHITECTURE LANDSCAPE
+-----------------------------------------------------------------------+
|                                                                       |
|  ABSTRACTION LAYERS (you choose where to sit)                        |
|  +------------------------------------------------------------------+ |
|  | Your Code                                                        | |
|  +------------------------------------------------------------------+ |
|  | FaaS/Serverless  | Containers | VMs      | Bare Metal          | |
|  | Azure Functions  | AKS        | VMs      | (IaaS dedicated)    | |
|  +------------------------------------------------------------------+ |
|  | Managed PaaS     | Container  | OS       | Firmware            | |
|  | App Service      | Runtime    | Kernel   |                     | |
|  +------------------------------------------------------------------+ |
|  | Network, Storage, Compute (IaaS)                                 | |
|  +------------------------------------------------------------------+ |
|  | Physical: Servers, Switches, Storage Arrays, Power, Cooling     | |
|  +------------------------------------------------------------------+ |
|  ↑ You manage this      ↑ Cloud provider manages this →            | |
+-----------------------------------------------------------------------+

CLOUD-NATIVE PRINCIPLES (CNCF):
  Microservices   Containers   Dynamic orchestration   DevOps practices

ECONOMICS:
  CapEx → OpEx: no data center, no hardware refresh cycle
  Elasticity: scale in minutes, not procurement quarters
  Global reach: regions available in minutes
  Pay-per-use: idle capacity costs nothing (serverless model)
```

---

## The Three Major Clouds: Azure, AWS, GCP

This guide is Azure-first (learner worked on Azure), but equivalent services are mapped.

```
SERVICE EQUIVALENCE TABLE (major categories)

COMPUTE:
  Azure VMs             AWS EC2               GCP Compute Engine
  Azure Kubernetes (AKS) Amazon EKS            GKE (Google Kubernetes Engine)
  Azure Container Apps   AWS Fargate            Cloud Run
  Azure Functions        AWS Lambda             Cloud Functions

STORAGE:
  Azure Blob Storage     Amazon S3              Cloud Storage
  Azure Disk (Managed)   Amazon EBS             Persistent Disk
  Azure Files            Amazon EFS             Filestore

DATABASE:
  Azure SQL DB           Amazon RDS             Cloud SQL
  Azure Cosmos DB        Amazon DynamoDB        Cloud Firestore / Bigtable
  Azure Cache for Redis  Amazon ElastiCache     Cloud Memorystore

MESSAGING:
  Azure Service Bus      Amazon SQS/SNS         Cloud Pub/Sub
  Azure Event Hubs       Amazon Kinesis         Cloud Pub/Sub
  Azure Event Grid       Amazon EventBridge     Cloud Eventarc

NETWORKING:
  Azure VNet             Amazon VPC             VPC
  Azure Load Balancer    Amazon ELB/ALB         Cloud Load Balancing
  Azure Front Door       AWS CloudFront+WAF     Cloud Armor + CDN
  Azure ExpressRoute     AWS Direct Connect     Cloud Interconnect

IDENTITY:
  Azure AD (Entra ID)    AWS IAM + Cognito      Cloud IAM + Identity Platform

DEVOPS:
  Azure DevOps           AWS CodePipeline        Cloud Build / Cloud Deploy
  Azure Container Registry Amazon ECR           Artifact Registry
```

---

## Why You Built What You Built — The Azure Insider View

You worked on Azure's data platform services (ADF, ADB, Azure SQL). From the inside, you see what many architects only see from the outside:

```
ADF (Azure Data Factory): you know this deeply
  → Pipeline orchestration = the ETL/ELT equivalent of distributed workflow
  → The integration runtimes, trigger types, dataflow execution
  → This maps directly to modern cloud-native patterns:
    - ADF triggers → Azure Functions triggers
    - ADF pipeline = Durable Functions orchestrator
    - ADF IR (Integration Runtime) = compute layer abstraction
    - ADF connected services = service connections with managed identity

AZURE SQL / ADO.NET: you know this deeply
  → DTU vs. vCore model, elastic pools, read replicas, geo-replication
  → This is the same "single-leader, async replication" pattern (04-REPLICATION.md)
  → Elastic pools = resource sharing across databases (multi-tenancy pattern)
  → Geo-replication = follower replicas with async lag

AZURE DEVOPS (VSTS): you built this
  → Build/release pipelines = what every engineering team uses now
  → The service itself is a distributed system (consistent with this library)
  → Your scale challenges are the distributed systems problems in this library
```

---

## Cloud Economics

```
CAPEX vs. OPEX SHIFT
  Traditional:
    Purchase servers → 3-5 year depreciation
    Buy capacity for peak, waste during off-peak
    Hardware refresh cycles: plan 18 months ahead
    Data center: power, cooling, physical security, staff

  Cloud:
    Pay per use: compute, storage, network by the second/GB
    Reserve capacity for discount (1 or 3 year commitments)
    Spot/preemptible for fault-tolerant workloads (70-90% discount)
    No data center overhead: 100% operational expense

SCALE ECONOMICS:
  Azure, AWS, GCP buy hardware at a scale that provides
  30-50% cost advantage over individual enterprise purchasing
  Pass savings partially to customers; keep remainder as margin

RESERVED CAPACITY:
  Commitment to use (not "pay whether you use it or not")
  Azure Reserved VM Instances: 1 or 3 year, 40-72% discount vs. pay-as-you-go
  Azure Hybrid Benefit: use existing Windows Server/SQL Server licenses in Azure
  Savings Plans (Azure): flexible usage commitment (not instance-specific)
```

---

## Cloud-Native vs. Cloud-Hosted vs. Cloud-Enabled

```
CLOUD-ENABLED (Lift and Shift):
  Take on-premises app, move to cloud VMs with minimal change
  Same architecture: IIS + SQL Server, just in the cloud
  Benefit: stop running the data center
  Cost: not exploiting cloud capabilities; often more expensive than on-prem
  Pattern: migrate first, optimize later

CLOUD-HOSTED:
  Refactor to use managed cloud services: Azure SQL instead of SQL VM,
  Azure Storage instead of NFS mount, Azure Key Vault instead of HSM
  Benefit: managed services (patching, backup, HA handled by Azure)
  Pattern: right-size each component to appropriate service tier

CLOUD-NATIVE:
  Architecture designed for cloud characteristics:
    - Stateless services (12-factor app principles)
    - Horizontal scaling (not vertical)
    - Resilience to infrastructure failure built-in
    - Event-driven, asynchronous communication
    - Managed services throughout
    - Immutable infrastructure (containers, IaC)
    - Observability from day one
  Pattern: CNCF landscape, Kubernetes, Helm, OpenTelemetry
```

---

## Guide Map

```
00-OVERVIEW.md         ← you are here
01-CLOUD-MODELS.md     ← IaaS/PaaS/SaaS/FaaS, shared responsibility, deployment models
02-COMPUTE-PATTERNS.md ← VMs, containers, AKS, spot/reserved, autoscaling
03-STORAGE-PATTERNS.md ← Blob, disk, files, database selection, access patterns
04-NETWORKING.md       ← VNet, NSG, load balancer, ExpressRoute, CDN, DNS
05-MICROSERVICES.md    ← AKS deep-dive, service mesh, API Management, Event Grid
06-SERVERLESS.md       ← Azure Functions, Durable Functions, Logic Apps, cold start
07-DATA-PLATFORMS.md   ← Synapse, Databricks, ADF, Delta Lake, lakehouse
08-COST-OPTIMIZATION.md← FinOps, reserved instances, right-sizing, tagging
09-MULTI-CLOUD.md      ← Azure Arc, multi-cloud governance, data gravity
```

---

## Common Confusion Points

**"Cloud is just someone else's computer"**
Cloud is someone else's computer, plus: elastic scaling, managed services that abstract operational complexity, global network backbone, economy of scale pricing, and a rich ecosystem of integrations. The "just a computer" framing misses why 80% of enterprise workloads are migrating to cloud.

**"PaaS is always cheaper than IaaS"**
PaaS (App Service, Azure SQL) includes managed overhead in the price. For very high throughput, self-managed IaaS may be cheaper. But PaaS eliminates operations cost (patching, monitoring, HA configuration) — the total cost of ownership comparison must include engineering time.

**"Cloud is inherently less secure than on-prem"**
Major cloud providers invest more in physical security, patch management, and certifications than most enterprises can afford. The risk difference is in the configuration: misconfigured cloud resources are more easily exposed to the internet than misconfigured on-premises servers. The security risk of cloud is primarily misconfiguration risk.
