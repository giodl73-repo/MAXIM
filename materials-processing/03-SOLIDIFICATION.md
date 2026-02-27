# Solidification and Casting Metallurgy

## The Big Picture

Solidification transforms liquid metal into solid by nucleation and growth of crystals. The as-cast microstructure — grain size, grain orientation, phase distribution, defect content — is determined during this phase transition. All subsequent processing starts from the as-cast state; you cannot fix what solidification creates without re-melting or extensive thermomechanical processing.

```
SOLIDIFICATION FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Liquid metal at liquidus temperature
        │
        ▼  undercooling (driving force for solidification)
Nucleation: first crystals form
        │
        ▼  crystal growth into liquid
Crystal growth: dendrites extend into undercooled liquid
        │
        ▼  latent heat of fusion released, slows cooling
Dendritic solidification: branching tree-like growth
        │
        ▼  final liquid solidifies between dendrite arms
Solidification complete: as-cast grain structure formed

Result determines:
  Grain size (coarse → lower strength, more ductility)
  Grain orientation (columnar vs equiaxed)
  Segregation (composition variation within grains)
  Porosity (voids from shrinkage and gas)
  Inclusions (oxides, sulfides, non-metallic phases)
```

---

## Nucleation in Solidification

### Undercooling and Nucleation

```
SOLIDIFICATION NUCLEATION
──────────────────────────────────────────────────────────────────
Liquid must be below Tm (undercooled) for solidification to occur.
Driving force: ΔGv = ΔHf × ΔT / Tm
  (greater undercooling ΔT → stronger driving force)

Homogeneous nucleation:
  Requires ΔT ≈ 100–300°C undercooling for metals
  Rarely achieved in casting (mold walls and heterogeneous sites prevent it)

Heterogeneous nucleation (dominant in practice):
  Nucleation on: mold wall, oxide particles, added inoculants
  Lower energy barrier → nucleation at small undercooling (1–10°C)
  More nucleation sites → finer grain size

INOCULATION (grain refinement):
  Deliberately add nucleants to melt → many more nucleation sites
  → Finer equiaxed grain structure → better mechanical properties

  Steel:    Titanium + nitrogen (TiN nucleants)
  Aluminum: Ti + B (TiAl₃ + TiB₂ nucleants), grain refiner rod
  Cast iron: Ferrosilicon inoculant (promotes graphite nucleation)
  Magnesium: Zr additions
```

---

## Dendritic Growth and Segregation

### Dendritic Structure

A dendrite is literally a tree data structure grown in metal: primary arm = root, secondary arms = children, tertiary arms = grandchildren. SDAS (secondary dendrite arm spacing) is the characteristic inter-node distance. The growth algorithm is physically instantiated recursive branching: preferential growth along crystallographically fast directions, with branching where curvature maximizes undercooling. Coarser dendrites (slow cooling) = fewer branching levels; finer dendrites (fast cooling) = deeper tree.

```
DENDRITIC GROWTH MECHANISM
──────────────────────────────────────────────────────────────────
Dendrite = tree-like crystal growing with preferential orientation

        Primary arm
          │
          ├─── Secondary arm ──── Tertiary arm
          │       (SDAS)
          ├─── Secondary arm
          │
          └─── Secondary arm

SDAS = Secondary Dendrite Arm Spacing
  Controls microsegregation and post-solidification properties

SDAS depends on cooling rate:
  Fast cooling → small SDAS (finer dendrites)
  SDAS ∝ (cooling rate)^(-1/3) typically

  Die cast aluminum: SDAS ≈ 5–15 µm
  Sand cast aluminum: SDAS ≈ 50–100 µm
  Directionally solidified (single crystal): columnar, SDAS controlled
```

### Microsegregation

