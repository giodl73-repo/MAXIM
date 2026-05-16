---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `archaeology/03-MATERIAL-ANALYSIS.md`
- `archaeology/04-PREHISTORY.md`
- `archaeology/05-ANCIENT-CIVILIZATIONS.md`
- `archaeology/06-CLASSICAL-ARCHAEOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
method-selector tables. Current Certified Gold requires diagnostic reader-task
support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `archaeology/03-MATERIAL-ANALYSIS.md` | Rebuilt the analysis-method selector around provenance, diet, mobility, kinship, residue, zooarchaeology, archaeobotany, paleoenvironment, and metal-source caveats. |
| `archaeology/04-PREHISTORY.md` | Rebuilt the prehistory method selector around pre-ceramic dating, aDNA, isotopic time windows, invention/diffusion, extinction chronology, exchange, and stage-label caveats. |
| `archaeology/05-ANCIENT-CIVILIZATIONS.md` | Rebuilt the civilization approach table around urbanism, text/material conflict, state formation, scripts, crop/technology spread, collapse, and value-language caveats. |
| `archaeology/06-CLASSICAL-ARCHAEOLOGY.md` | Rebuilt the classical archaeology selector around coins, epigraphy, sealed contexts, geophysics, wrecks, underwater formation, urban form, and source criticism caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- archaeology\03-MATERIAL-ANALYSIS.md archaeology\04-PREHISTORY.md archaeology\05-ANCIENT-CIVILIZATIONS.md archaeology\06-CLASSICAL-ARCHAEOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml archaeology\03-MATERIAL-ANALYSIS.md archaeology\04-PREHISTORY.md archaeology\05-ANCIENT-CIVILIZATIONS.md archaeology\06-CLASSICAL-ARCHAEOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

