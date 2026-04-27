# Contemporary Architecture Movements

## The Big Picture

Contemporary architecture is not a single style. It is a field in productive tension between several major tendencies, each driven by a different forcing function.

```
+--------------------------------------------------------------------+
|              CONTEMPORARY ARCHITECTURE LANDSCAPE                   |
|                                                                    |
|  COMPUTATIONAL /         SUSTAINABILITY          SOCIAL /          |
|  PARAMETRIC              IMPERATIVE              CONTEXTUAL        |
|  ──────────────         ───────────────         ───────────        |
|  Hadid, Gehry, BIG      Mass timber             Adaptive reuse     |
|  Snøhetta, MVRDV        Net-zero / PH           Community-led      |
|  Form follows           Embodied carbon         Participatory      |
|  algorithm              Living Building         Historic context   |
|                         Biophilic design        Jane Jacobs        |
|                                                                    |
|        TECTONIC /            PREFAB /                              |
|        STRUCTURAL            OFFSITE                               |
|        ──────────────        ──────────────                        |
|        Calatrava             Volumetric modular                    |
|        Piano (Rogers)        Panelized systems                     |
|        Glenn Murcutt         DFMA                                  |
|        Structure as          Factory quality,                      |
|        architecture          field speed                           |
|                                                                    |
|  These are not competing — a project can be simultaneously         |
|  parametric, mass timber, biophilic, and prefabricated.            |
+--------------------------------------------------------------------+
```

---

## Parametric and Computational Design

### The Shift from Drafting to Algorithm

The transition from manual drafting to CAD was a tools change. The transition to parametric design was a paradigm change: instead of drawing a shape, you write rules that generate a family of shapes.

```
  PARAMETRIC DESIGN SHIFT
  ========================

  CONVENTIONAL DESIGN:           PARAMETRIC DESIGN:
  Draw this shape.               Write rules that generate shapes.

  Plan with fixed dimensions.    Plan with variable parameters:
  Change one dimension           - Façade density = f(solar exposure)
  → redraw everything.           - Column spacing = f(floor load + program)
                                 - Panel size = f(structure + budget + fab)
                                 Change parameter → all instances update.

  WHAT ENABLES IT:
  Rhino + Grasshopper (McNeel)   Visual programming + NURBS geometry
  CATIA (Dassault)               Originally aerospace/auto → Gehry
  ArchiCAD + Grasshopper         Open BIM + parametric
  Dynamo + Revit (Autodesk)      BIM-integrated parametric
  Python / C# scripting          Code-first geometry generation
```

### Zaha Hadid Architects (ZHA)

ZHA's work represents the most extreme application of computational form to architecture. Key characteristics: continuous flowing surfaces, no right angles, fluid transitions between floor/wall/ceiling.

```
  ZHA DESIGN LOGIC
  =================

  GEOMETRIC BASIS:
  NURBS (Non-Uniform Rational B-Splines): curves defined by
  control points and weights, not arcs or lines.
  Surfaces: swept, lofted, blended NURBS.
  No Euclidean geometry — forms that cannot be described
  by classical geometry.

  STRUCTURAL CHALLENGE:
  A continuously curved surface has no standard structural grid.
  Each element is unique. Connection geometry is non-repetitive.
  Solution: computational structural analysis (CATIA + FEA)
  that generates unique section sizes for each unique element.

  FABRICATION CHALLENGE:
  CNC fabrication of formwork (concrete) or
  laser-cut / CNC-milled steel/aluminum panels.
  Each panel is cut from its own digital file.
  No two panels identical → no economy of repetition.

  COST IMPLICATION:
  ZHA buildings cost 2–4× comparable conventional buildings.
  The aesthetic premium is the client's choice.
  Data: MAXXI Rome, Guangzhou Opera House, CCTV casing.
```

### Frank Gehry / Gehry Technologies

The Bilbao Guggenheim (1997) is the canonical moment when computational fabrication entered mainstream architecture.

