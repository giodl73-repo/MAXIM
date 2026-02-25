# SysML: Systems Modeling Language

## The Big Picture

SysML (Systems Modeling Language) is a general-purpose visual modeling language for systems engineering. It is a profile (restricted extension) of UML 2.x adapted for SE — retaining some UML diagrams, modifying others, and adding new ones specific to systems engineering.

```
SYSML vs UML
──────────────────────────────────────────────────────────────────
UML (Unified Modeling Language):
  Designed for software systems modeling
  13 diagram types, software-centric

SysML (subset + extensions of UML):
  Reuses 7 of UML's 13 diagrams (with modifications)
  Adds 2 new diagram types (Requirements, Parametric)
  Designed for systems (hardware, software, humans, procedures)

SysML is standardized by OMG (Object Management Group)
Current version: SysML 1.x (mature)
  SysML 2.0 (major revision in progress, pure model, no diagram focus)

SYSML DIAGRAM TAXONOMY
──────────────────────────────────────────────────────────────────
                    ┌─────────────┐
                    │   SysML     │
                    │  Diagrams   │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐  ┌──────▼──────┐ ┌────▼──────────┐
    │  Behavior   │  │  Structure  │ │ Cross-Cutting │
    │  Diagrams   │  │  Diagrams   │ │  Diagrams     │
    └──────┬──────┘  └──────┬──────┘ └───────────────┘
           │                │         Requirements (req)
    ┌──────┤         ┌──────┤         Parametric (par)
    │      │         │      │
   act   seq       bdd    ibd
   stm   uc        pkg
```

---

## SysML Diagram Types

### Block Definition Diagram (bdd) — Structure

```
BLOCK DEFINITION DIAGRAM
──────────────────────────────────────────────────────────────────
The "class diagram" equivalent for systems.
Shows: blocks (system elements), their properties, and relationships.

  bdd [Package] Vehicle [Vehicle Structure]
  ┌─────────────────────────────────────────┐
  │ «block»                                  │
  │ Vehicle                                  │
  ├─────────────────────────────────────────┤
  │ values:                                  │
  │   mass: kg = 1500                        │
  │   maxSpeed: m/s                          │
  ├─────────────────────────────────────────┤
  │ parts:                                   │
  │   engine: Engine [1]                     │
  │   transmission: Transmission [1]         │
  │   wheels: Wheel [4]                      │
  └─────────────────────────────────────────┘
         │ composition             inheritance
         ◆                              ◁
    ┌────▼────┐                  ┌──────────────┐
    │ Engine  │                  │  Vehicle     │
    └─────────┘                  │  (general)   │
                                  └──────────────┘
                                        △
                                  ┌─────┴──────┐
                                  │  Car        │
                                  └─────────────┘

Composition ◆: part cannot exist without whole
Aggregation ◇: part can exist independently
Association  : relationship
Generalization ◁: specialization (subtype)
```

### Internal Block Diagram (ibd) — Internal Structure

```
INTERNAL BLOCK DIAGRAM
──────────────────────────────────────────────────────────────────
Shows the INTERNAL structure of a specific block:
  - Parts (internal components)
  - Connectors (how parts connect)
  - Ports (connection points on block boundary)
  - Flow specifications (what flows through connections)

  ibd [Block] Aircraft [Internal Structure]
  ┌──────────────────────────────────────────────────────────────┐
  │ :Aircraft                                                    │
  │  ┌──────────┐   fuel   ┌────────────┐  power ┌──────────┐  │
  │  │:Fuel     ├──────────►:Propulsion │ ──────►│:Avionics │  │
  │  │System   │           │           │         │          │  │
  │  └──────────┘  thrust  └─────┬──────┘         └──────────┘  │
  │                              │                               │
  │                              ▼ thrust                        │
  │  ┌──────────┐         ┌──────────────┐                      │
  │  │:Flight   │◄────────│:Structures   │                      │
  │  │Control   │ loads   │              │                      │
  │  └──────────┘         └──────────────┘                      │
  └──────────────────────────────────────────────────────────────┘

Ports: proxy port (delegates to part), full port (own behavior)
Flow ports: specify direction and type of flow (energy, material, data)
```

### Package Diagram (pkg) — Namespace Organization

```
PACKAGE DIAGRAM
──────────────────────────────────────────────────────────────────
Organizes model elements into namespaces (like Java packages).
Shows dependencies between packages.

  pkg [Model] SystemModel [Architecture]
  ┌──────────────────────────────────────┐
  │ «package»  «package»  «package»      │
  │ Structure  Behavior   Requirements   │
  │ ─────────  ─────────  ────────────   │
  │ Aircraft   MissionOps SysReqs        │
  │   ├─bdd    ├─act      ├─req          │
  │   ├─ibd    ├─seq      └─par          │
  │   └─pkg    └─stm                     │
  └──────────────────────────────────────┘

Use cases: grouping related elements, access control,
reuse (import one package into another)
```

