# Human Spaceflight: Physiology and Life Support

## The Big Picture

Human spaceflight is not just an engineering challenge — it's a biomedical engineering challenge. The human body did not evolve for microgravity, radiation, or sealed life support systems. Every system that keeps humans alive in space must work 100% of the time.

<!-- @editor[diagram/P2]: Diagram lists physiological challenges, life support systems, and radiation in columns without showing how they interact — bone loss drives exercise time which drives food/water/O2 consumption which sizes ECLSS; radiation constrains mission duration which constrains all other systems; rework as a dependency chain -->
```
+------------------------------------------------------------------+
|              HUMAN SPACEFLIGHT CHALLENGE MAP                      |
+------------------------------------------------------------------+
|                                                                  |
|  PHYSIOLOGICAL              LIFE SUPPORT               RADIATION |
|  CHALLENGES                 SYSTEMS                              |
|  ----------                 --------                  --------- |
|  Bone loss (2%/month)       O₂ supply/CO₂ removal    Van Allen  |
|  Muscle atrophy             Water recovery            Solar SEPs |
|  Fluid shift (headward)     Food (caloric + nutrition)GCRs       |
|  Vision changes (VIIP)      Waste management          Cumulative |
|  Immune suppression         Thermal control           dosimetry  |
|  Vestibular disruption      Fire suppression                    |
|  Psychological (isolation)  Pressure control                    |
|                                                                  |
|  MISSION DURATION:          VEHICLE SYSTEMS:                     |
|  LEO (ISS): up to 1 yr      Soyuz → Crew Dragon/Starliner       |
|  Lunar: ~14-30 days         Orion (Artemis) → Gateway           |
|  Mars: ~2-3 years           (Starship Mars concepts)            |
+------------------------------------------------------------------+
```

---

## Physiological Effects of Microgravity

### Bone and Muscle

```
MUSCULOSKELETAL EFFECTS
========================

  BONE LOSS:
    Rate: ~1-2% bone density per month (without countermeasures)
    Mechanism: without weight-bearing, bone remodeling shifts to resorption
    Primarily: lower limbs, lumbar spine, pelvis
    Calcium: excreted in urine; elevated urinary Ca²⁺ (kidney stone risk)
    Countermeasure: ~2 hrs/day vigorous exercise (ARED on ISS: Advanced Resistive Exercise Device)
    Recovery: months after return; some permanent loss after long durations

  MUSCLE ATROPHY:
    Rate: ~20% loss in lower limbs within 5-11 days without exercise
    Type I (slow-twitch endurance) fibers affected first
    Shift to less fatigue-resistant fiber types
    Countermeasure: combined aerobic + resistive exercise
    ISS protocol: 6 days/week exercise, 2+ hours/day including T2 (treadmill),
                  CEVIS (bike), ARED (weights)

  FLUID SHIFT:
    Earth: 70% of body fluid in legs (hydrostatic pressure)
    Microgravity: fluid redistributes toward upper body
    Facial puffiness + sinus congestion (common complaint, day 1)
    Leg circumference decreases ("bird legs")
    Cardiac output initially decreases → blood pressure adaptations
```

### Vision and VIIP

```
VISUAL IMPAIRMENT INTRACRANIAL PRESSURE (VIIP)
===============================================

  DISCOVERY: ~70% of long-duration astronauts show structural eye changes
  FIRST RECOGNIZED: ~2006-2010; now considered major concern for Mars

  MECHANISM:
    Fluid shift → increased intracranial pressure (ICP)
    → Optic disc swelling (papilledema)
    → Choroidal folds (retinal deformations)
    → Globe flattening (eyeball shape changes)
    → Hyperopic shift (farsightedness increases)
    → In some: permanent visual impairment on return

  SEVERITY SPECTRUM:
    Grade 1: Cotton wool spots on retina; minimal symptoms
    Grade 2: Optic disc edema, some visual field loss
    Grade 3-4: Significant visual impairment (rare but documented)

  MONITORING: Regular ophthalmologic exams; Optical Coherence Tomography (OCT)
  COUNTERMEASURES: None definitively effective yet; lower-body negative pressure
                   (LBNP) draws fluid down; under study

  MARS CONCERN:
    ~3-year mission; 6 months transit + 18 months surface + 6 months return
    VIIP could accumulate to disabling levels
    No return possible if vision deteriorates in transit
    Critical unresolved problem for Mars human mission safety
```

---

## Radiation Exposure

