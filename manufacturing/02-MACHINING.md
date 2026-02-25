# Machining: Turning, Milling, and Grinding

## The Big Picture

Machining is controlled material removal. Three cutting mechanisms cover nearly all work: shearing (turning/milling), abrasion (grinding), and erosion (EDM/ECM). The physics of chip formation determines surface finish, tool life, and achievable tolerances.

```
MACHINING PROCESS MAP
──────────────────────────────────────────────────────────────────
CUTTING (single/multi-point)         ABRASIVE               EROSION
────────────────────────────         ─────────────          ───────
Turning   → cylindrical OD/ID        Grinding → ±1–5µm Ra   EDM
Milling   → prismatic, complex        Honing   → cylinder    ECM
Boring    → precision holes           bores, Ra 0.1         Laser
Drilling  → hole creation             Lapping  → ±0.25µm    Waterjet
Reaming   → hole sizing               superfinish
Tapping   → threads                   Superfinish → Ra 0.025
Broaching → splines, keyways
```

---

## Turning (Lathe Operations)

### Process Physics

```
                    ┌─────────────────────┐
Workpiece rotates   │   CUTTING GEOMETRY  │
at N rpm.           │                     │
Tool feeds at f     │  Rake angle α       │
in/rev (or mm/rev)  │   ↑ positive → less │
at depth d.         │     cutting force   │
                    │   ↑ negative → more │
                    │     tool strength   │
                    │                     │
                    │  Relief angle β     │
                    │   prevents heel     │
                    │   rubbing           │
                    └─────────────────────┘

Chip formation:
  Chip thickness (uncut) = f × sin(SCEA)
  where SCEA = side cutting edge angle

  Cutting speed V = π × D × N / 12  (sfm, D in inches, N in rpm)
  or V = π × D × N / 1000           (m/min, D in mm, N in rpm)
```

### Cutting Speed Recommendations

| Material | Carbide Insert (sfm) | HSS (sfm) |
|----------|---------------------|-----------|
| Aluminum (6061) | 800–1200 | 200–400 |
| Mild steel (1018) | 400–600 | 80–120 |
| Alloy steel (4140) | 250–400 | 50–80 |
| Stainless 304 | 200–350 | 50–70 |
| Titanium Ti-6Al-4V | 100–200 | 30–60 |
| Cast iron (gray) | 300–500 | 80–120 |
| Inconel 718 | 60–120 | 15–25 |

### Lathe Operations

```
TURNING OPERATIONS
──────────────────────────────────────────────────────
OD Turning     → reduces outer diameter, facing tool
Facing         → creates flat end face perpendicular to axis
Boring         → enlarges or trues up an existing hole (ID)
Parting/Cutoff → severs part from bar stock (narrow groove tool)
Threading      → single-point thread form, matched to lead
Knurling       → work-hardens and texturizes OD surface
Taper turning  → tool path at angle (compound rest or taper att.)
Form turning   → contoured insert follows curved profile
```

### Tolerances Achievable (Turning)

| Condition | Diameter Tolerance | Surface Finish Ra |
|-----------|-------------------|------------------|
| Rough turning | ±0.010" (±0.25mm) | 3.2–6.3 µm |
| Finish turning | ±0.003" (±0.075mm) | 0.8–1.6 µm |
| Precision turning | ±0.001" (±0.025mm) | 0.4–0.8 µm |
| Precision boring | ±0.0005" (±0.013mm) | 0.4 µm |

---

## Milling (Machining Center Operations)

### Process Physics

```
CLIMB vs CONVENTIONAL MILLING
──────────────────────────────────────────────────────────────────
Climb milling          Conventional milling
(down milling)         (up milling)

Cutter rotation and    Cutter rotation opposite
feed in same direction to feed direction

  ──── Feed ────►        ◄─── Feed ────
    ↙ ↙ ↙                ↗ ↗ ↗
   cutter teeth          cutter teeth

Chip starts thick,     Chip starts thin,
ends thin → cleaner    grows → more
cut, better surface,   rubbing, pushes
less heat, preferred   part up (needs
when machine is        good fixturing)
rigid and backlash-
free (CNC)
```

### Milling Operations

```
PERIPHERAL (SIDE) MILLING
  End mill side teeth cut
  Vertical walls, slots, pockets

FACE MILLING
  Face mill with indexable inserts
  Large flat surfaces, fast stock removal

PLUNGE MILLING
  Tool plunges axially
  Reduces radial cutting forces for deep pockets

TROCHOIDAL / DYNAMIC MILLING
  Circular arc toolpaths
  Maintains constant chip load
  Allows full depth of cut with reduced radial engagement
  Modern CAM strategy for hard materials, extended tool life

HELICAL INTERPOLATION
  Tool spirals down into pocket
  Eliminates need for drill-first
  Reduces entry forces
```

