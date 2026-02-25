# Design Process: Brief to Prototype

## The Big Picture

The design process converts a problem (imprecisely stated, poorly understood) into a solution (manufacturable, usable, appropriate). The process is not linear -- it is iterative, with multiple cycles of divergence (generating options) and convergence (selecting and refining). This maps directly to Agile/Lean product development, which borrowed its vocabulary from design.

```
+----------------------------------------------------------------------+
|           THE DESIGN PROCESS: DOUBLE DIAMOND                         |
|                                                                      |
|  DISCOVER        DEFINE        DEVELOP        DELIVER                |
|  (research)      (framing)     (ideation)     (refinement)           |
|                                                                      |
|  "What is        "What is      "What could    "What will             |
|  happening?"     the real      the solution   work?"                 |
|                  problem?"     be?"                                  |
|                                                                      |
|  DIVERGENT       CONVERGENT    DIVERGENT      CONVERGENT             |
|  (expand)        (focus)       (expand)       (focus)                |
|                                                                      |
|  Methods:        Methods:      Methods:       Methods:               |
|  Ethnography     Brief         Sketching      User testing           |
|  Interviews      POV statement Ideation       A/B testing            |
|  Observation     HMW questions Concept models Iteration              |
|  Empathy maps    Design reqs   CAD / mockup   Refinement             |
|  Journey mapping JTBD          Prototyping    Spec + tooling         |
+----------------------------------------------------------------------+

BRIDGE TO AGILE:
  Double Diamond = Discovery Sprint + Delivery Sprint
  "Define" = Product Backlog with proper problem framing
  "Develop" = Feature prototyping / spike
  "Deliver" = Sprint delivery + retrospective
  The vocabulary is identical; the artifact (physical vs digital) differs.
```

---

## Phase 1: Discover -- Understand Before Solving

### The Fundamental Rule

The design process begins with the explicit assumption that you do not know what the problem is. The brief you receive is a hypothesis, not a specification.

```
THE PROBLEM WITH THE GIVEN PROBLEM

Henry Ford (apocryphal): "If I had asked people what they wanted,
they would have said faster horses."
-- People describe problems in terms of solutions they already know
-- "I need a faster horse" = "I need faster personal transportation"
-- The real need: speed and autonomy in travel
-- The solution: automobile (not horse breeding)

IDEO'S CLASSIC EXAMPLE: Hospital gurney redesign
  Brief: "Improve the hospital gurney for patient comfort"
  Research: Observed patients' experience of being wheeled to surgery
  Discovery: Patients experienced enormous anxiety because they spent
             the journey staring at ceiling fluorescent lights and
             strangers' faces looking down at them
  REAL PROBLEM: Visual isolation and disorientation during transit
  ACTUAL SOLUTION: Ceiling decorations + design of the overhead visual
                   experience, not the gurney's cushioning
```

### Research Methods

```
RESEARCH METHODS IN DESIGN DISCOVERY

ETHNOGRAPHIC OBSERVATION:
  Watch people doing the thing, in context, without intervention
  -- Do NOT ask what they would want
  -- OBSERVE what they actually do and struggle with
  -- Workarounds are gold: if users have invented a workaround,
     the product has a problem at that point

  BRIDGE: This is observability and telemetry. In software, you instrument
  to see what users actually do, not what they report. Same epistemology.

CONTEXTUAL INQUIRY:
  Observe + interview simultaneously, in the user's environment
  -- "Walk me through what you just did"
  -- "Why did you do that?"
  -- Not: "What would you want the product to do?"

INTERVIEWS (properly conducted):
  Open-ended; past behavior not hypothetical future
  -- "Tell me about the last time you..." (not "Would you...")
  -- "What happened when..." (not "What would you do if...")
  Hypothetical responses are unreliable; past behavior is evidence

USER JOURNEY MAPPING:
  Map all touchpoints in a user's experience with a problem
  -- Before / during / after using the product
  -- Emotional state at each point
  -- Pain points, moments of joy
  -- The journey includes: awareness, purchase, unboxing, first use,
     learning, mastery, repair, end of life
  -- Most briefs address only one stage; journey map reveals all

EMPATHY MAPPING:
  For a specific user persona:
    THINKS: What is in their head?
    FEELS: Emotional state?
    SAYS: What do they tell others?
    DOES: Actual behavior?
  The gaps between SAYS and DOES are the interesting data.

COMPETITIVE ANALYSIS:
  How is the problem currently solved?
  By products: direct competitors
  By behaviors: people who don't buy any product (latent demand)
  By analogies: how is a similar problem solved in a different domain?
```

