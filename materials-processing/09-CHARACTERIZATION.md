# Materials Characterization Techniques

## The Big Picture

Materials characterization answers: "what is this material and what is its microstructure?" Every processing decision — heat treatment, sintering, welding — changes microstructure, and characterization is how you verify the result. The toolkit spans from macroscale mechanical testing to atomic-scale imaging, each technique revealing a different layer of the structure-property relationship.

```
CHARACTERIZATION TECHNIQUE LANDSCAPE
──────────────────────────────────────────────────────────────────
SCALE:        Atomic → Nano → Micro → Meso → Macro
              (Å)     (nm)   (µm)    (mm)   (cm–m)

STRUCTURAL CHARACTERIZATION (what phases, crystal structure, microstructure):
  Atomic/crystal:  XRD (phase ID, lattice parameter, residual stress)
                   TEM (atom columns, defects, phases at nm scale)
  Microstructure:  SEM (topography, phases at µm scale)
                   Optical microscopy (grain structure, phases at µm–mm)
  Phase chemistry: EDS/WDS (elemental maps), EBSD (crystal orientation maps)
  Near-surface:    XPS (surface chemistry), AES (thin films)

MECHANICAL CHARACTERIZATION (how it responds to load):
  Bulk:            Tensile, compression, hardness, impact (Charpy), fatigue
  Small-scale:     Nanoindentation (films, phases), micro-pillar compression
  Fracture:        K_IC (compact tension), J-integral, crack growth (Paris)

THERMAL CHARACTERIZATION (phase transitions, thermal properties):
  DSC (Differential Scanning Calorimetry): Tm, Tg, crystallinity, cure
  TGA (Thermogravimetric Analysis): decomposition, moisture, filler content
  Dilatometry: dimensional change vs temperature (CTE, phase changes)

CHEMICAL / COMPOSITIONAL:
  OES/GDOES: bulk elemental composition (metals)
  ICP-MS/OES: trace elements, solution analysis
  FTIR: organic functional groups (polymers, coatings, adhesives)
  Raman: complementary to FTIR, surface-sensitive, works through glass

NON-DESTRUCTIVE EVALUATION (NDT):
  Radiography (X-ray, neutron): internal defects
  Ultrasonic: internal flaws, thickness, elastic constants
  Eddy current: surface/near-surface flaws in conductive materials
  Penetrant / Magnetic particle: surface-open flaws
```

---

## Optical Microscopy

```
OPTICAL MICROSCOPY IN METALLURGY
──────────────────────────────────────────────────────────────────
Resolution limit: ~0.2 µm (limited by visible light wavelength ~400–700 nm)
Magnification: 50×–1000× (typical metallographic range)

SAMPLE PREPARATION (critical — determines data quality):
  1. Section: abrasive cutoff saw (cool to avoid phase changes)
  2. Mount: epoxy or phenolic hot-mount resin (conductive mount for SEM)
  3. Grind: progressive SiC papers (120→240→320→400→600→800 grit)
  4. Polish: diamond slurry (9→3→1 µm), then OPS or colloidal silica finish
  5. Etch: chemical etch attacks boundaries/phases at different rates → contrast

COMMON ETCHANTS:
  Nital (2–4% HNO₃ in ethanol):  steel — reveals grain boundaries, phases
  Keller's reagent:               aluminum alloys (HF + HCl + HNO₃ + H₂O)
  Aqua regia (3:1 HCl:HNO₃):     Ni superalloys
  Vilella's reagent:              stainless steel (picric acid + HCl + ethanol)
  Swab, immerse, or electrolytic etching: depends on material/phase of interest

IMAGING MODES:
  Bright field:   standard illumination → etched features appear dark
  Dark field:     scattered light collected → fine precipitates glow bright
  Polarized light: crystallographic contrast, grain orientation in Al
  DIC (Nomarski): surface relief, deformation steps, coating interfaces

WHAT YOU SEE:
  Grain boundaries (etched preferentially)
  Phase boundaries (different etch response)
  Non-metallic inclusions (oxide, sulfide)
  Graphite morphology in cast iron (flake vs nodular)
  Decarburized surface layer after heat treatment
  Case depth (carburized or nitrided layer)
  Martensite needles vs bainite laths vs pearlite colonies
```

