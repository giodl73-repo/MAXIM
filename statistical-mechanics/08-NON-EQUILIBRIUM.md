# Non-Equilibrium Statistical Mechanics

## The Big Picture

Equilibrium statistical mechanics is about systems that have reached their steady state.
Non-equilibrium statistical mechanics is about everything else: transport, fluctuations,
relaxation, driven systems. The key bridge between equilibrium and non-equilibrium is the
fluctuation-dissipation theorem (FDT): the same microscopic fluctuations that cause Brownian
motion also cause dissipation (viscosity, resistance). The Jarzynski equality and Crooks
relation extend thermodynamics to arbitrary non-equilibrium processes, proving exact equalities
(not just inequalities) involving work and free energy differences.

```
NON-EQUILIBRIUM STATISTICAL MECHANICS — LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  EQUILIBRIUM                        NON-EQUILIBRIUM
  S = k ln Ω                         dS/dt ≥ 0 (second law inequality)
  F = −kT ln Z                       F is not the relevant potential
  Boltzmann distribution             Time-dependent distributions P(x,t)

  NEAR-EQUILIBRIUM (linear response):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Fluctuation-Dissipation Theorem:                                │
  │  Response to perturbation = equilibrium fluctuations             │
  │  Kubo formula: χ(ω) = ∫ e^{iωt} ⟨[A(t),B(0)]⟩ dt              │
  │  Einstein: D = k_BT/γ  (diffusion = mobility × temperature)      │
  └──────────────────────────────────────────────────────────────────┘

  FAR FROM EQUILIBRIUM:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Jarzynski equality: ⟨e^{-βW}⟩ = e^{-βΔF}                      │
  │  Crooks relation:    P_F(W)/P_R(−W) = e^{β(W−ΔF)}              │
  │  Valid for ANY process, however fast or far from equilibrium     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Brownian Motion and the Langevin Equation

**Einstein (1905)**: A pollen grain in water is jostled by random molecular impacts. The mean-square displacement:

    ⟨x²(t)⟩ = 2Dt    where D = k_BT/γ (Einstein relation)

γ is the drag coefficient (Stokes: γ = 6πηr for a sphere of radius r in fluid of viscosity η).

**Langevin equation** (Langevin 1908): The equation of motion for a particle subject to drag and random force:

    m ẍ = −γẋ + F(x) + η(t)

where η(t) is a random (Gaussian white noise) force:

    ⟨η(t)⟩ = 0
    ⟨η(t) η(t')⟩ = 2γk_BT δ(t − t')    ← fluctuation-dissipation relation

The amplitude of the noise (2γk_BT) is fixed by temperature and damping — they come from the SAME microscopic origin (molecular collisions).

**Overdamped Langevin** (m → 0, γ large — typical for colloidal particles):

    γẋ = F(x) + η(t)    ⟹    ẋ = −(1/γ)∇U(x) + √(2D) ξ(t)

where ξ(t) = η(t)/√(2γ²D) is normalized white noise.

```
LANGEVIN EQUATION — UNITS AND INTERPRETATION:

  F(x) = −∇U(x):  deterministic restoring force from potential U
  η(t):            thermal noise — models all the molecular kicks
  γ:               friction (drag) — same coefficient as in noise amplitude
  D = k_BT/γ:      diffusion constant (Einstein relation)

  At long times:
  ⟨x²⟩ = 2Dt          (diffusion)
  ⟨v²⟩ = k_BT/m       (equipartition)
  Velocity autocorrelation: ⟨v(0)v(t)⟩ = (k_BT/m) e^{-γt/m}
```

---

## The Fokker-Planck Equation

The Langevin equation describes individual trajectories. The Fokker-Planck equation (FPE) describes the time evolution of the probability density P(x, t).

**Derivation**: The overdamped Langevin equation ẋ = −(1/γ)∂U/∂x + ξ(t) implies:

    ∂P/∂t = −∂J/∂x    (continuity equation)

where the probability flux J:

    J = −(1/γ)(∂U/∂x)P − D ∂P/∂x    (drift + diffusion)

**Fokker-Planck equation** (1D overdamped):

    ∂P/∂t = ∂/∂x [(1/γ)(∂U/∂x) P + D ∂P/∂x]
           = ∂/∂x [D e^{−βU(x)} ∂/∂x (e^{βU(x)} P)]

```
STEADY-STATE SOLUTION:
  At steady state: ∂P/∂t = 0 → J = const.
  For a confining potential (U → ∞ as |x| → ∞): J = 0 at steady state.
  Then P_ss(x) ∝ e^{−βU(x)}  ← Boltzmann distribution!

  FPE preserves the Boltzmann distribution as the steady state.
  This is the consistency check: the Langevin/FPE dynamics must relax
  to the correct equilibrium distribution.
