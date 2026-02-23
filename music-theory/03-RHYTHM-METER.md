# Rhythm & Meter

## The Big Picture: Time Organization Hierarchy

```
TEMPO (BPM)
│  The absolute rate — how fast is the pulse?
│  ♩= 60 = 1 beat/second; ♩= 120 = 2 beats/second
│
├── BEAT UNIT (the "pulse" note value)
│   Quarter note (♩), half note (♩♩), eighth note (♪) — context dependent
│
├── METER = how beats group
│   │
│   ├── SIMPLE METER: each beat divides into 2
│   │   2/4 = 2 beats of ♩ each    (march)
│   │   3/4 = 3 beats of ♩ each    (waltz)
│   │   4/4 = 4 beats of ♩ each    (most common)
│   │
│   └── COMPOUND METER: each beat divides into 3
│       6/8  = 2 beats of dotted-♩ each    (each beat = ♪♪♪)
│       9/8  = 3 beats of dotted-♩ each
│       12/8 = 4 beats of dotted-♩ each
│
├── SUBDIVISION: how beat units divide
│   Simple duple: ♩ → ♪♪ (2 eighths per quarter)
│   Simple triple: ♩ → ♪♪♪ (but this makes it compound)
│   Triplets: 3 equal notes in the space of 2 (♩ triplet = 3 in space of 2)
│
└── PHRASE / HYPERMETER: how measures group
    Common: 2, 4, 8, 16-bar phrase units
    Irregular: 5, 7, 11 bars (Brubeck, Bartók, Balkan music)
```

**Mathematical structure:** Rhythm is about **rational relationships** between durations. A triplet is a 3:2 ratio. Polyrhythm is simultaneous different subdivisions. Metric modulation is a tempo change defined by a precise ratio.

---

## Simple vs Compound Meter

### Reading Time Signatures

```
TIME SIGNATURE FORMAT:
    3   ← numerator: beats per measure (or subdivisions)
    4   ← denominator: note value that gets one beat (4 = quarter note)

SIMPLE METER: top number = beats per bar
  2/4: strong-weak          (march, polka)
  3/4: strong-weak-weak     (waltz, minuet)
  4/4: strong-weak-semi-weak (most music)
  2/2 (alla breve "¢"): half note gets beat, faster feel than 2/4

COMPOUND METER: top number = number of SUBDIVISIONS (not beats!)
  6/8: 6 eighth notes per bar, but felt as 2 beats of 3 eighths each
  9/8: 3 beats of 3 eighths
  12/8: 4 beats of 3 eighths

Key test: how does it feel in performance?
  6/8 at slow tempo → counted as 6 (1-2-3-4-5-6)
  6/8 at fast tempo → counted as 2 (ONE-and-a-TWO-and-a)
  The "beat unit" at fast 6/8 is the dotted quarter (♩.)
```

### The Dotted Note Rule

```
A dot adds half the value of the note:
♩.  = ♩ + ♪  = 3 eighth notes = one compound beat
♩   = ♪ + ♪  = 2 eighth notes = one simple beat

In compound meter, the beat unit is ALWAYS a dotted note:
  6/8  → beat = ♩.  (dotted quarter)
  6/4  → beat = ♩.. (dotted half)
  9/8  → beat = ♩.  (dotted quarter, 3 per bar)
```

---

## Syncopation

Accent on a normally **weak** beat or between beats:

```
METRIC ACCENT STRUCTURE in 4/4:
  Beat:    1    2    3    4
  Weight:  STRONG weak SEMI  weak
           ↑              ↑
           Primary        Secondary

SYNCOPATION: accent displaced from strong beat position

Examples:
  Off-beat accent:    _ ♩ _ ♩ _ ♩ _ ♩ (2nd and 4th — the "backbeat" in rock/funk)
  Anticipation:       resolves chord one eighth-note early (lands on the "and" before the beat)
  Tie-over:           note starts on weak position, held through strong beat
  Hemiola:            implies 3-beat pattern inside 2-beat context (see below)

```

**Syncopation creates forward momentum.** It sets up an expectation (the pattern) then violates it (the accent displacement), creating tension that resolves when the pattern realigns.

---

## Hemiola

Superimposing 3 against 2 at the measure level:

```
HEMIOLA: 2 measures of 3/4 reinterpreted as 3 measures of 2/4
(or equivalently: 3 beats of 2 in the space of 2 beats of 3)

WRITTEN:
  Measure:   |  1  2  3  |  1  2  3  |
             |  ♩  ♩  ♩  |  ♩  ♩  ♩  |

PERFORMED:
  Implied:   |  1     2     3     |
             |  ♩.    ♩.    ♩.    |
             (three equal half-note values across two 3/4 bars)

USE: Cadential emphasis in Baroque, Classical, Renaissance
  Often at phrase endings to broaden the cadence
  Common in Handel, Brahms, and Baroque dance forms
  Also in Afro-Cuban clave patterns (see polyrhythm below)
```

---

## Polyrhythm

**Simultaneously different metric layers:**

### 3-against-2 (the fundamental polyrhythm)

```
3 AGAINST 2: the universal polyrhythm, foundation of West African and jazz rhythm

Fitting 3 equal notes against 2 equal notes of the same duration:
  Layer 1: ♩   ♩   ♩   (3 equally-spaced beats)
  Layer 2: ♩     ♩     (2 equally-spaced beats)

  1     2     3   |
  ●─────●─────●   ← 3 notes (each 1/3 of the measure)
  ●─────────●     ← 2 notes (each 1/2 of the measure)

Alignment:
  Beat   0       1/3     2/3      1
  3:    [●]      [●]      [●]    [●]
  2:    [●]               [●]    [●]
                 ↑ only the downbeat aligns

Mnemonic: say "nice cup of TEA" → "nice cup" = 3, "of TEA" = 2
```

### African Rhythmic Tradition and the Clave

```
The 3:2 clave pattern underlies Afro-Cuban music, and ultimately jazz rhythm:

SON CLAVE (3:2):
  Bar 1: ♩  . ♩ . ♩ . . .    (3 strokes: beats 1, and-of-2, beat-3-early)
  Bar 2: ♩ . . ♩ . . . .     (2 strokes: beats 1, 3)

RUMBA CLAVE: slight variation of bar 1 (and-of-2 shifts to and-of-2-and)

The clave pattern is the rhythmic "key" — everything locks to it.
Swap 3-side and 2-side = "clave reversal" — a common compositional device.
```

### 4-against-3, 4-against-5, etc.

```
General rule: m against n
  LCM(m,n) = total pulses in the grid before both realign
  3:2 → LCM=6, realign every 6 smallest units
  4:3 → LCM=12, realign every 12
  5:4 → LCM=20

West African drumming: 4+ independent rhythmic layers simultaneously
Brazilian samba: multiple percussion patterns creating a composite polyrhythm
Conlon Nancarrow: player piano studies at ratios like 5:3:4, 12:11:10
```

---

## Additive / Irregular Meters

Western metric tradition assumes beat groupings of 2 and 3. Additive meter combines them:

```
ADDITIVE METER: measure built from unequal beat-groups

5/4:  most common grouping: 2+3 or 3+2
      Take Five (Dave Brubeck): 3+2 per bar
      "Mars" from Planets (Holst): 5/4 throughout

7/8:  most common: 2+2+3 or 3+2+2 or 2+3+2
      "Money" (Pink Floyd): 7/4, counted as 4+3
      Balkan folk music: ubiquitous

Other Balkan meters:
  7/8:  2+2+3 or 3+2+2 (Bulgarian "Lesnoto")
  9/8:  2+2+2+3 or 3+2+2+2 (various)
  11/8: 2+2+3+2+2 or countless others
  13/8: even more variations
  15/8: Bartók's "Bulgarian Rhythm" studies

The key feature: unequal beat durations create a characteristic "limp"
  The short beats feel like rushing, the long beat like a catch
```

**Visualization:**

```
7/8 in 2+2+3:
  Short Short Long
    ♪+♪   ♪+♪  ♪+♪+♪
    1  2   3  4   5  6  7
    ───   ───   ───────

7/8 in 3+2+2:
  Long Short Short
  ♪+♪+♪  ♪+♪  ♪+♪
  1  2  3  4  5  6  7
  ───────  ───   ───
```

---

## Metric Modulation

A **tempo change defined by a precise ratio**, using a note value or subdivision from the old tempo as the pulse unit of the new tempo:

```
EXAMPLE: ♩ = 60 (old) → new tempo where the triplet eighth = new quarter

Old tempo: ♩ = 60 → eighth-note triplet = 60 × 3 = 180 triplet eighths/min
New tempo: old triplet eighth becomes new quarter → ♩ = 90

FORMULA:
  If old_BPM corresponds to beat unit Xold,
  and new_BPM corresponds to beat unit Xnew,
  and the "pivot" note = the old subdivision value v:
    new_BPM = old_BPM × (beats_in_v for old) / (beats_in_v for new)
```

