# R2 Reference Editor Panel - Gold Reset Wave 8 Sample 5

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `statistical-mechanics/07-ISING-MODELS.md` | `ising-model-landscape` | 4.6 |
| `statistical-mechanics/08-NON-EQUILIBRIUM.md` | `non-equilibrium-stat-mech-landscape` | 4.6 |
| `quantum-computing/02-ALGORITHMS.md` | `quantum-algorithm-landscape` | 4.6 |
| `quantum-computing/03-ERROR-CORRECTION.md` | `quantum-error-correction-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides already used the reset target diagnostic decision table rather than factory-era selector prose. | Confirmed the `If you need to diagnose...` tables and preserved the current guide text. |
| expert-skeptic | Statistical-mechanics and quantum-computing claims need caveats about dimensionality, exact solvability, finite-size scaling, detailed balance, noise models, oracle costs, condition numbers, thresholds, and hardware overhead. | Existing caveats were sufficient for diagnostic use and were verified during panel review. |
| bridge-builder | The guide bodies already bridge Ising/RG, non-equilibrium dynamics, quantum algorithm classes, and QEC implementation constraints. | Preserved bridges; cheat sheets route reader diagnosis rather than giving broad recommendations. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `statistical-mechanics/07-ISING-MODELS.md` | Reader can diagnose Ising-model claims by separating dimension, coupling assumptions, exactness, universality, finite-size behavior, RG interpretation, and computation. |
| `statistical-mechanics/08-NON-EQUILIBRIUM.md` | Reader can diagnose non-equilibrium systems by separating detailed-balance failure, stochastic dynamics, entropy production, driven steady states, fluctuation theorems, glassiness, and active matter. |
| `quantum-computing/02-ALGORITHMS.md` | Reader can diagnose quantum-algorithm fit by separating Shor/Grover/simulation/phase-estimation structure, oracle assumptions, HHL conditioning, NISQ limits, and fault-tolerance requirements. |
| `quantum-computing/03-ERROR-CORRECTION.md` | Reader can diagnose QEC claims by separating stabilizer logic, syndrome extraction, surface-code thresholds, logical operators, magic-state overhead, erasures, and hardware constraints. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era confirmation,
proof/Da Vinci validation, and guide-specific reader-task review.

