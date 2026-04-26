# Exoplanets
## Detection Methods, Demographics, Characterization, Habitability, JWST Era

---

## Big Picture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        EXOPLANET LANDSCAPE                                 │
│                                                                            │
│   DETECTION ERA     MISSION           PLANETS FOUND                        │
│   ────────────      ───────           ─────────────                        │
│   1992–1995         Ground RV         First confirmed (51 Peg b, 1995)     │
│   2004–2013         Ground transit    WASP, HAT surveys                    │
│   2009–2018         Kepler            >2600 confirmed; statistics          │
│   2018–present      TESS              All-sky; bright nearby stars         │
│   2013–present      Gaia              Astrometric detections               │
│   2021–present      JWST              Atmospheric characterization         │
│   ~2030s+           PLATO             Rocky planets around FGK stars       │
│   ~2040s            HWO / LUVOIR      Direct imaging, rocky planet spectra │
│                                                                            │
│   POPULATION CENSUS (confirmed ~5700+ as of 2025):                         │
│   Gas giants (R > 6 R_E)          ~5%  — overrepresented (detection bias)  │
│   Sub-Neptunes (1.7–4 R_E)        ~36% — most common type                │
│   Super-Earths (1–1.7 R_E)        ~30% — rocky side of Fulton gap        │
│   Earths (< 1.2 R_E)              ~13% — difficult to detect               │
│   Hot Jupiters (a < 0.1 AU, large) ~1%  — rare but first detected        │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Detection Methods

### Transit Method (Kepler/TESS)

A planet crossing the stellar disk blocks a fraction of starlight:

$$\frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2$$

Earth/Sun: ΔF/F = (6371/696000)² = 8.4×10⁻⁵ (84 ppm) — measurable by Kepler.
Hot Jupiter/Sun: ΔF/F ~ 1% — ground detectable.

**Transit probability**: p = R_\star/a (geometric probability of alignment)

| Planet | a | Transit prob. |
|--------|---|---------------|
| Hot Jupiter (a = 0.05 AU) | 0.05 AU | R_☉/0.05 AU = 9.3% |
| Earth (a = 1 AU) | 1 AU | R_☉/1 AU = 0.47% |
| Jupiter (a = 5.2 AU) | 5.2 AU | 0.089% |

**Limb darkening**: stellar disc is not uniform — center is brighter, edges darker. Transit light curve shape encodes this; fitting limb darkening coefficients tightens planet parameter constraints.

**Transit duration**: T_dur = (P/π) · arcsin(√((R_\star + R_p)² - b²)/a), where b = impact parameter.

**Geometric bias**: transit method strongly favors close-in planets (high probability + short period → multiple transits in mission lifetime). Kepler observed for 4 years → minimum 3 transits required → hard to detect P > 400 days.

### Radial Velocity (RV)

Doppler shift of stellar spectral lines due to reflex motion around the center of mass.

**RV semi-amplitude**:

$$K = \frac{2\pi a_\star \sin i}{P \sqrt{1-e^2}} = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{M_p \sin i}{(M_\star + M_p)^{2/3}} \frac{1}{\sqrt{1-e^2}}$$

RV measures **M_p sin i** — the inclination degeneracy. If transit is also observed → i ≈ 90° → true mass known.

| Planet | K (m/s) | Comment |
|--------|---------|---------|
| 51 Peg b (hot Jupiter) | 56 m/s | Discovered Mayor & Queloz 1995 |
| Jupiter analog (5 AU) | 12 m/s | Detectable with HARPS |
| Earth analog | 0.09 m/s | Below current state-of-art (~0.3 m/s) |
| Venus analog | 0.086 m/s | Similar difficulty |

Current best RV precision: ESPRESSO ~0.3 m/s; NEID ~0.3 m/s. Stellar activity (spots, jitter) is the limiting noise source for Earth analogs.

### Direct Imaging

Block stellar light with a coronagraph or starshade, then detect the planet directly.

**Inner working angle (IWA)**: minimum angular separation resolvable after coronagraphic suppression. For a 30-m telescope at 1 μm: λ/D = 7 mas. Earth at 10 pc = 100 mas → detectable with adequate contrast ratio.

**Contrast requirement**: Earth in reflected light at 1 AU: flux ratio ~10⁻¹⁰ at visible wavelengths ("Earth contrast"). Roman Space Telescope coronagraph (2027): targets ~10⁻⁸ (giant planets). HWO (Habitable Worlds Observatory, ~2040): targets 10⁻¹⁰ for rocky planets.