```

**General multidimensional FPE**:

    ∂P/∂t = −∇·(A P) + ∇·(D ∇P)    = −∇·J

where A is the drift vector and D is the diffusion matrix. For thermal equilibrium:
D = k_BT × (mobility tensor).

**Connection to the Schrödinger equation**: The FPE with U can be rewritten as:

    ∂ψ/∂t = −H_FP ψ    where H_FP is a Hermitian operator (after a gauge transformation P → e^{-βU/2} ψ)

This is a Euclidean (imaginary-time) Schrödinger equation. The relaxation to equilibrium is governed by the gap of H_FP (difference between ground state eigenvalue 0 and the first excited eigenvalue).

---

## Fluctuation-Dissipation Theorem

The FDT is one of the deepest results in near-equilibrium physics: linear response of a system to an external perturbation equals the equilibrium fluctuations of the conjugate variable.

**Setup**: System in equilibrium at temperature T. Apply a small perturbation h(t) that couples to observable A:

    H → H − h(t) A

The mean response ⟨A⟩(t):

    ⟨A(t)⟩ = ⟨A⟩_0 + ∫_{-∞}^t χ(t − t') h(t') dt'    (linear response)

where χ(t − t') is the **response function** (retarded Green's function).

**FDT** (Callen-Welton form):

    χ''(ω) = (ω/2k_BT) S_{AA}(ω)    where S_{AA}(ω) = ∫ dt e^{iωt} ⟨A(t)A(0)⟩

Here χ''(ω) is the imaginary part of the response (dissipation) and S_{AA}(ω) is the spectral density of equilibrium fluctuations.

```
PHYSICAL MEANING:
  ┌──────────────────────────────────────────────────────────────┐
  │  The dissipation when you shake a system (χ''(ω))           │
  │  is proportional to the system's equilibrium fluctuations   │
  │  at the same frequency (S_{AA}(ω)).                         │
  │                                                              │
  │  Same physics: a resistor dissipates electrical energy      │
  │  AND generates Johnson-Nyquist thermal noise.               │
  │  They are related: S_V(ω) = 4k_BT Re[Z(ω)]                 │
  │  (Nyquist theorem: noise voltage spectral density ∝ T × R)  │
  └──────────────────────────────────────────────────────────────┘

  CONSEQUENCES:
  Einstein relation:    D = k_BT / γ  (diffusion from mobility)
  Nyquist noise:        ⟨V²⟩ = 4k_BTR Δf  (thermal noise in resistor R)
  Brownian motion:      ⟨x²⟩ = 2Dt
  Kramers-Kronig:       Re[χ(ω)] determined by Im[χ(ω)] (causality)
```

**Kubo formula** (general FDT for quantum systems):

    χ(t) = (i/ℏ) θ(t) ⟨[A(t), A(0)]⟩_eq    (retarded commutator)

This relates the linear response to an equilibrium time-correlation function — entirely within equilibrium statistical mechanics, but gives non-equilibrium transport coefficients.

---

## Linear Response and Transport Coefficients

The Kubo formula gives transport coefficients as equilibrium time-correlation functions:

```
KUBO FORMULAS FOR TRANSPORT:

  ELECTRICAL CONDUCTIVITY (σ):
  σ(ω) = (1/kTV) ∫₀^∞ dt e^{iωt} ⟨J(t)·J(0)⟩
  DC conductivity: σ = lim_{ω→0} σ(ω) = (1/kTV) ∫₀^∞ dt ⟨J(t)·J(0)⟩

  VISCOSITY (η):
  η = (V/kT) ∫₀^∞ dt ⟨σ_{xy}(t) σ_{xy}(0)⟩
  (pressure tensor autocorrelation)

  THERMAL CONDUCTIVITY (κ):
  κ = (V/kT²) ∫₀^∞ dt ⟨J_Q(t)·J_Q(0)⟩
  (heat current autocorrelation)

  DIFFUSION COEFFICIENT:
  D = (1/3) ∫₀^∞ dt ⟨v(t)·v(0)⟩   (velocity autocorrelation)

  These are GREEN-KUBO RELATIONS.
  All transport coefficients are equilibrium time-correlation functions.
  This is deep: dissipation (irreversible, macroscopic) emerges from
  reversible microscopic correlations.
