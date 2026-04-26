# Product to Interaction Design

## The Big Picture

Interaction design (IxD) is the discipline of designing the behavior of products -- how they respond to user actions over time. It emerged from industrial design as products became software-mediated and needed explicit design of their temporal dimension (sequences, states, feedback). The concepts of affordances, feedback, mapping, and conceptual models originated in physical product design and were applied to digital interfaces.

```
+----------------------------------------------------------------------+
|           THE SPECTRUM FROM PRODUCT TO INTERACTION DESIGN            |
|                                                                      |
|  PHYSICAL PRODUCT         HYBRID PRODUCT         DIGITAL INTERFACE   |
|  (pure hardware)           (hardware + software)   (pure software)   |
|                                                                      |
|  Dial on radio             iPhone home screen      Web application   |
|  Ergonomics: primary       Both: co-equal          Cognitive: primary|
|  Materials: constrain      SW mediates HW          Pixels: constrain |
|  Manufacturing: limits     OS constrains both      Framework: limits |
|                                                                      |
|  Don Norman's work     <-- ORIGIN OF KEY CONCEPTS -->                |
|  "Design of Everyday       "The Design of               UX design    |
|  Things" (1988)            Everyday Things"             (1990s-)     |
|  applies to: doors,        first applied digital                     |
|  faucets, switches         HCI (Human-Computer Interaction)          |
+----------------------------------------------------------------------+

KEY CONTRIBUTORS:
  Don Norman:    "Design of Everyday Things" (1988, 2013 revised)
                 Affordances, feedback, mapping, constraints, conceptual model
  Bruce Tognazzini: "Tog on Interface" (Apple Human Interface guidelines author)
  Alan Cooper:   "The Inmates are Running the Asylum" (1999) -- Personas, Goal-Directed Design
  Bill Moggridge: coined "interaction design" (1984, IDEO co-founder)
  Jef Raskin:    Macintosh UI designer; "The Humane Interface" (2000)
```

---

## Norman's Framework: The Foundation

Don Norman's conceptual framework, introduced in "The Design of Everyday Things," is the vocabulary for all subsequent interaction design work.

### The Seven Stages of Action

```
NORMAN'S ACTION CYCLE

  +---> GOAL (what I want to achieve)
  |          |
  |          v
  |     PLAN (decide on action sequence)
  |          |
  |          v
  |     SPECIFY (sequence of actions to take)
  |          |
  |          v
  |     PERFORM (execute the actions)
  |          |
  |          v
  |     PERCEIVE (what happened to the world?)
  |          |
  |          v
  |     INTERPRET (what does the state mean?)
  |          |
  |          v
  +---- EVALUATE (did I achieve my goal?)

GULF OF EXECUTION: gap between goal and how to achieve it
  User doesn't know what actions are available or how to do them.
  Design solution: make actions visible and their effects predictable.

GULF OF EVALUATION: gap between system state and user understanding
  User can't tell if their action succeeded or what the current state is.
  Design solution: make system state visible and understandable.
```

### Affordances

```
AFFORDANCES (Gibson -> Norman)

ORIGINAL CONCEPT (James Gibson, ecological psychology):
  An affordance is a relationship between an object and an actor.
  A chair "affords" sitting for a human but not for an ant.
  Affordances are real (physical) properties.

NORMAN'S ADAPTATION:
  "Perceived affordances" are what matter for design.
  The user must perceive that an action is possible.
  A flat plate on a door affords pushing even if it could be pulled.

EXAMPLES:
  STRONG AFFORDANCE (physical):
    Button depresses when pressed: physically communicates "push here"
    Handle shape: hand naturally falls into the grip position
    Chair seat height: suggests sitting

  SIGNIFIERS (added signals):
    "Push" label on door: compensates for missing affordance in handle design
    Arrow on USB connector: signals orientation
    Dotted scroll indicator: shows scrollable content exists

  ANTI-AFFORDANCES:
    Smooth plate on door: signals "don't pull" (push only)
    Single round steering wheel: suggests rotation, not linear push

DIGITAL AFFORDANCES:
  Buttons that look raised/3D (skeuomorphic): afford pressing
  Underlined blue text: affords clicking (learned convention)
  Drag handle: ☰ icon affords drag (learned convention)
  The "flat design" problem: buttons that don't look like buttons
  are buttons that violate their affordance
```

