# Polymer Processing: Extrusion, Molding

## The Big Picture

Polymer processing converts raw polymer resin (pellets, powder, or preforms) into shaped parts by exploiting the viscous flow behavior of melted thermoplastics or the crosslinking chemistry of thermosets. The physics is fundamentally different from metal processing: polymers are viscoelastic fluids — they have both viscous (flow) and elastic (spring-back) character simultaneously, and their viscosity drops dramatically with temperature and shear rate.

```
POLYMER PROCESSING LANDSCAPE
──────────────────────────────────────────────────────────────────
FEEDSTOCK TYPE → PROCESS FAMILY → OUTPUT FORM

THERMOPLASTICS (melt, shape, solidify — repeatable):
  Pellets/granules → Extrusion        → Profile, sheet, film, pipe, wire coat
  Pellets          → Injection Molding → Discrete 3D parts
  Sheet            → Thermoforming    → Cups, blister packs, panels
  Preform          → Blow Molding     → Bottles, containers
  Pellets/powder   → Rotomolding     → Large hollow parts (tanks, kayaks)

THERMOSETS (liquid, cure — irreversible crosslink):
  Liquid resin     → RTM/VARTM       → Fiber composite panels
  Prepreg (tape)   → Autoclave cure  → Aerospace CFRP structure
  Liquid           → Transfer molding → Encapsulated electronics

ELASTOMERS (vulcanize — crosslink with sulfur):
  Compound         → Compression molding → Seals, tires
  Compound         → Injection molding   → High-volume rubber parts

PROCESSING PARAMETERS THAT MATTER:
  Melt temperature  → viscosity, degradation limit
  Shear rate        → thinning (pseudoplastic behavior)
  Cooling rate      → crystallinity, residual stress, warpage
  Pressure          → fill, packing, density
  Time              → cycle time (economics), crystallization, cure
```

---

## Polymer Melt Rheology (Why It Matters)

```
RHEOLOGY FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Viscosity η: resistance to flow (Pa·s)

Newtonian fluid (water, mineral oil):
  η = constant (independent of shear rate)

Polymer melt — Non-Newtonian pseudoplastic (shear-thinning):
  η decreases as shear rate increases
  Power law model: η = K × γ̇^(n-1)
    n < 1: shear-thinning (all common polymers)
    K = consistency index (material constant)
    γ̇ = shear rate (1/s)
  Systems bridge: shear-thinning is a nonlinear system where increased
  throughput (shear rate) reduces resistance (viscosity) — positive
  feedback on flow rate. Unlike most congestion models where resistance
  increases with throughput, polymer flow gets easier at higher rates.
  The Arrhenius temperature dependence (viscosity halves per 10°C) adds
  exponential thermal sensitivity to the nonlinearity.

  Typical viscosity:
    At rest (zero shear): η ≈ 10³–10⁵ Pa·s (10³–10⁵× water)
    At injection molding shear rates (10³–10⁴ s⁻¹): η ≈ 10²–10³ Pa·s

  Practical consequence: HIGH shear rate in runner/gate → lower viscosity
    → helps fill thin sections; back off shear to avoid degradation

Temperature dependence — Arrhenius-like:
  η ∝ exp(Ea/RT)  (Ea = activation energy, T in Kelvin)
  → Every 10°C rise: viscosity drops ~factor of 2 for typical polymers
  → Processing window: above Tg (glass transition) or Tm (melting point)
    but below Tdeg (degradation temperature)

VISCOELASTICITY:
  Polymers store and release elastic energy during flow
  Die swell (extrudate swell): melt expands on exiting die (elastic recovery)
    → Die must be compensated to achieve desired final dimension
  Melt fracture: above critical shear rate → sharkskin or gross melt fracture
    → Surface defect, glossy → rough transition
```

---

## Extrusion

### The Extrusion Process

