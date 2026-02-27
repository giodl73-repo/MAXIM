# Site Remediation

## The Big Picture

Site remediation is the engineering response to contamination that has already occurred.
The regulatory structure determines who pays and what the cleanup standard is.
The technical challenge is getting contaminants out of complex subsurface geology
at reasonable cost.

```
  REMEDIATION PROGRAM PATHWAYS

  ┌─────────────────────────────────────────────────────────────────┐
  │                  SITE DISCOVERY                                 │
  └─────────────────────────────┬───────────────────────────────────┘
                                 │
            ┌────────────────────┴─────────────────────┐
            │                                           │
            v                                           v
  ┌──────────────────────┐              ┌──────────────────────────┐
  │  CERCLA (SUPERFUND)  │              │  RCRA CORRECTIVE ACTION  │
  │  Federal program     │              │  (or State Superfund)    │
  │  Historical releases │              │  Operating/closed RCRA   │
  │  Any property        │              │  permitted facilities     │
  │  NPL listed sites    │              │  Compliance-oriented      │
  │  Strict/joint/sev.   │              │  State VCP: voluntary,   │
  │  retroactive liab.   │              │  faster, more flexible    │
  └─────────┬────────────┘              └──────────────────────────┘
            │
   ┌────────+───────────────────────────────┐
   │  CERCLA PROCESS STAGES                 │
   │                                        │
   │  Preliminary Assessment (PA)           │
   │         |                              │
   │  Site Inspection (SI)                  │
   │         |                              │
   │  Hazard Ranking System (HRS) score     │
   │         |                              │
   │  If HRS ≥ 28.5 → NPL listing          │
   │         |                              │
   │  Remedial Investigation (RI)           │
   │  (full site characterization)          │
   │         |                              │
   │  Feasibility Study (FS)                │
   │  (evaluate alternatives)              │
   │         |                              │
   │  Record of Decision (ROD)             │
   │  (selected remedy)                    │
   │         |                              │
   │  Remedial Design (RD)                  │
   │         |                              │
   │  Remedial Action (RA)                  │
   │         |                              │
   │  Operations + Maintenance (O&M)        │
   │  Long-term monitoring                  │
   └────────────────────────────────────────┘
```

---

## CERCLA Liability

The liability structure is critical to understand — it determines why Superfund cleanup
is contentious and expensive.

```
  CERCLA LIABILITY CHARACTERISTICS

  STRICT: No proof of negligence required. Released a hazardous substance
          → you are liable. Period.

  JOINT AND SEVERAL: Any single PRP can be held responsible for the
                     entire cleanup cost. EPA pursues the party with
                     the deepest pockets, who then recovers contribution
                     from other PRPs.

  RETROACTIVE: Applies to releases that occurred before CERCLA was
               enacted (1980). PRPs from 1955 industrial operations
               can be liable today.

  PRP CATEGORIES:
  ├── Current owner/operator of the facility
  ├── Owner/operator at the time of disposal
  ├── Arranger (person who arranged for disposal — e.g., generator who
  │   hired the hauler)
  └── Transporter (who selected the disposal site)

  INNOCENT LANDOWNER DEFENSE:
  Requires: Phase I ESA performed before purchase (AAI standard —
  All Appropriate Inquiries, ASTM E1527-21), no prior knowledge of
  contamination, did not cause release.
  This is why Phase I ESA is standard in ALL commercial real estate
  acquisitions, including Microsoft data center sites.
```

---

## Site Characterization

Before any remediation, you must know what is there, where it is, and how it moves.

