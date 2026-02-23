# 05 — Nuclear Safety Systems

## Defense in Depth, LOCA, Passive Safety, Accident Lessons

```
DEFENSE IN DEPTH — FIVE BARRIERS TO FISSION PRODUCT RELEASE

  ┌──────────────────────────────────────────────────────────────────────┐
  │  5. Containment Building (reinforced concrete, 1.5–2.0 m thick)     │
  │     ┌────────────────────────────────────────────────────────────┐   │
  │     │  4. Reactor Pressure Vessel (12 cm steel, 155 bar)         │   │
  │     │     ┌──────────────────────────────────────────────────┐   │   │
  │     │     │  3. Primary Coolant Boundary (piping, pumps, SGs) │   │   │
  │     │     │     ┌──────────────────────────────────────────┐  │   │   │
  │     │     │     │  2. Fuel Cladding (Zircaloy, 0.57 mm)    │  │   │   │
  │     │     │     │     ┌────────────────────────────────┐   │  │   │   │
  │     │     │     │     │  1. Fuel Matrix (UO₂ ceramic)  │   │  │   │   │
  │     │     │     │     │  retains ~99% fission products │   │  │   │   │
  │     │     │     │     └────────────────────────────────┘   │  │   │   │
  │     │     │     └──────────────────────────────────────────┘  │   │   │
  │     │     └──────────────────────────────────────────────────┘   │   │
  │     └────────────────────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────────────┘

Any accident must breach multiple independent barriers to cause a significant release.
Each barrier independently delays/reduces public dose. All must fail simultaneously for
a major release (very low probability — but Chernobyl and Fukushima demonstrated it's possible).
```

Nuclear safety philosophy is fundamentally about **defense in depth** (DiD): multiple
independent layers of protection such that no single failure or reasonable combination
of failures can lead to unacceptable consequences. This is not just redundancy —
it's heterogeneous, independent defense against independent failure modes.

---

## Defense in Depth Philosophy

### IAEA Safety Principles (SSR-2/1)

```
Level 1: Prevention of abnormal operation and failures
  → Good design, quality assurance, adequate margins, trained operators

Level 2: Control of abnormal operation and detection of failures
  → Control systems, protection systems, monitoring, alarms

Level 3: Control of design basis accidents
  → Reactor protection system (RPS), ECCS, emergency procedures
  → Prevents escalation of design basis events to severe accidents

Level 4: Control of severe plant conditions, including prevention of accident progression
  → Severe accident management guidelines (SAMGs), hydrogen recombiners
  → Core catchers, filtered containment venting

Level 5: Mitigation of radiological consequences of significant releases
  → Emergency planning zone (EPZ), evacuation planning, dosimetry
  → 10-mile EPZ (nuclear), 50-mile EPZ (ingestion pathway)
```

### Deterministic vs Probabilistic Safety

```
DETERMINISTIC (traditional, licensing-basis):
  Define design basis accidents (DBAs) by type/size
  Show safety systems can handle each DBA
  "Worst single failure" assumption: any one active component fails

PROBABILISTIC RISK ASSESSMENT (PRA):
  Model ALL accident sequences, not just DBAs
  Calculate frequencies and consequences
  CDF (Core Damage Frequency): target < 10⁻⁴/yr (Gen II), < 10⁻⁵/yr (Gen III+)
  LERF (Large Early Release Frequency): target < 10⁻⁵/yr

  Both required: deterministic for licensing (10 CFR 50.46), PRA for insights
  NRC Regulatory Guide 1.200: PRA technical adequacy standard
```

---

## Reactor Protection System (RPS)

### Trip Signals and Logic

