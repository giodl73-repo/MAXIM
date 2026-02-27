# Interface Management and Integration

## The Big Picture

Interfaces are where systems fail. The internal design of each subsystem may be fully correct, yet the system fails because subsystems make different assumptions about what crosses the boundary. Interface management is the discipline of defining, controlling, and verifying all inter-element connections to prevent integration surprises.

```
WHY INTERFACES ARE HARD
──────────────────────────────────────────────────────────────────
Subsystem A design team assumes:
  Power input: 28.0 VDC ±1V
  Signal: RS-422, 9600 baud, MSB-first

Subsystem B design team assumes:
  Power output: 28.0 VDC ±3V (within their spec, but not B's need)
  Signal: RS-422, 9600 baud, LSB-first (different bit order)

Both teams built exactly what their spec said.
Integration fails.

Interface failures are proportionally cheap to prevent,
catastrophically expensive to fix late:
  Interface spec written wrong → change order before design
  Design complete, interface discovered wrong → redesign both teams
  Hardware built, interface discovered wrong → hardware rework + retest
  System deployed, interface discovered wrong → field fix + recall
```

---

## Interface Control Documents (ICDs)

The ICD is the formal contract between two systems or subsystems at an interface — exactly an API contract for physical systems. ICD = OpenAPI/Swagger spec: it specifies what crosses the boundary, in what format, at what rate, with what error handling, agreed by both sides before implementation begins. ICD revision = breaking API change requiring a version bump. ICWG change process = API deprecation policy. Change freeze after CDR = API stability guarantee in a versioned SDK.

```
ICD STRUCTURE
──────────────────────────────────────────────────────────────────
1. IDENTIFICATION
   Interface name and number
   Drawing number / document number
   Revision level, date, approvers
   System A (producer side)
   System B (consumer side)

2. REFERENCE DOCUMENTS
   Parent system specification
   Standards applicable (MIL-STD-1553, ARINC 429, etc.)
   Component datasheets referenced

3. INTERFACE DEFINITION (the core content)
   Physical: connector type, pinout, strain relief, mating force
   Electrical: voltage levels, current, impedance, timing
   Mechanical: envelope, mounting, loads at attachment points
   Thermal: heat load exported to adjacent system, fluid flow
   Data: protocol, message format, timing, error handling
   Functional: what information is exchanged, when, who initiates

4. ENVIRONMENTS AT INTERFACE
   Temperature, vibration, moisture → applicable to connector/connector

5. VERIFICATION
   How will compliance with this ICD be verified?
   Test procedure reference

6. CHANGE HISTORY
   Every approved change, reason, signatures
```

### Interface Types

```
INTERFACE TYPES
──────────────────────────────────────────────────────────────────
MECHANICAL INTERFACE
  Attachment geometry: bolt pattern, fastener size, torque spec
  Alignment features: dowel pins, datum surfaces
  Envelope: cleared space for mating hardware
  Loads: forces and moments transmitted across interface
  Thermal: conductive heat transfer path

ELECTRICAL INTERFACE
  Connector: part number, gender, contact arrangement
  Power: voltage, current, ripple, inrush, disconnects
  Signal: voltage levels (TTL, LVDS, RS-422), timing, loading
  Ground reference: signal ground vs chassis ground vs floating
  EMI/EMC: shielding, filtering at interface

DATA/PROTOCOL INTERFACE
  Physical layer: wire type, speed, connector
  Data link: protocol (CAN, Ethernet, MIL-STD-1553, ARINC 429)
  Application: message format, content, encoding, timing
  Error handling: what to do when message lost/corrupted

THERMAL INTERFACE
  Fluid connections: pipe/tube size, material, fittings, flow rate
  Conductive path: thermal resistance at joint (W/°C), material
  Radiative: emissivity, view factors

HUMAN INTERFACE (HMI)
  Displays: information presented, update rate, format
  Controls: physical layout, force required, feedback
  Alarms: when/how system alerts operator
  Documented in HFE (Human Factors Engineering) plan
```

---

## Interface Matrix

The interface matrix is the "complete map" — every possible pair of subsystems × every type of interface.

