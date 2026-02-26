# Infrastructure Governance: Ownership, Regulation, Funding, and Policy

## The Big Picture

Infrastructure governance determines who builds it, who owns it, who pays for it, who
regulates it, and who is accountable when it fails. These are not peripheral administrative
questions -- they directly determine the condition of infrastructure. The US has ~$20T
in public infrastructure, owned across federal/state/local governments, regulated private
utilities, and purely private entities. Each ownership model has different investment
incentives, accountability structures, and failure modes.

```
INFRASTRUCTURE GOVERNANCE LANDSCAPE
=======================================

               OWNERSHIP MODEL
               ================
     PUBLIC          REGULATED          PRIVATE         QUASI-PUBLIC
   (government)      PRIVATE (IOU)      (unregulated)   (P3/PPP)
        |                  |                 |               |
   City water system   Electric utility  Freight rail    Toll road concession
   State highway       Natural gas IOU   Private ports   Airport terminal
   Municipal transit   Telecom carrier   Data centers    Stadium (public land)
   Federal dam         Cable company     Pipelines       Social infrastructure
        |                  |                 |               |
  Funded by taxes    Funded by rates    Funded by fees  Funded by user fees
  Accountable to     Accountable to     Accountable to   Accountable to
  voters/councils    PUC (rate-setting) market/contract  contract (40-99 yr)

   WHO DECIDES PRICE?
        |                  |                 |               |
   Political process   Rate case at PUC   Market price    Concession agreement
   (rates often        (return on rate     (no price       (fixed CPI escalation
    below cost)         base + O&M)         control)        + triggers)

   INVESTMENT INCENTIVE:
        |                  |                 |               |
   Subject to           Rate base grows  ROI maximized    ROI constrained
   budget cycle,        → more capex is  → underinvest    by contract;
   political pressure;  rewarded by       in non-revenue-  scope determines
   maintenance deferred  formula           generating assets performance risk

ACCOUNTABILITY GAPS:
  Public: accountability diffuse (voters; no direct consequence for deferred maintenance)
  Regulated IOU: PUC oversight strong on rates; less on operational outcomes
  Private: market accountability only; no duty to serve if unprofitable
  P3: complex contracts; public may lose flexibility; private gains if demand exceeds forecast
```

---

## Ownership Models

### Public Infrastructure

```
PUBLIC INFRASTRUCTURE OWNERSHIP
==================================

FEDERAL INFRASTRUCTURE (direct federal ownership):
  Examples: Hoover Dam (Bureau of Reclamation), Bonneville Power Administration (BPA),
            Tennessee Valley Authority (TVA), US Postal Service, Amtrak (mostly)
            FAA air traffic control, interstate highway system (FHWA/state partnership)
  Model: federal agency owns, operates, funds from appropriations or dedicated revenues
  Political economy: federal budget allocation; line items in appropriations bills
  Congressional authorization required for major investments
  Strength: national planning possible; cross-subsidy across regions
  Weakness: political cycle funding vs. long infrastructure life cycles
  TVA example: regional power authority created 1933 (New Deal); serves 10M people;
    operates coal + nuclear + hydro fleet; rates set by TVA board (not FERC/PUC)
    ~$13B revenue; ~$24B long-term debt; major capital investment without appropriations

STATE AND LOCAL OWNERSHIP (dominant for most infrastructure):
  Examples: state DOTs (highways), municipal water/wastewater, city transit, local airports
  Financing: general obligation bonds (backed by taxing power), revenue bonds,
             federal grants (FHWA, FTA, EPA SRF), state aid formulas
  Governance: City councils, water boards, transit boards, state legislatures
  Accountability mechanism: electoral (voters); media; oversight bodies; bond rating agencies
  Investment incentive problem: elected officials rewarded for ribbon cuttings, not maintenance
    ASCE infrastructure report card C- average: reflects chronic underinvestment in O&M
  Municipal fiscal stress: cities with declining population / tax base
    Detroit, Flint, Puerto Rico: fiscal distress -> infrastructure neglect -> crisis

SPECIAL DISTRICTS: ubiquitous US infrastructure governance form
  ~38,000 special districts in US (most are infrastructure-related)
  Single-purpose: water district, fire district, irrigation district, port authority, transit authority
  Governed by: elected or appointed board (varies by state law)
  Revenue: user fees (water/sewer rates) + debt
  Advantages: insulated from general fund competition; focused mandate; can cross city limits
  Disadvantages: less democratic oversight; governance often opaque to the public
  Examples: New York MTA, Metropolitan Water District of Southern California, BART
```

