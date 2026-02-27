# Information Geometry

## The Big Picture

Information geometry treats the set of probability distributions as a Riemannian manifold, with the Fisher information metric as the natural geometry. This gives a coordinate-free framework unifying statistics, information theory, and optimization.

```
+------------------------------------------------------------------+
|                   INFORMATION GEOMETRY LANDSCAPE                 |
+------------------------------------------------------------------+
|                                                                  |
|  STATISTICAL MANIFOLD S                                          |
|  = {p(x; theta) : theta in Theta}                               |
|  Each point is a probability distribution.                      |
|                                                                  |
|  GEOMETRY ON S:                                                  |
|  Fisher information metric g_{ij} = E[partial_i log p * partial_j log p]
|  (Riemannian metric on the manifold of distributions)           |
|                                                                  |
|  TWO NATURAL CONNECTIONS:                                        |
|  e-connection (exponential): flat for exponential families      |
|  m-connection (mixture): flat for mixture families              |
|  These are dual connections: together they determine the geometry|
|                                                                  |
|  DIVERGENCES (asymmetric distances):                            |
|  KL divergence D_KL(p||q)                                       |
|  alpha-divergences (generalization)                             |
|  Bregman divergences                                            |
|                                                                  |
|  APPLICATIONS:                                                   |
|  Natural gradient descent      Cramer-Rao bound (geodesic)     |
|  Sufficient statistics         EM algorithm (e/m projections)  |
|  Hypothesis testing geometry   Neural network optimization     |
+------------------------------------------------------------------+
```

---

## The Statistical Manifold

A parametric family {p(x; theta) : theta in Theta subset R^k} is a **statistical manifold** — a k-dimensional smooth manifold where each point is a probability distribution.

