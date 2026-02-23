# 03 — Quasi-Experimental Methods

## Diff-in-Diff, RDD, Synthetic Control, IV, Event Studies

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Why quasi-experimental: can't randomize (ethical/practical), need causal estimate from observational data; requires identifying assumption (untestable but assessable)
- Difference-in-Differences (DiD): parallel trends assumption (treatment and control would have moved together absent treatment); two-period DiD estimator (β = (Ȳ_T,post - Ȳ_T,pre) - (Ȳ_C,post - Ȳ_C,pre)); testing parallel pre-trends; staggered DiD (Callaway-Sant'Anna heterogeneous treatment timing — the OLS TWFE problems)
- Regression Discontinuity Design (RDD): assignment determined by continuous running variable crossing threshold; continuity assumption (potential outcomes continuous at cutoff); sharp vs fuzzy (IV interpretation for fuzzy); bandwidth selection (local linear regression, MSE-optimal bandwidth); donut RDD; McCrary test for manipulation
- Synthetic Control (Abadie-Diamond-Hainmueller 2010): construct weighted combination of control units to match pre-treatment outcomes of treated unit; inference via permutation; placebo tests; no parallel trends assumption needed; single treated unit setting
- Instrumental Variables (IV): instrument Z affects treatment D but affects outcome Y only through D; two-stage least squares (2SLS); first stage strength (F-stat >10 rule of thumb, weak instruments problem); monotonicity assumption (LATE = Local Average Treatment Effect for compliers only); natural experiments as instruments (Angrist-Pischke classics: draft lottery, compulsory schooling laws)
- Event Studies: examine outcomes around a discrete event (earnings announcements, policy changes, product launches); relative time specification; pre-event test for parallel trends; stacked event study design for multiple events
- Interrupted time series (ITS): single unit, many time periods; segmented regression (level + trend changes); autoregressive errors (Newey-West SEs); ARIMA-OLS
- Selection on observables vs unobservables: propensity score methods (matching/IPW/AIPW) — only eliminate observed confounders; sensitivity analysis (Rosenbaum bounds) for unobserved confounding
- DiD + RDD + IV comparison: when each identification strategy is appropriate, threat table (what assumption might fail and how to assess it)
