# Additive Manufacturing: FDM, SLA, DMLS

## The Big Picture

Additive manufacturing (AM) builds parts layer-by-layer from digital models. Process choice determines material class, resolution, anisotropy, porosity, cost, and lead time. The same CAD file can yield parts with vastly different properties depending on process.

```
ADDITIVE PROCESS LANDSCAPE
──────────────────────────────────────────────────────────────────────────
                    POLYMER                    METAL
                ────────────────           ────────────────────
                                           Powder Bed Fusion
 Material       Filament  Resin  Powder    (DMLS/SLM)  Binder Jet
 ───────────    ────────  ─────  ──────    ──────────  ──────────
 Process        FDM/FFF   SLA/   SLS/MJF   Layer by    Inkjet
                          DLP              layer laser  binder+sinter
 Resolution     Low       High   Med-High  High        Medium
 Strength       Low       Med    Med-High  Near-wrought Low-med
 Anisotropy     High      Med    Low       Low         Low
 Support        Yes       Yes    No        Yes (metal) No
 Build volume   Large     Med    Medium    Small-med   Large
 Cost           $         $$     $$$       $$$$        $$$
 Lead time      Hours     Hours  Hours     Days        Days
 Materials      PLA,ABS,  Most   Nylon,    Ti,Ni,SS,   Steel,
                PETG,etc  resins PA12,etc  Al,Co,etc   Cu,etc
```

---

## FDM / FFF (Fused Deposition Modeling / Fused Filament Fabrication)

### Process Physics

```
FDM PROCESS
──────────────────────────────────────────────────────────────────
Filament spool → heated nozzle (180–300°C) → melted material
→ extruded onto build platform (or previous layer)
→ cools and solidifies → next layer

           ┌─────────────────┐
           │  Filament Spool │
           └────────┬────────┘
                    │ (1.75mm or 2.85mm filament)
                    ▼
           ┌─────────────────┐
           │  Extruder/Motor │  (Bowden or direct drive)
           └────────┬────────┘
                    │
                    ▼
           ┌─────────────────┐
           │  Hot End        │  250°C melt zone
           │  0.4mm nozzle   │  (hardened for abrasive)
           └────────┬────────┘
                    │
                    ▼
                  Part  (layer by layer, bottom up)
```

### FDM Parameters and Their Effects

```
Layer height:
  0.3mm = fast, visible layers, weaker Z
  0.2mm = standard
  0.1mm = fine, slow, better Z strength
  0.05mm = very fine, slow (diminishing returns)

Infill:
  15–20% = light structure, prototype
  40–60% = functional parts
  80–100% = solid (heavy, slow, rarely needed)
  Patterns: gyroid (strongest/weight), rectilinear, honeycomb

Wall perimeters:
  2–3 = standard
  4–6 = structural
  More walls → stronger than more infill for most loading

Print temperature:
  Too low → poor layer adhesion, delamination
  Too high → stringing, oozing, dimensional inaccuracy

Bed temperature:
  ABS requires 100–110°C bed (warping prevention)
  PLA works 60°C
  PETG 70–80°C
```

### FDM Material Properties

| Material | Temp (°C nozzle) | Strength | Heat Resistance | Notes |
|----------|-----------------|----------|-----------------|-------|
| PLA | 190–220 | Low | Poor (60°C) | Biodegradable, easy to print |
| PETG | 230–245 | Med | Med (80°C) | Food safe, tougher than PLA |
| ABS | 230–250 | Med | Good (100°C) | Warps without enclosure |
| ASA | 240–260 | Med | Good (100°C) | UV resistant, outdoor |
| TPU | 220–240 | — | Med | Flexible, Shore A 85–95 |
| Nylon PA12 | 250–270 | High | Good (120°C) | Hygroscopic, tough |
| PC | 260–300 | High | Excellent (130°C) | Transparent possible |
| ULTEM 9085 | 380°C | Very High | Excellent (170°C) | FAA aircraft interiors |
| CF-PA/PEI | 260–380 | Very High | Excellent | Short fiber reinforced |

### FDM Anisotropy

```
FDM parts are WEAKEST in Z (layer separation direction):

  XY plane strength:     ~100%
  Z direction strength:  ~30–60% (layer adhesion limited)

  Solution strategies:
    - Orient part so critical stress is in XY
    - Increase perimeters/walls for Z-loaded features
    - Increase overlap between layers
    - Continuous fiber (Markforged) for structural Z strength
```

---

## SLA / DLP (Stereolithography / Digital Light Processing)

### Process Physics

```
SLA PROCESS                          DLP PROCESS
────────────────────────────────     ────────────────────────────────
Laser scans each layer point         UV projector flashes entire
by point (vector scan)               layer at once (raster)

  UV laser → galvanometer             UV projector (DMD chip)
  mirrors → resin surface             → resin surface via mirror
  → polymerize → elevator             → polymerize entire layer
  moves up/down                       → elevator moves

Speed: slower (point scan)           Speed: faster (flash each layer)
Resolution: excellent (spot size)    Resolution: projector pixel size
Best for: large fine-detail parts    Best for: high throughput, jewelry
```

