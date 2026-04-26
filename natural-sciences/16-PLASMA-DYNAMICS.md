# 16-PLASMA-DYNAMICS — Plasma Dynamics & Confinement

> MHD instabilities, magnetic reconnection, tokamaks, stellarators,
> inertial confinement, astrophysical plasmas, and industrial applications.
> Where plasma physics meets engineering and astrophysics.

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PLASMA DYNAMICS & CONFINEMENT                    │
│                                                                     │
│  MHD EQUILIBRIUM                                                    │
│  ─────────────────                                                  │
│  J × B = ∇p (force balance)    β = p / (B²/2µ₀)                     │
│  Grad-Shafranov equation        Flux surfaces, q safety factor      │
│          │                                                          │
│          ▼                                                          │
│  MHD INSTABILITIES (perturbation grows if energy is released)       │
│  ─────────────────────────────────────────────────────────────      │
│  Interchange / RT:  bad curvature → density finger penetrates       │
│  Kink (m=1):        current column bends → j×B amplifies bend       │
│  Tearing:           resistive layer → magnetic island formation     │
│  NTM:               bootstrap current loss → self-reinforcing island│
│  Disruption:        catastrophic confinement loss (ms timescale)    │
│          │                                                          │
│          ▼                                                          │
│  MAGNETIC RECONNECTION                                              │
│  ────────────────────────                                           │
│  Topology change at X-point     Sweet-Parker vs. Petschek rate      │
│  Converts B-field energy → heat + jets + particle acceleration      │
│          │                                                          │
│     ┌────┴──────────────────────────────────┐                       │
│     ▼                                        ▼                       │
│  MAGNETIC CONFINEMENT               INERTIAL CONFINEMENT            │
│  ─────────────────────               ────────────────────           │
│  Tokamak: helical B, plasma current  ICF: compress D-T capsule      │
│  Stellarator: external helicity only fast → fusion before disassem  │
│  Lawson criterion: nTτ_E threshold  RT instability is key challenge │
│          │                                                           │
│     ┌────┴──────────────────────────────────┐                       │
│     ▼                                        ▼                      │
│  ASTROPHYSICAL PLASMAS              INDUSTRIAL APPLICATIONS         │
│  ──────────────────────              ────────────────────────       │
│  Solar flares, CMEs, substorms       Plasma etching (chips)         │
│  Accretion disks (MRI transport)     Sputtering deposition          │
│  Pulsar/AGN jets                     Ion thrusters (SpaceX, Dawn)   │
│  Radiation belts                     Arc furnaces                   │
└─────────────────────────────────────────────────────────────────────┘

Reading path: equilibrium → what breaks it (instabilities) →
catastrophic topology change (reconnection) → confinement strategies →
applications where same physics appears.
```

---

## MHD Equilibrium

Before instability: what is the equilibrium?

```
Force balance in magnetized plasma:
  J × B = ∇p

  Magnetic pressure:  p_mag = B²/2µ₀
  Magnetic tension:   T = B²/µ₀ (along field lines)
  Thermal pressure:   p = nk_BT

∇(p + B²/2µ₀) = (B·∇)B/µ₀    (gradient of total pressure = tension)

β = p/(B²/2µ₀) = plasma pressure / magnetic pressure
  Low β: magnetic forces dominate (fusion devices: β ~ 1–10%)
  High β: thermal pressure dominates (astrophysical: β >> 1 in some regions)

Flux surfaces (tokamak):
  Nested toroidal surfaces where B lies tangent to surface
  Pressure gradient drives current; current creates confining field
  Grad-Shafranov equation: Δ*ψ = −µ₀R² dp/dψ − F dF/dψ
    (elliptic PDE for poloidal flux ψ in axisymmetric geometry)
```

---

## MHD Instabilities

Instabilities are perturbations that grow exponentially, limited by nonlinear effects.
Classified by energy source: pressure gradient, current, free energy in topology.

### Interchange and Rayleigh-Taylor

```
Rayleigh-Taylor (RT) instability:
  Heavy fluid on top of light fluid in gravity → fingers penetrate
  Plasma analog: dense plasma supported against gravity (or centrifugal) by B-field
  Growth rate: γ_RT = √(g·k_⊥) (k = wavenumber of perturbation)

