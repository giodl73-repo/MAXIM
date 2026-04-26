# Planetary Interiors
## Differentiation, PREM, Seismology, Geodynamo, Plate Tectonics, Comparative Planetology

---

## Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     HOW WE KNOW PLANETARY INTERIORS                         │
│                                                                             │
│   HEAT SOURCE           PROCESS              OBSERVABLE                     │
│   ──────────            ───────              ──────────                     │
│   Accretion energy  ──► Melting & mixing ──► Differentiation                │
│   ²⁶Al decay       ──► Iron sinks      ──► Core / mantle / crust          │
│   ⁴⁰K, U, Th decay ──► Sustained heat  ──► Active tectonics               │
│   Tidal friction   ──► Local heating   ──► Io volcanism, Europa ocean       │
│                                                                             │
│   PROBE METHOD          WHAT IT SEES         RESOLUTION                     │
│   ────────────          ────────────         ──────────                     │
│   Seismology (P/S) ──► 1-D velocity ──► PREM layers, CMB                  │
│   Normal modes     ──► Bulk elastic  ──► K, G, density vs. depth          │
│   Moment of inertia──► Core fraction ──► C/MR² = 0.3307 (Earth)           │
│   Geodesy / tides  ──► Tidal Love k₂──► Core state (liquid vs solid)      │
│   Geomagnetism     ──► Dynamo active ──► Liquid conducting outer core       │
│   Meteorites       ──► Bulk chemical ──► Core/mantle composition            │
│   Sample return    ──► Rock types    ──► Crust + upper mantle               │
│                                                                             │
│   KEY NUMBERS — Earth                                                       │
│   R_E = 6371 km   M_E = 5.972×10²⁴ kg   ρ_mean = 5514 kg/m³              │
│   Inner core: r = 1221 km (solid Fe-Ni)                                     │
│   Outer core: r = 3480 km (liquid Fe + light elements)                      │
│   CMB at 2891 km depth; D″ layer ~200 km above                              │
│   Mantle: 2891–35 km depth; mostly peridotite/bridgmanite                   │
│   Crust: oceanic ~7 km; continental ~35 km                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Differentiation — How Planets Stratify

### Heat Sources

A rocky body melts when heat generation exceeds radiative loss. Three dominant mechanisms:

| Heat Source | Formula / Value | Timescale | Dominant In |
|-------------|-----------------|-----------|-------------|
| Accretion (kinetic→thermal) | E ~ (3/5)GM²/R | First few Myr | All large bodies |
| ²⁶Al decay | t₁/₂ = 0.717 Myr | 0–5 Myr | Early-accreting planetesimals |
| Long-lived: ⁴⁰K, ²³²Th, ²³⁵U, ²³⁸U | ~20 TW today (Earth) | Gyr | Sustained mantles |
| Tidal dissipation | Q-dependent | Continuous | Io, Europa, Enceladus |
| Differentiation itself | ~500 K release | Same as accretion | Adds ~20% to accretion |

**Why ²⁶Al is pivotal**: any body that accreted within ~2 Myr of CAI formation received enough ²⁶Al to melt completely. This is why S-type asteroids (parent bodies of ordinary chondrites) show iron cores. Bodies that accreted late (>5 Myr) — like carbonaceous chondrite parents — largely avoided melting.

### The Differentiation Cascade

```
Molten rocky body (undifferentiated — chondritic composition)
│
├─► Fe-Ni liquid: ρ ~ 7000 kg/m³, low viscosity → sinks
│   └─► Core formation: ~10⁶ yr timescale once liquid
│       Physics: Stokes settling (r² Δρ g / 18η) OR
│               percolation through solid silicate (requires melt fraction > ~2%)
│
├─► Silicate melt: peridotite / basalt → "magma ocean" phase
│   └─► Crystallization sequence: olivine/pyroxene settle → layered mantle
│       Perovskite (now bridgmanite) crystallizes at 25 GPa → lower mantle
│       Last liquid = KREEP enriched (K, REE, P) → lunar highlands example
│
└─► Crust: partial melting of mantle → low-density melt rises
    Oceanic: Fe-Mg basalt (MORB), ~7 km, ρ ~ 2900 kg/m³
    Continental: felsic granite/andesite, ~35 km, ρ ~ 2700 kg/m³
```

