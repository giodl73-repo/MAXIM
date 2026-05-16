---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `evolutionary-biology/07-SEXUAL-SELECTION.md`
- `evolutionary-biology/08-COEVOLUTION.md`
- `evolutionary-biology/09-MACROEVOLUTION.md`
- `virology/01-VIRUS-STRUCTURE.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/scenario selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `evolutionary-biology/07-SEXUAL-SELECTION.md` | Rebuilt the table around ornaments, choosiness, honesty, sperm competition, senescence, kin selection, and life history. |
| `evolutionary-biology/08-COEVOLUTION.md` | Rebuilt the table around toxin resistance, Red Queen dynamics, MHC diversity, virulence, cospeciation, and pollinator matching. |
| `evolutionary-biology/09-MACROEVOLUTION.md` | Rebuilt the table around K-Pg extinction, tempo, extinction survival, clade size trends, first appearance, and rapid radiation. |
| `virology/01-VIRUS-STRUCTURE.md` | Rebuilt the table around capsid geometry, triangulation, envelope fragility, RNA genome limits, segmentation, and host range. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- evolutionary-biology\07-SEXUAL-SELECTION.md evolutionary-biology\08-COEVOLUTION.md evolutionary-biology\09-MACROEVOLUTION.md virology\01-VIRUS-STRUCTURE.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml evolutionary-biology\07-SEXUAL-SELECTION.md evolutionary-biology\08-COEVOLUTION.md evolutionary-biology\09-MACROEVOLUTION.md virology\01-VIRUS-STRUCTURE.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

