# Robotics — Actuators

## The Big Picture

Actuators are where computation meets physics. Every joint torque from the controller
must be physically produced by a motor, drive, and transmission. The choice of actuator
determines what the robot can do.

```
+===========================================================================+
|                        ACTUATOR LANDSCAPE                                 |
+===========================================================================+
|                                                                           |
|  ELECTRIC                    HYDRAULIC              PNEUMATIC             |
|  =======                    =========              =========             |
|  DC brushed motor           Servo valve            PAM (McKibben)        |
|  BLDC motor (most common)   Linear hydraulic       Soft pneumatic        |
|  Stepper motor              Rotary hydraulic       Linear cylinder       |
|  Linear motor (direct)                                                   |
|                                                                           |
|  TRANSMISSION                                       NOVEL                 |
|  ============                                      ======                |
|  Spur / planetary gears                            Shape memory alloy    |
|  Harmonic drive (key for manipulation)             Dielectric elastomer  |
|  Ball screw                                        Piezoelectric         |
|  Cable / tendon drive                              Twisted coiled        |
|                                                                           |
|  SERVO DRIVE LOOP:                                                        |
|  Position ref -> [Position ctrl] -> Velocity ref                         |
|  Velocity ref -> [Velocity ctrl] -> Current ref                          |
|  Current ref  -> [Current ctrl]  -> Motor voltage/PWM (10-100 kHz)       |
|                                                                           |
+===========================================================================+
```

---

## DC Brushed Motors

The simplest electric motor. Found in cheap robots, toys, early servo systems.

### Physics

```
TORQUE:
  tau = Kt * I
  Kt: torque constant [N*m/A]
  I:  armature current [A]

BACK-EMF:
  V_emf = Ke * omega
  Ke: back-EMF constant [V/(rad/s)]
  omega: angular velocity [rad/s]

  Note: Kt = Ke (numerically, in SI units). Same constant.

CIRCUIT EQUATION:
  V = R * I + L * dI/dt + Ke * omega
  V:  applied voltage
  R:  armature resistance
  L:  armature inductance

  At steady-state (dI/dt = 0):
  I = (V - Ke * omega) / R
  tau = Kt * (V - Ke * omega) / R

SPEED-TORQUE CURVE:
  tau         Stall torque: tau_stall = Kt * V / R   (omega = 0)
  ^
  | *
  |  *
  |   *    Linear. Higher V shifts curve up.
  |    *
  +-------> omega
         No-load speed: omega_nl = V / Ke   (tau = 0)
```

### Limitations

```
BRUSHES: physical carbon brushes rub on commutator ring.
  Wear out: typical brush life 500-2000 hours.
  Arcing: brushes spark at high speed/voltage.
  Friction: brushes add static friction (cogging in precision positioning).
  Speed limit: centrifugal force limits brush contact at high rpm.

BRUSHED MOTORS STILL USED IN:
  Cheap hobbyist robots, RC servo actuators, window motors.
  NOT USED IN: modern industrial arms, cobots (BLDC is standard).
```

---

## BLDC Motors (Brushless DC)

The dominant actuator in modern robotics. Higher power density, longer life,
better thermal performance than brushed DC.

### Commutation

```
BRUSHLESS = no brushes. Commutation (switching current direction to produce
continuous torque) is done ELECTRONICALLY by the motor controller.

3-PHASE WINDINGS:
  Motor has 3 coil phases: U, V, W.
  ESC (Electronic Speed Controller) or servo drive energizes phases in sequence.

TRAPEZOIDAL COMMUTATION (6-step):
  Simpler, cheaper. Torque ripple.
  Measures rotor position via Hall-effect sensors (3 digital signals).
  Only 6 states per electrical revolution.

FIELD-ORIENTED CONTROL (FOC / sinusoidal commutation):
  The standard for precision robotics.
  Continuously aligns current vector with rotor flux for maximum torque.
  Requires high-resolution encoder (12+ bit).
  Smooth torque. Better efficiency. Higher bandwidth.
```

