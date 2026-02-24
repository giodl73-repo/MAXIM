# Musical Acoustics — A Layered Guide

## The Big Picture

Musical instruments are physical systems that convert mechanical energy into structured
acoustic radiation. The physics determines timbre, pitch stability, and playing technique.

```
INSTRUMENT ACOUSTIC TAXONOMY
════════════════════════════════════════════════════════════════════

CHORDOPHONES (string vibration):
  Transverse string vibration → sound box radiation
  Examples: violin, guitar, piano, harp, clavichord

AEROPHONES (air column resonance):
  Reed, lips, or edge-tone → air column resonance → bell radiation
  Examples: clarinet, oboe, trumpet, flute, organ pipe

MEMBRANOPHONES (membrane vibration):
  Struck/scraped membrane → body resonance → radiation
  Examples: drum, tabla, timpani, kazoo

IDIOPHONES (body vibration):
  Struck/scraped body resonates directly
  Examples: xylophone, marimba, glockenspiel, cymbals, bells, wine glass

ELECTROPHONES: electronic instruments (not included here)

GENERAL PRINCIPLE FOR ALL:
┌──────────┐    coupling    ┌──────────┐    radiation    ┌──────────┐
│  Driver  │ ─────────────► │ Resonator│ ──────────────► │  Sound   │
│(energy   │               │ (selects  │                 │  Field   │
│ source)  │               │ harmonics)│                 │          │
└──────────┘               └──────────┘                 └──────────┘
  Bow/pluck/blow             Strings/tube/membrane/plate   Air radiation
```

---

## Vibrating String

The foundation of all chordophone acoustics.

```
VIBRATING STRING FUNDAMENTALS

For a string of length L, linear mass density μ, tension T:

Wave speed:  c_s = √(T/μ)     (m/s)

Fundamental mode (1/2 wavelength = L):
  f₁ = c_s / (2L) = (1/2L)·√(T/μ)

Harmonic series:
  fₙ = n · f₁    n = 1, 2, 3, ...  (exactly harmonic, IDEAL string)

STRING MODES (visualized):

n=1 (fundamental):  ─╭─────────────╮─   f₁
n=2 (2nd harmonic): ─╭──╮ ╭──╮─────   2f₁  (node in center)
n=3:                ─╭──╮─╭──╮─╭──╮─  3f₁  (two nodes)

TUNING:
Increase T → higher pitch (tightening peg)
Increase L → lower pitch (open string lower than fretted)
Increase μ → lower pitch (wound strings for bass)
```

**Bowing physics**:
```
STICK-SLIP MECHANISM (Helmholtz motion)

Bow hair (rosin-coated) sticks to string:
  1. STICK phase: string accelerates with bow
  2. SLIP phase: string snaps back (faster than bow)
  3. Kink travels around string at wave speed c_s
  4. Repeats at fundamental frequency

Contact point (β = distance from bridge / string length):
  β → 0 (near bridge): more scratchy, high harmonics, bright tone
  β → 0.5 (middle): fewer harmonics, flute-like tone
  β = 1/n eliminates nth harmonic (bowing at a node of that harmonic)

BOW SPEED × PRESSURE: Quality window — too fast or too slow → non-periodic scratching
```

---

## Wind Instrument Resonance

Wind instruments use air column resonances. The physics differs for open vs. closed tubes.

