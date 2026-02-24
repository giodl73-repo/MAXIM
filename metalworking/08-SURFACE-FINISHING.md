# Surface Finishing

## The Big Picture

Surface finishing modifies the outermost layer of a component — its chemistry, microstructure, or texture — to achieve properties the bulk material cannot provide: corrosion resistance, wear resistance, electrical conductivity, thermal insulation, or aesthetics. The critical insight is that **bulk properties and surface properties are independent design variables**. A cheap carbon steel component can have the corrosion resistance of platinum (electroplating) or the hardness of tungsten carbide (thermal spray).

```
SURFACE FINISHING — LANDSCAPE:

  CATEGORY          PROCESS             ADDS              TYPICAL THICKNESS
  ─────────────────────────────────────────────────────────────────────────
  Electrochemical   Electroplating      Metal layer       1–500 μm
                    Anodizing           Oxide layer       5–25 μm (standard), 25–100 μm (hard)
                    Electroless plating Metal (no current) 0.1–25 μm

  Organic coating   Powder coating      Polymer film      50–100 μm
                    Painting            Polymer film      25–250 μm
                    E-coating           Epoxy primer      15–30 μm

  Thermal spray     Flame spray         Metal/ceramic     50–1500 μm
                    HVOF                WC-Co/MCrAlY      50–500 μm
                    Plasma spray        Ceramic TBC       100–500 μm

  PVD/CVD           Physical vapor dep  TiN/TiAlN/DLC    1–10 μm
                    Chemical vapor dep  TiC/Al₂O₃        5–20 μm

  Diffusion         Carburizing         C diffusion       0.5–3 mm
                    Nitriding           N diffusion       0.1–0.8 mm
                    Boriding            B diffusion       0.1–0.5 mm

  Mechanical        Shot peening        Compressive stress N/A (surface modification)
                    Burnishing          Work hardening    N/A
                    Polishing           Reduced Ra        N/A

  SELECTION DRIVERS:
    Corrosion protection → electroplating (Zn, Ni, Cr), anodizing (Al), powder coat
    Wear resistance → PVD TiN/TiAlN (tools), thermal spray WC-Co (pumps, bearings)
    Thermal barrier → plasma spray YSZ (turbine blades)
    Aesthetics + protection → electroplating (Cr, Au, Ni), powder coat
    Fatigue improvement → shot peening (induces compressive residual stress)
```

---

## Electroplating

### Faraday's Laws

```
ELECTROPLATING CELL:

  Power supply (DC) → anode (dissolving metal or inert) → electrolyte → cathode (workpiece)

  At cathode (workpiece): M²⁺ + 2e⁻ → M  (metal deposits)
  At anode (soluble):     M → M²⁺ + 2e⁻  (metal dissolves into bath)
  At inert anode:         2H₂O → O₂ + 4H⁺ + 4e⁻ (bath becomes acidic; replenishment needed)

FARADAY'S LAWS:
  1st law: Mass deposited ∝ charge passed (Q = I × t)
  2nd law: Equivalent masses of different metals deposited by same charge

  m = (I × t × M) / (n × F)

  Where:
    m = mass deposited (grams)
    I = current (amperes)
    t = time (seconds)
    M = molar mass of deposited metal (g/mol)
    n = electrons per ion (valence)
    F = Faraday constant (96,485 C/mol)

  Example: deposit 1 gram of nickel (M=58.7, n=2):
  Q = (1 × 2 × 96,485) / 58.7 = 3,289 coulombs = 54.8 A·min
  At 5A: 660 seconds = 11 minutes

  CURRENT EFFICIENCY:
  Not all current goes to metal deposition (H₂ evolution competes)
  Efficiency = 95–99% for Ni, Cu; lower for Cr (~15% for hexavalent chrome!)
  → Hexavalent chromium: 85% of current evolves H₂ → very low efficiency → high cost + toxicity
```

### Major Electroplating Systems

