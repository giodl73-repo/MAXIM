# Robotics — ROS 2 Ecosystem

## The Big Picture

ROS 2 is the middleware layer that wires all robot subsystems together. It is not a
framework, not an OS, and not a monolith. It is a communication layer + tooling ecosystem.

```
+===========================================================================+
|                         ROS 2 ECOSYSTEM LANDSCAPE                         |
+===========================================================================+
|                                                                           |
|  YOUR ROBOT APPLICATION                                                   |
|  +------------------------------------------------------------------+    |
|  | Navigation stack  | Manipulation stack | Perception | Your code  |    |
|  | (Nav2)            | (MoveIt2)          | pipeline   |            |    |
|  +------------------------------------------------------------------+    |
|                           |                                              |
|  ROS 2 MIDDLEWARE LAYER                                                   |
|  +------------------------------------------------------------------+    |
|  | Nodes | Topics | Services | Actions | Parameters | Lifecycle     |    |
|  +------------------------------------------------------------------+    |
|                           |                                              |
|  DDS (Data Distribution Service)                                          |
|  +------------------------------------------------------------------+    |
|  | Fast DDS (eProsima) | Cyclone DDS | Connext DDS                  |    |
|  | RTPS wire protocol  | QoS policies | Discovery                   |    |
|  +------------------------------------------------------------------+    |
|                           |                                              |
|  HARDWARE LAYER                                                           |
|  +------------------------------------------------------------------+    |
|  | ros2_control | Sensor drivers | Motor drives | Simulation        |    |
|  +------------------------------------------------------------------+    |
|                           |                                              |
|  SIMULATION                BUILD SYSTEM               CLI TOOLS           |
|  Gazebo / Isaac Sim        colcon / ament              ros2 CLI           |
|  Ignition Gazebo           Python / CMake              rviz2 / rqt        |
|                                                                           |
+===========================================================================+
```

---

## ROS 1 vs ROS 2: Why the Rewrite

ROS 1 (2007-2025 supported) was a research platform that escaped into production.
Its design assumptions did not hold at scale.

```
ROS 1 PROBLEMS:              ROS 2 SOLUTIONS:
=====================         ====================
rosmaster: single-point-      No master. DDS discovery:
  of-failure. If it dies,       nodes find each other
  the whole system fails.       via multicast/unicast.

No real-time support.         DDS with real-time QoS.
Latency unpredictable.        PREEMPT-RT Linux support.

TCP-only comms.               DDS transports: UDP, TCP,
Limited to LAN.               shared memory (zero-copy).

No security.                  DDS-Security: encryption,
Messages unencrypted.         authentication, access ctrl.

Python 2 / C++11.             Python 3 / C++17.

No lifecycle nodes.           Lifecycle nodes: managed
Nodes either run or           startup/shutdown/error
crash -- no in-between.       states (like a state machine).

Single-thread executors.      Multithreaded executors,
                              callback groups.
```

---

## Core Abstractions

### Nodes

```
NODE: the basic unit of computation. A process (or intra-process component).

  Each node has:
    - Unique name (namespace/node_name)
    - Publishers and subscribers (for topics)
    - Service clients and servers
    - Action clients and servers
    - Parameters

  Create a node (C++):
    auto node = std::make_shared<rclcpp::Node>("my_node");

  Create a node (Python):
    node = Node("my_node")

  Nodes communicate via DDS -- completely decoupled.
  A node can be in any language: C++, Python, Rust (rclrs), Julia.

COMPOSABLE NODES (intra-process):
  Multiple nodes in one process.
  Zero-copy communication via shared_ptr passing.
  Needed for high-bandwidth data (point clouds, images).
```

### Topics

```
TOPIC: anonymous publish-subscribe channel.

  Publisher:
    pub = node.create_publisher<sensor_msgs::msg::Image>("/camera/image", 10)
    pub.publish(image_msg)

  Subscriber:
    sub = node.create_subscription<sensor_msgs::msg::Image>(
            "/camera/image", 10, callback)

  QoS (Quality of Service) policies:
    Reliability:  RELIABLE (retransmit on loss) or BEST_EFFORT (fire and forget)
    Durability:   VOLATILE (no history) or TRANSIENT_LOCAL (late-join gets last msg)
    History:      KEEP_LAST (buffer depth N) or KEEP_ALL
    Deadline:     maximum period between messages
    Liveliness:   how to detect if publisher is alive
    Lifespan:     max age of message before discarded

  MISMATCH RULE: publisher and subscriber QoS must be compatible.
    RELIABLE pub + BEST_EFFORT sub: OK (sub gets what pub sends).
    BEST_EFFORT pub + RELIABLE sub: INCOMPATIBLE (no connection formed).
```

