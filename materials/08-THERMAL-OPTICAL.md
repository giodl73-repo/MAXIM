# Thermal and Optical Properties of Materials

## The Big Picture

```
THERMAL & OPTICAL PROPERTIES LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  ATOMIC CARRIERS
  ┌─────────────────────┐    ┌────────────────────────┐
  │  PHONONS             │    │  ELECTRONS            │
  │  (lattice vibrations)│    │  (electronic excitations)│
  └────────┬──────┬──────┘    └──────┬──────┬───────────┘
           │      │                  │      │
    ┌──────▼──┐ ┌─▼──────────┐ ┌────▼───┐ ┌▼─────────────┐
    │ THERMAL │ │ IR PHONON   │ │THERMAL │ │ OPTICAL     │
    │ CONDUCT.│ │ ABSORPTION  │ │CONDUCT.│ │ ABSORPTION  │
    │ κ_ph    │ │ (Reststrahl)│ │ κ_el   │ │ (interband) │
    └────┬────┘ └──────┬──────┘ └───┬────┘ └──────┬────────┘
         │             │            │              │
         └──────┬──────┘            └──────┬───────┘
                │                          │
    ┌───────────▼──────────┐   ┌───────────▼──────────────┐
    │ EMISSIVITY / PLANCK  │   │ REFRACTIVE INDEX         │
    │ (Kirchhoff: ε = α)   │   │ ñ = n + iκ               │
    │ Hot surfaces emit    │   │ Controls reflection,     │
    │ photons via phonon   │   │ refraction, absorption   │
    │ + electron coupling  │   │ Kramers-Kronig links n,κ │
    └──────────┬───────────┘   └───────────┬──────────────┘
               │                           │
    ┌──────────▼───────────────────────────▼──────────────┐
    │  DEVICE APPLICATIONS                                │
    │  CPU cooling (κ_th) · Telecom fiber (low α at 1550nm)│
    │  Photovoltaics (bandgap absorption) · TBC coatings  │
    │  Thermal imaging (emissivity) · LED phosphors       │
    └─────────────────────────────────────────────────────┘

  Heat capacity: C_v = ∂U/∂T            Refractive index: ñ = n + iκ
  Thermal conductivity: κ = J·L/ΔT      Absorption: α = 4πκ/λ
  Thermal expansion: ΔL/L = α·ΔT        Reflection: R = |(ñ-1)/(ñ+1)|²

  Carrier of heat:                        Carrier of light interaction:
    Phonons (insulators, semiconductors)    Free electrons (metals — Drude)
    Electrons (metals — Wiedemann-Franz)    Bound electrons (semiconductors, insulators)
    Photons (transparent at high T)         Phonons (IR absorption, Raman)

  BRIDGE TO COMPUTING:
  Thermal: CPU junction temp, PCB trace heating, solder joint fatigue,
           heat spreaders (copper vs diamond vs graphene), TIM selection
  Optical: fiber optic communication (1550nm minimum loss), CMOS image
           sensors, LED/laser diodes, photovoltaics, LiDAR for autonomy
```

---

## Part 1: Thermal Properties

### Heat Capacity — From Einstein to Debye

```
  CLASSICAL LIMIT (Dulong-Petit, 1819):
  C_v = 3Nk_B = 3R per mole ≈ 25 J/(mol·K) for all solids

  Works at high temperature. Fails below Debye temperature θ_D.

  EINSTEIN MODEL (1907):
  All atoms vibrate at same frequency ω_E

  C_v = 3Nk_B · (ℏω_E/k_BT)² · [e^(ℏω_E/k_BT) / (e^(ℏω_E/k_BT) - 1)²]

  Better than classical but: C_v ∝ e^(-θ_E/T) at low T (too fast a drop)
  Real solids show C_v ∝ T³ at low T — needs density of states model

  DEBYE MODEL (1912):
  Phonons treated as elastic waves; density of states g(ω) ∝ ω² up to cutoff ω_D

  C_v = 9Nk_B·(T/θ_D)³ · ∫₀^(θ_D/T) x⁴eˣ/(eˣ-1)² dx

  Limits:
    High T (T >> θ_D): C_v → 3Nk_B = 3R  (recovers Dulong-Petit) ✓
    Low T (T << θ_D):  C_v → (12π⁴/5)Nk_B(T/θ_D)³  (T³ law) ✓

  DEBYE TEMPERATURES:
  Material    θ_D (K)    Implication
  Diamond      2230       Still quantum at room temperature (T << θ_D)
  Si            640       Partially quantum at RT
  Al            428       Near Dulong-Petit at RT
  Cu            315       Classical at RT
  Pb             88       Fully classical well below RT
```

