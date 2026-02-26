# Information-Theoretic Bounds on Generalization

## The Big Picture

Information-theoretic approaches to generalization bounds use mutual information, KL divergence, and related measures to capture how much an algorithm "remembers" about its training data. These bounds are tighter for stochastic algorithms (like SGD) than classical VC/Rademacher bounds, and they connect generalization to compression.

```
+──────────────────────────────────────────────────────────────────+
|          INFORMATION-THEORETIC GENERALIZATION FRAMEWORK         |
|                                                                  |
|  CORE INSIGHT                                                    |
|  The generalization gap is bounded by how much information       |
|  the algorithm's output (W) contains about its training data (S) |
|                                                                  |
|   generalization gap ≤ f( I(W; S) )                              |
|                                                                  |
|  LOW MUTUAL INFORMATION → GOOD GENERALIZATION                   |
|  (Algorithm "forgets" training data → can't have overfit it)    |
|                                                                  |
|  THREE MAIN FRAMEWORKS                                           |
|  ─────────────────────                                           |
|  PAC-Bayes:        KL(Q || P) bounds generalization             |
|                    Output distribution Q close to prior P        |
|                                                                  |
|  Mutual Information: I(W; S) bounds generalization              |
|                    Algorithm output W barely depends on S        |
|                                                                  |
|  CMI:              Conditional MI; tighter, handles dependence  |
|                    across the sample                             |
+──────────────────────────────────────────────────────────────────+
```

---

## PAC-Bayes Theory

PAC-Bayes is the information-theoretic framework with the longest history and tightest known bounds:

```
SETUP
──────
Prior distribution P over hypothesis space H
Posterior distribution Q over H (after observing S)
Stochastic classifier: draw h ~ Q, then predict with h.

Expected risk:   R(Q) = E_{h~Q}[R(h)]
Empirical risk:  R_S(Q) = E_{h~Q}[R_S(h)]

PAC-BAYES THEOREM (McAllester 1999, Catoni 2007)
─────────────────────────────────────────────────
For any prior P (independent of S), any δ ∈ (0,1),
with probability ≥ 1-δ over S:

  For ALL posteriors Q simultaneously:

  R(Q) ≤ R_S(Q) + √( (KL(Q||P) + log(1/δ)) / (2m) )

  OR (Catoni's tighter version):
  R(Q) ≤ (1 - e^{-c·R_S(Q) - c·(KL(Q||P)+log(2/δ))/m}) / (1 - e^{-c})

KL(Q||P) = ∫ log(dQ/dP) dQ  =  E_{h~Q}[log Q(h)/P(h)]

READING THE BOUND
  If Q ≈ P (posterior ≈ prior): KL small → tight bound
  If Q is concentrated (small variance): KL can be large if far from P
  Good P = good prior about what h* looks like
```

---

## PAC-Bayes: Tightness and Numerics

PAC-Bayes bounds are the only generalization bounds that are numerically non-vacuous for neural networks in practice:

```
BERNSTEIN-PAC-BAYES (Langford & Shawe-Taylor 2002)
────────────────────────────────────────────────────
More precise inversion via Bernoulli KL:

  kl(R_S(Q) || R(Q)) ≤ (KL(Q||P) + log(2/δ)) / m

where kl(p||q) = p log(p/q) + (1-p) log((1-p)/(1-q))

NUMERICAL EXAMPLE (MNIST-like setting)
  m = 50,000 training examples
  Neural net with weight perturbation scheme as Q
  KL(Q||P) ≈ 10⁶ nats (derived from Gaussian noise injection)

  Bound: R(Q) ≤ R_S(Q) + √( (10⁶ + log 20) / 100,000 )
                       ≤ R_S(Q) + √10 ≈ 3  ← still vacuous!

  With tighter construction (Dziugaite & Roy 2017):
    KL(Q||P) ≈ 10,000 nats (optimized PAC-Bayes bound)
    R(h) ≤ 0.16  ← FIRST non-vacuous bound for a real network!
    (Compare to actual test error ≈ 0.02 — bound is loose but valid)
```

---

