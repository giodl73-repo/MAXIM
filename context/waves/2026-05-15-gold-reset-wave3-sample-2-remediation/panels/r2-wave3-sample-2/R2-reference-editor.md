# R2 Reference Editor Panel - Gold Reset Wave 3 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `topology/05-CONNECTEDNESS.md` | `connectedness-hierarchy` | 4.6 |
| `topology/06-FUNDAMENTAL-GROUP.md` | `fundamental-group-loops` | 4.6 |
| `topology/08-COHOMOLOGY.md` | `cohomology-dual-ring-structure` | 4.6 |
| `topology/09-MANIFOLDS.md` | `manifolds-locally-euclidean` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained task/tool selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Topology claims need caveats about connected versus path-connected, simply connected hypotheses, covering-space conditions, normal covers, UCT torsion, duality hypotheses, orientability, smooth-manifold axioms, and dimension-sensitive exotic smoothness. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge connectedness, fundamental groups, cohomology, and manifolds. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `topology/05-CONNECTEDNESS.md` | Reader can diagnose connectedness claims by separating clopen partitions, paths, simple connectedness, IVT, winding, `H_0`, Jordan separation, and universal covers. |
| `topology/06-FUNDAMENTAL-GROUP.md` | Reader can diagnose `pi_1` claims by separating homotopy equivalence, van Kampen, covering classification, deck groups, no-retraction arguments, lifts, branch cuts, and surface presentations. |
| `topology/08-COHOMOLOGY.md` | Reader can diagnose cohomology claims by separating UCT, ring structure, de Rham, periods, duality, orientability, characteristic classes, spectral sequences, and Gauss-Bonnet. |
| `topology/09-MANIFOLDS.md` | Reader can diagnose manifold claims by separating smooth axioms, surface classification, exotic smoothness, tangent bundles, handles, curvature-topology, vector fields, geometrization, and 4D invariants. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

