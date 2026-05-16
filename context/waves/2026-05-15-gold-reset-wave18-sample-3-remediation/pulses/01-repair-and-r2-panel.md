---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `historiography/01-ANCIENT-MEDIEVAL.md`
- `historiography/02-ENLIGHTENMENT.md`
- `historiography/03-RANKEAN-POSITIVISM.md`
- `historiography/04-ANNALES-SCHOOL.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
historian, thinker, concept, and Annales selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `historiography/01-ANCIENT-MEDIEVAL.md` | Rebuilt the historian table around Herodotus, Thucydides, Polybius, Livy, Sima Qian, Bede, and Ibn Khaldun diagnostics. |
| `historiography/02-ENLIGHTENMENT.md` | Rebuilt the Enlightenment table around Voltaire, Gibbon, Hume, Vico, Herder, and stadialism diagnostics. |
| `historiography/03-RANKEAN-POSITIVISM.md` | Rebuilt the Rankean table around archives, source criticism, historicism, detachment, state narrative, seminar model, and formula misreadings. |
| `historiography/04-ANNALES-SCHOOL.md` | Rebuilt the Annales table around longue duree, environmental constraint, conjunctures, mentalites, serial history, memory sites, and school diversity. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- historiography\01-ANCIENT-MEDIEVAL.md historiography\02-ENLIGHTENMENT.md historiography\03-RANKEAN-POSITIVISM.md historiography\04-ANNALES-SCHOOL.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml historiography\01-ANCIENT-MEDIEVAL.md historiography\02-ENLIGHTENMENT.md historiography\03-RANKEAN-POSITIVISM.md historiography\04-ANNALES-SCHOOL.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

