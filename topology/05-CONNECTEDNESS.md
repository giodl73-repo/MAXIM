# Connectedness

## The Big Picture

```
+====================================================================+
|        CONNECTEDNESS — THE HIERARCHY                               |
+====================================================================+
|                                                                    |
|  CONNECTED: cannot be split into two disjoint nonempty open sets. |
|  PATH-CONNECTED: any two points joined by a continuous path.      |
|  LOCALLY PATH-CONNECTED: each neighborhood contains a path-conn.  |
|  SIMPLY CONNECTED: path-connected + every loop is contractible.   |
|                                                                    |
|  IMPLICATIONS:                                                     |
|  Simply connected → path-connected → connected.                   |
|  Converses FAIL in general.                                       |
|                                                                    |
|  Path-conn. + locally path-conn. → connected components =         |
|                                     path-components.              |
|                                                                    |
|  JORDAN CURVE THEOREM:                                            |
|  A simple closed curve in R² separates R² into exactly 2 regions. |
|  "Obvious" but requires serious proof.                            |
+====================================================================+
```

---

## Connected Spaces

```
DEFINITION: X is CONNECTED if it cannot be written as X = U ∪ V where
  U, V are disjoint, nonempty, and open.

EQUIVALENCES:
  X is connected iff:
  - The only clopen (closed-and-open) sets are ∅ and X.
  - Every continuous function f: X → {0,1} (discrete) is constant.

EXAMPLES:
  Connected: R, [a,b], Rⁿ, Sⁿ, T², any interval.
  NOT connected: {0,1} (discrete), (0,1)∪(2,3), Q (topologically disconnected).

CONNECTED COMPONENTS:
  The maximal connected subsets of X.
  X is a disjoint union of its connected components.
  Components are closed (always); may not be open.
  If all components are open: X is "locally connected."

R\{0} = (-∞,0) ∪ (0,∞): two connected components.
Q: every point is its own connected component (totally disconnected).
Cantor set: totally disconnected + compact + perfect (no isolated points).
```

---

## Path-Connected Spaces

```
PATH: A continuous map γ: [0,1] → X. Start γ(0), end γ(1).

PATH-CONNECTED: For any x,y ∈ X, ∃ path from x to y.

IMPLICATIONS:
  Path-connected → connected.
  Converse FAILS: the topologist's sine curve.

TOPOLOGIST'S SINE CURVE:
  S = {(x, sin(1/x)) : x > 0} ∪ {0} × [-1,1].
  S is connected (closure of connected set is connected).
  S is NOT path-connected: no path from (0,0) to any point on the sine part.
  [The sine oscillates infinitely fast near x=0; any path would need to traverse
   infinitely many oscillations in finite time — impossible for uniform continuity.]

PATH-CONNECTED COMPONENTS:
  Maximal path-connected subsets.
  If X is locally path-connected: path components = connected components.
  (Locally path-connected: every point has a path-connected neighborhood.)
```

---

## Simply Connected Spaces

```
SIMPLY CONNECTED: X is path-connected AND every loop is contractible to a point.
  ∀ continuous γ: S¹ → X, γ is homotopic to a constant map.
  Equivalently: π₁(X) = 0 (trivial fundamental group).

INTUITION: No "holes" — any loop can be shrunk to a point.

EXAMPLES:
  Simply connected: Rⁿ, Sⁿ (n ≥ 2), D² (disk), trees.
  NOT simply connected: S¹ (π₁ = Z), T² (π₁ = Z×Z), R²\{0} (π₁ = Z).

WHY S¹ is not simply connected:
  The identity loop γ: [0,1] → S¹ by γ(t) = e^{2πit} wraps once around.
  This loop cannot be contracted to a point within S¹.
  (If it could, the degree (winding number) would be 0, but it's 1.)

HIGHER CONNECTIVITY:
  k-connected: X is path-connected and πᵢ(X) = 0 for all 1 ≤ i ≤ k.
  Simply connected = 1-connected.
  Sⁿ is (n-1)-connected.

UNIVERSAL COVER:
  Every connected locally path-connected space X has a simply connected covering space X̃.
  π₁(X) acts on X̃ by deck transformations.
  X = X̃ / π₁(X).
  (See 06-FUNDAMENTAL-GROUP.md for full treatment.)
```

---

## Invariance Under Continuous Maps

```
THEOREM: Continuous image of connected space is connected.
THEOREM: Continuous image of path-connected space is path-connected.

These give the standard "applied" results:

INTERMEDIATE VALUE THEOREM:
  f: [a,b] → R continuous. If f(a) < c < f(b), then ∃x: f(x) = c.
  Proof: [a,b] is connected. f([a,b]) is a connected subset of R.
  Connected subsets of R are intervals. c ∈ [f(a),f(b)] ⊆ f([a,b]). □

GENERALIZATIONS:
  f: X → R continuous, X connected → f(X) is an interval (connected subset of R).
  f: X → R continuous, X path-connected → same conclusion.

  Theorem: Connected subsets of R = intervals (open, closed, half-open, R itself).
  Proof: If S ⊆ R is connected and a,b ∈ S with a < b, then [a,b] ⊆ S
    (otherwise S = (S∩(-∞,c)) ∪ (S∩(c,∞)) for some c ∈ [a,b] — a disconnection).
```

