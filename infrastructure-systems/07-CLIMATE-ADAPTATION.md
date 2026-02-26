# Climate Adaptation for Infrastructure: Sea Level Rise, Flooding, Heat, Wildfire

## The Big Picture

Infrastructure was designed for the historical climate. The historical climate is no longer
reliable. IPCC AR6 (2021) and its follow-on synthesis establish: sea levels will rise 0.3-1.0m
by 2100 under moderate scenarios, with 2m possible under high-end scenarios. Rainfall extremes
are intensifying. Wet-bulb temperature records are being set. Design-basis events (100-year
floods, design wind speeds) calculated from historical data increasingly understate the hazard.

```
CLIMATE HAZARD EXPOSURE TAXONOMY
===================================

                        CLIMATE HAZARD
                              |
          +-------------------+-------------------+
          |                   |                   |
    ACUTE (extreme events)    |             CHRONIC (slow-onset)
          |                   |                   |
   Hurricane intensification  |         Sea level rise
   Extreme rainfall           |         Permafrost thaw
   Flash flood                |         Desertification
   Heat waves                 |         Aquifer depletion
   Wildfire                   |         Coastal erosion
   Ice storms                 |         Salinization
          |                   |                   |
          +-------------------+-------------------+
                              |
                   INFRASTRUCTURE VULNERABILITY
                              |
          +-------------------+-------------------+
          |                   |                   |
   PHYSICAL EXPOSURE    SYSTEM EXPOSURE    CASCADING EXPOSURE
   (asset in harm's way) (capacity stress)  (interdependency)
   Flood inundation     Peak demand during  Power loss -> water
   Wind loading         heat wave           pumps fail -> health
   Wave surge           Drought -> energy   Heat -> pavement
   Thermal expansion    -> water nexus      damage -> transit
   Wildfire proximity   Supply chain stress failure -> logistics

IPCC AR6 KEY NUMBERS:
  1.1°C: global warming above pre-industrial as of 2019 (each 0.5°C: step-change in extremes)
  1.5°C pathway: requires net-zero by ~2050; some committed warming is "locked in"
  2.0°C pathway: significantly higher risk across all hazard categories
  Tail risk: 4°C+ scenarios (current policies trajectory) are infrastructure-catastrophic

NOTE: Infrastructure planning horizon (50-100 years for bridges, dams, water mains)
  means assets designed today will operate under 2070-2100 climate conditions.
  Design for expected future climate, not historical climate.
```

---

## Sea Level Rise

```
SEA LEVEL RISE: MECHANISMS AND PROJECTIONS
============================================

MECHANISMS:
  Thermal expansion: ocean warming -> water density decreases -> volume increases
    Accounts for: ~40% of 20th century SLR
    Committed expansion: even if warming stops today, expansion continues for centuries
    (thermal mass of ocean lags surface temperature)

  Ice sheet melt: Greenland + West Antarctic Ice Sheet (WAIS)
    Greenland: ~7m SLR equivalent if fully melted (very slow, millennial timescale)
    WAIS: ~3.3m SLR; marine ice sheet instability (MISI) = potential rapid collapse
    MISI concern: ice sheet rests on bedrock below sea level; warming ocean undermines
    Critical threshold: uncertain, but somewhere between 1.5-3°C above pre-industrial
    (IPCC AR6: low confidence in exact threshold but high concern)

  Mountain glaciers: ~0.3m SLR equivalent globally; fast-melting already committed

IPCC AR6 PROJECTIONS (2100 relative to 1995-2014 baseline):
  Scenario        Likely range      Upper end (17% prob)
  SSP1-2.6        0.32-0.62 m       ~0.8 m
  SSP2-4.5        0.44-0.76 m       ~1.0 m
  SSP5-8.5        0.63-1.01 m       ~1.5 m
  Low-likelihood
  high-impact     Up to 2.0 m       (MISI / marine instabilities)
  (SSP5)

  Rates: current ~3.7 mm/yr -> accelerating -> ~7-14 mm/yr by 2100 under high scenarios

LOCAL SEA LEVEL (varies significantly from global mean):
  Land subsidence adds to SLR:
    Jakarta: -25 cm/year subsidence (groundwater extraction) -> effective SLR 10x global rate
    Houston-Galveston: -5 to -10 cm/year
    New Orleans: -10 to -30 cm/year (differential compaction + extraction)
  Gravitational: as ice sheets melt, gravitational field weakens near ice -> SLR faster elsewhere
    WAIS melt: higher relative SLR on US East Coast than global average (counter-intuitive)
  Ocean circulation: AMOC weakening -> higher SLR in Northeast US
  Vertical land motion: monitored by GPS CORS stations + InSAR
```

