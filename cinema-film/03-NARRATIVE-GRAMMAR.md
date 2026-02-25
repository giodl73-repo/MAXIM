# Film Narrative Grammar: Shot Types, Continuity Editing, Parallel Editing, Eisenstein Montage

## The Big Picture

Film grammar is a system of conventions that the viewer has learned to decode. None of it is natural — a close-up on a face initially alarmed audiences (a severed head?). The grammar was built through trial and error by filmmakers from 1895-1930 and has been codified and internalized so thoroughly that modern viewers process it unconsciously.

```
FILM NARRATIVE GRAMMAR HIERARCHY

UNIT 1: THE SHOT (basic building block)
  Duration: from camera-start to camera-cut
  Parameters: framing, angle, movement, focus, exposure
  Analogous to: a statement in a programming language

UNIT 2: THE CUT (transition between shots)
  Joining principle: continuity, contrast, rhythm, meaning
  Types: cut, dissolve, fade, wipe, jump cut, match cut
  Analogous to: operator connecting statements

UNIT 3: THE SCENE (shots forming a unit of action)
  One continuous time/space unit (or connected through editing)
  Function: narrative beat, emotional unit
  Analogous to: a function

UNIT 4: THE SEQUENCE (scenes forming a narrative unit)
  Multiple scenes connected by theme, causality, time
  Act structure, genre conventions at this level
  Analogous to: a module or class

UNIT 5: THE FILM (complete work)
  Three-act structure (Syd Field, 1979, but ancient roots)
  Genre expectations, character arcs
  Analogous to: a complete application

Grammar is what allows meaning to be assembled from shots.
Without grammar conventions, a sequence of shots = no coherent story.
With grammar conventions, two shots can imply vastly more than either shows.
(See: Kuleshov Effect in 08-EDITING-THEORY.md)
```

---

## Shot Types and Framing

```
SHOT SIZE TAXONOMY (standard Hollywood convention)

ECU  EXTREME CLOSE-UP
     Eyes only, texture of skin
     Use: extreme psychological intensity, detail
     |  [           ]  |
     |  [  eyes    ]  |
     |  [           ]  |

CU   CLOSE-UP
     Face from chin to above head
     Use: emotional state, reaction, emphasis
     |  [              ]  |
     |  [    face      ]  |
     |  [              ]  |

MCU  MEDIUM CLOSE-UP (also: "bust shot")
     Head and shoulders
     Use: dialogue, two-person conversation
     |  [              ]  |
     |  [  head+       ]  |
     |  [  shoulders   ]  |

MS   MEDIUM SHOT
     From waist/hips to head
     Use: action + reaction, walking
     |  [              ]  |
     |  [  waist-up    ]  |
     |  [              ]  |

MLS  MEDIUM LONG SHOT (also: "American shot" or "cowboy shot")
     Thighs/knees to head
     Use: shows hands (for action), standard coverage
     |  [              ]  |
     |  [  knees-up    ]  |
     |  [              ]  |

LS   LONG SHOT (also: "full shot")
     Full body, some environment
     Use: action, location, relationship between person and space
     |  [full body +   ]  |
     |  [environment   ]  |

VLS  VERY LONG SHOT (also: "wide shot" or "establishing shot")
     Subject small in frame; environment dominant
     Use: establish location, scale, isolation
     |  [landscape/    ]  |
     |  [environment   ]  |
     |  [  . subject . ]  |

ELS  EXTREME LONG SHOT (also: "aerial shot", "God's eye view")
     Subject barely visible; geography/context dominant
     Use: extreme isolation, geography, epic scale
```

---

## Camera Angles

```
CAMERA ANGLE TAXONOMY

ANGLE         | SETUP                      | EFFECT
--------------+----------------------------+--------------------------------
Eye level     | Camera at subject's        | Neutral; naturalistic
              | eye height                 | Most common for dialogue
--------------+----------------------------+--------------------------------
High angle    | Camera above subject,      | Subject appears smaller,
              | shooting down              | weaker, diminished
              |                            | Used: Citizen Kane's Boss;
              |                            | Hitchcock's Psycho shower
--------------+----------------------------+--------------------------------
Low angle     | Camera below subject,      | Subject appears larger,
              | shooting up                | powerful, threatening
              |                            | Used: Orson Welles as Kane;
              |                            | superhero landings
--------------+----------------------------+--------------------------------
Bird's eye    | Directly overhead,         | Abstract; disorienting;
(Top-down)    | 90 degrees                 | pattern/composition
              |                            | Used: Busby Berkeley musicals
--------------+----------------------------+--------------------------------
Dutch angle   | Camera tilted on           | Psychological instability,
(canted)      | longitudinal axis          | unease, disorientation
              |                            | Used: expressionist films,
              |                            | horror, thrillers
--------------+----------------------------+--------------------------------
Point-of-view | Camera placed where        | Viewer = character; subjective
(POV)         | character's eye would be   | Used: Murnau's "The Last Laugh";
              |                            | modern FPS sequences
```