```
SINGLE-SCREW EXTRUDER ANATOMY
──────────────────────────────────────────────────────────────────
             Hopper
               │
               ▼
  ┌─────────────────────────────────────────────────┐
  │  Feed zone  │  Compression zone  │  Metering zone│→ Die
  │  (deep       │  (decreasing       │  (shallow,    │
  │   channels)  │   channel depth)   │   pumping)    │
  └─────────────────────────────────────────────────┘
       Barrel heaters (multiple zones)
       Screw (L/D ratio: 20:1 to 30:1)

ZONES:
  Feed:        Pellets enter, convey solid material
  Compression: Channels shallow → compresses, melts by shear heat + conduction
  Metering:    Melt pumped at constant rate to die

SCREW PARAMETERS:
  L/D ratio:        length/diameter, typical 24:1 – 32:1
  Compression ratio: feed channel depth / metering channel depth (~3:1)
  RPM:              shear rate, output rate, melt temperature
  Back pressure:    pressure on returning material → better mixing, higher melt T

DIE:
  Profile die:   shapes melt into desired cross-section
  Die swell:     melt expands 5–20% beyond die opening
  Die design:    land length, taper angle, must account for swell
  Calibration:   downstream cooling fixture holds final dimension

DOWNSTREAM:
  Cooling tank (water) → Puller → Cutter or winder
  Puller speed vs screw RPM ratio → sets wall thickness by drawing
```

### Extrusion Outputs

```
EXTRUSION PRODUCT FORMS
──────────────────────────────────────────────────────────────────
PROFILE:    Custom cross-section → window frames (PVC), structural channels
            Die profile ≠ final profile (swell + drawdown must be modeled)

PIPE/TUBE:  Annular die with mandrel
            Cooling: water tank immediately after die
            Common polymers: PVC, HDPE, CPVC, PP
            Standard: ASTM D1785 (PVC), ASTM F714 (HDPE)

SHEET/FILM: Flat die (coat-hanger manifold) → uniform melt width
            Sheet (>0.25mm): 3-roll calender stack → surface finish
            Film (<0.25mm): blown film (tubular die → inflated bubble) or cast film
            Biaxial orientation in blown film → improved tensile + barrier

WIRE COATING: Wire pulled through annular crosshead die
              Melt coats wire → cooling trough
              Materials: PVC (general wiring), XLPE (high temp), PTFE (ultra high temp)
              Speed: 100–1000 m/min

TWIN-SCREW EXTRUDER:
  Intermeshing co-rotating screws → much better mixing than single-screw
  Used for: compounding (adding fillers, colorants, reinforcing fibers)
            reactive extrusion (chain extension, grafting reactions)
  Not primarily for profile production — for material preparation
```

---

## Injection Molding

### Process Overview

The injection molding cycle is a deterministic synchronous state machine: five states (clamp → inject → pack → cool → eject) with guarded transitions (clamp force reached → inject; gate freeze → pack; ejection temperature reached → eject). Every part traverses the same sequence with the same state invariants.

```
INJECTION MOLDING CYCLE
──────────────────────────────────────────────────────────────────
CYCLE PHASES (sequential):
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. CLAMPING: mold halves close → clamp force applied        │
  │                                                             │
  │ 2. INJECTION: screw advances → melt injected into cavity   │
  │    Gate freezes → end of injection phase                    │
  │                                                             │
  │ 3. PACKING/HOLDING: extra melt pushed in to compensate      │
  │    shrinkage → gate seal → pressure holds                   │
  │                                                             │
  │ 4. COOLING: part cools below ejection temperature           │
  │    Screw recovers (rotates, feeds next shot while cooling)  │
  │                                                             │
  │ 5. EJECTION: mold opens → ejector pins push part out       │
  └─────────────────────────────────────────────────────────────┘

CYCLE TIME BREAKDOWN (typical):
  Injection: 0.5–3 s  (fast fill = good part quality)
  Packing:   2–10 s
  Cooling:   5–60 s   (DOMINANT — part must solidify below ejection T)
  Open/eject/close: 1–5 s
  Total: ~10–100 s depending on wall thickness

Cooling dominates: reducing wall thickness by 25% → halves cooling time
→ Most important DfM decision: minimize wall thickness (uniform)
```

