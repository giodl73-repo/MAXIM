# Urban Transit

## The Big Picture

Urban transit is fundamentally a network problem. Its value grows non-linearly with coverage — a transit system that gets you to 90% of destinations is far more than 2× as useful as one covering 45%. This is Metcalfe's law applied to physical mobility. The challenge is that building a high-coverage network costs proportionally to coverage, while the utility benefit grows faster — which creates the political economy of transit: underinvestment is the stable equilibrium unless cities intervene.

```
+------------------------------------------------------------------+
|                    URBAN TRANSIT SYSTEM                          |
|                                                                  |
|  MODE PERFORMANCE SPECTRUM                                       |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Metro    |  | LRT      |  | BRT      |  | Bus      |         |
|  | (Heavy   |  | (Light   |  | (Rapid)  |  | (Local)  |         |
|  | Rail)    |  | Rail)    |  |          |  |          |         |
|  | 60-80k   |  | 20-40k   |  | 10-20k   |  | 5-10k    |         |
|  | pphpd    |  | pphpd    |  | pphpd    |  | pphpd    |         |
|  |$200-700M |  |$50-150M  |  |$2-20M/km |  |$0.5-2M   |         |
|  | /km      |  |/km       |  |          |  |/km       |         |
|  +----------+  +----------+  +----------+  +----------+         |
|                                                                  |
|  DEMAND MODELING                                                 |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Trip gen |  | Mode     |  | Route    |  | Network  |         |
|  | 4-step   |  | Choice   |  | Choice   |  | Assignment|         |
|  | model    |  | (Logit)  |  |          |  |          |         |
|  +----------+  +----------+  +----------+  +----------+         |
|                                                                  |
|  NETWORK DESIGN PRINCIPLES                                       |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Coverage |  | Frequency| | Transfer  |  | TOD/Land |         |
|  | vs       |  | is       |  | design   |  | Value    |         |
|  | Ridership|  | Freedom  |  |          |  | Capture  |         |
|  +----------+  +----------+  +----------+  +----------+         |
+------------------------------------------------------------------+
```

---

## Mode Comparison

### Capacity and Cost

The fundamental dimensions for mode selection: how many people per hour, at what cost per kilometre of infrastructure.

```
  TRANSIT MODE COMPARISON:

  Mode      pphpd    Vehicle cap  Headway   Const cost   Operating cost
  -----     ------   -----------  -------   ----------   --------------
  Metro     60-80k   1,000-2,000  90-120s   $200-700M/km High
  (grade    (6-10    per train           (can be <90s    (operations,
  separated  cars)                       with CBTC)       maintenance)
  rail)

  Commuter  30-60k   1,000-2,500  5-30min   $20-100M/km  High
  Rail      (8-12    per train           (track upgrade    (crew-intensive)
            cars)                        if existing)

  LRT       20-40k   200-600      5-10min   $50-150M/km  Medium
            (2-3     per vehicle          (at-grade is     (driver per
            cars)                         much cheaper)    vehicle)

  BRT       10-20k   80-160       5-10min   $2-20M/km    Low-medium
  (full     (1-3     per bus              (dedicated        (driver per
  BRT)       cars)                        lanes = key)      bus)

  Standard  5-10k    40-80        10-20min  $0.5-2M/km   Low
  Bus                per bus              (shared lanes)   (driver per
                                                           bus)

  WALK/BIKE  <5k     N/A          N/A       $0.5-5M/km   Very low
  infra.                                   (path/lane)

  pphpd = persons per hour per direction = corridor capacity metric
```

### Capacity Formula

The capacity of any transit service is a function of vehicle capacity, train length, and headway:

    Capacity (pphpd) = (vehicle capacity × vehicles per train) / headway_in_hours

Example: Metro with 6-car train (200 pax/car) at 2-minute headway:
- = (200 × 6) / (2/60)
- = 1,200 / 0.0333
- = 36,000 pphpd

To increase capacity: (1) lengthen trains, (2) reduce headway, (3) add platforms/tracks.

---

## Mode Choice Modeling

### Random Utility Theory

