# 12 — Design Patterns Across Reality

## The Big Picture

This crosscut is the **Computing & Software companion atlas**. It uses section
number 12 because software gives the sharpest vocabulary for patterns:
interfaces, state, feedback, modularity, protocols, abstraction, composition,
and failure boundaries.

But the point is not to turn the library into software. The point is to show
that the same structural ideas recur in cells, cities, circuits, legal systems,
markets, instruments, materials, languages, and civilizations.

```
DESIGN PATTERNS ACROSS REALITY

A pattern is a reusable solution shape, not a reusable implementation.

BOUNDARIES
  interfaces, membranes, laws, APIs, skins
      |
      v
MODULES ---------> COMPOSITION ---------> HIERARCHY
parts vary        parts become systems   levels constrain
      |                   |                    |
      v                   v                    v
FEEDBACK <------> STATE <--------------> MEMORY
correction        what persists          history that matters
      |                   |                    |
      v                   v                    v
REDUNDANCY -----> BOTTLENECKS ---------> FAILURE
backup paths      constrained flow       where assumptions break

Same pattern, different substrate:
code, tissue, steel, water, law, song.
```

Read this as a **pattern stack**. A system has boundaries. Boundaries create
modules. Modules compose. Composition creates hierarchy. Hierarchy carries
state and memory. Feedback changes state. Redundancy protects function.
Bottlenecks constrain function. Failure reveals where the design assumptions
were wrong.

---

## Why This Belongs in Crosscuts, Not the Computing Volume

Computing already teaches many of these ideas in concrete form:

```
module       -> package, library, service
interface    -> API, type signature, protocol
state        -> memory, database, session, cache
feedback     -> control loop, retry, monitor, test failure
redundancy   -> replica, backup, quorum, fallback
bottleneck   -> hot path, lock, network hop, queue
failure      -> exception, outage, exploit, split brain
```

The crosscut asks the next question:

```
If that structure is visible in software,
where else does the same structure appear?
```

| Software Pattern | Biological Echo | Social Echo | Physical / Material Echo |
|---|---|---|---|
| API boundary | Cell membrane receptor | Legal jurisdiction | Valve, joint, seal |
| Modular service | Organ system | Department or guild | Replaceable component |
| Feedback loop | Endocrine regulation | Price signal, election | Thermostat, governor |
| Cache | Short-term memory | Institutional precedent | Thermal mass |
| Redundancy | Paired organs, immune diversity | Checks and balances | Safety factor, backup pump |
| Queue | Neural signal bottleneck | Court docket, port congestion | Traffic lane, pipeline |
| Protocol | Genetic code, signaling pathway | Treaty, standard | Measurement convention |

This is not metaphor for its own sake. It is a way to reason faster:

```
find the boundary -> identify what crosses it
find the state    -> identify what persists
find the feedback -> identify what corrects
find the bottleneck -> identify what limits
find the failure mode -> identify what assumption broke
```

---

## Layer 1: Boundaries and Interfaces

A boundary is where a system says: **inside behaves differently from outside**.
An interface is the controlled crossing point.

```
OUTSIDE WORLD
     |
     v
[ INTERFACE ]  what may cross, in what form, under what rule
     |
     v
[ SYSTEM ]     state, invariants, internal rules
```

| Field | Boundary | Interface | What Goes Wrong |
|---|---|---|---|
| Computing | Process, service, module | API, ABI, protocol | Leaky abstraction, version mismatch |
| Biology | Cell, organ, organism | Receptor, membrane channel, immune marker | Infection, autoimmune error |
| Law | Jurisdiction | Court, statute, treaty | Forum conflict, loophole |
| Architecture | Building envelope | Door, window, facade joint | Water intrusion, thermal bridge |
| Language | Speech community | Translation, grammar, notation | Ambiguity, untranslatable distinction |
| Materials | Phase or grain boundary | Interface layer, weld, adhesive | Delamination, corrosion, crack initiation |

**Old world -> new world bridge:** in older enterprise systems, you might have
called this "contract-first design" or "component boundaries." In modern
distributed systems it becomes API governance, schema evolution, auth scopes,
and backward-compatible deployment. In biology or law, the same boundary logic
appears with different substrates.

---

## Layer 2: Modularity and Composition

Modularity is not "parts." Everything has parts. Modularity means parts can
vary somewhat independently because their interfaces are stable enough.

```
TIGHT COUPLING                         MODULAR COUPLING

A changes -> B breaks                  A changes internally
        |                                      |
        v                                      v
   [ A-B-C ]                              [ A ]
                                               |
                                        stable interface
                                               |
                                             [ B ]
```

