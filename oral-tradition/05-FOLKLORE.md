# Folklore and Myth: Propp Morphology, Tale Types, Urban Legend, Rumor

## The Big Picture

```
FOLKLORE TAXONOMY
==================

+------------------------------------------------------------------+
|                        FOLKLORE                                  |
|                                                                  |
|  NARRATIVE               PROVERB / RIDDLE      CUSTOM / RITUAL  |
|  ---------               ----------------      ---------------  |
|  Myth                    Proverb                Festival        |
|  Legend                  Wellerism              Life-cycle rite  |
|  Folktale (Marchen)      Riddle                 Folk belief      |
|  Epic                    Tongue twister         Superstition     |
|  Ballad                  Blessing/curse         Folk medicine    |
|  Fable                                                          |
|  Urban legend                                                   |
|                                                                  |
+------------------------------------------------------------------+
         |
         v
KEY DISTINCTION (Bascom 1954):
  MYTH: sacred narrative, believed true,
        set in remote past / other world,
        explains origins
  LEGEND: secular, believed true (or disputed),
          set in recent historical past or here,
          about humans and encounters with supernatural
  FOLKTALE: secular, not believed literally true,
            explicitly fictional, entertainment primary
```

---

## Vladimir Propp: Morphology of the Folktale (1928)

### The Project

Vladimir Propp (1895-1970) analyzed 100 Russian fairy tales from the Afanasiev collection. His goal: find the **minimal structural units** — the way a morphologist identifies the minimal units of organic structure.

```
PROPP'S KEY CLAIMS
==================

1. All Russian fairy tales have the same structure.

2. The structure consists of 31 FUNCTIONS in invariant order.
   (Not all functions appear in every tale, but order never reverses.)

3. Characters can vary; functions are constant.
   "The functions of dramatis personae represent
    those parts which have an importance for the
    course of the action." (Propp, 1928)

4. There are 7 SPHERES OF ACTION (character roles):
   Villain, Donor, Helper, Princess (sought-person),
   Dispatcher, Hero, False Hero

ANALOGY (MIT TCS):
  Propp's functions = productions in a context-free grammar
  The tale = a string derived from that grammar
  Functions = terminals; spheres of action = non-terminals
  The morphology = the grammar itself
```

### The 31 Functions

```
PROPP'S 31 FUNCTIONS (abbreviated)
====================================

PREPARATORY SECTION (a-g):
  alpha  Absentation -- family member leaves home
  beta   Interdiction -- prohibition imposed on hero
  gamma  Violation -- interdiction is violated
  delta  Reconnaissance -- villain seeks information
  eps    Delivery -- villain gets information
  zeta   Trickery -- villain deceives victim
  eta    Complicity -- victim is deceived

COMPLICATION (1-7):
  1  Villainy (or Lack) -- villain does harm OR
     hero lacks something (two structural variants)
  2  Mediation -- hero becomes aware, is dispatched
  3  Beginning counteraction -- hero agrees to act
  4  Departure -- hero leaves home

DONOR SEQUENCE (8-14):
  5  First function of donor -- hero tested/questioned
  6  Hero's reaction -- hero reacts to donor
  7  Receipt of magical agent -- hero receives aid

HERO'S JOURNEY (15-19):
  8  Spatial transference -- hero travels to destination
  9  Struggle -- hero and villain fight
  10 Branding -- hero is marked/wounded
  11 Victory -- villain is defeated
  12 Resolution of lack -- initial lack is resolved

RETURN AND RECOGNITION (20-31):
  13 Return
  14 Pursuit
  15 Rescue
  16 Unrecognized arrival
  17 False claims by False Hero
  18 Difficult task
  19 Solution
  20 Recognition
  21 Exposure of False Hero
  22 Transfiguration -- hero transformed
  23 Punishment -- villain punished
  24 Wedding -- hero marries, ascends throne
```

### Propp's Influence

```
PROPP'S IMPACT
===============

1. Structuralist narratology:
   Greimas (1966) -- actantial model (6 actants from Propp's 7)
   Levi-Strauss -- mythological analysis (binary oppositions)

2. Computer science / AI:
   Story grammars (Rumelhart 1975, Mandler & Johnson 1977)
   Plan-based narrative understanding
   Schank & Abelson -- scripts (stereotyped event sequences)
   Interactive fiction / game design:
     Brenda Laurel: computers as theatre
     Will Wright: procedural narrative generation

3. Film theory:
   Christopher Vogler's "The Writer's Journey" (1992)
     adapted Propp via Joseph Campbell's "Hero with a Thousand Faces"
   "Save the Cat" (Blake Snyder) -- screenwriting beats
   All story structure frameworks derive from Propp

4. Comparative limitations:
   Propp works for Russian fairy tales; applicability
   to other corpora is contested
   Alan Dundes extended to Native American tales
   Critics: Propp's functions are too specific to Russian material
```