---

## Scanning Electron Microscopy (SEM)

```
SEM FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Focused electron beam rastered over surface → detect emitted electrons/X-rays

Accelerating voltage: 1–30 kV (lower for surface sensitivity, higher for X-ray)
Resolution: 1–10 nm (much better than optical ~200 nm)
Depth of field: >> optical → excellent topographic imaging
Vacuum required: ~10⁻⁴ torr (environmental SEM: lower vacuum, wet samples OK)

SIGNAL TYPES:
  Secondary electrons (SE): surface topography
    Low energy (< 50 eV), escape depth ~1–10 nm
    → Fine surface detail, fracture morphology, particle morphology

  Backscattered electrons (BSE): compositional contrast (Z-contrast)
    High energy, elastic scattering
    Heavy elements (high Z) → scatter more → appear bright
    → Distinguishes phases (WC bright, Co matrix dark in cemented carbide)
    → Grain orientation contrast (EBSD prep)

  X-rays: elemental composition (EDS or WDS analysis)

SAMPLE REQUIREMENTS:
  Must be electrically conductive (or coat with Au, Pt, C)
  Polymers/ceramics: sputter coat with ~5 nm Au-Pd or carbon
  Mounted/polished metal samples: ready to use

KEY APPLICATIONS:
  Fracture surface analysis (fractography):
    Fatigue striations, dimpled ductile fracture, cleavage facets
    Find crack origin (trace back from striation or river mark convergence)
  Powder characterization: particle shape, size, surface
  Coating cross-section: layer thickness, adhesion, defects
  Phase identification combined with EDS
  Inclusion analysis (automated feature analysis)
```

### EDS and WDS (X-ray Spectroscopy)

```
EDS vs WDS COMPARISON
──────────────────────────────────────────────────────────────────
Both: identify elements from characteristic X-ray energies emitted by beam

EDS (Energy Dispersive Spectroscopy):
  Single detector, fast (~60 seconds for spectrum)
  Energy resolution: ~130 eV FWHM at 5.9 keV (Mn Kα)
  Peak overlaps: common problem (Fe Kα overlaps with Cr, Ti Kβ, etc.)
  Quantification: accurate to ~0.5–2 wt% with standards
  Application: qualitative identification, elemental maps, phase chemistry

WDS (Wavelength Dispersive Spectroscopy):
  Crystal spectrometer, sequential wavelength scan (slower, more precise)
  Energy resolution: ~5–10 eV (10× better than EDS)
  Better for light elements (C, N, B) and overlapping peaks
  More accurate quantification (~0.01 wt% detection limits with standards)
  Available on: EPMA (Electron Probe Microanalyzer) — dedicated instrument

ELEMENTAL MAPPING:
  Raster beam with EDS → color map of element concentration
  Shows: segregation, diffusion profiles, coating composition, inclusion chemistry
  Resolution: limited by beam interaction volume (~1 µm at 15 kV for dense metals)
  → Can't resolve features < ~1 µm with standard EDS mapping (use TEM-EDS for finer)
```

### EBSD (Electron Backscatter Diffraction)

```
EBSD — CRYSTAL ORIENTATION MAPPING
──────────────────────────────────────────────────────────────────
Kikuchi patterns from BSE → index crystal orientation at each point
Raster across polished (no etch) surface → orientation map (IPF map)

What EBSD reveals:
  Grain size distribution (automated grain detection)
  Texture (preferred crystallographic orientation → pole figures)
  Grain boundary character (misorientation angle → LAB vs HAB)
  Phase identification (pattern matching vs crystal structure databases)
  Strain/kernel average misorientation (KAM) → deformation state

Applications:
  Verify recrystallization (new equiaxed grains, low KAM)
  Quantify deformation (high KAM = high dislocation density)
  Texture development in rolled/drawn products
  Identify phases in complex alloy (distinguish martensite from retained austenite)
  EBSD + EDS combined: simultaneous chemistry + orientation

Sample requirement: carefully polished (OPS or electropolish finish)
  Residual scratches cause pattern degradation → wrong orientation data
```

---

## Transmission Electron Microscopy (TEM)

