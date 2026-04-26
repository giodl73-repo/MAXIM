# Western Musical Notation — Complete Reference

## The Big Picture

Western musical notation is a **two-dimensional symbolic system** that encodes five simultaneous streams of information: pitch (which note), duration (how long), timing (where in the measure), dynamics (how loud), and articulation (how to attack). It evolved over ~1,000 years from Gregorian neumes to the modern five-line staff.

```
┌──────────────────────────────────────────────────────────────────┐
│              MUSICAL NOTATION INFORMATION LAYERS                 │
│                                                                  │
│  Horizontal axis = TIME progression (left → right)               │
│  Vertical axis   = PITCH (up = higher frequency)                 │
│                                                                  │
│  A single page of orchestral score encodes simultaneously:       │
│                                                                  │
│  PITCH:         Which note? (staff position + accidentals)       │
│  DURATION:      How long? (note head shape + stem + flags/beams) │
│  TIMING:        When? (position in measure, time signature)      │
│  DYNAMICS:      How loud? (pp to ff, hairpin crescendo)          │
│  ARTICULATION:  How attacked? (staccato, legato, accent, slur)   │
│  TEMPO:         How fast? (beats per minute, Italian terms)      │
│  EXPRESSION:    What character? (espressivo, con fuoco, etc.)    │
│                                                                  │
│  Information density rivals: a single measure of orchestral      │
│  score can specify 30+ independent parameters simultaneously.    │
└──────────────────────────────────────────────────────────────────┘
```

---

## The Staff System

### Basic Staff

```
┌──────────────────────────────────────────────────────────────────┐
│                    THE FIVE-LINE STAFF                           │
│                                                                  │
│  Line 5 ─────────────────────────────────────────────────────    │
│  Space 4                                                         │
│  Line 4 ─────────────────────────────────────────────────────    │
│  Space 3                                                         │
│  Line 3 ─────────────────────────────────────────────────────    │
│  Space 2                                                         │
│  Line 2 ─────────────────────────────────────────────────────    │
│  Space 1                                                         │
│  Line 1 ─────────────────────────────────────────────────────    │
│                                                                  │
│  Notes sit on lines or in spaces.                                │
│  Notes above/below staff use ledger lines (short temporary       │
│  extensions of the staff up or down).                            │
│                                                                  │
│  Middle C (C4) is on the FIRST LEDGER LINE BELOW treble clef     │
│  and on the FIRST LEDGER LINE ABOVE bass clef.                   │
└──────────────────────────────────────────────────────────────────┘
```

### The Five Standard Clefs

The clef fixes which pitch each line/space represents:

```
┌──────────────────────────────────────────────────────────────────┐
│                        CLEFS                                     │
│                                                                  │
│  TREBLE CLEF (G clef):                                           │
│  — The curl of the symbol wraps around line 2 → that line = G4   │
│  — Used for: violin, flute, clarinet, trumpet, guitar*, voice    │
│  — Lines bottom up: E G B D F ("Every Good Boy Does Fine")       │
│  — Spaces bottom up: F A C E ("FACE")                            │
│                                                                  │
│  BASS CLEF (F clef):                                             │
│  — The two dots straddle line 4 → that line = F3                 │
│  — Used for: bass, cello (low range), trombone, tuba, piano LH   │
│  — Lines bottom up: G B D F A ("Good Boys Do Fine Always")       │
│  — Spaces bottom up: A C E G ("All Cows Eat Grass")              │
│                                                                  │
│  ALTO CLEF (C clef on line 3):                                   │
│  — Middle line (line 3) = middle C (C4)                          │
│  — Used for: viola (primary clef)                                │
│                                                                  │
│  TENOR CLEF (C clef on line 4):                                  │
│  — Line 4 = middle C (C4)                                        │
│  — Used for: cello, bassoon, trombone (high passages)            │
│                                                                  │
│  PERCUSSION CLEF (2 vertical lines):                             │
│  — No pitch implied — each line/space = specific drum/cymbal     │
│  — Standard mapping varies by publisher/context                  │
└──────────────────────────────────────────────────────────────────┘

Grand Staff (piano):
  [Treble clef staff]
  ─────────────────────────────────────
  Middle C on first ledger line below treble / above bass
  ─────────────────────────────────────
  [Bass clef staff]
```

