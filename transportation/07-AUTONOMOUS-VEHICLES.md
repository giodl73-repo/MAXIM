# Autonomous Vehicles

## The Big Picture

Autonomous vehicles are a real-time embedded systems problem at the intersection of robotics, machine learning, and safety-critical software engineering. The perception-prediction-planning pipeline is well understood; the unsolved problem is long-tail edge cases and the statistical validation challenge of proving safety in a world where rare events matter most.

```
+------------------------------------------------------------------+
|                    AV SYSTEM ARCHITECTURE                        |
|                                                                  |
|  PERCEPTION                                                      |
|  +----------+ +----------+ +----------+ +----------+            |
|  | LiDAR    | | Camera   | | Radar    | | Ultrasonic|           |
|  | (point   | | (RGB,    | | (Doppler,| | (parking, |           |
|  | cloud)   | | semantic)| | velocity)| | close)   |           |
|  +----------+ +----------+ +----------+ +----------+            |
|       |            |           |              |                 |
|       +------------+-----------+--------------+                 |
|                         |                                       |
|                   SENSOR FUSION                                  |
|                   (Kalman filter,                               |
|                   deep fusion)                                   |
|                         |                                       |
|  PREDICTION                                                      |
|  +--------------------------------------------+                 |
|  | Object detection + tracking + prediction   |                 |
|  | "That car will turn left in 2 seconds"     |                 |
|  +--------------------------------------------+                 |
|                         |                                       |
|  PLANNING                                                        |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Route    | | Behavioral| | Motion  | | Control  |           |
|  | Planning | | Planning  | | Planning| | (actuators)|         |
|  +----------+ +----------+ +----------+ +----------+            |
|                                                                  |
|  LOCALIZATION (runs in parallel)                                 |
|  +--------------------------------------------+                 |
|  | HD Map + LiDAR/camera matching + GPS/IMU   |                 |
|  | "I am at this exact position on the map"   |                 |
|  +--------------------------------------------+                 |
+------------------------------------------------------------------+
```

---

## SAE J3016 Autonomy Levels

SAE International defines 6 levels of driving automation. The naming is often misused commercially.

```
  LEVEL | NAME                | Monitors | Who drives?  | ODD
  ------+---------------------+-----------+--------------+--------
  L0    | No Automation       | Human     | Human always | Any
        | (warnings ok)       |           |              |
  ------+---------------------+-----------+--------------+--------
  L1    | Driver Assistance   | Human     | Human (+1    | Limited
        | (AEB, ACC, or       |           | system)      |
        | lane-keep, not both)|           |              |
  ------+---------------------+-----------+--------------+--------
  L2    | Partial Automation  | Human     | Human (must  | Limited
        | (ACC + lane-keep    | MUST watch| supervise    |
        | combined)           |           | continuously)|
  ------+---------------------+-----------+--------------+--------
  L3    | Conditional         | SYSTEM    | System (in   | Specific
        | Automation          | (driver   | ODD); driver | (highway,
        |                     | on-standby| on standby   | traffic jam)
  ------+---------------------+-----------+--------------+--------
  L4    | High Automation     | SYSTEM    | System       | Specific
        |                     |           | (no driver   | (geofenced)
        |                     |           | needed)      |
  ------+---------------------+-----------+--------------+--------
  L5    | Full Automation     | SYSTEM    | System       | ANY
        |                     |           | everywhere   |

  ODD = Operational Design Domain: the specific conditions (geography,
  weather, speed, road type) in which the system is designed to operate.

  KEY INSIGHT: L5 does not exist in any commercial deployment.
  All deployed systems are L2 or L4 in limited ODD.
  There is no L5 vehicle for sale or in commercial service.
```

### The L3 Trap

Level 3 ("conditional automation") has been largely abandoned by the industry. The reason is cognitive science, not engineering:

```
  THE L3 COGNITIVE TRAP:

  L3 promise: "System drives; driver monitors but can look away."
  When system fails: "Driver, take over immediately."

  PROBLEM: Out-of-the-loop syndrome.
  Humans cannot maintain vigilant monitoring for hours while doing nothing.
  Reaction time after extended passive monitoring: 3-25 seconds.
  At 120 km/h: car travels 100-833m before driver is in control.
  This exceeds almost any reasonable takeover distance.

  EVIDENCE:
  Stanford simulation studies: drivers disengaged (phone, sleep) within minutes.
  Volvo autonomous driving study: drivers asleep within 10 minutes.
  NTSB analysis of Tesla Autopilot (L2) crashes: drivers treat L2 as L3.

  RESULT: Most manufacturers skipped L3.
  Mercedes Level 3 (DRIVE PILOT): approved Germany/Nevada at <=60 km/h only.
  Honda Legend: L3 approved Japan at <=50 km/h, limited production.
  Nearly everyone else: L2 -> L4 (skip L3 for high-speed operation).
  Tesla: remains L2 (SAE), despite "Full Self-Driving" marketing name.
```

---

## Sensor Modalities

### LiDAR (Light Detection and Ranging)

LiDAR produces a 3D point cloud of the environment by measuring time-of-flight of laser pulses.

```
  LIDAR OPERATION:

  Spinning/mechanical (Velodyne HDL-64E, Ouster OS1):
  +----------+
  | 64 laser |  -> Rotates 360 degrees, 10-20 Hz
  | channels |  -> 1.3M points/second
  | 100m     |  -> Range: 0.1m to 120m (typical)
  | range    |  -> Accuracy: ±2cm
  +----------+
  Advantage: full 360-degree coverage
  Disadvantage: large, expensive ($75K in 2017), moving parts fail

  Solid-state (MEMS, OPA, Flash):
  +----------+
  | No       |  -> Fixed field of view (120°x25° typical)
  | moving   |  -> Lower cost ($500-5000)
  | parts    |  -> More reliable
  +----------+
  Advantage: cost, reliability, compact
  Disadvantage: limited FOV; need multiple units for 360°
  Examples: Luminar Iris, Mobileye EyeQ, Cepton MEMS

  POINT CLOUD OUTPUT:
  Each point: (x, y, z, intensity, return_number)
  64-channel spinning: ~128,000 points per rotation
  Dense enough to: detect pedestrians at 50m, vehicles at 100m+,
  lane lines, traffic cones, debris in road.

  LIDAR LIMITATIONS:
  - Fog/heavy rain: scatters laser -> range degraded
  - Snow: accumulates on housing -> blind spots
  - Dark objects (black car): lower return intensity
  - Bright retro-reflective surfaces: saturation
  - Cost: still $500-5000+ for automotive grade
```

### Camera

Cameras provide rich semantic information but require learned models for depth estimation.

```
  CAMERA TYPES IN AV:

  Forward-facing (1-3 cameras):   Fisheye surround (4-8 cameras):
  +------------------+            +------------------+
  | 60° FOV          |            | 180-195° FOV     |
  | 1280x960 @ 30fps |            | Wide, low-res    |
  | Long range main  |            | Parking, close   |
  | object detection |            | object detection |
  +------------------+            +------------------+

  MONOCULAR DEPTH AMBIGUITY:
  A single camera cannot measure distance directly.
  A 2m object at 10m and a 4m object at 20m look identical.
  Solutions:
  1. Stereo camera: geometric triangulation (precise but only ~50m)
  2. Monocular depth estimation (CNN): learned from training data
     Accurate if training distribution covers the scenario.
  3. Camera + LiDAR fusion: LiDAR provides sparse but accurate depth.

  TESLA FSD PHILOSOPHY:
  Camera-only (no LiDAR). Uses:
  - 8 cameras (forward, lateral, surround)
  - Neural network depth estimation
  - Occupancy networks (3D voxel occupancy, not object detection)
  Argument: humans drive with just eyes; cameras are cheaper; LiDAR
            false positive issues in some conditions.
  Counter-argument: human visual cortex is far more capable than
                    current cameras + networks; LiDAR provides range
                    directly without requiring depth estimation.
  Industry consensus (2024): most full L4 programs use LiDAR.
```

