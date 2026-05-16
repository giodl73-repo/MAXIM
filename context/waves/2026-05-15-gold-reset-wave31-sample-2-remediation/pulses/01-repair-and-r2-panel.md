---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `coral-reefs/09-RESTORATION.md`
- `criminology/00-OVERVIEW.md`
- `culinary-history/00-OVERVIEW.md`
- `culinary-history/01-PREHISTORIC.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
answer or router tables that selected restoration tools, criminology frameworks,
culinary-history files, or prehistoric food facts without enough diagnostic
caveats.

## Changes

| Guide | Repair |
|---|---|
| `coral-reefs/09-RESTORATION.md` | Rebuilt the cheat sheet around coral gardening, micro-fragmentation, artificial substrate, biorock, assisted evolution, scale gap, outplanting failure, and larval seeding diagnosis. |
| `criminology/00-OVERVIEW.md` | Rebuilt the overview router around deterrence, neighborhood concentration, law compliance, labeling, white-collar crime, organized crime, policing, incarceration, and desistance diagnosis. |
| `culinary-history/00-OVERVIEW.md` | Rebuilt the overview router around cooking as technology, early states, spice systems, traditional cuisine, kitchen hierarchy, industrial food, global comparison, and food-system critique. |
| `culinary-history/01-PREHISTORIC.md` | Rebuilt the cheat sheet around cooking evidence, human evolution, fermentation, grinding stones, salt, and earth-oven technology. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- coral-reefs\09-RESTORATION.md criminology\00-OVERVIEW.md culinary-history\00-OVERVIEW.md culinary-history\01-PREHISTORIC.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml coral-reefs\09-RESTORATION.md criminology\00-OVERVIEW.md culinary-history\00-OVERVIEW.md culinary-history\01-PREHISTORIC.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

