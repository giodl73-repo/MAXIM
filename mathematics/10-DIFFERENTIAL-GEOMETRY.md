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
  │  Straight line:  κ=0, τ=0    (no bending, no twisting)               │
  │  Circle of radius r: κ=1/r, τ=0   (constant bending, flat)           │
  │  Helix (r, pitch p): κ=r/(r²+p²), τ=p/(r²+p²)  (constant κ and τ) │
  │  Plane curve: τ=0 always (stays in its plane)                        │
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
  │  You cannot flatten a sphere without distortion.                     │
  │  (K=1/R²≠0 on sphere, K=0 on plane → not isometric)               │
  │  This is why maps of Earth always distort either area or angle.      │
  │                                                                      │
  │  You CAN flatten a cylinder (K=0 on both cylinder and plane).      │
  │  Unrolling a cylinder = isometric map.                               │
  │                                                                      │
  │  An ant can measure K by doing geometry:                             │
  │  Sum of angles of a geodesic triangle = π + K × (area)             │
  │  On sphere: triangle angles sum > π ✓                                │
  │  On saddle: triangle angles sum < π ✓                                │
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
  │  EXAMPLE: Sphere S² of radius R                                     │
  │                                                                     │
  │  Start at North Pole with vector pointing toward 0° longitude.      │
  │  Transport south along 0° longitude to equator.                     │
  │  Transport east along equator by angle φ.                           │
  │  Transport north back to North Pole along φ longitude.              │
  │                                                                     │
  │  Vector returns rotated by angle φ (the solid angle enclosed).      │
  │  Rotation angle = K × (enclosed area) = (1/R²)(φR²) = φ           │
  │                                                                     │
  │     N                                                               │
  │     │↑                                                              │
  │     │ ↖ (rotated by φ on return)                                    │
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
  │  Geometric interpretation:                                           │
  │                                                                      │
  │  Transport Z first in Y-direction, then in X-direction:   ∇_X∇_YZ │
  │  Transport Z first in X-direction, then in Y-direction:   ∇_Y∇_XZ │
  │  The difference = R(X,Y)Z                                            │
  │                                                                      │
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
  │   Gμν = Rμν - ½ gμν R      (Einstein tensor = spacetime curvature)   │
  │   Tμν = stress-energy tensor  (energy, momentum, pressure, stress)   │
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
  │                                                                      │
  │  Torus (χ=0):       ∫K dA = 0                                      │
  │  Positive curvature (outside) and negative (inside hole) cancel.   │
  │                                                                      │
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

## 11. Differential Geometry in Modern ML

