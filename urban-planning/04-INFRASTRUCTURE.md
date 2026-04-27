# Urban Infrastructure Planning and Finance

## The Big Picture

Urban infrastructure is the physical capital that makes cities function: water, sewer, roads, bridges, power, parks, fiber. It is long-lived (50-100 year design life), capital-intensive, politically difficult to fund, and almost always underfunded in operations and maintenance. The fundamental challenge: build cheaply now, pay dearly for maintenance later.

```
+------------------------------------------------------------------+
|                    URBAN INFRASTRUCTURE SYSTEM                   |
|                                                                  |
|  TRANSPORTATION     WATER/WASTEWATER      UTILITY/ENERGY         |
|  Streets/roads      Drinking water        Electric grid          |
|  Bridges            Distribution          Natural gas            |
|  Transit            Wastewater            Telecommunications     |
|  Bike/ped           Treatment             Broadband              |
|  Freight            Stormwater            District energy        |
|                                                                  |
|  PUBLIC SPACE/      SOLID WASTE           DIGITAL                |
|  PARKS              Collection            Smart sensors          |
|  Parks/plazas       Transfer stations     5G small cells         |
|  Urban tree canopy  Landfills/composting  Fiber backbone         |
|  Public buildings   Recycling             Traffic control        |
+------------------------------------------------------------------+
         |                    |
         v                    v
+--------------------+ +------------------------+
| PLANNING PROCESS   | | FINANCE MECHANISMS     |
| CIP development    | | GO bonds               |
| Asset management   | | Revenue bonds          |
| Life-cycle costing | | TIF                    |
| Prioritization     | | Impact fees            |
| Level of service   | | Developer exactions    |
|                    | | Federal grants (IIJA)  |
|                    | | PPP/concessions        |
+--------------------+ +------------------------+
```

---

## Capital Improvement Programming (CIP)

The CIP is the multi-year plan (typically 5-6 years) that translates infrastructure needs into funded projects. It is the infrastructure equivalent of a product roadmap with a budget.

```
CIP DEVELOPMENT PROCESS:

  STEP 1: NEEDS ASSESSMENT
  +-----------------------+
  | Asset inventory       |
  | Condition assessment  |
  | Level of service gaps |
  | Growth projections    |
  +-----------------------+
  Which assets are failing? Which LOS standards are unmet?
  What capacity is needed?
          |
          v
  STEP 2: PROJECT DEVELOPMENT
  +-----------------------+
  | Scope definition      |
  | Preliminary cost est. |
  | Phasing options       |
  | Alternatives analysis |
  +-----------------------+
  What does it cost? When can it be done?
  What are the alternatives?
          |
          v
  STEP 3: PRIORITIZATION
  +-----------------------+
  | Scoring criteria:     |
  |  - Safety/risk        |
  |  - LOS impact         |
  |  - Strategic fit      |
  |  - Equity/access      |
  |  - Leverage (grants)  |
  +-----------------------+
  Weighted score matrix. Like a sprint backlog
  prioritization — but with $50M consequences.
          |
          v
  STEP 4: FUNDING ASSIGNMENT
  +-----------------------+
  | Match projects to     |
  | funding sources.      |
  | Identify gaps.        |
  | Grant applications    |
  +-----------------------+
  Which fund pays? What can be bonded? Are grants available?
          |
          v
  STEP 5: ADOPTION
  Incorporated into annual budget.
  Year 1 = budget appropriation.
  Years 2-5 = programming (subject to revision).
  Annual CIP update slides projects forward.

PRIORITIZATION SCORING (example matrix):

  CRITERION              WEIGHT   SCORE (0-10)  WEIGHTED
  Safety/risk              30%        8           2.40
  LOS improvement          25%        6           1.50
  Strategic fit            20%        7           1.40
  Equity/access impact     15%        9           1.35
  Grant leverage           10%        5           0.50
                                              ---------
  TOTAL SCORE:                                   7.15

  Projects ranked by total score.
  Budget allocated from highest score down
  until funding is exhausted.

  This is a judgment call formalized with numbers.
  The weights embed political choices.
  ("Equity impact" at 15% is a political decision,
   not a technical one.)
```

---

## Asset Management: Infrastructure as a Software System

