---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-DATA-STRUCTURES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:data-structures
kind: guide
module: algorithms
section: mathematics-physics
title: Data Structures - Heaps, Balanced BSTs, Hash Tables, Segment/Fenwick
status: source-custody
source_custody: partial
current_path: algorithms/06-DATA-STRUCTURES.md
canonical_path: algorithms/06-DATA-STRUCTURES.md
backsource_ids: [proof-backfill:algorithms:06-data-structures, git-history:algorithms:06-data-structures]
concepts: [heaps, balanced binary search trees, hash tables, segment trees, fenwick trees, skip lists, B-trees]
root_concepts: [data structures]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Data Structures — Heaps, Balanced BSTs, Hash Tables, Segment/Fenwick

Data structures are the *amortized-cost engines* that turn naive O(n) or O(n²) loops
into O(log n) or O(1) operations. Each one is a contract: a set of operations and
their cost bounds, achieved by maintaining an invariant. The job here is to state
those bounds **exactly** — worst-case vs amortized vs expected — and to know which
structure's contract matches the operation mix you actually have. The single most
abused bound in the field lives here: hash-table O(1) is *amortized expected*, never
worst-case.

```
  DATA STRUCTURES BY THE OPERATION CONTRACT THEY OFFER
  =====================================================================================

   ORDERED (comparisons; keep keys sorted)     UNORDERED (hashing; no order)
   ---------------------------------------     -----------------------------
   +-------------------+ +-----------------+    +-----------------------------+
   | BALANCED BST      | | SKIP LIST       |    | HASH TABLE                  |
   | (red-black,AVL,   | | randomized,     |    | chaining / open addressing  |
   |  treap, B-tree)   | | expected O(logn)|    | O(1) AMORTIZED EXPECTED     |
   | O(log n) WORST    | |                 |    | O(n) worst-case (collisions)|
   | search/ins/del    | |                 |    | NO order, NO range queries  |
   | + range/successor | |                 |    |                             |
   +-------------------+ +-----------------+    +-----------------------------+
            |  comparison-based -> Omega(log n) per op (decision-tree, see 02)
            v
   PRIORITY (partial order on one key)        RANGE / PREFIX AGGREGATES
   ----------------------------------         -------------------------
   +-------------------+                       +-----------------------------+
   | HEAP              |                       | FENWICK (BIT)  prefix sums  |
   | binary: insert,   |                       |   point update / prefix qry |
   | extract O(log n); |                       |   O(log n), tiny constant   |
   | peek O(1)         |                       | SEGMENT TREE  any assoc op  |
   | Fibonacci: O(1)   |                       |  range query + range update |
   | decrease-key amrt |                       |  O(log n), lazy propagation |
   +-------------------+                       +-----------------------------+

   THE BOUNDS YOU MUST NOT MISQUOTE:
     balanced BST: O(log n) WORST-CASE (a guarantee)
     hash table:   O(1) AMORTIZED EXPECTED (collisions/resize; adversary -> O(n))
     binary heap:  O(log n) insert/extract; decrease-key O(log n)
     Fibonacci heap: decrease-key O(1) AMORTIZED (the Dijkstra speedup)
```

**Read by operation mix**: need ordered iteration / range queries → balanced BST or
segment/Fenwick; need only fastest exact-match → hash table; need a dynamic
min/max → heap. The right structure is the one whose contract matches your queries.

---

## Layer 1: Heaps (the priority-queue engine)

A binary heap is a complete binary tree (stored in an array) with the heap property:
parent ≤ children (min-heap). It is the standard priority queue.

