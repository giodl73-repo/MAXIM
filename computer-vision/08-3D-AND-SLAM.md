---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:3d-and-slam
kind: guide
module: computer-vision
section: computing-software
title: 3D Reconstruction and SLAM
status: source-custody
source_custody: partial
current_path: computer-vision/08-3D-AND-SLAM.md
canonical_path: computer-vision/08-3D-AND-SLAM.md
backsource_ids: [proof-backfill:computer-vision:08-3d-and-slam, git-history:computer-vision:08-3d-and-slam]
concepts: [structure from motion, bundle adjustment, multi-view stereo, point clouds, visual SLAM, NeRF]
root_concepts: [3D reconstruction]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# 3D Reconstruction and SLAM

## The Big Picture: From Many Images to a Map

Two views give one 3D point (guide 06). *Many* views, jointly, give a whole scene *and*
the camera trajectory that produced them. That joint recovery has two names depending on
context: **Structure-from-Motion** (SfM) when done offline from a photo collection, and
**SLAM** (Simultaneous Localization And Mapping) when done online on a moving robot or
phone. Both solve the same problem — estimate camera poses and 3D structure together — and
both are refined by the same optimizer: **bundle adjustment**.

```
+------------------------------------------------------------------------------+
|         MANY IMAGES -> CAMERA POSES + 3D STRUCTURE  (joint estimation)       |
|                                                                              |
|   input: overlapping images        output: poses + sparse/dense 3D           |
|                                                                              |
|     [img1][img2][img3]...           C1    C2    C3   (camera trajectory)     |
|         \    |    /                  \    |    /                             |
|          \   |   /         ==>        \   |   /     . . .  (3D points X_j)   |
|       feature matches                  \  |  /     . map .                   |
|       across views                      \ | /      . . . .                   |
|                                          scene                               |
|                                                                              |
|   SfM = offline (photo collection).  SLAM = online (live camera).            |
|   Same unknowns; same refiner (bundle adjustment).                           |
+------------------------------------------------------------------------------+
```

---

## Layer 1: Structure-from-Motion — The Offline Pipeline

SfM reconstructs a 3D scene and all camera poses from an unordered set of images (think:
reconstructing a cathedral from tourist photos). It chains the two-view geometry of
guide 06 across many images.

```
+------------------------------------------------------------------------------+
|                       STRUCTURE-FROM-MOTION PIPELINE                         |
|                                                                              |
|  1. FEATURES      extract SIFT/ORB keypoints in every image (guide 02)       |
|  2. MATCH         match features between image pairs; RANSAC-filter (g.06)   |
|  3. INITIALIZE    pick a good pair; estimate E -> (R,t); triangulate points  |
|  4. INCREMENTAL   for each new image: PnP pose from known 3D<->2D matches;   |
|     GROWTH        triangulate new points; repeat                             |
|  5. BUNDLE        globally refine ALL poses + ALL points by minimizing       |
|     ADJUST        reprojection error (next layer)                            |
|                                                                              |
|   Output: a SPARSE point cloud + every camera's pose. (COLMAP is the         |
|   reference open-source implementation.)                                     |
+------------------------------------------------------------------------------+
```

**PnP** (Perspective-n-Point) is the per-image localization step: given known 3D points
and their 2D projections in a new image, solve for that camera's pose `[R|t]`. It is the
single-camera analogue of the two-view pose recovery — a constrained least-squares /
minimal-solver problem (P3P needs just three points, then RANSAC).

**Bridge — linear algebra:** PnP, like the 8-point algorithm (guide 06), is a
least-squares/SVD problem with a minimal-solver core (P3P) wrapped in RANSAC for
robustness.

---

## Layer 2: Bundle Adjustment — The Optimizer That Ties It Together

Bundle adjustment (BA) is the gold-standard refinement: jointly adjust *all* camera
parameters and *all* 3D points to minimize the total **reprojection error** — the
pixel distance between each observed feature and where its 3D point projects.

