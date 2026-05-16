# R2 Reference Editor Panel - Gold Reset Wave 4 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `information-theory/08-QUANTUM-INFORMATION.md` | `quantum-vs-classical-information` | 4.6 |
| `information-theory/09-INFORMATION-GEOMETRY.md` | `information-geometry-statistics` | 4.6 |
| `number-theory/06-ALGEBRAIC-NUMBER-THEORY.md` | `algebraic-number-theory-factorization` | 4.6 |
| `number-theory/09-COMPUTATIONAL-NUMBER-THEORY.md` | `computational-number-theory-complexity` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Claims need caveats about resource models, regularization, KL direction, transport metrics, field-specific formulas, discriminants, ideal factorization, cryptographic parameters, probabilistic runtimes, and side-channel-safe implementation. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge quantum/classical information, statistical geometry, algebraic number theory, and computational arithmetic. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `information-theory/08-QUANTUM-INFORMATION.md` | Reader can diagnose quantum-information claims by separating state entropy, total correlation, entanglement, coherent information, Holevo bounds, quantum capacity, and entanglement-assisted resources. |
| `information-theory/09-INFORMATION-GEOMETRY.md` | Reader can diagnose information-geometry claims by separating Fisher-Rao, KL direction, symmetric divergence, Wasserstein, natural gradient, K-FAC, EM, Sinkhorn, and bottleneck objectives. |
| `number-theory/06-ALGEBRAIC-NUMBER-THEORY.md` | Reader can diagnose algebraic-number-theory claims by separating rings of integers, splitting, norms, units, class number, PID status, class group, and ideal-lattice crypto assumptions. |
| `number-theory/09-COMPUTATIONAL-NUMBER-THEORY.md` | Reader can diagnose computational-number-theory claims by separating gcd/inverse/power primitives, primality, factor-size-dependent algorithms, NFS, and sieving. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

