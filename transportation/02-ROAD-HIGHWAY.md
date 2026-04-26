# Road and Highway Engineering

## The Big Picture

Roads are the default transportation infrastructure of the 20th and 21st centuries. Every other mode feeds into the road network at origin and destination. Understanding the engineering determines what roads can and cannot do — and why adding capacity often fails to solve congestion.

```
+------------------------------------------------------------------+
|                    ROAD SYSTEM LAYERS                            |
|                                                                  |
|  GEOMETRIC DESIGN                                                |
|  +-----------+  +-----------+  +-----------+  +-----------+      |
|  | Horizontal|  | Vertical  |  | Cross-    |  | Sight     |     |
|  | Alignment |  | Alignment |  | Section   |  | Distance  |     |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
   |                                                              |
   |  PAVEMENT STRUCTURE                                          |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
|  | Flexible  |  | Rigid     |  | Composite |  | Distress  |     |
|  | (Asphalt) |  | (Concrete)|  | (Overlay) |  | & Repair  |     |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
   |                                                              |
   |  TRAFFIC FLOW                                                |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
|  | Flow-     |  | LWR       |  | Level of  |  | Capacity  |     |
|  | Density   |  | Waves     |  | Service   |  | Analysis  |     |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
   |                                                              |
   |  INTELLIGENT TRANSPORTATION SYSTEMS                          |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
|  | Signal    |  | Freeway   |  | Connected |  | Traffic   |     |
|  | Control   |  | Mgmt      |  | Vehicles  |  | Data      |     |
|  +-----------+  +-----------+  +-----------+  +-----------+     |
+------------------------------------------------------------------+
```

---

## Highway Geometric Design

### Horizontal Alignment

The path of the road in plan view: tangent (straight) sections connected by curves.

```
  HORIZONTAL ALIGNMENT ELEMENTS:

  Tangent ----+                 +---- Tangent
              |                 |
              | Transition      |
              | Spiral          |
              |  (clothoid)     |
              +---[Circular]----+
                  Curve R

  Clothoid spiral: curvature increases linearly with distance.
  Reduces lateral jerk (rate of change of centripetal acceleration).
  Required for high-speed roads and railways.

  CIRCULAR CURVE GEOMETRY:
  R = radius of curvature (metres)
  D = degree of curve (old US convention, 1 degree = 100ft chord)
  PC = Point of Curvature (start)
  PT = Point of Tangency (end)
  PI = Point of Intersection (where tangents meet)

  SPEED vs MIN RADIUS (AASHTO, max 10% superelevation):

  Design Speed (km/h)  | 50  | 80  | 100 | 120 | 130
  Min Radius (m)       | 75  | 229 | 395 | 663 | 819
```

**Superelevation (banking):** The cross-slope applied in curves. Provides centripetal force partially from gravity instead of tire friction. Maximum superelevation: 8-12% depending on climate (ice risk) and context (urban intersections). Transition from normal crown to full superelevation happens over the spiral/transition section.

### Vertical Alignment

Profile in cross-section: grades (slopes) connected by parabolic curves.

```
  VERTICAL CURVE TYPES:

  Crest curve (hill):              Sag curve (valley):

       apex
      /     \                    ____
  ___/       \___                /    \____

  Controls: stopping sight        Controls: headlight sight
  distance over crest             distance in sag
  Comfort: lateral g force        Comfort: vertical g force
  at apex                        at bottom

  K-VALUE:
  K = L/A  where L = curve length, A = algebraic grade change (%)
  Higher K = gentler curve = better sight distance + comfort

  Design speed   Crest K    Sag K
  50 km/h           7        10
  80 km/h          29        30
  100 km/h         54        45
  120 km/h        100        61
```

### Sight Distance

The minimum distance a driver must be able to see ahead to make safe decisions.

```
  STOPPING SIGHT DISTANCE (SSD):
  SSD = reaction distance + braking distance
  SSD = v * t_r + v^2 / (2 * a)

  Where:
    v = design speed (m/s)
    t_r = perception-reaction time (AASHTO: 2.5 seconds)
    a = deceleration rate (AASHTO: 3.4 m/s^2 comfortable braking)

  Design speed   SSD (AASHTO minimum)
  50 km/h        65m
  80 km/h        130m
  100 km/h       185m
  120 km/h       250m

  PASSING SIGHT DISTANCE (PSD): much longer (480-670m at 80-100 km/h)
  Required for 2-lane 2-way roads to allow safe overtaking.
  Why 2-lane rural roads are dangerous: insufficient PSD zones.
```

### Interchange Types