Modern infrastructure asset management uses exactly the kind of data systems, condition monitoring, and predictive analytics that software engineers build.

```
ASSET MANAGEMENT LIFECYCLE:

  INVENTORY (what do we own?):
    GIS asset registry (geometry + attribs)

  CONDITION (what state?):
    Field inspection (PCI/BCI), sensor data

  DETERIORATION (how fast failing?):
    Deterioration curves (empirical or model)
                         |                     |
                         v                     v
                   +--------------------------------+
                   | RISK-BASED PRIORITIZATION      |
                   | P(failure) × Consequence       |
                   | = Risk score                   |
                   | High consequence failures      |
                   | (water main under freeway)     |
                   | prioritized over low conseqnce |
                   | (water main in park)           |
                   +--------------------------------+
                              |
                              v
                   +--------------------------------+
                   | WORK PROGRAM                   |
                   | Optimize intervention timing:  |
                   | Preventive: low cost, early    |
                   | Rehabilitative: medium cost    |
                   | Replacement: high cost, late   |
                   +--------------------------------+

KEY STANDARDS:
  IIMM: International Infrastructure Management Manual
  ISO 55000: Asset management systems standard
  MicroPAVER: USACE pavement management software
  Pontis/AASHTOWare: bridge management
```

### Condition Assessment: Pavement as Example

```
PAVEMENT CONDITION INDEX (PCI):

  SCALE: 0-100
  100: Perfect (new pavement)
   70: Good (minor surface distress)
   55: Fair (moderate distress, roughness)
   40: Poor (major distress, potholes)
   25: Very Poor (severe damage)
    0: Failed (impassable)

  TYPES OF DISTRESS MEASURED:
  - Alligator (fatigue) cracking
  - Block cracking
  - Edge cracking
  - Longitudinal/transverse cracking
  - Potholes
  - Rutting
  - Raveling
  - Bleeding

  FIELD MEASUREMENT:
  Visual survey by trained inspector.
  Walking the road and recording distress type,
  severity, and extent.
  FWD (Falling Weight Deflectometer):
  measures structural capacity.
  Ground Penetrating Radar: subsurface condition.
  Modern: automated van-mounted systems
  (LIDAR + cameras + AI) at highway speed.

  DETERIORATION CURVE:
  PCI
  |  100 \_
  |       \ (slow initial deterioration)
  |        \
  |         \____
  |              \____ (rapid deterioration past ~55)
  |                   \____
  |                        \____
  +-----------------------------> Age

  CRITICAL INSIGHT:
  Cost of treatment at PCI 70: $1-3/sq yd (crack seal)
  Cost of treatment at PCI 55: $3-8/sq yd (mill/overlay)
  Cost of treatment at PCI 40: $10-20/sq yd (full depth)
  Cost of treatment at PCI 25: $30-60/sq yd (reconstruction)

  Preventive maintenance at PCI 70 costs 10x less
  than reconstruction at PCI 25.
  Deferred maintenance always costs more.
  (This is technical debt in concrete.)
```

---

## Life-Cycle Cost Analysis (LCCA)

LCCA is **total cost of ownership (TCO) analysis** for physical infrastructure — the same framework any enterprise leader uses to evaluate build-vs-buy decisions, with construction cost replacing license fees, O&M replacing support contracts, and rehabilitation replacing upgrade cycles. The discount rate debate (3%? 7%?) drives the same sensitivity as choosing a depreciation schedule for cloud infrastructure.

LCCA evaluates the total cost of an asset over its design life, accounting for time value of money.

