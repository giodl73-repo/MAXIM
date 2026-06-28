---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:inclusion-exclusion
kind: guide
module: combinatorics
section: combinatorics
title: Inclusion-Exclusion and the Sieve
status: source-custody
source_custody: partial
current_path: combinatorics/04-INCLUSION-EXCLUSION.md
canonical_path: combinatorics/04-INCLUSION-EXCLUSION.md
backsource_ids: [proof-backfill:combinatorics:04-inclusion-exclusion, git-history:combinatorics:04-inclusion-exclusion]
concepts: [inclusion-exclusion, derangements, surjections, sieve, bonferroni]
root_concepts: [inclusion-exclusion]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Inclusion–Exclusion and the Sieve

## The Big Picture

```
+============================================================================+
|          INCLUSION-EXCLUSION: OVERCOUNT, THEN CORRECT                      |
+============================================================================+
|                                                                            |
|   |A u B u C| = |A|+|B|+|C|                                                |
|              - |AB|-|AC|-|BC|       add singles, subtract pairs,           |
|              + |ABC|                add triples, alternate...              |
|                                                                            |
|       +-----------+        Venn intuition:  each region must be            |
|      / A   /-------\       counted exactly once. Adding singles            |
|     /     / overlap \      double-counts overlaps; subtracting pairs       |
|    |  +--+----+  C   |     over-subtracts the triple; add it back.         |
|    |  |  | B  |      |                                                     |
|     \ |  +----+-----/                                                      |
|      \+--------+----/                                                      |
|                                                                            |
|   GENERAL FORM (n sets):                                                   |
|   | UNION A_i | = SUM_{S nonempty} (-1)^{|S|+1} | INTERSECT_{i in S} A_i | |
|                                                                            |
|   COMPLEMENT FORM (count elements in NO A_i):                              |
|   | NONE | = SUM_{S} (-1)^{|S|} | A_S |   ,  A_empty = whole universe U    |
|                                                                            |
|         |                  |                   |                           |
|         v                  v                   v                           |
|   DERANGEMENTS        SURJECTIONS         EULER PHI / SIEVE                |
|   D_n = n! SUM        n! S(k,n) =          phi(n)=n PROD(1-1/p)            |
|   (-1)^j / j!         SUM (-1)^j C(n,j)    (number theory link)            |
|                       (n-j)^k                                              |
+============================================================================+
```

Inclusion–exclusion (I-E) is the correction machine of counting: when sets
overlap, you cannot just add. **Add the singletons, subtract the pairwise
overlaps, add back the triples, and alternate.** The complement form — *count the
elements satisfying none of a list of "bad" properties* — is the version you
actually reach for, because most counting problems are "how many avoid all of
these forbidden conditions."

---

## Layer 1 — The Principle, Two Forms

```
   UNION FORM
   | A_1 u ... u A_n | = SUM_{k=1}^{n} (-1)^{k+1}
                          SUM_{|S|=k} | A_{i1} INTERSECT ... INTERSECT A_{ik} |

   COMPLEMENT FORM (more useful)
   Let U = universe, A_i = "elements WITH bad property i".
   # elements with NO bad property =
        SUM_{S subset of [n]} (-1)^{|S|} | A_S |
   where A_S = INTERSECT_{i in S} A_i  and  A_empty = U.
```

**Why the alternating signs work.** Take an element `x` with *exactly* `m` of the
bad properties. Its net contribution to the complement-form sum is
`Σ_{j=0}^{m} (-1)^j C(m,j)`, the number of size-S subsets among its `m`
properties weighted by sign. By the alternating binomial identity (`02`), this is
`0` for `m ≥ 1` and `1` for `m = 0`. So every element with at least one bad
property cancels to zero, and only the "clean" elements survive — exactly what
the complement form claims. The proof *is* the `Σ (-1)^j C(m,j) = [m=0]` identity.

---

## Layer 2 — Derangements (the flagship application)

