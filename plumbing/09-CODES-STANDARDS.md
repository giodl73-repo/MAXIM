# Codes & Standards

## IRC, IPC, UPC, Permits, Sizing Tables

## The Big Picture

```
THE MODEL CODE SYSTEM:

  Model codes are developed by code organizations
  → Adopted (with amendments) by states and municipalities
  → Enforced by local Authority Having Jurisdiction (AHJ)

  ┌─────────────────────────────────────────────────────────────┐
  │  MODEL CODE ORGANIZATION → MODEL CODE                      │
  │                                                             │
  │  ICC (International Code Council) →                        │
  │    IBC (International Building Code): commercial           │
  │    IRC (International Residential Code): 1-2 family        │
  │    IPC (International Plumbing Code): plumbing supplement  │
  │    IMC (International Mechanical Code): mechanical         │
  │                                                             │
  │  IAPMO (Int'l Assoc. Plumbing/Mechanical Officials) →      │
  │    UPC (Uniform Plumbing Code): Western US states          │
  │    UMC (Uniform Mechanical Code)                           │
  └─────────────────────────────────────────────────────────────┘

  CRITICAL RULE: The model code book is not "the code"
  in your jurisdiction. The local adopted version, WITH
  local amendments, is the code. Always verify with AHJ.

  GEOGRAPHIC SPLIT (approximate):
    IPC/IRC: Eastern, Southern, and Midwestern US
    UPC: California, Washington, Oregon, Nevada, Arizona, Hawaii
    Some states use their own code: Wisconsin Plumbing Code, etc.
    Canada: National Plumbing Code (separate document entirely)
```

---

## Code Bodies and Adoption

```
  UPDATE CYCLES:
    ICC: 3-year update cycle (2018, 2021, 2024 editions)
    IAPMO: same 3-year cycle
    States/localities: adopt on variable lag
    Common situation (2024): many jurisdictions still on 2018 cycle
    Some: 2015 cycle
    Bottom line: your jurisdiction may be 1-2 editions behind

  STATE-LEVEL ADOPTION:
    States pass building code legislation → reference specific
    edition of model code + state amendments
    California: Title 24 (California Building Standards Code)
      Uses modified UPC; significant California amendments
    New York: uses modified IPC
    Texas: cities choose their own codes; no statewide mandate
    (Texas is an exception — local control more extreme)
    Florida: Florida Building Code (FBC) = modified IBC/IRC + Florida amendments

  IAPMO (UPC) vs ICC (IPC) DIFFERENCES:
    Same fundamental plumbing principles
    Different organization and numbering
    Some technical differences:
      Vent pipe sizing: slightly different table values
      Wet venting rules: different allowable configurations
      Trap-to-vent distance: slightly different requirements
    Cannot mix code references: use one or the other for a project

  AHJ PRIMACY:
    The AHJ (Authority Having Jurisdiction) = local building department
    Their interpretation of the code is final
    Code sections can be ambiguous; inspector's interpretation controls
    Best practice: call the local plumbing inspector BEFORE starting
    work on anything non-routine. "Is X acceptable?" costs nothing;
    rework after failed inspection costs time and money.
```

---

## The Permit Process

```
  WHY PERMITS EXIST:
    Life-safety: trap seals, vent systems, gas pressure testing,
    T&P relief valves — failures kill people
    Insurance: work done without permit may void homeowner's insurance
    Resale: un-permitted work = disclosure issue; can require demolition
    Code documentation: future owners know how it was built

  WHEN PERMITS ARE REQUIRED (varies by jurisdiction):
    Generally required: new construction, new fixtures, water heater
    replacement, gas additions, sewer lateral work, re-piping
    Generally not required (varies): like-for-like fixture replacement
    (same faucet, same toilet), minor repairs, unclogging drains
    Rule of thumb: if you're opening walls, adding new pipes,
    or changing system capacity → permit likely required

  THE PERMIT WORKFLOW:
  ┌──────────────────────────────────────────────────────────────┐
  │  APPLICATION: submit forms, describe scope, pay fee         │
  │  Fee: typically $50-200 residential; based on project value │
  │          ↓                                                   │
  │  PLAN REVIEW (if required):                                 │
  │  Complex systems: plumber submits drawings                  │
  │  Simple residential: over-counter permit (same day)         │
  │          ↓                                                   │
  │  ROUGH-IN INSPECTION:                                       │
  │  Pipes installed but walls NOT covered                       │
  │  Inspector checks: materials, supports, joints, traps,      │
  │  vent arrangement, drain slope                              │
  │          ↓                                                   │
  │  PRESSURE TEST (supply):                                    │
  │  Supply pipes capped and pressurized (water or air)         │
  │  Hold at test pressure (typically 100 PSI × 15 minutes)     │
  │  Inspector or plumber witnesses; no pressure drop = pass    │
  │          ↓                                                   │
  │  FINAL INSPECTION:                                          │
  │  Fixtures installed; trim complete; all covers on           │
  │  Functional test: flush toilet, run water, check hot/cold   │
  │  correct, no leaks                                          │
  │          ↓                                                   │
  │  APPROVED: work accepted; permit closed                     │
  └──────────────────────────────────────────────────────────────┘
```