```
MICROSEGREGATION (CORING)
──────────────────────────────────────────────────────────────────
During dendritic solidification, solute rejected at solid-liquid interface.
First material to solidify: lower solute content (lean)
Last material to solidify (interdendritic): higher solute content (rich)

Al-Cu alloy example (2024):
  Dendrite center: ~3% Cu
  Interdendritic: ~6% Cu (enriched)
  Eutectic phase (CuAl₂) at grain boundaries (if >5.65% Cu locally)

Effects:
  Non-uniform mechanical properties within grain
  Incipient melting during heat treatment (hot spots in Cu-rich zones)
  Corrosion preferentially attacks Cu-rich interdendritic regions

Remedy: Homogenization anneal
  Heat to just below solidus for many hours
  Diffusion homogenizes composition
  SDAS → determines homogenization time (D × t ∝ SDAS²)
  Al alloys: 460–520°C for 12–24 hours (before solution treatment)
```

### Macrosegregation

```
MACROSEGREGATION
──────────────────────────────────────────────────────────────────
Composition variation over large scale (cm to meters).
Caused by: bulk fluid flow, gravity, dendrite settling.

Types:
  Normal segregation:   solute-rich liquid flows to ingot center/top
                        as solidification progresses from outside in
  Inverse segregation:  solute-rich liquid squeezes outward
                        (pressure from shrinkage)

A-segregates and V-segregates:
  Flow channels in ingot casting create tubes of high-solute material
  "A-segregates" = inclined channels
  "V-segregates" = central vertical channels
  Dangerous defects in large forgings (must be inspected ultrasonically)

Remedy:
  Electromagnetic stirring (EMS) in continuous casting
  Refinement of casting practice (superheat reduction, cooling rate increase)
  Ingot cropping: discard segregated top (pipe zone)
```

---

## Solidification Defects

### Porosity

```
TYPES OF POROSITY
──────────────────────────────────────────────────────────────────
SHRINKAGE POROSITY:
  Metal shrinks ~2–7% in volume on solidification
  Last metal to solidify (hot spots) has no liquid feed
  → Voids form where liquid cannot reach

  Macroporosity (pipe, cavity): large void, detectable by radiograph
  Microporosity: distributed fine voids between dendrites
  Occurs in: isolated "hot spots", thick sections, poor riser design

  Prevention:
    Solidification from thin → thick → riser (directional solidification)
    Large risers that stay liquid while part solidifies
    Chills (metal inserts) to accelerate local cooling
    Pressure casting or squeeze casting

GAS POROSITY:
  Dissolved gas (H₂ in Al, N₂/CO in steel) comes out of solution
  Solubility of gas in liquid >> in solid → gas rejected on solidification
  → Spherical voids (distinguishable from shrinkage by shape)

  Source in aluminum: moisture on charge material, hydrogen from moisture
    2Al + 3H₂O → Al₂O₃ + 3H₂ (at casting temperature)
    Dissolved H₂ forms spherical pores on solidification
  Prevention: degas treatment (rotary degassing with N₂/Cl₂)
  Testing: reduced pressure test (RPT), density index

COMBINED SHRINKAGE + GAS:
  Most common: irregular voids at hot spots filled with gas
```

### Hot Tearing / Hot Cracking

```
HOT TEARING (HOT CRACKING)
──────────────────────────────────────────────────────────────────
Crack that forms in semi-solid state (mushy zone) as metal contracts.
Between dendrites where strength is nearly zero.

Mechanism:
  Dendrite skeleton forms → starts to contract on cooling
  Interdendritic liquid feeds contraction
  If feeding insufficient → tensile stress in mushy zone
  → Hot tear forms (wide, branching, oxide-filled crack)

Susceptibility increases with:
  Wide solidification range (large mushy zone)
  High shrinkage alloys
  Geometric constraints on contraction
  Insufficient interdendritic feeding

Susceptible alloys:
  Al-Cu alloys (2024): yes (need controlled pouring)
  Al-Si alloys (356): no (Si reduces shrinkage, narrow mushy zone)
  High-carbon steel: susceptible
  Single-crystal Ni superalloys: major concern → casting practice critical

Prevention:
  Add Zr to Al-Cu (grain refinement → more paths for liquid feeding)
  Optimize alloy composition (Si in Al alloys)
  Preheat dies to reduce thermal gradients
  Modify die design to avoid strain concentration
```

