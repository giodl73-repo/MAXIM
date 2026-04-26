# Construction Materials — Glass and Curtain Wall Systems

## The Big Picture: Glass and Facade Systems

```
FACADE SYSTEM TAXONOMY
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  MASONRY            FRAMED INFILL        CURTAIN WALL         POINT-FIXED    │
│  (loadbearing)      (non-structural)     (non-structural)     (structural    │
│  ┌────────────┐     ┌────────────┐       ┌────────────┐        silicone/bolt)│
│  │Brick/stone │     │Alum. frame │       │Stick-built │       ┌────────────┐ │
│  │self-loads  │     │+ glass/GRC │       │Unitized    │       │Spider fitt.│ │
│  │wall        │     │panel       │       │SSG (no ret.)│       │Patch fitting│ │
│  └────────────┘     └────────────┘       └────────────┘       └────────────┘ │
│  Structural          Load from frame      Load from façade     Minimal frame  │
│  integral           to slab edge         mullion to anchor     tension glass  │
│                                                                              │
│  GLASS TYPES                    IGU (INSULATED GLAZING UNIT)                │
│  ┌───────────────────────────┐   ┌──────────────────────────────────┐        │
│  │ Float (annealed)          │   │  ┌─────┐gap┌─────┐             │        │
│  │ Tempered (toughened)      │   │  │Glass│   │Glass│             │        │
│  │ Heat-strengthened         │   │  └─────┘   └─────┘             │        │
│  │ Laminated (PVB/SGP/EVA)   │   │  spacer bar + desiccant        │        │
│  │ Borosilicate              │   │  gas fill: Ar / Kr               │        │
│  └───────────────────────────┘   └──────────────────────────────────┘        │
│                                                                              │
│  SOLAR CONTROL                    THERMAL PERFORMANCE                        │
│  ┌───────────────────────────┐   ┌───────────────────────────────────┐      │
│  │ Low-e coating             │   │ Centre-of-glass U-value           │      │
│  │ SHGC control              │   │ Edge/frame thermal bridge         │      │
│  │ Automated blinds/shading  │   │ Condensation risk (dew point)     │      │
│  └───────────────────────────┘   └───────────────────────────────────┘      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Glass Types and Manufacturing

### Float Glass (Pilkington Process, 1959)

Float glass is the substrate for virtually all architectural glass worldwide.

```
FLOAT GLASS PRODUCTION PROCESS
──────────────────────────────────────────────────────────────────────────────
  RAW MATERIALS:
    SiO₂ (silica sand):    73%  ← glass former; melts at 1,713°C
    Na₂O (soda ash):       14%  ← network modifier; lowers melting point
    CaO (limestone):        9%  ← stabilizer; durability
    MgO, Al₂O₃, K₂O:       4%  ← minor components; process control

  PROCESS:
  1. Batch melting: raw materials → furnace at 1,550–1,600°C → molten glass
  2. Float bath: molten glass flows onto molten tin (Sn, mp 232°C)
     → glass floats; surface tension flattens both faces perfectly
     → tin temperature profile: 1,100°C at entry → 600°C at exit
     → glass solidifies as flat, parallel-face sheet without grinding/polishing
  3. Lehr (annealing oven): controlled cooling 600°C → 200°C
     → relieves thermal stresses; glass is annealed (no residual stress)
  4. Cut to size, inspect, dispatch

  STANDARD THICKNESSES:
  2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 25 mm
  Standard sheet: 3.21 m × 6 m (common jumbo); up to 3.21 m × 9 m

  PROPERTIES (soda-lime-silica glass):
    E = 70 GPa
    ν = 0.22
    ρ = 2,500 kg/m³
    σ_t = 45 MPa (annealed — this is LOW; only ~1–2 MPa allowable design tensile)
    λ = 1.0 W/mK
    α_T = 9 × 10⁻⁶ /°C
    Mohs hardness: 5.5–6