### Mold Design

```
INJECTION MOLD ANATOMY
──────────────────────────────────────────────────────────────────
                      Sprue bushing
                           │
            ┌──────────────┼──────────────┐
            │  Runner system (cold or hot)│
            │        │         │          │
            │       Gate     Gate         │
            │        ↓         ↓          │
            │   [Cavity 1] [Cavity 2]     │
            │                             │
            │  Cooling channels (water)   │
            │  Ejector pins              │
            └─────────────────────────────┘
              Fixed half    Moving half

RUNNER SYSTEMS:
  Cold runner: runner solidifies with part → must be ground/remelted (waste)
    Simpler, lower tooling cost
  Hot runner: heated manifold keeps runner molten → no runner waste
    Higher tooling cost (~$5,000–50,000 for manifold), eliminates regrind
    Standard for high-volume production

GATE TYPES:
  Edge gate:  simple, visible gate vestige, easy to change
  Submarine gate: auto-degates on ejection
  Pin gate:   small, round, minimal vestige
  Valve gate (hot runner): pneumatic/hydraulic pin → precise control, no vestige
  Fan gate:   wide thin gate → low stress for large flat parts

COOLING:
  Conformal cooling channels (AM-made molds): follow part contour
  → 30–50% cycle time reduction possible
  Baffles/bubblers for cores that can't have straight channels
  Temperature uniformity → warpage reduction

DRAFT ANGLES:
  Minimum: 1° per side for smooth surfaces
  Textured surfaces: 1–3° extra per 0.025mm texture depth
  No draft → part sticks in mold, ejection damage
```

### Injection Molding Defects

```
INJECTION MOLDING DEFECTS AND CAUSES
──────────────────────────────────────────────────────────────────
SHORT SHOT (incomplete fill):
  Causes: insufficient injection pressure, temperature too low,
          gate too small, thin wall sections restrict flow, early gate freeze
  Fix: increase injection speed/pressure, raise melt T, enlarge gate

SINK MARKS (depressions):
  Occurs: thick sections cool last → skin solidifies, core shrinks → surface sinks
  Causes: insufficient packing pressure/time, gate freezes too early
  Fix: increase packing pressure/time, add packing phase, reduce wall thickness

WARPAGE:
  Non-uniform shrinkage → part distorts from mold shape
  Causes: non-uniform cooling, asymmetric gate, orientation from flow,
          differential crystallinity in semi-crystalline polymers
  Fix: balance cooling, multiple gates, anneal post-mold

WELD LINES (knit lines):
  Where two melt fronts meet → cold front-to-front interface → weak bond
  Always present where melt flows around holes or inserts
  Strength ~50–90% of base material depending on temperature at fusion
  Fix: increase melt T, injection speed; relocate gate to minimize weld lines in critical areas

FLASH:
  Melt escapes parting line → thin web of plastic
  Causes: insufficient clamp force, worn parting line, excessive injection pressure
  Fix: increase clamp, check parting line condition, reduce pressure

JETTING:
  Melt squirts through gate and folds → serpentine pattern, surface defect
  Causes: gate too small, injection speed too high for gate geometry
  Fix: reduce injection speed, enlarge gate, relocate gate to hit wall first

BURN MARKS (diesel effect):
  Trapped air compressed by advancing melt → heats to ignition → burns polymer
  Causes: no venting at end-of-fill, injection too fast
  Fix: add vents, reduce injection speed at end of fill
```

### Injection Molding Materials and Shrinkage

