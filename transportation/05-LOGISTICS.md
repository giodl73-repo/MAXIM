# Logistics and Supply Chain

## The Big Picture

Logistics is the discipline of moving the right thing to the right place at the right time at the right cost. Supply chain management adds the upstream dimension: design the entire network of suppliers, manufacturers, distributors, and customers so that products flow efficiently. The 2020-2022 disruptions demonstrated that supply chains optimized purely for efficiency are fragile — resilience requires redundancy, which costs money.

```
+------------------------------------------------------------------+
|                    SUPPLY CHAIN LAYERS                           |
|                                                                  |
|  NETWORK DESIGN (strategic, multi-year)                          |
|  +----------+ +----------+ +----------+ +----------+             |
|  | Facility | | Mode     | | Inventory| | Make vs  |            |
|  | Location | | Selection| | Placement| | Buy vs   |            |
|  |          | |          | |          | | Outsource|            |
|  +----------+ +----------+ +----------+ +----------+            |
|                                                                 |
|  TRANSPORTATION (tactical, daily-weekly)                        |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Ocean    | | Air      | | Truckload| | LTL/     |            |
|  | Freight  | | Freight  | | (FTL)    | | Parcel   |            |
|  +----------+ +----------+ +----------+ +----------+            |
|                                                                 |
|  WAREHOUSING (execution, hourly)                                |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Receiving| | Storage  | | Pick/Pack| | Shipping |            |
|  | Cross-   | | Slotting | | Order    | | Sortation|            |
|  | docking  | |          | | Mgmt     | |          |            |
|  +----------+ +----------+ +----------+ +----------+            |
|                                                                 |
|  LAST MILE (delivery to customer)                               |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Route    | | Delivery | | Returns  | | Customer |            |
|  | Optim.   | | density  | | (reverse)| | Experience|           |
|  +----------+ +----------+ +----------+ +----------+            |
+------------------------------------------------------------------+
```

---

## Supply Chain Network Design

### Facility Location Models

The strategic question: where to put warehouses, distribution centers, and factories to minimize total cost while meeting service requirements.

```
  NETWORK DESIGN PROBLEM:

  INPUTS:
  - Customer locations and demand (D_i for each customer i)
  - Candidate facility locations (j)
  - Fixed cost to open facility j (f_j)
  - Variable cost to serve customer i from facility j (c_ij)
  - Service constraints (max transit time, coverage requirement)

  OBJECTIVE:
  Minimize: Sum(f_j * y_j) + Sum(c_ij * x_ij)
  Subject to: Each customer served by exactly one facility
              Customer served only by open facility

  This is the p-median (minimize total cost) or
  p-center (minimize maximum distance) problem.
  NP-hard in general; solvable by heuristics for practical sizes.

  PRACTICAL APPROACHES:
  1. Center of Gravity: weighted average of customer locations
     Simple, ignores fixed costs, good starting point
     Cog_lat = Sum(D_i * lat_i) / Sum(D_i)

  2. Integer programming (MILP): exact solution for <200 locations
     Solvers: Gurobi, CPLEX — solve 50-location problems in seconds

  3. Simulation: test candidate configs against demand scenarios
     Monte Carlo for demand uncertainty

  4. Commercial tools: Llamasoft (now Coupa), LLamasoft Guru,
     o9 Solutions — the software layer above the math
```

### DC Network Design

```
  ECHELON STRUCTURES:

  Single-echelon (direct):           Multi-echelon (tiered):
  +----------+                       +----------+
  | Factory  |                       | Factory  |
  +----+-----+                       +----+-----+
       |                                  |
    (direct)                              | (bulk)
       |                             +----+------+
  +----+----+                        |  Regional |
  | Customer|                        |    DC      |
  +---------+                        +---+-+------+
                                         | |
                                    (zone| |(zone)
                                    +----+ +----+
                                    |Local| |Local|
                                    | DC  | | DC  |
                                    +-----+ +-----+
                                         |
                                    +---------+
                                    | Customer|
                                    +---------+

  SINGLE ECHELON: lower fixed cost, higher transport cost
                  (each customer farther from single DC)
  MULTI ECHELON: higher fixed cost (multiple DCs),
                 lower transport cost + faster delivery

  CROSS-DOCKING:
  Freight arrives at facility, sorted immediately, departs
  same or next day. No storage cost. Requires synchronized
  inbound and outbound schedules.
  Used by: Walmart, Amazon (sort centers), UPS (hub operations)
  Works when: demand is predictable, inbound = enough volume
```

---

## Mode Selection and Incoterms

### Incoterms 2020

