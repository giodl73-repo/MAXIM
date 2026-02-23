# 10 — Differential Geometry: Curvature, Geodesics, and the Shape of Spacetime

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  CURVES                SURFACES              RIEMANNIAN GEOMETRY
  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────────────────┐
  │ arc length       │  │ first fund. form │  │ covariant derivative ∇      │
  │ curvature κ      │→ │ second fund. form│→ │ parallel transport          │
  │ torsion τ        │  │ Gauss curvature K│  │ geodesics                   │
  │ Frenet-Serret    │  │ mean curvature H │  │ Riemann curvature tensor    │
  └──────────────────┘  └──────────────────┘  └─────────────────────────────┘
                                                            │
                                                            ▼
                                               GENERAL RELATIVITY
                                               Gμν = (8πG/c⁴)Tμν
                                               "Curvature = energy"

  KEY INSIGHT: Theorema Egregium (Gauss, 1827)
  Gaussian curvature K is INTRINSIC — measurable by an ant on the surface
  without reference to any ambient space.
  An ant can tell it's on a sphere (K>0), saddle (K<0), or flat plane (K=0).
  GR is built on this: spacetime geometry is intrinsic, not embedded in higher D.
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. Curves in ℝ³

### 1.1 Arc Length and Parameterization

```
  CURVE: γ: I → ℝ³,   γ(t) = (x(t), y(t), z(t))

  Arc length from t=a to t=b:
  s(t) = ∫ₐᵗ |γ'(τ)| dτ = ∫ₐᵗ √(ẋ²+ẏ²+ż²) dτ

  ARC LENGTH PARAMETERIZATION: |γ'(s)| = 1 (unit speed)
  Reparameterize by arc length s → tangent vector T = γ'(s) has unit length.

  UNIT TANGENT:   T(s) = γ'(s)        |T| = 1
  NORMAL vector:  N(s) = T'(s)/|T'(s)|  (points toward center of curvature)
  BINORMAL:       B(s) = T(s) × N(s)    (completes right-handed frame)
```

### 1.2 Frenet-Serret Formulas

```
  {T, N, B} form the FRENET-SERRET FRAME — an orthonormal frame moving along γ.

  FRENET-SERRET EQUATIONS:
  T' = κN               (T turns toward N at rate κ)
  N' = -κT + τB         (N pulled back by κ, twisted toward B by τ)
  B' = -τN              (B twists toward -N at rate τ)

  CURVATURE:  κ = |T'(s)| = |γ''(s)|  [how fast tangent turns, 1/radius]
  TORSION:    τ = -B'·N               [how fast curve twists out of plane]

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Straight line:  κ=0, τ=0    (no bending, no twisting)              │
  │  Circle of radius r: κ=1/r, τ=0   (constant bending, flat)          │
  │  Helix (r, pitch p): κ=r/(r²+p²), τ=p/(r²+p²)  (constant κ and τ) │
  │  Plane curve: τ=0 always (stays in its plane)                       │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 2. Surfaces in ℝ³ — First Fundamental Form

### 2.1 Surface Parameterization and Metric

```
  SURFACE: r: U ⊆ ℝ² → ℝ³,   r(u,v) = (x(u,v), y(u,v), z(u,v))

  Tangent vectors: rᵤ = ∂r/∂u,   rᵥ = ∂r/∂v

  FIRST FUNDAMENTAL FORM (metric tensor on surface):
  gᵢⱼ = rᵢ · rⱼ   where r₁=rᵤ, r₂=rᵥ

  ┌         ┐   ┌                  ┐
  │ g₁₁ g₁₂│ = │ rᵤ·rᵤ  rᵤ·rᵥ   │ = ┌E  F┐
  │ g₂₁ g₂₂│   │ rᵥ·rᵤ  rᵥ·rᵥ   │   └F  G┘
  └         ┘   └                  ┘
  E=|rᵤ|², F=rᵤ·rᵥ, G=|rᵥ|²   (classical notation)

  ARC LENGTH of curve u(t), v(t) on surface:
  ds² = E du² + 2F du dv + G dv²   (the line element)

  AREA of surface patch:
  dA = √(EG-F²) du dv = |rᵤ × rᵥ| du dv
```

### 2.2 The First Fundamental Form is Intrinsic

```
  The metric gᵢⱼ depends only on inner products of tangent vectors.
  An ant on the surface can measure distances and angles using gᵢⱼ.
  It cannot determine how the surface is embedded in ℝ³ from gᵢⱼ alone.

  ISOMETRIC SURFACES: same gᵢⱼ (same intrinsic geometry, can differ extrinsically)
  Example: cylinder and flat plane are locally isometric (you can unroll a cylinder).
  Both have K=0 (flat intrinsically), even though the cylinder "looks" curved in ℝ³.
