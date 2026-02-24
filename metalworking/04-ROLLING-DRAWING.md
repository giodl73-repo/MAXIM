# Rolling and Drawing

## The Big Picture

Rolling and drawing are **continuous deformation processes** that convert large primary shapes (slabs, billets, ingots) into useful product forms (sheet, plate, bar, rod, wire, structural sections). They are the highest-volume metalworking processes globally — virtually all sheet steel, aluminum, and copper goes through rolling.

```
ROLLING AND DRAWING LANDSCAPE:

PRIMARY FORMS (from steelmaking/casting)
  Slabs (flat, thick) ──────────────► Hot strip mill → cold rolling → sheet/coil
  Blooms (square, large) ──────────► Hot rolling → structural sections (I-beams, channels)
  Billets (square, small) ────────► Hot rolling → bar, rod → cold drawing → wire

PROCESS HIERARCHY:
  HOT ROLLING (above recrystallization T)
    ├── Strip rolling → flat products (coils, plate)
    ├── Long product rolling → bar, rod, rail, structural sections
    └── Tube rolling → seamless pipe (Mannesmann)

  COLD ROLLING (room temperature)
    ├── Cold reduction of hot-rolled strip → CRS (cold-rolled steel)
    └── Temper rolling → surface finish + stress relief

  DRAWING
    ├── Wire drawing → wire (all diameters)
    ├── Tube drawing → precision tube/pipe
    └── Bar drawing → turned, ground, polished bar (precision diameter)

  EXTRUSION (companion process — pushes rather than pulls)
    └── Aluminum: profiles, tubes, channels
```

---

## Hot Rolling

### Process Mechanics

```
HOT ROLLING FUNDAMENTALS:

Rolling stand geometry:
  Two work rolls (driven) compress the workpiece
  Entry thickness h₀ → exit thickness h₁
  Draft: Δh = h₀ - h₁
  Reduction ratio: r = Δh/h₀
  Spread (width increase): small for most rolling; significant for flat plate

Contact arc:
  L = √(R·Δh)  where R = work roll radius
  Contact length L determines rolling pressure and torque

Material flows:
  Volume conservation: h₀·w₀·v₀ = h₁·w₁·v₁
  Entry speed < exit speed (metal exits faster because it's thinner)
  Neutral point: where material speed = roll surface speed (zero slip)
```

### Hot Strip Mill

```
HOT STRIP MILL (continuous):

  Slab (200–250mm thick, ~1000–2000mm wide, ~10 tonnes)
     │
     ▼ Reheat furnace (~1200°C)
     │
     ▼ Roughing mill (4–6 passes, reduces slab to transfer bar ~25–45mm)
     │
     ▼ Finishing train (5–7 tandem stands in line)
     │ Each stand: ~2–3mm to next, rolling at increasing speed
     │ Exit speed: up to 25 m/s (90 km/h)
     │ Strip thins and accelerates continuously
     ▼
     ▼ Run-out table: laminar flow water cooling
     │ Controls final microstructure via cooling rate
     │ High cool rate: smaller ferrite grain, harder
     │ Low cool rate: softer, better formability
     ▼
Coiler: hot-rolled coil, typically 2–8mm thick, scale-covered surface

MINIMUM GAUGE:
  Hot rolling limited to ~1.5–2mm minimum
  → Below this: temperature drops too fast; rolling forces impractical
  → Thinner products require cold rolling
```

### Hot Rolling Products and Standards

| Product | Thickness | Width | Application |
|---------|-----------|-------|-------------|
| Hot-rolled coil (HRC) | 1.5–16mm | 600–2000mm | Fabrication, pipes, automotive frame |
| Cut-to-length plate | 5–200mm | up to 3600mm | Structural, pressure vessels, shipbuilding |
| Rail | profile | — | Railway track (special shape mill) |
| Structural sections | I/H/channel/angle | — | Building construction |
| Seamless tube | OD/WT | — | High-pressure piping (Mannesmann plug mill) |

---

## Cold Rolling

Cold rolling hot-rolled strip at room temperature (no heating).

