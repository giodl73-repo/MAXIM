# Information Theory for Machine Learning
## Shannon's Framework — Uncertainty, Compression, Communication, and Learning

```
THE INFORMATION THEORY MAP

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  ENTROPY H(X)          JOINT H(X,Y)         CONDITIONAL H(X|Y)         │
  │  uncertainty in X      total uncertainty     uncertainty in X given Y   │
  │                                                                          │
  │  KL DIVERGENCE D(P‖Q)  MUTUAL INFO I(X;Y)   CHANNEL CAPACITY C         │
  │  "distance" P from Q   shared information    max info through channel    │
  │                                                                          │
  │  FISHER INFORMATION     CROSS-ENTROPY         MINIMUM DESCRIPTION LENGTH│
  │  curvature of log-lik   loss function for ML  compression = learning     │
  └─────────────────────────────────────────────────────────────────────────┘

  All of ML optimization is information theory in disguise.
```

---

## 1. Shannon Entropy

**Definition**: expected surprise (in bits if log₂, nats if ln):
```
H(X) = -Σ_x p(x) log p(x) = E_p[-log p(X)]
```

**Properties**:
- H(X) ≥ 0 always
- H(X) = 0 iff X is deterministic
- H(X) ≤ log|X| with equality iff X is uniform (maximum uncertainty)
- Concavity: H(λp + (1-λ)q) ≥ λH(p) + (1-λ)H(q)

**Intuition**: H(X) is the minimum average number of bits needed to describe X. Shannon's source coding theorem makes this precise.

**Joint and conditional**:
```
H(X, Y) = -Σ_{x,y} p(x,y) log p(x,y)

H(X | Y) = -Σ_{x,y} p(x,y) log p(x|y) = E_{p(y)}[H(X|Y=y)]

Chain rule: H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)
```

**Conditioning reduces entropy**: H(X|Y) ≤ H(X) — knowing Y can only decrease (or not change) uncertainty about X. Equality iff X ⊥ Y.

---

## 2. KL Divergence

**Definition**: relative entropy from P to Q:
```
D_KL(P ‖ Q) = Σ_x p(x) log (p(x) / q(x)) = E_P[log P/Q]
```

**Properties**:
- D_KL(P‖Q) ≥ 0 always (Gibbs inequality, follows from log ≤ x-1)
- D_KL(P‖Q) = 0 iff P = Q a.e.
- **Not symmetric**: D_KL(P‖Q) ≠ D_KL(Q‖P) in general
- **Not a metric**: triangle inequality fails
- D_KL(P‖Q) = ∞ if Q(x) = 0 where P(x) > 0 — Q must cover P's support

**Proof of non-negativity** (Gibbs inequality):
```
-D_KL(P‖Q) = E_P[log Q/P] ≤ log E_P[Q/P]   (Jensen, log is concave)
            = log Σ_x p(x)(q(x)/p(x))
            = log Σ_x q(x) ≤ log 1 = 0
```

**Forward vs reverse KL**:
```
  D_KL(P ‖ Q):  "forward" — minimize over Q
    → zero-forcing: Q goes to zero wherever P is small
    → mode-seeking: Q concentrates on major mode of P
    → used in variational inference

  D_KL(Q ‖ P):  "reverse" — minimize over Q
    → zero-avoiding: Q stays positive wherever P is positive
    → mean-seeking: Q spreads to cover all modes
    → used in expectation propagation, MLE (minimize D_KL(P_data ‖ P_model))
```

**KL and cross-entropy**:
```
D_KL(P ‖ Q) = H(P, Q) - H(P)

  where H(P, Q) = -E_P[log Q]  is cross-entropy

MLE = minimize D_KL(P_data ‖ P_θ)
    = minimize H(P_data, P_θ)    (H(P_data) is constant w.r.t. θ)
    = maximize E_{x~data}[log p_θ(x)]
```

So **cross-entropy loss is KL divergence from data to model** — MLE minimizes it.

---

## 3. Mutual Information

```
I(X; Y) = D_KL(p(x,y) ‖ p(x)p(y))
         = H(X) - H(X|Y)
         = H(Y) - H(Y|X)
         = H(X) + H(Y) - H(X,Y)
```

**Intuition**: how much does knowing Y reduce uncertainty about X? Symmetric — I(X;Y) = I(Y;X).