```
RADIATION DOSIMETRY IN SPACE
==============================

  DOSE UNITS:
    Gray (Gy): absorbed energy per unit mass (J/kg)
    Sievert (Sv): effective dose = Gy × quality factor (accounts for biological damage)
    Quality factors: photons/electrons = 1; protons = 2-5; heavy ions = 20

  DOSE RATES:
    LEO (ISS, 51° incl.): ~0.3-1 mSv/day (vs 0.01 mSv/day on Earth surface)
    ISS annual: ~100-150 mSv/yr (vs Earth 2-3 mSv/yr average)
    GEO: ~3-5 mSv/day (higher; more Van Allen exposure)
    Interplanetary: ~1.8 mSv/day (outside Earth's magnetic field)
    Solar particle event (SPE): can add 100s mSv in hours
    Mars surface: ~0.67 mSv/day (with atmosphere shielding; no magnetic field)

  CUMULATIVE DOSE LIMITS (NASA):
    Career limit: 3% excess lifetime risk of cancer (statistical)
    Translates to: ~400-800 mSv career limit depending on age + sex
    Single year limit: ~50 mSv (as low as reasonably achievable, ALARA)
    Mars round trip: ~700-1200 mSv (exceeds career limits under current rules!)

  SHIELDING:
    Adding mass helps against energetic particles but:
    GCRs: secondary radiation from heavy ions hitting shielding is worse than primary
    Optimal shielding: hydrogen-rich material (polyethylene, water, food stores)
    Spacecraft walls: adequate for solar wind; insufficient for GCRs
    Water wall concept: surround habitat with water tanks (also life support!)

  COUNTERMEASURE RESEARCH:
    Pharmaceutical: antioxidants, DNA repair enhancers; no approved protocol
    Timing: fly during solar maximum (GCR minimum) + shelter during SPEs
    SPE shelter: high-mass central core of spacecraft (storm shelter)
```

---

## Life Support Systems (ECLSS)

```
ENVIRONMENTAL CONTROL AND LIFE SUPPORT SYSTEM (ECLSS)
=======================================================

  ATMOSPHERE MANAGEMENT:
    O₂ generation: Oxygen Generation Assembly (OGA) — electrolysis of water
    H₂O → H₂ + ½O₂; O₂ into cabin; H₂ to Sabatier system or vented
    Pressure control: N₂ supply; maintain 14.7 psi (101 kPa) total; 21% O₂
    (Or: 100% O₂ at 34.5 kPa — early Apollo; fire risk)

    CO₂ removal: Carbon Dioxide Removal Assembly (CDRA)
    Zeolite beds (adsorbent); alternating beds to regenerate
    Target: < 5 mmHg CO₂ partial pressure (above this: headaches, impairment)
    Problematic at high crew levels: CO₂ buildup on ISS occasionally exceeds limits

    Sabatier Reactor:
    CO₂ + 4H₂ → CH₄ + 2H₂O
    Recovers water from H₂ waste stream; methane vented
    Closes the water loop partially

  WATER RECOVERY:
    Urine Processor Assembly (UPA): distills urine → brine
    Water Recovery System (WRS): processes brine + condensate → potable water
    Current efficiency: ~85-93% (some water still lost in brine)
    Future goal: 98%+ (closed loop)
    Without recovery: need ~3 kg/person/day resupply (for drinking, hygiene, food)
    With recovery: significantly reduced resupply mass

  FOOD:
    ISS: ~3000 kcal/person/day from packaged food (irradiated, thermostabilized)
    Shelf life: 1-3 years
    Currently: all food brought from Earth; no in-flight production
    Mass: ~2 kg/person/day (food + packaging)
    Taste: reported as blander; fluid shift reduces sense of smell/taste
    XROOTS experiment: growing plants on ISS; romaine lettuce eaten on ISS (2015)

  WASTE MANAGEMENT:
    Solid waste: sealed in bags; stored; returned or burned on reentry (cargo vehicle)
    Urine: collected; processed to water
    Microbial control: constant HEPA filtration; surface wipe-downs with biocides
    Atmosphere: continuous filtration; VOC removal; CO₂ primary concern
```

---

## Spacecraft Vehicle Systems

### Soyuz (1967-present)

