# Photonic Devices

## The Big Picture

Photonic devices are the optics equivalent of electronic components: converters between the photon domain and the electron domain, sources, detectors, and signal-processing elements. The field is stratified by whether the device is active (requires power, performs gain or modulation) or passive (routes and shapes light without power):

```
+------------------------------------------------------------------+
|                     PHOTONIC DEVICE LANDSCAPE                    |
|                                                                  |
|  SOURCES              DETECTORS         MODULATORS               |
|  -------              ---------         ----------               |
|  Laser diodes         Photodiodes       Pockels/EO cell          |
|  VCSELs               APDs              Mach-Zehnder mod         |
|  LEDs                 SPADs             Ring resonator mod       |
|  Fiber lasers         PMTs              Acousto-optic mod (AOM)  |
|                       Bolometers        Electro-absorption mod   |
|                       (thermal, IR)                              |
|                                                                  |
|  PASSIVE WAVEGUIDE    PHOTONIC CRYSTALS  FLAT OPTICS             |
|  ----------------     ----------------  ----------               |
|  Optical fiber        PhC bandgap        Metasurfaces            |
|  SOI waveguides        structures        Metalenses              |
|  Arrayed waveguide    Defect modes       Diffractive lenses      |
|  gratings (AWG)       PC fibers                                  |
+------------------------------------------------------------------+
```

---

## Photodetectors

### PIN Photodiode

The workhorse detector for optical communications and instrumentation:

```
  Structure:
  p+ | intrinsic (I-layer) | n+

  Operation:
  1. Photon absorbed in I-layer (or p/n regions)
  2. Electron-hole pair created (E_photon > E_bandgap)
  3. Electric field (reverse bias) sweeps carriers apart
  4. Current flows in external circuit

  +--------+       +--------+
  |   p+   |  I   |   n+   |  <-- structure
  +--------+-------+--------+
              ^
              photon absorbed here (thick I-layer for high QE)

  Key parameters:
    Responsivity R = I_photocurrent / P_optical  [A/W]
    R = (e * QE) / (h * nu) = (e * lambda * QE) / (h * c)

    At 1550nm: R = 1.24 * QE  [A/W]  (where QE = quantum efficiency 0 to 1)
    InGaAs photodiode at 1550nm: R ~ 0.9 A/W (QE ~ 0.72)
    Silicon at 850nm: R ~ 0.6 A/W

    Bandwidth: limited by carrier transit time and RC time constant
    Transit time limit: f_3dB ~ 0.45 * v_sat / d  (d = I-layer thickness)
    RC limit: f_3dB = 1 / (2*pi*R*C)

    Trade-off: thick I-layer -> high QE, slow; thin I-layer -> fast, lower QE

    Dark current: reverse leakage current without illumination
    Sets noise floor; increases with temperature; T doubles for ~10 deg C rise
```

### Avalanche Photodiode (APD)

```
  Like a PIN diode, but operated at high reverse bias (near breakdown):

  Photogenerated carrier + high E-field -> impact ionization
  -> secondary electron-hole pairs -> multiplication (gain M)

  Gain: M = 1 / (1 - (V/V_br)^n)   (V_br = breakdown voltage)
  Typical M: 10-100 for linear mode APD
  Excess noise factor: F(M) = M^x  (x = 0.2-0.7 for silicon, worse for InGaAs)

  Signal-to-noise improvement:
  SNR with APD vs PIN: improved only if M^2 * F < M^2, i.e., if x < 1
  In practice: APDs better than PINs at low light levels where shot noise dominates

  Applications: long-haul fiber receivers (before coherent comms became practical),
  LiDAR, barcode scanners, photon-counting applications

  Geiger mode (SPAD):
  Bias above breakdown. Single photon triggers an avalanche cascade:
  -> large detectable current pulse from single photon
  -> must quench (reset) after each detection (dead time 20-100ns)
  -> used in LiDAR, quantum cryptography, PET scanners (SPAD arrays)
```

### Detector Comparison

