# Transportation Economics

## The Big Picture

Transportation economics is applied welfare economics and industrial organization. The core questions: how much to invest (CBA), how to price (externalities and marginal cost), who should own and operate (natural monopoly theory), and how markets behave when competition is feasible. These questions apply directly to cloud infrastructure investment — the same NPV machinery evaluates a highway as evaluates an Azure data center expansion.

```
                 TRANSPORTATION ECONOMICS MAP

  INVESTMENT APPRAISAL:
    CBA Benefits (travel time, etc.) | NPV/BCR/IRR
    Wider Economic Benefits | Discount Rate Debate

  EXTERNALITIES AND PRICING:
    Congestion externality | Emissions pricing (carbon)
    Accidents external costs | First-best Pigouvian tolls

  ROAD PRICING CASES:
    Singapore ERP | Stockholm Charge | London CC | SR91 Express

  PUBLIC VS PRIVATE PROVISION:
    Natural Monopoly | PPP Models | Port Competition | Aviation Markets
```

---

## Infrastructure Investment Appraisal

### Cost-Benefit Analysis

CBA is the standard framework for public infrastructure investment. Identical in structure to NPV analysis for private investment — the difference is in what goes in the benefit stream.

```
  STANDARD CBA FRAMEWORK:

  NPV = Sum_t [ (B_t - C_t) / (1+r)^t ]

  Where:
    B_t = total benefits in year t
    C_t = total costs in year t (capital + O&M)
    r   = discount rate
    t   = year (0 = construction start)

  BCR (Benefit-Cost Ratio) = PV(Benefits) / PV(Costs)
  BCR > 1.0: project passes CBA test
  BCR > 2.0: typically considered strong
  UK DfT: BCR > 1.5 for "good value for money"

  IRR (Internal Rate of Return):
  The r* such that NPV = 0.
  Accept if IRR > hurdle rate (typically social discount rate).
  Prefer NPV for mutually exclusive projects; IRR for go/no-go.

  SAME AS AZURE DC INVESTMENT:
  Azure data center CBA:
  Benefits: future cloud revenue (discounted)
  Costs:    construction + equipment + operations
  Decision: IRR vs Microsoft WACC (~10%)

  Transport CBA:
  Benefits: travel time savings + accident reductions + etc.
  Costs:    construction + maintenance
  Decision: BCR vs government threshold (1.0 or 1.5 or 2.0)
```

### What Goes in the Benefit Stream

```
  TRANSPORT PROJECT BENEFITS:

  1. TRAVEL TIME SAVINGS (usually largest benefit, 60-80%)
     Savings = trips * time_saved * Value of Time
     VOT: UK DfT uses ~£17/hr for work travel, ~£8/hr for leisure
     IMPORTANT: VOT must match trip purpose
     Highway freight: truck time * driver wage + vehicle operating cost
     Commuter rail: commute time * commuter VOT

  2. VEHICLE OPERATING COST SAVINGS (10-20%)
     Fuel, maintenance, tires reduced by shorter/smoother route.
     Quantified from unit costs per vehicle-km.

  3. ACCIDENT COST SAVINGS (5-15%)
     Reduction in accidents * average accident cost.
     Accident cost: medical, property damage, lost productivity, pain.
     UK unit costs: ~£2.3M per fatal accident, £270K per serious injury.
     Safety measures (median barriers, grade separation) often have
     BCR > 20: highest-return infrastructure investment.

  4. EMISSIONS SAVINGS (2-8%)
     Carbon savings at social cost of carbon ($50-200/tonne CO2).
     Local air quality savings (NOx, PM2.5) — can exceed carbon value
     in dense urban areas.

  5. WIDER ECONOMIC BENEFITS (0-30%, depends on context)
     Agglomeration: workers closer together -> productivity gains.
     Labour market access: more jobs reachable -> better matching.
     Competition effects: new trade routes -> lower prices.
     These are controversial and hard to quantify; easily overstated.
     UK HMT Guidance: wider benefits can be added if "catalytic" effects
     are genuine and not double-counted with user benefits.
```

### Discount Rate — The Pivotal Assumption

The discount rate choice for 50-100 year infrastructure projects is **not** a technical matter — it is a philosophical and political one. It determines whether long-run benefits (decarbonization, climate adaptation) look worthwhile.

