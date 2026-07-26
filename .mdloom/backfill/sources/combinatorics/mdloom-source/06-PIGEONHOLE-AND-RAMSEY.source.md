---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-PIGEONHOLE-AND-RAMSEY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:pigeonhole-and-ramsey
kind: guide
module: combinatorics
section: combinatorics
title: Pigeonhole and Ramsey Theory
status: source-custody
source_custody: partial
current_path: combinatorics/06-PIGEONHOLE-AND-RAMSEY.md
canonical_path: combinatorics/06-PIGEONHOLE-AND-RAMSEY.md
backsource_ids: [mdloom-backfill:combinatorics:06-pigeonhole-and-ramsey, git-history:combinatorics:06-pigeonhole-and-ramsey]
concepts: [pigeonhole, ramsey numbers, van der waerden, schur, unavoidable structure]
root_concepts: [ramsey theory]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Pigeonhole and Ramsey Theory

## The Big Picture

```
+=============================================================================+
|        UNAVOIDABLE STRUCTURE: "ENOUGH" FORCES ORDER                         |
+=============================================================================+
|                                                                             |
|   PIGEONHOLE                RAMSEY                  RELATIVES               |
|   n+1 items, n boxes        2-color edges of        van der Waerden:        |
|   => some box has >= 2      K_R(s,t); enough        long arithmetic         |
|        |                    => mono K_s or K_t      progressions forced     |
|        v                         |                  Schur: x+y=z mono       |
|   GENERALIZED               R(3,3) = 6              Hales-Jewett: combo     |
|   N items, k boxes          R(4,4) = 18             lines in a cube         |
|   => some box >= ceil(N/k)  R(5,5) in [43,48]            |                  |
|                                  |                       v                  |
|        |                         v                  "Complete disorder      |
|        v                  BOUNDS:                    is impossible"         |
|   PROBABILISTIC           R(s,t) <= C(s+t-2,s-1)    -- T. Motzkin           |
|   pigeonhole:             2^{s/2} < R(s,s) < 4^s                            |
|   E[X] argument           lower via prob. method (file 08)                  |
+=============================================================================+
```

This is the theory of **forced structure**. The pigeonhole principle — `n+1`
pigeons in `n` holes force a shared hole — looks trivial but is the seed of
Ramsey theory, which proves that *any sufficiently large structure, however you
try to disorder it, contains a large ordered substructure.* Frank Ramsey's
theorem and its relatives (van der Waerden, Schur, Hales–Jewett) all say the same
thing: **complete disorder is impossible.** The hard part is the *quantitative*
question — *how large* is "sufficiently large"? — where exact answers are
famously scarce.

---

## Layer 1 — The Pigeonhole Principle

```
   BASIC      If n+1 objects go into n boxes, some box has >= 2.

   GENERAL    If N objects go into k boxes, some box has
              >= ceil(N/k) objects.   (averaging: max >= mean)

   INFINITE   If infinitely many objects go into finitely many
              boxes, some box holds infinitely many.
```

The principle is "the maximum is at least the average" stated for integers. Its
power is entirely in the **clever choice of pigeons and holes** — the technique
is recognizing what to count.

```
+---------------------------------------------------------------+
|  CLASSIC APPLICATIONS (the art is choosing the boxes)         |
|                                                               |
|  * Among 13 people, two share a birth MONTH (12 holes).       |
|  * Any 5 points in a unit square: two within distance         |
|    sqrt2 / 2 (cut square into 4 quadrant holes).              |
|  * Any sequence of n^2+1 distinct reals has a monotone        |
|    subsequence of length n+1 (Erdos-Szekeres; holes = pairs   |
|    (longest incr, longest decr ending here)).                 |
|  * Some consecutive run of days sums to a multiple of n       |
|    (holes = residues of partial sums mod n).                  |
+---------------------------------------------------------------+
```

**Erdős–Szekeres** deserves emphasis: any sequence of `n^2 + 1` distinct reals
contains a monotone subsequence of length `n+1`. Proof by pigeonhole: label each
term with the pair `(i, d)` = (length of longest increasing run ending here,
longest decreasing run ending here). Distinct terms get distinct labels; if all
runs had length `≤ n`, there are only `n^2` labels for `n^2+1` terms — a
collision contradicts distinctness. A two-line proof of a non-obvious theorem,
and a template for "labels as pigeonholes."

---

## Layer 2 — Ramsey's Theorem

