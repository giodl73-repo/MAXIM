# Phase Transitions and Critical Phenomena

## The Big Picture

A phase transition is a non-analyticity of the free energy as a function of thermodynamic
variables. First-order transitions have discontinuous first derivatives (latent heat, density
jump); second-order transitions have continuous first derivatives but divergent or discontinuous
second derivatives (heat capacity, susceptibility). Near a second-order critical point, the
system becomes scale-invariant — correlation length diverges, and the system looks the same
at all length scales. This scale invariance is captured by critical exponents that depend only
on a few features (dimensionality, symmetry of the order parameter) — universality.

```
PHASE TRANSITION TAXONOMY
═══════════════════════════════════════════════════════════════════════════════

  FREE ENERGY F(T, P, ...) has a NON-ANALYTICITY at the transition.

  FIRST ORDER (Ehrenfest: first derivative discontinuous):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ∂F/∂T = −S  discontinuous  →  LATENT HEAT Q = T ΔS           │
  │  ∂F/∂P = V   discontinuous  →  DENSITY JUMP Δρ                  │
  │  Order parameter jumps discontinuously at transition            │
  │  Examples: melting, boiling, liquid-gas below critical point    │
  └─────────────────────────────────────────────────────────────────┘

  SECOND ORDER (continuous order parameter, divergent response):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ∂F/∂T = −S  continuous                                         │
  │  ∂²F/∂T² = −C_V/T  diverges or has cusp                       │
  │  Order parameter → 0 continuously at T_c                        │
  │  Correlation length ξ → ∞ at T_c                                │
  │  Examples: ferromagnet (T_c = Curie), superfluid, superconductor│
  └─────────────────────────────────────────────────────────────────┘

  CRITICAL POINT: where first-order line ends and second-order behavior appears.
  Liquid-gas critical point: T_c = 647 K, P_c = 220 atm (water).
  At critical point: ρ_liquid = ρ_gas, meniscus vanishes.
```

---

## Order Parameters

An order parameter is a macroscopic quantity that is zero in the disordered phase and nonzero in the ordered phase.

```
COMMON ORDER PARAMETERS:

  System               Order parameter              Symmetry broken
  ─────────────────────────────────────────────────────────────────
  Ferromagnet          M = ⟨Σᵢ sᵢ⟩ (magnetization) Z₂ (spin flip)
  Antiferromagnet      Staggered magnetization       Translational
  Liquid-gas           ρ_liquid − ρ_gas              —
  Superconductor       ⟨ψ⟩ (complex field)           U(1) phase
  Superfluid           ⟨ψ⟩ (complex field)           U(1) phase
  Liquid crystal       Orientation tensor Q_ij       Rotational O(3)/D_∞h
  Crystal              Density wave ρ_G (Fourier)    Translational+Rotational
  XY model             ⟨e^{iθ}⟩                     U(1) phase
  Heisenberg magnet    Vector M = ⟨S⟩                O(3) rotational

  SYMMETRY BREAKING:
  The high-T phase has the full symmetry of the Hamiltonian.
  The low-T phase spontaneously breaks a symmetry — choosing one
  from a degenerate set of ground states.
```

---

## Mean-Field Theory

Mean-field theory replaces the fluctuating interaction with a field produced by the average:

**Ising mean-field**: Replace sᵢ sⱼ by sᵢ ⟨sⱼ⟩ = sᵢ m (where m = ⟨s⟩).

    H_MF = −(Jz m + h) Σᵢ sᵢ    (z = coordination number, h = external field)

Single-spin problem: sᵢ = ±1 in effective field h_eff = Jzm + h.

Self-consistency equation:

    m = tanh(β h_eff) = tanh(β(Jzm + h))

**At h = 0, near T_c**: Expand tanh for small m:

    m = tanh(βJzm) ≈ βJzm − (βJzm)³/3 + ...
    m(1 − βJz) = −(βJz)³m³/3 + ...

For T > T_c = Jz/k_B: only solution m = 0 (disordered).
For T < T_c: m ≠ 0 solves the equation.

```
MEAN-FIELD ORDER PARAMETER (h=0):
  T > T_c:  m = 0
  T < T_c:  m ≈ ±√(3(1 − T/T_c))   ∝ |T_c − T|^{1/2}

  Exponent β_order = 1/2  (mean-field value)

  SUSCEPTIBILITY (h → 0, T > T_c):
  χ = ∂m/∂h|_{h=0} = 1/(k_B(T−T_c)) ∝ |T − T_c|^{−1}   (Curie-Weiss law)
  Exponent γ = 1  (mean-field value)

  HEAT CAPACITY: jump at T_c (mean-field), C_V ~ |T−T_c|^0 (α=0)
```

**Validity**: Mean-field theory is exact when:
1. Spatial dimension d ≥ d_c (upper critical dimension, d_c = 4 for Ising)
2. Long-range interactions (each spin interacts with many others — Curie-Weiss model)
3. Large coordination number z → ∞

Below d_c, fluctuations dominate near T_c and mean-field exponents are wrong.

---

## Landau Theory

Landau (1937): expand the free energy as a power series in the order parameter m, exploiting symmetry.

