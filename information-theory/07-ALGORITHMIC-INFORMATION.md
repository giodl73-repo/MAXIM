# Algorithmic Information Theory

```
KOLMOGOROV COMPLEXITY: INFORMATION WITHOUT PROBABILITY

Shannon entropy:      H(X) = E[-log p(X)]     requires probability distribution
Kolmogorov complexity: K(x) = min |p|         defined for individual strings
                               U(p)=x

Shannon = average case over ensemble
Kolmogorov = worst case / individual string

┌──────────────────────────────────────────────────────────────────┐
│  K(x) = length of shortest self-delimiting program p             │
│         running on universal TM U that outputs x                 │
│                                                                  │
│  "The complexity of a string is the length of its shortest       │
│   description in a fixed universal formal language"              │
│                                         — Kolmogorov (1965)     │
│                                                                  │
│  K("0101010101...01") = O(log n)   [short description]          │
│  K(π to n places)    = O(log n)   [short program]               │
│  K(random n bits)    ≈ n          [no compression possible]     │
└──────────────────────────────────────────────────────────────────┘
```

---

## 1. Formal Definition

Let U be a universal prefix-free TM. The **prefix Kolmogorov complexity** is:

```
K(x) = min{ |p| : U(p) = x }

Prefix-free: no codeword is a prefix of another → Kraft inequality holds
  Σ_x 2^{-K(x)} ≤ 1    (K is a valid code-length function)

Conditional complexity:
  K(x|y) = min{ |p| : U(p, y) = x }    (given y for free)

Joint complexity:
  K(x,y) = min{ |p| : U(p) = (x,y) }
```

**K is not computable**: Given x, no algorithm halts and outputs K(x) for all x.
Proof: If K were computable, enumerate all programs by length; for each string x find its
shortest program. But this process doesn't halt for some x (halting problem).

K is **upper semi-computable**: K(x) ≤ |p| for any program p you can exhibit. The true K(x)
is the infimum, which you can approximate from above but never certify.

---

## 2. Invariance Theorem

```
Theorem (Kolmogorov 1965): For any two universal TMs U, V:
  |K_U(x) - K_V(x)| ≤ c_{UV}     for all strings x

where c_{UV} = |simulation program of V on U|  (a constant)

Proof: To simulate V on U, write a fixed program of constant length c
that first reads a simulation of V, then runs V's program.
  K_U(x) ≤ K_V(x) + c  (simulate V on U)
  K_V(x) ≤ K_U(x) + c' (simulate U on V)
  → |K_U(x) - K_V(x)| ≤ max(c, c')
```

**Why this justifies AIT**: For strings of length n, a constant difference becomes negligible.
The choice of UTM changes K(x) by at most O(1) — independent of x. So statements about
complexity classes, random strings, etc. are universal.

**The additive constant caveat**: For small strings (say |x| < 100 bytes), the constant c_{UV}
dominates. AIT is asymptotic theory. Don't apply K-complexity reasoning to short strings.

---

## 3. Basic Properties

```
Chain rule (exact form):
  K(x,y) = K(x) + K(y|x, K(x)) + O(1)

  [K(x) must be provided along with x to ensure computability of K(y|x,K(x))]

Subadditivity:
  K(x,y) ≤ K(x) + K(y) + O(log(min(K(x),K(y))))

Symmetry of information:
  K(x,y) = K(x) + K(y|x) + O(log K(x,y))

Upper bound:
  K(x) ≤ |x| + O(1)    [identity program: just output x literally]
  K(x) ≤ 2·|x| + O(1)  [non-prefix version; self-delimiting costs at most 2|x|]

With regularity:
  K(xx) ≤ K(x) + O(log K(x))    [concatenation is cheap if K known]
```

**Algorithmic mutual information**:
```
I(x:y) = K(x) + K(y) - K(x,y) + O(log K(x,y))
        = K(x) - K(x|y) + O(log K(x))    [via chain rule]
```
Positive in general but can be negative in individual cases (unlike Shannon mutual information
which is always ≥ 0). Negative I(x:y) means knowing y makes x HARDER to describe.

---

## 4. Incompressibility and Counting

**Counting argument**: There are 2^n binary strings of length n, but only 2^n - 1 programs
of length < n. By pigeonhole, at least one string of length n has K(x) ≥ n.

**Formally**: For any c, |{x : |x| = n, K(x) < n - c}| < 2^{n-c}.
So at least (1 - 2^{-c}) fraction of n-bit strings have K(x) ≥ n - c.

**Incompressibility method** (proof technique): To prove a combinatorial lower bound on
some quantity f(n), assume x is an incompressible string of length n (K(x) ≥ n - c).
If the object in question had a "nice structure", x would have a short description — contradiction.