```
LCCA FRAMEWORK:

  Total LCC = Initial Construction Cost
            + PV(Operations & Maintenance)
            + PV(Rehabilitation)
            + PV(Replacement)
            - PV(Residual Value)

  Where PV = Present Value = FV / (1+r)^n
  r = discount rate (typically 3-4% real for
      public infrastructure)

EXAMPLE: Stormwater System

  OPTION A: Gray infrastructure (pipe)
  Construction:  $2.5M
  O&M:           $80K/yr for 50 years
  Rehabilitation: $500K at year 25
  Replacement:   $2.5M at year 50
  PV (3% rate):  $5.8M over 50 years

  OPTION B: Green infrastructure (bioswales, rain gardens)
  Construction:  $1.2M (25% less upfront)
  O&M:           $120K/yr (higher mowing, replanting)
  Rehabilitation: $200K at year 20
  Replacement:   distributed (plant replacement)
  PV (3% rate):  $3.9M over 50 years

  Green wins on LCCA despite higher O&M.
  Plus co-benefits: heat reduction, aesthetics,
  habitat, groundwater recharge.

COMMON LCCA MISTAKE:
  Award contract to lowest initial bid.
  Cheap construction = high maintenance.
  Cheap materials + poor installation =
  early failure = expensive reconstruction.
  LCCA corrects for this.

  DOT practice: Low bid + LCCA adjustment.
  Some contracts require contractors to
  warrant performance (gives them incentive
  to build quality).
```

---

## Utility Coordination: The "Dig Once" Problem

Every utility company digs up the same streets, independently, at different times.

```
THE DIG ONCE PROBLEM:

  Year 1: Water main replacement
  [==========DIG==========]

  Year 2: Gas main upgrade (same street)
  [==========DIG==========]

  Year 3: Fiber optic installation
  [==========DIG==========]

  Year 4: Electric conduit upgrade
  [==========DIG==========]

  Each dig:
  - $500K-2M per block in disruption costs
  - Traffic impact + business disruption
  - Pavement life reset to zero
  - Utility coordination cost

  DIG ONCE SOLUTION:
  Coordinate all utility work into single
  excavation. Install conduit for future
  utilities (fiber, future needs).

  POLICY TOOLS:
  Utility notification systems (811/JULIE/MISS DIG)
  Right-of-way (ROW) coordination ordinances
  Municipal utility tunnels (London Mail Rail,
  Helsinki service tunnels under city center)
  Conduit-in-conduit (micro-trench for fiber)

  SUBSURFACE UTILITY ENGINEERING (SUE):
  ASCE 38-22 quality levels:
  QL-D: Record research only (maps)
  QL-C: Field observation + mark visible features
  QL-B: Geophysical detection (GPR, EM)
        (shows horizontal location, not depth)
  QL-A: Expose actual utility (test holes)
        (exact 3D location confirmed)

  "Hit utilities" (misidentified locations)
  cost $1B+/yr in US.
  QL-A for critical utilities prevents the
  most expensive failures.

  MICROSOFT DATA CENTER CONTEXT:
  When Microsoft sites a data center, utility
  coordination is mission-critical:
  - Power: High voltage transmission + distribution
  - Water: Cooling water supply and return
  - Fiber: Redundant diverse fiber paths
  - All must be coordinated in the ROW
  - Dig once where possible
  - Underground vs overhead resilience tradeoff
```

---

## Stormwater and Green Infrastructure

### The Problem: Impervious Surface and Runoff

```
IMPERVIOUS SURFACE IMPACT:

  Natural ground (pre-development):
  +--------------------------------+
  |  Precipitation: 100%           |
  |                                |
  |  Evapotranspiration: 40%       |
  |  Shallow groundwater: 25%      |
  |  Deep groundwater: 25%         |
  |  Runoff: 10%                   |
  +--------------------------------+

  Urban area (75% impervious):
  +--------------------------------+
  |  Precipitation: 100%           |
  |                                |
  |  Evapotranspiration: 25%       |
  |  Shallow groundwater: 10%      |
  |  Deep groundwater: 5%          |
  |  Runoff: 55%       ^^^^^^^^    |
  +--------------------------------+
  5x increase in runoff volume.
  Faster concentration time.
  Higher peak flows.
  Channel erosion + downstream flooding.
  Combined sewer overflow (CSO) events.

COMBINED SEWER OVERFLOW (CSO):
  ~770 US cities have combined sewers
  (storm + sanitary in same pipe).
  In heavy rain, pipe overflows to
  water body -- raw sewage + stormwater.
  EPA consent decrees requiring CSO
  reduction: multi-billion dollar compliance.
  Example: DC Clean Rivers Project: $2.6B
  tunnel system to capture CSO.
```

### Green Infrastructure: The Alternative