### Use Case Diagram (uc) — External Behavior

```
USE CASE DIAGRAM
──────────────────────────────────────────────────────────────────
Same concept as UML use cases — actors and system interactions.

  uc [Package] MissionSystem [Mission Scenarios]
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  ┌────────┐                                         │
  │  │Operator├────► (Navigate to Target)               │
  │  └────────┘      (Monitor System Health)            │
  │                  (Communicate with HQ)              │
  │  ┌────────┐                                         │
  │  │  HQ   ├────► (Transmit Mission Orders)          │
  │  └────────┘      (Receive Status Reports)          │
  │                                                     │
  │  Extend / Include relationships between use cases   │
  └─────────────────────────────────────────────────────┘
```

### Activity Diagram (act) — Behavior / Process Flow

```
ACTIVITY DIAGRAM
──────────────────────────────────────────────────────────────────
Shows flow of control and data across activities.
Used for: operational scenarios, process models, data flows.

  act [Activity] StartupSequence [System Startup]
       ┌──────────────────────────────────┐
       │         ● (start)                │
       │         │                        │
       │    [Power on]                    │
       │         │                        │
       │  ┌──────▼──────┐                 │
       │  │Initialize BIT│ (built-in test) │
       │  └──────┬───────┘                │
       │         │                        │
       │    [BIT passed?]                 │
       │       /    \                     │
       │     Yes    No                   │
       │      │      │                   │
       │  [Continue] [Fault→Ground]       │
       │      │                          │
       │      ● (end)                    │
       └──────────────────────────────────┘

Object flow: data passed between activities
Control flow: sequence of activities
Swim lanes: which actor/block performs each activity
```

### Sequence Diagram (sd) — Message Interaction

```
SEQUENCE DIAGRAM
──────────────────────────────────────────────────────────────────
Shows time-ordered sequence of messages between system elements.
Directly equivalent to UML sequence diagram.

  sd [Interaction] SensorDataFlow [GPS Update Cycle]
  ┌────────────────────────────────────────────────────┐
  │  :GPS      :NavProcessor    :FlightController      │
  │  Sensor                                            │
  │    │              │                   │             │
  │    │──GPS frame──►│                   │             │
  │    │              │──pos, vel, time──►│             │
  │    │              │                   │─servo cmd──►│
  │    │              │                   │             │
  │    │ (every 1 Hz) │ (computed in <10ms)│             │
  │                                                    │
  └────────────────────────────────────────────────────┘

Combined fragments: loop, opt (optional), alt (conditional),
  par (parallel), break (exception exit)
Duration constraints: labels specify timing requirements
```

### State Machine Diagram (stm) — Discrete States

```
STATE MACHINE DIAGRAM
──────────────────────────────────────────────────────────────────
Shows states of a block and transitions between them.
Used for: lifecycle states, mode management, protocol modeling.

  stm [Block] Aircraft [Flight Mode States]

          ┌─────────────┐
       ●──► GROUND      │
          │    (init,   │
          │     check)  │
          └──────┬──────┘
                 │  takeoff clearance received / throttle up
                 ▼
          ┌─────────────┐   engine flame-out
          │ CLIMB       ├─────────────────────────────────┐
          └──────┬──────┘                                  │
                 │ altitude reached                        │
                 ▼                                        │
          ┌─────────────┐                                  │
          │ CRUISE      │                                  ▼
          └──────┬──────┘                          ┌──────────────┐
                 │ descent                         │  EMERGENCY   │
                 ▼                                 └──────────────┘
          ┌─────────────┐
          │ APPROACH /  │
          │ LANDING     │
          └──────┬──────┘
                 │ touchdown
                 ▼
               ● (terminal)

Entry/exit actions on states
Guard conditions [in brackets] on transitions
Internal transitions: events that don't change state
```

### Requirements Diagram (req) — New in SysML

```
REQUIREMENTS DIAGRAM
──────────────────────────────────────────────────────────────────
Unique to SysML (not in UML).
Shows requirements and their relationships visually.

  req [Package] SystemRequirements [Top Level]
  ┌───────────────────────────────────────────────────────────────┐
  │ «requirement»                «requirement»                     │
  │ System Capabilities          Performance                       │
  │   id="REQ-SYS-001"           id="REQ-SYS-010"                 │
  │   text="The system shall     text="The system shall           │
  │   support 6000nm range"      detect targets at ≥50km"         │
  │                                         │                      │
  │ «deriveReqt»          «containment»     │ «refine»             │
  │ id="REQ-FUEL-005"     │                 ▼                      │
  │ text="Fuel system     ▼        «requirement»                   │
  │ shall have 20 ton     [child   Detection Range                 │
  │ capacity"             reqs]    id="REQ-SEN-001"                │
  └───────────────────────────────────────────────────────────────┘

Relationships:
  «deriveReqt»:    requirement derived from another (design choice)
  «refine»:        requirement refined by model element (design)
  «satisfy»:       block satisfies requirement
  «verify»:        test case verifies requirement
  «trace»:         general traceability (no formal semantics)
  «containment»:   hierarchy (parent-child requirement)
```