### Services

```
SERVICE: synchronous request-response communication.

  Service definition file (.srv):
    int64 a
    int64 b
    ---
    int64 sum

  Server:
    srv = node.create_service<AddTwoInts>(
            "add_two_ints", handle_request)

  Client:
    client = node.create_client<AddTwoInts>("add_two_ints")
    future = client.call_async(request)

  USE WHEN: query-response that takes < 1 second.
  AVOID FOR: long-running operations (use Actions).
  AVOID FOR: sensor streams (use Topics).
```

### Actions

```
ACTION: for long-running tasks with progress feedback and cancellation.

  Action definition file (.action):
    # Goal
    float64 target_angle
    ---
    # Result
    float64 final_angle
    ---
    # Feedback
    float64 current_angle

  Client:
    client.send_goal(goal)                   <- start
    client.get_result_async()                <- wait for done
    client.cancel_goal_async()               <- cancel

  Feedback callback: called periodically during execution.
  State machine: IDLE -> ACCEPTED -> EXECUTING -> SUCCEEDED/ABORTED/CANCELED

  EXAMPLES:
    MoveIt2 arm motion (send goal: "go to pose X", feedback: current progress)
    Nav2 navigation (go to waypoint, feedback: distance remaining)
    Assembly task server (execute sequence, feedback: step completed)
```

### Parameters

```
PARAMETERS: node-local key-value configuration.

  Declare in node (C++):
    declare_parameter("max_speed", 1.0)
    get_parameter("max_speed", max_speed_)

  CLI:
    ros2 param get /controller max_speed
    ros2 param set /controller max_speed 2.0
    ros2 param dump /controller > params.yaml
    ros2 param load /controller params.yaml

  Launch file parameter:
    Node(package=..., executable=...,
         parameters=[{"/controller/max_speed": 1.5}])

  DIFFERENT FROM TOPICS: parameters are configuration, not data streams.
  Parameters are node-specific; topics are network-wide.
```

### Lifecycle Nodes

```
LIFECYCLE NODE STATE MACHINE:
   [Unconfigured] --on_configure()--> [Inactive]
   [Inactive]     --on_activate()---> [Active]
   [Active]       --on_deactivate()--> [Inactive]
   [Inactive]     --on_cleanup()----> [Unconfigured]
   [Active/Inactive] --on_error()--> [ErrorProcessing]
   [Unconfigured] --on_shutdown()--> [Finalized]

USE CASE: deterministic startup/shutdown sequence.
  Node 1 (sensor driver) must be Active before Node 2 (filter) starts.
  Lifecycle manager controls startup order.
  Used in: Nav2, ros2_control.
```

---

## DDS (Data Distribution Service)

DDS participant discovery (PDP/EDP) is the same problem as service registration/discovery in distributed systems: nodes announce themselves via multicast, peers discover available topics. The failure modes are identical — multicast-based discovery fails across NAT boundaries and VLANs for the same reason Kubernetes service discovery requires explicit configuration in multi-cloud or air-gapped environments.

The middleware that powers ROS 2. Understanding DDS helps debug QoS issues.

```
DDS ARCHITECTURE:
  Standard: OMG DDS specification.
  Wire protocol: RTPS (Real-Time Publish-Subscribe).

  RTPS runs over UDP by default (multicast for discovery, unicast for data).
  Does not require a central broker (contrast: MQTT needs a broker).

DISCOVERY:
  Participant Discovery Protocol (PDP): nodes announce themselves via multicast.
  Endpoint Discovery Protocol (EDP): nodes exchange topic/service endpoints.
  First message on UDP port 7400 (by default).

DDS VENDOR COMPARISON:
  Fast DDS (eProsima): ROS 2 default. Good all-around.
  Cyclone DDS: good for high throughput, used by some automotive systems.
  Connext DDS (RTI): enterprise, expensive, safety-certified (DO-178C, ISO 26262).
  OpenSplice (ADLINK): discontinued.

SHARED MEMORY TRANSPORT (for same-machine zero-copy):
  Fast DDS data-sharing: publisher and subscriber share memory.
  Point clouds (millions of points/sec) need this to avoid CPU copy overhead.
  Enable via QoS: TransportConfigQos with shared memory data writer/reader.
```

