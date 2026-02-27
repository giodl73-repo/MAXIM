# Tonal Harmony — Advanced

## The Big Picture: Common-Practice Harmony as a System

```
COMMON-PRACTICE PERIOD (≈ 1600–1900):
  A unified harmonic language shared across Baroque, Classical, Romantic
  Characterized by:
    ┌─────────────────────────────────────────────────────────┐
    │ 1. FUNCTIONAL TONALITY: T → PD → D → T drives structure │
    │ 2. DIATONIC CORE: most chords from the key's scale       │
    │ 3. CONTROLLED CHROMATICISM: non-diatonic notes prepared  │
    │ 4. VOICE LEADING RULES: smooth motion, resolved tensions │
    │ 5. HIERARCHICAL FORM: keys organized around a tonic key  │
    └─────────────────────────────────────────────────────────┘

CHROMATIC EXPANSION TIMELINE:
  Bach (1700s):    diatonic + secondary dominants + diminished 7ths
  Mozart/Haydn:    smoother modulations, secondary dominants common
  Beethoven:       remote modulations, modal mixture, longer prolongations
  Schubert:        third relations (C major → A♭ major directly)
  Chopin/Liszt:    extended chromaticism, non-functional color chords
  Wagner (1865):   Tristan — chromatic saturation, tonal ambiguity
  Late Mahler:     polytonality, chromaticism threatening tonal coherence
  Schoenberg (1909): tonality dissolves into "free atonality"
```

---

## Modulation Types

A modulation is a change of tonal center — the music establishes a new key as home.

### Pivot Chord Modulation

```
The smoothest modulation: a chord belongs to both the old and new key

PROCESS:
  1. Play in Key A: establish the home key
  2. Introduce a PIVOT CHORD: a chord interpretable in both Key A and Key B
  3. Reinterpret the pivot chord in Key B context
  4. Confirm Key B with a strong cadence (V7 → I in Key B)

EXAMPLE: C major → G major
  In C major: Am  (= vi in C)
  In G major: same chord Am = ii in G
  → Am is the pivot chord (vi = ii)
  After the pivot, V7 of G (D7) → G confirms the modulation

COMMON PIVOT CHORD RELATIONSHIPS:
  Between keys a fifth apart: many chords in common (5 shared diatonic chords)
  Between relative keys (same key signature): 5 of 7 chords identical
  Between parallel keys: only the tonic chord differs by quality (C vs Cm)

NEAR MODULATION: closely related keys (up to 1 accidental difference)
  Most modulations in Classical era are to closely related keys
  5 closely related keys to C major:
    G major (V), F major (IV), A minor (vi), E minor (iii), D minor (ii)
```

### Chromatic Modulation

```
Pivot note rather than pivot chord:
  One note in the old chord is held (common tone) and reinterpreted
  as part of a chord in the new key — no common CHORD, just common NOTE

EXAMPLE: C major → E major (third relation)
  C major chord: C–E–G
  E major chord: E–G♯–B
  Common tone: E (appears in both chords)
  The E in C major becomes the root of E major
  G→G♯ moves by chromatic half step

Third-relation modulation (Schubert's specialty):
  Keys a major or minor third apart
  C major → E major: up a M3
  C major → E♭ major: up a m3
  C major → A major: down a m3 (enharmonic of up a M3's complement)
  C major → A♭ major: down a M3 (= up a m6)

  These modulations are sudden and colorful — there is no pivot chord
  in the standard sense, just chromatic voice leading between the keys
```

### Enharmonic Modulation

