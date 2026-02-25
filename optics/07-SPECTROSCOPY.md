# Spectroscopy

## The Big Picture

Spectroscopy is the measurement of how matter interacts with light as a function of wavelength (or frequency or wavenumber). It's the primary tool for identifying what something is made of and how much of it is present — from parts per trillion in blood serum to the composition of galaxies 10 billion light-years away.

```
+------------------------------------------------------------------+
|                    SPECTROSCOPY LANDSCAPE                         |
|                                                                  |
|  INTERACTION TYPE     SPECTRAL REGION    INFORMATION OBTAINED    |
|  ----------------     --------------    -------------------     |
|  Absorption           UV-Vis             Electronic transitions   |
|  (Beer-Lambert law)   IR                 Vibrational modes        |
|                        Microwave          Rotational modes        |
|  Emission             UV-Vis, X-ray      Elemental composition    |
|  (excited states)     Gamma              Nuclear transitions      |
|  Scattering           Any (Raman)        Molecular structure      |
|  (photon energy shift) (elastic=Rayleigh)Surface chemistry(SERS) |
|  Fluorescence         UV-Vis-NIR         Labeled molecules,       |
|  (absorb then emit)                      environmental, biosensors|
+------------------------------------------------------------------+

  KEY RULE: The spectrum is a fingerprint.
  Each molecule/atom has a unique absorption/emission pattern.
  Identify the pattern -> identify the substance.
  Measure the amplitude -> measure the concentration.
```

---

## Beer-Lambert Law — Foundation of Quantitative Spectroscopy

```
  A = epsilon * c * l

  A = absorbance (dimensionless, "optical density")
  epsilon = molar extinction coefficient [L/(mol*cm)]
  c = concentration [mol/L]
  l = path length [cm]

  Transmittance: T = I / I0 = 10^(-A)
  Absorbance: A = -log10(T) = log10(I0/I)

  A = 1: T = 10%  (90% absorbed)
  A = 2: T = 1%   (99% absorbed)
  A = 0.1: T = 79% (21% absorbed)

  Linear range: A = 0.01 to ~1.5 (above ~2, stray light, scattering corrupt the measurement)

  Example: hemoglobin in red blood cells
  epsilon_HbO2 at 541nm = 14,900 L/(mol*cm)
  Blood [Hb] ~ 0.15 g/mL = 2.3 mmol/L (MW = 65000 g/mol)
  l = 1 cm cuvette
  A = 14900 * 0.0023 * 1 = 34  (essentially opaque -- use shorter path or dilute)

  Deviations from Beer-Lambert:
  - High concentration: molecular interactions change epsilon
  - Stray light: detector sees non-sample photons at high A
  - Inhomogeneous samples: scattering adds apparent absorption
  - Fluorescence: emitted photons reach detector, artificially reduce A
```

---

## Absorption Spectroscopy

### Electronic Transitions (UV-Vis, 200-800nm)

```
  Transition types (energy ordering, low to high):
  n -> pi* (lone pair to antibonding pi orbital): low-energy visible/UV
  pi -> pi* (bonding to antibonding pi):           UV-Vis, aromatic compounds
  sigma -> sigma*:                                 deep UV (< 200nm)

  Chromophores (UV-Vis absorbing groups):
  +------------------+------------------+---------------------+
  |  Chromophore     |  lambda_max (nm) |  Example            |
  +------------------+------------------+---------------------+
  |  C=C conjugated  |  210-250         |  butadiene: 217nm   |
  |  Benzene ring    |  254             |  toluene, amino-    |
  |  Extended conj.  |  300-600         |  acids, GFP, drugs  |
  |  Carbonyl (C=O)  |  280 (weak)      |  ketones, amides    |
  |  Porphyrin       |  410 (Soret)     |  heme, chlorophyll  |
  |  Transition metal|  400-800         |  Cu, Fe complexes   |
  +------------------+------------------+---------------------+

  Solvent effects (solvatochromism):
  Polar solvent stabilizes polar excited state -> red shift (bathochromic)
  or destabilizes -> blue shift (hypsochromic), depending on transition type
```

