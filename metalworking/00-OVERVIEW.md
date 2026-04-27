# Metalworking — Overview

## The Big Picture

Metalworking is the value chain from ore in the ground to a precision component in a machine.
Every step either changes **composition**, **shape**, or **surface properties** — often all three.

```
ORE IN THE GROUND
        │
        ▼
┌────────────────────────────────────────────────────────────────┐
│  STAGE 1: EXTRACTION & REFINING                                │
│  Blast furnace / BOF / EAF (steel)                             │
│  Hall-Héroult (aluminum)   Flash smelting (copper)             │
│  Output: ingots, billets, slabs, cathodes                      │
└────────────────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────────────────┐
│  STAGE 2: PRIMARY SHAPING (near-net shape)                     │
│  Casting: sand / investment / die / continuous                 │
│  Forging: open-die / closed-die / ring rolling                 │
│  Rolling: hot strip mill, plate, structural sections           │
│  Extrusion: aluminum profiles, copper tube                     │
│  Output: castings, forgings, sheet, bar, rod, tube             │
└────────────────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────────────────┐
│  STAGE 3: SECONDARY SHAPING (precise geometry)                 │
│  Machining: turning / milling / drilling / grinding            │
│  Drawing: wire, tube (reduce cross-section + work harden)      │
│  Sheet metal: stamping, deep drawing, hydroforming             │
│  Output: machined parts, stampings, precision components       │
└────────────────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────────────────┐
│  STAGE 4: JOINING                                              │
│  Welding (SMAW/MIG/TIG/laser), Brazing, Soldering              │
│  Mechanical: bolts, rivets, press-fit                          │
│  Output: assemblies, structures                                │
└────────────────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────────────────┐
│  STAGE 5: HEAT TREATMENT & SURFACE FINISHING                   │
│  Anneal / Quench+Temper / Carburize / Nitriding                │
│  Electroplate / Anodize / PVD / Powder coat                    │
│  Output: final properties, corrosion resistance, appearance    │
└────────────────────────────────────────────────────────────────┘
        │
        ▼
PRECISION COMPONENT IN SERVICE
```

Key insight: **shape and properties are largely independent**. You can forge a shape (sets grain flow and near-net geometry), then heat treat it (sets hardness and strength), then grind it (sets final tolerances) — three separate transformations on the same part.

---

## Metals Taxonomy

```
METALS
├── FERROUS (iron-based, ~70% of all metal used industrially)
│   ├── Carbon Steel
│   │   ├── Low carbon (< 0.3% C): mild steel, structural — weldable, not hardenable
│   │   ├── Medium carbon (0.3–0.6% C): machinery, shafts — heat treatable
│   │   └── High carbon (> 0.6% C): springs, tools, blades — hardenable, brittle
│   ├── Alloy Steel (+ Cr/Mo/Ni/V/Mn)
│   │   ├── 4140 (Cr-Mo): tooling, shafts, gears — most-used engineering steel
│   │   ├── 4340 (Ni-Cr-Mo): aircraft undercarriage, high-strength critical parts
│   │   └── Tool steels (H13, D2, M2): dies, cutting tools, punches
│   ├── Stainless Steel (≥ 10.5% Cr forms passive Cr₂O₃ layer)
│   │   ├── 304/316 austenitic: corrosion resistant, non-magnetic, weldable
│   │   ├── 410/430 ferritic: lower cost, magnetic, less corrosion resistant
│   │   └── 17-4 PH: precipitation hardened, high strength + corrosion resistance
│   └── Cast Iron (2–4% C — mostly carbide or graphite precipitates)
│       ├── Gray iron: graphite flakes, good damping, cheap, brittle
│       ├── Ductile/nodular: spheroidal graphite, tougher than gray
│       └── White iron: iron carbide (Fe₃C), very hard, wear resistant
│
├── NON-FERROUS
│   ├── Aluminum (Al) — density 2.7 g/cc, corrosion resistant, recyclable
│   │   ├── 1xxx: pure Al, electrical conductors (very high conductivity)
│   │   ├── 2xxx (Cu alloy): aircraft (2024) — high strength, poorer corrosion
│   │   ├── 6xxx (Mg-Si): structural, extrudable, weldable (6061) — workhorse
│   │   └── 7xxx (Zn alloy): highest Al strength (7075) — aerospace, firearms
│   ├── Copper (Cu) — best electrical/thermal conductor among structural metals
│   │   ├── Brass (Cu-Zn): machinability, plumbing, marine hardware
│   │   └── Bronze (Cu-Sn, Cu-Al): bearings, marine propellers, coins
│   ├── Titanium (Ti) — 4.5 g/cc, corrosion immune, biocompatible
│   │   └── Ti-6Al-4V (Grade 5): aerospace, medical implants, consumer goods
│   └── Nickel (Ni) — high temperature, extreme corrosion resistance
│       └── Inconel 718, Hastelloy: gas turbine components, chemical plant
│
├── REFRACTORY (melting point > 2000°C)
│   ├── Tungsten (W, Tm = 3422°C): filaments, heavy alloy (kinetic penetrators)
│   ├── Molybdenum (Mo): high-temp tooling, electrode, alloying element in steel
│   └── Tantalum (Ta): chemical plant (acid-resistant), capacitors, implants
│
└── PRECIOUS (Au, Ag, Pt, Pd, Rh, Ir)
    └── Electronics contacts, catalytic converters, jewelry, reference standards
```

