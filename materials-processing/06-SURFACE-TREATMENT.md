# Surface Treatments and Coatings

## The Big Picture

Surface treatments modify only the near-surface region of a part while leaving the bulk unchanged. They solve the fundamental materials engineering conflict: bulk properties (toughness, machinability) optimized for the substrate, while surface properties (hardness, wear resistance, corrosion protection) optimized independently.

```
SURFACE TREATMENT TAXONOMY
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  SURFACE MODIFICATION (no new layer added)                       │
│    Mechanical: shot peen, laser peen, burnishing (cold work)    │
│    Thermal: induction harden, flame harden, laser harden        │
│    Diffusion: carburize, nitride, boriding, chromizing          │
├─────────────────────────────────────────────────────────────────┤
│  CONVERSION COATINGS (substrate surface chemically converted)    │
│    Anodizing (Al) → Al₂O₃ layer                                 │
│    Phosphating (Fe) → iron phosphate                            │
│    Chromate conversion (Al) → chrome complex                    │
│    Bluing (Fe) → magnetite (cosmetic/mild corrosion)            │
├─────────────────────────────────────────────────────────────────┤
│  APPLIED COATINGS (new layer deposited)                          │
│    PVD (Physical Vapor Deposition): sputtering, evaporation      │
│    CVD (Chemical Vapor Deposition): thermal or plasma            │
│    Thermal spray: HVOF, plasma spray, arc spray                 │
│    Electroplating / electroless plating                         │
│    Paint / organic coatings                                      │
│    Hot-dip galvanizing / tin coating                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## PVD (Physical Vapor Deposition)

### PVD Process Overview

```
PVD PROCESS
──────────────────────────────────────────────────────────────────
Source material (target) → vaporized by physical means
→ vapor travels through vacuum
→ condenses on substrate as thin film

Methods:
  Evaporation:  electron beam or resistive heating evaporates source
                Low energy → porous coatings, limited adhesion
                Still used for: optical coatings, decorative

  Sputtering:   Argon ions (plasma) bombard target
                Atoms ejected, travel to substrate
                Higher energy → denser, better adhesion
                Magnetron sputtering: most common industrial PVD

  Arc evaporation: cathodic arc ignites on target → very energetic
                   Highest ionization, best film density and adhesion
                   Macroparticles (droplets) → surface roughness
                   Filtered arc: eliminates macroparticles

Process conditions:
  Vacuum: 10⁻³ to 10⁻⁶ torr
  Temperature: 150–500°C (substrate, depends on process)
  Coating thickness: 1–10 µm typical
  Deposition rate: 0.1–10 µm/hour
```

### PVD Coating Materials

| Coating | Hardness (GPa) | Friction vs steel | Color | Applications |
|---------|---------------|-------------------|-------|--------------|
| TiN | 25–28 | 0.4–0.6 | Gold | Cutting tools (general) |
| TiAlN | 28–35 | 0.4–0.6 | Violet/black | High-speed dry machining |
| AlTiN | 38–42 | 0.4–0.6 | Dark gray | Hardest standard coating |
| CrN | 18–22 | 0.3–0.5 | Silver | Corrosion + wear, decorative |
| TiCN | 30–35 | 0.2–0.4 | Blue-gray | Low friction, forming dies |
| DLC (a-C:H) | 15–35 | 0.05–0.2 | Black | Ultra-low friction, bearings |
| Diamond (CVD) | 100+ | 0.05–0.15 | Transparent | Abrasive tools, optics |

### PVD Limitations

```
PVD LIMITATIONS
──────────────────────────────────────────────────────────────────
Line-of-sight deposition:
  PVD coats what it can "see" from source
  Deep holes, blind features → shadowing → incomplete coverage
  Substrate rotation helps, but deep features remain problematic

Temperature limitation:
  Most PVD processes: 150–500°C
  Tempered steel tools: if temper temp < PVD temp → re-tempering
  High-speed steel (M2): temper at 540°C, PVD at 480°C → OK
  D2 cold work steel: temper at 520°C, PVD at 480°C → marginal

