# Robotics — Landscape Overview

## The Big Picture

Robotics is a systems integration discipline. A robot is a closed-loop cyber-physical system:
sense → plan → act, continuously. Every subsystem maps to a well-defined engineering domain.

```
+===========================================================================+
|                        ROBOTICS SYSTEM STACK                              |
+===========================================================================+
|                                                                           |
|   PHYSICAL WORLD                                                          |
|   +------------------------------------------------------------------+   |
|   | Objects, terrain, humans, physics                                |   |
|   +------------------------------------------------------------------+   |
|            |  forces, light, distance             ^ forces, motion        |
|            v                                      |                       |
|   +-----------------+                   +-------------------+             |
|   |  SENSING        |                   |  ACTUATION        |             |
|   |  (Ch 03)        |                   |  (Ch 07)          |             |
|   |  LiDAR, cams    |                   |  Motors, drives   |             |
|   |  IMU, encoders  |                   |  Hydraulic, soft  |             |
|   |  Force/torque   |                   |  Harmonic gears   |             |
|   +-----------------+                   +-------------------+             |
|            |  raw data                          ^ joint torques           |
|            v                                    |                         |
|   +-----------------+                   +-------------------+             |
|   |  STATE ESTIMATN |                   |  CONTROL          |             |
|   |  (Ch 03, 04)    |                   |  (Ch 06)          |             |
|   |  SLAM, Kalman   |                   |  PID, computed-t  |             |
|   |  Odometry, AMCL |                   |  Impedance, force |             |
|   +-----------------+                   +-------------------+             |
|            |  pose + map                        ^ trajectory              |
|            v                                    |                         |
|   +--------------------------------------------------+                   |
|   |              PLANNING (Ch 05)                    |                   |
|   |  Task planning -> path planning -> trajectory gen|                   |
|   |  A*, RRT, RRT*, CHOMP, PDDL                      |                   |
|   +--------------------------------------------------+                   |
|            |  goal, constraints                                           |
|            v                                                              |
|   +--------------------------------------------------+                   |
|   |           AI / REASONING (Ch 09)                 |                   |
|   |  RL policies, imitation learning, foundation LLMs|                   |
|   |  Perception (6-DOF pose est.), task understanding|                   |
|   +--------------------------------------------------+                   |
|                                                                           |
|   MIDDLEWARE: ROS 2 / DDS (Ch 08) -- wires all subsystems together        |
|   MATH FOUNDATION: Kinematics (Ch 01) + Dynamics (Ch 02)                 |
|                                                                           |
+===========================================================================+
```

The "network" is physics. Every subsystem has latency, bandwidth, and failure modes —
the same layered abstraction discipline you apply to software stacks applies here, just
the medium is torque and photons rather than TCP packets.

---

## Four Subsystems — Brief Taxonomy

```
+---------------------------+---------------------------+
|       MECHANICS           |       SENSING             |
|---------------------------|---------------------------|
| Structure + kinematics    | Proprioceptive (self)     |
| Links, joints, frames     |   Encoders, IMUs          |
| Serial / parallel / soft  | Exteroceptive (world)     |
| DH parameters             |   LiDAR, cameras, FT      |
| Workspace envelopes       | Fusion: Kalman, EKF       |
+---------------------------+---------------------------+
|       COMPUTATION         |       ACTUATION           |
|---------------------------|---------------------------|
| State estimation          | Electric: DC, BLDC        |
| SLAM, localization        | Transmissions: gears,     |
| Planning: path, task      |   harmonic drives, cable  |
| Control laws              | Hydraulic / pneumatic     |
| AI/ML inference           | Soft: PAM, elastomers     |
+---------------------------+---------------------------+
```

---

## Robot Taxonomy

### By Structure

```
SERIAL (open-chain)              PARALLEL (closed-chain)
+------+                         +--Actuator--+--Actuator--+
| Base |                         |            |            |
|  J1  |-- link1 --+             +----link----+----link----+
|  J2  |-- link2 --+                          |
|  J3  |-- link3 -- EE            End-effector (delta, Stewart)
+------+
  Each joint affects all         All actuators share load.
  downstream links.              High stiffness, small workspace.
  Industrial arms (KUKA, ABB,    Pick-and-place (Adept Quattro),
  Fanuc, UR5/UR10).              Flight simulators (Stewart).
```

