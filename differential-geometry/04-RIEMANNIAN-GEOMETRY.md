# Riemannian Geometry

## The Big Picture

A Riemannian metric turns a smooth manifold into a metric space with notions of length, angle, area, and volume. Geodesics generalize straight lines; the exponential map connects linear algebra at a point to the curved geometry globally.

```
+------------------------------------------------------------------+
|                   RIEMANNIAN GEOMETRY OVERVIEW                   |
+------------------------------------------------------------------+
|                                                                  |
|  RIEMANNIAN METRIC g                                            |
|  Smooth assignment of inner product to each tangent space.      |
|  g = g_{ij} dx^i tensor dx^j   (in coordinates)                |
|                                                                  |
|       |                                                          |
|       v                                                          |
|  +------------------+  +------------------+  +--------------+  |
|  | LENGTH of curves |  | ANGLE between    |  | VOLUME of    |  |
|  | L = Int |gamma'| |  | vectors          |  | regions      |  |
|  +------------------+  +------------------+  +--------------+  |
|       |                                                          |
|       v                                                          |
|  GEODESICS (locally length-minimizing curves)                   |
|  Solve: gamma'' + Gamma^k_{ij} gamma'^i gamma'^j = 0           |
|                                                                  |
|       |                                                          |
|       v                                                          |
|  +--------------------+  +-------------------------+           |
|  | EXPONENTIAL MAP    |  | RIEMANNIAN DISTANCE     |           |
|  | exp_p: T_p M -> M  |  | d(p,q) = inf_curves L   |           |
|  | geodesics from p   |  | (metric space structure) |          |
|  +--------------------+  +-------------------------+           |
|                                                                  |
+------------------------------------------------------------------+
```

---

## The Riemannian Metric

A **Riemannian metric** g on M is a smooth (0,2) tensor field that is:
- Symmetric: g(X,Y) = g(Y,X)
- Positive definite: g(X,X) > 0 for X != 0

```
  In local coordinates (x^1,...,x^n):
  g = Sum_{i,j} g_{ij} dx^i tensor dx^j

  g_{ij}(p) = g(partial_i, partial_j)|_p    (smooth matrix-valued function)
  g_{ij} = g_{ji}  (symmetry)
  g_{ij} is positive definite as a matrix at each point.

  The inverse g^{ij}: g_{ik} g^{kj} = delta^j_i
  (raising and lowering indices, see 02-TANGENT-BUNDLES musical isomorphisms)
```

**Existence**: Every smooth manifold admits a Riemannian metric (using partition of unity to glue together local flat metrics). This is not trivial — it relies on the smoothness of M.

**Induced metric**: If F: M -> (N, h) is an immersion/embedding, the induced metric on M is the pullback:

```
  g = F* h    (g_{ij} = h_{kl} partial F^k/partial x^i partial F^l/partial x^j)

  Example: Standard metric on S^2 from inclusion i: S^2 -> R^3:
  g_{S^2} = i*(g_{R^3}) = standard round metric.
```

**Riemannian volume form**: On an oriented Riemannian manifold:

```
  Vol_M = sqrt(det g) dx^1 wedge ... wedge dx^n

  This allows integration of functions: Integral_M f dVol = Integral f sqrt(det g) dx
  Volume of M: Vol(M) = Integral_M dVol
```

---

## Length, Distance, and Geodesics

**Length of a curve**: For a smooth curve gamma: [a,b] -> M:

```
  L(gamma) = Integral_a^b sqrt(g(gamma'(t), gamma'(t))) dt
           = Integral_a^b ||gamma'(t)||_g dt
```

**Riemannian distance**:

```
  d(p, q) = inf_{gamma: p->q} L(gamma)

  This makes (M, d) a metric space.
  The infimum may not be achieved (e.g., antipodal points deleted from S^2).
  When achieved, the minimizing curve is a geodesic.
```

**Geodesics**: Locally length-minimizing curves. They satisfy the geodesic equation:

```
  gamma''^k + Sum_{i,j} Gamma^k_{ij} gamma'^i gamma'^j = 0

  Where Gamma^k_{ij} are the Christoffel symbols (defined in 05-CONNECTIONS):
  Gamma^k_{ij} = (1/2) g^{kl} (partial_i g_{jl} + partial_j g_{il} - partial_l g_{ij})

  This is a system of nonlinear ODEs.
  Given initial position gamma(0) = p and initial velocity gamma'(0) = v:
  Unique geodesic exists for t in some interval.
```

**Geodesics are not globally minimizing**: A geodesic is locally minimizing — it minimizes length for small enough intervals. Globally, there may be shorter paths. Example: On S^2, great circle arcs are geodesics. For points that are not antipodal, the short arc minimizes; the long arc is still a geodesic but not minimizing.

---

## The Exponential Map

The exponential map encodes the "go straight from p in direction v" operation:

