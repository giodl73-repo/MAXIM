# Cognitive and Cultural Anthropology

## The Big Picture

```
+------------------------------------------------------------------+
|             COGNITIVE AND CULTURAL ANTHROPOLOGY                  |
|                                                                  |
|  Where mind, material culture, and cumulative knowledge meet     |
+------------------------------------------------------------------+
         |              |              |              |
         v              v              v              v
  +-----------+ +-----------+ +-----------+ +-----------+
  | DISTRIBUTED| | MATERIAL  | | NICHE     | | CULTURAL |
  | COGNITION  | | CULTURE   | | CONSTRUC- | | EVOLUTION |
  |            | | & MIND    | | TION      | |          |
  +-----------+ +-----------+ +-----------+ +-----------+
  | Hutchins   | | Malafouris| | Odling-   | | Richerson |
  | Clark/Cha  | | Object    | | Smee      | | /Boyd     |
  | lmers      | | agency    | | Laland    | | Henrich   |
  | Suchman    | | Latour    | | Gene-cult | | WEIRD     |
  +-----------+ +-----------+ +-----------+ +-----------+

         +----------------------------------+
         | COGNITIVE ARCHAEOLOGY            |
         | Symbolic behavior origins        |
         | Dunbar's number                  |
         | Language origins                 |
         +----------------------------------+
```

---

## Section 1: Distributed Cognition

### Hutchins — Cognition in the Wild (1995)

```
  TRADITIONAL VIEW: Cognition = processes inside a single skull.
  Think "the brain solves the problem."

  HUTCHINS' OBSERVATION (studying US Navy navigation teams):
  The navigation team is a cognitive system.
  The "computation" of the ship's position is distributed across:
  - Multiple crew members with different partial knowledge
  - Instruments (gyrocompass, radar, bearing repeaters)
  - Charts and navigation tools
  - Procedures and protocols that coordinate information flow
  - The physical layout of the bridge

  ┌────────────────────────────────────────────────────────┐
  │ The fix computation (determining position):            │
  │                                                        │
  │ Bearing taker 1 -> bearing to landmark A -> pelorus    │
  │ Bearing taker 2 -> bearing to landmark B -> pelorus    │
  │ Chart table     -> plot both bearings -> intersection  │
  │                    = ship's position                   │
  │                                                        │
  │ NO SINGLE PERSON knows the position until the          │
  │ distributed process completes.                         │
  │ The "computation" is in the team + instruments + space.│
  └────────────────────────────────────────────────────────┘

  REPRESENTATIONAL STATES:
  The navigation computation is a series of transformations
  of representational states:
  physical bearing -> spoken/signaled number -> plotted line
  -> intersection -> position -> course correction

  The representation propagates through the sociotechnical system.
  "Cognition" is wherever the representation is being transformed.

  IMPLICATIONS FOR SOFTWARE ENGINEERING:
  Your team is a distributed cognitive system. The codebase
  is external memory. Code review is a representational state
  transformation. Documentation is not overhead — it is the
  system's working memory. When a key engineer leaves, you
  don't just lose "a person" — you lose a crucial node in
  a distributed cognitive system that cannot be rebuilt quickly.
```

### The Extended Mind Thesis — Clark and Chalmers (1998)

```
  THE THOUGHT EXPERIMENT (Otto and Inga):

  INGA: wants to go to Museum of Modern Art. She thinks about
  it, recalls it is on 53rd Street, walks there.
  The information was in her biological memory.

  OTTO: has Alzheimer's. He always carries a notebook.
  He wants to go to MoMA. He looks in his notebook, finds
  "MoMA is on 53rd Street," walks there.

  QUESTION: Is Otto's notebook part of his mind?

  Clark/Chalmers' answer: YES, under functional equivalence.
  The notebook plays the same functional role for Otto
  that biological memory plays for Inga:
  - It was reliably available when he consulted it
  - It was directly endorsed for action upon retrieval
  - It was endorsed unconditionally (he doesn't question it)
  - It was previously endorsed (he wrote it in good faith)

  PARITY PRINCIPLE:
  If a process, if it were located in the head, we would
  not hesitate to call it cognitive, then we should not
  hesitate to call it cognitive when it occurs outside the
  head, if it plays the same functional role.

  IMPLICATIONS:
  ┌────────────────────────────────────────────────────────┐
  │ External artifacts can be PART of the cognitive system,│
  │ not merely TOOLS used by it.                           │
  │                                                        │
  │ Software tools: IDE, documentation, version control    │
  │ -> not just tools but extensions of developer cognition│
  │                                                        │
  │ AI assistants: if your coding assistant functions as   │
  │ part of your working memory and reasoning process,     │
  │ is it part of the cognitive system? Clark would say    │
  │ yes, conditionally.                                    │
  │                                                        │
  │ Org knowledge: team wikis, architectural decision      │
  │ records (ADRs), runbooks -> extended organizational    │
  │ cognition. Their degradation is cognitive degradation. │
  └────────────────────────────────────────────────────────┘

  CRITICISMS:
  - Cognitive bloat: this makes everything "cognitive"
  - Active externalism requires causal coupling, not just
    functional equivalence
  - The notebook doesn't "forget" the way neural memory
    does — the dynamics are genuinely different
  The debate is productive rather than settled.
```

