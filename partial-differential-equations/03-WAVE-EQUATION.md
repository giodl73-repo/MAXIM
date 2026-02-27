# Wave Equation and Hyperbolic Systems

## The Big Picture

The wave equation u_tt = c²∇²u is the archetype of **reversible, finite-speed propagation**.
It models acoustics, electromagnetism, seismology, and is the non-relativistic limit of many
field theories. Understanding it deeply gives you the template for all hyperbolic systems.

```
+-----------------------------------------------------------------------+
|              WAVE EQUATION LANDSCAPE                                   |
|                                                                       |
|  1D: u_tt = c²u_xx                     (string vibration, acoustics)  |
|  2D: u_tt = c²(u_xx + u_yy)            (drum membrane, water surface) |
|  3D: u_tt = c²∇²u = c²(u_xx+u_yy+u_zz)(sound, light in vacuum)       |
|                                                                       |
|  SCALAR → SYSTEMS                                                     |
|  Maxwell (EM):   ε₀E_tt = c²∇×(∇×E)   6-component hyperbolic system  |
|  Elasticity:     ρu_tt = ∇·σ(u)        vector wave, two speeds       |
|  MHD:            coupled magneto-hydro   more complex hyperbolic sys.  |
|                                                                       |
|  PROPERTIES                                                           |
|  • Finite propagation speed c                                         |
|  • Energy conserved (no dissipation)                                  |
|  • Singularities in data propagate along characteristics              |
|  • Huygens' principle (dimension-dependent)                           |
|  • Time-reversal symmetry (t → −t)                                    |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## 1D Wave Equation: Complete Solution

```
  u_tt = c²u_xx,    u(x,0) = u₀(x),    u_t(x,0) = v₀(x)

  CHARACTERISTICS:  two families
      ξ = x + ct  (left-moving)
      η = x − ct  (right-moving)

  In (ξ,η) coordinates:  u_ξη = 0
  General solution:       u = F(ξ) + G(η) = F(x+ct) + G(x−ct)

  Apply initial conditions to find F and G:
      u(x,0) = F(x) + G(x) = u₀(x)
      u_t(x,0) = cF'(x) − cG'(x) = v₀(x)

  Integrate second equation: F(x) − G(x) = (1/c)∫₀ˣ v₀(s) ds + const

  D'ALEMBERT'S FORMULA:
  ┌─────────────────────────────────────────────────────────────────┐
  │  u(x,t) = ½[u₀(x+ct) + u₀(x−ct)] + 1/(2c) ∫_{x−ct}^{x+ct} v₀(s)ds│
  └─────────────────────────────────────────────────────────────────┘

  DOMAIN OF DEPENDENCE of (x,t):
      [x−ct, x+ct]  on the initial line t=0.
  Only the initial data in this interval affects u(x,t).
  Points outside: CAUSALLY DISCONNECTED from (x,t).
```

---

## Energy and Conservation

```
  ENERGY DENSITY:  e = ½(u_t² + c²u_x²)  [kinetic + potential]

  ENERGY FLUX:     j = −c²u_t u_x

  CONSERVATION LAW:  ∂e/∂t + ∂j/∂x = 0   (energy flux balance)

  TOTAL ENERGY:  E(t) = ∫_{−∞}^{∞} e(x,t) dx = CONSTANT (if u₀, v₀ ∈ L²)

  This conservation means the wave equation is TIME-REVERSIBLE.
  Run t → −t: wave equation is unchanged (unlike heat equation).
  A wave packet moving right becomes a wave packet moving left.
