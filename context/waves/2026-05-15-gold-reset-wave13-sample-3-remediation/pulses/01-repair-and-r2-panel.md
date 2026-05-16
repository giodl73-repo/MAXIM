---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ecology/02-COMMUNITY-ECOLOGY.md`
- `ecology/03-ECOSYSTEM-ENERGETICS.md`
- `ecology/04-BIOGEOCHEMICAL-CYCLES.md`
- `ecology/05-SUCCESSION-STABILITY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
observation/context/management selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `ecology/02-COMMUNITY-ECOLOGY.md` | Rebuilt the community table around keystone release, trophic cascades, niche partitioning, predation-mediated diversity, naive prey, and fire disturbance. |
| `ecology/03-ECOSYSTEM-ENERGETICS.md` | Rebuilt the energetics table around trophic transfer, meat resource intensity, tropical NPP, inverted biomass pyramids, detrital pathways, and old-growth NEP. |
| `ecology/04-BIOGEOCHEMICAL-CYCLES.md` | Rebuilt the cycles table around eutrophication, dead zones, old-growth carbon balance, wetlands, boreal peatlands, and N2O emissions. |
| `ecology/05-SUCCESSION-STABILITY.md` | Rebuilt the succession/stability table around secondary succession, hysteresis, resilience, fire suppression, old-field restoration, and coral-regime shifts. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ecology\02-COMMUNITY-ECOLOGY.md ecology\03-ECOSYSTEM-ENERGETICS.md ecology\04-BIOGEOCHEMICAL-CYCLES.md ecology\05-SUCCESSION-STABILITY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ecology\02-COMMUNITY-ECOLOGY.md ecology\03-ECOSYSTEM-ENERGETICS.md ecology\04-BIOGEOCHEMICAL-CYCLES.md ecology\05-SUCCESSION-STABILITY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