```
GREEN INFRASTRUCTURE TOOLKIT:

  BIORETENTION (Rain Garden):
  +------------------+
  |   \  /  \  /    |  Engineered soil mix
  |    \/    \/     |  (high infiltration rate)
  |================|  Overflow to storm sewer
  |  gravel layer  |  at capacity
  +------||--------+  Infiltrate to groundwater
         ||
  Underground to groundwater or storm sewer.
  Sized for a design storm (1.25" typical).
  Cost: $5-15K per 100 sq ft of drainage area.

  BIOSWALE:
  Linear version of bioretention.
  Follows street edge.
  Slows and filters runoff.
  Replaces traditional curb/gutter+pipe.

  GREEN ROOF (see 02-URBAN-FORM.md for UHI).
  50-80% retention of 1-2" storm events.
  Detention (delay) + some retention.

  PERMEABLE PAVEMENT:
  Pervious concrete, permeable asphalt,
  or paving grids with gravel/grass fill.
  Allows infiltration through surface.
  Requires stone reservoir base.
  Maintenance: vacuum sweeping to prevent clogging.
  Cost premium: 25-50% over standard pavement.

  URBAN TREE CANOPY:
  Tree intercepts precipitation (leaf interception).
  One large tree: 1,000-2,000 gallons/yr
  interception and transpiration.
  Root channels increase soil infiltration.
  Most multi-benefit GI option.

GREEN vs. GRAY ECONOMICS:

  EPA Analysis (2013):
  "The Economics of Green Infrastructure":
  Green infrastructure typically 25-75% cheaper
  than gray (pipe) for equivalent stormwater
  management, when co-benefits are counted.

  Co-benefits counted:
  - Energy savings (cooling)
  - Air quality
  - Property value increase
  - Recreational value
  - Carbon sequestration

  Caveat: Co-benefits are real but distributed.
  Hard to monetize for project justification.
  Green typically wins on strict stormwater
  cost/capacity comparison in many contexts too.

SPONGE CITY PHILOSOPHY (China):
  National program (2015): 30 pilot cities.
  Target: 70-80% of precipitation absorbed
  or utilized locally rather than discharged.
  Integrated GI at city scale:
  - Retention ponds integrated into parks
  - Bioswales along all streets
  - Restored wetlands at urban periphery
  - Green roofs on public buildings
  Mixed results in implementation
  (engineering quality variable, some
  flood disasters still occurred). But
  the integrated systems approach is correct.
```

---

## Resilience Planning

```
CLIMATE RISKS TO URBAN INFRASTRUCTURE:

  SEA LEVEL RISE + STORM SURGE:
  +----------------------------------+
  | Coastal cities: 1-4 ft rise by   |
  | 2100 (RCP4.5), 3-10 ft (RCP8.5)  |
  | Storm surge now compound with    |
  | higher baseline.                 |
  | NYC Sandy (2012): $65B damage.   |
  | Miami Beach: $400M+ seawall,     |
  | pump systems, road raising.      |
  | Jakarta: sinking + sea level =   |
  | capital relocation to Nusantara. |
  +----------------------------------+

  URBAN FLOODING:
  More intense precipitation events.
  Aging stormwater systems sized for
  historical rainfall (not projected).
  "100-year flood" is occurring every
  10-20 years in many cities.
  Green infrastructure + updated
  detention pond sizing.

  EXTREME HEAT:
  Heat dome events. Heat mortality.
  Cooling center networks.
  UHI reduction.
  Passive cooling design standards.
  Peak power demand exceeds grid capacity.

  WILDFIRE (WUI - Wildland Urban Interface):
  Defensible space requirements.
  Non-combustible materials.
  Evacuation route capacity.
  Power shut-off protocols (PSPS in CA).

RESILIENCE FRAMEWORK (UNDRR):
  Prevention/Mitigation: Reduce hazard or exposure
  Preparedness: Capacity to respond
  Response: Emergency management
  Recovery: Reconstruction and restoration

CRITICAL INFRASTRUCTURE INTERDEPENDENCIES:
  Power failure --> pump failure --> water failure
  Water failure --> fire suppression failure
  Telecom failure --> traffic signal failure --> congestion
  These cascading failures are the key threat.
  Resilience requires redundancy at each node.

  MICROSOFT DATA CENTER RESILIENCE:
  N+1 or 2N power redundancy.
  Multiple fiber providers, diverse paths.
  On-site diesel/gas generation.
  Water storage for cooling.
  All of this is urban infrastructure
  resilience thinking applied to a building.
```

