# Systems Engineering — Landscape and Taxonomy

## The Big Picture

Systems engineering (SE) is the interdisciplinary field that orchestrates the design, integration, and management of complex engineered systems over their entire lifecycle. It exists because no single engineering discipline can own the interactions between disciplines — and those interactions are where systems fail.

```
WHY SYSTEMS ENGINEERING EXISTS
──────────────────────────────────────────────────────────────────
Simple product:    One discipline → design → build → done
  One engineer can hold the whole thing in their head.

Complex system:    Multiple disciplines, emergent behaviors,
                   interfaces between subsystems, long lifecycle.

  ┌───────────────────────────────────────────────────────────────┐
  │                 Aircraft example                               │
  │  ┌───────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   │
  │  │Structures │ │Avionics  │ │Propulsion│ │Flight Control│   │
  │  └─────┬─────┘ └────┬─────┘ └─────┬────┘ └──────┬───────┘   │
  │        │            │             │              │            │
  │        └────────────┴─────────────┴──────────────┘           │
  │                              │                                │
  │                     INTERFACES                                │
  │             (where failures actually happen)                  │
  │        avionics weight → structural load budget               │
  │        fuel system → propulsion + structures                  │
  │        EMP → electronics → flight control stability           │
  └───────────────────────────────────────────────────────────────┘

  SE manages the interfaces that no single discipline owns.
```

**Bridge to software**: Systems engineering is software architecture's ancestor. Architecture decision records (ADRs), interface specifications, requirements traceability, V-model testing — all have direct software equivalents. The tools differ but the intellectual framework is the same. SEI (Software Engineering Institute at Carnegie Mellon) explicitly derives software architecture from SE principles.

---

## The Systems Engineering Taxonomy

```
SYSTEMS ENGINEERING KNOWLEDGE AREAS (INCOSE Systems Engineering Handbook)
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  PROCESS                                                         │
│  Lifecycle models (waterfall, vee, spiral, agile hybrid)        │
│  Technical processes (requirements, architecture, design, V&V)  │
│  Project processes (planning, risk, configuration management)   │
├─────────────────────────────────────────────────────────────────┤
│  METHODS                                                         │
│  Requirements engineering (stakeholder analysis, elicitation)  │
│  Functional analysis / functional decomposition                 │
│  Trade studies (Pugh matrix, AHP, MCDM)                        │
│  FMEA / FTA / reliability engineering                           │
│  Interface management (ICD, ICDs, IMS)                         │
│  Verification and validation (V&V) planning                     │
├─────────────────────────────────────────────────────────────────┤
│  TOOLS                                                           │
│  MBSE (Model-Based SE) — SysML, Cameo, Rhapsody                 │
│  Simulation — MATLAB/Simulink, AMESim                           │
│  Requirements management — DOORS, Jama, Polarion               │
│  PLM — Windchill, Teamcenter, Enovia                            │
│  SE-specific: SEAM, Vitech CORE, IBM Rational                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Domains Where SE is Practiced

```
SE DOMAIN MAP
──────────────────────────────────────────────────────────────────
DEFENSE / AEROSPACE         Most rigorous SE practice
  Aircraft, spacecraft      Mandated by MIL-STD-499, NASA-STD-7009
  Missiles, satellites      Long lifecycle, high cost of failure
  Naval systems             DO-178C (avionics SW), MIL-SPEC throughout

CIVIL / CRITICAL INFRA      SE growing, not always called "SE"
  Transportation systems    Railway: CENELEC 50128, NFPA 130
  Power grids               IEEE Std 1220, energy systems
  Large construction        Systems integration across contractors

COMMERCIAL TECH             SE principles, Agile vocabulary
  Automotive                ISO 26262 (functional safety), V-model
  Medical devices           IEC 62304 (software), IEC 60601
  Consumer electronics      Condensed SE (time-to-market pressure)

SOFTWARE / IT               SE principles well-integrated
  Enterprise systems        TOGAF, DoDAF, ArchiMate frameworks
  Mission-critical SW       DO-178C, IEC 61508 for safety-critical
  Cloud platforms           SRE (Site Reliability Engineering)
                            = operational SE for software systems
```

---

## Systems Engineering Standards Landscape

| Standard | Issuer | Scope |
|----------|--------|-------|
| ISO 15288 | ISO/IEC | System lifecycle processes — generic |
| ISO 12207 | ISO/IEC | Software lifecycle processes |
| INCOSE SE Handbook | INCOSE | SE best practices guide |
| MIL-STD-499B (draft) | DoD | Systems engineering requirements for defense |
| NASA-STD-7009 | NASA | Models, simulations, and digital twins |
| DO-178C | RTCA / EUROCAE | Aviation software certification |
| ARP4754A | SAE | Aircraft systems development process |
| ISO 26262 | ISO | Road vehicles functional safety |
| IEC 61508 | IEC | Functional safety of E/E/PE systems |
| IEEE Std 1220 | IEEE | Application and management of SE process |

---

## Key Concepts

### System vs Product

```
PRODUCT:   Can be fully specified by one discipline.
           A gear, a sensor, a PCB.