```
+------------------------------------------------------------------+
|  DETECTOR     WAVELENGTH  GAIN   NOTES                           |
|  --------     ----------  ----   -----                           |
|  Silicon PIN  350-1100nm  1      Cheap, fast, large area         |
|  InGaAs PIN   900-1700nm  1      Telecom, NIR                    |
|  Ge PIN       800-1800nm  1      Low cost NIR                    |
|  Si APD       400-1000nm  10-100 Low noise, photon counting      |
|  InGaAs APD   900-1700nm  10-40  Telecom, higher noise than Si   |
|  Si SPAD      400-1000nm  10^6   Single photon, dead time        |
|  PMT          200-800nm   10^6   Ultra-sensitive, fragile, bulky|
|  Bolometer    1um-1mm     1      IR/THz uncooled thermal         |
|  HgCdTe (MCT) 3-12um      varies Cooled IR, highest performance|
+------------------------------------------------------------------+
```

---

## Light-Emitting Diodes (LEDs)

### Recombination Physics

```
  In a direct-bandgap semiconductor (GaAs, InGaAs, GaN):
  Conduction band electron + valence band hole -> photon + phonon (small)
  E_photon ~ E_bandgap  (emission wavelength = hc / E_g)

  In an indirect-bandgap semiconductor (Silicon, Germanium):
  Conduction band minimum and valence band maximum at different k-vectors
  Recombination requires phonon participation -> very low radiative efficiency
  -> Silicon cannot be a practical LED or laser (must use external structure)

  LED structure: forward-biased p-n junction (or p-i-n)
  Injection of minority carriers -> recombination in active region
```

### LED Efficiency

```
  Wall-plug efficiency = electrical power in / optical power out

  Chain:
  Injection efficiency: fraction of carriers that reach active region
  Radiative efficiency: fraction of recombinations that emit photons (vs phonons)
  Extraction efficiency: fraction of photons that escape the chip

  Extraction is the hardest:
  Critical angle for TIR: theta_c = arcsin(1/n)  (GaN: n=2.5, theta_c=23.6 deg)
  -> Most photons hit the surface > theta_c -> TIR -> reabsorbed
  Without engineering: extraction efficiency ~ 4% (sphere: 1/(4n^2))

  Solutions: roughened surfaces, photonic crystal top surface,
             flip-chip (light out through substrate), shaped dies

  Modern power LEDs: wall-plug efficiency up to 80% (blue GaN)
  "Efficiency droop": efficiency falls at high current density (hot carriers, Auger)

  White LEDs:
  Blue LED (InGaN, 450nm) + yellow phosphor (YAG:Ce) -> white
  Phosphor absorbs blue, re-emits broad yellow/green -> mixes with blue residual
  CRI (Color Rendering Index): 80-95 for good phosphors (100 = sunlight)
  Color temperature: 2700K (warm) to 6500K (cool daylight)
```

---

## Optical Modulators

### Electro-Optic (Pockels) Effect

```
  Applied electric field changes refractive index:
  Delta_n = -(1/2) * n^3 * r * E   (linear/Pockels effect)

  r = electro-optic coefficient (r_33 for LiNbO3: 31 pm/V)
  E = applied electric field

  Phase shift: Delta_phi = (2*pi/lambda) * Delta_n * L
             = (pi * n^3 * r * V) / (lambda * d)  (d = electrode gap)

  Half-wave voltage V_pi: voltage to achieve Delta_phi = pi
  V_pi = lambda * d / (n^3 * r * L)
  LiNbO3 bulk modulator: V_pi ~ 5V (for 10mm crystal, 1550nm)
```

### Mach-Zehnder Modulator (MZM)

The dominant modulator for high-speed optical communications:

```
  Input waveguide
        |
        +---- arm 1 (EO phase shift phi_1) ----+
        |                                       | -> output
        +---- arm 2 (EO phase shift phi_2) ----+

  Output intensity:
  I_out = I_in * cos^2((phi_1 - phi_2) / 2)
        = (I_in / 2) * (1 + cos(Delta_phi))

  Quadrature bias: operate at Delta_phi = pi/2 for linear modulation
  At quadrature: small delta_phi -> linear change in I_out

  ON state: Delta_phi = 0   -> I_out = I_in
  OFF state: Delta_phi = pi -> I_out = 0   (extinction ratio)

  Key specs:
    Bandwidth: 10-100 GHz for LiNbO3; up to 50+ GHz for InP/SiPh
    Vpi: 1-5V for LiNbO3 (shorter device = higher Vpi)
    Extinction ratio: 20-30 dB typical (limited by arm imbalance)
    Insertion loss: 3-6 dB

  Bridge: This is exactly a Mach-Zehnder interferometer with voltage-controlled
  phase rather than mechanically-scanned path length. The voltage-to-intensity
  transfer function is the same cos^2 you saw in interference.
```

### Silicon Photonic Ring Resonator Modulator

```
  Compact (5-10 um radius) resonant structure:
  - Light circulates in ring; on-resonance: couples out of bus waveguide (dark)
  - Off-resonance: light passes through bus waveguide unaffected (bright)
  - Free carrier injection/depletion: shifts resonant wavelength slightly

  Modulation: shift resonance wavelength by ~0.1-0.2nm -> on/off switching
  Speed: 10-50 Gbaud achievable
  Size: ~100um^2 vs ~cm^2 for LiNbO3 MZM
  Temperature sensitivity: ~0.1 nm/deg C -- must be thermally stabilized
  Bandwidth: narrow (finesse-limited) -- works only at one wavelength

  Used in: Intel's silicon photonic transceivers (400G, 800G)
  Azure data center optical interconnects use exactly these devices
```

---

## Photonic Integrated Circuits (PICs)

### Silicon Photonics Platform

```
  Silicon-on-insulator (SOI) wafer:
  +--Si device layer (220nm) --+
  +--SiO2 buried oxide (2um) --+   <- waveguide cladding (n=1.45)
  +--Si substrate (750um)------+

  Si core: n = 3.48 at 1550nm
  SiO2 cladding: n = 1.45
  Delta_n = 2.03 -> very high confinement, tight bends (R > 5um)

  SOI platform components:
  +--wavelength--+   +--active--+   +--coupling--+
  | Waveguides   |   | Laser*   |   | Grating    |
  | Ring res.    |   | Modulator|   | coupler    |
  | AWG          |   | Detector |   | Lensed     |
  | Filters      |   | Amplifier|   | fiber      |
  +--routing--+  +--other--+
  | Splitters |  | Heaters  |
  | Couplers  |  | (phase)  |

  *Silicon cannot lase -- laser is external (III-V bonded, or fiber pigtail)
  Challenge: heterogeneous integration of GaAs/InP lasers on Si wafers

  InP platform:
  - Native laser and detector capability
  - Higher insertion loss waveguides than Si
  - Used for coherent 400G/800G transceivers (QAM modulation requires coherent detection)
```

### Wavelength Division Multiplexing (WDM)

```
  Arrayed Waveguide Grating (AWG):
  - Passive waveguide structure on chip
  - Functions as a wavelength demultiplexer/multiplexer
  - 40+ channels on 100GHz or 50GHz ITU grid
  - Key element in DWDM systems

  Principle: free propagation regions + phased array of waveguides
  -> different wavelengths arrive at different output ports (grating-like)

  DWDM (Dense WDM): channel spacing 100GHz (0.8nm) or 50GHz (0.4nm)
  C-band: 1530-1565nm (~45nm window, 40-80 channels at 100GHz spacing)
  L-band: 1565-1625nm (additional capacity)
  O-band: 1310nm window (for short-reach, zero-dispersion)

  Azure data center WDM: CWDM4 (4 wavelengths, 20nm spacing) for intra-DC
  Hyperscale long-reach: DWDM at 100GHz+ with coherent detection
```

---

## Optical Fiber