```

### Thermally Toughened (Tempered) Glass

```
TOUGHENING PROCESS
──────────────────────────────────────────────────────────────────────────────
  THERMAL TOUGHENING:
  1. Heat annealed glass to ~680–700°C (near softening point)
  2. Rapid air quench on both surfaces
     → surface cools and contracts while core still hot
     → when core finally cools: it wants to contract but is constrained by
        already-rigid surface → core in TENSION; surface in COMPRESSION

  STRESS PROFILE:
  Surface compression:   ~70–170 MPa
  Core tension (balancing): ~35–85 MPa at centre
  (Surface residual stress must be measured: GASP polarimetry, or Scattered Light)

  EFFECT:
  To break glass in tension: applied tensile stress must first overcome
    surface compression before net tension occurs
  → apparent tensile strength: 120–170 MPa (vs 45 MPa annealed)
  → 3–5× stronger in bending

  FAILURE MODE (critical point):
  Once core tension is released (crack initiates): TOTAL FRAGMENTATION
  → shatters into thousands of small cube-like dice (± 40 mm² each)
  → no large shards → safe failure mode
  → but no post-fracture integrity → facade loses weather protection instantly

  CHEMICAL TOUGHENING:
  Glass immersed in molten potassium nitrate bath at ~400°C
  K⁺ ions (larger) exchange with Na⁺ ions (smaller) in glass surface
  → compressed surface layer (K⁺ forced in → residual compression)
  Surface compression: up to 700 MPa (much higher than thermal)
  Depth of compression layer (DOL): 20–50 μm (thin)
  Used for: thin glass (< 4 mm); screens/devices; not standard construction
```

### Heat-Strengthened Glass

Between annealed and fully toughened. Heated to ~580–620°C then quenched (slower
than toughening). Surface compression: ~25–50 MPa. Strength ~2× annealed.
Failure: large shards (not diced). Used where breakage residue integrity needed
(overhead glazing).

### Laminated Glass

Two or more glass plies bonded by interlayer material, usually in autoclave.

```
LAMINATED GLASS INTERLAYERS
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  INTERLAYER       MATERIAL           PROPERTIES                              │
│  ─────────────────────────────────────────────────────────────────────────   │
│  PVB              Polyvinyl butyral  Most common; flexible; good post-       │
│  (polyvinyl       Thickness: 0.38,   fracture glass adhesion; clear/tinted   │
│  butyral)         0.76, 1.52 mm      Shear modulus G: 0.4–2 MPa (rate-dep.)  │
│                                      → creep-compliant for long-term loads   │
│                                                                              │
│  SGP (SentryGlas) Ionoplast polymer  Stiffer (G ~ 65 MPa); higher strength   │
│                   Thickness: 0.89,   Better structural performance;          │
│                   1.52, 2.28 mm      Point-fixed glazing; overhead           │
│                                      50× stiffer than PVB; 5× stronger       │
│                                                                              │
│  EVA              Ethylene vinyl     For laminating non-float glass;         │
│                   acetate            solar panels; humid environments        │
│                                                                              │
│  POST-FRACTURE BEHAVIOUR:                                                    │
│  Single glass lite fractures → fragments adhere to interlayer                │
│  → "broken but holding" → weather protection maintained temporarily          │
│  → THIS is why laminated is required for overhead, structural, fall hazard   │
│                                                                              │
│  BUILDING USES:                                                              │
│  Overhead glazing:  must be laminated (HSG + PVB or T + PVB, or T + SGP)   │
│  Balustrade glass:  must be laminated (structural; post-fracture integral)   │
│  Safety glass (BS EN 12600): impact performance Class 1B1 (BS 6206)        │
│  Bulletproof glass: multiple laminates (polycarbonate + glass; 25–50 mm)   │
│  Blast glazing:     laminated with thicker PVB or SGP; stiff frame critical  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Insulated Glazing Units (IGUs)

### IGU Construction

