# Statistical Learning Theory
## Why Finite Data Generalizes — and When It Doesn't

```
THE GENERALIZATION QUESTION

  Training data D = {(x_i, y_i)}  →  learn h: X→Y  →  predict on unseen x
       n samples from P(X,Y)             from H             drawn from same P

  Risk R(h)      = E_{(x,y)~P}[ℓ(h(x), y)]       ← true, unknowable
  Emp. risk R̂(h) = (1/n) Σ ℓ(h(x_i), y_i)        ← measurable

  Generalization gap: R(h) - R̂(h)  ← how much does training loss underestimate test loss?
```

---

## 1. The Learning Problem — Formal Setup

**Hypothesis class H**: the set of functions the learner is allowed to output.
- Linear classifiers: `H = {x ↦ sign(w·x + b) | w ∈ ℝ^d, b ∈ ℝ}`
- Neural nets with architecture A: all parameter settings
- Decision trees of depth ≤ k

**Loss function ℓ**: `Y × Y → ℝ₊`
- 0-1 loss: `ℓ(ŷ, y) = 1[ŷ ≠ y]` — standard for classification
- Squared loss: `(ŷ - y)²` — regression
- Hinge, log-loss, huber...

**ERM (Empirical Risk Minimization)**:
```
ĥ = argmin_{h ∈ H} R̂(h)
```
Minimize what you can measure. The central algorithm of supervised learning.

**Agnostic vs Realizable**:
- Realizable: ∃ h* ∈ H with R(h*) = 0 (the truth lives in H)
- Agnostic: no assumption — best you can do is match the best h ∈ H

---

## 2. Bias-Variance Decomposition

Under squared loss, for a fixed test point x:

```
E_D[(h_D(x) - y)²] = Bias²(x) + Var(x) + σ²_noise

  Bias(x)  = E_D[h_D(x)] - f*(x)              ← systematic error: H is wrong
  Var(x)   = E_D[(h_D(x) - E_D[h_D(x)])²]     ← sensitivity to which D you got
  σ²_noise = E[(y - f*(x))²]                  ← irreducible, from label noise
```

**The tradeoff**:
```
  Small H (linear)                 Large H (deep net)
  ────────────────────────────     ──────────────────────────────────
  High bias — underfits            Low bias — can fit anything
  Low variance — stable output     High variance — sensitive to D
  R(h) ≈ R̂(h) + large const       R(h) >> R̂(h) typically
```

Classical story: U-shaped test error curve as complexity grows.
Modern twist: double descent (§7) breaks this past the interpolation threshold.

---

## 3. Uniform Convergence and Finite H

**Goal**: bound `sup_{h∈H} |R(h) - R̂(h)|` — does ERM work uniformly?

For **finite H**, union bound + Hoeffding's inequality gives:

```
P[ sup_{h∈H} |R(h) - R̂(h)| > ε ] ≤ 2|H| · exp(-2nε²)

Rearranged — with probability ≥ 1-δ, for all h ∈ H simultaneously:
  R(h) ≤ R̂(h) + √(log(2|H|/δ) / 2n)

For ERM solution ĥ:
  R(ĥ) ≤ R(h*) + 2√(log(2|H|/δ) / 2n)
```

Bound scales as `√(log|H| / n)`. The log compresses H — exponentially large finite H can still generalize.

**Problem**: most interesting H is infinite. Need a complexity measure that works for infinite classes.

---

## 4. VC Dimension

**Shattering**: H shatters C = {x_1,...,x_m} if for every binary labeling y ∈ {±1}^m, some h ∈ H agrees with y on all of C.

```
  H = halfplanes in ℝ²:

    ·   ·          Any 3 points in general position: shattered (YES)
       ·            Any 4 points: XOR configuration fails  (NO)

  → VC(halfplanes in ℝ²) = 3
```

**VC dimension**: `VCdim(H) = max{m : ∃ C of size m that H shatters}`

**Key examples**:
| H | VCdim |
|---|-------|
| Halfplanes in ℝ^d | d+1 |
| Degree-k polynomials in ℝ | k+1 |
| Balls in ℝ^d | d+1 |
| Convex polygons in ℝ² | ∞ |
| 1-NN classifier | ∞ |
| Neural net (n params, piecewise linear) | O(n log n) |

