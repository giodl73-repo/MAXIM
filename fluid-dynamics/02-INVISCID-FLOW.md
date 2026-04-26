# Ideal and Inviscid Flow

## The Big Picture

Inviscid flow (μ = 0) is the foundation of classical fluid dynamics. Without viscosity, the Euler equations admit exact analytical solutions via potential flow — and potential flow is holomorphic function theory in disguise. Bernoulli's equation is the most famous result: along a streamline, higher velocity means lower pressure. This underpins aerodynamics (lift), hydraulics (flow meters), and atmospheric dynamics. D'Alembert's paradox — that inviscid theory predicts zero drag on a body — shows the limits of ideal flow and motivates the boundary layer theory of Prandtl.

```
INVISCID FLOW — CONCEPTUAL STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  EULER EQUATIONS:
  ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇p + ρ**g**
  ∇·**v** = 0  (incompressible)

  IRROTATIONAL FLOW (∇ × **v** = 0):
  ┌──────────────────────────────────────────────────────────────────────┐
  │  ∇ × **v** = 0  ⟹  **v** = ∇φ  (velocity potential exists)           │
  │  Continuity: ∇·∇φ = 0  ⟹  ∇²φ = 0  (Laplace equation!)          │
  │                                                                      │
  │  In 2D: φ + iψ = W(z)  is HOLOMORPHIC                                │
  │  (velocity potential = real part of complex potential)               │
  └──────────────────────────────────────────────────────────────────────┘

  BERNOULLI'S EQUATION:
  Steady, incompressible, inviscid, along a streamline:
  p/ρ + v²/2 + gz = constant  (total energy per unit mass conserved)
```

---

## Euler Equations

**Incompressible inviscid** (μ = 0):

    ∂**v**/∂t + (**v**·∇)**v** = −(1/ρ)∇p + **g**
    ∇·**v** = 0

Using the vector identity (**v**·∇)**v** = ∇(v²/2) − **v** × **ω**:

    ∂**v**/∂t + ∇(v²/2) − **v** × **ω** = −(1/ρ)∇p + **g**

For irrotational flow (**ω** = 0):

    ∂∇φ/∂t + ∇(v²/2) = −(1/ρ)∇p + ∇(−gz)

    ∇[∂φ/∂t + v²/2 + p/ρ + gz] = 0

    ⟹  ∂φ/∂t + v²/2 + p/ρ + gz = f(t)  (unsteady Bernoulli)

---

## Bernoulli's Equation — Three Forms

### Form 1: Along a Streamline (Steady, Any Inviscid Flow)

    p + (1/2)ρv² + ρgz = const  (along a streamline)

    or: p/ρ + v²/2 + gz = const

**Derivation**: Dot Euler's equation with **v** (along the streamline):

    d/ds[p/ρ + v²/2 + gz] = 0

where s is arc length along the streamline.

**Applications**:
- Pitot tube: measures v from stagnation pressure
- Venturi meter: measures flow rate from pressure difference
- Lift generation: faster flow over wing → lower pressure on top

### Form 2: Irrotational Steady Flow (Entire Domain)

    p + (1/2)ρv² + ρgz = const  (everywhere, not just streamlines)

This stronger form holds because irrotational flow has potential φ, and the constant is the same for all streamlines.

### Form 3: Unsteady Irrotational

    ∂φ/∂t + (1/2)|∇φ|² + p/ρ + gz = f(t)

---

## Potential Flow — The Holomorphic Framework

For 2D, steady, incompressible, irrotational flow:

    ∇²φ = 0    (Laplace equation for velocity potential)
    **v** = ∇φ = (∂φ/∂x, ∂φ/∂y)

The **stream function** ψ satisfies: **v** = (∂ψ/∂y, −∂ψ/∂x) and ∇²ψ = 0.

The **complex potential**: W(z) = φ(x,y) + iψ(x,y)

    dW/dz = ∂φ/∂x + i∂ψ/∂x = u − iv    (complex velocity)

W(z) is holomorphic (Cauchy-Riemann = Laplace for both φ and ψ + irrotationality condition). Every holomorphic function defines a valid 2D potential flow.