```
   ARRAY-EMBEDDED BINARY HEAP (min-heap):  node i -> children 2i+1, 2i+2; parent (i-1)/2

   array: [1, 3, 6, 5, 9, 8]            tree:        1
   index:  0  1  2  3  4  5                        /   \
                                                  3     6
                                                 / \   /
                                                5   9 8

   insert(2): place at end, SIFT UP        extract-min: remove root, move last to root,
     [1,3,6,5,9,8,2] -> swap 2 with 6         SIFT DOWN.  [8,3,6,5,9] -> sift 8 down:
     [1,3,2,5,9,8,6]  (2<6, stops at parent 1)   swap with min child 3 -> [3,8,6,5,9]
                                                 -> swap 8 with min(5) -> [3,5,6,8,9]

   OPERATION       BINARY HEAP   FIBONACCI HEAP (amortized)
   insert          O(log n)      O(1)
   peek-min        O(1)          O(1)
   extract-min     O(log n)      O(log n) amortized
   decrease-key    O(log n)      O(1) amortized   <-- the Dijkstra/Prim speedup
   build (heapify)  O(n)          O(n)
```

**Build-heap is O(n), not O(n log n).** Sifting from the bottom up, most nodes are
near the leaves and sift a short distance; the sum `Σ n/2^h · h` telescopes to O(n).
This is the classic "it looks like n log n but isn't" bound.

**Fibonacci heaps** give O(1) *amortized* decrease-key (potential-method proof,
`01`/`07`), which improves Dijkstra/Prim from `O(E log V)` to `O(E + V log V)` —
though high constants mean binary/pairing heaps usually win in practice
(`graph-algorithms/03`,`04`).

---

## Layer 2: Balanced Binary Search Trees

A BST gives ordered operations, but degenerates to O(n) if unbalanced (insert sorted
data → linked list). Balanced BSTs maintain an invariant guaranteeing O(log n)
**worst-case** height.

```
   THE FAMILY (ordered ops; O(log n) search/insert/delete — worst-case for
   AVL/Red-Black/B-tree, expected for Treap, amortized for Splay)
   +-----------------------------------------------------------------------------+
   | Structure   | Balance invariant                  | Notes                    |
   |-------------|------------------------------------|--------------------------|
   | AVL         | |height(L)-height(R)| <= 1         | strictest; faster lookup |
   | Red-Black   | no red-red; equal black-height     | fewer rotations on write |
   | Treap       | BST on key + heap on random prio   | simple, expected O(log n)|
   | B-tree      | high fan-out, all leaves same depth| disk/SSD: minimize I/Os  |
   | Splay       | move-to-root on access             | amortized O(log n)       |
   +-----------------------------------------------------------------------------+
   beyond search: SUCCESSOR/PREDECESSOR, RANGE QUERY, ORDERED ITERATION, rank/select.
```

```
   ROTATION (the rebalancing primitive — preserves BST order):

        y                          x
       / \      right-rotate(y)   / \
      x   C    ------------->    A   y
     / \       <-------------       / \
    A   B       left-rotate(x)     B   C
   in-order: A x B y C   ==   A x B y C    (order preserved, heights rebalanced)
```

```
   AVL vs RED-BLACK trade-off:
     AVL: tighter balance -> shallower -> FASTER LOOKUPS, but MORE rotations on insert/delete
     RB:  looser balance  -> deeper      -> fewer write-time rotations -> better for write-heavy
   This is why language standard libraries (std::map, TreeMap) use red-black:
     amortized fewer structural changes under mixed workloads.
```

**B-trees** are the bridge to systems: high fan-out minimizes pointer chases / disk
seeks, which is why every database index and filesystem uses a B-tree/B+-tree, not an
AVL tree. A senior engineer who has tuned an index already knows this structure
operationally; the O(log_B n) bound with large B is why (cross-ref `computing/`).

---

## Layer 3: Hash Tables (the O(1)-expected engine)

A hash table maps keys to buckets via a hash function. The contract is the one most
often misstated: **O(1) amortized expected**, with O(n) worst-case.

```
   CHAINING                              OPEN ADDRESSING
   --------                              ---------------
   each bucket = a linked list           store directly in the array; on collision,
   collisions appended                   PROBE for the next slot (linear/quadratic/double)
   load factor alpha = n/m can exceed 1  alpha < 1 required; resize before full
   simple deletion                       deletion needs tombstones

   buckets:  0: ->                        slots (linear probe, h(k)=k mod 7):
             1: -> [8] -> [15]             insert 8: slot 1; insert 15: slot 1 taken -> slot 2
             2: -> [23]                    insert 23: slot 2 taken -> slot 3 ...
             3: ->
   EXPECTED chain length = alpha = n/m   -> O(1) per op when alpha is bounded.
```