```
  DISCOUNT RATE EFFECTS ON 50-YEAR BENEFIT:

  $1B benefit in year 50, discounted to today:

  Rate    PV of $1B in year 50
  ----    --------------------
  1.4%    $ 499M  (Stern Review, social discount rate)
  3.0%    $ 228M  (UK Green Book)
  5.0%    $  87M  (Nordhaus, market rate)
  7.0%    $  34M  (OMB, US federal standard for many uses)
  10%     $   9M  (private sector hurdle)

  STERN vs NORDHAUS DEBATE (climate, but applies to transport):
  Stern (1.4%): future generations deserve near-equal weight to present.
                Low discounting makes climate action highly worthwhile.
  Nordhaus (5%): market rates reflect actual time preferences.
                 High discounting makes near-term benefits dominate.

  PRACTICAL IMPLICATION:
  A highway project with benefits concentrated in years 1-20:
  Discount rate barely matters (both Stern and Nordhaus give similar PV).

  A rail project with 80-year life, major carbon benefits in years 30-80:
  7% discount rate: benefits in years 30-80 barely count.
  1.4% discount rate: those same benefits are very significant.
  The discount rate determines the answer before you run the model.
```

### Common Appraisal Errors

```
  SUNK COST FALLACY IN INFRASTRUCTURE:

  CONCORDE:
  1965: UK-France committed to supersonic airliner.
  1970s: clear the aircraft will be uneconomic (only 14 ordered).
  Decision: continue anyway because £1B already spent.
  CORRECT DECISION: abandon (future costs > future benefits).
  ACTUAL DECISION: complete; operated 1976-2003 at a loss.
  Cost: ~$13B (2024 dollars) total.

  BOSTON BIG DIG (I-93 tunnel):
  Estimated 1983: $2.6B.
  Final cost: $14.6B (completed 2007).
  Cost overrun: 463%.
  LESSON: Large infrastructure projects routinely have 50-200%
  cost overruns and 30-70% optimism bias in benefit estimates.
  Flyvbjerg (Oxford): infrastructure projects average 45% cost overrun.
  Better to use reference class forecasting (what similar projects cost).

  OPTIMISM BIAS ADJUSTMENT:
  UK Green Book mandates adding optimism bias:
  Roads: +15% to costs in appraisal
  Rail: +40% to costs in appraisal
  New builds: even higher (50-100%)
  Rationale: systematic bias in project forecasts; correct a priori.
```

---

## Transportation Externalities

### The Congestion Externality

When you enter a congested road, you slow down all other vehicles. You bear only your own time cost; the cost you impose on others is an externality.

```
  CONGESTION EXTERNALITY DIAGRAM:

  Costs
  ^
  SMC |         /
      |        /  Social Marginal Cost (SMC) = PMC + external cost
      |       /
  PMC |      /   Private Marginal Cost (PMC) = your own time cost
      |     /
      |____/
      +----------> Traffic volume (q)

  PRIVATE EQUILIBRIUM (no toll):
  Driver enters road if PMC < value of time.
  Equilibrium at q* where demand = PMC.
  Total cost = area under SMC curve for q* trips.

  OPTIMAL TOLL = SMC - PMC at q* (Pigou, 1920)
  This internalizes the externality.
  Result: volume falls from q* to q** < q*
  Travel time for remaining users IMPROVES.
  Revenue from toll = (q**) * toll_rate.

  FIRST-BEST THEORY vs SECOND-BEST REALITY:
  First-best: toll every road at marginal external cost.
  Problem: political resistance; toll booths; truck logistics.
  Second-best: toll some roads; not others.
  When some roads are tolled and alternatives are not:
  diverted traffic imposes externality on alternative route.
  Optimal toll in second-best may be BELOW marginal cost.
```

### Accident Externalities

Road accidents impose costs on third parties (other road users, pedestrians, emergency services, healthcare system). These are not borne by the at-fault driver.