```
SHRINKAGE AND MATERIAL SELECTION
──────────────────────────────────────────────────────────────────
Mold shrinkage: polymer shrinks as it cools → mold cavity must be oversized

  Amorphous polymers (PS, ABS, PC, PMMA): low, predictable shrinkage
    Typical: 0.4–0.8%
    Reason: no crystallization, uniform density change

  Semi-crystalline polymers (PP, PE, POM, Nylon, PBT): higher, anisotropic
    Typical: 1.5–3% (flow direction often different from transverse)
    Reason: crystallization causes significant volume change
    Problem: differential shrinkage → warpage if cooling not balanced

  Filled materials: fiber reinforcement reduces shrinkage, causes anisotropy
    30% glass-filled Nylon: ~0.4% vs ~2% unfilled
    But: highly anisotropic (flow vs. transverse shrinkage different)
    → Warpage risk high if not addressed in tool design

Common Injection Molding Polymers:
  PP (polypropylene):    commodity, living hinge capability, chemical resistant
  ABS:                   tough, paintable, electronic enclosures
  PC (polycarbonate):    transparent, impact resistant, automotive
  Nylon (PA6, PA66):     wear resistant, fatigue resistant, gears/bushings
  POM (Delrin/acetal):   tight tolerances, bearing/gear material
  PBT/PET:               dimensional stability, connector bodies
  PEEK:                  high temperature (~250°C), medical/aerospace
  TPE/TPU:               flexible, overmolding, grips, seals
```

---

## Other Molding Processes

### Blow Molding

```
BLOW MOLDING
──────────────────────────────────────────────────────────────────
EXTRUSION BLOW MOLDING (EBM):
  1. Extruder produces hollow tube (parison)
  2. Mold closes around parison
  3. Compressed air blown in → parison inflates to mold shape
  4. Cool → eject

  Applications: HDPE bottles, automotive ducts, toys
  Materials: HDPE, PP, PVC, PETG
  Limitation: wall thickness control limited (depends on parison swell)

INJECTION BLOW MOLDING (IBM):
  1. Injection mold: precise preform (test-tube shape) with finish
  2. Transfer to blow station: heated, inflated to bottle shape
  3. Superior neck/thread precision (injection formed)
  Applications: pharma bottles, cosmetic containers

INJECTION STRETCH BLOW MOLDING (ISBM / PET bottles):
  1. Injection mold precise PET preform
  2. Reheat to ~100°C (above Tg=80°C)
  3. Stretch rod extends axially + air inflates radially → biaxial orientation
  4. PET crystallites align → high clarity, high strength, gas barrier

  ISBM = how ALL PET beverage bottles are made
  Key: biaxial orientation of PET → 4× better CO₂ barrier vs unoriented
  Single stage (preform to bottle in one machine) vs two-stage (separate)
```

### Thermoforming

```
THERMOFORMING
──────────────────────────────────────────────────────────────────
Heat thermoplastic sheet → clamp over mold → vacuum/pressure forms to shape

VACUUM FORMING (simplest):
  Sheet heated to rubbery state (Tg to Tm range)
  Mold moves into sheet, vacuum applied from mold side
  Sheet stretches to mold → cools → part ejected
  Male (positive) or female (negative) tooling

  Limitation: wall thinning at corners (draw ratio = depth/width)
              Higher draw ratio → severe thinning at corners and rims

PRESSURE FORMING:
  Air pressure on top surface + vacuum → higher resolution, sharper detail
  Better for textured surfaces

TWIN-SHEET FORMING:
  Two sheets formed simultaneously → welded around perimeter
  Creates hollow double-wall panels

Applications:
  Cups, trays, blister packs (PS, PET)
  Refrigerator liners (ABS)
  Automotive headliners, door panels
  Aircraft interior trim (PEEK, PEI at elevated T)

vs injection molding:
  Thermoforming: lower tooling cost ($5,000–50,000 vs $50,000–500,000)
  But: geometry limited (uniform thin-wall, open forms)
  Injection: complex 3D, tight tolerances, high volume economics
```

### Rotational Molding