| Pattern Question | Ask It In Software | Ask It Outside Software |
|---|---|---|
| What can change independently? | Can the service deploy alone? | Can the organ, institution, or component adapt without redesigning the whole? |
| What contract must stay stable? | API, schema, type, protocol | Ritual, standard, law, joint, membrane, measurement |
| What is hidden behind the contract? | Implementation detail | Tacit craft, internal metabolism, manufacturing process |
| What breaks the modularity? | Shared database, hidden coupling | Correlated failure, shared resource, political dependency |

Composition is the second step: modules become systems.

```
parts -> assemblies -> subsystems -> systems -> ecosystems
```

That ladder appears in mechanics, biology, social systems, and software. The
danger is assuming that because the parts are understood, the composition is
understood. It usually is not.

---

## Layer 3: Feedback, State, and Memory

Feedback is information about the result of an action returning to influence
the next action.

```
        action
ACT -------------> WORLD
 ^                  |
 |                  v
 |               MEASURE
 |                  |
 |                  v
 +------------- COMPARE
        correction
```

Feedback only works if the system has state: something persists long enough
for correction to matter.

| Domain | State | Feedback | Memory |
|---|---|---|---|
| Control theory | Plant state | Sensor error | Controller integral term |
| Software | Database, cache, session | Tests, telemetry, user action | Logs, commits, event store |
| Biology | Hormone levels, gene expression | Receptor signaling | Immune memory, epigenetic marks |
| Ecology | Population, nutrients | Predator-prey response | Seed bank, soil history |
| Economics | Prices, inventories | Profit/loss, demand | Contracts, capital stock |
| Culture | Norms, canon, institutions | Criticism, imitation | Archive, tradition, curriculum |

The common failure is **bad measurement**:

```
bad sensor -> wrong feedback -> wrong correction -> amplified error
```

That one line covers broken tests, biased datasets, bad public metrics,
miscalibrated instruments, and ecological interventions that optimize the wrong
indicator.

---

## Layer 4: Redundancy, Diversity, and Resilience

Redundancy is duplicated capacity. Diversity is non-identical capacity.
Resilience usually needs both.

```
SAME BACKUP                         DIVERSE BACKUP

  Pump A                              Pump A
  Pump A clone                        Gravity feed
  Pump A clone                        Manual bypass

  survives one break                  survives design-class failure
  fails if design is wrong            costs more coordination
```

| System | Redundancy | Diversity | Fragility If Missing |
|---|---|---|---|
| Distributed systems | Replicas | Different zones, quorum paths | Single-region outage |
| Immune system | Many cells | Antibody diversity | Novel pathogen escape |
| Engineering | Safety factor, backup pump | Different failure principles | Common-mode failure |
| Agriculture | Seed stores | Crop diversity | Monoculture disease |
| Law/governance | Appeals, bicameralism | Competing institutions | Capture or arbitrary power |
| Knowledge | Replication | Independent methods | Groupthink, instrument bias |

**Common-mode failure** is the key abstraction. Three identical backups are not
three independent protections if the same design flaw, dependency, or incentive
can kill all three.

---

## Layer 5: Bottlenecks and Throughput

A bottleneck is the narrowest constraint in a flow. It can be physical,
informational, institutional, metabolic, or cognitive.

```
wide input       narrow constraint        wide demand
===========>  |  BOTTLENECK  |  =====================>
              |              |
              +--------------+

Throughput is not set by average capacity.
It is set by the constrained step.
```

| Flow | Bottleneck Examples | Typical Bad Fix |
|---|---|---|
| Software request | Lock, DB query, network hop, cold start | Add app servers while DB is saturated |
| Manufacturing | Critical machine, inspection station, supplier | Optimize non-critical workstations |
| Medicine | Triage, imaging, specialist review | Add beds without staffing |
| Logistics | Port, bridge, customs, warehouse | Buy more trucks |
| Ecology | Limiting nutrient, habitat corridor | Add food while habitat is gone |
| Education | Feedback quality, attention, prerequisite gap | Add content volume |

The diagnostic move is always:

```
trace the flow -> measure each queue -> find the constrained step
```

---

## Cross-Library Appearance Map

This crosscut should feel like a map over the existing deck, not a replacement
for it.