---

## Build System

### colcon and ament

```
COLCON (Collective Construction):
  The build tool for ROS 2 workspaces.
  Replaces catkin_make from ROS 1.

  colcon build                    <- build all packages
  colcon build --packages-select my_pkg    <- build one package
  colcon test                     <- run all tests
  colcon test-result               <- show results

WORKSPACE STRUCTURE:
  ws/
  ├── src/           <- put packages here
  │   ├── my_pkg/
  │   │   ├── package.xml
  │   │   ├── CMakeLists.txt  (C++ package)
  │   │   └── ...
  │   └── my_py_pkg/
  │       ├── package.xml
  │       ├── setup.py         (Python package)
  │       └── ...
  ├── build/         <- build artifacts (gitignore)
  ├── install/       <- installed packages
  └── log/           <- build logs

SETUP (after building):
  source install/setup.bash      <- adds packages to PATH/PYTHONPATH

AMENT (Ant Ement):
  The CMake/Python build extension for ROS 2 packages.
  ament_cmake: CMake macros for C++ packages.
  ament_python: setuptools integration for Python packages.

PACKAGE.XML:
  <depend>rclcpp</depend>          <- runtime + build dep
  <build_depend>ament_cmake</build_depend>
  <exec_depend>sensor_msgs</exec_depend>
```

---

## Nav2 Stack

Nav2 is the complete autonomous navigation stack for ROS 2 mobile robots.

```
NAV2 ARCHITECTURE:

  Goal (x, y, theta)
        |
  +------------------+
  |  BT NAVIGATOR    |  Behavior Tree-based task execution.
  |  (BT.cpp)        |  Handles: navigate, recovery behaviors, cancel.
  +------------------+
        |
  +------------------+   +------------------+
  |  GLOBAL PLANNER  |   |  LOCALIZATION    |
  |  NavFn (A*)       |   |  AMCL (particle   |
  |  SMAC (lattice)  |   |  filter), or     |
  |  Theta* (any-ang)|   |  SLAM Toolbox    |
  +------------------+   +------------------+
        |                        |
  +------------------+   +------------------+
  |  LOCAL PLANNER   |   |  COSTMAPS        |
  |  DWB / MPPI / RPP|   |  Global costmap  |
  |                  |   |  Local costmap   |
  +------------------+   |  Inflation layer |
        |                |  Obstacle layer   |
  cmd_vel (v, omega)     +------------------+

COSTMAPS:
  Each cell stores a cost value (0=free, 254=inscribed, 255=lethal obstacle).
  Layers: obstacle layer (from sensor data) + inflation layer (safety buffer).
  Global costmap: coarse, full environment.
  Local costmap: fine, rolling window around robot.

BEHAVIOR TREES (BT.cpp):
  Nav2 uses XML-defined behavior trees for high-level logic.
  Replaces finite state machines from Nav1.
  Nodes: Sequence, Fallback, Action, Condition.
  Example: [Navigate -> Recover if stuck -> Spin -> Wait -> Navigate again]

NAVIGATION2 CLI:
  ros2 action send_goal /navigate_to_pose \
    nav2_msgs/action/NavigateToPose \
    "{pose: {header: {frame_id: map}, pose: {position: {x: 1.0, y: 2.0}}}}"
```

---

## MoveIt2 (Manipulation)

MoveIt2 is the motion planning and kinematics library for robotic arms.

