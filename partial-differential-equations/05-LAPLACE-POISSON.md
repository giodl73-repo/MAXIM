# Laplace and Poisson Equations

## The Big Picture

The Laplace equation ∇²u = 0 governs all **equilibrium** states. It is the archetype of
elliptic PDEs and appears in electrostatics, gravitation, steady heat, and irrotational flow.

```
+-----------------------------------------------------------------------+
|              LAPLACE / POISSON LANDSCAPE                               |
|                                                                       |
|  LAPLACE EQUATION:   ∇²u = 0   (harmonic functions)                  |
|  Electrostatics:  ∇²φ = 0  in vacuum                                  |
|  Gravitation:     ∇²φ = 0  outside masses                             |
|  Steady heat:     ∇²T = 0  in equilibrium                             |
|  Ideal fluid:     ∇²φ = 0  (velocity potential, irrotational)         |
|  Complex analysis: Re(f) and Im(f) for holomorphic f                  |
|                                                                       |
|  POISSON EQUATION:   ∇²u = f   (harmonic with source)                 |
|  Electrostatics:  ∇²φ = −ρ/ε₀  (charge density source)               |
|  Gravitation:     ∇²φ = 4πGρ   (mass density source)                 |
|  Steady heat:     ∇²T = −Q/k   (heat source Q)                       |
|                                                                       |
|  KEY TOOLS:                                                           |
|  • Fundamental solution (Green's function for free space)             |
|  • Green's theorems (integration by parts for ∇²)                    |
|  • Maximum principle (extrema on boundary)                            |
|  • Mean value property                                                |
|  • Separation of variables (spherical/cylindrical harmonics)          |
|  • Green's functions for specific domains                             |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Harmonic Functions: Core Properties

A function u satisfying ∇²u = 0 in an open set Ω is called **harmonic**.

### Mean Value Property

```
  MEAN VALUE THEOREM FOR HARMONIC FUNCTIONS:

  If ∇²u = 0 in a ball B_r(x₀) (and continuously up to boundary):

  u(x₀) = 1/(4πr²) ∫_{|x−x₀|=r} u(x) dσ(x)    [3D: surface average]
  u(x₀) = 1/(πr²)  ∫_{|x−x₀|≤r} u(x) dA(x)     [2D: area average]

  The value at the CENTER equals the average over any sphere (or disk)
  centered there — as long as u is harmonic in the region.

  PHYSICAL INTERPRETATION:
  In electrostatics: the potential at any point equals the average
  of the potential over any surrounding sphere in free space.
  This makes intuitive sense: no charge in the interior means
  no preferred direction; potential averages out perfectly.

  CONVERSE: The mean value property characterizes harmonic functions.
  If a continuous function satisfies the mean value property,
  it is harmonic. (Koebe's theorem)
```

### Maximum Principle

```
  STRONG MAXIMUM PRINCIPLE:

  If ∇²u = 0 in connected Ω, and u achieves its maximum (or minimum)
  at an INTERIOR point, then u is CONSTANT in Ω.

  Equivalently: a non-constant harmonic function has no interior extrema.
  All extrema are on the boundary ∂Ω.

  COROLLARIES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ UNIQUENESS:  If ∇²u = ∇²v = 0 in Ω and u = v on ∂Ω,          │
  │              then u = v everywhere in Ω.                        │
  │                                                                 │
  │ STABILITY:   max|u − v| in Ω ≤ max|u − v| on ∂Ω               │
  │              The solution depends continuously on boundary data. │
  │                                                                 │
  │ LIOUVILLE:   A bounded harmonic function on all of Rⁿ must be   │
  │              constant. (Complex analysis: bounded entire function│
  │              is constant.)                                      │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Fundamental Solution

The key building block for all Laplace/Poisson theory:

```
  PROBLEM:  Find Φ(x) such that  ∇²Φ = δ(x)  (point source at origin)

  SOLUTION (n = 3):  Φ(x) = −1/(4π|x|)

  SOLUTION (n = 2):  Φ(x) = 1/(2π) log|x|

  SOLUTION (n ≠ 2):  Φ(x) = −1/(n(n−2)ωₙ) · |x|^{2−n}
                     where ωₙ = volume of unit ball in Rⁿ

  VERIFICATION (n=3): ∇²Φ(x) = 0 for x ≠ 0.
  For x = 0: in distributional sense, ∇²(−1/4π|x|) = δ(x).

  PHYSICAL MEANING:
  Φ(x) = electric potential of a unit point charge at origin.
  (In electrostatics: φ = q/(4πε₀r), so Φ = −ε₀ × Coulomb potential)
```

---

## Green's Theorems: The Fundamental Identity

Green's theorems are integration by parts for ∇²:

```
  NOTATION: ∂u/∂n = ∇u · n̂ = normal derivative (n̂ = outward unit normal)

  GREEN'S FIRST IDENTITY:
  ∫_Ω (v∇²u) dV = ∮_{∂Ω} v ∂u/∂n dS − ∫_Ω ∇u · ∇v dV

  GREEN'S SECOND IDENTITY:
  ∫_Ω (v∇²u − u∇²v) dV = ∮_{∂Ω} (v ∂u/∂n − u ∂v/∂n) dS

  APPLICATIONS:
  (1) If ∇²u = ∇²v = 0 (both harmonic):
      ∮_{∂Ω} (v ∂u/∂n − u ∂v/∂n) dS = 0

  (2) Reciprocity: swap u and v → same result
      The Laplacian operator is self-adjoint.

  (3) Setting v = Φ (fundamental solution):
      Leads to GREEN'S REPRESENTATION FORMULA.
```

---

## Green's Representation Formula

The centerpiece of elliptic theory:

```
  GREEN'S REPRESENTATION FORMULA:

  For any harmonic function u in Ω (with smooth boundary):

  u(x₀) = ∮_{∂Ω} [u(y) ∂Φ(y−x₀)/∂n_y − Φ(y−x₀) ∂u/∂n(y)] dS_y

  This expresses the value at ANY interior point x₀ in terms of the
  boundary values of u and its normal derivative.

  FOR POISSON EQUATION ∇²u = f:
  u(x₀) = ∫_Ω Φ(y−x₀) f(y) dV_y
           + boundary terms

  The first term: volume potential (effect of sources).
  The boundary terms: single layer and double layer potentials.
```

---

## Green's Functions for Bounded Domains

```
  GREEN'S FUNCTION G(x,y) for domain Ω with Dirichlet BC:
  ┌───────────────────────────────────────────────────────────────┐
  │  ∇²_x G(x,y) = δ(x−y)    in Ω  (for fixed y)               │
  │  G(x,y) = 0               on ∂Ω                              │
  └───────────────────────────────────────────────────────────────┘

  Decomposition: G(x,y) = Φ(x−y) + H(x,y)
  where H is harmonic in Ω (corrects Φ to vanish on ∂Ω).

  SOLUTION TO POISSON:
  u(x) = ∫_Ω G(x,y) f(y) dV_y   (with u=0 on ∂Ω)

  SOLUTION TO LAPLACE (Dirichlet BVP):
  u(x) = −∮_{∂Ω} ∂G/∂n_y (x,y) g(y) dS_y
  where g = boundary data and ∂G/∂n = Poisson kernel.

  SYMMETRY: G(x,y) = G(y,x)  (Green's function is symmetric)
  This follows from the self-adjointness of ∇².
```

### Method of Images: Green's Function for the Half-Space

```
  DOMAIN: Ω = {x ∈ R³ : x₃ > 0} (upper half-space)

  For source at y = (y₁,y₂,y₃) with y₃ > 0:

  G(x,y) = Φ(x−y) − Φ(x−y*)

  where y* = (y₁,y₂,−y₃) is the REFLECTION of y across x₃=0.

  PHYSICAL PICTURE:
  +----------------------------------------------------+
  |         REAL CHARGE at y (upper half-space)        |
  | ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · |
  ======================= x₃ = 0 (grounded plane) ===
  |         IMAGE CHARGE at y* (lower half-space)      |
  +----------------------------------------------------+

  The image charge −1 at y* ensures G=0 on the boundary.
  Method of images works for: half-space, quarter-space, wedge,
  rectangle, sphere.

  POISSON KERNEL FOR HALF-SPACE (x₃>0, source on x₃=0):
  P(x,y') = x₃ / [2π((x₁−y₁)²+(x₂−y₂)²+x₃²)^{3/2}]

  Dirichlet solution: u(x) = ∫_{R²} P(x,y') g(y') dA(y')
```

### Green's Function for the Ball

```
  DOMAIN: B = {|x| < R}  (ball of radius R in R³)

  For source at y ∈ B:  y* = (R/|y|)² y  (Kelvin inversion)

  G(x,y) = Φ(x−y) − (R/|y|)·Φ(x−y*)

  POISSON KERNEL FOR BALL (Poisson integral formula):
  P(x,y) = (R²−|x|²) / (nωₙ R |x−y|ⁿ)  for x ∈ B, y ∈ ∂B

  SOLUTION: u(x) = ∮_{|y|=R} P(x,y) g(y) dS(y)

  CHECK: As x→y₀ ∈ ∂B, P(x,y) → δ(y−y₀)  (approximate identity).
  → u(x) → g(y₀) (boundary data recovered).
```

---

## Separation of Variables: Rectangular Domain

```
  ∇²u = 0  on [0,a]×[0,b],   BCs: u=0 on three sides, u=g(x) on y=b

  STEP 1: u(x,y) = X(x)Y(y)
          X''/X = −Y''/Y = λ

  STEP 2: X problem: X'' + λX = 0, X(0) = X(a) = 0
          λ_n = (nπ/a)², X_n = sin(nπx/a)

  STEP 3: Y problem: Y'' − λ_n Y = 0, Y(0) = 0
          Y_n(y) = sinh(nπy/a)

  STEP 4: u = Σ_n c_n sin(nπx/a) sinh(nπy/a)
          Apply u(x,b) = g(x):
          c_n = 2/(a sinh(nπb/a)) ∫₀ᵃ g(x) sin(nπx/a) dx
```

---

## Spherical Harmonics: Separation in Spherical Coordinates

The natural basis for ∇²u = 0 on spherical domains:

```
  LAPLACIAN IN SPHERICAL COORDS (r,θ,φ):
  ∇²u = u_rr + 2/r·u_r + 1/r²·[u_θθ + cot(θ)u_θ + csc²(θ)u_φφ]
       = u_rr + 2/r·u_r + 1/r²·L_sphere u

  SEPARATION: u = R(r)·Y(θ,φ)
  R'' + 2/r R' − ℓ(ℓ+1)/r² R = 0  →  R = Ar^ℓ + Br^{−(ℓ+1)}
  L_sphere Y = −ℓ(ℓ+1) Y         →  Y = Y_ℓᵐ(θ,φ) (spherical harmonics)

  SPHERICAL HARMONICS:
  Y_ℓᵐ(θ,φ) = c_ℓᵐ · P_ℓᵐ(cos θ) · e^{imφ}

  ℓ = 0,1,2,...  (degree),   m = −ℓ,...,ℓ  (order)

  ORTHOGONALITY: ∫ Y_ℓᵐ · Y̅_{ℓ'm'} dΩ = δ_{ℓℓ'} δ_{mm'}

  PHYSICAL MEANING:
  ℓ = 0: monopole (charge, mass)
  ℓ = 1: dipole
  ℓ = 2: quadrupole
  ℓ = n: 2ⁿ-pole

  Used in: atomic orbitals, gravitational multipole expansion,
           seismology, geomagnetic field decomposition,
           computer graphics (irradiance environment maps).

  GENERAL SOLUTION IN BALL (interior):
  u(r,θ,φ) = Σ_{ℓ=0}^∞ Σ_{m=−ℓ}^{ℓ} A_ℓᵐ · r^ℓ · Y_ℓᵐ(θ,φ)
```

---

## Regularity Theory

```
  INTERIOR REGULARITY:

  THEOREM (Elliptic regularity): If ∇²u = f in Ω and f ∈ C^k(Ω),
  then u ∈ C^{k+2}(Ω).

  If f ∈ C∞(Ω), then u ∈ C∞(Ω).
  If f = 0 (harmonic), u ∈ C∞ (in fact real analytic).

  SOBOLEV FRAMEWORK (shift-by-2):
  If f ∈ H^k(Ω) then u ∈ H^{k+2}(Ω).
  Solving Poisson gains exactly two derivatives.

  Lp REGULARITY (Calderón-Zygmund):
  If f ∈ Lp(Ω), 1 < p < ∞, then D²u ∈ Lp(Ω).
  Estimate: ‖D²u‖_{Lp} ≤ C_p ‖f‖_{Lp}
  ──────────────────────────────────────────────────────────────────
  Fails at the endpoints:
    p = 1:  D²u ∉ L¹ in general (Ornstein non-inequality)
    p = ∞:  D²u ∉ L∞ in general; must use BMO (bounded mean oscillation)
  The C-Z constant C_p → ∞ as p → 1 or p → ∞.

  BOUNDARY REGULARITY:
  Interior regularity is free. Boundary regularity costs domain smoothness.
  ──────────────────────────────────────────────────────────────────
  ∂Ω ∈ C^{k+2}  and  g ∈ H^{k+3/2}(∂Ω)  →  u ∈ H^{k+2}(Ω) up to ∂Ω
  ∂Ω ∈ C^{k,α}  (Hölder smooth)            →  Schauder estimates apply

  What breaks for rough domains:
  • Lipschitz ∂Ω: H² regularity holds, but higher regularity fails
  • Polyhedral domains (3D): corner/edge singularities u ~ r^λ
    (λ depends on corner angle; re-entrant corners → λ < 1 → u ∉ H²)
  • Crack tips: u ~ r^{1/2} sin(θ/2) — the classic stress singularity
  These singularities limit FEM convergence on non-smooth domains
  and explain why adaptive mesh refinement near corners is essential.

  WHY THIS MATTERS FOR NUMERICS:
  FEM error: ‖u − u_h‖_{H¹} ≤ C h^k ‖u‖_{H^{k+1}}
  If u ∉ H^{k+1} (corner singularity), the rate degrades.
  PINNs face the same issue: spectral bias + singularities = poor
  approximation of r^λ modes near corners.

  SCHAUDER ESTIMATES (Hölder spaces):
  ‖u‖_{C^{2,α}} ≤ C(‖f‖_{C^α} + ‖g‖_{C^{2,α}})
  These are the classical regularity estimates; they preceded Sobolev
  theory historically but are less natural for FEM analysis.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|--------------|-----|
| Solve ∇²u = 0 in rectangle | Separation of variables (Fourier sine series) |
| Solve ∇²u = 0 in ball/sphere | Spherical harmonics expansion |
| Solve ∇²u = 0 in half-space | Method of images + Poisson integral formula |
| Solve ∇²u = f in general domain | Green's function G(x,y) — volume potential |
| Solve ∇²u = 0 with given boundary values | Poisson kernel P(x,y) — boundary integral |
| Prove uniqueness for Laplace | Maximum principle or energy method |
| Extend u harmonically from boundary | Poisson integral formula |
| Expand in multipoles | Spherical harmonics Y_ℓᵐ with Ar^ℓ + Br^{−ℓ−1} radial factors |

---

## Common Confusion Points

**"Is the fundamental solution Φ = −1/4π|x| actually a solution to ∇²Φ = 0?"**
It satisfies ∇²Φ = 0 for x ≠ 0, but not at x = 0. At the origin, ∇²Φ = δ(x) in the
distributional sense. This is the entire point: Φ is NOT a classical solution — it is a
distributional (weak) solution, and its Laplacian is a delta function. This is what makes it
the Green's function (response to a point source).

**"Why does the 2D fundamental solution (log|x|) behave differently from 3D (1/|x|)?"**
The 2D log grows without bound at infinity, while 3D 1/|x| decays. This causes the 2D
Neumann problem on an unbounded domain to have a compatibility condition (total flux must
equal total source). 2D electrostatics is a logarithmic potential theory.

**"What's the Poisson kernel geometrically?"**
The Poisson kernel P(x,y) for the ball is the "harmonic measure" — the weight given to
boundary point y when computing the harmonic function at interior point x. It concentrates
near the boundary point y that is closest to x as x→∂B. Geometrically, it is the normal
derivative of the Green's function: P = −∂G/∂n_y.