---

## Jordan Curve Theorem

```
JORDAN CURVE THEOREM (1887, proved rigorously Jordan; modern proof easier):
  Let C ⊆ R² be a simple closed curve (homeomorphic image of S¹).
  Then R²\C has exactly TWO connected components:
  - One bounded (the "inside")
  - One unbounded (the "outside")
  Both are simply connected (after compactification: S²\C has two simply connected pieces).
  C is the boundary of both components.

WHY IS IT NON-TRIVIAL?
  For "nice" curves (circles, ellipses, polygons): obvious.
  For a general simple closed curve (could be wildly fractal):
  You need to prove: (1) exactly two components, (2) each is simply connected,
  (3) C is the boundary of both.

PROOF APPROACHES:
  Original Jordan: attempted analytic approach, gaps found later.
  Modern: uses Alexander duality (algebraic topology).
    H₁(S²\C; Z) = Z (one cycle from the two components).
    By Alexander duality: H̃_n(S²\C) ≅ H̃^{1-n}(C) = H̃^{1-n}(S¹).
    n=0: H̃₀ = Z (one fewer component than 2) → exactly 2 components.

GENERALIZATIONS:
  Jordan-Brouwer: Sⁿ⁻¹ ⊆ Sⁿ separates Sⁿ into exactly 2 simply connected regions.
  Schoenflies theorem: the two components are homeomorphic to open balls.
    (Needs extra regularity in n=3.)
  Alexander horned sphere: S² ⊆ S³ can have non-simply-connected complement.
    (Wild embedding — shows Schoenflies requires regularity in higher dimensions.)
```

---

## Connected Graphs and Trees

```
GRAPH TOPOLOGY:
  A graph G = (V, E) as a 1-dimensional CW complex.
  Connected graph ↔ connected 1-complex (any two vertices joined by a path of edges).
  Tree = connected graph with no cycles.
  = simply connected graph (all loops trivial, since there are none).

CONNECTED COMPONENTS = connected subgraphs.
  Count = H₀ = rank of 0-th homology group.
  For connected graph: H₀ = Z. For n components: H₀ = Zⁿ.

CYCLE RANK (first Betti number):
  b₁ = |E| - |V| + (# connected components)  [Euler formula for graphs]
  = dimension of H₁ = number of independent cycles.
  Tree: b₁ = 0 (no cycles).
  Cycle graph Cₙ: b₁ = 1 (one cycle).

FUNDAMENTAL GROUP OF GRAPH:
  π₁(G) = free group of rank b₁.
  Tree: π₁ = trivial (contractible to a point).
  Figure 8 (wedge of two circles): π₁ = F₂ (free group on 2 generators).
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Prove X connected | Show no clopen partition; or show f: X→{0,1} must be constant |
| Prove X path-connected | Construct explicit path between any two points |
| Prove simply connected | Show π₁(X) = 0 via van Kampen; or show every loop is null-homotopic |
| Apply IVT | Use connectedness of [a,b] |
| Understand S¹ not simply connected | Winding number argument; loop e^{2πit} has winding 1 |
| Count connected components | Compute H₀ (rank = # components) |
| Separate region in R² | Jordan curve theorem |
| Understand proofs about homotopy groups | Need simply connected universal cover |

---

## Common Confusion Points

**"Connected = path-connected."**
Topologist's sine curve is connected but not path-connected. In most "nice" spaces
(manifolds, CW complexes, open subsets of Rⁿ), connected and locally path-connected implies
path-connected. But for general topological spaces, the notions diverge.

**"Simply connected means connected and simple."**
"Simple" here means "trivial fundamental group," not "simple" in the algebraic sense.
Simply connected = path-connected + π₁ = 0. The intuition: no holes that loops can go around.
Rⁿ is simply connected. S² is simply connected (any loop on a sphere is contractible). S¹ is not.

**"R²\{finite points} is disconnected."**
Wrong. Removing finitely many (or even countably many) points from R² leaves a path-connected
space. (Any two points in R²\S can be joined by a path avoiding the countable set S.)
Contrast: removing a point from R disconnects it (two half-lines). The "dimension" matters.

**"Jordan curve theorem is trivial for smooth curves."**
For smooth (or piecewise linear) curves, there are elementary proofs using intersection
numbers (winding number argument). For continuous curves (which can be fractal, space-filling
in a lower-dimensional sense), the proof requires genuine topological machinery.
