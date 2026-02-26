# Infrastructure Lifecycle Management: Asset Management, Condition Assessment, Capital Planning

## The Big Picture

Lifecycle management is the discipline of systematically knowing what you own,
knowing its condition, understanding its risk profile, and making rational investment
decisions over the asset's full life -- not just at construction. ISO 55000 (asset management)
and structural health monitoring are the technical foundations.

```
ASSET MANAGEMENT FRAMEWORK (ISO 55000)
=========================================

     ORGANIZATIONAL STRATEGIC PLAN
               |
     ASSET MANAGEMENT POLICY & OBJECTIVES
               |
     ASSET MANAGEMENT STRATEGY (SAMP)
               |
     +----------+----------+
     |                     |
  ASSET MANAGEMENT     ASSET MANAGEMENT
  PLANS (actions)      SYSTEM (processes)
     |                     |
     v                     v
  IMPLEMENT        MONITOR & REVIEW
  (create, operate, (performance, risk,
   maintain, dispose) condition, cost)
               |
          CONTINUAL IMPROVEMENT
          (update plans, standards, tools)

ISO 55000 CORE CONCEPTS:
  Asset register: inventory of all assets with attributes
  Asset criticality: consequence of failure for each asset
  Condition: current physical state
  Risk: probability of failure x consequence
  Capital plan: prioritized investment based on risk
  Life-cycle cost: total cost from creation to disposal
```

---

## Asset Inventory and Register

```
ASSET REGISTER REQUIREMENTS
==============================

MINIMUM ATTRIBUTES (per asset):
  Identifier (unique ID)
  Location (GIS coordinates preferred)
  Type / classification
  Installation date / estimated age
  Design specifications (load rating, capacity, material)
  Maintenance history (what was done, when)
  Inspection history (condition records)
  Condition score (current)
  Estimated remaining useful life (RUL)
  Replacement value ($)

POWER UTILITY ASSET REGISTER (typical):
  Transmission lines: each structure (pole/tower), each conductor segment
  Substations: each transformer, breaker, disconnect, bus
  Distribution: each feeder section, transformer, switch
  ~1-10 million individual assets for a large utility (PSEG, PEPCO, etc.)

WATER UTILITY ASSET REGISTER:
  Each pipe segment (material, diameter, installation year, length)
  Each pump, valve, meter, treatment unit
  ~100,000-1,000,000 assets for major city water system

GIS INTEGRATION:
  Modern asset management: GIS (Geographic Information System) linked to asset register
  Spatial analysis: which assets are in floodplain? near fault? near road intersection?
  Work order routing: technician finds nearest asset in the field
  Network analysis: which assets, if failed, isolate largest customer population?

ASSET REGISTRY CHALLENGES:
  Legacy paper records: many agencies have assets with no digital record
  Inaccurate records: installed dates wrong, specifications missing
  Underground infrastructure: locations inaccurate (utility conflict = contractor strikes pipe)
    US 811 "call before you dig": ~$1B/year in infrastructure strikes despite system
    ≥50% of underground utility drawings are inaccurate by more than 50 cm
```

---

## Condition Assessment Methods

