# Systems Engineering Process and Lifecycle

## The Big Picture

SE process is the structured sequence of activities that transforms stakeholder needs into a verified, validated system and sustains it through its lifecycle. ISO 15288 defines the canonical framework; it is process-agnostic (works with waterfall, agile, iterative).

```
ISO 15288 PROCESS GROUPS
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  AGREEMENT PROCESSES                                             │
│  Acquisition ·· Supply                                          │
│  (customer-supplier relationship management)                    │
├─────────────────────────────────────────────────────────────────┤
│  ORGANIZATIONAL PROJECT-ENABLING PROCESSES                       │
│  Life cycle model management ·· Infrastructure management       │
│  Portfolio management ·· Human resource management             │
│  Quality management ·· Knowledge management                    │
├─────────────────────────────────────────────────────────────────┤
│  PROJECT PROCESSES                                               │
│  Project planning ·· Project assessment and control             │
│  Decision management ·· Risk management                         │
│  Configuration management ·· Information management            │
│  Measurement ·· Quality assurance                               │
├─────────────────────────────────────────────────────────────────┤
│  TECHNICAL PROCESSES  ◄── The core SE work                      │
│  Stakeholder needs and requirements definition                  │
│  System requirements definition                                 │
│  Architecture definition ·· Design definition                   │
│  System analysis ·· Implementation                              │
│  Integration ·· Verification ·· Transition ·· Validation       │
│  Operation ·· Maintenance ·· Disposal                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technical Processes in Detail

### The Logical Flow

```
TECHNICAL PROCESS FLOW
──────────────────────────────────────────────────────────────────
Stakeholder needs  →  System requirements  →  Architecture
     (what they        (what the system         (how the system
      actually want)    must do — specified)      is structured)
           │                   │                       │
           ▼                   ▼                       ▼
    Stakeholder       System Requirements        Architecture
    Requirements      Specification (SRS)        Description
    Review (SRR)     or Allocated Baseline      Document (ADD)
                                                 / MBSE Model

Architecture  →  Design definition  →  Implementation
  (system level)  (subsystem level)     (build/code)
       │                 │                    │
       ▼                 ▼                    ▼
  System Design    Detailed Design     Fabricated
  Review (SDR)     Review (DDR)        Components
                   Preliminary &
                   Critical Design
                   Reviews (PDR/CDR)

Implementation  →  Integration  →  Verification  →  Validation
  (components)     (combine)        (meets spec)     (meets need)
       │               │                 │                │
       ▼               ▼                 ▼                ▼
  Unit test        Integration      Test reports      Customer
                   testing          T&E results       acceptance
```

---

## Lifecycle Models

### Sequential (Waterfall) Model

```
WATERFALL / SEQUENTIAL MODEL
──────────────────────────────────────────────────────────────────
Concept → Requirements → Architecture → Design → Build → Test → Deploy

  ┌──────────┐
  │ Concept  │
  └────┬─────┘
       │ Requirements Review
  ┌────▼─────┐
  │   Req.   │
  └────┬─────┘
       │ System Design Review
  ┌────▼─────┐
  │  Arch.   │
  └────┬─────┘
       │ Preliminary Design Review (PDR)
  ┌────▼─────┐
  │  Design  │
  └────┬─────┘
       │ Critical Design Review (CDR)
  ┌────▼─────┐
  │  Build   │
  └────┬─────┘
       │ Test Readiness Review (TRR)
  ┌────▼─────┐
  │   Test   │
  └────┬─────┘
       │ Operational Readiness Review (ORR)
  ┌────▼─────┐
  │ Operate  │
  └──────────┘

Advantages: Clear phase gates, contractual milestones, auditable
Disadvantages: Requirements discovery late, expensive late changes
When: Defense/government programs, cost-plus contracts
```

### The Vee Model

The Vee model shows that each design level has a corresponding verification/validation level — addressed in detail in 04-V-MODEL.md.

```
VEE MODEL OVERVIEW
──────────────────────────────────────────────────────────────────
Decompose ──────────────────────────────────────── Integrate/Verify
   │                                                        │
