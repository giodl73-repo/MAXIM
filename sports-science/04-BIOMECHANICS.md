# Biomechanics and Movement Analysis

## The Big Picture

Biomechanics applies mechanics (Newtonian physics) to biological systems. In sports, it answers: what forces are acting, what motions result, and how can we optimize the motion for performance or injury prevention?

```
BIOMECHANICS HIERARCHY:

  KINEMATICS                          KINETICS
  (describe motion)                   (explain motion)
  +---------------------------+        +---------------------------+
  | Linear: position,          |        | Forces: ground reaction    |
  | velocity, acceleration     |        | forces, joint moments,     |
  | Angular: joint angles,     |        | muscle forces              |
  | angular velocity           |        | Impulse-momentum theorem   |
  | Center of mass trajectory  |        | Work-energy theorem        |
  | Segment positions          |        | Power output               |
  +---------------------------+        +---------------------------+
          |                                      |
          +------------------+-------------------+
                             |
              FREE BODY DIAGRAM (FBD)
              The analytical tool that connects both:
              Draw the body segment; label all forces;
              apply Newton's 2nd law: ΣF = ma; ΣM = Iα
```

---

## Free Body Diagrams in Sport

```
RUNNING FBD (midstance, one leg in contact):

         Body weight (W) → acting downward through CoM
              |
              v
  +---[Body]-+
              |
              |
          +--[Leg]--+
              |
  ←←←←←←←←←←+→→→→→→→→→   Ground Reaction Force (GRF)
  Braking    CoP          Vertical
  component              component
              |
        (center of pressure)

  At midstance vertical GRF ≈ 2.5× body weight at running speed.
  During sprint: peak GRF = 3–5× body weight.
  Each step: impulse = force × time = change in momentum.

  NEWTON'S THIRD LAW:
  Foot pushes back and down on ground.
  Ground pushes forward and up on foot (equal and opposite).
  This is how we accelerate — we don't push "forward";
  we push the earth backward and the earth pushes us forward.
```

---

## Ground Reaction Forces

The force plate is the primary measurement tool for kinetics:

```
FORCE PLATE OUTPUT:
  Measures 3-component GRF: Fx (anterior-posterior), Fy (medial-lateral), Fz (vertical).
  Sample rate: typically 1,000–2,000 Hz for running analysis.
  Also computes: Center of Pressure (CoP) — location of GRF application on plate.

RUNNING VERTICAL GRF PROFILE (double-peak):

  Force/BW
  3.0 |     /\            /\
  2.5 |    /  \          /  \
  2.0 |   /    \        /    \
  1.5 |  /      \      /      \
  1.0 |_/        \____/        \___
  0.5 |
  0.0 |_________________________________> Time
           Impact      Active push-off
           peak        peak

  Impact peak (first): heel-strike related; bone/ligament loading.
  Active peak (second): push-off; muscle-generated force.
  Valley between: midstance, leg spring loaded.

  Heel vs. Forefoot strike:
  Heel: distinct sharp impact peak (loading rate matters for injury).
  Forefoot: impact peak absent or smaller; loading rate lower.
  Evidence on injury: unclear; current consensus = transition carefully
  if changing foot strike (Achilles tendinopathy risk when switching to forefoot).
```

---

## Running Gait

### The Gait Cycle

```
GAIT CYCLE (one complete stride):

  LEFT FOOT STRIKE → RIGHT FOOT STRIKE → LEFT FOOT STRIKE

  STANCE PHASE (~40% of cycle at running):
    Loading response (heel strike to flat foot)
    Midstance (single support)
    Terminal stance (heel off to toe off)
    Pre-swing (toe off preparation)

  SWING PHASE (~60% of cycle at running):
    Initial swing (toe off to maximum knee flexion)
    Mid swing
    Terminal swing (before next contact)

  DOUBLE SUPPORT (in walking, not running):
    Walking: both feet on ground simultaneously.
    Running: aerial phase instead — neither foot on ground.
    Walk-run transition: ~1.8–2.0 m/s.

KEY GAIT VARIABLES:
  Stride length × stride frequency = velocity.
  Optimal stride length is self-selected (Froude number optimization).
  Increasing speed: primarily increased stride length at low-moderate speeds;
                    increasing stride frequency at high speeds.
  Overstriding: heel contacts far in front of center of mass →
                large braking GRF → energy waste → injury risk.
  Target: foot lands under or slightly in front of CoM.
```

### Cadence

