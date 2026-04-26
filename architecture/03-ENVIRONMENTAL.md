# Environmental Design

## The Big Picture

A building is a climate-control device. Before any mechanical system is switched on, the building's geometry, orientation, mass, and skin determine the baseline thermal and lighting environment. Passive design reduces the load on active systems (HVAC, lighting). The building that needs no air conditioning is better than the one that cools efficiently.

```
+--------------------------------------------------------------------+
|                  ENVIRONMENTAL DESIGN HIERARCHY                    |
|                                                                    |
|  1. PASSIVE STRATEGIES (free — use sun, wind, mass, earth)         |
|     - Orientation (reduce solar gain / maximize winter sun)        |
|     - Shading devices (overhang, fins, trees)                      |
|     - Thermal mass (phase shift, dampen swings)                    |
|     - Natural ventilation (cross-ventilation, stack effect)        |
|     - Earth sheltering, green roofs                                |
|                          |                                         |
|  2. HIGH-PERFORMANCE ENVELOPE                                      |
|     - Insulation (R-value / U-value)                               |
|     - Air barrier (airtightness)                                   |
|     - Glazing (g-value, U-value)                                   |
|     - Thermal bridging elimination                                 |
|                          |                                         |
|  3. DAYLIGHTING                                                    |
|     - Window placement (orientation, size, glare control)          |
|     - Top-lighting (skylights — 3× more efficient)                 |
|     - Light shelves, diffuse glazing                               |
|                          |                                         |
|  4. ACTIVE SYSTEMS (minimize — see hvac/ directory)                |
|     - Sized to the reduced load from steps 1–3                     |
|     - High-efficiency equipment (heat pumps, ERV)                  |
|                          |                                         |
|  5. RATING / VERIFICATION                                          |
|     - LEED, BREEAM, WELL, Passivhaus, Living Building              |
|     - Energy modeling (EnergyPlus, OpenStudio)                     |
+--------------------------------------------------------------------+
```

---

## Passive Design Strategies

### Solar Geometry

The sun's path varies by latitude, season, and time of day. Designing without this data is not architecture — it is random form-making.

```
  SUN ANGLES (Northern Hemisphere)
  ==================================

  SUMMER SOLSTICE (June 21):        WINTER SOLSTICE (Dec 21):
  High sun angle                    Low sun angle
  Solar altitude at noon:           Solar altitude at noon:
    40°N latitude: ~73°               40°N latitude: ~26°
    50°N latitude: ~63°               50°N latitude: ~16°

  IMPLICATIONS:
  ─────────────
  South-facing walls:
  - Get LOW-angle winter sun (desirable — heat gain, daylight)
  - Get HIGH-angle summer sun (easy to shade with horizontal overhang)
  - BEST orientation for temperate climates

  East/West-facing walls:
  - Morning (east) and afternoon (west) sun is LOW-angle
  - Impossible to shade with horizontal overhang
  - Maximum summer heat gain (afternoon west is worst)
  - Minimize east/west glazing in hot climates

  North-facing walls (Northern Hemisphere):
  - Never direct sun (below Arctic Circle)
  - Diffuse sky light only — even, glare-free
  - Best for studio/gallery/office tasks requiring consistent light
  - No solar gain → good in hot climates, needs insulation in cold

  OVERHANG DESIGN:
  ─────────────────
                ├─── d ───┤
  ──────────────┐
  OVERHANG      │
  ──────────────┘         Shadow angle at noon = sun altitude
                |         Summer: shade window fully (high sun)
           WINDOW         Winter: admit sun fully (low sun)
                |
                           Overhang depth d = window height h × (1/tan α_summer)
                           where α_summer = noon solar altitude in summer

  For 40°N latitude:
  d ≈ h × (1/tan 73°) ≈ h × 0.30  (overhang 30% of window height)
```

### Thermal Mass

Mass absorbs heat during the day, releasing it at night. This phase shift damps temperature swings.

