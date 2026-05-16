---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the third Wave 36 reset sample:

- `furniture/00-OVERVIEW.md`
- `furniture/01-WOOD-JOINERY.md`
- `furniture/02-HISTORY-STYLES.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml furniture\00-OVERVIEW.md furniture\01-WOOD-JOINERY.md furniture\02-HISTORY-STYLES.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
still found lookup-style decision support, a wood-movement inconsistency, and
several historical/engineering overclaims that were not acceptable for Gold.

## Changes

| Guide | Repair |
|---|---|
| `furniture/00-OVERVIEW.md` | Rebuilt the cheat sheet around diagnostic furniture questions; corrected the Thonet shipping and Bauhaus/Eames aircraft-tooling framing. |
| `furniture/01-WOOD-JOINERY.md` | Corrected the seasonal movement rule and aligned the EMC example with flatsawn/tangential oak. |
| `furniture/02-HISTORY-STYLES.md` | Corrected Egyptian folding-stool/chest language, softened sabre-leg and cabriole-origin overclaims, and rebuilt the cheat sheet as a style-diagnosis table. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- furniture\00-OVERVIEW.md furniture\01-WOOD-JOINERY.md furniture\02-HISTORY-STYLES.md
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml furniture\00-OVERVIEW.md furniture\01-WOOD-JOINERY.md furniture\02-HISTORY-STYLES.md | Tee-Object -Variable proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

