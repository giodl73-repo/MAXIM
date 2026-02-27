# Sustainability Engineering

## The Big Picture

Sustainability engineering provides the quantitative frameworks for measuring and reducing
environmental impact across entire product and organizational systems. Three interlocking
methodologies: LCA (what are the impacts?), GHG Protocol (what is the carbon footprint?),
and circular economy (how do we eliminate waste by design?).

```
  SUSTAINABILITY ENGINEERING FRAMEWORKS

  ┌─────────────────────────────────────────────────────────────────┐
  │  LIFE CYCLE ASSESSMENT (LCA)                                    │
  │  ISO 14040 / 14044                                              │
  │  Goal: quantify ALL environmental impacts across full           │
  │  product/system life — climate, water, toxicity, land use      │
  │  Scale: product/process/service                                 │
  ├─────────────────────────────────────────────────────────────────┤
  │  CARBON FOOTPRINT / GHG ACCOUNTING                             │
  │  GHG Protocol Corporate Standard                               │
  │  Goal: quantify greenhouse gas emissions (CO₂e)                │
  │  Scale: organization, product, project, value chain            │
  │  Subset of LCA focused on climate change impact only           │
  ├─────────────────────────────────────────────────────────────────┤
  │  CIRCULAR ECONOMY                                               │
  │  Ellen MacArthur Foundation model                              │
  │  Goal: eliminate waste and pollution by design; keep           │
  │  materials in use; regenerate natural systems                  │
  │  Scale: business model, product design, industrial symbiosis   │
  └─────────────────────────────────────────────────────────────────┘
            ↓                    ↓                    ↓
  ┌─────────────────────────────────────────────────────────────────┐
  │  REPORTING / DISCLOSURE FRAMEWORKS                             │
  │  GHG Protocol → Scope 1/2/3 reporting                         │
  │  TCFD / ISSB IFRS S2 → climate-related financial disclosure    │
  │  SBTi → science-based emission reduction targets              │
  │  CDP / GRI / SASB → voluntary disclosure aggregators          │
  │  SEC Climate Rule → mandatory US public company disclosure     │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Life Cycle Assessment (LCA)

LCA is the gold standard for environmental impact quantification — structurally identical to **total cost of ownership (TCO) analysis**, substituting environmental impact categories for currency. Define scope (functional unit = unit of service delivered), enumerate all impacts across the lifecycle (inventory = cost model), aggregate to impact scores (characterization = cost rollup), identify hotspots (sensitivity analysis = TCO decomposition). LCA uses kg CO2e and disability-adjusted life years instead of USD, but the analytical structure is the same framework any enterprise leader uses for infrastructure procurement decisions. ISO 14040 (principles) and ISO 14044 (requirements) define the methodology.

### Four Phases of LCA

```
  PHASE 1: GOAL AND SCOPE DEFINITION
  ├── Functional unit (FU): the reference unit for all inputs/outputs
  │   Example: "provision of 1 m³ of drinking water at the customer tap"
  │   Example: "1 year of operation of a 10 MW data center"
  │   Choice of FU determines what gets compared and how
  ├── System boundary: what is included/excluded
  │   Cradle-to-grave: raw materials → disposal
  │   Cradle-to-gate: raw materials → factory gate (common for B2B)
  │   Gate-to-gate: just the manufacturing stage
  │   Cradle-to-cradle: circular, materials re-enter system
  ├── Allocation rules: how to distribute impacts when a process
  │   produces multiple outputs (e.g., refinery → gasoline + diesel + jet fuel)
  │   Methods: mass-based, economic, system expansion (preferred)
  └── Intended audience and decision context

  PHASE 2: LIFE CYCLE INVENTORY (LCI)
  ├── Data collection: all material inputs, energy inputs, water,
  │   and all emissions to air/water/soil for each unit process
  ├── Foreground data: the specific system being studied (measured/modeled)
  ├── Background data: upstream supply chain → use LCI databases
  │   Ecoinvent (ecoinvent.org): 18,000+ datasets; global coverage;
  │   gold standard; licensed (~$3k–10k/yr or via SimaPro/GaBi)
  │   US LCI database (NREL): free; US-specific but smaller
  │   GaBi: LCI database + software (Thinkstep/Sphera)
  └── Uncertainty: parameter uncertainty vs. model uncertainty vs.
      scenario uncertainty

  PHASE 3: LIFE CYCLE IMPACT ASSESSMENT (LCIA)
  ├── Characterization: multiply LCI results by characterization factors
  │   to convert emissions to impact scores (e.g., CH₄ × 29.8 = kg CO₂e)
  ├── Normalization: divide by reference system (optional but context-giving)
  └── Weighting: assign relative importance to impact categories (subjective)

  PHASE 4: INTERPRETATION
  ├── Identify hotspots: which processes/flows dominate which impact?
  ├── Sensitivity analysis: how do results change with key assumptions?
  ├── Uncertainty analysis: Monte Carlo or analytical propagation
  └── Conclusions and recommendations