### Feedback

```
FEEDBACK DESIGN

DEFINITION: Every action must produce a perceptible result
           that tells the user what happened.

FEEDBACK MODALITIES:
  Visual:    LED indicator, screen change, animation, color change
  Auditory:  Click sound, tone, voice response
  Tactile:   Button travel, vibration, resistance change
  Force:     Kickback, resistance, tension

TIMING:
  < 100ms:   Feels instantaneous; no feedback needed beyond action itself
  100ms-1s:  Should indicate that system is processing
  > 1s:      Progress indicator; estimated time
  > 10s:     Detailed progress; cancel option

POOR FEEDBACK EXAMPLES:
  Door with no click/resistance when fully closed:
    Did it latch? Must check manually.
  Button with no state change when pressed:
    Did I press it? Was it registered? Must press again?
  Form submit with no response:
    Did it submit? Network error? Loading?

GOOD FEEDBACK EXAMPLES:
  Physical button: travel + click (tactile + auditory)
  Car door: thump sound + latch feeling + door lamp off
  Save function: "Saved" text appears briefly, then fades
  Error: red border + icon + text explanation

FEEDBACK CONSTRAINTS:
  Too much feedback = noise
  Warning fatigue: if everything is a warning, nothing is
  Confirmation dialogs overused: users learn to dismiss without reading
```

### Mapping

```
MAPPING: RELATIONSHIP BETWEEN CONTROL AND EFFECT

NATURAL MAPPING: the spatial relationship between control and effect
                 matches the user's natural expectation.

GOOD MAPPING:
  Stovetop controls: control is directly below the burner it controls
    (common failure: controls in a row; burner in a square pattern)

  Car window controls: positioned to match window position in door
    (vs: all four windows controlled from single bank, no spatial logic)

  Aircraft throttle quadrant: levers in same L-R order as engines

  Screen scrollbar: at right edge, indicating position in long document

POOR MAPPING:
  Hotel shower: two knobs, no labels
    Which is hot? Which controls flow? No spatial logic.
    Solution: single control lever (temperature = rotation; flow = pull)

  Copy machine: complex button bank with no spatial relationship
    to the physical paper path
    Solution: diagram of machine on control panel; controls near their
    relevant physical components

DIGITAL MAPPING:
  Scroll bar position maps to document position
  Volume slider: left = quiet, right = loud (horizontal mapping)
  Geographic map pan: drag in direction of desired movement
  Color temperature slider: warm (orange) to cool (blue) visual mapping

BRIDGE: Direct Manipulation (Ben Shneiderman's principle)
  Objects should be manipulated directly (not through commands)
  File drag to trash can: direct manipulation of metaphorical object
  Zoom with pinch: direct scaling gesture
  This is natural mapping applied to gesture control
```

### Conceptual Model

```
CONCEPTUAL MODEL

The designer builds a design model.
The user builds a mental model from experience with the product.
The product reveals its system image through its design.

DESIGN MODEL <-- SYSTEM IMAGE --> MENTAL MODEL
(designer's intent)  (what the product shows)  (user's understanding)

GOOD DESIGN: all three are aligned.
BAD DESIGN: system image poorly communicates design model;
           user builds wrong mental model.

EXAMPLE (thermostat, again):
  Design model: thermostat sets target temperature;
               heater turns on until target reached.
  System image: single dial; temperature numbers
  User mental model (wrong): higher number = more heat = faster heating

  FIX: display current AND target temperature;
       show heating status indicator (on/off);
       this corrects the mental model mismatch.

CONCEPTUAL MODEL IN SOFTWARE:
  File system metaphor: files in folders in hierarchy
    -- Mental model: physical documents in physical folders
    -- Works until: files in multiple locations, search-based retrieval,
       cloud sync breaks the mental model
  iOS "back" gesture: slide from left edge to go back
    -- Works if: mental model is a stack of screens
    -- Fails: when there is no back screen; confusing navigation context
```