### Milling Parameter Relationships

```
Feed rate (in/min) = RPM × Chip load (in/tooth) × Number of teeth
                   = N × fz × Nt

Chip load fz depends on:
  - Cutter diameter
  - Material (see table above for speed, then back-calculate)
  - Axial depth of cut (Ap)
  - Radial depth of cut (Ae)

Radial chip thinning: when Ae < D/2, actual chip thickness is less
than programmed chip load. CAM systems compensate automatically.
```

### Machine Configurations

```
MACHINING CENTER TYPES
──────────────────────────────────────────────────────────────────
VMC (Vertical Machining Center)
  Spindle vertical, table horizontal
  Gravity helps chip evacuation from workpiece
  Best for: flat parts, plates, prismatic blocks

HMC (Horizontal Machining Center)
  Spindle horizontal, tombstone/pallet fixtures
  Chips fall away from workpiece by gravity
  Best for: production, multiple faces, palletized

5-Axis
  3 linear + 2 rotary axes
  Simultaneous 5-axis or 3+2 positioning
  Can machine undercuts, compound angles, aerospace parts
  Reduces setups, improves accuracy (single setup)

Turn-Mill (Mill-Turn)
  Lathe with live milling spindle
  Complete part in one setup
  Best for: complex turned parts with off-axis features
```

---

## Grinding

### Process Physics

Grinding is multi-point cutting with random geometry abrasive grains. Each grain acts as a cutting tooth with extreme negative rake angle (−60° to −80°).

```
GRINDING WHEEL STRUCTURE
─────────────────────────────────────────────────────────
Abrasive grain:   Al₂O₃ (aluminum oxide) → steel/iron
                  SiC (silicon carbide) → non-ferrous, ceramics
                  CBN (cubic boron nitride) → hardened steel
                  Diamond → ceramics, carbide, CFRP

Bond:             Vitrified (glass) → most common, rigid
                  Resinoid → flexible, lighter cuts
                  Metal → diamond wheels for dressing

Grade (hardness): A–Z (A = softest bond, Z = hardest)
                  Soft bond → hard materials (grain releases easily)
                  Hard bond → soft materials (grain stays longer)

Structure (spacing): 1–15 (open = more chip clearance)
```

### Grinding Operations

```
SURFACE GRINDING        Flat surfaces
  Wheel horizontal or   ±0.0005" / Ra 0.2–0.4 µm
  vertical spindle

CYLINDRICAL GRINDING    Shafts, pins, ID/OD
  Between centers or    ±0.0002" / Ra 0.1–0.4 µm
  centerless

INTERNAL GRINDING       Bores, cylinders ID
  Small wheel, high RPM ±0.0002" / Ra 0.2–0.8 µm

CENTERLESS GRINDING     High-volume bar/shaft OD
  No centers, regulating ±0.0001" diameter
  wheel controls feed

PROFILE GRINDING        Gear teeth, cams, complex
  CNC dressed wheel     profiles; tight form accuracy
```

### Grinding Wheel Selection Logic

```
Hard material (carbide, ceramics, glass) → Diamond or CBN wheel
Soft material (aluminum, copper) → Al₂O₃, open structure
Hardened steel (>40 HRC) → CBN wheel
Annealed/soft steel → Al₂O₃, medium-soft grade
Stainless steel → Al₂O₃, open structure (avoid loading)
Large contact area → soft grade (wheel breaks down faster)
Small contact area → hard grade (retains shape)
```

### Grinding Defects

```
THERMAL DAMAGE (grinding burn)
  Cause: too aggressive, dull wheel, insufficient coolant
  Result: tempered surface (hardness loss), tensile residual stress
  Detection: acid etch (Barkhausen noise for critical parts)
  Prevention: sharp wheel, adequate coolant, dress frequently

CHATTER
  Cause: wheel imbalance, worn spindle bearings, loose workholding
  Result: regular waviness pattern on surface
  Fix: balance wheel, check spindle, tighten fixture

LOADING
  Cause: workpiece material builds up in wheel pores
  Result: rubbing, no cutting, heat buildup
  Fix: open structure wheel, dress more frequently, flood coolant
```

---

## EDM (Electrical Discharge Machining)

### Process Principle

```
SPARK EROSION MECHANISM
─────────────────────────────────────────────────────────────────
Electrode (tool) and workpiece separated by dielectric fluid.
Voltage applied → spark discharge bridges gap.
Each spark removes ~10⁻⁶ to 10⁻⁴ mm³ of material.
Series of millions of sparks → shape transferred.

Key property: hardness of workpiece is IRRELEVANT.
Any electrically conductive material can be EDM'd.
```

### Wire EDM vs Sinker EDM

