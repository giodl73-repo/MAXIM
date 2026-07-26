---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-ANALYSIS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:analysis
kind: guide
module: algorithms
section: mathematics-physics
title: Algorithm Analysis - Asymptotics, Recurrences, Amortized
status: source-custody
source_custody: partial
current_path: algorithms/01-ANALYSIS.md
canonical_path: algorithms/01-ANALYSIS.md
backsource_ids: [mdloom-backfill:algorithms:01-analysis, git-history:algorithms:01-analysis]
concepts: [asymptotic analysis, recurrences, master theorem, amortized analysis, average-case, potential method]
root_concepts: [algorithm analysis]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Algorithm Analysis — Asymptotics, Recurrences, Amortized

You know what O, Ω, Θ mean. This guide is about the *machinery that produces
bounds*: how to solve the recurrences divide-and-conquer generates, how to charge
costs across a sequence of operations (amortized), how to reason about a random
input (average-case), and exactly where each of those four worlds differs. Getting
these distinctions exactly right is what separates a correct complexity claim from
a plausible-sounding wrong one.

```
  THE FOUR ANALYSIS WORLDS — pick the right one, they answer different questions
  ==================================================================================

   WORST-CASE             AVERAGE-CASE            AMORTIZED              SMOOTHED
   ----------             ------------            ---------             --------
   adversary picks        random input,           ANY op sequence,      random PERTURBATION
   the single worst       expectation over        total cost / #ops     of an adversarial
   input                  a distribution                                input
        |                      |                       |                     |
        v                      v                       v                     v
   "guaranteed ceiling"   "typical run"          "contract over a      "why simplex is
                          (can be unlucky)        sequence, no luck"     fast in practice"

   quicksort O(n^2)       quicksort O(n log n)   array push O(1)        simplex poly
                          (random pivot)          amortized             (Spielman-Teng)

   T E C H N I Q U E S
   -------------------
   recurrences:           indicator RVs +        aggregate /            (research-level;
   - recursion tree       linearity of           accounting /            noted for context)
   - Master theorem       expectation            potential method
   - Akra-Bazzi
   - substitution
```

**The whole guide in one sentence**: choose the analysis world that matches the
guarantee you actually need, then use the technique in its column.

---

## Layer 1: Asymptotic Notation, Used Precisely

A one-screen refresher only to fix *usage*, since the common errors are about
which symbol to use, not what they mean.

```
  f = O(g)    f grows AT MOST as fast as g     (upper bound; "<=")
  f = Omega(g) f grows AT LEAST as fast as g   (lower bound; ">=")
  f = Theta(g) f and g grow at the SAME rate   (tight; "=")
  f = o(g)    f grows STRICTLY slower          (strict "<")
  f = omega(g) f grows STRICTLY faster         (strict ">")
```

Two usage rules that catch real mistakes:

- **A lower bound on a *problem* is Ω; an upper bound from an *algorithm* is O.**
  "Comparison sorting is Ω(n log n)" is a statement about the problem (no algorithm
  can beat it). "Mergesort is O(n log n)" is about an algorithm. When both meet,
  the problem is Θ(n log n) *in that model*.
- **O(n²) does not mean "quadratic."** It means "no worse than quadratic." An O(n²)
  algorithm might run in linear time on your inputs. Use Θ when you mean tight.

```
  Common growth ladder (each dominates the one below for large n):

    n!  >  2^n  >  n^3  >  n^2  >  n log n  >  n  >  sqrt(n)  >  log n  >  1
    ^^^^^^^^^^^^         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    intractable          the "efficient" zone (polynomial) -- see 09
```

---

## Layer 2: Solving Recurrences

Divide-and-conquer (`03`) produces recurrences of the form `T(n) = a·T(n/b) + f(n)`:
`a` subproblems, each of size `n/b`, plus `f(n)` to split and combine. Three tools
solve essentially all of them.

### Tool 1: The Recursion Tree (always works, builds intuition)

Expand the recurrence into a tree; sum the work per level.

