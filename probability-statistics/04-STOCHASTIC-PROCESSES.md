# Stochastic Processes

## The Big Picture

A stochastic process is a collection of random variables indexed by time (or space): {X_t, t in T}. The theory studies how randomness evolves.

```
+------------------------------------------------------------------+
|                  STOCHASTIC PROCESS TAXONOMY                     |
+------------------------------------------------------------------+
|                                                                  |
|  INDEX SET T         STATE SPACE S          KEY PROCESSES        |
|  +---------------+   +---------------+      +----------------+  |
|  | Discrete time |   | Discrete       |  ->  | Markov chains  |  |
|  | T = {0,1,2,...}|  | (countable)    |      | Random walks   |  |
|  +---------------+   +---------------+      +----------------+  |
|  | Continuous    |   | Discrete       |  ->  | Poisson process|  |
|  | T = [0, inf)  |   | (countable)    |      | Birth-death    |  |
|  +---------------+   +---------------+      +----------------+  |
|  | Continuous    |   | Continuous     |  ->  | Brownian motion|  |
|  | T = [0, inf)  |   | R or R^n       |      | Diffusions     |  |
|  +---------------+   +---------------+      +----------------+  |
|  | Continuous    |   | Continuous     |  ->  | Gaussian field |  |
|  | T = R^d       |   | R              |      | (spatial stats)|  |
|  +---------------+   +---------------+      +----------------+  |
|                                                                  |
|  SPECIAL PROPERTIES:                                            |
|  Markov: future depends only on present                         |
|  Martingale: E[X_{t+1} | past] = X_t  (fair game)              |
|  Stationary: distribution doesn't change with time shift        |
|  Ergodic: time average = ensemble average (a.s.)               |
+------------------------------------------------------------------+
```

---

## Filtrations and Adaptedness

The measure-theoretic setup for processes:

```
  FILTRATION: increasing sigma-algebras F_0 subset F_1 subset ... subset F

  F_t represents "information available up to time t"

  A process {X_t} is ADAPTED to {F_t} if X_t is F_t-measurable for all t.
  (The process doesn't see the future.)

  A process is PREDICTABLE if X_t is F_{t-1}-measurable.
  (The process is determined by strictly past information.)

  This is the formal version of "causal" in signal processing.
```

---

## Markov Chains

**Definition**: A process {X_n, n>=0} on a countable state space S is Markov if:

```
  P(X_{n+1} = j | X_n = i, X_{n-1}, ..., X_0)  =  P(X_{n+1} = j | X_n = i)

  "Future depends only on present, not past."

  Transition matrix: P = (P_{ij}) where P_{ij} = P(X_1 = j | X_0 = i)
  P is a stochastic matrix: P_{ij} >= 0, Sum_j P_{ij} = 1 for all i.
```

**n-step transitions**:

```
  P(X_n = j | X_0 = i) = (P^n)_{ij}  (matrix power)

  This is why diagonalization of the transition matrix matters:
  P^n = Q Lambda^n Q^{-1}
  Eigenvalues of P are in [-1, 1]. The dominant eigenvalue is 1 (by Perron-Frobenius).
```

**Classification of states**:

```
  RECURRENT:  P(return to i) = 1           (will return a.s.)
    Positive recurrent: E[return time] < inf  (has stationary dist)
    Null recurrent: E[return time] = inf      (no stationary dist)
  TRANSIENT: P(return to i) < 1            (will eventually leave)

  PERIODIC: state i has period d > 1 if gcd{n: P^n_{ii} > 0} = d
  APERIODIC: period = 1

  IRREDUCIBLE: every state reachable from every other state
```

**Stationary distribution**:

```
  pi is stationary if pi P = pi (and pi_i >= 0, Sum pi_i = 1)
  For irreducible, positive recurrent chain: unique pi exists.
  pi_i = 1 / E[T_i]   where T_i = return time to state i.
```

**Convergence theorem** (Ergodic theorem for Markov chains):

```
  If chain is irreducible, aperiodic, positive recurrent:
  P^n_{ij} -> pi_j  as n -> inf   for all i, j

  Exponential convergence rate determined by 2nd eigenvalue:
  ||P^n - pi|| <= C |lambda_2|^n
```

**Mixing time and spectral gap — the TCS bridge:**

