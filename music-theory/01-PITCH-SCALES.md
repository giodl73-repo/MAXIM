# Pitch & Scales

## The Big Picture: From Frequency to Scale

```
FREQUENCY SPACE                 PITCH CLASS SPACE (12-TET)
────────────────────────        ──────────────────────────────────
Continuous (R⁺)                 Discrete (Z₁₂)

261.63 Hz ──→ C₄ (middle C)     C  = 0
277.18 Hz ──→ C♯₄/D♭₄           C♯ = 1
293.66 Hz ──→ D₄                 D  = 2
...                              ...
440.00 Hz ──→ A₄ (tuning ref)    A  = 9
523.25 Hz ──→ C₅                 C  = 0  (same pitch class, one octave up)

Rule: each semitone = multiply by ¹²√2 = 1.05946...
      each octave   = multiply by 2 (= 12 semitones × 1.05946¹² = 2.000)
```

**Pitch class:** Strip octave information. C₄ and C₅ are the same pitch class (0). Z₁₂ is the natural algebraic structure: 12 elements, addition mod 12.

---

## 12-TET Mathematics

### The Fundamental Formula

```
f(n) = f₀ × 2^(n/12)

where:
  f₀ = reference frequency (A₄ = 440 Hz by ISO 16)
  n  = number of semitones above/below f₀
  (negative n = below reference)

Examples:
  A₄  = 440 × 2^(0/12)  = 440.00 Hz
  A♯₄ = 440 × 2^(1/12)  = 466.16 Hz
  B₄  = 440 × 2^(2/12)  = 493.88 Hz
  C₅  = 440 × 2^(3/12)  = 523.25 Hz
  A₃  = 440 × 2^(-12/12) = 220.00 Hz  (one octave below)
  A₅  = 440 × 2^(12/12)  = 880.00 Hz  (one octave above)
```

<!-- @editor[bridge/P2]: 12-TET is a rational approximation problem: we want log₂(3/2) = 0.58496... (the just fifth) to be a rational number p/q so that q steps in a p-octave system produces a pure fifth. The approximation 7/12 is excellent (error ~0.27%); this is why 12 was chosen over competing systems (31-TET, 53-TET, etc.). This is continued-fraction approximation: the convergents of log₂(3/2) = [0; 1, 1, 2, 2, 3, 1, 5, 2, ...] give 1/2, 1/1, 3/5, 7/12, 17/29, 24/41... — each a better rational approximation. 12 is the denominator of the 4th convergent, making it the smallest tuning system where fifths are well-approximated. This is number theory applied to acoustics, and any mathematician will find the continued-fraction derivation deeply satisfying. Worth at least naming the rational approximation framing explicitly.
-->
### Cents

A **cent** = 1/100 of a semitone. 1200 cents per octave. Useful for measuring deviation from 12-TET:

```
Cents from A₄: c = 1200 × log₂(f / 440)

JI perfect fifth above A₄: 440 × 3/2 = 660 Hz
  c = 1200 × log₂(660/440) = 1200 × log₂(1.5) = 701.96 cents
12-TET fifth (E₅):  7 semitones = 700 cents
Deviation: 1.96 cents flat (inaudible in most contexts)
```

---

## The Interval Table

| Name | Semitones | Abbreviation | JI ratio | Example (from C) |
|------|-----------|--------------|----------|-----------------|
| Unison | 0 | P1 | 1:1 | C–C |
| Minor second | 1 | m2 | 16:15 | C–D♭ |
| Major second | 2 | M2 | 9:8 | C–D |
| Minor third | 3 | m3 | 6:5 | C–E♭ |
| Major third | 4 | M3 | 5:4 | C–E |
| Perfect fourth | 5 | P4 | 4:3 | C–F |
| Tritone (dim5/aug4) | 6 | TT | 45:32 / √2:1 | C–F♯/G♭ |
| Perfect fifth | 7 | P5 | 3:2 | C–G |
| Minor sixth | 8 | m6 | 8:5 | C–A♭ |
| Major sixth | 9 | M6 | 5:3 | C–A |
| Minor seventh | 10 | m7 | 16:9 | C–B♭ |
| Major seventh | 11 | M7 | 15:8 | C–B |
| Octave | 12 | P8 | 2:1 | C–C |

**Interval quality taxonomy:**