**Current detections**: HR 8799 b,c,d,e (4 planets, directly imaged — young, hot, self-luminous, massive), Beta Pictoris b. These are young giant planets still radiating formation heat — much easier than reflected-light Earth analogs.

### Microlensing

Background star (source) lensed by a foreground star with a planet. The planet creates a brief perturbation on the Einstein ring crossing event.

$$\theta_E = \sqrt{\frac{4GM}{c^2} \cdot \frac{D_{LS}}{D_L D_S}}$$

**Unique capability**: sensitive to planets at 1–5 AU (the "snowline") and even free-floating planets (rogue planets). Mass function deduced statistically. Roman Space Telescope will survey the galactic bulge for microlensing — expected to find thousands of cold planets.

**Limitation**: events are non-repeating; no follow-up. Usually can't determine host star mass/distance precisely. Not useful for characterization.

### Astrometry (Gaia)

Measure stellar wobble in the plane of the sky. Sensitive to long-period, massive planets around nearby stars.

**Gaia astrometric signal**: θ = a_\star/d = (M_p/M_\star)(a/d)

Gaia DR3 (2022) + DR4 (2025): hundreds to thousands of giant planet candidates from astrometry. Complements RV — where RV sees sin i, astrometry sees cos i → combined gives true mass.

**Limitation**: poor for close-in planets (small a → small wobble). Also takes long for long-period planets.

---

## 2. The Kepler/TESS Revolution — Population Statistics

### Occurrence Rates (η)

η_⊕ (Earth-sized, habitable zone): estimated 0.1–0.5 for FGK stars; ~0.16 for G dwarfs (Petigura et al. 2013). For M dwarfs: ~0.5–1.0 (TRAPPIST-1 shows multiple rocky planets are common around M stars).

**Key demographic results**:
- Super-Earths and sub-Neptunes are the *most common* planet type (no analog in the solar system)
- Hot Jupiters rare (~0.5–1% of stars)
- Planet occurrence increases at small radii, decreasing sharply above ~4 R_E
- Multi-planet systems are common; many near mean-motion resonances (migration signature)

### The Fulton Gap (Radius Gap)

```
Planet frequency
    │   peak
    │   here
    │    │
    │    │          peak
    │    │          here
    │    │           │
    └────┴───────────┴──────── R/R_E
         1.3       2.4
         │         │
         super-    sub-Neptune
         Earth     region
              1.7
         ← Fulton gap →
```

CKS survey (California-Kepler Survey, Fulton et al. 2017): bimodal distribution of planet radii with a gap at ~1.7 R_E.

**Mechanism — photoevaporation model** (Owen & Wu 2017): planets near ~1.7 R_E are borderline — either they retain their H/He envelope (stay as sub-Neptunes, R > 2 R_E) or lose it to EUV irradiation (become bare rocky cores, R < 1.5 R_E). The gap is depopulated because the timescale for envelope loss at these radii is short.

**Alternative — core-powered mass loss** (Ginzburg et al. 2018): heat from the cooling rocky core drives atmospheric escape (slower, interior-driven rather than stellar-driven). Both mechanisms may operate.

---

## 3. Mass-Radius Diagram and Bulk Composition

### The M-R Plane

Different internal compositions define families of M-R curves:

```
R/R_E
  4 │                     gas dwarfs / sub-Neptunes
    │                   ╱  (H₂/He envelope)
  3 │                  ╱
    │            water worlds (H₂O-dominated)
  2 │          ╱
    │         ╱
    │    ────────────── Fulton gap ──────────────
  1 │  ╱   rocky Earth-like
    │ ╱
  0.5│ iron-dominated (Mercury-like)
    └──────────────────────────────── M/M_E
       1    2    5    10   20   50  100
```

**Equations of state used**:

| Layer | Material | EOS |
|-------|----------|-----|
| Iron core | Fe (hcp at >100 GPa) | Vinet; Dewaele et al. 2006 |
| Silicate mantle | MgSiO₃ bridgmanite | Birch-Murnaghan 3rd order |
| Water/ice layer | Phase VII, X | IAPWS + ab initio |
| H/He envelope | Ideal + metallic | Chabrier SCvH |

**Degeneracy problem**: a given (M, R) pair is consistent with multiple compositions. Example: 5 M_E, 1.6 R_E could be a rocky planet with thin H₂ envelope OR a water-rich planet OR a differentiated rocky + thin water. Spectroscopy needed to break the degeneracy.