---

## Infrastructure Finance

```
FINANCING LANDSCAPE:

  +--------------------------------------------------------+
  |                 INFRASTRUCTURE FINANCE                 |
  |                                                        |
  |  PUBLIC/TAX-BACKED    REVENUE/USER-BACKED   PRIVATE    |
  |  ---------------      ------------------    -------    |
  |  General Obligation   Revenue Bonds         PPP        |
  |  (GO) Bonds           Water/sewer user fees Concession |
  |                       Toll roads            DBFOM      |
  |  Federal grants       Transit fares                    |
  |  (FHWA, FTA,          Airport fees          Developer  |
  |  IIJA, CDBG)                                exactions  |
  |                       Special Assessment    Impact fees|
  |  Tax Increment        District              Mello-Roos |
  |  Financing (TIF)                                       |
  +--------------------------------------------------------+
```

### General Obligation Bonds

```
GO BONDS:

  WHAT: Long-term debt (10-30 years).
  BACKED BY: "Full faith and credit" of
  the issuing government = property tax
  authority (can raise taxes to pay).

  VOTER APPROVAL: Required in most states
  (simple or supermajority).

  INTEREST: Tax-exempt federal (Municipal bonds).
  This is a federal subsidy to municipal
  borrowing: city pays 3-4% interest;
  equivalent taxable bond would be 5-6%.

  USE: Capital projects that benefit
  general public: parks, libraries, roads,
  public buildings.

  TYPICAL TERMS:
  $100M bond at 3.5%, 20 years:
  Annual debt service: ~$7M
  Total interest: ~$40M
  Total repayment: ~$140M
```

### Revenue Bonds

```
REVENUE BONDS:

  WHAT: Long-term debt secured by specific
  revenue stream, not general taxes.

  BACKED BY: Fees from the specific enterprise
  (water rates, sewer charges, airport fees, tolls).

  NO VOTER APPROVAL (typically).
  Only the fee revenue at risk -- not taxes.
  Higher interest rate than GO bonds
  (more risk, no tax backstop).

  USE: Self-funding enterprises -- water/sewer
  utilities, airports, toll facilities, ports.

  RATE COVENANT:
  Bond indenture requires maintaining rates
  sufficient to cover: O&M expenses +
  debt service + rate coverage ratio (1.25x typical).
  This is a contractual constraint on
  rate-setting that protects bondholders.

  REVENUE BOND vs GO BOND:
  Revenue bond: enterprise finances itself.
  GO bond: general taxpayers backstop.
  Revenue bond: no tax pledge, self-contained.
  GO bond: voters must approve, broadest support.
```

### Tax Increment Financing (TIF)

TIF is one of the most widely used (and most controversial) infrastructure finance tools.

```
TIF MECHANISM:

  BASE YEAR:
  Tax rolls frozen at current assessed value.
  Current taxes distributed normally
  to school district, county, city, etc.

         [SCHOOL DISTRICT TAXES]
         [COUNTY TAXES         ]
         [CITY TAXES           ]
         [LIBRARY DISTRICT     ]

  POST-TIF DEVELOPMENT:
  Property value increases due to
  TIF-funded investment.

  Increment = New value - Base year value
  Increment taxes --> TIF district fund
  (school district, county, etc. continue
  to receive only their base year share)

  [BASE TAXES: same as before --> taxing bodies]
  [INCREMENT TAXES: all --> TIF fund]

  TIF FUND:
  Issued TIF bonds against future increment.
  Funds: streets, utilities, affordable housing,
  park, parking structure.
  Infrastructure makes development feasible.
  Development creates increment.
  Increment repays bonds.
  Self-financing (in theory).

  THE TIF CONTROVERSY:

  PROPONENTS: "But for" test: development would
  not occur without TIF. City creates value
  from nothing. Schools get more students
  without any cost increase. Catalytic.

  CRITICS: "But for" test often not met --
  development would have happened anyway.
  TIF "starves" schools for 20-30 years.
  School district gets no share of increment
  while serving more students (from new
  development) on the same base budget.
  TIF has been used to subsidize profitable
  development (eg. Chicago Tribune Tower
  conversion) that needed no subsidy.
  "Corporate welfare" critique.

  REALITY: TIF is a tool. Works well for
  genuinely blighted areas needing
  public investment to become viable.
  Overused: ~$5B/yr in TIF revenue in US,
  much of it capturing value that would
  have been created anyway.
```