```
ZINC PLATING:
  Purpose: cathodic corrosion protection for steel
  Mechanism: zinc is anodic to steel → sacrificial anode
    Even if zinc layer is scratched → zinc corrodes preferentially → steel protected
  Typical thickness: 5–25 μm
  Salt spray life: 100–200 hours (plain Zn); 200–400 hours (Zn + chromate passivation)
  Applications: fasteners, brackets, sheet metal parts
  Bath: alkaline (cyanide or non-cyanide) or acid sulfate/chloride
  Environmental: cyanide baths being replaced; hexavalent chromate passivation
    now largely replaced by trivalent chromate (EU RoHS compliance)

NICKEL PLATING:
  Purpose: decorative + corrosion protection; wear resistance
  Mechanism: barrier protection only (not sacrificial) → complete coverage essential
  Decorative: bright nickel (organic brighteners) + thin chrome topcoat
  Engineering: thicker deposits; autocatalytic (electroless) for uniform coverage
  Applications: automotive trim, firearms, electronic contacts, molds
  Electroless nickel (EN):
    No current needed; uses reducing agent (hypophosphite) in bath
    Deposits uniformly on any conductive surface (no current density variation)
    Phosphorus content: 2–14% → affects hardness, corrosion resistance, magnetism
    Med-P EN (6–9% P): balance of properties → most common
    High-P EN (>10% P): amorphous; excellent corrosion resistance; non-magnetic

CHROME PLATING:
  DECORATIVE CHROME (very thin: 0.1–0.3 μm):
    Over nickel undercoat → provides brightness and thin corrosion protection
    High reflectance (automotive trim)
    Traditional: hexavalent CrO₃ bath → now being replaced by trivalent Cr (lower toxicity)

  HARD CHROME (25–500 μm):
    Purpose: wear resistance, low friction, corrosion resistance
    Industrial shafts, hydraulic cylinders, dies, printing rolls
    Hardness: 900–1000 HV
    Environmental: hexavalent Cr is carcinogenic → REACH regulation in EU
    Replacement candidates: HVOF WC-Co; electroless Ni-P; plasma spray; TiN PVD

GOLD PLATING:
  Electronics: prevent oxidation on contact surfaces (0.05–3 μm)
  Jewelry: aesthetic (flash gold = 0.05 μm; heavy gold = 1–3 μm)
  Medical: biocompatible; corrosion immune
  Gold bath: gold cyanide complex (alkaline); pure gold (25 karat) or alloys
  Hard gold: alloyed with Co or Ni → 200–300 HV vs 60 HV pure gold → contact durability
```

---

## Anodizing

```
ANODIZING MECHANISM:

  Electrolytic process: workpiece is the ANODE (opposite of electroplating)
  Electrolyte: sulfuric acid (H₂SO₄) — most common; phosphoric, oxalic, chromic also used
  At anode (aluminum workpiece):
    2Al + 3H₂O → Al₂O₃ + 6H⁺ + 6e⁻
    → Porous oxide layer grows into + out of surface
  At cathode: 2H⁺ + 2e⁻ → H₂

OXIDE LAYER STRUCTURE:
  Two zones:
    Barrier layer: dense, non-porous, ~10–20 nm, at metal interface
    Porous layer: columnar cells with central pore; grows outward
  Pore diameter: ~10–25 nm (sulfuric acid)
  Cell size: ~100 nm
  → Pores: site for dyeing (color anodize) and sealing

TYPES:
  TYPE I (Chromic acid anodize): 0.5–7.5 μm; lightest, most ductile; aerospace
  TYPE II (Sulfuric acid anodize): 5–25 μm; standard decorative + corrosion
  TYPE III (Hard anodize / hardcoat): 25–100 μm; dense; hard (400–600 HV)

HARD ANODIZE (Type III):
  Low temperature (0–5°C) H₂SO₄; high current density
  → Slower oxide growth at lower temperature → denser, harder oxide
  Hardness: 400–600 HV (harder than most steels)
  Applications: aircraft parts, hydraulic pistons, gears (light load), textile machinery
  Limitation: reduces fatigue life (tensile residual stress in outer oxide)

SEALING:
  After anodize: pores must be sealed to close corrosion path
  Hot DI water seal: 96–100°C water → boehmite (γ-AlO·OH) closes pores
  Nickel acetate seal: better corrosion resistance than water seal
  Mid-temperature seal (60–75°C Ni): balances sealing quality + energy
  PTFE seal: added lubricity → reduces friction for sliding applications

DYEING:
  Before sealing: water-soluble dyes absorbed into open pores
  Gold, black, red, blue — standard colors
  Anodize color is in the oxide layer → does not wear off like paint
  "Natural" (clear) anodize: no dye; silver-gray appearance
```

