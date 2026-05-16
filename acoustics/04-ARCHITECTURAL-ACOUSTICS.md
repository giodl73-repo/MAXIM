---
maxim_schema: maxim.frontmatter.v1
id: maxim:acoustics:architectural-acoustics
kind: guide
module: acoustics
section: acoustics
title: Architectural Acoustics - A Layered Guide
status: source-custody
source_custody: partial
current_path: acoustics/04-ARCHITECTURAL-ACOUSTICS.md
canonical_path: acoustics/04-ARCHITECTURAL-ACOUSTICS.md
backsource_ids: [proof-backfill:acoustics:04-architectural-acoustics, git-history:acoustics:04-architectural-acoustics]
concepts: [architectural, acoustics]
root_concepts: [architectural, acoustics]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Architectural Acoustics — A Layered Guide

## The Big Picture

Architectural acoustics is the discipline of designing built spaces to achieve specific
acoustic performance goals — whether for orchestral richness, speech intelligibility,
or workplace privacy.

```
ARCHITECTURAL ACOUSTICS DESIGN SPACE
====================================================================

  Two axes: RT60 (reverberation time) and use case.

  SHORT RT60 (dry, clear) - high speech intelligibility:
    - Classroom, office, recording booth
    - Theater (RT60 ~1.0s)
  LONG RT60 (reverberant) - musical resonance:
    - Cathedral, large church
    - Concert hall (RT60 = 1.8-2.2s, optimized for orchestral music)
    - Opera house (RT60 ~1.4s)

  Background noise floor runs orthogonal: low NC -> high NC.
```

---

## Concert Hall Acoustics

Concert halls are among the most acoustically demanding buildings. Key metrics:

```
CONCERT HALL ACOUSTIC PARAMETERS

1. RT60 (Reverberation Time):
   Optimal for orchestral: 1.8–2.2 s at mid-frequencies (500-1000 Hz)
   RT60 at 125 Hz should be > RT60 at 500 Hz (bass "warmth")

2. EDT (Early Decay Time):
   Decay time of first 10 dB of decay × 6 (extrapolated to 60 dB)
   EDT < RT60 in a well-designed hall (early energy is clear)
   Subjective impression of reverberance correlates better with EDT than RT60

3. C80 (Clarity, 80 ms):
   C80 = 10·log₁₀[E_early / E_late]  dB
   E_early = energy in first 80 ms; E_late = energy after 80 ms
   C80 > 0 dB: clear (good for chamber music)
   C80 < 0 dB: reverberant (good for orchestral music, Brahms)
   Optimal: -2 to +2 dB for symphony

4. G (Strength / Loudness):
   G = 10·log₁₀[E_measured / E_free_field]  dB
   Measures how much the room amplifies the sound.
   Optimal: G > 4 dB (room should strengthen the orchestra)

5. LF / LFC (Lateral Energy Fraction):
   Fraction of early energy arriving from lateral directions.
   High LF → "envelopment" (feeling of being surrounded by sound)
   Optimal: LF > 0.2 for good spatial impression
```

### Hall Geometry

```
CONCERT HALL SHAPES

SHOEBOX (Rectangular):
  Audience area in a single rectangle, stage at one end,
  long parallel side walls.

VINEYARD (Terraced):
  Audience seating arranged in stepped terraces around the
  stage on multiple sides; angled walls and balcony fronts
  scatter sound rather than reflecting it parallel.

Shoebox advantages:            Vineyard advantages:
• Long parallel side walls     • More seats within similar RT60
• Strong lateral reflections   • Visual intimacy (all close to stage)
• High LF (envelopment)       • Good sightlines
• Classic: Boston Symphony,    • Good example: Berlin Philharmonie,
  Vienna Musikverein, Concertgebouw  LA Philharmonic (Walt Disney Hall)

Rule of thumb:
Hall width 15–25 m → strong lateral reflections from side walls
Stage opening: 18–22 m wide, 12–15 m high → projects sound into hall
Balcony overhang: limit depth (<= 1× height opening) to avoid cutting off late reverb
```

