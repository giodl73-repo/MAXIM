# Building Systems Integration

## The Big Picture

MEP (Mechanical, Electrical, Plumbing) is typically 40–60% of a commercial building's construction cost and is where most of the complexity lives. The architect does not design MEP — but the architect allocates space for it, coordinates it with structure, and must understand it well enough to resolve conflicts before they become field problems.

```
+--------------------------------------------------------------------+
|                    BUILDING SYSTEMS MAP                            |
|                                                                    |
|  ┌─────────────────────────────────────────────────────────────┐  |
|  │                    STRUCTURAL GRID                           │  |
|  │  (column spacing drives everything else)                    │  |
|  └─────────────────────────────────────────────────────────────┘  |
|                          │                                         |
|         ┌────────────────┼─────────────────┐                      |
|         ▼                ▼                 ▼                       |
|  ┌─────────────┐  ┌────────────┐  ┌──────────────┐               |
|  │ MECHANICAL  │  │ ELECTRICAL │  │  PLUMBING /  │               |
|  │             │  │            │  │  FIRE PROT.  │               |
|  │ HVAC ducts  │  │ Panels     │  │ Drain stacks │               |
|  │ AHUs        │  │ Risers     │  │ Supply risers│               |
|  │ Chilled     │  │ UPS rooms  │  │ Sprinkler    │               |
|  │  water      │  │ Lighting   │  │ Gas service  │               |
|  │ Boilers     │  │ BAS/DDC    │  │              │               |
|  └─────────────┘  └────────────┘  └──────────────┘               |
|         │                │                │                        |
|         └────────────────┼────────────────┘                       |
|                          ▼                                         |
|               CEILING PLENUM (the battleground)                   |
|               Ducts + conduit + pipes + sprinklers                |
|               + structure ALL compete for the same space           |
|                          │                                         |
|                          ▼                                         |
|               BIM CLASH DETECTION                                  |
|               (resolves conflicts in design, not field)           |
+--------------------------------------------------------------------+
```

---

## MEP Integration

### The Coordination Challenge

```
  TYPICAL CEILING PLENUM SECTION
  ================================

  STRUCTURAL SLAB (top)
  ─────────────────────
        beam         beam
  ─────────────────────
                              ← beam depth: 18"–36"
  ─────────────────────
  HVAC DUCT MAIN           → 18"–36" deep × 24"–48" wide
  ─────────────────────
  HVAC BRANCH DUCT         → 10"–18" deep × 12"–24" wide
  ─────────────────────
  SPRINKLER MAIN           → 4"–6" pipe + hanger space
  ─────────────────────
  ELECTRICAL CONDUIT       → 2"–4" diameter, horizontal runs
  ─────────────────────
  TELECOM / DATA CABLE     → 2"–4" cable trays
  ─────────────────────
  CEILING GRID             → 1"–2" support structure
  ─────────────────────  ← suspended ceiling
  OCCUPIED SPACE

  ALL OF THE ABOVE must fit between structural slab and
  finished ceiling height.

  If architectural floor-to-floor = 14'-0" and program requires
  9'-0" finished ceiling, the plenum is only 5'-0" = 60".
  Subtract 12" of structure = 48" of plenum.
  Does it all fit? This is the MEP coordination problem.
```

### Mechanical Room Sizing

```
  MECHANICAL ROOM AREA RULES OF THUMB
  =====================================

  Building type            Mechanical room % of GFA
  ──────────────────────────────────────────────────
  Office (VAV system)      3–5%
  Hospital                 6–12% (high mechanical intensity)
  Laboratory               10–20% (fume hoods + exhaust)
  Data center              15–30% (cooling plant, UPS, generators)
  Hotel / residential      2–4%

  VERTICAL DISTRIBUTION:
  Main mechanical room:   Basement or rooftop
  Branch distribution:    Each floor (fan coil units in ceiling)
  or
  Mechanical floors:      Every 10–15 stories in tall buildings
                         (sky lobbies, mechanical floors alternate
                          with occupied floors)

  CRITICAL DIMENSION: Air shaft / duct risers must be
  stacked vertically floor-to-floor. Coordinate with
  structural frame from day one.
```

