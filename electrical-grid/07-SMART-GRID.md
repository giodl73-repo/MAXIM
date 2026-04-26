# Electrical Grid — Smart Grid and DERs
## SCADA, AMI, Demand Response, Virtual Power Plants, Microgrids

---

## The Big Picture: Intelligence Layered on the Physical Grid

```
SMART GRID STACK:

APPLICATION LAYER:
  Market systems, optimization, forecasting, DER aggregation, customer apps

ANALYTICS & CONTROL LAYER:
  EMS (Energy Management System) — transmission
  ADMS (Advanced Distribution Management System) — distribution
  DER Management System (DERMS)
  Virtual Power Plant (VPP) platforms

COMMUNICATION LAYER:
  SCADA communications (DNP3, IEC 61850, IEC 60870)
  AMI communications (mesh RF, PLC, cellular)
  PMU data streams (GPS-synchronized, 30-120 samples/sec)
  Field devices: RTUs, IEDs, smart meters, sensors

SENSING & ACTUATION LAYER:
  CTs, PTs (current/potential transformers)
  RTUs (remote terminal units) at substations
  PMUs (phasor measurement units)
  Smart meters (AMI endpoints)
  Automated switches (reclosers, tie switches)
  DER inverter controllers (rooftop solar, batteries)

PHYSICAL INFRASTRUCTURE:
  Generation, transmission, distribution, loads
  (covered in 01–04)

DISTRIBUTED SYSTEMS ANALOGY:
  Physical infrastructure = data plane
  Protection relays = kernel (fast, deterministic)
  SCADA/EMS = control plane
  Markets/optimization = management plane
  AMI/DERs = edge computing endpoints
```

---

## SCADA: The Original Real-Time Control System

### Architecture

SCADA (Supervisory Control and Data Acquisition) has operated the grid since the 1960s. Modern SCADA systems are sophisticated distributed real-time systems, but the core architecture is unchanged:

```
SCADA ARCHITECTURE (transmission):

  FIELD DEVICES                  COMMUNICATION           MASTER STATION
  ─────────────────────────────────────────────────────────────────────
  CTs, PTs → Analog              Dedicated fiber         EMS Master Station
  Status contacts → Digital      SONET/SDH optical         │
  Control points ← Commands      networks (reliable,        ├─ State Estimation
                                  low latency)              ├─ Security Analysis
              RTU (Remote         OR:                       ├─ Economic Dispatch
              Terminal Unit)      Leased telecom lines      ├─ AGC Control
              at each substation  Frame relay (legacy)      ├─ Load Forecasting
              polls field         Microwave radio           ├─ Generation Scheduling
              devices every       (some rural)              ├─ Operator Interface
              2-4 seconds         OR:                       └─ Historical data
              sends reports       IP/MPLS networks
              to master           (modern, some CIP concerns)

SCAN RATE: 4 seconds (traditional SCADA)
  Each RTU polled every 4s → 15 data points per minute per RTU
  A utility with 2,000 RTUs: ~30,000 points updated per minute
  Compare to PMU: 30-120 samples/sec (7,500× more frequent)
```

### EMS Functions

The Energy Management System is the control plane for transmission grid operations — the same three-layer architecture as building management systems or datacenter BMS (field sensors -> controllers -> supervisory optimization), with MW dispatch signals replacing chilled-water setpoints:

```
EMS FUNCTIONAL STACK:

REAL-TIME OPERATIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  State Estimation: Compute full system V, I, P, Q from          │
  │  subset of measurements (some RTUs fail; some values estimated) │
  │  Result: real-time "power flow snapshot" of entire grid         │
  │  Run: every 30-60 seconds                                       │
  ├─────────────────────────────────────────────────────────────────┤
  │  Contingency Analysis (N-1 Security): Simulate each element    │
  │  tripping; check if system remains stable for all N-1 events   │
  │  Run: every 5-10 minutes; flags violations for operator        │
  ├─────────────────────────────────────────────────────────────────┤
  │  AGC (Automatic Generation Control): Regulate frequency         │
  │  Send regulating signals to participating generators every 4s   │
  │  Balances ACE (Area Control Error) to zero                      │
  ├─────────────────────────────────────────────────────────────────┤
  │  Economic Dispatch: Minimize fuel cost while meeting load      │
  │  Re-dispatch every 5-15 minutes as load changes               │
  └─────────────────────────────────────────────────────────────────┘

PLANNING (lookahead):
  Load forecasting: 1h, 4h, 24h, 7-day ahead predictions
  Unit commitment: which generators to start/stop for next day
  Transmission security assessment: outage scheduling
```

