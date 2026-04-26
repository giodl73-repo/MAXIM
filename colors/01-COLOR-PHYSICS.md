# Color Physics — Light, Wavelength, and Why Objects Have Color

## The Big Picture

```
+------------------------------------------------------------------+
|             FOUR MECHANISMS OF COLOR IN MATTER                   |
|                                                                  |
|  1. SELECTIVE ABSORPTION / REFLECTION                            |
|     Chromophores in material absorb specific wavelengths         |
|     Complementary wavelengths reflected → perceived color        |
|     EXAMPLES: pigments, dyes, colored glass, solutions           |
|               → dominant mechanism for most human-made color     |
|                                                                  |
|  2. STRUCTURAL COLOR (interference / diffraction)                |
|     No chromophore — color from geometry at nanoscale            |
|     Wavelength-dependent constructive/destructive interference   |
|     EXAMPLES: soap bubbles, morpho butterfly, opal, CD surface   |
|               → angle-dependent iridescence                      |
|                                                                  |
|  3. EMISSION                                                     |
|     Object generates its own light (not reflected)               |
|     Blackbody radiation (hot objects), LEDs (band gap),          |
|     fluorescence (absorb short λ, re-emit longer λ)              |
|                                                                  |
|  4. SCATTERING                                                   |
|     Wavelength-selective scattering from particles/molecules     |
|     Rayleigh (small particles: λ⁻⁴) → blue sky                   |
|     Mie (large particles: wavelength-independent) → white clouds |
+------------------------------------------------------------------+
```

---

## Electromagnetic Radiation and Visible Light

```
PHOTON ENERGY: E = hc/λ
  h = Planck's constant (6.626 × 10⁻³⁴ J·s)
  c = speed of light (3 × 10⁸ m/s)
  λ = wavelength

  At λ = 400 nm (violet): E = 3.1 eV
  At λ = 700 nm (red):    E = 1.8 eV
  → Violet photons carry ~70% more energy than red

VISIBLE SPECTRUM:
+------+------+------+------+------+------+------+
| ~420 | ~450 | ~490 | ~530 | ~580 | ~620 | ~700 |
| nm   | nm   | nm   | nm   | nm   | nm   | nm   |
+------+------+------+------+------+------+------+
 Violet  Blue  Cyan  Green Yellow Orange  Red

  ~380–420 nm: violet (border with UV)
  ~420–490 nm: blue
  ~490–560 nm: green
  ~560–590 nm: yellow
  ~590–625 nm: orange
  ~625–700 nm: red

  Boundaries are fuzzy — color names are human conventions imposed on
  a continuous spectrum. The spectrum has no natural boundaries.

ONE OCTAVE OF VISION:
  700 nm / 380 nm ≈ 1.84 (less than one octave of frequency)
  Audible range: ~20 Hz to 20,000 Hz = 10 octaves
  Human vision samples an absurdly narrow slice of EM spectrum.
```

---

## Mechanism 1: Selective Absorption

### How Chromophores Work

```
BEER-LAMBERT LAW:
  A = ε × c × l
  A = absorbance
  ε = molar absorptivity (intrinsic property of the chromophore)
  c = concentration
  l = path length

  → Double the concentration: double the absorbance
  → Transmittance T = 10⁻ᴬ (exponential, not linear)

COMPLEMENTARY COLOR RULE:
  Wavelengths absorbed → appear as their complement in perception

+---------------------------+---------------------------+
| WAVELENGTHS ABSORBED      | COLOR PERCEIVED           |
+---------------------------+---------------------------+
| ~400-430 nm (violet)      | Yellow-green              |
| ~430-480 nm (blue)        | Orange                    |
| ~480-490 nm (blue-green)  | Red-orange                |
| ~490-500 nm (green-blue)  | Red                       |
| ~500-560 nm (green)       | Red-purple/magenta        |
| ~560-580 nm (yellow-green)| Violet                    |
| ~580-600 nm (yellow)      | Blue-violet               |
| ~600-620 nm (orange)      | Blue                      |
| ~620-700 nm (red)         | Blue-green/cyan           |
+---------------------------+---------------------------+

EXAMPLE: Chlorophyll
  Absorbs: ~430 nm (blue) and ~680 nm (red)
  Reflects: ~530 nm (green) → leaves look green
  In autumn, chlorophyll breaks down → underlying carotenoids
  (yellow/orange) revealed; anthocyanins (red) synthesized

EXAMPLE: Hemoglobin
  Oxygenated (HbO₂): absorbs ~415 nm, ~540-580 nm
  → Reflects red → bright red arterial blood
  Deoxygenated (Hb): absorbs ~430 nm (different peak)
  → Darker red/maroon venous blood
  CO-hemoglobin (HbCO): cherry red — CO shifts absorption
```