```
  Structure:
  +---core (n_core)---+
  +--cladding (n_clad) -- (n_core > n_clad, TIR guidance)-+
  +--protective coating--+

  Normalized frequency (V number):
  V = (2*pi/lambda) * a * NA = (2*pi/lambda) * a * sqrt(n_core^2 - n_clad^2)

  Single mode condition: V < 2.405
  Step-index SMF at 1550nm: a ~ 4.5um, NA ~ 0.12

  Types:
  +------------------------------------------------------------------+
  |  TYPE              CORE   USE CASE               NA              |
  |  ----              ----   --------               --              |
  |  SM step-index     9um    Long-haul, metro comms 0.12            |
  |  SM dispersion-    9um    Long-haul (DWDM)       0.12            |
  |  shifted (DSF)                                                   |
  |  MM step-index     50um   Short-reach LAN        0.20            |
  |  MM graded-index   50um   Short-reach LAN (OM3/4)0.20            |
  |  (GRIN)                   Lower dispersion                       |
  |  PM (polarization  10um   Fiber sensors, coherent comms          |
  |  maintaining)             interferometry                         |
  |  Large mode area   25+um  High power delivery    small           |
  |  (LMA)                    (fiber lasers)                         |
  +------------------------------------------------------------------+

  Attenuation mechanisms:
  - Rayleigh scattering: ~ 1/lambda^4 -> decreases at longer wavelengths
  - OH absorption: peaks at 1383nm (water in glass) -> avoid this band
  - Infrared absorption: rises beyond 1700nm
  - Minimum: ~0.2 dB/km at 1550nm (Rayleigh tail + IR absorption balance)

  Dispersion in fiber:
  - Material dispersion: dn/dlambda (group velocity varies with wavelength)
  - Waveguide dispersion: mode field distribution changes with wavelength
  - Total: ~17 ps/(nm*km) at 1550nm for standard SMF-28
  - Zero-dispersion wavelength of SMF-28: ~1310nm
  - Dispersion-shifted fiber (DSF): moves zero-dispersion to 1550nm
    BUT: four-wave mixing causes crosstalk in WDM systems at zero-dispersion
  - Non-zero DSF (NZ-DSF, LEAF): small but nonzero dispersion at 1550nm
```

---

## Photonic Crystals and Metamaterials

### Photonic Crystals

```
  Periodic variation in refractive index on wavelength scale.
  Analogy: electronic bandgap from crystal lattice periodicity (Bloch theorem)
           photonic bandgap from optical periodicity (same math)

  1D: alternating layers (thin-film interference -- HR coatings, VCSELs)
  2D: holes in slab (photonic crystal slab waveguides, slow light)
  3D: full 3D periodic (complete bandgap in all directions -- hard to fabricate)

  Photonic bandgap: frequency range where no propagating modes exist.
  Light cannot enter/propagate -> perfect mirror or waveguide confinement.

  Defect modes: remove one period -> localized mode in the gap
  (analogy: dopant atom in semiconductor crystal creates state in gap)
  Applications: ultra-high-Q resonators, PC fiber (hollow core guidance)

  Photonic crystal fiber (PCF):
  Microstructured holey fiber: air holes around solid core (modified TIR guidance)
  Hollow-core PCF: light guided in air core by photonic bandgap
    Ultra-low nonlinearity (air has 1000x less nonlinearity than glass)
    Used for: high-power delivery, gas-phase spectroscopy
```

### Metamaterials and Metasurfaces