Flute/interchange instability:
  Plasma at unfavorable curvature (concave side of field lines)
  "Bad curvature" → ∇B points into plasma → unstable
  "Good curvature" → ∇B points away from plasma → stable
  Minimum-B configuration stabilizes RT

Examples:
  ICF implosion: RT at ablation front and fuel-pusher interface → limits compression
  Sausage instability (m=0): uniform pinch squeezes → constricts → pinches off
  Kink instability (m=1): current-carrying plasma bends → j×B amplifies bend
```

### Kink (m=1) Instability — Kruskal-Shafranov Criterion

```
A cylindrical plasma column carrying current kinks if field line pitch is too shallow.

Safety factor: q = rBφ/(RBθ)  (ratio of toroidal to poloidal field winding)
  q > 1 everywhere: Kruskal-Shafranov criterion → kink stabilized
  q < 1 at some radius → kink unstable → "sawtooth" oscillations in tokamak center

Tokamak design: q > 2–3 at edge, q ~ 1 in core (sawteeth acceptable)
  q < 1 core: internal kink → sawtooth crash (periodic reconnection)
  q = 1.5 (rational surface): neoclassical tearing mode (NTM)
  q = 2 (rational surface): external kink / disruption risk
```

### Tearing Mode and Magnetic Islands

```
At rational surfaces q = m/n: field line closes after m toroidal + n poloidal transits

Tearing mode: resistivity allows field lines to tear and reconnect at rational surface
  → magnetic islands form (O-point + X-point topology)
  → island width w ∝ √(current gradient)

Neoclassical tearing mode (NTM):
  Bootstrap current (pressure-driven current in tokamak) lost inside island
  → self-reinforcing island growth → confinement degradation
  Control: electron cyclotron current drive (ECCD) deposited at island O-point

Disruption: sudden loss of confinement (ms timescale)
  Causes: density limit (Greenwald), beta limit, VDE (vertical displacement event)
  Effects: thermal quench (plasma cools → current quench → large halo currents)
  → structural damage to vacuum vessel → major concern for ITER/reactors
```

---

## Magnetic Reconnection

Topology change of field lines — converts magnetic energy to kinetic and thermal energy.

```
WITHOUT RECONNECTION (ideal MHD):
  Field lines frozen to plasma → anti-parallel field lines can't merge
  → no energy release despite large gradient

WITH RECONNECTION (resistive MHD, thin current sheet):
  Thin current sheet (Sweet-Parker layer thickness δ ~ L/√S)
  → resistive diffusion breaks frozen-flux condition at reconnection point (X-point)
  → field line topology changes → field energy → outflow jets + heating

Sweet-Parker reconnection rate:
  v_in / v_A = 1/√(S)   (S = Lundquist number = v_A L/η_m ~ 10⁸–10¹²)
  → VERY SLOW: for S = 10¹², v_in/v_A = 10⁻⁶ → too slow for solar flares

Petschek reconnection: localized X-point with standing slow shocks → v_in/v_A ~ 1/ln(S)
  → much faster, but requires special conditions

Fast reconnection (observations):
  Actual reconnection in solar flares: Alfvénic timescale (fast) — observations confirmed
  Mechanism: plasmoid instability (large S → thin layer → tearing → plasmoid chains → fast)
  Collisionless effects: Hall MHD, electron inertia → bypasses resistive constraint

ASTROPHYSICAL IMPORTANCE:
  Solar flares: 10²⁵ J released in minutes (stored B-field energy)
  Coronal mass ejections (CMEs): reconnection triggers eruption → ~10²⁴ J
  Magnetospheric substorms: dayside + nightside reconnection → auroras
  Pulsar wind nebulae: striped wind reconnection → particle acceleration
```

---

## Tokamak Confinement

### Geometry

```
TOKAMAK = toroidal magnetic confinement device (Soviet acronym: toroidal chamber + magnetic coils)

  Toroidal field (Bφ): from external TF coils (dominant, ~5 T in ITER)
  Poloidal field (Bθ): from plasma current (OHMIC heating coil drives plasma current)
  Combined: helical field lines winding around torus → closed flux surfaces