Incoterms define at which point risk and responsibility transfer from seller to buyer. They are not about payment terms — they are about who is responsible for freight, insurance, and customs at each stage.

```
  INCOTERMS 2020 SPECTRUM:

  Seller           Risk/Cost Transfer Point          Buyer
  bears all                                          bears all
  |                                                       |
  EXW  FCA  CPT  CIP  DAP  DPU  DDP
  |     |    |    |    |    |    |
  |     |    |    |    |    |    +-- Delivered Duty Paid (buyer door, duty paid by seller)
  |     |    |    |    |    +------ Delivered at Place Unloaded (unloaded at destination)
  |     |    |    |    +----------- Delivered at Place (destination, unloaded by buyer)
  |     |    |    +---------------- Cost, Insurance, Paid to (named destination)
  |     |    +--------------------- Carriage Paid To (named destination)
  |     +-------------------------- Free Carrier (seller delivers to carrier)
  +-------------------------------- Ex Works (buyer collects at seller's door)

  PRACTICAL RULES:
  - EXW: seller does minimum. Buyer's problem from factory door.
  - FOB (Free on Board): applies to maritime only. Seller loads vessel;
    risk transfers once on board. Most commodity trading uses FOB.
  - CIF (Cost, Insurance, Freight): seller pays ocean freight and insurance.
    Standard for many manufacturing imports.
  - DDP: seller does everything including destination customs. Rare except
    for e-commerce (Amazon FBA, cross-border DTC).

  NOTE: FOB and CIF exist in Incoterms 2010 and 2020; they are
  maritime-only. Use FCA and CIP for multimodal.
```

### Total Landed Cost (TLC)

The full cost of getting a product to the customer, including all elements hidden in a simple "unit cost."

```
  TOTAL LANDED COST COMPONENTS:

  Unit product cost (ex-factory)
  + Export charges (EXW -> FOB): export customs, inland transport, port fees
  + Ocean freight (container or LCL)
  + Marine insurance
  + Import customs duty (% of declared value; varies by HTS code)
  + Import customs broker fees
  + Port/terminal handling charges (THC)
  + Inland delivery to DC
  + In-transit inventory carrying cost (time x value x WACC)
  + Import compliance (labeling, testing, certifications)
  + Return freight allowance (reverse logistics)
  = TOTAL LANDED COST

  EXAMPLE: Electronics from Shenzhen to US Midwest DC
  Unit cost: $100
  + Ocean freight (share of 40' container): $15
  + US customs duty (3.5% for HTS category): $3.50
  + THC + inland: $8
  + In-transit inventory (18 days x $100 x 10% WACC/365): $0.49
  = TLC: ~$130

  If sourced domestically at $120/unit -> domestic is cheaper despite
  unit cost premium. TLC analysis required for sourcing decisions.
```

---

## Intermodal Transportation

### Container Standards

```
  ISO CONTAINER DIMENSIONS:

  Type         Length  Width  Height  Capacity  Use
  ----         ------  -----  ------  --------  ---
  20' standard 6.06m  2.44m  2.59m   33 m^3    Heavy cargo (steel, machinery)
  40' standard 12.19m 2.44m  2.59m   67 m^3    General cargo
  40' HC (high) 12.19m 2.44m  2.89m  76 m^3    Most common (30cm taller)
  45' HC        13.72m 2.44m  2.89m   86 m^3    Used mainly intra-Europe/US
  Reefer (40')  12.19m 2.44m  2.59m  58 m^3    Temperature controlled (-25 to +25C)

  DOMESTIC US:
  53' container: 16.15m long — cannot go on a ship (too long for ISO)
  Used exclusively for domestic rail/truck (rail boxcars and 53' domestic)
  Enables double-stack rail for domestic intermodal (TOFC obsolete)
```

### Intermodal Flow

```
  OCEAN-RAIL-TRUCK INTERMODAL (US):

  China/Asia
    |
    | Ocean container (20'/40' ISO)
    v
  West Coast Port (LA/Long Beach, Seattle)
    |
    | Rail intermodal (double-stack)
    | 2-5 days to Midwest/East
    v
  Inland Port or Intermodal Ramp
    |
    | Drayage (local truck, 25-100 miles)
    v
  Distribution Center
    |
    | LTL or parcel
    v
  Customer / Retail Store

  KEY ECONOMICS:
  Double-stack train: 200+ cars * 2 containers = 400+ containers
  vs 400 trucks on the highway.
  Rail cost: ~$0.02-0.04 per ton-mile
  Truck cost: ~$0.10-0.15 per ton-mile
  But: rail requires drayage at each end (~$200-400 per container)

  IPI (Interior Point Intermodal): carrier arranges ocean + rail + drayage
  OPI (Overland Point Intermodal): ditto but origin side

  CHASSIS POOLS:
  Containers need a wheeled chassis to move by truck.
  Chassis pools (DCLI, TRAC, Flexi-Van) provide shared chassis.
  Chassis availability crises (2020-2021) revealed hidden fragility.
```