## Mutual Information Bounds

```
RUSSO-ZOU BOUND (2016)
───────────────────────
Let A: Z^m → W be a learning algorithm.
S = (Z₁,...,Zₘ) iid from D.
W = A(S) (the trained model).

If the loss function ℓ(w, z) is σ²-subgaussian in z for any w:

  |E[generalization gap]| = |E_S[R(A(S)) - R_S(A(S))]|
                          ≤ √( 2σ² · I(W; S) / m )

  I(W; S) = mutual information between output model W and training set S.

INTERPRETATION
  I(W; S) = 0: algorithm ignores training data → terrible accuracy
  I(W; S) = m·log|Z|: algorithm memorizes S → terrible generalization
  Sweet spot: algorithm uses just enough information from S to solve task

SGD IMPLICATION
  SGD with small learning rate is "more random" → smaller I(W;S)
  Large batch → less randomness → more information used
  This formalizes "small-batch SGD generalizes better"
```

---

## Individual-Sample Bounds

The Russo-Zou bound uses I(W; S) — mutual information with the whole training set. Tighter bounds use per-sample mutual information:

```
INDIVIDUAL SAMPLE BOUND (Bu et al. 2020)
──────────────────────────────────────────
  |E[generalization gap]| ≤ (1/m) Σᵢ √( 2σ² · I(W; Zᵢ) )

  I(W; Zᵢ) = mutual information between W and the i-th training example.

WHY TIGHTER?
  I(W; S) ≤ Σᵢ I(W; Zᵢ)   by chain rule
  So individual-sample bound ≤ full-S bound.

  If most examples are "uninformative" but a few are influential,
  individual bound captures this; full-S bound does not.
```

---

## Conditional Mutual Information (CMI)

```
CMI BOUND (Steinke & Zakynthinou 2020)
────────────────────────────────────────
SUPERSAMPLE CONSTRUCTION
  Generate 2m examples Z₁,...,Z_{2m} iid from D.
  Let U = (U₁,...,Uₘ) ∈ {0,1}^m be a random index set.
  Training set: S = {Z_{Uᵢ + 2(i-1)} : i = 1,...,m}
  (For each pair, choose one for training)

  CMI = I(W; U | Z₁,...,Z_{2m})
       = how much knowing the algorithm output W tells us
         about which samples were used for training,
         given all 2m examples.

  |E[generalization gap]| ≤ √( 2σ² · CMI(W) / m )

ADVANTAGE
  CMI is smaller than I(W; S) because conditioning on all 2m
  examples removes data-content information.
  CMI measures only "which were training examples" —
  not the content of the examples.

  Tighter for deterministic algorithms (I(W;S) could be large,
  CMI can be small if algorithm doesn't identify which samples
  were training examples).
```

---

## MDL and Compression

```
MINIMUM DESCRIPTION LENGTH (MDL) VIEW
───────────────────────────────────────
MDL PRINCIPLE: The best hypothesis is the one that compresses
the data most, i.e., minimizes description length:

  L(h) + L(data | h)

where L(x) = -log₂ P(x) is the code length under a prior P.

CONNECTION TO PAC-BAYES
  PAC-Bayes with P = prior, Q = posterior:
    KL(Q || P) = description overhead of Q over P
  = additional bits needed to describe Q given P

OCCAM'S RAZOR THEOREM (formal version)
  If an algorithm outputs h that represents S in s bits
  beyond a universal prior:

    R(h) ≤ R_S(h) + √( (s + log(1/δ)) / (2m) )

  Short description (small s) → good generalization.

PRACTICAL CONSEQUENCES
  • MDL-based compression of neural net weights → generalization bound
  • Weight quantization: compressing weights to k bits each
    reduces effective s
  • Sparse networks (many zero weights) have smaller s
  • Lottery ticket hypothesis: small sparse subnetworks generalize
    because they have small s
```

---

## Comparison of Approaches