### Radar

Radar works in all weather conditions and provides direct velocity measurements via Doppler effect.

```
  AUTOMOTIVE RADAR TYPES:

  Short-range (SRR): 0.15m to 30m, 150° FOV
  Corner radars (4): used for blind spot, parking, cross-traffic

  Long-range (LRR): 0.5m to 250m, 18° FOV
  Front-facing: ACC (adaptive cruise), highway AEB

  UNIQUE CAPABILITIES:
  - Measures relative velocity directly (Doppler)
  - Works in: fog, rain, snow, darkness, dust
  - Sees through visual obstructions (limited)

  LIMITATIONS:
  - Low angular resolution (difficult to distinguish two close objects)
  - Ghosts/multipath (reflections from guardrails, bridges)
  - No height measurement (traditional)
  - Imaging radar (4D) improves resolution significantly

  4D IMAGING RADAR (2022+):
  ZF, Arbe, AEye, Aptiv smart radar.
  Resolution: x, y, z, velocity (4 dimensions).
  Approaching LiDAR quality in some scenarios.
  Advantage: all-weather, established supply chain, lower cost.
```

---

## Sensor Fusion

No single sensor is sufficient. Fusion combines their complementary strengths.

```
  SENSOR FUSION LEVELS:

  EARLY FUSION (raw data):         LATE FUSION (detections):
  +------+                         +------+
  |LiDAR | -> raw points            |LiDAR | -> objects
  |Camera| -> raw pixels   FUSE    |Camera| -> objects   FUSE
  |Radar | -> raw signals   HERE   |Radar | -> objects    HERE
  +------+                         +------+

  Early: richer representation, harder to train, larger compute
  Late: modular, easier to test, loses cross-modal features

  DEEP FUSION (intermediate):
  Middle ground: fuse at feature level after some processing.
  Most production systems use deep or late fusion in practice.

  KALMAN FILTER (tracking):
  Extended Kalman Filter (EKF) tracks object state over time.
  State: (x, y, z, vx, vy, vz, heading)
  Predict: extrapolate state forward using motion model
  Update: incorporate new sensor measurement, weighted by confidence

  OBJECT TRACKING OUTPUT:
  For each tracked object:
  - ID (persistent across frames)
  - Bounding box (3D)
  - Velocity vector
  - Classification (car, truck, pedestrian, cyclist, unknown)
  - Confidence score
  - Prediction horizon (next 3-5 seconds)
```

---

## HD Maps and Localization

### Why HD Maps

Standard GPS accuracy is 3-10m (95% confidence). Lane-level driving requires <0.3m. HD maps provide the prior information that enables centimeter-level localization.

```
  HD MAP LAYERS:

  Layer 1: Lane geometry
  +---------------------------+
  | Lane centerlines          |
  | Lane widths               |
  | Lane connectivity graph   |
  | Speed limits              |
  | Lane markings type        |
  +---------------------------+

  Layer 2: Regulatory information
  +---------------------------+
  | Stop lines                |
  | Traffic light positions   |
  | Turn restrictions         |
  | Crosswalk locations       |
  | School zone boundaries    |
  +---------------------------+

  Layer 3: 3D features (for localization)
  +---------------------------+
  | Road surface intensity    |
  | Static landmarks          |
  | Building faces            |
  | Overhead structures       |
  | Feature descriptors       |
  +---------------------------+

  PROVIDERS: HERE HD Live Map, TomTom AMS, Baidu Apollo Maps,
             Waymo private maps, Mobileye Road Experience

  MAP UPDATE PIPELINE:
  Mapping vehicles collect data.
  Processing: extract features, detect changes.
  Diff update: send only changed tiles to vehicles.
  Frequency: safety-critical changes (road closure, new barrier) < 1 hour.
  Normal updates: daily.
  Challenge: every construction zone is a potential map error.
```

