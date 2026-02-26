# Machine Learning Theory — Landscape and Taxonomy

## The Big Picture

ML theory asks: *why does learning work at all?* Three lineages of answer, converging on a hard unsolved center:

```
+------------------------------------------------------------------+
|              MACHINE LEARNING THEORY LANDSCAPE                   |
+------------------------------------------------------------------+
|                                                                  |
|  COMPUTATIONAL          STATISTICAL           OPTIMIZATION       |
|  LEARNING THEORY        LEARNING THEORY       THEORY             |
|  ──────────────         ───────────────       ────────────       |
|  Valiant 1984           Vapnik 1971–95        SGD analysis       |
|  PAC Learning           VC Dimension          Implicit reg.      |
|  Tractability           Generalization        Why SGD works      |
|  Sample complexity      bounds                                   |
|                         Rademacher complexity                    |
|                                                                  |
+────────────────────────────────┬─────────────────────────────────+
                                 |
                                 v
+────────────────────────────────────────────────────────────────--+
|              MODERN ML PHENOMENOLOGY (2018–present)              |
|  Double Descent  ·  Neural Tangent Kernel  ·  Benign Overfitting |
|  Grokking  ·  Mechanistic Interpretability  ·  Scaling Laws      |
|  "Classical theory fails for overparameterized models.           |
|   Here is the emerging framework."                               |
+──────────────────────────────────────────────────────────────────+
                                 |
                                 v
+──────────────────────────────────────────────────────────────────+
|              INFORMATION-THEORETIC PERSPECTIVE                   |
|  PAC-Bayes  ·  Mutual Information  ·  MDL                        |
|  "Compression = Generalization"                                  |
+──────────────────────────────────────────────────────────────────+
```

---

## The Central Question

You have a hypothesis class H (e.g., all linear classifiers, all depth-3 networks). You train on m samples from distribution D. Will your learned hypothesis generalize?

```
+─────────────────────────────────────────────────────────────────+
|                  GENERALIZATION PROBLEM                          |
|                                                                  |
|  TRAINING DATA                   TRUE DISTRIBUTION              |
|  m samples from D                                               |
|                                                                  |
|  Empirical Risk:  R_S(h) = (1/m) Σᵢ loss(h(xᵢ), yᵢ)            |
|  True Risk:       R(h)   = E_{(x,y)~D}[loss(h(x), y)]           |
|                                                                  |
|  Generalization gap:  R(h) - R_S(h)                             |
|                                                                  |
|  Classical theory:  bound this gap via complexity of H           |
|  Modern reality:    gap stays small even when H is enormous      |
+─────────────────────────────────────────────────────────────────+
```

Classical theory bounds the generalization gap using measures of hypothesis class complexity. Modern theory asks why overparameterized models violate these predictions while still generalizing.

---

## Taxonomy of Generalization Bounds

```
GENERALIZATION BOUNDS
├── Combinatorial complexity
│   ├── VC Dimension          binary classification, 0/1 loss, distribution-free
│   ├── Natarajan Dimension   multiclass extension
│   └── Fat-shattering Dim    real-valued functions, margin classifiers
│
├── Functional complexity
│   ├── Rademacher Complexity  data-dependent, applies to any bounded loss
│   ├── Gaussian Complexity    related, sometimes tighter in continuous settings
│   └── Covering Numbers       metric entropy; exponential in parameter count
│
├── Algorithmic stability
│   ├── Uniform stability      Bousquet & Elisseeff 2002; ERM algorithms
│   └── On-average stability   Hardt, Recht, Singer 2016; SGD analysis
│
├── Information-theoretic
│   ├── PAC-Bayes              McAllester; bounds via KL(Q||P) from prior
│   ├── Mutual information     Russo & Zou 2016; I(W; S) controls gap
│   └── CMI (conditional MI)   Steinke & Zakynthinou 2020; tighter
│
└── Optimization-based
    ├── Neural Tangent Kernel  Jacot 2018; infinite-width limit
    ├── Mean field theory      large but finite width
    └── PAC-Bayes + SGD        implicit regularization via trajectory
```

---

## Learning Models: A Taxonomy