```
TEM FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Electron beam transmitted THROUGH thin specimen (~50–200 nm thick)
Resolution: 0.1–0.2 nm (can image individual atom columns)
Voltage: 80–300 kV (higher = shorter wavelength = better resolution)

WHAT TEM REVEALS THAT SEM CANNOT:
  Dislocation structure (density, arrangement, interaction)
  Precipitate size and distribution at nanometer scale
  Coherency of precipitates with matrix (coherency strains)
  Stacking faults, twins at atomic scale
  Grain boundary structure and chemistry at nm scale
  Crystal structure of unknown phases (selected area diffraction patterns)

IMAGING MODES:
  Bright field (BF): transmitted beam → defects appear dark (diffraction contrast)
  Dark field (DF): diffracted beam selected → precipitates/defects appear bright
  HAADF-STEM (High-Angle Annular Dark Field):
    Z-contrast imaging: heavy elements bright, light elements dark
    → Atomic-column imaging, precipitate contrast, segregation

  STEM-EDS: elemental maps at 1–5 nm resolution (much better than SEM-EDS)
  EELS (Electron Energy Loss Spectroscopy): light elements, bonding states, oxidation states

SAMPLE PREPARATION (labor-intensive):
  FIB (Focused Ion Beam): site-specific lift-out → thin from specific location
    Essential for: coatings, interfaces, specific microstructural features
    30 kV Ga ion mill → ~100 nm specimen, then clean at low kV
  Electropolishing: jet of electrolyte thins bulk metal sample
  Ion milling: Ar ion beam from both sides until electron transparent

Applications:
  Precipitate identification in age-hardened alloys (γ' in Ni superalloys)
  Dislocation density quantification after deformation
  Thin film interface structure (adhesion layers, diffusion barriers)
  Atomic-scale imaging of grain boundaries
  Research: novel phases, defect mechanisms, interface chemistry
```

---

## X-ray Diffraction (XRD)

<!-- @editor[bridge/P2]: Bragg's law (nλ = 2d sinθ) is constructive interference — the same physics as diffraction gratings, antenna arrays, and phased array radar. The XRD diffraction pattern is a hash/fingerprint of the crystal structure: each phase produces a unique pattern (set of d-spacings) that identifies it, just as a spectral fingerprint identifies a molecule. Phase identification from XRD is pattern matching against a database (ICDD) — the same operation as a hash lookup or signature matching in software. For any engineer who knows wave optics or signal processing, the Bragg equation is immediately familiar. Not called out. -->
```
XRD FUNDAMENTALS
──────────────────────────────────────────────────────────────────
X-rays diffract from crystal planes → Bragg's Law:
  nλ = 2d sin(θ)
  d = interplanar spacing, θ = diffraction angle, λ = X-ray wavelength
  Each crystal phase has unique set of d-spacings → unique diffraction pattern

APPLICATIONS:

1. PHASE IDENTIFICATION:
   Compare diffraction peaks to ICDD database (powder diffraction file)
   → Identify which phases present (α-Fe, γ-Fe, Fe₃C, Fe₄N, etc.)
   Can detect phases down to ~3–5 wt% (detection limit)
   Example: verify carburized steel → detect retained austenite (FCC γ-Fe peaks)

2. RETAINED AUSTENITE QUANTIFICATION:
   Compare intensities of austenite vs. martensite peaks
   Standards: ASTM E975
   Important for: bearing steels, gear steels (retained austenite = lower hardness,
     dimensional instability → must be minimized or controlled)

3. RESIDUAL STRESS MEASUREMENT:
   Lattice parameter shifts with stress → sin²ψ method
   Peak position shifts by ~0.01–0.1° 2θ per 100 MPa
   Measure at multiple tilt angles (ψ) → slope gives stress
   Applications: shot-peened surfaces, welded joints, machined surfaces
   Non-destructive (surface layer ~10–50 µm penetration depth)

4. CRYSTALLITE SIZE AND MICROSTRAIN (Scherrer/Williamson-Hall):
   Peak broadening → particle/crystallite size (Scherrer equation)
   Williamson-Hall plot separates size broadening from strain broadening
   Applications: nanoparticles, cold-worked metals, thin films

5. LATTICE PARAMETER DETERMINATION:
   Precise d-spacing → composition in solid solutions (Vegard's law)
   Example: carbon content in austenite (lattice expands with C content)
```