```
  THERMAL MASS BEHAVIOR
  ======================

  WITHOUT MASS:                    WITH MASS:

  Temp                             Temp
   |   /\                           |      ___
   |  /  \  interior                |     /   \  interior
   | /    \ follows                 |    /     \ (phase shifted,
   |/      \ outdoor                |   /       \  damped)
   |        \___                    |  /         \___
   +──────────────  time            +──────────────────  time
   6am    noon   6pm               6am    noon    midnight

  Mass materials (thermal capacitance):
  Concrete (150 mm):    lag ≈ 4–6 hours, damping factor 0.4–0.6
  Brick (220 mm):       lag ≈ 6–8 hours, damping factor 0.3–0.5
  Stone (300 mm):       lag ≈ 8–12 hours

  EFFECTIVE CONDITIONS:
  Works best where diurnal temperature swing ≥ 10°C (18°F)
  and nights are cool (Mediterranean, high-altitude climates)
  Less effective in humid tropical climates (warm nights = no discharge)

  DATA CENTER ANALOGY:
  Thermal mass is a thermal capacitor — same as a heat sink.
  Time constant = mass × specific heat / (surface × h-coefficient)
  The architect is designing thermal RC circuits.
```

### Natural Ventilation

```
  NATURAL VENTILATION MECHANISMS
  ================================

  CROSS-VENTILATION:
  ┌─────────────────────────────────────────┐
  │                                         │
  │ INLET   →→→ wind-driven air →→→  OUTLET│
  │ (low    →→→ cross the floor →→→  (high  │
  │  pressure)                    pressure) │
  └─────────────────────────────────────────┘

  Requirements:
  - Openings on opposite (or at least two) walls
  - Building depth ≤ 5× story height for single-sided
  - Building depth ≤ 15m (50ft) for cross-ventilation to work

  STACK EFFECT (thermal buoyancy):
  Hot air rises — use this:

           [EXHAUST OPENINGS AT TOP]
                    ↑ ↑ ↑
               warm air rises
  ┌─────────────────────────────────────┐
  │                         heated      │
  │                         air         │
  │                                     │
  │    cool air enters at base          │
  └─────────────────────────────────────┘
           [INLET OPENINGS AT BASE]

  Stack height determines pressure: ΔP = ρ g H (ΔT/T)
  Greater height difference → more pressure → more flow
  Works year-round in hot climates; works in summer in temperate

  HYBRID (mixed-mode):
  Natural ventilation when conditions allow.
  Mechanical backup when conditions require.
  Best of both — common in high-performance institutional buildings.
  BMS (building management system) manages the mode transitions.
```

---

## Building Envelope Performance

### Key Metrics

```
  ENVELOPE PERFORMANCE VOCABULARY
  ==================================

  U-VALUE (W/m²K or BTU/hr·ft²·°F):
  Thermal transmittance — rate of heat transfer per unit area
  per degree temperature difference.
  LOWER IS BETTER (less heat flows through).
  U = 1/R (reciprocal of R-value)

  R-VALUE (m²K/W or hr·ft²·°F/BTU):
  Thermal resistance — reciprocal of U-value.
  HIGHER IS BETTER (more resistance to heat flow).
  Add R-values in series (layers of insulation sum).

  g-VALUE (SHGC — Solar Heat Gain Coefficient):
  Fraction of incident solar radiation transmitted through glazing.
  Range: 0.2 (very low SHGC, solar-rejecting) to 0.7 (clear glass)
  HOT CLIMATE: low g-value (reject solar gain)
  COLD CLIMATE: higher g-value on south (admit solar gain)

  AIR LEAKAGE (ACH or m³/hr·m²):
  Air changes per hour through infiltration at 50 Pa.
  Standard building: 3–10 ACH50
  Good building: 1–3 ACH50
  Passivhaus: 0.6 ACH50 (test requirement)

  TYPICAL VALUES (2024 good practice, US):
  ──────────────────────────────────────────
  Wall assembly:        R-20 to R-30 (U-0.05 to 0.033)
  Roof/ceiling:         R-30 to R-60 (U-0.033 to 0.017)
  Window (triple glaz): U-0.15 to 0.20, g ≈ 0.30–0.50
  Window (dbl glaz LE): U-0.25 to 0.35, g ≈ 0.25–0.45

  THERMAL BRIDGING:
  Continuous insulation (ci) vs cavity insulation:
  - Steel studs: R-21 cavity but only R-7 effective (70% penalty)
  - Steel conducts heat through the studs, bridging the insulation
  - Passivhaus requires: all insulation continuous, no steel through
```

### Passivhaus Standard

Passivhaus (Passive House) is the most rigorous energy performance standard for buildings. German origin (1991, Feist/Adamson), now global.

