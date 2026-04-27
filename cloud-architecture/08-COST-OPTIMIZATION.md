# Cost Optimization: FinOps, Reserved Capacity, Autoscaling, Tagging

## The Big Picture

Cloud cost management is a continuous engineering discipline, not a one-time exercise. The FinOps framework provides the vocabulary and process.

```
FINOPS FRAMEWORK (CNCF FinOps Foundation)

PRINCIPLES:
  Teams need to collaborate (finance, engineering, business units)
  Everyone takes ownership of their cloud usage
  FinOps reports should be accessible and timely
  A centralized team drives FinOps practice
  Decisions driven by business value of cloud

THREE PHASES (continuous cycle):

  +-------------------+
  |  INFORM           |
  |  Cost allocation  |
  |  Reporting        |
  +-------------------+
    Visibility: what are we spending and why?
    Tagging, cost analysis, unit economics.
          |
          v
  +-------------------+
  |  OPTIMIZE         |
  |  Rightsizing      |
  |  Reservations     |
  +-------------------+
    Reduce waste: rightsizing, reservations, spot.
    Idle resources, unused licenses, oversized.
          |
          v
  +-------------------+
  |  OPERATE          |
  |  Budgets          |
  |  Anomaly detect   |
  +-------------------+
    Continuous improvement: budgets, alerts, culture.
    Engineering accountability, governance.
          |
          (feeds back to Inform)
```

---

## Reserved Instances and Savings Plans

The single highest-impact cost optimization for stable workloads.

### Azure Reserved VM Instances

```
RESERVED INSTANCE MECHANICS:
  Commitment: you agree to use specific VM family in specific region
  Duration: 1 year or 3 years
  Payment: upfront (max discount) / monthly / partial upfront
  Discount vs. pay-as-you-go:
    1-year: ~40% discount
    3-year: ~63% discount
    3-year + Azure Hybrid Benefit (Windows): up to 80% discount

SCOPE:
  Shared: applies to any subscription in billing account (recommended)
  Single subscription: applies to specific subscription only
  Resource group: narrowest scope (least flexibility)

INSTANCE SIZE FLEXIBILITY:
  Reservations apply within the same "instance size flexibility group"
  e.g., Dsv5 reservation applies to D2s_v5, D4s_v5, D8s_v5, etc.
  No need to buy reservations for exact size — within family it normalizes
  Caveat: GPU, HPC series have less flexibility

CANCELLATION:
  Can cancel within first 90 days of first 3-year reservation
  Swap: exchange unused reservation for different size/region
  Auto-renew: configure to auto-renew at expiry (watch pricing changes)
```

### Azure Hybrid Benefit

```
AZURE HYBRID BENEFIT:
  Use existing on-premises Windows Server or SQL Server licenses in Azure
  Windows Server with SA (Software Assurance):
    → Dual use: run on-prem AND in Azure
    → D4s VM (Windows): normally $0.21/hr OS + $0.19/hr compute = $0.40/hr
       with Hybrid Benefit: $0.19/hr compute only (0.21/hr OS waived)
  SQL Server with SA:
    → Azure SQL DB, SQL MI, SQL VM: SQL license included at no extra cost
    → Massive savings for SQL Server workloads (SQL licenses are expensive)

SAVINGS PLANS (Azure):
  Like a Reserved Instance but flexible across instance types
  Commit to spend $X per hour
  Applies to: VMs, Container Apps, AKS, Functions Premium, App Service
  Discount: up to 65% vs. pay-as-you-go
  Trade-off vs. RI: less discount than RI, but applies to any VM size/family
  Use: when you need flexibility (don't know exact VM mix 1-3 years out)
```

---

## Spot Instances / Spot VMs

```
AZURE SPOT VMs:
  Azure's excess capacity at 60-90% discount
  Eviction: 30-second notice when Azure needs capacity back
  Eviction policy options:
    Stop/Deallocate: VM stops, disk preserved, IP lost
    Delete: VM and disk deleted
  Eviction rate varies by region, VM family, time of day
  Check eviction rates: Azure Portal → Spot Pricing History

WHEN TO USE SPOT:
  Batch processing with checkpointing
  CI/CD agents (build fail → retry next agent)
  ML training with checkpoint saves
  Rendering, simulation (retryable tasks)
  AKS spot node pools (pods evicted → scheduler reschedules)

WHEN NOT TO USE:
  Production web APIs (eviction causes downtime)
  Databases without DR/failover
  Any stateful workload without recovery logic

AKS SPOT NODE POOL PATTERN:
  Taint: kubernetes.azure.com/scalesetpriority=spot:NoSchedule
  Toleration in workload: tolerates this taint
  Fallback: on-demand node pool for non-spot-tolerant pods
  Budget: spot nodes for 80% of batch workload, on-demand for 20% overhead
```

