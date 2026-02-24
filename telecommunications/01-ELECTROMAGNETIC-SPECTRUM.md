# Electromagnetic Spectrum — A Layered Guide

## The Big Picture

The EM spectrum is a physical resource. Each frequency band has unique propagation
characteristics that determine what it's useful for.

```
EM SPECTRUM — TELECOMMUNICATIONS BANDS
════════════════════════════════════════════════════════════════════

ITU  Freq      Wavelength  Propagation          Primary Uses
Band Range                 Mechanism
─────────────────────────────────────────────────────────────────────
ELF  3-30 Hz   100Mm-10Mm  Ground wave          Submarine comm (USN ELF)
SLF  30-300Hz  10Mm-1Mm    Ground wave          Submarine comm (Russia)
ULF  300Hz-3kHz 1Mm-100km  Ground wave          Mine comm, natural sources
VLF  3-30 kHz  100km-10km  Ground wave          OMEGA nav (retired), military
LF   30-300kHz 10km-1km    Ground wave          AM long wave, LORAN-C, DECCA
MF   0.3-3MHz  1km-100m    Ground + Sky wave    AM broadcast (530-1700 kHz)
HF   3-30MHz   100m-10m    Sky wave (ionosphere) Shortwave, amateur, military
VHF  30-300MHz 10m-1m      Line-of-sight (LoS)  FM radio (88-108 MHz), VHF TV
UHF  0.3-3GHz  1m-10cm     LoS + diffraction    Cellular, WiFi, GPS, UHF TV
SHF  3-30GHz   10cm-1cm    LoS, rain sensitive  5G, satellite, point-to-point
EHF  30-300GHz 1cm-1mm     LoS, strong attn     5G mmWave, 60 GHz, automotive radar
THF  300GHz+   <1mm        Experimental         THz imaging, spectroscopy
─────────────────────────────────────────────────────────────────────
```

---

## Propagation Mechanisms

```
THREE MAIN PROPAGATION MODES

1. GROUND WAVE (LF/MF):
   Wave follows earth's curvature via diffraction
   Range: hundreds of km for LF, tens of km for MF
   Attenuation: increases with frequency and distance
   Penetrates well into sea water (why submarines use ELF/VLF)

2. SKY WAVE (HF ionospheric):
   Wave bounces off ionosphere → beyond-horizon propagation
   Range: 100–3000 km (F-layer refraction)
   Ionosphere layers: D (60-90 km), E (90-140 km), F1/F2 (140-300+ km)
   Varies with: solar activity, time of day, season, sunspot cycle
   Maximum usable frequency (MUF): highest HF freq that can reach target via sky wave
   Critical frequency: highest freq reflected back at vertical incidence

3. LINE-OF-SIGHT (VHF/UHF/SHF/EHF):
   Direct path; blocked by obstacles
   Range: limited by earth's curvature + antenna height
   LoS range: d ≈ 4.12·(√h_T + √h_R) km  (h in meters, "radio horizon")
   For h_T = h_R = 100m: d ≈ 82 km
   Augmented by slight refraction (effective earth radius factor k ≈ 4/3)

MULTIPATH FADING (UHF/SHF):
Multiple reflections arrive with different delays → constructive or destructive interference
→ rapid amplitude fluctuations as mobile moves (Rayleigh fading at high Doppler)
→ frequency-selective fading when delay spread > symbol period
OFDM is designed specifically to handle frequency-selective fading
```

---

## Free-Space Path Loss (FSPL)

The minimum signal loss in open air between isotropic antennas:

```
FREE SPACE PATH LOSS:

FSPL = (4πd/λ)² = (4πdf/c)²

In dB:
FSPL(dB) = 20·log₁₀(d) + 20·log₁₀(f) + 20·log₁₀(4π/c)
          = 20·log₁₀(d_km) + 20·log₁₀(f_MHz) + 32.45  dB

EXAMPLES:
Cellular (900 MHz, 1 km):   32.45 + 20 + 59.1 = 91.6 dB
Cellular (1800 MHz, 1 km):  32.45 + 20 + 65.1 = 97.6 dB  (+6 dB for 2× freq)
Satellite (Ku 12 GHz, 36000 km): 32.45 + 91.1 + 141.6 = 205 dB!
WiFi (2.4 GHz, 100m):        32.45 + 40 + 67.6 = 80 dB

Key: FSPL increases +20 dB per decade of distance and +20 dB per decade of frequency.
Double the distance → 4× power loss (−6 dB).
Double the frequency → 4× power loss (−6 dB) for same physical aperture antenna.
```

---

## Atmospheric Absorption

Beyond FSPL, absorption in atmosphere limits high-frequency links.

```
ATMOSPHERIC ABSORPTION vs FREQUENCY

Attenuation
(dB/km)
│
10  ─────────────────────────────────────────────── 60 GHz O₂ peak (~15 dB/km)
    │
 1  ─                                            ╱ 183 GHz H₂O
    │                              ╱                 22 GHz H₂O peak
    │                          ╱
0.1 ─               ╱─────────                  30 GHz: ~0.1 dB/km
    │           ╱─╱
    │         ╱
0.01 ─  ╱─────
    │ ╱  < 10 GHz: < 0.01 dB/km
    └──────────────────────────────────────────────────────► frequency
    1     10    30  60   100  183  300 GHz

ABSORPTION PEAKS:
22 GHz: Water vapor resonance (0.2 dB/km at sea level)
60 GHz: Oxygen absorption (13–15 dB/km) — prevents eavesdropping → 802.11ad/WiGig uses this
183 GHz: Strong water vapor resonance

RAIN FADE (> 10 GHz):
Rain attenuation ≈ k · R^α  dB/km  (R = rain rate mm/hr)
At 12 GHz: 0.01 dB/km per mm/hr rain (moderate impact)
At 30 GHz: ~0.1 dB/km per mm/hr (significant for satellite links)
At 60 GHz: ~0.5 dB/km per mm/hr (rain fade is major concern)

RAIN MARGIN: satellite links at Ka-band (26.5-40 GHz) must budget 3-10+ dB rain margin
Site diversity (two earth stations, geographically separated) helps
```

