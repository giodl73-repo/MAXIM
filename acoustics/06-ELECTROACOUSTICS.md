# Electroacoustics — A Layered Guide

## The Big Picture

Electroacoustics is the conversion between acoustic (pressure/velocity) and electrical
(voltage/current) energy. Microphones convert acoustic → electrical; loudspeakers do the reverse.
All transducers obey the same reciprocity principle.

```
ELECTROACOUSTIC TRANSDUCER MAP
════════════════════════════════════════════════════════════════════

ACOUSTIC ──────────────────────────────────────────► ELECTRICAL
  │                 TRANSDUCTION                          │
  │                 MECHANISMS                            │
  │                                                       │
  │   Electromagnetic (dynamic)    Moving coil in field   │
  │   Electrostatic (condenser)    Moving plate in field  │
  │   Piezoelectric                Mechanical strain      │
  │   Magnetostrictive             Magnetic strain        │
  │   Electret                     Permanent polarization │
  │                                                       │
  ▼                                                       ▼
Pressure wave                               Electrical signal
(Pa, m/s)                                   (V, A, W)

RECIPROCITY PRINCIPLE:
Any transducer that converts acoustic → electrical also works in reverse.
Dynamic microphone ↔ Dynamic loudspeaker (same physical principle)
Condenser microphone ↔ Electrostatic loudspeaker
Piezo microphone ↔ Piezo speaker (buzzer, ultrasonic transducer)
```

---

## Microphone Types

### Dynamic (Moving Coil) Microphone

```
DYNAMIC MICROPHONE CONSTRUCTION:

        Sound
         ↓
    ┌─────────────────────────────┐
    │  Diaphragm (plastic/mylar)  │
    │       │                     │
    │    ┌──┴──┐                  │
    │    │Coil │ ← suspended in   │
    │    │     │   magnetic gap   │
    │    └──┬──┘                  │
    │       │                     │
    │   [permanent magnet]        │
    └─────────────────────────────┘
            │
        Electrical output
        (AC voltage, ~1 mV/Pa)

PHYSICS: Faraday's law — coil moves in magnetic field → EMF = B·l·v
         v = velocity of diaphragm (acoustic particle velocity)
         Output voltage ∝ diaphragm velocity (velocity microphone)

CHARACTERISTICS:
• Robust, handles high SPL (130+ dB), doesn't need power
• Limited low-frequency response (mass of coil + diaphragm)
• Typically ±3 dB from 50 Hz – 15 kHz (decent dynamic range)
• Self-noise: 14–20 dB SPL equivalent
• Use: live vocals, drums, guitar amps (Shure SM58, SM57)

PROXIMITY EFFECT:
Close-miking (< 30 cm) of directional dynamics: bass frequencies boosted.
Cause: pressure gradient mics (cardioid) have a distance-dependent low-frequency response.
F_bass boost = ∝ 1/distance at low frequencies.
```

### Condenser (Capacitor) Microphone

```
CONDENSER MICROPHONE CONSTRUCTION:

    Sound ↓
    ┌─────────┐
    │ Thin    │  Backplate (fixed electrode)
    │ Membrane│──────────────────────
    │(moving  │  Air gap (~20 µm)
    │electrode│──────────────────────
    └─────────┘  Fixed backplate
                  ↑
            V_bias = 48–200V DC (phantom power or internal)

PHYSICS: Q = C·V, but Q is held constant by high source impedance.
         If membrane moves Δd: C = ε₀A/d, so ΔV = V·Δd/d
         Output voltage ∝ diaphragm displacement (pressure microphone)

CHARACTERISTICS:
• Highest sensitivity (typically -40 to -25 dBV/Pa)
• Very flat, extended frequency response (20 Hz – 20 kHz, ±1-2 dB)
• Requires 48V phantom power (P48) — standard for XLR microphones
• More fragile than dynamic (moisture, rough handling)
• Use: studio vocals, acoustic instruments, measurement mics

SMALL DIAPHRAGM vs LARGE DIAPHRAGM:
Small (< 1/2" capsule): better transient response, flatter off-axis response
Large (≈ 1"): warmer sound, more sensitive, character (KM84/AKG 414)
```

