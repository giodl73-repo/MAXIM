# Structural Logic in Architecture

## The Big Picture

Every load applied to a building must travel from the point of application through the structure to the ground. This is the load path. The architect does not calculate the load path — the structural engineer does — but the architect must understand it well enough to generate geometry that makes structural sense, avoid designs that require heroic engineering to achieve, and collaborate productively with the SE.

```
+--------------------------------------------------------------------+
|                    STRUCTURAL LOGIC MAP                            |
|                                                                    |
|  LOADS                  SPANNING SYSTEMS            RESISTANCE     |
|  ─────                  ────────────────            ─────────      |
|  Gravity (dead)         Beam (bending)              Compression    |
|  Gravity (live)         Arch (compression)          Tension        |
|  Wind (lateral)         Truss (triangulated)        Bending        |
|  Seismic (lateral)      Rigid frame                 Shear          |
|  Snow                   Shell / vault               Torsion        |
|  Thermal / movement     Cable / suspension                         |
|                         Tensegrity                                 |
|                                                                    |
|  MATERIALS                          LATERAL SYSTEMS               |
|  ─────────                          ──────────────                 |
|  Concrete (strong in compression)   Moment frame (ductile)        |
|  Steel (strong in both)             Shear wall (stiff)            |
|  Timber (moderate both)             Braced frame                  |
|  Masonry (compression only)         Core + outrigger (tall)       |
|                                                                    |
|  EXPRESSION                                                        |
|  ─────────                                                         |
|  Exposed (structure = aesthetic element)                           |
|  Concealed (structure hidden, architecture independent)            |
+--------------------------------------------------------------------+
```

---

## Load Path Logic

### Types of Loads

```
  LOAD CLASSIFICATION
  ===================

  DEAD LOADS (DL)              LIVE LOADS (LL)
  ───────────────              ───────────────
  Self-weight of structure     Occupancy loads (people, furniture)
  Permanent finishes           Snow loads (roof)
  Fixed mechanical equipment   Movable equipment
  Soil pressure (basements)    Construction loads
  Hydrostatic pressure
                               DATA CENTER LIVE LOADS:
  ENVIRONMENTAL LOADS          Office floor:        50 psf (2.4 kPa)
  ──────────────────           Computer room floor: 100–200 psf
  Wind (lateral + uplift)      Server room (raised): 250–2,000 psf
  Seismic (lateral + vertical) Transformer room:    400+ psf
  Thermal expansion
  Settlement / creep
```

### The Gravity Load Path

```
  GRAVITY LOAD PATH (typical multi-story)
  =========================================

  ROOF LOADS
      │ (dead: roofing, structure; live: snow, maintenance)
      ▼
  ROOF STRUCTURE (decking / slab)
      │ (loads collected, span to beams)
      ▼
  BEAMS / GIRDERS
      │ (transfer to columns)
      ▼
  COLUMNS
      │ (accumulate floor-by-floor)
      ▼
  TRANSFER STRUCTURE (if needed — podium, parking)
      │
      ▼
  FOUNDATION (spread footings, mat, piles)
      │
      ▼
  SOIL / BEDROCK
  ════════════════════════════════════════

  RULE: Every load must have a continuous path to the ground.
  Columns must land on beams or other columns, not in space.
  Beams must land on columns or walls, not in space.
  "Floating" structure is always supported by something — find it.
```

### Lateral Load Path

Wind and seismic loads act horizontally. They require a separate load-resisting system.

```
  LATERAL LOAD PATH
  =================

  WIND / SEISMIC FORCE
  (acts on facade, enters at each floor level)
      │
      ▼
  FLOOR DIAPHRAGM
  (floor slab or decking acts as a rigid plate
   collecting lateral force from all columns)
      │
      ▼
  LATERAL FORCE RESISTING SYSTEM (LFRS)
  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
  │ MOMENT FRAME│  │ SHEAR WALL  │  │BRACED FRAME │
  │             │  │             │  │             │
  │ Rigid beam- │  │ Concrete or │  │ Diagonal    │
  │ column      │  │ masonry     │  │ members in  │
  │ connections │  │ plane. Very │  │ triangulated│
  │ resist      │  │ stiff.      │  │ frame.      │
  │ rotation.   │  │ Concentrates│  │ Stiffer     │
  │ Flexible,   │  │ force in    │  │ than moment │
  │ ductile.    │  │ wall plane. │  │ frame.      │
  └─────────────┘  └─────────────┘  └─────────────┘
      │                  │                 │
      ▼                  ▼                 ▼
  FOUNDATION — transfers all lateral force to ground
  (grade beams, piles, caissons)
```

