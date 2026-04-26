# Robotics — Kinematics

## The Big Picture

Kinematics answers one question: given joint angles, where is the end-effector?
And its inverse: given a desired end-effector pose, what joint angles achieve it?

```
+=========================================================================+
|                         KINEMATICS LANDSCAPE                            |
+=========================================================================+
|                                                                         |
|  FORWARD KINEMATICS (FK)                INVERSE KINEMATICS (IK)         |
|  ========================               ========================         |
|                                                                         |
|  Input:  q = [q1, q2, ..., qn]          Input:  T (4x4 pose matrix)    |
|          joint angles                            desired EE pose         |
|          (n = DOF of robot)                                             |
|                                                                         |
|  Output: T_0n (4x4 matrix)              Output: q = [q1, q2, ..., qn]  |
|          end-effector pose                       joint angles            |
|          (position + orientation)                                        |
|                                                                         |
|  Always has a UNIQUE solution.          May have MULTIPLE solutions,    |
|  O(n) computation.                      NO solution, or infinite        |
|  Solved by DH transform chain.          solutions (redundant arms).     |
|                                                                         |
|  +----------+    DH chain     +----------+                              |
|  | q1..qn   | ------------->  | T_0n     |    DIFFERENTIAL KINEMATICS   |
|  | angles   |                 | 4x4 pose |    J(q): maps q_dot -> v_EE  |
|  +----------+                 +----------+    Jacobian matrix           |
|                                                                         |
|  WORKSPACE ANALYSIS              SINGULARITIES                          |
|  Reachable workspace:            J loses rank -> velocity               |
|    set of all poses FK can       amplification -> infinite joint        |
|    produce within joint limits   velocities for finite EE velocity      |
|                                                                         |
+=========================================================================+
```

---

## Coordinate Frames and Homogeneous Transforms

Before DH parameters, the prerequisite: how poses are represented.

A rigid body pose in 3D is position (3 values) + orientation (3 values = 6 DOF for pose,
but orientation requires a 3x3 rotation matrix or quaternion to encode non-linearly).

```
Homogeneous Transform (4x4):

   T = | R  p |     R: 3x3 rotation matrix (SO(3))
       | 0  1 |     p: 3x1 translation vector
                    0: 1x3 zero row
                    1: scalar 1

   Represents: "frame B's origin is at p, and its axes are rotated by R,
                all expressed in frame A."

   Composition: T_AC = T_AB * T_BC
                "A to C" = "A to B" * "B to C"
                (matrix multiply — this is the FK chain)
```

Rotation matrix encodes direction cosines. Three common parametrizations:
- **Euler angles** (ZYX, ZYZ): 3 numbers, gimbal lock at singularity. Used in aerospace.
- **Axis-angle**: axis n (unit vector) + angle theta. Compact. Used in optimization.
- **Quaternion**: 4 numbers (w, x, y, z), |q|=1. No gimbal lock. Used in robotics control.

---

## Denavit-Hartenberg Convention

DH is a systematic recipe for constructing the homogeneous transform matrices — the FK computation T_0n = T_01 * T_12 * ... * T_{n-1,n} is matrix chain multiplication of 4x4 homogeneous transforms, the same operation used in 3D graphics scene graphs, CSS transform stacking, and any coordinate frame chaining in linear algebra. DH just standardizes which four parameters define each inter-frame transform. It
reduces an arbitrary serial chain to a table of 4 parameters per joint.

### The Four DH Parameters

For joint i, the DH parameters describe the transform from frame i-1 to frame i:

```
+-----------+----------------------------------------------------------+
| Parameter | Meaning                                                  |
+-----------+----------------------------------------------------------+
| a_i       | Link length: distance along x_i between z_{i-1} and z_i |
| alpha_i   | Link twist: rotation about x_i from z_{i-1} to z_i      |
| d_i       | Link offset: distance along z_{i-1} from x_{i-1} to x_i |
| theta_i   | Joint angle: rotation about z_{i-1} from x_{i-1} to x_i |
|           |   ** THIS is the variable for revolute joints **         |
+-----------+----------------------------------------------------------+

For revolute joint i:  theta_i is the variable, a_i/alpha_i/d_i are constants.
For prismatic joint i: d_i is the variable, a_i/alpha_i/theta_i are constants.
```

### DH Transform Matrix

The transform from frame i-1 to frame i using DH parameters:

```
T_{i-1,i} =

| cos(theta_i)  -sin(theta_i)*cos(alpha_i)   sin(theta_i)*sin(alpha_i)   a_i*cos(theta_i) |
| sin(theta_i)   cos(theta_i)*cos(alpha_i)  -cos(theta_i)*sin(alpha_i)   a_i*sin(theta_i) |
|      0              sin(alpha_i)                cos(alpha_i)                  d_i         |
|      0                   0                           0                          1         |
```

### Forward Kinematics via DH Chain

```
T_0n = T_01 * T_12 * T_23 * ... * T_{n-1,n}

       ^--- frame 0 (world/base) to frame n (end-effector)
       Each T_{i-1,i} depends on q_i (the joint angle).
       Just multiply the matrices in sequence.
```

### Example: 2R Planar Arm (2 revolute joints in a plane)

```
       L1          L2
  o----[=====]----[=====]--- EE
 Base  J1(q1)     J2(q2)

DH table:
  i  |  a_i  |  alpha_i  |  d_i  |  theta_i
  1  |   L1  |     0     |   0   |    q1      <- variable
  2  |   L2  |     0     |   0   |    q2      <- variable

T_01 = | cos(q1) -sin(q1) 0  L1*cos(q1) |
       | sin(q1)  cos(q1) 0  L1*sin(q1) |
       |    0        0    1      0       |
       |    0        0    0      1       |

T_12 = | cos(q2) -sin(q2) 0  L2*cos(q2) |
       | sin(q2)  cos(q2) 0  L2*sin(q2) |
       |    0        0    1      0       |
       |    0        0    0      1       |

End-effector position (from T_0n = T_01 * T_12):
  x = L1*cos(q1) + L2*cos(q1+q2)
  y = L1*sin(q1) + L2*sin(q1+q2)

This is FK. Always unique. Always solvable.
```

---

## The Jacobian Matrix

The Jacobian bridges joint velocities to end-effector velocity. It is the key matrix
for differential kinematics, singularity analysis, and IK.

### Definition

```
v_EE = J(q) * q_dot

where:
  v_EE : 6x1 vector [vx, vy, vz, wx, wy, wz]^T
           linear velocity (3) + angular velocity (3)
  q_dot: nx1 vector of joint velocity (n = DOF)
  J(q) : 6xn Jacobian matrix (depends on current joint angles q)
```

### Structure of J for a Serial Arm

Each column of J is the contribution of one joint to end-effector velocity:

```
J = [ J_1 | J_2 | ... | J_n ]

For revolute joint i:
  J_linear_i  = z_{i-1} x (p_n - p_{i-1})     <- cross product
  J_angular_i = z_{i-1}

For prismatic joint i:
  J_linear_i  = z_{i-1}
  J_angular_i = 0

where z_{i-1} is the joint axis direction in world frame,
      p_n is end-effector position,
      p_{i-1} is the joint i origin position.
```

### Using the Jacobian

```
FORWARD differential:    v_EE = J(q) * q_dot
INVERSE differential:    q_dot = J^+(q) * v_EE

J^+ = J^T (J J^T)^{-1}   <- Moore-Penrose pseudoinverse (for 6xn, n>6)
J^+ = (J^T J)^{-1} J^T   <- for overdetermined case (n<6)

For n=6 (square J):  q_dot = J^{-1}(q) * v_EE
```

---

## Inverse Kinematics

IK is harder than FK: you want q given T. Two main approaches.

### Analytical (Closed-Form) IK

For specific robot geometries, closed-form solutions exist. The standard result:

**6-DOF serial arm with spherical wrist** (most industrial arms: KUKA, ABB, PUMA style):
The wrist center position decouples the problem.

```
Step 1: Compute wrist center position from desired EE pose.
        p_wc = p_EE - d_6 * R_EE * [0, 0, 1]^T

Step 2: Solve for first 3 joints (q1, q2, q3) from wrist center position.
        Geometric / trigonometric solution.
        Typically 2 solutions: "elbow up" and "elbow down."

Step 3: Solve for wrist joints (q4, q5, q6) from required wrist orientation.
        ZYZ or ZXZ Euler angle extraction from R_3_6.
        Typically 2 solutions: "wrist flip" configurations.

Total: up to 8 solutions (2^3) for a 6R spherical-wrist arm.
       Robot picks based on joint limits and closest to current config.
```

### Numerical IK

When geometry does not admit closed-form, or for general arms, use iterative methods.

