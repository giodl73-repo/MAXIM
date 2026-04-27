# Robotics — Robot Control

## The Big Picture

Control is what closes the loop between the desired trajectory and the actual motion.
Every other subsystem (kinematics, dynamics, planning) feeds into the control layer.

```
+===========================================================================+
|                         ROBOT CONTROL LANDSCAPE                           |
+===========================================================================+
|                                                                           |
|  HIERARCHY:                                                               |
|                                                                           |
|  Task Planner -------> desired task (symbolic)                            |
|       |                                                                   |
|  Trajectory Planner --> q_d(t), q_dot_d(t), q_ddot_d(t)                 |
|       |                                                                   |
|  CONTROLLER <---------- state feedback: q, q_dot                         |
|       |                                                                   |
|  Actuators -----------> torques/forces/currents                           |
|       |                                                                   |
|  Plant (robot) -------> actual motion q(t)                               |
|       |                                                                   |
|  Sensors -------------> q, q_dot (back to controller)                    |
|                                                                           |
|  JOINT SPACE CONTROL      OPERATIONAL SPACE CONTROL                       |
|  ====================     ========================                        |
|  PID, computed-torque     Cartesian control (x,y,z)                      |
|  Works in q directly      Uses Jacobian                                   |
|                                                                           |
|  FREE SPACE CONTROL       CONTACT / FORCE CONTROL                         |
|  ===================      ======================                          |
|  Position tracking        Impedance control                               |
|  Trajectory following     Force/torque regulation                         |
|                           Hybrid position-force                            |
|                                                                           |
+===========================================================================+
```

---

## PID Control

The most widely deployed controller in all of engineering. Robot joint control is no
exception. Every industrial servo runs PID (or PI for velocity loops).

### PID Structure

```
  PID feedback loop:

  reference r(t) ─→ (sum) ─→ e(t) ─┬─→ P ──→
                     ↑              ├─→ I ──→ (sum) ──→ u(t) ──→ Plant ──→ y(t)
                     │              └─→ D ──→             |
                     └──────────────── y(t) ──────────────┘

        error: e(t) = r(t) - y(t)
        r(t): reference (desired q_d)
        y(t): measurement (actual q)

u(t) = Kp * e(t)  +  Ki * integral(e) dt  +  Kd * de/dt

  Kp: proportional gain (stiffness) -- drives error toward 0
  Ki: integral gain   -- eliminates steady-state error
  Kd: derivative gain -- damps oscillations (velocity feedback)

DISCRETE IMPLEMENTATION:
  u[k] = Kp * e[k]  +  Ki * sum(e) * dt  +  Kd * (e[k] - e[k-1]) / dt
```

### PID Tuning

```
ZIEGLER-NICHOLS (frequency-domain):
  1. Set Ki = Kd = 0.
  2. Increase Kp until sustained oscillation: Kp = Ku (ultimate gain).
  3. Record period of oscillation: Tu.
  4. ZN table:
     P   controller:  Kp = 0.5 * Ku
     PI  controller:  Kp = 0.45 * Ku, Ki = 1.2/Tu
     PID controller:  Kp = 0.6 * Ku,  Ki = 2/Tu, Kd = Tu/8

MODEL-BASED TUNING:
  If joint dynamic model is known (mass, friction):
    Kp = desired_bandwidth^2 * I_effective
    Kd = 2 * zeta * sqrt(Kp * I_effective)
  Set zeta = 0.7 for good transient response.

PRACTICAL NOTES:
  For robot joints: use Kd sparingly (encoder noise amplified by derivative).
  "Derivative kick": sudden step reference change gives infinite Kd output.
  Fix: use "derivative on measurement" (Kd * dy/dt, not Kd * de/dt).
  Integral windup: clamp integrator when saturated.
```

### Windup Prevention

```
INTEGRAL WINDUP:
  During large tracking error (startup, obstacles), integral accumulates large value.
  When error recovers, integrator must unwind -> overshoot.

FIXES:
  1. Clamping: only integrate when |u| < u_max.
  2. Back-calculation: u_feedback = u_sat - u_unsaturated -> drives integrator toward 0.
  3. Conditional integration: disable integrator unless error < threshold.

  Industrial servo drives handle this internally.
  In ROS 2 control: controlled_joints pid_gains parameter block.
```

---

## Feedforward Control

PID alone is reactive. Adding feedforward from the dynamics model dramatically reduces
tracking error without increasing gains (which risks instability).

