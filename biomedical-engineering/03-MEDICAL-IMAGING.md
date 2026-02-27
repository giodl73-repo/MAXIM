# Medical Imaging Physics

## The Big Picture

Medical imaging produces spatial maps of tissue properties using different physical phenomena.
Each modality trades resolution, contrast, cost, radiation dose, and temporal resolution
differently. Understanding the physics determines what you can and cannot see — and where
artifacts come from.

```
+---------------------------------------------------------------------+
|              MEDICAL IMAGING MODALITIES                             |
+---------------------------------------------------------------------+
|                                                                     |
|  MRI                   CT                 PET / SPECT              |
|  Nuclear magnetic      X-ray attenuation  Radiotracer              |
|  resonance             (Hounsfield units) distribution             |
|  Soft tissue king      Bone, hemorrhage,  Functional/metabolic     |
|  No ionizing radiation lung, fast         activity, oncology       |
|  Slow, expensive       Excellent spatial  Poor spatial resolution  |
|       |                     |                    |                  |
|       v                     v                    v                  |
|  ULTRASOUND            X-RAY / FLUORO     OPTICAL (clinical)       |
|  Acoustic impedance    Projection image   OCT, endoscopy           |
|  mismatch reflection   2D, fast, cheap    Ophthalmology,           |
|  Real-time, portable   Interventional     GI, intravascular        |
|  No ionizing radiation fluoroscopy        Near-surface             |
+---------------------------------------------------------------------+

  IMAGE RECONSTRUCTION: all modalities require solving an inverse problem
  Raw data (k-space, sinogram, counts) -> algorithm -> spatial image
```

---

## MRI Physics

### Nuclear Magnetic Resonance

MRI exploits the quantum mechanical property of spin in hydrogen nuclei (protons), which
constitute most of the signal in biological tissue (water + fat).

```
  NMR FUNDAMENTALS
  ================

  Spin: proton has intrinsic angular momentum -> magnetic moment

  In external field B0:
  - Protons align: parallel (low energy) or anti-parallel (high energy)
  - NET magnetization M0 along B0 (z-axis)
  - Larmor precession: protons precess at frequency ω0 = γ * B0

  γ (gyromagnetic ratio for H): 42.58 MHz/T

  Field Strength  Larmor Frequency (1H)
  1.5 T           63.9 MHz
  3.0 T           127.7 MHz
  7.0 T           298.0 MHz
  (Radio frequency range — hence "RF pulse")

  RF EXCITATION:
  Apply B1 field (RF pulse) at exactly ω0 (resonance condition)
  -> Tips M0 by flip angle α:
     α = 90°  ->  M0 entirely in transverse plane (max signal)
     α = 180° ->  M0 inverted (inversion recovery)
     α = small -> Ernst angle for fast acquisition (GRE sequences)
```

### Relaxation — T1 and T2

```
  RELAXATION AFTER RF EXCITATION
  ================================

  After 90° pulse, two independent relaxation processes:

  T1 — LONGITUDINAL (SPIN-LATTICE) RELAXATION:
  Mz recovers toward M0:  Mz(t) = M0 * (1 - exp(-t/T1))

  T1 is time to recover 63% of longitudinal magnetization.
  Physical mechanism: energy exchange with molecular lattice.
  Shorter T1: small molecules, fat, Gd contrast agent nearby
  Longer T1: water, CSF, large molecules

  T2 — TRANSVERSE (SPIN-SPIN) RELAXATION:
  Mxy decays from M0 to 0:  Mxy(t) = M0 * exp(-t/T2)

  T2 is time to lose 63% of transverse magnetization.
  Physical mechanism: spin-spin dephasing (irreversible).
  Shorter T2: solid-like tissues, cartilage, tendons, metal
  Longer T2: free water, edema, CSF, cysts

  T2* — includes additional dephasing from field inhomogeneity:
  1/T2* = 1/T2 + 1/T2'   (T2' from B0 inhomogeneity)
  T2* < T2 always.
  Relevant for gradient echo sequences, fMRI (BOLD), metal artifacts.

  TISSUE TYPICAL VALUES (1.5 T):
  +---------------+--------+--------+
  | Tissue        | T1 (ms)| T2 (ms)|
  +---------------+--------+--------+
  | Fat           | 260    | 80     |
  | White matter  | 780    | 90     |
  | Gray matter   | 900    | 100    |
  | CSF           | 4000   | 2000   |
  | Liver         | 490    | 40     |
  | Muscle        | 870    | 45     |
  | Blood (art.)  | 1200   | 200    |
  +---------------+--------+--------+

  Contrast strategy:
  T1-weighted: short TR, short TE -> fat bright, water dark
  T2-weighted: long TR, long TE  -> water bright, fat less so
  Proton density: long TR, short TE -> relative proton density
```