```
COLD ROLLING PROCESS:

HRC (hot-rolled coil) → pickling (HCl or H₂SO₄ to remove scale)
     │
     ▼ Cold rolling mill (4-high, 6-high, or cluster mill)
     │ Typical total reduction: 40–80% (e.g., 3mm → 0.8mm)
     │ Multiple passes or tandem cold mill (5 stands in line)
     │ Heavy lubricant (rolling oil) critical for surface quality + roll life
     ▼
Cold-rolled coil (CRC): smooth surface, tight tolerances, work-hardened

PROPERTIES AFTER COLD ROLLING:
  Yield strength: increases 50–100% from work hardening (dislocation accumulation)
  Elongation: decreases (less ductility)
  Hardness: increases
  Surface: smooth, Ra ~0.5–1.5µm vs 2–5µm hot-rolled

TEMPERS (aluminum designation, similar concept in steel):
  Full-hard (H18 for Al): maximum cold work; high strength, low ductility
  Three-quarter hard (H16), Half-hard (H14), Quarter-hard (H12)
  Annealed (O): fully softened; maximum ductility
  → Tempering (partial anneal + light cold roll pass) between extremes
```

### Annealing and Temper Rolling

```
BATCH ANNEALING (box anneal):
  Coils stacked in sealed furnace; annealed with N₂ atmosphere
  Temperature: ~650–750°C for low-carbon steel
  Time: 24–48 hours (slow heat + cool)
  Result: recrystallization → new equiaxed grains → soft and ductile

CONTINUOUS ANNEALING (CAPL):
  Strip runs continuously through long furnace tunnel at speed
  Heating → soaking → rapid cooling in one pass
  Cycle time: minutes instead of days
  Better uniformity and some microstructure control vs batch

TEMPER ROLLING (skin pass):
  Very light cold reduction (0.5–2%) after annealing
  Purpose:
  • Eliminate Lüders bands (yield point elongation — causes stretcher strain marks)
  • Improve surface roughness and flatness
  • Small increase in yield strength
  Not enough to significantly work-harden; just surface conditioning
```

---

## Work Hardening

Work hardening (strain hardening) is the fundamental physical phenomenon underlying all cold deformation processes.

```
MECHANISM:
  Crystal plasticity: dislocations move on slip planes → plastic deformation
  As deformation continues → dislocation density increases
  Dislocations entangle and block each other
  → Higher stress required to continue deformation

  Flow stress σ = σ₀ + K·εⁿ  (empirical power law, Hollomon)
  K = strength coefficient, n = strain hardening exponent
  High n: spreads strain uniformly (good for deep drawing)
  Low n: localizes strain (necking occurs earlier)

RECOVERY AND RECRYSTALLIZATION:
  Cold-worked metal heated → three stages:
  1. Recovery (< recrystallization T):
     Internal stress relief; slight hardness decrease
     Dislocation rearrangement, not grain formation
  2. Recrystallization (typically 30–60% of melting T in K):
     New strain-free grains nucleate and grow from old deformed grains
     Hardness drops significantly; ductility restored
     Grain size determined by prior deformation and annealing temperature
  3. Grain growth (above recrystallization T):
     New grains grow to reduce boundary energy
     → Coarser grains; slightly lower strength

RECRYSTALLIZATION TEMPERATURES:
  Aluminum: ~150°C (why Al can be work-hardened only at low temps)
  Copper: ~120–150°C
  Low-carbon steel: ~450–500°C
  Titanium: ~500°C
  Tungsten: ~1200°C (can be cold worked at temperatures steel cannot)
```

---

## Profile Rolling

Hot rolling of non-flat shapes through specially designed roll pass sequences.

