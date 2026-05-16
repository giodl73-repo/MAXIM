---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `genomics/01-SEQUENCING-TECH.md`
- `genomics/02-GENOME-ASSEMBLY.md`
- `genomics/09-PERSONALIZED-MEDICINE.md`
- `immunology/02-ADAPTIVE-IMMUNITY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
goal/scenario/question selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `genomics/01-SEQUENCING-TECH.md` | Rebuilt the table around population-scale variants, validation, de novo assembly, structural variants, field sequencing, methylation, single-cell, spatial expression, T2T, and RNA-seq. |
| `genomics/02-GENOME-ASSEMBLY.md` | Rebuilt the table around mapping, de novo assembly, SVs, chromosome-scale assembly, T2T, phasing, quality, and pangenomes. |
| `genomics/09-PERSONALIZED-MEDICINE.md` | Rebuilt the table around rare disease, cancer risk, NSCLC, ctDNA, PGx, warfarin, abacavir, NIPT, PGT, cancer screening, WGS, and immunotherapy biomarkers. |
| `immunology/02-ADAPTIVE-IMMUNITY.md` | Rebuilt the table around B/T-cell maturation, central tolerance, MHC restriction, costimulation, cross-presentation, affinity maturation, AID, anergy, and CTLA-4. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- genomics\01-SEQUENCING-TECH.md genomics\02-GENOME-ASSEMBLY.md genomics\09-PERSONALIZED-MEDICINE.md immunology\02-ADAPTIVE-IMMUNITY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml genomics\01-SEQUENCING-TECH.md genomics\02-GENOME-ASSEMBLY.md genomics\09-PERSONALIZED-MEDICINE.md immunology\02-ADAPTIVE-IMMUNITY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

