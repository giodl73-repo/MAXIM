---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-IMAGE-FORMATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:image-formation
kind: guide
module: computer-vision
section: computing-software
title: Image Formation - The Camera Model
status: source-custody
source_custody: partial
current_path: computer-vision/01-IMAGE-FORMATION.md
canonical_path: computer-vision/01-IMAGE-FORMATION.md
backsource_ids: [proof-backfill:computer-vision:01-image-formation, git-history:computer-vision:01-image-formation]
concepts: [pinhole camera, camera intrinsics, camera extrinsics, projection matrix, lens distortion, sampling, color]
root_concepts: [image formation]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Image Formation — The Camera Model

## The Big Picture: From 3D Point to Pixel

Every pixel is the end of a chain that starts at a 3D point in the world. The whole of
multi-view geometry (guide 06) is the inversion of this chain, so getting it exactly
right here is non-negotiable. The chain has four stages, each a matrix or a function.

```
+------------------------------------------------------------------------------+
|                   THE IMAGE-FORMATION CHAIN  (3D point -> pixel)             |
|                                                                              |
|  X_world          X_camera          x_normalized         x_pixel             |
|  [X Y Z 1]^T      [Xc Yc Zc]^T      [Xc/Zc, Yc/Zc]       [u v]^T             |
|     |                 |                  |                  |                |
|     |  EXTRINSICS     |  PERSPECTIVE     |  INTRINSICS      |  SAMPLING      |
|     |  [R | t]        |  DIVISION (/Zc)  |  K              |  + COLOR        |
|     v                 v                  v                  v                |
|  .--------.      .---------.       .-----------.      .-----------.          |
|  | world  | ---> | camera  | --->  |  image    | ---> |  sensor   |          |
|  | frame  |  rigid  frame  | proj  |  plane    |  pix  |  array    |         |
|  '--------'  move '---------' ect   '-----------' grid '-----------'         |
|                                                                              |
|   x ~ K [R | t] X      (the full 3x4 projection, up to scale '~')            |
+------------------------------------------------------------------------------+
```

Read left to right: a rigid transform `[R|t]` moves the point into the camera's frame;
perspective division collapses depth; the intrinsic matrix `K` converts to pixel units;
sampling and a color filter turn continuous irradiance into a discrete RGB array.

---

## Layer 1: The Pinhole Camera Model

The pinhole (camera obscura) is the idealization: a single point through which all rays
pass, projecting an inverted image on the plane behind it. We use the mathematically
equivalent **virtual image plane in front** of the center to avoid the sign flip.

```
            world point X = (Xc, Yc, Zc) in camera frame
                 *
                  \
                   \         image plane at z = f
            ........\........+------------+
                     \       |            |
                      \      |   x = ?    |
        optical -------C-----+------------+----> Z (optical axis)
        center         |     |
        (pinhole)      f     |
                       <----->
                    focal length

   Similar triangles:   x = f * Xc / Zc ,   y = f * Yc / Zc
```

The governing equation is **perspective projection** — the only nonlinearity in the
chain, the division by depth `Zc`:

```
   x = f * Xc / Zc          (this 1/Z is why parallel lines converge
   y = f * Yc / Zc           at vanishing points; depth is destroyed)
```

That single `1/Zc` is the source of the ill-posedness: any point along the ray `(t*Xc,
t*Yc, t*Zc)` projects to the same `(x, y)`. Recovering `Zc` is the central problem of
guides 06 and 08.

**Bridge — graphics:** this is the identical perspective transform from
`computer-graphics/01-TRANSFORMS-AND-PROJECTION.md`. Graphics applies it forward to
render; vision inverts it. The homogeneous-coordinate trick (below) is the same.

---

## Layer 2: Intrinsics — The Calibration Matrix K

`K` converts the projected point (in metric units on the image plane) into **pixel
coordinates**. It packages five parameters that describe the camera's internal optics
and sensor geometry.

```
        .                  .
        |  fx   s    cx     |     fx, fy : focal length in PIXELS (f / pixel size)
   K =  |   0   fy   cy     |     cx, cy : principal point (image center), in pixels
        |   0    0    1     |     s      : skew (~0 for modern sensors)
        '                  '

   Full intrinsic projection (point already in camera frame):

     .   .     .              . .     .
     | u |     | fx   s    cx | | Xc/Zc |
     | v |  ~  |  0   fy   cy | | Yc/Zc |     (homogeneous, defined up to scale)
     | 1 |     |  0    0    1 | |   1   |
     '   '     '              ' '     '
```

| Parameter | Meaning | Typical source of value |
|-----------|---------|-------------------------|
| `fx, fy` | Focal length in pixels along each axis | Calibration; differ if pixels non-square |
| `cx, cy` | Principal point (where optical axis hits sensor) | Near image center, not exactly |
| `s` (skew) | Shear between pixel axes | ~0 except on exotic/old sensors |

Why focal length is in *pixels*: `fx = f_metric / pixel_width`. A 24 mm lens on a sensor
with 6 µm pixels gives `fx = 0.024 / 0.000006 = 4000` pixels. **Calibration** is the
process of estimating `K` (and distortion) from images of a known target (a
checkerboard), typically via Zhang's method.