```
  PHASE I ESA (ASTM E1527-21)
  ├── Records review:
  │   Historical maps, aerial photos, city directories, EDR report
  │   (Environmental Data Resources — searches federal/state databases),
  │   ASTM historical use research
  ├── Site reconnaissance: visual inspection, current + adjacent
  │   property uses, observable RECs (recognized environmental conditions)
  ├── Interviews: current/past owners, occupants, local officials
  └── Output: Phase I report with RECs (de minimis, controlled, historic)
               No sampling — desk and observation work only
               Provides innocent landowner defense under CERCLA

  PHASE II ESA (limited investigation)
  ├── Triggered by RECs from Phase I
  ├── Soil borings: disturbed soil sampling by hollow-stem auger,
  │   direct push (Geoprobe), or rotary drill
  ├── Groundwater monitoring wells: direct push or drilled and cased;
  │   groundwater sample after development
  ├── Laboratory analysis: VOCs (SW-846 Method 8260), SVOCs (8270),
  │   metals (6010/6020), PFAS (537.1 or 533), TPH
  └── Output: Phase II report with analytical results vs. screening criteria
               May recommend Phase III (full characterization) if positive results

  PHASE III (Remedial Investigation — RI)
  ├── Full 3D delineation of contamination extent
  ├── Dense sampling grid; contour maps of contamination
  ├── Fate and transport modeling
  └── Baseline risk assessment (HHRA + ERA)
```

---

## Contaminant Fate and Transport

Understanding subsurface contaminant behavior is the foundation of remediation design.

### NAPLs (Non-Aqueous Phase Liquids)

```
  NAPL BEHAVIOR IN THE SUBSURFACE

  LNAPL (Light NAPL — floats on water table):
  ├── Petroleum products: gasoline, diesel, fuel oil, crude oil
  ├── Residual saturation in vadose zone as it migrates
  ├── Pools at water table surface → "free product"
  ├── Dissolved phase plume downgradient
  ├── Vapor phase upward in vadose zone
  └── Recovery: free product skimming pump; bioremediation for dissolved

  DNAPL (Dense NAPL — sinks below water table):
  ├── Chlorinated solvents: TCE (trichloroethylene), PCE (tetrachloroethylene),
  │   TCA (trichloroethane), carbon tetrachloride, methylene chloride
  │   Also: coal tar, creosote, some pesticides
  ├── DNAPL sinks through saturated zone along preferential pathways
  │   (fractures, sandy lenses) — follows density-driven flow, not
  │   hydraulic gradient
  ├── Leaves residual blobs/ganglia in pore spaces → long-term
  │   source of dissolved phase contamination (source zone)
  ├── DNAPL source zones may be 30+ meters deep in fractured rock
  └── THE HARDEST CONTAMINATION PROBLEM — decades of cleanup, billions $
```

### Groundwater Transport Equations

The advection-dispersion equation is the **parabolic PDE** from heat/mass transfer — Fick's second law (∂C/∂t = D∇²C) with an advection term (−v·∂C/∂x) and a first-order reaction term (−λC). The three terms decompose as: Fickian diffusion (spreading), advection (bulk transport), and reactive decay. This is the same equation governing heat conduction with convective transport — D_L plays the role of thermal diffusivity, v_x the convective velocity, and λ the heat loss coefficient. Solutions follow from the same Green's function methods: point source in uniform flow yields a Gaussian plume advected downstream.

```
  ADVECTION-DISPERSION EQUATION (1D):

  ∂C/∂t = D_L(∂²C/∂x²) - v_x(∂C/∂x) - λC

    C   = contaminant concentration (mg/L)
    D_L = longitudinal dispersion coefficient (m²/s)
    v_x = advective pore velocity = K·i/n_e (m/s)
    λ   = first-order degradation rate constant (s⁻¹)

  DARCY'S LAW:
    q = -K·(∂h/∂l)     q = specific discharge (m/s)
    v = q/n_e           v = pore velocity (accounts for porosity)
    K = hydraulic conductivity (m/s):
        sand 10⁻³–10⁻⁵; silt 10⁻⁵–10⁻⁷; clay <10⁻⁸; fractured rock: variable

  RETARDATION (sorption slows transport):
    R = 1 + (ρ_b · K_d) / n_e
    K_d = K_oc × f_oc   (organic carbon partition coefficient × fraction OC)
    Example: benzene in aquifer with 0.1% OC:
    K_oc ≈ 83 L/kg; K_d = 83 × 0.001 = 0.083 L/kg
    If ρ_b = 1.8 kg/L, n_e = 0.3: R = 1 + (1.8 × 0.083)/0.3 = 1.5
    → benzene moves at 1/R = 67% of groundwater velocity

  REDUCTIVE DECHLORINATION (natural attenuation of chlorinated solvents):
    PCE → TCE → DCE → vinyl chloride → ethene
    Requires: anaerobic conditions (DO <0.5 mg/L), organic carbon,
    Dehalococcoides (DHC) microorganism present
    Vinyl chloride step is rate-limiting and most toxic intermediate
    → evidence of complete dechlorination (ethene) required for MNA
```