```
   T(n) = 2 T(n/2) + n          (mergesort)

   level 0:                 n                       work = n
                          /     \
   level 1:          n/2         n/2                work = n
                    /   \       /   \
   level 2:      n/4   n/4   n/4   n/4              work = n
                  ...                               ...
   level log2(n): 1 1 1 ... 1   (n leaves)          work = n

   #levels = log2(n) + 1 , each level does n work
   => T(n) = n * (log2 n + 1) = Theta(n log n)
```

```
   T(n) = 2 T(n/2) + 1          (e.g. tree size)

   per-level work: 1, 2, 4, ..., n   (DOUBLES each level — leaf-dominated)
   total = 1 + 2 + 4 + ... + n = 2n - 1 = Theta(n)
   => the LEAVES dominate, not the levels
```

### Tool 2: The Master Theorem (the fast path for `aT(n/b)+f(n)`)

Compare `f(n)` against `n^(log_b a)` — the "watershed" exponent, which is just the
number of leaves `n^(log_b a)`.

```
  Let c_crit = log_b(a).   Compare f(n) to n^c_crit:

  CASE 1  f(n) = O(n^(c_crit - eps))     leaves win    => T(n) = Theta(n^c_crit)
  CASE 2  f(n) = Theta(n^c_crit log^k n) balanced      => T(n) = Theta(n^c_crit log^(k+1) n)
  CASE 3  f(n) = Omega(n^(c_crit + eps)) root wins*     => T(n) = Theta(f(n))
          (*plus a regularity condition: a f(n/b) <= c f(n), c<1)
```

Worked examples (verify each against the cases):

```
  T = 2T(n/2) + n        a=2,b=2 -> c_crit=1, f=n=n^1   CASE 2 (k=0) -> Theta(n log n)   [mergesort]
  T = 2T(n/2) + 1        a=2,b=2 -> c_crit=1, f=1<n^1   CASE 1       -> Theta(n)          [tree walk]
  T = T(n/2) + 1         a=1,b=2 -> c_crit=0, f=1=n^0   CASE 2 (k=0) -> Theta(log n)      [binary search]
  T = 7T(n/2) + n^2      a=7,b=2 -> c_crit=log2 7~2.807 CASE 1 (f<n^2.807) -> Theta(n^2.807) [Strassen]
  T = 3T(n/2) + n        a=3,b=2 -> c_crit=log2 3~1.585 CASE 1 (f=n<n^1.585) -> Theta(n^1.585) [Karatsuba]
  T = 2T(n/2) + n log n  a=2,b=2 -> c_crit=1, f=n log n CASE 2 (k=1) -> Theta(n log^2 n)
```

**The Master theorem gap.** It does *not* cover everything — e.g. `T = 2T(n/2) + n/log n`
falls between cases 1 and 2 (regularity/polynomial-gap fails). For those, use a
recursion tree or Akra-Bazzi.

### Tool 3: Akra-Bazzi (uneven splits the Master theorem can't touch)

For `T(n) = Σ a_i·T(n/b_i) + f(n)` with *different* subproblem sizes, find `p` with
`Σ a_i / b_i^p = 1`, then `T(n) = Θ( n^p (1 + ∫ f(u)/u^{p+1} du) )`.

```
  Median-of-medians selection:  T(n) = T(n/5) + T(7n/10) + O(n)
  Solve  (1/5)^p + (7/10)^p = 1  at  p = 1  ->  (1/5)+(7/10) = 0.9 < 1
  so p < 1 and the f(n)=n term dominates  =>  T(n) = Theta(n)     [linear-time select! see 02]
```

This is the proof that median-of-medians selection is **worst-case O(n)** despite
two recursive calls — the unequal split keeps the work geometrically shrinking.

---

## Layer 3: Amortized Analysis (the cost-of-a-sequence guarantee)

Amortized analysis answers: *over any sequence of m operations, what is the total
cost divided by m?* It is a **worst-case** guarantee over the sequence — no
probability. Three techniques, increasing in power.

### The canonical example: dynamic array (geometric doubling)