**Key properties**:
- I(X;Y) ≥ 0 with equality iff X ⊥ Y
- Data processing inequality: X → Y → Z ⟹ I(X;Z) ≤ I(X;Y)
  - You can't gain information by processing
  - Markov chain: Z is sufficient for X iff I(X;Y) = I(X;Z)

**Conditional mutual information**:
```
I(X; Y | Z) = H(X|Z) - H(X|Y,Z)
            = E_Z[I(X;Y|Z=z)]
```

**Chain rule for MI**:
```
I(X₁,...,Xn; Y) = Σ_i I(Xᵢ; Y | X₁,...,X_{i-1})
```

**Information bottleneck** (Tishby et al.):
```
  Compress X into T (representation) while preserving information about Y:
  max I(T; Y) - β·I(T; X)

  Deep nets as bottleneck: each layer compresses input while retaining task-relevant info
  Debate: whether layers actually perform IB compression in practice
```

---

## 4. Source Coding — Compression Bounds

**Shannon's source coding theorem**: the minimum average code length for source X is H(X) bits. You cannot do better; entropy is the fundamental limit.

**Huffman coding**: optimal prefix-free code. Expected length L satisfies:
```
H(X) ≤ L < H(X) + 1
```

**Arithmetic coding**: approaches H(X) arbitrarily closely.

**Asymptotic Equipartition Property (AEP)**:
```
For i.i.d. X_1,...,X_n ~ p:
  -(1/n) log p(X_1,...,X_n) → H(X)  in probability

The "typical set" A_ε^n has:
  P(A_ε^n) → 1
  |A_ε^n| ≈ 2^{nH(X)}
```

Most probability mass concentrates on ~2^{nH} equally likely sequences. Everything else is negligible. This is why entropy bounds compression.

---

## 5. Channel Capacity — Communication Limits

**Noisy channel**: input X transmitted through channel p(y|x), received as Y.

**Channel capacity**:
```
C = max_{p(x)} I(X; Y)   bits per channel use
```

**Shannon's channel coding theorem**: you can transmit at rate R < C with arbitrarily small error probability (with long block codes). At R > C, error probability → 1.

**AWGN channel** (additive white Gaussian noise):
```
Y = X + Z,  Z ~ N(0, N₀),  E[X²] ≤ P (power constraint)

C = ½ log₂(1 + P/N₀)  = ½ log₂(1 + SNR)   [bits per channel use]

  ← Shannon limit: the maximum SNR efficiency of any coding scheme
```

This appears in wireless communication, but also in:
- Rate-distortion theory (lossy compression)
- Capacity of neural networks as information processors

---

## 6. Fisher Information

**Definition**: expected squared score, or negative expected Hessian of log-likelihood:
```
I(θ) = E_{x~p(x;θ)}[ (∂ log p(x;θ)/∂θ)² ]
      = -E_{x~p(x;θ)}[ ∂² log p(x;θ)/∂θ² ]    (under regularity)
```

**Cramér-Rao Lower Bound**: for any unbiased estimator θ̂(X):
```
Var(θ̂) ≥ 1/I(θ)

Multivariate: Cov(θ̂) ≥ I(θ)^{-1}  (matrix inequality)
```

No unbiased estimator can have lower variance than the inverse Fisher information. MLE achieves this asymptotically (efficiency).

**Natural gradient**:
```
Standard gradient descent ignores geometry of parameter space.
Fisher information matrix = Riemannian metric on the manifold of distributions.

Natural gradient: θ ← θ - α I(θ)^{-1} ∇L(θ)

Amari's information geometry: steepest descent in distribution space,
not parameter space. Invariant to reparameterization.

In practice: approximated by K-FAC (Kronecker-Factored Approximate Curvature)
```

**Fisher and KL**:
```
D_KL(p(·;θ) ‖ p(·;θ+δ)) ≈ ½ δᵀ I(θ) δ   for small δ

Fisher is the local curvature of KL divergence.
Trust region policy optimization (TRPO) uses this: constrain policy updates
by KL ≤ ε ↔ δ stays inside Fisher ellipsoid.
```

---

## 7. Minimum Description Length (MDL)

**Core idea**: learning = compression. The best model is the one that compresses the data most.

