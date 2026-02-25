# Requirements Engineering and Management

## The Big Picture

Requirements engineering (RE) defines what a system must do and the constraints it must satisfy. It is the highest-leverage SE activity — errors found in requirements are 100× cheaper to fix than errors found after deployment. It is also where most systems fail: not because of bad engineering, but because the wrong thing was built.

```
REQUIREMENTS HIERARCHY
──────────────────────────────────────────────────────────────────
Stakeholder Needs (informal)
  "We need an aircraft that can fly 6,000 miles nonstop"
       │
       ▼ elicitation + analysis + formalization
System Requirements (SRS / top-level specs)
  "The vehicle shall achieve a minimum range of 6,000 nmi
   with standard fuel load at cruise altitude."
       │
       ▼ allocation to subsystems
Subsystem Requirements (allocated baseline)
  Airframe: structural load requirements
  Propulsion: thrust, fuel consumption envelope
  Fuel system: capacity, flow rate
       │
       ▼ further decomposition
Component Requirements (design specifications)
  Engine: thrust-specific fuel consumption curve
  Tank: structural loads, material compatibility
       │
       ▼
Design solution
       │
       ▼ verification (does it meet requirements?)
Test Results / Analysis
       │
       ▼ validation (does it meet original needs?)
Customer Acceptance
```

---

## Requirement Types

```
REQUIREMENT TAXONOMY
──────────────────────────────────────────────────────────────────
FUNCTIONAL REQUIREMENTS
  What the system SHALL DO
  "The system shall transmit data at ≥ 100 Mbps"
  "The system shall detect targets at ≥ 50 km range"
  Expressed in terms of behavior, capability, function

NON-FUNCTIONAL REQUIREMENTS (QoS, Quality Attributes)
  How the system shall perform its functions
  Performance: "response time < 200ms at 95th percentile"
  Reliability: "MTBF > 10,000 hours"
  Availability: "system availability > 99.9%"
  Maintainability: "MTTR < 4 hours"
  Interoperability: "shall interface with MIL-STD-1553 bus"
  Security: "shall comply with NIST SP 800-53 Level 2"
  Safety: "shall not emit radiation exceeding FCC Part 15"

INTERFACE REQUIREMENTS
  System boundaries with external entities
  "The system shall accept GPS input via RS-422 at 9600 baud"
  "The system shall interface with legacy ACARS protocol"

DESIGN CONSTRAINTS
  Restrictions on how the system can be designed
  "The system shall use components on the QPL (Qualified Parts List)"
  "The system shall operate on 28VDC aircraft bus"
  "The total weight shall not exceed 45 kg"

DERIVED REQUIREMENTS
  Not from stakeholder — derived from design decisions
  If you decide to use a microprocessor, it derives power requirements
  Must be flagged — no stakeholder explicitly requested them
  Often the source of scope creep
```

---

## Writing Good Requirements

### The SMART Criteria for Requirements

```
REQUIREMENT QUALITY ATTRIBUTES
──────────────────────────────────────────────────────────────────
Singular:       One requirement per statement
  Bad:  "The system shall detect and track targets"
  Good: "The system shall detect targets..." (separate req)
        "The system shall track detected targets..." (separate req)

Verifiable:     Can be tested or analyzed
  Bad:  "The system shall be reliable"
  Good: "The system shall achieve MTBF > 5,000 hours in
         operational environment (IEC 60068 conditions)"

Unambiguous:    One interpretation only
  Bad:  "The system shall have fast response"
  Good: "The system response time shall be < 500ms for
         95% of transactions under nominal load"

Achievable:     Technically feasible within constraints
  Check against state of practice, physics, budget

Traceable:      Unique identifier, traces to parent requirement
  REQ-SYS-0042: "shall maintain ≥ 3g maneuver capability"
  Parent: STAKE-007 (combat aircraft need)

Necessary:      Remove it → gap in stakeholder need
  Gold-plating = requirements that no stakeholder actually needs
```