```
+─────────────────────────────────────────────────────────────────+
|                  FORMAL LEARNING MODELS                          |
|                                                                  |
|  REALIZABILITY SETTING (target in H)                            |
|  ─────────────────────────────────                               |
|  PAC Learning (Valiant 1984)                                    |
|  • There exists h* ∈ H with R(h*) = 0                           |
|  • Goal: find h with R(h) ≤ ε with prob ≥ 1-δ                   |
|  • Sample complexity: m = O(log|H|/ε) finite H,                 |
|    or O(VC(H)/ε) for infinite H                                  |
|                                                                  |
|  AGNOSTIC SETTING (no assumption on target)                     |
|  ───────────────────────────────────────                         |
|  Agnostic PAC / Statistical Learning Theory                     |
|  • Compete with best h ∈ H (which may have nonzero error)        |
|  • Goal: R(h) ≤ min_{h*∈H} R(h*) + ε with prob ≥ 1-δ           |
|  • Sample complexity driven by VC dimension                      |
|                                                                  |
|  ONLINE LEARNING                                                 |
|  ─────────────                                                   |
|  • Adversarial: no distributional assumptions                    |
|  • Regret vs best fixed h ∈ H in hindsight                      |
|  • Littlestone dimension replaces VC dimension                   |
|                                                                  |
|  BAYESIAN / PAC-BAYES                                            |
|  ────────────────────                                            |
|  • Prior P over H, posterior Q after seeing S                    |
|  • Bound involves KL(Q || P): complexity = surprise from prior   |
|                                                                  |
+─────────────────────────────────────────────────────────────────+
```

---

## Sample Complexity vs Computational Complexity

A critical distinction your TCS background makes obvious, but worth making sharp in the ML context:

```
SAMPLE COMPLEXITY               COMPUTATIONAL COMPLEXITY
─────────────────               ────────────────────────
How many examples               How much time / compute
to learn accurately?            to find the hypothesis?

Bounded by VC dimension,        Separate question entirely.
Rademacher complexity,          A class can be PAC-learnable
PAC-Bayes KL term.              in finite samples but NP-hard
                                to find the ERM.
SEPARABLE: these are
independent axes.               Example: Learning intersections
                                of halfspaces — small VC dim,
An efficient PAC learner        computationally hard.
must achieve BOTH.
                                DNF formulas: VC-dim = n,
                                learning is hard unless
                                RP = NP (Kearns & Valiant).
```

The "efficient PAC learning" question asks for polynomial time AND polynomial sample complexity simultaneously.

---

## Classical Learnability Hierarchy

```
CONCEPT CLASSES (efficient PAC learnability)
│
├── EFFICIENTLY PAC-LEARNABLE
│   ├── Halfspaces (linear classifiers) — LP or perceptron
│   ├── Decision lists — greedy algorithm works
│   ├── DFAs from membership queries — Angluin L* algorithm
│   └── Monotone DNF — polynomial-time with random examples
│
├── POLYNOMIAL SAMPLES, HARD TO FIND ERM
│   ├── Depth-2 threshold networks
│   ├── DNF formulas — PAC with poly samples, no efficient learner known
│   └── Intersections of halfspaces
│
└── PROVABLY HARD (under cryptographic assumptions)
    ├── General neural networks (improper learning hardness)
    ├── Sparse parity with noise — hardness from learning parities
    └── Planted clique reductions — various geometric problems
```

---

## The Modern Problem: Theory vs Practice Gap

```
CLASSICAL THEORY PREDICTION      WHAT ACTUALLY HAPPENS
────────────────────────────     ─────────────────────
More parameters → more           Neural nets with 10⁸ params
overfitting                      generalize well

Bias-variance tradeoff:          Double descent: test error
optimal at intermediate          decreases again past
model size                       interpolation threshold

Explicit regularization          Unregularized SGD on neural
required for generalization      nets generalizes on MNIST

Kernel machines optimal for      Neural nets dramatically
bounded-norm function classes    outperform kernel methods
                                 on same function class
```

This gap is the engine of modern ML theory. NTK, double descent, implicit regularization, and grokking are all attempts to close it.

---

## Key Inequalities and Concentration Tools

These appear throughout every module — good to have in one place:

