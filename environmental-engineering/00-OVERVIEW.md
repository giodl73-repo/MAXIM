# Environmental Engineering — Landscape Overview

## The Big Picture

Environmental engineering applies engineering principles to protect human health and the
natural environment. Five technical domains, one regulatory backbone, one unifying
quantitative tool (mass balance).

```
+------------------------------------------------------------------+
|              ENVIRONMENTAL ENGINEERING DOMAINS                    |
|                                                                  |
|  WATER            WASTEWATER        AIR QUALITY                  |
|  TREATMENT        TREATMENT         CONTROL                      |
|  ---------        ----------        -----------                  |
|  Source water     Primary/          Criteria                     |
|  coag/floc/sed    secondary/        pollutants (NAAQS)           |
|  filtration       tertiary          Dispersion modeling          |
|  Disinfection     Activated sludge  Control tech                 |
|  Membranes (RO)   Nutrient removal  (ESP/SCR/FGD/baghouse)      |
|  PFAS/DBPs        Biogas/CHP        Indoor air quality           |
|  01-WATER-        02-WASTEWATER     03-AIR-QUALITY               |
|  TREATMENT.md     .md               .md                          |
+------------------------------------------------------------------+
|  SOLID/HAZARDOUS  SITE              SUSTAINABILITY                |
|  WASTE MGMT       REMEDIATION                                    |
|  ---------------  -----------       ----------------             |
|  MSW composition  Phase I/II ESA    LCA (ISO 14040)              |
|  Waste hierarchy  Fate/transport    GHG Protocol                 |
|  Landfill design  NAPLs/plumes      Scope 1/2/3                  |
|  Recycling econ   P&T/SVE/ISCO/     Circular economy             |
|  RCRA Subtitle C  bioremediation    ESG / SBTi                   |
|  04-SOLID-        05-REMEDIATION    06-SUSTAINABILITY            |
|  WASTE.md         .md               .md                          |
+------------------------------------------------------------------+
                              |
              +---------------+---------------+
              |  REGULATORY BACKBONE          |
              |  EPA statutes: SDWA / CWA /   |
              |  CAA / RCRA / CERCLA / TSCA   |
              |  + state programs              |
              +-------------------------------+
```

**The quantitative foundation**: mass balance runs through every domain.
What enters a system = what leaves + what accumulates.
Apply it to a treatment plant, a contaminant plume, an LCA inventory, a carbon account.

---

## The Regulatory Backbone

Six federal statutes partition the field. Every practitioner needs to know which statute
governs which medium and what the key mechanism is.

```
+--------+----------------------------+---------------------------+
| Statute| Governs                    | Key Mechanism             |
+--------+----------------------------+---------------------------+
| SDWA   | Drinking water quality     | MCLs — maximum            |
| 1974   | from source to tap         | contaminant levels        |
|        |                            | (enforceable health std)  |
+--------+----------------------------+---------------------------+
| CWA    | Surface water quality,     | NPDES permits for point   |
| 1972   | wetlands, dredge/fill      | source discharges;        |
|        |                            | §404 for wetland fills;   |
|        |                            | TMDLs for impaired waters |
+--------+----------------------------+---------------------------+
| CAA    | Ambient air quality,       | NAAQS (criteria           |
| 1970   | stationary + mobile        | pollutants); NESHAP for   |
|        | source emissions           | HAPs; Title V operating   |
|        |                            | permits; PSD/NSR review   |
+--------+----------------------------+---------------------------+
| RCRA   | Solid and hazardous        | Cradle-to-grave manifest; |
| 1976   | waste at active facilities | generator categories;     |
|        |                            | TSD facility permits;     |
|        |                            | land disposal restrictions|
+--------+----------------------------+---------------------------+
| CERCLA | Contaminated sites         | NPL listing; strict       |
| 1980   | (historical releases)      | joint-and-several         |
|        | "Superfund"                | retroactive liability;    |
|        |                            | ROD cleanup decision      |
+--------+----------------------------+---------------------------+
| TSCA   | Chemical substances in     | Pre-manufacture notice    |
| 1976   | commerce                   | (PMN); PFAS reporting;    |
|        | (manufacture/import/use)   | risk evaluation and risk  |
|        |                            | management rules          |
+--------+----------------------------+---------------------------+
```

### Key Distinctions

**RCRA vs. CERCLA**: RCRA governs active waste management (prospective, compliance-oriented).
CERCLA governs cleanup of historical releases (retrospective, liability-oriented). A site
can be subject to both — a RCRA-permitted facility that had historical releases triggering
CERCLA liability. RCRA compliance does not provide CERCLA immunity.

**SDWA vs. CWA**: SDWA protects drinking water (tap backward to intake). CWA protects
receiving water bodies from discharges. They work in sequence — CWA keeps source water
clean enough that SDWA treatment is feasible and affordable.

