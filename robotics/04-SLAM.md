# Robotics — SLAM (Simultaneous Localization and Mapping)

## The Big Picture

SLAM is the chicken-and-egg problem: you need a map to localize, and you need your
pose to build a map. SLAM solves both simultaneously.

```
+===========================================================================+
|                          SLAM LANDSCAPE                                   |
+===========================================================================+
|                                                                           |
|  THE PROBLEM:                                                             |
|    p(x_{1:t}, m | z_{1:t}, u_{1:t})                                       |
|    ^^^^^^^^^   ^   ^^^^^^^^^^^^^^^^                                       |
|    robot trajectory + map | observations + controls                       |
|    <- ESTIMATE THESE ->     <- GIVEN THESE ->                             |
|                                                                           |
|  FILTER-BASED               GRAPH-BASED                                   |
|  (online, sequential)       (offline, batch optimization)                 |
|  ==================         ==================================             |
|  EKF-SLAM                   Pose Graph / Factor Graph                     |
|    Landmark-based           g2o / GTSAM / Ceres                           |
|    O(n^2) in landmarks      Handles loop closure globally                 |
|    < 100 landmarks          Millions of poses possible                    |
|                                                                           |
|  Particle Filter (FastSLAM) VISUAL SLAM          LIDAR SLAM               |
|    Multi-modal posteriors   ORB-SLAM3             LOAM / LIO-SAM           |
|    Rao-Blackwellized        Feature-based         Scan matching            |
|    Handles non-Gaussianity  Keyframe selection    IMU pre-integration      |
|                             Loop closure (BoW)    NDT / ICP                |
|                                                                           |
|  MAP REPRESENTATIONS:                                                     |
|    Landmark cloud   Occupancy grid   Point cloud   Mesh   NeRF             |
|                                                                           |
+===========================================================================+
```

---

## The SLAM Problem Formulation

### Probabilistic State Estimation

SLAM is a Bayesian estimation problem. Define:

```
x_{1:t}: robot trajectory (poses at all timesteps up to t)
m:       map (landmark positions, occupancy grid, or other representation)
z_{1:t}: sensor observations (LiDAR scans, camera frames, encoder ticks)
u_{1:t}: control inputs (wheel commands, joint torques)

FULL SLAM (offline):
  Estimate p(x_{1:t}, m | z_{1:t}, u_{1:t})
  Process all data batch. Best accuracy. Used for post-processing.

ONLINE SLAM (real-time):
  Estimate p(x_t, m | z_{1:t}, u_{1:t})
  Only marginal over current pose. Must run in real time.

COMPONENTS:
  1. Motion model:       p(x_t | x_{t-1}, u_t)   "where did I go?"
  2. Observation model:  p(z_t | x_t, m)           "what would I see here?"
  3. Map model:          how landmarks or grid cells relate to poses
```

---

## Occupancy Grid Maps

The most practical 2D map representation for mobile robots.

```
OCCUPANCY GRID:
  Discretize space into a 2D grid of cells.
  Each cell stores: log-odds probability of being occupied.

  log_odds(p) = log(p / (1-p))

  Initial value: 0  (= probability 0.5, unknown)
  After measuring free space: subtract log_odds_free (e.g., -0.4)
  After measuring occupied:   add log_odds_occ  (e.g., +0.9)
  Clamp to [-5, 5] to avoid saturation.

  Convert back to probability: p = 1 - 1/(1 + exp(log_odds))

BAYESIAN UPDATE (per cell):
  l_t(x,y) = l_{t-1}(x,y) + l_occ_or_free - l_0
             ^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^   ^^^
             prior            sensor update      prior correction

LIDAR RAY CASTING:
  For each LiDAR ray:
    - All cells along the ray before endpoint: mark free (subtract log_odds_free)
    - Cell at endpoint: mark occupied (add log_odds_occ)
    Bresenham's line algorithm for efficiency.

RESOLUTION TRADE-OFFS:
  5 cm cells: detailed, large memory for big environments
  25 cm cells: coarse, fast, sufficient for navigation
  1 cm cells: extremely detailed, for manipulation workspace

EXAMPLE:
  100m x 100m environment at 5cm resolution:
  2000 x 2000 = 4,000,000 cells. Fine for a modern CPU.
```

---

## EKF-SLAM

The classical SLAM algorithm. History: Durrant-Whyte and Bailey (2006). Theoretically
optimal for linear Gaussian systems, but has scaling problems.

### State Vector

```
State vector includes BOTH robot pose and ALL landmark positions:

  x = [x_robot, y_robot, theta_robot,   <- robot pose (3)
       lx_1, ly_1,                       <- landmark 1 (2)
       lx_2, ly_2,                       <- landmark 2 (2)
       ...
       lx_n, ly_n]                       <- landmark n (2)

  Total: 3 + 2n dimensions.
  Covariance matrix P: (3+2n) x (3+2n)
```