---

## Aarne-Thompson-Uther Index (ATU)

The ATU is the international tale type catalogue — a classification system for oral narratives.

```
ATU HISTORY
============

1910: Antti Aarne (Finnish) -- first comparative index
      Classified 540 tale types
1928: Stith Thompson (American) -- expanded to 2,499 types
1961: Thompson's "Motif-Index of Folk-Literature"
      (6 volumes) -- catalogued motifs below tale type level
2004: Hans-Jorgen Uther (German) -- revised to 2,232 types

STRUCTURE:
  Tale types: numbered (e.g., ATU 333 = "Little Red Riding Hood")
  Motifs: sub-components (e.g., D672 = "obstacle flight")

SCOPE:
  Covers European and Western Asian traditions primarily
  Non-Western traditions are underrepresented
  Ongoing: Berezkin's cross-cultural mythology database
    (more globally comprehensive)
```

### ATU 333: Little Red Riding Hood — Case Study

The most studied tale type: 58 documented variants.

```
ATU 333 VARIANT ANALYSIS
=========================

BASIC PLOT: Girl + basket + wolf + grandmother + rescue (or not)

Key variant axes:
  1. Fate of grandmother:
     - Wolf kills and eats her (most versions)
     - Wolf locks her in closet (some versions)
     - Girl eats her flesh/drinks her blood (oldest French versions)
       [the "werewolf" variant -- explicit cannibalism]

  2. Rescue:
     - Huntsman cuts wolf open (Grimm)
     - Girl tricks wolf herself (Perrault's "moral" -- she doesn't)
     - No rescue -- didactic cautionary tale (Perrault 1697)

  3. Geographic distribution by ending:
     - Europe: rescued
     - East Asia (Japan, China, Korea): girl defeats wolf herself
       [ATU 333 exists in oral tradition independently of Perrault]

Charles Perrault (1697): first literary version
     -> "Le Petit Chaperon Rouge" -- no rescue, moral appended
Brothers Grimm (1812): huntsman rescue added
     -> "Rotkäppchen" -- moral ending, rescue

The oral tradition predates both literary versions.
Tehrani (2013): phylogenetic analysis of 72 variants
  -> African versions form distinct clade
  -> Suggests tale type is genuinely ancient (~2,600+ years)
```

---

## Myth: A Precise Definition

Folklore scholars distinguish myth from folktale by three criteria:

| Criterion | Myth | Legend | Folktale |
|-----------|------|--------|---------|
| Sacred or secular? | Sacred | Secular | Secular |
| Believed true? | Yes (within tradition) | Yes or debated | No (explicitly fiction) |
| Setting | Remote past / other world | Recent past / here | Timeless / "once upon a time" |
| Function | Cosmological explanation | Historical exemplar | Entertainment / moral |
| Performers | Ritual specialists | Any storyteller | Any storyteller |

**Cosmogonic myths** (creation stories) are the most universal myth type — every documented culture has one. Lévi-Strauss's structural analysis: myths resolve cultural contradictions through mediation (binary opposition pairs resolved by a third term).

---

## Urban Legend: Contemporary Oral Tradition

Jan Harold Brunvand (1933-2022) established the academic study of urban legends:

```
URBAN LEGEND CHARACTERISTICS
==============================

1. Told as true (legend = believed, unlike folktale)
2. "Friend of a friend" attribution (FOAF)
   -> Creates distance from verifiability
   -> "This happened to someone my colleague knows"
3. Set in recognizable modern context
   (not forest but freeway; not castle but hospital)
4. Contains "message" or cautionary element
   (moral function like traditional legend)
5. Circulates via oral transmission
   (now also via email, text, social media)

Brunvand's taxonomy:
  Automobile legends: "The Hook" (escaped convict), "The Vanishing Hitchhiker"
  Medical legends: contaminated food, organ theft
  Campus legends: exam rules, killer in the dorm
  Technology legends: razors in candy, needles in seats
```

