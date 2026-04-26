# Ergonomics and Human Factors

## The Big Picture

Ergonomics (human factors engineering) is the scientific discipline of designing for human use -- matching the physical and cognitive characteristics of the human body to the demands of products, tools, and environments. The principle is straightforward: if the human must adapt to the tool, the tool is badly designed; the tool must adapt to the human.

```
+----------------------------------------------------------------------+
|           ERGONOMICS: THREE DOMAINS                                  |
|                                                                      |
|  PHYSICAL ERGONOMICS    COGNITIVE ERGONOMICS    ORGANIZATIONAL       |
|  (body-product fit)     (mind-product fit)      ERGONOMICS           |
|                                                                      |
|  Anthropometrics        Information display     Work flow design     |
|  Biomechanics           Decision support        System design        |
|  Reach envelopes        Cognitive load          Team interaction     |
|  Force requirements     Mental models           Shift work design    |
|  Posture analysis       Error prevention        Environment design   |
|  Vibration/noise        Feedback design                              |
|                                                                      |
|  TOOLS: CAESAR data,    TOOLS: ISO standards,   TOOLS: Simulation,   |
|  manikins, motion       usability testing,      task analysis        |
|  analysis, force        eye tracking                                 |
|  measurement                                                         |
+----------------------------------------------------------------------+
```

---

## Anthropometrics: The Body's Dimensions

Anthropometrics is the systematic measurement of the human body for design purposes. The fundamental challenge: humans vary enormously, but designed objects must work for a range of users.

### The 5th-50th-95th Percentile Framework

```
PERCENTILE DESIGN STRATEGY

  5th percentile: only 5% of the population is SMALLER
  50th percentile: the average (rarely the right target)
  95th percentile: only 5% of the population is LARGER

WHAT YOU DESIGN FOR:
  CLEARANCE dimensions (how large must an opening be?):
    Design for 95th percentile (or larger)
    -- Door width: must fit the largest expected user
    -- Legroom: must accommodate the tallest user's legs
    -- Hatches, access panels: must accommodate largest users

  REACH dimensions (how far does a control need to be?):
    Design for 5th percentile (or smaller)
    -- A control that the smallest user can reach is reachable by all
    -- Shelf height: bottom shelf for shortest user; top for everyone
    -- Steering wheel: must be reachable by shortest driver

  FORCE dimensions (how much force should an actuator require?):
    Design for 5th percentile (weakest user can operate)
    -- Jar lid: the weakest user's grip strength sets the limit
    -- Emergency stop button: must be operable by injured, fatigued operator

ANTHROPOMETRIC DATA SOURCES:
  CAESAR (Civilian American and European Surface Anthropometry Resource):
    3D scans of 4,400 adults in US + Europe
    99+ body measurements; 3D body shapes
    Reference standard for US product design

  ANSUR II (US Army):
    6,000 US Army soldiers measured; 93 measurements
    Useful for equipment design; more restricted demographic

  WHY SINGLE-COUNTRY DATA IS INSUFFICIENT:
    US 50th percentile male stature: 175.6 cm
    Japanese 50th percentile male stature: 171.0 cm
    Dutch 50th percentile male stature: 182.9 cm
    A seat designed for US 50th has wrong cushion depth for Japan and Netherlands.
    Global products need global anthropometric data.
```

### Key Measurements for Product Design

```
CRITICAL ANTHROPOMETRIC MEASUREMENTS (adult US males, 5th/50th/95th %ile)

STATURE (standing height):    163.0 / 175.6 / 188.2 cm
SITTING HEIGHT:               80.6 / 88.0 / 95.0 cm
SHOULDER HEIGHT (seated):     55.6 / 61.9 / 68.2 cm
EYE HEIGHT (seated):          69.1 / 76.2 / 83.4 cm
SHOULDER WIDTH:               40.0 / 45.2 / 50.6 cm
ELBOW-TO-WRIST LENGTH:        24.7 / 27.3 / 30.0 cm
HAND LENGTH:                  17.5 / 19.1 / 20.8 cm
HAND BREADTH:                 8.0 / 8.8 / 9.7 cm
THUMB TIP DIAMETER:           1.5 / 1.8 / 2.1 cm (touch target minimum)
GRIP DIAMETER:                28 / 34 / 40 mm (tool handle target)

NOTE: Female data differs significantly:
  Female grip strength: ~40% less than male (important for force-critical design)
  Female hand length: ~10% smaller
  Female hip breadth: larger relative to stature
```

### Reach Envelopes

