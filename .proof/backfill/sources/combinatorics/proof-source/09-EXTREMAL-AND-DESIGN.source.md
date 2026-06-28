---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-EXTREMAL-AND-DESIGN.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:extremal-and-design
kind: guide
module: combinatorics
section: combinatorics
title: Extremal Combinatorics and Design Theory
status: source-custody
source_custody: partial
current_path: combinatorics/09-EXTREMAL-AND-DESIGN.md
canonical_path: combinatorics/09-EXTREMAL-AND-DESIGN.md
backsource_ids: [proof-backfill:combinatorics:09-extremal-and-design, git-history:combinatorics:09-extremal-and-design]
concepts: [turan, dilworth, sperner, erdos-ko-rado, latin squares, block designs, coding theory]
root_concepts: [extremal combinatorics]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Extremal Combinatorics and Design Theory

## The Big Picture

```
+==============================================================================+
|       EXTREMAL: HOW LARGE/SMALL UNDER A CONSTRAINT?                          |
|       DESIGN: HOW TO ARRANGE WITH PERFECT BALANCE?                           |
+==============================================================================+
|                                                                              |
|   EXTREMAL GRAPH/SET THEORY          DESIGN THEORY                           |
|   .-------------------------.        .---------------------------.           |
|   | Turan:  max edges with  |        | Latin squares: n-symbol   |           |
|   |   no K_{r+1}            |        |   grid, each symbol once   |          |
|   |   = (1-1/r) n^2/2       |        |   per row & column         |          |
|   | Dilworth: poset = union |        | Block designs (BIBD):     |           |
|   |   of (width) chains     |        |   v points, blocks of k,   |          |
|   | Sperner: max antichain  |        |   every pair in lambda     |          |
|   |   in 2^[n] = C(n, n/2)  |        |   blocks                   |          |
|   | Erdos-Ko-Rado: max      |        | Steiner systems S(t,k,v)  |           |
|   |   intersecting k-family  |        |   t-subsets each in 1 blk  |         |
|   |   = C(n-1, k-1)         |        | Projective/affine planes  |           |
|   '-------------------------'        '---------------------------'           |
|                |                              |                              |
|                '--------------+---------------'                              |
|                               v                                              |
|             CODING-THEORY BRIDGE: designs <-> codes <-> packings             |
|             Hamming/Reed-Muller, Singleton & Gilbert-Varshamov bounds        |
|             (cross: cryptography/, abstract-algebra/ finite fields)          |
+==============================================================================+
```

Two faces of "structure under constraint." **Extremal combinatorics** asks for
the maximum (or minimum) size of a structure avoiding a forbidden configuration —
and characterizes the optimum. **Design theory** asks for arrangements with
*perfect balance* (every pair covered equally often), which turns out to be the
same mathematics as error-correcting codes. Both lean on finite-field algebra
(`abstract-algebra/`) and bridge directly to coding theory (`cryptography/`).

---

## Layer 1 — Turán's Theorem (the foundational extremal result)

```
   QUESTION: max # of edges in an n-vertex graph with NO clique K_{r+1}?

   TURAN (1941): the unique maximizer is the TURAN GRAPH T(n,r) --
   the complete r-partite graph with parts as equal as possible.
   Its edge count is
        ex(n, K_{r+1}) = (1 - 1/r) * n^2 / 2.

   r = 2 case (no triangle) = MANTEL'S THEOREM:
        max edges with no K_3  =  n^2 / 4
        achieved by the balanced complete bipartite graph K_{n/2, n/2}.
```

**Proof sketch (one of many).** A `K_{r+1}`-free graph's edge count is maximized
by making it complete `r`-partite (any non-edge inside a part can be improved by
moving a vertex to its higher-degree side), and balancing the parts maximizes
edges among `r`-partite graphs (convexity). The extremal object is *unique* and
*explicit* — the hallmark of a clean extremal theorem.

Turán's theorem launched extremal graph theory; its density version (the
**Erdős–Stone–Simonovits theorem**) gives the asymptotic edge threshold for
forbidding *any* fixed subgraph `H` in terms of its chromatic number. Bridges to
`graph-algorithms/` (cliques, independent sets) and to the probabilistic method
(`08`, independent-set lower bounds are Turán-dual).

---

## Layer 2 — Order-Theoretic Extremal Results

### Dilworth's theorem (chains and antichains)

```
   In any finite POSET:
        minimum # of CHAINS needed to cover all elements
        =  maximum size of an ANTICHAIN (the "width").

   Dual (Mirsky): min # of antichains covering = longest chain (height).

   CONSEQUENCE (Erdos-Szekeres again, file 06): any sequence of >n^2
   reals has a monotone subsequence of length > n -- via Dilworth on
   the dominance order.
```