---

## Note Values and Duration

### Note Head Shapes and Stems

```
┌──────────────────────────────────────────────────────────────────┐
│                     NOTE VALUE HIERARCHY                         │
│                                                                  │
│  Whole note (semibreve):        ○          4 beats (in 4/4)      │
│  Half note (minim):             ♩ (open)   2 beats               │
│  Quarter note (crotchet):       ♩ (filled) 1 beat                │
│  Eighth note (quaver):          ♪          1/2 beat              │
│  Sixteenth note (semiquaver):   ♬          1/4 beat              │
│  32nd note (demisemiquaver):    ♬ + flag   1/8 beat              │
│  64th note:                     4 flags    1/16 beat             │
│  128th note:                    5 flags    1/32 beat (rare)      │
│                                                                  │
│  Division rule: each level = half the previous                   │
│  1 whole = 2 halves = 4 quarters = 8 eighths = 16 sixteenths     │
│                                                                  │
│  DOTTED NOTES: Dot after a note = note + half its value          │
│  Dotted half = 2 + 1 = 3 beats                                   │
│  Dotted quarter = 1 + 1/2 = 1.5 beats                            │
│  Double-dotted = note + 1/2 + 1/4 its value                      │
│                                                                  │
│  TIED NOTES: Curved line connecting same pitch = sum duration    │
│  Quarter tied to quarter = 2 beats (plays as one 2-beat note)    │
│  Used to cross barlines or create unusual durations              │
└──────────────────────────────────────────────────────────────────┘
```

### Rests

Rests have exact analogues to notes:
```
Whole rest:     Rectangle hanging from 4th line  (4 beats)
Half rest:      Rectangle sitting on 3rd line    (2 beats)
Quarter rest:   Squiggle symbol                  (1 beat)
Eighth rest:    7-with-flag symbol               (1/2 beat)
Sixteenth rest: 7-with-two-flags                 (1/4 beat)
```

Mnemonic: whole rest "hangs down" (heavy, falls off ledge); half rest "sits up" (lighter, balanced). They look identical except orientation.

---

## Time Signatures

### What They Mean

```
┌──────────────────────────────────────────────────────────────────┐
│                     TIME SIGNATURES                              │
│                                                                  │
│     4              ← beats per measure                           │
│     ─     ← fraction-like symbol, NOT actually a fraction        │
│     4              ← note value that gets one beat               │
│                                                                  │
│  Top number: how many beats per measure                          │
│  Bottom number: which note value = 1 beat                        │
│    4 = quarter note, 2 = half note, 8 = eighth note              │
│                                                                  │
│  Common signatures:                                              │
│  4/4  = "common time" (C) = 4 quarter beats / measure            │
│  2/4  = march time = 2 quarter beats (strong-weak)               │
│  3/4  = waltz time = 3 quarter beats (strong-weak-weak)          │
│  6/8  = compound duple = 6 eighth beats, grouped 3+3             │
│  3/8  = compound simple = 3 eighth beats                         │
│  12/8 = compound quadruple = 12 eighth beats, grouped 3+3+3+3    │
│  5/4  = 5 quarter beats (uncommon; "Take Five", Brubeck)         │
│  7/8  = 7 eighth beats (Balkan and progressive rock)             │
│                                                                  │
│  Cut time (₵) = 2/2 = 2 half beats per measure (march/alla breve)│
└──────────────────────────────────────────────────────────────────┘
```

### Simple vs. Compound

```
SIMPLE time: the beat divides into 2 (duple subdivision)
  2/4, 3/4, 4/4, 2/2 — beat = quarter note, sub-beat = eighth note

COMPOUND time: the beat divides into 3 (triple subdivision)
  6/8, 9/8, 12/8 — beat = dotted quarter, sub-beat = eighth note

  6/8 sounds like two beats, each subdivided into 3 eighths (1-and-a 2-and-a)
  NOT like six separate eighth beats
  This is the compound/simple distinction that trips up notation readers
```

---

## Key Signatures and the Circle of Fifths

### Key Signature Basics

