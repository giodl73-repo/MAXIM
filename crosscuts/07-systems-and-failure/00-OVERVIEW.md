# 07 — Systems & Failure

## The Big Picture

This crosscut is the **Technology companion atlas**. It uses section number 7
because modern technology makes failure visible as a system property: grids,
robots, implants, formal methods, urban infrastructure, environmental systems,
semiconductor processes, batteries, and communication networks all fail through
interactions, not merely broken parts.

Risk asks what action follows under uncertainty. Systems & Failure asks what the
system reveals when assumptions meet load, time, coupling, incentives, and
maintenance reality.

```
SYSTEMS AND FAILURE

Failure is not just a component breaking.
Failure is loss of intended function under real conditions.

INTENT ----------> DESIGN ----------> OPERATION
what should happen architecture       real use, real load
   |                 |                  |
   v                 v                  v
ASSUMPTIONS ----> COUPLINGS -------> STRESSORS
what must hold     hidden links       load, time, attack, weather
   |                 |                  |
   v                 v                  v
DEGRADATION ----> INCIDENT --------> LEARNING
margin erodes      function lost      design, training, doctrine change

A failure is a measurement of the system's true boundary.
```

Read this as a **failure chain**. A system begins with intent and design, but it
lives in operation. Assumptions meet couplings. Couplings meet stressors.
Stressors erode margin. Margin loss becomes an incident. The mature system
learns; the brittle system merely repairs the broken part and waits.

---

## Why This Belongs With Technology

Technology is where knowledge becomes operational responsibility. A theorem, a
prototype, a material, or a policy can look sound in isolation. Once embedded in
an operating system, failure can arrive through interfaces, maintenance,
incentives, scale, weather, users, attackers, or supply chains.

```
artifact + environment + operators + time = system
```

| Technology Domain | Typical Failure Surface | What Must Be Designed |
|---|---|---|
| Power grids | cascading trips, demand spikes, weather | protection, reserve, islanding, restoration |
| Robotics | sensor error, actuator limits, human proximity | control, fail-safe states, supervision |
| Medical devices | biocompatibility, software, use error | verification, alarms, clinical workflow |
| Formal methods | spec gap, model boundary, proof misuse | assumptions, refinement, runtime checks |
| Urban systems | flooding, heat, congestion, governance | redundancy, maintenance, adaptation |
| Energy storage | thermal runaway, degradation, supply | monitoring, containment, lifecycle planning |
| Telecom | congestion, routing, power, physical cuts | diversity, routing, backup power |

The central bridge:

```
engineering proves capacity
operations prove resilience
incidents prove assumptions
```

---

## Layer 1: Function, Margin, and Degradation

A system fails when intended function is lost. The path to that loss usually
starts earlier, when margin begins to erode.

```
healthy margin -> reduced margin -> degraded service -> incident -> loss
```

| Concept | Diagnostic Question | Failure Signal |
|---|---|---|
| Function | What must the system continue to do? | ambiguous success criteria |
| Margin | How far from the limit is normal operation? | repeated near misses |
| Degradation | What gets worse before failure? | latency, cracks, heat, noise, drift |
| Threshold | Where does behavior change sharply? | cliff edge, phase transition, trip point |
| Recovery | How does function return? | manual workaround, restart, repair, failover |
| Residual risk | What remains after controls? | accepted hazard, untested tail |

The practical move is to monitor **leading indicators**, not just final failure.
A bearing warms before it seizes. A queue grows before outage. A foundation
settles before collapse. A team burns out before delivery fails.

---

## Layer 2: Coupling and Cascades

Tightly coupled systems propagate failure faster than humans can understand
them. Complex systems can hide paths no diagram shows.

```
LOOSE COUPLING                         TIGHT COUPLING

part fails -> local effect             part fails -> immediate cascade
operator has time                      operator is already behind
buffers absorb                         buffers absent or full
```

| Coupling Type | Example | Cascade Risk |
|---|---|---|
| Physical | fire, flood, vibration, thermal runaway | local damage spreads through proximity |
| Informational | bad sensor, stale data, wrong map | wrong action propagates through control |
| Logical | shared dependency, protocol assumption | one bug breaks many services |
| Financial | leverage, collateral, liquidity | forced selling or default chain |
| Ecological | trophic link, invasive species | population or nutrient cascade |
| Institutional | single approval path, brittle rule | delay or capture blocks response |

Cascades do not require every component to be weak. They require a path where
one failure changes the load on the next part faster than the system can adapt.

---

## Layer 3: Human, Organizational, and Interface Failure

Many failures are blamed on "human error" after the system has made the human
the final, overloaded safety device.

```
bad interface -> wrong mental model -> wrong action -> blamed operator
```

| Failure Surface | What to Inspect | Better Question |
|---|---|---|
| Alarm flood | signal priority, false positives, timing | Why was the operator trained to ignore alarms? |
| Procedure drift | work-as-imagined vs work-as-done | Why did the workaround become necessary? |
| Hand-off | information loss between roles | What context failed to cross the boundary? |
| Maintenance | access, spares, incentives, schedule | Why was degradation allowed to accumulate? |
| Training | rare event practice, simulators, drills | Did the organization train the actual failure mode? |
| Authority | who can stop the line | Could anyone halt the system before loss? |

The mature frame is:

```
human error is often the name of the last visible action
not the root cause
```

---

## Layer 4: Safety Cases, Verification, and Proof

Verification asks whether the artifact meets a specification. A safety case asks
whether the system is acceptably safe in context.

