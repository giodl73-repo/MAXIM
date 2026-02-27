# Differential Geometry — Landscape Overview

## The Big Picture

Differential geometry extends calculus from flat Euclidean spaces to curved spaces (manifolds). The central insight: local coordinates exist everywhere, but the global space need not be flat.

```
DIFFERENTIAL GEOMETRY — DEPENDENCY STRUCTURE
+====================================================================+
|  LAYER 1: SMOOTH FOUNDATIONS                                       |
|  ┌──────────────────────┐                                          |
|  │ SMOOTH MANIFOLDS (01)│ charts, atlases, smooth maps             |
|  └──────────┬───────────┘                                          |
|             ▼                                                      |
|  LAYER 2: TANGENT MACHINERY                                        |
|  ┌──────────────────────┐                                          |
|  │ TANGENT BUNDLES (02) │ TM, T*M, vector fields, tensor fields   |
|  └──┬─────────┬─────────┘                                         |
|     │         │                                                    |
|     ▼         ▼                                                    |
|  LAYER 3: THREE BRANCHES (additional structures on M)              |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐ |
|  │ FORMS (03)   │  │ METRIC (04)  │  │ PRINCIPAL BUNDLES (08)   │ |
|  │ k-forms, d   │  │ g_ij, geod.  │  │ P → M, gauge theories   │ |
|  │ Stokes, de   │  │ exp map      │  │ Yang-Mills, holonomy     │ |
|  │ Rham cohom.  │  │              │  │                          │ |
|  └──────────────┘  └──────┬───────┘  └──────────┬───────────────┘ |
|                           ▼                      ▼                 |
|  LAYER 4: CURVATURE AND STRUCTURE                                  |
|  ┌────────────────────────────────────────────────────────────┐    |
|  │ CONNECTIONS (05): covariant derivative, parallel transport │    |
|  │ CURVATURE (06): Riemann tensor, Ricci, sectional, Gauss-B │    |
|  │ LIE GROUPS (07): SO(n), SE(3), Lie algebra, exp map       │    |
|  └──────────────────────────┬─────────────────────────────────┘    |
|                             ▼                                      |
|  LAYER 5: APPLICATIONS (09)                                        |
|  ┌────────────────────────────────────────────────────────────┐    |
|  │ General Relativity: Lorentzian manifolds, Einstein eqs.    │    |
|  │ Gauge Theories: Yang-Mills, Standard Model                 │    |
|  │ Symplectic Geometry: Hamiltonian mechanics, integrators     │    |
|  │ Information Geometry: Fisher metric, natural gradient       │    |
|  │ Geometric Deep Learning: equivariant networks, Riem. optim │    |
|  │ Robotics: configuration spaces, SE(3), kinematics          │    |
|  └────────────────────────────────────────────────────────────┘    |
+====================================================================+
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
  information-geometry/ (→ 09-APPLICATIONS)
    Statistical manifolds: parametric family {p(x; θ)} is a manifold.
    Fisher information metric: g_ij(θ) = E[∂_i log p · ∂_j log p]
      is a canonical Riemannian metric on the parameter space.
    Natural gradient descent = Riemannian SGD with the Fisher metric.
    Exponential families are flat (zero curvature) under the e-connection.
    This is the most direct DG → ML bridge: the Fisher metric IS
      a Riemannian metric, and natural gradient IS Riemannian optimization.
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

## Decision Cheat Sheet

| When you need to... | Use | Because |
|---|---|---|
| Optimize a loss function on SO(3) or SPD matrices | 04-RIEMANNIAN + 09-APPLICATIONS §ML | Riemannian gradient descent respects manifold constraints |
| Formulate electromagnetism or Yang-Mills covariantly | 08-FIBER-BUNDLES + 05-CONNECTIONS | F = dA is curvature of a principal bundle connection |
| Understand why gravity curves spacetime | 06-CURVATURE + 09-APPLICATIONS §GR | Einstein eqs.: Ricci curvature = stress-energy |
| Build an equivariant neural network | 07-LIE-GROUPS + 08-FIBER-BUNDLES + 09 §ML | Features are bundle sections; equivariance = gauge symmetry |
| Plan robot motion through SE(3) | 07-LIE-GROUPS + 09-APPLICATIONS §Robotics | Robot configurations live on Lie groups |
| Use natural gradient for ML training | 04-RIEMANNIAN + 09-APPLICATIONS §Info. Geom. | Natural gradient = Riemannian gradient with Fisher metric |
| Prove a topological identity via integration | 03-DIFFERENTIAL-FORMS | Stokes' theorem unifies all classical integral theorems |
| Understand parallel transport and holonomy | 05-CONNECTIONS | Connection defines "constant" along a path; holonomy = path dependence |
| Simulate Hamiltonian dynamics preserving energy | 09-APPLICATIONS §Symplectic | Symplectic integrators preserve the symplectic 2-form |

---

## Common Confusion Points

**"A manifold is just a curved surface."**
Surfaces (2-manifolds embedded in R^3) are the most visual example, but manifolds can be any dimension and need not be embedded in any ambient space. The definition is intrinsic: a topological space with locally Euclidean charts. S^3 (3-sphere) is a 3-manifold that lives in R^4; spacetime is a 4-manifold that does not live in any ambient space.

**"Differential geometry requires a metric."**
No. Much of differential geometry (manifolds, tangent bundles, differential forms, connections, Lie groups) is purely about smooth structure, not metric structure. Riemannian geometry adds a metric. Symplectic geometry adds a closed non-degenerate 2-form. These are additional structures on top of the smooth manifold.

**"Topology/ and differential-geometry/ are the same."**
Topology studies properties invariant under continuous deformations. DG requires smooth deformations and studies metric properties. The Euler characteristic (topology) constrains which curvature functions are possible on a surface (Gauss-Bonnet). topology/ covers the base; differential-geometry/ adds the smooth and metric structure.
