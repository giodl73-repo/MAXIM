# Casting, Forging, and Forming Processes

## The Big Picture

Formative processes reshape material without removing it. Three major branches: casting (liquid solidifies in a mold), bulk deformation (solid plastically deformed at scale), and sheet metal forming (thin plate bent/drawn/stamped). Each branch spans a range of processes with different tooling costs, achievable geometry, and volume economics.

```
FORMATIVE MANUFACTURING MAP
──────────────────────────────────────────────────────────────────────
                    ┌───────────────────────────────────────────────┐
                    │           FORMATIVE PROCESSES                 │
                    └──────────────┬──────────────────┬────────────┘
                                   │                  │
               ┌───────────────────┘                  └──────────────────┐
               │                                                          │
    ┌──────────▼─────────┐                                   ┌──────────▼────────┐
    │     CASTING        │                                   │  BULK DEFORMATION  │
    │   (liquid→solid)   │                                   │   (solid plastic)  │
    │                    │                                   │                    │
    │ Sand Casting       │                                   │ Forging            │
    │ Die Casting        │                                   │ Rolling            │
    │ Investment (lost   │                                   │ Extrusion          │
    │   wax) Casting     │                                   │ Drawing (wire/tube)│
    │ Lost Foam          │                                   │ Sheet Metal        │
    │ Centrifugal Cast   │                                   │ (bend/stamp/draw)  │
    └────────────────────┘                                   └────────────────────┘
```

---

## Sand Casting

### Process Flow

```
SAND CASTING PROCESS
──────────────────────────────────────────────────────────────────
Pattern       →  Pattern is a model of the part
(wood/metal)     plus draft angles, parting line, gating

Pattern placed in  →  Cope (top half) and Drag (bottom half)
sand molding box      Green sand (clay-bonded) or no-bake resin sand

Pattern removed  →  Cavity = negative of part shape
                    Core (sand) placed for internal cavities

Molten metal poured  →  Into sprue, down runner, into cavity
                        Risers (reservoirs) feed shrinkage

Solidification  →  Cool time depends on mass
                   Heavy sections cool slower (hot spots)

Shakeout        →  Destroy mold, remove casting
                   Shot blast to clean sand
                   Cut off sprues and runners

Finish          →  Machine critical surfaces
                   Heat treat if required
```

### Sand Casting Parameters

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| Dimensional tolerance | ±0.030"–0.060" | Depends on size, material |
| Surface finish Ra | 6.3–25 µm | Rough — machining usually required |
| Draft angle | 1–5° per side | Allows pattern withdrawal |
| Minimum wall | 3–6mm (steel/iron) | Thinner → incomplete fill |
| Shrinkage allowance | 1–2% linear | Pattern made oversized |

**Economics**: Low tooling cost ($500–$5K for pattern). Labor-intensive. Best for large, complex parts at low volume (1–1,000). Gray iron, ductile iron, steel, aluminum, bronze.

### Green Sand vs No-Bake vs Shell

```
GREEN SAND         Clay-bonded, recyclable, fast, most common
                   Slightly rough surface, limited detail

NO-BAKE (furan)    Chemical binder, very hard mold, better surface
                   More accurate, slower setup, harder to recycle

SHELL MOLD         Phenolic resin + sand, heated pattern
                   Very accurate, excellent surface, higher tooling cost
                   Good for aluminum, small precision castings
```

---

## Die Casting

### Process

```
HOT CHAMBER DIE CASTING           COLD CHAMBER DIE CASTING
(Zinc, Magnesium, low-melt)        (Aluminum, Brass, high-melt)
──────────────────────────────     ──────────────────────────────
Injection system submerged         Metal ladled manually or
in molten metal (gooseneck)        automatically into cold sleeve
→ faster cycle (2–10s)             → hydraulic plunger injects
                                   → 15–60 second cycle

Both: High pressure injection (1,000–30,000 psi)
      Steel dies (H13 tool steel)
      Near-net shape, excellent surface finish
      Tight tolerances (±0.002" on small features)
```

### Die Casting Process Parameters

| Material | Injection Pressure | Die Temp | Typical Tolerance |
|----------|--------------------|----------|------------------|
| Aluminum (A380) | 5,000–15,000 psi | 200–300°C | ±0.002"–0.005" |
| Zinc (Zamak) | 1,000–5,000 psi | 150–200°C | ±0.001"–0.003" |
| Magnesium (AZ91) | 5,000–15,000 psi | 200–250°C | ±0.003"–0.006" |

**Economics**: Tooling $10K–$100K+. Per-part cost very low. Break-even typically 10,000–50,000 parts. Die life: 100K–1M shots (aluminum). Zinc = longer die life. Ferrous alloys too hot — use squeeze casting instead.

### Die Casting Design Rules

