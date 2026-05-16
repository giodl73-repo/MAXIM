---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `data-science/02-PANDAS.md`
- `data-science/04-PYTORCH.md`
- `data-science/05-MLOPS.md`
- `data-science/06-AZURE-ML.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
promotion defects: task-routing cheat sheets that answered "what tool" rather
than helping the reader diagnose failure modes and boundaries.

## Changes

| Guide | Repair |
|---|---|
| `data-science/02-PANDAS.md` | Rebuilt the cheat sheet around selection/assignment, groupby, reshape, joins, performance, and time-series diagnosis. |
| `data-science/04-PYTORCH.md` | Rebuilt the cheat sheet around tool fit, tensor shape, gradients, training loops, scaling, and inference/deployment. |
| `data-science/05-MLOPS.md` | Rebuilt the cheat sheet around experiment tracking, promotion, data versioning, serving, drift, feature stores, and retraining triggers. |
| `data-science/06-AZURE-ML.md` | Rebuilt the cheat sheet around compute choice, training packaging, AutoML fit, pipelines/components, online vs batch endpoints, governance, and cost control. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- data-science\02-PANDAS.md data-science\04-PYTORCH.md data-science\05-MLOPS.md data-science\06-AZURE-ML.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml data-science\02-PANDAS.md data-science\04-PYTORCH.md data-science\05-MLOPS.md data-science\06-AZURE-ML.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

