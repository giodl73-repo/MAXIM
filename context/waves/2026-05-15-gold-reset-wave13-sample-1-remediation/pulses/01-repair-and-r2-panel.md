---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `botany/02-ROOTS-SOILS.md`
- `botany/03-STEMS-WOOD.md`
- `botany/04-LEAVES-PHOTOSYNTHESIS.md`
- `botany/05-FLOWERS-REPRODUCTION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/answer selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `botany/02-ROOTS-SOILS.md` | Rebuilt the roots/soils table around root architecture, water uptake, phosphorus limitation, arbuscular mycorrhizae, rhizosphere activity, and network claims. |
| `botany/03-STEMS-WOOD.md` | Rebuilt the stems/wood table around cambial growth, grass/tree differences, sapwood, hardness, crossdating, chronology depth, and porous wood anatomy. |
| `botany/04-LEAVES-PHOTOSYNTHESIS.md` | Rebuilt the leaves/photosynthesis table around photorespiration, C4, CAM, maize/wheat productivity, stomata, ABA, and O2 origin. |
| `botany/05-FLOWERS-REPRODUCTION.md` | Rebuilt the flowers/reproduction table around double fertilization, endosperm, orchids, wind dispersal, megafaunal dispersal, apomixis, and burdock biomimicry. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- botany\02-ROOTS-SOILS.md botany\03-STEMS-WOOD.md botany\04-LEAVES-PHOTOSYNTHESIS.md botany\05-FLOWERS-REPRODUCTION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml botany\02-ROOTS-SOILS.md botany\03-STEMS-WOOD.md botany\04-LEAVES-PHOTOSYNTHESIS.md botany\05-FLOWERS-REPRODUCTION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

