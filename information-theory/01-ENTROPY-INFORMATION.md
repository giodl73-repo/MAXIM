# Entropy and Information — Shannon's Core Measures

## The Full Entropy Toolbox

<!-- @editor[diagram/P2]: The "MEASURES LANDSCAPE" diagram lists the measures but doesn't show their relationships as a layered structure — e.g., that I(X;Y) = KL(p(x,y)||p(x)p(y)) connecting mutual info to KL, or that cross-entropy H(P,Q) = H(P) + KL(P||Q) connecting all three. Rework as a relationship diagram showing how the measures derive from each other. -->

```
    MEASURES LANDSCAPE
    ══════════════════════════════════════════════════════════

    H(X)        ← entropy of X
    H(X|Y)      ← conditional entropy: uncertainty in X after knowing Y
    H(X,Y)      ← joint entropy
    I(X;Y)      ← mutual information: how much Y tells us about X
    D_KL(P||Q)  ← relative entropy / KL divergence
    H(P,Q)      ← cross-entropy
    h(X)        ← differential entropy (continuous)
    I(θ)        ← Fisher information

    Chain rules connect everything:
    H(X,Y) = H(X) + H(Y|X)
    I(X;Y) = H(X) + H(Y) - H(X,Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
    I(X;Y) = H(X,Y) - H(X|Y) - H(Y|X)
```

---

## Entropy H(X): Axiomatics and Properties

### Shannon's Uniqueness Theorem

<!-- @editor[audience/P2]: The 5-axiom uniqueness theorem characterization and proof sketch are standard MIT probability/information theory curriculum — this learner knows that H = -Σ p log p is the unique function satisfying continuity + symmetry + expansibility + maximum + recursion. Trim the proof sketch; the key point to preserve is the axiomatic grounding and the Gibbs inequality interpretation, not rederiving the result. -->

Shannon (1948) showed that H(X) = -Σ p_i log p_i is the UNIQUE function satisfying:

1. **Continuity**: H is continuous in p_1,...,p_n
2. **Symmetry**: H(p_1,...,p_n) = H(p_σ(1),...,p_σ(n)) for any permutation σ
3. **Expansibility**: H(p_1,...,p_n, 0) = H(p_1,...,p_n) (adding zero-prob event changes nothing)
4. **Maximum**: H(p_1,...,p_n) ≤ H(1/n,...,1/n) = log n (uniform is most uncertain)
5. **Recursion / Additivity**: H(pq, p(1-q), (1-p)) = H(p, 1-p) + p·H(q, 1-q)

```
    Result: Any H satisfying all 5 axioms must be H(X) = -c Σ p_i log p_i for c > 0.
    Choosing c=1 and log base 2 → bits. Base e → nats. Base 10 → hartleys (Hartley units).

    Proof sketch of maximum at uniform (Gibbs inequality method):
    Want to show H(p₁,...,pₙ) ≤ log n for all distributions.
    By log-sum inequality (or Jensen on concave -x log x):
    -Σ p_i log p_i ≤ -Σ p_i log(1/n) = -Σ p_i(-log n) = log n
    (use: p_i log(p_i/q_i) ≥ 0 for q_i = 1/n)
```

### Key Properties

```
    1. Non-negativity: H(X) ≥ 0, with equality iff X is deterministic.
       H = 0 means no uncertainty.

    2. Maximum: H(X) ≤ log₂|X|, with equality iff X is uniform over its support.
       Maximum uncertainty = uniform distribution.

    3. Chain rule: H(X,Y) = H(X) + H(Y|X)
       Joint uncertainty = uncertainty in X + remaining uncertainty in Y given X.
       Proof: H(X,Y) = -Σ_{x,y} p(x,y) log p(x,y)
                     = -Σ_{x,y} p(x,y) [log p(x) + log p(y|x)]
                     = H(X) + H(Y|X)

    4. Conditional entropy: H(Y|X) = Σ_x p(x) H(Y|X=x)
       H(Y|X) ≤ H(Y) with equality iff X and Y are independent.
       Conditioning reduces entropy (knowing something can only help).

    5. Subadditivity: H(X,Y) ≤ H(X) + H(Y)
       Equality iff X, Y independent.
       Proof: H(X) + H(Y) - H(X,Y) = I(X;Y) ≥ 0 (see mutual information below)
```