### From SCADA to IEC 61850: The Digital Substation Revolution

Traditional substations: analog instruments → hardwired copper cables → relay panels → RTU.
Modern substations: digital IEDs (Intelligent Electronic Devices) → Ethernet → process bus.

```
IEC 61850 COMMUNICATION ARCHITECTURE:

Traditional (analog):                 IEC 61850 (digital):
  CT → 5A hardwired → relay           CT → Merging Unit (digitizes at CT)
  PT → 115V hardwired → relay            → Sampled Value (SV) stream over Ethernet
  Relay → hardwire → breaker          Relay IED → GOOSE message → breaker IED
  Binary signals: 30-100 copper        Binary signals: < 4ms GOOSE over LAN
  cables per protection panel          One fiber cable per IED

KEY PROTOCOL CLASSES:
  GOOSE (Generic Object Oriented Substation Event):
    Priority: deterministic, < 4ms end-to-end
    Use: protection trip signals, status exchange, interlock logic
    Transmission: multicast UDP/IP with priority 7 (IEEE 802.1Q)
    Retry: continuous retransmission until change-of-state (no ACK needed;
           confidence from retransmit)

  Sampled Values (SV):
    High-speed digitized V and I measurements
    96-256 samples/cycle (5,760-15,360 samples/second at 60 Hz)
    Replaces analog wiring from CTs/PTs to protection relays

  MMS (Manufacturing Message Specification):
    SCADA communications, slower, TCP/IP
    Setting changes, report control, files

BENEFITS:
  ✓ Faster protection: GOOSE trips in < 4ms vs hardwired ~2ms (marginal,
    but GOOSE enables complex logic)
  ✓ Interoperability: IEDs from different vendors communicate via standard protocol
  ✓ Commissioning: no hardwiring = faster, fewer errors
  ✓ Monitoring: continuous monitoring of relay health, performance
  CONCERN: IT/OT convergence → cybersecurity attack surface expands
```

---

## PMUs: Wide-Area Situational Awareness

Phasor Measurement Units (PMUs) are GPS-synchronized instruments that measure voltage and current phasors at 30-120 samples per second. This is 7,500× more frequent than traditional SCADA (4-second scans), enabling real-time observation of grid dynamics.

```
PMU MEASUREMENT AND SYNCHRONIZATION:

  GPS signal → timestamp precision ~1 μs (microsecond)
  PMU measures V and I, computes phasor (magnitude + phase angle)
  Phase angle: referenced to GPS-synchronized UTC → absolute phase
  (Traditional SCADA: relative phase unknown without synchrophasor)

  At any point in time, all PMUs report using the same time reference
  → Can compare phase angles at different locations across the interconnection
  → Observe power oscillations, voltage angles, inter-area mode behavior

SYNCHROPHASOR DATA:
  C37.118 standard: 30 or 120 frames/second
  Each frame: V magnitude, V phase angle, I magnitude, I phase angle, frequency, ROCOF
  Communications: typically IEEE C37.118 over TCP/IP to Phasor Data Concentrator (PDC)
  PDC: aligns and archives data from multiple PMUs

US PMU NETWORK:
  NASPI (North American SynchroPhasor Initiative)
  >3,000 PMUs installed on transmission grid
  NASPInet: real-time data sharing between utilities
  Eastern Interconnection wide-area PMU data shared across utilities

APPLICATIONS:
  Oscillation detection: observe inter-area oscillations developing
                        (seen as sinusoidal variation in phase angles)
  Voltage angle: large angle differences → potential transient stability limit approaching
  Event reconstruction: post-event analysis with high-fidelity data
  Dynamic line rating: infer actual line loading from electrical measurements
  Real-time model validation: compare PMU data to EMS state estimation
```

