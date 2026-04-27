# Cosmology
## Big Bang, Expansion, CMB, Dark Matter, Dark Energy, Large-Scale Structure

---

## 1. The Full Picture — Cosmic History and Components

```
  COSMIC TIMELINE (log scale)

  t=0          Planck epoch (t_P ~ 5×10⁻⁴⁴ s, T~10³² K) — GR breaks down, QG needed
  10⁻³⁶ s     Inflation begins: exponential expansion, ~60 e-folds in ~10⁻³² s
  10⁻³² s     Inflation ends: reheating, particle production, standard model restored
  10⁻¹² s     Electroweak transition (T~100 GeV): W/Z bosons gain mass
  10⁻⁶ s      QCD transition: quarks → hadrons, protons/neutrons form (T~150 MeV)
  1 s          Neutrino decoupling (T~1 MeV); e⁺e⁻ annihilation heats photons
  3 min        Big Bang Nucleosynthesis (BBN): H→He, D, ³He, ⁷Li (T~0.1 MeV)
  70 kyr       Matter-radiation equality (z~3400): matter begins to dominate
  380 kyr      RECOMBINATION (z~1100, T~3000 K): plasma → neutral H → CMB released
  200 Myr      First stars (Pop III, z~10-20): end of cosmic dark ages
  1 Gyr        Reionization complete (z~6); first quasars, galaxy formation
  3 Gyr        Peak star formation + quasar activity (z~2-3)
  5 Gyr        Dark energy begins to dominate (z~0.4, ä changes sign)
  9.8 Gyr      Solar System forms (z~0.5)
  13.787 Gyr   Today (z=0)

  THE ΛCDM CONTENT PIE:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Dark Energy (Λ):    68.5%  — drives accelerated expansion           │
  │  Dark Matter (CDM):  26.5%  — gravitational scaffold for structure   │
  │  Ordinary Matter:     4.9%  — baryons (stars, gas, planets, you)     │
  │  Radiation:          ~0.01% — photons + neutrinos, negligible today  │
  └──────────────────────────────────────────────────────────────────────┘
  Of the ~5% ordinary matter: ~90% is diffuse gas in filaments/CGM,
  ~10% is stars, ~0.1% is everything else (planets, dust, black holes...)
```

---

## 2. The FLRW Metric — Geometry of an Expanding Universe

The cosmological principle (large-scale homogeneity + isotropy) forces the metric to be:

```
  FRIEDMANN-LEMAÎTRE-ROBERTSON-WALKER (FLRW) METRIC:

  ds² = −c² dt² + a(t)² [ dr²/(1−kr²) + r² dΩ² ]

  a(t) = scale factor (dimensionless; by convention a₀ = a(t_now) = 1)
  r    = comoving coordinate (doesn't change as universe expands)
  k    = spatial curvature: −1 (hyperbolic), 0 (flat), +1 (spherical)

  Physical distance: d_phys(t) = a(t) × d_comoving
  Physical velocity: v = ḋ_phys = ȧ d_comoving = (ȧ/a) d_phys = H(t) d_phys

  HUBBLE'S LAW:  v = H₀ d     [Hubble 1929, recession velocity ∝ distance]

  H(t) = ȧ/a   (Hubble parameter; H₀ = H(t_now))

  REDSHIFT:
  1 + z = a(t_now)/a(t_emit) = 1/a(t_emit)     [photon wavelength stretched by a]

  z = 0:    now
  z = 0.5:  a = 2/3, universe was 2/3 current size
  z = 1100: a = 1/1101 ≈ 0.001, time of recombination (CMB)
  z = ∞:    t = 0, Big Bang singularity
```

### 2.1 The Friedmann Equations

From Einstein's field equations G_μν + Λg_μν = 8πG/c⁴ T_μν with FLRW metric:

```
  FIRST FRIEDMANN EQUATION  (energy-like):
  ┌──────────────────────────────────────────────────────────────────────┐
  │  H² = (ȧ/a)² = 8πGρ/3 − kc²/a² + Λc²/3                               │
  │                 ────────  ───────  ──────                            │
  │                 matter    curvature dark energy                      │
  └──────────────────────────────────────────────────────────────────────┘
  ρ = total energy density (matter + radiation)

  SECOND FRIEDMANN EQUATION  (force-like / acceleration):
  ┌──────────────────────────────────────────────────────────────────────┐
  │  ä/a = −4πG/3 (ρ + 3P/c²) + Λc²/3                                    │
  └──────────────────────────────────────────────────────────────────────┘
  Deceleration if ρ + 3P > 0; acceleration if Λc²/3 > 4πG(ρ + 3P/c²)/3

  KEY: dark energy (Λ) has P = −ρc² (negative pressure!) → drives ä > 0
```

### 2.2 Density Parameters and Critical Density