### Binary Entropy Function

For a Bernoulli(p) random variable:

$$H_b(p) = -p\log_2 p - (1-p)\log_2(1-p)$$

```
    Properties:
    H_b(0) = 0, H_b(1) = 0 (deterministic → no uncertainty)
    H_b(1/2) = 1 bit (maximum)
    Symmetric: H_b(p) = H_b(1-p)
    Concave: d²H_b/dp² < 0

    Values:
    p=0.01: H_b = 0.081 bits (mostly certain)
    p=0.1:  H_b = 0.469 bits
    p=0.3:  H_b = 0.881 bits
    p=0.5:  H_b = 1.000 bit (max)
    p=0.9:  H_b = 0.469 bits (same as p=0.1 by symmetry)

    CRITICAL IN CHANNEL CODING:
    BSC capacity: C = 1 - H_b(p) bits/use
    BSC rate-distortion: R(D) = H_b(p) - H_b(D) for D ≤ min(p,1-p)
    Hamming code rate: k/n = 1 - log(n+1)/n → C_BSC(p=1/7) from Hamming [7,4]
```

---

## Mutual Information I(X;Y)

How much does Y tell us about X?

$$I(X;Y) = H(X) + H(Y) - H(X,Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$$

Alternatively:

$$I(X;Y) = \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)} = D_{KL}(p(x,y) \| p(x)p(y))$$

```
    Venn diagram:
    ┌───────────────────────────────────────┐
    │         H(X,Y)                        │
    │  ┌─────────────────────┐              │
    │  │  H(X) ┌─────────────┐──────┐       │
    │  │       │    I(X;Y)   │H(Y)  │       │
    │  │H(X|Y) │             │H(Y|X)│       │
    │  └───────┴─────────────┴──────┘       │
    └───────────────────────────────────────┘

    I(X;Y) = overlap region
    H(X|Y) = part of H(X) not in H(Y)
    H(Y|X) = part of H(Y) not in H(X)
    H(X,Y) = all of both circles

    PROPERTIES:
    1. Symmetry: I(X;Y) = I(Y;X)
    2. Non-negativity: I(X;Y) ≥ 0 with equality iff X,Y independent
    3. I(X;X) = H(X) (X tells you everything about itself)
    4. I(X;Y|Z) = H(X|Z) - H(X|Y,Z) ≥ 0 (conditional MI also ≥ 0)
    5. Chain rule: I(X;Y₁Y₂) = I(X;Y₁) + I(X;Y₂|Y₁)
```

### Non-negativity Proof (via Log-Sum Inequality)

**Log-sum inequality**: For non-negative a_i, b_i:
$$\sum_i a_i \log\frac{a_i}{b_i} \geq \left(\sum_i a_i\right)\log\frac{\sum_i a_i}{\sum_i b_i}$$

Applying with a_i = p(x,y), b_i = p(x)p(y):
$$I(X;Y) = \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)} \geq \left(\sum_{x,y} p(x,y)\right)\log\frac{1}{1} = 0$$

Equality iff p(x,y)/p(x)p(y) = const for all (x,y) with p(x,y) > 0 → p(x,y) = p(x)p(y).

### Data Processing Inequality

If X → Y → Z is a Markov chain (Z depends on X only through Y):

$$I(X;Z) \leq I(X;Y)$$

Processing cannot increase information. Proof: I(X;Z) = I(X;Y) - I(X;Y|Z) + I(X;Z|Y).
Since X→Y→Z, X ⊥ Z | Y → I(X;Z|Y) = 0. Since I(X;Y|Z) ≥ 0, I(X;Z) ≤ I(X;Y).

```
    Applications:
    1. Sufficient statistics: T(X) is sufficient for X iff I(θ;T(X)) = I(θ;X)
       (no loss of information about parameter θ from compressing to T(X))
    2. Bottleneck principle: any lossy representation T must satisfy I(T;Y) ≤ I(X;Y)
       Can't recover lost information about Y from intermediate representation
    3. Feature extraction: features F = f(X) must satisfy I(F;Y) ≤ I(X;Y)
       → Upper bounds the achievable accuracy of any classifier using features F
    4. Encryption: cipher C = enc(M,K) must satisfy I(C;M) ≥ I(M;M) = H(M)
       if C is to allow recovery of M (by data processing on C→M)
       Perfect secrecy: I(C;M) = 0 → OTP (key masks all information)
```