### Vibrational Spectroscopy (IR, 2.5-25 um / 400-4000 cm^-1)

```
  Wavenumber nu_bar = 1/lambda = nu/c  [cm^-1]
  4000 cm^-1 = 2500nm = 2.5 um
  400 cm^-1  = 25000nm = 25 um

  IR absorption requires dipole moment change during vibration
  (selection rule: d(mu)/dQ != 0)

  Characteristic group frequencies:
  +------------------+------------------+---------------------+
  |  Bond/Group      |  cm^-1 range     |  Intensity          |
  +------------------+------------------+---------------------+
  |  O-H stretch     |  3200-3600 (broad)| Strong, broad       |
  |  N-H stretch     |  3300-3500       |  Medium             |
  |  C-H stretch     |  2850-3100       |  Medium             |
  |  C=O stretch     |  1650-1850       |  Strong             |
  |  C=C stretch     |  1600-1680       |  Variable           |
  |  C-O stretch     |  1000-1300       |  Strong             |
  |  C-H bend        |  700-900         |  Strong             |
  |  Fingerprint     |  500-1500        |  Complex, unique    |
  +------------------+------------------+---------------------+

  Fingerprint region (500-1500 cm^-1): complex pattern unique to each molecule
  Used for definitive ID by comparison to reference spectra
```

---

## Emission Spectroscopy

### Atomic Emission

```
  Excite atoms to high energy states (flame, plasma, arc)
  -> spontaneous emission at characteristic wavelengths

  Selection rules for atomic transitions (hydrogen-like):
  Delta_l = +/-1  (angular momentum selection rule)
  Delta_m = 0, +/-1

  Hydrogen emission series:
  Lyman:   transitions to n=1    (UV, 91-121nm)
  Balmer:  transitions to n=2    (visible: H_alpha 656nm, H_beta 486nm)
  Paschen: transitions to n=3    (NIR: 820-1875nm)
  Brackett: transitions to n=4   (MIR)

  H_alpha (656nm) is the prominent red line in nebulae and stellar spectra
  H_beta  (486nm) is the blue-green line (second Balmer)

  Kirchhoff's laws of spectroscopy:
  1. Hot dense gas emits continuous spectrum
  2. Hot thin gas emits bright emission lines
  3. Cool thin gas absorbs against bright background -> Fraunhofer lines
     (Fraunhofer dark lines in solar spectrum = solar atmosphere absorption)

  Stellar classification (Harvard sequence: OBAFGKM LTY):
  O: hottest (>30000K), He+ and H lines
  B: 10000-30000K, He and H lines
  A: 7500-10000K, strong H Balmer lines (Vega, Sirius)
  F: 6000-7500K, H + Ca II
  G: 5200-6000K, Ca II + metals (Sun = G2V)
  K: 3700-5200K, metals (Arcturus)
  M: coolest (<3700K), molecular bands TiO, VO
  L, T, Y: brown dwarfs, methane/ammonia bands
```

---

## Fluorescence Spectroscopy

```
  Jablonski diagram (energy level diagram for fluorescence):

  S2 --+--  (higher singlet excited state)
       | IC (internal conversion, fast, ps)
  S1 --+--  (first singlet excited state)
       |  \
       |   \ fluorescence (ns lifetime)
  S0 --+--  (ground state)
       ^
       | absorption (fs)

  T1 ----    (triplet state, reached by ISC from S1)
       |
       | phosphorescence (us to s, spin-forbidden)
  S0 ----

  Key parameters:
    Stokes shift: lambda_emission - lambda_absorption (emission is red-shifted)
      Stokes shift arises from vibrational relaxation in S1 before emission
    Quantum yield: QY = photons emitted / photons absorbed (0 to 1)
    Fluorescence lifetime: tau = 1/(k_r + k_nr)
      k_r = radiative rate, k_nr = non-radiative rates (quenching, IC, ISC)
    Typical lifetimes: 1-10 ns for organic fluorophores
```