```
CONDITION ASSESSMENT HIERARCHY
================================

LEVEL 1: VISUAL INSPECTION
  Lowest cost, most subjective
  Bridge sufficiency rating (FHWA): inspector rates elements 0-9
  Road condition (PASER): 1-10 visual scale
  Water main: external inspection of exposed sections; corrosion coupon analysis
  Typical interval: 2 years for bridges (NBIS mandate); annual for roads
  Limitation: only surface visible; misses internal/subsurface defects

LEVEL 2: NON-DESTRUCTIVE EVALUATION (NDE/NDT)
  Detects internal defects without destroying the component

  ULTRASONIC TESTING (UT):
    High-frequency sound waves (MHz range) propagate through material
    Reflect off defects, interfaces -> time-of-flight = distance to defect
    Used for: pipe wall thickness measurement, weld inspection, fatigue crack detection
    Inline inspection tool ("smart pig"): UT based, travels inside pipeline
    Resolution: detect wall loss to 1-2% of wall thickness

  MAGNETIC FLUX LEAKAGE (MFL):
    Magnetize pipe wall; flux "leaks" at metal loss (corrosion, pitting)
    Industry standard for oil/gas pipeline inspection
    Speed: 1-5 m/s through pipeline; 10-50 km/day throughput
    Cannot detect: SCC, hydrogen-induced cracking (requires UT or EMAT)

  GROUND-PENETRATING RADAR (GPR):
    Electromagnetic pulses (0.1-2 GHz) penetrate ground/concrete
    Reflect off rebars, voids, utilities, moisture zones
    Used for: concrete delamination, buried utility location, void detection
    Limitation: limited depth in clay soils (<1 m); resolution decreases with depth

  EDDY CURRENT TESTING (ECT):
    Induced eddy currents in conductor; defects change impedance
    Used for: surface/near-surface cracks in metals
    Rail inspection: eddy current instruments at 100+ km/hr on track vehicles

  ACOUSTIC EMISSION (AE):
    Active cracks emit stress waves (AE events)
    Sensors detect AE events: locate active crack growth
    Used for: pressure vessel monitoring, bridge wire monitoring, pipeline monitoring
    Advantage: continuous monitoring, detects active damage

  INFRARED THERMOGRAPHY:
    Thermal camera detects temperature differences
    Delamination in concrete bridge deck: warms differently in sun
    Moisture in building envelope: wet insulation has different thermal signature
    Electrical connection failure: high resistance -> hot spot

LEVEL 3: STRUCTURAL HEALTH MONITORING (SHM)
  Continuous sensor networks embedded in or attached to structure

  STRAIN GAUGES:
    Measure strain at specific points (fiber optic: FBGS cover continuous profiles)
    Bridge load monitoring: detect overloads, track degradation patterns
    Cost: $10,000-$500,000 per bridge depending on sensor count

  ACCELEROMETERS (SEISMIC / VIBRATION):
    Measure structural response to vibration
    Modal analysis: natural frequencies shift as structure stiffness changes
    Example: Golden Gate Bridge vibration monitoring -> wind-induced oscillation tracking
    Alert if natural frequency drops >5% (indicates structural change)

  FIBER OPTIC SENSORS (FBG - Fiber Bragg Grating):
    Optical fiber with periodic refractive index changes
    Strain or temperature changes -> wavelength shift of reflected light
    Can multiplex 100s of sensors on single fiber cable
    Immune to EMI; works in harsh environments (underwater, in concrete)
    Distributed sensing: BOTDR/BOTDA measure temperature/strain along entire fiber length

  WIRELESS SENSOR NETWORKS:
    Battery/solar-powered nodes, wireless transmission
    LoRaWAN or cellular backbone
    Reduces installation cost vs. wired (no cable trenching)
    Battery life: 2-10 years depending on sampling frequency
    Used for: slope stability monitoring, pipe vibration, equipment condition

REMOTE SENSING:
  SATELLITE InSAR (Interferometric Synthetic Aperture Radar):
    Measure millimeter-scale ground deformation from satellite orbit
    Sentinel-1, TerraSAR-X: repeat cycle 6-12 days
    Applications: subsidence monitoring (oil/gas fields, mining, groundwater pumping)
               pipeline right-of-way movement detection
               dam foundation deformation monitoring
    Resolution: 3-5 mm deformation over large area (km scale)
    Cost: $50-500 per km^2 for processed imagery

  LiDAR:
    3D point cloud of infrastructure surface
    Airborne LiDAR: bridge, road, levee surface mapping
    Mobile LiDAR: rail inspection from moving train (40 km/hr, 3mm accuracy)
    Change detection: compare scans over time -> identify movement, erosion
```

---

## Capital Planning Models

### Risk-Based Prioritization

```
RISK-BASED CAPITAL PLANNING
==============================

RISK MATRIX:
            CONSEQUENCE
            Low     Medium    High    Catastrophic
PROB-  Low  | 1      2         3         4
ABIL-  Med  | 2      4         6         8
ITY    High | 3      6         9        12
       V.Hi | 4      8        12        16

Investment priority = Risk score (higher = more urgent)

For infrastructure:
  Probability = f(age, condition, failure history, stress level)
  Consequence = f(asset criticality, redundancy available, population served)

EXAMPLE (water main prioritization):
  Asset A: 1960s cast iron, poor condition (8/100), serves 10,000 customers, no backup
    Probability: HIGH (4); Consequence: HIGH (8); Risk: 32 -- top priority
  Asset B: 2005 ductile iron, good condition (75/100), serves 500 customers, backup exists
    Probability: LOW (1); Consequence: LOW (2); Risk: 2 -- low priority

OPTIMIZATION MODELS:
  Markov chain models: asset condition transitions probabilistically over time
    State i (condition 1-5) -> transition matrix -> probability of next-period state
    Condition decline rate: function of age, material, environment, maintenance
  Lifecycle cost optimization:
    NPV(replace now) vs. NPV(replace later + probability of failures)
    Optimal replacement at point where NPV(defer) > NPV(replace now)

WORST-FIRST vs. RISK-BASED:
  Worst-first: replace most deteriorated assets first (simple, intuitive)
    Problem: ignores consequence -- worst condition on low-consequence asset ranks above
    moderate condition on high-consequence asset
  Risk-based: multiply probability by consequence -> correct prioritization
    Challenge: requires good data on consequences (often poorly quantified)
    Solution: criticality matrix, customer impact analysis
```

