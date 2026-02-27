# Bayesian Statistics

## The Big Picture

Bayesian statistics treats parameters as random variables and updates beliefs using data via Bayes' theorem.

```
+------------------------------------------------------------------+
|                    BAYESIAN WORKFLOW                             |
+------------------------------------------------------------------+
|                                                                  |
|  1. PRIOR                    2. LIKELIHOOD              3. POSTERIOR           |
|     p(theta)                    p(x | theta)               p(theta | x)        |
|  "What do I believe          "How probable is           "Updated beliefs       |
|   before seeing data?"        data given theta?"         after data"           |
|          |                          |                          |                |
|          +----------x--------------+                          |                |
|                     |                                          |                |
|             BAYES' THEOREM                                      |                |
|             p(theta|x) = p(x|theta) p(theta) / p(x)           |                |
|                          = p(x|theta) p(theta) /               |                |
|                            Integral p(x|theta) p(theta) dtheta |                |
|                                                                  |
|  4. PREDICTION                                                  |
|     p(x_new | x) = Integral p(x_new | theta) p(theta | x) dtheta              |
|     "Integrate out uncertainty in theta"                        |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Priors

**Informative priors**: Encode genuine prior knowledge.

```
  Coin fairness: theta ~ Beta(10, 10)
  (strong belief coin is fair; centered at 0.5 with low variance)

  Drug effect size: delta ~ Normal(0, 0.5)
  (most drugs have small effects; large effects are rare)
```

**Weakly informative priors**: Encode constraints without strong belief.

```
  Positive quantities: theta ~ Exponential(1) or Half-Normal
  Probabilities: theta ~ Beta(1, 1) = Uniform(0,1)
  Regression coefficients: beta ~ Normal(0, 10)
  (says effects are probably less than 30; not truly flat)
```

**Non-informative / reference priors**:

```
  Jeffreys prior: p(theta) proportional to sqrt(det I(theta))
  Invariant under reparametrization.
  For Normal mean: Jeffreys = Uniform on R (improper but OK)
  For Normal variance: Jeffreys = 1/sigma (improper; scale-invariant)

  Maximum entropy priors: given constraints, choose the prior
  with highest entropy (least information).
  With only mean constraint: p = Exponential.
  With only mean + variance constraints: p = Normal.
```

**Improper priors**: Unnormalized priors (Integral p(theta) dtheta = inf). Used when proper priors introduce undesired information. Posterior can still be proper (proper posterior from improper prior is fine; check carefully).

---

## Conjugate Priors

A **conjugate prior** is a prior such that the posterior is in the same family.

```
  Likelihood        Prior           Posterior
  +-----------+-----+------------+--+------------------+
  Bernoulli(p)      Beta(a,b)       Beta(a+x, b+1-x)
  Binomial(n,p)     Beta(a,b)       Beta(a+k, b+n-k)
  Poisson(lambda)   Gamma(a,b)      Gamma(a+Sum x_i, b+n)
  Normal(mu,sigma^2 Normal(m,v)     Normal(m', v')      (sigma^2 known)
  known)                            m' = (m/v + n*xbar/sigma^2)/(1/v + n/sigma^2)
  Normal(mu known,  Inv-Gamma(a,b)  Inv-Gamma(a+n/2, b+SS/2)
  sigma^2)
  Multinomial(p)    Dirichlet(a)    Dirichlet(a + counts)
  +-----------+-----+------------+--+------------------+
```

**Why conjugacy matters**: The posterior has a closed-form. No need for numerical integration. Sequential updating is trivial: yesterday's posterior is today's prior.

**The exponential family has conjugate priors**: For any exponential family likelihood, the conjugate prior is of the form:

```
  p(theta | chi, nu) proportional to exp(chi^T theta - nu A(theta))

  chi = prior sufficient statistics, nu = pseudo-sample-size
  Posterior: chi_new = chi + T(x), nu_new = nu + 1  (per observation)
```

---

## Posterior Computation

For non-conjugate models, the posterior denominator (marginal likelihood) is often intractable:

```
  p(theta | x) = p(x | theta) p(theta) / Integral p(x | theta') p(theta') dtheta'

  The denominator is typically a high-dimensional integral.
  Solutions: MCMC, variational inference, Laplace approximation.
```

### MCMC: Markov Chain Monte Carlo

Draw samples {theta^{(1)}, ..., theta^{(N)}} from p(theta | x) without computing the normalizing constant.

**Metropolis-Hastings**:

```
  Algorithm:
  1. Start at theta^{(0)}
  2. Propose theta* ~ q(theta* | theta^{(t)})
  3. Accept with probability:
     alpha = min(1, [p(theta*|x) q(theta^{(t)}|theta*)] /
                    [p(theta^{(t)}|x) q(theta*|theta^{(t)})])
  4. If accept: theta^{(t+1)} = theta*. Else: theta^{(t+1)} = theta^{(t)}.

  Key: Only the RATIO p(theta*|x)/p(theta^{(t)}|x) appears.
  The normalizing constant cancels! This is the key insight.

  Correct detailed balance: the chain's stationary distribution is p(theta|x).
