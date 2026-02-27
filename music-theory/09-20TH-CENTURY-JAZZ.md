# 20th Century Music & Jazz Theory

## The Big Picture: Breaking and Rebuilding the Tonal System

```
TIMELINE OF HARMONIC DISSOLUTION AND RECONSTRUCTION:
  1900  ─────────────────────────────────────────────────────────  2000
    │                                                               │
    │  TONALITY                                                     │
    │  UNDER STRAIN:   FREE          SERIALISM     MINIMALISM      │
    │  Chromaticism → ATONALITY  →   12-TONE   →  PHASE MUSIC     │
    │  (Scriabin,      (Schoen-       TOTAL SER.    SPECTRAL       │
    │   late Wagner,   berg 1908)     (Babbitt)     (Grisey)       │
    │   Ives)                                                       │
    │                                                               │
    │  NEO-                                                         │
    │  CLASSICISM: (Stravinsky, Prokofiev, Bartók)                  │
    │              Tonal but not "common practice"                  │
    │                                                               │
    │  JAZZ:  Ragtime → Blues → Swing → Bebop → Modal → Free Jazz  │
    │         (1900)  (1910s) (1930s)  (1940s)  (1959)  (1960s)   │
    │                                                               │
    │  ROCK/POP: overlaps with jazz harmony from the 1950s onward  │
    └───────────────────────────────────────────────────────────────
```

---

## Free Atonality (1908–1921)

**Emancipation of dissonance:** Schoenberg, Webern, Berg declared dissonances no longer needed resolution.

```
CHARACTERISTICS:
  No tonal center — no key
  All 12 pitches treated equally — no hierarchy
  Dissonance as primary sound, not exception
  Extreme chromaticism — very few repeated pitches before cycling through all 12
  Dense counterpoint, complex textures
  Short, compressed forms (can't sustain long spans without tonal structure)

KEY WORKS:
  Schoenberg: Three Piano Pieces Op. 11 (1909), Pierrot Lunaire (1912)
    Pierrot Lunaire: voice + chamber ensemble, "Sprechstimme" (speech-song —
    pitched speech, halfway between singing and speaking, notated with x-noteheads)
  Webern: Six Bagatelles for String Quartet Op. 9 (1913) — 6 pieces, ~10 seconds each
    Maximum concentration, minimum notes
  Berg: Altenberg Lieder (1912), Wozzeck (opera, 1922)
    Berg retained more expressionist continuity than Schoenberg or Webern
    Wozzeck uses tonal forms (passacaglia, suite, rondo) to organize atonal material

WHY FREE ATONALITY COULDN'T LAST LONG:
  Without tonal reference points, all harmonic locations feel equal
  Large-scale formal organization becomes difficult to perceive
  Serialization (twelve-tone) was Schoenberg's solution to provide structure
```

---

## Twelve-Tone (Dodecaphony)

Schoenberg's 1921 compositional method using a **tone row** as organizational basis:

### The Tone Row

```
A TONE ROW: an ordered series of all 12 chromatic pitches, each used once
  Example (Schoenberg Op. 25 suite):
    E F G C♯ G♯ E♭ A♭ D B C A B♭
    0 1 2  3   4   5  6  7 8 9 10 11
    (numbered 0–11 from first pitch)

PROPERTIES:
  Each pitch class appears exactly once before any is repeated
  The row is an ORDERING, not a chord — it prescribes succession, not simultaneity
  BUT: intervals between row members define the piece's harmonic "DNA"
  The row can appear as a melody, as chords (verticalized), or fragmented
```

### The Four Row Forms (4 × 12 = 48 possible statements)

The 48 row forms constitute a group action on the row. The operations — P (identity), I (negate all intervals mod 12), R (time reversal), RI (both) — composed with 12 transpositions form a group isomorphic to Z₁₂ × Z₂ × Z₂ (order 48). The 12×12 matrix is a Cayley table for this structure. Webern's rows with special symmetry (palindromes, self-inverting rows) are exactly the rows with non-trivial stabilizer subgroups under this group action — fixed points of R or I operations.

