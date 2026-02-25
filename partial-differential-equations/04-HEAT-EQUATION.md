# Heat Equation and Parabolic Systems

## The Big Picture

The heat equation u_t = α∇²u is the archetype of **irreversible, diffusive evolution**.
It models heat conduction, mass diffusion, Brownian motion, option pricing, and is the
imaginary-time version of the Schrödinger equation.

```
+-----------------------------------------------------------------------+
|              HEAT EQUATION LANDSCAPE                                   |
|                                                                       |
|  FORMS:                                                               |
|  u_t = α∇²u          (heat / diffusion, α = diffusivity)             |
|  u_t = α∇²u + f      (with source f)                                  |
|  u_t = ∇·(D(x)∇u)   (variable diffusivity D)                        |
|  u_t = ∇·(D(u)∇u)   (nonlinear diffusion)                            |
|  iℏψ_t = −(ℏ²/2m)∇²ψ + Vψ   (Schrödinger = i × heat)               |
|  V_t + ½σ²S²V_SS + rSV_S − rV = 0  (Black-Scholes)                  |
|                                                                       |
|  PROPERTIES:                                                          |
|  • Infinite propagation speed (instantaneous awareness)               |
|  • Immediate regularization (rough → smooth in any ε > 0 time)        |
|  • Irreversible (entropy increases; backward problem ill-posed)        |
|  • Gaussian kernel (the fundamental solution)                          |
|  • Maximum principle (no interior extrema)                             |
|  • Energy dissipation (‖u‖_L² decreases)                             |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## The Fundamental Solution (Heat Kernel)

The heat kernel K(x,t) is the solution starting from a point mass at the origin:

```
  PROBLEM:   u_t = α·u_xx  on R,  u(x,0) = δ(x)  (Dirac delta)

  SOLUTION:  K(x,t) = 1/√(4παt) · exp(−x²/4αt)

  In n dimensions:  K(x,t) = (4παt)^{−n/2} · exp(−|x|²/4αt)

  PROPERTIES OF K:
  ┌──────────────────────────────────────────────────────────┐
  │ ∫ K(x,t) dx = 1  for all t > 0  (mass conservation)    │
  │ K(x,t) > 0  for all x, t>0  (strict positivity)        │
  │ K(x,t) → δ(x) as t → 0+                                │
  │ K(x,t) is a Gaussian: mean 0, variance 2αt              │
  │ K(x,t) → 0 as t → ∞ (spreads to zero)                  │
  └──────────────────────────────────────────────────────────┘

  SOLUTION TO IVP:
  u(x,t) = ∫ K(x−y,t) u₀(y) dy = (K(·,t) * u₀)(x)
  This is CONVOLUTION with the heat kernel.

  SCALING SYMMETRY: K(λx, λ²t) = λ^{−1} K(x,t)
  The heat equation is invariant under x → λx, t → λ²t.
  This diffusive scaling x ~ √t is everywhere in probability theory.
```

---

## Physical Derivation: Fourier's Law + Continuity

```
  FOURIER'S LAW:  heat flux q = −k∇T
  (heat flows from hot to cold; flux proportional to gradient)

  ENERGY CONSERVATION:
  ρc·∂T/∂t = −∇·q + Q  (density × heat capacity × rate = divergence of flux + source)

  SUBSTITUTING:
  ρc·∂T/∂t = ∇·(k∇T) + Q

  CONSTANT k:
  ∂T/∂t = (k/ρc)∇²T + Q/ρc = α∇²T + f

  where α = k/(ρc) is the THERMAL DIFFUSIVITY.

  DIMENSIONAL ANALYSIS:
  [α] = m²/s    (same units as kinematic viscosity ν = μ/ρ)
  [K(x,t)] = m^{−1}   (in 1D)
  Diffusion length scale: L ~ √(αt)  (characteristic spreading distance)
```

---

## Separation of Variables: Finite Domain

On [0,L] with Dirichlet BCs:

```
  u_t = α·u_xx,  u(0,t) = u(L,t) = 0,  u(x,0) = u₀(x)

  STEP 1: u(x,t) = X(x)T(t)
          T'/αT = X''/X = −λ  (must be constant)

  STEP 2: X eigenvalue problem
          X'' + λX = 0,  X(0) = X(L) = 0
          λ_n = (nπ/L)²,  X_n = sin(nπx/L)

  STEP 3: T equation
          T' + αλ_n T = 0  →  T_n(t) = e^{−αλ_n t}

  STEP 4: Solution
          u(x,t) = Σ_{n=1}^∞ b_n · e^{−α(nπ/L)²t} · sin(nπx/L)

          b_n = 2/L ∫₀ᴸ u₀(x) sin(nπx/L) dx  (Fourier sine coefficients)

  KEY OBSERVATION: Each mode decays exponentially with rate α(nπ/L)².
  HIGH MODES DECAY FASTEST.

  Long-time behavior: u ≈ b₁ · e^{−α(π/L)²t} · sin(πx/L)
  The solution approaches zero dominated by the slowest-decaying fundamental mode.