---

## Thermal Analysis

### Differential Scanning Calorimetry (DSC)

```
DSC PRINCIPLES AND APPLICATIONS
──────────────────────────────────────────────────────────────────
Measures heat flow into/out of sample vs temperature (or time)
Reference pan vs sample pan → measure differential heat input needed for same T

WHAT DSC MEASURES:

Thermal transitions:
  Tg (glass transition): step change in heat capacity → baseline shift
    Amorphous polymers, glasses, metallic glasses
    Below Tg: glassy; above Tg: rubbery → critical for service temperature

  Tm (melting): endothermic peak → latent heat absorbed
    Semi-crystalline polymers, metals, alloys
    Area under peak = latent heat of fusion (J/g) → crystallinity calculation:
      % crystallinity = (ΔHm_measured / ΔHm_100%) × 100

  Crystallization: exothermic peak on cooling (or heating, cold crystallization)
    Crystallization temperature, rate, enthalpy

  Cure of thermosets: exothermic peak during isothermal hold
    Total heat of reaction, degree of cure, gelation point
    Quality control: verify epoxy has fully cured (residual cure exotherm)

Phase transformations in metals:
  Austenite → martensite: athermal (not well measured by DSC)
  Precipitation reactions: exothermic, measureable
  Solidus/liquidus temperatures of alloys: melting onset and completion

Applications:
  Polymer: identify material (Tg/Tm fingerprint), verify crystallinity, check cure
  Metal: verify age-hardening precipitation sequences, measure transformation T
  Pharmaceutical: polymorphic forms, stability
  Food: fat crystallization, starch gelatinization
```

### Thermogravimetric Analysis (TGA)

```
TGA PRINCIPLES AND APPLICATIONS
──────────────────────────────────────────────────────────────────
Measures sample MASS vs temperature/time
Detects: decomposition, oxidation, moisture evaporation, phase changes involving gas

APPLICATIONS:

Polymer analysis:
  Decomposition temperature: safety, processing limit
  Filler content: burn off organic matrix → residue = inorganic filler (%)
    QC: verify 30% glass-filled Nylon actually has 30% glass
  Moisture content: weight loss at 100–150°C
  Plasticizer content: loss before polymer decomposition
  Carbon black content (in HDPE/PP): step loss in N₂ at 400–500°C

Ceramic/metal:
  Oxidation kinetics: weight gain vs time at elevated T (parabolic law fit)
  Carbon/sulfur content: loss on combustion
  TGO growth rate on MCrAlY coatings: continuous TGA in oxidizing atmosphere

Decomposition onset temperature:
  Defines maximum processing temperature for polymers
  Critical for injection molding (melt temperature must be below Tdeg)
  ABS: Tdeg ~350°C; Nylon 66: ~430°C

TGA + DSC combined (simultaneous TGA-DSC or STA):
  Same sample, same experiment → correlate mass loss with heat flow
  → Distinguish endothermic vaporization vs exothermic combustion
```

---

## Mechanical Testing

```
MECHANICAL TESTING OVERVIEW
──────────────────────────────────────────────────────────────────
TENSILE TESTING (ASTM E8, ISO 6892):
  Dog-bone specimen → monotonic axial load to fracture
  Measures:
    E (Young's modulus): initial elastic slope
    σ_YS (0.2% offset yield strength): practical yield
    UTS (ultimate tensile strength): maximum load
    Elongation at fracture (%El): ductility
    Reduction in area (%RA): ductility (sensitive to inclusions)

  Precision: load cell ±0.5%, extensometer ±0.5%
  Critical details: specimen geometry (parallel vs full-section), gauge length (25 vs 50 mm)
    → Results differ — must specify

HARDNESS TESTING:
  Rockwell (HR): most industrial, fast, direct scale reading
    HRC (cone indenter): hard materials, tool steel, case hardened
    HRB (ball indenter): softer materials, annealed steel, Al
  Vickers (HV): versatile, applies to any material, small load possible
    Pyramid indenter → optical measurement of indent diagonal
    Micro-Vickers (HV 0.1–1 kg): phases, thin layers, case depth profiles
  Brinell (HB): large ball indenter → averages over larger area → for cast, PM parts
    Standard for: aluminum castings, gray iron
  Knoop: elongated diamond → very light loads → surface layers, ceramics

CONVERSION (approximate):
  HRC 60 ≈ HV 746 ≈ HB 578 (very hard tool steel)
  HRC 40 ≈ HV 392 ≈ HB 372 (hardened gear)
  HRC 20 ≈ HV 248 ≈ HB 238 (normalized steel)
  Conversion formulas: ASTM E140 (never perfectly accurate — material dependent)

IMPACT TESTING:
  Charpy V-notch (CVN): standard (ASTM A370)
  Energy vs temperature → DBTT determination
  Specification: structural steel ASTM A36, A572 require minimum CVN at -20°C

FATIGUE TESTING:
  R.R. Moore rotating bending: constant amplitude → S-N curves
  Servo-hydraulic (MTS): any load ratio R, frequency, environment
  Crack growth (ASTM E647): pre-cracked CT specimen → da/dN vs ΔK
```