System         ┌──────────────────┐          System Acceptance
Requirements   │ System Level Req │         Test (validates needs)
   │           └────────┬─────────┘                │
Subsystem         │     │           Subsystem Integration
Requirements  ┌───▼─────▼───┐       Test (verifies subsystem req)
   │          │ Subsystem   │              │
Component    │   Req       │    Component Verification Test
Design       └──────┬───────┘           │
   │              │    │              Unit/Component Test
   └──────────────┘    └────────────────────────────────────┘
                           Build / Implement
                          (bottom of the Vee)
```

### Spiral Model (Boehm)

```
SPIRAL MODEL
──────────────────────────────────────────────────────────────────
Iterative development with explicit risk management each cycle.

         Determine objectives    Identify risks
                    \              /
              ────────────────────
             /                    \
    Plan next       Spiral        Evaluate alternatives
    iteration       Cycle         Risk mitigation
             \                    /
              ────────────────────
                    /              \
         Develop and test         Customer review

Each spiral = one iteration of planning → risk reduction → development → review
Appropriate for: large programs with significant technical risk
```

### Agile SE (SAFe / Agile + Systems Engineering)

```
AGILE SE INTEGRATION CHALLENGES
──────────────────────────────────────────────────────────────────
Pure Agile (software):
  Sprint-based, backlog, user stories
  Works well for: software, low physical coupling

SE challenge:
  Physical hardware has long lead times (not sprint-length)
  Safety certification requires documentation before build
  Interface control must be locked before parallel development
  Test campaigns are not 2-week sprints

Hybrid approaches:
  SAFe (Scaled Agile Framework) with SE discipline extensions
  "Lean SE": SE discipline applied lean/agile
  Agile at subsystem level, SE waterfall at system level
  "Incremental commitment" — define system-level requirements early,
  allow subsystem design flexibility

Key: requirements that define INTERFACES must be stable early.
     Requirements internal to a subsystem can be evolved.
```

---

## Design Reviews (Technical Reviews and Audits)

These review gates map directly to CI/CD pipeline gates: SRR = requirements approval gate, CDR = architecture review gate (no build without approved design), TRR = test-ready gate (won't deploy to staging without passing test suite), ORR = production release gate. The vocabulary differs but the pattern — mandatory quality gates with defined entry/exit criteria — is identical.

```
STANDARD SE REVIEW SEQUENCE
──────────────────────────────────────────────────────────────────
MCR    Mission Concept Review
       "Does the mission concept make sense?"
       Too early to have requirements, discuss concept viability

SRR    System Requirements Review
       "Are the system requirements complete and consistent?"
       Top-level requirements baseline established
       Exit criteria: requirements allocated to subsystems

SDR    System Design Review
       "Does the architecture meet the requirements?"
       Functional decomposition complete
       Major interfaces identified

PDR    Preliminary Design Review
       "Is the design approach sound and low risk?"
       Subsystem requirements baselined
       Design-to specifications issued
       Make/buy decisions complete
       Interface Control Documents (ICDs) drafted

CDR    Critical Design Review
       "Is the design complete enough to build from?"
       Detailed design drawings/models complete
       Analysis done (stress, thermal, EMC, etc.)
       ICDs approved
       Risk items resolved or have mitigation plans

TRR    Test Readiness Review
       "Are we ready to test?"
       Test plans, procedures approved
       Hardware/software ready for formal test

ORR    Operational Readiness Review
       "Are we ready to operate/deploy?"
       All tests complete, acceptance criteria met
       Support infrastructure in place
```

---

## Technical Performance Measures (TPMs)

```
TECHNICAL PERFORMANCE MEASURES
──────────────────────────────────────────────────────────────────
TPMs are the "vital signs" of a program's technical health.

Definition: Key system parameters tracked across development
  against a planned trajectory from current design estimate
  to final requirement.