```
PERFECT intervals: P1, P4, P5, P8  → can be augmented or diminished
  (no "major" or "minor" version)

MAJOR/MINOR intervals: 2nd, 3rd, 6th, 7th
  major → one semitone up → augmented
  major → one semitone down → minor
  minor → one semitone down → diminished

AUGMENTED: one semitone wider than major or perfect
DIMINISHED: one semitone narrower than minor or perfect
DOUBLY-AUG/DIM: two semitones wider/narrower (rare, in chromatic harmony)
```

**Inversion rule:** An interval + its inversion = 9.
- M3 (4) inverts to m6 (8) → 4+8=12... no: the rule counts quality: M inverts to m, P inverts to P, aug inverts to dim
- m3 → M6, M2 → m7, P5 → P4, TT → TT (self-inverting)

---

## Major Scale Construction

### The WWHWWWH Pattern

```
W = Whole step (2 semitones)
H = Half step  (1 semitone)

Pattern: W W H W W W H
         _ _ _ _ _ _ _
Degree:  1 2 3 4 5 6 7 (8=octave)

C major:
C   D   E   F   G   A   B   C
 W   W   H   W   W   W   H

Semitones from root:
0   2   4   5   7   9   11  12
```

### Scale Degree Names

| Degree | Roman | Name | Function |
|--------|-------|------|----------|
| 1 | I | Tonic | Home, stability |
| 2 | II | Supertonic | One above tonic |
| 3 | III | Mediant | Midpoint T→D |
| 4 | IV | Subdominant | Pre-dominant |
| 5 | V | Dominant | Strongest tension → I |
| 6 | VI | Submediant | Relative minor root |
| 7 | VII | Leading tone | Half-step to tonic (strong pull) |

**Leading tone:** The major 7th (11 semitones from tonic) is only one semitone below the tonic — creates the strongest melodic/harmonic resolution. This is why the raised 7th appears in harmonic minor (see below).

---

## All 12 Major Scales

```
KEY    SHARPS/FLATS    SCALE PITCHES
───────────────────────────────────────────────────────────
C      (none)          C  D  E  F  G  A  B
G      1♯ (F♯)         G  A  B  C  D  E  F♯
D      2♯ (F♯C♯)       D  E  F♯ G  A  B  C♯
A      3♯              A  B  C♯ D  E  F♯ G♯
E      4♯              E  F♯ G♯ A  B  C♯ D♯
B      5♯              B  C♯ D♯ E  F♯ G♯ A♯
F♯/G♭  6♯/6♭ (pivot)   F♯ G♯ A♯ B  C♯ D♯ E♯ / G♭ A♭ B♭ C♭ D♭ E♭ F
D♭     5♭              D♭ E♭ F  G♭ A♭ B♭ C
A♭     4♭              A♭ B♭ C  D♭ E♭ F  G
E♭     3♭              E♭ F  G  A♭ B♭ C  D
B♭     2♭ (B♭E♭)       B♭ C  D  E♭ F  G  A
F      1♭ (B♭)         F  G  A  B♭ C  D  E
```

