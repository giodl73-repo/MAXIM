# The V-Model and Verification/Validation

## The Big Picture

The V-model visualizes the relationship between development activities (left side: decompose) and integration/verification activities (right side: integrate and verify). Each level on the left side has a corresponding level on the right — ensuring every design decision is tested at the appropriate level.

```
THE VEE MODEL (V-Model)
──────────────────────────────────────────────────────────────────
Decompose ◄────────────────────────────────────────► Integrate

Concept                                              System
Operations  ──────────────────────────────────────► Acceptance
                                                     Test
    │                                                │
System          ────────────────────────────────► System
Requirements                                     Verification
Spec (SRS)          System Design                Test
    │                   Review (SDR)             │
    │                                            │
Subsystem         ──────────────────────────► Subsystem
Requirements                                 Integration
(Allocated                                   Test
 Baseline)     PDR / CDR                     │
    │                                        │
Component         ──────────────────────► Component
Spec /                                    Verification
Design-to                                 Test
    │                                    │
    └──────────────── BUILD ─────────────┘
                  (bottom of the V)
                  Code / Fabricate

Left side:    Decompose and specify
Right side:   Integrate and verify
Horizontal:   Each spec is verified by corresponding test
```

---

## Verification vs Validation

The most commonly confused terms in SE. They are not interchangeable.

```
VERIFICATION                          VALIDATION
──────────────────────────────────    ──────────────────────────────────
"Did we BUILD IT RIGHT?"              "Did we build THE RIGHT THING?"

Are we meeting the specification?     Are we meeting stakeholder needs?

Measured against:                     Measured against:
  The written requirement               The original operational need
                                        (CONOPS, stakeholder intent)

When:                                 When:
  Throughout development (each         After system is fully integrated
  design review, unit tests)           Acceptance testing by customer

Who:                                  Who:
  Developer / independent test team    Customer / end user / certifier

Example:                              Example:
  Spec says "range ≥ 6,000 nmi"        Did the aircraft fulfill the
  Test proves 6,340 nmi achieved       actual mission it was built for?
  → Verified                           → Validated

You CAN verify every requirement and still fail validation:
  The requirements were wrong / incomplete
  The customer didn't know what they needed
  The operational environment was different from assumed
```

---

## Verification Methods (IATAD)

Each requirement must specify a verification method. Four standard methods:

```
VERIFICATION METHODS
──────────────────────────────────────────────────────────────────
I — Inspection
  Visual examination of a product, drawing, document
  No operation or measurement
  "Verify that the unit has a serial number label"
  "Verify that protective coating covers all fasteners"
  Lowest cost, but limited scope

A — Analysis
  Mathematical / logical computation from known data
  No physical testing required
  "Calculate structure stress under max load via FEA"
  "Verify timing margin by analysis of timing diagrams"
  Good for: physics-based requirements, early verification

T — Test
  Operate the item under controlled conditions, measure output
  "Apply 50kg load, measure deflection < 2mm"
  "Transmit 1000 frames, verify frame error rate < 10⁻⁶"
  Most rigorous, most expensive, most credible

D — Demonstration
  Show function operates correctly, without precise measurement
  "Demonstrate that door locks when powered off"
  "Demonstrate that manual override disables autopilot"
  Between inspection and test — functional but not measured

Selection logic:
  Safety-critical: Test (or Analysis where test is impossible)
  Performance-critical: Test
  Physical attributes: Inspection
  Performance via physics: Analysis (validated model)
  Functional behavior: Demonstration or Test
```

---

## Verification and Validation Planning

```
VERIFICATION AND VALIDATION (V&V) PLAN CONTENTS
──────────────────────────────────────────────────────────────────
System Test Plan:
  Test philosophy and approach
  Test levels (unit / integration / system / acceptance)
  Test environment description
  Test tooling and facilities
  Schedule and resources
  Pass/fail criteria
  Regression testing approach

Per-requirement:
  Verification method (I/A/T/D)
  Verification level (component / subsystem / system)
  Test procedure reference
  Success criteria (measurable)
  Test environment (lab / hardware-in-loop / operational)

Requirements Verification Matrix (RVM):
  All requirements × verification methods × test references
  Traceability to test results after test completion
```