---

## Structural Grid as Coordination Framework

### Why the Grid Matters

The column grid is the primary organizing element. Every other system — MEP, circulation, program — nests within it. Setting the grid wrong at schematic design creates cascade problems through the rest of the project.

```
  GRID SELECTION BY BUILDING TYPE
  =================================

  OFFICE (typical):
  30' × 30' or 30' × 40'
  - 30' spans span economically in both concrete and steel
  - 60-person floor plate: ~21,000 sqft → 7×10 bay grid
  - Each 30'×30' bay = ~2 open-plan workstations × 8 rows

  PARKING STRUCTURE:
  60' × 60' preferred (fits 3 parking stalls × 2 rows per bay)
  or 60' × 18' (perpendicular to aisle direction)
  - 8.5' stall + 9' stall = 27' parking bay
  - 24' drive aisle (minimum for 90° parking)
  - 60' bay = 27' + 24' + 9' stall edge

  WAREHOUSE / DISTRIBUTION CENTER:
  40' × 40' to 40' × 60'
  - Clear height 28'–40' (fork truck + racking)
  - Grid driven by rack layout, not structural efficiency

  DATA CENTER WHITE SPACE:
  40' × 40' minimum (2 rows of racks + hot/cold aisle)
  or 40' × 60' (better for aisle containment)
  - Standard server rack: 24"–30" wide × 48"–60" deep
  - Hot aisle: 4' minimum (2 rack rows back-to-back)
  - Cold aisle: 3' minimum (2 rack fronts facing)
  - Row of 20 racks: 20 × 30" wide = 50' long
  - 2-row module + aisles = ~40' depth minimum

  HOSPITAL:
  30' × 30' module (patient room = 14'×28' typical)
  or 32' × 32'
  - ICU bay: 200-250 sqft each
  - OR suite: 600-800 sqft floor area + 400 sqft support
  - Nursing unit: 8-16 beds per floor zone
```

---

## Vertical Transportation

### Elevator Sizing

```
  ELEVATOR SYSTEMS
  =================

  TRACTION (cable) ELEVATOR:
  - Standard for buildings over 5 stories
  - Machine room required (traditionally above shaft)
  - Machine-Room-Less (MRL): motor in shaft, no overhead room
  - Gearless traction: premium speed/comfort, 4+ stories
  - Variable-speed drives: current standard

  HYDRAULIC ELEVATOR:
  - For low-rise (2–5 stories)
  - Slower, lower capacity
  - Cylinder requires boring into ground below pit
  - Oil hydraulic fluid = environmental concern
  - Rarely specified for new commercial

  LINEAR MOTOR (MULTI):
  - Thyssen/KONE MULTI: multiple cabins per shaft
  - Horizontal + vertical movement (building loop concept)
  - Not yet mainstream; buildings designed around single-shaft concept

  SIZING RULES OF THUMB:
  ──────────────────────
  Elevator count:    1 elevator per 40,000–50,000 sqft of office
  Cab capacity:      2,000–4,500 lbs (common: 3,500 lb = ~20 persons)
  Speed:             200–800 fpm (floors × 30 fpm rule of thumb)
  Wait time target:  ≤ 30 seconds average during 5-minute peak
  Lobby depth:       Minimum 8'–10' in front of elevator doors
  Shaft core:        Allow 60–70 sqft per cab for shaft + structure

  5-MINUTE PEAK CAPACITY:
  Elevators should handle 12–15% of population in 5 minutes.
  Office building (1,000 people, 8 floors, 200 fpm):
  → 3–4 elevators typically required
  This is the traffic analysis that drives elevator count.
```

### Stair Design