```
  ACCIDENT COST COMPONENTS:

  PRIVATE COST (borne by driver/passengers):
  Own medical costs (if insured)
  Own time lost
  Own vehicle damage
  Own insurance premium (imperfect)

  EXTERNAL COST (borne by others):
  Other parties' medical costs
  Emergency services (police, ambulance, fire)
  Healthcare system costs
  Third-party property damage
  Pain and suffering of third parties
  Insurance cross-subsidy

  ESTIMATE (UK, per vehicle-km):
  Car external accident cost: ~0.3p/km
  Truck external accident cost: ~1.5p/km
  Motorbike external accident cost: ~5p/km
  (Motorbikes impose highest per-km external accident cost)

  POLICY IMPLICATION:
  Drivers do not face the full social cost of accident risk.
  Optimal: insurance that fully internalizes risk (usage-based, risk-based).
  UK: third-party insurance mandatory but not risk-differentiated enough.
```

### Emissions Externalities

Transport GHG emissions impose costs on global climate — a textbook negative externality with no current market price (absent carbon pricing).

```
  SOCIAL COST OF CARBON (SCC):
  The welfare cost of emitting one additional tonne of CO2.
  Discount rate sensitivity: enormous.

  US EPA (2023): $190/tonne (revised up significantly from prior $51/tonne)
  UK HMT: £70/tonne CO2e (2030), rising to £250 (2050)
  EU ETS price: €50-70/tonne (2024 range; varies with market)
  Stern Review: >$250/tonne

  TRANSPORT CO2 COSTS (at $190/tonne):
  Car (average US): ~9kg CO2/gallon * $190/tonne = $1.71 per gallon carbon cost
  Aviation: ~90g CO2/passenger-km * 1000km = 90kg = $17 per 1,000km passenger
  Container ship: 10g CO2/tkm * 20,000 tkm/container = 200kg = $38/container Shanghai-LA

  AVIATION EXTRA FORCING:
  Aviation creates NOx, contrails, and cirrus clouds at altitude.
  Total warming effect estimated at 2-4x CO2 alone.
  ERF (effective radiative forcing) adjustment needed.
  EU ETS covers aviation within EU since 2012; not globally.
  ICAO CORSIA: international offsetting scheme from 2024.
```

---

## Road Pricing — Theory to Practice

### First-Best and Second-Best Pricing

```
  MARGINAL SOCIAL COST PRICING:
  Optimal price = direct cost to provider (maintenance, capital)
               + congestion cost externality
               + accident cost externality
               + emissions cost
               + noise/local air quality cost
               - government subsidy received

  For a congested urban motorway:
  Direct cost:        ~2p/km
  Congestion:        ~10-30p/km (peak hours)
  Accidents:          ~0.3p/km
  Emissions:          ~0.5p/km
  Total:             ~13-33p/km peak
  vs current fuel tax ~3p/km

  The gap is large. Road users are undercharged for peak urban use.
  This is why congestion is endemic — pricing too low.

  RAMSEY PRICING (second-best, natural monopoly):
  If you cannot price at marginal cost (political/transaction constraints),
  set prices to minimize deadweight loss subject to revenue constraint.
  Ramsey rule: set price-cost markup inversely proportional to elasticity.
  High-elasticity users: price closer to MC.
  Low-elasticity users (trucking): higher markup.
  Applied to: airports, rail networks, ports.
```

### Road Pricing Case Studies

