# Laser Physics

## The Big Picture

A laser is a feedback oscillator for light — identical in architectural concept to an RF oscillator or a software PID loop, just operating at 10^14 Hz instead of MHz or Hz. The conditions for oscillation are: gain > loss, and the round-trip phase is a multiple of 2pi. What makes lasers distinctive is the *coherent amplification* mechanism: stimulated emission.

```
+------------------------------------------------------------------+
|                      LASER ARCHITECTURE                          |
|                                                                  |
|  GAIN MEDIUM          PUMP               OPTICAL CAVITY          |
|  ----------           ----               ---------------         |
|  Atoms/molecules/     Converts external  Mirrors providing       |
|  semiconductors       energy to          feedback + mode         |
|  with population      population         selection               |
|  inversion            inversion                                  |
|                                                                  |
|  Active medium <-- pump from energy source                       |
|  Energy source: electrical, optical, or thermal                  |
|  Cavity: M1 (R=1.0)  --->  gain medium  --->  M2 (R=0.98)        |
|  Photons bounce M1 <-> M2 on round-trip; small leakage at M2     |
|  becomes the laser output beam.                                  |
|                                                                  |
|  Threshold condition: round-trip gain = round-trip loss          |
|  g(nu) * 2L >= alpha_loss + ln(1/(R1*R2)) / (2L)                 |
+------------------------------------------------------------------+
```

---

## Einstein Coefficients — The Quantum Foundation

Einstein derived three interaction processes between light and a two-level atom (upper state |2>, lower state |1>):

```
  Process             Rate                    Description
  -------             ----                    -----------
  Absorption          R_12 = B12 * rho * N1   Atom absorbs photon, goes up
  Spontaneous emit.   R_21 = A21 * N2         Atom emits random photon, goes down
  Stimulated emit.    R_stim = B21 * rho * N2 Photon triggers identical copy

  rho = photon energy density at frequency nu
  N1, N2 = population densities in states |1> and |2>
  A21 = Einstein A coefficient (spontaneous emission rate)
  B12 = B21 = Einstein B coefficient (proportional to A21)

  Key ratios:
  A21 / B21 = 8*pi*h*nu^3 / c^3

  At frequency nu:
  - Spontaneous rate grows as nu^3 -> harder to make X-ray lasers
  - Stimulated rate independent of nu -> visible lasers efficient

  Why stimulated emission is the magic:
  Stimulated photon is IDENTICAL to trigger photon:
    - Same frequency
    - Same phase
    - Same polarization
    - Same direction
  This is coherent amplification. The copied photon adds in phase.
  In contrast, spontaneous emission goes in random directions and phases.
```

---

## Population Inversion

Thermal equilibrium population follows Boltzmann:

```
  N2/N1 = exp(-(E2-E1) / kT)

  At any positive temperature: N2 < N1 (lower state always more populated)
  -> absorption always dominates over stimulated emission
  -> no net gain -> can't lase with just two levels

  Need POPULATION INVERSION: N2 > N1 (more atoms in upper state)
  This is NOT a thermal equilibrium state -- it requires pumping

  Two-level system: IMPOSSIBLE to invert
    - Pump drives N1 -> N2, but stimulated emission also drives N2 -> N1
    - At best: N1 = N2 (transparent, not amplifying)
    - Saturation prevents inversion
```

### Three-Level Laser (Ruby, early lasers)

```
  +--------+ Level 3 (fast decay)
      |      <- pump absorbs here (fast, broad)
      | fast
      v
  +--------+ Level 2 (metastable, long lifetime = laser upper level)
      |      <- STIMULATED EMISSION happens here (laser transition)
      |      <- Level 2 lifetime ~ms (for ruby), >> thermal relaxation
      v
  +--------+ Level 1 (ground state = lower laser level)

  Problem: lower laser level is the ground state, which is always populated.
  Must pump MORE than half the atoms to get inversion -> high pump threshold.
  Ruby laser: requires very intense flashlamp pumping.
```

### Four-Level Laser (Nd:YAG, HeNe, most practical lasers)

```
  +--------+ Level 4 (fast decay from pump absorption)
      |
      | fast (~ps)
      v
  +--------+ Level 3 (metastable, upper laser level)
      |
      | stimulated emission at laser wavelength
      v
  +--------+ Level 2 (lower laser level, rapidly depopulated)
      |
      | fast (~ps)
      v
  +--------+ Level 1 (ground state)

  Advantage: lower laser level (2) is quickly emptied -> always empty.
  Any pump-excited population in level 3 -> inversion maintained.
  Much lower threshold than three-level systems.
  Nd:YAG: transitions at 1064nm (main), 1319nm, 946nm.
  HeNe: lower level actively depopulated by collisions with tube walls.
```