---

## Right-Sizing Methodology

```
RIGHT-SIZING PROCESS:

1. COLLECT METRICS (7-30 day window):
   CPU: average, p95, peak
   Memory: average usage
   Disk IOPS: peak sustained
   Network: egress/ingress peak

2. IDENTIFY CANDIDATES:
   Azure Advisor: automatically flags underutilized VMs
   Criteria: CPU avg < 5% AND memory < 50% over 14 days
   Cost: potential savings shown per recommendation

3. ANALYZE HEADROOM:
   Current: D8s_v5 (8 vCPU, 32GB RAM)
   Actual usage: CPU avg 12%, peak 40%; Memory avg 28%, peak 55%
   Target: D4s_v5 (4 vCPU, 16GB RAM) with 20% headroom
   Risk: none (peak CPU 40% → on D4s = 80%, still within limits)

4. TEST AND MONITOR:
   Change in dev/test first
   Monitor for 1 week: any performance degradation?
   Promote to production
   Monitor for 2 weeks

5. REPEAT QUARTERLY:
   Workloads change; right-sizing is not one-time
   New Azure VM generations often offer better price/perf
   (D5s → D5s_v5: same price, ~20% better performance)
```

---

## Autoscaling as Cost Control

```
AUTOSCALING FOR COST:
  Scale out during peak → scale in during off-peak
  Pay only for capacity actually needed

  Web API: VMSS / AKS HPA
    Scale out: CPU > 70% for 3 minutes
    Scale in: CPU < 30% for 10 minutes (scale-in delay prevents thrash)
    Min instances: 2 (HA), Max: 20

  Development environments:
    Scale to zero at end of day
    VMSS: scheduled scaling (scale to 0 at 8pm, scale to 5 at 8am)
    AKS: dev cluster scaled down, or auto-shutdown VM nodes overnight

  Synapse Dedicated SQL Pool:
    Pause when not in use (pause = $0, no data loss)
    Auto-pause after 1 hour of inactivity (built-in)
    Resume: ~5 minutes (plan for this in pipeline scheduling)

  Azure Functions (Consumption):
    Scale to zero by default → zero cost when idle
    Premium plan: min instances > 0 → cost even when idle
    Choose based on cold start tolerance
```

---

## Tagging Governance

Tags enable cost allocation — without tags, you cannot answer "how much does team X's product Y cost per environment?"

```
TAGGING STRATEGY

RECOMMENDED MINIMUM TAG SET:
  Application: the product or system (e.g., "payment-service")
  Environment: dev / staging / prod
  Team / CostCenter: which team owns it (e.g., "payments-team")
  Owner: email of tech lead (for alerting)
  BusinessUnit: which org unit (e.g., "core-banking")

ENFORCEMENT:
  Azure Policy: deny resource creation without required tags
    Built-in policy: "Require tag and its value"
    Audit mode first → Deny mode after teams are compliant
  Azure Blueprints: apply tag policy + RBAC + resource groups as a unit
  Infrastructure as Code: enforce in Bicep/Terraform templates

INHERITANCE LIMITATION:
  Azure tags do NOT inherit from resource group to resources by default
  Solution 1: Policy to inherit RG tags to resources automatically
  Solution 2: Apply tags in IaC at both RG and resource level

COST ALLOCATION VIEWS:
  Azure Cost Management + Billing → Cost Analysis → Group By Tag
  Filter: last 30 days, by Application="payment-service"
  Export: send cost data to Storage → query with Power BI / Synapse

CHARGEBACK vs. SHOWBACK:
  Showback: show each team what they're spending (informational)
  Chargeback: actually invoice teams for their usage (financial)
  Most organizations start with showback; mature FinOps → chargeback
```

---

## Azure Cost Management + Budgets

