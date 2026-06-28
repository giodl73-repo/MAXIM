---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-COUNTING-BASICS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:counting-basics
kind: guide
module: combinatorics
section: combinatorics
title: Counting Basics and the Twelvefold Way
status: source-custody
source_custody: partial
current_path: combinatorics/01-COUNTING-BASICS.md
canonical_path: combinatorics/01-COUNTING-BASICS.md
backsource_ids: [proof-backfill:combinatorics:01-counting-basics, git-history:combinatorics:01-counting-basics]
concepts: [counting, permutations, combinations, twelvefold way, multisets]
root_concepts: [counting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Counting Basics and the Twelvefold Way

## The Big Picture

```
+============================================================================+
|              FROM TWO RULES TO THE TWELVEFOLD WAY                          |
+============================================================================+
|                                                                            |
|   RULE OF SUM                       RULE OF PRODUCT                        |
|   disjoint choices: A or B          sequential choices: A then B           |
|   |A| + |B|                          |A| * |B|                             |
|        \                                 /                                 |
|         \                               /                                  |
|          v                             v                                   |
|        .-----------------------------------.                               |
|        |  SELECTION:  pick k from n        |                               |
|        |                                   |                               |
|        |  ordered, no repeat ... P(n,k)    |                               |
|        |  ordered, repeat ....... n^k      |                               |
|        |  unordered, no repeat .. C(n,k)   |                               |
|        |  unordered, repeat ..... C(n+k-1,k)|                              |
|        '-----------------------------------'                               |
|                          |                                                 |
|                          v                                                 |
|        .-----------------------------------.                               |
|        |   THE TWELVEFOLD WAY              |                               |
|        |   functions f: [k] balls -> [n] boxes                             |
|        |   x {any, injective, surjective} |                                |
|        |   x {balls dist/same} x {boxes dist/same}                         |
|        |   = 12 cells                      |                               |
|        '-----------------------------------'                               |
+============================================================================+
```

Everything in enumerative combinatorics grows from **two rules** — sum and
product. Layer selection on top (ordered/unordered × with/without repetition)
and you get the four fundamental counts. Generalize "select k from n" to "place
k balls in n boxes" and you arrive at the **twelvefold way**, Gian-Carlo Rota's
unifying frame for elementary counting.

---

## Layer 1 — The Two Rules

```
+---------------------------------------------------------------+
|  RULE OF SUM (disjoint union)                                 |
|    If task can be done in EITHER way A (m ways) OR way B      |
|    (n ways), and the ways are disjoint, total = m + n.        |
|                                                               |
|  RULE OF PRODUCT (sequence)                                   |
|    If task is "do A (m ways) THEN B (n ways)" with the count  |
|    of B independent of the choice of A, total = m * n.        |
+---------------------------------------------------------------+
```

These are the additive and multiplicative structure of finite sets:
`|A ⊔ B| = |A| + |B|` and `|A × B| = |A|·|B|`. Every elementary count is a
nesting of these two, with **inclusion–exclusion** (`04`) handling the case
where the "or" is *not* disjoint.

**Old → new bridge.** This is exactly how you reason about state-space size: a
record with three independent fields of sizes m, n, p has `m·n·p` possible
values (product); a tagged union over disjoint variants has the *sum* of the
variant sizes. Counting and type cardinality are the same arithmetic — a sum
type's cardinality is the sum, a product type's is the product.

---

## Layer 2 — The Four Fundamental Counts

Select `k` items from a set of `n`. Two binary choices — does order matter, and
may items repeat — give four formulas.

```
                         REPETITION ALLOWED?
                    NO                      YES
              +-------------------+-------------------+
   ORDER  YES |  P(n,k)           |  n^k              |
   MATTERS    |  = n!/(n-k)!      |  k-tuples         |
              |  k-permutations   |  (functions)      |
              +-------------------+-------------------+
          NO  |  C(n,k)           |  C(n+k-1, k)      |
              |  = n!/(k!(n-k)!)  |  multisets        |
              |  k-subsets        |  "stars and bars" |
              +-------------------+-------------------+
```

| Count | Formula | Counts | Example (n=4, k=2) |
|-------|---------|--------|---------------------|
| Ordered, no repeat | `n!/(n-k)!` | k-permutations | `4·3 = 12` |
| Ordered, repeat | `n^k` | k-tuples / functions | `4^2 = 16` |
| Unordered, no repeat | `C(n,k)` | k-subsets | `C(4,2) = 6` |
| Unordered, repeat | `C(n+k-1,k)` | k-multisets | `C(5,2) = 10` |

### Permutations and the factorial

A permutation of `n` distinct objects is an ordered arrangement: `n!` of them.
A **k-permutation** arranges `k` of the `n`: `P(n,k) = n·(n-1)···(n-k+1) =
n!/(n-k)!`. The factorial is the engine; everything else divides it down.

### Combinations: divide out the order

`C(n,k)` (the **binomial coefficient**, read "n choose k") counts k-subsets.
Derivation: each k-subset can be ordered in `k!` ways, so
`C(n,k)·k! = P(n,k)`, giving `C(n,k) = n!/(k!(n-k)!)`. This division-by-symmetry
move — count ordered, divide by the size of each equivalence class — is the
single most reused step in counting. (Its full generalization is the
orbit-counting / Burnside machinery in `abstract-algebra/`.)

### Multisets and stars and bars

How many ways to choose `k` items from `n` types **with repetition, order
irrelevant**? Equivalently: nonnegative integer solutions to
`x_1 + x_2 + ... + x_n = k`. Encode a solution as `k` stars and `n-1` bars:

```
   x_1=2, x_2=0, x_3=3   for n=3, k=5:

      * *  |  |  * * *
      ^^^^    ^^^^^^^
      two    (zero)   three

   k stars + (n-1) bars in a row, choose which (n-1) of the
   (n+k-1) positions are bars:   C(n+k-1, n-1) = C(n+k-1, k).
```

This bijection — **stars and bars** — is the workhorse for counting
distributions of identical items, monomials of degree k in n variables, and
nonnegative integer solutions of a single linear equation.

---

## Layer 3 — The Twelvefold Way

Rota observed that "place `k` balls into `n` boxes" — equivalently, count
functions `f: [k] → [n]` — unifies elementary counting. Two binary distinctions
(are the **balls** distinguishable? are the **boxes** distinguishable?) times
three constraints on `f` (any / injective / surjective) give **twelve** cells.

```
+======================================================================+
|  f : [k] balls --> [n] boxes                                         |
+======================================================================+
|  BALLS    BOXES    | ANY f          | INJECTIVE      | SURJECTIVE    |
|  (k)      (n)      | (<=1 not req)  | (<=1 per box)  | (>=1 per box) |
+--------------------+----------------+----------------+---------------+
|  distinct distinct | n^k            | n!/(n-k)!      | n! S(k,n)     |
|  same    distinct  | C(n+k-1, k)    | C(n, k)        | C(k-1, n-1)   |
|  distinct same     | SUM_{j} S(k,j) | [k<=n]         | S(k, n)       |
|  same    same      | p_{<=n}(k)     | [k<=n]         | p_n(k)        |
+--------------------+----------------+----------------+---------------+
|  S(k,n) = Stirling 2nd kind;  p_n(k) = partitions of k into n parts  |
|  [P] = 1 if P true else 0;  SUM_j S(k,j) = Bell number B_k           |
+======================================================================+
```

Reading the cells (these are derived, not memorized):

| Cell | Why |
|------|-----|
| dist/dist, any = `n^k` | each of k balls independently picks one of n boxes |
| dist/dist, injective = `P(n,k)` | balls distinct, no box reused: ordered selection |
| dist/dist, surjective = `n! S(k,n)` | partition k balls into n nonempty groups, then label groups |
| same/dist, any = `C(n+k-1,k)` | stars and bars |
| same/dist, injective = `C(n,k)` | choose which k of n boxes get a ball |
| same/dist, surjective = `C(k-1,n-1)` | compositions: stars and bars with each box ≥ 1 |
| dist/same, surjective = `S(k,n)` | set partitions of [k] into exactly n blocks |
| dist/same, any = `B_k` | sum over block counts: the Bell number |
| same/same, surjective = `p_n(k)` | integer partitions of k into exactly n parts |
| same/same, any = `p_{≤n}(k)` | partitions of k into at most n parts |
| injective + same balls = `[k≤n]` | identical balls, ≤1 per box: only the indicator survives |

The Stirling, Bell, and partition numbers in the bottom rows are developed in
`07-SPECIAL-NUMBERS.md`. The point here: **all twelve are reachable from the two
rules plus a bijection.** The "balls same → boxes same" column shows why
partitions (of sets and of integers) are the natural endpoint of counting when
you erase labels.

---

## Worked Counts (verify the formulas)

```
+---------------------------------------------------------------+
|  Q1. License plates: 3 letters then 4 digits, repeats OK.     |
|      26^3 * 10^4 = 17,576 * 10,000 = 175,760,000.             |
|      (product rule, ordered with repetition)                  |
|                                                               |
|  Q2. Committees of 3 from 10 people.                          |
|      C(10,3) = 120.   (unordered, no repeat)                  |
|                                                               |
|  Q3. Ways to write 7 as an ordered sum of 3 positive parts    |
|      (compositions): C(7-1, 3-1) = C(6,2) = 15.               |
|                                                               |
|  Q4. Nonneg integer solutions to a+b+c+d = 10:                |
|      C(10+4-1, 10) = C(13,3) = 286.   (stars and bars)        |
|                                                               |
|  Q5. Surjections from 4 distinct balls onto 2 distinct boxes: |
|      2! * S(4,2) = 2 * 7 = 14.                                |
|      (or 2^4 - 2 = 14 by inclusion-exclusion, see file 04)    |
+---------------------------------------------------------------+
```

Note Q5 cross-checks the twelvefold formula `n! S(k,n)` against the
inclusion–exclusion count `n^k - C(n,1)(n-1)^k + ...` of `04` — `14` both ways.
Consistency across methods is how you trust a count.

---

## Old World → New World Bridges

| You know (engineering) | Maps to (combinatorics) |
|------------------------|--------------------------|
| Cartesian product of fields | Rule of product, `n^k` |
| Tagged union / discriminated union size | Rule of sum |
| Number of distinct query plans / orderings | Permutations `P(n,k)` |
| Choosing a subset of feature flags | Combinations `C(n,k)` |
| Distributing N identical tasks to W workers | Stars and bars |
| Hash function `f: keys → buckets` | Functions `[k] → [n]`, the `n^k` cell |
| Counting onto mappings (every bucket hit) | Surjections, `n! S(k,n)` |

The twelvefold way is, viewed through a CS lens, a complete taxonomy of
**functions between finite sets up to relabeling of domain and/or codomain** —
which is exactly what you reason about when you ask "how many distinct hash
distributions / load assignments / type inhabitants are there."

---

## Decision Cheat Sheet

| The objects are... | and you... | Count |
|--------------------|------------|-------|
| ordered, distinct | take all n | `n!` |
| ordered, distinct | take k of n | `P(n,k) = n!/(n-k)!` |
| ordered, repeats OK | take k | `n^k` |
| unordered, distinct | take k of n | `C(n,k)` |
| unordered, repeats OK | take k of n types | `C(n+k-1,k)` |
| identical balls → distinct boxes | any placement | `C(n+k-1,k)` |
| identical balls → distinct boxes | ≥1 per box | `C(k-1,n-1)` |
| distinct balls → distinct boxes | onto | `n! S(k,n)` |
| distinct balls → identical boxes | any | Bell `B_k` |
| identical balls → identical boxes | any | `p_{≤n}(k)` |

---

## Common Confusion Points

### "Do I use n^k or C(n,k)? They feel similar."

Order and repetition decide. `n^k` = ordered with repetition (k independent
slots, each n choices). `C(n,k)` = unordered without repetition (a subset). If
you find yourself dividing `n^k` (or `P(n,k)`) by some symmetry factor, you are
on the path to `C(n,k)` or a multinomial coefficient — that division-by-symmetry
is the tell.

### "Stars and bars gives C(n+k-1, k) — but I keep getting C(n+k-1, n)."

They are equal: `C(n+k-1, k) = C(n+k-1, n-1)`. Choosing which positions are
stars is complementary to choosing which are bars. Both are correct; pick the
one whose "choose" parameter matches what you are placing.

### "Why is the surjection count n! · S(k,n) and not just S(k,n)?"

`S(k,n)` (Stirling 2nd kind) counts partitions of the k balls into n *unlabeled*
nonempty blocks. If the boxes are **distinct**, you must then assign the n blocks
to the n boxes: `n!` ways. So distinct boxes → multiply by `n!`; identical boxes
→ leave it as `S(k,n)`. This is the dist/same vs dist/dist distinction in the
twelvefold table.

### "Permutations of a multiset?"

If you arrange `n` items where there are `n_1` copies of type 1, `n_2` of type 2,
..., the count is the **multinomial** `n! / (n_1! n_2! ... n_m!)` — you divide
out the indistinguishable orderings within each type. (Full treatment of
multinomials is in `02-BINOMIAL-AND-IDENTITIES.md`.) Classic instance: distinct
arrangements of MISSISSIPPI = `11! / (4! 4! 2! 1!) = 34,650`.
