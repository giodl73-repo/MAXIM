# Bayesian Practice — Stan/PyMC, MCMC, Priors, Hierarchical Models

## The Big Picture

```
+------------------------------------------------------------------+
|              BAYESIAN WORKFLOW (Gelman et al., 2020)             |
|                                                                  |
|  1. SPECIFY MODEL                                                |
|     Prior p(θ): what you believe before data                     |
|     Likelihood p(y|θ): probability of data given parameters      |
|                                                                  |
|  2. PRIOR PREDICTIVE CHECK                                       |
|     Sample θ from prior → generate fake data y_pred              |
|     Does y_pred look plausible? (not "does it match data")       |
|     → Catches unreasonable priors before seeing real data        |
|                                                                  |
|  3. FIT MODEL                                                    |
|     Compute posterior p(θ|y) ∝ p(y|θ) × p(θ)                   |
|     MCMC (HMC/NUTS) or variational inference                     |
|                                                                  |
|  4. POSTERIOR DIAGNOSTICS                                        |
|     R̂ (convergence), ESS (effective samples), trace plots       |
|                                                                  |
|  5. POSTERIOR PREDICTIVE CHECK                                   |
|     Sample θ from posterior → generate y_rep                    |
|     Does y_rep match real data structure? → Model fit            |
|                                                                  |
|  6. COMPARE MODELS (if multiple)                                 |
|     LOO-CV (PSIS-LOO), WAIC, stacking                           |
|                                                                  |
|  7. ITERATE                                                      |
|     If failed at any step → refine model, prior, likelihood      |
+------------------------------------------------------------------+
```

---

## Prior Selection

```
SPECTRUM OF PRIOR INFORMATIVENESS:

FLAT / DIFFUSE PRIORS (e.g., Uniform(−∞, ∞)):
  "Let data speak completely"
  PROBLEMS:
  • Improper: don't integrate to 1 → can cause improper posteriors
  • Uniform on θ ≠ uniform on f(θ): uninformative on one scale =
    highly informative on transformed scale
  • Weakly identified models: flat prior → poor posterior sampling
  USE CASE: almost never in modern practice; historical artifact

JEFFREYS PRIORS:
  Invariant under parameter transformations
  Jeffreys: π(θ) ∝ √det(I(θ))  (square root of Fisher information)
  Binomial rate: Jeffreys = Beta(1/2, 1/2) (not Beta(1,1) = flat)
  → Principled "non-informative" choice
  USE CASE: single-parameter problems; reference analysis

WEAKLY INFORMATIVE PRIORS (recommended default):
  "Constrain to plausible region without strong commitment"
  Does not encode strong beliefs; prevents pathological posteriors
  GUIDELINES (Gelman et al., 2008 onward):
  For coefficients in regression (standardized predictors):
  → Normal(0, 2.5) or Normal(0, 10): rules out implausibly large effects
  For intercept: Normal(mean, 5×SD) on outcome scale
  For σ (scale): HalfNormal(σ) or Exponential(λ)
  For correlations: LKJ(η) prior on correlation matrices (η=1: uniform; η=2: shrinks toward 0)

INFORMATIVE PRIORS:
  Encode specific domain knowledge
  EXAMPLES:
  Phase 2 clinical trial: prior from Phase 1 data (power prior approach)
  Historical control arm: incorporate as informative prior on control rate
  Regression coefficient: sign-constrained if known direction
  Physical constraint: θ ∈ [0,1] → Beta prior
  → Requires documentation and sensitivity analysis

PRIOR PREDICTIVE SIMULATION:
  BEFORE fitting: sample θ from prior → compute E[Y]
  Plot: does simulated data look plausible?
  "Does my prior imply that the average person has 10,000 children? → Too diffuse"
  "Does my prior imply only effects between −0.001 and 0.001? → Too tight"
  This check catches unit mistakes, scale errors, structural problems
```

---

## Conjugate Priors