```
  exp_p: T_p M -> M (defined on a neighborhood of 0 in T_p M)

  exp_p(v) = gamma_v(1)

  where gamma_v is the geodesic starting at p with velocity v.

  PROPERTIES:
  exp_p(0) = p
  d(exp_p)_0 = id_{T_p M}  (exponential map is a local diffeomorphism near 0)
  The curve t |-> exp_p(tv) is the geodesic from p in direction v.
```

**Normal coordinates**: exp_p provides a chart around p (for small enough neighborhood). In these **Riemann normal coordinates**:

```
  g_{ij}(p) = delta_{ij}              (metric is flat at p)
  partial_k g_{ij}(p) = 0             (no first-order curvature correction)
  Gamma^k_{ij}(p) = 0                 (Christoffel symbols vanish at p)

  The curvature appears at second order:
  g_{ij} = delta_{ij} - (1/3) R_{ikjl} x^k x^l + O(|x|^3)

  Normal coordinates are the "most Euclidean" chart at p.
```

**Logarithmic map**: log_p = exp_p^{-1} (inverse of exp_p on the cut locus complement):

```
  log_p(q) in T_p M  is the "initial velocity" to reach q from p by geodesic.
  d(p, q) = ||log_p(q)||_g

  The vector log_p(q) "points from p to q in the tangent space at p."
  Used in Riemannian optimization: optimization algorithms generalize by
  replacing Euclidean steps with geodesic steps (using exp and log maps).
```
**SPD manifold Sym+(n) — the key ML example**: The manifold of symmetric positive definite n×n matrices with the affine-invariant metric g_A(U,V) = tr(A^{-1}U A^{-1}V) is the most important concrete Riemannian manifold for ML. The exp and log maps have closed forms: Exp_A(U) = A^{1/2} exp(A^{-1/2} U A^{-1/2}) A^{1/2}, Log_A(B) = A^{1/2} log(A^{-1/2} B A^{-1/2}) A^{1/2}. Geodesic distance: d(A,B) = ||log(A^{-1/2} B A^{-1/2})||_F. Applications: covariance estimation (each data covariance matrix is a point on Sym+(n)), diffusion tensor MRI (each voxel has a 3×3 SPD diffusion tensor), and Gaussian process kernel learning. Riemannian gradient descent on Sym+(n) automatically preserves positive definiteness — no projection step needed.

---

## Cut Locus and Completeness

**Cut locus**: The cut locus of p is the set of points where geodesics from p stop being minimizing. Beyond the cut locus, exp_p is not injective.

```
  Example: On S^2 with standard metric, the cut locus of the north pole N
  is the south pole S. Every geodesic from N reaches S after distance pi.
  exp_N is a diffeomorphism on B(0,pi) in T_N S^2 and the preimage of S
  is the entire sphere of radius pi.
```

**Hopf-Rinow theorem** (completeness):

```
  For a connected Riemannian manifold M, the following are equivalent:
  1. M is geodesically complete: every geodesic extends to all t in R.
  2. M is metrically complete: every Cauchy sequence converges.
  3. exp_p is defined on all of T_p M for some (equiv. every) p in M.
  4. Closed bounded sets in M are compact.

  Corollary: If M is complete, any two points are connected by a minimizing geodesic.

  Compact manifolds are always complete.
  R^n with a complete metric is complete.
  R^n \ {0} is NOT complete (geodesics can reach 0 in finite time).
```

---

## Sectional Curvature

The curvature of a Riemannian manifold can be encoded in sectional curvatures:

```
  For a 2-dimensional subspace sigma = span(X, Y) of T_p M:
  K(sigma) = g(R(X,Y)Y, X) / [g(X,X)g(Y,Y) - g(X,Y)^2]

  (R is the Riemann curvature tensor, see 06-CURVATURE)

  This is the "Gaussian curvature of the 2-plane sigma through p."

  Constant curvature spaces:
  K = 0:   Flat: R^n, T^n (torus, locally flat)
  K = +1:  Sphere S^n (round metric)
  K = -1:  Hyperbolic space H^n (Poincare disk model)
```

**Constant curvature space forms**:

```
  Dimension n, constant sectional curvature K:
  K > 0: Sphere S^n / Gamma (Gamma = discrete group of isometries)
  K = 0: R^n / Gamma (flat tori, flat Klein bottle, ...)
  K < 0: H^n / Gamma (hyperbolic manifolds — Thurston's geometrization)
```

**Behavior of geodesics by curvature sign**:

```
  K > 0 (positive curvature):
  Geodesics tend to converge. Focal points exist.
  Sphere: all geodesics from north pole meet at south pole.

  K = 0 (flat):
  Geodesics remain parallel (or diverge linearly).
  R^n: parallel lines stay parallel.

  K < 0 (negative curvature):
  Geodesics diverge exponentially.
  Hyperbolic plane: many parallels to a given line through an external point.
```

---

## Jacobi Fields and Conjugate Points

**Jacobi fields** measure how a family of geodesics spreads apart:

