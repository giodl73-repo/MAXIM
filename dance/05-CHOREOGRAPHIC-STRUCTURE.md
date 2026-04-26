# Choreographic Structure and Composition

## The Big Picture

Choreographic structure is the syntax of dance -- how movement phrases are organized into larger units, how those units relate to each other, and how the whole creates meaning or experience over time. The bridge to computing and formal systems is direct: motif development, variation, accumulation, and canon are all algorithmic operations applied to movement material.

```
+-------------------------------------------------------------------+
|              CHOREOGRAPHIC HIERARCHY                              |
|                                                                   |
|  SMALLEST UNIT                                  LARGEST UNIT      |
|                                                                   |
|  GESTURE    -->  MOTIF  -->  PHRASE  -->  SECTION  -->  WORK      |
|                                                                   |
|  Single         Smallest     Grammatical   Unified     Complete   |
|  identifiable   meaningful   sentence      passage     piece      |
|  movement       unit         (4-32 counts) (topic)     (20min+)   |
|                                                                   |
|  ANALOGY TO CODE:                                                 |
|  Expression  -->  Variable  -->  Statement  -->  Function  --> Program |
+-------------------------------------------------------------------+

COMPOSITIONAL OPERATIONS on movement material:
  REPEAT          same material again
  VARY            change one parameter (timing, dynamic, spatial direction)
  DEVELOP         transform through multiple parameters
  FRAGMENT        use only part of original motif
  ACCUMULATE      add to, phrase builds each cycle
  CANON           delay same material by one or more beats
  RETROGRADE      reverse temporal order
  INVERSION       reverse spatial direction
  AUGMENT         slow down (expand time values)
  DIMINISH        speed up (compress time values)
  JUXTAPOSE       place contrasting material side by side
```

---

## The Motif: Basic Unit of Meaning

A motif is the smallest movement unit that carries identity across a work -- it recurs in recognizable form, even when varied. Its repetition creates memory and expectation in the audience.

```
WHAT QUALIFIES AS A MOTIF?

Not just any movement -- it must:
  1. Have distinctive IDENTITY (a quality or shape that is recognizable)
  2. RECUR in the work (used at least twice)
  3. Be VARIED when it recurs (variation reveals the motif through contrast)

TYPES OF MOTIFS:
  Spatial motif:   a specific path or direction pattern
  Dynamic motif:   a specific effort quality pattern (sudden/strong/etc.)
  Body part motif: specific body part used in distinctive way
  Gestural motif:  a gesture with symbolic or emotional resonance
  Rhythmic motif:  a specific timing pattern

EXAMPLE:
  Martha Graham's "Letter to the World" (1940)
  Motif: deep drop and recovery of torso + outstretched arm
  The motif identifies the character (Emily Dickinson's inner life)
  Returns varied: sometimes the drop is stopped mid-way; sometimes
  the arm pulls the body; same identity, different expression.
```

---

## Phrase Structure

The phrase is the grammatical sentence of dance -- a complete movement thought with implicit beginning, middle, and end.

### Phrase Types

```
PHRASE TYPES

  BREATH PHRASE:
    Follows the breath cycle -- inhale to prepare, exhale to execute
    Natural duration: 4-8 counts typically
    Feels "inevitable" and organic

  MUSICAL PHRASE:
    Structured to match musical phrase (typically 8 counts in Western)
    Most visible in ballet and jazz dance
    Risk: movement becomes illustrative rather than independent

  MOVEMENT PHRASE:
    Structured by its own internal logic (not breath or music)
    Cunningham's phrases often have no "natural" length
    Can end mid-breath; can span multiple musical phrases

  TASK PHRASE:
    Organized as a task to be completed (Judson Theater)
    "Cross the floor while carrying a chair"
    Phrase ends when task ends, regardless of count
```

### Phrase Manipulation: The Compositional Toolkit

```
PHRASE OPERATION    DESCRIPTION                    BRIDGE
-------------------+------------------------------+------------------
EXACT REPETITION   | Same phrase, identical       | Loop/replay
SPATIAL REPETITION | Same phrase, new direction   | Transform(rotate)
RHYTHMIC VARIATION | Same movement, different time | Resample
DYNAMIC VARIATION  | Same path, different effort  | Change parameter
FRAGMENTATION      | First half only; last half   | Substring
LAYERING           | Two phrases simultaneously   | Parallel threads
CANON              | Same phrase, time-offset      | Delayed copy
ACCUMULATION       | P1, P1+P2, P1+P2+P3...       | Incremental build
RETROGRADE         | Phrase backward in time       | Reverse iteration
INVERSION          | Forward becomes backward spatially | Negation
AUGMENTATION       | Phrase slowed (2x, 4x)       | Time stretch
DIMINUTION         | Phrase sped up (2x, 4x)      | Time compress
```

---

## Formal Structures: Large-Scale Organization

These are the architecture of a complete work -- how sections relate to each other across time.

### ABA (Ternary Form)

