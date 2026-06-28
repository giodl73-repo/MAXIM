---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:complexity-and-np
kind: guide
module: algorithms
section: mathematics-physics
title: Complexity and NP
status: source-custody
source_custody: partial
current_path: algorithms/09-COMPLEXITY-AND-NP.md
canonical_path: algorithms/09-COMPLEXITY-AND-NP.md
backsource_ids: [proof-backfill:algorithms:09-complexity-and-np, git-history:algorithms:09-complexity-and-np]
concepts: [P, NP, co-NP, NP-completeness, reductions, approximation algorithms, randomized algorithms, PSPACE]
root_concepts: [computational complexity]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Complexity and NP

This is the boundary of the directory: which problems the preceding paradigms can
solve efficiently, and which are provably (or conjecturally) beyond *exact efficient*
solution. You know the definitions of P, NP, and reductions; this guide is about
*using* them — building reductions to prove hardness, and the three escape routes
when a problem is NP-hard: approximation algorithms with proven ratios, randomization,
and parameterization. Every class and reduction direction below is stated precisely,
because the entire field turns on getting the direction of a reduction right.

```
  THE COMPLEXITY LANDSCAPE
  =====================================================================================

   +-----------------------------------------------------------------------------+
   |                              PSPACE                                          |
   |   +-------------------------------------------------------------------+      |
   |   |                        NP            co-NP                        |      |
   |   |   +---------------------------+   +---------------------------+   |      |
   |   |   |          NP-complete      |   |       co-NP-complete      |   |      |
   |   |   |   SAT, 3-SAT, CLIQUE,     |   |   TAUTOLOGY, UNSAT        |   |      |
   |   |   |   VERTEX-COVER, HAM-CYCLE,|   |                           |   |      |
   |   |   |   TSP(dec), SUBSET-SUM,   |   |                           |   |      |
   |   |   |   3-COLORING, KNAPSACK    |   |                           |   |      |
   |   |   +---------------------------+   +---------------------------+   |      |
   |   |               \           +-----+           /                    |      |
   |   |                \          |  P  |          /                     |      |
   |   |                 \         |     |         /                      |      |
   |   |   NP-intermediate?\       | sort| (poly)/   if P=NP this all     |      |
   |   |   (factoring, GI) +-------|  MST|------+    collapses to P        |      |
   |   |                           |  LP |                                |      |
   |   |                           +-----+                                |      |
   |   +-------------------------------------------------------------------+      |
   +-----------------------------------------------------------------------------+

   P        solvable in poly time            (decision problems)
   NP       VERIFIABLE in poly time (given a certificate)        P subset NP
   co-NP    complement is in NP (verify a NO)
   NP-hard  everything in NP reduces to it (>= as hard as all of NP)
   NP-COMPLETE  in NP AND NP-hard  (the hardest problems IN NP)
   PSPACE   poly MEMORY (QBF is PSPACE-complete) ; NP subset PSPACE

   OPEN: P =? NP  (and NP =? co-NP).  Conjectured P != NP.
```

**Read this as a map of what's reachable**: P is what the rest of this directory
reaches; NP-complete problems have no known poly algorithm and one would collapse all
of them; the escape routes (approximation, randomization, parameterization) are how
you *engineer around* an NP-hard problem you actually have to ship.

---

## Layer 1: The Classes, Precisely

```
   P        a DETERMINISTIC poly-time algorithm decides it.
            e.g. sorting, shortest path, MST, linear programming (Khachiyan), primality (AKS).

   NP       a poly-size CERTIFICATE for YES instances, checkable in poly time.
            SAT: the certificate is a satisfying assignment; verify by evaluating.
            Equivalent: solvable by a nondeterministic TM in poly time.

   co-NP    YES/NO swapped: poly-checkable certificate for NO instances.
            UNSAT (no satisfying assignment), TAUTOLOGY.

   P subset (NP intersect co-NP).   P=NP is open.   NP=co-NP is open (and would be
   surprising; e.g. it would put a poly certificate on UNSAT).
```

The MIT-level subtleties worth pinning down:

- **NP is about verification, not "nondeterministic-polynomial-as-in-slow."** A YES
  instance has a short proof you can check fast; you needn't be able to *find* it fast.