```
RPS monitors reactor parameters → actuates SCRAM if limits exceeded

Typical trip signals:
  High neutron flux (power) → immediate
  High-high flux (fast rate trip) → immediate
  Low coolant flow → if power/flow ratio too high
  Low RCS pressure → if coolant boiling risk
  High RCS pressure → if structural limit approached
  High containment pressure → loss of coolant
  Low steam generator level → loss of feedwater event
  Safety injection signal (SIS) → automatic

2-out-of-4 logic (typical):
  Four independent channels measure each parameter
  Trip if any 2 of 4 channels exceed setpoint
  → Tolerates one spurious trip (no 1/4 single-point spurious shutdown)
  → Still trips on 1/3 (can detect incipient failure before demand)

SCRAM (rod trip): rods dropped by gravity in 1–2 seconds
  PWR: 48–88 control rod assemblies drop by gravity
  BWR: rods driven in by high-pressure nitrogen + gravity (from below)
  Reactivity insertion: ~7000 pcm in < 2 seconds → deep subcriticality

ATWS (Anticipated Transient Without Scram):
  ATWS = normal transient + failure to scram (stuck rods)
  PWR ATWS: high boron injection + turbine trip (10 CFR 50.62)
  BWR ATWS: recirculation pump trip + standby liquid control (boron/sodium pentaborate)
```

### Safety Injection Signal (SIS)

```
SIS actuated by: low RCS pressure (≤ 1724 psia), high containment pressure
Initiates:
  ECCS (Emergency Core Cooling System) actuation
  Reactor trip
  Containment isolation
  Emergency diesel generators start

Single failure criterion: ECCS must function with ONE active component failed
  → two trains, each independently capable
  → separation: different buildings, different power buses, different cooling
```

---

## Emergency Core Cooling System (ECCS)

### ECCS Subsystems (PWR)

```
HIGH PRESSURE INJECTION SYSTEM (HPIS):
  Trigger: RCS pressure < setpoint (~1750 psia)
  Source: RWST (Refueling Water Storage Tank) or IRWST
  Flow: ~1500 gpm per train
  Purpose: maintain core cooling before significant depressurization
  Effective for: small-break LOCA, steam line break, steam generator tube rupture

ACCUMULATORS (passive injection):
  Pressure: nitrogen-pressurized tanks at ~600 psia
  Volume: 4 × large tanks (4-loop PWR)
  Activation: passive — check valve opens when RCS drops below accumulator pressure
  Flow: very large (thousands of gpm)
  Purpose: core reflood during large-break LOCA blowdown → refill phase

LOW PRESSURE INJECTION SYSTEM (LPIS / LPSI / RHR):
  Trigger: RCS pressure < ~100 psia (fully depressurized)
  Source: RWST → sump recirculation (after ~20 min)
  Purpose: long-term core cooling after LOCA
  Shares trains with: Residual Heat Removal (RHR) for normal decay heat removal

Timing:
  0–30 s: HPIS actuates; accumulator check valves begin to crack
  30–200 s: LOCA blowdown; accumulators discharge
  200+ s: LPIS active; sump recirculation begins
  Core reflood complete: ~300–600 s → stable cooling
```

### ECCS 10 CFR 50.46 Criteria

```
Five acceptance criteria for large-break LOCA:

1. Peak Cladding Temperature (PCT): ≤ 1204°C (2200°F)
2. Maximum local cladding oxidation: ≤ 17% of total wall thickness
3. Total hydrogen generation: ≤ 1% of cladding as ZrO₂ (if all reacted with water)
4. Coolable geometry: core must remain geometrically coolable
5. Long-term cooling: ECCS provides sustained cooling after refill

Demonstrated by:
  LOCA analysis computer codes: RELAP5, TRAC, TRACE, GOTHIC
  Emergency Core Cooling System Evaluation Models (10 CFR 50, Appendix K)
  Conservative assumptions in licensing analysis (hot channel, minimum ECCS)
```

---

## Passive Safety Systems (Generation III+)

### AP1000 Passive Safety Philosophy

```
"Active" safety → requires: AC power, pumps, operator action, diesels
"Passive" safety → relies on: gravity, natural circulation, stored energy (compressed N₂), buoyancy

AP1000 passive safety:
  NO active ECCS pumps required
  72-hour grace period without ANY operator action or external power

PASSIVE CORE COOLING SYSTEM (PXS):
  CMT (Core Makeup Tanks): 2 × 70 m³ tanks, pressurized
    → driven by pressure differential; injects directly on SIS
  Accumulators: 2 × passive injection (N₂ pressurized)
  IRWST: 1700 m³ large tank inside containment
    → gravity drains through check valves when pressure drops sufficiently
    → provides gravity-injection for 72 hours
  ADS (Automatic Depressurization System): 4-stage depressurization
    → drops RCS pressure → allows accumulator + IRWST injection

PASSIVE CONTAINMENT COOLING (PCS):
  Water tank on top of containment building
  Gravity flow over steel containment shell → evaporative cooling
  Air inlet chimney + PCS water evaporation → removes heat by natural draft
  72+ hours on tank water; indefinite on air alone after tank depletion

  Heat removal capacity: >1 MW for long-term; adequate for decay heat
```