```

### Impact Categories and Methods

```
  LCIA IMPACT CATEGORIES (major)

  ┌────────────────────────┬─────────────────────┬────────────────────┐
  │ Impact Category        │ Unit                │ Key Characterization│
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Climate change (GWP)   │ kg CO₂ equivalent  │ IPCC AR6 GWP100    │
  │ (global warming)       │                     │ CH₄ = 29.8, N₂O = │
  │                        │                     │ 273, SF₆ = 23,500  │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Acidification          │ kg SO₂ equivalent  │ SO₂, NOₓ, HCl,    │
  │                        │                     │ HF, NH₃ → acid dep │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Eutrophication         │ kg N eq. or         │ N and P emissions  │
  │ (freshwater / marine)  │ kg P eq.            │ to water and air   │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Human toxicity         │ kg 1,4-DCB eq.      │ Cancer and non-    │
  │ (cancer/non-cancer)    │                     │ cancer toxicity    │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Ozone depletion        │ kg CFC-11 eq.       │ Halogenated cpds.  │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Water scarcity         │ m³ water eq.        │ Availability-      │
  │                        │ (AWARE method)      │ weighted; relevant │
  │                        │                     │ for water positive │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Land use               │ m²·yr               │ Transformation and │
  │                        │                     │ occupation         │
  ├────────────────────────┼─────────────────────┼────────────────────┤
  │ Resource depletion     │ kg Sb eq. (abiotic) │ Mineral and fossil │
  └────────────────────────┴─────────────────────┴────────────────────┘

  LCIA METHODS (implement the characterization factors):
  ├── ReCiPe 2016: most complete European method; midpoint + endpoint
  ├── CML-IA: older but widely cited; midpoint only
  ├── TRACI 2.1: US EPA method; North America–specific characterization
  └── EF (Environmental Footprint): EU regulatory preferred method

  Attributional vs. Consequential LCA:
  ├── Attributional: describes environmental burden allocated to
  │   functional unit under average market conditions (status quo)
  │   → use for product/process comparison, labeling, reporting
  └── Consequential: models changes in environmental flows resulting
      from a decision under marginal conditions
      → use for policy analysis, investment decisions
      Example: attributional electricity LCA uses average grid mix;
      consequential uses marginal (what generator turns on at margin)
