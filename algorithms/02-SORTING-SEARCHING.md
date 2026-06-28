---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:sorting-searching
kind: guide
module: algorithms
section: mathematics-physics
title: Sorting and Searching
status: source-custody
source_custody: partial
current_path: algorithms/02-SORTING-SEARCHING.md
canonical_path: algorithms/02-SORTING-SEARCHING.md
backsource_ids: [proof-backfill:algorithms:02-sorting-searching, git-history:algorithms:02-sorting-searching]
concepts: [sorting, comparison sort lower bound, quicksort, mergesort, heapsort, radix sort, selection, binary search]
root_concepts: [sorting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Sorting and Searching

Sorting is the field's canonical case study: it has a *provable lower bound* in the
comparison model, a family of algorithms that hit it, a separate family that
escapes it under extra assumptions, and clean stability/in-place trade-offs that
matter in real systems. Searching is its dual — sorted structure is what makes
sublinear search possible. Every complexity bound below is stated best/average/worst
with the precondition that governs it.

```
  THE SORTING LANDSCAPE
  =====================================================================================

   COMPARISON SORTS  (only learn via "a<b?")        NON-COMPARISON  (read key bits)
   bounded BELOW by Omega(n log n)                   can be O(n) — ESCAPE the bound
   ------------------------------------              ----------------------------------
   +----------------------------------+              +------------------------------+
   | O(n^2) family    | O(n log n)    |              | counting   O(n+k)            |
   |  insertion       |  mergesort *  |              | radix      O(d(n+k))         |
   |  selection       |  heapsort     |              | bucket     O(n) avg          |
   |  bubble          |  quicksort**  |              +------------------------------+
   +----------------------------------+               precondition: integer/bounded keys
     * stable          ** avg n log n / worst n^2
                          NOT stable, in-place

            |  the lower bound (decision tree):
            v
   n! orderings -> binary decision tree of height >= log2(n!) = Theta(n log n)
   => NO comparison sort does better than Omega(n log n) in the worst case.

   SEARCHING                          SELECTION (k-th smallest)
   ---------                          -------------------------
   unsorted: O(n) linear              quickselect   O(n) avg / O(n^2) worst
   sorted:   O(log n) binary search   median-of-medians O(n) WORST (Akra-Bazzi, see 01)
   sorted+indexed: O(log log n)
     interpolation (uniform keys)
```

**Read top-down**: the comparison model has a hard floor (`Ω(n log n)`); algorithms
either hit that floor (mergesort, heapsort, quicksort-avg) or leave the model
entirely (counting/radix) to go linear, at the cost of assuming structured keys.

---

## Layer 1: The Comparison-Sort Lower Bound

This is the cleanest impossibility result in the directory, and it pins down
*exactly* what "you can't sort faster than n log n" means.

```
   A comparison sort's only window into the data is the question "is a[i] < a[j]?"
   Its entire execution is a binary DECISION TREE:

                        a < b ?
                       /        \
                    yes          no
                    /              \
                 b < c ?          a < c ?
                 /   \            /     \
            [a,b,c]  a<c?     [b,a,c]   b<c?
                     / \                / \
               [a,c,b][c,a,b]    [b,c,a][c,b,a]

   - Each LEAF is one of the n! possible orderings (all must be reachable).
   - The number of comparisons on an input = depth of its leaf.
   - Worst case = tree HEIGHT.
   - A binary tree with L leaves has height >= ceil(log2 L).
   - L >= n!  =>  height >= log2(n!) = Theta(n log n)   [Stirling: log2(n!) ~ n log2 n]

   THEOREM: every comparison sort makes Omega(n log n) comparisons in the worst case.
```

The bound is about the **model**, not about cleverness. Counting/radix sort run in
O(n) precisely because they are *not* comparison sorts — they never ask "a < b?",
they read the key directly, so the decision-tree argument does not apply to them.
This is the same move as a reduction in `09`: an impossibility result is only as
strong as the model it is stated in.

---

## Layer 2: The Comparison Sorts (the property matrix)

```
  +-------------------------------------------------------------------------------+
  | Sort       | Best       | Average    | Worst      | Space   | Stable | In-place|
  |------------|------------|------------|------------|---------|--------|---------|
  | Insertion  | O(n)       | O(n^2)     | O(n^2)     | O(1)    | YES    | yes     |
  | Selection  | O(n^2)     | O(n^2)     | O(n^2)     | O(1)    | no     | yes     |
  | Bubble     | O(n)       | O(n^2)     | O(n^2)     | O(1)    | YES    | yes     |
  | Mergesort  | O(n log n) | O(n log n) | O(n log n) | O(n)    | YES    | no      |
  | Heapsort   | O(n log n) | O(n log n) | O(n log n) | O(1)    | no     | yes     |
  | Quicksort  | O(n log n) | O(n log n) | O(n^2)     | O(log n)| no     | yes     |
  | Timsort    | O(n)       | O(n log n) | O(n log n) | O(n)    | YES    | no      |
  +-------------------------------------------------------------------------------+
   "Stable" = equal keys keep their original relative order.
   Quicksort space O(log n) = recursion stack depth (with tail-recursion on the smaller side).
```

### Insertion sort — O(n) on nearly-sorted input

Best-case O(n) (already sorted), and it is the building block Timsort uses on small
runs. Adaptive: cost is O(n + inversions).

```
   sort [5, 2, 4, 6, 1, 3], insert each into the sorted prefix:

   [5 | 2 4 6 1 3]            take 2, shift 5
   [2 5 | 4 6 1 3]            take 4, shift 5
   [2 4 5 | 6 1 3]            take 6, no shift
   [2 4 5 6 | 1 3]            take 1, shift 6 5 4 2
   [1 2 4 5 6 | 3]            take 3, shift 6 5 4
   [1 2 3 4 5 6]              done
```

### Mergesort — stable, O(n log n) worst-case, O(n) extra space

```
   split to singletons, then merge sorted runs (T(n)=2T(n/2)+n -> Theta(n log n), see 01):

   [5 2 4 6 1 3]
   -> [5 2 4] [6 1 3]
   -> [5][2 4] [6][1 3]
   -> [5][2][4] [6][1][3]
   merge: [2 4][5] -> [2 4 5]   ;   [1 3][6] -> [1 3 6]
   merge: [2 4 5] + [1 3 6]:
          take min of fronts each step:
          1<2 ->1 | 2<3 ->2 | 3<4 ->3 | 4<6 ->4 | 5<6 ->5 | 6
   => [1 2 3 4 5 6]
```

Stable because the merge takes from the left run on ties. The O(n log n) is
worst-case (no bad inputs), which is why it backs `OrderBy`-style stable sorts and
external sorts.

### Quicksort — avg O(n log n), **worst O(n²)**, not stable

```
   partition around a pivot (here last element = 3): elements < 3 left, >= 3 right.

   [5 2 4 6 1 | 3]   pivot 3
     scan: 5>=3 keep right, 2<3 swap-left, 4>=3, 6>=3, 1<3 swap-left
     -> [2 1 | 3 | 5 6 4]      (3 in final position)
   recurse left [2 1] -> [1 2] ; recurse right [5 6 4] -> [4 5 6]
   => [1 2 3 4 5 6]

   WORST CASE: pivot is always the min/max (e.g. already-sorted input + first-element pivot)
     -> partitions of size n-1, 0  ->  T(n)=T(n-1)+n = Theta(n^2).
   FIX: randomized pivot OR median-of-three -> O(n log n) EXPECTED for any input (see 01).
```

Quicksort is the practical default (in-place, cache-friendly, small constants) but
its O(n log n) is *average/expected*, never a worst-case guarantee. Production
libraries use **introsort**: quicksort that switches to heapsort once recursion
depth exceeds ~2·log n, capping the worst case at O(n log n).

### Heapsort — O(n log n) worst-case, in-place, **not stable**

Build a max-heap in O(n), then repeatedly extract-max into the back. O(1) extra
space, O(n log n) worst-case — but poor cache locality and not stable, so it is
usually the *fallback*, not the default. (Heaps themselves are in `06`.)

---

## Layer 3: Non-Comparison Sorts (escaping Ω(n log n))

These read key *values/bits* directly. They beat the comparison bound only under
the precondition of integer (or fixed-width) keys in a bounded range.

### Counting sort — O(n + k), stable, for keys in [0, k)

```
   sort [2,5,2,0,3,2] with keys in [0,5]:
   1) count occurrences:   value: 0 1 2 3 4 5
                           count: 1 0 3 1 0 1
   2) prefix-sum to positions: 1 1 4 5 5 6   (cumulative)
   3) place each element (scanning RIGHT-to-LEFT keeps it STABLE):
      => [0, 2, 2, 2, 3, 5]
   cost: O(n + k).  Linear when k = O(n).  Needs O(k) extra space.
```

### Radix sort — O(d·(n + k)), stable

Sort by each digit, least-significant first, using a *stable* sort (counting) per
digit. With `d` digits over base `k`: O(d·(n+k)). For 32-bit ints in base 256,
d = 4, k = 256 → effectively O(n).

```
   LSD radix on [170, 45, 75, 90, 802, 24, 2, 66] (base 10):

   by 1s: 170 90 802 2 24 45 75 66        (ones: 0 0 2 2 4 5 5 6)
   by 10s: 802 2 24 45 66 170 75 90       (tens: 0 0 2 4 6 7 7 9)
   by 100s: 2 24 45 66 75 90 170 802      (hundreds: 0 0 0 0 0 0 1 8)
   => sorted. Each pass MUST be stable or earlier-digit order is lost.
```

**Why stability is non-negotiable here**: radix relies on earlier (less significant)
passes having already ordered ties; a non-stable per-digit sort would scramble them.

### Bucket sort — O(n) average for uniform keys

Distribute into n buckets by key range, sort each (insertion), concatenate. O(n)
average under a uniform-distribution assumption; O(n²) worst-case if everything
lands in one bucket.

```
  WHEN A NON-COMPARISON SORT WINS
  counting  -> small integer key range k = O(n)
  radix     -> fixed-width integer/string keys, large range
  bucket    -> keys ~uniform over a known interval (e.g. floats in [0,1))
  otherwise -> a comparison sort; you cannot beat Omega(n log n) generically
```

---

## Layer 4: Selection (the k-th smallest)

You can find the k-th order statistic *without fully sorting* — better than the
O(n log n) a sort would cost.

```
  QUICKSELECT (partition like quicksort, recurse into ONE side):
    avg O(n):  n + n/2 + n/4 + ... = O(n)    worst O(n^2): bad pivots
    median:    k = n/2

  MEDIAN-OF-MEDIANS (deterministic pivot = median of group-of-5 medians):
    T(n) = T(n/5) + T(7n/10) + O(n)  ->  Theta(n) WORST CASE  (Akra-Bazzi, see 01)
    guarantees the pivot splits off at least 30% each side.
```

Quickselect is what you reach for in practice (small constants); median-of-medians
is the existence proof that **worst-case linear selection** is possible, and is the
pivot strategy that makes a deterministic O(n log n) quicksort variant possible.

---

## Layer 5: Searching

```
  +------------------------------------------------------------------------+
  | Structure        | Search    | Notes / precondition                    |
  |------------------|-----------|-----------------------------------------|
  | unsorted array   | O(n)      | linear scan; no structure to exploit    |
  | sorted array     | O(log n)  | binary search                           |
  | sorted, uniform  | O(log log n)| interpolation search (uniform keys)   |
  | hash table       | O(1) exp* | *amortized expected, NOT worst-case (06)|
  | balanced BST     | O(log n)  | worst-case guarantee, ordered (06)      |
  | B-tree           | O(log n)  | disk/SSD-friendly, high fan-out (06)    |
  +------------------------------------------------------------------------+
```

### Binary search — and the off-by-one that bites everyone

```
   find 23 in [4, 8, 15, 16, 23, 42]   (indices 0..5)
   lo=0 hi=5  mid=2 -> 15 < 23 -> lo=3
   lo=3 hi=5  mid=4 -> 23 == 23 -> FOUND at index 4

   Invariant: target, if present, is always in [lo, hi].
   Use mid = lo + (hi - lo)/2  (NOT (lo+hi)/2 — that can overflow for large indices).
```

Binary search generalizes far beyond arrays: any **monotone predicate** can be
binary-searched ("smallest x where f(x) is true"), which is the backbone of
parametric search and many "minimize the maximum" optimization problems.

---

## Old World → New World Bridges

| You already know | The sorting/searching concept |
|---|---|
| `OrderBy` is a *stable* sort | LINQ/`OrderBy` guarantees stability — mergesort/Timsort property, not heapsort/quicksort |
| `Array.Sort` "just sorts" | It is **introsort**: quicksort + heapsort fallback to cap worst case at O(n log n) |
| A clustered index keeps rows sorted | The Ω(n log n) build cost / O(log n) seek of a sorted B-tree (`06`) |
| Bucketing rows by hash for a hash join | Bucket sort's distribute-then-combine, same idea |
| "Find the p99 latency" | A selection (k-th order statistic) — O(n) quickselect, no full sort needed |
| Feature flag rollout by `id % N` | Counting/radix-style bucketing by integer key |

The `OrderBy`-stability bridge is the practically important one: an engineer who
swaps a stable sort for an unstable one (or vice versa) can silently change output
ordering for equal keys — a real bug source in pagination and tie-breaking.

---

## Decision Cheat Sheet

| I need to... | Use | Why |
|---|---|---|
| General-purpose in-place sort | quicksort / introsort | fast, small constants, O(n log n) capped |
| Stable sort (preserve tie order) | mergesort / Timsort | stability guaranteed |
| Worst-case O(n log n), O(1) space | heapsort | no bad inputs, in-place (not stable) |
| Sort small integers, k = O(n) | counting sort | O(n+k), stable, escapes the bound |
| Sort fixed-width int/string keys | radix sort | O(d(n+k)), stable per digit |
| Sort ~uniform floats in [0,1) | bucket sort | O(n) average |
| Nearly-sorted data | insertion / Timsort | O(n + inversions), adaptive |
| k-th smallest, expected linear | quickselect | O(n) avg, simple |
| k-th smallest, worst-case linear | median-of-medians | O(n) worst (proof in `01`) |
| Search a sorted array | binary search | O(log n), watch overflow & off-by-one |
| Search "smallest x with f(x) true" | binary search on predicate | monotonicity is the only requirement |
| Exact-match by key | hash table (`06`) | O(1) expected (not worst) |

---

## Common Confusion Points

### "Quicksort is O(n log n)"

Average/expected only. Worst case is **O(n²)** (sorted input + naive pivot).
Randomized or median-of-three pivoting makes O(n log n) hold *in expectation for any
input*, but the worst case remains O(n²) for the pure algorithm — which is why real
libraries use introsort to *guarantee* O(n log n) by falling back to heapsort.

### "Heapsort is the best sort — O(n log n) worst-case and in-place"

It is O(n log n) worst-case and in-place, but **not stable** and cache-hostile (heap
indexing jumps around memory). Quicksort beats it in wall-clock on typical data;
heapsort is the *fallback that bounds the worst case*, not the default.

### "Counting/radix sort prove you can sort in O(n) — the lower bound is wrong"

The Ω(n log n) bound is **only for comparison sorts**. Counting and radix are
non-comparison: they read key values/bits and assume integer keys in a bounded
range. Under those preconditions O(n+k) / O(d(n+k)) is real; for arbitrary
comparable keys you are stuck with Ω(n log n). The bound is not wrong — it is
scoped to a model these sorts leave.

### "Stability doesn't matter, I just want it sorted"

It matters whenever equal keys carry meaning beyond the key — multi-key sorts
(sort by date, then stably by name), pagination, and tie-breaking all depend on it.
`OrderBy` is stable; swapping in an unstable sort silently reorders ties.

### "Radix sort can be most-significant-digit, order doesn't matter"

LSD radix *requires* a **stable** per-digit sort, and the standard form goes
least-significant first precisely so earlier passes' order survives. MSD radix
exists but partitions recursively and is a different algorithm; you cannot just
flip the digit order of LSD radix and keep it correct.

### "Binary search is trivial"

The algorithm is trivial; the implementation is famously bug-prone — integer
overflow in `(lo+hi)/2`, off-by-one in the `lo`/`hi` update, and infinite loops on
the boundary condition. Use `lo + (hi-lo)/2` and a clear loop invariant.