### Regulated Private Utilities (IOUs)

```
INVESTOR-OWNED UTILITIES (IOUs): RATE-OF-RETURN REGULATION
============================================================

MODEL: Private company owns and operates infrastructure; regulated monopoly
  Granted franchise area: exclusive right to serve; customer can't switch
  In exchange: must serve all customers; rates regulated by Public Utility Commission
  Federal: FERC regulates interstate transmission (electric, gas, hydro)
  State: PUC/PSC regulates distribution and retail rates

RATE CASE PROCESS:
  1. Utility files rate case: proposes new revenue requirement
  2. Revenue requirement = O&M + D&A + taxes + Return on Rate Base
     Return on Rate Base = Rate Base × Authorized ROE
     Rate Base: net book value of utility plant in service
  3. Interveners: industrial customers, consumer advocates, state AG
  4. Hearings: discovery, testimony, cross-examination
  5. PUC issues order: authorized rates (typically 10-18 months process)

RATE BASE CALCULATION:
  Rate Base = Gross Plant in Service
            - Accumulated Depreciation
            - Customer Advances and Contributions
            + Working Capital Allowance

  Return on Rate Base: typically 6-10% overall (weighted avg cost of capital + allowed equity)
  Example: $10B rate base × 8% return = $800M/yr return component of revenue requirement
  Authorized ROE: typically 9-11% for electric utilities; FERC-set for transmission

CAPEX INCENTIVE STRUCTURE (the rate base incentive):
  Capex → grows rate base → more return ($ profitable)
  O&M → expense → passed through at cost (no markup)
  Implication: IOUs have financial incentive to capitalize rather than expense
    → "gold plating" risk: over-investment in capital (regulated)
    → under-investment in O&M (no return earned)
  Regulators respond: disallowances (disallow imprudent capex); O&M performance metrics
  Recent evolution: performance-based regulation (PBR)
    Link allowed returns to performance outcomes (reliability, decarbonization, customer sat)
    Hawaii, California leading on PBR; traditional PUCs slow to adopt

IOU UNIVERSE (major US utilities):
  Electric: NextEra ($100B+ assets), Duke, Southern Company, Dominion, Exelon, etc.
            ~3,300 electric utilities; 190+ IOUs serve 69% of US customers
  Gas: Southern Company Gas, Sempra, Atmos, NiSource
  Water: American Water Works, Essential Utilities, SJW Group (small relative to water munis)
  Telecom: AT&T, Verizon (partially regulated for some services; largely deregulated post-1996)
```

### Public-Private Partnerships (P3)