### K-Space and Image Reconstruction

<!-- @editor[bridge/P2]: K-space is the Fourier domain but the connection to signal processing fundamentals is never made explicit. The Nyquist sampling theorem governs k-space sampling density → field-of-view; undersampling → aliasing (wrap-around artifact) is exactly the temporal aliasing any DSP engineer knows. Add a one-sentence bridge: "k-space sampling obeys Nyquist: sampling interval Δk = 1/FOV; undersampling produces spatial aliasing identical to temporal aliasing in discrete time signals." -->
```
  K-SPACE FORMALISM
  =================

  K-space is the Fourier transform of the final image.
  Each MRI acquisition fills one or more k-space lines.
  Gradient encoding places each acquisition at a specific
  (kx, ky) k-space location.

  Image = FT^-1 { k-space data }

  FREQUENCY ENCODING (readout gradient Gx):
  Varying Gx during readout -> different protons precess at
  different frequencies -> frequency encodes x-position.
  One readout fills one row of k-space.

  PHASE ENCODING (gradient Gy applied before readout):
  Each phase-encode step applies a different Gy magnitude
  -> protons at different y positions acquire different phase.
  One phase-encode step per TR (one k-space line per repetition).

  K-SPACE STRUCTURE:
  +-------------------------------+
  |  Low spatial frequency: center|
  |  -> overall contrast/signal   |
  |                               |
  |  High spatial frequency: edges|
  |  -> fine detail, edges        |
  +-------------------------------+
  Partial k-space acquisition + zero-fill: faster, but worse SNR.
  Parallel imaging (SENSE, GRAPPA): under-sample k-space,
  use coil sensitivity maps to reconstruct -> acceleration R=2-4x.

  MRI ACQUISITION TIME ≈ TR × N_phase_encodes × NEX
  (NEX = number of signal averages)
  Long TR needed for T2-weighted: slow acquisition.
```

### Pulse Sequences

```
  COMMON PULSE SEQUENCES
  ======================

  SPIN ECHO (SE):
  90° pulse -> TE/2 -> 180° refocusing -> TE -> signal
  Advantage: T2 weighted (not T2*), robust to B0 inhomogeneity
  Disadvantage: slow (long TR for T2w)

  FAST SPIN ECHO (FSE / TSE):
  Multiple 180° pulses per TR -> multiple k-space lines per TR
  -> 4-16x faster than SE. Standard clinical workhorse.

  GRADIENT ECHO (GRE):
  Small flip angle -> short TR possible -> fast
  T2* weighted (not true T2 — sensitive to metal, air)
  Used for: angiography, cartilage, bleeding (hemosiderin)

  INVERSION RECOVERY (IR):
  180° inversion -> TI delay -> 90° excite -> image
  FLAIR (Fluid Attenuated IR): TI chosen to null CSF signal
  -> brain lesions not obscured by bright CSF
  STIR (Short TI IR): TI chosen to null fat signal
  -> edema clearly visible (fat dark)

  EPI (Echo Planar Imaging):
  Fill all of k-space after ONE RF excitation
  -> whole-brain volume in ~2 seconds
  Used for: fMRI (BOLD), diffusion (DWI/DTI), perfusion
  Disadvantage: severe distortion near air/bone interfaces (T2* effects)

  DIFFUSION (DWI/DTI):
  EPI with diffusion-sensitizing gradients (b-value)
  Diffusion-weighted: detects restricted diffusion (acute stroke)
  DTI: diffusion tensor -> white matter tractography
  DWI is standard of care for acute ischemic stroke triage.
```

### Contrast Agents and Safety