```
IGU CROSS-SECTION (double-glazed unit)
──────────────────────────────────────────────────────────────────────────────

  Outer lite  ←  glass (e.g., 6 mm tempered)
  ──────────────────────────────────────────
       ↕ gap (12–20 mm Ar or Kr)
  ──────────────────────────────────────────
  Spacer bar: aluminium (traditional) or warm-edge spacer
  Desiccant: molecular sieve / silica gel packed in spacer
  Primary sealant: polyisobutylene (PIB) at inner edge
  Secondary sealant: silicone or polysulfide at outer edge
  ──────────────────────────────────────────
  Inner lite  ←  glass (e.g., 6 mm annealed + low-e coating on face 3)
  ──────────────────────────────────────────

  GAS FILL COMPARISON:
    Air:    λ = 0.024 W/mK; μ = 1  (reference)
    Argon:  λ = 0.016 W/mK  (34% lower) → cheaper, common
    Krypton: λ = 0.009 W/mK (63% lower) → expensive; used in narrow gaps
    Argon at 12–16 mm optimum gap (wider → convection currents reduce benefit)
    Krypton optimum gap: 8–12 mm (allows thinner profiles)

  GLASS SURFACES (numbered from outside in):
    Face 1: outer face of outer glass (exterior)
    Face 2: inner face of outer glass (in cavity)
    Face 3: outer face of inner glass (in cavity) ← best for soft-coat low-e
    Face 4: inner face of inner glass (interior)
    Soft-coat low-e on Face 3: protected in cavity; high emissivity reduction
    Hard-coat low-e on Face 2 or 4: exposed; more durable; lower performance

  CENTRE-OF-GLASS U-VALUE (W/m²K):
    Single clear glass 6mm:    U_cog = 5.8
    Double (6+16Ar+6):         U_cog = 1.1 (with low-e Face 3)
    Double (4+12Ar+4) low-e:   U_cog = 1.2–1.4
    Triple (4+14Ar+4+14Ar+4):  U_cog = 0.5–0.7 (with 2 low-e coatings)
    Passivhaus requires:       U_w ≤ 0.80 W/m²K (whole window including frame)
      → need triple glazing + warm-edge spacer + thermally broken frame
```

### Thermal Bridging at Spacer Bar

```
THERMAL BRIDGING IN IGU: SPACER BAR SIGNIFICANCE
──────────────────────────────────────────────────────────────────────────────
  Traditional aluminium spacer bar:
    λ_Al = 160 W/mK → high conductivity along spacer
    Conducts heat from warm inside glass to cold cavity edge
    → COLD SPOT at edge of glass → condensation risk; increased U-value

  Warm-edge spacer alternatives:
    Thermix TX.N (stainless steel hybrid):  λ ~ 0.2 W/mK
    TGI (fibreglass + silicone):            λ ~ 0.1 W/mK
    Swisspacer:                              λ ~ 0.1 W/mK

  EFFECT ON WINDOW ENERGY BALANCE:
    Aluminium spacer IGU:   edge U-value ~ 3.5 W/m²K (hot spot to cold)
    Warm-edge spacer IGU:   edge U-value ~ 1.8 W/m²K
    Whole-window U-value improvement: ~0.1–0.3 W/m²K from spacer bar alone
    → small windows (high edge:area ratio) benefit most

  CONDENSATION RISK:
    Glass inner surface temperature < dew point → condensation
    Surface temp formula:  T_surf = T_indoor − U_local × (T_indoor − T_outdoor)
    Low surface temp (U high) → condensation on warm side → mould risk
```

---

## Low-e Coatings: Solar Control

### Hard Coat vs Soft Coat

