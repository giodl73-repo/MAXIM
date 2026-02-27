# Smooth Manifolds

## The Big Picture

A smooth manifold is a topological space that locally looks like R^n, with compatible smooth structure allowing calculus everywhere.

```
+------------------------------------------------------------------+
|                    SMOOTH MANIFOLD CONSTRUCTION                  |
+------------------------------------------------------------------+
|                                                                  |
|  TOPOLOGICAL SPACE M                                             |
|  +------------------------------------+                          |
|  |  Hausdorff, second-countable       |                          |
|  |  (technical conditions: separates  |                          |
|  |   points; has countable basis)     |                          |
|  +------------------------------------+                          |
|          +                                                       |
|  ATLAS  {(U_alpha, phi_alpha)}                                   |
|  +-------------------------------------------------+             |
|  | Open cover U_alpha of M                         |             |
|  | Homeomorphisms phi_alpha: U_alpha -> V_alpha     |             |
|  | where V_alpha open in R^n                        |             |
|  |                                                  |             |
|  | COMPATIBILITY: On overlaps U_alpha cap U_beta,  |             |
|  | phi_beta o phi_alpha^{-1}: R^n -> R^n is C^inf  |             |
|  +-------------------------------------------------+             |
|          =                                                       |
|  SMOOTH MANIFOLD: can do calculus                               |
|  A function f: M -> R is smooth if f o phi^{-1} is C^inf in R^n |
+------------------------------------------------------------------+
```

---