```
  STAIR GEOMETRY (IBC and common standards)
  ===========================================

  RISER HEIGHT:     7" maximum (residential: 8.25")
  TREAD DEPTH:      11" minimum (residential: 9")
  RULE OF THUMB:    2r + t = 24" to 25"
                    (2 × 7" + 11" = 25" — exactly right)

  EXIT STAIR WIDTH: 44" minimum (commercial), per IBC
  EGRESS WIDTH:     0.3" per occupant per floor served
  (at 300 occ per floor, 6 floors = 1,800 → 540" = 45"
   → two 44" stairs = 88" → adequate)

  ADA REQUIREMENTS:
  Riser height:     4" min, 7" max
  Tread depth:      11" minimum
  Handrail height:  34"–38" above tread nosing
  Handrail return:  12" beyond top riser, 1 tread depth at bottom

  FIRE STAIR (exit enclosure):
  - 2-hour fire-rated enclosure
  - Pressurized in high-rise (positive pressure vs smoke)
  - Direct exit to exterior or exit discharge
  - Maximum travel distance to stair: 200' (unsprinklered), 250' (spr)
```

---

## Facade Systems

The facade is the building's primary environmental filter — it mediates between exterior climate and interior conditions. Four main facade systems:

### Curtain Wall

```
  CURTAIN WALL SYSTEM
  ====================

  PRINCIPLE: Facade is suspended from structure, not load-bearing.
  The skin is independent of the floor slabs.

  UNITIZED CURTAIN WALL:
  ┌────────────────────────────────────────────────┐
  │ Floor slab n+1                                 │
  │         │                                      │
  │         ▼ bracket attachment                   │
  │  ┌──────┴───────────────────────────────────┐  │
  │  │       PRE-ASSEMBLED UNIT (factory)        │  │
  │  │  spandrel glass   vision glass            │  │
  │  └───────────────────────────────────────────┘  │
  │         │                                      │
  │         ▼ bracket attachment                   │
  │ Floor slab n                                   │
  └────────────────────────────────────────────────┘

  Units fabricated in factory, shipped, installed in 1-2 day/floor.
  Fastest installation; tight quality control.
  Dominant system for commercial high-rise.

  STICK-BUILT CURTAIN WALL:
  Mullions installed first in field, glass filled in.
  More flexible for complex geometry.
  Slower, more field quality risk.
  Used for smaller projects, complex facades.

  THERMAL PERFORMANCE:
  Aluminum frame (thermally broken):   U ≈ 0.30–0.40 W/m²K
  Triple-glazed unit:                  U ≈ 0.50–0.80 W/m²K
  Overall wall assembly:               U ≈ 0.70–1.20 W/m²K
  (worse than insulated opaque wall — unavoidable physics of glass)
```

### Rainscreen Principle

```
  RAINSCREEN PRINCIPLE
  ======================

  The key insight: you cannot keep ALL rain off a wall.
  Instead, manage it: drain, dry, and protect.

  WRONG (face-sealed):               RIGHT (rainscreen):
  ┌──────────────────┐               ┌───────────────────┐
  │ CLADDING         │               │ CLADDING          │ ← 1. Rain hits
  │ (sealant at      │               │ (open joints ok)  │
  │  every joint —   │               ├──────────── ──────┤
  │  any failure     │               │  DRAINAGE CAVITY  │ ← 2. Water drains
  │  = water         │               │  (25–50mm air gap)│    (not sealed)
  │  intrusion)      │               ├───────────────────┤
  │                  │               │  AIR BARRIER      │ ← 3. Air barrier
  │                  │               │  (airtight)       │    is the real
  └──────────────────┘               │                   │    weather line
                                     │  INSULATION       │
                                     ├───────────────────┤
                                     │  STRUCTURE        │
                                     └───────────────────┘

  AIR BARRIER controls: air infiltration (dominant heat loss)
  WATER-RESISTIVE BARRIER beneath cladding controls: bulk water
  DRAINAGE CAVITY: allows any intrusion to drain harmlessly
  CLADDING: primary rain deflector (doesn't need to be perfect)

  WHY IT WORKS:
  Pressure-equalized cavity: inner air barrier equalizes
  pressure across the cladding. No pressure differential
  to drive water inward. Water cannot travel upward or
  inward against neutral pressure.
```