**Fundamental Theorem of Statistical Learning** (Vapnik-Chervonenkis):
```
For binary classification, TFAE:
  1. H is PAC learnable (agnostic)
  2. VCdim(H) < ∞
  3. ERM learns H

Bound: with probability ≥ 1-δ, for VCdim(H) = d:
  R(ĥ) ≤ R(h*) + O( √((d·log(n/d) + log(1/δ)) / n) )
```

**Sauer-Shelah Lemma**: Growth function `m_H(n) ≤ Σ_{k=0}^d C(n,k) = O(n^d)`. VC dimension d means H can realize at most O(n^d) distinct labelings on n points — polynomial, not exponential.

---

## 5. PAC Learning

**Probably Approximately Correct** (Valiant 1984):

```
Algorithm A PAC-learns H if:
  ∀ ε, δ > 0, ∀ distribution D:
  A uses m(ε, δ) samples, runs in poly(1/ε, 1/δ, size(x)) time, outputs h with:

    P_{D^m}[ R(h) ≤ R(h*) + ε ] ≥ 1 - δ
                        ↑               ↑
                   ε-approximate     probably (1-δ confidence)
```

**Sample complexity** for agnostic PAC with VCdim d:
```
m(ε, δ) = O( (d + log(1/δ)) / ε² )
```

**Computational vs statistical complexity split**:
- Statistical: how many samples needed? → VC theory
- Computational: how long to find ERM? → separate question
- ERM for 3-layer neural nets is NP-hard in the worst case
- SGD finds "good enough" solutions heuristically; not provably optimal under PAC

**Learning complexity classes**:
```
  Efficiently PAC-learnable  ⊆  PAC-learnable  ⊆  identifiable in the limit

  Boolean conjunctions:       efficiently PAC (LP)
  3-CNF:                      PAC but likely not efficiently (touches crypto)
  Halfspaces with margin:     efficiently PAC (SVM / perceptron)
```

---

## 6. Rademacher Complexity

VC dimension is worst-case over distributions. Rademacher complexity is data-dependent — tighter in practice.

**Definition**: for function class F and sample S = {x_1,...,x_n}:
```
R̂_n(F) = E_σ[ sup_{f∈F} (1/n) Σ_i σ_i f(x_i) ]

  where σ_i ~iid Uniform({±1})   ← Rademacher variables = pure noise labels
```

**Intuition**: how well can F correlate with pure noise on your actual data? High R̂_n = F can fit noise = bad generalization.

**Generalization bound**:
```
With probability ≥ 1-δ, for all f ∈ F:
  R(f) ≤ R̂(f) + 2R̂_n(F) + √(log(2/δ) / 2n)
```

**Why better than VC**: VC is worst-case over all distributions; Rademacher uses the actual sample. Can give meaningful bounds even when VCdim = ∞ if the data structure is benign.

**Rademacher for neural nets** (spectral norm bound):
```
For L-layer net with weight matrices W_k, ‖W_k‖_F ≤ B_k, input ‖X‖_F ≤ C_X:
  R̂_n(F) ≤ (√(2 log 2) · Π_k ‖W_k‖_F · C_X) / √n

Frobenius norm product bounds generalization → theoretical justification for weight decay
```

---

## 7. Double Descent

Classical bias-variance predicts a single U-shaped test error curve. Overparameterized modern models break this.

```
Test error
  │
  │\         classical regime
  │ \       /
  │  \_____/          ← classical minimum
  │        \   /─────   ← modern interpolating regime (descends again)
  │         \_/
  │          ↑
  └──────────┴──────────────────────→  Model complexity (params / n)
        interpolation threshold
        (params ≈ n: variance spike)
```

**Two distinct regimes**:
1. **Underparameterized** (params < n): classical bias-variance U-shape
2. **Overparameterized** (params > n): model interpolates training data; test error descends again

**Why interpolation helps**:
- SGD/GD finds the **minimum norm interpolant** among all interpolating solutions
- For linear models: `ĥ = X^T(XX^T)^{-1}y` (min-norm pseudoinverse solution)
- This carries implicit regularization — not all interpolants generalize equally
- Neural nets: SGD finds flat minima (wide basins) that generalize (PAC-Bayes)

