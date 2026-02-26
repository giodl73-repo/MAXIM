# Infrastructure Resilience: Frameworks, Metrics, and Investment

## The Big Picture

Resilience is the capacity of infrastructure to absorb disruption, adapt to changed
conditions, and recover to full function. It is distinct from reliability (expected
performance) and security (resistance to threat). A highly reliable system designed for
normal conditions can be completely non-resilient to unexpected events.

```
RESILIENCE vs. RELIABILITY vs. ROBUSTNESS
==========================================

RELIABILITY:         Performs as expected under designed operating conditions
  "The bridge is rated for 40-ton trucks 99.9% of the time"
  Measured: MTBF, availability %, failure rate
  Threat: normal wear, component failure within design envelope

ROBUSTNESS:          Resists disruption without significant change in function
  "The bridge doesn't fail when hit by a 45-ton truck (above design)"
  Measured: factor of safety, excess capacity
  Threat: loads and hazards near or slightly above design

RESILIENCE:          Absorbs disruption, adapts, and recovers fully
  "The bridge is destroyed by a flood, but the region quickly restores
   connectivity via ferry service, then temporary bridge, then permanent bridge"
  Measured: time to recovery, functionality during disruption
  Threat: events well outside design envelope (surprises, Black Swans)

RELATIONSHIP:
  Reliability ensures normal operations
  Robustness prevents easy failure
  Resilience ensures recovery when failure occurs anyway
  All three are necessary; none is sufficient alone
```

---

## The Resilience Triangle

```
RESILIENCE TRIANGLE (Bruneau et al., 2003)
==========================================

                    DISRUPTION EVENT
                           |
   System         100%     |
   Functionality      -----+
   (%)            |        |
               80 +    ....+.........
                  |   .    |         ...........
               60 +  .     |                   ......
                  | .      |                         .........
               40 +.       |  LOSS OF FUNCTIONALITY       .....
                  |        |  (RESILIENCE TRIANGLE)            ..
               20 +        |                                     ..
                  |        |                                       ...
                0 +        |                                          .
                           t0 (event)                                   t1 (full recovery)
                                 TIME

FOUR DIMENSIONS (Bruneau):
  ROBUSTNESS:     Ability to withstand disruption (height of trough = 1 - robustness)
  REDUNDANCY:     Substitute resources exist during disruption (less deep trough)
  RESOURCEFULNESS: Capacity to mobilize resources in response (recovery slope)
  RAPIDITY:       Speed of recovery (time to full function = t1 - t0)

RESILIENCE MEASURE:
  R = integral(Q(t) dt, from t0 to t1) / (100% * (t1-t0))
  = fraction of "full functionality" actually delivered during disruption period
  Range: 0 (total loss, never recovers) to 1 (no impact)

  Better resilience: smaller triangle area (less lost functionality for less time)

FOUR WAYS TO IMPROVE:
  Higher robustness: withstand more -> shallower trough
  More redundancy: switch to backup faster -> shallower trough
  Better resourcefulness: better response -> steeper recovery
  Higher rapidity: faster recovery -> shorter duration (narrower triangle)
```

---

## ASCE Community Resilience Framework

```
ASCE INFRASTRUCTURE RESILIENCE FRAMEWORK (MOP 140)
====================================================

FOUR-R FRAMEWORK:

ROBUSTNESS:     Ability to absorb stress without catastrophic failure
  Design for excess capacity (factor of safety)
  Redundancy in critical systems
  Hardening against known hazards
  Example: bridge designed for 150% of expected load

RESOURCEFULNESS: Ability to manage disruption (human and material)
  Emergency planning and procedures
  Resource stockpiling (fuel, water, supplies)
  Mutual aid agreements (utility-to-utility assistance)
  Trained response personnel
  Example: city pre-positions 3-day generator fuel supply in critical facilities

RAPID RECOVERY: Speed of returning to normal function
  Pre-negotiated contracts with repair contractors
  Cached spare parts (transformers, pipes, generator parts)
  Clear decision authorities (who can authorize what spending)
  Community recovery plans
  Example: utility pre-orders one spare 345kV transformer (12-month lead time if not)

ADAPTABILITY: Learning and improving after events
  After-action reviews (AAR)
  Incorporating new hazard data (updated FEMA maps, climate projections)
  Updating design standards after failures
  Example: post-Sandy NYC hospitals elevated critical equipment from basement to roof

PROCESS:
  1. Characterize community (assets, population, hazards)
  2. Establish performance goals (what functionality, in what time, after what hazard)
  3. Assess vulnerability (what fails, when)
  4. Identify dependencies (what else fails when that fails)
  5. Develop plans (how to achieve performance goals)
  6. Implement and monitor
```

