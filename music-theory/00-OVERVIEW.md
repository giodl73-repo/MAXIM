# Music Theory — Overview

## The Big Picture: Physics → Perception → Structure

```
PHYSICS                   PERCEPTION              MUSIC THEORY
─────────────────────     ──────────────────────  ────────────────────────────
Vibrating air column  →   Cochlea frequency map → PITCH (Hz → note name)
  f = 440 Hz               Logarithmic response    A4, middle C, etc.
  f = 880 Hz (2:1)         Equal semitones feel    OCTAVE equivalence
  f = 660 Hz (3:2)         equal-sized             INTERVAL perception

Fourier partials      →   Timbre                → ORCHESTRATION
  fundamental              Harmonic series          which instruments blend
  overtones                brightness/darkness      doubling principles

Periodic pulse        →   Beat perception       → RHYTHM / METER
  tempo (BPM)              grouping into beats      time signatures
  subdivision              strong/weak accents      syncopation

Simultaneous pitches  →   Consonance/dissonance → HARMONY
  frequency ratios          roughness (Helmholtz)    chord function
  2:1, 3:2, 4:3             fusion                   tension → resolution

Sound through time    →   Pattern memory        → FORM
  recurrence               expectation/violation    AABA, sonata, fugue
  variation                resolution               development arc
```

The discipline has **two faces**: an empirical science (acoustics, psychoacoustics) and a prescriptive grammar (the "rules" of common-practice Western music). This library covers both, with mathematical structure throughout.

**Bridge:** The 12-TET pitch system is isomorphic to **Z₁₂** (integers mod 12). Transposition is addition, inversion is negation. Set-theoretic pitch-class analysis is literally applying group theory to music.

---

## The Frequency Foundation

### Octave and the Harmonic Series

Every vibrating body produces a **fundamental** and **overtones** at integer multiples:

```
STRING VIBRATION — HARMONIC SERIES
───────────────────────────────────────────────────────────
Harmonic   Frequency ratio   Interval above fundamental
────────   ───────────────   ──────────────────────────
  1st       f₀  × 1          Unison (fundamental)
  2nd       f₀  × 2          Octave
  3rd       f₀  × 3          Octave + perfect fifth
  4th       f₀  × 4          Two octaves
  5th       f₀  × 5          Two octaves + major third
  6th       f₀  × 6          Two octaves + perfect fifth
  7th       f₀  × 7          Two octaves + minor seventh*
  8th       f₀  × 8          Three octaves
  ─────────────────────────────────────────────────────
  *7th harmonic is notably flat relative to 12-TET — hence
   the "blue note" in blues/jazz, and why dominant 7ths feel
   so natural (7th partial suggests ♭7).
```

This harmonic series is the **physical origin** of why a perfect fifth (3:2) and major third (5:4) sound consonant — they lock onto low-numbered partials.

### Engineering Bridge: The Harmonic Series as Fourier Decomposition

```
MUSICAL CONCEPT                  SIGNAL PROCESSING EQUIVALENT
──────────────────────────────────────────────────────────────────────────
Harmonic series (partials)       Fourier series of a periodic waveform
  f₀, 2f₀, 3f₀, ...            → any periodic signal = Σ aₙ sin(nωt + φₙ)

Timbre (bright, dark, reedy)     Spectral envelope (magnitude spectrum shape)
  violin ≠ flute at same pitch   → different aₙ coefficients, same f₀

Consonance (sounds "pure")       Shared spectral components reinforce
  3:2 fifth: every 3rd partial   → partials coincide, no beating
  of upper note = every 2nd
  of lower note

Dissonance (sounds "rough")      Beating = amplitude modulation
  closely-spaced partials         → Δf small → AM at frequency Δf
  produce roughness               → ear perceives this as dissonance

Orchestral blend                 Spectral overlap of two signals
  horn + viola blend well         → similar spectral envelope shapes sum cleanly
  trumpet + flute clash           → dissimilar envelopes create spectral gaps
```

