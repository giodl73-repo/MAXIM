---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-MULTIVIEW-GEOMETRY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:multiview-geometry
kind: guide
module: computer-vision
section: computing-software
title: Multi-View Geometry
status: source-custody
source_custody: partial
current_path: computer-vision/06-MULTIVIEW-GEOMETRY.md
canonical_path: computer-vision/06-MULTIVIEW-GEOMETRY.md
backsource_ids: [proof-backfill:computer-vision:06-multiview-geometry, git-history:computer-vision:06-multiview-geometry]
concepts: [epipolar geometry, fundamental matrix, essential matrix, stereo, triangulation, RANSAC, homography]
root_concepts: [multi-view geometry]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Multi-View Geometry

## The Big Picture: Recovering Depth from Two Eyes

A single image destroys depth (guide 01: projection divides by `Z`). Two images of the
same scene from different viewpoints recover it — the difference in where a point appears
(its *disparity*) encodes its distance. Multi-view geometry is the precise machinery for
this: the **epipolar constraint** that links the two views, the **fundamental** and
**essential** matrices that encode it, **triangulation** that reconstructs 3D points, and
**RANSAC** that makes it all robust to wrong matches. This is the geometric heart of
vision — the part deep learning has *not* replaced.

```
+------------------------------------------------------------------------------+
|              TWO VIEWS RECOVER THE THIRD DIMENSION                           |
|                                                                              |
|                          X  (3D point, unknown depth)                        |
|                         /|\                                                  |
|                        / | \                                                 |
|                       /  |  \                                                |
|                      /   |   \                                               |
|        image 1 -----x1   |   x2----- image 2                                 |
|                   /      |      \                                            |
|                  C1------|-------C2     two camera centers                   |
|                  (left)  |   (right)                                         |
|                          v                                                   |
|                     baseline C1-C2 + the two rays -> triangulate X           |
|                                                                              |
|   Disparity (x1 - x2) is INVERSELY proportional to depth Z.                  |
+------------------------------------------------------------------------------+
```

---

## Layer 1: The Epipolar Constraint — Search Becomes 1D

Given a point `x1` in image 1, where is its match in image 2? Without geometry you would
search the whole image (2D). The epipolar constraint reduces this to a *single line* —
the **epipolar line** — because the true match must lie on the projection of the ray
through `x1`.

```
+------------------------------------------------------------------------------+
|                        EPIPOLAR GEOMETRY                                     |
|                                                                              |
|                            X (somewhere on this ray)                         |
|                           /:\                                                |
|                          / : \                                               |
|                         /  :  \                                              |
|              image1    /   :   \    image2                                   |
|             +--------+/    :    \+--------+                                  |
|             |   x1 . |     :     | . . . .|  <- epipolar LINE l2:            |
|             |        |     :     |  the image of x1's ray                    |
|             |  e1 .  |     :     |  . e2  |  <- epipoles e1,e2 = image of    |
|             +--------+     :     +--------+     the OTHER camera center      |
|                  C1 -------:------- C2                                       |
|                       baseline                                               |
|                                                                              |
|   The two image planes, the two centers, and X all lie in ONE epipolar       |
|   plane. Its intersection with each image is an epipolar line.               |
+------------------------------------------------------------------------------+
```

| Term | Definition |
|------|------------|
| **Epipolar plane** | Plane through `X`, `C1`, `C2` |
| **Epipolar line** | Intersection of the epipolar plane with an image |
| **Epipole** | Image of one camera's center in the other view; all epipolar lines pass through it |
| **Baseline** | The line `C1`–`C2` joining the two centers |

The payoff: stereo matching searches a 1D line, not a 2D plane — a quadratic-to-linear
reduction in the matching problem.

---

## Layer 2: The Fundamental Matrix F

The epipolar constraint is captured algebraically by the **fundamental matrix** `F`, a
3x3 rank-2 matrix relating corresponding *pixel* coordinates in two **uncalibrated**
views.