### Coastal Infrastructure Exposure

```
COASTAL INFRASTRUCTURE VULNERABILITY TO SLR
=============================================

STORM SURGE + SLR INTERACTION (most dangerous compound event):
  Storm surge: temporary ocean rise driven by hurricane wind + low pressure
    Sandy 2012: 4.3m surge in NYC (>100-year surge on pre-Sandy frequency)
    Storm surge ≠ SLR but SLR elevates storm surge impacts
    100-year flood today: equivalent to 10-year flood with 1m SLR (10x more frequent)
    Compound events: SLR + storm surge + high tide + river flood coincide

ASSET CATEGORIES BY EXPOSURE:
  Airports:   Logan (Boston BFE +2-3m), SFO, LAX partially in SLR zones
              JFK runway 13R: 2m above mean higher high water
  Ports:      Most major US ports built at current tidal levels; 2m SLR = routine inundation
              Port of Los Angeles, Port of New York: elevation studies show significant exposure
  Water/Wastewater: Treatment plants often sited at sea level (gravity flow)
              WWTP inundation -> raw sewage discharge -> public health crisis
              Bay Area: ~$10B in SLR-exposed wastewater infrastructure
  Transit:    NYC subway: 245 km of underwater tunnels at sea level
              Sandy: flooded 25 tube crossings; $4.75B MTA repair bill
  Power:      Nuclear plants (many coastal): seawater cooling; regulatory cooling water elevation

FEMA FLOOD INSURANCE RATE MAPS (FIRMs):
  SFHA (Special Flood Hazard Area): 1% annual chance flood (100-year BFE)
  Zone AE: base flood elevation (BFE) determined; regulated
  Zone VE: coastal, wave action expected; more restrictive standards
  Problem: FIRMs based on historical data; many not updated in decades
           26,000+ FIRM panels; many last updated 1980s-90s
  NFIP reform: FEMA Risk Rating 2.0 (2021): actuarial rates based on actual risk
    Many coastal properties: premiums rising 100-400% (reveals true risk)
  Mandate gap: federal flood insurance required for federally-backed mortgages
    -> private lenders in non-NFIP properties bear risk without disclosure
```

---

## Flooding: Pluvial, Fluvial, Coastal

