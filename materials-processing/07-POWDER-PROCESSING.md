# Powder Processing and Sintering

## The Big Picture

Powder processing builds dense solid parts from powder feedstock. It is the dominant manufacturing route for cemented carbide cutting tools, PM steels, and advanced ceramics — materials that cannot be economically cast or machined to final shape. The key physics: sintering drives densification by reducing surface energy.

```
POWDER PROCESSING ROUTES
──────────────────────────────────────────────────────────────────
POWDER PRODUCTION → POWDER CONDITIONING → SHAPING → DENSIFICATION → FINISHING

Powder production:
  Atomization (liquid metal): water, gas, or centrifugal
  Chemical reduction (oxides → metal powder): Fe, W, Mo
  Mechanical comminution: brittle materials (ceramics)
  Electrolytic: Cu, Fe (dendritic/flaky powders)
  Carbonyl decomposition: Ni, Fe (very fine, pure)

Powder conditioning:
  Screening (size classification)
  Blending (mix powders + lubricants)
  Annealing (reduce work hardening from atomization)

Shaping methods:
  Uniaxial pressing: die compaction (most common PM parts)
  Cold Isostatic Pressing (CIP): flexible membrane, hydrostatic
  Injection Molding (MIM): binder + powder mix
  Tape casting: thin sheets (electronic substrates)
  Slip casting: ceramics in plaster molds
  Extrusion: binder-assisted extrusion

Densification:
  Sintering (solid-state or liquid-phase): furnace process
  Hot Pressing (HP): simultaneous pressure + heat
  HIP (Hot Isostatic Pressing): gas pressure + heat
  SPS (Spark Plasma Sintering): pulsed DC current + pressure

Finishing:
  Machining (limited — hardness of many PM parts)
  Infiltration (fill residual pores)
  Surface treatment
```

---

## Sintering Theory

### Driving Force and Mechanisms

```
SINTERING DRIVING FORCE
──────────────────────────────────────────────────────────────────
Driving force: reduction in total surface energy
  Powder has enormous surface area → high surface energy
  Sintering reduces surface area → energy released

Surface energy of a sphere radius r:
  E_surface = 4πr² × γ
  Larger surface area = more energy = driving force to sinter

Sintering mechanisms (contribute in parallel):
  ┌──────────────────────────────────────────────────────────────┐
  │ SURFACE DIFFUSION:    Atoms move on surface, fill neck       │
  │                       → Neck grows, no densification         │
  │                                                              │
  │ VOLUME DIFFUSION:     Atoms diffuse through bulk, fill neck  │
  │                       → Densification (pores shrink)         │
  │                                                              │
  │ GRAIN BOUNDARY DIFF:  Atoms move along GB, most important    │
  │                       for densification in metals            │
  │                                                              │
  │ VISCOUS FLOW:         Glass/amorphous → flow fills pores     │
  │                       Important for: glass sintering         │
  └──────────────────────────────────────────────────────────────┘

Neck growth equation (early stage, surface diffusion dominates):
  (X/D)⁷ = (56 Ds δs γ Ω) / (kT) × (t/D⁴)
  X = neck radius, D = particle diameter, Ds = surface diffusivity
  Linear: densification only from volume or grain boundary diffusion
```

### Sintering Stages

**Percolation bridge:** The sintering stages represent a connectivity phase transition. Stage 2 has an open, connected pore network (percolating — gas can penetrate). Stage 3 has isolated closed pores (network disconnected, percolation threshold crossed). The Stage 2 → Stage 3 transition is a topological change: the pore network goes from connected to disconnected. This matters practically because atmosphere-controlled sintering (carburizing, deoxidizing) only works while pores are open (Stage 2). Once pores close (Stage 3), gas cannot reach interior porosity.

```
THREE STAGES OF SINTERING
──────────────────────────────────────────────────────────────────
STAGE 1 (Neck formation, initial): Density ~60–70% → ~70–80%
  Rapid neck growth between adjacent powder particles
  Contact areas grow (neck radius X/D ≈ 0 to 0.4)
  Little shrinkage, most dimensional change comes later
  Surface area decreases rapidly

STAGE 2 (Pore rounding, intermediate): ~70–80% → ~92–95%
  Pores become interconnected but cylindrical tubes
  Pores shrink, grain growth begins
  Significant densification and shrinkage
  Pore channels remain open → can gas-debind during this stage

STAGE 3 (Pore elimination, final): ~92–95% → 99%+
  Isolated closed pores
  Slow densification (pores must be eliminated against grain boundaries)
  Grain growth accelerates (fewer pores to pin boundaries)
  Oversintering (excessively high T or long t): grain coarsening → weaker

Sintering map: plots temperature, density, mechanism dominance
  Enables process optimization for specific material
```