---

## Spanning Systems

### Beam (Bending)

The simplest spanning element. A beam transfers load to its supports by developing bending stress.

```
  BEAM BENDING
  ============

  Load applied:    ↓   ↓   ↓   ↓   ↓
                   ┌───────────────────┐
                   │   BEAM            │
                   └───────────────────┘
                   ↑                   ↑
               Support             Support

  Internal stress distribution:

  TOP FIBER:    C   C   C   C   C    ← COMPRESSION (beam bows)
  NEUTRAL AXIS: 0   0   0   0   0    ← zero stress
  BOTTOM FIBER: T   T   T   T   T    ← TENSION

  WHY I-BEAMS WORK:
  Most bending stress is at extreme fibers (top/bottom).
  The web (middle) carries shear, not much bending.
  I-shape puts most material where stress is highest.

        ══════════   ← top flange (compression)
           │
           │         ← web (shear)
           │
        ══════════   ← bottom flange (tension)

  Steel is strong in both compression and tension → efficient I-beam
  Concrete is weak in tension → bottom flange fails without reinforcing

  ECONOMIC SPANS:
  Steel W-shape beam:   20–50 ft (6–15m)
  Concrete beam:        15–35 ft (5–10m)
  Timber glulam:        20–60 ft (6–18m)
  Prestressed concrete: 30–80 ft (9–25m)
```

### Arch

The arch is a fundamentally different structural logic: it converts bending into axial compression, which masonry and concrete handle well.

```
  ARCH ACTION
  ===========

                   ↓ load
           ┌───────────────────┐
          /                     \
         /    COMPRESSION        \
        /       (axial only)      \
       /                           \
      /                             \
  ───/─────────────────────────────/───
  ↑                                 ↑
  reaction (vertical + horizontal)  reaction (vertical + horizontal)
  THRUST                            THRUST

  KEY: The arch develops horizontal thrust at the supports.
  This thrust must be resisted by buttresses, tie rods, or the ground.
  If you remove the buttress, the arch collapses sideways.

  GOTHIC CATHEDRAL LOGIC:
  ┌─────┐         ┌─────┐
  │Nave │ →THRUST→│Aisle│ →THRUST→[Flying Buttress]→[Pier]→[Ground]
  └─────┘         └─────┘
  The flying buttress is the arch thrust management system.

  ARCH EFFICIENCY: pure axial compression, no bending.
  All masonry arches, Roman vaults, Baroque domes work this way.
  The structure is purely in compression — masonry's only strong mode.
```

### Truss

A truss is a triangulated frame. Triangles are inherently rigid (unlike squares, which can rack). Each member is in pure tension or pure compression — no bending.

```
  PRATT TRUSS (common in bridges and long-span roofs)
  ════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────┐
  │  ─────────────────────────────────────────────  │  ← top chord (C)
  │   \    |    /    |    \    |    /    |    \  /   │
  │    \   |   /     |     \   |   /     |     X     │
  │     \  |  /      |      \  |  /      |    / \    │
  │  ────────────────────────────────────────────    │  ← bottom chord (T)
  └─────────────────────────────────────────────────┘

  C = compression members (diagonals slope toward center)
  T = tension members (verticals, bottom chord)
  | = vertical web members

  EFFICIENCY: very light relative to span
  DEPTH REQUIRED: typically span/8 to span/12 (deep but light)
  SPACE REQUIREMENT: structural depth is wasted floor-to-floor
  SOLUTION: put mechanical runs through the truss openings

  ECONOMIC SPANS: 50–200 ft (15–60m) common; longer possible
```

### Shell and Vault

Thin curved surfaces in compression. The curvature converts bending into membrane action (in-plane compression), making very efficient structures.

```
  SHELL LOGIC
  ===========

  SINGLE CURVATURE (barrel vault):
  Curved in one direction only.
  Cylindrical surface.
  Thrust at both ends (like a flattened arch).

  DOUBLE CURVATURE (dome, hyperbolic paraboloid):
  Curved in two directions.
  Membrane action in biaxial compression.
  Much more efficient than single curvature.

                    (dome)
               _______________
             /                 \
            /   COMPRESSION     \
           /  everywhere in the  \
          |       surface         |
           \                     /
            \___________________/
             ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
             HOOP TENSION at base
             (rings want to burst outward)
             → managed by steel hoop ring

  WHY THIN SHELLS WORK:
  A 3mm concrete shell 20m in diameter is structurally comparable
  to an eggshell — the curvature does the work, not the thickness.
  The genius of Candela, Nervi, and Saarinen's work.
```