Cross-section (ITER-like):
  R (major radius) = 6.2 m,  a (minor radius) = 2.0 m,  κ (elongation) = 1.85

  ┌──────────────────────────────┐
  │    Plasma (D-shaped cross-   │
  │    section, elongated)       │
  │    ○ ← magnetic axis         │
  │    Nested flux surfaces      │
  │    X-point (divertor)        │
  └──────────────────────────────┘

Safety factor: q = (1/2π) ∮ (Bφ/RBθ) dθ  ≈ a Bφ/(R Bθ)
  Core: q ≈ 1,  Edge: q > 3
```

### Heating Methods

```
Ohmic heating:  P = I²R (plasma resistivity η ∝ T^(-3/2))
  → resistivity falls with temperature → Ohmic heating self-limiting
  → useful to T ~ 10–20 keV; not sufficient for ignition

Neutral beam injection (NBI):  accelerate D or H ions → neutralize → inject
  → ions traverse B-field (neutral), re-ionize inside plasma → heat by collisions
  → also drives toroidal rotation (shear stabilizes turbulence)

Ion cyclotron resonance heating (ICRH): RF waves at Ωᵢ (30–100 MHz in tokamaks)
  → resonant absorption by minority ions → fast ion population → Coulomb collisions → heat

Electron cyclotron resonance heating (ECRH): mm-waves at Ωₑ (~100–200 GHz)
  → resonant absorption by electrons → direct electron heating
  → also used for current drive (ECCD): drives localized current → NTM control
```

### Energy Confinement and Lawson Criterion

```
Lawson criterion for fusion energy gain:
  n τ_E T > triple product threshold

  D-T fusion: n τ_E > 10²⁰ m⁻³·s  (at T ~ 10–20 keV)
  Or: n T τ_E > 3 × 10²¹ keV·m⁻³·s  (triple product)

  τ_E = energy confinement time = W / P_loss  (stored energy / loss power)

Q-factor: Q = P_fusion / P_heating
  Q < 1: net energy input
  Q = 1: break-even (JET record: Q ~ 0.67)
  Q > 1: net energy gain
  Q = ∞: ignition (alpha heating sustains plasma without external heating)

ITER target: Q ≥ 10  (500 MW fusion from 50 MW heating)
DEMO / reactor: Q >> 10, continuous operation, tritium breeding blanket

Empirical scaling (IPB98(y,2)):
  τ_E ∝ I_p^0.93 B_T^0.15 n^0.41 P^(-0.69) R^1.97 κ^0.78 ...
  → larger, more current, denser → longer confinement
```

---

## Stellarator

Alternative to tokamak: no plasma current → no disruptions.

```
TOKAMAK vs STELLARATOR:

Feature            Tokamak                Stellarator
──────────────────────────────────────────────────────────────────
Plasma current     Large (MA-scale)       Zero (or small)
Disruptions        Yes — major concern    No (no current → no kink)
Steady-state       Requires non-inductive Naturally steady-state
  operation        CD (bootstrap, NBI, ECCD)
Confinement        Good (database)        Slightly worse (historically)
Geometry           Axisymmetric           Non-axisymmetric (complex coils)
Complexity         Simpler plasma physics Complex coil engineering
Key example        JET, ITER, DEMO        W7-X (Greifswald, Germany), HSX, LHD

W7-X (Wendelstein 7-X): most advanced stellarator, optimized for neoclassical transport
  50 non-planar superconducting coils, plasma volume ~30 m³
  First "optimized" stellarator — demonstrates feasibility of stellarator path to fusion
```

---

## Inertial Confinement Fusion (ICF)

Compress and heat D-T capsule so fast that fusion occurs before plasma disassembles.

```
IGNITION CONDITION: αρR > 0.3 g/cm²   (areal density × alpha stopping range)

