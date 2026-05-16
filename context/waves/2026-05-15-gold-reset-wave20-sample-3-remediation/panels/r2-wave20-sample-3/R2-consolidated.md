# R2 Consolidated Panel - Gold Reset Wave 20 Sample 3

## Verdict

PASS. The Wave 20 mixed quantum/statistical-mechanics sample satisfies Gold
Rubric v2 after targeted repair, proof/Da Vinci validation, and guide-specific
R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `quantum-computing/04-HARDWARE-COMPLEXITY.md` | 4.6 | `quantum-computing-stack` | Certified Gold |
| `quantum-computing/06-QUANTUM-COMMUNICATION.md` | 4.6 | `qkd-protocol-family` | Certified Gold |
| `statistical-mechanics/06-RENORMALIZATION.md` | 4.6 | `renormalization-group-flow` | Certified Gold |
| `statistical-mechanics/07-ISING-MODELS.md` | 4.6 | `ising-model-landscape` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: answer, recommendation, and model-selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `quantum-computing/04-HARDWARE-COMPLEXITY.md` | Diagnose hardware and complexity claims by separating fidelity, count, platform uncertainty, annealing, RSA timelines, PQC, factoring, and NP-complete limits. | PASS |
| `quantum-computing/06-QUANTUM-COMMUNICATION.md` | Diagnose quantum communication by separating QKD requirements, distance regimes, trusted repeaters, satellite/repeater options, DI-QKD, QBER, and PQC. | PASS |
| `statistical-mechanics/06-RENORMALIZATION.md` | Diagnose renormalization by separating universality, linearization, mean-field limits, relevance, epsilon expansion, 1D Ising, QFT mapping, and scaling relations. | PASS |
| `statistical-mechanics/07-ISING-MODELS.md` | Diagnose Ising models by separating dimensional transitions, Hopfield capacity, BKT topology, Metropolis rules, and critical slowing down. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