**Gravitational energy of differentiation**: Rearranging iron from homogeneous to core-concentrated releases:

$$\Delta E_{\text{grav}} \approx \frac{3GM^2}{5R} \left[ f_c \left(\frac{R}{R_c}\right)^2 - \frac{1}{3} \right] \approx 500 \text{ K equivalent for Earth}$$

This is why differentiation itself is a heat source: the potential energy of mixing is released as thermal energy.

### Moment of Inertia — The Core Fraction Diagnostic

For a uniform sphere: C/MR² = 2/5 = 0.400. Any concentration toward center reduces this.

| Body | C/MR² | Interpretation |
|------|--------|----------------|
| Earth | 0.3307 | Large dense iron core |
| Moon | 0.394 | Nearly uniform (small core, <350 km) |
| Mars | 0.3662 | Intermediate core |
| Jupiter | 0.254 | Heavy core + H/He envelope |
| Mercury | ~0.346 | Anomalously large core (>60% by radius) |
| Uniform sphere | 0.4 | Reference |

Mercury's large core: either originally iron-rich (reduced nebular condensation) or giant impact stripped the silicate mantle — current data supports giant impact (MESSENGER geochemistry).

---

## 2. Earth's Interior — The PREM Model

**PREM** = Preliminary Reference Earth Model (Dziewonski & Anderson 1981). Defines 1-D spherically symmetric profiles of density ρ, P-wave velocity V_P, S-wave velocity V_S, bulk modulus K, and shear modulus G vs. radius.

### Structure Layers

```
┌─────────────────────────────────────────────────────────┐
│                  EARTH CROSS-SECTION                    │
│                                                         │
│    Depth     Layer          V_P    V_S    ρ             │
│    (km)                    (km/s) (km/s) (g/cm³)        │
│    ─────     ─────         ─────  ─────  ──────         │
│    0–35      Crust          6.5    3.7    2.9           │
│    35–80     Lithosphere    8.1    4.5    3.3           │
│    35–410    Upper mantle   8–9    4.5    3.3–3.5       │
│    410–660   Transition zone 9–11  5      3.5–3.9       │
│    660–2891  Lower mantle   11–13  6–7    4.4–5.6       │
│    2891      CMB ←─── zero shear below this             │
│    2891–5150 Outer core     8–11   0      9.9–12.1      │
│    5150–6371 Inner core     11.0   3.5    12.8–13.1     │
│    6371      Center                                     │
└─────────────────────────────────────────────────────────┘
```

**Key discontinuities:**

| Name | Depth | Cause |
|------|-------|-------|
| Moho (Mohorovičić) | ~35 km (variable) | Crust/mantle composition change |
| Olivine → wadsleyite | 410 km | Phase transition; density jump ~5% |
| Ringwoodite → bridgmanite + periclase | 660 km | Phase transition; traps mantle convection? |
| CMB (Core-Mantle Boundary) | 2891 km | Liquid iron vs solid silicate; V_S → 0 |
| ICB (Inner Core Boundary) | 5150 km | Liquid → solid iron; Lehmann discontinuity |
| D″ layer | 200–300 km above CMB | Partially molten; post-perovskite phase; LLSVP roots |

**Equation of state inside Earth**: Adams-Williamson equation for adiabatic self-compression:

$$\frac{d\rho}{dr} = -\frac{\rho(r) g(r)}{\Phi(r)}, \quad \Phi = K_S/\rho = V_P^2 - \frac{4}{3}V_S^2$$

Seismic parameter Φ is directly measurable from PREM; integrating gives density. This is the fundamental link between seismology and interior structure.

### Pressure and Temperature Profile

$$\frac{dP}{dr} = -\rho(r) g(r), \quad g(r) = \frac{G M(r)}{r^2}$$