```
  push() when full -> allocate 2x, copy all elements, then insert.
  Costs for n pushes starting from capacity 1:

    op:   1  2  3  4  5  6  7  8  9 ...
    cost: 1  2  3* 1  5* 1  1  1  9* ...   (* = a doubling/resize op copies everything)

  Total copy work across all resizes: 1 + 2 + 4 + ... + n/2 + n < 2n
  Plus n inserts of cost 1.
  => total <= 3n for n pushes  =>  O(1) AMORTIZED per push.
```

This is exactly why `List<T>.Add`, Go slices, and C++ `vector::push_back` are
"O(1)" — they are O(1) *amortized*, and a single push that triggers a resize is
genuinely Θ(n). Quoting it as worst-case O(1) is wrong.

### Technique A — Aggregate

Bound the *total* cost of m operations directly, divide by m. (Used above: total
< 3n ⇒ 3 per op.) Simple but only gives one average for all op types.

### Technique B — Accounting (banker's) method

Charge each operation an *amortized cost*; cheap ops overpay and bank credit, which
expensive ops spend. Invariant: bank balance never goes negative.

```
  Dynamic array, charge $3 per push:
    $1 pays for inserting this element.
    $1 saved on the element ITSELF (to pay for copying it at next resize).
    $1 saved on an OLD element (to pay for copying it at next resize).
  At a resize, every element has $1 banked to fund its copy. Balance stays >= 0.
  => amortized $3 = O(1) per push.   (Same answer, per-op view.)
```

### Technique C — Potential method (the heavy-duty one)

Define a potential function Φ(D) ≥ 0 over the data structure's state. Amortized
cost = actual cost + ΔΦ. The total amortized cost upper-bounds total actual cost
when Φ(start) ≤ Φ(end).

```
  amortized_i = actual_i + Phi(D_i) - Phi(D_{i-1})
  sum of amortized = sum of actual + Phi(D_m) - Phi(D_0)
                   >= sum of actual    (if Phi_0 <= Phi_m, and Phi >= 0)

  Dynamic array: Phi = 2*size - capacity.
    Non-resize push:   actual=1, capacity fixed, size+1 -> dPhi = +2, amortized = 3.
    Resizing push:     actual = size+1 (copy size, insert 1); capacity doubles.
      Before: Phi = 2n - n = n.  After: size n+1, cap 2n -> Phi = 2(n+1)-2n = 2.
      dPhi = 2 - n.  amortized = (n+1) + (2 - n) = 3.   Both cases -> 3 = O(1).
```