```
  Critical density (k=0, Λ=0 would make expansion exactly marginal):
  ρ_c = 3H²/(8πG)
  ρ_c(t_now) ≈ 9.47 × 10⁻³⁰ g/cm³  (~5 protons/m³)

  Density parameters:  Ω_i = ρ_i / ρ_c

  Friedmann eq. with all components:
  H²(z)/H₀² = Ω_r(1+z)⁴ + Ω_m(1+z)³ + Ω_k(1+z)² + Ω_Λ

  Scaling with redshift:
  ─────────────────────────────────────────────────────────────────────
  Radiation:     ρ_r ∝ a⁻⁴  = (1+z)⁴    (photon number density + blueshift)
  Matter:        ρ_m ∝ a⁻³  = (1+z)³    (conserved mass in expanding volume)
  Curvature:     ∝ a⁻²  = (1+z)²
  Dark energy:   ρ_Λ = const              (vacuum energy — doesn't dilute)
  ─────────────────────────────────────────────────────────────────────

  PLANCK 2018 BEST-FIT ΛCDM PARAMETERS:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  H₀     = 67.36 ± 0.54  km/s/Mpc   (Planck CMB)                     │
  │  H₀     = 73.0  ± 1.0   km/s/Mpc   (SH0ES Cepheids) ← TENSION!      │
  │  Ω_b h² = 0.02237        baryons                                    │
  │  Ω_c h² = 0.1200         cold dark matter                           │
  │  Ω_Λ   = 0.6847          dark energy                                │
  │  n_s    = 0.9651          primordial spectral index                 │
  │  σ₈    = 0.8111           amplitude of matter fluctuations          │
  │  t₀    = 13.787 ± 0.020 Gyr   age of universe                       │
  │  Flat: Ω_total = 1.000 ± 0.002                                      │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Inflation — Solving the Classical Problems

Before inflation was proposed, ΛCDM had three unresolved problems:

```
  HORIZON PROBLEM:
  CMB is uniform to 1 part in 10⁵ across the entire sky.
  Without inflation, opposite sides of the CMB were NEVER in causal contact —
  their particle horizons didn't overlap at recombination.
  → How did they equilibrate to the same temperature?

  FLATNESS PROBLEM:
  Ω_total = 1 to ~0.1% today. But Ω = 1 is an unstable fixed point:
  small deviations grow as Ω−1 ∝ a²  (radiation era) or a (matter era)
  → at t=1s, |Ω−1| < 10⁻¹⁶ required → extraordinary fine-tuning

  MONOPOLE PROBLEM:
  GUT-scale phase transitions should produce magnetic monopoles.
  Observed: none. → Where did they go?

  INFLATION SOLUTION:
  Exponential expansion (de Sitter-like) stretches a tiny causally-connected
  patch to >> observable universe.
  ─────────────────────────────────────────────────────────────────────────
  → Horizon problem: all observable universe from one causally-connected patch
  → Flatness: curvature diluted as k/a² → 0 during inflation → Ω → 1
  → Monopoles: density diluted exponentially → effectively zero

  MECHANISM (slow-roll inflation):
  Scalar field φ (inflaton) slowly rolls down a nearly flat potential V(φ)
  Pressure ≈ −V(φ) < 0  →  ä > 0  →  exponential expansion
  ρ ≈ V(φ) ≈ const during roll  →  de Sitter-like expansion: a ∝ e^(Ht)

  QUANTUM FLUCTUATIONS:
  During inflation, quantum fluctuations δφ are stretched to macroscopic scales.
  They freeze when scale > Hubble radius during inflation.
  → Re-enter Hubble radius later as classical density perturbations
  → Seeds all subsequent structure formation

  PREDICTION: nearly scale-invariant power spectrum
  P(k) ∝ k^(n_s − 1)    n_s = 1 − 2ε − δ  (slow-roll parameters)
  Planck measured: n_s = 0.9651 ± 0.0044   (tilt away from 1 → finite slow-roll)
  ─────────────────────────────────────────────────────────────────────────
  Tensor modes (primordial gravitational waves):
  r = tensor/scalar ratio  →  B-mode polarization in CMB
  Not yet detected; r < 0.036 (BICEP/Keck 2022)
  Many inflation models already ruled out; others survive (Starobinsky: r~0.004)