```
LOW-E COATING COMPARISON
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  HARD COAT (pyrolytic):                                                      │
│    Applied during float glass production while glass is still hot (~600°C)   │
│    Chemical vapour deposition (CVD) onto hot ribbon                          │
│    Doped tin oxide (SnO₂:F) layer; ~300 nm thick                             │
│    Chemically bonded to glass → very durable                                 │
│    Can be used on Face 2 (exposed position) without deterioration            │
│    Emissivity: ε ~ 0.15–0.2 (moderate performance)                           │
│    Slight haze sometimes visible                                             │
│                                                                              │
│  SOFT COAT (sputtered, offline):                                             │
│    Applied after float production in separate magnetron sputtering machine   │
│    Multiple thin metallic/oxide layers deposited by sputtering               │
│    Typical stack: SiO₂ / Ag / NiCr / SiO₂ (silver is the active layer)    │
│    Silver layer: IR-reflective; very thin (~10 nm)                           │
│    Chemically delicate: must be protected in IGU cavity (Face 3 or Face 2) │
│    Cannot be exposed to atmosphere → SEALED in IGU                           │
│    Emissivity: ε ~ 0.02–0.05 (high performance; much better than hard coat)  │
│    Best U-value improvement → used in all Passivhaus-grade glazing           │
│                                                                              │
│  KEY METRICS FOR SOLAR GLAZING:                                              │
│                                                                              │
│  EMISSIVITY (ε):                                                             │
│    Measure of longwave (thermal) IR radiation from surface                   │
│    Normal glass: ε ~ 0.84 (like a black body)                                │
│    Low-e coating: ε ~ 0.02–0.20                                              │
│    → low ε → reflects room heat back into room (winter benefit)              │
│                                                                              │
│  SHGC (Solar Heat Gain Coefficient):                                         │
│    Fraction of solar radiation transmitted through window (0–1)              │
│    High SHGC (0.4–0.7): cold climates → welcome solar gain                 │
│    Low SHGC (0.2–0.35): hot climates / south-facing offices → reject solar   │
│    Can control SHGC independently of U-value with appropriate coatings       │
│    "Solar control" glass: absorbs or reflects near-IR spectrum selectively   │
│                                                                              │
│  VISIBLE TRANSMITTANCE (VT or T_vis):                                        │
│    Fraction of visible light transmitted (0–1)                               │
│    Clear: T_vis ~ 0.80–0.88                                                  │
│    Tinted: T_vis ~ 0.35–0.60 (but also blocks daylight)                    │
│    High-performance low-e: T_vis ~ 0.60–0.70 (light in; IR out)            │
│    → "selective" coatings: high VT + low SHGC = best of both worlds        │
│    Light-to-solar-gain ratio (LSG = VT/SHGC): > 1.25 = good selective glass│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Curtain Wall Systems

### Stick-Built vs Unitized

```
CURTAIN WALL SYSTEM COMPARISON
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  STICK-BUILT:                                                                │
│  ─────────────────────────────────────────────────────────────────────────   │
│  Mullions (vertical) and transoms (horizontal) installed piece by piece      │
│  on site; glazing units inserted after frame                                 │
│                                                                              │
│  SECTION ELEVATION:                                                          │
│  ─────────────────────────────── structural floor slab edge                  │
│  │          │          │                                                     │
│  │  glass   │  glass   │  ← glass units held by pressure plate + gaskets   │
│  │          │          │                                                     │
│  │──────────│──────────│ ← transom (horizontal; spans mullion to mullion)    │
│  │          │          │                                                     │
│  │  glass   │  glass   │                                                     │
│  │          │          │                                                     │
│  mullion  mullion  mullion ← span floor to floor; load to slab               │
│  ─────────────────────────────── structural floor slab edge                  │
│                                                                              │
│  Advantages: flexible; can accommodate irregular geometry                    │
│  Disadvantages: extensive site work; weather exposure during installation    │
│    sequence; difficult quality control                                       │
│                                                                              │
│  UNITIZED:                                                                   │
│  ─────────────────────────────────────────────────────────────────────────   │
│  Factory-assembled panels (typically one floor height × one bay width)     │
│  Delivered to site; hoisted by tower crane; hook-on to edge of slab        │
│  Stack-joint at top/bottom of each panel: vertical drainage path           │
│                                                                              │
│  Advantages: factory quality; speed (1 bay/day/crane); parallel production │
│  Disadvantages: high tooling cost; inflexible (changes → whole panel);     │
│    shipping volume; crane-dependent installation                             │
│                                                                              │
│  STACK JOINT DETAIL (critical for weather tightness):                        │
│  ┌──────────────┐  ← upper panel (head frame)                                │
│  │ ╔══════════╗ │  ← glass unit                                              │
│  │ ║          ║ │                                                            │
│  │ ╚══════════╝ │  ← glass unit                                              │
│  ├──────────────┤  ← stack joint: interleave male/female profiles            │
│  │ ╔══════════╗ │  ← glass unit                                              │
│  │ ║          ║ │                                                            │
│  │ ╚══════════╝ │                                                            │
│  └──────────────┘  ← lower panel (sill frame)                                │
│  Rainwater enters joint → drained to exterior via weep holes                 │
│  Two-stage sealing: outer barrier (rain screen) + inner air seal           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Structural Silicone Glazing (SSG)