---

## Solidification Control

### Directional Solidification (DS) and Single Crystal (SX)

```
DIRECTIONAL SOLIDIFICATION (DS)
──────────────────────────────────────────────────────────────────
Controlled heat extraction from one end of casting → columnar grains
grown parallel to heat flow direction.

Purpose:
  Grain boundaries perpendicular to thermal/mechanical stress eliminated
  High-temperature creep resistance improved (no transverse grain boundaries)
  Applied to: Ni superalloy turbine blades and vanes

Process:
  1. Part mold in vacuum furnace
  2. Molten superalloy poured
  3. Mold withdrawn slowly from furnace (10–25 mm/min)
  4. Temperature gradient maintained: solid below, liquid above
  5. Solidification front moves upward → columnar grains aligned

SINGLE CRYSTAL (SX):
  Same as DS but with a spiral selector or "grain selector" at base
  Only one grain orientation passes through spiral
  Entire turbine blade is ONE crystal → no grain boundaries at all
  Maximum creep resistance at turbine inlet temperature (>1000°C)
  Commercial alloys: CMSX-4, René N6, PWA 1484

Property comparison:
  Equiaxed: baseline
  DS: 2× creep life vs equiaxed at same conditions
  SX: 5–10× creep life vs equiaxed
  → Enables 50–100°C higher turbine inlet temperature
  → 2–5% increase in engine efficiency per 10°C turbine temp increase
```

---

## Solidification of Key Materials

### Cast Iron Solidification

```
CAST IRON SOLIDIFICATION
──────────────────────────────────────────────────────────────────
Carbon content 2.5–4% → eutectic solidification dominates

Gray iron (flake graphite):
  Si promotes graphite (not cementite) formation
  Flake graphite forms during eutectic solidification
  Casting properties: good machinability, damping, compressive strength
  Tensile strength limited by stress concentrations at graphite flakes
  Grade: ASTM A48 (30B, 35B, 40B by tensile strength)

Ductile (nodular/spheroidal graphite) iron:
  Mg + Ce additions → graphite forms spheres, not flakes
  Treatment: Mg treatment in ladle, then inoculation
  Much higher ductility and tensile strength vs gray iron
  Grade: ASTM A536 (65-45-12, 80-55-06, 100-70-03: UTS-Yield-Elongation)
  Applications: crankshafts, gears, valves, automotive structural

White iron:
  Fast cooling OR low Si → Fe₃C (cementite) forms instead of graphite
  Very hard, brittle, white fracture surface
  Used for wear applications (mill liners, pump impellers)

Malleable iron:
  Start as white iron (cementite), then anneal:
  950–1050°C → temper carbon rosettes form from Fe₃C
  Better ductility than white, machinability better than ductile
  Largely superseded by ductile iron (faster to produce)
```

### Aluminum Alloy Solidification

```
ALUMINUM CASTING ALLOY SOLIDIFICATION
──────────────────────────────────────────────────────────────────
A356 (Al-7Si-0.3Mg): most common sand/permanent mold cast alloy
  Near-eutectic composition → excellent fluidity
  Al-Si eutectic (12.6% Si) solidifies last, fills all spaces
  As-cast: coarse eutectic Si particles → poor ductility

Modification (Sr, Na addition):
  Na or Sr (50–200 ppm) → changes Si particle morphology
  Fibrous/modified eutectic → improved ductility
  Eutectic solidifies at lower temperature (thermal analysis detectable)
  Sr treatment: lasts for hours; Na treatment: shorter life

Grain refinement (Ti-B):
  Al-Ti-B grain refiner rod added to melt
  TiAl₃ + TiB₂ particles nucleate α-Al grains
  Result: fine equiaxed α-Al → better properties, reduced hot tearing

Correct sequence:
  1. Melt
  2. Add grain refiner (Ti-B rod)
  3. Add modifier (Sr)
  4. Degas (rotary degassing)
  5. Clean flux
  6. Pour

A380 (Al-8.5Si-3.5Cu): die casting alloy
  Lower freezing range than A356
  Excellent die castability (high Si, good fluidity)
  Cu addition → some precipitation hardening possible
  Cannot be heat treated effectively (die casting = subsurface porosity
    → T6 treatment causes blistering)
```

