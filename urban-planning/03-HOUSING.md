# Housing Markets and Policy

## The Big Picture

Housing markets are economically unusual: inelastic supply (building takes years), inelastic demand (people need shelter), durable assets (buildings last 50-100+ years), and location-specific (you cannot move a unit to where demand is higher). These characteristics combine to make housing markets volatile and policy interventions frequently counterproductive.

```
+------------------------------------------------------------------+
|                    HOUSING SYSTEM                                 |
|                                                                  |
|  DEMAND SIDE            SUPPLY SIDE            POLICY LEVERS    |
|  -----------            -----------            ------------      |
|  Population growth      New construction       Zoning            |
|  Income levels          (flow)                 (supply quantity) |
|  Interest rates                                                  |
|  Household formation    Existing stock         Rent regulation   |
|  In-migration           (stock)                (price limits)    |
|                                                                  |
|  TENURE CHOICE:         Demolition/           Subsidies          |
|  Own vs. rent           conversion            (supply-side:      |
|  (tax policy,           (exits from stock)    LIHTC, public      |
|  wealth, mobility)                            housing)           |
|                                               (demand-side:      |
|                                               vouchers, tax      |
|                                               deductions)        |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|                    HOUSING MARKET OUTCOMES                        |
|  Price levels    Affordability    Neighborhood composition        |
|  Vacancy rates   Tenure mix       Commute patterns               |
|  Crowding        Homelessness     Segregation                    |
+------------------------------------------------------------------+
```

---

## Housing Market Economics: Foundations

### Land as the Fundamental Scarce Resource

Ricardo's theory of rent (1817) explains why land near desirable locations commands a premium: land is fixed in supply. All productivity gains from location are captured in the price of land, not labor or capital.

```
RICARDIAN RENT:

  A and B are identical farmers.
  A farms fertile land near market.
  B farms poor land far from market.

  A earns: revenue - costs + LOCATION PREMIUM
  B earns: revenue - costs (just survives)

  A's location premium = ECONOMIC RENT
  (the return to location, not to effort)

  In urban land:
  ECONOMIC RENT = value of location
               = premium over least desirable
                 (but still used) location

  Henry George (1879, "Progress and Poverty"):
  Tax only land value (not improvements).
  Land tax: cannot be passed to renters
  (supply fixed), encourages development
  (you pay whether you build or not),
  captures publicly created value.
  Single Tax movement. Georgist economics.
  Modern form: Land Value Tax (LVT).
```

### Alonso's Bid-Rent Theory (1964)

Households and firms bid for land based on the value they derive from proximity to the city center (jobs, customers).

```
BID-RENT FUNCTION:

  RENT
  |
  |  Retail
  |  (highest bid near center,
  |   steepest gradient)
  |    \
  |     \   Office
  |      \    \
  |       \    \  Residential
  |        \    \    \
  |         \    \    \________
  |          \    \____________
  |           \_________________
  |
  +--------------------------------> DISTANCE FROM CENTER

  Each use bids its maximum willingness
  to pay at each distance.
  The envelope of all bid-rent curves
  = the actual rent surface.

  RESULTS:
  - Retail/office at center (highest gradient)
  - Residential in middle ring
  - Industrial/warehouse at periphery

  MODIFIED BY:
  - Multiple employment centers (polycentric)
  - Transit (extends center access)
  - Amenities (parks, schools, water)
  - Disamenities (noise, pollution, highways)
```

### Muth-Mills Monocentric City Model (1969)

The formal spatial model of the city. Workers maximize utility subject to:
- Housing cost (decreases with distance)
- Commuting cost (increases with distance)
- Income constraint

```
MUTH-MILLS EQUILIBRIUM:

  Housing consumption (lot size)
  increases with distance.
  Rent decreases with distance.
  At equilibrium: nobody prefers to move.

  Commuting cost gradient = housing cost
  gradient + utility gradient = 0

  IMPLICATIONS:
  - Lower-income households live closer
    to center (high rent, high density)
    OR farther out (low rent, but high
    commuting cost relative to income)
  - Middle class: suburbs (car commute,
    large lot, lower rent)
  - Rich: either inner-city premium
    (amenity access) or exurban
    (large estate, long commute tolerated)

  MODEL BREAKS DOWN:
  - Multiple employment centers
  - Telecommuting (post-COVID)
  - Amenity-driven location
  - Racial/socioeconomic sorting
    (not just economics)
```

