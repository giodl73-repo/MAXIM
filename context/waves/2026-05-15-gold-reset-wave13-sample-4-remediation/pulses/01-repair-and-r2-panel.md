---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ecology/06-BIOGEOGRAPHY.md`
- `ecology/07-AQUATIC-ECOSYSTEMS.md`
- `ecology/08-DISTURBANCE-ECOLOGY.md`
- `ecology/09-CONSERVATION-BIOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/observation/situation selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `ecology/06-BIOGEOGRAPHY.md` | Rebuilt the biogeography table around vicariance/dispersal, species-area relationships, species loss, tropical diversity, Australian mammals, and island richness. |
| `ecology/07-AQUATIC-ECOSYSTEMS.md` | Rebuilt the aquatic table around stratification, fall blooms, eutrophication, cyanobacteria, headwaters, coral bleaching, and estuarine nurseries. |
| `ecology/08-DISTURBANCE-ECOLOGY.md` | Rebuilt the disturbance table around fire suppression, meadow diversity, trophic cascades, invasives, prescribed fire, and pathogen disturbance. |
| `ecology/09-CONSERVATION-BIOLOGY.md` | Rebuilt the conservation table around fragmentation, reserve size, risk priority, connectivity, investment priority, and rewilding feasibility. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ecology\06-BIOGEOGRAPHY.md ecology\07-AQUATIC-ECOSYSTEMS.md ecology\08-DISTURBANCE-ECOLOGY.md ecology\09-CONSERVATION-BIOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ecology\06-BIOGEOGRAPHY.md ecology\07-AQUATIC-ECOSYSTEMS.md ecology\08-DISTURBANCE-ECOLOGY.md ecology\09-CONSERVATION-BIOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

