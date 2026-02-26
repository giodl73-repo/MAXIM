# Infrastructure Failure Modes: Physical, Cyber, Systemic

## The Big Picture

Infrastructure fails through four distinct mechanisms: physical degradation, natural
hazards, cyber attack/failure, and systemic factors (deferred maintenance, organizational
failure). Understanding the mechanism determines the appropriate mitigation strategy.

```
INFRASTRUCTURE FAILURE TAXONOMY
=================================

                    FAILURE CAUSE
                          |
         +----------------+----------------+
         |                |                |
    PHYSICAL         NATURAL HAZARD     CYBER
    DEGRADATION      (external)         (IT/OT)
         |                |                |
   Material failure  Earthquake          Attack
   Fatigue           Hurricane           Malware
   Corrosion         Flood               Ransomware
   Overload          Tornado             Insider
   Construction      Ice storm           SCADA failure
   defects           Wildfire
         |                |                |
         +----------------+----------------+
                          |
                     SYSTEMIC
                    (underlying)
                          |
              Deferred maintenance
              Budget constraints
              Organizational failure
              Regulatory gaps
              Design standards obsolescence
```

---

## Physical Failure Modes

### Corrosion

```
CORROSION: THE INVISIBLE INFRASTRUCTURE KILLER
===============================================

US ANNUAL CORROSION COST: ~$270B/yr (2002 NACE study, inflation-adjusted ~$550B/yr 2025)
  ~3.1% of GDP -- comparable to annual federal defense spending
  Infrastructure-specific portion: ~$100B/yr (bridges, pipelines, utilities)

MECHANISMS:
  Electrochemical corrosion (dominant):
    Galvanic cell: two dissimilar metals + electrolyte (moisture, salt water)
    Anode: Fe -> Fe2+ + 2e- (iron oxidizes, dissolves)
    Cathode: O2 + 2H2O + 4e- -> 4OH- (oxygen reduction)
    Net: 4Fe + 3O2 + 2H2O -> 2Fe2O3*H2O (rust = iron hydroxide)
    Accelerators: salt (road salt on bridges: Cl- disrupts passive oxide layer),
                  moisture, low pH, elevated temperature, impressed current

  Microbiologically influenced corrosion (MIC):
    Sulfate-reducing bacteria (SRB): produce H2S from sulfate
    H2S attacks steel pipe: Fe + H2S -> FeS + 2H (accelerated corrosion under anaerobic conditions)
    Common in: water mains, buried gas pipelines, oil pipelines

  Stress corrosion cracking (SCC):
    Combined: tensile stress + corrosive environment + susceptible material
    Results in cracking at stress levels well below yield strength
    Catastrophic: no visible warning; sudden failure
    Example: SCC in high-pressure gas pipelines (high-strength steel + cathodically disbonded coating)
    San Bruno, CA pipeline explosion (2010): SCC + poor maintenance + seam weld defect -> 8 deaths

PIPELINE CORROSION:
  US natural gas transmission: ~500,000 km of pipeline
  Average age: >40 years (many pre-1970)
  Cathodic protection: impressed current or sacrificial anode
    CP maintains pipe potential at -850 mV vs. Cu/CuSO4 reference
    CP failure: corrosion resumes; typical failure: coating disbondment + CP inadequacy
  Inline inspection (ILI): "smart pig" tool runs inside pipeline
    Magnetic flux leakage (MFL): detects metal loss (corrosion)
    Geometry tool: detects dents, deformations
    Run interval: high-consequence areas every 5-7 years (per federal regulations)

BRIDGE CORROSION:
  Rebar in concrete: normally passive (high pH concrete)
  Chloride ingress (road salt, marine): destroys passive film -> active corrosion
  Rebar expands 2-3x when rusting -> concrete spalling (chunks falling off)
  Approximately 7.5% of US bridges are structurally deficient (2024)
  ~600 bridges in poor condition (FHWA BCI < 50 -- immediate priority)
```

### Fatigue and Material Failure

