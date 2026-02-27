# Stagecraft and Production Design

## The Big Picture

Stagecraft is the technical art of making theater happen: scene design, lighting, sound, costume, and the organizational structure (production management, dramaturgy) that integrates them. It is simultaneously art (vision), engineering (execution), and project management (coordination).

<!-- @editor[diagram/P2]: The landscape diagram lists subsystems but doesn't show the coordination model — how the subsystems interact during a live performance. For this learner's calibration (lighting/sound/rigging as coordinated subsystems, live production as no-rollback system engineering) the missing layer is the integration architecture: the stage manager as the runtime coordinator calling all cues, DMX as the lighting control bus, the fly system as a load-bearing mechanical subsystem with its own rigging state. The diagram reads as a feature list, not a system diagram. -->
<!-- @editor[content/P1]: Rigging and fly systems are entirely absent from this guide. For a learner mapping stagecraft to systems engineering, the counterweight fly system is the most mechanically interesting subsystem: a fixed-capacity load-balancing system (counterweights matched to load), operated by line sets, with hard constraints on load distribution and timing. Hemp houses, counterweight linesets, motor-driven automation, and the grid/gallery/fly tower as the vertical infrastructure are all missing. This is a significant gap given the learner calibration explicitly names "rigging" as a target domain. -->
```
+------------------------------------------------------------------+
|              STAGECRAFT — LANDSCAPE                              |
+------------------------------------------------------------------+
|                                                                  |
|  DESIGN ELEMENTS                                                 |
|  Scene design: the physical world of the production             |
|  Lighting design: time, mood, focus, revelation                 |
|  Sound design: atmosphere, music, practical effects             |
|  Costume design: character, period, social status               |
|                                                                  |
|  STAGE ARCHITECTURE                                              |
|  Proscenium: picture frame stage (dominant form)               |
|  Thrust: stage projects into audience (3-sided)                 |
|  In-the-round: audience on all sides                            |
|  Black box: flexible space (variable configurations)           |
|  Environmental: audience and performers share same space        |
|                                                                  |
|  LIGHTING TECHNOLOGY EVOLUTION                                   |
|  Candles (pre-1800) → Gas (1820s) → Electricity (1882+)        |
|  Followspot → Ellipsoidal → PAR cans → Moving lights (1990s+) |
|  LED (2000s+) → Automated LED (present)                         |
|                                                                  |
|  PRODUCTION ORGANIZATION                                         |
|  Director + Designers + Stage Manager = production team         |
|  Dramaturgy: textual/research support for production           |
+------------------------------------------------------------------+
```

---

## Layer 1: Stage Architecture — The Configuration Is the Dramaturgy

The shape of the theatrical space is not neutral — it determines what kind of drama is possible.

```
STAGE CONFIGURATIONS
---------------------

PROSCENIUM (picture frame):
  +---------------------------+
  |   STAGE (performance)     |
  +=============================+  <- proscenium arch
  |         AUDIENCE           |
  +---------------------------+
  Audience: ONE direction only
  Stage: behind the arch, like a picture
  Strengths: rich illusionistic scenic design; clear sightlines
  Weaknesses: distance from audience; soliloquy awkward;
              the actor cannot look directly at the audience
              without looking "into the house" (formal)
  History: developed in Italy (16th-17th c.); dominant
           in commercial theater worldwide

THRUST:
  +---------------------------+
  |    AUDIENCE               |
  +---------------------------+
  |  AUD | STAGE  | AUDIENCE  |
  +------+--------+-----------+
  |        AUDIENCE           |
  +---------------------------+
  Audience: THREE sides
  Stage: projects into audience
  Strengths: intimacy; soliloquy is natural (you speak
             into surrounding audience); no "front"
  Weaknesses: every design choice must work from 3 angles;
              limited scenic flying capacity
  History: Shakespeare's Globe; RST (Royal Shakespeare
           Theatre) thrust version; many regional theaters

IN-THE-ROUND (arena):
  +--+--AUDIENCE--+--+
  |                   |
  A                   A
  U   [PERFORMANCE]   U
  D                   D
  |                   |
  +--+--AUDIENCE--+--+
  Audience: ALL FOUR sides
  Strengths: maximum intimacy; pure actor-audience focus
  Weaknesses: cannot have scenic walls; no flying;
              some audience always sees backs of actors
  History: many black box theaters; Chichester Festival;
           some Greek theaters

BLACK BOX:
  A flexible, neutral space. No fixed configuration.
  Audience and stage can be arranged any way:
  thrust, proscenium, in-the-round, traverse (two sides),
  promenade (audience moves through), environmental.
  The choice of configuration IS the first design decision.

ENVIRONMENTAL THEATER (Schechner):
  The distinction between performance space and
  audience space is dissolved. Audience and performers
  share the same space.
  See 09-PERFORMANCE-STUDIES.md for theory.
```