```
  GEHRY'S COMPUTATIONAL PROCESS
  ================================

  PHYSICAL MODEL (still primary design tool at Gehry):
  Hand-built crumpled titanium / paper model
             │
             ▼
  3D SCAN / DIGITIZE:
  Model scanned with 3D digitizer
  → point cloud → NURBS surface
             │
             ▼
  CATIA (aerospace software, Dassault):
  Surfaces rationalized into:
  - Flat panels (cheapest)
  - Single-curvature panels (bent sheet, affordable)
  - Double-curvature panels (most expensive, minimize)
             │
             ▼
  UNFOLDING / DEVELOPABILITY:
  Single-curvature surface can be unrolled flat.
  Pattern cut from flat titanium sheet.
  Bent to final curve in factory.
  CNC ensures precision.
             │
             ▼
  TITANIUM CLADDING PANELS (Bilbao):
  0.38mm thick titanium (thinner than US dime).
  33,000 panels, each unique.
  Random-looking surface is actually highly optimized.
  Budget was preserved by eliminating double-curvature panels.

  THE LESSON:
  Digital fabrication decouples complexity of form from
  cost — IF the complexity is resolved into fabricatable
  geometry. A doubly-curved panel costs 10× a flat one.
  Gehry's team eliminates 90% of double-curvature by
  rationalizing to single-curvature equivalents.
```

### BIG (Bjarke Ingels Group)

A different parametric approach: not formal complexity, but diagrammatic logic. BIG's work is legible as a concept diagram before it is legible as a building.

```
  BIG'S DESIGN METHOD
  ====================

  1. START WITH PROGRAM (functional requirements)
  2. APPLY CONSTRAINTS (solar, views, neighbors, code)
  3. GENERATE DIAGRAM (simple geometric operation on program)
  4. EVALUATE: does the diagram solve multiple constraints
     simultaneously?

  EXAMPLES:
  ──────────

  8 House Copenhagen (2010):
  Program: housing + retail + office
  Constraint: all units need daylight + garden access
  Diagram: stack housing on a loop — figure-8 shape
           ground-level loop = street for cyclists
           all units face outward or into courtyard
           penthouse accessible by bike up sloped walkway

  VIA 57 West NYC (2016):
  Program: residential tower on Manhattan west side
  Constraint: courtyard (ground amenity) + views + sunlight
  Diagram: hybrid — courtyard block on one side,
           tower on the other. "Courtscraper."
  Result: single form resolves courtyard + tower typologies.

  AMAGER BAKKE (CopenHill, 2019):
  Program: waste-to-energy plant + public amenity
  Constraint: Copenhagen has no hills → no ski slope
  Diagram: put a ski slope on the power plant roof
  Result: industrial building + ski/hiking amenity
  Carbon emission signal: ring of smoke = one ton CO2 emitted
```

---

## Biomimicry and Structural Form-Finding

### Frei Otto

Frei Otto (1925–2015) developed physical form-finding experiments that presaged computational form-finding by 40 years.

```
  OTTO'S FORM-FINDING EXPERIMENTS
  ==================================

  PROBLEM: What is the optimal shape for a minimal surface?
  (A surface spanning a boundary with minimum area)

  PHYSICAL EXPERIMENT:
  Wire frame dipped in soapy water.
  Soap film automatically forms minimal surface.
  Hang wet mesh from fixed points:
  mesh sags into catenary — the optimal compression form.

  RESULTS:
  Munich Olympic Stadium (1972):
  Tensile cable net (not soap film, but same logic)
  Irregular topography → irregular cable net spans gracefully
  Form found by models, not calculation (calculation verified it)

  Multihalle Mannheim (1975):
  Timber lattice gridshell — curved in two directions
  Form-found by hanging chain mesh upside down
  → invert to get compression surface
  Spans 60m with 50mm timber laths

  CONNECTION TO COMPUTATION:
  Grasshopper "Kangaroo" plugin → physical simulation
  Catenary form-finding → digitally
  Same logic as Otto's physical experiments, now parametric
```

### Grimshaw's Eden Project