---

## Casting Simulation

**CALPHAD** (CALculation of PHAse Diagrams): computational thermodynamics for multi-component alloys. Instead of reading a binary phase diagram, CALPHAD computes equilibrium phases for 10+ component alloys using assessed thermodynamic databases (SGTE, COST). Software: Thermo-Calc, Pandat, FactSage. This is database-driven computation replacing manual lookup — the same shift from hand-calculated tables to computational models that happened in every engineering field. Modern "CALPHAD-informed alloy design" means using these tools to predict phase stability, transformation temperatures, and solidification paths before casting a single ingot.

```
SOLIDIFICATION SIMULATION
──────────────────────────────────────────────────────────────────
Software tools: MAGMAsoft, ProCAST, FLOW-3D, AnyCasting

Physics modeled:
  Heat transfer: FEA/FVM of thermal fields
  Fluid flow: filling, turbulence, cold shuts
  Solidification: thermal gradients, solidification front
  Porosity prediction: feeding, Niyama criterion
  Residual stress: thermal contraction

Niyama criterion:
  Predicts interdendritic shrinkage porosity location:
  Ny = (dT/dx) / √(dT/dt) [°C^0.5 s^0.5 mm^-1]
  Low Ny → poor feeding → shrinkage risk
  Threshold varies by alloy: Al ~1.0, Steel ~0.1

Applications of simulation:
  Optimize riser design before cutting tooling
  Identify hot spots, gate locations
  Predict where macro-porosity will form
  Reduce trial-and-error (expensive scrap + tooling rework)
```

---

## Decision Cheat Sheet

| Solidification Challenge | Solution |
|--------------------------|----------|
| Shrinkage porosity in thick sections | Add/enlarge risers, use chills, optimize solidification direction |
| Gas porosity in aluminum | Rotary degassing, dry charge, dehumidify molds |
| Coarse grain in aluminum casting | Add Ti-B grain refiner |
| Poor ductility from flake Si in Al-Si | Add Sr or Na modifier |
| Hot tearing in Al casting | Grain refine with Zr (Al-Cu) or reduce geometric restraint |
| Maximum creep life in Ni turbine blade | Single crystal solidification |
| Need to eliminate segregation in aluminum billet | Homogenization anneal (460°C/24h) |
| Predict where shrinkage will form | Solidification simulation (Niyama criterion) |

---

## Common Confusion Points

**Riser must solidify after the casting**: A riser that solidifies before the part it feeds causes more porosity, not less. The riser must be located and sized to be the last thing to solidify — it feeds liquid into the part as the part contracts. "Directional solidification toward the riser" is the fundamental casting design principle.

**Gas porosity is spherical; shrinkage is irregular**: You can distinguish them on radiograph or cross-section. Gas pores are round (surface tension creates spherical shape). Shrinkage voids are irregular, dendritic, jagged. This distinction matters for root cause analysis of casting scrap.

**Modified Si morphology can revert**: Sr or Na modification is consumed over time in the holding furnace. If the metal sits too long before pouring, modification level drops and Si reverts toward coarser morphology. Thermal analysis (cooling curve shape) can detect adequate modification level.

**Continuous casting vs ingot casting**: Modern steel and aluminum production uses continuous casting (mold is short, metal continuously withdraws as it solidifies — producing slab, billet, bloom). Ingot casting (liquid poured into a large mold, solidifies as a block) is used for special alloys, large forgings. Continuous casting is faster, more uniform, less segregation.

**Single crystal is not glassy**: A single crystal turbine blade IS a crystal — a single, continuous, perfect crystal lattice. It's not amorphous (glass) — it has the same FCC structure as ordinary Ni alloys. The difference is the absence of grain boundaries, which are the weak links for high-temperature creep and thermal fatigue.