```
  MRI CONTRAST AGENTS
  ===================
  Gadolinium (Gd) chelates:
  - Paramagnetic: shortens T1 (bright on T1-weighted images)
  - Extracellular agents: leak through disrupted blood-brain barrier
  - Applications: tumor enhancement, vascular imaging
  - NSF (nephrogenic systemic fibrosis) risk in severe renal failure
  - Gd retention concern: signal in brain (globus pallidus) after
    repeated dosing — significance under investigation

  MRI SAFETY:
  +------------------+-------------------------------------------+
  | SAR              | Specific Absorption Rate — RF heating     |
  |                  | FDA limit: 4 W/kg whole body, 8 W/kg head |
  |                  | Higher field -> higher SAR for same        |
  |                  |   sequence -> sequence modification needed |
  +------------------+-------------------------------------------+
  | Implant heating  | Resonant antenna effect in RF field       |
  |                  | Long conductive implants (deep brain stim  |
  |                  |   leads, spinal cord stim) at risk        |
  +------------------+-------------------------------------------+
  | Projectile       | Ferromagnetic objects in fringe field     |
  |                  | 5 Gauss line defines controlled zone      |
  +------------------+-------------------------------------------+
  | Acoustic noise   | Gradient coil Lorentz forces -> 100+ dB  |
  |                  | Ear protection required                   |
  +------------------+-------------------------------------------+

  FIELD STRENGTH TRADEOFFS:
  1.5 T: clinical standard, lower SAR, most implants conditional
  3.0 T: better SNR (+2x vs 1.5T), higher SAR, faster
  7.0 T: research / specialized clinical, excellent SNR, limited coverage
```

---

## CT Physics

### X-Ray Attenuation

X-ray intensity decays exponentially through matter (Beer-Lambert law):
I = I0 * exp(-μ * x), where μ is the linear attenuation coefficient.

```
  HOUNSFIELD UNITS (HU)
  =====================
  CT encodes μ relative to water:
  HU = 1000 * (μ_tissue - μ_water) / μ_water

  Material           HU Range
  --------           --------
  Air                -1000
  Fat                -100 to -50
  Water              0
  Soft tissue        20 to 80
  Blood (acute)      50 to 80
  Calcification      >200
  Bone (cancellous)  300 to 700
  Bone (cortical)    700 to 3000
  Metal implant      >3000 (saturated, causes artifacts)

  Clinical windows:
  Brain window:   W=80, L=40   -> gray/white matter contrast
  Bone window:    W=2000, L=400 -> cortex visible
  Lung window:    W=1500, L=-500 -> airways, vessels
  Soft tissue:    W=400, L=40   -> abdomen
  (W=window width, L=window level)
```

### Detector Geometry and Acquisition

```
  CT SCANNER EVOLUTION
  ====================

  FAN BEAM (single/multi-detector row):
  X-ray source -> fan beam -> detector arc
  Gantry rotates around patient
  Multiple detector rows: 4-slice -> 64-slice -> 256-slice -> 640-slice

  CONE BEAM CT (CBCT):
  Wide detector area, cone-shaped beam
  Faster acquisition (one rotation = volume)
  Used in: dental (low dose), interventional, radiation therapy

  SPIRAL/HELICAL ACQUISITION:
  Table moves continuously during gantry rotation
  Pitch = table distance per rotation / collimation width
  Pitch > 1: faster scan, less dose, slightly lower resolution
  Pitch < 1: overlapping slices, better z-resolution

  DUAL-ENERGY CT (DECT):
  Two different kVp (e.g., 80 kVp + 140 kVp)
  Different photoelectric vs. Compton attenuation ratios
  -> Material decomposition: separate iodine from calcium,
     detect uric acid (gout), virtual monoenergetic images
     reduce metal artifact
```

### Reconstruction Algorithms