```
  SINGAPORE ELECTRONIC ROAD PRICING (ERP):

  1975: World's first cordon pricing (Area Licensing Scheme, paper).
  1998: Electronic Road Pricing (ERP) replaces ALS.
  2023: Moving to GPS-based pricing (ERP2 — GNSS).

  HOW IT WORKS:
  Gantries placed on expressways and into CBD.
  In-vehicle unit (IU) with CashCard deducted automatically.
  Prices vary by: time of day, road segment, traffic conditions.
  Prices adjusted quarterly to maintain target speed (45-65 km/h expressway).

  RESULTS:
  Speed maintained at targets during peak hours.
  ~9% reduction in traffic entering CBD vs pre-ERP.
  Revenue: SGD 100-150M/year; funds road maintenance.
  Acceptance: high (Singapore is authoritarian context; privacy less contested).

  STOCKHOLM CONGESTION TAX:

  Timeline:
  2006: 7-month trial.
  2006: Referendum — 53% against (regret effect: traffic improved during trial).
  2007: Made permanent despite referendum (government override).
  2016: Tax level increased.
  2020: Further expansion.

  CHARGES:
  SEK 11-45 per crossing depending on time and direction.
  Maximum SEK 135/day.
  Exemptions: alternative-fuel vehicles (removed 2012 after abuse).

  RESULTS:
  Traffic reduction: -20% in CBD at peak.
  Revenue: ~SEK 1B/year.
  Public acceptance: low pre-trial; high post-trial; now broadly accepted.
  Key learning: people predict they will hate it; then discover they don't.

  LONDON CONGESTION CHARGE:

  2003: First major western city cordon charge.
  Initial: £5/day; now £15/day (2023 weekday rate).
  ULEZ (2021/2023): Ultra-Low Emission Zone — surcharge for high-emission vehicles.

  RESULTS:
  Traffic reduction: -15-20% in zone.
  Revenue: ~£200M/year.
  Air quality: NOx and PM2.5 improved in zone.
  Mode shift: bus and cycling ridership increased.
  Acceptability: low initially; improved over time.
  Legal challenges: Mayor Khan (2023) ULEZ expansion to Greater London.

  SR91 EXPRESS LANES (California):

  1995: First US private variable-priced express lane.
  Parallel to SR91 (free lanes), 10-mile section.
  Price dynamically set to maintain speed > 65 mph.
  Peak: $10-15 for 10 miles.

  LESSON:
  Users voluntarily pay high prices when they value time.
  Demonstrated that road pricing works in US context.
  Price elasticity: ~-0.1 to -0.3 for choice lane vs free lane.
```

---

## Public vs Private Infrastructure Provision

### Natural Monopoly Framework

Transport infrastructure has natural monopoly characteristics:

```
  NATURAL MONOPOLY CONDITIONS:

  1. HIGH SUNK COSTS:
     Track, runways, port berths are specific assets.
     Cannot be liquidated if investment fails.
     Creates commitment problem: government may expropriate.
     Private investor demands high risk premium.

  2. ECONOMIES OF SCALE:
     Average cost declines with output (for a fixed network).
     Duplication is wasteful: two competing railways on the same route?
     Natural monopoly: one firm can serve at lower cost than two.

  3. ECONOMIES OF DENSITY:
     More traffic on same network lowers per-unit cost.
     Reinforces monopoly: incumbent with more traffic has cost advantage.

  RESULT:
  Competition on infrastructure is often wasteful.
  Competition for infrastructure (franchise/concession) can be efficient.
  Regulation of natural monopolies is required to prevent monopoly pricing.

  REGULATION MODELS:
  Rate-of-return regulation: regulator caps return on capital.
     Problem: Averch-Johnson effect — over-invest in capital.
  Price-cap (RPI-X): regulator sets price ceiling.
     Incentive to reduce costs (you keep the savings).
     Problem: quality degradation (Railtrack UK: collapsed 2002).
  Regulatory Asset Base (RAB): regulator sets allowed revenue based
     on asset value and allowed return.
     Used for: UK water, gas, airports (Heathrow, Gatwick).
     Provides long-run investment incentives.
```

### PPP (Public-Private Partnership) Models

```
  PPP STRUCTURES:

  TYPE           PRIVATE SECTOR DOES        RISK TRANSFER
  ----           -------------------        -------------
  O&M            Operate and maintain       Performance risk only
  Contract       existing public asset      Capital stays with public

  Design-Build   Design and construct       Construction risk to private
  (DB)           Turn over to public        Cost overrun risk transferred

  DBFM           Design, build, finance,    Construction + financing risk
                 maintain                   transferred
                 User fees = 0;             Performance risk to private
                 availability payment       Demand risk: government

  DBFOT          Design, build, finance,    Construction + financing risk
  (Concession)   operate, transfer          + DEMAND RISK to private
                 After 25-30 years:         All commercial risk transferred
                 transfer back to public    (revenue risk = demand risk)

  KEY QUESTION: Who bears demand risk?
  If the private operator bears demand risk (DBFOT):
  - If traffic is below forecast: private operator loses money
  - Government gets the infrastructure, private bears the bet
  Example: Chicago Skyway (1.8B$ concession 2005): operator wins when
           traffic is high; renegotiation risk if revenue insufficient.

  PPP PERFORMANCE EVIDENCE:
  Mixed globally. Benefits:
  - Transfers construction and financing risk
  - Private sector project management efficiency (sometimes)
  - Off-balance-sheet for government (controversial)
  Problems:
  - Incomplete contracts (35-year concession cannot anticipate all events)
  - Renegotiation: private operator fails -> government backstops anyway
  - Higher financing cost (private WACC > government bond rate)
  - UK PFI: systematic higher cost than direct procurement (NAO evidence)
```