```
   THE PARTY THEOREM (R(3,3) = 6):
   Among any 6 people, there are 3 mutual acquaintances OR
   3 mutual strangers. With only 5 people, you can avoid both.

   GRAPH FORM: color every edge of the complete graph K_n red or
   blue. R(s,t) is the least n such that EVERY coloring contains
   a red K_s OR a blue K_t.

   GENERAL RAMSEY: for any number of colors and any target sizes,
   a finite threshold R exists.  (Existence is the theorem;
   computing R is the hard part.)
```

### Proving R(3,3) = 6

```
   UPPER BOUND (<=6): pick any vertex v in K_6. It has 5 edges; by
   pigeonhole >= 3 share a color, say red, to neighbors a,b,c.
   If ANY edge among a,b,c is red -> red triangle (with v).
   If NONE is red -> a,b,c form a blue triangle.  Either way, done.

   LOWER BOUND (>=6): the 2-coloring of K_5 as a red 5-cycle plus
   a blue 5-cycle (the pentagon and pentagram) has NO monochromatic
   triangle. So 5 is not enough.   Hence R(3,3) = 6 exactly.
```

This proof is the whole subject in miniature: **pigeonhole for the upper bound,
an explicit construction for the lower bound.** The gap between these two methods
is why Ramsey numbers are so hard.

---

## Layer 3 — Ramsey Numbers and Their Bounds

```
+------------------------------------------------------------------+
|  KNOWN SMALL RAMSEY NUMBERS (diagonal and off-diagonal)          |
|                                                                  |
|  R(3,3) = 6        R(3,4) = 9        R(3,5) = 14                 |
|  R(4,4) = 18       R(3,6) = 18       R(3,7) = 23                 |
|  R(4,5) = 25       R(5,5) in [43,48] (UNKNOWN!)                  |
|                                                                  |
|  Erdos's famous remark: if aliens demanded R(5,5) we should      |
|  marshal all our computers; if they demanded R(6,6) we should    |
|  attack them first.                                              |
+------------------------------------------------------------------+
```

### The recursive upper bound

```
   R(s,t) <= R(s-1, t) + R(s, t-1).
   With R(s,1)=R(1,t)=1, induction gives the binomial bound:
       R(s,t) <= C(s + t - 2, s - 1).
   Diagonal:  R(s,s) <= C(2s-2, s-1) = O(4^s / sqrt(s)).
```

**Proof of the recursion.** In `K_n` with `n = R(s-1,t)+R(s,t-1)`, fix a vertex
`v` (degree `n-1`). Its red-degree `r` and blue-degree `b` satisfy
`r + b = n-1 = R(s-1,t)+R(s,t-1)-1`, so by pigeonhole either `r ≥ R(s-1,t)` or
`b ≥ R(s,t-1)`. In the first case the red neighborhood forces a red `K_{s-1}`
(which with `v` makes a red `K_s`) or a blue `K_t`; symmetric otherwise.

### The lower bound — the probabilistic method's debut

```
   ERDOS (1947):  R(s,s) > 2^{s/2}.
   MDLOOM (probabilistic method, file 08): randomly 2-color K_n.
   A fixed s-subset is monochromatic with prob 2^{1-C(s,2)}.
   Expected # of mono s-cliques = C(n,s) 2^{1-C(s,2)}.
   If this is < 1, some coloring has ZERO mono cliques, so R(s,s) > n.
   Solving gives n ~ 2^{s/2}.

   Together:   2^{s/2} < R(s,s) < 4^s  (roughly).
```

This is the foundational application of the probabilistic method (`08`): a
*non-constructive* lower bound, still essentially the best known after 75 years —
nobody has explicitly built colorings matching the random one. The exponential
gap between `2^{s/2}` and `4^s` is one of the most famous open problems in
combinatorics.

---

## Layer 4 — Ramsey's Relatives

```
+------------------------------------------------------------------+
|  THEOREM (van der Waerden)                                       |
|  For any r colors and length k, there is W(r,k) such that any    |
|  r-coloring of {1,...,W} contains a monochromatic arithmetic     |
|  progression of length k.   W(2,3) = 9.                          |
|                                                                  |
|  THEOREM (Schur)                                                 |
|  For any r colors there is S(r) such that any r-coloring of      |
|  {1,...,S} has a monochromatic solution to x + y = z.            |
|  (Implies Fermat's equation x^n+y^n=z^n is solvable mod p for    |
|   large p -- a number-theory corollary, see number-theory/.)     |
|                                                                  |
|  THEOREM (Hales-Jewett)                                          |
|  Coloring the cells of a high-dimensional k^n cube forces a      |
|  monochromatic "combinatorial line." The abstract engine         |
|  behind van der Waerden; dimension-free density version is       |
|  the Szemeredi/Furstenberg circle of ideas.                      |
+------------------------------------------------------------------+
```