**The 2003 blackout counterfactual:** If wide-area PMU data had been available and shared in real time across utilities in 2003, the cascading deterioration in Ohio would have been visible. Voltage angles and power flows would have shown the system moving toward instability 30-60 minutes before the irreversible cascade. This is why NASPI and wide-area monitoring were prioritized post-2003.

---

## AMI: Advanced Metering Infrastructure

Traditional meters: electromechanical disk (Ferraris meter), read once monthly by meter reader walking the street. AMI: two-way communicating smart meter, reports 15-minute interval data, enables remote connect/disconnect.

```
AMI ECOSYSTEM:

  Customer Premises                   Utility
  ─────────────────────────────────────────────────────────────────────
  Smart meter              ←→    Communications    ←→  Meter Data
    • 15-min interval data          network              Management
    • Real-time voltage             (Mesh RF:            System (MDMS)
    • Outage detection              900 MHz/2.4 GHz)
    • Remote connect/disconnect     OR PLC (power
    • Tamper detection              line communication)
    • Home area network (HAN)       OR Cellular (4G/5G)
      port for IHDs, smart
      appliances, EV chargers
                                                        Billing system
                                                        OMS (Outage Mgmt)
                                                        DRM (Demand Response)
                                                        Analytics

AMR (Automated Meter Reading, legacy): one-way drive-by reading; still reads monthly
AMI: two-way; real-time or 15-min; enables time-of-use, demand response

US AMI DEPLOYMENT (2024):
  ~115 million smart meters installed (~75% of all residential meters)
  Largest deployments: Pacific Gas & Electric (10M), FPL (5M+), ComEd (4M+)

DATA GENERATED:
  15-min reads × 115M meters × 8,760 hours = ~1 trillion data points/year
  This is serious big data infrastructure — not trivial to store, process, analyze
  Major utilities use cloud (Azure, AWS) for AMI data processing
```

### What AMI Enables vs What AMR Enabled

| Capability | AMR | AMI |
|-----------|-----|-----|
| Billing data | Monthly read | 15-min interval (96 reads/day) |
| Outage detection | Customer calls | Automatic (last gasp signal) |
| Restoration verification | Crew visual | Automatic ping from meter |
| Voltage monitoring | None | Continuous at every meter |
| Remote connect/disconnect | Truck roll | Remote command |
| Theft detection | Manual investigation | Automated analysis |
| Time-of-use pricing | Not practical | Enabled |
| Demand response | Limited | Full (direct signal or pricing) |
| DER monitoring | None | Solar generation monitoring |
| EV managed charging | None | Scheduled charging programs |

**The outage management revolution:** Pre-AMI, a utility learned about outages when customers called. AMI meters send a "last gasp" signal at the moment of outage. The utility's outage management system automatically triangulates the fault location before the customer even calls. Crew dispatch is faster, and "lights on" verification (did the restoration actually reach the customer?) is instant.

---

## Demand Response: Load as a Resource

Demand response (DR) treats customer loads as dispatchable resources — pay customers to reduce consumption during peak periods, rather than building generation to meet those peaks.

```
DR CATEGORIES:

1. PRICE-RESPONSIVE (indirect control):
   Time-of-Use (TOU): different rates at different hours
     Peak: $0.30-0.50/kWh (2-8 PM summer weekdays)
     Off-peak: $0.08-0.12/kWh (nights, weekends)
     Customer shift discretionary loads → dishwasher, laundry, EV charging

   Real-Time Pricing (RTP): prices change every hour or 15 min
     Wholesale price pass-through → highly responsive large customers
     California CAISO exports real-time prices → some industrial customers
     respond automatically

2. INCENTIVE-BASED (direct control):
   Interruptible Rate: large industrial customers (steel mills, aluminum smelters)
     agree to curtail on utility request; receive reduced rates year-round
     Curtailment: hours/yr (predictable); advance notice: 30 min to 4 hours

   Direct Load Control (DLC): utility can cycle central AC, water heaters
     via radio signal or smart thermostat
     Residential programs: 15-min on/off cycling; 3-5°F setpoint bump
     Up to 5 kW per home × millions of homes = GW-scale

   Emergency DR: last resort during extreme events; very high compensation
     ISO-NE: up to $40,000/MWh for emergency load curtailment
```

