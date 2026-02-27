# Lithography — A Layered Guide

## The Big Picture

Lithography is the patterning engine of semiconductor manufacturing. Every layer
of a chip — transistors, contacts, metal wires — starts with light printing a pattern
onto photoresist. At 2 nm nodes, EUV light with 13.5 nm wavelength is printing
features that are still 5-10× smaller than the wavelength through clever optics and
multi-patterning schemes.

```
LITHOGRAPHY IN THE FAB FLOW
════════════════════════════════════════════════════════════════════

Wafer enters clean room (ISO Class 1 — <10 particles/m³ ≥0.1 µm)
    │
    ▼
Coat photoresist (spin-coat: ~30-100 nm thick polymer film)
    │
    ▼
Expose: light through mask/reticle → photoresist records pattern
    │
    ▼
Post-exposure bake (PEB) — acid diffusion (chemically amplified resist)
    │
    ▼
Develop: dissolve exposed (positive) or unexposed (negative) resist
    │
    ▼
Inspect: CD-SEM measures critical dimensions, defect inspection
    │
    ▼
Etch or implant using resist as mask → pattern transferred to film below
    │
    ▼
Strip resist (O₂ plasma + wet clean)
    │
    ▼ Repeat ~100× for all layers of a 3 nm chip
```

---

## The Rayleigh Criterion

```
OPTICAL RESOLUTION LIMIT

Rayleigh criterion (for minimum resolvable feature):
  R = k₁ · λ / NA

  R  = minimum feature size (half-pitch)
  k₁ = process factor (0.25 minimum, practical ~0.28-0.35)
  λ  = light wavelength
  NA = numerical aperture of lens (NA = n·sin θ, n = refractive index)

DEPTH OF FOCUS (also critical):
  DoF = k₂ · λ / NA²   (DoF shrinks faster than resolution as NA increases)

IMPROVEMENT LEVERS:
  1. Reduce λ (wavelength)
  2. Increase NA
  3. Reduce k₁ via resolution enhancement techniques (OPC, PSM, SMO)
  4. Immersion: fill space between lens and wafer with water (n=1.44) → NA > 1

HISTORICAL WAVELENGTHS:
  g-line   436 nm  (1970s-80s, mercury lamp)
  i-line   365 nm  (1980s-90s, mercury lamp)
  KrF DUV  248 nm  (1990s-2000s, excimer laser)
  ArF DUV  193 nm  (2000s → present, excimer laser) ← STILL USED
  ArF imm  193 nm  but in water: effective λ/1.44 = 134 nm equivalent
  EUV      13.5 nm (2019+ high volume, ASML only)

RESOLUTION EXAMPLES (ArF immersion, NA=1.35, k₁=0.28):
  R = 0.28 × 134 nm / 1.35 ≈ 28 nm  single patterning
  With SADP: 14 nm half-pitch effectively
  With SAQP: 7 nm half-pitch effectively
```

---

## DUV Lithography: 248 nm and 193 nm

```
DUV (DEEP ULTRAVIOLET) LITHOGRAPHY

KrF EXCIMER LASER (248 nm):
  Used: 250 nm → 130 nm generation (1990s-2000s)
  Pulse energy: ~10 mJ, repetition rate 2-4 kHz
  Now used for non-critical layers at 10 nm nodes (field, pad layers)

ArF EXCIMER LASER (193 nm):
  Introduced ~2000 for 130 nm, extended far beyond expectation
  Dry ArF: 193 nm in air, NA up to ~0.93
    Used to pattern: 90 nm node (2004), 65 nm, 45 nm
  ArF IMMERSION (193i) — the key breakthrough:
    Demineralized water between final lens element and wafer (n=1.44)
    Effective wavelength: 193/1.44 ≈ 134 nm
    Max NA achievable: 1.35 (Zeiss lenses in ASML, Nikon tools)
    Single patterning limit: ~38 nm (k₁=0.28, NA=1.35)
    Extended via multi-patterning to 10 nm and below

ArF IMMERSION TOOL SPECS (ASML TWINSCAN NXT:1980i):
  Throughput: ~275 wafers/hour (26 mm × 33 mm field)
  Overlay: <2 nm (3σ)
  CD uniformity: <1 nm (3σ)
  Cost: ~$60-80M per tool

CHEMICALLY AMPLIFIED RESIST (CAR):
  KrF/ArF use CAR: acid catalyst amplifies sensitivity 100-1000×
  Each photon creates acid → diffuses during PEB → deprotects many polymer sites
  Resolution limit determined by acid diffusion length (blur) + resist roughness
  193i resist: acrylic polymer, tailored for 193 nm absorption
```

---