```
  Metamaterials: artificial structures with sub-wavelength unit cells
  Effective medium properties determined by structure, not just composition
  Can achieve: n < 0 (negative index), n < 1, epsilon < 0, mu < 0

  Negative index: Snell's law gives negative refraction
  -> "perfect lens" (Pendry 2000): theoretically perfect imaging
     (including evanescent waves -- sub-wavelength features)
     In practice: high loss, narrow bandwidth

  Metasurfaces: 2D array of sub-wavelength antennas/pillars
  Control phase, amplitude, and polarization pixel-by-pixel
  Can implement: lens, prism, beam splitter, polarizer -- flat!

  Metalens: metasurface implementing a lens function
  Phase profile: phi(r) = -k0 * (sqrt(r^2 + f^2) - f)
  Implement via: TiO2 nanopillars, Si nanopillars, resonant antennas
  Diameter: mm to cm demonstrated; f/# as small as 0.5 achieved

  Advantages vs refractive lens:
  - Ultra-thin (< 1um vs mm-cm glass)
  - Compatible with CMOS fab
  - Can correct multiple aberrations simultaneously in a single element

  Limitations:
  - Narrow bandwidth (chromatic aberration severe without special design)
  - Lower efficiency than refractive at present
  - Expensive to fabricate large area
  - Applications: compact cameras, VR/AR optics, computational imaging
```

---

## Decision Cheat Sheet

| I need to... | Choose |
|---|---|
| Detect optical signal at 1550nm, high bandwidth | InGaAs PIN photodiode |
| Detect single photons for LiDAR | Si SPAD (at 850nm) or InGaAs SPAD (at 1550nm) |
| Detect low-level visible light with gain | Si APD (linear mode) |
| Detect broadband IR (thermal imaging) | Bolometer array (uncooled) or MCT (cooled, high sensitivity) |
| Modulate data at 100+ Gbaud for telecom | LiNbO3 MZM or InP MZM |
| Compact modulator in a silicon PIC | Ring resonator modulator |
| Long-haul single-mode fiber | SMF-28 (or low-loss variant, 1550nm) |
| Short-reach data center interconnect | OM4 graded-index MMF + VCSEL at 850nm |
| High-power fiber delivery | Large mode area (LMA) fiber |
| Demultiplex DWDM channels on chip | Arrayed waveguide grating (AWG) |
| Understand why Si can't lase | Indirect bandgap -- requires phonon, low efficiency |
| Compact flat lens for AR/VR | Metalens (TiO2 pillars) |

---

## Common Confusion Points

**Responsivity vs. quantum efficiency**: QE = fraction of photons that generate an electron-hole pair (0 to 1). Responsivity = photocurrent / optical power [A/W]. They are related: R = (e * lambda * QE) / (hc). At 1550nm, R = 1.24 * QE. At 850nm, R = 0.68 * QE. Same QE gives lower responsivity at shorter wavelengths (photons carry more energy).

**APD gain is not free**: The multiplication gain M also multiplies the noise. The excess noise factor F(M) > 1 means the noise grows faster than the signal. The optimum gain for SNR exists and is not "maximum gain." For silicon APDs, the ionization ratio k is small (~0.02), giving low noise; for InGaAs APDs, k ~ 0.4, much noisier.

**Single-mode vs. multimode fiber and bandwidth**: MMF supports thousands of modes, each traveling at slightly different speed (modal dispersion) -> limited bandwidth * length product. SMF eliminates modal dispersion but has chromatic dispersion. For > 100m runs at > 1 Gbps, SMF dominates. For data center rack-to-rack (< 100m), OM4 MMF with VCSEL is cheaper.

**Silicon photonics cannot include a laser**: Si is indirect bandgap. Integration requires bonding or coupling a III-V (InP, GaAs) laser die to the Si chip. This is the main manufacturing challenge for fully monolithic Si PICs. Some companies (Intel, Marvell) bond InP on Si wafer scale; others package discrete III-V lasers with Si PICs.

**Ring resonator temperature sensitivity**: Silicon has a high thermo-optic coefficient (dn/dT = 1.86e-4 /K). A ring resonator resonance shifts ~0.1 nm/K. In a data center (temperature drifts), this requires active thermal stabilization (heater + feedback) -- adding complexity and power consumption. LiNbO3 MZM is much less temperature-sensitive.

**Metamaterial "perfect lens" is practically limited**: Pendry's proposal requires negative-index material with zero loss. All experimental negative-index materials have substantial loss, which destroys the evanescent wave amplification needed for sub-diffraction imaging. The perfect lens remains a theoretical curiosity; metasurface imaging is the practical frontier.