```
u = u_ff + u_fb

u_ff = G(q_d)                  <- gravity compensation (always useful)
     or M(q_d)*q_ddot_d + C(q_d,q_dot_d)*q_dot_d + G(q_d)  <- full model

u_fb = PID(q_d - q)            <- error correction only

With feedforward:
  PID only needs to correct MODEL ERRORS and DISTURBANCES.
  Can use lower PID gains -> more stable, less noise amplification.
  Gravity compensation alone reduces required Kp by 5-10x for vertical joints.
```

---

## Computed-Torque Control (Inverse Dynamics Control)

The "perfect" model-based controller. If the dynamics model is exact, it achieves
perfect decoupling and reduces each joint to a linear double integrator.

### Derivation

```
ROBOT EOM: M(q) q_ddot + C(q,q_dot) q_dot + G(q) = tau

Let: tau = M(q) * a + C(q,q_dot) q_dot + G(q)
              ^
              desired acceleration

Then: M(q) q_ddot + C(q,q_dot) q_dot + G(q)
    = M(q) * a   + C(q,q_dot) q_dot + G(q)
   => q_ddot = a

Choose: a = q_ddot_d + Kd*(q_dot_d - q_dot) + Kp*(q_d - q)

Then the tracking error e = q_d - q satisfies:
  e_ddot + Kd * e_dot + Kp * e = 0

This is a LINEAR stable ODE! Choose Kd, Kp for desired damping/bandwidth.
```

### Block Diagram

```
q_d, q_dot_d, q_ddot_d
         |
         v
  +-----------+      tau_ff = M(q)*a_des + C*q_dot + G
  | COMPUTED  |---> tau = tau_ff
  | TORQUE    |
  | CONTROL   |
  +-----------+
         ^           a_des = q_ddot_d + Kd*(q_dot_d - q_dot) + Kp*(q_d - q)
         |
  q, q_dot (measured)
```

### Practical Considerations

```
MODEL ACCURACY: Computed-torque is sensitive to model errors.
  10% mass error -> 10% residual force -> PID must compensate.
  For good cobots: model accuracy is ~95%, so residuals are small.
  For unknown payloads: must either estimate online or use robust control.

COMPUTATIONAL COST: M(q), C(q,q_dot), G(q) via Newton-Euler at 1 kHz.
  6-DOF arm: ~microseconds. Fine for modern CPU cores.
  Embedded MCU: optimize with fixed-point arithmetic.

SINGULARITIES: M(q)^{-1} ill-conditioned near singularities.
  Add regularization: M_reg = M + epsilon * I.
```

---

## Operational-Space Control

Joint-space control tracks joint angles. Operational-space control (Khatib, 1987)
tracks Cartesian end-effector pose directly.

```
OPERATIONAL SPACE (task space):
  x_EE = [px, py, pz, roll, pitch, yaw]   <- end-effector pose (6D)

  Cartesian error:
  e_x = x_d - x_EE

  Cartesian acceleration desired:
  a_x = x_ddot_d + Kd*(x_dot_d - x_dot_EE) + Kp*(x_d - x_EE)

  Map to joint torques via Jacobian:
  tau = J^T * Lambda * a_x  +  C*q_dot  +  G  (+ null-space term)

  where Lambda = (J M^{-1} J^T)^{-1}   <- operational space inertia matrix
  (accounts for how joint inertia appears in Cartesian space)

NULL-SPACE PROJECTION:
  tau = tau_task  +  (I - J^T J^{+T}) * tau_null
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    projects null-space torque so it doesn't affect EE motion

  tau_null can be used for: joint limit avoidance, posture optimization,
  secondary task (e.g., keep shoulder joint near neutral).
```

---

## Impedance Control

Impedance control is the right framework for tasks involving contact.
Instead of commanding position or force, it defines the desired mechanical behavior
of the robot: how it responds to forces.

### Mechanical Impedance Concept

```
IMPEDANCE: relationship between force and motion.

  F = Z * v   (force = impedance * velocity)

  OR in s-domain:
  Z(s) = M_d * s^2 + D_d * s + K_d
           ^            ^        ^
           virtual mass  virtual  virtual
           (inertia)     damping  stiffness

IMPEDANCE CONTROL:
  Robot behaves as if it WERE a mass-spring-damper system:
  F_contact = M_d*(x_ddot_d - x_ddot) + D_d*(x_dot_d - x_dot) + K_d*(x_d - x)

WHY THIS MATTERS FOR CONTACT:
  FREE SPACE: high stiffness K_d -> tracks position precisely.
  CONTACT: lower K_d -> complies with surface, absorbs contact forces.
           High K_d + contact = large forces -> breaks parts or hurts humans.

  Assembly robots use K_d~= 1000 N/m for insertion.
  Surgical robots use K_d ~= 100-500 N/m for tissue safety.
  Physical therapy robots: even lower (patient safety).
```