### Impact Fees and Developer Exactions

```
IMPACT FEES:

  RATIONALE: New development creates demand
  for infrastructure (roads, parks, water).
  Existing taxpayers should not subsidize
  new development. "Growth pays for growth."

  NEXUS REQUIREMENT (Dolan v. Tigard 1994):
  Fee must have rational nexus to the
  impact of the specific development.
  Cannot charge new development for
  citywide infrastructure improvement
  unless there is a demonstrated impact.
  Fee must be roughly proportional to
  the impact.

  TYPICAL FEES (vary widely by jurisdiction):
  Transportation: $2,000-20,000/unit
  Parks: $1,000-8,000/unit
  Schools: $2,000-15,000/unit
  Water/sewer connection: $5,000-30,000/unit
  Total in high-cost cities: $50,000-150,000/unit

  EFFECT ON HOUSING AFFORDABILITY:
  Impact fees are passed to homebuyers
  (in competitive land markets) or reduce
  feasibility of projects in weak markets.
  San Jose: $72,000 total impact fees/unit
  This is a tax on new housing.
  NIMBYism through fees: communities that
  want to limit growth set very high
  impact fees.

EXACTIONS / CONDITIONS OF APPROVAL:
  Dedications (land: ROW, park, easement).
  In-lieu fees (fee instead of dedication).
  Affordable units (inclusionary zoning).
  Off-site improvements (developer builds
  intersection improvement, sewer extension).
  Designed to offset specific project impacts.
```

### Public-Private Partnerships (PPP)

```
PPP SPECTRUM:

  DESIGN-BID-BUILD (DBB)   <-- Traditional public delivery
  Owner: designs, bids construction, operates
  Risk: public retains all design + operational risk

  DESIGN-BUILD (DB)
  Owner contracts for design+construction combined.
  Faster delivery (overlapped D+C).
  Single point of accountability.
  Public retains operational risk.

  DESIGN-BUILD-OPERATE-MAINTAIN (DBOM)
  Private designs, builds, operates for contract term.
  Performance specifications (LOS requirements).
  Risk: operational performance risk to private.

  DESIGN-BUILD-FINANCE-OPERATE-MAINTAIN (DBFOM)
  Private finances (raises capital), designs,
  builds, operates. Long-term concession.

  AVAILABILITY PAYMENT CONCESSION:
  Government pays private fixed payment
  when facility is "available" (meets LOS).
  Government bears demand risk.
  Private bears design/construction/operational risk.
  Use: where demand risk should be public's
  (courts, hospitals, social infrastructure).

  TOLL CONCESSION:
  Private raises revenue from user fees (tolls).
  Private bears demand risk.
  Use: roads, bridges, airports where
  user fees viable.
  Example: Chicago Skyway (privatized 2005,
  $1.83B to 99-year concession).

  RISK ALLOCATION TABLE:

  RISK TYPE          OPTIMAL BEARER
  Design risk        Private (designer has most control)
  Construction risk  Private (contractor has most control)
  Demand risk        Public (government controls zoning,
                     demographics, alternative routes)
  Regulatory risk    Public (cannot transfer sovereign risk)
  Force majeure      Share or public
  Interface risk     Whoever controls the interface

  PPP VALUE FOR MONEY:
  PPP makes sense when:
  - Private brings genuine expertise/innovation
  - Performance-based contract is possible
  - Term long enough for private to recoup
  - Risk transferred is genuinely manageable by private
  PPP is poor value when:
  - Public can borrow more cheaply (usually true)
  - Risk being transferred not actually manageable
  - Contract term is too short
  - Competition for contract is limited
```

---

## The Infrastructure Gap

