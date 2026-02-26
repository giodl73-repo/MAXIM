# VC Dimension and Shattering

## The Big Picture

VC dimension (Vapnik-Chervonenkis, 1971) is the combinatorial measure of hypothesis class complexity that controls PAC learnability. It captures the richest interaction between the hypothesis class and any finite sample.

```
+──────────────────────────────────────────────────────────────────+
|                  VC DIMENSION FRAMEWORK                          |
|                                                                  |
|  SHATTERING                                                      |
|  H shatters a set C = {x₁,...,xd} iff for every labeling       |
|  y: C → {0,1}, there exists h ∈ H with h(xᵢ) = yᵢ for all i    |
|                                                                  |
|  VC DIMENSION                                                    |
|  VCdim(H) = largest d such that some set of d points is         |
|             shattered by H                                       |
|           = ∞ if H shatters sets of every size                  |
|                                                                  |
|  FUNDAMENTAL THEOREM OF STATISTICAL LEARNING                    |
|  The following are equivalent for binary classification:         |
|  (1) H has finite VC dimension                                   |
|  (2) H is PAC learnable (realizable)                             |
|  (3) H is agnostic PAC learnable                                 |
|  (4) H has the uniform convergence property                      |
+──────────────────────────────────────────────────────────────────+
```

---

## Shattering: Step by Step

**Example 1: Intervals on the real line**

Hypothesis class H = {[a,b] : a ≤ b} (classify positive iff inside interval)

```
Can H shatter 2 points {x₁, x₂} with x₁ < x₂?

  Labeling (0,0):  use interval [∞, -∞] (empty) — no point inside  ✓
  Labeling (1,0):  use interval [x₁, x₁]                           ✓
  Labeling (0,1):  use interval [x₂, x₂]                           ✓
  Labeling (1,1):  use interval [x₁, x₂]                           ✓
  → Yes, H shatters {x₁, x₂}

Can H shatter 3 points {x₁, x₂, x₃} with x₁ < x₂ < x₃?

  Try labeling (1,0,1): need h with h(x₁)=1, h(x₂)=0, h(x₃)=1
  An interval must be contiguous — cannot classify x₁ and x₃
  positive while x₂ is negative.
  → No set of 3 points is shattered.

VCdim(H) = 2
```

**Example 2: Halfspaces in ℝ²**

H = {sign(w·x + b) : w ∈ ℝ², b ∈ ℝ}

```
3 points in general position (non-collinear):
  For any of the 8 labelings, draw a line separating + from −.
  ✓ H shatters these 3 points.

4 points (say, corners of a square):
  The XOR labeling (++−−ᵀ diagonally opposite) cannot be
  achieved by a halfspace.
  → No 4 points in ℝ² are shattered by halfspaces.

VCdim(halfspaces in ℝ²) = 3

General: VCdim(halfspaces in ℝⁿ) = n+1
```

---

## Sauer's Lemma: The Growth Function

The growth function counts the maximum number of distinct labelings H can impose on any m points:

```
GROWTH FUNCTION
  Π_H(m) = max_{x₁,...,xₘ ∈ X} |{(h(x₁),...,h(xₘ)) : h ∈ H}|

SAUER-SHELAH LEMMA
  If VCdim(H) = d, then:
    Π_H(m) ≤ Σᵢ₌₀ᵈ C(m,i)  ≤  (em/d)ᵈ

IMPLICATIONS
  m ≤ d:   Π_H(m) = 2^m       (can shatter — exponential)
  m > d:   Π_H(m) ≤ (em/d)^d  (polynomial in m!)

This is the critical transition: past VC dimension,
the growth function drops from exponential to polynomial.
```

The jump from 2^m to poly(m) is what makes finite VC dimension the lever for generalization bounds.

---

## The VC Generalization Bound

```
MAIN THEOREM (VC Generalization Bound)
────────────────────────────────────────

For any distribution D, any δ ∈ (0,1), with probability ≥ 1-δ
over the draw of m iid samples, uniformly for all h ∈ H:

  |R(h) - R_S(h)| ≤ √( (8/m) · [d·ln(2em/d) + ln(4/δ)] )

where d = VCdim(H).

SAMPLE COMPLEXITY CONSEQUENCE
  To ensure generalization gap < ε with probability ≥ 1-δ,
  it suffices to have:
    m = O( (d · ln(1/ε) + ln(1/δ)) / ε² )

AGNOSTIC ERM BOUND
  If h_ERM = argmin_{h∈H} R_S(h), then:
    R(h_ERM) ≤ min_{h∈H} R(h) + 2√(d/m) + small δ-term
```

---

## Computing VC Dimension: Methods

```
+─────────────────────────────────────────────────────────────────+
|                COMPUTING VCdim: TWO STEPS                        |
|                                                                  |
|  STEP 1: LOWER BOUND                                             |
|  Exhibit a set of d points that H shatters.                     |
|  One construction achieves every labeling → d is achievable.    |
|                                                                  |
|  STEP 2: UPPER BOUND                                             |
|  Show no set of d+1 points can be shattered.                    |
|  Must hold for ALL sets of d+1 points, not just specific ones.  |
|                                                                  |
|  COMMON UPPER BOUND TECHNIQUES                                   |
|  • Dimension counting: parameterized by k real numbers          |
|    → VCdim ≤ k (usually; need to be careful)                    |
|  • Direct case analysis: enumerate all labelings                 |
|  • Radon's theorem: convex position argument for halfspaces      |
+─────────────────────────────────────────────────────────────────+
```

---

## VC Dimensions of Common Hypothesis Classes

