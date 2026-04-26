# Harmonic Functions and the Dirichlet Problem

## The Big Picture

Harmonic functions are solutions to Laplace's equation ∇²u = 0. They appear in electrostatics (electric potential), steady-state heat conduction, fluid potential flow, and gravitational theory. Complex analysis provides the most powerful two-dimensional toolkit for harmonic functions: every harmonic function is locally the real part of a holomorphic function, and conformal maps preserve harmonicity. The Dirichlet problem (find a harmonic function with prescribed boundary values) is solved explicitly on the disk and upper half-plane via the Poisson formula.

```
HARMONIC FUNCTIONS — LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  DEFINITION:  u: Ω ⊂ ℝ² → ℝ  harmonic  ↔  ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0

  ┌─────────────────────────────────────────────────────────────────────┐
  │  COMPLEX ANALYSIS CONNECTION                                        │
  │  f = u + iv  holomorphic  ⟹  u harmonic,  v harmonic              │
  │  Converse: given u harmonic on simply connected Ω,                  │
  │            ∃ harmonic conjugate v: u + iv holomorphic on Ω          │
  └─────────────────────────────────────────────────────────────────────┘

  KEY PROPERTIES (flow from Cauchy theory):
  ─ Mean value property: u(z₀) = average of u on any circle centered at z₀
  ─ Maximum principle: u achieves max/min on boundary, not interior
  ─ Real-analyticity: harmonic ⟹ C^∞, in fact real-analytic
  ─ Unique determination by boundary values (Dirichlet problem)
  ─ Preserved by conformal maps

  DIRICHLET PROBLEM:
  Given: boundary values u = g on ∂Ω
  Find: harmonic u on Ω with those boundary values
  Solution: Poisson formula (explicit on disk and half-plane)
```

---

## Harmonic Functions — Basic Properties

### Laplace's Equation in 2D

    ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0

In polar coordinates (r, θ):
    ∇²u = ∂²u/∂r² + (1/r)∂u/∂r + (1/r²)∂²u/∂θ² = 0

**Harmonic polynomials** (low-degree solutions):
- Degree 0: constants
- Degree 1: ax + by (any linear function)
- Degree 2: x² − y², xy, ax + by + c (not x² + y²)
- Degree n (complex notation): Re(zⁿ) and Im(zⁿ)

The n-th harmonic polynomials are Re(zⁿ) = r^n cos(nθ) and Im(zⁿ) = r^n sin(nθ) — the building blocks of Fourier series on circles.

### Connection to Holomorphic Functions

If f = u + iv is holomorphic, then u and v satisfy Laplace's equation (proved via CR equations — see 01-ANALYTIC-FUNCTIONS.md). The converse:

**Existence of harmonic conjugate**: If Ω is simply connected and u is harmonic on Ω, then there exists v: Ω → ℝ such that u + iv is holomorphic. v is unique up to a constant.

**Construction**: Given u harmonic, define v by the line integral:

    v(x,y) = ∫_{(x₀,y₀)}^{(x,y)} (−∂u/∂y dx + ∂u/∂x dy)