<!-- @editor[bridge/P3]: Multi-patterning section could connect to a software analogy: SADP/SAQP adds litho steps to recover resolution that physics no longer provides directly — same pattern as technical workarounds that accumulate layers of complexity to compensate for a fundamental constraint; the comparison to shim layers / compatibility layers in software would resonate with a senior engineering leader evaluating architectural trade-offs -->

## Multi-Patterning: Extending 193i Beyond Its Limit

```
MULTI-PATTERNING (MPT) — extending 193i to 10 nm and below

SADP (Self-Aligned Double Patterning):
  Create features at half the litho pitch

  Step 1: Pattern "core" features by 193i litho at pitch P
          ┌─┐   ┌─┐   ┌─┐   ┌─┐   spacing = P
  Step 2: Deposit conformal spacer material (ALD)
         ┌┼─┼┐ ┌┼─┼┐
  Step 3: Etch spacer anisotropically — leaves spacers on core sidewalls
           │ │   │ │ (spacers at P/2)
  Step 4: Remove core (etch selective to spacer)
           │ │   │ │   final pitch = P/2
  Step 5: Etch underlying film using spacers as mask

  Net effect: half the pitch from one litho step
  Used for: metal pitches at 14 nm → 10 nm → 7 nm

SAQP (Self-Aligned Quadruple Patterning):
  Apply SADP twice → 1/4 pitch
  Used for: metal pitches at 5 nm, 3 nm
  TSMC N3: SAQP for metal layers at ~18-24 nm pitch (originally printed at ~72 nm)

LELE (Litho-Etch-Litho-Etch) Double Patterning:
  Two separate litho + etch cycles, features interdigitated
  Problem: overlay between exposures must be <5 nm for adjacent features at 20 nm pitch
  CDR (Cut Define and Remove) and coloring: EDA tools partition patterns across masks

COST IMPACT:
  Each multi-patterning step adds 1-3 litho exposures + extra process steps
  10 nm logic: 30-40 patterning steps (some layers need 3-4 exposures)
  Major contributor to 3 nm wafer costing $20K (vs $3K for 28 nm)
```

---

## EUV Lithography

```
EUV (EXTREME ULTRAVIOLET) LITHOGRAPHY — 13.5 nm

THE ASML NXE PLATFORM (ASML has ~100% market share for EUV):
  NXE:3400C: production since 2019, ~170 wph throughput
  NXE:3600D: production since 2022, ~220 wph
  High-NA EUV (NXE:5000): NA=0.55 (vs 0.33 for current EUV), first delivery 2024

HOW EUV WORKS:
  1. Tin (Sn) droplets fall at 70,000 drops/sec
  2. 1st CO₂ laser pulse shapes droplet into thin disk
  3. 2nd high-power CO₂ laser pulse vaporizes → Sn plasma at 500,000°C
  4. Plasma emits EUV photons at 13.5 nm
  5. Multilayer mirrors (Mo/Si, 40 layers) collect ~2% of photons
     (EUV absorbed by everything — no transmissive optics, all reflective)
  6. EUV bounces through reflective mask → 6 mirror reduction optics → wafer
  7. Resist captures pattern

EUV SOURCE POWER:
  EUV source power: 250+ W at wafer (NXE:3400C)
  600 W target for NXE:5000 (High-NA)
  CO₂ laser: 50-100 kW infrared input → 250 W EUV → huge energy waste
  A fab running 20 EUV tools consumes significant MW

REFLECTIVE MASK:
  EUV masks: quartz substrate + Mo/Si multilayer + absorber pattern
  Defect-free: a single buried multilayer defect ruins the mask
  Mask inspection: actinic (at-wavelength) inspection using ASML AIMS EUV
  Mask pellicle: polysilicon membrane to protect mask from particles
    (long delayed; now available but reduces source power)

EUV vs 193i+MPT TRADE-OFF:
  EUV single patterning: fewer masks, fewer process steps, better overlay
  EUV cost per wafer higher (tool $150-380M, low throughput, expensive masks)
  Break-even: typically >3-4 mask layers → EUV wins on total cost
  TSMC N7 (2018): first EUV in HVM, only a few non-critical layers
  TSMC N5 (2020): EUV for 14 layers; N3: ~20 EUV layers; N2: 25+ EUV layers

HIGH-NA EUV (NXE:5000):
  NA = 0.55 (current EUV: 0.33)
  Resolution: ~8 nm half-pitch (vs 13 nm current EUV single patterning)
  Problem: reduced depth of focus → requires ultra-flat wafers
  Problem: half-field exposure → must stitch fields (die size impact)
  Intel 14A target: first high-volume High-NA EUV user (~2026-2027)
```

---

## E-Beam Lithography

