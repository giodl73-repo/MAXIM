# R2 Reference Editor Panel - Gold Reset Wave 8 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `machine-learning-theory/07-DOUBLE-DESCENT.md` | `double-descent-curve` | 4.6 |
| `machine-learning-theory/08-INFORMATION-THEORETIC.md` | `information-theoretic-generalization` | 4.6 |
| `machine-learning-theory/09-OPEN-PROBLEMS.md` | `ml-theory-frontier` | 4.6 |
| `control-theory/08-ADAPTIVE-CONTROL.md` | `adaptive-control-architecture` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables were too prescription/list oriented. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | ML/control claims need caveats about interpolation-threshold dependence, benign-overfitting assumptions, MI infinities, PAC-Bayes prior legitimacy, toy ICL mechanisms, worst-case hardness, learnability versus expressivity, certainty equivalence, adaptive-filter tradeoffs, and time-varying parameter noise. | Added caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge modern ML theory frontiers with adaptive-control design choices. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `machine-learning-theory/07-DOUBLE-DESCENT.md` | Reader can diagnose double-descent behavior by separating classical U-curves, interpolation peaks, benign overfitting, epoch-wise descent, grokking, scaling, and optimizer effects. |
| `machine-learning-theory/08-INFORMATION-THEORETIC.md` | Reader can diagnose information-theoretic bounds by separating PAC-Bayes, CMI, MI, MDL, optimized posteriors, and informed priors. |
| `machine-learning-theory/09-OPEN-PROBLEMS.md` | Reader can diagnose frontier problems by separating deep-net generalization, SGD bias, ICL, hardness, grokking, complexity measures, and transformer theory. |
| `control-theory/08-ADAPTIVE-CONTROL.md` | Reader can diagnose adaptive-control strategy by separating MRAC, STR/RLS, gain scheduling, L1, NN adaptive control, and time-varying estimation. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