### Implementation

```
IMPEDANCE CONTROL LAW (Cartesian):
  tau = J^T * (M_d * a_x_desired  +  D_d * (x_dot_d - x_dot)  +  K_d * (x_d - x))
         +  C*q_dot  +  G

ADMITTANCE CONTROL (dual of impedance):
  Measures force F_contact.
  Computes desired modification to reference trajectory:
  M_d * x_ddot_desired + D_d * x_dot_desired + K_d * x_desired = F_contact

  Solve for x_desired -> feed to position controller.

CHOICE:
  Impedance: use with joint-torque-controlled robots (Franka, iiwa, cobots).
  Admittance: use with position-controlled robots that have force sensors.
```

---

## Force Control

When you need to explicitly regulate contact force (not just comply softly).

### Hybrid Position-Force Control

```
HYBRID CONTROL (Raibert & Craig, 1981):
  Partition Cartesian DOF into POSITION-controlled and FORCE-controlled directions.

  Example: robot pushing on a surface:
  +----------+--------------------------------+
  | Direction| Control mode                   |
  +----------+--------------------------------+
  | x, y     | POSITION (move along surface) |
  | z        | FORCE (push with 5 N)         |
  | rz       | POSITION (tool orientation)   |
  +----------+--------------------------------+

  Selection matrix S:
    S = diag([0, 0, 1, 0, 0, 0])   <- select z for force control
    (I - S) = diag([1, 1, 0, 1, 1, 1])  <- others position controlled

  Force error: e_F = F_d - F_measured
  tau_force = J^T * (I-S)^T * (Kp_F * e_F + Ki_F * integral(e_F))

  LIMITATION: surface contact must be stiff enough that force sensor reads correctly.
              Works well for: grinding, polishing, surface following, assembly insertion.
```

---

## Whole-Body Control (Legged Robots)

For legged robots (quadrupeds, humanoids), control must simultaneously manage:
- Body pose and gait
- Contact forces (legs must not slip)
- Multiple tasks with priority ordering

### Quadratic Programming (QP) for WBC

```
LEGGED ROBOT STATE:
  q = [floating base pose, leg joint angles]
  EOM: M(q)*q_ddot + b(q,q_dot) = tau + J_c^T * F_c

  where J_c: contact Jacobian, F_c: contact forces

WBC as QP:
  minimize:   sum_i ||J_i * q_ddot - a_i_desired||^2_{W_i}   (task objectives)
  subject to:
    Dynamics: M*q_ddot = tau + J_c^T * F_c - b  (physical consistency)
    Friction cones: F_c in friction_cone(mu, normal)  (no slip)
    Torque limits: tau_min <= tau <= tau_max
    Contact: J_c * q_ddot + J_c_dot * q_dot = 0  (rigid contact)

  Solve QP at 1 kHz. Outputs tau (joint torques).

TASK HIERARCHY (priority):
  Priority 1: maintain balance (do not fall)
  Priority 2: follow desired body velocity
  Priority 3: track foot placements
  Priority 4: maintain default posture

  Lower priority tasks only use the NULL SPACE of higher priority tasks.
  Same null-space projection concept as operational-space control.
```

---

## Adaptive Control

When the model is uncertain or changes over time (different payloads, wear).

### Model Reference Adaptive Control (MRAC)

```
MRAC STRUCTURE:
  Reference model: defines desired closed-loop behavior
    M_ref: x_ddot_ref + ... = commanded trajectory

  Adaptive law: updates controller parameters online to match reference model.
    Parameter update: theta_dot = -Gamma * e * phi
    where:
      Gamma: adaptation gain matrix
      e: tracking error (actual vs reference model output)
      phi: regression vector (depends on current state)

APPLICATION TO ROBOTS:
  EOM: M(q)*q_ddot + C*q_dot + G = tau
  Write as: tau = phi(q,q_dot,q_ddot)^T * theta
            phi: regressor (measurable functions)
            theta: inertial parameters (unknown, to be estimated)

  Adaptive law: theta_hat_dot = -Gamma * phi * s
                s: filtered error s = e_dot + Lambda * e

RESULT:
  Proven globally stable (Lyapunov analysis).
  theta_hat -> theta as long as robot is persistently excited.
  Handles unknown payloads (mass, COM offset) online.
```

