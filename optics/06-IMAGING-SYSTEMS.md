# Imaging Systems

## The Big Picture

An imaging system maps the object space to the image space. The quality of that mapping is characterized by the system's response to spatial frequencies — identical in concept to the frequency response of a linear system in signal processing. The PSF is the impulse response; the OTF is the transfer function; MTF is its magnitude:

```
+------------------------------------------------------------------+
|                    IMAGING SYSTEM LANDSCAPE                      |
|                                                                  |
|  CHARACTERIZATION        DETECTORS          ENHANCEMENT          |
|  ----------------        ---------          ----------           |
|  PSF (impulse resp)      CCD sensors        Deconvolution        |
|  OTF (transfer fn)       CMOS sensors       Adaptive optics      |
|  MTF (magnitude)         sCMOS (scientific) Computational photo  |
|  Rayleigh/Abbe limit     EMCCD              HDR, focus stacking  |
|                          InGaAs arrays      Light field cameras  |
|                                                                  |
|  MEDICAL IMAGING         SUPER-RESOLUTION   RANGING/DEPTH        |
|  -------------           ---------------    ------               |
|  OCT (retina, heart)     STED microscopy    LiDAR                |
|  Endoscopes              PALM/STORM         Structured light     |
|  Surgical microscopes    SIM                Stereo vision        |
|  Fundus cameras          Expansion micro    Time-of-flight       |
+------------------------------------------------------------------+
```

The key mental model: **every imaging system is a low-pass filter**. Objects with spatial frequencies above the cutoff (limited by wavelength and NA) are not reproduced. Super-resolution techniques push past this classical limit by exploiting additional physics.

---

## Point Spread Function and Optical Transfer Function

### PSF: The Impulse Response

```
  A perfect point object (delta function) at the input maps to a
  finite blob at the output: this is the PSF h(x, y).

  For a circular aperture (lens), the PSF is the Airy pattern:
  I(r) = I0 * [2*J1(pi*D*r / (lambda*f)) / (pi*D*r / (lambda*f))]^2

  J1 = first-order Bessel function of the first kind
  D = aperture diameter
  f = focal length
  r = distance from center in image plane

  First zero of J1(x) at x = 3.832 -> first dark ring at:
  r_Airy = 1.22 * lambda * f / D = 1.22 * lambda * f/#

  At f/4, lambda = 550nm: r_Airy = 1.22 * 550nm * 4 = 2.7 um (radius)
  Airy disk diameter = 5.4 um

  If CCD pixel pitch > Airy disk: pixel-limited resolution
  If CCD pixel pitch < Airy disk: diffraction-limited resolution
```

### OTF: The Transfer Function

```
  OTF = Fourier transform of PSF

  OTF(fx, fy) = FT{h(x,y)}

  For a coherent system: OTF = Pupil function (directly)
  For an incoherent system: OTF = autocorrelation of pupil function

  Components:
  MTF = |OTF|  (Modulation Transfer Function -- the amplitude)
  PTF = phase(OTF)  (Phase Transfer Function)

  MTF tells you: what fraction of contrast is preserved at each spatial frequency.
  MTF = 1: perfect contrast  (100% modulation preserved)
  MTF = 0: no information    (spatial frequency completely lost)

  MTF measurement:
  - Slanted edge method: sharp edge at 5-10 deg, compute derivative (ESF->LSF), then FT
  - Resolution chart (USAF 1951): visual, qualitative
  - Interferometric PSF measurement: most precise

  MTF cutoff frequency (incoherent):
  f_cutoff = 2*NA / lambda = D / (lambda * f)  [cycles/mm in image plane]
  = NA / (lambda * magnification)  [cycles/mm in object plane]

  For NA=0.9, lambda=550nm (oil immersion microscope):
  f_cutoff = 2*0.9/550nm = 3.27 x 10^6 cycles/mm = 3272 cycles/mm
  -> minimum resolvable period = 1/f_cutoff = 305 nm
```

---

## Resolution Limits

```
  CRITERION          FORMULA           INTERPRETATION
  ---------          -------           --------------
  Rayleigh           d = 1.22*lambda/NA Just-resolved: first zero of one
                                        Airy pattern at center of other

  Abbe (coherent)    d = lambda/NA      For coherent illumination
                                        (laser sources, coherent imaging)

  Abbe (incoherent)  d = lambda/(2*NA)  For incoherent illumination
                                        (LED, halogen, fluorescence)

  Sparrow            d = 0.95*lambda/NA No dip between two point images
                                        (most permissive criterion)

  For a 100x oil immersion objective (NA=1.4) at lambda=500nm:
  Rayleigh: d = 1.22 * 500nm / 1.4 = 435nm (diffraction limit)
  Abbe (incoherent): d = 500nm / (2 * 1.4) = 178nm
  With 405nm UV excitation: d = 145nm

  These are the "diffraction limits" that super-resolution techniques overcome.
```

