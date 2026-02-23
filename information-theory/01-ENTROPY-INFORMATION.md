# Entropy & Information — Shannon's Core Measures

---

## Big Picture

```
SELF-INFORMATION of event x with probability p(x):
  I(x) = log₂(1/p(x)) = -log₂ p(x)   [bits]

Interpretation: "how surprised are you?" or "how many bits to describe x?"
  p(x) = 1 → I = 0 bits (certain → no surprise)
  p(x) = 1/2 → I = 1 bit (fair coin flip)
  p(x) = 1/8 → I = 3 bits (needs 3 binary questions)

ENTROPY: expected self-information over the distribution
  H(X) = E[I(X)] = -Σ p(x) log₂ p(x)   [bits/symbol]
```

---

## Shannon Entropy

```
H(X) = -Σ_{x ∈ X} p(x) log₂ p(x)

PROPERTIES:
• H(X) ≥ 0   (always non-negative)
• H(X) = 0   iff p(x₀) = 1 for some x₀  (no uncertainty)
• H(X) ≤ log₂ |X|   (max entropy = uniform distribution)
  Proof: Jensen's inequality (log is concave)
• Continuity: H(p) continuous in p
• Symmetry: H(p₁,...,p_n) = H(p_{π(1)},...,p_{π(n)}) for any permutation π
• Additivity: H(X,Y) = H(X) + H(Y)  iff X,Y independent
• Concavity: H(λp + (1-λ)q) ≥ λH(p) + (1-λ)H(q)
```

**Binary entropy:**

```
h(p) = -p log₂ p - (1-p) log₂(1-p)

h(0) = h(1) = 0   (certain → no entropy)
h(0.5) = 1 bit    (maximum)
h(0.1) ≈ 0.47 bits
```

**Differential entropy (continuous X):**

```
h(X) = -∫ f(x) log f(x) dx

NOT always non-negative: h(X) can be negative for concentrated distributions
NOT scale-invariant: h(aX) = h(X) + log|a|

Maximum differential entropy: For fixed variance σ², h(X) ≤ ½ log(2πeσ²)
Achieved by Gaussian: h(N(μ,σ²)) = ½ log(2πeσ²)
→ Gaussian is maximum entropy distribution with fixed variance
```

---

## Joint and Conditional Entropy

```
JOINT ENTROPY:
  H(X,Y) = -Σ_{x,y} p(x,y) log p(x,y)

CONDITIONAL ENTROPY:
  H(Y|X) = Σ_x p(x) H(Y|X=x)
           = -Σ_{x,y} p(x,y) log p(y|x)

CHAIN RULE:
  H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)

CONDITIONING REDUCES ENTROPY:
  H(X|Y) ≤ H(X)   (knowledge of Y cannot increase uncertainty about X)
  H(X|Y) = H(X)   iff X ⊥ Y (independent)

CHAIN RULE FOR N VARIABLES:
  H(X₁,...,Xₙ) = Σ_{i=1}^n H(Xᵢ | X₁,...,X_{i-1})
```

---

## Mutual Information

The most important measure of dependence.

```
MUTUAL INFORMATION:
  I(X;Y) = H(X) - H(X|Y)
           = H(Y) - H(Y|X)
           = H(X) + H(Y) - H(X,Y)
           = Σ_{x,y} p(x,y) log [p(x,y)/(p(x)p(y))]

INTERPRETATION: "How much does knowing Y reduce uncertainty about X?"
                "How many bits of X are predictable from Y?"
                "How far is the joint distribution from independence?"

PROPERTIES:
  I(X;Y) ≥ 0   (equality iff X ⊥ Y)
  I(X;Y) = I(Y;X)   (symmetric)
  I(X;Y) ≤ min(H(X), H(Y))
  I(X;X) = H(X)   (self-information = entropy)
  Data processing inequality: X → Y → Z implies I(X;Z) ≤ I(X;Y)
    → Processing can only lose information, never create it
    → Z = f(Y) with deterministic f: I(X;Z) ≤ I(X;Y)

VENN DIAGRAM:
       ┌───────────────────────┐
       │   H(X,Y)              │
       │  ┌──────┬──────┐      │
       │  │ H(X│Y)│I(X;Y)│H(Y│X)│
       │  └──────┴──────┘      │
       └───────────────────────┘
```

**Conditional mutual information:**

```
I(X;Y|Z) = H(X|Z) - H(X|Y,Z)
           = Σ_z p(z) I(X;Y|Z=z)

Chain rule: I(X₁,...,Xₙ;Y) = Σ_i I(Xᵢ;Y|X₁,...,X_{i-1})
```

---

## KL Divergence (Relative Entropy)