---

## Layer 2: Scene Design — A History

### Design Philosophy Through History

```
HISTORICAL SCENE DESIGN PROGRESSION
--------------------------------------
GREEK (5th c. BCE):
  Virtually no scenery. The skene is a building;
  pinakes (painted panels) in doorway slots.
  The "scenery" is verbal (text) and architectural (theater).

MEDIEVAL:
  "Mansions" (small structures representing locations
  placed around the performance area — Heaven at one end,
  Hell at the other, earthly locations between).
  The "platea" (neutral performance area between mansions)
  = anywhere.

RENAISSANCE ITALY (Serlio, 1545; perspective scenery):
  Single-point perspective painted backdrops.
  Wing-and-drop system: flat painted panels in slots
  to the side (wings) + painted backdrop at rear.
  Changeable by sliding wings and flying/dropping cloths.
  Spectacle becomes possible.

18th-19th CENTURY:
  Wing-and-drop increasingly elaborate.
  Charles Kean (1850s): archaeological accuracy
    (historically researched sets for Shakespeare).
  Gas lighting allows dimming (late 19th c.) →
    more subtle scenic illusion possible.
  "Box set" (Madame Vestris, 1832): a room with three
    walls and a ceiling, representing the interior
    realistically. The naturalist scene design.

APPIA AND CRAIG (c. 1900):
  Adolphe Appia (Swiss) and Gordon Craig (English):
  React against the flat painted scene.
  Three-dimensional platforms, ramps, steps.
  Lighting as design element (Appia especially).
  Selective, non-realistic: suggest rather than depict.
  Huge influence on 20th-c. design.

20th CENTURY:
  Unit set: a single design serves all scenes (more
    practical for repertory and touring).
  Environmental: no separation (Schechner, Living Theatre)
  Projections: slides, film, video projected onto stage
  Robert Wilson: pure design theater; slow movement;
    image as primary element, not story or character.

CONTEMPORARY:
  Digital projection (mapping): full 3D video mapping
  onto stage surfaces. The "set" can be a single white
  form onto which any environment is projected.
  LEDs as set elements (not just lighting instruments).
  Immersive: the entire building as set.
<!-- @editor[content/P2]: Projection mapping as a scene design technology deserves more than two sentences given the learner calibration explicitly names it as a target. The technical architecture: a media server (e.g., disguise/d3, Resolume) renders video in real-time; the output is warped/blended to correct for the non-planar surface geometry (mesh calibration); the result is projected via high-lumen projectors. Timecode sync (SMPTE or MIDI) locks the media server to the lighting console and audio playback, making the full production a synchronized multi-stream system. The computational geometry of mapping to arbitrary surfaces — calibration, warping, edge-blending — is directly in this reader's domain. -->
```

---

## Layer 3: Lighting Design — Technology and Art

Lighting is perhaps the most technically sophisticated design element. Its history is also a story of enabling dramatically new theatrical possibilities.