### FRET (Forster Resonance Energy Transfer)

```
  Non-radiative energy transfer from donor to acceptor:
  Rate: k_FRET = (1/tau_D) * (R0/r)^6

  R0 = Forster radius (distance for 50% transfer efficiency, 2-8nm typically)
  r  = donor-acceptor distance

  Efficiency: E = 1 / (1 + (r/R0)^6)

  E = 50% at r = R0
  E = 97% at r = 0.5*R0
  E = 3% at r = 2*R0

  FRET is a "molecular ruler" for 1-10nm distances.
  Application: protein conformational change, DNA hybridization,
  biosensors, single-molecule studies.
```

---

## Raman Spectroscopy

```
  Inelastic scattering of photons from molecules:
  Incident photon + molecule -> scattered photon (different frequency) + molecular vibration

  +--lambda_0--+          +--laser--+
  |  incident  | scatter  |         | Raman shifts:
  |   photon   +--------> | Stokes  | nu_Raman = nu_incident - nu_vib
  +------------+          |  shift  | (photon loses energy to vibration)
                          +---------+
                          | anti-S  | nu_Raman = nu_incident + nu_vib
                          |  shift  | (photon gains energy from vibration)
                          +---------+ (weaker, requires thermally excited vibration)

  Selection rule: polarizability must change during vibration
  (complementary to IR: IR requires dipole change)
  Many vibrations are both IR and Raman active, some only one

  Intensity: I_Raman ~ nu^4 (strongly wavelength-dependent)
  -> Short wavelength excitation gives more Raman signal
  -> But: shorter wavelength -> more fluorescence background -> tradeoffs

  Common excitation wavelengths:
  532nm: high signal, fluorescence often overwhelming
  785nm: reduced fluorescence, lower signal, popular for biological samples
  1064nm: minimal fluorescence, much weaker Raman -> use SERS or long integration

  SERS (Surface-Enhanced Raman Spectroscopy):
  Metal nanoparticles (Au, Ag) near molecule -> electromagnetic field enhancement
  Enhancement factor: 10^6 to 10^10 (single-molecule SERS demonstrated)
  Mechanism: localized surface plasmon resonance (LSPR) concentrates E-field
  Application: trace detection, single-molecule fingerprinting
```

---

## Spectrometer Designs

### Czerny-Turner Grating Spectrometer

```
  Entrance slit                                   Detector array
       |                                               |
       +-- collimating mirror -> diffraction grating -> focusing mirror --+

  +--slit--+  +-mirror-+  +--grating--+  +-mirror-+  +--CCD/InGaAs-+
  |         |  |        |  |           |  |        |  |             |
  | narrow  |->|collimt |->|  disperse |->|  focus |->| array det.  |
  | slit    |  | mirror |  |  by angle |  | mirror |  |             |
  +---------+  +--------+  +-----------+  +--------+  +-------------+

  Dispersion: D = (m * lambda) / (d * cos(theta_d))  [deg/nm]
  Linear dispersion on detector: D_L = f * D  [mm/nm]  (f = focal length)
  Spectral range determined by detector array size / D_L

  Focal length: 150mm (compact) to 1000mm (high resolution)
  Gratings: 300-3600 lines/mm; more lines -> more dispersion -> narrower range
  CCD detector: silicon (200-1100nm), cooled for low noise
  InGaAs array: 900-1700nm (NIR/SWIR), thermoelectric cooling

  Resolution = slit width contribution + diffraction limit of grating
  Resolution limited by: R = m*N (grating) or by slit width, whichever worse
```

### Echelle Spectrograph