```
ROTATIONAL MOLDING (ROTOMOLDING)
──────────────────────────────────────────────────────────────────
Polymer powder loaded into hollow mold
Mold heated in oven while rotating biaxially → powder coats inner surface
→ Melt flows, coats evenly → cool → demold

Advantages:
  No internal pressure required → inexpensive tooling (aluminum, even fiberglass)
  Very large parts possible: kayaks, storage tanks, playground equipment
  Uniform wall thickness on complex hollow shapes
  No weld lines (single cavity)

Disadvantages:
  Slow cycle (oven heating/cooling, 20–45 min cycles)
  Limited to hollow parts
  Surface detail limited (no fast injection pressure to fill fine features)
  Material: mostly LLDPE (>80% of rotomolded volume)

Applications: tanks (chemical, water, fuel), kayaks, playground equipment,
  traffic cones, agricultural equipment, marine floats
```

---

## Thermoset Processing

```
THERMOSET PROCESSING OVERVIEW
──────────────────────────────────────────────────────────────────
Thermosets: liquid or solid that CROSSLINKS irreversibly on cure
  Cannot be remelted (unlike thermoplastics)
  Network polymer: high modulus, high temperature resistance

Key thermoset families:
  Epoxy (EP):      structural adhesives, CFRP prepreg, PCBs
  Polyester (UP):  boat hulls, auto body panels, construction
  Vinyl ester:     better corrosion resistance than UP, marine/chemical
  Phenolic (PF):   electrical parts, brake linings, cookware handles
  Polyurethane (PU): foam (rigid/flexible), RIM, elastomers

CURE REACTION:
  Epoxy: resin + hardener (amine or anhydride) → exothermic crosslinking
  Cure time/temperature tradeoff: cold cure (room T) = slow + lower Tg
                                   Hot cure (120–180°C) = fast + high Tg
  Tg of cured epoxy: room-temp cure ~60°C; 180°C cure ~180–220°C

RTM (Resin Transfer Molding):
  Dry fiber preform in closed mold → resin injected under pressure
  Moderate tooling cost, closed mold (clean), good surface both sides
  Used: automotive structural, aerospace secondary structure

VARTM (Vacuum-Assisted RTM):
  One rigid tool + vacuum bag → resin drawn by vacuum
  Low tooling cost (one-sided mold), large structures possible
  Used: wind turbine blades, boat hulls, infrastructure repair

Autoclave prepreg:
  Carbon or glass fiber pre-impregnated with partially cured resin ("B-stage")
  Layup by hand or AFP (Automated Fiber Placement)
  Cure in autoclave: 120–180°C, 5–7 bar (nitrogen)
  Highest quality: minimum porosity, tightly controlled fiber volume fraction
  Cost: autoclave capital + cycle time + refrigerated prepreg storage
  Used: primary aerospace structure (fuselage, wings, nacelles)

COMPRESSION MOLDING (thermoset):
  Sheet Molding Compound (SMC): mat of glass + polyester resin
  Place charge in hot mold, close press → heat + pressure → cure
  Applications: automotive hoods/fenders, electrical enclosures
  Cycle time: 1–5 min (much faster than autoclave)
```

---

## Polymer Crystallinity and Thermal Properties