```
  EDEN PROJECT GEODESIC DOMES
  ============================

  Program: Botanical biomes (tropical + Mediterranean)
  in an exhausted china clay pit, Cornwall UK (2001)

  CHALLENGE:
  Irregular pit topography → no flat datum for structure
  Solution: Each biome is a set of interlocked geodesic spheres
           Ground-touching point varies per sphere
           No two structural frames identical

  STRUCTURAL LOGIC:
  Hexagonal-pentagonal geodesic subdivision of sphere.
  ETFE (Ethylene Tetrafluoroethylene) pneumatic cushions
  fill each hexagon/pentagon (3 layers, air-inflated,
  transparent, very light, excellent insulation).
  The structure is pure geometry optimization.

  ETFE vs GLASS:
  ETFE:  1% of glass weight; 70% light transmission
         R-4 to R-6 (multi-layer cushion)
         Self-cleaning (rain runs off)
         Flexible → geodesic curvature easy
         Birds don't see it → death risk (vs fritted glass)
  GLASS: heavier, brittle, fixed panels, conventional
```

---

## Mass Timber Revolution

### Why Mass Timber Is Exploding

```
  MASS TIMBER DRIVERS
  ====================

  1. CARBON:
     Concrete cement: ~800 kg CO2/tonne (calcination process)
     Steel (blast furnace): ~1,800 kg CO2/tonne
     CLT (cross-laminated timber): sequesters carbon during growth
     Net: CLT is carbon-positive over full lifecycle

  2. SPEED:
     CLT panels prefabricated in factory
     Arrive on site, crane to position, bolt down
     One floor per week is achievable (vs 2–3 weeks concrete)
     No formwork → no stripping time

  3. SEISMIC:
     CLT is light (1/5 density of concrete)
     Lighter building → smaller seismic force (F = ma)
     Timber is ductile (bends before breaking)
     Post-Northridge: mass timber buildings performed well

  4. BIOPHILIC:
     Exposed wood reduces stress (Kellert / Terrapin Bright Green)
     Occupant preference consistently shown in POE studies
     No acoustic penalty: CLT floors can be acoustic-rated

  5. ECONOMICS:
     Faster schedule = less financing cost
     Lighter structure = smaller foundation
     Often cost-competitive with concrete at 8–15 stories
     Above 20 stories: hybrid (timber floors + concrete core)
```

### Mass Timber Products

```
  MASS TIMBER PRODUCT FAMILY
  ============================

  CLT (Cross-Laminated Timber)
  ────────────────────────────
  Layers of dimensional lumber at 90° angles, glued.
  Layer stack (5-ply CLT):
    layer 1: grain runs 0  deg ( ──────────── )
    layer 2: grain runs 90 deg ( |  |  |  |  )
    layer 3: grain runs 0  deg ( ──────────── )
    layer 4: grain runs 90 deg ( |  |  |  |  )
    layer 5: grain runs 0  deg ( ──────────── )
  Two-way spanning (like a concrete slab)
  Panels: typically 3, 5, or 7 layers
  Panel sizes: up to 3.5m wide × 20m long
  Spans: 4–8m (floor); up to 12m with special design
  Use: floors, walls, roofs

  DLT (Dowel-Laminated Timber)
  ────────────────────────────
  Lumber boards stacked vertically, connected by hardwood
  dowels (no glue, no metal fasteners).
  One-way spanning, but more sustainable (no adhesives).
  Spans: 4–8m typical.

  GLT / Glulam (Glue-Laminated Timber)
  ─────────────────────────────────────
  Horizontal laminations, all parallel grain.
  Used for: beams, columns, arches.
  Spans: 8–40m economically (arches to 80m+).
  Custom curved profiles: glulam arch, glulam portal frame.
  Finish: exposed, stained — architecturally beautiful.

  LVL (Laminated Veneer Lumber)
  ──────────────────────────────
  Thin wood veneers, all parallel grain, glued.
  High, consistent strength.
  Use: headers, beams, rim boards.
  Not exposed architecturally (veneered appearance).

  NAIL-LAMINATED TIMBER (NLT)
  ─────────────────────────────
  Dimensional lumber stood on edge, nailed together.
  Very old system (platform framing era).
  Low tech, low cost, can use local lumber.
  Exposed: beautiful grain lines.
```