```
SOYUZ MS CREW CAPSULE
======================

  CREW: 3 (sometimes 2 with cargo)
  LAUNCH VEHICLE: Soyuz-2.1a
  DURATION: up to 6 months docked to ISS; 3.5-hour ascent; 3.5-hour descent

  MODULES:
    Orbital Module (OM): habitable during approach/departure; 5 m³
    Descent Module (DM): crew ride during ascent + descent; 3.5 m³
    Instrument/Service Module (SM): propulsion + solar panels; non-habitable

  RE-ENTRY + LANDING:
    Ballistic re-entry (not lifting body)
    Parachutes + retrorockets for landing (Kazakhstan steppe)
    Solid rocket braking motors fire just before impact (1m altitude)
    ~3.5G peak deceleration
    First operational capsule design still in service (updated avionics)

  LEGACY:
    Most reliable human spacecraft ever (99.9%+ crew survival rate)
<!-- @editor[content/P1]: Claim may be incorrect — verify: Scott Kelly is American (NASA), not Russian; listing him under "Russian record" is misleading; the 342-day ISS mission was a joint US-Russia experiment but Kelly is a US astronaut -->
    Russian record: Valeri Polyakov, 437 days (1994-1995); Scott Kelly + Mikhail Kornienko, 342 days (2015-2016)
```

### SpaceX Crew Dragon

```
SPACEX CREW DRAGON
===================

  CREW: up to 7; typically 4 for ISS missions
  LAUNCH VEHICLE: Falcon 9
  REUSE: Capsule reused (3+ flights demonstrated); trunk discarded

  KEY FEATURES:
    Fully automated docking (no manual options required)
    Touch-screen interface (significant departure from toggle switches)
    Abort system: 8 SuperDraco engines in capsule wall (pusher, not tower)
    Can abort at any point during ascent (all-altitude abort capability)
    Seats: custom-molded to each crew member
    Life support: N₂/O₂ atmosphere; 14.7 psi

  FIRST OPERATIONAL FLIGHT:
    Demo-2: May 30, 2020 — first crewed commercial orbital flight
    Crew-1: November 2020 — first operational commercial crew to ISS

  ABORT SYSTEM:
    SuperDraco: hypergolic (NTO/MMH); 71 kN each × 8 = 568 kN total
    Pusher design (no tower to jettison)
    In-flight abort demonstrated successfully Oct 2019 (maximum dynamic pressure)
```

---

## EVA (Extravehicular Activity)

```
SPACEWALK (EVA) SYSTEMS
========================

  PURPOSE:
    Repair/maintenance (Hubble servicing, ISS maintenance)
    Construction assembly (ISS built by 200+ EVAs)
    Science (JAXA experiments outside ISS)
    Exploration (Moon surface operations)

  EMU (Extravehicular Mobility Unit) — ISS spacesuit:
    Upper Torso + Lower Torso + Gloves + Helmet + PLSS (backpack)
    PLSS: Primary Life Support System
      O₂ supply: 8+ hrs operational; 30 min consumable O₂ emergency
      CO₂ removal: lithium hydroxide canisters
      Water cooling: 1 liter/hr to undergarment cooling system
      Pressure: 29.6 kPa (4.3 psi) pure O₂ (much lower than cabin)
      Communications, displays, biosensors

  PREBREATHE PROTOCOL:
    Cabin: 14.7 psi, 21% O₂ → 2.1 psi partial O₂
    Suit: 4.3 psi pure O₂
    Problem: nitrogen dissolved in blood at 14.7 psi → if suddenly at 4.3 psi,
             nitrogen comes out of solution → decompression sickness (bends)
    Protocol: breathe 100% O₂ for 4 hours before EVA to purge N₂ from tissues
    Alternative: campout at 10.2 psi for 24 hours first
    ISS typically: 4-hour pre-breathe in suit

  LUNAR SURFACE SUIT (Artemis xEMU / Axiom suit):
    Designed for 1/6 G on lunar surface; mobility for sampling, climbing
    Dusty regolith: critical challenge; suits must seal against lunar dust
    Lunar dust: sharp, electrostatically charged, sub-micron particles
                Sticks to everything; abrasive; potential health hazard
    New suit features: hip and waist mobility; improved glove dexterity

  DURATION: Typically 6-8 hours; record is 8hr 56min
```

---

## Long-Duration Mission Challenges