### Thermal Conductivity

```
  KINETIC THEORY EXPRESSION:
  κ = (1/3) · C_v · v_s · λ

  where: C_v = volumetric heat capacity (J/m³·K)
         v_s = speed of sound (phonon group velocity, m/s)
         λ   = mean free path (m) — limited by scattering

  PHONON SCATTERING MECHANISMS (limit λ and thus κ):
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Umklapp (U) processes:    phonon-phonon; dominant at high T             │
  │    κ_phonon ∝ 1/T at high T  (Umklapp increases with T)                  │
  │  Impurity/alloy scattering: κ drops with alloying (stainless < pure Fe)  │
  │  Grain boundary scattering: significant in nanostructures (κ of bulk     │
  │    Si = 150 W/mK; nanowire Si = 5 W/mK)                                  │
  │  Isotope scattering:       natural Si has 3 isotopes; isotopically pure  │
  │    Si-28: κ ≈ 11,000 W/mK at low T (current record)                      │
  └──────────────────────────────────────────────────────────────────────────┘

  ELECTRON CONTRIBUTION IN METALS — Wiedemann-Franz Law:
  κ_e / (σ · T) = L₀ = π²k_B² / 3e² = 2.44 × 10⁻⁸ W·Ω/K²  (Lorenz number)

  In pure metals: κ_e dominates (electrons are much better heat carriers
  than phonons in metals, because they're fast and have long mean free paths)

  THERMAL CONDUCTIVITY VALUES:
  Material           κ (W/mK)    Dominant carrier   Note
  ─────────────────────────────────────────────────────────────────────────
  Diamond            1000–2300   Phonons            Highest known solid
  Graphene (2D)      ~5000       Phonons            In-plane only
  Carbon nanotube    3000+       Phonons            Axial only
  Silver             429         Electrons          Best electrical + thermal
  Copper             401         Electrons          PCB traces, heat spreaders
  Gold               318         Electrons          Bonding wire, contacts
  Aluminum           237         Electrons          Heatsinks, conductors
  Silicon            150         Phonons            CPU substrate concern
  Tungsten           174         Electrons          Filaments, contacts
  Stainless steel    14–16       Electrons          Poor (alloying kills κ)
  SiC                120–490     Phonons            Power device substrates
  AlN                180–320     Phonons            LED/RF module substrates
  Glass              1.0–1.4     Phonons            Insulator
  HDPE polymer       0.46        Phonons            Insulator
  Aerogel            0.015       Gas (mostly)       Best insulator
  Air                0.026       Gas molecules      Reference
```

### Thermal Expansion

```
  LINEAR THERMAL EXPANSION:
  α = (1/L) · dL/dT   (K⁻¹)

  Volumetric: β ≈ 3α  (isotropic materials)

  GRÜNEISEN PARAMETER γ links thermal expansion to phonon behavior:
  α = γ · C_v / (3 · B · V)
  where B = bulk modulus, V = molar volume
  γ ≈ 1-2 for most solids; larger γ = larger mismatch between
  acoustic and optical phonon frequencies → more anharmonicity

  THERMAL EXPANSION VALUES:
  Material        α (10⁻⁶/K)   Note
  ────────────────────────────────────────────────────────────────────────
  Invar (Fe-36Ni)     1.2       Near-zero CTE (cancelation mechanism)
  Zerodur glass-cer   0.05      Telescope mirrors, lithography stages
  Si                  2.6       CPU substrate
  SiC                 4.0       Close to Si → low interfacial stress
  Al₂O₃ (alumina)    6.5–8     IC substrate, ceramic package
  AlN                 4.5       Good Si match + high κ
  GaAs                5.7       III-V semiconductor
  Silicon             2.6       —
  Copper             17.0       PCB traces; large mismatch to Si
  Solder (63Sn37Pb)  24.7       BGA solder balls; fatigue in ΔT cycling
  Aluminum           23.1       Heatsinks
  Steel              11.7       Structural
  CFRP (0°)        −0.5 to +2  Anisotropic; can engineer near-zero
  CFRP (quasi-iso)    2–4       In-plane; more isotropic than UD

  MISMATCH IMPLICATIONS (computing context):
  Cu trace (17 ppm/K) on FR-4 PCB (16–18 ppm/K): good match
  Cu pad (17 ppm/K) bonded to Si die (2.6 ppm/K): 6.5× mismatch
  → Solder joint fatigue from repeated thermal cycling (power-on/off)
  → Coffin-Manson: N_f ∝ (Δγ)^(-c) — fatigue life scales with strain range
  → Underfill epoxy reduces differential displacement; extends BGA life
```