```
CRYSTALLINITY AND THERMAL TRANSITIONS
──────────────────────────────────────────────────────────────────
AMORPHOUS POLYMERS:
  Random chain entanglement → no long-range order
  Single thermal transition: Tg (glass transition temperature)
  Below Tg: glassy, stiff, brittle
  Above Tg: rubbery, viscous
  Examples: PS, PC, PMMA, ABS, SAN
  Properties: transparent (no crystallite light scattering), no sharp melting point

SEMI-CRYSTALLINE POLYMERS:
  Regions of folded-chain lamellae (crystallites) in amorphous matrix
  Two transitions: Tg (amorphous phase) + Tm (melting, sharp)
  Degree of crystallinity: 20–80% (never 100% — chains too long)
  Processing affects crystallinity:
    Slow cooling: higher crystallinity → stiffer, denser, better chemical resistance
    Fast quench: lower crystallinity → tougher, more transparent
  Examples: PP, PE (HDPE/LDPE/LLDPE), POM, PET, Nylon, PEEK

  Nucleating agents: accelerate crystallization, finer spherulites → toughness
    In PP: clarifier nucleants → optical clarity while maintaining semi-crystalline structure

KEY THERMAL PROPERTIES:
  Material     Tg (°C)    Tm (°C)    Max service T
  PS           ~100       ---        ~70°C (amorphous)
  PC           ~147       ---        ~120°C
  POM          ~-60       ~165       ~100°C
  PP           ~-10       ~160–165   ~100°C (unfilled)
  Nylon 66     ~50        ~260       ~120°C (dry)
  PEEK         ~143       ~343       ~250°C (continuous)
  PTFE         ~115       ~327       ~260°C

MOISTURE EFFECTS:
  Hygroscopic polymers (Nylon, PC, PBT, PET) absorb moisture → plasticization
  → Lowers Tg, reduces mechanical properties
  CRITICAL: must dry before processing (100–120°C for 4–8 hours)
  Wet Nylon injection molded → hydrolytic degradation → reduced MW → brittleness
  Use: Karl Fischer titration or moisture analyzer to verify dryness
```

---

## Polymer Additives

```
ADDITIVES THAT CHANGE PROCESSING AND PROPERTIES
──────────────────────────────────────────────────────────────────
Plasticizers:
  Reduce Tg → increase flexibility, improve low-temp properties
  PVC requires plasticizers (PVC rigid = unplasticized UPVC, flexible = plasticized)
  Dioctyl phthalate (DOP/DEHP): legacy, regulatory pressure → alternatives (DINP, DEHA)
  Migration problem: plasticizer migrates out over time → brittleness

Fillers:
  Talc, calcium carbonate, glass beads: lower cost, increase modulus, reduce shrinkage
  Glass fiber (short chopped): 10–40% loading → 2–5× modulus increase, lower ductility
  Carbon fiber (short): higher stiffness than glass, conductive (EMI shielding)
  Mineral fillers: reduce shrinkage/warpage in semi-crystalline polymers

Flame Retardants:
  Halogenated (Br, Cl compounds): effective, regulatory pressure (RoHS/REACH)
  Halogen-free: aluminum trihydrate (ATH), intumescent systems, phosphorus-based
  Required for: UL 94 ratings (HB, V-2, V-1, V-0)

Stabilizers:
  Heat stabilizers (PVC): prevent HCl evolution during processing
  UV stabilizers: HALS (Hindered Amine Light Stabilizers) for outdoor applications
  Antioxidants: prevent oxidative chain scission during melt processing (especially PP)

Colorants:
  Masterbatch: high-concentration pigment in carrier resin → let-down into base resin
  Typical let-down ratio: 2–5% masterbatch into base
  Carbon black: UV protection + black color (HDPE pipe spec requires CB for UV resistance)
```

---

## Polymer Joining and Secondary Operations

```
POLYMER JOINING
──────────────────────────────────────────────────────────────────
WELDING (thermoplastics only — must melt and fuse):

  Ultrasonic welding:
    High-frequency vibration (20–40 kHz) → friction heat at joint interface
    Fast: 0.5–2 second cycles
    Requires designed energy director (small rib at joint focuses energy)
    Best for: amorphous polymers (ABS, PC, PS), less for semi-crystalline
    Applications: medical devices, automotive, electronics housings

  Vibration welding:
    Linear or orbital vibration between parts → friction melts interface
    Good for large flat parts, irregular joints
    Applications: automotive fluid reservoirs, intake manifolds

  Hot plate welding:
    Heated platen melts both surfaces → remove platen, press together
    Simple tooling, good for polyolefins (PE, PP) which don't ultrasonically weld well
    Slower than ultrasonic

  Spin welding:
    Rotational friction for circular joints
    Simple, effective for round parts (PP tanks, bottles, valves)

  Laser welding:
    Transmitting upper part + absorbing lower part (carbon black or IR dye)
    Laser passes through upper, absorbed at interface → melts joint
    Precise, no mechanical vibration, works on complex joint geometry
    Cost: laser capital, need matched transmittance/absorbance

ADHESIVE BONDING:
  Structural epoxy: 2K, high strength, gap-filling
  UV-cure acrylate: fast, optical assemblies
  Hot melt: EVA, non-structural, packaging

  Surface preparation critical:
    Polyolefins (PP, PE): low surface energy → corona/flame/plasma treatment required
    Flame/corona: oxidizes surface → creates polar groups → adhesion
    Without treatment: adhesive beads up → no bond
```