```
PUBLIC-PRIVATE PARTNERSHIPS (P3 / PPP)
=========================================

DEFINITION: Long-term contractual arrangement where private party
  designs, builds, finances, and/or operates infrastructure
  Government retains ownership (typically) but transfers operational risk/reward

P3 SPECTRUM (risk transfer continuum):
  DBB (Design-Bid-Build):      Public risk; public financing; separate contracts
  DB  (Design-Build):          Construction risk to contractor; public financing
  DBF (Design-Build-Finance):  Construction + financing risk to private
  DBFO (Design-Build-Finance-Operate): Adds 20-40 yr operations + maintenance
  DBFOM (+ Maintain):          Full lifecycle responsibility to private partner
  Concession (BOT/BOOT):       Private finances, builds, operates, revenue for 30-99 yr
  Privatization:               Full ownership transfer (UK 1980s water/rail)

KEY RISK ALLOCATION (P3 value proposition):
  Risk Type         Traditional (DBB)   P3 (DBFOM/Concession)
  Construction cost Government          Private
  Schedule/delay    Government          Private
  O&M performance   Government          Private
  Demand risk       Government          Depends (availability vs. concession)
  Force majeure     Government          Split (contract-specific)
  Technology risk   Government          Private (for design period)
  Long-term maint.  Government          Private (whole-life)

  Availability payment model: Government pays for facility being available (not usage)
    → private bears no demand risk but bears performance risk
    → common for social infrastructure (hospitals, schools, courthouses)
  Revenue concession: private receives user fees (tolls, rates)
    → private bears demand risk + performance risk
    → toll roads, airports, bridges

EXAMPLES:
  Chicago Skyway (2005): 99-year concession for $1.83B (Macquarie/Cintra)
    City needed cash; private got long-term toll revenue stream
    Later: Macquarie sold stake at significant profit; criticism that Chicago sold at low price

  Denver Eagle P3 (2010): DBFOM for 36-mile commuter rail expansion; $2.2B
    Concessionaire (Denver Transit Partners): build + 29-yr operations
    FasTracks: public authority retains oversight, sets fares

  LaGuardia Airport Terminal B (2016): DBFOM; LaGuardia Gateway Partners; $4B
    Port Authority of NY/NJ owns land + concession; private builds/operates terminal
    30-year agreement; complex revenue-sharing with Port Authority

  Indiana Toll Road (2006): 75-year concession; $3.85B
    Macquarie/Ferrovial; later bankruptcy 2014 (traffic lower than projected)
    State got cash upfront; private took demand risk → in this case, over-paid

P3 TRADE-OFFS:
  Advantage:
    Off-balance-sheet financing (often political motivation, not efficiency)
    Whole-life cost management: private party responsible for O&M → incentive to build well
    Construction risk transfer: fixed-price contract with performance bonds
    Operational innovation: private company may manage more efficiently
    Speed: can sometimes move faster than public procurement

  Disadvantage:
    Cost of private capital > municipal bonds (private cost of capital: 8-12%; muni: 3-5%)
    Long contract lock-in: 30-99 year agreements lose flexibility
    Renegotiation risk: when concessionaires go bankrupt or underperform, public bears rescue cost
    Reduced transparency: private operator may not be subject to FOIA
    Profit extraction: returns flow to pension funds, sovereign wealth funds, private equity
    Windfall profits: if traffic/demand exceeds forecast, concessionaire wins; public can't recapture

WHEN P3 WORKS BEST:
  Predictable revenue stream (existing toll road, not greenfield)
  Long-horizon O&M savings from whole-life design (complex buildings, tunnels)
  Construction cost certainty needed and risk transfer worth premium
  Government capacity constrained (can't manage large capital project in-house)
WHEN P3 WORKS POORLY:
  Greenfield demand risk (new transit line without ridership history)
  Political desire to monetize for short-term cash (often undervalued)
  Complex renegotiation-prone assets (technology risk, major city infrastructure)
```

---

## Regulatory Frameworks

```
US INFRASTRUCTURE REGULATORY FRAMEWORK
=========================================

SECTOR         FEDERAL REGULATOR    STATE REGULATOR       FOCUS
-------------  -------------------  -------------------   ----------------
Electricity    FERC (transmission)  PUC/PSC (retail)      Rates, reliability,
                NERC (standards)     State AG/ISO           transmission access
Natural gas    FERC (interstate)    PUC (intrastate)      Rates, safety, pipelines
               PHMSA (safety)
Water/Sewer    EPA (standards)      PUC (rates, some)     Drinking water quality,
               none for rates       State health dept      wastewater discharge
Telecom        FCC (spectrum, ISP)  PUC (limited)         Common carrier, access,
                                                           spectrum
Rail           FRA (safety)         None (freight)         Safety, grade crossings
               STB (rates/access)   PUC (intercity)       Rate access disputes
Aviation       FAA (safety, ATC)    None (federal)         Safety, ATC, airports
Pipelines      PHMSA (safety)       State PSC (some)       Integrity, incident
               FERC (rates,gas)                            response, rates
Roads          FHWA (federal-aid)   State DOT             Design standards, funding
               (no rate regulation)
Ports          Maritime Admin       Port authorities       Commerce, security
               (MARAD)              (quasi-public)

KEY REGULATORY BODIES DETAIL:
  FERC (Federal Energy Regulatory Commission):
    Regulates: wholesale electricity markets, electric transmission, interstate natural gas,
               hydroelectric licensing, LNG terminals
    Rate authority: cost-of-service for transmission; market-based for wholesale generation
    NERC oversight: FERC approves NERC reliability standards; FERC enforces CIP compliance
    Cannot regulate: state utility distribution rates, retail rates

  PHMSA (Pipeline and Hazardous Materials Safety Administration):
    Regulates: pipeline safety (natural gas, hazardous liquids)
    Inspection and enforcement: ~500,000 km of regulated pipelines
    Incident investigation: post-incident investigation authority
    Does not regulate: pipeline rates (FERC for interstate; states for intrastate)

  EPA:
    Sets: drinking water standards (NPDWR - National Primary Drinking Water Regulations)
         Maximum Contaminant Levels (MCLs): binding; trigger-based
    Enforces: Clean Water Act (NPDES permits for wastewater discharge)
    Does not regulate: water utility rates; ownership; capital plans

  FCC:
    Regulates: spectrum allocation, broadcast licenses, some telecom services
    Net neutrality: contested regulatory authority over ISPs
    Post-2015/2017 flip-flop: net neutrality status uncertain; awaiting court/Congress
    Emergency communications: GETS (Government Emergency Telecommunications Service)

REGULATORY GAP: RESILIENCE
  NERC TPL-001: N-1 reliability (required for bulk electric)
  But: no mandatory long-duration blackout resilience standard
  FERC Order 881: ambient-adjusted line ratings (improves operational efficiency, not resilience)
  Gap: regulated utilities required to be operationally reliable, not resilient to extreme events
  Post-Texas Uri (2021): FERC/NERC required winterization for bulk electric (Order 881, NERC RRO-001)
    Still limited: distribution (last-mile to customer) not covered by bulk power rules
```