### Thermoelectrics

```
  THREE THERMOELECTRIC EFFECTS:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  SEEBECK: ΔV = S · ΔT         (thermocouple, temperature sensor, TEG)   │
  │    S = Seebeck coefficient (µV/K)                                       │
  │    Metals: S ≈ 1–10 µV/K                                                │
  │    Semiconductors: S ≈ 100–300 µV/K  (better thermoelectrics)           │
  │                                                                         │
  │  PELTIER: Q = Π · I            (active heat pump, TEC cooler)           │
  │    Π = Peltier coefficient = S·T                                        │
  │    Heat pumped proportional to current — NOT temperature difference     │
  │                                                                         │
  │  THOMSON: q = β · I · ∇T       (reversible heat in current-carrying     │
  │    conductor in temperature gradient; small correction to above)        │
  └─────────────────────────────────────────────────────────────────────────┘

  FIGURE OF MERIT ZT:
  ZT = S²σT / κ    (dimensionless)

  S² σ = "power factor" (maximize for good thermoelectric)
  κ    = thermal conductivity (minimize — hard: good TE = good electrical conductor
         = good thermal conductor)

  This is the fundamental tension in thermoelectrics: Wiedemann-Franz means
  σ↑ → κ_e↑, so reducing κ while keeping σ high requires reducing κ_phonon only.

  Strategy: "phonon glass, electron crystal"
    • Rattler atoms (Zn₄Sb₃, skutterudites): loosely bonded atoms scatter phonons
    • Nanostructuring: grain boundaries scatter phonons more than electrons
    • Complex unit cells: many phonon branches, slow group velocity

  ZT VALUES:
  Material                ZT    T (°C)   Note
  ─────────────────────────────────────────────────────────────────────────
  Bi₂Te₃ (bulk)           1.0   25       Best near RT; commercial TEC modules
  Bi₂Te₃ (nanostructured) 1.4   25       Research — IBM/RTI record
  PbTe alloys              2.2   500      Mid-T range; power generation
  GeTe/AgSbTe₂ (TAGS)     1.7   400      Efficiency ~10% at ΔT = 300°C
  SnSe (single crystal)    2.6   650      Record 2014; anisotropic crystal
  Half-Heusler alloys       1    700      High-T; mechanically robust
  Skutterudites            1.7   600      CoSb₃-based; auto exhaust recovery

  ZT > 1 required for commercial viability at ~10% efficiency
  ZT > 3 needed for solid-state refrigeration to compete with compressor cycles
  Applications: space (RTG — Pu-238 decay → 5% efficiency), industrial waste heat,
  automotive (BMW turbocharger exhaust → 1 kW), CPU spot cooling (TEC)
```

---

## Part 2: Optical Properties

### Refractive Index and Absorption

```
  COMPLEX REFRACTIVE INDEX:  ñ = n + iκ

  n  = real part → determines phase velocity v = c/n
                   → determines reflection angle (Snell's Law: n₁sinθ₁ = n₂sinθ₂)
  iκ = imaginary part → determines absorption

  INTENSITY ATTENUATION (Beer-Lambert):
  I(z) = I₀ · e^(-αz)
  α = 4πκ/λ  (absorption coefficient, m⁻¹)
  1/α = absorption depth (distance at which intensity falls to 1/e)

  REFLECTANCE at normal incidence:
  R = |(ñ - 1) / (ñ + 1)|²

  For metals (large κ): R ≈ 1 − 2/√(ωτ·σ/ε₀ω) → metals are highly reflective
  For glass (κ = 0): R = (n-1)²/(n+1)²; glass with n=1.5: R = 4% per surface

  n VALUES AT VISIBLE WAVELENGTHS (λ ≈ 500 nm):
  Material              n       κ        Application
  ─────────────────────────────────────────────────────────────────────────
  Vacuum               1.000   0         Reference
  Air                  1.0003  0         Essentially vacuum
  Water                1.33    0         Optics, biology
  SiO₂ (fused silica) 1.46    0         Optical fiber cladding
  Optical fiber core   1.47–1.5 0        Single-mode (Δn ≈ 0.3%)
  Borosilicate glass   1.52    0         Microscope optics
  Crown glass          1.52    0         Camera lenses
  Flint glass          1.62    0         High-dispersion lens elements
  Sapphire (Al₂O₃)    1.77    0         Watch crystals, LED windows
  Diamond              2.42    0         Gem optics, high-n windows
  Silicon              3.5     small     Near-IR detector, photonics
  GaAs                 3.6     small     III-V optoelectronics
  Gold (at 500nm)      0.27    3.0       Reflective (mirror, nanoparticles)
  Silver (at 500nm)    0.13    3.1       Best visible mirror (~98% R)
```