---

## Resilience Metrics

### Power Utility Metrics: SAIDI and SAIFI

```
POWER UTILITY RELIABILITY/RESILIENCE METRICS
============================================

SAIDI (System Average Interruption Duration Index):
  Average hours of power outage per customer per year
  SAIDI = sum(Customer Interruption Duration) / Total Customers Served
  Units: customer-hours / customer = hours/customer/year

  US average (2024): SAIDI ~ 5-8 hours/customer/year
    Without major events (SAIDI-MED): 2-4 hours
    With major events (hurricanes, ice storms): adds 2-6 hours

  Comparison by territory:
    Premium utilities (well-maintained, underground): 1-2 hours
    Average US utility: 5-8 hours
    Rural cooperative: 8-15 hours
    Developing world: 50-500 hours (Africa: some areas >200 hrs/yr)

SAIFI (System Average Interruption Frequency Index):
  Average number of interruptions per customer per year
  SAIFI = sum(Customer Interruptions) / Total Customers Served
  Units: interruptions/customer/year

  US average: SAIFI ~ 1.0-1.5 interruptions/customer/year

CAIDI (Customer Average Interruption Duration Index):
  Average time to restore power per outage event
  CAIDI = SAIDI / SAIFI (hours per interruption)
  US average: ~3-5 hours per outage event

MAIFI (Momentary Average Interruption Frequency Index):
  Frequency of short-duration interruptions (< 5 minutes)
  More sensitive to voltage sag, momentary interruptions

RESILIENCE METRICS (beyond standard reliability):
  Standard SAIDI doesn't capture extreme events well
  New metrics:
    Recovery time after extreme events (hurricane, ice storm)
    Percent of customers restored within 24 hr / 72 hr / 1 week
    "Longest customer outage" for equity analysis
    Infrastructure damage per event (repair cost as resilience measure)
```

### NIST Community Resilience Planning

```
NIST COMMUNITY RESILIENCE PLANNING GUIDE (NIST SP 1190)
=========================================================

PERFORMANCE GOALS FRAMEWORK:
  For each infrastructure system: define desired performance level at each hazard level

  HAZARD LEVELS:
    Routine hazard: expected several times per year
    Design event:   significant but within design basis (1% annual probability = 100-yr return)
    Extreme event:  beyond design basis (black swan, 0.1% annual probability)

  PERFORMANCE LEVELS:
    Continuous: no disruption (full function maintained)
    Disrupted but functional: reduced capacity but service continues
    Life safety: minimum function needed (no deaths from infrastructure failure)
    Damaged but repairable: function restored within days/weeks

  MATRIX EXAMPLE:
             ROUTINE        DESIGN EVENT      EXTREME
  HOSPITAL   Continuous     Full function     Life safety
  ROAD       Continuous     Life safety       Disrupted
  POWER      Continuous     Life safety       Damaged/repairable
  WATER      Continuous     Functional        Life safety

DEPENDENCY ANALYSIS:
  Map clusters: which buildings/systems are connected
  Critical nodes: failures that disconnect large portions
  Sequencing: restore in priority order (power first -> enables others)

RECOVERY TIME OBJECTIVES (RTO):
  Similar to IT disaster recovery but for physical infrastructure
  Water: restore within 72 hours for critical customers
  Power: restore within 24 hours for critical facilities; 1 week for all
  Communications: restore within 4 hours for emergency responders
  Transport: critical corridors within 48 hours
```

---

## Infrastructure Resilience Investment ROI