```
METAL FATIGUE IN INFRASTRUCTURE
=================================

MECHANISM:
  Cyclic loading: each load cycle creates/propagates microcracks
  Paris law: da/dN = C * (delta_K)^m
    a = crack length, N = cycles, K = stress intensity factor (MPa*sqrt(m))
  Critical crack length: when K > K_IC (fracture toughness): catastrophic failure

INFRASTRUCTURE EXAMPLES:
  Railway: rail fatigue from passing trains (1B+ cycles over 50 years)
    Rail inspection: eddy current, ultrasonic (detect cracks before failure)
    Change-out interval: 100-500 million gross tonnes (varies by traffic)

  Bridges: girder web fatigue at connection details
    AASHTO fatigue categories: A (best) to E' (worst)
    Fatigue life: 20-100 million cycles (major highway bridge)
    Silver Bridge collapse (WV, 1967): 46 deaths; eyebar chain stress corrosion + fatigue
    -> Led to National Bridge Inspection Program (NBIP)

  Offshore wind: cyclic wave + wind loading on monopile foundations
    10^8 to 10^9 load cycles over 25-year design life
    Foundation inspection every 5 years; grouted connections problematic (cracking found)

CONCRETE FAILURE MODES:
  Carbonation: CO2 + Ca(OH)2 -> CaCO3 (reduces pH -> rebar corrosion initiation)
  Alkali-silica reaction (ASR): alkali (Na+, K+) + reactive silica aggregate -> expansive gel
    Concrete cracking, "map cracking" visible on surface
    Long time scale: 10-30 years to manifest; irreversible once started
  RAAC (Reinforced Autoclaved Aerated Concrete): UK problem 2023
    Brittle failure without warning; 100+ UK school buildings closed suddenly
    Design life ~30 years; buildings now 50-60 years old
```

---

## Natural Hazard Failures

### Earthquake and Liquefaction

```
SEISMIC INFRASTRUCTURE FAILURE MODES
======================================

GROUND SHAKING:
  Bridges: inadequate seating length (spans fall off bearings); column shear failure
  Pipelines: wave propagation damage at bends, joints, transitions
  Buildings: soft-story collapse; unreinforced masonry

LIQUEFACTION:
  Mechanism: saturated loose sand + shaking -> pore pressure increase -> soil loses strength
  Behaves like liquid: bearing capacity essentially zero
  Results: buildings tilt/sink, buried pipes float up, bridges settle
  Geographic risk: river deltas, reclaimed land, coastal areas
    Christchurch NZ (2011): extensive liquefaction damage to entire neighborhoods
    Kobe (1995): port area on reclaimed land: massive liquefaction

  Mitigation: densification (vibroflotation, dynamic compaction), drainage, deep foundations

LANDSLIDE AND ROCKFALL:
  Triggered by: earthquake, heavy rain, saturation
  Infrastructure at risk: mountain roads, railways, pipelines, powerlines
  Washington state SR 530 (Oso mudslide, 2014): 43 deaths, US 2 highway buried

CHEMICAL PLANT EARTHQUAKE:
  Puerto Rico (2020): multiple earthquakes + power outages -> chemical plant issues
  Texas (2021): winter storm + power outages -> chemical plant cooling failures
  Harvey (2017): Arkema chemical plant: loss of refrigeration + flooding
    -> peroxide decomposition -> fire -> toxic fumes (key: power + flooding = chemical cascade)
```

### Hurricane Harvey: Cross-Sector Case Study

```
HURRICANE HARVEY (August-September 2017)
==========================================

DIRECTLY OBSERVED CROSS-SECTOR CASCADE:

1. FLOODING (primary hazard):
   51" of rain over Houston metro (largest US rain event on record)
   Addicks and Barker reservoirs: EXCEEDED CAPACITY (by design, to prevent worse flooding)
   Controlled release: flooded 3,000+ homes
   Uncontrolled release risk: dam failure would flood 60,000+ homes

2. POWER OUTAGES:
   ~30,000 customers without power at peak (relatively limited due to wind)
   Power outages disabled: gas stations (no pump power), ATMs, stores

3. WASTEWATER:
   Houston MUD: 45+ water/wastewater systems compromised
   Storm inundation of wastewater lift stations -> sewage overflow
   Bayou Buffalo Bayou, Brays Bayou: E. coli counts 135x safe limit

4. CHEMICAL PLANTS (Arkema Crosby):
   Plant in 100-year floodplain (designed for 100-yr flood)
   Harvey: exceeded 500-yr flood threshold
   Loss of primary + backup power for refrigeration
   Organic peroxides (unstable without cooling): decomposed -> fire
   Sheriff deputy hospitalized from vapor exposure during firefighting attempt
   Lesson: design basis flood exceeded; chemical consequence unanticipated

5. HEALTH SYSTEM:
   Multiple hospitals flooded (some built in floodplain without elevation)
   Patient evacuation mid-storm -> dangerous transfers
   Medication access: pharmacy chain access disrupted for 1M+ patients

TOTAL COST: $125B (second only to Katrina)
KEY LESSON: Design basis flood (100-year) is increasingly being exceeded
  Climate change: Harvey-level events more frequent
  Floodplain maps: based on historical data, increasingly inaccurate
```

---

## Cyber Failure Modes

### ICS/SCADA Vulnerabilities

