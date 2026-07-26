---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:overview
kind: guide
module: computer-vision
section: computing-software
title: Computer Vision - Overview
status: source-custody
source_custody: partial
current_path: computer-vision/00-OVERVIEW.md
canonical_path: computer-vision/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:computer-vision:00-overview, git-history:computer-vision:00-overview]
concepts: [computer vision, inverse graphics, image formation, feature extraction, recognition, multi-view geometry]
root_concepts: [computer vision]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Computer Vision — Overview

## The Big Picture: Vision Is Inverse Graphics

Computer graphics answers a *forward* question: given a 3D scene and a camera, what
pixels result? Computer vision answers the *inverse* question: given the pixels, what
scene produced them? That inversion is ill-posed — infinitely many scenes project to
the same image — so every method in this directory is, at root, a way of injecting the
priors and constraints that pick out the *one* scene we actually care about.

```
+------------------------------------------------------------------------------+
|                  VISION = INVERTING THE IMAGE-FORMATION MODEL                |
|                                                                              |
|   GRAPHICS (forward)                          VISION (inverse)               |
|   -----------------                           ---------------                |
|   scene + lights + camera                     pixels (one or many images)    |
|            |                                          |                      |
|            v   project, shade, sample                 v   recover            |
|   +------------------+                        +------------------+           |
|   |  PIXEL ARRAY     |  <------------------>  |  SCENE / LABELS  |           |
|   |  I(x,y)          |     well-posed         |  geometry, ID,   |           |
|   +------------------+     vs ILL-POSED       |  motion, depth   |           |
|                                                                              |
|   The image is a many-to-one projection. Vision must add priors to invert.   |
+------------------------------------------------------------------------------+
```

Read this top-down: graphics maps scene → pixels deterministically; vision must climb
back up a collapsed dimension (the world is 3D, the image is 2D) using geometry,
statistics, and learned priors.

---

## The Pipeline: What This Directory Covers

The guides follow the natural flow from raw photons to scene understanding. Each layer
below is one or two guides.

```
+------------------------------------------------------------------------------+
|                        THE COMPUTER VISION STACK                             |
|                                                                              |
|  LAYER 0  IMAGE FORMATION         pinhole model, intrinsics K, extrinsics    |
|           (01)                    [R|t], sampling, color    -> the FORWARD   |
|              |                                                 model we      |
|              v                                                 invert        |
|  LAYER 1  EARLY VISION            convolution, edges (Canny), corners        |
|           (02)                    (Harris), descriptors (SIFT/ORB)           |
|              |                                                               |
|              v                                                               |
|  LAYER 2  MID-LEVEL VISION        segmentation: threshold, watershed,        |
|           (03)                    graph cuts, semantic/instance/panoptic     |
|              |                                                               |
|              v                                                               |
|  LAYER 3  CLASSICAL RECOGNITION   HOG, bag-of-visual-words, SVM/boosting,    |
|           (04)                    Viola-Jones  -> the pre-deep recognizer    |
|              |                                                               |
|              v                                                               |
|  LAYER 4  DEEP VISION             CNNs as learned filters, receptive         |
|           (05)                    fields, ResNet lineage, ViT, transfer      |
|              |                                                               |
|              v                                                               |
|  LAYER 5  MULTI-VIEW GEOMETRY     epipolar constraint, F and E matrices,     |
|           (06)                    stereo, triangulation, RANSAC              |
|              |                                                               |
|              v                                                               |
|  LAYER 6  DETECTION + TRACKING    R-CNN/YOLO, NMS, IoU/mAP, Kalman,          |
|           (07)                    optical flow                               |
|              |                                                               |
|              v                                                               |
|  LAYER 7  3D + SLAM               structure-from-motion, MVS, point          |
|           (08)                    clouds, visual SLAM, NeRF                  |
|              |                                                               |
|              v                                                               |
|  LAYER 8  APPLICATIONS            OCR, faces, medical, generative,           |
|           (09)                    deployment                                 |
+------------------------------------------------------------------------------+
```

---

## Three Eras (and Why They Coexist)

