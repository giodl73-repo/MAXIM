# Conformal Mappings and Applications

## The Big Picture

Conformal maps are the geometric face of holomorphic functions. They preserve angles and local shape (but not generally area or length). Their power comes from the Riemann Mapping Theorem: any simply connected domain (other than all of ℂ) is conformally equivalent to the unit disk. This means: solving a PDE on a complicated domain reduces to finding the right conformal map, solving on the disk, then transforming back.

```
CONFORMAL MAPS — LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  CONFORMAL MAP: f holomorphic, f'(z) ≠ 0
  Preserves: angles (including orientation)
  Maps: circles and lines → circles and lines (for Möbius)
         regions → regions (biholomorphically for bijective maps)

  KEY CLASSES
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Möbius (linear fractional)   f = (az+b)/(cz+d),  ad−bc ≠ 0      │
  │  Power maps                   f = zⁿ, f = z^{1/n}                 │
  │  Exponential/logarithm        f = e^z, f = log z                  │
  │  Joukowski                    f = z + 1/z   (circles → airfoils)  │
  │  Schwarz-Christoffel          maps to polygons                     │
  └─────────────────────────────────────────────────────────────────────┘

  RIEMANN MAPPING THEOREM
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Ω ⊂ ℂ simply connected and Ω ≠ ℂ                                 │
  │  ⟹  ∃ unique biholomorphic f: Ω → D (unit disk)                  │
  │      with f(z₀) = 0 and f'(z₀) > 0 for any fixed z₀ ∈ Ω         │
  └─────────────────────────────────────────────────────────────────────┘

  APPLICATIONS
  ┌──────────────┬────────────────────────────────────────────────────┐
  │ Laplace PDE  │ Map complex domain to disk; solve; map back        │
  │ Fluid flow   │ Map airfoil to disk; solve potential flow          │
  │ Airfoil      │ Joukowski transform: circle → wing profile        │
  │ Electrostatics│ Potential on Ω = real part of holomorphic f on Ω │
  └──────────────┴────────────────────────────────────────────────────┘
```

---

## Conformal Maps — Definition and Basic Properties

A holomorphic map f: Ω → ℂ is **conformal at z₀** if f'(z₀) ≠ 0. It is conformal (on Ω) if conformal at every point.

**Why angles are preserved**: f'(z₀) = |f'(z₀)| e^{iα}. This is a local linear approximation: f rotates tangent vectors by α and scales by |f'(z₀)|. Since the *same* rotation α applies to all directions, the angle between any two curves through z₀ is preserved.

```
TWO CURVES THROUGH z₀:
   γ₁ and γ₂ with angle θ between tangents

   AFTER MAPPING BY f:
   f(γ₁) and f(γ₂) with angle θ between tangents
   (same angle, same orientation)

AT CRITICAL POINTS (f'(z₀) = 0):
   f(z) − f(z₀) ≈ c(z − z₀)^k
   Angles are MULTIPLIED by k  (not preserved)
```

**Biholomorphic** = holomorphic bijection with holomorphic inverse. These are the "conformal equivalences" between domains.

---

## Möbius Transformations (Linear Fractional Transformations)

A **Möbius transformation** is f(z) = (az + b)/(cz + d), where a, b, c, d ∈ ℂ and ad − bc ≠ 0.

These are the automorphisms of the Riemann sphere ℂ ∪ {∞}. They form the group PGL(2, ℂ) ≅ PSL(2, ℂ).

**Key properties**:

```
1. Bijection ℂ ∪ {∞} → ℂ ∪ {∞}
   Maps circles and lines to circles and lines
   (lines = circles through ∞ on Riemann sphere)

2. Composition of Möbius transformations is Möbius
   (closed under composition — they form a group)

3. Determined by THREE points: given z₁,z₂,z₃ and their images w₁,w₂,w₃,
   there is a unique Möbius transformation sending zⱼ → wⱼ

4. Fixed points: solve f(z) = z  →  quadratic  →  0, 1, or 2 fixed pts
   (on Riemann sphere, always exactly 2 counting multiplicity)

5. Cross-ratio invariant:
   (z−z₁)(z₂−z₃) / [(z−z₃)(z₂−z₁)] is preserved under Möbius maps
```

