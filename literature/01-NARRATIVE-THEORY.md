# Narrative Theory

## The Big Picture

Narrative theory (narratology) is the formal study of how stories are structured. It is genuinely formal — in the same spirit as structural linguistics — and produces taxonomies and grammars of story construction. The two dominant traditions are the Russian/French structuralist line (Propp → Greimas → Genette) and the Anglo-American analytic line (Wayne Booth, Seymour Chatman, David Herman).

```
+------------------------------------------------------------------+
|                   NARRATIVE THEORY — LANDSCAPE                   |
+------------------------------------------------------------------+
|                                                                  |
|  THE FUNDAMENTAL DISTINCTION                                     |
|  Story (WHAT happens)  vs.  Discourse (HOW it is told)          |
|                                                                  |
|  Russian: fabula  (abstract story events in chronological order) |
|           syuzhet (the concrete arrangement in the text)         |
|  French:  histoire (story) vs. recit (narrative text)           |
|  English: story    vs.  plot                                     |
|                                                                  |
|  STRUCTURAL APPROACHES (deep grammar)                            |
|  Propp (1928)    — 31 functions + 7 character spheres            |
|  Greimas (1966)  — 6 actants, semantic square, narrative grammar |
|  Todorov (1969)  — narrative = equilibrium → disruption → new eq.|
|                                                                  |
|  DISCOURSE APPROACHES (how stories are told)                     |
|  Genette (1972)  — narratological taxonomy (5 dimensions)        |
|  Booth (1961)    — implied author, unreliable narrator           |
|  Chatman (1978)  — story vs. discourse theory                    |
|                                                                  |
|  COGNITIVE APPROACHES (how minds process stories)                |
|  Herman (2002)   — story logic, storyworld construction          |
|  Fludernik (1996)— experientiality as narrative criterion         |
|  Zunshine (2006) — theory of mind and narrative (why we read)    |
+------------------------------------------------------------------+
```

---

## Layer 1: The Fabula/Syuzhet Distinction

This is the foundational cut in narrative theory, introduced by the Russian Formalists (Shklovsky, Tomashevsky, Eikhenbaum) in the 1910s–20s.

```
FABULA                           SYUZHET
------                           -------
Abstract chronological order     The text's actual arrangement
of story events                  of those events

"What happened"                  "How it is told"

A, B, C, D, E                    C, A, D, B, E
(chronological)                  (in medias res + flashbacks)

Always linear                    Can be non-linear, recursive,
in the fabula                    fragmented, multi-threaded

Independent of text              The text itself

Examples:
  Fabula: Hamlet's father dies;  Syuzhet: play opens with ghost,
  ghost appears; Hamlet learns;  works backward to reveal murder,
  Hamlet delays; everyone dies.  forward through Hamlet's choices.

  Fabula: WWII in chronological  Syuzhet: Slaughterhouse-Five
  order 1939–1945                jumps between Billy Pilgrim's
                                 life, Dresden, and Tralfamadore.
```

The gap between fabula and syuzhet is where **literary technique lives**. In medias res, analepsis (flashback), prolepsis (flash-forward), ellipsis, summary — all are syuzhet manipulations of the fabula.

---

## Layer 2: Propp's Morphology — Narrative as Formal Grammar

Vladimir Propp's **Morphology of the Folktale** (1928, translated 1958) is one of the most genuinely formal contributions to literary theory. It is not a metaphor — it is a structural analysis that yields a generative grammar for a corpus of 100 Russian fairy tales.

### The Key Move

Propp observed that previous classifications of folk tales by theme or character were unstable. His insight: what is stable is **function** — the role an action plays in the narrative, regardless of which character performs it.