| Section | Where the Pattern Shows Up |
|---|---|
| Natural World | Taxonomy, food webs, soil systems, reef niches, species boundaries |
| Earth & Space | Watersheds, climate feedbacks, plate boundaries, orbital resonances |
| Material Culture | Grain boundaries, fiber structures, composite layers, joinery, surface coatings |
| Life Sciences | Membranes, organs, immune memory, neural loops, developmental pathways |
| History & Ideas | Institutional memory, historiography, causal chains, ethical boundary cases |
| Mechanics | Load paths, control systems, HVAC loops, acoustic resonances, manufacturing cells |
| Technology | Formal verification, infrastructure systems, robotics control, medical devices |
| Social Sciences | Incentives, games, organizations, law, public health, demography |
| Language & Communication | Syntax, semantics, protocols, translation interfaces, media channels |
| Mathematics & Physics | Symmetry, invariants, state spaces, phase transitions, information channels |
| Arts & Culture | Composition, constraints, style systems, performance feedback, design reduction |
| Computing & Software | APIs, modules, services, protocols, caches, consensus, security boundaries |
| People | Inventors, reformers, scientists, and artists as pattern recognizers under constraint |

---

## What This Crosscut Is For

Use it when a reader is trying to move from one field to another without losing
the structure of the problem.

```
KNOWN FIELD                         NEW FIELD
software service outage      ->     hospital throughput failure
API version mismatch         ->     legal jurisdiction conflict
cache invalidation           ->     institutional memory problem
feedback instability         ->     climate or market oscillation
common-mode outage           ->     monoculture crop disease
```

The bridge is not "everything is software." The bridge is:

```
systems expose recurring design shapes
```

Once the shape is recognized, the details still matter. A cell membrane is not
an API. A treaty is not a type signature. But all three enforce boundary rules,
and that shared structure is useful.

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether a problem is really a boundary problem | Identify what crosses, who validates it, and what invariant must be preserved | A boundary can be physical, legal, semantic, biological, or computational |
| Whether modularity is real | Ask what can change independently without forcing a whole-system redesign | Parts are not modules unless interfaces absorb variation |
| Whether composition changed behavior | Compare part-level behavior with system-level feedback and constraints | Emergent behavior is often a coupling effect, not mysticism |
| Whether feedback is stabilizing or destabilizing | Map sensor, comparator, actuator, delay, and gain | Bad measurement or delay turns correction into oscillation |
| Whether memory is helping or trapping the system | Separate useful persistence from stale state | Memory preserves learning and preserves bias |
| Whether redundancy is meaningful | Look for common-mode dependencies | Identical backups do not protect against design-class failure |
| Whether a bottleneck is real | Trace the flow and measure queues at each constrained step | Optimizing non-bottlenecks usually adds inventory, not throughput |
| Whether the pattern analogy is legitimate | Name the shared structure and the substrate-specific differences | Crosscuts are diagnostic lenses, not claims that all fields are the same |

---

## Common Confusion Points

**Pattern does not mean metaphor** — A metaphor says one thing is like another.
A pattern says two systems share a structural relation: boundary, state,
feedback, hierarchy, bottleneck, redundancy, or failure mode. The distinction
matters because patterns can guide diagnosis; loose metaphors mostly decorate.

**Modularity is not decomposition** — Breaking a system into pieces is easy.
Making pieces that can change independently is hard. The proof of modularity is
not a diagram; it is low-cost change behind stable interfaces.

**Feedback is not automatically good** — Positive feedback can accelerate
growth or collapse. Negative feedback can stabilize or suppress necessary
change. The sign, delay, gain, and measurement quality determine behavior.

**Redundancy is not resilience by itself** — Redundancy protects against
component failure. Diversity protects against common-mode failure. Resilience
also requires detection, switching, repair, and recovery time.

**Bottlenecks move** — Once one constraint is relieved, another becomes visible.
This is why optimization is iterative. The system's limiting factor is not a
permanent identity; it is the current narrowest constraint.

---

## Connection Forward

This pilot establishes the template for the remaining crosscuts:

```
01  Scale & Hierarchy                 -> Natural World
02  Infrastructure & Logistics         -> Earth & Space
03  Materials & Substrates             -> Material Culture
04  Energy & Flows                     -> Life Sciences
05  Time, Evolution & Memory           -> History & Ideas
06  Tools & Instruments                -> Mechanics
07  Systems & Failure                  -> Technology
08  Institutions & Standards           -> Social Sciences
09  Interfaces & Communication         -> Language & Communication
10  Methods of Knowing                 -> Mathematics & Physics
11  Practice, Craft & Judgment         -> Arts & Culture
12  Design Patterns Across Reality     -> Computing & Software
13  Risk, Uncertainty & Decision       -> People
```

Each crosscut should keep this discipline: one home section for publishing,
many sections for evidence, and no claim that the lens replaces the field.

