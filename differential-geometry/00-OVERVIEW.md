# Differential Geometry — Landscape Overview

## The Big Picture

Differential geometry extends calculus from flat Euclidean spaces to curved spaces (manifolds). The central insight: local coordinates exist everywhere, but the global space need not be flat.

<!-- @editor[diagram/P2]: Landscape diagram lists the 9 modules in boxes but doesn't show the dependency arrows — which modules build on which, and which structures branch off the core (smooth manifold → tangent bundle → {metric branch, forms branch, connection branch}). Also missing: symplectic geometry and information geometry as named structures in the landscape, even though they are first-class applications. Rework to show layered dependency: smooth structure → tangent/cotangent bundles → {Riemannian (metric), symplectic (2-form), principal bundles (gauge)} → curvature → applications. -->
```
+------------------------------------------------------------------+
|              DIFFERENTIAL GEOMETRY LANDSCAPE                     |
+------------------------------------------------------------------+
|                                                                  |
|  SMOOTH MANIFOLDS (01)           TANGENT BUNDLES (02)           |
|  +-------------------+           +-------------------+          |
|  | Coordinate charts |           | Tangent spaces    |          |
|  | Smooth maps       |           | Vector fields     |          |
|  | Submanifolds      |           | Differential forms|          |
|  | Partition of unity|           | Tensor fields     |          |
|  +-------------------+           +-------------------+          |
|          |                                |                      |
|          v                                v                      |
|  DIFFERENTIAL FORMS (03)        RIEMANNIAN GEOMETRY (04)        |
|  +-------------------+           +-------------------+          |
|  | k-forms           |           | Metric tensor     |          |
|  | Exterior algebra  |           | Geodesics         |          |
|  | Stokes' theorem   |           | Exponential map   |          |
|  | de Rham cohomology|           | Completeness      |          |
|  +-------------------+           +-------------------+          |
|                                           |                      |
|  CONNECTIONS (05)               CURVATURE (06)                  |
|  +-------------------+           +-------------------+          |
|  | Covariant deriv.  |           | Riemann tensor    |          |
|  | Parallel transport|           | Ricci tensor      |          |
|  | Levi-Civita       |           | Scalar curvature  |          |
|  +-------------------+           +-------------------+          |
|                                                                  |
|  LIE GROUPS (07)                FIBER BUNDLES (08)              |
|  +-------------------+           +-------------------+          |
|  | Manifold + group  |           | E -> M -> B       |          |
|  | Lie algebra       |           | Gauge theories    |          |
|  | SO(3), SE(3)      |           | Principal bundles |          |
|  +-------------------+           +-------------------+          |
|                                                                  |
|  APPLICATIONS (09): GR, gauge theories, robotics, ML            |
+------------------------------------------------------------------+
```

---

## Why Differential Geometry?

The need arises wherever you have a space that locally looks Euclidean but globally is curved.

```
  R^n (flat space):
  One coordinate chart covers everything.
  "Straight lines" (geodesics) are literally straight.
  Parallel transport is trivial — just keep the vector constant.

  2-sphere S^2 (Earth's surface):
  No single chart covers everything (map projection distortion).
  "Straight lines" are great circles — the shortest paths curve.
  Parallel transport around a loop rotates the vector.
  The holonomy angle IS the Gaussian curvature integrated over the region.

  Spacetime (General Relativity):
  4-dimensional Lorentzian manifold.
  Matter curves the manifold; curved manifold controls motion.
  Geodesics = free-fall trajectories.
  Einstein field equations: Ricci curvature ~ stress-energy tensor.
```

---

## The Coordinate-Free Philosophy

Classical multivariate calculus ties everything to R^n coordinates. Differential geometry makes structure independent of coordinate choice — just as good type systems make code independent of representation choices.

```
  COORDINATE-BOUND (classical):        COORDINATE-FREE (DG):
  "f: R^n -> R, partial f/partial x_i"  "f: M -> R, df is a 1-form"
  "tangent vector (v_1,...,v_n)"         "derivation on smooth functions"
  "metric g_{ij} in coordinates"         "symmetric bilinear form on TM"
  "curl, div, grad on R^3"               "exterior derivative d on forms"

  Coordinate-free is harder to learn but:
  - Invariant under coordinate changes
  - Generalizes to any manifold
  - Reveals the real structure
  - Required for GR, gauge theories, and information geometry
```

**The type-theoretic parallel**: A coordinate-free object is like a well-typed abstraction — its behavior is specified without reference to internal representation. A vector field on M is a section of TM; its components in a chart are just one representation.

---

## Module Map

```
  00-OVERVIEW (this file)
  |
  +-- 01-MANIFOLDS              Smooth manifolds, charts, atlases, smooth maps
  |
  +-- 02-TANGENT-BUNDLES        TM, T*M, vector fields, 1-forms, tensor fields
  |
  +-- 03-DIFFERENTIAL-FORMS     k-forms, d, wedge product, Stokes, de Rham
  |
  +-- 04-RIEMANNIAN-GEOMETRY    Metric, geodesics, exponential map, completeness
  |
  +-- 05-CONNECTIONS            Affine connections, covariant derivative,
  |                             parallel transport, Levi-Civita
  |
  +-- 06-CURVATURE              Riemann tensor, Ricci, scalar, sectional curvature,
  |                             Bianchi identities
  |
  +-- 07-LIE-GROUPS             Lie groups, Lie algebras, exp map, SO(3), SE(3)
  |
  +-- 08-FIBER-BUNDLES          Vector/principal bundles, gauge theories, holonomy
  |
  +-- 09-APPLICATIONS           GR, Yang-Mills, robot kinematics, ML on manifolds
```