```
+------------------------------------------------------------------------------+
|                       BUNDLE ADJUSTMENT                                      |
|                                                                              |
|   minimize over {camera poses P_i} and {3D points X_j}:                      |
|                                                                              |
|       E = SUM_i SUM_j  v_ij * || x_ij  -  project(P_i, X_j) ||^2             |
|                                                                              |
|   x_ij    = observed 2D feature of point j in image i                        |
|   project = the pinhole projection (guide 01)                                |
|   v_ij    = 1 if point j is visible in image i, else 0                       |
|                                                                              |
|   This is a huge NONLINEAR LEAST-SQUARES problem. Solved by                  |
|   Levenberg-Marquardt, exploiting the SPARSE block structure (most           |
|   points are seen by few cameras -> sparse Jacobian / Schur complement).     |
+------------------------------------------------------------------------------+
```

The name comes from the "bundles" of light rays converging at each camera center being
adjusted to meet optimally. The key to tractability is **sparsity**: each 3D point is seen
by only a handful of cameras, so the Jacobian is block-sparse and the normal equations are
solved via the Schur complement.

**Bridge — numerical methods:** BA is large-scale sparse nonlinear least squares —
Levenberg-Marquardt (a damped Gauss-Newton) on a problem whose sparsity pattern is
exploited exactly as in `numerical-methods/`. This is the workhorse of all geometric
vision.

---

## Layer 3: Multi-View Stereo — Going Dense

SfM produces a *sparse* cloud (only at matched features). **Multi-View Stereo** (MVS) uses
the now-known camera poses to compute a *dense* depth for nearly every pixel, yielding a
full surface.

```
+------------------------------------------------------------------------------+
|              SPARSE (SfM) -> DENSE (MVS) -> SURFACE                          |
|                                                                              |
|   SfM points (sparse)      MVS depth (dense)        meshed surface           |
|     .   .   .                ::::::::::::             /\/\/\/\               |
|       .   .          ->     ::::::::::::::   ->      |      |                |
|     .   .   .                ::::::::::::            \/\/\/\/                |
|                                                                              |
|   MVS idea: for each pixel, hypothesize depths along its ray; check          |
|   PHOTO-CONSISTENCY across the other views (does the patch look the same     |
|   when reprojected?). PatchMatch MVS is the standard fast method.            |
|                                                                              |
|   Then: depth maps -> fused point cloud -> Poisson surface reconstruction    |
|   -> textured MESH.                                                          |
+------------------------------------------------------------------------------+
```

Photo-consistency is the dense analogue of the matching cost in stereo (guide 06): the
correct depth is the one at which the pixel's neighborhood, reprojected into the other
images, looks consistent. Texture-less surfaces (white walls) break this and remain the
classic MVS failure case.

---

## Layer 4: Point Clouds and Surfaces

The raw 3D output is a **point cloud** — an unordered set of `(x, y, z)` points (often
with color and normals). Downstream tasks convert it to usable geometry.

| Representation | What it is | Use |
|----------------|-----------|-----|
| Point cloud | Set of 3D points | Raw LiDAR/MVS output |
| Mesh | Vertices + faces (triangles) | Rendering, simulation |
| Voxel grid | 3D occupancy lattice | Volumetric reasoning, collision |
| SDF / implicit | Signed distance to surface | Smooth reconstruction (Poisson) |
| Depth map | Per-pixel `Z` (2.5D) | RGB-D, single-view depth |

```
   Common point-cloud operations:
     - ICP (Iterative Closest Point): align two clouds -> registration
     - normal estimation: local plane fit (eigenvector of small covariance)
     - Poisson reconstruction: implicit surface from oriented points -> mesh
     - PointNet / sparse convs: DEEP learning directly on point sets
```

**Bridge — graphics:** meshes, voxels, and SDFs are the exact representations
`computer-graphics/07-GEOMETRY-AND-MESHES.md` *renders*; here vision *recovers* them. ICP
registration is a least-squares pose fit (closed-form via SVD for the rotation —
Procrustes).

