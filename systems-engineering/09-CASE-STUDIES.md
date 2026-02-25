# Case Studies: Aerospace, Defense, and Software

## The Big Picture

SE failures and successes teach the discipline's most durable lessons. These cases span aerospace failures, software disasters, and successful complex system deliveries. Each illustrates specific SE principles with real consequences.

```
CASE STUDY MAP
──────────────────────────────────────────────────────────────────
CLASSIC FAILURES (fundamental SE failures):
  Mars Climate Orbiter (1999)      Units mismatch — interface failure
  Therac-25 (1985–1987)            SW safety without system-level view
  Ariane 5 Flight 501 (1996)       Reuse without re-verification
  Boeing 737 MAX (2018–2019)       Requirements and safety process failures
  Tacoma Narrows Bridge (1940)     Missing physics in requirements

COMPLEX SUCCESSES:
  Apollo Program (1961–1969)       SE discipline invented under pressure
  Space Shuttle Challenger (1986)  Where SE broke down (for contrast)
  F-22 Raptor development          Large-scale MBSE adoption
  ISS (International Space Station) SoS (System of Systems) SE

SOFTWARE-SE INTERSECTIONS:
  Denver Airport Baggage System    SW in physical system integration
  Healthcare.gov launch (2013)     Requirements + integration failure
  Knight Capital (2012)            Change management, deployment risk
```

---

## Mars Climate Orbiter (1999)

### What Happened

```
TIMELINE
──────────────────────────────────────────────────────────────────
1998-12-11: MCO launched (Mars Climate Orbiter spacecraft)
1999-09-23: MCO arrives at Mars, initiates orbit insertion burn
             → satellite enters Mars atmosphere at wrong angle
             → atmospheric friction destroys spacecraft
             → $327M mission lost

ROOT CAUSE:
  Lockheed Martin Astronautics (ground software) output
  navigation forces in English units (pound-force seconds).

  NASA JPL navigation software expected
  metric units (newton-seconds).

  This mismatch was passed as a navigation parameter
  across an interface for 10 months of cruise.
  The spacecraft drifted progressively off course.
```

### SE Lessons

```
LESSONS LEARNED
──────────────────────────────────────────────────────────────────
1. Interface Control Document (ICD) failure:
   The ICD should have specified: parameter name, units, sign convention.
   Either the ICD didn't specify units, or the deviation from ICD
   wasn't caught by code review or testing.

2. Anomaly not investigated:
   Small navigation residuals (errors) were reported for months.
   Multiple engineers noticed but didn't escalate effectively.
   "Residuals within acceptable range" → accepted as normal.
   No root cause investigation was triggered.

3. Independent verification gaps:
   Navigation data was not cross-checked by an independent team.
   In-loop simulation during cruise should have revealed drift.

DIRECT SE FIXES AFTER MCO:
  Unit specification mandatory in all interface specifications
  Navigation cross-check procedures revised
  Anomaly investigation triggers lowered
  Independent validation of navigation data required

BROADER PRINCIPLE:
  Small consistent deviations from expected are early warning signals.
  Investigation should happen when pattern is noticed, not at failure.
  "Acceptable range" doesn't mean "no problem exists."
```

---

## Therac-25 (1985–1987)

### What Happened

```
THERAC-25: RADIATION THERAPY MACHINE
──────────────────────────────────────────────────────────────────
Medical linear accelerator for cancer radiation therapy.
1985–1987: 6 patients given radiation overdoses.
3 patients died. 3 severely injured.

Overdose: 100× intended dose (100 rads vs 10,000 rads delivered).

TECHNICAL CAUSE:
  Race condition in control software.
  Rapid operator key entry while machine transitioning mode
  → software flag not cleared at right time
  → machine entered X-ray mode (high power) while configured for
     electron mode (low power, no physical shield engaged)
  → raw electron beam at full X-ray power hit patient directly
     (with no beam-flattening filter)

KEY SE FAILURE: The previous Therac-20 had hardware interlocks.
  The Therac-25 removed hardware interlocks and relied on software alone.
  Software redundancy was never validated as equivalent to hardware.
  The software was reused from Therac-20 without full re-verification.
```

### SE Lessons

