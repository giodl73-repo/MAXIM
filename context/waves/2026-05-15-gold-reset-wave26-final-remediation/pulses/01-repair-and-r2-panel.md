---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `cloud-architecture/05-MICROSERVICES.md`
- `cloud-architecture/06-SERVERLESS.md`
- `cloud-architecture/07-DATA-PLATFORMS.md`
- `cloud-architecture/08-COST-OPTIMIZATION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but their cheat sheets were
direct service/action selector tables. Current Certified Gold requires
diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `cloud-architecture/05-MICROSERVICES.md` | Rebuilt the service selector around AKS, Container Apps, API Management, Istio, Event Grid, Event Hubs, Service Bus, Dapr, and Front Door caveats. |
| `cloud-architecture/06-SERVERLESS.md` | Rebuilt the recommendation table around Functions Consumption/Premium, Durable Functions, fan-out/fan-in, human workflows, Logic Apps, timers, Container Apps, and Durable Entities. |
| `cloud-architecture/07-DATA-PLATFORMS.md` | Rebuilt the service table around ADF, Databricks/Synapse Spark, serverless/dedicated SQL, ML tracking, Snowflake/Azure Data Share, Purview, Delta Lake, and streaming. |
| `cloud-architecture/08-COST-OPTIMIZATION.md` | Rebuilt the action table around reservations, spot, dev/test shutdown, Synapse pause, tagging, anomaly alerts, right-sizing, and savings planning. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- cloud-architecture\05-MICROSERVICES.md cloud-architecture\06-SERVERLESS.md cloud-architecture\07-DATA-PLATFORMS.md cloud-architecture\08-COST-OPTIMIZATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml cloud-architecture\05-MICROSERVICES.md cloud-architecture\06-SERVERLESS.md cloud-architecture\07-DATA-PLATFORMS.md cloud-architecture\08-COST-OPTIMIZATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

