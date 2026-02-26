# Embodied and Extended Cognition

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    BEYOND BRAIN-IN-A-VAT COGNITION                    |
+-----------------------------------------------------------------------+
|                                                                       |
|  CLASSICAL COGNITIVE SCIENCE         EMBODIED / EXTENDED VIEW        |
|  +----------------------------+       +---------------------------+   |
|  | Mind = symbol manipulator  |       | Mind = embodied agent     |   |
|  | Brain = central processor  |       | Body + world = cognitive  |   |
|  | Body = peripheral I/O      |       | system                    |   |
|  | World = external input     |       | Brain-body-environment    |   |
|  |                            |       | = coupled system          |   |
|  | Cognition is INNER         |       | Cognition EXTENDS         |   |
|  | computation                |       | beyond the skull          |   |
|  +----------------------------+       +---------------------------+   |
|                                                                       |
|  THE 4E FRAMEWORK:                                                    |
|  Embodied + Embedded + Enacted + Extended                             |
+-----------------------------------------------------------------------+
```

---

## The Classical Cognitive Science Target

```
GOFAI: GOOD OLD-FASHIONED AI (Haugeland's term)
=================================================

Classical cognitive science (1950s-1980s):
  Mind = computation over symbolic representations.
  Intelligence = search through symbol-structured spaces.
  Cognition is substrate-independent (functionalism).
  The body is input/output, not constitutive of cognition.

  Logic Theorist (Newell/Simon 1956): first AI program.
  General Problem Solver (1957): means-ends analysis.
  GOFAI successes: chess (Deep Blue), theorem proving, games.

GOFAI ASSUMPTIONS:
  1. Knowledge is propositional (can be stated explicitly)
  2. Reasoning is inference over propositions
  3. The body provides inputs; the mind processes them
  4. Context is handled by explicit representations

DREYFUS'S PHENOMENOLOGICAL CHALLENGE (1972, 1979):
  Hubert Dreyfus: "What Computers Can't Do"
  Drawing on Heidegger, Merleau-Ponty:
  Human cognition is grounded in embodied, skillful engagement
  with a world, not in explicit symbol manipulation.

  DREYFUS'S HEIDEGGER ANALYSIS:
  Heidegger: READY-TO-HAND vs. PRESENT-AT-HAND

  Ready-to-hand: using a hammer skillfully, not attending to it.
    You are "absorbed" in hammering; the hammer is transparent.
    The world recedes; only the goal (the nail, the joint) shows.
    This is NORMAL tool use.

  Present-at-hand: the hammer breaks. Now you examine it.
    The hammer becomes an OBJECT of attention.
    You now have explicit propositional knowledge of it.
    But this is the EXCEPTIONAL case, not the norm.

  DREYFUS'S POINT:
  GOFAI treats all cognition as if things were present-at-hand.
  Explicit symbolic representation is what appears when
  normal absorbed engagement BREAKS DOWN.
  Expert skill is absorbed engagement, not rule-following.
  No program can capture this because embodied background
  competence cannot be fully made explicit.
```

---

## Embodied Cognition

### Lakoff and Johnson: Philosophy in the Flesh

```
LAKOFF/JOHNSON: "PHILOSOPHY IN THE FLESH" (1999)
=================================================

CORE CLAIM: Concepts are not abstract symbols.
They are grounded in sensorimotor experience.

CONCEPTUAL METAPHORS:
  Our most abstract concepts are understood via concrete bodily experience.

  UP = GOOD: "Things are looking up." "I'm feeling down."
  ARGUMENT IS WAR: "I demolished his argument." "She defended her position."
  UNDERSTANDING IS GRASPING: "I get it." "Can you grasp this idea?"
  LIFE IS A JOURNEY: "I've come a long way." "She's at a crossroads."

  These are not decorative metaphors -- they are how we THINK.
  Abstract reasoning runs on concrete sensorimotor structure.

EMPIRICAL SUPPORT (cognitive linguistics):
  Cross-linguistic: these conceptual metaphors are very widespread.
  Developmental: infants develop conceptual metaphors via embodied
  interaction (UP/DOWN comes from being lifted; WARM/COLD comes
  from being held; POWER comes from height differential with adults).

  Brain imaging: abstract "up-good" judgments activate sensorimotor
  cortex for upward movement.

IMPLICATION FOR AI:
  LLMs trained on text learn linguistic manifestations of conceptual
  metaphors.
  Do they have the underlying sensorimotor grounding?
  Lakoff/Johnson: no. They have the words, not the concepts.
  Whether that matters for cognitive function is debated.
```

### Enactivism

```
ENACTIVISM (Varela, Thompson, Rosch: "The Embodied Mind", 1991)
================================================================

AUTOPOIESIS (Maturana & Varela 1972):
  Living systems are self-producing (auto = self, poiesis = production).
  A cell maintains its own organization by producing its own components.
  The boundary between self and environment is constituted by the system.

  This is different from: input --> processor --> output.
  The system ENACTS its own environment by making distinctions
  that matter for its survival.

  A bacterium enacts a world of nutrients and toxins.
  It doesn't represent the world -- it enacts a world through
  its sensorimotor coupling with the environment.

COGNITION AS ENACTION:
  Cognition is not a matter of representing an independent world.
  Cognition is the process by which the organism ENACTS a domain
  of interactions with an environment.
  "Knowing is doing" -- not "knowing is representing."

  Vision: traditional view = camera that captures images.
  Enactivist view: vision is a sensorimotor skill --
  a set of expectations about how visual input changes
  with movement. We explore the visual scene; we don't photograph it.

RELEVANCE FOR AI:
  Current AI: mostly representational (models of world states).
  Enactivists: genuine cognition requires sensorimotor coupling
  with an environment, not just representation.
  A robot that explores and acts is closer to enactivist cognition
  than a text-generating system.
```

---

## The Extended Mind Thesis

```
CLARK AND CHALMERS: "THE EXTENDED MIND" (1998)
================================================

QUESTION: "Where does the mind stop and the rest of the world begin?"

THE PARITY PRINCIPLE:
  If, as we confront some task, a part of the world functions
  as a process which, were it done in the head, we would have
  no hesitation in recognizing as part of the cognitive process,
  then that part of the world is (as we claim it to be) part of
  the cognitive process.

  More simply: if it plays the FUNCTIONAL ROLE of a cognitive
  state, it IS a cognitive state, regardless of location.

THE OTTO/INGA THOUGHT EXPERIMENT:
  INGA wants to go to the Museum of Modern Art.
  She consults her memory: remembers it's on 53rd Street.
  Goes there.

  OTTO has Alzheimer's.
  He carries a notebook in which he writes information.
  He consults the notebook: it says 53rd Street.
  Goes there.

  Clark/Chalmers:
  Inga's memory = Otto's notebook, functionally.
  Both guide behavior in response to a desire.
  Both are reliably and immediately accessible.
  Both are endorsed as correct by the agent.

  Therefore: Otto's notebook is part of his BELIEF that the
  Museum is on 53rd Street.
  His cognitive system extends into the world.

FUNCTIONAL CONDITIONS FOR EXTENDED COGNITIVE STATES:
  1. Reliably accessible (can be consulted when needed)
  2. Endorsed by the agent (agent doesn't doubt it usually)
  3. Automatically endorsed (no more scrutiny than internal memory)
  4. Reliably available (not intermittent)
```

### Objections to Extended Mind

```
OBJECTIONS TO EXTENDED MIND THESIS
=====================================

1. THE COUPLING-CONSTITUTION FALLACY (Adams & Aizawa):
   Just because a brain process is COUPLED TO an external process
   doesn't mean the external process CONSTITUTES cognition.
   A heart is coupled to blood; blood doesn't constitute the heart.
   The relevant question is what's inside the cognitive system,
   not what it interacts with.

   CLARK'S RESPONSE:
   For Otto: the notebook doesn't just couple with cognition.
   It plays exactly the same functional role as internal memory.
   The coupling IS constitutive in this case.
   The argument turns on whether parity is maintained.

2. MARK OF THE COGNITIVE (Adams & Aizawa):
   Cognition involves representations with derived intentionality
   (content intrinsically, not via interpretation).
   Otto's notebook has derived intentionality (it means what it
   means because Otto and others interpret it).
   Therefore: it doesn't have the right kind of intentionality
   to be genuinely cognitive.

   RESPONSE: This objection only works if Searle's original
   intentionality/derived intentionality distinction is correct.
   Functionalists deny this distinction is fundamental.

3. THE TRUST/ENDORSEMENT PROBLEM:
   We scrutinize external memory in ways we don't scrutinize
   internal memory (usually).
   "Did I write this down correctly?" vs.
   "Did I remember this correctly?"
   External memory requires additional verification.
   RESPONSE: This is an empirical contingency, not a conceptual barrier.
```

---

## Distributed Cognition

```
HUTCHINS: DISTRIBUTED COGNITION (1995, "Cognition in the Wild")
=================================================================

HUTCHINS' CLAIM:
  The unit of cognitive analysis should not be the individual.
  Many cognitive tasks are distributed across:
  - Multiple people
  - Artifacts and tools
  - Environmental structures

CASE STUDY: NAVIGATION ON A NAVAL VESSEL:
  Traditional cognitive psychology: captain makes decision.
  Hutchins: navigation is a cognitive system consisting of:
  - Multiple crew members (bearing-takers, helm, navigator)
  - Instruments (compass, radar, charts, depth sounder)
  - Communication protocols
  - Representational artifacts (chart, plotting tool, bearing log)

  The COGNITIVE PROCESS of navigation is distributed across
  all these components.
  No individual "has" the navigation cognition.
  The system as a whole navigates.

IMPLICATIONS:
  Cognitive science should study systems, not just brains.
  Workplace design is cognitive system design.
  Artifacts are cognitive components, not just tools.

  This maps directly to software engineering: a development team + IDE + documentation + tests + CI/CD pipeline is a distributed cognitive system. Productivity and error rates are properties of the entire system — not reducible to individual developer capability. The pipeline (build server, automated tests, dashboards, deployment gates) is a cognitive artifact that extends the team's capacity to hold and verify system state. Removing any component degrades the cognitive system as a whole, even if no individual loses any knowledge. This is Hutchins' key finding: when the ship's instruments fail, the crew does not simply resort to doing computationally what they were doing instrumentally — the cognitive task genuinely changes character.
```

---

## The Moravec Paradox and Embodied AI

```
MORAVEC PARADOX (1988)
=======================

"It is comparatively easy to make computers exhibit adult level
performance on intelligence tests or playing checkers, and
difficult or impossible to give them the skills of a one-year-old
when it comes to perception and mobility."

  HARD FOR HUMANS:                EASY FOR HUMANS:
  Chess                           Walking over uneven ground
  Symbolic reasoning              Recognizing faces
  Mathematical proof              Catching a thrown ball
  Jeopardy                        Grasping objects reliably

  EASY FOR AI:                    HARD FOR AI:
  Chess (Deep Blue 1997)          Dexterous manipulation
  Symbolic math                   Open-world navigation
  Text generation (LLMs)          Common sense physical reasoning
                                  Embodied task execution

WHY?
  High-level reasoning = recent evolutionary development.
  Narrow cortical modules, relatively small neural real estate.
  EASY to copy in silicon.

  Sensorimotor skills = 540 million years of evolution.
  Huge neural real estate (60% of brain volume).
  HARD to copy in silicon.

  Brooks' embodied robotics (1990):
  "Intelligence without representation."
  The subsumption architecture: layers of behavior-producing modules.
  No central world model.
  Behavior emerges from embodied interaction.
  Roomba is a descendant.

IMPLICATION FOR LLMs:
  LLMs are good at "high-level" language tasks -- which map to
  recent evolutionary developments.
  LLMs lack physical grounding -- poor at tasks requiring
  understanding of physical causality, spatial reasoning,
  manipulation planning.
  This is consistent with the Moravec paradox.
```

---

## Decision Cheat Sheet

| If evaluating AI claim... | The embodied cognition counter is... |
|---|---|
| "LLMs understand physical causality / spatial reasoning" | Moravec paradox + enactivism: sensorimotor grounding is 540 million years of evolution; abstract language processing is recent. LLMs have the shallow layer (recent evolutionary layer = narrow cortical module) but lack the foundation (sensorimotor coupling). Consistent with observed failures in physical reasoning tasks. |
| "Adding tools/APIs to an LLM gives it grounded cognition" | Clark/Chalmers extended mind can support this — if the tool is reliably accessible and automatically endorsed, it may qualify as an extended cognitive component. But Dreyfus counter: tool use in the extended mind sense still requires the right kind of sensorimotor coupling. A robot with tools is different from an LLM with API calls. |
| "LLMs will achieve human-level common sense with scale" | Dreyfus: expert-level skill is absorbed engagement, not rule-following at scale. GOFAI (which Dreyfus critiqued) also improved with scale without achieving common sense. Deep learning is architecturally different from GOFAI, but the missing embodied grounding concern still applies. |
| "A team using AI tools is just a human team with better tools" | Hutchins distributed cognition: the team + AI tools is a new cognitive system with different properties from either component alone. Productivity, error patterns, and failure modes are properties of the whole system. Managing the cognitive system well requires understanding how the distributed components interact — not just evaluating individual tools. |
| "Conceptual reasoning is substrate-independent" | Lakoff/Johnson: abstract concepts are built on sensorimotor schemas. The words are substrate-independent; the conceptual structure they encode may not be. LLMs learn the linguistic manifestations of conceptual metaphors without the underlying sensorimotor grounding — whether this matters for the conceptual operations they can perform is empirically open. |
| "AI systems will be conscious when sufficiently complex" | Enactivism/Merleau-Ponty: consciousness may require autopoietic sensorimotor coupling with an environment, not just sufficient computational complexity. A sufficiently complex text processor might still lack the embodied engagement that constitutes experience. |

---

## Common Confusion Points

**"Embodied cognition means you can't think without a body."**
The strong claim is that cognition is constituted by embodied sensorimotor engagement, not just caused by it. The moderate claim is that many cognitive capacities are shaped by embodiment and require it. The empirical claim is that abstract thought borrows structure from sensorimotor systems. Which version you accept affects how you think about AI — from "LLMs are fundamentally limited" to "LLMs lack some optional capacities."

**"The extended mind thesis says everything you interact with is part of your mind."**
No. Clark and Chalmers have specific functional conditions: reliable accessibility, automatic endorsement, etc. The car radio doesn't become part of your mind when you listen to it. But a smartphone that you reliably consult for navigation, schedule, and contacts — and would be cognitively impaired without — might qualify. The conditions are demanding.

**"Dreyfus was proven wrong by AlphaGo and ChatGPT."**
Dreyfus's critique of GOFAI (symbolic AI) was largely vindicated — GOFAI failed for exactly the reasons he predicted (brittleness, commonsense, embodied skills). Deep learning and LLMs are fundamentally different from GOFAI. Dreyfus's critique does not straightforwardly apply to neural networks. However, Dreyfus-style concerns about physical grounding and embodiment remain relevant: LLMs struggle with physical reasoning, manipulation, and open-world navigation.

**"Distributed cognition means no one is responsible for group decisions."**
Hutchins is making a point about where cognitive processes occur, not about moral responsibility. That navigation is distributed across a crew doesn't mean no one is responsible for errors. Moral responsibility is a different level of description. Distributed cognition describes the cognitive architecture; responsibility attribution happens at a different level.

**"Autopoiesis (enactivism) is just saying living things maintain themselves."**
Autopoiesis is more precise: a system is autopoietic if it produces its own components and maintains its own boundary as a thermodynamically open system far from equilibrium. This specific kind of self-organization is proposed as the key to what makes something cognitive (not just alive). The claim is that cognition requires autopoietic organization, not just any self-maintenance.