```
LIGHTING TECHNOLOGY HISTORY
-----------------------------
PRE-ELECTRICITY:
  Candles: uniform, warm, dim. No directional control.
    Chandeliers over the stage AND the audience (both lit).
    The audience and stage were in the same light.
    → No separation of audience from performance.
    → Performance was partly social (you could see who else
      was in the audience; they could see you).

  Oil lamps: brighter; controllable somewhat via wick.
  Limelight (1820s): calcium oxide heated to incandescence
    by oxyhydrogen flame. Very bright spot.
    The first instrument to create a "spotlight effect."
    "In the limelight" = exposed, celebrated.

GAS LIGHTING (from 1820s):
  Gas pipes to each light; centralized control possible.
  The DIMMER: reduce gas pressure to dim all lights.
  First systematic lighting control.
  The possibility of dimming changed what theater could do:
  scenes could begin and end in light/darkness.

ELECTRICITY (from 1882):
  Edison demonstrates practical electric light, 1879.
  The Savoy Theatre, London (1881) = first fully electric
  theater. Richard D'Oyly Carte, for Gilbert and Sullivan.
  Electric lighting was safer (no gas; fewer fires),
  brighter, and more controllable.

ELLIPSOIDAL (LEKO):
  The "Leko" (brand name from Levy and Kook — the inventors):
  An ellipsoidal reflector spotlight with a lens system
  that can project a sharp-edged beam.
  Gobos (cutout patterns) can create textures and shapes.
  The workhorse of theatrical lighting.

MOVING LIGHTS (from 1990s):
  Computer-controlled instruments with motorized pan,
  tilt, color, gobo rotation, iris, zoom.
  A single instrument can do in seconds what previously
  required manually refocusing many fixtures.
  The "intelligent light" revolution.

LED (from 2000s):
  Low power, cool, long life, no color gels needed
  (RGB or RGBW mixing). Eliminated many practical problems.
  Color mixing digitally vs. physical gel changes.

CONTEMPORARY:
  Full DMX/wireless control; the lighting console is
  a software application. The designer programs cues
  (states, transitions, timing) in advance; the stage
  manager executes them in performance.
<!-- @editor[bridge/P2]: DMX512 is a serial lighting control protocol — 512 channels per universe, 0-255 values, 44 Hz refresh rate. The lighting console is literally a real-time control plane: it holds the desired state (cue stack), and the stage manager calling "go" is a state transition trigger with no rollback. This is a compelling systems engineering parallel that the guide leaves implicit. The analogy: DMX universe = control bus; moving light = intelligent actuator; console = state machine with programmed transitions; the show = a sequence of pre-validated state transitions executed live with no ability to pause. One paragraph would make this section substantially more valuable for this reader. -->
```

### Lighting Functions

```
WHAT LIGHTING DOES
-------------------
1. VISIBILITY: the audience must be able to see the actors
   (fundamental; everything else follows)

2. FOCUS: what draws the eye? Where in the picture is
   the audience looking?
   Bright area draws attention; dark areas recede.
   A shaft of light isolates a single actor.

3. TIME OF DAY AND SEASON:
   Amber/warm → late afternoon, sunset
   Cold blue → night, moonlight, winter
   Neutral/white → noon, interior day
   Side-lighting → raking light, dawn or dusk angle

4. MOOD:
   Underlit face (light from below) → menace
   High side light → drama and form
   Front light → flatness, openness, vulnerability
   Top light → isolation, loneliness

5. REVELATION AND CONCEALMENT:
   Lighting brings things into being; darkness makes
   them not exist. A world is created and destroyed
   by the lighting states.

6. STYLE:
   Naturalistic (motivated sources: window, lamp)
   Non-naturalistic (arbitrary colored pools, isolations)
   Abstract (pure color and geometry; no naturalism)
```

---

<!-- @editor[content/P1]: The sound design section covers functions and categories but omits the signal chain architecture entirely — and for a systems-engineering-minded reader, the signal chain IS the sound design infrastructure: microphones → preamps → mixing console → DSP/processing → amplifiers → speaker arrays → monitoring. Spatial audio (described in the learner calibration as a target topic) gets one sentence at the end ("surround sound systems"). The signal chain, matrix routing, and the distinction between FOH (front of house) and monitor mixing are the engineering substance here. This section is thin relative to the lighting section which covered technology history in depth. -->
## Layer 4: Sound Design

Sound design was the last of the main design elements to be systematized (only recognized as a professional credit in major theater from the 1960s–70s):

```
SOUND DESIGN FUNCTIONS
-----------------------
1. LIVE MUSIC vs. RECORDED SOUND
   Live music (pit orchestra, stage musicians) = presence
   Recorded sound (playback) = control and repeatability
   Many productions mix both.

2. PRACTICAL SOUND EFFECTS
   "Practical" = sounds from visible sources
     (telephone rings, thunder, door knock)
   "Non-practical" = sounds with no visible source
     (underscoring, ambient, atmospheric)

3. ATMOSPHERIC SOUND
   Room tone: silence is not silent.
   A forest has birds, wind, insects.
   A city has traffic, voices, sirens.
   Ambient sound creates the world.

4. REINFORCEMENT
   Amplification of actors' voices.
   Controversial in classical theater (should voices
   be amplified? The "natural voice" tradition resists this).
   Musical theater: always amplified.
   Opera: almost never amplified.
   Drama: increasingly amplified, especially in large venues.

5. UNDERSCORING
   Music under dialogue (like film scoring).
   Manipulates emotional response.
   Used in musical theater; in drama more selectively.

SPATIAL SOUND:
   Surround sound systems in theaters allow sound to
   move through space: rain from above, traffic from
   the right, a crowd approaching from behind.
   Immersive theater makes extensive use of this.
```

---

## Layer 5: Production Organization

