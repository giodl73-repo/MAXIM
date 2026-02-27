# Turbulence: Models and Structure

## The Big Picture

Turbulence is the unsolved problem of classical physics. Richard Feynman called it "the most important unsolved problem of classical physics." It is the irregular, chaotic, three-dimensional, vortical motion that occurs at high Reynolds numbers. It is not random — it is fully deterministic (governed by N-S) but chaotic (sensitive to initial conditions). Its key features: energy cascades from large scales to small scales; dissipation occurs only at the smallest scales (Kolmogorov scale); statistical descriptions (RANS, LES) are required for practical use.

```
TURBULENCE — CONCEPTUAL MAP
═══════════════════════════════════════════════════════════════════════════════

  WHAT TURBULENCE IS:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Irregular, chaotic, deterministic (N-S solution at high Re)        │
  │  3D (vortex stretching requires 3D — 2D "turbulence" is different)  │
  │  Multi-scale (eddies from meters to millimeters simultaneously)     │
  │  Dissipative (converts KE to heat at small scales)                  │
  │  Diffusive (turbulent mixing >> molecular diffusion)                │
  └──────────────────────────────────────────────────────────────────────┘

  KOLMOGOROV ENERGY CASCADE:
  Large scales (energy input)                                            Energy in
  ─────────────────────────────────────────────────────────────────── ↓
  L_integral ~ 0.1 m   (large eddies, most energy)
                ↓ inertial cascade (scale-by-scale energy transfer)
                ↓ E(k) ~ k^{-5/3}   (Kolmogorov spectrum, k = wavenumber)
                ↓
  η ~ 1 mm     (Kolmogorov scale — viscosity stops the cascade)        ↓ Energy dissipated
  ─────────────────────────────────────────────────────────────────── as heat
```

---

## Reynolds Decomposition and RANS

The most common approach to turbulence: decompose velocity into mean + fluctuation.

**Reynolds decomposition**: u = ⟨u⟩ + u'

where ⟨u⟩ is the time-averaged velocity and u' is the turbulent fluctuation.

By definition: ⟨u'⟩ = 0 but ⟨u'u'⟩ ≠ 0 (fluctuations are zero-mean but have nonzero variance).

**RANS equations** (Reynolds-Averaged Navier-Stokes): substitute decomposition into N-S, time-average:

    ρ(⟨u_j⟩ ∂⟨u_i⟩/∂x_j) = −∂⟨p⟩/∂x_i + ∂/∂x_j[μ ∂⟨u_i⟩/∂x_j − ρ⟨u_i'u_j'⟩]

The new term **−ρ⟨u_i'u_j'⟩ = τᵢⱼ_R** is the **Reynolds stress tensor**.

```
REYNOLDS STRESS TENSOR:
  τᵢⱼ_R = −ρ⟨u_i'u_j'⟩

  3×3 symmetric tensor:
  [⟨u'u'⟩  ⟨u'v'⟩  ⟨u'w'⟩]
  [⟨v'u'⟩  ⟨v'v'⟩  ⟨v'w'⟩]
  [⟨w'u'⟩  ⟨w'v'⟩  ⟨w'w'⟩]

  Diagonal: turbulent normal stresses (= turbulent kinetic energy)
  Off-diagonal: turbulent shear stresses (cause mixing)

  PROBLEM: 6 new unknowns, no new equations → CLOSURE PROBLEM
```

**The closure problem**: RANS adds 6 new unknowns (Reynolds stresses) but no new equations. We need a turbulence model to close the system.

---

## Turbulence Models (RANS)

### Eddy Viscosity Models

**Boussinesq hypothesis**: Reynolds stresses are proportional to mean strain rate (like viscous stress but with turbulent "eddy viscosity" ν_T >> ν):

    −⟨u_i'u_j'⟩ = ν_T (∂⟨u_i⟩/∂x_j + ∂⟨u_j⟩/∂x_i) − (2/3)k δᵢⱼ

where k = (1/2)⟨u_i'u_i'⟩ is the turbulent kinetic energy.

### Zero-Equation (Mixing Length) Model

Prandtl's mixing length: ν_T = l² |∂u/∂y|

where l = κy (near a wall, κ = 0.41). This crude model works well for flows without separation.

### k-ε Model (Two-Equation)

Most widely used in engineering:

    Dk/Dt = ∂/∂x_j[(ν + ν_T/σ_k) ∂k/∂x_j] + P_k − ε
    Dε/Dt = ∂/∂x_j[(ν + ν_T/σ_ε) ∂ε/∂x_j] + C₁ε(ε/k)P_k − C₂ε(ε²/k)

where:
- k = turbulent kinetic energy
- ε = turbulent dissipation rate
- ν_T = C_μ k²/ε (eddy viscosity from k and ε)
- P_k = production = ν_T |∂u_i/∂x_j|² (production by mean shear)
- C_μ = 0.09, C₁ε = 1.44, C₂ε = 1.92, σ_k = 1.0, σ_ε = 1.3 (empirical constants)

