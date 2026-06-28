---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:filtering-and-features
kind: guide
module: computer-vision
section: computing-software
title: Filtering and Features
status: source-custody
source_custody: partial
current_path: computer-vision/02-FILTERING-AND-FEATURES.md
canonical_path: computer-vision/02-FILTERING-AND-FEATURES.md
backsource_ids: [proof-backfill:computer-vision:02-filtering-and-features, git-history:computer-vision:02-filtering-and-features]
concepts: [convolution, correlation, edge detection, corner detection, SIFT, ORB, scale space]
root_concepts: [image features]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Filtering and Features

## The Big Picture: From Pixels to Repeatable Points

Raw pixels are too low-level to match across images or feed a classifier. This guide is
the classical signal-processing layer of vision: it convolves the image with kernels to
expose structure (edges, corners), then summarizes that structure into **features** —
descriptors that are repeatable under viewpoint and lighting change. SIFT is the
canonical endpoint; a CNN (guide 05) is the learned successor.

```
+------------------------------------------------------------------------------+
|              FROM PIXELS TO MATCHABLE FEATURES  (the early-vision flow)      |
|                                                                              |
|   IMAGE          FILTERING            DETECTION           DESCRIPTION        |
|   I(x,y)   --->  convolve with  --->  find edges /  --->  encode local       |
|                  kernels h            corners / blobs     patch -> vector    |
|     |                |                    |                   |              |
|     v                v                    v                   v              |
|  .------.      .-----------.        .-----------.       .-----------.        |
|  |pixels|      | gradients |        | keypoints |       |descriptor |        |
|  |grid  |      | Gx, Gy    |        |(x,y,scale,|       |128-dim    |        |
|  |      |      | smoothed  |        | orient)   |       |SIFT vector|        |
|  '------'      '-----------'        '-----------'       '-----------'        |
|                                                                              |
|   Goal: points that survive rotation, scale, illumination -> MATCHING        |
+------------------------------------------------------------------------------+
```

---

## Layer 1: Convolution vs Correlation (Get This Exactly Right)

Both slide a kernel over the image and accumulate weighted sums. The *only* difference
is whether the kernel is flipped. This distinction matters because the literature uses
the terms loosely and CNNs actually compute correlation.

```
   CROSS-CORRELATION  (no flip):
       (I * h)[m,n] = SUM_{i,j} I[m+i, n+j] * h[i, j]

   CONVOLUTION  (kernel flipped in both axes):
       (I . h)[m,n] = SUM_{i,j} I[m-i, n-j] * h[i, j]
                    = correlation with h flipped 180 degrees

   If h is SYMMETRIC (e.g. a Gaussian), convolution == correlation.
```

```
+------------------------------------------------------------------------------+
|                    CONVOLUTION vs CORRELATION                                |
|                                                                              |
|  CONVOLUTION                          CORRELATION                            |
|  -----------                          -----------                            |
|  kernel flipped 180 deg               kernel used as-is                      |
|  commutative, associative             not commutative                        |
|  LTI-system output (signal theory)    template matching                      |
|  the "true" linear filter             "does this patch look like h?"         |
|                                                                              |
|  KEY FACT: a CNN "convolution" layer computes CORRELATION (no flip).         |
|  It learns the kernel, so the flip is irrelevant -- the learned weights      |
|  simply absorb it. The name is a historical misnomer.                        |
+------------------------------------------------------------------------------+
```

**Bridge — signal processing:** this is the 2D version of
`signal-processing/04-CONVOLUTION-CORRELATION.md`. Convolution in space ↔
multiplication in the 2D Fourier domain; large kernels (big Gaussians) are often
applied via FFT. Separable kernels (Gaussian, Sobel) factor a 2D convolution into two
1D passes, cutting cost from `O(k^2)` to `O(2k)` per pixel.

### Boundary handling

| Strategy | Behavior at edges |
|----------|-------------------|
| Zero-pad | Treat outside as 0; darkens borders |
| Replicate | Extend edge pixel outward |
| Reflect | Mirror the image at the boundary |
| Wrap | Toroidal (matches FFT convolution) |

---

## Layer 2: Smoothing and the Gaussian

Before differentiating, you smooth — differentiation amplifies noise, so you low-pass
first. The **Gaussian** is the canonical smoother: rotationally symmetric, separable,
and the unique kernel that introduces no spurious extrema as scale increases (the
scale-space axiom).

```
   G(x,y; sigma) = (1 / (2 pi sigma^2)) * exp( -(x^2 + y^2) / (2 sigma^2) )

   sigma controls the blur radius. Larger sigma -> coarser scale.
   Separable:  G_2D = G_1D(x) (convolved with) G_1D(y).

   3x3 box blur          5x5 Gaussian (sigma~1)
   1/9 * [1 1 1]         1/256 * [1  4  6  4 1]
         [1 1 1]                 [4 16 24 16 4]
         [1 1 1]                 [6 24 36 24 6]
                                 [4 16 24 16 4]
                                 [1  4  6  4 1]
```

---

## Layer 3: Edges — Where Intensity Changes Fast

