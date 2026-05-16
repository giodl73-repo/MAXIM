# R2 Reference Editor Panel - Gold Reset Wave 6 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | `laplace-poisson-landscape` | 4.6 |
| `partial-differential-equations/06-FOURIER-METHODS.md` | `fourier-methods-pde-landscape` | 4.6 |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | `greens-function-concept` | 4.6 |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | `weak-formulation-concept` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four PDE guides retained use/problem/question selector tables without explicit caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | PDE method claims need caveats about boundary conditions, domain geometry, zero modes, spectral convergence, free-space versus bounded-domain kernels, causality, weak regularity, coercivity, and entropy conditions. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge elliptic methods, Fourier/spectral tools, Green's functions, and weak/FEM formulations. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | Reader can diagnose elliptic solution methods by separating separation, spherical harmonics, images, Green's functions, Poisson kernels, uniqueness, harmonic extension, and multipoles. |
| `partial-differential-equations/06-FOURIER-METHODS.md` | Reader can diagnose spectral-method fit by separating geometry, BCs, transform type, periodicity, radial/spherical bases, and endpoint behavior. |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | Reader can diagnose Green's-function claims by separating free-space kernels, image methods, heat/wave causality, bounded-domain spectra, and Duhamel accumulation. |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | Reader can diagnose weak-form claims by separating function spaces, trace conditions, bilinear forms, stiffness matrices, coercivity, FEM error, entropy, Poincare, and Lax-Milgram. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

