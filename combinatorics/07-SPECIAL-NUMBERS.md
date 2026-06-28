---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:special-numbers
kind: guide
module: combinatorics
section: combinatorics
title: Special Counting Numbers
status: source-custody
source_custody: partial
current_path: combinatorics/07-SPECIAL-NUMBERS.md
canonical_path: combinatorics/07-SPECIAL-NUMBERS.md
backsource_ids: [proof-backfill:combinatorics:07-special-numbers, git-history:combinatorics:07-special-numbers]
concepts: [catalan numbers, stirling numbers, bell numbers, eulerian numbers, integer partitions]
root_concepts: [special numbers]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Special Counting Numbers

## The Big Picture

```
+============================================================================+
|        THE NAMED SEQUENCES OF COMBINATORICS                                |
+============================================================================+
|                                                                            |
|   CATALAN C_n          STIRLING 2nd S(n,k)     STIRLING 1st c(n,k)         |
|   binary trees,        set partitions into     permutations with           |
|   balanced parens,     k nonempty blocks       k cycles                    |
|   Dyck paths,                |                       |                     |
|   triangulations       BELL B_n = SUM_k S(n,k) (signed: x^n falling)       |
|   C_n=C(2n,n)/(n+1)    all set partitions                                  |
|        |                     |                                             |
|        |               EULERIAN A(n,k)         INTEGER PARTITIONS p(n)     |
|        |               permutations with        unordered sums;            |
|        |               k ascents/descents        OGF = PROD 1/(1-x^k)      |
|        '---------------------+----------------------'                      |
|                              |                                             |
|                   each has: a COMBINATORIAL MODEL, a RECURRENCE,           |
|                   a GENERATING FUNCTION, and BIJECTIONS to one another.    |
+============================================================================+
```

Certain sequences appear so often that they are named. Each is defined by *what
it counts*, tied to its neighbors by **bijections and triangular recurrences**,
and packaged by a generating function (`03`). Knowing these — Catalan, the two
kinds of Stirling, Bell, Eulerian, and the partition numbers — lets you recognize
a count on sight rather than re-deriving it.

---

## Layer 1 — Catalan Numbers

```
   C_n = (1/(n+1)) C(2n, n) = C(2n,n) - C(2n,n+1).
   C_0..C_8 :  1, 1, 2, 5, 14, 42, 132, 429, 1430.
   Recurrence:  C_{n+1} = SUM_{i=0}^{n} C_i C_{n-i}   (convolution, file 05)
   GF:          C(x) = (1 - sqrt(1-4x))/(2x),  C(x)=1+xC(x)^2  (file 03)
   Asymptotics: C_n ~ 4^n / (n^{3/2} sqrt(pi)).
```

The Catalan numbers are the most ubiquitous "non-trivial" sequence. Dozens of
combinatorial families are counted by `C_n` — and the *bijections* between them
are the real content.

```
+---------------------------------------------------------------------+
|  C_n COUNTS (all bijective to each other):                          |
|                                                                     |
|  * binary trees with n internal nodes                               |
|  * triangulations of a convex (n+2)-gon                             |
|  * balanced strings of n pairs of parentheses                       |
|  * monotone lattice paths from (0,0) to (n,n) staying on/below      |
|    the diagonal (Dyck paths)                                        |
|  * ways to multiply n+1 factors (associativity bracketings)         |
|  * non-crossing partitions of {1,...,n}                             |
+---------------------------------------------------------------------+
```

### The Cycle Lemma (a clean closed-form proof)

```
   Among the C(2n,n) lattice paths with n up-steps and n down-steps,
   exactly 1/(n+1) of them never go below the start (a "good" Dyck
   path). DVORETZKY-MOTZKIN cycle lemma: of the 2n+1 cyclic rotations
   of any sequence of n up + (n+1) down steps, EXACTLY ONE is a "good"
   path prefix.  => good paths = (1/(2n+1)) C(2n+1, n) = C_n.
```

The factor `1/(n+1)` is *not* an accident of algebra — the cycle lemma explains
it bijectively. This is the difference between knowing `C_n = C(2n,n)/(n+1)` and
understanding *why* the denominator is there.

---

## Layer 2 — Stirling Numbers (Two Kinds)

```
   SECOND KIND  S(n,k) = # ways to partition an n-SET into k nonempty
                          unlabeled BLOCKS.
       Recurrence:  S(n,k) = k S(n-1,k) + S(n-1,k-1).
       (element n: drop into one of k existing blocks, OR start a new
        block by itself.)
       Closed form (file 04):  S(n,k) = (1/k!) SUM_j (-1)^j C(k,j)(k-j)^n.

   FIRST KIND   c(n,k) = # permutations of [n] with exactly k CYCLES
                          (unsigned / "cycle" Stirling numbers).
       Recurrence:  c(n,k) = (n-1) c(n-1,k) + c(n-1,k-1).
       (element n: insert into an existing cycle in n-1 ways, OR form
        its own fixed-point cycle.)
```

