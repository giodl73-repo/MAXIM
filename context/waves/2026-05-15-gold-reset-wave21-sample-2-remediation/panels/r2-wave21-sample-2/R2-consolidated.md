# R2 Consolidated Panel - Gold Reset Wave 21 Sample 2

## Verdict

PASS. The Wave 21 market/anomaly and applied-statistics sample satisfies Gold
Rubric v2 after targeted repair, proof/Da Vinci validation, and guide-specific
R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `behavioral-economics/08-MARKET-ANOMALIES.md` | 4.6 | `behavioral-finance-landscape` | Certified Gold |
| `statistics-applied/01-EXPERIMENTAL-DESIGN.md` | 4.6 | `experimental-design-decision-tree` | Certified Gold |
| `statistics-applied/02-AB-TESTING.md` | 4.6 | `online-experimentation-architecture` | Certified Gold |
| `statistics-applied/04-BAYESIAN-PRACTICE.md` | 4.6 | `bayesian-workflow` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: answer-key and implication-table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `behavioral-economics/08-MARKET-ANOMALIES.md` | Diagnose anomalies by separating equity premium, disposition, momentum, reversal, excess trading, analyst optimism, and IPO caveats. | PASS |
| `statistics-applied/01-EXPERIMENTAL-DESIGN.md` | Diagnose experimental designs by separating power, concealment, ITT, cluster effects, factorial aliasing, crossover validity, and alpha spending. | PASS |
| `statistics-applied/02-AB-TESTING.md` | Diagnose A/B tests by separating SRM, CUPED, novelty/primacy, bandits, multiplicity, continuous monitoring, and cluster randomization. | PASS |
| `statistics-applied/04-BAYESIAN-PRACTICE.md` | Diagnose Bayesian workflows by separating prior scale, convergence, samplers, divergences, pooling, posterior comparisons, and LOO diagnostics. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