---

## Key Connections to Other Library Directories

```
  topology/
    Manifolds are topological spaces with extra (smooth) structure.
    topology/ covers the topological foundation.
    DG adds: smooth structure, differential calculus, metric.

  mathematics/
    Linear algebra: tangent spaces are vector spaces
    Multivariable calculus: the computational substrate
    Abstract algebra: Lie groups are simultaneously groups and manifolds

  physics/
    General relativity: Lorentzian manifolds, Einstein equations
    Gauge theories: principal bundles, connections, curvature = field strength
    Electromagnetism: F = dA (curvature of U(1) principal bundle)
    Mechanics: phase space is a symplectic manifold (Hamiltonian formalism)

  probability-statistics/
    Information geometry: statistical manifolds with Fisher metric
    09-INFORMATION-GEOMETRY bridges directly to this directory

  data-science/
    ML on manifolds: optimization on S^n, SO(n), positive definite matrices
    Riemannian SGD, natural gradient (= natural gradient of Fisher metric)
    Geometric deep learning (gauge equivariance in ML)
<!-- @editor[content/P2]: Information geometry is listed here in a subordinate bullet but deserves its own cross-reference entry — statistical manifolds with the Fisher information metric are a major application domain (natural gradient descent, amortized inference, exponential families as curved submanifolds). The Fisher metric is a Riemannian metric on the space of probability distributions; this bridge from DG to ML is the most direct and should be elevated. -->
```

---

## The Central Objects (Quick Reference)

| Object | Definition | Lives In |
|--------|-----------|---------|
| Manifold M | Topological space locally homeomorphic to R^n | — |
| Smooth map f: M -> N | Smooth in every chart | — |
| Tangent vector at p | Equivalence class of curves through p | T_p M |
| Vector field | Smooth section of TM | Gamma(TM) |
| Differential form (1-form) | Smooth section of T*M | Omega^1(M) |
| k-form | Antisymmetric (0,k) tensor field | Omega^k(M) |
| Riemannian metric g | Smooth, positive-definite (0,2) tensor | Sym^2(T*M) |
| Connection nabla | Map (X, Y) -> nabla_X Y, linear in X | — |
| Curvature R | R(X,Y)Z = nabla_X nabla_Y Z - nabla_Y nabla_X Z - nabla_{[X,Y]} Z | T^{1,3}(M) |
| Lie group G | Manifold + compatible group structure | — |
| Lie algebra g | T_e G (tangent space at identity) | — |
| Principal bundle | P -> M with structure group G | Bundle over M |

---

## Dimension Examples

```
  n=0: Point (trivial)
  n=1: Curves (circles, lines, figure-8 is NOT a manifold)
  n=2: Surfaces (S^2, torus T^2, Klein bottle, hyperbolic plane)
  n=3: 3-manifolds (S^3, RP^3, Thurston geometries — 8 types)
  n=4: Spacetime (Lorentzian), S^4 (topological complications!)
  n=6: Complex 3-manifolds (Calabi-Yau spaces in string theory)
  inf: Function spaces (Banach/Hilbert manifolds)
```

---

<!-- @editor[structure/P2]: Cheat sheet is a navigation index, not a decision tool — rows should be "use X when Y" (e.g., "Need to optimize a loss on rotation matrices → 04-RIEMANNIAN-GEOMETRY + 09-APPLICATIONS §ML; need to formulate a gauge theory → 08-FIBER-BUNDLES + 05-CONNECTIONS"). Redirect pointers alone don't guide decisions. -->
## Decision Cheat Sheet

| I need to... | See |
|---|---|
| Understand what a manifold is rigorously | 01-MANIFOLDS |
| Work with vectors, covectors, tensors on manifolds | 02-TANGENT-BUNDLES |
| Generalize Stokes'/Green's/divergence theorem | 03-DIFFERENTIAL-FORMS |
| Measure lengths, angles, geodesics | 04-RIEMANNIAN-GEOMETRY |
| Define derivatives of vector fields on curved spaces | 05-CONNECTIONS |
| Compute and interpret curvature | 06-CURVATURE |
| Understand rotation groups, rigid body motion | 07-LIE-GROUPS |
| Understand gauge theories, connections on bundles | 08-FIBER-BUNDLES |
| See how this connects to GR / ML / robotics | 09-APPLICATIONS |

---

## Common Confusion Points

**"A manifold is just a curved surface."**
Surfaces (2-manifolds embedded in R^3) are the most visual example, but manifolds can be any dimension and need not be embedded in any ambient space. The definition is intrinsic: a topological space with locally Euclidean charts. S^3 (3-sphere) is a 3-manifold that lives in R^4; spacetime is a 4-manifold that does not live in any ambient space.

**"Differential geometry requires a metric."**
No. Much of differential geometry (manifolds, tangent bundles, differential forms, connections, Lie groups) is purely about smooth structure, not metric structure. Riemannian geometry adds a metric. Symplectic geometry adds a closed non-degenerate 2-form. These are additional structures on top of the smooth manifold.

**"Topology/ and differential-geometry/ are the same."**
Topology studies properties invariant under continuous deformations. DG requires smooth deformations and studies metric properties. The Euler characteristic (topology) constrains which curvature functions are possible on a surface (Gauss-Bonnet). topology/ covers the base; differential-geometry/ adds the smooth and metric structure.