---

## Risk Assessment

Risk assessment drives cleanup standards. Not all contamination requires cleanup —
the question is whether the contamination poses an unacceptable risk given actual
exposure pathways. This is **probabilistic safety analysis** — the same framework used in aerospace (FMEA), nuclear (PRA), and safety-critical software. Each exposure pathway (soil ingestion, groundwater ingestion, vapor intrusion) is an independent risk contributor, analogous to a fault tree branch. Total risk is the sum across all pathways, compared to an acceptable threshold (10^-6 excess cancer risk). The structure maps directly to event tree analysis: probability of exposure x severity of effect = risk estimate.

```
  RISK ASSESSMENT FRAMEWORK (EPA RAGS)

  Step 1: Hazard Identification
    Which contaminants are present? Which are the "chemicals of concern" (COCs)?

  Step 2: Dose-Response Assessment
    Carcinogens: cancer slope factor (CSF or SF, per mg/kg-day)
    Non-carcinogens: reference dose (RfD, mg/kg-day)
    Sources: EPA IRIS (Integrated Risk Information System)

  Step 3: Exposure Assessment
    Conceptual site model (CSM): who is exposed, how, for how long?
    ├── Soil ingestion (on-site worker, child)
    ├── Groundwater ingestion (drinking water pathway)
    ├── Vapor intrusion (VOCs from soil → indoor air)
    ├── Inhalation of contaminated dust
    └── Dermal contact with soil/water

    ADD = C × CR × EF × ED / (BW × AT)
    (average daily dose — same framework as drinking water standards)

  Step 4: Risk Characterization
    Cancer: cancer risk (CR) = ADD × CSF  → target 10⁻⁶ per pathway
    Non-cancer: hazard quotient (HQ) = ADD / RfD  → target HQ < 1.0
    Hazard index (HI) = sum of HQs for contaminants with same target organ

  RISK-BASED CORRECTIVE ACTION (RBCA):
    Instead of cleanup to background, set site-specific target levels (SSTLs)
    based on actual land use and exposure pathways.
    Residential SSTL < Industrial SSTL (more sensitive receptor)
    Groundwater cleanup to drinking water MCL (if there's a pathway)
    Soil cleanup may differ if groundwater pathway is removed by ICs
    (institutional controls — deed restrictions, groundwater use restrictions)
```

---

## Remediation Technology Selection