```

---

## 4. Big Bang Nucleosynthesis (BBN)

```
  At t ~ 1 s (T ~ 1 MeV):
  Weak reactions (n + ν ↔ p + e⁻, etc.) maintain n/p equilibrium
  → n/p = exp(−(m_n−m_p)c²/kT) = exp(−1.293 MeV/T)

  At T ~ 1 MeV: reactions freeze out → n/p ≈ 1/6
  Free neutron decay (τ_n ~ 880 s) reduces this before BBN starts → n/p ≈ 1/7

  At t ~ 3 min (T ~ 0.1 MeV = 10⁹ K):
  ┌─────────────────────────────────────────────────────────────────────┐
  │  p + n → D + γ                                                      │
  │  D + D → ³He + n,  ⁴He + p                                          │
  │  D + p → ³He + γ,  ³He + n → ⁴He + p (etc.)                         │
  │  Bottleneck: D photodissociation delays start until T < 0.07 MeV    │
  │  (despite n+p→D available, photons destroy D until cool enough)     │
  └─────────────────────────────────────────────────────────────────────┘

  BBN ABUNDANCES:
  ─────────────────────────────────────────────────────────────────────────
  ⁴He:   ~25% by mass (Y_p ≈ 0.247)  ← most of ⁴He is primordial
  D/H:   ~2.5×10⁻⁵               ← deuterium bottleneck probe
  ³He/H: ~1×10⁻⁵
  ⁷Li/H: ~5×10⁻¹⁰               ← "lithium problem": predicted vs observed
  ─────────────────────────────────────────────────────────────────────────

  BBN is EXQUISITELY sensitive to:
  1. Baryon-to-photon ratio η = n_b/n_γ ~ 6×10⁻¹⁰  (sets He, D abundances)
  2. Number of light neutrino species N_ν (more ν → faster expansion → higher n/p)
     BBN constrains N_ν = 2.88 ± 0.27 → consistent with 3 (LEP: exactly 3)
  3. Neutron lifetime τ_n (directly sets n/p ratio)

  The agreement between BBN predictions and measured primordial abundances is
  one of the strongest supports for the standard hot Big Bang model.

  LITHIUM PROBLEM (unresolved):
  Observed ⁷Li/H in old Pop II halo stars is ~3× lower than BBN prediction
  → depletion in stellar atmospheres? BBN physics? Unknown. Active research.
```

---

## 5. The Cosmic Microwave Background

### 5.1 Origin and Spectrum

```
  At recombination (z~1100, t~380 kyr, T~3000 K):
  Protons capture electrons → neutral H (Saha equation sets timescale)
  Mean free path of photons → ∞  (universe becomes transparent)
  CMB photons free-stream from "last scattering surface"

  CMB TODAY:
  Redshifted blackbody:  T_CMB = 2.7255 ± 0.0006 K
  Peak wavelength:  λ_max ≈ 2 mm  (microwave band)
  Energy density:   ρ_γ = 4.64×10⁻³⁴ g/cm³
  Photon number density: n_γ ≈ 411 photons/cm³  (everywhere, right now)

  CMB is the most perfect blackbody spectrum ever measured:
  COBE FIRAS (1990): δB/B < 10⁻⁴ — essentially perfect Planck curve
  (Any energy injection after z~10⁶ would distort this — all distortions < 10⁻⁵)
```

### 5.2 Temperature Anisotropies

```
  TEMPERATURE FLUCTUATIONS:  δT/T ~ 10⁻⁵

  SOURCES:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ Primary (from recombination):                                           │
  │                                                                         │
  │ 1. Sachs-Wolfe effect (ℓ < 100, θ > 2°):                                │
  │    Photons climbing out of density wells at recombination               │
  │    Are gravitationally redshifted → cooler toward overdensities         │
  │    (counter-intuitive: overdense regions appear cool on large scales)   │
  │                                                                         │
  │ 2. Acoustic oscillations (ℓ ~ 100–2000):                                │
  │    Pre-recombination plasma is coupled gas+radiation                    │
  │    Pressure waves oscillate in photon-baryon fluid                      │
  │    At recombination: modes "frozen" at random phase in oscillation      │
  │    → peaks in power spectrum where modes caught at extrema              │
  │                                                                         │
  │ 3. Silk damping (ℓ > 1000, small scales):                               │
  │    Photon diffusion erases fluctuations below Silk scale (~7 Mpc)       │
  │    Exponential suppression of power at high ℓ                           │
  │                                                                         │
  │ Secondary (after recombination):                                        │
  │    Reionization (τ_reion): suppresses power by e^(−2τ) at small scales  │
  │    Integrated Sachs-Wolfe (ISW): DE-induced potential decay at late time│
  │    Sunyaev-Zel'dovich (SZ): hot cluster gas inverse-Compton scatters    │
  │    Gravitational lensing: smears acoustic peaks                         │
  └─────────────────────────────────────────────────────────────────────────┘
