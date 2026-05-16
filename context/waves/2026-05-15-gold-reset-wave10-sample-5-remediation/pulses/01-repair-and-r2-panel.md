---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `biophysics/04-MEMBRANE-BIOPHYSICS.md`
- `biophysics/05-HODGKIN-HUXLEY.md`
- `biophysics/06-MOLECULAR-MOTORS.md`
- `biophysics/07-SINGLE-MOLECULE.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/goal selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `biophysics/04-MEMBRANE-BIOPHYSICS.md` | Rebuilt the table around resting potential, Nernst voltage, lipid diffusion, K-channel selectivity, sodium exclusion, patch clamp, vesicle bending, and endocytic curvature. |
| `biophysics/05-HODGKIN-HUXLEY.md` | Rebuilt the table around upstroke, termination, repolarization, undershoot, refractory periods, passive spread, myelination, and ANN simplification. |
| `biophysics/06-MOLECULAR-MOTORS.md` | Rebuilt the table around kinesin, dynein, step size, ATP synthase, flagellar energy, processivity, stall force, and rotation evidence. |
| `biophysics/07-SINGLE-MOLECULE.md` | Rebuilt the table around optical tweezers, AFM, magnetic tweezers, smFRET, wide-field throughput, HS-AFM, calibration, and distance inference. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- biophysics\04-MEMBRANE-BIOPHYSICS.md biophysics\05-HODGKIN-HUXLEY.md biophysics\06-MOLECULAR-MOTORS.md biophysics\07-SINGLE-MOLECULE.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml biophysics\04-MEMBRANE-BIOPHYSICS.md biophysics\05-HODGKIN-HUXLEY.md biophysics\06-MOLECULAR-MOTORS.md biophysics\07-SINGLE-MOLECULE.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

