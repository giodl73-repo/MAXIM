# Casting

## The Big Picture

Casting is **solidification of molten metal in a shaped mold**. It's the most shape-versatile of all metalworking processes — you can produce almost any geometry — but it's constrained by solidification physics: shrinkage, gas porosity, and segregation.

```
CASTING PROCESS TAXONOMY

Feed form: LIQUID METAL
                │
                ├── SAND CASTING — expendable sand mold, reusable pattern
                │   Good for: large, complex iron/steel/Al castings; low volume
                │   Limitations: rough surface finish, dimensional tolerance ~±1mm
                │
                ├── INVESTMENT CASTING (lost-wax) — expendable ceramic mold
                │   Good for: complex geometry, superalloys, thin walls, tight tolerances
                │   Limitations: expensive tooling (wax dies), slow, small size typically
                │
                ├── DIE CASTING — permanent steel die, high-pressure injection
                │   Good for: Al/Zn/Mg, high volume, good surface finish
                │   Limitations: ferrous metals mostly excluded (die life), high tool cost
                │
                ├── PERMANENT MOLD (gravity die) — permanent metallic mold, gravity fill
                │   Good for: Al, Cu alloys, medium complexity, better than sand
                │   Limitations: less complex than investment; die cost
                │
                ├── CENTRIFUGAL CASTING — rotation forces metal outward
                │   Good for: pipes, cylindrical hollow parts, bi-metallic rings
                │
                └── CONTINUOUS CASTING — steady-state process for steel/Al
                    Good for: flat-rolled and long products (slabs, billets, blooms)
                    Dominant process: >95% of world steel is continuously cast
```

---

## Sand Casting

### Process Mechanics

```
SAND CASTING SEQUENCE:

1. PATTERN CREATION
   Permanent pattern (wood, plastic, aluminum) dimensioned with:
   • Draft angle (1–3°): enables withdrawal from sand without collapsing
   • Machining allowance: extra material where precision surfaces needed
   • Shrinkage allowance: pattern is larger than desired casting
     (Al shrinks ~1.3%, steel ~2%)

2. MOLD MAKING
   Sand mixture packed around pattern in two halves (cope and drag)
   Parting line: the split plane between cope and drag
   Cores (sand shapes on metal/ceramic supports) create internal cavities

3. MOLD SYSTEM DESIGN
   Gating system: controls metal entry
   ┌──────────────────────────────────────────────────┐
   │  Pouring cup → sprue (vertical) → runner         │
   │  (horizontal) → gate (into cavity) → casting     │
   └──────────────────────────────────────────────────┘
   Risers: reservoirs above hot spots that feed liquid metal
           as the casting solidifies and contracts
           (if riser is omitted → shrinkage void inside casting)
   Chills: metal inserts to accelerate local solidification
           (used near risers to force directional solidification toward riser)

4. POURING
   Metal poured at appropriate temperature (superheat above liquidus)
   Too hot: gas pickup, shrinkage, grain coarsening
   Too cold: misruns (metal solidifies before filling)

5. SHAKEOUT, FETTLING
   Sand broken out; risers and gates cut off; surface cleaned (shot blast)
   Internal cores removed; parting line flash ground off
```

### Sand Types

| Sand type | Binder | Hardening | Notes |
|-----------|--------|-----------|-------|
| Green sand | Bentonite clay + water | Moisture + pressing | Most common; reusable; poor dimensional accuracy |
| Resin-bonded (no-bake) | Phenolic/furan resin + acid | Chemical cure | Better accuracy; not reusable; good for steel |
| Shell molding | Phenolic resin | Heat cure against heated die | Good accuracy; thin shell; high-volume iron |
| CO₂ / sodium silicate | Na₂SiO₃ | CO₂ gas blows | Good core making; high temp resistance |

---

## Investment Casting (Lost-Wax)

The oldest precision casting process (used for bronze artifacts ~3000 BCE; now makes turbine blades).