```
  PASSIVHAUS PERFORMANCE REQUIREMENTS
  ======================================

  HEATING DEMAND:       ≤ 15 kWh/m²·yr
                        (typical new building: 60–120 kWh/m²·yr)
  COOLING DEMAND:       ≤ 15 kWh/m²·yr (or ≤ 10 W/m² peak)
  TOTAL PRIMARY ENERGY: ≤ 120 kWh/m²·yr (all energy uses)
  AIRTIGHTNESS:         ≤ 0.6 ACH at 50 Pa pressure test
  THERMAL COMFORT:      ≤ 10% of hours with uncomfortable temps

  THE FIVE PILLARS:
  ─────────────────
  1. INSULATION         Superinsulation (R-30+ walls, R-50+ roofs)
                        Continuous — no thermal bridges

  2. WINDOWS            Triple glazing, U ≤ 0.8 W/m²K
                        Insulated frames, low-e coatings

  3. AIRTIGHTNESS       0.6 ACH50 — blower door verified
                        Taped membranes at all penetrations

  4. THERMAL BRIDGE     Zero tolerance: all junctions modeled,
     FREE               detailed, and verified

  5. MECHANICAL         MVHR (mechanical ventilation with heat
     VENTILATION        recovery) — 75–90% heat recovery
     WITH HEAT          Provides fresh air without losing heat
     RECOVERY (MVHR)

  PHPP (Passivhaus Planning Package):
  Excel-based energy balance tool. Extremely detailed.
  Models climate, solar gains, internal gains, infiltration,
  thermal bridges, occupancy. The specification tool for PH.
```

---

## Daylighting

### The Case for Daylighting

Daylight is not just about energy savings (though they are significant — lighting is 20–35% of commercial building energy use). Daylight is correlated with better health outcomes (circadian rhythm support), higher productivity in offices, and faster recovery in hospitals.

```
  DAYLIGHTING STRATEGIES
  =======================

  SIDE-LIGHTING (windows):
  - Most common
  - 1% daylight factor at 2.5× room depth from window
  - Rule of thumb: room depth ≤ 2.5× head height of window
  - Glare control critical (direct sun + white paper = visual impairment)

  TOP-LIGHTING (skylights):
  - 3× MORE EFFICIENT than side windows for same area
  - Even distribution (no glare from low-angle sun)
  - Great for: art galleries, atriums, top-floor offices
  - Heat loss / gain penalty in insulated roofs

  LIGHT SHELF:
  ┌──────────────┬─────────────────────────────────┐
  │   EXTERIOR   │        INTERIOR ROOM            │
  │              │                                 │
  │    ──────────┤  light shelf (horizontal)       │
  │     upper    │       bounces light               │
  │     glazing  │    ↗  to ceiling                │
  │    ──────────┤────────────────────               │
  │     lower    │        deep                       │
  │     glazing  │        penetration                │
  └──────────────┴─────────────────────────────────┘
  Light shelf shades direct sun at lower glazing (glare control)
  while bouncing diffuse light off ceiling (depth penetration).

  DAYLIGHT FACTOR (DF):
  DF = interior illuminance / exterior diffuse sky illuminance × 100%
  2% DF = adequate for reading
  5% DF = good for most tasks
  10%+ DF = overlit, potential overheating
```

---

## Acoustics

### Room Acoustics

```
  ACOUSTIC DESIGN VOCABULARY
  ============================

  REVERBERATION TIME (RT60):
  Time for sound to decay 60 dB after source stops.
  LONGER = more reverberant (cathedrals, concert halls)
  SHORTER = more anechoic (recording studios, open offices)

  RECOMMENDED RT60 BY SPACE TYPE:
  ──────────────────────────────────
  Music performance hall:   1.8–2.2 seconds
  Opera house:              1.4–1.7 seconds
  Chamber music:            1.4–1.7 seconds
  Lecture / speech:         0.6–1.0 seconds
  Open plan office:         0.3–0.5 seconds
  Recording studio:         0.2–0.4 seconds
  HVAC hum reference:       RT60 < 0.3 creates discomfort

  RT60 (Sabine formula): T = 0.161 V / A
  V = room volume (m³)
  A = total absorption (m² Sabin = area × NRC)

  NRC (Noise Reduction Coefficient):
  0 = perfect reflector (glass, concrete)
  0.5 = 50% absorption
  1.0 = perfect absorber (special acoustic foam)

  SOUND TRANSMISSION CLASS (STC):
  Single-number rating for sound isolation between spaces.
  HIGHER = better isolation.

  STC PERFORMANCE:
  ──────────────────────────────────────────────────
  STC 25: normal speech clearly understood through wall
  STC 30: loud speech understood
  STC 40: loud speech heard but not intelligible
  STC 50: loud speech barely audible
  STC 60: excellent isolation (recording studio, court)

  TYPICAL ASSEMBLIES:
  Single drywall stud wall: STC 34
  Double drywall stud wall: STC 45–50
  Concrete masonry 8" CMU: STC 50–52
  Concrete 8" solid:        STC 56–58

  FLANKING PATHS:
  The weakest link determines the STC.
  A STC-60 wall is irrelevant if sound travels through:
  - The ceiling plenum
  - The ductwork
  - Electrical outlets (back-to-back)
  - Structural floor/ceiling assembly

  OPEN OFFICE ACOUSTICS:
  Three variables: absorption (RT60), blocking (partitions),
  and masking (background noise).
  The ABCs of open office acoustics (Ecophon/Aurelius framework).
```