```
ABA STRUCTURE

  Section A: Opening material, establishes world
  Section B: Contrasting material, departure, development
  Section A': Return -- same as A, but now changed by B
             (the return is NEVER identical to the original;
              the audience has been changed by Section B)

EXAMPLES:
  Swan Lake: court scene (A), lakeside scene (B), court again (A')
  Graham: "Appalachian Spring" -- broadly ABA with coda
  Most pop songs: verse-chorus-verse (variant of ABA)

NOTE: The "prime" (A') is crucial. The return carries the
weight of everything that happened in B. This is not circular --
it is dialectical. A' is not A.
```

### Through-Composed

```
THROUGH-COMPOSED

  Section A --> Section B --> Section C --> Section D...
  No return; no repetition of large sections
  Linear development; narrative arc

  CHARACTERISTIC: Each section grows from what preceded it
  Cannot be rearranged without losing meaning

  EXAMPLES:
    Most dramatic ballets (Giselle, Swan Lake Act by Act)
    Many Pina Bausch works: images that accumulate
    Cunningham "Events": deliberately prevents this by mixing

  RISK: Without return, audience has no anchor; can feel arbitrary
```

### Rondo (ABACADA...)

```
RONDO

  Theme A recurs between contrasting episodes:
  A - B - A - C - A - D - A (- coda)

  The A material provides anchor and coherence
  Each episode explores something different

  EXAMPLES:
    Baroque dance forms (rigaudon, minuet in rondo)
    Some Balanchine works with recurring theme group
    Theme-and-variations: A-A1-A2-A3-A4... (variation on rondo)
```

### Canon

Canon deserves special treatment because it is the most structurally complex large-scale device:

```
CANON (also: round, fugue-equivalent in music)

  SIMPLE CANON:
    Dancer A performs phrase
    Dancer B begins same phrase 4 counts later
    They are always 4 counts apart (canon at the octave = musical term)

  COMPLEX CANON:
    Multiple entry points (A, B, C, D all enter at different offsets)
    Retrograde canon: B performs A's phrase backward
    Inversion canon: B mirrors A's spatial directions
    Augmentation canon: B performs A's phrase at half speed

VISUAL EFFECT:
  Simple canon at close interval: wave effect (swell moving through group)
  Simple canon at wide interval: phrases overlap and diverge strangely
  Combined: complex visual polyphony

FAMOUS EXAMPLES:
  Doris Humphrey's "Passacaglia" -- elaborate counterpoint of groups
  Mark Morris uses musical canons directly (he reads scores; his
  movement canons match the musical ones)
  Any synchronized flash mob that staggers the sequence
```

### Accumulation

Trisha Brown's signature structure -- worthy of its own analysis because it makes the structure itself the subject:

```
TRISHA BROWN'S ACCUMULATION (1971)

Performance:
  Perform movement 1
  Perform movements 1, 2
  Perform movements 1, 2, 3
  Perform movements 1, 2, 3, 4
  ... (32 movements total)
  Final performance: all 32 in sequence

CHARACTERISTICS:
  -- No climax (the structure itself IS the content)
  -- Audience sees the building process directly
  -- Memory is required (performer must remember all previous)
  -- Each return to the beginning recontextualizes what was simple

FORMAL PROPERTIES:
  Complexity: O(n^2) -- to perform to n, you have repeated movements
              1+2+3+...+n = n(n+1)/2 times total
  The 32nd movement is seen only once; the 1st is seen 32 times

BRIDGE: This is literally incremental addition of state. The structure
of accumulation is identical to building a linked list and traversing
from the head each time you add a node.
```

---

## Spatial Design: The Stage as Canvas

Choreography organizes not just time but space -- who is where, moving in what direction, creating what visual geometry.

### Stage Positions and Directions

```
STAGE GEOGRAPHY (proscenium stage -- audience at one end)

        UPSTAGE (away from audience)
        +--------+--------+
        | UP     | UP     |
        | LEFT   | RIGHT  |
        | (UL)   | (UR)   |
        +--------+--------+
        | CENTER | CENTER |
        | LEFT   | RIGHT  |
        | (CL)   | (CR)   |
  LEFT  +--------+--------+  RIGHT
        | DOWN   | DOWN   |
        | LEFT   | RIGHT  |
        | (DL)   | (DR)   |
        +--------+--------+
        DOWNSTAGE (toward audience)

        [AUDIENCE]

STAGE RIGHT = dancer's right when facing audience (audience's left)
STAGE LEFT = dancer's left when facing audience (audience's right)
```

### Spatial Patterns

```
SPATIAL PATTERNS AND THEIR EFFECTS

  LINE (horizontal):     Formal; democratic; no individual focus
  DIAGONAL:              Dynamic; creates depth; strong visual tension
  CIRCLE / RING:         Community; equality; no hierarchy; ritual
  CLUSTER / CROWD:       Organic; natural; contrast to formation
  SCATTER:               Disorder; individuality; democratic
  TRIANGLE (apex front): Leadership visible; hierarchy
  CONTRAST (one vs many): Individual vs community tension

V-FORMATIONS:
  Pointing upstage (V from audience view):
    Creates recession; makes space seem deep
  Pointing downstage (inverted V):
    Advances toward audience; can feel threatening or welcoming
```