```
MOBILE                           AERIAL
+-------+                        +-rotors-+
| drive |                        | body   |
| wheels|                        | IMU    |
+-------+                        +-rotors-+
chassis -- sensors --
wheels/tracks/legs
  Differential drive             Multirotor (quad/hex/octo)
  Ackermann (car steering)       Fixed-wing UAV
  Omnidirectional (mecanum)      VTOL hybrid
  Legged: biped/quadruped        Tethered / free
```

### By Morphology

| Type | DOF | Workspace | Speed | Precision | Example |
|------|-----|-----------|-------|-----------|---------|
| Serial 6-DOF arm | 6 | Large, irregular | Med | High | KUKA KR, ABB IRB |
| SCARA | 4 | Cylindrical | Fast | High | Electronics assembly |
| Delta (parallel) | 3+1 | Compact cone | Very fast | Med-High | Adept Quattro |
| Stewart platform | 6 | Small, symmetric | Med | Very high | Flight sims, machining |
| Cartesian (gantry) | 3 | Rectangular | Med | Very high | CNC, 3D printing |
| Collaborative (cobot) | 6-7 | Large | Low-Med | High | UR5e, Franka, ABB YuMi |
| Legged biped | ~30+ | Everywhere | Med | Med | Atlas, Digit, Unitree H1 |
| Legged quadruped | ~12+ | Everywhere | Med-Fast | Med | Spot, ANYmal, Unitree Go2 |
| Humanoid | ~40+ | Human-scale | Med | Med | Atlas, Figure 01, 1X |

### By Application Domain

```
+--Industrial--+  +--Service--+  +--Medical--+  +--Field--+  +--Research--+
| Welding      |  | Warehouse |  | Surgical  |  | Drone   |  | MIT Cheetah|
| Assembly     |  | logistics |  | (Da Vinci)|  | mapping |  | CMU arm    |
| Painting     |  | Cleaning  |  | Rehab     |  | Disaster|  | Stanford   |
| CNC machining|  | Delivery  |  | Prosthetics|  | Space  |  | ETH Zurich |
+--------------+  +-----------+  +-----------+  +---------+  +------------+
```

---

## Historical Timeline

```
1961  Unimate #001 -- first industrial robot arm, GM Trenton plant.
      Hydraulic, 2-ton, spot welding. Programmed by playback.
       |
1969  Shakey (SRI) -- first mobile robot with onboard reasoning.
      Camera + bump sensors, STRIPS planner, moved 2 m/min.
       |
1970s Stanford Arm (1969), PUMA (1978) -- first all-electric,
      computer-controlled arms. Inverse kinematics in software.
       |
1980s SCARA robots revolutionize electronics assembly.
      Robot programming languages: VAL, Karel.
       |
1990s Industrial automation peak. 6-DOF arms everywhere.
      ABB, KUKA, Fanuc dominate. Safety cages required.
       |
1997  NASA Sojourner -- first autonomous planetary rover.
      Path planning on another world.
       |
2004  DARPA Grand Challenge: autonomous vehicles, Mojave Desert.
      No team finishes 142 miles.
       |
2005  DARPA Grand Challenge 2: Stanley (Stanford) wins.
      Self-driving cars proved feasible. Deep learning not yet involved.
       |
2002  iRobot Roomba -- first commercially successful mobile robot.
       |
2004  Boston Dynamics BigDog: hydraulic quadruped, DARPA funded.
       |
2011  DARPA Robotics Challenge announced (post-Fukushima).
      Humanoid disaster response focus.
       |
2013  DRC humanoid teams: Atlas unveiled (Boston Dynamics).
      Boston Dynamics acquired by Google.
       |
2016  AlphaGo beats Lee Sedol -> deep learning wave hits robotics.
       |
2017  OpenAI begins Dactyl: dexterous in-hand manipulation via RL.
      Solves Rubik's Cube (2019) -- landmark for dexterity.
       |
2019  Boston Dynamics Spot: quadruped, first commercial robot dog.
       |
2021  Boston Dynamics Atlas backflip. Legged locomotion matured.
      Unitree, ANYbotics, Ghost Robotics: quadruped market emerges.
       |
2022  Figure, 1X, Apptronik, Agility: humanoid startup wave begins.
       |
2023  RT-2 (Google DeepMind): vision-language-action model.
      Foundation models directly output robot actions.
       |
2024  Boston Dynamics Atlas electric (hydraulic retired).
      OpenVLA, Octo, pi0: open-source manipulation foundations.
      NVIDIA Gr00t announced; "Physical AI" as coined term.
       |
2025+ Foundation model manipulation, sim-to-real pipelines,
      synthetic data at scale, embodied AI investment surge.
      Humanoid labor deployment in manufacturing begins (Figure, 1X).
```