```
CADENCE (stride rate):
  Measured in steps/minute or strides/minute (strides = two steps).
  Typical recreational runner: 160–170 steps/min.
  Common advice: 170–180 steps/min ("Daniels 180 rule").
  Elite runners: typically 185–200+ steps/min.

  CADENCE-INJURY RELATIONSHIP:
  Higher cadence at same speed:
    Shorter ground contact time.
    Lower peak GRF.
    Less knee flexion at contact.
    Lower patellofemoral, hip, and IT band stress.
  10% cadence increase: ~14% reduction in knee load (meta-analysis data).

  PRACTICAL INTERVENTION:
  Increasing cadence by 5–10%: possible with metronome training.
  Overcorrecting (dramatic cadence increase): can cause Achilles overload.
  Cadence change should be gradual (5% increase; adapt over weeks).

RUNNING ECONOMY:
  O₂ cost of running at a given speed (mL/kg/km).
  Lower economy (less O₂ cost) = more efficient runner.
  Factors improving economy:
    Appropriate cadence (not too low).
    Spring-like leg stiffness (elastic energy return).
    Low vertical oscillation (energy wasted moving up-down).
    Lightweight, flexible footwear (reduces foot segment inertia).
    Strength training (improved tendon stiffness and neuromuscular efficiency).
```

---

## Swimming Biomechanics

```
SWIMMING FORCES:
  Drag: water resistance to forward motion. Proportional to velocity².
  Propulsive force: derived from arm stroke and kick.

  F_net = F_propulsive - F_drag
  To accelerate or maintain speed: F_propulsive > F_drag.

DRAG TYPES:
  Pressure drag (form drag): dominant. Due to pressure difference
  front-to-rear of swimmer. Reduced by streamlined position.
  Friction drag: skin friction. Reduced by smooth, tight suits.
  Wave drag: energy in surface waves. Reduced by swimming deeper.

HIGH ELBOW CATCH:
  The "early vertical forearm" (EVF) or "high elbow catch."
  When: as hand enters water and begins pull phase.
  What: maintain elbow higher than hand, forearm nearly vertical.
  Why: maximizes the area of the forearm and hand pushing against water.
       More propulsive surface area = more thrust per stroke.
  This is the single most important technique element in freestyle.
  Incorrect catch (dropped elbow): hand pushes downward, not backward → wasted effort.

BODY ROTATION:
  Freestyle: 45–60° body rotation per stroke.
  Enables: reach further with entry hand, more powerful pull.
  Also reduces shoulder injury risk (reaches along longitudinal axis, not transversely).
  Too little rotation: shorter reach, impaired power.
  Too much rotation: corkscrew effect, drag increase.
```

---

## Throwing Biomechanics

### The Kinetic Chain

```
THROWING KINETIC CHAIN:
  Energy generated at large body segments, transferred to smaller:

  LEGS → HIPS → TRUNK → SHOULDER → ELBOW → WRIST → FINGERS → BALL

  SEQUENCE TIMING:
  Each segment reaches peak velocity, then decelerates.
  The deceleration of each proximal segment transfers energy
  to the next distal segment ("whipping" effect).

  FOOT STRIKE (rotational torque)
       ↓ (50–100ms)
  HIP ROTATION (peak ~900°/s for baseball pitcher)
       ↓ (30–50ms)
  TRUNK ROTATION / SHOULDER EXTERNAL ROTATION (extreme — up to 170°)
       ↓ (20–30ms)
  SHOULDER INTERNAL ROTATION (fastest rotation in human body ~7000°/s)
       ↓ (10–20ms)
  ELBOW EXTENSION → WRIST SNAP → BALL RELEASE

BASEBALL PITCH (peak values):
  Elbow valgus torque: 60–100 Nm at foot contact.
  Shoulder internal rotation: ~7,000°/s — fastest angular velocity
                               in any documented human movement.
  Ball velocity: ~40 m/s (90 mph); release: ~55ms from peak rotation.

UCL STRESS:
  The ulnar collateral ligament (UCL) of the medial elbow bears
  the valgus load during the acceleration phase.
  Chronic overload → UCL insufficiency → "Tommy John" surgery.
  Partial/full UCL reconstruction with palmaris longus tendon graft.
  Recovery: 12–18 months (baseball pitchers); career-limiting before
  modern reconstruction; now pitchers often return to pre-injury level.
```

---

## Video Analysis Methods

### 2D Kinematics

```
2D VIDEO ANALYSIS:
  Single camera; analysis software (Dartfish, Kinovea — free, widely used).
  Measures: joint angles, segment positions, velocity, acceleration.
  LIMITATIONS:
    Only accurate for motion in the plane of the camera.
    Out-of-plane motion introduces error.
    Must calibrate with known reference distance.
  APPLICATIONS:
    Running gait screening (sagittal plane view — camera from side).
    Swim stroke analysis (underwater camera — sagittal or frontal).
    Weight room technique review.
    Sprinting: kinematics clearly visible at 120–240 fps.

  FRAME RATE REQUIREMENTS:
    Walking (1 m/s): 30 fps sufficient.
    Running (4 m/s): 60–120 fps recommended.
    Sprinting (10+ m/s): 120–240 fps.
    Golf swing: 500–1,000 fps.
    Pitch release: 1,000 fps.
    Most events: 120 fps provides useful data at low cost (consumer cameras).
```

### 3D Motion Capture

