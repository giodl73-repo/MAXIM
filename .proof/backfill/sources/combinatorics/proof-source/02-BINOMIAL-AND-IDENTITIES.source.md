---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-BINOMIAL-AND-IDENTITIES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:binomial-and-identities
kind: guide
module: combinatorics
section: combinatorics
title: Binomial Coefficients and Identities
status: source-custody
source_custody: partial
current_path: combinatorics/02-BINOMIAL-AND-IDENTITIES.md
canonical_path: combinatorics/02-BINOMIAL-AND-IDENTITIES.md
backsource_ids: [proof-backfill:combinatorics:02-binomial-and-identities, git-history:combinatorics:02-binomial-and-identities]
concepts: [binomial coefficients, binomial theorem, pascal triangle, vandermonde, multinomial]
root_concepts: [binomial coefficients]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Binomial Coefficients and Identities

## The Big Picture

```
+===========================================================================+
|             THE BINOMIAL COEFFICIENT C(n,k) AND ITS WEB                   |
+===========================================================================+
|                                                                           |
|   DEFINITION              GENERATING IDENTITY        TRIANGLE             |
|   C(n,k) = n!/k!(n-k)!     (1+x)^n = SUM C(n,k) x^k    Pascal's:          |
|   = # of k-subsets         binomial theorem            C(n,k) =           |
|        |                         |                      C(n-1,k-1)        |
|        |                         |                      + C(n-1,k)        |
|        '--------------------------------------'                           |
|                     |                                                     |
|              CORE IDENTITIES (each has a bijective proof)                 |
|        .------------------------------------------------.                 |
|        | Symmetry      C(n,k) = C(n,n-k)                |                 |
|        | Pascal        C(n,k) = C(n-1,k-1) + C(n-1,k)   |                 |
|        | Absorption    k C(n,k) = n C(n-1,k-1)          |                 |
|        | Vandermonde   SUM C(m,j)C(n,k-j) = C(m+n,k)    |                 |
|        | Hockey stick  SUM_{i<=n} C(i,k) = C(n+1,k+1)   |                 |
|        | Row sum       SUM_k C(n,k) = 2^n               |                 |
|        | Alt. row sum  SUM_k (-1)^k C(n,k) = 0  (n>0)   |                 |
|        '------------------------------------------------'                 |
|                     |                                                     |
|                     v                                                     |
|        MULTINOMIAL  C(n; k1,...,km) = n!/(k1!...km!)                      |
|        (x1+...+xm)^n = SUM multinomial * monomials                        |
+===========================================================================+
```

The binomial coefficient is the most important number in combinatorics. Three
equivalent faces — an algebraic formula, the coefficients of `(1+x)^n`, and the
entries of Pascal's triangle — generate a web of identities, each of which
admits a **bijective or combinatorial proof** (count one set two ways). The
multinomial coefficient is the multivariable lift.

---

## Layer 1 — Three Faces of C(n,k)

```
   ALGEBRAIC                COMBINATORIAL              ALGEBRAIC (series)
   C(n,k) = n!/(k!(n-k)!)   = # of k-subsets of [n]   = [x^k] (1+x)^n
        |                          |                        |
        +--------------------------+------------------------+
                       all three are the SAME number
```

The **combinatorial definition** (number of k-subsets) is primary — it makes
identities *visible*. The factorial formula is for computation. The generating
identity `(1+x)^n = Σ_k C(n,k) x^k` ports every identity into algebra and is the
gateway to `03-GENERATING-FUNCTIONS.md`.

Extend to **real/complex upper index** via the falling-factorial form
`C(α,k) = α(α-1)···(α-k+1)/k!`, valid for any α — this is what powers Newton's
**generalized binomial series** `(1+x)^α = Σ_k C(α,k) x^k` for `|x|<1`, the
source of `(1-x)^{-1} = Σ x^k`, `(1-4x)^{-1/2}` (Catalan), and friends.

---

## Layer 2 — The Binomial Theorem

```
              n
   (x + y)^n = SUM  C(n,k) x^k y^(n-k)
             k=0

   PROOF (combinatorial):  expanding the product of n factors (x+y),
   each term picks x or y from each factor. A term with exactly k
   x's appears once per k-subset of the n factors => C(n,k) copies of
   x^k y^(n-k).  No algebra needed; just the rule of product + counting.
```