### Demand Response Aggregators

Individual homes can't bid into wholesale markets (too small, too complex). Aggregators bundle thousands of small resources into a single dispatchable block:

```
AGGREGATION MODEL:

  Home 1: Smart thermostat (3 kW)  ─┐
  Home 2: Water heater (4.5 kW)    ─┤
  Home 3: EV charger (7.2 kW)      ─┤  Aggregator platform
  Home 4: Pool pump (1.5 kW)       ─┤  (Enel X, AutoGrid, OhmConnect)
  ...                               ─┤  Controls load via API/radio
  Home N: Battery storage (5 kW)   ─┘  Bids aggregate into ISO market

  1,000 homes × average 3 kW = 3 MW dispatchable DR resource
  ISO market minimum bid: 1 MW → aggregated homes qualify

  Revenue split: aggregator keeps 15-30%; homeowner gets rest
  Homeowner value: $50-200/year for minimal inconvenience

DEMAND FLEXIBILITY ROADMAP:
  2015: Simple DLC (AC cycling, limited penetration)
  2020: Smart thermostats, Nest/Ecobee, 15M+ deployed
  2024: EV managed charging (Ford Pro Intelligent Charge), V2G pilots
  2026+: Home batteries + EV charging + HVAC + appliances → full home energy management
```

---

## DERs: Distributed Energy Resources

DERs are any generation, storage, or load-flexibility resource located at or near the customer premises. The grid is inverting: traditionally power flowed one way (substation → customer); now it increasingly flows both ways.

```
DER LANDSCAPE:

GENERATION DERs:
  Rooftop solar PV:     8 kW average residential system
                        US: ~4 million residential systems, ~30 GW installed (2024)
  Small wind:           Rare residential (<10 kW); some rural
  Fuel cells:           BloomEnergy commercial systems (250 kW–5 MW)
  Small CHP:            Microturbines, engine CHP (commercial/industrial)

STORAGE DERs:
  Behind-the-meter BESS: Tesla Powerwall (13.5 kWh), LG Chem RESU
                         US: ~200,000 residential installations (2024, growing fast)
  EV batteries:         Nissan LEAF, Ford F-150 Lightning → Vehicle-to-Home (V2H)
                         Ford Lightning: 98 kWh; can power average home 3-10 days

FLEXIBLE LOAD DERs:
  Smart thermostats:    15 million+ (Nest, Ecobee); 3-4 kW flexibility
  EV chargers:          Level 2 (7.2 kW), DCFC (50-350 kW)
  Smart water heaters:  Demand response capable, 4.5 kW
  Pool pumps:           1-3 kW, variable speed, schedule-able
  Smart appliances:     Washer/dryer, dishwasher

TOTAL DER POTENTIAL (US):
  Installed solar: 170 GW (end of 2024)
  EV fleet (2030 projected): 30-50M vehicles × 7 kW L2 = 200-350 GW flexible load
  Home batteries (2030): 10-15 GW
  Total DER potential: 200-500 GW of flexible resources — comparable to current US peak!
```

### Virtual Power Plant (VPP)

Aggregate DERs and control them as a single dispatchable resource — a "virtual" power plant visible to the grid as if it were a conventional generator.