### Focus and Gaze

```
FOCUS (where the dancer's gaze goes)

  TO AUDIENCE (direct address):    breaks fourth wall; implicates viewer
  TO OTHER DANCERS (inner focus):  creates world that excludes audience
  TO SPACE (unfocused):            internal state; meditative
  TO OBJECT:                       creates object's significance

  COLLECTIVE FOCUS:
    All dancers focus same direction = powerful visual unity
    Disparate focus = individuation; chaos aesthetic
```

---

## Phrase Rhythm and Dynamics

Dance has its own rhythmic logic independent of music:

```
MOVEMENT RHYTHM

PHRASING AGAINST THE BEAT:
  ON the beat: accent coincides with musical accent -- synchronized
  BEFORE beat: anticipation -- urgency, energy
  AFTER beat: suspension -- weight, weight of aftermath

DYNAMIC SHAPE OF A PHRASE:
  CRESCENDO PHRASE:
    Builds energy to end: quiet... quiet... BURST
  DIMINUENDO PHRASE:
    Decreases energy: BURST... fading... still
  ARCH PHRASE:
    Builds to midpoint then releases: quiet... PEAK... quiet

  NOTE: Ballet tends toward arch phrases (preparation -> jump -> landing)
  Graham works often use inverted arch (open -> contraction -> release)
  Cunningham deliberately disrupted natural phrasing
```

---

## Composition Devices: The Choreographer's Toolkit

```
DEVICE                  DESCRIPTION                    EXAMPLE
-----------------------+------------------------------+------------------
REPETITION             Simple reuse                   Chorus
DEVELOPMENT            Transformation over time       Theme to variations
RETROGRADE             Time reversal                  Backward phrase
INVERSION              Spatial mirror                 Left-right flip
AUGMENTATION           Slower (double time values)    Dramatic weight
DIMINUTION             Faster (half time values)      Urgency
FRAGMENTATION          Partial phrase only            Building suspense
JUXTAPOSITION          Contrasting materials side by  Irony; tension
                        side
UNISON                 All together                   Power; community
COUNTERPOINT           Independent simultaneous lines Polyphony
SOLO/ENSEMBLE          Alternation                    Dialogue
INTERRUPTION           Stop mid-phrase                Surprise; violence
STILLNESS              Deliberate pause               Weight; power
TASK                   Organized as functional task   Pedestrian reality
```

---

## Compositional Methods: How Choreographers Make Work

```
CHOREOGRAPHIC METHOD COMPARISON

  METHOD            DESCRIPTION                    MAJOR USERS
  -----------------+---------------------------------+------------------
  Set movement      Choreographer sets exact phrases  Petipa, Graham
                    on performers                     (classical)

  Improvisation     Performers improvise; choreo      Contact improv,
  score             score provides constraints        Grand Union

  Task-based        Give performers a task;           Judson, Brown
                    what results is the work

  Chance procedures Random operations determine       Cunningham
                    sequence, duration, space

  Collaboration     Performers generate material;     Forsythe's later
                    choreo curates and organizes      research work

  Score-based       Written score that different      Fluxus, Cage
                    performers interpret              tradition

  Digital/generative Algorithmic rules generate        Chunky Move (AU)
                    movement possibilities            Merce + Architects
```

---

## Decision Cheat Sheet

| Compositional goal | Device to use |
|-------------------|---------------|
| Create cohesion across a work | Motif + development |
| Show a passage of time | Augmentation or retrograde |
| Create visual unity | Unison + same spatial pattern |
| Create complexity from simple material | Canon or accumulation |
| Make structure visible (self-referential) | Accumulation |
| Avoid narrative expectation | Chance procedures |
| Organize a large ensemble | Formal structures (ABA, rondo) |
| Create dialogue between individual and group | Solo/ensemble alternation |
| Remove theatrical artifice | Task-based composition |
| Make dynamic contrast | Crescendo/diminuendo phrase shaping |

---

## Common Confusion Points

**Motif ≠ phrase.**
A motif is a unit of identity; a phrase is a unit of time/syntax. A phrase typically contains multiple motifs, or develops one motif through time.

**Retrograde is not just playing the sequence backward.**
Movement retrograde reverses the temporal sequence of movement. This is NOT simply running video in reverse -- the body does not move in the same way in reverse as it does forward. Executing true movement retrograde requires re-learning the material from the end.

**Chance procedure does not produce random-looking dance.**
Cunningham's chance-composed work often looks highly structured because the movements themselves are precise and trained. The random operation determines their sequence, not their quality. The result often looks more coherent than expressionist work because it has no awkward "narrative joints."

**Canon is more common than you think.**
Every time a group of dancers performs the same material staggered in time (wave effect), that is canon. It appears in nearly every form -- ballet corps variations, hip-hop crew dances, folk circle dances. Formal canon as compositional device is the explicit version of an instinct that appears everywhere.

**"Structure" in dance is not opposed to emotion.**
The most technically structured works (Cunningham, Brown, early Forsythe) often produce the most intense viewer experiences. Structure makes visible what would otherwise be unnoticed. The structure IS the emotional content -- not a container that holds it separately.