---

## Camera Movement

```
CAMERA MOVEMENT TYPES

PAN (panoramic)
  Camera ROTATES horizontally on fixed head (tripod)
  Left pan / right pan
  Use: follow action, reveal environment
  Hardware: tripod + fluid head

TILT
  Camera ROTATES vertically on fixed head
  Tilt up / tilt down
  Use: reveal height, follow vertical action, symbolic (power)
  Hardware: tripod + fluid head

DOLLY (tracking)
  Camera MOVES horizontally (on wheeled platform = dolly)
  Dolly in = camera moves toward subject (different from zoom)
  Dolly out = camera moves away
  Use: emotional intimacy/distance (Hitchcock "dolly zoom")
  Hardware: dolly on rails or dolly on wheels

TRUCKING (lateral dolly)
  Camera moves parallel to subject's movement
  Follow walking character from side
  Hardware: same as dolly

DOLLY ZOOM (Hitchcock effect / "Vertigo effect")
  Dolly out WHILE zooming in (or vice versa)
  Subject stays same size; background changes size
  Effect: spatial distortion, dread, unreality
  First: Vertigo (1958, Hitchcock)
  Optical physics: zoom changes focal length + field of view;
                   dolly changes perspective;
                   combined: compensate subject size while
                   distorting background size

CRANE
  Camera moves vertically (up or down), often with horizontal
  Use: reveal scale, God's-eye transitions, sweeping shots

STEADICAM (Garrett Brown, 1975)
  Camera on body-mounted stabilizer system
  Counterbalanced: operator can walk/run without camera shake
  Characteristic movement: smooth but slightly "organic"
  First major use: Rocky (1976), The Shining (1980)
  Hardware: Arri, Tiffen, MōVI (digital gimbals)

HANDHELD
  Camera held by operator
  Characteristic: slight shake, movement, "reality" feel
  Use: documentary, action, intimacy, verisimilité
  New Wave: Godard, Cassavetes stylized this

DRONE (aerial)
  Remote-controlled aerial gimbal-stabilized camera
  Enabled: complex aerial shots at ~1/100th of helicopter cost
  Changed: establishing shots, action sequences
```

---

## Continuity Editing System

The Hollywood continuity system (developed 1907-1920s) is a set of conventions designed to make editing invisible — to create the perception of seamless continuous space and time from discontinuous shots.

```
THE 180° RULE (THE AXIS OF ACTION)

Setup: two characters facing each other in conversation

      Character A              Character B
          |                        |
          v                        v
      [Left side]     -------> [Right side]
                     Action axis
                     (line of action)

Camera positions ALLOWED (stay on ONE side of axis):

  Position 1: Camera left of A, shooting right
              A: left frame    B: right frame
              A: faces right   B: faces left

  Position 2: Camera between them, angled toward B
              A in background left, B in foreground right

  Position 3: Camera right of B, shooting left
              A: right frame   B: left frame
              A: faces right   B: faces left

  Positions 1, 2, 3 all cut seamlessly: spatial logic preserved

CROSSING THE LINE (violation):
  Camera crosses to other side of axis
  A and B: both now face same direction
  Viewer: loses spatial orientation
          "Where are these people relative to each other?"
  Jarring, disorienting

  LEGITIMATE VIOLATIONS:
  - New camera move establishes new axis during shot
  - POV shot: briefly cross if character turns
  - Deliberately for disorientation effect (horror, action chaos)
  - Eisenstein intentionally violated rules for montage effect
```

---

## The Continuity Editing Rules

