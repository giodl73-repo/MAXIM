# Electrical Grid — Distribution Systems
## Last-Mile Delivery: From Substation to Meter

---

## The Big Picture: Distribution System Hierarchy

```
TRANSMISSION GRID (69–500 kV)
        │
        │ Bulk Power Transformer (e.g., 230/69 kV, or 115/12.47 kV)
        │
┌────────────────────────────────────────────────────────────────────────────┐
│   DISTRIBUTION SUBSTATION (boundary between transmission & distribution)   │
│   Typical: 69 kV or 115 kV → 12.47 kV (most common US) or 34.5 kV          │
│   Equipment: Power transformer(s), circuit breakers, protective relays,    │
│              bus, capacitor banks, voltage regulators, SCADA               │
└──────────────────────────────────┬─────────────────────────────────────────┘
                                   │
        Primary distribution feeders (12.47 kV three-phase, 3-wire or 4-wire)
                                   │
   ┌──────────────────────────────────────────────────────────┐
   │         PRIMARY DISTRIBUTION FEEDER (~8 miles average)   │
   │  OH/UG conductors, reclosers, sectionalizing switches,   │
   │  capacitor banks, voltage regulators, laterals           │
   └───┬──────────────────┬────────────────────┬──────────────┘
       │                  │                    │
       ▼                  ▼                    ▼
   Pole TX            Pad TX              Network vault TX
   Single phase       3-phase             (urban)
   5-100 kVA          25-500 kVA          120/208V dense urban
   120/240V           208/480V            network
   Residential        Commercial/Ind.
   single-phase       three-phase
```

---

## Distribution Substation: The Grid Gateway

The distribution substation is where transmission ends and distribution begins. It's the most common substation type by count (thousands in a US utility territory vs dozens of transmission substations).

### Typical Configuration

```
DISTRIBUTION SUBSTATION — ONE-LINE DIAGRAM (simplified):

  115 kV from transmission ────────────────────────────────
                              |                    |
                            [OCB]                [OCB]      115 kV breakers
                              |                    |        (Oil/SF₆ Circuit Breaker)
                  115 kV Bus ─┴────────────────────┘
                              |
                       ┌──────────────┐
                       │  115 kV /    │
                       │  12.47 kV    │
                       └──────┬───────┘
                          (Power transformer, e.g., 50 MVA)
                              |
              12.47 kV Bus ───┴───────────────────────
                        |         |         |         |
                      [OCB]     [OCB]     [OCB]     [OCB]   Feeder breakers
                        |         |         |         |
                    Feeder 1  Feeder 2  Feeder 3  Feeder 4
                    (to NE)   (to NW)   (to SE)   (to SW)

KEY EQUIPMENT:
  Power transformer: 25–300 MVA, with OLTC (on-load tap changer) for voltage regulation
  OLTC: steps through ±16 taps of ±1.25% each → ±20% voltage range adjustment
  Breakers: modern SF₆ puffer or vacuum types; can interrupt 20-50 kA fault current
  Protective relays: overcurrent (51), distance (21), transformer differential (87T)
  SCADA RTU: reports status to utility operations center every 2-4 seconds
  Battery: 125V DC station battery for relay/breaker operation during power loss
  Capacitor banks: 600 kVAR to 10 MVAR, switchable, for voltage/VAR support
```

**Substation automation:** Modern substations have IEDs (intelligent electronic devices) following IEC 61850 standard. The IEDs communicate via GOOSE (Generic Object Oriented Substation Event) messages — deterministic, < 4ms delivery for protection applications. Digital substations are replacing analog meters and hardwired relay logic with software-defined protection and Ethernet communications.

---

## Primary Distribution Voltages

Different voltages around the world, with trade-offs:

| Voltage | Markets | Feeder Radius | Capacity | Notes |
|---------|---------|--------------|---------|-------|
| 4.16 kV | Legacy US urban | 1–3 miles | Low | Very old; being eliminated |
| 12.47 kV (7.2 kV phase-ground) | US (most common, ~60%) | 5–15 miles | 10–30 MW | Phase-to-phase/phase-to-neutral |
| 13.2 kV | Some US | 5–15 miles | 10–30 MW | Close to 12.47 in practice |
| 25 kV | Rural US, Canada | 15–40 miles | 20–50 MW | Two-step down required |
| 34.5 kV | Large US industrial | 10–30 miles | 40–80 MW | Often for large commercial loads |
| 11 kV | UK, Australia, Asia | 5–10 miles | 8–20 MW | UK standard |
| 6.6 kV | Japan | 3–8 miles | Low | Japan standard (being upgraded) |
| 20 kV | France, Germany | 8–15 miles | 15–35 MW | Common in continental Europe |