```
P  (Prime):     Original row — reads left to right
I  (Inversion): Every interval is inverted (ascending → descending, etc.)
R  (Retrograde): Original row backwards
RI (Retrograde-Inversion): Inversion backwards

Each form can start on any of the 12 pitches = 12 transpositions
Total: 4 forms × 12 transpositions = 48 possible row statements

THE 4×4 MATRIX (Magic Square):
  Rows across = Prime forms (P₀, P₂, P₄... at various transpositions)
  Rows down  = Inversions (I₀, I₂...)
  Reading across right-to-left = Retrograde
  Reading down bottom-to-top  = Retrograde-Inversion

Construction:
  1. Write P₀ (original row) across the top
  2. Write I₀ (inversion of P₀) down the left column
  3. Fill each row by transposing P₀ to start on that row's first note
  4. Any row = one P form; any column = one I form
```

### Twelve-Tone Example Matrix

```
P₀:  0  1  2  3  4  5  6  7  8  9  10 11
     E  F  G  C# G# Eb Ab D  B  C  A  Bb

I₀:  0  11 10  9  8  7  6  5  4  3   2  1
     E  Eb D  Ab Eb' B  F# C  A  G#  F  Bb

(full matrix extends as 12×12 grid)
Reading column 0 downward = I₀
Reading P₀ backward (right-to-left) = R₀ = Bb A C B D Ab Eb G# C# G F E
```

---

## Total Serialism

Post-WWII extension of twelve-tone technique to ALL musical parameters:

```
PARAMETERS SERIALIZED:
  Pitch:     12-tone row (Schoenberg's innovation)
  Duration:  12-step duration row (e.g., powers of 2: 1,2,3,4,5,6,7,8,9,10,11,12 16ths)
  Dynamics:  12 dynamic levels (ppp, pp, p, mp, mf, f, ff, fff + more gradations)
  Articulation: 12 attack types (legato, staccato, accent, marcato, etc.)
  Register:  12 octaves assigned to pitches

KEY COMPOSERS:
  Olivier Messiaen: "Mode de valeurs et d'intensités" (1949) — the seed text
    Messiaen used modes (scales) with fixed durations, articulations, dynamics
    This wasn't fully serial but inspired the next generation

  Pierre Boulez: "Structures Ia" (1952) — fully serialized 2 pianos
    Derived EVERYTHING from Messiaen's mode via row operations
    Extreme: the music sounds like random notes because every parameter
    is independently serialized — they don't align to create perceivable structure

  Milton Babbitt: "Three Compositions for Piano" (1947), "Composition for Twelve Instruments"
    American twelve-tone: even more rigorously derived, "super-sets" and "arrays"
    Babbitt coined "total organization" — the complete serialization of all parameters
    "Who Cares If You Listen?" (1958 essay) — defense of academic new music
    (Original title: "The Composer as Specialist")

LISTENING PROBLEM:
  The human ear cannot perceive simultaneous serialization of pitch, duration,
  dynamics, and articulation as related to a single row
  Music sounds highly complex but the system is inaudible as a system
  This created the "new music = unlistenable" reputation that persists
```

---

## Aleatoric Music (Chance Procedures)

John Cage's radical departure — using chance to remove composer control:

```
JOHN CAGE'S AESTHETIC:
  Influenced by Zen Buddhism (D.T. Suzuki) and the I Ching
  Goal: eliminate the composer's ego, personal taste, habits
  Let sounds be themselves — not representations of emotion or structure
  Any sound is music: the frame (concert hall, attention) creates music

METHODS:
  I Ching (chance operations): throw coins to determine parameters
    Determine pitch, duration, dynamics by consulting a random system
    "Music of Changes" (piano, 1951) — every parameter determined by I Ching

  "4'33" (1952): famous/infamous piece
    Three movements of silence (performer sits at piano, doesn't play)
    The "music" = environmental sounds during the performance
    Any ambient noise = the work
    Duration = 4 minutes and 33 seconds (arbitrary, determined by I Ching)

  Graphic notation: scores that look like art (lines, shapes, colors)
    Performers interpret freely
    "Fontana Mix" — acetate overlays over paper with points + lines

DIFFERENCE: aleatory vs improvisation
  Aleatory: the system removes choice — random operations decide
  Improvisation: performers make choices in real time
  Cage wanted to REMOVE choice; jazz improvisers make choices
```

