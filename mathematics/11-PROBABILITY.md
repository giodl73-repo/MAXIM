# 11 — Probability & Statistics

```
PROBABILITY LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Sample space Ω ──► events (subsets) ──► probability measure P: 2^Ω → [0,1]
         │
         │  Random variables X: Ω → ℝ
         │         │
         │         ├── Discrete  ── PMF p(x) = P(X=x)
         │         └── Continuous ── PDF f(x), CDF F(x) = ∫_{-∞}^x f(t)dt
         │
         ├── Expectation, variance, moments
         ├── Joint distributions, independence, conditioning
         ├── Limit theorems: LLN, CLT
         └── Stochastic processes: Markov chains, Poisson process

  PHYSICS CONNECTION:
    Statistical mechanics ──► Boltzmann distribution, partition functions
    QM ──► Born rule |ψ|² = probability density
    Algorithms ──► Master Theorem (recurrences), randomized complexity
```

---

## 1. Kolmogorov Axioms — The Foundation

### Probability Space (Ω, ℱ, P)

| Component | Definition | Example (fair die) |
|-----------|------------|-------------------|
| **Ω** | Sample space — all outcomes | {1,2,3,4,5,6} |
| **ℱ** | σ-algebra of events (subsets closed under complement and countable union) | All 2⁶ subsets |
| **P** | Probability measure | P({k}) = 1/6 |

### Three Axioms

```
  K1: P(A) ≥ 0             for all A ∈ ℱ
  K2: P(Ω) = 1
  K3: If A₁, A₂,... disjoint, then P(⋃ᵢ Aᵢ) = Σᵢ P(Aᵢ)   (countable additivity)

  Everything else is a theorem:
    P(∅) = 0
    P(Aᶜ) = 1 - P(A)
    P(A∪B) = P(A) + P(B) - P(A∩B)          (inclusion-exclusion)
    P(A) ≤ P(B) if A ⊆ B
```

### Conditional Probability

```
  P(A|B) = P(A∩B) / P(B)     (B is the new universe)

  Chain rule:  P(A∩B∩C) = P(A|B∩C)·P(B|C)·P(C)

  Total probability:  P(A) = Σₖ P(A|Bₖ)·P(Bₖ)    where {Bₖ} partition Ω

  Bayes' theorem:
    P(H|E) = P(E|H)·P(H) / P(E)
           = P(E|H)·P(H) / [P(E|H)·P(H) + P(E|Hᶜ)·P(Hᶜ)]

    prior P(H) × likelihood P(E|H) → posterior P(H|E)
```

**Independence**: A and B are independent iff P(A∩B) = P(A)·P(B)
(equivalently P(A|B) = P(A))

---

## 2. Random Variables and Distributions

### Discrete Distributions

| Distribution | PMF p(k) | Mean | Variance | Use |
|---|---|---|---|---|
| **Bernoulli(p)** | p^k(1-p)^(1-k), k∈{0,1} | p | p(1-p) | Single trial |
| **Binomial(n,p)** | C(n,k)p^k(1-p)^(n-k) | np | np(1-p) | n independent trials |
| **Geometric(p)** | (1-p)^(k-1)p, k≥1 | 1/p | (1-p)/p² | Waiting time to first success |
| **Poisson(λ)** | e^(-λ)λ^k/k! | λ | λ | Rare events in interval |
| **Negative Binomial(r,p)** | C(k-1,r-1)p^r(1-p)^(k-r) | r/p | r(1-p)/p² | r-th success |

**Poisson as limit of Binomial**: n→∞, p→0, np=λ fixed → Binomial(n,p) → Poisson(λ)

### Continuous Distributions

| Distribution | PDF f(x) | Mean | Variance | Use |
|---|---|---|---|---|
| **Uniform(a,b)** | 1/(b-a) | (a+b)/2 | (b-a)²/12 | No information |
| **Exponential(λ)** | λe^(-λx), x≥0 | 1/λ | 1/λ² | Waiting times, memoryless |
| **Gaussian N(μ,σ²)** | (1/σ√2π)e^(-(x-μ)²/2σ²) | μ | σ² | CLT limit, everywhere |
| **Gamma(α,β)** | x^(α-1)e^(-x/β)/(β^α Γ(α)) | αβ | αβ² | Sum of α exponentials |
| **Beta(α,β)** | x^(α-1)(1-x)^(β-1)/B(α,β) | α/(α+β) | αβ/[(α+β)²(α+β+1)] | Probabilities (x∈[0,1]) |
| **Cauchy** | 1/[π(1+x²)] | undefined | undefined | Heavy tails, no CLT |
| **Log-normal** | (1/xσ√2π)e^(-(ln x-μ)²/2σ²) | e^(μ+σ²/2) | — | Multiplicative processes |
| **χ²(k)** | — | k | 2k | Sum of k squared Gaussians |

