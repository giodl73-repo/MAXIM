# Stochastic Biology — Noise, Langevin Equation, and Fluctuation Theorems

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│             STOCHASTIC PROCESSES IN BIOLOGY LANDSCAPE                    │
│                                                                            │
│  WHY STOCHASTICITY MATTERS:                                              │
│  Cell volume ~10⁻¹⁵ L → low copy numbers                                 │
│  Typical transcription factor: ~10-1000 molecules per cell               │
│  Transcription: 1-2 copies of each gene → discrete, bursty events        │
│  Single-molecule reactions: Poisson statistics, not continuous flows     │
│                                                                            │
│  MATHEMATICAL FRAMEWORKS:                                                  │
│  ─────────────────────────────────────────────────────────────────────── │
│  Langevin equation:  mẍ = F_det - γẋ + ξ(t)    (trajectory level)        │
│  Fokker-Planck eq:   ∂P/∂t = -∂(FP)/∂x + D∂²P/∂x²  (density level)     │
│  Master equation:    dPₙ/dt = Σ [W(n|m)Pₘ - W(m|n)Pₙ]  (discrete)      │
│  Birth-death process: gene expression, protein synthesis/degradation     │
│                                                                            │
│  KEY RESULTS:                                                              │
│  Fluctuation-dissipation theorem: noise ↔ dissipation are linked         │
│  Jarzynski equality: ⟨exp(-βW)⟩ = exp(-βΔF)  (non-eq → eq)             │
│  Crooks fluctuation theorem: P(W)/P(-W) = exp(β(W-ΔF))                   │
│  Transcriptional bursting: protein count CV² = 1/⟨n⟩ + b/(1+kf/kb)     │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — Why Noise Matters in Small Systems

### The Scale of Biological Fluctuations

```
  Volume of E. coli: ~10⁻¹⁵ L = 1 femtoliter
  1 nM concentration = 1 molecule per femtoliter (Avogadro's number check:
    1 nM × 10⁻¹⁵ L × 6×10²³ mol⁻¹ = 6×10⁻⁴ molecules → <1 molecule)
  1 molecule in E. coli: ~1.6 nM effective concentration

  Typical gene expression in E. coli:
    mRNA:     1-50 molecules per cell
    Protein: 100-50,000 molecules per cell

  For Poisson-distributed counts with mean ⟨n⟩:
    Variance: Var(n) = ⟨n⟩
    CV = σ/⟨n⟩ = 1/sqrt(⟨n⟩)

    ⟨n⟩ = 1:    CV = 100%  → huge fluctuations
    ⟨n⟩ = 10:   CV = 32%
    ⟨n⟩ = 100:  CV = 10%
    ⟨n⟩ = 10⁶:  CV = 0.1%  → classical deterministic limit
```

Below ~1000 molecules, fluctuations are biologically significant. Many
regulatory proteins in cells operate in this regime. This is not a failure
of regulation — it is exploited for stochastic differentiation and bet-hedging.

---

## Section 2 — The Langevin Equation

### Derivation and Physical Content

For a colloidal particle (protein, motor, vesicle) in aqueous solution:

```
  m ẍ = F_det(x) - γẋ + ξ(t)

  m:       mass
  ẍ:       acceleration
  F_det(x): deterministic force (potential gradient, applied force)
  γ:       friction coefficient = 6πηr (Stokes, sphere radius r, viscosity η)
  ξ(t):    Gaussian white noise (thermal force)

  Statistical properties of ξ(t):
    ⟨ξ(t)⟩ = 0                       (zero mean)
    ⟨ξ(t)ξ(t')⟩ = 2γk_BT δ(t-t')   (fluctuation-dissipation theorem)

  The δ(t-t') means: uncorrelated across time
  The 2γk_BT prefactor: couples noise strength to dissipation (see FDT below)
```

### Overdamped Limit

At the nanoscale, inertia is negligible. The Reynolds number Re = ρvL/η:

```
  For a protein (r = 5 nm) moving at v = 1 nm/ns in water:
    Re = (1000 kg/m³)(10⁻⁹ m/ns)(5×10⁻⁹ m) / (10⁻³ Pa·s)
       = 10⁻⁶  << 1

  Inertial relaxation time: τ_i = m/γ ≈ 10⁻¹³ s

  For t >> τ_i (always true for biological processes):
  Overdamped Langevin equation:
    γẋ = F_det(x) + ξ(t)

  Or equivalently:
    ẋ = F_det(x)/γ + √(2D) η(t)   where D = k_BT/γ (Einstein relation)
    η(t) = unit-variance Gaussian white noise
```

### Potential Well Dynamics

For a particle in a harmonic potential F_det = -kx:

```
  γẋ = -kx + ξ(t)

  Solution: x(t) = x(0)e^(-t/τ) + noise integral
  Relaxation time: τ = γ/k

  Steady-state variance: ⟨x²⟩ = k_BT/k  (equipartition theorem)
  Power spectral density: S(f) = (k_BT/γ) × 1/(f_c² + f²)
  Corner frequency: f_c = k/(2πγ)

  These are the optical tweezer calibration equations from 07-SINGLE-MOLECULE.md.
```

### Kramers Escape Rate

For a particle in a double-well potential (two-state system), the rate of
barrier crossing is:

```
  k_Kramers = (ω₀ ω_b) / (2πγ) × exp(-ΔU/k_BT)

  ω₀ = angular frequency at potential minimum (curvature)
  ω_b = angular frequency at potential maximum (barrier curvature)
  ΔU = barrier height

  Overdamped regime (γ >> ω_b):
  k = D ω₀ ω_b / (2π k_BT) × exp(-ΔU/k_BT)

  This is Arrhenius / transition state theory from a dynamical perspective.
  Prefactor = attempt frequency × geometric factor
  Exponential = Boltzmann factor for barrier height
```

---

## Section 3 — Fokker-Planck Equation

### The Probability Density Evolution

The Fokker-Planck equation (Smoluchowski equation in overdamped limit) describes
how the probability density P(x,t) evolves:

```
  ∂P/∂t = -∂[μ F(x) P]/∂x + D ∂²P/∂x²

  μ = 1/γ (mobility)
  F(x) = -∂U/∂x (force from potential U)
  D = k_BT/γ (diffusion coefficient)

  Can be written as continuity equation:
  ∂P/∂t = -∂J/∂x

  where J = μF(x)P - D∂P/∂x  (probability current)

  At equilibrium: J = 0 → P_eq(x) ∝ exp(-U(x)/k_BT)  (Boltzmann distribution)
  Non-equilibrium: J ≠ 0 → non-Boltzmann steady state
```

### Diffusion in 3D

For free diffusion (F = 0) in 3D:

```
  ∂P/∂t = D ∇²P

  Solution: P(r,t) = (4πDt)^(-3/2) × exp(-r²/(4Dt))

  Mean squared displacement: ⟨r²⟩ = 6Dt  (3D)
                              ⟨x²⟩ = 2Dt  (1D)

  Diffusion coefficient (Stokes-Einstein):
    D = k_BT / (6πηr)

  E. coli cytoplasm (η ≈ 3 × water, r = 5 nm protein):
    D ≈ 4.1×10⁻²¹ J / (6π × 3×10⁻³ Pa·s × 5×10⁻⁹ m)
    D ≈ 15 μm²/s

  Time to diffuse across E. coli (L ≈ 1 μm):
    τ = L² / (6D) = 1/(6×15) s ≈ 10 ms
    → Fast! Diffusion is not the rate-limiting step in most signaling
```

---

## Section 4 — Master Equation and Birth-Death Processes

### Discrete Stochastic Processes

When molecule numbers are small and integer-valued, the master equation
tracks the probability P_n(t) of having exactly n molecules:

```
  dP_n/dt = Σ_m [W(n|m) P_m - W(m|n) P_n]

  W(n|m) = rate of transition from state m to state n

  For birth-death process (gene expression):
    Birth: protein produced at rate k_s (synthesis)
    Death: protein degraded at rate k_d × n (first-order)

  Master equation:
    dP_n/dt = k_s P_{n-1} - k_s P_n + k_d(n+1)P_{n+1} - k_d n P_n

  Steady-state solution: Poisson distribution
    P_n = e^{-λ} λⁿ/n!   where λ = k_s/k_d = ⟨n⟩

  Noise measure: Fano factor F = Var(n)/⟨n⟩ = 1  (Poisson)
```

### Transcriptional Bursting

In eukaryotes (and many prokaryotes), genes alternate between active and
inactive states. Transcription occurs in bursts:

```
  TWO-STATE MODEL:

  Gene-OFF ⇌ Gene-ON
     kb  ↗   ↘ kf (burst initiation rate)
            ↓
         mRNA produced at rate ks per active gene
            ↓
         mRNA degraded at rate km

  Steady-state protein distribution (Friedman et al. 2006):
    P(n) = Gamma distribution (not Poisson)
    Mean: ⟨n⟩ = ks·kf / (km·kb) (for slow switching)
    Noise: CV² = 1/⟨n⟩ + b/(1 + kf/kb)

    where b = ks/km × kf/(kf+kb) = burst size (proteins per burst)

  When kb >> kf (mostly off → rare bursts):
    CV² ≈ 1/⟨n⟩ + b   (first term: Poisson; second: excess noise from bursting)

  Burstiness: b × kf/(kf+kb) → measured by single-cell RNA-seq variability
```

Transcriptional bursting is now well-established experimentally:
- MS2/PP7 hairpin reporters (label individual mRNA molecules)
- Live-cell imaging shows discrete transcription pulses
- Single-cell RNA-seq distributions reveal non-Poisson variance

### Noise Decomposition: Intrinsic vs. Extrinsic

Elowitz et al. (2002) distinguished two types of noise in gene expression:

```
  INTRINSIC NOISE:
    Due to stochasticity in the biochemical reactions themselves
    (transcription, translation, degradation)
    Same for two identical gene copies in the same cell

  EXTRINSIC NOISE:
    Due to cell-to-cell variation in shared factors
    (transcription factor levels, ribosome concentration, cell size, cell cycle)
    Correlated between two genes in the same cell

  Measurement:
    Two distinguishable reporters under same promoter (CFP and YFP)
    η²_intrinsic = ⟨(ΔCFP - ΔYFP)²⟩ / (2⟨CFP⟩²)
    η²_extrinsic = ⟨ΔCFP·ΔYFP⟩ / ⟨CFP⟩²
    η²_total = η²_intrinsic + η²_extrinsic
```

---

## Section 5 — Fluctuation-Dissipation Theorem (FDT)

### Statement and Physical Content

The fluctuation-dissipation theorem relates the spontaneous fluctuations of a
system at equilibrium to its linear response to an external perturbation:

```
  Classical FDT (Nyquist-Johnson, 1928):

  Electrical: noise voltage PSD = S_V(f) = 4k_BT R
  (R = resistance, T = temperature, f in one-sided convention)

  Generalized FDT:
  S_x(ω) = -2k_BT / ω × Im[χ(ω)]

  where:
    S_x(ω) = power spectral density of equilibrium fluctuations
    χ(ω) = susceptibility (linear response function: x̃(ω) = χ(ω) F̃(ω))
    Im[χ(ω)] = imaginary part (dissipative component)

  Physical content:
    Dissipation (energy absorption from external force) and
    Spontaneous fluctuations (thermal noise) are two faces of the same
    underlying dynamics.
    Large susceptibility (easy to perturb) → large fluctuations
    Large damping → large fluctuations (for fixed temperature)
```

### Biological Implications

