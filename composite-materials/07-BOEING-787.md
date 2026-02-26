# Case Study: Boeing 787 Dreamliner

## The Big Picture

```
+------------------------------------------------------------------+
|              787 COMPOSITE CONTENT BREAKDOWN                     |
|                                                                  |
|   MATERIAL       BY WEIGHT    BY VOLUME   KEY LOCATIONS         |
|   ────────       ─────────    ─────────   ────────────          |
|   Composites     50%          ~80%        Fuselage, wings       |
|   Aluminum       20%                      Wing boxes, nacelles  |
|   Titanium       15%                      Fasteners, fittings   |
|   Steel          10%                      Landing gear          |
|   Other           5%                      Various               |
|                                                                  |
|   Previous Boeing aircraft: 787 was step-change                  |
|   777 (1994): ~10% composites by weight                          |
|   787 (2011): 50% composites by weight                          |
|   Enabled by: 30 years of aerospace composite maturation         |
+------------------------------------------------------------------+
```

The 787 represents the most ambitious structural composites program in commercial
aviation history — and the one with the most publicly documented lessons learned.
It went over budget, over schedule, and encountered post-service issues (battery
fires, delamination) that illustrate the full lifecycle complexity of composites.

---

## Why Go Composite: The Business Case

### The 777 Baseline

Boeing 777 (1994): conventional aluminum fuselage, 10% composites.
Operating economics: driven by fuel burn, which scales with structural weight.

```
   787 DESIGN TARGETS (vs. 767 baseline):
   ────────────────────────────────────────
   Fuel burn: -20% per seat (primary driver)
   Weight:    -20% structural weight (CFRP replacing aluminum)
   Operating cost: -30% direct maintenance cost
   Passenger comfort: larger windows, higher cabin pressure possible
                       (composites don't fatigue-crack from pressurization)

   ALUMINUM FATIGUE CONSTRAINT:
   ──────────────────────────────
   Conventional fuselage: pressurize / depressurize every flight cycle
   Aluminum: fatigue life → maintenance inspection intervals
   CFRP: no stress-corrosion cracking, no fatigue cracks from pressure
   → 787 cabin pressure: 6,000 ft equivalent (vs. 8,000 ft in 777)
   → Higher O2 partial pressure → less passenger fatigue on long flights
   → Higher humidity: 15% relative humidity (vs. 4–8% in aluminum fuselage)
   Larger windows: no stress-concentration fatigue life limit from oval hole
```

### Weight Savings Numbers

```
   787 STRUCTURAL WEIGHT SAVINGS vs. EQUIVALENT ALUMINUM:
   ──────────────────────────────────────────────────────
   Fuselage barrels (CFRP vs. Al):        ~20% weight reduction
   Wing (CFRP skins, spars, ribs):       ~15–18% weight reduction
   System components (various):           ~5–10%

   TOTAL: ~50,000 kg lighter than equivalent aluminum structure
   At average jet fuel price ($0.60/L, 2010–2015):
   50,000 kg weight → ~3% fuel burn reduction → ~$1.5M/yr/aircraft savings
   Fleet of 1,000 787s: ~$1.5 billion/year in fuel savings

   Payback on CFRP premium:
   CFRP cost premium vs. Al: ~$50M per aircraft (rough)
   Annual fuel savings: ~$1.5M/aircraft
   Payback: ~33 years → marginal without productivity/range benefits
   With range/capacity improvements: 787 routes (London-Perth direct) = revenue driver
```

---

## Fuselage Design: The Barrel Approach

### Conventional Aluminum Fuselage Construction

```
   CONVENTIONAL:
   ──────────────
   Aluminum skins: 2–6 mm panels, lap-jointed and riveted
   Frames and stringers: riveted to skin
   ~40,000–50,000 fasteners per fuselage section
   Seams: structural + aerodynamic challenge
   Water ingress at seam locations: corrosion risk

   787 ONE-PIECE BARREL:
   ──────────────────────
   Each fuselage section: one continuous CFRP barrel
   Formed on rotating mandrel using AFP (Automated Fiber Placement)
   ~65,000 m of prepreg tow per barrel section
   No longitudinal seams → smooth exterior
   Reduced fastener count: ~50% reduction in fuselage
   No corrosion (CFRP vs. aluminum)
```

### AFP Fuselage Manufacturing