The two kinds are **inverse** as change-of-basis matrices between the ordinary
powers `x^n` and the falling factorials `x^{(n)} = x(x-1)...(x-n+1)`:

```
   x^n          = SUM_k S(n,k) * x^{(k)}        (powers -> falling factorials)
   x^{(n)}      = SUM_k s(n,k) * x^k            (falling factorials -> powers)
   where s(n,k) = (-1)^{n-k} c(n,k)  (SIGNED first-kind Stirling).
```

This duality — second kind expands ordinary powers into falling factorials,
signed first kind inverts it — is why both are called "Stirling numbers." It also
explains the surjection formula `Surj(n,k) = k! S(n,k)` (`01`, `04`): labeling
the `k` blocks costs `k!`.

| n\k | S(n,1) | S(n,2) | S(n,3) | S(n,4) |
|-----|--------|--------|--------|--------|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 1 | 3 | 1 | 0 |
| 4 | 1 | 7 | 6 | 1 |

---

## Layer 3 — Bell Numbers

```
   B_n = total # of partitions of an n-set = SUM_{k=0}^{n} S(n,k).
   B_0..B_6 :  1, 1, 2, 5, 15, 52, 203.

   RECURRENCE (condition on the block containing element n+1):
       B_{n+1} = SUM_{k=0}^{n} C(n,k) B_k.
       (choose the k elements joining n+1's block from the other n;
        partition the remaining n-k arbitrarily.)

   EGF (labelled objects, file 03):   SUM B_n x^n/n! = exp(e^x - 1).
       (the "set of nonempty sets" species; e^x - 1 is one nonempty
        block, exp of it assembles a set of blocks.)
```

The EGF `e^{e^x - 1}` is a perfect illustration of the **exponential formula**:
"a structure = a set of connected components" becomes `EGF = exp(component EGF)`.
Here a component is a nonempty block (`e^x - 1`). Bell numbers also satisfy
**Dobiński's formula** `B_n = (1/e) Σ_{k≥0} k^n / k!` — a probabilistic identity
(the `n`-th moment of a Poisson(1) variable), bridging to
`probability-statistics/`.

---

## Layer 4 — Eulerian Numbers

```
   A(n,k) = # permutations of [n] with exactly k ASCENTS
            (positions i where pi(i) < pi(i+1)).
   Recurrence:  A(n,k) = (k+1) A(n-1,k) + (n-k) A(n-1,k-1).
   Symmetry:    A(n,k) = A(n, n-1-k)   (reverse the permutation).
   Row sum:     SUM_k A(n,k) = n!      (every permutation has some
                                        ascent count).

   WORPITZKY IDENTITY (ties Eulerian numbers to powers):
       x^n = SUM_k A(n,k) C(x + k, n).
```

Eulerian numbers are the "descent statistic" of permutations. They appear in the
**Worpitzky identity** above (yet another expansion of `x^n`, parallel to the
Stirling one), and in summing `Σ_{i=1}^{m} i^n` in closed form. They are distinct
from Euler's *numbers* (secant/tangent) and from the totient `φ` — a common name
collision.

---

## Layer 5 — Integer Partitions

```
   p(n) = # of ways to write n as an UNORDERED sum of positive integers.
   p(1)..p(8) :  1, 2, 3, 5, 7, 11, 15, 22.   (no elementary closed form)

   GF (file 03):   SUM p(n) x^n = PROD_{k>=1} 1/(1 - x^k).
   Asymptotics (Hardy-Ramanujan):  p(n) ~ exp(pi sqrt(2n/3)) / (4 n sqrt3).

   FERRERS / YOUNG DIAGRAM: a partition drawn as left-justified rows
   of boxes. Transposing (rows <-> columns) is the CONJUGATE partition.
       4+2+1 :   # # # #            conjugate:  # # #
                 # #                            # #
                 #                              #
                                                #
   => # partitions of n with largest part = k  EQUALS
      # partitions of n into exactly k parts.   (conjugation bijection)
```

Partitions are where bijective combinatorics meets `number-theory/` (the
partition function's congruences, e.g. Ramanujan's `p(5n+4) ≡ 0 mod 5`). The
**conjugation** (transpose the Ferrers diagram) and **Euler's distinct=odd**
identity (`03`) are the canonical partition bijections.

---

## How They Relate