```
  Uses high diffraction order (m = 10-100) for high dispersion:
  -> Very high resolution per grating
  BUT: overlapping orders must be separated by cross-disperser

  Echelle grating: coarse grating, steep blaze angle
  Cross-disperser: prism or fine grating, perpendicular dispersion

  Result: 2D format on detector -- wavelength in one direction, order in other
  Like a map of spectrum folded back and forth

  Used in: high-resolution astronomical spectroscopy (HIRES on Keck, HARPS)
  Echelle for Doppler radial velocity: lambda/Delta_lambda > 50,000-100,000
  -> Detect stellar motion of 1 m/s (exoplanet discovery tool)
```

---

## FTIR — Fourier Transform Infrared Spectroscopy

FTIR is a Michelson interferometer-based spectrometer. Instead of dispersing light and measuring wavelengths one at a time, it measures the interferogram (intensity vs. mirror position) and Fourier-transforms it to get the spectrum.

```
  Michelson interferometer:
  Source -> beamsplitter -> {reference arm (fixed mirror) + sample arm (scanning mirror)}
         -> detector measures I(delta)  [interferogram]

  I(delta) = integral S(nu) * (1 + cos(2*pi*nu*delta)) d(nu)

  S(nu) = source * sample * detector spectrum
  delta = OPD = mirror displacement x 2

  Spectrum: S(nu) = FT{I(delta)}
  (The interferogram IS the Fourier transform of the spectrum)
```

### FTIR Advantages over Grating Spectrometers

```
  Fellgett (multiplex) advantage:
    Grating: measures one wavelength at a time -> N measurements for N points
    FTIR: measures ALL wavelengths simultaneously
    SNR improvement: sqrt(N) for same measurement time
    N = number of spectral resolution elements (can be 1000+)
    -> FTIR SNR ~ 30x better than grating for same time (sqrt(1000))

  Jacquinot (throughput) advantage:
    Grating: slit limits throughput (entrance aperture is a narrow slit)
    FTIR: uses a circular aperture (Jacquinot stop) -> much larger etendue
    -> typically 40-200x more light collected

  Connes advantage:
    Wavenumber calibration from HeNe laser (position reference) -> very accurate
    Grating calibration depends on mechanical positioning

  Disadvantages:
    Single detector -> no good for imaging
    Moving mirror: vibration sensitivity, alignment critical
    Not ideal for transient phenomena (scan takes seconds)
```

---

## Atomic Spectroscopy Techniques

```
+------------------------------------------------------------------+
|  TECHNIQUE    ANALYTE        DETECTION LIMIT   PRINCIPLE         |
|  ---------    -------        ---------------   ---------         |
|  AAS          Trace metals   ppb-ppt           Absorption of lamp|
|  (Atomic      (single elem.  (graphite         light by ground-  |
|  Absorption)  at a time)     furnace: ppt)     state atoms       |
|                                                                  |
|  ICP-OES      Multi-element  ppb               Plasma (8000-10000K)|
|  (Optical     metals,        simultaneous       excites atoms,    |
|  Emission     metalloids     (30+ elements)    measure emission  |
|  Spectroscopy)|                                                   |
|                                                                  |
|  ICP-MS       Multi-element  ppt-ppq           Plasma + mass     |
|  (Mass Spec)  isotope ratio  10^6x better      spectrometry      |
|               analysis       than OES          (quadrupole/TOF)  |
|                                                                  |
|  XRF          Surface        ppm               X-ray fluorescence|
|  (X-ray       elements,      (non-destructive) K/L shell emission|
|  Fluorescence) coatings                        after X-ray excit.|
|                                                                  |
|  LIBS         In-situ        ppm-ppb           Laser ablation +  |
|  (Laser-      remote         (matrix-          plasma emission   |
|  induced      analysis       dependent)        (portable, standoff)|
|  breakdown)                                                      |
+------------------------------------------------------------------+
```

---

## Astronomical Spectroscopy

