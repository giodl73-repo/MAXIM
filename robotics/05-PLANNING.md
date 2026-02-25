# Robotics — Motion Planning

## The Big Picture

Planning is a hierarchy: abstract goals get refined into geometry, then into time-parameterized
trajectories, then into control references.

```
+===========================================================================+
|                        MOTION PLANNING LANDSCAPE                          |
+===========================================================================+
|                                                                           |
|  TASK PLANNING              PATH PLANNING            TRAJECTORY PLANNING   |
|  (symbolic)                 (geometric)              (time-parameterized)  |
|  ============               ============             ==================    |
|  What to do?                Where to go?             When to be where?    |
|  PDDL / behavior trees      C-space: RRT, PRM, A*    CHOMP, min-snap      |
|  LLM reasoning              Obstacle avoidance       Velocity profiles     |
|  1-10 Hz                    1-100 Hz                 100-1000 Hz           |
|                                                                           |
|  INPUT: task goal           INPUT: start, goal,      INPUT: waypoints,     |
|         world state                obstacle map             constraints     |
|  OUTPUT: action sequence    OUTPUT: collision-free   OUTPUT: q(t), q_dot(t)|
|                                     waypoints                q_ddot(t)     |
|                                                                           |
|  REACTIVE CONTROL           COLLISION CHECKING       TASK-AND-MOTION       |
|  Potential fields           GJK/EPA                  PDDLStream            |
|  Velocity obstacles         BVH (AABB, OBB)          STRIPS operators      |
|  DWA / MPC                  Continuous (CCD)         Geometric constraints |
|                                                                           |
+===========================================================================+
```

---

## Configuration Space (C-space)

All planning algorithms work in configuration space, not Cartesian space.

```
CONFIGURATION SPACE:
  C = set of all robot configurations q = [q1, q2, ..., qn]
  For an n-DOF robot: C is an n-dimensional space.

  C_free: configurations with no collision (robot + environment).
  C_obs:  configurations causing collision.

  GOAL: find a path from q_start to q_goal that stays in C_free.

WHY NOT PLAN IN CARTESIAN SPACE?
  A robot arm tip can be at (x,y,z) with many different joint configurations.
  C-space captures ALL constraints (joint limits, self-collision, obstacles).
  Cartesian path planning misses configurations that are unreachable
  even if the Cartesian path seems clear.

EXAMPLE: 2-DOF arm in C-space
  q1: [0, 2*pi)    <- joint 1 angle
  q2: [-pi, pi)    <- joint 2 angle
  C is a 2D torus. Obstacles project as "forbidden zones" in the torus.

C-SPACE OBSTACLE:
  An obstacle in workspace maps to a REGION in C-space.
  The robot might have many configurations that put any link inside the obstacle.
  These all form a connected region in C-space.
  Cannot be computed analytically for general robots -- hence sampling.
```

---

## Graph Search Planners

### A* (Heuristic Search)

For grid-based environments (occupancy grids), A* is the standard.

```
A* ALGORITHM:
  OPEN: priority queue of nodes to expand (sorted by f = g + h)
  CLOSED: set of already-expanded nodes

  f(n) = g(n) + h(n)
  g(n): cost from start to n (exact)
  h(n): heuristic estimate of cost from n to goal

  ADMISSIBLE HEURISTIC: h(n) <= actual cost to goal
    -> A* is guaranteed to find optimal path

  COMMON HEURISTICS:
    Euclidean distance: h = sqrt(dx^2 + dy^2)   [admissible]
    Manhattan distance: h = |dx| + |dy|          [admissible for 4-connected]
    Octile distance: for 8-connected grid         [admissible]

  ALGORITHM:
  while OPEN not empty:
    n = OPEN.pop()   (lowest f)
    if n == goal: return path
    for each neighbor m of n:
      g_new = g(n) + cost(n, m)
      if m not in CLOSED, or g_new < g(m):
        g(m) = g_new
        f(m) = g_new + h(m)
        parent(m) = n
        OPEN.push(m)
    CLOSED.add(n)

COMPLEXITY: O(b^d) worst case (b=branching factor, d=depth)
In practice with good h: near-linear in path length.
```

### D* Lite (Dynamic Replanning)

```
D* LITE (Koenig & Likhachev, 2002):
  A*-variant that efficiently replans when the world changes (new obstacles detected).
  Used in: Mars rovers, real-time navigation when sensor reveals new obstacles.

  Key idea: replanning is cheap because it only expands the changed portion of the
  search graph, not the whole grid from scratch.

  Used in: Karto SLAM, early DARPA autonomous vehicle contestants.
```

---

## Sampling-Based Planners