---

## KL Divergence D_KL(P||Q)

$$D_{KL}(P\|Q) = \sum_x p(x)\log\frac{p(x)}{q(x)} = E_P\left[\log\frac{P}{Q}\right]$$

### Non-negativity Proof (Gibbs' Inequality / Jensen)

Since -log is convex (log is concave):
$$D_{KL}(P\|Q) = -E_P[\log(Q/P)] \geq -\log E_P[Q/P] = -\log\sum_x q(x) = -\log 1 = 0$$

with equality iff Q/P = const on support of P → P = Q.

```
    Key properties:
    D_KL(P||Q) ≥ 0  (non-negative)
    D_KL(P||Q) = 0 iff P = Q
    D_KL(P||Q) ≠ D_KL(Q||P)  (asymmetric!)
    D_KL(P||Q) = ∞ if Q(x)=0 but P(x)>0 for some x

    Interpretation:
    D_KL(P||Q) = extra bits needed per symbol when using code optimized for Q
                 but actual distribution is P.
    Average code length under P using Q-optimal code = H(P) + D_KL(P||Q) = H(P,Q) (cross-entropy)
    vs. optimal average code length = H(P)
    → D_KL = inefficiency from using wrong distribution

    Forward vs reverse KL:
    min D_KL(P||Q) over Q: q covers all of p (zero-forcing, mean-seeking behavior)
    min D_KL(Q||P) over Q: q concentrates on modes of p (mode-seeking behavior)
    → VAEs minimize KL(q(z|x)||p(z)) = forward direction → approximate posterior covers prior
    → GAN uses reverse KL implicitly in some formulations
```

### Pinsker's Inequality

$$D_{KL}(P\|Q) \geq \frac{1}{2}\|P - Q\|_{TV}^2$$

Total variation distance: $\|P-Q\|_{TV} = \frac{1}{2}\sum_x |p(x) - q(x)|$.

```
    → If KL is small, distributions are close in TV distance
    → TV controls probability of any event: |P(A) - Q(A)| ≤ ||P-Q||_TV
    → Pinsker: small KL → can't distinguish P from Q by any statistical test
    Constant 1/2 is tight; better constants: Bretagnole-Huber (1978): tighter for small KL
```

---

## Cross-Entropy H(P,Q)

$$H(P,Q) = -\sum_x p(x)\log q(x) = H(P) + D_{KL}(P\|Q)$$

```
    The ML CONNECTION:
    Training a model with parameters θ:
    - True data distribution: p(x) (empirical: 1/n for each training example)
    - Model distribution: q_θ(x) = p_θ(x)

    Maximum likelihood = minimize negative log-likelihood:
    L(θ) = -1/n Σ_i log p_θ(x_i) = -E_p[log q_θ(x)] = H(p, q_θ)

    Cross-entropy loss = H(p, q_θ) = H(p) + D_KL(p||q_θ)

    Since H(p) is fixed (doesn't depend on θ):
    Minimizing CE loss = minimizing KL(p||q_θ) = making model match true distribution

    WHY THIS IS THE RIGHT LOSS:
    1. Maximum likelihood = maximum entropy principle = MLE
    2. Minimizing KL = information-theoretically optimal
    3. CE is the unique proper scoring rule satisfying locality
    4. Gradient of CE is better-conditioned than squared error for classification

    PERPLEXITY:
    Perplexity = 2^{H(p,q)} = 2^{CE}
    For a language model on text with entropy h bits/token:
    Perplexity = 2^h
    Interpretation: effective vocabulary size if all tokens equally likely
    → Good LM: perplexity 15-30 on held-out text
    → Random unigram model on 50K vocab: perplexity = 50000
    → Human: ~30-100 depending on text domain
```

---

## Differential Entropy h(X) for Continuous Distributions