SSG eliminates mechanical glass retention — silicone adhesive is the ONLY structural
connection between glass and aluminium frame.

```
SSG STRUCTURAL SILICONE DESIGN
──────────────────────────────────────────────────────────────────────────────
  SILICONE: 2-part neutral-curing structural silicone (e.g., Dow 795, GE SCS2000)
    E: 0.8–2.0 MPa (viscoelastic; modulus rate-dependent)
    Tensile strength: ~0.8–1.4 MPa (design value ~0.14–0.21 MPa with safety factor)
    Elongation at break: 100–300%
    Temperature range: −57°C to +150°C (continuous)
    Fire behaviour: B2 / E (combustible; check local codes)

  JOINT SIZING:
    Bite (structural bond width b): min 6 mm (typical: 10–25 mm)
    Thickness (t): min 6 mm (eccentricity and rotation accommodation)
    b = P_wind_design / (σ_design × 1 m width)
    t: check for rotation capacity; L/t ≤ 3 (do not make too thin)

  ADVANTAGES:
    No visual mullions at glass edges → completely flush facade
    Uniform pressure sealing around perimeter → very low air leakage
    Glass can thermally expand/contract freely (silicone is elastic)

  DISADVANTAGES:
    Cannot replace single glass unit without full silicone re-bonding (access issue)
    Silicone adhesion depends on surface preparation (cleaning, primer critical)
    Facade requires regular inspection; silicone life 20–30 years before reglaze
    Cannot be used for overhead glass (gravity load → creep; use mechanical retainers)
    Requires glazing rebate depth (bite) → heavier framing

  FIRE NOTES:
    SSG systems in fire: silicone softens → glass may fall away after initial intact period
    Fire-rated SSG: uses fire-rated intumescent silicone (specialist products)
```

### Thermal Break in Aluminium Mullions

Aluminium (λ = 160 W/mK) is an excellent thermal bridge. Without interruption, the
inner and outer aluminium extrusion flanks form a continuous conductive path.

```
THERMAL BREAK DESIGN
──────────────────────────────────────────────────────────────────────────────

  WITHOUT THERMAL BREAK:
  Exterior aluminium ─────────────────── Interior aluminium
  (cold)               continuous metal     (warm)
  → heat flows directly through → frame U-value ~ 6–8 W/m²K

  WITH THERMAL BREAK:
  Exterior alum. ─── [polyamide strip] ─── Interior alum.
  (cold)             (insulating insert)    (warm)
  λ_polyamide = 0.25 W/mK vs λ_Al = 160
  → frame U-value ~ 1.5–2.5 W/m²K (with warm-edge spacer)

  POLYAMIDE (Nylon 6.6 + glass fibre reinforcement):
    Poured polyamide (liquid cast in aluminium groove → machined)
    or Rolled-in isolator (pre-formed section pressed in)
    Tensile strength: ~80 MPa → structurally adequate for mullion loads
    Width of break: 20–34 mm (wider = better thermal but less stiff)

  PASSIVHAUS FRAME U-VALUE TARGET: U_f ≤ 0.80 W/m²K
    → requires wider thermal break (~34mm) + foam fill in frame cavities

  CRITICAL DETAIL: condensation on inner face of window frame
    Frame inner surface temperature must stay > dew point of interior air
    At −15°C exterior, 20°C interior, 50% RH:
      Dew point ≈ 9°C
      Frame inner temp must be ≥ 9°C → requires high-quality thermal break
      Old aluminium windows: inner frame at 5–10°C → chronic condensation
```

---

## Wind Load and Glass Thickness Selection

