# MEMS and NEMS: Accelerometers, Pressure Sensors, Resonators, Fabrication

## The Big Picture

MEMS (Microelectromechanical Systems) integrate mechanical structures with electronics
at the micrometer scale. NEMS (Nanoelectromechanical Systems) extend this to sub-100 nm.
MEMS is a mature industry; NEMS is largely still research.

```
MEMS/NEMS LANDSCAPE
====================

SIZE SCALE:
  1 mm   Package (die + wire bonds + housing)
  100 um MEMS membrane, proof mass, comb structure
  10 um  Comb fingers, flexures, beam width
  1 um   Thin film polysilicon, SiO2 layer
  100 nm <- NEMS begins here
  10 nm  Carbon nanotube resonator
  1 nm   Single-molecule switch (NEMS)

MARKET (2025):
  MEMS: ~$20B global market
  Consumer (phones): accelerometers, gyroscopes, microphones, pressure sensors
  Medical: pressure sensors, drug delivery actuators, hearing aids
  Automotive: airbag accelerometers, yaw sensors, TPMS pressure
  Industrial: IMUs, flow sensors, gas sensors
  Optical: DLP projector mirrors (Texas Instruments)
  RF: MEMS switches, resonators, filters

NEMS:
  Primarily research; few commercial products
  CNT resonators, graphene resonators
  NEMS memory switches (no gate leakage -- key advantage)
```

---

## MEMS Fabrication Processes

### Surface Micromachining

Surface micromachining builds 3D structures by depositing and selectively etching
thin films on top of a substrate. The key concept: sacrificial layers.

```
SURFACE MICROMACHINING PROCESS FLOW
=====================================

Substrate: Si wafer

STEP 1: Deposit and pattern structural layer 1
  Thermal SiO2 (1 um) or LPCVD Si3N4 -- electrical isolation
  Pattern by photolithography + RIE etch

STEP 2: Deposit sacrificial layer
  LPCVD SiO2 (PSG -- phosphosilicate glass, easier to etch)
  Thickness = gap between structure and substrate (~2 um)
  This layer will be removed at the end -- creates the air gap

STEP 3: Etch anchor holes in sacrificial layer
  Photolithography + BOE (buffered oxide etch)
  These holes allow structural layer to contact substrate

STEP 4: Deposit structural layer (polysilicon)
  LPCVD polysilicon at 620 C, ~2 um thick
  Anneal at 1000 C: stress relief (otherwise structure bows)

STEP 5: Pattern structural layer
  Photolithography + RIE etch
  Define: beams, comb fingers, membranes, anchors

STEP 6: RELEASE ETCH (critical step)
  HF vapor or liquid HF etches SiO2 but NOT polysilicon
  Sacrificial SiO2 dissolves, structure floats free
  Result: freestanding polysilicon structures suspended over Si substrate

  [substrate] [SiO2 sacrificial]   [substrate]  (gap)
  [polysilicon structure]       =>  [polysilicon] <- RELEASED
  (before release)                  (after release)

STICTION RISK:
  During release, surface tension of liquid pulls structure to substrate
  If they touch: van der Waals + capillary adhesion sticks them permanently
  Solutions:
    - Supercritical CO2 drying (no liquid-vapor surface tension)
    - Anti-stiction coatings (self-assembled monolayers: HMDS, FDTS)
    - Design: bumpers limit contact area
    - HF vapor release (avoids liquid phase entirely)
```

### Bulk Micromachining

Bulk micromachining removes large volumes of the substrate itself, not just thin films.

