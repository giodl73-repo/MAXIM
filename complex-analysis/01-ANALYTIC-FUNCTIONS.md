# Analytic Functions and Cauchy-Riemann Equations

## The Big Picture

Holomorphic functions are the central object of complex analysis. The Cauchy-Riemann equations are the bridge from the algebraic definition (limit of difference quotient exists) to the analytic structure (power series, harmonic parts). Understanding *why* CR equations are both necessary and sufficient (with continuity) is the entry point for everything else.

```
ANALYTIC FUNCTIONS — CONCEPTUAL MAP
═══════════════════════════════════════════════════════════════════════════════

  COMPLEX FUNCTION  f: Ω ⊂ ℂ → ℂ
  Write z = x + iy,  f(z) = u(x,y) + iv(x,y)
  u, v are real-valued functions of two real variables

  ┌─────────────────────────────────────────────────────────────────────┐
  │  HOLOMORPHIC AT z₀                                                  │
  │  lim_{h→0} [f(z₀+h) − f(z₀)] / h  exists  (h ∈ ℂ, any direction) │
  │                                                                     │
  │  EQUIVALENT CONDITIONS (Goursat: no continuity hypothesis needed):  │
  │  (1) f'(z₀) exists as complex limit                                │
  │  (2) C-R: ∂u/∂x = ∂v/∂y,  ∂u/∂y = −∂v/∂x   (and partials exist) │
  │  (3) f has a convergent power series near z₀                       │
  │  (4) f is conformal at z₀ (if f'(z₀) ≠ 0)                        │
  └─────────────────────────────────────────────────────────────────────┘

  HOLOMORPHIC ON Ω  →  ANALYTIC ON Ω  (classical equivalence)
         │
         ├── real part u satisfies Laplace: ∇²u = 0   (harmonic)
         ├── imag part v satisfies Laplace: ∇²v = 0   (harmonic)
         ├── u and v are C^∞ (infinitely differentiable)
         └── Taylor series at z₀ converges in largest disk in Ω
```

---

## The Complex Number System

Before functions, the domain. Every complex number z = x + iy lives in the Argand plane, with:

    Rectangular form:   z = x + iy,   x = Re(z),  y = Im(z)
    Polar form:         z = r·e^{iθ} = r(cos θ + i sin θ)
    Modulus:            |z| = √(x² + y²) = r
    Argument:           arg(z) = θ (multi-valued; principal branch Arg(z) ∈ (−π, π])
    Conjugate:          z̄ = x − iy

Key arithmetic identities:
```
z · z̄ = |z|²                     zz̄ = x² + y²
|z₁z₂| = |z₁||z₂|                arg(z₁z₂) = arg(z₁) + arg(z₂)
|z₁ + z₂| ≤ |z₁| + |z₂|         (triangle inequality)
e^{iπ} + 1 = 0                    (Euler's identity)
```

**Geometric view**: multiplication by z = r·e^{iθ} rotates by θ and scales by r. This geometry is why analytic functions are conformal (angle-preserving at non-critical points).

---

## Cauchy-Riemann Equations — Derivation

Write f(z) = u(x,y) + iv(x,y). For f to be complex-differentiable at z₀ = x₀ + iy₀, the limit

    f'(z₀) = lim_{h→0} [f(z₀+h) − f(z₀)] / h

must be the same regardless of how h → 0.

**Approach h → 0 along the real axis** (h = Δx, real):

    f'(z₀) = lim_{Δx→0} [u(x₀+Δx, y₀) − u(x₀,y₀) + i(v(x₀+Δx,y₀) − v(x₀,y₀))] / Δx
           = ∂u/∂x + i·∂v/∂x

**Approach h → 0 along the imaginary axis** (h = iΔy, imaginary):

    f'(z₀) = lim_{Δy→0} [u(x₀, y₀+Δy) − u(x₀,y₀) + i(v(x₀,y₀+Δy) − v(x₀,y₀))] / (iΔy)
           = (1/i)·∂u/∂y + ∂v/∂y
           = −i·∂u/∂y + ∂v/∂y

Setting the two expressions equal:

    ∂u/∂x + i·∂v/∂x = ∂v/∂y − i·∂u/∂y

Equating real and imaginary parts:

```
┌─────────────────────────────────────────────┐
│   CAUCHY-RIEMANN EQUATIONS                  │
│                                             │
│   ∂u/∂x = ∂v/∂y                            │
│   ∂u/∂y = −∂v/∂x                           │
│                                             │
│   (necessary condition for holomorphicity)  │
└─────────────────────────────────────────────┘
```

**Converse** (Goursat-Looman-Menchov): If ∂u/∂x, ∂u/∂y, ∂v/∂x, ∂v/∂y exist and are continuous at z₀ and CR holds, then f is holomorphic at z₀. Continuity of partials matters — just having CR hold pointwise is not enough.