---

## Design Basis Accidents (DBAs)

### Large-Break Loss of Coolant Accident (LB-LOCA)

```
Initiating event: double-ended guillotine break of 2-foot diameter cold-leg pipe
  (PWR has cold-leg, cross-over leg, hot-leg; cold-leg break is worst case for ECCS)

Sequence:
  t=0: break opens; pressure wave propagates; flow reversal
  t<1s: SCRAM signal on low pressure; rods drop; fission power stops
  t=1-30s: BLOWDOWN — vessel depressurizes, core partially uncovered
       → decay heat with no cooling → clad temperature rises
       → PCT typically 900–1100°C during blowdown (Zr oxidation starts at ~950°C)
  t≈25s: HPIS and accumulators activate (accumulators at ~600 psia)
  t=30-200s: REFLOOD begins — water injection into lower plenum
       → quench front moves upward through core
       → PCT may peak here (~1200°C if marginal margin)
  t>200s: LPIS active; stable long-term cooling established

  KEY 10 CFR 50.46 LIMIT: PCT ≤ 1204°C
  Design margin: typical analysis shows PCT ≈ 1050–1150°C (150–350°C margin)
```

### Small-Break LOCA (SB-LOCA)

```
Initiating event: small pipe break, stuck-open PORV, steam generator tube rupture
  Flow out < HPIS makeup → slow pressure decrease

Challenges unique to SB-LOCA:
  Loop seal filling: liquid fills U-bend of steam generator coolant pipes
  → core uncovery possible even while loop seals remain full
  → natural circulation interrupted (no driving head if steam-filled hot legs)

  TMI-2 was an SB-LOCA (stuck-open PORV):
  → Pressurizer appeared FULL (but was actually an air/steam bubble)
  → operators thought HFP was normal → manually throttled HPIS!
  → core uncovered → severe fuel damage (~50% core damage)
  → no significant public health impact but dramatic loss of plant

  Post-TMI changes:
  → Added pressurizer level indication
  → Added subcooling monitors (shows how far from boiling — not just pressure)
  → Emergency Operating Procedures (EOPs) completely revised
  → Operator training on event-based AND symptom-based approaches
```

### Main Steam Line Break (MSLB)

```
Initiating event: steam line rupture between steam generator and turbine isolation valve
  → rapid cooldown of primary side
  → RCS temperature drops → reactivity increases (negative MTC → positive for cooldown)
  → if boron diluted (start of cycle, high enrichment) → possible return to criticality

  Design requirement: maintain subcriticality during MSLB with highest worth rod stuck out
  Control: SIS injects borated water; steam isolation valves close

Control rod ejection:
  Failed control rod assembly cover → ejection by pressure differential
  Rapid positive reactivity insertion → "stuck rod ejection" analyzed
  RPS trip on high flux → limits power excursion
  Fuel centerline temperature limit: no fuel pellet melting
```

---

## Probabilistic Risk Assessment (PRA)

### PRA Structure

```
Level 1 PRA: Core damage frequency (CDF)
  → Identifies combinations of failures that lead to core damage
  → Event trees + fault trees
  → CDF target: < 10⁻⁴/yr (existing plants), < 10⁻⁵/yr (Gen III+)

Level 2 PRA: Large early release frequency (LERF)
  → Given core damage, what is probability of large early release?
  → Models containment failure modes, severe accident progression
  → LERF target: < 10⁻⁵/yr

Level 3 PRA: Consequence analysis (off-site dose)
  → Given release, what are doses to population?
  → Used for emergency planning zone sizing
  → Not required for licensing but used for safety insights

Dominant accident sequences (typical PWR):
  Station blackout (SBO): 35–40% of CDF
  Loss of feedwater (LOFW): 10–15%
  Transients with ATWS: 5–10%
  LOCA: 10–15% (large break is rare; small break dominates)
  Interfacing systems LOCA: 2–5%
  Fire: 20–25% (major external hazard)
```