### Drude Model for Metals

```
  FREE ELECTRON MODEL:
  Electrons respond to E-field: m·dv/dt = -eE - mv/τ (damping term)

  AC response → complex permittivity:
  ε(ω) = 1 - ωp² / (ω² + iω/τ)
  where ωp = √(ne²/ε₀m) = plasma frequency

  AT HIGH FREQUENCY (ω >> 1/τ):
  ε(ω) ≈ 1 - ωp²/ω²

  PLASMA FREQUENCY consequences:
  ω < ωp: ε < 0 → purely imaginary ñ → evanescent field → REFLECTION
  ω > ωp: ε > 0 → real ñ → propagating wave → TRANSMISSION

  Aluminum: ωp = 2.24×10¹⁶ rad/s → λp ≈ 84 nm (deep UV)
  → Al reflects visible, UV-A, UV-B but transmits vacuum UV → Al foil IS transparent
     in X-ray range (very low α at high frequency)

  VISIBLE COLORS OF METALS — why gold is yellow, copper is orange, silver is white:
  Silver: ωp at ~UV boundary → reflects all visible uniformly → white/grey
  Gold:   d-band transitions at ~2.5 eV (blue/green) → absorption of blue/green
          → reflects yellow/red → yellow color
  Copper: d-band at ~2.1 eV → absorbs blue → reflects red/orange → copper color
```

### Semiconductors: Optical Transitions

```
  DIRECT vs INDIRECT BANDGAP:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  DIRECT (GaAs, InP, GaN, InGaAs, CdTe):                                 │
  │    Conduction band minimum directly above valence band maximum in k-space│
  │    E-k: both extrema at k=0 (Γ point)                                   │
  │    Photon absorption/emission: momentum conserved with k_photon ≈ 0     │
  │    → efficient light emission; high absorption coefficient near E_g     │
  │    → used for LEDs, laser diodes, solar cells, photodetectors           │
  │                                                                         │
  │  INDIRECT (Si, Ge, GaP, AlAs):                                          │
  │    CB minimum at different k than VB maximum (k ≠ 0)                    │
  │    Photon + phonon required to conserve momentum                        │
  │    → two-particle process → low probability → poor light emitter        │
  │    → high optical absorption depth (mm for Si at 1µm vs nm for GaAs)    │
  │    → Si solar cells need 200 µm thickness vs 1 µm for GaAs              │
  │    → Si cannot make practical laser diode (but CAN detect with thick    │
  │       absorption layer)                                                 │
  └─────────────────────────────────────────────────────────────────────────┘

  ABSORPTION EDGE:
  Photon energy hν < E_g: material transparent (low α)
  Photon energy hν > E_g: strong absorption (α rises steeply)

  At T > 0: Urbach tail (exponential sub-gap absorption from phonon broadening)

  BURSTEIN-MOSS SHIFT (heavily doped semiconductors):
  n-type doping fills CB states → optical gap appears LARGER than E_g
  (electrons block transitions near CB edge)
  Effect matters in heavily doped ITO (transparent conducting oxide):
  ITO: E_g ≈ 2.9 eV (visible), but BM shift pushes effective edge toward UV

  SEMICONDUCTOR OPTICAL PROPERTIES:
  Material   E_g (eV)  Gap type   λ_edge (nm)  Application
  ──────────────────────────────────────────────────────────────────
  GaN         3.4      Direct      365           UV-A LED, blue LED pump
  GaP         2.3      Indirect    540           Yellow-green LED (indirect; low eff)
  AlGaAs   1.4–2.2    Direct      562–886       Heterojunction laser, HBT
  GaAs        1.42     Direct      873           Near-IR laser, solar cell
  InP         1.35     Direct      920           Telecom laser (1.3µm with strain)
  Si          1.12     Indirect   1107           Photodetector, image sensor
  Ge          0.67     Indirect   1850           IR detector, germanium-on-Si
  InGaAs(P)   0.73–1.35 Direct   920–1700       Telecom (1310/1550 nm) lasers
  InAs        0.36     Direct     3400           Mid-IR detector
  HgCdTe   0.0–1.5    Direct     variable       MWIR/LWIR FPA (tunable)
```

