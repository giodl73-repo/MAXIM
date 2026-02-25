# Robotics — Dynamics

## The Big Picture

Kinematics ignores forces. Dynamics answers: what joint torques produce a desired motion?
This is the physics layer that sits between the control law and the actuators.

```
+==========================================================================+
|                          ROBOT DYNAMICS LANDSCAPE                        |
+==========================================================================+
|                                                                          |
|  EQUATION OF MOTION (EOM):                                               |
|                                                                          |
|         M(q) * q_ddot  +  C(q, q_dot) * q_dot  +  G(q)  =  tau         |
|         ^^^^^^^^^^^^^     ^^^^^^^^^^^^^^^^^^      ^^^^      ^^^          |
|         Inertia term      Coriolis/centripetal    Gravity   Joint        |
|         (mass matrix)     term                   vector    torques       |
|                                                                          |
|  FORWARD DYNAMICS         |  INVERSE DYNAMICS                            |
|  Input:  tau (torques)    |  Input:  q, q_dot, q_ddot (motion)           |
|  Output: q_ddot (accel)   |  Output: tau (torques required)              |
|  Used in: simulation      |  Used in: computed-torque control            |
|                           |           motor sizing                       |
|                                                                          |
|  TWO FORMULATIONS         |                                              |
|  Newton-Euler (recursive) |  Efficient: O(n) for serial chain            |
|  Lagrangian (energy)      |  Elegant: derives EOM from energy functions  |
|                                                                          |
+==========================================================================+
```

---

## Rigid Body Dynamics — Single Body

Before tackling the full chain, the foundations.

### Inertia Tensor

For a rigid body, the inertia tensor I (3x3 symmetric matrix) describes how mass
is distributed relative to a frame (typically the center of mass):

```
I = | Ixx  -Ixy  -Ixz |     Ixx = integral of (y^2 + z^2) dm
    |-Iyx   Iyy  -Iyz |     Iyy = integral of (x^2 + z^2) dm
    |-Izx  -Izy   Izz |     Izz = integral of (x^2 + y^2) dm
                             Ixy = integral of xy dm  (products of inertia)

For a solid cylinder of mass m, radius r, length h:
  About symmetry axis:   Izz = m*r^2 / 2
  About diameter:        Ixx = Iyy = m*(3r^2 + h^2) / 12
```

Parallel axis theorem: shift inertia tensor from COM to an offset point d:
```
  I_offset = I_com + m * (|d|^2 * I_3x3 - d * d^T)
```

### Newton-Euler Equations for One Body

```
  F = m * a_com           (linear: force = mass * linear accel of COM)
  tau = I * alpha + omega x (I * omega)    (rotational, in body frame)

  where:
    F:     net external force vector (3x1)
    m:     scalar mass
    a_com: linear acceleration of center of mass (3x1)
    tau:   net external torque about COM (3x1)
    I:     3x3 inertia tensor about COM in body frame
    alpha: angular acceleration (3x1)
    omega: angular velocity (3x1)
    x:     cross product
```

The omega x (I * omega) term is the Euler term — it accounts for why a torque-free
spinning body can still precess (the gyroscopic effect). This is why a BLDC motor
spinning at high speed has gyroscopic effects on robot dynamics.

---

## Recursive Newton-Euler Algorithm

For a serial chain of n links, the recursive Newton-Euler (RNE) algorithm computes
inverse dynamics in O(n) — linear in number of joints. This is what real robot
controllers use (not Lagrangian, which is slower to compute symbolically for large n).

### Two Passes