### PRA Insights and Uses

```
Risk-informed regulation (10 CFR 50.65, 50.69):
  → Allows relaxation of some deterministic requirements if low risk
  → Maintenance scheduling optimization (don't take both trains down simultaneously)
  → Importance measures: Fussell-Vesely, risk achievement worth (RAW)

  Fussell-Vesely (FV): fractional contribution to CDF if component fails
  RAW: how much CDF increases if component is unavailable

  High RAW + High FV → most risk-important components → most maintenance attention

Fire PRA:
  10 CFR 50.48 / NFPA 805: fire most important external hazard
  Cable fire → loss of multiple systems → must show diverse/redundant alternatives
  All plants required to have fire PRA by NRC
```

---

## Severe Accident Progression

### Core Damage Sequence

```
If core cooling fails (SBO + ECCS failure + ATWS):

  0–1 hr: Core uncovery begins; decay heat heats core
  1–2 hr: Fuel temperatures exceed 1204°C → Zircaloy oxidation accelerates
           Zr + H₂O → ZrO₂ + H₂ (exothermic, generates hydrogen)
           Fission gas release → clad failure → volatile FPs (I-131, Cs-137) released

  2–4 hr: Core damage → fuel collapse → corium (molten fuel + cladding + steel) forms
           Molten pool in lower head of RPV
           Lower head heats → potential RPV failure ("vessel melt-through")

  4–6 hr: REACTOR VESSEL FAILURE → corium falls to containment floor
           MCCI (Molten Core Concrete Interaction) → basemat attack
           → generates CO₂, CO, H₂O → containment pressurization
           → also: aerosol release of FPs into containment atmosphere

  6–12 hr: Containment pressurization → risk of:
           → Hydrogen detonation (if H₂ accumulates + ignites)
           → Overpressure failure
           → Steam explosion (if corium contacts water pool)

  Long-term: containment integrity determines offsite release
```

### Hydrogen Generation and Control

```
Sources of hydrogen in severe accidents:
  1. Zircaloy oxidation (primary source during in-vessel phase):
     Zr + 2H₂O → ZrO₂ + 2H₂   (1 kg Zr → 0.45 m³ H₂ at STP)
     Total in-vessel: ~1000 kg Zr in PWR core → up to 500 m³ H₂

  2. Core-concrete interaction (ex-vessel):
     Corium + concrete → CO₂ + CO + H₂O → reduces to H₂

  Hydrogen concentration in containment:
  Flammable if > 4% H₂ (lower flammable limit)
  Detonable if > ~18% H₂ (depending on O₂, steam concentration)

  Hydrogen control systems:
  Passive Autocatalytic Recombiners (PAR): Pd/Pt catalyst converts H₂ + O₂ → H₂O
    → no power needed, self-starting above ~50°C
    → PARs in all new designs (AP1000, EPR, APR-1400)
    → post-Fukushima retrofit required for existing LWRs
  Ignitors (deliberate): controlled burn at low concentration (< detonable)
    → TMI containment design: spark ignitors
  Hydrogen recombiners (catalytic): active (require power)
    → older systems, being replaced by PARs

  Fukushima: loss of PAR-equivalent led to H₂ buildup in reactor buildings
    Unit 1, 3, 4 (Unit 4 via exhaust duct) → hydrogen explosions
    → destroyed secondary confinement but NOT primary containment
```

### Core Catcher (Ex-Vessel Melt Retention)

```
Gen III+ designs include core catcher for in-vessel or ex-vessel melt retention:

  VVER-1200 / EPR: dedicated core catcher below RPV
    → corium flows into sacrificial material (iron oxide) → dilutes → solidifies
    → passive water cooling of catcher vessel

  AP1000: in-vessel melt retention (IVR)
    → Cool OUTSIDE of reactor vessel with cavity flooding
    → Natural circulation of water around lower RPV head
    → Heat removal path: corium → steel wall → water film → boiling
    → Must show RPV lower head thermally survives (critical heat flux not exceeded)
    → Works for AP1000 power level; may not scale to large EPR/VVER

  TMI-2: demonstrated ~50% core damage but NO reactor vessel failure
    → in-vessel melt retention occurred passively (water kept vessel cool)
```