---

## Phase 2: Define -- Frame the Problem Precisely

### The Design Brief

The design brief is the convergent output of the Discover phase -- a precise, agreed statement of the problem to be solved.

```
DESIGN BRIEF STRUCTURE

1. CONTEXT:
   Who is the user? (specific, not demographic abstraction)
   What situation are they in? (context matters enormously)
   What are they trying to achieve? (the job to be done)

2. PROBLEM STATEMENT:
   "We have observed that [user] struggles to [do X] when [context]
   because [root cause]. How might we [reframed solution space]?"

   EXAMPLE:
   "We have observed that hospital nurses struggle to accurately
   dose medications during shift transitions because they lack
   a clear record of what was administered. How might we make
   medication history instantly visible at the patient bedside?"

3. CONSTRAINTS:
   Hard constraints: regulatory requirements, manufacturing limits,
                    cost ceiling, weight/size limits
   Soft constraints: brand language, material preferences, timeline

4. SUCCESS CRITERIA:
   How will we know the design works?
   Quantitative: if measurable (task completion time, error rate)
   Qualitative: user experience targets

5. WHAT IS OUT OF SCOPE:
   Explicitly list what is not being solved.
   Scope creep in design = as much problem as in software.
```

### Jobs To Be Done (JTBD) Framework

```
JTBD FRAMEWORK (Clayton Christensen)

"People don't buy products; they hire them to do a job."

EXAMPLES:
  "Milkshake study" (Christensen, 1990s):
    Fast food chain wanted to increase milkshake sales.
    Asked customers: how can we improve the milkshake?
    Got: "make it thicker, more flavors, etc."

    Christensen observed: most milkshakes sold in morning.
    Asked: what job is the morning customer hiring the milkshake for?
    Discovery: commuters buying milkshakes for the 45-minute commute
    -- Something to do during boring drive
    -- Thick enough to last the commute
    -- Hand-holdable, doesn't require attention
    -- More filling than a banana (the alternative)

    JOB: "Keep me occupied and somewhat full during my morning commute"
    This is different from: "satisfy my milkshake craving"

JTBD STRUCTURE:
  "When [situation], I want to [motivation], so I can [outcome]."
  "When I'm stuck in traffic commuting, I want something to keep
   me occupied and slightly full, so I can arrive at work not hungry
   and having done something with the dead time."

DESIGN IMPLICATION:
  The milkshake competing with: banana, bagel, audio content
  (not: other milkshakes, ice cream)
  Knowing the actual competition changes the design response.
```

---

## Phase 3: Develop -- Generate Solutions

### Ideation Techniques

```
IDEATION PRINCIPLES

RULE 1: Quantity before quality
  -- First 20 ideas are usually conventional
  -- Ideas 21-50 are where interesting territory begins
  -- The brain's first responses are the most obvious ones
  -- You must exhaust the obvious before reaching the interesting

RULE 2: No evaluation during generation
  -- "Yes, and..." not "Yes, but..."
  -- Judgment kills generation
  -- Separate the generating session from the evaluating session
  -- BRIDGE: in code review, you separate "does this work?" from
    "could we approach this differently?" -- same principle

RULE 3: Build on others' ideas
  -- Ideas are inputs, not property, during ideation
  -- "What if we combined X and Y?"
  -- Combinatorial creativity: most innovation is synthesis

SPECIFIC TECHNIQUES:
  BRAINWRITING: Each person writes 3 ideas; passes paper; adds 3 more
    (Avoids HiPPO effect: Highest Paid Person's Opinion dominates)

  RANDOM STIMULUS: Take random object; force connection to problem
    "A mirror + hospital chair = ?"
    Forces non-obvious combinations

  WORST POSSIBLE IDEA: Design the absolute worst solution
    Then invert: the bad idea's opposite is often a good idea
    "The worst hospital bed: hard, cold, tilted, bright lights,
     no privacy, visible from hallway"
    -> Invert: soft, warm, flat, dimmable, private, screened

  ANALOGIES: "How does nature solve this?"
    Biomimicry as ideation technique
    Velcro: burr stuck to dog fur
    Sharkskin: drag-reducing swimsuit surfaces
```