```
  1. Fluctuations probe response functions:
     Passive microrheology: track bead Brownian motion → extract viscosity
     and elasticity of cytoplasm without applying force (non-invasive)

  2. FDT is violated in active systems:
     Cytoskeletal networks with motors → enhanced fluctuations beyond
     thermal at low frequencies (active noise)
     Measuring FDT violation quantifies the ATP-driven non-equilibrium activity
     → "active temperature" >> thermal temperature

  3. Patch clamp noise analysis:
     Spontaneous channel openings (Johnson noise + shot noise) →
     extract single-channel conductance without resolving individual events
     (Nyquist-like noise analysis for ionic channels)
```

---

## Section 6 — Jarzynski Equality and Fluctuation Theorems

### Jarzynski Equality (1997)

This is the key result connecting non-equilibrium work measurements to
equilibrium free energy differences:

```
  For a process that drives the system from state A to state B:

  ⟨exp(-βW)⟩ = exp(-βΔF)

  where:
    W = work performed on system in a single realization
    β = 1/(k_BT)
    ΔF = F_B - F_A = equilibrium free energy difference
    ⟨·⟩ = average over many realizations of the process

  This is remarkable because:
    - W is measured in non-equilibrium processes (path-dependent)
    - ΔF is an equilibrium quantity (path-independent)
    - Valid for ANY process speed — infinitely fast or quasi-static
    - Generalizes the second law: ⟨W⟩ ≥ ΔF (inequality)
```

### Comparison with Second Law

```
  Second law:        ⟨W⟩ ≥ ΔF     (work ≥ free energy change)
  Equality holds:    quasi-static, reversible process

  Jensen's inequality: for convex function f, ⟨f(x)⟩ ≥ f(⟨x⟩)
  exp(-β⟨W⟩) ≤ ⟨exp(-βW)⟩ = exp(-βΔF)
  → ⟨W⟩ ≥ ΔF  ← second law recovered from Jarzynski

  Jarzynski contains the second law but provides more information:
  From the full distribution P(W), recover ΔF exactly.
```

### Practical Application: Single-Molecule Free Energies

Liphardt et al. (2002) stretched and compressed RNA hairpins with optical
tweezers at varying speeds, used Jarzynski to extract ΔG:

```
  Protocol:
    Pull RNA hairpin at speed v → measure work W (area under F-x curve)
    Repeat N times (N = 100-10,000 realizations)
    Compute: ΔF = -k_BT ln⟨exp(-W/k_BT)⟩

  Challenge: exponential average dominated by rare low-W trajectories
    → need many realizations for convergence (exponential convergence problem)

  In practice: use Bennett Acceptance Ratio (BAR) or
  Free Energy Perturbation (FEP) instead of naive Jarzynski for
  computational efficiency

  Applications:
    • Protein/RNA unfolding free energies from optical tweezer pulling
    • Drug binding ΔG from computational simulations
    • Verification of equilibrium ΔG from fast switching experiments
```

### Crooks Fluctuation Theorem (1999)

A stronger result: relates forward (A→B) and reverse (B→A) work distributions:

```
  P_F(W) / P_R(-W) = exp(β(W - ΔF))

  P_F(W) = work distribution for forward process (A→B)
  P_R(-W) = reversed-work distribution for time-reversed process (B→A)

  At W = ΔF: P_F(W=ΔF) = P_R(-W=-ΔF) → distributions cross at W = ΔF

  This gives a direct graphical method to find ΔF:
    The crossing point of P_F(W) and P_R(-W) = the free energy difference
    No exponential averaging needed → more robust than Jarzynski
```

---

## Section 7 — Stochastic Gene Expression: Biological Consequences

### Phenotypic Variability and Bet-Hedging

```
  DETERMINISTIC WORLD:    Two cells with identical DNA → identical phenotype
  STOCHASTIC REALITY:     Two cells with identical DNA → variable phenotype

  Example: B. subtilis sporulation
    ~10-20% of cells sporulate even in identical conditions
    Due to stochastic fluctuations in Spo0A phosphorylation
    Bet-hedging: some cells sporulate (survive starvation), some don't
    (grow if conditions improve)

  Example: HIV latency
    HIV can enter latent state in T cells
    Stochastic switching of Tat-mediated transactivation
    Bimodal distribution: active replication vs. deep latency
    Explains why eliminating HIV reservoirs is clinically difficult
```

