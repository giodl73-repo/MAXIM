# 13-GEOPHYSICS — Geophysics

> Earth's interior from seismology, mantle convection, plate tectonics,
> geomagnetism, and gravitational field. The physics of a living planet.

---

## Earth Interior Structure

```
LAYER           DEPTH (km)   DENSITY (g/cm³)  STATE       KEY EVIDENCE
──────────────────────────────────────────────────────────────────────────
Crust (oceanic)   0–10         2.9–3.0          Solid       Drilling, seismic refraction
Crust (continental) 0–35–70   2.7–2.9          Solid       Seismic, isostasy
Upper mantle      35–410       3.3–3.6          Solid       P/S wave velocities
Transition zone   410–660      3.6–4.4          Solid       Seismic discontinuities
Lower mantle      660–2890     4.4–5.6          Solid       High-P mineralogy
Outer core        2890–5150    9.9–12.2         LIQUID      S-waves absent (shadow zone)
Inner core        5150–6371    12.8–13.1        Solid       PKiKP reflections, PKIKP

Key seismic discontinuities:
  Mohorovičić (Moho): crust/mantle boundary (~7 km ocean, ~35 km continent)
  410 km: olivine → wadsleyite phase transition
  660 km: ringwoodite → bridgmanite + ferropericlase (major barrier to convection)
  Core-mantle boundary (CMB, 2890 km): dramatic density jump, D″ layer above
```

### How We Know (Seismic Evidence)

```
Body waves:
  P-waves (compressional): travel through solid AND liquid; faster in denser rock
  S-waves (shear): travel ONLY through solid; absent in outer core → liquid

P-wave shadow zone (103°–143° from earthquake epicenter):
  P-waves refracted around liquid outer core → shadow
  Proves outer core is liquid

S-wave shadow zone (>103°):
  S-waves completely blocked by outer core
  Proves outer core cannot transmit shear

Travel time curves:
  Plot arrival time vs epicentral distance
  Slope gives seismic velocity; discontinuities = velocity jumps
  Tomography: deviations from reference model → 3D temperature/composition structure
```

---

## Seismology

### Earthquake Mechanics

```
Elastic rebound theory (Reid, 1906):
  Tectonic stress accumulates in rock → elastic deformation
  → failure at fault → rapid slip → elastic energy released as seismic waves
  → surfaces spring back (rebound) from deformed state

Fault types:
  Normal fault:   hanging wall moves DOWN (extensional, divergent margins)
  Reverse fault:  hanging wall moves UP (compressional, subduction zones)
  Strike-slip:    horizontal motion along fault (transform margins; San Andreas, NAF)
  Thrust:         low-angle reverse fault → mountain building

Seismic moment: M₀ = μ · A · D
  μ = shear modulus (~3 × 10¹⁰ Pa), A = fault area, D = average slip
  Moment magnitude: Mw = (2/3) log₁₀(M₀) − 6.0
  Each unit increase: 31.6× more energy, 10× more ground motion amplitude
```

### Seismic Waves

```
Body waves (travel through interior):
  P-waves: compressional; vₚ = √((K + 4/3·G)/ρ)   ~6–8 km/s in crust
  S-waves: shear; vₛ = √(G/ρ)                      ~3.5–4.5 km/s in crust
  vₚ/vₛ ≈ √3 for typical crustal rock (Poisson ratio ~0.25)

Surface waves (travel along surface, slower, larger amplitude):
  Love waves:   horizontal shear, faster, no vertical motion
  Rayleigh waves: elliptical particle motion, slower, most damaging in earthquakes

Snell's law for seismic waves:
  sin(i₁)/v₁ = sin(i₂)/v₂   (same as optics, refraction at layer boundary)
  Velocity generally increases with depth → seismic rays curve upward

Seismic tomography:
  Measure travel time residuals (observed − predicted) across global station networks
  Invert for 3D velocity structure (temperature proxy)
  Fast = cold/dense (subducted slabs); slow = hot/low-density (plumes)
```

### Focal Mechanisms (Beach Balls)

```
Equal-area projection of first motion polarities:
  Black quadrant: compressional first motion (toward station)
  White quadrant: dilatational first motion (away from station)

Reading beach balls:
  Normal fault:     two black lobes at poles, white equatorial band
  Reverse fault:    two white lobes at poles, black equatorial band
  Strike-slip:      alternating black/white quadrants like checkerboard
  Oblique:          intermediate patterns

Two nodal planes: one = actual fault plane; other = auxiliary plane
  Distinguish using: aftershock distribution, surface rupture, satellite geodesy (InSAR)
```