```
NEWTON-RAPHSON (damped least squares variant):
==============================================

Given: T_desired (target pose)
       q_current (current joint angles)

Loop until converged:
  1. Compute current pose: T_current = FK(q_current)

  2. Compute pose error:
     e_pos = p_desired - p_current         (3x1 position error)
     e_ori = 0.5 * (R_current x R_desired) (3x1 orientation error, SO(3) log)
     e = [e_pos; e_ori]                    (6x1)

  3. Compute Jacobian: J = J(q_current)

  4. Damped pseudoinverse (avoids singularity blow-up):
     J_damp = J^T (J J^T + lambda^2 * I)^{-1}
     where lambda is the damping factor

  5. Joint update:
     q_next = q_current + J_damp * e

  6. Apply joint limits and check convergence.
```

Key parameters:
- `lambda` (damping): 0.01-0.1. Larger = more stable near singularity, less accurate.
- Convergence criterion: ||e|| < epsilon (typically 1e-4 to 1e-6)
- Max iterations: 50-200. Failure to converge = IK failure (report no solution).

---

## Singularities

A singularity is a configuration where the Jacobian J(q) loses rank — the robot loses
the ability to move in one or more Cartesian directions regardless of joint velocities.

```
MATHEMATICAL: det(J J^T) = 0   (or equivalently, sigma_min(J) ~ 0)

PHYSICAL MEANING: Near a singularity,
  - Small Cartesian velocity requires INFINITE joint velocities
  - Joint velocities become numerically unbounded
  - The robot "locks up" or thrashes in practice

TYPES FOR A 6R ARM:
+--------------+------------------------------------------+-------------+
| Type         | Description                              | Configuration|
+--------------+------------------------------------------+-------------+
| Shoulder     | Wrist center crosses shoulder joint axis | Arm fully    |
|              |                                          | extended     |
+--------------+------------------------------------------+-------------+
| Elbow        | Joints 2, 3 are aligned (arm straight)   | Fully       |
|              | or fully folded                          | extended    |
+--------------+------------------------------------------+-------------+
| Wrist        | Joints 4, 6 axes are aligned             | q5 = 0       |
|              | (gimbal lock for wrist)                  |              |
+--------------+------------------------------------------+-------------+

DETECTION:
  Manipulability measure: w = sqrt(det(J J^T))
  w = 0 at singularity
  w small = near singularity (ill-conditioned)

AVOIDANCE:
  - Path planning: avoid singular configurations in trajectory
  - Damped least squares: degrade gracefully (lambda bumped up)
  - Singularity-robust IK: task augmentation near singularity
```

---

## Workspace Analysis

```
REACHABLE WORKSPACE                DEXTEROUS WORKSPACE
===================                ===================
Set of all positions p that        Set of all positions p where
the EE can reach with AT LEAST     the EE can achieve EVERY
one orientation.                   orientation.

Always larger than dexterous.      Typically much smaller.
"Can I get there?"                 "Can I get there with any tool angle?"

Bounded by:
  - Link lengths (max reach)
  - Joint limits (angular range)
  - Self-collision constraints

VISUALIZATION:
  Monte Carlo: sample random q vectors, compute FK, plot EE positions.
  Result: point cloud showing reachable workspace shape.
```

### Robot Morphology Workspace Comparison

```
                SERIAL 6-DOF              SCARA (4-DOF)

              ___________                 ___________
             /           \               /           \
            /   Large,    \             /  Cylindrical\
           /   irregular   \           / (strong in   |
          |   envelope      |         |  horizontal,  |
          |   (doughnut     |         |  weak in      |
          |    shape with   |          \  vertical)  /
           \   inner void) /             \___________/
            \             /
             \___________/

  Full 6-DOF pose in most of volume.    Only 4-DOF (x,y,z,rz). Fast.

                DELTA (PARALLEL)        CARTESIAN (GANTRY)

             <----workspace---->        +------------------+
                   /\                   |                  |
                  /  \                  |  Rectangular     |
                 /    \                 |  workspace.      |
                / cone \                |  Full stiffness  |
               /________\              |  throughout.     |
                                        +------------------+
  Very fast. Stiff. Small cone.         Large. Heavy. Expensive.
  Pick-and-place only (limited DOF).    CNC machines, gantry robots.
```

---

## 7-DOF Redundant Arms

Most industrial arms are 6-DOF (exactly enough for 6D pose). 7-DOF arms (Franka Panda,
KUKA iiwa, Kinova Gen3) add one extra joint — kinematic redundancy.