### Stochastic Switching and Bistability

Some gene networks are bistable: two stable states with noise-driven switching:

```
  Genetic toggle switch (Gardner et al. 2000):
    Gene A represses Gene B; Gene B represses Gene A
    → two stable states: [A high, B low] or [A low, B high]

  ┌──────────────────────────────────────────────────────────────────┐
  │  Effective energy landscape (Waddington landscape):              │
  │                                                                  │
  │  G     ┌──┐         ┌──┐                                         │
  │        │  │         │  │  ← energy barrier between states        │
  │       ─┘  └─────────┘  └─   (set by synthesis/degradation rates) │
  │       State A        State B                                      │
  │                                                                   │
  │  Switching rate ∝ exp(-ΔG_barrier / k_BT_effective)              │
  │  k_T_effective = effective noise temperature                      │
  │  Noise drives stochastic switching between states                 │
  └──────────────────────────────────────────────────────────────────┘

  Mean switching time ∝ exp(+ΔG/σ²) where σ² = noise variance
  → Strong noise: fast switching (high noise temp)
  → Weak noise: slow switching (low noise temp)
```

---

## Probability, CS, and Information Theory Bridges

Stochastic biology uses exactly the same mathematical machinery as stochastic processes in CS, probability theory, and quantitative finance.

```
  STOCHASTIC BIOLOGY            CS / PROBABILITY PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Master equation               CTMC (continuous-time Markov chain):
  dP_n/dt = Σ [W(n|m)P_m - W(m|n)P_n]   the standard formulation of any
                                CTMC. Gene expression birth-death process
                                is a standard M/M/∞ queue: birth rate k_s
                                (arrivals), degradation k_d·n (service
                                rate proportional to queue length).
                                Steady-state is Poisson — exactly as for
                                a Poisson process in queuing theory.

  Transcriptional bursting      Compound Poisson process (burst arrivals):
  (Gamma-distributed noise,     genes fire at rate kf (burst rate) with
  Fano > 1)                     geometric burst size b. The resulting
                                protein distribution is Negative Binomial
                                (or Gamma for continuous approximation).
                                This is the shot noise model: Poisson
                                number of bursts, random burst size.

  Langevin equation             Stochastic differential equation (Ito SDE):
  γẋ = F(x) + ξ(t)             ẋ = -dU/dx·(1/γ) + √(2D)·dW_t
                                where W_t is a Wiener process. The Einstein
                                relation D = k_BT/γ connects diffusivity to
                                temperature — the same relation as in
                                Brownian motion models in quantitative
                                finance (though without the biology context).

  Fokker-Planck equation        Probability flux continuity equation:
  ∂P/∂t = -∂(μFP)/∂x + D∂²P/∂x²   formally identical to the convection-
                                diffusion PDE. Steady-state P_eq ∝ exp(-U/k_BT)
                                is the Boltzmann distribution — also the
                                invariant measure of the Langevin SDE.

  Fluctuation-dissipation       Johnson-Nyquist noise in electrical circuits:
  theorem                       S_V(f) = 4k_BT·R. Thermal noise voltage across
  ⟨ξ(t)ξ(t')⟩ = 2γk_BT·δ(t-t') a resistor equals 2γk_BT in the mechanical
                                analog. Active systems violate FDT — they have
                                an "effective temperature" > T_bath because
                                ATP-driven motors inject non-thermal noise.

  Jarzynski equality            Exponential moment identity from probability:
  ⟨exp(-βW)⟩ = exp(-βΔF)      If W = -ΔF in all trajectories (reversible),
                                equality holds exactly. Away from reversibility,
                                rare low-W trajectories dominate the exponential
                                average — same bias problem as importance
                                sampling with the wrong proposal distribution.

  Gene expression noise         Shannon entropy and mutual information:
  (intrinsic vs extrinsic)      intrinsic noise is shot noise (fundamental
                                irreducible noise of a counting process);
                                extrinsic noise is parameter variation
                                (variability in the channel). The Elowitz
                                two-reporter decomposition is exactly a
                                variance decomposition — analogous to
                                decomposing total variability into within-
                                cell and between-cell components.
  ──────────────────────────────────────────────────────────────────────
```