```
   For corresponding points x1, x2 (homogeneous pixel coords):

          x2^T F x1 = 0          <- THE epipolar constraint

   Meaning: F x1 = l2 is the epipolar LINE in image 2 on which x2 must lie.
            F^T x2 = l1 is the epipolar line in image 1.

   Properties of F:
     - 3x3, RANK 2 (det F = 0)        <- one of its singular values is 0
     - 7 degrees of freedom           (9 entries, -1 scale, -1 rank constraint)
     - epipoles are its null spaces:  F e1 = 0,   F^T e2 = 0
     - depends on intrinsics K1,K2 AND the relative pose (uncalibrated)
```

### The 8-point algorithm

`F` is estimated from point correspondences. Each match `x2^T F x1 = 0` gives one linear
equation in the 9 entries of `F`; eight matches determine it (up to scale).

```
+------------------------------------------------------------------------------+
|                  NORMALIZED 8-POINT ALGORITHM (estimate F)                   |
|                                                                              |
|  1. NORMALIZE   translate/scale points so they are centered, ~unit spread    |
|                 (Hartley normalization -- essential for numerical stability) |
|  2. BUILD A     each match -> one row of A from x2^T F x1 = 0; stack >= 8    |
|  3. SVD of A    F = the singular vector for the smallest singular value      |
|                 (least-squares null space)                                   |
|  4. ENFORCE     SVD F = U S V^T; zero the smallest singular value; recompose |
|     RANK 2      -> guarantees det F = 0 (valid epipolar geometry)            |
|  5. DENORMALIZE undo the step-1 transform                                    |
+------------------------------------------------------------------------------+
```

**Bridge — linear algebra:** every step is SVD. Solving `A f = 0` for the homogeneous
null space is "smallest-singular-vector of `A`"; enforcing rank 2 is "zero the smallest
singular value of `F`." Hartley's normalization is the difference between a usable `F`
and numerical garbage.

---

## Layer 3: The Essential Matrix E — When the Cameras Are Calibrated

If you know the intrinsics `K1, K2`, work in *normalized* camera coordinates (`x_hat =
K^-1 x`) and the constraint uses the **essential matrix** `E`, which encodes *only the
relative pose* — pure geometry, no intrinsics.

```
   Normalized coords:  x_hat = K^-1 x      Then:   x2_hat^T E x1_hat = 0

   Relationship:        E = K2^T F K1       (F is E "wrapped" in the intrinsics)

   E factorizes into the relative ROTATION and TRANSLATION:

        E = [t]_x R          [t]_x = skew-symmetric matrix of translation t
                             R = relative rotation between the two cameras

   Properties of E:
     - 3x3, rank 2; its two NONZERO singular values are EQUAL
     - 5 degrees of freedom (3 rotation + 3 translation - 1 scale)
     - decomposes into 4 (R, t) candidates; pick the one with points in
       front of BOTH cameras (cheirality test)
```

```
+------------------------------------------------------------------------------+
|              FUNDAMENTAL vs ESSENTIAL  (uncalibrated vs calibrated)          |
|                                                                              |
|  FUNDAMENTAL F                         ESSENTIAL E                           |
|  -------------                         -----------                           |
|  pixel coordinates                     normalized (calibrated) coords        |
|  x2^T F x1 = 0                          x2_hat^T E x1_hat = 0                |
|  encodes intrinsics + pose             encodes ONLY relative pose            |
|  7 DOF, rank 2                          5 DOF, rank 2, equal singular values |
|  no metric meaning                      decomposes to R, t (up to scale)     |
|                                                                              |
|  E = K2^T F K1    (calibration is the bridge between them)                   |
+------------------------------------------------------------------------------+
```

The decomposition of `E` into `(R, t)` is *the* motion-recovery step: from two calibrated
images you get the relative camera rotation and translation direction (translation scale
is unobservable from images alone — the monocular scale ambiguity).

---

## Layer 4: Triangulation — Recovering the 3D Point

With both camera matrices `P1 = K1[I|0]` and `P2 = K2[R|t]` known, and a matched pair
`(x1, x2)`, intersect the two rays to find `X`. Because of noise the rays usually do not
exactly meet, so it is a least-squares problem.