### Cable and Suspension

Pure tension — cables are the structural complement of arches.

```
  CABLE LOGIC
  ===========

  SUSPENSION BRIDGE / TENSILE ROOF:

  ╔═════════════════════════════════════╗
  ║          CABLE (pure tension)        ║
  ╚═════════════════════════════════════╝
   \                                   /
    \     ─────────────────────       /
     \   / COMPRESSION MAST          /
      \ /                           /
       X                           X
      / \                         / \
   anchor                       anchor

  CABLE: 100% tension, no bending, extremely efficient
  MAST: 100% compression (the only compression element)
  DECK: hangs in catenary, transfers live loads to cable

  KEY ISSUE: cables are flexible → large deflections under load
  Need secondary stiffening (orthogonal cables, fabric pretension)
  or accept that the structure moves.

  EXAMPLES: Brooklyn Bridge, Raleigh Arena (Nowicki, 1953 — first
  major cable roof), Frei Otto's Munich Olympic Stadium (1972),
  tensile fabric structures.
```

### Tensegrity

Discontinuous compression members floating in a continuous tension network. Buckminster Fuller coined the term; Kenneth Snelson built the first pure tensegrity sculptures.

```
  TENSEGRITY LOGIC
  ================

                        [T]──────[T]
                       /             \
                      [T]    [C]     [T]
                       \    /   \   /
                        [T]       [T]
                       /             \
                      [T]    [C]     [T]

  C = compression members (disconnected from each other)
  T = tension cables (continuous network)

  No compression member touches another directly.
  All compression is transmitted via the tension network.

  IN ARCHITECTURE: rare as primary structure (too flexible for
  most programs). Used aesthetically: Calatrava's cable-stayed
  structures approximate tensegrity logic. Engineering curiosity
  more than mainstream structural system.

  IN BIOLOGY: cells, fascia, and bone microstructure are tensegrity
  systems — another example of optimal natural form appearing in
  both nature and engineering.
```

---

## Materials and Structural Behavior

### Concrete

```
  REINFORCED CONCRETE BEHAVIOR
  =============================

  CONCRETE ALONE:
  - Compressive strength: 3,000–10,000 psi (20–70 MPa)
  - Tensile strength: ~10% of compressive — essentially zero
  - Brittle in tension (cracks, then fails suddenly)

  REINFORCED CONCRETE (RC):
  - Steel rebar placed where tension occurs
  - Concrete handles compression, steel handles tension
  - Together: strong in both, monolithic, moldable

  PRESTRESSED CONCRETE:
  - High-strength steel strands tensioned BEFORE casting
  - Pre-compression eliminates tensile cracking
  - Allows thinner slabs, longer spans
  - Used in: parking structures, bridges, slabs for long spans

  POST-TENSIONED (PT) SLABS:
  - Common in office and residential construction
  - Strands are tensioned AFTER casting
  - Flat-plate slab spans 25–35 ft without beams
  - Favorite for developer-built office — thin floor-to-floor
```

### Steel

```
  STEEL STRUCTURAL BEHAVIOR
  ==========================

  PROPERTIES:
  - Yield strength: 36–50 ksi (Grade 36, Grade 50 common)
  - Equal strength in tension and compression
  - Ductile — deforms before fracturing (critical for seismic)
  - Slender → buckling governs for columns

  BUCKLING:
  - Steel columns are slender; crushing not the governing failure
  - Euler buckling: P_cr = π²EI / (kL)²
  - Solution: lateral bracing, larger sections, moment frames

  MOMENT FRAME:
  - Rigid beam-column connections
  - Frame deforms elastically (and plastically) under lateral loads
  - Ductile — absorbs seismic energy
  - Allows column-free space (no shear walls needed)
  - Common in tall buildings in seismic zones

  LONG SPAN:
  - Steel W-shapes span 40–80 ft economically
  - Trusses to 200+ ft
  - Cable to any span (structural efficiency at its maximum)
```

### Timber