### Building Block Möbius Maps

Every Möbius transformation is a composition of:
- Translation: z ↦ z + b
- Dilation/rotation: z ↦ az  (|a| ≠ 1 scales, arg(a) ≠ 0 rotates)
- Inversion: z ↦ 1/z  (most important — maps the interior of unit disk to exterior)

### Standard Möbius Maps

**Upper half-plane to unit disk**:
    f(z) = (z − i)/(z + i)
    Maps ℍ = {Im(z) > 0} → D = {|w| < 1}
    Sends 0 ↦ −1, 1 ↦ (1−i)/(1+i), ∞ ↦ 1, i ↦ 0

**Disk to disk** (automorphisms of D):
    f(z) = e^{iθ} (z − a)/(1 − āz)    for |a| < 1, θ ∈ ℝ
    These are ALL automorphisms of the unit disk (Schwarz-Pick lemma)

**Cayley transform**:
    f(z) = (z − i)/(z + i)  maps ℍ to D
    f⁻¹(w) = i(1 + w)/(1 − w)  maps D to ℍ
    In signal processing / control: maps unit circle to jω-axis

---

## Power Maps

**f(z) = zⁿ** (n ≥ 2, integer):
- Maps sectors {0 < arg(z) < 2π/n} to the full slit plane
- n-to-1 map of ℂ (except at 0)
- Useful for straightening sector boundaries

**f(z) = z^{1/n}** (principal branch):
- Maps slit plane ℂ \ (−∞, 0] to sector {|arg w| < π/n}
- Conformal on the slit plane

**Example — mapping a wedge to a half-plane**:
    Wedge: {0 < arg(z) < π/3}  (60° sector)
    Map w = z³: maps wedge to upper half-plane ℍ
    (arg(z³) = 3 arg(z), so 0 < 3 arg(z) < π = upper half-plane)

---

## Exponential and Logarithm

**f(z) = e^z**:
- Maps horizontal strip {0 < Im(z) < π} to upper half-plane ℍ
- Maps horizontal strip {0 < Im(z) < 2π} to punctured plane ℂ \ {0}
- Real axis → positive real axis; axis Im(z)=π → negative real axis

**f(z) = log z** (principal branch):
- Maps ℂ \ (−∞, 0] to horizontal strip {−π < Im(w) < π}
- Inverse of e^z restricted to this strip

```
STRIP → HALF-PLANE PIPELINE:
  Complicated polygon domain
        ↓  Schwarz-Christoffel
  Upper half-plane ℍ
        ↓  Cayley transform
  Unit disk D
        ↓  explicit formula
  Solve boundary value problem
        ↓  compose all maps
  Solution on original domain
```

---

## Joukowski Transform

The **Joukowski transformation** w = z + 1/z is the bridge between complex analysis and aerodynamics.

```
JOUKOWSKI TRANSFORMATION: w = z + 1/z = z + z^{-1}

  CRITICAL POINTS: w'(z) = 1 − 1/z² = 0  →  z = ±1
  (Not conformal at z = ±1 — these become cusps)

  ACTION ON CIRCLES:
  Circle |z| = 1 (unit circle):
    z = e^{iθ}:  w = e^{iθ} + e^{-iθ} = 2cos θ  → real segment [−2, 2]
    The unit circle maps to the interval [−2, 2] on the real axis
    (degenerate: circle → line segment)

  Circle |z| = R > 1:
    z = Re^{iθ}:  w = Re^{iθ} + (1/R)e^{-iθ}
    x = (R + 1/R)cos θ,  y = (R − 1/R)sin θ  → ELLIPSE
    semi-axes:  a = R + 1/R,  b = R − 1/R

  Circle through z = 1 (offset circle):
    → JOUKOWSKI AIRFOIL (realistic wing profile)
```

**Airfoil design**: Start with a circle in the z-plane passing near z = −1 and through z = +1. The Joukowski transform maps this to an airfoil cross-section with a cusped trailing edge.