```
   Each view gives x ~ P X, i.e. x cross (P X) = 0. Stack the cross-product
   rows from both views into A X = 0, solve for X by SVD (smallest singular
   vector). This is the LINEAR (DLT) triangulation.

         ray from C1 ----.        the rays are SKEW under noise;
                          X*       X* minimizes reprojection error
         ray from C2 ----'         (the "optimal" / Gold Standard method
                                    minimizes geometric error in both images).

   Depth from disparity (rectified stereo, focal f, baseline b):

         Z = f * b / disparity        disparity = x1 - x2  (in pixels)
```

The `Z = f*b/d` relation is the quantitative core of stereo: depth is inversely
proportional to disparity, scaled by focal length times baseline. A wider baseline `b`
gives more depth precision but harder matching (more occlusion, more appearance change).

---

## Layer 5: Stereo and Rectification

A calibrated stereo *rig* (two fixed cameras) makes matching easy by **rectification**:
warp both images so epipolar lines are horizontal and aligned. Then the match for any
pixel lies on the *same row* in the other image — search is a 1D horizontal scan.

```
+------------------------------------------------------------------------------+
|                    STEREO PIPELINE  (rectified rig -> depth map)             |
|                                                                              |
|  1. CALIBRATE     intrinsics + extrinsics of both cameras                    |
|  2. RECTIFY       warp so epipolar lines are horizontal & row-aligned        |
|  3. MATCH         for each pixel, scan the same row in the other image;      |
|                   cost = SAD/SSD/census/NCC over a window                    |
|  4. DISPARITY     disparity map d(x,y) = horizontal shift of best match      |
|  5. DEPTH         Z = f*b/d  -> depth map / 3D point cloud                   |
|                                                                              |
|   Global methods (semi-global matching SGM, graph cuts) enforce smoothness   |
|   across the whole map; local window methods are fast but noisy.             |
+------------------------------------------------------------------------------+
```

| Matching cost | Property |
|---------------|----------|
| SAD / SSD | Sum of (absolute / squared) differences; fast, brightness-sensitive |
| NCC | Normalized cross-correlation; invariant to brightness/contrast |
| Census / Hamming | Bit-string of local ordering; robust to illumination |

**Bridge — signal processing:** disparity matching is windowed cross-correlation (guide
02); NCC is the normalized version that cancels gain/bias. **Bridge — segmentation:** SGM
and graph-cut stereo use the same smoothness-energy MRF as graph-cut segmentation (guide
03).

---

## Layer 6: Homography — When the Scene Is Planar

If all points lie on a *plane* (or the camera only *rotates* about its center), the two
views are related by a single 3x3 **homography** `H`, not the epipolar machinery. `H` maps
points directly: `x2 ~ H x1`.

```
   x2 ~ H x1          H is 3x3, 8 DOF (up to scale), full rank (invertible).

   Estimated from >= 4 point correspondences (DLT, same SVD machinery).

   Uses:
     - image stitching / panoramas (camera rotates about its center)
     - rectifying a planar surface (document, whiteboard, road plane)
     - augmented-reality marker tracking (planar fiducial)
```

| Relation | When it applies | DOF | Min points |
|----------|-----------------|-----|------------|
| **Homography H** | Planar scene OR pure rotation | 8 | 4 |
| **Fundamental F** | General scene, uncalibrated | 7 | 7–8 |
| **Essential E** | General scene, calibrated | 5 | 5 |

Choosing the wrong model is a classic error: fitting `F` to a planar scene is
*degenerate* (the configuration is rank-deficient), and you must fall back to `H`.

---

## Layer 7: RANSAC — Robustness to Wrong Matches

Feature matching (guide 02) produces *outliers* — wrong correspondences. A least-squares
fit of `F` or `H` is destroyed by even a few. **RANSAC** (RANdom SAmple Consensus) fits a
model from random minimal samples and keeps the one with the most inliers.

```
+------------------------------------------------------------------------------+
|                         RANSAC  (robust model fitting)                       |
|                                                                              |
|  REPEAT N times:                                                             |
|    1. SAMPLE   pick the MINIMAL set at random (8 for F, 4 for H)             |
|    2. FIT      estimate the model from just those points                     |
|    3. SCORE    count INLIERS: matches with error < threshold t               |
|  KEEP the model with the most inliers; REFIT using all its inliers.          |
|                                                                              |
|   data with outliers:    o o o   X (outlier)                                 |
|                         o o o o        X                                     |
|       best line  -------o-o-o-o-o-------   ignores the X's                   |
|                                                                              |
|   #iterations N for success prob p, inlier ratio w, sample size s:           |
|       N = log(1 - p) / log(1 - w^s)                                          |
+------------------------------------------------------------------------------+
```