```
LESSONS LEARNED (Nancy Leveson's definitive analysis)
──────────────────────────────────────────────────────────────────
1. Removed safety-critical hardware without safety analysis:
   Physical interlocks provide independence from software.
   Removing hardware interlocks required demonstrating software
   was at least as safe — this was never done.
   SE principle: Safety-critical functions require defense-in-depth.
   Software alone is insufficient for safety-critical functions.

2. Reuse without re-verification:
   Code reused from Therac-20, which had hardware safety barriers.
   With barriers, software race condition was harmless.
   Without barriers, same code was lethal.
   SE principle: Reusing components in a different context
   requires re-analysis of requirements, not just the component.

3. Severity underreported and investigation delayed:
   AECL (manufacturer) initially dismissed patient reports.
   "Software is correct" assertion without investigation.
   SE principle: When reported harm exceeds expected range,
   investigate immediately regardless of apparent confidence in system.

4. Inadequate testing:
   Race condition only reproducible under specific timing.
   Testing did not cover concurrent state transitions.
   SE principle: Test for timing vulnerabilities in concurrent systems.
   Formal methods (model checking) can find these.

5. Error messages weren't actionable:
   "MALFUNCTION 54" — no information about what to do.
   Operator continued treating patients to avoid schedule delays.
   SE principle: Safety-critical error messages must mandate action.
   Never design a safety system where user can continue past an error.

RESULT: Therac-25 became the canonical case in software safety.
  Every software safety standard (IEC 61508, DO-178C) references its lessons.
  Led directly to IEC 60601-1 (medical electrical equipment requirements).
```

---

## Ariane 5 Flight 501 (1996)

### What Happened

```
ARIANE 5 FLIGHT 501
──────────────────────────────────────────────────────────────────
1996-06-04: First flight of Ariane 5 launch vehicle.
37 seconds after launch: rocket deviates sharply, self-destructs.
Payload destroyed: $370M (Cluster scientific satellites).

ROOT CAUSE:
  Reused Inertial Reference System (IRS) software from Ariane 4.
  Ariane 4 code converted a 64-bit floating point horizontal
  velocity to a 16-bit integer.
  This conversion could overflow — but on Ariane 4, the
  velocity value was always < 16-bit max.

  Ariane 5 flew a different trajectory. Same code ran.
  Ariane 5's horizontal velocity exceeded Ariane 4 limits.
  → 64-bit float converted to 16-bit int → OVERFLOW
  → Ada exception raised → IRS shut down and sent error code to
     flight computer → flight computer interpreted error code
     as valid navigation data → commanded full deflection of
     nozzles → aerodynamic forces destroyed vehicle.

DETAILED FAILURE CHAIN:
  Software bug (overflow) → exception → diagnostic data output
  → interpreted as navigation data → wrong flight command
  → physical destruction
```

### SE Lessons

```
LESSONS LEARNED
──────────────────────────────────────────────────────────────────
1. Reuse requires re-analysis in new context:
   Software was "qualified" for Ariane 4 envelope.
   Qualification is context-specific.
   New vehicle with different trajectory = new context = new analysis.
   SE principle: Verify requirements on the new system, not just the component.

2. Exception handling in safety-critical software:
   When IRS failed, it should have failed safe (hold last valid value,
   or transfer to backup).
   Instead it sent raw exception diagnostic data on the output bus.
   Flight computer had no protection against invalid data on nav bus.
   SE principle: Every failure mode must have an explicit safe response.

3. Unnecessary code running:
   The overflow-prone function was for horizontal bias calculation.
   That calculation was only needed for 50 seconds before launch.
   It was still running at 37 seconds into flight (post-launch),
   where it served no purpose.
   SE principle: Eliminate unnecessary functionality from safety-critical
   systems. Code that is not needed should not run.

4. Independent review scope:
   The software was reviewed and certified for Ariane 4.
   An independent review of the reuse decision was not done.
   SE principle: Changes in context require new independent review.

RESULT: Led to rigorous software reuse policies in space industry.
  ESA SW engineering standards updated.
  ECSS-Q-ST-80C (space SW engineering) now requires:
  explicit analysis when reusing heritage software.
```

---

## Boeing 737 MAX (2018–2019)

### What Happened

