# Stellar Physics
## Structure, Evolution, Nucleosynthesis, and Compact Objects

---

## 1. The Full Picture — Stars as Engines

```
  THE STAR LIFECYCLE MAP

  Molecular cloud
       │
       ▼  gravitational collapse (Jeans instability)
  Protostar → Pre-main sequence (Hayashi track, then Henyey track)
       │
       ▼  core T reaches ~10 MK → hydrogen ignites
  ZERO-AGE MAIN SEQUENCE (ZAMS)
       │
       ├─────────────────────────────────────────────────────────────────────┐
       │  M < ~8 M☉ (low/intermediate mass)                                 │ M > ~8 M☉ (massive)
       ▼                                                                     ▼
  Core H exhaustion                                              Much faster — core H out
       ▼                                                                     ▼
  Subgiant → Red Giant Branch (RGB)                          Red Supergiant / LBV / Wolf-Rayet
  (H shell burning, He core contracts)                           (He, C, Ne, O, Si shell burning)
       ▼                                                                     ▼
  Helium Flash (M < 2M☉) or smooth He ignition              Fe core accumulates → IRON WALL
       ▼                                                          (no exothermic fusion past Fe)
  Horizontal Branch (He core burning)                                        ▼
       ▼                                                         Core collapse (0.1 s implosion)
  Asymptotic Giant Branch (AGB)                                              ▼
  (He + H shell, thermal pulses)                              CORE BOUNCE → supernova shock
       ▼                                                                     ▼
  Mass loss → planetary nebula                               Type II/Ib/Ic supernova
       ▼                                                          ▼               ▼
  WHITE DWARF                                              NEUTRON STAR        BLACK HOLE
  (< 8 M☉ remnant, ~0.6 M☉)                               (M_rem < 3M☉)     (M_rem > 3M☉)
                                                          Pulsar, MSP, magnetar
```

**The physics in tension:** gravity wants to collapse the star; pressure (thermal, radiation, degeneracy) resists. The star's life is a sequence of nuclear fuel exhaustion events, with gravity winning each time — until it wins permanently.

---

## 2. Stellar Structure — The Four Equations

A star in spherical hydrostatic equilibrium is described by four coupled ODEs:

```
  HYDROSTATIC EQUILIBRIUM:
  ┌───────────────────────────────────────────────────────┐
  │  dP/dr = −G m(r) ρ(r) / r²                            │
  └───────────────────────────────────────────────────────┘
  Inward gravity of shell mass balanced by outward pressure gradient.
  m(r) = total mass interior to radius r.

  MASS CONTINUITY:
  ┌───────────────────────────────────────────────────────┐
  │  dm/dr = 4π r² ρ(r)                                   │
  └───────────────────────────────────────────────────────┘
  Trivial: mass in thin shell dr is 4πr²ρ dr.

  ENERGY TRANSPORT:
  ┌───────────────────────────────────────────────────────────────────────┐
  │  dT/dr = − (3 κ ρ L(r)) / (64π r² σ_SB T³)   [radiative]              │
  │  dT/dr = − (1 − 1/γ) T/P · dP/dr              [convective/adiabatic]│
  └───────────────────────────────────────────────────────────────────────┘
  κ = opacity [cm²/g]; σ_SB = Stefan-Boltzmann constant.
  The steeper gradient applies — if radiative gradient exceeds adiabatic,
  convection sets in (Schwarzschild criterion): ∇_rad > ∇_ad

  ENERGY GENERATION:
  ┌───────────────────────────────────────────────────────┐
  │  dL/dr = 4π r² ρ ε(r, T, ρ, composition)              │
  └───────────────────────────────────────────────────────┘
  ε = nuclear energy generation rate [erg/g/s], strong T-dependence.
```

### 2.1 The Virial Theorem — Why Gravity Has Negative Heat Capacity

```
  For a self-gravitating system in equilibrium:
  2K + U = 0     K = total kinetic (thermal) energy, U = gravitational PE

  Total energy: E = K + U = U/2 = −K

  COUNTERINTUITIVE RESULT:
  When a star contracts (loses energy, E decreases):
    → U decreases (more negative), but K INCREASES
    → the star gets HOTTER as it radiates energy away

  Kelvin-Helmholtz mechanism: gravitational contraction → temperature rise

  This is why pre-main-sequence stars heat up, why cores contract
  after fuel exhaustion, and why nuclear burning eventually ignites
  in the contracted core.
```