---

## Powder Coating

```
POWDER COATING PROCESS:

  1. Surface preparation: blast + phosphate or chromate pretreat (critical for adhesion)
  2. Electrostatic spray gun: powder (charged at 50–100 kV) → attracted to grounded part
     OR fluidized bed: part preheated → dipped in fluidized powder tank → powder adheres
  3. Cure oven: 150–230°C for 10–20 min → powder melts, flows, crosslinks → film

POWDER TYPES:
  THERMOSETTING (most common):
    Epoxy: excellent adhesion + chemical resistance; poor UV → indoors
    Polyester (TGIC): outdoor durable; UV resistant; most architectural + automotive
    Polyurethane: flexible; good chemical resistance; OEM automotive
    Epoxy-polyester hybrids: interior use; good flow; lower cost

  THERMOPLASTIC:
    Nylon, PVC, polyethylene: thicker coatings; re-melted; used for tool handles, wire racks

ELECTROSTATIC MECHANISM:
  Corona charging: high-voltage electrode → corona discharge → ionizes air → charges powder
  Tribocharging: friction with PTFE gun barrel → charge by triboelectricity
  Charged particles: attracted to grounded (or oppositely charged) workpiece
  Faraday cage effect: recessed areas shield from charging → difficult to coat deep cavities
  → Workaround: electrostatic flocking, higher voltage, or different gun geometry

ADVANTAGES vs LIQUID PAINT:
  No solvents → lower VOC emissions → more environmentally favorable
  Single coat adequate (no primer + topcoat for many applications)
  90%+ transfer efficiency (vs 30–50% for spray paint)
  More uniform film; no runs/drips
  Thicker film (50–100 μm vs 25–50 μm paint) → more durable

LIMITATIONS:
  Minimum film thickness: ~50 μm → not suitable for precision tolerances
  Color change: time-consuming (entire gun system must be cleaned)
  Not suitable: heat-sensitive substrates; complex curves (Faraday cage); very thick parts
  Touch-up: difficult (powder doesn't blend with existing coat)
```

---

## Thermal Spray

```
THERMAL SPRAY — PRINCIPLE:
  Feedstock (powder, wire, or rod) → heated to molten or semi-molten state
  → Propelled by gas jet → impacts substrate → spreads → solidifies ("splat")
  → Successive splats build up a lamellar deposit

PROCESSES:

  HVOF (High Velocity Oxy-Fuel):
    Fuel (kerosene or hydrogen) + oxygen → combustion chamber at high pressure
    Exit velocity: 500–1000 m/s (supersonic) at ~2700°C
    → Very high particle velocity → excellent bond strength (~70 MPa)
    → Low temperature at substrate → minimal oxidation; low porosity (~0.5%)

    WC-10Co4Cr (tungsten carbide-cobalt-chromium):
      → Hardness: 1000–1100 HV
      → Wear resistance: best available by thermal spray
      → Applications: pump components, aircraft landing gear, paper industry
      → Replaces electroless nickel and hard chrome for many wear applications

  PLASMA SPRAY:
    Plasma arc (argon + hydrogen): ~8,000–15,000°C (hottest available)
    → Melts highest melting point materials (ceramics, refractory metals)
    → Lower particle velocity than HVOF → higher porosity (~5–15%)
    → Higher temperature capability

    Thermal Barrier Coatings (TBC) — yttria-stabilized zirconia (YSZ):
      → 7–8% Y₂O₃ → stabilizes tetragonal phase → thermal cycling resistant
      → Thermal conductivity: ~2 W/m·K (vs steel 50; Al₂O₃ 30)
      → Gas turbine blade TBC: allows combustion gas T above alloy melting point!
        Metal substrate: ~1000°C; combustion gas: ~1400°C; TBC thermal gradient: 150–200°C
      → MCrAlY bond coat (M=Ni/Co; Cr; Al; Y): Al₂O₃ TGO (thermally grown oxide)
        → TBC adhesion via TGO; failure = TGO spallation at cycling (Tmax and ΔT critical)

  FLAME SPRAY (older, lower performance):
    Oxy-acetylene flame; lower velocity; higher porosity; lower bond strength
    Still used: simple coatings, low-budget, manual repair

THERMAL SPRAY COATING PROPERTIES:
  Lamellar (splat) microstructure → anisotropic properties
  Porosity: 0.5% (HVOF) to 15% (flame)
  Bond strength: 20–70+ MPa (depends on process + surface prep)
  Residual stress: compressive (HVOF); tensile (plasma)
  → Tensile residual stress + porosity → fatigue degradation; must consider in design
```