```

---

## Jarzynski Equality

Classical result (1997, Jarzynski): relates non-equilibrium work to equilibrium free energy differences.

**Setup**: System initially in equilibrium at temperature T and parameter λ₀ (e.g., a spring constant, external field). Perform ANY process that takes λ: λ₀ → λ₁ in time τ, measuring the work W done.

**Jarzynski equality**:

    ⟨e^{-βW}⟩ = e^{-βΔF}    where ΔF = F(λ₁) − F(λ₀)

The average is over all realizations of the (possibly irreversible) process.

**Proof sketch**: For a system in contact with a heat bath:

    ⟨e^{-βW}⟩ = ⟨e^{-β(W−Q)}⟩ e^{-βQ}    ... via Boltzmann weight ...    = e^{-βΔF}

The key is that e^{-βW} samples the rare trajectories where work is less than ΔF (which Jensen's inequality tells us are rare).

```
CONSEQUENCES:

  Jensen's inequality: ⟨e^{-βW}⟩ ≥ e^{-β⟨W⟩}  combined with Jarzynski:
  e^{-β⟨W⟩} ≤ ⟨e^{-βW}⟩ = e^{-βΔF}
  ⟹  ⟨W⟩ ≥ ΔF   ← Second law (irreversible work ≥ free energy change)

  Jarzynski STRENGTHENS the second law:
  Second law: ⟨W⟩ ≥ ΔF  (inequality)
  Jarzynski:  ⟨e^{-βW}⟩ = e^{-βΔF}  (exact equality, for ANY process)

  APPLICATIONS:
  - Free energy calculation from non-equilibrium pulling experiments
  - Single-molecule biophysics (AFM, optical tweezers)
  - Fast free energy methods in drug design (non-equilibrium alchemical calculations)
