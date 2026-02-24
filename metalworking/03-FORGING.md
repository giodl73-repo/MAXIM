# Forging

## The Big Picture

Forging is **controlled plastic deformation** of metal in solid state using compressive force. The defining advantage over casting: the deformation aligns the grain structure with the part geometry, dramatically improving fatigue and impact properties.

```
FORGING: FORCE → PLASTIC DEFORMATION → GRAIN FLOW → SUPERIOR PROPERTIES

WHY FORGING BEATS CASTING FOR CRITICAL APPLICATIONS:

  CASTING:                          FORGING:
  ┌──────────────┐                 ┌──────────────┐
  │ ○ ○ ○ ○ ○ ○ │                 │ ──────────── │
  │ ○ ○ ○ ○ ○ ○ │   forge it →   │ ──────────── │ ← grain flow
  │ ○ ○ ○ ○ ○ ○ │                 │ ──────────── │   follows shape
  └──────────────┘                 └──────────────┘
  Random equiaxed grains            Elongated grains aligned
                                    with stress direction

  Fatigue life: forgings 2–3× better than castings for same alloy
  Impact resistance: forgings significantly better
  Tensile strength: comparable or slightly better
  Ductility: better
  Internal defects: fewer (no porosity, no inclusions from solidification)
```

---

## Temperature Regimes

### Hot Forging

```
HOT FORGING: deformation above recrystallization temperature
  Steel: 900–1200°C (above ~60% of melting point in °K)
  Aluminum: 350–500°C
  Titanium: 900–1000°C (narrow window → careful temp control)

BENEFITS:
  • Low flow stress → modest equipment tonnage needed
  • No work hardening → can deform to large strains without cracking
  • Recrystallization occurs during deformation → refined grain size
  • Easier to fill complex die geometry

DISADVANTAGES:
  • Scale (oxide) forms → surface contamination
  • Dimensional tolerance poor (±0.5–3mm) → often needs machining
  • Poor surface finish
  • Decarburization of steel surface (C burned off near surface)
  • Heating cost and handling complexity
```

### Cold Forging

```
COLD FORGING: deformation at room temperature (or mildly warm, < 30% Tm)

BENEFITS:
  • Work hardening → higher strength than annealed starting material
  • Excellent dimensional accuracy (±0.01–0.1mm)
  • Good surface finish — no scale
  • No heating cost
  • High production rate (can be automated)

DISADVANTAGES:
  • High flow stress → requires much more force (3–5× vs hot)
  • Limited to ductile materials (low-C steel, Al, Cu, soft alloys)
  • Formability limited: can't deform much before cracking → multiple passes needed
  • Intermediate annealing (softening) required between stages

PRODUCTS: bolts, nuts, screws, pins, bearing races, spark plug bodies
          (All of these are cold-headed or cold-forged at high volume)
```

### Warm Forging

```
WARM FORGING: intermediate temperature (typically 500–800°C for steel)

Compromise: lower flow stress than cold + better precision than hot
Eliminates or reduces scale
Increasingly used for precision components that need better properties than machining
```

---

## Open-Die Forging

Open-die (smith) forging uses flat or simple dies that don't enclose the workpiece. The metal flows freely laterally.

```
OPEN-DIE FORGING OPERATIONS:

FULLERING: reduce cross-section of a section
  Force applied through rounded "fuller" dies
  Metal spreads sideways + lengthens

UPSETTING (heading): reduce height, increase diameter
  Force applied axially
  Metal spreads radially
  Used: before closed-die to distribute material

DRAWING OUT: lengthen a bar
  Successive hammer blows advance along bar
  Cross-section reduces, length increases

SWAGING: reduce diameter of round bars/rods
  Rotating hammers or dies close around bar
  Used: tapered sections, reducing tube/rod ends

COGGING: break down large ingots
  Open-die forge to refine grain, eliminate cast structure
  Preliminary operation before more precise forging

MANDREL FORGING (hollow): core mandrel used to forge hollow cylinders
  Prevents collapse of internal bore while diameter is forged
```

```
HAND FORGING SEQUENCE (for a simple part):

  Billet → heat to forge temperature
  1. Upset to get width
  2. Draw out to get length
  3. Fuller transitions
  4. Bend if needed
  5. Finish with flat dies
  Inspect: grain flow follows shape → superior part
```

