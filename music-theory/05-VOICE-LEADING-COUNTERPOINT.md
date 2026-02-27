# Voice Leading & Counterpoint

## The Big Picture: Independent Lines in Harmonic Space

```
COUNTERPOINT: Multiple independent melodic lines that are rhythmically
  and harmonically coordinated

VOICE LEADING: The path each individual voice (part) takes from one
  chord to the next — the microscopic motion of harmony

These are two scales of the same concept:
  Counterpoint = the art of independent melodic lines (horizontal)
  Voice leading = how those lines connect chords (vertical + horizontal)

THE FOUR VOICES (SATB chorale):
  Soprano (S): highest voice, carries melody, treble range
  Alto (A):    inner voice, treble range, below soprano
  Tenor (T):   inner voice, bass range, above bass
  Bass (B):    lowest voice, often follows harmonic roots

RANGE CONVENTIONS:
  S:  C₄ – G₅   (middle C to high G)
  A:  G₃ – C₅
  T:  C₃ – G₄
  B:  E₂ – C₄

VOICE SPACING (standard):
  S–A: up to an octave apart
  A–T: up to an octave apart
  T–B: up to two octaves (larger spacing common in bass register)
  S–T, S–B: any distance is possible
```

---

## SATB Chorale Rules

These rules codify 300+ years of common-practice voice leading. They're not arbitrary — each prevents a specific acoustic problem.

SATB harmonization is a constraint satisfaction problem (CSP). The variables are the four voice pitches at each time step. The constraints map directly:

```
CSP VARIABLE                     MUSICAL CONSTRAINT
──────────────────────────────────────────────────────────────────────────
Domain per variable               Voice range (S: C₄–G₅, A: G₃–C₅, etc.)
Binary constraint (adjacent       No parallel P5/P8 between any voice pair
  time steps × voice pairs)
Unary constraint on specific      Leading tone (7̂) must resolve up to 1̂
  pitch-class assignments         Chordal 7th must resolve down by step
Constraint on chord voicing       Double root (preferred), never double
                                  leading tone
Arc consistency / propagation     If soprano = B (leading tone), then
                                  soprano at t+1 ∈ {C} — prunes the tree
```

The search space is enormous (each voice has ~20 feasible pitches × 4 voices × N time steps), but the constraints propagate aggressively. This is why DeepBach (Hadjeres et al., 2017) models SATB harmonization as probabilistic inference: given constraints, sample from the posterior distribution over valid voice assignments.

### Rules about Motion Type

```
FOUR TYPES OF MOTION BETWEEN TWO VOICES:
  Parallel: both voices move in the same direction by the same interval type
  Similar:  both voices move in the same direction by different intervals
  Contrary: voices move in opposite directions (preferred)
  Oblique:  one voice holds, other moves

FORBIDDEN MOTIONS:
  1. Parallel fifths (P5→P5): two voices maintaining a fifth apart while both move
     C–G to D–A: FORBIDDEN
     Why: two voices "fuse" into one timbre — voice independence lost
          Historically heard as medieval, regression to organum

  2. Parallel octaves (P8→P8): same pitch doubling at octave while both move
     C–C to D–D: FORBIDDEN
     Why: voices become identical, lose identity as separate lines

  3. Direct (hidden) fifths/octaves: voices jump in similar motion to P5 or P8
     S and B moving in same direction to a perfect fifth or octave
     ALLOWED only if soprano moves by step (one of the voices)
```

### Rules about Specific Notes

