# 04 — Bayesian Practice

## Prior Selection, MCMC, Credible Intervals, Bayesian Workflow, Stan/PyMC

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Bayesian workflow (Gelman et al.): prior predictive checks → model fitting → posterior predictive checks → model comparison → iteration; distinguishing "did the model fit" from "is this the right model"
- Prior selection: flat/non-informative priors (can cause problems — Jeffreys priors as improvement), weakly informative priors (constrain to plausible range without strong commitment — N(0,1) for standardized effects), informative priors (domain knowledge encoded); prior predictive simulation to check sensibility
- Conjugate priors: Beta-Binomial (conversion rates), Gamma-Poisson (counts), Normal-Normal (continuous); closed-form posteriors; when conjugacy matters vs when MCMC needed
- Markov Chain Monte Carlo (MCMC): Metropolis-Hastings (proposal + acceptance ratio), Gibbs sampling (conditional distributions), Hamiltonian Monte Carlo (HMC — gradient-guided, much more efficient); NUTS (No U-Turn Sampler — auto-tunes HMC); convergence diagnostics (R̂/Rhat, ESS, trace plots)
- Stan: probabilistic programming language, declares model in data/parameters/model blocks, generates MCMC samples; interfaces (RStan/PyStan/CmdStanPy); vectorization for efficiency
- PyMC: Python-native, NUTS via PyTensor backend, more ML-friendly API; model comparison with LOO-CV (PSIS-LOO)
- Bayesian credible intervals vs frequentist CIs: posterior interval containing 95% probability (genuine statement vs procedural confidence interval); practical interpretation difference
- Model comparison: WAIC, LOO-CV (leave-one-out cross-validation via PSIS), Bayes factors (sensitive to prior choice), posterior predictive checks; stacking for model combination
- Bayesian A/B testing: posterior probability of winning (P(θ_B > θ_A)), expected loss framework, no multiple comparisons problem (but prior sensitivity), decision rules vs hypothesis tests
- Hierarchical models (multilevel/mixed effects): partial pooling as Bayesian regularization, shrinkage toward group mean, random effects as Bayesian priors; schools-as-example (Gelman 8-schools)