```
FLOOD TYPOLOGY
================

THREE TYPES:
  PLUVIAL (rainfall-generated, no waterbody):
    Cause: rain overwhelms urban stormwater system; sheet flow
    Location: urban areas with impervious surfaces, localized depressions
    Return period: design standards typically 2-10 year storm for drainage;
                   25-100 year storm for larger systems
    Climate change: precipitation intensification (thermodynamic: ~7% per °C of warming
                   per Clausius-Clapeyron); 100-year storm becoming 50-year storm
    Examples: Houston flooding outside official floodplains; Chicago basement floods
    Most frequent type: hits transportation, basements, surface infrastructure

  FLUVIAL (river/stream overflow):
    Cause: river flow exceeds channel capacity; floodplain inundation
    Location: riparian areas, river valleys; mapped in FIRM Zone A/AE
    Design: 100-year floodplain (1% AEP); FEMA NFIP regulates building in Zone AE
    Climate change: winter precipitation now rain vs. snow (warmer) -> rapid snowmelt + rain
                   = compound event; precipitation intensity -> peak flows higher
    Examples: Missouri River 1993, 2011, 2019; Mississippi River flooding

  COASTAL (storm surge, tide, SLR):
    Cause: storm surge (wind/pressure), king tides, tsunami
    Location: coast, estuaries, tidal rivers
    Climate change: SLR amplifies all coastal events (see above)
    Examples: Sandy NYC 2012, Katrina 2005, Harvey Houston 2017

STORMWATER DESIGN STANDARDS PROBLEM:
  Traditional design: calculate peak runoff using rational method or TR-55
    Q = C * i * A (runoff = runoff coefficient × intensity × area)
    "i" from IDF (Intensity-Duration-Frequency) curves based on historical record
  Problem: IDF curves derived from ~30-50 year historical records
    NOAA Atlas 14: published IDF data; many regions' Atlas 14 data already outdated
    NOAA is updating Atlas 14 to incorporate climate trends (Atlas 15 coming)
    Many stormwater systems: designed to Atlas 14; already undersized for current events
  Future design requirement: use climate-adjusted precipitation estimates
    "Non-stationary" frequency analysis: integrate trend into return-period calculation

GREEN INFRASTRUCTURE:
  Traditional gray: pipes, concrete channels, detention basins
  Green: retain/infiltrate/evapotranspire stormwater on site
  Tools:
    Green roofs: 50-75% runoff reduction for storms up to 2.5 cm
    Permeable pavement: infiltrate up to 100% of small storms
    Bioswales: slow + filter sheet flow; 25-50% runoff reduction
    Urban trees: interception + ET; 1 mature tree: 30-90 L/day ET
    Rain gardens: 50-90% first-flush capture
    Constructed wetlands: multiple-function (flood, water quality, habitat)
  Philadelphia GSI: $2.4B green infrastructure program replacing sewer CSO overflows;
    cost of $60-80k/acre managed vs. $300-500k/acre gray equivalent
  Limit: effective for small storms (first flush); major floods still need gray infrastructure
```

---

## Heat Stress

```
EXTREME HEAT AND INFRASTRUCTURE
==================================

WET-BULB TEMPERATURE (WBT): THE SURVIVAL THRESHOLD
  Wet-bulb temperature: temperature with 100% humidity at that level
    (measured by wet thermometer; combines heat + humidity)
  35°C WBT = theoretical physiological limit for healthy humans
    At 35°C WBT: core body temperature rises even at rest in shade
    Actual danger: WBT 28-31°C = significant risk for outdoor workers/elderly
  Historical: never exceeded before ~2017; now occurring in Persian Gulf, South Asia
    Pakistan/India (2022): wet-bulb temps 31-33°C reached for hours
    Pakistan Jacobabad: 30°C WBT reached; WHO emergency conditions
  IPCC projection: 35°C WBT events (1-2 hr duration): likely in some regions by 2050
    under SSP5-8.5; dangerous WBT levels much more widespread

INFRASTRUCTURE HEAT EFFECTS:
  ROADS:
    Asphalt pavement: bitumen softens at high temp -> rutting under traffic load
    Thermal expansion: concrete pavement joint blowup (buckling of slabs)
      Chicago 2012: several concrete highway blowups during heat wave
    Steel bridges: thermal expansion; 100m bridge: +12 cm at ΔT = 50°C (200m bridge: 24 cm)
    AASHTO bridge design: expansion joints and thermal forces calculated for design temp range
    Changing climate: design temperature ranges shifting; joints undersized in some climates

  ELECTRICAL GRID:
    Transmission lines: thermal sag
      Aluminum ACSR conductor: rated ampacity based on thermal limit (75-90°C conductor)
      High ambient temp + high solar load: reduces ampacity 20-40% on hot days
      Demand peaks on hot days: highest demand exactly when capacity lowest
      NERC: thermal emergency ratings must account for ambient temperature
    Distribution transformers: ambient temp affects insulation life
      Per Montsinger Rule: +10°C = ~50% reduction in transformer insulation life
      Urban heat island + climate warming = shorter transformer life
    Substations: oil-filled equipment thermal limits; some require supplemental cooling
    Air conditioning load: positive feedback loop -- heat -> more AC -> more load

  RAILWAYS:
    Rail thermal expansion: steel rail expands 12 mm per 1°C per 100m (or: 1.2 mm per 1°C per 10m)
    Thermal neutral temperature (TNT): rail is stress-free at TNT (typically 25-35°C depending on region)
    Above TNT: compression -> buckling ("sun kink" or "thermal misalignment")
      Buckling causes derailment: historic UK speed restrictions when temp >30°C
      Netherlands 2021: trains slowed to 80 km/h when ambient >27°C
    Speed restriction protocols: mandatory slow orders when temp exceeds thresholds
    Design solution: higher TNT during rail installation (thermite welding at higher tension)

  COOLING WATER:
    Thermal power plants: require cold water for cooling (efficiency decreases in hot water)
    Rivers: elevated temp reduces dissolved oxygen + river flow in drought -> forced derating
    France 2003: EDF forced to derate 8 nuclear plants due to Rhone/Loire thermal limits
    France 2022: repeated; nuclear generation reduced by ~10% during August heat
    Regulatory limits: water discharge temperature limits (Clean Water Act thermal standards)
    Climate interaction: warmer rivers + lower flow = more frequent conflict

URBAN HEAT ISLAND (UHI):
  Magnitude: urban core 3-10°C hotter than surrounding rural area
  Mechanism: impervious surfaces (low albedo), waste heat from buildings/vehicles,
             reduced evapotranspiration (fewer trees, surfaces don't evaporate)
  Infrastructure implication: UHI amplifies climate warming for urban infrastructure
  Mitigation:
    Cool pavements (high-albedo coatings, reflective chips): reduce temp 2-5°C
    Green roofs: reduce surface temp 30-40°C vs. conventional black roof
    Urban tree canopy: 40% canopy cover target (most US cities at 20-25%)
    White roofs: albedo 0.6-0.8 vs. black 0.05; reduce cooling energy 10-15%
```

