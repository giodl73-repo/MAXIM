# Polarization

## The Big Picture

Light is a transverse electromagnetic wave: the electric field oscillates perpendicular to the direction of propagation. Polarization describes the geometric shape that E traces out as a function of time. There are two complete formalisms — one for fully polarized light (Jones), one for partially polarized or mixed light (Stokes/Mueller):

```
+------------------------------------------------------------------+
|                    POLARIZATION LANDSCAPE                         |
|                                                                  |
|  POLARIZATION STATES      JONES CALCULUS    STOKES/MUELLER       |
|  ------------------       -------------     ------------         |
|  Linear polarization      2x1 complex       4x1 real vector      |
|  Circular polarization    Jones vector      Stokes vector         |
|  Elliptical polarization  2x2 Jones matrix  4x4 Mueller matrix   |
|  Partial polarization                       handles depolarization|
|  Unpolarized                                                      |
|                                                                  |
|  PHYSICAL MECHANISMS      APPLICATIONS                           |
|  ------------------       ------------                           |
|  Birefringence            LCD displays                           |
|  Reflection (Brewster)    Optical isolators                      |
|  Scattering               Stress analysis                        |
|  Dichroism                Ellipsometry                           |
|  Faraday rotation         Remote sensing                         |
|  Waveplates               3D cinema                              |
+------------------------------------------------------------------+
```

---

## Polarization States

The electric field of a monochromatic wave propagating in the z direction:

```
  E(z,t) = Ex * cos(kz - wt + phi_x) * x_hat
          + Ey * cos(kz - wt + phi_y) * y_hat

  Ex, Ey = amplitudes
  phi_x, phi_y = phases
  delta = phi_y - phi_x = relative phase difference

  STATE                CONDITION
  -----                ---------
  Linear horizontal    Ey = 0
  Linear vertical      Ex = 0
  Linear at angle      Ex, Ey nonzero; delta = 0 or pi
  Right circular       Ex = Ey; delta = -pi/2  (E rotates clockwise as seen by receiver)
  Left circular        Ex = Ey; delta = +pi/2
  Elliptical           All other cases

  Visualization of E-field tip trajectory (looking at source, xy plane):

  Linear horizontal:   --------    Linear 45 deg: /
  Linear vertical:        |        Right circular: O (clockwise)
  Right elliptical:    (  )        Left elliptical: (  ) (counterclockwise)
```

**Warning on circular polarization handedness convention**: "Right circular" means E rotates clockwise when viewed by the receiver (looking at the source). Some older optics texts use the opposite convention (right-hand screw rule along propagation direction). IEEE/physics community differs from optics community. Always verify which convention is being used.

---

## Malus's Law

Fundamental result for linear polarizers:

```
  I_transmitted = I_incident * cos^2(theta)

  theta = angle between polarizer transmission axis and incident polarization

  theta = 0:   I_trans = I_incident  (full transmission)
  theta = 90:  I_trans = 0           (extinction)
  theta = 45:  I_trans = I/2         (half power)
```

---

## Brewster's Angle

At a specific incidence angle, reflected light is completely s-polarized (TE only; no p-polarization in reflection):

```
  tan(theta_B) = n2 / n1

  For air to glass (n2 = 1.5): theta_B = arctan(1.5) = 56.3 deg

  p-polarization (TM): E-field in the plane of incidence
  s-polarization (TE): E-field perpendicular to plane of incidence
  (s from German "senkrecht" = perpendicular)

  At Brewster's angle:
  - Refracted and reflected rays are perpendicular to each other
  - r_p = 0 (no reflected p-component)
  - Reflected beam is 100% s-polarized

  Application: polarized sunglasses block s-polarization (horizontal)
  which is the dominant component of glare from horizontal surfaces
  (water, roads). Camera polarizing filters work the same way.
```

---

## Jones Calculus

For **fully polarized** light only. Works with complex amplitude, so it handles phase.

### Jones Vectors