---

## Closed-Die (Impression Die) Forging

The workpiece is enclosed in a die set that defines the final shape. Flash (thin fin of excess metal) forms at the die parting line.

```
CLOSED-DIE FORGING PROCESS:

DIE DESIGN:
  Upper die + lower die — form cavity that defines part shape
  Draft angles (5–7°): allow part removal from die
  Flash gutter: groove at parting line that accommodates excess metal
  Die fill: metal must fill every cavity detail
  Parting line: where dies split — flash forms here

FORGING SEQUENCE FOR COMPLEX PART:
  1. Cut billet to correct weight (volume = finished part + flash + cleanup)
  2. Heat to forge temperature
  3. Multiple operations in sequence:
     Blocker die: rough shape (large draft, not net shape)
     Finisher die: final shape (close tolerances)
  4. Trim flash (punch and die at trim press)
  5. Often: shot blast + straighten + inspect
  6. Heat treat if required (normalize, Q+T)
  7. Machine critical surfaces (bore, bearing surfaces)

FLASH ROLE:
  Flash generates back-pressure → forces metal to fill die corners + ribs
  Without flash → metal escapes → die underfill → scrap
  Excess flash → trimming waste + extra force needed
  Flash is ~10–20% of billet weight → yield consideration
```

### Drop Hammer vs Hydraulic Press

```
COMPARISON:

DROP HAMMER (gravity + gravity + steam/pneumatic assisted):
  Energy stored in falling ram mass (50–5000 kg at 3–7 m/s)
  Impact: instantaneous force at high velocity
  Energy: typically 5–500 kJ per blow; multiple blows needed
  Effect: high strain rate → adiabatic heating + rapid deformation
  Best for: complex shapes where die fill benefits from impact energy
           high-alloy steels (die fill before cooling)
  Sound: extremely loud; vibration; not suitable for urban settings
  Typical applications: connecting rods, axles, gears

HYDRAULIC PRESS:
  Pressure applied slowly (5–50mm/s vs 3–7 m/s for hammer)
  Force: 1000–50,000 tonnes; controlled and sustained
  Energy: very high (limited only by press capacity and stroke)
  Effect: low strain rate → heat lost to dies → cooler metal
  Best for: titanium (sensitive to temperature loss in hammer);
           large forgings; isothermal forging
  Advantage: precise stroke control; can be automated; quieter
  Isothermal forging: heated dies = same temperature as metal → no heat loss
                      → very precise net-shape; typical for Ti aerospace parts

STRAIN RATE EFFECTS:
  High strain rate (hammer): adiabatic — deformation energy stays as heat
                              reduces flow stress; good for complex shapes
  Low strain rate (press): isothermal — heat dissipates to dies
                           increases flow stress; need larger press
```

---

## Grain Flow and Mechanical Property Advantage

The microstructural argument for forging over machining or casting:

```
GRAIN FLOW IN FORGING VS MACHINING:

Example: a crankshaft cheek

  MACHINED FROM BAR:
  ┌─────────────────┐
  │ ─────────────── │  grain runs straight through bar
  │ ─────────────── │  machining cuts across grains at fillets
  │ ─────────────── │  ← grain boundary cut perpendicular to stress = weakness
  └─────────────────┘

  CLOSED-DIE FORGED:
  ┌─────────────────┐
  │   ╭─────────╮   │  grain follows contour
  │ ──╯         ╰── │  grain flow wraps around fillet
  │                 │  ← stress runs along grain boundary = maximum strength
  └─────────────────┘

WHY GRAIN BOUNDARIES MATTER:
  Fatigue crack initiation prefers: grain boundaries cut perpendicular to stress
  If grain flow is parallel to maximum stress → crack must cross grain matrix
                                                not run along boundary
  → Fatigue life improvement: 2–5× in controlled studies

FATIGUE DATA (typical, same alloy, 4340 steel):
  Casting: fatigue life at given stress = baseline
  Machined from bar: ~1.5× better
  Forging (grain flow aligned): 2–3× better than casting

INDUSTRY PRACTICE:
  Safety-critical fatigue parts are ALWAYS forged:
  Aircraft landing gear, wing spars
  Automotive crankshafts, connecting rods, steering knuckles
  Marine propeller shafts
  Gas turbine disks (forged superalloy + special heat treat)
```