```
3D MOTION CAPTURE:
  Marker-based: retroreflective markers attached to body landmarks.
    Cameras (typically 8–12) detect marker positions.
    Reconstruct 3D positions of each marker.
    Calculate: joint angles, moments, powers using inverse dynamics.
    "Inverse dynamics": measure GRF and kinematics → calculate joint moments.
    Gold standard for clinical gait analysis and research.
    Limitation: markers required on skin; special suit needed; lab environment.

  MARKERLESS (2015+):
    Computer vision: pose estimation from video.
    Open-source tools: OpenPose, MediaPipe, DeepLabCut.
    Accuracy: improving rapidly; approaching marker-based accuracy for gross joints.
    No special equipment; standard cameras or smartphone.
    Limitation: accuracy still lower than marker-based for small joints;
                self-occlusion (limbs blocking each other) problematic.

INVERSE KINEMATICS / INVERSE DYNAMICS PIPELINE:
  Marker positions → 3D segment positions (kinematics).
  3D segment positions + GRF from force plates → joint moments/torques (kinetics).
  This pipeline requires: calibrated cameras, force plates synchronized with cameras.
  A full motion lab setup costs $100,000–$500,000+.
```

---

## Wearable Sensors

### GPS Systems

```
GPS IN TEAM SPORTS:
  Team vest worn during training/matches.
  GPS receivers: typically 10–18 Hz update rate.
  Accuracy: ±0.5–1.0 m positioning; ±0.1 m/s velocity.
  Data collected: total distance, high-speed running distance (>5.5 m/s),
                   sprint count, acceleration/deceleration counts,
                   training load (PlayerLoad = accelerometer-based).

GPS ACCURACY LIMITATIONS:
  Trees, buildings, stadiums obstruct satellite signal.
  In-stadium use: poor (limited sky view).
  Modern units: augmented with GNSS (multiple satellite systems), IMUs.
  Field sports (outdoor): generally acceptable accuracy.
  Indoor sports: GPS non-functional. Use local UWB (Ultra-Wideband) tracking instead.

  UWB TRACKING (indoor):
  Anchor nodes around the venue; tag worn by players.
  Accuracy: ±0.15–0.30 m positioning; real-time.
  Used for: basketball, volleyball, indoor soccer.
```

### Inertial Measurement Units

```
IMU (Inertial Measurement Unit):
  9-DOF sensor: accelerometer (3-axis) + gyroscope (3-axis) + magnetometer (3-axis).
  Measures: linear acceleration and angular velocity of the segment it's attached to.
  From IMU data: infer segment orientation, step count, impact load, jump height.

APPLICATIONS:
  Wrist IMU: consumer fitness (step count, sleep, heart rate via PPG).
  Torso IMU: training load in contact sports (rugby, football).
  Shoe pod IMU: running foot strike, cadence, ground contact time.
  Bat/racket IMU: swing speed, swing path.
  Mouthguard accelerometer: head impact detection (concussion research).

LIMITS:
  Drift: gyroscopes accumulate error over time; requires periodic correction.
  Orientation ambiguity: without external reference (GPS, magnetic north,
                          or video), only relative orientation measurable.
  Soft tissue artifact: sensor on skin moves slightly vs. underlying bone.
                        Creates noise in dynamic movements.
```

---

## Decision Cheat Sheet

| Question | Method | Data Type |
|---------|--------|-----------|
| How fast is the sprinter at top speed? | GPS + video | Kinematics |
| What force does the knee experience at landing? | Force plate + 3D motion capture | Kinetics (joint moment) |
| What is the athlete's jump height? | Force plate (impulse-momentum method) | Kinetics |
| What is the running stride frequency? | Video at 120fps or IMU shoe pod | Kinematics |
| What is the elbow valgus torque in pitching? | 3D motion capture + force plate | Kinetics |
| What is the athlete's weekly training load? | GPS PlayerLoad metric | Applied kinetics |
| How asymmetric is the athlete's gait? | Bilateral force plates or 2D video | Kinematics + kinetics |

---

## Common Confusion Points

**Kinematics describes; kinetics explains**: "the knee bent 30° at landing" is kinematics. "The knee joint experienced 200 Nm flexion moment at landing" is kinetics. You need both to understand injury mechanisms — the motion and the forces.

**GRF is not the same as impact force on joints**: the GRF is the ground-to-body force. The forces at internal joints are very different (and generally much larger than GRF due to muscle forces crossing joints). Running GRF = ~3× body weight; compressive force at the knee at midstance = ~4–8× body weight (quadriceps force added to GRF).

**Video at 30 fps is insufficient for fast movements**: a baseball pitch takes ~50ms from peak external rotation to ball release. At 30 fps, this is approximately 1.5 frames. You cannot analyze the mechanics from 1–2 frames. Minimum 120 fps for running; 500+ fps for anything above 10 m/s.

**Overstriding is not the same as heel striking**: overstriding means the foot contacts far in front of the center of mass, creating a braking impulse. A midfoot striker can also overstride. The landing position relative to CoM, not the foot strike pattern, is the key variable.

**Wearable training load metrics are not absolute**: PlayerLoad, arbitrary units, TRIMP — these are all relative metrics. An athlete's training load is high or low relative to their own recent history, not in absolute terms. A high PlayerLoad for one athlete may be moderate for another. Use within-athlete longitudinal comparison, not cross-athlete absolute values.