```
WIRE EDM                          SINKER (Die Sinking) EDM
──────────────────────────────    ──────────────────────────────
Thin wire (0.004"–0.012")         Shaped electrode machines
cuts through workpiece            cavity into workpiece

  2D through-cuts                 3D cavities
  Punch/die blanks                Injection mold cavities
  Complex external profiles       Blind holes, pockets
  Hardened tool steel             Deep slots, fine ribs
                                  Any conductive material

  Tolerance: ±0.0002"             Tolerance: ±0.0005"
  Ra: 0.4–1.6 µm                  Ra: 0.4–3.2 µm
```

### EDM Applications

Ideal for: hardened tool steels (H13, D2, M2), carbide, exotic alloys, thin fragile features, no cutting force (no deflection or distortion).

Not suitable for: non-conductive materials (ceramics, polymers), very large material removal (slow process).

---

## Tool Materials and Coatings

```
CUTTING TOOL HIERARCHY
────────────────────────────────────────────────────────────────
HSS (High Speed Steel)    M2, M42     Slowest, most impact resistant
                                       Drills, taps, form tools
                                       Regrindable, cheap

Cermet                    TiC+Ni      Finishing steel at high speed
                                       Good edge retention, brittle

Carbide (uncoated)        WC+Co       10× harder than HSS
                                       Grades: C1–C8 (roughing→finish)

Carbide (coated)          CVD TiN     Standard production insert
  TiN  → general purpose  PVD AlTiN   AlCrN, TiSiN
  TiCN → wear resistance  coating     extended tool life
  TiAlN → high-temp ops   CVD Al₂O₃
  Al₂O₃ → thermal barrier

CBN                       Cubic BN    Hardened steel > 45 HRC
                                       Hard turning (replaces grinding)
                                       Brittle, expensive

PCD                       Polycrystal  Non-ferrous, composites, carbon
  (Polycrystalline         Diamond      Cannot cut steel (reacts)
   Diamond)                             Highest wear resistance
```

---

## Cutting Fluids

```
FUNCTION: Cool, lubricate, flush chips, prevent BUE

TYPE              BASE        BEST FOR           AVOID
──────────────────────────────────────────────────────────────────
Straight oil      Mineral oil High lubricity     Cast iron (fire)
                              Threading, broach  High-speed
Soluble oil       Water+oil   General machining  Aluminum (corrosion)
(flood coolant)   emulsion    Good cooling       (add inhibitor)
Synthetic         No oil      High-speed alum    Grinding of steel
                  solution    and cast iron      (less lubricity)
Semi-synthetic    Partial oil Compromise         Depends on ratio
MQL               Micro-mist  Titanium, Inconel  High material removal
(min. quantity    near tool   aerospace apps     rate operations
 lubrication)                 environmental
Air blast         Compressed  Cast iron          Materials that need
                  air         ceramics           lubrication
```

---

## Decision Cheat Sheet

| I need to make... | Process |
|-------------------|---------|
| Cylindrical OD features | Turning (lathe) |
| Flat faces, pockets, slots | Milling |
| Precision ID bore | Boring bar (lathe or boring mill) |
| Hardened steel cavity | EDM (sinker) |
| Complex profile external | Wire EDM or 5-axis milling |
| Final surface finish, tight tol | Grinding |
| Cylinder bore, Ra < 0.4 µm | Honing |
| Flat surface, Ra 0.2 µm | Surface grinding |
| Internal spline or keyway | Broaching |
| Titanium complex aerospace part | 5-axis CNC with climb milling |

---

## Common Confusion Points

**Climb vs conventional milling**: On manual machines with backlash, climb milling grabs — conventional is required. On CNC with ballscrews (zero backlash), climb is always preferred — better finish, longer tool life, less heat.

**Grinding burn detection**: A tempered surface looks normal visually. Acid etch (Nital etch test) shows over-tempered zones as dark patches, re-hardened zones as white. Barkhausen noise testing is non-contact and production-capable.

**SFM vs RPM**: Cutting speed (SFM or m/min) is the property of the material-tool pair. RPM is what you set on the machine. RPM = (SFM × 12) / (π × D) for inches. At larger diameters, RPM must drop to maintain the same SFM.

**MQL vs flood**: MQL (minimum quantity lubrication) uses a near-dry air-oil mist directly at the cutting zone. Thermal management is primarily via chip evacuation and air convection. Works well for titanium (which degrades with water-based coolants in some regimes) and for dry machining where flood is impractical.

**Carbide grade selection**: Lower cobalt content = harder, more wear resistant, more brittle. Higher cobalt = tougher, better for interrupted cuts. Coarse grain = tougher. Fine grain = sharper edge. C1 = rough cast iron; C8 = precision aluminum.
