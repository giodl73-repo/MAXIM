---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-MAX-FLOW-MATCHING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:max-flow-matching
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Maximum Flow and Matching
status: source-custody
source_custody: partial
current_path: graph-algorithms/06-MAX-FLOW-MATCHING.md
canonical_path: graph-algorithms/06-MAX-FLOW-MATCHING.md
backsource_ids: [proof-backfill:graph-algorithms:06-max-flow-matching, git-history:graph-algorithms:06-max-flow-matching]
concepts: [max flow, min cut, Ford-Fulkerson, Edmonds-Karp, Dinic, bipartite matching, augmenting paths]
root_concepts: [maximum flow]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Maximum Flow and Matching — The LP-Dual Frontier

Max-flow is the last great polynomial conquest before the NP-hard cliff, and its
central result — **max-flow value = min-cut capacity** — is the most reused
duality in combinatorial optimization. Bipartite matching, vertex-disjoint paths,
project selection, image segmentation, and baseball elimination all reduce to it.
This file is also the bridge to `operations-research/04-NETWORK-FLOWS.md`, where
the same object appears as a linear program; here we treat the combinatorial
augmenting-path algorithms and their exact bounds.

```
  THE MAX-FLOW LANDSCAPE
  ======================

   Source s --capacities--> network --> Sink t       Goal: max units s->t
                                                      subject to:
        s --10--> A --4--> t                            0 <= f(e) <= cap(e)
        |          ^                                     flow in = flow out (except s,t)
        8          6
        v          |                          +-------------------------------------+
        B ---10----+                          | MAX-FLOW MIN-CUT THEOREM            |
                                              |   max flow value = min cut capacity|
   AUGMENTING-PATH FAMILY (Ford-Fulkerson):   +-------------------------------------+
     repeatedly find an s->t path with spare              |
     capacity in the RESIDUAL graph, push flow.           | dual / certificate
     +-------------------+-------------------+             v
     | Edmonds-Karp:     | Dinic:            |     a CUT (S, T) with s in S, t in T
     | BFS aug paths     | BFS levels +      |     whose crossing capacity == flow
     | O(V * E^2)        | blocking flow     |     PROVES the flow is optimal.
     |                   | O(V^2 * E)        |
     +-------------------+-------------------+

   REDUCES TO MAX-FLOW: bipartite matching, vertex/edge-disjoint paths,
                        project selection, min-cut image segmentation.
```

**Read this whole-cloth:** find augmenting paths in the residual graph until none
remain; the leftover unreachable-from-s set defines the min cut that certifies
optimality.

---

## The Setup, the Residual Graph, and the Theorem

> **Preconditions:** a directed graph with a source s, sink t, and a non-negative
> **capacity** on each edge. A *flow* assigns f(e) to each edge with
> 0 ≤ f(e) ≤ cap(e) and *conservation* (in = out) at every vertex except s and t.
> The **value** is the net flow out of s. Integer capacities ⇒ an integral maximum
> flow exists (integrality theorem) — the basis of the matching reduction.

The engine is the **residual graph** Gf: for each edge with flow f and capacity
c, a forward residual edge of capacity c−f (unused capacity) and a *backward* edge
of capacity f (flow that can be cancelled). The backward edges are the subtle part
— they let the algorithm *re-route* earlier decisions.

```
  Edge with cap 10, flow 6:        Residual:
       u --6/10--> v                  u --4--> v    (forward: 10-6 = 4 spare)
                                       u <--6-- v    (backward: 6 cancellable)

  An AUGMENTING PATH is any s->t path in Gf with all-positive residual capacity.
  Push flow = the path's BOTTLENECK (min residual along it). Repeat until none.
```

**Max-flow min-cut theorem.** The maximum flow value equals the minimum capacity
of an s-t cut. Three statements are equivalent: (1) f is a maximum flow; (2) Gf
has no augmenting path; (3) there is a cut (S,T) with capacity = |f|. The cut is a
*certificate*: when no augmenting path remains, let S = vertices reachable from s
in Gf; every edge crossing S→T is saturated, so the cut capacity equals the flow.
That cut is a proof of optimality you can hand to a skeptic.

```
  At max flow, the residual graph has NO s->t path. The reachable set from s
  is S; the rest is T. Every forward edge S->T is SATURATED (full), every
  backward edge T->S carries zero. So:  cut capacity = sum of crossing caps = |f|.

      S | T
   s--*--+--*--t      crossing edges all full => flow can't increase => OPTIMAL
```