---

## CCD vs. CMOS Sensors

```
+------------------------------------------------------------------+
|  PROPERTY        CCD                    CMOS                     |
|  --------        ---                    ----                     |
|  Architecture    Charge transfer        Per-pixel amplifier      |
|                  (bucket brigade)       (active pixel)           |
|                                                                  |
|  Readout         Sequential (shift out) Random access per-pixel  |
|                  Single on-chip ADC     Per-column or per-pixel  |
|                                                                  |
|  Read noise      Low (2-5 e-)           Higher historically;     |
|                                         modern sCMOS: 1-2 e-     |
|                                                                  |
|  Full-well       High (100k+ e-)        Lower per pixel          |
|  capacity                               (dynamic range tradeoff) |
|                                                                  |
|  Dynamic range   High (>70 dB)          Moderate (60-70 dB CCD-  |
|                                         comparable in modern)    |
|                                                                  |
|  Shutter type    Global (all pixels     Rolling (row-by-row)     |
|                  same exposure)         or global shutter option |
|                                                                  |
|  Rolling shutter                        Skew artifacts for fast  |
|  artifacts       None                   moving objects           |
|                  (global only)                                   |
|                                                                  |
|  Power           Higher (charge         Lower (local readout)    |
|  consumption     transport lossy)                                |
|                                                                  |
|  Uniformity      Excellent (single      Column FPN (fixed pattern|
|                  readout chain)         noise) -- calibrated out |
|                                                                  |
|  Speed (frame    Moderate (serial       High (parallel readout,  |
|  rate)           readout, < 100fps)     >1000fps possible)       |
|                                                                  |
|  Cost            Higher (specialized    Lower (standard CMOS fab)|
|                  process)                                        |
|                                                                  |
|  Current status  Declining in high-vol  Dominant in all markets  |
|                  applications           sCMOS now matches CCD    |
+------------------------------------------------------------------+
```

---

## Adaptive Optics

Corrects wavefront aberrations in real time — originally for astronomy, now ubiquitous in ophthalmology and microscopy.

```
  System architecture:

  Incoming wavefront (aberrated by atmosphere, eye, or sample)
        |
        v
  Wavefront sensor (Shack-Hartmann)
        |
        | measures aberration
        v
  Controller (compute correction)
        |
        | sends correction signal
        v
  Deformable mirror (apply correction)
        |
        v
  Corrected wavefront to science camera or retinal imager

  Shack-Hartmann Wavefront Sensor:
  +----------------+
  |  lenslet array |
  +----------------+
        |
        v
  +----------------+
  |  CCD/CMOS      |
  +----------------+
    Lenslet array: grid of small lenses (subapertures).
    Each lenslet focuses its sub-aperture to a spot on the
    CCD/CMOS sensor.

  Flat wavefront -> regular grid of spots
  Aberrated wavefront -> spots displaced from reference
  Displacement vector map -> wavefront gradient -> integrate -> phase
```

### Astronomical AO

```
  Fried parameter r0: characteristic scale of atmospheric turbulence
  r0 = 10-20cm in good seeing at visible wavelengths (10m telescope aperture: 50+ subapertures needed)
  r0 scales as lambda^(6/5) -> easier at longer wavelengths (why AO started in NIR)

  Isoplanatic angle theta_0:
  Correction valid only within a cone of angle theta_0 from guide star
  theta_0 ~ 2 arcsec at visible, ~10 arcsec at 2.2 um (K-band)

  Natural guide star: need bright star near target
  Laser guide star: create artificial star with resonant Na backscatter at 90km altitude
    -> allows AO anywhere on sky (but tip-tilt still needs natural star -- LGS doesn't measure overall image motion)

  Keck AO: 349-actuator deformable mirror, 500nm Strehl > 0.4 (vs diffraction limit = 1.0)
```

---

## Computational Photography