**Key users:**
- Elliott Carter: metric modulation as primary structural device (String Quartets, Concertos)
- Brahms: hemiola and dotted-note tempo shifts
- Jazz: "double time" (subdivisions double, implied tempo doubles)

```
Common metric modulations:
  ♩. → ♩  : new quarter = old dotted quarter → ♩(new) = ♩.(old) → multiply BPM by 3/2
  ♩  → ♩. : new dotted quarter = old quarter → divide BPM by 3/2
  triplet ♩ → ♩ : triplet quarter becomes new quarter → multiply BPM by 2/3
```

---

## Groove and Microtiming

In notation, all notes are positioned on a grid. In performance, slight deviations from the grid create **groove** — the feeling that the music "locks in" and drives:

```
MICROTIMING PLACEMENT:
  ─────────────────────────────────────────────────────────
  Behind the beat: slightly after the grid position
    → Heavy, relaxed, "laid back"
    → Characteristic of: slow blues, soul, certain jazz feels
    → Example: Al Jackson Jr. (Booker T. & the MGs) drums

  On the beat: exactly at grid position
    → Driving, precise, mechanical (sequencers, classical)

  Ahead of the beat: slightly before the grid position
    → Urgent, pushing, exciting
    → Characteristic of: punk, certain gospel, excitement builds
  ─────────────────────────────────────────────────────────

SWING: elongating the first note of each pair, shortening the second
  Straight: ♪ ♪ ♪ ♪  (all eighth notes equal)
  Swing:    ♩♪ ♩♪     (first longer, second shorter, approximately triplet feel)
  Shuffle:  ♩♪ pattern is more pronounced, more extreme

  Swing ratio varies: from slight shuffle (1.1:1) to full triplet (2:1)
  Jazz swing is typically around 1.5:1 to 1.7:1 (context-dependent)
```

---

## Notation Shorthand

```
COMMON RHYTHMIC NOTATIONS:
  ♩   = quarter note = 1 beat in 4/4
  ♩.  = dotted quarter = 1.5 beats
  ♪   = eighth note = 0.5 beat
  ♪.  = dotted eighth = 0.75 beat
  𝅘𝅥𝅯   = sixteenth note = 0.25 beat

  Tuplets (ratios):
    ³♪♪♪ = triplet: 3 eighths in the space of 2 (1 beat)
    ⁵♩    = quintuplet: 5 notes in the space of 4
    ⁶♪    = sextuplet: 6 sixteenths in the space of 4

  Rests:
    𝄽   = quarter rest
    𝄾   = eighth rest
    𝄼   = half rest
    𝄻   = whole rest (also used for full measure rest in any meter)

  Special markings:
    > = accent mark (stress this note)
    ^ = marcato (heavy accent)
    sf/sfz = sforzando (sudden strong accent)
    fp = forte-piano (loud then immediately soft)
```

---

## Decision Cheat Sheet

| I hear/want... | Meter/concept |
|---------------|---------------|
| March-like, duple feel | 2/4 or 2/2 (alla breve) |
| Waltz, 3-beat swing | 3/4 |
| Most common default | 4/4 (common time) |
| Lilt, compound duple | 6/8 |
| Heavy lilt (jig feel) | 12/8 |
| Five-beat asymmetry | 5/4 (2+3 or 3+2) |
| Seven-beat Balkan feel | 7/8 (2+2+3 most common) |
| Two rhythms at once | Polyrhythm (specify ratio) |
| Cross-rhythm / hemiola | 3 against prevailing 2 |
| Precise tempo change | Metric modulation |
| Jazz eighth-note feel | Swing ratio ~1.5–1.7:1 |
| Laid-back groove | Behind the beat |
| Driving urgency | Ahead of the beat |

---

## Common Confusion Points

**6/8 vs 3/4:** Both have 6 eighth notes per measure, but they feel completely different. 6/8 groups as 2×3 (compound duple), 3/4 groups as 3×2 (simple triple). At the same BPM: 3/4 has 3 beats, 6/8 has 2. A famous ambiguous passage: Bernstein's "America" from West Side Story alternates between 6/8 and 3/4.

**Syncopation vs polyrhythm:** Syncopation displaces accents within a single metric layer. Polyrhythm maintains two independent metric layers simultaneously.

**Tuplets vs actual meter change:** A triplet (³) is a one-time subdivision of a beat into 3 rather than 2. It doesn't change the meter — it's a local exception. A metric modulation actually changes the tempo.

**Compound meter denominator trap:** 6/8 does NOT mean "6 beats of eighth notes." It means 6 eighth notes grouped as 2 compound beats. The "8" is the subdivision value, not the beat. At performance tempo, you count in 2, not 6.
