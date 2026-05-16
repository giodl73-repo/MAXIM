---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `computing/28-CONCURRENCY.md`
- `construction-materials/01-PREHISTORIC-VERNACULAR.md`
- `construction-materials/02-ANCIENT-MASONRY.md`
- `construction-materials/03-MEDIEVAL-TIMBER.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but their cheat sheets were
answer keys or direct selectors. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `computing/28-CONCURRENCY.md` | Converted the concurrency solution list into a diagnostic table covering locks, fairness, read/write patterns, STM, lock-free structures, async, CPU pools, actors, channels, distributed state, reclamation, Rust, structured concurrency, and memory ordering. |
| `construction-materials/01-PREHISTORIC-VERNACULAR.md` | Converted vernacular material choices into diagnostic climate, labor, breathability, dry-stone, mortar, span, thatch, and wattle caveats. |
| `construction-materials/02-ANCIENT-MASONRY.md` | Converted masonry answers into diagnostic arch, thrust, Roman concrete, oculus, stone, mortar, frost, barrel-vault, and cross-vault caveats. |
| `construction-materials/03-MEDIEVAL-TIMBER.md` | Converted medieval timber and lime answers into diagnostic hydraulic lime, repointing, buttress, king-post, hammer-beam, fan-vault, green-oak, infill, and bird's-mouth caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- computing\28-CONCURRENCY.md construction-materials\01-PREHISTORIC-VERNACULAR.md construction-materials\02-ANCIENT-MASONRY.md construction-materials\03-MEDIEVAL-TIMBER.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml computing\28-CONCURRENCY.md construction-materials\01-PREHISTORIC-VERNACULAR.md construction-materials\02-ANCIENT-MASONRY.md construction-materials\03-MEDIEVAL-TIMBER.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