```
KL(P||Q) = Σ_x p(x) log [p(x)/q(x)]   (discrete)
           = ∫ p(x) log [p(x)/q(x)] dx  (continuous)

PROPERTIES:
  KL(P||Q) ≥ 0   (Gibbs inequality)
  KL(P||Q) = 0   iff P = Q (a.e.)
  NOT symmetric: KL(P||Q) ≠ KL(Q||P) in general
  NOT a metric (no triangle inequality)

INTERPRETATION:
  "Extra bits needed when using code optimized for Q but true distribution is P"
  Regret of wrong model assumption
  Divergence measure (not distance)

RELATION TO OTHER QUANTITIES:
  I(X;Y) = KL(p(x,y) || p(x)p(y))   (how far joint is from product)
  H(X) = log|X| - KL(p || uniform)   (entropy gap from maximum)

FORWARD vs REVERSE KL:
  KL(P||Q): "exclusive" — Q=0 where P>0 → infinite penalty → Q covers all of P
  KL(Q||P): "inclusive" — Q spreads to cover all of P, even where P is small
  → Matters for variational inference:
    Minimizing KL(Q||P) (ELBO): Q understimates support of P (mode-seeking)
    Minimizing KL(P||Q): Q overestimates support (mean-seeking)
```

---

## Information Inequalities

```
GIBBS INEQUALITY (foundation of KL ≥ 0):
  -Σ p(x) log q(x) ≥ -Σ p(x) log p(x) = H(X)
  Cross-entropy H(P,Q) ≥ H(P)
  Equality iff P = Q

JENSEN'S INEQUALITY (used everywhere):
  For convex function φ: φ(E[X]) ≤ E[φ(X)]
  For concave function φ: φ(E[X]) ≥ E[φ(X)]
  log is concave → E[log X] ≤ log E[X]

LOG-SUM INEQUALITY:
  Σᵢ aᵢ log(aᵢ/bᵢ) ≥ (Σaᵢ) log(Σaᵢ/Σbᵢ)
  Used to prove subadditivity of entropy

FANO'S INEQUALITY:
  P_e = P(X̂ ≠ X) → H(X|Y) ≤ h(P_e) + P_e log(|X|-1)
  "If you can't predict X from Y with low error, X|Y must have high entropy"
  → Lower bound on error probability from entropy

DATA PROCESSING INEQUALITY:
  Markov chain X → Y → Z: I(X;Z) ≤ I(X;Y)
  Consequence: no deterministic function of Y can increase mutual information with X
  Application: feature extraction cannot increase relevant information beyond raw features
```

---

## Information Diagrams (I-diagrams)

```
THREE VARIABLES X, Y, Z:
  Regions: I(X;Y;Z), I(X;Y|Z), I(X;Z|Y), I(Y;Z|X), H(X|Y,Z), H(Y|X,Z), H(Z|X,Y)

  Interaction information (co-information):
  I(X;Y;Z) = I(X;Y) - I(X;Y|Z)
  Can be NEGATIVE (synergy: Z helps X predict Y, but Z itself doesn't help)
  vs POSITIVE (redundancy: Z,Y both carry same info about X)
```

---

## Entropy Rate

For a stationary process {Xᵢ}:

```
ENTROPY RATE:
  H(X) = lim_{n→∞} H(X₁,...,Xₙ)/n = lim_{n→∞} H(Xₙ|X_{n-1},...,X₁)

For ergodic Markov chain: H(X) = -Σ_{i,j} μᵢ P_{ij} log P_{ij}
  μ = stationary distribution, P = transition matrix

ENGLISH TEXT:
  Shannon (1951): ~1–1.5 bits/character (by human guessing experiment)
  Formal bound (with n-gram): ~1.3 bits/char (decreases with larger context)
  Compare: ASCII = 8 bits/char → ~6:1 compression possible
  Modern LLMs: measured ~1 bit/char perplexity on held-out text → near Shannon limit?
```

---

## Decision Cheat Sheet

| Quantity | Formula | Range | Meaning |
|----------|---------|-------|---------|
| Entropy H(X) | -Σ p log p | [0, log\|X\|] | Average uncertainty |
| Joint entropy H(X,Y) | -Σ p(x,y) log p(x,y) | ≥ max(H(X),H(Y)) | Combined uncertainty |
| Conditional entropy H(X\|Y) | H(X,Y) - H(Y) | [0, H(X)] | Remaining uncertainty given Y |
| Mutual info I(X;Y) | H(X) - H(X\|Y) | [0, min(H(X),H(Y))] | Shared information |
| KL divergence KL(P\|\|Q) | Σ p log(p/q) | [0, ∞) | "Extra bits" from wrong model |
| Cross-entropy H(P,Q) | -Σ p log q | [H(P), ∞) | H(P) + KL(P\|\|Q) |