```
BULK MICROMACHINING METHODS
============================

WET ETCHING -- KOH (potassium hydroxide):
  Anisotropic: etches Si {100} planes 100-400x faster than {111} planes
  Creates V-grooves and pyramidal cavities with 54.7-degree walls
  Si wafer orientation determines geometry

  [100] wafer:
  +---------------+
  |   Si (100)    |
  |               |
  | \           / |  <- {111} planes (slow etch)
  |  \         /  |
  |   \       /   |
  |    -------    |  <- bottom (100) plane
  +---------------+

  KOH etch of (100) Si: forms perfect pyramid or V-groove
  Etch rate (100): ~1-2 um/min at 80 C, KOH 30%
  Selectivity: Si over SiO2 ~100:1; SiO2 used as etch mask

  Applications: inkjet nozzle plates, through-wafer vias, pressure sensor diaphragms

DEEP REACTIVE ION ETCHING (DRIE) -- Bosch Process:
  Alternating etch and passivation cycles (patented by Bosch, 1994)

  ETCH CYCLE:
    SF6 plasma: isotropic Si etch (all directions)
    Duration: 5-15 seconds

  PASSIVATION CYCLE:
    C4F8 plasma: deposits fluoropolymer on all surfaces
    Duration: 5-15 seconds

  Net result: vertical walls with ~90-degree angle, scalloping on sidewalls (~100 nm)
  Aspect ratio: 30:1 to 50:1 easily; 100:1 with optimization
  Depth: 10 um to >500 um possible
  Rate: 1-15 um/min depending on area and machine

  Characteristic "Bosch scallops":
    Sidewall shows ~100-300 nm scallop ripple (from alternating cycles)
    Visible in SEM; can be smoothed with O2 oxidation + HF strip if needed

  Applications:
    Inertial sensors (proof mass release trenches)
    Through-silicon vias (TSV)
    MEMS gyroscope structures
    Pressure sensor diaphragm
```

---

## Key MEMS Devices

### MEMS Accelerometer: Analog Devices ADXL Series

The ADXL accelerometer (invented at Analog Devices, 1991) is in essentially every
smartphone, gaming controller, vehicle airbag system, and hard drive.

```
ADXL ACCELEROMETER STRUCTURE
==============================

Plan view (top-down):
                    ANCHOR      ANCHOR
                      |          |
    +--------+    +---+----------+---+    +--------+
    | fixed  |----| spring beam  |---|----| fixed  |
    | finger |    +---+----------+---+    | finger |
    +--------+        | PROOF   |        +--------+
    +--------+        |  MASS   |        +--------+
    | fixed  |--------| (large  |--------| fixed  |
    | finger |        |  poly-  |        | finger |
    +--------+        |  Si     |        +--------+
    +--------+        | plate)  |        +--------+
    | fixed  |--------+----+----+--------| fixed  |
    | finger |             |             | finger |
    +--------+         MOVABLE           +--------+
                        COMB FINGERS

Operation:
  Proof mass suspended by spring beams (folded flexure design)
  Acceleration -> proof mass moves relative to fixed anchors
  Moving comb fingers interdigitate with fixed comb fingers
  Capacitance changes: C = epsilon * A / d
  delta_C = epsilon * A * delta_d / d^2

  Sensitivity: delta_C / delta_d = epsilon * A / d^2
  For ADXL: finger gap ~2 um, finger length 100 um, 50+ finger pairs
  Resolution: ~1 mg (mg = 10^-3 * 9.8 m/s^2) at 1 Hz bandwidth

  Force balance operation (closed-loop):
    Electrostatic force applied to proof mass to keep it centered
    Applied force = measured acceleration * mass
    Better linearity, wider dynamic range than open-loop

FABRICATION:
  2 um thick polysilicon structural layer
  Released by HF etch of sacrificial PSG
  Integrated CMOS circuitry for C/V conversion (sigma-delta ADC)
  Combined MEMS + CMOS in same chip (iMEMS process)
```

### MEMS Gyroscope (Coriolis Effect)