```
CONJUGATE PRIOR:
  Prior from the same family as the posterior → closed-form posterior
  Valuable for: speed, interpretability, online updating, teach intuition

+------------------+------------------+------------------+--------------------------+
| LIKELIHOOD       | CONJUGATE PRIOR  | POSTERIOR        | APPLICATION              |
+------------------+------------------+------------------+--------------------------+
| Binomial(n, θ)   | Beta(α, β)       | Beta(α+x, β+n-x) | Conversion rate, CTR     |
| Poisson(λ)       | Gamma(α, β)      | Gamma(α+Σxᵢ,     | Count data, event rates  |
|                  |                  | β+n)             |                          |
| Normal(μ, σ²)    | Normal(μ₀, σ₀²) | Normal(μₙ, σₙ²) | Continuous outcomes      |
| (σ known)        |                  |                  |                          |
| Normal(μ, σ²)    | Normal-Inv-χ²   | Normal-Inv-χ²   | Full normal model        |
| (both unknown)   |                  |                  |                          |
| Multinomial      | Dirichlet(α)     | Dirichlet(α+x)  | Category probabilities   |
+------------------+------------------+------------------+--------------------------+

BETA-BINOMIAL (KEY EXAMPLE):
  Prior: θ ~ Beta(α, β)
  Data: x successes in n trials
  Posterior: θ ~ Beta(α+x, β+n−x)

  Hyperparameter interpretation:
  α = prior successes; β = prior failures
  α+β = prior sample size (how much to trust prior)

  ONLINE A/B TEST VARIANT:
  Control: θ_C ~ Beta(α_C + x_C, β_C + n_C − x_C)
  Treatment: θ_T ~ Beta(α_T + x_T, β_T + n_T − x_T)
  P(θ_T > θ_C) = ∫∫ p(θ_T > θ_C | data) = computed by simulation or incomplete Beta
  → "Probability treatment wins" — direct decision-relevant quantity

GAMMA-POISSON:
  Prior: λ ~ Gamma(α, β)  (mean = α/β)
  Data: n events in T time
  Posterior: λ ~ Gamma(α + n, β + T)
  → Natural for: count events, failure rates, arrivals
```

---

## Markov Chain Monte Carlo

### Why MCMC

```
PROBLEM:
  For any but the simplest models, p(θ|y) has no closed form
  Integral Z = ∫ p(y|θ) p(θ) dθ is computationally intractable in high dimensions

MCMC SOLUTION:
  Construct a Markov chain with p(θ|y) as its stationary distribution
  Sample from the chain → eventually (after burn-in) → samples approximate posterior
  → No need to compute Z; only need unnormalized posterior p(y|θ) × p(θ)

METROPOLIS-HASTINGS:
  Propose: θ* ~ q(θ*|θ_t)  (proposal distribution)
  Accept: with probability min(1, [p(θ*|y) × q(θ_t|θ*)] / [p(θ_t|y) × q(θ*|θ_t)])
  → Accept if proposed posterior ≥ current; accept with some probability if lower
  Properties: detailed balance → stationary distribution = p(θ|y)
  Problem: proposal scale matters; random walk → slow mixing in high dimensions

GIBBS SAMPLING:
  Sample each parameter θⱼ conditional on all others:
  θⱼ^(new) ~ p(θⱼ | θ₋ⱼ, y)
  If conditional distributions available in closed form: very efficient
  Works well for hierarchical models with conjugate priors (known conditionals)
  Problem: high correlation → slow mixing (each step small)
```

### Hamiltonian Monte Carlo (HMC)