```

### 5.3 The CMB Power Spectrum — Reading the Cosmological Parameters

```
  ANGULAR POWER SPECTRUM C_ℓ (where ℓ ~ 180°/θ)

  C_ℓ  ↑
      │         ●  ← 1st acoustic peak (ℓ~220, θ~1°)
      │        ●●●
      │       ●   ●   ●  ← 2nd peak (ℓ~540)
      │      ●     ● ●  ●  ← 3rd peak (ℓ~810)
      │    ●●        ●●    ●●     ← 4th, 5th peaks
  SW  │●●●                           ●●●  ← Silk damping
  plateau──────────────────────────────────────────→ ℓ
       10        100       1000      2000

  WHAT EACH FEATURE TELLS YOU:
  ─────────────────────────────────────────────────────────────────────────
  Feature                           Constraint
  ─────────────────────────────────────────────────────────────────────────
  1st peak position (ℓ~220)         Geometry: flat (k=0) → Ω_total ≈ 1
                                    (curvature shifts peak left/right)
  1st peak height                   Matter/radiation ratio at recombination
  2nd peak height (relative to 1st) Baryon density Ω_b h²
                                    (more baryons → compresses odd peaks,
                                    rarefies even peaks → height alternation)
  3rd peak height                   Cold dark matter density Ω_c h²
  Peak spacing                      Sound horizon at recombination (~150 Mpc)
  Damping tail slope                Silk diffusion scale, helium abundance
  Overall amplitude                 σ₈ (amplitude of matter fluctuations)
  Low-ℓ plateau (Sachs-Wolfe)       Primordial power spectrum tilt n_s
  Large-angle anomalies (ℓ=2,3)    Quadrupole/octopole: low (unexplained)
  ─────────────────────────────────────────────────────────────────────────
  The CMB is essentially a photograph of quantum fluctuations at t=380 kyr,
  encoding the entire cosmological parameter set in a single sky map.
```

---

## 6. Dark Matter — Evidence and Candidates

### 6.1 The Evidence (Multiple Independent Lines)

```
  1. GALAXY ROTATION CURVES (Rubin & Ford 1970s):
     Keplerian expectation: v(r) = √(GM(<r)/r) → v ∝ r^(−1/2) outside disk
     Observed: v(r) = const ("flat rotation curve") out to 50+ kpc
     → mass must continue increasing: M(<r) ∝ r, ρ_DM ∝ r^(−2) → NFW halo

  2. GALAXY CLUSTER DYNAMICS (Zwicky 1933 — first evidence):
     Virial theorem: M_virial ~ 10× M_luminous
     Same seen in X-ray gas temperature, gravitational lensing mass maps

  3. GRAVITATIONAL LENSING:
     Weak lensing: coherent shear of background galaxy shapes → mass map
     Mass maps don't follow light distribution → dark component

  4. BULLET CLUSTER (1E0657-558):
     Two galaxy clusters that collided ~100 Myr ago
     ┌──────────────────────────────────────────────────────────────┐
     │  Hot gas (X-ray):   slowed by ram pressure → sits between    │
     │  Galaxies + DM:     collisionless → passed through each other│
     │  Grav lens: mass peak coincides with galaxies, NOT gas       │
     └──────────────────────────────────────────────────────────────┘
     → DM is collisionless (no electromagnetic interaction)
     → Best direct evidence against MOND (modified gravity alternatives)

  5. BBN + CMB CONSISTENCY:
     BBN → Ω_b h² ~ 0.022  (ordinary matter only)
     CMB → Ω_m ~ 0.315     (total matter)
     → Non-baryonic dark matter makes up ~84% of all matter

  ALL FIVE are independent and consistent: dark matter is real.
```

### 6.2 Dark Matter Candidates

```
  CANDIDATE         MASS RANGE        STATUS (2025)
  ──────────────────────────────────────────────────────────────────────────
  WIMPs             1–10,000 GeV      No direct detection (LZ: 10⁻⁴⁸ cm²)
  (LSP, neutralino)                   No LHC SUSY signal; WIMP window closing
  Axions            10⁻⁶–10⁻³ eV    ADMX (axion mass ~3 μeV), CASPEr
  Sterile neutrinos ~keV              X-ray line at 3.5 keV (debated)
  Primordial BHs    asteroid-mass     Microlensing: LIGO mass range ruled out;
                    window open       asteroid-mass window still open
  Ultralight ALP    ~10⁻²² eV        "Fuzzy DM" — quantum interference at kpc
                    ("fuzzy DM")      Some tension with Ly-α constraints
  ──────────────────────────────────────────────────────────────────────────
  No confirmed dark matter particle candidate as of 2025.
  This is one of the biggest open problems in physics.

  KEY CONSTRAINT: DM must be:
  ● Cold (non-relativistic at structure formation epoch) — explains observed structure
  ● Collisionless (Bullet Cluster) or very weakly self-interacting
  ● Non-baryonic (BBN)
  ● Stable on cosmological timescales (or τ >> t_universe)
  ● Not too strongly interacting with ordinary matter (direct detection limits)