```
Key signatures appear at the start of each line, between clef and time signature:
— Sharps (♯) or flats (♭) placed on specific lines/spaces
— Apply to ALL notes on those lines/spaces unless canceled
— Define which diatonic scale the piece uses

SHARPS — F C G D A E B (order of sharps, one added per key)
Key of G: 1 sharp (F♯)
Key of D: 2 sharps (F♯, C♯)
Key of A: 3 sharps (F♯, C♯, G♯)
Key of E: 4 sharps
Key of B: 5 sharps
Key of F♯: 6 sharps
Key of C♯: 7 sharps

FLATS — B E A D G C F (order of flats = reverse of sharps)
Key of F: 1 flat (B♭)
Key of B♭: 2 flats (B♭, E♭)
Key of E♭: 3 flats
Key of A♭: 4 flats
Key of D♭: 5 flats
Key of G♭: 6 flats
Key of C♭: 7 flats
```

### Circle of Fifths

```
┌──────────────────────────────────────────────────────────────┐
│                    CIRCLE OF FIFTHS                          │
│                                                              │
│                    C (0 sharps/flats)                        │
│               F (1♭)         G (1♯)                          │
│           B♭ (2♭)               D (2♯)                       │
│        E♭ (3♭)                     A (3♯)                    │
│      A♭ (4♭)                         E (4♯)                  │
│       D♭ (5♭)                       B (5♯)                   │
│           G♭ (6♭/F♯6♯)          F♯/G♭                        │
│               C♭(7♭) ≡ B(5♯)                                 │
│                                                              │
│  Moving clockwise = up a fifth = add one sharp               │
│  Moving counterclockwise = up a fourth = add one flat        │
│                                                              │
│  Enharmonic equivalents at the bottom:                       │
│  G♭ major = F♯ major (6 flats = 6 sharps, same sound)        │
│  C♭ major = B major  (7 flats = 5 sharps)                    │
│  D♭ major = C♯ major (5 flats = 7 sharps)                    │
│                                                              │
│  Relative minors: each major key has a relative minor        │
│  sharing the same key signature, a minor third below:        │
│  C major ↔ A minor, G major ↔ E minor, etc.                  │
└──────────────────────────────────────────────────────────────┘
```

---

## Accidentals

Accidentals modify a single note (within a measure, unless tied or carried):

```
♯ = Sharp: raise pitch by one half-step (semitone)
♭ = Flat: lower pitch by one half-step
♮ = Natural: cancel a key-signature sharp or flat
✕ = Double sharp: raise by two half-steps
𝄫 = Double flat: lower by two half-steps

Scope rules:
— Accidental applies to all notes on that pitch in the same measure
— New measure: accidentals reset (key signature applies again)
— Courtesy accidentals: reminders after a barline (editorial convention)
```

---

## Dynamics

Dynamics use Italian abbreviations (from quietest to loudest):

```
ppp  = pianississimo — as soft as possible
pp   = pianissimo — very soft
p    = piano — soft
mp   = mezzo-piano — moderately soft
mf   = mezzo-forte — moderately loud
f    = forte — loud
ff   = fortissimo — very loud
fff  = fortississimo — as loud as possible
sfz  = sforzando — sudden strong accent
sfp  = sforzato-piano — sudden accent then immediately soft
fp   = forte-piano — loud then immediately soft
rf/rfz = rinforzando — reinforced, sudden emphasis

Hairpin (gradual change):
<  = crescendo (gradually louder)
>  = decrescendo / diminuendo (gradually softer)
cresc. = crescendo (written out)
dim. or decresc. = diminuendo/decrescendo
```

---

## Tempo Markings

Italian tempo terms (slowest to fastest):

```
Larghissimo  — extremely slow (~24 BPM)
Grave        — very slow, solemn (~35 BPM)
Largo        — very slow, broad (~50 BPM)
Larghetto    — rather slow (~60 BPM)
Lento        — slow (~52–68 BPM)
Adagio       — slow and stately (~66–76 BPM) — "at ease"
Adagietto    — somewhat slow (~70–80 BPM)
Andante      — walking pace (~76–108 BPM)
Andantino    — slightly faster than andante
Marcia moderato — moderate march pace (~83–85 BPM)
Moderato     — moderate (~108–120 BPM)
Allegretto   — moderately fast (~112–120 BPM)
Allegro      — fast (~120–156 BPM)
Allegro vivace — fast and vivacious (~172 BPM)
Presto       — very fast (~168–200 BPM)
Prestissimo  — as fast as possible (~200+ BPM)
```

