---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-PROBABILISTIC-METHOD.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:probabilistic-method
kind: guide
module: combinatorics
section: combinatorics
title: The Probabilistic Method
status: source-custody
source_custody: partial
current_path: combinatorics/08-PROBABILISTIC-METHOD.md
canonical_path: combinatorics/08-PROBABILISTIC-METHOD.md
backsource_ids: [mdloom-backfill:combinatorics:08-probabilistic-method, git-history:combinatorics:08-probabilistic-method]
concepts: [probabilistic method, first moment, second moment, lovasz local lemma, alteration]
root_concepts: [probabilistic method]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Probabilistic Method

## The Big Picture

```
+=============================================================================+
|     PROVE EXISTENCE BY SHOWING A RANDOM OBJECT WORKS                        |
+=============================================================================+
|                                                                             |
|   THE CORE LOGIC                                                            |
|   Build a RANDOM object X. If Pr[X is good] > 0, a good object EXISTS.      |
|                                                                             |
|   FIRST MOMENT             SECOND MOMENT            LOVASZ LOCAL LEMMA      |
|   E[X] argument            Var(X) argument          (LLL)                   |
|        |                        |                       |                   |
|   * E[X] < 1 => some          * X concentrates       * many "bad" events    |
|     outcome has X=0             near E[X] if Var       each rare, weakly    |
|   * E[X] >= t => some          is small (Chebyshev)   dependent => all      |
|     outcome has X>=t           => existence of a       avoidable AT ONCE    |
|     ("averaging")              "typical" object        Pr > 0 even when     |
|        |                        |                       union bound fails   |
|        v                        v                       |                   |
|   ALTERATION (delete-defects):  build random, then remove the few bad       |
|   parts; what remains is good and still large.                              |
|        |                                                                    |
|        v                                                                    |
|   DERANDOMIZE: method of conditional expectations -> explicit algorithm.    |
+=============================================================================+
```

Erdős's idea: to prove an object with property `P` exists, define a *random*
object and show `Pr[P] > 0`. Since the sample space is nonempty wherever the
probability is positive, **some** object has `P` — even though you never exhibit
one. This non-constructive move is the most powerful existence technique in
combinatorics, and (via derandomization) a generator of real algorithms.

We use probability here as a *tool*; the underlying theory (expectation,
variance, concentration) lives in `probability-statistics/`. This file is about
the combinatorial *method*.

---

## Layer 1 — The First Moment Method

```
   TWO COMPLEMENTARY FORMS (X a nonnegative integer random variable):

   (a)  If E[X] < 1, then Pr[X = 0] > 0
        => some outcome has X = 0  (no bad events occurred).

   (b)  There is always an outcome with X >= E[X], and one with
        X <= E[X]  ("an object at least as good as average exists").

   The whole power is in choosing X to COUNT the defects (form a) or
   the GOODNESS (form b).
```

### Application: Ramsey lower bound `R(s,s) > 2^{s/2}`

```
   Randomly 2-color K_n (each edge red/blue independently, prob 1/2).
   Let X = number of monochromatic s-cliques.
   A fixed s-subset is mono with prob 2 * (1/2)^{C(s,2)} = 2^{1-C(s,2)}.
   By LINEARITY of expectation (no independence needed!):
       E[X] = C(n,s) * 2^{1 - C(s,2)}.
   If E[X] < 1, some coloring has X = 0 => no mono s-clique => R(s,s) > n.
   Solving C(n,s) 2^{1-C(s,2)} < 1 gives  n ~ 2^{s/2}.   QED.
```

The lever is **linearity of expectation** — `E[ΣX_i] = ΣE[X_i]` holds with *no
independence assumption*, which is why the method is so robust. This 1947 bound
(`06`) is still essentially the best known lower bound on diagonal Ramsey numbers.

### Application: every graph has a large bipartite subgraph

```
   Put each vertex independently into side L or R with prob 1/2.
   An edge is "cut" iff its endpoints land on opposite sides: prob 1/2.
   E[# cut edges] = m/2.  By form (b), SOME partition cuts >= m/2 edges.
   => every graph has a bipartite (cut) subgraph with >= half its edges.
```