```

---

## 3. Second Fundamental Form and Extrinsic Curvature

### 3.1 Normal Curvature

```
  UNIT NORMAL to surface: n = (rᵤ × rᵥ)/|rᵤ × rᵥ|

  SECOND FUNDAMENTAL FORM:
  Lᵢⱼ = r_{ij} · n   where r_{ij} = ∂²r/∂uⁱ∂uʲ

  ┌         ┐   ┌                  ┐
  │ L₁₁ L₁₂│ = │ rᵤᵤ·n  rᵤᵥ·n   │ = ┌ e  f ┐  (classical)
  │ L₂₁ L₂₂│   │ rᵥᵤ·n  rᵥᵥ·n   │   └ f  g ┘
  └         ┘   └                  ┘

  NORMAL CURVATURE in direction v: κₙ = Lᵢⱼvⁱvʲ / gᵢⱼvⁱvʲ

  This measures how the surface bends in the direction of v
  — an EXTRINSIC quantity (needs the embedding in ℝ³).
```

### 3.2 Shape Operator and Principal Curvatures

```
  SHAPE OPERATOR (Weingarten map) S: TₚM → TₚM
  Sᵢⱼ = gⁱᵏ Lₖⱼ   (raise index with inverse metric)

  PRINCIPAL CURVATURES κ₁, κ₂ = eigenvalues of S
  PRINCIPAL DIRECTIONS = corresponding eigenvectors (orthogonal)

  ┌──────────────────────────────────────────────────────────────────────┐
  │  GAUSSIAN CURVATURE: K = κ₁κ₂ = det(S) = det(L)/det(g)             │
  │  MEAN CURVATURE:     H = (κ₁+κ₂)/2 = ½ trace(S)                    │
  └──────────────────────────────────────────────────────────────────────┘

  SURFACE EXAMPLES:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Sphere radius R:  κ₁=κ₂=1/R,   K=1/R²>0,  H=1/R                │
  │  Saddle (monkey): κ₁>0, κ₂<0,   K<0                              │
  │  Cylinder radius R: κ₁=1/R, κ₂=0, K=0,   H=1/(2R)               │
  │  Flat plane:       κ₁=κ₂=0,   K=0,   H=0                        │
  │  Minimal surface:  κ₁=-κ₂,   H=0     (soap films)               │
  └────────────────────────────────────────────────────────────────────┘
```

---

## 4. Theorema Egregium

```
  GAUSS'S THEOREMA EGREGIUM (1827): "Remarkable Theorem"

  K = κ₁κ₂  is an INTRINSIC invariant.
  It depends only on gᵢⱼ, not on how the surface is embedded.

  Explicit formula in terms of metric:
  K = (R₁₂₁₂) / det(g)
  where R₁₂₁₂ is a component of the Riemann curvature tensor
  (which depends only on gᵢⱼ and its derivatives)

  CONCRETE CONSEQUENCES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  You cannot flatten a sphere without distortion.                    │
  │  (K=1/R²≠0 on sphere, K=0 on plane → not isometric)               │
  │  This is why maps of Earth always distort either area or angle.     │
  │                                                                     │
  │  You CAN flatten a cylinder (K=0 on both cylinder and plane).      │
  │  Unrolling a cylinder = isometric map.                              │
  │                                                                     │
  │  An ant can measure K by doing geometry:                            │
  │  Sum of angles of a geodesic triangle = π + K × (area)             │
  │  On sphere: triangle angles sum > π ✓                               │
  │  On saddle: triangle angles sum < π ✓                               │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Covariant Derivative and Christoffel Symbols

### 5.1 The Problem with Ordinary Derivatives

```
  On a curved surface, you can't just take d/dt of a vector field —
  the result may point off the surface (into ℝ³).

  You need to PROJECT back onto the tangent plane.

  For a vector field W along a curve γ on a surface:
  DW/dt = (dW/dt)^tangential = dW/dt - (dW/dt · n)n

  This "covariant derivative" stays tangential.
  On flat ℝⁿ: DW/dt = dW/dt (no projection needed).
```

### 5.2 Christoffel Symbols

