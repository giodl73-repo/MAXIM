# Fourier Methods and Separation of Variables

## The Big Picture

Fourier methods convert a PDE into an algebraic or ODE problem by representing the solution
as a superposition of eigenfunctions. The key idea: derivatives become multiplications in
frequency space.

```
+-----------------------------------------------------------------------+
|              FOURIER METHODS LANDSCAPE                                 |
|                                                                       |
|  SEPARATION OF VARIABLES:                                             |
|  u(x,t) = X(x)·T(t)  →  each factor solves an ODE                   |
|  Eigenvalue problem determines the basis functions                    |
|  Works on: rectangles, cylinders, spheres (separable geometries)     |
|                                                                       |
|  FOURIER SERIES (finite domain):                                      |
|  u(x) = Σ c_n φ_n(x)  where φ_n are the eigenfunctions               |
|  Inner product: (f,g) = ∫ f·g dx                                     |
|  Coefficients: c_n = (u, φ_n) / (φ_n, φ_n)                          |
|                                                                       |
|  FOURIER TRANSFORM (infinite domain):                                 |
|  û(k) = ∫_{-∞}^{∞} u(x) e^{−ikx} dx   (spatial → frequency)        |
|  u(x) = 1/(2π) ∫ û(k) e^{ikx} dk      (inverse)                     |
|  Turns ∂/∂x → ×ik;  ∂²/∂x² → ×(−k²)                               |
|                                                                       |
|  LAPLACE TRANSFORM (temporal):                                        |
|  Û(x,s) = ∫₀^∞ u(x,t) e^{−st} dt                                   |
|  Turns ∂/∂t → ×s (after handling IC)                                 |
|  Converts time-evolution PDE → ODE in x                              |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Sturm-Liouville Theory: The Universal Framework

Separation of variables always leads to a Sturm-Liouville eigenvalue problem:

```
  STURM-LIOUVILLE PROBLEM:
  − d/dx [p(x) dy/dx] + q(x)y = λ w(x) y   on [a,b]
  with separated BCs at x=a and x=b.

  Examples:
  • y'' + λy = 0 on [0,L]:  p=1, q=0, w=1  →  λ_n=(nπ/L)², y_n=sin,cos
  • Legendre:  −[(1−x²)y']' = λy on [−1,1]  →  λ_n=n(n+1), y_n=P_n(x)
  • Bessel:    −[xy']' + m²/x·y = λxy on [0,1]  →  y_n=J_m(α_{mn}x)
  • Chebyshev: −[(1−x²)^{1/2}y']' = λ(1−x²)^{−1/2}y  →  T_n, U_n

  SPECTRAL THEOREM (S-L):
  ┌─────────────────────────────────────────────────────────────────┐
  │ If p,q,w are smooth and p,w > 0:                                │
  │ • Eigenvalues λ₁ ≤ λ₂ ≤ λ₃ ≤ ... → +∞ (discrete, real)       │
  │ • Eigenfunctions φ_n are orthogonal: ∫ φ_n φ_m w dx = 0 (n≠m) │
  │ • Completeness: {φ_n} forms a basis for L²_w([a,b])            │
  │ • nth eigenfunction has exactly n−1 zeros in (a,b)              │
  └─────────────────────────────────────────────────────────────────┘

  This guarantees the eigenfunction expansion converges.
```

---

## Fourier Series: Complete Reference

```
  FULL FOURIER SERIES on [−L,L]:
  u(x) = a₀/2 + Σ_{n=1}^∞ [aₙ cos(nπx/L) + bₙ sin(nπx/L)]

  Coefficients:
  aₙ = 1/L ∫_{−L}^L u(x) cos(nπx/L) dx
  bₙ = 1/L ∫_{−L}^L u(x) sin(nπx/L) dx

  COMPLEX FORM:
  u(x) = Σ_{n=−∞}^{∞} cₙ e^{inπx/L}
  cₙ = 1/(2L) ∫_{−L}^L u(x) e^{−inπx/L} dx

  CONVERGENCE:
  Pointwise: converges to u(x) at continuity points; to ½[u(x+)+u(x−)] at jumps.
  L² convergence: Σ|cₙ|² = 1/(2L)∫|u|² dx  (Parseval's theorem).
  Uniform: if u ∈ C¹, series converges uniformly.

  SINE SERIES (odd extension, u(0)=u(L)=0):
  u(x) = Σ bₙ sin(nπx/L),   bₙ = 2/L ∫₀ᴸ u sin(nπx/L) dx

  COSINE SERIES (even extension, u_x(0)=u_x(L)=0):
  u(x) = a₀/2 + Σ aₙ cos(nπx/L),   aₙ = 2/L ∫₀ᴸ u cos(nπx/L) dx
```

---

## Fourier Transform: Properties and Formulas

```
  DEFINITION:
  û(k) = F[u](k) = ∫_{−∞}^∞ u(x) e^{−ikx} dx

  INVERSE:
  u(x) = F⁻¹[û](x) = 1/(2π) ∫_{−∞}^∞ û(k) e^{ikx} dk

  KEY PROPERTIES:
  ┌────────────────────────────────────────────────────────────┐
  │  F[u']         = ik · û(k)                                │
  │  F[u'']        = (ik)² û(k) = −k² û(k)                   │
  │  F[u^{(n)}]    = (ik)ⁿ û(k)                              │
  │  F[xu]         = i (d/dk) û(k)                            │
  │  F[e^{iax}u]   = û(k−a)     (modulation → frequency shift)│
  │  F[u(x−a)]     = e^{−ika} û(k)  (translation → phase shift)│
  │  F[u * v]      = û(k) · v̂(k)   (convolution → product)   │
  │  F[u · v]      = 1/(2π) û * v̂  (product → convolution)  │
  └────────────────────────────────────────────────────────────┘

  PARSEVAL'S THEOREM:
  ∫_{−∞}^∞ |u(x)|² dx = 1/(2π) ∫_{−∞}^∞ |û(k)|² dk

  IMPORTANT TRANSFORMS:
  F[e^{−ax²}] = √(π/a) · e^{−k²/4a}       (Gaussian → Gaussian)
  F[δ(x)]     = 1                           (delta → constant)
  F[1]        = 2π·δ(k)                     (constant → delta)
  F[H(x)e^{−ax}] = 1/(a+ik)  (a>0)         (exponential decay)
```

---

## Solving PDEs with Fourier Transform

### Heat Equation on the Whole Line

```
  u_t = α·u_xx,   u(x,0) = u₀(x)

  Apply F in x:    û_t = α(ik)²û = −αk²û
  This is an ODE in t:  û(k,t) = û₀(k)·e^{−αk²t}

  Invert:  u(x,t) = F⁻¹[û₀(k)·e^{−αk²t}]
         = u₀ * F⁻¹[e^{−αk²t}]
         = u₀ * [1/√(4παt) e^{−x²/4αt}]    (heat kernel K)
         = ∫ u₀(y) K(x−y,t) dy

  Note: e^{−αk²t} → 0 as t→∞ for k≠0 (all modes decay)
        e^{+αk²t} → ∞ (backward heat: Fourier modes blow up)
```

### Wave Equation on the Whole Line

```
  u_tt = c²u_xx,   u(x,0) = u₀, u_t(x,0) = v₀

  Apply F:  û_tt = c²(ik)²û = −c²k²û
  ODE:   û(k,t) = A(k)cos(ckt) + B(k)sin(ckt)
  ICs:   A(k) = û₀(k),  B(k) = v̂₀(k)/(ck)

  û(k,t) = û₀(k)cos(ckt) + v̂₀(k) sin(ckt)/(ck)

  Invert using F[cos(ckt)]→π[δ(x+ct)+δ(x−ct)]:
  u(x,t) = ½[u₀(x+ct)+u₀(x−ct)] + 1/(2c)∫_{x−ct}^{x+ct} v₀(s)ds

  This reproduces d'Alembert's formula — consistent.
```

### Laplace Equation in the Half-Plane

```
  ∇²u = 0 for y > 0,   u(x,0) = g(x)

  Apply F in x:  û_yy − k²û = 0
  ODE solution:  û(k,y) = A(k)e^{ky} + B(k)e^{−ky}

  Boundedness as y→∞: require û→0, so A(k)=0 (if k>0) or B(k)=0 (k<0)
  → û(k,y) = ĝ(k)·e^{−|k|y}

  Invert:  u(x,y) = ∫ g(x') P(x−x',y) dx'
           P(x,y) = F⁻¹[e^{−|k|y}] = y/π(x²+y²)   (Poisson kernel)
```

---

## Separation of Variables: Algorithmic Guide

```
  ALGORITHM FOR SEPARATION OF VARIABLES:

  STEP 1: Identify geometry (rectangular, cylindrical, spherical).

  STEP 2: Assume product form:
    Rectangular:  u = X(x)Y(y)T(t)  or  X(x)Y(y)
    Cylindrical:  u = R(r)Θ(θ)Z(z)T(t)
    Spherical:    u = R(r)Y(θ,φ)T(t)

  STEP 3: Substitute, divide, set equal to separation constant.
    PDE → decoupled ODEs, one per variable.
    Separation constants couple the equations.

  STEP 4: Solve eigenvalue problems first.
    Homogeneous BCs → discrete eigenvalues and eigenfunctions.
    BCs determine which separation constants are allowed.

  STEP 5: Write general solution as eigenfunction expansion.
    u = Σ cₙ (solution for λₙ)

  STEP 6: Apply remaining ICs/BCs to find coefficients cₙ.
    Usually a Fourier or Fourier-Bessel expansion.

  STEP 7: Write series solution and check convergence.
```

### Rectangular: Laplace on a 2D Rectangle

```
  ∇²u = 0 on [0,a]×[0,b], u=0 on three sides, u=g(x) on y=b

  Separation: u = X(x)·Y(y)
    X'' + λX = 0,  X(0)=X(a)=0  →  X_n = sin(nπx/a), λ_n=(nπ/a)²
    Y'' − λY = 0,  Y(0)=0       →  Y_n = sinh(nπy/a)

  Solution: u = Σ cₙ sin(nπx/a) sinh(nπy/a)
  At y=b:   g(x) = Σ cₙ sin(nπx/a) sinh(nπb/a)
            cₙ = 2/(a sinh(nπb/a)) ∫₀ᵃ g(x) sin(nπx/a) dx
```

### Cylindrical: Bessel Functions

```
  LAPLACE IN 2D CYLINDER (Bessel's equation):
  ∇²u = u_rr + 1/r u_r + 1/r² u_θθ = 0

  Separation: u = R(r)·Θ(θ)
    Θ'' + m²Θ = 0  →  Θ_m = cos(mθ), sin(mθ)  (m=0,1,2,...)
    r²R'' + rR' − m²R = 0  →  Bessel's equation for √λ·r

  BESSEL'S EQUATION: r²R'' + rR' + (λr²−m²)R = 0
  Solutions: J_m(√λ r) and Y_m(√λ r)

  J_m = BESSEL FUNCTION OF FIRST KIND (regular at 0)
  Y_m = Bessel of second kind (singular at 0, usually rejected)

  On disk r ≤ a: u finite at r=0 → use J_m only
  Eigenvalues from J_m(√λ a) = 0:  √λ_{mn} = α_{mn}/a
  where α_{mn} = nth zero of J_m

  SOLUTION:
  u(r,θ) = Σ_{m,n} [A_{mn} cos(mθ) + B_{mn} sin(mθ)] J_m(α_{mn}r/a)
```

---

## Spectral Methods (Numerical)

The same eigenfunction expansion idea applied numerically:

```
  SPECTRAL METHOD:
  Approximate u by finite sum:  u_N = Σ_{n=0}^N c_n φ_n(x)

  FOURIER SPECTRAL (periodic):
  φ_n = e^{inx},  approximate in frequency space
  FFT computes the N coefficients in O(N log N) operations
  Convergence: exponentially fast for smooth functions (spectral accuracy)

  CHEBYSHEV SPECTRAL (non-periodic):
  φ_n = T_n(x) (Chebyshev polynomials)
  Gauss-Chebyshev quadrature for coefficients
  Handles endpoints naturally; exponential convergence

  SPHERICAL HARMONIC SPECTRAL:
  u = Σ c_ℓᵐ Y_ℓᵐ(θ,φ)
  Used in: global weather models, geophysics, astrophysics

  vs. FINITE DIFFERENCES: spectral methods give more accuracy
  per degree of freedom for smooth solutions, but struggle
  with discontinuities and complex geometries.
```

---

## Gibbs Phenomenon

```
  When a Fourier series represents a discontinuous function,
  the partial sums exhibit overshoot at the jump:

  f(x) = +1 for 0 < x < π,  −1 for −π < x < 0  (square wave)

  f_N(x) = 4/π [sin(x) + sin(3x)/3 + sin(5x)/5 + ... + sin((2N−1)x)/(2N−1)]

  AT THE JUMP: overshoot ≈ 8.9% of jump height, regardless of N.
  The overshoot doesn't disappear as N→∞ — it just sharpens.

  GIBBS PHENOMENON IS NOT a convergence failure.
  The series DOES converge in L² (Parseval).
  It's a pointwise overshoot at discontinuities.

  REMEDY: Filtering (Lanczos filter, σ-approximation), spectral
  element methods, or using the correct weak/entropy solution.
```

---

## Decision Cheat Sheet

| Domain / Problem | Method | Eigenfunctions |
|-----------------|--------|----------------|
| Rectangle with Dirichlet BCs | Fourier sine series | sin(nπx/L) |
| Rectangle with Neumann BCs | Fourier cosine series | cos(nπx/L) |
| Disk / cylinder | Bessel functions | J_m(α_{mn}r/a) × sin/cos(mθ) |
| Sphere / ball | Spherical harmonics | Y_ℓᵐ(θ,φ) × r^ℓ or r^{−ℓ−1} |
| Whole line (−∞,∞) | Fourier transform | e^{ikx} (continuous) |
| Half-line (0,∞) | Fourier sine/cosine transform | |
| Time-only initial data | Laplace transform | e^{st} |
| Periodic domain | Fourier series | e^{i2πnx/L} |
| Non-periodic, smooth | Chebyshev expansion | T_n(x) |

---

## Common Confusion Points

**"Separation of variables produces an infinite series — does it always converge?"**
If the Sturm-Liouville problem is regular (smooth coefficients, separated BCs), Sturm-Liouville
theory guarantees the eigenfunction expansion converges in L², and often pointwise if the
function is smooth enough. For the standard Fourier series: pointwise convergence at continuity
points, Gibbs phenomenon at jumps.

**"Why does the Fourier transform turn derivatives into multiplications?"**
Because e^{ikx} are eigenfunctions of d/dx: d/dx (e^{ikx}) = ik·e^{ikx}. The derivative
operator acts diagonally in the Fourier basis (eigenfunction expansion). This is the core
of spectral theory: PDE → algebraic equation in the eigenfunction basis.

**"Bessel functions look like decaying oscillations. Are they related to sine/cosine?"**
At large r: J_m(r) ≈ √(2/πr) cos(r − mπ/2 − π/4). Yes — asymptotically they are decaying
oscillations. They are the "natural sines and cosines for radial problems" — separating
Laplace (or wave) equation in cylindrical or spherical coordinates inevitably produces them.
They arise from the radial part of the Sturm-Liouville problem with the cylindrical Laplacian.