NIF (National Ignition Facility):
  192 UV laser beams, 1.8 MJ, 3 ns pulse
  Indirect drive: lasers heat hohlraum (gold cylinder) → X-rays → ablate outer capsule
    → rocket reaction → compression → central hot spot + main fuel layer

  Implosion physics:
    Convergence ratio: ~30× (initial radius / final radius)
    Ablation pressure: ~100 Mbar
    Stagnation: kinetic energy → thermal energy → fusion

  Rayleigh-Taylor instability: major challenge
    At ablation front: pressure-driven RT during acceleration phase
    At fuel-pusher interface: deceleration phase RT
    Seeded by: laser non-uniformity, capsule surface roughness, fill tube, tent

  NIF ignition milestone (December 2022): 2.05 MJ fusion yield from 2.05 MJ laser input
    Q (laser-plasma) = 1.0 — first demonstration of ignition
    Q (wall-plug) << 1 (lasers ~3% efficient) — not yet energy-relevant
    Scientific ignition: yes; commercial viability: far future

DIRECT DRIVE alternative: lasers directly ablate capsule (no hohlraum)
  More efficient coupling, but requires more uniform illumination
```

---

## Astrophysical Plasmas

### Solar Wind and Magnetosphere

```
Solar wind: continuous outflow of coronal plasma (Parker, 1958)
  Speed: ~400 km/s (slow) to ~800 km/s (fast) at 1 AU
  Density at 1 AU: ~5–10 cm⁻³
  Temperature: T_e ~ 10 eV, T_i ~ 5 eV
  Structure: sector structure from rotating Sun + helmet streamers

Parker spiral: field lines frozen to solar wind → spiral from solar rotation
  Angle at 1 AU: ~45° to radial (Earth-Sun line)
  R² (r/R_☉)² · B_r = const  (flux conservation)

Magnetosphere:
  Bow shock: supersonic solar wind → standing shock ~15 R_E upstream
  Magnetopause: pressure balance: B²/2µ₀ + n_sw m v_sw² → standoff ~10 R_E
  Magnetotail: stretched night-side field → current sheet → reconnection → substorms
  Radiation belts (Van Allen): trapped particles in Earth's dipole field
    Inner belt: protons (E > 10 MeV) from cosmic ray albedo neutron decay (CRAND)
    Outer belt: electrons (E ~ 0.1–10 MeV) from injections + wave acceleration
```

### Solar Flares and CMEs

```
Solar flare:
  Rapid release of magnetic energy stored in coronal field (10²⁴–10²⁵ J in minutes)
  Standard model (CSHKP): flux rope rises → stretched field → current sheet → reconnection
  Energy partition: ~30% radiation, ~20% particle acceleration, ~50% kinetic + thermal

  Classifications: A, B, C, M, X (each 10× more intense)
  X-class flares: peak X-ray flux > 10⁻⁴ W/m² (GOES band: 1–8 Å)
  Carrington Event (1859): estimated X40+ → telegraph systems failed worldwide

Coronal Mass Ejections (CMEs):
  ~10¹²–10¹³ kg plasma ejected at 100–3000 km/s
  10–100× more energy than flares; arrive at Earth in 1–3 days
  Geoeffective CME: southward B_z → reconnects with Earth's field → geomagnetic storm
  Dst index: measures ring current intensification (Dst < −50 nT: moderate storm)
  Extreme events: Dst < −500 nT (Carrington equivalent) → power grid damage
```

### Accretion Disks and Jets

```
Accretion disk: infalling gas forms rotating disk around compact object (BH, NS, WD)
  Angular momentum transport: MRI (magnetorotational instability — Balbus-Hawley 1991)
    Weak B-field + differential rotation → amplify field → Maxwell stress → angular momentum outward
    → mass inflows inward → accretion → converts gravitational PE to radiation
  Efficiency: η = Δ(mc²)/mc² → η ≈ 6–42% (Schwarzschild to maximally spinning Kerr BH)
  Luminosity: L = η ṁ c²  (up to 10× more efficient than nuclear burning!)

Relativistic jets:
  Collimated plasma outflows at ~0.99c from active galactic nuclei (AGN) and GRBs
  Length: up to Mpc (>10²² m) for powerful FR-II radio galaxies
  Power source: Blandford-Znajek: rotating BH extracts rotational energy via B-field
  Composition: electrons + positrons? or electrons + protons? (debated)
  Confinement: hoop stress from toroidal B-field, ambient pressure
```

---

## Industrial Plasma Applications

```
Application              Plasma type        Key physics
──────────────────────────────────────────────────────────────────
Silicon etching (chips)  Capacitively coupled RF, Ion bombardment + radical
                         3–100 mTorr         chemistry → anisotropic etch