```
  MIXING TIME: t_mix(eps) = min{t : max_i ||P^t(i, .) - pi||_TV <= eps}
  How many steps until the chain is eps-close to stationarity?

  SPECTRAL GAP and mixing:
  gap = 1 - lambda_2   (lambda_2 = second-largest eigenvalue magnitude)
  t_mix(eps) = Theta(log(1/eps) / gap)   (for reversible chains)

  CHEEGER'S INEQUALITY (conductance → spectral gap):
  Conductance: Phi = min_{S: pi(S) <= 1/2} [Sum_{i in S, j not in S} pi_i P_ij] / pi(S)
  Cheeger: Phi^2 / 2  <=  gap  <=  2 Phi
  This links a combinatorial property (bottleneck structure) to mixing.

  EXPANDER GRAPH CONNECTION (TCS bridge):
  A regular graph is an eps-expander iff the spectral gap of its
  random walk is >= eps. Expanders mix in O(log n) steps.
  The Markov chain on an expander IS a rapidly mixing chain.
  MCMC on a well-connected state space ≈ random walk on an expander.

  COUPLING METHOD: To bound mixing time, construct a coupling
  (X_t, Y_t) where X_t starts at worst case, Y_t starts at stationarity.
  t_mix <= E[coupling time]. Path coupling (Bubley-Dyer) simplifies
  this to checking contraction on neighboring states.

  LOG-SOBOLEV INEQUALITIES: Give tighter bounds than spectral gap
  for continuous-state chains (e.g., Langevin dynamics).
  Modified log-Sobolev: t_mix = O(1/alpha_LS) (independent of state space size).
```

**Detailed balance** (reversibility):

```
  pi_i P_{ij} = pi_j P_{ji}  for all i, j

  "Probability flow from i to j equals flow from j to i."
  Sufficient condition for pi to be stationary.
  Used in MCMC: design transition kernels that satisfy detailed balance.
```

---

## Poisson Process

The canonical counting process:

```
  N(t) = number of events in [0, t]

  DEFINITION (three equivalent characterizations):

  1. INCREMENTS:
     N(0) = 0
     Independent increments: N(t+s) - N(t) independent of N(t)
     Stationary: N(t+s) - N(t) ~ Poisson(lambda s)

  2. WAITING TIMES:
     Interarrival times T_1, T_2, ... i.i.d. Exponential(lambda)

  3. INFINITESIMAL:
     P(N(t+dt) - N(t) = 1) = lambda dt + o(dt)
     P(N(t+dt) - N(t) = 0) = 1 - lambda dt + o(dt)
     P(N(t+dt) - N(t) >= 2) = o(dt)
```

**Properties**:

```
  E[N(t)] = lambda t
  Var(N(t)) = lambda t      (variance = mean: hallmark of Poisson)
  N(t) ~ Poisson(lambda t)

  SUPERPOSITION: N1(t) + N2(t) ~ Poisson((lambda1+lambda2)t)
  THINNING: Color each event red/blue with prob p/(1-p).
            Red events form a Poisson(lambda*p) process.
  CONDITIONAL: Given N(t) = n, the n event times are
               uniformly distributed on [0,t] (order statistics of Uniform(0,t)).
```

**Inhomogeneous Poisson process**: Lambda(t) is a function, not constant:

```
  P(N(a,b) = n) = Poisson(Integral_a^b lambda(t) dt)

  "Time warping" of a homogeneous process.
  Used for non-stationary event rates (call center traffic patterns, etc.)
```

---

## Brownian Motion (Wiener Process)

The continuous-time limit of the random walk — foundational for mathematical finance and diffusion.

**Definition**: B_t is standard Brownian motion if:

```
  1. B_0 = 0
  2. Independent increments: B_t - B_s independent of F_s for t > s
  3. Gaussian increments: B_t - B_s ~ Normal(0, t-s)
  4. Continuous sample paths: t -> B_t is continuous a.s.
```

**Key properties**:

```
  E[B_t] = 0,   Var(B_t) = t,   Cov(B_s, B_t) = min(s,t)

  SCALING: B_{ct} and sqrt(c) B_t have the same distribution
  TIME REVERSAL: B_T - B_{T-t} is BM on [0,T]
  SELF-SIMILARITY: Brownian motion is fractal.

  NOWHERE DIFFERENTIABLE: B_t is continuous but a.s. nowhere differentiable.
  Total variation of B over [0,T] is infinite a.s.
  Quadratic variation: Sum |B_{t_k} - B_{t_{k-1}}|^2 -> T  as mesh -> 0
```

**Quadratic variation is the key insight**: The "derivative" of Brownian motion is white noise with formal properties (dt)^2 = 0, (dB)^2 = dt, dt * dB = 0.

**Geometric Brownian Motion** (GBM):