---

## Mantle Convection

### Thermal Convection

```
Rayleigh number:
  Ra = α·g·ΔT·d³ / (κ·ν)

  α = thermal expansivity (~3 × 10⁻⁵ K⁻¹)
  g = gravitational acceleration
  ΔT = temperature difference top-bottom
  d = layer thickness
  κ = thermal diffusivity (~10⁻⁶ m²/s)
  ν = kinematic viscosity

  Convection onset: Ra > Ra_crit ≈ 1000 (for free-slip boundaries)
  Earth's mantle: Ra ~ 10⁷ → vigorous convection

Mantle viscosity: ~10²¹ Pa·s (lower mantle) to ~10²⁰ Pa·s (upper mantle)
  Highly non-Newtonian: dislocation creep (power law) + diffusion creep
  Temperature-dependent: hot rock flows, cold lithosphere rigid

Convection pattern:
  Upwelling: hot material rises (mid-ocean ridges, hot spots)
  Downwelling: cold material sinks (subducting slabs — most efficient cooling)
  Whole mantle vs layered convection: ongoing debate
  660 km discontinuity: partial filter → mostly whole-mantle with some ponding
```

### Mantle Convection — Fluid Mechanics Bridge

Mantle convection is Rayleigh-Bénard convection at planetary scale. The same
dimensionless parameters and instability analysis govern both a laboratory heated
fluid layer and the mantle:

```
RAYLEIGH-BÉNARD CONVECTION:

  Ra = (α g ΔT d³) / (ν κ)

  α = thermal expansion coefficient
  g = gravity
  ΔT = temperature difference top to bottom
  d = layer thickness
  ν = kinematic viscosity
  κ = thermal diffusivity

  Critical: Ra_c ≈ 1708 (onset of convection cells — Bénard instability)
  Lab water (~100°C ΔT): Ra ~ 10⁵–10⁶ → mild turbulence
  Earth's mantle:         Ra ~ 10⁶–10⁷ → vigorous convection

  SAME GOVERNING EQUATION: Navier-Stokes + energy equation + buoyancy
    ρ(∂u/∂t + u·∇u) = −∇p + µ∇²u + ρα(T−T₀)g
    (for mantle: inertia term negligible → Stokes flow, Re ~ 10⁻²³)

HEAT EXCHANGER ANALOGY:
  Earth = natural convective heat exchanger
  Heat source: radioactive decay in crust + core cooling (primordial heat)
  Hot side: core-mantle boundary (CMB, ~3500°C, ~135 GPa)
  Cold side: ocean floor (0°C, ~250 MPa)
  Convection cells: upwelling at mid-ocean ridges, downwelling at subduction zones

  Nusselt number Nu = convective / conductive heat transfer:
    Nu = (q_conv × d) / (k × ΔT)
    Mantle Nu ~ 10–20: convection enhances cooling ~10–20× over pure conduction
    Similar to forced convection in industrial heat exchangers (Nu ~ 100–1000)

NON-NEWTONIAN VISCOSITY:
  Mantle viscosity (10²⁰–10²¹ Pa·s) is strongly T- and P-dependent
  Power-law creep: ε̇ ∝ σⁿ (n = 3–5 for dislocation creep)
  → Analogous to non-Newtonian fluids in polymer processing or lava flows
  → Makes numerical simulation harder: viscosity varies 10⁴× across domain
```

### Heat Sources

```
Primordial heat:  accretion + core formation (~10¹⁰ years ago)
                  Still contributing ~30% of surface heat flow

Radioactive decay: ²³⁸U → ²⁰⁶Pb  (t½ = 4.47 Gyr)
                   ²³⁵U → ²⁰⁷Pb  (t½ = 704 Myr)
                   ²³²Th → ²⁰⁸Pb (t½ = 14.0 Gyr)
                   ⁴⁰K → ⁴⁰Ar   (t½ = 1.25 Gyr)
                   Concentrated in crust (incompatible elements)
                   ~70% of surface heat flow

Surface heat flow: ~80 mW/m² average; ~100 mW/m² ocean; ~65 mW/m² continent
```

---

## Plate Tectonics

### Plate Boundaries