---

## Decision Cheat Sheet

| Polymer Processing Need | Process |
|------------------------|---------|
| High-volume discrete 3D part | Injection molding |
| Complex geometry with internal features | Injection molding (cores, side actions) |
| Continuous profile, pipe, sheet | Extrusion |
| PET beverage bottle | Injection stretch blow molding (ISBM) |
| Large hollow part (tank, kayak) | Rotational molding |
| Thin-wall packaging, tray | Thermoforming |
| Aerospace CFRP primary structure | Autoclave cure prepreg |
| High-volume composite with closed mold | RTM or compression molding (SMC) |
| Wind turbine blade | VARTM (vacuum infusion) |
| Flexible PVC part | Extrusion or compression molding (plasticized compound) |
| Join PP parts (welding) | Hot plate or vibration welding |
| Join ABS parts (welding) | Ultrasonic welding |
| Adhesive bond to polyolefin | Surface treat (corona/plasma) + structural adhesive |
| Reduce injection mold cycle time | Reduce wall thickness, conformal cooling, hot runner |

---

## Common Confusion Points

**Thermoplastic vs thermoset recycling**: Thermoplastics can be remelted and reprocessed (though molecular weight degrades with each cycle). Thermosets cannot — the crosslinks are permanent. This is why CFRP aerospace composites are difficult to recycle: the epoxy matrix cannot be remelted to separate from the carbon fiber. Thermoplastic matrix composites (PEEK, PPS) are emerging specifically to enable recycling.

**Shrinkage is not just dimensional**: Differential shrinkage in injection-molded semi-crystalline parts causes warpage — the part curves away from its designed shape. This is not just a size issue. Uniform cooling, balanced gating, and adding fillers (which reduce and equalize shrinkage) are all warpage countermeasures, not just dimensional corrections.

**Mold temperature controls crystallinity**: For semi-crystalline polymers (PP, Nylon, POM), higher mold temperature = more crystallinity = higher stiffness/chemical resistance but slower cycle. Lower mold temperature = faster cycle but lower crystallinity. The common mistake is setting mold temperature as cold as possible for cycle time, then wondering why parts are soft or dimensionally unstable.

**Extrusion shear history matters**: Twin-screw compounding extrusion (mixing) and single-screw profile extrusion (shaping) are fundamentally different operations with different screw designs. A single-screw designed for pipe extrusion will poorly mix colorants or additives — it just pumps. For compounding, twin-screw with kneading blocks is needed.

**Die swell prediction is empirical**: Extrudate swell (the expansion of melt beyond the die opening) is a viscoelastic effect that depends on material, temperature, and die geometry. Software can model it (Moldex3D, Ansys Polymat), but die design almost always requires empirical tuning — cut die, extrude, measure swell, adjust die geometry. First-pass die is always a prototype.

**PET preform storage matters**: PET preforms for ISBM can be injection molded and stored for weeks or months before blow molding. But PET is hygroscopic — improperly stored preforms absorb moisture, which causes haze and mechanical property degradation during stretch blow molding. Dry storage (<50% RH) or pre-drying before blowing is required.