```
  S_t = S_0 exp((mu - sigma^2/2)t + sigma B_t)

  Multiplicative process: dS_t / S_t = mu dt + sigma dB_t  (Ito form)
  Log-normal distribution at each t.
  Used in Black-Scholes model for stock prices.
```

---

## Ito Calculus (the Calculus of Brownian Motion)

Classical calculus fails for Brownian motion because (dB)^2 = dt (finite quadratic variation). Ito calculus handles this.

**Ito integral**: Integral_0^T H(t) dB_t for adapted processes H.

```
  NOT a Riemann-Stieltjes integral (B has infinite variation).
  Defined as L^2 limit of simple processes.

  Key property: Ito integral is a martingale (zero expectation).
  E[Integral_0^T H dB] = 0
  Var[Integral_0^T H dB] = E[Integral_0^T H^2 dt]  (Ito isometry)
```

**Ito's formula** (the chain rule of stochastic calculus):

```
  If dX_t = mu(t, X_t) dt + sigma(t, X_t) dB_t  (Ito SDE)
  and f(t, x) has continuous partial derivatives, then:

  df(t, X_t) = [partial_t f + mu partial_x f + (sigma^2/2) partial_{xx} f] dt
             + sigma partial_x f dB_t

  The EXTRA TERM (sigma^2/2) partial_{xx} f dt is the Ito correction.
  It comes from (dB)^2 = dt.

  For f(x) = x^2: d(B_t^2) = 2B_t dB_t + dt
  Classical calculus: d(x^2) = 2x dx (no extra term)
```

**Ito vs. Stratonovich**: Two conventions for the stochastic integral. Ito uses left-endpoints (non-anticipating), Stratonovich uses midpoints (satisfies classical chain rule). Physics prefers Stratonovich; mathematical finance prefers Ito.

---

## Martingales

A process {M_n} adapted to {F_n} is a **martingale** if:

```
  E[M_{n+1} | F_n] = M_n     (fair game — no expected gain or loss)

  Submartingale: E[M_{n+1} | F_n] >= M_n  (expected to increase)
  Supermartingale: E[M_{n+1} | F_n] <= M_n  (expected to decrease)

  Examples:
  - Simple random walk S_n = Sum_{i=1}^n X_i, E[X_i]=0: martingale
  - S_n^2 - n: martingale (if X_i iid, mean 0, variance 1)
  - Likelihood ratio L_n = p(X_1,...,X_n | theta1) / p(X_1,...,X_n | theta0): martingale under theta0
  - B_t (Brownian motion): continuous martingale
```

**Optional stopping theorem**:

```
  If tau is a stopping time (a.s. finite) and the martingale
  is uniformly integrable (or bounded), then:
  E[M_tau] = E[M_0]

  Application: Expected time for random walk to hit boundary,
  expected winnings in a fair game when you stop.

  Ruin probability: starting at x, walk ends at 0 or N.
  P(reach N before 0) = x/N.   E[stopping time] = x(N-x).
```

**Doob's martingale convergence theorem**:

```
  If {M_n} is a submartingale bounded in L^1:
  M_n -> M_inf a.s.  for some integrable M_inf.

  Corollary: Bounded martingales converge a.s.
  This is a very general convergence result.
```

**Doob's maximal inequality**:

```
  For a non-negative submartingale:
  P(max_{k<=n} M_k >= lambda) <= E[M_n] / lambda

  Analogous to Markov's inequality but for the maximum over time.
```

---

## Gaussian Processes

A Gaussian process (GP) is a collection of random variables such that any finite subset has a joint Gaussian distribution. Completely characterized by:

```
  Mean function:       m(t) = E[X_t]
  Covariance kernel:   k(s,t) = Cov(X_s, X_t)

  Brownian motion:     m = 0, k(s,t) = min(s,t)
  Ornstein-Uhlenbeck:  m = 0, k(s,t) = sigma^2 exp(-|s-t|/l)
  Squared exponential: k(s,t) = sigma^2 exp(-|s-t|^2 / (2l^2))
  (infinitely differentiable sample paths)
```

**GPs in machine learning**: GP regression is Bayesian non-parametric regression. The posterior given observations is also a GP with updated mean and covariance. The kernel encodes assumptions about smoothness and periodicity of the function. Connects to: Gaussian process optimization (Bayesian optimization for hyperparameter tuning in Azure ML), spatial statistics, and time series interpolation.

---

## Hidden Markov Models

Latent Markov chain {Z_t} with observed process {X_t} where X_t | Z_t has distribution depending only on Z_t:

