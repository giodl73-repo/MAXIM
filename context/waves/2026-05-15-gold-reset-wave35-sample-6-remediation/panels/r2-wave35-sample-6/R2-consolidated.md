# R2 Consolidated Panel - Gold Reset Wave 35 Sample 6

## Verdict

PASS. The sixth Wave 35 reset sample satisfies Gold Rubric v2 after targeted
editorial repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `finance/02-DERIVATIVES.md` | 4.6 | `derivatives-structural-landscape` | Certified Gold |
| `finance/03-FIXED-INCOME.md` | 4.6 | `fixed-income-landscape` | Certified Gold |
| `finance/04-RISK-MODELS.md` | 4.6 | `financial-risk-landscape` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all three scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: lookup-table, bootstrap, currentness, VaR convention, and FRTB issues repaired |
| Reader-task check | PASS: all three guides now support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `finance/02-DERIVATIVES.md` | Diagnose a derivative by identifying payoff structure, replication/pricing model, exercise feature, path dependence, Greeks, volatility surface, and hedge caveat. | PASS |
| `finance/03-FIXED-INCOME.md` | Diagnose a fixed-income claim by separating cash-flow discounting, spot/par/forward curves, DV01, key-rate risk, convexity, optionality, spread, and liquidity. | PASS |
| `finance/04-RISK-MODELS.md` | Diagnose a risk metric by naming the distribution, tail behavior, dependence model, liquidity/funding interaction, stress scenario, and regulatory scope. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