**Why 12.47 kV dominates US:** It's a legacy of the 7.2/12.47 kV class insulation evolution from earlier 4.16 kV systems. Most US utilities standardized on this through the 1950s–1970s and the infrastructure investment keeps it dominant. The 12.47 kV (phase-to-phase) = 7.2 kV (phase-to-neutral) design allows single-phase laterals to tap off individual phases at 7.2 kV to single-phase distribution transformers.

---

## Feeder Design: Radial, Loop, and Network

The feeder topology progression — radial (N), loop (N+1), network (2N) — mirrors datacenter power path redundancy: radial = single path, any fault = outage; loop = alternate path available; network = fully meshed with multiple simultaneous paths. The same reliability vs. cost trade-off applies.

```
1. RADIAL FEEDER (most common US suburban/rural):

   Substation
      │
    ┌─┴──────────┬─────────────┬────────────────┐
    │            │             │                │
   Load         Load          Load            Load
    │
   (each load has exactly ONE path from substation)

   ADVANTAGE: Simple, cheap, easy protection (one-directional current flow)
   DISADVANTAGE: Any single fault = outage for all downstream customers
   RELIABILITY: SAIDI ~100-300 min/yr
   USE: Low-density residential and rural areas

2. LOOP FEEDER (common US suburban):

   Substation
      │
    ┌─┴──────────────────────────────────┐
    │                                    │ Normally-Open switch (NO)
    │                                    │
   Loads along feeder A            Loads along feeder B

   During normal: open switch at midpoint, each feeder serves its section
   During fault on feeder A: open at fault, close NO switch → feeder B serves both
   Customer restoration: 30-60 minutes (manual) to ~30 seconds (automated FDIR)

   ADVANTAGE: Much better reliability than radial
   DISADVANTAGE: 2× the feeder infrastructure cost
   COMMON PATTERN: Residential subdivisions, commercial corridors

3. NETWORK (GRID) DISTRIBUTION (urban centers only):

   ┌────────────────────────────────────────┐
   │Substation A│  │Substation B│  │Sub C│  │
   └──┬──────────────────┬───────────┬──────┘
      │    ╔═════════╗   │    ╔══╗   │
      ├────╣ Network ╠───┤    ║  ║   ├──── loads
      │    ║ protector║   │    ╚══╝   │     (served from multiple
      ├────╣ (NP)    ╠───┤           │      directions)
      │    ╚═════════╝   │           │
      │                  │           │
   Network Bus ──────────────────────────────
   (low voltage, 120/208V or 265/460V)
      │
   Load loads loads loads loads (restaurants, offices, apartments)

   Network protectors (NP): automatic switches that allow power to flow
   from transformer to network bus but not reverse (prevents backfeed)

   ADVANTAGE: Extremely reliable — any single transformer failure → no customer outage
              (multiple paths → automatic switching)
   DISADVANTAGE: Very expensive (multiple transformers, network protectors)
   USE: Manhattan, downtown Chicago, downtown DC — dense urban with 24/7 critical loads
   RELIABILITY: SAIDI < 30 min/yr in mature network areas
```

---

## Distribution Transformers

The final voltage step-down to customer service voltage. There are approximately 100 million distribution transformers in the US.

### Types

```
POLE-MOUNTED SINGLE-PHASE (US rural/suburban):
  ┌──────────────┐
  │  [XFMR]      │
  │  25 kVA      │
  │  7200/120-240│
  └──────┬───────┘
  Mounted on distribution pole (5-167 kVA typical range)
         │ Service drop (to house)
         ▼ 120/240V split-phase
  Three wires to meter:
    L1: 120V to neutral (top half of 240V)
    L2: 120V to neutral (bottom half of 240V)
    N: neutral (center tap of secondary)
  → 240V for ranges, dryers, EV chargers
  → 120V for receptacles and lighting
  Serves: 2-10 houses typically (varies)

PAD-MOUNTED THREE-PHASE (commercial/industrial):
  Ground-level, padlocked steel enclosure
  Typically: 75-2,500 kVA
  Primary: 12.47 kV (loop-feed — cable enters and exits, allowing bypass)
  Secondary: 480/277V three-phase 4-wire (most commercial) or 208/120V
  Oil-filled: mineral oil immersed core and coils
  Standard: IEEE C57.12.34

NETWORK VAULT TRANSFORMER (dense urban):
  Below-grade vault installation (under sidewalk)
  Primary: 13.8 kV or 4.16 kV
  Secondary: 265/460V (commercial network) or 120/208V (residential network)
  "Network protector" integral or adjacent
  Submerged in periodic flooding → special insulation systems
```

