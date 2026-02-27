# Noise and Vibration — A Layered Guide

## The Big Picture

Noise and vibration control is the engineering of unwanted mechanical energy.
The source-path-receiver model is the universal framework: treat at source, block the path,
protect the receiver — in that priority order.

```
NOISE AND VIBRATION CONTROL FRAMEWORK
════════════════════════════════════════════════════════════════════

SOURCE ─────────────────► PATH ─────────────────► RECEIVER
  │                        │                         │
  │ Reduce at source:       │ Interrupt path:          │ Protect receiver:
  │ • Change process        │ • Barriers/enclosures    │ • Hearing protection
  │ • Redesign mechanism    │ • Isolation mounts       │ • PPE, HPDs
  │ • Balance rotating      │ • Decoupling             │ • Administrative controls
  │   parts                 │ • Absorption             │   (time limits)
  │ • Damping               │ • Mass addition          │ • Distance (1/r² rule)
  │ • Quiet materials       │ • Stiffness change       │
  │                         │ (for vibration)          │
  ▼                         ▼                          ▼
FIRST PRIORITY          SECOND PRIORITY           LAST RESORT
```

---

## Sound Radiation Mechanisms

Different source geometries radiate sound differently:

```
MULTIPOLE RADIATION ORDERS

MONOPOLE (point source, pulsating sphere):
  Radiates equally in all directions
  Intensity ∝ 1/r² (spherical spreading)
  Radiation efficiency: Pr ∝ ω⁴ · (volume velocity)²  → HIGH
  Example: pulsating balloon, loudspeaker diaphragm (bass)

DIPOLE (two equal and opposite monopoles):
  Figure-8 radiation pattern: strong at poles, null at equator
  Intensity ∝ 1/r² but lower efficiency
  Radiation efficiency: Pr ∝ ω⁶ → low at low frequencies
  Example: vibrating sphere, open-back loudspeaker, vibrating plate (free)

QUADRUPOLE (two equal and opposite dipoles):
  Complex radiation pattern
  Radiation efficiency: Pr ∝ ω⁸ → very low
  Example: turbulent jet noise (Lighthill's acoustic analogy)
  Jet aircraft noise is dominated by quadrupole → 8th power of jet velocity!
  This is why jet noise decreases so dramatically when throttling back.

RULE: Higher multipole order → less efficient radiator → easier to reduce noise
      Adding a baffle to a dipole source can increase radiation (converts to monopole)
```

---

## Vibration Isolation

Vibration isolation prevents transmission of mechanical vibrations between structures.

```
SINGLE DEGREE OF FREEDOM ISOLATOR MODEL

         m (machine)
          ╔═══╗
          ║   ║
          └─┬─┘
          [k]|[c]   spring k + damper c
          ──┴──
         Foundation

EQUATION OF MOTION:
  m·ẍ + c·ẋ + k·x = F(t)

NATURAL FREQUENCY:
  fₙ = (1/2π)·√(k/m)   Hz  (lower → better isolation at high frequencies)

FORCE TRANSMISSIBILITY (ratio of transmitted to applied force):

T(f) = |1 + 2jζ(f/fₙ)| / |1 - (f/fₙ)² + 2jζ(f/fₙ)|

where ζ = c/(2√(km)) = damping ratio

ISOLATION REGION: f > √2 · fₙ  (T < 1 → isolation achieved)

At f = fₙ: resonance → T > 1 (amplification!)
T at resonance ≈ 1/(2ζ) — damping prevents catastrophic amplification

TRANSMISSIBILITY vs FREQUENCY:

T(dB)
  │    Resonance peak
 +20 ─         ╱╲
    │          ╱  ╲
  0 ─────────╱────╲──────────────
    │      fₙ·√2   ╲
 -20 ─                ╲─────────── isolation region (-40 dB/decade for undamped)
    └─────────────────────────────►
    0       fₙ     2fₙ    5fₙ   10fₙ
```