For a continuous random variable X with pdf f(x):

$$h(X) = -\int f(x)\log f(x)\, dx$$

```
    KEY DIFFERENCES from discrete H(X):
    1. h(X) CAN BE NEGATIVE (unlike discrete H(X))
    2. Not invariant under reparametrization: h(aX) = h(X) + log|a|
    3. Not directly interpretable as "bits" (but differences h(Y) - h(X) are valid)

    Key results:
    Uniform on [0,a]: h = log a (negative if a < 1)
    Gaussian N(μ,σ²): h = ½log(2πeσ²)  ← maximum for given variance
    Exponential(λ): h = 1 - log λ
    Laplace(0,b): h = 1 + log(2b)

    GAUSSIAN MAXIMIZES DIFFERENTIAL ENTROPY:
    Among all distributions with fixed variance σ²:
    h(X) ≤ ½log(2πeσ²)  with equality iff X ~ N(μ,σ²)

    Proof via Lagrange multipliers:
    Maximize -∫f log f subject to: ∫f = 1, ∫(x-μ)²f = σ²
    Lagrangian: -∫f log f - λ₀∫f - λ₂∫(x-μ)²f → f(x) ∝ exp(-λ₂(x-μ)²) → Gaussian ✓

    AWGN channel capacity uses this: h(Y|X) = h(N) = ½log(2πeN₀)
    h(Y) ≤ ½log(2πe(P+N₀)) with equality iff X ~ Gaussian
    → Gaussian input achieves AWGN capacity
```

---

## Fisher Information and Cramér-Rao Bound

For a parametric family p(x;θ), the Fisher information:

$$I(\theta) = E_\theta\left[\left(\frac{\partial \log p(X;\theta)}{\partial \theta}\right)^2\right] = -E_\theta\left[\frac{\partial^2 \log p(X;\theta)}{\partial \theta^2}\right]$$

**Cramér-Rao lower bound**: For any unbiased estimator θ̂(X₁,...,X_n):

$$\text{Var}(\hat{\theta}) \geq \frac{1}{n I(\theta)}$$

```
    Efficient estimator: achieves the Cramér-Rao bound.
    MLE is asymptotically efficient under regularity conditions.
    (MLE → N(θ, 1/nI(θ)) as n → ∞ by CLT + delta method)

    Fisher matrix F_ij = E[∂ log p/∂θ_i × ∂ log p/∂θ_j]
    For Gaussian N(0,Σ): F = Σ⁻¹ (Fisher matrix = inverse covariance)
    Rao-Cramér for vectors: Var(θ̂) - F⁻¹ ≥ 0 (positive semi-definite)

    NATURAL GRADIENT:
    Standard gradient: ∇L in Euclidean parameter space
    Natural gradient: F⁻¹∇L → steepest descent in information geometry
    Fisher information matrix defines Riemannian metric on parameter space
    (Amari's information geometry)

    Natural gradient = parameter update in the "manifold" of distributions
    More efficient: ignores parameter redundancy (e.g., different parameterizations of same distribution)
    Used in: actor-critic RL (natural policy gradient), K-FAC optimizer
```

---

## Entropy Rate for Stochastic Processes

For a stationary stochastic process {X_n}:

$$H(\mathcal{X}) = \lim_{n\to\infty} \frac{1}{n} H(X_1,...,X_n) = \lim_{n\to\infty} H(X_n|X_{n-1},...,X_1)$$

```
    MARKOV CHAIN:
    Transition matrix P, stationary distribution π.
    H(X_n|X_{n-1}) = -Σ_{i,j} π_i P_{ij} log P_{ij}
    Entropy rate = H(X|X_prev) (conditional on one previous state, since Markov)

    ENGLISH TEXT:
    Shannon (1951): estimated ~1-1.5 bits/letter for English
    LM perplexity 30 ≈ 5 bits/token; assume 4 chars/token → 1.25 bits/char ✓
    GPT-4 class models: < 1 bit/char for English text
    → Modern LLMs are near Shannon limit for English text compression!

    ERGODIC THEOREM (McMillan / AEP):
    For ergodic source: -(1/n)log p(X₁,...,Xₙ) → H(X) almost surely
    → Probability of typical sequence ≈ 2^{-nH(X)}
    → Number of typical sequences ≈ 2^{nH(X)} (AEP = Asymptotic Equipartition Property)
    This is the foundation of both source coding and channel coding proofs.
```