### Moments and Generating Functions

```
  Raw moment:    μₙ = E[Xⁿ] = ∫ xⁿ f(x) dx
  Central moment: E[(X-μ)ⁿ]

  Mean:      μ = E[X]
  Variance:  σ² = E[(X-μ)²] = E[X²] - (E[X])²
  Std dev:   σ = √Var(X)
  Skewness:  E[(X-μ)³]/σ³         (asymmetry)
  Kurtosis:  E[(X-μ)⁴]/σ⁴ - 3    (tail weight; Gaussian = 0)

  Moment Generating Function:
    M_X(t) = E[e^(tX)] = Σ μₙ tⁿ/n!

    M_X'(0) = E[X],  M_X''(0) = E[X²], etc.

  Characteristic Function:
    φ_X(t) = E[e^(itX)]    (always exists — Fourier transform of PDF)
    Uniquely determines distribution.
    For independent X,Y:  φ_{X+Y}(t) = φ_X(t)·φ_Y(t)
```

---

## 3. Joint Distributions and Independence

```
  Joint PDF:   f_{X,Y}(x,y)     with ∫∫ f_{X,Y} dx dy = 1

  Marginals:   f_X(x) = ∫ f_{X,Y}(x,y) dy
               f_Y(y) = ∫ f_{X,Y}(x,y) dx

  Independent:  f_{X,Y}(x,y) = f_X(x)·f_Y(y)  ⟺  X ⊥ Y

  Conditional:  f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)

  Covariance:   Cov(X,Y) = E[XY] - E[X]E[Y] = E[(X-μ_X)(Y-μ_Y)]
  Correlation:  ρ = Cov(X,Y)/(σ_X σ_Y)    ∈ [-1,1]

  X ⊥ Y  ⟹  Cov(X,Y) = 0   (converse false in general)
```

### Multivariate Gaussian

```
  X ~ N(μ, Σ)   where μ ∈ ℝⁿ, Σ = covariance matrix (PSD)

  PDF: f(x) = (2π)^(-n/2)|Σ|^(-1/2) exp(-½(x-μ)ᵀΣ⁻¹(x-μ))

  Key: Level sets are ellipsoids.
       Marginals are Gaussian.
       X ⊥ Y iff Cov(X,Y) = 0 (only for Gaussians is ρ=0 ⟹ independence)
       Linear transform:  AX + b ~ N(Aμ + b, AΣAᵀ)
```

---

## 4. Limit Theorems

### Law of Large Numbers (LLN)

```
  Weak LLN (Chebyshev):
    X₁, X₂,... iid with mean μ, finite variance σ²
    X̄ₙ = (X₁+...+Xₙ)/n

    For any ε > 0:  P(|X̄ₙ - μ| > ε) → 0  as n → ∞
    Proof: Var(X̄ₙ) = σ²/n → 0, apply Chebyshev P(|Z-E[Z]|≥ε) ≤ Var(Z)/ε²

  Strong LLN:  X̄ₙ → μ  almost surely (with probability 1)
```

### Central Limit Theorem (CLT)

```
  X₁,...,Xₙ iid, mean μ, variance σ²

  Zₙ = (X̄ₙ - μ)/(σ/√n) = √n(X̄ₙ - μ)/σ  →  N(0,1)  in distribution

  Equivalently: Σᵢ Xᵢ ~ N(nμ, nσ²) approximately for large n

  Physical intuition: Independent random contributions add.
    Each step doesn't "know" the distribution — the sum always Gaussianizes.
    This is why Gaussian appears everywhere: it's the attractor of sums.

  Rate of convergence: Berry-Esseen: |P(Zₙ ≤ x) - Φ(x)| ≤ C·ρ/(σ³√n)
    where ρ = E[|X-μ|³]  (third absolute moment)

  When CLT fails:
    - Infinite variance (Cauchy, power law tails α ≤ 2)
    - Dependent random variables (need mixing conditions)
    → Heavy-tailed sums → stable distributions (Lévy, Pareto)
```

