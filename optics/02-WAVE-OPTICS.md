# Wave Optics

## The Big Picture

When feature sizes approach the wavelength of light, rays fail and waves take over. Wave optics is Maxwell's equations applied to bounded geometries — and it maps directly onto the signal processing you already know: diffraction is convolution, lenses perform Fourier transforms, spatial filtering is just a bandpass filter in 2D frequency space.

```
+------------------------------------------------------------------+
|                    WAVE OPTICS LANDSCAPE                          |
|                                                                  |
|  FOUNDATION           DIFFRACTION         INTERFERENCE           |
|  ----------           -----------         ------------           |
|  Huygens-Fresnel      Fraunhofer          Two-beam               |
|  principle            (far field)         (Young, Michelson)     |
|  Wave equation        Fresnel             Multi-beam             |
|  Coherence            (near field)        (Fabry-Perot)          |
|                       Gratings                                   |
|                                                                  |
|  FOURIER OPTICS       HOLOGRAPHY          COHERENCE              |
|  ------------         ----------          ---------              |
|  Lens as FT           Recording           Temporal               |
|  4f system            Reconstruction      (coherence length)     |
|  Spatial filtering    Volume holograms    Spatial                |
|  PSF/OTF              Applications        (van Cittert-Zernike)  |
+------------------------------------------------------------------+
```

The key bridge: **a converging lens performs a 2D spatial Fourier transform** in its back focal plane. If you know the DFT, you understand Fourier optics. Spatial frequency (cycles/mm) maps to angle; temporal frequency maps to color.

---

## Huygens-Fresnel Principle

Foundation of wave diffraction theory:

```
  Huygens (1678): Every point on a wavefront acts as a secondary
  point source emitting spherical wavelets. The new wavefront is
  the envelope of all secondary wavelets.

  Fresnel (1818): Added the interference between wavelets, giving
  a quantitative theory that explains diffraction patterns.

  +--wavefront at t=0--+
  *  *  *  *  *  *  *     <- each point emits a wavelet
  |  |  |  |  |  |  |
  o  o  o  o  o  o  o     <- secondary sources
   \  \ | /  / \ | /
    \   X   /   X
     \  |  /   / \
      +-+-+-+-+-+          <- new wavefront at t = dt
                           (constructive along original direction,
                            destructive off-axis for plane wave)
```

The Fresnel-Kirchhoff diffraction integral formalizes this:

```
  U(P) = -i/lambda * integral_aperture [U(Q) * exp(ikr)/r * cos(theta)] dA

  U(P) = field at observation point P
  U(Q) = field at aperture point Q
  r    = distance from Q to P
  k    = 2*pi/lambda
  theta = angle between normal and Q-to-P direction
```

---

## Diffraction Regimes

Characterized by the Fresnel number N:

```
  N = a^2 / (lambda * L)

  a = aperture half-width
  lambda = wavelength
  L = propagation distance

  +---------+----------+------------------------------------------+
  | N >> 1  | Geometric | Geometric optics valid                   |
  | N ~ 1   | Fresnel   | Near-field diffraction; Fresnel integrals|
  | N << 1  | Fraunhofer| Far-field diffraction; aperture FT       |
  +---------+----------+------------------------------------------+

  Practical threshold for Fraunhofer (far field):
    L >> a^2 / lambda  (Fraunhofer condition)

  Example: a = 1mm aperture, lambda = 500nm
    Fraunhofer regime: L >> 1mm^2 / 500nm = 2 meters
    For lab work: use a lens to bring far field to focal plane
```

---

## Fraunhofer Diffraction

Far-field diffraction pattern = Fourier transform of the aperture function.

### Single Slit

```
  Aperture function: rect(x/a)  (width a, unit transmission)

  Intensity pattern:
  I(u) = I0 * sinc^2(pi*a*u/lambda)
  where u = sin(theta) (spatial variable)

  sinc(x) = sin(x)/x

  Intensity:
     |
  I0 +
     |  *
     | * *
     |*   *
     +-----*-----------*-----------*--> theta
          first          second
          zero at        zero at
          theta = lambda/a   theta = 2*lambda/a

  Central maximum width: 2*lambda/a
  First null: theta = arcsin(lambda/a) ~ lambda/a (small angle)
  -> Narrower slit: wider diffraction pattern (Fourier uncertainty)
```