```
MOVEIT2 ARCHITECTURE:

  User request: "move to pose X"
        |
  +---------------------+
  |  MOVE GROUP INTERFACE|  High-level API: plan, execute, query state.
  +---------------------+
        |
  +---------------------+   +---------------------+
  |  MOTION PLANNING     |   |  PLANNING SCENE      |
  |  FRAMEWORK (OMPL)    |   |  Collision objects   |
  |  RRTConnect default  |   |  ACM (allowed        |
  |  PILZ (industrial)   |   |  collision matrix)   |
  +---------------------+   | Robot model (URDF)  |
        |                   +---------------------+
  +---------------------+
  |  TRAJECTORY EXECUTION|
  |  JointTrajectoryCtrl |
  |  follow_joint_traj   |
  +---------------------+
        |
  ros2_control (hardware interface)

ROBOT MODEL (URDF + SRDF):
  URDF: kinematics, geometry, physical properties (links, joints, inertia).
  SRDF: semantic: named states, planning groups, passive joints.
  Generated by: MoveIt Setup Assistant.

COLLISION OBJECTS:
  # Add a box to planning scene:
  box = CollisionObject()
  box.id = "table"
  box.header.frame_id = "world"
  box.primitives = [SolidPrimitive(type=BOX, dimensions=[0.5, 0.8, 0.1])]
  scene.add_collision_object(box)

OMPL PLANNERS:
  RRTConnect (default): fast, bidirectional, good for single queries.
  PRM: multi-query, good for repeated motions.
  STOMP/CHOMP: trajectory optimization.
  PILZ: deterministic, for industrial use (PTP, LIN, CIRC motion types).
```

---

## Simulation

### Gazebo / Ignition Gazebo

```
GAZEBO CLASSIC (versions 1-11):
  Physics engines: ODE (default), Bullet, DART, Simbody.
  ROS 1 native. Used widely but being deprecated.

IGNITION GAZEBO / GAZEBO HARMONIC (new):
  Renamed from Ignition to Gazebo (confusingly).
  Gazebo Harmonic = current stable LTS (2023+).
  Plugin-based, more modular than classic.
  Better: ROS 2 integration, material/sensor simulation, SDF format.
  Physics: DART (default in Gazebo Harmonic).

PHYSICS ENGINES:
  ODE:    Oldest. Good general purpose. Limited contact handling.
  Bullet: Widely used in games. Good rigid body contacts.
  DART:   Best for articulated systems (manipulators, legged). Used in research.
  Simbody: High-fidelity multi-body dynamics.

GAZEBO-ROS INTEGRATION:
  ros_gz_bridge: bridges Gazebo topics to ROS 2 topics.
  ros_gz_sim: spawns robots, applies controls.

ROBOT MODEL IN GAZEBO:
  SDF (Simulation Description Format): native Gazebo format.
  URDF -> SDF conversion via robot_description_utils or xacro.
```

### NVIDIA Isaac Sim

```
ISAAC SIM:
  GPU-accelerated, photorealistic robot simulation.
  Built on NVIDIA Omniverse platform (USD format).
  Uses PhysX 5.x physics engine.

  ADVANTAGES OVER GAZEBO:
    Photorealistic rendering: domain randomization for sim-to-real.
    GPU physics: 1000s of parallel simulations (RL training).
    RTX sensors: physically accurate LiDAR and cameras.
    Python API: accessible via Isaac Lab.

  ISAAC LAB:
    Open-source RL training framework on top of Isaac Sim.
    Trains locomotion, manipulation, dexterity policies.
    Train in minutes what would take days on CPU sim.
    Directly produces policies deployable to real robots.

  REQUIREMENTS: NVIDIA RTX GPU (10+ GB VRAM recommended).
  COST: Free for research. Licensing for commercial use.
```

---

## ROS 2 CLI Cheat Sheet