---

## PVD and CVD Coatings

```
PVD (Physical Vapor Deposition):
  Material source → vapor → deposits on substrate in vacuum chamber
  Substrate temperature: 200–500°C (low → can coat HSS tools)

  METHODS:
    Evaporation: resistive or electron beam heating of target → evaporation
    Sputtering: argon ion bombardment of target → target atoms ejected → deposit
    Arc evaporation (cathodic arc): arc on target → ionized plasma → dense coating

  REACTIVE PVD:
    Nitrogen (N₂) or carbon-containing gas added → reacts with target metal
    Ti target + N₂ → TiN (gold color, 2300 HV)
    Ti + Al + N₂ → TiAlN (dark gray, 3300 HV, better high-temp stability)
    Cr + N₂ → CrN (silver, 1750 HV, better chemical resistance)
    Ti + C₂H₂ → TiC/TiCN (high hardness, good adhesion)
    DLC (diamond-like carbon) + CH₄ → amorphous carbon → 3000+ HV; very low friction

  COATING THICKNESS: 1–5 μm (very thin → minimal dimensional change)
  HARDNESS: 1700–3500 HV (vs WC 1600 HV; steel tools 65 HRC = 832 HV)
  APPLICATIONS: cutting tools, forming dies, gears, medical implants

CVD (Chemical Vapor Deposition):
  Reactant gases flow into hot chamber → react at substrate surface → deposit
  Temperature: 900–1100°C → too hot for HSS; used on cemented carbide only

  TiC: TiCl₄ + CH₄ → TiC + 4HCl (1000°C)
  TiN: TiCl₄ + N₂ + H₂ → TiN + HCl (1000°C)
  Al₂O₃: AlCl₃ + 3/2 H₂O → Al₂O₃ + 3HCl (1000°C)

  CVD advantages vs PVD:
    Thicker coatings (5–20 μm) → longer tool life
    Better adhesion (metallurgical bond; higher temperature)
    Can coat complex 3D shapes uniformly (gas-phase → all surfaces)
    Al₂O₃ possible: excellent at high cutting temps → hardened steel + cast iron

  Multilayer CVD (e.g., TiN/TiCN/Al₂O₃/TiN):
    Combines: TiCN (toughness transition) + Al₂O₃ (hot hardness) + TiN (wear indicator)
    Standard on most commercial carbide inserts
    Gold TiN topcoat: visual wear indicator — when gold disappears, coating worn

PVD vs CVD SELECTION:
  HSS, cobalt steel tools → PVD only (500°C vs HSS Ac temp ~600°C)
  WC carbide inserts → CVD (higher temp capability; thicker; Al₂O₃ possible)
  Precision tolerance parts → PVD (thinner deposit; less dimensional change)
  Complex geometry → CVD (uniform gas-phase deposition)
```

---

## Tribology