```
Two chords that SOUND identical but are spelled differently,
used to pivot between otherwise distantly related keys:

<!-- @editor[bridge/P2]: The "only 3 distinct diminished 7th chords" result is a direct consequence of Z₁₂ group structure. A fully diminished 7th chord = 4 equally-spaced pitch classes (spacing = 3 semitones). The set {0, 3, 6, 9} in Z₁₂ divides the 12 pitch classes into exactly 3 equivalence classes (cosets of the subgroup {0, 3, 6, 9} under addition mod 12 — the subgroup has order 4, so 12/4 = 3 distinct cosets). Similarly: only 4 distinct augmented triads (3 equally-spaced = spacing 4, 12/3=4), only 6 tritone pairs (spacing 6, 12/2=6), only 2 whole-tone scales (spacing 2, 12/6=2). These counts all fall out immediately from Lagrange's theorem applied to subgroups of Z₁₂. The file presents the facts without naming the algebraic structure. Any mathematician will want to know why, and the why is elementary group theory. -->
DIMINISHED 7TH as pivot:
  Fully diminished 7th (°7) = four minor thirds stacked
  Symmetry: only 3 distinct diminished 7th chords (then cycle repeats)
  Each can be respelled as any of its 4 enharmonic rotations

  B°7 = B–D–F–A♭
  Respell as D°7 = D–F–A♭–C♭  (C♭ = B enharmonically)
  Respell as F°7 = F–A♭–C♭–E♭♭ (E♭♭ = D)
  Respell as A♭°7 = A♭–C♭–E♭♭–G♭♭ (G♭♭ = F)

  Any °7 chord can resolve to one of four different keys
  → can modulate from, say, C major to E♭ minor using one °7 pivot chord

AUGMENTED 6TH as pivot (German):
  The German augmented 6th chord in one key is enharmonically identical
  to a dominant 7th in another key (a tritone away):
  In C major: A♭–C–E♭–F♯ (Ger+6) = G♯–B♯–D♯–F♯ (if respelled = A♭7 dominant)
  This allows modulation to the tritone-related key via an enharmonic pivot
  Used famously in Schubert's "Winterreise" and Wagner
```

---

## Modal Mixture Chords (Extended)

Beyond the basic borrowed chords (see 04-HARMONY-CHORDS.md), mixture creates a full palette:

```
IN C MAJOR — BORROWING FROM C MINOR:
  Chord   Notes        Roman  Function
  ─────────────────────────────────────────
  Cm      C E♭ G       i      minor tonic (rare but effective)
  B°      B D F        vii°   leading-tone triad (from harmonic minor)
  B°7     B D F A♭     vii°7  fully dim leading-tone 7th
  E♭      E♭ G B♭      ♭III   mediant major (mixture)
  Fm      F A♭ C       iv     minor subdominant (very common, poignant)
  F°      F A♭ C°      iv°    rarely used
  A♭      A♭ C E♭      ♭VI    flat-six major (powerful dark color)
  B♭      B♭ D F       ♭VII   flat-seven major (Mixolydian rock chord)
  Bdim    B D F        vii°   as above

MIXTURE FROM MINOR → MAJOR (Picardy third):
  In minor key, end with a MAJOR tonic chord
  A minor piece ending on A major (the raised 3rd = C♯ instead of C)
  Common in Baroque (nearly all minor-key pieces end with Picardy third)
  Symbol: I (at end of minor piece) or I♯3 in some notations
```

---

## The Neapolitan Chord (♭II)

```
NEAPOLITAN (N or ♭II): a major triad built on the flattened 2nd scale degree
  In C major: D♭ major (D♭–F–A♭)
  In C minor: D♭ major (same)

  Most often appears in FIRST INVERSION: N⁶ (= ♭II⁶)
  F in the bass (the 3rd of D♭ major): D♭/F → G7 → C

HARMONIC FUNCTION: Pre-Dominant (like iv or ii°)
  N⁶ → V → I  (or N⁶ → i⁶₄ → V → i in minor)
  The D♭ "steps down" by a half step to C (tonic), or
  the F steps down by a semitone to E (3rd of I)

WHY "NEAPOLITAN": associated with 18th-century Neapolitan opera school
  Scarlatti, Pergolesi used it; later: Beethoven, Schubert, Chopin, Brahms

VOICE LEADING:
  In N⁶: bass on F, upper voices have D♭ and A♭
  To V: F stays or moves to G (P5 of V)
        D♭ → C (half step down, smooth)
        A♭ → G or B (depending on which part of V)
  Both D♭ and A♭ want to resolve downward — chromatic pull

SOUND: deeply somber, especially in minor contexts
  The D♭ above C (or G♯ above A in A minor) creates
  maximum chromatic distance from the home key region
```

