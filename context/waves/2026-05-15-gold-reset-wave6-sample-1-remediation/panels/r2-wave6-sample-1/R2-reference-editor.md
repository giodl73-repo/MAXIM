# R2 Reference Editor Panel - Gold Reset Wave 6 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `partial-differential-equations/01-CLASSIFICATION.md` | `pde-classification-determines` | 4.6 |
| `partial-differential-equations/02-FIRST-ORDER.md` | `first-order-pde-taxonomy` | 4.6 |
| `partial-differential-equations/03-WAVE-EQUATION.md` | `wave-equation-landscape` | 4.6 |
| `partial-differential-equations/04-HEAT-EQUATION.md` | `heat-equation-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four PDE guides retained question/situation selector tables without explicit caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | PDE claims need caveats about ill-posed data, characteristic crossing, entropy selection, Huygens dimension dependence, boundary flux, backward heat instability, and modeling assumptions. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge classification, characteristics, wave propagation, and diffusion. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | Reader can diagnose PDE type by separating boundary/initial data, characteristics, domains of dependence, energy uniqueness, and weak formulations. |
| `partial-differential-equations/02-FIRST-ORDER.md` | Reader can diagnose first-order PDE claims by separating characteristics, shocks, entropy conditions, rarefactions, Hamilton-Jacobi solutions, and conservation-law jumps. |
| `partial-differential-equations/03-WAVE-EQUATION.md` | Reader can diagnose wave-equation claims by separating traveling waves, Huygens behavior, energy, standing modes, dispersion, solitons, and reflection. |
| `partial-differential-equations/04-HEAT-EQUATION.md` | Reader can diagnose heat-equation claims by separating kernels, scaling, eigenmodes, backward ill-posedness, maximum principles, positivity, and reaction-diffusion effects. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

