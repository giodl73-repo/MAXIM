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

## Formal Definition (Quick Reference)

The standard construction (Hausdorff + second-countable + smooth atlas with C^inf transition maps). The key subtleties worth flagging:

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

## Smooth Maps — Quick Reference

| Map type | Condition | Intuition |
|---|---|---|
| Diffeomorphism | Smooth bijection, smooth inverse | Isomorphism of smooth manifolds |
| Immersion | df_p injective at all p | Locally embeds M in N |
| Submersion | df_p surjective at all p | Level sets are submanifolds |
| Embedding | Injective immersion + homeomorphism onto image | Global embedding |

**Whitney embedding theorem**: Every smooth n-manifold embeds smoothly in R^{2n} (compact case). Abstract manifolds always realize as subsets of Euclidean space — but the intrinsic viewpoint avoids coordinate dependence on the ambient space.

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
**Why dimension 4 is special — the gauge theory connection**: Exotic R^4 was discovered through Donaldson's theorem (1983): the moduli space of anti-self-dual Yang-Mills instantons (solutions to the gauge field equations on a 4-manifold) gives polynomial invariants that can distinguish smooth structures. Specifically, Donaldson showed that if a simply-connected smooth 4-manifold has a definite intersection form, the form must be diagonalizable — a constraint that does NOT hold for topological 4-manifolds (Freedman 1982). The gap between Freedman's topological classification and Donaldson's smooth constraints produces exotic structures: topological 4-manifolds that cannot support any smooth structure, and smooth 4-manifolds (like exotic R^4) that are homeomorphic but not diffeomorphic to the standard one. This is why dimension 4 spacetime is geometrically richer than any other: gauge physics (instantons) is the tool that probes smooth structure, and smooth structure is most complex in exactly dimension 4. See 08-FIBER-BUNDLES for the gauge theory side.

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

## Manifolds in Practice — Why Smooth Structure Matters

The smooth structure (not just the topology or the metric) is what makes gradient-based optimization well-defined on a manifold. Without smooth charts, you cannot take derivatives; without smooth transition maps, derivatives are chart-dependent.

```
WHERE MANIFOLDS APPEAR IN ML / ENGINEERING:

  PARAMETER SPACES:
    Neural network weights with orthogonality constraint → Stiefel manifold St(k,n)
    Rotation matrices → SO(3)   (6D → 3D manifold, smooth, compact)
    Positive definite matrices → SPD(n) = Sym+(n)   (open cone, non-compact)
    Probability simplices → open simplex Δⁿ  (or with Fisher metric: stat. manifold)

  CONFIGURATION SPACES:
    n-joint robot arm → T^n (n-torus, one angle per joint)
    Rigid body in 3D → SE(3) = SO(3) ⋉ R³  (Lie group)
    Camera pose → SE(3)

  DATA MANIFOLDS:
    High-dimensional data often lies near a low-dimensional manifold
    Manifold hypothesis in ML: learn the intrinsic coordinates

  WHY SMOOTH STRUCTURE IS NEEDED:
    Gradient descent requires ∂f/∂θ → need smooth charts.
    Riemannian SGD: θ_{t+1} = Exp_{θ_t}(-η grad_g f) → need exp map (smooth).
    Natural gradient: F^{-1} ∇f → Fisher metric F is a smooth (0,2) tensor.
    Without smooth structure, none of these are well-defined.
```