- **NP-hard ⊋ NP-complete.** NP-hard means "at least as hard as everything in NP" but
  need not be *in* NP (e.g. the *optimization* TSP, or the halting problem, are NP-hard
  but not in NP). NP-complete = NP-hard **and** in NP.
- **co-NP ≠ "not NP."** It is the class of complements. SAT ∈ NP; UNSAT ∈ co-NP. If any
  NP-complete problem is in co-NP, then NP = co-NP.

---

## Layer 2: Reductions (the load-bearing tool)

A reduction transforms problem `A` into problem `B` so that an algorithm for `B`
solves `A`. **The direction is everything** — get it backwards and you've proved
nothing.

```
   A  <=_p  B     "A poly-time reduces to B"     (A is NO HARDER than B)
   ----------------------------------------------------------------------
   To prove B is NP-HARD: reduce a KNOWN NP-hard problem A *to* B  (A <=_p B).
     "B is at least as hard as A, which is already hard."
   To prove B is EASY: reduce B to a known EASY problem.

   THE #1 MISTAKE: reducing B to a known-hard problem proves NOTHING about B's hardness.
     (showing your problem is no harder than SAT doesn't make it hard.)

   reduction must be: (1) poly-time computable, (2) YES(A) <=> YES(B).
```

### Worked reduction: 3-SAT ≤_p INDEPENDENT-SET

```
   Given 3-SAT formula  (x1 OR ~x2 OR x3) AND (~x1 OR x2 OR x3) ...  (k clauses):
   BUILD a graph:
     - one TRIANGLE per clause (3 vertices = the 3 literals; edges within the triangle)
     - connect a literal to its NEGATION across clauses (x1 -- ~x1 edges)
   CLAIM: formula is satisfiable  <=>  graph has an independent set of size k.
     pick one TRUE literal per clause -> k vertices, no two adjacent (triangle edges
     forbid two-in-a-clause; negation edges forbid x and ~x both true). <=> consistent
     satisfying assignment.
   poly-time, equivalence holds  => INDEPENDENT-SET is NP-hard (and in NP) => NP-complete.
```

This is the template: encode the source problem's logic in the target's structure so a
solution maps back and forth. **Cook-Levin** seeded the whole web by proving SAT is
NP-complete *from the definition of NP* (a TM computation encoded as a formula);
everything else is a reduction chain from SAT.

```
   THE CLASSIC REDUCTION WEB (Karp's 21):
     SAT -> 3-SAT -> { CLIQUE, INDEPENDENT-SET, VERTEX-COVER } (graph-algorithms/07)
                  -> 3-COLORING -> ...
                  -> SUBSET-SUM -> KNAPSACK(dec) (04)
                  -> HAMILTONIAN-CYCLE -> TSP(dec)
   Build a NEW hardness proof by reducing the closest of these to your problem.
```

The NP-hard *graph* problems (CLIQUE, VERTEX-COVER, COLORING, HAM-CYCLE, TSP) get full
treatment in `graph-algorithms/07`; this guide gives the classification machinery that
places them.

---

## Layer 3: Weak vs Strong NP-Hardness (and pseudo-polynomial)

```
   SUBSET-SUM / 0/1 KNAPSACK have a DP in O(n * W)  (see 04).
   Is that polynomial?  W is a VALUE; its ENCODING is log W bits.
   => O(nW) is EXPONENTIAL in input SIZE -> "PSEUDO-polynomial".

   WEAKLY NP-hard:   has a pseudo-poly algorithm (poly in the numeric values).
                     KNAPSACK, SUBSET-SUM.  -> tractable when numbers are small.
   STRONGLY NP-hard: NP-hard even when all numbers are poly-bounded -> NO pseudo-poly
                     algorithm unless P=NP.  TSP, 3-PARTITION, BIN-PACKING.
```

This is exactly the distinction `04` flagged for knapsack: O(nW) feels polynomial but
is exponential in the bit-length of `W`. It tells you *when* the DP escape works (small
numbers) and when it doesn't (strongly NP-hard).

---

## Layer 4: Escape Route 1 — Approximation Algorithms

If you can't solve it exactly and efficiently, get a solution provably within a factor
of optimal.