### Molecular Basis of Chromophores

```
WHAT CREATES A CHROMOPHORE:
  Electronic transition between energy levels must match visible photon energy

  For visible light (1.8–3.1 eV), need transitions in that range:
  1. π → π* transitions (conjugated organic systems)
     Extended conjugation lowers HOMO-LUMO gap into visible range
     Indigo: two indole units → absorption at ~610 nm
     Carotene (β-carotene): 11 conjugated double bonds → absorbs blue/green

  2. n → π* transitions
     Lone pair (n) excitation into antibonding orbital
     Usually UV range unless conjugated system present

  3. d-d transitions (transition metal complexes)
     d-electrons in crystal/ligand field split into energy levels
     Blue of copper sulfate (Cu²⁺, d-d transition)

  4. Charge-transfer transitions
     Electron transferred between metal center and ligand
     Very intense (high ε) — Prussian blue, permanganate purple

  5. Band gap absorption (semiconductors)
     Valence band → conduction band; cadmium yellow/red family
```

---

## Mechanism 2: Structural Color

```
STRUCTURAL COLOR: color from nanostructure geometry, not chemical absorption
  Wavelength-independent underlying material + periodic structures at
  100-500 nm scale (comparable to visible λ) → wavelength-selective effects

TWO MAIN MECHANISMS:

A. THIN-FILM INTERFERENCE
   Light hits thin transparent film → reflects at TOP and BOTTOM surfaces
   Two reflected waves → interfere constructively or destructively
   Which wavelengths interfere constructively depends on film thickness

   Constructive: 2nt = mλ (m = integer, n = refractive index, t = thickness)
   → At given thickness t, specific λ reinforced → specific color perceived

   Examples:
   • Soap bubbles: soapy film ~200-900 nm thick → colors change with thickness
   • Oil on water: oil film ~100-1000 nm
   • Tempering colors on steel: iron oxide film grows as steel is heated
     (straw yellow → brown → purple → blue → gray with increasing thickness)
   • Beetle elytra: multilayer thin films → structural iridescence
   • Peacock feathers: melanin nanorod arrays with thin-film properties

   KEY FEATURE: angle-dependent
   Tilt the surface → film thickness in line of sight changes → color shifts
   → Iridescence (color changes with viewing angle)

B. PHOTONIC CRYSTALS
   3D periodic structure with ~100-500 nm repeat → "photonic bandgap"
   Certain wavelengths cannot propagate through the structure
   → Those wavelengths strongly reflected

   Examples:
   • Opal: close-packed silica spheres (~150-300 nm) + amorphous arrangement
     → Play-of-color as different crystal domains scatter different wavelengths
   • Morpho butterfly wings: parallel lamellar ridges
     → Deep iridescent blue (no blue pigment present)
   • Kingfisher feathers: sponge-like nanostructure of air pockets in keratin
     → Coherent scattering of blue (quasi-photonic crystal)

   The morpho butterfly:
   Wings appear brilliant iridescent blue from above
   Ridges on scales: ~200 nm lamellae stacked with ~200 nm air gaps
   Constructive interference for ~450 nm (blue) at normal incidence
   From below: different angle → different effective wavelength → greenish
   ZERO blue pigment; blue is pure geometry
```