The potential method is the universal tool for `06` (Fibonacci heaps, splay trees)
and `07` (union-find's α(n) bound is a potential argument).

```
  WHICH AMORTIZED TECHNIQUE?
  aggregate   -> one op type, want a quick total
  accounting  -> intuitive per-op story, easy invariants
  potential   -> multiple op types, state-dependent costs (heaps, splay, union-find)
```

---

## Layer 4: Average-Case and Probabilistic Analysis

Average-case takes an **expectation over a distribution of inputs** (or over a
*randomized algorithm's* coin flips). The workhorse is **indicator random
variables + linearity of expectation**.

### Worked: expected comparisons in randomized quicksort

```
  Let X_ij = 1 if elements of rank i and j are ever compared, else 0.
  Two elements are compared <=> one of them is the FIRST pivot chosen from the
  range [i..j].  That range has (j - i + 1) elements, all equally likely first.
    => Pr[X_ij = 1] = 2 / (j - i + 1)
  E[total comparisons] = sum_{i<j} 2/(j-i+1)
                       = sum_i sum_{k=1}^{n-i} 2/(k+1)  ~ 2n * H_n ~ 2n ln n
                       = Theta(n log n)
```

No distribution over inputs is assumed here — the randomness is in the *pivot
choice*, so this O(n log n) holds for **every** input. That is the difference
between a randomized algorithm (random internal choices, any input) and average-case
analysis (random input, deterministic algorithm).

```
  RANDOMIZED ALGORITHM            vs   AVERAGE-CASE ANALYSIS
  randomness inside the algorithm      randomness in the input
  guarantee holds for ANY input        guarantee holds for TYPICAL input
  randomized quicksort, hashing        deterministic quicksort on random data
  -> see 09 for RP/BPP/ZPP classes
```

### Average-case ≠ amortized (the most common conflation)

```
  AVERAGE-CASE                        AMORTIZED
  expectation over inputs             total over a sequence / #ops
  can be DEFEATED by an adversary     holds for ANY sequence (adversary-proof)
  needs a probability model           NO probability
  e.g. hash table O(1) EXPECTED       e.g. dynamic array O(1) AMORTIZED
```

A hash table is O(1) **expected amortized** — *expected* because collisions depend
on the (random) hash, *amortized* because of resize/rehash. Both qualifiers are
required and they are not the same word.

---

## Old World → New World Bridges

| You already know | The analysis concept |
|---|---|
| "`List.Add` is basically free" | O(1) **amortized** via geometric doubling; one resize is Θ(n) |
| Profiling shows p99 spikes on resize | The amortized average hides the worst single op — measure tails too |
| A query optimizer's cost model | Recurrence/closed-form cost estimate over an execution plan |
| "It's fast in practice but worst-case bad" | Smoothed analysis (e.g. simplex) — adversarial input + small perturbation |
| Cache-friendly vs cache-hostile loops | The constant factor / memory model the O(·) hides — Θ same, wall-clock differs |
| Retry-with-backoff total cost | An aggregate amortized argument over the retry sequence |

The p99/resize bridge is the most practically important: amortized O(1) is a
*statement about totals*, and the engineer who ships latency SLAs must remember the
individual Θ(n) resize still happens and shows up in the tail.

---

## Decision Cheat Sheet

| Question | Use | Result form |
|---|---|---|
| Solve `aT(n/b)+f(n)`, clean split | Master theorem | one of 3 cases |
| Uneven split (`T(n/5)+T(7n/10)+n`) | Akra-Bazzi / recursion tree | find p, integrate |
| Verify a Master-theorem edge case | recursion tree | sum per level |
| Cost of a *sequence* of ops | amortized (potential) | total/#ops, no luck |
| One op type, quick total | aggregate method | total/m |
| State-dependent op costs (heap/splay) | potential method | Φ + ΔΦ |
| Cost on *random input* | average-case (indicator RVs) | E[·] over inputs |
| Cost with random *internal* choices | randomized analysis | E[·] over coins, any input |
| "Worst-case bad, practice good" | smoothed analysis | E over perturbations |

---

## Common Confusion Points

### "Amortized and average-case are the same"

No. Amortized is a guarantee over a **sequence of operations** with **no
probability** — adversary-proof. Average-case is an **expectation over random
inputs** and can be defeated by an adversary. Dynamic-array push is O(1) amortized
(any sequence); quicksort is O(n log n) average (random input/pivot). A hash table
is O(1) *expected amortized* — both words, because it has random collisions *and*
resizing.

### "The Master theorem solves every divide-and-conquer recurrence"

It has gaps. `T = 2T(n/2) + n/log n` falls between cases 1 and 2 and the theorem
says nothing; Case 3 needs an extra regularity condition. Uneven splits
(`T(n/5)+T(7n/10)+n`) are out of scope entirely — use Akra-Bazzi or a recursion
tree.

### "O(n²) means the algorithm is quadratic"

O is an *upper* bound: O(n²) means "no worse than quadratic," and the algorithm may
run in Θ(n) on your inputs. Use Θ for tight, Ω for "at least." Mixing them up turns
a correct upper bound into a false claim about actual growth.

### "If I randomize, I've done average-case analysis"

Randomizing the *algorithm* (random pivots, random hash seed) gives a guarantee for
**any** input — that is randomized analysis, stronger than average-case, which
assumes the *input* is random. Randomized quicksort's O(n log n) holds on
adversarial input; deterministic quicksort's average-case O(n log n) does not.

### "Constant factors don't matter — it's all Big-O"

Asymptotically true, operationally false. Two O(n log n) sorts can differ 10× from
cache behavior and branch prediction (this is why Timsort/introsort beat textbook
mergesort in practice). The O(·) deliberately hides constants and the memory model;
for production latency you still measure.