**Isolation mount design**:
```
ISOLATION MOUNT TYPES

Rubber mounts:
  fₙ: 5–25 Hz depending on stiffness and load
  ζ: 0.05–0.1 (some damping inherent)
  Use: HVAC equipment, industrial machinery

Air springs (pneumatic):
  fₙ: 0.5–2 Hz (very low, very good isolation)
  Need air supply, level-sensing for variable load
  Use: precision optical tables, printing presses, premium isolation

Wire rope isolators:
  High load capacity, weather resistant, fatigue resistant
  Use: military electronics, outdoor equipment

Active isolation:
  Sensors measure vibration → actuators cancel it
  Can achieve isolation below fₙ
  Use: AFM microscopes, semiconductor fabs, premium optics

STATIC DEFLECTION RULE:
fₙ = 0.5/√(x_st)   Hz  where x_st = static deflection (cm)

To isolate 50 Hz machine at 85% isolation (T < 0.15):
Need fₙ < 50/(√(1/0.15)) ≈ 19 Hz
x_st = (0.5/fₙ)² = (0.5/19)² ≈ 0.7 mm → achievable with rubber
```

---

## Damping vs Isolation

These are often confused but are fundamentally different:

```
DAMPING:
  Converts vibration energy → heat within the structure
  Reduces amplitude at resonance (reduces resonance peak)
  Acts over the entire frequency range
  Material damping: η (loss factor), typically 0.001–0.1 for metals
  Constrained layer damping: viscoelastic material sandwiched between stiff layers
  Use when: resonance amplification is the problem

ISOLATION:
  Prevents vibration energy from entering or leaving a structure
  Attenuates vibration ABOVE the isolator's natural frequency
  Does nothing (amplifies!) at and below resonance frequency
  Soft mounts → lower fₙ → better isolation at given excitation frequency
  Use when: excitation frequency is fixed and above the natural frequency

BOTH TOGETHER: Damping reduces the resonance peak; isolation reduces transmission above fₙ
  Ideal isolator: very soft spring (low fₙ) + moderate damping (ζ ≈ 0.1–0.2)
```

---

## NVH: Noise, Vibration, and Harshness

NVH is the automotive/aerospace discipline for controlling structure-borne and airborne noise.

```
AUTOMOTIVE NVH SOURCES

Frequency     Source                  Path                   Receiver
────────────────────────────────────────────────────────────────────────
10–80 Hz      Engine vibration        Mounts → body → seat  Whole-body vibration
20–200 Hz     Road roughness          Tires → suspension     Floor, seat vibration
20–500 Hz     Powertrain              Drivetrain → mounts    Structural vibration
100–1000 Hz   Tire-road noise         Air → door seals       Interior noise
500–8000 Hz   Wind noise              A-pillars, mirrors     Interior noise
All           Brake squeal            Caliper chatter        Airborne noise

NVH TESTING:
• Modal analysis: hammer test or shaker → FRF (frequency response function)
  Identify resonant modes of panels, chassis, subframes
• Transfer path analysis (TPA): decompose contribution of each path
• Sound quality metrics: loudness, sharpness, roughness, tonality, articulation index
```

**Key NVH treatments**:
```
AUTOMOTIVE NOISE TREATMENTS

Dead space barrier: mass + decoupling
  - Mass law for transmission loss: TL = 20·log(m·f) - 47 dB
  - Typical: 5 kg/m² bituminous layer → TL ≈ 30–40 dB at 1 kHz

Acoustic absorption:
  - Porous absorber (foam, felt, fibrous materials) in cavities
  - Absorbs reflected energy in trunk, door panels

Constrained layer damping (CLD):
  - Viscoelastic + steel sheet bonded to body panels
  - Reduces panel resonances (sheet metal modes at 100–1000 Hz)

Acoustic encapsulation:
  - Full engine bay enclosure: barrier + absorber
  - Can reduce 6–10 dB engine noise in passenger compartment
```

---

## Regulatory Standards

```
NOISE EXPOSURE LIMITS

OSHA (USA) — Occupational:
  90 dB(A) for 8 hours TWA (time-weighted average)
  For every 5 dB increase: permitted time halves
  85 dB(A): action level (must provide hearing protection option)
  85 dB: NIOSH recommends as TLV

  TWA (dB) | Permissible hours/day
  ─────────────────────────────────
  90       | 8
  95       | 4
  100      | 2
  105      | 1
  110      | 0.5
  115      | 0.25 (15 min)
  120      | impulse only

WHO Community Noise Guidelines:
  Day (7am-11pm): < 55 dB Lden outdoors
  Night (11pm-7am): < 45 dB outdoors (sleep disturbance)
  Schools: < 35 dB during teaching
  Hospitals: < 30 dB in wards at night

EU Environmental Noise Directive:
  Noise mapping → action plans → quiet zones
  L_den (day-evening-night level): penalties for evening (+5 dB) and night (+10 dB)

VEHICLE PASS-BY NOISE:
  Euro 6d passenger cars: 68–72 dB(A) (ISO 362 pass-by test)
  Targets reduction to 68 dB(A) by 2024 (EU Regulation 540/2014)
```