**Attainment vs. nonattainment**: If a county is designated nonattainment for PM2.5 or
ozone, new major sources face LAER (lowest achievable emission rate) plus emission offsets.
This directly affects data center siting decisions.

### State Programs

EPA sets federal floors; states often implement and exceed them:

| Program | State Role |
|---------|-----------|
| SDWA primacy | 49/50 states administer their own drinking water programs |
| NPDES | 46 states administer their own discharge permit programs |
| CAA SIPs | States write State Implementation Plans for NAAQS attainment |
| Superfund | State VCPs (voluntary cleanup programs) — faster than federal |
| RCRA auth. | Most states have authorization to run RCRA Subtitle C programs |

---

## Engineering vs. Environmental Science

```
  ENVIRONMENTAL SCIENCE            ENVIRONMENTAL ENGINEERING
  =====================            =========================
  Characterizes problems           Designs systems to solve problems
  Measures concentrations          Sizes equipment, sets parameters
  Models contaminant transport     Designs barriers and treatment trains
  Determines ecological impact     Implements risk reduction to standards
  Peer-reviewed literature         PE-stamped design drawings and specs

  "What is in the water             "What treatment process removes it
   and where does it go?"            to below the MCL at what cost?"
```

Both use the same scientific foundation. Engineering adds:
- Mass balance and reactor kinetics
- Safety factors (regulatory minimums + engineering conservatism, typically 1.5–2×)
- Cost-benefit tradeoffs (capital vs. O&M, present worth analysis)
- Permitting obligations and compliance schedules

---

## The Fundamental Tool: Mass Balance

Every environmental engineering calculation starts here. The mass balance equation is the **continuity equation** — the same conservation PDE that governs heat transfer (energy balance), electromagnetics (charge conservation), and fluid mechanics (Reynolds transport theorem). The form d(M)/dt = flux_in - flux_out + source is universal across physics and engineering; environmental engineering applies it to chemical species concentrations rather than energy or charge.

```
  Accumulation = Inputs - Outputs + Generation - Consumption

  d(M_sys)/dt = Q_in·C_in - Q_out·C_out + r·V

  Steady state (d/dt = 0):
  Q_in·C_in + r·V = Q_out·C_out

  +-----------+----------------------------------------+
  | Domain    | Mass Balance Application               |
  +-----------+----------------------------------------+
  | Water Tx  | Contaminant in raw water minus         |
  |           | removal in each unit process equals    |
  |           | contaminant in finished water          |
  +-----------+----------------------------------------+
  | WWTP      | BOD_in = BOD removed by microbes       |
  |           |         + BOD in effluent              |
  +-----------+----------------------------------------+
  | Air       | SO₂ from stack = SO₂ captured in FGD  |
  |           |                 + SO₂ to atmosphere    |
  +-----------+----------------------------------------+
  | Landfill  | Leachate volume = precip - ET          |
  |           |                  ± Δ moisture storage  |
  +-----------+----------------------------------------+
  | LCA       | Scope 3 = Σ(activity data × EF)       |
  |           | for all upstream/downstream categories |
  +-----------+----------------------------------------+
```

### Reactor Models

The vessel configuration determines the removal equation:

```
  CSTR (completely mixed — ideal):
    C_out = C_in / (1 + k·τ)      k = first-order rate constant
                                   τ = V/Q = hydraulic retention time

  PFR (plug flow — ideal):
    C_out = C_in · exp(-k·τ)

  ENGINEERING BRIDGE — REACTOR MODELS AS SYSTEM ARCHETYPES:
  ─────────────────────────────────────────────────────────────────
  CSTR ≡ memoryless system (M/M/1 queue analog)
    Output depends only on current state, not history.
    Transfer function: H(s) = 1/(1 + τs)  — first-order lag.
    Impulse response: exponential decay e^{-t/τ}.

  PFR ≡ deterministic delay line (pure pipeline)
    Every element spends exactly τ time in the system.
    Transfer function: H(s) = e^{-τs}  — pure time delay.
    Impulse response: delta function at t = τ.

  N CSTRs in series → approaches PFR as N → ∞
    (gamma distribution RTD converges to delta function)
  ─────────────────────────────────────────────────────────────────

  Real reactors: characterized by tracer tests (RTD — residence time
  distribution). Most treatment reactors behave between CSTR and PFR.
  Multiple CSTRs in series approximate PFR behavior.
```

PFR achieves better removal for a given HRT (exponential vs. linear decay).
That is why filtration (near-PFR) follows clarification (near-CSTR) in a
drinking water treatment train.

---

## Risk-Based Standards

Environmental standards are risk-derived, not arbitrary. The derivation framework:

```
  RISK = HAZARD × EXPOSURE

  Hazard characterization:
  ├── Carcinogen: cancer slope factor SF (risk per mg/kg-day)
  └── Non-carcinogen: reference dose RfD (mg/kg-day, no adverse effect)

  Exposure assessment:
  ├── Pathway: ingestion / inhalation / dermal absorption
  ├── Average daily dose ADD = C × IR × EF × ED / (BW × AT)
  │     C  = concentration in medium (mg/L or mg/kg)
  │     IR = intake rate (L/day or kg/day)
  │     EF = exposure frequency (days/year)
  │     ED = exposure duration (years)
  │     BW = body weight (kg), AT = averaging time (days)
  └──

  Risk characterization:
  ├── Cancer risk = ADD × SF          (target: 10⁻⁶ per individual)
  └── Hazard quotient HQ = ADD / RfD  (target: HQ < 1.0)

  MCL derivation: solve for C given target risk level
  MCL = target risk / (SF × IR × EF × ED / (BW × AT))
```

Why contaminants have wildly different standards:
- Arsenic MCL = 10 ppb: moderate carcinogenicity, high chronic ingestion exposure
- Nitrate MCL = 10 mg/L as N: non-carcinogen, infant methemoglobinemia risk
- PFOA MCL = 4 ppt (2024): high potency, bioaccumulative, lifelong exposure pathway

---

## Life Cycle Assessment — The Cross-Cutting Framework

LCA quantifies environmental impacts across the full life of a product, process, or service.
Detailed coverage in 06-SUSTAINABILITY.md; introduced here because it cuts across all domains.

```
  SYSTEM BOUNDARY

  Raw material  →  Manufacturing  →  Use phase  →  End-of-life
  extraction       + distribution     operation      disposal /
  + processing                                       recycling
       |                |                 |               |
       +----------------+-----------------+---------------+
                                 |
                    Life Cycle Inventory (LCI)
                    All inputs: energy, water, materials
                    All outputs: air/water/soil emissions
                                 |
                    Life Cycle Impact Assessment (LCIA)
                    +----------------------------------+
                    | Climate change    (kg CO₂e)     |
                    | Acidification     (kg SO₂e)     |
                    | Eutrophication    (kg PO₄³⁻e)   |
                    | Human toxicity    (kg 1,4-DCBe) |
                    | Water scarcity    (m³ eq.)      |
                    | Land use          (m²·yr)       |
                    +----------------------------------+
```

For a data center operator: LCA of server hardware (silicon mining → e-waste), LCA of
electricity (marginal vs. average grid mix), LCA of water treatment (chemicals, energy,
residuals) — these feed directly into Scope 1/2/3 GHG accounting and Microsoft's
Environmental Sustainability Report.

---

## Professional Credentials

```
  PE (Professional Engineer)
  ├── Licensed by state boards (NCEES exams: FE → PE Environmental)
  ├── Required to stamp/seal design drawings submitted to regulators
  └── Continuing education required for license renewal

  BCEE (Board Certified Environmental Engineer)
  ├── AAEE — highest academic/practice recognition in the field
  ├── Requires PE + practice hours + peer review board examination
  └── Specialty areas: water, wastewater, air, solid/hazardous waste, remediation

  REM (Registered Environmental Manager)
  ├── NREP credential — broader environmental management role
  └── Common in compliance, EHS, and corporate sustainability roles

  CIH (Certified Industrial Hygienist)
  └── Workplace air quality, occupational exposure — overlaps with IAQ
      and indoor air quality engineering
```

---

## Bridge: Microsoft Operations Context

Microsoft's sustainability commitments map directly to environmental engineering deliverables:

```
  COMMITMENT              ENGINEERING TRANSLATION
  ----------              ----------------------
  Carbon Negative         Scope 1/2/3 per GHG Protocol Corporate Std.
  by 2030                 CAA compliance for backup diesel generators
                          LCA of Azure/Surface hardware lifecycle
                          Marginal vs. average grid carbon for Scope 2

  Water Positive          Water balance (withdrawal/consumption) at
  by 2030                 every data center site
                          RO/NF/UF for cooling water treatment
                          Wastewater reclaim and reuse programs
                          Water risk indexing (WRI Aqueduct tool)

  Zero Waste              RCRA compliance — hazardous waste manifests
  by 2030                 E-waste program (Circular Centers decommission)
                          Landfill diversion rates for campuses
                          Packaging LCA and EPR alignment

  Real estate due         Phase I ESA (ASTM E1527-21) before acquisition
  diligence               PFAS risk at sites near airports/fire training
                          CERCLA PRP liability screen

  New construction        CWA §404/401 — wetlands and stormwater permits
  permitting              CAA Title V or minor source for generators
                          PSD review if in attainment area (major source)
                          NEPA review for federal land/permits
```