These share Ramsey's signature — a finite threshold beyond which a monochromatic
target is unavoidable — but in arithmetic settings (progressions, sum equations).
**Schur's theorem** has a clean number-theory payoff: it implies that for every
`n`, the congruence `x^n + y^n ≡ z^n` has nontrivial solutions modulo all
sufficiently large primes (cross-reference `number-theory/`). The growth of these
thresholds (`W(r,k)`, `R(s,t)`) is wildly fast — Ackermann-scale for some — which
is itself a deep combinatorial fact.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Hash collisions: > n keys into n buckets collide | pigeonhole, exactly |
| Birthday paradox / load balancing | generalized + probabilistic pigeonhole |
| "Every large enough input has a worst-case pattern" | Ramsey-style unavoidability |
| Lower bounds by adversary argument | Ramsey lower bound = adversarial coloring |
| Lossless compression can't shrink all inputs | counting pigeonhole (2^n strings, fewer shorter ones) |

**CS bridge.** Pigeonhole is the proof that **no lossless compressor shrinks
every input**: there are `2^n` length-`n` strings but only `2^n - 1` shorter
ones, so some input cannot get a shorter code. Ramsey theory underlies
**communication-complexity and circuit lower bounds** (forcing structure in any
protocol/circuit) and **property testing**. The probabilistic lower bound on
`R(s,s)` is the historical reason the probabilistic method (`08`) entered
mainstream CS — derandomizing such existence proofs is a core theme of
algorithmic combinatorics.

---

## Decision Cheat Sheet

| I want to show... | Use |
|-------------------|-----|
| Two of N items collide in k categories | Pigeonhole (`⌈N/k⌉ ≥ 2`) |
| A monotone subsequence exists | Erdős–Szekeres (`n²+1` ⟹ length `n+1`) |
| 3 mutual friends or strangers | `R(3,3)=6` |
| Mono `K_s` or `K_t` is forced | Ramsey number `R(s,t)`, bound `C(s+t-2,s-1)` |
| A *lower* bound on `R(s,s)` | Probabilistic method (`08`), `2^{s/2}` |
| Mono arithmetic progression | van der Waerden `W(r,k)` |
| Mono solution of `x+y=z` | Schur `S(r)` |
| Compression / counting impossibility | Pigeonhole on `2^n` strings |

---

## Common Confusion Points

### "Ramsey's theorem tells me R(5,5) — so why is it unknown?"

Ramsey's theorem guarantees the number `R(s,t)` *exists and is finite*; it says
nothing about its value. The upper bound `C(2s-2,s-1)` and the probabilistic
lower bound `2^{s/2}` leave an exponential gap, and exact values require
exhaustive (or near-exhaustive) search over colorings — infeasible past `R(4,5)`.
`R(5,5)` is pinned only to `[43,48]`. Existence is easy; the constant is brutal.

### "Pigeonhole feels too obvious to be a real technique."

The principle is trivial; the *modeling* is not. Erdős–Szekeres, the
subsequence-sum-divisible-by-`n` result, and the `R(3,3)` upper bound all hinge
on inventing the right pigeons (labels, partial sums, neighborhoods) and holes
(residues, run-lengths, colors). The difficulty is always "what should I count,
and into what boxes."

### "Is the probabilistic lower bound on R(s,s) constructive?"

No — and that is the point. Erdős's argument proves a good coloring *exists* (the
expected number of monochromatic cliques is `<1`, so some coloring has none) but
exhibits none. Explicitly constructing 2-colorings of `K_n` with no
monochromatic `K_s` for `n` near `2^{s/2}` is a notorious open problem; the best
*explicit* constructions are far weaker than the random bound. This existence-
without-construction gap is the recurring tension of `08`.

### "Van der Waerden vs Szemerédi — same thing?"

Related but distinct. **van der Waerden** is a *coloring* (Ramsey) statement:
*any* `r`-coloring of a long enough interval has a monochromatic length-`k`
progression. **Szemerédi's theorem** is a *density* statement: any subset of the
integers with positive upper density contains arbitrarily long progressions — a
much stronger result (one color class alone suffices if it is dense). Density
versions are deeper and motivated the Hales–Jewett / Furstenberg ergodic program.
