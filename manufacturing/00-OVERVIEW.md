# Manufacturing — Landscape and Taxonomy

## The Big Picture

Manufacturing converts raw material into finished product. Every process choice is a tradeoff across the same axes: geometry achievable, material compatibility, volume economics, tolerance capability, and lead time.

```
RAW MATERIAL ──────────────────────────────────────────────────────► FINISHED PART
     │
     │  SUBTRACTIVE          FORMATIVE           ADDITIVE            JOINING
     │  (remove material)    (reshape material)  (add material)      (combine parts)
     │
     │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐
     │  │  Machining   │    │  Casting     │    │  FDM/SLA/    │    │  Welding    │
     │  │  Turning     │    │  Forging     │    │  SLS/DMLS    │    │  Brazing    │
     │  │  Milling     │    │  Rolling     │    │  Binder Jet  │    │  Adhesive   │
     │  │  Grinding    │    │  Extrusion   │    │  DED         │    │  Fastening  │
     │  │  EDM / ECM   │    │  Sheet Metal │    │              │    │             │
     │  └──────────────┘    └──────────────┘    └──────────────┘    └─────────────┘
     │        │                    │                   │                    │
     │   CNC / CAM            Tooling-heavy       Design freedom      Process qual
     │   Tight tolerance      High volume OK      Low volume OK       Metallurgy
     │   All hard materials   Near-net shape      Complex geometry    Joint strength
```

---

## The Four Primary Process Families

### Family 1 — Subtractive Manufacturing

Material starts oversized; cutting tools remove everything that is not the part.

```
┌────────────────────────────────────────────────────────────────────┐
│  SUBTRACTIVE PROCESSES                                             │
│                                                                    │
│  Turning          workpiece spins, tool feeds in                   │
│  (lathe)          → cylindrical geometry, OD/ID features          │
│                                                                    │
│  Milling          cutter spins, workpiece moves on table           │
│  (mill/machining  → 3-5 axis, prismatic and complex geometry       │
│   center)                                                          │
│                                                                    │
│  Grinding         Fine abrasive wheel → surface finish, hard mat   │
│  EDM              Spark erosion → hardened steel, complex cavities │
│  ECM              Electrochemical dissolution → burr-free, no HAZ  │
│  Laser Cutting    Focused beam → sheet metal, 2.5D only            │
│  Waterjet         Abrasive jet → thick plate, no heat-affected zone│
│  Broaching        Pulled/pushed multi-tooth tool → keyways, splines│
└────────────────────────────────────────────────────────────────────┘
```

### Family 2 — Formative Manufacturing

Material is plastically deformed into shape. No material removed (except flash/trim).

```
┌────────────────────────────────────────────────────────────────────┐
│  FORMATIVE PROCESSES                                               │
│                                                                    │
│  LIQUID-STATE (casting)                                            │
│    Sand Casting    Low tooling cost, large parts, rough surface    │
│    Die Casting     High tooling cost, high volume, tight tol (Al)  │
│    Investment Cast Near-net shape, complex geometry, thin walls    │
│    Injection Mold  Thermoplastics, high volume, excellent finish   │
│    Lost Foam       Evaporative pattern → complex geometry, metals  │
│                                                                    │
│  SOLID-STATE (bulk deformation)                                    │
│    Forging         Compressive force → aligned grain, high strength│
│    Rolling         Mill rolls → plate, sheet, structural sections  │
│    Extrusion       Force through die → constant cross-section      │
│    Drawing         Pull through die → wire, tube, bar              │
│    Sheet Metal     Stamping, bending, deep drawing, hydroforming   │
│    Powder Metal    Press + sinter → near-net, porosity possible    │
└────────────────────────────────────────────────────────────────────┘
```

### Family 3 — Additive Manufacturing

Material deposited layer by layer. No tooling. Geometry freedom highest; material properties improving rapidly.

```
┌────────────────────────────────────────────────────────────────────┐
│  ADDITIVE PROCESSES                                                │
│                                                                    │
│  POLYMER                                                           │
│    FDM (FFF)      Fused filament → cheap, fast, anisotropic        │
│    SLA / DLP      Photopolymer resin → fine detail, brittle        │
│    SLS            Nylon powder, laser sintered → no supports       │
│    MJF            Multi-Jet Fusion (HP) → functional nylon, fast   │
│    PolyJet        Multi-material, rubber+rigid, fine features      │
│                                                                    │
│  METAL                                                             │
│    DMLS / SLM     Laser powder bed fusion → Ti/Ni/SS/Al            │
│    EBM            Electron beam powder bed → Ti, vacuum, no stress │
│    DED / LENS     Directed energy + wire/powder → large parts      │
│    Binder Jet     Inkjet binder + sinter → high volume, porous     │
│    WAAM           Wire arc additive → large structural metal parts  │
│                                                                    │
│  CERAMIC / COMPOSITE                                               │
│    Vat photopolymerization (ceramic slurry) → dental, implants     │
│    Continuous Fiber (Markforged) → CFRP in desktop form factor     │
└────────────────────────────────────────────────────────────────────┘
```