### 2.2 The Three Timescales

```
  DYNAMICAL TIMESCALE:  τ_dyn = 1/√(Gρ̄) ≈ (R³/GM)^(1/2)
    Sun: ~27 minutes
    Giant: hours to days
    White dwarf: ~10 seconds
    If pressure support removed → collapse in τ_dyn

  KELVIN-HELMHOLTZ TIMESCALE:  τ_KH = GM²/(RL)
    Sun: ~15 Myr
    (Before nuclear was known, Kelvin proposed this as solar age — wrong)
    Controls pre-MS contraction rate; also sets mass-loss response time

  NUCLEAR TIMESCALE:  τ_nuc = ε M / L  (fraction of mass available × efficiency)
    Sun: ~10 Gyr for H burning (10% of mass available, 0.7% mass→energy efficiency)
    20 M☉: ~8 Myr for H burning
    ∝ M / L ∝ M^(−2.5)  →  massive stars live much shorter

  HIERARCHY:  τ_dyn ≪ τ_KH ≪ τ_nuc
  → structure equilibrates faster than composition changes: quasi-static evolution
```

---

## 3. The Hertzsprung-Russell Diagram

### 3.1 Axes and Regions

```
  HERTZSPRUNG-RUSSELL DIAGRAM

  log L/L☉
    6 │         ●●  Supergiants (I)
      │       ●●●
    4 │          ●● Giants (III)
      │ ●●●●●●●●●●●●●●●
    2 │  ●●●●●●●●●●●●   ← Main Sequence
      │  ●●●●●●●        (ZAMS band)
    0 │  ●●●●
      │ ● Sun (G2V)  ●● Subgiants (IV)
   −2 │              ●●●●●● White Dwarfs
      │              ●●●●●
   −4 │──────────────────────────────────→ log T_eff (reversed)
      50000  20000   10000   6000   3000  K
        O      B       A     F G K       M

  KEY REGIONS:
  ┌──────────────────────────────────────────────────────────────────────┐
  │ Main Sequence:  hydrogen core burning; τ_nuc ∝ M^(−2.5)              │
  │ Red Giants:     H shell burning; greatly expanded envelope           │
  │ Horizontal Branch: He core burning (post-RGB helium flash)           │
  │ AGB:            He+H shell burning; thermal pulses; mass loss        │
  │ White Dwarfs:   cooling sequence; no nuclear burning; e⁻ degeneracy  │
  │ Instability Strip: Cepheid, RR Lyrae, Delta Scuti variables          │
  └──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Spectral Classification

```
  O B A F G K M  (L T Y for cool dwarfs/brown dwarfs, added later)
  "Oh Be A Fine Guy/Girl Kiss Me"

  Class   T_eff (K)   Color       Features              Examples
  ─────────────────────────────────────────────────────────────────────
  O       > 30,000    Blue-white  He II absorption       ζ Pup, Mintaka
  B       10–30,000   Blue-white  He I, H Balmer          Rigel, Spica
  A        7–10,000   White       Strong Balmer           Sirius, Vega
  F        6–7,000    Yellow-wht  Ca II, weaker Balmer    Procyon
  G        5–6,000    Yellow      Ca II K&H, Fe lines     Sun, Capella
  K        3.5–5,000  Orange      Neutral metals          Arcturus, Aldebaran
  M        < 3,500    Red         TiO molecular bands     Betelgeuse, Proxima
  ─────────────────────────────────────────────────────────────────────
  Luminosity classes (Roman numerals):
  Ia/Ib = supergiants, II = bright giants, III = giants,
  IV = subgiants, V = main sequence (dwarfs)
  Sun = G2V