```
RESILIENCE INVESTMENT BENEFIT-COST ANALYSIS
=============================================

FEMA BRIC (Building Resilient Infrastructure and Communities) PROGRAM:
  Mitigation grants for pre-disaster infrastructure hardening
  Average benefit-cost ratio: $6 benefit per $1 invested
  (National Institute of Building Sciences analysis)

  Benefit calculation includes:
    Direct damage reduction (physical infrastructure saved)
    Business interruption avoided (economic output maintained)
    Lives saved (VSL: value of statistical life = $10-12M USDOT)
    Community disruption avoided (social costs)
    Long-term fiscal impact (tax base maintained)

  Examples:
    Elevating a water pump station: +$50k cost, avoids $300k average flood damage
    Burying overhead power lines: +$100k/km, reduces hurricane outage 80%, 50yr life
    Seismic retrofit of bridge: +$5M, avoids $100M+ replacement + 6 months closure

DEFERRED MAINTENANCE TRAP:
  Cost of fix NOW: $1M (current replacement)
  Cost of failure in 10 years: $5-10M (emergency replacement + outage costs)
  NPV of deferral "savings": negative at any reasonable discount rate >0%
  Why deferral happens: annual budget pressure wins over long-term NPV

  "Fix on fail" vs. "preventive maintenance" economics:
    Predictable failure rates: preventive usually wins (same job done once vs. emergency)
    Unpredictable failure: emergency response costs 3-5x planned maintenance
    Soft costs: outage economic impact often 10-100x physical repair cost

UTILITY EXAMPLE:
  Transformer replacement:
    Planned: $1.5M, 2-week planned outage
    Reactive (failure): $1.5M transformer + $500k emergency mobilization
                        + 4-week unplanned outage + $50M economic loss for customers
    Ratio: reactive / planned = ~35x

  SAIDI improvement economics:
    Reducing SAIDI from 6 hr to 4 hr:
      2 hr reduction * 1M customers = 2M customer-hours/year
      At $10-30/customer-hour value of reliability: $20-60M/year benefit
      Investment needed: $50-200M in distribution upgrades
      Payback: 1-10 years depending on cost estimates
```

---

## Resilience Standards and Frameworks

```
RESILIENCE FRAMEWORKS COMPARISON
===================================

FRAMEWORK              SECTOR      FOCUS             MANDATORY?
--------------------   ---------   ----------------  ----------
NERC CIP               Electric    Cybersecurity     YES (FERC)
NERC TPL               Electric    Physical N-1/N-2  YES (FERC)
AWIA 2018              Water       Risk assessment   YES (>3,300 service connections)
TSA SD-2021            Pipeline    Cybersecurity     YES (TSA directive)
NIST CSF               General     Cybersecurity     Voluntary (referenced widely)
NIST SP 800-82         ICS         OT security       Voluntary
ASCE 7 + 41            Structures  Seismic, wind     YES (building codes)
ASCE MOP 140           Community   Resilience plan   Voluntary
ISO 22316              General     Organizational    Voluntary
ISO 55000              Assets      Asset management  Voluntary
FEMA P-1024            Community   Resilience plan   Voluntary
NIST SP 1190           Community   Resilience plan   Voluntary

KEY GAPS:
  Long-duration blackout standard: no mandatory resilience requirement
    (utilities required to be N-1 reliable, not resilient to extended outages)
  Water utility cyber: AWIA mandates assessment, not specific controls
  Private sector (non-regulated): voluntary only (cloud providers, broadband)
  Cross-sector resilience: no mandatory interdependency analysis requirement
```

---

## Decision Cheat Sheet

| Resilience question | Answer |
|--------------------|--------|
| Key metric for power reliability | SAIDI (hours of outage / customer / year) |
| How is resilience different from reliability? | Reliability: normal conditions; resilience: unexpected disruption + recovery |
| What is the resilience triangle? | Functionality vs. time diagram: triangle area = total impact |
| What are the four Rs? | Robustness, Redundancy, Resourcefulness, Rapidity |
| Average FEMA mitigation ROI | ~$6 benefit per $1 invested |
| Why is deferred maintenance a trap? | Emergency repair 3-35x cost of planned; outage impacts multiply cost further |
| Is N-1 compliance the same as resilience? | No -- N-1 is for normal events; resilience addresses extreme/unexpected |

---

## Common Confusion Points

**"Resilience is just another word for redundancy."** Redundancy is ONE component of
resilience (Redundancy is one of the four Rs). A system can have redundant components
but poor resourcefulness (no response plan, no spare parts, no trained crews) and thus
be non-resilient despite redundancy.

**"High reliability means high resilience."** A highly reliable system designed for
narrow conditions can be extremely non-resilient to anything outside those conditions.
Swiss watchmaking precision (high reliability) doesn't help when a flood destroys the
entire factory (resilience requires adaptability and recovery, not just precision).

**"Resilience is expensive."** Some hardening investments are expensive. But resilience
also includes response planning, mutual aid agreements, pre-positioned spare parts, and
training -- often low-cost interventions with high return. The $6:1 FEMA BCR includes
the full range of measures, many of which are planning rather than capital investment.