### Online Localization

```
  LIDAR-TO-MAP LOCALIZATION:

  ICP (Iterative Closest Point):
  Align current LiDAR scan to HD map feature layer.
  Iteratively minimize distance between corresponding points.
  Converges to <0.1m accuracy if initialization is good.
  Fragile if environment changed significantly (construction).

  NDT (Normal Distributions Transform):
  Divide map into voxels; fit normal distribution to points in each.
  Align scan to map by maximizing likelihood.
  More robust than ICP to sparse scans and dynamic objects.
  Used by: Autoware (open source AV stack).

  GPS/IMU DEAD RECKONING:
  IMU (accelerometers + gyroscopes): measure linear acceleration + rotation.
  Dead reckoning: integrate IMU from last known position.
  Error accumulates rapidly: 1% of distance traveled typical.
  100m traveled -> 1m error from dead reckoning alone.
  GPS corrects drift when available.
  GNSS + IMU Kalman filter: <0.5m in nominal conditions.
  GPS-denied (tunnel, urban canyon): rely on LiDAR matching.
```

---

## Prediction

The system must predict what surrounding objects will do next. This is the hardest subproblem.

```
  PREDICTION PROBLEM:

  Inputs:
  - Object state history (last 3-5 seconds)
  - Road geometry (from HD map)
  - Traffic signals state
  - Context (other vehicles' states)

  Output: probability distribution over future trajectories
  for each dynamic object (next 5-10 seconds).

  PREDICTION MODEL EVOLUTION:

  Simple:         Constant velocity; constant acceleration.
                  "That car will keep going straight."
                  Fails at intersections, merge scenarios.

  Physics-based:  Bicycle model, kinematic constraints.
                  Handles curves better.
                  Still single-mode (only one future predicted).

  Social forces:  LSTM sequence models, Transformer models.
                  Learn interaction patterns from data.
                  Examples: SoPhie (CVPR 2019), GRIP++, TNT, Wayformer.
                  Multi-modal: predicts distribution of futures.

  MULTI-MODAL PREDICTIONS:
  +----------------------------------+
  | Future: Turn left (prob: 0.55)   |
  |         Go straight (prob: 0.30) |
  |         Turn right (prob: 0.15)  |
  +----------------------------------+
  Planner must handle all modes with probability weighting.
  This is intractable for many objects if done naively.
  Solution: importance sampling; consider only high-probability futures.

  PREDICTION FAILURE = THE HARD PROBLEM:
  An agent doing something unexpected (jaywalker suddenly running,
  car making illegal U-turn) will have low probability assigned
  to the actual outcome. The planner must still react correctly.
  No prediction model handles this perfectly.
```

---

## Planning

### The Planning Stack

```
  PLANNING HIERARCHY:

  ROUTE PLANNING (route-level, pre-trip):
  Dijkstra/A* on road graph from origin to destination.
  Waypoints every few hundred metres.
  Updates when: road closure detected, traffic changes route.

  BEHAVIORAL PLANNING (intersection/merge level, 10-30 seconds):
  Decide: yield or proceed at intersection?
          when to change lane for upcoming exit?
          how to merge into traffic?
  Inputs: prediction of others, current state, map.
  Output: high-level actions (change lane left, slow for pedestrian).
  Methods: finite state machine (explicit rules), behavior trees,
           decision trees, inverse RL (learned policies).

  MOTION PLANNING (trajectory level, 3-10 seconds, ~10Hz):
  Given behavioral decision, generate a smooth, safe trajectory.
  Inputs: behavioral decision, current position/velocity, objects.
  Output: trajectory (position, velocity, acceleration) over time.

  FRENET FRAME:
  Transform 3D road geometry to (s, d) coordinates.
  s = distance along road centerline.
  d = lateral offset from centerline.
  Trajectory planning in Frenet is much easier than Cartesian.
  Polynomial trajectories in (s, d) can be generated analytically.

  CONTROL (actuation level, 100Hz):
  Track the planned trajectory.
  PID controllers for steering and throttle/brake.
  Or: Model-Predictive Control (MPC) for optimal tracking.
  Output: steering angle, throttle %, brake pressure.
```