### Tall Mass Timber

```
  TALL TIMBER BUILDINGS (2024)
  ==============================

  Building                    Location    Stories  Height  System
  ──────────────────────────────────────────────────────────────────
  Ascent                      Milwaukee   25       87m     GLT+CLT+conc.core
  Brock Commons (UBC)         Vancouver   18       58m     CLT + conc.core
  HoHo Wien                   Vienna      24       84m     Timber-concrete
  Sara Kulturhus              Skellefteå  20       75m     Glulam+CLT
  Mjostarnet                  Brumunddal  18       85.4m   Glulam (tallest timber)

  PATTERN:
  All tall timber buildings use a HYBRID approach:
  - Timber for floors and envelope framing (low weight, fast)
  - Concrete or steel for lateral core (stiffness, fire rating)
  - Below ground: concrete (durability, waterproofing)

  PURE TIMBER to 25+ stories is theoretical.
  Practical upper limit without concrete core: ~12 stories.
  Above that: timber floors + concrete/steel lateral core.

  FIRE CODE:
  IBC 2021 (US): Mass Timber Construction Types IV-A, IV-B, IV-C
  Up to 18 stories (IV-A) with sprinklers + char design
  Some jurisdictions have adopted; others pending.
  EU: varies significantly by country.
```

---

## Adaptive Reuse

### The Embodied Carbon Argument

```
  ADAPTIVE REUSE vs NEW CONSTRUCTION (carbon)
  =============================================

  TYPICAL COMMERCIAL BUILDING:
  Embodied carbon (construction):  ~400 kg CO2/m² (concrete/steel)
  Operational carbon/yr:           ~30–80 kg CO2/m²·yr

  NEW CONSTRUCTION CARBON DEBT:
  Day 1: 400 kg CO2/m² emitted immediately.
  Even with perfect operational performance (15 kWh/m²·yr),
  this debt takes 10–15 years to "repay" vs existing building.

  ADAPTIVE REUSE:
  Embodied carbon in existing structure is already spent.
  Reuse preserves it — no carbon cost to keep existing structure.
  Renovation adds only fit-out carbon (~80–150 kg CO2/m²).
  Net: reuse is dramatically lower carbon than new.

  BEYOND CARBON:
  Character and memory: industrial buildings have spatial quality
  (high ceilings, heavy timber, brick) that new construction
  struggles to replicate.
  Urban grain: historic fabric contributes to neighborhood identity.
  Economics: in many markets, renovation is cheaper than new.
```

### Notable Adaptive Reuse Projects

```
  ADAPTIVE REUSE EXAMPLES
  =========================

  TATE MODERN (Bankside Power Station → Museum):
  Herzog & de Meuron, 2000
  Turbine Hall: 155m × 35m × 34m — one of world's great interior spaces
  Oil tanks (added 2016): found circular geometry preserved
  Lesson: the industrial structure provides spatial quality
          that the new architecture cannot rival. Don't compete — frame it.

  HIGHLINE (elevated freight railway → public park):
  Diller Scofidio + Renfro, 2009–2014
  Steel structure preserved, planted over.
  Catalyzed entire West Side neighborhood transformation.
  Lesson: infrastructure can become public amenity.
          The elevated datum creates urban experience.

  PECKHAM RYELANDS (coal bunker → community center):
  Haworth Tompkins / local partnership, 2015
  Minimum intervention: structure preserved, openings created.
  Lesson: structural limitation is creative constraint,
          not problem to be solved by demolition.
```

---

## Prefabrication and Offsite Construction

### Volumetric Modular

