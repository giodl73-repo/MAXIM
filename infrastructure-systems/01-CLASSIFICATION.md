# Infrastructure Classification: CISA Sectors, Lifeline Infrastructure, and Taxonomy

## The Big Picture

Infrastructure classification serves multiple purposes: policy coordination, security
planning, investment prioritization, and interdependency analysis. The CISA 16-sector
framework (US federal) is the canonical reference for critical infrastructure in the
United States and influences policy frameworks globally.

```
CRITICAL INFRASTRUCTURE CLASSIFICATION FRAMEWORK
=================================================

POLICY BASIS:          CISA 16 SECTORS
Presidential Policy    (Presidential Policy Directive 21, 2013)
Directive 21                    |
                                v
                        SECTOR-SPECIFIC AGENCIES (SSA)
                        (coordinate security + standards)
                                |
                        +-------+-------+
                        |               |
                  LIFELINE SECTORS  SUPPORT SECTORS
                  (enable all)      (important but
                  Energy            dependent on lifeline)
                  Water
                  Communications
                  Transportation

OWNERSHIP SPECTRUM:
  100% Public         Regulated Utility        Private
  =========          ================        =========
  Water mains        Electric distribution    Telecom (most)
  Roads              Gas pipelines            Airlines
  Locks/dams         Nuclear plants           Railroads (US)
  Military           Water utilities          Data centers
```

---

## The CISA 16 Sectors in Detail

### Lifeline Sectors (Tier 1)

```
LIFELINE INFRASTRUCTURE: THE ENABLING FOUR
===========================================

These four sectors enable all others. Their failure cascades universally.

1. ENERGY (SSA: Department of Energy)
   Subsectors:
   - Electric systems: generation, transmission, distribution
     Roughly: 3,300 utilities, 700,000+ km transmission lines, 1.7M km distribution
     Generation mix (US 2024): ~40% gas, 20% nuclear, 18% wind+solar, 17% coal, 5% hydro
   - Natural gas: production, processing, pipeline, distribution
     ~500,000 km pipeline, 12,000 delivery points
   - Petroleum: refineries, pipelines, terminals, retail
     Depends on: transportation (product delivery), water (refinery cooling)
     Depends on by: essentially all other sectors (fuel, feedstocks)

2. WATER AND WASTEWATER (SSA: EPA)
   Subsectors:
   - Drinking water: ~148,000 public water systems (US)
     Source -> treatment -> distribution -> customer
     SDWA (Safe Drinking Water Act): federal standards
   - Wastewater: ~16,000 publicly owned treatment works (POTWs)
     Collection -> primary treatment -> secondary -> tertiary -> discharge/reuse
   Critical dependency: water treatment requires electricity (pumps, UV, chlorination)
   Critical dependency: electricity requires water (cooling for 90% of thermoelectric generation)
   This is the water-energy NEXUS -- circular dependency with no safe dominant failure direction

3. COMMUNICATIONS (SSA: CISA / DHS)
   Subsectors:
   - Wireline: copper PSTN (declining), fiber broadband, co-ax cable
   - Wireless: cellular (LTE/5G), satellite (LEO: Starlink; GEO: Hughes)
   - Internet backbone: IXPs (Internet Exchange Points), submarine cables (~400 active)
   - Broadcast: AM/FM radio, television, emergency alert system (EAS)
   Critical: every other sector's SCADA/control relies on communications
   Single-point risks: submarine cables (physical damage, e.g., Taiwan Strait), IXPs

4. TRANSPORTATION (SSA: DOT)
   Subsectors:
   - Roads and bridges: 4.2M miles of roads, 619,000 bridges (US)
   - Rail: freight (7 Class I railroads), passenger (Amtrak + commuter rail)
   - Aviation: 497 commercial airports, ~14,000 air traffic control facilities
   - Maritime: 360 ports, waterways (Great Lakes, Mississippi, Intracoastal)
   - Pipeline: 2.7M miles natural gas distribution + transmission
   - Postal and shipping: mail, parcel, supply chain logistics
```

### Support Sectors (Tier 2 and 3)