### Safety Guarantees

```
  FORMAL SAFETY APPROACHES:

  RSS (Responsibility-Sensitive Safety — Mobileye):
  Mathematical model that defines when an AV is "responsible"
  for a potential collision.
  Safe distance equations based on kinematics.
  AV only acts in ways that maintain "safe state."
  Advantage: formal, verifiable safety guarantee.
  Limitation: conservative; may not match human-level performance.

  SHADOW MODE (Tesla):
  L2 vehicle logs what human did vs what FSD would have done.
  1M+ vehicles collecting data continuously.
  Statistical validation: FSD intervention rate vs human intervention rate.
  Scale advantage: unprecedented data volume.
  Limitation: human performance is the baseline; not sufficient for
              proving safety against rare events (black swans).

  SIMULATION:
  Waymo runs >1B virtual miles per year.
  Parameterize scenarios from real disengagements.
  Fuzz testing: modify parameters (pedestrian speed, vehicle position).
  Limitation: sim-to-real gap; simulator cannot perfectly model physics.
              Rare events in reality may be rarer in simulation.
              Cannot validate against events never seen.
```

---

## Current Deployment Status (2025)

### Commercial Deployments

```
  AV STATUS (early 2025):

  ROBOTAXI:

  Waymo (Alphabet):
  Service: San Francisco, Phoenix, Austin
  Fleet: ~700 vehicles (Jaguar I-PACE + Zeekr-based W6)
  Status: Paid commercial service, no safety driver
  SAE Level: 4 (in defined ODD)
  2024: expanded to LA; first licensed interstate (on-ramp) operation
  Safety record: lower injury rate per mile than human-driven
                 (per Waymo published data; externally not yet verified)

  Cruise (GM subsidiary):
  Status: Suspended October 2023 after pedestrian drag incident
          California DMV suspended permit.
          GM restructured Cruise, significant layoffs.
          Limited operations resumed 2024.
  Lesson: ONE serious safety incident can ground an entire program.
          Public trust is fragile; incident investigation is existential.

  Zoox (Amazon):
  Purpose-built vehicle (bidirectional, no steering wheel, no front/back)
  Service: Foster City CA, Las Vegas NV (employee shuttles 2023-2024)
  Timeline: public service announcement "coming soon" since 2021

  BAIDU Apollo Go (China):
  ~1,000 Robotaxis in Wuhan, Chongqing, Shenzhen
  Commercial service without safety driver (selected areas)
  China's most advanced commercial L4 deployment

  AV TRUCKING:

  Aurora (Aurora Driver):
  Launched commercial driverless trucking April 2024 (Texas I-45)
  Volvo, PACCAR (Kenworth/Peterbilt) partners
  First true L4 commercial freight operation in US
  ODD: Texas highways, daytime, good weather initially

  Waymo Via (trucking arm):
  Partnership with Daimler/Freightliner
  Testing in Texas/Arizona; commercial timeline unclear

  Tesla Semi:
  Currently L2 (driver required). Timeline to L4: unclear.
```

### The Validation Problem

```
  WHY PROVING AV SAFETY IS HARD:

  Rand Corporation study (2016):
  To demonstrate with 95% confidence that AVs are 20% safer
  than human drivers, AVs need to drive 11 billion km.
  Current Waymo cumulative: ~32 million km (public roads, 2024).

  THE LONG TAIL:
  Most driving is routine (highway, clear weather, normal traffic).
  Fatalities per billion km: ~7 (US road average).
  AV must perform better on these common cases AND on rare events.
  Rare events (child running from behind parked car, ice storm,
  wrong-way driver) occur once per million km.
  Statistical validation requires billions of miles for rare events.

  SOLUTION ATTEMPT: Adverse scenario injection.
  Run simulations with injected rare events.
  Test against "scenario database" from all real-world incidents.
  Validates system against known unknowns; not unknown unknowns.

  THE UNKNOWN UNKNOWNS PROBLEM:
  Human drivers fail unpredictably in specific edge cases (fatigue,
  distraction, impairment).
  AV systems fail in different edge cases (novel scenarios not in
  training distribution, sensor failures, rare map errors).
  Neither failure mode is fully characterizable in advance.
  This is fundamentally a safety engineering problem, not just ML.
```