> Bridge to `operations-research/`: this *is* LP strong duality. The max-flow LP's
> dual is the min-cut LP; strong duality forces their optima equal. The same
> complementary-slackness story in `operations-research/02-DUALITY.md` plays out
> here as "saturated forward edges, empty backward edges." Min-cost flow and the
> assignment problem in `operations-research/04-NETWORK-FLOWS.md` generalize this.

---

## The Algorithms — and Their Exact Bounds

The augmenting-path family differs only in *how it chooses* the augmenting path.
That choice is everything for the complexity bound.

| Algorithm | Path choice | Time | Notes / precondition |
|-----------|-------------|------|---------------------|
| Ford-Fulkerson (generic) | *any* augmenting path | O(E · \|f\*\|) | only integer caps; **can loop forever on irrationals** |
| Edmonds-Karp | **BFS** (shortest aug path) | **O(V·E²)** | bound independent of capacities |
| Dinic | BFS level graph + blocking flow | **O(V²·E)** | O(E·√V) on **unit-capacity** / bipartite |
| Push-relabel (FIFO) | local push + relabel | O(V³) | often fastest in practice |
| Push-relabel (highest-label) | — | O(V²·√E) | strong practical performer |

```
  WHY Ford-Fulkerson's bound is O(E*|f*|), not polynomial in input size:

       s --1000--> A           pick the bad path s->A->B->t (bottleneck 1):
       |  \          \  1000    pushes 1 unit; then s->B->A->t pushes 1 unit;
     1000  1        1000        ... if you keep choosing the 1-capacity middle
       |     \  1     /         edge, you augment 2000 times for a flow of 2000.
       v       v   v
       B --1000--> t           Edmonds-Karp's BFS avoids this: it always takes
                               the FEWEST-EDGE path, bounding augmentations to O(VE).
```

**Edmonds-Karp** fixes Ford-Fulkerson's pathology by always augmenting along the
*shortest* (fewest-edge) path via BFS. The key lemma: shortest-path distances from
s are non-decreasing across augmentations, bounding the number of augmentations to
O(V·E), each found in O(E) — hence **O(V·E²)**, *independent of capacity
magnitudes*. **Dinic** goes further: it builds a BFS *level graph* and pushes a
*blocking flow* (saturating all shortest paths at once) per phase, giving
**O(V²·E)** general and a celebrated **O(E·√V)** on unit-capacity graphs — which
is exactly the bipartite-matching case.

> **Ford-Fulkerson caveat (audit-critical):** with *irrational* capacities and
> adversarial path choice, generic Ford-Fulkerson may not even terminate. With
> integer capacities it terminates in O(E·|f\*|) — pseudo-polynomial, fine for
> small flows, bad when |f\*| is huge. Edmonds-Karp and Dinic remove the capacity
> dependence; use them as the default.

---

## Bipartite Matching — The Flagship Reduction

A **matching** pairs up vertices with no shared endpoints; a **maximum matching**
has the most pairs. On a **bipartite** graph (vertices split L ∪ R, edges only
cross) this reduces *exactly* to max-flow.

```
  Bipartite graph (workers L, jobs R):     Reduce to max-flow:
                                           -------------------------------------
    L1 --- R1        add super-source s -> each Li (cap 1)
    L1 --- R2        add super-sink   each Rj -> t (cap 1)
    L2 --- R2        original edges Li -> Rj have cap 1
    L3 --- R1                          s =1=> Li =1=> Rj =1=> t

   MAX MATCHING = MAX FLOW value (integral, so every f(e) in {0,1};
                  a saturated Li->Rj edge = a matched pair).

   Hopcroft-Karp does this directly: O(E * sqrt(V)) -- the Dinic bound on the
   unit-capacity reduction, found without explicitly building the flow network.
```

| Matching problem | Best algorithm | Time |
|------------------|----------------|------|
| Max bipartite matching | Hopcroft-Karp | **O(E·√V)** |
| Max bipartite matching (simple) | augmenting-path (Hungarian-style) | O(V·E) |
| Min-cost / max-weight bipartite (assignment) | Hungarian algorithm | O(V³) |
| Max matching, **general** (non-bipartite) | Blossom (Edmonds) | O(V³) |

**König's theorem** is the matching face of max-flow/min-cut: in a bipartite
graph, *max matching size = min vertex cover size*. (Vertex cover is NP-hard in
general — `07` — but *polynomial* on bipartite graphs, exactly because of this
flow connection. The bipartite restriction collapses an NP-hard problem to P.)