### Common Requirement Anti-Patterns

```
ANTI-PATTERNS (avoid)
──────────────────────────────────────────────────────────────────
"All" / "every":     "The system shall handle all inputs"
  → What inputs? Finite or infinite? Specify.

"Minimize/maximize": "The system shall minimize weight"
  → Unmeasurable. Set a threshold: "weight ≤ 50 kg"

"User-friendly":     "The interface shall be user-friendly"
  → Unmeasurable. Use usability metrics: task time, error rate.

"If possible":       "The system shall achieve 100 km range if possible"
  → Not a requirement. Either it must or it doesn't.

Passive voice:       "Data shall be processed within 2 seconds"
  → Who processes? "The server shall process..." specifies the subject.

Rationale embedded:  "The system shall use AES-256 because it is secure"
  → Requirements state what, not why. Rationale goes in a separate field.

Multiple conditions: "The system shall detect targets > 50 km in day
                      and > 20 km in night with 90% probability"
  → Two requirements. Separate them.
```

---

## Requirements Elicitation

```
ELICITATION TECHNIQUES
──────────────────────────────────────────────────────────────────
Stakeholder interviews
  One-on-one with each stakeholder class
  Open-ended questions first, then specifics
  Good for: tacit knowledge, constraints, background

Workshops (JAD — Joint Application Design)
  Facilitated group session with key stakeholders
  Rapid consensus building, conflict surfacing
  Risk: groupthink, dominant personalities

Observation (Ethnographic study)
  Watch operators using current system or workaround
  Reveals what users actually do vs what they say they do
  Critical for: workflow automation, ergonomics

Document analysis
  Review existing specs, contracts, regulations
  Mandatory for: regulated industries (FAA, FDA), gov't contracts

Prototyping
  Build mock interface, present to users for feedback
  Rapidly surfaces ambiguity and missing requirements

Use cases / user stories
  "As a [role], I want [capability] so that [benefit]"
  Good for: functional requirements, workflow
  Weak for: non-functional requirements, constraints

Viewpoint analysis (VOSE — Viewpoints-Oriented Systems Engineering)
  Different stakeholder classes have different views of same system
  Operator: usability, reliability
  Maintainer: accessibility, spare parts
  Safety officer: hazard avoidance
  Integrate all viewpoints → complete requirements
```

---

## Requirements Traceability

```
REQUIREMENTS TRACEABILITY MATRIX (RTM)
──────────────────────────────────────────────────────────────────
RTM links:
  Stakeholder need → System requirement → Subsystem requirement
  System requirement → Verification method → Test result

Example RTM structure:
  REQ ID  | Description         | Parent    | Subsystem | V Method | Test ID
  ─────────────────────────────────────────────────────────────────────────
  SYS-001 | Range ≥ 6000 nmi    | STAKE-07  | PROP-012  | Analysis | N/A
  SYS-002 | Speed ≥ 200 kt      | STAKE-08  | PROP-013  | Test     | T-0043
  SYS-003 | Payload ≥ 5000 lb   | STAKE-09  | STRUC-004 | Test     | T-0045

Bidirectional traceability:
  Forward: Stake need → requirement → design → test
  Backward: test → requirement → need
  Gap detection: requirement with no parent = gold-plating
                 need with no requirement = missing coverage

Tools: IBM DOORS (industry standard), Jama Connect,
       Polarion ALM, Codebeamer, JIRA (for software-centric)
```

---

## Requirements Management Tools

### IBM DOORS (Telelogic DOORS)

```
DOORS ARCHITECTURE
──────────────────────────────────────────────────────────────────
Database of requirement objects (attributes + text)
Modules = documents (each requirement = one row)
Links = traceability connections between modules
Attributes = metadata per requirement (status, verification method, etc.)
Views = filtered/sorted subset of module
Baselines = frozen snapshots at review milestones

DOORS structure:
  Project
  ├── Stakeholder Needs Module
  ├── System Requirements Module (SRS)
  │   └── Links to Stakeholder Needs
  ├── Subsystem A Requirements Module
  │   └── Links to System Requirements
  ├── Test Cases Module
  │   └── Links to System Requirements
  └── Results Module
      └── Links to Test Cases

DOORS XT / DOORS Next: web-based successor, REST API,
more modern UX, same data model concept.
```