```
  Doppler shift (radial velocity):
  Delta_lambda / lambda = v_r / c
  v_r = c * (lambda_obs - lambda_rest) / lambda_rest

  Positive v_r (recession): redshift, lambda_obs > lambda_rest
  Negative v_r (approach): blueshift, lambda_obs < lambda_rest

  Example: H_alpha normally 656.28nm, observed at 656.34nm
  v_r = 3e8 * (656.34-656.28)/656.28 = 3e8 * 9.1e-5 = 27 km/s (recession)

  Cosmological redshift: z = (lambda_obs - lambda_rest) / lambda_rest
  Galaxy at z=1: lambda_obs = 2 * lambda_rest (universe scale factor 2x smaller)
  CMB at z~1100: visible light blueshifted down to microwave

  Radial velocity technique for exoplanets:
  Star wobbles due to orbiting planet -> periodic Doppler shift
  Earth causes ~0.09 m/s wobble on the Sun (requires R = 10^8 resolution)
  51 Peg b (first hot Jupiter, 1995): ~56 m/s wobble -> R ~ 100,000 sufficient
```

---

## Decision Cheat Sheet

| I need to identify/measure... | Use |
|---|---|
| Concentration of a chromophore in solution | UV-Vis absorption + Beer-Lambert |
| Functional groups in an unknown organic compound | IR absorption (FTIR or ATR-IR) |
| Molecular identity (fingerprint) of a solid/liquid | Raman or FTIR |
| Trace metal concentration (ppb level) | ICP-OES (multi-element) or AAS |
| Ultra-trace metals (ppt level) | ICP-MS |
| Surface elemental composition (non-destructive) | XRF |
| Molecule in a fluorescent assay | Fluorescence spectroscopy |
| Distance between two protein domains (1-10nm) | FRET (fluorescence energy transfer) |
| Chemical composition of a star | Absorption/emission spectroscopy + stellar models |
| Galaxy recession velocity | Spectral Doppler shift (z measurement) |
| Best spectral range for organic functional groups | Mid-IR (400-4000 cm^-1), FTIR |
| High resolution + broad range simultaneously | Echelle spectrograph |
| Speed advantage for low-light IR measurement | FTIR (Fellgett + Jacquinot advantages) |

---

## Common Confusion Points

**Absorbance is logarithmic**: A = 2 means 99% absorption, not 2x. A = 3 means 99.9%. Beer-Lambert is log10-based. When combining two absorbers, their absorbances ADD (not multiply): A_total = A1 + A2. This is because: T_total = T1 * T2, and log(T1 * T2) = log(T1) + log(T2).

**Raman and fluorescence compete**: Strong fluorescence background can overwhelm Raman signal (Raman cross-sections are ~10^-30 cm^2/molecule; fluorescence ~10^-16 cm^2/molecule). Solutions: use longer wavelength (785nm or 1064nm) to avoid fluorescence excitation; use time-gating (Raman is instantaneous, fluorescence is ns-delayed); use SERS to boost Raman 10^6x.

**FTIR is for bulk IR, not imaging**: Standard FTIR uses a single detector and characterizes bulk samples. IR imaging requires either IR microscope (focusing IR onto small area) or FPA (focal plane array) detector with a microscope objective. FTIR imaging exists but is much more expensive.

**ICP-MS measures elemental mass, not molecular structure**: ICP destroys molecular structure completely. You get elemental composition (which elements, at what concentrations) but NOT molecular identity. For molecular mass spectrometry (drug identification, proteomics), you need different ionization methods (ESI, MALDI) that preserve molecular integrity.

**Fluorescence quantum yield is not the same as sensitivity**: High QY means efficient emission, but sensitivity also depends on absorption cross-section, background, and detector. Some high-QY dyes absorb weakly -> still dim. Sensitivity requires both high epsilon (strong absorption) and high QY.

**Fraunhofer lines are absorption, not emission gaps**: The dark lines in the solar spectrum are NOT gaps in the sun's emission. They are absorption by cooler atoms in the solar atmosphere overlying the photosphere. The photosphere emits a continuous blackbody spectrum; the chromosphere absorbs specific wavelengths. This is Kirchhoff's third law.