### Markov and Chebyshev Inequalities

```
  Markov (one-sided, X ≥ 0):   P(X ≥ a) ≤ E[X]/a

  Chebyshev:    P(|X - μ| ≥ kσ) ≤ 1/k²
    No assumptions on distribution — holds universally.
    k=2: ≤ 25% of probability outside 2σ   (vs 4.6% for Gaussian)
    k=3: ≤ 11%  (vs 0.3%)

  Chernoff bound (tightest for sums of bounded r.v.):
    P(X ≥ a) ≤ e^(-ta)·M_X(t) for any t > 0
    Exponentially tight — use for randomized algorithm analysis
```

---

## 5. Master Theorem — Recurrences

Used to analyze divide-and-conquer algorithms. Appears everywhere in CS theory.

### The Setup

```
  T(n) = a·T(n/b) + f(n)

  a = number of subproblems
  b = size reduction factor (n/b per subproblem)
  f(n) = work at this level (split + merge cost)

  Critical exponent:  c* = log_b(a) = log(a)/log(b)
```

### Three Cases

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Compare f(n) vs n^(c*)                                             │
  │                                                                     │
  │  Case 1: f(n) = O(n^(c*-ε))  for some ε > 0                        │
  │    Subproblems dominate — leaves do most work                       │
  │    T(n) = Θ(n^c*)                                                   │
  │                                                                     │
  │  Case 2: f(n) = Θ(n^(c*) · log^k(n))  for some k ≥ 0              │
  │    Balanced — work spread across all levels                         │
  │    T(n) = Θ(n^(c*) · log^(k+1)(n))                                 │
  │    Common: f(n) = Θ(n^c*) → k=0 → T(n) = Θ(n^c* log n)            │
  │                                                                     │
  │  Case 3: f(n) = Ω(n^(c*+ε))  for some ε > 0,                       │
  │    AND  a·f(n/b) ≤ c·f(n)  for c < 1  (regularity condition)       │
  │    Top level dominates — root does most work                        │
  │    T(n) = Θ(f(n))                                                   │
  └─────────────────────────────────────────────────────────────────────┘
```

### Classic Examples

| Recurrence | a | b | f(n) | c*=log_b(a) | Case | T(n) |
|---|---|---|---|---|---|---|
| Merge sort: T(n) = 2T(n/2) + n | 2 | 2 | n | 1 | 2 (k=0) | **Θ(n log n)** |
| Binary search: T(n) = T(n/2) + 1 | 1 | 2 | 1 | 0 | 2 | **Θ(log n)** |
| Strassen: T(n) = 7T(n/2) + n² | 7 | 2 | n² | log₂7≈2.807 | 1 | **Θ(n^2.807)** |
| Naive matrix mult: T(n) = 8T(n/2) + n² | 8 | 2 | n² | 3 | 1 | **Θ(n³)** |
| T(n) = 4T(n/2) + n² | 4 | 2 | n² | 2 | 2 | **Θ(n² log n)** |
| T(n) = 2T(n/2) + n² | 2 | 2 | n² | 1 | 3 | **Θ(n²)** |

**Intuition for cases**: draw the recursion tree. Level k has aᵏ nodes each doing f(n/bᵏ) work.
- Case 1: geometric series dominated by leaves (aᵏ nodes × tiny work)
- Case 2: each level does same work → multiply by log n levels
- Case 3: geometric series dominated by root

**Akra-Bazzi** extends this to unequal splits and multiple terms.

---

## 6. Markov Chains

### Discrete-Time Markov Chain

```
  State space S = {1,...,n}  (or countably infinite)

  Markov property: P(Xₜ₊₁ = j | Xₜ = i, Xₜ₋₁, ..., X₀) = P(Xₜ₊₁ = j | Xₜ = i)
    "The future depends on the present, not the history"

  Transition matrix:  Pᵢⱼ = P(Xₜ₊₁ = j | Xₜ = i)
    Rows sum to 1:  Σⱼ Pᵢⱼ = 1   (stochastic matrix)

  n-step transitions:  P(Xₙ = j | X₀ = i) = (Pⁿ)ᵢⱼ

  State distribution at time t:  πₜ = π₀ · Pᵗ   (row vector × matrix)