---

## Funding Mechanisms

```
INFRASTRUCTURE FUNDING SOURCES
================================

FEDERAL SOURCES:
  Appropriations: annual discretionary spending
    FHWA: ~$50B/yr for highways (from Highway Trust Fund + general fund)
    FTA: ~$15B/yr transit capital
    EPA SRF (State Revolving Fund): $3-5B/yr (water and wastewater loans)
    USACE: $8B/yr (flood control, navigation, water management)
    Corps projects: authorized by WRDA (Water Resources Development Act, biennial)

  IIJA (Infrastructure Investment and Jobs Act, 2021): $1.2T total, $550B new money
    Highways: $110B
    Rail (Amtrak + freight): $66B
    Bridges: $40B (specific bridge program)
    Public transit: $39B
    Water/wastewater: $55B (largest water infrastructure investment in history)
    Broadband: $65B
    Ports/waterways: $17B
    Electric vehicle infrastructure: $7.5B
    Power grid/clean energy: $73B
    Resilience: $50B (FEMA BRIC and other resilience programs)
    Timeline: 5-year authorization; significant spending through ~2026-2028

  IRA (Inflation Reduction Act, 2022): energy/climate
    $369B total energy/climate investment
    EV credits, clean energy tax credits, hydrogen production tax credit
    Direct Pay: allows non-tax-paying entities (munis) to receive credits as cash
      → first time government-owned utilities can access investment tax credits

STATE AND LOCAL SOURCES:
  General obligation (GO) bonds: backed by full faith and credit (taxing power)
    No dedicated revenue; repaid from general taxes
    Requires voter approval in most states
    Lowest interest rate (AAA muni: 3-4%)
    Used for: schools, general public buildings, general infrastructure

  Revenue bonds: backed by revenues from the project
    No voter approval in most states
    Slightly higher rate than GO
    Used for: water/wastewater rates, toll roads, transit fare revenue, airport fees

  Special assessment bonds: charge properties that benefit
    Used for: local road improvements, sewer extensions in new development

  Build America Bonds (BAB): taxable munis with federal subsidy (2009-2010 stimulus)
    No longer available but precedent for direct subsidy model

  Tax Increment Financing (TIF):
    Designate TIF district: capture future property tax growth to fund infrastructure
    Mechanism: assess value at baseline; all increment goes to TIF fund (not general fund)
    Used for: transit-oriented development, urban redevelopment, brownfield sites
    Chicago: most aggressive TIF user; $2B+ in TIF funds at any time
    Criticism: diverts incremental tax from schools and general services

  ASSET RECYCLING: monetize underutilized public assets; reinvest in infrastructure
    Australia model: lease of ports, electrical networks; proceeds to new infrastructure fund
    US: limited use (Chicago Skyway, Indiana Toll Road); often criticized as asset sale
    Canada's Investing in Canada Plan: federal asset recycling program (mixed results)

DEBT SUSTAINABILITY:
  Municipal debt rating: Moody's/S&P/Fitch; investment grade (BBB-/Baa3 and above)
  Debt coverage ratio: net revenues / debt service (>1.25x typical covenant)
  Rate covenant: usually requires utility to set rates sufficient to cover debt service
  Puerto Rico 2016: PROMESA oversight board; $72B debt default
    Water/power infrastructure: PREPA (power), PRASA (water) both restructured
    Infrastructure neglect + debt = compounding crisis (Maria amplified existing fragility)
```

---

## International Governance Models