```
   FUSELAGE BARREL PROCESS (at Boeing Everett / Spirit AeroSystems):
   ────────────────────────────────────────────────────────────────────
   1. Mandrel: aluminum or composite cylinder (aft fuselage ~6 m diameter)
   2. AFP head: 8–32 tow heads apply prepreg tow (6 mm wide strips)
      at programmed angle (primarily ~±45° + 0°)
   3. Mandrel rotates, AFP gantry traverses
   4. Full-thickness layup: ~50–70 plies in barrel, ~6–7 mm skin
   5. Vacuum bag applied over entire barrel
   6. Autoclave cure: 180°C, 6 bar, ~8 hours for full barrel
   7. Demold: pull mandrel from cured barrel
   8. Inspection: full ultrasonic C-scan (UT)

   BARREL DIMENSIONS:
   ───────────────────
   Section 41 (nose): ~6 m diameter, ~7 m long
   Section 47/48 (main cabin): 6 m × 8 m
   Sections produced: Everett (Boeing) + Spirit AeroSystems (Wichita) +
                       Alenia Aermacchi (Italy) + Kawasaki (Japan)
   Sections shipped: Spirit/Alenia → join at Everett
```

---

## Wing and Empennage Design

### Wing Design

```
   787 WING STRUCTURE:
   ────────────────────
   Wing skins: CFRP upper and lower skins, integrally stiffened (stringers molded in)
   Front spar: CFRP spar caps + web (CF/epoxy)
   Rear spar: CFRP
   Wing ribs: CFRP (most) + aluminum (some)
   Wing tips: CFRP raked wingtip (no winglet)
   Ailerons, spoilers: CFRP

   WING BOX:
   ─────────
   Entire wing box: CFRP with titanium fasteners
   No aluminum in primary wing structure
   Design allowed sweep angle: 32° (aggressive sweep for high subsonic speed)
   Composite wing flex: elastically tailored for aeroelastic stability

   WING SKIN MANUFACTURING:
   ─────────────────────────
   ATL (Automated Tape Laying): flat skin panels up to 12 m × 3 m
   AFP: complex contours near root and tip
   Cure: large autoclave at Boeing South Carolina (787 wing)
   Largest autoclaves: ~12 m diameter × 27 m long ($30–50M each)
```

### Empennage (Tail)

CFRP horizontal and vertical stabilizers. Manufactured by Alenia (Italy) and
other suppliers. Conventional laminate construction, autoclave cure.

---

## Critical Problems and Lessons

### Supply Chain and Integration Failures (2007–2011)

The 787 program was the first major attempt at a "distributed composites
manufacturing" model — suppliers worldwide build major substructures that bolt
together at final assembly.

```
   SUPPLY CHAIN ARCHITECTURE (intended):
   ────────────────────────────────────────
   Tier 1 suppliers: Fuselage sections, wing, empennage
   → Ship pre-assembled sections to Everett
   → "Join and Fly" in 3 days

   REALITY:
   ─────────
   Fastener shortages: suppliers had no inventory buffer
   Shimming (gap-filling): CFRP parts less dimensionally predictable
     than aluminum → more shimming required than anticipated
   Supplier quality: some supplier laminates failed inspection on delivery
   Out-of-sequence work: assembly work moved to Everett instead of suppliers
   Weight: first aircraft 14,000 lb (6,350 kg) overweight → weight reduction program
   First flight: December 2009 (2.5 years late)

   ROOT CAUSE:
   ────────────
   Distributed CFRP manufacturing at global scale was untested
   Aluminum design/build experience did not directly transfer
   Supplier composite expertise: variable globally in 2006–2008
   Integration tolerance stack-up: harder to predict than aluminum machining
```

### Battery Fires (2013)

Lithium-ion battery system caused fires on two 787s in January 2013 → worldwide
fleet grounding (50 aircraft, 99 days).

```
   DIRECT RELEVANCE TO COMPOSITES:
   ──────────────────────────────────
   Battery enclosure: contained in composite bay
   Thermal runaway: 787 APU battery system
   Composite fire response: CFRP does not burn like aluminum but does degrade
                             above ~200°C
   Recovery: battery system redesigned → metal enclosure venting to exterior
   Impact: raised awareness of CFRP response to thermal events in service

   BROADER IMPLICATION:
   ─────────────────────
   Composite structures: different response to fire than metal
   Emergency: burning CFRP → HCN (acrylonitrile origin) + other toxics
   FAA/EASA: specific flammability requirements for composite interiors and structure
```

### Lightning Strike Protection

CFRP is electrically conductive but not as conductive as aluminum.