**Memory aid for sharps order:** F C G D A E B (Father Charles Goes Down And Ends Battle)
**Memory aid for flats order:** B E A D G C F (Battle Ends And Down Goes Charles' Father) — reverse of sharps

**Sharp keys:** The new sharp is always the leading tone of the new key.
**Flat keys:** The new flat is always the 4th degree of the new key.

---

## Relative and Parallel Minor

### Relative Minor (same notes, different center)

Every major key has a **relative minor** sharing identical key signature, centered on scale degree 6:

```
C major:    C  D  E  F  G  A  B  C
                              ↑
                         start here
A natural minor: A  B  C  D  E  F  G  A
```

| Major | Relative Minor |
|-------|---------------|
| C | a |
| G | e |
| D | b |
| A | f♯ |
| E | c♯ |
| B | g♯ |
| F | d |
| B♭ | g |
| E♭ | c |
| A♭ | f |
| D♭ | b♭ |
| G♭ | e♭ |

### Parallel Minor (same tonic, different notes)

C major and C minor share the same tonic (C) but differ in scale content:

```
C major:         C  D  E  F  G  A  B   (no flats)
C natural minor: C  D  E♭ F  G  A♭ B♭  (3 flats: E♭, A♭, B♭)

Three notes differ: ♭3, ♭6, ♭7
```

---

## The Three Forms of Minor

The natural minor (Aeolian mode) has a problem: the 7th degree is a whole step below the tonic, creating a weak resolution. Solutions:

```
NATURAL MINOR:   W H W W H W W
Pattern:         1  2  ♭3  4  5  ♭6  ♭7  8
Example (A):     A  B  C   D  E  F   G   A

HARMONIC MINOR:  W H W W H aug2 H
Pattern:         1  2  ♭3  4  5  ♭6  7   8   (raise ♭7 to 7)
Example (A):     A  B  C   D  E  F   G♯  A
Unique feature: augmented second between ♭6 and ♯7 (1.5 steps)
Purpose: restores leading tone (G♯ → A) for V7 chord (E-G♯-B-D)

MELODIC MINOR:   W H W W W W H (ascending)
Pattern (asc):   1  2  ♭3  4  5  6   7   8   (raise both ♭6 and ♭7)
Pattern (desc):  8  ♭7  ♭6  5  4  ♭3  2   1   (descend as natural minor)
Example (A asc): A  B  C   D  E  F♯  G♯  A
Purpose: eliminates aug2 in melody while preserving leading tone
Jazz note: jazz melodic minor uses the ascending form in both directions
```

**When each appears:**
- Natural minor: diatonic harmony in minor, Aeolian mode feel
- Harmonic minor: V7 chord in minor keys (the raised 7th is essential)
- Melodic minor: ascending lines to the tonic; jazz theory (jazz minor = ascending melodic always)

---

## Interval Recognition Framework

Quick identification: intervals can be calculated from the major scale.

```
TRICK: All intervals measured from scale degree 1 of the MAJOR scale
       are either MAJOR (2, 3, 6, 7) or PERFECT (1, 4, 5, 8).

To identify an interval:
1. Name the lower note
2. Count the letter-name span (C to E = 3rd; C to G = 5th)
3. Check if upper note is in the lower note's major scale
   → YES: it's major (if 2/3/6/7) or perfect (if 1/4/5/8)
   → one semitone below major → minor
   → one semitone above major → augmented
   → one semitone below perfect → diminished
   → one semitone above perfect → augmented
```

Example: C to E♭
1. Lower note = C, upper = E♭, span = 3rd
2. C major has E♮ (major third)
3. E♭ is one semitone below E♮ → minor third ✓

---

## Decision Cheat Sheet

| I want to... | Use this |
|--------------|----------|
| Find a note n semitones above f₀ | f₀ × 2^(n/12) |
| Express deviation from 12-TET | Cents = 1200 × log₂(f₁/f₂) |
| Build any major scale | Start on root, apply WWHWWWH |
| Find relative minor | Go to scale degree 6 of the major |
| Find parallel minor | Same tonic, lower ♭3 ♭6 ♭7 |
| Get V7 in minor | Use harmonic minor (raised 7th) |
| Smooth ascending line to tonic in minor | Melodic minor ascending |
| Remember sharps order | F C G D A E B |
| Remember flats order | B E A D G C F |
| Identify interval | Count letter-names, check against major scale |

---

## Common Confusion Points

**"C♯ minor" vs "D♭ major":** C♯ major (7 sharps) and D♭ major (5 flats) sound identical on piano but are spelled differently. Choose the spelling that gives simpler notation in context (D♭ major is preferred over C♯ major because 5 flats is simpler than 7 sharps; but C♯ minor is standard while D♭ minor has 8 flats — impractical, so C♯ minor is always used).

**Tritone = exactly half an octave:** 6 semitones. The only interval that divides the octave equally. F to B (or F♯ to C) — maximally dissonant in tonal music, the "diabolus in musica." Also the basis for tritone substitution in jazz (see 09).

**"The 7th degree" ambiguity:** "7th" can mean:
- The natural seventh of the scale (M7 = 11 semitones, e.g., B in C major)
- The added 7th in a chord context (e.g., the B♭ in C7 = dominant 7th = m7 above root)
- The scale degree VII (in Roman numerals)
Context determines which is meant.

**Octave numbering:** Middle C is C₄. A₄ = 440 Hz. Octave numbers change at C (not at A): B₃ is below C₄, not above it. B₄ is above C₄.