Helmholtz's "On the Sensations of Tone" (1863) derived these connections explicitly: consonance is spectral reinforcement, dissonance is beating between near-frequency partials, and timbre is the Fourier spectrum of the waveform. The entire psychoacoustic foundation of music theory is Fourier analysis applied to perception.

### Just Intonation vs. 12-TET: The Comma Problem

**Just intonation** tunes intervals to pure integer ratios:

| Interval | JI ratio | Frequency factor |
|----------|----------|-----------------|
| Unison | 1:1 | 1.000 |
| Major second | 9:8 | 1.125 |
| Major third | 5:4 | 1.250 |
| Perfect fourth | 4:3 | 1.333 |
| Perfect fifth | 3:2 | 1.500 |
| Major sixth | 5:3 | 1.667 |
| Major seventh | 15:8 | 1.875 |
| Octave | 2:1 | 2.000 |

**Problem:** Stack 12 pure fifths (3:2)¹² and you should arrive at 7 octaves (2:1)⁷. But:

```
12 pure fifths: (3/2)¹² = 129.746...
7 octaves:       2⁷     = 128.000

Ratio: 129.746/128 = 1.01364...
This gap = the PYTHAGOREAN COMMA (≈ 23.46 cents)
```

The circle of fifths **doesn't close** in pure intonation. You can't modulate to all 12 keys without retuning.

**12-TET solution:** Set every semitone to exactly ²¹²√2 = 1.05946..., distributing the comma equally. Every fifth is now 1.4983... (2 cents flat of pure). All keys equally in tune (and equally slightly out of tune).

```
JI perfect fifth:   702.0 cents (pure, locked to 3:2)
12-TET fifth:       700.0 cents (2 cents flat — imperceptible in isolation)
Pythagorean comma:   23.5 cents (the total "fudge" spread over 12 fifths)
```

---

## The Circle of Fifths

The primary organizing structure of tonal music — and a group-theoretic object:

```
                    C (0 sharps/flats)
               F ───────────── G
          (1♭)                     (1♯)
        B♭                             D
      (2♭)                               (2♯)
       E♭                               A
      (3♭)                               (3♯)
        A♭                             E
          (4♭)                     (4♯)
               D♭ ──────────── B
                    G♭/F♯
                   (6♭/6♯)
                   enharmonic

Moving CLOCKWISE: add one sharp (or remove one flat) — go UP a fifth
Moving COUNTER-CLOCKWISE: add one flat (or remove one sharp) — go UP a fourth
```

**Key signatures by position:**

| Clockwise | Sharps | Key | Counter-clockwise | Flats |
|-----------|--------|-----|-------------------|-------|
| C | 0 | C major / a minor | C | 0 |
| G | 1♯ (F♯) | G major / e minor | F | 1♭ (B♭) |
| D | 2♯ | D major / b minor | B♭ | 2♭ |
| A | 3♯ | A major / f♯ minor | E♭ | 3♭ |
| E | 4♯ | E major / c♯ minor | A♭ | 4♭ |
| B | 5♯ | B major / g♯ minor | D♭ | 5♭ |
| F♯/G♭ | 6♯/6♭ | enharmonic pivot | G♭ | 6♭ |

**Why fifths?** The most structurally important harmonic relationship after the octave (2:1) is the fifth (3:2). Stacking fifths generates all 12 pitch classes before repeating. The circle is Z₁₂ under mod-7 addition (adding a fifth = adding 7 semitones mod 12).

---

## Western Music Historical Arc

