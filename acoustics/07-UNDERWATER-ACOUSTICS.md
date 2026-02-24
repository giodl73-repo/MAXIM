# Underwater Acoustics — A Layered Guide

## The Big Picture

Sound is the dominant information-carrying wave in the ocean. EM waves attenuate within
meters in seawater; sound can travel thousands of kilometers. This makes acoustics the
foundation of underwater navigation, detection, communication, and sensing.

```
UNDERWATER ACOUSTICS APPLICATIONS MAP
════════════════════════════════════════════════════════════════════

Military:           Navigation:          Science:             Commercial:
Submarine           SONAR                Seismic survey       Echo sounding
detection           GPS (surface)        Marine mammal        Fish finding
Torpedo guidance    Acoustic beacons     research             Seabed mapping
Mine detection      USBL positioning     Climate monitoring   Offshore drilling

                    CORE PHYSICS:
                    Sound speed profile → refraction and ducting
                    Impedance and boundary → reflection/bottom loss
                    Absorption → range limits
                    Noise → detection limits
```

---

## Sound Speed in the Ocean

The speed of sound in seawater depends on temperature, salinity, and pressure (depth):

```
SOUND SPEED EQUATION (Medwin approximation):

c(T, S, z) = 1449.2 + 4.6T - 0.055T² + 0.00029T³
             + (1.34 - 0.010T)(S - 35) + 0.016z

T = temperature (°C), S = salinity (PSU), z = depth (m)

Ranges: c ≈ 1450–1540 m/s in typical ocean

SENSITIVITY:
∂c/∂T ≈ +4.6 m/s per °C   (temperature most important near surface)
∂c/∂S ≈ +1.3 m/s per PSU  (salinity less important)
∂c/∂z ≈ +0.016 m/s per m  (pressure effect, increases with depth)
```

**Sound Speed Profile (SSP)**: Vertical profile of c(z) — the most important input to ocean
acoustic propagation prediction.

```
TYPICAL OCEAN SOUND SPEED PROFILE

Depth (m)     c (m/s)
              1480    1500    1520    1540
     0        ├─────────────────●         ← warm surface layer (~1530)
  100 │       │               ●           thermocline: temp drops fast
  200 │       │           ●
  300 │       │       ●
  500 │       │     ●                     minimum sound speed (~1480 m/s)
 1000 │       │      ●                    ← SOFAR axis
 2000 │       │         ●
 3000 │       │             ●
 4000 │       │                 ●         ← pressure dominates (c increases)
 5000 │       │                     ●

SOFAR (Sound Fixing And Ranging) channel:
Centered at the sound speed minimum (~1000 m typical)
Sound refracts back toward the axis → trapped in horizontal waveguide
Allows propagation over thousands of km with little loss
```

---

## Sound Propagation: Snell's Law and Ray Theory

Sound refracts toward the region of lower sound speed (just like optics):

```
SNELL'S LAW IN OCEAN:
sin(θ₁)/c₁ = sin(θ₂)/c₂ = constant along a ray

(θ is angle from horizontal, not from vertical as in optics convention)

RAY BENDING RULES:
c increases with depth → rays bend downward (toward high c)
c decreases with depth → rays bend upward (toward high c above)

PROPAGATION SCENARIOS:

1. SURFACE DUCT (c increases from surface downward):
   Rays trapped near surface by temperature inversion
   Common in Arctic waters or after warm surface layer
   ┌──────────────────────────────────────────►
   │ ╲╱╲╱╲╱╲╱╲╱╲╱   Sound trapped in duct
   └──────────────────────────────────────────

2. SHADOW ZONE (thermocline):
   Source near surface, thermocline below
   Rays that go down: refracted through thermocline, no return
   Shadow zone at distance beyond first convergence zone
   Submarines can hide in shadow zone

3. CONVERGENCE ZONES (deep ocean):
   SOFAR channel traps → refracted up → convergence zone at surface
   CZ spacing: ~65 km intervals in typical N Atlantic
   Reliable detection at 65, 130, 195 km without bottom interaction

4. BOTTOM BOUNCE:
   Shallow water or direct bottom-hitting rays
   Bottom type determines bottom loss (sand: low loss, silt: high loss)
```

---

## SONAR

**SONAR = Sound Navigation And Ranging** (analogous to RADAR, but acoustic, ≤100 kHz typical)

```
SONAR EQUATION (passive):

SE = SL - TL - NL + DI - DT ≥ 0   (detection)

SE = Signal Excess (dB)
SL = Source Level (dB re 1 µPa at 1 m)
TL = Transmission Loss (dB)
NL = Noise Level (dB re 1 µPa in receiver bandwidth)
DI = Directivity Index of hydrophone array (dB)
DT = Detection Threshold (related to required SNR for given Pd, Pfa)

SONAR EQUATION (active):

SE = SL - 2·TL + TS - NL + DI - DT ≥ 0

TS = Target Strength (dB) = 10·log₁₀(σ/(4π))
     σ = backscattering cross-section (m²)
     Large submarine: TS ≈ 15–25 dB
     School of fish: TS ≈ -20 to 0 dB
     Seamount: TS ≈ high positive
```

### Transmission Loss

```
TRANSMISSION LOSS MODELS

Spherical spreading (free field, no boundaries):
TL = 20·log₁₀(r)    dB    (TL doubles every doubling of distance)

Cylindrical spreading (in waveguide, energy stays in layer):
TL = 10·log₁₀(r)    dB    (more favorable)

Combined (practical rule of thumb for shallow water):
TL = 15·log₁₀(r) + α·r/1000   dB

α = absorption coefficient (dB/km), function of frequency:
  At 1 kHz: α ≈ 0.06 dB/km
  At 10 kHz: α ≈ 1.0 dB/km
  At 100 kHz: α ≈ 30 dB/km
  At 1 MHz: α ≈ 200+ dB/km (ultrasound only useful for short range)

RANGE LIMITS:
Low frequency (< 1 kHz): limited by ocean noise (shipping, surf)
High frequency (> 10 kHz): limited by absorption
Mid frequency (1–10 kHz): optimal for long-range detection
```