---

## Cold Chain Logistics

The cold chain is a logistics system that maintains temperature-controlled conditions from production to consumption. Failure means product loss, food safety incidents, or drug efficacy loss.

```
  COLD CHAIN TEMPERATURE ZONES:

  Zone            Temperature Range    Products
  ----            -----------------    --------
  Frozen          -18°C or colder      Frozen food, ice cream, some biotech
  Refrigerated    2°C to 8°C           Dairy, fresh meat, pharma (vaccines, insulin)
  Controlled cool 8°C to 15°C          Chocolate, wine, some produce
  Modified atm.   Varies + gas mix      Fresh produce (CA storage)
  Ambient         15°C to 25°C         Room temperature products

  PHARMACEUTICAL COLD CHAIN:
  GDP (Good Distribution Practice) guidelines.
  Deviation > 2-8°C for any duration requires investigation.
  Excursion: any time-temperature deviation from specification
  MKT (Mean Kinetic Temperature): weighted average that accounts
  for Arrhenius degradation kinetics. Not a simple average.

  COVID VACCINE DISTRIBUTION (2020-2021):
  mRNA vaccines (Pfizer/BioNTech): -70°C storage requirement
  No existing cold chain infrastructure for -70°C at scale.
  Solution: dry ice shipping + point-of-use storage only.
  AstraZeneca/Johnson & Johnson: 2-8°C -> deployable globally.
  Temperature requirement was the primary distribution constraint, not
  manufacturing. Perfect example of logistics constraining a rollout.
```

### Active vs Passive Cold Chain

```
  ACTIVE (powered refrigeration):
  +------------------+
  | Refrigerated     | Diesel generator or electric shore power
  | container (reefer)| Maintains temperature ±2°C
  | Temperature log  | Data logger required (GDP)
  +------------------+
  Cost premium: ~3-5x standard container
  Used for: bulk pharma, large food volumes, long duration

  PASSIVE (thermal materials, no power):
  +------------------+
  | Insulated        | EPS/polyurethane foam or VIP (vacuum insulated panel)
  | shipper          | Phase change material (PCM): wax at 2°C or 20°C
  | Temperature log  | Absorbs/releases heat at phase transition
  +------------------+
  Duration: 24-120 hours depending on design
  Used for: individual pharma doses, clinical trials, last-mile
  Validation: must be tested against worst-case ambient profiles
              (ISTA 7E profile for summer/winter temperature extremes)
```

---

## Inventory and Transportation Tradeoffs

### The Fundamental Tradeoff

```
  SHIP LESS FREQUENTLY:           SHIP MORE FREQUENTLY:
  +------------------+            +------------------+
  | Larger batches   |            | Smaller batches  |
  | Lower freight    |            | Higher freight   |
  | per unit         |            | per unit         |
  | Higher cycle     |            | Lower cycle      |
  | stock (average   |            | stock            |
  | inventory = Q/2) |            |                  |
  +------------------+            +------------------+
                  Optimal Q = EOQ

  EOQ (Economic Order Quantity):
  Q* = sqrt(2 * D * S / (h * c))

  Where:
    D = annual demand (units)
    S = ordering/shipping cost per order ($)
    h = holding cost rate (fraction of unit value per year)
    c = unit cost ($)

  EXAMPLE:
  D = 10,000 units/yr, S = $500/order, c = $50, h = 20%
  Q* = sqrt(2 * 10,000 * 500 / (0.20 * 50)) = sqrt(1,000,000) = 1,000 units
  Order frequency = 10 times per year = monthly

  KEY INSIGHT: total cost curve is flat near the optimum.
  Ordering 750 or 1,250 instead of 1,000 barely changes total cost.
  But ordering 100 or 5,000 is significantly worse.
```

### Safety Stock

Safety stock protects against demand variability and lead time variability.