```
SPECIFICATION -> VERIFICATION -> SAFETY CASE -> OPERATIONAL EVIDENCE
```

| Evidence Type | Strength | Weakness |
|---|---|---|
| Test | concrete behavior | sparse relative to state space |
| Proof | exhaustive inside assumptions | spec may omit real hazard |
| Simulation | explores many regimes | model may be wrong |
| Inspection | finds material or process defects | sampling misses rare defects |
| Incident history | real operating evidence | biased toward what has already happened |
| Safety case | integrates evidence and argument | can become paperwork if not challenged |

Formal methods are powerful, but they do not remove the need to ask:

```
did we prove the right property
of the right model
under the right assumptions
for the real operating context?
```

---

## Layer 5: Incident Learning and Resilience

The point of incident review is not to find the guilty component. It is to
change the system so the next stressor has a different path.

```
incident -> timeline -> contributing factors -> controls -> changed behavior
```

| Learning Mode | Good Output | Bad Output |
|---|---|---|
| Timeline | shared sequence of events | cherry-picked story |
| Root-cause analysis | interacting contributors | single-cause myth |
| Blameless postmortem | system improvements | no accountability for neglected risk |
| Red team | exposed assumption | theatrical adversary exercise |
| Drill | practiced response | checkbox exercise |
| Design change | removed failure path | more warning labels |

Resilience is more than redundancy. It includes detection, absorption,
adaptation, recovery, and learning.

```
detect -> absorb -> adapt -> recover -> learn
```

---

## Cross-Library Appearance Map

| Section | How Systems and Failure Appear |
|---|---|
| Natural World | ecosystem collapse, invasive species, food-chain cascades, crop failure |
| Earth & Space | earthquakes, storms, floods, climate feedbacks, groundwater depletion |
| Material Culture | fatigue, corrosion, delamination, firing defects, fiber failure |
| Life Sciences | organ failure, immune dysregulation, epidemics, clinical safety |
| History & Ideas | empire collapse, military failure, failed reforms, ethical disasters |
| Mechanics | bridges, aircraft, reactors, grids, HVAC, plumbing, manufacturing lines |
| Technology | verification, robotics, medical devices, infrastructure, batteries, telecom |
| Social Sciences | market crashes, institutional failure, crime control failure, public-health failure |
| Language & Communication | misinformation cascades, translation failures, protocol breakdowns |
| Mathematics & Physics | stability, control, phase transitions, uncertainty, model failure |
| Arts & Culture | performance failure, conservation loss, design defects, audience breakdown |
| Computing & Software | outages, security incidents, consensus failure, rollback, observability gaps |
| People | decision makers, operators, reformers, investigators, whistleblowers |

---

## What This Crosscut Is For

Use it when a system has failed, nearly failed, or is being designed for
conditions where failure would matter.

```
QUESTION                           FIRST DIAGNOSTIC MOVE

"What broke?"                   -> define lost function, not broken part
"Why did it spread?"            -> map coupling and cascade path
"Why did nobody stop it?"       -> inspect signals, authority, and timing
"Was it human error?"           -> reconstruct interface, workload, and incentives
"Is proof enough?"              -> compare verified spec with real hazard
"Did we learn?"                 -> look for changed controls and behavior
```

The goal is not pessimism. The goal is to design systems that can be surprised
without becoming catastrophes.

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether a failure is component-level or system-level | Define intended function, operating context, and lost capability | The broken part may only be the final visible symptom |
| Whether margin is eroding | Track leading indicators: heat, latency, cracks, queue depth, near misses | Final failure metrics arrive too late |
| Whether coupling can cause cascades | Map physical, informational, logical, financial, ecological, and institutional links | Strong parts can still fail together through shared dependencies |
| Whether "human error" is the root cause | Inspect interface, alarms, procedures, workload, training, and authority | Blaming the operator often hides design debt |
| Whether verification covers the hazard | Compare tests, proofs, simulations, and safety case against real operating assumptions | Proof of the wrong property is false comfort |
| Whether redundancy creates resilience | Check detection, switching, recovery, diversity, and common-mode exposure | Backup components do not help if the same event disables them all |
| Whether incident learning happened | Look for changed controls, doctrine, training, incentives, or architecture | A postmortem without changed behavior is documentation, not learning |
| Whether a design is safe enough | Identify residual risk, who bears it, and who can stop operation | "Acceptable" is a governance claim, not just an engineering calculation |

---

## Common Confusion Points

**Failure is not the opposite of success** — A system may be "working" while
margin erodes. Near misses, workarounds, alarm floods, deferred maintenance, and
operator heroics are often signs that success is being borrowed from the future.

**Root cause is rarely singular** — Complex failures usually have contributing
conditions. A single root cause is often a managerial simplification, not a
technical explanation.

**Human error is usually downstream** — People do make mistakes, but systems
shape what mistakes are likely, visible, recoverable, and punished.

**Proof is not a safety case** — Proof can establish a property of a model or
program. A safety case must argue that the whole system is acceptably safe in
the operating context.

**Redundancy is not recovery** — A backup that cannot be detected, switched to,
powered, staffed, or maintained is not resilience.

---

## Connection Forward

Systems & Failure links the early crosscuts:

```
10 Methods of Knowing
  What evidence supports the claim?

13 Risk, Uncertainty & Decision
  What action follows under uncertainty?

07 Systems & Failure
  What did the operating system reveal when reality pushed back?
```

The next natural crosscut is `06-tools-and-instruments`: failure analysis almost
always depends on the tools that make hidden degradation visible.