```
  GEODESICS AND OPTIMAL TRANSPORT:
  The Wasserstein distance W_p(μ,ν) between probability distributions
  is a geodesic distance on the space of distributions.
  The space of probability measures on a manifold carries a Riemannian
  structure (Otto calculus) where geodesics = optimal transport plans.
  W₂ is the Riemannian distance on (Prob(M), g_Fisher).

  Practical consequence: diffusion model training = minimizing Wasserstein
  distance between learned and data distributions via score matching.

  NATURAL GRADIENT DESCENT (Amari 1998):
  For a statistical model parameterized by θ ∈ Θ:
  Fisher information matrix I(θ)_{ij} = E[∂_i log p_θ · ∂_j log p_θ]
  defines a Riemannian metric on the STATISTICAL MANIFOLD.

  Natural gradient:  θ_{t+1} = θ_t - α I(θ)⁻¹ ∇L(θ)
  ├── Steepest descent in the intrinsic geometry of the parameter space
  ├── Invariant under reparameterization of the model
  ├── Geodesics of the Fisher metric = minimum-KL paths between distributions
  └── K-FAC (Kronecker-Factored Approximate Curvature): practical approximation
      to I(θ)⁻¹ for neural networks using Kronecker products.

  RIEMANNIAN GRADIENT DESCENT ON MATRIX MANIFOLDS:
  (Introduced in 09-MANIFOLDS.md §10; connection to curvature here)

  Why curvature matters for optimization:
  ├── Sectional curvature κ of Stiefel St(n,k): bounded, κ ∈ [-1, ¼]
  ├── SPD manifold Sym⁺(n): non-positive sectional curvature (Hadamard space)
  │   → unique geodesics, convex optimization has unique global minimum
  └── Grassmannian Gr(n,k): positive curvature → geodesics can converge
      faster than in flat space, BUT conjugate points exist (geodesics stop
      being length-minimizing after certain distance)

  Geodesic equation on Stiefel St(n,k):
  d²X/dt² + X(ẊᵀẊ) = 0  (zero covariant acceleration in the induced metric)
  Solved by matrix exponential: X(t) = X(0)·exp(t·A) for skew-symmetric A.

  GEOMETRIC DEEP LEARNING (Bronstein-Bruna-LeCun-Szlam-Vandergheynst):
  Blueprint: G-equivariant neural networks respect symmetry G acting on M.

  Layers of the hierarchy:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Group G on domain M  →  Function space on M  →  Equivariant maps   │
  │                                                                     │
  │  G=translation on ℝ²:  CNN (convolutional layers)                   │
  │  G=SO(2) on sphere:    Spherical CNNs                               │
  │  G=SE(3) on ℝ³:        E(3)-equivariant (molecular property pred.)  │
  │  G=Diff(M) on mesh:    Gauge-equivariant mesh CNNs                  │
  │  G=permutations Sₙ:    Graph Neural Networks (on graphs)            │
  └─────────────────────────────────────────────────────────────────────┘

  The key operation: equivariant convolution uses the group structure to
  define "filters" that respect geometry:
  (f ★ ψ)(g) = ∫_G f(h) ψ(g⁻¹h) dh  (convolution on the group)

  CURVATURE OF LOSS LANDSCAPES:
  The Hessian H = ∇²L(θ) at a point θ acts as a Riemannian metric on
  parameter space (locally). Key differential-geometric facts:
  ├── Trace(H) = sum of eigenvalues = total curvature in all directions
  ├── det(H) > 0, all eigenvalues > 0: local minimum (positive definite Hessian)
  ├── Negative eigenvalues: saddle point (directions of descent)
  └── Zero eigenvalues: flat directions (degenerate — related to symmetries,
      overparameterization, or BN-induced scale invariances)

  SECTIONAL CURVATURE of the loss surface along the 2D slice {θ₀ + su + tv}:
  κ(u,v) involves 4th-order derivatives of L. Practically approximated by
  Hessian-vector products (Pearlmutter's trick, O(n) not O(n²)).

  DIFFUSION MODELS AS RIEMANNIAN FLOWS:
  Score function: s(x,t) = ∇_x log p_t(x) = a vector field on data manifold.
  Denoising SDE: dx = -½ β(t) x dt + √β(t) dW
  Score-based reverse: dx = [-½ β(t) x - β(t) s(x,t)] dt + √β(t) dW̄
  The score is the gradient of log-density = gradient vector field on Riemannian
  data manifold. Score matching loss = enforcing this vector field is correct.
```

## 12. Gauge Theory and Chern-Weil Theory

```
  THE PARALLEL BETWEEN GRAVITY AND GAUGE THEORY:

  GRAVITY (GR)                    YANG-MILLS GAUGE THEORY
  ─────────────────────────────────────────────────────────────────────
  Spacetime manifold M             Principal G-bundle P → M
  Metric gμν                       Bundle metric (via representation)
  Levi-Civita connection Γⁱⱼₖ      Connection 1-form A (gauge potential)
  Curvature Rⁱⱼₖˡ                  Field strength F = dA + A∧A
  Bianchi identity ∇[μRνρ]σλ=0     Bianchi: DF = dF + [A,F] = 0
  Einstein equations Gμν = 8πG Tμν Yang-Mills equations: D★F = J
  Gauge freedom: coordinate change  Gauge freedom: A → g⁻¹Ag + g⁻¹dg

  Both are "curvature = source" equations.
  GR: curvature of tangent bundle (rank-2 tensor bundle) = matter stress.
  YM: curvature of internal symmetry bundle = matter current.

  EXPLICIT YANG-MILLS:
  Connection 1-form: A = Aμ^a T^a dxμ  (g-valued 1-form, T^a = Lie algebra basis)
  Field strength: Fμν = ∂μAν - ∂νAμ + [Aμ, Aν]
  (The [Aμ,Aν] term is new vs EM and encodes the non-abelian self-interaction.)

  For G = U(1) (electromagnetism): [Aμ,Aν] = 0 → Fμν = ∂μAν - ∂νAμ ✓
  For G = SU(2) (weak force): [Aμ,Aν] ≠ 0 → W bosons interact with each other.
  For G = SU(3) (strong force): gluon self-coupling → confinement.

  CHERN-WEIL THEOREM:
  Characteristic classes are cohomology classes computed from curvature
  using invariant polynomials of the Lie algebra.

  CHERN CLASSES (complex vector bundles):
  c₁ = [tr(iF/2π)] ∈ H²(M;ℤ)          first Chern class
  c₂ = [tr(iF/2π)² - (tr(iF/2π))²/2] ∈ H⁴(M;ℤ)  (second Chern class)
  ∫_M c₁ = n ∈ ℤ   (integer! — the "instanton number" or monopole charge)

  PONTRYAGIN CLASSES (real vector bundles):
  p₁ = [-tr(F∧F)/8π²] ∈ H⁴(M;ℤ)

  INSTANTONS (self-dual Yang-Mills solutions):
  F = ★F  (self-dual: field strength = its own Hodge dual)
  Solutions in Euclidean 4-space with ∫ tr(F∧F) = 8π²n (topological charge n).
  Yang-Mills action ≥ 8π²|n| (from Cauchy-Schwarz: tr(F∧F) ≤ ‖F‖²dV).
  Equality iff F = ±★F.
  Instantons are absolute minima of the Yang-Mills action in each topological sector.

  CHERN-SIMONS THEORY:
  The 3D action S = ∫_M tr(A∧dA + 2/3 A∧A∧A) depends only on topology.
  Quantization of CS theory produces invariants of 3-manifolds and knots
  (Jones polynomial, Witten-Reshetikhin-Turaev invariants).
  Relevant to: topological quantum computing (anyons), 3-manifold topology.

  ATIYAH-SINGER INDEX THEOREM (briefest statement):
  For a Dirac operator D on a compact Riemannian manifold:
  dim ker D - dim coker D = ∫_M Â(M) ∧ ch(E)
  LHS = analytical index (solution space)
  RHS = topological index (Chern-Weil integrals of curvature)
  Unifies Gauss-Bonnet, Hirzebruch-Riemann-Roch, and Chern-Gauss-Bonnet.
  The Â genus and Chern character ch(E) are computed from Pontryagin/Chern classes.
```