**JWST 55 Cancri e** (M = 8.0 M_E, R = 1.88 R_E): MIRI observations show thermal phase curve → dayside temp ~2300 K, significant heat redistribution → possible thick atmosphere of CO/CO₂ from magma ocean outgassing.

---

## 4. The Habitable Zone

### Classical Habitable Zone (Kasting 1993; Kopparapu 2013)

Temperature range supporting liquid surface water. Defined by flux limits:

```
            Inner edge         Outer edge
            (runaway GH)       (max CO₂)
               │                   │
    Venus─────┤                   │
              │                   ├───────Mars
              │        Earth      │
              │          ★        │
    0.75 AU   │        1 AU       │  1.77 AU
 (recent Venus)                 (early Mars)
```

**Conservative HZ** (Kopparapu 2013): 0.99–1.68 AU for the Sun.
**Optimistic HZ** (using Venus + early Mars evidence): 0.75–1.77 AU.

The boundaries depend sensitively on: CO₂ cloud feedback (not well modeled), H₂ greenhouse effect (extends HZ), planetary albedo, obliquity.

### Extended Definitions

| Zone | Definition | Comment |
|------|------------|---------|
| Classical HZ | Liquid water on surface | CO₂-H₂O climate models |
| Moist greenhouse | H₂O in stratosphere → H loss | Inner edge 1.01 AU |
| Maximum greenhouse | Max CO₂ before CO₂ condenses | Outer edge ~1.67 AU |
| H₂ HZ | H₂ greenhouse extends outer edge | Out to ~2.4 AU (Pierrehumbert & Gaidos) |
| Subsurface ocean HZ | Tidal/radioactive heating → liquid water anywhere | Europa, Enceladus — distance irrelevant |

### TRAPPIST-1 Habitable Zone

```
TRAPPIST-1 system (0.09 M☉, M8 dwarf):
  a    b    c    d    e    f    g    h
  |    |    |    |    |    |    |    |
        ─── ─── [──────HZ──────]
  b,c: too hot (Venus zone)
  d:   near inner edge
  e,f,g: in conservative HZ  ← prime targets
  h:   too cold
```

All 7 planets are Earth-sized (0.77–1.16 R_E). All are tidally locked (one face always toward the star). Orbital resonance chain: 8:5:3:2:4:3:2 (TRAPPIST-1 b:c:d:e:f:g:h approximately).

**Tidal locking challenge**: the dayside may be in runaway greenhouse; nightside may freeze. Atmospheric heat redistribution is crucial — models suggest TRAPPIST-1e,f,g could be habitable if they retain substantial atmospheres.

---

## 5. Atmospheric Characterization — JWST Era

### Transmission Spectroscopy Technique

Planet transits → starlight passes through atmospheric limb → wavelength-dependent absorption → transmission spectrum.

**Transit depth at wavelength λ**:

$$\delta(\lambda) = \left(\frac{R_p + n(\lambda) H}{R_\star}\right)^2 - \left(\frac{R_p}{R_\star}\right)^2 \approx \frac{2 R_p H}{R_\star^2} n(\lambda)$$

where n(λ) is the number of scale heights of opacity, H is the scale height. Signal per scale height: 2R_p H / R_\star².

For TRAPPIST-1 planets (R_\star = 0.12 R_☉, R_p ~ 1 R_E, H ~ 8 km): signal ~150 ppm per scale height — marginal even for JWST.

### JWST Instrument Modes for Atmosphere

| Mode | Wavelength | Molecules targeted |
|------|-----------|-------------------|
| NIRSpec PRISM | 0.6–5.3 μm | CO₂ (4.3 μm), H₂O, CH₄, CO |
| NIRSpec G395H | 2.87–5.27 μm | CO₂, H₂O |
| NIRISS SOSS | 0.6–2.8 μm | H₂O, K, Na |
| MIRI LRS | 5–14 μm | CO₂, O₃, NH₃, SO₂ |

### Key JWST Results

| Target | Result | Interpretation |
|--------|--------|----------------|
| WASP-39b (hot Jupiter) | CO₂ at 4.3 μm (first exoplanet CO₂) | Solar C/O; photochemistry detected |
| TRAPPIST-1b | No CO₂ feature; thermal emission matches bare rock | No thick CO₂ atmosphere |
| TRAPPIST-1c | Similar — no thick CO₂ | Not Venus-like |
| TRAPPIST-1g | Ongoing — habitable zone | Results pending |
| K2-18b (sub-Neptune) | CO₂ detected; CH₄ detected; possible DMS | Hycean world hypothesis; DMS disputed |
| 55 Cancri e | CO₂/CO in thermal phase curve | Volcanic atmosphere from magma ocean |
| LHS 1140b | CO₂ detected | First rocky HZ planet with atmosphere hints |