```
  SAFETY STOCK FORMULA:

  SS = z * sigma_LT

  Where:
    z = service level z-score (z=1.65 for 95% service level)
    sigma_LT = standard deviation of demand during lead time

  For combined demand and lead time uncertainty:
  sigma_LT = sqrt(L * sigma_d^2 + d^2 * sigma_L^2)

  Where:
    L = average lead time (days)
    sigma_d = std dev of daily demand
    d = average daily demand
    sigma_L = std dev of lead time (days)

  PIPELINE INVENTORY:
  Inventory in transit = average lead time * average demand
  This is the hidden cost of long supply chains.

  Example: product value $100, daily demand 100 units, sea transit 20 days
  Pipeline inventory = 2,000 units = $200,000 tied up in transit
  Carrying cost at 15% WACC: $200,000 * 15% = $30,000/year
  This appears in NO freight invoice. Easy to miss in TLC analysis.

  POST-COVID SHIFT:
  JIT (Just-In-Time): minimize inventory, lean manufacturing
  -> Lean is fragile when supply disruption materializes
  JIC (Just-In-Case): carry more safety stock, diversify suppliers
  -> More expensive but more resilient
  Current best practice: tiered safety stock by item criticality
```

---

## Last-Mile Delivery

Last-mile is the final delivery leg from distribution center to customer. Disproportionately expensive.

```
  COST DISTRIBUTION IN SUPPLY CHAIN:

  Manufacturing  Ocean freight  Inland freight  Last mile
  ~$0.10/unit    ~$0.15/unit    ~$0.10/unit     ~$3-10/unit!

  LAST-MILE IS 25-50% OF TOTAL DELIVERY COST.

  WHY SO EXPENSIVE:
  - Low density: each stop is unique address (vs pallet to DC)
  - Time windows: customer wants specific delivery time
  - Failed delivery: package not accepted -> re-delivery attempt
  - Urban congestion: truck speed drops to 10-15 mph
  - Labor intensive: driver time >> driving time in urban dense

  DENSITY ECONOMICS:
  Stop density (stops per route-mile) is the key driver.
  1 stop/mile: uneconomic residential
  5 stops/mile: suburban, acceptable
  10+ stops/mile: dense urban, economical

  Daganzo's square-root formula (approximate last-mile cost):
  Cost ~ sqrt(demand_density * service_area)

  Double the area: cost * sqrt(2) = 41% more
  Double the stops per area: cost * sqrt(0.5) = 29% less
  => DENSITY is the ally; SPRAWL is the enemy of last-mile economics.
```

### Vehicle Routing Problem (VRP)

```
  VRP FORMULATION:

  Given:
  - Depot location
  - N customer locations with demand
  - K vehicles with capacity Q

  Find: routes for K vehicles to serve all customers
        minimizing total distance

  This is NP-hard (reduces to TSP, which is NP-hard).
  Exact solution: intractable for N > 20-30.
  Practical solution: metaheuristics.

  CLARKE-WRIGHT SAVINGS ALGORITHM:
  1. Start: each customer on separate route from depot
  2. For each pair (i,j): compute savings S(i,j) = d(D,i) + d(D,j) - d(i,j)
     (savings from merging two routes via depot into direct i->j link)
  3. Sort by S descending
  4. Merge routes greedily if capacity allows

  MODERN APPROACHES:
  - Tabu search: maintain "forbidden" moves list to escape local optima
  - Large neighborhood search (LNS): destroy-repair cycles
  - ML-guided heuristics: predict which customers to cluster together
  - Google OR-Tools (open source): production-quality VRP solver
  - Commercial: Ortec, Paragon, Roadnet

  EXTENSIONS:
  VRPTW: VRP with Time Windows (customer can only receive in window)
  CVRP: Capacitated VRP (vehicle capacity constraint)
  DVRP: Dynamic VRP (new orders arrive during the route)
  MDVRP: Multi-Depot VRP
```

---

## 3PL, 4PL, and Logistics Outsourcing

```
  LOGISTICS PROVIDER SPECTRUM:

  1PL: You own and operate your own trucks/warehouses.
       Amazon (for own operations), Walmart (private fleet).
       Control: maximum. Capital: maximum.

  2PL: Asset-based carrier or warehouse.
       FedEx, UPS, J.B. Hunt, Prologis.
       You contract specific assets.
       Control: moderate. Asset ownership: theirs.

  3PL (Third-Party Logistics):
  Asset-light or asset-based.
  Provides: warehousing + transportation + value-added services.
  Examples: DHL Supply Chain, XPO Logistics, Geodis, CEVA.
  You outsource operations; they manage execution.
  Performance measured by: order fill rate, on-time delivery, cost/unit.

  4PL (Fourth-Party Logistics / Lead Logistics Provider):
  No physical assets. Pure orchestration.
  Manages 3PLs on your behalf. Supply chain control tower.
  Examples: Accenture Supply Chain, some functions of Kuehne+Nagel.
  You outsource the management function itself.
  Performance measured by: network optimization, 3PL SLA compliance.

  WHEN TO USE WHAT:
  +------------------+  Company stage  +------------------+
  | Own everything   |  Large, stable  | 1PL for core,    |
  | (Amazon)         |  predictable    | 3PL for overflow |
  +------------------+  +---------+   +------------------+
                         Growing or
  +------------------+  seasonal vol  +------------------+
  | Full outsource   |  Small-medium  | 3PL for ops,     |
  | to 3PL           |  e-commerce    | 4PL if complex   |
  +------------------+  +---------+   +------------------+
```

