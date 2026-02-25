# Connections and Covariant Derivatives

## The Big Picture

A connection answers: "How do you differentiate a vector field on a curved manifold?" Ordinary partial derivatives are chart-dependent. A connection provides a chart-independent notion of differentiation and parallel transport.

```
+------------------------------------------------------------------+
|                   CONNECTIONS OVERVIEW                           |
+------------------------------------------------------------------+
|                                                                  |
|  PROBLEM: In R^n, differentiate vector field V along X:         |
|  (nabla_X V)^i = Sum_j X^j partial_j V^i   -- chart dependent! |
|                                                                  |
|  SOLUTION: Affine connection nabla                              |
|  nabla_X V is a new vector field encoding "rate of change of V  |
|  as you move along X, corrected for the curvature of the space" |
|                                                                  |
|  +---------------------+  +-----------------------------+       |
|  | COVARIANT DERIVATIVE|  | PARALLEL TRANSPORT          |       |
|  | nabla_X V           |  | Move V along a curve        |       |
|  | (derivative at a pt)|  | keeping it "parallel"       |       |
|  +---------------------+  +-----------------------------+       |
|             |                           |                        |
|             v                           v                        |
|  +-----------------------------------+                          |
|  | LEVI-CIVITA CONNECTION            |                          |
|  | Unique torsion-free connection    |                          |
|  | compatible with the Riemannian    |                          |
|  | metric g.                         |                          |
|  +-----------------------------------+                          |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Affine Connections

An **affine connection** (or linear connection) nabla on M is a bilinear map:

```
  nabla: Gamma(TM) x Gamma(TM) -> Gamma(TM)
  (X, V) |-> nabla_X V

  satisfying:
  1. nabla_{fX+Y} V = f nabla_X V + nabla_Y V         (tensor in X -- f in C^inf)
  2. nabla_X (V + W) = nabla_X V + nabla_X W          (additive in V)
  3. nabla_X (fV) = (Xf) V + f nabla_X V             (Leibniz rule in V)

  Condition 1 makes nabla_X V tensorial in X (depends only on X at the point).
  Condition 3 is the Leibniz rule -- nabla_X is a derivation.
```

**Christoffel symbols**: In local coordinates (x^1,...,x^n):

```
  nabla_{partial_i} partial_j = Sum_k Gamma^k_{ij} partial_k

  The n^3 smooth functions Gamma^k_{ij} completely determine the connection.
  Note: Gamma^k_{ij} are NOT the components of a tensor — they transform
  with an inhomogeneous (affine) term under coordinate changes.
  (This is why a connection is not simply a tensor field.)

  For any vector fields X = X^i partial_i, V = V^j partial_j:
  (nabla_X V)^k = Sum_j X^j (partial_j V^k + Sum_i Gamma^k_{ij} V^i)
               = X^j (partial_j V^k) + Gamma^k_{ij} X^j V^i
