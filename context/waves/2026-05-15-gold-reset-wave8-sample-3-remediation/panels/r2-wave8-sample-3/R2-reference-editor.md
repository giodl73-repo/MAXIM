# R2 Reference Editor Panel - Gold Reset Wave 8 Sample 3

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `control-theory/09-LEARNING-BASED-CONTROL.md` | `learning-based-control-spectrum` | 4.6 |
| `variational-calculus/04-LAGRANGIAN-MECHANICS.md` | `lagrangian-mechanics-architecture` | 4.6 |
| `variational-calculus/05-HAMILTONIAN-MECHANICS.md` | `lagrangian-vs-hamiltonian` | 4.6 |
| `variational-calculus/06-SECOND-VARIATION.md` | `first-second-variation` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables were too advice/list oriented. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | Control and variational claims need caveats about excitation coverage, sim-to-real gaps, uncertainty propagation, safety-filter assumptions, persistent excitation, nonholonomic constraints, canonical versus mechanical momentum, singular Legendre transforms, noncanonical coordinates, local versus global minima, and endpoint hypotheses. | Added caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge learning-based control with Lagrangian/Hamiltonian and second-variation mechanics. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `control-theory/09-LEARNING-BASED-CONTROL.md` | Reader can diagnose learning-based control by separating known-model control, system ID, model-free RL, model-based RL, demonstrations, safety, offline RL, and DeePC. |
| `variational-calculus/04-LAGRANGIAN-MECHANICS.md` | Reader can diagnose Lagrangian setups by separating forces, cyclic coordinates, constraints, EM fields, rigid bodies, fields, and Noether symmetries. |
| `variational-calculus/05-HAMILTONIAN-MECHANICS.md` | Reader can diagnose Hamiltonian mechanics by separating transform validity, equations, brackets, conservation, volume, integrability, H-J, and quantization. |
| `variational-calculus/06-SECOND-VARIATION.md` | Reader can diagnose second-variation claims by separating local positivity, necessary/sufficient conditions, conjugate points, stability, global existence, and Morse theory. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