---

## Optical Cavities

### Longitudinal Modes

The cavity selects frequencies where a standing wave fits:

```
  Condition: 2 * n * L = m * lambda  (m = integer, mode number)

  In frequency:
  nu_m = m * c / (2*n*L)

  Mode spacing (Free Spectral Range):
  Delta_nu = c / (2*n*L)

  Example: HeNe laser, L = 30cm, n=1:
  Delta_nu = 3e8 / (2 * 0.3) = 500 MHz

  The gain medium has a gain bandwidth (determined by atomic linewidth):
  - Homogeneous broadening: all atoms same frequency (Lorentzian shape)
  - Inhomogeneous broadening: different atoms at different frequencies
    (Doppler broadening in gas lasers is Gaussian; typical width 1-5 GHz)

  Number of modes within gain bandwidth:
  N_modes ~ Gain bandwidth / FSR
  HeNe example: 1.5 GHz / 500 MHz ~ 3 modes (typically 1-3 modes lase)
```

### Transverse Modes (TEM Modes)

```
  Cavity with finite aperture supports transverse modes:
  TEM_mn (Transverse Electromagnetic, mode indices m, n)

  TEM_00 : Gaussian beam (lowest order, preferred for most applications)
           Single central lobe, no zeros
           Diffraction-limited divergence
           Beam quality factor M^2 = 1 (ideal)

  TEM_01 : Donut mode (two lobes, azimuthal)
  TEM_10 : Two lobes, horizontal split
  TEM_11 : Four lobes (2x2 grid)
  Higher modes: larger, more complex patterns, larger divergence

  M^2 quality factor:
  M^2 = beam_parameter_product / (lambda/pi)
  M^2 = 1: diffraction-limited Gaussian (ideal)
  M^2 > 1: beam diverges faster than ideal Gaussian
  High-power fiber lasers: M^2 ~ 1.1-1.2
  Multimode diode bar: M^2 ~ 10-100 (fast axis) x 1000+ (slow axis)
```

### Cavity Stability Criterion

Using ABCD matrices, the cavity is stable when the round-trip matrix eigenvalue has magnitude <= 1:

```
  Round-trip ABCD matrix: M = M_mirror2 * M_propagation * M_mirror1 * M_propagation

  Stability condition:
  -1 <= (A+D)/2 <= +1

  Equivalently (for symmetric two-mirror cavity with mirror ROC = R, length = L):
  0 <= (1 - L/R1)(1 - L/R2) <= 1   [g1 and g2 stability parameters]
  g1 = 1 - L/R1,  g2 = 1 - L/R2

  Stable configurations:
    Plane-plane (R1 = R2 = inf): g1=g2=1, marginally stable (sensitive to misalignment)
    Concentric (R1=R2=L/2): g1=g2=-1, marginally stable (opposite extreme)
    Hemispherical (R1=L, R2=inf): g1=0, g2=1, stable and practical
    Confocal (R1=R2=L): g1=g2=0, center of stability diagram

  Bridge: this is exactly the stability analysis of a feedback loop --
  the round-trip matrix is the loop transfer matrix, and the eigenvalue
  condition is the Nyquist stability criterion for optical resonators.
```

---

## Gaussian Beam Propagation

The fundamental TEM_00 mode has a Gaussian intensity profile. Key parameters:

```
  Intensity profile (at waist location z=0):
  I(r, z) = I0 * [w0/w(z)]^2 * exp(-2*r^2 / w(z)^2)

  Beam radius w(z):
  w(z) = w0 * sqrt(1 + (z/z_R)^2)

  Rayleigh range: z_R = pi * w0^2 / lambda
    = distance from waist where beam radius = sqrt(2) * w0
    = depth of focus (distance over which beam is "focused")

  Divergence half-angle (far field):
  theta = lambda / (pi * w0)    [radians, small angle]
  -> Smaller waist = larger divergence (Fourier uncertainty)

  Beam parameter product (BPP):
  BPP = w0 * theta = lambda / pi    [for ideal M^2=1 beam]

  M^2 factor:
  Real beam: BPP_real = M^2 * lambda/pi
  M^2 = 1: ideal; M^2 > 1: non-ideal (multimode, aberrated)

  Example: 1064nm Nd:YAG, w0 = 1mm:
  z_R = pi * (1mm)^2 / 1064nm = 2.96m
  theta = 1064nm / (pi * 1mm) = 0.34 mrad = 0.019 deg
```

---

## Laser Types Survey