```
POTENTIAL FLOW ↔ HOLOMORPHIC FUNCTION DICTIONARY:
  ─────────────────────────────────────────────────────
  Complex potential W(z)     ↔  holomorphic function
  Real part φ = Re(W)        ↔  velocity potential  (equipotentials)
  Imag part ψ = Im(W)        ↔  stream function     (streamlines)
  dW/dz = u − iv             ↔  complex velocity
  |dW/dz|                    ↔  flow speed
  dW/dz = 0                  ↔  stagnation point
  Conformal map of W         ↔  maps one flow to another flow
```

---

## Elementary Flows and Superposition

Potential flow is **linear** (Laplace equation is linear), so solutions can be superposed.

### Uniform Flow

    W = U∞ z = U∞(x + iy)
    φ = U∞x,  ψ = U∞y
    u = U∞,   v = 0  (flow in x-direction)

### Source/Sink at Origin (strength m, m > 0 = source)

    W = (m/2π) log z
    φ = (m/2π) ln r,  ψ = (m/2π)θ
    u_r = m/(2πr),  u_θ = 0  (radial flow)

Source: fluid emerges from origin (mass added). Sink: m < 0 (mass removed).

### Vortex at Origin (circulation Γ)

    W = −(iΓ/2π) log z
    φ = (Γ/2π)θ,  ψ = −(Γ/2π) ln r
    u_r = 0,  u_θ = Γ/(2πr)  (swirling flow, zero radial)

Circulation: Γ = ∮_C **v**·d**l** = ∮_C u_θ r dθ = Γ (consistent).

The vortex is irrotational everywhere except at r = 0 (which is a singularity). This is the "potential vortex" — has circulation but no vorticity away from the axis.

### Doublet at Origin

    W = μ/(2πz)  (where μ is the doublet strength)
    φ = μ cos θ / (2πr),  ψ = −μ sin θ / (2πr)

A doublet is a source-sink pair in the limit of vanishing separation: the flow pattern is dipole-like.

### Flow Around a Cylinder (radius R, uniform flow U∞)

Superpose uniform flow + doublet (doublet strength μ = 2πU∞R²):

    W(z) = U∞(z + R²/z)
    φ = U∞(r + R²/r)cos θ
    u_r = U∞(1 − R²/r²)cos θ    (vanishes on r = R: boundary condition satisfied)
    u_θ = −U∞(1 + R²/r²)sin θ

Stagnation points: dW/dz = U∞(1 − R²/z²) = 0 → z = ±R (at θ = 0, π on the cylinder).

Surface pressure (Bernoulli): p = p_∞ + (1/2)ρU∞²(1 − 4sin²θ)
Lift = 0 (fore-aft symmetry). Drag = 0 (D'Alembert's paradox).

Adding a vortex of circulation Γ:
    W(z) = U∞(z + R²/z) − (iΓ/2π) log z
    Lift = ρU∞Γ  (Kutta-Joukowski theorem — lift generated by circulation!)

---

## Kelvin's Circulation Theorem and Helmholtz's Laws

**Kelvin's Circulation Theorem**: In an inviscid, barotropic flow with conservative body forces, the circulation Γ = ∮_C **v**·d**l** around a material loop C (a loop that moves with the fluid) is constant:

    DΓ/Dt = 0

**Meaning**: Vorticity is conserved in inviscid flow. If a parcel has no vorticity initially, it never acquires any (in ideal flow). Vorticity can only be created by viscosity (at walls) or baroclinic effects (density gradients).

**Helmholtz's Vortex Laws** (for inviscid, barotropic flow):
1. **No free ends**: Vortex lines cannot end inside a fluid — they form closed loops or end on boundaries.
2. **Vortex tubes move with the fluid**: The vortex tube of a set of fluid parcels retains those parcels (material).
3. **Circulation of a vortex tube is constant**: Along the tube and in time.

---

## D'Alembert's Paradox

**Statement**: In potential (inviscid, irrotational) flow, the net drag force on a body is zero (regardless of body shape).

**Proof**: For flow around any body in uniform stream U∞, the pressure integral over the body surface yields zero net force by symmetry of potential flow. The fore and aft pressure distributions are mirror images.

**Resolution** (why real bodies have drag):
1. **Viscous drag**: No-slip → boundary layer → wake. The viscous boundary layer breaks the fore-aft symmetry.
2. **Pressure drag (form drag)**: Boundary layer separation creates a wake with lower pressure. Separated flow ≠ potential flow.
3. **Wave drag** (at high speed): Shock waves dissipate momentum.