```
  Z_0, Z_1, Z_2, ...    (Markov chain, hidden)
       |    |    |
       v    v    v
  X_0, X_1, X_2, ...    (observations)

  Parameters:
  A_{ij} = P(Z_{t+1}=j | Z_t=i)       (transition matrix)
  B_i(x) = P(X_t=x | Z_t=i)           (emission distribution)
  pi_i   = P(Z_0=i)                    (initial distribution)

  KEY ALGORITHMS:
  Forward-backward: P(Z_t=i | X_0,...,X_T)   O(T |S|^2)
  Viterbi: arg max P(Z_0,...,Z_T | X_0,...,X_T)  (MAP sequence)  O(T |S|^2)
  Baum-Welch: EM algorithm for parameter estimation
```

HMMs appear in speech recognition (the original application), bioinformatics (gene finding), and NLP.

---

## Random Matrix Theory (High-Dimensional Probability)

Spectral properties of random matrices — essential for PCA in high dimensions and compressed sensing.

```
  WIGNER SEMICIRCLE LAW:
  For n×n symmetric matrix W with W_ij ~ iid, mean 0, variance 1/n:
  Empirical spectral distribution → semicircle on [-2, 2] as n → ∞.
  Density: f(x) = (1/2π) sqrt(4 - x^2) for |x| <= 2.
  Eigenvalues of random symmetric matrices are NOT Gaussian-distributed.

  MARCHENKO-PASTUR LAW:
  For n×p data matrix X with iid entries, S = X^T X / n (sample covariance):
  As n, p → ∞ with p/n → γ ∈ (0, ∞):
  Spectral distribution of S → Marchenko-Pastur with parameter γ.
  Support: [(1-√γ)^2, (1+√γ)^2].

  CONSEQUENCE FOR PCA:
  If true covariance Σ = I (no signal): eigenvalues of S spread over [(1-√γ)^2, (1+√γ)^2].
  A "signal" eigenvalue λ is detectable only if λ > 1 + √γ (BBP phase transition).
  Below this threshold: noise eigenvalues dominate, PCA gives garbage.
  This is why p/n matters: more features relative to samples = harder detection.

  TRACY-WIDOM LAW:
  The fluctuations of the largest eigenvalue around (1+√γ)^2 follow
  the Tracy-Widom distribution (not Gaussian!). Governs hypothesis testing
  for the number of significant principal components.

  APPLICATIONS:
  - PCA: spiked covariance model determines when eigenvalues are signal vs. noise
  - Compressed sensing: RIP of random matrices follows from concentration of eigenvalues
  - MCMC: spectral gap of random walk on random graph
  - Wireless communications: capacity of MIMO channels = random matrix eigenvalue problem
```

---

## Decision Cheat Sheet

| Process | Use When | Key Parameter |
|---|---|---|
| Discrete Markov chain | System with countable states, memoryless transitions | Transition matrix P |
| Poisson process | Count of events, exponential interarrivals | Rate lambda |
| Brownian motion | Continuous diffusion, finance | Volatility sigma |
| Geometric BM | Multiplicative processes, stock prices | Drift mu, volatility sigma |
| Ornstein-Uhlenbeck | Mean-reverting diffusion | Mean theta, reversion kappa |
| Martingale | Fair-game structure, optional stopping | Filtration |
| Gaussian process | Function estimation with uncertainty | Mean m(t), kernel k(s,t) |
| HMM | Latent state inference from observations | A, B, pi |

---

## Common Confusion Points

**"Markov means no memory."**
Not quite: Markov means memory is summarized by the current state. A high-order Markov chain X_{n+1} depends on (X_n, X_{n-1}, ..., X_{n-k}) — this is just a Markov chain on the enlarged state space (X_n, ..., X_{n-k}).

**"Brownian motion has independent increments, so consecutive increments are uncorrelated."**
Yes — that is precisely what "independent increments" means. But the *positions* B_s and B_t are correlated: Cov(B_s, B_t) = min(s,t). Independent increments do not imply uncorrelated positions.

**"The Ito correction is a mathematical technicality."**
It has real physical content. In the Black-Scholes model, the correction term is exactly what distinguishes the risk-neutral drift from the physical drift. In statistical mechanics, it appears as noise-induced drift in stochastic differential equations.

**"A martingale always converges."**
A bounded martingale converges a.s. (Doob). Unbounded martingales need not converge — the simple random walk is a martingale that oscillates with limsup = +inf, liminf = -inf (a.s.) in d=1,2 dimensions.