---

## Ring Rolling

Specialized forging process for hollow cylindrical parts (rings, flanges, bearing races).

```
RING ROLLING PROCESS:

  Starting piece: forged and pierced hollow disk (donut shape)

  RADIAL ROLL:
  ├── Main roll (driven) + mandrel roll (inside ring)
  ├── Ring rotates between rolls
  ├── Compression reduces wall thickness
  └── Ring diameter grows (conservation of volume)

  AXIAL ROLL (optional):
  └── Tapered axial rolls control ring height

OUTCOME:
  Ring grows in diameter while wall thins
  Continuous circumferential grain flow
  → Circumferential fatigue resistance (exactly what pressure vessels, flanges need)
  Can produce rings 10cm to 10m diameter

APPLICATIONS:
  Flanged pipe joints (pressure vessels, reactors)
  Bearing races (inner and outer)
  Turbine casing segments
  Gear blanks
  Structural rings for rocket nozzles

SEAMLESS vs WELDED RINGS:
  Welded ring (rolled plate → butt weld): lower cost, weld seam = potential weakness
  Ring-rolled: no seam, continuous grain, superior fatigue → chosen for high-stress
```

---

## Forging Design Rules

```
DESIGN FOR FORGABILITY:

1. Keep parting line in a plane (or simple surface)
   → Complex parting lines → die complexity → cost

2. Draft angles (away from parting line): 5–7° for steel, 3–5° for Al
   → Required for part removal without die damage

3. Avoid sharp corners (internal): prefer generous radii
   → Sharp internal corners = stress concentrations in die AND part
   → Minimum internal radius: 3–5mm typical

4. Wall thickness uniformity
   → Uneven sections → uneven cooling → distortion, residual stress

5. Grain flow direction consideration
   → Specify critical load direction; work with metallurgist on die design

6. Dimensional tolerances (hot forging):
   → Typically ±0.5–1.5mm as-forged
   → Machining allowance: 1.5–4mm on critical surfaces

7. Net-shape and near-net-shape (NNS) forging:
   → Precision (cold/warm) forging can achieve ±0.05mm
   → Reduces machining cost significantly
```

---

## Decision Cheat Sheet

| Requirement | Forging recommendation |
|-------------|------------------------|
| High fatigue life, critical part | Closed-die forge + aligned grain flow |
| Complex shape, high volume | Closed-die (impression die) hot forging |
| Simple shape, tight tolerance | Cold forging or precision warm forging |
| Very large part (> 10 tonnes) | Open-die forging |
| Ring or cylindrical hollow | Ring rolling |
| Titanium or high-alloy superalloy | Isothermal forging (heated dies, slow press) |
| Eliminate porosity from casting | Forge or at minimum hot work → refines grain |
| Fasteners (bolts, nuts) at volume | Cold heading (form of cold forging) |

---

## Common Confusion Points

**Forging requires flow — cracking is failure, not a defect tolerance**
Unlike casting defects (porosity, shrinkage) which may be present at acceptable levels, forging cracks are catastrophic. The process must either avoid cracking entirely or the part is scrapped. This is why material ductility (and forging temperature choice) is critical.

**Grain flow cannot be seen from outside the part**
The whole argument for forging's superiority requires that grain flow is actually aligned. In production, grain flow is verified by sectioning and etching a sample part (macro-etch) or by ultrasonic testing. A bad billet, wrong temperature, or incorrect die fill can all produce poor grain flow.

**Draft angles and parting lines add material, not just geometry**
Draft angles mean the forged part has more material than the final design requires — that material must be machined off. Parting line flash must be trimmed. This is why forging yield (useful metal fraction) is 80–90%, not 100%.

**Cold forging work hardening is not the same as heat treatment hardening**
Cold forging strengthens by dislocation accumulation (work hardening). Heat treatment hardens by microstructural transformation (martensite). Both raise hardness and strength; they operate by different mechanisms and have different heat sensitivity (work hardening is erased by annealing; tempered martensite is not, at low temperature).

**Ring rolling is forging, not rolling**
Despite the name "rolling," ring rolling is a forging process — it plastically deforms a solid ring, creating grain flow. Flat rolling (sheet rolling) stretches and thins flat stock by passing between flat rolls — that's more like drawing. The equipment looks similar; the process and products are quite different.