Vision did not progress by replacement; the eras *stack*. A modern SLAM system uses
deep features (era 3) inside a RANSAC + bundle-adjustment skeleton (era 2) on imagery
described by a pinhole model (era 1). Knowing which era a technique belongs to tells
you what assumptions it makes.

| Era | Period | Core idea | What it is good at | Where it breaks |
|-----|--------|-----------|--------------------|-----------------|
| **Classical / signal** | 1960s–1990s | Hand-designed filters and features; the image as a 2D signal | Edges, corners, blobs; interpretable; cheap | Semantics, occlusion, intra-class variation |
| **Geometric** | 1980s–2010s | Recover 3D structure from projection geometry | Pose, depth, reconstruction, calibration | Texture-less, dynamic, or non-rigid scenes |
| **Deep / learned** | 2012–now | Learn the features *and* the decision end-to-end | Classification, detection, segmentation, generation | Data hunger, distribution shift, geometric guarantees |

```
   classical signal        geometric            deep / learned
   ----------------        ---------            --------------
   |Sobel, Canny|          |F-matrix|           |  CNN / ViT |
   |Harris, SIFT| -------> |epipolar| -------->  |  end-to-end|
   |  filters   |  feed    |bundleAdj|  features |  learned   |
   +------------+          +--------+            +-----------+
        2D signal           3D geometry            statistics
   They COMPOSE: modern systems use all three at once.
```

---

## Old World → New World Bridges

You bring deep linear algebra, probability, and systems experience. Vision rewards all
three. The bridges below route through universal concepts first, then your prior art.

| You already know | Maps to in vision |
|------------------|-------------------|
| Convolution / LTI systems (signal processing) | A CNN layer is a bank of learned convolution kernels; the receptive field is the impulse-response support |
| Projective geometry / homogeneous coords (graphics) | The pinhole model, camera matrix, and homographies are the same machinery, *used to invert* |
| Least squares / SVD (linear algebra) | Triangulation, the 8-point algorithm for F, and PnP pose are constrained least-squares / null-space problems |
| Kalman filtering (control theory) | Object tracking propagates a Gaussian belief over object state frame to frame |
| Backprop / optimization (ML) | Same training machinery; vision adds spatial structure (weight sharing, pooling) as an architectural prior |
| Compression / sampling (signal) | Nyquist governs aliasing in images; mipmaps in graphics ↔ scale space (SIFT) in vision |

The single most useful reframing: **a convolutional network is a learned, hierarchical
version of the classical SIFT/HOG pipeline** — Layer 1 learns Gabor-like edge filters,
deeper layers learn parts and objects. Era 3 did not discard era 1; it *learned* it.

---

## Where Vision Touches the Rest of the Library

```
                          +-------------------+
                          |  COMPUTER VISION  |
                          +-------------------+
              /        /         |          \          \
             v        v          v           v          v
   signal-      computer-    mathematics/  ai-eng /     optics/
   processing/  graphics/    (lin alg,     ml-theory/   (lens
   (conv,       (forward     SVD, proj     (training,   physics,
   sampling,    render       geometry,     transformers,image
   Fourier)     model, proj  least sq)     generalization)formation)
                geometry)
```

- `signal-processing/` — convolution, correlation, sampling/Nyquist, Fourier, wavelets. Guide 02 leans on this directly; we state convolution-vs-correlation precisely here.
- `computer-graphics/` — the *forward* model vision inverts. Homogeneous coordinates, projection matrices, and homographies are shared; guide 01 and 06 bridge constantly.
- `mathematics/` — linear algebra is load-bearing: SVD for the 8-point algorithm and PnP, null spaces, least squares, projective geometry.
- `ai-engineering/` / `machine-learning-theory/` — the training machinery, transformers, and generalization theory. Guide 05 uses these; it does not re-derive backprop.
- `optics/` — the physics of lenses, aperture, depth of field, and real image formation behind the idealized pinhole.
- `control-theory/` — the Kalman filter and its EKF variant for tracking (guide 07) and SLAM (guide 08).

---

## A Worked Mental Model: One Image, Every Layer

Take a single photo of a parked car and trace what each layer would extract.