```
SUPPORT SECTORS TAXONOMY
==========================

DIRECTLY DEPENDENT ON LIFELINE:
  Healthcare and Public Health (SSA: HHS)
    Hospitals, labs, blood supply, pharmaceutical supply chain
    Cannot operate without reliable power, clean water, communications
    EHR systems, life-critical equipment: extreme power dependency

  Emergency Services (SSA: DHS)
    Police, fire, EMS, USAR (Urban Search and Rescue)
    Requires: communications (radio), transport (vehicles + fuel), power
    First responders ARE part of the resilience system -- protect them first

  Financial Services (SSA: USDT)
    Banks, clearinghouses (DTCC: $2 quadrillion/year), exchanges, ATMs
    Depends critically on: communications, power, cyber infrastructure
    Systemic risk: financial crisis can trigger infrastructure underinvestment

INDUSTRIAL / PRODUCTION:
  Critical Manufacturing (SSA: CISA)
    Steel, aluminum, primary chemicals, semiconductor fab, aerospace
    Highly dependent on energy (aluminum smelting: 15 kWh/kg)
    Material inputs to other critical infrastructure (steel for bridges, Si for chips)

  Chemical (SSA: CISA)
    Chemical plants (hazmat risk: chlorine, ammonia, toxic industrial chemicals)
    Chemical weapons potential (dual-use concern)
    Proximity to population (1/3 of US population within 1 mile of chemical facility)

  Dams (SSA: USACE)
    ~90,000 dams in US (6,600 high-hazard potential)
    Functions: flood control, hydroelectric, water supply, navigation
    Age concern: average dam age >50 years (many designed pre-computer structural analysis)
    Failure mode: overtopping + erosion (Oroville 2017: $1.1B repair, 188k evacuated)

GOVERNMENT AND CIVIC:
  Government Facilities (SSA: GSA / DHS)
    Continuity of government (COG) planning
    Court systems, records, administrative function
    Not just federal: state and local government is larger total asset base

  Defense Industrial Base (SSA: DoD)
    Contractors supporting defense: Boeing, Lockheed, RTX, defense electronics
    Supply chain vulnerability: concentration in few suppliers
    Single-source components: critical vulnerability (rare earth magnets, specialty chips)

  Nuclear (SSA: NRC)
    Nuclear reactors: ~90 commercial (US); highest-consequence, lowest-probability risk
    Strict NRC regulation (10 CFR 50, 73); license basis analysis
    Physical security: armed response force requirement (DBT: Design Basis Threat)
    Waste storage: spent fuel pools + dry cask storage; no permanent repository (US)

INFORMATION:
  Information Technology (SSA: CISA)
    Hardware manufacturers (Intel, TSMC, Samsung -- mostly not in US)
    Cloud providers (AWS, Azure, GCP -- top 3 = 65% of cloud)
    Software: OS, critical applications, open-source dependency chains
    Internet infrastructure: BGP routing, DNS, certificate authorities
    Note: "IT" and "Communications" overlap significantly -- policymakers debate boundary

FOOD AND CIVIC:
  Food and Agriculture (SSA: USDA + FDA)
    Primary production (farms, ranches, aquaculture)
    Processing (meatpacking, grain mills, dairy processing)
    Distribution (cold chain, trucking, warehousing)
    Dependency: water (irrigation), energy (refrigeration, processing), transportation
    Concentration risk: 4 meatpackers control 85% of US beef processing

  Commercial Facilities (SSA: CISA)
    Malls, hotels, theme parks, sports venues, casinos
    High-occupancy, publicly accessible -> terrorist target concern
    Relatively low infrastructure dependency vs. other sectors
    More economic resilience concern than physical cascades
```

---

## Infrastructure Taxonomy by Ownership