---

## Energy Modeling

### EnergyPlus

EnergyPlus is the US Department of Energy's open-source whole-building energy simulation engine. It underlies most commercial energy modeling software.

```
  ENERGY MODELING TOOL STACK
  ============================

  DATA INPUT                   ENGINE                 OUTPUT
  ─────────                    ──────                 ──────
  IDF / IDD                    EnergyPlus             EnergyUse (kWh/yr)
  (text format)                (DOE, C++)             Load profiles
  or                           │                      HVAC sizing
  OpenStudio                   ├─ Hourly simulation   Fuel bills
  (Revit plugin,               │  (8,760 hrs/yr)      CO2 emissions
  visual interface)            │                      Peak loads
  or                           └─ Weather file input
  DesignBuilder                  (EnergyPlus .epw)
  (commercial GUI)

  USES IN DESIGN:
  - Compare passive design alternatives (orientation, shading)
  - Size HVAC systems (calculate peak and annual loads)
  - Predict LEED energy points (EA Prerequisite 2)
  - Compliance with ASHRAE 90.1 (US energy code)
  - Operational energy certificates (EPC in UK)

  LIMITATIONS:
  - Only as good as the input assumptions
  - Occupant behavior is the wildest variable
  - Construction quality affects actual vs modeled performance
    (the "performance gap" — modeled vs measured is typically 20–50%)
```

---

## Green Building Rating Systems

### Comparison Matrix

```
  RATING SYSTEM COMPARISON
  ==========================

  LEED v4          BREEAM            WELL v2         LIVING BUILDING
  (US-dominant)    (UK-dominant)     (Health focus)  CHALLENGE
  ──────────────   ──────────────    ──────────────  ──────────────────
  Points-based     Points-based      Performance-    Net positive
  Certified /      Pass/Good/Very    based           (regenerative)
  Silver/Gold/     Good/Excellent/   Preconditions
  Platinum         Outstanding       + Optimizations

  8 categories:    9 categories:     10 concepts:    7 petals:
  Sustainable      Management        Air             Place
  Sites            Health &          Water           Water
  Water            Wellbeing         Nourishment     Energy
  Energy           Energy            Light           Health + Happiness
  Materials        Transport         Movement        Materials
  Indoor Env.      Water             Thermal         Equity
  Innovation       Materials         Sound           Beauty
  Regional         Waste             Mind
                   Land Use
                   Pollution

  Widely adopted.  More holistic     Employer        Most ambitious.
  Criticized for   than LEED.        market: WeWork, Actual performance
  "checkbox"       Strong in         etc.            required.
  gaming.          commercial UK.    WELL AP cert.   Very few buildings.

  FOCUS:           FOCUS:            FOCUS:          FOCUS:
  Buildings.       Buildings.        Human health.   Regeneration.
  Mostly design.   Design +          Certifies       Annual measured
  Some measured    management.       buildings AND   data required.
  performance.     More ops weight.  company interiors.
```

### The Embodied Carbon Frontier