A **derangement** is a permutation with no fixed point: `π(i) ≠ i` for all `i`.
"How many ways can n hats be returned so nobody gets their own?"

```
   Universe U = all n! permutations.
   Bad property i = "fixes point i" (pi(i) = i).
   A_S = permutations fixing every i in S = (n - |S|)! arrangements
         of the remaining points.  There are C(n,|S|) sets of each size.

   D_n = SUM_{j=0}^{n} (-1)^j C(n,j) (n-j)!
       = n! SUM_{j=0}^{n} (-1)^j / j!
       = n! * [ 1 - 1 + 1/2! - 1/3! + ... ]
       ->  n!/e   as n -> infinity.

   D_0=1, D_1=0, D_2=1, D_3=2, D_4=9, D_5=44, ...
```

The punchline is striking: `D_n / n! → 1/e ≈ 0.3679`. The **probability a random
permutation is a derangement converges to 1/e**, essentially independent of `n`.
There is also a clean recurrence `D_n = (n-1)(D_{n-1} + D_{n-2})`, and the EGF
(`03`) is `e^{-x}/(1-x)` — the `e^{-x}` is the I-E sign-alternation, `1/(1-x)`
the `n!`.

---

## Layer 3 — Counting Surjections

How many functions `f: [k] → [n]` are **onto** (hit every one of the n
codomain elements)?

```
   Universe U = all n^k functions.
   Bad property i = "element i of codomain is MISSED".
   A_S = functions avoiding all i in S = (n - |S|)^k.

   Surj(k,n) = SUM_{j=0}^{n} (-1)^j C(n,j) (n-j)^k.

   This equals  n! * S(k,n)   (Stirling 2nd kind) -- cross-check with
   the twelvefold way (file 01) and special numbers (file 07).
```

**Worked count.** Surjections `[4] → [2]`: `Σ_j (-1)^j C(2,j)(2-j)^4 =
2^4 - 2·1^4 + 0 = 16 - 2 = 14`. Matches `2!·S(4,2) = 2·7 = 14` from `01`.
Two independent methods, same answer — that is how you trust the count.

The same I-E template counts: number of ways to **n-color** so that all n colors
are used; number of **size-n sequences over an n-alphabet using every symbol**;
the **Stirling number** `S(k,n) = (1/n!) Σ_j (-1)^j C(n,j)(n-j)^k`.

---

## Layer 4 — The Sieve and Number-Theoretic I-E

Inclusion–exclusion *is* the abstract sieve; the **sieve of Eratosthenes** and
Euler's totient are its number-theory incarnations (full treatment in
`number-theory/`).

```
   EULER'S TOTIENT phi(n) = # integers in [1,n] coprime to n.
   For n = p1^a1 ... pr^ar, "bad property i" = divisible by p_i.

   phi(n) = SUM_{S subset of {p1..pr}} (-1)^{|S|} * n / (PROD_{p in S} p)
          = n PROD_{i=1}^{r} (1 - 1/p_i).

   Example n = 12 = 2^2 * 3:
   phi(12) = 12 (1 - 1/2)(1 - 1/3) = 12 * 1/2 * 2/3 = 4.
   ({1,5,7,11} -- the four coprime residues.)
```

This is I-E with the universe `{1,...,n}` and bad properties "divisible by
prime `p_i`." The product form `∏(1 - 1/p)` is exactly the alternating sum
factored — multiplicativity of `φ` falls out for free. The general "count
integers up to N divisible by none of a set of primes" is the **Legendre sieve**,
the analytic-number-theory workhorse (`number-theory/07`).

---

## Layer 5 — Bonferroni Bounds (when the full sum is too hard)

Truncating the I-E sum gives rigorous **one-sided bounds** — the Bonferroni
inequalities. Stop after an even number of correction terms and you get an
upper bound on the union; stop after an odd number and a lower bound.