Dilworth is a **min–max theorem** — the combinatorial cousin of LP duality and
max-flow/min-cut (`graph-algorithms/`). Indeed it is equivalent to König's
theorem on bipartite matchings; chains-covering-a-poset is a matching problem in
disguise.

### Sperner's theorem (largest antichain in the subset lattice)

```
   The largest ANTICHAIN in the Boolean lattice 2^[n] (no set contains
   another) is the middle layer:
        max size = C(n, floor(n/2)).

   PROOF (symmetric chain decomposition / LYM inequality):
        SUM over an antichain F of  1 / C(n, |A|)  <= 1   (LYM)
        => |F| <= C(n, n/2) since the middle binomial is largest.
```

The **LYM inequality** (Lubell–Yamamoto–Meshalkin) is the slick proof: each set
sits on a maximal chain, chains are disjointly counted, and the middle layer
saturates the bound. A model "weight each object by its chain-share" argument.

---

## Layer 3 — Erdős–Ko–Rado (intersecting families)

```
   QUESTION: largest family of k-subsets of [n] such that EVERY TWO
   sets intersect?  (n >= 2k, else all k-sets trivially intersect.)

   ERDOS-KO-RADO (1961):  the maximum is  C(n-1, k-1),
   achieved by the "star" -- ALL k-sets containing one fixed element.

   For n > 2k the star is the UNIQUE optimum (up to relabeling).
```

The star is the obvious intersecting family (everyone shares the fixed point);
EKR says nothing beats it. The classic proof is **Katona's cyclic permutation
argument**: arrange `[n]` on a circle; in any cyclic order only `k` of the
`n` intervals of length `k` can pairwise intersect, and averaging over all
`(n-1)!` cyclic orders yields the bound. EKR is the prototype of
**intersection theorems** — a large subfield (Frankl, Wilson, the
Frankl–Rödl and Ahlswede–Khachatrian extensions).

---

## Layer 4 — Design Theory

A **combinatorial design** is an arrangement of points into blocks with uniform
balance — every `t`-subset covered the same number of times.

```
   BALANCED INCOMPLETE BLOCK DESIGN  (v, k, lambda)-BIBD:
   * v points, blocks each of size k,
   * every PAIR of points lies in exactly lambda blocks.
   Counting (necessary conditions):
       each point in r = lambda(v-1)/(k-1) blocks,
       total blocks b = v r / k = lambda v(v-1)/(k(k-1)).
   (r, b must be integers -- divisibility constraints on (v,k,lambda).)

   STEINER SYSTEM S(t, k, v): every t-subset in EXACTLY ONE block.
   * S(2,3,v) = Steiner triple system; exists iff v = 1 or 3 (mod 6).
   * S(5,8,24) = the Witt design, tied to the Mathieu group M_24
     and the binary Golay code.
```

### Latin squares and orthogonality

```
   LATIN SQUARE of order n: an n x n grid filled with n symbols so each
   symbol appears once per row and once per column. (= multiplication
   table of a quasigroup; Cayley table of a group is one example.)

   Two Latin squares are ORTHOGONAL (a Graeco-Latin square) if
   superimposing them yields all n^2 ordered symbol-pairs once.
   A complete set of n-1 mutually orthogonal Latin squares (MOLS)
   EXISTS iff a projective plane of order n exists -- known for all
   prime powers n; OPEN/known-impossible for some others (no order-6
   pair -- Euler's "36 officers"; no order-10 projective plane, by a
   massive computation).
```

Designs are built from **finite fields** (`abstract-algebra/`): the points and
lines of a projective plane `PG(2,q)` form an `S(2, q+1, q^2+q+1)` Steiner
system, giving a Graeco-Latin construction for every prime-power order.

---

## Layer 5 — The Coding-Theory Bridge

Designs, codes, and sphere packings are three views of one object. This is the
cleanest CS bridge in the directory.

```
+---------------------------------------------------------------------+
|  DESIGN  <-->  CODE  <-->  PACKING                                  |
|                                                                     |
|  An error-correcting code is a set of codewords (points in F_q^n)   |
|  pairwise far apart in HAMMING distance. The codewords of many      |
|  optimal codes form (or come from) combinatorial designs.           |
|                                                                     |
|  * Hamming code [7,4,3]: its codewords/supports give the Fano       |
|    plane = S(2,3,7) Steiner triple system.                          |
|  * Golay [24,12,8] code: cosets give the S(5,8,24) Witt design.     |
|  * Reed-Muller / Reed-Solomon: polynomial evaluation codes,         |
|    built on finite-field structure.                                 |
|                                                                     |
|  KEY BOUNDS (extremal flavor):                                      |
|    Singleton:        d <= n - k + 1   (MDS codes meet it)           |
|    Hamming (sphere): packing bound on # codewords vs radius         |
|    Gilbert-Varshamov: EXISTENCE bound -- good codes exist           |
|       (proved by the probabilistic / greedy method, file 08)        |
+---------------------------------------------------------------------+
```