```

---

## 7. Dark Energy — The Accelerating Universe

### 7.1 Discovery and Evidence

```
  1998: Two independent teams (Perlmutter/LBL + Schmidt/Riess/Harvard)
  Measured Type Ia SNe to z~1 → distance vs redshift relation

  EXPECTED: matter-dominated universe → deceleration at high z
  OBSERVED: SNe at z~0.5-1 are ~25% dimmer than expected
           → they are farther away → universe expanded MORE than expected
           → expansion is ACCELERATING   (Nobel Prize 2011)

  SUBSEQUENT EVIDENCE:
  ● CMB (Planck): Ω_total = 1.00 ± 0.002, Ω_m ≈ 0.31 → Ω_Λ ≈ 0.69 required
  ● BAO (galaxy surveys): independent distance-redshift measurements confirm Λ
  ● Age of universe: 13.787 Gyr — only consistent if dark energy present
                     (matter-only flat universe would be ~9 Gyr → younger than old stars)
```

### 7.2 What Dark Energy Is (and Isn't Known)

```
  COSMOLOGICAL CONSTANT (Λ):
  Einstein added Λ in 1917 (to get static universe), then called it his "biggest blunder"
  Now: Λ ≡ constant vacuum energy density

  Equation of state: w = P / (ρc²) = −1  (for Λ)
  → Vacuum energy: as universe expands, new volume has same energy density
  → Energy grows with volume → accelerates expansion

  THE COSMOLOGICAL CONSTANT PROBLEM:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  QFT prediction: ρ_vac ~ (E_Planck)⁴/(ℏc)³ ~ 10⁹⁴ g/cm³                  │
  │  Observed:       ρ_Λ  ~ 10⁻²⁹ g/cm³                                      │
  │  Discrepancy:    10¹²³  — worst fine-tuning problem in physics           │
  │  SUSY would reduce to ~10⁶⁰, still terrible.                             │
  └──────────────────────────────────────────────────────────────────────────┘

  ALTERNATIVES:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Quintessence: dynamical scalar field, w > −1, w varies with time         │
  │ Phantom energy: w < −1 → Big Rip (all structure torn apart)              │
  │ Modified gravity (f(R), DGP, etc.): GR modified at cosmological scales   │
  │ Anthropic selection (landscape): Λ small enough for galaxies to form     │
  └──────────────────────────────────────────────────────────────────────────┘

  CURRENT MEASUREMENT:
  w = −1.03 ± 0.03  (Planck + SNe + BAO combined) — consistent with Λ
  DESI 2024 (BAO): hints of w₀ ≈ −0.8, wₐ ≈ −0.8 (dynamical DE at 2.6σ)
  → Not yet conclusive; watch this space
```

---

## 8. Large-Scale Structure

### 8.1 The Cosmic Web

```
  COSMIC WEB HIERARCHY:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Voids         ~10–100 Mpc  underdense regions, ~70% of volume          │
  │  Filaments     ~10–100 Mpc  web connecting nodes, ~5% of volume         │
  │  Walls/sheets  ~100 Mpc     flattened overdensities                     │
  │  Clusters      ~1–30 Mpc   massive collapsed structures, ~500 galaxies+ │
  │  Groups        ~1–5 Mpc    ~50 galaxies (Local Group: MW + Andromeda)   │
  │  Galaxies      ~10–100 kpc  stars + DM halo + CGM                       │
  │  Stars         varies       nuclear-burning plasma spheres (§ 04)       │
  └─────────────────────────────────────────────────────────────────────────┘

  ORIGIN: inflation → quantum fluctuations → classical density perturbations
  δ(x,t) = (ρ(x,t) − ρ̄) / ρ̄

  Growth of perturbations:
  ● Radiation era (z > z_eq ~ 3400): DM perturbations suppressed (Meszaros effect)
    Photon pressure resists baryon compression; DM decoupled but gravity competes with H
  ● Matter era (z < z_eq): δ ∝ a(t) ∝ (1+z)⁻¹  (linear growth)
  ● Dark energy era (z < 0.4): growth suppressed again (expansion wins over gravity)