### The Production Team

```
PRODUCTION HIERARCHY
--------------------
ARTISTIC DIRECTOR (in a producing organization)
  |
DIRECTOR (production)
  |
  +---> SCENE DESIGNER -----> Technical Director (builds)
  |       (creates visual world)     | --> Scenic Artists (paint)
  |                                  | --> Carpenters (construct)
  |
  +---> LIGHTING DESIGNER --> Master Electrician (hangs, focuses)
  |       (creates light world)
  |
  +---> SOUND DESIGNER -----> A1 (sound board op)
  |       (creates sound world)
  |
  +---> COSTUME DESIGNER ---> Wardrobe Supervisor
  |       (creates clothing)          | --> Costume Shop
  |
  +---> CHOREOGRAPHER (if musical/dance)
  |
  STAGE MANAGER
    The spine of the production:
    - Schedules rehearsals
    - Maintains blocking records
    - Runs rehearsals (with director)
    - Calls cues in performance
    - The point of communication between all departments
    - The production's institutional memory
<!-- @editor[bridge/P1]: The stage manager role is described correctly but the no-rollback systems engineering parallel is never made explicit — and it's the sharpest bridge in this entire guide for the learner calibration. The stage manager calling cues is the runtime coordinator of a distributed system with no ability to pause, rewind, or retry: lighting, sound, fly, automation, and performance subsystems all execute on verbal "go" signals with no compensating transactions. The prompt copy is the execution plan; tech rehearsals are the integration testing phase; the production run is the deployment. A missed cue cannot be un-called; a fly cue that moves at the wrong moment has physical consequences. This is the operational model of a no-rollback system under SLA. Making this bridge explicit here — even two sentences — is the single highest-value edit in this file. -->

DRAMATURGY:
  The dramaturg provides research support, text analysis,
  historical context, consultation on translation.
  May help select/adapt texts.
  "The director's intellectual partner."
```

### Production Dramaturgy

```
WHAT A DRAMATURG DOES
----------------------
1. RESEARCH: historical context, biography, primary sources
   that inform the production's world-building

2. TEXT ANALYSIS: structural analysis, thematic mapping,
   identification of cruxes/problems in the text

3. ADAPTATION: if the production involves adapting a
   novel, historical document, or classic text, the
   dramaturg often does or supervises this work

4. AUDIENCE COMMUNICATION: program notes, study guides,
   pre-show talks

5. PRODUCTION SUPPORT: attends rehearsals; the "second pair
   of eyes" for the director; asks "why are we telling
   this story this way, for this audience, now?"

The dramaturg position is more established in German
and Scandinavian theater (where it was developed) than
in Anglo-American theater (where it is newer and more contested).

German: every major theater company has a Dramaturgie
  department with several dramaturgists.
English/American: the role varies enormously between
  institutions.
```

---

## Decision Cheat Sheet

| I want to understand... | Key section |
|------------------------|-------------|
| The different stage configurations and their dramatic consequences | Stage Architecture section |
| How scene design evolved from ancient to contemporary | Scene Design History section |
| What "limelight" means historically | Lighting Technology section |
| How moving lights work and why they changed theater | LED/Moving lights section |
| What lighting actually does dramatically | Lighting Functions section |
| What a stage manager does | Production Hierarchy section |
| What a dramaturg is | Production Dramaturgy section |

---

## Common Confusion Points

**"Scenery" in Greek theater was minimal**
The grand pictures of Greek theater we imagine are largely projections from the Roman and Renaissance theaters. Greek theater had a skene building, possibly some painted panels, and the elaborate architecture of the theater of Dionysus itself. The "scene" was largely verbal and architectural.

**Electric lighting did not immediately replace gas**
The transition from gas to electricity in theaters was gradual (1880s–1910s). Some theaters used both for a period. The advantages of electricity (safety, controllability, brightness) were obvious, but the investment was substantial and gas lighting was already sophisticated by the 1880s.

**"Black box" is not a style, it is a format**
A black box theater is a neutral space. What happens inside it can be any style — naturalistic, environmental, thrust, in-the-round. The flexibility is the point: the configuration is chosen per production, not fixed by the architecture.

**The stage manager in theater vs. film**
In theater, the stage manager is crucial throughout: they run rehearsals (director's right hand), maintain all records, and CALL THE SHOW in performance (saying "go" for every cue from a prompt copy). In film, the "stage manager" role splits between the 1st AD (on set) and the script supervisor (continuity). Theater stage managers have more authority and responsibility per production than their film equivalents.