## 13. Spin Geometry and the Dirac Operator

```
  CLIFFORD ALGEBRA Cl(n):
  Generated by {e₁,...,eₙ} with the relation: eᵢeⱼ + eⱼeᵢ = -2δᵢⱼ
  (Anticommuting generators — the square of each basis element = -1.)
  dim Cl(n) = 2ⁿ as a vector space.

  For n=1: Cl(1) = {a + be₁ | a,b ∈ ℝ},  e₁² = -1 → Cl(1) ≅ ℂ
  For n=2: Cl(2) = {a + be₁ + ce₂ + de₁e₂},  (e₁e₂)² = -1 → Cl(2) ≅ ℍ (quaternions!)
  For n=3: Cl(3) ≅ M₂(ℂ) ⊕ M₂(ℂ)   (relates to Pauli matrices)

  PAULI MATRICES generate Cl(3):
  σ₁=[0 1;1 0], σ₂=[0 -i;i 0], σ₃=[1 0;0 -1]
  σᵢσⱼ + σⱼσᵢ = 2δᵢⱼ   (Clifford relation with positive signature)

  SPIN GROUPS:
  Spin(n) = double cover of SO(n), realized inside Cl(n).
  Spin(2) ≅ U(1) → SO(2) (2-to-1)
  Spin(3) ≅ SU(2) → SO(3) (2-to-1 — the spinor cover from 08-TOPOLOGY.md)
  Spin(4) ≅ SU(2) × SU(2) → SO(4)
  Spin(6) ≅ SU(4) → SO(6)

  Physical spinors (spin-½ particles) are vectors in a representation of Spin(3)=SU(2)
  that does NOT factor through SO(3). They pick up a factor -1 under 360° rotation:
  need 720° to return to identity. This is not a physical oddity — it's the
  topology of SO(3): π₁(SO(3)) = ℤ/2ℤ, and spinors "see" the ℤ/2ℤ.

  SPINOR BUNDLE:
  For an oriented Riemannian n-manifold M (with spin structure):
  the spinor bundle S → M is an associated bundle to the spin frame bundle.
  Fibers = spinor representations of Spin(n).
  For n=4 (spacetime): Dirac spinors ∈ ℂ⁴ at each point.
  The spinor bundle has a connection (spin connection) derived from the
  Levi-Civita connection + the Clifford algebra structure.

  DIRAC OPERATOR:
  D = Σμ γμ ∇μ   where γμ = Clifford generators, ∇μ = spin connection

  ├── D is a first-order elliptic differential operator: sections of S → sections of S
  ├── D is self-adjoint (on a compact manifold without boundary)
  ├── D² = ∇*∇ + R/4   (Lichnerowicz formula: Laplacian + scalar curvature)
  └── This is the Weitzenböck formula: D² relates analysis (Laplacian) to geometry (R)

  LICHNEROWICZ THEOREM:
  If R > 0 everywhere, then D has no zero eigenvalues (no harmonic spinors).
  Proof: D²ψ = 0 ⟹ ∫(∇*∇ + R/4)ψ·ψ̄ = 0 ⟹ ∫|∇ψ|² + R/4|ψ|² = 0.
  With R > 0: both terms non-negative and must both be zero → ψ = 0.
  CONSEQUENCE: positively curved spin manifolds have trivial index → topological constraint.
  This is an analytic proof of a TOPOLOGICAL fact about curvature-topology interaction.

  ATIYAH-SINGER (revisited with spinors):
  ind(D) = dim ker D - dim coker D   (analytical index = "excess of zero modes")
  = ∫_M Â(M)   (Â = "A-roof genus" = topological invariant from Pontryagin classes)

  For surfaces (n=2): ind = χ/2 = (1 - genus) ← Gauss-Bonnet!
  For 4-manifolds: ind = (p₁ - sign)/8  (relates to 4-manifold topology)

  PHYSICAL IMPLICATIONS:
  ├── Zero modes of the Dirac operator count topological invariants
  ├── In QCD: zero modes of the Dirac operator on gauge backgrounds ↔ instantons
  │   (Atiyah-Singer: index = instanton number = ∫ tr(F∧F)/8π²)
  ├── Anomalies in QFT: when the path integral measure fails to be invariant
  │   under gauge transformations → traced back to the index of the Dirac operator
  └── Topological insulators: zero modes of the Dirac operator at interfaces
      (Jackiw-Rebbi solitons) = protected edge states (10-TOPOLOGY.md §7.1)
```