```
BOEING 737 MAX ACCIDENTS
──────────────────────────────────────────────────────────────────
2018-10-29: Lion Air Flight 610 crashes, 189 killed.
2019-03-10: Ethiopian Airlines Flight 302 crashes, 157 killed.
Total: 346 killed. 737 MAX grounded worldwide.

TECHNICAL CAUSE (simplified):
  MCAS (Maneuvering Characteristics Augmentation System):
    Added to compensate for changed engine position (larger engines
    moved forward on wing → changed pitch characteristics).
    MCAS pushed nose down when it detected high angle of attack (AoA).

  Single AoA sensor:
    MCAS received input from single AoA sensor.
    If sensor failed, MCAS activated repeatedly.
    When pilots countered, MCAS re-activated (short activation logic).
    Runaway nose-down → unrecoverable.

  Single point of failure: one sensor
  Runaway trigger: MCAS could re-activate after pilot counter-input
  No redundancy validation: dual AoA disagreement warning was optional
    (customers could pay extra for it — Boeing didn't make it standard)
```

### SE Lessons

```
LESSONS LEARNED
──────────────────────────────────────────────────────────────────
1. Single point of failure in safety-critical path:
   MCAS relied on single AoA sensor.
   Standard SE practice: safety-critical sensing must be redundant.
   AoA sensor disagree alert was "optional" = $8K add-on.
   SE principle: Safety equipment cannot be optional on safety-critical system.

2. Hazard severity was understated:
   MCAS was characterized as a handling quality system (not safety-critical)
   → lower design assurance level (DAL) → less rigorous certification.
   MCAS effect (unrecoverable nose-down) is clearly catastrophic.
   SE principle: Safety classification must reflect worst-case consequence,
   not nominal function.

3. Runaway control not adequately analyzed:
   MCAS could continuously re-activate after pilot counter-input.
   This interaction was not in the FMEA scope.
   SE principle: FMEA must include human-machine interaction failure modes.
   "Pilot follows incorrect checklist" is a failure mode.

4. Lack of full disclosure:
   737 MAX MCAS details were not fully disclosed to pilots or airlines.
   Assumption: "qualified 737 pilots need no additional MCAS training."
   SE principle: If a system significantly changes operational characteristics,
   operators must be informed and trained.

5. Certification pressure on derivative vs new type:
   Full new type certification for a new aircraft vs
   supplemental certification for a derivative saves years/billions.
   MCAS scope grew during development, but certification basis
   was not updated accordingly.
   SE principle: Changes in scope trigger changes in certification basis.

RESULT: Congressional hearings. FAA restructuring.
  Boeing leadership change. $20B+ total cost.
  2023: DOJ investigation, additional safety improvements required.
  Triggered fundamental review of FAA Organization Designation Authorization (ODA).
```

---

## Apollo Program: A SE Success

```
APOLLO: INVENTING SE UNDER PRESSURE
──────────────────────────────────────────────────────────────────
Context: 1961, Kennedy's "moon before decade's end" commitment.
  Technology to get to the Moon did not exist.
  500,000 people, 20,000 companies, $25B (equivalent ~$175B today).
  No precedent for systems this complex.

SE contributions invented during Apollo:
  Formal requirements specification for complex systems
  Configuration management (track WHICH hardware is in WHICH vehicle)
  Systems integration testing (all systems integrated in SIL before flight)
  Mission operations as systems engineering (Mission Control)
  Earned Value Management (track cost and schedule vs plan)
  Formal failure mode analysis (FMEA applied systematically post-Apollo 1 fire)

Apollo 13 (1970) — SE success under failure:
  Oxygen tank explosion → life-threatening emergency
  Mission Control improvised CO₂ scrubber using available parts
  (lunar module scrubber canisters ≠ command module sockets)
  Successfully brought crew home in 4 days
  → Ground-based systems engineering + simulation capability
    was the enabling factor

APOLLO 1 FIRE (1967) — Where SE was weak:
  Command module had 11 miles of wiring, no systematic EMC review
  Flammable materials in 100% oxygen environment (not analyzed)
  No abort procedure for launch pad fire
  → 3 astronauts killed
  → Led to full safety review, FMEA methodology expansion
  → Apollo 7 flew 18 months later, all missions successful after
```

---

## Denver Airport Automated Baggage System