```

### Classification

```
  Communicating classes: i ↔ j if i → j and j → i
    Irreducible: one communicating class (all states communicate)

  Recurrent: P(return to i | start at i) = 1
  Transient: P(return to i | start at i) < 1

  Period d(i) = gcd{n ≥ 1 : P(Xₙ=i|X₀=i) > 0}
  Aperiodic: d(i) = 1 for all i
```

### Stationary Distribution

```
  π is stationary if πP = π  (left eigenvector of P with eigenvalue 1)

  Equivalently: πⱼ = Σᵢ πᵢ Pᵢⱼ  for all j,  with Σⱼ πⱼ = 1

  Detailed balance (sufficient but not necessary):
    πᵢ Pᵢⱼ = πⱼ Pⱼᵢ   for all i,j
    (reversible chains — MCMC exploits this)
```

### Convergence (Ergodic Theorem)

```
  Irreducible + Aperiodic ⟹ unique stationary π,  and
    Pⁿ → Π  (matrix of identical rows = π)   as n → ∞

  Rate: |Pᵢⱼⁿ - πⱼ| ≤ λ₂ⁿ   where λ₂ = second-largest eigenvalue magnitude
  Mixing time: τ_mix ∝ 1/(1 - λ₂)

  Time average = space average:
    (1/T)Σₜ f(Xₜ) → Σᵢ πᵢ f(i)   a.s.   (ergodic theorem)
```

### Example: Google PageRank

```
  Web = directed graph. Pᵢⱼ = 1/deg(i) if edge i→j.
  Add teleportation: P' = αP + (1-α)(1/n)1·1ᵀ
  PageRank = stationary distribution π of P'.
  Computed via power iteration: πₜ₊₁ = πₜP'.
```

### Poisson Process

```
  Events arrive at rate λ per unit time.
  N(t) = count of events in [0,t] ~ Poisson(λt)
  Interarrival times: T₁, T₂,... iid Exponential(λ)

  Memoryless: P(T > s+t | T > s) = P(T > t)
    The exponential distribution is the unique memoryless continuous distribution.
    → Justifies Markov assumption in continuous-time models.

  Superposition: Poisson(λ₁) + Poisson(λ₂) = Poisson(λ₁+λ₂)
  Thinning: Keep each event with prob p → Poisson(pλ)
```

---

## 7. Bayesian Inference

```
  Prior: p(θ)          — beliefs before data
  Likelihood: p(D|θ)   — probability of data given parameters
  Posterior: p(θ|D) ∝ p(D|θ)·p(θ)   — updated beliefs

  Point estimates:
    MAP: θ_MAP = argmax p(θ|D)      (maximum a posteriori)
    MLE: θ_MLE = argmax p(D|θ)      (maximum likelihood — flat prior)

  Conjugate priors (posterior is same family as prior):
    Beta-Binomial: Beta(α,β) prior + n trials k successes → Beta(α+k, β+n-k)
    Gaussian-Gaussian: N(μ₀,σ₀²) prior + N(θ,σ²) data → Gaussian posterior
    Dirichlet-Multinomial: Dirichlet prior + categorical data → Dirichlet posterior

  MCMC (Markov Chain Monte Carlo):
    Sample from posterior when it's not analytically tractable.
    Metropolis-Hastings: proposal q(θ'|θ), accept with ratio p(θ'|D)q(θ|θ')/[p(θ|D)q(θ'|θ)]
    Detailed balance ⟹ stationary distribution = posterior.
    Gibbs sampling: special case — sample each variable conditioned on all others.
```

---

## 8. Boltzmann Distribution — Physics Connection

```
  System at temperature T. Energy levels E₁, E₂,...
  Probability of being in state with energy Eᵢ:

    P(state i) = e^(-Eᵢ/kT) / Z

  where  Z = Σᵢ e^(-Eᵢ/kT)   is the partition function.

  β = 1/(kT)  (inverse temperature)
  P(state i) = e^(-βEᵢ) / Z

  Physical intuition:
    Low T (β large): system concentrates on lowest energy states
    High T (β small): all states roughly equally probable

  Entropy: S = -k Σᵢ Pᵢ ln Pᵢ    (Gibbs/Shannon entropy)
  Free energy: F = -kT ln Z = ⟨E⟩ - TS    (minimize at equilibrium)

  Connection to probability:
    Boltzmann distribution = maximum entropy distribution
    subject to constraint ⟨E⟩ = fixed.
    Lagrange multiplier ⟹ β = 1/kT.

  Simulated annealing (optimization):
    Start with high T (explore). Cool slowly.
    At each step: accept proposal with P = min(1, e^(-ΔE/T))
    Mirrors physical annealing to find ground state.
