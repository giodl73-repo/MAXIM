# Land Use and Zoning

## The Big Picture

Zoning is the primary legal mechanism through which cities control what gets built where. It is the API contract of the built environment — defining permitted uses, dimensional limits, and procedural requirements for every parcel of land.

```
+------------------------------------------------------------------+
|                    LAND USE CONTROL SYSTEM                       |
|                                                                  |
|  CONSTITUTIONAL     STATUTORY           REGULATORY               |
|  BASIS              FRAMEWORK           INSTRUMENTS              |
|                                                                  |
|  Police power  -->  State enabling  --> Zoning code              |
|  (states, delegated  legislation        Zoning map               |
|  to localities)      (Standard State    General plan             |
|                      Zoning Enabling    Subdivision regs         |
|  Euclid v. Ambler    Act 1926)          Building code            |
|  Realty 1926:                           Environmental review     |
|  upheld zoning       Delegation to      (CEQA/NEPA)              |
|  as constitutional   local governments                           |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|                    ZONING MECHANICS                              |
|                                                                  |
|  WHAT IS REGULATED:                                              |
|  Use (residential/commercial/industrial/agricultural/            |
|       mixed-use/open space)                                      |
|  Bulk (height, setbacks, lot coverage, FAR)                      |
|  Parking (minimums -- and increasingly maximums)                 |
|  Landscaping / open space requirements                           |
|  Signage / lighting                                              |
|                                                                  |
|  HOW IT IS ENFORCED:                                             |
|  By-right approval (meets code --> permit issued, no discretion) |
|  Conditional use permit (meets base criteria + conditions)       |
|  Variance (hardship exception from dimensional standards)        |
|  Rezoning (legislative act, amends the map)                      |
|  Planned Unit Development (PUD -- negotiated project-level code) |
+------------------------------------------------------------------+
```

---

## Constitutional Basis: Euclid v. Ambler Realty (1926)

The Supreme Court case that made American zoning constitutional. Euclid, Ohio (a Cleveland suburb) had enacted a zoning ordinance. Ambler Realty challenged it as an unconstitutional taking of property value without compensation.

```
EUCLID v. AMBLER (1926):

  FACT PATTERN:
  Ambler Realty owned 68 acres in Euclid.
  Zoning reduced the industrial-use land
  to residential-only, cutting value by ~75%.

  HOLDING:
  Zoning is a valid exercise of the police power
  (government authority to regulate for health,
  safety, morals, and general welfare).
  Nuisance analogy: separating incompatible uses
  is like preventing a nuisance before it occurs.

  JUSTICE SUTHERLAND:
  "A nuisance may be merely a right thing
   in the wrong place, like a pig in a parlor
   instead of the barnyard."

  WHAT IT ESTABLISHED:
  - Use separation is constitutional
  - Localities have broad authority to zone
  - Property value reduction alone is not a taking
    (Lucas v. South Carolina Coastal Council 1992:
     total wipeout IS a taking requiring compensation)

  WHAT IT DID NOT ESTABLISH:
  - No requirement that zoning be rational
  - No requirement that zoning be consistent
    with a comprehensive plan (in most states)
  - No federal constitutional right to build
    (only a right not to have property taken without
    just compensation)
```

The takings doctrine boundary matters for planners:

```
TAKINGS SPECTRUM:

  REGULATION                              TAKING
  (no compensation)                   (requires compensation)

  |-----------------------------------------------|
  Health/safety        Penn Central     Lucas
  regulation           balancing test   total wipeout
  (nuisance           (3 factors:        (100% loss =
  prevention)          economic          per se taking)
                       impact,
                       interference
                       with investment
                       expectations,
                       character of
                       government action)

  Most zoning falls here. Courts rarely
  find ordinary zoning regulations to be
  compensable takings.
```

---

## Euclidean Zoning: The Standard Model

The "Euclidean" model (named after the Euclid case, not the geometry) separates uses into hierarchical districts. This was the dominant 20th-century American zoning model.

```
EUCLIDEAN USE HIERARCHY:

  R1 (Single-family residential)    <-- Most restrictive
    |
  R2 (Duplex residential)
    |
  R3 (Multi-family residential)
    |
  C1 (Neighborhood commercial)
    |
  C2 (General commercial)
    |
  C3 (Regional commercial)
    |
  M1 (Light industrial)
    |
  M2 (Heavy industrial)             <-- Least restrictive

  CUMULATIVE ZONING (older model):
  Higher use classes can locate in lower-restriction zones.
  A house can be built in an industrial zone.

  EXCLUSIVE ZONING (modern model):
  Each zone is exclusive -- only the listed uses permitted.
  Industrial uses cannot locate in residential zones AND
  residential cannot locate in industrial zones.
```