```
+------------------------------------------------------------------+
|  LASER TYPE   WAVELENGTH  OUTPUT       KEY APPLICATION           |
|  ----------   ----------  ------       ---------------           |
|                                                                  |
|  SOLID-STATE                                                     |
|  Nd:YAG       1064nm      CW/pulsed    Industrial, medical,      |
|  (Nd:glass)               multi-W to  pumping other lasers       |
|               532nm       kW with      532nm via SHG (green)     |
|               355nm       harmonics    355nm UV via THG          |
|                                                                  |
|  Ti:sapphire  650-1100nm  Tunable CW,  Ultrafast science,        |
|  (Ti:Al2O3)               modelocked   spectroscopy, STED micro  |
|               (pump with  fs pulses    Pulse: 10-100 fs          |
|               532nm Nd)                                          |
|                                                                  |
|  Er:YAG       2940nm      Pulsed       Dental/medical (water     |
|                                        absorbs strongly here)    |
|                                                                  |
|  GAS                                                             |
|  HeNe         632.8nm     CW, mW       Alignment, holography,    |
|               1152nm      low power    laser pointers (historic) |
|               3390nm                   Single freq, long l_c     |
|                                                                  |
|  CO2          10.6um      CW/pulsed    Cutting, welding,         |
|               9.6um       W to kW      marking, surgery          |
|                                        Highest power CW lasers   |
|                                                                  |
|  Excimer      193nm (ArF) Pulsed       Photolithography (Intel   |
|  (rare gas +  248nm (KrF) high energy  7nm node: EUVL at 13.5nm) |
|  halide)      308nm (XeCl) per pulse   LASIK eye surgery (193nm) |
|                                                                  |
|  SEMICONDUCTOR                                                   |
|  Diode laser  780nm       mW to W      CD/DVD, telecom,          |
|  (edge emit)  808nm       single mode  pumping solid-state,      |
|               980nm       to 10W bars  LiDAR, sensing            |
|               1310nm                                             |
|               1550nm                                             |
|                                                                  |
|  VCSEL        850nm       mW,          Short-reach fiber links,  |
|  (Vertical    940nm       fast mod     face ID sensors (iPhone), |
|  cavity SE)   1310nm      >10 GHz      LiDAR arrays              |
|                                                                  |
|  FIBER                                                           |
|  Er-doped     1550nm      1W to kW     Long-haul fiber amp,      |
|  fiber laser  (EDFA       (CW)         high-power industrial,    |
|               amplifier)               coherent comms            |
|  Yb-doped     1030-1120nm             Industrial cutting/weld    |
|  fiber laser              to 100kW    Best beam quality at power |
+------------------------------------------------------------------+
```

---

## Q-Switching and Mode-Locking

### Q-Switching (Short Pulses, High Peak Power)

```
  Normal cavity: Q = omega * (stored energy) / (power loss)
  High Q cavity -> narrow linewidth -> stores energy -> lases efficiently

  Q-switch operation:
  1. Insert high-loss element (Q-spoiler): Q is LOW
  2. Keep pumping: population inversion builds up (can't lase, too much loss)
  3. Suddenly switch to HIGH Q: now gain >> loss
  4. All stored inversion releases in a single short intense pulse

  Pulse width: nanoseconds (cavity round-trip time scale)
  Peak power: 10^6 x CW average power (pulse compression by ~1 million)

  Q-switch methods:
    Acousto-optic (AOM): fast, external RF signal, rep rate flexible
    Electro-optic (EOM/Pockels cell): fastest, kV switching required
    Passive (saturable absorber): crystal or film bleaches at high intensity

  Bridge: Q-switching is analogous to a pipeline stall-and-release:
  fill the pipeline (gain medium) while blocking output, then open
  the floodgates. The capacitor-discharge analogy from circuits works too.
```

### Mode-Locking (Ultrashort Pulses, Femtosecond Scale)

```
  N longitudinal modes with fixed phase relationship:
  When N modes are locked in phase, they sum coherently -> short pulse

  Pulse width:  tau_p ~ 1 / Delta_nu_gain  (Fourier limit)
  Repetition rate = c / (2L)   (FSR of cavity)

  Example: Ti:sapphire, gain bandwidth = 120THz, L = 1.5m:
  tau_p ~ 1/120THz = 8 fs  (femtosecond)
  Rep rate = 3e8/(2*1.5) = 100 MHz (10ns spacing)

  Mode-locking methods:
    Active: acousto-optic modulator at cavity FSR frequency
    Passive: saturable absorber (SESAM -- semiconductor saturable
             absorber mirror; bleaches at high intensity, shorter pulses survive)
    Kerr lens mode-locking (KLM): Kerr effect in Ti:sapphire itself;
      high intensity -> self-focusing -> selects for pulsed operation
      (Kerr lens has higher transmission for pulsed than CW mode)

  Chirped Pulse Amplification (CPA, Nobel 2018 -- Mourou & Strickland):
  Problem: amplifying fs pulses to high energy -- intensity in gain
  medium destroys it (GW/cm^2 level).
  Solution:
  1. Generate fs pulse from oscillator
  2. STRETCH in time by chirp (~1000x longer, 10 ps -> 10 ns)
     (diffraction grating or dispersive fiber)
  3. Amplify the stretched pulse safely (now nanosecond, manageable intensity)
  4. RECOMPRESS (reverse grating pair)
  5. Get original fs duration back, but now with amplified energy

  Result: petawatt (10^15 W) peak power lasers
  Applications: ablation physics, electron acceleration, attosecond science
```