```
ROLL PASS DESIGN:

Purpose: progressively change billet cross-section into desired profile
         in the minimum number of passes

I-BEAM ROLLING:
  Starts: rectangular billet or bloom
  Passes:
  1. Roughing → breakdown square to approximately H shape
  2. Intermediate → develop web and flange dimensions
  3. Universal mill: vertical + horizontal rolls simultaneously
     → Control flange and web independently
  4. Edger mill: compress flange thickness
  5. Finishing pass: final shape

  Key constraint: metal flows into flange corners → must be forced by roll geometry
  Roll caliber: the shape of the groove cut into the roll face
  → Each pass designed to move metal closer to final shape while maintaining
    temperature above recrystallization

SEAMLESS TUBE (MANNESMANN PROCESS):
  Principle: bar rotated + pushed through conical rolls set at angle
  Rotary rolling creates tensile stress at center → Mannesmann effect: center cracks
  → Piercing plug opens the crack into a hole → hollow shell forms
  Passes:
  1. Cross-roll piercing mill → shell
  2. Elongating mill → elongate shell, reduce wall thickness
  3. Reeling + sizing → finish OD and roundness
  Result: seamless pipe — no weld seam → preferred for high-pressure applications
          (hydrogen service, high-temp steam, oil/gas downhole)
```

---

## Wire Drawing

Wire drawing reduces cross-section by pulling through a series of dies.

```
WIRE DRAWING PROCESS:

  Rod (5–6mm diameter, hot-rolled) → wire drawing bench/block
          │
          ▼
  Point end (swage tip) → thread through die
          │
          ▼
  Die: hardened tool (tungsten carbide or diamond for fine wire)
       Conical entry (drawing cone angle: 6–12°)
       Bearing (land: parallel section sets final diameter)
       Back relief
          │
          ▼
  Pull with capstan (driven drum) → wire drawn through die
  Reduction per pass: 15–25% area reduction
  Multiple passes in sequence: e.g., 5.5mm → 3.4 → 2.1 → 1.3 → 0.8mm

LUBRICATION:
  Wet drawing (fine wire): soap solution, oil, liquid lubricant
  Dry drawing (coarse wire): dry soap powder
  Purpose: reduce friction between wire and die → lower drawing force + die wear
           without lubrication: die fails in passes (seizing); wire surface damaged

ANNEALING STAGES:
  Work hardening accumulates with each pass
  After ~80% total area reduction: wire too hard to draw without fracturing
  → Intermediate patenting or annealing required:
    Patenting (steel): heat to austenite → quench in molten lead → pearlite
                       fine pearlite = high strength + still drawable
    Annealing (copper, aluminum): full recrystallization anneal
  Then continue drawing
```

### Wire Products

| Application | Material | Diameter range | Notes |
|-------------|---------|----------------|-------|
| Electrical conductor | Cu (OFC or ETP) | 0.1–3mm | Soft-annealed for flex |
| High-strength wire rope | High-C steel | 0.15–5mm | Patented + cold-drawn |
| Music wire | High-C steel | 0.1–3mm | Highest strength grades |
| Spring wire | Medium-C steel | 0.1–6mm | Hard-drawn or oil-tempered |
| Welding wire | Low-C or austenitic SS | 0.6–3.2mm | Copper-coated for MIG |
| Fiber optic armor | High-C steel | 0.2–0.5mm | Protective sheath |

---

## Tube Drawing

Similar to wire drawing but preserves or controls bore diameter.

```
TUBE DRAWING METHODS:

SINKING (no mandrel):
  Tube drawn through die; bore unsupported
  OD reduced; wall increases; bore shrinks unpredictably
  Simple; used for roughing passes

FIXED PLUG:
  Stationary plug inside tube anchored to drawbench
  OD die + ID plug = both dimensions controlled
  Good OD and ID tolerance; limited length (plug held on rod)

FLOATING PLUG:
  Plug self-locates in die throat by pressure equilibrium
  Not anchored externally → long tube lengths possible
  Very common for precision tube production

MANDREL DRAWING:
  Long mandrel rod fills bore; tube drawn over mandrel
  Excellent surface quality and dimensional control
  Mandrel must be extracted → separate operation

APPLICATIONS:
  Hydraulic cylinder tubing: floating plug, tight tolerances ±0.05mm OD
  Heat exchanger tubes: many alloys; precision OD for tube rolling
  Medical tubing (stainless): very tight tolerances, very smooth ID
  Structural tube: standard sinking to size
```

---

## Aluminum Extrusion

Not rolling but related: aluminum profiles made by pushing billets through dies.