**For Ising symmetry** (m → −m under Z₂ flip — no odd powers):

    F(m, T) = F₀(T) + a(T) m² + b(T) m⁴ + c(T) m⁶ + ... − hm

**At equilibrium**: ∂F/∂m = 0, ∂²F/∂m² > 0.

```
LANDAU FREE ENERGY — SECOND ORDER TRANSITION:
  Assume b > 0, a(T) = a₀(T − T_c) (changes sign at T_c):

  T > T_c: a > 0 → minimum at m = 0 (disordered)
  T < T_c: a < 0 → double well → minima at m = ±√(−a/2b) ∝ |T−T_c|^{1/2}

        F(m)                F(m)
         │ T > T_c           │ T < T_c
         │   ∪               │ ∪     ∪
    ─────┼──────────      ───┼────────────
         │              -m*  0  +m*

  This is a spontaneous symmetry breaking bifurcation
  (cf. pitchfork bifurcation in dynamical systems).
```

**For first-order transition**: a(T) > 0 near transition, but b(T) < 0, c(T) > 0.

```
LANDAU FREE ENERGY — FIRST ORDER TRANSITION:
  b < 0: cubic minimum appears BEFORE a changes sign.

        F(m) at T slightly above T*

         │
         │  local min   global min
         │     m=0         m=m*
         ╰───────────────────────
                      m

  Discontinuous jump at T* (latent heat).
  Coexistence of phases in a range of T (meta-stability).
```

**Ginzburg-Landau theory**: Landau with spatial variation of the order parameter:

    F[m(r)] = ∫ d³r [a(T) m² + b m⁴ + c|∇m|² − hm]

The gradient term |∇m|² penalizes spatial variations. Minimizing this functional (Euler-Lagrange) gives the GL equation, which describes domain walls, vortices, and the correlation length ξ.

**Correlation length** from GL theory: ξ = √(c/|a(T)|) ∝ |T − T_c|^{-1/2} (mean-field).

---

## Critical Exponents and Universality

Near T_c, all physical quantities follow power laws:

```
CRITICAL EXPONENTS DEFINED:

  Order parameter:    m ~ |T − T_c|^β         (T < T_c)
  Correlation length: ξ ~ |T − T_c|^{-ν}
  Correlation function: G(r) ~ r^{-(d-2+η)} e^{-r/ξ}  (r << ξ at T_c: ~ r^{-(d-2+η)})
  Susceptibility:     χ ~ |T − T_c|^{-γ}
  Specific heat:      C_V ~ |T − T_c|^{-α}
  Equation of state:  m ~ h^{1/δ}  (T = T_c, varying field h)

  SCALING RELATIONS (thermodynamic consistency):
  α + 2β + γ = 2    (Rushbrooke)
  γ = β(δ − 1)      (Widom)
  γ = ν(2 − η)      (Fisher)
  dν = 2 − α        (hyperscaling, valid for d < d_c)
```

**Universality**: Systems with the same (d, symmetry of order parameter) have identical critical exponents, regardless of microscopic details.

```
UNIVERSALITY CLASSES — CRITICAL EXPONENTS REFERENCE TABLE:

  Class             α       β       γ       ν       η      Examples
  ─────────────────────────────────────────────────────────────────────────
  Mean-field        0       1/2     1       1/2     0      d ≥ 4, any n
  (d ≥ d_c)

  2D Ising (exact)  0(log)  1/8     7/4     1       1/4    Square lattice
                                                           (Onsager 1944)

  3D Ising (n=1)    0.110   0.326   1.237   0.630   0.036  Ferromagnet,
                                                           liquid-gas,
                                                           binary alloy

  3D XY (n=2)      −0.007   0.348   1.316   0.671   0.038  Superfluid ⁴He,
                                                           easy-plane magnet

  3D Heisenberg    −0.115   0.366   1.391   0.707   0.037  Isotropic
  (n=3)                                                     ferromagnet

  Note: 2D Ising β = 1/8 = 0.125 vs 3D Ising β = 0.326 — dimension
  changes exponents dramatically. Mean-field β = 1/2 overestimates order
  in both 2D and 3D. All rows satisfy the scaling relations
  (α + 2β + γ = 2, dν = 2 − α for d < d_c).

  Why same exponents within a class? Near T_c, fluctuations on scale ξ
  dominate. ξ → ∞ means microscopic details (lattice spacing, etc.) are
  irrelevant. Only d and symmetry of the order parameter determine exponents.
```

---

## First-Order Transitions — Latent Heat and Coexistence

At a first-order transition, the free energy has two equal minima. The system must choose one, releasing latent heat in the process.

**Clausius-Clapeyron equation**: slope of coexistence curve in (T, P) space:

    dP/dT = ΔS/ΔV = L/(T ΔV)

where L = T ΔS is the latent heat and ΔV = V_gas − V_liquid.

For liquid-gas transition: ΔV = V_gas ≈ NkT/P (ideal gas), so:

    dP/dT = LP/Nk_BT²    ⟹    P(T) ∝ e^{-L/Nk_BT}    (vapor pressure curve)