Physical vapor dep.      DC/RF magnetron      Sputtering: Ar⁺ → target → film
  (PVD sputtering)       at target           Substrate B-field traps electrons
Plasma-enhanced CVD      CW or pulsed RF     Dissociation → reactive radicals
  (PECVD: SiN, SiO₂)                         → film deposition at low T
Plasma sterilization     Atmospheric DBD      O, OH, UV, H₂O₂ → inactivate pathogens
Ion thruster (electric   Gridded Xenon ECR   Xe ionized → extracted by grid →
  propulsion)                                thrust (Isp ~3000 s vs 400 s chemical)
Hall thruster (SpaceX    Crossed E×B         E×B drift → ionization + acceleration
  Starlink, Dawn)        discharge            High Isp, low thrust, efficient for Δv
Arc furnace (steel)      DC arc              High-current plasma arcs → resistive
                         5–30 MW              heating → melt scrap steel
```

---

## Decision Cheat Sheet

| Question | Concept | Key criterion |
|----------|---------|--------------|
| When does a pinch kink? | Kruskal-Shafranov | q < 1 → kink unstable |
| Why do tokamaks have D-shaped cross-sections? | MHD stability | Elongation improves β-limit; triangularity stabilizes edge |
| Why is Q = 1 important for NIF? | Fusion ignition | First time fusion yield ≥ laser input energy (2022) |
| What drives angular momentum transport in accretion disks? | MRI | Weak B + differential rotation → turbulence → outward AM transport |
| Why do solar flares release energy so fast? | Reconnection | Plasmoid-unstable current sheet → fast reconnection → Alfvénic energy release |
| Why doesn't stellarator disrupt? | No plasma current | Kink instability requires current; stellarator externally provides helicity |
| What accelerates particles in Earth's radiation belts? | Wave-particle resonance | Whistler-mode chorus waves accelerate electrons at cyclotron resonance |
| Why are ion thrusters efficient? | High exhaust velocity | Isp = v_exhaust/g → xenon accelerated to 30+ km/s vs 4 km/s chemical |
| What limits tokamak beta? | Ideal MHD β-limit | Troyon limit: β_N < 2.8–3.5 (normalized beta); above → ballooning/kink |

---

## Common Confusion Points

**Fusion energy is not the same as atomic bomb physics**
Fission bombs: heavy nuclei (U, Pu) split → uncontrolled chain reaction.
Fusion (H-bomb): requires fission trigger → not practical for commercial energy.
Tokamak/ICF fusion: D-T (light nuclei) → cannot produce runaway chain reaction
— stopping heating immediately stops fusion. No meltdown scenario.

**ITER is not a power plant**
ITER (under construction, Cadarache, France): physics experiment. Q ≥ 10.
Produces 500 MW thermal but converts ZERO to electricity.
First power-producing reactors: DEMO (~2050s, planned), then commercial plants.
NIF ignition (2022) is scientific proof-of-concept, not a power source.

**Magnetic reconnection is not the same as field annihilation**
Reconnection changes field topology but conserves magnetic helicity (Woltjer's theorem
in ideal MHD; quasi-conserved in resistive MHD for high S).
Field lines don't disappear — they reconnect into lower-energy configuration
and release the excess energy as plasma heating and kinetic energy.

**Plasma beta varies enormously across settings**
Tokamak: β ~ 1–10% (magnetically dominated → MHD stable)
Solar corona: β < 1 (magnetically dominated → B controls structure)
Solar wind at 1 AU: β ~ 1 (comparable thermal and magnetic pressure)
Accretion disk midplane: β >> 1 (thermally dominated)
ICF hotspot at ignition: β >> 1
"Low β" and "high β" plasmas have qualitatively different instability regimes.

**The "plasma confinement problem" is turbulent transport, not equilibrium**
Grad-Shafranov equilibrium is solved (analytically for simple, numerically for real tokamaks).
The unsolved problem is anomalous cross-field transport from micro-turbulence
(drift waves, ITG modes) that exceeds classical predictions by 10–100×.
Gyrokinetic simulation (GYRO, GS2, CGYRO) is the state-of-the-art tool —
orders of magnitude more expensive than MHD codes.