### The Filtering Model

New construction enters at the top of the market (where margins are highest). Over time, buildings age and depreciate, filtering down to lower-income occupants.

```
FILTERING PROCESS:

  NEW LUXURY UNITS
  (High-income tenants)
        |
        | Time + depreciation
        v
  UPPER-MIDDLE UNITS
  (Previous luxury units, now older)
        |
        | Time + depreciation
        v
  MIDDLE-INCOME UNITS
        |
        | Time + depreciation
        v
  WORKFORCE HOUSING
  (Previous middle units, substantially aged)
        |
        | Time + neglect
        v
  LOW-INCOME / SUBSIDIZED
  (Very old, poor condition)
        |
        | Abandonment or demolition
        v
  EXITS STOCK

  FILTERING WORKS WHEN:
  - Sufficient new supply is added at top
  - Building quality degrades gradually
  - Neighborhood remains stable (not abandoned)
  - Not over-filtered (demolition exceeds
    filtering into affordability)

  FILTERING FAILS WHEN:
  - New supply is restricted (high-cost cities)
  - New units are demolished before filtering
    (teardowns for luxury redevelopment)
  - Neighborhood gentrification reverses
    filtering (renovation increases rents
    back to market level)
  - Supply restriction so severe that
    40-year-old units rent near new prices
    (Manhattan, San Francisco today)
```

---

## Rent Regulation: Evidence and Politics

### First-Generation Hard Rent Control

```
FIRST-GENERATION RENT CONTROL (pre-1970):

  MECHANISM:
  Rent frozen at historical level.
  No or minimal adjustments.

  EXAMPLES:
  NYC pre-1969 "rent control" buildings
  (still ~27,000 units remaining)

  CONSEQUENCES (well-documented):
  - Tenant "lock-in": tenants stay forever
    (rent $400/month in $3,000 market)
  - Massive misallocation of housing
    (single elderly person in 4-bedroom apt)
  - Landlord underinvestment (margins gone)
  - Black market: key money, subletting
  - Conversion to condos (exits rental stock)
  - "Warehousing" (units left vacant)

  Assar Lindbeck (Swedish economist):
  "In many cases rent control appears to be
   the most efficient technique presently
   known to destroy a city -- except for bombing."
  (Quoted approvingly by both sides as
  overstated but directionally correct)
```

### Second-Generation Rent Stabilization

```
SECOND-GENERATION RENT STABILIZATION:

  MECHANISM:
  Annual rent increases permitted at some
  fraction of inflation (CPI-based formula).
  Vacancy decontrol: when tenant leaves,
  landlord can reset to market rate.

  NYC RENT STABILIZATION SYSTEM (RSA/RSL):
  - ~1 million units
  - Covers buildings built 1947-1974
    with 6+ units
  - RGB sets annual increases
  - "Preferential rent" loophole (pre-2019)
  - 2019 HSTPA: vacancy decontrol eliminated,
    preferential rent tied for tenancy
  - Capital improvements: limited pass-through
    now reduced post-2019

  DIAMOND/McQUADE/QIAN (2019):
  San Francisco rent control study.
  Natural experiment: 1994 SF ordinance
  covered small multifamily buildings.
  Buildings just above/below size threshold.

  FINDINGS:
  - Rent-controlled tenants stayed 19%
    longer (desired goal)
  - Landlords responded: 15% reduction
    in rental housing supply
  - Method: converted to condos, sold,
    redeveloped to larger exempt buildings
  - Long-run effect: RAISED rents citywide
    by 5-7% (supply reduction outweighed
    price control benefit)

  TAKEAWAY: Rent control transfers surplus
  to current tenants at cost of future
  tenants and housing supply. Politically
  popular (current voters benefit).
  Economically damaging (future renters
  cannot vote yet).
```

---

## Affordable Housing Production Tools

### LIHTC: The Primary US Affordable Housing Tool

The Low Income Housing Tax Credit (LIHTC, "lie-tech") was created in the 1986 Tax Reform Act. It is the dominant mechanism for affordable housing production in the US.