### Double Slit (Young's Experiment)

```
  Two slits of width a, separated by d:

  I(theta) = I0 * sinc^2(pi*a*sin(theta)/lambda)
                * cos^2(pi*d*sin(theta)/lambda)
           = [single slit envelope] * [double slit fringes]

  Fringe spacing: Delta_theta = lambda/d
  Envelope zeros: theta = lambda/a, 2*lambda/a, ...

  Classic result: fringes prove interference, which requires waves.
  This experiment (1801) killed Newton's corpuscle theory.
```

### Diffraction Grating

N slits with period d:

```
  Grating equation (constructive interference):
    d * sin(theta_m) = m * lambda   (m = 0, +/-1, +/-2, ...)

  m = grating order
  theta_m = diffraction angle for order m

  Resolving power:
    R = lambda / Delta_lambda = m * N
    m = grating order used, N = total number of illuminated slits

  Example: 1200 lines/mm grating, N = 5000 illuminated lines,
  order m = 1: R = 5000 -> resolves lambda and lambda + 0.1nm at 500nm

  Grating dispersion (angular):
    d(theta)/d(lambda) = m / (d * cos(theta_m))

  Blazed grating: groove shaped to concentrate diffraction
  into one specific order (typically m=1) for maximum efficiency.
  Blaze wavelength = wavelength of maximum efficiency.
```

---

## Fresnel Diffraction

Near-field diffraction; cannot use the Fraunhofer approximation.

```
  Fresnel zones: concentric annular zones around axis at aperture,
  each contributing half-period of path-length difference to P.

  Zone radii: r_m = sqrt(m * lambda * L)   (m = 1, 2, 3, ...)

  Zone plate (alternating opaque/transparent zones):
  Acts as a lens! Focal length f = r_1^2 / lambda
  Blocks even (or odd) zones, leaving constructive interference.

  Fresnel integrals:
  C(u) = integral_0^u cos(pi*t^2/2) dt
  S(u) = integral_0^u sin(pi*t^2/2) dt

  Cornu spiral: parametric plot of C(u) vs S(u)
  Diffraction intensity from an aperture = |C + iS|^2
```

---

## Interference

### Two-Beam Interference

Two beams of same frequency, electric fields E1 and E2:

```
  I_total = |E1 + E2|^2
           = I1 + I2 + 2*sqrt(I1*I2) * cos(delta)

  delta = phase difference = (2*pi/lambda) * OPD
  OPD   = optical path difference (n1*L1 - n2*L2)

  Fringe visibility (contrast):
  V = (I_max - I_min) / (I_max + I_min)
    = 2*sqrt(I1*I2) / (I1 + I2)
    = 1 when I1 = I2 (maximum contrast)

  V = 1: perfect fringes (fully coherent beams)
  V = 0: no fringes (incoherent beams or OPD > coherence length)
```

### Michelson Interferometer

```
                     Mirror M1
                        |
  Source --> Beamsplitter ---> Mirror M2
                  |
                Detector

  OPD = 2 * (L1 - L2)   (factor 2: beam travels path twice)

  Applications:
  - Measure displacement to lambda/100 precision
  - Measure refractive index of gas (insert cell in one arm)
  - LIGO gravitational wave detector (L ~ 4km, measures 10^-18 m)
  - FTIR spectrometer (scan M1 while recording intensity)

  The "old world" equivalent: measuring a voltage to ppm precision
  with a Wheatstone bridge. Same null-measurement principle -- you
  measure a difference against a reference, not an absolute value.
```

### Fabry-Perot Etalon

Two parallel partially-reflecting surfaces separated by distance L:

```
  Multiple reflections add coherently:

  R1          R2
  |           |
  |<--- L --->|

  Transmission as function of wavelength (Airy function):
  T(delta) = 1 / (1 + F * sin^2(delta/2))
  where delta = 4*pi*n*L*cos(theta) / lambda
  F = 4R / (1-R)^2   (R = mirror reflectance)

  Transmission peaks: sharp maxima when delta = 2*pi*m (m = integer)
  Peak condition:     2 * n * L * cos(theta) = m * lambda

  Free spectral range (FSR): spacing between adjacent peaks
    FSR = lambda^2 / (2*n*L)   [wavelength units]
    FSR = c / (2*n*L)          [frequency units]

  Finesse: F_n = pi*sqrt(F)/2 = pi*sqrt(R)/(1-R)
    Number of resolvable peaks within one FSR
    Higher R -> sharper peaks -> higher finesse

  Example: L = 1 cm, n = 1.5, R = 0.99
    FSR = c/(2*1.5*0.01) = 10 GHz
    Finesse = pi*sqrt(0.99)/(1-0.99) ~ 313
    Resolution = FSR/Finesse ~ 32 MHz

  Applications: laser line selection, laser linewidth measurement,
  optical spectrum analyzers, cavity for laser oscillation.
```

---

## Coherence

Coherence measures the ability of light to form interference fringes.

```
  TEMPORAL COHERENCE              SPATIAL COHERENCE
  ------------------              -----------------
  Related to spectral width       Related to source angular size
  Measured along beam             Measured across beam

  Coherence length:               Coherence width (van Cittert-Zernike):
  l_c = lambda^2 / Delta_lambda   r_c = lambda / (2 * theta_s)
      = c * tau_c                 theta_s = angular source size

  Can form fringes when:          Can form fringes when:
  OPD < l_c                       source separation < r_c

  Examples:
  HeNe laser:  l_c ~ 30 cm (Delta_lambda ~ 0.002 nm)
  LED (50nm BW): l_c ~ 6 um
  White light: l_c ~ 1 um (hence white-light fringes are few)
  LIGO laser (1 kHz LW): l_c ~ 300 km
```

---

## Fourier Optics

This is where wave optics directly maps to DSP. You know Fourier analysis deeply from MIT — this is the spatial version.

```
  TEMPORAL SIGNAL PROCESSING      FOURIER OPTICS
  --------------------------      --------------
  time t                          position (x, y)
  frequency f (Hz)                spatial frequency (fx, fy) [cycles/mm]
  temporal FT                     2D spatial FT
  bandpass filter                 aperture stop (pupil)
  convolution theorem             PSF = h(x,y) = FT of pupil
  LTI system response             Coherent imaging system
  transfer function H(f)          OTF (optical transfer function)
```

### The Lens as a Fourier Transform

A converging lens of focal length f performs a 2D FT:

```
  Input plane            Lens           Back focal plane
  (object)                                (Fourier plane)

  u(x, y)   ---[lens f]---  U(fx, fy)

  U(fx, fy) = FT{u(x,y)} evaluated at fx = x'/(lambda*f), fy = y'/(lambda*f)

  x', y' = coordinates in back focal plane

  Physical meaning:
    A plane wave at angle theta_x arrives at a single point x' = f * tan(theta_x) ~ f * sin(theta_x)
    An object point at (x, y) creates a spherical wave -> plane wave at specific angle -> point in focal plane
    The focal plane contains the angular spectrum of the input
```

### The 4f Optical Processing System

```
  Input  Lens1  Fourier  Lens2  Output
  plane  (f1)   plane    (f2)   plane
    |      |      |        |      |
    |<-f1->|<-f1->|<--f2-->|<-f2->|

  - Lens 1: FT of input appears in middle (Fourier) plane
  - Place a spatial filter mask in the Fourier plane
  - Lens 2: inverse FT reconstructs the filtered image
  - Total length = 2*f1 + 2*f2

  Spatial filtering examples:
  - Low-pass filter: circular aperture blocking high spatial freq (blur)
  - High-pass filter: central stop blocking low freq (edge enhancement)
  - Notch filter: block specific spatial freq (remove periodic noise)
  - Dark-field microscopy: block zero order (DC), pass scattered light

  Bridge: identical concept to DSP filter design, just operating on
  2D spatial data rather than 1D temporal signals. The "sampling theorem"
  becomes the Nyquist-Shannon criterion for pixel pitch vs. optical bandwidth.
```

