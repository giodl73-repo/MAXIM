# PAC Learning: Valiant Framework

## The Big Picture

PAC learning (Probably Approximately Correct, Valiant 1984) is the foundational formal model for asking when a concept can be learned from data. It cleanly separates *what is learnable* from *how hard it is to learn*, while providing the language for all subsequent theory.

```
+──────────────────────────────────────────────────────────────────+
|                  PAC LEARNING FRAMEWORK                          |
|                                                                  |
|  INPUTS                                                          |
|  ──────                                                          |
|  • Unknown distribution D over instance space X                 |
|  • Unknown target concept c* ∈ C (concept class C over X)       |
|  • Error parameter ε ∈ (0, 1)                                   |
|  • Confidence parameter δ ∈ (0, 1)                              |
|  • Training set S = {(x₁,y₁),...,(xₘ,yₘ)}, xᵢ ~ D, yᵢ = c*(xᵢ) |
|                                                                  |
|  OUTPUT                                                          |
|  ──────                                                          |
|  • Hypothesis h ∈ H                                              |
|                                                                  |
|  SUCCESS CRITERION                                               |
|  ─────────────────                                               |
|  With probability ≥ 1-δ over choice of S:                       |
|    error(h) := Pr_{x~D}[h(x) ≠ c*(x)] ≤ ε                      |
|                                                                  |
|  "Probably" = with probability 1-δ                               |
|  "Approximately Correct" = error at most ε                       |
+──────────────────────────────────────────────────────────────────+
```

---

## Formal Setup

**Instance space**: X (typically {0,1}ⁿ or ℝⁿ)

**Concept**: A function c: X → {0,1}

**Concept class**: C = a set of concepts; the learning problem is defined by C

**Hypothesis class**: H = set of functions the learner outputs from; often H = C, sometimes H ⊃ C (improper learning)

**Distribution D**: Unknown, fixed, arbitrary distribution over X. The PAC model is *distribution-free* — the same sample bound must work for any D.

```
REALIZABILITY ASSUMPTION (standard PAC)
  There exists c* ∈ C such that for all (x,y) in training data,
  y = c*(x).  The target concept is in the class.

AGNOSTIC PAC (relaxed)
  No assumption on labels.  Goal becomes:
  error(h) ≤ min_{c ∈ C} error(c) + ε
  The learner competes with the best concept in C.
```

---

## Sample Complexity: Finite Hypothesis Classes

For finite H, the analysis is clean and illustrates the core proof technique.

**Setup**: Realizability. There exists h* ∈ H with error 0. The ERM learner picks any h consistent with all m training examples.

**Question**: How large must m be so that h is probably approximately correct?

```
PROOF SKETCH (consistent learner, finite H)
────────────────────────────────────────────

Call h ∈ H "bad" if error(h) > ε.

Fix a bad h. It is consistent with one example with probability ≤ 1-ε.
It is consistent with all m examples with probability ≤ (1-ε)^m ≤ e^{-εm}.

Union over all bad hypotheses in H:
  Pr[∃ bad h consistent with S] ≤ |H| · e^{-εm}

Set this ≤ δ and solve for m:
  |H| · e^{-εm} ≤ δ
  m ≥ (1/ε) · ln(|H|/δ)

Result:  m = O(log|H| / ε) examples suffice.
```

**Insight**: You pay logarithmically in the size of the hypothesis class. This is why Occam's Razor has formal content — shorter descriptions → smaller H → fewer examples needed.

---

## Sample Complexity: Infinite Hypothesis Classes

For infinite H (e.g., all halfspaces in ℝⁿ), the above bound is vacuous. The correct quantity is VC dimension.

```
FUNDAMENTAL THEOREM OF PAC LEARNING

C is PAC learnable if and only if VCdim(C) < ∞.

Moreover, sample complexity satisfies:
  Ω( (d + log(1/δ)) / ε ) ≤ m_C(ε, δ) ≤ O( (d log(1/ε) + log(1/δ)) / ε )

where d = VCdim(C).

In the agnostic setting:
  m_C(ε, δ) = Θ( (d + log(1/δ)) / ε² )
```

The 1/ε → 1/ε² gap between realizable and agnostic is fundamental — agnostic learning requires a square more data to achieve the same accuracy.

---

## Efficient PAC Learning

PAC learnability (finite sample complexity) does NOT imply efficient learning. You also need:

```
EFFICIENT PAC LEARNER REQUIREMENTS
───────────────────────────────────

1. POLYNOMIAL SAMPLE COMPLEXITY
   m = poly(1/ε, 1/δ, n, size(c*))
   where n = instance size, size(c*) = representation size of target

2. POLYNOMIAL TIME
   The learning algorithm runs in time poly(m, n)

3. PROPER vs IMPROPER
   Proper:   output hypothesis is in C
   Improper: output hypothesis may be in larger H ⊃ C
   Improper learning sometimes easier computationally
```

**Key separation**: Valiant showed some concept classes have poly sample complexity but no known poly-time learner (unless RP = NP).

---

## Examples of PAC Learnability

```
CONCEPT CLASS         PAC LEARNABLE?   EFFICIENT?   ALGORITHM
─────────────────     ──────────────   ──────────   ─────────
Conjunctions          Yes (d=n)        Yes          Eliminate inconsistent literals
k-CNF (fixed k)       Yes              Yes          Brute force over (2n+1)^k formulas
3-CNF (k=3, n-var)    Yes (samples)    NO           Kearns-Valiant hardness
DNF                   Yes (samples)    NO           Hard unless RP=NP
Halfspaces            Yes              Yes          LP / Perceptron
Decision lists        Yes              Yes          Greedy
DFAs (with queries)   Yes              Yes          Angluin L* (uses membership queries)
Depth-2 NNs           Yes (samples)    Unknown      No poly-time ERM algorithm known
```