```
PROPP'S METHOD
--------------
1. Collect corpus of 100 Russian fairy tales
2. Identify all narrative "moves" (functions)
3. Observe: functions are ALWAYS performed in the same order
4. Observe: any given tale performs a SUBSET of the functions
5. Result: a finite ordered sequence of 31 functions

This is essentially:
  - An alphabet of 31 symbols (functions)
  - A grammar rule: any tale is a subsequence of the
    canonical 31-function sequence
  - Tales are "derivations" from this grammar

Compare: BNF grammar, where non-terminals have
fixed expansions and sentences are derivation paths.
```

### The 31 Functions (condensed)

```
INITIAL SITUATION (not a function, labeled alpha)
I.   Absentation — member of family leaves home
II.  Interdiction — prohibition issued to hero
III. Violation — interdiction is violated
IV.  Reconnaissance — villain seeks information
V.   Delivery — villain gains information
VI.  Trickery — villain attempts to deceive hero
VII. Complicity — hero is deceived
VIII.Villainy — villain causes harm OR lack established
IX.  Mediation — misfortune known; hero dispatched
X.   Beginning counter-action — hero agrees to act
XI.  Departure — hero leaves home
XII. First function of donor — hero is tested
XIII.Hero's reaction — hero passes/fails test
XIV. Provision — hero acquires magical agent
XV.  Spatial translocation — hero led to object
XVI. Struggle — hero and villain fight
XVII.Branding — hero is branded/marked
XVIII.Victory — villain is defeated
XIX. Initial misfortune liquidated
XX.  Return — hero returns
XXI. Pursuit — hero is pursued
XXII.Rescue — hero is saved
XXIII.Unrecognized arrival — hero arrives unrecognized
XXIV. Unfounded claims — false hero presents false claims
XXV.  Difficult task — difficult task proposed to hero
XXVI. Solution — task is resolved
XXVII.Recognition — hero is recognized
XXVIII.Exposure — false hero/villain is exposed
XXIX. Transfiguration — hero is given new appearance
XXX.  Punishment — villain is punished
XXXI. Wedding — hero is married, ascends throne
```

### Character Spheres (Typed Roles)

Propp identified **7 character spheres** (typed functional roles, not psychological characters):

| Sphere | Function |
|--------|----------|
| Villain | Causes harm, creates conflict |
| Donor | Provides magical agent after testing hero |
| Helper | Assists hero |
| Princess (Sought-for person) | Goal of hero's quest; rewards hero |
| Dispatcher | Sends hero on quest |
| Hero | Performs the quest, liquidates harm |
| False Hero | Claims credit, gets exposed |

One character can occupy multiple spheres; one sphere can be split across characters. This is **role typing without character essentialism**.

---

## Layer 3: Greimas's Actantial Model

A.J. Greimas in **Structural Semantics** (1966) formalized Propp into a more abstract, universal actantial grammar applicable to any narrative, not just folktales.

```
GREIMAS'S ACTANTIAL MODEL
--------------------------

        SENDER ---------> OBJECT ---------> RECEIVER
          |                  |                  |
          |                  |                  |
          +---------> SUBJECT <---------+       |
                       (Hero)           |       |
                          |             |       |
                       HELPER      OPPONENT     |
                          |             |       |
                          v             v       |
                    assists hero   opposes hero  |
                                                |
Example: Hamlet
  Sender:   Ghost (dispatches quest)
  Object:   Justice/revenge
  Receiver: Denmark / the Ghost
  Subject:  Hamlet
  Helper:   Horatio
  Opponent: Claudius + Hamlet's own hesitation

Example: Software project
  Sender:   Business need / customer
  Object:   Working product
  Receiver: Users / stakeholders
  Subject:  Engineering team
  Helper:   Platform tools, infrastructure
  Opponent: Technical debt, scope creep, time
```

The actantial model is a **semantic frame** — a typed relational structure that any narrative instantiates. Every story is a mapping from its characters and events onto this frame.

### The Semantic Square

Greimas also proposed a formal device for mapping conceptual oppositions:

```
SEMANTIC SQUARE
---------------
       S1 -------------------- S2
    (positive)            (contrary)
       |         \  /          |
       |          \/           |
       |          /\           |
       |         /  \          |
      ~S2 ------------------  ~S1
  (sub-contrary)          (negative)

Example: Life vs. Death
  S1 = Life        S2 = Death
  ~S2 = Not-death  ~S1 = Not-life (the undead, inert)

This is used to map the ideological tensions
in a narrative. A story "resolves" by moving
through the square.
```

---

## Layer 4: Genette's Narratological Taxonomy

Gerard Genette's **Narrative Discourse** (1972) is the most comprehensive formal taxonomy of HOW stories are told. It analyzes Marcel Proust's *In Search of Lost Time* but the framework is general.

Genette identifies **three levels** and **five dimensions**:

```
THREE LEVELS
------------
Histoire  = story (the sequence of events)
Recit     = narrative text (the actual words on the page)
Narration = the act of narrating (who tells, when, how)

FIVE DIMENSIONS OF DISCOURSE
-----------------------------

1. ORDER (when events are narrated relative to story time)
   Analepsis    = flashback (narrate past events now)
   Prolepsis    = flash-forward (narrate future events now)
   Anachrony    = any deviation from chronological order
   Example: Citizen Kane (prolepsis from death, then analepsis)

2. DURATION (how long narration takes vs. story time)
   Scene        = narration time = story time (dialogue)
   Summary      = narration time < story time (decades in a page)
   Ellipsis     = narration time = 0, story time passes (gap)
   Stretch      = narration time > story time (slow motion)
   Pause        = narration time = infinity, story time = 0
                  (description, digression)

3. FREQUENCY (how often events are narrated)
   Singulative  = once told once = happened (normal)
   Repeating    = n times told once (told multiple times)
   Iterative    = once told what happened n times ("every morning...")

4. MOOD (distance and perspective)
   Focalization = "who sees" (perspective/point of view)
   - Zero foc.     = omniscient narrator
   - Internal foc. = a character's perspective
   - External foc. = camera eye (behaviorist, no interiority)
   Distance     = how much narrator mediates vs. shows

5. VOICE (who narrates and when)
   Homodiegetic = narrator is in the story (first person)
   Heterodiegetic = narrator outside the story (third person)
   Autodiegetic = narrator is the protagonist
   Extradiegetic = narrator at highest narrative level
   Intradiegetic = narrator within a story (embedded narrator)
   Metalepsis   = crossing narrative levels (Calvino's trick)
```

---

## Layer 5: Unreliable Narrator

Wayne Booth coined **"unreliable narrator"** in **The Rhetoric of Fiction** (1961). An unreliable narrator's account diverges from the implied author's norms — but the reader must detect this divergence.

```
RELIABILITY SPECTRUM
--------------------

TRUSTWORTHY                              UNRELIABLE
-----------                              ----------
Nick Carraway      Stevens             Stevens           Humbert
(Great Gatsby)     (Remains of        (on his           Humbert
-- fairly honest   the Day)           suppressed        (Lolita)
about others,      -- honest on       emotion)          -- full
naive about        surface, massive                     manipulator
himself            self-deception

TYPES OF UNRELIABILITY
----------------------
1. Naive narrator    — lacks knowledge or maturity to understand
                       what they report (Holden Caulfield in parts,
                       Watson to Holmes, Stevens in Remains)

2. Mentally ill      — perception is distorted (Governess in Turn
                       of the Screw — ambiguous, contested)

3. Lying narrator    — deliberately deceives reader (Humbert)

4. Limited narrator  — simply cannot know certain things
                       (not "unreliable" in a judgment sense,
                       just epistemically bounded)

The IRONY of unreliable narration:
  The reader constructs a "true" story from the gap between
  what the narrator says and what the text implies.
  The implied author speaks through the gap.
```

---

## Layer 6: Narrative Levels and Metalepsis