| Depth | P | T |
|-------|---|---|
| Moho (~35 km) | 1 GPa | ~600°C |
| 410 km | 13.5 GPa | ~1500°C |
| 660 km | 23.5 GPa | ~1800°C |
| CMB (2891 km) | 136 GPa | ~3500–4000°C |
| ICB (5150 km) | 329 GPa | ~5000–6000°C |
| Center | 364 GPa | ~5000–6000°C |

The inner core solidifies not because it's cold by absolute measure, but because the liquidus slope exceeds the adiabatic gradient at high pressure — the Lindemann melting criterion.

---

## 3. Seismology — Reading the Interior from Waves

### Wave Types

```
Body waves:
  P-waves (primary/compressional):  ──►  ──►  ──►    V_P = √((K+4G/3)/ρ)
     Travel through solids AND liquids (K>0 for fluids, G=0)

  S-waves (secondary/shear):        ─►  ─►         V_S = √(G/ρ)
     Travel through solids only (G=0 in liquids → S blocked by outer core)

Surface waves:
  Love waves:  SH polarization, guided by crust + mantle layering
  Rayleigh waves:  elliptical retrograde motion, coupled P-SV
  Frequency-dependent (dispersive) → constrain layering vs. depth
```

### Snell's Law in Spherical Earth

Wave speed increases with depth (mostly). By Snell's law (Benndorf's form):

$$\frac{r \sin i}{V(r)} = p = \text{ray parameter (constant along ray)}$$

Rays curve toward regions of lower velocity. A ray turning point is where V(r)/r = V(r_surface)/r_surface — it bottoms out and curves back up.

### Shadow Zones — Mapping the Core

```
       ┌──────────────────────────────────────────┐
       │           P-WAVE SHADOW ZONE             │
       │                                          │
       │  Earthquake epicenter = 0°               │
       │                                          │
       │  0°–103°:  Direct P waves arrive         │
       │  103°–142°: P-WAVE SHADOW ZONE           │
       │             (refracts into liquid core → │
       │              slows, bends away from crit │
       │              angle; no direct P arrival) │
       │  >142°: PKP arrives (went through core)  │
       │         PcP bounces off CMB              │
       │                                          │
       │  S-WAVE SHADOW: >103° (complete)         │
       │  S cannot propagate through liquid outer │
       │  core — SKS (S converted to K in core)   │
       └──────────────────────────────────────────┘
```

**Notation**: P = mantle leg, K = outer core (compressional), I = inner core (compressional), J = inner core shear (barely detected), c = CMB reflection, i = ICB reflection.

Common phases: PcP, PKP, PKIKP (straight through), SKS, PKJKP.

**Lehmann discontinuity** (Inge Lehmann, 1936): early arrivals inside the P-wave shadow zone revealed a solid inner core — P-waves refracted through it appear at distances where they should not arrive if the entire core were liquid.

### Normal Modes

A whole-Earth oscillation — seismically excited by great earthquakes. The $_{0}S_2$ "football mode" has period ~54 min. Normal modes constrain bulk Earth structure independently of ray-theory seismology, especially for very long periods. Also the only way to detect inner-core shear velocity.

---

## 4. The Geodynamo — Magnetic Field Generation

### Basic Requirements

Earth's magnetic field is generated by convection in the liquid outer core — **magnetohydrodynamic (MHD) dynamo**. Requirements:
1. Electrically conducting fluid (Fe-Ni liquid: σ ~ 10⁶ S/m)
2. Differential rotation / convection (Coriolis-organized)
3. Seed magnetic field (any small field amplified)

### Why the Outer Core Convects

Two mechanisms drive convection:
- **Thermal**: secular cooling of Earth + radioactive heating (some ⁴⁰K may partition to core)
- **Compositional**: as inner core freezes, light elements (O, S, Si) expelled → buoyant compositional plumes. This is the *dominant* driver in present Earth.

### The αΩ Dynamo (Parker 1955)