### Photovoltaics

```
  P-N JUNCTION UNDER ILLUMINATION:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Dark (equilibrium): depletion region, built-in field E_bi              │
  │  Light: photons create electron-hole pairs                              │
  │  Minority carriers diffuse to junction → separated by E_bi              │
  │  → photocurrent I_ph flows opposite to diode forward current            │
  │                                                                         │
  │  I-V under illumination:  I = I_0·(e^(qV/nkT) - 1) - I_ph               │
  │                                                                         │
  │  Short-circuit current: I_sc = I_ph  (at V=0)                           │
  │  Open-circuit voltage:   V_oc = (nkT/q)·ln(I_ph/I_0 + 1)                │
  │  Fill factor:            FF = P_max / (V_oc · I_sc) ≈ 0.7–0.85          │
  │  Efficiency:             η = FF · V_oc · I_sc / P_incident              │
  └─────────────────────────────────────────────────────────────────────────┘

  SHOCKLEY-QUEISSER LIMIT:
  Single junction: η_max ≈ 33% (at E_g ≈ 1.1–1.4 eV, AM1.5 spectrum)
  Si (1.12 eV): theoretical max ~32%; best lab Si cell: ~26%
  Losses:
    Sub-bandgap photons not absorbed
    Above-bandgap photons: excess energy thermalized as heat
    Recombination losses
    Reflection, series resistance (practical)

  EXCEEDING SHOCKLEY-QUEISSER:
  Multi-junction (tandem): series-connected cells, each absorbs different E range
    III-V 3J: GaInP (1.9 eV) / GaAs (1.4 eV) / Ge (0.7 eV)
    Lab record: ~47.1% (concentrated, 6-junction III-V)
    Commercial: 30–40% under concentration; expensive → space + concentrating PV
  Perovskite/Si tandem: Si bottom cell + perovskite (1.7 eV) top
    → >33% lab record (2023); lower cost potential than III-V
```

### LEDs and Lasers

```
  LED vs LASER DIODE:
  LED: spontaneous emission — random phase, broad spectrum, Lambertian
  Laser: stimulated emission — coherent, narrow linewidth, directional

  LASER THRESHOLD:
  Below threshold: only spontaneous emission (like LED)
  Above threshold: stimulated emission dominates → lasing
    Threshold current density J_th: gain = loss (cavity losses + absorption)

  QUANTUM WELL ACTIVE REGION:
  Single QW or MQW (multiple quantum wells) confines carriers in 2D
  → density of states → higher gain per carrier → lower J_th
  → now standard in all semiconductor lasers

  VERTICAL-CAVITY SURFACE-EMITTING LASER (VCSEL):
  Emits perpendicular to chip surface; array-able → data center transceivers
  GaAs VCSEL at 850 nm: 10–25 Gbps/lane; low threshold (~1 mA)
  InP VCSEL at 1310/1550 nm: emerging for telecom

  EDGE-EMITTING LASER (FP, DFB):
  Emits from cleaved facet; DFB (distributed feedback) has grating → single mode
  DFB laser at 1550 nm: standard for fiber-optic long-haul; linewidth < 1 MHz
```

### Optical Fiber

```
  WAVEGUIDING PRINCIPLE: total internal reflection
  n_core > n_cladding → TIR for rays within acceptance cone

  NUMERICAL APERTURE:  NA = √(n_core² - n_clad²) = n·sin(θ_max)
  Typical SM fiber: NA ≈ 0.12 (tight acceptance angle)

  FIBER TYPES:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Multimode (MM):  core 50–62.5 µm; many modes travel different paths     │
  │    → modal dispersion limits bandwidth-distance product                  │
  │    → 10 GbE: max 300m at 850 nm on OM4 fiber                             │
  │    → cheap (LED source); data center campus backbones                    │
  │                                                                          │
  │  Single-mode (SM): core 8–10 µm; only HE₁₁ mode propagates               │
  │    → no modal dispersion; bandwidth limit from chromatic dispersion only │
  │    → 100+ km without amplification (EDFA every 80 km in long-haul)       │
  │    → requires laser source; all metro/long-haul fiber                    │
  └──────────────────────────────────────────────────────────────────────────┘

  DISPERSION TYPES:
  Material dispersion: n(λ) varies with wavelength → different λ → different v
  Waveguide dispersion: mode shape changes with λ; opposite sign to material
  Total chromatic = material + waveguide
  Zero-dispersion wavelength λ_ZD ≈ 1310 nm for standard SM fiber (ITU G.652)
  Dispersion-shifted fiber: moves λ_ZD to 1550 nm (minimum loss)

  ATTENUATION:
  Loss mechanisms: Rayleigh scattering ∝ λ⁻⁴ (dominant at short λ)
                   OH absorption (water peak at 1385 nm)
                   IR absorption (phonon absorption > 1700 nm)
  Minimum: 0.154 dB/km at 1550 nm (SSMF Corning SMF-28)
  → telecom uses 1310 nm (low dispersion) and 1550 nm (low loss) windows
  Dense WDM (DWDM): 80–100 channels in C-band (1530–1565 nm) @ 50 GHz spacing
```