### Ribbon Microphone

```
RIBBON MICROPHONE:

Thin corrugated aluminum ribbon (0.5-2 µm thick)
suspended between magnet poles.
Vibrates as both diaphragm AND coil simultaneously.

CHARACTERISTICS:
• Figure-8 polar pattern (bidirectional — inherent to the physics)
• Very high sensitivity to velocity (not pressure)
• Characteristic smooth, "warm" high-frequency rolloff
• Extremely fragile — air blasts (plosives, air conditioning) can destroy ribbon
• No phantom power (can DAMAGE older ribbon mics)
• Use: broadcast room mics, guitar amplifier recording (RCA 44, 77, Coles 4038)
```

---

## Polar Patterns

```
POLAR PATTERNS

Omnidirectional: captures equally from all directions
    Sensitivity: 1 (all angles)

Cardioid: front-facing, rejects rear
    Sensitivity: (1 + cos θ)/2
    Front to back rejection: ∞ (null at 180°) → practical 20-25 dB

Hypercardioid: narrower pickup, some rear sensitivity
    Sensitivity: (1 + 3cos θ)/4
    Maximum rejection: at 120° from front

Figure-8 / Bidirectional: front + rear, null at sides
    Sensitivity: cos θ
    Use: MS recording, ribbon mics

        Omni          Cardioid          Figure-8
         ●               ●                 ●
    ◄─ – – – ─►    ◄──/  \──►         ◄─/│\─►
         ●            ───              ───┼───
                                          │

MULTI-PATTERN CONDENSERS (e.g., AKG C414):
Combine two back-to-back capsules electrically to select pattern.
Physical cardioid capsule: omni + figure-8 = cardioid.
```

---

## Loudspeaker Design

```
DYNAMIC LOUDSPEAKER STRUCTURE:

            ┌─────────────────────────────────────────┐
            │                                          │
    Input   │  Spider ─►[Voice coil]◄─ Spider         │
    (AC)   ─┤           Motor: B·l·I = Force          │
            │  Force moves diaphragm (cone or dome)    │
            │                                          │
            │  [Cone/dome diaphragm]                   │
            │  │                                       │
            │  └──► Acoustic radiation                 │
            └─────────────────────────────────────────┘

PARAMETERS (Thiele-Small parameters):
  fs: free-air resonance frequency
  Qts: total Q factor at resonance
  Vas: equivalent acoustic volume
  Sensitivity: dB SPL at 1m, 1W (typically 85–92 dBSPL)
  Xmax: maximum linear excursion (determines max SPL at bass)
```

**Frequency range and crossovers**:
```
TYPICAL SPEAKER DRIVER FREQUENCY RANGES:

Driver           Diameter    Frequency Range      Use
────────────────────────────────────────────────────────────
Subwoofer        12–21"      20–80 Hz            Deep bass
Woofer            8–15"      50–500 Hz           Bass/mid-bass
Midrange          3–6"       500–3000 Hz         Vocals, instruments
Tweeter           1–2"       2000–20,000 Hz      High frequencies
Super-tweeter    < 1"        10,000–40,000+ Hz   Air, HF extension

TWO-WAY SPEAKER: woofer + tweeter + crossover
THREE-WAY: woofer + midrange + tweeter + crossover

CROSSOVER NETWORK:
Passive: L/C filter after amplifier → splits frequency bands → different drivers
Active (bi-amp/tri-amp): separate DSP filters → separate amplifiers → separate drivers
Active is more efficient, better controlled, but more complex

Butterworth 2nd-order crossover:
  LPF: H_LPF(f) = 1/(1 + (f/fc)² + j√2·f/fc)   → woofer
  HPF: H_HPF(f) = (f/fc)² / (1 + (f/fc)² + j√2·f/fc)  → tweeter
```