### Nanoindentation

```
NANOINDENTATION (INSTRUMENTED INDENTATION)
──────────────────────────────────────────────────────────────────
Berkovich (3-sided pyramid) or cube corner indenter
Load and displacement measured continuously → P-h curve
Depth resolution: < 1 nm; load resolution: < 1 µN

WHAT IT MEASURES:
  Hardness H = P / A (projected area from depth)
  Reduced modulus Er from unloading stiffness (Oliver-Pharr method)
  Creep: hold at peak load → displacement vs time
  Strain rate sensitivity: multiple loading rates

APPLICATIONS:
  Thin films: measure coating hardness (depth < 1/10 film thickness → substrate effect)
  Individual phases: test γ vs γ' in Ni superalloys separately
  Graded structures: hardness profile across carburized case
  Small samples: test where bulk tensile specimen impossible
  Polymers: measure Tg via nanoindentation (modulus drop)

LIMITATION:
  Pileup: soft materials pile up around indent → area underestimated → H wrong
  Residual stress: changes hardness and modulus measurement
  Surface roughness: must be < 5–10% of indent depth
```

---

## Non-Destructive Evaluation (NDE)

```
NDE OVERVIEW — DETECT INTERNAL DEFECTS WITHOUT DESTRUCTION
──────────────────────────────────────────────────────────────────
NDE METHODS COMPARED:

  ┌──────────────────────────────────────────────────────────────┐
  │ METHOD        │ DEFECT TYPE         │ DETECTION LIMIT        │
  ├──────────────────────────────────────────────────────────────┤
  │ Radiography   │ Internal voids,     │ ~1–2% of section       │
  │ (X-ray, γ)    │ inclusions, cracks  │ thickness; shape        │
  │               │ if open to beam     │ dependent               │
  ├──────────────────────────────────────────────────────────────┤
  │ Ultrasonic    │ Internal cracks,    │ 0.5–1 mm (pulse-echo)  │
  │ (UT)          │ delaminations,      │ TOFD/phased array:     │
  │               │ porosity            │ better resolution       │
  ├──────────────────────────────────────────────────────────────┤
  │ Eddy current  │ Surface + near-     │ 0.1–0.5 mm from        │
  │ (ET)          │ surface cracks      │ surface, depth ~3 mm   │
  │               │ (conductive only)   │                         │
  ├──────────────────────────────────────────────────────────────┤
  │ Liquid        │ Surface-open        │ ~0.025 mm (surface      │
  │ penetrant (PT)│ cracks only         │ only, all materials)    │
  ├──────────────────────────────────────────────────────────────┤
  │ Magnetic      │ Surface + near-     │ ~0.1 mm (ferromagnetic  │
  │ particle (MT) │ surface cracks      │ materials only)         │
  └──────────────────────────────────────────────────────────────┘

PHASED ARRAY UT (PAUT):
  Multiple elements electronically steered → images without moving probe
  Time-of-flight diffraction (TOFD): accurate depth sizing
  Full Matrix Capture (FMC) + Total Focusing Method (TFM):
    Software-focused imaging → highest resolution UT
  Applications: weld inspection, aerospace composites, pipeline

COMPUTED TOMOGRAPHY (CT) for materials:
  Industrial CT (micro-CT): 3D X-ray image of internal structure
  Resolution: 1–50 µm (micro-CT), better with synchrotron
  Applications: additive manufacturing pore mapping, casting inspection,
    fiber orientation in CFRP, electronics packaging failure analysis
  Limitation: thick metal sections attenuate too much for micro-CT
```