```
OWNERSHIP AND GOVERNANCE TAXONOMY
====================================

PUBLIC (government-owned and operated):
  Water utilities (most US water systems)
  Roads, bridges, ports (most)
  Transit (municipal)
  Public power (TVA, NYPA, municipal utilities -- ~25% of US electricity)
  Government buildings

  Governance: elected officials, appointed directors
  Finance: general obligation bonds, taxes, federal grants
  Accountability: public oversight, FOIA, procurement rules

REGULATED PRIVATE (investor-owned utility, IOU):
  Electric distribution and most transmission (~75% of US electricity)
  Natural gas distribution and interstate pipelines
  Most US telecommunications (AT&T, Verizon)
  Nuclear power plants

  Governance: private corporation under regulatory oversight
  Finance: rate of return regulation: FERC, state PUC set allowed rate of return
    Allowed ROE (return on equity): 8-12% for electric utilities (PUC-determined)
    Cost-plus regulation: revenue = operating cost + capital return -> no incentive to cut cost
  Accountability: rate cases (public hearings on rate increases), annual reports
  Security requirements: NERC CIP (electric), TSA (pipeline), FCC (telecom)

PRIVATE UNREGULATED:
  Most broadband internet providers (ISPs in US: no rate regulation post-2017 FCC)
  Airlines, railroads (deregulated 1978, 1980)
  Data centers, cloud providers (mostly unregulated)
  Privately-owned ports
  Fuel retail (gas stations)

  Governance: private company, minimal public oversight
  Finance: market-driven
  Accountability: market competition (if it exists) or voluntary standards

QUASI-PUBLIC / AUTHORITY:
  Port authorities (Port Authority of NY/NJ: bridges, tunnels, airports, ports)
  Airport authorities
  Transit authorities (MTA, Bay Area BART, DC Metro)
  Toll road authorities

  Governance: appointed board, revenue bonds, limited oversight
  Finance: toll revenue, bonds
  Accountability: varies; less transparent than pure government in some cases

INTERNATIONAL COMPARISON:
  UK: privatized water (1989), electricity (1990), rail (1993) -- mixed results
    Thames Water: heavily indebted, required government rescue 2024
    UK rail: re-nationalized 2023-2024 (failed private franchise model)
  France: mixed (EDF state-majority for nuclear, SNCF for rail)
  Germany: DB (rail) state-owned; energy: mixed public/private
  Japan: JR (rail) privatized 1987 -- broadly successful
```

---

## Sector Criticality and Prioritization Framework

```
RISK-BASED SECTOR PRIORITIZATION
===================================

CONSEQUENCE ASSESSMENT (example framework):
  Life safety (immediate): deaths, injuries in event
  Life safety (delayed): healthcare system failure, water contamination
  Economic: GDP impact, supply chain disruption
  Social: civil order, government function
  Duration: hours vs. days vs. weeks vs. permanent

RISK = PROBABILITY x CONSEQUENCE x VULNERABILITY
  High-risk sectors: high consequence + high vulnerability (many entry points)
    Communications: extremely high consequence (everything depends on it);
                   moderate vulnerability (redundant but attack surface huge)
    Electric: high consequence; moderate-high vulnerability (physical + cyber)
  Lower-risk: low consequence OR low vulnerability
    Commercial facilities: moderate consequence; high vulnerability (open public access)
    Postal: low consequence; low vulnerability

INTERDEPENDENCY MULTIPLIER:
  Lifeline sectors have consequence multiplier due to cascades:
    Power failure -> water treatment fails within 12-24 hr (backup power limited)
    -> Healthcare systems overwhelmed within 48 hr
    -> Social stability concerns within 72 hr
  Non-lifeline sectors rarely trigger this cascade
  Prioritize: protect lifeline sectors above all others in limited resource scenario

NIPP (National Infrastructure Protection Plan):
  US framework: sector-specific plans + CISA coordination
  Updated periodically; 2013 framework most recent (some updates 2024)
  Key concept: "risk-informed" prioritization, not protection of all equally
```

---

## Decision Cheat Sheet

| Sector question | Answer |
|----------------|--------|
| Which 4 sectors enable all others? | Energy, Water, Communications, Transportation |
| Who sets federal standards for electric grid security? | NERC (NERC CIP mandatory) under FERC oversight |
| Who sets water security standards? | EPA (AWIA) + CISA for critical water |
| Who is the SSA for IT sector? | CISA / DHS |
| What is the legal basis for CI protection? | PPD-21 (2013) + CISA Act (2018) |
| What % of US electricity comes from IOUs? | ~75% (regulated private) |
| What is the biggest ownership gap? | Broadband internet: private, largely unregulated |
| What sector has most concentrated ownership risk? | Financial (DTCC single clearinghouse) + food (4 meatpackers) |

---

## Common Confusion Points

**"Critical infrastructure is public property."** Most US critical infrastructure is
privately owned: ~85% of electricity generation and transmission, most telecommunications,
most rail (freight), most pipelines. This creates significant governance challenges --
private owners have legal rights that complicate mandatory security investment.

**"CISA 16 sectors are comprehensive."** They are the US government's categorization for
planning purposes, not a rigorous taxonomy. Sectors overlap (IT and Communications; Energy
and Critical Manufacturing). The categorization reflects organizational history as much
as technical logic.

**"Lifeline infrastructure failure would take weeks to cascade."** Much faster.
Loss of electric power -> water treatment pump stops working -> backup generator runs 24-72 hr
-> without resupply: water service disruption within 3 days in most systems.
Hospital backup generators: typically 72-96 hour fuel supply, then fuel delivery required.
Modern society has shorter resilience buffers than most people imagine.