---

## Mechanism 3: Blackbody Radiation and Emission

```
PLANCK'S LAW:
  B(λ, T) = (2hc²/λ⁵) × 1/(exp(hc/λkT) − 1)
  Spectral radiance as function of wavelength and temperature

  → Every object above 0 K emits thermal radiation
  → Peak wavelength: Wien's Law: λ_max = 2898 μm·K / T

TEMPERATURE AND COLOR:
+----------+------------------+-------------------------------+
| TEMP (K) | PEAK λ           | APPEARANCE                    |
+----------+------------------+-------------------------------+
| 800 K    | ~3600 nm (IR)    | Dull red glow (barely visible)|
| 1000 K   | ~2900 nm         | Red (dim)                     |
| 2700 K   | ~1070 nm         | Warm white (tungsten bulb)    |
| 3500 K   | ~830 nm          | Warm white (halogen)          |
| 5500 K   | ~530 nm          | Daylight (noon)               |
| 6500 K   | ~445 nm          | Cool/overcast daylight        |
| 10,000 K | ~290 nm (UV)     | Blue-white (hot star)         |
| 30,000 K | ~97 nm (far UV)  | Blue supergiant star          |
+----------+------------------+-------------------------------+

"COLOR TEMPERATURE" — COUNTERINTUITIVE NAMING:
  Higher Kelvin = bluer/cooler looking to humans
  Lower Kelvin = redder/warmer looking to humans
  The PHYSICAL temperature is higher for blue;
  the AESTHETIC association of warm colors (fire) is opposite.
  → Always specify which "warm/cool" you mean: temperature or aesthetics

CORRELATED COLOR TEMPERATURE (CCT):
  Non-blackbody sources (LEDs, fluorescent) assigned "equivalent blackbody T"
  CCT 2700K = "warm white LED" (same hue as tungsten)
  CCT 6500K = "daylight LED" (same hue as overcast sky)
  CCT doesn't describe full spectrum — Color Rendering Index (CRI) does

FLUORESCENCE:
  Absorb high-energy photon (UV or short visible)
  Re-emit lower-energy photon (longer wavelength, visible)
  Stokes shift = energy difference (lost to heat/vibration)
  → Optical brighteners in laundry detergent: absorb UV → emit blue
    → Shirt appears "whiter than white" under UV-containing daylight
  → Fluorescent minerals, highlighter inks, fluorescent pigments
  → GFP (green fluorescent protein): 395 nm excitation → 509 nm emission
```

---

## Mechanism 4: Scattering

```
RAYLEIGH SCATTERING:
  Particles much smaller than λ (molecules, nanoscale particles)
  Scattering cross-section ∝ λ⁻⁴
  → Blue light scattered ~5.5× more than red (λ_blue ≈ 0.45/λ_red ≈ 0.65)

WHY THE SKY IS BLUE:
  Sunlight enters atmosphere → N₂/O₂ molecules (~0.3 nm) = Rayleigh scatters
  Blue wavelengths scatter in all directions → diffuse illumination of whole sky
  → Look anywhere in sky away from sun → scattered blue → sky appears blue

WHY SUNSETS ARE RED:
  At sunrise/sunset, sunlight path through atmosphere is ~38× longer
  Blue and green wavelengths scattered away entirely
  → Only red/orange remain to reach observer directly

WHY CLOUDS ARE WHITE:
  Water droplets ~10-100 μm (much larger than λ) → Mie scattering
  Mie scattering is approximately wavelength-independent → scatters all equally
  → White cloud (all colors scattered equally)
  Dark storm clouds: droplets so dense total light scattered before exit

TYNDALL EFFECT:
  Visible scattering from colloidal particles (larger than Rayleigh, smaller than Mie)
  → Blue color of some iris eyes (melanin particles in stroma scatter blue)
  → Blue color of some bird feathers (not pigment, not photonic crystal)
  → Milk (casein micelles scatter all wavelengths equally → white)
  → Blue smoke from burning wood (submicron carbon particles)

NOTE: Rayleigh vs Tyndall vs Mie = same physics, different particle size regime
```