---

## Wildfire

```
WILDFIRE AND INFRASTRUCTURE
==============================

WILDFIRE-INFRASTRUCTURE INTERACTIONS:
  Transmission lines: arcing/sparking -> ignition (Camp Fire, CA 2018: PG&E transmission line)
    -> liability for utility (PG&E $13.5B bankruptcy settlement)
    Direct burn: wooden poles burn; steel towers survive; conductors may anneal/sag
  Substations: oil-filled equipment vulnerable; loss of station = widespread outage
  Water systems:
    Plastic distribution pipes in burned areas: benzene contamination from thermally deformed PE
    Paradise, CA (Camp Fire): ~90% of plastic water mains detected benzene;
    system had to be replaced entirely ($280M)
    Mechanism: volatile organics from burning buildings permeate HDPE pipe walls
  Roads/bridges: wooden bridges burn; asphalt may soften; debris flow risk post-fire
    Post-fire debris flow (1-2 years): denuded slopes, lost vegetation -> erosion
    LA Basin: I-405 corridor post-fire debris risk significant
  Telecommunications: cell tower survival depends on concrete vs. wood construction
  Natural gas: exposed pipelines at risk from external heat; coating damage

ELECTRIC TRANSMISSION AND WILDFIRE RISK:
  High-Fire Threat Districts (HFTD): California CPUC defines zones H/T by risk
  Wildfire mitigation plans: California AB 1054 requires IOUs to submit annually
  Weather stations + sensors: utilities installing dense weather networks
    SCE: 800+ weather stations in fire territory; PG&E: 1,200+
  High-Definition cameras: ALERTWildfire network; 1,000+ cameras in CA alone
  AI fire detection: smoke detection algorithms on camera feeds (real-time)
  Public Safety Power Shutoff (PSPS): de-energize circuits during extreme fire weather
    PG&E 2019: ~900,000 customers blacked out for 5 days (wildfire vs. economic damage trade-off)
    Problematic for: medical equipment, food, pumping stations, cell towers on backup
  Undergrounding: gold standard but expensive ($3-5M/mile underground vs. $0.5M/mile overhead)
    PG&E undergrounding plan: 10,000 miles over 10 years ($15-20B)
    Triage approach: underground highest-risk segments only

DROUGHT-INFRASTRUCTURE NEXUS:
  Water supply: reservoir levels, snowpack, groundwater depletion
    Colorado River: Lake Mead at 30% capacity (2022); first Tier 1 shortage declared
    Long-term: IPCC projects Mediterranean-climate regions drying further
  Hydroelectric: drought -> reduced generation -> grid stress
    Pacific Northwest 2021 heat dome: BPA/Columbia River system derated
    California 2021: hydro fell to 8% of mix (vs. historical 20-25%)
  Ground subsidence: groundwater extraction -> land subsidence -> pipe damage
    San Joaquin Valley: up to 8m subsidence over 20th century; ongoing
    Aqueduct damage, levee settlement, well casing damage all observed
  Soil shrink-swell: expansive clay soils: water loss -> shrinkage -> foundation/pipe damage
    Southern US clays: most common cause of residential foundation damage
  Wildfire-drought connection: drought dries fuels -> more intense fire -> worse water quality
```

