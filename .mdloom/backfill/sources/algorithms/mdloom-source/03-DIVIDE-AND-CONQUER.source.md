---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-DIVIDE-AND-CONQUER.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:divide-and-conquer
kind: guide
module: algorithms
section: mathematics-physics
title: Divide and Conquer
status: source-custody
source_custody: partial
current_path: algorithms/03-DIVIDE-AND-CONQUER.md
canonical_path: algorithms/03-DIVIDE-AND-CONQUER.md
backsource_ids: [mdloom-backfill:algorithms:03-divide-and-conquer, git-history:algorithms:03-divide-and-conquer]
concepts: [divide and conquer, recurrences, karatsuba, strassen, fft, closest pair, master theorem]
root_concepts: [divide and conquer]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Divide and Conquer

Divide-and-conquer is the paradigm where subproblems are **disjoint**: you split
the input, solve the pieces independently (recursively), and combine. Because the
pieces share no work, the cost is a clean recurrence `T(n) = a·T(n/b) + f(n)`, and
the entire art is *moving the watershed* between the leaf cost (`a`, `b`) and the
combine cost (`f`). The famous wins — Karatsuba, Strassen, FFT — all come from
reducing `a` (fewer subproblems) so the leaves stop dominating.

```
  DIVIDE & CONQUER: T(n) = a T(n/b) + f(n)        (a subproblems, size n/b, combine f)
  ===================================================================================

                         +-----------------+
                         |  PROBLEM size n |
                         +-----------------+
                                |  DIVIDE into a pieces of size n/b
        +-----------------+-----------------+----------+
        v                 v                 v
        +----------+      +----------+      +----------+
        | size n/b |      | size n/b |  ... | size n/b |     (a of them)
        +----------+      +----------+      +----------+
        |     CONQUER (recurse)                        |
        +-----------------+-----------------+----------+
                                |  COMBINE in f(n)
                                v
                         +-----------------+
                         |   SOLUTION      |
                         +-----------------+

   The lever:  watershed exponent c = log_b(a)  (= log of #leaves)
     a small (few subproblems) -> combine f(n) dominates  -> T = Theta(f)
     a large (many subproblems)-> leaves dominate         -> T = Theta(n^c)

   ALGORITHM         a   b   f(n)     c=log_b a       T(n)
   ---------         -   -   ----     ---------       ----
   mergesort         2   2   n        1               n log n     (balanced)
   binary search     1   2   1        0               log n
   Karatsuba mult    3   2   n        1.585           n^1.585     (fewer mults!)
   Strassen matmul   7   2   n^2      2.807           n^2.807     (7 not 8 mults)
   FFT               2   2   n        1               n log n
   closest pair      2   2   n        1               n log n
   median-of-med.    (uneven split, Akra-Bazzi)       n          (see 01)
```

**Read this with `01-ANALYSIS.md` open**: every bound here is a Master-theorem or
Akra-Bazzi solution. The design game is to *lower `a`* — do fewer recursive calls
by being clever in the combine step.

---

## Layer 1: The Template and the Two Canonical Sorts

```
  divide_and_conquer(P):
     if |P| small: return base_solve(P)        # base case
     split P into P_1 .. P_a                     # DIVIDE   -> determines a, b
     S_i = divide_and_conquer(P_i)               # CONQUER  -> the recursion
     return combine(S_1 .. S_a)                  # COMBINE  -> determines f(n)
```

The two textbook sorts (full treatment in `02`) sit at opposite ends of the work
distribution:

```
   MERGESORT: cheap divide, EXPENSIVE combine        QUICKSORT: EXPENSIVE divide, free combine
   T = 2T(n/2) + n  (the merge is the n)             T = 2T(n/2) + n  (the partition is the n)
   balanced split ALWAYS                             split quality depends on the PIVOT
   => Theta(n log n) worst-case                      => avg n log n, worst n^2 (bad pivots)
```

This is the cleanest illustration of the paradigm's lever: same recurrence shape,
but mergesort *guarantees* the balanced split while quicksort gambles on it.

---

## Layer 2: Fast Multiplication — Reducing `a`

### Karatsuba — integer multiplication in O(n^1.585)

Schoolbook multiplication of two n-digit numbers is Θ(n²). Split each into high/low
halves: `x = x1·B + x0`, `y = y1·B + y0`. Naively `xy` needs **4** half-size
products. Karatsuba's trick computes it with **3**.

```
   x*y = x1y1 B^2 + (x1y0 + x0y1) B + x0y0
   Naive: 4 multiplications  -> T(n)=4T(n/2)+n = Theta(n^2)   (no win)

   Karatsuba: compute only 3 products:
       z2 = x1*y1
       z0 = x0*y0
       z1 = (x1+x0)(y1+y0) - z2 - z0      <-- the middle term, ONE multiply
   x*y = z2 B^2 + z1 B + z0
   T(n) = 3 T(n/2) + O(n)  ->  Theta(n^1.585)     [Master case 1, c=log2 3]
```