<!-- @editor[bridge/P2]: CT reconstruction is an inverse problem but this framing is implicit, not stated. Make it explicit: the sinogram is a set of line integrals (Radon transform) and reconstruction is Radon inversion. FBP is the analytical solution (ramp-filter then backproject); iterative methods minimize ||Ax - b||. Any engineer who knows linear algebra or numerical methods maps this immediately — this is the core intellectual structure of CT and PET/SPECT reconstruction. -->
```
  CT IMAGE RECONSTRUCTION
  =======================

  RAW DATA: sinogram (line integrals of attenuation vs. angle)
  Same mathematical problem as MRI k-space: inverse transform needed.

  FILTERED BACKPROJECTION (FBP):
  Analytic. Each projection angle backprojected across image.
  Ram-Lak filter (ramp) sharpens image but amplifies noise.
  Fast. Noisy at low dose. The traditional method.

  ITERATIVE RECONSTRUCTION (IR, ASIR, SAFIRE):
  Iterative algorithms minimize difference between measured
  projections and forward projections of candidate image.
  Better noise handling at low dose -> dose reduction 30-50%.
  Slightly waxy/plastic appearance at strong iteration levels.

  MODEL-BASED IR (MBIR, Veo):
  Includes full physics model (X-ray statistics, focal spot,
  detector response). Best image quality at lowest dose.
  Very slow computation (minutes per study). Now GPU-accelerated.

  DEEP LEARNING RECONSTRUCTION (DLR, TrueFidelity, AIR recon):
  Neural network trained on high-dose reference images.
  Denoises low-dose acquisitions. Fast, high quality.
  FDA-cleared as IIR-equivalent, not as diagnostic in isolation.

  DOSE METRICS:
  CTDIvol (mGy): energy deposited per unit volume
  DLP (mGy·cm): CTDIvol × scan length -> total dose indicator
  Effective dose (mSv): DLP × body region k-factor -> risk metric
  Chest CT: ~5-7 mSv (vs. CXR ~0.02 mSv, annual background ~3 mSv)
```

---

## PET and SPECT

Nuclear medicine imaging: introduce a radiotracer, image its distribution.

```
  PET vs. SPECT COMPARISON
  =========================

  +------------------+-----------------------+----------------------+
  | Property         | PET                   | SPECT                |
  +------------------+-----------------------+----------------------+
  | Physics          | Annihilation photons   | Single gamma emitter |
  |                  | (511 keV coincidence) | (80-200 keV)         |
  | Detector         | Ring of scintillators | Rotating gamma camera|
  |                  | (BGO, LSO, LYSO)      | with collimator      |
  | Spatial res.     | 4-8 mm                | 8-15 mm              |
  | Sensitivity      | Higher (no collimator)| Lower                |
  | Typical tracers  | F-18 (FDG, NaF),      | Tc-99m (sestamibi,  |
  |                  | Ga-68, C-11, N-13     |   MDP, HMPAO)        |
  |                  | Rb-82 (cardiac)       | I-123, In-111        |
  | Acquisition time | 10-30 min/bed pos     | 15-30 min/head       |
  | Common use       | Oncology staging,     | Myocardial perf.,    |
  |                  | neurology, cardiology | bone scan, thyroid   |
  +------------------+-----------------------+----------------------+

  FDG-PET MECHANISM:
  F-18 FDG (fluorodeoxyglucose):
  Glucose analog -> taken up by cells proportional to glucose metabolism
  Phosphorylated by hexokinase -> trapped in cell (can't continue glycolysis)
  Cancer cells: Warburg effect (aerobic glycolysis) -> high FDG uptake
  FDG SUV (standardized uptake value) = tracer concentration / (injected dose / body weight)
  SUV > 2.5: typical malignancy threshold (tissue-dependent)

  ATTENUATION CORRECTION:
  Photons absorbed before reaching detector -> underestimate activity
  CT-based attenuation correction: CT HU -> attenuation at 511 keV
  PET/CT: anatomic localization + functional quantification
  PET/MRI: better soft tissue anatomy, no additional radiation

  IMAGE RECONSTRUCTION:
  OSEM (Ordered Subsets Expectation Maximization):
  Iterative ML method. Partitions projections into subsets.
  Converges faster than EM. Standard for PET and SPECT.
  Controls: iterations × subsets = effective EM iterations.
```

---

## Ultrasound

Ultrasound uses acoustic waves rather than electromagnetic radiation. Safe, real-time, portable,
no ionizing radiation — but limited by bone (reflects sound) and air (reflects sound).

### Basic Physics