---

## Adaptation Strategies

### The Adaptation Framework

```
ADAPTATION DECISION FRAMEWORK: PROTECT-ACCOMMODATE-RETREAT
============================================================

PROTECT (keep water out):
  Hard armoring:
    Sea walls: vertical concrete/steel structures; reflect wave energy; undermine over time
    Revetments: sloped riprap; dissipate wave energy; less reflection but large footprint
    Levees: earthen embankments; protect large areas; failure is catastrophic (not gradual)
    Floodgates/barriers: movable; Netherlands Delta Works; Thames Barrier (London)
      Thames Barrier: 10 steel gates 61m wide × 20m; raised 200+ times since 1982
      New York ESCR: proposed 8km barrier for Upper NY Bay (cost $119B, decades to build)
    Pump stations: remove water from protected area (New Orleans: 130 pumping stations)

  Nature-based solutions (NbS):
    Living shorelines: oyster reefs + marsh grass + sand; attenuate waves; self-repairing
    Mangrove restoration: 50-90% wave attenuation; provides 100s kms of buffer
    Barrier island restoration: natural storm surge buffer; Louisiana Coastal Master Plan
    Dune restoration: stabilize with native grasses; dunes serve as first defense
    NbS advantage: self-maintaining, ecologically beneficial, cost-effective at scale
    NbS limitation: can't protect urban areas at high storm surge; wave height/period limits

ACCOMMODATE (live with water):
  Flood-resilient design:
    Elevate buildings: first-floor elevation above BFE (+ freeboard)
    Floodproofing: dry (barriers) or wet (allow water in, protect contents)
    Wet-proof critical equipment: move electrical panels, HVACs to roof/upper floors
    Permeable design: let water pass through at grade; waterproof below grade
  Blue-green urban design:
    Sponge cities: Chinese policy framework; Wuhan, Xiamen pilot cities
    Rotterdam WaterSquares: public plazas that flood as temporary detention basins
      Benthemplein, Rotterdam: 1,700 m² basin stores 1.7M liters; drained to canal after storm
    Singapore ABC Waters Programme: convert concrete canals to naturalized waterways
    Floating structures: Netherlands floating homes/offices on IJburg; resilient by design

RETREAT (move out of the way):
  Managed retreat: planned relocation of communities away from high-risk areas
    Most cost-effective long-term; politically most difficult
    FEMA Hazard Mitigation Grant Program: voluntary buyouts
    Post-Sandy: New Jersey Hazard Mitigation bought out 800+ homes ($2B)
    Louisiana: CDBG-DR used for voluntary buyout in Isle de Jean Charles
  Infrastructure retreat:
    Power lines: reroute inland (California utility undergrounding programs)
    Roads: elevate or reroute vulnerable segments
    Water intakes: move coastal intakes inland (saltwater intrusion)

COMPARISON TABLE:
  Strategy    Cost     Effectiveness  Duration  Ecological  Political
  Hard armor  $$$$     High (if sized) 50-100yr  Negative    Easy
  NbS         $$       Med-High        Ongoing   Positive    Easy
  Accommodate $$-$$$   High (local)    Permanent Mixed       Moderate
  Retreat     $-$$     Very high       Permanent Positive    Very Hard
```