### Resin Types

| Resin Class | Properties | Applications |
|-------------|-----------|--------------|
| Standard | Brittle, fine detail | Visual prototypes |
| Tough | ABS-like, impact resistant | Functional prototypes |
| Flexible | Rubber-like | Seals, gaskets |
| Castable | Burns out cleanly | Jewelry, dental |
| Dental | Biocompatible | Clear aligners, surgical guides |
| High-temp | HDT >200°C | Under-hood, tooling |
| Ceramic-filled | Very stiff, hard | Jigs, fixtures |

### SLA Limitations

```
Post-processing required:
  1. Wash in IPA (isopropyl alcohol) to remove uncured resin
  2. UV cure in post-cure station (full depth cure)
  3. Support removal (visible marks left)
  4. Optional sanding/painting

Limitations:
  - Photopolymers are brittle vs engineering thermoplastics
  - UV degradation over time (yellowing, embrittlement)
  - Layer delamination under sustained load
  - Resin waste (support material, failed prints)
  - Odor, skin irritation (uncured resin is irritant)
```

---

## SLS / MJF (Selective Laser Sintering / Multi Jet Fusion)

### SLS Process

```
SLS PROCESS
──────────────────────────────────────────────────────────────────
1. Powder spreader deposits thin layer (~0.1mm) of PA12 nylon
2. CO₂ laser scans cross-section → sinters (fuses) particles
3. Build piston lowers, new layer deposited
4. Repeat until complete
5. Cool down (critical — rapid cooling = warpage)
6. Excavate from powder cake
7. Media blast to remove loose powder

NO SUPPORTS NEEDED: unsintered powder supports the part
→ complex geometry without support removal
→ multiple parts stacked vertically (nest packing)

PA12 nylon typical properties:
  Tensile strength: 48 MPa (XY) / 42 MPa (Z)
  Elongation: 20% (XY) / 10% (Z)
  HDT: 170°C
  Much less anisotropic than FDM
```

### MJF (HP Multi Jet Fusion)

HP's inkjet-based powder process. More uniform than SLS (full-layer ink deposit instead of point-scan). Better dimensional accuracy, smoother surfaces. Standard material: PA12. Introduces colorants into the powder bed for colored parts. Higher production throughput.

---

## DMLS / SLM (Metal Powder Bed Fusion)

### Process Physics

```
DMLS (Direct Metal Laser Sintering) / SLM (Selective Laser Melting)
──────────────────────────────────────────────────────────────────
Same conceptual flow as SLS but:
  - Metal powder (10–45 µm particle size)
  - High-power fiber laser (200W–1000W, multiple lasers)
  - Fully melted (SLM) not just sintered (DMLS)
  - Inert atmosphere (argon or nitrogen — prevents oxidation)
  - Layers 20–60 µm thick
  - Build platform temperature elevated (Ti6Al4V: 200°C)

Result: dense metal part (99.5–99.9% density typical)
Near-wrought mechanical properties for Ti, Ni, SS
```

### Materials and Properties

| Material | Typical Application | Notes |
|----------|---------------------|-------|
| Ti-6Al-4V | Aerospace, medical implants | Near-wrought after HIP |
| AlSi10Mg | Lightweight structures | Porosity risk, post-HT |
| Inconel 625/718 | Hot section aerospace, turbines | Difficult to machine |
| 316L Stainless | Medical, food, chemical | Corrosion-resistant |
| 17-4 PH SS | General structural, tooling | Age-hardenable |
| Maraging Steel M300 | Tool inserts with conformal cooling | Machinable after AM |
| CoCrMo | Dental, orthopaedic implants | Biocompatible |
| Copper | Heat exchangers, induction coils | High thermal conductivity |

### DMLS Support Structures

```
Metal support structures are required because:
  1. Overhanging geometry needs support (>45° typically)
  2. Thermal management — supports conduct heat from part
  3. Anchors part to build plate (prevents distortion)

Support types:
  Block supports → easy to remove, poor surface quality
  Lattice supports → better heat transfer, harder to remove
  Cone/tree → minimal contact, easier removal, common for Ti

POST-PROCESSING IS MANDATORY for DMLS:
  1. Stress relief anneal (while on build plate)
  2. Wire EDM to remove from build plate
  3. Support removal (manual or EDM)
  4. HIP (Hot Isostatic Pressing) → closes subsurface pores → best for aerospace
  5. Machining of critical surfaces (near-net only)
  6. Heat treatment (age hardening for 17-4, Ti-64, Inconel)
  7. Surface finishing (bead blast, shot peen, polish if needed)
```

### DMLS Design Rules

