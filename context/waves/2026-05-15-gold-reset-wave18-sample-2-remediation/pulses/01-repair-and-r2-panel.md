---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `epigraphy/06-MESOAMERICAN.md`
- `epigraphy/07-INDUS-UNDECIPHERED.md`
- `epigraphy/08-MEDIEVAL.md`
- `epigraphy/09-MODERN-METHODS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
system, script, formula, and method selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `epigraphy/06-MESOAMERICAN.md` | Rebuilt the Mesoamerican table around Maya, Aztec, Zapotec, Olmec, calendars, codices, accession formulae, and phonetic breakthrough diagnostics. |
| `epigraphy/07-INDUS-UNDECIPHERED.md` | Rebuilt the undeciphered-scripts table around Proto-Elamite, Indus, Linear A, Rongorongo, Voynich, non-writing arguments, and short-corpus limits. |
| `epigraphy/08-MEDIEVAL.md` | Rebuilt the medieval table around tomb, memorial, funerary, intercessory, royal, dedication, mason-mark, and graffiti diagnostics. |
| `epigraphy/09-MODERN-METHODS.md` | Rebuilt the methods table around RTI, photogrammetry, multispectral imaging, structured light, LiDAR, squeezes, databases, and AI assistance. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- epigraphy\06-MESOAMERICAN.md epigraphy\07-INDUS-UNDECIPHERED.md epigraphy\08-MEDIEVAL.md epigraphy\09-MODERN-METHODS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml epigraphy\06-MESOAMERICAN.md epigraphy\07-INDUS-UNDECIPHERED.md epigraphy\08-MEDIEVAL.md epigraphy\09-MODERN-METHODS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