```
   THE EXACT BOUNDS:
     search/insert/delete:  O(1 + alpha) EXPECTED  -> O(1) when alpha = O(1)
     resize (rehash all):   O(n) once, amortized O(1) per op (geometric growth, see 01)
     WORST CASE:            O(n)  (all keys collide into one bucket)
   => the correct phrasing is "O(1) AMORTIZED EXPECTED", never "O(1) worst-case".
```

**Adversarial collisions are a real attack.** If an attacker knows your hash
function, they can craft keys that all collide → O(n) per op → algorithmic-complexity
DoS. The fix is a **randomized / keyed hash** (SipHash) chosen at startup, so the
adversary cannot predict the bucket mapping — directly connecting this structure to
`cryptography/` and to the randomized classes in `09`.

```
   OPEN-ADDRESSING PROBING (and clustering):
     linear probing:    h(k)+i        -> primary clustering (long runs)
     quadratic probing: h(k)+i^2      -> reduces clustering
     double hashing:    h1(k)+i*h2(k) -> best distribution
   Keep alpha well below 1 (e.g. <= 0.7) and resize early to keep probes short.
```

---

## Layer 4: Segment Trees and Fenwick Trees (range aggregates)

When you need *range queries* with *updates* — both in O(log n) — a flat array can't
do it (query O(n) or update O(n)). These structures get both to O(log n).

### Fenwick tree (Binary Indexed Tree) — prefix sums

```
   Supports: point-update + prefix-sum query, both O(log n). Tiny constants, array of size n.
   Each index i is responsible for a range of length (i & -i) (its lowest set bit).

   query(prefix sum up to i):  walk i -> i - (i & -i)  until 0   (sum the responsible ranges)
   update(point i, delta):     walk i -> i + (i & -i)  until > n (update all covering nodes)

   range sum [l..r] = prefix(r) - prefix(l-1).
   O(log n) per op, ~2x faster constant than a segment tree, but only invertible ops (sum/xor).
```

### Segment tree — any associative operation, with lazy propagation

```
   Supports ANY associative op (sum, min, max, gcd) over ranges. Range query + RANGE update.

   array [2, 5, 1, 4, 9, 3] -> segment tree storing range-mins (or sums):

                    [0..5] min=1
                  /              \
          [0..2] min=1         [3..5] min=3
          /     \               /      \
      [0..1]m=2  [2]=1      [3..4]m=4  [5]=3
      /    \                 /   \
   [0]=2  [1]=5           [3]=4  [4]=9

   query min over [1..4]: combine [1], [2], [3..4] = min(5,1,4) = 1   -> O(log n) nodes touched
   LAZY PROPAGATION: defer range-updates as a pending tag, push down only when needed
     -> range-update + range-query both O(log n).
```

```
   FENWICK vs SEGMENT TREE
   Fenwick   -> prefix/range of INVERTIBLE ops (sum, xor); smallest/fastest; point update
   Segment   -> ANY associative op (min/max/gcd); range update via lazy propagation; more memory
   neither   -> if static (no updates), a prefix-sum array is O(1) query, O(n) build
```

---

## Layer 5: Skip Lists (randomized ordered structure)

A skip list is a probabilistic alternative to a balanced BST: stacked linked lists
where each level skips ~half the nodes, giving expected O(log n) search without
rotations.

```
   level 3:  HEAD ----------------------------------> 9 -> NULL
   level 2:  HEAD --------> 3 ---------------------> 9 -> NULL
   level 1:  HEAD --> 1 --> 3 --------> 6 --------> 9 -> NULL
   level 0:  HEAD --> 1 --> 3 --> 4 --> 6 --> 8 --> 9 -> NULL

   each node promoted to the next level with prob 1/2  -> expected height O(log n)
   search 8: drop down from the top, advancing while next <= target  -> expected O(log n).
```

Skip lists trade worst-case guarantees for simplicity — no rotation logic, easy
lock-free concurrent variants (used in Redis sorted sets, LevelDB memtables). Like
treaps, the O(log n) is *expected*, not worst-case.

