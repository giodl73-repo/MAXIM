# R2 Reference Editor Review - Gold Reset Wave 35 Sample 6

## Scope

| Guide | Invariant |
|---|---|
| `finance/02-DERIVATIVES.md` | `derivatives-structural-landscape` |
| `finance/03-FIXED-INCOME.md` | `fixed-income-landscape` |
| `finance/04-RISK-MODELS.md` | `financial-risk-landscape` |

## Rubric Findings

### `finance/02-DERIVATIVES.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Forwards, futures, swaps, options, exotics, structured products, Greeks, vol surface, and credit derivatives form a coherent map. |
| Diagrams | 4.5 | Structural derivative landscape remains proof-clean and useful. |
| Conceptual accuracy | 4.6 | Decision support now distinguishes quoting convention, model caveats, early exercise, skew, and local Greeks. |
| Peer tone | 4.7 | Uses stochastic calculus and no-arbitrage machinery at an appropriate level. |
| Bridges | 4.6 | Portfolio, fixed-income, and risk-model cross-links are targeted. |
| Decision support | 4.7 | Cheat sheet now diagnoses derivative pricing and hedging problems by structure and caveat. |

Decision: PASS at 4.6.

### `finance/03-FIXED-INCOME.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Bonds, yield curves, duration, term-structure models, credit, swaps, MBS, TIPS, and repo are integrated. |
| Diagrams | 4.5 | Fixed-income landscape and bridge diagrams remain proof-clean. |
| Conceptual accuracy | 4.6 | Bootstrap maturity example and TIPS currentness are corrected/caveated. |
| Peer tone | 4.7 | Treats curves and risk as computational objects, not glossary entries. |
| Bridges | 4.7 | DCF, dependency-resolution, derivative, and SDE bridges are strong. |
| Decision support | 4.7 | Cheat sheet now diagnoses price/yield, DV01, key-rate, convexity, OAS, and credit-spread questions. |

Decision: PASS at 4.6.

### `finance/04-RISK-MODELS.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | VaR, ES, EVT, copulas, stress testing, systemic risk, portfolio risk, capital, OpRisk, liquidity, and FRTB are connected. |
| Diagrams | 4.5 | Financial-risk landscape remains proof-clean and useful. |
| Conceptual accuracy | 4.6 | VaR convention/horizon wording, historical percentile, and FRTB currentness are corrected. |
| Peer tone | 4.7 | Maintains quantitative precision while naming model-risk failure modes. |
| Bridges | 4.6 | Portfolio, derivatives, and fixed-income cross-links are effective. |
| Decision support | 4.7 | Cheat sheet now diagnoses risk measures by failure mode and model limitation. |

Decision: PASS at 4.6.

## Adversarial Closure

| Concern | Closure |
|---|---|
| Derivatives guide ended with a method lookup table rather than decision support. | Table now diagnoses pricing, hedging, exercise, exotics, Greeks, skew, and swaps with caveats. |
| Fixed-income guide had a bootstrap indexing error and stale current-rate examples. | Bootstrap uses a 1.5yr bond for d(1.5); TIPS/nominal yields are framed as example 2024 ranges. |
| Risk-model guide mixed VaR conventions and over-specified evolving FRTB implementation. | VaR definitions and historical percentile are corrected; FRTB status is now explicitly jurisdiction-dependent. |

No BLOCK or WARN findings remain for the scoped Gold claims.