### Design Standards Reform

```
DESIGN STANDARDS FOR CHANGING CLIMATE
========================================

THE STATIONARITY PROBLEM:
  Classic hydrology assumption: "stationarity" -- statistical properties of climate variables
  (precipitation, temperature) are time-invariant; past record predicts future
  Reality: Milly et al. (2008) Science paper: "Stationarity Is Dead"
  Implication: every design standard based on historical IDF curves, 100-year flood
  estimates, design temperature ranges, sea level assumptions is potentially wrong

  Current practice (most jurisdictions):
    Infrastructure designed to historical 100-year flood (1% AEP)
    Climate change not formally incorporated into standard IDF curves
    Engineer's professional responsibility: note climate change risk, but no codified method
    Result: systematic under-design for future climate

  Leading practice:
    Climate-adjusted IDF curves (some states: Colorado, California, New York updating)
    Delta method: adjust historical quantiles by climate model change factors
    Scenario-based design: design for multiple scenarios (RCP 4.5, 8.5) + sensitivity

SPECIFIC STANDARDS EVOLUTION:
  FEMA FIRMs: slow update cycle; FEMA Risk Rating 2.0 includes some future risk
    Expected update to 50-year risk horizon (still insufficient for 100-year design life)
  ASCE 7 (loads standard): wind speeds updated 2022 for hurricane intensity increases
    Flood load provisions: updated for SLR in coastal sections
  ASCE 24 (flood-resistant design): freeboard requirements; minimum 1 ft above BFE
    Now recommending 2-3 ft in high-risk areas
  FHWA: issued "Climate Change and Extreme Weather Vulnerability Assessment Framework"
    Not mandatory; guidance only; some state DOTs using it
  USACE Engineering Manual 1110-2-1619: riverine flood frequency; guidance evolving
  Corp of Engineers: incorporating sea level change scenarios into coastal design
    3 scenarios (low/intermediate/high) per USACE ER 1100-2-8162

PERFORMANCE-BASED CLIMATE DESIGN:
  Define performance goals first: "Bridge serves traffic under 1.5-2.0m SLR + 100-yr storm"
  Identify hazards at each scenario
  Design to achieve performance goal
  This is the engineering answer to non-stationary climate
  Analogy to performance-based earthquake engineering (PBEE): well-established for seismic
  Climate equivalent still emerging; most rigorous framework
```

---

## Climate Risk Disclosure

```
CLIMATE RISK DISCLOSURE FOR INFRASTRUCTURE OWNERS
====================================================

TCFD (TASK FORCE ON CLIMATE-RELATED FINANCIAL DISCLOSURES):
  Created: Mark Carney + Michael Bloomberg 2015 (G20 initiative)
  Four pillars:
    Governance: board/management oversight of climate risk
    Strategy: climate impacts on strategy, business model, financial planning
    Risk Management: how climate risk identified, assessed, managed
    Metrics and Targets: GHG emissions, climate-related risks/opportunities metrics

  Two risk types:
    Physical risk: acute (extreme events) and chronic (long-term shifts)
      Relevant: asset exposure to floods, heat, SLR, wildfire
    Transition risk: shift to low-carbon economy
      Relevant: stranded assets (fossil fuel infrastructure), carbon pricing, policy change

  Infrastructure-specific TCFD guidance: TCFD Preparer Forum (utilities, transport, water)
    Asset registry: map assets to climate hazard zones
    Scenario analysis: financial impact under 1.5°C, 2°C, 4°C pathways
    Disclosure: in annual reports, 10-K, bond offering documents

SEC CLIMATE DISCLOSURE RULE (2024):
  Final rule (March 2024): large accelerated filers begin FY2025 disclosure
  Required disclosures:
    Material climate-related risks and impacts
    Governance and risk management processes
    Scope 1 and 2 GHG emissions (for large filers)
    Financial statement impacts >1% of line item
  Stayed by litigation (pending courts): future uncertain
  State equivalents: California SB 253 (emissions) + SB 261 (climate risk) effective 2026
    Applies to public + private companies doing business in CA with >$500M / >$1B revenue

MUNICIPAL BOND MARKET:
  Infrastructure debt: cities/counties issue munis to fund infrastructure
  Moody's, S&P, Fitch: incorporating climate risk into municipal credit ratings (2021+)
  Miami-Dade, Atlantic City: already rated lower partially due to flood/SLR risk
  Rule of thumb: 1m SLR within 20-year bond horizon -> material credit risk
  MSRB: Municipal Securities Rulemaking Board; no mandatory climate disclosure yet
  Investor pressure: CalPERS, CalSTRS, PGGM: requiring climate risk disclosure from issuers

PHYSICAL RISK SCREENING TOOLS:
  Four Twenty Seven (acquired by Morningstar): physical risk scoring by asset
  Jupiter Intelligence: forward-looking climate risk scores, 5/10/30-year horizons
  XDI (Cross Dependency Initiative): built environment physical risk
  ClimateCheck: property-level climate risk (flood, fire, heat, drought, storm)
  All tools: combine climate models + asset location + vulnerability modeling
  Limitation: uncertainty ranges are very wide; point estimates misleading
```