```

**Gibbs sampling**: A special case of MH for multivariate theta = (theta_1, ..., theta_k):

```
  At each step, sample one component at a time:
  theta_j^{(t+1)} ~ p(theta_j | theta_{-j}^{(t)}, x)

  No rejection: always accept (the full conditional is used directly).
  Requires knowing the full conditionals p(theta_j | rest).
  Conjugate priors give tractable full conditionals.
```

**HMC (Hamiltonian Monte Carlo)**:

```
  Uses gradient information to make large, efficient proposals.
  Treat theta as position, introduce auxiliary momentum p.
  Simulate Hamiltonian dynamics: H(theta, p) = -log p(theta|x) + p^T p/2
  (Kinetic + potential energy)

  Proposal: simulate Hamiltonian trajectory (leapfrog integrator).
  Accept/reject to correct for discretization error.

  NUTS (No-U-Turn Sampler): Automatically tunes step size and path length.
  This is what Stan uses. Much more efficient than random-walk MH in
  high dimensions.
```

**Diagnosing MCMC**:

```
  R-hat (Gelman-Rubin): Compare within-chain and between-chain variance
  from multiple chains. R-hat ≈ 1 indicates convergence.

  Effective sample size (ESS): Accounts for autocorrelation.
  ESS = N / (1 + 2 Sum_k rho_k)  where rho_k = lag-k autocorrelation

  Trace plots: Visual check for mixing and stationarity.
  Burn-in: Discard early samples (before chain mixes).
```

---

## Variational Inference

MCMC is exact but slow. Variational inference (VI) is approximate but fast.

**Idea**: Approximate the posterior p(theta|x) with a simpler distribution q(theta; phi) from a tractable family. Minimize KL divergence:

```
  q*(theta) = argmin_{q in Q} D_KL(q(theta) || p(theta | x))

  Equivalent to maximizing the ELBO (Evidence Lower Bound):
  ELBO(phi) = E_q[log p(x, theta)] - E_q[log q(theta; phi)]
            = E_q[log p(x|theta)] - D_KL(q(theta;phi) || p(theta))

  log p(x) = ELBO(phi) + D_KL(q || p(theta|x))  >= ELBO(phi)

  So ELBO is a lower bound on log marginal likelihood.
  Maximizing ELBO <=> minimizing KL(q || posterior).
```

**Mean-field VI**: Assume q(theta) = Product_i q_i(theta_i) (factored posterior).

```
  Optimal factors (coordinate ascent variational inference, CAVI):
  q_j*(theta_j) proportional to exp(E_{-j}[log p(x, theta)])

  Iterate until convergence.
  Fast, but underestimates posterior uncertainty (variance collapse).
```

**Reparameterization trick** (for gradient-based VI):

```
  If theta = mu + sigma * epsilon, epsilon ~ Normal(0,1):
  Gradient w.r.t. phi passes through the sampling operation.
  Enables stochastic gradient optimization of ELBO.
  Foundation of VAEs (Variational Autoencoders).
```

<!-- @editor[bridge/P2]: No bridge from variational inference to probabilistic programming — this learner needs: "Stan implements HMC/NUTS; Pyro/NumPyro implements VI with reparameterization trick; Edward2/TFP implement both." The reparameterization trick is the implementation-level insight that makes modern probabilistic programming work, and connecting to the probabilistic programming ecosystem (Stan, Pyro, Turing.jl) is an explicit bridge this learner needs per the calibration. -->

---

## Model Selection and Comparison

**Bayes Factor**:

```
  BF_{12} = p(x | M_1) / p(x | M_2)
           = [Integral p(x|theta_1, M_1) p(theta_1) dtheta_1] /
             [Integral p(x|theta_2, M_2) p(theta_2) dtheta_2]

  BF > 10: Strong evidence for M_1
  BF > 100: Decisive evidence for M_1

  Inherent Occam's razor: M_1 with more parameters gets penalized
  because the parameter integral spreads probability over a larger space.
  Models that make precise predictions are not penalized.
```

**Bayesian Information Criterion (BIC)**:

```
  BIC = -2 log L(theta_hat) + k log n

  Approximation to -2 log p(x | M) for large n.
  Penalizes more parameters (k).
  Select model with lowest BIC.

  Key: BIC approximation becomes exact only as n -> inf.
  For small n, the Bayes factor is more principled.
```

**WAIC (Widely Applicable Information Criterion)**:

```
  WAIC = -2 Sum_i log E_theta[p(x_i | theta)] + 2 Sum_i Var_theta[log p(x_i|theta)]

  First term: log predictive density (how well model predicts data)
  Second term: effective number of parameters (estimated from posterior variance)

  Advantages over BIC:
  - Works for singular models (many neural networks)
  - Uses full posterior (not just MLE)
  - Valid for non-regular models
  - Approximately equal to leave-one-out cross-validation