A clean, tight existence result (Max-Cut ≥ m/2) from one expectation. Cross-
reference `graph-algorithms/` (Max-Cut, the GW SDP approximation that improves
the constant).

---

## Layer 2 — The Second Moment Method

The first moment shows a *good* object exists; the second moment shows the random
object is *typically* good — it controls the variance so `X` concentrates near
`E[X]`.

```
   CHEBYSHEV:  Pr[ |X - E[X]| >= t ] <= Var(X) / t^2.

   KEY COROLLARY (for nonnegative X):
       if Var(X) = o(E[X]^2), then Pr[X = 0] -> 0
       => X > 0 almost surely for large n  (the good event is TYPICAL).

   Used to prove THRESHOLDS: a property appears suddenly as a parameter
   crosses a critical value (e.g. random graph G(n,p) contains a fixed
   subgraph H once p exceeds the threshold p* = n^{-1/m(H)}).
```

The first moment alone can be misleading: `E[X]` may be large while `X = 0` with
high probability (the expectation carried by rare huge values). The second moment
rules this out — bounding `Var(X)` forces `X` to cluster around `E[X]`, so
`E[X] → ∞` plus small variance gives `X > 0` whp. This is the engine behind
**threshold phenomena** in random structures (`probability-statistics/`,
random-graph theory).

---

## Layer 3 — The Alteration (Deletion) Method

When a purely random object has *a few* defects, **build it randomly, then delete
the defective parts.** What remains is defect-free and, if defects were rare,
still large.

```
   RAMSEY, SHARPENED via alteration:
   Random 2-color K_n; expected # mono s-cliques = E[X].
   DELETE one vertex from each mono clique. Remaining graph (n - X
   vertices) has NO mono s-clique. Choosing n to balance n vs E[X]
   gives a BETTER bound than the pure first-moment R(s,s) > 2^{s/2}.

   INDEPENDENT SETS:
   Graph with n vertices, m edges. Sample each vertex w.p. p; delete one
   endpoint of every surviving edge. Expected survivors >= pn - p^2 m;
   optimize p => independent set of size >= n^2/(4m)  (Turan-type bound).
```

Alteration trades a clean random object for a slightly trimmed one with a
*guaranteed* property — often the difference between a weak and a sharp bound.

---

## Layer 4 — The Lovász Local Lemma

The union bound (`Pr[∪ bad events] ≤ Σ Pr`) fails when there are many bad
events: the sum exceeds 1. The **Lovász Local Lemma (LLL)** rescues existence
when each bad event is *rare* and *weakly dependent* on the others.

```
   SYMMETRIC LLL.  Suppose each bad event A_i:
     (1) has Pr[A_i] <= p,
     (2) is mutually independent of all but <= d of the other events.
   If   e * p * (d + 1) <= 1   (e = 2.718...),
   then Pr[ NONE of the A_i occur ] > 0   => a good outcome EXISTS.
```

The crucial difference from the union bound: LLL cares about the **dependency
degree `d`**, not the total number of events. Even with exponentially many bad
events, if each touches only `d = O(1)` others and each is rare, all are
simultaneously avoidable.

```
   CLASSIC APPLICATION (k-SAT):
   A k-CNF formula where every clause shares variables with <= 2^k / e - 1
   other clauses is SATISFIABLE. (Bad event = "clause j unsatisfied" under
   a random assignment; Pr = 2^{-k}; dependency degree = clause overlap.)
   => sparse k-SAT instances are always satisfiable.
```

The **Moser–Tardos algorithm** (2010) made the LLL *constructive*: a simple
randomized "resample any violated clause" loop terminates in polynomial expected
time, turning the existence proof into an efficient algorithm — a landmark
derandomization-style result.

---

## Layer 5 — From Existence to Algorithm (Derandomization)