---

## Connection to Thermodynamics (for Physics Background)

```
    BOLTZMANN ENTROPY:
    S = k_B ln W
    where W = number of microstates consistent with macrostate

    For equiprobable microstates (microcanonical ensemble):
    S = k_B ln W = k_B log₂ W / log₂ e = k_B ln 2 × H  [H in bits]

    For non-equiprobable: S = -k_B Σ p_i ln p_i = k_B ln 2 × H [nats→bits]

    SECOND LAW as information principle:
    Entropy can only increase in isolated systems
    = Information about fine-grained microstate can only be lost, never gained
    = D_KL(p_current || p_uniform) is non-decreasing → erasure toward equilibrium

    MAXWELL'S DEMON:
    Demon measures molecule position (bit of information gained)
    Sorts molecules → reduces thermodynamic entropy of gas
    RESOLUTION: Demon's memory must be erased to run in a cycle
    Erasing 1 bit costs k_B T ln 2 Joules → exactly compensates entropy reduction
    Information erasure → thermodynamic entropy increase → 2nd law preserved

    LANDAUER + SZILARD = MAXWELL'S DEMON RESOLUTION:
    Bit erasure: ΔS ≥ k_B ln 2 per bit (Landauer 1961)
    Bit extraction from thermal: W ≤ k_B T ln 2 (Szilard engine)
    These are inverse processes → consistent, no contradiction
```

---

## Decision Cheat Sheet

| Need                                  | Formula                           | Key constraint |
|---------------------------------------|-----------------------------------|---------------|
| Average compression limit             | H(X) = -Σ p log p                | Can't go below H |
| Reduce to uncertainty given Y         | H(X|Y) = H(X,Y) - H(Y)           | ≤ H(X) always |
| How much Y tells us about X          | I(X;Y) = H(X) - H(X|Y)           | ≥ 0 always |
| Compare distributions P, Q          | D_KL(P||Q) = Σ p log(p/q)        | ≥ 0, not symmetric |
| ML training loss                      | H(p,q) = H(p) + D_KL(p||q)       | Minimize over model q |
| Maximum entropy for given variance   | N(μ,σ²), h = ½log(2πeσ²)         | Gaussian wins |
| Estimation variance lower bound      | Var(θ̂) ≥ 1/(n I(θ))              | Cramér-Rao |
| Optimal optimization direction        | F⁻¹ ∇L (natural gradient)         | Fisher = metric tensor |

---

## Common Confusion Points

**H(X|Y) ≤ H(X) is "conditioning reduces entropy" but H(X|Y=y) can be > H(X)**:
The CONDITIONAL entropy H(X|Y) = E_Y[H(X|Y=y)] is always ≤ H(X). But for a specific
observed value Y=y, the conditional entropy H(X|Y=y) can exceed H(X). Knowing that a
biased coin showed heads might increase your uncertainty about something correlated with
that coin flip. The inequality holds on average, not pointwise.

**KL divergence is not symmetric, and this matters**: D_KL(P||Q) ≠ D_KL(Q||P) in general.
Which direction you use in optimization has significant consequences:
- Forward KL: D_KL(p_data || q_model) → mass-covering (q spreads to cover p)
- Reverse KL: D_KL(q_model || p_data) → mode-seeking (q concentrates on modes of p)
MLE uses forward KL. Variational methods often use reverse KL (ELBO = -D_KL(q||p) + const).
The Jensen-Shannon divergence JSD(P,Q) = ½D_KL(P||M) + ½D_KL(Q||M), M=(P+Q)/2, IS symmetric.

**Fisher information and Shannon information are distinct**: Fisher information I(θ)
measures the sensitivity of the log-likelihood to θ — it's about ESTIMATION, not encoding.
Shannon entropy H(X) measures the average bits needed to encode X. They're related through
the Cramér-Rao bound and information geometry but are measuring different things. Fisher
information for a Gaussian model happens to equal the inverse variance, but this is a special case.
