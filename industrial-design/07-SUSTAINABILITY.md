# Sustainable Design and Circular Economy

## The Big Picture

Sustainability in industrial design is not primarily about materials — it is a systems-level
challenge. The dominant model (linear: extract -> make -> use -> discard) is being replaced,
in theory if not yet in practice, by circular models. The design stage determines 80% of a
product's environmental impact, so design is where sustainability either happens or doesn't.

```
+----------------------------------------------------------------------+
|              SUSTAINABILITY: THE SYSTEM LEVELS                       |
+----------------------------------------------------------------------+
|                                                                      |
|  LEVEL 1: PRODUCT EFFICIENCY                                         |
|  Better materials, less waste per unit, energy-efficient manufacture |
|  "The same thing, cleaner." Net effect: often marginal improvement   |
|                                                                      |
|  LEVEL 2: PRODUCT DESIGN FOR END-OF-LIFE                            |
|  Design for disassembly, recyclable materials, repairability         |
|  "The thing can be taken apart and materials recovered."             |
|                                                                      |
|  LEVEL 3: PRODUCT SYSTEM REDESIGN                                    |
|  Servitization (sell use, not ownership), sharing, modular extension |
|  "Sell light, not bulbs." (Philips), "sell mobility, not cars."      |
|                                                                      |
|  LEVEL 4: SOCIOTECHNICAL TRANSITION                                  |
|  New consumption patterns, infrastructure, regulations               |
|  "Redesign the entire system around different assumptions."          |
|                                                                      |
|  Most "green product" design operates at Level 1.                    |
|  Circular economy advocates for Level 2-3.                           |
|  True sustainability requires Level 4.                               |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## Planned Obsolescence: History and Forms

**Definition:** Designing products to fail, go out of fashion, or become technically superseded
within a planned timeframe, generating replacement purchases.

**Origin:** The term was coined by Bernard London in a 1932 pamphlet "Ending the Depression
Through Planned Obsolescence" — he literally proposed government-mandated product expiration
dates as a Keynesian stimulus. The idea was ignored but the practice emerged anyway through
market incentives.

**Alfred Sloan and GM (1920s-30s):** The annual model change (Sloanism) was a deliberate
strategy to make previous-year cars seem outdated — aesthetic obsolescence, not functional.
Ford's Model T philosophy (one model, long production run, cheapest possible) was defeated not
because it failed functionally but because Sloan made it unfashionable.

**Forms of planned obsolescence:**

| Type | Mechanism | Example |
|------|-----------|---------|
| Technical obsolescence | Incompatible upgrades, no backward compatibility | iPhone Lightning -> USB-C; Windows XP end-of-support |
| Material obsolescence | Designed to wear out | Nylon stockings (early versions were deliberately weakened after the war) |
| Aesthetic obsolescence | Fashion cycles, "outdated" appearance | Annual model refreshes in fashion, cars |
| Systemic obsolescence | The ecosystem changes around a working product | 32-bit app support dropped in macOS 10.15 |
| Psychological obsolescence | Marketing creates dissatisfaction with working products | "New and improved" formulations |

**Phoebus Cartel (1924-1939):** The first documented industrial cartel for planned technical
obsolescence. GE, Philips, Osram, and others agreed to limit incandescent bulb life to 1,000
hours (from ~2,500 hours) to maintain replacement demand. The cartel set a "quality committee"
that fined members whose bulbs lasted too long. This is documented in internal memos.

**Software planned obsolescence:** Modern software companies have perfected this without a
formal cartel. Feature freeze on old OS versions, APIs that are deprecated on aggressive
timescales, subscription models that make perpetual licenses unavailable. Adobe's shift from
Creative Suite (perpetual) to Creative Cloud (subscription) is planned obsolescence via
business model rather than hardware.

---

## Right-to-Repair Movement

**The problem:** Modern devices are designed to resist user repair:
- Proprietary screws (pentalobe in iPhones)
- Glued-in batteries (most modern laptops and phones)
- Pairing requirements (iPhone screen replacement requires Apple authentication; "Error 53")
- Software locks that disable replaced components
- Monopoly on repair manuals and diagnostic tools (John Deere equipment)

**Legal background:**
- **Digital Millennium Copyright Act (DMCA):** Initially used to argue that accessing repair
  software on farm equipment violated copyright. John Deere claimed farmers couldn't repair
  their own tractors because the software was licensed, not owned.
- **Massachusetts Right to Repair Law (2012):** First major right-to-repair legislation in
  the US, covering automotive. Required auto manufacturers to make diagnostic information
  available to independent repair shops.
- **EU Ecodesign Regulation (2021):** Required smartphones and large appliances to have spare
  parts available for 7-10 years after last sale; repair information must be provided.
- **FTC Report on Right to Repair (2021):** Found "scant evidence" that independent repair
  poses quality or safety risks; recommended limiting manufacturer repair monopolies.

**iFixit model:** The company that publishes repair manuals for electronics and sells repair
tools. Their repairability scores (0-10) are the closest thing to an industry-wide metric for
design repairability. Their teardowns are engineering documents.

**Design for repairability principles:**
- Accessible fasteners (standard Torx, Phillips, not proprietary)
- Modular components with defined replacement interfaces
- Component marking (which battery is which voltage, which board is which function)
- Public availability of repair documentation
- Spare parts availability with defined support period

---

## Circular Economy Principles

**Linear vs circular model:**
```
LINEAR ECONOMY:
  Raw materials -> Production -> Use -> Waste (disposal/landfill)
  "Take, Make, Dispose"