### Distribution Transformer Efficiency

US DOE standards (10 CFR 431) for pole-mounted transformers:
- 25 kVA single-phase: ≥ 98.0% efficiency at full load
- 100 kVA single-phase: ≥ 98.7%
- 500 kVA three-phase: ≥ 99.0%

These look good but the loss accumulates over millions of units. The US has ~100M distribution transformers. If average loss = 1.5% × average loading of 30% = 0.45% of rating wasted continuously. Total waste: significant GW-scale power loss.

**Amorphous metal core transformers:** Using amorphous rather than grain-oriented silicon steel reduces core losses by 70-80%. More expensive upfront ($50-100 extra per unit) but pays back in energy savings. Increasingly mandated in DOE efficiency standards.

---

## Secondary Service Configurations

Different service voltages serve different needs:

```
US SERVICE VOLTAGE CONFIGURATIONS:

1. RESIDENTIAL (single-phase, split-phase):
   ●──────────────────────────── L1 (hot): 120V to neutral, 240V to L2
   ●──────────────────────────── N (neutral): 0V
   ●──────────────────────────── L2 (hot): 120V to neutral, 240V to L1
   → 120V: wall outlets, lights, small appliances
   → 240V: range, dryer, AC, water heater, EV Level 2 charger

2. SMALL COMMERCIAL (three-phase, 4-wire wye, 120/208V):
   Phase A: 120V to neutral ─┐
   Phase B: 120V to neutral  ├─▶ 208V phase-to-phase
   Phase C: 120V to neutral ─┘
   Neutral: 0V
   → 120V single-phase: outlets, lighting
   → 208V: small three-phase motors, small HVAC
   → Used: small offices, retail, restaurants

3. COMMERCIAL/INDUSTRIAL (three-phase, 4-wire wye, 277/480V):
   Phase A: 277V to neutral ─┐
   Phase B: 277V to neutral  ├─▶ 480V phase-to-phase
   Phase C: 277V to neutral ─┘
   → 277V: fluorescent/LED commercial lighting (277V ballasts common)
   → 480V three-phase: large motors (HVAC, elevators, industrial machines)
   → Often add 120V via separate transformer (K-rated) for outlets/IT
   → Used: offices, hospitals, warehouses, factories

4. LARGE INDUSTRIAL (> 5 MW demand):
   Often served at primary voltage (12.47 kV, 34.5 kV, or higher)
   Customer-owned substations with their own transformers
   Utility responsibility ends at the primary voltage meter
```

---

## Reliability Metrics: SAIDI, SAIFI, CAIDI

These are the universal metrics for distribution reliability, mandated by NERC and state PUCs.

### Definitions

```
SAIDI = System Average Interruption Duration Index
      = Σ(Customer Interruption Durations) / Total Customers Served
      Units: minutes per customer per year
      Measures: how many minutes, on average, each customer is without power

SAIFI = System Average Interruption Frequency Index
      = Total Customer Interruptions / Total Customers Served
      Units: interruptions per customer per year
      Measures: how often, on average, each customer loses power

CAIDI = Customer Average Interruption Duration Index
      = SAIDI / SAIFI
      = Average duration of each outage
      Units: minutes per interruption
      Measures: once an outage starts, how long does it take to restore?

MAIFI = Momentary Average Interruption Frequency Index
      = Total Momentary Interruptions / Total Customers Served
      Measures: recloser operations (brief < 1 minute interruptions)
      Not always reported; matters for sensitive equipment
```

### Typical Values