This is the prototype of **combinatorial proof**: the coefficient *is* a count.
Set `x = y = 1` to read off `Σ_k C(n,k) = 2^n` (number of subsets of `[n]`); set
`x = 1, y = -1` to read off `Σ_k (-1)^k C(n,k) = 0` for `n>0` (a set has equally
many even- and odd-sized subsets — itself provable by a parity-flipping
bijection: toggle membership of element 1).

| Substitution | Identity | Combinatorial reading |
|--------------|----------|------------------------|
| `x=y=1` | `Σ_k C(n,k) = 2^n` | all subsets of `[n]` |
| `x=1, y=-1` | `Σ_k (-1)^k C(n,k) = 0` (n>0) | even subsets = odd subsets |
| differentiate, `x=1` | `Σ_k k C(n,k) = n 2^{n-1}` | sum of subset sizes |
| `x=2, y=1` | `Σ_k C(n,k) 2^k = 3^n` | functions `[n]→{a,b,c}`-style |

---

## Layer 3 — Pascal's Triangle and the Core Identities

```
   row 0:                1
   row 1:              1   1
   row 2:            1   2   1
   row 3:          1   3   3   1
   row 4:        1   4   6   4   1
   row 5:      1   5  10  10   5   1

   Each entry = sum of the two above it:
       C(n,k) = C(n-1,k-1) + C(n-1,k)          (Pascal's rule)
```

**Pascal's rule, bijectively.** A k-subset of `[n]` either contains element `n`
(then the rest is a (k-1)-subset of `[n-1]`: `C(n-1,k-1)` ways) or it does not
(a k-subset of `[n-1]`: `C(n-1,k)` ways). Disjoint cases, rule of sum. This
"condition on the last element" split is the engine behind most binomial
recurrences.

### The identity catalog

```
+----------------------------------------------------------------------+
|  IDENTITY            STATEMENT                  PROOF IDEA           |
+----------------------------------------------------------------------+
|  Symmetry      C(n,k) = C(n,n-k)               complement the subset |
|  Pascal        C(n,k)=C(n-1,k-1)+C(n-1,k)      condition on elt n    |
|  Absorption    k C(n,k) = n C(n-1,k-1)         pick subset + a       |
|                                                "leader" two ways     |
|  Trinomial     C(n,k)C(k,j)=C(n,j)C(n-j,k-j)   subset-of-subset      |
|  Hockey stick  SUM_{i=k}^n C(i,k)=C(n+1,k+1)   condition on max elt  |
|  Vandermonde   SUM_j C(m,j)C(n,k-j)=C(m+n,k)   split set into m,n    |
|  Row sum       SUM_k C(n,k) = 2^n              all subsets           |
+----------------------------------------------------------------------+
```

### Vandermonde's identity (the most useful)

```
            k
   C(m+n, k) = SUM  C(m, j) C(n, k-j)
           j=0

   PROOF: to choose k people from a room of m women and n men,
   choose j women and k-j men, summed over j. Both sides count the
   same k-subsets of an (m+n)-set.
```

Vandermonde is convolution of binomial rows; in generating-function terms it is
just `(1+x)^m (1+x)^n = (1+x)^{m+n}` read coefficient-by-coefficient (`03`).
Special case `m = n = k`: `Σ_j C(n,j)^2 = C(2n,n)` (use symmetry `C(n,n-j) =
C(n,j)`) — the count of monotone lattice paths and a Catalan-adjacent identity.

### Hockey stick (the "summing a column" identity)

```
   SUM_{i=k}^{n} C(i,k) = C(n+1, k+1)

   PROOF: count (k+1)-subsets of {0,1,...,n} by their LARGEST element i.
   If the max is i, the other k elements are a k-subset of {0,...,i-1}:
   C(i,k) ways.  Sum over i = k..n.
```

This is the discrete analog of `∫ x^k dx = x^{k+1}/(k+1)`, and it is how you
sum a "diagonal" of Pascal's triangle — directly useful for closing recurrences
in `05`.

---

## Layer 4 — Multinomial Coefficients

Generalize from two choices (x or y) to `m` choices.