```
MEMS GYROSCOPE PRINCIPLE
=========================

Coriolis effect: a mass moving with velocity v in a rotating frame
experiences a force perpendicular to v:

  F_Coriolis = 2 * m * (v x Omega)

where Omega = rotation rate vector

MEMS implementation:
  Drive mass into resonance (vibrate at ~10-50 kHz)
  Rotation -> Coriolis force -> out-of-plane or transverse vibration
  Sense this perpendicular motion capacitively

  Drive axis: x (electrostatic comb drive)
  Input rotation: about z axis (yaw)
  Coriolis force: along y axis (sense)

TUNING FORK GYROSCOPE:
         A ------> oscillates in X direction
        / \
       /   \
  ----/     \----  (pivot)
       \   /
        \ /
         B <------ oscillates in X direction (antiphase to A)

  When device rotates about Z: A and B feel Coriolis forces in +Y and -Y
  Differential sensing cancels common-mode; measures Coriolis only

Key specs (consumer grade, e.g., InvenSense MPU-6050):
  Full scale: +/- 2000 deg/s
  Sensitivity: 16.4 LSB per deg/s
  Noise density: 0.005 deg/s/sqrt(Hz)
  Power: 3.6 mW

  Automotive/tactical grade: 0.01 deg/hr bias stability (much harder)
```

### MEMS Pressure Sensor

```
MEMS PRESSURE SENSOR
=====================

PIEZORESISTIVE TYPE:
  Thin Si membrane (5-50 um) etched by KOH bulk micromachining
  Four piezoresistors diffused into membrane edges (max stress locations)
  Wheatstone bridge: two resistors at max tensile stress, two at max compressive
  Bridge imbalance voltage proportional to pressure

  Membrane cross-section:
  +----------------------------------------+
  |  Si bulk (handle wafer)                |
  |         +----------------+             |
  |         |  cavity (etch) |             |
  |         +----------------+             |
  | [membrane: 10 um thin, max stress here]|
  +----------------------------------------+

  Gauge pressure: cavity open to atmosphere, measures differential
  Absolute pressure: cavity sealed in vacuum, measures absolute
  Differential: two ports, measures difference

  Application: barometric altimeter in phone (5 Pa = ~42 cm altitude resolution)

CAPACITIVE TYPE:
  Membrane forms one plate of capacitor
  Fixed plate below membrane
  Pressure deflects membrane -> changes gap -> changes capacitance
  Less sensitive to temperature than piezoresistive
  Used in: MEMS microphones (iPhone, AirPods)
```

### DLP Projector: MEMS Micromirror Array

Texas Instruments Digital Light Processing (DLP) uses a 2D array of MEMS mirrors:

```
DMD (Digital Micromirror Device)
==================================

Each pixel: 10.8 um x 10.8 um aluminum mirror
Tilts +12 or -12 degrees (on/off state)
Array: 1920 x 1080 = 2,073,600 mirrors for 1080p
Switching time: ~20 microseconds

Mirror structure:
  Mirror plate: aluminum (reflective)
    |
  Hinge: thin torsional beam (spring)
    |
  Yoke + address electrodes (apply voltage -> electrostatic torque)
    |
  CMOS memory cell (SRAM) -- stores desired state

Operation:
  SRAM bit -> address voltage -> electrostatic torque -> tilt -> reflect light to screen
  Grayscale: time-domain modulation (mirror tilted on for fraction of frame period)
  Color: rotating color wheel (sequential R/G/B) or 3-chip system (parallel R/G/B)

Reliability: 10^12 switching cycles (proven in 30+ years of products)
Stiction challenge: mirror must tilt and STOP without sticking to landing electrode
Solution: spring tips on landing electrodes, anti-stiction coating
```

---

## NEMS: Nanoelectromechanical Systems

```
NEMS OVERVIEW
==============

NEMS = mechanical structures at <100 nm where:
  - Mass becomes very small (fg to ag range)
  - Resonant frequency becomes very high (MHz to GHz)
  - Quantum effects begin to matter (phonon quantization at <1 K)

CNT RESONATOR:
  Single-wall CNT suspended between two electrodes
  Length: 0.5-5 um; diameter: 1-2 nm
  Resonant frequency: 1-4 GHz
  Quality factor Q: 1000-10000 at room temperature
  Mass sensitivity: 10^-22 g (can detect single atom adsorption)
  Operation: gate voltage modulates CNT tension; current through CNT
  measured as a function of drive frequency; resonance = mass sensor

GRAPHENE RESONATOR:
  Suspended graphene sheet (nm thick, um^2 area)
  Resonant frequency: 10 MHz - 1 GHz
  Mass sensitivity approaching single proton detection
  Challenge: Q degradation from edge defects and substrate interactions

NEMS SWITCH:
  Mechanical switch at nm scale
  Gate pulls contact beam into contact with drain
  Advantage: NO gate leakage current (hard contact, no tunnel current)
  Disadvantage: speed, stiction, limited cycle life
  Application: ultralow-power logic; memory cells (non-volatile)
  Status: research, not in production
```

