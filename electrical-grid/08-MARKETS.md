# Electrical Grid — Electricity Markets
## ISOs, LMP, Day-Ahead, Capacity Markets, and the Economics of Power

---

## The Big Picture: Market Structure

```
ELECTRICITY MARKET STRUCTURE (US):

┌────────────────────────────────────────────────────────────────────────────┐
│                    WHOLESALE ELECTRICITY MARKETS                           │
├──────────────────────────────────────────────────────────────────────────── │
│  ISO/RTO Competitive Markets          Non-ISO Regulated Utility Areas      │
│  (PJM, MISO, CAISO, ERCOT, etc.)      (Southeast, Pacific NW)              │
│                                                                            │
│  ┌───────────────────────────────┐    ┌──────────────────────────────────┐ │
│  │  ENERGY MARKETS               │    │  TRADITIONAL VERTICALLY          │ │
│  │  • Day-ahead (DA) market       │    │  INTEGRATED UTILITY              │ │
│  │  • Real-time (RT) market       │    │  • Owns generation + T + D       │ │
│  │  • Price mechanism: LMP        │    │  • Rate-of-return regulation     │ │
│  │    (nodal pricing)             │    │  • State PUC sets retail rates   │ │
│  │                                │    │  • No competitive energy market  │ │
│  ├───────────────────────────────┤    └──────────────────────────────────┘ │
│  │  CAPACITY MARKETS             │                                         │
│  │  • Forward capacity auctions  │    Examples: Duke Energy Carolinas,     │
│  │  • Ensure adequate MW exist   │    Southern Company, Xcel Energy        │
│  │    3 years forward            │    Pacific Gas & Electric (hybrid)      │
│  ├───────────────────────────────┤                                         │
│  │  ANCILLARY SERVICES MARKETS   │                                         │
│  │  • Regulation (frequency)      │                                         │
│  │  • Spinning reserve            │                                         │
│  │  • Voltage support             │                                         │
│  └───────────────────────────────┘                                         │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## The Deregulation Story: FERC Orders 888 and 889 (1996)

Before deregulation: vertically integrated utilities (generation + transmission + distribution) in geographic monopolies. They owned it all, operated it all, and a rate commission approved their rates.

**The argument for deregulation:** Competition in generation → lower costs → lower prices. Utilities had no incentive to be efficient; they recovered all costs from ratepayers plus guaranteed return on investment.

**FERC Order 888 (1996):** Required utilities to provide "open access" to their transmission networks — competitors could use the wires at published rates (OATT — Open Access Transmission Tariff). Separated the natural monopoly (transmission) from the competitive function (generation).

**FERC Order 889 (1996):** Required real-time posting of available transmission capacity (OASIS — Open Access Same-time Information System). Prevented utilities from giving affiliate generators preferential access.

**The result:** ISOs and RTOs formed to operate the transmission system neutrally, separate from any market participant's interests. Markets developed to determine which generators run and at what price.

```
PRE-DEREGULATION (1990):              POST-DEREGULATION (2000+):

  Utility Corp                          Generator A (GENCO)  }
  ├── Generation (owned)               Generator B (GENCO)  } Competitive
  ├── Transmission (owned)             Generator C (GENCO)  }
  └── Distribution (owned)                     │
                                               ▼
  State PUC sets rates                   ISO/RTO (independent)
  Utility recovers all costs             ├── Operates transmission
  + guaranteed return                    ├── Runs competitive markets
                                         └── Coordinates dispatch
                                               │
                                               ▼
                                         Distribution Utility (DISCO)
                                         (buys wholesale, sells retail)
                                         State PUC regulates retail rates