---

## Conventional PM (Die Pressing + Sintering)

```
CONVENTIONAL PM PROCESS
──────────────────────────────────────────────────────────────────
1. POWDER PREPARATION
   Powder + lubricant (zinc stearate) → blend
   Lubricant: reduces die friction, aids green compact ejection

2. PRESSING (Compaction)
   Die: rigid tooling (WC, tool steel)
   Press: mechanical, hydraulic, or servo
   Typical pressures: 150–800 MPa (varies by material, density target)

   Pressure effects:
     Higher pressure → higher green density → easier sintering
     But: elastic springback → dimensional change on ejection
     Upper limit: tooling fracture, die wear

3. GREEN COMPACT
   Parts have enough strength to handle, transfer to furnace
   Green strength: from mechanical interlocking + small diffusion bonds
   ~5–20 MPa (weak by any standard)
   Handles: carefully (green parts are fragile)

4. SINTERING FURNACE
   Three zones:
     Burn-off zone: lubricant evaporates/burns at 200–500°C
     Sintering zone: 1000–1300°C (steel), 1400°C+ (ceramics/WC)
     Cooling zone: controlled rate (prevent distortion, residual stress)

5. FINAL PM PART
   Density: 90–96% theoretical (with standard PM)
   Residual porosity: 4–10% (interconnected at low density, closed at high)
   Properties: adequate for structural PM parts
   Applications: gears, bearings, connecting rods (automotive)

PM vs forging for same steel part:
  PM: near-net shape, lower cost at high volume, slightly lower properties
  Forging: better mechanical properties, higher cost, more material waste
  PM + forge (sinter-forge): near-net shape + forged properties
```

---

## MIM (Metal Injection Molding)

**Compilation pipeline bridge:** MIM is a multi-stage transformation pipeline: feedstock (all information present, unoptimized) → green part (structure formed but binder scaffolding still in place, like an AST) → brown part (binder removed, retained by powder skeleton, like a linked object) → sintered part (densified, final properties, like an optimized binary). Each stage is irreversible and removes scaffolding while consolidating structure. The predictable 15-20% linear shrinkage is compensated in the mold design — analogous to compile-time relocation.

```
MIM PROCESS
──────────────────────────────────────────────────────────────────
Purpose: Net-shape complex metal parts with injection mold process.
Bridges injection molding (geometry freedom) + PM (metal properties).

1. FEEDSTOCK PREPARATION
   Fine metal powder (5–15 µm) + binder (40–50 vol% binder)
   Binders: thermoplastic (paraffin + polyethylene) or
            water-soluble (PEG + water)
   Mix at elevated temperature → homogeneous "feedstock"
   Pelletize for injection molding machine

2. INJECTION MOLDING
   Standard injection mold machine, standard tooling design
   Gate placement critical (no regrind for most MIM)
   "Green part" = metal powder in binder matrix
   Dimensions: ~20% larger than final (must account for shrinkage)

3. DEBINDING (binder removal)
   Thermal (two-stage): burn out paraffin first, then backbone polymer
   Solvent: solvent removes first binder, retain backbone polymer
   Catalytic: nitric acid depolymerizes backbone binder
   "Brown part" = skeleton structure of powder (3% interconnected pores)

4. SINTERING
   950–1350°C in H₂ or N₂ atmosphere
   High shrinkage (15–20% linear) → predictable → mold compensated
   Density: 95–99% theoretical

MIM materials: SS 316L, 17-4 PH, Fe-Ni, Ti-6Al-4V, WC-Co, ceramics
MIM applications: firearms components, dental implants, watch parts,
  surgical instruments, laptop hinges — complex 3D geometry, high volume

vs DMLS (metal AM):
  MIM: high volume, lower cost per part, no porosity issues
  DMLS: low volume, no tooling, arbitrary geometry
```

