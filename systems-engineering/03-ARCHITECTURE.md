# System Architecture and Trade Studies

## The Big Picture

System architecture is the high-level structural decomposition of a system — what the major elements are, how they are connected, and which design principles govern the whole. Architecture decisions are the most consequential and most expensive to change. Getting them right early is the leverage point of SE.

```
WHAT ARCHITECTURE DEFINES
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  System boundary         │  What is inside vs outside           │
│  Functional decomposition│  What the major functions are        │
│  Physical decomposition  │  What the major components are       │
│  Interfaces              │  How elements connect and communicate│
│  Allocation              │  Which physical element does which   │
│                          │  function                            │
│  Design principles       │  Redundancy strategy, fault tolerance│
│                          │  make/buy decisions, modularity      │
│  Constraints             │  Technology limits, standards, budget│
└─────────────────────────────────────────────────────────────────┘
```

---

## Architecture Views and Frameworks

Different stakeholders need different perspectives. Architecture frameworks provide standard views.

### DoDAF (Department of Defense Architecture Framework)

```
DODAF VIEW TYPES
──────────────────────────────────────────────────────────────────
All Views (AV):  Context and glossary
  AV-1: Overview and summary
  AV-2: Integrated dictionary

Operational Views (OV): What the system must do
  OV-1: High-level operational concept graphic
  OV-2: Operational resource flow
  OV-3: Operational resource flow matrix
  OV-5: Operational activity model

Systems Views (SV): How the system does it
  SV-1: Systems interface description
  SV-2: Systems resource flow
  SV-4: Systems functionality description
  SV-10: Systems event-trace description (behavior)

Technical Standards Views (TV):
  TV-1: Technical standards profile (which standards apply)

Bridge: DoDAF = DoD-specific version of enterprise architecture.
Aligns with TOGAF (commercial) and ArchiMate (notation standard).
```

### MBSE Architecture Views

In Model-Based SE (addressed in 08-MBSE.md), SysML provides:
- Block Definition Diagrams (BDD): physical/logical structure
- Internal Block Diagrams (IBD): internal connections and flows
- Use Case Diagrams: external interactions
- State Machine Diagrams: system behavioral states
- Activity Diagrams: operational activities
- Sequence Diagrams: inter-element message flows

---

## Functional Architecture

### Functional Decomposition

```
FUNCTIONAL DECOMPOSITION
──────────────────────────────────────────────────────────────────
Start with top-level system function (mission function):
  "Deliver payload to destination"

Decompose to Level 1 functions:
  1.1 Navigate to destination
  1.2 Monitor system health
  1.3 Communicate with ground
  1.4 Manage payload

Each Level 1 decomposes further:
  1.1.1 Receive navigation input
  1.1.2 Compute optimal path
  1.1.3 Actuate flight control surfaces
  1.1.4 Monitor position error

Decompose until functions are at a level where
a single technology/component can fulfill them.
Stop when a function can be directly allocated
to a known component type.

FUNCTIONAL FLOW BLOCK DIAGRAM (FFBD):
  Shows sequence, branches, and iterations of functions
  "F1 → F2 → [F3A OR F3B] → F4"
  Used in defense SE (MIL-HDBK-499)
```

The N-squared diagram is the physical-systems counterpart of the Dependency Structure Matrix (DSM) used in software architecture analysis — both map inter-module coupling in a square matrix, expose coupling density and circular dependencies (cycles), and identify high-fan-out modules (packed rows).

### N-squared Diagram (N-squared)

```
N² DIAGRAM: INTERFACE MAPPING
──────────────────────────────────────────────────────────────────
Matrix where rows and columns = system elements.
Off-diagonal cells = interfaces between elements.

     │ Nav  │ Prop │ Power│ Comm │ GNC  │
─────┼──────┼──────┼──────┼──────┼──────┤
Nav  │ self │  ─   │ 28V  │  ─   │ pos  │
Prop │  ─   │ self │ 28V  │  ─   │thrust│
Power│  ─   │  ─   │ self │  ─   │  ─   │
Comm │  ─   │  ─   │ 28V  │ self │  ─   │
GNC  │nav sv│thrust│  ─   │cmd   │ self │

Row→column: what element in row PROVIDES to element in column
Column→row: what element in row RECEIVES from element in column

N² diagram reveals:
  Hidden interfaces (are any crossed out?)
  Circular dependencies (follow circular paths)
  Concentrated coupling (one element has many connections = integration risk)
  Interface inventory for ICD planning
```