Grade separation of intersecting highways. The choice of type balances cost, capacity, safety, and land area.

```
  INTERCHANGE COMPARISON:

  TRUMPET:              DIAMOND:              CLOVERLEAF:
  (T-intersection)      (most common)         (full interchange)
       |                    |   |                  / \
  -----+----           -----+---+-----        ---[   ]---
       |               ramps on each               |
  Loop ramp            quadrant              4 loop ramps
       |               Left turns via       All movements
  Lowest cost          signal at cross      possible, no
  One highway end      street               signals needed
                       Low cost but         Large footprint
                       signal delay         Weave problems

  SPUI (Single-Point Urban Interchange):
  All ramp traffic merges at a single signalized intersection.
  +--+--+
  |  X  |  <- All movements at one point
  +--+--+
  High capacity in small footprint. Popular in urban areas.
  Unusual geometry confuses infrequent users.

  DDI (Diverging Diamond Interchange):
  Traffic crosses to opposite side of road between ramps.
  Eliminates left-turn conflicts with freeway ramps.
  +--+--+
  | /  \|  <- Cross-over between ramps
  |X    X |
  +--+--+
  Becoming popular in US: 10-30% capacity improvement over diamond.
  Initially confusing; studies show drivers adapt within a few trips.
```

---

## Pavement Design

### Pavement Structure Basics

```
  FLEXIBLE (ASPHALT) PAVEMENT:      RIGID (CONCRETE) PAVEMENT:

  +------------------+              +------------------+
  | Surface course   | 40-75mm      | Concrete slab    | 200-300mm
  +------------------+              | (JPCP or CRCP)   |
  | Binder course    | 50-100mm     +------------------+
  +------------------+              | Subbase          | 100-200mm
  | Base course      | 100-200mm    +------------------+
  +------------------+              | Subgrade         |
  | Subbase          | 100-300mm    +------------------+
  +------------------+
  | Subgrade         |
  +------------------+

  Flexible: deflects under load,     Rigid: distributes load via
  load spread by layers.             beam/slab action.
  Fails by: fatigue cracking,        Fails by: joint faulting,
  rutting, roughness.                punchout, cracking.
  Cheaper to build, easier to        Lasts longer (30-40yr vs
  maintain incrementally.            20-30yr for flexible).
```

### AASHTO Flexible Pavement Design

The empirical 1993 AASHTO method is still widely used for design:

```
  STRUCTURAL NUMBER CONCEPT:

  SN = a1*D1 + a2*D2*m2 + a3*D3*m3

  Where:
    SN = structural number (reflects total structural capacity)
    a1, a2, a3 = layer coefficients (material strength)
    D1, D2, D3 = layer thicknesses (inches, old US convention)
    m2, m3 = drainage coefficients

  TYPICAL LAYER COEFFICIENTS:
  Asphalt concrete (dense grade): a1 = 0.44
  Crushed stone base: a2 = 0.14
  Granular subbase: a3 = 0.11

  DESIGN EQUATION:
  log(W18) = ZR*S0 + 9.36*log(SN+1) - 0.20
             + log(delta_PSI/(4.2-1.5)) / (0.40 + 1094/(SN+1)^5.19)
             + 2.32*log(MR) - 8.07

  Where:
    W18 = 18-kip ESALs (equivalent single axle loads) over design life
    ZR, S0 = reliability and standard deviation factors
    delta_PSI = performance loss acceptable
    MR = resilient modulus of subgrade (psi)

  KEY INSIGHT: ESAL concept
  Different axle loads produce different damage.
  Damage ~ (load/reference_load)^4  (fourth-power law)
  A 40-kip truck axle does 2^4 = 16x the damage of a 20-kip axle.
  Pavement is designed for total ESAL load over design life.
```

**Mechanistic-Empirical Pavement Design Guide (MEPDG):** The modern replacement for AASHTO 1993. Uses actual material properties, climate data, and traffic loading to predict distress mechanistically (calculate strains, predict cracking and rutting from those strains), calibrated to field performance. More complex but more accurate, especially for novel materials.

### Pavement Distress

| Distress Type | Description | Cause | Treatment |
|---------------|-------------|-------|-----------|
| **Fatigue cracking** | Alligator cracking pattern | Repeated flexural strain, insufficient structure | Full depth reclamation, reconstruction |
| **Rutting** | Longitudinal depressions in wheel paths | Plastic deformation of asphalt or subgrade | Mill and overlay, stiffer mix |
| **Roughness** | Irregular surface profile | Various — joints, settlements, patching | Measured by IRI (mm/m) |
| **Joint faulting** | Step at transverse joints (concrete) | Pumping of fines, differential settlement | Diamond grinding, full-depth repair |
| **Potholes** | Bowl-shaped holes | Water infiltration, freeze-thaw, fatigue | Patching (temporary), rehabilitation |