### Double-Skin Facade

```
  DOUBLE-SKIN FACADE
  ===================

  OUTER SKIN                    INNER SKIN
  (single glass)  GAP           (double glass)
  ─────────────  ─────────────  ─────────────
  Weather skin   Air cavity     Thermal skin
                 0.5m – 2m+     Operable windows
                 ↕ ventilated    possible

  HOW IT WORKS:
  - In summer: cavity ventilated (hot air exhausted at top)
    Solar-heated air exits before reaching inner skin
  - In winter: cavity closed (thermal buffer)
    Air in cavity warmer than exterior (reduces heat loss)
  - Year-round: external blinds in cavity → no wind load
    on blinds, no maintenance access required

  THE CONTROVERSY:
  Pros: External shading in cavity, natural ventilation possible,
        noise attenuation, reduced facade U-value in winter
  Cons: Double the glass cost, cleaning access issues,
        overheating risk if ventilation fails,
        mixed energy performance evidence in practice

  Common in: high-profile European commercial (Commerzbank Frankfurt,
             RWE Tower Essen), some East Asian commercial.
  Less common in US (cost premium hard to justify in analysis).
```

---

## Fire Protection

Fire protection is non-negotiable and shapes plan organization fundamentally.

### Compartmentation

```
  FIRE COMPARTMENTATION STRATEGY
  ================================

  The primary fire protection strategy is containment:
  prevent fire from spreading, not just put it out.

  FIRE-RATED CONSTRUCTION:
  Ratings: 1-hour, 2-hour, 3-hour, 4-hour
  (time before structural failure under standard fire test)

  WHAT REQUIRES FIRE RATING:
  ──────────────────────────
  Exit stairs:          1–2 hour enclosure (IBC Table 1006.3)
  Exit corridors:       1 hour (sprinklered), 1 hour (unsprinklered)
  Occupancy separation: 1–2 hours (varies by use group)
  High-rise floors:     2-hour floor/ceiling assemblies
  Vertical shafts:      1–2 hour (mechanical, plumbing risers)

  UL LISTINGS:
  Fire-rated assemblies are tested by UL (Underwriters Laboratory)
  and listed in UL's Fire Resistance Directory.
  Architects specify by UL Design Number (e.g., "UL Design U305").
  The contractor must build EXACTLY the listed assembly.
  Substituting materials voids the rating.

  OPENINGS IN FIRE-RATED ASSEMBLIES:
  Every opening (door, duct, pipe) breaches the rating.
  Solution: fire-rated doors (UL-labeled), fire dampers in HVAC
  ducts, intumescent pipe sleeves, fire-stopping sealant.
  Each penetration must be detailed and listed separately.
```

### Sprinkler Systems

```
  SPRINKLER SYSTEM TYPES
  =======================

  WET PIPE:                    DRY PIPE:
  ───────────                  ─────────
  Pipes filled with            Pipes filled with
  water at all times.          pressurized air/nitrogen.
  Fastest response.            Water held back by dry
  Most common type.            pipe valve.
  PROBLEM: freezing            Trips on sprinkler head
  in unheated spaces.          activation → water flows.
                               Used: parking garages,
                               loading docks, cold storage.

  PRE-ACTION:                  DELUGE:
  ──────────                   ───────
  Two-signal required:         All heads open, no fusible
  1. Fire detection            link. Single valve control.
  2. Sprinkler head activation Used: aircraft hangars,
  Prevents accidental          transformers, open-hazard.
  discharge.
  Used: DATA CENTERS,
  museums, libraries,
  computer rooms.

  DATA CENTER SPRINKLER:
  Standard: NFPA 75 (IT Equipment Protection)
  Pre-action required (no water unless fire confirmed)
  Concern: accidental discharge = catastrophic equipment loss
  Alternative: clean agent (FM-200, Novec 1230, CO2)
  - Suppresses fire chemically without water
  - Gas floods space, displaces O2 or interrupts chain reaction
  - Extremely expensive, single-use discharge
  - Used for most critical spaces (UPS rooms, server rooms)
```