---

## Designing Interactions Over Time: States and Transitions

Physical products have state (on/off, volume level, mode). Interactive products have elaborate state machines.

```
PRODUCT STATE DESIGN

FINITE STATE MACHINE AS DESIGN TOOL:
  Every product at any moment is in exactly one STATE.
  TRANSITIONS between states are triggered by user actions or time.
  The design problem: how does the user know which state they're in?
                     how are transitions triggered?
                     are all transitions valid?

EXAMPLE: MICROWAVE OVEN STATE MACHINE

  [IDLE] --> (door open) --> [DOOR OPEN]
    |         <------------ (door close)
    |
    --> (time set) --> [TIME SET]
                          |
                          --> (start) --> [RUNNING]
                                             |
                                             --> (time elapses) --> [DONE]
                                             |
                                             --> (cancel) --> [IDLE]

FEEDBACK REQUIRED AT EACH STATE:
  IDLE: display "0:00"; light off
  DOOR OPEN: light on; display unchanged; start disabled
  TIME SET: display shows entered time; start enabled
  RUNNING: countdown visible; magnetron light; sound
  DONE: beep x3; display "END"; light off

DESIGN FAILURE: "BLINKING 12:00" PROBLEM
  Many microwaves in the 1980s-90s had blinking 12:00.
  This occurred because: power outage created ambiguous state
  State: "time has been set" vs "time has been erased" was not visible
  Design fix: dedicated "CLOCK" button; indicator light for clock set state

BRIDGE TO SOFTWARE: State machine design is literally finite state machine
design in software. Every button, form, modal, and page transition
is a state machine. Design the states before writing code.
```

---

## Interaction Design in Physical Controls

```
PHYSICAL CONTROL VOCABULARY

CONTROL TYPE        INFORMATION ENCODED      DESIGN CONSIDERATIONS
-------------------+------------------------+------------------------
PUSH BUTTON         Momentary ON/off         Tactile click; clear state
                    (returns to rest)        feedback; antiglare

TOGGLE SWITCH       Two stable states        Position indicates state;
                    (stays in position)      up/down meaning consistent

ROTARY KNOB         Continuous range         Detents signal positions;
                    (indefinite turns)       hard stops at limits

ROTARY DIAL         Discrete positions       Click for each position;
                    (limited travel)         labels at each stop

SLIDER              Linear range             Thumb position = current value;
                                             scale visible alongside

ROCKER SWITCH       Two states (rocking)     Labeled + / - or I / O;
                    (no center neutral)      tactile difference pressed/not

JOYSTICK            2D directional           Spring return to neutral typical;
                    (continuous or 8-way)    deflection = speed/direction

TOUCHPAD            2D absolute or relative  Lack of physical feedback
                    position                 = must compensate with audio/visual

TOUCHSCREEN         Direct manipulation      Minimum 44pt targets;
                    (2D position + gesture)  no hover state possible
```

---

## Norman Doors and Interaction Failures: A Pattern Library