```
  TECHNOLOGY SELECTION MATRIX

  ┌────────────────────────┬────────────┬──────────┬────────────────┐
  │ Technology             │ Target     │ Phase    │ Notes          │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Pump-and-treat (P&T)  │ Dissolved  │ Sat. zone│ Extracts GW;  │
  │                        │ phase      │          │ treats ex-situ;│
  │                        │ plume      │          │ good plume     │
  │                        │            │          │ control; poor  │
  │                        │            │          │ source zone    │
  │                        │            │          │ cleanup; long  │
  │                        │            │          │ operating life │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Soil vapor extraction  │ VOCs in    │ Vadose   │ Apply vacuum;  │
  │ (SVE)                  │ vadose zone│          │ volatilize VOCs│
  │                        │            │          │ → extracted;   │
  │                        │            │          │ most effective │
  │                        │            │          │ for LNAPLs     │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Air sparging (AS)      │ Dissolved  │ Sat. zone│ Inject air     │
  │                        │ + residual │          │ below WT;      │
  │                        │ VOCs       │          │ volatilizes    │
  │                        │            │          │ dissolved VOCs │
  │                        │            │          │ to vadose →    │
  │                        │            │          │ captured by SVE│
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ In-situ chemical       │ Source zone│ Both     │ Inject strong  │
  │ oxidation (ISCO)       │            │          │ oxidant → fast │
  │                        │            │          │ but limited    │
  │                        │            │          │ radius; may    │
  │                        │            │          │ mobilize metals│
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ In-situ chemical       │ Chlorinated│ Sat. zone│ Inject ZVI     │
  │ reduction (ISCR)       │ solvents   │          │ (zero-valent   │
  │                        │            │          │ iron) or       │
  │                        │            │          │ sulfate — abio-│
  │                        │            │          │ tic reduction  │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Bioremediation         │ VOCs, PAHs,│ Both     │ See below      │
  │ (bio-stim/augment)     │ chlorinated│          │                │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Thermal treatment      │ DNAPLs,    │ Source   │ See below      │
  │ (ERH/ISTD/steam)       │ recalcit.  │ zone     │                │
  ├────────────────────────┼────────────┼──────────┼────────────────┤
  │ Monitored natural      │ Dissolved  │ Sat. zone│ Document NA    │
  │ attenuation (MNA)      │ phase      │          │ occurring;     │
  │                        │ plume      │          │ long-term      │
  │                        │            │          │ monitoring;    │
  │                        │            │          │ requires        │
  │                        │            │          │ shrinking plume │
  └────────────────────────┴────────────┴──────────┴────────────────┘
```

### In-Situ Chemical Oxidation (ISCO)

```
  ISCO REAGENTS:
  ┌──────────────────────┬────────────────────────────────────────┐
  │ Reagent              │ Notes                                  │
  ├──────────────────────┼────────────────────────────────────────┤
  │ Potassium/sodium     │ KMnO₄ or NaMnO₄; stable, long         │
  │ permanganate (KMnO₄) │ persistence in aquifer; good for       │
  │                      │ TCE/PCE; leaves MnO₂ precipitate      │
  ├──────────────────────┼────────────────────────────────────────┤
  │ Persulfate (Na₂S₂O₈) │ Activated by heat, iron, or alkaline; │
  │                      │ very reactive; treats wide range of    │
  │                      │ VOCs + SVOCs                           │
  ├──────────────────────┼────────────────────────────────────────┤
  │ Fenton's reagent     │ H₂O₂ + Fe²⁺ → hydroxyl radical (·OH) │
  │                      │ Extremely reactive but short-lived;   │
  │                      │ low pH required; exothermic           │
  ├──────────────────────┼────────────────────────────────────────┤
  │ Ozone (O₃)           │ Gas injection; very reactive;         │
  │                      │ quick treatment of accessible zones;  │
  │                      │ limited radius of influence           │
  └──────────────────────┴────────────────────────────────────────┘
  Challenge: DNAPL source zones have limited reagent contact due to
  heterogeneous geology. ISCO often achieves 60–90% mass removal
  but not 100% — residual dissolves back into groundwater.
```

### Bioremediation

```
  IN-SITU BIOREMEDIATION

  BIOSTIMULATION (enhance existing microbes):
  ├── Petroleum hydrocarbons (aerobic): inject O₂ or air → stimulate
  │   hydrocarbon-oxidizing bacteria (already ubiquitous in soil)
  ├── Chlorinated solvents (anaerobic reductive dechlorination):
  │   inject electron donor (EVO — emulsified vegetable oil, sodium lactate,
  │   molasses) → fermentation → H₂ → drives reductive dechlorination
  └── Sulfate addition: stimulates sulfate-reducing bacteria → ISCR (abiotic)

  BIOAUGMENTATION (add specific microbes):
  ├── KB-1 (SiREM Labs), SDC-9 (Shaw): commercial DHC cultures
  ├── Dehalococcoides mccartyi (DHC): the organism that completes
  │   TCE → vinyl chloride → ethene (key — prevents vinyl chloride
  │   accumulation which is more toxic than TCE)
  └── Requires: confirming DHC absent or insufficient in site aquifer
                before augmenting (qPCR analysis for DHC gene copy numbers)

  MONITORING (to confirm bioremediation is working):
  ├── Decreasing parent compound (PCE/TCE)
  ├── Increasing daughter products in expected sequence
  ├── Ethene/ethane as evidence of complete dechlorination
  ├── Decreasing ORP, increasing H₂ — indicator of reducing conditions
  └── qPCR: DHC gene copy numbers (Dhc_vcrA = vinyl chloride reductase gene)
```