---

## Beamforming

Arrays of hydrophones (receivers) process signals from multiple sensors to achieve directional gain.

```
LINEAR ARRAY BEAMFORMING

N hydrophones spaced d apart:

Output of delay-and-sum beamformer pointing at angle θ:
y(t) = Σ xₙ(t - τₙ)
        n
where τₙ = n·d·sin(θ)/c   (time delay for nth element)

Array gain: 10·log₁₀(N) dB improvement in SNR over single hydrophone
For N=100: 20 dB gain

BEAM PATTERN (far field):
|B(θ)| = |sin(N·π·d·sin(θ)/λ)| / |N·sin(π·d·sin(θ)/λ)|

Main lobe width ≈ λ/(N·d)   (radians, -3dB)

CRITICAL DESIGN:
Element spacing d ≤ λ/2 to avoid grating lobes (spatial aliasing)
Same rule as Nyquist sampling in space!
```

### Matched Field Processing (MFP)

```
MFP: Advanced coherent beamforming using full ocean acoustic model

Conventional beamforming: assumes straight-line paths
MFP: models actual curved ray paths through measured SSP
    Correlate received field with predicted field for each (r, z) source location
    → finds source location even in complex ocean environment

USE: Precision localization, ASW (anti-submarine warfare)
COST: Requires accurate ocean environmental model (SSP, bathymetry, bottom properties)
```

---

## Ambient Ocean Noise

The noise floor determines the detection limit.

```
KNUDSEN CURVES — Ocean Noise Spectrum

dB re 1 µPa²/Hz
│
130 ─                    ← Sea state 6 (high wind, waves)
    │
120 ─
    │                    Wind-generated noise:
110 ─                    dominant above ~200 Hz
    │
100 ─                    ← Sea state 2 (moderate)
    │
 90 ─                    ← Sea state 0 (calm)
    │
 80 ─         ←Shipping noise (dominant 10–200 Hz)
    │
 70 ─                    ← Thermal noise (dominant > 30 kHz)
    │
 60 ─
    └──────────────────────────────────────────────────►
    1 Hz    10     100     1k     10k    100k  (Hz)

NOISE SOURCES:
1–200 Hz:    Commercial shipping (dominant in most oceans)
200–50 kHz:  Wind-generated whitecapping, spray, bubbles
>50 kHz:     Thermal agitation noise of water molecules
Special:     Rain, ice cracking, snapping shrimp (bioacoustics)
```

---

## Marine Mammal Acoustics

```
CETACEAN SOUND PRODUCTION AND FUNCTION

DOLPHINS AND TOOTHED WHALES (Odontoceti):
• Echolocation: produce clicks at 20–200 kHz (ultrasonic)
  Click duration: 10–100 µs, source level: 220+ dB re 1 µPa at 1 m
  (among the loudest biological sounds)
  Resolve objects < 1 cm at 10 m range
• Communication: whistles, burst-pulse sounds (kHz range)

BALEEN WHALES (Mysticeti):
• Blue whale: 15–30 Hz (infrasound), SL ≈ 180–190 dB re 1 µPa at 1 m
  Audible across ocean basins via SOFAR channel
• Fin whale: 20 Hz pulses (now considered loudest animal sound)
• Humpback whale: complex songs (20 Hz – 8 kHz), used for reproduction

OCEAN NOISE IMPACT:
Commercial shipping noise (10–200 Hz) overlaps blue/fin whale communication band.
Measured ~10 dB increase in ambient noise at low frequencies since 1960s.
Marine Protected Areas and ship quieting (slow steaming, improved propellers) help.
```

---

## Decision Cheat Sheet

| Application | Key Principle |
|-------------|--------------|
| Long-range submarine detection | SOFAR channel, convergence zones, low frequency (< 500 Hz) |
| Short-range precision tracking | USBL (ultrashort baseline), high frequency |
| Fish finding | Echo sounder (38–120 kHz), target strength of fish |
| Seabed mapping | Multibeam sonar (200 kHz–400 kHz), swath bathymetry |
| Underwater communication | Acoustic modem (2–30 kHz), OFDM modulation |
| Shadow zone avoidance (navy) | Deploy towed array below thermocline |
| Measuring ocean temperature | Acoustic thermometry (ATOC: travel time changes with T) |

---

## Common Confusion Points

**c ≠ 1500 m/s always**: The 1500 m/s rule is a rough average. Real SSPs have variations
of ±50+ m/s with depth and season. These variations completely determine where sound goes —
don't treat c as a constant.

**SONAR frequency trade-off**: Low frequency = long range (low absorption, low noise floor in some
conditions) but poor resolution (large λ → large beam). High frequency = short range (high absorption)
but good resolution. No single frequency is optimal for all missions.

**Active vs passive SONAR**: Active (transmit + receive echo) reveals own position, detects quiet targets.
Passive (listen only) is stealthy, can detect loud targets at very long range. Modern submarines prefer
passive. Active used for shallow water mines, limited environments.

**Shipping noise and marine mammals**: The problem is not just loudness but overlap with whale
communication frequencies. Blue whales communicate at 15–30 Hz; ships generate strong noise at
20–200 Hz. Even moderate noise increases can mask communication over thousands of km.