---

## HIP (Hot Isostatic Pressing)

```
HIP PROCESS
──────────────────────────────────────────────────────────────────
Simultaneous application of:
  High temperature: 950–1300°C (material-dependent)
  High gas pressure: 100–200 MPa (argon gas, isostatic)

Result: closes all pores (closed or open if encapsulated)
→ near-theoretical density (99.5–99.9%)

Applications:

1. POST-PROCESS HIP (for cast or PM parts):
   Close residual porosity after conventional casting or PM sintering
   Ti-6Al-4V castings: HIP at 900°C, 100 MPa → fatigue life doubles
   DMLS/SLM metal AM: HIP closes sub-surface pores → flight-qualified
   Cemented carbide: HIP at final stage → highest density, best performance

2. POWDER HIP (near-net shape):
   Load powder into metal can (container)
   Evacuate, seal, HIP → fully dense near-net shape part
   No intermediate compaction required
   Excellent properties: HIPed powder is equivalent to wrought
   Applications: tool steels (PM-T15, CPM grades), Ni superalloy billets
   Large parts: turbine discs, extrusion dies

3. DIFFUSION BONDING via HIP:
   Multi-material assemblies sintered together
   Metal-ceramic composites, claddings

HIP limitations:
  Slow: 4–24 hour cycle
  Expensive: capital-intensive equipment, inert gas cost
  Closed pores only: open surface pores require encapsulation first
  Cannot close all crack-like defects (requires intimate contact between surfaces)
```

---

## SPS (Spark Plasma Sintering) / FAST

```
SPARK PLASMA SINTERING (FIELD-ASSISTED SINTERING, FAST)
──────────────────────────────────────────────────────────────────
Pulsed DC current + uniaxial pressure, very fast heating
  Current: pulsed DC (often attributed to "sparks" but mechanism debated)
  Heating rate: 100–1000°C/min (vs 5–20°C/min for conventional)
  Pressure: 50–100 MPa
  Cycle time: minutes (vs hours for conventional sintering)

Mechanism debate:
  Originally claimed: sparks at particle contacts → local melting → rapid bonding
  More accepted: Joule heating + current-enhanced diffusion
  Electrically conductive powders: direct Joule heating
  Non-conductive (ceramics): heated by graphite die

Advantages:
  Rapid: 2–10 minutes soak time → grain growth suppressed
  Fine microstructures: difficult to achieve with conventional sintering
  Novel materials: metastable phases, gradient compositions
  High final density without exaggerated grain growth

Applications:
  Nano-grained ceramics (Al₂O₃, SiC, WC) → fine grain → high toughness
  Functionally graded materials (composition gradient)
  Research/development (small batch sizes)
  Refractory materials: TiB₂, HfC, TaC → rapid sintering

Limitations:
  Lab/pilot scale (typically <200mm diameter specimens)
  Graphite die → carbon contamination possible for reactive materials
  No complex geometry (like HIP can do)
```

---

## Cemented Carbide (WC-Co)

```
CEMENTED CARBIDE (HARDMETAL)
──────────────────────────────────────────────────────────────────
The premier PM hard material: WC (ceramic) bonded by Co (metal binder)
Foundation of modern metal cutting tooling

POWDER PREPARATION:
  WC powder (0.5–10 µm particle size) + Co powder
  Ball milled with ethanol (intimate mixing, breakup agglomerates)
  Spray dried → free-flowing granules for pressing

PRESSING:
  Die press or CIP to near-net shape
  High pressure: 150–400 MPa

LIQUID-PHASE SINTERING:
  Sintering at 1370–1450°C (above Co melting, Co liquid at 1495°C in WC-Co)
  Co melts, wets WC → liquid phase sintering → fast densification
  WC grains dissolve in Co, reprecipitate → grain rounding, bonding
  Final density: 99.9%+

STRUCTURE:
  WC grains (hard, brittle): 1200–1600 HV
  Co binder (tough, ductile): holds WC together
  Interlocked WC + Co → "cemented" carbide

GRADING:
  Coarser WC + higher Co → tougher, better for interrupted cuts (milling)
  Finer WC + lower Co → harder, more wear resistant (fine turning)

  WC grain size:   0.5–10 µm (coarse → fine: submicron grades)
  Co content:      3–25% (3% = wear-resistant, 25% = toughest, mining)

APPLICATIONS:
  Cutting tool inserts (majority): turning, milling, drilling
  Rock drilling bits
  Wire drawing dies
  Metal forming dies (cold heading, stamping)
```