---

## Holography

### Recording

```
  Object beam          Reference beam
       \                    /
        \                  /
         v                v
  +-----------------------------+
  |         Holographic         |
  |         recording medium    |   <- interference pattern stored
  |         (film, photorefractive)   as refractive index variation
  +-----------------------------+

  Intensity pattern:
  I = |E_obj + E_ref|^2
    = |E_obj|^2 + |E_ref|^2 + E_obj*E_ref* + E_obj*E_ref

  Last two terms = hologram (contains amplitude AND phase of object)
  Ordinary photography: only |E_obj|^2 (intensity; phase lost)
```

### Reconstruction

```
  Illuminate developed hologram with reference beam alone:

  E_ref * hologram -> E_ref * (E_obj*E_ref*) + ...
                   -> |E_ref|^2 * E_obj + conjugate terms

  Result: reconstructed object wave E_obj appears!
  Observer sees a 3D image as if the original object were present.
```

### Volume vs. Surface Holograms

```
  Surface hologram:  thin recording medium
    Transmission angle responds to Bragg condition loosely
    Reflects/transmits white light producing colored images
    (credit card security holograms)

  Volume hologram:   thick recording medium (> 100 um)
    Strong Bragg selectivity: reconstruction only at specific
    lambda and angle -> high wavelength/angular selectivity
    Used in: WDM multiplexers, holographic storage (research),
    head-up displays, wavelength-selective elements
```

---

## Decision Cheat Sheet

| Situation | Tool |
|-----------|------|
| What is the diffraction pattern of my aperture? | Fraunhofer: Fourier transform of aperture |
| Am I in far-field or near-field? | Compute N = a^2/(lambda*L); N<<1 is far-field |
| I want maximum spectral resolution from a grating | Maximize mN (order times number of slits) |
| I need narrow spectral transmission bands | Fabry-Perot etalon; increase finesse (higher R) |
| I want to spatially filter a laser beam | 4f system with spatial filter mask in focal plane |
| I need to filter out periodic noise from an image | 4f system, block grating peaks in Fourier plane |
| I need to measure distance to nanometer precision | Michelson interferometer |
| My source is broadband -- will it form fringes? | Only if OPD < coherence length l_c = lambda^2/Delta_lambda |
| I want to record a 3D image | Holography (need coherent source -- laser) |
| What is the PSF of my imaging system? | FT of pupil function (aperture shape) |

---

## Common Confusion Points

**Fraunhofer vs. Fresnel naming**: Fraunhofer is the FAR field (N << 1, larger distance). Fresnel is the NEAR field. The naming is counterintuitive -- Fresnel came first (1818) and did the more general theory; Fraunhofer's is the simpler limiting case.

**Grating equation and sign convention**: m can be positive or negative. m = 0 is straight-through. m = 1 is first-order diffracted. Reflection gratings: incident and diffracted on same side of grating normal.

**Coherence length and coherence time**: tau_c = l_c / c = 1/(pi * Delta_nu). These are linked. Coherence length is what you compare to OPD; coherence time is what you compare to temporal delays.

**The 4f system reversal**: After two lens Fourier transforms, the image is inverted (FT of FT = time-reversed signal). For a 4f system: output = scaled, inverted version of input (with the filter applied). Account for this when designing spatial filter systems.

**Fabry-Perot: transmission vs. reflection**: At resonance, transmission is HIGH (energy stored in cavity leaks through). Between resonances, reflection is high. This is not obvious intuitively -- it comes from the coherent addition of all round-trip reflections.

**Holography requires coherence**: The object and reference beams must be mutually coherent. OPD between all object paths and reference path must be < l_c. For an extended object, this can require l_c of meters -- hence laser illumination is mandatory (not just "bright" light).