### Bulk Regulations: The Dimensional Controls

Use zoning tells you what can go on a lot. Bulk regulations tell you how big it can be.

```
BULK REGULATION SYSTEM:

  +------------------------------------------------------------+
  |                        LOT                                 |
  |     [FRONT SETBACK]                                        |
  |   +---------------------------+                            |
  |   |                           |                            |
  | [S|         BUILDING          |S]  <-- height limit        |
  | I |         ENVELOPE          |I      (storeys or feet)    |
  | D |                           |D                           |
  | E |                           |E                           |
  |   +---------------------------+                            |
      |     [REAR SETBACK]                                     |
  +------------------------------------------------------------+

  KEY CONTROLS:
  - Front setback: distance from street ROW to building face
  - Side/rear setbacks: distances from lot lines to building
  - Height limit: maximum building height (ft or storeys)
  - Lot coverage: % of lot that building footprint can occupy
  - FAR (Floor Area Ratio): total floor area / lot area

  FAR EXAMPLE:
  Lot = 10,000 sq ft. FAR = 2.0.
  Maximum building = 20,000 sq ft.
  Could be: 2 storeys at full lot coverage
         or 4 storeys at 50% lot coverage
         or 10 storeys at 20% lot coverage
  FAR is the fundamental density control lever.
```

Bulk regulations are **constraint satisfaction expressed geometrically**: permitted uses define the feasible set, FAR is a capacity constraint (sum(floor_area) / lot_area <= FAR_max), setbacks are spatial exclusion constraints, and height limits are upper bounds. A building permit is a feasibility check — does this proposed configuration satisfy all constraints simultaneously?

### FAR as a Density Dial

```
FAR COMPARISON ACROSS CITY TYPES:

  FAR 0.3    US suburban office park
             (one-storey building, parking lot dominates)

  FAR 0.5    Standard US suburban residential
             (house on lot with yard)

  FAR 1.0    Typical urban commercial
             (two-storey building, 50% lot coverage)

  FAR 2.0    Urban mid-rise
             (4-storey building, half lot coverage)
             Tokyo shitamachi (low-rise residential)

  FAR 5.0    Dense urban mixed-use
             (10-storey, half lot, or 5-storey full coverage)

  FAR 10.0   High-rise downtown
             (20-storey, half lot)

  FAR 15.0   Manhattan Midtown (permitted)
  FAR 21.4   Empire State Building (as built, with bonuses)

  The gap between FAR 0.5 (US suburbia) and FAR 2.0
  (walkable urbanism threshold) is the housing affordability
  crisis made visible in a single number.
```

---

## The Setback-Parking Problem

Front setbacks and parking minimums interact to produce a specific urban form that is hostile to pedestrian life.

```
WITHOUT SETBACK/PARKING MINIMUM:
  STREET
  |
  |  BUILDING FACE  (directly at sidewalk)
  |  Ground floor retail
  |  Parking behind or in structure
  |
  WALKABLE, ACTIVE STREET EDGE

WITH SETBACK + PARKING MINIMUM:
  STREET
  |
  |  [PARKING LOT - 5 spaces per 1000 sq ft]
  |
  |  [SETBACK - 20 ft from street]
  |
  |  BUILDING FACE  (set back behind parking)
  |
  STRIP MALL CONFIGURATION
  Dead pedestrian environment
  Building serves cars, not people

SETBACK MINIMUM + PARKING MINIMUM =
  Mandatory strip mall pattern
  No matter what the architect intends
```

### The Shoup Critique: Parking Minimums as Policy Failure

Donald Shoup's "The High Cost of Free Parking" (2005, updated 2011) is the most influential critique of parking policy in American planning.