---

## Supply Pipe Sizing

```
  HUNTER'S METHOD (Fixture Unit Method):
    Developed by Roy Hunter (National Bureau of Standards, 1940)
    Still the basis of code sizing tables

  SUPPLY FIXTURE UNITS (SFU):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Fixture              │ SFU (private) │ SFU (public)           │
  ├─────────────────────────────────────────────────────────────────┤
  │  Lavatory (sink)      │ 1.0           │ 2.0                    │
  │  Toilet (flush tank)  │ 2.5           │ 5.0                    │
  │  Bathtub              │ 1.5           │ 3.0                    │
  │  Shower               │ 1.5           │ 3.0                    │
  │  Kitchen sink         │ 1.5           │ 3.0                    │
  │  Clothes washer       │ 2.5           │ —                      │
  │  Dishwasher           │ 1.5           │ —                      │
  └─────────────────────────────────────────────────────────────────┘

  TOTAL SFU → DEMAND GPM (from probability table):
    Not linear (low probability all fixtures operate simultaneously)
    100 SFU → ~25 GPM (less than 100 × max per fixture)

  PIPE SIZING:
    From available pressure at source (PSI)
    Subtract: meter loss, vertical rise (0.43 PSI/ft), pipe friction
    → Residual pressure at design fixture
    Must maintain ≥15 PSI at any fixture during peak flow

  VELOCITY LIMITS:
    Maximum 8 ft/s in supply pipe:
    Above 8 ft/s: pipe erosion (copper especially)
    Noise (water rushing through pipe — "velocity noise")
    Cavitation at fittings

  DIRECT SIZING ALTERNATIVE:
    For small systems: specify min 3/4" main, 1/2" branches,
    1/2" to shower/tub, 3/8" to lavatory/toilet
    "Rule of thumb" sizing adequate for typical 1-3 bathroom residential
```

---

## DWV Sizing

```
  DRAINAGE FIXTURE UNITS (DFU):
    (Different from supply fixture units — separate calculation)

  ┌─────────────────────────────────────────────────────────────────┐
  │  Fixture           │ DFU (residential)                         │
  ├─────────────────────────────────────────────────────────────────┤
  │  Toilet (tank)     │ 3 (IRC) / 4 (IPC on horizontal branches) │
  │  Lavatory          │ 1                                         │
  │  Bathtub           │ 2                                         │
  │  Shower stall      │ 2                                         │
  │  Kitchen sink      │ 2                                         │
  │  Clothes washer    │ 3                                         │
  │  Dishwasher        │ 2                                         │
  │  Floor drain       │ 2                                         │
  └─────────────────────────────────────────────────────────────────┘

  HORIZONTAL DRAIN PIPE SIZING (IPC Table 704.1):
  ┌──────────────────────────────────────────────────────────────┐
  │  Pipe size │ Max DFU (1/4"/ft slope) │ Max DFU (1/8"/ft)   │
  ├──────────────────────────────────────────────────────────────┤
  │  1-1/2"    │ 3                       │ 1                    │
  │  2"        │ 6                       │3                     │
  │  2-1/2"    │ 12                      │ 6                    │
  │  3"        │ 20 (no toilet)          │ 10                   │
  │  4"        │ 160                     │ 90                   │
  │  6"        │ 620                     │ 400                  │
  └──────────────────────────────────────────────────────────────┘

  VERTICAL STACK SIZING (higher DFU capacity than horizontal):
    3" stack: 48 DFU (>20 DFU horizontal — stack handles better)
    4" stack: 500 DFU
    6" stack: 1,500 DFU

  MINIMUM SIZES:
    Toilet drain: 3" minimum (no toilet allowed on 2" or smaller)
    Shower drain: 2" minimum (1-1/2" allowed by some codes in some configurations)
    Lavatory drain: 1-1/4" minimum (1-1/2" strongly preferred)
    Kitchen sink: 1-1/2" minimum
    Clothes washer standpipe: 2" minimum (3" preferred)

  VENT SIZING (IPC Table 906.1):
    Vent diameter ≥ 1/2 the drain diameter it vents
    Minimum vent: 1-1/4"
    For longer vent runs: increase size per table
```