```

### 8.2 Matter Power Spectrum

```
  MATTER POWER SPECTRUM P(k) = |δ_k|²

  P(k)  ↑
        │  ●  ← peak (k_eq ~ matter-radiation equality scale)
        │ ●●●
        │●   ●●
        │      ●●●
        │         ●●●●        ← P(k) ∝ k^(n_s) × T²(k)  at large k
        │             ●●●●●●  (transfer function suppression from Silk/BAO)
        └───────────────────────────────────────────────────────── log k
         0.001              0.1              1  [h/Mpc]

  Primordial: P(k) ∝ k^n_s  (Harrison-Zel'dovich: n_s=1 → scale-invariant)
  Transfer function T(k): suppresses power at k > k_eq from radiation-era damping
  BAO wiggles: oscillations imprinted on P(k) at sound horizon scale

  σ₈ = amplitude of matter fluctuations smoothed over 8 h⁻¹ Mpc sphere
     = 0.8111 (Planck CMB)
     = 0.76-0.79 (weak lensing surveys) ← σ₈ TENSION (2-3σ) — may be new physics
```

### 8.3 Baryon Acoustic Oscillations (BAO)

```
  The sound horizon at recombination: r_s ≈ 147 Mpc (comoving)
  ─────────────────────────────────────────────────────────────────────────
  Pre-recombination: photon-baryon fluid has pressure waves (acoustic oscillations)
  At recombination: waves freeze → preferred scale r_s imprinted in:
    (a) CMB power spectrum: 1st acoustic peak position (θ_s ≈ r_s/d_A)
    (b) Galaxy distribution: excess galaxy pairs at ~150 Mpc separation

  BAO as "STANDARD RULER":
  We know r_s precisely from CMB. Measure angular scale θ(z) in galaxy surveys
  → get angular diameter distance D_A(z) at each redshift
  → trace H(z) → constrain dark energy equation of state

  KEY SURVEYS:
  ┌──────────────────────────────────────────────────────────────────────┐
  │ SDSS BOSS (2014):   BAO detected at 0.1 < z < 0.6, ~1% precision     │
  │ eBOSS (2021):       z up to 2.2 using quasars as tracers, ~0.7%      │
  │ DESI (2024):        6 million galaxies, 0.1 < z < 3.5, ~0.5%         │
  │                     First evidence of evolving dark energy (w₀,wₐ)   │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 9. The Distance Ladder

How we measure cosmic distances — each rung calibrates the next:

```
  DISTANCE LADDER

  ┌──────────────┬──────────────────┬──────────────┬───────────────────────┐
  │ Rung         │ Method           │ Range        │ Key assumption        │
  ├──────────────┼──────────────────┼──────────────┼───────────────────────┤
  │ 1. Geometry  │ Parallax (GAIA)  │ < 10 kpc     │ Euclidean geometry    │
  │              │ Maser distances  │ ~10-100 Mpc  │ VLBI trigonometry     │
  ├──────────────┼──────────────────┼──────────────┼───────────────────────┤
  │ 2. Standard  │ Cepheid P-L      │ < 100 Mpc    │ P-L calibrated in LMC │
  │    candles   │ RR Lyrae         │ < 1 Mpc      │ Period-luminosity     │
  │              │ TRGB (RGB tip)   │ < 30 Mpc     │ He flash luminosity   │
  ├──────────────┼──────────────────┼──────────────┼───────────────────────┤
  │ 3. SN Ia     │ Phillips relation│ < 1.5 Gpc    │ Calibrated by rung 2  │
  │              │ (width-lum.)     │              │ ← Hubble tension here │
  ├──────────────┼──────────────────┼──────────────┼───────────────────────┤
  │ 4. BAO       │ Standard ruler   │ any z        │ r_s from CMB          │
  │              │ (galaxy surveys) │              │ Cosmological model    │
  ├──────────────┼──────────────────┼──────────────┼───────────────────────┤
  │ 5. CMB       │ Angular scale of │ z~1100       │ Cosmological model    │
  │              │ sound horizon    │              │ (Planck)              │
  └──────────────┴──────────────────┴──────────────┴───────────────────────┘
```

---

## 10. The Hubble Tension — Current Crisis

```
  THE 5σ DISCREPANCY:

  EARLY-UNIVERSE MEASUREMENTS (CMB/BBN/BAO — standard ruler):
  H₀ = 67.4 ± 0.5 km/s/Mpc   (Planck 2018)
  H₀ = 67.6 ± 1.1 km/s/Mpc   (DESI 2024 BAO + BBN)

  LATE-UNIVERSE MEASUREMENTS (Cepheids → SNe Ia — standard candle):
  H₀ = 73.0 ± 1.0 km/s/Mpc   (SH0ES, Riess et al.)
  H₀ = 72.6 ± 2.0 km/s/Mpc   (H0LiCOW strong lensing time delays)
  H₀ = 73.8 ± 1.1 km/s/Mpc   (Carnegie-Chicago Hubble Program, TRGB)

  Tension: ~4.7σ (very unlikely to be statistical fluctuation)

  JWST FOLLOW-UP (2023):
  JWST independently measured Cepheids in SH0ES anchor galaxies
  → Confirms Cepheid distances, not systematic error
  → Late-universe H₀ holds; early-universe model must change (?)

  CANDIDATE RESOLUTIONS:
  ┌────────────────────────────────────────────────────────────────────────┐
  │ New physics before recombination:                                      │
  │   Early Dark Energy (EDE): decays at z~3000, increases expansion rate  │
  │   Extra relativistic species (ΔN_eff): more radiation → higher H_rec   │
  │   Neutrino self-interactions: alter sound horizon                      │
  │                                                                        │
  │ New physics after recombination:                                       │
  │   Modified gravity at cosmological scales                              │
  │   Evolving dark energy w(z)                                            │
  │                                                                        │
  │ Systematic errors:                                                     │
  │   Crowded fields in Cepheid host galaxies → blend contamination        │
  │   LMC Cepheid calibration                                              │
  │   Reddening + metallicity corrections                                  │
  │   JWST reduces these concerns but tension persists                     │
  └────────────────────────────────────────────────────────────────────────┘
  No consensus resolution as of 2025. Widely considered the most important
  problem in observational cosmology.
```

---

## 11. Gravitational Waves and Multi-Messenger Astronomy

```
  GW SOURCES AND DETECTORS:

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Frequency    Source                  Detector          Status            │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ~100 Hz      BH+BH, NS+NS mergers   LIGO/Virgo/KAGRA  Operating        │
  │ ~1-10 mHz    Massive BH mergers,    LISA               Launch ~2035     │
  │              compact binaries,                                           │
  │              stochastic background                                       │
  │ ~nHz         SMBH binary mergers    PTA (NANOGrav,     GWB detected     │
  │                                     PPTA, EPTA)        2023!            │
  └──────────────────────────────────────────────────────────────────────────┘

  GW150914 (LIGO, 2015):
  First direct detection: two 30 M☉ BHs merged → 60 M☉ + GW
  Confirmed GR prediction of gravitational waves (Einstein 1916, 99 yr delay)
  3 solar masses radiated as GWs in 0.2 s → peak power ~3.6×10⁵⁶ W

  GW170817 (LIGO+Virgo + 70 EM observatories, 2017):
  NS + NS merger (1.3 + 1.4 M☉, ~40 Mpc away)
  → Kilonova: optical transient confirmed r-process (Au, Pt, Eu — gold!)
  → Short GRB: confirmed sGRB = NS merger origin
  → H₀ = 70 ± 12 km/s/Mpc (distance from GW amplitude + redshift)
  Multi-messenger astrophysics begins.

  NANOGrav (2023):
  15-yr dataset, 67 ms pulsars → gravitational wave background detected
  Spectrum consistent with SMBH binary merger background from z~1-3
  Possibly evidence of SMBH binaries throughout cosmic history
```

---

## 12. Cosmological Distances — The Vocabulary

```
  DISTANCE MEASURES (they all differ in an expanding universe):

  ┌────────────────────────────────────────────────────────────────────────┐
  │ Comoving distance:  χ = ∫₀ᶻ c dz'/H(z')                                │
  │   Distance in today's coordinates; doesn't change as universe expands  │
  │   Observable universe: χ_max ≈ 46.5 Gly (comoving)                     │
  │                                                                        │
  │ Angular diameter distance: D_A = χ/(1+z)                               │
  │   Physical size of object / observed angle: θ = l/D_A                  │
  │   Has a MAXIMUM: peaks at z ~ 1.5 (objects at z > 1.5 appear LARGER    │
  │   with increasing z — expansion shrinks angular diam. distance)        │
  │                                                                        │
  │ Luminosity distance: D_L = χ(1+z) = D_A(1+z)²                          │
  │   flux = L/(4πD_L²)    [used for SNe Ia, Type Ia standard candle]      │
  │   Always larger than comoving distance                                 │
  │                                                                        │
  │ Hubble radius: d_H = c/H₀ ≈ 14.5 Gly                                   │
  │   NOT a horizon — objects beyond can still send light to us            │
  │   (due to acceleration, some comoving regions already out of reach)    │
  │                                                                        │
  │ Particle horizon:  χ_particle ≈ 46.5 Gly   (furthest light could       │
  │   have reached us from Big Bang — defines observable universe)         │
  │                                                                        │
  │ Event horizon:  χ_event ≈ 16 Gly  (furthest we can ever influence      │
  │   or receive light from — due to accelerating expansion)               │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 13. Fate of the Universe

```
  DEPENDS ON w (dark energy equation of state parameter):

  w = −1 (cosmological constant, ΛCDM):
    Universe expands exponentially forever → de Sitter space
    All galaxies beyond ~5 Gly will eventually redshift out of sight
    After ~10¹⁴ yr: last stars burn out → "degenerate era"
    After ~10³⁷ yr: proton decay (if predicted by GUT) → matter dissolves
    After ~10⁶⁴ yr: stellar BHs evaporate (Hawking radiation)
    After ~10¹⁰⁰ yr: SMBH evaporate
    → Heat death (maximum entropy, zero usable energy)

  w > −1 (quintessence):
    Slower acceleration; similar endpoint; DE may eventually decay

  w < −1 (phantom energy):
    Dark energy density grows with time → expansion accelerates unboundedly
    → BIG RIP: at some finite time, expansion rips apart galaxies,
               stars, planets, atoms
    For w = −1.5: Big Rip in ~20 Gyr
    Current data: w = −1.03 ± 0.03, not significantly phantom

  k = +1, no Λ (hypothetical):
    Expansion slows → halts → recollapse → Big Crunch
    Ruled out by observation (flat + Λ)

  VACUUM DECAY WILDCARD:
  Our vacuum may be a metastable "false vacuum" (Higgs field)
  Quantum tunneling to lower energy state travels at c — no warning
  Current Higgs mass (125 GeV) sits near stability boundary
  Probability in 13.8 Gyr: calculable, appears low but uncertain
```

---

## Decision Cheat Sheet

```
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Question                               │ Key fact                          │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What is 68% of the universe?           │ Dark energy (Λ), constant density │
  │ What is 27%?                           │ Dark matter (non-baryonic, CDM)   │
  │ What is 5%?                            │ Ordinary matter (baryons)         │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What does the CMB first peak tell us?  │ Universe is flat (k ≈ 0)          │
  │ What does peak height alternation?     │ Baryon density Ω_b                │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why is matter ∝ (1+z)³ but DE const?  │ Matter dilutes with volume;        │
  │                                        │ vacuum energy = constant density   │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Best evidence DM is not baryonic?      │ BBN: Ω_b h²=0.022 vs CMB          │
  │                                        │ Ω_m h²=0.143 → 84% non-baryonic   │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Best evidence DM is collisionless?     │ Bullet Cluster: mass peak follows │
  │                                        │ galaxies, not hot gas             │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What is BAO used for?                  │ Standard ruler → D_A(z) and H(z)  │
  │                                        │ → dark energy constraints         │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What problems did inflation solve?     │ Horizon, flatness, monopoles      │
  │ What did it predict?                   │ n_s ≈ 0.96, primordial GWs (B-mode│
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What is the Hubble tension?            │ CMB: H₀=67.4 vs Cepheids: 73.0    │
  │                                        │ ~5σ; unresolved; new physics?     │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What did GW170817 confirm?             │ NS mergers → r-process (gold!)    │
  │                                        │ Short GRBs = NS mergers           │
  │                                        │ First multi-messenger GW event    │
  └────────────────────────────────────────┴───────────────────────────────────┘
```

---

## Common Confusion Points

**"The universe is expanding into something"**
No. The FLRW metric describes the expansion of space itself — distances between comoving objects increase. There is no "outside." The observable universe is not expanding into a larger space; space itself is what's growing. (Analogies like "raisin bread" are useful but carry baggage — raisins move through dough; galaxies don't move through a pre-existing space.)

**"The Big Bang happened at a point in space"**
No. At the Big Bang, all space (the entire FLRW manifold) was compressed into a singularity. There was no "outside" into which the Big Bang exploded. Every point in today's universe was at the same location at t=0. "Where did the Big Bang happen?" → Everywhere.

**"Distant galaxies recede faster than light — that violates SR"**
No. Special relativity prohibits objects moving faster than light through space. Hubble recession is space itself expanding — there's no local SR violation. At z ~ 1.5, objects have recession velocities > c. We can still receive light from them (they are within the particle horizon) because light moves through curved spacetime. Causal contact depends on the event horizon, not v_rec.

**"Dark matter is just dark baryons (black holes, brown dwarfs)"**
Ruled out: BBN fixes baryon density to ~5% of the critical density. There simply aren't enough baryons to account for dark matter (27%). MACHOs (massive compact halo objects) are also constrained by microlensing surveys to be a small fraction of DM.

**"The CMB is the afterglow of the Big Bang explosion"**
The CMB was emitted 380,000 years after the Big Bang — not at the Big Bang itself. It's the photons released when the universe cooled enough for atoms to form (recombination). The 2.7K temperature is because those photons have been redshifted by factor ~1100 since then. We see the CMB as if looking at a spherical shell around us at z~1100.

**"Dark energy = dark matter"**
Completely different. Dark matter is clustered (forms halos, filaments) and non-relativistic. Dark energy is uniform throughout space and has negative pressure. They don't interact except gravitationally. The "dark" in both names just means electromagnetically transparent.

**"The cosmological constant problem is solved by supersymmetry"**
SUSY cancels some vacuum energy terms, reducing the discrepancy from 10¹²³ to ~10⁶⁰. Still off by 60 orders of magnitude. No proposed mechanism fully solves the cosmological constant problem — it remains one of the deepest unsolved problems at the interface of QFT and GR.
