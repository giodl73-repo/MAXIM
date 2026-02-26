# Infrastructure Systems — Landscape Overview

## The Big Picture

Infrastructure systems are the physical and organizational foundations upon which
civilization operates. They are system-of-systems: complex assemblies of components
whose interdependencies create emergent behaviors -- including emergent failure modes
that cannot be predicted from analyzing individual components.

```
INFRASTRUCTURE AS SYSTEM-OF-SYSTEMS
=====================================

                        SOCIETY
                           |
         +-----------------+-----------------+
         |                 |                 |
         v                 v                 v
   LIFELINE            SUPPORT          ECONOMIC
   INFRASTRUCTURE      INFRASTRUCTURE   INFRASTRUCTURE
   ===========         ==============   ==============
   Energy               Healthcare      Financial services
   Water                Government      Commercial facilities
   Communications        Defense         Industrial
   Transportation         Emergency Svc.

   LIFELINE = enables all others
   Power fails -> water treatment fails -> communications fail -> economy halts

CRITICAL PROPERTY:
  Infrastructure systems are INTERDEPENDENT
  Failure in one often cascades to others
  The interdependency graph is not a tree -- it contains cycles
  Cycles mean cascading failures can loop and amplify

LIFECYCLE:
  Plan -> Design -> Finance -> Build -> Commission -> Operate -> Maintain -> Retire
  Each phase: different risk profile, different stakeholders, different failure modes
  US infrastructure is concentrated in the "Operate/Maintain" phase
  (built mostly 1950-1980; 40-70 year old assets)
```

---

## The System-of-Systems Problem

```
INFRASTRUCTURE INTERDEPENDENCY MAP
====================================

                ELECTRIC POWER
               /     |       \
              /      |        \
     WATER -----  TELECOM  --- TRANSPORT
     TREATMENT|   /    \    |  FUEL SUPPLY
       \      | /        \ |     /
        \     |            |    /
         \    |           FUEL  /
          \   |          SUPPLY/
           \  |          /    /
            HEALTHCARE ------

Specific dependencies:
  Electric power -> water: pumps, treatment chemicals injection, SCADA control
  Water -> electric: cooling water for thermal plants, hydroelectric
  Telecom -> everything: SCADA, HVAC, financial transactions, 911
  Transport -> everything: fuel delivery, goods, workers, repair crews
  Healthcare -> electric: life support, HVAC, cold chain for drugs/blood

THE 2003 NORTHEAST BLACKOUT CASCADE:
  1. Software bug in FirstEnergy SCADA (alarm system failed silently)
  2. Transmission line sag into tree (1 line lost)
  3. No alarm -> operator unaware
  4. Load shifted to adjacent lines -> they overloaded -> tripped
  5. Chain reaction: 50 million people lost power in 4 minutes
  6. Initiated by: alarm software bug in Ohio
  Result: 50 million without power, $6B economic loss, deaths from heat
  Lesson: tight coupling + unmonitored failure modes -> catastrophic cascade
```

---

## CISA Critical Infrastructure: 16 Sectors

```
CISA 16 CRITICAL INFRASTRUCTURE SECTORS (PPD-21, 2013)
========================================================

SECTOR                          KEY ASSETS
------------------------------  ----------------------------------------
1. Chemical                     Chemical plants, hazmat facilities
2. Commercial Facilities        Malls, hotels, sports venues, casinos
3. Communications               Internet exchanges, data centers, fiber, satellites
4. Critical Manufacturing       Steel, automotive, aerospace production
5. Dams                         Hydroelectric, flood control dams
6. Defense Industrial Base      Defense contractors, military supply chain
7. Emergency Services           Police, fire, EMS, search and rescue
8. Energy                       Electric grid, oil/gas pipelines, refineries
9. Financial Services           Banks, exchanges, clearinghouses, ATM networks
10. Food & Agriculture          Farms, food processing, water for irrigation
11. Government Facilities       Federal, state, local government buildings
12. Healthcare / Public Health  Hospitals, labs, pharmaceutical supply chain
13. Information Technology      Hardware, software, cloud infrastructure
14. Nuclear                     Nuclear power plants, research reactors
15. Transportation Systems      Aviation, rail, roads, ports, pipelines, postal
16. Water & Wastewater          Drinking water systems, wastewater treatment

LIFELINE SECTORS (subset that enables all others):
  Energy, Water, Communications, Transportation
  (all others require at least one of these four to function)

SECTOR-SPECIFIC AGENCIES (SSA):
  Energy: DOE
  Water: EPA
  Communications: DHS
  Transportation: DOT (with sector-specific agencies)
  Each SSA: set sector-specific security standards, coordinate with CISA
```

---

## Infrastructure Lifecycle