---

## Surface and Near-Surface Analysis

```
SURFACE ANALYSIS TECHNIQUES
──────────────────────────────────────────────────────────────────
XPS (X-ray Photoelectron Spectroscopy):
  X-ray excites photoelectrons from surface → measure kinetic energy
  Sampling depth: 2–10 nm (extreme surface sensitivity)
  Elements detected: Li and above (not H, He)
  Provides: elemental composition AND chemical bonding state
    Fe → metallic Fe vs FeO vs Fe₂O₃ vs FeOOH
    Ti → metallic vs TiO₂ vs TiC vs TiN
  Applications:
    Coating adhesion failure (which layer failed? interface chemistry)
    Passivation layer thickness and composition
    Contamination identification (why won't this bond?)
    Lubricant film characterization

AES (Auger Electron Spectroscopy):
  Electron beam excites Auger electrons
  Sampling depth similar to XPS (~2–5 nm)
  Advantage: fine beam (~10 nm) → spatial mapping, depth profiles
  Applications: thin film interdiffusion, grain boundary segregation (fracture surface)

SIMS (Secondary Ion Mass Spectrometry):
  Sputtered ions from primary ion beam analyzed by mass spectrometer
  Extreme sensitivity: sub-ppm trace elements
  Depth profiling: compositional profile with nm resolution
  Applications: semiconductor dopant profiles, oxide layer chemistry, trace contamination

Profilometry:
  Contact (stylus) or optical (white light interferometry, confocal)
  Measures: surface roughness (Ra, Rz, Rq), waviness, step height
  Output: Ra, Rz, Rq, power spectral density
  Critical for: PVD coating adhesion verification (Ra < 0.3 µm required)
              sealing surfaces, bearing surfaces
```

---

## Chemical Analysis

```
BULK CHEMICAL ANALYSIS
──────────────────────────────────────────────────────────────────
OES (Optical Emission Spectroscopy) — spark OES:
  Electric spark excites metal surface → emission spectrum
  Quantifies: C, Si, Mn, P, S, Cr, Ni, Mo, V, Cu in steels
  Fast (< 30 seconds per analysis), shop-floor instrument
  Standard: mill cert verification, incoming inspection of steel
  Detection limits: ~0.001–0.01 wt%

ICP-OES / ICP-MS (Inductively Coupled Plasma):
  Solution analysis: dissolve sample in acid → spray into Ar plasma
  ICP-OES: 0.1–10 ppm detection limits (multi-element simultaneously)
  ICP-MS:  0.001–0.1 ppb detection limits (very sensitive, trace elements)
  Applications: trace element certification, process bath analysis, water

LECO (combustion analysis):
  Carbon, sulfur, nitrogen, oxygen, hydrogen by combustion + gas detection
  C/S: burn in O₂, detect CO₂ and SO₂ by IR
  N/O: inert gas fusion, detect N₂ and CO by TCD/IR
  Critical for: C in steel (ppm level in IF steel), oxygen in steel/titanium

FTIR (Fourier Transform Infrared Spectroscopy):
  IR absorption → molecular bond vibrations → functional group identification
  Polymers: identify polymer type (PE, PP, PET all have distinctive spectra)
            detect oxidation (carbonyl peak at 1720 cm⁻¹)
            monitor cure of adhesives/coatings
  Not useful for: pure metals (no IR-active bonds), most ceramics

Raman Spectroscopy:
  Complementary to FTIR (different selection rules)
  Works through glass containers, aqueous samples
  Applications: carbon allotropes (graphene, diamond, DLC — sp2 vs sp3 D/G ratio)
               ceramic phase identification (Al₂O₃ polymorphs)
               polymer stress (peak shift under strain)
               in-situ monitoring through reactor windows
```

---

## Decision Cheat Sheet