**IRI (International Roughness Index):** Standardized roughness measure in mm/m. Calculated by simulating a quarter-car model traversing the road profile.
- New highway: IRI < 1.0 m/km
- Good condition: IRI 1.0-2.5 m/km
- Fair condition: IRI 2.5-5.0 m/km
- Poor condition: IRI > 5.0 m/km (triggers rehabilitation)

---

## Traffic Flow Theory

Traffic flow theory applies fluid dynamics to vehicle streams. The mathematical structure is shared with queuing theory — the same tools used for analyzing server queues and network throughput.

### The Fundamental Relationship

```
  q = k * v

  q = flow (vehicles per hour)
  k = density (vehicles per km)
  v = space-mean speed (km/h)

  This is analogous to:
  Throughput = Utilization * Efficiency
  (in queuing/systems terms)

  THREE STATES OF TRAFFIC:

  FREE FLOW                  CAPACITY             CONGESTED
  (undersaturated)           (critical)           (oversaturated)

  v = free flow speed        v = optimal speed    v = near zero
  k = low density            k = critical density k = jam density
  q = low-moderate           q = maximum          q = low (jam)

  FUNDAMENTAL DIAGRAM:
  Flow q
  ^
  qmax |     *
       |    / \
       |   /   \
       |  /     \
       | /       \___
       +------------>
       0   kc   kjam   Density k

  Left branch: free flow (stable)
  Right branch: congested (unstable, stop-and-go waves)
  qmax: capacity, at critical density kc
```

### Greenshields and Calibrated Models

**Greenshields (1935):** Linear speed-density relationship.

    v = vf * (1 - k/kjam)
    q = vf * k * (1 - k/kjam)

Simple but underestimates capacity at intermediate densities. Still useful for first approximations and analytical solutions.

**Triangular fundamental diagram (Newell-Daganzo):**

```
  Flow q
  ^
  qmax |    /\
       |   /  \
       |  / w  \  <- backward wave speed w
       | /      \
       +------------>
       0   kc  kjam   Density k

  Free flow: slope = vf (free flow speed)
  Congested: slope = -w (backward wave speed, ~15-25 km/h)

  The triangular model captures the key asymmetry:
  Congestion propagates backward at speed w.
  This is a shock wave in the traffic stream.
```

### LWR Kinematic Wave Model

Lighthill-Whitham-Richards (1955-1956) — the foundational continuum model of traffic flow. Traffic density is a conserved quantity: vehicles are not created or destroyed.

```
  Conservation equation:
  dk/dt + dq/dk * dk/dx = 0

  This is a first-order hyperbolic PDE.
  Same mathematical form as ideal gas dynamics, shallow water waves.

  Key result: Disturbances propagate as kinematic waves.
  - In free flow: waves travel forward (downstream)
  - In congestion: waves travel backward (upstream)

  STOP-AND-GO WAVES:
  Once a bottleneck forms (incident, merge, lane drop),
  the congestion wave propagates backward at ~15-20 km/h.
  The bottleneck can persist long after the incident clears.
  On I-405 LA: morning congestion waves from incidents at 7am
              persist until 10am even after incident cleared at 7:30am.
```

### Level of Service

The Highway Capacity Manual (HCM) quantifies traffic operations quality as Levels of Service A-F.

```
  FREEWAY LOS (Basic Freeway Segment):

  LOS | Density (pc/km/ln) | v/c ratio | Description
  ----|--------------------|-----------|-----------
  A   | <= 7               | <= 0.32   | Free flow, unconstrained
  B   | 7-11               | <= 0.49   | Reasonably free flow
  C   | 11-16              | <= 0.69   | Stable flow, restricted
  D   | 16-22              | <= 0.88   | High density, less stable
  E   | 22-28              | <= 1.00   | Near capacity, unstable
  F   | > 28 or breakdown  | > 1.00    | Forced flow, stop-and-go

  Capacity: ~2,200 pc/h/lane for basic freeway (ideal conditions)
  pc = passenger car equivalent (trucks count as 1.5-2.5 pc each)

  URBAN ARTERIAL LOS:
  Based on control delay (seconds/vehicle):
  LOS A: < 10s | LOS B: 10-20s | LOS C: 20-35s
  LOS D: 35-55s | LOS E: 55-80s | LOS F: > 80s
```

### Signalized Intersections

