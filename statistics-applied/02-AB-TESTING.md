# 02 — A/B Testing

## Online Experiment Architecture, CUPED, SRM, Novelty Effects, Bandits

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Online experimentation architecture: experiment assignment (hash-based, sticky, consistent), logging pipeline (click/conversion events), analysis pipeline (metric computation, statistical tests), experiment registry
- Metric taxonomy: guardrail metrics (must not regress — latency/crashes/core engagement), primary decision metrics (OEC — Overall Evaluation Criterion), secondary/diagnostic metrics, ratio metrics (clicks/session — delta method for variance)
- Sample Ratio Mismatch (SRM): detected when assignment ratio ≠ observed ratio in analysis; causes (bot traffic, logging bugs, survivorship bias, redirects); SRM as experiment health check; never analyze if SRM detected
- Variance reduction (CUPED): Control Using Pre-Experiment Data (Deng/Xu/Ghosh/Zhang, 2013); subtract prediction from pre-experiment covariate; variance reduction 30-70% typical; CUPAC (model-based covariate); practical implementation
- Novelty and primacy effects: users behave differently when experiencing something new; novelty effect (inflates treatment effect, decays over time), primacy effect (users stick with familiar, inflates control); holdout designs to detect; long-term holdback experiments
- Multiple testing: FWER (Bonferroni/Holm) vs FDR (Benjamini-Hochberg); sequential testing (mSPRT, always-valid p-values); continuous monitoring; alpha spending
- Interference and network effects: SUTVA violations in social networks, marketplace two-sided interference; graph clustering randomization (network clusters), switchback designs (time-based randomization), holdout at user+country grain
- Multi-armed bandits vs A/B tests: exploration-exploitation tradeoff (ε-greedy/UCB/Thompson Sampling); when to use bandits (fast iteration, low cost of exploration) vs A/B (rigorous causal estimate needed); Bayesian regret as objective
- Heterogeneous treatment effects (HTE): subgroup analysis (multiple comparisons risk), CATE estimation (causal forests), interaction terms; from average treatment effect to personalization
- Experiment velocity: democratizing experimentation, self-serve platforms, trustworthy culture (not p-hacking), peer review for experiments, learning from losses
