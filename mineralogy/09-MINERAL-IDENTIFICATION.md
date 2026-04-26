# Mineral Identification Methods

## The Big Picture

```
+------------------------------------------------------------------+
|           MINERAL IDENTIFICATION: FROM FIELD TO LABORATORY       |
|                                                                  |
|  FIELD                 PETROGRAPHIC LAB          ANALYTICAL LAB  |
|  Hand specimen         Thin section under         XRD            |
|  observation           polarizing microscope      XRF            |
|                                                                  |
|  Properties:           Optical properties:        EPMA / EDS     |
|  Color, luster         Birefringence              LA-ICP-MS      |
|  Hardness              Interference colors        Raman          |
|  Cleavage              Extinction angle           FTIR           |
|  Streak                Pleochroism                               |
|  Specific gravity      Twinning                  DATABASES:      |
|  Crystal form          Habit in thin section      RRUFF          |
|  Associations          Mode (%)                   ICDD (XRD)     |
|                                                                  |
|  Resolution: to genus  Resolution: to species    Resolution:     |
|  level                 level for most minerals   trace element,  |
|                                                                  |
|                                                  geochronology   |
+------------------------------------------------------------------+
```

---

## Level 1: Hand Specimen Identification

The field geologist's toolkit: observation and a few simple tests.

```
HAND SPECIMEN IDENTIFICATION WORKFLOW
+------------------------------------------------------------------+
|                                                                  |
|  1. LUSTER                                                       |
|     Metallic/opaque → go to sulfides/oxides/native metals        |
|     Non-metallic → silicates/carbonates/phosphates/sulfates      |
|                                                                  |
|  2. HARDNESS (carry: fingernail, penny, knife, quartz piece)     |
|     <2.5: talc, gypsum, graphite, sulfur                         |
|     2.5–3.5: calcite, halite, argentite                          |
|     3.5–5.5: fluorite, apatite, chalcopyrite                     |
|     5.5–7: pyroxene, amphibole, feldspar                         |
|     >7: quartz, topaz, corundum, garnet                          |
|                                                                  |
|  3. CLEAVAGE/FRACTURE                                            |
|     1 perfect basal: mica                                        |
|     3 planes ≈90°: halite, galena, orthoclase                    |
|     3 planes rhombohedral: calcite, dolomite                     |
|     2 planes ≈90°: pyroxene (also feldspar)                      |
|     2 planes ≈60°/120°: amphibole                                |
|     Conchoidal: quartz, obsidian, flint                          |
|                                                                  |
|  4. STREAK (on unglazed porcelain if H < 7)                      |
|     Red-brown: hematite       Greenish-black: pyrite, chalcopyrite|
|     Black: magnetite          Yellow: gold                       |
|                                                                  |
|  5. SPECIFIC GRAVITY ("heft" test)                               |
|     Very dense for size: galena, barite, native metals           |
|                                                                  |
|  6. SPECIAL TESTS                                                |
|     Magnet: magnetite (strongly), pyrrhotite (weakly)            |
|     HCl fizz: calcite (cold), dolomite (hot/powder)              |
|     Taste: halite (salty), sylvite (bitter)                      |
|     UV light: scheelite (bright blue-white), willemite (green)   |
+------------------------------------------------------------------+
```

**Field databases and apps**:
- Mindat.org: comprehensive mineral database (locality + property data)
- RRUFF database: Raman spectra + XRD patterns for ~4,500 minerals. The practical field pipeline: handheld Raman spectrometers (e.g., Rigaku Progeny, Metrohm Mira) acquire a spectrum in 30 seconds on a rock surface; the device's onboard software or a Bluetooth-connected phone app matches the spectrum against the RRUFF reference library and returns the top candidates with match scores. This gives species-level identification in the field without sampling — the same workflow as portable XRF for elemental analysis, but structure-sensitive rather than composition-sensitive.
- iRocks, Hudson: collector databases with photos
- Minerals ID apps (iMinerals, Smart Geology): camera + AI identification

---

## Level 2: Polarizing Microscope (Petrographic Microscopy)

The standard tool of the economic geologist and petrologist. A 30 µm thick rock slice (thin section) on a glass slide, viewed with polarized light.

```
POLARIZING MICROSCOPE SETUP
+------------------------------------------------------------------+
|                                                                  |
|    [Analyzer] ← (can insert/remove)                              |
|    +---------+                                                   |
|    |         |   ← Upper polarizer (analyzer): N-S             |
|    | UPPER   |       perpendicular to lower                     |
|    +---------+                                                   |
|         |                                                        |
|  MINERAL IN THIN SECTION  (30 µm thick)                          |
|         |                                                        |
|    +---------+                                                   |
|    | LOWER   |   ← Lower polarizer (polarizer): E-W            |
|    +---------+                                                   |
|    [Light source]                                                |
|                                                                  |
|  PPL: Plane Polarized Light (analyzer out)                       |
|  → Color, pleochroism, cleavage, habit                           |
|                                                                  |
|  XPL: Cross Polarized Light (analyzer in)                        |
|  → Birefringence (interference colors), extinction angle,        |
|    twinning patterns                                             |
+------------------------------------------------------------------+
```