```
INDUSTRIAL CONTROL SYSTEM ATTACK SURFACE
==========================================

ASSET LAYER:
  RTUs (Remote Terminal Units): field data acquisition, remote control
    Often decades old; no authentication; no encryption
    Modbus, DNP3 protocols: designed for reliability, not security

  PLCs (Programmable Logic Controllers): direct control of equipment
    Siemens S7, Allen-Bradley, GE: targeted by Stuxnet
    Running custom ladder logic; firmware rarely updated

  HMIs (Human-Machine Interfaces): operator consoles
    Windows-based in modern systems; sometimes internet-accessible
    Vulnerable to: phishing (operator accounts), remote desktop exploits

COMMUNICATION LAYER:
  Modbus/TCP: no authentication, plaintext; ~30% of ICS protocols
  DNP3: designed for reliability; authentication added only in 2012 (DNP3-SA)
  IEC 61850: substation automation; GOOSE messages on LAN (fast, no auth)
  OPC DA/UA: Windows-based; OPC UA has security, legacy OPC DA does not
  ProfiNET, Ethernet/IP: factory automation; network segmentation critical

NETWORK LAYER:
  Historical design: isolated OT network ("air gap")
  Current reality: IT/OT convergence eroded air gaps
  Entry points:
    Remote access: vendor VPN for maintenance (Colonial Pipeline attack vector)
    Engineering workstations: connected to both IT and OT networks
    Historian server: data aggregation connects OT to enterprise network
    USB ports: Stuxnet entered via infected USB drives in Iran
    Cellular modems: remote RTUs sometimes have cellular backup (internet-exposed)

SHODAN STATISTICS (2025):
  ~50,000+ internet-exposed ICS devices found by Shodan search engine
  Including: water treatment PLCs, substation HMIs, building automation
  Many running Modbus, DNP3, Telnet (no authentication)
  These are accessible to anyone with a browser and Shodan account
```

### Stuxnet: The Canonical ICS Attack

```
STUXNET TECHNICAL ANALYSIS (Langner, Symantec 2010 analyses)
=============================================================

TARGET: Natanz uranium enrichment facility, Iran
         ~1,000 Siemens S7-315 PLCs controlling centrifuge cascades

DELIVERY:
  Windows zero-days (4 simultaneously -- unprecedented)
  Spread via: infected USB drives, Windows network shares, Step 7 project files
  Payload: install silently, spread to adjacent systems

DETECTION EVASION:
  Rootkit: hid itself from Windows; hid modified PLC code from Step 7
  Waited for specific PLC configuration (Siemens S7-315 + S7-417 combination)
  Only activated at specific centrifuge count and speed range

ATTACK PAYLOAD:
  Target: Centrifuge motor frequency (Fararo Paya / Vacon variable-frequency drives)
  Normal operating frequency: 1000-1064 Hz
  Attack sequence:
    1. For ~13 days: record normal centrifuge operation
    2. Phase 1: over 15 minutes, speed up rotors to 1410 Hz (overstress)
    3. Return to normal
    4. Wait 27 days
    5. Phase 2: slow rotors to 2 Hz for 50 minutes (mechanical stress from resonance)
    6. Return to normal
    7. Repeat
  Result: centrifuges failed at 5-10x normal rate; operators saw no anomaly on HMI
    (Stuxnet sent fake "normal" readings to HMI while manipulating hardware)

SIGNIFICANCE:
  First confirmed weapon-grade malware targeting physical infrastructure
  Demonstrated: nation-state can destroy physical equipment through software
  Designed to be stealthy (Iran took months to detect problem)
  Changed ICS security posture globally
  ICS-CERT (US) created as direct response
  NERC CIP mandatory cybersecurity standards strengthened post-Stuxnet
```

### Colonial Pipeline (2021) -- OT Perspective

Covered in 02-INTERDEPENDENCY.md. Key point: IT ransomware -> self-imposed OT shutdown.
The lesson for ICS security: even without direct OT compromise, IT compromise can force
operational shutdown of physical infrastructure.

---

## Systemic Failure: Deferred Maintenance

