---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `partial-differential-equations/05-LAPLACE-POISSON.md`
- `partial-differential-equations/06-FOURIER-METHODS.md`
- `partial-differential-equations/07-GREENS-FUNCTIONS.md`
- `partial-differential-equations/08-VARIATIONAL-WEAK.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but all four retained
factory-era use/problem/question selector tables without explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | Rebuilt the table around separation, spherical harmonics, images, Green's functions, Poisson kernels, uniqueness, harmonic extension, and multipoles. |
| `partial-differential-equations/06-FOURIER-METHODS.md` | Rebuilt the table around domain geometry, boundary conditions, Fourier/Bessel/spherical bases, transforms, periodicity, and Chebyshev expansions. |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | Rebuilt the table around free-space kernels, images, Kelvin inversion, heat/wave causality, bounded-domain spectra, and Duhamel's principle. |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | Rebuilt the table around weak formulation, trace spaces, stiffness matrices, symmetry, coercivity, FEM error, conservation-law entropy, Poincare, and Lax-Milgram. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- partial-differential-equations\05-LAPLACE-POISSON.md partial-differential-equations\06-FOURIER-METHODS.md partial-differential-equations\07-GREENS-FUNCTIONS.md partial-differential-equations\08-VARIATIONAL-WEAK.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml partial-differential-equations\05-LAPLACE-POISSON.md partial-differential-equations\06-FOURIER-METHODS.md partial-differential-equations\07-GREENS-FUNCTIONS.md partial-differential-equations\08-VARIATIONAL-WEAK.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