```
  ULTRASOUND PHYSICS
  ==================

  Sound wave propagation in tissue:
  Speed of sound c ≈ 1540 m/s in soft tissue (varies: fat ~1450, bone ~3500)
  Frequency: 1-20 MHz for diagnostic imaging
  Wavelength λ = c/f:
    2 MHz -> 0.77 mm wavelength (deep imaging, lower resolution)
    15 MHz -> 0.10 mm wavelength (superficial, high resolution)

  FREQUENCY / PENETRATION TRADEOFF:
  +---------------------------+
  | Higher freq -> more resol-|
  |   ution, less penetration |
  | Lower freq -> less resol- |
  |   ution, more penetration |
  +---------------------------+
  2-5 MHz: abdomen, cardiac (deep)
  7-12 MHz: musculoskeletal, breast, vascular (superficial)
  15-20 MHz: skin, intravascular (IVUS)

  ACOUSTIC IMPEDANCE and REFLECTION:
  Z = ρ * c (density × wave speed)
  At interface between two media:
  Reflection coefficient R = ((Z2-Z1)/(Z2+Z1))^2

  Material       Z (MRayl)
  Air            0.0004       Large mismatch with tissue -> total reflection
  Fat            1.38         Small mismatch with water
  Soft tissue    1.65         Standard
  Bone           7.8          Large mismatch -> blocks ultrasound

  Transducer pulse:
  Piezoelectric crystal (PZT) vibrates at resonant frequency
  Transmits pulse -> pulse echoes back from interfaces -> same
  crystal receives echo -> time of flight -> depth
  z = c * Δt / 2
```

### Imaging Modes

```
  ULTRASOUND IMAGING MODES
  ========================

  A-MODE (Amplitude): single scanline, echo amplitude vs depth.
  Historical; ophthalmology still uses it.

  B-MODE (Brightness): multiple scanlines sweep across a plane.
  Echo amplitude -> brightness. Standard 2D image. Real-time.

  M-MODE (Motion): B-mode along one scanline vs time.
  High temporal resolution. Cardiac valve motion, fetal heart rate.

  DOPPLER:
  Frequency shift when reflector is moving:
  Δf = 2 * f0 * v * cos(θ) / c

  Pulsed Wave (PW): range-gated, one location
  Continuous Wave (CW): no depth gating, higher velocity range
  Color Flow Imaging: color-coded velocity superimposed on B-mode
  Power Doppler: magnitude of flow signal (no directional info)

  Aliasing: velocity > Nyquist limit -> aliasing. Nyquist:
  v_max = c * PRF / (4 * f0 * cos θ)
  Solution: lower frequency, increase PRF, use CW Doppler.

  TISSUE HARMONIC IMAGING:
  Nonlinear propagation generates harmonics (2f0, 3f0...)
  Receive at 2f0 only: reduced artifact, better contrast
  Standard on modern systems for difficult imaging windows.

  ELASTOGRAPHY:
  Tissue stiffness mapping. Two approaches:
  Strain elastography: apply compression manually, map strain
  Shear wave: focused US push pulse -> shear wave -> wave speed
    mapped to stiffness (E = 3ρc²). Liver fibrosis staging.
```

---

## Image Quality Metrics

```
  IMAGING PERFORMANCE METRICS
  ============================

  +------------------+------------------------------------------+
  | SNR              | Signal-to-noise ratio                    |
  | (Signal/Noise)   | MRI: proportional to B0^1.5, voxel vol  |
  |                  | CT: inversely proportional to dose^0.5   |
  +------------------+------------------------------------------+
  | CNR              | Contrast-to-noise ratio                  |
  | (Contrast/Noise) | (Signal_A - Signal_B) / Noise            |
  |                  | What actually determines visibility       |
  +------------------+------------------------------------------+
  | Spatial          | MTF (modulation transfer function)       |
  | Resolution       | Described as line pairs per mm (lp/mm)   |
  |                  | CT at 50% MTF: ~0.5 lp/mm (0.3mm pixel) |
  |                  | MRI: typically 0.3-1mm in-plane          |
  |                  | PET: 4-8 mm FWHM                        |
  |                  | US: frequency-dependent (~0.3-1mm)       |
  +------------------+------------------------------------------+
  | Temporal         | How fast image updates                   |
  | Resolution       | US: real-time (30-100 fps)               |
  |                  | MRI: seconds to minutes per volume       |
  |                  | CT: <1 second (cardiac gated)            |
  |                  | PET: 10-30 min/bed position              |
  +------------------+------------------------------------------+
  | Sensitivity/     | Diagnostic accuracy metrics              |
  | Specificity      | Not purely physics — depends on reader,  |
  |                  | protocol, post-processing                |
  +------------------+------------------------------------------+
```

---

## PACS and DICOM

