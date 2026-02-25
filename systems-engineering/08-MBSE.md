# Model-Based Systems Engineering (MBSE)

## The Big Picture

MBSE replaces document-centric SE with a central authoritative model. Instead of a pile of documents (SRS, ICD, architecture description) that go out of sync with each other, the model IS the design. Documents are generated views of the model.

```
DOCUMENT-CENTRIC SE (Traditional)
──────────────────────────────────────────────────────────────────
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│   SRS    │  │   ICD    │  │  Arch    │  │  FMEA    │
│ v3.2.1   │  │ v2.1.0   │  │  Descr   │  │ v4.0     │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
     │              │              │             │
     └──────────────┴──────────────┴─────────────┘
                           │
               No automated consistency check
               Manual cross-referencing
               Version drift inevitable
               Requirement changed in SRS, not propagated to ICD
               FMEA references wrong architecture version

MODEL-BASED SE (MBSE)
──────────────────────────────────────────────────────────────────
                    ┌──────────────────────────────┐
                    │       SYSTEM MODEL             │
                    │                              │
                    │  Requirements + Architecture  │
                    │  + Behavior + ICDs + Analyses  │
                    │  All in one consistent model  │
                    └──────────────────────────────┘
                         │           │           │
                         │  generate views       │
                   ┌──────┘      ┌───┘       ┌──────┘
                   ▼             ▼            ▼
               SRS view      ICD view    Test view
               (auto-gen)   (auto-gen)   (auto-gen)
               Always        Always      Always
               consistent    consistent  consistent
```

**Bridge**: MBSE is the software analog of moving from "architecture documented in Word docs" to "architecture as code" (Infrastructure as Code, OpenAPI specs, GraphQL schemas). The model is the single source of truth. Documents are derived artifacts.

---

## Why MBSE?

```
MBSE MOTIVATION
──────────────────────────────────────────────────────────────────
Problem 1: Ambiguity in natural language
  "The system shall respond quickly" → 10 engineers, 10 interpretations
  Model: "ResponseTime: Duration [unit=ms] ≤ 200" → unambiguous

Problem 2: Traceability is manual in documents
  Requirement changed → manually find all affected items → miss some
  Model: change requirement → automated impact analysis → consistent

Problem 3: Integration of analysis
  FEA model, FMEA spreadsheet, requirements doc → separate tools
  Model: single data source → analysis driven from model data

Problem 4: Communication across disciplines
  Mechanical engineer reads SRS differently from software engineer
  Model: multiple views of same model → each discipline sees their view
  Consistent because generated from same underlying data

Problem 5: Reuse
  "Can we reuse this subsystem design?" → compare docs manually
  Model: compare models formally → automated compatibility check
```

---

## MBSE Methodologies

### INCOSE OOSEM (Object-Oriented SE Method)

```
OOSEM METHOD
──────────────────────────────────────────────────────────────────
Object-Oriented approach applied to SE
Uses SysML as modeling language

Steps:
1. Analyze stakeholder needs (use case model)
2. Define system requirements (SysML requirements diagram)
3. Define logical architecture (BDD + IBD at logical level)
4. Synthesize physical architecture (allocate to physical)
5. Optimize and evaluate (parametric diagrams, simulation)
6. Integrate (verify interfaces via model)
```

### ARCADIA / Capella

```
ARCADIA METHODOLOGY (Thales, widely used in France/Europe)
──────────────────────────────────────────────────────────────────
Four analysis levels:
  OA: Operational Analysis
    Who uses the system? Operational capabilities needed?
    Actors, operational activities, operational capability

  SA: System Analysis
    What does the system do (functions)?
    System functions, data flows, system interfaces (external)

  LA: Logical Architecture
    How does the system do it (logical components)?
    Logical components, logical data flows

  PA: Physical Architecture
    How is it implemented (physical components)?
    Physical component allocation, ICDs, technologies

Tool: Capella (Eclipse-based, open source, Thales)
Widely used in French defense, rail, automotive (Thales, Airbus)
Strong functional analysis capability
```

### RFLP (Dassault Systèmes / Cameo)

```
RFLP METHOD (Requirements-Functional-Logical-Physical)
──────────────────────────────────────────────────────────────────
R - Requirements    Stakeholder and system requirements
F - Functional      Functional decomposition, data flows
L - Logical         Architecture (vendor-agnostic)
P - Physical        Actual product configuration

Each level traced to next
Cameo Systems Modeler (formerly Magic Systems) implements RFLP
Popular in aerospace (Boeing, Airbus, NASA)
Strong integration with simulation (Simulink via SysML parametric)
```