```
AIR COLUMN MODES

OPEN TUBE (open both ends — e.g., flute, open organ pipe):
Boundary conditions: pressure nodes at both ends (p = 0)
Actually: velocity antinodes at both ends

Resonant frequencies: fₙ = n·c/(2L)    n = 1, 2, 3, ...
(all harmonics, same as open string)

CLOSED TUBE (closed one end — e.g., clarinet, closed organ pipe):
One end: pressure antinode (closed), one end: pressure node (open)

Resonant frequencies: fₙ = (2n-1)·c/(4L)    n = 1, 2, 3, ...
= c/(4L), 3c/(4L), 5c/(4L), ...
= f₁, 3f₁, 5f₁, ...   (ODD harmonics only!)

FREQUENCY COMPARISON:
Open pipe length L:    f₁ = c/(2L) = 343/(2×0.3m) = 572 Hz  (e.g., piccolo range)
Closed pipe length L:  f₁ = c/(4L) = 143 Hz     (one octave lower for same length)
→ CLARINET plays one octave lower than equivalent flute length because it's a closed tube
→ CLARINET overblows to 3rd harmonic (12th above fundamental = 1 octave + 5th)
→ FLUTE overblows to 2nd harmonic (octave)
```

### Reed and Lip Oscillators

```
REED MECHANISM:
Reed acts as a pressure-controlled valve:
• High pressure pulse arrives at reed → reed blows closed → pulse reflects
• At specific flow rate, reed oscillates in sync with tube resonance

BERNOULLI EFFECT + REED STIFFNESS → SELF-SUSTAINING OSCILLATION:
At playing frequency, tube resonance provides feedback to control reed motion.
The player selects different harmonics by overblowing (increasing pressure/embouchure).

LIP BUZZ (brass instruments):
Lips work similarly to a reed — mechanical resonance coupled to air column.
Tube shape (conical vs cylindrical) changes available harmonics.
• Cylindrical bore (trombone, trumpet): odd+even harmonics, strong fundamental
• Conical bore (saxophone, french horn, flugelhorn): all harmonics, different timbre
```

---

## Percussion Instruments

```
DRUMS AND MEMBRANES

Circular membrane modes (Bessel functions!):
Mode frequencies: f_{m,n} = (α_{m,n} / (2πa)) · √(T/σ)
where α_{m,n} = nth zero of m-th Bessel function J_m
      a = radius, T = tension, σ = surface mass density

NODAL DIAMETERS AND CIRCLES:
(0,1): 1.000 f₁     (no node lines)
(1,1): 1.594 f₁     (1 nodal diameter)
(2,1): 2.136 f₁     (2 nodal diameters)
(0,2): 2.295 f₁     (1 nodal circle)
(3,1): 2.653 f₁
...

CRITICAL POINT: Mode frequencies are NOT harmonically related!
Unlike strings, membrane modes are inharmonic (non-integer ratios).
→ Drums have indefinite pitch (no clear fundamental)
→ Tabla and timpani use physical constraints to emphasize near-harmonic modes

TIMPANI: Kettle drum — bowl cavity tunes the membrane by damping non-harmonic modes,
         emphasizing (1,1), (2,1), (3,1) which are approximately harmonic.
         Result: definite pitch, can be tuned.
```

**Bars and plates (idiophones)**:
```
XYLOPHONE AND MARIMBA (bars):

Free-free bar (Euler-Bernoulli beam theory):
f₁ = (3.011² / (2π)) · (r/L²) · √(E/ρ)   (for circular bar, r = radius)
Higher modes: f₂ = 2.76 f₁, f₃ = 5.40 f₁   (inharmonic)

TUNING: Undercutting the bar center raises f₁ (lowers relative to higher modes)
        Undercutting creates:
        f₂ ≈ 4f₁  (2 octaves above fundamental)
        f₃ ≈ 10f₁
        → Marimba undercutting creates near-harmonic relationship
```

---

## Piano Inharmonicity