### Sketching as Thinking

```
SKETCHING IN DESIGN PROCESS

Sketching is thinking, not recording.
The hand and the eye develop ideas that the mind alone cannot.

SKETCH TYPES BY PURPOSE:
  Thumbnail sketches (20-40 per page):
    -- Tiny, fast, no detail
    -- Pure form exploration: overall shape only
    -- Generate 50 before selecting any

  Concept sketches (1/4 page):
    -- Enough detail to evaluate form
    -- Annotated: what is this solving?
    -- 3-5 per concept direction

  Communication sketches:
    -- Drawn for others to understand
    -- Perspective; shading; labels; callouts
    -- Context (show scale: hand holding the object)

  Exploded views:
    -- Show how parts relate
    -- Manufacturing and assembly logic visible
    -- Design and engineering language combined

DIGITAL vs PHYSICAL SKETCHING:
  Physical (pencil/marker): fastest; most fluid; most ideation-oriented
  Tablet (iPad Pro): combination; can iterate digitally; slightly slower
  CAD: for evaluation, not ideation (too slow for exploration phase)

BRIDGE TO SOFTWARE:
  Wireframing in UX is identical to concept sketching in product design.
  The purpose is the same: externalize thinking quickly without committing.
  Whiteboard architecture diagrams: same function.
```

### Prototyping

```
PROTOTYPING FIDELITY SPECTRUM

LOW FIDELITY                                         HIGH FIDELITY
(fast, cheap, answerable questions: does the         (slow, expensive, answerable
concept make sense?)                                  questions: does this work?)

Paper       Foam   3D      CAD     FDM(PLA)  SLA(resin)  CNC    Production
mockup      model  print   model   print     print       part   tooling

PURPOSE:
  Low fidelity: concept validation; user testing of the idea
  Mid fidelity: ergonomics testing; form evaluation
  High fidelity: engineering validation; pre-production approval

THE GOLDEN RULE: Use the lowest fidelity that answers the question.
Making a high-fidelity prototype to test whether users understand
the concept is wasteful. Making a paper mockup to test structural integrity
is useless.

SPECIFIC PROTOTYPE TYPES:
  APPEARANCE MODEL:
    Looks exactly like the final product; doesn't work
    Tests: visual design, size/scale, material language
    Materials: stereolithography (SLA), CNC aluminum

  WORKS-LIKE MODEL:
    Functions correctly; doesn't look like final product
    Tests: electronics, mechanisms, ergonomics
    Materials: 3D printed shell + development electronics

  LOOKS-LIKE + WORKS-LIKE ("feels like"):
    Both; pre-production equivalent
    Tests: everything together; used for user testing
    Made from production-equivalent processes
    Cost: high; required for final validation

PROTOTYPING TIMELINE (typical consumer electronics):
  Months 1-3:  Low-fi form models (foam, paper)
  Months 3-6:  3D printed appearance + works-like models
  Months 6-9:  Engineering validation prototypes
  Months 9-12: Pre-production pilot builds
  Month 12+:   Mass production tooling and ramp
```

---

## Phase 4: Deliver -- Refine to Production

### User Testing

```
USER TESTING PRINCIPLES

WHAT TESTING CAN TELL YOU:
  -- Users struggle at [specific point]
  -- Users expect [behavior that product doesn't have]
  -- Users don't notice [feature you thought was obvious]
  -- Users use [feature] in a way you didn't intend

WHAT TESTING CANNOT TELL YOU:
  -- The right solution (users describe problems, not solutions)
  -- Whether something will sell (test ≠ purchase behavior)
  -- Whether the concept is right (only whether execution works)

PROTOCOLS:
  THINK-ALOUD PROTOCOL:
    User narrates internal experience while doing tasks
    "I'm looking for the power button... hmm, not obvious..."
    Rich qualitative data; low sample size needed (n=5-8 for patterns)

  TASK-BASED TESTING:
    Define tasks; observe completion rate, time, errors
    "Please turn on the device and connect to wifi"
    Quantitative; usability metrics
    Larger sample (n=10-20 for statistical power)

  REMOTE UNMODERATED:
    Users test at home with recording software
    Larger scale; less rich qualitative data
    Useful for secondary validation after lab testing

SAMPLE SIZE:
  Jakob Nielsen's finding: 5 users discover 85% of usability problems
  The first user finds something new 33% of the time
  The 5th user finds something new <10% of the time
  After ~8 users, diminishing returns for qualitative usability testing
```