---

## Water Heater Code Requirements

```
  T&P RELIEF VALVE (mandatory on ALL tank water heaters):
    Temperature-Pressure Relief Valve
    Opens at: >150 PSI OR >210°F (either condition)
    Self-resetting (some) or replace after actuation
    Annual test: lift lever briefly to verify valve opens
    (do NOT test if valve has not been tested in years —
    valve may not re-seat; leaking valve → replacement)

  T&P DISCHARGE PIPE REQUIREMENTS (IRC P2803.6.1):
    Material: same as water supply pipe
    Size: same diameter as relief valve outlet (typically 3/4")
    No reduction in size
    Cannot be trapped (no elbow pointed up)
    Must TERMINATE:
      → No more than 6" above floor
      → OR over floor drain
      → OR to outside (indirect waste)
    Must be visible (NOT piped into wall or concealed)
    Reason: T&P event = scalding steam/water; must discharge
    safely to visible/accessible location, not into wall

  EXPANSION TANK (required in closed systems):
    IRC P2903.4: where backflow preventer or check valve
    creates closed system → expansion tank required
    Pre-charge pressure must equal supply pressure
    Sized per IRC Table P2903.4 (tank size × supply pressure)

  SEISMIC STRAPPING (California and seismic zones):
    California Health and Safety Code 19211:
    All water heaters must be strapped to prevent toppling
    Double-strap: upper strap in upper 1/3 of tank, lower
    strap in lower 1/3
    Minimum 4 anchor bolts per strap into studs or blocking
    Required in Seismic Zones 3 and 4 (much of Western US)

  FIRST-HOUR RATING SIZING:
    IRC guidance: size water heater based on first-hour rating
    (FHR) matching peak morning demand
    FHR must meet demand of occupant morning hot water use
    FHR printed on EnergyGuide label
    Not tank size (gallons) — FHR (gallons deliverable in first hour)
```

---

## Backflow Prevention

```
  THE CROSS-CONNECTION HAZARD:
    Potable water system connected to non-potable source
    → Backpressure or back-siphonage → contaminated water
    enters potable supply

  EXAMPLES:
    Irrigation system with fertilizer injector connected
    to potable supply → backflow → fertilizer in house water
    Garden hose submerged in pool or chemical bucket
    Commercial kitchen: dishwasher connection to drain
    Hospital: medical equipment to water supply

  BACKFLOW PREVENTER TYPES:
  ┌──────────────────────────────────────────────────────────────┐
  │  DEVICE             │ HAZARD LEVEL │ USE                    │
  ├──────────────────────────────────────────────────────────────┤
  │  Air Gap: physical  │ High-hazard  │ Most reliable; limited │
  │  break in flow      │              │ where feasible         │
  │  (no physical       │              │                        │
  │  connection at all) │              │                        │
  ├──────────────────────────────────────────────────────────────┤
  │  RPZ (Reduced       │ High-hazard  │ Irrigation with chem.  │
  │  Pressure Zone)     │              │ Commercial kitchen     │
  │                     │              │ Solar thermal          │
  │  Redundant checks   │              │ Annual test required   │
  │  + intermediate     │              │                        │
  │  pressure relief    │              │                        │
  ├──────────────────────────────────────────────────────────────┤
  │  PVB (Pressure      │ Low-to-medium│ Irrigation (no chem.  │
  │  Vacuum Breaker)    │              │ injection)             │
  │  One-way + air      │              │ Hose bibs              │
  │  intake chamber     │              │                        │
  ├──────────────────────────────────────────────────────────────┤
  │  DCVA (Double       │ Low-hazard   │ Supplemental (not      │
  │  Check Valve)       │              │ for high-hazard)       │
  └──────────────────────────────────────────────────────────────┘

  TESTABLE DEVICES:
    RPZ, DCVA: annual testing required (most jurisdictions)
    Must be tested by state-licensed tester
    Test results filed with water utility
    Brands: Watts, Febco, Ames, Wilkins

  HOSE BIB VACUUM BREAKER:
    Simple screw-on device at every hose bib
    Very low cost (<$10); required by many codes
    Prevents back-siphonage from garden hose submersion
    Must NOT be removed (common mistake)
    Drips after shutoff: mechanism working properly; not a leak
```