```
INTERFACE MATRIX
──────────────────────────────────────────────────────────────────
       │Nav │Prop│Power│Comm │GNC │Struct│
───────┼────┼────┼─────┼─────┼────┼──────┤
Nav    │ — │  — │28VDC│  — │Pos  │  — │
Prop   │  — │ — │28VDC│  — │Thrust│Loads│
Power  │  — │  — │ — │28VDC│28VDC│Heat │
Comm   │  — │  — │28VDC│ — │Cmd  │  — │
GNC    │ NavSv│Thr│  — │  — │ — │  — │
Struct │  — │Loads│  — │  — │Loads│ — │

Each non-empty cell = an interface = requires an ICD
Matrix is symmetric (interface A-to-B same as B-to-A, different view)

Use N² diagram (from architecture) to populate interface matrix.
Interface matrix identifies WHICH ICDs need to be written.
```

---

## Integration Management

### Integration Strategy

```
INTEGRATION APPROACHES
──────────────────────────────────────────────────────────────────
Big Bang:
  Integrate everything at once
  Fast to reach system configuration
  Impossible to isolate faults — which interface failed?
  Only acceptable for very simple systems

Incremental:
  Integrate one element at a time
  Fault isolation: last added = the issue (usually)
  Methods:
    Top-down: integrate from top, use stubs for lower elements
    Bottom-up: integrate bottom first, use drivers to exercise
    Horizontal: integrate by function thread (all elements on one function)

Parallel / Branching:
  Multiple integration streams in parallel (different branches of architecture)
  Merges as integration matures
  Requires synchronized interface definitions (ICDs must be locked first)

RECOMMENDATION:
  Horizontal (function thread) integration best for system-level testing
  Start with safety-critical / highest-risk interfaces first
  Interface simulation (stubs) for elements not yet available
```

### Integration Test Environment

```
INTEGRATION ENVIRONMENTS
──────────────────────────────────────────────────────────────────
Bench Test:
  Individual subsystem on lab bench
  Stimulus: signal generators, power supplies, lab equipment
  Response: oscilloscope, logic analyzer, data acquisition
  Fast iteration, low cost

Subsystem Integration Lab (SIL):
  Multiple subsystems integrated
  Some real hardware, some simulated
  Allows testing of subsystem-level interfaces
  Lower cost than full system, higher fidelity than bench

Systems Integration Lab (SIL) / Test Bed:
  Full avionics/electronics rack
  All computing and I/O present (or high-fidelity sim)
  Flight software runs on target hardware
  Physical environment simulated (pilot inputs, sensor data)
  Used for flight software validation on aircraft

Hardware-in-the-Loop (HIL):
  Physical hardware in control loop with simulated plant
  Autopilot HIL: real avionics, simulated aircraft dynamics
  Automotive ECU HIL: real ECU, simulated engine/vehicle
  Most rigorous test short of real operation

Iron Bird (aircraft specific):
  Full aircraft system test rig without airframe structure
  All actuation, hydraulics, avionics, fuel, landing gear
  Test flight control, hydraulic, electrical systems integrated
  Reveals system-level issues before first flight
```

---

## Interface Change Control

```
INTERFACE CHANGE PROCESS
──────────────────────────────────────────────────────────────────
After ICD is baselined (approved), changes require formal process:

Engineering Change Request (ECR):
  Proposer documents: what changes, why, impact
  Impact analysis: which other ICDs or subsystems are affected?
  Cost and schedule impact
  → Route to Interface Control Working Group (ICWG)

Interface Control Working Group (ICWG):
  Representatives from BOTH sides of every affected interface
  Customer (program manager) representative
  Reviews ECR, approves, rejects, or requests more data

Engineering Change Notice (ECN) / Engineering Change Order (ECO):
  Approved change documented
  New ICD revision issued
  ALL affected drawings and specs updated
  Verification of change at integration

Change freeze points:
  After PDR: system-level interfaces frozen (SV-1)
  After CDR: detailed ICDs frozen
  After CDR changes: require CCB (Change Control Board) approval
  Very expensive to change after CDR — hardware may need rework
```

---

## Integration Risk Management

```
TOP INTEGRATION RISKS
──────────────────────────────────────────────────────────────────
Late ICD baselinealing:
  Teams designing to TBD interfaces
  Mitigation: aggressive ICD schedule, interim ICDs

Assumption mismatch:
  Two teams assume different defaults
  (byte order, timing reference, ground reference)
  Mitigation: formal interface review workshops

Schedule compression at integration:
  Integration is last phase, always has schedule pressure
  Defects found late → exponential cost growth
  Mitigation: early integration test of high-risk interfaces

Simulator/stub fidelity:
  If real hardware is replaced by low-fidelity simulator,
  integration test misses issues → found at system test
  Mitigation: formally track simulator fidelity vs real hardware

Hardware delivery delays:
  Integration can't start without hardware
  Mitigation: engineering model hardware (EM), incremental delivery

Software maturity at integration:
  SW too immature → integration reveals SW bugs, not interface bugs
  Mitigation: SW integration readiness criteria (test coverage, etc.)
```