```

---

## ISOs and RTOs: The Market Operators

```
US ISO/RTO MAP:

  PJM (PJM Interconnection):
    Territory: Pennsylvania, New Jersey, Maryland + DC + 10 other states
    Load: ~180 GW peak; ~840 TWh/yr
    Customers: 65 million
    The largest competitive wholesale electricity market in the world

  MISO (Midcontinent ISO):
    Territory: 15 states + Manitoba
    Load: ~130 GW peak
    Market: 3-part offer model; strong wind integration

  SPP (Southwest Power Pool):
    Territory: 14 states (Great Plains)
    Focus: heavy wind integration (40%+ of generation)

  CAISO (California ISO):
    Territory: 80% of California
    Load: ~50 GW peak
    Notable: ERCOT-like CA energy crisis 2000-01; duck curve pioneer

  NYISO (New York ISO):
    Territory: New York State
    Notable: complex congestion market; Manhattan-LI congestion

  ISO-NE (ISO New England):
    Territory: 6 New England states
    Notable: high gas dependence; winter supply concern

  ERCOT (Electric Reliability Council of Texas):
    Territory: Most of Texas
    Load: ~85 GW peak; ~400 TWh/yr
    UNIQUE: Not FERC-regulated (intrastate commerce); state-regulated by PUCT
             Energy-only market (no capacity market until proposed 2024)
             Winter Storm Uri 2021: near-complete grid failure, ~$60B economic damage

  Non-ISO areas:
    Southeast: Alabama, Georgia, Mississippi, most of South Carolina, most of Florida
    Pacific NW: Bonneville Power Administration (federal), NV Energy
    Mountain West: Arizona, NM, parts of Nevada, Colorado (joining markets)
```

---

## Locational Marginal Pricing (LMP): The Core Market Mechanism

LMP is the price of electricity at a specific location in the transmission network at a specific time. It is not one price for the whole grid.

### Why Location Matters: Congestion

```
CONGESTION EXAMPLE:

  Node A ─────────── Line AB (limit: 500 MW) ─────────── Node B
  │                                                         │
  Generator A: 100 MW at $20/MWh (cheap gas)              Load B: 1000 MW
  Generator B: 500 MW at $30/MWh (more expensive gas)

  Scenario 1: Line AB NOT congested (can carry 600 MW)
    Dispatch cheapest first: A (100 MW at $20), B (500 MW at $30) plus local Gen C
    LMP at both nodes: ~$30/MWh (last dispatched unit sets price)

  Scenario 2: Line AB AT LIMIT (can carry only 500 MW)
    Can only send 500 MW from cheap generation region to Node B
    Node B needs 1000 MW; local generation must make up the rest
    Local Node B generator (expensive): 500 MW at $80/MWh
    LMP at Node A: $30/MWh (plenty of cheap generation)
    LMP at Node B: $80/MWh (expensive local generation at margin)
    LMP DIVERGENCE = $50/MWh = CONGESTION COST

  RESULT: Same electricity; different prices at different locations
  Generator at A: sells at $30/MWh
  Load at B: pays $80/MWh
  ISO keeps the difference ($50/MWh × 500 MW = $25,000/hour) → Congestion rent
  (redistributed to Financial Transmission Rights holders)