---

## Common Code Violations

```
  VIOLATIONS FOUND AT ROUGH-IN INSPECTION:

  TRAP VIOLATIONS:
    S-trap installed (S-traps banned; install P-trap)
    Trap arm too long (exceeds max distance to vent)
    Trap below slab with no accessible cleanout
    Missing trap entirely (direct connection to drain)

  VENT VIOLATIONS:
    No vent at all (AAV installed where not approved)
    Vent terminates below roof (must terminate above)
    Vent too close to window or air intake
    Vent diameter undersized for drain served

  PIPE SUPPORT VIOLATIONS:
    Copper: hangers >6 ft apart horizontal (max 6 ft horizontal,
    10 ft vertical)
    PVC: hangers >4 ft apart (max 4 ft horizontal)
    PEX: hangers >32" apart horizontal
    Pipe vibrating against structure (must be isolated at penetrations)

  DRAIN SLOPE VIOLATIONS:
    Negative slope (low point away from stack) — water pools
    Too steep on large drain pipe (liquid/solid separation)
    No slope documented (inspector may call for water test)

  MATERIAL VIOLATIONS:
    PVC cement used on CPVC (wrong solvent; incompatible)
    CPVC cemented with PVC primer only (no cement)
    Galvanized for gas lines (zinc flakes = hazard)
    Non-listed pipe or fittings (must be listed/certified product)

  SUPPLY SYSTEM VIOLATIONS:
    Missing T&P discharge pipe (code requires visible termination)
    T&P discharge pipe reduced below valve outlet size
    Expansion tank missing on closed system (common after PRV or
    backflow preventer installation)
    Missing shutoff valve at appliance connections
    Cross-connection (hot and cold mixed before fixtures)
    Cold to hot side or hot to cold (swapped connections)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Which code applies in California? | California Plumbing Code (modified UPC + CA amendments) |
| Which code applies in New York? | Modified IPC (2022 NYS Uniform Fire Prevention and Building Code) |
| Do I need a permit to replace a toilet? | Check local AHJ — usually no for like-for-like; yes if relocating |
| What pressure test is required at rough-in? | 100 PSI × 15 min water or air pressure hold on supply |
| T&P discharge pipe: where does it terminate? | ≤6" above floor or over drain; visible; never in wall |
| Toilet drain minimum size | 3" (no toilet allowed on 2" or smaller) |
| Expansion tank: when required? | Any time backflow preventer or check valve creates closed system |
| Irrigation system: what backflow preventer? | RPZ (with chemical injection) or PVB (water only); annual test |

---

## Common Confusion Points

**The model code book is not your local code**: The 2021 IPC is a starting point. Your municipality may have adopted the 2018 IPC with 50 local amendments. The inspector enforces the local version. When in doubt — call the local building department, not a code consultant quoting the model code.

**"Approved" does not mean "listed"**: Listed means a product has been tested and certified by a listed testing lab (UL, NSF, CSA) and is on a published list. Approved means the AHJ accepts it. Listed products are generally automatically approved; unlisted products require special AHJ approval. For plumbing, insist on listed products — inspectors will reject unlisted materials.

**S-traps are existing condition, not automatic violation**: Most jurisdictions do not require removal of existing non-code-compliant plumbing in a house until the room is being renovated. An S-trap in place is typically grandfathered. But if you're touching the drain in a renovation — fix it. "Grandfathering" ends when you open the walls.

**Permits are not just bureaucracy**: Un-permitted water heater installations have killed people (improper T&P relief valve installation, missing discharge pipe). Unpermitted gas work has caused explosions. The inspection system catches life-safety errors that plumbers and homeowners regularly make. The permit fee is cheap insurance.

**The AHJ has broad discretion**: Even if you can quote a code section, the inspector's on-site interpretation controls. Some inspectors are highly knowledgeable; some are less so. When an inspector requires something not clearly mandated by code, you can appeal (through formal channels) but practically often better to comply and document. Building the relationship with local inspectors is a professional asset.