```
DIVERGENT (constructive):
  Plates move apart → asthenospheric mantle upwells → decompression melting → basalt
  Mid-ocean ridges: ~65,000 km global system; seafloor spreading rate 1–10 cm/yr
  Continental rifts: East African Rift → eventually → new ocean basin
  Products: oceanic crust (5–10 km basalt + gabbro + peridotite), normal faults

CONVERGENT (destructive):
  Ocean-ocean: denser plate subducts → Wadati-Benioff zone → island arc volcanoes
               (fluid from slab → lowers melting point → wet melting → andesite/rhyolite)
  Ocean-continent: oceanic plate subducts → continental arc (Andes, Cascades)
  Continent-continent: both too buoyant to subduct → collision → mountain belt
                       (Himalayas: India-Eurasia; Alps: Africa-Eurasia)

TRANSFORM (conservative):
  Plates slide horizontally past each other → no creation/destruction of plate
  San Andreas (N. America-Pacific), North Anatolian, Dead Sea Transform
  Offset mid-ocean ridge segments → fracture zones

Plate driving forces:
  Slab pull: ~3× larger than ridge push (cold dense slab sinks)
  Ridge push: thermal expansion pushes plates away from ridge
  Mantle drag: debated; possibly resists motion in some places
```

### Paleomagnetism Evidence

```
Seafloor spreading confirmation (Vine-Matthews-Morley hypothesis, 1963):
  Basalt records Earth's magnetic field at time of formation
  Symmetric magnetic anomaly stripes parallel to ridge axis
  → spreading rate from stripe width + magnetic reversal timescale

Apparent Polar Wander (APW) paths:
  Each continent traces different path → must have moved relative to each other
  Same-age rocks on different continents record different pole positions

Paleolatitude from inclination:
  I = arctan(2 tan(λ))    (I = inclination, λ = paleolatitude)
  Rocks at equator: I = 0°; poles: I = 90°
  → reconstruct past positions of continents
```

### Wilson Cycle

```
Continental rifting
    → Initial rift basin (failed: aulacogen; or → narrow ocean: Red Sea stage)
    → Young ocean (Atlantic-type passive margins)
    → Mature ocean (Pacific-type, subduction begins on margins)
    → Closing ocean (Tethys-type, collision zones)
    → Mountain belt (Himalayas, Appalachians)
    → Erosion, peneplain
    → Next rifting cycle begins

Duration: ~500 Myr per cycle
Pangea assembly (~300 Ma) + breakup (~200 Ma): most recent cycle
```

---

## Geomagnetism

### The Geodynamo

```
Earth's magnetic field generated by convection in liquid outer core:
  Iron-nickel alloy (Fe + ~10% lighter elements: O, S, Si)
  Temperature range: ~4000 K (CMB) to ~6000 K (ICB)
  Convection driven by: compositional (light element release as inner core solidifies)
                       + thermal (secular cooling)

Self-sustaining dynamo requires:
  1. Electrically conducting fluid (liquid iron)
  2. Fluid motion (convection + rotation)
  3. Seed field (any initial field — maintained, not created, by dynamo)

Governing equations: MHD (magnetohydrodynamics)
  ∂B/∂t = ∇×(v×B) + η∇²B
  Magnetic Reynolds number: Rm = VL/η >> 1 (induction dominates diffusion)
  Earth's outer core: V ~10⁻³ m/s, L ~10⁶ m, η ~1 m²/s → Rm ~ 1000

Dipole approximation:
  ~90% of field at surface is dipole, tilted ~11° from rotation axis
  Remaining 10%: non-dipole field from higher harmonics
  Secular variation: field changes on decades–centuries timescale
```

### Field Reversals

```
Average reversal frequency: ~4–5 per Myr (not periodic)
Last reversal: Brunhes-Matuyama boundary at ~780 ka
Current: Brunhes normal polarity epoch

Transition duration: ~1000–10,000 years (geologically instantaneous)
During reversal: field weakens to ~10–20% of normal, multi-polar structure
South Atlantic Anomaly: current weak spot (~30% weaker) — NOT a reversal precursor (probably)

Paleomagnetic record:
  Marine sediment cores: 0–5 Ma reversals well-constrained
  GPTS (Geomagnetic Polarity Time Scale): ~160 Myr (seafloor spreading history)
  Older: baked rocks, flood basalts

Excursions: field dips/partially reverses but recovers (Laschamp at ~41 ka)
```

---

## Gravitational Field and Isostasy

### The Geoid

