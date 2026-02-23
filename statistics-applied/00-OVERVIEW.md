# 00 — Applied Statistics Overview

## Frequentist vs Bayesian, Estimands, Causal Hierarchy

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Frequentist framework: parameters are fixed, data is random; confidence intervals as procedure properties not probability statements; p-values as P(data | H₀), not P(H₀ | data); Neyman-Pearson hypothesis testing vs Fisher significance testing (the conceptual confusion that produced p<0.05)
- Bayesian framework: parameters have distributions; posterior ∝ likelihood × prior; credible intervals as genuine probability statements; updating beliefs with evidence; decision-theoretic framing (expected utility)
- When each wins: frequentist (regulatory/confirmatory settings where pre-specified type I error matters), Bayesian (exploratory/adaptive/decision-under-uncertainty settings), pragmatic (just use the tool that answers the right question)
- Estimands (ICH E9(R1)): the treatment effect you actually want to estimate — intercurrent events matter (what population? what treatment strategy?); estimand ≠ estimator ≠ estimate
- Causal hierarchy (Pearl's ladder of causation): rung 1 — association (P(Y|X)); rung 2 — intervention (P(Y|do(X))); rung 3 — counterfactual (P(Yₓ=1|X=0)); observational data lives on rung 1; experiments reach rung 2; structural models reach rung 3
- Identification vs estimation: identification (can the causal effect be recovered from observational data in principle?), estimation (given identification, how to estimate from finite samples efficiently?)
- Common errors: HARKing (hypothesizing after results known), p-hacking (optional stopping, multiple comparisons without correction), overfitting, underpowered studies, Simpson's paradox
- Key reference: ASA statement on p-values (2016), Moving to a World Beyond p<0.05 (2019)
- Index of modules: experimental design, A/B testing, quasi-experimental methods, Bayesian practice, reliability/SPC