```
RELIABILITY BENCHMARKS (US utilities, SAIDI minutes/yr, excluding major events):

Top Quartile (suburban, underground, automated):
  SAIDI: 30–60 min/yr
  SAIFI: 0.5–0.8 interruptions/yr
  CAIDI: 60–90 min

Middle (typical suburban OH):
  SAIDI: 100–180 min/yr
  SAIFI: 1.0–1.5
  CAIDI: 80–120 min

Lower Quartile (rural, aging infrastructure):
  SAIDI: 250–400 min/yr
  SAIFI: 2.0–3.0
  CAIDI: 100–150 min

Including Major Event Days (MED — storms, ice, wildfires):
  Can triple SAIDI in some years
  Utilities often report separately: "SAIDI excluding MEDs"

INTERNATIONAL COMPARISON (approximate):
  Japan:       SAIDI ~4 min/yr (exceptional — densely undergrounded, aggressive maintenance)
  South Korea: SAIDI ~12 min/yr
  Germany:     SAIDI ~15 min/yr
  UK:          SAIDI ~45 min/yr
  USA average: SAIDI ~110 min/yr (excluding MEDs)
  Puerto Rico (pre-Maria): ~200 min/yr; post-Maria recovery: years of issues
```

**Why does Japan achieve SAIDI ~4 min/yr?** Very high underground cable penetration (>70% urban), aggressive vegetation management, aggressive equipment replacement programs, and granular fault isolation (many sectionalizing switches). The cost is high — underground distribution is 5-10× more expensive than overhead per km.

### Causes of Outages

```
TYPICAL SAIDI CONTRIBUTION BY CAUSE (US, IEEE 1366 reporting):

Equipment failure (transformers, cables, connectors): ~20-25%
  Aging equipment; thermal overload; insulation degradation

Tree contact / vegetation:                           ~30-35%
  Branches fall on lines; trees fall; storm damage

Other overhead line (animals, vehicles, etc.):       ~15-20%
  Squirrels, raccoons shorting at transformer;
  cars hitting poles; vandalism; kite strings

Lightning:                                           ~10-15%
  Direct strikes; flashover; induced surges

Planned outages (maintenance):                       ~5-10%
  Scheduled switching, equipment work

Unknown/miscellaneous:                               ~5-10%
```

**Vegetation management** is the single largest controllable factor in reliability improvement. Most utilities spend $400M–$1B+ annually on tree trimming. NERC FAC-003 mandates transmission ROW vegetation management; distribution standards are state PUC regulated.

---

## Feeder Automation: FDIR

Manual switching (lineman drives to a switch, operates it) takes 30-60 minutes to restore customers after a fault isolation. Automated FDIR (Fault Detection, Isolation, and Restoration) can do it in seconds.

```
FDIR SEQUENCE (automated):

1. FAULT OCCURS on feeder segment A-B
   │ Fault current → substation breaker trips (feeder de-energized)
   │ Time: 0 seconds

2. RECLOSER ATTEMPTS (automatic):
   │ Breaker closes (auto-reclose): 0.5 seconds
   │ If fault still there → trips again
   │ Tries 2-3 more times with increasing time delays
   │ Purpose: 80% of faults are transient (tree branch, animal)
   │         → automatic reclose restores without any SAIDI impact
   │ If fault persists after 3-4 attempts: LOCKOUT
   │ Time: 0-30 seconds

3. FAULT LOCATION, ISOLATION, RESTORATION (FDIR):
   │ Substation IED detects fault current direction and magnitude
   │ Automated switches detect fault passage (current direction sensors)
   │ Fault location algorithm narrows to segment
   │ ISOLATION: Open automated switches around faulted segment
   │            (isolate just the faulted cable/line section)
   │ RESTORATION:
   │   Section upstream of fault: restore by closing main breaker
   │   Section downstream of fault: restore via normally-open tie
   │           (closes tie switch from neighboring feeder)
   │ Time: 10-60 seconds (automated) vs 30-60 minutes (manual)

4. CREW DISPATCHED to repair the fault (physical repair still needed)
   Time: 2-8 hours (permanent repair)

SAIDI IMPACT:
  Without FDIR: all customers on feeder out 2-8 hours
  With FDIR: customers on faulted segment out 2-8 hours (unavoidable)
             all other customers restored in 10-60 seconds
             Only a fraction of customers count toward SAIDI
```

---

## Voltage Regulation Along Feeders

Voltage drops as current flows through feeder impedance. The customer at the end of a feeder gets lower voltage than the customer at the substation end. Utilities must maintain voltage within ±5% of nominal (ANSI C84.1: service voltage 114V–126V for 120V nominal).