---

## Band-by-Band Propagation Characteristics

```
HF (3-30 MHz): Sky Wave Details

IONOSPHERIC LAYERS:
  D layer (day): 60-90 km, absorbs MF/lower HF, disappears at night
  E layer: 90-140 km, reflects some HF, sporadic E unpredictable
  F1/F2 (daytime): merge to F layer at night, 200-400 km
  F layer: primary HF reflection, usable for 1000s of km

MUF (Maximum Usable Frequency):
  Depends on ionospheric electron density (varies with solar cycle)
  Solar max → higher MUF (~30 MHz); solar min → lower MUF
  MUF for 3000 km path: typically 8-20 MHz (day), 5-12 MHz (night)

HF SKIP ZONE:
  Ground wave dies beyond ~500 km; sky wave "skip distance" (first hop) is 500-1500 km
  Between: radio blackout (no coverage)
  Long range: multiple hops (two bounces: 6000 km)
```

```
VHF/UHF (30 MHz – 3 GHz): Line-of-Sight and Beyond

KNIFE-EDGE DIFFRACTION:
  Sound diffracts around hills/buildings (VHF: partial coverage beyond obstacles)
  Attenuation = 6 dB for tangential path over ridge → augments LoS range

TROPOSCATTER:
  Turbulent troposphere scatters energy (40-4000 MHz)
  Extends range to 100-1000 km with high transmit power
  Used for: military communications over horizon, pipeline monitoring

DUCTING (temperature inversion):
  Normally: temperature decreases with altitude
  Inversion: creates duct that traps and guides VHF/UHF signals
  Effect: can extend range to 1000+ km (interference problem for broadcasters)
```

---

## Link Budget

A link budget accounts for all gains and losses between transmitter and receiver.

```
LINK BUDGET COMPONENTS

Transmitted power:     Pt  = +33 dBm (2W typical cellular)
Tx antenna gain:       Gt  = +15 dBi (sector antenna)
Free-space path loss:  FSPL = -120 dB (900 MHz, 5 km)
Building penetration:  L_b  = -15 dB (indoor)
Rx antenna gain:       Gr   = +0 dBi (phone)
────────────────────────────────────────────────────────
Received power:        Pr  = 33 + 15 - 120 - 15 + 0 = -87 dBm

Noise floor:
  Thermal noise density: N₀ = -174 dBm/Hz (kT at 300K)
  Bandwidth: B = 20 MHz → noise power = -174 + 10·log₁₀(20×10⁶) = -101 dBm
  Receiver noise figure: NF = 7 dB
  Noise floor = -101 + 7 = -94 dBm

SNR = Pr - Noise_floor = -87 - (-94) = 7 dB
Required SNR for QPSK at BER 10⁻³: ~7 dB ✓ (just barely works)
Required SNR for 64-QAM: ~22 dB ✗ (need to be closer to tower)

LINK MARGIN: Extra SNR above minimum required.
Typically design for 10-20 dB margin to handle fading, shadowing.
```

---

## Decision Cheat Sheet

| Application | Frequency Band | Why |
|-------------|----------------|-----|
| Over-the-horizon communications | HF (3-30 MHz) | Sky wave reflection |
| AM broadcast (hundreds of km) | MF (550-1700 kHz) | Ground wave |
| FM radio (local) | VHF (88-108 MHz) | LoS, good coverage, wide bandwidth |
| Cellular mobile | UHF (700-2600 MHz) | LoS, penetration, large bandwidth available |
| Fixed point-to-point microwave | SHF (6-11 GHz) | High bandwidth, LoS |
| Satellite (high capacity) | Ku/Ka (12-40 GHz) | High bandwidth, manageable FSPL |
| Short-range high-speed (indoor) | 60 GHz | High bandwidth, oxygen absorption limits interference |
| Submarine communication | ELF/VLF | Penetrates seawater |

---

## Common Confusion Points

**dBi vs dBd**: Antenna gain in dBi = gain relative to isotropic antenna (equal in all directions).
dBd = gain relative to a half-wave dipole (+2.15 dBi). When manufacturers say "6 dBi" they mean
the antenna focuses the signal 4× relative to isotropic — it doesn't add power, just directs it.

**FSPL is not all the path loss**: FSPL assumes free space. Real links add: building penetration,
foliage, rain, reflection/absorption by ground (for low antennas), shadowing. FSPL is the minimum.

**Higher frequency ≠ more "powerful" signal**: Higher frequency means shorter wavelength, which
means smaller effective antenna aperture for the same physical size, hence more FSPL per km.
To compensate, higher-frequency systems use higher-gain antennas (which have narrower beams —
requires pointing accuracy).

**HF "skip zone" is a coverage gap, not a design feature**: There's a dead zone between the end
of ground wave range and the start of sky wave coverage. Emergency HF systems may have blackouts.
Some systems use near-vertical incidence sky wave (NVIS) to fill the skip zone (10-12 MHz,
very high elevation angle).