```
                        SET PARTITIONS
                       (Stirling 2nd S(n,k))
                              |  sum over k
                              v
                          BELL B_n
                              |  EGF = exp(e^x - 1)
   PERMUTATIONS  --cycles-->  STIRLING 1st c(n,k)   --ascents-->  EULERIAN
        |  (n! of them)                                              |
        |                                                            |
        v                                                            v
   FALLING FACTORIAL  <----- both Stirling kinds are the ----->  expansions
   x^{(n)} <-> x^n           change-of-basis between these         of x^n

   CATALAN: a SEPARATE world (Dyck/tree structures), its own
   quadratic GF; not a Stirling/Bell relative but equally ubiquitous.

   PARTITIONS (integer): the "erase all labels" endpoint; OGF, not EGF.
```

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| # of distinct binary-tree shapes / parse trees | Catalan `C_n` |
| # of ways to fully-parenthesize a chain product | Catalan (matrix-chain DP states) |
| # of GROUP BY partitions of n rows | Bell `B_n` / Stirling 2nd |
| # of ways to assign tasks to k nonempty teams | `k! S(n,k)` (labeled) or `S(n,k)` |
| Cycle structure of a random permutation | Stirling 1st `c(n,k)` |
| Sorting-network / inversion statistics | Eulerian numbers (descents) |

**CS bridge.** Catalan numbers count the states of the classic matrix-chain and
optimal-BST dynamic programs, and the shapes of parse/expression trees — their
`4^n` growth is why naive enumeration of bracketings is intractable and DP is
required. Stirling 2nd counts `GROUP BY` outcomes / clusterings; Bell counts all
of them. The exponential formula `EGF = exp(component EGF)` is the combinatorial
core of "labelled structure = set of connected pieces" used throughout analytic
combinatorics for average-case analysis.

---

## Decision Cheat Sheet

| I am counting... | Number | Formula / GF |
|------------------|--------|--------------|
| Binary trees / balanced parens / Dyck paths | Catalan `C_n` | `C(2n,n)/(n+1)` |
| Triangulations of an (n+2)-gon | Catalan `C_n` | same |
| Set partitions into exactly `k` blocks | Stirling 2nd `S(n,k)` | `S=kS+S` recurrence |
| Onto functions `[n]→[k]` | `k! S(n,k)` | I-E (`04`) |
| All set partitions of `[n]` | Bell `B_n` | EGF `e^{e^x-1}` |
| Permutations with `k` cycles | Stirling 1st `c(n,k)` | `(n-1)c+c` recurrence |
| Permutations with `k` ascents | Eulerian `A(n,k)` | `(k+1)A+(n-k)A` |
| Unordered integer sums | partitions `p(n)` | OGF `∏ 1/(1-x^k)` |

---

## Common Confusion Points

### "Stirling first kind vs second kind — which is which?"

**Second kind `S(n,k)`** partitions a *set* into `k` blocks (think: clustering,
GROUP BY). **First kind `c(n,k)`** counts permutations with `k` *cycles* (think:
cycle structure). Mnemonic: "second = sets, first = cycles." They are inverse
change-of-basis matrices between `x^n` and the falling factorial, which is why
they travel together. The *signed* first kind `s(n,k) = (-1)^{n-k}c(n,k)` is what
inverts the second kind.

### "Set partitions vs integer partitions?"

A **set partition** splits a labeled set `{a,b,c}` into blocks — `{a,b}{c}` and
`{a,c}{b}` are different (counted by Bell/Stirling 2nd). An **integer partition**
splits a *number* `n` into unordered parts — only the multiset of sizes matters
(`p(n)`, OGF `∏1/(1-x^k)`). Labels distinguish them: set partitions are
*labelled* (EGF), integer partitions *unlabelled* (OGF).

### "Why is the Catalan denominator `n+1`?"

The cycle lemma: among all `C(2n,n)` paths with `n` up and `n` down steps,
exactly the fraction `1/(n+1)` stay weakly below the diagonal (equivalently, of
the `2n+1` cyclic rotations of an `n`-up/`(n+1)`-down sequence, exactly one is a
valid Dyck prefix). The `1/(n+1)` is a genuine bijective fact, not a normalizing
fudge — it is the reflection/cycle structure of lattice paths.

### "Are Catalan numbers a Stirling/Bell relative?"

No. Bell, Stirling, and Eulerian numbers all describe *set partitions and
permutation statistics* and share the falling-factorial / exponential-formula
algebra. Catalan numbers describe *tree and lattice-path* structures and satisfy
a **quadratic** generating-function equation (`C = 1 + xC^2`), a different
algebraic world. They are equally ubiquitous but unrelated by the
change-of-basis story — do not expect a Stirling-style recurrence for `C_n`.