---

## Key Institutions and Labs

| Institution | Focus | Notable Work |
|-------------|-------|--------------|
| MIT CSAIL / Leg Lab | Legged, manipulation | Cheetah, mini cheetah; Russ Tedrake group (Drake) |
| Stanford Robotics | Manipulation, HRI | PUMA heritage, Pinocchio toolkit |
| CMU Robotics | Mobile, manipulation | SLAM heritage, Red Whittaker, field robotics |
| ETH Zurich | Legged, learning | ANYmal; Julian Floreano aerial |
| UC Berkeley | RL, manipulation | Pieter Abbeel, Sergey Levine; RT-series collaboration |
| Google DeepMind | Foundation models | RT-1, RT-2, SayCan, Gemini Robotics |
| Boston Dynamics | Legged, agility | BigDog, Spot, Atlas |
| DARPA | Challenge programs | Grand Challenge, DRC, OFFSET, RACER |
| NASA JPL | Planetary robotics | Sojourner, Spirit, Opportunity, Perseverance |

---

## The Autonomy Stack — Layered View

Robotics autonomy has the same layered architecture as a software stack — but with physics
at the bottom. Each layer runs at a different rate, just as network layers have different
latency budgets.

```
+----------------------------------------------------------+
|  TASK LEVEL                                              |
|  "Pick the red block and place it in the bin"            |
|  PDDL planners, LLM task understanding, behavior trees   |
|  Rate: 1-10 Hz or event-driven                           |
+----------------------------------------------------------+
                        |
+----------------------------------------------------------+
|  NAVIGATION / PATH LEVEL                                 |
|  "Go from A to B avoiding obstacles"                     |
|  A*, RRT, Nav2, global costmaps                          |
|  Rate: 10-50 Hz                                          |
+----------------------------------------------------------+
                        |
+----------------------------------------------------------+
|  TRAJECTORY / MOTION LEVEL                               |
|  "Follow this Cartesian path at 0.5 m/s"                 |
|  CHOMP, minimum-snap, trajectory interpolation           |
|  Rate: 100-500 Hz                                        |
+----------------------------------------------------------+
                        |
+----------------------------------------------------------+
|  CONTROL LEVEL                                           |
|  "Track this reference joint angle"                      |
|  PID, computed-torque, impedance control                 |
|  Rate: 1-10 kHz                                          |
+----------------------------------------------------------+
                        |
+----------------------------------------------------------+
|  HARDWARE / ACTUATOR LEVEL                               |
|  "Apply 12 N*m to joint 3"                               |
|  Motor drives, current control, FOC                      |
|  Rate: 10-100 kHz (current loop)                         |
+----------------------------------------------------------+
                        |
+----------------------------------------------------------+
|  PHYSICS                                                 |
|  Newton's laws, electromagnetism, contact mechanics      |
|  Runs at infinite Hz (or c)                              |
+----------------------------------------------------------+
```

This is exactly analogous to the network stack latency hierarchy: application →
transport → network → physical. The abstraction boundary is just as sharp, and the
same rule applies: layers only talk to adjacent layers.

---

## Old World to New World Bridges