For high-dimensional C-spaces (6+ DOF arms), grid-based search is infeasible.
Sampling-based planners explore C_free by sampling random configurations.

### PRM (Probabilistic Roadmap Method)

```
PRM (Kavraki, 1996): OFFLINE, MULTI-QUERY

PHASE 1 -- LEARNING (offline):
  Repeat N times:
    1. Sample random q in C.
    2. If q is collision-free (in C_free):
       a. Find k nearest neighbors in roadmap.
       b. Try to connect q to each neighbor via local planner.
       c. Add edge if connection is collision-free.
  Result: a roadmap graph G = (V, E) covering C_free.

PHASE 2 -- QUERY (online, fast):
  Given q_start, q_goal:
    1. Connect q_start and q_goal to roadmap.
    2. Find path in graph G using A* or Dijkstra.
  Very fast if roadmap is already built.

GOOD FOR: multiple queries in same environment (assembly, warehouse).
BAD FOR: dynamic environments (roadmap must be rebuilt when obstacles change).

LOCAL PLANNER:
  Simplest: straight-line interpolation in C-space.
  Check collision along the line at small intervals (delta = 0.01 rad).
  Only proceed if ALL sampled configurations along the line are collision-free.
```

### RRT (Rapidly-Exploring Random Tree)

```
RRT (LaValle, 1998): ONLINE, SINGLE-QUERY

ALGORITHM:
  T = {q_start}
  for i = 1 to N:
    q_rand = sample_random_config()     <- uniform random in C
    q_near = nearest_node(T, q_rand)    <- closest node in tree (Euclidean)
    q_new  = steer(q_near, q_rand, step_size)  <- move step_size toward q_rand
    if collision_free(q_near, q_new):
      T.add_node(q_new)
      T.add_edge(q_near, q_new)
      if ||q_new - q_goal|| < epsilon:
        return path(T, q_start, q_new)  <- success!
  return failure

KEY PARAMETERS:
  step_size: 0.01-0.1 rad (smaller = better but slower)
  N: 5,000-100,000 iterations
  Goal bias: with probability p_goal, sample q_goal instead of random
             (p_goal = 0.05-0.1, helps converge)

PROPERTIES:
  Probabilistically complete: will find solution if one exists (given enough samples).
  NOT optimal: path is jagged and usually suboptimal.
  Good for:   single-query planning in high-dimensional C-space.
              Real-time arm motion planning.
```

### RRT* (Asymptotically Optimal RRT)

```
RRT* (Karaman & Frazzoli, 2011):
  Adds two steps to RRT to achieve asymptotic optimality:

  1. NEAR NODES: instead of just 1 nearest neighbor, find all nodes within
     radius r (r shrinks as tree grows: r = gamma*(log(n)/n)^{1/d}).

  2. REWIRING:
     a. Choose q_new's parent = the near node minimizing total cost to q_new.
        (not just q_near, but the best of all near nodes.)
     b. For each near node q_near_i:
        If cost(q_start -> q_new -> q_near_i) < cost(q_start -> q_near_i):
          rewire: make q_new the parent of q_near_i.

  RESULT: As N -> inf, path converges to the optimal path.
  COST: O(n log n) per iteration vs O(1) for RRT. Slower but better quality.

RRT* PATH QUALITY vs ITERATION COUNT:
  n=1000:   ~30% above optimal
  n=10000:  ~10% above optimal
  n=100000: ~3% above optimal
  Sufficient quality usually reached well before convergence.

BIDIRECTIONAL RRT (BiRRT):
  Grow two trees: one from q_start, one from q_goal.
  Connect when they are close enough.
  2-5x faster than single-tree RRT in practice.
  Used in: MoveIt2 OMPL integration.
```

---

## Trajectory Optimization

Once you have a rough path (from RRT or similar), you want a smooth, dynamically
feasible, obstacle-avoiding trajectory. Trajectory optimization refines the path.

### CHOMP (Covariant Hamiltonian Optimization for Motion Planning)

```
CHOMP (Ratliff, 2009):
  Optimize trajectory xi (a sequence of q_0, q_1, ..., q_T) to minimize:

  U(xi) = f_obs(xi)  +  lambda * f_smooth(xi)
           ^^^^^^^^^      ^^^^^^^^^^^^^^^^^^
           obstacle cost   smoothness cost (finite differences)

  f_obs: signed distance from obstacles along trajectory.
         Pushes trajectory away from obstacles.
         Gradient: dU/dxi computed from obstacle distance field.

  f_smooth: penalizes jerk/acceleration (high-order finite differences).
             Encourages smooth, dynamically-comfortable motions.

  OPTIMIZATION: gradient descent on xi.
    xi_{k+1} = xi_k - eta * A^{-1} * gradient U(xi_k)
    A^{-1}: preconditioner (accounts for trajectory parameterization).

  RESULT: smooth, obstacle-avoiding trajectory in C-space.
  LIMITATION: can get stuck in local minima. Multiple restarts help.
```