---

## MBSE Tools Landscape

```
MBSE TOOL CATEGORIES
──────────────────────────────────────────────────────────────────
Full MBSE Tools (SysML-capable):
  Cameo Systems Modeler    Industry standard (Dassault/No Magic)
    → Best SysML 1.x implementation, Java-based, expensive
  IBM Rhapsody             IBM, strong HW/SW co-design, code gen
  YAKINDU (itemis CREATE)  Strong state machine focus
  Enterprise Architect     Sparx Systems, lower cost, broad use
  Papyrus (Eclipse)        Open source, SysML plugin
  Capella (Thales/Eclipse) Open source, ARCADIA-specific

Requirements Management (MBSE adjacent):
  IBM DOORS / DOORS Next   Industry standard RM tool
  Jama Connect             Modern RM, collaboration focus
  Polarion ALM             Siemens, full ALM

Simulation integration:
  MATLAB/Simulink          Parametric analysis, behavior sim
  SystemC / ModelSim       Hardware simulation
  AMESim (Siemens)         Multi-domain physical simulation
  OpenModelica             Open source Modelica

PLM Integration:
  Windchill (PTC)          PLM backbone, MBSE add-on
  Teamcenter (Siemens)     PLM + simulation + MBSE
  Enovia (Dassault)        CATIA ecosystem MBSE
```

---

## The System Model Contents

```
WHAT GOES IN THE SYSTEM MODEL
──────────────────────────────────────────────────────────────────
Requirements layer:
  Stakeholder needs
  System requirements (all levels)
  Derived requirements
  Rationale
  Verification methods

Structural layer:
  Block hierarchy (system → subsystems → components)
  Interface definitions (ports, flow specifications)
  ICDs captured as IBD connections
  Allocation matrix (function → physical)

Behavioral layer:
  Use cases (external interactions)
  Activity diagrams (operational flows)
  Sequence diagrams (message timing)
  State machines (mode management)

Analysis layer:
  Parametric constraints (performance equations)
  Budgets (mass, power, link margin, volume)
  FMEA capture (criticality attributes on blocks)
  Trade study parameters

Verification layer:
  Test cases linked to requirements
  Test results (pass/fail) against requirements
  Verification methods per requirement
```

---

## Digital Thread and Digital Twin

```
DIGITAL THREAD
──────────────────────────────────────────────────────────────────
The digital thread is the continuous data lineage from:
  Customer requirement → system model → design → manufacturing
  → test → operations → sustainment → disposal

All data linked, traceable, consistent.
No data islands. No manual re-entry.

┌─────────┐    ┌──────────┐    ┌─────────┐    ┌─────────────┐
│Customer │    │ System   │    │  CAD /  │    │ MES / Test  │
│ Need    │───►│  Model   │───►│  CAM    │───►│ Results     │
│ (CRM)   │    │ (MBSE)   │    │  (PLM)  │    │ (MES/QMS)   │
└─────────┘    └──────────┘    └─────────┘    └──────────────┘
         single data model, bidirectional traceability

DIGITAL TWIN (in SE context):
  Physical system running in operation
  + digital model continuously updated from sensor data
  = digital twin

  Uses in MBSE:
    Virtual commissioning: test control software on digital twin
    Operational monitoring: compare actual vs model predictions
    Failure prediction: model-driven prognostics
    Fleet management: each unit has its own twin
```

---

## MBSE in Practice: Typical Implementation Path

```
MBSE ADOPTION JOURNEY
──────────────────────────────────────────────────────────────────
Level 0 — Documents only
  Word/Excel/PDF for all SE artifacts
  No model tool

Level 1 — Tool adoption
  SysML tool purchased, introductory training
  Some requirements in tool
  Diagrams created but disconnected from documents

Level 2 — Partial model
  Requirements in DOORS or equivalent
  SysML used for architecture diagrams
  Some traceability established
  Still dual-maintenance (docs AND model)

Level 3 — Model as source
  Model generates views (PDF/Word/HTML)
  Documents derived from model, not independently maintained
  Traceability complete
  Analysis (FMEA, budgets) driven from model data

Level 4 — Executable model
  Behaviors in model are simulated / analyzed automatically
  Parametric constraints evaluated → performance prediction
  Test cases generated from model
  Near real-time consistency checks

Level 5 — Digital thread
  Model connected to PLM, CAD, MES, test tools
  Full digital thread: requirement → design → build → test
  Continuous update from production/operations
  Most programs at 1–3, few at 4, almost none at 5 today
```