```
  HDR (High Dynamic Range):
  - Capture multiple exposures (1/1000s, 1/100s, 1/10s, 1s)
  - Merge: use short exposure where bright, long exposure where dark
  - Result: 100dB dynamic range from 60dB sensor
  - Tone mapping: compress HDR for display (HLG, PQ EOTF, HDR10)

  Focus stacking:
  - Capture series at different focus distances (z-stack)
  - Detect sharpness metric per pixel per image (gradient magnitude, Laplacian)
  - Composite: select sharpest pixels from each image
  - Application: macro photography, microscopy of thick samples

  Deconvolution:
  - Observed image g = f * h  + noise  (f = object, h = PSF, * = convolution)
  - Goal: recover f from g knowing (or estimating) h
  - Wiener filter: H*(f) / (|H(f)|^2 + 1/SNR(f))  (optimal linear filter)
    H(f) = OTF, H* = complex conjugate
    Regularizes at frequencies where SNR is low
  - Richardson-Lucy (RL): iterative ML estimator assuming Poisson noise
    Converges to maximum-likelihood solution
    Used in Hubble Space Telescope image restoration (before servicing)
    Medical imaging, astronomy standard

  Light field cameras (plenoptic cameras):
  - Microlens array between main lens and sensor
  - Captures not just x,y but also angle (ray direction) information
  - 4D light field: L(x, y, u, v) -- position and direction
  - Post-capture: refocus to any depth, change perspective, extract depth map
  - Lytro camera: commercial product (2012-2018, now discontinued)
  - Active research for VR/AR, medical imaging
```

---

## Super-Resolution Microscopy

The diffraction limit is not a fundamental physical law — it assumes fluorophores are always on simultaneously. Turn them on/off selectively, and you can localize each one with nanometer precision:

```
  Classical resolution: ~200nm (Abbe limit, NA=1.4, lambda=500nm)

  Technique        Resolution    Principle
  ---------        ----------    ---------
  Confocal         ~200nm        Pinhole rejects out-of-focus light
                   (same as wide-     Better Z-sectioning, not lateral SR
                   field, better Z)

  STED             20-50nm       Stimulated emission depletes periphery
                   (up to 2.5nm  of excitation spot, leaving only
                   reported)     central nanoscale region excitable

  PALM             10-30nm       Single-molecule localization:
  STORM            (lateral)     turn on few molecules, localize centroid
  dSTORM                         to nm, turn off, repeat, reconstruct

  SIM              ~100nm        Moire interference between structured
  (Structured       (2x beyond    illumination and sample
  Illumination)    diffraction)  Linear SIM: 2x; nonlinear SIM: 4x+

  Expansion        ~20nm         Physically expand sample in hydrogel
  microscopy       (using        before conventional imaging
                   standard      (Nobel 2024 to Betzig et al. adjacent)
                   confocal)
```

### STED Mechanics

```
  Excitation PSF (Gaussian spot)
        +
  STED donut beam (zero at center, maximum at periphery)
        |
        v
  Depletion: stimulated emission drives excited molecules back to
  ground state everywhere EXCEPT the donut center

  Remaining fluorescence only from tiny central region
  -> effective PSF << diffraction limit

  d_STED = lambda / (2*n*sin(alpha) * sqrt(1 + I_STED/I_sat))

  I_sat = STED saturation intensity (depends on fluorophore)
  I_STED >> I_sat -> very small effective spot

  Trade-off: high intensity -> photobleaching -> limited images per experiment
```

---

## Optical Coherence Tomography (OCT)

Low-coherence interferometry for depth sectioning. The medical equivalent of ultrasound but using light — much higher resolution, but shallower penetration:

```
  Principle: Michelson interferometer with broadband (low-coherence) source

  Reference arm: mirror at known distance
  Sample arm: light scatters from sample at various depths

  Interference occurs only when:
  |OPD| < l_c (coherence length)

  By scanning reference mirror (TD-OCT) or analyzing spectrum (SD-OCT):
  -> Depth profile (A-scan) from interference vs. depth

  Depth resolution (axial):
  Delta_z = 2*ln(2)/pi * lambda^2 / Delta_lambda
  For SLD at 850nm, Delta_lambda = 40nm:
  Delta_z = 0.44 * (850nm)^2 / 40nm = 7.9 um

  Lateral resolution: same as conventional microscope (depends on NA)

  Types:
    Time-domain (TD-OCT): scan reference mirror mechanically
      -> slow (kiloHz A-scan rate)
    Spectral-domain (SD-OCT): use spectrometer + CCD, no moving parts
      -> 10-100x faster (MHz A-scan rates possible)
    Swept-source (SS-OCT): tunable laser swept in frequency
      -> longer wavelength (1050nm, 1310nm) -> deeper penetration

  Applications:
    Ophthalmology: retinal layers to 5um resolution -> detect macular degeneration
    Cardiology: intravascular OCT catheter (IVOCT) -> coronary plaque imaging
    Dermatology: skin layer structure
    Dentistry: caries detection (non-ionizing radiation)
```