```

### 3.3 Mass-Luminosity Relation and Stellar Lifetimes

```
  MAIN SEQUENCE: L ∝ M^n

  n ≈ 4    for solar-type (0.3–30 M☉)  — empirical power law
  n ≈ 3.5  for low-mass stars
  n ≈ 1    for M > ~60 M☉ (Eddington luminosity limit)

  L_Edd = 4πGMc/κ_es ≈ 1.26 × 10³⁸ (M/M☉) erg/s
  (electron scattering opacity limits radiation pressure to this value)

  STELLAR LIFETIMES: τ ∝ M/L ∝ M^(1−n) ≈ M^(−3)

  Star        Mass      τ_MS
  ─────────────────────────────────────────
  O5 V        40 M☉     ~3 Myr
  B0 V        15 M☉     ~12 Myr
  A0 V         3 M☉     ~400 Myr
  G2 V (Sun)   1 M☉     ~10 Gyr
  K5 V        0.7 M☉    ~30 Gyr
  M5 V        0.2 M☉    > 200 Gyr (older than universe)
  ─────────────────────────────────────────

  CLUSTER DATING — the turnoff point:
  A star cluster formed at the same time; plot all stars on HR diagram.
  The "main sequence turnoff" — where stars are just departing for the giant
  branch — corresponds to stars whose τ_MS ≈ cluster age.
  Fitting isochrones (theoretical evolutionary tracks) gives cluster age.
  Oldest globular clusters: ~13 Gyr (constrains minimum age of universe)
```

---

## 4. Nuclear Burning — Fuel Sequence

### 4.1 The Gamow Peak — Why Stars Can Fuse at All

Quantum tunneling + Maxwell-Boltzmann distribution create a narrow energy window:

```
  GAMOW PEAK (qualitative):

  Probability(E) ∝ e^(−E/kT)     ← Maxwell-Boltzmann (high E suppressed)
              ×  e^(−E_G/E)^(1/2) ← Gamow tunneling (low E suppressed)
                  E_G = Gamow energy ∝ Z₁²Z₂²

  Product has a peak at E_Gamow ≈ 1.22 (Z₁Z₂/A_r)^(2/3) T₆^(2/3)  keV

  Sun core: T ≈ 15.7 MK → kT ≈ 1.4 keV, Gamow peak for pp at ~6 keV
  Classical barrier for pp: ~550 keV → tunneling through factor 10^(−80)
  → quantum tunneling is the only reason stars burn slowly (not explosively)

  T-dependence of reaction rates (steep!):
  pp chain:   ε ∝ T⁴       (at solar T)
  CNO cycle:  ε ∝ T^17     (at solar T)
  Triple-α:   ε ∝ T^40     (at He burning T)
  → Small T change → huge rate change → stellar thermostat
```

### 4.2 The Proton-Proton Chain (pp chain)

Dominant for M ≲ 1.3 M☉, T_core ≲ 18 MK:

```
  THREE BRANCHES (all start with):
  p + p → D + e⁺ + ν_e          (slow! weak force, τ ~ 5 Gyr at solar core density)
  p + D → ³He + γ               (fast)

  PP I  (86% in Sun):
  ³He + ³He → ⁴He + 2p

  PP II (14% in Sun):
  ³He + ⁴He → ⁷Be + γ
  ⁷Be + e⁻  → ⁷Li + ν_e        ← solar neutrino problem (these ν detected)
  ⁷Li + p   → 2⁴He

  PP III (0.02% in Sun, but high-energy neutrinos):
  ⁷Be + p   → ⁸B + γ
  ⁸B        → ⁸Be + e⁺ + ν_e   ← SNO detected these, solved neutrino problem
  ⁸Be       → 2⁴He

  NET (all branches): 4p → ⁴He + 2e⁺ + 2ν + energy
  Q = 26.73 MeV per ⁴He formed (minus neutrino losses)
  Sun fuses ~600 million tons of H per second
```

### 4.3 The CNO Cycle

Dominant for M ≳ 1.3 M☉, T_core ≳ 18 MK. Carbon/nitrogen/oxygen act as catalysts:

```
  CNO BI-CYCLE (main branch):

  ¹²C + p → ¹³N + γ        (¹³N β⁺ decays quickly)
  ¹³C + p → ¹⁴N + γ        (bottleneck: ¹⁴N+p slowest step)
  ¹⁴N + p → ¹⁵O + γ        ← rate-limiting step (entire cycle speed)
  ¹⁵N + p → ¹²C + ⁴He      (catalyst recovered — but 0.04% goes ¹⁵N+p→¹⁶O+γ)

  Net: 4p → ⁴He + 2e⁺ + 2ν + 26.73 MeV   (same as pp, CNO just catalyzes)

  KEY: CNO converts ¹²C to ¹⁴N (¹⁴N+p is slowest step)
  → CNO-processed stellar material has ¹²C/¹⁴N ratio far below solar
  → Observed in spectra of evolved stars (CN anomalies, mixing signatures)
