# R2 Reference Editor Panel - Gold Reset Wave 3 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `topology/01-METRIC-SPACES.md` | `metric-spaces-concrete-foundation` | 4.6 |
| `topology/02-TOPOLOGICAL-SPACES.md` | `topological-spaces-framework` | 4.6 |
| `topology/03-CONTINUITY-HOMEOMORPHISM.md` | `topological-maps-hierarchy` | 4.6 |
| `topology/04-COMPACTNESS.md` | `compactness-finite-cover` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained task/tool selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Topology claims need caveats about metric dependence, completion, metrizability hypotheses, quotient separation, compact-Hausdorff shortcuts, invariant incompleteness, sequential compactness, and infinite-dimensional failures. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge metric spaces, topological spaces, maps, and compactness. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `topology/01-METRIC-SPACES.md` | Reader can diagnose metric-space claims by separating continuity, convergence, completeness, fixed-point hypotheses, metric equivalence, and compactness regimes. |
| `topology/02-TOPOLOGICAL-SPACES.md` | Reader can diagnose topology claims by separating open-set continuity, generated topology, quotient/product construction, separation, metric validity, and metrizability. |
| `topology/03-CONTINUITY-HOMEOMORPHISM.md` | Reader can diagnose map-equivalence claims by separating continuity, homeomorphism, compact-Hausdorff shortcuts, invariants, homotopy equivalence, and dimension invariance. |
| `topology/04-COMPACTNESS.md` | Reader can diagnose compactness claims by separating cover compactness, Euclidean compactness, extrema, uniform continuity, function-family compactness, operators, products, and Banach-space failures. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