This integral is path-independent (follows from Green's theorem + harmonicity of u) on simply connected domains.

**On multiply connected domains**: The conjugate may be multi-valued. Example: u = ln r = ln|z| is harmonic on ℂ \ {0}, but its conjugate v = θ = arg(z) is multi-valued (it is the imaginary part of log z, which is multi-valued on ℂ \ {0}).

---

## Mean Value Property

**Theorem**: If u is harmonic in a disk D(z₀, R), then

    u(z₀) = (1/2π) ∫_0^{2π} u(z₀ + re^{iθ}) dθ    for all r < R

The value of u at any point equals the average of u on any circle centered at that point.

**Proof**: u = Re(f) for holomorphic f near z₀. Apply Cauchy's integral formula to f:

    f(z₀) = (1/2πi) ∮_{|z−z₀|=r} f(z)/(z−z₀) dz = (1/2π) ∫_0^{2π} f(z₀ + re^{iθ}) dθ

Taking real parts gives the mean value property for u. □

**Conversely** (Converse of Mean Value Property): If u is continuous and satisfies the mean value property, then u is harmonic. This is Morera's theorem for harmonic functions.

---

## Maximum and Minimum Principles

**Maximum Principle**: If u is harmonic on a bounded connected domain Ω and continuous on Ω̄ = Ω ∪ ∂Ω, then u achieves its maximum and minimum on the boundary ∂Ω.

More precisely: if u achieves its maximum at an interior point z₀, then u is constant (on the connected component containing z₀).

**Proof**: If u(z₀) = M = max of u, then by the mean value property u(z₀) = average of u on any circle centered at z₀. Since u ≤ M everywhere, and the average is M, we must have u = M everywhere on the circle. Since this holds for all small r, u = M in a neighborhood of z₀. By connectedness, u = M on all of Ω. □

**Consequence — Uniqueness of Dirichlet Problem**: If u₁ and u₂ are both harmonic on Ω with u₁ = u₂ on ∂Ω, then u₁ = u₂ on all of Ω. (Apply maximum principle to u₁ − u₂: achieves max and min of 0 on boundary, so u₁ − u₂ ≡ 0.)

**Hadamard's Three Circles Theorem**: For f holomorphic on r₁ ≤ |z| ≤ r₂, log M(r) is convex in log r. (Follows from maximum principle applied to log|f|.)

---

## The Dirichlet Problem

**Problem**: Given a domain Ω with boundary ∂Ω, and a continuous function g: ∂Ω → ℝ, find a function u harmonic on Ω and continuous on Ω̄ with u = g on ∂Ω.

Existence and uniqueness:
- Uniqueness: from maximum principle (always holds)
- Existence: holds for regular domains (smooth boundaries, or even Lipschitz)

### Poisson Formula on the Unit Disk

For u harmonic on D = {|z| < 1} with boundary values u = g on ∂D = {|z| = 1}:

    u(re^{iφ}) = (1/2π) ∫_0^{2π} P_r(φ − θ) g(e^{iθ}) dθ    for r < 1

where P_r(ψ) = (1 − r²)/(1 − 2r cos ψ + r²) is the **Poisson kernel**.

```
POISSON KERNEL PROPERTIES:

  P_r(ψ) > 0  for r < 1  (positive — no cancellation)
  (1/2π) ∫_0^{2π} P_r(ψ) dψ = 1  (normalized — it's a probability kernel)
  P_r(ψ) → δ(ψ)  as r → 1⁻  (concentrates at the boundary point)

  ↑  These three properties make P_r(ψ) an "approximate identity" (Dirac delta approximation)
```

**Derivation**: Use Cauchy's integral formula for a holomorphic f with u = Re(f):

    f(z) = (1/2πi) ∮_{|ζ|=1} f(ζ)/(ζ−z) dζ

For |z| < 1 = |ζ|, the conjugate point z* = 1/z̄ satisfies |z*| > 1 (outside disk), so 1/(ζ−z*) contributes 0 by Cauchy's theorem. Combining:

    f(z) = (1/2πi) ∮_{|ζ|=1} f(ζ) · [1/(ζ−z) + 1/(ζ(1/z̄−ζ))] dζ/2 → Poisson formula

### Poisson Formula on the Upper Half-Plane

For u harmonic on ℍ = {Im(z) > 0} with boundary values u = g on ℝ:

    u(x + iy) = (y/π) ∫_{-∞}^{∞} g(t)/((x−t)² + y²) dt    for y > 0

The Cauchy-Poisson kernel: P(x,y;t) = y/(π[(x−t)² + y²]) is the Cauchy distribution (in probability theory) and the fundamental solution of Laplace's equation in the half-plane.

### Green's Function

For a general domain Ω, the **Green's function** G(z, z₀) is the harmonic function with a "logarithmic point source":

    G(z, z₀) = log|z − z₀| + h(z, z₀)

where h is harmonic on Ω (corrects for boundary conditions: G = 0 on ∂Ω).

Green's function exists for any regular domain and provides the kernel for solving the Dirichlet problem:

    u(z₀) = −(1/2π) ∫_{∂Ω} g(z) ∂G(z,z₀)/∂n ds

where ∂/∂n is the outward normal derivative on ∂Ω.

**Green's function for the disk**: G(z, z₀) = log|z − z₀| − log|1 − z̄₀ z| + log|z₀|

(The second term uses the "Schwarz reflection" of z₀ through the unit circle.)

---

**Why the complex analysis approach is special to 2D.** Everything in this file depends on the connection: harmonic function = real part of holomorphic function. This is fundamentally a 2D phenomenon. In ℝⁿ for n ≥ 3, Laplace's equation ∇²u = 0 still has solutions (harmonic functions), and the maximum principle, mean value property, and Harnack inequality all generalize. But the *holomorphic function machinery* does not: there is no notion of "holomorphic" in ℝ³ that links to ∇²u = 0 (the closest analogue, quaternionic analysis, does not have the same power). Conformal maps in ℝⁿ for n ≥ 3 are severely restricted — only Möbius transformations (Liouville's theorem in differential geometry), not the infinite-dimensional family of holomorphic maps in 2D. The fundamental solution also differs: log|z| in 2D vs. 1/|x|^{n−2} in ℝⁿ. For 3D PDEs, one uses Green's functions, spherical harmonics, and potential theory directly — without the conformal mapping shortcuts available here.

---

## Subharmonic and Superharmonic Functions

**Subharmonic**: u satisfies ∇²u ≥ 0. Equivalently: u(z₀) ≤ average of u on circles.
**Superharmonic**: u satisfies ∇²u ≤ 0. Equivalently: u(z₀) ≥ average.
**Harmonic**: ∇²u = 0. Both subharmonic and superharmonic.

**Maximum principle for subharmonic functions**: Subharmonic functions achieve their maximum on the boundary, not interior (same as harmonic, but not minimum).