---

## Layer 5: Visual SLAM — Mapping While Moving

SLAM does SfM *online*: a camera (often plus IMU) moves through an unknown environment and
must, in real time, estimate its own pose *and* build a map — the two depending on each
other (you need the map to localize, and your pose to map). It is the perception core of
robots, drones, AR headsets, and self-driving cars.

```
+------------------------------------------------------------------------------+
|                  VISUAL SLAM ARCHITECTURE (front end + back end)             |
|                                                                              |
|  FRONT END (per frame, fast)            BACK END (occasional, accurate)      |
|  --------------------------             ----------------------------         |
|  track features -> estimate pose        local bundle adjustment              |
|  (VISUAL ODOMETRY)                      keyframe map management              |
|       |                                       |                              |
|       v                                       v                              |
|  .-----------.    LOOP CLOSURE         .-----------------.                   |
|  | new frame | --detect revisit-->     | pose-graph      |                   |
|  | pose, map |   (place recognition)   | optimization    |                   |
|  '-----------'                         | corrects DRIFT  |                   |
|                                        '-----------------'                   |
|                                                                              |
|   DRIFT: small per-frame errors accumulate. LOOP CLOSURE recognizes a        |
|   previously seen place and corrects the whole trajectory globally.          |
+------------------------------------------------------------------------------+
```

The two failure modes SLAM must fight are **drift** (accumulated odometry error) and
**relocalization** after tracking is lost. **Loop closure** — recognizing a place you have
visited (via bag-of-visual-words, guide 04, or learned descriptors) — corrects drift by
adding a constraint that closes the loop, after which pose-graph optimization redistributes
the error globally.

| SLAM system | Approach |
|-------------|----------|
| **ORB-SLAM** | Feature-based (ORB) + keyframes + loop closure; the reference |
| **LSD-SLAM / DSO** | Direct (photometric) — optimizes intensity, not features |
| **VINS / OKVIS** | Visual-inertial — fuses camera with an IMU |
| **Learned SLAM** | DROID-SLAM, etc. — deep features/depth inside the geometric frame |

**Feature-based vs direct** is the core SLAM dichotomy: feature methods (ORB-SLAM) extract
and match keypoints, then minimize *reprojection* error; direct methods (DSO) skip features
and minimize *photometric* error over pixel intensities — better in low-texture, harder
under lighting change.

**Bridge — control theory:** visual-inertial SLAM fuses the camera with an IMU using the
same filtering/optimization machinery as state estimation in `control-theory/`; the Kalman
filter (guide 07) is the filtering-based alternative to the optimization-based back end.

---

## Layer 6: Neural 3D — NeRF and Gaussian Splatting

The newest branch represents the scene as a *learned function* rather than explicit
geometry. **NeRF** (Neural Radiance Fields, 2020) trains a small network to map a 3D point
and viewing direction to color and density, then renders novel views by volumetric ray
integration.

```
+------------------------------------------------------------------------------+
|                  NEURAL SCENE REPRESENTATIONS                                |
|                                                                              |
|  NeRF: MLP F(x, y, z, theta, phi) -> (color, density)                        |
|        render a pixel = integrate color*density along its ray                |
|        (the volume-rendering equation), differentiable -> train on images    |
|                                                                              |
|        ray ---o---o---o---o--->   sample points, query MLP, alpha-composite  |
|                                                                              |
|  3D GAUSSIAN SPLATTING (2023): represent the scene as millions of 3D         |
|        Gaussians; rasterize them -> real-time, high quality, explicit        |
|        (faster to render than NeRF's per-ray MLP queries).                   |
+------------------------------------------------------------------------------+
```

| Method | Representation | Strength | Weakness |
|--------|----------------|----------|----------|
| Classical SfM+MVS | Explicit points/mesh | Metric, interpretable, robust | Sparse detail, texture-less fails |
| NeRF | Implicit MLP | Photoreal novel views | Slow to train/render; per-scene |
| 3D Gaussian Splatting | Explicit Gaussians | Real-time, high quality | Memory-heavy; editing harder |