```

### LMP Decomposition

**LMP = Energy + Congestion + Losses**

- **Energy component:** Marginal cost of energy at a reference bus (the "hub" price), system-wide
- **Congestion component:** Additional cost at a specific node due to transmission constraints
- **Loss component:** Marginal cost of line losses at that node (small, ±5% of LMP)

```
EXAMPLE (PJM day-ahead, hypothetical):

  Hub LMP (Western Hub):  $45.00/MWh
  Node X LMP:             $65.00/MWh
    Energy component:     $45.00
    Congestion component: $18.50  (load pocket, constrained import)
    Loss component:        $1.50  (far from generation)

  Node Y LMP:             $38.00/MWh
    Energy component:     $45.00
    Congestion component: -$8.00  (generation surplus in zone, can't export)
    Loss component:        $1.00

  LMP range in real PJM operations:
    Typical (off-peak): $20-50/MWh at most nodes
    Congested (summer peak): $100-500/MWh in load pockets (Manhattan, Boston)
    Scarcity: $1,000-10,000/MWh (rare; ERCOT Winter 2021: $9,000/MWh cap)
    Oversupply: -$50 to -$200/MWh (excess renewable generation)
```

### Financial Transmission Rights (FTRs)

FTRs are financial instruments that hedge against congestion costs:
- An FTR from Node A to Node B entitles the holder to receive congestion rents between A and B
- If LMP at B - LMP at A = congestion cost = $50/MWh, and you hold 100 MW FTR: receive $5,000/hr
- Generators and loads use FTRs to lock in predictable prices across congested paths
- FTRs are allocated to existing transmission owners and auctioned

---

## The Merit Order and Uniform Clearing Price

Economic dispatch is a linear program: minimize sum(C_i * P_i) subject to sum(P_i) = P_demand (power balance), P_i_min <= P_i <= P_i_max (generator limits), and ramp rate constraints. The uniform clearing price is the LP dual variable (shadow price) on the power balance constraint — the textbook definition of a competitive market equilibrium. LMP congestion components are shadow prices on transmission line flow constraints. The entire wholesale electricity market mechanism is LP duality made into real-time policy.

```
MERIT ORDER DISPATCH + UNIFORM CLEARING PRICE:

                          MW demand at hour t = 8,000 MW
                                              │
Cost     Nuclear, wind, solar                 │ All dispatched generators
$/MWh    (near zero marginal cost)            │ receive clearing price!
         │                                    │
  $80    │                             ┌──────▼───────┐ ← CLEARING PRICE
         │                    ┌────────┘    Peaker     │   set by marginal unit
  $50    │           ┌────────┘  Coal/Oil  │           │
         │  ┌────────┘  CCGT gas          │           │
  $30    │  │                             │           │
         │  │                             │           │
  $10    │  │                             │           │
         │──┘                             │           │
   $0    │                                │           │
         └────────────────────────────────┴───────────┴──▶ MW
         0        2000       4000       6000       8000 10000

  Nuclear and wind at $5/MWh → run; also receive $50/MWh clearing price
  CCGT at $30/MWh → dispatched; receive $50/MWh (profit: $20/MWh)
  Coal at $40/MWh → dispatched; receive $50/MWh (profit: $10/MWh)
  Peaker at $50/MWh → marginal unit; receive $50/MWh (breakeven)
  Any unit at $55/MWh → not dispatched

  "UNIFORM PRICE AUCTION": Everyone pays (or receives) the same clearing price,
  set by the most expensive dispatched unit. This is the standard design in
  most US energy markets.
```

**Economic logic of uniform price:** Encourages generators to bid their true marginal cost (not game the bidding). If a generator bids below its cost, it may be dispatched and lose money. If it bids above its cost, it may be excluded when it could have been profitable. The dominant strategy is to bid true marginal cost.

**Renewable pricing impact (merit order effect):** Wind and solar have ~$0/MWh marginal cost. As more wind/solar enters, they push all other generators to the right on the stack. The clearing price is set by ever-more-expensive marginal units... wait, actually the opposite: as more renewables enter at $0 marginal cost, they displace coal and gas that were previously at the margin → clearing price drops. In 2020, German average day-ahead prices dropped 30%+ from pre-Energiewende levels during midday solar hours.

---

## Day-Ahead vs Real-Time Markets

```
TWO SETTLEMENT SYSTEMS (standard in all major US ISOs):

DAY-AHEAD (DA) MARKET:
  Runs: day before delivery (by ~noon for next day)
  Mechanism: demand bids + supply offers → co-optimize → optimal schedule
  Settlement: financially binding forward contract
  Clears at: hourly or sub-hourly intervals
  Why participate: hedge price risk; predictable revenue; commitment certainty
  Generators: want to be committed DA so they know to start up
  Loads: want to lock in price vs face uncertain RT price

REAL-TIME (RT) MARKET (balancing market):
  Runs: every 5 minutes (some markets: 15 min)
  Mechanism: continuous clearing; dispatch instructions to generators
  Settlement: deviation from DA schedules settled at RT price
  Prices: highly volatile; can diverge dramatically from DA

SETTLEMENT EXAMPLE:
  Generator bids 100 MW in DA at $45/MWh → cleared at $45/MWh (DA price = $45)
  Actually generates 110 MW in real time → 10 MW extra settled at RT price
  RT price at that hour = $65/MWh (demand spike)
  Total revenue: (100 MW × $45) + (10 MW × $65) = $4,500 + $650 = $5,150

  If RT price = $20/MWh (mild weather, oversupply):
  Revenue: (100 MW × $45) + (10 MW × $20) = $4,500 + $200 = $4,700

The DA market is the "hedge" — it locks in predictable revenue for ~95% of generation.
The RT market handles deviations and real-time balancing.

VIRTUAL TRADING (financial participants):
  "Virtual supply" bid: buy in DA, sell in RT (if RT < DA, profit)
  "Virtual demand" bid: sell in DA, buy in RT (if RT > DA, profit)
  Financials arbitrage DA vs RT price differences
  Efficiency: improved price convergence between DA and RT
```

---

## Capacity Markets: Paying for Availability

In energy-only markets (like ERCOT historically), generators earn revenue purely from energy (MWh sold). The problem: a peaker with 8% capacity factor earns energy revenue for only 700 hours/year. The energy market may not provide enough revenue to keep peakers (needed for reliability) in operation.

### The Missing Money Problem

```
MISSING MONEY ANALYSIS:

  Gas peaker (CT): Capital cost $450/kW
  Annual fixed cost (capital recovery + fixed O&M): $60/kW/yr = $60,000/MW/yr

  Revenue from energy market:
    8% capacity factor = 700 hours/year
    Average price during those 700 hours: $80/MWh
    Energy revenue: 1 MW × 700h × $80 = $56,000/MW/yr

  SHORTFALL: $60,000 - $56,000 = $4,000/MW/yr missing
  (In volatile markets, scarcity pricing fills this gap — but unpredictably)

  IMPLICATIONS:
    Peakers may retire if energy prices are depressed (high renewables)
    But peakers are NEEDED for the 700 hours they run (system reliability)
    If they retire, reliability degrades → blackouts
    ERCOT learned this painfully: no capacity market → inadequate reserve margins → Uri 2021

SOLUTION: CAPACITY MARKET
  Pay generators for "capacity" = being available = option to generate
  Separate from energy payment
  Revenue: $60-120/kW-year (PJM typical range)
  Ensures generators stay in service even if energy revenue alone is insufficient
```

### PJM Capacity Market: RPM (Reliability Pricing Model)

```
PJM CAPACITY MARKET MECHANICS:

  Annual Base Residual Auction (BRA):
    Held 3 years before delivery (e.g., 2024 auction clears capacity for 2027-28)
    Generators offer capacity (MW available)
    Load Serving Entities (LSEs) required to procure capacity for their load
    ISO clears supply vs demand → clearing price ($/MW-day)

  Demand Curve (VRR — Variable Resource Requirement):
    Not a vertical demand curve (which would cause extreme price volatility)
    Downward-sloping: if excess capacity, price falls; if shortage, price rises
    Design to provide reasonable revenue while limiting price spikes

  CLEARING PRICE EXAMPLES:
    2016-17 delivery year: $59/MW-day = $21,535/MW-year = $21.5/kW-year (very low)
    2021-22 delivery year: $140/MW-day = $51,100/MW-year = $51.1/kW-year (higher)
    2024-25 delivery year (cleared 2022): $28.92/MW-day (very low; excess capacity)
    2025-26 delivery year: $269.92/MW-day (historic high — capacity shortage signal!)

  LOCATIONAL CONSIDERATIONS:
    RTO-wide auction; but "Limited Deliverability" zones
    If a region can't import enough capacity (transmission constraints):
    Local clearing price can exceed RTO price significantly
    Boston: often $200+/MW-day vs RTO $50/MW-day (transmission constrained)
```

**Capacity market controversy:** Critics argue capacity markets are unnecessary (energy markets should provide scarcity pricing), distortionary (keep uneconomic old plants in service), and expensive (transfer wealth from consumers to generators). Proponents argue they provide reliability insurance and predictable revenue for investment. ERCOT's near-miss in February 2021 strengthened the case for capacity markets.

---

## Ancillary Services

Ancillary services are grid services distinct from energy that the ISO procures to maintain system reliability.

```
ANCILLARY SERVICES SPECTRUM (by response speed):

REGULATION (fastest): ±AGC signal, 4-second response
  Provider: generators on regulation, battery storage
  Reason: continuously balances small supply/demand deviations
  Duration: continuous; symmetric (up and down equally)
  Compensation: $/MWh for capacity held + $/MW for performance
  Market: $5-30/MWh (varies widely; CAISO pays premium for batteries)

SPINNING RESERVE: Online, can respond within 10 minutes
  Provider: generators synchronized to grid, running below full output
  Reason: backup for sudden large generation loss (unit trip)
  Duration: enough to cover 10-30 minutes until additional reserves respond
  Compensation: $/MWh availability payment
  Market: $5-20/MWh (less than regulation; slower response value)

NON-SPINNING (SUPPLEMENTAL) RESERVE: Offline, can respond within 10 minutes
  Provider: cold generators capable of fast start (gas CT typically)
  Reason: additional insurance beyond spinning reserve
  Duration: respond within 10 min, sustain for 30-60 min
  Compensation: $/MWh availability payment
  Market: $2-10/MWh

REPLACEMENT/TERTIARY RESERVE: Can respond within 60 minutes
  Provider: slower generators, demand response
  Reason: restore spinning/regulation reserves after they're consumed
  Duration: long enough to restore previous reserve levels

VOLTAGE/REACTIVE SUPPORT: Provide or absorb reactive power
  Provider: generators with reactive capability, SVCs, STATCOMs
  Reason: voltage stability across grid; can't be transmitted long distances
  Compensation: typically cost-of-service (cost recovery), not market price
  Often "must-run" requirements on specific generators near load centers
```

### Battery Storage and Ancillary Services Premium

```
BATTERY ADVANTAGE IN REGULATION MARKETS:

Speed comparison:
  Gas peaker (CTG):          responds in 2-5 minutes
  CCGT:                      responds in 1-3 minutes
  Hydro:                     responds in 30-60 seconds
  Battery storage:           responds in < 100 milliseconds (150ms typical)

Performance-based regulation (PBF):
  PJM, CAISO, MISO use performance-based scoring
  "Mileage" metric: how many times and how precisely did you respond?
  Fast/accurate (battery): high performance score
  Slow/imprecise (gas): low performance score
  Payment: $/MWh × capacity × performance score

  Battery earns: 2-3× what a slow gas unit earns for same MW of regulation
  This makes regulation the highest-value market for batteries in PJM and CAISO
  Hornsdale Power Reserve (Australia): earned 2× projected revenue in year 1
  from frequency regulation alone
```

---

## Power Purchase Agreements (PPAs)

Not an ISO market product — PPAs are bilateral contracts between generator and offtaker, bypassing the spot market.

### Physical PPA

```
PHYSICAL PPA STRUCTURE:

  Generator (wind farm)         PPA Contract              Offtaker (utility)
  ┌────────────────────┐        $/MWh, 15-25 years        ┌───────────────┐
  │ Nameplate: 200 MW  │  ←──── Fixed price: $35/MWh ───── │ Utility LSE  │
  │ CF: ~35%           │  ←──── Delivery point: grid ────── │ (or corporate)│
  │ Annual output:     │        All energy physically       └───────────────┘
  │  ~613 GWh/yr       │        delivered                   Physically buys
  └────────────────────┘                                    and uses the energy

TERMS:
  Duration: 10-25 years (long-term certainty enables project finance)
  Price: fixed $/MWh (hedge against energy price volatility)
  Indexing: some PPAs: CPI-escalator, or partial index
  Shape risk: wind generates when it generates → utility may not want that shape
  Firming: utility may need "firm" power (guaranteed MW) → need storage or backup
  Physical delivery: actual kWh change hands
```

### Virtual PPA (VPPA) / Financial PPA

Corporate renewable procurement (Amazon, Google, Microsoft, Meta) often uses VPPAs because:
- Company doesn't need physical delivery to their facilities
- They want to "green" electricity they buy from local utility in a different region
- Financial settlement allows any geography

```
VPPA STRUCTURE:

  Wind farm in Texas (ERCOT)        Financial settlement      Microsoft data center
  ┌────────────────────────┐        Contract for Differences  ┌─────────────────┐
  │ Generate electricity   │  ←──── Strike price: $30/MWh ─── │  Buys local     │
  │ Sell into ERCOT spot   │        Duration: 20 years        │  grid power at  │
  │ market at market price │                                  │  market rate    │
  └────────────────────────┘                                   └─────────────────┘
           │                                                           │
           │ Settle difference with Microsoft:                        │
           │ If ERCOT spot = $25 (below strike):                     │
           │   Microsoft pays wind farm $5/MWh difference            │
           │ If ERCOT spot = $45 (above strike):                     │
           │   Wind farm pays Microsoft $15/MWh difference           │
           │                                                          │
  MICROSOFT'S ECONOMICS:                                             │
    Earns more from VPPA when prices high → offsets higher grid costs │
    Net cost: approximately the $30/MWh strike price                 │
    Gets RECs (renewable energy credits) from Texas wind             │
    Claims renewable energy for sustainability reporting             │

VPPA ADVANTAGES:
  ✓ No physical delivery constraint (can be anywhere)
  ✓ No "shape risk" (wind generates when it generates — financial settlement)
  ✓ RECs for sustainability claims
  ✓ Long-term price hedge for both parties
  CONSIDERATION: "Additionality" debate — does this actually cause new renewable
  capacity to be built? (It generally does — project finance requires the PPA)
```

### Corporate PPA Market Scale

```
CORPORATE RENEWABLE PPA (2023):
  Total US corporate PPA: ~50 GW contracted (cumulative)
  Top buyers: Amazon (~23 GW), Microsoft (~10 GW), Meta (~8 GW), Google (~7 GW)
  Drivers: RE100 pledge, Scope 2 emissions, electricity cost hedging, ESG metrics
  Market: BloombergNEF tracked 37 GW new corporate PPA in 2023 alone
  Impact: Corporate PPAs are a primary driver of new wind/solar development
```

---

## Electricity Price Formation: What Drives the Price

```
PRICE FORMATION SUMMARY:

SHORT-TERM (daily):
  Primary driver: fuel costs (natural gas price dominates US wholesale)
  Gas $3/MMBtu → CCGT marginal cost ~$20/MWh → wholesale ~$25-40/MWh
  Gas $8/MMBtu → CCGT marginal cost ~$53/MWh → wholesale ~$55-70/MWh

  Demand: hot summer → high AC load → high prices; mild spring → low prices
  Renewables: high wind/solar → push gas off margin → lower prices
  Congestion: transmission limits → LMP spikes in constrained areas

MEDIUM-TERM (monthly/seasonal):
  Gas storage levels (is winter supply adequate?)
  Hydro conditions (drought in West → lower CF → higher prices)
  Generator outage schedule (when do nuke/coal units refuel/overhaul?)
  Forward gas prices (NYMEX Henry Hub curve)

LONG-TERM (years):
  Capacity adequacy: are enough plants in service?
  Capacity factor trends: retiring coal → less supply → higher prices
  New renewable entry: more solar → lower midday prices
  Demand growth: more EVs, data centers → higher load → higher prices
  Carbon policy: carbon price → higher gas/coal generation cost → higher prices

PRICE VOLATILITY EXAMPLES:
  ERCOT Winter Storm Uri (Feb 2021):
    Price cap hit: $9,000/MWh for extended periods
    Total cost: ~$50B in consumer bills + debt
    Some generators: $30,000/MWh average revenue during the week

  California heat dome (Sep 2022):
    CAISO peak hour price: $2,000-5,000/MWh
    Grid operator issued flex alerts; narrowly avoided blackouts

  European natural gas crisis (2022):
    UK/Germany day-ahead: $1,000-1,500/MWh (yes, per MWh) in winter
    Driven by: Russia gas supply cut, LNG competition from Asia
    US comparatively insulated (domestic gas production)
```

---

## Energy Arbitrage: Storage Economics in Markets

```
BATTERY STORAGE ARBITRAGE LOGIC:

  Revenue = (Discharge price - Charge price) × MWh × Round-trip efficiency - Operating costs

  EXAMPLE (California CAISO, 2023):
    Off-peak price (10am-2pm solar surplus): $0-20/MWh (sometimes negative)
    Peak price (5pm-9pm evening ramp): $80-150/MWh
    Spread: $80-150/MWh
    100 MW / 400 MWh BESS, 90% round-trip efficiency
    Daily cycle: charge 400 MWh at $10/MWh, discharge 360 MWh at $100/MWh
    Revenue: 360 MWh × $100 = $36,000
    Cost of charging: 400 MWh × $10 = $4,000
    Net: $32,000/day
    Annual (250 operating days): $8M/yr from arbitrage alone
    (Plus capacity payments + ancillary services for total of $12-20M/yr)

PRICE CANNIBALIZATION LIMIT:
  As more batteries build out in California, they ALL charge at the same
  off-peak hours and discharge at the same peak hours.
  Effect: off-peak prices rise (battery demand), peak prices fall (battery supply)
  → spread narrows → arbitrage revenue declines
  This is the same "value deflation" problem as solar
  First-mover advantage; later projects earn less
```

---

## Market Design Challenges: Texas as a Case Study

ERCOT is the most interesting US market for understanding market design tradeoffs.

**What makes ERCOT unique:**
- No FERC jurisdiction (intrastate commerce)
- Energy-only market (no capacity payments until proposed reform 2024)
- No mandatory renewable portfolio standard (just incentives)
- Complete market price cap: $9,000/MWh (raised from $3,000 after Uri)
- Relies on scarcity pricing for investment signals

**The Winter Storm Uri Failure (February 2021):**
```
ERCOT URI FAILURE ANATOMY:
  Cold snap: -18°F in Texas (far below design temperature for ERCOT equipment)
  Generation: thermal plants (gas, coal, some nuclear) freeze:
    - Gas wellheads freeze → fuel supply cut
    - Gas plant instruments freeze → forced outages
    - Nuclear unit (Wolf Creek): cooling tower froze
    Total loss: ~30 GW of generation, simultaneously
  ERCOT had ~85 GW of capacity; lost 30 GW → reserve margin evaporated

  Market response:
    ERCOT hit system-wide offer cap ($9,000/MWh) for ~80 hours
    Total uplift cost: ~$50B (socialized across all ratepayers)
    Some generators earned $9,000/MWh for 80 hours → windfall

  Lessons:
    Energy-only markets provide incentives for weatherization in theory
    but $9,000/MWh cap may not recover weatherization costs over 10+ years
    Winter fuel security requires PIPELINE winterization (gas supply chain)
    Interconnection isolation limits mutual aid
    Market design does not guarantee physical reliability under extreme stress
```

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| What is an ISO/RTO? | Independent System Operator / Regional Transmission Organization — independent entity that operates transmission and runs competitive wholesale markets |
| What is LMP? | Locational Marginal Price — cost of serving one more MW of load at a specific grid node, including energy + congestion + losses; varies by location and time |
| What causes LMP congestion? | Transmission line at thermal limit can't carry cheapest generation to load → must use more expensive local generation → price diverges between nodes |
| Day-ahead vs real-time market? | DA: financially binding schedule for next day, run day before; RT: 5-minute balancing, settles deviations from DA schedule |
| What is a capacity market? | Forward market paying generators for availability (MW available), not energy produced; ensures adequate generation capacity exists 3 years forward |
| What is the "missing money" problem? | In energy-only markets, peakers earn insufficient revenue from infrequent dispatch → may retire → reliability gap; capacity markets fill this gap |
| What are ancillary services? | Grid services beyond energy: regulation (fast frequency control), spinning reserve (online backup), non-spinning reserve (fast-start backup) |
| What is a physical vs virtual PPA? | Physical: actual electricity delivered to offtaker; Virtual/Financial: contract-for-differences financial settlement, no physical delivery |
| Why do batteries earn premium regulation payments? | Millisecond response vs minutes for gas; performance-based markets pay premium for speed and accuracy (2-3× more than slow resources) |
| What is uniform clearing price? | All dispatched generators receive the clearing price set by the marginal (most expensive dispatched) unit, regardless of their offer price |

---

## Common Confusion Points

**LMP vs "the wholesale price":** When news reports cite a wholesale electricity price, they usually cite a hub price (e.g., PJM Western Hub). This is the energy component of LMP at a reference bus. Actual prices vary by node. Congested nodes can be $50-300/MWh above the hub price in real operations.

**Capacity market "capacity" is not energy:** Paying $50/MW-day for capacity is not paying for electricity. It's paying for the *option* to call on that generator — availability insurance. A generator that gets paid capacity payments and never generates has still earned its capacity payment (assuming it was available when called).

**Carbon-free energy claims and VPPA:** A company buying a VPPA from a Texas wind farm does not power their California data center with wind energy. The electrons are separate. What they're buying is the attribute (renewable energy certificate) and the financial hedge. The "matching" is accounting, not physical. This creates debate about whether VPPAs are meaningful for emissions reduction — they are if they drive additionality (new capacity built that wouldn't have been otherwise), which PPAs generally do.

**Scarcity pricing and market power:** During scarcity (very tight supply), LMP prices can spike to $10,000/MWh. This is theoretically correct market design (scarcity has value; high prices signal need for new investment). In practice, if a generator can physically affect whether the price is $100 or $10,000/MWh by holding back supply, this is market power abuse. FERC monitors for and penalizes market manipulation.

**Why ERCOT has no capacity market:** Ideological commitment to pure market design. The theory: if energy prices can spike to $9,000/MWh during scarcity, this provides sufficient investment signal for new generation. The practice: high caps are politically sustainable for the hours they occur but may not provide reliable incentives for weatherization, seasonal reliability investments, or specific resource types needed. ERCOT is debating adding a capacity mechanism after Uri.

---

*Next: 09-RESILIENCE.md — N-1 criterion, cascading failures, the 2003 Northeast blackout in full detail, hardening*
*See also: 06-ENERGY-STORAGE.md for storage revenue stacking across energy, capacity, ancillary services*