---

## Infrastructure Asset Depreciation

```
DEPRECIATION AND USEFUL LIFE
===============================

ACCOUNTING DEPRECIATION (vs. PHYSICAL DEPRECIATION):
  Accounting: straight-line, MACRS, units-of-production (tax/accounting purposes)
  Physical: actual material degradation (doesn't follow straight line)

INFRASTRUCTURE DEPRECIATION SCHEDULES (IRS/GASB):
  Bridges:          40-50 years (typical)
  Roads:            10-25 years
  Sewer mains:      40-80 years (ductile iron, concrete)
  Water mains:      40-80 years
  Electric utility: 20-40 years (distribution); 40-60 years (transmission)
  Buildings:        25-50 years
  Tunnels:          50+ years (concrete tunnel; longer with maintenance)

PHYSICAL USEFUL LIFE (actual):
  Concrete bridge: 50-100+ years with maintenance
  Cast iron pipe: 50-120 years (some still operating at 150 years in Boston)
  Asphalt pavement: 15-25 years surface course; 40-50 years structural base
  Transformer: 35-40 years (winding insulation life-limiting)
  Transmission tower: 50-80 years

  GAP: Accounting life < Physical useful life means:
    Fully depreciated assets that are still functional (underfunded replacement accounts)
    Assets "carrying" zero book value but with significant deferred maintenance needs

REPLACEMENT RESERVE FUNDING:
  Best practice: set aside annual "depreciation equivalent" for future replacement
  Many public utilities: don't fund reserves; rely on future debt/grants
  Result: when replacement needed, capital shock (borrow or defer)
  Private utilities (rate-regulated): depreciation component in rates -> forced reserve
  Municipal utilities: no such requirement; political pressure to keep rates low
    -> systematic under-funding of long-term capital needs
```

---

## Decision Cheat Sheet

| Asset management question | Answer |
|--------------------------|--------|
| Where to start with asset inventory? | GIS-linked database; import existing paper records first |
| Best condition assessment for pipelines | Inline inspection (smart pig): MFL + UT combination |
| Best condition assessment for bridges | Visual + NDE (GPR for deck, UT for welds) + SHM for high-value |
| How to prioritize limited budget | Risk-based: (probability x consequence), not worst-first |
| What is ISO 55000? | Asset management standard: strategy, plans, risk, performance metrics |
| What degrades condition assessment usefulness? | Inaccurate asset records, no historical baseline to compare |
| When to replace vs. repair? | Lifecycle cost analysis: NPV(replace now) vs. NPV(repair + future failure risk) |

---

## Common Confusion Points

**"Condition rating (0-9) is objective."** Bridge condition ratings involve significant
inspector judgment. Two inspectors can give the same element different ratings. AASHTO
training improves consistency, but subjective elements remain. Ratings are useful for
trending and relative comparisons, less useful for precise engineering decisions.
Supplement with NDE for critical decisions.

**"Monitoring system tells you when something is about to fail."** Current SHM systems
detect developing damage and long-term trends. Predicting exact failure time with high
confidence is difficult -- damage models have significant uncertainty. SHM is better
framed as "continuous risk assessment" than "failure prediction." Alert thresholds are
set conservatively to allow intervention before failure.

**"Most infrastructure has good asset data."** Most doesn't. AWWA (American Water Works
Association) surveys find ~50% of water utilities have asset data "mostly complete" or
better. The other 50% have partial or poor data. Transportation: many states have good
bridge databases (FHWA requirement) but poor data on culverts, retaining walls, and
structures below bridge inventory threshold. Energy: generation assets well-documented;
distribution less so.