McFadden (1974 Nobel Prize) formalized mode choice as utility maximization with unobserved heterogeneity. Each mode has an indirect utility — the traveler chooses the mode with highest utility — but since the analyst cannot observe all factors, the choice appears probabilistic.

```
  UTILITY OF MODE j FOR TRAVELER i:

  U_ij = V_ij + epsilon_ij

  V_ij = "systematic" (observable) utility
  epsilon_ij = unobserved random component

  TYPICAL UTILITY FUNCTION:

  V_ij = beta_IVT * IVT_ij    (in-vehicle travel time)
       + beta_OVT * OVT_ij    (out-of-vehicle: wait + walk)
       + beta_FAR * fare_ij   (fare/cost)
       + beta_REL * REL_ij    (reliability)
       + ASC_j                (mode-specific constant)
       + beta_INC * income_i * ASC_j   (income interaction)

  RULE OF THUMB COEFFICIENTS (derived from value-of-time studies):
  Wait time disutility: ~2x in-vehicle time (people hate waiting)
  Walk time disutility: ~2-2.5x in-vehicle time
  Transfer penalty: equivalent to 8-15 minutes of IVT

  US average value of time (commute): $15-20/hour (2024)
  High-income workers: $30-50/hour
  This is why park-and-ride lots capture suburban riders who
  value their time too highly to walk 15 minutes to a bus.
```

### Multinomial Logit (MNL)

When the unobserved component epsilon follows an extreme value distribution (Gumbel), the choice probability has a closed form:

    P(mode j) = exp(V_ij) / sum_k(exp(V_ik))

This is the softmax function — exactly what you use in neural network output layers and recommendation systems. The mathematical structure is identical.

```
  MULTINOMIAL LOGIT EXAMPLE:

  3 modes: Car (C), Transit (T), Walk (W)
  V_C = -2.5   (traffic, parking cost)
  V_T = -1.8   (moderate frequency, some wait)
  V_W = -1.2   (direct, no wait, short trip)

  exp(V_C) = 0.082
  exp(V_T) = 0.165
  exp(V_W) = 0.301
  Sum      = 0.548

  P(Car)     = 0.082/0.548 = 15%
  P(Transit) = 0.165/0.548 = 30%
  P(Walk)    = 0.301/0.548 = 55%

  IMPROVE TRANSIT (reduce wait by 5 min -> delta_V_T = +0.5):
  V_T -> -1.3, exp(-1.3) = 0.272
  New sum = 0.655
  P(Transit) = 0.272/0.655 = 42% (was 30%)
  P(Car) = 0.082/0.655 = 13% (was 15%)

  Frequency improvement attracts riders primarily from walking
  (the most sensitive mode for short trips).
```

**IIA (Independence of Irrelevant Alternatives) problem:** In MNL, adding a new mode draws proportionally from all existing modes. Adding a red bus when there is already a blue bus should not draw from car — but MNL says it does. Nested logit and mixed logit models address this, nesting similar modes together (e.g., rail and bus in a "transit" nest).

---

## Network Design Principles

### Coverage vs Ridership