The **Gilbert–Varshamov bound** is a probabilistic-method existence result
(`08`): a greedy/random construction shows codes of guaranteed rate and distance
*exist*, while explicit constructions matching it are a long-standing pursuit —
the same exists-vs-construct tension as the Ramsey lower bound (`06`). Full
treatment of the codes themselves: `cryptography/`. The finite-field algebra:
`abstract-algebra/`.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Max-flow/min-cut, LP duality | Dilworth's min–max theorem |
| Bipartite matching (König) | Dilworth equivalent / chain covers |
| Hamming distance, parity-check codes | design–code correspondence |
| Test-coverage "every pair of params covered" | covering designs / orthogonal arrays |
| Sudoku / scheduling constraints | Latin squares (each symbol once per line) |
| RAID parity / erasure coding | MDS codes, Singleton bound |

**CS bridge — combinatorial testing.** **Orthogonal arrays** (close kin of MOLS
and BIBDs) are exactly the structures behind *pairwise / t-wise combinatorial
testing*: cover every combination of `t` parameter values in as few test cases as
possible. The same designs schedule tournaments, allocate experiments
(statistical DOE, `probability-statistics/`), and lay out erasure-coded storage.

---

## Decision Cheat Sheet

| I want... | Result |
|-----------|--------|
| Max edges with no `K_{r+1}` | Turán: `(1-1/r)n²/2`, Turán graph |
| Max edges with no triangle | Mantel: `n²/4`, `K_{n/2,n/2}` |
| Min chains covering a poset | Dilworth: = width (max antichain) |
| Largest antichain in `2^[n]` | Sperner: `C(n,⌊n/2⌋)` |
| Largest pairwise-intersecting `k`-family | Erdős–Ko–Rado: `C(n-1,k-1)` (star) |
| Every pair covered `λ` times | `(v,k,λ)`-BIBD |
| Every `t`-subset in exactly one block | Steiner system `S(t,k,v)` |
| Grid with each symbol once per line | Latin square; orthogonal pair = MOLS |
| Code existence at given rate/distance | Gilbert–Varshamov (probabilistic, `08`) |
| Max distance for given `n,k` | Singleton bound `d ≤ n-k+1`, MDS codes |

---

## Common Confusion Points

### "Extremal vs design theory — why are these one chapter?"

Both ask "structure under a rigid constraint," and the answers interlock: the
*existence* of designs (Steiner systems, MOLS) is itself an extremal/packing
question, and bounds like Fisher's inequality (`b ≥ v` for a `2`-design) are
extremal statements about designs. The unifying object is the incidence structure
(points × blocks), studied for its maxima (extremal) and its perfect balance
(design). Coding theory is the third vertex of the same triangle.

### "Dilworth's theorem — is it just about sorting?"

It is a general **min–max duality** on partial orders: minimum chain cover =
maximum antichain. Sorting/monotone-subsequence results (Erdős–Szekeres) are
*corollaries*, obtained by applying Dilworth to a specific poset (the dominance
order on a sequence). The theorem itself is equivalent to König's bipartite
matching theorem and sits alongside max-flow/min-cut in the family of
combinatorial dualities.

### "Why do projective planes only exist for prime-power orders?"

Existence is *known* for every prime-power order `q` (build from the finite field
`GF(q)`); for non-prime-powers it is mostly open, with key impossibilities proved
(no plane of order 6 by the Bruck–Ryser theorem, no order 10 by exhaustive
computation). The deep link is that a projective plane of order `n` is equivalent
to a complete set of `n-1` mutually orthogonal Latin squares — so the same
divisibility/algebraic obstructions govern both. The general existence question
remains unsolved.

### "Erdős–Ko–Rado needs n ≥ 2k — why?"

If `n < 2k`, *any* two `k`-subsets of `[n]` must overlap (their sizes sum past
`n`), so the maximum intersecting family is trivially *all* `C(n,k)` of them and
the theorem says nothing new. EKR's content — that the star `C(n-1,k-1)` is
optimal — is meaningful precisely when `n ≥ 2k`, where non-intersecting `k`-sets
exist and the constraint bites. For `n > 2k` the star is moreover the *unique*
optimum.