```
  OPERATIONAL vs EMBODIED CARBON
  ================================

  OPERATIONAL CARBON:
  Carbon emitted from running the building (heating, cooling,
  lighting, plug loads).
  Targeted by LEED/BREEAM energy credits, Passivhaus.
  CAN be driven to zero with renewables + heat pumps.

  EMBODIED CARBON:
  Carbon emitted from materials manufacturing + construction.
  Upfront carbon = concrete (cement production) + steel
  (blast furnace) + glass + insulation manufacturing.
  CANNOT be offset — it has already been emitted before
  the building opens.

  THE SHIFT:
  2000s thinking: optimize operational energy (LEED Era 1)
  2024 thinking: operational is nearly zeroed out for high-
                 performance buildings. Embodied is now the
                 dominant lifetime contribution.

  AS BUILDINGS GET MORE EFFICIENT OPERATIONALLY,
  EMBODIED CARBON BECOMES THE LARGER FRACTION.

  Typical new commercial building (60-year life):
  Embodied: 40–60% of lifetime carbon (upfront)
  Operational: 40–60% (accumulated over 60 years)

  IMPLICATIONS FOR MATERIAL CHOICE:
  ────────────────────────────────────
  Concrete (cement):  ~800 kg CO2/tonne — high embodied
  Steel (BF):         ~1,800 kg CO2/tonne — very high
  Steel (EAF, scrap): ~400 kg CO2/tonne — better
  Timber (CLT):       negative carbon (sequesters while growing)
                      ~(-500) to +200 kg CO2/m³ (depending on grid)
  Brick:              ~200–250 kg CO2/tonne
  Aluminum:           ~8,000–11,000 kg CO2/tonne — extremely high

  WHY MASS TIMBER EXPLODED:
  CLT sequesters carbon during tree growth.
  Carbon stored in the timber for building lifetime.
  Factory fabrication reduces construction waste.
  The full lifecycle carbon is strongly favorable vs concrete.
```

---

## Decision Cheat Sheet

| Design goal | Primary passive strategy | Key metric |
|-------------|-------------------------|------------|
| Reduce summer cooling load | South orientation + horizontal overhangs; minimize east/west glazing | g-value < 0.25 for E/W; overhang sized to sun angles |
| Reduce winter heating load | Thermal mass on south walls; increase south glazing | R-30+ walls; triple glazing U < 0.20 |
| Maximize daylighting | North light (diffuse), skylights (3× efficiency), light shelves | Daylight factor 2–5% at task surfaces |
| Reduce noise between spaces | STC-rated assembly + eliminate flanking | STC 50+ for private offices; address plenum flanking |
| Certify at LEED Gold | Energy model, optimize envelope, water reduction, materials tracking | 60+ LEED points; EA credit is highest weight |
| Achieve Passivhaus | 5 pillars: superinsulation + triple glaz + airtightness + thermal bridge free + MVHR | 0.6 ACH50 blower door test is the non-negotiable |
| Minimize embodied carbon | Specify mass timber over concrete; recycled steel; low-carbon cement | Whole-life carbon assessment; WBLCA per EN 15978 |
| Data center cooling | PUE optimization starts with passive: economizer first, then cooling | PUE target ≤ 1.2 (hyperscale) vs industry avg 1.58 |

---

## Common Confusion Points

**R-value is not U-value**: They are reciprocals. R = 1/U. Contractors speak in R-values (higher = better). Engineers speak in U-values (lower = better). Converting: U = 1/R-total (sum all layers).

**SHGC vs visible transmittance**: SHGC (= g-value) measures total solar energy transmitted (including absorbed and re-radiated). Visible transmittance (VT) measures only visible light. You can have low SHGC with high VT (spectrally selective glass) — admits daylight but rejects heat. This is the modern target for commercial glazing.

**LEED is a design tool, not a performance guarantee**: LEED certification is based on predicted performance, not measured. The "performance gap" between modeled and actual is 20–50% in many studies. LEED v4 added some measured performance credits but it is still predominantly design-based. NABERS (Australia) and Display Energy Certificates (UK) are measured operational energy — much more honest.

**Thermal mass requires night ventilation to work**: Mass absorbs heat. To release it, it needs to be cooler than the mass — which requires the building to be ventilated (or cooled) at night. Mass without night cooling just stores heat and makes the space hotter the next day. The strategy is diurnal temperature swing management, not permanent heat absorption.

**Data center PUE is architecture's problem too**: Power Usage Effectiveness = total facility power / IT equipment power. PUE = 1.0 is theoretically perfect. PUE = 1.5 means 50% overhead for cooling/power. Hyperscalers target 1.1–1.2. The PUE gap is dominated by cooling — which is architectural (airflow, economizer integration, hot aisle/cold aisle containment, building envelope).