---

## Major Nuclear Accidents

### Three Mile Island Unit 2 (1979) — USA

```
Event type: Small-Break LOCA (stuck-open PORV — pilot-operated relief valve)

Sequence:
  03:53 AM: Loss of feedwater → PORV opens (to relieve pressure surge) → correct
  03:53:05: PORV fails to reseat → small LOCA → coolant escapes through PORV
            PORV indicator shows "commanded closed" (not position indicator) → WRONG
  Operators see FULL PRESSURIZER → assume adequate cooling
  Operators TURN OFF HPIS (thinking they're in a solid-water transient) → WRONG
  ~2 hours: Core begins to uncover
  ~5 hours: Core severely damaged (~50% core melt); H₂ bubble in RPV
  No early containment failure; small H₂ explosion in containment (no damage)

Releases:
  ~17 Ci I-131 (small vs Chernobyl); no direct deaths
  Releases mostly noble gases; very small public health impact

Lessons learned:
  → Symptom-based EOPs (not just event-based): diagnose what's happening, not assume it
  → Subcooling monitoring required: know actual margin from boiling
  → Pressurizer level not sufficient: PORV position indicator required
  → Human factors in control room design: reduce alarm overload
  → Training revolution: NRC requirement for simulator training
  → Operator licensing requirements strengthened
  → Created Institute of Nuclear Power Operations (INPO) — peer review
```

### Chernobyl Unit 4 (1986) — USSR

```
Event type: Prompt criticality excursion + steam explosion

Context:
  RBMK-1000: graphite-moderated, water-cooled, positive void coefficient
  Safety test: testing emergency feedwater pump on turbine coastdown (low power)
  Operating at ~200 MWt (intended: 700 MWt; design: 3200 MWt) — dangerously low

Sequence:
  01:23:04 AM: Test begins; turbines disconnecting from grid
  01:23:40: AZ-5 SCRAM signal pressed
              PROBLEM: graphite tips on control rod bottoms INSERT BEFORE BORON
              → "positive scram" effect → brief reactivity addition at top of core
  01:23:43: Power excursion → ~30,000 MWt (~10× design)
  01:23:44-47: Two explosions: steam explosion + possible prompt criticality
              → Roof blown off; 1600-ton reactor lid lifted
              → Graphite fire begins (no containment at all)

Physics:
  At low power: positive void coefficient dominant; positive scram effect → catastrophic
  Post-accident investigation: RBMK fundamentally unsafe at low power
  → Operating staff had NO awareness of positive scram effect (classified information)

Releases: ~5 million Ci I-131; 70 million Ci noble gases
  27 acute radiation deaths (first responders); 28 early deaths
  ~6,000 thyroid cancers in children (mostly treatable); 15 deaths
  WHO estimate: ~4,000 excess cancer deaths total (upper range; uncertain)
  Liquidator radiation exposure: ~600,000 workers, varying doses

Lessons learned:
  → RBMK design fundamentally unsafe; retrofitted (but never fully fixed)
  → No reactor design may have a positive void coefficient without demonstrated safety
  → Secretive nuclear culture kills people: IAEA Convention on Nuclear Safety (1994)
  → Emergency planning zones revised globally
  → WANO (World Association of Nuclear Operators) created 1989 — peer review, no more isolation
```

### Fukushima Daiichi (2011) — Japan