**Bridge — graphics:** NeRF's renderer is the *volume-rendering equation* — the same
ray-marched alpha compositing from `computer-graphics/03-RAY-TRACING.md`, made
differentiable so gradients flow back to the scene representation. Neural 3D is where
vision and graphics fully merge: differentiable rendering inverts the forward model
directly.

---

## Old World → New World Bridges

| You already know | 3D / SLAM analogue |
|------------------|---------------------|
| Sparse nonlinear least squares (numerics) | Bundle adjustment (Levenberg-Marquardt + Schur) |
| State estimation / filtering (control) | SLAM back end; visual-inertial fusion |
| Procrustes / SVD pose fit | ICP cloud registration |
| Meshes, voxels, SDFs (graphics) | The geometry SfM/MVS recover |
| Volume rendering (graphics) | NeRF's differentiable renderer |
| Place recognition / retrieval (guide 04) | Loop closure via bag-of-visual-words |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Reconstruct a scene from a photo set (offline) | Structure-from-Motion (COLMAP) |
| Localize a new image against known 3D | PnP (P3P + RANSAC) |
| Refine all poses + points optimally | Bundle adjustment |
| Get a dense surface, not sparse points | Multi-View Stereo + meshing |
| Align two point clouds | ICP |
| Map and localize in real time | Visual SLAM (ORB-SLAM) |
| Add robustness with an IMU | Visual-inertial SLAM (VINS) |
| Correct accumulated drift | Loop closure + pose-graph optimization |
| Photorealistic novel-view synthesis | NeRF or 3D Gaussian Splatting |

---

## Common Confusion Points

### "SfM vs SLAM — what's the actual difference?"

The problem is identical (jointly estimate poses + structure); the *constraints* differ.
SfM is offline and unordered — it can use all images at once, take its time, and globally
optimize. SLAM is online, sequential, and real-time — it processes frames as they arrive,
must run within a frame budget, and splits into a fast front end (per-frame tracking) and a
slower back end (occasional optimization, loop closure). Same geometry, different latency
contract.

### "Why is bundle adjustment 'the' optimizer everywhere in geometry?"

Because every geometric pipeline ultimately reduces to: find the poses and points that best
explain the observed pixels. That *is* minimizing reprojection error — bundle adjustment.
Two-view estimation, PnP, stereo, SfM, and SLAM back ends all end in a BA refinement. Its
tractability comes entirely from sparsity (each point seen by few cameras), which makes the
huge least-squares system solvable.

### "Feature-based vs direct SLAM — which is better?"

Trade-offs. Feature-based (ORB-SLAM) is robust to lighting and large motion, gives reusable
maps and easy loop closure, but discards most pixels and struggles in low-texture scenes.
Direct (DSO/LSD-SLAM) uses all photometric information, excels in low-texture and
fine-detail scenes, but is sensitive to lighting changes and rolling shutter. Production AR
often uses feature-based + IMU; both remain active.

### "Does NeRF replace classical 3D reconstruction?"

Not for everything. NeRF/Gaussian splatting excel at *photorealistic view synthesis* but
are typically per-scene, need known poses (usually from classical SfM first!), and don't
natively give clean metric meshes or robustness for robotics. Classical SfM+MVS still wins
for measurement, mapping, and pipelines needing explicit geometry. They are increasingly
combined: SfM provides the poses, neural methods provide the appearance.

### "Why does SLAM drift, and how does loop closure fix it?"

Each frame's pose estimate has small error; chained sequentially, these errors *accumulate*
without bound (like dead reckoning). Loop closure detects that the camera has returned to a
previously mapped place, adding a constraint that the two poses should coincide. Pose-graph
optimization then redistributes the accumulated error around the whole loop, snapping the
trajectory back to consistency. Without loop closure, a long traverse slowly bends away from
the truth.