```
SHOUP'S ARGUMENT:

  1. ARBITRARY ORIGINS:
     Parking minimums were set by copying
     other cities' standards, which copied
     each other. Original numbers based on
     peak demand at suburban sites -- applied
     everywhere regardless of context.

  2. HIDDEN SUBSIDY TO DRIVING:
     "Free" parking is paid for by everyone
     (higher rents, higher prices, taxes).
     Non-drivers cross-subsidize drivers.

  3. INDUCED DEMAND:
     More parking supply --> more driving
     (Braess's paradox analog: adding capacity
     increases total traffic by changing behavior)

  4. LAND COST:
     One surface parking space = 300 sq ft at
     $50-200/sq ft land cost = $15,000-$60,000
     of land not producing housing or commerce.

     Structured parking: $25,000-$50,000/space
     Underground parking: $50,000-$100,000/space

  5. THE MINIMUM PROBLEM:
     Minimums are calibrated for peak demand
     (Black Friday, not Tuesday 2pm).
     Parking sits empty ~80% of the time.

  SHOUP'S THREE REFORMS:
  1. Eliminate parking minimums
  2. Price on-street parking to achieve
     15% vacancy rate (always one spot
     available on every block)
  3. Return parking revenue to the district
     (business district improvement)

GLOBAL REFORM MOVEMENT:
  Buffalo NY: first US city to eliminate
  all parking minimums citywide (2017)
  San Francisco, Seattle, Portland: eliminated
  minimums near transit
  Minneapolis, Hartford, Austin, Houston:
  eliminated citywide minimums
  New Zealand: national law eliminated
  all minimums (2022)
```

---

## NIMBY Dynamics and the Homevoter Hypothesis

Zoning is not politically neutral. It is a mechanism through which existing property owners capture the regulatory process to limit competition and preserve property values.

```
WHO WINS AND WHO LOSES FROM RESTRICTIVE ZONING:

  WINNERS (existing homeowners):
  - Higher home values (restricted supply)
  - Neighborhood character preserved
  - Traffic and parking impacts limited
  - School quality preserved (limited enrollment)
  - "Homevoter" incentive: home = largest asset

  LOSERS (everyone else):
  - Future residents who cannot afford housing
  - Current renters who pay more for less
  - Workers who must commute from far away
  - Regional economy (misallocated workers)
  - Climate (sprawl --> driving)

FISCHEL'S "HOMEVOTER HYPOTHESIS" (2001):
  Homeowners vote their home values.
  Unlike shareholders who diversify portfolios,
  homeowners have all their wealth in one
  illiquid, location-specific asset.
  Result: extreme political motivation to
  block anything that might reduce values.
  Zoning is the instrument.

  THIS IS RATIONAL INDIVIDUAL BEHAVIOR
  THAT PRODUCES IRRATIONAL AGGREGATE OUTCOMES
  (the classic collective action problem)
```

### Upzoning: The Debate

The pro-housing movement (YIMBY — Yes In My Backyard) argues that restrictive zoning is the primary driver of housing unaffordability and that upzoning is the solution.

```
UPZONING CASE STUDIES:

  MINNEAPOLIS 2040 PLAN:
  - Eliminated single-family-only zoning
    citywide (first major US city)
  - Permitted triplexes on all residential lots
  - Early results: construction increase,
    but primarily in already-dense areas
  - Rent growth in Minneapolis lower than
    peer cities during 2019-2023

  CALIFORNIA ADU REFORM (2016-2020):
  - State laws preempted local ADU restrictions
  - Streamlined permit process
  - Dramatic supply increase: 20,000 ADUs/yr
    statewide by 2022 (vs. ~1,200/yr pre-reform)
  - ADUs represent 20%+ of new CA housing units
  - Lesson: removing barriers works when
    underlying demand exists

  AUCKLAND, NEW ZEALAND (2016):
  - Rezoned 75% of city to allow apartments
  - Glaeser/Gyourko "zoning tax" study:
    projected 40% rent reduction potential
  - Reality (7 years): construction surge,
    rents ~30% lower than comparable NZ cities
  - One of the strongest upzoning results globally

  OREGON HB 2001 (2019):
  - Statewide preemption: all cities > 10,000
    must allow duplexes on all residential lots;
    cities > 25,000 must allow middle housing
    (triplexes, fourplexes, townhouses, cottage clusters)
  - First statewide legislation of this type in US
```

---

## Form-Based Codes

The alternative to use-based zoning: regulate physical form rather than use.