```
KEY INNOVATION:
  Use gradient information (∇ log p(θ|y)) to guide exploration
  Simulate Hamiltonian dynamics in augmented space (θ, momentum p)
  → Takes large steps in parameter space
  → Much more efficient than random walk in high dimensions

HAMILTONIAN:
  H(θ, p) = U(θ) + K(p)
  U(θ) = −log p(θ|y)  (potential energy = negative log posterior)
  K(p) = p^T M⁻¹ p / 2  (kinetic energy, M = mass matrix)

  Simulate: dθ/dt = ∂H/∂p, dp/dt = −∂H/∂θ
  → Trajectories follow constant-H surfaces = constant posterior density
  → Move far before proposing → high acceptance rate + large moves
  → Requires gradient ∇ log p(θ|y): automatic differentiation (autodiff) in Stan

NUTS (No U-Turn Sampler):
  Problem with basic HMC: how long to simulate trajectory?
  → Too short: like random walk
  → Too long: doubles back (wastes computation)
  NUTS: stops simulation when trajectory starts to double back
  → Adaptive trajectory length; self-tuning
  DUAL AVERAGING: automatically adapts step size ε
  → Stan uses NUTS with dual averaging → virtually no tuning required

NUTS ADVANTAGES:
  vs MH: much more efficient in high dimensions (fewer correlated samples)
  vs Gibbs: no need for conjugate conditionals
  vs random walk: guided by geometry of posterior
  vs Variational Inference: exact (asymptotically), not approximate
```

### Convergence Diagnostics

```
R̂ (Rhat / potential scale reduction factor):
  Compare within-chain vs between-chain variance
  R̂ = √(estimated posterior variance / within-chain variance)
  R̂ ≈ 1: chains agree → convergence (to same target)
  R̂ > 1.01 (modern strict threshold; old: 1.1): suspect non-convergence
  Run multiple chains (4 standard); if not mixed: rethink model

EFFECTIVE SAMPLE SIZE (ESS):
  MCMC draws are autocorrelated; each draw not independent
  ESS = N_draws / (1 + 2 × Σ autocorrelations)
  ESS = 1000 from 4000 draws: autocorrelation = 3× redundancy
  Target: ESS > 400 bulk ESS + ESS_tail > 400
  Low ESS → longer chains, better initialization, reparameterize

TRACE PLOTS:
  Plot θ vs iteration for each chain
  Should look like: "fat hairy caterpillar" (well-mixed, stationary)
  Warning signs:
  • Funnel: chain stuck in narrow region
  • Drift: trend in time → not stationary → still mixing
  • One chain separated → poor initialization

DIVERGENCES (Stan-specific):
  HMC leapfrog integrator encounters pathological geometry:
  → "Divergent transition after warmup"
  → Not a numerical error: signal of problematic posterior geometry
  → Posterior has regions of extreme curvature (funnel, hard corners)
  FIX: reparameterize (non-centered parameterization for hierarchical models)
  → NEVER ignore divergences; they invalidate posterior estimates
```

---

## Stan and PyMC

```
STAN:
  Probabilistic programming language: C++ backend
  Model blocks: data / transformed data / parameters / transformed parameters / model / generated quantities
  Interfaces: RStan, PyStan, CmdStanPy (recommended), CmdStanR
  Autodiff: computes ∇ log p(θ|y) automatically for HMC
  Sampler: NUTS with dual averaging (state of the art)

  STAN MODEL STRUCTURE:
  data {
    int<lower=0> N;
    array[N] real y;
  }
  parameters {
    real mu;
    real<lower=0> sigma;
  }
  model {
    mu ~ normal(0, 10);       // prior
    sigma ~ exponential(0.1); // prior
    y ~ normal(mu, sigma);    // likelihood
  }

  CMDSTANPY (recommended):
  stan_model = CmdStanModel(stan_file='model.stan')
  fit = stan_model.sample(data={'N': n, 'y': y.tolist()},
                          chains=4, iter_warmup=1000, iter_sampling=2000)
  fit.diagnose()  # check R̂, ESS, divergences
  fit.summary()

PYMC:
  Python-native; PyTensor autodiff backend
  Model specified in Python (no separate language)
  Sampler: NUTS via PyTensor; also supports variational inference (ADVI)

  PYMC MODEL STRUCTURE:
  with pm.Model() as model:
      mu = pm.Normal('mu', mu=0, sigma=10)
      sigma = pm.Exponential('sigma', lam=0.1)
      y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
      trace = pm.sample(2000, tune=1000, chains=4, target_accept=0.9)
  pm.plot_trace(trace)
  pm.summary(trace)

  NON-CENTERED PARAMETERIZATION (critical for hierarchical):
  Centered:     θ_j ~ Normal(μ, σ)
  Non-centered: z_j ~ Normal(0, 1); θ_j = μ + σ × z_j
  → Identical model; different geometry
  → Non-centered: μ and σ can vary independently → fewer divergences

ARVIZ (model diagnostics library):
  Works with both Stan and PyMC outputs
  import arviz as az
  az.summary(idata, round_to=3)    → summary with R̂, ESS
  az.plot_trace(idata)              → trace plots
  az.plot_posterior(idata)          → posterior distributions
  az.loo(idata)                     → LOO-CV score
  az.compare({'model1': idata1, 'model2': idata2})  → model comparison
```