### "The Hook" (ATU variant)

Classic urban legend structure analysis:

```
"THE HOOK" STRUCTURE
=====================

Setting: teenagers in car at "lover's lane"
Tension element: radio warning about escaped mental patient
                  with a hook for a hand
Action: couple decides to leave
Punchline: back home, find a hook hanging from car door handle

Propp analysis:
  Villain: escaped mental patient (villainy: threat)
  Hero(es): teenagers
  Helper: radio warning (donor)
  Magical object: decision to leave (negative -- the hook is left behind)
  Resolution: partial escape (hook = evidence)

Function: cautionary -- young people alone in cars
  at night are in danger; sexual activity outside
  the home is punished/threatened
  (Brunvand: legends articulate cultural anxieties)
```

---

## Rumor, Legend, Myth: Structural Differences

```
ORAL NARRATIVE TYPE CONTINUUM
===============================

RUMOR
  Unverified claim about current events
  Short, non-narrative, or minimally narrative
  Time-sensitive (decays when events resolve)
  No fixed story structure
  Example: "The server is down because X"

LEGEND (including urban legend)
  Narrative (story with characters and events)
  Believed true (or claimed true)
  Set in recent past / plausible present
  Persists beyond precipitating events
  Example: "Kidney theft in hotel"

MYTH
  Narrative explaining cosmological or social order
  Sacred context; performed by specialists
  Set in primordial time or other world
  Does not decay -- is actively maintained
  Example: creation narratives, divine genealogies

FOLKTALE
  Narrative entertainment
  NOT believed true (explicitly fictional)
  Timeless setting ("once upon a time")
  Structural formulas at opening and closing
  Example: Cinderella, Jack and the Beanstalk
```

---

## Internet Meme as Digital Folklore

Limor Shifman's *Memes in Digital Culture* (2014) analyzed memes using folklore methodology:

```
MEME AS ORAL FORMULA ANALOG
=============================

Traditional oral formula:
  Metrically fixed phrase reused across contexts
  Modified by tradition bearers
  Community recognizes formula, fills in expected content

Internet meme:
  Template image / video / phrase format
  Reused across contexts by many users
  Community recognizes template, fills in new content

Parallels:
  Formula economy = meme template economy
    (Drakeposting, Distracted Boyfriend, etc.)
  Variation = meme remixing
  Community control = platform meme norms
  Decay of old formulas = meme death (oversaturation)

Key distinction from Ong's "secondary orality":
  Internet memes are textual but have ORAL characteristics:
  participatory, agonistic (competitive remixing),
  communal, redundant, formulaic
```

---

## Decision Cheat Sheet

| Framework | Author | What it explains |
|-----------|--------|----------------|
| Propp's 31 functions | Propp (1928) | Invariant sequence structure of fairy tales |
| ATU tale type index | Aarne, Thompson, Uther | Cross-cultural classification of narrative types |
| Myth/Legend/Folktale distinction | Bascom (1954) | Sacred vs. secular vs. believed |
| Urban legend analysis | Brunvand (1981+) | Contemporary oral narrative, FOAF structure |
| Structuralist myth analysis | Lévi-Strauss | Binary oppositions resolved by mediation |
| Meme as folklore | Shifman (2014) | Digital media as continuation of oral tradition |

---

## Common Confusion Points

**Propp's functions are specific to Russian fairy tales.** He analyzed the Afanasiev collection. The claim that all fairy tales have this structure is an extrapolation — partially supported but contested. The grammar applies widely to European Marchen; it is less applicable to myths, ballads, or non-European traditions.

**Myth does not mean "false story."** In academic usage, myth is a sacred narrative believed true within its tradition. Dismissing a tradition's myths as "just myths" conflates the scholarly term with the colloquial use.

**"Urban legend" does not mean an internet hoax.** It is an academic term for contemporary oral legend — a believed narrative in the legend tradition. Urban legends predate the internet; the internet is their new medium, not their origin.

**The ATU index has geographic bias.** It was built from European and Western Asian material. The Berezkin database is more globally comprehensive. Using ATU numbering for non-European traditions imposes European categories on different structures.

**Lévi-Strauss and Propp disagree fundamentally.** Propp: structure is temporal (sequence of events). Lévi-Strauss: structure is spatial (simultaneous oppositions that are read "like an orchestral score"). Both are right about different aspects; neither is complete.