---

## Regulatory Frameworks

| Jurisdiction | Framework | Key Rules | Status |
|-------------|-----------|-----------|--------|
| **US Federal (NHTSA)** | SGO 2023 (Standing General Order) | Incident reporting mandate for L2-L5 | Active since 2021 |
| **California DMV** | AV Testing + Deployment rules | Per-incident reporting, permit system | Active, model for other states |
| **Texas/Arizona** | Minimal regulation | No special AV permits required | Permissive |
| **EU** | EU Type Approval Regulation 2022/1426 | L3 approved to 130 km/h | Active 2022 |
| **Germany** | AFGBV 2021 | L4 in defined areas; federal authority | Active, first in world |
| **China** | GB/T standard + city licenses | City-level approvals | Rapidly advancing |
| **Japan** | Road Traffic Act amendments 2023 | L4 limited areas | Active |

---

## Decision Cheat Sheet

| AV decision | Guidance |
|-------------|---------|
| Assess AV safety level claims | Ask: L2 or L4? What ODD? What disengagement rate? Compare to Waymo published data |
| Choose sensor suite for L4 | LiDAR + camera + radar required for production; camera-only for L2 |
| Estimate localization accuracy | GPS/IMU: ~3-10m; with LiDAR-to-map: <0.1m; in tunnel (dead reckoning): degrades |
| Evaluate prediction model | Single-mode vs multi-modal; long-tail coverage; pedestrian/cyclist handling |
| Validate planning safety | Test against scenario database; RSS formal constraints; simulation + real-world |
| Assess L3 for a new program | Generally avoid for highway speeds; cognitive science problem is unsolvable |

---

## Common Confusion Points

**Tesla FSD is not Full Self-Driving in SAE terms**
Tesla's marketing name "Full Self-Driving" is an SAE Level 2 system. The driver must supervise continuously. NHTSA/NTSB have investigated multiple fatalities where drivers were not monitoring. Tesla's own terms state the driver must remain attentive. The SAE community and regulators view the naming as misleading.

**L4 is not L5**
Every commercial L4 deployment is geofenced. Waymo operates only in defined cities with pre-mapped HD maps and clear weather requirements. None of these systems can operate everywhere. L5 — full automation in any condition anywhere — does not exist and has no near-term commercial roadmap.

**Disengagement rates are not a consistent safety metric**
California requires reporting of disengagements (human took control from system). But definitions of "reportable disengagement" differ across companies, and more disengagements might mean a more cautious system (good) or a less reliable one (bad). Waymo stopped reporting disengagements as a primary metric; they report safety event rates instead.

**The Cruise incident (2023) matters more than the incident itself**
A single pedestrian-drag incident caused California to suspend Cruise's permits, effectively ended Cruise as an independent entity, cost GM $900M in write-downs, and delayed the entire US robotaxi industry. The lesson: public trust in AV safety is extremely fragile, and the regulatory/reputational response to incidents is potentially existential. Safety engineering in AV is not just technical — it is enterprise risk management.

**Camera-only vs LiDAR is not settled**
Tesla's camera-only FSD is commercial at scale (L2). Waymo/Cruise/Aurora use LiDAR for their L4 deployments. The argument is about cost vs robustness at different automation levels. For L2 (driver supervises), camera-only may be sufficient. For L4 (no driver), the industry consensus is currently LiDAR. This may change if imaging radar or camera depth estimation matures sufficiently.
