# Compute Patterns: VMs, Containers, Kubernetes, Spot/Reserved/On-Demand

## The Big Picture

Compute in the cloud comes in multiple flavors — each suited to different workload characteristics. The decision flows from workload type → appropriate abstraction → appropriate pricing model.

```
COMPUTE DECISION HIERARCHY

WHAT IS YOUR WORKLOAD?
        |
   +----+----+----+----+
   |    |    |    |    |
  Web  Batch Job  ML  Legacy
  API  Process Schedule Train  App
   |    |    |    |    |
   v    v    v    v    v
AKS/  Container AKS/  AKS + VM with
App   Apps/ACI  Jobs  GPU   specific
Svc              /ACI  N-   config
                       series

COST MODEL?
        |
   +----+----+----+
   |    |    |    |
Always Always Fault-
  on  on but tolerant
      variable workload
        |    |    |
   Reserved  On-  Spot
   instances demand (70-90%
             (base) discount)
```

---

## VM Generations and Series (Azure)

Azure VM SKUs are organized into series with specific optimization targets.

```
GENERAL PURPOSE
+----------------------------------------------------------+
| D-series (Dv5, Dav5, Dlsv5)                             |
|   Balanced CPU:memory (1:4 ratio)                        |
|   Most common: web servers, dev/test, databases          |
|   Standard_D4s_v5: 4 vCPU, 16 GB RAM                   |
+----------------------------------------------------------+

MEMORY OPTIMIZED
+----------------------------------------------------------+
| E-series (Ev5, Eas_v5)                                   |
|   High memory ratio (1:8 ratio)                          |
|   Large relational databases, in-memory caches           |
|   Standard_E8s_v5: 8 vCPU, 64 GB RAM                   |
+----------------------------------------------------------+

COMPUTE OPTIMIZED
+----------------------------------------------------------+
| F-series (Fv2, FX)                                       |
|   High CPU ratio (1:2 ratio)                             |
|   Batch processing, web servers, high-CPU analytics      |
|   Standard_F8s_v2: 8 vCPU, 16 GB RAM                   |
+----------------------------------------------------------+

GPU / ML
+----------------------------------------------------------+
| N-series                                                 |
|   NC: NVIDIA V100/A100, ML training                     |
|   ND: NVIDIA A100, deep learning                        |
|   NV: NVIDIA T4, visualization                          |
+----------------------------------------------------------+

BURSTABLE (B-series)
+----------------------------------------------------------+
| B-series (Bsv2, Basv2)                                  |
|   Accumulate credits when below baseline CPU usage       |
|   Burst above baseline using accumulated credits         |
|   Dev/test, small web apps, low baseline with peaks     |
|   Standard_B2ms: 2 vCPU, 8 GB RAM, 40% baseline CPU   |
|   Cheapest general-purpose option for intermittent load |
+----------------------------------------------------------+

HIGH PERFORMANCE COMPUTE
+----------------------------------------------------------+
| H-series, HB-series (HBv3, HBv4)                        |
|   AMD EPYC, high memory bandwidth                       |
|   InfiniBand 200 Gbit/s for MPI workloads              |
|   Molecular dynamics, finite element analysis, CFD      |
+----------------------------------------------------------+
```

### VM SLA Tiers

```
SINGLE VM + Standard SSD:     99.9%  (4.38h/year downtime budget)
SINGLE VM + Premium SSD:      99.9%  (same)
AVAILABILITY SET (2+ VMs):    99.95% (2.19h/year)
  Distributes VMs across fault domains (different racks) and
  update domains (different patch cycles)
AVAILABILITY ZONES (2+ VMs):  99.99% (52min/year)
  Distributes VMs across physically separate AZ buildings
  Recommended for production workloads
```

---

## Pricing Models: Reserved vs. Spot vs. On-Demand

```
ON-DEMAND PRICING:
  Pay per second of usage
  No commitment
  Full price (most expensive per unit)
  Use: variable workloads, dev/test, burst capacity

RESERVED INSTANCES:
  Commit to 1 or 3 years
  Pay upfront or monthly
  Discount: 1-year = ~40% off; 3-year = ~70% off (approximate)
  Instance size flexibility: applies to same family/region
  Azure Hybrid Benefit: add Windows Server / SQL Server license discount
    → 3-year RI + Hybrid Benefit: up to 80% discount vs. on-demand
  Savings Plans (Azure): flexible RI — any VM size/family, fixed hourly spend commitment
    Not as deep discount as RI, but flexible across instance types
  Use: stable, predictable workloads

SPOT INSTANCES (Azure Spot VMs):
  Spare capacity at 60-90% discount
  Azure can preempt with 30-second notice
  NOT guaranteed availability
  Use: fault-tolerant batch workloads, CI/CD agents, non-critical processing
  AKS: spot node pools → jobs tolerate node disappearance
  Pattern: use checkpointing + restart logic; jobs are idempotent

COMPARISON:
  Stable production workload (web API): Reserved (1 or 3 year)
  Dev/test environment (business hours): Scheduled shutdown + on-demand
  ML training job (can restart): Spot
  Burst traffic (holiday sales): On-demand or Spot fallback
```

---

## Containers vs. VMs: Overhead Comparison