| Hypothesis Class | Instance Space | VCdim |
|-----------------|---------------|-------|
| Intervals [a,b] | ℝ | 2 |
| Halfspaces | ℝⁿ | n+1 |
| Axis-aligned rectangles | ℝ² | 4 |
| Axis-aligned rectangles | ℝⁿ | 2n |
| Convex polygons with k sides | ℝ² | 2k+1 |
| Polynomials of degree d | ℝ | d+1 |
| Sine functions sin(ax) | ℝ | ∞ |
| Decision trees, depth k | {0,1}ⁿ | O(k·log n) |
| Neural nets: k layers, w weights | ℝⁿ | O(w² log w) |
| Neural nets: k layers, w weights | {0,1}ⁿ | Θ(w log w) |
| k-nearest neighbor (k=1) | Any | ∞ |
| Linear threshold on {0,1}ⁿ | {0,1}ⁿ | n |

The ∞ entries mean no finite sample guarantee from VC theory alone.

---

## Structural Properties

```
MONOTONICITY
  H₁ ⊆ H₂  →  VCdim(H₁) ≤ VCdim(H₂)
  Larger hypothesis class ≥ larger VC dimension.

COMPOSITION
  H₁ composed with H₂: VCdim ≤ 2·VCdim(H₁)·log(VCdim(H₁)) + ...
  (messy; the point is it stays bounded)

INTERSECTION
  VCdim(H₁ ∩ H₂) ≤ VCdim(H₁) + VCdim(H₂) + 1

UNION
  VCdim(H₁ ∪ H₂) ≤ VCdim(H₁) + VCdim(H₂) + 2·log(|X|)?
  — only clean when X is finite

FUNCTION COMPOSITION
  If g: Y → Z and H maps X → Y, then:
  VCdim(g ∘ H) ≤ VCdim(H)  (labels get coarser; can only decrease)
```

---

## VC Dimension for Neural Networks

```
SHALLOW NETWORKS (single hidden layer)
  n inputs, k hidden units (threshold activations)
  VCdim = O(nk log(nk))      — Baum & Haussler 1989
  VCdim = Ω(nk)              — lower bound exists

DEEP NETWORKS
  L layers, W total weights
  VCdim = O(W·L·log W)       — Goldberg & Jerrum
  VCdim = Ω(W·L)             — Bartlett et al.

MODERN LARGE NETWORKS
  GPT-3: ~175 billion parameters
  VCdim ≈ O(W·L·log W) ≈ 10¹²
  Training set: ~300 billion tokens ≈ 3×10¹¹

  → VCdim ≈ training set size
  → Classical VC bound: √(VC/m) ≈ O(1) ← vacuous!

  Classical theory gives USELESS bounds for modern deep learning.
  This is the theoretical crisis that motivated NTK, double descent.
```

---

## Natarajan Dimension: Multiclass Extension

For multiclass problems (k > 2 labels), VC dimension doesn't directly apply. The Natarajan dimension is the correct generalization:

```
NATARAJAN DIMENSION
  H: X → {1,...,k}
  H N-shatters a set C if for every function f: C → {1,...,k},
  there exists h ∈ H with h(xᵢ) = f(xᵢ) for all xᵢ ∈ C.

  Wait — that would be the trivial generalization.

  ACTUAL DEFINITION:
  H N-shatters C if there exist two functions f₁, f₂: C → {1,...,k}
  with f₁(x) ≠ f₂(x) for all x ∈ C, and for every T ⊆ C,
  there exists h ∈ H with h(xᵢ) = f₁(xᵢ) for xᵢ ∈ T
                         and h(xᵢ) = f₂(xᵢ) for xᵢ ∉ T.

Ndim(H) = max size of N-shattered set

MULTICLASS FUNDAMENTAL THEOREM
  H is multiclass PAC-learnable iff Ndim(H) < ∞.
```

---

## Decision Cheat Sheet

| Task | Approach | Notes |
|------|----------|-------|
| Prove H is PAC-learnable | Show VCdim(H) < ∞ | Sufficient and necessary |
| Get sample complexity bound | m = O(d/ε²) agnostic | d = VCdim(H) |
| Prove H is NOT learnable | Show VCdim(H) = ∞ | Or show shattering of all sizes |
| Lower bound sample complexity | Exhibit shattered set of size d | Show d points truly shattered |
| VC dim of neural net | O(W·L·log W) | W = weights, L = layers |
| Deep learning theory | VC bounds are vacuous | Need NTK or double descent theory |
| Multiclass | Use Natarajan dimension | Not VC directly |

---

## Common Confusion Points

**"VCdim(halfspaces in ℝⁿ) = n+1, but I have a billion parameters — doesn't that mean huge VC dim?"**
Yes. Modern neural nets have enormous VC dimension — comfortably exceeding training set size. Classical VC bounds are therefore vacuous. The fact that neural nets generalize anyway is the central mystery driving modern ML theory.

**"Can a hypothesis class shatter infinitely many points?"**
Yes — for example, the class of all functions f: ℝ → {0,1} shatters any set. Also, the class {sin(nx) > 0 : n ∈ ℕ} has infinite VC dimension (and indeed this class fails spectacularly to generalize). Infinite VC dimension is a real obstruction.

**"Does VCdim = d mean exactly d points are shattered, or at least d?"**
Exactly the *maximum* d. VCdim = d means some set of d points is shattered, and no set of d+1 points is shattered. So some smaller sets might not be shattered — the definition asks for existence of a shattered set of that size, not that every set of size d is shattered.

**"Sauer's lemma says growth function is polynomial — why does that help?"**
The generalization proof works by counting how many ways H can behave on the sample S. If this count is polynomial (rather than exponential), a union bound over bad hypotheses can be made to converge with polynomial samples. Exponential → impossible; polynomial → PAC learnable.