```
CONTINUITY EDITING CONVENTIONS

MATCH ON ACTION:
  Cut mid-movement on both sides of cut
  Character opens door -> CUT -> (different angle) door finishing opening
  Brain: fills in gap, perceives continuous action
  Rule: action state must match at cut point
  Exception: jump cut (intentional discontinuity)

EYELINE MATCH:
  Character looks in direction X
  CUT TO: what they're looking at
  Basic: A looks left -> B (to A's left) faces right
  Advanced: A looks out window -> CUT TO exterior view
  Establishes: spatial relationship between characters and objects

CUT ON LOOK (reaction shot):
  Show A looking -> CUT TO -> what A sees
  Then: CUT BACK to A's reaction
  This is the basic building block of scene construction
  Kuleshov demonstrated this creates meaning (see editing module)

SHOT-REVERSE-SHOT (SRS):
  Most common dialogue construction:
  Shot of A (over B's shoulder) -> CUT -> Shot of B (over A's shoulder)
  Alternating: creates sense of exchange, conversation
  Over-shoulder: maintains spatial relationship
  The 180° rule enables this to work

ESTABLISHING SHOT -> COVERAGE:
  Begin scene: wide establishing shot (shows space, characters)
  Then: closer coverage (medium, close-up)
  This sequence: tells audience where everything is
  before showing them details

SCREEN DIRECTION MATCHING:
  Action moving right-to-left in shot A
  Cut to shot B: action must continue right-to-left
  (Or: transition shot explicitly showing direction change)
  Violation: subject appears to reverse direction instantly
```

---

## Parallel Editing (Cross-Cutting)

```
PARALLEL EDITING (CROSSCUTTING)

DEFINITION:
  Alternating between two or more simultaneous actions
  in different locations
  Creates: temporal relationship between events

STRUCTURE:
  Scene A (hero riding to rescue)
  Scene B (heroine in danger)
  A → B → A → B → A → B → [CONVERGENCE]
  A + B happening simultaneously
  Final: A and B meet

EMOTIONAL MECHANISM:
  Each cut back to B: viewer knows hero is getting closer
  Each cut back to A: tension — will he arrive in time?
  Temporal compression: 30 minutes of story in 3 minutes of film
  The audience's knowledge (hero is coming) vs character's lack of knowledge
  = suspense engine

GRIFFITH'S LAST MINUTE RESCUE (1908+):
  Standardized the "last minute rescue" as genre formula
  Template: anyone in trouble + anyone coming to help + intercutting = suspense
  Still used constantly: action films, thrillers

PURE PARALLEL (no convergence):
  The Godfather baptism sequence (Coppola, 1972):
  Michael in church for baptism (peaceful, religious)
  His men executing rivals (violent)
  No convergence, no chase
  Intercutting creates: IRONY (Michael's public piety vs private violence)
  This is montage logic: meaning from juxtaposition, not from continuity
```

---

## Soviet Montage Theory

Eisenstein and the Soviet filmmakers (1920s) rejected Hollywood continuity editing and developed an alternative theory: meaning emerges from COLLISION between shots, not seamless connection.

```
EISENSTEIN'S MONTAGE THEORY

BASIC PREMISE:
  Hollywood continuity: shots = transparent, create immersive space
  Eisenstein: shots = meaningful elements; collision creates concept

  A + B (Eisenstein) ≠ A followed by B (continuity)
  A + B = a new idea C, not contained in either A or B

  Mathematical model: THESIS + ANTITHESIS = SYNTHESIS
                      (Dialectical materialism applied to cinema)

  A: image of fat capitalist
  B: image of peacock preening
  Viewer: perceives "the fat capitalist is vain as a peacock"
  This meaning is NOT in either shot; it's constructed by juxtaposition

  This is exactly the Kuleshov effect generalized to meaning-making

EISENSTEIN'S TYPES OF MONTAGE:
  (from his 1929 essay "Methods of Montage")

  1. METRIC MONTAGE:
     Cut on absolute time length (e.g., every 2 seconds)
     Rhythmic, musical, visceral
     Effect: matches to music beat, physical tension

  2. RHYTHMIC MONTAGE:
     Cut based on content movement (action creates rhythm)
     Moving content in shot governs cut length
     Odessa Steps sequence: rhythm from marching soldiers

  3. TONAL MONTAGE:
     Cut based on dominant emotional tone of shot
     Grief = slow, low-contrast shots; Joy = fast, bright shots
     Emotional "key" of shot governs assembly

  4. OVERTONAL MONTAGE:
     Combination of all three simultaneously
     Multiple rhythms operating together

  5. INTELLECTUAL MONTAGE:
     Juxtapose conceptually unlike images to create abstract idea
     Most radical; most theoretical
     Workers uprising + slaughter of cattle = workers as cattle
     (Strike, 1925)

BATTLESHIP POTEMKIN (1925):
  Odessa Steps sequence:
  Tsarist troops march down steps, massacre civilians
  Rhythmic montage: march pace + intercut close-ups
  Axial cuts: same direction, varying distance
  155 cuts in 4 minutes (fast for era)
  "Baby carriage on steps" = most quoted image in film analysis
  No record: actual massacre on Odessa steps didn't happen
  (Eisenstein constructed the emotional truth, not historical fact)

INFLUENCE ON ADVERTISING:
  Montage theory is literally the grammar of advertising
  Cut fast: product + aspirational image + product + desire
  Apple's "1984" Super Bowl ad: Eisenstein structure
  Every music video: montage, not continuity
```