### Family 4 — Joining

Combining separately manufactured components.

```
┌────────────────────────────────────────────────────────────────────┐
│  JOINING PROCESSES                                                 │
│                                                                    │
│  FUSION WELDING      MIG (GMAW), TIG (GTAW), Laser, EB, Plasma    │
│  SOLID-STATE WELD    Friction Stir (FSW), Ultrasonic, Diffusion    │
│  BRAZING / SOLDERING Filler metal, capillary flow, below melt     │
│  ADHESIVE BONDING    Epoxy, structural acrylic, anaerobic          │
│  MECHANICAL          Bolts, rivets, press-fit, snap-fit, staking   │
│  PRESS/INTERFERENCE  Thermal expansion or hydraulic press          │
└────────────────────────────────────────────────────────────────────┘
```

---

## Process Selection Logic

```
                    PROCESS SELECTION TREE
                            │
            ┌───────────────┼──────────────┐
            │               │              │
        Volume?         Material?      Geometry?
            │               │              │
       Low  High     Metal Plastic    Simple Complex
            │               │              │
            │           Casting       ─────┘
            │           Forging       CNC 5-axis
            │           Injection     EDM/DMLS
            │           Molding
            │
       Low-vol:         High-vol:
       CNC machining    Die cast
       Additive proto   Stamping
       Investment cast  Injection mold
```

### Volume Economics

| Process | Tooling Cost | Per-Part Cost | Volume Sweet Spot |
|---------|-------------|---------------|-------------------|
| CNC Machining | Low ($0–$500 setup) | Medium-High | 1–500 |
| Sand Casting | Low ($200–$5K) | Medium | 1–1,000 |
| Investment Casting | Medium ($2K–$20K) | Medium | 100–5,000 |
| Die Casting | High ($10K–$100K) | Very Low | 10,000+ |
| Injection Molding | Very High ($5K–$500K) | Very Low | 10,000+ |
| FDM/SLA | $0 | Medium | 1–50 |
| DMLS/SLM | $0 (machine time) | High | 1–200 |
| Sheet Metal Stamping | High ($5K–$50K) | Very Low | 50,000+ |
| Forging | High ($5K–$50K) | Low | 1,000+ |

---

## Dimensional Accuracy Landscape

```
TIGHT ◄────────────────── ACHIEVABLE TOLERANCE ──────────────────► LOOSE

 ±0.001"  ±0.002"  ±0.005"  ±0.010"  ±0.020"  ±0.030"   ±0.050"
  25µm     50µm     125µm    250µm    500µm     750µm     1.25mm

  Grind    CNC Mill  CNC Turn  Invest.   Sand     Forging   Sand
  Hone     5-axis    Lathe     Cast      Cast     Stamping  Cast
  EDM      Jig Bore            Die Cast           FDM       Rough
  Wire EDM Boring              Injection          SLS
```

---

## The Manufacturing Enterprise Stack

```
┌─────────────────────────────────────────────────────────────────┐
│  BUSINESS LAYER                                                  │
│  ERP (SAP, Oracle)  MRP  Cost Accounting  Supply Chain PLM      │
├─────────────────────────────────────────────────────────────────┤
│  ENGINEERING LAYER                                               │
│  CAD (SolidWorks, CATIA, NX)     PLM (Windchill, Teamcenter)   │
│  CAM (Mastercam, HSMWorks, NX)   FEA (ANSYS, Abaqus)           │
│  GD&T / MBD (Model-Based Def.)   Simulation / DFM analysis     │
├─────────────────────────────────────────────────────────────────┤
│  PRODUCTION LAYER                                                │
│  MES (Manufacturing Execution System)  — real-time tracking     │
│  SCADA  ·  PLC programs  ·  Quality (CMM data, SPC charts)      │
│  Work orders  ·  Routing  ·  Scheduling  ·  Material tracing    │
├─────────────────────────────────────────────────────────────────┤
│  SHOP FLOOR LAYER                                                │
│  CNC machines  ·  Robots  ·  Inspection equipment (CMM, vision) │
│  Fixtures  ·  Tooling  ·  Material handling  ·  Conveyors       │
└─────────────────────────────────────────────────────────────────┘
```