**K2-18b controversy**: Madhusudhan et al. (2023) reported possible dimethyl sulphide (DMS) — a biosignature — at ~3σ. Required follow-up before claims of biological origin are justified. The sub-Neptune size (~2.6 R_E) makes a surface ocean uncertain. May be a "Hycean" world — H₂-rich atmosphere over a deep liquid water ocean.

---

## 6. TRAPPIST-1 System Deep Dive

### System Architecture

```
TRAPPIST-1 system (star: 0.09 M☉, 0.12 R☉, T_eff = 2566 K, age ~7.6 Gyr)

Planet  a (AU)   P (days)   R/R_E   M/M_E    T_eq (K)    Zone
─────   ──────   ────────   ─────   ─────    ────────    ────
b       0.0115   1.51       1.116   1.374     400         Hot
c       0.0158   2.42       1.097   1.308     342         Hot
d       0.0223   4.05       0.788   0.388     288         Near-inner
e       0.0293   6.10       0.920   0.692     251         HZ ★
f       0.0385   9.21       1.045   1.039     219         HZ ★
g       0.0469   12.35      1.148   1.321     199         HZ ★
h       0.0619   18.77      0.773   0.326     173         Cold
```

**Resonance chain**: near 8:5:3:2:4:3:2 period ratios — evidence of disk migration bringing planets inward into resonance.

**Tidal locking**: all planets likely tidally locked (synchronous rotation). τ_lock ~ 1 Myr for the inner planets → well within stellar age. Permanent dayside/nightside temperature contrast.

**Atmospheric retention concern**: M dwarfs are magnetically active and emit high XUV flux, especially during their long pre-main-sequence phase (~1 Gyr for M8 star). TRAPPIST-1 planets may have received 10–1000× Earth's EUV dose during their formation. Whether any atmosphere survived depends on initial volatile inventory and magnetic shielding.

**Bulk densities** (from transit timing variations, Agol et al. 2021): all 7 planets have densities broadly Earth-like (3.7–7.6 g/cm³, ranging from water-rich to Earth-like to iron-rich). This constrains compositions but doesn't uniquely determine rock vs water vs ice fraction.

---

## 7. Hot Jupiters

### Formation and Migration

Hot Jupiters (HJs): gas giants with P < 10 days (a < 0.1 AU). No in-situ formation possible (insufficient disk material inside snowline for core accretion + no time for gravitational instability). Must have formed beyond ~3 AU and migrated inward:

**Disk migration (Type II)**: giant planet clears a gap; migrates with the disk on viscous timescale (~10⁵ yr). Natural outcome of core accretion + massive disk.

**High-eccentricity migration (Kozai-Lidov + tidal circularization)**: a distant stellar companion (or planet) pumps eccentricity of a proto-HJ → tidal friction at periapsis → circularization at a small a. Produces misaligned HJs (obliquity relative to stellar spin ≠ 0). Observed: many HJs have spin-orbit misalignment (Winn et al. 2010).

**Two pathways explain demographic split**: aligned HJs (disk migration) and misaligned HJs (high-e migration).

### Ultra-Hot Jupiters

Dayside temperatures > 2200 K → molecular dissociation (H₂ dissociates, FeI/TiO/VO vaporize). KELT-9b (T_eq ~ 4000 K): hottest exoplanet known. JWST phase curves show Fe, Mg, Ca vapor; extremely asymmetric day/night temperature contrast.

**Magnetic inflation**: some HJs have radii significantly larger than expected from standard models ("inflated hot Jupiters"). Ohmic dissipation of currents driven by zonal winds interacting with the magnetic field provides internal heating → inflates the envelope. Batygin & Stevenson (2010).

### Hot Jupiter Demographics

- Occurrence rate: ~0.5–1% around FGK stars (rare)
- No hot Jupiters have nearby sibling planets (unlike other planet types) — evidence for high-e migration disrupting multi-planet systems
- Occurrence anti-correlates with stellar metallicity decreasing: HJs prefer metal-rich stars (core accretion needs solids)

---

## 8. Future Missions and Direct Imaging

