---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `biophysics/08-STOCHASTIC-BIO.md`
- `biophysics/09-ALPHAFOLD-ERA.md`
- `pharmacology/01-RECEPTOR-THEORY.md`
- `pharmacology/02-PHARMACOKINETICS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/parameter selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `biophysics/08-STOCHASTIC-BIO.md` | Rebuilt the table around copy-number noise, Langevin dynamics, Poisson assumptions, bursting, Jarzynski, Crooks, second-law logic, and two-reporter noise. |
| `biophysics/09-ALPHAFOLD-ERA.md` | Rebuilt the table around AF2 input, triangular updates, pLDDT, database coverage, drug-binding limits, ESMFold, RFdiffusion, and AF3. |
| `pharmacology/01-RECEPTOR-THEORY.md` | Rebuilt the table around affinity, occupancy, Emax, competitive/noncompetitive antagonism, tolerance, and withdrawal rebound. |
| `pharmacology/02-PHARMACOKINETICS.md` | Rebuilt the table around half-life, Vd, clearance, bioavailability, steady state, loading dose, hepatic impairment, and renal impairment. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- biophysics\08-STOCHASTIC-BIO.md biophysics\09-ALPHAFOLD-ERA.md pharmacology\01-RECEPTOR-THEORY.md pharmacology\02-PHARMACOKINETICS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml biophysics\08-STOCHASTIC-BIO.md biophysics\09-ALPHAFOLD-ERA.md pharmacology\01-RECEPTOR-THEORY.md pharmacology\02-PHARMACOKINETICS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