```
+------------------------------------------------------------------------------+
|  RAW IMAGE  ->  640x480 RGB pixel array I(x,y,c)                             |
|       |                                                                      |
|  (01) FORMATION   known: focal length f, principal point, pixel size         |
|       |           the car's 3D points X projected by  x ~ K[R|t]X            |
|       v                                                                      |
|  (02) FEATURES    Canny edges trace the body; Harris/SIFT mark wheel-arch    |
|       |           corners and badge keypoints with scale + orientation       |
|       v                                                                      |
|  (03) SEGMENT     a mask separates "car" pixels from road and sky            |
|       |                                                                      |
|  (04/05) RECOGNIZE  classical: HOG+SVM says "car"; deep: a CNN says          |
|       |             "car, sedan, 0.97" and localizes it                      |
|       v                                                                      |
|  (06) GEOMETRY    with a second photo, epipolar matching + triangulation     |
|       |           recovers the car's depth and the camera's motion           |
|       v                                                                      |
|  (07) TRACK       across a video, a Kalman filter follows the car's box      |
|       |                                                                      |
|  (08) 3D / SLAM   many frames -> a 3D point cloud and the camera trajectory  |
|       v                                                                      |
|  (09) APPLY       OCR the license plate; flag it; deploy on an edge device   |
+------------------------------------------------------------------------------+
```

Every guide in this directory is one of these arrows, made precise.

---

## Decision Cheat Sheet

| I want to... | Go to | Core tool |
|---|---|---|
| Understand how pixels relate to 3D points | 01 | Pinhole model, `x ~ K[R\|t]X` |
| Detect edges or corners; match keypoints | 02 | Canny, Harris, SIFT/ORB |
| Cut an image into regions or objects | 03 | Thresholding, graph cuts, semantic/instance seg |
| Classify images without deep nets | 04 | HOG, bag-of-visual-words + SVM |
| Build a modern recognizer | 05 | CNN (ResNet) or ViT + transfer learning |
| Recover depth or camera pose from 2+ views | 06 | Epipolar geometry, F/E matrices, triangulation |
| Find and follow objects in video | 07 | YOLO/R-CNN, NMS, IoU/mAP, Kalman, optical flow |
| Reconstruct a 3D scene from images | 08 | SfM, bundle adjustment, MVS, SLAM |
| Read text, recognize faces, or generate images | 09 | OCR, face embeddings, GAN/diffusion |
| Fit a model to noisy correspondences | 06 | RANSAC |

---

## Common Confusion Points

### "Isn't computer vision just a subfield of machine learning now?"

Deep learning dominates *recognition*, but vision is broader. Multi-view geometry
(guides 06, 08) is a geometric and optimization discipline with provable structure; a
CNN cannot, by itself, give you metric depth from two calibrated cameras the way
triangulation does. Modern systems are hybrids: learned features inside geometric
estimators. This is why the directory keeps geometry and learning as distinct spines.

### "Image processing vs computer vision — what's the line?"

```
  IMAGE PROCESSING            COMPUTER VISION
  image  -> image             image  -> description / scene
  denoise, sharpen, warp      "what is this, where, how far"
  signal in, signal out       signal in, MEANING out
```

Filtering (guide 02) sits on the boundary: it is image-processing machinery used as the
first step of vision. The distinction is the *output*: a transformed image vs a claim
about the world.

### "Vision and graphics use the same math — why two directories?"

They share projective geometry and the camera model, but the *direction* differs.
Graphics composes a known scene forward into pixels (well-posed). Vision inverts pixels
into an unknown scene (ill-posed, needs priors). The shared chapter — projection — is
the hinge; guides 01 and 06 are where this library's `computer-graphics/` and
`computer-vision/` meet.

### "Why call it 'inverse graphics' if most CV is classification?"

Classification is one slice. The inverse-graphics framing is the *unifying* lens: even
a classifier is implicitly answering "what object, under what pose and lighting, would
generate this image?" Generative vision (guide 09) makes the inversion literal —
diffusion models learn the image distribution and can be conditioned to recover scene
properties. The framing predicts where the field is heading.