D'Alembert's paradox was a major puzzle for 150+ years (1752–1904). Prandtl resolved it with boundary layer theory.

---

## Irrotational vs Rotational Flows

```
IRROTATIONAL (∇ × **v** = 0):          ROTATIONAL (∇ × **v** ≠ 0):
  Velocity potential exists: **v** = ∇φ    No potential
  Laplace equation for φ                  Full vorticity equation needed
  Complex potential W(z) in 2D            No such tool in general
  No vortex stretching in 2D             Vortex stretching possible
  D'Alembert: no drag                    Realistic: drag exists
  Analytical solutions possible          Usually numerical
  Examples: far-field of wing,           Examples: vortex core, near-wall
            acoustic waves, water waves  boundary layer, turbulence
```

---

## Kelvin-Stokes Theorem and Circulation

The link between vorticity and circulation:

    Γ = ∮_C **v**·d**l** = ∫∫_S (**∇ × **v**)**·dS = ∫∫_S **ω**·dS

Circulation = flux of vorticity through any surface bounded by C.

**For a 2D flow**: If **ω** = ω(x,y)ẑ (out-of-plane), then:
    Γ = ∫∫ ω dA

The potential vortex W = −(iΓ/2π) log z has zero vorticity everywhere except at the origin, yet has circulation Γ around any loop enclosing the origin. The origin is a point vortex — a singularity where all vorticity is concentrated.

---

## Applications of Bernoulli and Potential Flow

### Pitot Tube (measuring airspeed)

```
   STAGNATION POINT                FREE STREAM
        ×                         →→→→→→→→→
      p = p_stag                  p = p_∞,  v = V
   (velocity = 0)

   Bernoulli: p_stag = p_∞ + (1/2)ρV²
   V = √(2(p_stag − p_∞)/ρ)
```

### Venturi Meter (measuring flow rate in a pipe)

```
   Area A₁        Area A₂ < A₁       Area A₁
   →→→→            →→→→→→             →→→→
   v₁, p₁         v₂ > v₁, p₂ < p₁   v₁, p₁

   Continuity: A₁v₁ = A₂v₂
   Bernoulli:  p₁ + ½ρv₁² = p₂ + ½ρv₂²
   Flow rate: Q = A₁A₂ √(2(p₁−p₂)/(ρ(A₁²−A₂²)))
```

### Flow Over a Hill (potential flow around a bump)

Potential flow over a sinusoidal hill: use conformal map to transform flat surface to bumped surface. Higher velocity over hilltop → lower pressure → clouds can form (adiabatic cooling in low-pressure region).

---

## Decision Cheat Sheet

| Situation | Approach |
|----------|---------|
| 2D inviscid irrotational flow | Complex potential W(z) = φ + iψ |
| Find velocity from potential | **v** = ∇φ, or dW/dz = u − iv |
| Pressure distribution | Bernoulli: p = p_∞ + ½ρ(U∞² − v²) |
| Flow around cylinder | W = U∞(z + R²/z) |
| Lift on airfoil (inviscid) | Kutta-Joukowski: L = ρU∞Γ |
| Prove no drag (inviscid) | D'Alembert's paradox |
| Check if vorticity is conserved | Kelvin's theorem (inviscid, barotropic) |
| Check if potential flow is valid | Need ∇ × **v** = 0, no separation, no shock |

---

## Common Confusion Points

**Potential vortex is irrotational**: The potential vortex W = −(iΓ/2π)log z has circular streamlines and swirling flow, yet ∇ × **v** = 0 everywhere except at the singular point z = 0 (where all the vorticity is concentrated). "Irrotational" refers to the local rotation of fluid elements, not the curvature of streamlines.

**Bernoulli applies along streamlines, not across them** (for rotational flows): For rotational flow, the constant in p + ½ρv² + ρgz = const may differ from streamline to streamline. Only for irrotational flow is the constant global (same everywhere).

**Zero drag (D'Alembert) requires irrotational flow**: If separation occurs (boundary layer detaches), the flow becomes rotational in the wake and D'Alembert no longer applies. Real bodies have drag precisely because the flow separates.

**W(z) = φ + iψ requires incompressible, 2D, irrotational flow**: All three conditions together. Compressible potential flow exists but requires a different equation (not Laplace). Three-dimensional potential flow exists but cannot be described by a single holomorphic function of one complex variable.