---

## Spectralism

French movement (~1970s) treating the harmonic series as primary compositional material:

```
SPECTRALISM: start with the acoustic physics of a sound (its spectrum of overtones),
  derive pitches and chords directly from that natural structure

PROCESS:
  1. Analyze a real sound (e.g., solo cello low C) with a spectrum analyzer
  2. Extract the strongest partials (harmonic frequencies)
  3. Write these as orchestra pitches — including microtones
  4. Use the overtone series relationship as the harmonic basis of the piece

KEY COMPOSERS:
  Gérard Grisey: "Partiels" (1975) — cello low E spectrum used for entire piece
    Opening: spectrum of one pitch spread across the orchestra
    Development: "time-stretched" attack of the cello note over 8 minutes
    Each section = different phase of the original sound's life: attack, sustain, decay

  Tristan Murail: "Gondwana" (1980) for orchestra
    Interpolation between brass spectrum (harsh, odd harmonics) and string spectrum (pure)

MICROTONALITY in spectralism:
  The 7th, 11th, 13th partials don't land on 12-TET pitches
  Spectralist scores require 1/4-tone or 1/8-tone notation
  Strings and trombones can produce these; wind players use alternative fingerings
```

---

## Minimalism

American movement (~1960s–present) using simple materials, process-based composition:

```
PHASE MUSIC (Steve Reich):
  Steve Reich: "Piano Phase" (1967)
    Two identical pianos begin playing same pattern in unison
    One piano gradually accelerates (speeds up slightly)
    As phase difference grows, complex patterns emerge from the overlap
    Eventually reaches next rhythmic unison (12 steps later), process restarts
    This is literally a comb filter in time — spectral analogy
    This is not an analogy to signal processing — it IS signal processing applied
    to rhythm. Two identical periodic signals with increasing phase offset =
    a comb filter (H(z) = 1 + z^{-d}). Constructive/destructive interference
    at each rhythmic position produces the emergent patterns the audience hears.
    "Clapping Music" below makes this discrete: 12 integer phase shifts through
    all cyclic rotations of a binary rhythm pattern, where the composite at each
    step = the original pattern convolved with a unit impulse at the offset position.

    "Clapping Music" (1972): two performers clap same pattern
    One shifts by one 16th note at a time — no tempo change, just phase shift
    Completes all 12 rotations and returns to unison

  "Music for 18 Musicians" (1976): Reich's masterwork
    Modal, pulsed, texture-based
    Cycles of chords with constantly changing instrumental superimposition
    The process is gradual and audible (unlike total serialism)

ADDITIVE PROCESS (Glass):
  Philip Glass: "Einstein on the Beach" (1976)
    Add and subtract notes from a repeating figure
    ABCDE → ABCDEF → ABCDEFG (additive) or reverse (subtractive)
    Extreme length (5 hours, no intermission, audience can leave and return)

  "Akhnaten," "Satyagraha": similar approach, operatic scale

MINIMALISM vs MAXIMALISM:
  Minimalism: simplest possible materials, let repetition create perception shifts
  Maximalism (Mahler, Strauss, late Romantic): everything expanded to maximum scale
  Post-minimalism: more harmonic/melodic variety but same patient approach (Adams)

JOHN ADAMS:
  "Shaker Loops" (1978): strings; Phrygo-Lydian mode, shimmering tremolo textures
  "Nixon in China" (1987): minimalist opera — pulsed, modal, genuinely accessible
  "Short Ride in a Fast Machine" (1986): orchestral, additive process, fanfare
```

---

## Jazz Theory: Chord-Scale Relationships