```
PASS 1 — OUTWARD (base to end-effector): propagate velocities and accelerations
============================================================================

For i = 1 to n (joint 1 to end-effector):

  omega_i = R_i^T * omega_{i-1} + q_dot_i * z_i
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            rotate parent angular velocity to link frame + joint rotation contribution

  alpha_i = R_i^T * alpha_{i-1} + q_ddot_i * z_i + q_dot_i * (omega_i x z_i)

  a_i = R_i^T * (alpha_{i-1} x p_{i-1,i} + omega_{i-1} x (omega_{i-1} x p_{i-1,i}) + a_{i-1})
        ^^^^^^^   angular accel contribution  centripetal term                         parent accel

  a_{ci} = a_i + alpha_i x p_{i,ci} + omega_i x (omega_i x p_{i,ci})
            linear acceleration of center of mass of link i

where:
  omega_i, alpha_i: angular velocity/acceleration of link i
  a_i:              linear acceleration of link i origin
  a_{ci}:           linear acceleration of COM of link i
  z_i:              joint axis in link i frame (typically [0,0,1])
  p_{i-1,i}:        vector from joint i-1 to joint i in link i frame
  p_{i,ci}:         vector from joint i origin to link i COM
```

```
PASS 2 — INWARD (end-effector to base): propagate forces and torques
=====================================================================

For i = n down to 1:

  f_i = m_i * a_{ci} + R_{i+1} * f_{i+1}
        ^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^
        link inertial   reaction from next link (zero for n+1)

  n_i = I_i * alpha_i + omega_i x (I_i * omega_i) + R_{i+1} * n_{i+1}
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^
              Euler equation for link i            reaction torque

  then add contribution of COM offset:
  n_i += p_{i,ci} x (m_i * a_{ci}) + p_{i,i+1} x (R_{i+1} * f_{i+1})

JOINT TORQUE (revolute joint i):
  tau_i = n_i^T * z_i    <- project reaction torque onto joint axis

JOINT FORCE (prismatic joint i):
  f_i_joint = f_i^T * z_i
```

This is the O(n) algorithm. For 6-DOF arm: 6 iterations outward + 6 inward = 12 passes.
Used in every industrial robot controller and simulation engine.

---

## Lagrangian Formulation

The Lagrangian gives the equation of motion in a form directly useful for analysis
and control design. Slower to compute numerically, but gives symbolic insight.

### The Lagrangian

```
L = T - V

T: total kinetic energy of all links
V: total potential energy of all links
```

### Kinetic Energy

```
T = sum_i (0.5 * m_i * v_{ci}^T * v_{ci} + 0.5 * omega_i^T * I_i * omega_i)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         translational KE of link i COM      rotational KE of link i

This can be written as:
T = 0.5 * q_dot^T * M(q) * q_dot

where M(q) is the n x n MASS MATRIX (also called inertia matrix).

Properties of M(q):
  - Symmetric: M(q) = M(q)^T
  - Positive definite: q_dot^T M(q) q_dot > 0 for all non-zero q_dot
  - Depends on configuration q (not constant!)
```

### Potential Energy

```
V = sum_i (m_i * g^T * p_{ci}(q))

where g is the gravity vector [0, 0, -9.81] in world frame,
      p_{ci}(q) is COM position of link i (function of joint angles).

G(q) = dV/dq    (n x 1 gravity torque vector)
```

### Coriolis and Centripetal Matrix

From the Euler-Lagrange equations:

```
C_ij(q, q_dot) = sum_k (Christoffel symbols * q_dot_k)

Christoffel symbol: c_{ijk} = 0.5 * (dM_{ij}/dq_k + dM_{ik}/dq_j - dM_{jk}/dq_i)

C(q, q_dot) * q_dot contains:
  - Coriolis terms:    proportional to q_dot_i * q_dot_j (i != j)
  - Centripetal terms: proportional to q_dot_i^2
```

### The Equation of Motion

```
EULER-LAGRANGE: d/dt (dL/dq_dot) - dL/dq = tau

Result:

     M(q) * q_ddot  +  C(q, q_dot) * q_dot  +  G(q)  =  tau

This is the fundamental EOM for a serial robot arm with rigid links.

In practice:
  tau = M(q)*q_ddot + C(q,q_dot)*q_dot + G(q)   <- INVERSE DYNAMICS
        (given desired motion, compute required torques)

  q_ddot = M(q)^{-1} * (tau - C(q,q_dot)*q_dot - G(q))   <- FORWARD DYNAMICS
        (given applied torques, compute resulting acceleration)
```

---

## Physical Meaning of Each Term