```

---

## Carbon Footprint: GHG Protocol

The GHG Protocol Corporate Standard is the dominant framework for organizational
carbon accounting. Developed by WRI + WBCSD; used by >90% of Fortune 500.

### The Three Scopes

```
  GHG PROTOCOL SCOPE FRAMEWORK

  SCOPE 1: Direct emissions — owned or controlled sources
  ├── Stationary combustion: natural gas boilers, emergency generators
  ├── Mobile combustion: company vehicle fleet
  ├── Process emissions: on-site chemical reactions
  └── Fugitive: refrigerant leaks (HFCs), SF₆ from switchgear

  SCOPE 2: Indirect from purchased energy
  ├── Purchased electricity (the dominant Scope 2 for most facilities)
  ├── Purchased steam, heat, or cooling
  └── TWO METHODS (important distinction):
      Location-based: uses average emission factor for regional grid
        Example: ISO-NE grid average → ~0.23 kg CO₂e/kWh (2023)
      Market-based: uses contractual instruments
        Renewable Energy Certificates (RECs): 0 kg CO₂e/kWh if matched
        Power Purchase Agreements (PPAs): use generator emission factor
        Residual mix factors: for unmatched purchases
      Microsoft reports both but targets market-based Scope 2 = 0
      (100% renewable matching via PPAs and RECs)

  SCOPE 3: Value chain indirect emissions (15 categories)
  Typically 70–95% of total corporate footprint
```

### Scope 3 Categories

```
  SCOPE 3 CATEGORIES (GHG Protocol Corporate Value Chain Standard)

  UPSTREAM (supplier-side):
  ┌────┬──────────────────────────────────────────────────────────┐
  │ 1  │ Purchased goods and services                            │
  │    │ Raw materials, components, outsourced services          │
  │    │ Largest category for most manufacturers                 │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 2  │ Capital goods                                           │
  │    │ Servers, building construction, equipment               │
  │    │ Embodied carbon in purchased capital                    │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 3  │ Fuel- and energy-related activities                     │
  │    │ Upstream emissions from extraction/processing of        │
  │    │ purchased fuel and energy (not Scope 1 or 2)           │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 4  │ Upstream transportation and distribution                │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 5  │ Waste generated in operations                          │
  │    │ Disposal/treatment of operational waste                 │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 6  │ Business travel                                         │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 7  │ Employee commuting                                      │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 8  │ Upstream leased assets                                  │
  └────┴──────────────────────────────────────────────────────────┘

  DOWNSTREAM (customer-side):
  ┌────┬──────────────────────────────────────────────────────────┐
  │ 9  │ Downstream transportation and distribution              │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 10 │ Processing of sold products                             │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 11 │ Use of sold products                                    │
  │    │ Electricity consumed by products during use phase       │
  │    │ Typically the #1 or #2 category for electronics/software│
  │    │ For Microsoft: Azure customers' workloads run on Azure  │
  │    │ hardware → Category 11 dwarfs Microsoft's direct emiss. │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 12 │ End-of-life treatment of sold products                  │
  │    │ E-waste, product disposal                               │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 13 │ Downstream leased assets                                │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 14 │ Franchises                                              │
  ├────┼──────────────────────────────────────────────────────────┤
  │ 15 │ Investments                                             │
  └────┴──────────────────────────────────────────────────────────┘
```

### Science-Based Targets (SBTi)

```
  SCIENCE-BASED TARGETS INITIATIVE (SBTi)

  Purpose: Align corporate emission reduction targets with climate
  science (1.5°C or well-below 2°C Paris Agreement pathways)

  Requirements for validation:
  ├── Near-term target (5–10 years): 4.2% absolute Scope 1+2 reduction/yr
  │   (1.5°C pathway) OR sector-specific rate
  ├── Long-term target (to 2050): net-zero — achieve 90–95% reduction;
  │   remaining 5–10% via carbon removals (not offsets)
  ├── Scope 3 required if >40% of total footprint is Scope 3
  └── Annual progress tracking and public disclosure

  SBTi Net-Zero Standard (2021):
  ├── Net-zero ≠ carbon neutral: net-zero requires DEEP decarbonization first
  ├── Offset purchases do NOT count toward SBTi net-zero pathway
  └── Only permanent carbon removals (DAC, BECCS, enhanced weathering)
      count for the residual 5–10% after deep reductions

  Microsoft SBTi alignment:
  ├── Carbon negative by 2030 (remove more than emitted)
  ├── Remove historical cumulative emissions by 2050
  └── Investment in carbon removal portfolio (DAC, soil carbon, forests)