### Suchman — Plans and Situated Actions (1987)

```
  XEROX PARC STUDY of people using photocopiers:

  OBSERVATION: When someone encounters a problem with the
  copier, they do NOT follow the plan (user manual, mental
  script). They improvise, try things, read the machine's
  responses, adapt.

  KEY CLAIM:
  Plans are not instructions for action.
  Plans are POST-HOC RATIONALIZATIONS of what happened.
  Action is fundamentally SITUATED — responsive to the
  local environment in real time, not pre-scripted.

  ┌────────────────────────────────────────────────────────┐
  │ "The purpose of plans is not to control action —       │
  │  it is to provide retrospective accounts of it."       │
  └────────────────────────────────────────────────────────┘

  IMPLICATIONS FOR ENGINEERING ORGS:
  This is a direct challenge to top-down planning culture:

  - Sprint plans are not instructions for what engineers
    will do; they are frameworks that will be revised
    constantly as work reveals hidden complexity.

  - Architecture documents are not constraints; they are
    starting-point resources that practitioners adapt.

  - "Why didn't you follow the plan?" — because situated
    action is adaptive, not plan-following. The question
    reveals a misunderstanding of how work actually happens.

  - Agile methodology is partly the institutionalization
    of Suchman's insight: build in feedback loops that
    accommodate situated adaptation rather than enforcing
    plan compliance.
```

---

## Section 2: Material Culture and the Mind

### Malafouris — Material Engagement Theory

```
  Lambros Malafouris: the mind does not REPRESENT the world
  and then ACT on it. Mind and matter are MUTUALLY CONSTITUTIVE.

  EXAMPLE: Clay and the potter's hands.
  When a potter works clay:
  - The potter's intention shapes the clay
  - The clay's resistance and affordances shape the potter's
    next intentions and movements
  - Neither is prior; they co-emerge in the engagement

  The cognitive process is not in the head and then executed
  on the clay. The cognitive process IS the hand-clay interaction.

  IMPLICATIONS:
  - Writing doesn't just record thought; writing SHAPES thought.
    The act of writing a document forces cognitive restructuring.
  - Drawing architecture diagrams doesn't just communicate
    architecture; the drawing process reveals design issues
    that pure mental modeling misses.
  - Code review: the act of reading and annotating changes
    what the reviewer notices and how they think about the code.

  Malafouris calls this "metaplasticity" — the cognitive
  system (including the extended mind) is reshaped by its
  own engagements with material culture.
```

### Latour — Actants and Sociotechnical Systems

```
  Bruno Latour's Actor-Network Theory (ANT):

  ACTANTS: anything that acts in a network, whether human
  or non-human. Door-closers, texts, microbes, and
  politicians are all actants if they affect the network.

  Not "the users use the tool."
  Not "the tool is just an artifact."
  Rather: "humans-and-tools form a network in which all
  components have agency."

  EXAMPLE: The Microbe and Pasteur
  Pasteur didn't defeat cholera. Pasteur + institutions +
  laboratories + funding bodies + the microbe ITSELF
  (which is detectable in specific ways, not others) +
  public health infrastructure — the network changed the
  world. The microbe is an actant.

  ENGINEERING RELEVANCE:
  "The code doesn't do what I told it to do" — yes, the
  code is an actant. It has properties that resist, redirect,
  and transform the intentions put into it. The computer
  system is not a passive tool; it is a participant with
  its own constraints that shape what engineers can do.

  This reframing is not mysticism — it is recognition that
  non-human elements of sociotechnical systems have
  deterministic effects that must be negotiated, not simply
  commanded. Infrastructure is an actant; it shapes
  organizational behavior as much as it is shaped by it.
```

---