```
COMMON INTERACTION DESIGN FAILURE PATTERNS

THE NORMAN DOOR:
  Pull handle on a push door.
  Cause: handle type (pull) contradicts operation (push)
  Fix: push plate (no grip; affords push only)

THE MYSTERY BURNER:
  Stovetop controls in a row; burners in a square.
  Cause: no spatial mapping between controls and burners
  Fix: controls directly below/beside their burner; spatial mapping

THE INVISIBLE BUTTON:
  Flat design button with no visual affordance.
  Cause: minimalist aesthetic removed affordance cue
  Fix: subtle drop shadow; background contrast; shape border

THE ERROR-ONLY FEEDBACK:
  Form gives feedback only on error, not on success.
  Cause: developer only implemented error handling
  User experience: must guess if submission succeeded
  Fix: explicit success state with visual and text confirmation

THE MODAL TRAP:
  Dialog appears; user dismisses without reading; unintended action.
  Cause: overuse of confirmation dialogs; warning fatigue
  Fix: make dangerous actions irreversible-looking; use undo vs confirm

THE UNLABELED ICON:
  Icon without text label; meaning ambiguous.
  Cause: aesthetic minimalism; assumed icon vocabulary
  Fix: label on hover/long-press; contextual label always visible

THE MYSTERY TIMEOUT:
  System times out; user loses work; no warning.
  Cause: backend session limit not communicated to UI
  Fix: countdown warning before timeout; auto-save

THE HIDDEN CANCEL:
  Destructive action with no undo or cancel.
  Cause: developer did not think about error recovery
  Fix: 5-second undo window (Gmail delete email model);
       confirmation for truly irreversible actions
```

---

## The Four Principles of Interaction Design (Cooper)

Alan Cooper's Goal-Directed Design added to Norman's framework:

```
COOPER'S INTERACTION DESIGN PRINCIPLES

1. REDUCE CONCEPTUAL COMPLEXITY:
   Minimize the number of things users must understand
   -- Fewer modes; fewer options; fewer categories to track
   -- Not: feature-complete; but: task-complete

2. EVERY DESIGN DECISION SERVES A GOAL:
   Users have goals (book a flight), not tasks (fill out form)
   Design to accomplish goals, not to expose system capability
   -- "Book a flight" is a goal
   -- "Fill in departure city, arrival city, date, passengers..."
      is what a badly designed system makes you do

3. ACCOMMODATE NOVICES AND EXPERTS SIMULTANEOUSLY:
   Novice path: guided, step-by-step, labeled
   Expert path: shortcuts, keyboard commands, power features
   Do not sacrifice expert efficiency for novice handholding;
   do not abandon novices for expert aesthetics

4. DESIGN FOR HUMAN BEHAVIOR, NOT HUMAN RATIONALITY:
   Users do not read instructions.
   Users do not explore systematically.
   Users do not follow intended flows.
   Design for what humans actually do, not what they should do.
```

---

## Decision Cheat Sheet

| Interaction design problem | Solution approach |
|---------------------------|------------------|
| User doesn't know what to do | Add affordances + signifiers |
| User can't tell what happened | Improve feedback (timing, modality) |
| User picks wrong control | Fix spatial mapping |
| User builds wrong mental model | Redesign system image to match design model |
| User makes irreversible errors | Error prevention + undo + confirmation |
| Expert users frustrated by novice pacing | Add expert shortcuts (power user path) |
| User loses state unexpectedly | Auto-save + session warning + undo history |
| Controls in unfamiliar pattern | Align with established conventions |

---

## Common Confusion Points

**Affordances and signifiers are different things.**
An affordance is a real property (the button physically moves when pressed). A signifier is a communication of what is possible (a label saying "press"). Modern design often confuses these: a flat button has no physical affordance but may have strong signifiers. Norman's revised edition (2013) separates these concepts.

**Interaction design is not the same as UX design.**
Interaction design focuses on the behavior of the system -- states, transitions, feedback, mapping. UX design includes research, information architecture, visual design, and strategy in addition. IxD is a component of UX; UX is not a subset of IxD.

**Good interaction design is invisible.**
When users achieve their goals without noticing the design, the interaction design is successful. Interaction design that draws attention to itself is decoration, not design. The test is not "does it look designed?" but "did the user accomplish their goal?"

**Direct manipulation is not always best.**
Direct manipulation (drag, pinch, rotate) is intuitive for spatial tasks. For sequential processing (data entry, programming, command-line work) direct manipulation is actually slower and more error-prone than keyboard commands. The right interface paradigm depends on the task.