---

## Layer 3: Extrinsics — Where the Camera Is

The extrinsics `[R | t]` are the rigid-body transform from **world coordinates to camera
coordinates**. `R` is a 3x3 rotation (orthonormal, `det = +1`); `t` is the translation.

```
   X_camera = R * X_world + t        (R: world->camera rotation; t: translation)

   Equivalently, the camera CENTER in world coords is:   C = -R^T t

   +              +   These 6 DOF (3 rotation + 3 translation) are the camera POSE.
   | R   t |          Recovering pose from images = "localization" (guide 08 SLAM).
   | 0   1 |
   +              +   <- the 4x4 homogeneous form
```

```
+------------------------------------------------------------------------------+
|             INTRINSICS vs EXTRINSICS  (the two halves of calibration)        |
|                                                                              |
|  INTRINSICS  K                         EXTRINSICS  [R | t]                   |
|  -----------                           -------------                         |
|  inside the camera                     camera's pose in the world            |
|  fx fy cx cy s   (5 DOF)               R (3 DOF) + t (3 DOF) = 6 DOF         |
|  fixed per lens setup                  changes every time you move           |
|  found ONCE by calibration             estimated PER frame                   |
|                                                                              |
|  Together:   P = K [R | t]   is the 3x4 PROJECTION MATRIX (11 DOF)           |
+------------------------------------------------------------------------------+
```

The full forward model, in homogeneous coordinates:

```
   x ~ P X  =  K [R | t] X         x = [u v 1]^T,  X = [X Y Z 1]^T

   P is 3x4, defined up to a nonzero scale, so it has 11 degrees of freedom
   (12 entries minus 1 for scale). Camera resectioning / DLT recovers P from
   >= 6 known 3D<->2D correspondences.
```

---

## Layer 4: Homogeneous Coordinates — Why the '~'

The `~` ("equal up to scale") and the appended `1` are not bookkeeping; they linearize
the nonlinear perspective division. A point `[u v w]^T` represents the pixel `(u/w,
v/w)`. The depth division `1/Zc` becomes the act of dividing through by the last
homogeneous coordinate.

```
   Projection in homogeneous form is LINEAR:   x_h = P X_h   (matrix multiply)
   The nonlinearity hides in the final step:   (u, v) = (x_h[0]/x_h[2], x_h[1]/x_h[2])

   Benefit: translations, rotations, projection all become matrix products.
   This is exactly the trick computer-graphics/ uses for the MVP pipeline.
```

**Bridge — linear algebra:** homogeneous coordinates embed affine + projective maps as
linear maps on `P^n` (real projective space). The same construction underlies
`mathematics/` projective geometry and `computer-graphics/` transforms.

---

## Layer 5: Lens Distortion — Where the Pinhole Lies

Real lenses bend the ideal straight-line projection. The dominant effect is **radial
distortion** (barrel or pincushion), modeled as a polynomial in the radius from the
principal point, applied in *normalized* coordinates before `K`.

```
   Let r^2 = x_n^2 + y_n^2   (normalized, undistorted coords)

   Radial:     x_d = x_n (1 + k1 r^2 + k2 r^4 + k3 r^6)
               y_d = y_n (1 + k1 r^2 + k2 r^4 + k3 r^6)

   Tangential: adds p1, p2 terms for lens-sensor misalignment

   k1<0 -> barrel (wide angle);  k1>0 -> pincushion (telephoto)
```

```
   ideal grid          barrel (k1<0)        pincushion (k1>0)
   .--+--+--.          .-+----+-.            .--+--+--.
   |  |  |  |          | |    | |            \  |  |  /
   +--+--+--+          +-+----+-+             +-+--+-+
   |  |  |  |          | |    | |             | |  | |
   '--+--+--'          '-+----+-'            /  |  |  \
   straight            edges bow out         edges pinch in
```

You **undistort** before doing geometry: estimate `k1, k2, p1, p2` during calibration,
then warp pixels back to the pinhole-ideal positions. Multi-view geometry (guide 06)
assumes undistorted, pinhole-clean imagery.

---

## Layer 6: Sampling — Continuous Irradiance to Discrete Pixels

The sensor integrates light over each photosite and samples on a grid. This is the
2D analogue of the sampling theorem from `signal-processing/02-SAMPLING-THEORY.md`.

```
   continuous image  I(x,y)    --multiply by 2D comb (sensor grid)-->  I[m,n]

   Nyquist in 2D: spatial frequencies above the pixel-pitch limit ALIAS.
   Manifestation: moiré on fine textures (a striped shirt, a brick wall).
   Mitigation: an optical low-pass (anti-aliasing) filter + lens MTF rolloff.
```

| Concept | Signal-processing analogue | Vision manifestation |
|---------|----------------------------|----------------------|
| Sampling grid | Impulse train / Dirac comb | The pixel lattice |
| Aliasing | Spectral overlap above Nyquist | Moiré patterns, jaggies |
| Reconstruction | Sinc / interpolation | Bilinear/bicubic resampling |
| Point spread function | Impulse response (blur kernel) | Lens + sensor blur (MTF) |