```
   Let T_k = SUM_{|S|=k} |A_S|  (the k-th symmetric sum).

   |UNION A_i|  <=  T_1                     (stop after singletons)
   |UNION A_i|  >=  T_1 - T_2               (stop after pairs)
   |UNION A_i|  <=  T_1 - T_2 + T_3         ...
   partial sums alternately over- and under-estimate, squeezing the
   true value. Crucial when SUM has too many high-order terms to
   evaluate but the first few are computable.
```

Bonferroni bounds are the combinatorial backbone of the **first/second moment
method** (`08-PROBABILISTIC-METHOD.md`): `T_1` is essentially `E[X]` (the first
moment) and `T_2` feeds the second moment. The union bound `Pr[∪A_i] ≤ Σ Pr[A_i]`
is the probabilistic shadow of the first Bonferroni inequality.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| `COUNT(DISTINCT)` over overlapping predicate sets | union form of I-E |
| `WHERE NOT (a OR b OR c)` — rows matching none | complement form |
| De Morgan: `¬(A∨B) = ¬A ∧ ¬B` | "none of the bad" = intersection of complements |
| Bitmask over subsets in a `2^n` loop | the `Σ_{S⊆[n]}` sum literally iterates masks |
| Cache/branch "all-miss" probability | union bound / first Bonferroni |

**CS bridge.** The complement form is exactly the algorithm pattern "iterate over
all `2^n` subsets of forbidden conditions, accumulate with sign" — an `O(2^n)`
DP that is the basis of fast subset-sum, the **Möbius transform over the subset
lattice**, and Bjorklund's inclusion–exclusion algorithm for the Hamiltonian path
/ chromatic polynomial. I-E is not just a proof technique; it is a complexity
class of algorithms.

---

## Decision Cheat Sheet

| I want to count... | Use |
|--------------------|-----|
| `\|A ∪ B ∪ ...\|` with overlaps | Union form |
| Elements satisfying **none** of n conditions | Complement form |
| Permutations with no fixed point | Derangements `D_n = n! Σ (-1)^j/j!` |
| Onto functions `[k]→[n]` | `Σ (-1)^j C(n,j)(n-j)^k = n! S(k,n)` |
| Integers in `[1,n]` coprime to n | Euler totient `n ∏(1-1/p)` |
| Integers divisible by none of given primes | Legendre sieve |
| A bound when full I-E is intractable | Bonferroni inequalities |
| "At least one of the bad events" probability | Union bound (`Σ Pr`) |

---

## Common Confusion Points

### "Union form or complement form?"

Use **complement form** whenever the question is "how many avoid all of these
forbidden things" (derangements, surjections, coprimality) — it is cleaner
because the empty subset gives the whole universe and signs line up as `(-1)^{|S|}`.
Use **union form** when you literally want the size of a union (`|A∪B∪C|`). They
are the same identity (`|none| = |U| - |union|`); pick the phrasing that makes
`A_S` easy to count.

### "I get the wrong sign."

The sign is `(-1)^{|S|}` in the complement form and `(-1)^{|S|+1}` in the union
form. The discrepancy is the leading `|U|` term: complement keeps the empty-set
term `(+|U|)` and subtracts the union; the union form has dropped it. Track which
quantity you are computing and the sign convention follows.

### "The intersections A_S are hard to compute."

I-E only helps when the *intersections* are easier than the union — which is
common because "satisfying several conditions simultaneously" is often very
structured (fixing k points → `(n-k)!`; missing k values → `(n-k)^k`; divisible
by `∏ p_i` → `n/∏p_i`). If the `A_S` are no easier than the target, I-E will not
help; reach for a generating function (`03`) or a bijection instead.

### "Does I-E give 1/e for derangements *exactly*?"

No — `D_n/n! = Σ_{j=0}^n (-1)^j/j!` is the *truncated* exponential series, which
**converges** to `1/e` but equals it only in the limit. For finite `n`, `D_n` is
the nearest integer to `n!/e` (the tail is smaller than `1/(n+1)`). Useful exact
fact: `D_n = round(n!/e)` for all `n ≥ 1`.