---

## Physical Architecture

### Allocation: Function → Form

```
FUNCTIONAL TO PHYSICAL ALLOCATION
──────────────────────────────────────────────────────────────────
Functions from functional architecture must be
allocated to physical components.

Function              →  Physical element
1.1.2 Compute path    →  Mission Computer (hardware + software)
1.1.3 Actuate surfaces→  Flight Control Computer + Actuators
1.2 Monitor health    →  Onboard Health Management System
1.3 Communicate       →  UHF Radio + Datalink

One function → one physical element: simple (one-to-one)
One function → multiple elements: implemented across subsystems
Multiple functions → one element: multifunctional unit (complex)

Allocation matrix documents this formally.
```

### Architecture Patterns in Complex Systems

```
COMMON PHYSICAL ARCHITECTURE PATTERNS
──────────────────────────────────────────────────────────────────
FEDERATED ARCHITECTURE
  Each subsystem has its own processor and buses
  Traditional approach (pre-2000 aircraft, spacecraft)
  High redundancy per subsystem
  High SWaP (size/weight/power) — lots of duplicated hardware

CENTRALIZED / IMA (Integrated Modular Architecture)
  Shared computing resources (processors, I/O)
  Partitioned software runs on common hardware
  DO-178C, ARINC 653 partitioning
  Boeing 787, Airbus A380 avionics — saves weight, complexity
  Single hardware failure can affect multiple functions (risk)

DISTRIBUTED (service-oriented)
  Many processing nodes on high-bandwidth network
  Functions as services, network provides integration
  Modern vehicles (automotive Ethernet, automotive SOA)
  Tesla's EE architecture: zone-based with central compute

HIERARCHICAL (layered control)
  Mission level → Subsystem level → Component level
  Each level commands/queries level below
  Industrial automation: PLC → drive → actuator
```

---

## Trade Studies

A trade study is a formal comparison of architecture alternatives against multiple criteria. It replaces informal "gut feeling" decisions with documented, defensible analysis.

### Pugh Matrix (Concept Selection Matrix)

```
PUGH MATRIX
──────────────────────────────────────────────────────────────────
        │ Criteria │ Weight │ Alt A │ Alt B │ Alt C │
        ├──────────┼────────┼───────┼───────┼───────┤
        │ Range    │  0.30  │ DATUM │   +   │   –   │
        │ Speed    │  0.25  │ DATUM │   +   │   S   │
        │ Cost     │  0.20  │ DATUM │   –   │   +   │
        │ Maint.   │  0.15  │ DATUM │   S   │   S   │
        │ Risk     │  0.10  │ DATUM │   –   │   –   │
        ├──────────┼────────┼───────┼───────┼───────┤
        │ Score    │        │  0    │ +0.25 │ -0.05 │

+ = better than datum, – = worse, S = same
Weighted: (+0.30+0.25 – 0.20 – 0.10) × weights

When: early concept selection, many alternatives, qualitative
Good for: narrowing field from many alternatives
Weakness: "+" and "–" are subjective; may mask quantitative differences
```

### Weighted Decision Matrix (AHP — Analytic Hierarchy Process)

```
WEIGHTED DECISION MATRIX
──────────────────────────────────────────────────────────────────
1. Define criteria and weights (sum to 1.0)
2. Score each alternative on each criterion (1–10 or 0–5)
3. Weighted score = sum(weight × score) per alternative

Example: Sensor selection trade study

Criterion    Weight  Optical  RF     Acoustic
──────────────────────────────────────────────
Detection    0.30      9      7        4
Range        0.25      8      9        3
All-weather  0.20      3      9        6
Cost         0.15      6      5        8
SWaP         0.10      7      5        7

Weighted     ─        6.95   7.35     5.00
scores

Result: RF sensor wins on this criteria set.

AHP formalizes criteria weighting via pairwise comparisons
  (Saaty scale 1–9)
Ensures logical consistency in weights.
```

### Multi-Attribute Utility Theory (MAUT)

For quantitative trade studies where alternatives have known performance numbers on each criterion. Each criterion is converted to a dimensionless utility (0–1) via a utility function, then weighted and summed. More rigorous than simple weighting — handles non-linear value functions (risk aversion, diminishing returns).