```

---

## Smoothing Effect

The heat equation instantly smooths any L² initial data:

```
  If u₀ ∈ L²(R) (any square-integrable function — could be rough):

  Then u(x,t) = (K(·,t) * u₀)(x) ∈ C∞(R)  for any t > 0.

  Proof sketch: K(x,t) = 1/√(4παt) e^{−x²/4αt} is C∞ for t>0,
  and convolution with a C∞ function yields a C∞ function.

  FOURIER PERSPECTIVE:
  û(k,t) = K̂(k,t) · û₀(k) = e^{−αk²t} · û₀(k)

  The Gaussian e^{−αk²t} kills all high frequencies (large k) instantly.
  Even if û₀ has polynomially growing high-frequency content,
  multiplying by e^{−αk²t} makes everything decay faster than any polynomial.
  → Infinite differentiability for t > 0.

  BACKWARD HEAT: undo the e^{−αk²t} factor by multiplying by e^{+αk²t}.
  For large k, this blows up exponentially. Hence ill-posedness.
```

---

## Maximum and Comparison Principles

```
  WEAK MAXIMUM PRINCIPLE:

  If u_t ≤ α∇²u in Q_T = Ω × (0,T), then
  max_{Q_T} u = max_Γ u
  where Γ = (Ω × {0}) ∪ (∂Ω × [0,T]) is the parabolic boundary.

  PHYSICAL MEANING:
  Temperature cannot exceed its maximum on the initial time-slice
  or the spatial boundary at any intermediate time.
  Interior local hot spots cannot spontaneously appear.

  COROLLARIES:
  • Uniqueness: two solutions with same BCs/ICs are identical.
  • Comparison: if u₀ ≤ v₀ and boundary data of u ≤ v, then u ≤ v everywhere.
  • Non-negativity: if u₀ ≥ 0 and BCs ≥ 0, then u(x,t) ≥ 0 for all t>0.

  STRONG MAXIMUM PRINCIPLE:
  If u achieves its maximum at any interior point (x₀,t₀) with t₀ > 0,
  then u is constant in Ω × [0,t₀].
  (Extremum in interior forces everything to be constant.)
```

---

## Long-Time Behavior and Spectral Theory

The long-time asymptotics are controlled by the lowest eigenvalue:

```
  For the heat equation on bounded domain Ω with Dirichlet BCs:
  u_t = α∇²u,  u|_{∂Ω} = 0

  Eigenvalue problem:  −∇²φ = λφ in Ω,  φ|_{∂Ω} = 0
  Spectrum: 0 < λ₁ < λ₂ ≤ λ₃ ≤ ... → ∞

  SOLUTION:  u(x,t) = Σ_n c_n e^{−αλ_n t} φ_n(x)

  LONG TIME:  u(x,t) ≈ c₁ e^{−αλ₁ t} φ₁(x)   (if c₁ ≠ 0)

  DECAY RATE: set by first eigenvalue λ₁ = (π/L)² in 1D.
  In general: λ₁ grows as 1/L² — larger domains diffuse more slowly.

  WEYL'S LAW (counting eigenvalues):
  N(λ) = #{n: λ_n ≤ λ} ~ C_n |Ω| λ^{n/2}   as λ → ∞
  The eigenvalue distribution encodes the volume of the domain.
  "Can you hear the shape of a drum?" (Kac, 1966 — partially answered by
  Gordon-Webb-Wolpert 1992: you cannot in general)
```

---

## Nonlinear Diffusion

```
  POROUS MEDIUM EQUATION:  u_t = ∇·(uᵐ ∇u) = Δ(u^{m+1}/(m+1))  (m>0)

  Models: gas flow in porous rock, groundwater, crowd dynamics.

  KEY DIFFERENCE from linear heat equation:
  • Has FINITE SPEED OF PROPAGATION (unlike linear heat)
  • If u₀ ≥ 0 with compact support, the support grows at finite speed
  • BARENBLATT SIMILARITY SOLUTION:
    u(x,t) = t^{−α} [C − k|x|²t^{−2β}]_+^{1/m}
    (+ means take positive part; support is a growing ball)

  FAST DIFFUSION (m < 1):  faster spreading, extinction in finite time
  SLOW DIFFUSION (m > 1):  finite speed of propagation

  P-LAPLACIAN: u_t = ∇·(|∇u|^{p−2}∇u)
  Models: non-Newtonian fluids, image processing (total variation flow at p→1).