---

## Speech Intelligibility

### STI (Speech Transmission Index)

STI measures how well a room transmits speech. Range 0 (unintelligible) to 1 (perfect).

```
STI CALCULATION CONCEPT:

1. Transmit modulated test signal at 7 frequency bands (125 Hz – 8 kHz)
   and 14 modulation frequencies
2. Measure transmission index m(f, F) = modulation transfer function
   (ratio of received modulation depth to transmitted)
3. STI = weighted average over all m(f, F) values

PHYSICAL MEANING:
Any effect that reduces modulation depth reduces STI:
• Reverberation: fills in pauses (reduces modulation contrast)
• Background noise: adds constant energy floor
• Echo: creates competing signal

SHORTHAND FORMULA (approximate):
STI depends on:
  - Signal-to-noise ratio (SNR) at each frequency
  - RT60 at each frequency

For SNR > 18 dB and RT60 < 0.5s: STI > 0.7 (good-excellent)

STI RATING:
< 0.30: Bad      0.30–0.45: Poor
0.45–0.60: Fair  0.60–0.75: Good
> 0.75: Excellent

APPLICATIONS:
• Public address (PA) systems: STI requirement typically > 0.50 (fair-good)
• Emergency voice evacuation: IEC 60849 → STI ≥ 0.50
• Classroom design: ANSI S12.60 → STI ≥ 0.67
• Call centers, offices: STI ≥ 0.60
```

### Design for Speech Intelligibility

```
KEY PRINCIPLES:

1. Short RT60 (0.3–0.7 s at 500 Hz):
   RT60 < 0.5s → modulation preserved → STI high
   Use absorptive finishes, avoid parallel reflective surfaces

2. Low background noise:
   Background noise (HVAC, external) must be 15–20 dB below speech
   Design to NC 25–35 for classrooms (see below)

3. Avoid late echoes:
   Any distinct reflection > 50 ms after direct sound → echo → hurts STI
   Avoid deep overhanging balconies, flat rear walls (use diffusion)

4. Sound reinforcement delay alignment:
   Delay loudspeakers to arrive just after (or with) direct sound
   Listener perceives direction from first arrival (precedence effect)
```

---

## Recording Studio Design

### LEDE (Live End Dead End)

```
LEDE CONTROL ROOM CONCEPT (Chips Davis, 1980):

DEAD END (front):          LIVE END (rear):
  │                              │
  │  Absorptive treatment         Diffusive treatment
  │  (anechoic near monitors)     (reflective/diffusive rear wall)
  │                               QRD diffusers
  │  Near-field monitoring        Angled side panels
  │  possible                     Ceiling cloud (absorptive)
  │
  ├─────── MONITORING POSITION ──────────────────────────────►
  │        Engineer's desk
  │        Near mixing position: anechoic
  │        Far field: controlled early reflections from rear

BENEFITS:
• No early reflections that corrupt monitor listening
• Late energy from rear is diffuse → pleasant ambience, not coloring
• Stereo image clarity (no comb filtering from side walls)
• Low RT60 at mid/high freq (< 0.3s), controlled bass
```

### RFZ (Reflection-Free Zone)

```
RFZ: Alternative to LEDE. Create a reflection-free zone around the listening position.

Design: Calculate first-order reflections from all surfaces for the listening position.
        Angle surfaces so reflections go elsewhere (not to listening position).
        Absorb at predicted reflection points if angling isn't possible.

Critical surfaces: Console meter bridge, ceiling above engineer, side walls at first
                   reflection points, front wall behind monitors.
```

---

## Noise Criteria Curves

NC/NR curves specify the maximum background noise level acceptable for different spaces.