```
NODE COMMANDS:
  ros2 node list                     <- list all running nodes
  ros2 node info /node_name          <- topics, services, parameters of node

TOPIC COMMANDS:
  ros2 topic list                    <- all topics
  ros2 topic echo /topic_name        <- print messages
  ros2 topic hz /topic_name          <- measure publish rate
  ros2 topic bw /topic_name          <- measure bandwidth
  ros2 topic pub /topic geometry_msgs/msg/Twist "{linear: {x: 0.5}}"

SERVICE COMMANDS:
  ros2 service list                  <- all services
  ros2 service call /add_two_ints \
    example_interfaces/srv/AddTwoInts "{a: 1, b: 2}"

ACTION COMMANDS:
  ros2 action list                   <- all actions
  ros2 action send_goal /action_name action_type "{goal_field: value}"

PARAMETER COMMANDS:
  ros2 param list /node_name
  ros2 param get /node_name param_name
  ros2 param set /node_name param_name value

BAG COMMANDS (record/replay):
  ros2 bag record -o bag_name /topic1 /topic2    <- record
  ros2 bag play bag_name                          <- replay
  ros2 bag info bag_name                          <- inspect

BUILD:
  colcon build --symlink-install    <- faster iteration (Python: no rebuild)
  colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

LAUNCH:
  ros2 launch package_name launch_file.launch.py
  ros2 run package_name executable_name
```

---

## Standard Message Types

```
COMMON MESSAGE PACKAGES:
  std_msgs:     String, Bool, Int32, Float64, Header
  geometry_msgs: Pose, Twist, Transform, Wrench, Vector3, Quaternion
  sensor_msgs:  Image, PointCloud2, LaserScan, Imu, JointState
  nav_msgs:     Odometry, Path, OccupancyGrid, MapMetaData
  tf2_msgs:     TFMessage (transform tree)

TRANSFORM TREE (TF2):
  Every robot frame relationship stored in /tf and /tf_static topics.
  robot_state_publisher: publishes URDF joint transforms.
  tf2_ros:

  # Look up transform (Python):
  tf_buffer = Buffer()
  t = tf_buffer.lookup_transform("base_link", "camera_link", rclpy.time.Time())

  # Full robot transform tree:
  ros2 run tf2_tools view_frames   <- generates PDF of all frames
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Mobile robot navigation | Nav2 (AMCL + A* + DWB) |
| Arm motion planning | MoveIt2 (OMPL + RRTConnect) |
| Sensor data streaming | ROS 2 topic, BEST_EFFORT QoS |
| Long-running task with feedback | ROS 2 action |
| Configuration that changes at runtime | ROS 2 parameter |
| Startup order control | Lifecycle nodes + lifecycle_manager |
| Robot simulation (casual/research) | Gazebo Harmonic |
| RL training (GPU, large scale) | Isaac Sim + Isaac Lab |
| Record robot data | ros2 bag record |
| Debug node graph | rqt_graph |
| Visualize data | rviz2 |
| Build packages | colcon build |
| Real-time motor control | ros2_control + EtherCAT driver |

---

## Common Confusion Points

**ROS 2 is not an operating system**
"Robot Operating System" is a misnomer. ROS 2 runs on top of Linux/macOS/Windows.
It provides communication, tooling, and package management for robot software.
Think of it as the middleware layer, like a message bus (similar in concept to
Azure Service Bus) plus a build system, plus a package registry (packages.ros.org).

**DDS discovery can fail in complex networks**
Multicast is required for DDS participant discovery. It fails across VLANs, NAT, most
cloud VMs, and corporate networks that block multicast. For these cases: configure
Fast DDS with explicit peer unicast list, or use a discovery server (DDS router).

**Topics vs Services vs Actions: choose correctly**
Use topics for continuous sensor data streams (camera, LiDAR, joint states).
Use services for quick queries (get current map, set parameter).
Use actions for operations that take multiple seconds and you want cancellation
(navigate to waypoint, execute arm trajectory, run a task sequence).
Using services for long operations blocks the client and has no cancellation.

**ros2_control is separate from Nav2/MoveIt2**
ros2_control handles the hardware-abstraction layer (motor drives, hardware interfaces).
Nav2 and MoveIt2 are higher-level applications that output trajectory commands which
ros2_control follows. The JointTrajectoryController in ros2_control bridges MoveIt2
plans to motor drive commands. These are three separate packages with clean interfaces.

**Gazebo Classic vs Ignition Gazebo vs Gazebo (new branding)**
Gazebo Classic: old (versions 1-11), being deprecated but still widely used.
Ignition Gazebo: new, renamed mid-stream.
Gazebo Harmonic: the current stable release of the new simulator (was Ignition).
When you see tutorials saying "Gazebo" without qualification, check the year:
pre-2022 = almost certainly Classic. Post-2022 = likely Gazebo Harmonic.