```
Differential rotation (Ω):
  ──► Stretches poloidal field → toroidal field
      (B_toroidal ~ Rm × B_poloidal, Rm = UL/η = magnetic Reynolds number)

Cyclonic convection (α):
  ──► Coriolis twists toroidal field → regenerates poloidal field
      (α = −τ₀ <u'·(∇×u')>/3 — kinetic helicity)

Closed loop:
  Poloidal ──Ω──► Toroidal ──α──► Poloidal
```

**Magnetic Reynolds number**: Rm = UL/η, where η = 1/(μ₀σ) is magnetic diffusivity. Rm >> 1 (induction dominates diffusion) → dynamo can sustain field. For Earth's outer core: U ~ 10⁻⁴ m/s, L ~ 10⁶ m, η ~ 1 m²/s → Rm ~ 100–300.

**Cowling's anti-dynamo theorem**: no purely axisymmetric field can be maintained by fluid flow — some 3-D asymmetry is required. This is why the geomagnetic field is not perfectly aligned with the rotation axis.

### Paleomagnetic Record and Reversals

- **Current dipole tilt**: ~11° from rotation axis; drifting westward ~0.2°/yr
- **Total reversals**: ~183 in past 83 Myr (M-sequence anomalies); irregular intervals
- **Duration of reversal**: ~1,000–10,000 yr transition (field weakens, multipolarity, recovers)
- **Current**: weakening ~5% per century; South Atlantic Anomaly is low-field region — possibly early reversal precursor, or just normal secular variation
- **Geodynamo simulations**: Glatzmaier-Roberts 1995 first realistic reversal simulation; modern codes (MAGIC, CALYPSO) reproduce Earth-like dynamos with correct Rm, Elsasser number

**Elsasser number** Λ = σB²/(2ρΩ): ratio of Lorentz to Coriolis force. Earth: Λ ~ 1 → magnetic and rotational forces comparable — the "magnetostrophic balance."

### Magnetic Field as Life Shield

The magnetosphere deflects solar wind (~400 km/s protons) before they can strip the atmosphere. Mars lost its dynamo ~4 Gya → solar wind erosion contributed to atmospheric loss (Mars MAVEN data). Venus has no dynamo (possibly no inner core, possibly wrong rotation/convection regime) yet retains thick CO₂ atmosphere — so magnetosphere is not strictly necessary, but helps over Gyr timescales.

---

## 5. Mantle Convection and Plate Tectonics

### Convection Fundamentals

Mantle viscosity: η ~ 10²¹ Pa·s (1 Pa·s = water; 10²¹ is a trillion billion times more viscous than water). Despite this, convects on timescales of 10⁸ yr.

**Rayleigh number**:

$$Ra = \frac{\rho g \alpha \Delta T d^3}{\kappa \eta}$$

Earth's mantle: Ra ~ 10⁷–10⁸ (strongly supercritical, turbulent convection). Critical Ra_c ≈ 10³.

Variables: g = 10 m/s², α (thermal expansion) ~ 2×10⁻⁵ K⁻¹, ΔT ~ 3000 K, d ~ 2900 km, κ (thermal diffusivity) ~ 10⁻⁶ m²/s.

### Plate Tectonics Engine

```
┌─────────────────────────────────────────────────────────────────┐
│                  PLATE TECTONICS OVERVIEW                       │
│                                                                 │
│   DRIVER            MECHANISM              MAGNITUDE            │
│   ──────            ─────────              ─────────            │
│   Ridge push    ──► Elevated ridge → GP    ~10¹² N/m            │
│   Slab pull     ──► Cold dense slab sinks  ~10¹³ N/m ← dominant│
│   Mantle drag   ──► Viscous coupling       variable             │
│                                                                 │
│   PLATE BOUNDARIES:                                             │
│   Divergent (MOR): basalt eruption, new oceanic crust           │
│   Convergent:      subduction (one oceanic plate) OR            │
│                    collision (both continental)                 │
│   Transform:       strike-slip, no creation/destruction         │
│                                                                 │
│   WHY EARTH HAS PLATES:                                         │
│   • Water in mantle → lowered solidus → partial melt            │
│   • Weak oceanic crust (basalt) dense enough to subduct         │
│   • Plate boundaries as weak zones (damage rheology)            │
│   Venus: no subduction (hot/dry crust too buoyant?), stagnant lid│
└─────────────────────────────────────────────────────────────────┘
```