```
  If {gamma_s} is a family of geodesics with s a parameter:
  J(t) = d/ds gamma_s(t)|_{s=0}  is a Jacobi field along gamma_0.

  Jacobi equation: J'' + R(J, gamma') gamma' = 0
  (a linear second-order ODE along the geodesic)

  J(0) = 0, J'(0) = v  =>  unique Jacobi field starting at p with initial spread v.
```

**Conjugate points**: q = gamma(t_0) is conjugate to p = gamma(0) if there is a non-zero Jacobi field with J(0) = J(t_0) = 0.

```
  Geometric meaning: nearby geodesics from p refocus at q.
  Beyond the first conjugate point, the geodesic is no longer minimizing.

  Connection to Morse theory: index of the geodesic (as a critical point
  of energy functional) = number of conjugate points counted with multiplicity.
```

---

## Isometries and Space of Riemannian Manifolds

A map F: (M,g) -> (N,h) is an **isometry** if F*h = g (pullback of metric = metric):

```
  Isometries preserve all metric properties: lengths, angles, curvature.
  They are the "symmetries" of a Riemannian manifold.

  Isometry group Isom(M,g): all isometries M -> M.
  For S^n with round metric: Isom = O(n+1)
  For R^n with flat metric:  Isom = O(n) semi-direct product R^n  (rigid motions)
  For H^n hyperbolic:        Isom = O(n,1)  (Lorentz group!)
```

**Homogeneous spaces**: M is homogeneous if Isom(M) acts transitively — you can move any point to any other point by an isometry. Homogeneous spaces have constant sectional curvature. They are of the form G/H where G is a Lie group and H is a closed subgroup.

## Information Geometry — Fisher Metric as Riemannian Geometry

For a parametric family {p(x; θ) : θ ∈ Θ ⊂ R^n}, the **Fisher information metric** makes the parameter space a Riemannian manifold:

    g_{ij}(θ) = E_{p(·;θ)}[∂_i log p(x;θ) · ∂_j log p(x;θ)]

This is positive semi-definite (positive definite for identifiable models), symmetric, and transforms correctly under reparametrization — a bona fide Riemannian metric.

**Natural gradient descent** (Amari 1998) = Riemannian gradient descent with the Fisher metric: θ_{t+1} = θ_t − η g^{-1}(θ_t) ∇L(θ_t). The Fisher metric g^{-1} acts as an adaptive preconditioner that accounts for the curvature of the statistical manifold. This is why natural gradient outperforms vanilla SGD on curved loss landscapes: it follows geodesics rather than coordinate lines.

**Exponential families are flat**: For an exponential family p(x; η) = h(x) exp(η·T(x) − A(η)), the Fisher metric under natural parameters η gives zero curvature (the e-connection is flat). This means: Newton's method on the natural parameter space converges in one step, and the Bregman divergence D_A(η||η') = KL(p_η || p_{η'}) is the squared geodesic distance. Practical approximations: K-FAC ≈ block-diagonal Fisher, Shampoo ≈ Kronecker-factored Fisher.

---

## Decision Cheat Sheet

| Concept | Formula/Tool | Application |
|---|---|---|
| Riemannian metric | g = g_{ij} dx^i dx^j (PD) | All geometric quantities |
| Length of curve | L = Int ||gamma'||_g dt | Distance computation |
| Geodesic equation | gamma'' + Gamma gamma'gamma' = 0 | Shortest paths, free fall |
| Exponential map | exp_p(v) = geodesic from p in direction v | Normal coords, optimization |
| Log map | log_p(q) = initial velocity to q | Riemannian optimization |
| Sectional curvature | K(sigma) = R(X,Y)Y,X normalized | Curvature at a point, plane |
| Completeness | Hopf-Rinow: metrically iff geodesically | When geodesics exist globally |
| Jacobi field | J'' + R(J,gamma')gamma' = 0 | Geodesic deviation, conjugate pts |

---

## Common Confusion Points

**"Geodesics are the shortest paths."**
Only locally and when unique. A geodesic is a locally minimizing curve — it satisfies the geodesic equation. Globally, there may be multiple geodesics between two points, only one of which is shortest. On S^2, both great circle arcs from p to q are geodesics; only the shorter one minimizes.

**"The Riemannian distance is always achieved."**
Only on complete manifolds (Hopf-Rinow). On incomplete manifolds (like R^n minus a point), sequences of curves can approach an infimum without a minimizer existing.

**"Normal coordinates make things flat globally."**
Normal coordinates make the metric flat at a single point p — Christoffel symbols vanish at p and the metric agrees with the Euclidean metric to first order. But curvature appears at second order (the Riemann tensor terms). The metric is globally flat iff the curvature tensor vanishes.

**"The exponential map exp_p is the matrix exponential."**
For matrix Lie groups (which are Riemannian manifolds), the two coincide — the geodesic exponential map at the identity equals the matrix exponential when the metric is bi-invariant. For general Riemannian manifolds, exp_p is the geodesic exponential, which is a different construction.