```
DESIGN FOR ADDITIVE (DfAM):
  - Minimum feature size: ~0.3mm for walls/pins
  - Overhangs > 45° from horizontal → need support
  - Self-supporting internal channels: prefer circular/teardrop cross-sections
  - Hollow structures (lightweighting): design with powder escape holes
  - Conformal cooling: sinuous channels possible inside mold tooling
  - Lattice structures: replace solid with open-cell lattice for weight
  - Topology optimization: FEA-driven organic geometry → often only via AM

Build orientation matters:
  - Part properties are slightly anisotropic (Z weaker ≈5–10%)
  - Critical surfaces should be oriented to minimize stairstepping
  - Minimize support contact on functional surfaces
  - Long parts may require tilting to fit build volume
```

---

## Binder Jetting (Metal)

```
BINDER JET PROCESS (ExOne, Desktop Metal, HP Metal Jet)
──────────────────────────────────────────────────────────────────
1. Powder layer spread (fine metal powder, 15–45 µm)
2. Inkjet head deposits binder (glue) at part cross-section
3. Repeat layers
4. "Green part" — binder holds powder together
5. Cure in oven (harden binder)
6. Remove from powder cake
7. Sinter in furnace → burn out binder, fuse metal particles
8. Part shrinks ~20% during sintering (predictable → CAD compensates)

Result: 97–99% density (vs 99.5%+ for SLM)
Larger build volumes than SLM
More brittle than SLM (less dense)
Lower mechanical properties
But: faster, cheaper, no support removal, scale-able

Materials: 316L, 17-4 PH, copper, tungsten
Applications: high volume, complex small metal parts
```

---

## DED (Directed Energy Deposition)

```
DED / LENS (Laser Engineered Net Shaping)
──────────────────────────────────────────────────────────────────
Laser or electron beam creates melt pool on existing surface.
Powder or wire is fed into melt pool.
Used for: large structures, repair, cladding, hybrid machining

Variants:
  LMD  (Laser Metal Deposition)  → aerospace repair, cladding
  WAAM (Wire Arc Additive)       → large Ti, steel structures, ships
  EBW  (Electron Beam Wire)      → large Ti aerospace (Sciaky)

Build volume: can be meters (unlike SLM which is ~400mm cube)
Resolution: poor (±1mm layer height for WAAM)
Post-machining: always required for dimensional accuracy
Properties: good — near-wrought possible with proper parameters
```

---

## Comparing AM Processes for Metal

| | DMLS/SLM | Binder Jet | DED/WAAM |
|--|---------|-----------|---------|
| Density | 99.5%+ | 97–99% | 99%+ |
| Resolution | 0.1mm | 0.3mm | 1–3mm |
| Build volume | 400mm cube | 800mm+ | Meters |
| Speed | Slow | Fast | Fast |
| Support needed | Yes | No | No |
| Post-process | Extensive | Sinter+machine | Machine |
| Properties | Near-wrought | Good | Near-wrought |
| Best for | Complex, small | High volume | Large, repair |

---

## Decision Cheat Sheet

| Need | Process |
|------|---------|
| Fast visual prototype | FDM (PLA, 0.2mm layers) |
| Accurate concept model with fine detail | SLA/DLP |
| Functional polymer prototype (no supports, complex) | SLS/MJF |
| High-temp polymer prototype | FDM ULTEM or SLS high-temp nylon |
| Metal prototype, no tooling | DMLS/SLM |
| Flight-qualified metal bracket (Ti, Ni) | DMLS/SLM + HIP + machine |
| High-volume small metal parts | Binder Jetting |
| Very large metal structure | DED/WAAM |
| Mold insert with conformal cooling | DMLS (maraging steel M300) |
| Flexible parts (grips, seals) | FDM (TPU) or SLA (flexible resin) |

---

## Common Confusion Points

**DMLS vs SLM**: Marketing terms for essentially the same process (laser powder bed fusion). DMLS (EOS trademark) = originally sintering. SLM (Realizer/SLM Solutions) = full melt. Modern DMLS also fully melts. In practice: same process, different vendor names.

**FDM anisotropy in Z**: Layers bond via re-melting of the previous layer surface. The bond strength is never equal to bulk material strength. A part pulled apart between layers (Z tension) is 30–50% weaker than the same load in XY. This is fundamental, not a tuning issue.

**Support removal scars on DMLS**: Metal supports leave surface marks. Design around this: orient support contact faces away from functional surfaces, use EDM or machining post-process for those surfaces.

**SLS powder reuse**: Unsintered SLS powder can be partially recycled (typically 50:50 virgin:used), but aged powder degrades part properties. Binder jet powder is more reusable. SLM/DMLS powder is more expensive and recycling protocols are tighter.

**HIP (Hot Isostatic Pressing)**: HIP at ~900°C and 100 MPa argon pressure closes internal voids via plastic deformation. For flight-critical DMLS Ti-6Al-4V, HIP is mandatory — it takes density from 99.5% to 99.9%+ and dramatically improves fatigue life.