RANSAC is the glue of geometric vision: it sits between matching and estimation in SfM,
SLAM, stereo, and stitching. The iteration-count formula is worth internalizing — with a
sample size of 8 (for `F`), a low inlier ratio explodes `N`, which is why minimal models
and good initial matches matter.

**Bridge — old → new:** RANSAC is a hypothesize-and-verify search; it is robust
statistics applied to geometry. Learned matchers (SuperGlue) reduce the outlier rate but
do *not* remove RANSAC — they make it converge faster.

---

## Old World → New World Bridges

| You already know | Multi-view geometry analogue |
|------------------|------------------------------|
| SVD / null space / least squares | Estimating F, E, H, and triangulation are all SVD |
| Skew-symmetric matrix of a cross product | `[t]_x` in the essential matrix `E = [t]_x R` |
| Projective geometry (graphics) | Epipolar geometry is its two-view specialization |
| Robust statistics / median | RANSAC = consensus-based robust fitting |
| Cross-correlation (signal) | Stereo block matching; NCC is the normalized form |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Constrain a match to a 1D search | Epipolar line from `F` (or `E`) |
| Relate two uncalibrated views | Fundamental matrix `F` (8-point) |
| Relate two calibrated views | Essential matrix `E` (5-point) |
| Recover relative camera motion | Decompose `E` → `(R, t)` + cheirality test |
| Reconstruct a 3D point from two views | Triangulation (DLT / optimal) |
| Get a dense depth map from a stereo rig | Rectify + block match + `Z = f*b/d` |
| Stitch a panorama or rectify a plane | Homography `H` (4 points) |
| Fit a model despite wrong matches | RANSAC (minimal sample + consensus) |
| Stabilize an estimate numerically | Hartley normalization before the SVD |

---

## Common Confusion Points

### "Fundamental vs essential — when do I use which?"

`E` if you know the intrinsics `K` (calibrated camera), `F` if you do not. They are linked
by `E = K2^T F K1`. `E` is more constrained (5 DOF, equal singular values) and decomposes
directly into `(R, t)` for motion recovery; `F` (7 DOF) works on raw pixels but carries no
metric meaning until you supply `K`. In practice: phone camera with EXIF focal length →
use `E`; unknown camera → estimate `F`.

### "Why does F have rank 2 — and why force it?"

All epipolar lines pass through the epipole, which means `F` has a null space (`F e1 = 0`),
so it cannot be full rank — `det F = 0`. The 8-point algorithm's raw least-squares
solution is full-rank from noise; step 4 zeros the smallest singular value to *enforce*
rank 2. Skip it and your epipolar lines won't intersect at a single epipole — the geometry
is invalid.

### "Disparity and depth — which way does the relationship go?"

Inversely: `Z = f*b/d`. Near objects have *large* disparity (shift a lot between views);
far objects have *small* disparity (sky barely moves). This is why stereo precision
degrades with distance — at large `Z`, a one-pixel disparity error spans a huge depth
range. Widen the baseline `b` for far-range precision, at the cost of harder matching.

### "When does homography apply instead of the fundamental matrix?"

When the scene is *planar* or the camera only *rotates about its center* (no translation).
Then there is no parallax, no epipolar geometry to recover, and a single `H` maps one view
to the other. Fitting `F` here is degenerate. Robust pipelines fit *both* `H` and `F` via
RANSAC and pick the model that explains the data (the GRIC / model-selection step in
ORB-SLAM) — this is how a system decides "pure rotation" vs "general motion."

### "RANSAC is random — is the result reproducible?"

It is stochastic, but with enough iterations the inlier set converges to the same answer
with high probability — that is what `N = log(1-p)/log(1-w^s)` guarantees. Fix the random
seed for exact reproducibility. The final refit on all inliers (a deterministic
least-squares step) is what makes the output stable; RANSAC's job is only to find the
inlier set.