```
FRAMEWORK         STRENGTHS                    WEAKNESSES
──────────────    ─────────────────────────    ──────────────────────
VC Bounds         Distribution-free            Vacuous for deep nets
                  Combinatorially clean        Only binary classification
                  Fundamental theorem          Only worst-case D

Rademacher        Any loss function             Still vacuous for deep nets
                  Data-dependent               Requires bounding sup

PAC-Bayes         Numerically non-vacuous!      Prior choice is critical
                  Works for stochastic algs     KL computation expensive
                  Tight for specific algs       Not fully interpretable

MI Bounds         Connects to SGD analysis      Tight only in expectation
(Russo-Zou)       Captures randomness           Not high-probability bound
                  Generalizes to online

CMI Bounds        Tightest IT bound known       Supersample construction
                  Works for deterministic algs  complex to compute
                  Better than I(W;S)

MDL / Compression Interpretable                 Approximate; coding overhead
                  Connect to physics (free E)   Empirically limited
```

---

## Connection to Physics: Free Energy

```
FREE ENERGY CONNECTION
───────────────────────
PAC-Bayes resembles the variational free energy in stat. mech.:

  F(Q) = E_{h~Q}[L(h)] + (1/β) KL(Q || P)

  = average energy + (1/β) × entropy relative to prior

  Minimize F over Q:
    Optimal Q = Gibbs distribution: Q*(h) ∝ P(h) · e^{-β L(h)}

  For learning: L(h) = empirical risk R_S(h)
    Optimal posterior = P(h) × exp(-β m R_S(h))

  The PAC-Bayes bound says R(Q) ≈ R_S(Q) + O(1/β):
    High β = strong regularization toward prior = better bound but worse fit
    Low β = weak regularization = worse bound but better fit
    Optimal β balances these → Catoni's tighter PAC-Bayes bound

LANGEVIN DYNAMICS
  SGD + Gaussian noise = discrete Langevin dynamics
  Converges to Gibbs distribution → PAC-Bayes posterior
  SGD is implicitly doing variational inference!
```

---

## Decision Cheat Sheet

| Goal | Framework | Key Quantity |
|------|-----------|-------------|
| Tight bound for stochastic classifier | PAC-Bayes | KL(Q \|\| P) |
| Bound for deterministic algorithm | CMI | I(W; U \| Z₁,...,Z_{2m}) |
| Analyze SGD generalization | MI bound | I(W; S)/m |
| Understand weight compression | MDL | Description length in bits |
| Non-vacuous bound for neural net | PAC-Bayes (optimized) | Numerically minimize KL |
| Prior knowledge about task | PAC-Bayes with informed P | Better P → tighter bound |

---

## Common Confusion Points

**"PAC-Bayes needs a prior P — isn't that cheating?"**
No, but you must choose P before seeing data. P can encode architectural priors (e.g., Gaussian weight initialization), sparsity priors, or any domain knowledge. The bound is valid for any P chosen independently of S. Choosing a better P gives a tighter bound — analogous to choosing good priors in Bayesian inference. Data-dependent priors are handled by splitting the data.

**"MI bound is only in expectation — does that matter?"**
Russo-Zou gives E[generalization gap] ≤ bound. High-probability versions require more work (CMI gives high-probability bounds via Markov). For most practical purposes, expected-generalization bounds are useful for analyzing training dynamics. For worst-case guarantees, you want high-probability.

**"If I(W; S) = 0, the algorithm ignores training data — how is that useful?"**
It isn't for accurate prediction. The MI bound has two sides: I(W;S) small → good generalization, but I(W;S) large → potentially bad generalization. The tight learning algorithm is one that uses just enough information from S to find the right h, without memorizing noise. Perfect memorization: I(W;S) = H(S) (huge); perfect algorithm: I(W;S) = I(W;label function) (much smaller in theory).

**"How do you compute KL(Q||P) in practice for neural nets?"**
Approximate approaches: (1) Gaussian posterior Q with Gaussian prior P → closed form KL; (2) Variational Bayes (ELBO maximization); (3) Randomized smoothing: add Gaussian noise to weights, treat noisy model as sample from Q. Dziugaite & Roy (2017) optimized the PAC-Bayes bound by treating λ (noise scale) as a hyperparameter and computing the resulting KL numerically.
