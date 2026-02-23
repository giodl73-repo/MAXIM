# 01 — Experimental Design

## RCTs, Power Analysis, Sample Size, Factorial Designs, Blocking

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Randomization: simple vs block vs stratified vs cluster; why randomization enables causal inference (balances observed and unobserved confounders in expectation); randomization unit vs analysis unit (avoid unit-of-analysis errors)
- CONSORT framework: consolidated standards for reporting RCTs; intention-to-treat (ITT) vs per-protocol vs as-treated analysis; non-compliance and instrumental variables
- Power analysis: Type I error α (false positive rate, typically 0.05), Type II error β (false negative rate), power = 1-β (typically 80% or 90%); MDE (minimum detectable effect) as primary input; sample size formula for two-sample t-test; G*Power / R pwr package
- Effect size conventions: Cohen's d (0.2 small/0.5 medium/0.8 large), r, odds ratio, NNT; why standardized effect sizes matter for comparing across studies; practical vs statistical significance
- Factorial designs: 2ᵏ full factorial (all factor combinations), main effects + interactions; 2ᵏ⁻ᵖ fractional factorial (aliasing, resolution III/IV/V), Plackett-Burman (screening); response surface methodology (RSM) for optimization
- Blocking: remove nuisance variation (blocks = days/batches/subjects in crossover); randomized complete block design (RCBD); Latin square (two blocking factors); split-plot design (hard-to-change factors)
- Within-subjects / crossover designs: carryover effects, washout periods, period effects, sequence effects; when within-subjects is much more efficient
- Adaptive designs: group sequential (O'Brien-Fleming/Pocock stopping boundaries), adaptive sample size re-estimation, response-adaptive randomization, basket/umbrella/platform trials
- Sequential testing and peeking: why classical tests break with interim looks; alpha-spending functions; always-valid p-values (e-values/anytime-valid inference)
- Field experiments: randomization at scale (online platforms), interference between units (SUTVA violations — network effects, spillovers), cluster-level randomization implications
