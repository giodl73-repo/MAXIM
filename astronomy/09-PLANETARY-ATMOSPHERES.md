# Planetary Atmospheres
## Structure, Escape, Greenhouse, Circulation, Comparative Planetology, Biosignatures

---

## Big Picture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                     PLANETARY ATMOSPHERE OVERVIEW                          │
│                                                                            │
│   ORIGIN                RETENTION              MODIFICATION                │
│   ──────                ─────────              ────────────                │
│   Primordial H/He  ──►  Mass (gravity) ──►     Photochemistry             │
│   Volcanic outgas  ──►  Temperature   ──►      Biology (O₂, CH₄, N₂O)   │
│   Cometary delivery──►  Magnetic field ──►     Impacts (catastrophic)     │
│   Late veneer      ──►  Stellar wind   ──►     Climate feedbacks          │
│                                                                            │
│   KEY PARAMETERS:                                                          │
│   Scale height   H = kT/mg  (homogeneous approximation)                   │
│   Jeans escape   λ_J = R·g·m/(kT) — thermal loss parameter               │
│   Optical depth  τ = ∫κρ dr — controls greenhouse effect                  │
│   Radiative forcing ΔF = 5.35 ln(C/C₀) W/m² for CO₂                     │
│                                                                            │
│   SOLAR SYSTEM ATMOSPHERE CENSUS:                                          │
│   Venus  92 bar CO₂    737 K   stagnant, extreme greenhouse               │
│   Earth   1 bar N₂/O₂  288 K   active biosphere + moderate greenhouse    │
│   Mars  0.006 bar CO₂  210 K   thin, partially frozen, ancient thick?    │
│   Titan   1.5 bar N₂   94 K    hydrocarbon haze, CH₄ cycle               │
│   Jupiter  ~1 bar H₂   165 K   upper deck — no solid surface             │
│   Triton  0.00001 bar N₂ 38 K  cryo-active nitrogen geysers              │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Atmospheric Structure and Scale Height

### Vertical Layers

```
Altitude
(km)
 500 ┤ Exosphere: mean free path > scale height; thermal escape
     │
 100 ┤ Thermosphere: T rises with EUV absorption (O₂, N₂ dissociation)
     │ Earth: 180–1800 K depending on solar activity
  80 ┤─────────────── Mesopause (~86 km, coldest point −100°C) ─────────
  80 ┤ Mesosphere: T decreasing upward; meteor ablation zone
     │
  50 ┤─────────────── Stratopause (~50 km) ────────────────────────────
  50 ┤ Stratosphere: T rising upward (O₃ absorbs UV at 200–315 nm)
     │ Stable: warmer above cold → no vertical mixing (unusual)
  12 ┤─────────────── Tropopause (~12 km, varies 8–16 km) ─────────────
  12 ┤ Troposphere: T decreasing at ~6.5 K/km (env. lapse rate)
     │ Unstable: weather, convection, bulk of mass (75%)
   0 ┤ Surface
```

**Dry adiabatic lapse rate**: for an air parcel lifted without condensation:

$$\Gamma_d = \frac{g}{c_p} = \frac{9.81}{1005} \approx 9.8 \text{ K/km}$$

Environmental lapse rate ~6.5 K/km < 9.8 → stable against dry convection (but conditionally unstable if moist, since condensation releases latent heat, reducing effective lapse rate).

### Scale Height

For an isothermal atmosphere in hydrostatic equilibrium:

$$P(z) = P_0 \exp\left(-\frac{z}{H}\right), \quad H = \frac{k_B T}{\bar{m} g}$$

where m̄ = mean molecular mass.

| Planet | T (K) | m̄ (amu) | g (m/s²) | H (km) |
|--------|--------|----------|----------|--------|
| Earth | 250 | 29 | 9.81 | 8.5 |
| Venus | 450 | 44 (CO₂) | 8.87 | 15.9 |
| Mars | 210 | 44 (CO₂) | 3.72 | 11.1 |
| Titan | 94 | 28 (N₂) | 1.35 | 21 |
| Jupiter | 165 | 2.2 | 24.8 | 27 |

Scale height determines how far the atmosphere extends, how quickly pressure falls, and the effective radiating level for thermal emission.

---

## 2. Atmospheric Escape Mechanisms

### Thermal (Jeans) Escape

At the exobase (mean free path ~ scale height, ~500 km for Earth), fast molecules in the Maxwellian tail escape if v > v_esc.