```
VPP ARCHITECTURE:

  1,000 homes × 10 kWh home battery = 10 MW × 10 MWh aggregate resource
  Controller receives: CAISO dispatch signal (e.g., "need 8 MW for 4 hours")
  → Platform sends API commands to each home battery inverter
  → Each battery discharges at ~8 kW
  → Aggregate: 1,000 × 8 kW = 8 MW to grid
  → Metered and settled at ISO market rates

VPP VALUE:
  For customers: earn $200-500/year passively
  For utilities: avoid $50-200M transmission/substation upgrades
  For ISO: defer peaker plant construction ($450/kW × 100 MW = $45M saved)
  For grid: distributed resource = resilient (no single point of failure)

KEY EXAMPLES:
  Sunrun (California): 108 MW VPP from home solar + batteries (2023)
  Green Mountain Power (Vermont): Tesla Powerwall VPP
  OhmConnect (Texas/California): 500 MW+ aggregated smart home DR
  Next Kraftwerke (Germany): 11+ GW aggregated DER VPP — world's largest
  Tesla Energy (Australia): VPP of Powerwalls for SA Govt

TECHNICAL REQUIREMENTS:
  Two-way communication: Internet to each home system
  API standards: IEEE 2030.5 (SEP 2.0), OpenADR 2.0
  Telemetry: 1-minute interval data from each device
  Latency: < 5 seconds for dispatch signal delivery
  Forecasting: next 4h load/generation forecast per device
  Aggregation math: real-time portfolio state estimation
```

---

## Microgrids: Islands of Resilience

A microgrid is a local energy system with: (1) distributed generation/storage, (2) controlled boundary (point of common coupling with main grid), (3) ability to operate in island mode (disconnected from main grid).

```
MICROGRID ARCHITECTURE:

     MAIN GRID
         │
   ┌─────┴──────────────────────────────────────────────────────┐
   │  POINT OF COMMON COUPLING (PCC)                            │
   │  Smart switch / static transfer switch                     │
   │  Normal: connected to main grid (import/export possible)   │
   │  Island: disconnected (self-sufficient operation)          │
   │                                                            │
   │  ┌────────────────────────────────────────────────────┐    │
   │  │           MICROGRID BOUNDARY                        │   │
   │  │                                                    │   │
   │  │  ┌──────────┐    ┌──────────┐    ┌─────────────┐  │   │
   │  │  │  Solar   │    │ Battery  │    │  Generator  │  │   │
   │  │  │  PV      │    │ Storage  │    │  (Diesel or │  │   │
   │  │  │ 500 kW   │    │  1 MWh   │    │  NatGas CHP)│  │   │
   │  │  └────┬─────┘    └────┬─────┘    └──────┬──────┘  │   │
   │  │       │               │                  │          │   │
   │  │       └───────────────┴──────────────────┘          │   │
   │  │                    LOCAL BUS                         │   │
   │  │                       │                              │   │
   │  │              ┌────────┴────────┐                    │   │
   │  │              │ Critical Loads  │                    │   │
   │  │              │ (hospital wing, │                    │   │
   │  │              │ command center, │                    │   │
   │  │              │ data center)    │                    │   │
   │  └────────────────────────────────────────────────────┘    │
   └───────────────────────────────────────────────────────────┘
```

### Microgrid Control Modes

```
GRID-CONNECTED MODE:
  Main grid sets V and f (grid reference)
  DERs inject power at set points (PQ mode — constant P and Q)
  Battery: arbitrage, demand charge reduction, ancillary services
  Solar: MPPT (maximum power point tracking)

ISLAND MODE (after intentional or forced disconnection):
  No external V/f reference → some DER must be grid-forming
  Grid-forming inverter (or diesel gen) establishes V and f
  Other DERs shift to load-following (VF mode — maintain voltage and freq)
  Battery: maintains V/f; absorbs/supplies imbalance
  Solar: curtails if excess; MPPT if deficit
  Critical load shedding: if generation insufficient, shed non-critical loads

TRANSITION (grid → island):
  Detect grid outage (V collapse, frequency deviation, anti-islanding)
  Open PCC switch in < 100ms
  Black-start local generation (or activate grid-forming battery)
  Stabilize local V and f
  Restore load
  Total transition: 50-200 ms for seamless transfer
                    2-30 seconds for non-seamless
```

### Microgrid Use Cases