```
  TIMBER STRUCTURAL BEHAVIOR
  ===========================

  TRADITIONAL (sawn lumber):
  - Spans: 12–20 ft typical
  - Moderate strength-to-weight ratio
  - Strong along grain, weak across grain
  - Fire: chars at ~0.5 mm/min; predictable failure behavior

  MASS TIMBER (the revolution):
  ┌─────────────────────────────────────────────────────┐
  │ CLT (Cross-Laminated Timber)                        │
  │ Layers of lumber at 90° angles, glued.              │
  │ Behaves like a concrete slab (two-way spanning).    │
  │ Panels up to 20m long, 3.5m wide.                   │
  │ 5–7 layer panels for floors, 3 layers for walls.    │
  │                                                     │
  │ DLT (Dowel-Laminated Timber)                        │
  │ Dowels instead of glue — more sustainable.          │
  │                                                     │
  │ GLT/Glulam (Glue-Laminated Timber)                  │
  │ Horizontal laminations — for beams and columns.     │
  │ Spans to 40m economically.                          │
  │                                                     │
  │ LVL (Laminated Veneer Lumber)                       │
  │ Thin veneers, all parallel — engineered for         │
  │ consistent strength. Headers, beams.                │
  └─────────────────────────────────────────────────────┘

  FIRE PERFORMANCE REALITY:
  Mass timber chars predictably at ~0.6 mm/min (CLT).
  A 175mm CLT floor panel has a 60-min fire rating.
  The char layer INSULATES the remaining wood.
  Structural failure occurs when remaining cross-section
  falls below required strength — calculable.

  This is counterintuitive but true: mass timber is more
  predictable in fire than unprotected steel, which loses
  50% strength at 550°C (often within 15–20 min of fire).
```

### Masonry

```
  MASONRY STRUCTURAL BEHAVIOR
  ============================

  PROPERTIES:
  - Compressive strength: 1,000–3,000 psi (brick), 1,500–3,500 psi (CMU)
  - Tensile strength: essentially zero (mortar joint fails)
  - Brittle — no warning before failure

  STRUCTURAL FORMS:
  - Bearing wall: masonry carries gravity loads directly
    (works well, but walls must stack floor-to-floor)
  - Arch / vault: masonry in pure compression (its strong mode)
  - Reinforced masonry: steel in voids of CMU, grouted
    (adds tensile capacity, used in seismic zones)

  SEISMIC VULNERABILITY:
  Unreinforced masonry (URM) is the most dangerous building type
  in earthquakes. Brittle, heavy, no ductility.
  Most URM buildings in seismic zones require retrofit.
  Confined masonry (steel frame + masonry infill) performs better.
```

---

## Lateral Force Resistance Systems

```
  LATERAL SYSTEM COMPARISON
  ==========================

  MOMENT FRAME              SHEAR WALL / CORE        BRACED FRAME
  ─────────────             ─────────────────        ─────────────
  Rigid connections         Reinforced concrete       Diagonal members
  between beams             wall or masonry.          in triangulated
  and columns.              Very stiff.               pattern.

  ┌─┐  ┌─┐  ┌─┐           ┌────────────────┐        ┌─┐╲ ┌─┐
  │ │  │ │  │ │            │████████████████│        │ │ ╲│ │
  ─┤ ├──┤ ├──┤ ├─          │████████████████│        ─┤ ├─╳─┤ ├─
  │ │  │ │  │ │            │████████████████│        │ │╱ ╲│ │
  └─┘  └─┘  └─┘           └────────────────┘        └─┘   └─┘

  Ductile (seismic       Stiff (minimal drift)     Stiffer than MF,
  energy absorption)     Concentrates force         but less ductile
  Large plan flexibility High overturning moment   than MF
  Larger beam/column     Forces plan layout         Works in steel
  sections required      (walls consume floor)      and concrete

  TALL BUILDING SYSTEMS:
  ──────────────────────
  Core + outrigger: central concrete core (elevator/stair)
  connected to perimeter columns via outrigger trusses at
  mechanical floors. Very efficient for 30–60 story range.

  Tube: perimeter closely spaced columns acting as a hollow
  tube. Framed tube (WTC), bundled tube (Sears Tower).
  Efficient for 40–100+ stories.

  Diagrid: diagonal grid on exterior — combines gravity and
  lateral resistance. Hearst Tower (Foster), CCTV (Koolhaas/
  Cecil Balmond). Eliminates interior columns.
```

---

## Structural Expression vs Concealment

A core architectural design decision: is the structure an aesthetic element or a hidden infrastructure?

```
  STRUCTURAL EXPRESSION SPECTRUM
  ================================

  EXPRESSED                              CONCEALED
  ─────────────────────────────────────────────────
  Structure IS the architecture.         Structure is hidden behind
  Joints, sections, connections          finishes, ceilings, cladding.
  are carefully detailed as              Architecture independent of
  visual elements.                       structural geometry.

  EXAMPLES:                              EXAMPLES:
  - Eames House (steel frame)            - Neoclassical architecture
  - Kahn's Richards Labs                 - Most commercial office
  - Piano's Pompidou (color-coded        - Cladded skyscrapers
    structure = architecture)            - Traditional masonry
  - Foster's HSBC HK (external          - Drywall over structure
    structure)
  - Nervi's concrete vaults

  NEITHER IS "BETTER" —
  Expression demands structural precision (tolerances tighten).
  Concealment allows structural pragmatism (bolt + cover).

  CRITICAL DECISION POINT:
  In design development, the architect and SE must agree on
  tolerance standards. Exposed steel connections require
  fabrication tolerances 3–5× tighter than covered work.
```