CIRCULAR ECONOMY:
  Raw materials
       |
       v
  Production <---- Remanufacture/Refurbish
       |                    ^
       v                    |
  First use           Collect/Sort
       |                    ^
       v                    |
  Second use --> Repair/Upgrade
       |
       v
  Component recovery --> Next production cycle
       |
       v
  Material recovery --> Material feedstock
```

**The Ellen MacArthur Foundation model:** The standard industry framework for circular economy.
Distinguishes:
- **Biological cycle:** Food, natural fibres — materials designed to re-enter biosphere safely
- **Technical cycle:** Electronics, metals, plastics — materials designed to be recovered and
  reused in technical systems (NOT to enter biosphere)

**The levels of circularity (from most to least value-preserving):**

| Level | Value preserved | Example |
|-------|----------------|---------|
| Maintain/Extend life | Highest | Software updates, firmware patches |
| Reuse | High | Second-hand market, device donation |
| Repair | High | Fix broken components |
| Refurbish | Medium-high | Restore to near-new condition |
| Remanufacture | Medium | Disassemble, replace worn parts, rebuild |
| Recycle | Low | Material recovery, loses product structure |
| Recover energy | Lowest | Incinerate for energy — worst circular option |

**Design implications:** Design for circularity means maximizing the level at which products
can be recovered — which means design for disassembly, modularity, and standardization.

---

## Lifecycle Assessment (LCA)

**What it is:** A quantitative method for assessing the environmental impact of a product
across its entire life from raw material extraction through manufacture, use, and end-of-life.

**The four phases of LCA (ISO 14040/14044):**

```
PHASE 1: GOAL AND SCOPE DEFINITION
  What are we assessing? Functional unit definition.
  Example: "1 kg of paper towels" vs "per hand-drying use"
  System boundary: cradle-to-gate, cradle-to-grave, cradle-to-cradle

PHASE 2: LIFE CYCLE INVENTORY (LCI)
  Data collection: mass/energy flows at each stage
  Inputs: raw materials, energy, water
  Outputs: products, wastes, emissions

PHASE 3: LIFE CYCLE IMPACT ASSESSMENT (LCIA)
  Categorize and characterize impacts:
  - Climate change (kg CO2-eq)
  - Acidification (kg SO2-eq)
  - Eutrophication
  - Resource depletion
  - Toxicity (human and ecotoxicity)

PHASE 4: INTERPRETATION
  Identify hotspots, compare alternatives, sensitivity analysis