```
  CLINICAL IMAGING INFRASTRUCTURE
  =================================

  DICOM (Digital Imaging and Communications in Medicine):
  - Standard format for medical images (ISO 12052)
  - Image data + metadata in one file (UID, patient, modality, etc.)
  - Mandatory for FDA-cleared medical imaging devices
  - Structured as series -> studies -> patients -> hierarchy
  - DICOM SR: structured reports; DICOM RT: radiotherapy

  PACS (Picture Archiving and Communication System):
  Modality -> DICOM send -> PACS server -> radiologist workstation
  Replaces film. Enables teleradiology. Integration with EHR/RIS.

  KEY DICOM UIDs:
  SOP Instance UID: unique per image
  Series UID: unique per acquisition series
  Study UID: unique per imaging study
  Patient ID: institution-specific (not globally unique)

  Bridge for software engineers:
  DICOM is a messaging and file format standard older than XML.
  It has its own binary encoding, its own tag namespace (GGGG,EEEE),
  and its own network protocol (DIMSE over TCP/IP).
  Tools: dcm4che (Java), pydicom (Python), OsiriX (macOS viewer),
  3D Slicer (open source workstation), Horos.
  Cloud PACS: Google Healthcare API supports DICOMweb standard.
```

---

## Common Confusion Points

**T1 vs. T2 weighting**: T1-weighted images look good anatomically (fat is bright, water is dark).
T2-weighted images are pathology-sensitive (most pathology = increased water = bright on T2).
Gadolinium enhancement appears on T1-weighted images (shortens T1 -> brighter). FLAIR and STIR
are special inversion recovery sequences, not simply T1 or T2.

**T2 vs. T2***: T2 is the intrinsic spin-spin relaxation time of the tissue. T2* includes
additional dephasing from magnetic field inhomogeneities (susceptibility effects, metal implants,
air-tissue interfaces). Spin echo sequences refocus T2* effects. Gradient echo sequences do not
— making them sensitive to hemorrhage (hemosiderin), iron, and calcification, but also prone to
metal artifacts.

**Hounsfield units and window/level**: The raw CT data spans thousands of HU. "Windowing" maps
a subrange to the display grayscale. Changing the window does not change the underlying data —
it only changes the display. Two radiologists using different windows on the same scan will
see apparently different images.

**FBP vs. iterative CT reconstruction**: FBP is fast and historically the standard; iterative
reconstruction has better noise properties especially at low dose but can produce overly smooth
images at high iteration counts. Clinical recommendation: use the lowest dose protocol that
gives diagnostic quality for the specific question — iterative reconstruction enables this.

**PET SUV is semi-quantitative**: SUV is normalized by injected dose and body weight, but still
affected by uptake time, blood glucose level, patient weight distribution, and reconstruction
parameters. An absolute SUV cut-off cannot replace clinical judgment and comparison to baseline.

**Ultrasound acoustic shadowing**: Objects that strongly absorb or reflect sound (gallstones,
calcifications, bone) cast an acoustic shadow distal to themselves. This is both a limitation
(can't see behind bone) and a diagnostic feature (posterior acoustic shadowing = hallmark of
gallstone on US).

---

## Decision Cheat Sheet — Modality Selection

| Clinical Question | First Choice | Why |
|---|---|---|
| Acute stroke | MRI (DWI) | Detects ischemia in minutes, no radiation |
| Acute hemorrhage | CT (non-contrast) | Fast, bright blood on CT |
| Bone fracture | CT | Superior bone detail, Hounsfield units |
| Soft tissue tumor | MRI | Superior soft tissue contrast |
| Lung, thoracic | CT | High contrast between air and soft tissue |
| Cardiac anatomy | CT or MRI (no radiation) | Gated acquisition |
| Cardiac function | Echo (ultrasound) | Real-time, Doppler |
| Myocardial perfusion | PET (Rb-82) or SPECT | Functional imaging |
| Metabolic/oncology staging | PET/CT (FDG) | Warburg effect |
| Liver fibrosis | MRI elastography | Non-invasive shear wave |
| Pregnancy | Ultrasound | No radiation, real-time, portable |
| Joint cartilage | MRI | T2 mapping, dGEMRIC |
| Prostate cancer | MRI (multiparametric) | PI-RADS scoring |
| Thyroid nodule | Ultrasound first | Size, vascularity, calcification |
