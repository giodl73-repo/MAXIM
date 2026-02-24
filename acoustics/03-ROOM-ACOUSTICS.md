# Room Acoustics — A Layered Guide

## The Big Picture

A room transforms a direct sound into a complex reverberant field.
Understanding this transformation determines how spaces sound and how to design them.

```
ROOM SOUND FIELD TIMELINE
════════════════════════════════════════════════════════════════════

Source emits a pulse at t=0

                                                     Late reverb
                    Early reflections               (diffuse field)
         Direct     (from nearby surfaces)
         ↓          ↓↓↓↓                          ↓↓↓↓↓↓↓↓↓↓↓↓↓
         │          │││                           ─────────────────────
Sound ──►│──────────│││────────────────────────── echo density grows ──► silence
Level   ─┼──        │││                                                RT60
(dB)     │  └─Direct│││Early                     Diffuse reverberant
         │          └┘└reflections                tail decays -60 dB
         ─────────────────────────────────────────────────────────►
         0        5–50ms           100ms                  Time
                                              ↑
                                    Schroeder freq crossover

THREE ACOUSTIC ZONES:
1. Direct field: falls as 1/r²
2. Early reflections: arrive within 50–80 ms, carry useful spatial information
3. Reverberant (diffuse) field: energy density uniform, dominated by late reflections
```

---

## Reverberation Time: RT60

RT60 (T60) is the time for sound level to decay by 60 dB after the source stops.
It's the most important single acoustic descriptor of a room.

```
RT60 DEFINITION

T60: time for impulse response energy to decay by -60 dB (= factor of 10⁶ in power)

More practically, T30 × 2 (decay from -5 to -35 dB, extrapolated to 60 dB)
  — the full 60 dB range is often in the noise floor

RT60 VS INTENDED USE:
Spaces for SPEECH:    T60 = 0.3–0.7 s  (short → intelligibility)
Offices/classrooms:   T60 = 0.4–0.8 s
Concert halls:        T60 = 1.5–2.2 s  (long → orchestral richness)
Opera houses:         T60 = 1.2–1.7 s
Churches/cathedrals:  T60 = 2–5+ s    (very long → choral/organ "bloom")
Recording studios:    T60 = 0.2–0.4 s  (dry, controllable)
Recording booths:     T60 < 0.1 s      (virtually anechoic)
```

---

## Sabine Formula

Wallace Clement Sabine (1900) derived the first RT60 formula empirically.

```
SABINE FORMULA:

T60 = 0.161 · V / (S · ᾱ)      (SI units)

V  = room volume (m³)
S  = total surface area (m²)
ᾱ  = average absorption coefficient (dimensionless, 0–1)
S·ᾱ = total absorption A (m² Sabin or "sabins")

ABSORPTION COEFFICIENTS (typical, 500 Hz):
Material                    α
────────────────────────────────────────
Bare concrete               0.02
Plaster on brick            0.03
Glass (large pane)          0.03
Carpet (thick)              0.35
Acoustic ceiling tile       0.65–0.80
Upholstered seat (unoccupied) 0.60
Audience (per person)       0.45 m²
Porous absorber (mineral wool) 0.80–0.95

EXAMPLE: Concert hall
V = 15,000 m³, S = 5,000 m², ᾱ = 0.15
T60 = 0.161 × 15,000 / (5,000 × 0.15) = 0.161 × 15,000 / 750 = 3.2 s
(too reverberant — need more absorption or smaller volume)
```

**Sabine's assumption**: random, diffuse sound field (energy uniformly distributed).
Works well for large rooms with moderate absorption and many reflecting surfaces.

---

## Eyring Formula

Sabine overestimates RT60 in rooms with high absorption. Eyring corrects this.

```
EYRING FORMULA:

T60 = 0.161 · V / (-S · ln(1 - ᾱ))

For small ᾱ: ln(1-ᾱ) ≈ -ᾱ → Eyring ≈ Sabine
For large ᾱ: Eyring gives significantly shorter RT60

WHY EYRING IS BETTER:
Sabine: each reflection absorbs a fraction ᾱ of remaining energy independently
Eyring: accounts for the statistical mean free path (average distance between reflections)
        and the compounding effect of each absorption event

Mean free path: d = 4V/S
Mean time between reflections: Δt = d/c = 4V/(S·c)

Both formulas fail when:
• Absorption is highly non-uniform (one absorptive wall, others reflective)
• Room is strongly coupled (multiple rooms connected)
• Room is below the Schroeder frequency (modal behavior, not statistical)
```

---

## Frequency Dependence of Absorption

Absorption coefficients vary strongly with frequency — low frequencies are hard to absorb.

```
ABSORPTION VS FREQUENCY (typical materials)

α
1.0│
   │
0.8│           Thick mineral    ●──────────────●
   │           wool (100mm)    ●               ●
0.6│                         ●
   │         Acoustic     ●─●─●───────────────●
0.4│         ceiling tile●
   │                   ●
0.2│   Carpet (10mm)  ●─●─●──●───●────────────●
   │                ●
0.0│────●──●──●──●──────────────────────────────
   │ Bare concrete / plaster
   └──────────────────────────────────────────►
      63  125  250  500  1k   2k   4k  (Hz)

KEY OBSERVATIONS:
• Low frequencies (< 250 Hz) require thick absorbers (λ/4 minimum = 0.34 m at 250 Hz)
• Thin carpet: good at high frequencies, useless at low
• Porous absorbers (mineral wool): effective above ~400 Hz only
• Bass traps needed for low-frequency control:
  - Corner-mounted porous absorbers (minimum 200mm thick)
  - Resonant panel absorbers (tuned to specific low frequency)
  - Helmholtz resonators (cavity resonator, adjustable frequency)
```