```
ASCE INFRASTRUCTURE REPORT CARD (2021):

  Overall grade: C- (was D+ in 2017)

  Roads:          D          Roads and bridges account for
  Bridges:        C          $786B in backlog deferred maintenance.
  Transit:        D-
  Aviation:       D+         Estimated 10-year infrastructure
  Water:          C-         investment need: $2.6 trillion
  Wastewater:     D+         (gap between needs and projected
  Energy:         C-         spending: $2.59 trillion)
  Broadband:      D+

  WHY THE GAP EXISTS:
  - Capital is visible/ribbon-cutting.
    Maintenance is invisible/political liability.
  - Politicians are rewarded for building new,
    not for maintaining old.
  - Infrastructure vote cycles mismatched:
    30-year bridge life vs. 4-year election.
  - Federal "new starts" programs reward
    new projects over maintenance.

  IIJA (2021): $1.2T Infrastructure Investment
  and Jobs Act. Largest federal infrastructure
  investment since Interstate Highway System.
  - Roads/bridges: $110B
  - Rail/transit: $105B
  - Broadband: $65B
  - Water: $55B
  - Electric vehicles/charging: $7.5B

  STRONG TOWNS CRITIQUE:
  "The Growth Ponzi Scheme" (Chuck Marohn):
  Suburban growth pattern generates
  short-term revenue (development fees, taxes)
  but creates long-term infrastructure
  liabilities (roads, pipes, utilities)
  that the tax base cannot sustain.
  Cities are locked in: need more growth
  to fund current obligations, creating
  more future obligations.
```

---

## Common Confusion Points

**"Revenue bonds are safer than GO bonds"**
For the issuer, revenue bonds do not pledge general taxes — they are safer for taxpayers if the enterprise fails (limited liability). For bondholders, GO bonds are safer (backed by taxing power). Revenue bonds carry more credit risk to buyers and therefore carry higher interest rates.

**"TIF is free money"**
TIF borrows against future tax increment. The increment must be real and must exceed the cost of debt service. When TIF districts underperform (common in overly optimistic projections), the city must backstop the bonds or the district fails. TIF also "captures" revenue from schools and other taxing bodies — they lose what would have been incremental revenue.

**"Impact fees are paid by developers"**
In a competitive land market, impact fees are borne by land sellers (the land price is bid down by the amount of the fee) or by homebuyers (passed forward). In weak markets, fees can make projects infeasible. "Developer pays" is a convenient political fiction; the economics are more complex.

**"Green infrastructure is less reliable than gray"**
Gray pipe has defined capacity and performance. Green infrastructure performance varies with maintenance and storm intensity. But gray infrastructure has a single failure mode; green has distributed redundancy. Over-designed gray (pipe too small) fails catastrophically in large storms. Green typically fails gracefully (overflow occurs at surface rather than backing up in basements).

**"The cheapest construction is the best value"**
Life-cycle cost analysis consistently shows that initial construction cost is the wrong metric. Pavement rehabilitation at PCI 70 costs 3-5x less than reconstruction at PCI 40. The decision to defer maintenance is a decision to spend more later — it just defers the cost to the next budget cycle (and often the next administration).

---

## Decision Cheat Sheet

| Finance mechanism | Best for | Key constraint |
|---|---|---|
| GO bonds | Parks, roads, public buildings | Voter approval; full faith and credit pledge |
| Revenue bonds | Water, sewer, airports, transit | Rate covenant; no voter approval needed |
| TIF | Brownfield/blighted area redevelopment | Schools lose increment; "but for" test |
| Impact fees | New development infrastructure | Nexus/proportionality (Dolan); housing cost impact |
| Federal grants (IIJA) | Major projects, match required | 20-80% match; federal requirements (Davis-Bacon) |
| Availability payment PPP | Courts, hospitals, social infra | Complex procurement; higher financing cost |
| Toll concession PPP | High-traffic roads, bridges | Demand risk; public interest vs. private profit |

| Asset type | Key condition metric | Design life |
|---|---|---|
| Pavement | PCI (0-100) | 20-30 years (flexible), 40-50 (rigid) |
| Bridge | NBI condition rating (0-9) | 75-100 years |
| Water main | Break rate, age, material | 50-100 years |
| Sewer | CCTV grade, inflow/infiltration | 50-100 years |
| Building | Facility Condition Index (FCI) | 50-75 years |