```
TERM            PHYSICAL MEANING                    WHEN DOMINANT
====            ================                    =============
M(q) q_ddot     Inertial resistance to              High accelerations,
                acceleration. Larger M -> harder    heavy links, or
                to move, but also harder to stop.   extreme poses (full
                M varies with pose (more extended   extension: higher M)
                = higher effective inertia).

C(q,q_dot)q_dot Coriolis: coupling between joints.  High joint velocities.
                Moving joint 1 while joint 2 moves  Fast manipulation,
                generates a "fictitious" force at    legged locomotion.
                joint 2 due to rotating frame.
                Centripetal: q_dot^2 terms pulling
                links inward (like a spinning chain).

G(q)            Gravity torque. All the torque the  Any non-zero g.
                actuators must provide just to       Dominant at slow
                hold the arm still against gravity.  speeds / static.
                G(q) = 0 for horizontal plane arms.
```

---

## Motor Sizing from Dynamics

The EOM directly tells you what torques joints must produce. Motor sizing follows:

```
STEPS:
1. Define the worst-case task motion (fastest, heaviest payload, most extended pose).
2. Compute q_ddot required for the desired EE trajectory (inverse kinematics for velocity).
3. Compute tau_required = M(q)*q_ddot + C(q,q_dot)*q_dot + G(q).
4. Add payload forces at EE (via Jacobian transpose: tau_payload = J^T * F_ext).
5. Add friction model (viscous + Coulomb: tau_friction = b*q_dot + c*sign(q_dot)).
6. Apply gear ratio N: tau_motor = tau_joint / N, omega_motor = N * q_dot.
7. Check motor torque-speed curve: tau_motor < tau_rated at omega_motor.
8. Check thermal: RMS torque < continuous rated torque.
9. Add 20-30% safety factor for model inaccuracy.

GEAR RATIO EFFECT:
  tau_joint = N * tau_motor    (torque amplification)
  omega_joint = omega_motor / N  (speed reduction)
  I_reflected = N^2 * I_motor   (inertia reflected through gearbox)
  <- This is why high gear ratios appear to stiffen the arm (reflected motor
     inertia dominates over link inertia).
```

---

## Contact Mechanics

When a robot touches the world, additional forces enter the EOM via the Jacobian.

### Rigid Contact Model

```
FRICTION CONE:
                 /\
                /  \  friction cone
               / mu \
        ------+------+------  contact surface
               normal force n

  For contact to be stable (no slip):
    |f_tangential| <= mu * f_normal    (Coulomb friction)
    f_normal >= 0                       (no pull: unilateral constraint)

  mu_s: static friction coefficient (no motion)
  mu_k: kinetic friction coefficient (sliding)
  Typically: mu_s > mu_k.
```

### Force Closure (Grasp Stability)

```
A grasp has FORCE CLOSURE if the set of contact forces can
generate any net wrench on the object (resist any external force/torque).

FORM CLOSURE: purely geometric -- object physically cannot move
              (like a box in a fixture). No friction needed.

FORCE CLOSURE: needs friction forces. Object can resist wrenches.
               Stronger than form closure in practice.

For a parallel gripper: 2 contact points.
  Need friction cone from each finger to "cancel" any external torque.
  Minimum: 2 contacts for planar, 3+ for 3D force closure.
```

### EOM with External Contact Forces

```
M(q) q_ddot + C(q,q_dot) q_dot + G(q) = tau + J_c^T * F_c

where:
  J_c:  contact Jacobian (maps contact forces to joint torques)
  F_c:  contact wrench at contact point
  tau:  actuator torques

This is why impedance control (Ch 06) is needed for contact-rich tasks:
the control law must regulate F_c explicitly.
```

---

## Flexible-Link and Soft-Body Extensions

Real robots are not perfectly rigid. Links flex under load.