```

**LOO-CV (Leave-One-Out Cross-Validation)**:

```
  log score = Sum_i log p(x_i | x_{-i})

  Pareto-smoothed importance sampling LOO (PSIS-LOO):
  Efficiently estimates LOO from a single posterior sample.
  Available in Stan/ArviZ. Provides diagnostic (Pareto k-hat).

  If k-hat > 0.7 for an observation: that observation is "influential"
  and PSIS-LOO estimate may be unreliable. Flag for investigation.
```

---

## Hierarchical Models

When you have groups of observations with shared structure:

```
  HIERARCHICAL (MULTILEVEL) MODEL:

  Group-level: theta_i ~ p(theta | hyperparameter phi)   (i = 1,...,G groups)
  Observation: x_{ij} | theta_i ~ p(x | theta_i)         (j = 1,...,n_i obs per group)
  Hyper-prior: phi ~ p(phi)

  PARTIAL POOLING:
  - Complete pooling: assume all theta_i = theta (ignores group differences)
  - No pooling: estimate each theta_i independently (ignores shared structure)
  - Partial pooling: hierarchical model borrows strength across groups
    Estimates for small groups shrink toward the overall mean.
    Estimates for large groups dominated by group data.

  The amount of shrinkage is DATA-ADAPTIVE (estimated from the data).
  This is superior to ad hoc regularization in many settings.
```

**Azure ML connection**: Hierarchical models appear in multi-task learning and federated learning — different clients share a prior distribution over model parameters, enabling knowledge transfer with partial pooling.

---

<!-- @editor[content/P1]: Bayesian nonparametrics is completely absent — this is an explicit "DOES need" in the learner calibration. Bayesian nonparametrics (Dirichlet process, Gaussian process regression as nonparametric Bayes, Chinese restaurant process, Indian buffet process, Pitman-Yor process) is the modern bridge between Bayesian statistics and machine learning. Missing: Dirichlet process mixture models, stick-breaking representation, the CRP as a generative model, and connection to modern topics like topic models (LDA) and neural network priors. This is P1 — explicitly called out as a gap. -->

## Bernstein-von Mises Theorem

The formal statement that "with enough data, the prior doesn't matter":

```
  Under regularity conditions, as n -> inf:
  The posterior p(theta | x_1,...,x_n) concentrates around the true theta_0,
  and after centering and scaling:

  sqrt(n)(theta - theta_hat) | x_1,...,x_n  --d-->  Normal(0, I(theta_0)^{-1})

  In other words: posterior ≈ Normal(theta_hat_MLE, I(theta_0)^{-1}/n)

  Implication: Bayesian credible intervals and frequentist confidence intervals
  agree to first order for large n. The prior is asymptotically irrelevant.
```

**Caveats**: BvM fails for:
- High-dimensional problems (p grows with n)
- Semiparametric and nonparametric models
- Models with non-identified parameters
- Singular models (neural networks often violate regularity)

---

## Decision Cheat Sheet

| Goal | Method | When to Use |
|---|---|---|
| Closed-form posterior | Conjugate prior | Model fits conjugate family |
| High-dimensional posterior | HMC / NUTS (Stan) | Complex models, n not huge |
| Very large data | Variational inference (ADVI) | Scalability needed |
| Compare models | LOO-CV (PSIS), WAIC, Bayes factor | Prefer LOO for practical use |
| Select model order | BIC | Large n, quick approximation |
| Borrow strength across groups | Hierarchical model | Grouped data with imbalance |
| Propagate parameter uncertainty | Posterior predictive | Predictions with uncertainty |

---

## Common Confusion Points

**"Bayesian updating is sequential — each update uses the previous posterior as prior."**
Yes, and this is exact: Bayes' theorem is associative. Update once on all data = update sequentially one observation at a time. The order doesn't matter. This makes online learning natural in the Bayesian framework.

**"MCMC samples are i.i.d. from the posterior."**
No. MCMC produces autocorrelated samples — consecutive samples are correlated. Effective sample size (ESS) accounts for this. For MH with random walk proposals, ESS can be much less than the number of MCMC iterations (typical HMC chains: ESS ~1000 from 2000 iterations; random walk MH: ESS ~100 from 2000 iterations).

**"Variational inference gives the correct posterior."**
VI gives an approximation. Mean-field VI systematically underestimates posterior variance (the KL direction q||p penalizes spreading q beyond where p has mass). This means credible intervals from VI are too narrow.

**"A flat (uniform) prior is objective / non-informative."**
Flat priors are not invariant under reparametrization. A Uniform(0,1) prior on p implies a non-uniform prior on log(p/(1-p)). Jeffreys priors are designed to be invariant. For many problems, weakly informative priors (Half-Normal, regularized horseshoe) are more principled than flat priors.