---

## Port and Airport Competition

### Port Competition

```
  PORT MARKET STRUCTURE:

  INTER-PORT COMPETITION:
  Multiple ports serving same hinterland compete on price and service.
  US East Coast: NY/NJ, Baltimore, Philadelphia, Norfolk, Charleston, Savannah.
  All compete for containers from/to Eastern US.

  HINTERLAND CAPTURE:
  Port's catchment = economic geography where transport cost to port
  is lower than to any competing port.
  Drayage + rail + time costs determine hinterland.

  INLAND WATERWAY ACCESS:
  Rotterdam: Rhine corridor -> inland barges to Ruhr, Bavaria.
  Antwerp: Scheldt -> industrial heartland Belgium.
  This access is the primary competitive advantage vs UK ports.
  UK has no comparable inland waterway for container barges.

  CONCENTRATION:
  Herfindahl-Hirschman Index (HHI): sum of squared market shares.
  HHI > 2,500: highly concentrated; raises competition concerns.
  Major port markets: HHI often 2,000-4,000 (concentrated but with
  some competition especially for large container ports).

  TERMINAL CONCESSIONS:
  Ports often retain harbor infrastructure (public ownership).
  Individual terminals concessioned to private operators.
  Global terminal operators: PSA, HPH (Hutchison), APM Terminals,
                             DP World, MSC Terminal, CMA CGM Terminal.
  These 6 operators handle ~65% of global container throughput.

  SUEZ vs PANAMA: ASIA-US EAST COAST ROUTING COMPETITION
  Traditional: Asia -> Suez -> Atlantic -> US East Coast
  Alternative: Asia -> Pacific -> Panama Canal -> US East Coast
  Competitive if: Panama handling capacity, canal expansion, vessel size.
  New Panama locks (2016): opened this route to 14,500 TEU vessels.
  Now: genuine competition; routing choice depends on canal fees,
       congestion, vessel availability.
```

### Aviation Economics — Bilateral ASAs and Open Skies

```
  BILATERAL AIR SERVICE AGREEMENTS (ASA):

  Traditional "Bermuda II" type (1946-1990s):
  - Designate one or two national carriers per route
  - Regulate frequencies, capacity, fares
  - State department negotiates; airlines implement

  Open Skies (US model, from 1992):
  - Any number of carriers from each country
  - No capacity or frequency restrictions
  - Fares set by market
  US has 130+ Open Skies agreements (2024)

  EU SINGLE AVIATION MARKET (1997):
  Any EU carrier can fly any intra-EU route.
  Transformed European aviation: LCCs (Ryanair, easyJet) exploded.
  Routes proliferated; fares fell 30-50%.

  THE SIXTH FREEDOM:
  A carrier uses its home hub to connect passengers between two foreign countries.
  Example: Singapore Airlines connects US passengers to Australia via Singapore.
  The US and Australia each allow the 6th freedom operation.
  Middle East carriers (Emirates, Etihad, Qatar) are the quintessential
  6th freedom operators: connect every city in the world via Dubai/Abu Dhabi/Doha.

  ALLIANCE ECONOMICS:
  Star Alliance, Oneworld, SkyTeam.
  Revenue sharing: code-sharing, interline agreements.
  Immunity from antitrust for trans-Atlantic joint ventures.
  American-British Airways-Iberia trans-Atlantic JV:
  pools revenue across all 3 carriers' transatlantic capacity.
  Result: effective merger economics without legal merger.
```

---

## Transport and Development