```
  Electric field = [Ex * exp(i*phi_x)]  = E0 * [cos(theta)]
                   [Ey * exp(i*phi_y)]          [sin(theta)*exp(i*delta)]

  Common Jones vectors (normalized):

  Horizontal linear:   [1]     Vertical linear:   [0]
                       [0]                        [1]

  Linear at +45:       [1] / sqrt(2)
                       [1]

  Linear at -45:       [ 1] / sqrt(2)
                       [-1]

  Right circular:      [ 1] / sqrt(2)     (RHC: delta = -pi/2)
                       [-i]

  Left circular:       [1] / sqrt(2)      (LHC: delta = +pi/2)
                       [i]
```

### Jones Matrices for Common Elements

```
+------------------------------------------------------------------+
|  ELEMENT                      JONES MATRIX                       |
|  -------                      ------------                       |
|                                                                  |
|  Linear polarizer (horizontal)  [1 0]                           |
|                                 [0 0]                           |
|                                                                  |
|  Linear polarizer (vertical)    [0 0]                           |
|                                 [0 1]                           |
|                                                                  |
|  Linear polarizer at angle theta:                                |
|  [cos^2(theta)      sin(theta)cos(theta)]                       |
|  [sin(theta)cos(theta)   sin^2(theta)  ]                        |
|                                                                  |
|  Half-wave plate (fast axis at 0):                               |
|  [1  0]  (QWP: retardation = pi/2 between slow and fast axes)   |
|  [0 -1]                                                          |
|                                                                  |
|  Quarter-wave plate (fast axis at 0):                            |
|  [1  0 ]  = [1    0  ]                                          |
|  [0  i ]    [0  exp(i*pi/2)]                                    |
|                                                                  |
|  Rotation matrix (rotate polarization by angle theta):          |
|  [ cos(theta)  sin(theta)]                                      |
|  [-sin(theta)  cos(theta)]                                       |
|                                                                  |
|  Faraday rotator (rotation by theta, nonreciprocal):            |
|  [ cos(theta)  sin(theta)]  (same form but different physics)   |
|  [-sin(theta)  cos(theta)]                                       |
+------------------------------------------------------------------+
```

### Composing Systems

```
  For elements E1, E2, E3 (light passes E1 first):
  J_total = E3 * E2 * E1

  Output field: E_out = J_total * E_in

  Same matrix multiplication order as ABCD matrices:
  rightmost matrix = first element encountered.

  Example: Linear polarizer at 0 deg, then QWP fast axis at 45 deg:

  J = QWP(45) * LP(0)

  Input: unpolarized? Jones doesn't handle unpolarized -- use Stokes.
  Input: horizontal linear -> becomes right circular? Check:

  QWP(45) = 1/sqrt(2) * [1-i  1+i]
                         [1+i  1-i] ... (rotated QWP)

  -> Horizontal linear [1,0] becomes circular [left or right depending on orientation]
  This is how LCDs and waveplates generate circular polarization.
```

---

## Stokes Parameters and Mueller Calculus

For **partially polarized or unpolarized light**. Uses measurable intensities only -- no phase information required directly.

### Stokes Parameters

Defined in terms of six measurements with a polarimeter:

```
  S0 = I_x + I_y = total intensity
  S1 = I_x - I_y = excess linear horizontal over vertical
  S2 = I_45 - I_135 = excess linear +45 over -45
  S3 = I_R - I_L = excess right circular over left circular

  Stokes vector: S = [S0, S1, S2, S3]^T

  For fully polarized light: S0^2 = S1^2 + S2^2 + S3^2
  For partially polarized:   S0^2 > S1^2 + S2^2 + S3^2
  For unpolarized:           S1 = S2 = S3 = 0

  Degree of polarization:
  DOP = sqrt(S1^2 + S2^2 + S3^2) / S0    [0 to 1]

  Common states:
  Horizontal linear:  [1,  1, 0, 0]
  Vertical linear:    [1, -1, 0, 0]
  Linear +45 deg:     [1,  0, 1, 0]
  Right circular:     [1,  0, 0, 1]
  Left circular:      [1,  0, 0,-1]
  Unpolarized:        [1,  0, 0, 0]
```

### Poincare Sphere

Visual representation of all polarization states:

```
  Sphere of radius 1 (normalized):
  - North pole: right circular
  - South pole: left circular
  - Equator: all linear polarizations (at various angles)
  - Northern hemisphere: right-elliptical
  - Southern hemisphere: left-elliptical
  - Longitude: 2 * polarization angle
  - Latitude: related to ellipticity

  QWP effect: rotation around an axis through the poles
  HWP effect: rotation by 180 deg (reflection through equatorial plane)
  General waveplate: rotation around equatorial axis
```

### Mueller Matrices

4x4 real matrices acting on Stokes vectors. Can represent depolarizing elements (unlike Jones):

```
+------------------------------------------------------------------+
|  ELEMENT              MUELLER MATRIX                             |
|  -------              -----                                      |
|                                                                  |
|  Linear polarizer     [1  1  0  0]                              |
|  (horizontal) *1/2    [1  1  0  0]                              |
|                        [0  0  0  0]                              |
|                        [0  0  0  0]                              |
|                                                                  |
|  Linear polarizer     [1  0  1  0]                              |
|  (+45 deg) *1/2       [0  0  0  0]                              |
|                        [1  0  1  0]                              |
|                        [0  0  0  0]                              |
|                                                                  |
|  Quarter-wave plate   [1  0   0   0]                            |
|  (fast axis horiz)    [0  1   0   0]                            |
|                        [0  0   0  -1]                            |
|                        [0  0   1   0]                            |
|                                                                  |
|  Half-wave plate      [1  0   0   0]                            |
|  (fast axis horiz)    [0  1   0   0]                            |
|                        [0  0  -1   0]                            |
|                        [0  0   0  -1]                            |
|                                                                  |
|  Ideal mirror         [1  0   0   0]                            |
|  (at normal           [0  1   0   0]                            |
|   incidence)          [0  0  -1   0]   <- handedness reverses   |
|                        [0  0   0  -1]                            |
+------------------------------------------------------------------+

  System composition: M_total = M_n * ... * M2 * M1
  Stokes output: S_out = M_total * S_in
```

---

## Birefringence

Anisotropic crystals have a refractive index that depends on polarization direction and propagation direction.

```
  Uniaxial crystal (e.g., calcite, quartz):
    One optical axis (c-axis)
    Ordinary ray (o-ray): n_o, same in all directions, obeys Snell normally
    Extraordinary ray (e-ray): n_e(theta), varies with angle to optical axis

  Calcite: n_o = 1.658, n_e = 1.486  (negative uniaxial: n_e < n_o)
  Quartz:  n_o = 1.544, n_e = 1.553  (positive uniaxial: n_e > n_o)

  Birefringence: Delta_n = n_e - n_o

  Retardation (phase difference after propagating distance L):
    Gamma = (2*pi / lambda) * Delta_n * L

  For a given retardation target (e.g., lambda/4 plate):
    L = lambda / (4 * |Delta_n|)
    For quartz at 550nm: L = 550nm / (4 * 0.009) ~ 15 um (zero-order plate)
```

### Waveplates

```
  Quarter-wave plate (QWP): Gamma = pi/2 = lambda/4 retardation
    Fast axis aligned with one linear polarization component
    Slow axis at 90 deg from fast axis
    Effect: converts linear to elliptical/circular polarization
    -> Linear at 45 deg to waveplate axes -> circular polarization

    Input: [1, 1] (linear at 45 deg, equal components)
    After QWP: [1, 1*exp(i*pi/2)] = [1, i]  -> right circular

  Half-wave plate (HWP): Gamma = pi = lambda/2 retardation
    Rotates the polarization ellipse
    -> Linear at angle theta to fast axis -> linear at angle -theta
    Effectively: reflects polarization angle about fast axis
    Input: linear at 30 deg, fast axis at 0 deg -> output: linear at -30 deg

  Common waveplate configurations:
  QWP(45 deg) after linear(0): creates circular polarization
  HWP(22.5 deg) after linear(0): rotates to linear(45 deg)
  Two QWPs: can simulate any retardation
```

---

## LCD Displays — Twisted Nematic Operation

This is a direct application of Jones calculus to consumer electronics:

```
  Unactivated (ON state for normally white):
  +--polarizer (0 deg)--+
  |                     |
  |  liquid crystal      |  <-- molecules rotate 90 deg through cell
  |  layer (90 deg twist)|     (twisted nematic = TN)
  |                     |
  +--polarizer (90 deg)-+

  Light path: enters H-polarized -> TN layer rotates polarization 90 deg
  -> now V-polarized -> passes rear polarizer -> BRIGHT

  Activated (voltage applied):
  +--polarizer (0 deg)--+
  |                     |
  |  LC molecules       |  <-- molecules align with field, lose twist
  |  align vertical     |
  |                     |
  +--polarizer (90 deg)-+

  Light path: enters H-polarized -> no rotation -> blocked by rear polarizer -> DARK

  IPS mode: in-plane switching; both electrodes on same substrate;
  molecules rotate in plane -> better viewing angles, more accurate color
  VA mode: vertical alignment; molecules tilt vertically when activated;
  high contrast ratio, some viewing angle issues
```

---

## Optical Isolators (Faraday Effect)

Faraday rotation is non-reciprocal — the rotation does not reverse on back-propagation. This enables one-way transmission:

```
  Forward propagation:
  Polarizer (0 deg) -> Faraday rotator (+45 deg) -> Polarizer (45 deg)
  -> passes through (polarization matches output polarizer)

  Backward propagation:
  Polarizer (45 deg) -> Faraday rotator (+45 deg AGAIN, not -45)
  -> now 90 deg -> blocked by input polarizer (0 deg)

  Why non-reciprocal: rotation sense depends on B-field direction,
  not on light propagation direction. Counterpropagating beam still
  sees +45 deg rotation (not -45 deg as it would for a wave plate).

  Application: protect laser sources from back-reflections
  (back-reflections into a laser cause instability or damage).
  Every fiber laser and semiconductor laser in a communication
  system has an isolator at its output.

  Isolation: typically 30-60 dB (1000x to 1 million x power reduction)
```

---

## Decision Cheat Sheet

| I need to... | Use |
|---|---|
| Analyze fully polarized light through a system | Jones calculus (2x1 vectors, 2x2 matrices) |
| Analyze partially polarized or depolarizing system | Stokes/Mueller (4x1 vectors, 4x4 matrices) |
| Convert linear to circular polarization | QWP with fast axis at 45 deg to linear polarization |
| Rotate linear polarization by angle theta | HWP with fast axis at theta/2 from input polarization |
| Protect a laser from back-reflections | Optical isolator (Faraday rotator + polarizers) |
| Understand LCD pixel switching | Twisted nematic Jones analysis |
| Measure film thickness / optical constants | Ellipsometry (Stokes parameter measurement) |
| Eliminate glare from horizontal surfaces | Polarized filter aligned vertically |
| Understand why sky is blue (Rayleigh scattering) | Scattering induces partial polarization; Stokes S1 |
| Check stress in glass or plastic | Photoelasticity: birefringence induced by stress |

---

## Common Confusion Points

**Jones vs. Stokes**: Jones requires coherent, fully polarized light and tracks phase. Stokes uses only intensity measurements and handles partial polarization and incoherent superposition. If you need to handle unpolarized light or multiple incoherent sources, Jones fails — use Stokes/Mueller.

**QWP orientation matters critically**: A QWP converts linear to circular ONLY when the linear polarization is at 45 deg to the waveplate's fast axis. At 0 deg or 90 deg, the QWP does nothing (the light is already aligned with a principal axis). Small alignment errors create elliptical rather than circular polarization.

**HWP doubles angles**: If you want to rotate polarization from 0 to 45 deg, put the HWP fast axis at 22.5 deg. The general rule: output angle = 2*(HWP angle) - (input angle). This is often counterintuitive the first time.

**Faraday rotation vs. mechanical rotation**: A mechanical rotator (e.g., a twisted fiber) IS reciprocal — backward-propagating light unrotates. Faraday rotation is NOT reciprocal. This is the physical basis for the optical isolator.

**Mirror handedness reversal**: A mirror reverses handedness. Right circular becomes left circular on reflection. The Mueller matrix for a mirror has -1 in the S3 diagonal position. This matters for retroreflector designs and free-space optical links.

**Birefringent vs. dichroic polarizers**: A waveplate (birefringent element) shifts phase between polarization components without absorbing. A polarizer (dichroic, like Polaroid sheet) absorbs one component. These are different devices with different loss profiles.