| Concept You Know | Robotics Equivalent |
|-----------------|---------------------|
| Distributed systems | Robot = distributed system; physics is the network |
| Service bus / message queue | ROS 2 topics and DDS pub/sub |
| Database (state store) | Map representations, state estimator output |
| CI/CD pipeline | ROS 2 build system (colcon), sim-based regression |
| API contract | ROS 2 message types (.msg, .srv, .action files) |
| Load balancing | Task allocation in multi-robot systems |
| Latency SLA | Control loop timing, hard real-time constraints |
| Integration testing | Hardware-in-the-loop (HIL) simulation |
| Microservices | ROS 2 nodes (each a process, communicate over DDS) |
| Configuration management | Robot URDF/XACRO model files |
| Feature flags | ROS 2 parameters (runtime-configurable node behavior) |

---

## Where Robotics Intersects Other Disciplines

```
                  ROBOTICS
                     |
        +------------+------------+
        |            |            |
   Mechanical    Electrical    Computer
   Engineering   Engineering    Science
        |            |            |
   Kinematics    Motor drives   Algorithms
   Dynamics      Power elec.    SLAM
   Structures    Sensors        Planning
   Mechanisms    Embedded       AI/ML
                 systems        ROS 2
                     |
               Control Theory
               (sits at the intersection
                of all three)
```

No other engineering discipline requires this breadth simultaneously. A robotics engineer
needs enough mechanical to spec a gearbox, enough electrical to debug a motor driver,
enough CS to write a planner, and enough math to derive a Jacobian — in the same week.

---

## Decision Cheat Sheet — Which Chapter to Read

| Question | Chapter |
|----------|---------|
| How does a robot arm know where its hand is? | 01 — Kinematics |
| How do you compute joint torques for a motion? | 02 — Dynamics |
| What sensors does a robot use and how do they fuse? | 03 — Sensors |
| How does a robot build a map while navigating? | 04 — SLAM |
| How does a robot plan a collision-free path? | 05 — Planning |
| How does a robot follow a trajectory precisely? | 06 — Control |
| What actuates the joints and why harmonic drives? | 07 — Actuators |
| What is ROS 2 and how does Nav2/MoveIt2 work? | 08 — ROS |
| How do you train a robot with RL or imitation learning? | 09 — AI Robotics |

---

## Common Confusion Points

**"Robot" vs "Manipulator" vs "Agent"**
Manipulator = robot arm with fixed base, interacts with objects. Mobile robot = moves
through space, may or may not have arm. Agent = software entity that acts in an
environment (may have no body). The industry uses "robot" loosely; context determines
meaning.

**"Degrees of Freedom" vs "Axes"**
DOF = independent dimensions of motion (formal kinematic meaning). Axes = physical
joints (usually same count, but not always). A 6-DOF arm has 6 revolute joints; a 7-DOF
arm is kinematically redundant — has an infinite number of solutions for any given
end-effector pose, which is both useful (obstacle avoidance) and computationally harder.

**"Autonomous" vs "Automated"**
Automated = follows a fixed program (factory arm repeating a weld path — no sensing
of environment). Autonomous = perceives environment and makes decisions (self-driving,
legged locomotion over uneven terrain). Most industrial robots today are automated, not
autonomous. The distinction is whether the robot adapts to unplanned situations.

**"End-effector" vs "Tool Center Point (TCP)"**
End-effector = the physical device at the wrist (gripper, welder, suction cup). TCP =
the mathematical point whose pose kinematics tracks. TCP is user-defined; for a flat
gripper it is usually the center of the fingertips. The FK solution gives you TCP pose.

**Real-time vs soft real-time**
Hard real-time: missed deadline = system failure (motor drives, servo loops at 10 kHz).
Soft real-time: missed deadline = degraded performance (navigation planner at 10 Hz).
ROS 2 with real-time Linux (PREEMPT-RT kernel patch) handles hard real-time loops.
Standard ROS 2 nodes are soft real-time only. Control code should not live in ROS 2
nodes — it belongs in a dedicated real-time thread or separate MCU firmware.

**"Simulation" vs "Real world" gap**
Sim-to-real gap is not a bug — it is fundamental. Simulation approximates contact,
friction, motor dynamics, sensor noise. Models that work perfectly in Gazebo often
fail on hardware because of unmodeled effects. Domain randomization (intentionally
varying sim parameters) forces learned policies to be robust to this uncertainty.
