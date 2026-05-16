# R2 Consolidated Panel - Gold Reset Wave 6 Sample 2

## Verdict

PASS. The Wave 6 Laplace/Poisson, Fourier methods, Green's functions, and
variational weak-form sample satisfies Gold Rubric v2 after targeted repair,
proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | 4.6 | `laplace-poisson-landscape` | Certified Gold |
| `partial-differential-equations/06-FOURIER-METHODS.md` | 4.6 | `fourier-methods-pde-landscape` | Certified Gold |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | 4.6 | `greens-function-concept` | Certified Gold |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | 4.6 | `weak-formulation-concept` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: use/problem/question selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | Diagnose elliptic-method claims by separating domain geometry, BCs, Green/Poisson kernels, uniqueness principles, and multipole structure. | PASS |
| `partial-differential-equations/06-FOURIER-METHODS.md` | Diagnose Fourier/spectral-method claims by separating geometry, boundary conditions, transform family, periodicity, radial bases, and convergence. | PASS |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | Diagnose Green's-function claims by separating free-space, boundary, heat, wave, spectral, and Duhamel settings. | PASS |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | Diagnose weak-form claims by separating spaces, traces, bilinear forms, coercivity, matrix properties, FEM rates, and entropy conditions. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