```
   APPROXIMATION RATIO rho: ALG <= rho * OPT (minimization) for ALL inputs.

   VERTEX COVER  2-approximation (greedy on edges):
     repeatedly pick any uncovered edge (u,v), add BOTH u,v to the cover, remove
     incident edges.  The chosen edges form a matching M; OPT must cover each,
     using >= |M| vertices; ALG uses 2|M|  => ALG <= 2*OPT.   (graph-algorithms/07)

   METRIC TSP  1.5-approximation (Christofides): MST + min-weight matching on
     odd-degree vertices + shortcut an Euler tour.  (graph-algorithms/04,06)

   SET COVER  ln(n)-approximation (greedy: take the set covering the most new elements)
     and this is TIGHT -- no poly algorithm does better unless P=NP.

   PTAS / FPTAS:
     PTAS  : (1+eps)-approx in time poly(n) for each fixed eps (eps in the exponent ok).
     FPTAS : (1+eps)-approx in time poly(n, 1/eps).  KNAPSACK has an FPTAS.
   INAPPROXIMABILITY: some problems (general TSP, MAX-CLIQUE) cannot be approximated
     within ANY constant unless P=NP (PCP theorem).
```

The approximation hierarchy (FPTAS ⊂ PTAS ⊂ constant-factor ⊂ log-factor ⊂
inapproximable) is the precise vocabulary for "how well can we do." LP relaxation +
rounding (`operations-research/01`,`02`) is the systematic source of these ratios —
the LP-duality bridge to OR is direct.

---

## Layer 5: Escape Route 2 — Randomized Algorithms

Allowing the algorithm to flip coins yields simpler and sometimes asymptotically
faster algorithms, classified by their error model.

```
   RANDOMIZED COMPLEXITY CLASSES
   -----------------------------
   RP   poly time; YES -> accepts w.p. >= 1/2; NO -> always rejects   (one-sided error)
   co-RP mirror: NO -> rejects w.p. >= 1/2; YES -> always accepts
   ZPP  = RP intersect co-RP; LAS VEGAS: always correct, expected poly time
   BPP  poly time; bounded TWO-sided error <= 1/3 (amplifiable to 2^-k by repetition)

   P subset ZPP subset RP subset NP ;  RP subset BPP.   BPP vs P: conjectured BPP = P
     (derandomization; strong evidence from circuit lower bounds).

   MONTE CARLO  vs  LAS VEGAS
   may be wrong,      always correct,
   fixed runtime      runtime is random (expected poly)
   e.g. Miller-Rabin  e.g. randomized quicksort, treaps
        primality (RP-style)
```

```
   WHY RANDOMIZE
   - simpler: randomized quicksort (01,02), treaps/skip lists (06) -- O(log n) EXPECTED
   - faster:  Karger's min-cut, polynomial identity testing (Schwartz-Zippel)
   - robust:  random pivots / random hash seeds defeat ADVERSARIAL inputs (02,06,08)
   amplification: repeat k times, error drops exponentially -> any practical confidence.
```

Randomized primality testing (Miller-Rabin) is the bridge to `cryptography/`: RSA key
generation relies on it, and the entire public-key edifice rests on the *conjectured*
average-case hardness of factoring (an NP problem not known to be NP-complete, plausibly
NP-intermediate). Cryptography is applied complexity theory.

---

## Layer 6: Beyond NP (the rest of the hierarchy)

```
   PSPACE   poly MEMORY (any time). QBF (quantified boolean formula) is PSPACE-complete.
            Games (generalized chess/Go) live here.  NP subset PSPACE.
   #P       COUNTING versions (how MANY satisfying assignments?). #SAT is #P-complete;
            counting can be harder than deciding (permanent vs determinant).
   EXPTIME  provably > P (time hierarchy theorem) -- some problems are PROVABLY intractable.
   UNDECIDABLE  halting problem, etc. -- no algorithm at all (computing/21-AUTOMATA.md).

   the ladder:  P subset NP subset PSPACE subset EXPTIME (and P != EXPTIME, PROVABLY).
```

The time/space hierarchy theorems give *unconditional* separations (P ⊊ EXPTIME) — a
reminder that some intractability is proven, not merely conjectured like P ≠ NP.
Undecidability (`computing/21-AUTOMATA.md`) sits above all of this.

---

## Old World → New World Bridges