```
Earth's true gravitational equipotential surface (≈ mean sea level extended under continents)
Deviations from reference ellipsoid: ±100 m (geoid undulations)

Geoid highs: dense material (subducted slabs, ancient cratons)
Geoid lows: ancient subduction zones, hot upwellings

Measured by:
  GRACE: satellite pair → differential acceleration → gravity anomalies
  GOCE: gravity gradient tensor → detailed geoid

Gravity anomalies:
  Free-air: measured − theoretical; reflects topography + sub-surface density
  Bouguer: free-air corrected for topography → sub-surface density anomalies
  Isostatic: after removing isostatic compensation → remaining tectonic anomalies
```

### Isostasy

```
Principle: continental/mountain topography "floats" on denser mantle.
Two end-member models:

AIRY MODEL (local compensation):
  Thicker crust (mountain root) = high topography compensated by deep crustal keel
  Like icebergs: higher → deeper root
  h/r = (ρ_mantle − ρ_crust)/ρ_crust   (ratio of root to height)
  Crustal density ~2.8 g/cm³, mantle ~3.3 g/cm³:
  Root ≈ h × (2.8/(3.3−2.8)) = 5.6h   (mountains ~5–6× deeper root)

PRATT MODEL (lateral density variation):
  Same compensation depth everywhere; mountains have lower density
  Applicable to: mid-ocean ridges (hot/less-dense mantle), rifts

Isostatic rebound:
  Remove load (melt ice sheet) → mantle flows in → surface rises
  Scandinavia: still rising ~10 mm/yr from Pleistocene ice unloading
  Rate limited by mantle viscosity: time constant ~10⁴ yr
  Used to constrain mantle viscosity profile
```

---

## Decision Cheat Sheet

| Question | Concept | Key indicator |
|----------|---------|--------------|
| Why is the outer core liquid? | S-wave shadow zone | S-waves absent beyond 103° → liquid outer core |
| What drives plate tectonics? | Slab pull dominates | Cold dense subducting lithosphere sinks — major driver |
| How do we know mantle temperature? | Seismic tomography | Fast = cold, slow = hot; subducted slabs image as fast |
| Why do island arcs have explosive volcanoes? | Wet melting | Water from subducting slab → low melting point → silicic magma → high viscosity → explosive |
| Why are mountains in isostatic equilibrium? | Crustal root | Continental crust floats; high topography needs deep root |
| How old is the seafloor? | Magnetic anomalies | Oldest: ~200 Ma at subduction zones; all older crust subducted |
| Why does Scandinavia still rise? | Glacial isostatic adjustment | Mantle flow (η~10²¹ Pa·s) slowly responding to ice sheet removal |
| What causes normal vs reverse faults? | Stress regime | Extension → normal; compression → reverse/thrust |
| How is magnetic reversal recorded? | Seafloor spreading | Symmetric magnetic stripes about mid-ocean ridge |

---

## Common Confusion Points

**Tectonic plates ≠ continents**
Tectonic plates include both continental and oceanic lithosphere.
The Pacific plate is almost entirely oceanic. The North American plate includes
half the Atlantic Ocean floor. Plate boundaries cut through oceans and continents.

**Mantle is solid, not liquid**
Mantle rock is solid at seismic timescales (S-waves propagate through it).
At geological timescales (~10⁴–10⁹ years), it flows viscously.
High pressure suppresses melting — the mantle is hotter than the solidus of surface rock
but below the high-pressure solidus. Only decompression (rising material) or
water addition (subduction) melts it.

**Magnetic north ≠ geographic north**
Magnetic north (where compass points) is currently ~11° offset from geographic (rotation axis) north.
It wanders on decadal timescales (secular variation).
For paleomagnetic work: paleolatitude from paleomagnetic inclination gives paleogeographic
latitude, not paleomagnetic latitude — different things.

**Hot spots are not all the same**
"Hot spot" loosely means a volcanic chain not explained by plate boundary volcanism.
Some (Hawaii) are thought to have deep mantle plume origins. Others (Yellowstone)
may be shallow lithospheric processes. Plume existence is debated for many hotspots.
The plume hypothesis (Morgan 1971) is well-established for Hawaii, Iceland, Reunion —
less so for 40+ other "hot spots."

**Earthquake magnitude ≠ intensity**
Magnitude (Mw): single number, intrinsic property of the earthquake (energy released)
Intensity (MMI): local shaking at a specific location — depends on distance, depth,
local geology (amplification in sediment basins), building quality
A M7.0 at 10 km depth is far more damaging than M7.0 at 100 km depth.
