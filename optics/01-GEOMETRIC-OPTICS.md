# Geometric Optics

## The Big Picture

Geometric optics treats light as rays — directed lines that carry power, obey Snell's law at interfaces, and travel in straight lines through homogeneous media. Valid when all feature sizes >> wavelength. The entire field rests on one principle:

```
+---------------------------------------------------------------+
|  FERMAT'S PRINCIPLE (foundation of all geometric optics)      |
|                                                               |
|  Light follows the path of stationary optical path length.    |
|  In practice: the path light takes between two points is      |
|  the one for which the optical path length (OPL) is an        |
|  extremum (usually a minimum -- "least time").                |
|                                                               |
|  OPL = integral of n(s) ds  along the path                   |
|       = n * L  (uniform medium, n = refractive index)         |
|                                                               |
|  From Fermat's principle, you derive:                         |
|    1. Law of reflection (theta_i = theta_r)                   |
|    2. Snell's law of refraction                               |
|    3. All lens equations                                      |
|    4. ABCD matrix formalism                                   |
+---------------------------------------------------------------+
```

---

<!-- @editor[audience/P2]: Snell's law derivation and TIR basics are covered in MIT undergrad physics — this learner explicitly does not need them. The Fermat's principle framing above is useful (conceptual foundation). The detailed Snell's law section through TIR could be condensed to a reference table (what matters: fiber optic TIR application, critical angle formula) and the depth shifted toward the ABCD matrix formalism and aberration content where the real value is. -->

## Snell's Law and Total Internal Reflection

### Snell's Law

At any interface between media with refractive indices n1 and n2:

```
              Normal to surface
                    |
   Medium 1 (n1)   |   theta_1 = angle of incidence
   .................|...................
                    |   theta_2 = angle of refraction
   Medium 2 (n2)   |

   n1 * sin(theta_1) = n2 * sin(theta_2)
```

**Physical meaning**: phase velocity changes at the interface (v = c/n), so the wavefront tilts. The phase matching condition along the surface gives Snell's law.

Selected refractive indices:
| Medium | n (at 589 nm) |
|--------|--------------|
| Vacuum | 1.0000 |
| Air | 1.0003 |
| Water | 1.333 |
| Crown glass (BK7) | 1.517 |
| Flint glass | 1.620 |
| Silicon | 3.48 (at 1550 nm) |
| Diamond | 2.42 |

### Total Internal Reflection (TIR)

When light goes from a dense medium (n1 > n2) to a less dense one, there exists a critical angle beyond which no transmitted ray exists:

```
  n1 * sin(theta_c) = n2 * sin(90 deg) = n2

  theta_c = arcsin(n2 / n1)

  For glass (n1=1.5) to air (n2=1.0):
  theta_c = arcsin(1/1.5) = 41.8 deg

  At theta > theta_c:
  +------------------+
  | Glass (n1=1.5)   |  All power reflects back.
  |    \   reflected  |  No transmitted ray.
  |     \ /           |  Used in: fiber optics,
  |------X------------|  prism reflectors, TIR
  |   (no refracted)  |  microscopy.
  | Air (n2=1.0)      |
  +------------------+
```

TIR is the physical mechanism behind optical fiber waveguiding, corner-cube retroreflectors, and the brilliance of diamond (theta_c = 24.4 deg — far steeper than glass, so most rays TIR internally).

---

## Paraxial (Gaussian) Optics

"Paraxial" = small-angle approximation: sin(theta) ~ theta ~ tan(theta). This linearizes all optics and enables the elegant thin-lens and ABCD machinery.

### Thin Lens Equation

```
    Object                Lens            Image
      |                    |               |
      |<------- do ------->|<----- di ---->|
      |                    |               |
      O (object)          f (focal pt)    I (image)

  Gaussian lens equation:
  1/f = 1/do + 1/di

  Lateral magnification:
  m = hi/ho = -di/do

  Sign convention (real-is-positive):
  - Distances measured from the lens
  - do > 0 for real object (left of lens)
  - di > 0 for real image (right of lens)
  - f > 0 for converging (convex) lens
  - f < 0 for diverging (concave) lens
  - m < 0 means inverted image
```