```
DENVER AIRPORT BAGGAGE SYSTEM (1993–1995)
──────────────────────────────────────────────────────────────────
Scope: Fully automated baggage handling system for new Denver
  International Airport. 4,000 automated cars, 21 miles of track.
  30 destinations. Simultaneous loading/unloading while aircraft at gate.
  Largest automated baggage system attempted.

Schedule: Airport opened 1993. System would be ready.
Result: Airport opening delayed 16 months waiting for baggage system.
  Total delay cost: $500M+.
  System activated 1995 — only for United Airlines concourse.
  Full system (all concourses) never completed as designed.
  Manual backup system built in parallel.

ROOT CAUSES:
  1. Requirements ambiguity:
     No formal requirements specification written.
     Contract awarded, design began without agreed requirements.
     Scope changed throughout development (e.g., added automated
     baggage from check-in at later stage — massive integration change).

  2. Integration not planned:
     Mechanical, software, and systems teams worked independently.
     Assumed integration would be straightforward.
     First system-level test: cars crashed into each other,
     bags fell from carts, system jammed continuously.

  3. Concurrency underestimated:
     30 simultaneous destinations with continuous car routing
     → combinatorial routing problem not analyzed
     → software could not compute paths fast enough at design load

  4. Physical-software interaction not modeled:
     Mechanical timing assumptions (car acceleration, deceleration)
     were not matched to software timing model.
     Cars arrived at positions before software expected them.

LESSONS:
  Physical-cyber integration requires co-design, not sequential design.
  Requirements specification is not optional for novel systems.
  System-level integration testing must start early.
```

---

## International Space Station: SoS SE Success

```
ISS: SYSTEM OF SYSTEMS SE
──────────────────────────────────────────────────────────────────
Context:
  16 nations, 5 space agencies, 20+ year operational life.
  Individual modules built by NASA, Roscosmos, JAXA, ESA, CSA.
  First module launched 1998; completed 2011.
  Currently inhabited (2025+).

SE challenges solved:
  Multi-national interface management:
    Every physical and data interface required bilateral ICD.
    American docking systems compatible with Russian Soyuz.
    Power systems: Russian (28VDC) + American (120VDC) co-exist.
    Data systems: MIL-STD-1553, Ethernet, and Russian equivalents.

  Long lifecycle requirement management:
    Requirements from 1984 still relevant to 2025 hardware.
    Formal CM maintained across decades and agencies.

  Evolving SoS:
    Commercial crew (SpaceX Dragon, Boeing Starliner) integrated
    as new "system" added to ISS "system of systems."
    New ICDs, new verification → same ISS.

  Key SE success factors:
    Early and aggressive interface definition
    Multinational CCB with treaty-level authority over changes
    Formal test at every integration point before launch
    Operations SE as rigorous as development SE

Ongoing challenges:
  Russian segment cooperation post-2022 (geopolitical)
  Lifetime extension decisions (original design life: 2024)
  Demonstrates: SoS lifecycle SE continues as long as system operates
```

---

## Decision Cheat Sheet (Case Study Lessons)

| SE Failure Pattern | Lesson | Case |
|-------------------|--------|------|
| Units/encoding mismatch at interface | Specify units in ICD, verify end-to-end | Mars Orbiter |
| Software safety relies on removed hardware | Hardware interlocks cannot be replaced by software without full safety analysis | Therac-25 |
| Component reused without context re-analysis | Reuse requires re-verification in new context | Ariane 5 |
| SPOF in safety-critical sensing | Redundancy required for catastrophic-risk sensors | 737 MAX |
| Safety classification understated | FMEA severity based on worst-case effect, not nominal | 737 MAX |
| Integration not planned | Integration must be designed, not assumed | Denver Baggage |
| Requirements undefined for novel system | Novel systems require more rigorous requirements, not less | Denver Baggage |

---

## Common Confusion Points

**Failure reports assign blame to individuals; SE looks at system**: The Mars Orbiter failure was attributed to "contractor used wrong units." But SE asks: why was no process in place to catch unit mismatches? Why did navigation anomalies not trigger investigation? System causation goes deeper than individual error.

**Certified = safe is false**: Therac-25 was reviewed and approved. Ariane 4 software was certified. 737 MAX was certified by FAA. Certification processes can be fooled by honest mistakes or bad-faith gaming. Certification demonstrates adherence to a process; it does not guarantee safety. The process must be appropriate for the risk.

**Complexity ≠ inevitable failure**: The Apollo program, ISS, and the Space Shuttle (183 successful missions before two losses) show that extremely complex systems can work reliably when SE is applied rigorously. Complexity increases risk — SE processes manage that risk without eliminating it.

**"Works on previous system" is not a safety argument for new system**: Ariane 5 and 737 MAX both failed because validated behavior on a previous system was assumed to apply on the new system. Context change requires new analysis. "It worked before" is a starting point for investigation, not a conclusion.