---

## Decision Cheat Sheet

| You need to... | Know / Use |
|----------------|-----------|
| Cool a CPU hot spot actively | Bi₂Te₃ TEC (ZT ≈ 1.0); limited ΔT_max ≈ 70°C |
| Generate power from waste heat | PbTe or skutterudite TEG (ZT ≈ 1.5–2 at 500°C) |
| Maximize heat spreading | Copper (400 W/mK) → vapor chamber → graphite sheet |
| Match Si CTE for substrate | AlN (CTE 4.5 ppm/K, κ 320 W/mK) or Si carrier |
| Understand why solder joints crack | CTE mismatch + Coffin-Manson fatigue |
| Understand minimum-loss telecom | 1550 nm window, SM fiber, DWDM, EDFA |
| Understand why Si can't lase | Indirect bandgap (Si) vs direct (GaAs, InP) |
| Near-IR laser source at 1550 nm | InGaAsP DFB laser diode on InP substrate |
| Short-reach data center link | VCSEL at 850 nm + OM4 MM fiber, up to 400m |
| High-efficiency solar cell | Multi-junction III-V (space) or perovskite/Si tandem |
| Understand why gold is yellow | d-band absorption cuts out blue/green |
| Understand plasma frequency | Drude model; metals reflect below ωp, transmit above |

---

## Common Confusion Points

**Thermal conductivity of metals is dominated by electrons, not phonons.**
That's why alloying metals so drastically reduces κ — impurity atoms scatter
electrons. Stainless steel (16 W/mK) vs pure iron (80 W/mK). Brass (109 W/mK)
vs pure copper (400 W/mK). Phonon κ barely changes; electron κ collapses.

**ZT is a material property at a given temperature — not a device efficiency.**
Device Carnot efficiency × (conversion factor involving ZT) gives you actual η.
ZT = 1 gives ~8% device efficiency at ΔT = 300 K. ZT = 4 would give ~25%.
The jump from ZT=1 to ZT=2 is huge; ZT=3+ is a materials science holy grail.

**"1550 nm is the low-loss telecom window" — but what does low mean?**
0.154 dB/km means at 1000 km of fiber you have 154 dB loss — completely
unworkable without amplification. An EDFA (erbium-doped fiber amplifier) at 80
km spacings gives you about 15 dB gain per stage. Without EDFA (invented 1987),
long-haul fiber communication would be impossible. The 1550 nm window and EDFA
gain band are perfectly matched — that's why 1550 nm was adopted.

**Direct vs indirect bandgap is about k-space, not energy.**
GaAs has a smaller bandgap (1.42 eV) than GaP (2.26 eV) but GaAs is the better
LED/laser material because it's direct. GaP is indirect → ~1000× lower radiative
efficiency. Nitrogen doping creates an isoelectronic trap in GaP that partially
localizes the exciton in k-space — this is why old green LEDs used GaP:N; they're
inefficient but workable. Modern green LEDs use InGaN/GaN quantum wells (direct).

**Debye temperature and heat capacity at room temperature.**
If θ_D >> 300 K (diamond: θ_D = 2230 K), C_v at room temperature is much less
than the classical 3R value. Diamond C_v ≈ 0.51 J/(g·K) vs lead 0.13 J/(g·K)
(lead θ_D = 88 K → fully classical). But diamond has both high κ and low C_v →
κ = C_v·v_s·λ/3 is dominated by extremely high v_s (17,500 m/s) and very long
phonon mean free path (λ >> other materials at room T).