### Birefringence and Michel-Lévy Chart

```
INTERFERENCE COLORS (Michel-Lévy chart)
  When crystal in XPL: two polarized rays interfere
  Retardation = birefringence × thickness × 1000 (nm)
  → Produces a color from the Michel-Lévy chart

  Retardation <100 nm: black/gray (first order)
  100–500 nm: white to yellow to red (first order)
  500–1000 nm: blue, green, yellow (second order)
  1000–1500 nm: pink, red, green, blue (third order)

  Thin section standard: 30 µm thick
  Quartz: birefringence = 0.009 → pale gray/white in XPL
  Calcite: birefringence = 0.172 → extreme high-order (pearl-gray)
  Olivine: 0.035 → vivid colors in XPL
  Mica: 0.03–0.05 → vivid yellows and blues
  Feldspar: 0.007–0.013 → pale gray/white (barely above quartz)
  Opaque minerals: no transmission → black in all orientations
```

### Key Optical Properties

| Property | What it shows | Example |
|----------|--------------|---------|
| Pleochroism (PPL, rotate stage) | Color change with orientation | Biotite: yellow-brown to dark brown |
| Extinction angle (XPL) | Angle crystal goes dark vs. cleavage | Pyroxene: parallel; amphibole: oblique ~15° |
| Twinning (XPL) | Multiple domains with different orientations | Plagioclase: polysynthetic; microcline: tartan |
| Cleavage traces (PPL) | Parallel lines in crystal | 2 sets at 90°: pyroxene; 60°: amphibole |
| Relief | Apparent "height" vs. mounting medium | High relief: olivine, garnet; low: quartz |
| Crystal shape | Euhedral/anhedral in context | Feldspar: tabular; hornblende: prismatic |

**Pyroxene vs. amphibole in thin section** (the classic identification):
- Pyroxene: 2-pyroxene cleavages at ~90° in cross-section; parallel to near-parallel extinction; no OH in structure
- Amphibole: 2-cleavages at 60°/120°; oblique extinction (~15° from cleavage); often pleochroic; elongate prisms

---

## Level 3: X-Ray Diffraction (XRD)

The definitive mineral identification method — uses crystal structure, not just chemistry.

```
POWDER XRD WORKFLOW
+------------------------------------------------------------------+
|  Sample: ~0.5 g mineral, ground to <45 µm powder                 |
|  Loaded into sample holder (flat plate or capillary)             |
|       |                                                          |
|  Irradiated with X-rays (Cu Kα = 1.5406 Å most common)           |
|       |                                                          |
|  Detector scans 2θ from 2° to 70°+                               |
|  Peak positions → d-spacings via Bragg's law: nλ = 2d·sin(θ)     |
|       |                                                          |
|  MATCH against ICDD database (International Centre for           |
|  Diffraction Data) — PDF-4/Minerals database                     |
|       |                                                          |
|  Each mineral has a unique "fingerprint" of d-spacings           |
|  and relative intensities                                        |
|       |                                                          |
|  Qualitative analysis: identify which minerals are present       |
|  Quantitative analysis (Rietveld refinement):                    |
|    Fit calculated pattern to observed → wt% of each phase        |
+------------------------------------------------------------------+
```

**The Fourier transform connection**:

XRD measures the reciprocal lattice of the crystal — equivalent to the Fourier transform of the electron density. Each peak in the XRD pattern corresponds to a set of crystal planes (hkl). The pattern IS the frequency-domain representation of the crystal structure. Solving a crystal structure = inverting the Fourier transform (with the phase problem as the complication: you measure |F|² but not the phase of F, so you cannot directly invert to get the real-space electron density). See 02-CRYSTAL-SYSTEMS for the full Bragg's Law and phase problem discussion; this file focuses on the practical identification workflow.

**Applications**:
- Identify unknown minerals in soil, rock, dust
- Phase analysis: cement (clinker phases), concrete, pharmaceutical QC
- Quantify clay mineralogy in soils and sediments
- Confirm mineral purity for industrial applications
- Battery material QC (NMC cathode phase, graphite anode)

---

## Level 4: Electron Probe Microanalysis (EPMA) and EDS

**Electron Probe Microanalysis (EPMA)**: focused electron beam (1–20 µm spot) excites characteristic X-rays from each element present.