The exterior of the circle (flow around cylinder) maps to the exterior of the airfoil (flow around wing). The known cylinder solution (from complex potential flow) becomes the wing solution. This is how Joukowski calculated lift analytically in 1910, decades before computers.

---

## Schwarz-Christoffel Transform

Maps the upper half-plane ℍ (or unit disk D) to the interior of a polygon with prescribed vertices and angles.

For polygon with vertices w₁, ..., wₙ and interior angles α₁π, ..., αₙπ:

    f(z) = C + A ∫_0^z ∏ⱼ (ζ − zⱼ)^{αⱼ−1} dζ

where z₁ < z₂ < ... < zₙ are pre-images of the vertices on the real axis, A is a scaling constant, C is a translation.

```
POLYGON SHAPES AND THEIR SCHWARZ-CHRISTOFFEL MAPS:

  Rectangle:       angles π/2 each     → elliptic integral
  Triangle:        angles α, β, γ      → hypergeometric function
  Strip (degenerate polygon):           → e^z or log z
  Right-angle wedge:                    → z²
  Slit (degenerate):                    → z^{1/2}
```

**Application**: Solving Laplace's equation (electrostatics, heat, flow) with polygon-shaped boundaries. Map to half-plane where Poisson/Schwarz formula applies.

---

**The upper half-plane as moduli space.** Beyond signal processing, ℍ plays a deeper role in number theory and algebraic geometry. The automorphisms of ℍ form SL(2, ℝ) acting by Möbius transformations τ ↦ (aτ+b)/(cτ+d). The discrete subgroup SL(2, ℤ) (integer entries, determinant 1) acts on ℍ, and the quotient ℍ/SL(2, ℤ) is the **moduli space of elliptic curves**: each point τ ∈ ℍ/SL(2, ℤ) parametrizes a conformally distinct torus ℂ/(ℤ + τℤ). The j-invariant j(τ) is the map ℍ/SL(2, ℤ) → ℂ that classifies tori. Modular forms — holomorphic functions on ℍ with prescribed transformation behavior under SL(2, ℤ) — are central to number theory (modularity theorem, Langlands program).

---

## Riemann Mapping Theorem — Statement and Significance

**Theorem**: Let Ω ⊂ ℂ be simply connected with Ω ≠ ℂ. Fix z₀ ∈ Ω. Then there is a unique biholomorphic map f: Ω → D (the unit disk) with f(z₀) = 0 and f'(z₀) > 0.

**Why Ω ≠ ℂ matters**: ℂ is simply connected but not conformally equivalent to D. (Liouville: any bounded entire function is constant, so a biholomorphic map ℂ → D would be bounded and entire, hence constant — contradiction.)

**The theorem guarantees existence but the explicit map is hard**: For a given domain Ω, finding the Riemann map explicitly requires Schwarz-Christoffel for polygons, or numerical methods in general. The theorem says the map exists and is unique; it does not give a formula.

**Corollary**: Any two simply connected proper subdomains of ℂ are conformally equivalent to each other (via Ω₁ → D → Ω₂). The "shape" of a simply connected domain is irrelevant for complex analysis — only topology matters.

---

## Solving Laplace's Equation via Conformal Maps

Laplace's equation (∇²u = 0) is preserved by conformal maps:

**Principle**: If f: Ω → Ω' is conformal and U is harmonic on Ω', then u = U ∘ f is harmonic on Ω.

**Recipe for Dirichlet problem on Ω**:
1. Find conformal map f: Ω → D (unit disk) or ℍ (half-plane)
2. Transform boundary conditions under f
3. Solve Dirichlet problem on D or ℍ using Poisson formula
4. Pull back: u(z) = U(f(z))

```
POISSON FORMULA ON UNIT DISK:
  U(re^{iθ}) = (1/2π) ∫_0^{2π} P(r, θ−φ) u(e^{iφ}) dφ

  Poisson kernel:  P(r, θ) = (1 − r²)/(1 − 2r cos θ + r²)

POISSON FORMULA ON UPPER HALF-PLANE:
  U(x,y) = (y/π) ∫_{-∞}^{∞} u(t)/(( x−t)² + y²) dt

  Cauchy-Poisson kernel:  y/π · 1/((x−t)² + y²)
```