**Wilson cycle**: ocean opens → matures → closes → collision → subduction begins anew. ~500 Myr period. Current example: Atlantic opening, Pacific subducting.

### Mantle Plumes and Hotspots

Narrow upwellings (thermal plumes) originating at CMB or 660-km discontinuity. Evidence: seamount chains (Hawaii-Emperor chain, ~10 cm/yr Pacific Plate speed), flood basalts (Deccan, Siberian Traps — possible extinction triggers), isotopic signature (less depleted than MORB source).

Plume tail diameter: ~100 km; head: can be 1000 km → flood basalt province upon arrival.

---

## 6. Comparative Planetology

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                    TERRESTRIAL PLANET INTERIORS COMPARED                       │
│                                                                                │
│  Property      Earth       Moon        Mars        Venus       Mercury         │
│  ──────────    ─────       ────        ────        ─────       ───────         │
│  Mass (M_E)    1.0         0.0123      0.107       0.815       0.0553          │
│  Radius (km)   6371        1737        3390        6051        2440            │
│  C/MR²         0.3307      0.3932      0.3662      0.337(est)  0.346           │
│  Core radius   3480 km     <350 km     ~1400–1600  ~3000 km    ~2000 km        │
│  Core state    Liq+solid   Mostly solid Mostly solid ?         Liq outer       │
│  Dynamo        Active      Dead        Dead (4Gya) Dead?       Active(weak)    │
│  Tectonics     Plate       None (rigid) None       Stagnant lid None           │
│  Volcanism     Active      Dead        Ancient (Tharsis active?) Recent        │
│  Mantle H₂O    0.5–1 oc.vol Dry        Dry         ?           Extremely dry   │
└────────────────────────────────────────────────────────────────────────────────┘
```

### Moon

- **Formation**: Giant impact (Theia) → debris disk → fast accretion. High-energy → global magma ocean → crystallization → anorthosite highlands (low-density plagioclase floats), mare basalt (Fe-rich melt fills impact basins later).
- **Lunar Magma Ocean (LMO)**: crystallized in ~100–200 Myr. KREEP (K, REE, P) — last 1–2% of melt — concentrated on nearside (related to giant impact asymmetry? — Garrick-Bethell et al.)
- **No dynamo now**: core too small, cooled too fast. Paleomagnetic evidence for ancient field 3.5–4.2 Gya — briefly active dynamo during LHB? Controversial: also impact-driven demagnetization patterns.
- **Seismology (Apollo)**: 4 seismometers. Found: very thin crust (~40 km farside), highly fractured megaregolith, deep moonquakes (700 km — tidally driven by Earth), shallow moonquakes (~50 km), meteorite impacts.
- **InSight on Mars**: First seismometer on Mars (2018–2022). Detected ~1300 marsquakes. Measured: crust 20–39 km (2–3 layers), mantle lid to ~500 km, liquid outer core r ~ 1830 km (larger than expected → light elements: O, H, C, S). No detected inner core.

### Mars

- **Tectonics**: stagnant lid — one plate, no recycling. Tharsis bulge ~9×10⁶ km² formed by sustained mantle plume ~3.7 Gya; loaded lithosphere and tilted whole planet ~20° (changed obliquity reference).
- **Valles Marineris**: ~4000 km long, 200 km wide, 10 km deep — rift system, not carved by water
- **Ancient dynamo**: strong crustal remanence in southern highlands (Acuña et al. 1999) records field >10× Earth's current field before ~4 Gya. Why it stopped: core cooled past threshold, inner core solidification? — still debated.
- **Water**: evidence for ancient oceans/rivers. Present: ice caps (mostly CO₂, some H₂O), subsurface permafrost, CRISM hydrated minerals (phyllosilicates, sulfates). MAVEN: solar wind is currently stripping ~100 g/s of atmosphere — magnetosphere loss → atmospheric loss pathway.

### Venus

- **Mystery of missing tectonics**: similar mass to Earth, expected to be geologically active. Yet no plate tectonics, essentially no magnetic field. Hypotheses: (1) too dry — no water to lubricate plates; (2) episodic resurfacing — global overturn every ~500 Myr rather than continuous recycling; (3) thin lithosphere prevents slab formation. Magellan (radar) showed ~1000 impact craters distributed randomly → resurfacing ~500–800 Mya.
- **Dynamo puzzle**: Venus rotates retrograde at 1 rotation per 243 days (extremely slow). Slow rotation → weak Coriolis → αΩ dynamo doesn't work? Or maybe no inner core solidification to drive compositional convection.

### Mercury

- **Anomalously large core**: ~85% of radius, ~60% of mass. Giant impact hypothesis (Benz 2007): a 1:6 mass impactor stripped the silicate mantle. Or: Instability in solar nebula preferentially evaporated silicates near the Sun (Cameron 1985 — now disfavored).
- **Active dynamo**: MESSENGER discovered weak global dipole (~1% Earth's field). Puzzling: moment arm (core to surface) large → Ohmic diffusion should dominate. Possible: core stratification suppresses convection → weak field (Christensen & Wicht 2008, "Mercury dynamo" with stable layer).
- **Surface**: heavily cratered, Caloris Basin (1550 km) — largest impact feature in solar system. Cliffs (lobate scarps) up to 3 km — global contraction as core cooled (diameter decreased ~7 km).
- **Ice in permanently shadowed craters**: Radar-bright deposits at poles — confirmed water ice by MESSENGER neutron spectrometer.

---

## 7. Tidal Heating and Subsurface Oceans

### Tidal Heating Formula

Tidal dissipation rate for a body in an eccentric orbit:

$$\dot{E}_{\text{tidal}} = -\frac{21}{2} \frac{k_2}{Q} \frac{GM_p^2 R^5 n e^2}{a^6}$$

where k₂ = tidal Love number (measures deformability), Q = quality factor (inverse of dissipation), n = mean motion, e = eccentricity, a = semi-major axis.

**Io** (Jupiter's innermost Galilean moon):
- Forced into e = 0.0041 by Laplace resonance (Io 1:2:4 with Europa:Ganymede)
- k₂/Q ~ 0.015 → heat flux ~2 W/m² (compare Earth's 0.087 W/m²)
- Result: ~100 active volcanoes, SO₂ atmosphere, surface continuously resurfaced
- Tidal heating rate ~6×10¹³ W (comparable to Earth's total internal heat)
- No water — too hot and tidally stripped; but demonstrates sustained tidal engine

**Europa**:
- e = 0.009 from resonance with Io/Ganymede
- Less dissipation than Io → moderate heating → maintains liquid water under ~15–25 km ice shell
- Evidence for ocean: Galileo magnetometer detected induced magnetic field (from saline liquid layer), surface tectonics (chaotic terrain, ridges consistent with liquid below), low crater density (young surface ~60 Myr)
- Ocean depth ~100 km; total water volume ~2× Earth's oceans
- Target for Europa Clipper (launched 2024 — arrives ~2030)

**Enceladus** (Saturn's moon, 252 km radius):
- Cassini detected active plumes from south polar "tiger stripes"
- Plume composition: H₂O, CO₂, CH₄, H₂, silica nanoparticles, complex organics, pH~9
- H₂ from hydrothermal water-rock reactions (serpentinization) — energy source compatible with life
- Internal ocean confirmed: libration measurements → ice shell decoupled from rocky core
- Tiny moon but tidal heating from Saturn in eccentric orbit (e = 0.0047), possibly maintained by resonance with Dione (2:1 MMR)

**Titan** (Saturn's largest moon):
- Likely subsurface ocean (saline, ~100 km depth) but tidal heating minimal
- Main interest: hydrocarbon lakes (methane/ethane) at surface — CH₄ cycle analogous to water cycle on Earth
- Thick N₂ atmosphere (1.5 bar) with haze
- Dragonfly mission (launch 2028, arrival 2034) — rotorcraft lander

### Ocean Worlds Summary

```
┌──────────────────────────────────────────────────────────────────┐
│                    SOLAR SYSTEM OCEAN WORLDS                     │
│                                                                  │
│  Body         Ocean type    Evidence strength   Habitability     │
│  ────         ──────────    ─────────────────   ────────────     │
│  Earth        Surface       Trivial             Confirmed        │
│  Europa       Subsurface    Strong              High potential   │
│  Enceladus    Subsurface    Very strong         Very high        │
│  Titan        Subsurface    Moderate            Low (cold)       │
│  Ganymede     Subsurface    Strong (Hubble HST) Uncertain        │
│  Callisto     Subsurface    Moderate            Lower            │
│  Ceres        Subsurface(?) Moderate (Dawn)     Unknown          │
│  Pluto        Ancient(?)    Weak                Unknown          │
└──────────────────────────────────────────────────────────────────┘
```

---

## 8. Exoplanet Interior Models

### Mass-Radius Diagram

The bulk composition of a planet is encoded in its position on the M-R diagram. Different internal structure models (equations of state) predict different M-R curves:

```
       R/R_E
    3  │         gas dwarfs / sub-Neptunes (H₂/He envelope)
       │        ╱
    2  │       ╱   water worlds (H₂O-dominated)
       │      ╱
  1.5  │─────────────── Fulton gap ─────────────────
       │    ╱  rocky + thin atmosphere
    1  │   ╱
       │  ╱ iron-dominated (Mercury-like)
    0  └────────────────────────────
       0.5  1   2   5   10   20  M/M_E