## 14. Computational Differential Geometry

```
  NUMERICAL GEODESICS:
  The geodesic equation (§7.1) is a system of 2n ODEs in (xᵏ, ẋᵏ):

  d²xᵏ/dt² = -Γⁱⱼᵏ ẋⁱ ẋʲ

  Solve with RK4 / Dormand-Prince (scipy.integrate.solve_ivp).
  Given initial position x₀ and velocity v₀, integrate forward.
  Geodesic boundary value problem (start + end fixed): shooting method.

  GEODESIC SHOOTING (Riemannian exponential map):
  Exp_p(v) = γ(1)  where γ solves geodesic IVP with γ(0)=p, γ'(0)=v.
  Implemented by integrating the geodesic ODE.

  Log_p(q) = v  (inverse: find initial velocity to reach q from p)
  Requires solving a BVP (boundary value problem) — harder, needs iteration.

  FOR MATRIX MANIFOLDS (closed-form geodesics available):
  SO(n):  Exp_R(V) = R · exp(RᵀV)      (matrix exponential of skew-symmetric)
  SPD:    Exp_A(V) = A^{1/2} exp(A^{-1/2}VA^{-1/2}) A^{1/2}
  Stiefel: use matrix exponential of augmented skew-symmetric matrix

  DISCRETE CURVATURE ON MESHES:
  For a triangle mesh (V,F), discretize the curvature tensors:
  Gaussian curvature at vertex v: K(v) = 2π - Σ θᵢ  (angle defect)
  (Σθᵢ = sum of angles at v in incident triangles)
  Gauss-Bonnet check: Σᵥ K(v) = 2π χ(M) ✓  (exact, not approximate!)

  Mean curvature at vertex v: H(v) = ½ |Lv|  (magnitude of Laplacian of position)
  where L = cotangent Laplacian (from 09-MANIFOLDS.md §12).

  Principal curvatures: from the shape operator S = gⁱᵏ Lₖⱼ on the mesh,
  approximated via principal curvature directions fitting or discrete shape operator.

  HEAT METHOD FOR GEODESIC DISTANCE (Crane-Weischedel-Wardetzky 2013):
  1. Solve heat equation: (I - t·L) u = δ_v  (one backward Euler step from source v)
  2. Normalize gradient: X = -∇u/|∇u|  (unit gradient field pointing away from source)
  3. Solve Poisson: L φ = ∇·X   (integrate to get distance function φ)
  Result: approximate geodesic distances from v to all vertices.
  Cost: two sparse linear system solves (O(n) after factorization precomputed).
  Far faster than Dijkstra on fine meshes.

  import igl
  V, F = igl.read_triangle_mesh("mesh.obj")
  L = igl.cotmatrix(V, F)           # cotangent Laplacian
  M_area = igl.massmatrix(V, F)     # vertex area matrix

  # Gaussian curvature (angle defect)
  K = igl.gaussian_curvature(V, F)  # K[i] = curvature at vertex i

  # Geodesic distances from vertex 0
  t = 0.01  # diffusion time (bandwidth parameter)
  D = igl.heat_geodesics_precompute(V, F, t)
  dist = igl.heat_geodesics_solve(D, np.array([0], dtype=np.int32))

  FINITE ELEMENTS ON CURVED DOMAINS:
  Laplace-Beltrami stiffness matrix = cotangent Laplacian L (see §09-MANIFOLDS §12).
  Mass matrix M = diagonal (vertex areas) or lumped.
  PDE ∂u/∂t = ∆_M u → implicit Euler: (M - Δt L) u_{n+1} = M u_n
  Eigenvalue problem: L φ = λ M φ  (generalized eigenvalue → spectral geometry)

  LIBRARIES:
  libigl (C++/Python): geometry processing, discrete DG, FEM
  PyGEL3D: half-edge meshes, Laplacians
  Open3D: 3D data processing, mesh I/O
  Geomstats (Python): Riemannian geometry + statistical learning on manifolds
```

