# Psychoacoustics — A Layered Guide

## The Big Picture

Psychoacoustics is the study of subjective perception of sound — how the auditory system
processes physical stimuli into perceived loudness, pitch, timbre, and location.
It is the foundation of lossy audio compression (MP3, AAC) and spatial audio.

```
PSYCHOACOUSTIC PROCESSING CHAIN
════════════════════════════════════════════════════════════════════

Physical          Outer/Middle    Cochlea (inner ear)     Auditory
Sound             Ear             Spectral analysis        Cortex
                                  + Timing                 Perception

p(t) ──►  [Pinna/EAC] ──► [Ossicles] ──► [Basilar] ──► [Auditory] ──► Pitch
[SPL dB]  [Resonances]   [Impedance      [membrane]    [nerve]         Loudness
          [HRTF          match           [tonotopic     [Phase lock     Timbre
          filtering]     air→fluid]      map]           + rate code]    Location
                                         |                              Rhythm
                                         └── Each location responds
                                             to narrow frequency band
                                             (critical band / CB)
```

---

## Equal-Loudness Contours (Fletcher-Munson / ISO 226)

The ear is not equally sensitive to all frequencies. Equal-loudness contours show which SPL values
at each frequency are perceived as equally loud.

```
EQUAL-LOUDNESS CONTOURS (approximate)

SPL (dB)
  │
110├─────────────────────────────────────── 100 phon
   │                                    ╱
100├──────────────────────────────────╱──── 90 phon
   │                              ╱
 90├────────────────────────────╱────────── 80 phon
   │                        ╱
 80├──────────────────────╱──────────────── 70 phon
   │                  ╱
 70├────────────────╱────────────────────── 60 phon
   │           ╱ ──╱
 60├─────────╱─╱─────────────────────────── 50 phon
   │      ╱╱
 50├────╱╱─────────────────────────────────  40 phon
   │  ╱  ──────────────── dip at 3-4 kHz
 40├─╱──────────────────────────────────────  30 phon
   │ Most sensitive here (2-5 kHz)
 30├────────────────────────────────────────  20 phon
   │
 20├─────────────────────────────────────────  10 phon
   │
  0├──────────────────────────────────────── 0 phon (threshold)
   └──────────────────────────────────────────►
   20 Hz   100    500   1k   3k  5k  10k   20kHz

KEY OBSERVATIONS:
• Human ear most sensitive at 2–5 kHz (ear canal resonance + cochlear response)
• At 1 kHz: 40 dB SPL perceived as 40 phon (definition)
• At 100 Hz: needs ~55 dB SPL to sound as loud as 40 dB at 1 kHz
• At very high levels (> 80 phon): curves flatten → all freqs perceived more equally
```

**Phon vs sone**: Phon is a relative measure (defined by equal-loudness comparison).
Sone is a linear perceptual scale: 1 sone ≡ 40 phon. Doubling sones ≈ +10 phon.

**A-weighting**: Filter that approximates the 40-phon equal-loudness curve.
dB(A) = SPL measured with A-weight filter. Attenuates low and very high frequencies.
Standard for regulatory noise measurements (OSHA occupational noise, WHO community noise).

---

## Critical Bands and Masking

The cochlea performs a frequency analysis using the basilar membrane.
Different locations along the basilar membrane respond maximally to different frequencies —
this is the **tonotopic map**.

```
CRITICAL BANDS

The auditory system processes sound in "critical bands" (auditory filters).
Width of each critical band ≈ 100 Hz below 500 Hz, ~20% of center frequency above.

ERB (Equivalent Rectangular Bandwidth):
ERB(f) ≈ 24.7·(4.37f/1000 + 1)  Hz    (for f in Hz)

At 1 kHz: ERB ≈ 128 Hz
At 4 kHz: ERB ≈ 400 Hz
At 100 Hz: ERB ≈ 35 Hz

Bark scale: 24 critical bands covering 20 Hz – 20 kHz
Mel scale: perceptual scale, 1000 mel ≡ 1000 Hz reference (used in MFCC)
```