---

## Ceramics Processing

```
CERAMIC POWDER PROCESSING
──────────────────────────────────────────────────────────────────
Ceramics cannot be processed like metals:
  No ductility → cannot plastically deform into shape
  High melting points → casting impractical for most
  Hard → machining very limited/expensive
  Solution: start as powder, sinter to shape

Common structural ceramics:
  Alumina (Al₂O₃): hardness 2000 HV, inert, insulating
  Silicon carbide (SiC): hardness 2500 HV, thermal shock resistant
  Silicon nitride (Si₃N₄): toughest structural ceramic, bearing balls
  Zirconia (ZrO₂): toughened by transformation plasticity
  WC (cemented carbide as above)

Densification challenge:
  Ceramics diffuse much slower than metals → need higher T, longer time
  Or: liquid phase sintering additives (Si₃N₄ → MgO or Y₂O₃ + Al₂O₃)

Sintering conditions:
  Al₂O₃: 1500–1700°C, 2–4 hours
  SiC: 2000–2100°C or hot pressing
  Si₃N₄: 1700–1800°C with liquid phase additives
  ZrO₂ (TZP): 1400–1500°C

Transformation-toughened zirconia (TTZ):
  ZrO₂ tetragonal → monoclinic transformation (phase change on stress)
  Volume expansion at crack tip → compressive stress → crack arrest
  Kic up to 8–12 MPa√m (vs ~3–4 for untoughened ZrO₂)
  Applications: dental crowns (high aesthetic + strength), cutting inserts
```

---

## Decision Cheat Sheet

| PM/Sintering Need | Process |
|------------------|---------|
| High-volume automotive PM gears/bearings | Conventional die pressing + sintering |
| Complex 3D geometry metal part (medium to high volume) | MIM |
| Maximum density for DMLS aerospace parts | Post-process HIP |
| Near-net shape from difficult-to-machine alloy (tool steel, superalloy) | Powder HIP |
| Cemented carbide tool insert | WC-Co liquid phase sintering |
| Nano-grained ceramic, minimum grain growth | SPS/FAST |
| Structural ceramic component | Die press + sinter (+ HIP for max density) |
| Repair/densify cast Ti aerospace part | HIP at 900°C/100 MPa |

---

## Common Confusion Points

**PM density vs theoretical density**: Wrought steel = 100% of theoretical. Cast steel = ~99%. Conventional PM = 92–96%. MIM = 96–99%. HIPed PM = 99.9%. Properties scale with density — a 4% porosity PM part can have 20–30% lower fatigue strength than wrought equivalent. Specify density (or HIP requirement) for fatigue-loaded PM parts.

**Liquid-phase sintering ≠ partial melting**: In liquid-phase sintering (WC-Co, Fe with Cu addition), a BINDER phase melts while the structural phase (WC, Fe) remains solid. The liquid wets the solid grains, fills pores, and provides capillary driving force for densification. The structural phase never melts. This is fundamentally different from "sintering liquid metal."

**MIM cannot sinter open porosity**: After debinding, a MIM brown part has ~40% binder-derived porosity. This porosity is interconnected (open), so sintering atmosphere can reach all surfaces. If you seal the surface before sintering is complete (too fast ramp), you trap closed pores that won't fully densify. MIM sintering profiles are carefully controlled to allow gradual pore closure.

**SPS "spark" mechanism is disputed**: The original name implied localized sparking at particle contacts that caused local melting. The majority of current research suggests this is not the mechanism — instead, DC current enhances diffusion and provides very rapid Joule heating. The name "Field-Assisted Sintering Technique (FAST)" or "Flash Sintering" is preferred for accuracy.

**Grain growth in ceramics is bad for toughness**: Fine grains in toughened ceramics (Si₃N₄, ZrO₂) are REQUIRED for toughness mechanisms (crack bridging, transformation toughening). Excessive sintering temperature or time → grain growth → loss of toughening mechanism. This is why SPS is valuable for ceramics — rapid cycle suppresses grain growth.