**Nucleation**: A metastable phase (superheated liquid, supercooled vapor) must form a nucleus of the new phase to begin the transition. The nucleus has surface energy cost and volume energy gain:

    ΔG(r) = 4πr² σ − (4/3)πr³ |ΔG_bulk|

The nucleus grows only if r > r* = 2σ/|ΔG_bulk| (critical nucleus radius).

---

## The Ising Model and Exact Results

The Ising model is the simplest lattice model with a phase transition. Covered in detail in 07-ISING-MODELS.md; key facts for context:

```
ISING HAMILTONIAN:
  H = −J Σ_{⟨ij⟩} sᵢ sⱼ − h Σᵢ sᵢ    (sᵢ = ±1)

  J > 0: ferromagnetic coupling (parallel spins preferred)
  h: external magnetic field

  1D ISING: no phase transition at T > 0 (Peierls argument shows
            domain walls cost only finite energy = 2J).

  2D ISING: phase transition at T_c = 2J/[k_B ln(1+√2)] ≈ 2.27 J/k_B
            EXACT SOLUTION by Onsager (1944). C_V has logarithmic divergence.
            Exponents: α=0 (log), β=1/8, γ=7/4, ν=1, η=1/4.

  3D ISING: no exact solution. Exponents from conformal bootstrap:
            β ≈ 0.326, γ ≈ 1.237, ν ≈ 0.630.
```

---

## Decision Cheat Sheet

| Question | Answer |
|---------|--------|
| First vs. second order? | Discontinuous vs. continuous order parameter at transition |
| Order parameter for ferromagnet | M = ⟨magnetization⟩, zero for T > T_c |
| Landau: when is transition second-order? | b(T) > 0 near T_c (quadratic well becomes double well) |
| Landau: when is transition first-order? | b(T) < 0 with c > 0 (cubic minima appear discontinuously) |
| Universality class of Ising ferromagnet | d=3 Ising: β≈0.326, γ≈1.237, ν≈0.630 |
| Critical exponent for ξ | ξ ~ |T−T_c|^{-ν} |
| Mean-field critical exponents | β=1/2, γ=1, ν=1/2, α=0 |
| Why universality? | ξ → ∞ at T_c; microscopic details irrelevant at scale ξ |
| Scaling relation | α + 2β + γ = 2 (Rushbrooke) |
| Clausius-Clapeyron | dP/dT = L/(T ΔV) |

---

## Common Confusion Points

**β the critical exponent vs β = 1/kT**: Both symbols are standard in their respective contexts. The critical exponent β describes how the order parameter vanishes: m ~ |T−T_c|^β. The thermodynamic β = 1/k_BT is the inverse temperature. Unfortunately the same letter is standard in both cases. Context determines which is meant.

**Landau theory is mean-field theory**: Landau's free energy expansion implicitly assumes the order parameter is uniform and ignores fluctuations. The gradient term |∇m|² is a minimal extension (Ginzburg-Landau). Full fluctuation effects require renormalization group methods.

**Universality class depends on symmetry of the order parameter, not the Hamiltonian**: The 3D Ising universality class includes liquid-gas critical points, binary mixtures, and uniaxial ferromagnets — very different physical systems that all share the same Z₂ symmetry (order parameter can be ±m) in 3 dimensions.

**Second-order transitions are not "less physical" than first-order**: Both are sharp transitions. Second-order transitions have divergent fluctuations and scale invariance — they are if anything richer physics. Superconductors and superfluids undergo second-order transitions; the phase is fundamentally different from a classical phase transition.

**Ginzburg criterion — when does mean-field break down?** The Ginzburg criterion quantifies how close to T_c fluctuations overwhelm the mean-field order parameter. Compare the fluctuation in m within a correlation volume ξ^d to the mean-field value m_MF:

    Gi = (fluctuation / mean-field)² = (⟨δm²⟩_ξ / m_MF²) ~ (k_BT_c / |a₀|ξ^d) / (|a₀|t/b)

where t = |T − T_c|/T_c. Using ξ ~ t^{-1/2} (mean-field) and m ~ t^{1/2}: Gi ~ t^{(d−4)/2}. Mean-field is self-consistent when Gi << 1, i.e., when t >> t_Gi where t_Gi ~ (b²k_BT_c / a₀² ξ₀^d)^{2/(4−d)}. For d > 4, Gi → 0 always: mean-field is exact. For d < 4, there is a Ginzburg window |t| < t_Gi near T_c where fluctuations dominate and mean-field exponents are wrong. This is the regime where the renormalization group (06-RENORMALIZATION.md) is essential.

**Universality in neural network phase transitions**: The universality framework — same critical exponents from very different microscopic systems — applies beyond condensed matter. Neural networks exhibit sharp phase transitions at the interpolation threshold (where training error drops to zero), and the double descent phenomenon (test error peaks at the interpolation threshold, then decreases again) appears universally across architectures (fully-connected, convolutional, random features). The underlying mechanism is the same: at the critical point, the effective dimension of the model equals the number of constraints (training data), and the critical exponents governing generalization error depend on the universality class (e.g., random matrix ensemble), not on architectural details. The spin glass connection is developed in 09-CONNECTIONS.md.