Thickness limited:
  >10 µm: residual stress → coating spallation
  Most PVD tools: 2–5 µm for best balance

Adhesion requires:
  Excellent surface preparation (cleaning, plasma etch)
  Surface roughness < Ra 0.3 µm preferred
  No contamination, oil, oxide
```

---

## CVD (Chemical Vapor Deposition)

### CVD Process

```
CVD PROCESS
──────────────────────────────────────────────────────────────────
Reactive gases introduced into hot furnace
→ chemical reaction at substrate surface
→ coating material deposited

Example: TiCN CVD on cemented carbide insert
  TiCl₄ + CH₄ + N₂ + H₂ → TiCN + HCl + other products
  Temperature: 1000–1050°C
  Atmosphere: controlled gas mixture
  Deposition rate: 0.5–2 µm/hour (slower than PVD)
  Thickness: 5–20 µm (thicker than PVD)

CVD coatings on carbide inserts:
  TiC (base layer, adhesion)
  TiCN (transition)
  TiN or Al₂O₃ (top layer)
  Multi-layer stack: 3–20 µm total
  Applied to essentially ALL carbide inserts for metal cutting

Advantages over PVD:
  Full conformal coverage (no line-of-sight limitation)
  Greater thickness achievable
  Al₂O₃ only practical via CVD (not PVD — too stable)

Disadvantages:
  High temperature: 900–1100°C → cannot use on hardened steel
  Post-coat treatment may be needed (strength recovery for cemented carbide)
  CVD residual stress → more brittle coating
```

### PECVD (Plasma-Enhanced CVD)

Plasma provides additional energy → allows lower deposition temperature (200–400°C). Used for: DLC coatings on precision parts, SiN/SiO₂ on semiconductors. Lower temperature than thermal CVD → can coat hardened steel.

---

## Thermal Spray

```
THERMAL SPRAY PROCESSES
──────────────────────────────────────────────────────────────────
Feedstock (powder or wire) heated to molten/semi-molten state
→ accelerated toward substrate by gas jet
→ impacts, flattens (splat), solidifies
→ layer-by-layer buildup

Processes by energy level:
  Arc spray:     electric arc melts wire
                 Simple, cheap, high deposition, thick coatings
                 Porosity ~5–15%
                 Applications: corrosion coatings (zinc, aluminum)

  Flame spray:   Oxy-fuel flame melts powder/wire
                 Economical, versatile
                 Porosity ~5–15%

  Plasma spray:  DC plasma torch → 10,000–20,000°C
                 Can spray refractory ceramics (Al₂O₃, ZrO₂)
                 Porosity ~2–5%
                 Applications: TBC (thermal barrier coating) on turbines

  HVOF:          High-Velocity Oxy-Fuel
                 Supersonic jet → high impact velocity → dense coating
                 Porosity <1%, high hardness
                 Applications: WC-Co (tungsten carbide) hard facing
                               aircraft landing gear rebuild
                               pump shafts

  Cold spray:    Particles never melt → purely kinetic energy
                 Below material melting → substrate/particle not overheated
                 Copper, aluminum, titanium, steel
                 Additive repair of high-value components
```

### Thermal Barrier Coatings (TBC)

```
TBC SYSTEM (gas turbine hot section)
──────────────────────────────────────────────────────────────────
Purpose: insulate Ni superalloy substrate from hot gas (>1000°C)
         → allows higher turbine inlet temperature
         → increases engine efficiency

TBC system layers:
  ┌────────────────────────────────────────────┐
  │ Ceramic top coat: 7% YSZ (yttria-stabilized│
  │ zirconia, ZrO₂+7%Y₂O₃), ~150–500 µm thick │
  │ Thermal conductivity: ~2 W/m·K (vs 12 for  │
  │ substrate)  Low but non-zero→ temp gradient │
  ├────────────────────────────────────────────┤
  │ Thermally grown oxide (TGO): α-Al₂O₃      │
  │ Grows during service from MCrAlY oxidation │
  │ TGO growth → eventually causes spallation  │
  ├────────────────────────────────────────────┤
  │ Bond coat: MCrAlY (M=Ni, Co, Fe)          │
  │ ~100–150 µm, applied by HVOF or plasma     │
  │ Provides adhesion for top coat             │
  │ Al-rich → forms protective TGO             │
  ├────────────────────────────────────────────┤
  │ Ni superalloy substrate (CMSX-4 or similar)│
  └────────────────────────────────────────────┘