```
  WEBSTER OPTIMAL CYCLE LENGTH:

  C = (1.5L + 5) / (1 - Y)

  Where:
    C = optimal cycle length (seconds)
    L = total lost time per cycle (all phases, typically 4-6s each)
    Y = sum of critical phase flow ratios = sum(q_ci / s_ci)
    q_ci = critical lane flow for phase i
    s_ci = saturation flow for phase i (~1,800 veh/h/lane)

  WEBSTER AVERAGE DELAY PER VEHICLE:
  d = C*(1-lambda)^2 / (2*(1-lambda*x)) + x^2 / (2*q*(1-x))
  where lambda = green/cycle, x = degree of saturation (v/c)

  ACTUATED CONTROL:
  Instead of fixed cycle lengths, extend green in real-time
  based on detector presence.
  Modern: SCATS (Sydney), SCOOT (UK) — network-level adaptive control
  Signal timing updated every 90-180 seconds based on measured flow.
```

---

## Intelligent Transportation Systems (ITS)

### Freeway Management System (FMS)

```
  FREEWAY MANAGEMENT COMPONENTS:

  +------------------+     +------------------+
  | DETECTION        |     | CONTROL          |
  | Loop detectors   | --> | Variable Message |
  | Radar sensors    |     | Signs (VMS)      |
  | Bluetooth MAC    |     | Ramp Meters      |
  | probe vehicles   |     | Variable Speed   |
  |                  |     | Limits (VSL)     |
  +------------------+     +------------------+
           |                       |
           v                       v
  +------------------+     +------------------+
  | TMC (Traffic     | <-> | ALGORITHMS       |
  | Management       |     | Incident detect  |
  | Center)          |     | Congestion alg   |
  |                  |     | Ramp meter rate  |
  +------------------+     +------------------+
```

**Ramp metering:** Controls entry rate to freeway by signalizing on-ramps (1 car per green). Prevents demand exceeding capacity on merge; delays the onset of breakdown. Controversial (lines form on surface streets) but effective: studies show 3-10% reduction in travel time when implemented well.