### 8.3 Weyl Tensor and Conformal Geometry

```
  RIEMANN DECOMPOSITION:
  In n ≥ 4 dimensions, the Riemann tensor decomposes uniquely as:

  Rᵢⱼₖˡ = Wᵢⱼₖˡ + (n-2)⁻¹ (gᵢ[ₖRˡ]ⱼ - gⱼ[ₖRˡ]ᵢ) - (n-1)(n-2)⁻¹ R gᵢ[ₖgˡ]ⱼ

  WEYL TENSOR Wᵢⱼₖˡ:
  ├── Trace-free: gⁱᵏ Wᵢⱼₖˡ = 0 (vanishes on any contraction)
  ├── Same symmetries as Riemann: antisymmetric in [ij] and [kl], symmetric under swap
  ├── In 4D: 10 independent components (= Riemann 20 − Ricci 10)
  └── Carries all curvature information NOT captured by Ricci

  PHYSICAL MEANING:
  Ricci tensor Rμν: source-dependent curvature (set by Einstein equations)
  Weyl tensor Wμνρσ: vacuum ("free") curvature — exists even when Tμν = 0
  Ricci = 0 (vacuum) ≠ Riemann = 0: gravitational waves and tidal forces live in Weyl.

  ┌────────────────────────────────────────────────────────────────────┐
  │  TIDAL FORCES (geodesic deviation equation):                       │
  │  D²ξμ/dτ² = -Rμνρσ Uν ξρ Uσ                                    │
  │  ξμ = separation vector between nearby geodesics                   │
  │  Uμ = 4-velocity along geodesic                                    │
  │  In vacuum: this is ENTIRELY due to the Weyl tensor.               │
  │  Tidal disruption of infalling objects near black holes = Weyl.    │
  └────────────────────────────────────────────────────────────────────┘

  GRAVITATIONAL WAVES: perturbation of flat spacetime gμν = ημν + hμν
  In TT gauge (transverse-traceless): hμν encodes the Weyl tensor perturbation.
  The two polarizations h₊ and h× are the two independent Weyl degrees of freedom.

  CONFORMALLY FLAT: W = 0 everywhere.
  A manifold is conformally flat iff it's locally related to flat space by a
  conformal (angle-preserving, not length-preserving) rescaling: g̃ = Ω²g.
  Examples: Sⁿ, any 2D manifold (ALL surfaces are conformally flat!),
            Robertson-Walker cosmological spacetimes.

  CONFORMAL GEOMETRY:
  CONFORMAL MAP f: M → N preserves angles but not distances.
  In ℝ² ≅ ℂ: conformal maps = holomorphic functions with f'(z) ≠ 0!
  This is the bridge between complex analysis and differential geometry.

  WEYL TRANSFORMATION (physics): g → Ω²(x) g (local rescaling)
  WEYL INVARIANT: theories where action is unchanged under Weyl transformations.
  Weyl anomaly: classical Weyl invariance broken by quantum corrections
  (the trace of the stress-energy tensor Tμμ ≠ 0 after quantization).
  Central charge in CFT = coefficient of Weyl anomaly.
  This anomaly-cancellation condition constrains string theory to 26 (bosonic)
  or 10 (superstring) spacetime dimensions.

  CONFORMAL BOUNDARY (AdS/CFT):
  Anti-de Sitter space AdSₙ₊₁ has a conformal boundary = Sⁿ ≅ ℝⁿ ∪ {∞}.
  The Weyl tensor vanishes on AdS (maximally symmetric space).
  Holography: bulk fields in AdS_{n+1} ↔ operators in CFT_n on the boundary.
  The conformal group SO(n,2) acts as isometries of AdS and as conformal
  symmetries of the boundary CFT — same group, two realizations.
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