Genette introduced the concept of **diegetic levels** — stories within stories create hierarchical levels:

```
NARRATIVE LEVELS
----------------

Level 1 (Extradiegetic): The frame narrator
  |
  v
Level 2 (Intradiegetic): Character tells a story
  |
  v
Level 3 (Metadiegetic): That character's character tells a story

Example: Arabian Nights
  Level 1: Scheherazade narrates to Shahryar
  Level 2: Sinbad narrates his voyages
  Level 3: Person in Sinbad's tale narrates something

METALEPSIS: violating the hierarchy
  Narrator enters the story (author intrusion)
  Character escapes the story (Pirandello's Six Characters)
  Calvino: "You are about to begin reading Italo Calvino's
           new novel, If on a winter's night a traveler."
           — narrator addresses YOU, the reader, directly

This is not just a postmodern trick — it makes the frame
visible, like breaking the fourth wall in theater.
Brecht used this deliberately (see 03-DRAMA.md).
```

---

## The Narrative Turn in Other Disciplines

Since the 1980s, "narrative theory" has spread beyond literary study:

```
NARRATIVE IN OTHER FIELDS
--------------------------
Cognitive science:   Story is how minds organize experience
                     (Schank & Abelson "scripts", mental models)
                     We comprehend events by fitting them to
                     narrative schemas.

Psychology:          Narrative identity (MacAdams) — people
                     construct identity by narrating their lives
                     as a coherent story.

History:             Hayden White "Metahistory" — historical
                     writing uses narrative emplotment (comedy,
                     tragedy, romance, satire). History is not
                     just about events but their narrative form.

Law:                 Narrative theory applied to trial argument
                     — juries decide by which story is more
                     coherent, not just which facts win.

AI/NLP:              Story generation, narrative planning,
                     script theory, commonsense reasoning.
                     GPT models are, among other things,
                     very good narrative prediction engines.
```

---

## Decision Cheat Sheet

| I want to analyze... | Tool |
|---------------------|------|
| The abstract plot structure of a story | Fabula/syuzhet distinction |
| What character types appear and what roles they play | Propp's 7 spheres |
| The 31 narrative "moves" in a story | Propp's morphology |
| The deep relational grammar of any narrative | Greimas's actantial model |
| How a story handles time (flashbacks, summary, pacing) | Genette's ORDER and DURATION |
| Whose perspective filters the story | Genette's FOCALIZATION (mood dimension) |
| Whether the narrator can be trusted | Booth's unreliable narrator |
| Stories within stories | Genette's diegetic levels, metalepsis |
| How readers cognitively process story | Herman's story logic, Zunshine's theory of mind |

---

## Common Confusion Points

**Story vs. Plot vs. Discourse**
These terms have inconsistent usage. Aristotelian "plot" (mythos) ≈ fabula. Russian Formalist "syuzhet" ≈ what most people call "plot" in everyday speech (the arrangement). Genette's "recit" ≈ the text itself. The word "story" is ambiguous — in everyday use it means the whole thing; in narratology it means the abstract event sequence only.

**Focalization is not the same as point of view or narration**
Genette's distinction: focalization is WHO SEES; narration is WHO SPEAKS. A heterodiegetic (third-person) narrator can focalize through a character. Emma Woodhouse is not the narrator of Emma, but the novel is focalized through her — we see what she sees, understand what she understands (and misunderstands). Point of view is the looser colloquial term for the same phenomenon.

**Propp's functions are ordered — this is the key claim**
It is not just that there are 31 function types. The claim is that they appear in a fixed sequence. Any given tale is a subsequence, but never out of order. This is the falsifiable (and frequently tested) empirical claim of the morphology.

**Greimas's actants are not characters**
One character can fill multiple actant slots; one actant slot can be filled by multiple characters or by abstractions (Hamlet's own conscience as an opponent). The actantial model is a semantic role structure, not a character taxonomy.