```
PIANO STRING INHARMONICITY

Real strings have finite stiffness (not perfectly flexible).
Bending stiffness introduces inharmonicity:

f_n = n·f₁·√(1 + B·n²)

where B = inharmonicity coefficient
      B = (π·d·E) / (64·T·L²)   × (d²)

For typical piano string:
  B ≈ 10⁻⁴ to 10⁻³ (treble strings worse than bass)

AUDIBLE CONSEQUENCES:
• Treble strings: f₂ is SHARP of 2×f₁ → beats when two strings hit same note
• Bass strings: wound (reduce B) but still some inharmonicity
• Piano tuning: stretched tuning — treble tuned slightly sharp, bass slightly flat
  to match perceived pitch (matching inharmonic partials)
  "Railsback curve" describes the empirical stretched tuning

"PIANO TUNING IS NOT EQUAL TEMPERAMENT":
Concert grand A=440 Hz but A5 is not 880 Hz — it's 881–882 Hz due to stretched tuning.
This matches perceptual octave equivalence for inharmonic strings.
```

---

## Voice Source-Filter Model

```
VOICE PRODUCTION (source-filter model, Fant 1960)

SOURCE: Vocal folds (glottis)
  • Vibrate at fundamental frequency f₀ (100–300 Hz speaking, up to 1200 Hz singing)
  • Create periodic pulse train: rich harmonic spectrum
  • Each harmonic: amplitude falls ~12 dB/octave (source spectrum slope)

VOCAL TRACT FILTER:
  • Tube ~17 cm, area function varies with tongue/jaw/lip position
  • Resonances (formants) amplify selected harmonics
  • Filter is adjustable in real time → different vowels

FORMANTS:
  F1 (500–1000 Hz): mainly jaw height / tongue body height
  F2 (1000–3000 Hz): mainly tongue front/back position
  F3 (2500–3500 Hz): lip/tongue shape
  F4, F5: larynx, pharynx shape

VOWEL IDENTITY = formant pattern:
  /a/ (as in "father"): F1≈800 Hz, F2≈1200 Hz  (open, back)
  /i/ (as in "see"):    F1≈300 Hz, F2≈2700 Hz  (close, front)
  /u/ (as in "who"):    F1≈300 Hz, F2≈800 Hz   (close, back)

SINGER'S FORMANT (~3 kHz cluster):
  Trained opera singers develop extra resonance at 2500–3500 Hz
  → Voice "cuts through" orchestra (which has less energy there)
  → Amplitude boost without microphone
  Physical cause: clustering of F3–F5 by singing technique
```

---

## Decision Cheat Sheet

| Instrument | Key Physics |
|------------|-------------|
| Why does bass guitar need longer strings? | Longer L → lower f₁ = (1/2L)√(T/μ) |
| Clarinet vs flute same length, different pitch? | Clarinet: closed tube → f₁ = c/(4L); flute: open → c/(2L) |
| Why does piano need "stretched" tuning? | Inharmonicity of stiff strings (f_n ≠ n·f₁) |
| Why do drums have indefinite pitch? | Membrane modes have inharmonic frequency ratios (Bessel zeros) |
| How does a singer project over an orchestra? | Singer's formant cluster at 3 kHz |
| Why does a thick string sound lower? | Larger μ → lower √(T/μ) → lower c_s and f₁ |

---

## Common Confusion Points

**"Harmonic" vs "overtone" vs "partial"**: Harmonic = integer multiple of fundamental (2f₁, 3f₁, ...).
Partial = any component of the spectrum. Overtone = partial above the fundamental (1st overtone = 2nd harmonic).
Piano and bell tones are inharmonic — their partials are NOT integer multiples.

**Open tube fundamental is twice the frequency of same-length closed tube**: Not a paradox.
Open tube has two open ends (both pressure nodes) → half wavelength fits in length L → f₁ = c/(2L).
Closed tube has one node and one antinode → quarter wavelength in L → f₁ = c/(4L). Factor of 2.

**Singing and speaking use the same source but different filter**: Same vocal folds; different
vocal tract shape. The "source" (glottal pulse) doesn't change much between vowels — the vocal
tract formant pattern changes everything.

**Why does a stopped horn play different notes?**: Inserting a hand partially into the bell
changes the effective tube length and shifts resonances. Complete stopping raises pitch ≈ semitone
(resonance shift from open to closed boundary condition).