```
ERA           APPROX DATES    KEY FEATURES                EXEMPLARS
──────────────────────────────────────────────────────────────────────────
Medieval      850–1400        Plainchant, organum,        Hildegard von Bingen
                              modal (not tonal),          Machaut
                              no regular barlines

Renaissance   1400–1600       Polyphony matures,          Palestrina, Byrd,
                              four-part vocal texture,    Lassus
                              modal → tonal transition,
                              madrigal, motet

Baroque       1600–1750       Functional tonality         Bach, Handel,
                              established, continuo,       Vivaldi, Monteverdi
                              fugue, concerto grosso,
                              equal temperament adopted

Classical     1750–1820       Sonata form, symphony,      Haydn, Mozart,
                              string quartet,              early Beethoven
                              clarity + balance,
                              functional harmony peaks

Romantic      1820–1900       Chromatic harmony,          Schubert, Chopin,
                              extended forms,              Wagner, Brahms,
                              program music,               Mahler, Liszt
                              nationalism, large orch.

Late Romantic 1880–1910       Tonal dissolution begins,   Strauss, Elgar,
/ Post-Rom.                   extreme chromaticism         Reger, late Mahler

Impressionist 1890–1920       Parallel motion, color      Debussy, Ravel
                              over function, modes,
                              whole-tone/pentatonic

20th Century  1900–2000       Atonality, serialism,       Schoenberg, Bartók,
(see 09)                      neo-classicism,              Stravinsky, Cage,
                              minimalism, spectralism      Reich, Messiaen

Contemporary  2000–           Spectralism, microtonality, Saariaho, Lachenmann,
                              electronics + live,          Ligeti legacy,
                              post-minimalism              crossover with jazz/pop
```

---

## Non-Western Music Systems

The Western system is one of many. Three major traditions:

### Indian Classical Music — Raga System

```
STRUCTURE HIERARCHY
────────────────────────────────────────────────────────
Shruti (22 microtones)  — the perceptual pitch universe
    ↓
Swara (7 named degrees + variants)  — sa re ga ma pa dha ni
    ↓
That (10 parent scales)  — like modal parent scales
    ↓
Raga (hundreds of ragas)  — specific ascending/descending
    rules + characteristic phrases + time/season of day
    ↓
Performance = alap (unmetered) → jor → jhala → gat (with tala)
```

**Key concepts:**
- **Raga** is not just a scale — it's a melodic grammar with obligatory phrases (pakad), characteristic ornaments (gamak, meend), and emotions (rasa)
- **Tala** = rhythmic cycle (e.g., teental = 16 beats in 4×4, rupaktal = 7 beats in 3+2+2)
- **Shruti** microtonality — the octave divided into 22 unequal intervals (not 12)
- **Improvisation** within strict structural constraints — jazz has structural parallels

### Arabic/Persian Music — Maqam System

```
MAQAM STRUCTURE
────────────────────────────────────────────────────────
Ajnas (tetrachords/trichords) are the building blocks:
  Rast jins:    W  W  ¾  (where ¾ = 3/4-tone, between semitone and whole tone)
  Hijaz jins:   ½  1½  ½  (augmented second characteristic sound)
  Bayati jins:  ¾  ¾  W  (two neutral seconds)

Maqam = lower jins + upper jins + characteristic movements
  ~50+ named maqamat, each with emotional/spiritual associations (tarab)
```

**Key features:**
- **Neutral intervals** (~3/4 tone, ~150 cents) — between the Western semitone (100c) and whole tone (200c)
- **Microtonal inflection** during performance (not fixed pitches)
- **Modulation between maqamat** within a piece (not to different keys)
- Used across Arabic, Turkish, Persian, and Greek musical traditions

### Indonesian Gamelan — Tuning as Identity

```
GAMELAN STRUCTURE
────────────────────────────────────────────────────────
Two tuning systems:
  Slendro: 5-note scale, roughly equal steps (~240 cents each)
  Pelog:   7-note scale (5 used), unequal — includes both small and large steps

Key features:
  ┌──────────────────────────────────────────────────┐
  │ Each gamelan ensemble is individually tuned      │
  │ Two gamelans cannot play together — no           │
  │ universal pitch standard                         │
  │ Tuning is the ensemble's "fingerprint"           │
  └──────────────────────────────────────────────────┘
Colotomic structure: stratified layers at different speeds
  (bonang/saron play at fast speed, gong marks slow phrase boundaries)
Heterophony: same melody simultaneously in different elaborated forms
```

---

## Module Map