```

### Entropy and Information Theory

```
  Shannon entropy: H(X) = -Σ p(x) log₂ p(x)   bits

  Uniform over n: H = log₂ n  (maximum entropy)
  Single outcome: H = 0

  KL divergence (not a metric — not symmetric):
    D_KL(P||Q) = Σ p(x) log(p(x)/q(x)) ≥ 0
    = 0 iff P = Q  (by Jensen's inequality)

  Cross-entropy: H(P,Q) = -Σ p(x) log q(x) = H(P) + D_KL(P||Q)
    → Loss function in ML classification

  Mutual information: I(X;Y) = D_KL(P_{X,Y} || P_X P_Y)
    = H(X) + H(Y) - H(X,Y)
    = H(X) - H(X|Y)
    → 0 iff X,Y independent
```

---

## 9. Common Distributions in Physics and CS

| Context | Distribution | Why |
|---|---|---|
| Radioactive decay counts | Poisson | Independent rare events |
| Thermal fluctuations | Gaussian | Sum of many kicks (CLT) |
| Particle velocities (kinetic theory) | Maxwell-Boltzmann | Max entropy + fixed ⟨E⟩ |
| Energy levels | Boltzmann | Max entropy + fixed ⟨E⟩ |
| Quantum spin measurement | Bernoulli | Two outcomes: ±ℏ/2 |
| Network degree | Power law | Scale-free networks |
| Hash collision analysis | Birthday / Poisson | √n collision threshold |
| Randomized quicksort | Geometric | Expected pivot position |
| Financial returns | Log-normal (approx) | Multiplicative shocks |
| Turbulence (intermittent) | Lévy / stable | Infinite variance |

---

## 10. Decision Cheat Sheet

| You need to... | Tool |
|---|---|
| Model counts in interval | Poisson(λ) |
| Model k successes in n trials | Binomial(n,p) |
| Model waiting time (continuous) | Exponential(λ) |
| Model sum of many effects | Gaussian (CLT) |
| Model proportions / probabilities | Beta(α,β) |
| Update beliefs given data | Bayes' theorem |
| Bound tail probability, any distribution | Chebyshev |
| Bound tail for bounded r.v., tight | Chernoff |
| Analyze divide-and-conquer T(n) | Master Theorem |
| Find long-run behavior of system | Markov chain stationary π |
| Sample from intractable posterior | MCMC (Metropolis/Gibbs) |
| Model physical state probabilities | Boltzmann e^(-βE)/Z |
| Quantify information / compression | Shannon entropy H(X) |
| Measure distribution distance | KL divergence D_KL |

---

## 11. Common Confusion Points

**1. P(A|B) ≠ P(B|A) — Prosecutor's fallacy**
P(DNA match | innocent) is tiny, but P(innocent | DNA match) depends on prior — base rate matters. Confusing them is the prosecutor's fallacy. Bayes' theorem is the fix.

**2. Independence vs uncorrelatedness**
Cov(X,Y) = 0 does not imply independence (except for Gaussians). X and X² are uncorrelated if X is symmetric around 0 but maximally dependent. Independence ⟹ uncorrelated, not vice versa.

**3. CLT requires finite variance**
Cauchy distribution has no mean or variance. Sum of n Cauchy r.v. / n is still Cauchy — the CLT does not apply. Power-law distributions with tail index α ≤ 2 similarly escape CLT convergence.

**4. Master Theorem gaps**
The Master Theorem doesn't cover all cases: T(n) = 2T(n/2) + n/log(n) falls in the gap between cases 1 and 2. Akra-Bazzi or direct analysis needed. Also requires a and b to be positive constants, not functions of n.

**5. Stationary ≠ starting distribution**
π is where the chain converges to, not where it starts. PageRank starts from uniform and iterates to convergence. The chain needs to be irreducible + aperiodic for convergence to π to be guaranteed.

**6. Entropy and physical entropy differ by scale**
Shannon H (bits) = k_B·S_physics / (k_B ln 2). Both measure the same thing (missing information / uncertainty), just in different units. The Boltzmann factor e^(-E/kT) can be understood as maximum-entropy inference given a mean energy constraint.