<!-- @editor[audience/P2]: The learner profile explicitly states "does NOT need: what a manifold is, smooth maps" — the full formal definition from topological manifold up, atlas construction, and smooth maps from scratch are below the pitch level. The learner knows this cold from MIT. Replace with: the key subtleties that matter for the applications (exotic smooth structures, manifolds that aren't subsets of R^n, why the definition is set up the way it is) rather than restating the definition. -->
## Formal Definition

**Topological manifold**: A Hausdorff, second-countable topological space M such that every point p in M has an open neighborhood U homeomorphic to an open set V in R^n.

- (U, phi: U -> V) is called a **chart** or **local coordinate system**
- n is the **dimension** of M

**Smooth (C^inf) manifold**: A topological manifold with an **atlas** (maximal collection of compatible charts):

```
  Atlas A = {(U_alpha, phi_alpha)}  covering M, where:

  Transition maps: phi_beta o phi_alpha^{-1}: phi_alpha(U_alpha cap U_beta) -> phi_beta(U_alpha cap U_beta)
  are C^inf (smooth) wherever defined.

  Two atlases are compatible if their union is also an atlas.
  A maximal atlas (containing all compatible charts) = smooth structure.
```

**Dimension**: All charts map to the same dimension n (assuming M is connected). The dimension is a topological invariant.

---

## Key Examples of Manifolds

**Euclidean space R^n**: Trivial — one chart = identity map. The model space itself.

**The n-sphere S^n**:

```
  S^n = {x in R^{n+1} : ||x|| = 1}

  Atlas with two charts (stereographic projections):
  - Remove north pole N: phi_N(x) = stereographic proj from N -> R^n
  - Remove south pole S: phi_S(x) = stereographic proj from S -> R^n
  Transition map on overlap is C^inf (and conformal).

  S^1 = circle (1-manifold)
  S^2 = sphere (2-manifold)
  S^3 = 3-sphere (is the Lie group SU(2) = unit quaternions)
```

**The torus T^n = S^1 x S^1 x ... x S^1**:

```
  T^2 = S^1 x S^1  (donut surface)
  Can also be defined as R^2 / Z^2 (quotient manifold)
  Flat (zero curvature) but has non-trivial topology
```

**Real projective space RP^n**:

```
  RP^n = S^n / (x ~ -x)  (antipodal identification)
  = lines through origin in R^{n+1}
  RP^1 = circle (homeomorphic to S^1)
  RP^2 = non-orientable surface (cannot be embedded in R^3 without self-intersection)
```

**Matrix groups**: GL(n,R), SL(n,R), O(n), SO(n), U(n), SU(n) — these are both groups and manifolds (Lie groups, see 07-LIE-GROUPS). GL(n,R) = {A: det A != 0} is an open subset of R^{n^2}, hence a manifold.

**Products**: If M (dim m) and N (dim n) are manifolds, so is M x N (dim m+n).

---

<!-- @editor[audience/P2]: "Smooth maps" section defines immersion/submersion/embedding from scratch — learner has differential topology at this level from MIT. Condense to a quick reference table (keep the Whitney embedding theorem result and its implication for intrinsic vs. extrinsic geometry). The section should focus on what's surprising or non-obvious, not the vocabulary. -->
## Smooth Maps

A function f: M -> N between smooth manifolds is **smooth** if in any charts (U, phi) on M and (V, psi) on N:

```
  psi o f o phi^{-1}: R^m -> R^n  is C^inf

  This must hold for ALL chart pairs where it is defined.
  Independence of chart choice is guaranteed by smooth compatibility.
```

**Special smooth maps**:

```
  Diffeomorphism: smooth bijection with smooth inverse.
  The isomorphism of smooth manifolds — "same manifold up to smooth rearrangement."

  Immersion: df_p is injective for all p in M.
  (M "locally embeds" in N)

  Submersion: df_p is surjective for all p in M.
  (Fiber map — level sets are submanifolds)

  Embedding: injective immersion that is a homeomorphism onto its image.
  (Global embedding — M sits inside N)
```

**Whitney embedding theorem**: Every smooth n-manifold can be smoothly embedded in R^{2n+1} (in fact R^{2n} suffices for compact manifolds). So abstract manifolds can always be thought of as subsets of Euclidean space — but working intrinsically is cleaner.

---

## Submanifolds

S subset M is an **embedded submanifold** if locally it looks like R^k sitting inside R^n:

```
  At each p in S, there is a chart (U, phi) of M such that
  phi(U cap S) = phi(U) cap (R^k x {0})
  (S looks like the first k coordinates in this chart)

  Regular level set: If f: M -> N is smooth and c in N is a regular value
  (df_p surjective for all p in f^{-1}(c)), then f^{-1}(c) is a submanifold
  of M with dim(M) - dim(N).

  Example: S^{n-1} = {||x||^2 = 1} = level set of f: R^n -> R, f(x) = ||x||^2.
  df_x = 2x^T != 0 for x != 0, so 1 is a regular value.
  S^{n-1} is an (n-1)-manifold. ✓
```

---

## Tangent Vectors — Two Equivalent Definitions

The tangent space T_p M at a point p can be defined several ways. Two are important:

**Equivalence classes of curves**:

```
  A tangent vector at p = equivalence class of smooth curves gamma: (-eps, eps) -> M
  with gamma(0) = p, where gamma_1 ~ gamma_2 iff (phi o gamma_1)'(0) = (phi o gamma_2)'(0)
  in any (hence all) charts phi.

  The equivalence class [gamma] is the "velocity" of gamma at p.
  This is coordinate-free and geometric.
```

**Derivations** (the algebraic definition):

```
  A tangent vector at p = linear map v: C^inf(M) -> R satisfying
  Leibniz rule: v(fg) = v(f) g(p) + f(p) v(g)

  In local coordinates (x^1, ..., x^n):
  v = Sum_i v^i (partial/partial x^i)|_p

  The partial derivatives partial/partial x^i form a basis of T_p M.
```

**Why the derivation definition?** It generalizes to infinite-dimensional manifolds (Banach/Hilbert manifolds), algebraic geometry (algebraic varieties), and formal schemes in algebraic geometry. The derivation perspective is the "abstract algebra" side; the curve perspective is the geometric side.

---

## Charts, Coordinates, and Invariance

A key skill: computing in coordinates while knowing the intrinsic object.

```
  INTRINSIC:                  COORDINATE EXPRESSION:
  Smooth function f: M -> R   f o phi^{-1}: R^n -> R
  Tangent vector v at p       v = Sum_i v^i partial_i  (components in chart)
  Smooth map F: M -> N        psi o F o phi^{-1}: R^m -> R^n

  CHANGE OF COORDINATES (if phi, psi are two charts at p):
  v^i_new = Sum_j (partial x^i_new / partial x^j_old) v^j_old

  This is the transformation law for contravariant vectors.
  The Jacobian matrix of the transition map tells you how components change.
```

**Tensors transform consistently**: The power of the differential geometry framework is that you can verify an object is well-defined (coordinate-independent) by checking transformation laws, then compute in convenient coordinates.

---

## Orientability

A smooth manifold M is **orientable** if there exists an atlas such that all transition maps have positive Jacobian determinant. An orientation is a consistent choice of "handedness" across M.

```
  ORIENTABLE:    R^n, S^n, T^n, all Lie groups, complex manifolds
  NON-ORIENTABLE: Mobius band, RP^2, Klein bottle

  Why it matters:
  - Integration of top-forms requires orientability
  - Stokes' theorem needs a consistent orientation
  - Physical theories typically require orientability
  - The Mobius band has a non-trivial fiber bundle structure over S^1 (08)
```

---

## Partition of Unity

The technical tool that makes local-to-global constructions work:

```
  Given any open cover {U_alpha} of a smooth manifold M,
  there exists a partition of unity: smooth functions {rho_alpha: M -> [0,1]} such that:
  - supp(rho_alpha) subset U_alpha  (each function supported in one chart)
  - Sum_alpha rho_alpha(p) = 1 for all p in M  (they sum to 1)

  Use: To define a global object, define it locally in each chart and
  glue together using a partition of unity.

  Example: Riemannian metrics. Define g_alpha in each chart U_alpha.
  Then g = Sum_alpha rho_alpha g_alpha is a global Riemannian metric.
```

---

## Topological vs. Smooth Structure

Exotic smooth structures: A topological manifold can admit multiple non-diffeomorphic smooth structures.

```
  R^n:   Unique smooth structure for n != 4.
         In n=4: uncountably many exotic smooth structures!
         "Exotic R^4" — same topological space as R^4 but different smooth structure.

  S^7:   28 exotic 7-spheres (Milnor 1956 — the first surprise)
  S^4:   Unknown (smooth Poincare conjecture in dim 4 is open!)

  This is a deep result. The smooth category is much more subtle than
  the topological category in dimension 4. This is related to why
  4-dimensional spacetime is special in physics.
```
<!-- @editor[bridge/P2]: Exotic R^4 and its physics implication is mentioned but not developed — this is the most important point in this section for a sophisticated reader. The connection: Donaldson's theorem (from Yang-Mills gauge theory on 4-manifolds) was what revealed the exotic smooth structures. The smooth Poincaré conjecture in dim 4 being open is directly connected to the difficulty of 4D spacetime topology. Expand this bridge: Yang-Mills instantons on 4-manifolds (08-FIBER-BUNDLES) provided the first tools to distinguish smooth structures, connecting gauge physics to 4-manifold topology. -->

---

## Decision Cheat Sheet

| Situation | Tool | Notes |
|---|---|---|
| Define "function on M is smooth" | Charts + compatibility | f smooth iff f o phi^{-1} smooth in R^n |
| Work with tangent vectors | Derivations or velocity curves | Derivations better for computation |
| Verify something is a submanifold | Regular value theorem | Check Jacobian of defining equations |
| Move smoothly between charts | Transition maps | Must be C^inf for smooth structure |
| Define global objects from local data | Partition of unity | Sum up local pieces with smooth cutoffs |
| Show two manifolds are "the same" | Construct a diffeomorphism | Smooth bijection with smooth inverse |

---

## Common Confusion Points

**"The sphere S^2 is a 2-manifold, so it can be covered by one R^2 chart."**
No. Topological obstruction: any continuous map from S^2 to R^2 must have non-trivial topology (Borsuk-Ulam theorem says antipodal points map to the same point under any continuous map to R^2). Stereographic projection gives two charts but each misses one point.

**"Coordinates are part of the manifold's definition."**
Coordinates (charts) are auxiliary tools for computation, not part of the manifold itself. The smooth structure is the maximal atlas; specific coordinates are just choices within it. Coordinate-free statements are geometrically intrinsic.

**"Smooth maps and continuous maps are essentially the same."**
Very different. There are continuous everywhere but nowhere differentiable functions (Weierstrass). Smooth maps satisfy infinitely many conditions (all derivatives exist). The smooth category is much more rigid than the continuous category, which is why Whitney's embedding theorem (smooth embedding in R^{2n+1}) is non-trivial.

**"The dimension of a manifold is obvious from looking at it."**
Dimension is defined locally (dimension of R^n in charts). For embedded manifolds in R^k, the dimension equals the dimension of the tangent plane. But the invariance of dimension under homeomorphism (let alone diffeomorphism) requires proof — it follows from invariance of domain, which requires algebraic topology.

<!-- @editor[content/P2]: Missing ML/applications bridge — the guide defines manifolds rigorously but never connects to why a practitioner working with Riemannian optimization, geometric deep learning, or information geometry cares about the smooth structure specifically (as opposed to just the metric structure). Add a short "Manifolds in Practice" section: parameter spaces of neural networks are smooth manifolds (implicitly or explicitly), configuration spaces in robotics are manifolds, the space of probability distributions with Fisher metric is a statistical manifold. The smooth structure (not just topology) is what makes gradient-based optimization well-defined. -->