**The spike at threshold** (n ≈ params):
```
At threshold: X has near-null directions → pseudoinverse blows up → high variance
In overparameterized regime: regularization (min-norm) controls this
```

Double descent also appears **epoch-wise**: keep training past "early stopping optimum" and test error can descend again.

---

## 8. No Free Lunch

**Statement**: averaged over all possible target functions, every learning algorithm has the same expected test error.

```
∀ A, B:  E_f[ R(A(D_n, f)) ] = E_f[ R(B(D_n, f)) ]

where expectation is over uniform distribution over all f: X → {0,1}
```

**Implications**:
- No universal learner — you must bake in inductive bias
- The question is whether your bias matches the problem structure
- "Free lunch" = assuming nothing = paying full price at test time

**What this means in practice**:
```
  CNNs      → assume translation equivariance (strong bias for vision)
  Transformers → assume permutation equivariance + attention structure
  GNNs      → assume local message passing on graphs
  Linear    → assume linear separability

  The bias that crushes ImageNet helps nothing on random Boolean functions.
```

**Bayesian framing**: NFL = you need a prior. The prior is the inductive bias. A flat prior over all functions is the NFL worst case.

---

## 9. Structural Risk Minimization

Rather than fixing H and running ERM, let the hypothesis class grow:

```
H_1 ⊂ H_2 ⊂ H_3 ⊂ ...  (nested by complexity)

SRM: choose k* = argmin_k [ R̂(ĥ_k) + penalty(k, n, δ) ]

  where penalty comes from VC/Rademacher bounds
```

Theoretical justification for:
- Held-out validation and cross-validation (empirical SRM)
- AIC: `−2 log L̂ + 2k` (k = # params)
- BIC: `−2 log L̂ + k log n` (stronger penalty)
- MDL (Minimum Description Length): prefer model that compresses data most

---

## 10. Decision Cheat Sheet

| Concept | Key quantity | Practical implication |
|---------|-------------|----------------------|
| ERM | `argmin R̂(h)` | The baseline algorithm |
| Bias-variance | `MSE = Bias² + Var + σ²` | Diagnose under/overfitting |
| VC bound | `O(√(d log n / n))` | Binary classification, worst-case D |
| Rademacher bound | `R ≤ R̂ + 2R̂_n + ...` | Tighter, data-dependent |
| PAC sample complexity | `O((d + log 1/δ) / ε²)` | How much data do I need? |
| Double descent | interpolation threshold | Why overparameterization can help |
| NFL | no free lunch | Why inductive bias is mandatory |
| SRM | min R̂ + complexity penalty | Model selection theory |

---

## 11. Where This Surfaces in Practice

```
  PAC theory          →  cross_val_score(), GridSearchCV (empirical SRM)
  Bias-variance       →  learning_curve() in sklearn
  VC / Rademacher     →  weight decay (L2) = Frobenius norm regularization
  Double descent      →  why LLMs trained past convergence keep improving
  NFL                 →  why no single model wins every benchmark

  Deep learning:
    Implicit regularization of SGD ↔ minimum norm interpolant theory
    Flat minima ↔ PAC-Bayes generalization bounds
    NTK (neural tangent kernel) ↔ linearized infinite-width limit
```

---

## 12. Common Confusion Points

1. **"High VC dim = overfit"** — Not quite. High VC dim means *potentially* high variance. If your training data has structure, Rademacher complexity can still be small.

2. **"ERM always works"** — ERM is NP-hard for many H including neural nets. SGD heuristically finds good solutions but has no PAC guarantee.

3. **"Double descent means bias-variance is wrong"** — The decomposition is always correct. Double descent refines what "variance" means for minimum-norm interpolating estimators.

4. **"NFL makes learning impossible"** — NFL averages over all functions uniformly. Real-world distributions (images, language, physics) are not uniform — they have massive exploitable structure.

5. **"Overfitting = high test error"** — Overparameterized models can interpolate training data (technically "overfitting") yet generalize. The old term conflates interpolation with poor generalization.

6. **"More data always helps"** — True asymptotically under fixed distribution. With distribution shift, more data from the wrong distribution can hurt.

7. **"VC bounds are tight"** — Almost never. The constants are large. Bounds are useful for understanding scaling behavior and relative comparisons, not absolute guarantees.