```
SESSION 13 — MUSIC THEORY
│
├── 00-OVERVIEW.md (this file)
│     Physics pipeline, JI vs 12-TET, circle of fifths, historical arc, non-Western
│
├── 01-PITCH-SCALES.md
│     12-TET math, interval table, major/minor scale construction, all 12 keys
│
├── 02-MODES-PENTATONIC.md
│     Church modes, brightness ranking, pentatonic, whole-tone, octatonic,
│     modal jazz, world music modes
│
├── 03-RHYTHM-METER.md
│     Pulse/tempo, simple/compound meter, syncopation, polyrhythm, additive meters,
│     metric modulation, groove microtiming
│
├── 04-HARMONY-CHORDS.md
│     All triad/seventh types, extensions, inversions, Roman numeral analysis,
│     chord function, secondary dominants, modal mixture
│
├── 05-VOICE-LEADING-COUNTERPOINT.md
│     SATB rules, cadence types, five species, suspensions, fugue anatomy
│
├── 06-TONAL-HARMONY.md
│     Modulation types, augmented sixths, Neapolitan, Tristan chord,
│     Romantic chromaticism, Debussy stasis
│
├── 07-FORM-ANALYSIS.md
│     Binary/ternary, 12-bar blues, AABA, sonata form, symphony archetype
│
├── 08-ORCHESTRATION.md
│     Instrument ranges, transposing instruments, string techniques, score reading
│
└── 09-20TH-CENTURY-JAZZ.md
      Twelve-tone, serialism, aleatoric, minimalism, jazz chord-scale theory,
      tritone substitution, Coltrane changes
```

**Bridge to notation basics:** `codes/07-MUSICAL-NOTATION.md` covers staff, clefs, note values, key signatures, and time signatures — read that first if notation is unfamiliar.

**Computational connections not covered in this series:** Music Information Retrieval (MIR) — chord recognition via chromagram analysis (STFT → 12-bin pitch-class histogram), beat tracking (onset detection → autocorrelation), automatic transcription (spectrogram → note events) — bridges signal processing and ML directly. See `signal-processing/` for STFT foundations. Schenkerian hierarchical analysis is discussed in `07-FORM-ANALYSIS.md` as the parse-tree bridge.

---

## Quick Concept Index

| Concept | Core idea | See |
|---------|-----------|-----|
| 12-TET | 12th root of 2 per semitone | 01 |
| Interval | Named distance between pitches | 01 |
| Scale | Ordered pitch collection + pattern | 01 |
| Mode | Rotation of a parent scale | 02 |
| Meter | Grouping of beats | 03 |
| Triad | 3-note chord (root/3rd/5th) | 04 |
| Seventh chord | Triad + 7th degree | 04 |
| Voice leading | Smooth part motion between chords | 05 |
| Counterpoint | Independent simultaneous lines | 05 |
| Modulation | Shifting tonal center | 06 |
| Sonata form | 3-part arch: exposition/dev/recap | 07 |
| Transposing instrument | Written pitch ≠ concert pitch | 08 |
| Twelve-tone | Serialized pitch rows (Schoenberg) | 09 |
| Tritone substitution | Dominant substitute a tritone away | 09 |

---

## Common Confusion Points

**JI vs 12-TET: which is "correct"?**
Neither. JI has pure intervals but can't modulate freely. 12-TET enables modulation at the cost of slightly impure intervals. Singers and unfretted string players naturally drift toward JI; fixed-pitch instruments must use 12-TET. Barbershop quartets and a cappella choirs lock to JI in sustained chords — you can hear the difference.

**Enharmonic equivalence:** C♯ and D♭ are the same key on a piano (12-TET) but different notes in tonal harmony — they resolve differently (C♯ wants to go up to D; D♭ wants to go down to C). Context determines the correct spelling.

**"Key" vs "scale" vs "mode":** A key implies tonal center + functional harmony. A scale is an ordered pitch set. A mode is a rotation of a parent scale with its own tonal color. C major (key) uses the C major scale; D Dorian uses the same pitches (as C major) but centers on D.

**The "relative" vs "parallel" minor confusion:** C major's *relative* minor is A minor (same notes, different center). C major's *parallel* minor is C minor (same center, different notes — 3 new flats). These are completely different relationships.
