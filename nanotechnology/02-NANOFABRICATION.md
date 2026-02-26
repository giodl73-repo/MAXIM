# Nanofabrication: Top-Down Lithography and Bottom-Up Deposition

## The Big Picture

Nanofabrication is the set of processes that create structures at 1-100 nm. Top-down
methods start with bulk material and remove or pattern it. Bottom-up methods build
from atoms and molecules. Production semiconductor manufacturing is almost entirely
top-down; emerging nanotechnology uses both.

```
NANOFABRICATION METHODS MAP
=============================

TOP-DOWN (remove material)            BOTTOM-UP (add material)
==================================    ==================================

OPTICAL LITHOGRAPHY                   CHEMICAL VAPOR DEPOSITION (CVD)
  DUV (193 nm ArF): 7-10 nm node        Polysilicon, Si3N4, SiO2
  EUV (13.5 nm): 3-5 nm node            CNT growth, graphene on Cu
  Immersion, multipatterning             SiC, III-V compound semiconductors

ELECTRON BEAM LITHOGRAPHY (EBL)       ATOMIC LAYER DEPOSITION (ALD)
  10 nm resolution                      Self-limiting: 1 monolayer/cycle
  Serial (slow)                         HfO2 gate dielectric (MOSFET)
  Research tool                         Al2O3 encapsulants, barrier layers
  Proximity effect challenge

FOCUSED ION BEAM (FIB)               MOLECULAR BEAM EPITAXY (MBE)
  Ga+ or He+ ions                      Single monolayer control
  Dual-beam: image + mill              III-V semiconductors (GaAs, InP)
  Circuit edit, TEM prep               Quantum wells, HEMT structures
  ~10 nm resolution milling

NANOIMPRINT LITHOGRAPHY (NIL)        SELF-ASSEMBLED MONOLAYERS (SAM)
  Physical stamp (mold)                Thiols on gold, silanes on SiO2
  Sub-10 nm resolution                 Chemical functionalization
  High throughput potential            Bionanotechnology interface

DEEP REACTIVE ION ETCH (DRIE)        DNA ORIGAMI / SELF-ASSEMBLY
  Bosch process for deep Si            Sub-10 nm features possible
  MEMS structures (gyros, mirrors)     Defect rates still challenging
  Aspect ratio up to 50:1
```

---

## Top-Down: Optical Lithography

### Resolution Limit: Rayleigh Criterion

```
RAYLEIGH RESOLUTION LIMIT
===========================

  R = k1 * lambda / NA

where:
  R   = minimum resolvable feature (half-pitch)
  k1  = process factor (theoretical minimum 0.25, practical ~0.28)
  lambda = exposure wavelength
  NA  = numerical aperture (n * sin(theta))

WAVELENGTH PROGRESSION:
  g-line:   436 nm -> R ~ 350 nm (1980s)
  i-line:   365 nm -> R ~ 250 nm (1990s)
  KrF DUV:  248 nm -> R ~ 180 nm (late 1990s)
  ArF DUV:  193 nm -> R ~ 130 nm dry (early 2000s)
  ArF immersion: 193 nm, NA=1.35 -> R ~ 38 nm (with k1~0.27)
  EUV:      13.5 nm, NA=0.33 -> R ~ 13 nm, NA=0.55 -> R ~ 8 nm

TRICKS TO BEAT THE RAYLEIGH LIMIT:
  Immersion lithography: water (n=1.44) between lens and wafer
    Effective lambda = 193/1.44 = 134 nm -- bought another generation
  Phase shift masks (PSM): modify phase to enhance contrast
  Off-axis illumination: dipole, quadrupole, annular
  Optical proximity correction (OPC): pre-distort mask to correct diffraction
  Multipatterning: pattern same layer 2-4 times (LELE, SADP, SAQP)
    SADP: single lithography -> spacer deposition -> etch spacer -> removes
          original, leaving spacer features at half the pitch
    Cost: 2-4x process steps per layer; complexity, overlay errors
```

### EUV Lithography (13.5 nm)