```
Event type: Station blackout (SBO) from external event → hydrogen explosions → core melt

Context:
  March 11, 2011: Tōhoku earthquake (M9.0) + 15-meter tsunami
  All Units 1, 2, 3 operating; Units 4, 5, 6 in outage
  Reactors scrammed correctly on earthquake → fission stopped

Sequence:
  Unit 1: RCIC (isolation condenser) worked 8 hours then stopped; operators didn't notice
    → Core uncovered → fuel damage → H₂ generation
    → March 12: H₂ explosion in reactor building (secondary containment)
    → Containment NOT breached; damage to reactor building only

  Unit 3: RCIC/HPCI operated ~36 hours; SBO continued
    → Eventually operators lost track of system status
    → March 14: H₂ explosion, similar to Unit 1

  Unit 4 (shutdown): H₂ traveled via exhaust duct from Unit 3
    → March 15: explosion in Unit 4 spent fuel pool area
    → Spent fuel pool remained intact; no fuel damage in SFP

  Unit 2: RCIC worked longest; pressure relief valve stuck initially
    → Core damage but containment more intact (less H₂ release)

Releases:
  ~1/10 of Chernobyl release (much of ocean-deposited)
  ~900 km² exclusion zone (temporary); ~400 km² still restricted 2024
  No direct radiation deaths; 1 cancer death (worker) recognized
  Evacuation-related deaths: ~2,200 stress-related (indirect)

Why different from Chernobyl:
  BWR containment remained largely intact (pressure suppression)
  No prompt criticality (fission stopped by SCRAM immediately)
  No graphite fire
  Lower total release; ocean deposition reduced land contamination

Lessons learned:
  → FLEX strategy: portable ECCS equipment at all plants (NRC Order EA-12-049)
  → Hardened filtered containment vents required (remove H₂ + filter FPs)
  → Battery backup extended to 8 hours → 24 hours → 72 hours
  → Spent fuel pool monitoring/cooling backup required
  → Station blackout duration assumptions: 4 hours → extended to 72 hours
  → IAEA Fukushima Action Plan: all countries reviewed procedures
  → Japan: all reactors shut down 2011–2013 for review; restarts under new NRA regulator
```

---

## Post-Fukushima Requirements (FLEX)

```
NRC Order EA-12-049 (FLEX strategy):
  Flexible and diverse (FLEX) mitigation equipment:
  → Portable diesel generators, portable pumps, portable spray systems
  → Stored on-site and off-site (regional FLEX Support Centers)
  → Deployable within 8 hours

  Three-phase approach:
  Phase 1 (0–8 hr): Use existing installed systems (AC power if available)
  Phase 2 (8–72 hr): Deploy FLEX portable equipment on-site
  Phase 3 (72 hr+): Resupply from FLEX Support Center (2 centers: Raleigh NC, Phoenix AZ)

  All US plants required to implement FLEX by 2016
  European stress tests: similar requirements implemented across EU

New safety features post-Fukushima:
  → Spent fuel pool instrumentation (level, temperature)
  → Filtered containment venting (hardened vent + filter for FPs)
  → Emergency core cooling backup power (72-hour batteries)
  → Diverse and flexible coping strategies
  → Enhanced on-site emergency diesel fuel storage
```

---

## Radiation Protection

### Dose Limits

```
Radiation exposure limits (US NRC, 10 CFR 20):

  Occupational workers:
    Annual limit: 50 mSv/yr whole body  (NRC limit, TEDE)
    5-year average: 20 mSv/yr (ICRP recommendation, adopted by many countries)
    Lens of eye: 150 mSv/yr
    Extremities, skin: 500 mSv/yr

  Embryo/fetus (pregnant worker): 5 mSv for duration of pregnancy

  General public:
    Annual limit: 1 mSv/yr (excluding natural background + medical)
    Effluent release limit: 0.1 mSv/yr (10 CFR 50, Appendix I)

  Emergency workers:
    Life-saving actions: up to 250 mSv (voluntary, with informed consent)
    Protecting major property: up to 100 mSv

  Typical US nuclear power plant worker dose:
    ~1–3 mSv/yr (ALARA program keeps it low)
    Background radiation (US average): ~3 mSv/yr (0.94 natural + medical)
    Airline crew: ~3–4 mSv/yr (cosmic radiation)
```

### ALARA Principle

```
ALARA: As Low As Reasonably Achievable

  Not just meeting limits — continuous minimization

  Implementation:
  → Remote handling equipment (reduce hands-on time)
  → Shielding optimization: lead curtains, temporary concrete shields
  → Source term control: reactor water chemistry (CRUD buildup reduces dose)
    Zn addition (depleted zinc oxide) reduces CRUD activity on pipes/components
  → Scheduling: minimize time in radiation areas (time × dose rate = dose)
  → Dosimetry: real-time alarming dosimeters; TLD for record

  Collective dose (man-rem or person-mSv):
  PWR typical annual: 50–150 person-mSv (improved from 300+ person-rem in 1970s)
  BWR typically higher due to radioactive turbine area maintenance
```