```

**Crooks fluctuation theorem** (Crooks 1999):

    P_F(W) / P_R(−W) = e^{β(W − ΔF)}

where P_F is the work distribution for forward process and P_R for the time-reversed process. The two distributions cross at W = ΔF. This provides both a derivation of Jarzynski and a direct method for measuring ΔF (from the crossing point).

---

## Stochastic Thermodynamics

<!-- @editor[content/P2]: The stochastic thermodynamics section defines trajectory-level work, heat, and entropy production correctly but does not cover the Seifert integral fluctuation theorem (⟨e^{-σ}⟩ = 1, where σ is total entropy production). This is both the generalization of Jarzynski and the most general statement of the second law from stochastic thermodynamics. A one-equation statement with the physical interpretation (the ratio of forward to reverse trajectory probabilities is e^σ) would complete the section's logical arc. -->

Stochastic thermodynamics extends classical thermodynamics to the level of individual trajectories.

**For a single overdamped trajectory x(t)** between times 0 and t:

    Work:                W = ∫₀^t ∂H/∂λ × λ̇ dt'    (change in Hamiltonian due to driving)
    Heat dissipated:     Q = ∫₀^t F(x)·ẋ dt' = ΔU − W    (first law)
    Entropy production:  σ = −ΔS_system + Q/T ≥ 0    (second law)

These quantities are well-defined for individual trajectories — not just averages.

**Entropy production along a trajectory**:

    σ[x(t)] = ln(P_F[x(t)] / P_R[x̃(t)])

where P_F is the probability of the forward trajectory and P_R of the time-reversed trajectory. This gives a microscopic definition of irreversibility.

---

## Master Equation Approach

For discrete-state Markov processes (e.g., chemical reactions, ion channels):

**Master equation**:

    dP_n/dt = Σ_{m≠n} [W_{nm} P_m − W_{mn} P_n]

where W_{nm} is the rate of transition from state m to state n.

**Detailed balance** (equilibrium condition):

    W_{nm} P_m^{eq} = W_{mn} P_n^{eq}    for all m, n

This means the probability flux is zero for every pair — time-reversal symmetric.

**Non-equilibrium steady state (NESS)**: When detailed balance is broken (e.g., external driving), the system maintains a non-zero current:

    J_{nm} = W_{nm} P_m − W_{mn} P_n ≠ 0

Entropy is produced at rate dS/dt = (k_B/2) Σ_{mn} J_{nm} ln(J_{nm}/J_{mn}) ≥ 0.

---

## Boltzmann Transport Equation

<!-- @editor[content/P2]: The Boltzmann transport equation section correctly states the equation and the H-theorem but doesn't connect to the modern applications this learner would care about: the BTE is the starting point for drift-diffusion equations in semiconductor physics (the Drude model and its quantum corrections), and for the phonon Boltzmann equation that governs heat transport in nanostructures. More relevantly for this learner's calibration, the linearized BTE gives the kinetic theory expression for viscosity, conductivity, and diffusion — the Onsager reciprocal relations that relate these transport coefficients to each other. A sentence on the Onsager relations would close the loop between this section and the Kubo formula section above. -->

For gases far from equilibrium, the Boltzmann transport equation governs the single-particle distribution function f(r, p, t):

    ∂f/∂t + v·∇_r f + F·∇_p f = (∂f/∂t)_collisions

The left side is free streaming; the right side is the collision integral:

    (∂f/∂t)_coll = ∫ [f(p₁')f(p₂') − f(p₁)f(p₂)] × σ(Ω) |v₁−v₂| d²Ω d³p₂

**H-theorem**: Boltzmann's H function:

    H = ∫ d³r d³p f ln f

satisfies dH/dt ≤ 0, approaching its minimum at equilibrium (Maxwell-Boltzmann distribution). This established the microscopic basis for the second law (with the caveats about the molecular chaos assumption discussed in 01-FOUNDATIONS.md).

---

## Decision Cheat Sheet

| Need to... | Tool |
|-----------|------|
| Model Brownian particle | Langevin: mẍ = −γẋ + F + η(t) |
| Time evolution of probability density | Fokker-Planck: ∂P/∂t = ∇·(D∇P − AP) |
| Relate noise to dissipation | FDT: ⟨η(t)η(t')⟩ = 2γk_BT δ(t−t') |
| Compute diffusion coefficient | D = k_BT/γ (Einstein) or D = ∫⟨v(0)v(t)⟩dt |
| Electrical conductivity | Kubo: σ = (1/kTV) ∫⟨J(t)J(0)⟩ dt |
| Free energy from non-eq. work | Jarzynski: ⟨e^{-βW}⟩ = e^{-βΔF} |
| Measure ΔF from work distributions | Crooks: P_F(W)/P_R(−W) = e^{β(W−ΔF)} |
| Second law from Jarzynski | Jensen + Jarzynski ⟹ ⟨W⟩ ≥ ΔF |
| Discrete-state non-equilibrium | Master equation + entropy production rate |

---

## Common Confusion Points

**The FDT holds only near equilibrium — but "near equilibrium" is not small fluctuations**: The FDT holds for linear response, meaning the perturbation h(t) is small enough that second-order terms in h are negligible. The equilibrium state itself can be highly fluctuating. FDT breaks down for strong drives, not for large equilibrium fluctuations.

**Jarzynski applies to irreversible processes, not near-equilibrium**: Jarzynski is exact for ANY process, arbitrarily far from equilibrium. The practical challenge is that ⟨e^{-βW}⟩ is dominated by rare trajectories where W < ΔF — these are exponentially unlikely but exponentially large. For very fast processes, the estimator has large variance and requires many samples.

**The Fokker-Planck and Langevin equations are equivalent descriptions**: Langevin gives individual trajectory realizations; FPE gives the ensemble probability density. Both encode the same physics. The FPE is an Itô stochastic PDE and requires care about the interpretation of the noise (Itô vs Stratonovich conventions matter when the diffusion coefficient depends on x).

**Entropy production is defined for trajectories, not just equilibrium states**: Stochastic thermodynamics defines entropy production along individual trajectories. The ensemble average of trajectory entropy production equals the thermodynamic entropy production, but individual trajectories can violate the second law. The Crooks relation quantifies how probable such violations are.

<!-- @editor[content/P2]: Missing: diffusion models as stochastic processes — the learner calibration explicitly lists "diffusion models as stochastic processes" as a target bridge. Score-based generative models (Song & Ermon) and DDPM (Ho et al.) are exactly forward/reverse stochastic differential equations: the forward process is Langevin diffusion (add noise, destroy signal), and the reverse process learns to reverse the Fokker-Planck flow. The Fokker-Planck and Langevin equations of this file are the exact mathematical foundation. A brief subsection connecting these would be the highest-value addition to this file for this learner. -->