---

## Polar Form of Cauchy-Riemann

For f(z) = u(r,θ) + iv(r,θ) in polar coordinates z = re^{iθ}:

    r·∂u/∂r = ∂v/∂θ
    ∂u/∂θ = −r·∂v/∂r

Useful for functions naturally expressed in polar form: z^n, log z, etc.

---

## Harmonic Conjugates

If f = u + iv is holomorphic, differentiating CR equations:

    ∂²u/∂x² = ∂²v/∂x∂y = ∂²v/∂y∂x = −∂²u/∂y²

    ⟹  ∂²u/∂x² + ∂²u/∂y² = 0   (Laplace equation: ∇²u = 0)

Similarly ∇²v = 0. So:

```
f = u + iv  holomorphic  ⟹  u and v each satisfy Laplace's equation

Converse: Given harmonic u on simply connected domain Ω,
          there exists harmonic conjugate v such that f = u + iv
          is holomorphic on Ω.
          v is unique up to an additive constant.
          v(x,y) = ∫ (∂u/∂x dy − ∂u/∂y dx)  (path-independent by harmonicity)
```

This connection is the foundation for using complex analysis to solve Laplace's equation in 2D, with direct application to electrostatics, heat conduction, and fluid potential flow.

---

## Standard Holomorphic Functions

### Polynomials and Rational Functions

    p(z) = aₙzⁿ + ... + a₁z + a₀    holomorphic everywhere on ℂ
    R(z) = p(z)/q(z)                  holomorphic except at zeros of q

Zeros of q are poles of R. Order of pole at z₀ = order of z₀ as zero of q (assuming p(z₀) ≠ 0).

### Exponential

    e^z = e^{x+iy} = e^x(cos y + i sin y)

Properties:
```
e^{z+w} = e^z · e^w           (group homomorphism ℂ → ℂ*)
|e^z| = e^{Re(z)}
arg(e^z) = Im(z)
e^z = 1  ↔  z = 2πni  for some n ∈ ℤ   (periodic with period 2πi)
```

Holomorphic everywhere (entire function). Note: e^z is periodic in the imaginary direction with period 2πi, unlike e^x which is never periodic.

### Trigonometric and Hyperbolic

Defined via exponential:

    sin z = (e^{iz} − e^{−iz}) / 2i
    cos z = (e^{iz} + e^{−iz}) / 2
    sinh z = (e^z − e^{−z}) / 2
    cosh z = (e^z + e^{−z}) / 2

Relationships: sin(iz) = i·sinh(z),  cos(iz) = cosh(z)

These functions are entire (holomorphic on all of ℂ) and agree with real trig/hyp on the real axis. But unlike their real counterparts, sin z and cos z are **unbounded** — |sin z| can be arbitrarily large for complex z.

### Logarithm

    log z = ln|z| + i·arg(z)

Multi-valued: arg(z) is defined only modulo 2π. The **principal branch** Log(z) takes Arg(z) ∈ (−π, π] and is holomorphic on ℂ \ (−∞, 0] (the plane minus the negative real axis):

    (Log z)' = 1/z    for z ∉ (−∞, 0]

The branch cut along the negative real axis is needed to make Log single-valued. Different choices of branch cut give different single-valued branches of log.

### Power Functions

    z^α = e^{α log z}    for α ∈ ℂ

Multi-valued if α ∉ ℤ. For rational α = p/q, there are q branches. For irrational α, there are infinitely many. The principal branch uses Log:

    z^α = e^{α Log z}    holomorphic on ℂ \ (−∞, 0]

---

## Power Series Representation

A function holomorphic on a disk D(z₀, R) = {|z − z₀| < R} has a unique power series:

    f(z) = Σ_{n=0}^{∞} aₙ(z − z₀)ⁿ,    aₙ = f^(n)(z₀) / n!

The series converges absolutely in D(z₀, R) and diverges outside the *circle of convergence* (radius = distance from z₀ to the nearest singularity of f).

```
CONVERGENCE OF POWER SERIES
                                          singularity
                                              ×
    z₀ ×              convergent            ×
         ╰──────────────────────────────────╯
                       ↑
               radius R = dist(z₀, nearest singularity)

Inside |z − z₀| < R:  absolute and uniform convergence
On |z − z₀| = R:      can converge or diverge (case by case)
Outside:               diverges
```

**Radius from coefficients** (Cauchy-Hadamard formula):
    1/R = limsup_{n→∞} |aₙ|^{1/n}

---

## The Wirtinger Derivatives

Elegant reformulation using the operators:

    ∂/∂z̄ = (1/2)(∂/∂x + i·∂/∂y)
    ∂/∂z  = (1/2)(∂/∂x − i·∂/∂y)

Then the Cauchy-Riemann equations become simply:

    ∂f/∂z̄ = 0    (f is holomorphic ↔ independent of z̄)