```

---

## Circular Economy

The circular economy reframes waste as a design failure, not an inevitable output.

```
  ELLEN MACARTHUR FOUNDATION CIRCULAR ECONOMY MODEL

  TWO CYCLES:

  TECHNICAL CYCLE (inorganic/synthetic materials):
  Product use → maintenance → reuse → refurbishment
             → remanufacturing → recycling
  Goal: keep materials at highest utility level as long as possible

  BIOLOGICAL CYCLE (organic/natural materials):
  Consumption → food/beverage → compost/biogas
  → cascades → regeneration of natural systems

  R-STRATEGIES (most to least preferred):
  ┌────────────────────────────────────────────────────────────────┐
  │ R0: Refuse — eliminate product/material entirely              │
  │ R1: Rethink — servicize; optimize product use intensity       │
  │ R2: Reduce — less material/energy per unit function           │
  │ R3: Reuse — same function, different user                     │
  │ R4: Repair — extend product life by maintenance               │
  │ R5: Refurbish — restore product performance                   │
  │ R6: Remanufacture — rebuild to original specs                 │
  │ R7: Repurpose — different function, different user            │
  │ R8: Recycle — material recovery (loses product value)         │
  │ R9: Recover — energy from waste (lowest CE value)             │
  └────────────────────────────────────────────────────────────────┘

  Microsoft Circular Centers:
  ├── On-campus facilities that disassemble, test, refurbish servers
  ├── Servers refurbished → resold (R5/R6) rather than e-waste
  ├── Components (memory, SSDs, CPUs) sold into secondary market
  └── Measures: reuse rate, zero-waste-to-landfill from datacenters
```

### Industrial Ecology

```
  INDUSTRIAL ECOLOGY: the metabolism metaphor applied to industry

  KALUNDBORG INDUSTRIAL SYMBIOSIS (Denmark — the archetype):
  ┌────────────────────────────────────────────────────────────────┐
  │ Asnæs Power Plant → steam → Novo Nordisk (pharma)            │
  │                   → cooling water → fishery                   │
  │                   → fly ash → cement manufacturer             │
  │                   → gypsum → wallboard manufacturer           │
  │                   → district heating → Kalundborg city        │
  │ Statoil refinery  → fuel gas → power plant (vs. flaring)     │
  │ Novo Nordisk      → sludge → agriculture (fertilizer)        │
  └────────────────────────────────────────────────────────────────┘
  Result: ~30% energy savings, significant waste diversion,
  economic benefits to all participants — emergent, not designed.

  MATERIAL FLOW ANALYSIS (MFA):
  ├── Quantifies flows and stocks of materials through a system
  │   (economy, region, industry sector)
  ├── Input: extraction, imports / Output: exports, emissions, waste
  ├── Tools: STAN software (TU Wien); ODYM (Industrial Ecology Lab)
  └── Used for: identifying recycling opportunities, critical materials,
      policy analysis (Extended Producer Responsibility design)

  SUBSTANCE FLOW ANALYSIS (SFA):
  └── Single substance tracked through entire socioeconomic system
      Example: lead flows (mining → batteries → recycling → soil/water)
```

---

## Environmental Management Systems

```
  ISO 14001 (Environmental Management System)

  PLAN-DO-CHECK-ACT framework for systematic environmental improvement:

  PLAN:
  ├── Environmental policy (top management commitment)
  ├── Aspects and impacts assessment (identify significant impacts)
  ├── Legal compliance obligations
  └── Objectives, targets, and programs

  DO:
  ├── Operational controls (procedures, training, emergency prep)
  └── Document control

  CHECK:
  ├── Monitoring and measurement
  ├── Legal compliance evaluation
  ├── Internal audit
  └── Nonconformity and corrective action

  ACT:
  ├── Management review
  └── Continual improvement

  Certification: accredited third-party auditor; 3-year cycle
  (initial certification + two surveillance audits)
  ISO 14001 vs. EMAS: EMAS (EU Eco-Management and Audit Scheme) is
  more stringent (public environmental statement required, verified
  data, regulatory compliance mandatory)