```
TRIBOLOGY: friction, wear, and lubrication — the science of interacting surfaces in relative motion

FRICTION:
  Amontons' laws (1699; formalized by Coulomb):
    1. Friction force ∝ normal load (F_f = μ × F_N)
    2. Friction force independent of apparent contact area
    3. Kinetic friction < static friction (approximately; not universally true)

  PHYSICAL MECHANISMS:
    Adhesion: molecular-level bonding at asperity contacts → shearing adhesive junctions
    Ploughing: harder asperities plow grooves in softer surface → deformation energy
    Real contact area << apparent contact area
    → At microscale, only asperities contact → "real area" much smaller than geometric
    → Adhesion at asperities: μ = τ / H where τ = shear strength; H = hardness

  FRICTION COEFFICIENTS (dry):
    Steel on steel: 0.4–0.8
    Steel on PTFE: 0.04–0.1
    DLC on DLC: 0.01–0.05 (near superlubricity)
    Lubricated steel: 0.05–0.15

WEAR MECHANISMS:
  Adhesive wear: material transfer between surfaces (galling; welding at asperities)
  Abrasive wear: harder particle or asperity plows softer surface
    Two-body: surface against abrasive surface (grinding)
    Three-body: abrasive particles between two surfaces (most damaging in practice)
  Fatigue wear: cyclic loading → subsurface crack nucleation → surface pitting (gears, bearings)
  Corrosive/oxidative wear: surface reaction products removed by wear → fresh surface exposed

ARCHARD WEAR LAW:
  V = K × L × W / H
  V = wear volume; K = dimensionless wear coefficient; L = sliding distance;
  W = normal load; H = hardness

  Higher hardness → lower wear (H in denominator)
  This is why hard coatings (TiN, WC-Co) dramatically reduce wear

LUBRICATION REGIMES (Stribeck curve):
  Boundary lubrication (thin film; asperity contact): μ = 0.1–0.5; chemical film protects
  Mixed (partial EHD): μ = 0.02–0.1; film partially separates surfaces
  Hydrodynamic (full film; no asperity contact): μ = 0.001–0.01; viscosity carries load
  EHD (elastohydrodynamic): high-pressure; film remains despite very high loads (gear teeth, rolling bearings)

VISCOSITY AND FILM THICKNESS:
  Viscosity index (VI): how viscosity varies with temperature (higher VI = less change)
  ISO VG grades: ISO VG 46 = 46 mm²/s at 40°C (turbine oil, hydraulic)
  SAE 10W-40: winter (cold cranking) + 40 at 100°C (multigrade)
  Film thickness (EHD): h_min ∝ η^0.6 × U^0.6 / W^0.2 (Hamrock-Dowson)
    → Film thickness increases with viscosity × speed; decreases with load
```

---

## Decision Cheat Sheet

| Goal | Process |
|------|---------|
| Corrosion protection, steel fasteners | Zinc electroplating + chromate passivation |
| Decorative + corrosion, automotive trim | Bright nickel + thin decorative chrome |
| Uniform coating on complex 3D geometry | Electroless nickel or CVD |
| Lightweight + hard + anodized Al | Type III hard anodize |
| Color powder coat, outdoor | TGIC polyester powder coat |
| Wear resistance on pump/shaft (hard chrome replacement) | HVOF WC-Co thermal spray |
| Thermal barrier, turbine blade | APS YSZ + MCrAlY bond coat |
| Wear resistance on cutting tools (HSS) | PVD TiAlN |
| Wear resistance on carbide inserts | CVD TiCN + Al₂O₃ multilayer |
| Fatigue life improvement | Shot peening (compressive residual stress) |

---

## Common Confusion Points

**Anodizing is not plating — the aluminum becomes the coating**
Electroplating deposits a foreign metal onto the substrate. Anodizing converts the aluminum surface into aluminum oxide in situ — the coating grows from and into the base metal. Anodize thickness measurements must account for the fact that approximately half the coating grows inward and half outward. The coating is the workpiece material transformed, not an addition.

**HVOF and plasma spray are not the same despite both being "thermal spray"**
HVOF uses supersonic velocity + moderate temperature → low porosity, high bond strength, best for WC-Co. Plasma spray uses very high temperature + moderate velocity → higher porosity, but can melt ceramics that HVOF cannot. They occupy different niches: WC-Co wear coatings → HVOF; TBC ceramics → plasma spray.

**PVD TiN on cutting tools does not simply make steel harder**
PVD TiN hardness (~2300 HV) is only relevant at the cutting edge where it contacts the workpiece. The coating also: reduces friction, provides thermal insulation, acts as a diffusion barrier (prevents steel-chip welding), and provides a visual wear indicator. The wear resistance improvement is from multiple mechanisms, not just hardness.

**Tribological wear coefficient K is not a material constant**
The Archard wear coefficient K depends on the tribological system (mating materials, lubricant, speed, temperature, contact geometry) — not just the material alone. A material with K = 10⁻³ in one tribological pair may have K = 10⁻⁶ in another. Wear data must always specify the test conditions.

**Electroless nickel and nickel electroplating are different in mechanism and properties**
Electroplating requires current; deposits at the cathode; deposits vary in thickness with current density distribution. Electroless nickel uses autocatalytic chemistry; deposits uniformly regardless of shape; contains 2–14% phosphorus (which changes its properties dramatically). The "nickel" in both cases is different materials: pure Ni vs Ni-P alloy.