```
LEADING TONE RULE: The leading tone (scale degree 7) must resolve up to tonic
  In V or V7 → I, the 7th degree MUST go to the tonic
  Exception: leading tone in inner voice (A or T) may occasionally go down
             to the 5th of I if needed to complete the chord

  V7 → I resolution in C major:
    G7 (G B D F) → C (C E G)
    G: stays as G (common tone rule — common tones held)
    B: resolves UP to C (leading tone → tonic) ↑
    D: resolves DOWN to C or up to E (choose based on voice)
    F: resolves DOWN to E (7th of chord resolves down by step) ↓

CHORDAL SEVENTH RULE: The 7th of a seventh chord must resolve DOWN by step
  In G7 → C: the F (7th) resolves to E
  The 7th is a "prepared dissonance" — it arrives by step or common tone,
  and departs by step downward

DOUBLED NOTES:
  Root position: double the root (preferred), or the fifth
  NEVER double the leading tone (already has strong tendency — doubling
    would require parallel octaves or awkward resolution)
  First inversion: double the soprano note or root (avoid doubling the bass = 3rd)
  Second inversion (I⁶₄): double the 5th (which is in the bass)
```

---

## Cadence Types

A cadence is a chord progression at the end of a phrase. Four main types:

```
AUTHENTIC CADENCE (AC): V(7) → I
  Perfect Authentic (PAC): V → I, both in ROOT POSITION, soprano ends on tonic (1̂)
    Strongest possible ending — full stop, resolved
  Imperfect Authentic (IAC): V → I but:
    - V or I not in root position (inversion used), OR
    - Soprano does not land on scale degree 1
    Weaker, sense of continuation

HALF CADENCE (HC): ends on V (no resolution)
  Any chord → V
  Feels like a question — "comma" in the phrase, not a full stop
  Common endings: I → V, ii → V, IV → V, ii⁶ → V

PLAGAL CADENCE (PC): IV → I
  "Church" cadence (the "Amen" cadence)
  Softer, less directed than authentic — more conclusive than half
  Can follow an authentic cadence to extend the ending

DECEPTIVE CADENCE (DC): V → vi (or other non-I)
  Frustrated expectation — sounds like an AC coming, lands on vi
  vi shares two notes with I (both C and E in Am and C) → partial satisfaction
  Creates continuation: phrase must keep going to find the real cadence
```

---

## Five Species Counterpoint

Johann Joseph Fux (1725) codified counterpoint pedagogy as five "species" — historical exercises still used today. Each species adds rhythmic complexity against a *cantus firmus* (CF) in long notes.

```
SETUP:
  Cantus Firmus (CF): a given melody in whole notes (or similar long values)
  Added voice: the species exercises practice against the CF

SPECIES 1: NOTE AGAINST NOTE (1:1)
  One note in added voice per CF note
  Only consonant intervals allowed against CF: P1, m3, M3, P5, m6, M6, P8
  Perfect consonances (P1, P5, P8) must be approached by contrary or oblique motion
  Primary motion: contrary motion preferred throughout

SPECIES 2: TWO NOTES AGAINST ONE (2:1)
  Two half notes against each CF whole note
  Beat 1: must be consonant (strong beat)
  Beat 2: passing tones (dissonances) allowed IF approached and left by step
  The passing tone is the first allowed dissonance — by stepwise context only

SPECIES 3: FOUR NOTES AGAINST ONE (4:1)
  Four quarter notes against CF whole note
  Beats 1 and 3: preferably consonant
  Beats 2 and 4: passing tones and neighbor tones allowed
  Cambiata (changing note figure): a 4-note melodic pattern C–A–G–B (or down)
  This species develops melodic fluency

SPECIES 4: SYNCOPATED (TIE) COUNTERPOINT
  Tied half notes creating syncopation: note enters on beat 2, held to beat 1
  SUSPENSIONS: the tied note creates a dissonance on the strong beat,
    resolving DOWN by step to consonance
  This species is the origin of the suspension formula

SPECIES 5: FLORID (MIXED) COUNTERPOINT
  Combines all previous species rhythmically
  Uses all legal note values and ornamental figures
  Most like actual composed music
  The culmination: freely chosen rhythm against CF
```

---

## Suspension Types

The suspension is the essential voice leading device — a form of controlled dissonance:

```
SUSPENSION FORMULA: Preparation → Suspension → Resolution
  P: consonant note (prepared)
  S: same note held over bar line into dissonance (suspended)
  R: resolves DOWN by step to consonance

NOTATION: interval of suspension → interval of resolution
  4–3 suspension: suspended P4 resolves down to M3
    Tenor: ... G | G – F♯ |     (G = P4 above D, resolves to F♯ = M3)
    Bass:  ... D | D – D  |

  7–6 suspension: suspended m7 resolves down to M6
  9–8 suspension: suspended M9 (= M2) resolves down to P8
  2–1 suspension: M2 resolves down to unison

RETARDATION: suspension resolves UP instead of down (rare)
  7–8: seventh resolves up to octave (the "delayed leading tone")

BASS SUSPENSION (2–3): bass voice has the suspension, resolves down
  Upper voice is consonant, bass is dissonant → inverts the normal hierarchy

DECORATED RESOLUTION: resolution elaborated with passing tones, ornaments
  Common in Baroque: the resolution note approached via ornamental turn or trill
```

---

## Invertible Counterpoint

Two voices that can be swapped (the lower becomes upper and vice versa) while remaining harmonically valid:

```
INVERTIBLE AT THE OCTAVE (most common):
  Original:   Soprano: C E G  (above)
              Bass:    G E C  (below)
  Inverted:   Soprano: G E C  (was the bass, now soprano)
              Bass:    C E G  (was the soprano, now bass)

  When inverted at the octave:
    P1 → P8 (fine)
    M3 → m6 (fine, both consonant)
    P5 → P4 (PROBLEM: P4 is now dissonant in bass position)
    P8 → P1 (fine)

  Consequence: avoid perfect fifths when writing invertible counterpoint
    at the octave — they become fourths upon inversion (fourths require
    resolution when in bass)

INVERTIBLE AT THE 12th (Fux, used in fugue):
  Transpose one voice by a 12th rather than an octave
  Intervals transform differently: M3 → m7 (problem)
  More restricted — only certain interval combinations work

DOUBLE COUNTERPOINT = generic term for invertible counterpoint (two voices swappable)
TRIPLE COUNTERPOINT = three voices, all permutations valid (6 orderings)
  Bach's "Art of the Fugue" uses triple and quadruple counterpoint
```

---

## Canon and Imitation

```
IMITATION: one voice enters with a melody, another enters with the same
  (or similar) melody after a time delay

  Strict imitation: exact copy at some interval (unison, octave, 5th, etc.)
  Free imitation: melodic shape preserved, pitches adjusted for harmony

CANON: strict imitation maintained throughout — the "follow" voice
  mirrors the "lead" voice at every moment after the initial delay

  Canon at the octave: follower enters a perfect octave below/above leader
  Canon at the fifth: follower enters a perfect fifth below (most common)
  Canon at the unison: follower enters at same pitch level (hardest)

  ROUND: canon at the unison where voices cycle endlessly
    "Row, Row, Row Your Boat" = a 3-part round
    Pachelbel's Canon in D = canon at the unison over a repeating bass
    (technically: canon with basso ostinato)

  CRAB CANON (cancrizans): follower plays the leader backwards
    Rare, found in Bach's Musical Offering

  MIRROR CANON: follower is exact inversion (upside-down) of leader
    All ups → downs, all downs → ups
```

---

## Fugue Anatomy

The fugue is a formal grammar over a single data structure (the subject). The transformations applied — transposition, inversion, retrograde, augmentation, diminution, stretto — are operations on the subject as a sequence, and the compositional structure is a set of production rules: `Exposition → Subject + Answer + CS`, `MiddleEntry → transpose(Subject, key)`, `Episode → fragment(Subject) + sequence`, `Stretto → overlap(Subject, delay)`. The countersubject is constrained by double counterpoint (must be valid when swapped above/below the subject). Bach's "Art of Fugue" is an exhaustive exploration of the subject's generative potential under these operations — a systematic study of what a single input yields under all possible transformations.

The fugue is the highest form of contrapuntal writing — a multi-voice composition based on systematic development of a single melodic idea.