### Means of Egress

```
  EGRESS DESIGN REQUIREMENTS (IBC)
  ==================================

  TRAVEL DISTANCE TO EXIT:
  ──────────────────────────────────────────────────────────────
  Use Group         Unsprinklered    Sprinklered
  Business (B)      200 ft           300 ft
  Assembly (A)      200 ft           250 ft
  Hospital (I-2)    150 ft           200 ft
  High-hazard (H)    75 ft            75 ft

  COMMON AREA FACTOR (exit access corridor):
  For most assemblies: 0.2" per occupant per floor served
  For high-rise: 0.3" per occupant

  NUMBER OF EXITS (minimum):
  Occupant load > 50: 2 exits required
  Occupant load > 500: 3 exits required
  Occupant load > 1,000: 4 exits required

  EXIT DISCHARGE:
  All exit stairs must discharge to exterior OR
  exit passageway to exterior.
  50% of exits can discharge through first floor (sprinklered).

  HIGH-RISE EGRESS:
  Pressurized exit stairs (prevent smoke entry)
  Areas of refuge (wheelchair-accessible stair landings)
  Occupant notification system (voice + tone)
  Phase I/II elevator recall
```

---

## Building Automation Systems

Modern buildings are distributed real-time control systems — more complex than most IT infrastructure.

```
  BAS / BMS ARCHITECTURE
  =======================

  FIELD DEVICES (sensors + actuators)
  ────────────────────────────────────
  Temperature sensors, CO2 sensors, occupancy sensors
  VAV box actuators, AHU damper actuators
  Chiller/boiler enable signals
  Lighting dimmers, occupancy relays
  Energy meters (BTU, kW)
       │
       ▼ (field bus: BACnet/IP, BACnet MS/TP, Modbus)
  CONTROLLERS (DDC — Direct Digital Control)
  ──────────────────────────────────────────
  Zone controllers (VAV boxes, FCUs)
  AHU controllers
  Chiller plant controllers
  Lighting controllers
  One controller per 4–20 points typically
       │
       ▼ (BACnet/IP, LAN)
  SUPERVISORY (Building Controller / Head End)
  ─────────────────────────────────────────────
  Tridium Niagara (dominant platform — "the JVM of BAS")
  Trend IQ, Johnson Controls Metasys, Siemens Desigo
  Aggregates all DDC data
  Schedules, global setpoints, alarms, trending
       │
       ▼ (IP network / cloud)
  ENTERPRISE / ANALYTICS
  ───────────────────────
  Fault detection and diagnostics (FDD)
  Energy dashboards (Energy Star Portfolio Manager)
  CMMS integration (Maximo, ServiceNow Facilities)
  IoT platforms (Azure IoT Hub, AWS IoT)

  PROTOCOLS:
  BACnet   = the building industry standard (ANSI/ASHRAE 135)
  Modbus   = older, simpler, serial or TCP
  LonWorks = older, now legacy in most new builds
  KNX      = European standard, residential + light commercial
  MQTT     = IoT protocol, cloud-side aggregation
  REST/API = modern integration to enterprise systems
```

The BAS analogy: Tridium Niagara is to building controllers what the .NET CLR is to application code — a runtime abstraction layer that allows different manufacturers' controllers to coexist in one supervisory system.

---

## BIM Coordination

### Clash Detection Workflow