### Enclosure Types

```
LOUDSPEAKER ENCLOSURES

SEALED BOX:
  Woofer in sealed enclosure.
  Roll-off: 12 dB/octave below fs (2nd order)
  Tighter bass, smaller enclosure, well-controlled
  Less efficient than ported

PORTED (Vented/Bass-Reflex):
  Port is a Helmholtz resonator tuned to extend bass.
  Below port tuning: roll-off steeper (24 dB/octave)
  More efficient, deeper bass extension for same driver
  Trade-off: louder transients possible but port creates non-linearity at extremes

OPEN BAFFLE:
  No enclosure, driver on flat board.
  Rear and front waves cancel (dipole radiation) at low frequencies
  Very open sound but very inefficient at bass

HORN-LOADED:
  Throat → flaring horn → bell
  Exponential/tractrix horn profiles match driver impedance to air
  Very high efficiency (99 dB/W/m), but large, directional, complex
  Used in: PA systems, vintage hi-fi, acoustic amplification
```

---

## Key Specifications

```
MICROPHONE SPECIFICATIONS:
Sensitivity:     dBV/Pa (ref 1V/Pa)   typical: -40 to -25 dBV/Pa
Self-noise:      dB(A)  equivalent input noise    typical: 10–25 dB(A)
Dynamic range:   max SPL - self noise (dB)          typical: 110–130 dB
Max SPL:         SPL at 1% THD (total harmonic distortion)   typical: 120–150 dB
Frequency resp:  ±dB from flat, 20–20k Hz
Polar pattern:   omni/cardioid/figure-8/variable

LOUDSPEAKER SPECIFICATIONS:
Sensitivity:     dB SPL at 1m, 2.83V input        typical: 84–100 dB
Impedance:       Ω (nominal, varies with freq)    typical: 4, 6, 8 Ω
Frequency resp:  Hz–kHz ±dB in specified tolerance
Power handling:  Continuous/program/peak W
THD:             % at rated power, given frequency
Xmax:            mm one-way excursion at specified THD
```

---

## Decision Cheat Sheet

| Application | Best Microphone Type |
|-------------|---------------------|
| Live vocals (stage) | Dynamic cardioid (SM58 type) — handles abuse, feedback rejection |
| Studio vocals | Large diaphragm condenser — maximum detail and sensitivity |
| Acoustic piano | Small diaphragm condenser pair — precise transients and stereo |
| Kick drum | Large diaphragm dynamic (D112, Beta 52) — handles high SPL |
| Guitar amp | Dynamic (SM57) or ribbon — close micing |
| Room ambience | Pair of small condensers (ORTF, XY) or large condenser |
| Measurement/calibration | Reference condenser omnidirectional |
| Ultrasound | Piezoelectric transducer (piezo) |

---

## Common Confusion Points

**Phantom power (+48V) is not always safe**: Balanced dynamic mics (SM57 etc.) ignore phantom power.
Ribbon mics — old ones can be damaged by phantom power (T-connector accidental short). Modern ribbon
mics are often safe, but check the datasheet. Never apply phantom power to unbalanced connections.

**Sensitivity vs noise floor**: High sensitivity means 1 Pa → high output voltage. But the self-noise
is what determines the noise floor. A mic with -30 dBV/Pa sensitivity but 25 dB(A) self-noise is
worse for quiet sources than -40 dBV/Pa with 10 dB(A) self-noise.

**Thiele-Small parameters are small-signal**: Ts parameters (fs, Qts, Vas) are linear approximations
at tiny excursion. At large excursion (near Xmax), the driver becomes nonlinear. Distortion rises
dramatically above Xmax — many manufacturers specify 10% THD, which is audibly terrible.

**Room acoustics dominates speaker quality in practice**: Even a mediocre speaker in a well-treated
room sounds better than an excellent speaker in a bad room. Above ~200 Hz, the room's reflection
pattern and modes swamp the driver response variations. Acoustic treatment before upgraded speakers.