```
  In local coordinates, the covariant derivative of a vector field V
  in direction ∂/∂xʲ:

  ∇_j Vⁱ = ∂Vⁱ/∂xʲ + Γⁱⱼₖ Vᵏ

  CHRISTOFFEL SYMBOLS Γⁱⱼₖ (connection coefficients):

  Γⁱⱼₖ = ½ gⁱˡ (∂gₗⱼ/∂xᵏ + ∂gₗₖ/∂xʲ - ∂gⱼₖ/∂xˡ)

  Γ is NOT a tensor — it transforms inhomogeneously under coordinate changes.
  This is intentional: ∇V = ∂V + ΓV where both terms are non-tensorial,
  but their sum IS tensorial. The Γ terms correct for coordinate curvature.

  ON FLAT ℝⁿ in Cartesian coordinates: Γⁱⱼₖ = 0 (no correction needed).
  ON FLAT ℝ² in polar coordinates: Γʳ_θθ = -r, Γθ_rθ = 1/r  (nonzero!)
  This is why "straight" lines look curved in polar coordinates.

  KEY PROPERTY: ∇g = 0 (metric is covariantly constant — Levi-Civita connection)
```

---

## 6. Parallel Transport

### 6.1 Definition

```
  A vector field V along a curve γ is PARALLEL TRANSPORTED if:

  DV/dt = ∇_{γ'} V = 0

  In components: dVⁱ/dt + Γⁱⱼₖ (dxʲ/dt) Vᵏ = 0

  Intuition: V is "as constant as possible" along γ,
  given that it must stay tangent to the manifold.

  On flat space: parallel transport = keep the vector constant direction.
  On curved space: you keep it as parallel as you can, but curvature causes it to rotate.
```

### 6.2 Holonomy — Curvature Detected by Transport

```
  PARALLEL TRANSPORT AROUND A CLOSED LOOP:

  If you parallel-transport a vector around a closed loop on a curved surface,
  the vector returns ROTATED (in general). The rotation angle = holonomy.

  ┌─────────────────────────────────────────────────────────────────────┐
  │  EXAMPLE: Sphere S² of radius R                                    │
  │                                                                     │
  │  Start at North Pole with vector pointing toward 0° longitude.     │
  │  Transport south along 0° longitude to equator.                    │
  │  Transport east along equator by angle φ.                          │
  │  Transport north back to North Pole along φ longitude.             │
  │                                                                     │
  │  Vector returns rotated by angle φ (the solid angle enclosed).     │
  │  Rotation angle = K × (enclosed area) = (1/R²)(φR²) = φ           │
  │                                                                     │
  │     N                                                               │
  │     │↑                                                              │
  │     │ ↖ (rotated by φ on return)                                   │
  │   φ─┤                                                               │
  │   equator                                                           │
  └─────────────────────────────────────────────────────────────────────┘

  The holonomy measures the curvature enclosed by the loop.
  This is directly related to Berry phase in QM (module 08-TOPOLOGY.md):
  parallel transport of a quantum state around a loop in parameter space.
```

---

## 7. Geodesics

### 7.1 The Geodesic Equation

```
  A GEODESIC is a curve whose tangent vector is parallel along itself:

  ∇_{γ'} γ' = 0

  In components (the geodesic equation):
  d²xᵏ/dt² + Γⁱⱼᵏ (dxⁱ/dt)(dxʲ/dt) = 0

  Geodesics are the "straightest possible paths" on a curved manifold.
  On flat space: geodesics are straight lines.
  On sphere: geodesics are great circles.
  In GR: free-falling particles follow geodesics of spacetime.

  GEODESICS LOCALLY MINIMIZE DISTANCE:
  A short enough piece of a geodesic is the shortest path between its endpoints.
  Globally: a geodesic minimizes distance locally but not necessarily globally.
  (Two points on a sphere have two great circle arcs — both are geodesics,
   only the shorter one minimizes distance.)
```

### 7.2 Examples

```
  SPHERE S²:
  Geodesics = great circles (intersection of sphere with plane through center)
  Shortest path from New York to London = great circle arc ✓

  FLAT TORUS (square with edges identified):
  Geodesics = straight lines in the square, wrap around
  Closed geodesics = lines with rational slope

  HYPERBOLIC PLANE (Poincaré disk model):
  Geodesics = circular arcs perpendicular to boundary disk
  Infinitely many geodesics through a point "parallel" to a given geodesic
  (non-Euclidean geometry, constant K=-1)

  SPACETIME (Schwarzschild geometry around a mass M):
  Timelike geodesics = worldlines of freely falling particles (orbits!)
  Null geodesics = paths of light rays
  The elliptical orbits of planets are geodesics in curved spacetime.
```

---

## 8. Riemann Curvature Tensor

### 8.1 Definition — Failure of Parallel Transport to Commute