---

## Supply Chain Resilience Post-COVID

The COVID-19 pandemic revealed single-point-of-failure risks in hyper-efficient global supply chains. The analysis maps directly to system reliability engineering:

```
  PRE-COVID (JIT optimized):              POST-COVID (resilience-aware):

  Single source for key parts             Multi-source (2-3 suppliers)
  Zero safety stock                       Weeks to months safety stock
  <24h replenishment from supplier        Days to weeks replenishment
  Single geography (China-centric)        Geographic diversification
  Lowest cost = primary criterion         Lowest RISK-ADJUSTED cost

  RESILIENCE STRATEGIES:

  1. Dual/multiple sourcing:
     Cost: 5-15% premium (second source is often less efficient)
     Benefit: continuity during single-source failure
     Same trade-off as N+1 redundancy in data centers.

  2. Inventory buffering:
     Cost: carrying cost (10-20% of inventory value/year)
     Benefit: X days of supply during disruption
     Same trade-off as hot standby vs cold spare in systems.

  3. Supply chain visibility platforms:
     project44, FourKites, Shippeo: real-time tracking of all in-transit
     inventory across all modes (ocean, rail, truck).
     Analogous to application performance monitoring (APM) for supply chains.
     Enables: faster reaction to disruptions, proactive customer notification.

  4. Nearshoring/friendshoring:
     Move production closer to consumption (US: Mexico, Central America)
     or to politically aligned countries (EU: Eastern Europe, Morocco).
     Cost premium: 10-30% higher unit cost
     Benefit: shorter lead times, lower geopolitical risk, lower carbon.

  THE BULLWHIP EFFECT:
  Small demand fluctuation at retail -> amplified inventory variation
  at each upstream tier.
  Cause: each tier adds safety stock; order batching; price promotion effects.
  Mitigation: VMI (Vendor-Managed Inventory), demand signal sharing,
              CPFR (Collaborative Planning, Forecasting, Replenishment).
  Root cause: information delay and distortion — identical to lag in
  feedback control systems.
```

---

## Decision Cheat Sheet

| Logistics decision | Approach |
|-------------------|----------|
| Where to locate a DC | Center of gravity heuristic; then MILP for exact optimization |
| How many DCs to operate | Model total cost (fixed + transport) vs service time vs risk |
| Choose between modes | Total Landed Cost analysis; not just freight rate |
| Set safety stock levels | z * sigma_LT formula; calibrate z to service level target |
| Determine order quantity | EOQ model; adjust for transportation minimums (full container loads) |
| Plan last-mile delivery routes | VRP with TW; Clarke-Wright or OR-Tools for implementation |
| Decide 3PL vs 1PL | Fixed cost vs variable cost; scale and predictability of volume |
| Assess cold chain compliance | MKT analysis; validate temperature loggers at each handoff |

---

## Common Confusion Points

**Logistics vs supply chain management vs operations**
Logistics = physical movement and storage of goods. Supply chain management = the broader discipline including procurement, demand planning, and supplier relationships. Operations management = the widest umbrella including manufacturing. They are nested, not synonymous.

**Incoterms do not determine payment terms or customs entry**
Incoterms determine who arranges transportation and bears risk. They say nothing about when payment is due or who is the importer of record for customs purposes (though DDP does include customs by convention). A common error: assuming FOB means the buyer handles all US customs entry. It does, but the importer of record designation is separate from Incoterms.

**3PL is not just trucking**
A 3PL may own warehouses, manage labor, provide freight brokerage, handle customs brokerage, operate order management systems, and provide analytics. Reducing 3PL to "trucker" misses the integrated service model.

**JIT is not dead post-COVID**
JIT remains valuable where demand is predictable and supplier reliability is high. Automotive JIT with nearby suppliers (US-Mexico Tier 1) still works. What died was JIT with single-source offshore suppliers across long, unpredictable supply chains. The geography changed, not the principle.

**The bullwhip effect is not about physical goods**
The bullwhip is an information problem. The solution is better information sharing — real-time POS data to suppliers, vendor-managed inventory, shared demand forecasts. The physical goods flows are a consequence of the information flows. Fix the information problem and the inventory oscillation dampens. Same principle as reducing control loop latency in any feedback system.
