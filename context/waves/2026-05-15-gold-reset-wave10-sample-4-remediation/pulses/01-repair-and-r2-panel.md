---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `virology/09-APPLICATIONS.md`
- `biophysics/01-THERMODYNAMICS-BIO.md`
- `biophysics/02-PROTEIN-FOLDING.md`
- `biophysics/03-STRUCTURAL-METHODS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
application/question/situation selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `virology/09-APPLICATIONS.md` | Rebuilt the table around AAV, lentiviral, mRNA, adenoviral, phage, oncolytic, and phage-display applications. |
| `biophysics/01-THERMODYNAMICS-BIO.md` | Rebuilt the table around spontaneity, Boltzmann ratios, ATP energy, NESS collapse, folding thermodynamics, drug affinity, proton-motive force, hydrophobic burial, and ITC. |
| `biophysics/02-PROTEIN-FOLDING.md` | Rebuilt the table around energy funnels, kinetics, equilibrium, chaperonins, prions, amyloid stability, AlphaFold2 scope, and AlphaFold2 limits. |
| `biophysics/03-STRUCTURAL-METHODS.md` | Rebuilt the table around X-ray, NMR, cryo-EM, solution conformation, heterogeneity, IDPs, drug-site mapping, and phasing. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- virology\09-APPLICATIONS.md biophysics\01-THERMODYNAMICS-BIO.md biophysics\02-PROTEIN-FOLDING.md biophysics\03-STRUCTURAL-METHODS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml virology\09-APPLICATIONS.md biophysics\01-THERMODYNAMICS-BIO.md biophysics\02-PROTEIN-FOLDING.md biophysics\03-STRUCTURAL-METHODS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