This is clean: holomorphic means "depends on z but not on z̄." Thinking of z and z̄ as independent variables (formally, in ℂ²), holomorphic functions live on the "z-direction" only.

---

## Conformal Maps at Non-Critical Points

If f is holomorphic at z₀ and f'(z₀) ≠ 0, then f is **conformal** there: it preserves angles and orientation.

```
CONFORMAL PROPERTY

    Two curves γ₁, γ₂ meeting at z₀ with angle α
         │
         ▼
    f(γ₁), f(γ₂) meet at f(z₀) with the same angle α
    (and same orientation)

Reason: f'(z₀) = |f'(z₀)| e^{iφ} acts on tangent vectors by
         rotation by φ and scaling by |f'(z₀)|
         Same rotation applied to both tangent vectors → angle preserved
```

At **critical points** (f'(z₀) = 0), angles are multiplied by the order of the zero of f'. If f(z) − f(z₀) ≈ c(z − z₀)^k near z₀, angles are multiplied by k.

---

## Examples — Working Through CR

**Example 1**: f(z) = z²
    u = x² − y²,   v = 2xy
    ∂u/∂x = 2x = ∂v/∂y ✓
    ∂u/∂y = −2y = −∂v/∂x ✓
    Holomorphic everywhere, f'(z) = 2z.

**Example 2**: f(z) = z̄ = x − iy
    u = x,   v = −y
    ∂u/∂x = 1,   ∂v/∂y = −1    → 1 ≠ −1: CR fails everywhere
    NOT holomorphic anywhere.

**Example 3**: f(z) = |z|² = x² + y²
    u = x² + y²,   v = 0
    ∂u/∂x = 2x,   ∂v/∂y = 0    → 2x ≠ 0 except at origin
    Holomorphic only at z = 0 (but not in any neighborhood → not analytic there).

**Example 4**: f(z) = e^z
    u = e^x cos y,   v = e^x sin y
    ∂u/∂x = e^x cos y = ∂v/∂y ✓
    ∂u/∂y = −e^x sin y = −∂v/∂x ✓
    Entire function, f'(z) = e^z.

---

## The Goursat Theorem

A key technical point: Goursat proved that the definition of holomorphic does *not* require assuming continuity of the derivative. If the complex limit

    lim_{h→0} [f(z+h) − f(z)] / h

exists at every point of a domain, then f is automatically analytic (has convergent power series). This is much stronger than the real case, where differentiability gives only C¹, not C^∞.

The proof uses a clever argument: approximate the integral ∮_C f dz over any small triangle by zero, using the existence of the complex derivative as a local linear approximation. From ∮ = 0 for triangles, bootstrap to the integral formula, then to power series.

---

## Decision Cheat Sheet

| Question | Test |
|---------|------|
| Is f(z) holomorphic? | Check CR: ∂u/∂x = ∂v/∂y, ∂u/∂y = −∂v/∂x |
| Where does f fail to be holomorphic? | Where CR fails, or partials don't exist |
| What is the radius of convergence? | Cauchy-Hadamard: 1/R = limsup |aₙ|^{1/n} |
| Does a harmonic conjugate exist? | Yes, if domain is simply connected |
| Is f conformal? | Yes, at points where f'(z) ≠ 0 |
| What does f'(z₀) = 0 mean geometrically? | Angles multiplied by order of zero |
| Is f(z) = z̄ holomorphic? | No — CR fails everywhere |

---

## Common Confusion Points

**CR necessary but not sufficient without continuity**: There exist functions where CR equations hold at a single point but the complex derivative does not exist there. The standard example: f(z) = z̄²/z = (x−iy)²/(x+iy) for z ≠ 0, f(0) = 0. This satisfies CR at z = 0 but is not differentiable there.

**"Analytic on a set" vs "analytic at a point"**: A function is analytic on an open set Ω if it is holomorphic at every point of Ω. "Analytic at z₀" means holomorphic in some open disk centered at z₀. Analyticity is an open-set condition.

**Harmonic ≠ holomorphic**: |z|² = x² + y² satisfies ∇²(|z|²) = ∇²(x² + y²) = 2 + 2 = 4 ≠ 0. Not harmonic. But Re(z²) = x² − y² does satisfy Laplace. Harmonic functions are those satisfying ∇²u = 0, and they arise as real or imaginary parts of holomorphic functions.

**e^z is not "the real exponential"**: e^z is periodic with period 2πi. There are infinitely many z with e^z = 1, namely z = 2πni. The real exponential is monotone and injective. The complex exponential maps horizontal strips to sectors.

**Power series can converge outside the stated disk**: The Cauchy-Hadamard formula gives the exact radius. On the boundary circle, behavior varies: the geometric series 1/(1−z) = Σzⁿ diverges everywhere on |z|=1; a different series might converge everywhere or at some points on the boundary.