```
REACH ENVELOPE ANALYSIS

NORMAL REACH ZONE (comfortable seated operation):
  Without moving torso: 35-45 cm from body centerline
  Forearm-only reach: arc defined by elbow pivot

MAXIMUM REACH ZONE:
  Full arm extension: 60-70 cm from shoulder
  Requires torso rotation

OVERHEAD REACH (standing):
  Normal (arm extended): 185-200 cm above floor (varies by stature)
  With load: reduce by 15-20 cm (shoulder fatigues faster)

FORWARD REACH IN SEATED POSITION (cockpit / control panel):
  5th percentile female (limiting case):
    Normal work: to 36 cm forward of shoulder
    Maximum: to 60 cm forward (requires leaning)
  This determines cockpit instrument panel layout in aircraft
  ALL instruments that must be operated must be within 5th %ile reach

GRAB BARS (accessibility):
  Toilet grab bar height: 33-36 inches above floor (ADA)
  -- Designed for 5th %ile (needs support while seated/rising)
  -- Also tested: strength under 250 lb lateral load
  -- Design for both the weakest and the heaviest user
```

---

## Biomechanics: Force, Posture, and Injury Prevention

### Grip Analysis

```
GRIP TYPES AND OPTIMAL HANDLE DESIGN

POWER GRIP (whole hand wraps handle):
  -- Used for: hammers, power tools, luggage handles
  -- Optimal handle diameter: 30-40 mm (for 5th %ile male)
  -- At extremes (too thin or too thick): strength drops by 40-50%
  -- Surface texture: adds grip by ~30% vs smooth surface
  -- Oval cross-section better than circular: prevents rotation

PRECISION GRIP (fingertips only; thumb opposition):
  -- Used for: pens, tweezers, knobs, small switches
  -- Optimal diameter: 8-12 mm
  -- Surface features: knurling, ribs increase control

PINCH GRIP (thumb + 1-2 fingers):
  -- Used for: tags, coins, flat objects
  -- Minimum thickness for pickup: 2-4 mm
  -- Difficult for gloved hands: increase to 6-8 mm

KEY MEASURE: Grip strength varies dramatically:
  5th %ile female grip: 19-24 kg force
  95th %ile male grip: 58-68 kg force
  Range: 3:1 ratio between weakest and strongest
  Consumer product force requirements: design for <10 kg (accessible to all)
```

### Posture and Musculoskeletal Risk

```
POSTURAL ANALYSIS FOR PRODUCT DESIGN

NEUTRAL POSTURE PRINCIPLES:
  Wrist: slight extension (0-15 degrees), minimal ulnar deviation
  Elbow: 90-110 degrees flexion during work
  Shoulder: arm below shoulder height, <15-20 degree abduction
  Neck: 0-15 degree forward flexion
  Back: lumbar support maintained; slight lordosis

DEVIATIONS AND RISK:
  Ulnar wrist deviation: risk after 15 degrees, high risk after 25
  Shoulder elevation: 30+ minutes at shoulder height = cumulative risk
  Neck flexion: >30 degrees = high risk; smartphone use posture

RULA (Rapid Upper Limb Assessment):
  Scoring system: 1-7 score based on posture + force + duration
  Score 1-2: acceptable
  Score 3-4: investigate further; change soon
  Score 5-6: investigate and change now
  Score 7: investigate and change immediately

PRODUCT DESIGN IMPLICATIONS:
  Knife handle angle: tilted 15 degrees reduces wrist deviation vs straight
  Power tool grip: pistol grip vs inline; context-dependent
  Laptop screen height: users tilt neck forward excessively (see "text neck")
  Mouse design: vertical mouse eliminates forearm pronation
```

---

## Cognitive Ergonomics: The Mental Interface

### Mental Models and Product Design

```
MENTAL MODELS IN PRODUCT DESIGN

A MENTAL MODEL is the user's internal representation of how a system works.
Good design: product's behavior matches user's mental model.
Bad design: gap between model and reality.

EXAMPLE: Thermostat mental model problem
  USER MENTAL MODEL: "Turn the thermostat up more to heat room faster"
  REALITY: The thermostat is a binary on/off switch; the number
           sets the target temperature, not the heating rate.
  RESULT: Users set thermostat to 90 to "heat faster";
          room reaches 90°F; energy wasted.
  DESIGN SOLUTION: Display actual room temperature AND target;
                   show that heating rate is constant.

PHYSICAL AFFORDANCES (Norman's model):
  An affordance is a design feature that signals correct operation.
  -- Round doorknob: affords grasping and turning
  -- Push plate: affords pushing
  -- Pull handle: affords pulling
  -- Flat surface: affords pushing
  -- Slotted screw head: affords torque (with the right tool)

  ANTI-AFFORDANCES: design features that prevent incorrect operation
  -- Knives with guard: prevents fingers sliding to blade
  -- Asymmetric connectors: USB-C vs USB-A

THE DOOR HANDLE PROBLEM (Norman):
  "The most important thing about design is not the door handle.
  It's that you should know which way to push or pull a door
  without thinking about it."

  Norman Doors: doors where the handle is on the wrong side,
  or the handle type (push vs pull) conflicts with the required operation.
  -- Pull handle + push door = Norman door (failure)
  -- The handle communicates the wrong affordance
  This single example captures the core of interaction design.
```