### Lensmaker's Equation

Connects focal length to surface curvatures:

```
  1/f = (n_lens - 1) * [1/R1 - 1/R2]

  R1 = radius of curvature of first surface
       (positive if center of curvature is to the right)
  R2 = radius of curvature of second surface
  n_lens = refractive index of lens material

  Biconvex lens: R1 > 0, R2 < 0  --> f > 0  (converging)
  Biconcave lens: R1 < 0, R2 > 0  --> f < 0  (diverging)
  Plano-convex: R1 = inf          --> 1/f = (n-1)/R2 * (-1)
```

---

## ABCD Ray Transfer Matrix Formalism

This is the matrix mechanics of geometric optics. Every optical element is a 2x2 matrix; compose a system by multiplying matrices. Identical in structure to state transfer matrices in control theory.

### The Ray Vector

A ray is represented as a column vector:

```
  [y ]
  [u ]

  y = height from optical axis
  u = paraxial angle (ray slope, in radians, small angle)
      or sometimes nu = n*u (reduced angle, more common in thick lens work)
```

### ABCD Matrices for Common Elements

```
+------------------------------------------------------------------+
|  ELEMENT              MATRIX          NOTES                      |
|  -----------------    ------          -----                      |
|                                                                  |
|  Free space           [1  d]          d = propagation distance   |
|  propagation          [0  1]          y' = y + d*u               |
|                                                                  |
|  Thin lens            [ 1    0]       f > 0: converging           |
|  (focal length f)     [-1/f  1]       u' = u - y/f               |
|                                                                  |
|  Flat interface       [1  0]          n1, n2 = refractive indices |
|  (refraction)         [0  n1/n2]      (using reduced angle nu)   |
|                                                                  |
|  Curved interface     [ 1      0   ]  R > 0: center to right     |
|  (refraction, R)      [-(n2-n1)/R n1/n2]                        |
|                                                                  |
|  Flat mirror          [1  0]          same as free space but      |
|  (reflection)         [0  1]          reverses direction          |
|                                                                  |
|  Curved mirror        [ 1    0]       f = R/2 (R = mirror radius)|
|  (focal length f)     [-1/f  1]       same form as thin lens      |
+------------------------------------------------------------------+
```

### System Matrix Composition

```
  For a system with elements M1, M2, M3 (light travels left to right):

  M_system = M3 * M2 * M1

  CAUTION: Matrix order is REVERSED relative to light travel order.
           Rightmost matrix = first element encountered by light.

  Example: telescope (objective + eyepiece separated by f1 + f2):

  M = [1   0 ] * [1  f1+f2] * [1   0 ]
      [-1/f2 1]   [0    1  ]   [-1/f1 1]

  This gives the system matrix from which you extract:
    - Back focal distance (where image forms)
    - Front focal distance
    - Angular magnification
    - Pupil locations
```

### Key System Properties from ABCD

```
  M = [A  B]
      [C  D]

  Back focal length (from last surface to rear focal point):  BFL = -A/C
  Front focal length (from first surface to front focal pt):  FFL = -D/C
  Rear principal plane location: H' = (1-A)/C from last surface
  Front principal plane location: H = (D-1)/C from first surface
  Focal length: f = -1/C

  For a complete system: det(M) = 1 (energy conservation in lossless system)
```

---

## Thick Lenses and Principal Planes