```
EUV LITHOGRAPHY SYSTEM
========================

Light source:
  Sn plasma (tin droplet hit by CO2 laser)
  Emission at 13.5 nm (Sn ion transitions)
  Power: 250-500 W at intermediate focus
  Collector mirror collects ~3-4% of emitted EUV

Optics:
  All reflective (no lenses -- EUV absorbed by glass)
  10 multilayer Mo/Si mirrors (40% reflectivity each)
  Final transmission to wafer: ~2-3%

Mask:
  Reflective (vs. transmissive in DUV)
  TaN absorber on Mo/Si multilayer reflector
  Defects: 1 programmed defect ruins a chip -- must be zero defects

Resists:
  CAR (chemically amplified resists): stochastic noise is challenge
  Metal-containing resists (Inpria): better resolution/LER
  Dose required: 10-30 mJ/cm^2 (higher than DUV)

Vacuum environment: all above in 10^-6 Pa vacuum (EUV absorbed by air)

Current state (2026):
  ASML NXE:3600D: NA=0.33, ~3 nm node capable
  ASML EXE:5000 (High-NA): NA=0.55, ~2 nm node capable, introduced 2024
  Throughput: 120-150 wafers/hour
  Cost: ~$380M per system (NXE), ~$500M+ (High-NA)
  TSMC 3nm: all-EUV patterning critical layers
```

---

## Electron Beam Lithography (EBL)

```
EBL SYSTEM OVERVIEW
====================

Principle:
  Focused electron beam (10-100 keV) directly writes resist
  No mask -- pattern defined by deflection control
  Serial writing: beam moves point to point

Resolution:
  Forward scattering: beam broadens in resist (~1-5 nm)
  Backscattering from substrate: electrons scatter back (range ~10 um)
  Point spread function: sharp core + broad tail
  Minimum feature: ~10 nm (forward scattering dominated)
  Demonstrated sub-5 nm in research labs (on thin membranes)

PROXIMITY EFFECT:
  +------------------+        +------------------+
  |  isolated dot    |        |  dense array     |
  |  (low dose)      |        |  (high local dose|
  |                  |        |   from backscatter|
  |    *             |        |  **   **   **    |
  |                  |        |  dose overlap    |
  +------------------+        +------------------+

  Solution: Proximity effect correction (PEC) -- modify dose at each pixel
  based on pattern environment. Computationally expensive.

Speed:
  Writing 1 cm^2 at 10 nm pixels: ~1 cm^2 / (10e-9)^2 = 10^14 pixels
  At 10 MHz writing rate: 10^7 seconds = not feasible
  Typical: write only features, not entire wafer area
  Practical write time: hours to days for full chip -- research only

Equipment:
  Raith EBPG5000+: 100 keV, sub-10 nm
  JEOL JBX-9500FS: 100 keV, high throughput variant
  Modified SEMs: 10-30 keV, 30-50 nm resolution (cheap, educational)
```

---

## Focused Ion Beam (FIB)

FIB uses a focused beam of gallium ions (Ga+) or helium ions (He+) to sputter material
or deposit material via gas injection.

```
FIB OPERATIONS
===============

MILLING (subtractive):
  Ga+ at 30 keV, current 1 pA - 20 nA
  Sputter rate: ~1-10 um^3/min depending on material
  Resolution: ~10 nm (Ga+), ~2 nm (He+)
  Damage layer: ~20 nm Ga implantation (Ga+ FIB)

DEPOSITION (additive):
  Inject precursor gas (organometallic: W(CO)6, Pt(PF3)4)
  FIB cracks gas -> deposits Pt, W, C on surface
  Used for: circuit edit (connect/sever metal lines on IC)
            TEM sample prep (protective cap before sectioning)

DUAL-BEAM (FIB + SEM):
  FIB mills cross-section, SEM images it simultaneously
  3D tomography: slice and image sequentially
  TEM lamella preparation: extract 100 nm thin slice from specific location

Applications:
  Circuit edit: modify IC after fabrication (add/remove connections)
  TEM prep: standard method for cross-sectional TEM of semiconductor devices
  Failure analysis: expose and image defect sites
  Rapid prototyping: custom nanostructures for research
```

---

## Nanoimprint Lithography (NIL)