```
   LIGHTNING STRIKE ON CFRP FUSELAGE:
   ─────────────────────────────────────
   Aluminum fuselage: disperses lightning energy across skin
   CFRP: ~100× lower conductivity than aluminum
   Risk: current concentration → locally high temperature → fiber/matrix damage
           arc between fasteners → fuel tank spark ignition risk

   787 SOLUTION:
   ──────────────
   Embedded copper mesh (wire mesh foil) in outer CFRP plies
   Connects to metallic frame members → controlled current path
   Copper mesh: 0.4–1.0 oz/ft² expanded copper foil
   Adds ~1.5 kg/m² to skin weight
   All 787 CFRP structures have embedded lightning strike protection (LSP)

   TESTING REQUIREMENTS:
   ──────────────────────
   Lightning strike zone 1A testing: direct strike 200,000 A
   Validate: no penetration, no sparking into fuel bays
   Zone 2: swept stroke zones
```

---

## In-Service Performance Data

### Maintenance Experience (2011–2023)

```
   INSPECTIONS:
   ─────────────
   Scheduled inspection: based on flight cycles and calendar time
   CFRP does not suffer fatigue cracking like aluminum → fewer cycle-based inspections
   Corrosion: effectively eliminated in CFRP fuselage (vs. Al)
   Impact damage: hail, ground handling incidents more impactful than for aluminum
   Cost of repair: CFRP repair more expensive than aluminum patch
   Repair certification: complex — must be Boeing-documented repair scheme

   DELAMINATION DISCOVERY:
   ────────────────────────
   2019: FAA issued airworthiness directive for inspections of certain
   fuselage section joints (shimming compound between CFRP barrel joints)
   CFRP layup shimming inadequate → interlaminar voids at some joints
   Required: ultrasonic inspection and repair on affected aircraft
   → Illustrates: CFRP assembly defects can be latent and hard to detect

   LIFE-CYCLE COSTS:
   ──────────────────
   Reported: ~30% lower airframe maintenance cost vs. aluminum equivalent
   Primary savings: no corrosion treatment, fewer fatigue inspections
   Offset: CFRP repair expertise requirement, higher repair cost per incident
```

---

## Comparison: 787 vs. A350

Both aircraft committed to ~50% composites; different design choices:

```
   787 vs. A350 (representative comparison):
   ─────────────────────────────────────────────
                    787-8          A350-900
   MTOW (t)         228            280
   CFRP% by weight  50%            53%
   Fuselage         CFRP barrels   CFRP panels + frame
   Wing             Full CFRP      Full CFRP
   First flight     2009           2013
   EIS              2011           2015
   Autoclave size   5.5m × 27m     8.5m × 30m (Airbus)

   DESIGN PHILOSOPHY DIFFERENCE:
   ──────────────────────────────
   787: integrated barrel sections (fewer pieces, complex manufacturing)
   A350: panelized fuselage (more pieces, more joints, more conventional)
   Both: approximately equal structural efficiency
   A350 benefited from 787 lessons → less schedule overrun
```

---

## Decision Cheat Sheet

| 787 Design Question | Answer |
|---------------------|--------|
| Why CFRP fuselage? | Weight (-20%), fatigue elimination, pressure/humidity benefits |
| How are fuselage barrels made? | AFP layup on mandrel, autoclave cure, ultrasonic inspection |
| Why so many delays? | Supply chain and integration issues, not CFRP technology per se |
| Why copper mesh in skin? | CFRP not conductive enough for lightning strike protection |
| What failed in service? | Battery system (Li-ion), shimming compound delamination at joints |
| How does CFRP change maintenance? | Less corrosion/fatigue inspection, but CFRP repair is expensive |
| How does it compare to A350? | Similar composite fraction; A350 learned from 787 delays |

---

## Common Confusion Points

**The 787's weight problems were supply chain, not composites**: The 14,000 lb
overweight first aircraft came primarily from out-of-tolerance manufacturing
(more shimming), extra fasteners, and system installation issues — not inherently
worse CFRP structural efficiency. The design was sound; execution at global scale
for first time was not.

**50% composites by weight ≠ 50% of the aircraft is a composite panel**: Many
"composite" components are CF/epoxy structure bolted to titanium joints and
aluminum sections. The 50% figure includes all composite forms (primary structure,
secondary, interiors, nacelles). The load-carrying primary structure is essentially
100% CFRP.

**CFRP does not eliminate all inspection**: The claim that CFRP requires no
maintenance is wrong. It eliminates corrosion-driven and many fatigue-driven
inspections. But impact damage (hail, tool drops, ground vehicle contact) requires
damage detection and repair protocols. The 787 program has generated an extensive
repair manual for CFRP-specific damage scenarios.