| You already know | The complexity concept |
|---|---|
| "This scheduling/packing feature is NP-hard" | A reduction from a Karp problem places it; ship an approximation |
| A solver/SAT-based config validator | SAT is NP-complete; modern SAT solvers are the practical workhorse |
| "We can only get within X% of optimal" | Approximation ratio ρ with a proof — FPTAS/PTAS/constant/log hierarchy |
| LP relaxation in an optimizer | The standard route to approximation ratios (`operations-research/`) |
| Miller-Rabin in key generation | Randomized (RP-style) primality; RSA rests on factoring hardness (`cryptography/`) |
| "Retry until it works" Monte Carlo job | Amplification: error drops exponentially with repetition |
| Hash-flood / ReDoS defense | Randomized hashing / linear automata defeat adversarial worst cases (`06`,`08`) |

The "NP-hard feature" bridge is the one a VP actually uses: recognizing that a request
(optimal scheduling, bin-packing, minimal config) is NP-hard reframes the engineering
goal from "find the optimum" to "pick an escape route" — approximation with a proven
ratio, a pseudo-poly DP if the numbers are small, or a SAT/ILP solver that is
exponential in the worst case but fast in practice.

---

## Decision Cheat Sheet

| Situation | Move | Reference |
|---|---|---|
| Prove my problem B is NP-hard | reduce a known NP-hard A **to** B (A ≤_p B) | Layer 2 |
| Suspect B is easy | reduce B to a known poly problem | Layer 2 |
| NP-hard but numbers are small | pseudo-poly DP (weakly NP-hard) | `04`, Layer 3 |
| NP-hard, numbers large | approximation / heuristic / solver | Layers 4–5 |
| Need a quality guarantee | approximation algorithm with ratio ρ | Layer 4 |
| Want (1+ε) and it's knapsack-like | FPTAS | Layer 4 |
| Constant-factor impossible? | check PCP-based inapproximability | Layer 4 |
| Simpler/faster algorithm acceptable with tiny error | randomized (BPP/RP) + amplify | Layer 5 |
| Need always-correct + expected-fast | Las Vegas (ZPP) | Layer 5 |
| Adversarial worst-case inputs | randomize pivots/hash seeds | `02`,`06`,`08` |
| Counting solutions, not deciding | #P — expect it to be harder | Layer 6 |
| Game / quantified problem | likely PSPACE-complete | Layer 6 |

---

## Common Confusion Points

### "Reduce my problem to SAT to prove it's hard"

Backwards. Reducing **your** problem *to* SAT shows it is **no harder** than SAT —
proving nothing about its hardness. To prove your problem is NP-hard, reduce a known
NP-hard problem (3-SAT, VERTEX-COVER, ...) **to your problem** (`A ≤_p B`, source → your
target). Direction is the single most common reduction error.

### "NP means it takes exponential time"

NP is defined by **poly-time verification** of a certificate, not by exponential
solving. P ⊆ NP, so every easy problem is in NP. Whether NP requires exponential time
is exactly the open P-vs-NP question; "NP" does not assert intractability.

### "NP-hard and NP-complete are the same"

NP-complete = in NP **and** NP-hard. NP-hard alone may be *outside* NP (harder) — e.g.
the optimization TSP or the halting problem are NP-hard but not in NP. Only the
problems that are both verifiable (in NP) and universal (NP-hard) are NP-complete.

### "0/1 knapsack's O(nW) DP means knapsack is in P"

O(nW) is **pseudo-polynomial**: W is a numeric value of bit-length log W, so the DP is
exponential in input size. Knapsack is (weakly) NP-hard; the DP is efficient only when
W is small. Strongly NP-hard problems (TSP, bin-packing) have no such pseudo-poly
escape unless P=NP.

### "A 2-approximation guarantees within 2x on average"

It guarantees within the factor for **every** input (worst case), with a proof — not an
average. And not every NP-hard problem is approximable: general TSP and MAX-CLIQUE have
no constant-factor approximation unless P=NP (PCP theorem). The ratio is a proven
worst-case bound or it is nothing.

### "Randomized = unreliable / probably wrong"

Error is *amplifiable*: repeat a BPP algorithm k times and the error falls to 2^{-k} —
you can make it astronomically more reliable than your hardware. Las Vegas algorithms
(ZPP, e.g. randomized quicksort) are **always correct** and only their *runtime* is
random. Randomization is a precision tool, not a gamble.
