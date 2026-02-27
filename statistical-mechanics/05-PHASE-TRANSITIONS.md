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
  │  ∂F/∂P = V   discontinuous  →  DENSITY JUMP Δρ                 │
  │  Order parameter jumps discontinuously at transition            │
  │  Examples: melting, boiling, liquid-gas below critical point    │
  └─────────────────────────────────────────────────────────────────┘

  SECOND ORDER (continuous order parameter, divergent response):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ∂F/∂T = −S  continuous                                        │
  │  ∂²F/∂T² = −C_V/T  diverges or has cusp                       │
  │  Order parameter → 0 continuously at T_c                       │
  │  Correlation length ξ → ∞ at T_c                               │
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

<!-- @editor[content/P2]: The universality table lists exponents for Ising, XY, and Heisenberg universality classes but is missing the mean-field row for d=3 comparison alongside exact 3D values, and is also missing a column for 2D Ising exact values for comparison (β=1/8 vs 0.326 illustrates how dramatically dimension changes exponents). Adding a "2D Ising (exact)" column would make this the reference table the learner reaches for, not just a static list. -->

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
UNIVERSALITY CLASSES — CRITICAL EXPONENTS:

  Class              d=3 exponents          Examples
  ──────────────────────────────────────────────────────────────────
  Ising (n=1)        α=0.110, β=0.326,      Ferromagnet, liquid-gas,
                     γ=1.237, ν=0.630       binary alloy, ⁴He
  XY (n=2)           α=−0.007, β=0.348,     Superfluid transition
                     γ=1.316, ν=0.671       (n=2 complex order param)
  Heisenberg (n=3)   α=−0.115, β=0.366,     Isotropic ferromagnet
                     γ=1.391, ν=0.707
  Mean-field         α=0, β=1/2,            d ≥ 4, long-range interactions
  (all classes, d≥d_c) γ=1, ν=1/2

  Why same exponents? Near T_c, fluctuations on scale ξ dominate.
  ξ → ∞ means the microscopic details (lattice spacing, etc.) don't matter.
  Only d and symmetry of the order parameter determine the exponents.
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

<!-- @editor[content/P2]: Missing: the Ginzburg criterion — the condition for when mean-field theory actually fails and fluctuations take over. The file says "Below d_c, fluctuations dominate" but doesn't give the Ginzburg condition (ξ^d × (fluctuations) ~ (mean-field value)) that tells you *quantitatively* how close to T_c mean-field breaks down. This is the bridge between the Landau free energy section and the renormalization group — exactly what this learner would want to see. -->

<!-- @editor[bridge/P2]: No connection to the ML "generalization transition" or "double descent" phenomenon. The universality framework (same critical exponents from very different microscopic systems) is exactly the insight needed to understand why neural network phase transitions (interpolation threshold, jamming) are universal across architectures. The 09-CONNECTIONS.md file covers this lightly but the core insight belongs here, at the point where universality is first explained in depth. -->