```

### 4.4 Helium Burning — The Triple-Alpha Process

After core H exhaustion, core contracts until T ≈ 100 MK:

```
  THE HOYLE RESONANCE PROBLEM:

  ⁴He + ⁴He → ⁸Be + γ        ⁸Be is UNSTABLE (τ ~ 10⁻¹⁶ s)
  ⁸Be + ⁴He → ¹²C + γ        requires resonance to work at stellar T

  Without a resonance at ~7.65 MeV in ¹²C, there would be essentially
  no carbon in the universe.

  Fred Hoyle (1953): predicted this resonance MUST exist from the existence
  of carbon-based life. Fowler and team found it at exactly 7.6549 MeV.
  First use of anthropic reasoning to make a successful prediction in physics.

  NET: 3⁴He → ¹²C + 7.27 MeV
  Plus: ¹²C + ⁴He → ¹⁶O + γ   (competes with triple-α, sets C/O ratio)
  The C/O ratio from He burning (~0.5-1) has profound implications for
  subsequent evolution and for the existence of rocky planets.
```

### 4.5 Advanced Burning Stages (Massive Stars Only)

After He exhaustion, the core contracts, heats further:

```
  BURNING STAGES IN A 20 M☉ STAR

  Stage        Fuel   Products      T_core     τ_stage
  ──────────────────────────────────────────────────────────────
  H burning    H      He            15 MK      ~8 Myr
  He burning   He     C, O          200 MK     ~0.8 Myr
  C burning    C      Ne, Mg, Na    700 MK     ~1000 yr
  Ne burning   Ne     O, Mg         1.5 GK     ~1 yr
  O burning    O      Si, S, Ar     2 GK       ~6 months
  Si burning   Si     Fe-peak (Ni)  5 GK       ~1 day (!)
  ──────────────────────────────────────────────────────────────
  Si burning = nuclear statistical equilibrium (NSE):
  At 5 GK, photons have enough energy to photodisintegrate nuclei;
  reactions go both ways; equilibrium favors the deepest nuclear binding
  energy: the iron-peak (⁵⁶Fe, ⁵⁶Ni, ⁵⁸Ni, ⁵⁴Cr...)

  THE IRON WALL:
  ⁵⁶Fe has the highest binding energy per nucleon (~8.8 MeV)
  Fusing beyond Fe is ENDOTHERMIC — energy cost, not yield
  → no radiation pressure support from Fe fusion
  → core collapses when Fe mass > Chandrasekhar limit (~1.4 M☉)

  ONION SHELL STRUCTURE just before collapse:
         ┌──────────────┐  ← H envelope
         │    He shell   │
         │   C/O shell   │
         │   Ne/Mg shell │
         │   O/Si shell  │
         │  Si/S shell   │
         │   Fe core     │  ← ~1.4 M☉, Earth-sized, about to collapse
         └──────────────┘
```

---

## 5. Nucleosynthesis — Origin of the Elements

**B²FH** (Burbidge, Burbidge, Fowler, Hoyle — 1957): laid out the framework for where every element comes from.

```
  NUCLEOSYNTHESIS CHANNELS

  Process        Location              Products          Key nuclei
  ──────────────────────────────────────────────────────────────────────────────
  Big Bang (BBN) First 3 minutes       H, ⁴He, D, ³He, ⁷Li  H (~75%), He (~25%)
  pp chain/CNO   All main-seq stars    ⁴He from H           He
  Triple-α       He-burning (AGB, MS)  ¹²C, ¹⁶O             C, O
  α-capture      Core/shell burning    Ne, Mg, Si, S, Ar, Ca, Ti, Cr, Fe
  s-process      AGB stars (low mass)  Sr→Ba→Pb (slow)      roughly Fe→Bi
  r-process      NS mergers + CC SN    Au, Pt, U, Th (fast)  roughly Fe→U
  p-process      SN shockwave          Proton-rich isotopes  rare p-nuclei
  Spallation     Cosmic ray + ISM      Li, Be, B            fragmentation
  ──────────────────────────────────────────────────────────────────────────────

  s-PROCESS (slow neutron capture):
  Neutron added slower than β-decay: n + ¹⁴N → ¹⁵N → ¹⁵O (etc.)
  AGB stars: neutrons from ¹³C(α,n)¹⁶O and ²²Ne(α,n)²⁵Mg reactions
  Builds a path along the valley of stability from Fe to Bi (~209)
  Cannot make anything heavier than ²⁰⁹Bi (alpha-unstable beyond)

  r-PROCESS (rapid neutron capture):
  Neutron flux so high (~10²² n/cm²/s) that nuclei capture before β-decay
  → far neutron-rich side of stability valley → highly exotic nuclei
  → β-decay back toward stability produces heavy r-process nuclei
  GW170817 (2017): kilonova spectrum showed Au, Pt, Eu — r-process confirmed
  in neutron star merger. ~10 Earth masses of r-process material produced.

  WHERE DID YOUR ELEMENTS COME FROM:
  H in your body:    Big Bang
  He in birthday balloons: Big Bang + stars
  O, C, N in you:    AGB stars + CC supernovae (previous stellar generations)
  Fe in your blood:  Type Ia supernova (WD+WD or WD+accretion → Chandrasekhar)
  Gold in jewelry:   Neutron star merger r-process (~all Au in universe)
  Ca in your bones:  CC supernovae (oxygen burning shell)