---

## Standards for Interface Definitions

### Electrical / Data Interfaces

| Standard | Interface Type | Domain |
|----------|---------------|--------|
| MIL-STD-1553 | 1 Mbit/s dual-redundant bus | Military avionics |
| ARINC 429 | 100 kbit/s unidirectional serial | Civil avionics |
| CAN (ISO 11898) | 1 Mbit/s differential serial bus | Automotive, industrial |
| Ethernet (IEEE 802.3) | 10M–100G | Commercial IT, modern vehicles |
| ARINC 664 (AFDX) | Deterministic Ethernet for avionics | Civil avionics |
| SpaceWire (ECSS-E-ST-50-12) | 200 Mbit/s point-to-point | Spacecraft |
| RS-422/485 | Differential serial | Industrial, legacy |
| USB 3.x | 5–40 Gbit/s | Consumer, lab test |
| PCIe | 8–32 GT/s per lane | Embedded computing |

### Mechanical Interfaces

| Standard | Domain |
|----------|--------|
| MIL-C-5015 | Military circular connector (legacy, widely used) |
| MIL-DTL-38999 | Modern military circular connector (Series III) |
| D-Sub (DE-9, DB-25) | Legacy serial/parallel data |
| VPX (VITA 65) | Rugged embedded computing boards |
| OpenVPX | Interoperability on VPX |

---

## Data Interface Definitions in MBSE

In MBSE practice (SysML), interfaces are modeled as ports with typed flows:

```
SYSML INTERFACE MODELING
──────────────────────────────────────────────────────────────────
FlowSpecification: typed data/energy/material that flows
  «flowSpecification» FuelFlow
    in: flowRate: L/s
    out: pressure: Pa

Block A: «block» FuelPump
    +p1: «flowPort» FuelFlow  ← typed port

Block B: «block» Engine
    +p2: «flowPort» FuelFlow  ← matching port

In IBD, connect p1 to p2 = interface defined in model
ICD can be generated from model automatically (MBSE value)

ProxyPort (SysML 1.4+):
  Represents boundary of block as seen from outside
  Full port vs proxy port distinction = interface behavior
  Replaces older flow port notation
```

---

## Decision Cheat Sheet

| Interface Challenge | Action |
|--------------------|--------|
| Define what crosses a subsystem boundary | Write ICD (Interface Control Document) |
| Map all interfaces in the system | Create interface matrix + N² diagram |
| Control changes after baseline | ICWG + ECR/ECO process |
| Test a subsystem before mating hardware available | Simulator/stub for unavailable hardware |
| Integrate without losing isolation | Incremental integration, one interface at a time |
| Early detection of interface mismatches | Interface requirements review workshop (both teams) |
| Capture interfaces in system model | SysML ports + flow specifications in IBD |

---

## Common Confusion Points

**ICD is a contract, not a description**: An ICD is not written after the fact to describe how things connected. It is written first, agreed by both parties, and signed. The ICD precedes the design on both sides of the interface. Writing it after hardware is built means you're documenting, not managing.

**Who owns the ICD?**: For internal interfaces (within a program), the systems engineer owns it, with inputs from both interface owners. For external interfaces (your system to customer's system), often jointly owned. Ambiguity in ownership = no change control = interface creep. Assign explicit ownership.

**Protocol is not sufficient specification**: Saying "uses Ethernet" is not an interface definition. You need: speed, connector, physical layer, protocol stack, application-layer message format, timing, error handling, connection establishment/teardown, security. Protocol is just one layer.

**Simulator fidelity must be documented**: When hardware A is simulated for testing hardware B, the simulation's fidelity to the real interface must be documented. "We tested against a simulator" without knowing the fidelity level leaves unknown risk. Test against the lowest-fidelity simulator, and document what was not modeled.

**Integration ≠ acceptance**: Successful integration (subsystems can talk to each other) does not mean the system meets its requirements. Integration verifies interfaces. System-level test verifies functional requirements. Acceptance test validates that the customer's needs are met. All three are required.