```
  The RIEMANN CURVATURE TENSOR R measures how parallel transport fails to commute:

  R(X,Y)Z = ∇_X∇_YZ - ∇_Y∇_XZ - ∇_{[X,Y]}Z

  ┌──────────────────────────────────────────────────────────────────────┐
  │  Geometric interpretation:                                          │
  │                                                                     │
  │  Transport Z first in Y-direction, then in X-direction:   ∇_X∇_YZ │
  │  Transport Z first in X-direction, then in Y-direction:   ∇_Y∇_XZ │
  │  The difference = R(X,Y)Z                                           │
  │                                                                     │
  │  On flat space: partial derivatives commute → R=0.                 │
  │  On curved space: R≠0 measures the curvature.                      │
  └──────────────────────────────────────────────────────────────────────┘

  In components: Rⁱⱼₖˡ = ∂ₖΓⁱⱼˡ - ∂ˡΓⁱⱼₖ + Γⁱₘₖ Γᵐⱼˡ - Γⁱₘˡ Γᵐⱼₖ

  Symmetries:
  Rᵢⱼₖˡ = -Rⱼᵢₖˡ = -Rᵢⱼˡₖ = Rₖˡᵢⱼ
  Bianchi identity: Rᵢ[ⱼₖˡ] = 0   (cyclic sum = 0)
```

### 8.2 Ricci Tensor and Scalar

```
  RICCI TENSOR: Rᵢⱼ = Rᵏᵢₖⱼ  (trace over first and third indices)

  RICCI SCALAR: R = gⁱʲ Rᵢⱼ  (full trace)

  EINSTEIN TENSOR: Gᵢⱼ = Rᵢⱼ - ½ gᵢⱼ R

  KEY PROPERTY: ∇ʲ Gᵢⱼ = 0  (contracted Bianchi identity — divergence-free)
  This is ESSENTIAL for GR: it ensures energy-momentum conservation ∇ʲTᵢⱼ = 0.

  In 4D spacetime, the Riemann tensor has 20 independent components.
  The Ricci tensor has 10. The "leftover" 10 = Weyl tensor (tidal forces, gravity waves).
```

---

## 9. Einstein's Field Equations Decoded

### 9.1 The Equation

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                                                                      │
  │   Gμν = (8πG/c⁴) Tμν                                               │
  │                                                                      │
  │   Gμν = Rμν - ½ gμν R      (Einstein tensor = spacetime curvature)  │
  │   Tμν = stress-energy tensor  (energy, momentum, pressure, stress)  │
  │   G = Newton's gravitational constant                                │
  │   c = speed of light                                                 │
  │                                                                      │
  │   "Curvature of spacetime = energy content of spacetime"             │
  └──────────────────────────────────────────────────────────────────────┘

  COUNTING EQUATIONS:
  Gμν and Tμν are symmetric 4×4 tensors → 10 independent equations.
  But contracted Bianchi: ∇μGμν=0 gives 4 constraints.
  Net: 6 independent equations for the 6 independent metric components gμν
  (after using 4 coordinate degrees of freedom / gauge freedom).