```
EPMA/EDS PRINCIPLE
+------------------------------------------------------------------+
|  Electron beam → mineral surface                                 |
|       |                                                          |
|  Incident electrons eject core electrons from atoms              |
|       |                                                          |
|  Outer electrons fall to fill vacancies → emit X-rays            |
|  X-ray energy = specific to element (characteristic X-rays)      |
|       |                                                          |
|  EDS (Energy Dispersive Spectrometry):                           |
|  → Fast; identifies all elements simultaneously                  |
|  → Lower precision (better for qualitative/semi-quantitative)    |
|                                                                  |
|  WDS (Wavelength Dispersive Spectrometry — EPMA proper):         |
|  → Slower; analyzes one element at a time                        |
|  → Higher precision (±0.01–0.1 wt%) → full quantitative          |
|  → Can measure light elements (B, C, N, O, F) with appropriate   |
|    crystals — EDS typically cannot                               |
+------------------------------------------------------------------+

OUTPUTS:
  Quantitative elemental composition (wt% oxides for silicates)
  Formula calculation: convert wt% to mineral formula
  Element distribution maps: show where elements concentrate
  Point analyses: compositional zoning in mineral crystals
  Detection limit: ~100 ppm (WDS), ~0.1% (EDS)
```

**Use cases**:
- Full mineral formula from point analysis (name the mineral precisely)
- Compositional zoning in feldspar (records crystallization history)
- Garnet zoning (P-T path of metamorphism)
- Ore mineral characterization
- Identification of very fine-grained mineral mixtures

---

## Level 5: LA-ICP-MS — Laser Ablation ICP Mass Spectrometry

**The trace element and isotope powerhouse.**

```
LA-ICP-MS WORKFLOW
+------------------------------------------------------------------+
|  Pulsed UV laser (193 nm ArF excimer) → mineral surface          |
|  Ablation spot: 10–200 µm diameter; ~50 µm deep pit              |
|       |                                                          |
|  Ablated material transported in He carrier gas                  |
|       |                                                          |
|  ICP (inductively coupled plasma): 6000–8000 K → full ionization|
|       |                                                          |
|  Mass spectrometer: separates ions by m/z → measures each isotope|
|       |                                                          |
|  Calibration against glass standards (NIST SRM 610, 612)         |
|  Internal standard: usually a major element from EPMA            |
+------------------------------------------------------------------+

WHAT LA-ICP-MS CAN DO:
  Trace elements (to <1 ppb for many elements)
  Rare earth element (REE) patterns → fingerprint source rock
  U-Pb geochronology in zircon: ~10,000 zircons/day possible
    → Age of crystallization, metamorphic overprints
  Hf isotopes in zircon: crustal evolution
  Sr, Nd isotopes (after dissolution): source tracing
  Gem origin fingerprinting: emerald Colombia vs. Zambia
  Archaeological provenance: glass, obsidian sourcing
```

**U-Pb zircon geochronology** — this is why zircon is so important:

```
ZIRCON U-Pb SYSTEM:
  ²³⁸U → ²⁰⁶Pb (t₁/₂ = 4.468 Ga) — two simultaneous decay chains
  ²³⁵U → ²⁰⁷Pb (t₁/₂ = 703.8 Ma)
  Initial Pb (²⁰⁴Pb) measured for correction

  Concordia diagram:
    If both U-Pb systems agree → concordant = gives reliable age
    If discordant → Pb loss event; upper/lower intercepts on
    Wetherill concordia = crystallization age + resetting event age

  ZAP it, count isotopes, plot concordia, get an age.
  This is the backbone of Precambrian geology and crustal evolution studies.
```

---

## Level 6: Other Analytical Methods

### Raman Spectroscopy

```
RAMAN: inelastic scattering of photons from molecular vibrations
  Laser (usually green 532 nm or red 785 nm) → mineral sample
  Scattered photons have shifted frequencies (Raman shift, cm⁻¹)
  Each mineral has a characteristic Raman spectrum (vibrational fingerprint)

ADVANTAGES:
  Non-destructive, no sample prep
  Works through glass (ideal for fluid inclusions in gems)
  Point identification in thin section
  Handheld Raman devices available (portable mineral ID)
  RRUFF database: reference Raman spectra for most minerals

APPLICATIONS:
  Fluid inclusion phase identification (minerals + fluids inside gems)
  Polymorph distinction: quartz vs. cristobalite; calcite vs. aragonite
  Non-destructive gem analysis
  Carbon phases: diamond vs. graphite vs. amorphous C
```

### FTIR (Fourier Transform Infrared Spectroscopy)

```
FTIR: absorption of IR light by molecular vibrations
  OH stretching, CO₃ vibrations, PO₄ vibrations
  Specific to structural OH vs. fluid inclusions vs. adsorbed water

APPLICATIONS IN MINERALOGY:
  Distinguish heat-treated sapphire (silk dissolved = fewer OH defects)
  Quantify water in nominally anhydrous minerals (olivine, pyroxene)
  Identify carbonate minerals (calcite vs. dolomite vs. aragonite)
  Clay mineral speciation
  Diamond type classification (Type I = N impurities; Type II = N-free)
```