SUBSYSTEM: Collection of components with unified function.
           The fuel pump assembly, the landing gear actuator.

SYSTEM:    Multiple subsystems + their interactions.
           The aircraft, the satellite, the power grid.
           Properties emerge from interactions, not parts.

SYSTEM OF SYSTEMS (SoS): Multiple independent systems that
  operate together for a common mission.
  Air Traffic Control: aircraft + radar + comm + navigation
  Smart city: transportation + energy + communications + emergency services
```

### Emergent Properties

```
EMERGENCE: properties of a system not present in any component
──────────────────────────────────────────────────────────────────
Simple emergence:      predictable from component properties
  System weight = sum of component weights (no emergence)

Complex emergence:     unpredictable from components alone
  Software reliability: depends on interactions, not just code quality
  Traffic jam: emerges from individual driver behavior
  Aircraft flutter: aerodynamic + structural interaction instability

SE must manage emergent behavior:
  Identify emergent properties early (hazard analysis)
  Model interactions (simulation, SysML)
  Test at system level (not just unit/subsystem)
```

---

## The SE Lifecycle

```
GENERIC SYSTEMS LIFECYCLE
──────────────────────────────────────────────────────────────────
Concept        → Feasibility, market need, mission analysis
   │               "What problem are we solving?"
   ▼
Development    → Requirements, design, build, V&V
   │               "What does it do and how do we prove it?"
   ▼
Production     → Manufacturing, quality, delivery
   │               "Replicate it reliably"
   ▼
Utilization    → Operations, support, maintenance
   │               "Keep it running"
   ▼
Support        → Training, spares, updates, field service
   │               "Sustain it economically"
   ▼
Retirement     → Decommission, disposal, transition
               "End it safely and responsibly"

SE has formal processes for EACH phase.
Requirements change across phases — requirements in Concept are not
the same detail level as requirements in Development.
```

---

## Directory Guide

| File | Content |
|------|---------|
| 01-SE-PROCESS.md | Lifecycle models, ISO 15288, process areas |
| 02-REQUIREMENTS.md | Requirements engineering, DOORS, traceability |
| 03-ARCHITECTURE.md | System architecture, MBSA, trade studies |
| 04-V-MODEL.md | V-model, verification vs validation |
| 05-SYSML.md | SysML diagram types, notation, tools |
| 06-FMEA-RELIABILITY.md | FMEA, FTA, reliability allocation |
| 07-INTERFACE-MANAGEMENT.md | ICDs, interface control, integration |
| 08-MBSE.md | Model-Based SE, tools, workflows |
| 09-CASE-STUDIES.md | Mars Climate Orbiter, Boeing 737 MAX, Therac-25 |

---

## Decision Cheat Sheet

| SE Challenge | Relevant Practice |
|--------------|------------------|
| How do I capture what the system must do? | Requirements engineering (SRS, use cases) |
| How do I design the high-level structure? | System architecture + trade studies |
| How do I prove it works? | V-model: verification and validation plan |
| How do I find failure modes early? | FMEA / FTA / hazard analysis |
| How do I manage subsystem interfaces? | ICDs + interface management |
| How do I trace requirements to tests? | Requirements traceability matrix |
| How do I manage complexity with models? | MBSE with SysML |
| How do I coordinate across disciplines? | Systems integration process |

---

## Common Confusion Points

**Systems engineering vs software engineering**: SE is the parent discipline. Software engineering is a sub-discipline. SE coordinates ALL technical work (mechanical, electrical, software, human factors, etc.) while each sub-discipline has its own engineering practices. For large systems, the systems engineer is the integrator, not the implementer.

**Verification vs validation (always confused)**: Verification = "Did we build it right?" (Does the system meet the specification?) Validation = "Did we build the right thing?" (Does the system meet stakeholder needs?) You can verify every requirement and still have a wrong system (requirements were wrong). The V-model handles both.

**Requirements vs design**: Requirements state WHAT the system must do (behavior, constraints, performance). Design states HOW it will do it (architecture, mechanisms, implementation). A requirement that specifies implementation is a design decision masquerading as a requirement — it prematurely constrains design space.

**INCOSE vs ISO 15288**: INCOSE (International Council on Systems Engineering) publishes a handbook that is a best practices guide. ISO 15288 is a formal standard defining system lifecycle process categories. They align but serve different purposes — ISO 15288 is the "what" to certify against, INCOSE handbook is the "how."