```
AZURE COST MANAGEMENT FEATURES:

COST ANALYSIS:
  Visualize costs by subscription, resource group, tag, service
  Date range: last 30d, custom, monthly, quarterly
  Accumulated vs. daily view
  Download as CSV for offline analysis

BUDGETS:
  Set monthly budget for subscription/resource group/tag
  Alert thresholds: 80%, 100%, 120% of budget
  Alert types: actual cost (real spend) or forecast (projected by month end)
  Actions: email + optional Logic App action
    (Logic App: scale down dev cluster when budget exceeded)

ANOMALY DETECTION:
  Cost Management automatically detects unusual spend
  Example: "your App Service costs are 300% higher than usual yesterday"
  Root cause: forgot to delete accidentally created large VM
  Alert: email notification with comparison to baseline

COST RECOMMENDATIONS (Azure Advisor):
  Underutilized VMs: shutdown or downsize
  Reserved Instance recommendations: based on 30-day usage pattern
  Unattached managed disks: delete orphaned disks
  Expired App Service certificates: cleanup
  Idle load balancers / Application Gateways: review and remove

UNIT ECONOMICS:
  Cost per API request = (monthly cost) / (monthly API calls)
  Cost per active user = (monthly cost) / (monthly active users)
  Cost per transaction = (monthly cost) / (monthly transactions)
  Track over time: ensure cost/unit decreases or stays flat as scale increases
```

---

## TCO Analysis: Cloud vs. On-Premises

```
TOTAL COST OF OWNERSHIP (3-YEAR TYPICAL)

ON-PREMISES COSTS:
  Hardware: servers, networking, storage (3-5 year depreciation)
  Datacenter: power, cooling, physical security, colocation fees
  Staffing: datacenter operators, network engineers, storage admins
  Software: OS licenses, middleware, monitoring tools
  Maintenance: hardware warranty, firmware updates

CLOUD COSTS (Azure):
  Compute: VM/container/function pricing
  Storage: object, block, file
  Network: egress (usually 5-10% of total), inter-region
  Licenses: pay-as-you-go SQL/Windows, or Hybrid Benefit
  Support: included basic, paid for enhanced

HIDDEN CLOUD SAVINGS:
  No hardware refresh planning (3-year cliff in on-prem)
  Elastic scaling: no over-provisioning for peak
  Managed services: reduced ops headcount needed
  Global reach: no datacenter in each region needed
  Speed: provision in minutes vs. months for on-prem procurement

HIDDEN CLOUD COSTS:
  Egress: data leaving Azure to internet (cost per GB)
  Inter-region: data transfer between regions
  Premium tiers: Premium SSD, Premium networking, always-on services
  Support plans: Developer: $29/mo; Standard: $100+; Premier: contractual

AZURE TCO CALCULATOR: azure.microsoft.com/pricing/tco/calculator/
  Input: on-prem servers, storage, bandwidth
  Output: estimated 5-year TCO comparison
```

---

## Common Confusion Points

**"Reserved Instances lock you in"**
Reserved Instances are a billing commitment, not a capacity lock-in. You can change VM size within the same family. You can cancel with a fee within 90 days. You can exchange RIs for different SKUs. The architecture remains flexible.

**"Autoscaling will always save money"**
Autoscaling saves money on variable workloads. For steady, predictable workloads, a fixed appropriately-sized deployment may be cheaper and simpler. Evaluate whether autoscaling complexity is worth the savings.

**"We just need more monitoring"**
More monitoring data without action is just more cost (monitoring itself costs money). FinOps requires a feedback loop: visibility (inform) → decision (optimize) → governance (operate) → accountability. Data without process change is noise.

**"Tags can be added later"**
Retrofitting tags onto 10,000 resources is painful and error-prone. Enforce tags at creation via Azure Policy. Resources created without required tags are denied. Tag discipline from day one is far cheaper than cleanup later.

---

## Decision Cheat Sheet

| Situation | Action |
|-----------|--------|
| Stable workload running 24/7 | Reserved Instance (1 or 3 year) + Hybrid Benefit |
| Batch job that can restart | Spot VM/AKS spot node pool |
| Dev/test environments | Auto-shutdown schedule, scale to zero |
| Synapse Dedicated SQL Pool idle | Configure auto-pause |
| Cannot answer "what does product X cost?" | Tag governance + Azure Policy enforcement |
| Cloud bill spike without explanation | Cost Management anomaly detection + alert |
| VM showing <5% CPU utilization | Azure Advisor right-size recommendation |
| Preparing for 3-year budget planning | Azure Savings Plans + TCO Calculator |