This is the fundamental design tension in transit networks (Jarrett Walker's framing):

```
  COVERAGE OBJECTIVE:                 RIDERSHIP OBJECTIVE:
  Maximize geographic coverage.       Maximize riders per cost dollar.

  +---------------------------+       +---------------------------+
  | SERVE LOW-DENSITY AREAS  |       | CONCENTRATE ON HIGH-      |
  | Many routes, low frequency|       | DEMAND CORRIDORS         |
  | 30-60min headways        |       | Few routes, high frequency|
  | 2-3 riders per bus       |       | 5-10 min headways        |
  | High subsidy per trip    |       | 50+ riders per bus       |
  | Social equity argument   |       | Lower subsidy per trip   |
  |                          |       |                          |
  | Serves transit-dependent |       | Maximizes overall system |
  | (no car) populations     |       | ridership and farebox    |
  +---------------------------+       +---------------------------+

  THE TENSION:
  Limited budget. You can't do both.
  Political pressure: cover all neighborhoods (equity)
  Operational logic: concentrate for ridership (efficiency)

  COMMON MISTAKE: trying to do both -> low frequency everywhere
                  = system nobody uses (even transit-dependent)
  OPTIMAL: Decide the goal explicitly, then design accordingly.
```

### Frequency is Freedom

The most cited principle in transit network design:

```
  WITH 5-MINUTE HEADWAYS:            WITH 30-MINUTE HEADWAYS:
  You approach the stop.             You must plan your trip.
  A bus comes shortly.               You arrive exactly at departure
  You take it.                       or wait up to 30 minutes.
  Total wait: 2-3 min.               Total wait: 0 to 30 min.
  Freedom: high.                     Freedom: low.

  WHAT FREQUENCY ENABLES:
  - Spontaneous travel decisions (like car ownership enables)
  - Acceptable transfer connections (short wait = low transfer penalty)
  - Resilience to minor delays (next bus is 5 min away)
  - Competitive with car for short trips

  THE RULE OF THUMB: 10-minute maximum frequency for serious ridership
  15-minute: acceptable. 30-minute: transit-dependent only.
  This is why bus routes that run every 30 minutes fail to attract riders
  even when the route is otherwise good.
```

### Transfers vs One-Seat Rides

```
  ONE-SEAT RIDE (direct route):       TRANSFER-BASED NETWORK:
  +--A----B----C----D--+              +--A----hub--D--+
  |                    |              |               |
  | Passengers going   |              +--B----hub--E--+
  | A->D: comfortable  |              |               |
  | No transfer penalty|              +--C----hub--F--+
  |                    |
  | Passengers going   |              BENEFITS:
  | A->B: infrequent   |              Higher frequency on each segment
  | service (route     |              More combinations served
  | covers all OD)     |              Lower cost per route

  TRADEOFF:
  Customers pay 8-15 min transfer penalty.
  But service is more frequent (cost is spread across more OD pairs).
  Net benefit: positive if frequency gain > transfer penalty.
  Empirically: 15-minute frequency with transfers beats 30-minute
               without transfers for most trip purposes.
```

---

## Bus Rapid Transit

BRT is the most misused term in transit. "BRT-lite" (just a label on a regular bus route) is rampant. Real BRT requires all five core components:

```
  BRT SPECTRUM: LITE vs FULL

  Feature           BRT-lite          Full BRT
  -------           --------          --------
  Dedicated lanes   No or partial     100% dedicated ROW
  Off-board fare    No (pay on bus)   Fare paid before boarding
  Level boarding    No (steps)        Platform = floor level
  Station quality   Bus stop          Enclosed station
  Signal priority   No                Transit Signal Priority (TSP)
  Branding/identity Generic bus       Branded vehicle + stop
  Frequency         30-60 min         5-10 min (high frequency)
  Network effect    None              Integrated with other modes

  CAPACITY WITH FULL BRT:
  Bogota TransMilenio: 45,000 pphpd
  (comparable to metro, built for ~5% of metro cost)
  Curitiba, Brazil: 15,000-20,000 pphpd

  WHAT MAKES BRT FAIL:
  - Mixing with general traffic (no dedicated lanes)
  - On-board fare payment (slow boarding -> slow frequency)
  - Inconsistent implementation (TSP implemented on 60% of intersections)
  - Political compromise: bus lanes removed under driver pressure
```

---

## Transit-Oriented Development (TOD)

Transit stations create value. Land near transit is worth more than equivalent land without transit. TOD attempts to capture this value to fund the transit that created it.

```
  LAND VALUE UPLIFT:

  Station area                     Non-transit area
  +------------------+             +------------------+
  |  Property value  |             |  Property value  |
  |  PREMIUM due to  |             |  BASE: car-     |
  |  transit access: |             |  dependent land  |
  |  +10-30% within  |             |  value           |
  |  800m of station |             |                  |
  +------------------+             +------------------+

  The value is created by public investment (transit).
  Land owners who did nothing to create the transit
  capture the uplift through higher property values.
  VALUE CAPTURE: mechanisms to return some of this
  value to the transit system that created it.

  VALUE CAPTURE MECHANISMS:

  1. Property tax increment financing (TIF):
     Tax the increment above pre-transit value.
     Used for many US rail extensions.

  2. Developer contributions/impact fees:
     Require developers near stations to contribute
     to station infrastructure or transit fund.

  3. Land sale/ground lease by transit authority:
     Agency owns land at stations; sells or leases
     at premium; uses proceeds for transit.

  THE HONG KONG MTR MODEL:
  MTR Corporation acquires land BEFORE announcing station locations.
  Develops property at stations (residential, commercial).
  Property profits subsidize transit operations.
  MTR is one of few transit systems that does not require
  government operating subsidy.
  2022 operating profit: ~HKD 15B from property + transport combined.
  Net result: Fares do not cover costs, but property does.
  World's most financially sustainable metro model.

  CATCHMENT AREA:
  Primary: 400-800m walk (5-10 minutes): highest ridership generation
  Secondary: 800-1,600m (bike, shuttle, feeder bus): meaningful
  Beyond: limited walk-up ridership; requires park-and-ride
```

---

## Fare Policy and Equity

### Fare Structure Options

```
  FARE STRUCTURES:

  FLAT FARE:
  Same price regardless of distance.
  Simple: one price, easy to understand.
  Cross-subsidy: short-trip users pay same as long-trip users.
  Equitable outcome: benefits long-distance (often lower income) riders.
  Technology: simple; turnstile validation or proof of payment.
  Examples: Chicago CTA ($2.50 flat), BART has distance-based.

  DISTANCE-BASED:
  Cost proportional to distance traveled.
  Pricing: fair in theory (longer trips cost more to serve).
  Impact: can be regressive if low-income riders travel farther.
  Technology: requires tap-in + tap-out (e.g., Oyster card London).
  Revenue: more predictable; matches cost structure.

  ZONE-BASED:
  Distance approximated by zone.
  Common in European systems (Berlin, Vienna).
  Simple enough, less precise than distance-based.

  TIME-BASED:
  Single price for unlimited travel within a time window (e.g., 90 min).
  Encourages transfers (no penalty for multi-leg trips).
  Used: Los Angeles Metro, many BRT systems.

  FREE FARE:
  Fare = zero. Used in Tallinn (Estonia), some smaller cities.
  Eliminates fare evasion, reduces dwell time (no validation).
  Revenue replaced by: local taxes, advertising, property.
  Evidence: modest ridership increase; equity benefits.
  Concern: removes price signal; large systems face cost sustainability.

  INTEGRATED TICKETING:
  Single payment covers multiple modes.
  Oyster card (London): tube + bus + rail all on one card.
  Octopus card (Hong Kong): transit + retail + parking.
  OMNY (NYC): contactless credit card tap-in.
  Critical for network usability: transfer penalties are reduced
  when the same fare covers all modes seamlessly.
```

### Equity Analysis

```
  TRANSIT EQUITY DIMENSIONS:

  HORIZONTAL EQUITY: Equal access for equal need.
  Low-income households have lower car ownership rates.
  Transit-dependent = relies on transit, no viable car option.
  US: ~9% of households with zero cars; concentrated in low-income areas.
  Equity argument: transit is essential infrastructure, not optional.

  VERTICAL EQUITY: Benefit relative to need.
  Do those who need transit most get the most service?
  Often: no. Higher-income urban areas have better transit
  (faster, more frequent) than low-income suburban/exurban areas.
  Transit deserts: areas with insufficient transit service
  given transit-dependent population density.

  GENTRIFICATION-TRANSIT INTERACTION:
  Transit investment raises property values near stations.
  Rising rents can displace low-income residents from transit-rich areas.
  Net result: transit-dependent people move farther from transit.
  Mitigation: community land trusts, inclusionary zoning near stations,
  anti-displacement protections.

  DEMAND ELASTICITY:
  Fare elasticity: ~-0.3 to -0.5 (10% fare increase -> 3-5% ridership loss)
  Service frequency elasticity: ~+0.5 to +0.7
  (service improvement more powerful than fare reduction, per rider gained)
```

---

## Urban Transit Planning Tools

```
  FOUR-STEP DEMAND MODEL (classical):

  1. TRIP GENERATION:
     How many trips originate from each zone?
     Function of: households, income, car ownership, employment.
     ITE rates (e.g., 10 trips/day per household).

  2. TRIP DISTRIBUTION:
     Where do those trips go?
     Gravity model: T_ij = A_i * P_i * B_j * A_j * f(c_ij)
     Where c_ij = cost/time between zones i and j
     Calibrated to observed OD matrices.

  3. MODE SPLIT:
     How do people travel?
     Logit model (see above).

  4. TRAFFIC ASSIGNMENT:
     Which routes do travelers use?
     User equilibrium (Wardrop): no user can reduce travel time
     by unilaterally changing routes.
     Same as Nash equilibrium.

  BPR VOLUME-DELAY FUNCTION (assignment):
  t = t0 * [1 + alpha * (v/c)^beta]
  Typical: alpha=0.15, beta=4
  v/c = volume to capacity ratio
  As volume approaches capacity, delay grows rapidly (v^4 term).
  Same mathematical structure as queueing M/D/1: delay -> infinity
  as utilization -> 1.

  MODERN ALTERNATIVES:
  Activity-based models: simulate individual person decisions across full day.
  More accurate than 4-step for understanding behavioral responses.
  Computational cost: high; used for major investment decisions.
```

---

## Decision Cheat Sheet

| Transit decision | Approach |
|-----------------|----------|
| Choose metro vs LRT vs BRT | Demand corridor: >30,000 pphpd -> metro; 15-30k -> LRT; <15k -> BRT |
| Determine minimum frequency | 10 min peak for ridership; 15 min off-peak; 30 min = coverage only |
| Optimize network structure | Coverage vs ridership tradeoff: decide goal, then design |
| Evaluate TOD potential | 400-800m walk catchment; assess land values; consider MTR model |
| Set fare policy | Flat fare for equity + simplicity; distance-based for revenue alignment |
| Model mode split | Logit model; calibrate to local VOT; weight wait time 2x IVT |
| Assess BRT quality | Check all 5 core components; "BRT-lite" without dedicated lanes fails |
| Address transit equity | Map transit deserts vs transit-dependent population; plan accordingly |

---

## Common Confusion Points

**BRT is not just a paint job**
The most common mistake in transit planning: add a label, maybe some queue-jump lanes, and call it BRT. Without dedicated lanes, off-board fare, and level boarding, it is a bus with a marketing name. Capacity and speed are indistinguishable from standard bus. The Bogota/Curitiba evidence for high-capacity BRT comes from systems with all five core components.

**LRT vs streetcar vs tram**
These terms are used inconsistently globally. "Light rail" in the US often means fully grade-separated LRT. "Tram" in Europe can mean at-grade streetcar or modern LRT. "Streetcar" in US cities typically means at-grade urban tram. The technical distinction: grade separation is the key variable. At-grade systems are limited by intersection delays regardless of what they're called.

**Frequency beats coverage for ridership**
If you add a new route with 30-minute headway to a neighborhood vs adding 5-minute frequency to an existing high-demand corridor, the frequency improvement will attract far more new riders per dollar. Coverage decisions are about equity; frequency decisions are about ridership. Both matter; they are not the same decision.

**Value of time is not uniform**
The average commute VOT (~$15-20/hr in US) hides enormous variation. A software engineer earning $200/hr values their commute time very differently from a service worker at minimum wage. Transit mode choice models calibrated to average VOT will underpredict premium transit demand among high-income riders and overpredict price sensitivity for low-income riders.

**The Hong Kong MTR model is not directly transferable**
Hong Kong MTR's property development model works because: (1) very high land values, (2) government assigned land development rights to MTR before announcing stations, (3) long-term development pipeline. US law and land-use regulations make the Hong Kong model difficult to replicate directly. Value capture is possible (TIF, impact fees) but property development by the transit agency is legally/politically harder.