```
COMPARATIVE INFRASTRUCTURE GOVERNANCE
=========================================

EU MODEL:
  Ownership: varies by member state (France: state-owned utilities; UK/Germany: privatized)
  Regulation: EC sets rules; national regulators implement
  Energy: ACER (Agency for Cooperation of Energy Regulators) coordinates national regs
    TSO/DSO unbundling: transmission system operators must be independent of generation
    Internal Energy Market: cross-border trade, third-party access rules
  Water: EU Water Framework Directive: river basin management; good ecological status by 2027
  Transport: TEN-T (Trans-European Transport Network): EU-funded corridor investment
  Digital: NIS2 Directive (2022): mandatory cybersecurity for critical infrastructure operators
    Extends to more entities than NIS1; incident reporting; supply chain security
  Resilience: CER Directive (2022 Critical Entities Resilience Directive): physical resilience
    Replaces 2008 ECI Directive; requires member state risk assessments; entity obligations

UK MODEL (post-privatization, post-Brexit):
  Privatization: Thatcher era 1984-1991: BT, British Gas, British Airways, water, electricity
  Regulators: Ofgem (energy), Ofwat (water), Ofcom (telecom), ORR (rail), CAA (aviation)
    Price review: typically 5-year control periods; AMP (Asset Management Plan for water)
    Ofwat AMP7 (2020-2025): £51B investment program; real price cuts required + investment
    Ofgem RIIO (Revenue = Incentives + Innovation + Outputs): performance-based regulation
  Post-privatization water quality: mixed; Thames Water (2024): private equity ownership,
    £14B debt, underinvestment, sewage spills, near-bankruptcy → regulatory intervention
    Case study: aggressive leverage + private ownership → infrastructure neglect
  Thames Water crisis: PE owners (Kemble Infrastructure) extracted value; deferred maintenance;
    2024: Ofwat took special measures; potential renationalization discussed
    Water regulator: has power to impose special administration (temporary renationalization)

AUSTRALIA MODEL:
  Privatization and regulation: similar to UK; state-level regulation
  Asset recycling: Infrastructure Australia framework
    Leasing of state-owned ports, electricity networks; proceeds to Restart NSW fund
    NSW: $20B+ proceeds from TransGrid, Port of Newcastle, Port Botany
  National Infrastructure Plan: 15-year roadmap; priority project list
  Critical Infrastructure Act 2018 (updated 2021):
    Mandates: critical infrastructure asset register (CIRMP - Risk Management Programs)
    Applies to 11 sectors; government has last-resort intervention powers
    "Positive security obligation": operators must have risk management programs
    Much more prescriptive than US CISA guidance (voluntary) or AWIA (risk assessment only)

LESSONS FROM INTERNATIONAL COMPARISON:
  UK water privatization: demonstrated that private ownership without adequate regulation
    → leveraged extraction → infrastructure neglect → water quality decline
  France EDF: state-owned nuclear fleet; high capital intensity managed through centralized ownership;
    heavy state support during financial stress (2022: €3B recap)
  Germany: municipal ownership (Stadtwerke) of local utilities; generally high quality
    but capital-intensive green transition stress testing model
  Australia critical infrastructure law: more aggressive mandatory obligation model than US
    US critical infrastructure protection: largely voluntary outside NERC CIP electric
```

---

## Infrastructure Investment Gap