---

## The Schwarz Lemma and Schwarz-Pick

**Schwarz Lemma**: If f: D → D is holomorphic with f(0) = 0, then |f(z)| ≤ |z| and |f'(0)| ≤ 1. If equality holds at any nonzero point (or if |f'(0)| = 1), then f(z) = e^{iθ}z (a rotation).

**Schwarz-Pick Lemma**: Any holomorphic f: D → D is a contraction of the hyperbolic metric on D:

    |f'(z)| / (1 − |f(z)|²) ≤ 1 / (1 − |z|²)

Equality holds iff f is an automorphism of D (a Möbius transformation of D).

The hyperbolic (Poincaré) metric on D is ds = 2|dz|/(1 − |z|²). The Schwarz-Pick lemma says holomorphic self-maps of D are non-expanding in this metric.

---

## Application: Potential Flow Around an Airfoil

This is the synthesis of conformal mapping, complex potential flow (from fluid dynamics), and the Joukowski transform:

```
STEP 1: Complex potential for flow around cylinder
  W(z) = U(z + 1/z) + (iΓ/2π) log z
  (uniform flow U∞ + vortex of circulation Γ)
  Velocity: dW/dz = U(1 − 1/z²) + iΓ/(2πz)

STEP 2: Joukowski transform w = z + 1/z
  Maps exterior of circle to exterior of airfoil

STEP 3: Kutta-Joukowski condition
  Γ chosen so velocity is finite at trailing edge
  (trailing edge = critical point of Joukowski map)
  Γ = 4πUR sin(α + β)  where α = angle of attack, β = geometric angle

STEP 4: Lift
  Kutta-Joukowski theorem: L = ρU∞Γ  (lift per unit span)
  This is why circulation Γ generates lift
```

---

## Decision Cheat Sheet

| Goal | Map to use |
|------|-----------|
| Upper half-plane → disk | f(z) = (z−i)/(z+i) (Cayley) |
| Disk → upper half-plane | f(w) = i(1+w)/(1−w) |
| Sector {0 < arg(z) < π/n} → half-plane | w = zⁿ |
| Strip {0 < Im(z) < π} → half-plane | w = e^z |
| Half-plane → strip | w = log z |
| Circle → ellipse or airfoil | Joukowski: w = z + 1/z |
| Polygon domain → half-plane | Schwarz-Christoffel formula |
| Arbitrary simply-connected → disk | Riemann Mapping Theorem (existence) |
| Solve Laplace on Ω | Conformally map Ω to disk; Poisson formula |
| Flow around airfoil | Joukowski + complex potential + Kutta condition |

---

## Common Confusion Points

**Conformal ≠ bijective**: f(z) = z² is conformal at every z ≠ 0, but it is not injective (it is 2-to-1). For the Riemann Mapping Theorem, you need a biholomorphic bijection, not just any conformal map.

**Riemann Mapping Theorem doesn't give an explicit map**: It guarantees existence and uniqueness. For a specific domain (polygon, half-strip, etc.), you need Schwarz-Christoffel, power maps, or exponentials to find the map explicitly.

**Möbius maps preserve circles and lines — not straight lines specifically**: A line in the plane is a circle of infinite radius passing through ∞. Möbius maps map circles to circles where "circles" includes lines. A straight line can map to a true circle.

**The Joukowski transform maps the circle to a slit, not to an airfoil**: The unit circle maps to the segment [−2, 2]. It's the off-center circle (displaced slightly up and left, passing through z=1) that maps to an airfoil. The displacement controls the camber and thickness.

**Schwarz-Christoffel has free parameters**: Three of the pre-images zⱼ on the real axis can be fixed arbitrarily (by the Möbius freedom — 3 real parameters). The rest are determined by the polygon geometry. Finding the free parameters is generally a transcendental system.