Real lenses have thickness. Principal planes (H and H') are the reference planes from which focal lengths are measured:

```
         H   H'
         |    |
  ------>|....|------>
         |    |
         f    f
      <--+    +-->

  - Rays entering parallel to axis from left appear to pivot at H'
  - Rays entering parallel to axis from right appear to pivot at H
  - Focal length f measured from H to rear focal point
  - Object distance measured from H, image distance from H'
  - For a thin lens: H and H' coincide at the lens plane
```

---

## Mirror Equations

Mirrors obey the same thin lens equation with the sign convention adjusted:

```
  Concave mirror (converging, center of curvature in front):
    f = R/2 (positive)
    1/f = 1/do + 1/di  (same form as thin lens)
    m = -di/do

  Convex mirror (diverging, center of curvature behind mirror):
    f = -R/2 (negative)
    Always produces virtual, upright, diminished images

  Flat mirror: f = infinity -> di = -do (virtual image, same distance behind)
```

---

## Seidel (Third-Order) Aberrations

The paraxial approximation uses sin(theta) ~ theta. Third-order (Seidel) theory uses sin(theta) ~ theta - theta^3/6. This gives five primary aberrations, each with a characteristic visual signature:

```
+------------------------------------------------------------------+
|  SEIDEL ABERRATION    VISUAL SIGNATURE      CAUSE                |
|  -----------------    ----------------      -----                |
|                                                                  |
|  1. Spherical         Halo around point     Marginal rays focus   |
|     aberration        source (on axis)      closer than paraxial  |
|                                             (spherical surfaces)  |
|                                                                  |
|  2. Coma              Comet-tail shape      Off-axis point        |
|                       (off-axis)            sources, magnification|
|                                             varies with aperture  |
|                                                                  |
|  3. Astigmatism       Lines instead of      Off-axis rays in two  |
|                       points (off-axis)     planes focus at       |
|                                             different distances   |
|                                                                  |
|  4. Field curvature   Sharp at center OR    Focal surface is      |
|     (Petzval)         edge, not both        curved, not flat      |
|                                                                  |
|  5. Distortion        Straight lines bow    Magnification varies  |
|                       (barrel or pincushion)with field height     |
|                       -- NOT a blur!                             |
+------------------------------------------------------------------+

  Barrel distortion:          Pincushion distortion:
  +-------+                   +-------+
  |  /-\  |                   | /---\ |
  | | | | |                   |/     \|
  |  \-/  |                   |\     /|
  +-------+                   | \---/ |
  Wide-angle lenses            +-------+
                               Telephoto lenses
```

### Chromatic Aberration

Refractive index varies with wavelength (dispersion). Two types:

```
  Longitudinal CA: Blue focuses closer than red (for converging lens)
                   Appears as colored halo; varies as ~1/f
  Transverse CA:   Magnification varies with wavelength
                   Appears as color fringing at edges; off-axis only

  Abbe number (V-number): V = (n_D - 1) / (n_F - n_C)
    n_D at 589 nm (sodium yellow)
    n_F at 486 nm (hydrogen blue)
    n_C at 656 nm (hydrogen red)

    High V (> 55): low dispersion glass (crowns, BK7: V=64)
    Low V (< 35):  high dispersion glass (flints, F2: V=36)

  Achromatic doublet: cemented crown+flint pair; brings two colors
  to same focus. Standard solution since ~1750.
  Apochromat: three colors. Used in high-end microscope objectives.
```

---

## Optical Instruments

### Telescope

```
  Keplerian (refracting):

  Objective (f_obj)                 Eyepiece (f_eye)
  +----+                            +----+
  |    |                            |    |
  |    |----( intermediate image )--|    |---> parallel rays to eye
  |    |                            |    |
  +----+                            +----+
  <----------- f_obj + f_eye ----------->

  Angular magnification: M = -f_obj / f_eye
  (negative = inverted image)

  Galilean: uses diverging eyepiece (f_eye < 0)
    M = -f_obj / f_eye  (positive = upright)
    Shorter length, smaller exit pupil
    Opera glasses, binoculars use this with image-erecting prisms

  Newtonian reflecting:
    Parabolic primary mirror avoids spherical aberration
    Flat secondary at 45 deg deflects beam to eyepiece on side
    f/# of 5-8 typical for amateur, f/2-3 for fast survey telescopes
```

### Microscope

```
  Object                Objective          Tube lens        Eyepiece
  (near focus)          (NA, f_obj)        (f_tube)         (f_eye)
     |                       |                 |                |
     *----[high-NA capture]---+--[intermediate--+--image to eye--+
                                   image]

  Total magnification M = M_obj * M_eye
    M_obj = -L / f_obj  (L = tube length, 160mm traditional, 200mm modern)
    M_eye = 250mm / f_eye  (250mm = "near point")

  Resolution (Abbe limit for coherent illumination):
    d_min = lambda / (2 * NA)
    d_min = lambda / (n * NA)  (for incoherent: Rayleigh criterion)

  Numerical aperture:
    NA = n * sin(theta_max)
    n = refractive index of medium between objective and sample
    Oil immersion (n=1.515) gives NA up to ~1.45
    Water immersion (n=1.33) gives NA up to ~1.2

  NA matters more than magnification:
    Resolution depends only on NA and lambda
    Magnification above the "useful" range adds no new detail ("empty magnification")
    Useful magnification ~ 500-1000 * NA
```

### Camera

```
  f-number (f/#):
    f/# = f / D   (focal length / aperture diameter)
    "Stops": f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, f/16
    Each stop halves the area (doubles the f/#), halves the light

  Depth of field (DOF):
    DOF approximately = 2 * f/# * c / m^2  (for distant objects)
    c = circle of confusion diameter (pixel pitch or acceptable blur)
    m = magnification

    Large f/# -> deep DOF (landscape photography, f/11-f/16)
    Small f/# -> shallow DOF (portrait "bokeh", f/1.4-f/2.8)

  Diffraction limit vs. sensor resolution:
    Airy disk diameter ~ 2.44 * lambda * f/#
    At f/16, lambda=550nm: Airy disk ~ 21 um
    If pixel pitch < Airy disk diameter: diffraction-limited
    If pixel pitch > Airy disk diameter: pixel-limited
    Practical balance: f/8-f/11 for most sensors
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Trace rays through a multi-element system | ABCD matrix multiplication |
| Find image location and size | Thin lens equation + magnification |
| Understand telescope magnification | M = -f_obj / f_eye |
| Maximize microscope resolution | Maximize NA (use oil immersion) |
| Control depth of field | Adjust f/# (larger = deeper DOF) |
| Correct chromatic aberration | Achromatic doublet (crown + flint glass) |
| Find critical angle for fiber guidance | theta_c = arcsin(n2/n1) |
| Analyze thick lens system | Find principal planes H, H'; use them as thin lens |
| Understand barrel/pincushion distortion | Distortion = Seidel aberration #5 |
| Model a mirror as a lens | Use same 1/f = 1/do + 1/di; f = R/2 |

---

## Common Confusion Points

**Sign conventions are inconsistent across textbooks**: The real-is-positive convention (do, di positive for real objects/images) is used here. Some texts use the Cartesian sign convention (distances measured from surface, leftward negative). Always check which convention a formula uses before plugging in numbers.

**Magnification sign vs. orientation**: Negative magnification means inverted image, which is real and useful (cameras, most microscopes). Positive magnification means upright image (magnifying glasses, viewfinder telescopes). The sign is not about quality.

**f-number is NOT the aperture diameter**: f/# = f/D. A 100mm f/2 lens has D = 50mm aperture. A 100mm f/4 lens has D = 25mm aperture. "Fast" lens = low f/# = large aperture = more light = shallower DOF.

**Spherical surfaces cause spherical aberration**: All simple lenses use spherical surfaces (cheap to grind). Spherical aberration is unavoidable with a single spherical surface. Aspheric surfaces or lens combinations cancel it. Parabolic mirrors are perfect for on-axis point sources (telescopes) but suffer coma off-axis.

**Distortion does not blur the image**: Barrel and pincushion distortion are geometric displacements, not focus errors. A scene with distortion can be perfectly sharp but geometrically warped. Correctable in software (lens distortion profiles in Lightroom, for example).

**ABCD matrix order is reversed**: Light going M1 then M2 then M3 requires M_total = M3 * M2 * M1. The rightmost matrix operates first. This is identical to function composition: f(g(x)) means g first, then f.
