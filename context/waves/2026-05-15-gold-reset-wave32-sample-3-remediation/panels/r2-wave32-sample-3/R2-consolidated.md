# R2 Consolidated Panel - Gold Reset Wave 32 Sample 3

## Verdict

PASS. The Wave 32 distributed-systems/weaving sample satisfies Gold Rubric v2
after targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `distributed-systems/02-CONSISTENCY-MODELS.md` | 4.6 | `consistency-model-hierarchy` | Certified Gold |
| `distributed-systems/04-REPLICATION.md` | 4.6 | `replication-topology-comparison` | Certified Gold |
| `distributed-systems/08-MICROSERVICES.md` | 4.6 | `microservices-infrastructure-layers` | Certified Gold |
| `dyeing-fiber/06-WEAVING.md` | 4.6 | `weaving-fundamentals` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: model-selection, topology-selection, pattern-selection, and weave-selection table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `distributed-systems/02-CONSISTENCY-MODELS.md` | Diagnose a consistency claim by separating real-time order, causality, session guarantees, convergence, and vendor terminology. | PASS |
| `distributed-systems/04-REPLICATION.md` | Diagnose a replication choice by separating leader/failover, read freshness, conflict semantics, quorum overlap, consensus need, and global latency. | PASS |
| `distributed-systems/08-MICROSERVICES.md` | Diagnose a microservices failure by separating retry budget, bulkhead boundary, queue pressure, saga isolation, mesh cost, gateway role, and rollout risk. | PASS |
| `dyeing-fiber/06-WEAVING.md` | Diagnose a weaving project by separating fiber/yarn, sett, loom control, float length, structure, tension, and finishing. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