---

## Architecture Patterns and Their Tradeoffs

```
ARCHITECTURAL TRADEOFF SPACE
──────────────────────────────────────────────────────────────────
REDUNDANCY:
  None:         Simple, cheap, SPOF (single point of failure)
  Passive (hot): Both units active, failure → instant switchover
  Active/standby: Standby detects failure, activates (seconds)
  Voting (TMR):  3 units vote, 2-of-3 continues with disagreement

  TMR:  ┌──A──┐
        ├──B──┤ → Voter → Output
        └──C──┘
  Detects: any single failure
  Masks:   any single failure (operation continues)
  Fails:   if 2 fail with same value (common cause)

COUPLING vs COHESION:
  Tight coupling:   subsystems directly dependent → fragile, hard to change
  Loose coupling:   clear interfaces, message-based → resilient, modular
  SE principle:     maximize cohesion within subsystem,
                    minimize coupling between subsystems

MODULARITY:
  Highly modular:   easy substitution, independent testing, upgrade path
                    Interface overhead → complexity, performance cost
  Integrated:       optimized for performance, hard to change
                    Platform-specific → integration risk

MAKE vs BUY vs REUSE:
  Make:   full control, custom performance, high cost + schedule risk
  Buy:    proven, fast, COTS → integration risk, support dependency
  Reuse:  heritage system → known properties, may need adaptation
  Hybrid: buy the COTS, integrate custom mission SW on standard HW
```

---

## Architecture Assessment

```
ARCHITECTURE ASSESSMENT METHODS
──────────────────────────────────────────────────────────────────
ATAM (Architecture Tradeoff Analysis Method) — SEI Carnegie Mellon
  Structured review of architecture against quality attributes
  Steps:
    1. Present architecture
    2. Identify architectural approaches for each quality scenario
    3. Analyze each approach against scenarios
    4. Find sensitivity points (one element affects multiple qualities)
    5. Find tradeoff points (improving one quality degrades another)
    6. Find risks and non-risks
  Output: prioritized list of risks and sensitivity points

Simulation-based assessment:
  Model architecture in simulation before hardware
  MATLAB/Simulink, SysML with parametric diagrams
  Evaluate performance, timing, resource utilization

Digital Twin for architecture evaluation:
  Build digital twin of the architecture model
  Run operational scenarios
  Evaluate emergent behavior

Failure mode impact at architecture level (FMAA — architectural FMEA):
  For each element, ask: what happens to the system if this fails?
  Identifies single points of failure in architecture
```

---

## Decision Cheat Sheet

| Architecture Decision | Method |
|-----------------------|--------|
| Select from several concepts | Pugh matrix (qualitative) |
| Select from alternatives with quantitative data | Weighted decision matrix or MAUT |
| Identify all interfaces between subsystems | N² diagram |
| Decompose system functions hierarchically | Functional decomposition + FFBD |
| Allocate functions to physical components | Allocation matrix |
| Assess architecture quality risks | ATAM |
| Check for single points of failure | Architectural FMEA |
| Document architecture for DoD program | DoDAF views (OV, SV, TV) |

---

## Common Confusion Points

**Architecture vs design**: Architecture defines the major structural elements and their relationships (subsystems, major components, interfaces). Design fills in the internal details of each element. The boundary is blurry, but the test is: "Would changing this decision require renegotiating the interface with other teams?" If yes, it's architectural.

**Functional architecture vs physical architecture**: Functional architecture describes what needs to happen (functions, data flows, sequences). Physical architecture describes what will do it (components, hardware, software). The allocation step maps function to form — this is where SE work is most creative and most risky.

**Trade studies require sensitivity analysis**: The weighted decision matrix result depends on the weights you chose. If changing a weight by 0.05 changes the winner, the trade study is sensitive to that criterion — you need more data or stakeholder alignment before the decision. Always check: what weight change would flip the decision?

**Architecture is not a diagram**: Architecture is the set of decisions that structure the system. A diagram is a representation. The decisions precede the diagram. A diagram without documented rationale is decoration — the rationale IS the architecture.

**"Best architecture" is context-dependent**: The "right" architecture for a $200M defense program (decades lifecycle, safety-critical, contractually locked) differs fundamentally from the right architecture for a consumer IoT product (12-month cycle, low margin, frequent updates). SE rigor must match lifecycle risk and cost.