### Minimum-Snap Trajectory (Quadrotors)

```
MINIMUM-SNAP TRAJECTORY (Mellinger & Kumar, 2011):
  For quadrotors: minimize snap (4th derivative of position).
  Snap couples to roll/pitch, so minimizing it reduces aggressive attitude changes.

  Polynomial segments: each segment is degree-7 polynomial.
  Constraints: start, end, waypoint positions and derivatives.
  Solve: quadratic program (QP) for polynomial coefficients.

  RESULT: smooth, differentially flat trajectory.
          Can be tracked by attitude controller with low tracking error.

  Also used for: manipulation path smoothing, autonomous vehicle planning.
```

---

## Reactive Planning

Reactive methods respond to sensor data in real time without global planning.
Good for dynamic environments but susceptible to local minima.

### Potential Fields

```
POTENTIAL FIELD (Khatib, 1986):
  Attractive potential: pulls robot toward goal.
  Repulsive potential: pushes robot away from obstacles.

  U_att = 0.5 * k_att * || q - q_goal ||^2
  U_rep = 0.5 * k_rep * (1/d - 1/d_0)^2   if d < d_0, else 0

  where d = distance to nearest obstacle
        d_0 = influence radius

  Force (negative gradient):
  F_att = -grad U_att = k_att * (q_goal - q)
  F_rep = -grad U_rep = k_rep * (1/d - 1/d_0) * (1/d^2) * grad_d

  Robot "falls downhill" in the combined potential field.

  LIMITATION: LOCAL MINIMA.
    Robot can get stuck where F_att + F_rep = 0, but not at goal.
    Common in corridors, narrow passages.
    Mitigation: random perturbation, wavefront potential (guaranteed no local min).
```

### Dynamic Window Approach (DWA)

```
DWA (Fox, 1997):
  Used in Nav2 (ROS 2) for local obstacle avoidance.

  At each timestep:
  1. Compute "dynamic window": all (v, omega) achievable in one timestep
     given current velocity + acceleration limits.
  2. Sample a grid of (v, omega) within the window.
  3. For each (v, omega): simulate robot forward dt.
  4. Score each trajectory: heading + clearance + velocity.
  5. Select highest-scoring (v, omega).
  6. Apply for one timestep. Repeat.

  FAST: runs at 10-50 Hz.
  GOOD FOR: wheeled mobile robots in indoor environments.
  BAD FOR: high-dimensional arms (C-space DWA is not standard).
```

### Velocity Obstacles (VO)

```
VELOCITY OBSTACLE (Fiorini & Shiller, 1998):
  For a robot A and moving obstacle B:
  VO_AB = {v_A | if A moves at v_A, A will collide with B (on current course)}

  Obstacle B moving at v_B "shifts" the VO:
  RVO (Reciprocal Velocity Obstacle): both agents share responsibility for avoidance.

  Each agent picks velocity OUTSIDE all velocity obstacles.
  Handles moving pedestrians, other robots.

  ORCA (Optimal Reciprocal Collision Avoidance):
    Linear programming to find closest v_A to preferred velocity
    that is outside all VOs.
    Used in: crowd simulation, multi-robot navigation.
```

---

## Task and Motion Planning (TAMP)

TAMP bridges symbolic task planning and continuous geometric planning.
The hardest and most active area in manipulation planning.

### PDDL (Planning Domain Definition Language)

```
PDDL STRUCTURE:
  DOMAIN file: defines predicates + actions.
  PROBLEM file: defines initial state + goal.

DOMAIN EXAMPLE (simplified pick-and-place):
  (:predicates
    (at-robot ?loc)
    (at-object ?obj ?loc)
    (holding ?obj)
    (empty-hand))

  (:action pick
    :parameters (?obj ?loc)
    :precondition (and (at-robot ?loc) (at-object ?obj ?loc) (empty-hand))
    :effect (and (holding ?obj) (not (at-object ?obj ?loc)) (not (empty-hand))))

  (:action move
    :parameters (?from ?to)
    :precondition (at-robot ?from)
    :effect (and (at-robot ?to) (not (at-robot ?from))))

PROBLEM EXAMPLE:
  (:init (at-robot kitchen) (at-object cup table) (empty-hand))
  (:goal (at-object cup counter))

SOLVER: Fast Downward, LAPKT produce a sequence of symbolic actions.
PROBLEM: symbolic plan says "pick cup" but does not say HOW (which grasp, path, etc.)
         -> requires geometric motion planning for execution.
```