### Cognitive Load

```
COGNITIVE LOAD AND DESIGN

COGNITIVE LOAD: the total amount of mental effort required
to understand and operate a product.

TYPES OF COGNITIVE LOAD (after Sweller):
  Intrinsic load: complexity inherent in the task (cannot reduce)
  Extraneous load: complexity from poor design (MUST reduce)
  Germane load: effort invested in learning and schema-building (good)

DESIGN PRINCIPLES TO REDUCE EXTRANEOUS LOAD:

1. MATCH TO EXISTING MENTAL MODEL:
   Use conventions users already know
   -- Power button symbol: IEC 60417-5009; universally recognized
   -- Color code: red = stop/danger; green = go/safe
   Don't reinvent symbols; leverage learned conventions

2. REDUCE NUMBER OF MODES:
   Each "mode" a product can be in requires the user to track state
   -- Phone: silent mode, vibrate mode, ring mode = 3 modes to manage
   -- Camera: aperture priority, shutter priority, manual, auto = cognitive load
   -- Principle: minimize modes; make current mode immediately obvious

3. PROVIDE FEEDBACK IMMEDIATELY:
   Action without feedback creates uncertainty
   -- Button click: physical travel + audio/tactile feedback
   -- Loading indicator: confirms system received action
   -- Error message: what happened + what user should do
   Every action must produce visible result within 100ms

4. PRINCIPLE OF LEAST SURPRISE:
   Product behaves as users expect
   Violations of expectation = extraneous cognitive load
   "The principle of least astonishment"
   (Same principle as in API design: behavior should match caller's expectation)

5. CHUNK INFORMATION:
   Miller's law: working memory holds 7±2 items
   Group controls into semantic clusters
   Labels: short; no abbreviations unless widely known
   Don't make user remember across sections of an interface
```

---

## Accessibility: Designing for the Full Range

```
ACCESSIBILITY AS ERGONOMICS

POPULATIONS REQUIRING SPECIFIC ACCOMMODATION:

MOBILITY IMPAIRMENTS:
  Reduced grip strength: -> lower force requirements; lever-style handles
  Limited reach: -> lower shelf heights; pull-out mechanisms
  Wheelchair users: -> ADA clear floor space (30"x48"), turning radius
  Tremor (Parkinson's): -> larger targets; anti-tremor grip design

VISUAL IMPAIRMENTS:
  Low vision: -> high contrast; large text; good lighting
  Color blindness: -> never use color alone to convey meaning
    (8% of males; 0.5% of females have some form of color blindness)
    Red-green blindness most common
    Design rule: use color + shape/pattern/position together
  Blind users: -> tactile indicators; Braille; audio feedback
    Tactile ground surface indicators: raised dots/lines for navigation

HEARING IMPAIRMENTS:
  Deaf users: -> visual alerts alongside audio (light flash)
  Hard of hearing: -> volume controls; loop induction for hearing aids
  In noisy environments: -> all important information must be non-auditory

COGNITIVE VARIATIONS:
  Dyslexia: -> sans-serif fonts; generous line spacing; short paragraphs
  ADHD: -> reduce distractions; clear visual hierarchy; progressive disclosure
  Alzheimer's: -> highly consistent interaction; clear labels; error prevention

TEMPORARY IMPAIRMENTS:
  Gloves: -> larger targets; different grip requirements
  Bright sunlight: -> screen visibility; physical controls vs touch
  Cold (reduced dexterity): -> larger controls; reduced force needed
  Injury (arm in cast): -> can user operate with non-dominant hand?
```

### Universal Design Principles