```
INVESTMENT GAP ANALYSIS
=========================

ASCE INFRASTRUCTURE REPORT CARD (2021): GPA = C-
  Roads:        D      Bridges:        C      Dams:          D+
  Wastewater:   D+     Drinking Water: C-     Energy:        C-
  Transit:      D-     Rail:           B      Ports:         B-
  Aviation:     D+     Inland Waterways: D+   Hazardous Waste: D+
  Levees:       D      Schools:        D
  Broadband:    D

INVESTMENT NEED VS. CURRENT INVESTMENT (ASCE 2021):
  Identified need: $5.9T over 10 years ($590B/year)
  Current investment: $2.6T over 10 years ($260B/year)
  Gap: $3.3T over 10 years ($330B/year)
  IIJA filled: ~$550B new federal over 5 years → significant but not gap-closing

GDP IMPACT OF INACTION:
  ASCE estimate: infrastructure investment gap costs each American household $3,300/yr
    (reduced wages, higher prices, transportation costs, business losses)
  GDP impact: $10T over 20 years if gap not addressed (ASCE economic model)
  These are contested estimates; directionally right even if not precisely accurate

WHY THE GAP PERSISTS:
  Short political horizons: 2-4 year election cycles vs. 50-100 year asset lives
  Visible spending vs. maintenance: new project ribbon-cutting vs. pipe replacement
  Diffuse ownership: no single actor accountable for national infrastructure condition
  User charge avoidance: water rates, gas taxes below cost-recovery (political constraint)
    Federal gas tax: 18.4 cents/gallon since 1993 (not indexed to inflation)
    Real purchasing power: ~50% erosion since 1993; Highway Trust Fund chronically short
  Pension overhang: many state/local government budgets stressed by pension obligations
    → crowd out capital investment for infrastructure maintenance
  Regulatory permitting: long project lead times (NEPA review, utility relocation, permits)
    → slows deployment of available funding (IIJA funds: slow to deploy for this reason)

CLOSING THE GAP: MECHANISMS THAT WORK
  Value capture: infrastructure investment creates land value → capture it to fund infra
    TIF, special benefit districts, developer exactions, air rights
    Hong Kong MTR model: real estate development rights + transit funding = self-financing system
    Denver RTD: TIF + FasTracks sales tax + federal grants → largest US transit expansion
  Asset recycling (Australia): realized value of underutilized assets → new investment
  Performance-based regulation: link allowed returns to outcomes → incentivizes investment
  Infrastructure bank: long-duration, patient capital for infrastructure at low cost
    US National Infrastructure Bank (proposed multiple times; not enacted)
    EIB (European Investment Bank): EU infrastructure bank; €80B+ lending/year
    Canada: CDPQ Infra; Ontario Infrastructure; various provincial models
```

---

## Decision Cheat Sheet

| Governance question | Answer |
|---------------------|--------|
| What is an IOU and how are its rates set? | Investor-owned utility; rates set by PUC rate case; revenue requirement = O&M + depreciation + taxes + return on rate base |
| Why do IOUs prefer capex over O&M? | Capex grows rate base → earns authorized return; O&M passed through at cost with no markup |
| What is an availability payment P3? | Private builds/operates; government pays for facility being available; private bears performance not demand risk |
| FERC vs. PUC jurisdiction | FERC: wholesale electricity + interstate transmission; PUC: retail rates + distribution |
| What does PHMSA regulate? | Pipeline safety (natural gas + hazardous liquids); ~500,000 km of regulated pipelines |
| What did IIJA 2021 provide for water? | $55B over 5 years — largest water infrastructure investment in US history |
| Why does the infrastructure investment gap persist? | Short political horizons vs. long asset lives; visible new vs. invisible maintenance; gas tax not inflation-indexed |
| Australia vs. US critical infrastructure mandate | Australia: mandatory positive security obligation (risk management programs required); US: largely voluntary except NERC CIP for electric |
| What went wrong with Thames Water? | Private equity leverage + extraction + deferred maintenance → debt + infrastructure neglect; Ofwat special measures 2024 |

---

## Common Confusion Points

**"Public infrastructure is accountable and efficient; private is profitable but neglects
the public interest."** The reality is more complex in both directions. Public agencies
defer maintenance when budgets are cut (Flint water, MTA signal system); private regulated
utilities can over-invest in capital when return structures incentivize it. The institutional
design -- incentive structure, accountability mechanisms, regulatory oversight -- matters
more than the public/private label alone.

**"P3 partnerships transfer risk to the private sector."** They transfer some risks that
the private sector can price and manage (construction, certain O&M outcomes). Demand risk
is often under-estimated in P3 contracts (Indiana Toll Road, Dulles Greenway). Political
risk is not transferable. Force majeure is split. When a P3 fails, the public often rescues
it anyway -- the risk transfer is real but incomplete. The value proposition depends entirely
on which risks are transferred and whether the private party is better positioned to manage them.

**"Rate-of-return regulation is outdated."** It still governs the majority of US utility
investment. Performance-based regulation (PBR) is an improvement in theory but difficult
to implement -- what metrics capture utility value? How do you prevent gaming? FERC and
state PUCs are experimenting. The rate-of-return floor remains for capital recovery; PBR
is being layered on top for performance adjustment. The base model won't disappear.

**"The IIJA infrastructure bill solved the investment gap."** It is the largest infrastructure
investment in US history, but $550B over 5 years = $110B/year of new federal spending.
ASCE's estimated gap is $330B/year. The bill addressed roughly one-third of the gap for
5 years. It did not address the underlying structural issues: gas tax erosion, political
short-termism, pension crowding-out, or local maintenance funding. A significant gap remains.