```
WALL THICKNESS:
  Aluminum: 2–4mm uniform preferred
  Varying wall → differential solidification → porosity, sink marks
  Transitions: gradual fillets, not sharp steps

DRAFT ANGLES:
  Exterior walls: 1° minimum
  Interior (cavity) walls: 2° minimum
  Cores (through holes): 1.5° minimum

PARTING LINE:
  Where two die halves meet → flash line on part
  Position to minimize core pulls, keep on flat surface

CORES (holes perpendicular to parting):
  Holes parallel to pull = simple core pin
  Holes at angle → side action (lifter/slider) → more expensive

RIBS:
  Height: 2.5× wall thickness max
  Thickness: 60% of wall at base
  Draft: 1° minimum each side
```

---

## Investment Casting (Lost Wax)

### Process Flow

```
INVESTMENT CASTING PROCESS
──────────────────────────────────────────────────────────────────
1. WAX PATTERN
   Wax injected into metal die → wax replica of part
   Multiple wax patterns welded to wax gating tree

2. SHELL BUILDING
   Tree dipped in ceramic slurry (silica sol + zircon)
   Stuccoed with coarse ceramic particles
   Repeat 5–15 layers → thick ceramic shell
   Dry between layers

3. DEWAX (AUTOCLAVE)
   Steam autoclave melts out wax
   Wax expands before melt → cracks thin shells if not managed
   Result: hollow ceramic shell = negative of part

4. FIRING
   Kiln at 1000°C → burns residual wax, sinters ceramic
   Pre-heats mold for metal pour

5. METAL POUR
   Molten metal poured (by gravity, tilt, vacuum, or pressure)
   Into hot mold (better flow, less gas porosity)

6. SHELL KNOCKOUT
   Vibration + water blasting destroys ceramic shell
   Cut off individual parts from gating tree

7. FINISH
   Grind off gates
   Inspect, heat treat, machine critical surfaces
```

### Investment Casting Characteristics

| Parameter | Value |
|-----------|-------|
| Dimensional tolerance | ±0.005"–0.010" typical |
| Surface finish Ra | 1.6–3.2 µm (much better than sand) |
| Minimum wall | 1–2mm |
| Weight range | <1g to >200 kg |
| Materials | Steel, SS, Ni superalloys, Ti, Co, Al, Cu |

**Advantage over die casting**: Works with any alloy including high-temp Ni superalloys (Inconel, Hastelloy) and titanium that die casting cannot handle. Complex internal geometry (turbine blade cooling passages) via ceramic cores.

**Turbine blade example**: Single-crystal directionally solidified Ni superalloy blades with internal cooling passages — only achievable via investment casting.

---

## Forging

### Process Principle

```
FORGING MECHANICS
──────────────────────────────────────────────────────────────────
Hot forging: metal heated above recrystallization temp (~0.6 Tm)
  → lower flow stress → large deformations
  → grain refinement during recrystallization
  → no work hardening (grains reform after deformation)

Cold forging: room temperature
  → higher force required
  → work hardening → higher yield strength
  → better surface finish
  → tighter tolerances (±0.001"–0.003")
  → limited to relatively ductile materials (aluminum, brass, mild steel)

Warm forging: between cold and hot (compromise)
```

### Forging Types

```
OPEN-DIE FORGING
  Simple flat or shaped dies
  Part moves between blows (operator reposition)
  Large parts (shafts, discs, blocks)
  Low tooling cost
  Poor dimensional control (±0.030"–0.060")
  Excellent internal soundness (worked throughout)

CLOSED-DIE (IMPRESSION DIE) FORGING
  Matched upper/lower dies with part cavity
  Metal fills cavity under high force
  Flash forms at parting line (trimmed)
  Near-net shape
  Good tolerances (±0.010"–0.030")
  Tooling cost: $5K–$50K

PRECISION FORGING (flashless)
  Dies fully closed — no flash
  Tightest tolerances for forging (±0.003"–0.010")
  Gears, turbine discs
  Higher die cost, controlled volumes

ROLL FORGING
  Part rolled between shaped rolls
  Long tapered sections (axles, blades)
  Continuous process

ROTARY (ORBITAL) FORGING
  Die tilts and rotates
  Smaller forming force
  Wheel hubs, flanges, symmetric parts
```

### Why Forging Gives Better Properties

```
CAST vs FORGED MICROSTRUCTURE
──────────────────────────────────────────────────────────────────
Cast:                              Forged:
  Random grain orientation           Grain flow follows part shape
  Possible porosity, shrinkage       No porosity (worked closed)
  Columnar grains from solidification Equiaxed, refined grains
  Lower fatigue resistance           Higher fatigue resistance
  Good enough for static loading     Required for dynamic loading

  ┌─────────────┐                  ┌─────────────┐
  │ Grain       │                  │  ←Grain     │
  │ structure   │                  │   flow→     │
  │ random      │                  │  follows    │
  │ defects     │                  │  contour    │
  └─────────────┘                  └─────────────┘

Aircraft connecting rods, crankshafts, landing gear, turbine discs
→ always forged. Cast equivalents would fail under fatigue loading.
```

---

## Rolling