---

## Stakeholder Analysis

```
STAKEHOLDER ANALYSIS FRAMEWORK
──────────────────────────────────────────────────────────────────
WHO are the stakeholders?
  Users: who operates the system daily
  Buyers: who funds/procures it
  Maintainers: who keeps it running
  Operators: direct interface
  Affected parties: neighbors, regulators, public
  Standards bodies: mandatory compliance

STAKEHOLDER CLASSIFICATION (Power-Interest grid):
                      Interest
                   Low        High
  Power High  │ Keep      │  Manage
              │ Satisfied │  Closely
  ────────────┼───────────┼──────────
  Power Low   │ Monitor   │  Keep
              │           │  Informed

CONFLICT RESOLUTION between stakeholder requirements:
  Negotiate: find compromise (often with performance tradeoff)
  Prioritize: stakeholders vote, highest priority wins
  Trade study: formal comparison of alternatives
  Escalate: to program manager / sponsor if unresolvable
```

---

## CONOPS (Concept of Operations)

```
CONOPS DOCUMENT
──────────────────────────────────────────────────────────────────
Describes how the system will be used in its operational environment
BEFORE requirements are written.

Contents:
  System purpose and mission overview
  Operational environment description
  System scenarios (day in the life, edge cases)
  User roles and their interactions
  Operational constraints (time, geography, resources)
  Expected operational performance criteria

Purpose:
  Validates understanding of problem before solution
  Surfaces operational requirements that stakeholders can't articulate
  Basis for acceptance testing (did we achieve the CONOPS scenarios?)
  Prevents "perfect spec for wrong problem"

Format: DoD has ConOps template (ANSI/AIAA G-043)
  Most programs use a tailored version
```

---

## Decision Cheat Sheet

| Need | Approach |
|------|----------|
| Understand what stakeholders actually need | Interviews + observation + workshops |
| Document system requirements formally | SRS (System Requirements Specification) |
| Link needs to requirements to tests | Requirements Traceability Matrix (RTM) |
| Manage requirements in large program | IBM DOORS or equivalent RM tool |
| Detect missing requirements coverage | Forward traceability gaps in RTM |
| Find gold-plating (no stakeholder origin) | Backward traceability — no parent requirement |
| Describe how the system will be used | CONOPS document |
| Resolve stakeholder conflicts | Power-interest grid + formal trade study |

---

## Common Confusion Points

**Requirements vs needs vs design**: Needs are informal (stakeholder wishes). Requirements are formal, verifiable system obligations. Design is how you meet requirements. Conflating them is the most common RE mistake: a requirement that says "the system shall use PostgreSQL" is actually a design decision, not a requirement.

**Shall vs should vs will**: In requirements, "shall" = mandatory (must be verified). "Should" = desired but not mandatory. "Will" = project intent or fact about the environment. Many organizations ban "should" in requirements — it's ambiguous whether it's mandatory.

**Derived requirements must be traced**: When a design decision creates a new requirement (you chose a 28VDC power supply, which now constrains all electronics to 28VDC input), that derived requirement must be documented and tracked. Undocumented derived requirements are a major source of unexpected failures during integration.

**Verification method must be specified at requirements time**: Each requirement needs a verification method: Analysis (calculation), Inspection (visual check), Demonstration (functional test), Test (measurement). If you cannot identify how you'll verify a requirement, the requirement is probably not verifiable — fix it before CDR.

**TBD / TBS in requirements is a risk**: "To Be Determined" or "To Be Specified" values in requirements are open risks. Formal SE programs track every TBD/TBS as a risk item with an owner and closure date. More than ~5% TBD at CDR is typically a flag for program risk.