## Section 3: Niche Construction and Gene-Culture Coevolution

### Niche Construction Theory

```
  STANDARD EVOLUTIONARY VIEW:
  Organisms adapt to their environments.
  Environment is an independent variable; organism adapts.

  NICHE CONSTRUCTION (Odling-Smee, Laland, Feldman 2003):
  Organisms MODIFY their environments, creating new
  selection pressures that feed back on the organism.

  ┌────────────────────────────────────────────────────────┐
  │ Example: Earthworms                                    │
  │ Earthworms digest soil -> change pH, drainage,         │
  │ nutrient availability -> changes selection pressure    │
  │ on earthworms AND on other soil organisms.             │
  │ The earthworm is adapting TO an environment it         │
  │ partially CREATED.                                     │
  └────────────────────────────────────────────────────────┘

  HUMAN CULTURAL NICHE CONSTRUCTION:
  Humans construct their niche primarily through culture.
  This creates gene-culture coevolution.

  CANONICAL CASES:
  ┌────────────────────────────────────────────────────────┐
  │ FIRE AND COOKING (~1 Ma):                              │
  │ Fire -> cooking -> more caloric extractable from food  │
  │ -> supports larger brain -> larger brain enables better │
  │ fire management. And: cooking -> softer food ->        │
  │ reduced jaw muscle -> smaller jaw -> face shape change │
  │ -> further changes in social signaling.                │
  │                                                        │
  │ CATTLE HERDING + LACTASE PERSISTENCE:                  │
  │ Cattle herding (cultural) creates abundant milk supply │
  │ -> adults who can digest lactose have higher fitness   │
  │ -> lactase persistence gene rises in frequency.        │
  │ Culture created the selection pressure for the gene.   │
  │                                                        │
  │ AGRICULTURE + STARCHY DIET + AMYLASE:                  │
  │ Grain agriculture -> starchy diet -> individuals with  │
  │ more copies of AMY1 (salivary amylase gene) digest     │
  │ starch better -> AMY1 copy number increases in         │
  │ agricultural populations. Farmers have more AMY1 than  │
  │ foragers.                                              │
  │                                                        │
  │ SETTLEMENT + CROWD DISEASES:                           │
  │ Dense settlements -> new pathogen ecology (measles,    │
  │ smallpox require dense hosts) -> selection for immune  │
  │ variants -> genetic differences between populations    │
  │ with long vs. short agricultural histories.            │
  └────────────────────────────────────────────────────────┘
```

### Dual Inheritance Theory — Richerson and Boyd

```
  Humans inherit through TWO transmission systems:
  1. GENES: biological inheritance, Mendelian/quantitative
  2. CULTURE: social learning, accumulated over generations

  These systems interact:
  - Genes constrain what culture can do
    (language has universal constraints from gene-based
    language capacity)
  - Culture changes selection pressure on genes
    (as above: lactase, AMY1, etc.)

  CULTURAL EVOLUTION AS POPULATION DYNAMICS:
  Cultural variants spread through populations by:

  ┌────────────────────────────────────────────────────────┐
  │ CONTENT BIAS: people preferentially adopt variants     │
  │ that "work" — effective farming techniques,            │
  │ successful hunting methods. Direct evaluation.         │
  │                                                        │
  │ MODEL BIAS (PRESTIGE BIAS): copy what successful       │
  │ people do, regardless of whether you can evaluate      │
  │ why they're successful. Copy high-prestige individuals.│
  │ Efficient when evaluation is costly.                   │
  │                                                        │
  │ FREQUENCY-DEPENDENT BIAS (CONFORMISM): copy what       │
  │ most people do. "When in Rome." Adaptive when local    │
  │ adaptation has occurred and you don't know what.       │
  │                                                        │
  │ CULTURAL DRIFT: random fluctuation (small populations  │
  │ lose cultural variants by chance — analogous to        │
  │ genetic drift in small populations)                    │
  └────────────────────────────────────────────────────────┘

  BIG-MISTAKE THEORY:
  In novel environments, natural selection cannot fine-tune
  cultural behavior fast enough. Genetic evolution is too slow.
  Cultural evolution fills the gap — but it can also produce
  maladaptive behaviors in novel environments (obesity from
  evolved fat/sugar cravings; status competition via
  consumerism; etc.).
```

---

## Section 4: The WEIRD Thesis — Deep Version

### Henrich's "WEIRDest People in the World" (2020)

