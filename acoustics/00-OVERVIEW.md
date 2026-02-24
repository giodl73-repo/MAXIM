# Acoustics — Overview

## The Big Picture

Acoustics is the physics and engineering of mechanical waves in elastic media.
Sound is a longitudinal pressure wave: molecules oscillate parallel to the direction of propagation.

```
THE ACOUSTIC FREQUENCY SPECTRUM
════════════════════════════════════════════════════════════════════════

Frequency:  0.001 Hz    20 Hz    200 Hz   2 kHz    20 kHz   1 MHz    1 GHz
            │           │        │        │        │        │        │
            ▼           ▼        ▼        ▼        ▼        ▼        ▼
            ─────────────────────────────────────────────────────────────
INFRASOUND: ████████████│                                              │
(< 20 Hz)  Seismic,     │                                              │
           wind, whale  │                                              │
                        │                                              │
AUDIBLE:                │█████████████████████████│                   │
(20–20k Hz) Speech, music│ Human hearing range      │                   │
                         │ Most sensitive: 2–5 kHz  │                   │
                                                    │                   │
ULTRASOUND:                                         │█████████████████│ │
(20 kHz–1 GHz)                   Medical imaging,  │bat, sonar, NDT   │ │
                                  HIFU treatment                       │
                                                                       │
HYPERSOUND: (> 1 GHz)                              Phonons, THz acoustics│
                                                    quantum acoustics      │
```

---

## Sound as a Physical Phenomenon

```
SOUND PROPAGATION MECHANISM

In a gas (air):
1. Source vibrates → compresses adjacent air layer
2. Compression wave propagates outward as series of high/low pressure regions

                Source     Compressions     Rarefactions
                  │        │ │ │ │          │ │ │ │
                  ●────────▓ ▓ ▓ ▓──────────░ ░ ░ ░────────►
                         (high P)          (low P)
                         ←─────── wavelength λ ──────────►

Speed of sound in air (ideal gas):
  c = √(γ·P₀/ρ₀) = √(γ·R·T/M) ≈ 331 + 0.6·T(°C)  m/s

  At 20°C: c ≈ 343 m/s
  At 0°C:  c ≈ 331 m/s

SOUND IS NOT EM RADIATION:
  • Requires a medium (can't travel through vacuum)
  • Particle motion is longitudinal (parallel to propagation)
  • Speed depends on medium elasticity and density
  • NOT c = 3×10⁸ m/s
```

---

## The Decibel Scale

Acoustic quantities span many orders of magnitude. Decibels (dB) compress this range.

```
THREE ACOUSTIC DECIBEL SCALES

Sound Pressure Level (SPL): most common, what microphones measure
  SPL = 20·log₁₀(p/p₀)  dB  where p₀ = 20 µPa (threshold of hearing)

Sound Intensity Level (SIL):
  SIL = 10·log₁₀(I/I₀)  dB  where I₀ = 10⁻¹² W/m²

Sound Power Level (SWL): source characteristic (independent of distance)
  SWL = 10·log₁₀(W/W₀)  dB  where W₀ = 10⁻¹² W

In a free field (anechoic, far from walls):
  SPL ≈ SIL  and  SWL = SIL + 10·log₁₀(4πr²)   for distance r from point source
```

**Key reference levels**:

| Level | SPL (dB) | Example |
|-------|----------|---------|
| 0 | 0 dB | Threshold of hearing |
| Whisper | 30 dB | Quiet library |
| Conversation | 60 dB | Normal speech at 1 m |
| City street | 70 dB | Busy traffic |
| Rock concert | 110 dB | Front row |
| Pain threshold | 130–140 dB | Jet engine at 30 m |
| Instant damage | 160+ dB | Gunshot, explosion |

**Inverse square law**: For a point source in free field:
```
SPL decreases 6 dB per doubling of distance (because area ∝ r², intensity ∝ 1/r²)
SPL(r₂) = SPL(r₁) - 20·log₁₀(r₂/r₁)  dB
```

---

## Module Map