| Characterization Need | Technique |
|-----------------------|-----------|
| Identify phases in heat-treated steel | XRD (phase ID) + optical microscopy (etch) |
| Measure retained austenite in hardened steel | XRD (ASTM E975) |
| Measure residual stress in shot-peened surface | XRD sin²ψ method |
| Image fracture surface (fatigue striation) | SEM (SE imaging) |
| Map element distribution across weld | SEM-EDS elemental map |
| Determine crystal orientation (texture) | EBSD |
| Image precipitates at nm scale (γ' in Ni alloy) | TEM (bright field + STEM-HAADF) |
| Measure grain size in steel | Optical microscopy after nital etch |
| Identify polymer (incoming QC) | FTIR or DSC (Tg/Tm fingerprint) |
| Measure polymer crystallinity | DSC (ΔHm comparison) |
| Verify thermoset fully cured | DSC (no residual cure exotherm) |
| Determine filler content in composite | TGA (burn off matrix, weigh residue) |
| Hardness of thin PVD coating | Nanoindentation (depth < film/10) |
| Detect internal pores in casting | X-ray radiography or CT scan |
| Inspect weld for subsurface flaws | Phased array UT (PAUT) |
| Detect surface cracks in aluminum | Liquid penetrant (PT) |
| Detect surface cracks in steel | Magnetic particle (MT) |
| Identify surface chemistry on failed bond | XPS (chemical state, not just elemental) |
| Bulk elemental composition of steel | Spark OES |
| Trace element content (ppm level) | ICP-MS |

---

## Common Confusion Points

**SEM resolution vs EDS resolution**: SEM can image features at 1–5 nm resolution using secondary electrons. But EDS spatial resolution is limited by the electron beam interaction volume in the material — at 15 kV in a dense metal, the X-ray generation volume is ~1 µm diameter. You can point the SEM at a 50 nm precipitate and measure X-rays, but the signal will include contributions from ~1 µm of surrounding matrix. For nm-resolution chemistry, you need TEM-EDS.

**XRD detects phases, not elements**: XRD identifies crystalline phases by their diffraction pattern. It cannot tell you the elemental composition of an unknown material directly — only what crystalline compounds are present. A steel with Fe₃C (cementite), α-Fe (ferrite), and retained γ-Fe (austenite) will show all three phases in XRD. But an amorphous phase won't appear in XRD at all. For elements, use OES or EDS.

**Hardness conversion tables are material-specific**: ASTM E140 provides conversion tables between HRC, HB, HV, etc. But these conversions are empirical, derived from carbon steel. For stainless steel, tool steel, cast iron, aluminum, or titanium, the conversions differ — sometimes significantly. Always specify which hardness scale you actually measured rather than converting and reporting a different scale.

**DSC measures heat flow, not phases directly**: DSC tells you that something happens thermally (exo or endo, at what temperature). It does not tell you what phase is forming or disappearing. To identify the phase, you need XRD or TEM on a sample quenched from that temperature. DSC + XRD together map the transformation temperature AND identify the phases involved.

<!-- @editor[bridge/P3]: NDE POD (probability of detection) curves are ROC curves for physical defect classifiers. The POD curve (P(detect | flaw size a) vs a) is the TPR curve as a function of signal strength — exactly the ROC curve used in ML classifier evaluation. The 90/95 POD value is the operating point on the ROC curve. The tradeoff between false negative rate (miss a crack) and false positive rate (unnecessary repair) maps exactly to ROC analysis. For anyone who works with ML classifiers, naming this as "ROC analysis for physical NDT classifiers" would be illuminating. -->
**NDE probability of detection (POD) vs detection limit**: An NDE technique's nominal detection limit (e.g., "UT detects 0.5 mm flaws") is deterministic. Real POD curves are probabilistic — there's a statistical probability of detecting a given flaw size, not a sharp cutoff. ASTM E2862 and MIL-HDBK-1823A define POD methodology. For damage tolerance calculations, use the 90/95 POD value (90% probability of detection with 95% confidence), not the nominal limit.

**Profilometry Ra vs Rz**: Ra (arithmetic mean roughness) is the most common surface roughness parameter. Rz (mean roughness depth, 10-point average) is more sensitive to peaks and valleys. A surface with a few deep scratches may have acceptable Ra but unacceptable Rz. For sealing surfaces and fatigue-critical parts, Rz is often the more relevant parameter. Specify which one you require.