The jazz theory framework that replaced "avoid notes" thinking with "use the scale that matches this chord":

```
CHORD-SCALE THEORY:
  Every chord implies one (or more) scales to improvise with
  The scale provides the "color" of that chord moment

DIATONIC CHORD-SCALE ASSIGNMENTS (in C major):
  Chord      Function   Scale to use
  ──────────────────────────────────────────────────
  Cmaj7      I          C Ionian (C major)
  Dm7        ii         D Dorian
  Em7        iii        E Phrygian
  Fmaj7      IV         F Lydian
  G7         V          G Mixolydian
  Am7        vi         A Aeolian
  Bø7        vii        B Locrian
  ──────────────────────────────────────────────────

JAZZ REFINEMENTS (more specific scale options for dominant chords):
  G7 (unaltered):   G Mixolydian
  G7♯11:            G Lydian Dominant (Mixolydian ♯4 = Mode 4 of D melodic minor)
  G7alt:            G Altered Scale (Mode 7 of A♭ melodic minor)
  G7b9:             G HW Diminished (Octatonic W-H)
  Gm7:              G Dorian (most common)
  Gm(maj7):         G Melodic Minor (ascending)
```

---

## Tritone Substitution

The most important jazz harmonic manipulation:

```
TRITONE SUBSTITUTION (triSub or TTS):
  A dominant 7th chord can be replaced by the dominant 7th a tritone away

  G7 ─── ─── ─→ D♭7  (both are tritone away = 6 semitones)

WHY IT WORKS:
  G7  contains: G–B–D–F
  D♭7 contains: D♭–F–A♭–C♭(=B)
                    ↑        ↑
                    F        B♮ (=C♭)
  The F and B are shared (enharmonic) — they're the TRITONE pair
  The tritone of the dominant chord (F–B in G7) = tritone of D♭7 (F–C♭=B)

  These two chords share the most important harmonic element (the tritone)
  and resolve identically: both the F and the B/C♭ pull toward the tonic

RESOLUTION:
  G7 → Cmaj7:   G → C (bass down P5), B → C (up semitone), F → E (down semitone)
  D♭7 → Cmaj7:  D♭ → C (bass down semitone!), F → E (same), B → C (same)

  The triSub gives a CHROMATIC bass motion (D♭ → C) instead of circle-of-fifths
  Very smooth, very jazzy sound

JAZZ ii-V-I with triSub:
  Normal:   Dm7 – G7  – Cmaj7
  With sub: Dm7 – D♭7 – Cmaj7
  Or:       A♭m7 – D♭7 – Cmaj7 (full tritone sub of the whole ii-V)
```

---

## Coltrane Changes

John Coltrane's harmonic innovation from ~1959–1965, most explicit in "Giant Steps" (1960):

```
"GIANT STEPS" HARMONIC PROGRESSION:
  B    D7   G    B♭7  E♭   Am7  D7   G    B♭7  E♭   F♯7  B    Fm7  B♭7
  Emaj7 –  Cm7 – F7 – B♭maj7 – Gm7 – C7 – Fmaj7... (subset shown)

THE COLTRANE MATRIX (Tonic System):
  Uses three tonal centers, each a major third apart:
    B – G – E♭ (major thirds = divides octave into 3 equal parts)
    The three "pillars" are major thirds: B, G♮, E♭ (= D♯)

  Each key is approached by its ii-V:
    To reach B:   C♯m7 – F♯7 → B
    To reach G:   Am7  – D7  → G
    To reach E♭:  Fm7  – B♭7 → E♭

  Then cycles: B → G → E♭ → B → G → E♭... at rapid tempo

WHY "GIANT STEPS":
  Moving between three key centers in major-third relationships
  creates "giant" intervallic jumps — very challenging to navigate at speed
  Bebop musicians had to develop entirely new vocabulary for this

COLTRANE SUBSTITUTION (in standard tunes):
  Replace any ii-V-I (or just the V-I) with the Coltrane matrix approach
  "Countdown" (1960): adds Coltrane substitutions to "Tune-Up" (Miles Davis)
  The chord movement covers the three tonal centers per original chord
```