```
MARS MISSION REQUIREMENTS
===========================

  TIMELINE:
    Transit Earth → Mars: 6-9 months (minimum energy)
    Mars surface stay: 14-20 months (conjunction class) or 30-90 days (opposition)
    Transit Mars → Earth: 6-9 months
    Total: ~2.5-3 years (conjunction class preferred for crew health)

  CUMULATIVE PHYSIOLOGICAL CHALLENGES:
    Bone loss: mitigation critical; resistive exercise but limited gravity on Mars
    VIIP: 3 years of ICP elevation; unknown outcome at mission end
    Radiation: ~700-1200 mSv (exceeds current career limits)
    Muscle: Mars 1/3 G partially helps vs full microgravity transit
    Psychological: isolation, 3-22 minute delay (no real-time communication), confinement

  COMMUNICATION DELAY:
    Mars: 3-22 minute one-way (6-44 min round trip)
    No real-time mission control support for emergencies on Mars
    Crew must be fully autonomous for medical, engineering, operations
    Mental health: loss of instant communication with family/friends; critical

  AUTONOMOUS MEDICAL CARE:
    No evacuation possible from Mars surface
    All medical situations (surgery, diagnosis) must be handled on-board
    Telemedicine with 22-min delay; remote guidance possible but not real-time
    Crew medical training: much more extensive than ISS crews
    Stock: surgical tools, medications, diagnostic equipment; mass-constrained

  FOOD FOR MARS:
    Not feasible to carry 3 years of food (mass)
    Bioregenerative life support: grow food on Mars / in transit
    VEGGIE/AstroGarden (ISS): lettuce, radishes, peppers grown; eaten on ISS
    Required for Mars: caloric closure (not just supplements from plants)
    Estimated: ~10-50 m² growing area for caloric supplement; more for full diet
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is the single most dangerous unresolved issue for Mars? | VIIP/ICP: ~70% of ISS astronauts show eye changes; 3-year Mars mission may cause permanent visual impairment; no effective countermeasure yet |
| Why is bone loss a problem even with exercise? | Exercise mitigates but doesn't eliminate bone loss; current ISS protocols reduce loss to ~0.5-1%/month in weight-bearing bones; Mars surface (1/3 g) may partially help |
| What are the radiation career limits and how does Mars compare? | NASA career limit: ~400-800 mSv (3% excess cancer risk); Mars round trip: ~700-1200 mSv — exceeds limits under current rules; either limits must be revised or shielding improved |
| Why must EVA suits operate at 4.3 psi pure O₂? | Lower pressure = easier suit mobility (less like a balloon); 4.3 psi × 100% O₂ = same O₂ partial pressure as sea level; but requires nitrogen pre-breathe to avoid bends |
| What is ECLSS? | Environmental Control and Life Support System: integrates atmosphere management (O₂ gen, CO₂ removal), water recovery, pressure control, and thermal control |
| What is the record for continuous time in space? | Valeri Polyakov: 437 days (1994-1995) on Mir; longest single mission; demonstrated survival of >1 year mission but with significant recovery time needed post-flight |
| Why is communication delay psychologically significant for Mars? | Up to 44-minute round-trip delay means no real-time conversation with family, friends, or mission control; crew must be psychologically self-sufficient for 3 years |

---

<!-- @editor[bridge/P2]: No old-world bridge — natural parallel: ECLSS closed-loop resource management (O2 generation, CO2 scrubbing, water recovery at 93% efficiency) is the same feedback-control pattern as capacity planning in distributed systems (resource pools, recycling, degradation rates, margin budgets); the learner managed Azure capacity at scale -->
## Common Confusion Points

**Exercise countermeasures do not fully prevent bone loss**: 2 hours of daily vigorous exercise on ISS reduces but doesn't eliminate bone loss. Astronauts typically lose 1-2% per month in critical load-bearing bones even with exercise. The mechanisms of bone remodeling in microgravity are not fully understood.

**Radiation is not the biggest immediate risk**: Day-to-day on ISS, the crew is exposed to elevated radiation but not immediate danger. The cumulative risk is statistical (cancer risk increase) not acute. Solar particle events can be dangerous but are predictable enough for shelter. GCRs are the chronic problem for deep space.

**The ISS is not a good analog for Mars**: ISS operates in LEO with immediate emergency evacuation available (Soyuz can return in 3.5 hours). ISS has real-time mission control communication (< 1 sec delay). ISS food is resupplied regularly. None of these apply to Mars. ISS research informs Mars planning but doesn't simulate Mars conditions.

**Microgravity and weightlessness are the same thing, but gravity is not zero**: At ISS altitude (408 km), Earth's gravitational acceleration is ~89% of sea-level value. The crew is in free fall, experiencing apparent weightlessness. The term "zero-g" is technically incorrect; "microgravity" is preferred (residual differential gravity across the spacecraft volume causes very small tidal forces).
