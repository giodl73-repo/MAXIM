---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-GENERATING-FUNCTIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:generating-functions
kind: guide
module: combinatorics
section: combinatorics
title: Generating Functions - Ordinary and Exponential
status: source-custody
source_custody: partial
current_path: combinatorics/03-GENERATING-FUNCTIONS.md
canonical_path: combinatorics/03-GENERATING-FUNCTIONS.md
backsource_ids: [proof-backfill:combinatorics:03-generating-functions, git-history:combinatorics:03-generating-functions]
concepts: [generating functions, ordinary generating function, exponential generating function, recurrences, partitions]
root_concepts: [generating functions]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Generating Functions — Ordinary and Exponential

## The Big Picture

```
+=============================================================================+
|         A GENERATING FUNCTION IS A SEQUENCE WEARING ALGEBRA                 |
+=============================================================================+
|                                                                             |
|   SEQUENCE  a0, a1, a2, ...                                                 |
|        |                                                                    |
|        .----------------------------+----------------------------.          |
|        |                            |                            |          |
|        v                            v                            v          |
|   ORDINARY (OGF)              EXPONENTIAL (EGF)            DIRICHLET        |
|   A(x)=SUM a_n x^n            E(x)=SUM a_n x^n/n!          SUM a_n / n^s    |
|   unlabelled structures       labelled structures         multiplicative    |
|   (subsets, partitions,       (permutations, set          (number theory,   |
|    integer compositions)       partitions, surjections)    see number-th.)  |
|        |                            |                                       |
|        v                            v                                       |
|   SEQUENCE OPS  <-->  ALGEBRA OPS                                           |
|     shift  ........ multiply by x / x^k                                     |
|     a_{n}->a_{n+1}.. (A(x)-a0)/x                                            |
|     CONVOLVE ...... MULTIPLY series   (product rule!)                       |
|     partial sums .. divide by (1-x)                                         |
|     weight by n ... x d/dx                                                  |
|        |                                                                    |
|        v                                                                    |
|   SOLVE RECURRENCE: turn recurrence -> functional equation -> A(x) ->       |
|   extract [x^n] A(x) by partial fractions / known series.                   |
+=============================================================================+
```