---

## Credible Intervals vs Confidence Intervals

```
POSTERIOR CREDIBLE INTERVAL:
  "Given data and prior, 95% probability that θ is in this range"
  This IS a direct probability statement about the parameter (given prior)
  Meaningful: "I believe with 95% probability that the effect is between 0.1 and 0.5"

FREQUENTIST CONFIDENCE INTERVAL:
  "If we repeated this procedure many times, 95% of computed intervals
  would contain the true parameter"
  Is NOT: "95% probability the true value is in this interval"
  The true value is fixed; this single interval either contains it or not
  (0% or 100% probability for THIS specific interval)

PRACTICAL DIFFERENCE:
  95% CI [0.1, 0.5]: frequentist → procedure has 95% coverage
  95% CrI [0.1, 0.5]: Bayesian → 95% posterior probability
  They often produce similar numbers (especially with diffuse priors)
  but the INTERPRETATION differs fundamentally

WHEN THE DIFFERENCE MATTERS:
  Sequential analysis: Bayesian CrI valid at any stopping point (no inflating)
  Decision-making: Bayesian posterior probability is the natural input
  With strong priors: they can diverge substantially
  Communication to stakeholders: "95% probability" is clearer than "procedural coverage"

HIGHEST POSTERIOR DENSITY INTERVAL (HPDI):
  Shortest interval containing 95% of posterior mass
  (vs equal-tails credible interval: 2.5th to 97.5th percentile)
  For symmetric posteriors: identical
  For skewed posteriors: HPDI is shorter and asymmetric
```

---

## Hierarchical (Multilevel) Models

```
STRUCTURE:
  Units j = 1,...,J are groups
  Observations i within groups
  Parameters θⱼ vary by group, drawn from common distribution

  Y_ij = f(θⱼ, x_ij) + ε_ij
  θⱼ ~ Normal(μ, τ)   ← hyperprior
  μ ~ prior; τ ~ prior

PARTIAL POOLING:
  Complete pooling: all groups share one θ (no variation allowed)
  No pooling: each group gets separate θ_j (no borrowing strength)
  Partial pooling: θ_j shrinks toward grand mean μ
    → More data in group j → less shrinkage (trust local estimate)
    → Less data in group j → more shrinkage (borrow from others)

  MATHEMATICALLY:
  θ_j^partial = w_j × θ_j^local + (1-w_j) × μ
  w_j = n_j × σ²_between / (n_j × σ²_between + σ²_within)

GELMAN'S 8-SCHOOLS EXAMPLE:
  8 schools, each with measured SAT effect of coaching
  θⱼ: true effect of coaching for school j
  Observed: y_j = θ_j + Normal(0, σ_j²) (measurement noise)
  Prior: θ_j ~ Normal(μ, τ²)
  → Partial pooling: extreme effects shrink toward grand mean
  → Schools with n → ∞ converge to their local estimate
  → Schools with n → 0 converge to grand mean
  Classic demonstration: no pooling = overfit; complete pooling = underfit

WHY BAYESIAN MULTILEVEL:
  Frequentist mixed effects: REML estimation of variance components
    → Treats hyperparameters as fixed → uncertainty in τ ignored
  Bayesian: full posterior over (θ₁,...,θⱼ, μ, τ)
    → Uncertainty in all levels propagated
    → Particularly important when J is small (few groups)

APPLICATIONS:
  Individual effects within experiment (user-level heterogeneity)
  School effects (students within schools)
  Clinical sites in multi-center trial
  Rater effects in content moderation
  Geographic random effects (state/country in policy analysis)
```