### Parametric Diagram (par) — Constraints / Analysis

```
PARAMETRIC DIAGRAM
──────────────────────────────────────────────────────────────────
Unique to SysML (not in UML).
Shows mathematical/constraint relationships between value properties.
Used to capture performance models, equations, analyses.

  par [Block] VehicleDynamics [Range Equation]
  ┌─────────────────────────────────────────────────────────────┐
  │  {Breguet Range Equation}                                   │
  │                                                             │
  │  ┌──────────┐  L/D  ┌────────────────┐   W0  ┌─────────┐  │
  │  │L/D ratio ├──────►│ Range:         │◄──────│Initial  │  │
  │  └──────────┘       │ R = (V/SFC)×   │       │weight W0│  │
  │                     │  (L/D)×ln(W0/W1│       └─────────┘  │
  │  ┌──────────┐  SFC  │                │   W1  ┌─────────┐  │
  │  │SFC       ├──────►│                │◄──────│Final    │  │
  │  └──────────┘       └───────┬────────┘       │weight W1│  │
  │                              │ R              └─────────┘  │
  │                     ┌────────▼────────┐                    │
  │                     │  Range R: nmi   │                    │
  │                     └─────────────────┘                    │
  └─────────────────────────────────────────────────────────────┘

Connects value properties via constraint blocks
Enables parametric analysis within the model
Can be linked to external simulation tools (Simulink, MATLAB)
```

---

## SysML Tools

| Tool | Vendor | Notes |
|------|--------|-------|
| Cameo Systems Modeler | Dassault Systèmes (No Magic) | Industry standard, full SysML 1.x |
| Rhapsody | IBM | Strong code/simulation integration |
| Enterprise Architect | Sparx Systems | Lower cost, broad use |
| Capella | Eclipse (Thales) | Open source, ARCADIA methodology |
| Papyrus | Eclipse Foundation | Open source, SysML plugin |
| Atoll | PTC (Integrity) | PLM integration |
| Siemens Teamcenter | Siemens | Full PLM + MBSE integration |

---

## Stereotypes and Tagged Values

SysML (and UML generally) extends base notation via stereotypes:

```
STEREOTYPE SYNTAX
──────────────────────────────────────────────────────────────────
«block»         : a system element (physical or logical)
«flowSpecification» : type of flow on a flow port
«constraint»    : mathematical constraint in parametric diagram
«requirement»   : a requirement element
«testCase»      : a test case (verifies a requirement)
«rationale»     : justification for a modeling decision
«view»          : a filtered perspective on the model

Tagged values (additional attributes):
  {id = "REQ-001", text = "...", status = "approved", ...}
```

---

## MBSE Relationship

SysML is the notation. MBSE is the methodology. The model built in SysML IS the design documentation — not an auxiliary diagram. See 08-MBSE.md for how the model replaces documents in MBSE practice.

---

## Decision Cheat Sheet

| I want to show... | Diagram type |
|-------------------|-------------|
| What parts make up a system | Block Definition Diagram (bdd) |
| How internal parts connect and communicate | Internal Block Diagram (ibd) |
| How users interact with the system | Use Case Diagram (uc) |
| Sequence of messages between elements | Sequence Diagram (sd) |
| System states and mode transitions | State Machine Diagram (stm) |
| Operational flow (activities, branches) | Activity Diagram (act) |
| Requirements and their relationships | Requirements Diagram (req) |
| Math relationships between parameters | Parametric Diagram (par) |
| How model elements are organized | Package Diagram (pkg) |

---

## Common Confusion Points

**SysML is not UML**: SysML reuses UML syntax but has different semantics. A SysML block is NOT the same as a UML class. Blocks don't have constructors/destructors — they model physical entities. A SysML port is not a UML interface. Reading UML books to learn SysML gives you the wrong mental model.

**ibd vs bdd**: The bdd defines TYPES (like a class definition). The ibd shows INSTANCES within a context (like an object diagram). A bdd shows "Car has an Engine part." An ibd shows "this specific Car instance has this specific Engine instance connected by this fuel line."

**Parametric diagrams need constraint blocks**: You cannot just draw equations in a parametric diagram — constraint blocks must be defined in a bdd first, then instantiated in the par. The notation is precise about the distinction between type (bdd constraint block) and instance (par binding).

**Stereotypes are not tags**: A stereotype (<<block>>) is a metaclass extension — it classifies the element type. A tagged value {status="approved"} is a property of the element. They are syntactically similar in diagrams but semantically different in the metamodel.

**SysML 2.0 is a breaking change**: SysML 2.0 (OMG in progress, 2024+) replaces the UML-profile approach with a dedicated kernel. Models will NOT be backward compatible with SysML 1.x. For current programs, use SysML 1.6 (the current stable version). Migration path from 1.x to 2.0 is being developed by tool vendors.