```
NC (Noise Criteria) CURVES — Balanced octave band limit

NC rating: the highest NC curve not exceeded in any octave band

NC-15: Broadcast studios, concert halls
NC-20: Recording studios, luxury residences
NC-25: Classrooms, bedrooms, private offices
NC-30: Conference rooms, theaters, churches
NC-35: Open-plan offices (sometimes too loud for concentration)
NC-40: Stores, restaurants, lobbies
NC-50: Computer rooms, machinery spaces
NC-65: Factory floor (hearing protection may be needed)

DESIGN RULE: HVAC system noise must be the dominant contributor.
Structural noise from elevators, mechanical rooms must be below NC target.
```

---

## Sound Transmission Loss (STC)

```
STC (Sound Transmission Class): single-number rating of how well a construction
assembly blocks airborne sound.

STC calculation:
1. Measure transmission loss TL(f) = 10·log₁₀(incident power / transmitted power)  dB
2. Fit STC reference curve to measured data
   (max sum of deficiencies ≤ 32 dB, max single deficiency ≤ 8 dB)
3. STC = reference curve value at 500 Hz

COMMON CONSTRUCTIONS:
Assembly                              STC
─────────────────────────────────────────────────────────
Single sheet drywall (1/2")          28
Double drywall (2×1/2" on each side) 40
Decoupled double stud wall           50–60
Office drywall partition (std)       35–42
Concrete masonry unit (CMU) 8"      48–55
Laminated glass (10mm)              36
Double glazed window (air gap)      28–35
Heavy concrete slab                 55–60

MASS LAW:
TL ≈ 20·log₁₀(m·f) - 47  dB    (for limp mass, below coincidence)
m = surface mass density (kg/m²), f = frequency

→ Doubling mass: +6 dB TL at any frequency
→ Doubling frequency: +6 dB TL
Bass is hardest to block (low f → low TL)
```

---

## Cross-References

- `acoustics/03-ROOM-ACOUSTICS.md` — RT60, reflections, and room-field mechanics.
- `architecture/03-ENVIRONMENTAL.md` — acoustic comfort as part of environmental design.
- `music-theory/01-PITCH-SCALES.md` — musical-performance requirements that drive hall acoustics.

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether a concert hall supports orchestra | RT60, lateral fraction, and early-reflection geometry | Long reverberation without lateral energy can sound large but not enveloping |
| Whether speech intelligibility is poor | RT60, SNR, STI, and echo paths | Shortening RT60 is not enough if HVAC noise or late echoes dominate |
| Whether STI is acceptable | Measured STI at listener positions | STI is in-room intelligibility; it is not wall isolation |
| Whether HVAC noise is the culprit | NC curve by octave band | A single broadband dB value can hide low-frequency rumble |
| Whether office isolation is adequate | STC assembly plus flanking inspection | The weakest path may be ceiling plenum, slab, duct, or door, not the partition |
| Whether a recording room is controlled | First-reflection points, RT60, and bass decay | A short midband RT60 can still have uncontrolled low-frequency ringing |
| Whether bass treatment is effective | Waterfall decay and corner pressure maxima | Thin foam is not a bass trap; depth or resonance is required |
| Whether shoebox or vineyard geometry fits | Program, seat count, lateral energy, and intimacy goals | Hall form is a tradeoff between envelopment, capacity, sightlines, and construction constraints |

---

## Common Confusion Points

**STI vs STC**: STI (0–1) measures how well a room transmits intelligible speech to a listener
in the same space. STC measures how well a wall blocks sound from one space to another.
They measure completely different things.

**NC is not just one number**: NC is a family of curves. A single measurement at one frequency
can't define NC — you need octave band measurements. A system might meet NC-30 at midrange
but fail it at low frequencies (100–250 Hz) where HVAC rumble lives.

**Concert hall is NOT the right model for all music**: Jazz clubs prefer shorter RT60 (~0.8–1.2 s)
for clarity and intimacy. Pipe organs in churches benefit from very long RT60 (3–5 s) to sustain
chords. Recording studios need controlled acoustic environments, not optimized ones.

**Flanking transmission often dominates**: A partition with STC 50 is useless if sound travels
via the floor slab, ceiling plenum, or HVAC ducts (flanking paths) with STC 30. Airborne and
structure-borne flanking paths must all be treated.