An edge is a step in intensity: a large gradient magnitude. The gradient is computed
with derivative kernels; **Sobel** is the standard, combining smoothing and
differentiation.

```
   Sobel kernels (separable: [1 2 1]^T x [-1 0 1]):

        Gx = [-1  0  +1]        Gy = [+1 +2 +1]
             [-2  0  +2]             [ 0  0  0]
             [-1  0  +1]             [-1 -2 -1]

   Gradient magnitude:  |G| = sqrt(Gx^2 + Gy^2)
   Gradient direction:  theta = atan2(Gy, Gx)
```

### Canny edge detector (the gold standard)

Canny (1986) is the optimal-by-design edge detector — it derived its steps from three
criteria: good detection, good localization, single response per edge.

```
+------------------------------------------------------------------------------+
|                      CANNY EDGE DETECTOR  (5 stages)                         |
|                                                                              |
|  1. SMOOTH        Gaussian blur to suppress noise                            |
|  2. GRADIENT      Sobel -> magnitude |G| and direction theta                 |
|  3. NON-MAX       thin edges: keep a pixel only if it is a local max         |
|     SUPPRESSION   ALONG the gradient direction (1-pixel-wide ridges)         |
|  4. DOUBLE        two thresholds: strong (> T_high) and weak (T_low..T_high) |
|     THRESHOLD                                                                |
|  5. HYSTERESIS    keep weak edges only if connected to a strong edge         |
|                                                                              |
|  Result: clean, thin, connected edge contours.                               |
+------------------------------------------------------------------------------+
```

| Operator | What it computes | Notes |
|----------|------------------|-------|
| Sobel / Prewitt | First derivative (gradient) | Cheap; gives magnitude + direction |
| Laplacian | Second derivative (`div grad`) | Zero-crossings = edges; noise-sensitive |
| LoG / Marr-Hildreth | Laplacian of Gaussian | Smooth then Laplacian; blob/edge detector |
| Canny | Multi-stage gradient pipeline | Best general-purpose edge map |

---

## Layer 4: Corners — The Harris Detector

Edges are 1D-localized (you can slide along them). A **corner** is localized in 2D —
intensity changes in *every* direction — which makes it a good anchor for matching.
Harris formalizes this via the **second-moment (structure) matrix** `M`.

```
   For a window, gradients Ix, Iy give the structure matrix:

         .                      .
   M  =  | SUM Ix^2   SUM IxIy  |     (sums weighted by a Gaussian window)
         | SUM IxIy   SUM Iy^2  |
         '                      '

   Eigenvalues lambda1, lambda2 of M classify the local patch:

   lambda1 ~ lambda2 ~ 0     -> FLAT region (no structure)
   lambda1 >> lambda2 ~ 0    -> EDGE (one strong direction)
   lambda1 ~ lambda2 >> 0    -> CORNER (structure in both directions)
```

```
   Harris response (avoids costly eigen-decomposition):

     R = det(M) - k * trace(M)^2
       = lambda1*lambda2 - k*(lambda1 + lambda2)^2 ,   k ~ 0.04..0.06

   R > 0 and large  -> corner;  R < 0 -> edge;  |R| small -> flat.

   Shi-Tomasi variant: R = min(lambda1, lambda2) ("good features to track").
```

**Bridge — linear algebra:** `M` is a 2x2 covariance of the gradient field; its
eigenvectors are the principal directions of intensity change. The same eigen-analysis
of a structure tensor appears in optical flow (guide 07) and texture analysis.

---

## Layer 5: Scale and Blobs — Why SIFT Needs Scale Space

A corner detected at one zoom level may vanish at another. To match across scale you
must *detect the scale itself*. SIFT does this by searching for extrema in a
**scale space** — the image blurred by a continuum of Gaussians.

```
+------------------------------------------------------------------------------+
|              SCALE SPACE  (image x sigma)  and the DoG approximation         |
|                                                                              |
|  Build a pyramid of Gaussian blurs:   L(x,y,sigma) = G(sigma) * I            |
|                                                                              |
|  Difference of Gaussians approximates the scale-normalized Laplacian:        |
|     DoG = L(x,y, k*sigma) - L(x,y, sigma)   ~  (k-1) sigma^2 * Laplacian(L)  |
|                                                                              |
|   sigma  small  +----+   blob detector: a keypoint is a LOCAL EXTREMUM       |
|     ^           |    |   in the 3x3x3 neighborhood across (x, y, AND scale). |
|     |  larger   +----+   The scale at which it peaks IS the keypoint scale.  |
|     |  blur                                                                  |
|     +-------------------> x,y                                                |
+------------------------------------------------------------------------------+
```

---

## Layer 6: SIFT — The Canonical Descriptor

SIFT (Lowe, 1999/2004) produces keypoints that are invariant to scale and rotation and
robust to illumination and small viewpoint change. It is the reference against which all
features — including learned ones — are measured.