```

---

## Domains of Dependence and Influence

```
  x-t PLANE PICTURE:

  t
  ↑
  |             CONE OF
  |           INFLUENCE
  |          of (x₀,t₀)
  t₀-----+        ·(x₀,t₀)
  |       \  /            /\
  |        \/            /  \
  |        (x₀,0)       /    \
  |                     (x₀,t₀)
  |                    ↑CONE OF
  |                     DEPENDENCE
  +------------------------→ x
      x₀−ct₀  x₀   x₀+ct₀

  DOMAIN OF DEPENDENCE of (x₀,t₀):
    D(x₀,t₀) = {(x,0) : |x−x₀| ≤ ct₀}
    Changing u₀ outside this interval → no effect at (x₀,t₀).

  DOMAIN OF INFLUENCE of (x₀,0):
    I(x₀) = {(x,t) : |x−x₀| ≤ ct, t≥0}
    A disturbance at x₀ can only influence inside this forward cone.

  CAUSALITY = FINITE DOMAIN OF INFLUENCE.
  This is exactly relativistic causality when c = speed of light.
```

---

## 3D Wave Equation: Kirchhoff's Formula

In 3D, the solution to the wave equation with initial data is given by averages over
expanding spheres — a beautiful result with no 2D analogue:

```
  3D WAVE EQUATION:  u_tt = c²∇²u  in R³

  KIRCHHOFF'S FORMULA:
  u(x,t) = ∂/∂t [t · M_{ct}(u₀)(x)] + t · M_{ct}(v₀)(x)

  where M_r(f)(x) = average of f on sphere of radius r centered at x:
        M_r(f)(x) = 1/(4πr²) ∫_{|y|=r} f(x+y) dσ(y)

  Equivalently:
  u(x,t) = 1/(4πc²t²) ∫_{|y-x|=ct} [t·v₀(y) + u₀(y) + ∇u₀(y)·(y-x)] dσ(y)

  KEY FACT (Huygens' Principle in 3D):
  u(x,t) depends ONLY on data on the sphere |y−x| = ct.
  NOT on data inside the sphere.

  A sharp initial pulse → sharp wavefront in 3D.
  Echo: distant signal arrives and leaves cleanly.
```

### Huygens' Principle: Dimension Dependence

```
  ODD DIMENSIONS (1D, 3D, 5D,...):  STRONG Huygens' principle holds.
    Signal has a sharp front AND sharp back.
    After the wavefront passes, signal returns to zero.
    ┌────────────────────────────────────────────────────────┐
    │  3D: u(x,t) depends only on data on sphere |y−x|=ct   │
    │  (thin shell, not ball)                                │
    └────────────────────────────────────────────────────────┘

  EVEN DIMENSIONS (2D, 4D,...):  WEAK Huygens' principle.
    Signal has a sharp front but diffuse back.
    2D: u(x,t) depends on data in DISK |y−x| ≤ ct.
    A "splash" in a pond sends a wave that diffuses behind it.

  PRACTICAL CONSEQUENCE:
  Sound in 3D: you hear a gun shot cleanly (sharp front and back).
  Sound in a 2D waveguide: you hear a reverberant tail.
```

---

## Separation of Variables: Standing Waves

On a finite domain with Dirichlet BCs:

```
  u_tt = c²u_xx,  u(0,t) = u(L,t) = 0,  u(x,0) = u₀(x),  u_t(x,0) = v₀(x)

  STEP 1: Separation.  u(x,t) = X(x)T(t)
          X(x)T''(t) = c²X''(x)T(t)
          T''/c²T = X''/X = −λ  (separation constant)

  STEP 2: X eigenvalue problem.
          X'' + λX = 0,  X(0) = X(L) = 0
          Eigenvalues:   λ_n = (nπ/L)²
          Eigenfunctions: X_n(x) = sin(nπx/L)

  STEP 3: T equation.
          T'' + c²λ_n T = 0  →  T_n(t) = A_n cos(ω_n t) + B_n sin(ω_n t)
          where ω_n = cnπ/L  (angular frequency of nth mode)

  STEP 4: General solution.
          u(x,t) = Σ_{n=1}^∞ [A_n cos(ω_n t) + B_n sin(ω_n t)] sin(nπx/L)

  STEP 5: Apply ICs (Fourier series coefficients):
          A_n = 2/L ∫₀ᴸ u₀(x) sin(nπx/L) dx
          B_n = 2/(Lω_n) ∫₀ᴸ v₀(x) sin(nπx/L) dx

  NORMAL MODES: each term is a standing wave with frequency ω_n = cnπ/L.
  Fundamental frequency ω₁ = cπ/L, overtones at integer multiples.
  Musical string: higher modes give harmonics.
```

---

## Reflection and Transmission

When a wave hits a boundary between two media:

```
  BOUNDARY at x=0:  c₁ (x<0) and c₂ (x>0)

  INCIDENT wave u_i = f(x − c₁t) (right-moving)
  REFLECTED wave u_r = g(x + c₁t) (left-moving)
  TRANSMITTED wave u_t = h(x − c₂t) (right-moving)

  MATCHING CONDITIONS at x=0:
  (1) Continuity of u:       f(−c₁t) + g(c₁t) = h(−c₂t)
  (2) Continuity of ρc·u_t: ρ₁c₁[−f'(−c₁t) + g'(c₁t)] = ρ₂c₂[−h'(−c₂t)]

  IMPEDANCES: Z_i = ρ_i c_i

  REFLECTION COEFFICIENT: R = (Z₁−Z₂)/(Z₁+Z₂)
  TRANSMISSION COEFFICIENT: T = 2Z₁/(Z₁+Z₂)

  Check: if Z₁ = Z₂ (matched impedances), R=0, T=1 — perfect transmission.
  If Z₂ → ∞ (rigid wall): R = −1 — perfect reflection, sign flip.
  If Z₂ → 0 (free end): R = +1 — perfect reflection, same sign.
```

---

## Dispersive Waves

Not all waves travel at the same speed. Dispersive waves have frequency-dependent speed:

```
  LINEAR WAVE with dispersion:  u_tt + α²u_xxxx = 0  (beam vibration)

  Plane wave ansatz:  u = e^{i(kx − ωt)}
  Dispersion relation: ω² = α²k⁴  →  ω = αk²  (phase velocity ω/k = αk)

  Different wavelengths travel at different speeds.
  Initial packet spreads out (disperses).

  Compare with non-dispersive (wave eq.): ω² = c²k²  →  ω/k = c
  All wavelengths travel at same speed c.
  Initial packet travels without deformation.

  GROUP VELOCITY: v_g = dω/dk
  PHASE VELOCITY: v_p = ω/k

  Non-dispersive: v_g = v_p = c.
  Dispersive: v_g ≠ v_p in general.
  Energy travels at group velocity.

  KdV is dispersive + nonlinear: balance gives SOLITONS (see below).
```

---

## Maxwell's Equations as a Hyperbolic System

```
  MAXWELL IN VACUUM:
  ∂B/∂t = −∇×E
  ∂E/∂t = c²∇×B
  ∇·E = 0
  ∇·B = 0

  This is a SYMMETRIC HYPERBOLIC SYSTEM for (E,B) ∈ R⁶.
  Characteristic speeds: 0 (static modes) and ±c (light speed).

  From Maxwell → wave equations for E and B separately:
  ∂²E/∂t² = c²∇²E  (using ∇×(∇×E) = ∇(∇·E) − ∇²E = −∇²E)

  So each component of E (and B) satisfies the 3D wave equation.
  Light is a solution to the wave equation. That's it.

  TRANSVERSE NATURE:
  The constraints ∇·E = 0, ∇·B = 0 (no magnetic monopoles)
  restrict to transverse waves (E,B perpendicular to propagation direction k).
  Plane wave: E ⊥ k, B ⊥ k, E ⊥ B.
```

---

## Nonlinear Wave Equations and Solitons

### KdV: The Canonical Soliton Equation

```
  KdV: u_t + 6u·u_x + u_xxx = 0

  DISPERSION (from linear part u_t + u_xxx = 0):
  Plane wave e^{i(kx−ωt)}: dispersion relation ω = k³  (strongly dispersive)
  Short waves are faster than long waves.

  NONLINEARITY (from 6u·u_x):
  Steepens waves. Without dispersion: shocks form.

  BALANCE: For a certain relationship, steepening and spreading cancel.
  → SOLITON: a wave that propagates without change of shape.

  ONE-SOLITON:  u(x,t) = 2κ² sech²(κ(x − 4κ²t))
  Speed:  v = 4κ². Taller solitons move faster.

  COLLISION OF SOLITONS:
  Two solitons of different speeds collide, pass through each other,
  and emerge unchanged — except for a phase shift.
  This is extraordinary: nonlinear waves that behave like particles.

  MATHEMATICAL DEPTH: KdV is completely integrable (Lax pair,
  inverse scattering transform). Infinitely many conservation laws.
```

---

<!-- @editor[content/P2]: No coverage of quantum field theory wave equations. The Klein-Gordon equation (∂²φ/∂t² − c²∇²φ + (mc/ℏ)²φ = 0) and the Dirac equation are relativistic wave equations central to QFT and directly in scope for this learner. Gravitational waves (linearized GR: □h_μν = 0 in the transverse-traceless gauge) are also absent. These are the equations that make the wave equation significant in modern physics, not just acoustics and strings. -->

<!-- @editor[content/P2]: No numerical methods coverage for hyperbolic equations in this file. The wave equation file covers only analytical solutions (d'Alembert, Kirchhoff, separation of variables). Leapfrog time integration, dispersion analysis of numerical wave equations, and the CFL condition for explicit hyperbolic schemes belong here or as a forward reference to 09-NUMERICAL-PDES.md. The learner needs this connection to see how the mathematical properties (finite speed, energy conservation) constrain numerical choices. -->

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| 1D wave general solution? | F(x+ct) + G(x−ct) (d'Alembert) |
| Solution given ICs? | d'Alembert formula |
| 3D wave solution? | Kirchhoff formula (spherical averages) |
| Why is Huygens sharp in 3D but not 2D? | 3D: only sphere surface contributes; 2D: full disk contributes |
| Energy conserved? | Yes: ∫[u_t² + c²|∇u|²] dx = constant |
| Standing waves on [0,L]? | Separation of variables; ω_n = cnπ/L |
| Dispersive vs. non-dispersive? | Group velocity = phase velocity → non-dispersive |
| What makes a soliton? | Balance of nonlinear steepening and dispersive spreading |
| When do waves reflect? | At impedance mismatch Z₁ ≠ Z₂ |

---

## Common Confusion Points

**"The wave equation is hyperbolic, so it has characteristics. Can information really travel
at exactly c, never faster?"**
Yes — for the linear wave equation in homogeneous media, the domain of dependence is exactly
the light cone. This is the mathematical content of special relativity: the wave equation for
the electromagnetic potential is Lorentz-invariant, and the characteristic speed is c.

**"What's the difference between group velocity and phase velocity?"**
Phase velocity v_p = ω/k is the speed of the wavecrest (constant phase surface).
Group velocity v_g = dω/dk is the speed of the envelope / energy packet.
For non-dispersive (ω = ck): v_g = v_p = c.
For deep water waves (ω = √(gk)): v_p = √(g/k), v_g = ½√(g/k) — energy moves at half
the phase speed. This is why wave crests seem to appear at the back of a ship's wake and
disappear at the front.

**"Huygens' principle says a disturbance in 3D leaves no 'afterglow'. Is that really true?"**
Yes, for the scalar wave equation in flat 3D space. The sharp-back property is Huygens'
principle in its strong form. It fails in: curved spacetime, waveguides, inhomogeneous media,
and (deliberately) for 2D membranes. The mathematical statement: the fundamental solution
(Green's function) of the 3D wave equation is supported on the light cone, not inside it.