---

## Jazz Harmony: Extensions and Alterations Quick Reference

```
CHORD SYMBOL VOCABULARY:
  maj7        = major 7th (M7 interval)
  7           = dominant 7th (m7 interval)
  m7          = minor 7th
  m7♭5 (ø7)  = half-diminished
  °7          = fully diminished

  EXTENSIONS (add above 7th):
  9   = M9 (major 9th — whole step above octave)
  ♭9  = m9 (minor 9th — half step above octave)
  ♯9  = A9 (augmented 9th = same as m3 above root)
  11  = P11 (perfect 11th = P4 above octave)
  ♯11 = A11 (augmented 11th = Lydian color)
  13  = M13 (major 13th = M6 above octave)
  ♭13 = m13 (minor 13th = m6 above octave)

  ALTERED DOMINANTS:
  7alt   = use altered scale (♭5, ♯5, ♭9, ♯9 all possible)
  7♯11   = Lydian Dominant (Mixolydian ♯4)
  7♭9    = Phrygian Dominant / octatonic
  7♯5    = augmented dominant (whole-tone scale)
  13♯11  = Lydian Dominant with added 13th
  7♭5♭9  = most dissonant standard alteration

JAZZ VOICING PRINCIPLES:
  Drop 2: take the 2nd highest note of a close-position chord, drop it an octave
    Creates an "open" voicing with wider intervals in the middle
    C6/9 close: C E A B → Drop 2: C A E B (or various orderings)
  Rootless voicings: omit the root (bass player covers it)
    Cmaj7: left hand plays E-G-B(-D) or 3-5-7-9 without root C
    Creates more harmonic ambiguity and voicing freedom
  Shell voicings: root + 3rd + 7th only (core harmony, skip 5th)
    Very common in piano comping + guitar chord-melody
```

---

## Decision Cheat Sheet

| Style / technique | Resource |
|-------------------|---------|
| No tonal center, maximum dissonance | Free atonality (Schoenberg Op. 11) |
| Organized non-tonal structure | Twelve-tone row + matrix |
| Every parameter controlled | Total serialism |
| Silence / ambient as music | Cage / aleatoric |
| Overtone-derived chords | Spectralism (Grisey) |
| Micro-repetition, gradual shift | Phase music (Reich) |
| Additive/subtractive patterns | Glass style minimalism |
| Blues-rock improvisational scale | Minor pentatonic + blues note |
| Jazz improvisation over ii-V-I | Use chord-scale theory (Dorian/Mixolydian/Ionian) |
| More outside color on dominant | Altered scale, Lydian Dominant |
| Chromatic bass motion to tonic | Tritone substitution |
| Move through 3 key centers quickly | Coltrane changes (major third cycle) |

---

## Common Confusion Points

**Twelve-tone ≠ atonal (necessarily):** Berg's Violin Concerto uses a twelve-tone row but sounds remarkably tonal — the row contains major and minor triads, a harmonized chorale, and quotes a Bach chorale. Twelve-tone is a METHOD; atonality is the RESULT. The two correlate strongly but aren't the same thing.

**Serialized duration is not the same as rhythmic feel:** When durations are serialized, the rhythmic organization has no pulse or groove. This is very different from the serialized pitch structure, which can theoretically be used with any rhythm. Total serialism kills groove entirely.

**Tritone substitution and enharmonics:** D♭7 is the tritone sub for G7 because the tritone from G is D♭ (6 semitones). The key is that D♭7 and G7 share the same tritone interval (F–B = F–C♭ enharmonically). In performance, many jazz players "play outside" before resolving — the triSub is the most common "outside" move.

**"Giant Steps" tempo:** The harmonic rhythm of Giant Steps is very fast (one chord per beat at quarter = 286 BPM). The challenge for improvisers isn't just learning the scales — it's navigating three different keys in the time of one normal ii-V-I. Coltrane practiced this by playing arpeggios through the changes at various speeds — a technical approach, not just theoretical knowledge.