### Thermal Treatment Technologies

```
  THERMAL REMEDIATION (aggressive source zone treatment)

  ERH (Electrical Resistance Heating):
  ├── Electrodes in ground → resistive heating of groundwater/soil
  ├── Heats to 100°C (boiling point) → volatilizes DNAPLs
  ├── Extracted vapors by SVE system
  ├── Effective for: TCE, PCE, PCBs, petroleum
  └── Time to completion: weeks to months vs. years for P&T

  STEAM ENHANCED EXTRACTION:
  ├── Steam injection drives heating front outward from wells
  ├── Steam condensate front mobilizes and volatilizes DNAPLs
  └── Effective but requires careful design to avoid mobilizing DNAPL
      beyond capture zone

  ISTD (In-Situ Thermal Desorption):
  ├── Thermal conduction heating wells → bake soil to 300–500°C
  ├── Very effective for recalcitrant contaminants (PCBs, dioxins,
  │   mercury, high boiling point semivolatiles)
  └── Slow heat conduction; higher cost but very thorough

  Thermal treatment is the closest to "complete" source zone elimination
  but is expensive ($50–200/ton treated soil). Most cost-effective when
  combined with bioremediation/MNA for the dissolved plume.
```

### Monitored Natural Attenuation (MNA)

```
  MNA is NOT "do nothing" — it is documented demonstration that natural
  processes are reducing risk at an acceptable rate.

  REQUIRED LINES OF EVIDENCE:
  1. Primary (essential): Historical data showing contaminant plume
     is stable or shrinking; geochemical indicators of degradation
     (decreasing ORP, sulfate, methane presence → reducing conditions)
  2. Secondary: Laboratory microcosm studies confirming degradation
  3. Tertiary (optional): Molecular biological tools (qPCR, stable
     isotope probing confirming degradation)

  Acceptance criteria:
  ├── Plume is not expanding toward receptors
  ├── Time to attainment is acceptable to regulators
  └── Institutional controls (deed restrictions) in place if needed

  MNA is often the endgame strategy after active remediation reduces
  contaminant mass — active treatment first, then MNA for residuals.
```

---

## PFAS Remediation — The Current Challenge

```
  PFAS REMEDIATION STATUS (as of 2025)

  What doesn't work (conventional approaches):
  ├── Bioremediation: C-F bond is essentially indestructible biologically
  ├── Chemical oxidation (permanganate, persulfate): do not cleave C-F
  ├── Air sparging/SVE: PFAS are not volatile (high-MW, ionic)
  └── P&T with standard effluent treatment: transfers PFAS to liquid
      waste stream — does not destroy

  What works for containment and concentration:
  ├── Pump-and-treat + GAC or PFAS-selective IX resin for treatment
  │   (concentrates PFAS in spent media — not destruction)
  └── Permeable reactive barriers (GAC PRB) — passive interception

  PFAS DESTRUCTION (emerging technologies):
  ├── Supercritical water oxidation (SCWO): water + O₂ at >374°C, >221 bar
  │   → cleaves C-F; proven but expensive; in early commercial deployment
  ├── Electrochemical oxidation: anodic oxidation with boron-doped diamond
  │   electrodes; mineralizes PFAS at point of use; promising for leachate
  ├── Sonochemical: ultrasonic cavitation → radical attack on C-F;
  │   works in lab but scale-up challenging
  └── High-temperature incineration: >1100°C in permitted hazardous waste
      incinerator; effective but PFAS must be concentrated first (brine/spent
      carbon → incinerator)

  REGULATORY PRESSURE:
  PFAS is now driving Phase I/II ESA at any site near AFFF use (airports,
  military bases, fire training areas, industrial facilities using AFFF),
  and in any due diligence for data center sites near such locations.
```