```
  THE PARADOX:
  Western social science discovered "human nature" by
  studying Western (usually American college) students.
  This "human nature" turns out to be WEIRD psychology —
  statistically unusual globally.

  THE MECHANISM (Henrich's argument):
  ┌────────────────────────────────────────────────────────┐
  │ Medieval Western Christian Church (particularly        │
  │ post-Papal Revolution, ~1000-1300 CE) banned:          │
  │ - Cousin marriage (to 6th degree initially)            │
  │ - Levirate marriage (marrying brother's widow)         │
  │ - Polygamy                                             │
  │ - Adoption                                             │
  │                                                        │
  │ WHY: Church accumulated donations and estates from     │
  │ dying members. Kin-based inheritance threatened this.  │
  │ Destroying kin groups served Church economic interests.│
  │                                                        │
  │ EFFECT OVER CENTURIES:                                 │
  │ - Extended kin networks weakened (no clans, no lineages│
  │   in Western Europe, uniquely)                         │
  │ - Nuclear family became primary unit                   │
  │ - Need for trust with NON-KIN strangers grew           │
  │ - Voluntary associations (guilds, universities,        │
  │   corporations) replaced kin groups                    │
  │ - Impersonal institutions (courts, contracts, law)     │
  │   became necessary and valued                          │
  └────────────────────────────────────────────────────────┘

  THE RESULTING PSYCHOLOGY (WEIRD):
  - High impersonal trust and prosociality
  - Analytical (object-focused) rather than holistic
    (relation-focused) cognition
  - Individualism (personal identity not lineage identity)
  - Abstract rule-following (rules apply universally,
    regardless of who you are relative to me)
  - Guilt-based (internal) vs. shame-based (social)
    moral psychology

  This psychology is NOT "modern" or "educated" — it is
  a SPECIFIC HISTORICAL PRODUCT of Western Catholicism.
  Northern European and American Protestants show the
  most extreme WEIRD psychology; Southern European
  Catholics less so; non-Western populations vary widely.
```

---

## Section 5: Dunbar's Number and the Social Brain

### The Neocortex Ratio Prediction

```
  ROBIN DUNBAR (1992-present):

  SOCIAL BRAIN HYPOTHESIS:
  Primate brains expanded primarily to manage social
  complexity, not ecological complexity (foraging, spatial
  navigation, etc.). Evidence: neocortex size predicts
  social group size across primate species.

  THE DATA:
  Plot neocortex volume / total brain volume (neocortex ratio)
  against mean social group size across ~40 primate species.
  Strong positive correlation (r ~0.7).

  HUMAN PREDICTION:
  Human neocortex ratio predicts group size of ~150.

  VALIDATIONS:
  ┌────────────────────────────────────────────────────────┐
  │ Hunter-gatherer bands: typical ~150 (range 100-200)    │
  │ Hutterite communities: split when >150 (historically)  │
  │ Gore-Tex: factories deliberately split at ~150         │
  │ Roman maniple: ~130-160 soldiers (tactical unit)       │
  │ Military units: company size ~100-200 in most armies   │
  │ Christmas card networks (UK study): ~150 active social │
  │ relationships maintained by typical person             │
  └────────────────────────────────────────────────────────┘

  THE NESTED STRUCTURE (Dunbar's circles):
  ~5: close support clique (most intimate)
  ~15: sympathy group
  ~50: band (can coordinate directly)
  ~150: community (Dunbar number)
  ~500: mega-band (can form coalitions)
  ~1,500: tribe (linguistic/identity group)

  MECHANISM:
  The constraint is the COGNITIVE OVERHEAD of tracking
  relationships: who is allied with whom, who owes what
  to whom, who has what status, who can be trusted.
  This requires "social arithmetic" — a demanding
  computational task even for large brains.

  Language may have evolved as "grooming at a distance"
  — physical grooming maintains social bonds in other
  primates; language enables bonding at scale (gossip,
  shared narratives, social information exchange).
```

---

## Section 6: Cognitive Archaeology — Inferring Minds from Matter

### What Material Culture Requires Cognitively

