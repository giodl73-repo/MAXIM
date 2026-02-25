# Industrial Design — Landscape and Taxonomy

## The Big Picture

Industrial design is the engineering discipline of making manufactured objects both functional and meaningful to human users. It sits at the intersection of engineering constraints, human factors, materials science, manufacturing processes, and cultural semiotics. The bridge to software: industrial design is constraint satisfaction under competing optimization targets -- performance, aesthetics, manufacturability, cost, sustainability, and user experience.

```
+----------------------------------------------------------------------+
|           INDUSTRIAL DESIGN AS CONSTRAINT SATISFACTION               |
|                                                                      |
|  INPUTS                    PROCESS                    OUTPUTS        |
|                                                                      |
|  User needs            --> Problem definition     --> Product        |
|  Engineering limits    --> Research               --> System         |
|  Manufacturing costs   --> Ideation               --> Service        |
|  Material properties   --> Prototyping            --> Interface      |
|  Cultural context      --> Testing                --> Experience     |
|  Aesthetic intent      --> Refinement             --> Identity       |
|  Sustainability req.   --> Production             --> Ecosystem      |
|                                                                      |
|  DISCIPLINES WITHIN INDUSTRIAL DESIGN:                               |
|  Product design | Transportation design | Furniture design           |
|  UI/UX (digital) | Service design | Systems design                   |
|  Environmental design | Medical devices | Military equipment         |
+----------------------------------------------------------------------+
```

---

## Taxonomy: Design by Scale and Domain

### By Scale

```
PRODUCT SCALE         DESCRIPTION                       EXAMPLES
-------------------+----------------------------------+--------------------
Micro (sub-1cm)    | Components, connectors, fasteners | USB connector, zipper
Handheld           | Hand-operated objects             | Phone, pen, toothbrush
Appliance          | Countertop/room-scale             | Kettle, coffee maker
Furniture          | Room-defining objects             | Chair, table, lamp
Architectural      | Building-integrated               | Door handle, stair railing
Vehicle            | Self-contained systems            | Car, bicycle, aircraft
Infrastructure     | Urban scale                       | Transit system, kiosk, sign
```

### By Relationship to User

```
PROXIMITY TO BODY           EXAMPLES                   KEY CONCERNS
------------------------+---------------------------+---------------------
Worn (wearables)        | Watch, glasses, prosthetics | Comfort, weight, skin
Handheld                | Tools, phones, controllers  | Grip, balance, haptics
Operated (contact)      | Chair, keyboard, steering   | Posture, reach, force
Used at distance        | TV, public kiosk, appliance | Visual, legibility
Environmental (passive) | Architecture, urban furn.   | Navigation, identity
```

---

## The Design Disciplines That Comprise Industrial Design

```
INDUSTRIAL DESIGN FAMILY TREE

  INDUSTRIAL DESIGN (1919-)
  [Making manufactured objects better for humans]
         |
    _____|_____________________________________
   |           |           |          |        |
   v           v           v          v        v
PRODUCT     TRANSPORT   FURNITURE   CONSUMER  MILITARY/
DESIGN      DESIGN      DESIGN      ELECTRON- DEFENSE
(broadest)  (cars/bikes  (chairs,   ICS       (ergonomics
            /aircraft)   storage)              under stress)
                                |
                                v
                         INTERACTION DESIGN (1980s+)
                         [GUI, UX, service design]
                                |
                                v
                         UX / SERVICE DESIGN (1990s+)
                         [Digital product experience]
```

---

## Historical Movements: The 200-Year Arc

```
+---------------------------------------------------+
|  CRAFT ERA (pre-1850)                             |
|  -- Individual craftsmen; no separation of        |
|     designer and maker                            |
|  -- Guild-based knowledge transmission           |
|  -- Machine production = debasement              |
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  ARTS AND CRAFTS MOVEMENT (1880-1920)            |
|  William Morris, John Ruskin (UK)                 |
|  -- Reaction against industrial mass production   |
|  -- Handcraft as moral/aesthetic ideal            |
|  -- Influenced: furniture, textiles, typography   |
|  -- Irony: expensive handcraft available only     |
|     to wealthy                                    |
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  BAUHAUS (1919-1933, Germany)                    |
|  Walter Gropius, Mies van der Rohe, Moholy-Nagy  |
|  -- Design FOR industrial production (not against)|
|  -- Unify fine art + craft + industrial technique |
|  -- Grid, geometry, function determines form      |
|  -- "Form follows function" radicalized           |
|  -- Dispersed 1933 (Nazi closure); spread globally|
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  STREAMLINING (1930s, USA)                       |
|  Raymond Loewy, Norman Bel Geddes                 |
|  -- Aerodynamic forms applied to all objects      |
|  -- (even refrigerators: no aerodynamic benefit)  |
|  -- Style as sales tool; first consumer design    |
|  -- Loewy: Lucky Strike package, Coke bottle,     |
|     Studebaker Avanti, Air Force One interior     |
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  FUNCTIONALIST CANON (1950s-1970s, Germany)      |
|  Braun, Dieter Rams, Ulm School of Design         |
|  -- Systematic reduction; "less but better"       |
|  -- Technology visible through form               |
|  -- Influenced: Apple product design              |
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  POSTMODERN (1970s-1990s)                        |
|  Memphis Group (Sottsass), Italian design         |
|  -- Rejected functionalism as authoritarian       |
|  -- Color, wit, decoration, contradiction         |
|  -- Bookcase shaped like skyscraper (Carlton)     |
+---------------------------------------------------+
             |
             v
+---------------------------------------------------+
|  DIGITAL + CONTEMPORARY (1990s-)                 |
|  Apple (Ive/Rams lineage), computational design   |
|  -- Software shapes physical form                 |
|  -- Platform products; ecosystem design           |
|  -- Sustainability imperative emerging            |
+---------------------------------------------------+
```