---

## Fabrication Challenges and Yield

```
MEMS FABRICATION CHALLENGES
=============================

1. RELEASE ETCH STICTION (worst yield killer):
   Problem: during HF release, surface tension collapses structures
   Solution hierarchy:
     Level 1: Supercritical CO2 drying (no surface tension)
     Level 2: Freeze-sublimation (freeze liquid, sublime ice)
     Level 3: Vapor HF (no liquid phase)
     Level 4: Anti-stiction SAM coating post-release

2. RESIDUAL STRESS IN THIN FILMS:
   Deposited polysilicon has ~200 MPa compressive stress
   If not annealed -> buckled beams
   Solution: anneal at 1000 C in N2 (stress relief)
   Stress gradient (varies through thickness): causes out-of-plane curl
   Solution: optimize deposition conditions, measure by cantilever deflection

3. MISMATCH WITH IC PROCESSING:
   MEMS anneal (1000 C) after CMOS kill transistors
   Solutions:
     a) MEMS before CMOS (rare)
     b) Low-temperature MEMS (SiGe at 450 C -- fits in backend)
     c) Separate chips + wire bond or wafer-level packaging

4. WAFER-LEVEL PACKAGING:
   Protect released MEMS from particles, humidity, damage
   Sealed cavity (vacuum or specific gas) needed for resonators
   Methods: wafer bonding (anodic, eutectic, fusion), thin-film cap

TYPICAL MEMS YIELD:
  Modern smartphone accelerometer: >99.9% die yield (mature process)
  MEMS gyroscope: 95-99%
  Research NEMS CNT device: 10-50% (very sensitive to process)
```

---

## Decision Cheat Sheet

| You are making... | Fabrication approach |
|-------------------|---------------------|
| Inertial sensor (accelerometer/gyroscope) | Surface micromachining, polysilicon + sacrificial SiO2 |
| Pressure sensor | Bulk micromachining (KOH) + piezoresistor or capacitive |
| MEMS microphone | Surface micro + capacitive membrane |
| DLP-style mirror array | Surface micro + rotational hinge |
| Deep trench or high-aspect structure | DRIE (Bosch process) |
| MEMS for optical (IR sensor) | Bulk or surface micro, often on SiN membrane |
| Fluidic channel (microfluidics) | SU-8 photopolymer + PDMS soft lithography |
| CNT resonator (research) | CVD CNT growth + EBL contacts |

---

## Common Confusion Points

**"MEMS uses the same process as ICs."** Partially. MEMS uses similar equipment (CVD,
lithography, RIE) but adds wet etching, sacrificial layers, and release steps that
standard CMOS processes don't have. Combining them on one chip is non-trivial
(temperature incompatibility between MEMS anneal and CMOS front-end).

**"The ADXL accelerometer works like a spring-mass system."** It does, but you read it
capacitively, not as a displacement. The electronics close the loop, applying a restoring
force to keep the mass centered and reading the applied force rather than displacement.
This is closed-loop (force-balance) operation, not open-loop.

**"NEMS is just smaller MEMS."** Not entirely. At NEMS scale, quantum effects become
relevant (Casimir force, phonon quantization at mK temperature), and classical detection
methods (capacitance) fail because the capacitance of a 10 nm gap, 100 nm beam is ~10^-19 F
(attofared range -- below most circuit noise levels). NEMS requires fundamentally different
transduction methods (optical, RF mixing, piezoelectric).

**"HF release is simple."** HF is the most dangerous reagent in a MEMS lab (produces
vapor that penetrates skin and chelates calcium in bones -- 5% body surface area
exposure can be fatal). HF vapor release requires full PPE and chemical engineering
controls. Not casual.