```
  COGNITIVE ARCHAEOLOGY (Mithen, Renfrew):
  Infer cognitive capacities from the archaeological record.
  What does it take to make this artifact?

  OLDOWAN CORE TOOLS (~2.6 Ma):
  ┌────────────────────────────────────────────────────────┐
  │ Requires: 3D spatial modeling of stone fracture        │
  │           mechanics.                                   │
  │ Not trivial: experimental archaeologists take weeks    │
  │ to learn. Knapping requires understanding conchoidal   │
  │ fracture, stone quality, angle of percussion.          │
  │                                                        │
  │ Does NOT clearly require: language, theory of mind,    │
  │ teaching (may be learned by observation alone)         │
  └────────────────────────────────────────────────────────┘

  ACHEULEAN HANDAXE (~1.7 Ma):
  ┌────────────────────────────────────────────────────────┐
  │ Requires: hierarchical planning (mental template       │
  │           imposed on stone before starting);           │
  │           mental rotation in 3D; working memory        │
  │           to hold the template while executing.        │
  │                                                        │
  │ Possibly: teaching (too complex for pure imitation?)   │
  │ Probably NOT: language (same template for 1.5 My       │
  │               with no variation suggests no cumulative │
  │               cultural change — no language driving it)|
  └────────────────────────────────────────────────────────┘

  MOUSTERIAN HAFTED TOOLS (~200-40 ka):
  ┌────────────────────────────────────────────────────────┐
  │ Requires: multi-part thinking (stone + handle +        │
  │           adhesive as unified concept);                │
  │           planning ahead (manufacture before need);    │
  │           understanding of material properties         │
  │                                                        │
  │ Possibly indicates: symbolic thinking about object     │
  │ identity persisting across disassembly/reassembly      │
  └────────────────────────────────────────────────────────┘

  BLOMBOS OCHRE ENGRAVINGS (75 ka):
  ┌────────────────────────────────────────────────────────┐
  │ Requires: making a MARK that refers to something else  │
  │           (symbolic reference)                         │
  │ This is the minimum requirement for symbolic cognition │
  │                                                        │
  │ Indicates: abstract, combinatorial thought;            │
  │           possibly the cognitive prerequisite for      │
  │           language and cumulative culture              │
  └────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| I want to understand... | Framework |
|------------------------|-----------|
| Why team knowledge > individual knowledge | Distributed cognition (Hutchins) |
| Why wikis/docs are part of the cognitive system | Extended mind (Clark/Chalmers) |
| Why engineering plans are always revised | Situated action (Suchman) |
| Why drawing/writing clarifies thinking | Material engagement (Malafouris) |
| Why "the code fights back" | Actants and sociotechnical systems (Latour) |
| Why gene-culture coevolution happened | Niche construction (Odling-Smee/Laland) |
| Why lactase persistence is a cultural product | Dual inheritance theory (Richerson/Boyd) |
| Why WEIRD psychology is not universal | Henrich 2020 — historical Catholic Church hypothesis |
| Why orgs split at ~150 people | Dunbar's number — cognitive load of relationship tracking |
| What ancient tools tell us about ancient minds | Cognitive archaeology (Mithen, Renfrew) |

---

## Common Confusion Points

**"Distributed cognition means 'teamwork.'"**
Hutchins means something stronger: the COGNITIVE PROCESSES (representation
transformation) are literally distributed across people and artifacts. Not just
that teams achieve more than individuals, but that the computational process
occurs across the sociotechnical system, with no locus purely "in a head."

**"Extended mind means smartphones have made us dumb."**
The extended mind thesis is neutral on whether external cognitive scaffolding
is beneficial. Clark and Chalmers argue the notebook IS part of Otto's mind —
they make no claim that this is worse than internal memory. The "smartphones
make us dumb" anxiety is a separate empirical claim requiring evidence.
Clark would likely argue the smartphone-extended mind is a different kind of
mind, not a diminished one.

**"Dunbar's 150 means companies should never exceed 150 people."**
Dunbar's number predicts the size of STABLE TRUST-BASED groups that can
coordinate without formal management hierarchy. Larger organizations exist
but require formal institutional structures (hierarchy, rules, roles) to
function — because the cognitive load of tracking ~1000+ relationships
informally is prohibitive. It is a constraint on informal coordination,
not a hard limit on organization size.

**"WEIRD just means 'not from developing countries.'"**
No — the WEIRD variable is specifically psychological, and it doesn't track
development status cleanly. Some populations in wealthy non-Western countries
(Japan, South Korea, Singapore) are non-WEIRD in many key dimensions despite
high economic development. The hypothesis is about kin-based social structure
and the cultural history that created specific psychological profiles.

**"Cultural evolution = social progress."**
Cultural evolution is a neutral population dynamics framework. Cultural
variants spread by frequency-dependent bias, prestige bias, and content
bias — not necessarily by being "better" in any absolute sense. Harmful
beliefs spread if they attach to prestigious models or become majority
practices. The framework is descriptive, not teleological.
