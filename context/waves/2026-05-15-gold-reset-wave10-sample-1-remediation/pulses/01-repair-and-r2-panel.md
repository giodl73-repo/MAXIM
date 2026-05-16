---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `evolutionary-biology/02-POPULATION-GENETICS.md`
- `evolutionary-biology/04-SPECIATION.md`
- `evolutionary-biology/05-PHYLOGENETICS.md`
- `evolutionary-biology/06-EVO-DEVO.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/task/situation selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `evolutionary-biology/02-POPULATION-GENETICS.md` | Rebuilt the table around Hardy-Weinberg departure, drift, selection versus drift, F_ST, migration, coalescent time, and SNP prediction caveats. |
| `evolutionary-biology/04-SPECIATION.md` | Rebuilt the table around island colonization, vicariance, host shifts, polyploidy, hybrid zones, and lake radiations. |
| `evolutionary-biology/05-PHYLOGENETICS.md` | Rebuilt the table around exploratory trees, ML models, clock dating, species trees, ancient divergence, ARG inference, and ancestral-state reconstruction. |
| `evolutionary-biology/06-EVO-DEVO.md` | Rebuilt the table around HOX colinearity, deep homology, cis-regulatory change, heterochrony, convergence, and modularity. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- evolutionary-biology\02-POPULATION-GENETICS.md evolutionary-biology\04-SPECIATION.md evolutionary-biology\05-PHYLOGENETICS.md evolutionary-biology\06-EVO-DEVO.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml evolutionary-biology\02-POPULATION-GENETICS.md evolutionary-biology\04-SPECIATION.md evolutionary-biology\05-PHYLOGENETICS.md evolutionary-biology\06-EVO-DEVO.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