**Metronome marking**: MM = ♩ = 120 means "120 quarter notes per minute." Invented by Johann Maelzel, 1815.

**Tempo modifiers**:
```
molto = very (molto allegro = very fast)
poco = a little (poco allegro)
non troppo = not too much
ma non troppo = but not too much (allegro ma non troppo)
poco a poco = little by little
subito = suddenly (subito piano = suddenly soft)
```

---

## Articulation Marks

```
.  above/below note = Staccato: detached, about half duration
─  above/below note = Tenuto: held for full duration, slight emphasis
^  above/below note = Marcato: strongly accented
>  above/below note = Accent: emphasized (softer than marcato)
+  = Stopped horn (French horn technique); also harmonics
○  = Open (horn); also harmonic
∼  = Vibrato/trill on some instruments
Tr = Trill: rapid alternation with note above (whole or half step)

Slur (curved line connecting different pitches):
— Bow/breath/phrase together; not repeated attack
— Distinguished from tie (connects same pitch)

Legato (without marks): smooth connected playing (default unless marked)
```

---

## Ornaments

Standard ornament notation:

```
Trill (tr or ~): rapid alternation between written note and note above
  Duration: whole length of note
  Speed: as fast as practical
  Starting note: debated — Baroque (start on upper note); Classical+ (start on written note)

Mordent (♩͈): written note → upper neighbor → written note (3 quick notes)
Inverted mordent / pralltriller (♩͉): written note → lower neighbor → written note

Turn (S-curve ~): written note → upper neighbor → written note → lower neighbor → written note

Appoggiatura (small grace note, filled, with slash):
  — Accented grace note, takes half the main note's value
  — Important in classical style (Haydn, Mozart)

Acciaccatura (small grace note, filled, with slash):
  — Unaccented grace note, played as quickly as possible before main note
  — "Crush note"

Glissando (gliss.): smooth slide between two notes
  Strings: slide finger; Piano: slide thumb across keys
```

---

## Chord Symbols

Used in jazz, pop, and lead sheets (not traditional classical notation):

```
┌──────────────────────────────────────────────────────────────┐
│                    CHORD SYMBOL SYSTEM                       │
│                                                              │
│  Root note:      C, D, E, F, G, A, B (+ ♯/♭)               │
│                                                              │
│  Chord quality:                                              │
│  (nothing)  = major triad:          C   = C-E-G              │
│  m or min   = minor triad:          Cm  = C-E♭-G             │
│  dim or °   = diminished triad:     Cdim= C-E♭-G♭            │
│  aug or +   = augmented triad:      C+  = C-E-G♯             │
│                                                              │
│  Extensions:                                                 │
│  7    = dominant 7th:               C7   = C-E-G-B♭          │
│  maj7 = major 7th:                  Cmaj7= C-E-G-B           │
│  m7   = minor 7th:                  Cm7  = C-E♭-G-B♭         │
│  m7♭5 = half-diminished:           Cm7♭5= C-E♭-G♭-B♭         │
│  dim7 = fully diminished 7th:       Cdim7= C-E♭-G♭-B♭♭       │
│  9    = dominant 9th (includes 7): C9   = C-E-G-B♭-D         │
│  add9 = major with added 9:        Cadd9= C-E-G-D (no 7th)   │
│  sus2 = suspended 2nd (no 3rd):    Csus2= C-D-G              │
│  sus4 = suspended 4th (no 3rd):    Csus4= C-F-G              │
│  6    = major 6th:                 C6   = C-E-G-A            │
│  m6   = minor 6th:                 Cm6  = C-E♭-G-A           │
│                                                              │
│  Slash chords (bass note):                                   │
│  C/E = C major chord with E in bass                          │
│  G/B = G major with B in bass                                │
└──────────────────────────────────────────────────────────────┘
```

---

## Guitar Tablature (TAB)

Alternative notation for string instruments (guitar, bass), encoding fret positions rather than pitches:

```
┌──────────────────────────────────────────────────────────────┐
│                    GUITAR TABLATURE                          │
│                                                              │
│  e|─────0────────3────────0────────────────────────────────  │
│  B|─────1────────0────────0────────────────────────────────  │
│  G|─────0────────0────────0────────────────────────────────  │
│  D|─────2────────0────────2────────────────────────────────  │
│  A|─────3────────2────────3────────────────────────────────  │
│  E|─────────────3─────────────────────────────────────────── │
│      C chord   G chord   Am chord                            │
│                                                              │
│  String names (top to bottom): low e (E2), A, D, G, B, high e│
│  Numbers = fret position (0 = open string)                   │
│  Read left to right = time order                             │
│  Vertical alignment = simultaneous (chord)                   │
│  Sequential = single notes                                   │
│                                                              │
│  TAB advantages: immediately tells player WHERE to play      │
│  TAB disadvantages: no duration information, no dynamics     │
│  Standard notation advantages: pitch, rhythm, expression     │
│  Standard notation disadvantages: doesn't specify position   │
│                                                              │
│  Professional guitarists use both: TAB for quick learning,   │
│  standard notation for orchestral/ensemble reading           │
└──────────────────────────────────────────────────────────────┘
```

---

## Score Layout and Conventions

```
┌──────────────────────────────────────────────────────────────────┐
│               ORCHESTRAL SCORE ORDER (top to bottom)             │
│                                                                  │
│  Woodwinds (highest → lowest):                                   │
│    Piccolo, Flute, Oboe, Cor Anglais, Clarinet, Bass Clarinet,   │
│    Bassoon, Contrabassoon                                        │
│  Brass (highest → lowest):                                       │
│    French Horn, Trumpet, Trombone, Tuba                          │
│  Percussion:                                                     │
│    Timpani, Snare, Bass drum, Cymbals, Glockenspiel, etc.        │
│  Keyboard:                                                       │
│    Harp, Piano, Celesta, Organ                                   │
│  Strings (highest → lowest):                                     │
│    Violin I, Violin II, Viola, Cello, Double Bass                │
│                                                                  │
│  Barlines connect all staves of the same family                  │
│  System brace connects all staves read simultaneously            │
│  Rehearsal numbers/letters every 10–20 bars for coordination     │
└──────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Situation | Symbol/Convention |
|-----------|-------------------|
| Piano right hand | Treble clef |
| Piano left hand | Bass clef |
| Viola part | Alto clef (C on line 3) |
| Cello high passage | Tenor clef (C on line 4) |
| Need 4 beats per measure | 4/4 time signature |
| Waltz | 3/4 |
| Jig/compound feel | 6/8 |
| Very fast | Presto, Allegro |
| Very slow | Adagio, Largo |
| Very loud | ff, fff |
| Very soft | pp, ppp |
| Gradual louder | Crescendo hairpin < |
| Detached notes | Staccato (dot) |
| Smooth connected notes | Legato / slur (curved line) |
| Guitar chord spelling | Chord symbol (C, Dm, G7, etc.) |
| Guitar position/fret | TAB notation |

---

## Common Confusion Points

**Slur ≠ Tie**: A tie connects two notes of the **same pitch** — they are played as one long note. A slur connects notes of **different pitches** — they are played smoothly without re-articulating. They use the same curved line symbol; pitch is the differentiator.

**6/8 ≠ 3/4**: Both have 6 eighth notes per measure, but the grouping differs. 6/8 groups as 2 dotted-quarter beats (2×3 eighths), creating a swinging compound feel. 3/4 groups as 3 quarter beats (3×2 eighths), creating a waltz feel. Same notes, completely different rhythmic character.

**Key signature ≠ key**: The key signature F♯-C♯ could be D major or B minor (relative minor). Context determines which. The relative minor is always a minor third below the major key — learning the relative pairs is essential.

**Treble clef for guitar sounds 8va lower**: Guitar sounds an octave lower than written in treble clef. The treble clef for guitar is actually a "G clef 8" (sometimes marked with an 8 below the clef). This convention means you can write guitar music on treble clef without constant ledger lines, while understanding the actual sounding pitch is an octave lower.

**"Forte" doesn't mean loud (absolutely)**: All dynamic markings are **relative**. A pp passage in a Beethoven symphony might be louder than an ff passage in a Baroque lute piece. Dynamics indicate relative levels within a piece, not absolute decibel levels.

**Chord symbols are not harmony analysis**: A lead sheet with chord symbols tells you what chord to play, not why. Roman numeral analysis (I, IV, V7, ii6) is the theory notation for harmonic function. They're different systems for different purposes.