Worked (base 10, B=10): x=12, y=34 → x1=1,x0=2,y1=3,y0=4.

```
   z2 = 1*3 = 3
   z0 = 2*4 = 8
   z1 = (1+2)(3+4) - 3 - 8 = 3*7 - 11 = 21 - 11 = 10
   xy = 3*100 + 10*10 + 8 = 300 + 100 + 8 = 408 = 12*34  CHECK
```

Going from `a=4` to `a=3` drops the exponent from 2 to 1.585 — the entire
improvement is "one fewer recursive multiply." (Toom-Cook generalizes this; FFT
takes it to the limit.)

### Strassen — matrix multiplication in O(n^2.807)

The same lever for n×n matrices. Block into 2×2 of (n/2)×(n/2) blocks: naive needs
**8** block multiplies → `8T(n/2)+n² = Θ(n³)`. Strassen uses **7**.

```
   T(n) = 7 T(n/2) + O(n^2)  ->  Theta(n^(log2 7)) = Theta(n^2.807)   [Master case 1]
   7 products (M1..M7) recombined with +/- into the 4 result blocks.
```

Strassen is the proof that the "obvious" Θ(n³) is not optimal; in practice it wins
only for large n (high constants, numerical-stability caveats) and is the gateway to
the theoretical frontier (current record ≈ O(n^2.37)). Cross-ref `numerical-methods/`
for the stability trade-offs.

---

## Layer 3: The FFT — Divide-and-Conquer over Roots of Unity

The FFT computes the Discrete Fourier Transform in **O(n log n)** instead of Θ(n²),
and via the convolution theorem it multiplies two degree-n polynomials (or two
n-digit numbers) in O(n log n) — the asymptotic limit of the Karatsuba idea.

```
   DFT: evaluate a degree-(n-1) polynomial at the n complex n-th roots of unity.
   KEY: split p(x) into even and odd coefficient polynomials:
        p(x) = p_even(x^2) + x * p_odd(x^2)
   The n roots of unity, when squared, give only n/2 DISTINCT values.
   => evaluating p at n points reduces to evaluating p_even, p_odd at n/2 points.

   T(n) = 2 T(n/2) + O(n)   ->   Theta(n log n)     [Master case 2, mergesort recurrence]

   USE (fast convolution / multiplication):

       +------+   FFT    +-------+
       | a, b | ------>  | A, B  |
       +------+          +-------+
                         A, B in point-value form

                         |  pointwise multiply  C[k] = A[k]*B[k]   (O(n))
                         v

       +-------+  inverse FFT    +----------+
       |  C    | ------------>   | a (*) b  |
       +-------+                 +----------+
                                 a (*) b = convolution / product

   Total: O(n log n) — beats Karatsuba's n^1.585 and schoolbook n^2.
```

The structural trick is identical to Karatsuba: exploit shared structure (here, the
roots of unity collapsing under squaring) so the recursion has `a=2` over halved
input instead of `a=4` over full work. FFT underpins signal processing, big-integer
libraries, and polynomial arithmetic. Cross-ref `signal-processing/` and
`information-theory/`.

---

## Layer 4: Geometric Divide-and-Conquer — Closest Pair

Finding the closest pair among n points is naively Θ(n²). Divide-and-conquer gets
O(n log n) — the subtlety is the *combine* step.

```
   1) Sort points by x. Split into LEFT / RIGHT halves by a vertical line.
   2) Recurse: get closest pair in each half, let d = min(d_left, d_right).
   3) COMBINE: the closest pair might straddle the line. Only points within a
      vertical STRIP of width 2d around the line can do better than d.

         |          strip width 2d        |
         |   .   .  | . :  . | .    .      |
         |       .  |.: .  . |.   .        |   <- a point compares to at most
         |   .      | . . . :|       .     |      7 OTHERS in the strip (packing
         |          |        |             |      argument: a d x 2d box fits <=8 pts
        L-half      <-- 2d -->     R-half          spaced >= d apart)

   Sort strip points by y; each compares to the next ~7 only -> O(n) combine.
   T(n) = 2 T(n/2) + O(n)  ->  Theta(n log n)    [mergesort recurrence]
```

The "7 neighbors" packing bound is what keeps the combine linear — without it the
strip comparison would be Θ(n²) and the whole thing would collapse back to brute
force. This is the signature move of geometric D&C: a packing/geometry argument
bounds the combine. Cross-ref `graph-algorithms/` and `mathematics/` for the
computational-geometry family.