```
E-BEAM (ELECTRON BEAM) LITHOGRAPHY

PRINCIPLE:
  Focused electron beam writes directly on resist — no mask needed
  Resolution: sub-5 nm (electrons have much shorter de Broglie wavelength)
  No diffraction limit: wavelength λ = h/p ≈ 0.01-0.1 nm at typical energies

THROUGHPUT PROBLEM:
  Serial writing: one pixel at a time
  Throughput: ~0.1-1 wafer/hour (vs 275 wph for 193i scanner)
  → Not practical for high-volume production

E-BEAM USES:
  Mask making: all optical + EUV masks are written by e-beam (single write per mask)
  R&D/prototyping: academic, government, specialty chips where volume is tiny
  Multi-beam e-beam (MAPPER, IMS): 1000-10,000 parallel beams → 10 wph target
    Not yet HVM competitive, but ongoing development

VARIABLE SHAPED BEAM (VSB) vs GAUSSIAN BEAM:
  VSB: shapes beam to complex patterns → faster mask writing
  Gaussian: smallest spot, highest resolution, very slow
  Multi-beam: many parallel Gaussian beams → compromise

E-BEAM + EUV SYNERGY:
  E-beam inspection of EUV masks (HERMES, Nuflare tools)
  EUV mask pattern defined by e-beam writers → all leading-edge masks
```

---

## Resolution Enhancement Techniques (RET)

```
RESOLUTION ENHANCEMENT TECHNIQUES (RETs)

OPC (Optical Proximity Correction):
  Problem: optical diffraction distorts printed features from mask design
  Solution: pre-distort mask pattern computationally so printed result = design
  Modern OPC: inverse lithography technology (ILT) — pixel-by-pixel optimization
  Computation: $50-200M in EDA licenses per process node; weeks of CPU time

PSM (Phase Shift Mask):
  Standard binary mask: chrome opaque / quartz clear
  PSM: regions shifted 180° in phase → destructive interference sharpens edges
  Attenuated PSM (AttPSM): 6% transmission shifter layer (standard for ArF)
  Alternating PSM (AltPSM): highest resolution, most complex, expensive

SMO (Source-Mask Optimization):
  Co-optimize illumination shape + mask pattern simultaneously
  Flexible illumination (freeform pixelated source): ASML Flexray
  Result: optimal combination of source + mask for target pattern

Off-axis Illumination:
  Annular, dipole, quadrupole illumination → enhances contrast for specific pitches
  ASML: source pupil shapes optimized per layer

FULL-CHIP RET FLOW:
  Design (GDS) → OPC/SMO → Mask tape-out → Mask write (e-beam) → Etch/inspect
  → Qualification on silicon → Sign-off
  Cycle time: 6-12 weeks per mask layer for leading edge
```

---

## Decision Cheat Sheet

| Node / Use Case | Lithography Approach |
|-----------------|----------------------|
| 28 nm and above | 193 nm dry ArF or KrF (non-critical layers) |
| 16/14 nm FinFET | 193i immersion + SADP for critical layers |
| 10/7 nm | 193i + SADP/SAQP (many mask layers); first EUV at N7 |
| 5/4 nm | EUV dominant for critical layers (~12-14 layers) |
| 3/2 nm | EUV ~20-25+ layers; SAQP for tightest pitches |
| Below 2 nm (2027+) | High-NA EUV (NA=0.55) + EUV multi-patterning |
| Mask making | E-beam (VSB or multi-beam) always |
| Prototyping / R&D | E-beam direct-write |

---

## Common Confusion Points

**EUV doesn't eliminate multi-patterning at 2 nm**: EUV single-patterning handles some layers,
but the tightest metal pitches still require SAQP even with EUV. The benefit of EUV is fewer
total mask layers compared to 193i-only approaches.

**ASML's EUV monopoly isn't a business decision — it's physics**: EUV requires technology from
Carl Zeiss (optics), Trumpf (CO₂ laser), Cymer/ASML (source), and decades of multilayer mirror
development. No competitor has reproduced the full system. ASML spent >€6B developing EUV
and it took 20 years from concept to production.

**"k₁ = 0.25" is a hard physical limit**: Below k₁ = 0.25, the Abbe criterion says features
cannot be resolved regardless of resist or OPC tricks. This is why multi-patterning is necessary —
it effectively reduces pitch while keeping each individual exposure at k₁ ≥ 0.28.

**Photoresist chemistry is an industry in itself**: EUV resists are distinct from 193i CAR.
EUV photons have higher energy → can use metal-oxide resists (hafnium/zirconium oxide clusters)
which absorb EUV better than organic CAR. JSR/TOK/Inpria lead. Resist LER (line edge roughness)
is now a key limiter for sub-10 nm features.