---

## Medical Imaging Optics

```
  Endoscope:
  - Flexible fiber bundle OR rod-lens system (Hopkins design)
  - Hopkins rod-lens: alternating air-glass elements, inverted from traditional
    -> air acts as "lens" material, glass as spacer
    -> very long working distance in narrow tube
  - Modern: chip-on-tip (CMOS at distal end, digital readout)
    -> better image quality, 4K resolution possible
  - GRIN (gradient index) rod lenses: n varies radially
    Equivalent to a thick lens; used as objective or relay in rigid endoscopes
    GRIN relay preserves image without large glass chunks

  Surgical microscope:
  - Parfocal zoom system: image stays focused through magnification change
  - Coaxial illumination: illumination coaxial with observation axis
  - Working distance: 200-400mm (surgeon's hands must fit)
  - 3D/stereoscopic: two parallel paths for stereo vision
  - Integration: OCT, fluorescence (ICG), AR overlay

  Fundus camera (retinal imaging):
  - Flash illumination through dilated pupil
  - Objective forms image of retina on CCD
  - Wide-field variants: 200-degree field of view
  - Scanning laser ophthalmoscope (SLO): raster scan with laser
    -> higher SNR, confocal Z-sectioning possible
    -> combined with OCT = OCT-A (angiography) showing blood flow
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Characterize resolution of an imaging system | MTF measurement (slanted edge method) |
| Maximize lateral resolution in microscopy | Maximize NA (use oil immersion, NA=1.4) |
| Get 3D information from a flat sample | OCT (depth sectioning) or confocal Z-stack |
| Image fluorescent molecules with nanometer resolution | STORM/PALM (10-30nm) |
| Correct atmospheric turbulence for telescope | Adaptive optics with Shack-Hartmann sensor |
| Extend dynamic range beyond sensor capability | HDR bracketing + merge |
| Remove known blur from an image | Wiener filter or Richardson-Lucy deconvolution |
| Image through a thick tissue sample | Two-photon microscopy or SPIM (light sheet) |
| Non-destructive depth imaging of retina/coronary | OCT (spectral-domain or swept-source) |
| Trade off depth of field vs. aperture | Adjust f/#: large f/# = deep DOF, diffraction-limited |

---

## Common Confusion Points

**MTF vs. resolution**: Resolution (Rayleigh, Abbe) is a scalar threshold. MTF is the full spatial frequency response. A system can have good MTF at low frequencies (correct contrast for large features) but bad MTF at high frequencies (blurs fine detail). "Resolution" alone doesn't tell the whole story.

**CCD extinction from market**: Modern scientific CMOS (sCMOS) now matches CCD read noise at 1-2 electrons while offering much higher frame rates and larger sensors. CCDs are legacy in new designs; sCMOS is the current standard for scientific imaging.

**Deconvolution is not free**: Wiener filter and RL both amplify noise at high spatial frequencies. The regularization parameter in Wiener filter is essentially the SNR -- too aggressive and you amplify noise; too conservative and you don't sharpen. Always check the noise level before aggressive deconvolution.

**Super-resolution requires fluorescent labels (mostly)**: STED, PALM, and STORM are fluorescence techniques. They work on labeled samples, not arbitrary transparent objects. Label-free super-resolution exists (e.g., ISCAT, COBRI) but is less established. Expansion microscopy is compatible with any stain after expansion.

**OCT depth vs. confocal depth**: OCT axial resolution (5-15 um) is set by source bandwidth, not NA. Confocal axial resolution is set by NA (depth of focus). OCT can image deeper (mm scale in tissue) than confocal (100-200 um) because it uses coherent gating, not pinhole spatial filtering.

**Adaptive optics "correction" means wavefront, not all aberrations**: AO corrects wavefront phase errors (the "blurring" aberrations). It doesn't correct for geometric distortions, vignetting, or scattering (multiply-scattered light is lost regardless). In thick scattering tissue, AO is less effective because scattering creates truly random, uncorrelatable wavefronts.
