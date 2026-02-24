# Optical Communications — A Layered Guide

## The Big Picture

Optical fiber carries the vast majority of the world's long-haul data traffic.
A single fiber pair can carry terabits per second across oceans.

```
OPTICAL FIBER COMMUNICATIONS HIERARCHY
════════════════════════════════════════════════════════════════════

Transmitter          Fiber           Optical Amplifiers      Receiver
    │                  │                    │                    │
[Laser source] ──► [SMF cable] ──► [EDFA every 80km] ──► [Coherent Rx] ──► Data
    │              │       │                │                │
  DFB laser       1310 or 1550 nm  Erbium-doped      DSP + ADC
  modulated       C+L band         fiber amplifier   carrier recovery
  up to 100 Gbps  1.5 dB/km       (C-band: 1525-1565nm) polarization recovery
  per wavelength  at 1550 nm      noise figure 5-6 dB  chromatic dispersion
                                                         compensation
                                                         equalization

DWDM: Multiple wavelengths on one fiber
  100 GHz channel spacing: 40 wavelengths in C-band
  50 GHz spacing: 80 wavelengths
  Each wavelength: 100-800 Gbps (with DP-QAM modulation)
  Per-fiber capacity: 10-100 Tbps possible
```

---

## Optical Fiber Physics

```
FIBER CONSTRUCTION

SINGLE-MODE FIBER (SMF):
  ┌─────────────────────────┐
  │    Core (8-10 µm dia)   │  Refractive index n₁
  │       cladding (125 µm) │  Refractive index n₂ < n₁
  │         jacket (250 µm) │  Protective coating
  └─────────────────────────┘

  Single mode: only one propagation mode → no modal dispersion
  Used for: long-distance (metro, long-haul, submarine)

MULTIMODE FIBER (MMF):
  Core diameter: 50 µm (OM3/OM4) or 62.5 µm (OM1/OM2)
  Supports many modes → modal dispersion limits bandwidth × distance
  Used for: short-range LAN (datacenter, up to ~2 km)
  OM3: 10 Gbps up to 300 m; OM5: 40-100 Gbps up to 150 m

TOTAL INTERNAL REFLECTION:
  Light in core (n₁) hitting cladding (n₂ < n₁)
  Critical angle: θ_c = arcsin(n₂/n₁)
  Light at angle > θ_c from normal: totally internally reflected → guided
  Numerical aperture: NA = √(n₁² - n₂²) ≈ √(2n₁Δn)  where Δn = (n₁-n₂)/n₁
```

**Fiber attenuation**:
```
ATTENUATION VS WAVELENGTH (silica fiber)

Loss (dB/km)
│
5 ─    ╲                   Rayleigh scattering: ∝ 1/λ⁴
  │     ╲
2 ─      ╲
  │       ╲        O-band  E-band    S-band  C-band  L-band
1 ─         ╲   │   │       │         │       │       │
  │           ╲──┼───┼───────┼─────────┼───────┼───────┼──
0.5─            ╲│   │  OH⁻  │         │minimum│       │
  │              ╲   │ peak  │         │ 0.18  │       │
0.2─               ╲ │1383nm │         │dB/km  │       │
  │                 ╲│       │         │1550nm │       │
0.1─                 ╲
  └─────────────────────────────────────────────────────►
    800nm  1000  1200  1300  1400  1500  1600  1700 nm

OPERATING WINDOWS:
  O-band (1260-1360 nm): zero dispersion, used in short-reach, 10G CWDM
  E-band (1360-1460 nm): high OH loss — now cleared in "low-water-peak" fiber
  S-band (1460-1530 nm): CWDM channels
  C-band (1530-1565 nm): ← LOWEST ATTENUATION, EDFA amplification → standard DWDM
  L-band (1565-1625 nm): EDFA extension band, ultra-long haul, submarine
```

---

## DWDM: Dense Wavelength Division Multiplexing

```
DWDM WAVELENGTH PLAN

C-band with 100 GHz channel spacing (ITU Grid):
  Anchor: 193.1 THz (1552.52 nm)
  Channels: 192.1, 192.2, ..., 196.0 THz = 40 channels
  Spectral extent: 192.1–196.0 THz = 3.9 THz bandwidth

With 50 GHz spacing: 80 channels in C-band
With 37.5 GHz (flex grid): 96+ channels

AGGREGATION:
  Each channel carries one wavelength (one laser wavelength = one channel)
  MUX/DEMUX: AWG (arrayed waveguide grating) or thin-film filters → combine/separate λ
  ROADM (Reconfigurable Optical Add/Drop Multiplexer):
    Route wavelengths at a node without O-E-O conversion
    Direction-independent, colorless, contentionless (modern 3C ROADM)

CAPACITY EXAMPLE:
  48 channels × 200 Gbps per channel = 9.6 Tbps per fiber
  Submarine cable (6 fiber pairs): 57.6 Tbps per cable
  2023: 25.6 Tbps per SMF pair demonstrated in labs
```

---

## Optical Amplifiers: EDFA