### EKF-SLAM Algorithm

```
PREDICTION (robot moves):
  Apply motion model to robot pose component of x.
  Update covariance P using Jacobian of motion model F.
  Landmark positions unchanged (map doesn't move).

UPDATE (landmark observed):
  Compute expected observation h(x_i, landmark_j)
    = [expected distance, expected bearing]^T
  Compute innovation: z_measured - z_expected
  Compute Kalman gain K using measurement Jacobian H.
  Update full state x and covariance P.

DATA ASSOCIATION (which landmark is this?):
  Match observed landmark to known landmarks.
  Use nearest-neighbor, Mahalanobis distance, or Hungarian algorithm.
  CRITICAL: wrong association = filter divergence.

NEW LANDMARK INITIALIZATION:
  If no match: add new landmark to state vector.
  Augment x and P accordingly.

COMPLEXITY:
  Update step: O(n^2) due to P matrix manipulation.
  Memory: O(n^2) for covariance.
  In practice: degrades badly beyond ~100 landmarks.
```

### EKF-SLAM Limitation Visualization

```
  Covariance matrix P for n=3 landmarks:
  (3+2*3) x (3+2*3) = 9x9

  +--+--+--+--+--+--+--+--+--+
  |Rr Rl1 Rl2 Rl3|   <- robot-robot, robot-landmark correlations
  |   L1  L1L2 ..|   <- landmark-landmark correlations
  |              |
  +--+--+--+--+--+
  All entries are correlated!
  Every landmark observation updates EVERY landmark covariance.
  n=100 landmarks: 200x200 = 40,000 matrix entries.
  n=1000 landmarks: unfeasible in real time.
```

---

## Particle Filter SLAM (FastSLAM)

FastSLAM (Montemerlo, 2002) solves the EKF scaling problem using Rao-Blackwellization:
factorize the posterior so each particle maintains its own map.

```
FACTORIZATION:
  p(x_{1:t}, m | z_{1:t}, u_{1:t})
  = p(x_{1:t} | z_{1:t}, u_{1:t})   <- robot trajectory (particle filter)
  * product_j p(m_j | x_{1:t}, z_{1:t})  <- independent landmark estimates

KEY INSIGHT:
  Given the robot trajectory, landmarks are INDEPENDENT.
  Each particle gets its OWN set of independent EKF landmark filters.

PARTICLE FILTER:
  N particles, each representing a hypothesis about robot trajectory.
  Each particle i has weight w_i and landmark set {EKF_j(i)}.

ALGORITHM PER TIMESTEP:
  1. SAMPLE: draw N new poses from motion model.
  2. OBSERVE: for each particle, update landmark EKFs.
  3. WEIGHT: score each particle by how well observations match landmarks.
  4. RESAMPLE: sample N particles proportional to weights.
     (low-variance resampling to avoid particle collapse)

COMPLEXITY:
  O(M * K) where M = # particles, K = # landmarks observed at once.
  Much better than EKF for large landmark counts.
  Typical M: 50-500 particles.
  Trade-off: particle degeneracy in high-dimensional spaces.
```

---

## Graph SLAM

Modern SLAM systems use factor graphs for batch optimization. This handles large
environments and loop closures cleanly.

### Pose Graph Formulation

```
NODES: robot poses x_1, x_2, ..., x_t
EDGES: constraints between poses

  ODOMETRY EDGE: consecutive poses connected by motion model.
    x_{i+1} = f(x_i, u_i) + noise
    Edge represents: "given I was at x_i and moved u_i, I should be at x_{i+1}"

  LOOP CLOSURE EDGE: non-consecutive poses identified as the same place.
    x_i ~ x_j (same location visited at different times)
    This is the global correction -- fixes accumulated drift.

POSE GRAPH:
  x1 - x2 - x3 - x4 - x5 - x6
                 |              |
                 +--- odom ---x7+--- LOOP CLOSURE (x6 ~ x2)
                                    (detected: same place visited again)
```

### Factor Graph Optimization

```
FACTOR GRAPH (more general than pose graph):
  Variables: poses x_i, landmark positions l_j
  Factors: probability functions connecting variables

  F(x, l) = product_i product_j factor(x_i, l_j, z_{ij})

OPTIMIZATION:
  Find x*, l* = argmax F(x,l)
  Equivalent to nonlinear least squares:
  min_x sum_i || z_i - h_i(x) ||^2_{information_i}

SOLVERS:
  g2o (Kummerle, 2011):   general graph optimization, widely used in ROS
  GTSAM (Dellaert, 2006): factor graph library, iSAM2 incremental solver
  Ceres Solver (Google):  general nonlinear least squares, used in Cartographer
  iSAM2:                  incremental update without re-solving from scratch

INCREMENTAL SOLVING (iSAM2):
  Key: when new factor arrives, only relinearize affected variables.
  Bayes tree data structure makes this efficient.
  Real-time capable for large-scale mapping.
```