---

## Feasibility Study and Remedy Selection

```
  EPA NINE CRITERIA FOR REMEDY SELECTION (40 CFR 300.430)

  THRESHOLD CRITERIA (must pass):
  1. Overall protection of human health and environment
  2. Compliance with ARARs (applicable/relevant/appropriate requirements)

  PRIMARY BALANCING CRITERIA:
  3. Long-term effectiveness and permanence
  4. Reduction of toxicity, mobility, or volume through treatment
  5. Short-term effectiveness
  6. Implementability (technical and administrative feasibility)
  7. Cost

  MODIFYING CRITERIA:
  8. State acceptance
  9. Community acceptance

  The Record of Decision (ROD) documents the selected remedy,
  the rationale against the nine criteria, and the PRG/RAO
  (preliminary remediation goals / remedial action objectives).
```

---

## Decision Cheat Sheet

| Scenario | Recommended Approach |
|----------|---------------------|
| Petroleum (LNAPL) contamination at UST site | Free product skimming + SVE for vadose; biostimulation for dissolved plume; MNA for residual |
| Chlorinated solvent (DNAPL) source zone — accessible | ERH or ISCO (permanganate) for source zone mass reduction; then biostimulation/bioaugmentation for dissolved phase |
| Chlorinated solvent — DHC absent in aquifer | Bioaugmentation (KB-1 or SDC-9) after biostimulation to establish reducing conditions |
| Dissolved plume, no active source, stable boundaries | MNA with monitoring network and ICs; submit three lines of evidence to regulator |
| PFAS plume at former airfield | P&T with PFAS-selective IX resin or GAC; concentrated brine to SCWO or permitted incineration; no in-situ options yet proven at scale |
| Need to evaluate site before purchase | Phase I ESA (ASTM E1527-21) — provides CERCLA innocent landowner defense |
| Site has clear RECs — former dry cleaner | Phase II ESA — soil borings + GW monitoring wells; PCE/TCE analysis (SW-846 8260) |
| What cleanup standard should I use? | RBCA: industrial use standard if land use stays commercial; residential if residential receptor possible |

---

## Common Confusion Points

**Pump-and-treat doesn't "clean up" source zones**: P&T is very effective for plume
containment (hydraulic control) but essentially never achieves drinking water standards
in the source zone for DNAPL contamination. Residual DNAPL in pore spaces continues
dissolving for decades. P&T is a management strategy, not a cleanup solution for
DNAPL source zones. Agencies increasingly require source zone treatment (thermal, ISCO)
before P&T can be approved as a long-term strategy.

**Phase I gives legal protection, not certainty**: A clean Phase I ESA does not mean a
site is uncontaminated. It means the due diligence was performed to the ASTM standard.
If contamination is discovered later, you've done what was reasonably required to claim
innocent landowner defense. The Phase I is a liability screen, not an environmental audit.

**MNA requires active documentation**: Regulators do not simply accept "nature will clean
it up." You need to demonstrate with data — groundwater monitoring, geochemical
indicators, molecular biology — that attenuation is occurring at a rate protective of
receptors. MNA with an approved monitoring plan is an active remedy with reporting
obligations, not passive abandonment.

**ISCO may cause rebound**: After chemical oxidant injection, contaminant concentrations
often spike (due to solubilization of previously trapped NAPL), then decrease. But
rebound — concentrations rising again after treatment — is common when DNAPL source
material dissolves back into the treated zone over time. Multiple ISCO injection events
may be required, or ISCO should be combined with source zone mass removal.

**Vinyl chloride is more regulated than TCE**: TCE (the parent compound) has an MCL of
5 ppb. Vinyl chloride (its dechlorination daughter product) has an MCL of 2 ppb and is
a known human carcinogen (Group 1, IARC). Partial reductive dechlorination that stalls
at vinyl chloride is worse than no dechlorination. This is why confirming complete
dechlorination to ethene is essential in bioremediation monitoring.