---

## Sound-Image Relationship

```
SOUND-IMAGE RELATIONSHIPS (Brief — see 04-SOUND-COLOR for full coverage)

DIEGETIC SOUND: Sound that exists within the story world
  Characters can hear it
  Examples: dialogue, footsteps, traffic, music playing on screen

NON-DIEGETIC SOUND: Sound that exists outside the story world
  Characters cannot hear it; only audience hears
  Examples: orchestral score, voiceover narration

COUNTERPOINT (Eisenstein's sound theory):
  Sound contradicts image for effect
  Violent image + gentle music = disturbing irony
  Kubrick: "Singin' in the Rain" in A Clockwork Orange
           "Blue Danube" in 2001's space dock sequence
  The contradiction creates meaning

SOUND BRIDGE:
  Sound from next scene plays over tail of current scene
  Or: sound from current scene continues over head of next
  Creates: smooth transition; expectation/revelation structure
```

---

## Decision Cheat Sheet

| Element | Description | Function |
|---------|-------------|---------|
| Establishing shot | Wide; shows space and character positions | Spatial orientation for viewer |
| 180° rule | Cameras on one side of action axis | Prevents spatial disorientation |
| Match on action | Cut in mid-movement | Creates continuous perceived action |
| Eyeline match | Look -> cut to what's seen | Establishes spatial relationship |
| Shot-reverse-shot | Alternate faces in dialogue | Standard conversation construction |
| Crosscutting | Alternate simultaneous events | Creates suspense, irony, temporal connection |
| Jump cut | Cut within same scene, discontinuous | Time ellipsis, psychological effect |
| Kuleshov effect | Same face + different context = different meaning | Editing creates meaning not in shots |
| Metric montage | Cut on absolute time intervals | Rhythmic, visceral, musical |
| Intellectual montage | Juxtapose for concept creation | Abstract meaning from unlike images |

---

## Common Confusion Points

**"Violating the 180° rule is always bad."** It's jarring only if unintentional or unexplained. Many filmmakers deliberately cross the line for effect: disorientation in action (battle sequences deliberately confuse), psychological instability (horror), or marking narrative transitions. The rule exists to be broken knowingly, not as an absolute constraint.

**"Jump cuts are editing errors."** Before Jean-Luc Godard's Breathless (1960), they essentially were — accidents in continuity. Godard used jump cuts deliberately to break the illusion of continuous time, emphasize the artifice of cinema, and create a fragmented, anxious rhythm. Jump cuts now signal: stylistic modernity, YouTube-era editing, documentary roughness, or deliberately Godardian affectation depending on context.

**"Eisenstein's theory is the opposite of Hollywood."** They're different aesthetic programs, but both are theories of how edited sequences create meaning. Hollywood continuity says meaning flows from immersive narrative; Eisenstein says meaning emerges from conceptual collision. Most films use both: continuity for scene structure, montage logic for thematic sequences (the Godfather baptism; match cuts; any dream sequence).

**"The 'grammar' is universal."** It's not. Western continuity conventions are culturally learned. Research shows that audiences without exposure to Hollywood-style editing initially misread eyeline matches, temporal relationships, and spatial constructions from continuous editing. The grammar was learned by Western audiences over decades of cinema-going. Audiences in newly mediated cultures initially find cross-cutting confusing.