```
   MULTINOMIAL COEFFICIENT
                    n!
   C(n; k1,...,km)= -----------------   ,   k1 + ... + km = n
                    k1! k2! ... km!

   = # of ways to partition n distinct items into labeled groups
     of sizes k1, k2, ..., km
   = # of distinct arrangements of a multiset with ki copies of symbol i

   MULTINOMIAL THEOREM
   (x1 + ... + xm)^n = SUM_{k1+...+km=n} C(n; k1,...,km) x1^k1 ... xm^km
```

A binomial coefficient is the `m=2` case: `C(n,k) = C(n; k, n-k)`. The number of
*terms* in the expansion is the stars-and-bars count `C(n+m-1, m-1)` (monomials
of degree n in m variables). Iterating Pascal gives a multinomial recurrence;
the cleanest derivation is the nested product `C(n;k1,...,km) = C(n,k1)·C(n-k1,k2)
···` (choose group 1, then group 2 from the rest, ...).

**Worked count.** Distinct arrangements of the letters in BANANA: one B, three
A, two N → `6!/(1!·3!·2!) = 720/12 = 60`. Equivalent to partitioning the 6
positions into labeled blocks of sizes 1, 3, 2.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Counting bit-strings with k ones | `C(n,k)` (k-subsets ↔ bitmasks) |
| `2^n` subsets / full truth table | row sum `Σ_k C(n,k) = 2^n` |
| Polynomial expansion in a CAS | binomial / multinomial theorem |
| Convolution of two distributions | Vandermonde (`(1+x)^m(1+x)^n`) |
| Splitting work into labeled buckets of fixed sizes | multinomial coefficient |
| Anagrams / multiset permutations | `n!/(k_1!...k_m!)` |

**CS bridge — analysis of algorithms.** Binomial coefficients are the
combinatorial backbone of average-case analysis: the number of comparisons,
inversions, or recursion-tree leaves is routinely a binomial sum, and
`Σ_k k C(n,k) = n 2^{n-1}` style identities close those sums. Central binomial
`C(2n,n) ≈ 4^n / √(πn)` (via Stirling) gives the ubiquitous "exponential over
square-root" growth seen in catalan-counted structures and random-walk return
probabilities.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Count k-subsets / bitmasks | `C(n,k) = n!/(k!(n-k)!)` |
| Expand `(x+y)^n` | Binomial theorem |
| Sum a Pascal row | `Σ_k C(n,k) = 2^n` |
| Sum with alternating signs | `Σ_k (-1)^k C(n,k) = 0` (n>0) |
| Split `C(m+n,k)` over two groups | Vandermonde |
| Sum a Pascal column/diagonal | Hockey stick |
| Count multiset arrangements | Multinomial `n!/(k_1!...k_m!)` |
| Expand `(x_1+...+x_m)^n` | Multinomial theorem |
| Handle non-integer exponent | Generalized binomial `(1+x)^α` |
| Prove a binomial identity | Count one set two ways (bijection) |

---

## Common Confusion Points

### "When is an identity easier to prove combinatorially vs algebraically?"

Default to **combinatorial** (count the same thing two ways) — it is shorter and
explains *why*. Reach for algebra (generating functions, induction on Pascal)
when the bijection is non-obvious or the identity involves alternating signs (use
inclusion–exclusion, `04`) or non-integer indices (use the generalized binomial
series). Vandermonde and hockey-stick are textbook combinatorial; the
alternating-sum identities are textbook sign-cancellation.

### "C(n,k) when k > n, or k < 0?"

Both are `0` by the combinatorial definition (no such subsets), and the
factorial formula agrees if you treat `1/(negative)! = 0`. Keeping this
convention lets you write sums `Σ_{k} C(n,k)(...)` without fussing over bounds —
the out-of-range terms vanish.

### "Is Vandermonde the same as the binomial theorem?"

No, but they are siblings. The binomial theorem expands one power; Vandermonde
is what you get from *multiplying two* such expansions and matching coefficients,
`(1+x)^m(1+x)^n = (1+x)^{m+n}`. Most binomial-sum identities are "read off a
product/quotient of `(1+x)^•` factors" — which is precisely the
generating-function viewpoint of `03`.

### "Multinomial coefficient vs choosing groups one at a time — same thing?"

Yes. `C(n; k_1,...,k_m) = C(n,k_1)C(n-k_1,k_2)···C(k_m,k_m)` telescopes to
`n!/(k_1!···k_m!)`. Picking the labeled groups sequentially (product rule) and
the closed multinomial form are the same count; the product form is often easier
to reason about, the closed form easier to compute.