```
MDL principle:
  Prefer the hypothesis H that minimizes:
    L(D | H) + L(H)
    ↑             ↑
  description   description
  of data       of hypothesis
  given H

  ↔ Bayesian MAP with -log prior as code length
```

**Two-part vs refined MDL**:
- Two-part (crude): L(H) + L(D|H) — pick model then encode data
- Normalized Maximum Likelihood (NML): minimax optimal single-part code

**Connection to model selection**:
```
  BIC ≈ Two-part MDL for exponential families:
  BIC = -2 log L̂ + k log n  ↔  L(D|H) + L(H)
                                  ↑            ↑
                              log-likelihood  k params × log n bits each

  AIC ≈ MDL for prediction (different complexity term):
  AIC = -2 log L̂ + 2k
```

---

## 8. Information Theory in ML — The Big Map

```
  ML concept                   Information theory connection
  ──────────────────────────   ─────────────────────────────────────────
  Cross-entropy loss           H(P_data, P_model) = D_KL(P_data‖P_model) + H(P_data)
  MLE                          Minimize D_KL(P_data ‖ P_θ)
  ELBO (VAE)                   log p(x) ≥ E_q[log p(x|z)] - D_KL(q‖p)
  KL penalty in RL (PPO)       Keep policy near reference; D_KL(π‖π_ref) ≤ ε
  Maximum entropy RL (SAC)     Maximize E[R] + α H(π) — prefer uncertain policies
  Mutual info objectives       Representation learning (InfoNCE, MINE)
  Knowledge distillation       Minimize H(p_teacher, p_student) via soft labels
  Calibration (ECE)            Reliability: H(Y|confidence) should be low
  Model selection              MDL / BIC / AIC — compression tradeoff
  Natural gradient             Fisher metric on distribution manifold
  Attention entropy            H(attention weights) — spread vs concentration
```

---

## 9. Decision Cheat Sheet

| Quantity | Formula | Use it for |
|----------|---------|-----------|
| Entropy H(X) | -E[log p(X)] | Measuring uncertainty; compression bound |
| Cross-entropy H(P,Q) | -E_P[log Q] | Classification loss function |
| KL divergence D(P‖Q) | E_P[log P/Q] | VAE, distillation, measuring distribution shift |
| Mutual info I(X;Y) | H(X) - H(X|Y) | Feature selection, representation quality |
| Channel capacity C | max_p I(X;Y) | Theoretical communication/compression limit |
| Fisher info I(θ) | E[(∂ log p/∂θ)²] | Cramér-Rao, natural gradient, TRPO |
| MDL | L(H) + L(D|H) | Model selection, learning as compression |

---

## 10. Common Confusion Points

1. **"KL divergence is a distance"** — It's not: not symmetric, no triangle inequality. The symmetric version `½(D_KL(P‖Q) + D_KL(Q‖P))` is the Jensen-Shannon divergence, which is bounded and is a metric after taking square roots.

2. **"Cross-entropy loss = entropy"** — Cross-entropy H(P,Q) ≠ entropy H(P). Cross-entropy includes KL divergence: H(P,Q) = H(P) + D_KL(P‖Q). MLE minimizes cross-entropy, which minimizes KL since H(P_data) is constant.

3. **"Mutual information is symmetric, so direction doesn't matter"** — I(X;Y) = I(Y;X) as a quantity, but conditioning can break symmetry: I(X;Y|Z) ≠ I(Y;X|Z) only when there's shared context. The data processing inequality I(X;Z) ≤ I(X;Y) for X→Y→Z has a specific direction.

4. **"High entropy = bad"** — Depends on context. In compression, high entropy = requires more bits. In RL (max entropy RL), high policy entropy is desirable for exploration. In calibration, entropy should match uncertainty.

5. **"Fisher information is always PSD"** — Yes by definition (it's a covariance matrix of scores). But it can be singular (non-invertible) when the model is overparameterized, leading to degenerate natural gradients.

6. **"Forward KL in VI is wrong — should use reverse KL"** — The choice depends on the application. Variational inference uses D_KL(q‖p) (reverse/exclusive KL, mode-seeking). Expectation propagation uses D_KL(p‖q) (inclusive KL, mean-seeking). Neither is universally "right."

7. **"MDL = Bayesian model selection"** — They're equivalent when the prior is the ideal code. In practice, MDL uses specific code length choices (NML, two-part) that don't always correspond to a natural prior.