---

## Key Mechanical Properties

These appear throughout every module. You need this vocabulary to navigate the field.

| Property | Definition | Test Method | Why It Matters |
|----------|-----------|-------------|----------------|
| **Yield strength** | Stress at onset of permanent deformation | Tensile test (0.2% offset) | Design limit; parts must not yield in service |
| **UTS** (Ultimate tensile strength) | Peak engineering stress before fracture | Tensile test | Failure ceiling; basis for safety factors |
| **Hardness** | Resistance to indentation | Rockwell / Brinell / Vickers | Wear resistance; rough strength proxy |
| **Toughness** | Energy absorbed before fracture (area under stress-strain) | Charpy / Izod impact | Resistance to shock, crack propagation |
| **Ductility** | Plastic deformation before fracture | % elongation, % reduction in area | Formability; ductile warning before failure |
| **Fatigue strength** | Maximum cyclic stress without failure at N cycles | S-N (Wöhler) curve | Rotating shafts, springs — dominant failure mode |
| **Creep resistance** | Resistance to slow deformation under sustained load at elevated T | Creep test | Gas turbines, steam boilers, petrochemical |
| **Corrosion resistance** | Resistance to electrochemical degradation | Salt spray / polarization curves | Service life in hostile environments |

### The Hardness–Toughness Tradeoff

```
HIGH HARDNESS ◄──────────────────────────────────► HIGH TOUGHNESS
     ↑                                                      ↑
White iron, fully               Low carbon steel, pure copper,
hardened tool steel,            annealed aluminum, mild steel
ceramics, carbides              (absorbs energy, deforms
(wear-resistant, brittle,        plastically, won't crack
crack without warning)          under impact)

For steels specifically:
  More carbon → higher potential hardness after quench → lower toughness
  Quenched → hard, brittle martensite
  Tempered → trades some hardness back for toughness (controlled carbide precipitation)
  The quench-and-temper cycle is optimization along this tradeoff curve
```

---

## The Fe-C Phase Diagram — The Reason Steel Is Dominant

Steel's entire heat treatment capability traces to one structural fact:
**iron undergoes an allotropic transformation at 912°C**.

```
Temperature
   (°C)
  1538 ─── Liquidus line (melting)
  1495 ─── δ-ferrite upper field
  1394 ─── δ → γ (austenite) transformation
            FCC structure; high C solubility (~2%)
   912 ─── γ → α (ferrite) transformation  ← THE KEY POINT
            BCC structure; C solubility drops to ~0.02%
            Excess C must go somewhere → precipitates as Fe₃C (cementite)
            How fast you cool through this region controls microstructure:

  Equilibrium cooling (very slow):
    → pearlite (lamellar ferrite + cementite)
    → medium strength, machineable, weldable

  Rapid quench (miss the pearlite "nose"):
    → martensite (diffusionless shear transformation)
    → supersaturated, body-centered tetragonal lattice
    → very hard, high internal stress, brittle

  Temper martensite (reheat to 150–650°C):
    → fine carbide precipitation, stress relief
    → hardness drops slightly, toughness increases significantly
    → this is "tempered martensite" — the engineering sweet spot
```

Covered in depth in `07-HEAT-TREATMENT.md`.

---

## Trade Hierarchy

The metalworking industry has distinct occupational tiers, each adding value:

```
MINER / MINING ENGINEER
  Extract ore: iron ore (hematite Fe₂O₃), bauxite (Al), copper sulfides
        │
        ▼
SMELTER / METALLURGICAL ENGINEER
  Reduce ore to metal: blast furnace, EAF, Hall-Héroult
  Output: pig iron, aluminum ingots, copper cathodes
        │
        ▼
FOUNDER / FOUNDRY ENGINEER
  Cast shapes from molten metal: sand casting, die casting
  Output: near-net castings
        │
        ▼
SMITH / FORGE OPERATOR
  Shape hot or cold metal: forging, rolling, drawing
  Output: forgings, sheet, bar, rod
        │
        ▼
MACHINIST / CNC PROGRAMMER
  Achieve precision geometry: turning, milling, grinding
  Output: precision components to print
        │
        ▼
FINISHER / SURFACE ENGINEER
  Protect and condition surfaces: plating, anodizing, PVD, heat treat
  Output: production-ready components
```

---