```

**Fulton gap** (~1.7 R_E, ~3 M_E): bimodal distribution of planet radii — super-Earths peak at ~1.3 R_E, sub-Neptunes at ~2.4 R_E. Gap explained by photoevaporation (Owen & Wu 2017) or core-powered mass loss: planets lose volatile H/He envelope from EUV irradiation, leaving bare rocky cores (the smaller peak) OR retaining enough to stay in sub-Neptune regime.

### Equations of State for Planetary Interior Modeling

| Layer | Material | EOS |
|-------|----------|-----|
| Iron core | Fe (hcp at high P) | Vinet EOS; Dewaele et al. 2006 |
| Silicate mantle | MgSiO₃ bridgmanite | Birch-Murnaghan 3rd order |
| Water layer | High-pressure ices (VII, X) | IAPWS + ab initio |
| Gas envelope | H/He | Chabrier EOS (SCvH) |

A 1-D interior model integrates pressure balance + EOS from surface inward:

$$\frac{dP}{dm} = -\frac{Gm}{4\pi r^4}, \quad \frac{dr}{dm} = \frac{1}{4\pi r^2 \rho(P)}$$

Mass-radius relations derived from published interior codes (MESA-based or custom):
- Pure Fe: R ∝ M^0.29
- Earth-like (33% Fe core + 67% silicate): R ∝ M^0.27
- Water world (50% water): R ∝ M^0.35
- H₂ atmosphere: R ∝ M^0.55 at fixed T_eq

**Degeneracy problem**: a given (M, R) point can be explained by multiple compositions — cannot distinguish "big iron core" from "small water layer" from "thin H₂ atmosphere" without spectroscopy.

### Super-Earths and Lava Worlds

- **55 Cancri e** (M = 8 M_E, R = 1.88 R_E): JWST detected thermal emission — surface temperature ~2300 K. Phase curves suggest magma ocean on dayside OR thick atmosphere. JWST NIRCam detected CO₂/CO — possible volcanic outgassing.
- **TRAPPIST-1 inner planets**: JWST transmission spectra — 1b has no thick atmosphere (thermal emission matches bare rock). 1c has no CO₂ despite being in "Venus zone." 1e–1g in habitable zone; JWST measurements ongoing.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| How do we know Earth's interior structure? | Seismology (P/S waves, shadow zones, normal modes), moment of inertia, geodesy, meteorites |
| What creates Earth's magnetic field? | Convection + compositional buoyancy in liquid outer core → αΩ MHD dynamo |
| Why is Io so volcanic? | Forced eccentricity (Laplace resonance 1:2:4) → tidal dissipation ~6×10¹³ W |
| Why does Europa have a liquid ocean? | Tidal heating from Laplace resonance; evidence: induced magnetic field, young surface |
| Why does Mars lack a dynamo? | Core cooled and solidified ~4 Gya; no inner core solidification to drive convection |
| Why does Venus lack plate tectonics? | Insufficient water in mantle (lubrication), slow rotation (weak Coriolis for dynamo) |
| Why does Mercury have such a large core? | Giant impact stripped silicate mantle; confirmed by MESSENGER geochemistry |
| What is the Fulton gap? | Bimodal gap at ~1.7 R_E; photoevaporation removes H/He from borderline planets |
| How do we model exoplanet interiors? | M-R diagram + EOS integration; degenerate without spectra |
| What seismic phase goes through Earth's center? | PKIKP (P → outer core K → inner core I → back through K → P) |
| What is the CMB? | Core-Mantle Boundary at 2891 km; V_S drops to zero (liquid below) |
| Adams-Williamson equation gives what? | Density profile from seismic velocities assuming adiabatic compression |

---

## Common Confusion Points

**"S-waves can't travel through the outer core — does that mean nothing does?"**
P-waves (compressional) still travel through liquid — K legs in phase notation. S converts to K at the CMB: SKS, SKKS. The *shear* (transverse) component dies but longitudinal pressure waves do not.

**"The inner core is solid — so Earth has no liquid metal?"**
The *outer* core (2891–5150 km) is liquid iron-nickel alloy — this is what drives the dynamo. The inner core (~1221 km radius) is solid, but surrounded by the liquid outer core. The solid inner core solidified ~1 Gyr ago (possibly ~500 Myr — still debated) and drives compositional convection as it grows.

**"Plate tectonics is driven by mantle convection pushing plates"**
Dominant driver is **slab pull** (old, cold, dense oceanic crust sinking under its own weight), not ridge push or mantle drag. Slabs pulling downward drag attached plates. Mid-ocean ridges are passive responses to plate separation, not engines pushing.

**"Venus is the same size as Earth — why no tectonics?"**
Size is necessary but not sufficient. Water content of the mantle seems crucial: water reduces olivine viscosity by orders of magnitude, enabling plate weakening and subduction initiation. Venus may have lost water early (runaway greenhouse) → locked in stagnant lid. Also debated: episodic catastrophic resurfacing every ~500 Myr may be Venus's alternative to continuous plate recycling.

**"If a planet has a magnetic field it has a liquid core"**
Not exactly — needs a *convecting* liquid conducting region. A fully stratified liquid core might not convect vigorously enough to sustain a dynamo. Mercury's weak field likely comes from a thin convective layer under a stable stratified region (Christensen model). Also: remanent magnetism (rocks recording ancient fields) can mimic an active dynamo in measurements.

**"The Moho separates continental from oceanic crust"**
The Moho separates *crust from mantle* everywhere. The crust-mantle transition is compositional (felsic/mafic → ultramafic peridotite) not a plate boundary. Continental crust averages ~35 km; oceanic ~7 km. Both sit above mantle peridotite.

**"Tidal heating requires a large moon"**
Tidal heating scales as (R/a)⁶ × e² × M_p² / Q. Small size can be compensated by small a (close orbit) and forced eccentricity from resonance. Enceladus is tiny (252 km) but heated by Saturn at a = 238,000 km with resonance-forced eccentricity.