```

---

## 6. Compact Objects

### 6.1 White Dwarfs — Electron Degeneracy

```
  ELECTRON DEGENERACY PRESSURE:
  From Pauli exclusion + uncertainty principle (covered in physics/09-ZERO-POINT-ENERGY.md):
  Fermions cannot share quantum states → momentum spread even at T=0

  P_deg ∝ (ρ/μ_e)^(5/3)    [non-relativistic; μ_e = mean molecular weight per electron ≈ 2]
  P_deg ∝ (ρ/μ_e)^(4/3)    [ultra-relativistic; softer → less stable]

  KEY: degeneracy pressure is INDEPENDENT OF TEMPERATURE
  → WDs don't regulate temperature by burning — they just cool forever

  CHANDRASEKHAR LIMIT:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  M_Ch = 5.83 / μ_e² × M☉ ≈ 1.44 M☉    (μ_e ≈ 2 for He/C/O)        │
  └─────────────────────────────────────────────────────────────────────────┘
  At M > M_Ch: electrons become ultra-relativistic → P ∝ ρ^(4/3) → pressure
  cannot balance gravity → no equilibrium → collapse or Type Ia SN

  Derivation sketch:
  Hydrostatic: dP/dr ~ −GM²/R⁴ (from virial)
  Degeneracy: P ~ ℏ²/m_e × (ρ/m_H)^(5/3) ~ ℏ²/m_e × (M/R³)^(5/3)
  Setting dP ~ gravity → R ∝ M^(−1/3)
  → as M increases, R decreases (WDs get smaller when more massive)
  → R → 0 as M → M_Ch: the Chandrasekhar limit

  PROPERTIES:
  Typical mass:  0.6 M☉ (most WDs end here from ~2-8 M☉ progenitors)
  Typical radius: ~R_Earth (~7000 km)
  Density:       ~10⁶ g/cm³ (teaspoon ~ 5 tons)
  Composition:   C/O core (C/O WD), He envelope, H atmosphere (DA type)
  Cooling time:  ~10 Gyr to cool below visibility → "cold black dwarfs"
                (none exist yet — universe too young)

  TYPE Ia SUPERNOVA:
  WD in binary system accretes from companion → approaches M_Ch
  → thermonuclear runaway (C ignition at ~1 GK, degenerate → no regulation)
  → entire star consumed in ~1 second
  → nearly uniform peak luminosity: L_peak ~ 10⁴³ erg/s (10¹⁰ L☉)
  → standard candle for cosmology
  → powered by: ⁵⁶Ni (→⁵⁶Co→⁵⁶Fe) decay, τ ~ 8.8 days → light curve shape
  Perlmutter + Schmidt + Riess (1998): Type Ia SNe dimmer than expected
  → universe expansion is ACCELERATING → dark energy (Nobel 2011)