---

## Test Levels in the V-Model

### Unit / Component Testing

```
UNIT TEST (bottom of V)
──────────────────────────────────────────────────────────────────
Physical: individual component tested in isolation
  Mechanical: stress test on a single bracket
  Electrical: PCB functional test on bench
  Software: unit tests for individual functions/classes

Purpose:
  Verify component meets its specification
  Identify defects at lowest (cheapest) level
  Before integration (not after — late defect discovery expensive)

Hardware unit tests:
  Environmental (vibration, thermal, humidity)
  Functional (inputs → expected outputs)
  Limits testing (at boundary conditions)
  Destructive testing for design margins (test to failure)

Software unit tests:
  Bridge: same as software unit tests you know
  White box: path coverage, branch coverage
  Black box: boundary value analysis, equivalence partitions
  DO-178C (aviation software) mandates coverage levels:
    Level A (catastrophic failure): MC/DC coverage
    Level B (hazardous): decision coverage
    Level C (major): statement coverage
```

### Integration Testing

```
INTEGRATION TESTING
──────────────────────────────────────────────────────────────────
Purpose: verify interfaces between components work as designed

Strategies:
  Big bang:     integrate all at once → hard to isolate failures
  Top-down:     integrate from top level, stub lower
  Bottom-up:    integrate from bottom, driver to exercise
  Incremental:  integrate one component at a time

HW/SW Integration (HSI):
  Most complex phase — hardware and software first meet
  Interface bugs surface here (timing, protocol, electrical)
  Requires: hardware ready, software loadable
  Environment: integration bench, not full system

Subsystem Integration Test (SIT):
  All components of a subsystem integrated and tested
  Verify subsystem-level requirements
  Interfaces to other subsystems via simulators/stubs
  Hardware: actual units (or EM — engineering model)
```

### System-Level Testing

```
SYSTEM LEVEL TEST
──────────────────────────────────────────────────────────────────
Full system integrated, tested against system requirements (SRS)
All subsystems present (or fully simulated)

Test types at system level:
  Functional testing:      Do all functions work?
  Performance testing:     Are performance requirements met?
  Environmental:           Does system work in its environment?
  Stress testing:          Behavior at limits and beyond (margins)
  Failure mode testing:    Does system handle failures gracefully?
  Regression testing:      After each change, verify nothing broke
  Long-duration:           Hours/days of operation, reliability demo

Environmental Test Sequence (for hardware):
  1. Structural qualification (vibration, shock, acoustic)
  2. Thermal cycling / thermal vacuum (spacecraft)
  3. EMC (Electromagnetic Compatibility) testing
  4. Humidity / salt fog (for maritime/outdoor)
  5. Combined environment (simultaneous: temp + vibration)

Test approach for safety-critical systems:
  Hardware-In-the-Loop (HIL): real hardware + simulated environment
  Software-In-the-Loop (SIL): software + simulated hardware
  Iron Bird: full aircraft system test without airframe
  Systems Integration Lab (SIL): full system, simulated scenario
```

### Acceptance Testing

```
ACCEPTANCE TESTING
──────────────────────────────────────────────────────────────────
Customer accepts (takes ownership of) the system
Verifies system meets contractual requirements
Demonstrates validation against operational scenarios

Types:
  FAT (Factory Acceptance Test): at manufacturer facility
  SAT (Site Acceptance Test): at customer site, after installation
  OAT (Operational Acceptance Test): with real users in real environment

Acceptance criteria:
  All level A requirements: must pass Test
  Mandatory level B requirements: Demonstration at minimum
  Performance requirements: quantitative pass/fail
  Defect thresholds: how many open defects allowed at acceptance?

Delta qualification:
  Existing qualified system with modifications
  Only verify requirements affected by modifications
  Saves cost vs full re-qualification
```

---

## Test Maturity Levels

Analogy to code review maturity — test processes have their own maturity:

```
TEST PROCESS MATURITY
──────────────────────────────────────────────────────────────────
Level 0: Testing = debugging
  No plan, test-as-you-build
  Common in startups, prototypes

Level 1: Ad hoc testing
  Test procedures exist but informal
  Tests written after code/design

Level 2: Managed testing
  Test plans written before design complete
  Traceability to requirements exists

Level 3: Defined testing
  Standard process, controlled
  Formal test documentation, reviews
  Pass/fail criteria defined upfront

Level 4: Measured testing
  Metrics: coverage, defect escape rate
  Independent test team

Level 5: Optimized testing
  Continuous improvement of test process
  Risk-based test selection
  Test automation strategy
```

---

## Qualification vs Certification

```
QUALIFICATION vs CERTIFICATION
──────────────────────────────────────────────────────────────────
Qualification:
  Internal process to show design meets specification
  Qualification test article (not production hardware)
  Tests to limits → typically 3 dB over design requirement (margin)
  "This design is qualified for this environment"

Certification:
  External regulatory body approves system for use
  FAA certification for aircraft
  FCC certification for RF devices
  FDA 510(k) or PMA for medical devices
  CE marking for EU market

Relationship:
  Qualification → provides evidence for certification
  Certification = regulator reviews qualification evidence + tests

Type Certificate (TC) vs Production Certificate (PC):
  TC: proves the design is safe/airworthy (FAA)
  PC: proves manufacturer can consistently produce to the TC
  Supplemental Type Certificate (STC): modification to existing TC
```

---

## Independent Verification and Validation (IV&V)

```
IV&V
──────────────────────────────────────────────────────────────────
IV&V = Verification and Validation performed by an independent party
  not the developer, not the customer — a third party

Purpose:
  Fresh eyes — developer bias toward "it works because I built it"
  Catch systematic errors that internal team cannot see
  Regulatory requirement for safety-critical systems

Mandatory for:
  NASA safety-critical software (NASA NPR 7150.2)
  Nuclear power plant I&C systems
  Flight control software (DO-178C Level A)
  Medical device software (FDA, IEC 62304)

IV&V scope:
  Review design documentation for correctness
  Execute test procedures independently
  Analyze test results
  Report findings directly to customer / regulator
  Not to developer (independent reporting channel)
```

---

## Decision Cheat Sheet

| V-Model Question | Answer |
|------------------|--------|
| What tests correspond to system requirements? | System Verification Test |
| What tests correspond to stakeholder needs? | Acceptance Test / Validation |
| How do I verify a weight requirement? | Test (weigh the hardware) |
| How do I verify a structural load requirement? | Analysis (FEA) or Test |
| How do I verify a software timing requirement? | Analysis or Test |
| How do I show the system works as a whole? | System-level functional test |
| What is required before acceptance? | All level-A requirements: Pass |
| When do I need IV&V? | Safety-critical, regulatory mandate |

---

## Common Confusion Points

**V-model vs waterfall**: Both are left-side (design/develop) followed by right-side (test/verify), but the V-model explicitly encodes the linkage between each design level and its corresponding test level. Waterfall doesn't visually show this — test is just "a phase at the end." The V-model is waterfall made honest about what testing must do.

**Verification at each level**: A common mistake is to only test at system level and assume it covers everything. System tests can miss component-level behavior that only manifests in isolation. Unit testing at each level is cheaper and finds more bugs per dollar than system-level-only testing. This is the same conclusion reached in software testing (test pyramid).

**Environment test sequence matters**: You cannot run EMC tests first and structural tests second for space hardware — vibration can cause structural changes that affect EMC performance. Standard qualification test sequences (e.g., GSFC-STD-7000 for NASA) define the mandated order. Deviating requires formal rationale.

**Margins and safety factors**: Requirements are verified at nominal values. Qualification tests are run at 3dB (factor of ~1.4) over requirements to demonstrate margin. Safety factors for structural analysis (1.5× limit load = ultimate load) serve the same purpose. Margin is not waste — it covers model uncertainty, manufacturing variation, and aging.

**Regression testing is mandatory, not optional**: After any change to hardware or software, regression testing verifies that the change didn't break something else. This is obvious in software development (you know it well from VSTS days). In hardware-dominated SE programs, it is equally true but often skipped due to cost — leading to late-program surprises during final acceptance.