```
VM OVERHEAD:
  Full OS: kernel, filesystem, networking stack, init system
  Memory: 512MB–2GB just for OS overhead
  Boot time: minutes
  Image size: 10–100GB
  Isolation: hardware virtualization (hypervisor)

CONTAINER OVERHEAD:
  Shares host OS kernel (namespace + cgroup isolation)
  Memory overhead: minimal (no OS duplication)
  Start time: seconds (milliseconds for warm containers)
  Image size: 50MB–1GB (base layer shared between containers)
  Isolation: kernel namespaces (weaker than VMs — same kernel)

WHEN CONTAINERS ARE NOT ENOUGH:
  Windows containers cannot share Linux kernel → Windows VM required
  High-security multi-tenant: different kernel per tenant → VMs
  Legacy applications requiring full OS control → VM
  Kernel module requirements → VM

WHEN VMs ARE NOT ENOUGH:
  Extreme density requirements → containers (1000s per node)
  Fast scaling (seconds, not minutes) → containers
  Immutable infrastructure, GitOps → containers + K8s
```

---

## AKS: Azure Kubernetes Service Architecture

```
AKS CLUSTER ARCHITECTURE

CONTROL PLANE (Azure managed, free):
  API Server:           kubectl and CI/CD tool talk to this
  etcd:                 cluster state store (Raft consensus)
  Scheduler:            assigns pods to nodes
  Controller Manager:   reconciliation loops (deployments, services, etc.)

NODE POOLS (you pay for these):
  System Node Pool:     runs critical cluster add-ons (DNS, monitoring)
    Recommendation: 3+ nodes, dedicated, no-schedule taint
  User Node Pool:       runs your application workloads
    Multiple pools allowed: different VM SKU per workload type

NETWORKING OPTIONS:
  Kubenet: simpler, NAT overlay, smaller IP consumption
  Azure CNI: pods get VNet IPs, visible on VNet, max scale
  Azure CNI Overlay: Azure CNI perf, Kubenet IP efficiency (newer)
  Cilium: eBPF-based, used for advanced network policy, observability

AUTOSCALING:
  Cluster Autoscaler: scales node count based on pending pods
    (nodes added when pods cannot be scheduled; removed when underutilized)
  Horizontal Pod Autoscaler (HPA): scales pod count based on CPU/memory metrics
  Vertical Pod Autoscaler (VPA): adjusts pod resource requests (requests/limits)
  KEDA: event-driven autoscaling (scale pods to 0 based on queue length, etc.)
    Used by Azure Container Apps internally

NODE POOL TYPES:
  Regular: always running, reserved/on-demand pricing
  Spot: preemptible, 60-90% discount, can disappear with 30s notice
  System: dedicated to cluster infrastructure (taint: CriticalAddonsOnly)
```

### AKS Integration with Azure Services

```
AZURE AD INTEGRATION:
  AKS uses Azure AD for cluster authentication (kubectl)
  Managed identity for node pool (no credential to manage)
  Workload identity: pods get Azure AD identity (no secrets)

AZURE MONITOR INTEGRATION:
  Container Insights: logs + metrics from all pods
  Azure Monitor Workspace: Prometheus metrics (Azure-managed)
  Grafana + Azure Monitor Workspaces: production dashboards

AZURE CNI + PRIVATE ENDPOINTS:
  Pods can call Azure SQL, Storage, Key Vault via private endpoint
  No public internet traffic for service calls
  NSG rules on node subnets control traffic

ACR (Azure Container Registry) INTEGRATION:
  Pull from ACR with managed identity (no credentials)
  Geo-replication: multi-region ACR for faster pulls in each region
```

---

## VM SKU Selection Decision Tree

```
+------------------------+
| What is the workload?  |
+------------------------+
          |
   +------+------+------+------+------+
   |      |      |      |      |      |
 Web    DB    Batch  ML   Legacy  Dev
 API  Server  Job   Train  App   Test
   |      |      |      |      |      |
D-ser  E-ser  D/F-  N-   Any + Bv2
(balanced)(memory)(compute)(GPU) config (cheap)
   |      |      |
   +------+------+------+
              |
   What SLA do I need?
              |
   +----------+----------+
   |                     |
Single zone          Multi-zone (AZ)
SLA 99.9%            SLA 99.99%
   |                     |
Pay-as-you-go      Multiple VMs with
dev/test           Zone distribution
   |
Is it steady state?
   |
+--+--+
|     |
Yes   No
|     |
RI    On-demand
(40-72% disc)
```

---

## Common Confusion Points

**"Spot instances are Azure's cheap leftover capacity"**
Azure Spot VMs use spare capacity from Azure's excess pool. They are real hardware, just provisioned when available. They can be preempted with 30-second notice when Azure needs the capacity. Not suitable for workloads that cannot tolerate interruption.

**"Availability Set = Availability Zone"**
Availability Sets distribute VMs across fault domains (different racks) and update domains within a single datacenter. Availability Zones are physically separate buildings (separate power, cooling, networking) within a region. Zones provide much stronger isolation (different building failure mode).

**"AKS control plane is free"**
The AKS control plane (API server, etcd, scheduler) is managed by Azure at no charge. You pay for the worker nodes (VMs) in your node pools. At scale, the control plane represents significant infrastructure — this is a real subsidy.

**"Containers are just VMs with less overhead"**
Containers share the host kernel — this is fundamentally different from VMs, which have separate kernels. The isolation model is weaker (container escapes are more feasible than VM escapes). For multi-tenant workloads with untrusted code, VMs or hypervisor-based containers (Kata Containers) provide stronger isolation.

---

## Decision Cheat Sheet

| Workload | Compute Choice | Pricing Model |
|---------|---------------|---------------|
| Stable web API (always on) | AKS or App Service | Reserved (1-3 year) |
| Batch ML training (restartable) | AKS spot node pool | Spot |
| Event-driven, scale to zero | Container Apps or Functions | Consumption |
| Legacy Windows app | App Service (Windows) or VM | Reserved |
| Dev/test workloads | VMs with auto-shutdown | On-demand |
| GPU training | N-series VM or AKS GPU node pool | On-demand or Reserved |
| Burst capacity for peak traffic | VMSS with autoscale + spot | On-demand + Spot |