The Environmental Sustainability Report published annually uses precisely the metrics
this directory covers: GWP100, Scope 1/2/3, water withdrawal/consumption ratios,
zero-waste-to-landfill percentages, and LCA results for Surface hardware.

---

## Domain Interaction Map

The five domains are not siloed — each generates waste streams that enter another domain.

```
  +-------------+      +-------------+      +-------------+
  | WATER       |      | WASTEWATER  |      | AIR         |
  | TREATMENT   |      | TREATMENT   |      | QUALITY     |
  |             |      |             |      |             |
  | Sludge  ----+----> | (or landfill|      | Generator   |
  | (alum/iron  |      |  Subtitle D)|      | permits →   |
  | floc)       |      |             |      | Gaussian    |
  | Brine/      |      | Biogas  ----+----> | dispersion  |
  | concentrate |      | (CH₄/CO₂)  |      | analysis    |
  | from RO --> |      | to CHP or   |      |             |
  | solid waste |      | flare →     |      | Dust from   |
  |             |      | air emiss.  |      | landfill →  |
  +-------------+      +-------------+      | air permit  |
         |                   |              +-------------+
         v                   v
  +-------------+      +-------------+      +-------------+
  | SOLID       |      | SITE        |      | SUSTAIN-    |
  | WASTE       |      | REMEDIATION |      | ABILITY     |
  |             |      |             |      |             |
  | Leachate ---+----> | Pump-and-   |      | LCA counts  |
  | collection  |      | treat efflu-|      | ALL domain  |
  | → WWTP or   |      | ent → WWTP  |      | impacts     |
  | evap pond   |      | or NPDES    |      | across full |
  |             |      |             |      | life cycle  |
  +-------------+      +-------------+      +-------------+
```

---

## Decision Cheat Sheet

| Question | Where to Look |
|----------|--------------|
| What health standard applies to my drinking water contaminant? | SDWA NPDWRs — EPA contaminant tables |
| Does my discharge need a permit? | CWA NPDES — point source to WOTUS triggers permit |
| What air permit does a backup diesel generator need? | CAA: PTE vs. major source threshold; nonattainment status |
| How do I classify my waste as hazardous? | RCRA: listed waste (F/K/P/U) or characteristic (TCLP test) |
| Site has chlorinated solvents — what cleanup standard? | CERCLA RAGS risk-based target or state VCP SSTLs |
| What is my facility's carbon footprint? | GHG Protocol Corporate Standard — Scope 1/2/3 |
| Is this site a Superfund candidate? | CERCLA HRS score ≥28.5 → potential NPL listing |
| What technology removes PFAS from drinking water? | BAT per 2024 MCL rule: GAC or PFAS-specific IX resin |
| How do I evaluate a candidate site for purchase? | Phase I ESA (ASTM E1527-21) — RECs and AAI |
| How do I quantify hardware environmental impacts? | ISO 14040 LCA, ecoinvent database, GWP100 characterization |
| What is "water positive"? | Net positive water balance: return more than withdrawn in stressed areas |

---

## Common Confusion Points

**RCRA vs. CERCLA liability**: RCRA compliance does not immunize from CERCLA liability.
A facility that followed RCRA perfectly can still be a PRP (potentially responsible party)
if historical releases occurred. CERCLA liability is strict, joint-and-several, and
retroactive — it applies to releases that predated the law.

**MCL vs. MCLG**: The MCLG (goal) is non-enforceable and is set at zero for carcinogens
and for pathogens. The MCL is enforceable and is set as close to MCLG as "feasible"
(technology and cost considered). For PFOA: MCLG = 0, MCL = 4 ppt. The gap reflects
analytical and treatment limits.

**Attainment area complexity**: A county can be in attainment for PM2.5 but nonattainment
for ozone — they are tracked by pollutant, not by geography alone. Check BOTH when siting.

**WOTUS jurisdiction**: "Waters of the United States" — the scope of CWA jurisdiction —
has been in constant litigation. Sackett v. EPA (2023) significantly narrowed coverage,
removing many adjacent wetlands. Check the current rule and local hydrology before any
ground disturbance near water features.

**LCA system boundary politics**: Scope 3 Category 11 (use of sold products) and Category 1
(purchased goods and services) typically dominate a tech company's total footprint —
Azure's customer workloads exceed Microsoft's direct emissions. The choice of what to
include in the system boundary is not a neutral technical decision; it determines political
and financial accountability.

**Carbon neutral vs. net-zero**: Carbon neutral allows any mix of reductions and offsets
to reach zero. Net-zero (as defined by SBTi) requires first achieving ~90% absolute
reduction, then using high-quality removals for residual emissions. "Carbon neutral" claims
without deep reduction are increasingly scrutinized by regulators and investors.