```
7 PRINCIPLES OF UNIVERSAL DESIGN (Ron Mace, 1997)

1. EQUITABLE USE:
   Useful to people with diverse abilities; no stigmatizing features
   Example: automatic doors useful for wheelchair users, parents with strollers,
   people carrying packages -- without marking any group as "special"

2. FLEXIBILITY IN USE:
   Accommodates wide range of preferences and abilities
   Example: Scissors with multiple grip options; right/left hand compatible

3. SIMPLE AND INTUITIVE USE:
   Easy to understand, regardless of experience, language, literacy
   Example: IKEA pictographic assembly instructions (no text)

4. PERCEPTIBLE INFORMATION:
   Communicates information effectively; sensory redundancy
   Example: Traffic light = color + position (red is always top)
   Works for color-blind users because position = redundant code

5. TOLERANCE FOR ERROR:
   Minimizes hazards from accidental action
   Example: Undo function; confirmation dialogs for destructive actions
   Disposable camera: you cannot accidentally expose the film before developing

6. LOW PHYSICAL EFFORT:
   Efficient and comfortable with minimum fatigue
   Example: Lever faucet vs twist knob (1/6 the force; wrist-neutral)

7. SIZE AND SPACE FOR APPROACH AND USE:
   Appropriate regardless of user's size, posture, or mobility
   Example: ATM accessible from standing and wheelchair height;
   front-loading washer vs top-loading (wheelchair access)
```

---

## Anthropometric Design Process

```
STEP-BY-STEP ANTHROPOMETRIC DESIGN PROCESS

STEP 1: IDENTIFY CRITICAL DIMENSIONS
  Which body dimensions will constrain the design?
  Seat: hip breadth (accommodation), back length (support), popliteal height (seat height)
  Handle: hand breadth, grip diameter, grip strength
  Screen: eye height, reading distance, neck angle

STEP 2: CHOOSE DESIGN APPROACH
  For each critical dimension, choose:
  a) FIXED: single size (choose percentile to accommodate)
  b) ADJUSTABLE: user-adjustable (define range + adjustment mechanism)
  c) UNIVERSAL: works for all without adjustment (rare; simplest)

STEP 3: SELECT PERCENTILE
  What percentage of the target population must be accommodated?
  General consumer: 5th-95th %ile (90% coverage)
  Safety-critical (vehicle, medical): often 1st-99th %ile (98% coverage)
  Military specification: sometimes 5th-95th of the specific population

STEP 4: APPLY DATA
  Look up actual measurements from appropriate database (CAESAR, local)
  Apply to design geometry
  Build in adjustment margin for clothing, footwear, posture variation

STEP 5: VALIDATE WITH PHYSICAL SIMULATION
  Digital human model software:
    RAMSIS, JACK, DELMIA (automotive industry standard)
    Position virtual manikins at 5th and 95th percentiles
    Check reach, clearance, posture quality

STEP 6: USER TESTING WITH REPRESENTATIVE POPULATION
  Test with real users (not design team members)
  Include the extremes (not just average users)
  Specific tasks; specific metrics
```

---

## Decision Cheat Sheet

| Design situation | Ergonomic consideration |
|-----------------|------------------------|
| Designing controls for diverse users | Use 5th %ile reach for all controls |
| Designing clearance (doorway, hatch) | Use 95th %ile body breadth/height |
| Designing handle/grip | 30-40mm diameter power grip; surface texture |
| Force-operated mechanism | Maximum 10-15N for consumer products |
| Screen readability | Minimum 4:1 contrast; 16px minimum text |
| Touch target | Minimum 44x44px (Apple HIG); prefer 48x48 |
| Color coding | Never color alone; add shape/position |
| Preventing errors | Mistake-proofing + confirmation for destructive actions |
| Workplace seat height | Adjustable 38-50cm; lumbar support adjustable |

---

## Common Confusion Points

**Designing for the "average user" designs for almost nobody.**
The mythical average person (50th percentile on all dimensions simultaneously) does not exist. Someone who is 50th percentile in height is almost certainly not 50th percentile in arm length, grip strength, and hip breadth simultaneously. Design for the 5th-95th range of each critical dimension independently.

**Ergonomics is not about comfort -- it is about function and safety.**
Comfort is a result of good ergonomics, not the goal. The goal is: users can perform their tasks accurately, without injury, and without excessive fatigue. Comfortable products that lead to repetitive strain injury are ergonomically failed.

**Cognitive ergonomics is not about making things simpler -- it is about matching complexity to user capability.**
A surgeon's workstation is cognitively complex by necessity. Good cognitive design does not eliminate complexity; it structures complexity to match the user's mental model and expertise level.

**Anthropometric data from one population does not transfer.**
Data collected from US Army soldiers does not represent elderly Japanese users. Data from 1970 does not represent current populations (secular trends in height, weight). Always check: whose data, collected when, from whom, in what posture.

**Universal Design does not mean identical design.**
Universal Design produces products that work for the widest range of users. Sometimes this means adjustable solutions (seat height adjustment); sometimes it means a single design that accommodates all (lever door handle vs knob). The goal is no excluded users -- not sameness.