---

## Visual SLAM: ORB-SLAM3

ORB-SLAM3 (Campos, 2021) is the state-of-the-art feature-based visual SLAM system.
Handles monocular, stereo, RGB-D, and inertial (IMU) configurations.

### Pipeline

```
INPUT FRAME
     |
     v
+------------------+
|  ORB EXTRACTION  |   Extract ORB (Oriented FAST + Rotated BRIEF) features.
|                  |   ~1000-3000 keypoints per frame. Scale-invariant.
+------------------+
     |
     v
+------------------+
|    TRACKING      |   Match current frame features to map points.
|                  |   Pose optimization (minimize reprojection error).
|                  |   Motion model: constant velocity assumption for init.
+------------------+
     |
     v
+------------------+
|  KEYFRAME SELECT |   Insert keyframe if: translation > threshold OR
|                  |   insufficient map points tracked.
|                  |   Keyframes keep a sparse set of "good" frames.
+------------------+
     |
     v
+------------------+
|  LOCAL MAPPING   |   Triangulate new map points from keyframe pairs.
|                  |   Bundle adjustment: optimize local keyframe poses
|                  |   + map points jointly. (Schur complement for speed.)
+------------------+
     |
     v
+------------------+
|  LOOP CLOSING    |   Detect revisited places using DBoW2 (bag-of-words).
|                  |   Verify loop closure geometrically (RANSAC).
|                  |   Correct drift: pose graph optimization.
|                  |   Fuse duplicate map points.
+------------------+
     |
     v
+------------------+
|  MAP REUSE       |   Save map. Reload and relocalize in saved map.
|                  |   Multi-session mapping.
+------------------+
```

### ORB Features

```
ORB = Oriented FAST + Rotated BRIEF

FAST keypoint detector: very fast, scale-space pyramid.
BRIEF descriptor: binary (256 bits). XOR comparison = very fast matching.
Oriented: compensate for rotation (makes descriptor rotation-invariant).
Scale pyramid: detect features at multiple scales.

Matching: Hamming distance of 256-bit descriptors. <30 bits = good match.
Outlier rejection: RANSAC with Essential/Homography matrix.
```

---

## LiDAR SLAM: LOAM and LIO-SAM

### LOAM (Lidar Odometry and Mapping)

```
LOAM (Zhang & Singh, 2014):
  Two simultaneously running algorithms:
  1. Odometry at 10 Hz: coarse, scan-to-scan matching.
  2. Mapping at 1 Hz: fine, scan-to-map matching.

  Feature extraction from LiDAR scan:
    Edge features: high curvature points (corners)
    Planar features: low curvature points (flat surfaces)

  Registration: match features to map using point-to-edge and
  point-to-plane distances. Levenberg-Marquardt optimization.

LOAM-variants:
  LeGO-LOAM: lightweight, ground-segmented, outdoor mobile robots.
  LiLi-OM: multiple LiDAR configurations.
  F-LOAM: faster LOAM without iterative optimization.
```

### LIO-SAM (Shan, 2020)

```
LIO-SAM (Lidar-Inertial Odometry via Smoothing and Mapping):

  Key improvement over LOAM: tightly-coupled IMU pre-integration.

  IMU pre-integration: accumulate IMU measurements between LiDAR scans.
  Provides: initial pose guess for scan matching (much faster convergence).
  Also: deskewing -- remove motion distortion from spinning LiDAR scan.

  Factor graph (GTSAM):
    IMU pre-integration factors
    LiDAR odometry factors
    GPS factors (if available)
    Loop closure factors

  This is the dominant approach for autonomous vehicle outdoor SLAM (2020-present).
  Also: FAST-LIO2 (HKU), more computationally efficient.
```

---

## Loop Closure Detection

Loop closure = recognizing that you've visited a place before.
Without loop closure, SLAM drift accumulates without bound.

### Bag-of-Words (Visual)

```
BUILDING A VOCABULARY:
  1. Collect large image dataset.
  2. Extract ORB/SIFT/SuperPoint features from all images.
  3. K-means cluster features into "visual words" (vocabulary tree).
  4. Vocabulary: hierarchical tree, ~10^5 to 10^6 words.

QUERY:
  New image -> extract features -> quantize to visual words -> TF-IDF vector.
  Compare against database of keyframe TF-IDF vectors (fast dot product).
  High similarity score = possible loop closure.

VERIFICATION:
  Geometric verification: check that matched images have consistent geometry.
  RANSAC with Essential matrix. Required to reject false positives.

LIBRARY: DBoW2 (used in ORB-SLAM), DBoW3, HFNET (learned).
```