```
LIHTC STRUCTURE:

  FEDERAL GOVERNMENT
  Treasury/IRS allocates tax credits
  to states (based on population).
          |
          v
  STATE HOUSING FINANCE AGENCY
  Allocates credits to developers
  via Qualified Allocation Plan (QAP).
  QAP scores applications by policy priorities
  (deeper affordability, harder-to-serve,
  TOD location, supportive services).
          |
          v
  DEVELOPER
  Receives tax credits (~$1M/yr for 10 yrs)
  for building/rehabbing affordable units.
  Developer sells credits to investor.
          |
          v
  TAX CREDIT INVESTOR (banks, corporations)
  Buys credits for ~$0.90-$1.05 per $1
  of credit. Gets $10M in tax savings
  for investing ~$9M in equity.
  Also claims losses from depreciation.
          |
          v
  LIMITED PARTNERSHIP STRUCTURE
  Developer (GP) + Investor (LP)
  Investor gets tax benefits.
  Developer gets construction fee + developer fee.

  AFFORDABILITY REQUIREMENT:
  20% of units at 50% AMI (Area Median Income)
  OR 40% of units at 60% AMI
  For 30 years (extended use agreement).

  COST:
  2022 LIHTC: ~$14,000-40,000 per unit
  in federal subsidy, depending on market.
  Total annual: ~$15 billion federal cost.
  Produces: ~100,000-120,000 units/year.

  CRITIQUE:
  Complex (developer + syndicator + investor
  + housing agency + architect + lender =
  "affordable housing industrial complex").
  Transaction costs are high.
  Deeper affordability (30% AMI, ELI) not
  served by LIHTC market-rate cross-subsidy.
  Requires low-income housing to be managed
  by compliance-heavy special-purpose
  entities for 30+ years.
```

### Public Housing: International Comparisons

```
US PUBLIC HOUSING vs. INTERNATIONAL MODELS:

  US PUBLIC HOUSING (1937 Housing Act):
  Built: 1940s-1970s
  Scale: ~1 million units (peak)
  Current: ~970,000 units
  Target: Very low income (<30% AMI)
  Funding: Capital from federal bonds,
           operations from rent (inadequate)

  FAILURES:
  - Concentration of poverty
  - Underfunding of operations/maintenance
  - Physical deterioration
  - Crime concentration
  - Cabrini-Green (Chicago), Pruitt-Igoe
    (St. Louis, demolished), Robert Taylor
    Homes -- became symbols of failure

  HOPE VI (1992):
  Demolished distressed projects.
  Replaced with mixed-income HOPE VI
  communities (LIHTC + market rate + vouchers).
  Displaced residents: outcomes mixed.

  WHY US MODEL FAILED:
  - Concentrated poverty by design
    (means-tested: only very poor)
  - Political isolation (no middle class
    constituency to maintain funding)
  - Architectural determinism (towers-in-park)
  - Chronic underfunding from day 1

  VIENNA GEMEINDEBAU:
  ~220,000 units (60% of residents in
  some form of subsidized housing)
  Income-mixed (middle class also eligible)
  High design quality (competitions)
  Funded by city: 1% payroll tax + residents'
  deposits at entry
  Result: Vienna among world's most
  livable cities, affordable rents,
  no housing crisis

  SINGAPORE HDB:
  Housing Development Board.
  80% of residents in HDB flats.
  Purchased on 99-year lease from HDB.
  Ethnic integration policy (quotas by block
  to prevent racial enclaves).
  City-state = eliminates fragmented governance.
  Uniquely favorable conditions (no suburbs,
  single authority) -- not replicable elsewhere.

  KEY LESSON:
  Public housing works at scale when:
  - Income mixing (not only poor)
  - High design standards
  - Sustained funding
  - Political constituency maintained
  US violated all three.
```

### Housing Vouchers: The Demand-Side Tool