Failure: TGO grows → stresses at TBC/TGO interface → delamination
Lifetime: 1,000–3,000 hours thermal cycles (turbine start-stop)
Inspection: fluorescent indicators in coating for damage detection
```

---

## Electroplating

```
ELECTROPLATING PRINCIPLES
──────────────────────────────────────────────────────────────────
Metal ions in solution reduced at cathode (part):
  M^n+ + ne⁻ → M (deposited metal)

At anode: metal oxidizes (dissolves) to replenish solution
  M → M^n+ + ne⁻

Key parameters:
  Current density (A/dm²): controls deposition rate, grain size
  Bath temperature: affects grain structure, stress
  Additives (brighteners, levelers): surface finish control
  Thickness: set by time × current density × efficiency

Thickness uniformity:
  Plating deposits preferentially on high-current-density areas
  (edges, corners, protrusions get thicker)
  Throwing power: how well bath deposits on recessed areas
```

### Common Electroplated Coatings

| Coating | Function | Applications | Notes |
|---------|----------|--------------|-------|
| Hard Chrome | Wear, corrosion | Hydraulic rods, piston rings | EPA concerns (Cr⁶⁺); HVOF replacing |
| Electroless Nickel | Uniform thickness, wear | Complex shapes, molds | Uniform (no current needed) |
| Decorative Chrome | Cosmetic + mild corrosion | Auto trim, fixtures | Flash over Ni undercoat |
| Zinc | Sacrificial corrosion | Steel fasteners, sheet | Dissolves preferentially to protect Fe |
| Cadmium | Corrosion + lubricity | Aerospace fasteners | Carcinogenic, RoHS restricted |
| Copper | Undercoat, conductivity | PCB, decorative base | Low Cr⁶⁺ concerns |
| Gold | Contact resistance | Electrical contacts | Very thin (0.1–1 µm) |
| Silver | Conductivity, soldering | Electronics, RF | Tarnishes → use on mating surfaces |
| Hard Chrome alternatives | Wear (HVOF WC-Co, LPCS) | Replacing hard chrome | REACH/EPA compliance |

---

## Conversion Coatings

### Anodizing (Aluminum)

```
ANODIZING PROCESS
──────────────────────────────────────────────────────────────────
Electrolytic oxidation: aluminum becomes ANODE in acidic bath
Al → Al₂O₃ (oxide grows into and above original surface)

Al(substrate) → Al³⁺ + 3e⁻ (at surface)
Al³⁺ + H₂O → Al₂O₃ + H⁺ (at electrolyte-oxide interface)

Anodize types:
  Type I (Chromic acid anodize):
    6–8% chromic acid, 20–45V
    Thinnest layer (~2–5 µm), excellent fatigue life
    Used where corrosion resistance needed without much thickness change
    REACH restricted (Cr⁶⁺) → Type I alternatives being developed

  Type II (Sulfuric acid anodize):
    15% H₂SO₄, 15–22V
    Standard anodize (~5–20 µm)
    Sealed with hot water or dichromate → corrosion resistance
    Colored by dyeing (porous oxide structure holds dye)

  Type III (Hard anodize, sulfuric acid):
    Low temperature, high current density
    Dense, thick layer (12–75 µm)
    Hardness: 400–500 HV (nearly as hard as hard chrome)
    Wear resistance, insulation
    Dark gray/black color

Sealing:
  Anodize layer is porous → seal for corrosion resistance
  Hot water seal: 95–100°C → boehmite seals pores
  Dichromate seal: chromate fills pores → better corrosion, restricted
  PTFE/silicone seal: low-friction applications