```
   METHOD OF CONDITIONAL EXPECTATIONS
   A first-moment proof says E[X] hits a good value. Decide the random
   choices ONE AT A TIME, always choosing the option that keeps the
   conditional expectation on the good side:

      E[X] = p*E[X | choice=A] + (1-p)*E[X | choice=B]
             => one of the two conditionals is at least E[X].
             Pick that branch. Repeat.

   After all choices are fixed, X is at least E[X] -- a DETERMINISTIC,
   polynomial-time construction of the object the probabilistic proof
   only promised existed.
```

This is the bridge from "exists" to "here it is." The Max-Cut ≥ m/2 existence
proof (Layer 1) derandomizes directly into a greedy linear-time algorithm: place
each vertex on the side that cuts more of its already-placed edges. Existence
proof and algorithm are two readings of the same expectation.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Monte Carlo "if a random sample passes, valid configs exist" | first moment, `Pr > 0` |
| Randomized algorithm correctness (RP/BPP) | the method's algorithmic face |
| Hash-collision / load-balance "whp" analysis | second moment / concentration |
| Greedy that beats the average | derandomized first-moment argument |
| Retry-on-conflict loops (e.g. lock backoff) | Moser–Tardos LLL algorithm |

**CS bridge.** The probabilistic method *is* the analysis of randomized
algorithms read backwards: a randomized algorithm that outputs a good object with
positive probability is an existence proof, and a derandomization (conditional
expectations, pessimistic estimators, `k`-wise independence) converts it to a
deterministic one. Expander graphs, error-correcting codes near the Gilbert–
Varshamov bound (`09`, `cryptography/`), and hashing schemes all have their best-
known *existence* results via this method, with constructive matches a major
research frontier.

---

## Decision Cheat Sheet

| I want to prove... | Use |
|--------------------|-----|
| An object with property `P` exists | First moment: show `Pr[P] > 0` |
| An object beating the average exists | First moment form (b): `∃ X ≥ E[X]` |
| No bad event occurs in *some* outcome | First moment: `E[#bad] < 1` |
| The random object is *typically* good | Second moment: `Var = o(E²)` |
| A sharp bound where pure random is loose | Alteration (delete defects) |
| All of *many* weakly-dependent bad events avoidable | Lovász Local Lemma |
| Turn an existence proof into an algorithm | Conditional expectations / Moser–Tardos |
| Lower bound a Ramsey number | First moment / alteration (`06`) |

---

## Common Confusion Points

### "If it's only existence, what good is it?"

Two answers. First, existence is often *exactly* the question (does a graph with
these extremal properties exist? is this sparse formula satisfiable?). Second,
many probabilistic proofs **derandomize** into explicit polynomial-time
algorithms via conditional expectations or Moser–Tardos — so "exists" frequently
upgrades to "and here is how to build it efficiently." The Ramsey lower bound is
the famous case where derandomization remains *open*, which is precisely why it
is celebrated.

### "First moment or second moment?"

**First moment** answers existence ("does a good object exist?") via `E[X]`.
**Second moment** answers typicality ("is the random object *usually* good, and
in particular is `X > 0` whp?") via `Var(X)`. If `E[X] → ∞` but you need to rule
out `X = 0`, the first moment is *not enough* (large mean can hide on rare
outcomes) — you must bound the variance. Thresholds in random graphs are the
canonical second-moment application.

### "Why does linearity of expectation not need independence?"

`E[X + Y] = E[X] + E[Y]` is a property of *integration*, true for any joint
distribution — correlated or not. This is what makes the first-moment method so
forgiving: in the Ramsey and Max-Cut proofs the indicator events are highly
dependent, yet `E[ΣX_i] = ΣE[X_i]` holds regardless. *Variance* and the LLL, by
contrast, *do* care about dependence — hence the `d` parameter in the LLL.

### "Union bound vs Lovász Local Lemma?"

The **union bound** proves all bad events avoidable when `Σ Pr[A_i] < 1` — it
fails the moment the bad events are numerous (sum exceeds 1), regardless of how
they interact. The **LLL** instead requires each event to be rare *and* depend on
few others (`e·p·(d+1) ≤ 1`), succeeding with arbitrarily many bad events so long
as the dependency graph is sparse. Use the union bound when events are few; reach
for the LLL when there are many but each is "local."