### FOC Deep Dive

```
FOC (Field-Oriented Control) = Park/Clarke transform + current control in d-q frame:

Step 1: MEASURE phase currents: Ia, Ib, Ic.

Step 2: CLARKE transform (abc -> alpha-beta, stationary frame):
  I_alpha = Ia
  I_beta  = (Ia + 2*Ib) / sqrt(3)

Step 3: PARK transform (alpha-beta -> d-q, rotating with rotor):
  Id = I_alpha * cos(theta) + I_beta * sin(theta)
  Iq = -I_alpha * sin(theta) + I_beta * cos(theta)

  theta: electrical rotor angle (from encoder or observer)
  Id: flux-producing component (set to 0 for max torque in PMSM)
  Iq: torque-producing component (the one you control)

Step 4: PID control on Id and Iq:
  Vd = PID(Id_ref - Id)
  Vq = PID(Iq_ref - Iq)     <- Iq_ref = torque_command / Kt

Step 5: INVERSE PARK + INVERSE CLARKE -> Va, Vb, Vc.

Step 6: SVPWM (Space Vector PWM) -> drive gate signals for 3-phase inverter.

BANDWIDTH: current loop typically 5-20 kHz bandwidth.
           This is the innermost loop, must be fastest.
```

### BLDC vs DC Comparison

| Property | DC Brushed | BLDC |
|----------|-----------|------|
| Commutation | Mechanical (brushes) | Electronic (FOC/ESC) |
| Maintenance | Brush replacement | None |
| Max speed | ~10,000 rpm (brush limit) | ~50,000+ rpm |
| Torque density | Good | 20-30% higher |
| Efficiency | 75-85% | 85-95% |
| Control complexity | Low (just voltage) | High (FOC required) |
| Cost | Low | Higher |
| Thermal | Rotor dissipates heat (bad) | Stator dissipates heat (better) |

---

## Stepper Motors

Fixed-angle rotation per electrical step. No encoder needed for position control
(open-loop). Common in 3D printers, CNC, cheap cartesian robots.

```
CHARACTERISTICS:
  200 steps/rev standard (1.8 deg/step). With microstepping: 3200+ steps/rev.
  Holding torque when powered: resistant to back-drive.
  Open-loop: no encoder needed. Miss steps = position error accumulates.
  Resonance frequency: 50-200 Hz (must avoid or use current reduction).
  Low speed: high torque. High speed: torque drops significantly.

NOT USED IN: high-performance manipulation.
USED IN: 3D printers, CNC routers, laser cutters.
```

---

## Servo Drive Architecture

The servo drive (amplifier) closes the current, velocity, and position control loops.

```
CASCADED CONTROL LOOPS:
=========================

  External planner/controller
           |
           | position setpoint (q_d)       -- e.g., 1 kHz from ROS
           v
  +------------------+
  |  POSITION LOOP   |
  +------------------+
   Kp*(q_d - q_measured) → velocity reference
           |
           | velocity setpoint (omega_d) — 1-4 kHz typically
           v
  +------------------+
  |  VELOCITY LOOP   |
  +------------------+
   Kp*(omega_d - omega) → current reference
           |
           | current setpoint (I_d) — 5-20 kHz
           v
  +------------------+
  |  CURRENT LOOP    |
  +------------------+
   FOC: Id/Iq PI + Park/Clarke + PWM
           |
  PWM to motor  (20-100 kHz switching)
           |
       Motor -> robot joint

KEY RULE: inner loop bandwidth must be 5-10x outer loop bandwidth.
  Current loop:   5-20 kHz
  Velocity loop:  500-4000 Hz
  Position loop:  100-1000 Hz
  Trajectory:     10-500 Hz
  Task planner:   1-50 Hz
```

### Fieldbuses