**Variable Speed Limits (VSL):** Lower speed limits posted during congestion. Two rationales: (1) safety — reduce speed differential between free-flow and congested vehicles, (2) capacity — maintaining consistent lower speeds can delay breakdown onset. Speed Harmonization systems (Germany's Streckenbeeinflussungsanlage) have demonstrated both effects.

### Connected and Automated Vehicles (CAV)

```
  V2X COMMUNICATION MODES:

  V2V (Vehicle-to-Vehicle):   V2I (Vehicle-to-Infrastructure):
  Direct 5.9GHz DSRC or       Roadside units (RSU)
  C-V2X (cellular LTE/5G)    Traffic signals broadcasting
                               phase/timing data (SPAT)
  Use cases:                   Map data (MAP)
  - Forward collision warning
  - Emergency brake warning    V2P (Vehicle-to-Pedestrian):
  - Cooperative adaptive       Smartphone-based warning
    cruise control (CACC)

  DSRC vs C-V2X DEBATE:
  DSRC: Dedicated Short-Range Communication (IEEE 802.11p / WAVE)
        Low latency (<10ms), works without network infrastructure
        FCC allocated 5.9GHz band in 1999
  C-V2X: Uses LTE/5G cellular network
         Can use existing carrier infrastructure
         Mode 4: direct sidelink (no infrastructure needed)

  US status (2024): FCC reallocated most of 5.9GHz band away from DSRC
  C-V2X is the dominant path forward.

  COOPERATIVE ADAPTIVE CRUISE CONTROL (CACC):
  Vehicles form platoons using V2V communication.
  Vehicle N+1 receives brake signal from vehicle N before seeing brake lights.
  Reaction time reduced from ~1.5s (human) to ~0.1s (V2V).
  Result: much smaller following gap, higher road capacity.
  Theoretical capacity increase: 20-40% with 100% penetration.
  Practical: penetration rates currently <5%, benefits negligible.
```

### Traffic Data and Probe Vehicles

```
  TRAFFIC DATA SOURCES:

  Traditional:
  +------------------+
  | Loop detectors   | Inductive loops in pavement
  | (point data)     | Count, speed, occupancy
  |                  | Expensive to maintain; spot data only
  +------------------+

  Modern:
  +------------------+     +------------------+
  | Bluetooth / WiFi |     | Probe vehicle    |
  | MAC address      |     | data             |
  | matching (privacy)| ... | Google/HERE/TomTom|
  +------------------+     | From smartphones |
                           | GPS tracks       |
                           | Near-real-time   |
  +------------------+     +------------------+
  | Radar / lidar    |     | Video analytics  |
  | roadside sensors |     | ALPR cameras     |
  +------------------+     +------------------+

  FUSED DATA -> TMC -> VMS + navigation apps + signal timing
```

---

## Road Safety

Road crashes kill **1.35 million people per year** (WHO, 2019). The leading cause of death for ages 5-29.

```
  SPEED-INJURY SEVERITY RELATIONSHIP:

  Pedestrian struck at:   Fatality risk
  30 km/h (19 mph):       ~5-10%
  50 km/h (31 mph):       ~30-40%
  60 km/h (37 mph):       ~70-80%
  80 km/h (50 mph):       ~90-95%

  Physics: KE = 0.5mv^2
  10% speed reduction -> ~20% KE reduction -> significant injury reduction

  VEHICLE-TO-VEHICLE CRASH:
  Delta-V (change in velocity) is the injury predictor.
  Head-on crash at 60+60 km/h = 120 km/h effective closing speed.

  SAFE SYSTEM APPROACH:
  Traditional: blame the driver (95% of crashes involve human error)
  Safe System: design roads so that human errors do not cause death

  Four elements:
  1. Safe speeds (speed limits match road function and forgiveness)
  2. Safe roads (median barriers, forgiving roadsides, clear zones)
  3. Safe vehicles (AEB, ESC, seatbelts, pedestrian AEB)
  4. Safe road use (enforcement, education)

  Vision Zero (Sweden, 1997): zero fatalities as aspirational target.
  Not achieved, but Sweden has lowest road fatality rate in the world.
  ~2 deaths/billion vehicle-km vs US ~7 deaths/billion vehicle-km.
```

**Automatic Emergency Braking (AEB):** The single highest-impact vehicle safety technology per dollar. Detects imminent collision and brakes automatically if driver does not react. NHTSA mandate for all new light vehicles by 2029. Insurance industry data shows ~50% reduction in rear-end crashes.

---

## Decision Cheat Sheet

| I want to... | Approach |
|-------------|----------|
| Determine minimum curve radius for design speed | AASHTO Green Book: R = v^2 / (127 * (e + f)) |
| Size a pavement structure for heavy trucks | AASHTO 1993 structural number method; consider MEPDG for major projects |
| Estimate capacity of a freeway lane | Start with 2,200 pc/h/lane, adjust for trucks, grades, weather |
| Diagnose where congestion is forming | Look for bottleneck: lane drops, merge zones, signal-controlled ramps |
| Optimize signal timing at intersection | Webster formula; use TRANSYT for arterial coordination |
| Evaluate freeway interchange type | Diamond (low cost, signal), SPUI (urban, high capacity), DDI (left-turn heavy) |
| Assess road safety improvement options | Safe System first: median barriers, junction redesign, speed management |
| Design a ramp metering strategy | Target 1,800-2,000 pc/h/lane mainline density; Demand-Capacity algorithm |

---

## Common Confusion Points

**Volume vs Capacity vs Flow**
Volume is what was actually measured (vehicles counted in a time period). Flow is the rate (veh/h). Capacity is the maximum flow the facility can sustain. Volume > Capacity is impossible — what happens instead is breakdown and queuing. Demand may exceed capacity.

**LOS F does not mean the road stops**
LOS F means demand exceeds capacity. Queues form and flow is forced (stop-and-go). Traffic still moves — just slowly and inconsistently. The road does not "stop" at LOS F; it just operates very badly.

**Induced demand is not a myth**
The empirical literature is clear (Duranton-Turner 2011, "fundamental law of road congestion"): adding lane-miles generates approximately equivalent vehicle-miles in the long run (elasticity ~0.9-1.1). The mechanism: induced demand from suppressed trips (people change destination, route, time, or mode when capacity adds). This does not mean adding capacity is never worthwhile — it depends on whether induced demand is desirable. But it does mean that adding capacity does not solve congestion permanently.

**Flexible vs rigid pavement — not always a clear choice**
Asphalt is not always "better." Concrete (rigid) lasts longer, tolerates more rutting-prone soils, and has lower life-cycle cost in some climates. The US interstate system is largely concrete. Urban roads are mostly asphalt for ease of utility access and incremental maintenance.

**The IRI roughness meter matters more than it sounds**
IRI affects vehicle operating costs significantly. A smooth road (IRI=1) generates ~10% lower vehicle operating costs than a rough road (IRI=5). For freight-heavy corridors, this is a quantifiable economic benefit in pavement CBA — often larger than the time savings.