Example TPMs:
  Vehicle empty weight vs. design estimate vs. requirement
  Radar detection range vs. requirement
  Software CPU margin vs. requirement
  Power consumption vs. budget

                      Requirement ──── (desired final value)
  T                  /
  P            Design
  M           estimate──────────────
  Value       trajectory
        │   /
        │  /  Actual estimate at each review
        │ /   (updated as design matures)
        │/
  ──────┴────────────────────────────► Program time
  Concept  PDR    CDR   Build  Test

  If actual trend diverges from planned → early warning signal
  Management action before late (expensive) discovery
```

---

## Configuration Management

```
CONFIGURATION MANAGEMENT (CM) IN SE
──────────────────────────────────────────────────────────────────
CM ensures consistency between design documentation and
as-built/as-tested hardware and software.

Three baselines (MIL-HDBK-61A):
  Functional Baseline:   System specifications (post-SRR)
                         "What the system must do"
  Allocated Baseline:    Subsystem specs, ICDs (post-PDR)
                         "What each subsystem must do"
  Product Baseline:      Detailed drawings, code (post-CDR)
                         "How it is built"

Change control after each baseline:
  Engineering Change Proposal (ECP) → formal review → approve/reject
  Deviation: one-time variance allowed before manufacture
  Waiver: acceptance of nonconformance after manufacture

Digital bridge: CM in SE = version control in software.
Functional baseline = API contract (public interface).
ECP process = PR review with gate keeper approval.
Product baseline = released artifact with version tag.
```

---

## Risk Management in SE

```
SE RISK MANAGEMENT PROCESS
──────────────────────────────────────────────────────────────────
Identify →  Analyze →  Plan →  Track →  Control

Risk characterization:
  Technical risk:    will the design work?
  Schedule risk:     will it be done in time?
  Cost risk:         will it stay in budget?

Risk rating = Likelihood × Consequence

         Consequence
         1    2    3    4    5
    ─────────────────────────────
  5 │  5   10   15   20   25
  4 │  4    8   12   16   20
  3 │  3    6    9   12   15
  2 │  2    4    6    8   10
  1 │  1    2    3    4    5

  >12 = High (mandatory mitigation plan)
  6-12 = Medium (watch list)
  <6  = Low (accept)

Risk handling strategies:
  Mitigate: reduce likelihood or consequence (testing, prototypes)
  Watch: monitor for growth without immediate action
  Accept: cost of mitigation > expected value of risk
  Transfer: to supplier, insurance
```

---

## Decision Cheat Sheet

| SE Question | Process |
|-------------|---------|
| Which lifecycle model for a DoD program? | Vee model (contractual milestones) |
| Which lifecycle for an Agile product company? | Iterative/spiral with SE gates at system boundaries |
| How do I track technical health during development? | TPMs at each design review |
| Who approves changes after CDR? | Change Control Board (CCB) via ECP process |
| What do I review at PDR vs CDR? | PDR: design approach sound. CDR: design complete to build from. |
| How do I prioritize risks? | Likelihood × Consequence risk matrix |

---

## Common Confusion Points

**ISO 15288 is a framework, not a prescription**: It defines process categories and their inputs/outputs. It does NOT prescribe a specific lifecycle model (waterfall, agile, spiral). You apply it to your chosen model.

**Review gates are not phases**: PDR and CDR are events (reviews), not phases. The design work happens before the review. The review decides if you can proceed. Confusing "we're in PDR" (a phase) with "we're holding PDR" (an event) is common in program management.

**CM is not just version control**: Configuration management in SE covers hardware, software, firmware, documentation, and the relationships between them. It includes physical hardware builds (effectivity — which serial number has which modification). Software CM is a subset.

**Technical risk ≠ programmatic risk**: Technical risk is "will it work?" Programmatic risk is "will it be done on time and on budget?" A technically sound design with a single-source supplier for a critical component has low technical risk but high supply chain/schedule risk. TPMs track technical risk; Earned Value Management (EVM) tracks programmatic risk.