```
acoustics/
│
├── 01-WAVE-PHYSICS           Foundation: wave equation, speed of sound, impedance
│       Reflection/transmission, diffraction, standing waves, resonance
│
├── 02-PSYCHOACOUSTICS        Perception: how the brain interprets sound
│       Equal-loudness contours, masking, pitch, binaural localization
│
├── 03-ROOM-ACOUSTICS         Enclosed spaces: reflection, reverberation
│       RT60, Sabine, Eyring, Schroeder frequency, diffusion
│
├── 04-ARCHITECTURAL-ACOUSTICS  Design of spaces for sound
│       Concert halls, speech intelligibility, recording studios, NC curves
│
├── 05-MUSICAL-ACOUSTICS      Instruments and voice as physics
│       String modes, wind resonance, percussion, piano, voice
│
├── 06-ELECTROACOUSTICS       Transducing between acoustic and electrical
│       Microphones (dynamic/condenser/ribbon), speakers, amplifiers
│
├── 07-UNDERWATER-ACOUSTICS   Sound in the ocean
│       SOFAR channel, sonar, beamforming, marine noise
│
├── 08-ULTRASOUND             Above 20 kHz: imaging and processing
│       Piezoelectric transducers, medical imaging, NDT
│
└── 09-NOISE-VIBRATION        Unwanted sound: isolation and control
        Sources, transmission paths, isolation vs damping, NVH, standards
```

---

## Acoustic Field Variables

| Quantity | Symbol | SI Unit | Description |
|----------|--------|---------|-------------|
| Sound pressure | p | Pa (N/m²) | Instantaneous pressure deviation from ambient |
| Particle velocity | u | m/s | Velocity of medium particles |
| Acoustic intensity | I | W/m² | Energy flow per unit area |
| Sound power | W | W | Total energy emitted per second |
| Acoustic impedance (specific) | Z = ρc | Pa·s/m (rayl) | Resistance to wave propagation |
| Wavelength | λ | m | λ = c/f |
| Wave number | k | rad/m | k = 2π/λ = ω/c |

**Specific acoustic impedance** Z = ρc:
- Air (20°C): Z ≈ 415 rayl (ρ ≈ 1.21 kg/m³, c ≈ 343 m/s)
- Water: Z ≈ 1.5 MRayl (3600× higher than air!)
- Steel: Z ≈ 47 MRayl

This 3600× impedance mismatch explains why ~99.9% of sound is reflected at air-water interfaces.

---

## Bridges to Prior Knowledge

| Signal Processing Background | Acoustics Equivalent |
|-------------------------------|---------------------|
| LTI system | Acoustic channel (room, horn, duct) |
| Convolution | Room impulse response (RIR) |
| Frequency response | Acoustic frequency response of space |
| Power spectral density | Noise spectral density (dB/Hz) |
| Resonance (pole near unit circle) | Room resonance (standing wave mode) |
| Matched filter | Sonar pulse compression |
| Beamforming (phased array) | Microphone array / sonar array |
| Human biology background | Ear anatomy → psychoacoustics |

---

## Decision Cheat Sheet

| Application | Key Concept |
|-------------|-------------|
| Why can I hear around corners? | Diffraction (wavelength-scale objects) |
| Why does bass go through walls? | Low frequency → long wavelength → less absorption |
| Concert hall sounds hollow? | Inadequate reverberation (RT60 too short) or flutter echo |
| Recording booth too reverberant? | Increase absorption (reduce RT60) |
| Measure sound level | SPL in dB re 20 µPa |
| Measure source loudness | Sound Power Level (SWL) |
| Subwoofer in a small room | Room modes (standing waves) at low frequencies |
| PA system feedback (squeal) | Loop gain > 1 at some frequency — microphone in speaker field |

---

## Common Confusion Points

**Sound is not the same as noise**: "Noise" in acoustics specifically means unwanted sound.
"Noise" in signal processing means random interference. Both fields use the same word differently.

**dB SPL vs dB(A) vs dB(C)**: SPL is unweighted. dB(A) applies A-weighting filter mimicking
human hearing sensitivity (less sensitive at low/high frequencies). dB(C) is C-weighting (flatter,
used for loud sounds/peak levels). Regulatory noise limits are usually in dB(A).

**Near field vs far field**: Close to a source (< wavelength), the acoustic field is complex
(near field). In the far field (> a few wavelengths), pressure falls as 1/r and the field
is well-behaved. Microphones should be in the far field of measured sources.

**Impedance mismatch at every boundary**: Any time sound crosses between media with different
Z = ρc, some reflects back. Air to glass, air to water, air to concrete — all have massive
mismatches. This is why sound isolation requires mass (adding mass = adding impedance).