```

---

## Black-Scholes Equation (Finance Application)

```
  The Black-Scholes PDE for option pricing:
  V_t + ½σ²S²V_SS + rSV_S − rV = 0

  where V(S,t) = option value, S = stock price, σ = volatility, r = interest rate.

  CHANGE OF VARIABLES:  S = e^x,  τ = T−t,  V = e^{αx+βτ} u
  (with α, β chosen to simplify)

  → Becomes the HEAT EQUATION:  u_τ = ½σ² u_xx

  SOLUTION via heat kernel:
  V(S,t) = e^{−r(T−t)} · E_Q[payoff(S_T) | S_t = S]
  (Expected value under risk-neutral measure Q)

  The fundamental solution of Black-Scholes is the lognormal distribution.
  This is why Black-Scholes is analytically tractable: it reduces to
  the heat equation, which we can solve exactly.

  PATH-DEPENDENCE:
  American options, barrier options → free-boundary problems
  (Stefan problem for the heat equation).
```

---

## Parabolic Systems: Reaction-Diffusion

```
  REACTION-DIFFUSION:  u_t = D∇²u + f(u)

  Single species, bistable:  u_t = u_xx + u(1−u)(u−a)  (0 < a < 1)
  TRAVELING WAVE SOLUTIONS:  u(x,t) = U(x − st)  (wave speed s)
  Models: nerve impulses (FitzHugh-Nagumo), combustion fronts.

  TURING INSTABILITY (two-species):
  [u_t]   [d_u  0] [u_xx]   [f(u,v)]
  [v_t] = [ 0  d_v][v_xx] + [g(u,v)]

  Homogeneous state (ū,v̄) stable to uniform perturbations.
  With diffusion: can be UNSTABLE (diffusion-driven instability).
  → Spatial patterns form spontaneously.
  Turing (1952): mechanism for biological pattern formation
  (stripes on zebra, spots on leopard).

  Key: activator-inhibitor dynamics + inhibitor diffuses much faster.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Fundamental solution of heat equation? | K(x,t) = (4παt)^{−n/2} e^{−|x|²/4αt} (Gaussian) |
| Characteristic length scale at time t? | L ~ √(αt) (diffusive scaling) |
| Separation of variables gives what? | Exponentially decaying Fourier modes |
| Long-time dominant behavior? | Lowest eigenmode, decay rate e^{−αλ₁t} |
| Why is backward heat ill-posed? | Gaussian → modes grow as e^{αk²T} when reversed |
| What is the maximum principle for heat? | Max/min achieved on parabolic boundary (t=0 or ∂Ω) |
| Does heat equation preserve positivity? | Yes — non-negative initial data stays non-negative |
| How does Black-Scholes relate to heat? | Change of variables transforms B-S exactly to heat equation |
| What is diffusion-driven instability? | Turing: two-species RD can form patterns from uniform state |

---

## Common Confusion Points

**"If the heat equation has infinite propagation speed, doesn't that violate relativity?"**
Yes — the classical heat equation is non-relativistic. The Cattaneo (or hyperbolic heat)
equation adds a relaxation term: τu_tt + u_t = α∇²u, making propagation finite. For most
practical purposes the difference is negligible (thermal relaxation time τ is ~femtoseconds
in metals), but it matters in ultrafast laser physics and cosmological applications.

**"The heat kernel is Gaussian. Is that related to the Central Limit Theorem?"**
Directly. Brownian motion is the limit of a random walk; the heat equation governs the
probability density of Brownian motion. The CLT says the sum of i.i.d. random variables
converges to Gaussian — this is exactly the heat kernel's spreading being Gaussian, and the
semigroup property K(·,t)*K(·,s) = K(·,t+s) corresponds to independent increments.

**"Why do higher eigenmodes decay faster?"**
Eigenvalues λ_n ~ n²(π/L)² grow like n². The decay rate e^{−αλ_n t} ~ e^{−αn²π²t/L²}
grows exponentially in n. Physically: short-wavelength temperature variations have steep
gradients → large Fourier heat flux → rapid equilibration. Long-wavelength modes survive.
This is why warming up a room takes minutes (λ₁ ~ (π/L)² with L~3m, α~2×10⁻⁵) while a
centimeter-scale metal cube equilibrates in seconds.