```
INFRASTRUCTURE ASSET LIFECYCLE
================================

PHASE 1: PLANNING (1-5 years)
  Need identification -> feasibility study -> alternatives analysis
  Environmental review (NEPA, EIS/EA in US)
  Public engagement, permitting
  Financial planning, funding sources
  Key stakeholders: government agencies, regulators, public
  Failure mode: unrealistic demand forecasts, poor site selection

PHASE 2: DESIGN (1-3 years)
  Conceptual -> preliminary -> detailed design
  Standards selection (ASCE, AISC, ASHRAE, IEEE, ASTM)
  Risk analysis, hazard mitigation
  Value engineering (cost reduction without performance compromise)
  Failure mode: value engineering that removes resilience features

PHASE 3: CONSTRUCTION (1-10 years, scale-dependent)
  Procurement: competitive bidding or negotiated
  Quality control: inspections, material testing
  Change orders: endemic in large projects (+20-50% cost is common)
  Key risk: cost overruns, schedule delays (average: 80% of major infra over budget)
  Reference class forecasting (Flyvbjerg): large infra projects 20-45% over budget

PHASE 4: OPERATIONS (20-100 years)
  Day-to-day operation: human operators + automation
  Monitoring: SCADA, sensors, inspections
  Performance tracking: availability, throughput, efficiency

PHASE 5: MAINTENANCE (ongoing throughout operations)
  Preventive: scheduled replacement on time/cycle
  Predictive: condition-based (sensor data drives decisions)
  Corrective: fix after failure
  Deferred: postponed due to budget -> accrues as backlog
  Key metric: backlog / annual budget ratio (US: often 5-10x)

PHASE 6: DECOMMISSION / RENEWAL
  End-of-life criteria: functional obsolescence, physical degradation, uneconomic repair
  Replacement vs. repair decision: life-cycle cost analysis
  Legacy contamination: brownfield challenges (Superfund sites, coal ash ponds)
```

---

## The Aging Infrastructure Crisis

```
US INFRASTRUCTURE AGE AND CONDITION (ASCE 2025 REPORT CARD)
=============================================================

System              Grade   Avg Age   Estimated Investment Need
------------------  -----   -------   -------------------------
Aviation            D+      40 yr     $111B over 10 yr
Bridges             C+      44 yr     $125B over 10 yr
Dams                D       57 yr     $70B over 10 yr
Drinking Water      C-      45 yr     $625B over 20 yr
Energy (grid)       C-      40 yr     $900B over 10 yr
Hazardous Waste     D+      --        $65B over 20 yr
Inland Waterways    D+      50+ yr    $100B over 10 yr
Levees              D       30+ yr    $80B over 10 yr
Ports               C+      --        $26B over 10 yr
Rail                C-      40+ yr    $38B over 10 yr
Roads               D       25-60 yr  $786B over 10 yr
Stormwater          D-      50+ yr    $298B over 20 yr
Wastewater          D+      50+ yr    $271B over 25 yr

ASCE Infrastructure Investment Gap: $2.6 trillion over 10 years (2021 estimate)
  US GDP ~$27T; annual infrastructure investment needed: ~$260B/yr
  Current spending: ~$150B/yr federal + state (growing with IIJA)
  Deficit: ~$100B/yr ($1T over 10 years)
  IIJA 2021: $1.2T over 10 years (largest infra investment since Interstate Highway System)

EU STATUS:
  Similar age profile for post-war infrastructure (1950s-1970s)
  EU: 25% of bridges beyond design life
  Germany: bridge inspections showing significant structural concerns (2019 collapse: Dresden)
  UK: "crumbling" RAAC (reinforced autoclaved aerated concrete) in hospitals, schools

DEVELOPING WORLD:
  Different problem: infrastructure never built, not aging
  Sub-Saharan Africa: ~$100B/yr infrastructure gap
  Access gap: 600 million without reliable electricity
```

---

## Cross-References Within This Directory

| File | Content |
|------|---------|
| 01-CLASSIFICATION.md | CISA 16 sectors, PPD-21, lifeline infrastructure |
| 02-INTERDEPENDENCY.md | Rinaldi taxonomy, N-1/N-2, cascade failure, Motter-Lai |
| 03-RESILIENCE.md | Resilience triangle, ASCE framework, SAIDI/SAIFI metrics |
| 04-FAILURE-MODES.md | Physical, cyber, natural hazard, systemic failures |
| 05-LIFECYCLE.md | ISO 55000, condition assessment, capital planning, SHM |
| 06-SMART-INFRA.md | Digital twins, IoT sensors, predictive maintenance, AI |
| 07-CLIMATE-ADAPTATION.md | Sea level, flooding, heat, adaptation strategies |
| 08-SECURITY.md | SCADA/ICS architecture, Stuxnet, NERC CIP, OT/IT |
| 09-GOVERNANCE.md | Ownership models, regulation, P3, funding mechanisms |

---

## Common Confusion Points

**"Infrastructure = buildings."** Infrastructure is the invisible systems that enable
everything else: pipes, wires, fiber, rails, roads. Buildings are connected to
infrastructure but are themselves structures, not infrastructure.

**"Resilience and reliability are the same thing."** Reliability is about performing
as expected under design conditions. Resilience is about recovering from unexpected
disruptions. A highly reliable bridge can be non-resilient (single point of failure);
a redundant, slightly less reliable network can be very resilient.

**"Aging infrastructure just means old infrastructure."** Age is a proxy for condition,
not condition itself. A 100-year-old bridge with proper maintenance can be in excellent
condition. A 20-year-old bridge with design defects and poor maintenance can be in
critical condition. Condition, not age, determines risk.

**"Infrastructure security is an IT problem."** IT security protects data. OT (operational
technology) security protects industrial control systems -- SCADA, PLCs, DCS -- that
physically operate infrastructure. Compromise of OT systems can cause physical harm:
blackouts, contaminated water, pipeline pressure surges. IT and OT security require
different approaches, different tools, and different expertise.