```

### 6.2 Neutron Stars — Nuclear Density

```
  FORMATION: Fe core collapse when M_Fe > M_Ch
  ─────────────────────────────────────────────────────────────────────────
  1. Photodisintegration: γ + ⁵⁶Fe → 13⁴He + 4n   (endothermic, removes pressure)
  2. Neutronization:      p + e⁻ → n + ν_e          (removes electrons + emits ν)
  3. Core collapse:       ~0.1 s implosion to nuclear density
  4. Core bounce:         nuclear repulsion at ρ ~ 3×10¹⁴ g/cm³ → outward shock
  5. Neutrino heating:    99% of SN energy in ν's; ~1% heats shock → explosion

  Neutrino luminosity during collapse: ~3×10⁵³ erg (10× Sun's 10-Gyr output)
  in ~10 seconds. SN 1987A: 24 neutrinos detected at Earth (17 kpc away).

  PROPERTIES:
  Mass:     1.4–2.5 M☉ (typical ~1.4 M☉; max uncertain, EOS-dependent)
  Radius:   ~10–12 km
  Density:  ~3×10¹⁴ g/cm³ (nuclear density; teaspoon ~ mass of Everest)
  B field:  10⁸–10¹² T (born magnetized; old pulsars lower B)
  Spin:     ~ms (milliseconds) to ~seconds at birth (young: 10-100 ms)

  TOV EQUATION (GR hydrostatic equilibrium):
  ┌────────────────────────────────────────────────────────────────────────┐
  │  dP/dr = −(ε + P)(m + 4πr³P/c²)  ×  G / (r²c² (1 − 2Gm/rc²))      │
  │                                                                        │
  │  Newtonian: dP/dr = −Gm ρ/r²                                           │
  │  GR additions: (ε+P) instead of ρ  [energy density + pressure]         │
  │               (m + 4πr³P/c²)      [effective gravitating mass + P]     │
  │               (1 − 2Gm/rc²)       [curved spacetime near center]       │
  └────────────────────────────────────────────────────────────────────────┘
  Maximum NS mass from TOV: ~2–3 M☉ (uncertain because nuclear EOS unknown)
  Observed: PSR J0952-0607 at 2.35 M☉ (2022) — near the theoretical ceiling

  PULSARS:
  Rotating NS + misaligned magnetic dipole → lighthouse emission
  ─────────────────────────────────────────────────────────────────────────
  Spin-down: E_rot lost → EM radiation; Ṗ/P gives B field estimate
  B ~ 3.2×10¹⁹ G √(P · Ṗ)    [Gaussian units]

  P–Ṗ DIAGRAM (key diagnostic):
  log Ṗ                        ●  ← magnetars (ultra-high B, soft gamma repeaters)
     │           ●●            ●● ← young pulsars (Crab, Vela)
     │      ●●●●●●●
     │    ●●●●●●●●
     │  ●●●●●● ← pulsar "graveyard" (too slow/low B to emit)
     │
     └───────────────────────────── log P
          ●●●●  ← ms pulsars (recycled by accretion, B weakened)

  Millisecond Pulsars (MSP): spun up by accreting matter from binary companion
  → fastest: PSR J1748-2446ad at 716 Hz (1.4 ms period)
  → timing precision rivals atomic clocks
  → PTA (Pulsar Timing Array): using MSPs to detect gravitational waves (NANOGrav)
```

### 6.3 Black Holes — Compact Remnants Beyond Neutrons

```
  FORMATION: neutron star cannot form if M_rem > ~3 M☉
  (or "failed SN" — collapse without explosion for very massive progenitors)

  SCHWARZSCHILD BLACK HOLE (non-rotating):
  ┌────────────────────────────────────────────────────────────────────┐
  │  Schwarzschild radius:  r_s = 2GM/c²                               │
  │  Sun:     r_s = 3.0 km                                             │
  │  Earth:   r_s = 8.9 mm                                             │
  │  10 M☉:   r_s = 30 km                                              │
  └────────────────────────────────────────────────────────────────────┘

  Event horizon: surface of no return; not a physical surface, a causal boundary
  Singularity: r = 0, classical GR breaks down; quantum gravity required

  KERR BLACK HOLE (rotating — astrophysically relevant):
  Most astrophysical BHs rotate. Kerr metric adds spin parameter a = J/(Mc)
  Ergosphere: region outside horizon where spacetime rotation drags everything
  ISCO (Innermost Stable Circular Orbit):
    Schwarzschild: r_ISCO = 3 r_s = 6GM/c²
    Maximally spinning: r_ISCO → 0.5 r_s (retrograde) or r_s/2 (prograde)
  → spin determines accretion efficiency: up to ~42% for max spin vs 6% Schwarzschild

  HAWKING RADIATION:
  T_H = ℏ c³ / (8π G M k_B) ≈ 6×10⁻⁸ (M☉/M) K

  10 M☉ BH:     T_H ~ 6×10⁻⁹ K        (utterly negligible)
  M = 10¹⁵ g:   T_H ~ 100 MeV         (primordial BH, evaporating now)
  Stellar BHs never evaporate in any cosmological timescale (CMB 2.7K > T_H)

  STELLAR BH CLASSES:
  ─────────────────────────────────────────────────────────────────────────
  Stellar mass BH:   5–100 M☉         CC SN or direct collapse; BH+BH mergers
  Intermediate:      100–10⁵ M☉       uncertain origin; in some globular clusters
  Supermassive (SMBH): 10⁶–10¹⁰ M☉   galactic centers; accrete as AGN/quasars
  ─────────────────────────────────────────────────────────────────────────
  Sgr A* (Milky Way center): 4.15×10⁶ M☉ (orbit of S2 star; Nobel 2020 Genzel/Ghez)
  M87* (EHT imaged 2019): 6.5×10⁹ M☉, 55 Mly away
```

---

## 7. Supernovae — Taxonomy

```
  TYPE      SPECTRUM          CAUSE                        Key Product
  ──────────────────────────────────────────────────────────────────────────
  Ia        no H, no He,      WD → Chandrasekhar limit     ⁵⁶Ni (→Fe), no remnant
            Si II at 6150Å    thermonuclear runaway         (standard candle)
  Ib        no H, He present  Massive star, H-stripped      NS/BH remnant
  Ic        no H, no He       Massive star, H+He stripped   NS/BH remnant (WR progenitor)
  II        H present         Core collapse, massive star   NS/BH remnant
   IIP      plateau in LC     Extended H envelope           NS
   IIb      H then He         Partial H stripping           NS
  ──────────────────────────────────────────────────────────────────────────

  ENERGETICS (core collapse):
  Total energy released:  ~3×10⁵³ erg  (99% in neutrinos)
  Optical energy:         ~10⁵¹ erg    ("one Bethe" = 1 foe)
  Kinetic energy of ejecta: ~10⁵¹ erg
  Peak optical luminosity: ~10¹⁰ L☉ for weeks → visible in daytime historically
  (SN 1006, SN 1054/Crab, Tycho 1572, Kepler 1604, SN 1987A)

  SN 1987A: only naked-eye SN since 1604; ~170,000 ly in LMC
  23 neutrinos detected (Kamiokande, IMB, Baksan) — confirmed core-collapse theory
  Central compact object still unconfirmed (dust-obscured; possibly NS)

  RATE:
  Milky Way: ~2 core-collapse SN per century (most dust-obscured)
  Type Ia: ~0.3 per century per Milky-Way-sized galaxy
  Closest Type Ia risk: no WD near Chandrasekhar limit within threat distance
```

---

## 8. Stellar Populations

```
  STELLAR POPULATIONS: metallicity + age + location

  ┌─────────────────────────────────────────────────────────────────────────┐
  │          Pop I          Pop II          Pop III                         │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ Metallicity  High (Z ~ Z☉) Low (Z < 0.01 Z☉) Zero (Z = 0)            │
  │ Age          Young (<1-2 Gyr) Old (>10 Gyr)   First stars (~200 Myr)  │
  │ Location     Disk, spiral arms Halo, bulge, GC Unknown — undetected    │
  │ Examples     Sun, Pleiades    Globular cluster  Predicted, not observed │
  │                               stars, metal-poor                        │
  │ Origin       Multiple SN      Early galaxy      Primordial H+He only   │
  │              enrichment       formation         (no metals to form dust)│
  ├─────────────────────────────────────────────────────────────────────────┤
  │ "Metallicity" in astronomy = everything heavier than He                 │
  │ Z☉ ≈ 0.0142 (1.42% of solar mass in elements heavier than He)           │
  └─────────────────────────────────────────────────────────────────────────┘

  POP III STARS: theoretical first stars (z ~ 20-30, ~200 Myr after BB)
  No metals → no dust cooling → very high Jeans mass → massive (100-1000 M☉)
  → die as direct-collapse BHs or pair-instability SN
  → seed early ISM with metals for Pop II formation
  → JWST searching for signatures via extreme UV emission lines
```

---

## Decision Cheat Sheet

```
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Question                               │ Answer                            │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What supports a star against collapse? │ Main seq: thermal (gas+radiation) │
  │                                        │ WD: e⁻ degeneracy                │
  │                                        │ NS: neutron deg + nuclear repulse │
  │                                        │ BH: nothing → collapsed           │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What kills a WD?                       │ Accumulate > M_Ch (~1.44 M☉)      │
  │                                        │ → Type Ia SN                      │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why does a star heat up when it        │ Virial theorem: negative heat      │
  │ contracts (loses energy)?              │ capacity of gravity                │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What ends the main sequence?           │ Core H exhaustion; core contracts;│
  │                                        │ H shell ignites; star expands     │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why does He burning have triple-alpha? │ ⁸Be is unstable; needs resonance  │
  │ Why is the Hoyle state remarkable?     │ Predicted from existence of C life │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Where does gold come from?             │ r-process in neutron star mergers │
  │ Where does Fe come from?               │ Type Ia SN (⁵⁶Ni→⁵⁶Co→⁵⁶Fe)       │
  │ Where does C come from?                │ Triple-α in He-burning stars      │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What is the turnoff point?             │ Stars just leaving main sequence;  │
  │                                        │ τ_MS = cluster age → dating method │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ How does Type Ia constrain cosmology?  │ Standard candle (uniform L_peak); │
  │                                        │ used to discover dark energy 1998 │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why is Fe the nuclear endpoint?        │ Highest binding energy per nucleon │
  │                                        │ (~8.8 MeV); fusion past it costs   │
  │                                        │ energy → no pressure support       │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Which nuclear chain dominates in Sun?  │ pp chain (~99%); CNO ~1%          │
  │ Which dominates in more massive stars? │ CNO (ε_CNO ∝ T^17 >> pp at T>18MK)│
  └────────────────────────────────────────┴───────────────────────────────────┘
```

---

## Common Confusion Points

**"The Sun will explode as a supernova"**
No. The Sun is 1 M☉ — far below the ~8 M☉ threshold for core collapse. It will become a red giant (in ~5 Gyr), lose its envelope as a planetary nebula, and leave a 0.6 M☉ white dwarf. Only stars above ~8 M☉ die as supernovae.

**"Neutron stars are made of neutrons"**
Outer layers: neutron-rich nuclei in a neutron drip lattice. Inner core: free neutrons + protons + electrons. Possibly at highest densities: hyperons, deconfined quark matter (QCD). The equation of state (EOS) of dense matter is an open problem — that's why the maximum NS mass is uncertain, and why NS merger observations (GW170817) are so valuable.

**"A black hole sucks in everything around it"**
No. At large distances, a BH of mass M is gravitationally identical to any other object of mass M. If the Sun were replaced by a 1 M☉ BH, Earth's orbit would be unchanged. BHs are dangerous only near the event horizon. Stars orbit supermassive BHs for billions of years.

**"The Chandrasekhar limit is why Type Ia SNe are standard candles"**
Approximately true but oversimplified. All Ia SNe detonate near M_Ch → similar amounts of ⁵⁶Ni → similar luminosity. But the actual standard candle comes from the Phillips relation (1993): broader light curve = more luminous. The width-luminosity relation allows calibration to ~5% precision. Pure M_Ch uniformity would only get you to ~15%.

**"Fe is the heaviest element made in stars"**
Stars make up to the iron peak (Fe, Ni, Co). But s-process on the AGB makes elements up to Pb/Bi (~Z=83) and r-process makes everything up to U/Th (Z=92+). These form in stars but through neutron capture on Fe seeds, not direct fusion. Elements *beyond* the iron peak require neutron capture, not additional fusion.

**"Fusion is easy — just smash nuclei together"**
Coulomb barrier: two protons repel each other with ~550 keV peak barrier. Stellar cores are at ~1–10 keV (kT). Fusion only happens via quantum tunneling through the tail of the Maxwell-Boltzmann distribution (Gamow peak). This is why the pp reaction is so slow (τ ~ 5 Gyr for a proton at solar core conditions) — without that slowness, the Sun would have burned out in millions of years.

**"Hawking radiation will destroy black holes soon"**
Only for very small primordial black holes (M ~ 10¹⁵ g, Planck-mass range). Stellar black holes (M > 3 M☉) have T_H < 10⁻⁸ K — far below the CMB temperature of 2.7 K — so they actually *absorb* more CMB photons than they radiate. They will not begin net evaporation until the universe cools below their T_H — in ~10^64 years for stellar BHs.