```
k-ε MODEL CAPABILITIES:
  Good for:   Attached flows, jets, wakes, simple shear
  Poor for:   Separated flows, strong curvature, rotating flows,
              adverse pressure gradients, reattachment
```

### k-ω Model (Wilcox)

Replace ε with ω = ε/k (specific dissipation rate). Better near walls, better for adverse pressure gradient flows. Used in k-ω SST (Menter), the default model in much aerospace CFD.

### Reynolds Stress Models (RSM)

Directly solve transport equations for all 6 Reynolds stress components. More accurate but computationally expensive and numerically stiff. Used for strongly anisotropic flows (rotating, buoyancy-driven).

---

## Kolmogorov Theory (K41)

Kolmogorov's 1941 theory is the most important theoretical result in turbulence.

**Assumptions**:
1. At sufficiently small scales, turbulence is locally isotropic and homogeneous
2. The statistics at small scales depend only on ε (energy dissipation rate) and ν (kinematic viscosity)
3. In the inertial range, statistics depend only on ε (not ν — ν not yet relevant)

**Kolmogorov scales** (where viscosity stops the cascade):

    Kolmogorov length:  η = (ν³/ε)^{1/4}    ~ 0.1–1 mm in typical flows
    Kolmogorov time:    τ_η = (ν/ε)^{1/2}
    Kolmogorov velocity: u_η = (νε)^{1/4}

At scale η: Re_η = u_η η/ν = 1 (Reynolds number at the Kolmogorov scale is of order 1 — viscosity and inertia balance).

**Scale separation** (ratio of integral scale L to Kolmogorov scale η):

    L/η ~ Re^{3/4}

At Re = 10⁶: L/η ~ 10^{4.5} ≈ 30,000 — so turbulent flows span ~5 orders of magnitude in length scale. This is why DNS (direct numerical simulation) is so expensive.

**Kolmogorov energy spectrum** (K41 scaling):

    E(k) ~ ε^{2/3} k^{-5/3}    (inertial range)

where k is the wavenumber (1/length). The famous -5/3 power law was confirmed experimentally and is one of the best-verified predictions in physics.

```
TURBULENT ENERGY SPECTRUM:

  E(k)
  (energy   ↑
  per unit   │  energy-containing range
  wavenumber)│  (large eddies)
             │\
             │ \
             │  \  k^{-5/3} inertial range
             │   \_______
             │           \_____
             │                 \___  dissipation range
             └──────────────────────── k (wavenumber, 1/m)
             k_L            k_η
            (integral scale)  (Kolmogorov scale)

  Region            Scale          Physics
  ─────────────────────────────────────────
  Large eddies       L             energy input from mean flow
  Inertial range     L > l > η    energy cascade, E ~ k^{-5/3}
  Dissipation        η            viscosity converts KE to heat
```

---

## Turbulent Kinetic Energy Budget