---

## Augmented Sixth Chords

A family of chromatic pre-dominant chords built on the raised 4th resolving outward to the 5th:

```
THE AUGMENTED SIXTH INTERVAL:
  In C major: A♭ in bass + F♯ above = augmented 6th interval
  The A♭ and F♯ are equidistant from G (the dominant note)
  They resolve outward by half step: A♭→G (bass) and F♯→G (soprano)

                  F♯ ─── G  (up by half step)
                   ↑        ↓ resolution to G
                  A♭ ─── G  (up by half step)

  Both voices move to the same note (G) = the dominant root
  → These chords are ALWAYS Pre-Dominant, always resolve to V

THREE TYPES (differing in the note between the bass A♭ and soprano F♯):

ITALIAN AUGMENTED 6TH (+6 or It+6):
  Notes: A♭–C–F♯ (3 notes only)
  = A♭ + C (the tonic scale degree) + F♯
  Simple, lacks the inner filling

FRENCH AUGMENTED 6TH (Fr+6):
  Notes: A♭–C–D–F♯ (4 notes)
  D is the supertonic (scale degree 2)
  Has a more dissonant "bite" due to the D
  Resembles a dominant 7th chord: D7 = D–F♯–A–C (enharmonically similar)
  The French +6 IS enharmonically equivalent to a dominant 7th a tritone from the main dominant

GERMAN AUGMENTED 6TH (Ger+6):
  Notes: A♭–C–E♭–F♯ (4 notes)
  E♭ is the lowered 3rd (mixture from minor)
  Most commonly used; richest sound
  Enharmonically = a dominant 7th chord: A♭7 = A♭–C–E♭–G♭ (G♭=F♯)
  → This enharmonic identity enables the Ger+6 as a modulation pivot (see above)

RESOLUTION:
  All three resolve to V (G major in C):
    A♭ → G (bass, up semitone)
    F♯ → G (soprano, up semitone)
    C → B or D (depends on specific chord/voice)
    E♭ → D (German, resolves down) — brief I⁶₄ often intervenes to avoid parallel 5ths

  Optional: resolve to I⁶₄ first, then I⁶₄ → V → I (classical convention)
```

---

## Romantic Chromaticism

### The Tristan Chord (Wagner, 1865)

```
From the opening of "Tristan und Isolde" (Act 1, Prelude):
  CHORD: F–B–D♯–G♯ (or as written: F–B–D♯–A♭)

  What is it?
    ─────────────────────────────────────────────────────────
    Interpretation 1: Half-diminished 7th (Bø7 = B–D♯–F♯–A)
      The F and G♯ would be non-chord tones (chromatic passing/neighbor)
    Interpretation 2: French augmented 6th in A minor
      Fr+6 in A minor: F–A–B♭ would be standard; this is highly altered
    Interpretation 3: A chord with no clear tonal function
      The Tristan Chord intentionally resists resolution —
      it moves to a dominant 7th (E7) but even that doesn't resolve to A
      The yearning-without-resolution is the POINT: it represents unfulfilled longing
    ─────────────────────────────────────────────────────────

  THE BROADER POINT: Wagner deliberately created harmonic ambiguity
    The chord's tonal function is always deferred, never resolved
    Over 4 hours of opera, this creates immense psychological tension
    After Tristan, tonality became increasingly unstable:
      Chromatic chords don't have to resolve properly
      Color and sonority can be ends in themselves
```

### Chromaticism Techniques

