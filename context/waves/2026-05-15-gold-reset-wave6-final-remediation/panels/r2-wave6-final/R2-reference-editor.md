# R2 Reference Editor Panel - Gold Reset Wave 6 Final

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `partial-differential-equations/09-NUMERICAL-PDES.md` | `numerical-pde-methods-landscape` | 4.6 |
| `variational-calculus/01-FUNCTIONALS.md` | `functionals-vs-functions` | 4.6 |
| `variational-calculus/02-EULER-LAGRANGE.md` | `euler-lagrange-equation` | 4.6 |
| `variational-calculus/03-CONSTRAINTS.md` | `constrained-variation` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained problem/concept/situation selector tables without explicit caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Numerical PDE and variational claims need caveats about geometry, mesh quality, stability, solver costs, aliasing, function-space choice, endpoint constraints, sufficiency, higher-order boundary data, and multiplier validity. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge numerical PDE methods and variational foundations. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `partial-differential-equations/09-NUMERICAL-PDES.md` | Reader can diagnose numerical PDE methods by separating geometry, stiffness, CFL, shocks, spectral smoothness, infinite domains, and solver structure. |
| `variational-calculus/01-FUNCTIONALS.md` | Reader can diagnose functional claims by separating function space, admissible perturbations, first/second variation, variational derivative, natural BCs, and Legendre checks. |
| `variational-calculus/02-EULER-LAGRANGE.md` | Reader can diagnose E-L claims by separating standard, Beltrami, coupled, multidimensional, higher-order, free-endpoint, and sufficiency cases. |
| `variational-calculus/03-CONSTRAINTS.md` | Reader can diagnose constrained variation by separating scalar, pointwise, holonomic, nonholonomic, eigenvalue, penalty, and augmented-Lagrangian constraints. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