---

## Budgets and Resource Tracking in MBSE

```
RESOURCE BUDGETS
──────────────────────────────────────────────────────────────────
A "budget" is a shared resource allocated across subsystems.
MBSE model captures allocations and rolls them up.

Common budgets:
  Mass:          Structural weight budget (kg allocated per subsystem)
  Power:         Available watts per subsystem, from power system
  Volume / SWaP: Size, Weight, and Power (military systems)
  Thermal:       Heat dissipation to shared cooling system
  Link margin:   RF link budget (dB margins for comm system)
  CPU utilization: Software CPU budget per process/partition
  Memory:        RAM and storage allocation per software partition
  ICD bandwidth: Data rate budget on shared buses

Model-based budget roll-up:
  Each block has a valueProperty "mass: kg"
  Parent block computes sum of children
  Constraint: sum ≤ budget allocation
  Parametric diagram enforces this automatically
  → No spreadsheet, automatically consistent with architecture changes
```

---

## MBSE and Safety Standards

```
MBSE INTEGRATION WITH SAFETY
──────────────────────────────────────────────────────────────────
DO-178C (avionics SW): safety objectives derived from hazard analysis
  Model-based requirements → FMEA in model → Derived safety objectives
  → Software requirements with DAL (Design Assurance Level) in model

ARP4754A (aircraft development): MBSE becoming standard approach
  Model traces: requirement → design → analysis → test
  Design organization approval for MBSE use (FAA/EASA)
  Tool qualification (DO-330) for safety-critical model use

ISO 26262 (automotive): V-model required
  MBSE tools used at Item Integration and Testing (HARA in model)
  Safety goals → functional safety requirements → SysML

IEC 61508 (general functional safety):
  Evidence artifacts can be model-generated views
  Traceability matrix auto-generated from model

Tool qualification:
  For model tool to generate safety-critical artifacts,
  the tool itself must be qualified (DO-330 / ISO 26262 Part 8)
  This adds process overhead — not all programs qualify tools
```

---

## Decision Cheat Sheet

| MBSE Decision | Choice |
|---------------|--------|
| Primary MBSE tool for defense program | Cameo Systems Modeler |
| Primary MBSE tool for European rail/defense | Capella (ARCADIA) |
| Requirements management in MBSE context | IBM DOORS Next + Cameo integration |
| Affordable MBSE starting point | Enterprise Architect or Capella (open source) |
| Simulate model behaviors (parametric) | Cameo + Simulink or Modelica integration |
| Model-to-code generation | Rhapsody (SW intensive) |
| PLM + MBSE integrated (Siemens shop) | Teamcenter + Capital/MBSE |
| When is MBSE not worth it? | Simple systems, short lifecycle, small team (<5 engineers) |

---

## Common Confusion Points

**MBSE is a methodology, not a tool**: Buying Cameo does not give you MBSE. MBSE requires process change — how SE work is done. Many organizations buy the tool, create diagrams, and continue with documents. That is not MBSE. The model must BE the design data, not illustrate it.

**SysML model ≠ software code model**: A SysML system model describes physical systems, functions, and requirements. It is NOT a software architecture model (though it can contain one). Confusing SysML with UML used for software design misses the point of each.

**MBSE does not eliminate documents**: Contracts, certification records, customer deliverables are documents. MBSE means those documents are generated from the model rather than maintained separately. The document still exists; it just doesn't have its own data — it's a view.

**Digital twin ≠ CAD model**: A CAD model is static geometry. A digital twin is dynamic — it contains the current state of the physical system, updated by real sensor data. A CAD model of a turbine blade is not a digital twin. A model updated with vibration, temperature, and fatigue cycle data from the flying engine is.

**Model fidelity must match purpose**: A SysML model built for system architecture analysis does not need to capture every screw and connector. Over-detailing in MBSE is a common failure mode — teams spend months modeling detail that adds no value. Define the model's purpose and stop at the appropriate level of abstraction.