```
NON-FUNCTIONAL CHROMATICISM:
  Chords used for color rather than function
  No longer T → PD → D → T — just chromatic sliding

CHROMATIC VOICE LEADING:
  Each voice moves by half step regardless of harmonic function
  "Planing": voices move in parallel motion, all chords same quality
  Debussy: parallel triads (first inversions especially) = "parallel planing"

CHROMATIC MEDIANT RELATIONS:
  Chords a major or minor third apart, sharing no common tones
  Used for sudden key-like shifts without modulation:
    C major → A♭ major (♭VI): brilliant sudden color change
    C major → E major (III♯): bright, shocking
  Both voices and harmonies slide by half step: "chromatic third"

CHROMATICALLY ALTERED CHORDS:
  Any chord that adds a chromatic note without implying modulation
  The Romantic "palette" includes all augmented triads, dim7 chords,
  augmented sixths, and free mixture across major/minor
```

---

## Impressionist Harmony (Debussy, Ravel)

```
IMPRESSIONISM breaks from functional harmonic grammar:

PARALLEL MOTION (Planing):
  Traditional: parallel P5s and P8s are FORBIDDEN
  Debussy: deliberately parallel everything
    Parallel first-inversion triads ("fauxbourdon-on-steroids")
    Parallel seventh chords
    No resolving of dissonances — chords just slide

STATIC HARMONY:
  Long static pedal tones with changing harmonies above
  No tonal direction — present-tense harmonic color
  Used in: "La Cathédrale engloutie," "Prélude à l'après-midi d'un faune"

PENTATONIC AND WHOLE-TONE:
  Both avoid half steps (no leading tones) → no functional pull
  Creates the floating, ambiguous quality
  "Voiles" (Debussy): entirely whole-tone in first section

NON-FUNCTIONAL ALTERED CHORDS:
  Major 7th chords with added 6ths, 9ths used as stable endpoints
  Dom7 chords NOT resolving to their implied tonic
  V7 → IV instead of V7 → I (plagal motion, anti-functional)

MODAL BORROWING:
  Dorian, Lydian, Pentatonic replace diatonic major/minor
  Medieval modes revived for "archaic" or exotic color
```

---

## Decision Cheat Sheet

| I want to modulate to... | Best method |
|--------------------------|-------------|
| Adjacent key (5th away) | Pivot chord (many shared chords) |
| Relative minor/major | Pivot chord (5 shared chords) |
| Key a 3rd away (Romantic) | Chromatic mediant, common-tone |
| Distant/unexpected key | Enharmonic modulation (°7 or Ger+6 pivot) |
| Add dark color pre-V | Neapolitan (♭II⁶) |
| Add tense chromatic PD | Augmented sixth (It/Fr/Ger) |
| Maximum pre-dominant tension | Ger+6 → V7 → I |
| Impressionist floating | Parallel planing, whole-tone, non-functional |
| Minor tragic close | Picardy third (major tonic in minor) |

---

## Common Confusion Points

**Neapolitan vs bII:** The Neapolitan IS the ♭II chord — they're the same thing, just different ways to say it. "Neapolitan" is the historical name; "♭II" or "♭II⁶" is the Roman numeral notation.

**German +6 vs dominant 7th:** They're enharmonically identical (e.g., Ger+6 in C = A♭–C–E♭–F♯ = A♭7 dominant). The difference is purely functional: Ger+6 is a pre-dominant resolving to G major (V); A♭7 dominant resolves to D♭ major. Composers exploit this enharmonic ambiguity for modulations.

**The Romantic ♭VI chord:** A♭ major in C major (♭VI) is simultaneously: a modal mixture chord (from parallel minor), a chromatic mediant, and potentially the Ger+6 with a missing F♯. Context distinguishes these — but often, in Romantic music, the chord is simply coloristic and defies single functional labeling.

**Chromatic vs enharmonic:** "Chromatic" = using notes outside the diatonic key. "Enharmonic" = the same pitch spelled with different note names (C♯ = D♭). Enharmonic modulation requires a respelling, chromatic modulation doesn't necessarily.