```

### 9.2 Special Cases

```
  VACUUM (Tμν = 0):  Gμν = 0  →  Rμν = 0
  (Ricci flat ≠ flat: Weyl tensor can be nonzero → gravitational waves)

  SCHWARZSCHILD SOLUTION (vacuum, spherical symmetry):
  ds² = -(1-2GM/rc²)c²dt² + (1-2GM/rc²)⁻¹dr² + r²dΩ²

  Schwarzschild radius: rs = 2GM/c²  (event horizon of black hole)
  For Earth: rs ≈ 9mm
  For Sun:   rs ≈ 3km

  WEAK FIELD LIMIT (gμν = ημν + hμν, |hμν|<<1):
  Recovers Newtonian gravity + GEM equations (module physics/10-GRAVITY-EM)
  ∇²Φ = 4πGρ   (Poisson's equation)

  COSMOLOGICAL CONSTANT:  Gμν + Λgμν = (8πG/c⁴)Tμν
  Λ = dark energy density × 8πG/c⁴
  Causes accelerating expansion of the universe (discovered 1998)
```

---

## 10. Gauss-Bonnet Theorem

```
  For a compact oriented surface M WITHOUT boundary:

  ∫∫_M K dA = 2π χ(M)

  K = Gaussian curvature (local differential geometry)
  χ = Euler characteristic (global topology, from 08-TOPOLOGY.md)

  CONSEQUENCES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Sphere (χ=2):      ∫K dA = 4π                                     │
  │  Deform sphere → ∫K dA stays 4π no matter how you squish it!       │
  │                                                                     │
  │  Torus (χ=0):       ∫K dA = 0                                      │
  │  Positive curvature (outside) and negative (inside hole) cancel.   │
  │                                                                     │
  │  Genus-g surface (χ=2-2g): ∫K dA = 4π(1-g)                       │
  └──────────────────────────────────────────────────────────────────────┘

  WITH BOUNDARY ∂M:
  ∫∫_M K dA + ∫_∂M κg ds = 2π χ(M)
  κg = geodesic curvature of boundary curve

  TRIANGULATION VERSION (for geodesic triangle on surface):
  (α₁ + α₂ + α₃) - π = ∫∫_{triangle} K dA
  Angle sum of geodesic triangle = π + K × area
  (On sphere: angle sum > π; hyperbolic: angle sum < π)

  GENERALIZATIONS:
  Chern-Gauss-Bonnet (4D): ∫ Pf(R) = (2π)² χ(M)  (Pfaffian of curvature)
  Atiyah-Singer index theorem: analytical index = topological index
  (One of the deepest theorems in 20th century mathematics)
```

---

## Decision Cheat Sheet

| Want to know... | Use... |
|----------------|--------|
| How a curve bends | κ = &#124;T'&#124;, Frenet-Serret |
| How a curve twists out of a plane | τ (torsion) |
| Arc length on a surface | ds² = gᵢⱼ duⁱduʲ (first fundamental form) |
| Intrinsic curvature of surface | K = κ₁κ₂ (Gaussian curvature, intrinsic) |
| Whether surface can be flattened | K=0 everywhere ↔ locally isometric to plane |
| Shortest path on surface | Solve geodesic equation d²xᵏ/dt² + Γⁱⱼᵏ ẋⁱẋʲ = 0 |
| How much curvature enclosed by a loop | Holonomy angle = ∫∫ K dA over enclosed region |
| Curvature of spacetime | Riemann tensor Rⁱⱼₖˡ from metric gμν |
| GR in vacuum | Rμν = 0 (Ricci flat) |
| Total curvature of closed surface | 2πχ(M) (Gauss-Bonnet — topology wins) |

---

## Common Confusion Points

**"Intrinsic vs extrinsic curvature — what's the difference?"**
Intrinsic curvature (Gaussian K, Riemann tensor) is measurable from within the manifold — no ambient space needed. Extrinsic curvature (mean curvature H, second fundamental form) depends on how the manifold is embedded. K is intrinsic (Theorema Egregium). H is extrinsic. A cylinder has K=0 (intrinsically flat) but H≠0 (extrinsically curved). In GR, spacetime curvature is intrinsic — there's no ambient 5D space we're curved in.

**"What are Christoffel symbols, and are they tensors?"**
Christoffel symbols Γⁱⱼₖ are the "correction terms" needed to differentiate vectors on a curved manifold and stay tangential. They are NOT tensors — they transform inhomogeneously under coordinate changes (they pick up extra terms). This means you can always make Γ=0 at a single point by choosing normal coordinates (geodesic coordinates). But you can't make R=0 this way — the Riemann tensor IS a tensor and cannot be zeroed by coordinate choice if genuine curvature is present.

**"Why are geodesics not always the shortest paths?"**
Geodesics are locally length-minimizing — any short segment of a geodesic is the shortest path between its endpoints. But globally, a geodesic just extremizes length (could be a saddle point of the length functional). On a sphere, the two great circle arcs between two points are both geodesics; only the shorter one is the actual minimum. In spacetime, timelike geodesics maximize proper time (not minimize — the twin paradox).

**"How does Einstein's equation relate to Newtonian gravity?"**
In the weak-field slow-motion limit: gtt ≈ -(1+2Φ/c²) where Φ is the Newtonian potential. The 00-component of Einstein's equation Rtt = 4πG(ρ+3p/c²) reduces to ∇²Φ = 4πGρ (Poisson's equation) when pressure p is small. The curvature of the time-time component of the metric IS the Newtonian gravitational potential. Gravity in Newtonian mechanics is a force; in GR it's the curvature of the time axis.

**"The Riemann tensor has 20 components in 4D — how do you work with it?"**
You usually don't work with all 20 directly. In practice: for vacuum GR (Rμν=0), you work with the Weyl tensor (10 components). For cosmology, high symmetry reduces everything to 1-2 scalar functions. For perturbation theory (gravitational waves), you linearize in hμν. Numerical relativity uses the full tensor but decomposes it into constraint and evolution equations via the ADM formalism. The 20-component structure is the "fine print" — the physics lives in contractions and symmetry reductions.

---

*Next: `mathematics/11-PROBABILITY.md` — distributions, Master Theorem, CLT, Markov chains, and the Boltzmann distribution.*
