---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `statistical-mechanics/08-NON-EQUILIBRIUM.md`
- `lie-groups/01-MATRIX-GROUPS.md`
- `lie-groups/02-LIE-ALGEBRAS.md`
- `differential-geometry/03-DIFFERENTIAL-FORMS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
tool, group, concept, and object selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `statistical-mechanics/08-NON-EQUILIBRIUM.md` | Rebuilt the tool table around Langevin, Fokker-Planck, FDT, diffusion, Kubo, Jarzynski, Crooks, second-law, and master-equation caveats. |
| `lie-groups/01-MATRIX-GROUPS.md` | Rebuilt the group selector around GL, SL, SO, O, U, SU, gauge groups, SE, symplectic, and Lorentz/spinor groups. |
| `lie-groups/02-LIE-ALGEBRAS.md` | Rebuilt the concept table around tangent algebras, brackets, exponential map, one-parameter subgroups, BCH, adjoint action, and Killing form. |
| `differential-geometry/03-DIFFERENTIAL-FORMS.md` | Rebuilt the object/operation table around forms, wedge, exterior derivative, interior product, Lie derivative, Stokes, closed/exact forms, cohomology, and Hodge star. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- statistical-mechanics\08-NON-EQUILIBRIUM.md lie-groups\01-MATRIX-GROUPS.md lie-groups\02-LIE-ALGEBRAS.md differential-geometry\03-DIFFERENTIAL-FORMS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml statistical-mechanics\08-NON-EQUILIBRIUM.md lie-groups\01-MATRIX-GROUPS.md lie-groups\02-LIE-ALGEBRAS.md differential-geometry\03-DIFFERENTIAL-FORMS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