```
RIGID LINK assumption:
  Links are infinitely stiff. EOM as above.
  Valid for: most industrial arms, cobots with stiff structures.
  Error: at high speeds or long spans (gantry, lightweight arms).

FLEXIBLE LINK:
  Each link has distributed compliance. EOM gains extra vibrational modes.
  State: joint angles + modal amplitudes (elastic DOF).
  Controller must damp these modes (notch filters common).
  Examples: space robot arms (SRMS on Space Shuttle), surgical instruments.

SERIES ELASTIC ACTUATOR (SEA) model:
  Spring between motor and joint (see Ch 07).
  tau_joint = K_spring * (theta_motor/N - q_joint)
  Adds a spring DOF to the EOM. Enables force sensing and impedance control.
```

---

## Dynamic Simulation

Dynamic simulation numerically integrates the EOM forward in time.

```
INTEGRATION:
  Given: tau(t), q(0), q_dot(0)

  At each timestep:
    1. Compute M(q), C(q,q_dot), G(q) via RNE or Lagrangian.
    2. Add contact forces and external loads.
    3. Compute q_ddot = M^{-1} * (tau - C*q_dot - G + J_c^T * F_c)
    4. Integrate: q_dot += q_ddot * dt
                  q     += q_dot * dt
    5. Detect and resolve contacts.

TYPICAL TIMESTEP:
  1-10 ms for rigid body (100-1000 Hz)
  Faster = more accurate = more computation

SIMULATORS:
  Mujoco:  fast, differentiable, good for RL training
  Gazebo:  ROS-integrated, ODE/Bullet/DART physics engines
  Isaac Sim (NVIDIA): GPU-accelerated, photorealistic, for large-scale RL
  PyBullet: Python-friendly, good for research
  Drake (MIT): symbolic + numerical, Lyapunov stability tools
```

---

## Decision Cheat Sheet

| Need | Approach |
|------|----------|
| Compute joint torques for a motion | Inverse dynamics via RNE algorithm |
| Simulate robot from applied torques | Forward dynamics: q_ddot = M^{-1}(tau - C*q_dot - G) |
| Understand energy / derive EOM symbolically | Lagrangian formulation |
| Size a motor for a joint | Compute peak and RMS tau from RNE, back-calculate through gear ratio |
| Check if grasp is stable | Force/form closure analysis using contact normals |
| Control force during contact | Add J_c^T * F_c term; use impedance or force control |
| Simulate for RL training (fast) | MuJoCo or Isaac Sim |
| Debug robot dynamics in ROS | Drake or PyBullet with ROS bridge |

---

## Common Confusion Points

**M(q) is NOT constant**
The mass matrix depends on configuration. At full extension, effective inertia is higher
than at a tucked pose because the links are farther from the rotation axis. This is why
control becomes harder at arm extension.

**C(q, q_dot)*q_dot is not the same as a friction force**
Coriolis/centripetal forces are inertial pseudo-forces arising from the rotating
coordinate frame — not energy dissipation. They do zero net work. Friction is
a separate physical term you add explicitly.

**Gravity vector G(q) depends on the robot's mounting orientation**
G(q) assumes some gravity vector g. If the robot is mounted upside-down (common for
ceiling-mounted industrial arms), g = [0, 0, +9.81]. Get this wrong and the controller
will fight gravity in the wrong direction.

**"Forward dynamics" vs "Forward kinematics"**
Forward kinematics: angles -> pose (geometry, no forces).
Forward dynamics: torques -> accelerations (physics, no geometry of pose needed beyond M,C,G).
These are completely separate computations.

**RNE vs Lagrangian: when to use which**
Lagrangian: for deriving EOM analytically, for control theory proofs, for symbolic small
systems (2-3 DOF). RNE: for real-time computation on embedded hardware with 6+ DOF arms.
RNE is O(n), Lagrangian is O(n^3) to compute M(q) symbolically.

**Gear ratio reflects motor inertia as N^2**
A gearbox with ratio N=100:1 reflects motor rotor inertia as N^2 = 10,000x. A small
motor rotor (1 kg*cm^2) appears as 10,000 kg*cm^2 at the joint. For high-gear-ratio
systems (harmonic drives: N=50-160), reflected motor inertia can dominate the dynamics,
which simplifies control (the robot feels like just motors, not complex links).