**Bridge to software**: This stack parallels CI/CD. CAD/CAM = source code. MES = build server. CMM inspection = automated test suite. ERP = project/cost tracking. The feedback loops are measured in hours/days rather than seconds.

---

## Key Standards and Governing Bodies

| Standard | Domain |
|----------|--------|
| ASME Y14.5 | GD&T — geometric dimensioning and tolerancing |
| ISO 2768 | General tolerances for machined parts (linear + angular) |
| ISO 286 | Fits and limits — shaft/hole tolerance systems (H7/g6 etc.) |
| AWS D1.1 | Structural welding code — steel |
| ASTM | Material specifications (steel grades, aluminum alloys, polymers) |
| ISO 9001 | Quality management systems — generic |
| IATF 16949 | Automotive quality systems (builds on ISO 9001) |
| AS9100 | Aerospace quality systems (builds on ISO 9001) |
| ISO 1101 | Geometric tolerances (international GD&T equivalent) |
| ASME Y14.41 | Digital product definition / Model-Based Definition |

---

## Surface Finish Reference

```
Ra (µm)  Typical Process          Application
──────────────────────────────────────────────────────────
0.025    Superfinish / lapping    Bearing races, gauge blocks
0.1      Fine grinding, honing    Cylinder bores, precision slides
0.4      Fine turning, grinding   Shaft journals, sealing surfaces
0.8      Finish turning           General rotating parts
1.6      Semi-finish machining    Mating surfaces, moderate seals
3.2      Rough machining          General non-critical surfaces
6.3      Heavy turning, milling   Clearance surfaces
12.5     Rough milling            Non-functional surfaces
25       As-cast (investment)     Cosmetic issues only
50       Sand cast, forged        Requires machining if functional
```

---

## Directory Guide

| File | Content |
|------|---------|
| 01-GDT-TOLERANCING.md | ASME Y14.5 symbols, datum system, feature control frames |
| 02-MACHINING.md | Turning, milling, grinding — physics and parameters |
| 03-CNC-CAM.md | G-code, CAM workflow, toolpath strategies |
| 04-ADDITIVE.md | FDM/SLA/DMLS — process physics, material properties |
| 05-CASTING-FORMING.md | Casting metallurgy, forging, sheet metal |
| 06-JOINING.md | Welding processes, joint design, brazing, adhesives |
| 07-LEAN-TPS.md | Toyota Production System, waste, kanban, kaizen |
| 08-QUALITY.md | SPC, Six Sigma, MSA, ISO 9001, APQP |
| 09-INDUSTRY-40.md | IIoT, digital twin, smart manufacturing, cyber-physical |

---

## Decision Cheat Sheet

| I need to make... | Best process to consider |
|-------------------|--------------------------|
| One-off metal bracket, tight tolerance | CNC machining |
| 10,000 aluminum housings | Die casting |
| Complex internal cooling channels | Investment casting or DMLS |
| Functional prototype in 24 hours | FDM or SLA |
| Metal prototype, no tooling | DMLS/SLM or CNC |
| High-strength structural part | Forging + finish machining |
| Thin-wall steel enclosure, high volume | Sheet metal stamping |
| Plastic part, 100K+ volume | Injection molding |
| Hardened steel die insert | EDM (wire or sinker) |
| Large weldment (frame, structure) | MIG/TIG + machining |
| Titanium aerospace bracket, complex | DMLS or 5-axis CNC |
| Gear blank, high strength | Forging (then hobbing) |

---

## Common Confusion Points

**GD&T vs coordinate tolerancing**: ±0.010" on a hole location creates a square zone (side = 0.020"). GD&T position ⌀0.020" creates a circular zone — 57% more area for the same number. GD&T is not tighter per se, but it describes intent more accurately.

**Near-net shape vs net shape**: Near-net = minimal finish machining required. Net shape = no machining. Investment casting and PM are often near-net. "Net shape" claims always require scrutiny.

**Additive for production**: DMLS/SLM aerospace parts (GE LEAP fuel nozzles) are flight-qualified. FDM is still mostly prototype/tooling in critical applications — though Stratasys FDM with ULTEM is FAA-compliant for aircraft interiors.

**MES vs ERP**: ERP (SAP) owns cost, inventory, orders, and financials. MES owns real-time shop floor execution — machine utilization, work order tracking, quality holds, genealogy/traceability. They share data but serve different masters.

**Surface finish Ra vs Rz**: Ra is the arithmetic mean roughness — the average. Rz is the mean peak-to-valley height — more sensitive to surface defects. Bearing surfaces often specify Rz because a single burr can cause failure that Ra wouldn't catch.