### Design Refinement and Iteration

```
REFINEMENT CYCLE

  USER TESTING identifies problem
       |
       v
  DESIGN TEAM analyzes root cause
  (not: fix the symptom; find the underlying issue)
       |
       v
  GENERATE alternatives to address root cause
  (not one fix; 3-5 variations)
       |
       v
  PROTOTYPE change at minimum viable fidelity
       |
       v
  TEST again (targeted; same task; same user type)
       |
       v
  EVALUATE: did the change help? Did it create new problems?
       |
       v
  REPEAT until quality threshold met

BRIDGE TO AGILE:
  This cycle is identical to: sprint -> retro -> backlog refinement
  -> sprint plan -> sprint
  The "prototype" is the sprint increment.
  User testing = user acceptance testing + analytics review.
  Design critique = code review.
```

### Specification and Engineering Handoff

```
DESIGN SPECIFICATION DOCUMENT STRUCTURE

1. DESIGN INTENT:
   Philosophy and principles; what are we trying to achieve
   Not: pixel-level specifications; this communicates WHY

2. FORM AND GEOMETRY:
   CAD files (neutral format: STEP, IGES, or native)
   Dimensional drawings (GD&T: geometric dimensioning and tolerancing)
   Surface files (NURBS surfaces or polyhedral mesh)

3. MATERIALS AND FINISHES:
   Material specifications (grade, alloy, standard)
   Surface finish specifications (Ra values; visual standards)
   Color specifications (Pantone, RAL, or manufacturer codes)

4. TOLERANCES:
   Critical dimensions: ±0.1mm
   Non-critical: ±0.5mm
   Assembly fits: clearance/interference specifications

5. INTERACTION DETAILS:
   Force required to actuate controls (in Newtons)
   Tactile feedback specifications
   Sound characteristics (click, thud, silence)
   Display brightness/contrast minimums

6. BRANDING ELEMENTS:
   Logo placement and size
   Typography specifications
   Color application rules

BRIDGE: This is exactly a technical specification document.
Same structure: what we're building, precise requirements,
testable criteria, interface contracts. The artifact is
a physical product; the document is a spec.
```

---

## Decision Cheat Sheet

| Design phase | Goal | Risk if skipped |
|-------------|------|----------------|
| Discover (research) | Understand actual user behavior | Solving the wrong problem elegantly |
| Define (brief) | Frame problem precisely | Scope creep; moving goalposts; misaligned team |
| Develop (ideation) | Generate range of options | First solution = only solution (rarely optimal) |
| Prototype (low-fi) | Validate concept cheaply | Investing in the wrong direction |
| User test | Find problems users encounter | Shipping known problems |
| Refine + iterate | Fix root causes | Shipping fixed version with new problems |
| Specify | Communicate intent to engineering | Lost in translation; compromised final product |

---

## Common Confusion Points

**The brief is not the problem.**
The design brief is the client's initial framing of the problem. It is a starting hypothesis, not a specification. The most important design skill is problem reframing: discovering that the stated problem is not the real problem.

**More research is not always better.**
Research serves decision-making. Once you have enough information to make a good decision about the next design step, more research is delay. The question is not "what is the best research method?" but "what decision am I trying to make, and what information do I need to make it well?"

**User testing is not market research.**
Market research: do people want this? User testing: can people use this? These are different questions, require different methods, and happen at different stages. User testing is not useful for validating demand; it is useful for identifying usability failures.

**Prototyping is not the goal; it is a tool.**
Prototyping exists to answer questions. When there are no remaining questions, prototyping stops. A team that continues prototyping when the design is clear is avoiding the decision to commit to production. This is analogous to refactoring code that works rather than shipping the feature.

**"How might we" questions are divergent prompts, not solution requests.**
"How might we make medication tracking easier for nurses?" is a divergent framing -- it invites any solution. It is not asking for one answer. The "HMW" format was developed by IDEO to keep teams in generative mode when they reflexively move to evaluation.