```
WIND LOAD DESIGN FOR GLASS
──────────────────────────────────────────────────────────────────────────────
  DESIGN WIND PRESSURE:
    q_w = 0.5 × ρ_air × v² × C_p × C_s
    C_p = pressure coefficient (varies by position: corner zones highest)
    At 45m height, open country: q_w ≈ 1.2–2.0 kPa for standard ULS

  GLASS BENDING:
    Plate bending → σ = α × q × a² / t²  (α = factor from support conditions)
    Simple support all-around, square panel (1:1 aspect):  α = 0.044
    → for 1.5m × 1.5m panel, q = 1.5 kPa, t = ?
    Target σ ≤ allowable (tempered: ~50 MPa design; annealed: ~8 MPa)
    Solve for t: minimise panel size or increase thickness

  GLASS SELECTION APPROACH (BS EN 13474 / prEN 16612):
    Characteristic tensile strength:
      Annealed: f_g,k = 45 MPa
      Heat-strengthened: f_g,k = 70 MPa
      Tempered: f_g,k = 120 MPa
    Design: f_g,d = k_mod × k_sp × f_g,k / γ_M  (with load duration factor k_mod)
    Longer duration loads → lower k_mod (creep in glass? No; statistical load effect)

  DEFLECTION LIMIT:
    EN 13830 for curtain wall: deflection ≤ span/200 but ≤ 15 mm
    Non-linearity: thin glass panes in wind → membrane action kicks in at large deflection
    → actual stiffness greater than linear plate theory at δ > t/2

  EDGE TREATMENT:
    Cut edge: weakest (surface microcracks at cut → stress concentration)
    Seamed edge: slight rounding → improved
    Polished edge: best surface quality → highest strength
    → edge strength governs in systems where edge is loaded (bolt holes, SSG bite)
```

---

## Double-Skin Facades and BIPV

### Double-Skin Facade

```
DOUBLE-SKIN FACADE TYPES
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  MULTI-STORY:  buffer zone full height of building                           │
│  ──────────────────────────────────────────────────────────────────────────  │
│  Outer skin: single glass (usually toughened laminated)                      │
│  Cavity: 300mm–2m+; automated blinds; sometimes walkable                   │
│  Inner skin: thermal IGU; operable vents                                     │
│  Stack effect: warm air rises in cavity → draws fresh air from base          │
│  Result: inner skin sheltered from wind → vent inner skin without draft      │
│  Problem: fire spread up cavity → fire stops at each floor level mandatory   │
│                                                                              │
│  CORRIDOR (SHAFT BOX) TYPE:  each floor is self-contained cavity bay         │
│  ──────────────────────────────────────────────────────────────────────────  │
│  Cavity divided horizontally at each floor level                             │
│  Ventilated by openings in outer skin at each bay                          │
│  → better fire containment; no stack effect                                  │
│  → most common in UK/EU commercial buildings                                 │
│                                                                              │
│  ENERGY PERFORMANCE:                                                         │
│  Winter: cavity acts as thermal buffer → reduces heat loss from inner skin   │
│  Summer: cavity can overheat → automated vents + blinds critical             │
│  Net energy performance depends heavily on control system sophistication     │
│  Energy modelling essential (EnergyPlus, IES-VE, TRNSYS)                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### BIPV (Building-Integrated Photovoltaics)

```
BIPV GLASS OPTIONS
──────────────────────────────────────────────────────────────────────────────
  CRYSTALLINE SILICON IN GLASS:
    PV cells laminated between two glass lites (as IGU inner or outer)
    Cells visible as dots/stripes → semi-transparency possible (designed spaced cells)
    Efficiency: monocrystalline ~20%; polycrystalline ~16%
    Power density: ~150–200 W/m²
    Connection: junction boxes routed in frame → wiring to inverter

  THIN-FILM AMORPHOUS SILICON:
    Deposited directly on glass (like a coating)
    Uniform appearance (no individual cells visible) → better aesthetics
    Efficiency: ~6–12%
    Better performance at high temperatures and diffuse light

  INTEGRATION ISSUES:
    Heat build-up: PV efficiency drops ~0.4–0.5% per °C above 25°C STC
    → ventilated cavity behind PV glass → keep cells cooler → +5–10% yield
    Fire: PV in facade → DC cables; DC arc fault → fire ignition risk
    → arc fault detection mandatory; rapid shutdown compliance (NEC 2014+)
    Structural: glass IGU with PV cells: as laminated IGU; safety glass rules apply
    Maintenance: no moving parts; ~0.5% annual degradation typical
    Economic: BIPV vs rack-mounted PV: BIPV more expensive/W but replaces cladding