---

## The Occam's Razor Theorem

The formal version: if a learner can compress the training data, it generalizes.

```
OCCAM'S RAZOR THEOREM (Blumer et al. 1987)
───────────────────────────────────────────

Let A be an algorithm that on input S of size m outputs h ∈ H where:
  (1) h is consistent with S (zero training error)
  (2) The representation size of h is at most s bits

Then with probability ≥ 1-δ:
  error(h) ≤ (s · ln 2 + ln(1/δ)) / m

Equivalently, need m ≥ (s ln 2 + ln(1/δ)) / ε to get error ≤ ε.

This is tight: |H| ≤ 2^s, so log|H| ≤ s, recovering the finite-class bound.
```

**Interpretation**: A short description of the training-consistent hypothesis implies good generalization. Compression is sufficient for generalization. This is why gzip-style arguments have theoretical traction in modern ML.

---

## Computational Hardness: The Valiant-Kearns Results

```
HARDNESS LANDSCAPE (under cryptographic assumptions)
────────────────────────────────────────────────────

HARD TO LEARN EFFICIENTLY (unless RP = NP or similar):
  • DNF formulas (even monotone DNF)
  • Intersections of halfspaces
  • k-term DNF for k ≥ 3

HARD EVEN WITH MEMBERSHIP QUERIES:
  • Constant-depth circuits (superpolynomial size)
  • General Boolean circuits

KEY TECHNIQUE:
  Reduction from satisfiability, factoring, or planted clique
  to learning problem. If you could learn C efficiently,
  you could solve NP-hard problem efficiently.

NOTE: Neural network hardness results:
  Blum & Rivest (1992): Learning 3-node networks is NP-hard.
  Yet in practice, SGD finds good solutions on huge networks.
  → Hardness of worst-case ERM ≠ hardness of learning on natural data.
```

---

## Query Models

Standard PAC uses only random examples. Extensions allow other query types:

```
QUERY TYPE              WHAT IT PROVIDES               EXAMPLE
───────────────         ────────────────               ───────
Random examples         (x, c*(x)), x ~ D              Standard PAC
Membership query        Oracle answers c*(x) for any x  Angluin's L*
Equivalence query       Oracle says YES or gives        Exact learning
                        counterexample
Comparison query        Oracle compares c*(x) vs c*(y)  Active learning
Unlabeled examples      x ~ D, label requested          Active learning
Corrupted labels        y = c*(x) XOR noise             Agnostic / noisy PAC
```

**Active learning**: If you can choose which points to label (membership queries from D), sample complexity can drop dramatically — sometimes from O(d/ε²) to O(d · log(1/ε)/ε) for halfspaces.

---

## The ε-δ Parameterization: Practical Reading

```
READING SAMPLE COMPLEXITY FORMULAS
────────────────────────────────────

m = O(d log(1/ε) / ε)     [realizable PAC]
m = O(d / ε²)              [agnostic PAC]

EXAMPLE: d = 100 (VC dim), ε = 0.01, δ = 0.05

Realizable: m ~ 100 · log(100) / 0.01 ≈ 46,000 examples
Agnostic:   m ~ 100 / (0.01)²         = 1,000,000 examples

The agnostic cost: 20× more data for same (ε, δ).
The δ dependence: only logarithmic — halving failure probability
costs almost nothing in samples.
```

---

## Decision Cheat Sheet

| Situation | Sample bound | Notes |
|-----------|-------------|-------|
| Finite H, realizable | O(log|H| / ε) | Occam bound |
| Finite H, agnostic | O(log|H| / ε²) | Agnostic costs 1/ε² |
| Infinite H, realizable | O(d log(1/ε) / ε) | d = VCdim(H) |
| Infinite H, agnostic | Θ(d / ε²) | Tight up to constants |
| With membership queries | Can be much smaller | Problem-dependent |
| Efficient PAC required | Need poly time + poly samples | Often open for neural nets |

---

## Common Confusion Points

**"PAC says I need ~1M examples but I fine-tune GPT with 1K and it works"**
PAC is distribution-free and worst-case. GPT's pretraining has already done enormous computation; fine-tuning is transfer learning, not learning from scratch. Also, modern implicit regularization from SGD operates outside the PAC framework. PAC gives correct *order* but not tight constants for natural data.

**"Realizability assumption is too strong — no real problem has zero Bayes error"**
Agreed. Agnostic PAC is the right model in practice. Realizability is used for clean proofs of the fundamental theorem and for establishing upper bounds. The key insight — that VC dimension controls learnability — holds in both settings.

**"Why does 1/ε in realizability become 1/ε² in agnostic?"**
In realizability, the consistent hypothesis cannot be bad in too many places — if it were, it would have violated a training example. In agnostic, all hypotheses may have nonzero error, so the learner must estimate *relative* errors, requiring tighter concentration, which costs a factor of 1/ε in the sample bound.

**"Proper vs improper — does it matter?"**
Computationally, yes. DNF formulas are hard to learn *properly* (output a DNF), but easy to learn *improperly* (output a polynomial threshold function that represents the same concept). Choosing H ⊃ C is sometimes the only tractable route.