**Bridge — graphics:** mipmaps in `computer-graphics/05-TEXTURING-AND-SAMPLING.md`
pre-filter to avoid aliasing on the *forward* path; SIFT's scale space (guide 02) builds
a similar pyramid on the *inverse* path.

---

## Layer 7: Color — From Spectrum to RGB

A monochrome sensor measures total irradiance. Color comes from a **color filter
array** (almost always a Bayer mosaic) plus *demosaicing*.

```
   BAYER PATTERN (2x2 tile)        each photosite sees ONE color;
   +----+----+                     the other two are interpolated
   |  R |  G |                     (demosaicing) from neighbors.
   +----+----+                     50% green (matches eye sensitivity),
   |  G |  B |                     25% red, 25% blue.
   +----+----+
```

```
+------------------------------------------------------------------------------+
|                       THE COLOR PIPELINE  (sensor -> usable RGB)             |
|                                                                              |
|  photons -> CFA mosaic -> demosaic -> white balance -> color space ->        |
|             (raw Bayer)   (interp)    (illuminant)     (sRGB) -> gamma       |
|                                                                              |
|  Gamma: stored values are NONLINEAR (sRGB ~ 1/2.2). For most CV math you     |
|  want LINEAR light -> linearize first, or your gradients/averages are wrong. |
+------------------------------------------------------------------------------+
```

Color spaces matter for vision algorithms:

| Space | Use in vision | Why |
|-------|---------------|-----|
| RGB (linear) | Geometry, gradients, deep nets | Physically additive; gradients meaningful |
| sRGB (gamma) | Storage, display | Perceptually uniform-ish; NOT for linear math |
| HSV / HSL | Color-based segmentation | Separates hue from brightness |
| Lab | Perceptual color distance | Euclidean distance ~ perceived difference |
| YCbCr | Compression, skin detection | Luma/chroma split; chroma subsampling |

**Bridge:** color science is treated in depth in
`computer-graphics/08-COLOR-AND-PERCEPTION.md` and `colors/`. Here the key vision
gotcha is gamma: average two sRGB pixels and you get the *wrong* color because you
averaged in a nonlinear space.

---

## Old World → New World Bridges

| You already know | Image formation analogue |
|------------------|--------------------------|
| MVP matrix pipeline (graphics) | `K[R\|t]` is the same composition, inverted in vision |
| Homogeneous coordinates | Identical; the `1` linearizes perspective |
| 2D Fourier / sampling (signal) | Pixel grid is a 2D sampler; aliasing = moiré |
| Change of basis | Extrinsics `[R\|t]` is world-frame → camera-frame change of basis |
| ADC quantization | Per-photosite integration + bit-depth quantization |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Relate a 3D point to a pixel | `x ~ K[R\|t]X` (full projection) |
| Get focal length in pixels | `fx = f_metric / pixel_width` |
| Find the camera's intrinsics | Calibrate with a checkerboard (Zhang's method) |
| Find where the camera is | Estimate extrinsics `[R\|t]` (pose) |
| Remove lens curvature | Undistort using `k1,k2,p1,p2` from calibration |
| Avoid moiré on fine texture | Optical low-pass + proper resampling (anti-alias) |
| Do correct color math | Linearize out of sRGB gamma first |
| Recover P from known points | DLT / camera resectioning, >= 6 correspondences |

---

## Common Confusion Points

### "Focal length is in millimeters — why do you say pixels?"

Both exist. The *lens* focal length is metric (24 mm). The *calibration* focal length
`fx, fy` is in pixels: `fx = f_metric / pixel_pitch`. Vision math operates in pixel
units because the output is pixels, so `K` carries the pixel-valued focal length. A
"35 mm equivalent" is yet a third convention (normalized to full-frame). State which
you mean.

### "Intrinsics vs extrinsics — which one changes when I move the camera?"

```
   Move the camera     -> EXTRINSICS [R|t] change. Intrinsics K unchanged.
   Zoom / change lens  -> INTRINSICS K change (focal length, principal point).
   Same lens, new shot -> only [R|t] differ between the two images.
```

This split is exactly why guide 06 can recover *motion* (the change in `[R|t]`) while
holding `K` fixed for a calibrated camera.

### "Why is the projection 'up to scale'? Doesn't every point have one pixel?"

A point projects to one pixel, but homogeneous coordinates `[u v w]` and `[2u 2v 2w]`
denote the *same* pixel `(u/w, v/w)`. The `~` says "equal after dividing out the scale."
The lost scale *is* the depth — which is precisely what a single image cannot recover.

### "Pinhole has no focal blur — so why does my photo have depth of field?"

The pinhole is an idealization with infinite depth of field and zero light. Real lenses
have an aperture, so only one plane is in perfect focus; everything else blurs (the
circle of confusion). Vision uses the pinhole *model* for geometry and treats defocus
separately — sometimes as a nuisance, sometimes as a depth cue (depth-from-defocus).
The optics live in `optics/`.