```
INVESTMENT CASTING PROCESS:

1. WAX PATTERN INJECTION
   Wax injected into metal die → wax patterns, accurate to final geometry
   Multiple wax patterns attached to a wax "tree" (gating system)

2. CERAMIC SHELL BUILDING
   Wax tree dipped in colloidal silica slurry → stucco (ceramic grit) applied
   Repeated 8–15 times → ceramic shell ~6–12mm thick
   Each coat dried before next (several hours each)

3. DEWAXING
   Shell placed in steam autoclave or flash fire furnace
   Wax melts and drains out (hence "lost wax")
   Shell fired at ~1000°C to cure ceramic

4. CASTING
   Molten metal poured into hot shell (often at 800–1100°C)
   Shell preheating prevents: thermal shock cracking + premature solidification
   For superalloys (turbine blades): cast under vacuum to prevent oxidation

5. SHELL REMOVAL
   Ceramic shell broken away (mechanical + water blasting)
   Individual parts cut from tree
   Finishing: blast, grind, inspect, machine (if required)

Key advantage over sand: wall thickness down to 1mm;
  tolerances ±0.1–0.2mm; complex internal passages possible

Turbine blade casting: directionally solidified (DS) and single-crystal (SX):
┌────────────────────────────────────────────────────────────────┐
│ CONVENTIONAL:   random polycrystalline grain structure          │
│   Grain boundaries perpendicular to stress axis → creep failure│
│                                                                 │
│ DIRECTIONAL SOLIDIFICATION (DS): grain boundaries parallel to  │
│   blade axis → eliminates transverse boundaries → better creep │
│                                                                 │
│ SINGLE CRYSTAL (SX): no grain boundaries at all                │
│   Process: withdraw slowly from melt → crystal grows upward    │
│   All modern high-temperature gas turbine stage-1 blades are SX│
│   Gas path temperature: 1700°C+ (above nickel melting point ~1340°C)│
│   Metal temperature: ~950-1050°C — kept below melting by:         │
│     (a) ceramic TBC (ZrO2-based, ~150μm) on blade surface         │
│     (b) internal cooling passages: compressor bleed air flows     │
│         through channels and film-cooling holes in blade wall      │
│   Enabled by: TBC + internal convective + film cooling combined   │
└────────────────────────────────────────────────────────────────┘
```

---

## Die Casting

High-pressure injection of molten metal into a hardened steel die.

```
DIE CASTING CYCLE:

1. Die closes (hydraulically clamped: 200–3000 tonnes)
2. Metal injected at high pressure (70–700 MPa) and velocity (30–120 m/s)
3. Solidification: rapid (die is water-cooled); ~0.5–5 seconds
4. Die opens; part ejected by pins
5. Die lubricated for next shot; scrap trimmed (flash)

Cycle time: 30 seconds to several minutes per part
Production rate: 100–1000 parts/hour depending on size

METALS:
  Aluminum (most common): ~350°C pour, excellent fluidity, good strength/weight
  Zinc (Zamak): ~420°C, lowest cost tooling, thin walls, good plating
  Magnesium: lightest structural metal; growing use in automotive/electronics
  Copper/brass: possible but high die wear; usually permanent mold instead

LIMITATIONS:
  • Ferrous metals (steel, iron): too high melting point → die life days/weeks
    → sand or investment casting for steel
  • Porosity: turbulent fill traps gas → cannot heat treat (gas expansion causes blistering)
    Vacuum die casting reduces this; "squeeze casting" applies pressure during solidification
  • Wall thickness minimum: ~0.8mm (Al), ~0.4mm (Zn)
  • Parting line flash unavoidable → trimming required

SURFACE FINISH: Ra 0.8–3.2 µm (can be machined, plated, anodized)
DIMENSIONAL TOLERANCE: ±0.1–0.15mm typical (better than sand)
```

---

## Continuous Casting of Steel

Before ~1970, most steel was poured into static ingot molds, cooled, and then reheated for rolling. Continuous casting (concast) eliminates the ingot stage entirely.

```
CONTINUOUS CASTING PROCESS:

Liquid steel from ladle
    │
    ▼ Tundish (buffer vessel — temperature/flow control)
    │
    ▼ Water-cooled copper mold (oscillates to prevent sticking)
    │  Primary solidification: skin forms as mold extracts heat
    │  Liquid pool inside solid shell may extend 10–15m below mold
    │
    ▼ Secondary cooling: water sprays on strand surface
    │  Successive rolls support and straighten the strand
    │
    ▼ Torch cutting at desired length

STRAND FORMATS:
  Slab (150–300mm × 900–2100mm): for flat-rolled products (sheet, plate)
  Bloom (150–400mm square): for structural, rails, large sections
  Billet (60–150mm square): for bar, rod, wire, small sections
  Round: for seamless tube making

ADVANTAGES OVER INGOT CASTING:
  • No ingot reheating step → energy saving ~20%
  • Higher yield (~98% vs ~85%): no crop losses from shrinkage cavities
  • More uniform composition: less macro-segregation
  • Faster: continuous production matches blast furnace output
  • Enables thin slab casting (CSP, ISP): 50–90mm slabs go direct to hot rolling
    → "Endless" strip production: cast-then-roll in one continuous pass

DEFECTS:
  • Breakout: shell rupture → liquid steel floods → emergency stop
    (prevented by: mold level control, oscillation pattern, casting speed control)
  • Longitudinal cracks: from uneven primary cooling or mold taper
  • Segregation: solutes partition toward centerline during solidification
  • Oscillation marks: surface marks from mold oscillation
```