## Process Selection Matrix

| Requirement | Best Process | Notes |
|-------------|-------------|-------|
| Complex geometry, low volume | Investment casting | Near-net; alloys including superalloys |
| Complex geometry, high volume (Al/Zn) | Die casting | Fast cycle; thin walls possible |
| High fatigue strength, critical part | Forging | Grain flow aligned to stress trajectory |
| Flat sheet, plate, structural sections | Rolling | Most cost-effective for flat/prismatic shapes |
| Long constant cross-section | Extrusion (Al) or rolling (steel) | Profiles, tubes, angles |
| Tight tolerances, any geometry | Machining (CNC) | Final finishing step; most expensive per kg |
| Thin-wall enclosures (automotive panels) | Deep drawing / stamping | Sheet metal; high-volume tooling |
| Dissimilar metal join | Brazing | Lower temp; less distortion than welding |
| Bulk hardness increase | Through-hardening (Q+T) | Uniform cross-section hardening |
| Surface hardness, tough core | Case hardening (carburize/nitriding) | Gears, camshafts |

---

## Module Map

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| `01-EXTRACTION-SMELTING.md` | Ore → metal | Blast furnace, BOF/EAF, Hall-Héroult, fire refining |
| `02-CASTING.md` | Liquid → shape | Sand, investment, die, continuous; shrinkage, porosity |
| `03-FORGING.md` | Hot deformation | Grain flow, dies, isothermal, ring rolling |
| `04-ROLLING-DRAWING.md` | Sheet, bar, wire | Hot/cold rolling, work hardening, temper designations |
| `05-MACHINING.md` | Precision geometry | Cutting theory, CNC, tool wear, speeds and feeds |
| `06-WELDING.md` | Joining | SMAW/MIG/TIG, HAZ metallurgy, distortion, NDT |
| `07-HEAT-TREATMENT.md` | Microstructure | Fe-C diagram, TTT/CCT, Q+T, case hardening |
| `08-SURFACE-FINISHING.md` | Surfaces | Electroplate, anodize, PVD/CVD, thermal spray |
| `09-PRECISION-METROLOGY.md` | Measurement | ISO fits, GD&T, CMM, gauge R&R, SPC |

---

## Bridges to Adjacent Fields

| Field | Connection |
|-------|-----------|
| `materials/` | Materials science explains *why* microstructure determines properties |
| `mechanical/` | Machine design specifies what tolerances and materials must be achieved |
| `structural/` | Structural engineering selects steel grades and weld specifications |
| `semiconductor-manufacturing/` | Precision machining of wafer stages; ultra-flat lapping; cleanroom requirements |
| `jewelry/` | Small-scale casting, forming, soldering — same principles, finer scale |
| `construction-materials/` | Structural steel, rebar, wire rope are primary metalworking outputs |

---

## Decision Cheat Sheet

| Goal | Process |
|------|---------|
| Ore → bulk metal | Pyrometallurgy: blast furnace / EAF / Hall-Héroult |
| Complex shape, good surface finish | Casting (investment or die) |
| High fatigue life (gears, crankshafts, aircraft) | Forging + heat treat |
| Sheet, plate, structural sections | Rolling |
| Precision holes, threads, surfaces | Machining |
| Join metals permanently | Welding (or brazing for dissimilar / thin) |
| Increase hardness, keep shape | Heat treatment (Q+T or case hardening) |
| Corrosion protection + wear resistance | Electroplate / anodize / PVD |
| Measure to microns, document tolerances | CMM + GD&T + SPC |

---

## Common Confusion Points

**Hardness ≠ Strength ≠ Toughness**
These are related but independent. Cast iron is hard but brittle (low toughness). Copper is neither hard nor very strong but has excellent toughness. Tool steel after quench is hard but will crack under impact; after tempering it trades some hardness for usable toughness.

**Forging changes microstructure, not just shape**
A casting has random, equiaxed grain structure. A forging has elongated grains aligned with die-flow direction. For a connecting rod under bending fatigue, a forging can be 2–3× more fatigue-resistant than a geometrically identical casting — the grain boundaries run with the stress lines, not across them.

**CNC is a control system, not a process**
CNC (Computer Numerical Control) is how you command a machine tool. The cutting process underneath is still turning, milling, drilling, or grinding. "CNC machining" = machining with computer-controlled tool paths.

**Welding a heat-treated part locally resets the heat treatment**
The heat-affected zone around a weld sees temperatures that convert tempered martensite back to austenite, then re-harden unpredictably on cooling. This is why high-strength steel welding requires preheat, controlled interpass temperature, and post-weld heat treatment (PWHT).

**Grade numbers are not standardized globally**
"4140 steel" is an AISI/SAE grade. EN (European), JIS (Japanese), and DIN (German) use completely different designations for equivalent compositions. Always verify by chemical analysis (% C, Cr, Mo), not by grade number alone.