A generating function is a **clothesline** (Herbert Wilf's image): you hang the
sequence `a_n` on the powers of `x` and manipulate the whole thing as one
algebraic object. The single most important fact: **convolution of sequences is
multiplication of series.** Because "combine two independent structures" is the
product rule, *combinatorial composition becomes polynomial multiplication.* That
is the entire reason generating functions work.

---

## Layer 1 — OGF vs EGF: Which to Use

```
+---------------------------------------------------------------+
|  ORDINARY (OGF):   A(x) = SUM_{n>=0} a_n x^n                  |
|    Use when objects are UNLABELLED — order/identity of the    |
|    n "slots" does not matter beyond their count.              |
|    Multiplication = "pick a structure of size j AND one of    |
|    size n-j", combined by concatenation.                      |
|      A(x) B(x):  [x^n] = SUM_j a_j b_{n-j}   (Cauchy product) |
|                                                               |
|  EXPONENTIAL (EGF): E(x) = SUM_{n>=0} a_n x^n / n!            |
|    Use when objects are LABELLED — the n elements are         |
|    distinct and a combination must choose WHICH labels go     |
|    to which part.                                             |
|      E(x) F(x):  [x^n/n!] = SUM_j C(n,j) a_j b_{n-j}          |
|                  (binomial convolution — note the C(n,j)!)    |
+---------------------------------------------------------------+
```

The dividing line is **labels**. Integer partitions, compositions, subsets-by-
size: unlabelled → OGF. Permutations, set partitions, labelled trees,
surjections: labelled → EGF. The EGF's `1/n!` exactly absorbs the `C(n,j)` that
appears when you split `n` distinct labels between two structures — this is why
the EGF product rule carries that binomial coefficient.

| Quantity | OGF | EGF |
|----------|-----|-----|
| `a_n = 1` | `1/(1-x)` | `e^x` |
| `a_n = n!` | `Σ n! x^n` (divergent, formal) | `1/(1-x)` |
| `a_n = C(m,n)` | `(1+x)^m` | — |
| `a_n = 2^n` | `1/(1-2x)` | `e^{2x}` |
| product means | concatenate (Cauchy) | label-split (binomial) |

---

## Layer 2 — The Operations Dictionary (OGF)

Master this table and most recurrences solve themselves. Let `A(x) = Σ a_n x^n`.

```
+----------------------------------------------------------------------+
|  SEQUENCE OPERATION              SERIES OPERATION                    |
+----------------------------------------------------------------------+
|  a_n  (baseline)                 A(x)                                |
|  scale  c a_n                    c A(x)                              |
|  shift right (prepend k zeros)   x^k A(x)                            |
|  shift left  a_{n+1}             (A(x) - a_0)/x                      |
|  a_{n-1} convolved with b        A(x) B(x)                           |
|  partial sums  s_n=SUM_{i<=n}a_i A(x)/(1-x)                          |
|  weight  n a_n                   x A'(x)                             |
|  alternate signs  (-1)^n a_n     A(-x)                               |
|  binomial transform SUM C(n,k)a_k (1/(1-x)) A(x/(1-x))               |
+----------------------------------------------------------------------+
```

Three series you must know cold:

```
   1/(1-x)      = 1 + x + x^2 + ...        (a_n = 1)
   1/(1-x)^2    = 1 + 2x + 3x^2 + ...      (a_n = n+1)
   1/(1-x)^{k}  = SUM_n C(n+k-1, k-1) x^n  (multiset / stars-and-bars)
   1/(1-ax)     = SUM_n a^n x^n            (geometric, a_n = a^n)
```

The last general fact — `[x^n] 1/(1-x)^k = C(n+k-1, k-1)` — is **stars and bars
in disguise** (`01`): the coefficient counts ways to write `n` as an ordered sum
of `k` nonnegative parts. Generating functions and elementary counting agree.

---

## Layer 3 — Solving a Recurrence (the canonical workflow)

Take the Fibonacci recurrence `f_n = f_{n-1} + f_{n-2}`, `f_0=0`, `f_1=1`.

```
   STEP 1  Define F(x) = SUM_{n>=0} f_n x^n.

   STEP 2  Multiply the recurrence by x^n and sum over n>=2:
           SUM f_n x^n = SUM f_{n-1} x^n + SUM f_{n-2} x^n
           F(x) - f_0 - f_1 x  =  x(F(x) - f_0)  +  x^2 F(x)
           F(x) - x            =  x F(x) + x^2 F(x)

   STEP 3  Solve the FUNCTIONAL EQUATION for F(x):
           F(x) (1 - x - x^2) = x
           F(x) = x / (1 - x - x^2)

   STEP 4  PARTIAL FRACTIONS. Roots of 1 - x - x^2: x = 1/phi, 1/psi
           where phi=(1+sqrt5)/2, psi=(1-sqrt5)/2. Decompose:
           F(x) = (1/sqrt5) [ 1/(1-phi x) - 1/(1-psi x) ]

   STEP 5  EXTRACT [x^n] using 1/(1-a x) = SUM a^n x^n:
           f_n = (phi^n - psi^n)/sqrt5      <-- Binet's formula.
```

The four-step rhythm — **define, multiply-and-sum, solve, extract** — handles
any linear recurrence with constant coefficients, and many with polynomial
coefficients. The closed form falls out of partial fractions because the
denominator factors over the roots of the **characteristic polynomial** (the same
object you meet in `05-RECURRENCES.md`, approached there without series).

### The Catalan recurrence via OGF

The Catalan numbers satisfy `C_{n+1} = Σ_{i=0}^{n} C_i C_{n-i}` — a *convolution*,
the signature of OGF multiplication.

```
   C(x) = SUM C_n x^n,   C_0 = 1.
   The convolution recurrence => C(x) = 1 + x C(x)^2.
   Quadratic in C(x):   x C^2 - C + 1 = 0
   C(x) = (1 - sqrt(1 - 4x)) / (2x)    (choose root finite at x=0)
   Generalized binomial on sqrt(1-4x) =>  C_n = (1/(n+1)) C(2n, n).
```

That a *quadratic* functional equation appears is the algebraic fingerprint of
Catalan-counted structures (binary trees, balanced parentheses, triangulations);
see `07-SPECIAL-NUMBERS.md`.

---

## Layer 4 — Partitions: Products of Geometric Series

Generating functions shine where no simple recurrence exists. The number `p(n)`
of **integer partitions** of `n` (unordered sums) has the OGF

```
                 oo
   SUM p(n) x^n = PROD   1/(1 - x^k)
   n>=0          k=1

   READ THE PRODUCT:  factor k contributes 1 + x^k + x^{2k} + ...
   = "use part k zero, one, two, ... times".  Multiplying over all
   k assembles every partition exactly once.  Each x^n coefficient
   counts partitions of n.
```

This single product encodes a sequence with no elementary closed form (Hardy–
Ramanujan: `p(n) ~ exp(π√(2n/3))/(4n√3)`). Restricting the product proves
identities for free:

| Restriction on parts | OGF factor included | Result |
|-----------------------|---------------------|--------|
| distinct parts | `∏_k (1 + x^k)` | distinct-part partitions |
| odd parts only | `∏_{k odd} 1/(1-x^k)` | Euler: distinct = odd parts |
| parts ≤ m | `∏_{k=1}^m 1/(1-x^k)` | partitions into parts ≤ m |

**Euler's theorem** (`#partitions into distinct parts` = `#partitions into odd
parts`) drops out by the algebraic identity `∏(1+x^k) = ∏ (1-x^{2k})/(1-x^k) =
∏_{k odd} 1/(1-x^k)`. An algebraic one-liner that is a genuinely surprising
combinatorial fact — the paradigm case for "let the generating function do the
proof." Cross-reference `number-theory/` (partitions, modular forms) and `07`.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Z-transform / generating polynomial of a signal | OGF (`Σ a_n x^n`, signal-processing dual) |
| Laplace / characteristic-function of a distribution | EGF / moment generating function |
| Convolution in DSP / probability | series multiplication `A(x)B(x)` |
| Solving a linear recurrence by characteristic roots | partial fractions of the OGF denominator |
| Polynomial multiply = FFT | Cauchy product is exactly that |

**CS bridge.** The OGF is the formal-power-series cousin of the **probability
generating function** and **moment generating function** (`probability-statistics/`):
products of PGFs count independent sums, exactly as products of OGFs count
independent combinatorial composition. Average-case algorithm analysis (Sedgewick–
Flajolet "Analytic Combinatorics") is built on extracting `[x^n]` asymptotics from
generating functions via singularity analysis — the radius/type of the nearest
singularity dictates the growth rate of the count.

---

## Decision Cheat Sheet

| Situation | Use | Why |
|-----------|-----|-----|
| Unlabelled objects, count by size | OGF | concatenation = Cauchy product |
| Labelled objects (distinct elements) | EGF | label-split = binomial convolution |
| Recurrence with a *convolution* term | OGF, expect a functional equation | convolution ↔ product |
| Linear recurrence, constant coeffs | OGF + partial fractions | roots of char. poly |
| Counting integer partitions | OGF as `∏ 1/(1-x^k)` | each factor = a part's multiplicity |
| Counting set partitions / permutations | EGF | objects are labelled |
| Need asymptotics of `a_n` | singularity analysis of the GF | growth ↔ nearest singularity |
| Need partial sums `Σ_{i≤n} a_i` | multiply OGF by `1/(1-x)` | summation operator |

---

## Common Confusion Points

### "Does the series have to converge?"

No. Generating functions are **formal power series** — `x` is an indeterminate,
not a number. `Σ n! x^n` has radius of convergence 0 yet is a perfectly valid
formal OGF; coefficient extraction is purely algebraic. Convergence matters only
when you later do **analytic** combinatorics (asymptotics via singularities),
where you treat `x` as complex.

### "OGF or EGF — I keep picking wrong."

Ask: *are the n elements distinguishable?* If swapping two elements gives a
genuinely different object (people, labelled vertices, positions in a permutation)
→ **EGF**. If only the *count* of each kind matters (an integer partition, a
multiset, a shape) → **OGF**. The `1/n!` in the EGF is precisely there to manage
the labels; if there are no labels, you do not want it.

### "Why does multiplying generating functions correspond to combining structures?"

Because `[x^n] A(x)B(x) = Σ_j a_j b_{n-j}` is the rule of product summed over the
size split: "make a combined object of size n by choosing a piece of size j from
A and a piece of size n−j from B." For EGFs the split additionally distributes
*labels*, hence the `C(n,j)`. Series multiplication *is* the product rule made
algebraic — the rest is bookkeeping.

### "I solved for A(x) — now how do I get a_n?"

Three routes: (1) recognize `A(x)` as a known series (geometric, binomial,
`e^x`); (2) **partial fractions** if `A(x)` is rational — each `1/(1-α x)^k`
term contributes `C(n+k-1,k-1) α^n`; (3) the **generalized binomial series** if a
root like `(1-4x)^{1/2}` appears (Catalan). If none apply in closed form, extract
*asymptotics* from the dominant singularity rather than an exact formula.