```
SECTION 8 / HOUSING CHOICE VOUCHER (HCV):

  MECHANISM:
  Household pays 30% of income toward rent.
  Federal voucher pays difference up to
  "Payment Standard" (% of FMR = Fair Market Rent).

  SUPPLY-SIDE (Project-Based Vouchers, PBV):
  Voucher attached to a specific unit.
  Tenant cannot take it with them.

  DEMAND-SIDE (Tenant-Based Vouchers, TBV):
  Tenant takes voucher anywhere landlord accepts.
  Portability = key advantage.

  SCALE: ~2.3 million households
  Wait lists: average 2-5 years; some closed
  (Chicago waitlist: 280,000 people for 44,000 vouchers)

  MOVING TO OPPORTUNITY (MTO) STUDY:
  1994-1998 HUD experiment. Random assignment
  of vouchers to high-poverty households.
  Three groups: voucher + counseling to
  low-poverty area, standard voucher, control.

  FINDINGS (Chetty/Hendren/Katz 2016,
  using IRS data to track children):
  - Children who moved at young age to
    low-poverty areas: 31% higher income
    as adults, lower incarceration, better
    health outcomes
  - Adults who moved: small improvement
  - KEY FINDING: neighborhood effects are
    real and large for children
  - Counseling to low-poverty area matters

  POLICY IMPLICATION:
  Vouchers + mobility counseling + source-of-
  income protections (requiring landlords to
  accept vouchers) = powerful tool.
  Without mobility support, vouchers often
  just concentrate in high-poverty areas.

  LANDLORD PARTICIPATION PROBLEM:
  In high-cost markets, landlords don't need
  to accept vouchers (market rents exceed FMR).
  In low-cost markets (high poverty), vouchers
  are easy to use -- in the "wrong" neighborhoods.
  Inspections and payment timing also deter landlords.
```

### Inclusionary Zoning (cross-reference with 01-LAND-USE.md)

### Community Land Trusts (CLTs)

```
CLT MODEL:

  STRUCTURE:
  Nonprofit organization holds land in
  perpetual trust. Sells buildings on
  land to homeowners.

  PERPETUAL AFFORDABILITY MECHANISM:
  Homeowner buys house but not land.
  Ground lease: long-term (99-year
  renewable), requires owner-occupancy,
  restricts resale price.

  RESALE FORMULA (Burlington VT model):
  Seller keeps:
  - 25% of appreciation
  - Value of improvements they made

  CLT keeps 75% of appreciation =
  unit stays affordable forever.

  EXAMPLE:
  Buy CLT house for $200,000.
  Market value grows to $400,000.
  Sell for: $200,000 + 25% of $200,000 = $250,000.
  Seller gains $50,000 (wealth building).
  Next buyer pays $250,000 (not $400,000).
  Affordability preserved.

  vs. STANDARD OWNERSHIP:
  Fully appreciated house = full wealth gain
  for owner, but unaffordable to next buyer.
  CLT: shared equity -- owner and community
  both gain.

  SCALE:
  ~280 CLTs in US. Burlington VT (birthplace),
  Champlain Housing Trust (largest US).
  Community Land Trust Network (UK).

  STRENGTHS:
  Permanent affordability (vs. 30-yr LIHTC
  deed restriction that expires).
  Homeownership wealth-building (vs. renting).
  Community control.

  WEAKNESSES:
  Slow to build portfolio.
  Governance challenges (community board).
  Works best with land grants or donations.
```

---

## Gentrification

### Definition and Evidence

Gentrification: the process by which higher-income residents and investment move into lower-income neighborhoods, typically resulting in rising rents, property values, and demographic change.

```
GENTRIFICATION STAGES (Clay 1979):

  STAGE 1: Pioneer gentrifiers
  Artists, students, risk-tolerant young
  professionals attracted by cheap rent.
  "Urban homesteading." Low displacement.

  STAGE 2: Incremental upgrading
  Renovation, small investment. Restaurants,
  galleries. Rising rents. First displacement
  of lowest-income.

  STAGE 3: Active reinvestment
  Developers renovate buildings.
  Significant rent increases.
  Long-term residents displaced.

  STAGE 4: Completion
  Fully gentrified. High-income, high-rent.
  No affordable housing without subsidy.
  (Brooklyn Heights, SoHo, Capitol Hill Seattle)

WHO GETS DISPLACED:
  Vigdor (2002): Used 1990s Boston data.
  Found: overall displacement rates low
  (most people stay), but disadvantaged
  groups at higher risk.

  Freeman (2005): NYC data. Poor households
  in gentrifying neighborhoods had LOWER
  mobility than comparable poor households
  elsewhere (tied to local social networks).

  "Low displacement" finding: controversial.
  The people who would have moved in
  (future residents priced out) are invisible
  in the data. Selection effects: those who
  remain are more attached; those at highest
  risk may have already left.

WHAT THE EVIDENCE SAYS:
  Gentrification causes some displacement,
  primarily of renters who receive rent
  increases at lease renewal, and of
  lower-income new movers who cannot
  enter the neighborhood.
  School quality loss: documented.
  Social network disruption: documented.
  But severe "whole-neighborhood" displacement
  is less common than often portrayed.
```