```
ALUMINUM EXTRUSION PROCESS:
  Billet heated (~450–520°C for 6061)
  Hydraulic ram presses billet against die at 1000–15,000 tonnes force
  Metal flows through die openings → continuous profile exits

ADVANTAGES OF EXTRUSION vs ROLLING:
  Can produce complex cross-sections (hollow, multi-void, integral fins)
  One die → one profile shape
  Very thin wall sections possible
  Economical tooling for medium volumes

LIMITATIONS:
  Length limited by billet size (seam weld where next billet joins)
  Not suitable for high-strength 2xxx and 7xxx (very high force; hot cracking)
  Surface speed limited (too fast → hot cracking)

TYPICAL PRODUCTS:
  Window and door frames, curtain wall sections
  Structural channels, angles, tees
  Heat sinks (integral fins)
  Automotive crash extrusions (6061, 6063)
  Industrial profiles (conveyor tracks, framing)
```

---

## Aluminum Temper Designations

```
ALUMINUM TEMPER SYSTEM (important for rolling + drawing):

-F: As fabricated (no thermal or mechanical treatment specified)
-O: Annealed (minimum strength; maximum ductility)
-H: Strain hardened (cold worked)
    H1x: Cold worked only
    H2x: Cold worked + partially annealed
    H3x: Cold worked + stabilized (some alloys)
    x = 2 (¼ hard), 4 (½ hard), 6 (¾ hard), 8 (full hard), 9 (extra hard)
-T: Thermally treated (solution heat treat and/or precipitation hardened)
    T4: Solution treated + naturally aged
    T5: Artificially aged after extrusion
    T6: Solution treated + artificially aged
    T73: Overaged for corrosion resistance (7xxx)

Examples:
  6061-T6: Solution treat (500°C) + water quench + age at 160°C/18h → peak strength
  2024-T3: Solution treat + cold work + natural age → high strength + good fatigue
  3003-H14: Cold rolled to ½ hard → intermediate strength cookware, general sheet
```

---

## Decision Cheat Sheet

| Goal | Process |
|------|---------|
| Sheet steel < 3mm for auto/appliances | Hot roll → pickle → cold roll |
| Flat plate > 10mm for structures | Hot roll (directly usable) |
| I-beams, structural sections | Hot profile rolling |
| Seamless high-pressure pipe | Mannesmann piercing + rolling |
| Electrical conductor wire | Cu rod → wet drawing (multiple passes) |
| High-strength steel wire (cable) | High-C rod → patenting → drawing |
| Aluminum architectural profiles | Extrusion (6063, 6061) |
| Tight-tolerance hydraulic tube | Tube drawing over floating plug |
| Maximum ductility for deep drawing | Cold-rolled + fully annealed (soft temper) |

---

## Common Confusion Points

**Hot-rolled vs cold-rolled steel: the difference is process, not final temperature**
"Hot-rolled" steel is used at the rolled thickness with scale on surface; "cold-rolled" is hot-rolled + pickled + cold-reduced. The terms describe the manufacturing route. CRS has tighter tolerance, smoother surface, and higher yield strength than HRS of the same nominal thickness.

**Reduction per pass is limited — you can't go from billet to wire in one die**
Each pass reduces area by 15–25%. Too much reduction per pass → drawing force exceeds wire strength → fracture. Total reductions of 90% require 8–12 passes. Intermediate anneals may be needed.

**Work hardening increases strength but reduces ductility**
Cold-rolled steel and hard-drawn wire are strong because of dislocation accumulation. But bending them too much causes cracking. Deep drawing (forming sheet into cups, pans, car doors) requires high n (strain hardening exponent) and sufficient total elongation. H18 aluminum won't deep draw; O temper will.

**Extrusion and drawing are opposite processes**
Drawing: pulling metal through a die (tension is the driving force)
Extrusion: pushing metal through a die (compression is the driving force)
Both reduce cross-section; they're complementary. Drawing produces better dimensional control over long lengths; extrusion produces more complex shapes.

**Profile rolling requires careful pass design to avoid seams and laps**
If metal in a roll groove is forced to fold over on itself → cold weld seam (lap) or open crack (seam). These are surface defects that don't show up dimensionally but cause fatigue failure in service. Roll pass design is as much art as engineering, refined over decades of production experience.