```
VOLTAGE PROFILE ALONG FEEDER:

Voltage
(pu)    1.05 ─── Allowable high limit
        1.025
        1.00 ─── Nominal
        0.975
        0.95 ─── Allowable low limit

        │         ╲ (voltage sags as current draws through impedance)
        │          ╲
        │           ╲___ (without compensation: end-of-feeder too low)
        │
        │     ╔═══════════╗ Voltage regulator (±10% range)
        │     ║ regulator ║ raises voltage for rest of feeder
        │     ╚═══════════╝
        │               ╲___
        └─────────────────────────────────▶ distance from substation

VOLTAGE REGULATION TOOLS:
  1. Substation LTC (Load Tap Changer): ±16 steps × 1.25% each = ±20% range
     Adjusts the entire feeder voltage up/down based on load
     Slow: 30-90 second response (motor-operated tap changer)

  2. Line Voltage Regulators: Autotransformers installed on the feeder
     ±10% range, typically placed 1/2 to 2/3 way down the feeder
     Boost voltage for the downstream section
     Typical location: every 5-8 miles on rural feeders

  3. Capacitor Banks: Switchable capacitor banks at feeder intervals
     Inject reactive current → reduce reactive drop → raise voltage
     Also improve power factor → reduce real losses
     Two types: fixed (always connected) + switched (connected by relay)
     Switched caps: close when reactive load high (daytime), open at night
     Cost: $25-60k per 1.2 MVAR bank (typical distribution size)

  4. Conservation Voltage Reduction (CVR):
     Lower feeder voltage slightly (within limits) → reduce energy consumption
     Rule of thumb: 1% voltage reduction → 0.5-1% energy reduction
     (loads that scale with V² — resistance heating, incandescent)
     Modern buildings with switching power supplies: less responsive to CVR
```

---

## Underground vs Overhead Distribution

```
COMPARISON TABLE:

                     OVERHEAD              UNDERGROUND
──────────────────────────────────────────────────────────────────────
Capital cost         $100-300k/mile        $500k-2M/mile
  (new installation)  (varies: rural/urban)  (trenching cost dominant)
                     1× baseline           3-8× baseline

Failure rate         Higher (weather,      Lower (protected)
                     animals, vehicles)
                     1-3 faults/100        0.1-0.5 faults/100
                     circuit-miles/yr      circuit-miles/yr

Fault location       Easy (visual patrol)  Hard (TDR, tone equipment
                                          needed; specialized crew)

Repair time          Shorter (accessible)  Longer (excavation needed)
                     2-6 hours            4-24+ hours

Asset life           40-80 years           30-50 years (TR-XLPE)
                     (wood pole 40-60yr;    but often limited by
                      conductor longer)     insulation degradation

Storm resilience     Poor (vulnerable)     Excellent (buried)
                     Ice, wind, falling    Protected from weather
                     trees, flooding

Heat dissipation     Air-cooled            Soil-limited (ampacity
                     (high ampacity)        derating 20-40% in poor
                                           soil or summer)

Visual impact        Significant           None (buried)

Best use case        Rural, low density,   Urban, high density,
                     low land cost         aesthetic requirements,
                                          storm-hardening programs
```

**The economics of undergrounding:** Utilities in Florida, Carolinas, and coastal areas that face frequent hurricane damage have analyzed undergrounding distribution. Cost per mile: $500k–$2M. SAIDI improvement: typically 40-60% reduction. Payback: often 40-100 years at current storm frequencies. Not economic unless storm damage costs are severe or property values / aesthetics drive regulatory mandates.

**Underground cable technology:** Modern underground distribution uses TR-XLPE (tree-retardant cross-linked polyethylene) cable. Older installations used EPR or direct-buried XLPE. Primary failure mode: "water treeing" — moisture penetrates insulation over decades, creating conductive paths → eventual insulation failure. Modern TR-XLPE dramatically slows this but doesn't eliminate it. Cable life: 30-50 years before replacement recommended.

---

## DER Integration at Distribution Level

Distributed energy resources (rooftop solar, home batteries, EV chargers) are inverting the traditional one-directional power flow assumption of distribution design.