### Anti-Displacement Tools

```
ANTI-DISPLACEMENT TOOLKIT:

  RIGHT TO COUNSEL (NYC, SF):
  Tenants facing eviction get free legal
  representation. Dramatically reduces
  eviction rates (NYC: 84% of represented
  tenants kept housing vs 40% unrepresented).

  COMMUNITY BENEFITS AGREEMENT (CBA):
  Negotiated agreement between developer
  and community coalition. Developer provides:
  - Local hiring provisions
  - Affordable housing set-aside
  - Community space
  In exchange for: community support,
  reduced opposition.

  RIGHT TO RETURN:
  For residents displaced by public action
  (public housing demolition, urban renewal),
  right to return to rebuilt units.
  Implementation: often broken in practice
  (HOPE VI right to return: ~25% exercised it).

  PRESERVATION: Acquire and preserve existing
  affordable stock (before conversion to
  market-rate). Cheaper per unit than new
  construction ($50-100K vs $300-500K
  development cost in high-cost markets).

  COMMUNITY LAND TRUST (permanent affordability,
  see above).
```

---

## Homelessness

### Structural vs. Individual Causes

```
HOMELESSNESS CAUSATION DEBATE:

  INDIVIDUAL FACTORS:
  - Mental illness (30-40% of homeless
    have serious mental illness)
  - Substance use disorder (50-60%
    on some measures)
  - Domestic violence (primary cause
    for ~26% of women experiencing
    homelessness)
  - Criminal record (restricts housing access)

  STRUCTURAL FACTORS:
  - Housing affordability: strongest
    predictor of homelessness rate across
    metros is the median rent-to-income ratio
  - Culhane/Metraux: metro areas with
    highest housing costs have highest
    visible homelessness per capita
  - California's homeless crisis mirrors
    its housing cost crisis
  - Individual factors explain who becomes
    homeless; structural factors explain
    how many become homeless

  THE RIGHT QUESTION:
  Not "why do individuals become homeless?"
  (individual factors explain)
  But "why does this country/city have
  this rate of homelessness?"
  (structural factors: housing cost,
  income inequality, safety net gaps)
```

### Housing First Evidence

```
HOUSING FIRST (Pathways to Housing, Sam Tsemberis 1992):

  TRADITIONAL "TREATMENT FIRST" MODEL:
  Street --> shelter --> transitional housing
  --> treatment/sobriety requirements
  --> permanent housing
  Must prove "housing readiness"
  before receiving housing.

  HOUSING FIRST MODEL:
  Street --> permanent housing immediately
  Voluntary services (not required)
  No sobriety requirement
  Assumption: stable housing enables recovery;
  does not follow from recovery.

  EVIDENCE (randomized controlled trials):
  Pathways to Housing NY RCT (2004):
  - Housing First: 80% housed at 2 years
  - Treatment as usual: 30% housed at 2 years
  - Substance use: NO DIFFERENCE at 2 years
    (housing itself does not cause sobriety,
    but it does not require it)
  - Mental health: modest improvement HF group

  At Homes (Canada, 2009-2013):
  - Largest RCT, 5 cities, 2,148 participants
  - Housing First: 62% stably housed at 2 years
  - Treatment as usual: 31%
  - Cost savings: averted hospital, jail,
    emergency shelter costs approximately
    offset HF program costs

  COST ANALYSIS:
  Average cost of chronic homelessness
  (emergency services, hospitalization,
  jail): $30,000-80,000/person/year
  Cost of permanent supportive housing:
  $15,000-25,000/person/year
  Housing First is cheaper.

  POLICY ADOPTION:
  Federal "Opening Doors" strategy (2010):
  explicitly adopted Housing First.
  HUD homeless funding now requires HF model.
  Veterans Affairs Supportive Housing (VASH):
  Housing First for veterans. Dramatic decline
  in veteran homelessness (2009-2022: 55% reduction).
```

---

## Seattle/Bay Area Bridge: Why This Matters for Microsoft