```

---

## Point-Fixed Glazing: Spider Fittings

```
POINT-FIXED GLAZING SYSTEMS
──────────────────────────────────────────────────────────────────────────────
  CONCEPT: glass suspended or supported at discrete points (holes or clamps)
    No continuous frame → maximum transparency → structural glass aesthetic

  PATCH FITTING (fin-glass):
    Countersunk stainless bolt through countersunk hole in glass
    Toughened or toughened-laminated glass only (bolt hole stress)
    Stress concentration at hole → toughened pre-compression essential
    Hole must be min 50mm from edge; hole diameter typically 15–25mm

  SPIDER FITTING:
    Cast or machined stainless steel "spider" with 2, 3, or 4 arms
    Each arm bolts through adjacent glass corner holes
    Spider connects to fin glass, cable, or structural steel

  PLANAR GLAZING:
    Glass panels hang from top fixing; bolt to adjacent panels via spider
    Wind load transferred panel-to-panel → support structure at top only
    Used for: full-height atria; facades; facades without visible frame

  STRUCTURAL REQUIREMENTS:
    Glass edge distance: min 5 × glass thickness from edge to hole centre
    Hole diameter to glass thickness: ≥ 1:1.5 (thicker → larger hole possible)
    Toughened: required (hole cannot be drilled in tempered glass → pre-drill then temper)
    Connection: spherical ball joint at fitting → accommodates glass rotation/thermal

  FAMOUS EXAMPLES:
    Canary Wharf DLR station canopy (London): planar glazing
    Apple stores: flush glass facades and structural glass stairs
    Broadgate Arena (London): glass frameless walls, fin-supported
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Overhead glazing — which glass? | Laminated mandatory (e.g., tempered + SGP interlayer); never single lite |
| Structural silicone for overhead glass? | No — silicone creeps under sustained gravity load; use mechanical retainers |
| Best U-value single IGU achievable (standard components)? | ~0.5 W/m²K (triple + two soft-coat low-e + krypton fill + warm edge + thermally broken frame) |
| South-facing glass in offices — cooling dominated? | Specify low SHGC (0.2–0.3); secondary shading still best practice |
| High SHGC when needed? | North-facing residential in cold climate; passive solar heating strategy |
| Tempered glass breaks — fragments safe? | Yes — thermally toughened: small dice. But no post-fracture residual capacity. |
| SSG vs stick-built — which for speed? | Unitized SSG panels: fastest on-site erection; highest factory cost |
| Thermal break width — trade-off? | Wider = better thermal; narrower = stiffer mullion. Typically 20–34 mm. |
| Argon vs krypton fill? | Argon: cheaper, adequate for 12–16 mm gap. Krypton: thinner gap (8–12 mm); higher cost. |

---

## Common Confusion Points

**Tempered glass cannot be cut after tempering.** The surface compression extends to
within 2–4 mm of all edges. Cutting after tempering shatters the glass. All cutting,
drilling, notching, and edge work must be done on annealed glass before toughening.

**Low-e coating does NOT significantly reduce visible light transmission.** Solar
control glass works by selectively reflecting near-infrared (heat) radiation. The
low-e coating target wavelength is 700–2500 nm (heat). Visible light (380–700 nm) is
largely unaffected. A high-performance selective low-e glass can have T_vis = 0.70
and SHGC = 0.25 simultaneously — letting light in while rejecting heat.

**SHGC and U-value are independent parameters.** SHGC controls solar radiation gain
(relevant to summer cooling). U-value controls conductive heat loss (relevant to
winter heating). High-performance glass can optimize both simultaneously. In passive
solar design, you want high SHGC + low U-value for south-facing glass; in office
cooling-dominated buildings, you want low SHGC regardless of U-value.

**Curtain wall is NOT watertight at the first seal.** All well-designed curtain wall
systems use a two-stage drainage principle: an outer rain-screen seal handles most
water; a cavity behind drains any penetration to weep holes at each floor. A
"watertight" first seal is impossible long-term as silicone ages, and trying to achieve
it causes pressure differentials that force water inward when it fails.

**Centre-of-glass U-value ≠ whole-window U-value.** Centre-of-glass U_cog measures
only the glass area, typically 1–2 m from the edge. Whole-window U_w includes the
frame, edge zone (spacer bar thermal bridge), and glass area weighted by area fraction.
For small windows, U_w can be 30–50% higher than U_cog. Passivhaus certificates
specify U_w (whole window), not U_cog.