**Key number**: for a gene expressed at mean ⟨n⟩ proteins, Poisson noise gives CV = 1/√⟨n⟩. At ⟨n⟩ = 10 (common for transcription factors), CV = 32% — this is not a defect of cellular machinery but the irreducible noise floor of a counting process. Cells exploit this variability; they do not simply tolerate it.

---

## Decision Cheat Sheet

| Question | Concept | Key Formula |
|----------|---------|-------------|
| When does stochasticity matter? | Low copy number | CV = 1/√⟨n⟩ → significant if ⟨n⟩ < 100 |
| How does thermal noise enter dynamics? | Langevin equation | ⟨ξ(t)ξ(t')⟩ = 2γk_BT δ(t-t') |
| What is the steady-state protein distribution? | Poisson (simple birth-death) | P_n = e^(-λ)λⁿ/n! |
| What causes super-Poissonian noise in gene expression? | Transcriptional bursting | CV² = 1/⟨n⟩ + b/(1+kf/kb) |
| How to get ΔF from non-equilibrium work? | Jarzynski equality | ⟨exp(-βW)⟩ = exp(-βΔF) |
| How to find ΔF graphically from pulling experiments? | Crooks FT | P_F(W=ΔF) = P_R(-W=ΔF) |
| Why does the second law follow from Jarzynski? | Jensen's inequality | exp(-β⟨W⟩) ≤ ⟨exp(-βW)⟩ |
| How does noise differ intrinsic vs. extrinsic? | Elowitz two-reporter | Correlated fluctuations = extrinsic |

---

## Common Confusion Points

**Fluctuation-dissipation theorem requires equilibrium.** The FDT is exact only
at thermodynamic equilibrium. In living cells, ATP-driven processes (motors,
signaling cascades) create non-equilibrium conditions that violate FDT. Measuring
FDT violation is itself a way to quantify the non-equilibrium activity — cells
use ATP to amplify mechanical fluctuations above the thermal floor.

**Jarzynski exponential average is biased for finite samples.** The exponential
⟨exp(-βW)⟩ is dominated by rare trajectories with small (or negative) W. With
finite sampling, the estimator is biased upward (overestimates ΔF). The bias
is O(σ²_W/N) where σ²_W is the work variance and N is the number of realizations.
The Crooks fluctuation theorem avoids this by comparing distributions directly.

**Poisson statistics are the minimal noise floor for biochemical reactions.** For
a simple birth-death process, Fano factor = 1 (Poisson). Any positive feedback,
bursting, or cooperative mechanism adds noise above this floor (Fano > 1). Any
negative feedback reduces noise below Poisson (Fano < 1). This is the basis of
noise-buffering circuits in synthetic biology.

**Overdamped ≠ no inertia in all senses.** The overdamped Langevin equation discards
inertial terms because τ_i = m/γ ~ 10⁻¹³ s is invisible at biological time scales.
But hydrodynamic memory effects (solvent inertia, not particle inertia) can be
relevant at sub-ns time scales for nm-scale particles. For biological processes
(ms-s), overdamped is always valid.

**Noise can be functional.** Stochastic gene expression is not simply a nuisance to
be minimized. Cells exploit noise for: probabilistic fate choices (Bacillus sporulation),
population diversification (bet-hedging), bistable switch stochastic transitions (HIV
latency), and sensory adaptation via noise-driven exploration. Evolution has tuned
noise levels, not just mean expression levels.
