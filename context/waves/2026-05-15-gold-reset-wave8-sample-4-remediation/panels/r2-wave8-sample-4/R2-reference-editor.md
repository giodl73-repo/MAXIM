# R2 Reference Editor Panel - Gold Reset Wave 8 Sample 4

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `variational-calculus/07-DIRECT-METHODS.md` | `direct-methods-concept` | 4.6 |
| `variational-calculus/08-OPTIMAL-CONTROL.md` | `variational-optimal-control-landscape` | 4.6 |
| `variational-calculus/09-ML-CONNECTIONS.md` | `variational-ml-map` | 4.6 |
| `statistical-mechanics/06-RENORMALIZATION.md` | `renormalization-group-flow` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables in the variational guides were too lookup oriented. | Repaired into diagnostic `If you need to diagnose...` tables; renormalization already matched target form. |
| expert-skeptic | Variational and RG claims need caveats about boundary/function-space choice, nonconvex microstructure, recovery sequences, PMP necessity, HJB dimensionality, adjoint numerics, score estimation, fixed-point dependence, asymptotic epsilon expansions, and hyperscaling failure. | Added or preserved caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge direct methods, optimal control, ML variational formulations, and RG scaling. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `variational-calculus/07-DIRECT-METHODS.md` | Reader can diagnose existence arguments by separating coercivity, lower semicontinuity, quasiconvexity, bounded sequences, weak limits, relaxation, Gamma-convergence, and embeddings. |
| `variational-calculus/08-OPTIMAL-CONTROL.md` | Reader can diagnose control methods by separating E-L, PMP, LQR, HJB, adjoints, bang-bang control, Neural ODEs, and stochastic HJB. |
| `variational-calculus/09-ML-CONNECTIONS.md` | Reader can diagnose ML variational links by separating gradient flow, momentum, Neural ODEs, natural gradient, optimal transport, VAEs, mechanics-aware networks, diffusion, and implicit bias. |
| `statistical-mechanics/06-RENORMALIZATION.md` | Reader can diagnose RG claims by separating universality, fixed-point linearization, upper critical dimension, relevant perturbations, epsilon expansion, 1D Ising, QFT bridge, and scaling relations. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

