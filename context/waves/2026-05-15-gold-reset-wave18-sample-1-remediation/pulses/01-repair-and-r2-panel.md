---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `epigraphy/01-ANCIENT-NEAR-EAST.md`
- `epigraphy/02-GREEK-LATIN.md`
- `epigraphy/04-DECIPHERMENT.md`
- `epigraphy/05-RUNIC.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
script, inscription, case, and term selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `epigraphy/01-ANCIENT-NEAR-EAST.md` | Rebuilt the script table around administrative writing, Sumerian/Akkadian cuneiform, Ugaritic, Old Persian, and survival bias diagnostics. |
| `epigraphy/02-GREEK-LATIN.md` | Rebuilt the inscription table around honorific, votive, funerary, milestone, electoral, diploma, and official-document diagnostics. |
| `epigraphy/04-DECIPHERMENT.md` | Rebuilt the decipherment table around Rosetta, Behistun, Linear B, Ugaritic, Maya, bilinguals, and partial-decipherment diagnostics. |
| `epigraphy/05-RUNIC.md` | Rebuilt the runic table around Elder Futhark, Younger Futhark, Futhorc, aettir, bind runes, carvers, directionality, and modern myths. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- epigraphy\01-ANCIENT-NEAR-EAST.md epigraphy\02-GREEK-LATIN.md epigraphy\04-DECIPHERMENT.md epigraphy\05-RUNIC.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml epigraphy\01-ANCIENT-NEAR-EAST.md epigraphy\02-GREEK-LATIN.md epigraphy\04-DECIPHERMENT.md epigraphy\05-RUNIC.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