### XRF (X-Ray Fluorescence)

```
XRF: bulk elemental analysis of rock/mineral samples
  X-ray beam → sample → characteristic fluorescence from each element
  Wavelength-dispersive XRF (WD-XRF): high precision, whole rock analysis
  Energy-dispersive XRF (ED-XRF): portable handheld devices for field use

APPLICATIONS:
  Whole-rock geochemistry (major + trace elements)
  Ore grade estimation in exploration
  Handheld XRF: real-time gold assay, Cu grade, lead in paint
  Environmental monitoring (heavy metals in soil)
  Museum conservation: artifact composition without sampling
```

---

## Databases and Reference Collections

| Resource | Content | Access |
|----------|---------|--------|
| **Mindat.org** | 5,800+ mineral species; localities; photos; properties | Free web |
| **RRUFF database** | Raman spectra, XRD patterns, chemistry for ~4,500 minerals | Free web |
| **ICDD PDF-4/Minerals** | Reference XRD patterns for phase ID | Commercial subscription |
| **EPMA standard database** | Reference compositions for comparison | Lab-specific |
| **Webmineral.com** | Physical/optical properties, crystal data | Free web |
| **GeoROC / EarthChem** | Geochemical datasets (LA-ICP-MS, XRF) | Free web |

---

## The Identification Hierarchy

```
STARTING POINT: unknown mineral
       |
       v
HAND SPECIMEN: luster, hardness, cleavage, streak, SG, special tests
  → Identifies most common minerals (~80% of what you'll encounter)
       |
       v
THIN SECTION (if rock): optical properties, associations, textures
  → Identifies all common rock-forming minerals, mode, textures
       |
       v
XRD (powder): definitive mineral ID by crystal structure
  → Distinguishes polymorphs, clay minerals, fine-grained mixtures
       |
       v
EPMA/EDS: full composition of individual mineral grain
  → Precise formula, solid solution composition, zoning
       |
       v
LA-ICP-MS: trace elements, isotope ratios, geochronology
  → Age of formation, source fingerprinting, geochemical history
       |
       v
Raman/FTIR: molecular vibrations; fluid inclusions; polymorph ID
  → Non-destructive; works on polished stones, gems, thin sections
```

---

## Decision Cheat Sheet

| Goal | Method | Why |
|------|--------|-----|
| Quick field ID | Hand specimen + properties | No equipment needed |
| Rock mode in thin section | Petrographic microscope | See texture + mineral proportions |
| Mineral ID by structure | Powder XRD | Structure = definitive; ICDD match |
| Full mineral formula | EPMA/EDS | Point analysis, quantitative chemistry |
| Trace elements + isotopes | LA-ICP-MS | Sub-ppb detection, isotope ratios |
| Age of mineral | LA-ICP-MS U-Pb on zircon | Only reliable high-closure-T geochronometer |
| Non-destructive gem analysis | Raman + FTIR | Works through glass; no damage |
| Bulk rock chemistry | XRF | Major + trace elements in one run |

---

## Common Confusion Points

**EPMA vs. EDS**: Both use electron beams and X-ray detection, but EPMA (WDS system) is a dedicated instrument with wavelength-dispersive spectrometers — much higher precision and light element capability. EDS is typically an add-on to a scanning electron microscope (SEM) — faster, less precise. Both are often on the same instrument (SEM with both EDS and WDS detectors).

**XRD identifies phases, not elements**: XRD tells you which mineral phases are present (quartz vs. tridymite; calcite vs. aragonite) because it measures crystal structure. XRF tells you which elements are present (Si, Al, Fe...) but not how they're arranged. You need both for complete characterization.

**The phase problem in XRD**: For mineral identification, you don't need to solve the phase problem — you just match your d-spacing pattern to the database. Phase problem solving is needed for new structure determination (where no reference pattern exists).

**Handheld XRF in the field**: Very useful for rapid semi-quantitative elemental analysis. Reasonably accurate for heavy elements (Fe, Cu, Pb, Zn, As); less reliable for light elements (Na, Mg, Al, Si). Useful for ore grade estimation and environmental monitoring but not a substitute for lab XRF for precise geochemistry.

**Zircon for geochronology vs. other minerals**: U-Pb in zircon is preferred because: (1) zircon strongly excludes initial Pb during crystallization (very high U/Pb ratio), (2) very high closure temperature (~900°C) means the system doesn't reset during regional metamorphism, (3) zircon is extremely resistant to weathering. Other U-Pb systems (monazite, rutile, apatite) have different closure temperatures and different applications.