Transport equation for k = (1/2)⟨u'²+v'²+w'²⟩:

    Dk/Dt = P − ε + Transport

    Production:    P = −⟨u_i'u_j'⟩ ∂U_i/∂x_j    (mean flow → turbulence)
    Dissipation:   ε = ν⟨(∂u_i'/∂x_j)²⟩            (small scales → heat)
    Transport:     diffusion + pressure-velocity correlation

**Production = dissipation** in equilibrium (log layer, fully developed flow): P ≈ ε. The energy extracted from the mean flow exactly replenishes what viscosity dissipates.

**At the wall**: P and ε both large; there is a near-balance but not exact.

**In free shear layers** (jets, wakes): P > ε in cores; ε > P in outer regions.

---

## Direct Numerical Simulation (DNS) and LES

### DNS (Direct Numerical Simulation)

Resolve all scales from L down to η. No turbulence model needed.

**Grid requirement**: N³ gridpoints where N ~ L/η ~ Re^{3/4}

**Cost**: N³ × (L/η)/(u_η η) timesteps ~ Re^{9/4} × Re^{1/2} ∼ Re^{11/4}

At Re = 10⁴: N³ ~ 10⁹, total ~ 10¹⁰ operations — feasible on supercomputer.
At Re = 10⁶: cost increases by (10²)^{11/4} ~ 10^{5.5} → 3×10¹⁵ — impossible today.

DNS is a research tool for low-Re flows and fundamental turbulence physics. The Re^{11/4} cost scaling means DNS runs are MPI-first, GPU-optimized, and use the same domain decomposition + halo exchange pattern as distributed ML training — partition the 3D grid, compute local derivatives, exchange boundary data with neighbors each timestep, all-reduce for global statistics.

### LES (Large Eddy Simulation)

Resolve large eddies; model subgrid scales (SGS).

**Filter**: separate resolved scales (> Δ filter width) from subgrid scales (< Δ).

**LES equations**: same as N-S but with SGS stress tensor τᵢⱼ^{SGS} to model.

**Smagorinsky model** (simplest SGS): ν_T = (C_s Δ)² |S̄| (S̄ = filtered strain rate)

**Cost**: intermediate between DNS and RANS. Grows like Re^{1.8} approximately.

```
SIMULATION METHOD COMPARISON:
  Method    Resolved    Modeled      Cost          Accuracy
  ──────────────────────────────────────────────────────────
  DNS       all scales  nothing      Re^{11/4}    exact (for N-S)
  LES       L >> l > Δ  l < Δ        Re^{1.8}    good, Δ-dependent
  RANS      mean only   all turb.    cheap        model-dependent
  hybrid    outer BL    inner BL     moderate     RANS near wall
  (DES,DDES)  (LES)    (RANS)
```

---

## Turbulence Structure — Coherent Structures

Turbulence is not purely random — it contains recurring organized structures:

**Near-wall (y⁺ < 50)**:
- Streaks: elongated alternating high/low speed regions (λz⁺ ~ 100)
- Quasi-streamwise vortices: paired, generate ejections and sweeps (burst events)
- Hairpin vortices (at higher Re)

**Free shear layers (jets, mixing layers)**:
- Kelvin-Helmholtz rolls at the outer layer
- Brown-Roshko large structures at moderate Re
- Fine-scale turbulence overlaid on large-scale organization

**Detection methods**: Proper Orthogonal Decomposition (POD = SVD of the snapshot matrix, extracting the energetically dominant spatial modes), Dynamic Mode Decomposition (DMD = eigendecomposition of the best-fit linear operator approximating the nonlinear dynamics — the data-driven Koopman operator), Q-criterion (vortex identification), lambda_2-criterion.

---

## Turbulent Transport: Why Turbulence Matters

For species/heat transport in turbulent flow:

    D⟨c⟩/Dt = ∂/∂x_j[(D + D_T) ∂⟨c⟩/∂x_j]

where D = molecular diffusivity, D_T = turbulent diffusivity >> D.

Turbulent Prandtl/Schmidt numbers:
    Pr_T = ν_T/α_T ≈ 0.7–0.9  (momentum / heat diffusivity ratio)
    Sc_T = ν_T/D_T ≈ 0.7–0.9  (momentum / mass diffusivity ratio)

**Practical consequence**: Turbulent heat transfer coefficients are 10–100× larger than laminar. This is why turbulence is exploited in heat exchangers, turbine cooling, and chemical reactors.

---

## Decision Cheat Sheet

| Situation | Approach |
|----------|---------|
| Engineering prediction of turbulent flow | RANS with k-ε or k-ω SST |
| Adverse pressure gradient, separation | k-ω SST or RSM; k-ε will fail |
| Turbulent heat transfer coefficient | Nu ~ Re^{0.8}Pr^{0.4} (Dittus-Boelter, turbulent pipe) |
| Estimate Kolmogorov scale | η = (ν³/ε)^{1/4}; need ε from experiment/RANS |
| High-fidelity turbulence prediction | LES (Re < 10⁶) or DNS (Re < 10⁴) |
| Energy spectrum slope | E(k) ~ k^{-5/3} in inertial range |
| Scale of turbulent structures | L/η ~ Re^{3/4} — rapidly grows with Re |

---

## Common Confusion Points

**Turbulence is not random**: Turbulence is deterministic (governed by N-S) but chaotic. It looks random statistically, but each realization is fully determined by initial conditions. The apparent randomness arises from extreme sensitivity to initial conditions (positive Lyapunov exponents).

**RANS computes mean quantities, not instantaneous**: A RANS simulation gives ⟨u⟩, not u. The turbulence is entirely in the model (k, ε, Reynolds stresses). LES gives instantaneous large-scale u with modeled small scales. DNS gives fully instantaneous u.

**k-ε fails near walls**: The standard k-ε model assumes local equilibrium (P = ε), which breaks down in the viscous sublayer. Near-wall corrections (wall functions or low-Re modifications) are required. This is why y⁺ placement matters in CFD grids.

**The -5/3 spectrum is for the inertial range**: Outside the inertial range (below Kolmogorov scale or above the integral scale), the spectrum falls off differently. The k^{-5/3} scaling is not universal — it requires a wide inertial range, which needs high Re.

**2D turbulence is qualitatively different from 3D**: In 2D, there is no vortex stretching term (**ω**·∇)**v** = 0 because vorticity is perpendicular to the plane. Energy cascades UPWARD (to larger scales) in 2D turbulence. Geophysical flows (ocean, atmosphere, which are thin and quasi-2D) exhibit inverse energy cascade — large coherent vortices emerge rather than fragmenting.