```
EUCLIDEAN ZONING vs. FORM-BASED CODE:

  EUCLIDEAN                    FORM-BASED CODE
  ---------                    ---------------
  Regulates: USE               Regulates: PHYSICAL FORM
  Question: What is it?        Question: What does it look like?

  "No commercial use in        "Building must be placed
   R-1 district."               at the front lot line.
                                Facade must have windows
                                at ground level. Blank
                                walls > 20ft prohibited."

  Result: Could be any         Result: Walkable street
  building form so long        edge regardless of use.
  as use is residential.

FORM-BASED CODE ELEMENTS:
  Regulating Plan: map of street types and building types
  Building Envelope Standards: setbacks, height, lot coverage
  Frontage Types: stoop, shopfront, forecourt, gallery, arcade
  Building Types: cottage, house, duplex, apartment, commercial block
  Architectural Standards: facade composition, materials
  Public Space Standards: sidewalk width, street trees

SMARTCODE (Duany Plater-Zyberk):
  The canonical form-based code template.
  Organized around the "transect" --
  a rural-to-urban gradient:
  T1 (natural) -- T2 (rural) -- T3 (sub-urban)
  -- T4 (general urban) -- T5 (urban center)
  -- T6 (urban core)
  Each transect zone has appropriate building
  types, frontage types, street standards.
```

---

## Mixed Use: The Jacobs Prescription in Code

```
MIXED-USE TYPOLOGIES:

  HORIZONTAL MIXED USE:
  +---------------+ +---------------+ +---------------+
  |   COMMERCIAL  | |  RESIDENTIAL  | |     PARK      |
  +---------------+ +---------------+ +---------------+
  Uses separated by block, not stacked.
  Can generate activity if proximate,
  but not at street level.

  VERTICAL MIXED USE:
  +-------------------------------+
  |  RESIDENTIAL (floors 3+)      |
  +-------------------------------+
  |  RESIDENTIAL (floor 2)        |
  +-------------------------------+
  |  COMMERCIAL / RETAIL (floor 1)|
  +-------------------------------+
  The "life of the street":
  retail activity at pedestrian level,
  residential above.
  Ground-floor commercial must have
  minimum frontage / window requirements
  or it becomes dead office/storage.

  LIVE-WORK:
  +-------------------------------+
  |  LIVE (residential above)     |
  +-------------------------------+
  |  WORK (studio/office below)   |
  +-------------------------------+
  Artist loft model. Permitting
  challenge: residential and commercial
  codes conflict.
```

---

## Special Districts and Overlay Zones

```
SPECIAL DISTRICT TYPES:

  BID (Business Improvement District):
  - Mandatory assessment on commercial
    property owners within defined area
  - Revenue funds: cleaning, security,
    marketing, streetscaping, programming
  - ~1,000 BIDs in US; NYC has 70+
  - Governance: property owner board
  - Critique: creates tiered public realm
    (rich BIDs vs. no BID areas)

  HISTORIC PRESERVATION DISTRICT:
  - Section 106 (federal undertakings)
  - State Historic Preservation Office (SHPO)
  - Local historic districts (Certificate
    of Appropriateness required for changes)
  - National Register listing = prestige,
    access to preservation tax credits (20%
    federal ITC for certified rehab of
    income-producing historic buildings)
  - Local district = regulatory teeth

  OVERLAY ZONES:
  Base zone + additional requirements
  applied to geographic area:
  - Flood plain overlay (FEMA SFHA)
  - Airport approach overlay (height limits)
  - Environmental overlay (riparian buffer)
  - Design overlay (architectural standards)
  - Affordable housing overlay (density bonuses)

  TOD DISTRICT:
  Applied within 1/4-1/2 mile of transit station:
  - Reduced or eliminated parking minimums
  - Increased FAR
  - Ground-floor retail requirements
  - Maximum setbacks (not minimums)
  - Design standards for pedestrian experience
  - Often paired with value capture mechanism
    (land value tax increment, density bonus)
```

---

## Transit-Oriented Development (TOD)

TOD is both a design typology and a regulatory framework.

```
TOD REGULATORY TOOLKIT:

  WITHIN 1/4 MILE OF STATION ("the walk zone"):
  - Maximum FAR: 4.0-10.0 (vs baseline 0.5-2.0)
  - Parking maximum (not minimum): 1 space/unit
  - Ground-floor retail required on main streets
  - Building height: up to 8-12 storeys
  - Maximum (not minimum) setbacks

  BETWEEN 1/4 AND 1/2 MILE ("the transition zone"):
  - FAR: 2.0-4.0
  - Parking: 0.5-1.0 spaces/unit
  - Mixed uses permitted

  BEYOND 1/2 MILE:
  - Standard zoning applies

VALUE CAPTURE MECHANISMS:
  When transit investment increases land values,
  how does the public capture some of that value
  to fund the transit investment?

  Methods:
  - TIF (Tax Increment Financing): future tax revenue
    from increased values goes to transit/infrastructure
  - Special Assessment District: properties near transit
    pay additional levy
  - Developer exactions / impact fees
  - Land value tax (recurrent tax on land, not buildings --
    encourages development, captures site value increase)
  - Air rights sales (NYC: Grand Central transfer rights)
```