```
TALENT PIPELINE AND HOUSING COSTS:

  Seattle Metro Median Home Price (2024): ~$800,000
  Down payment (20%): $160,000
  Monthly payment (7% rate): ~$4,800/month
  Required income to qualify: ~$185,000/year

  Microsoft entry-level SWE starting salary
  in Seattle: ~$130,000-160,000 base

  IMPLICATION: Entry-level SWEs cannot buy
  homes without substantial equity transfer
  from family or extremely long savings period.

  SF Bay Area: Same or worse.
  NYC: Same or worse.

  RECRUITING CONSEQUENCE:
  Candidates from lower-income backgrounds
  (first-generation, diverse talent pipeline)
  face housing access barrier that candidates
  from wealth (family help with down payment)
  do not face.
  "We pay $160,000 but you can only afford
  to rent a 1-bedroom apartment 45 min from
  the office" is a competitive disadvantage
  vs. Austin, Phoenix, Miami, etc.

  MICROSOFT CAMPUS DECISIONS:
  Redmond HQ in suburb (1986): was a housing
  affordability and sprawl driver -- tech
  campuses pull urban density outward.
  Microsoft's Puget Sound campus: 500+ acres
  of suburban land use.
  Inclusive hiring at scale requires either:
  - Paying enough to clear housing hurdle
    (bid up rents for everyone else)
  - Supporting housing production
    (Microsoft has committed $750M to
    housing fund in Puget Sound)
  - Remote work (the COVID experiment)
  Urban planning is a talent strategy question.
```

---

## Common Confusion Points

**"Rent control reduces affordability"**
Rent control reduces affordability for future renters (supply exits market) while improving affordability for current controlled tenants. Both statements are true simultaneously. The policy redistributes housing security from future to present, from would-be renters to existing tenants.

**"Filtering means only wealthy people need new housing"**
Filtering means new units at any price point free up units for lower-income households through a chain of moves. If a wealthy person buys a new condo, they vacate their older unit, which becomes available to a middle-income person, who vacates theirs for a lower-income person. The chain requires enough links and functioning market conditions.

**"Section 8 vouchers create slums"**
Vouchers enable poor households to rent in the private market. Whether this concentrates poverty depends on where vouchers can be used (payment standard vs. market rents in low-poverty areas), landlord acceptance (source-of-income protections), and mobility counseling. Vouchers themselves are neutral instruments; outcomes depend on program design.

**"Housing First enables addiction"**
The evidence shows no difference in substance use outcomes between Housing First and treatment-first models. What Housing First does is not withhold housing pending sobriety. The choice of treatment vs. treatment-first is false — both can and should be offered; the question is whether housing is conditional on it.

**"Gentrification is primarily about racial change"**
Gentrification often involves racial change (lower-income minority communities --> higher-income white new residents) because of historical patterns of residential segregation and income inequality. But the economic mechanism is income/rent, not race directly. Gentrification also occurs in white working-class neighborhoods near urban cores.

---

## Decision Cheat Sheet

| Policy tool | What it does well | What it does poorly |
|---|---|---|
| Rent control (first-gen) | Protects existing tenants' costs | Destroys housing supply over time |
| Rent stabilization (second-gen) | Reduces churning, tenant stability | Still reduces supply in hot markets |
| LIHTC | Scales affordable production | Expensive per unit; misses very poor |
| Section 8 vouchers | Tenant choice, demand-side flexibility | Wait lists; payment standard gaps |
| Public housing | Can work at scale (Vienna, Singapore) | US model: concentrated poverty + underfunding |
| Inclusionary zoning | Integrates affordable into market | Reduces feasibility; can suppress supply |
| Community land trust | Permanent affordability; wealth building | Slow to scale; governance intensive |
| Upzoning | Reduces price pressure long-run | Produces market-rate, not affordable units |
| Housing First | Proven most effective for chronic homeless | Requires ongoing rental subsidy |

| Affordability measure | Meaning |
|---|---|
| Area Median Income (AMI) | HUD-defined median income for metro area |
| 30% rule | Household paying >30% of income on housing = cost-burdened |
| 50% rule | >50% of income = severely cost-burdened |
| Fair Market Rent (FMR) | HUD's 40th percentile gross rent in metro |
| Affordability gap | Units affordable to 30% AMI households minus households at 30% AMI |
