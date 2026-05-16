---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `partial-differential-equations/09-NUMERICAL-PDES.md`
- `variational-calculus/01-FUNCTIONALS.md`
- `variational-calculus/02-EULER-LAGRANGE.md`
- `variational-calculus/03-CONSTRAINTS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but all four retained
factory-era problem/concept/situation selector tables without explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `partial-differential-equations/09-NUMERICAL-PDES.md` | Rebuilt the table around finite differences, FEM/AMG, implicit heat solvers, leapfrog/CFL, finite volume, spectral methods, BEM/FMM, and multigrid. |
| `variational-calculus/01-FUNCTIONALS.md` | Rebuilt the table around functionals, admissible variations, first/second variations, variational derivative, natural BCs, and Legendre conditions. |
| `variational-calculus/02-EULER-LAGRANGE.md` | Rebuilt the table around standard E-L, Beltrami identity, multiple functions, multidimensional domains, higher derivatives, natural BCs, and local minimum checks. |
| `variational-calculus/03-CONSTRAINTS.md` | Rebuilt the table around isoperimetric, pointwise, holonomic, nonholonomic, eigenvalue, penalty, and augmented-Lagrangian constraints. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- partial-differential-equations\09-NUMERICAL-PDES.md variational-calculus\01-FUNCTIONALS.md variational-calculus\02-EULER-LAGRANGE.md variational-calculus\03-CONSTRAINTS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml partial-differential-equations\09-NUMERICAL-PDES.md variational-calculus\01-FUNCTIONALS.md variational-calculus\02-EULER-LAGRANGE.md variational-calculus\03-CONSTRAINTS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