```
  VOLUMETRIC MODULAR CONSTRUCTION
  ==================================

  CONCEPT:
  Complete building modules (box units) built in factory.
  Craned onto site and connected.

  ┌──────────────────────────────────────────┐
  │ FACTORY (controlled environment)         │
  │                                          │
  │ ┌────┐  ┌────┐  ┌────┐  ┌────┐           │
  │ │ M1 │  │ M2 │  │ M3 │  │ M4 │          │
  │ └────┘  └────┘  └────┘  └────┘          │
  │  walls + floors + MEP all installed      │
  └──────────────────────────────────────────┘
               │ transport
               ▼
  ┌──────────────────────────────────────────┐
  │ SITE                                     │
  │         M4 M3                            │
  │         M2 M1     stacked, connected     │
  │         ──────────────                   │
  └──────────────────────────────────────────┘

  ADVANTAGES:
  90% of work in factory: weather-independent, repetitive,
  QC inspectable, labor-controlled.
  Site assembly: crane + bolts. Fast.
  Typical hotel floor: 2–4 modules/day vs 2 weeks conventional.
  Waste: factory can sort and recycle much more efficiently.

  LIMITATIONS:
  Module transport: max road transport: ~4m wide × 13m long
  Interior dimension: ~3.5m wide (structural wall on each side)
  Design flexibility: works for repetitive programs (hotel rooms,
  student housing, student apartments, hospital patient rooms)
  NOT: column-free spaces, complex geometry, custom programs

  EXAMPLES:
  CitizenM hotels: flagship volumetric modular
  AC Marriott NYC: 168 rooms, 90-day site erection
  Brock Commons UBC: hybrid (volumetric + CLT)
```

### Design for Manufacture and Assembly (DFMA)

```
  DFMA PRINCIPLES APPLIED TO BUILDINGS
  =======================================

  MINIMIZE PARTS:
  Standard structural connections vs custom.
  Repetitive facade panels (rationalize geometry).

  MAXIMIZE STANDARDIZATION:
  One window type where possible.
  Same structural bay repeated.
  Same room type replicated (hotel, hospital, housing).

  DESIGN FOR ASSEMBLY SEQUENCE:
  What goes in first? MEP rough-in before walls.
  Top-down construction for basement.
  Crane access all floors during steel erection.

  TOLERANCE:
  Factory tolerance: ±0.5mm
  Site tolerance: ±5–10mm
  Interface detail must accommodate tolerance difference
  (shims, adjustable anchors, oversize holes).

  DFMA PARALLEL TO SOFTWARE:
  Like designing microservices vs monolithic code.
  Modular, interchangeable, testable components.
  Factory testing (commissioning) before installation.
  The "unit test" for a building module is factory QC.
```

---

## Biophilic Design

### What Biophilia Is

E.O. Wilson's biophilia hypothesis (1984): humans have an innate affiliation with other living systems and with the natural world, evolved over millions of years before urbanization.

The design implication: environments that reference natural patterns, processes, and materials are inherently restorative.

### Kellert's 14 Biophilic Design Patterns

```
  BIOPHILIC DESIGN FRAMEWORK (Kellert / Browning / Ryan)
  =========================================================

  NATURE IN THE SPACE:
  1.  Visual connection with nature
  2.  Non-visual connection (sound, smell, touch, taste)
  3.  Non-rhythmic sensory stimuli (natural unpredictability)
  4.  Thermal and airflow variability
  5.  Presence of water
  6.  Dynamic and diffuse light
  7.  Connection with natural systems (seasons, weather)

  NATURAL ANALOGUES:
  8.  Biomorphic forms and patterns (fractal, organic)
  9.  Material connection with nature (wood, stone, water)
  10. Complexity and order (fractal organization)

  NATURE OF THE SPACE:
  11. Prospect (visual access to space)
  12. Refuge (sense of shelter)
  13. Mystery (partially revealed information, inviting exploration)
  14. Risk / peril (controlled sense of danger — edge, height)

  EVIDENCE BASE:
  Roger Ulrich: hospital views → faster recovery (1984)
  Rachel & Stephen Kaplan: attention restoration theory
  — nature restores directed attention (Kaplan 1989)
  Terrapin Bright Green research:
  - 8% increase in wellbeing (biophilic offices)
  - 13% increase in productivity
  - 15% increase in creativity
  These numbers are from consulting research, not RCT —
  treat as directional, not precise.
```

### Living Walls and Green Roofs