**Simultaneous masking**: A loud tone makes nearby quiet tones inaudible.

```
SIMULTANEOUS MASKING

Masker (1 kHz tone, 80 dB SPL):
Creates a masking threshold in its vicinity:

SPL (dB)
   │
80 │         ████████████████
   │       ██                ██          Masking threshold
   │     ██                    ██        (inaudible region)
   │   ██                        ██
60 │─██────────────────────────────██─
   │                                  Absolute threshold
   └──────────────────────────────────►
   100Hz  500  1k  2k    5k   10k

• Higher masker level → wider masking region
• Upward spread of masking: high-level low-frequency maskers mask high-frequency tones
  more effectively than the reverse (asymmetric)
• Auditory filters have steeper low-frequency slope → masking spreads upward more
```

**Temporal masking**: Sound before and after a masker is also masked.
```
TEMPORAL MASKING WINDOW

SPL of masked signal:
  │      ┌──────────────────┐
  │      │   MASKER         │
  │      │   (e.g. 80 dB)  │
  │      │                  │
60├──────┼──────────────────┼───────────
  │◄─50ms│                  │  ◄─200ms►
  │pre-  │                  │  post-masking
  │mask  │                  │  (forward masking)
  └──────┴──────────────────┴────────────► time

Pre-masking (backward): ~10–20 ms before masker (perceptual lookahead?)
Post-masking (forward): 50–200 ms after masker ends (neurons still firing)
```

<!-- @editor[bridge/P2]: Missing bridge from masking/critical bands to MP3/AAC codec architecture — this is the direct application of psychoacoustics that a signal-processing-aware learner would want. Critical bands → filterbank (MDCT), simultaneous masking → allocate fewer bits to masked frequencies, temporal masking → avoid pre-echo artifacts, missing fundamental → quality metrics. MPEG Audio Layer III (MP3) and AAC are essentially psychoacoustic models operationalized as bit allocation algorithms. A compact "psychoacoustics → codec" table (perceptual phenomenon → codec mechanism → tradeoff) would close this gap cleanly. -->

---

## Pitch Perception

Two competing theories for how the brain extracts pitch:

```
PITCH PERCEPTION THEORIES

PLACE THEORY (Helmholtz):
• Basilar membrane location of maximum vibration → pitch
• Different places for different frequencies (tonotopic)
• Works well for high frequencies (> 1 kHz)
• Problem: Missing fundamental (see below)

TEMPORAL THEORY (periodicity):
• Auditory nerve fires in synchrony with waveform (phase locking)
• Works up to ~5 kHz (phase locking limit)
• Dominant for low-frequency pitch

CURRENT CONSENSUS: BOTH work together
• Low freq (< 1-2 kHz): temporal coding dominates
• High freq (> 4-5 kHz): place coding dominates
• 1-5 kHz: transition / combined

THE MISSING FUNDAMENTAL:
A 200 Hz tone has harmonics at 200, 400, 600, 800 Hz...
If you remove the 200 Hz fundamental:
  Remaining: 400, 600, 800, 1000 Hz
  Perceived pitch: STILL 200 Hz (not 400 Hz!)

Why: Temporal theory — nerve firing pattern at 400, 600 Hz periods
     has a common period of 1/200 Hz = 5 ms → brain infers 200 Hz
     This is why phone speakers (roll off below 400 Hz) sound like
     the voice has proper bass — missing fundamental is perceptually inferred.
```

---

## Binaural Localization

The brain determines sound direction using differences between the two ears.