```

**LCA findings that counterintuitive designers:**
- A cotton tote bag must be used 131+ times to break even on climate vs a single-use plastic bag
  (because cotton is water/land/pesticide intensive in production)
- Electric vehicles: manufacturing carbon footprint is higher than ICE; payback period depends
  entirely on electricity source grid mix
- Stainless steel water bottle requires ~100 uses to break even vs plastic PET bottle

**Design for LCA:** LCA should be done in early design stages when decisions still matter —
80% of environmental impact is locked in at design stage. Material selection (aluminum vs steel vs
composite vs bio-based) is the highest-leverage decision.

---

## Sustainable Materials

**Categories and tradeoffs:**

| Material category | Examples | Advantage | Disadvantage |
|------------------|---------|-----------|-------------|
| Bio-based | PLA, bamboo, cork, hemp composites | Renewable source | May not biodegrade in practice; land use |
| Recycled content | Recycled aluminum, rPET, recycled steel | Avoids primary extraction | Quality loss over cycles; contamination |
| Recyclable at end-of-life | HDPE, aluminum, glass | Theoretically recoverable | Infrastructure-dependent; rarely achieved |
| Biodegradable | PHA, natural fibres | Compostable | Only in industrial composting conditions |
| Durability-maximizing | High-grade stainless, titanium, ceramics | Long life = low lifetime impact | High upfront energy; not recyclable with same infrastructure |

**The aluminum paradox:** Aluminum production requires enormous energy (the "solid electricity"
concept — smelting converts electrical energy to metal). Primary aluminum: ~170 GJ/tonne.
But recycled aluminum: ~10 GJ/tonne. So aluminum is simultaneously one of the highest-impact
primary materials and one of the lowest-impact recycled materials. Design decision: maximize
recycled content and recyclability at end-of-life.

**Plastic recyclability reality:**
```
Plastic type   Recycled globally   Notes
PET (#1)       ~30%                Bottles, some textiles
HDPE (#2)      ~10%                Containers
PVC (#3)       <1%                 Rarely recycled; contaminates other streams
LDPE (#4)      <5%                 Film plastic
PP (#5)        ~1%                 Improving
PS (#6)        <1%                 Styrofoam almost never recycled
Other (#7)     <1%                 Multimaterial; not recyclable
```
The "chasing arrows" recycle symbol indicates the resin type, NOT that it will be recycled.
Most plastic labeled recyclable is not recycled in practice due to economics and contamination.

---

## Design Frameworks

**Cradle to Cradle (C2C):** William McDonough and Michael Braungart (2002). Not just "less bad"
but "good" design — products designed so that all materials can safely return to either the
biological or technical cycle with no downcycling. Certification system (now Cradle to Cradle
Products Innovation Institute).

**Biomimicry:** Janine Benyus. Design inspired by biological solutions to analogous functional
challenges. Spider silk as composite inspiration; lotus effect as surface hydrophobicity model;
termite mound ventilation as passive climate control model. The argument: evolution has had
3.8 billion years of R&D; these solutions are field-tested.

**Doughnut Economics (Kate Raworth, 2017):** Design goal: meet social minimums without exceeding
ecological ceilings. Products designed within the "safe and just space for humanity." Industrial
design as a constraint satisfaction problem between the social floor (enough for human wellbeing)
and the ecological ceiling (planetary boundaries).

---

## Decision Cheat Sheet

| Design choice | Sustainability implication | Recommendation |
|---------------|--------------------------|----------------|
| Material selection | Highest single-factor impact | Prioritize recycled content; design for end-of-life recyclability |
| Fastener type | Determines repairability | Standard screws > proprietary > glue |
| Battery design | Key repairability point | Replaceable > user-accessible glued |
| Modular vs monolithic | Update and repair cycle | Modular if technology changes fast |
| Product lifespan target | Inversely related to total impact | Longer lifespan with update capability |
| Documentation | Required for repair economy | Publish repair manuals |
| Spare parts | Sustains repair market | Commit to X years availability |

---

## Common Confusion Points

**"Recyclable = recycled":** No. A material can be technically recyclable but economically
or infrastructurally not actually recycled. The rate at which recyclable materials actually
complete the recycling loop is far lower than commonly assumed. Design for recyclability only
matters if the collection and processing infrastructure exists.

**"Bio-based = biodegradable = sustainable":** Not automatically. Bio-based means the raw
material is from biological (renewable) sources, not from petroleum. Biodegradable means it
breaks down biologically. Bio-based plastic (PLA) does not biodegrade in typical conditions
(it requires industrial composting at specific temperatures). And "biodegradable" in the ocean
can still contribute to microplastic pollution.

**"Circular economy is about recycling":** Recycling is the lowest-value circularity strategy.
The higher-value options (reuse, repair, remanufacture) are more circular because they preserve
more of the embedded energy and labor. A true circular economy minimizes recycling in favor of
keeping products and components in use longer.

**"Sustainability is a cost penalty":** Often true at product unit scale, but lifecycle costs
(total cost of ownership including replacement) frequently favor durable, repairable products.
The business model determines whether the cost falls on the buyer (durable product is better)
or the manufacturer (disposable product with replacement revenue is better). Regulatory pressure
(EU Ecodesign) is shifting this equation.