```

---

## Parallel Transport

Given a curve gamma: [0,1] -> M and a vector v_0 at gamma(0), the **parallel transport** of v_0 along gamma is the vector field V(t) along gamma satisfying:

```
  nabla_{gamma'(t)} V(t) = 0   for all t    (covariant derivative = 0)
  V(0) = v_0

  In coordinates: dV^k/dt + Sum_{i,j} Gamma^k_{ij} gamma'^i V^j = 0

  This is a linear ODE: solution exists and is unique for all t in [0,1].
  Result: v_1 = V(1) is the parallel transport of v_0 to gamma(1).

  Parallel transport is a linear isomorphism T_{gamma(0)} M -> T_{gamma(1)} M.
  It depends on the curve gamma (not just the endpoints, in general).
```

**Holonomy**: Transport v_0 around a closed loop and return to v_0's tangent space:

```
  The holonomy group Hol(p, nabla) = {P_gamma: gamma is a loop at p}
  is a subgroup of GL(T_p M).

  For flat connection: holonomy is trivial (P_gamma = identity for all loops).
  For curved spaces: non-trivial holonomy.

  Holonomy tells you about the curvature:
  - Holonomy group is determined by the curvature (Ambrose-Singer theorem).
  - Berger's classification of holonomy groups for irreducible, simply-connected
    Riemannian manifolds: O(n), U(n), SU(n), Sp(n), G2, Spin(7), + rank-1 symmetric spaces.
```

---

## Torsion

A connection has an associated **torsion tensor**:

```
  T(X, Y) = nabla_X Y - nabla_Y X - [X, Y]

  T is a (1,2) tensor: antisymmetric in X, Y.
  In coordinates: T^k_{ij} = Gamma^k_{ij} - Gamma^k_{ji}

  Torsion-free connection: T = 0, i.e., Gamma^k_{ij} = Gamma^k_{ji}
  (symmetric in lower indices)
```

**Geometric meaning of torsion**: When you transport a vector X along Y and Y along X (infinitesimally), the resulting parallelogram "gap" is measured by torsion. A torsion-free connection closes the gap: the infinitesimal parallelogram closes up.

---

## Levi-Civita Connection

**Fundamental theorem of Riemannian geometry**: On a Riemannian manifold (M,g), there exists a unique connection nabla that is:
1. **Torsion-free**: nabla_X Y - nabla_Y X = [X,Y]
2. **Metric-compatible**: nabla_X g = 0, i.e., X(g(Y,Z)) = g(nabla_X Y, Z) + g(Y, nabla_X Z)

This is the **Levi-Civita connection**.

**Christoffel symbols** (from the metric):

```
  Gamma^k_{ij} = (1/2) g^{kl} (partial_i g_{jl} + partial_j g_{il} - partial_l g_{ij})

  This formula expresses the Christoffel symbols entirely in terms of g_{ij} and its derivatives.
  No extra data needed: the metric determines the connection uniquely.

  Properties guaranteed:
  Gamma^k_{ij} = Gamma^k_{ji}                    (torsion-free)
  Sum_k Gamma^k_{ij} g_{kl} = sum of metric derivatives  (metric-compatible)
```

**Geometric significance**: Parallel transport along any curve preserves the metric:

```
  If V, W are parallel along gamma (nabla_{gamma'} V = 0, nabla_{gamma'} W = 0):
  g(V, W) = constant along gamma.

  In particular: ||V|| = constant (parallel transport is an isometry of fibers).
  This is why the Levi-Civita connection is the "right" one for Riemannian geometry.
```

---

## Covariant Derivative Along a Curve

For a vector field V along a curve gamma: [a,b] -> M:

```
  DV/dt = nabla_{gamma'(t)} V

  In coordinates: (DV/dt)^k = dV^k/dt + Gamma^k_{ij} gamma'^i V^j

  This is the "rate of change of V as seen from the curved space."

  GEODESICS in terms of covariant derivative:
  gamma is a geodesic iff  D gamma'/dt = 0
  (the velocity vector is parallel transported along the curve)

  Geodesics = curves with zero acceleration in the curved sense.
```

---

## Extending to Tensor Fields

The covariant derivative extends to all tensor fields:

```
  For a function f: nabla_X f = X(f)   (directional derivative)
  For a vector field V: nabla_X V  (as defined above)
  For a 1-form omega: (nabla_X omega)(Y) = X(omega(Y)) - omega(nabla_X Y)

  Leibniz rule: nabla_X (T tensor S) = (nabla_X T) tensor S + T tensor (nabla_X S)

  For a (1,1) tensor T:
  (nabla_X T)(Y) = nabla_X(T(Y)) - T(nabla_X Y)

  Coordinate formula for (r,s) tensor T:
  (nabla_k T)^{i1...ir}_{j1...js} = partial_k T^{i1...}_{j1...}
    + Sum_{a} Gamma^{ia}_{km} T^{...m...}_{j1...} - Sum_b Gamma^m_{kj_b} T^{i1...}_{...m...}

  (One Gamma term with + for each upper index, one with - for each lower index)
```

---

## The Divergence and Laplacian

With a Riemannian metric and Levi-Civita connection:

```
  DIVERGENCE of a vector field X:
  div X = Sum_i nabla_i X^i = (1/sqrt(g)) partial_i(sqrt(g) X^i)

  LAPLACE-BELTRAMI OPERATOR on functions:
  Delta f = div(grad f) = (1/sqrt(g)) partial_i(g^{ij} sqrt(g) partial_j f)

  In flat R^n: Delta f = Sum_i partial_i^2 f   (ordinary Laplacian)
  On S^2 (round metric): Delta f = (1/sin theta) partial_theta(sin theta partial_theta f) + (1/sin^2 theta) partial_phi^2 f

  Eigenvalues of Delta on S^2: -l(l+1) for l = 0, 1, 2, ...
  Eigenfunctions: spherical harmonics Y_l^m.
```

---

## Connections on Vector Bundles

The connection concept extends beyond TM to any vector bundle E over M:

```
  A connection on E: nabla: Gamma(TM) x Gamma(E) -> Gamma(E)
  Same axioms as before: tensorial in X, Leibniz in the section.

  CURVATURE of connection on E:
  F(X,Y) s = nabla_X nabla_Y s - nabla_Y nabla_X s - nabla_{[X,Y]} s

  For Levi-Civita connection: F = R (Riemann curvature tensor)
  For gauge connections: F = field strength (see 08-FIBER-BUNDLES)

  U(1) connection over R^4:  F = electromagnetic field strength (F_{mu nu})
  SU(2) connection: F = weak nuclear field strength
  SU(3) connection: F = strong nuclear (gluon) field strength
```

This is the bridge to physics: gauge fields ARE connections on principal bundles, and their curvature is the field strength.

---

## Decision Cheat Sheet

| Concept | Definition | Key Property |
|---|---|---|
| Affine connection nabla | Derivative operator, Leibniz rule | Chart-independent differentiation |
| Christoffel symbols Gamma^k_{ij} | nabla_{partial_i} partial_j = Gamma partial_k | Not tensors; encode connection |
| Parallel transport P_gamma | Solve nabla_{gamma'} V = 0 | Preserves metric (Levi-Civita) |
| Holonomy | Parallel transport around loops | Measures curvature globally |
| Torsion T | nabla_X Y - nabla_Y X - [X,Y] | 0 for Levi-Civita |
| Levi-Civita | Torsion-free + metric-compatible | Unique; determined by g |
| Geodesic equation | D gamma'/dt = 0 | Zero covariant acceleration |
| Covariant derivative along curve | DV/dt = nabla_{gamma'} V | Generalizes d/dt in curved space |

---

## Common Confusion Points

**"The Christoffel symbols are the components of the connection tensor."**
No — Christoffel symbols are NOT the components of a tensor. They transform with an extra inhomogeneous term under coordinate changes. This is the whole point: a connection is a geometric structure that is not captured by any tensor alone. The non-tensorial transformation law of Gamma is what allows nabla_X V to be tensorial.

**"Parallel transport preserves the vector."**
Parallel transport preserves the inner product between vectors (length and angle), not the vector itself (in any ambient sense). When you parallel transport a vector along a curve on a curved manifold, the vector "rotates" relative to any fixed external frame but stays "unchanged" in the intrinsic sense of the manifold.

**"The Levi-Civita connection is the only connection on a Riemannian manifold."**
It is the only TORSION-FREE, METRIC-COMPATIBLE connection. There are infinitely many other connections (add any (1,2) tensor to the Christoffel symbols). But Levi-Civita is the canonical one determined entirely by the metric, which is why it is used in Riemannian geometry and GR.

**"Covariant derivative and Lie derivative measure the same thing."**
They are different. The Lie derivative L_X V = [X,V] measures how V changes under the flow of X (requires only the smooth structure). The covariant derivative nabla_X V requires a connection and measures how V changes along X in the connection's sense of "parallel." They agree only in special cases.