```
COMMUNICATION PROTOCOLS FOR SERVO DRIVES:

  EtherCAT (Ethernet for Control Automation Technology):
    Real-time Ethernet protocol. 1 kHz+ cycle times.
    Distributed clock synchronization. < 1 microsecond jitter.
    Standard in: KUKA, ABB, Franka, most industrial cobots.

  CANopen:
    Older. Slower (1 Mbit/s max). 500 Hz typical.
    Simpler, cheaper, widely supported.
    Used in: Kinova Gen3, many research arms.

  Modbus/RTU:
    Legacy. Very slow. Industrial PLCs.
    NOT for real-time servo control.

  PROFINET / SERCOS III:
    Industrial automation specific. Common in Siemens systems.
```

---

## Transmissions

Motors spin fast at low torque. Robot joints need slow at high torque.
Transmissions bridge this gap — and their properties dominate robot behavior.

### Gear Comparison

| Type | Ratio | Backlash | Efficiency | Cost | Used in |
|------|-------|----------|------------|------|---------|
| Spur gear | 1:3 to 1:10 per stage | High | 98%/stage | Low | Toys, simple robots |
| Planetary gear | 1:5 to 1:100 | Medium | 95-98% | Medium | Industrial drives |
| Harmonic drive | 1:30 to 1:200 | Near-zero | 70-90% | High | Cobots, surgical |
| Ball screw | N/A (linear) | Very low | 90-95% | Medium | Linear actuators |
| Cable drive | 1:5 to 1:50 | Low | 95-98% | Medium | Space robots |
| Cycloidal | 1:7 to 1:200 | Very low | 92-96% | High | High-torque robots |

### Harmonic Drive (Strain Wave Gear)

The standard transmission for precision robot manipulation. Understanding it matters.

```
HARMONIC DRIVE COMPONENTS:
  1. Wave Generator: elliptical cam with ball bearing on output shaft.
  2. Flexspline: thin-walled flexible gear cup (teeth on outside rim).
  3. Circular Spline: rigid ring gear with teeth on inside.

  Flexspline has 2 FEWER teeth than Circular Spline (e.g., 100 vs 102).

HOW IT WORKS:
  Wave Generator rotates (motor input).
  Flexspline deforms elastically into ellipse -- meshes with Circular Spline
  at 2 points (major axis of ellipse).
  Circular Spline is fixed to housing.
  Flexspline rotates SLOWLY (output) due to tooth count difference.

  GEAR RATIO:
  N = (C_teeth - F_teeth) / F_teeth   IF Circular Spline is fixed
  N = 50 for 100-tooth CS, 100-tooth FS (100 - 100 = 0... wrong)

  Correct formula: N = -F_teeth / (C_teeth - F_teeth)
  Example: FS=100, CS=102: N = -100/2 = -50:1 (negative = reverse direction)

  Typical ratios: 30:1 to 160:1 in a single stage.
  Common in: Franka Panda (40:1 to 160:1 per joint), KUKA iiwa.

PROPERTIES:
  Backlash: essentially zero (continuous mesh, no clearance).
  High reduction: 100:1 in compact package.
  Compliance: flexspline is flexible -> slight torsional springiness (< 1 arcmin).
  Efficiency: 65-90% (lower at high ratios due to flexing losses).
  Life: 10,000+ hours when properly lubricated.

WHY COMPLIANCE MATTERS:
  Slight torsional flexibility of harmonic drive + joint torque sensor =
  Series Elastic Actuator (SEA) behavior. Enables force sensing and
  safe force-limited operation. Critical for cobots.
```

### Cable Drives

```
CABLE DRIVE:
  Actuator (motor) is remote (base or proximal link).
  Cable transmits force to distal joint.
  Used in: lightweight arms (DARPA ARM), surgical robots (da Vinci),
           space robots (SRMS).

  ADVANTAGES:
    Motor weight at base -> low distal link inertia (faster, more backdrivable).
    No heavy joint gearboxes in the arm.

  DISADVANTAGES:
    Cable stretch -> compliance and backlash.
    Routing complexity.
    Cable fatigue and replacement.
    Pretension management.
```