```
┌──────────────────────────────────────────────────────────────────────┐
│                    UPCOMING EXOPLANET MISSIONS                       │
│                                                                      │
│  Mission     Launch   Goal                    Capability             │
│  ───────     ──────   ────                    ──────────             │
│  TESS        Active   All-sky transit survey  Bright nearby stars    │
│  JWST        Active   Atmosphere spectra      Sub-Neptune to rocky   │
│  Ariel       2029     Atmospheric survey      >1000 planets          │
│  PLATO       2026     Rocky HZ planets        P up to 2 yr           │
│  Roman       2027     Microlensing + coronagraph Cold planets + HJ   │
│  HWO         ~2040    Rocky planet direct imaging 10⁻¹⁰ contrast   │
│  LUVOIR-A    ~2040    UV-optical-IR direct imaging Rocky biosigs     │
└──────────────────────────────────────────────────────────────────────┘
```

**PLATO (ESA, 2026)**: photometric precision better than Kepler; 2+ years of continuous staring → Earth-period planets around FGK stars for the first time in statistically significant numbers. Will detect habitable-zone rocky planets around bright enough stars for RV follow-up.

**Roman Space Telescope coronagraph (2027)**: technology demonstrator for 10⁻⁸ contrast; giant planets only. Also: microlensing survey → thousands of cold planets and rogue planets.

**HWO (Habitable Worlds Observatory)**: NASA Decadal Survey 2020 priority. ~6m UV/optical/IR telescope with ~10⁻¹⁰ starlight suppression. Goal: characterize ~25 potentially habitable rocky planets, searching for biosignatures in reflected-light spectra.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does transit give you? | R_p/R_\star (radius ratio); T_eq estimate; transit timing variations → masses |
| What does RV give you? | M_p sin i (minimum mass); orbital elements |
| Combined transit + RV? | True density → bulk composition constraint |
| What is the Fulton gap? | Bimodal R distribution at ~1.7 R_E from photoevaporation stripping H/He envelopes |
| Why are hot Jupiters there? | Formed beyond 3 AU; migrated inward via disk migration or high-e tidal migration |
| What is the HZ? | Range of a where liquid surface water is stable; for Sun: ~1–1.7 AU (conservative) |
| Best JWST results so far? | WASP-39b CO₂; TRAPPIST-1b,c bare rock; LHS 1140b possible CO₂ |
| What is a Hycean world? | H₂ atmosphere over liquid water ocean (K2-18b candidate) |
| What is direct imaging contrast challenge? | Earth in reflected light: ~10⁻¹⁰; current coronagraphs: ~10⁻⁷ for ground |
| When will we get rocky planet spectra? | HWO era (~2040) for reflected-light spectra of HZ rocky planets |
| What is microlensing good for? | Cold planets (1–5 AU), rogue planets, statistical occurrence rates |

---

## Common Confusion Points

**"Kepler found thousands of Earth-like planets"**
Kepler found thousands of transiting planet *candidates* (and ~2600 confirmed), but the vast majority are sub-Neptunes, not Earth analogs. Genuine Earth-size, Earth-period, FGK-star planets are rare in the Kepler sample due to geometric bias + limited mission duration. PLATO is specifically designed to close this gap.

**"Transit depth tells you the planet's mass"**
Transit depth gives radius, not mass. Mass requires either RV (Doppler), transit timing variations (gravitational perturbations between planets), or astrometry. RV + transit together give density, which constrains bulk composition.

**"M sin i from RV is the true mass"**
M sin i is a minimum mass — the true mass could be higher if the orbital inclination is not 90°. For a random inclination distribution, the correction factor is ~4/π ≈ 1.27 on average. For transiting planets, i ≈ 90° is guaranteed → sin i ≈ 1 → true mass.

**"The habitable zone = can support life"**
The HZ is defined by liquid surface water, which is necessary for life as we know it but not sufficient. Many factors matter: magnetic field (atmosphere retention), chemical inventory, tidal locking, stellar UV flux. The subsurface ocean HZ (Europa, Enceladus) isn't covered by the classical definition at all.

**"TRAPPIST-1 planets are confirmed habitable"**
JWST is actively ruling things out: TRAPPIST-1b and 1c appear to lack thick CO₂ atmospheres (closer to bare rock than Venus-like). Whether the HZ planets (e, f, g) retain any atmosphere at all is unknown — ongoing JWST observations. Tidal locking + M-dwarf activity make habitability uncertain.

**"Direct imaging of an exoplanet means we see its surface"**
Direct imaging of giant planets gives a single pixel of light — the disc is unresolved. What we measure is the planet's spectrum and photometry (brightness, color). For self-luminous young giants, this is thermal emission. For rocky planets in reflected light (HWO era), it would be reflected starlight modulated by atmospheric and surface features.