```
ROLLING PROCESSES
──────────────────────────────────────────────────────────────────
HOT ROLLING (>0.6 Tm)
  Large reductions in passes through roll stands
  Structural shapes (I-beam, channel, angle, wide flange)
  Hot-rolled plate and sheet (HR)
  Surface: mill scale (oxide layer), rough

COLD ROLLING (ambient)
  HR coil is pickled (acid removes scale) then cold-rolled
  Produces cold-rolled sheet (CRS): tighter tolerances, smooth
  Work hardened → higher yield strength than HR
  Common: CRS 1008/1010 for stampings, enclosures

BAR/ROD/WIRE ROLLING
  Hot rolling → billets to rod (5–20mm dia)
  Cold drawing → rod to wire (down to 0.1mm)
  Each draw pass: 10–30% reduction, progressive dies

RING ROLLING
  Hollow preform compressed between inner/outer rolls
  → seamless rings (bearing races, flanges, gears)
  Excellent grain flow, very strong
```

---

## Sheet Metal Forming

### Bending

```
BENDING FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Neutral axis: no stress in bending
Outside of bend: tension (tensile stress)
Inside of bend: compression

Springback: elastic recovery after bend force removed
  High-strength material = more springback
  Over-bend by springback angle, let it spring to target

Minimum bend radius (by material and thickness t):
  Soft aluminum (1100-O): 0t  (can bend flat)
  2024-T4 aluminum: 3t
  Mild steel (1008): 1t
  SS 304: 1.5t–2t
  Titanium Grade 5: 3t–5t

V-bending:       Punch forces sheet into V-die
Air bending:     Sheet touches die sides only (partial die contact)
                  → more springback, versatile (any angle)
Bottom bending:  Sheet bottomed into die
                  → less springback, die-specific angle
```

### Deep Drawing

```
DEEP DRAWING
──────────────────────────────────────────────────────────────────
Flat blank → punch forces into die → cup/box form
Blank holder controls flange wrinkle

Key parameter: Draw Ratio (DR) = Blank diameter / Punch diameter
  DR < 2.0 typical (first draw)
  DR up to 2.2 for high-ductility materials (aluminum)
  Multiple draws (redraw) for deeper cups

Failure modes:
  Wall fracture:   tensile failure at punch radius (too aggressive draw)
  Wrinkling:       compressive instability in flange (blank holder too loose)
  Earing:          non-uniform thickness strains (material anisotropy)

Materials: Low-carbon steel (AISI 1006, 1008, IF steel)
           Aluminum (3003, 5052, 5182)
           Stainless (needs more force, work hardens)
```

### Stamping (Progressive Die)

```
PROGRESSIVE DIE STAMPING
──────────────────────────────────────────────────────────────────
Strip of metal feeds through series of stations in one die:
  Station 1: Pilot holes
  Station 2: Pierce holes
  Station 3: Notch
  Station 4: Blank / form
  Station 5: Coin / restrike
  Station 6: Cutoff

One stroke = one part (high speed: 100–400+ strokes/min)
Tooling: $10K–$500K
Application: connectors, brackets, panels (automotive, electronics)
```

---

## Decision Cheat Sheet

| Need | Process |
|------|---------|
| Large part, complex shape, one-off | Sand casting |
| High volume aluminum housings/enclosures | Die casting |
| Complex geometry, any alloy | Investment casting |
| Turbine blades / Ni-superalloy | Investment casting (directional solidification) |
| High-strength structural part | Closed-die forging |
| Seamless ring / bearing race | Ring rolling |
| Sheet metal enclosure, brackets | Stamping + bending |
| Deep drawn cup/can | Deep drawing |
| Long constant cross-section (angle, channel) | Extrusion or rolling |
| Wire / fine rod | Drawing |

---

## Common Confusion Points

**Die casting porosity**: High-pressure injection traps gas → subsurface porosity is inherent in die casting. Parts cannot be welded (gas expands and causes blistering). Solution: vacuum die casting, or accept that critical sections must be machined (porosity zone exposed as machined surface = stress concentration). T6 heat treatment also causes blister in porosity-containing die castings.

**Forging vs casting strength**: Tensile strength of a forged vs cast equivalent can be similar on first look. Fatigue life is where the difference matters — forged parts have 2–4× higher fatigue strength due to grain alignment and absence of porosity. Always specify forging for cyclically loaded parts.

**Hot-rolled vs cold-rolled steel**: HR steel has mill scale, rough surface, wider tolerances. CRS is smooth, tighter tolerance, higher yield strength (work hardened), ready for painting. HR is structural (I-beams); CRS is sheet metal for fabrication.

**Springback is material-dependent, not tooling**: Higher-strength steels (AHSS, UHSS in automotive) have massive springback. The same press and die that works for mild steel gives wrong angles with AHSS. CAD compensation (over-bending) must be tuned per material lot.

**Investment casting ceramic core removal**: Creating internal passages (turbine blade cooling) requires ceramic cores, which are placed in the wax and remain in the metal shell during pour. Post-cast, cores are chemically leached out (hot caustic) — delicate operation, inspection-critical.