---

## Series Elastic Actuators (SEA)

SEA = motor + gearbox + spring + link. The intentional spring changes everything.

```
SEA CONCEPT (Pratt & Williamson, 1995):

                 Motor + gearbox
                       |
                  spring (K_s)    <- intentional compliance
                       |
                  link output

FORCE MEASUREMENT:
  F = K_s * (theta_motor/N - q_link)   <- spring deflection * stiffness
  No separate F/T sensor needed. Spring IS the force sensor.
  Very accurate: K_s well-characterized, deflection measured by encoders.

BENEFITS:
  1. FORCE SENSING: accurate, low-cost force measurement.
  2. IMPEDANCE CONTROL: spring provides stable contact.
  3. ENERGY STORAGE: spring stores energy (useful for locomotion).
  4. SAFETY: spring absorbs impact (human-robot interaction).

COSTS:
  1. BANDWIDTH: spring limits force control bandwidth.
     omega_bandwidth ~ sqrt(K_s / I_reflected)
     Softer spring = safer but slower.
  2. COMPLEXITY: 2 encoders per joint (motor + output side).
  3. FOOTPRINT: spring adds length/mass.

USED IN: MIT Cheetah legs, Agility Robotics Digit, RoboImetics eCub.
```

---

## Hydraulic Actuators

Very high force density. Used in heavy robots and early Boston Dynamics Atlas.

```
HYDRAULIC SERVO SYSTEM:
  Pump (constant pressure supply) -> Servo valve -> Actuator

SERVO VALVE:
  Proportional valve: controls flow rate proportional to input current.
  High bandwidth: 50-200 Hz possible.
  Very precise: ~0.1% resolution.

FORCE DENSITY:
  Hydraulic: 1-10 kN from small cylinder.
  Electric: comparable power requires much larger motor.
  Force density (force/volume): hydraulic >> electric.
  Atlas (original): 28 hydraulic joints. Could lift 11 kg, survive falls.

DOWNSIDES:
  Leaks (oil contamination).
  High-pressure lines (safety hazard).
  Hydraulic power unit (HPU): heavy, loud, large.
  Thermal: oil temperature affects viscosity -> behavior changes.
  Not suitable for cleanroom, food, medical environments.

TREND: Atlas transitioned to electric in 2024. Most new humanoids are electric.
       Hydraulics remains superior for ultra-high-force field robots.
```

---

## Soft Actuators

Compliant by nature. Safe for human contact. Imprecise but interesting.

```
PNEUMATIC ARTIFICIAL MUSCLE (PAM, McKibben muscle):
  Braided mesh sleeve around inflatable bladder.
  Inflation -> sleeve shortens and expands -> pulling force.
  Mimics muscle (unidirectional force, needs antagonist pair).
  Compliance: excellent.
  Precision: poor (nonlinear, hysteresis).
  Used in: rehabilitation exoskeletons, soft grippers.

SOFT PNEUMATIC ACTUATORS (SPA):
  Silicone body with embedded chambers.
  Inflation causes programmed bending/twisting.
  Very safe (cannot injure).
  Used in: soft grippers (Soft Robotics Inc.), medical devices.

DIELECTRIC ELASTOMER ACTUATOR (DEA):
  Thin polymer film sandwiched between compliant electrodes.
  High voltage (1-10 kV) attracts electrodes -> film thins, expands laterally.
  Very high strain (>100%).
  Silent, lightweight, flexible.
  Challenges: requires high voltage, low force, limited lifetime.
  Research stage for most applications.
```

---

## Backdrivability

Backdrivability = can external forces move the joint when the motor is unpowered?