**Examples**: |f(z)|^p for holomorphic f and p > 0 is subharmonic. log|f(z)| is subharmonic when f is holomorphic. These are central to potential theory.

---

## Physical Interpretations

### Electrostatics

An electrostatic potential φ in a charge-free region satisfies ∇²φ = 0. The electric field E = −∇φ. Level curves of φ are equipotentials; gradient lines are field lines.

The complex potential f = φ + iψ (where ψ is the stream function / harmonic conjugate of φ) is holomorphic. In the Argand plane:
- Level curves of Re(f) = φ: equipotentials
- Level curves of Im(f) = ψ: field lines
- These two families of curves are orthogonal (since f is conformal)

### Steady-State Heat Conduction

For temperature distribution T in a 2D solid with no heat sources: ∇²T = 0. Same mathematics as electrostatics. Given temperatures on the boundary → unique harmonic function in the interior → Poisson formula gives the solution.

### Incompressible Irrotational Flow

For ideal (inviscid, incompressible) 2D flow:
- Velocity potential φ: v = ∇φ, ∇²φ = 0
- Stream function ψ: orthogonal to φ, ∇²ψ = 0
- Complex velocity: f'(z) = dW/dz = u(x,y) − iv(x,y)
- where W = φ + iψ is the complex potential

Flow is determined by a holomorphic function W(z). See 09-APPLICATIONS.md.

---

## Harnack's Theorem and Regularity

**Harnack's Inequality**: If u is positive harmonic in D(0, R) and |z| ≤ r < R:

    (R − r)/(R + r) · u(0) ≤ u(z) ≤ (R + r)/(R − r) · u(0)

**Harnack's Theorem**: A monotone increasing sequence of harmonic functions that is bounded above at one point converges uniformly on compact sets (to a harmonic function or to +∞ everywhere).

**Interior regularity**: Harmonic functions are real-analytic (have convergent power series in x and y) on the interior of their domain. This follows from the Poisson formula: the Poisson kernel is real-analytic in the interior variable.

---

## Connection to Potential Theory

The **Newtonian potential** in 2D is the logarithmic potential:

    u(z) = (1/2π) ∫ log|z − ζ| dμ(ζ)

where μ is a measure (charge distribution). This satisfies ∇²u = −μ (Poisson's equation, not Laplace's) in the sense of distributions.

**Fundamental solution of Laplace's equation in ℝ²**:

    G(z) = (1/2π) log|z|

(The "1/r" potential in 2D is logarithmic, unlike 3D where it is 1/r.)

**Equilibrium measure**: For a compact set K, the equilibrium measure is the distribution of charge on K that minimizes energy E(μ) = ∬ log|z−ζ|⁻¹ dμ(z)dμ(ζ). Its support is on ∂K, and the corresponding potential is constant on K.

---

## Decision Cheat Sheet

| Problem | Solution |
|---------|---------|
| Solve Laplace on unit disk with boundary data g | Poisson formula u(re^{iφ}) = ∫ P_r(φ-θ) g(e^{iθ}) dθ/2π |
| Solve Laplace on upper half-plane with data g(t) | Cauchy-Poisson: u(x+iy) = (y/π)∫ g(t)/((x-t)²+y²) dt |
| Solve Laplace on general domain Ω | Map Ω → disk (Riemann), then Poisson |
| Show u is constant on Ω | Maximum principle: if u has no boundary, u = constant |
| Find harmonic conjugate of u | Integrate: v = ∫(−∂u/∂y dx + ∂u/∂x dy) |
| Show u is real-analytic | u = Re(f) for holomorphic f → real-analytic |
| Prove uniqueness of Dirichlet problem | Maximum principle: u₁−u₂ harmonic, zero on boundary → zero everywhere |

---

## Common Confusion Points

**Harmonic ≠ holomorphic**: u(x,y) = x is harmonic (∂²x/∂x² + ∂²x/∂y² = 0) but not the real part of a holomorphic function that is *real* on the real axis in any complicated way. More precisely: every harmonic function is the real part of *some* holomorphic function (on simply connected domains), but you need to find the conjugate.

**The harmonic conjugate is not unique globally on multiply connected domains**: On ℂ \ {0}, ln|z| is harmonic, but its conjugate arg(z) is multi-valued. The period of arg(z) around the origin is 2π, and you cannot make it single-valued on ℂ \ {0}.

**Poisson formula is only for domains conformally equivalent to the disk**: For general domains, you need Green's function. The Poisson formula is explicit because it exploits the symmetry of the disk.

**Subharmonic ≠ harmonic**: |f|^p is subharmonic for holomorphic f but not harmonic unless f is constant or p is chosen very specially. The distinction matters in potential theory: subharmonic functions satisfy a maximum principle but not a minimum principle.

**∇²u = 0 in ℝ² vs ℝ³ have different Green's functions**: In 2D, the fundamental solution is log|x|. In 3D, it is 1/|x|. This affects physical interpretations: a point charge in 2D (= infinite line charge in 3D) produces a logarithmic potential; in 3D, a point charge produces 1/r potential.