**Connection to information-theory/**: See that directory for entropy and KL divergence fundamentals. This module builds on them with geometric structure.

**Connection to differential-geometry/**: The statistical manifold is literally a Riemannian manifold — see that directory for the definition and machinery of Riemannian geometry. The Fisher information metric IS a Riemannian metric.

```
  Point in manifold:     a distribution p(x; theta)
  Tangent vector at p:   partial_theta log p(x; theta) = score function
  Riemannian metric:     Fisher information matrix g_ij(theta)

  The score function s(x; theta) = partial/partial_theta log p(x; theta)
  acts as a tangent vector: it points in the direction of maximum
  change in the distribution.
```

---

## The Fisher Information Metric

**Definition**: The Fisher information matrix is the metric tensor of the statistical manifold:

```
  g_{ij}(theta) = I_{ij}(theta)
               = E_theta[partial_i log p(x;theta) * partial_j log p(x;theta)]
               = -E_theta[partial_i partial_j log p(x;theta)]

  (Both forms are equal under regularity conditions.)

  This is a positive semi-definite matrix at each theta.
  It defines inner products on tangent vectors (score functions).
```

**Why this is the "right" metric**:

1. **Invariance**: The Fisher metric is the unique Riemannian metric invariant under sufficient statistics — reparametrizations that preserve statistical information.

2. **Local approximation of KL divergence**:

```
  D_KL(p(theta) || p(theta + dtheta))
  = (1/2) dtheta^T I(theta) dtheta + O(||dtheta||^3)

  The Fisher metric is the second-order Taylor coefficient of KL divergence.
  It measures "statistical distinguishability" between nearby distributions.
```

3. **Cramér-Rao bound as a metric bound**:

```
  Cov(T) >= I(theta)^{-1}  (for unbiased T)

  In information-geometric language: the achievable variance of an
  unbiased estimator is bounded by the metric tensor (inverse Fisher).
  The bound is achieved by the geodesic path in the statistical manifold.
```

---

## KL Divergence as Geometry

The KL divergence is not a metric (it is asymmetric, doesn't satisfy triangle inequality), but it is the natural divergence on the statistical manifold.

```
  D_KL(p || q) = Integral p(x) log(p(x)/q(x)) dx
               = E_p[log p(x) - log q(x)]
               = E_p[log p(x)] - E_p[log q(x)]
               = -H(p) + H(p, q)
  where H(p) = entropy, H(p,q) = cross-entropy.

  D_KL(p||q) >= 0 with equality iff p = q (Gibbs' inequality).
  D_KL(p||q) != D_KL(q||p) in general.
```

**Pythagorean theorem in information geometry**:

```
  For distributions p, q, r with specific flatness conditions:
  D_KL(p || r) = D_KL(p || q) + D_KL(q || r)

  This holds when q is the "e-projection" of r onto an e-flat submanifold
  containing p. (And analogously for m-projections and m-flat submanifolds.)

  This is the statistical analogue of the Pythagorean theorem.
  The EM algorithm is exactly this: M-step = e-projection of the
  completed-data sufficient statistics onto the model manifold.
```

**The two KL divergence directions** and their projections:

```
  FORWARD KL: D_KL(p_data || q_model)     "M-projection"
  Minimizing: forces q to cover all modes of p (moment matching).
  If q = Normal family: q_hat has same mean and variance as p_data.
  Used in: MLE (which IS forward KL minimization).

  REVERSE KL: D_KL(q_model || p_data)     "E-projection"
  Minimizing: forces q to concentrate on ONE mode of p.
  "Zero-forcing": q prefers to be 0 where p is 0 (avoids hallucinating).
  Used in: Variational inference (ELBO = -KL + constant).

  This asymmetry is why mean-field VI underestimates variance:
  reverse KL penalizes putting mass where p_data is small.
```

---

<!-- @editor[content/P2]: Missing Wasserstein geometry — the optimal transport / Wasserstein distance has become as important as the KL divergence in modern ML (GANs, distributional robustness, domain adaptation). The Fisher metric is the right geometry for exponential families; Wasserstein is the right geometry for distributions supported on a metric space (interpolating between distributions while respecting the ground metric). A brief contrast (KL geometry vs. Wasserstein geometry, when each is appropriate) would complete the picture for a learner who will encounter both in deep learning contexts. -->

## Alpha-Divergences

A one-parameter family generalizing KL divergence:

```
  D_alpha(p || q) = [4/(1-alpha^2)] [1 - Integral p(x)^{(1+alpha)/2} q(x)^{(1-alpha)/2} dx]

  alpha = 1:  Forward KL divergence D_KL(p||q)
  alpha = -1: Reverse KL divergence D_KL(q||p)
  alpha = 0:  Hellinger divergence (symmetric)
  alpha = 3:  Chi-squared divergence (between p and q)

  The Fisher metric is recovered from all alpha-divergences:
  D_alpha(p(theta) || p(theta + dtheta)) = (1/2)(1-alpha^2)/4 * dtheta^T I dtheta + O(||dtheta||^3)

  All alpha-divergences have the same second-order term!
  The Fisher metric is the universal local geometry.
```

---

## Exponential and Mixture Families: Dual Flatness

The key structural result: exponential families and mixture families are flat submanifolds (with different connections).

**e-flat (exponential flat)**: A submanifold M is e-flat if, for any two points p, q in M, the exponential connecting family {p^{1-t} q^t / Z} (geometric interpolation) stays in M.

```
  EXPONENTIAL FAMILY is e-flat:
  p(x; theta) = h(x) exp(eta^T T(x) - A(eta))

  In natural parameters eta, the e-geodesics are straight lines.
  The e-connection is flat in these coordinates.
  Corollary: MLE of exponential family is a e-projection.
```

**m-flat (mixture flat)**: A submanifold M is m-flat if, for any two points p, q in M, the mixture (1-t)p + tq stays in M.

```
  MIXTURE FAMILY is m-flat:
  p(x; lambda) = Sum_k lambda_k p_k(x)

  In mixture (expectation) parameters mu = E_p[T(x)], the
  m-geodesics are straight lines.
  The m-connection is flat in these coordinates.
```

**Duality**: The e-connection and m-connection are dual with respect to the Fisher metric. This is the Amari-Nagaoka duality, and it is why exponential families have both natural parameters (e-coordinates) and expectation parameters (m-coordinates) related by the Legendre transform of A(eta).

```
  e-coordinates (natural params): eta_i
  m-coordinates (expectation params): mu_i = E[T_i(x)] = partial A/partial eta_i

  Legendre transform: A*(mu) = eta^T mu - A(eta)  (A* = convex conjugate of A)
  A(eta) + A*(mu) = eta^T mu  (Legendre duality)

  This is the SAME structure as convex duality in optimization.
  Statistical geometry and convex optimization are dual.
```

---

## Natural Gradient

The standard gradient descent uses Euclidean geometry in parameter space — which is arbitrary and ignores the statistical structure.

**Ordinary gradient**:

```
  theta_{t+1} = theta_t - alpha * gradient_theta L(theta_t)

  The gradient depends on how theta is parameterized.
  Changing parameterization changes the gradient direction.
  This is problematic: the optimization path changes with reparametrization.
```

**Natural gradient** (Amari 1998):

```
  theta_{t+1} = theta_t - alpha * I(theta_t)^{-1} gradient_theta L(theta_t)

  Precondition the gradient by the inverse Fisher information matrix.
  This is the gradient in the intrinsic geometry of the statistical manifold.

  KEY PROPERTY: Natural gradient is invariant under reparametrization.
  If you change coordinates from theta to phi(theta), the natural gradient
  gives the same update in distribution space.
```

**Why natural gradient is faster**:

```
  Standard gradient: steepest descent in Euclidean parameter space.
  Natural gradient: steepest descent on the statistical manifold.

  The Fisher metric captures "how much the distribution changes" per
  unit parameter change. The natural gradient moves in the direction
  of maximum improvement per unit KL divergence change.

  For exponential families: I(theta)^{-1} is the Hessian of A*(mu).
  Natural gradient = Newton's method for exponential families.
  Natural gradient converges in O(1) steps where SGD needs O(1/epsilon).
```

**In practice — K-FAC and its variants**:

```
  I(theta)^{-1} is expensive to compute (d x d matrix, d = # parameters).
  For neural networks: d ~ millions or billions.

  Approximations:
  K-FAC (Kronecker-Factored Approximate Curvature):
  Approximates I as a Kronecker product of smaller matrices.
  Used in deep learning optimization.

  Adam optimizer: approximates natural gradient with diagonal Fisher.
  (Adam ~ diagonal pre-conditioning with adaptive learning rate.)
  This explains why Adam works well empirically.
```

---

## EM Algorithm as Dual Projections

The Expectation-Maximization algorithm has a clean information-geometric interpretation.

```
  GOAL: maximize log p(x; theta) where x is incomplete/latent data.

  At each step, alternate between:
  E-STEP: compute Q(theta, theta^{(t)}) = E_{z|x,theta^{(t)}}[log p(x,z; theta)]
  M-STEP: theta^{(t+1)} = argmax Q(theta, theta^{(t)})

  GEOMETRIC INTERPRETATION (Csiszar duality):
  The E-step is an m-projection of the completed distribution
  onto the submanifold where the hidden variable distribution
  matches its conditional given current theta.

  The M-step is an e-projection back onto the model manifold.

  Convergence: each alternating projection decreases KL divergence.
  Not guaranteed to find global maximum (saddle points possible).
```

---

## Connections to Other Library Directories

```
  information-theory/
    Entropy: H(p) = -E_p[log p] (this is the log-partition minus energy)
    KL divergence D_KL(p||q) = E_p[log p/q] (basis of 09-INFORMATION-GEOMETRY)
    Mutual information I(X;Y) = D_KL(p(X,Y) || p(X)p(Y))
    Channel capacity = geometric optimization on simplex of input distributions

  differential-geometry/
    The statistical manifold IS a Riemannian manifold (see 04-RIEMANNIAN-GEOMETRY)
    Connections, curvature, geodesics all apply (see 05-CONNECTIONS, 06-CURVATURE)
    The e- and m-connections are the two canonical affine connections on S
    Lie groups appear: exponential map on statistical manifold ~ exponential family

  data-science/
    Natural gradient -> K-FAC -> Adam optimizer (deep learning)
    Variational inference = reverse KL minimization on posterior manifold
    VAE (Variational Autoencoder) = ELBO optimization (ELBO = -KL + log likelihood)
    Gaussian processes: the Fisher metric for GP family gives natural GP updates
```

---

## Sanov's Theorem: Large Deviations and KL Divergence

Connecting large deviations theory (03-LIMIT-THEOREMS) to information geometry:

```
  Let Q = {q : Integral f dq <= r} (some constraint on distributions).
  P_0 is the true distribution.

  P_0^n(empirical distribution P_n in Q) ~ exp(-n * D_KL(Q* || P_0))

  Where Q* = argmin_{q in Q} D_KL(q || P_0)  (the "nearest" distribution in Q to P_0)

  The exponent is the KL divergence!

  In other words: the probability of the empirical distribution
  falling in a "wrong" set Q decays exponentially at rate
  = KL divergence between the closest wrong distribution and the truth.

  This is the geometric version of large deviations:
  hypothesis testing and large deviations are dual.
```

---

## Decision Cheat Sheet

| Concept | What It Is | Used For |
|---|---|---|
| Fisher metric | Riemannian metric on distribution space | Cramer-Rao, natural gradient |
| KL divergence (forward) | D_KL(data \|\| model) | MLE, moment matching |
| KL divergence (reverse) | D_KL(model \|\| data) | Variational inference |
| Natural gradient | Fisher-preconditioned gradient | Efficient optimization |
| e-flat manifold | Exponential family geometry | MLE is a projection |
| m-flat manifold | Mixture family geometry | Moment matching is a projection |
| EM algorithm | Alternating dual projections | Latent variable models |
| Alpha-divergence | Generalization of KL | Robust estimation |

---

## Common Confusion Points

**"KL divergence is a distance."**
KL divergence is a divergence (measures separation), not a distance. It is not symmetric: D_KL(p||q) != D_KL(q||p) in general. It does not satisfy the triangle inequality. The square root of the Fisher metric gives a true distance (geodesic distance on the statistical manifold).

**"Natural gradient always helps."**
Natural gradient is theoretically optimal but computing the Fisher inverse is O(d^3) for d parameters. For modern neural networks with millions of parameters, this is infeasible without approximation. K-FAC and similar methods approximate it; Adam provides a diagonal approximation. The benefit depends on the curvature structure of the loss landscape.

**"The two KL directions are interchangeable for practical purposes."**
They are not. Forward KL (MLE) forces the model to cover all modes of the data. Reverse KL (VI) forces the model onto one mode (mode-seeking behavior). For multimodal posteriors, VI with reverse KL may miss modes. This is a fundamental qualitative difference.

**"The exponential family e-flat geometry is a curiosity."**
It is the structural reason exponential families are so tractable. The MLE for any exponential family is a sufficient statistic match (no numerical optimization needed in principle). Conjugate Bayesian updating is e-flat projection. The EM algorithm's convergence guarantee is the dual projections theorem. The geometry explains all the tractability.

<!-- @editor[content/P2]: Missing the connection between information geometry and statistical learning theory — specifically, the role of the Fisher information matrix in neural tangent kernel theory (NTK), and how the natural gradient / K-FAC connects to the geometry of the loss landscape in overparameterized networks. For a learner with TCS background who will read about NTK and double-descent, the information-geometric perspective on why flat directions in the Fisher matrix correspond to the implicit regularization of SGD would be a valuable addition. -->