---

## Spectral Power Distribution and Perceived Color

```
FULL CHAIN:
  Light source SPD [W/nm]
      ×
  Surface reflectance [0-1 at each nm]
      ×
  Observer cone sensitivity functions [L(λ), M(λ), S(λ)]
      ↓
  Tristimulus values (LMS → XYZ)
      ↓
  Brain processes → Perceived color

SPD EXAMPLES:
  Incandescent bulb: smooth, near-blackbody (2700K peak)
  Fluorescent tube: spiky (mercury emission lines + phosphor fill)
  LED: narrow peaks at LED wavelengths + phosphor conversion
  Daylight D65: standard defined by CIE (reference for sRGB)

SAME SURFACE UNDER DIFFERENT ILLUMINANTS:
  Incandescent (2700K): warm light → all colors shifted warm
  Cool LED (5000K): neutral to slightly cool
  Sodium vapor lamp (589 nm): near monochromatic → most colors gray
  → Metameric pairs can match under one but differ under another
  → This is the industrial metamerism problem
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is the sky blue? | Rayleigh scattering (λ⁻⁴) — N₂/O₂ molecules scatter blue far more than red; scattered blue fills the entire sky |
| Why are clouds white? | Mie scattering from large water droplets (~10-100 μm) — wavelength-independent, scatters all colors equally |
| Why are sunsets red? | Long atmospheric path (38×) → blue/green Rayleigh-scattered away entirely → only red/orange reaches eye |
| How does thin-film interference create color? | Partial reflections at top and bottom film surfaces → two reflected waves interfere; constructive interference wavelength set by 2nt = mλ (n=RI, t=thickness) |
| Does the morpho butterfly contain blue pigment? | No — structural color from periodic lamellae (photonic crystal effect); zero blue pigment, all geometry |
| What is Wien's displacement law? | λ_max = 2898 μm·K / T — hotter blackbodies peak at shorter (bluer) wavelengths |
| Why does vinyl glazing turn yellow? | UV absorption by plasticizers or polymer chains undergoes photodegradation; extended conjugation develops → absorbs blue → appears yellow |
| What makes a good chromophore? | Extended conjugation (lowers HOMO-LUMO gap into visible range), charge-transfer transitions, or d-d transitions in crystal field |

---

## Common Confusion Points

**Color temperature is counterintuitive:** Higher Kelvin = bluer (cooler appearance aesthetically). This trips people constantly. Photographers say "warm light" (sunset, tungsten) = low Kelvin (2700-3000K). "Cool light" (overcast, LED daylight) = high Kelvin (5500-6500K). The physics and the aesthetic vocabulary are inverted.

**Structural color ≠ no chemistry:** Structural color objects still have chemistry (chitin, silica, melanin). The color mechanism is geometric, but the material still matters. Morpho wing scales are made of chitin; the geometry is the color source, but the chitin provides the refractive index difference.

**Rayleigh scattering applies to molecules, not dust:** Atmospheric Rayleigh scattering involves N₂/O₂ molecules. Air pollution doesn't make the sky bluer — it degrades Rayleigh scattering and can add haze (Mie from larger particles). Mars's sky is pink/tan because of fine iron-oxide dust (Mie scattering with absorbing particles).

**Fluorescence and phosphorescence differ in timescale:** Fluorescence: emission stops when excitation stops (nanosecond timescale). Phosphorescence: emission continues after excitation (milliseconds to hours — glow-in-dark materials). Both involve absorption + re-emission, but different electronic pathways (singlet vs triplet excited states).