```
  LIVING WALLS (Vertical Gardens)
  ==================================

  TYPES:
  Green facade:     Climbing plants on trellis structure
                    (Boston ivy, Virginia creeper)
                    Minimal maintenance; needs ground soil.

  Living wall:      Modular panels with growing media
                    (felt, perlite, coconut fiber)
                    Plants rooted in panels.
                    Irrigation + drainage system built in.
                    Fernand Braudel, Patrick Blanc (pioneer).

  BENEFITS:
  Thermal insulation (air layer + plant mass)
  Evapotranspiration cooling
  Sound absorption (complex surface)
  Biophilic quality (visual + fragrance + life)
  Air quality (marginal — studies mixed for interior plants)

  MAINTENANCE REALITY:
  Living walls die without water and nutrients.
  Maintenance contract is essential.
  Factor 2–3× capital cost over 10 years in maintenance.
  Failed living walls are worse than no living wall.

  GREEN ROOFS:
  Extensive:  60–200mm growing media, sedums, self-sustaining
              Low maintenance, light (80–120 kg/m²)
  Intensive:  300–1,500mm growing media, trees, grass
              High maintenance, heavy (300–1,000+ kg/m²)
              Structural implications: existing roof may not support
  Benefits:   Stormwater retention (60–80% retention during storm)
              Thermal insulation (20–30% reduction in roof heat gain)
              Urban heat island mitigation
              Biodiversity (brownfield biodiversity value)
```

---

## Decision Cheat Sheet

| Design ambition | Contemporary approach | Key consideration |
|-----------------|----------------------|-------------------|
| Complex freeform geometry | Rhino/Grasshopper + rationalization to fabricatable surfaces | Cost is 2–4× conventional unless rationalized |
| Lowest carbon building | Mass timber (CLT/glulam) + adaptive reuse strategy | Check local fire code for mass timber stories |
| Fast hotel construction | Volumetric modular | Design must fit transport limits (≤4m wide module) |
| Biophilic workplace | Views to nature, natural materials (wood, stone), dynamic light, prospect-refuge spaces | POE shows 8–13% productivity gain |
| Adaptive reuse | Structural survey first; embodied carbon assessment; character preservation strategy | Seismic and fire code compliance are the common blockers |
| Tall timber building | Hybrid: CLT floors + concrete core. 8–18 stories pure timber, hybrid above | IBC 2021 Type IV-A/B/C; verify local adoption |
| LEED vs Passivhaus | LEED = points and certification. Passivhaus = physical performance standard | PH is harder to achieve but actually verifies energy use |

---

## Common Confusion Points

**"Parametric" does not mean "computational blob"**: Parametric design is about rule-based relationships between design variables. A parametric floor plan (apartment count varies with lot area) is parametric. Freeform ZHA surfaces are also parametric. The term describes method, not form language.

**Biophilic design ≠ plants**: Biophilic design includes plants (living walls, indoor trees) but also: natural light, natural materials, views, fractal patterns, prospect-refuge geometry, water features, variability (wind movement, flickering light). A wood-clad room with no plants can be more biophilic than a space full of plastic-potted plants.

**Mass timber fire**: Covered in 02-STRUCTURAL-LOGIC. The key counter-intuitive fact: mass timber is more predictable in fire than unprotected steel. The char layer insulates. Building codes took time to accommodate this (IBC 2021 is the US breakthrough). "Timber burns" is true for light-frame. Mass timber is a different material behavior.

**LEED points vs actual performance**: LEED Platinum does not mean the building performs well. It means the design was predicted to perform well and certain credits were documented. The "performance gap" — modeled vs measured energy — is 20–50% in surveys of certified buildings. WELL (health) and Passivhaus (energy) are more performance-anchored because they require measured verification.

**Adaptive reuse vs historic preservation**: They are related but not identical. Historic preservation protects character-defining features of buildings with historical significance. Adaptive reuse is the broader strategy of finding new uses for any existing building (historic or not) to avoid demolition. A 1970s concrete office building with no historic value is still a candidate for adaptive reuse on carbon grounds.
