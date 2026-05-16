---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `partial-differential-equations/01-CLASSIFICATION.md`
- `partial-differential-equations/02-FIRST-ORDER.md`
- `partial-differential-equations/03-WAVE-EQUATION.md`
- `partial-differential-equations/04-HEAT-EQUATION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but all four retained
factory-era question/situation selector tables without explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | Rebuilt the table around elliptic/parabolic/hyperbolic data, characteristics, domains of dependence, uniqueness, and weak formulations. |
| `partial-differential-equations/02-FIRST-ORDER.md` | Rebuilt the table around characteristics, shocks, entropy conditions, rarefactions, Hamilton-Jacobi theory, analytic existence, and Rankine-Hugoniot jumps. |
| `partial-differential-equations/03-WAVE-EQUATION.md` | Rebuilt the table around d'Alembert, Kirchhoff, Huygens, energy, modes, dispersion, solitons, and reflection. |
| `partial-differential-equations/04-HEAT-EQUATION.md` | Rebuilt the table around Gaussian kernels, diffusive scaling, eigenmode decay, backward ill-posedness, maximum principles, positivity, Black-Scholes, and Turing instability. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- partial-differential-equations\01-CLASSIFICATION.md partial-differential-equations\02-FIRST-ORDER.md partial-differential-equations\03-WAVE-EQUATION.md partial-differential-equations\04-HEAT-EQUATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml partial-differential-equations\01-CLASSIFICATION.md partial-differential-equations\02-FIRST-ORDER.md partial-differential-equations\03-WAVE-EQUATION.md partial-differential-equations\04-HEAT-EQUATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