### PDDLStream

```
PDDLStream (Garrett, 2020):
  Extends PDDL with "streams" -- generators that produce certified geometric facts.

  Stream: certifies that a geometric fact is true (with a feasible plan).
  Example: "grasp_stream(?obj) -> grasp_pose"
           runs IK + collision checking to certify the grasp is feasible.

  PDDLStream interleaves task planning with geometric feasibility checks.
  If a symbolic plan is geometrically infeasible, it backtracks in the task plan.

  This solves the fundamental TAMP problem: geometric constraints can invalidate
  symbolic plans ("pick cup from table" requires a collision-free approach path;
  if the table is blocked, the symbolic plan is infeasible -> replan symbolically).
```

---

## Collision Checking

Efficient collision detection is the inner loop of all sampling-based planners.

### GJK/EPA Algorithm

```
GJK (Gilbert-Johnson-Keerthi, 1988):
  Computes minimum distance between two convex shapes.
  Key insight: use the Minkowski difference shape.
  Iterative simplex algorithm.
  Complexity: near-O(1) amortized for similar shapes.

EPA (Expanding Polytope Algorithm):
  Extension of GJK for penetration depth (when shapes overlap).

Both are implemented in FCL (Flexible Collision Library) used by MoveIt2,
and in bullet physics, MuJoCo.
```

### Bounding Volume Hierarchies (BVH)

```
BVH for robotics collision:
  Approximate robot links with convex bounding volumes.
  Hierarchy: AABB (axis-aligned bounding box) at top, OBB/capsule at leaves.

  AABB: fast to test overlap, poor fit.
  OBB (oriented bounding box): better fit, slower test.
  Capsule (cylinder+sphere): very fast, great fit for robot links.

  Broad phase: AABB tree eliminates non-overlapping pairs quickly.
  Narrow phase: GJK/EPA for remaining candidate pairs.

  Self-collision check: run collision check between robot links.
  Robot model (URDF) defines allowed collision pairs (adjacent links OK).
```

---

## Decision Cheat Sheet

| Scenario | Algorithm |
|----------|-----------|
| 2D grid mobile robot navigation | A* on occupancy grid |
| 2D navigation with moving obstacles | D* Lite (dynamic replanning) |
| 6-DOF arm, single query, real time | RRT (BiRRT) or RRT-Connect |
| 6-DOF arm, multiple queries, known env | PRM (offline roadmap) |
| Optimal path required | RRT* (run to convergence) |
| Smooth trajectory from waypoints | CHOMP or trajectory optimization |
| Quadrotor trajectory | Minimum-snap polynomial |
| Mobile robot local avoidance | DWA (Nav2 default) |
| Multi-robot avoidance | ORCA velocity obstacles |
| Manipulation with symbolic constraints | TAMP: PDDLStream |
| High-level task reasoning | PDDL + geometric verifier |
| MoveIt2 arm planning | OMPL (RRT-Connect default) |

---

## Common Confusion Points

**"RRT is complete" means probabilistically complete, not complete**
RRT will find a path if enough samples are taken and one exists. But it may
require exponentially many samples in narrow passages. "Complete" in sampling-based
planning = "probability of finding a path approaches 1 as samples -> infinity."
Not the same as "always finds a path in finite time."

**Planning in C-space vs task space: which dimension counts**
A 6-DOF arm has 6D C-space. Collision checking is done in workspace (3D), but
the search tree is in C-space. The dimensionality that matters for RRT convergence
is the C-space dimension, not workspace. This is why arm planning (6D C-space)
is much harder than mobile robot planning (3D C-space: x, y, theta).

**CHOMP is not RRT with smoothing**
CHOMP is a trajectory optimizer that simultaneously avoids obstacles and smooths.
It starts from an initial trajectory (often a straight line in C-space) and
iterates. RRT produces a path; then you can optionally smooth it with shortcutting
or CHOMP. They are complementary, not competing.

**PDDL solves the task; it does not plan motion**
A PDDL planner outputs "move to location A, then pick object B, then move to C."
This is purely symbolic. Each action still requires a geometric motion planner
to execute (find collision-free path, compute IK, etc.). TAMP systems (like
PDDLStream) bridge these levels by making geometric feasibility a constraint on
the symbolic plan.

**Nav2 vs MoveIt2: different planning layers**
Nav2: mobile robot navigation (getting the base from A to B in a 2D map).
MoveIt2: manipulator arm planning (moving joints from configuration A to B).
Both use motion planning internally (Nav2 uses NavFn/SMAC; MoveIt2 uses OMPL),
but they operate on different robot subsystems and different state spaces.