---

## Schroeder Frequency

Below the Schroeder frequency, the room response is dominated by discrete standing wave modes.
Above it, modes overlap enough to behave statistically (diffuse field).

```
SCHROEDER FREQUENCY:

f_S = 2000 · √(T60/V)    (Hz)

Examples:
Concert hall: V = 15,000 m³, T60 = 2 s → f_S ≈ 23 Hz  (almost all diffuse)
Home studio:  V = 30 m³,   T60 = 0.4 s → f_S ≈ 115 Hz
Small room:   V = 20 m³,   T60 = 0.5 s → f_S ≈ 141 Hz

MEANING:
Below f_S: Use modal analysis (Schroeder-Kuttruff theory, FEM/BEM for room modes)
Above f_S: Use statistical/geometrical acoustics (ray tracing, image source method, sabine)

In a home recording studio or home theater:
f_S ≈ 100–200 Hz → bass frequencies (up to 200 Hz) are in modal regime
→ This is why bass buildup in corners is a problem
→ Geometric acoustics tools don't predict this regime
```

---

## Early Reflections and the Precedence Effect

```
ROOM IMPULSE RESPONSE ANATOMY

h(t):     Direct    Early          Late reverb
           pulse    reflections    (exponential decay)
             │       ↓↓↓          ↓↓↓↓↓↓↓↓↓↓↓↓↓
             ●      ●●●          ──────────────────────── decay -60dB
             0    10-50ms         50ms+
             │         │
             │         │
             ├─ Useful: ─┤
             │ Haas zone │
             │ (fuses    │
             │ with      │  Beyond 50ms: perceived as echo
             │ direct)   │  (in speech) or reverberance
                         │  (in music)

PRECEDENCE EFFECT (Haas effect):
Sound arriving within 30–50 ms of direct sound:
• Fuses perceptually with direct sound (not heard as separate echo)
• Direction is attributed to FIRST arriving sound (precedence)
• Level threshold: 10 dB later over 30 ms → separate echo perceived

PRACTICAL IMPLICATION:
Sound system design must ensure early reflections from walls arrive
within the 50 ms fusion window, or they cause intelligibility loss.
PA system delay lines: align delayed speakers so they don't create echoes
```

---

## Diffusion

Diffusion scatters sound energy in many directions, preventing flutter echo and discrete reflection problems.

```
DIFFUSERS:
1. Schroeder diffuser (QRD - Quadratic Residue Diffuser):
   Periodic array of wells with depths determined by quadratic residues mod prime p.
   All frequencies in design range diffused equally in one plane.
   Scattering coefficient ≈ 0.8–1.0 in design band.

2. Primitive Root Diffuser (PRD): Similar, 2D diffusion.

3. MLS (Maximum Length Sequence) diffuser: depth sequence based on MLS.

4. Profiled diffusers (convex/concave panels): broadband, less controlled.

DIFFUSION COEFFICIENT d(f):
d = 1: perfectly diffuse (all scattered energy in non-specular directions)
d = 0: perfectly specular (mirror reflection)

WHEN TO USE:
• Recording studio control room rear wall: diffusion instead of absorption
  → preserves energy, avoids acoustically dead space
• Concert hall side walls: diffusion creates acoustic width sensation
• Avoid flat parallel walls → standing wave build-up → use diffusion or splaying
```

---

## Decision Cheat Sheet

| Problem | Solution |
|---------|----------|
| Room too reverberant (speech muddy) | Add absorption (panels, carpet, upholstery) |
| Room too dry (music sounds dead) | Reduce absorption, add diffusion |
| Calculate RT60 quickly | Sabine: T60 = 0.161V/(Sᾱ) |
| More accurate RT60 (high absorption) | Eyring: use -ln(1-ᾱ) instead of ᾱ |
| Bass buildup in corners | Bass traps (thick porous, resonant panels) |
| Flutter echo between parallel walls | Break up with diffusers, or angle walls |
| Below what frequency does modal analysis apply? | f < f_S = 2000√(T60/V) |
| Measure RT60 | Fire starter pistol or sweep tone, measure decay curve |

---

## Common Confusion Points

**RT60 is frequency-dependent**: Sabine formula gives a single number, but real RT60 varies
with frequency. Upholstered seats absorb well at midrange but not at low frequencies → longer T60
at low frequencies. Always specify RT60 at octave bands (125 Hz to 4 kHz minimum).

**Sabine for highly absorptive rooms**: Sabine gives RT60 → 0 as ᾱ → 1, but Eyring gives -S·ln(1-1)
= -S·ln(0) = ∞, which is wrong. Eyring fails at ᾱ > 0.9. At near-total absorption, the room is
effectively anechoic and the formula doesn't apply.

**"Dead" vs "dry"**: Musicians often prefer "live" rooms for recording. Classical orchestras
need long RT60 for ensemble blend. Speech needs short RT60 for intelligibility. These are
opposite requirements — design for the intended use.

**Room modes ≠ resonances of room dimensions only**: Modes are at f_{nx,ny,nz} for any combination
of mode orders, not just f = c/(2L_x) etc. A room has hundreds of modes in the bass range,
creating a complex comb-filter response at different listening positions.