```
HOEFFDING'S INEQUALITY
  If X₁,...,Xₘ iid in [a,b], then:
  P(|Ē[X] - E[X]| ≥ t) ≤ 2 exp(-2m²t²/Σ(bᵢ-aᵢ)²)

UNION BOUND
  P(∃ bad event) ≤ Σ P(each bad event)
  Used to go from fixed-h bounds to uniform-over-H bounds

McDIARMID'S INEQUALITY
  If f(x₁,...,xₘ) changes by at most cᵢ when xᵢ changes,
  then f concentrates around its mean with exp(-2t²/Σcᵢ²)
  Core tool for Rademacher complexity bounds.

SYMMETRIZATION LEMMA
  Replaces true distribution with ghost sample via:
  E_S[sup_h (R(h) - R_S(h))] ≤ 2 E_S[Rademacher complexity]
  Bridges gap between fixed-distribution and worst-case analysis.
```

---

## Module Map

| Module | Core Concept | Key Theorem |
|--------|-------------|-------------|
| 01-PAC-LEARNING | Formal learning model | Fundamental theorem of PAC learning |
| 02-VC-DIMENSION | Combinatorial complexity | VC generalization bound; Sauer's lemma |
| 03-RADEMACHER | Data-dependent bounds | Rademacher generalization theorem |
| 04-BIAS-VARIANCE | Classical tradeoff | Bias-variance decomposition |
| 05-KERNEL-METHODS | RKHS theory | Mercer's theorem, SVM margin bound |
| 06-NEURAL-TANGENT | Infinite-width limit | NTK convergence theorem |
| 07-DOUBLE-DESCENT | Modern phenomenology | Interpolation threshold |
| 08-INFORMATION-THEORETIC | Compression = generalization | PAC-Bayes bound, MI bound |
| 09-OPEN-PROBLEMS | Frontier questions | — |

---

## Mathematical Prerequisites

| Area | Where It Appears |
|------|-----------------|
| Probability theory | Distribution D, expectations, concentration inequalities |
| Measure theory | Formal treatment of learning problems, Rademacher expectations |
| Functional analysis | RKHS, bounded linear operators, kernel theory |
| Linear algebra | Gram matrices, NTK, feature maps, spectral methods |
| Optimization | SGD dynamics, convexity, convergence rates |
| Information theory | PAC-Bayes, MDL, mutual information bounds |
| Combinatorics | VC shattering, growth function counting, Sauer's lemma |

All of this is MIT Mathematics + TCS territory — treated as given throughout.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Does H have finite VC dimension? | Probably agnostic PAC learnable |
| Is ERM computationally tractable for H? | Separate question from sample complexity |
| Data-dependent tighter bound needed? | Use Rademacher, not VC |
| Want probabilistic guarantee over the posterior? | PAC-Bayes |
| Analyzing infinite-width networks? | Neural Tangent Kernel framework |
| Model interpolates training data but generalizes? | Double descent regime |
| Prior knowledge available over parameters? | PAC-Bayes or Bayesian approach |
| Online, adversarial setting? | Littlestone dimension, not VC |

---

## Common Confusion Points

**"VC dimension vs Rademacher — which to use?"**
VC dimension: combinatorial, distribution-free, tight for binary 0/1-loss classifiers. Rademacher: data-dependent, tighter in practice, applies to any bounded loss. Rademacher bounds always subsume VC-based bounds (up to constants). Use VC for intuition; use Rademacher for actual analysis.

**"PAC learning vs statistical learning theory — same thing?"**
PAC (Valiant 1984) originated in computational learning theory, emphasizing both sample and computational efficiency, often under realizability. SLT (Vapnik-Chervonenkis) emphasizes agnostic bounds and generalization. Modern treatments merge both; the "fundamental theorem of statistical learning" ties VC dimension to PAC learnability in the agnostic setting.

**"Why don't classical bounds apply to deep learning?"**
Classical uniform convergence bounds read: R(h) ≤ R_S(h) + O(√(VCdim(H)/m)). For neural nets with billions of parameters, VCdim(H) ≫ m always, making bounds vacuous. Implicit regularization from SGD, the specific loss landscape structure, and inductive biases must do the work that explicit regularization does classically.

**"Agnostic PAC vs PAC — when does realizability matter?"**
Under realizability (target in H), you get O(log(1/δ)/ε) samples. In agnostic setting, you pay O(1/ε²) for the extra generality. A factor of 1/ε is the cost of not knowing the target concept is achievable.