```
EDFA (Erbium-Doped Fiber Amplifier)

KEY INVENTION (1987, Southampton + Bell Labs):
  Splice ~10 m of erbium-doped fiber (Er³⁺ ions) into path
  Pump with 980 nm or 1480 nm laser
  Signal photons (1530-1565 nm) stimulate emission from excited Er³⁺ → amplification!

PROPERTIES:
  Gain: 20-40 dB (typical)
  Bandwidth: 1530-1565 nm (C-band) → amplifies ALL channels simultaneously
  Noise figure: 3-6 dB
  Power output: +20 to +27 dBm (100 mW to 500 mW)

WHY EDFA CHANGED EVERYTHING:
  Before EDFA (1987): optical signal → convert to electrical → re-amplify → convert back
  Optical regenerator spacing: 50-100 km, expensive, speed-limited by electronics
  With EDFA: amplify optically every 80 km, no conversion, ALL wavelengths simultaneously
  → Enabled transoceanic fiber, DWDM capacity explosion

GAIN FLATTENING:
  EDFA gain spectrum is not flat — peaks at ~1530 and ~1558 nm
  Gain Flattening Filter (GFF) / Dispersion-Compensating Fiber (DCF): equalize gain
  Without equalization: after 20 amplifiers, gain variations multiply → channel imbalance

RAMAN AMPLIFIER:
  Stimulated Raman scattering in fiber itself (no doping needed)
  Distributed amplification → lower effective noise figure
  Can amplify outside EDFA band (S, L bands)
  Used in: ultra-long-haul, submarine cables, broadband DWDM
```

---

## Coherent Detection

```
COHERENT TRANSMISSION (dominant since 2010)

DIRECT DETECTION (older):
  Receiver: photodetector detects |E|² (optical power, loses phase)
  Limited to intensity modulation → OOK (on-off keying), DPSK
  Maximum ~40 Gbps per channel

COHERENT DETECTION:
  Local oscillator (LO) laser at receiver
  Mix received field with LO → beats → I and Q components recovered
  Enables: complex modulation (QAM) with full phase and amplitude recovery
  DSP compensates: chromatic dispersion, polarization mode dispersion, nonlinearities

DP-QPSK (Dual Polarization QPSK):
  4 bits per symbol: 2 bits in X polarization × 2 bits in QPSK + 2 more in Y polarization
  At 32 GBaud: 100 Gbps per channel
  Industry standard since ~2010

DP-16QAM:
  8 bits per symbol: 100 Gbps at 16 GBaud, 200 Gbps at 32 GBaud
  Requires higher SNR (shorter reach without regeneration)

DP-64QAM:
  12 bits per symbol → 400-600 Gbps per channel
  Short-reach (metro/datacenter interconnect) with high optical SNR

FLEXIBLE GRID + PROBABILISTIC SHAPING:
  Adaptive modulation: choose QAM order based on optical SNR at each wavelength
  Probabilistic constellation shaping: non-uniform symbol probabilities → approach Shannon limit
  ~1 dB gain, enables smooth trade between rate and reach
```

---

## Submarine Cable Systems

```
SUBMARINE CABLE FACTS (2024)

STRUCTURE OF A SUBMARINE CABLE:
  Optical fibers (8-24 pairs typically) + power conductor (copper center)
  Armor layers (shallow water) → anti-kink protection (deep water)
  EDFA/Raman amplifiers every 50-80 km (powered from shore via DC power)

SYSTEM CAPACITIES:
  TAT-8 (1988, first transatlantic fiber): 280 Mbps → historic
  TAT-14 (2001): 2 Tbps
  AEConnect-1 (2016): 17.6 Tbps
  MAREA (Microsoft/Facebook, 2017): 160 Tbps (8 pairs × 20 Tbps)
  Echo/Bifrost (2022): 200 Tbps
  Firmina (Google, 2023): 340 Tbps

GEOGRAPHY:
  ~1.4 million km of submarine fiber globally
  400+ active systems (2024)
  95% of international internet traffic carried by submarine cables
  (satellites carry rest: mainly backup, remote area, military)

CABLE BREAKS:
  ~100 cable faults per year globally
  Major causes: fishing trawls (50%), anchors (15%), geological/biological (rest)
  Repair: special cable ships, 2-6 weeks for deep-water repairs
  IMPORTANT: Multiple cables per route for resilience
  After 2022 Baltic cable cuts by ship anchors: NATO established monitoring programs
```

---

## Decision Cheat Sheet

| Application | Choice |
|-------------|--------|
| Long-haul terrestrial (>80 km) | SMF + C-band DWDM + EDFA |
| Datacenter interconnect (<10 km) | MMF OM4 + 100G/400G CWDM4 or SR4 |
| Metro network with reconfigurability | ROADM-based DWDM ring |
| Submarine transoceanic | SMF + DP-QPSK/DP-64QAM + EDFA+Raman + coherent |
| High-capacity campus | SMF OS2 + coherent ZR/ZR+ (100G-400G) |
| Maximum capacity per fiber | Flex-grid DWDM, DP-64QAM or higher, probabilistic shaping |

---

## Common Confusion Points

**Single-mode fiber is not faster**: Both SMF and MMF carry light at c/n (roughly 200,000 km/s).
SMF supports longer distances and higher bandwidth because it eliminates modal dispersion.
MMF is fine for 400 Gbps over 100 m; SMF is required for 10 Gbps over 50 km.

**EDFA amplifies noise too**: EDFA adds amplified spontaneous emission (ASE) noise to the signal.
The optical SNR (OSNR) degrades with each amplifier. After 20 EDFAs: OSNR budget is exhausted →
regeneration required. This is why ultra-long-haul uses Raman amplification (lower noise figure).

**Chromatic dispersion limits coherent links without DSP**: Different wavelengths travel at slightly
different speeds in fiber (dispersion: ~17 ps/nm/km for SMF at 1550 nm). At 100 Gbps, this disperses
pulses badly. Coherent DSP compensates digitally — no need for physical DCF anymore.

**Submarine cables are not satellite backup**: Submarine cables ARE the internet. Satellite
connections (Starlink, GEO) have latency, capacity, and reliability issues that make them
supplements, not replacements. Cutting a major submarine cable can isolate a country's internet.