```
FUGUE STRUCTURE:
┌─────────────────────────────────────────────────────────────────┐
│ EXPOSITION           │ DEVELOPMENT         │ FINAL SECTION      │
│ (all voices enter)   │ (episodes + entries)│ (stretto + coda)   │
└─────────────────────────────────────────────────────────────────┘

EXPOSITION:
  SUBJECT: the main melodic idea (5–15 notes typically)
    Enters first in one voice alone (called the "dux" or leader)

  ANSWER: the second entry of the subject, in dominant key (a 5th higher)
    REAL ANSWER: exact transposition of subject to dominant
    TONAL ANSWER: adjusted intervals to preserve key feeling
      (first note: if subject begins with P5 leap, answer adjusts to P4
       to avoid overshooting the key — the "tonal answer" keeps the exposition
       within the home key region)

  COUNTERSUBJECT (CS): the melody that accompanies the answer/subject
    Designed to be invertible with the subject (double counterpoint)
    The CS must work whether above or below the subject

  Entry order (typical 4-voice fugue):
    Entry 1: SOPRANO — SUBJECT in tonic key (C major)
    Entry 2: ALTO    — ANSWER in dominant (G major), soprano has CS
    Entry 3: TENOR   — SUBJECT in tonic, alto has CS
    Entry 4: BASS    — ANSWER in dominant, tenor has CS
    → All four voices now active

MIDDLE ENTRIES AND EPISODES:
  EPISODE: passage with no complete subject statement
    Uses sequences, fragmentation of subject motives, harmonic motion
    Typically modulates to related keys

  MIDDLE ENTRY: full subject statement in a related key
    Common keys: relative major/minor, subdominant, mediant

  SEQUENCE: melodic/harmonic pattern repeated at successive pitch levels
    The primary developmental device in Baroque music
    "Rosalia" sequence (Italian ground): diatonic sequence descending by step

FINAL SECTION:
  STRETTO: overlapping entries — answer enters before subject finishes
    Creates intensification (compression of time between entries)

  AUGMENTATION: subject played in doubled note values (twice as slow)
    Gives weight and grandeur at the climax

  DIMINUTION: subject in halved note values (twice as fast)
    Creates agitation or a fleeting echo

  INVERSION: subject played upside-down (all intervals flipped)
    P: ascending becomes descending, M3 up → M3 down

  RETROGRADE: subject played backwards (very rare in tonal fugue, common in 12-tone)

  CODA/FINAL PEDAL POINT: tonic sustained in bass, final resolution
```

---

## Decision Cheat Sheet

| Situation | Rule / Technique |
|-----------|-----------------|
| Smooth chord-to-chord motion | Contrary motion, common tones held |
| Avoid "jumpy" voice leading | Prefer steps (M2/m2), limit leaps |
| Two voices moving to P5 or P8 | Must use contrary or oblique motion |
| Leading tone in soprano or bass | Must resolve up to tonic |
| 7th of a V7 chord | Must resolve down by step |
| Writing invertible counterpoint | Avoid P5 (becomes P4 on inversion) |
| Create dissonance then resolve | Use suspension formula (P → S → R) |
| Build a canon | Decide delay + interval, strict imitation |
| Develop a fugue exposition | Subject → Tonal answer + CS → all 4 voices |
| Intensify at fugue climax | Stretto (overlapping entries) |

---

## Common Confusion Points

**Parallel fifths vs fifths in chord structure:** Parallel fifths is a *voice leading* error about *successive* chords — two voices maintaining a fifth as both move. Having a P5 in a chord (like the 5th of a major triad) is fine — that's not parallel motion.

**Suspension vs anticipation:** A suspension holds a note *from the previous chord* into the new chord (dissonance on strong beat, resolves). An anticipation arrives *early* from the next chord (on a weak beat). Opposite directions in time.

**Tonal vs real answer:** A real answer exactly transposes the subject up a fifth. A tonal answer adjusts certain intervals (typically the opening) to prevent the fugue from quickly leaving the home key. Bach's Well-Tempered Clavier fugues: roughly half use tonal answers, half real answers.

**Countersubject continuity:** The CS doesn't have to appear with every subject entry — it should, but it's not strictly required. What defines a CS is that it's distinct enough to be identifiable and designed to work in double counterpoint with the subject.