```
6-DOF arm: J is 6x6 (square).
  For a given EE pose: exactly 0 or finite # of IK solutions.
  No freedom to move without changing EE pose.

7-DOF arm: J is 6x7 (more joints than task DOF).
  For a given EE pose: infinite IK solutions (a manifold in joint space).
  The extra DOF can be used for:
    - Obstacle avoidance (null-space motion)
    - Joint limit avoidance
    - Optimizing some secondary criterion (min torque, etc.)

NULL-SPACE MOTION:
  q_dot = J^+ v_EE + (I - J^+ J) * q_dot_0
                     ^^^^^^^^^^^^^^^^^^^^^
                     null-space projector
                     q_dot_0: arbitrary joint velocity
                     (I - J^+J): projects onto null space of J
                     EE does not move while joints do!
```

---

## Robot Morphology Deep Dive

### SCARA (Selective Compliance Assembly Robot Arm)

```
         q1 (rotation)
         |
    L1   |   q2 (rotation)
  o------+------+--- q3 (translation, vertical)
  base         EE           + q4 (rotation about vertical)

  4 DOF: x, y, z, rotation about z.
  High stiffness in XY (plane), compliant in Z (assembly).
  Used for: PCB assembly, packaging, bolt insertion.
  Speed: 100+ cycles/min (pick-and-place).
```

### Delta Robot (Parallel)

```
         BASE (fixed)
     A1---A2---A3  (3 actuators at top, fixed base)
     |     |    |
    upper arms (3 sets, each with 2 parallel rods)
     |     |    |
     +--platform+  <- end-effector moves in XYZ only (+ optional 4th axis)

  All 3 actuators fire simultaneously.
  Very high acceleration (>10g for food packaging).
  Small workspace (cone below base).
  Stiff because loads shared across 3 chains.
  Examples: Adept Quattro, ABB FlexPicker.
```

### Stewart Platform (Hexapod)

```
         TOP PLATE (end-effector)
          o    o    o
          |    |    |
          6 actuated legs (linear actuators)
          |    |    |
          o    o    o
         BOTTOM PLATE (base)

  6 legs -> 6 DOF (position + orientation).
  All legs share load -> very high stiffness.
  Small workspace (must stay near neutral).
  Applications: flight simulators, precision machining, optical alignment.
```

---

## Decision Cheat Sheet

| Need | Approach |
|------|----------|
| Joint angles -> EE pose | Forward kinematics, DH chain multiplication |
| EE pose -> joint angles (known geometry) | Analytical IK (spherical wrist decoupling) |
| EE pose -> joint angles (general) | Numerical IK (damped least squares) |
| EE velocity -> joint velocities | Jacobian pseudoinverse: q_dot = J^+ v_EE |
| Check if configuration is singular | Compute manipulability w = sqrt(det(JJ^T)) |
| Move joints without moving EE | Null-space projection (needs 7-DOF arm) |
| Visualize what robot can reach | Monte Carlo FK sampling -> point cloud |
| Pick robot for fast flat-plane work | SCARA |
| Pick robot for fast pick-and-place | Delta (parallel) |
| Pick robot for complex 3D manipulation | Serial 6-DOF or 7-DOF |
| Need highest stiffness + precision | Stewart platform or Cartesian gantry |

---

## Common Confusion Points

**"FK always has a solution; IK may not"**
FK is just matrix multiplication — always produces an answer. IK requires solving
nonlinear equations. Outside the reachable workspace: no solution. At singularities:
infinitely many solutions or numerical divergence. Near joint limits: solutions may
be kinematically reachable but mechanically infeasible.

**DH convention variants: "standard" vs "modified"**
Craig's book uses Modified DH (MDH); Spong uses Standard DH. They differ in where
the frame is attached (distal vs proximal to joint). Same robot, different parameter
tables. When copying DH parameters, verify which convention the source uses.

**Jacobian = derivative of FK, not an explicit formula you memorize**
J(q) = d FK(q) / dq. For each robot configuration, J is different. It is computed
from the current joint angles every control cycle — it is not a constant matrix.

**"Pose" vs "position"**
Position = 3D coordinates (x, y, z) only. Pose = position + orientation (6D). IK
solving for position only (3 constraints) with 6 joints leaves 3 free DOF. Fully
specifying pose requires 6 constraints, hence 6 DOF minimum for general IK.

**Wrist singularity vs gimbal lock**
Wrist singularity (q5=0 in a 6R spherical-wrist arm) is exactly gimbal lock: joints
4 and 6 align, and the robot loses one orientation DOF. Not a software bug — it is a
physical, geometric property of the kinematic structure.