---

## Dieter Rams' 10 Principles: The Design Constitution

Rams' principles (formulated at Braun, 1970s-80s) remain the most influential explicit design philosophy:

```
RAMS' 10 PRINCIPLES OF GOOD DESIGN

1. Good design is innovative
   Not innovation for its own sake; innovation in service of function
   "It is only innovative if there is not a better solution"

2. Good design makes a product useful
   Function is primary; design serves use

3. Good design is aesthetic
   Good aesthetics improve well-being; ugliness is a failure

4. Good design makes a product understandable
   The product explains itself; no manual required

5. Good design is unobtrusive
   Products are tools, not art; neutral, restrained

6. Good design is honest
   Does not make a product look more powerful, innovative,
   or valuable than it actually is

7. Good design is long-lasting
   Avoids being fashionable; therefore never appears antique

8. Good design is thorough down to the last detail
   Nothing is arbitrary or left to chance

9. Good design is environmentally friendly
   Conserves resources; minimizes pollution

10. Good design is as little design as possible
    "weniger aber besser" -- less but better
    Back to purity; back to simplicity
```

The most quoted principle: #10 (less but better). The most violated: #6 (honesty -- marketing routinely violates it). The most relevant to software: #4 (makes product understandable), #8 (thorough to last detail), #10 (as little as possible).

---

## The Double Diamond: Design Process Model

The UK Design Council formalized the design process as a "double diamond":

```
DOUBLE DIAMOND MODEL

DISCOVER    DEFINE      DEVELOP      DELIVER
(diverge)   (converge)  (diverge)    (converge)
                |                        |
    *          *|*          *           *|*
   * *        * * *        * *         * * *
  *   *      *     *      *   *       *     *
   * *        * * *        * *         * * *
    *          *|*          *           *|*
               |                        |
        PROBLEM DEFINED         SOLUTION DELIVERED

DISCOVER: Open up -- research, observe, empathize
  -- What do people actually do? (not: what do they say they do)
  -- Ethnographic research; contextual inquiry
  -- "Go be a doctor for a week before designing medical equipment"

DEFINE: Narrow down -- what is the ACTUAL problem?
  -- The problem given is often not the real problem
  -- "Faster horse" problem: Ford's customers wanted speed, not horses
  -- Design brief: precise statement of problem + constraints

DEVELOP: Open up again -- generate solutions
  -- Ideation: quantity before quality
  -- Sketches, models, digital mockups
  -- Prototyping at increasing fidelity

DELIVER: Narrow down -- select, refine, test, iterate
  -- User testing
  -- Engineering validation
  -- Manufacturing preparation
  -- Final specification

BRIDGE: This is identical to Agile/Lean Product Discovery:
  Problem space exploration -> hypothesis definition ->
  solution prototyping -> validated delivery
```

---

## Decision Cheat Sheet

| You want to understand... | Go to |
|---------------------------|-------|
| How industrial design evolved historically | `01-HISTORY-MOVEMENTS.md` |
| Dieter Rams and the Bauhaus-to-Apple lineage | `02-BRAUN-RAMS.md` |
| The design process (double diamond etc.) | `03-DESIGN-PROCESS.md` |
| How materials and manufacturing shape design | `04-MATERIALS-MANUFACTURING.md` |
| Anthropometrics, reach envelopes, human factors | `05-ERGONOMICS.md` |
| Affordances, Norman doors, interaction design | `06-INTERACTION-DESIGN.md` |
| Planned obsolescence, circular economy, repair | `07-SUSTAINABILITY.md` |
| Parametric design, 3D printing, digital tools | `08-CONTEMPORARY-PRACTICE.md` |
| Semiotics, taste, design criticism | `09-DESIGN-CRITICISM.md` |

---

## Common Confusion Points

**Industrial design is not the same as engineering.**
Engineering optimizes function under constraints. Industrial design optimizes the human experience of function under constraints. Good industrial design requires engineering knowledge, but the goal includes aesthetics, cultural meaning, and user experience -- not just performance.

**"Form follows function" is descriptive, not prescriptive.**
Sullivan's aphorism (1896, architecture) describes how organic forms work, not a rule designers must follow. Functionalism as a rigid principle was challenged by postmodernism: sometimes form communicates identity, status, or joy in ways that exceed pure function.

**Good design is invisible when successful.**
The most successful designs disappear -- users don't think about them because they work so well. The scissors that fit the hand; the door handle that signals push vs pull without labels; the faucet that you operate correctly on first attempt. Invisibility is a design achievement, not a failure.

**User testing does not discover design solutions.**
User testing identifies problems with proposed solutions. It does not generate better solutions -- that requires designer judgment, expertise, and creative synthesis. The user can tell you the chair hurts their back; they cannot tell you how to redesign the lumbar support.