---

## Inclusionary Zoning

Inclusionary zoning (IZ) requires or incentivizes affordable units in market-rate developments.

```
INCLUSIONARY ZONING MECHANICS:

  MANDATORY IZ:
  Developer building X units must include Y%
  at affordable rent levels.

  Typical parameters:
  - 10-20% affordable units
  - Affordability: 60-80% Area Median Income (AMI)
  - Deed restriction: 30-55 years

  IN-LIEU FEE OPTION:
  Developer pays fee instead of building units.
  Fee goes to affordable housing fund.
  City builds affordable units elsewhere.

  DENSITY BONUS:
  In exchange for providing affordable units,
  developer gets additional FAR/height/units.
  California Density Bonus Law: state-mandated
  incentive structure (35-50% bonus for meeting
  affordability thresholds).

  THE VIABILITY CHALLENGE:
  +------------------------+    +------------------------+
  | MARKET RATE LAND VALUE |    | MARKET RATE + IZ       |
  |                        |    |                        |
  | Land: $X               |    | Land: $X               |
  | Construction: $Y       |    | Construction: $Y       |
  | Developer return: $Z   |    | IZ cost: reduces Z     |
  +------------------------+    +------------------------+
  IZ cost is borne by developer (absorbed into
  land price paid to landowner, or into reduced
  developer return). If land price is too high
  relative to what market rents support, IZ
  makes the project infeasible entirely.

  RESULT: IZ works in hot markets. Fails in
  soft markets where margins are thin.
  Can reduce total housing production if
  mandatory percentages are too high.
```

---

## Common Confusion Points

**"FAR and density are the same thing"**
FAR measures floor area relative to lot area. Density measures people or units per acre. A 4.0 FAR office building with large floor plates may have fewer people per acre than a 2.0 FAR apartment building with many small units. You can have high FAR with low residential density (office parks) or lower FAR with high residential density (many small apartments).

**"A variance lets you do anything"**
A variance is relief from dimensional standards (setbacks, height, lot coverage) — not from use restrictions. The use must still comply with the base zone. Variances require showing hardship specific to the property, not general inconvenience or financial preference.

**"Zoning controls design"**
Euclidean zoning controls use and bulk. It says nothing about architectural style, materials, or facade composition. Form-based codes and design review overlays add those controls. Most American cities use Euclidean zoning — you can build an ugly building that fully complies with zoning.

**"Upzoning automatically creates affordable housing"**
Upzoning increases housing supply potential but produces market-rate units unless paired with affordability requirements. It reduces affordability pressure over time (more supply = lower prices) but does not directly produce affordable units. Affordable production requires subsidies, inclusionary zoning, land trusts, or public housing.

**"Historic designation prevents all change"**
Local historic district designation requires review and a Certificate of Appropriateness for exterior changes. It does not freeze a building in amber. Interiors are generally not regulated. Additions are permitted if they are compatible. National Register listing has no regulatory effect unless federal funding is involved.

---

## Decision Cheat Sheet

| I want to... | The mechanism |
|---|---|
| Allow a use that zoning prohibits | Rezoning (legislative) or conditional use permit (quasi-judicial) |
| Reduce required setback for hardship | Variance (must show property-specific hardship) |
| Negotiate custom zoning for a large project | Planned Unit Development (PUD) |
| Control building form not just use | Form-based code or design review overlay |
| Require affordable units in new development | Inclusionary zoning (mandatory or voluntary with density bonus) |
| Capture value from transit investment | TIF, special assessment district, density bonus in exchange for public benefit |
| Prevent high parking lots dominating streetscape | Maximum setbacks, parking behind/under buildings, eliminate parking minimums |
| Understand if a proposed project is legal | Check zoning map (use district), zoning code (dimensional standards), then overlay zones |
| Enable housing near transit | TOD overlay: higher FAR + parking maximum + ground-floor retail required |
| Understand density limit precisely | FAR × lot area = maximum floor area; then divide by typical unit size = max units |