```
  THE CHICKEN-AND-EGG PROBLEM:

  Does transport investment CAUSE development?
  Or does development DEMAND transport investment?

  EVIDENCE FROM HISTORY:
  British canals (1760-1830): built before demand fully existed.
  Created markets by connecting isolated industrial areas.
  Caused development.

  US Interstates (1956-): built ahead of suburban demand.
  Enabled suburbanization that then demanded the highways.
  Caused suburban sprawl.

  UK experience (20th century): rail investment AFTER development.
  Improved transport connections after urban areas established.
  Responded to demand.

  AGGLOMERATION ECONOMIES:
  Businesses and workers cluster together -> higher productivity.
  Transport investment reduces effective distance between clusters.
  -> Agglomeration benefit = key "wider economic benefit" in CBA.
  UK evidence: Crossrail (Elizabeth Line) justified partly on
               London agglomeration effect: ~40% of total benefits.

  LAND VALUE CAPTURE:
  Station-area land values capture future agglomeration benefit.
  Measuring land value uplift = forward-looking measure of economic benefit.
  Used as: project finance mechanism (TIF) + appraisal evidence.

  TRANSPORT vs INEQUALITY:
  Transport investment can increase or reduce inequality:
  INCREASE: invest in routes used by high-income (suburban highway)
            and displace low-income from improved areas (gentrification)
  REDUCE:   connect low-income areas to employment centers
            (job accessibility benefit)
  Policy question: who benefits from what investment?
  This is an explicitly distributional choice, not a technical one.
```

---

## Decision Cheat Sheet

| Economic analysis question | Approach |
|---------------------------|----------|
| Should we build this road/rail? | CBA: NPV at appropriate social discount rate; BCR >1.5 typically required |
| What discount rate to use? | Government standard (3-7%); note sensitivity for long-lived benefits |
| Is there market failure here? | Check: externalities (congestion, emissions, accidents); natural monopoly characteristics |
| Optimal toll level? | Set toll = SMC - PMC at equilibrium flow; use demand elasticity to estimate flow change |
| Private vs public provision? | Check for natural monopoly (sunk costs + scale economies); if yes, regulate or franchise |
| PPP vs direct procurement? | Direct for simple projects; PPP for complex/long-term if risk transfer is genuine |
| Port competition assessment? | HHI of container throughput in hinterland; assess rail/road access equally |
| Value wider economic benefits? | Use UK DfT WEB methodology; additionality check; no double-counting with user benefits |

---

## Common Confusion Points

**BCR > 1 does not mean "build it"**
A BCR above 1 means the project creates more value than it destroys — necessary but not sufficient for investment. The government has a budget constraint. All projects compete for scarce capital. A BCR of 1.2 might be rejected when other projects offer BCR of 3.0. CBA gives the value created; the budget process allocates capital to the highest-value projects. Same logic as capital allocation in a business.

**Wider economic benefits (WEB) are routinely abused**
Agglomeration, competition, and labour market access effects are real but can be double-counted with user benefits. UK DfT guidance is explicit: only add WEB if: (1) market imperfections exist, (2) the transport change is transformative in scale, (3) no double-counting with consumer surplus. Many project appraisals inflate BCR by adding WEB without meeting these tests.

**Road pricing revenue is not the point**
Road pricing is about efficiency (correct externality), not revenue collection. The optimal congestion toll happens to generate revenue as a by-product. Hypothecating (ring-fencing) that revenue for roads or transit is politically convenient but not required for economic efficiency. Sweden's congestion tax revenue goes to the general budget.

**Natural monopoly arguments have limits**
Not every part of a transport system is a natural monopoly. The track is natural monopoly; the trains running on it may not be. The port berth is a natural monopoly for its location; the terminal operations can be competitively tendered. Vertical separation (split infrastructure from operations) is designed to introduce competition in the non-monopoly layers. UK rail: Network Rail owns track (regulated natural monopoly); train operators compete for franchises.

**PPP does not reduce the long-run cost to government**
Government debt is cheaper (lower yield) than private finance (higher WACC). PPP transfers risk — for which the private sector charges a risk premium. If the risk transfer is genuine and the private sector is better at managing it, PPP can create value. If the government backstops the risk anyway (as happened with Railtrack and many PFI hospitals), PPP is simply more expensive finance. The UK NAO has repeatedly found PFI/PF2 cost more than direct procurement.