| Application | Key DER | Storage | Critical Loads |
|------------|---------|---------|---------------|
| Military base | Solar + diesel gen | Li-ion | Command & control, communications |
| Hospital campus | CHP + solar | Li-ion | ICU, ORs, life safety systems |
| Island community | Wind + solar + diesel | Li-ion or flow | All community loads |
| University campus | Solar + CHP | BESS | Research labs, data centers |
| Data center | Solar + fuel cell | UPS + BESS | All IT loads |
| Remote telecom tower | Solar + diesel | Lead-acid/Li-ion | Telecom equipment |

---

## ADMS: Advanced Distribution Management System

The distribution-level equivalent of the EMS. Manages a distribution grid with thousands of automated switches, DERs, and sensors.

```
ADMS FUNCTIONAL STACK:

  ┌─────────────────────────────────────────────────────────────────┐
  │  OUTAGE MANAGEMENT SYSTEM (OMS)                                 │
  │  Fault detection (AMI last gasp), crew dispatch, ETR            │
  ├─────────────────────────────────────────────────────────────────┤
  │  FAULT DETECTION, ISOLATION, RESTORATION (FDIR)                │
  │  Automated switching to minimize outage impact (seconds)       │
  ├─────────────────────────────────────────────────────────────────┤
  │  VOLT/VAR OPTIMIZATION (VVO)                                    │
  │  Minimize losses + maintain voltage: coordinate OLTC,           │
  │  capacitor banks, DER reactive power, voltage regulators        │
  ├─────────────────────────────────────────────────────────────────┤
  │  DER MANAGEMENT (DERMS)                                        │
  │  Coordinate DER dispatch, curtailment, reactive support        │
  │  Prevent overvoltage from rooftop solar, manage exports        │
  ├─────────────────────────────────────────────────────────────────┤
  │  NETWORK TOPOLOGY ANALYSIS                                      │
  │  Real-time connectivity model from switch status                │
  │  Foundation for all above functions                             │
  └─────────────────────────────────────────────────────────────────┘
  Data: AMI meters, automated switches, sensors, SCADA
  Communications: SCADA, IEC 61968/61970 (CIM), DNP3
```

---

## NERC CIP: Cybersecurity Standards

IT/OT convergence has created serious attack surfaces. The grid was built on isolated, proprietary systems. Modern smart grid connects them to IP networks — and attackers.

```
KEY CYBER INCIDENTS:

Ukraine 2015 (BlackEnergy):
  Vector: Spear phishing → trojan on IT network → lateral movement to OT
  Technique: Compromised SCADA workstations; used legitimate HMI software
             to manually open breakers; custom KillDisk wiper to delay response
  Impact: 6 distribution companies, 225,000 customers, 3-6 hours

Ukraine 2016 (Industroyer/CrashOverride):
  Vector: More sophisticated — automated attack on protection relays
  Technique: Direct IEC 60870-5-101/104, IEC 61850 GOOSE replay attacks
             Opened circuit breakers via protocol commands
             Custom wiper, denial of service on serial-to-Ethernet converters
  Impact: Ukrenergo transmission company, 20% of Kiev dark for ~75 minutes
  Significance: First malware specifically designed to attack power grid protocols

Colonial Pipeline 2021:
  Vector: Compromised VPN credential (no MFA)
  Impact: IT systems only; but company shut OT (pipeline control) as precaution
  Impact: 5,500 miles of fuel pipeline shut, 6 days, eastern US fuel shortage
  Significance: IT incident → voluntary OT shutdown → massive real-world impact
```

### NERC CIP Standards

NERC CIP (Critical Infrastructure Protection) is the mandatory cybersecurity standard for bulk electric system components. Enforced by NERC; violations → fines up to $1M/day.

| Standard | Focus |
|----------|-------|
| CIP-002 | BES Cyber System Categorization (High/Medium/Low impact) |
| CIP-003 | Security Management Controls |
| CIP-004 | Personnel & Training |
| CIP-005 | Electronic Security Perimeters (network segmentation) |
| CIP-006 | Physical Security of BES Cyber Systems |
| CIP-007 | Systems Security Management (patching, port/service mgmt) |
| CIP-008 | Incident Reporting and Response |
| CIP-009 | Recovery Plans |
| CIP-010 | Configuration Management |
| CIP-011 | Information Protection |
| CIP-013 | Supply Chain Risk Management (added 2020) |