```
NIL PROCESS FLOW
=================

STEP 1: Master mold fabrication
  EBL or FIB to create Si or quartz mold
  Features down to <10 nm

STEP 2: Resist deposition
  Spin-coat imprint resist (thermoplastic or UV-curable)

STEP 3: Imprint
  Thermal NIL: heat above Tg (glass transition), press mold
  UV-NIL: transparent mold, UV cure at room temperature

  Mold        Mold        Mold
    \/          \/       lifts
  [resist]   [resist]     [pattern]
  [wafer]    [wafer]     [wafer]

STEP 4: Residual layer etch
  O2 RIE removes thin residual resist layer in mold recesses

STEP 5: Pattern transfer
  Etch or liftoff using imprinted resist as mask

ADVANTAGES vs. optical lithography:
  Sub-10 nm resolution (mechanical, not diffraction-limited)
  No expensive photons/electrons needed
  High throughput potential (parallel)
  Used in: hard disk magnetic patterns (1D pitch), nanophotonics, polymer electronics

CHALLENGES:
  Mold defects replicate to every wafer (contamination)
  Overlay accuracy: ~5 nm (vs 2 nm for EUV)
  Mold wear: how many prints before degradation?
  Not yet in mainstream semiconductor production
```

---

## Bottom-Up: Chemical Vapor Deposition (CVD)

```
CVD PROCESS TYPES
==================

THERMAL CVD:
  Precursor gas + heat -> decomposition -> deposition
  SiH4 -> Si + 2H2  (polysilicon deposition, 620 C)
  TEOS -> SiO2      (silicon dioxide, 650 C)
  TMGa + AsH3 -> GaAs (III-V growth, 650-750 C)

PLASMA-ENHANCED CVD (PECVD):
  Plasma breaks bonds at lower temperature (~300 C vs. 600+ C thermal)
  Critical for: depositing on already-processed devices (thermal budget)
  SiH4 + NH3 + plasma -> Si3N4 (nitride passivation)

METALORGANIC CVD (MOCVD / MOVPE):
  Metalorganic precursors (TMGa, TMAl, TEIn) + hydrides (AsH3, PH3)
  Growth of III-V compound semiconductors (GaAs, InGaAs, GaN)
  Used for: LED epitaxy (GaN LEDs), high-electron-mobility transistors (HEMT)
  Growth rate: 0.1-10 um/hour; thickness control ~1% with rate control

CNT GROWTH (CVD):
  Fe or Co catalyst nanoparticles on substrate
  CH4 or C2H2 + H2 at 700-900 C
  Carbon dissolves into catalyst, CNT grows from catalyst tip
  SWCNT: ~1 nm diameter; MWCNT: 5-50 nm diameter
  Diameter controlled by catalyst NP size
  Chirality (electronic type): currently not well-controlled -- random mixture
```

---

## Bottom-Up: Atomic Layer Deposition (ALD)

ALD is the most precise thin-film deposition technique. It deposits exactly one
monolayer per cycle via self-limiting surface chemistry.

```
ALD CYCLE (example: Al2O3 from TMA + H2O)
==========================================

Cycle step 1: PULSE A (trimethylaluminum, TMA)
  Al(CH3)3 gas enters chamber
  Reacts with -OH surface groups: -OH + Al(CH3)3 -> -O-Al(CH3)2 + CH4
  All surface -OH sites react (self-limiting)
  Excess TMA evacuated

Cycle step 2: PURGE
  N2 purge removes unreacted TMA and byproducts

Cycle step 3: PULSE B (water vapor, H2O)
  H2O reacts with surface -Al(CH3) groups
  -O-Al(CH3)2 + 2H2O -> -O-Al(OH)2 + 2CH4
  Surface covered with -OH again (self-limiting)

Cycle step 4: PURGE
  N2 purge removes unreacted H2O and CH4

ONE CYCLE = ONE MONOLAYER (~0.1 nm of Al2O3)

RESULT:
  Thickness = (cycles) x (growth per cycle, ~0.1 nm)
  Uniformity: <1% across 300 mm wafer
  Conformality: coats deep trenches with aspect ratio 100:1
  No pinholes: self-limiting prevents incomplete coverage

KEY ALD APPLICATIONS:
  HfO2 high-k gate dielectric (Intel 45nm node 2007, all CMOS since)
    ALD HfO2 replaced SiO2 -- same k*thickness, less tunneling leakage
  Al2O3 encapsulant for OLEDs (moisture barrier, 1 cycle = 0.1 nm)
  TiN barrier in Cu interconnects
  Conformal coating of 3D NAND flash storage (100+ layers)
  ZnO seed layer for nanowire growth
```