---

## Decision Cheat Sheet

| Climate adaptation question | Answer |
|-----------------------------|--------|
| IPCC AR6 SLR by 2100 (likely range) | 0.32-0.62m (SSP1-2.6) to 0.63-1.01m (SSP5-8.5); 2m possible under low-prob high-impact scenarios |
| What makes local SLR different from global mean? | Land subsidence (Jakarta -25cm/yr), gravitational effects from ice melt, AMOC changes |
| Three flood types | Pluvial (rainfall, no waterbody), Fluvial (river overflow), Coastal (surge/tide) |
| What is the stationarity problem? | Historical climate statistics no longer reliably predict future; design IDF curves outdated |
| Physiological heat limit | 35°C wet-bulb temperature: fatal for humans at rest; dangerous conditions from 28-31°C WBT |
| Why do plastic water mains fail after wildfire? | Benzene from burning structures permeates HDPE/PVC pipe walls; contamination persists |
| Protect-Accommodate-Retreat comparison | Protect = high cost, negative ecology; Accommodate = flexible, moderate cost; Retreat = cheapest but politically difficult |
| What is TCFD? | Task Force on Climate-related Financial Disclosures: governance/strategy/risk/metrics framework for climate risk reporting |
| Rotterdam WaterSquares | Urban plazas designed to function as temporary flood detention basins during storms |

---

## Common Confusion Points

**"The 100-year flood happens once per century."** It is the flood with 1% probability per year.
In any 100-year period, the probability of experiencing at least one such flood is 63% (1 - 0.99^100).
Climate change is shifting the statistical distribution: today's 100-year flood is estimated to become
a 50-year or 30-year event in many locations by mid-century under current trajectories.

**"Sea level rise is uniform globally."** It varies significantly. Local subsidence,
gravitational effects from ice sheets melting, and ocean circulation changes all create
regional patterns. Some regions (US East Coast) will experience SLR above global mean
due to AMOC weakening and WAIS gravitational effects. Some regions (Scotland, Scandinavia)
are rising from isostatic rebound faster than SLR. Global mean is a starting point, not
the operational number for any specific project.

**"Climate adaptation is a future problem for future engineers."** Infrastructure designed
today has a 50-100 year design life. A bridge designed in 2025 must perform under 2075-2125
climate conditions. The climate commitment from current GHG concentrations is already "locked in"
for substantial change within the design lives of assets being designed now. Climate-adjusted
design is an immediate engineering obligation, not a future one.

**"Managed retreat is giving up."** It is often the most rational and cost-effective long-term
strategy for highly exposed assets. In some locations -- low-lying barrier islands, tidal marshes,
floodplains -- the engineering cost of protection exceeds the value of what is being protected.
Continued investment in protection without transition planning creates stranded assets and
increases the eventual disruption. The political difficulty does not diminish the economic case.