```
+------------------------------------------------------------------------------+
|                          SIFT PIPELINE  (4 steps)                            |
|                                                                              |
|  1. SCALE-SPACE EXTREMA   DoG pyramid; find extrema across x, y, scale       |
|  2. KEYPOINT LOCALIZE     sub-pixel fit; reject low-contrast + edge points   |
|                          (edge rejection uses the Harris-like Hessian ratio) |
|  3. ORIENTATION ASSIGN    histogram of gradient directions -> dominant       |
|                           orientation -> ROTATION invariance                 |
|  4. DESCRIPTOR            4x4 grid of 8-bin gradient histograms = 128-D      |
|                           vector, normalized for illumination invariance     |
+------------------------------------------------------------------------------+

   Invariances achieved:
     scale       <- detected at its characteristic scale
     rotation    <- descriptor rotated to the dominant orientation
     illumination<- gradient-based + normalized (cancels affine brightness)
```

The 128-D descriptor is matched between images by Euclidean distance, usually with
**Lowe's ratio test**: accept a match only if the nearest neighbor is much closer than
the second-nearest (ratio < 0.8), which rejects ambiguous matches.

---

## Layer 7: Fast Binary Features — ORB and Friends

SIFT is accurate but slow and (historically) patented. Real-time systems use binary
descriptors compared by Hamming distance (a popcount XOR — extremely fast).

| Detector / Descriptor | Type | Speed | Invariance | Use case |
|-----------------------|------|-------|------------|----------|
| **SIFT** | Float (128-D) | Slow | Scale + rotation | Accuracy benchmark, SfM |
| **SURF** | Float (64/128-D) | Medium | Scale + rotation | Faster SIFT-like |
| **FAST** | Detector only | Very fast | None (rotation added later) | Corner detection in real time |
| **BRIEF** | Binary | Very fast | None | Quick descriptor (no rotation) |
| **ORB** | Binary (256-bit) | Very fast | Rotation + (limited) scale | SLAM, mobile, AR |

**ORB** = oriented FAST + rotated BRIEF: it detects corners with FAST, assigns an
orientation via the intensity centroid, and computes a rotation-steered BRIEF binary
string. It is the default feature in ORB-SLAM (guide 08).

**Bridge — old → new:** SIFT/HOG-style hand-engineered features were *the* recognition
front-end until 2012. A CNN's early layers learn near-identical oriented-edge filters
(guide 05) — deep learning automated this exact pipeline. For *geometry* (SLAM, SfM),
hand-crafted features like ORB remain competitive because they are cheap and well
understood.

---

## Old World → New World Bridges

| You already know | Filtering/features analogue |
|------------------|------------------------------|
| LTI convolution, impulse response | 2D image filtering; receptive field = kernel support |
| FFT-based fast convolution | Large-kernel blurs done in the Fourier domain |
| Covariance / eigenvectors | Harris structure matrix `M`; principal gradient directions |
| Template matching | Cross-correlation; the source of the "CNN convolution" name |
| Multiresolution / wavelets | Scale space and the DoG pyramid |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Smooth / denoise before differentiating | Gaussian blur (separable) |
| Find edges, clean and thin | Canny |
| Get a raw gradient (magnitude + direction) | Sobel |
| Detect blob-like edges at a scale | Laplacian of Gaussian |
| Find stable corner points | Harris (or Shi-Tomasi for tracking) |
| Match points across scale + rotation | SIFT (accuracy) |
| Match points fast, on-device | ORB (binary, Hamming) |
| Reject ambiguous matches | Lowe's ratio test (< 0.8) |
| Apply a kernel cheaply | Exploit separability or FFT |

---

## Common Confusion Points

### "CNNs do convolution — but you said they do correlation?"

Yes. A deep-learning "convolution" layer computes cross-correlation (no kernel flip).
Because the kernel is *learned*, the 180-degree flip is absorbed into the learned
weights — the network is equally expressive either way, so the framework skips the
flip for speed. Mathematically pedantic, operationally irrelevant. Just know that
`Conv2d` ≠ textbook convolution.

### "Harris finds corners — but SIFT also rejects edges. Same thing?"

Related, opposite use. Harris's response *selects* corners. SIFT step 2 uses the same
structure (a Hessian eigenvalue ratio) to *reject* keypoints lying on edges, because
edge points localize poorly along the edge and match unreliably. Same math (ratio of
principal curvatures), used to keep good points vs throw out bad ones.

### "Why blur the image before finding edges? Isn't that destroying the edges?"

Differentiation amplifies high-frequency noise far more than signal. Blurring first
trades a little edge localization for a large gain in robustness. The optimal trade-off
is exactly what Canny's first stage and the LoG operator formalize: smooth at a scale
`sigma`, then differentiate. Choose `sigma` to match the scale of edges you care about.

### "SIFT vs a CNN — is SIFT obsolete?"

For *recognition*, learned features dominate. For *geometry* — structure-from-motion,
SLAM, image stitching — classical features (SIFT, ORB) are still widely used: they are
cheap, need no training, generalize across domains, and integrate cleanly with RANSAC
and bundle adjustment (guides 06, 08). The field is hybridizing: learned detectors
(SuperPoint) and learned matchers (SuperGlue) now beat SIFT on hard matching, but the
geometric estimator downstream is unchanged.