```
HIGH BACKDRIVABILITY (easy to backdrive):
  Direct-drive motors (no gearbox).
  Low-ratio gears.
  Cable drives.
  SEA (spring absorbs reflected inertia).

  PROS: safe for human contact (force limited by reflected inertia).
        Enables compliant behavior.
        Easy force estimation from current.
  CONS: motor must resist gravity torque (high continuous current).
        Position disturbances from external forces.

LOW BACKDRIVABILITY (hard to backdrive):
  Harmonic drives (ratio > 50:1).
  Worm gears (mechanically self-locking).
  High-ratio planetary gears.

  PROS: holds position against gravity with no power (or low current).
        Position robust to external disturbances.
  CONS: impact forces transmitted directly to motor.
        Unsafe in uncontrolled contact (arm breaks or person injured).
        Force control requires dedicated F/T sensor.

TRADE-OFF EXAMPLES:
  Industrial arm (KUKA KR): high gear ratio, not backdrivable.
    -> Position stiff, safe for heavy payloads, NOT safe for human contact.
  Cobot (Franka Panda): harmonic drive + torque sensing.
    -> Position stiff in normal operation, switches to compliant on contact.
  Research arm (MIT mini cheetah leg): low-ratio gear or direct drive.
    -> Highly backdrivable, can feel and respond to ground contacts.
```

---

## Decision Cheat Sheet

| Need | Actuator choice |
|------|----------------|
| Precision manipulation (6-DOF arm) | BLDC + harmonic drive + encoder |
| Fast, lightweight manipulation | BLDC + low-ratio gear or direct drive |
| Collaborative robot (safe contact) | BLDC + harmonic drive + joint torque sensor |
| Quadruped leg (fast, impact) | BLDC + low-ratio planetary + SEA |
| Heavy lift (industrial) | BLDC + high-ratio planetary, or hydraulic |
| High-force, field/harsh environment | Hydraulic |
| Soft gripper (safe, food) | Soft pneumatic actuator |
| Rehabilitation exoskeleton | PAM or SEA |
| 3D printer / CNC | Stepper motor (cheap, open-loop fine) |
| Joint on EtherCAT network | Servo drive with EtherCAT interface |

---

## Common Confusion Points

**BLDC vs PMSM: same thing, different naming convention**
BLDC (Brushless DC): engineering term, trapezoidal back-EMF (or sinusoidal with FOC).
PMSM (Permanent Magnet Synchronous Motor): more physics-accurate term, sinusoidal.
In robotics, people say BLDC and usually mean FOC-controlled PMSM. Same hardware.

**Gear ratio does not affect speed-torque product**
Power = torque * angular_velocity. Gearbox conserves power (approximately):
tau_out = N * tau_motor, omega_out = omega_motor / N.
tau * omega = constant (minus friction losses). Gear ratio trades speed for torque,
it does not create power. Motor rated power is the fundamental limit.

**Harmonic drive efficiency drops at light loads**
Harmonic drive efficiency is 65-90%, but efficiency is load-dependent. At partial load
(< 30% rated), efficiency can drop to 50-60% because flexspline elastic hysteresis is
still high even at low load. Budget power accordingly for robot duty cycles.

**"Direct drive" does not mean no transmission**
Direct drive means motor directly coupled to joint (ratio 1:1 or small). The motor
must be physically large to produce joint torque directly. Examples: large radial-flux
BLDC motors in MIT mini cheetah, T-Motor U10+ motors used in various research arms.
Torque density (N*m/kg) is the key spec -- these motors have very high torque density.

**SEA bandwidth limitation is physical, not solvable by better control**
SEA force bandwidth omega_b ~ sqrt(K_s/I_reflected). Softer spring = more safety = less
bandwidth. Stiffer spring = more bandwidth = less safety. There is no getting around this.
Variable stiffness actuators (VSA) attempt to switch between stiff and soft dynamically,
but add complexity. For most cobots: accept ~50-100 Hz force bandwidth as the practical limit.