---

## Tuned Mass Damper (TMD)

```
TUNED MASS DAMPER:

Add a secondary mass-spring system tuned to the resonant frequency of the primary structure.
At resonance: secondary oscillator resonates, absorbs energy, reduces primary amplitude.

Primary:   Mass M, spring K → fₙ = (1/2π)√(K/M)
TMD:       mass m << M, spring k → f_TMD = (1/2π)√(k/m) = fₙ (tuned to primary)

Effect at primary resonance:
Without TMD: amplification up to 1/(2ζ) — can be 50–100×
With TMD:    amplification reduced to ~1/(2ζ_TMD) of TMD → much less peak response

REAL-WORLD EXAMPLES:
• Taipei 101: 660-ton steel sphere at 87th floor → reduces wind vibration
• Millennium Bridge, London: 37 TMDs (lateral) + 52 TMDs (vertical) retrofitted after 2000 resonance
• Buildings, bridges, power lines, turbine blades, drilling equipment
```

---

## Decision Cheat Sheet

| Problem | Tool |
|---------|------|
| Isolate vibrating machine from floor | Soft mounts with fₙ < excitation frequency/√2 |
| Reduce resonance amplitude | Damping treatment (CLD, viscoelastic inserts) |
| Reduce radiated noise from panel | Mass addition (mass law) + absorption |
| Measure vibration modes | Modal analysis (impact hammer, FRF measurement) |
| Protect workers from noise | Engineering controls first, then HPE, then PPE |
| Structural vibration at one frequency | Tuned mass damper (TMD) |
| Automotive interior noise above 500 Hz | Barrier (transmission loss) + absorption |
| Automotive interior noise below 200 Hz | Structural stiffening, subframe decoupling, mounts |

---

## Common Confusion Points

**Soft mounts amplify vibration at resonance**: If the excitation frequency is near the mount's
natural frequency, the mount amplifies rather than isolates. This is why HVAC fans on spring isolators
can be terrible during startup/shutdown as they pass through resonance.

**Absorption doesn't block sound**: Foam, fiberglass, and acoustic ceiling tiles absorb sound energy
(reduce reverberant noise), but they do NOT stop sound from passing through walls. For transmission
loss, you need mass and decoupling (stiff, heavy, discontinuous assembly).

**Vibration isolation and noise isolation are different paths**: A machine can be isolated vibrationally
from a floor (prevent structure-borne noise), but still radiate airborne noise directly. Both paths
must be addressed. Enclosures handle airborne; isolation mounts handle structure-borne.

**dB(A) weighting ignores infrasound and some high frequencies**: dB(A) de-emphasizes frequencies
below ~1 kHz. Wind turbine infrasound and very-low-frequency machinery are poorly captured by dB(A).
Alternative: dB(G) G-weighting for infrasound assessment, dB(C) for peak impact noise assessment.

## Beyond the Mass Law: Acoustic Metamaterials

```
ACOUSTIC METAMATERIALS — KEY CONCEPTS
═══════════════════════════════════════════════════════════════════

LOCALLY RESONANT STRUCTURES (Liu et al., 2000):
  Small resonators embedded in a matrix. At their resonance frequency,
  they produce negative effective mass → sound cannot propagate.
  Achieves sub-wavelength blocking: isolates low-frequency sound with
  a structure much thinner/lighter than the mass law would require.

PHONONIC CRYSTALS:
  Periodic structures with acoustic band gaps — frequency ranges
  where sound cannot propagate, analogous to photonic crystals
  in optics and electronic band gaps in semiconductors.
  Design parameter: lattice period ≈ wavelength of target frequency.

MEMBRANE-TYPE ACOUSTIC METAMATERIALS (MAMS):
  Tensioned membranes with attached masses. Create transmission loss
  peaks at specific frequencies. Lightweight alternative to mass-based
  barriers for targeted frequency control.

PRACTICAL STATUS (2025):
  Lab-proven for narrowband isolation. Broadband and tunable designs
  are active research. Commercial products emerging for HVAC duct
  silencers and automotive NVH panels.
```