**Jeans escape parameter**:

$$\lambda_J = \frac{G M m}{r k_B T} = \frac{m g r}{k_B T}$$

λ_J >> 6 → atmosphere stable. λ_J < 3 → rapid hydrodynamic escape.

| Body | H loss | He loss | H₂O loss | Comment |
|------|--------|---------|----------|---------|
| Earth (λ_J ~ 30 for H) | Slow leakage | Moderate | Negligible | Cold trap at tropopause |
| Mars (λ_J ~ 12 for H) | Fast | Fast | Fast | Lost most volatiles |
| Venus (λ_J ~ 15 for H) | Fast | Fast | Lost to photo | D/H ratio × 100 × Earth |
| Titan (λ_J ~ 60 for N₂) | N₂ retained | — | — | Massive N₂ for its gravity |

**Cold trap** (Earth's tropopause at −80°C): water vapor condenses out before reaching the exobase → H₂O escapes slowly. Venus lacks a cold trap (no stratospheric temperature inversion above the cloud deck) → water vapor reaches the thermosphere → photodissociation → H escapes to space.

### Non-Thermal Escape Mechanisms

| Mechanism | Process | Dominant at |
|-----------|---------|-------------|
| Photodissociation + Jeans | UV breaks molecule → light fragment escapes | All planets |
| Ion pickup | Solar wind ion + neutralized → energized to escape | Unmagnetized planets (Mars, Venus) |
| Sputtering | Energetic ions knock atmospheric atoms to >v_esc | Mars |
| Hydrodynamic escape | Massive thermal outflow in bulk | Hot, young planets; close-in exoplanets |
| Charge exchange | Solar wind proton + O atom → fast neutral O | Mars (MAVEN measured ~100 g/s O) |

**Mars vs Earth magnetosphere**: MAVEN shows Mars loses ~100 g/s of oxygen ions to solar wind pickup. Earth's dipole deflects the solar wind. Over 4 Gyr, Mars lost ~10–100 mbar equivalent — significant fraction of a thicker early atmosphere.

---

## 3. The Greenhouse Effect — Physics and Runaway

### Radiative Energy Balance

For a planet with no greenhouse gases (bare rock):

$$T_{\text{eq}} = T_\odot \left(\frac{R_\odot}{2 a}\right)^{1/2} (1-A)^{1/4}$$

Earth: A = 0.30, a = 1 AU → T_eq = 255 K. Observed T_s = 288 K → greenhouse provides **+33 K**.

### Two-Layer Greenhouse Model

Atmosphere is more transparent at short wavelengths (visible solar), opaque at long (IR thermal):

```
Space
  ↑ OLR (outgoing longwave radiation)
  │
Atmosphere (T_A):  Absorbs upwelling LW, emits up + down
  ↑ ↓
Surface (T_S):     Absorbs solar + atmospheric downwelling LW
```

With a single optically thick layer:

$$T_S^4 = 2 T_A^4, \quad T_A \approx T_{\text{eq}}$$

Each optically thick layer added warms the surface by factor 2^(1/4) ≈ 1.19. Real case: CO₂ 15-μm band, H₂O 6.3-μm band, plus window regions.

**Radiative forcing from CO₂** (logarithmic — line wings broaden):

$$\Delta F = 5.35 \ln(C/C_0) \; \text{W/m}^2$$

Doubling CO₂: ΔF = 3.7 W/m². Equilibrium climate sensitivity (ECS) = 3°C per doubling (likely range 2.5–4°C, IPCC AR6).

### Runaway Greenhouse

**Runaway condition** (Ingersoll 1969, Kasting 1988): if solar flux exceeds a critical threshold (~310 W/m² for an Earth-like atmosphere), water-vapor feedback becomes unregulated:

1. Warming → more H₂O evaporation → more greenhouse
2. OLR saturates at ~282 W/m² (Nakajima limit) — cannot increase further regardless of surface temperature
3. Planet heats until oceans fully evaporate
4. Photodissociation of H₂O → H escapes to space → permanent desiccation

**Moist greenhouse**: onset at ~1.1 AU. Stratosphere becomes wet → H loss begins but planet not fully desiccated. Venus crossed the runaway threshold sometime in its past.

**Evidence for Venus water loss**: D/H ratio ~120× Earth's. Deuterium is heavier → escapes more slowly → preferentially retained. Venus likely had liquid water early (when the young Sun was dimmer) and lost it as solar luminosity increased.

---

## 4. Atmospheric Circulation

### Driving Forces

```
FORCES GOVERNING CIRCULATION
  Differential heating (equator vs poles) → horizontal pressure gradient
  Rotation (Coriolis) → deflects NH flows rightward, SH leftward
  Friction (surface drag) → retards near-surface flow
  Moist convection + baroclinic instability → weather eddies
```

**Rossby number** Ro = U/(fL): ratio of inertial to Coriolis force. f = 2Ω sin φ.

- Ro << 1: rotation dominates → geostrophic balance: winds flow *along* isobars (extratropical Earth)
- Ro >> 1: rotation unimportant → direct overturning (Hadley cells)

### Earth's Three-Cell Circulation

```
90°N  ┤  Polar Cell (dry, sinking at pole)
60°N  ┤  ──── Ferrel Cell (indirect; mid-latitude westerlies) ────
30°N  ┤  Subtropical jet / High pressure (Hadley descent → deserts)
 0°   ┤  ════ ITCZ (rising, wet, deep convection) ════════════════
30°S  ┤  (symmetric)
60°S  ┤
90°S  ┤
```

**Hadley cell**: equatorial air rises → moves poleward aloft → sinks at ~30° → returns equatorward as trade winds. Coriolis deflects trades westward → easterlies. Hadley descent causes subtropical deserts (Sahara, Arabian, Australian, Atacama, Kalahari).

**Ferrel cell** (mid-latitudes): indirect cell driven by baroclinic eddies (weather systems). Produces westerly winds → temperate weather moves west→east.

**Jet streams**: arise from sharp temperature gradient at tropopause. Polar jet ~300 mb; subtropical jet ~200 mb.

### Venus: Super-Rotation

Venus's cloud tops rotate at ~4 km/s — completing an atmospheric circuit in ~4 Earth days, while the surface rotates in 243 Earth days (retrograde). The entire atmosphere super-rotates 60× faster than the surface. Mechanism: Gierasch-Rossow (thermal tides pump angular momentum upward from surface; eddies redistribute it poleward).

### Mars: Dust Storms

Mars global dust storms occur every few Martian years, particularly near southern-hemisphere perihelion. Dust absorbs solar radiation → warms atmosphere → increases convection → lifts more dust (positive feedback). Global storms can last months and raise temperatures ~30 K. Dust storms threatened InSight's solar panels (ended the mission in 2022).

**Seasonal pressure variation**: CO₂ atmosphere partially freezes at the winter pole (up to 30% of total atmosphere) → surface pressure varies ±25% annually. Unique in the solar system.

### Titan: Hydrocarbon Cycle

Titan's N₂ atmosphere (95%) + CH₄ (5%) mirrors Earth's water cycle:

- Methane lakes at poles (Ontario Lacus, Ligeia Mare)
- CH₄ evaporates → clouds → rain at high latitudes
- Photochemical tholins (UV breaks CH₄ → complex organic haze)
- CH₄ should be depleted in ~30 Myr without replenishment → geological resupply suspected
- Dragonfly (launch 2028, arrival 2034): rotorcraft lander to sample organic chemistry

---

## 5. Comparative Climatology — Venus, Earth, Mars

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    TERRESTRIAL ATMOSPHERE COMPARISON                         │
│                                                                              │
│  Property         Venus          Earth          Mars                        │
│  ─────────        ─────          ─────          ────                        │
│  P_surface        92 bar         1 bar          0.006 bar                   │
│  T_surface        737 K          288 K          210 K (mean)                │
│  Composition      96% CO₂, 3.5% N₂ 78% N₂, 21% O₂ 96% CO₂, 2.6% N₂      │
│  Greenhouse ΔT    +505 K         +33 K          +5 K                        │
│  Albedo           0.77           0.30           0.25                        │
│  T_eq (calc)      232 K          255 K          210 K                       │
│  Rotation         243 days retro  24 hr         24.6 hr                     │
│  Obliquity        177°           23.4°          25.2°                       │
│  Magnetic field   None           Active dipole  Ancient remnant             │
│  Water            None (lost)    Oceans         Ice + permafrost            │
│  Solar flux       2601 W/m²      1361 W/m²      588 W/m²                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Why Venus is hotter than expected**: absorbs less solar energy than Earth per unit area (~162 vs ~240 W/m² after albedo) yet is 449 K hotter. The 92-bar CO₂ atmosphere traps essentially all IR — this is the strongest greenhouse demonstration in the solar system.

**Mars past**: valley networks, delta sediments (Jezero Crater), outflow channels, and hydrated minerals all imply liquid surface water ~3.5–3.7 Gya. **Early Mars climate problem**: thick CO₂ alone cannot warm Mars enough (CO₂ also Rayleigh-scatters sunlight). Proposed supplements: H₂ (collision-induced absorption), SO₂ (volcanic), CH₄. Unresolved.

**Venus-Earth-Mars divergence**: all three started with broadly similar volatile inventories. Venus received more solar flux → lost water → CO₂ built up (no carbonate-silicate cycle without liquid water) → runaway. Mars: small mass + early dynamo loss → atmospheric escape. Earth: landed in the sweet spot + active carbonate-silicate cycle regulates CO₂ over Myr timescales.

---

## 6. Titan and Outer Planet Atmospheres

### Gas Giant Structure (Jupiter)

```
P level    Layer            Feature
~1 mbar    Stratosphere     CH₄ absorption; auroral chemistry
   1 bar   Tropopause       −108°C; NH₃ ice cloud tops
 1–5 bar   Troposphere      NH₃ clouds (white zones), NH₄SH (brown belts)
 ~5 bar    H₂O clouds       Inferred; not directly observed
 ~1 Mbar   H₂ metallization  Hydrogen becomes metallic conductor
 ~45 Mbar  Helium rain      He droplets form + fall (especially Saturn)
```

**Belts and zones**: zones (light) are rising, cold; belts (dark) are sinking, warm. Wind speeds at boundaries: up to 150 m/s (Jupiter) and 500 m/s (Neptune).

**Great Red Spot**: anticyclonic storm (southern hemisphere), ~1.3× Earth diameter, >150 years observed, winds ~130 m/s.

**Saturn**: equatorial jet 400 m/s. Hexagonal polar vortex (standing Rossby wave). Helium rain releases gravitational energy → Saturn radiates 1.8× more heat than absorbed.

**Internal heat**: Jupiter radiates 1.67× absorbed solar energy (~2–3×10¹⁷ W excess). Neptune: large internal heat excess despite low insolation. Source: Kelvin-Helmholtz contraction (residual formation energy), plus Saturn's helium rain.

**Juno findings**: Jupiter's core is "fuzzy" — dilute mixture of rock + ice + H extending over ~0.3 R_J. Likely result of a giant impact mixing a crisp rock core during early solar system history.

---

## 7. Biosignatures in Spectra

### The Thermodynamic Argument

A lifeless atmosphere equilibrates to its lowest free-energy state. Life maintains disequilibrium by continuously regenerating thermodynamically unstable combinations.

**Sagan et al. 1993**: used Galileo flyby of Earth as an unbiased search for life. Found: O₂ (21%) + CH₄ (1.7 ppm) coexisting — thermodynamically impossible at equilibrium. Also: narrowband modulated radio emissions (technosignature). This demonstrated that remote detection of life is in principle possible.

### Key Biosignature Gases

| Gas | Biogenic source | Abiotic mimics | Key spectral feature |
|-----|----------------|----------------|----------------------|
| O₂ (21%) | Oxygenic photosynthesis | Photolysis (limited) | 0.76 μm, NIR bands |
| O₃ (ppm) | Photochemistry from O₂ | None efficient | 9.6 μm; strong proxy for O₂ |
| CH₄ (1.7 ppm) | Methanogens, wetlands | Volcanic, serpentinization | 7.7 μm, 3.3 μm |
| N₂O (ppm) | Denitrifying bacteria | Lightning (trace) | 8.5, 17 μm |
| DMS (ppt) | Phytoplankton | None known | Weak UV features |

**O₂ + CH₄ together** is the canonical biosignature pair — abiotic sources cannot maintain both simultaneously at high concentrations.

**Abiotic O₂ false positive**: H-poor planets can build O₂ from photolysis (H escapes, O accumulates) without life — particularly relevant for M-dwarf planets receiving intense early XUV (Luger & Barnes 2015). TRAPPIST-1 planets may have built up abiotic O₂ during pre-main-sequence phase.

### JWST Transmission Spectroscopy

Starlight filters through the planet's atmospheric limb during transit. Wavelength-dependent absorption reveals molecular features.

Current results:
- **WASP-39b** (hot Jupiter): first clear exoplanet CO₂ detection (JWST first-light science, 2022)
- **TRAPPIST-1b**: MIRI photometry → no thick CO₂ atmosphere; bare rock or very thin atmosphere
- **TRAPPIST-1c**: NIRSpec + MIRI → no thick CO₂; thermal emission consistent with bare rock
- **K2-18b**: NIRSpec → CO₂ detected; possible DMS/CH₃SH (Madhusudhan et al. 2023) — disputed; sub-Neptune possibly a "Hycean world" (H₂ ocean)

Signal is ~10–100 ppm transit depth variation per molecular feature — requires systematic error below this level.

### Surface Biosignatures

**Vegetation red edge (VRE)**: chlorophyll absorption cutoff at ~700 nm → sharp reflectance jump. Detectable in Earth-shine measurements (spectroscopy of moonlight). HWO/LUVOIR targets: ~1% disc-averaged VRE signal.

**Temporal variability**: correlated reflectance variations at orbital timescales (seasons, rotation) can indicate biological patterning.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What determines atmospheric scale height? | H = kT/(mg) — temperature and mean molecular mass |
| Why does Mars have a thin atmosphere? | Small gravity + no magnetosphere → solar wind erosion over 4 Gyr |
| Why is Venus so hot despite high albedo? | 92 bar CO₂: greenhouse +505 K overwhelms the albedo cooling |
| What triggers runaway greenhouse? | OLR saturates at ~282 W/m²; H₂O feedback becomes unstoppable |
| Why doesn't water escape from Earth easily? | Cold trap at tropopause (−80°C): water condenses before reaching exobase |
| What makes O₂+CH₄ a biosignature? | Thermodynamic disequilibrium — they react; abiotic sources can't maintain both |
| Best current JWST biosignature result? | WASP-39b CO₂ confirmed; TRAPPIST-1b,c lack thick atmospheres |
| What is Venus super-rotation? | Atmosphere circles planet in 4 days; surface rotates in 243 days |
| Why does Mars have 25% pressure swings? | CO₂ freezes/sublimates seasonally at poles — unique in solar system |
| What is the vegetation red edge? | Chlorophyll absorption cutoff at ~700 nm → sharp reflectance increase |
| Jeans escape parameter? | λ_J = mGM/(rkT); λ_J < 3 → rapid escape |

---

## Common Confusion Points

**"The greenhouse effect is CO₂ heating the atmosphere"**
CO₂ does not generate heat — it *traps* outgoing IR. The surface and troposphere warm until a new radiative equilibrium is established at higher temperature. Energy is conserved; CO₂ raises the effective emission altitude, reducing OLR and requiring higher surface temperature to compensate.

**"Venus is hot because it's closer to the Sun"**
Venus's high albedo (0.77) means it absorbs *less* solar flux than Earth (~162 vs ~240 W/m²). T_eq = 232 K — actually colder than Earth's 255 K by the Sun-alone calculation. The observed 737 K requires the +505 K greenhouse. Proximity is a minor contributor.

**"Mars lost its atmosphere because it lost its magnetic field"**
Partial. The magnetic field is important but not sufficient. Mars also has 38% of Earth's gravity, which lowers escape velocity and means any loss mechanism operates faster. Even with a magnetosphere, Mars's small mass would have made atmospheric retention difficult over Gyr.

**"O₂ is always a biosignature"**
Not reliably in isolation. Abiotic O₂ can build up on planets losing hydrogen faster than oxygen (H₂-poor upper atmospheres). Particularly relevant for M-dwarf planets: intense early XUV irradiation of the pre-main-sequence phase could drive hydrogen escape and leave behind O₂-rich but lifeless atmospheres.

**"Transmission spectroscopy directly measures the surface"**
It probes the terminator limb at τ ~ 1 levels — typically millibar to microbar pressures. Surface conditions are accessible only if the atmosphere is very thin. Thermal emission spectroscopy (phase curves) probes deeper layers; direct imaging ground-truth requires very large telescopes (HWO era).

**"Gas giants don't have surfaces so interior structure doesn't matter"**
The lack of a crisp surface doesn't mean structure is irrelevant. Gravity measurements (Juno), ring seismology (Saturn), and normal mode oscillations probe the interior. The distribution of hydrogen, helium, and rock determines moment of inertia, internal heat, and magnetic field generation. Jupiter's "fuzzy core" finding (from Juno) changed our understanding of giant planet formation.