### Scan Context (LiDAR)

```
SCAN CONTEXT (Kim & Kim, 2018):
  Encode a 3D LiDAR scan as a 2D matrix:
    - Rows: azimuth sectors (0-360 degrees)
    - Cols: range rings (concentric)
    - Value: max height of points in that sector-ring

  Rotation-invariant comparison via column-shift search.
  Fast retrieval via two-stage approach: ring key (coarse) + scan context (fine).
  Works even with 180-degree viewpoint change.
  Used in LIO-SAM, ALOAM.
```

---

## Map Representations Comparison

```
+------------------+----------+----------+----------+----------+-----------+
| Representation   | Memory   | Dense?   | Queryable| Update   | Example   |
|                  |          |          | path plan| rate     | system    |
+------------------+----------+----------+----------+----------+-----------+
| Landmark cloud   | Low      | No       | No       | Fast     | EKF-SLAM  |
| Occupancy grid   | Med-High | Yes (2D) | Yes      | Med      | GMapping  |
| 3D point cloud   | Very high| Yes (3D) | Limited  | Slow     | LOAM      |
| Voxel map (OcTree)| Med     | Yes (3D) | Yes      | Med      | OctoMap   |
| Mesh             | Med      | Yes (3D) | Hard     | Slow     | RTABMap   |
| Signed distance  | Med-High | Yes (3D) | Yes      | Fast     | KinectFusion|
| NeRF / 3DGS      | Low-Med  | Dense    | No (yet) | Slow     | iNeRF     |
+------------------+----------+----------+----------+----------+-----------+
```

---

## SLAM Systems Reference

| System | Modality | Map type | Loop closure | Open source? |
|--------|----------|----------|--------------|--------------|
| GMapping | 2D LiDAR | Occ. grid | No | Yes (ROS) |
| Cartographer (Google) | 2D/3D LiDAR | Submap + pose graph | Yes | Yes |
| ORB-SLAM3 | Camera (+ IMU) | 3D landmarks | Yes (BoW) | Yes |
| RTAB-Map | Camera/LiDAR | 3D point cloud | Yes | Yes (ROS) |
| LOAM / LIO-SAM | 3D LiDAR + IMU | 3D map | Yes (SC) | Yes |
| FAST-LIO2 | 3D LiDAR + IMU | iKd-tree | Limited | Yes |
| OpenVSLAM | Camera | 3D landmarks | Yes | Yes |
| ElasticFusion | RGB-D | Surfel map | Yes | Yes |

---

## Decision Cheat Sheet

| Scenario | Recommended approach |
|----------|---------------------|
| Indoor flat floor, 2D navigation | GMapping or Cartographer 2D |
| Indoor 3D with robot arm | RTAB-Map or ORB-SLAM3 with RGB-D |
| Outdoor autonomous vehicle | LIO-SAM or Cartographer 3D |
| Visual only, no LiDAR | ORB-SLAM3 monocular or stereo |
| Real-time, computationally limited | FAST-LIO2 (very efficient) |
| Need dense map for grasping | ElasticFusion or KinectFusion |
| Large-scale multi-session | ORB-SLAM3 atlas (map reuse) |
| Loop closure only (no full SLAM) | Scan Context for re-ID |

---

## Common Confusion Points

**"SLAM solves localization AND mapping simultaneously" -- but one at a time matters more**
In practice, for a known map, you only need localization (AMCL in Nav2 is standard).
Full SLAM (building the map) is needed when the environment is new or changing.
Most warehouse robots use SLAM once to build a map, then switch to pure localization.

**EKF-SLAM vs Graph SLAM: not competing, different regimes**
EKF-SLAM works well for small-scale (< 100 landmarks), low-latency applications.
Graph SLAM works for large-scale, handles loop closure correctly, is now the standard
for any serious outdoor or building-scale system. EKF-SLAM is largely of historical
interest today.

**Loop closure = drift correction, not teleportation**
When a loop closure is detected, the pose graph optimizer distributes the error
across all poses in the loop. The robot's estimated position might jump slightly.
This can confuse a controller following a trajectory -- the robot needs to be aware
that its map frame may have shifted under it.

**"SLAM gives absolute position" -- false**
SLAM builds a consistent internal map and localizes within it. It does NOT provide
GPS-level absolute global coordinates. For absolute coordinates, GPS or a surveyed
map is needed. SLAM gives relative consistency (no drift within the map), not
absolute accuracy (where the map is on Earth).

**Particle filter degeneracy**
With too few particles, the particle filter can "collapse" -- all particles near
one hypothesis, which may be wrong. The robot gets lost and must recover. FastSLAM
ameliorates this but does not eliminate it. Particle count vs computational cost
is the main tuning knob.