```
  BIM CLASH DETECTION WORKFLOW
  ==============================

  AUTHORING (parallel)
  ─────────────────────
  Architect → Revit model (walls, floors, ceilings)
  Structural → Revit model (beams, columns, slabs)
  Mechanical → Revit MEP (ducts, AHUs, piping)
  Electrical → Revit MEP (conduit, panels, cable trays)
  Plumbing → Revit MEP (pipes, fixtures, drains)
       │
       ▼ (federated model — Navisworks or Revit Worksets)
  CLASH DETECTION
  ────────────────
  Navisworks Manage:
  - Hard clash: elements physically intersect
  - Soft clash: elements within specified clearance
  - Workflow clash: work sequence conflicts
       │
       ▼
  CLASH REPORT
  ─────────────
  Exported as BCF (BIM Collaboration Format)
  Or Excel/HTML report
  Tagged by: discipline A vs discipline B, location, severity
       │
       ▼
  COORDINATION MEETING
  ─────────────────────
  MEP, structural, architectural in same room (or model)
  Assign resolution: who moves? structural or duct?
  Typically: structure wins; duct routes around
  Sometimes: structural beam gets relocated by SE
  Rule: resolve in design, not RFI

  COST OF FIELD vs DESIGN CLASH RESOLUTION:
  Design: costs 1–2 engineer hours per clash
  Field: costs $500–$5,000+ per clash (RFI + rework + delay)
  A 1,000-clash project: $500K savings from BIM coordination
```

---

## Decision Cheat Sheet

| Coordination challenge | Key resolution principle | When to resolve |
|------------------------|-------------------------|-----------------|
| Duct vs beam conflict | Structure wins; route duct around or through truss | Design Development |
| Column spacing vs program | Set grid FIRST, size program to fit bays | Schematic Design |
| Elevator count vs building pop. | Traffic analysis at SD; 1 cab per 40,000 sqft office | Schematic Design |
| Sprinkler type for data center | Pre-action or clean agent; NFPA 75 governs | Design Development |
| MEP mechanical room location | Ground level, roof, or mechanical floors every 10–15 stories | Schematic Design |
| BAS integration standard | BACnet/IP for new; Modbus for legacy equipment | Design Development |
| Facade water resistance | Rainscreen principle; air barrier + drainage cavity | Schematic Design |
| Fire separation between uses | UL-listed assembly; field penetrations detailed | Construction Documents |

---

## Common Confusion Points

**MEP vs BAS**: MEP (Mechanical/Electrical/Plumbing) is the physical systems. BAS (Building Automation System) is the control software and hardware that runs MEP. The BAS is to MEP what an OS is to hardware — it orchestrates but does not replace.

**Curtain wall vs window wall**: Curtain wall hangs from structure and spans floor-to-floor (the facade is independent of the slab edge). Window wall is slab-to-slab — it sits on the slab and the slab edge is visible. Window wall is cheaper; curtain wall is more architecturally flexible and typically higher performance.

**Pre-action vs dry pipe**: Both have air/nitrogen in the pipes. The difference: dry pipe activates on a single sprinkler head fusing; pre-action requires both a fire detection signal AND a sprinkler head to activate. Pre-action has two-stage confirmation — critical for data centers where any false discharge means equipment replacement.

**BIM is not CAD**: BIM (Building Information Modeling) is a database of building objects with properties. CAD is 2D drafting. A Revit model contains wall type, fire rating, material, cost, area — not just geometry. A BIM clash is a spatial database query. The confusion is that both produce drawings — but the drawing is a byproduct of BIM, not its purpose.

**Structural grid is not modular grid**: The structural grid (column spacing) is not the same as the facade module or the ceiling grid. They need to be coordinated but are not automatically aligned. A 30'-0" structural bay with 5'-0" facade modules means 6 modules per bay — clean. A 31'-6" bay with 5'-0" modules means 6.3 modules — fraction at the bay joint. Fractional modules at structural joints are a design and fabrication problem. Set them to coordinate at Schematic Design.
