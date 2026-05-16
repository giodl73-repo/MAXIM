---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `mineralogy/05-CARBONATES-PHOSPHATES.md`
- `geochemistry/02-ISOTOPE-SYSTEMS.md`
- `geochemistry/03-GEOCHRONOLOGY.md`
- `geochemistry/04-STABLE-ISOTOPE-PALEO.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
tables. Current Certified Gold requires diagnostic reader-task support with
caveats.

## Changes

| Guide | Repair |
|---|---|
| `mineralogy/05-CARBONATES-PHOSPHATES.md` | Rebuilt the table around calcite, dolomite, birefringence, fertilizer phosphate, bone, Moroccan reserves, and speleothem archives. |
| `geochemistry/02-ISOTOPE-SYSTEMS.md` | Rebuilt the table around epsilon Nd, Sm-Nd, oxygen isotopes, aluminum-26, strontium contamination, Hf-W, and boron pH. |
| `geochemistry/03-GEOCHRONOLOGY.md` | Rebuilt the table around zircon U-Pb, concordia/discordia, Ar-Ar, closure temperature, T-t paths, carbonate dating limits, radiocarbon, and disturbance ages. |
| `geochemistry/04-STABLE-ISOTOPE-PALEO.md` | Rebuilt the table around delta 18O, Mg/Ca deconvolution, GMWL, deuterium excess, PETM carbon, ice cores, CIEs, and boron pH limits. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- mineralogy\05-CARBONATES-PHOSPHATES.md geochemistry\02-ISOTOPE-SYSTEMS.md geochemistry\03-GEOCHRONOLOGY.md geochemistry\04-STABLE-ISOTOPE-PALEO.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml mineralogy\05-CARBONATES-PHOSPHATES.md geochemistry\02-ISOTOPE-SYSTEMS.md geochemistry\03-GEOCHRONOLOGY.md geochemistry\04-STABLE-ISOTOPE-PALEO.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