```
THREE LOCALIZATION CUES

1. ITD — Interaural Time Difference (below ~1.5 kHz):
   Maximum delay when source is at 90° to one side: ~650 µs (head diameter / c ≈ 0.17m / 343m/s)
   Just noticeable difference: ~10 µs (about 1.4° azimuth)

            Source
              ↓
       ───────────────
      ●              ●   Ears
      │              │
   Close ear    Far ear
   (arrives      (arrives
   first)         later)
   Δt = ITD = d·sin(θ)/c

2. ILD — Interaural Level Difference (above ~1.5 kHz):
   At low freq: head is small relative to λ → sound diffracts around → small ILD
   At high freq: head casts an acoustic "shadow" → ILD can reach 20 dB at 90°

   ILD provides directional cues where ITD ambiguity occurs (wavelength < head diameter)

3. HRTF — Head-Related Transfer Function:
   Pinna (outer ear) shape diffracts sound differently depending on elevation and
   front-back direction. The HRTF encodes these cues.

   H_L(f, θ, φ): complex transfer function from source to left ear drum
   (Fourier transform of head-related impulse response, HRIR)

   HRTF enables:
   • Front/back discrimination
   • Elevation perception
   • Distance perception (indirect)

CONE OF CONFUSION:
Any point on a cone of constant azimuth has same ITD and ILD.
Brain uses HRTF spectral cues to resolve front/back ambiguity.
```

**3D Audio / Binaural Rendering**:
```
AMBISONICS / BINAURAL SYNTHESIS

To render a virtual sound at position (θ, φ):
1. Take source audio x(t)
2. Convolve with appropriate HRTF: L(t) = x(t) ★ h_L(t,θ,φ)
                                   R(t) = x(t) ★ h_R(t,θ,φ)
3. Listen on headphones → perceive sound at virtual location

HRTF databases: CIPIC, KEMAR dummy head, ARI
Individual HRTFs differ — "personalized HRTF" is active research area
```

---

## Key Auditory Illusions

| Illusion | Mechanism |
|----------|-----------|
| Missing fundamental | Temporal theory — brain infers pitch from harmonics |
| Shepard tone | Looping octave tones with amplitude envelope → infinite rising tone |
| Phantom center (stereo) | Two identical stereo channels → perceived center image |
| Precedence effect (Haas) | Echo within 30–40 ms fuses with first sound, direction from first |
| Octave equivalence | Tones at 2:1 ratio sound similar (octave equivalence) |
| Pitch shifts with loudness | Very low/high frequencies shift pitch with level (Stevens' rule) |

---

## Decision Cheat Sheet

| Application | Psychoacoustic Principle |
|-------------|--------------------------|
| MP3/AAC compression | Masking threshold — quantize below threshold |
| dB(A) measurement | A-weighting approximates 40-phon sensitivity |
| Speaker design: where to spend budget | 2–5 kHz is most perceptually sensitive |
| Binaural headphone rendering | Convolve with personalized HRTF |
| Perceptual pitch from bass-limited phone | Missing fundamental — temporal theory |
| Concert hall too reverberant | Late reverberation masks early reflections |
| Recording ambience in stereo | ITD + ILD cues via microphone spacing/angling |

---

## Common Confusion Points

**Loudness is not SPL**: SPL is a physical measurement (Pa or dB re 20 µPa).
Loudness is a perceptual quantity (phon or sone) that depends on frequency.
A 100 dB tone at 30 Hz sounds quieter than 80 dB at 3 kHz to a human.

**Pitch is not frequency**: Pitch is the perceptual correlate of frequency.
The relationship is non-linear (Mel/Bark scales). Musical intervals are logarithmic
(octave = 2:1 frequency ratio), not linear.

**Critical bands and masking explain codec artifacts**: When MP3 quantizes too coarsely,
the quantization noise spills outside the masking curve and becomes audible. At low bitrates,
you hear characteristic "swooshing" or "pre-echo" artifacts — the codec failed to stay below
the masking threshold.

**Phase is inaudible... except when it's not**: For steady-state tones, you can't hear phase.
But for transients and spatial cues (ITD), phase is critical. This is why audio codecs carefully
handle transient masking but may not preserve steady-state phase.