---

## Learning-Based Control

Modern trend: replace or augment model-based control with learned policies.

```
RESIDUAL RL:
  Controller = model_based_controller + learned_residual_policy
  Residual corrects for model errors.
  Easier to train (model does most of work, RL only learns corrections).
  More sample-efficient than pure RL.

NEURAL NETWORK POLICY AS CONTROLLER:
  pi(o_t) = a_t    (observation -> action directly)
  Trained by PPO, SAC, or imitation learning.
  Runs at 50-1000 Hz on GPU or dedicated ASIC.

  Examples: Isaac Lab (NVIDIA) trains locomotion policies at millions of Hz.
            These run on Spot quadruped, Unitree Go2.

LIMITATIONS:
  No formal stability guarantees.
  Behavior outside training distribution can be unsafe.
  Interpretability is low.
  Certification for safety-critical applications (surgery, autonomous vehicles)
  requires either formal verification or extensive testing.
```

---

## Control Architecture in ROS 2

```
ros2_control ARCHITECTURE:

  +------------------+
  | ros2_control     |
  | (controller_mgr) |
  +------------------+
   Framework for writing hardware-agnostic controllers.
          |
  +------------------+
  | Controllers      |
  | JointPositionCtl |
  | JointEffortCtl   |
  | ForwardCtl       |
  +------------------+
   Plugins implementing a controller interface.
   JointTrajectoryController: position control with trajectory interpolation.
   ForwardCommandController: pass-through torques.
   CartesianMotionController (Franka): Cartesian PID.
          |
  +------------------+
  | Hardware Iface   |
  | (robot driver)   |
  +------------------+
   URDF-defined joint interfaces: position, velocity, effort.
   Real or simulated (Gazebo plugin).
          |
      Real robot or Gazebo/Isaac Sim
```

---

## Decision Cheat Sheet

| Task | Controller choice |
|------|-----------------|
| Joint position tracking, simple | PID per joint |
| Joint position tracking, fast/precise | PID + gravity compensation feedforward |
| Full trajectory tracking | Computed-torque control (inverse dynamics) |
| Cartesian position tracking | Operational-space control |
| Robot interacting with environment | Impedance control |
| Explicit force regulation (polishing, grinding) | Hybrid position-force control |
| Unknown payload, adapts online | Adaptive control (MRAC) |
| Legged robot balance + tasks | Whole-body control (QP) |
| Hard-to-model nonlinear system | Learning-based (RL + sim-to-real) |
| ROS 2 robot | ros2_control + JointTrajectoryController |
| Franka arm | libfranka + FCI + CartesianImpedanceController |

---

## Common Confusion Points

**PID derivative gain amplifies noise**
Kd * de/dt differentiates the encoder signal. Encoder noise is roughly white.
Differentiating white noise gives white noise with infinite bandwidth. This shows
up as high-frequency torque chattering. Always low-pass filter encoder velocity
estimate (e.g., first-order filter, or use state estimator).

**Impedance vs admittance: not the same**
Impedance control = robot has torque control (servo drive in torque mode). The
controller outputs torques directly. Admittance control = robot has position control.
The controller computes modified position setpoints based on measured force.
Cobots (Franka, iiwa) support impedance. Most industrial arms only support admittance
(they are position-controlled, but have a F/T sensor at the wrist).

**Computed-torque needs real-time dynamics**
Computing M(q), C(q,q_dot), G(q) at 1 kHz requires fast Newton-Euler. For a 6-DOF
arm this is ~100 microseconds on a modern CPU. For 7-DOF with 1 kHz loop: fine.
For humanoids with 30+ DOF: need dedicated compute (GPUs or ASIC).

**Whole-body control QP is not always feasible**
The QP may be infeasible when constraints are contradictory (e.g., robot is
physically incapable of satisfying all tasks while maintaining balance). Controllers
must handle infeasibility gracefully (relax lower-priority tasks, report failure
to the task planner). Stack-of-tasks libraries handle this via soft constraints.

**"High stiffness = good control" -- only in free space**
High Kp = good position tracking in free space. But when contact occurs:
high Kp * contact_deformation = very large force. Parts break. Humans get hurt.
The right answer depends on the task: precision assembly needs medium stiffness
and good position; collaborative assembly needs low stiffness and force sensing.