---

## Data Center Structural Context

For large-scale compute facilities (data centers, HPC centers), these structural specifics are directly applicable:

```
  DATA CENTER STRUCTURAL REQUIREMENTS
  =====================================

  FLOOR LOADS:
  Office space:          50 psf live load (2.4 kPa)
  Computer room floor:   100–250 psf (4.8–12 kPa)
  Server row (heavy):    500–2,000 psf (24–96 kPa) — point loads
  UPS room:              300–500 psf
  Transformer vault:     600–1,000 psf
  Raised floor dead:     10–15 psf (tiles + pedestals)

  COLUMN GRID DRIVES LAYOUT:
  40' × 40' grid = standard for white space (matches 2 data rows)
  30' × 60' = better for raised floor lanes (60' direction = aisle)
  Column-free space for raised floor = structural requirement driving
  post-tensioned slab vs. flat-plate design.

  SEISMIC:
  Servers are not structural — but equipment anchorage is critical.
  Zone 2D/3+ requires rack anchorage, raised floor hold-down.
  Structural engineer reviews non-structural equipment anchorage.

  VIBRATION:
  Diesel generators → floor vibration → must be isolated from
  white space structure.
  Solution: spring isolators, separate structural slabs.

  RAISED FLOOR:
  Typical height: 18"–24" (450–600mm)
  Structural connection: pedestal base plate, not structural slab
  Raised floor not rated for seismic unless specifically designed.
```

---

## Decision Cheat Sheet

| Design condition | Structural logic to consider | Key constraint |
|-----------------|------------------------------|----------------|
| Column-free span 20–40 ft | Steel W-shape beam or PT concrete slab | Depth vs floor-to-floor |
| Column-free span 40–80 ft | Glulam / steel truss / long-span concrete | Structural depth requirement |
| Column-free span 80–200 ft | Steel truss, space frame, cable-stayed | Lateral stability of long elements |
| Building in seismic zone | Ductile moment frame or shear wall/core | Drift limits, connection ductility |
| Masonry building, seismic zone | Confined or reinforced masonry | URM is extremely dangerous |
| Tall building (20–40 stories) | Core + shear walls, moment frames | Wind governs above ~25 stories |
| Tall building (40+ stories) | Core + outrigger, tube, diagrid | Overturning moment critical |
| Expressing structure aesthetically | Tight fabrication tolerances | 3–5× cost premium on connections |
| Data center computer room floor | 100–250 psf minimum, check point loads | Column grid must accommodate rack rows |
| Mass timber project | CLT floor, glulam beams, fire char design | Check jurisdiction fire code approval |

---

## Common Confusion Points

**Architect vs Structural Engineer**: The architect sets form and geometry. The SE analyzes forces and sizes members. The architect must give the SE a structurally plausible starting geometry — the SE cannot make an impossible geometry work efficiently. Conversely, the SE should not override architectural decisions without structural justification.

**Dead load vs self-weight**: Self-weight is often the dominant dead load. A concrete floor slab weighs ~12 psf per inch of thickness — a 10" slab is 120 psf dead load before any live load is added. This is why long spans in concrete require careful assessment: the slab depth required to span becomes the dominant load on everything below.

**Fire resistance of steel**: Unprotected steel loses 50% strength at 550°C, which a structural fire can reach in 10–20 minutes. "Fire-rated steel" is protected steel (spray-on fireproofing, intumescent paint, concrete encasement) — not inherently fire-resistant steel. This is why unprotected exposed steel requires sprinkler protection in most codes.

**Mass timber fire**: The common intuition is wrong. Mass timber chars slowly and predictably. Light-frame timber (2×4 studs) is dangerous in fire because small sections burn through quickly. Mass timber (100mm+ sections) retains structural integrity far longer. The char layer is an insulator.

**Shear wall vs moment frame choice**: Shear walls are stiff (small deflections under lateral load) but consume floor plan. Moment frames are flexible (larger deflections) but allow open plans. High-rise buildings in seismic zones often use both — core shear walls for stiffness plus moment frames at perimeter for ductility.