---

## Old World → New World Bridges

| You already know | The data structure |
|---|---|
| `Dictionary<K,V>` / `HashMap` "is O(1)" | Hash table — O(1) **amortized expected**, O(n) worst (collisions) |
| `SortedDictionary` / `TreeMap` | Balanced BST (red-black) — O(log n) worst, ordered iteration |
| A clustered/B-tree database index | B-tree/B+-tree — high fan-out to minimize disk/SSD I/Os |
| A `PriorityQueue` / task scheduler | Binary heap — O(log n) insert/extract, O(1) peek |
| Redis sorted set (ZSET) | Skip list — expected O(log n), concurrency-friendly |
| Range/prefix aggregate in OLAP | Fenwick/segment tree — O(log n) update + range query |
| Hash-flood DoS mitigation | Keyed/randomized hashing (SipHash) — see `cryptography/`, `09` |

The hash-map bridge is the load-bearing correction: an engineer who treats
`Dictionary` lookups as worst-case O(1) will mis-bound a latency SLA and miss the
hash-collision DoS surface — the *amortized expected* qualifier is operationally real.

---

## Decision Cheat Sheet

| I need... | Use | Bound |
|---|---|---|
| Fastest exact-match by key, no order | hash table | O(1) amortized expected |
| Worst-case lookup guarantee + ordering | balanced BST (red-black) | O(log n) worst |
| Ordered iteration / range / successor | balanced BST or B-tree | O(log n) worst |
| Disk/SSD-resident ordered index | B-tree / B+-tree | O(log_B n), few I/Os |
| Dynamic min/max (priority queue) | binary heap | O(log n) ins/extract |
| Many decrease-key ops (Dijkstra/Prim) | Fibonacci/pairing heap | O(1) amortized decrease-key |
| Prefix sums + point updates | Fenwick (BIT) | O(log n), tiny constant |
| Range query + range update, any assoc op | segment tree + lazy | O(log n) |
| Static range aggregates (no updates) | prefix-sum array / sparse table | O(1) query |
| Ordered structure, concurrency-friendly | skip list | O(log n) expected |
| Defend against hash-collision DoS | keyed hash (SipHash) | restores expected O(1) |

---

## Common Confusion Points

### "Hash tables are O(1)"

O(1) is **amortized expected** — *expected* over the hash (a colliding adversary
forces O(n)) and *amortized* over resizes (a single rehash is Θ(n)). The worst case
is O(n). For any latency-critical or adversarially-exposed path, quote the real
bound and use a keyed hash.

### "Build-heap is O(n log n)"

It is **O(n)**. Heapify from the bottom: nodes at height h number ≤ n/2^{h+1} and
each sifts ≤ h, so total work is `Σ_h (n/2^{h+1})·h = O(n)`. (Heap*sort* is O(n log n)
because the n *extract-min* operations dominate — different operation.)

### "AVL is strictly better than red-black because it's more balanced"

AVL's tighter balance gives faster *lookups* but more rotations on *writes*; red-black
trees rebalance less aggressively and win under write-heavy/mixed workloads — which is
why standard libraries (`std::map`, `TreeMap`) choose red-black. "More balanced" is a
trade-off, not a strict win.

### "Fibonacci heaps make Dijkstra faster, so always use them"

They improve the *asymptotic* bound (O(E + V log V)) via O(1) amortized decrease-key,
but their constants and pointer overhead are large; binary or pairing heaps usually
win in wall-clock for real graph sizes. The asymptotic improvement is real; the
practical default is not Fibonacci.

### "Segment tree and Fenwick tree are interchangeable"

Fenwick is smaller/faster but only handles *invertible* prefix operations (sum, xor)
with point updates. Segment trees handle *any associative* operation (min, max, gcd)
and support range updates via lazy propagation, at higher memory cost. Choose by
whether your operation is invertible and whether you need range updates.

### "A skip list's O(log n) is a guarantee"

It is **expected** (over the random level assignments), like a treap — not worst-case.
A pathological run of coin flips could degrade it. For a hard worst-case guarantee you
need a deterministic balanced BST (AVL/red-black).