> The **general** (non-bipartite) case needs Edmonds' **Blossom** algorithm
> because odd cycles ("blossoms") break the simple augmenting-path argument — a
> genuinely harder problem than the bipartite one, but still polynomial. Don't
> apply the flow reduction to a non-bipartite graph; it doesn't hold.

---

## Reductions — What Secretly *Is* Max-Flow

```
  Edge/vertex-disjoint s-t paths   = max-flow with unit capacities (Menger, 05)
  Bipartite matching               = max-flow, unit caps via super s/t
  Min vertex cover (bipartite)     = max matching (Konig)  -> max-flow
  Project selection / max-weight   = min-cut (s=projects, t=costs)
   closure                           
  Image segmentation (graph cut)   = min s-t cut (foreground/background)
  Baseball elimination             = max-flow feasibility
```

The pattern: if a problem is "partition / select / route under capacity," suspect
a flow or cut reduction before reaching for anything NP-hard. The art of applied
flow is recognizing the reduction. `operations-research/04-NETWORK-FLOWS.md`
catalogs the optimization-flavored versions (min-cost flow, transportation,
assignment) of the same machinery.

---

## Old World → New World Bridges

| You know it as… | It is max-flow / min-cut of… |
|-----------------|------------------------------|
| Network bandwidth / bottleneck capacity | max-flow value; min-cut = the bottleneck links |
| "Two independent paths" redundancy SLA | edge-disjoint paths = max-flow, unit caps |
| Assigning on-call engineers to shifts | bipartite matching → max-flow |
| Load balancer capacity planning | max-flow on the request-routing graph |
| Image background removal (graph cut) | min s-t cut separating fg/bg pixels |
| Cluster failure domains | min-cut = cheapest set of links to sever |

The redundancy-SLA bridge is exact via Menger (`05`): the maximum number of
edge-disjoint s-t paths equals the min s-t cut, so "how many simultaneous link
failures before s and t are partitioned?" is a max-flow with unit capacities.

---

## Decision Cheat Sheet

| Situation | Use | Time |
|-----------|-----|------|
| General max-flow, default | Dinic | O(V²·E) |
| Max-flow, easy to implement | Edmonds-Karp | O(V·E²) |
| Max-flow, tiny integer caps | Ford-Fulkerson | O(E·\|f\*\|) |
| Max-flow in practice, large dense | push-relabel | O(V³) / O(V²√E) |
| Max bipartite matching | Hopcroft-Karp | O(E·√V) |
| Min-cost / weighted assignment | Hungarian | O(V³) |
| Max matching, non-bipartite | Blossom (Edmonds) | O(V³) |
| Min vertex cover on bipartite graph | König ⇒ max matching | O(E·√V) |
| Cheapest set of links to disconnect s,t | min-cut (= max-flow) | flow time |
| Optimization version (costs on flow) | min-cost flow (`operations-research/04`) | — |

---

## Common Confusion Points

**"Max-flow = min-cut only sometimes."** It is a *theorem*, always true for any
network with a source and sink: the maximum flow value *equals* the minimum cut
capacity, unconditionally. The min cut also serves as an efficiently-checkable
*certificate* that a given flow is maximum (no augmenting path ⇔ a saturated cut).

**"Ford-Fulkerson is polynomial."** Generic Ford-Fulkerson is
*pseudo-polynomial*: O(E·|f\*|), depending on the *magnitude* of the max flow, not
just V and E. With pathological path choices and irrational capacities it may not
terminate. Edmonds-Karp (O(V·E²)) and Dinic (O(V²·E)) are the truly polynomial
members of the family — their bounds don't mention capacities at all.

**"Backward (residual) edges are an implementation hack."** They are essential to
correctness, not an optimization. Backward edges let the algorithm *undo* earlier
flow to re-route, which is what makes the augmenting-path approach reach the global
optimum. Without them you'd get stuck at a maximal-but-not-maximum flow.

**"Bipartite matching needs a special algorithm unrelated to flow."** It *is*
max-flow with unit capacities (add a super-source/sink). Hopcroft-Karp is
precisely Dinic specialized to that unit-capacity network, which is where its
O(E·√V) comes from. The non-bipartite case is the one that needs genuinely
different machinery (Blossom).

**"Vertex cover is NP-hard, so it's hard on bipartite graphs too."** No — König's
theorem makes minimum vertex cover *polynomial* on bipartite graphs (it equals max
matching, hence a flow). Vertex cover is NP-hard on *general* graphs (`07`). The
bipartite structure is exactly what collapses it to P — a clean example of
structure defeating hardness.