**Classic application** (merge sort lower bound):
- Assume comparison-based sort can sort any permutation in < n log n comparisons
- An incompressible permutation π can be described by its sorted position + the sequence of
  comparisons. If < n log n comparisons, the description has length < n log n bits
- But K(π) ≥ log(n!) ≈ n log n — contradiction
- Therefore any comparison sort needs ≥ n log n comparisons for some input

---

## 5. Algorithmic Randomness

A string x is **algorithmically random** if K(x) ≥ |x| - O(1). Three equivalent definitions:

```
Definition 1 (Kolmogorov): x is random if K(x) ≥ |x| - c  for small c
  (incompressible: no significantly shorter description exists)

Definition 2 (Martin-Löf): x is random if it passes all effective statistical tests
  Effective test: c.e. set of measure-0 covering sequences
  A sequence fails at most countably many effective tests
  Random ⟺ not in any effective null set

Definition 3 (Schnorr/martingales): x is random if no computable betting strategy
  can win unboundedly on x
  Martingale M(w): M(w) = ½M(w0) + ½M(w1) (fair game)
  Random ⟺ no computable M with M(x₁...xₙ) → ∞

Theorem (Schnorr-Levin): Definitions 1, 2, 3 are equivalent for infinite sequences.
```

**Law of large numbers for random sequences**: If x is Martin-Löf random and drawn from
Bernoulli(p), then the limiting frequency of 1s is exactly p. Randomness implies all
computable statistical regularities hold.

**No finite certificate**: You cannot certify that a finite string is "really random" — you
can only show it has no short description. This is the computability constraint.

---

## 6. Minimum Description Length (MDL)

**MDL principle** (Rissanen 1978, refined by Grünwald): Choose the model M that minimizes
the total description length of model + data given model.

```
Two-part MDL (crude version):
  MDL(M) = K(M) + K(data | M)
           [model code] [data given model]

Choose M* = argmin_M MDL(M)

Example: polynomial regression
  Model M_d = polynomial of degree d
  K(M_d) ≈ d·log(1/ε)  [encoding d coefficients at precision ε]
  K(data|M_d) decreases with d (better fit)
  Optimal d* balances complexity vs fit
```

**Refined MDL (NML — Normalized Maximum Likelihood)**:
```
  p_NML(x^n) = max_θ p(x^n|θ) / Σ_{z^n} max_θ p(z^n|θ)

  MDL_NML = -log p_NML(x^n)
           = -log max_θ p(x^n|θ) + log Σ_{z^n} max_θ p(z^n|θ)
             [regret term = log normalization constant]
```

The NML distribution is the "least committal" distribution that still fits well. The log
normalization constant equals the **stochastic complexity** — the minimum codelength over all
possible data of that length.

**MDL vs Bayesian model selection**:
```
  Bayesian: P(M|data) ∝ P(data|M)·P(M)
  MDL:      MDL(M) ≈ -log P(data|M) + K(M)

  With prior P(M) = 2^{-K(M)}  (universal prior / Solomonoff prior):
  MDL = Bayesian with universal prior

  Solomonoff's universal prior: P(x) = Σ_{p: U(p)=x} 2^{-|p|}
    Assigns higher probability to simpler sequences
    Not normalizable (semimeasure) but works for prediction
```

---

## 7. Logical Depth (Bennett)

Kolmogorov complexity measures information content; logical depth measures computational
content — how hard the string is to compute from its shortest description.

```
Logical depth at significance s:
  d_s(x) = min{ time(U(p)) : U(p) = x, |p| ≤ K(x) + s }

  = time needed by the (s-incompressible) shortest programs for x

Intuition:
  K small + depth small: simple (e.g., "0000...0")
  K large + depth small: random (no structure, computed immediately)
  K small + depth large: complex (e.g., a hard theorem's proof; chess database)
  K large + depth large: doesn't exist (Shannon randomness)
```

**Depth captures "organized complexity"**: Random noise has high K, low depth. Crystal has
low K, low depth. Living organism has low K (specified by genome), high depth (product of
evolution/development — computing the phenotype from the genotype takes a long time).

**Logical depth is not computable**: Even harder than K. You'd need to verify that no shorter
program exists AND measure computation time simultaneously.

**Physical interpretation**: Shannon (bits) = description length. Kolmogorov (bits) = shortest
description. Depth (time steps) = computational work. Bennett argued that physical complexity
(e.g., biological complexity) corresponds to logical depth, not information content.

---

## 8. Thermodynamics of Computation

Landauer's principle connects information erasure to physical entropy:

```
Erasing 1 bit of information ──> minimum entropy increase kT ln 2

Physical reasoning:
  Erasure: 2 distinguishable states → 1 state
  Thermodynamically irreversible (entropy must go somewhere)
  Cost: at least kT ln 2 joules dissipated as heat

At room temperature (T = 300K):
  kT ln 2 ≈ 2.9 × 10⁻²¹ J  per bit erased

Modern CPUs dissipate ~10⁶ × this per operation — still far from Landauer limit
```

**Reversible computation**: Fredkin gate (controlled-SWAP) and Toffoli gate (controlled-CNOT)
are logically reversible — output uniquely determines input. Theoretically can compute without
erasing bits (no thermodynamic cost). Requires storing all intermediate results ("garbage bits").

**Maxwell's demon resolution**: Demon measures molecule velocities (gains info), opens trap
door (does work), violates 2nd law? No — demon must erase its memory to return to initial
state, costing kT ln 2 per bit. Information-theoretic accounting restores 2nd law.

```
┌──────────────────────────────────────────────────────────────┐
│  Maxwell's Demon resolved:                                   │
│                                                              │
│  Gas ──[demon measures]──> Demon memory: {fast, slow, ...}  │
│                                     ↓                        │
│  Demon operates trap door (work extracted from gas)          │
│                                     ↓                        │
│  Demon erases memory to repeat: costs ≥ kT ln 2 per bit     │
│                                     ↓                        │
│  Heat dissipated ≥ work extracted   [2nd law preserved]      │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Bridge to Machine Learning and Statistics

**MDL as theoretical foundation for model selection**:
- Occam's razor formalized: prefer simpler models (smaller K(M))
- BIC (Bayesian Information Criterion) ≈ MDL for regular parametric models
- K(model) ≈ (params/2)·log(n) for d-parameter model → Schwarz criterion

**K-complexity and PAC learning** (Li-Vitányi 1993):
```
For concept class C and sample of size m:
  If H = K(target_concept | domain), then m = O(H/ε·log(1/δ)) samples suffice
  K(c) ≤ VC-dimension(C)·log(n) in most cases
  → Kolmogorov complexity generalizes VC dimension for sample complexity
```

**Shannon entropy as expectation of K-complexity** (on average):
```
Theorem: E_{x ~ p}[K(x|p)] = H(p) + O(1)

Individual strings: K(x) may differ wildly from -log p(x)
Average over distribution: K and Shannon entropy agree up to additive constant

Shannon = ensemble perspective
K = individual string perspective
They agree in expectation, diverge for individual cases
```

---

## Decision Cheat Sheet

| Question | Tool | Notes |
|----------|------|-------|
| Minimum average code length | Shannon entropy H(X) | Distribution must be known |
| Description of individual string | Kolmogorov complexity K(x) | Not computable |
| Model selection criterion | MDL / NML | Computable approximation to K |
| Proving combinatorial lower bound | Incompressibility method | Assume K(x) ≥ n − c |
| Measuring "organized complexity" | Logical depth | Captures computation not just info |
| Thermodynamic cost of computation | Landauer's principle | kT ln 2 per bit erased |
| Prior for universal prediction | Solomonoff prior | Sum over all programs outputting x |
| Algorithmic randomness | Martin-Löf test | Passes all effective statistical tests |

---

## Common Confusion Points

**K is not computable**: You cannot write a program that computes K(x) for all x. The halting
problem directly reduces to K: if K(x) < n, then some short program halts and outputs x.
Enumerating programs of increasing length and waiting for them to halt doesn't terminate.

**Upper bounds vs lower bounds**: Exhibiting a program p with U(p) = x gives K(x) ≤ |p|.
Proving a lower bound K(x) ≥ n-c requires incompressibility argument or counting.
In practice, all known K lower bounds use counting — there's no positive test for randomness.

**K(x) vs -log p(x)**: For a specific string x drawn from distribution p, K(x) and -log p(x)
can differ by any amount. K(x) is about the string itself; -log p(x) is about how probable
it is under p. A very probable string can still have high K (if the distribution has high entropy).

**MDL ≠ MLE**: MLE maximizes likelihood P(data|M) — finds the best parameter setting.
MDL minimizes K(M) + K(data|M) — balances model complexity vs fit. MDL avoids overfitting
by penalizing complex models; MLE does not. MDL ≈ BIC ≈ AIC for large samples, regular models.

**Logical depth not the same as time complexity**: An algorithm's time complexity tells you
how long it runs as a function of input size. Logical depth of a string x is how long the
shortest programs for x take to run. Depth captures how hard x is to generate, not to verify.