```

### Phosphating

Conversion coating for steel by phosphoric acid reaction. Iron phosphate or zinc phosphate crystals grow on surface. Purpose: paint adhesion base (automotive, appliance) or wear-in surface for engine components. Rust prevention in dry storage. Not a standalone corrosion coating (must be sealed with oil or paint).

---

## Corrosion Protection Strategies

```
CORROSION PROTECTION HIERARCHY
──────────────────────────────────────────────────────────────────
Material selection:
  Use inherently corrosion-resistant material (SS, Al alloy, Ti)
  Most reliable, adds to base cost

Sacrificial anode (cathodic protection):
  Zinc galvanizing: Zn is more active than Fe → Zn corrodes first
  Protects steel even where coating has holidays/pinholes
  Also: Mg anodes on ships and underground pipes

Barrier coating:
  Paint, epoxy, powder coat → physical barrier to moisture
  Relies on adhesion and absence of defects
  Inspect and maintain (marine, buried structures)

Conversion coating + primer + topcoat (aerospace):
  Aluminum: anodize → chromate primer → topcoat
  Steel: phosphate → epoxy primer → polyurethane topcoat
  Military aircraft: DOD-PRF-23827 washprimer, MIL-PRF-23377 epoxy

Inhibitors:
  Chromate inhibitor in primer → self-heals damaged areas
  Replacing chromate: REACH/RoHS → vanadates, molybdates, Ce compounds
```

---

## Decision Cheat Sheet

| I need to... | Surface treatment |
|--------------|------------------|
| Protect cutting tool at high speed, dry | TiAlN or AlTiN PVD coating |
| Apply cemented carbide insert coating | CVD (TiCN/Al₂O₃/TiN multi-layer) |
| Coat complex geometry uniformly | CVD or electroless nickel |
| Hard wear surface on steel part | Hard chrome (legacy) or HVOF WC-Co |
| Thermal barrier on turbine blade | TBC system (plasma spray YSZ) |
| Corrosion protection for aluminum aircraft | Type I/II anodize + chromate primer |
| Decorative + corrosion on steel | Zinc electroplate |
| Wear resistance on steel without high heat | PVD (nitride-based) |
| Aluminum fatigue-critical part | Type I anodize (least effect on fatigue) |
| Rebuild worn shaft (repair) | HVOF spray + grind to dimension |

---

## Common Confusion Points

**PVD temperature limits steel use**: Most PVD processes run at 150–500°C. If the substrate was tempered at 200°C (high-hardness tool steel), PVD at 480°C will over-temper it — losing hardness. Always check PVD process temperature against substrate tempering temperature.

**Anodize adds AND removes dimension**: Type II anodize on aluminum grows approximately half into the surface (removes) and half above the surface (adds). 20 µm anodize = 10 µm added above original surface + 10 µm consumed from original surface. Hard anodize (Type III) = similar ratio. Final dimensions must account for this growth.

**Electroless nickel vs electroplated nickel**: Electroless nickel (EN) requires no current — uses chemical reduction. It deposits uniformly on all surfaces, including inside holes and complex recesses. Electroplated nickel requires current — deposits non-uniformly with higher thickness on edges and protrusions. EN is usually preferred for dimensional uniformity; electroplated Ni for cost.

**Hard chrome vs HVOF WC-Co**: Hard chrome (electroplated Cr from hexavalent chromium bath) is being replaced by HVOF tungsten carbide-cobalt (WC-Co) for most aerospace and hydraulic applications. HVOF is denser, harder (1000–1200 HV vs 800–900 HV for hard chrome), and better adhesion. The driver is environmental: hex chrome (Cr⁶⁺) is carcinogenic. REACH and HASAW regulations are forcing transition.

**DLC is not one material**: Diamond-like carbon covers a family of amorphous carbon films ranging from hydrogen-free (ta-C, hardest, highest carbon sp3) to hydrogenated (a-C:H, lower hardness, lower friction). Selection matters: ta-C for maximum hardness; a-C:H for minimum friction. Each has different deposition process and temperature sensitivity.