---

## Casting Defects and Remediation

```
DEFECT TAXONOMY:

POROSITY
├── Shrinkage porosity:
│   Cause: metal contracts on solidification (~2–8%); last liquid to solidify
│          in isolated pockets has nowhere to draw from
│   Appearance: ragged, internal voids; typically at hot spots
│   Prevention: proper riser design (feed liquid metal to hot spots)
│               directional solidification toward riser
│               chills to shift thermal gradient
│
└── Gas porosity:
    Cause: dissolved gas (H₂ from moisture; N₂ from air) comes out of solution
           as metal cools and solubility drops; trapped as spherical bubbles
    Appearance: round, smooth voids; subsurface or distributed
    Prevention: degas molten metal (argon purging, vacuum degassing);
                dry molds, dry tools, dry alloy additions

INCLUSIONS
  Metallic: undissolved alloy particles, intermetallics
  Non-metallic: oxide films (common in Al), slag, refractory particles
  Prevention: filtration (ceramic foam filters in gating system);
              degassing; clean scrap charge

COLD SHUTS / MISRUNS
  Cause: two metal streams meet but have cooled below fusion temperature
         → don't bond → surface defect
  Or: metal runs out of fluidity before filling mold
  Prevention: higher pouring temperature; faster fill; larger gates; vacuum assist

HOT TEARS / HOT CRACKING
  Cause: solidifying metal is weak in semi-solid state; if casting cannot
         contract freely (constrained by mold or core), it tears
  Appearance: irregular crack, usually at hot spot
  Prevention: adjust alloy (avoid hot-tear-prone compositions);
              better mold/core design to allow contraction; reduce constraint

SEGREGATION
  Cause: solute elements redistribute during solidification (partition coefficient)
  Micro-segregation: between dendrite arms → homogenized by annealing
  Macro-segregation: centerline enrichment; inverse segregation at surface
  Prevention: faster solidification (finer dendrite arm spacing);
              electromagnetic stirring in continuous casting
```

---

## Casting Process Comparison

| Process | Volume | Tolerance | Surface finish | Materials | Unit cost |
|---------|--------|-----------|----------------|-----------|-----------|
| Sand (green sand) | Low | ±1–3mm | Rough (Ra 12–25µm) | All metals | Very low tooling, moderate part |
| Sand (resin-bonded) | Low-medium | ±0.5–1mm | Moderate | All metals | Low tooling |
| Investment | Low-medium | ±0.1–0.3mm | Good (Ra 1.6–3.2µm) | All metals, superalloys | High tooling, high part |
| Die casting | High | ±0.1–0.15mm | Good (Ra 0.8–3.2µm) | Al, Zn, Mg | High tooling, low part |
| Permanent mold | Medium | ±0.2–0.5mm | Moderate (Ra 3–6µm) | Al, Cu, Mg | Moderate tooling |
| Continuous | Very high (only slabs) | — | N/A (rolled) | Steel, Al | Very low |

---

## Decision Cheat Sheet

| Requirement | Best casting process |
|-------------|---------------------|
| Large iron/steel part, low volume | Sand casting |
| Complex geometry, thin walls, tight tolerance | Investment casting |
| High volume aluminum parts (automotive) | Die casting |
| Steel slab for sheet/plate production | Continuous casting |
| Single-crystal turbine blade | Investment casting (SX withdrawal) |
| Internal passages (engine block cooling) | Sand casting with cores |
| Minimize porosity in structural Al | Squeeze casting or vacuum die casting |

---

## Common Confusion Points

**Risers are not vents — they are liquid metal reservoirs**
A riser's job is to feed molten metal into the shrinking casting as it solidifies. It must remain liquid longer than the section it feeds. Risers are sized and positioned to ensure directional solidification toward the riser.

**Die casting cannot make steel parts**
The copper die tooling can only survive a few hundred shots of steel at 1550°C+ before warping. Die casting is limited to lower-melting alloys. Steel castings are made by sand or investment processes.

**Investment casting ≠ high-volume cheapness**
Investment casting is expensive (wax patterns, 15-coat ceramic shells, labor-intensive). It's chosen when geometry complexity or material requirements (superalloys) make no other process feasible. Unit costs for turbine blades can be thousands of dollars.

**Continuous casting doesn't produce finished shapes**
Continuous casting makes slabs, blooms, or billets — these are then hot-rolled, forged, or drawn to final shape. It replaces ingot casting; it doesn't replace subsequent working processes.

**Porosity is not always a defect**
In non-structural applications (decorative, low-stress), some porosity is acceptable. The critical question is whether porosity will be in a stress-bearing section. NDT (X-ray, CT scanning) reveals internal porosity; acceptance criteria depend on the application standard (aerospace ASTM, automotive, etc.).