### Effluent Control

```
Normal operation releases:
  Gaseous: Noble gases (Kr-85, Xe-133), H-3 (tritium), I-131 (tiny amounts)
    → all plants have charcoal delay beds, HEPA filters, holdup tanks
  Liquid: Tritium (T) most common liquid release; low-level process water
    → liquid radwaste processing: evaporation, ion exchange, filtering

  10 CFR 50, Appendix I limits:
  Design objective: ≤ 5 mrem/yr (0.05 mSv/yr) to any individual from liquid releases
  ≤ 5 mrem/yr from gaseous releases (excluding noble gases)
  Noble gas: ≤ 10 mrem/yr whole body

  Tritium controversy (2020s):
  TEPCO planned Fukushima treated water release (ALPS) → tritium in Pacific
  ~1300 TBq/yr release (less than ocean background; below WHO limits)
  Controversial despite meeting all international safety standards
```

---

## Common Confusion Points

**SCRAM stops fission — but not the danger:** Inserting all rods immediately reduces
reactor power from ~3000 MWt to near zero (fission). But DECAY HEAT continues at 6–7%
of full power for seconds, 1.5% for an hour. This is why you need ECCS and cooling
systems running long after SCRAM. Fukushima: SCRAM worked perfectly; decay heat
without cooling killed the plant.

**Containment did NOT fail at Fukushima:** The hydrogen explosions destroyed the reactor
BUILDINGS (secondary confinement, outer concrete structures). The primary containment
(torus/drywell — the inner steel structure) remained largely intact. If it had fully failed
early (like Chernobyl, which had none), the release would have been far larger.

**Defense in depth is not redundancy:** Redundancy = two of the same thing. DiD = multiple
qualitatively different barriers. UO₂ matrix, then Zr cladding, then RCS boundary, then
RPV, then containment — each different material, different failure mode, different chemistry.
Any one fails without cascading the others (usually).

**CDF < 10⁻⁵ does not mean "never":** With ~440 reactors operating for ~30 years,
expected number of events ≈ 440 × 30 × 10⁻⁴ ≈ 1.3 (for current Gen II fleet at 10⁻⁴).
Three major accidents (TMI/Chernobyl/Fukushima) in 17,000 reactor-years of operation
≈ 1.8 × 10⁻⁴/reactor-year, which is consistent with Gen II PRA estimates.

**Active vs passive safety:** Active = requires power, pumps, operator action (traditional ECCS).
Passive = gravity, natural circulation, stored pressure, convection (AP1000). Passive is MORE
reliable (fewer active components to fail) but has lower maximum heat removal capacity.
Neither is inherently "safer" — depends on design adequacy for the scenario.

---

## Decision Cheat Sheet

| Safety question | Concept | Key fact |
|----------------|---------|---------|
| How many barriers to release? | Five barriers (DiD) | Fuel matrix, clad, RCS, RPV, containment |
| What triggers SCRAM? | RPS trip signals | Low P, high flux, low flow, high containment P |
| ECCS timing after LOCA? | Three phases | HPIS (0-30s), accumulators (30-200s), LPIS (200s+) |
| PCT limit for large LOCA? | 10 CFR 50.46 | ≤ 1204°C; ≤ 17% cladding oxidation |
| Why does AP1000 not need pumps? | Passive safety | Gravity-driven IRWST; 72 hr without AC |
| What killed TMI-2? | SB-LOCA + operator error | Stuck PORV + throttled HPIS = core damage |
| Why did Chernobyl explode? | Positive α_void + RBMK scram effect | 30,000 MWt excursion at t+3s after SCRAM |
| Why did Fukushima release FPs? | SBO + H₂ explosions | Tsunami defeated AC power; decay heat uncovered core |
| What is FLEX? | Post-Fukushima portable equipment | Portable pumps/generators; 72-hr coping without external power |
| Worker dose limit? | 10 CFR 20 | 50 mSv/yr (NRC); 20 mSv/yr (ICRP 5-year avg) |
| CDF target Gen III+? | PRA Level 1 | < 10⁻⁵/yr (10× better than Gen II ~10⁻⁴/yr) |