---

## Bottom-Up: Molecular Beam Epitaxy (MBE)

```
MBE SYSTEM
===========

Ultra-high vacuum: 10^-10 to 10^-11 torr
  (Base pressure lower than lunar surface atmosphere)

Effusion cells (Knudsen cells):
  Elemental sources (Ga, Al, In, As, P...) heated to evaporation temp
  Shutters control on/off of each beam
  Flux controlled by temperature -> growth rate

RHEED (in-situ monitor):
  Reflection High Energy Electron Diffraction
  Electron beam grazes surface; diffraction pattern on fluorescent screen
  Oscillations: each oscillation = 1 monolayer grown
  Real-time thickness control to 0.1 monolayer precision

GROWTH RATES AND CONTROL:
  GaAs: ~1 um/hr = ~3 monolayers/second
  Shutter speed: ~0.1 s -> 0.3 monolayer uncertainty
  Interface abruptness: 1-2 monolayers (0.3-0.6 nm) routinely achievable

EPITAXIAL STRUCTURES MADE BY MBE:
  Quantum wells: GaAs (10 nm) / AlGaAs (50 nm) repeating stack
  HEMT: AlGaAs/InGaAs (high-electron-mobility transistor -- RF, mm-wave)
  Quantum cascade laser: 200+ layers, each 3-20 nm, precise thickness
  Modulation-doped structures: dopants in barrier, carriers in well

WHY MBE OVER MOCVD?
  MBE: better interface abruptness, in-situ characterization, no H-bearing gas
  MOCVD: higher throughput, lower vacuum requirements, scale-up to manufacturing
  Research: MBE; Production: MOCVD
```

---

## Comparison Table

| Method | Resolution | Throughput | Mode | Primary Use |
|--------|-----------|------------|------|-------------|
| EUV lithography | 8-13 nm | 120-150 wph | Parallel | Semiconductor production |
| DUV + multipatterning | 7-10 nm | 250+ wph | Parallel | Semiconductor production |
| E-beam lithography | 10 nm | Very low | Serial | Research, masks |
| FIB milling | 10-50 nm | Very low | Serial | Edit, TEM prep |
| Nanoimprint | <10 nm | Medium | Parallel | Hard disk, nanophotonics |
| ALD | 0.1 nm/cycle | Medium | Blanket | High-k, barriers, MEMS |
| CVD | Varies | Medium-high | Blanket | Polysilicon, epitaxy |
| MBE | 0.3 nm/layer | Low | Blanket | III-V research, HEMT |

---

## Decision Cheat Sheet

| You want to... | Use... |
|---------------|--------|
| Make transistors at 3nm node in production | EUV + SAQP multipatterning |
| Write custom patterns at 10 nm (research) | E-beam lithography |
| Edit a circuit or prepare TEM sample | FIB dual-beam |
| Deposit exactly N monolayers of insulator | ALD |
| Grow III-V quantum wells for lasers | MBE (research) or MOCVD (production) |
| Grow carbon nanotubes on substrate | CVD with catalyst nanoparticles |
| Replicate a mold pattern at <10 nm | Nanoimprint lithography |
| Deposit conformal film in deep trench | ALD (>PECVD, >sputtering) |

---

## Common Confusion Points

**"EUV uses 13.5 nm wavelength, so how do you make 3nm features?"** The Rayleigh criterion
gives the minimum half-pitch, not minimum feature. With NA=0.33 and k1=0.28, you get
~13 nm half-pitch. Then multiple patterning (SADP) halves that. Plus the "3nm node" label
is not a literal dimension.

**"ALD is slow -- you'd need thousands of cycles for a thick film."** Correct. ALD is used
for precision thin films (3-20 nm) where thickness control and conformality are critical,
not for depositing microns of material. PECVD or CVD handles thick films.

**"EBL has the best resolution, so why not use it in production?"** Serial writing. A 300 mm
wafer with 5 nm features has ~10^12 elements to write. EBL writes at ~10^7 pixels/second.
You would need years per wafer. Parallel lithography (optical or imprint) is mandatory.

**"MBE needs ultra-high vacuum -- too expensive for production."** Correct observation; MBE
is primarily a research tool. MOCVD (MOVPE) fills the production role for III-V epitaxy
at much higher throughput in moderately low vacuum.