```
TRADITIONAL DISTRIBUTION (one direction):

Substation ──▶ Feeder ──▶ Loads (all power flows substation→customer)

MODERN DISTRIBUTION WITH DERs:

Substation ◀─▶ Feeder ◀─▶ Loads/Generators (bidirectional)

    ──── 12.47 kV Distribution Feeder ─────────────────────────────
                          │                            │
                      ┌───────┐                   ┌───────┐
                      │ 5 MW  │                   │ 200kW │
                      │ Solar │                   │ BESS  │
                      │ Farm  │                   │       │
                      └───────┘                   └───────┘
                                                  (export to grid)

PROBLEMS CREATED:
  1. Overvoltage: solar generation pushes voltage above 126V (ANSI limit)
     at end-of-feeder when it was designed for voltage DROP only
  2. Reverse flow: feeder protection assumes fault current flows FROM substation
     DER generation → fault current can flow BOTH directions → protection miscoordination
  3. Islanding: if feeder trips (breaker opens), DER may continue energizing
     the feeder → electrocution hazard for linemen, equipment damage
  4. Voltage flicker: cloud transients cause rapid voltage changes → power quality
  5. Harmonics: switching power supplies + inverters inject harmonic currents

IEEE 1547-2018: Standard for interconnection of DERs
  Updated 2018 to require DERs to:
  - Ride through voltage/frequency disturbances (not trip offline immediately)
  - Provide voltage regulation support (active/reactive power control)
  - Support abnormal frequency response
  - Anti-islanding protection (mandatory)

  This was a major update from 2003 version which required DERs to trip at ANY
  disturbance — a rule that made sense for 1% solar penetration but would cause
  cascading collapse at 30%+ penetration (all solar trips → grid can't recover)
```

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| Most common US primary distribution voltage? | 12.47 kV (phase-to-phase); 7.2 kV phase-to-neutral |
| Why 12.47 kV and not 25 kV everywhere? | Legacy infrastructure investment; 25 kV has longer feeder reach but requires complete system replacement |
| What is SAIDI? | System Average Interruption Duration Index — total customer outage minutes divided by total customers; units: minutes/customer/year |
| Best achievable SAIDI? | Japan achieves ~4 min/yr; US top quartile ~30-60 min; US average ~110 min |
| Overhead vs underground cost ratio? | Underground typically 3-8× more expensive per mile; but better reliability, resilience, aesthetics |
| What is FDIR? | Fault Detection, Isolation, Restoration — automated switching that restores unfaulted feeder sections in seconds rather than minutes |
| What limits voltage at end of feeder? | I×R and I×X drops in feeder impedance; managed by LTC, line regulators, capacitor banks |
| What voltages does residential service use? | 120/240V split-phase single-phase; L1 and L2 are 120V to neutral, 240V to each other |
| What voltages does commercial service use? | 208/120V three-phase 4-wire wye (small commercial) or 480/277V three-phase 4-wire wye (larger commercial/industrial) |
| What does IEEE 1547 require of DERs? | Fault ride-through, voltage/frequency support, anti-islanding protection |

---

## Common Confusion Points

**Why does residential US use 120V AND 240V from the same service?** The secondary winding of the pole transformer has a center tap. The two halves each supply 120V to neutral; the full winding supplies 240V between the two hots. This is "split-phase" single-phase service. Not the same as European 230V service, which is a different transformer configuration.

**SAIDI excluding major events:** Many utilities report SAIDI two ways — with and without "major event days." An MED is a day where the system-wide SAIDI impact exceeds a threshold (typically 2× normal daily SAIDI). This allows comparison of base reliability performance separate from extreme weather. Both numbers matter — the "excluding MEDs" figure reflects normal operations; the total figure shows vulnerability to weather.

**Feeder "capacity" is not transformer capacity:** A feeder's capacity is limited by the minimum of: (1) transformer size, (2) conductor ampacity, (3) voltage drop limits, (4) protection coordination. Often the binding constraint is voltage drop at the end of the feeder, not thermal limits of the conductors.

**Network distribution (urban) vs network utility (business term):** When utility people say "network distribution," they mean the multiple-source, low-voltage grid system used in dense urban areas. This is different from "network utility" (a business model term). Dense urban US (Manhattan, Loop Chicago) uses network distribution; suburban and rural use radial or loop feeders.

**Distribution vs transmission reliability:** Transmission SAIDI is negligible compared to distribution. The ~95% of customer outage minutes come from distribution failures (feeder faults, transformer failures, service drops). Transmission failures affect millions of customers but for very short periods (automatic switching in seconds to minutes). Distribution failures affect hundreds of customers for hours.

---

*Next: 05-GRID-STABILITY.md — frequency dynamics, swing equation, protection systems, cascading failures*
*See also: 07-SMART-GRID.md for AMI, demand response, and DER management platforms*