---

## Bayesian A/B Testing and Model Comparison

```
BAYESIAN A/B TEST:
  θ_A ~ Beta(α_A, β_A)  (conversion rate, control)
  θ_B ~ Beta(α_B, β_B)  (conversion rate, treatment)
  → Update with data → posteriors

  KEY QUANTITIES:
  P(θ_B > θ_A | data): "Probability treatment wins"
    → Compute by simulation: draw 10,000 samples, count fraction B > A
    → No threshold like p<0.05; directly interpretable probability

  Expected loss:
  L(choose A | truth) = E[max(θ_B − θ_A, 0) | data]
  L(choose B | truth) = E[max(θ_A − θ_B, 0) | data]
  → Ship B when E[loss if ship A] > threshold (e.g., 1% of baseline)
  → Natural business framing: "expected cost of wrong decision"

MULTIPLE COMPARISONS:
  Bayesian: no multiple comparisons problem IN THE SAME SENSE
  Posterior probability P(θⱼ > θ_control | data) is valid for each variant
  BUT: if you test many variants, some will have high posterior probability by chance
  → Still need to adjust your decision threshold
  → Or use a hierarchical model: θⱼ ~ Normal(μ, τ) → partial pooling shrinks extreme estimates

MODEL COMPARISON:
  LOO-CV (Leave-One-Out Cross-Validation via PSIS):
  elpd_loo = Σ log p(y_i | y_{-i})  (expected log predictive density)
  PSIS approximation (Pareto-smoothed importance sampling): avoids refitting N times
  az.loo() in ArviZ; implemented in loo R package
  → Compare models: larger elpd_loo = better out-of-sample prediction

  WAIC (Widely Applicable Information Criterion):
  lppd − p_WAIC (penalty for effective number of parameters)
  Similar to LOO-CV asymptotically; less stable in practice
  LOO-CV preferred (more robust to model misspecification)

  BAYES FACTORS:
  K = p(y | M₁) / p(y | M₂) = marginal likelihood ratio
  PROBLEM: strongly sensitive to prior (marginal likelihood integrates over prior)
  → Diffuse prior → punishes more complex model heavily (even correctly)
  → Requires proper, carefully chosen priors
  Jeffreys (1961) scale: K > 10 → strong evidence; K > 100 → decisive
  RARELY USED in modern practice due to prior sensitivity
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is a weakly informative prior? | Prior that constrains parameters to plausible range without strong commitment. Normal(0, 2.5) for standardized regression coefficients. Prevents pathological posteriors while letting data dominate. |
| What does R̂ > 1.01 mean? | Chains are not well-mixed — they haven't converged to the same distribution. Diagnose: trace plots, look for stuck chains, reparameterize or run longer. |
| What is NUTS? | No-U-Turn Sampler: HMC variant that auto-tunes trajectory length by detecting when trajectory starts doubling back. Stan's default sampler. |
| What do divergences in Stan indicate? | Pathological posterior geometry (funnels, hard constraints). Not numerical noise — they're informative. Fix by reparameterizing (non-centered parameterization for hierarchical models). |
| What is partial pooling? | Hierarchical model shrinks group-level estimates toward the grand mean. Amount of shrinkage inversely proportional to group sample size. Better than both no-pooling (overfit) and complete-pooling (underfit). |
| How do you compute P(treatment > control) in Bayesian A/B? | Sample N draws from both posteriors; count fraction of draws where θ_B > θ_A. Conjugate: direct simulation from Beta posteriors. |
| LOO-CV vs WAIC — which to use? | LOO-CV (PSIS-LOO) is preferred. More robust to model misspecification. WAIC is asymptotically equivalent but less stable. Both implemented in ArviZ. |

---

## CS and Formal Methods Bridges

| Bayesian practice concept | CS / formal methods analogue |
|---|---|
| Prior → posterior updating (Bayes' theorem) | Belief state update in a Hidden Markov Model / Kalman filter: each observation refines the distribution over the hidden state; the posterior is the updated belief state; additional observations continue the update — Bayesian inference is online learning on the state space |
| Conjugate prior (posterior has closed form) | Type-preserving transformation: a conjugate prior is one that makes the posterior the same distributional family as the prior — the algebraic closure property; Beta-Binomial, Normal-Normal, Gamma-Poisson are the "closed under update" families |
| MCMC (Metropolis-Hastings, HMC) | Randomized search in state space: MCMC constructs a Markov chain whose stationary distribution is the posterior; each proposal is accepted/rejected based on the density ratio — identical in structure to simulated annealing and randomized optimization |
| HMC / NUTS (Hamiltonian Monte Carlo) | Gradient-guided search: uses the gradient of log-posterior to propose samples along high-probability trajectories; analogous to gradient descent in optimization but over a probability landscape rather than a loss surface |
| Divergences in Stan | Numerical instability diagnostic: divergences indicate the sampler encountered near-degenerate geometry (funnel, hard constraint boundary); they are a correctness warning, not just noise — equivalent to NaN propagation in floating-point computation signaling ill-conditioned operations |
| Non-centered parameterization | Change of variables to improve conditioning: θ_j = μ + τ × z_j where z_j ~ N(0,1) removes the correlation between τ and θ_j that causes funnel geometry — identical to preconditioning a linear system to improve solver convergence |
| Hierarchical / multilevel model (partial pooling) | Regularization via shared prior: group-level parameters are shrunk toward a grand mean; amount of shrinkage scales inversely with group sample size — identical to L2 regularization (ridge) in ML, where the prior precision matrix is the regularization strength |
| PSIS-LOO cross-validation | Out-of-sample evaluation without refitting: importance-weighted leave-one-out CV using Pareto-smoothed importance sampling; k̂ > 0.7 flags influential observations — analogous to held-out set evaluation with a warning system for high-leverage test points |
| Prior predictive check | Static analysis / type checking before runtime: simulate from the prior to verify the model produces plausible data ranges before fitting — catches modeling errors (scale misspecification, impossible predictions) without touching the data |

## Common Confusion Points

**Bayesian credible intervals are NOT automatically better than frequentist CIs:** They answer a different question (posterior probability vs coverage frequency). With diffuse priors, they produce similar numbers. With informative priors, they can differ substantially. The Bayesian CI is "better" if you want a probability statement and your prior is reasonable.

**MCMC samples ≠ independent samples:** MCMC chains have autocorrelation. ESS = 100 from 10,000 iterations means you have the effective information of 100 independent draws. Report and interpret ESS; don't treat total iteration count as sample size.

**Non-centered parameterization is not optional for hierarchical models:** Centered parameterization (θ_j ~ Normal(μ, τ)) often produces funnel geometry in Stan → many divergences → invalid inference. Non-centered (z_j ~ Normal(0,1); θ_j = μ + τ × z_j) resolves this. Standard in all modern hierarchical model implementations.

**The multiple comparisons "problem" is different in Bayesian framework, not absent:** Bayesian posterior probabilities are valid on their own terms. But if you test 100 variants and pick the one with P(win) = 98%, that's still likely a winner by chance (among 100, several would show 98% by noise). The solution is hierarchical modeling (shrinkage), not the Bayesian framework alone.