```
DEFERRED MAINTENANCE DYNAMICS
================================

DEFINITION:
  Deferred maintenance: maintenance known to be needed but postponed
  Not negligence necessarily: constrained budgets, competing priorities
  BUT: accumulated deferred maintenance = "unfunded liability"

MECHANISM:
  Year 1: $100k maintenance needed, only $60k budgeted -> $40k deferred
  Year 2: $100k new + $40k deferred carry-forward -> $140k needed, $60k budgeted
  Year 5: ~$240k deferred backlog; asset now in "poor" condition
  Year 8: Asset fails: $500k emergency repair + 4-week outage + $2M economic impact
  NPV analysis shows: the $40k/yr savings was not worth $2.5M+ eventual cost

DEFERRED MAINTENANCE RATIOS:
  Universities: 2:1 to 10:1 (deferred backlog vs. annual maintenance budget)
    Many campuses have $500M+ deferred maintenance backlog
  Transit agencies: NYC MTA: ~$40B capital backlog (2024)
  Hospitals: ~$200B national estimate
  Federal buildings: ~$25B federal real property deferred maintenance
  Highway bridges: ~$125B (FHWA estimate)

POLITICAL ECONOMY OF DEFERRAL:
  Budget pressure: operations (nurses, police, teachers) more visible than maintenance
  Politician incentive: ribbon cuttings for new projects > maintenance of old
  Asset ownership diffuse: no single actor has clear responsibility for condition
  Time horizon mismatch: 3-year budget cycles vs. 50-year asset life
  "Infrastructure is invisible until it fails": no constituency for maintenance

CONDITION-BASED MAINTENANCE (the fix):
  Move from calendar-based to condition-based scheduling
  Sensor monitoring + predictive models -> maintain when needed, not on schedule
  Avoids both: premature maintenance (cost waste) and deferred maintenance (failure risk)
  Infrastructure example: bridge health monitoring (SHM) -> extend inspection interval for
    well-monitored bridges, reduce interval for deteriorating ones
```

---

## Failure Statistics

```
INFRASTRUCTURE FAILURE STATISTICS (US, PHMSA/NTSB/ASCE DATA)
===============================================================

Natural gas pipeline incidents (PHMSA, avg 2019-2024):
  ~100-120 significant incidents/year
  ~10-15 fatalities/year
  Leading causes: excavation damage (811 violations), corrosion, incorrect operations
  Pipeline safety investment: ~$15B/yr (driven by incident response)

Bridge failures:
  ~100-200 bridge collapses/year (mostly small bridges, rural)
  Structural deficiency: 43,000 bridges rated structurally deficient (2024)
  Notable: FIU pedestrian bridge (2018): construction error -> 6 deaths
           I-5 bridge (Skagit, WA 2013): oversized truck + design vulnerability
           Fern Hollow (Pittsburgh, 2022): corrosion + deferred maintenance -> collapse

Water main breaks:
  ~250,000 water main breaks/year (US)
  ~6 billion gallons/day water lost to leaks (14-18% of treated water)
  Leading cause: age, cast iron (pre-1950 mains), corrosion
  Replacement rate needed: ~1%/year; actual rate: ~0.4%/year (under-investing)

Power outages:
  All causes: ~1,300 major outages/year (NERC DOE-417 reports)
  Weather-caused: ~65% of all outage events
  Non-weather: equipment failure (20%), human error (10%), cyber (rare but growing)
  Average US customer: 5-8 hours/year without power (SAIDI)
```

---

## Decision Cheat Sheet

| Failure mode | Primary mitigation |
|--------------|-------------------|
| Corrosion in buried pipelines | Cathodic protection + coating + inline inspection |
| Bridge rebar corrosion | Epoxy-coated rebar, stainless steel, fiber reinforced polymer |
| Metal fatigue | Regular NDE inspection (ultrasonic, eddy current), fatigue-resistant details |
| Earthquake bridge collapse | Column seismic retrofit (jacketing), seat expansion, isolation bearings |
| Liquefaction | Densification, drainage, deep foundations, avoidance |
| Chemical plant flooding | Elevate critical equipment, berm design, consequence analysis for extreme events |
| ICS cyber attack | Network segmentation, strong authentication, patch management, monitoring |
| Deferred maintenance cascade | Condition-based programs, asset management system, lifecycle cost budgeting |

---

## Common Confusion Points

**"Corrosion is just rust -- manageable."** Corrosion costs 3% of GDP annually and is
responsible for more infrastructure failures than any other single cause. Pipeline
explosions, bridge collapses, and water main breaks are frequently corrosion-initiated.
The catastrophic failure is preceded by years of invisible material loss.

**"Stuxnet was an anomaly -- nation-state level attack."** It demonstrated the concept
and raised awareness. Subsequent attacks (CRASHOVERRIDE/Industroyer 2016 Ukraine power
grid; TRITON/TRISIS 2017 Saudi petrochemical) used Stuxnet-like approaches with
different tools. The attack pattern is now in the criminal and state-sponsored toolkit,
not just the most sophisticated nation-states.

**"Structural failures happen suddenly without warning."** Most failures have warning
signs that were either not monitored or not acted upon. The FIU bridge showed cracks
before collapse (they were noted in an internal call the morning of collapse and deemed
"not urgent"). Fern Hollow had poor condition ratings for years. The "sudden" failure
is usually the final stage of visible-but-ignored deterioration.