---

## Laser Safety

```
  Class     Output power / characteristics    Hazard
  -----     ----------------------------     ------
  Class 1   No hazard (enclosed system)      Safe under all conditions
  Class 1M  Safe without optics              Unsafe with magnifying optics
  Class 2   Visible CW, < 1 mW              Blink reflex sufficient
  Class 2M  Visible, < 1 mW, collimated     Unsafe with optical aids
  Class 3R  < 5 mW (visible), eye hazard    Eye hazard if directly viewed
  Class 3B  < 500 mW                        Direct/specular reflection hazard
  Class 4   > 500 mW (or pulsed equivalent) Diffuse reflection hazard, fire risk

  Maximum permissible exposure (MPE):
  For 633nm CW: MPE = 2.5 mW/cm^2 (skin/eye)
  For pulsed: MPE depends on pulse width, frequency, wavelength

  Near-IR (1064nm, 1550nm) hazards:
  1064nm: NOT absorbed by cornea/aqueous, focuses on retina -- high hazard
  1550nm: absorbed by cornea/aqueous -- lower retinal hazard, higher class
    allowed for eye-safe rangefinders and LiDAR

  The OD (optical density) of safety goggles:
  OD = log10(incident power / transmitted power)
  OD 6 = one million fold attenuation
  Choose OD based on: laser power, wavelength, exposure scenario
```

---

## Decision Cheat Sheet

| I need... | Choose |
|-----------|--------|
| Stable visible alignment beam, cheap | HeNe 633nm |
| High power cutting/welding | CO2 (10.6um) or Yb fiber laser (1070nm) |
| Femtosecond pulses for surgery/science | Mode-locked Ti:sapphire or fiber laser |
| Telecom amplification at 1550nm | Er-doped fiber amplifier (EDFA) |
| High-rep-rate nanosecond pulses | Q-switched Nd:YAG |
| Compact, high-bandwidth modulated source | Semiconductor diode laser |
| Eye-safe LiDAR | 1550nm fiber laser or VCSEL |
| UV photolithography | Excimer (ArF 193nm) or EUVL (13.5nm) |
| Single longitudinal mode, long coherence | Extended-cavity diode laser, stabilized |
| Understanding how a laser cavity works | ABCD round-trip stability, FSR, g-parameters |

---

## Common Confusion Points

**A laser is an oscillator, not an amplifier**: The gain medium is a light amplifier (like an op-amp). The mirrors provide feedback to make it oscillate. "LASER" = Light Amplification by Stimulated Emission of Radiation -- the acronym describes the amplifier, not the oscillator. Both exist: laser amplifiers (like EDFAs) and laser oscillators (what most people mean by "laser").

**Population inversion is not thermal**: You cannot achieve it by heating. It requires active pumping to a specific non-equilibrium state. The pump transfers energy from an external source (electrical, optical) specifically into the upper laser level.

**Four-level is not automatically better than three-level**: Four-level lasers have lower threshold and operate more efficiently. But the lower laser level must decay fast. If it doesn't (e.g., accumulates population), it becomes a three-level problem. Design and thermal management matter.

**Mode-locking generates frequency combs**: A phase-locked mode-locked laser produces a frequency comb -- a series of equally spaced frequencies in the frequency domain. These are the basis of optical frequency standards (Nobel 2005 to Hall & Hansch) and are now used for molecular fingerprinting, metrology, and as optical "rulers."

**M^2 = 1 does not mean the beam is perfect for all applications**: M^2 = 1 means the beam is a Gaussian TEM_00 mode. This is the best you can do for focusing to a diffraction-limited spot. But for uniform illumination, power delivery to a large area, or other geometries, you might deliberately use multi-mode beams.

**Laser threshold is not a sharp on/off**: Below threshold, the laser acts as an amplified spontaneous emission (ASE) source -- dim, incoherent, broadband. At threshold, coherent lasing begins. The transition is a phase transition-like behavior (photon number goes from noise to coherent buildup).