---

## Layer 5: Designing a Divide-and-Conquer Algorithm

```
  THE DESIGN CHECKLIST
  1. Can the problem split into INDEPENDENT subproblems? (if they overlap -> DP, see 04)
  2. What are a (count) and b (shrink factor)? -> fixes the watershed n^(log_b a).
  3. How cheap can COMBINE be? -> this is f(n); lowering it or lowering 'a' is the whole game.
  4. Solve T(n)=aT(n/b)+f(n) with Master theorem; uneven split -> Akra-Bazzi (see 01).
  5. Pick the base case size to amortize recursion overhead (real code: switch to
     insertion sort below ~16 elements, etc.).
```

```
   WHERE THE SPEEDUP COMES FROM (always one of these):
   - reduce a:  Karatsuba 4->3, Strassen 8->7   (fewer subproblems)
   - reduce f:  closest-pair strip O(n) combine  (cheaper combine via structure)
   - exploit shared structure: FFT roots of unity (the limit of "reduce a")
```

---

## Old World → New World Bridges

| You already know | The divide-and-conquer concept |
|---|---|
| MapReduce / fork-join parallelism | Divide-and-conquer's independent subproblems map directly to parallel tasks |
| A parallel `Sort` / PLINQ partitioning | Recursive split = the natural parallel decomposition (disjoint subproblems) |
| Big-integer arithmetic in a crypto lib | Karatsuba/Toom/FFT multiplication under the hood (`cryptography/`) |
| Signal/audio FFT in a DSP pipeline | The same O(n log n) DFT, used for convolution/filtering (`signal-processing/`) |
| BLAS/GEMM tuned matrix multiply | Strassen as the asymptotic improvement over the Θ(n³) triple loop |
| Recursive descent over a balanced tree | The recursion-tree cost model — depth × per-level work |

The fork-join/MapReduce bridge is the load-bearing one for a systems leader:
divide-and-conquer's *independence of subproblems* is exactly the property that makes
a computation embarrassingly parallel, which is why these algorithms map cleanly
onto multicore and distributed execution while DP (overlapping subproblems) does not.

---

## Decision Cheat Sheet

| Problem | Algorithm | Bound | Lever |
|---|---|---|---|
| Stable general sort | mergesort | Θ(n log n) | balanced split |
| In-place fast sort | quicksort | avg Θ(n log n) / worst Θ(n²) | partition |
| Multiply huge integers | Karatsuba → FFT | n^1.585 → n log n | reduce `a` (3 mults) → roots of unity |
| Multiply large matrices | Strassen | n^2.807 | 7 not 8 block mults |
| Polynomial mult / convolution | FFT | n log n | roots of unity |
| Closest pair of points | D&C strip | n log n | O(n) combine via packing |
| k-th order statistic, worst-case | median-of-medians | Θ(n) | uneven split, Akra-Bazzi (`01`) |
| Subproblems *overlap* | — use DP instead | — | go to `04` |

---

## Common Confusion Points

### "Karatsuba/Strassen are faster, so always use them"

Asymptotically yes, but they carry large constant factors and (Strassen) numerical-
stability concerns. Crossover points are large — schoolbook multiplication wins for
small operands, and Strassen only pays off for big matrices. The asymptotic win is
real but the constant matters in practice (cross-ref `numerical-methods/`).

### "FFT and Karatsuba do different things"

They are the same idea at different points on the curve: both compute polynomial /
integer products by exploiting shared structure to reduce the number of recursive
multiplications. Karatsuba reduces 4→3 per level; FFT pushes this to the limit via
the roots of unity, hitting O(n log n) — the asymptotic floor for multiplication by
these methods.

### "Divide-and-conquer and dynamic programming are interchangeable"

They split on **subproblem overlap**. D&C subproblems are *disjoint* (no shared
work → clean recurrence). DP subproblems *overlap* (re-solved exponentially often →
must memoize). If your recursion tree has repeated nodes, plain D&C is exponential
and you need `04`. Mergesort is D&C; edit distance is DP.

### "The Master theorem gives the bound for any of these"

Most, not all. Median-of-medians has an *uneven* split (`T(n/5)+T(7n/10)+n`) that
the Master theorem cannot handle — it needs Akra-Bazzi (`01`). And the regularity
condition in Case 3 must actually be checked.

### "More subproblems = faster (more parallelism)"

For the *asymptotic* bound, *fewer* subproblems is better — Karatsuba (3) beats
naive (4), Strassen (7) beats naive (8), because `a` is the base of the leaf-count
exponent `n^(log_b a)`. More subproblems gives more *parallelism* but a *worse*
serial complexity. Don't conflate the two.
