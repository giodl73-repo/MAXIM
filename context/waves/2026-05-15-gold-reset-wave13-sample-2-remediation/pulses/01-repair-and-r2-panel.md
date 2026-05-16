---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `botany/06-TREES-FORESTS.md`
- `botany/07-BIOMES.md`
- `botany/08-PLANT-DEFENSES.md`
- `botany/09-ECONOMIC-BOTANY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/answer selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `botany/06-TREES-FORESTS.md` | Rebuilt the trees/forests table around understory light, disturbance, old growth, serotiny, clonal organisms, and climax-theory limits. |
| `botany/07-BIOMES.md` | Rebuilt the biomes table around rainforest soils, leaf drop, carbon storage, Mediterranean diversity, grassland maintenance, and Amazon tipping risk. |
| `botany/08-PLANT-DEFENSES.md` | Rebuilt the plant-defenses table around caffeine, sulforaphane, myrosinase, artemisinin, tannins, and herbivory arms races. |
| `botany/09-ECONOMIC-BOTANY.md` | Rebuilt the economic-botany table around Janka hardness, instrument wood, aspirin, quinine, Taxol, natural rubber, and synthetic alizarin. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- botany\06-TREES-FORESTS.md botany\07-BIOMES.md botany\08-PLANT-DEFENSES.md botany\09-ECONOMIC-BOTANY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml botany\06-TREES-FORESTS.md botany\07-BIOMES.md botany\08-PLANT-DEFENSES.md botany\09-ECONOMIC-BOTANY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