**CIP-013 (Supply Chain):** Requires utilities to manage cybersecurity risk in vendor supply chains. Triggered by concerns about Chinese-manufactured grid components (transformers, SCADA software) potentially containing backdoors. This is the grid-specific equivalent of the SBOM (Software Bill of Materials) movement in software.

**The air gap fallacy:** Many utilities historically relied on air-gapped OT networks. Modern smart grid makes true air-gaps impossible — AMI, DER management, remote SCADA access all require connectivity. Defense-in-depth, network segmentation, and ICS-specific monitoring (Claroty, Dragos, Nozomi) are the realistic alternatives.

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| What is SCADA? | Supervisory Control and Data Acquisition — real-time monitoring and control of grid equipment via RTUs at substations, 4-second scan rate |
| EMS vs ADMS? | EMS manages transmission (generation dispatch, stability analysis); ADMS manages distribution (feeders, DERs, outage management) |
| What does AMI enable that AMR doesn't? | Two-way communication, 15-min data, remote connect/disconnect, outage detection, demand response, time-of-use pricing |
| What is a VPP? | Virtual Power Plant — aggregated DERs (home batteries, EV chargers, thermostats) controlled as single dispatchable resource in wholesale market |
| What is a microgrid? | Local energy system with generation/storage and ability to island (operate disconnected from main grid) |
| What is FDIR? | Fault Detection, Isolation, Restoration — automated switching that isolates faulted feeder section and restores unfaulted customers in seconds |
| What did the Ukraine 2016 attack demonstrate? | Malware can directly attack protection relay protocols (IEC 61850 GOOSE, IEC 60870) — IT/OT convergence creates physical-consequence cyber risk |
| What is IEC 61850? | Substation communication standard — GOOSE (< 4ms protection messages), Sampled Values (digitized CT/PT outputs), MMS (SCADA communications) |
| What is Volt/VAR Optimization? | Coordinated control of voltage and reactive power across distribution feeder to minimize losses and maintain acceptable voltages |
| What does IEEE 1547-2018 require? | DERs must ride through voltage/frequency disturbances and provide grid support (reactive power, voltage regulation) — major update from 2003 |

---

## Common Confusion Points

**SCADA scan rate vs PMU rate:** Traditional SCADA scans each RTU every 4 seconds — this is fine for steady-state operations but too slow to observe sub-second dynamics. PMUs at 30-120 samples/sec provide the high-fidelity view needed for oscillation detection and dynamic security assessment. Both exist and serve different purposes in modern EMS.

**AMI is not just billing:** Many utilities justified AMI deployment primarily for billing efficiency (eliminate meter readers). The strategic value — demand response, outage management, DER integration, voltage monitoring — often wasn't fully planned. Now those secondary capabilities are the primary driver of smart grid ROI.

**VPP ≠ microgrid:** A VPP is a virtual aggregation — the resources are geographically dispersed (thousands of homes across a service territory). A microgrid is a physically local system that can island. A VPP might contribute to grid-wide frequency response; a microgrid provides local resilience. They're complementary architectures, not alternatives.

**DERMS scope:** "DER Management System" means different things to different vendors. At minimum: visibility and control of connected DERs (solar inverters, batteries). Full DERMS: economic optimization, market participation, reactive power dispatch, forecast-based pre-positioning. The industry is still standardizing on what DERMS must do.

**Grid-forming vs grid-following for microgrids:** A microgrid that wants to island MUST have at least one grid-forming source (diesel generator, grid-forming BESS, grid-forming inverter). A grid-following-only microgrid collapses when it disconnects from the main grid because there's no voltage/frequency reference for the inverters to lock to. This is a common design error in early microgrids.

---

*Next: 08-MARKETS.md — ISOs/RTOs, LMP pricing, day-ahead/real-time markets, capacity markets*
*See also: 05-GRID-STABILITY.md for PMU and wide-area monitoring in stability context*
*See also: 06-ENERGY-STORAGE.md for BESS revenue stacking in markets*