```

---

## ESG Reporting Frameworks

Corporate environmental disclosure has proliferated into a complex landscape.
Understanding which framework is mandatory vs. voluntary and who the audience is.

```
  ESG REPORTING LANDSCAPE (2025)

  ┌──────────────────────┬────────────────────────────────────────────┐
  │ Framework            │ Audience / Status                          │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ GHG Protocol         │ Foundation layer — used by all others;    │
  │ (WRI/WBCSD)          │ not a reporting framework per se;         │
  │                      │ defines Scope 1/2/3 methodology           │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ CDP (Carbon          │ Investor/customer-facing; annual           │
  │ Disclosure Project)  │ questionnaire; A–D scoring; voluntary     │
  │                      │ but increasingly requested by supply chain │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ GRI (Global          │ Broad stakeholder-facing; voluntary;      │
  │ Reporting Initiative)│ comprehensive ESG topics beyond climate   │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ SASB (Sustainability │ Investor-focused; industry-specific       │
  │ Accounting Standards)│ metrics; now part of ISSB                 │
  │ Board                │                                            │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ TCFD (Task Force on  │ Investors; scenario analysis (physical +  │
  │ Climate-related      │ transition risk); 4 pillars:              │
  │ Financial Disclosures│ governance / strategy / risk mgmt /       │
  │                      │ metrics & targets; voluntary but becoming │
  │                      │ mandatory in many jurisdictions           │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ ISSB IFRS S2         │ IOSCO-endorsed global baseline for        │
  │ (2023)               │ climate disclosure; absorbs TCFD;         │
  │                      │ mandatory in many countries by 2026       │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ SEC Climate Rule     │ US public companies; mandatory (when      │
  │ (2024, stayed)       │ effective); Scope 1+2 required; Scope 3   │
  │                      │ if material or in SBTi target;            │
  │                      │ currently stayed pending court review     │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ EU CSRD              │ EU large companies; mandatory; ESRS       │
  │ (Corporate Sustain.  │ (European Sustainability Reporting Stds); │
  │ Reporting Directive) │ double materiality; very broad; audited   │
  └──────────────────────┴────────────────────────────────────────────┘
```

### TCFD / ISSB Physical and Transition Risk

```
  CLIMATE RISK FRAMEWORK

  PHYSICAL RISKS (climate change impacts on physical assets):
  ├── Acute: extreme weather events (hurricane, flood, wildfire)
  │   → data center flooding, power outages, supply chain disruption
  └── Chronic: gradual shifts (sea level, temperature increase)
      → cooling efficiency loss, water stress, permafrost thaw

  TRANSITION RISKS (policy and market response to climate change):
  ├── Policy/regulatory: carbon pricing, emission regulations
  │   → cost of backup generator permits, carbon taxes on Scope 1
  ├── Technology: energy efficiency improvements, stranded assets
  ├── Market: customer preferences, commodity price changes
  └── Reputational: ESG ratings, investor pressure

  SCENARIO ANALYSIS (required under TCFD/ISSB):
  ├── Physical risk: RCP 4.5 (intermediate) vs. RCP 8.5 (high emissions)
  │   using IPCC regional projections
  └── Transition risk: IEA Net Zero 2050 (orderly) vs. Delayed transition
      (disorderly) vs. Current Policies (hot house world)

  For Microsoft: cooling water availability under climate scenarios is a
  material physical risk; carbon pricing scenarios affect generator
  economics and data center siting cost models
```

---

## Green Building and Infrastructure Rating Systems

```
  RATING SYSTEM COMPARISON

  LEED (Leadership in Energy and Environmental Design):
  ├── Buildings: LEED BD+C (new construction), LEED O+M (existing)
  ├── Data centers: LEED certification covers envelope, HVAC, water,
  │   materials, indoor environment, innovation
  ├── Rating: Certified / Silver / Gold / Platinum (points-based)
  └── PUE (Power Usage Effectiveness) improvement scores points

  ENVISION (Infrastructure):
  ├── For roads, bridges, water infrastructure, pipelines, energy systems
  ├── 64 credits across 5 categories: Quality of Life, Leadership,
  │   Resource Allocation, Natural World, Climate + Resilience
  ├── Verification levels: Bronze / Silver / Gold / Platinum
  └── Increasingly required for public infrastructure projects

  PUE (Power Usage Effectiveness) — data center efficiency metric:
  PUE = Total facility energy / IT equipment energy
    Industry average: 1.5–1.6
    Best-in-class hyperscale: 1.1–1.15
    Microsoft target: <1.2 for new facilities
    Carbon footprint implication: PUE = 1.5 means 50% of energy
    goes to overhead (cooling, power conversion, lighting) — reducing
    PUE directly reduces Scope 2 emissions per unit compute

  WUE (Water Usage Effectiveness):
  WUE = Site water usage (L) / IT equipment energy (kWh)
    Industry average: 1.8 L/kWh
    Microsoft target: 0 L/kWh in water-stressed regions by 2024
    Strategy: adiabatic cooling (no evaporative water use)
    vs. evaporative cooling (high WUE but lower energy)
```

---

## Net-Zero vs. Carbon Neutral

```
  THE VOCABULARY MATTERS — these are not synonymous

  CARBON NEUTRAL:
  ├── Net zero CO₂e at organizational boundary
  ├── Achieved by: any combination of emission reductions AND offsets
  ├── Offset purchases can bridge the gap to "zero"
  ├── Criticism: allows purchasing cheap offsets without deep reduction
  └── Standard: PAS 2060 (BSI), ISO 14068 (2023)

  NET-ZERO (SBTi Corporate Net-Zero Standard):
  ├── Requires: 90–95% absolute emission reduction from base year (all scopes)
  ├── Residual 5–10%: only permanent, high-quality carbon removals
  │   (no avoided emissions, no REDD+ forest protection offsets)
  ├── Timeframe: typically by 2050
  └── Near-term targets also required (2030)

  CARBON NEGATIVE (Microsoft's pledge):
  ├── Remove MORE carbon than emitted annually (net negative)
  ├── More aggressive than SBTi net-zero
  └── Requires significant carbon removal portfolio investment

  CARBON REMOVAL METHODS:
  ┌────────────────────────┬────────────────────────────────────────┐
  │ Method                 │ Permanence / Scale                     │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Afforestation/         │ Low permanence (fire, disease risk);  │
  │ reforestation          │ large scale; low cost                  │
  ├────────────────────────┼────────────────────────────────────────┤
  │ BECCS (bioenergy +     │ Moderate permanence (geological);     │
  │ CCS)                   │ scaling challenges                    │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Direct Air Capture     │ Very high permanence (geological);    │
  │ + storage (DAC)        │ current cost $300–1000/MT CO₂;       │
  │                        │ Microsoft is major buyer (Climeworks,  │
  │                        │ CarbonCapture, Heirloom)              │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Enhanced weathering    │ High permanence; scaling challenge;   │
  │                        │ land use intensive                    │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Biochar                │ Moderate permanence (100+ yrs);       │
  │                        │ scalable; co-benefits for soil        │
  └────────────────────────┴────────────────────────────────────────┘
```

---

## Microsoft Sustainability Metrics Mapping

```
  MICROSOFT ENVIRONMENTAL SUSTAINABILITY REPORT — METRIC ORIGINS

  ┌──────────────────────────────┬────────────────────────────────────┐
  │ Reported Metric              │ Methodology / Standard             │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Scope 1 direct emissions     │ GHG Protocol — combustion EFs,    │
  │                              │ EPA AP-42, IPCC GWP100            │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Scope 2 (market-based)       │ RECs + PPAs → supplier EFs;       │
  │                              │ residual mix for remainder         │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Scope 3 value chain          │ GHG Protocol Corporate Value Chain │
  │                              │ Standard; spend-based methods for  │
  │                              │ Cat. 1; supplier-specific for      │
  │                              │ hardware manufacturing (Cat. 1/2)  │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Water withdrawal /           │ AWWA metrics; WRI Aqueduct for     │
  │ consumption by basin         │ water stress context               │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Waste diversion rate         │ Mass-based (kg diverted / total    │
  │                              │ waste generated); "zero waste"     │
  │                              │ = >90% diversion rate             │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Surface LCA results          │ ISO 14040/14044; ecoinvent DB;    │
  │ (carbon footprint of         │ TRACI or ReCiPe characterization; │
  │ Surface hardware)            │ cradle-to-grave FU = 1 device/    │
  │                              │ per year of use                   │
  ├──────────────────────────────┼────────────────────────────────────┤
  │ Carbon removal portfolio     │ SBTi removal accounting; verified │
  │                              │ by Gold Standard, Verra/VCS,      │
  │                              │ or direct contracts (DAC)         │
  └──────────────────────────────┴────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Need to compare environmental impacts of two cooling systems | LCA (ISO 14040/14044); include energy, water, refrigerant GWP, materials across full life |
| Reporting Scope 2 with renewable energy claims | Use market-based method with RECs or PPAs; location-based method for secondary disclosure |
| How much of our footprint is Scope 3? | Calculate all 15 categories; Cat. 1 (purchased goods) and Cat. 11 (use of products) dominate for tech companies |
| SBTi validation — what does it require? | 90%+ absolute reduction; all Scopes; near-term (2030) + long-term (2050) targets submitted |
| What framework should we use for climate risk disclosure? | ISSB IFRS S2 (global standard going forward); TCFD if not in mandatory jurisdiction yet |
| Is buying offsets enough for net-zero claim? | No — SBTi net-zero requires deep reduction first; offsets ≠ reductions |
| How do I measure circular economy performance? | Material flow analysis; reuse rate (% by mass); circularity rate (Ellen MacArthur CI) |
| What's the best LCI database for tech hardware? | Ecoinvent + industry-specific data (iNemi reports, PAIA data for electronics) |
| Carbon neutral vs. net-zero — which claim is defensible? | Net-zero (SBTi) is more rigorous; "carbon neutral" has no mandatory reduction requirement and is increasingly challenged |

---

## Common Confusion Points

**Location-based vs. market-based Scope 2**: A company can report both. Location-based
uses grid averages (useful for grid impact analysis). Market-based uses contractual
instruments (RECs, PPAs) — this is the number that matters for net-zero claims. A
Microsoft data center in a coal-heavy grid might have high location-based Scope 2 and
near-zero market-based Scope 2 if PPAs cover 100% of consumption. Both are true;
they answer different questions.

**RECs are not the same as renewable energy**: Buying a REC means someone somewhere
generated 1 MWh of renewable electricity and you claim the environmental attribute.
The electrons going into your data center are grid electrons (mix of all sources).
Additionality concerns: if the renewable plant would have been built anyway, buying its
RECs claims credit for an impact you didn't cause. This is why PPAs (bundled, often with
new capacity) are considered more credible than unbundled RECs.

**LCA functional unit drives everything**: Two LCAs of "data center energy" can produce
completely different results if one uses per kWh and one uses per unit of compute delivered.
A more energy-efficient facility might have higher per-facility impact but lower per-compute
impact. Always interrogate the functional unit before comparing LCA results.

**Scope 3 Category 11 vs. Category 1 for Microsoft**: Azure is a platform business.
Customers run their workloads on Microsoft hardware → Category 11 (use of sold services/
products) captures the electricity those workloads consume. Microsoft's own facility
operations are Scope 1+2. The vastly larger number is the customer footprint, which
Microsoft influences but does not control — hence the importance of Azure efficiency (PUE)
as a lever for reducing the Category 11 impact per unit of customer compute.

**Double materiality**: EU CSRD requires reporting on both (a) how climate affects the
company (financial materiality — risk/opportunity) AND (b) how the company affects
the environment (impact materiality). This is different from US/ISSB single materiality
(financial only). Companies subject to CSRD must assess both directions of impact.
