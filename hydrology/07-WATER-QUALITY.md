# Water Quality — Contaminant Transport, Treatment Processes, Water Quality Index

## The Big Picture

```
+===========================================================================+
|                   WATER QUALITY FRAMEWORK                                  |
+===========================================================================+
|                                                                           |
|  SOURCE          TRANSPORT            EXPOSURE              EFFECT        |
|  ──────          ─────────            ────────              ──────        |
|  Point source    Advection            Drinking              Acute toxicity|
|  Nonpoint        Dispersion           Swimming              Chronic/sub-  |
|  source          Dilution             Agriculture           lethal        |
|  Natural         Sorption/            Ecosystem             Carcinogen    |
|  background      desorption           (indirect)            Endocrine     |
|                  Decay/transform                            disrupt       |
|                                                                           |
|  CONTAMINANT CATEGORIES:                                                  |
|  Biological: bacteria, viruses, protozoa, helminths                       |
|  Chemical: nutrients (N, P), metals, organics, pharmaceuticals            |
|  Physical: turbidity, temperature, dissolved oxygen, salinity             |
|  Radiological: radium, radon, uranium (mostly natural), cesium (nuclear)  |
+===========================================================================+
```

---

## Key Water Quality Parameters

```
PHYSICAL:
  Temperature: affects DO solubility, reaction rates, aquatic life
  Turbidity (NTU): light scatter → measure of suspended solids
  Color: true (dissolved organics) vs. apparent (turbidity)
  Total Suspended Solids (TSS): filter-retained particles, mg/L

OXYGEN:
  Dissolved oxygen (DO): critical for aquatic life
    Cold saturation (~15°C): ~10 mg/L
    Warm saturation (~25°C): ~8 mg/L
    Below 5 mg/L: fish stress; below 2 mg/L: most fish die
  Biochemical Oxygen Demand (BOD₅):
    O₂ consumed by microbes in 5 days at 20°C
    Measure of biodegradable organic matter
    Clean river: <2 mg/L; Treated wastewater: 10–30 mg/L; Raw sewage: 100–300 mg/L
  Chemical Oxygen Demand (COD): all oxidizable organics
    BOD ≈ 0.5–0.7 × COD (for typical domestic wastewater)

NUTRIENTS:
  Total Phosphorus (TP): mg/L; sum of all P forms
  Soluble Reactive Phosphorus (SRP/TDP): immediately bioavailable
  Total Nitrogen (TN): sum of NO₃ + NO₂ + NH₄ + organic N
  NH₄⁺ (ammonium): toxic to fish at elevated pH (un-ionized NH₃ form)
    NH₄⁺ ⇌ NH₃ + H⁺; pKa = 9.25; at pH 8, ~2% NH₃; at pH 10, ~60% NH₃
  NO₃⁻ (nitrate): MCL 10 mg N/L (methemoglobinemia risk in infants)
```

---

## Contaminant Transport in Rivers and Groundwater

### Dissolved Transport

```
FULLY MIXED STREAM:
  For conservative (non-reacting) tracer in 1D river:
    C(x,t) = (M/A√(4πDt)) × exp(-(x-vt)²/(4Dt))

  v = stream velocity, D = longitudinal dispersion, A = cross-section, M = mass injected

  MIXING ZONES:
    Complete mixing requires travel time t* = B²/(8D_T)
    where B = stream width, D_T = transverse dispersion coefficient
    D_T ≈ 0.6 × u* × h (u* = shear velocity, h = depth)

FIRST-ORDER DECAY IN STREAMS:
  Bacterial die-off, BOD consumption, photodegradation:
  dC/dt = -k C → C(t) = C₀ exp(-k t)
  In terms of distance: C(x) = C₀ exp(-k x/v)

  DO SAG CURVE (Streeter-Phelps, 1925):
    Classic model for BOD → DO depletion in rivers

    dD/dt = k_d × L - k_r × D

    D = DO deficit (DO_sat - DO_actual), mg/L
    k_d = BOD decay rate (deoxygenation), day⁻¹
    k_r = reaeration rate (reoxygenation from atmosphere), day⁻¹
    L = BOD remaining at time t

    Solution gives "sag" shape: DO drops downstream of discharge,
    then recovers as BOD consumed and reaeration restores DO.
    Critical point: x_c = (v/k_d-k_r) × ln[(k_r/k_d) × (1 - D₀(k_r-k_d)/(k_d L₀))]

    Used to: set discharge limits on BOD to protect DO standards
```

### Nonpoint Source Pollution

```
NONPOINT SOURCE (NPS) vs. POINT SOURCE:
  Point source: pipe, outfall — precise location, regulated by permit
  Nonpoint source: diffuse — agriculture, urban runoff, atmospheric deposition
  NPS accounts for ~60–70% of US water quality impairments (EPA 303d lists)

MAJOR NPS CATEGORIES:
  Agricultural:
    NO₃⁻ from fertilizers: leaches through soil to groundwater or tile drains
    TP from manure, erosion: binds to sediment particles
    Pesticides: herbicides (atrazine), insecticides
  Urban:
    Heavy metals from vehicle brake pads (copper), tire wear (zinc, 6PPD-quinone)
    Hydrocarbons from road surfaces
    Pet waste, leaf litter (BOD, nutrients)
    Temperature (hot pavement runoff heats streams)
  Atmospheric:
    N deposition (NOₓ from combustion) on watersheds
    Mercury deposition → methylation → bioaccumulation in fish food chain

BEST MANAGEMENT PRACTICES (BMPs):
  Agricultural: riparian buffers, cover crops, precision fertilizer application
  Construction: silt fences, sediment basins, stabilization
  Urban: GI (see 06-WATER-ENGINEERING.md), street sweeping, pet waste stations
  Wetland restoration: natural nutrient filter in watershed
```

---

## Drinking Water Treatment Train

```
CONVENTIONAL SURFACE WATER TREATMENT:

  RAW WATER → INTAKE SCREENING → COAGULATION → FLOCCULATION
  → SEDIMENTATION → FILTRATION → DISINFECTION → DISTRIBUTION

1. COAGULATION/FLOCCULATION:
   COAGULATION: add coagulant → charge neutralization → primary particles destabilize
     Alum: Al₂(SO₄)₃ → Al³⁺ → compresses electrical double layer on particles
     Ferric chloride: FeCl₃ → similar mechanism + sweep floc
     Polymer coagulants: PAC (polyaluminum chloride) — common modern coagulant
     Optimum pH: Al coagulation: 6.5–7.5; Fe coagulation: 5–8
     Rapid mixing: G ~300–700 s⁻¹ for 30–60 seconds

   FLOCCULATION: gentle mixing to grow floc particles
     G ~20–70 s⁻¹ for 15–30 minutes
     Camp number Gt ≈ 10⁴–10⁵ (G = velocity gradient, t = time)
     Floc particles: 1 μm → 100–1000 μm (settles readily)

2. SEDIMENTATION:
   Gravity settling of coagulated particles
   Horizontal-flow sedimentation basin: overflow rate = Q/A = 0.5–2.5 m/h
   Inclined plate settler (lamella settler): increases effective area × 5–20
   Sedimentation efficiency: Stokes' law
     v_s = (ρ_p - ρ_w) g d² / (18μ)
     Particles > 50 μm settle quickly; < 1 μm → colloidal (doesn't settle → coagulation critical)

3. FILTRATION:
   Rapid gravity filter: sand + anthracite media, 5–15 m/h rate
   Mechanisms: straining, sedimentation, interception, diffusion, surface attachment
   Backwash: reverse flow to clean filter (every 24–72 hr)
   Membrane filtration (MF, UF): pore size 0.01–0.1 μm
     MF: removes protozoa (Cryptosporidium, Giardia), bacteria
     UF: removes viruses (some), bacteria
     NF, RO: removes dissolved organics, salts, pharmaceuticals

4. DISINFECTION:
   CHLORINATION (Cl₂ or NaOCl):
     Most common disinfectant globally
     Mechanism: oxidation of cell membrane, DNA damage
     Free chlorine: HOCl + OCl⁻; HOCl more effective
     CT concept: C × T = contact concentration × contact time (mg·min/L)
     Giardia inactivation (3-log): CT = 40 mg·min/L at pH 7, 10°C
     Cryptosporidium: CHLORINE INEFFECTIVE → use UV or ozone
     Disinfection Byproducts (DBPs): Cl₂ + NOM → trihalomethanes (THMs), HAAs
       THMs (chloroform, etc.): MCL = 80 μg/L total; suspected carcinogens
       DBP management: remove NOM before chlorination; reduce Cl₂ dose; switch to chloramine

   UV DISINFECTION:
     254 nm UV damages DNA (thymine dimers → inhibits replication)
     Dose: 40 mJ/cm² → 4-log Giardia; 40 mJ/cm² → 3-log Crypto (very effective)
     Advantages: no DBPs, effective against Crypto
     Disadvantages: no residual (must chlorinate after for distribution system)

   OZONATION:
     Ozone (O₃): very strong oxidant
     Effective against: pathogens, taste/odor compounds, micropollutants
     Forms biologically active filters (BAF): O₃ breaks large organics into biodegradable
       → biofilter (activated carbon) removes → better DBP precursor removal
     DBP: bromate (BrO₃⁻) from ozone + bromide; MCL = 10 μg/L

5. ADVANCED TREATMENT:
   Activated carbon: GAC (granular) or PAC (powdered)
     Adsorbs: taste/odor, pesticides, pharmaceuticals, DBP precursors
   Softening: lime-soda process or IX (ion exchange) to remove Ca, Mg (hardness)
   Reverse osmosis: removes dissolved salts, micropollutants
     Required for: brackish/saline sources, PFAS removal
```

---

## Wastewater Treatment

```
CONVENTIONAL WASTEWATER TREATMENT:

  SCREENING → PRIMARY SEDIMENTATION → BIOLOGICAL TREATMENT
  → SECONDARY SEDIMENTATION → DISINFECTION → DISCHARGE

PRIMARY TREATMENT: physical removal
  Bar screen: removes gross solids
  Primary clarifier: gravity settling of settleable solids
  Remove: ~50% TSS, ~35% BOD
  Primary sludge: ~40–60% of total sludge produced

SECONDARY (BIOLOGICAL) TREATMENT: dissolved organic removal
  ACTIVATED SLUDGE (most common):
    Aeration basin: air + wastewater + "mixed liquor" (bacteria suspension)
    Microorganisms oxidize BOD + NH₄ (nitrification)
    Secondary clarifier: bacteria settle → return activated sludge (RAS)
      back to aeration basin; waste activated sludge (WAS) to digestion
    Effluent: TSS < 20 mg/L, BOD < 20 mg/L (typical secondary standard)
    SRT (solids retention time): 5–15 days (mesophilic)
      Longer SRT → more nitrification; shorter → younger culture, less nitrification

  MEMBRANE BIOREACTOR (MBR):
    Activated sludge + membrane filtration in one tank
    Eliminates secondary clarifier
    Better effluent quality (TSS < 5 mg/L)
    More expensive, membrane fouling management required

NUTRIENT REMOVAL (nitrogen):
  Nitrification (aerobic): NH₄⁺ → NO₂⁻ → NO₃⁻ (Nitrifiers: Nitrosomonas, Nitrobacter)
  Denitrification (anoxic): NO₃⁻ → N₂ (Heterotrophs in anoxic zone)
  A/O, A/A/O, Bardenpho: various configurations of aerobic/anoxic zones
  BNR (Biological Nutrient Removal): removes both N and P biologically

PHOSPHORUS REMOVAL:
  Biological: "luxury uptake" by polyphosphate-accumulating organisms (PAOs)
  Chemical: add FeCl₃ or Al₂(SO₄)₃ → precipitate FePO₄ or AlPO₄

SLUDGE TREATMENT:
  Thickening → Anaerobic digestion → Dewatering → Biosolids
  Anaerobic digestion: 35–55°C, 20–30 day HRT, ~50% VS reduction
  Biogas production: ~0.5 m³ methane per kg VS destroyed
    → CHP (combined heat and power) at modern WRRFs
  Biosolids: Class A or B based on pathogen reduction
    Class A: land application, composting, direct food crop use possible
    Class B: restricted land application (no direct human food crop contact for period)
```

---

## Water Quality Standards and Indices

```
US REGULATORY FRAMEWORK:
  Safe Drinking Water Act (SDWA):
    MCLs (Maximum Contaminant Levels): legally enforceable standards
    MCLGs (Maximum Contaminant Level Goals): non-enforceable health goals
    Treatment technique requirements (Cryptosporidium, turbidity)

  Clean Water Act (CWA):
    Water quality standards: designated uses + criteria to protect them
    Designated uses: aquatic life, human contact recreation, water supply, aesthetic
    NPDES (National Pollutant Discharge Elimination System): permit for discharges
    303(d) list: impaired waters not meeting standards → TMDL required
    TMDL (Total Maximum Daily Load): maximum pollutant load a water body can receive

KEY MCLs (drinking water):
  Turbidity: ≤ 0.3 NTU (95% of samples), 1 NTU max (filtration)
  Total coliform: 5% positive samples in month (RTCR: zero positive allowed)
  E. coli: zero in any sample
  NO₃⁻: 10 mg N/L (methemoglobinemia)
  Arsenic: 10 μg/L
  Lead: 15 μg/L (action level, 90th percentile)
  PFAS (2024 EPA rule): PFOA: 4 ng/L; PFOS: 4 ng/L; combinations
  Total THMs: 80 μg/L; HAA5: 60 μg/L
  Atrazine: 3 μg/L

WATER QUALITY INDEX (WQI):
  Single number summarizing overall water quality
  Canadian WQI (CCME) — widely adopted:
    F1 = scope (% parameters failing)
    F2 = frequency (% tests failing)
    F3 = amplitude (magnitude of failures)
    WQI = 100 - (√(F1² + F2² + F3²) / 1.732)
    100 = excellent, 0 = terrible

TROPHIC STATE INDEX (TSI) for lakes (Carlson):
  TSI = 60 - 14.4 × ln(Secchi depth)
  TSI = 9.81 × ln(Chl-a) + 10.4
  TSI = 14.42 × ln(TP) + 4.15
  30–50: oligotrophic, 50–70: eutrophic, >70: hypereutrophic
```

---

## Emerging Contaminants

```
PFAS (Per- and Polyfluoroalkyl Substances):
  ~12,000+ compounds; "forever chemicals" — extremely resistant to degradation
  C-F bond: strongest in organic chemistry (bond energy ~544 kJ/mol vs C-H ~413)
  Sources: AFFF firefighting foam (military bases), non-stick coatings (Teflon), food packaging
  Detected: in blood of virtually all Americans; in Arctic marine mammals; breast milk
  Health: kidney cancer, thyroid disease, immune suppression, developmental effects
  Treatment: GAC (good but regeneration releases PFAS), ion exchange (IX), RO (best)
  Disposal: PFAS concentrate from treatment → must be destroyed (incineration at >1100°C, electrochemical oxidation)
  Liability: 3M, DuPont, Chemours have paid billions in settlements

MICROPLASTICS:
  <5 mm particles from plastic degradation, synthetic fibers, tire wear
  Found: all oceans, deep sea sediments, Arctic ice, drinking water, human blood
  Health effects: still being studied; bioaccumulation of sorbed contaminants
  Treatment: conventional filtration removes most; very fine particles escape

PHARMACEUTICALS AND PERSONAL CARE PRODUCTS (PPCPs):
  Antibiotics, hormones, anti-depressants, analgesics → wastewater → receiving waters
  Incomplete removal by conventional WWT (50–95% removal varies widely)
  Estrogenic effects: documented in fish (feminized male fish below WWT outfalls)
  Antibiotic resistance: contributes to AMR (antimicrobial resistance)
  Advanced treatment (ozonation, GAC, AOP) required for effective removal
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is BOD? | Biochemical oxygen demand: O₂ consumed by microbes in 5 days oxidizing organics in water |
| What is the CT concept? | Disinfectant concentration × contact time → required dose for specific pathogen inactivation |
| Why is Cryptosporidium special? | Resistant to chlorine; requires UV or ozone; transmitted by very low dose; important in drinking water |
| What does coagulation do? | Destabilizes colloidal particles via charge neutralization → they can aggregate and settle |
| What is TMDL? | Total Maximum Daily Load: maximum pollutant load a water body can assimilate and still meet standards |
| What removes PFAS from water? | GAC, ion exchange, or reverse osmosis; conventional treatment largely ineffective |
| What is the Streeter-Phelps model? | BOD-DO sag curve: dissolved oxygen deficit downstream of organic discharge; predicts DO minimum |
| What is biological nutrient removal? | Wastewater treatment using nitrification (aerobic) + denitrification (anoxic) to remove nitrogen |

---

## Common Confusion Points

**BOD vs. COD**: BOD measures what microbes can consume in 5 days (biodegradable organics). COD measures everything chemically oxidizable (biodegradable + non-biodegradable). COD/BOD ratio tells you treatability: ratio ~1.5 = easily treatable; ratio >3 = significant non-biodegradable fraction → needs advanced treatment.

**Turbidity is not the same as contamination**: High turbidity = suspended solids, but those solids could be harmless clay particles. However, turbidity interferes with UV disinfection and can shield pathogens from chlorine. The MCL of 0.3 NTU is about ensuring effective disinfection, not directly about pathogen content.

**Secondary treatment meets "basic" limits but not nutrient limits**: Secondary treatment (conventional activated sludge) typically achieves BOD < 30 mg/L, TSS < 30 mg/L. But it does NOT reliably remove nitrogen or phosphorus (15–30 mg/L TN typically remains). Tertiary (nutrient removal) steps are needed for sensitive water bodies. Many old plants are secondary-only → major source of eutrophication.

**PFAS is everywhere and persistent**: Unlike most organic contaminants that biodegrade or adsorb to sediments, PFAS compounds are mobile (highly water-soluble), don't biodegrade (C-F bond too strong), and bioaccumulate. Even very low concentrations (pg/L) are detectable everywhere. The 2024 EPA MCLs of 4 ng/L are extremely stringent — many plants cannot meet them without advanced treatment upgrades.

**Hard water is not a health issue but is an infrastructure issue**: Hard water (high Ca²⁺, Mg²⁺) causes scale (CaCO₃ precipitation in pipes and water heaters), not a direct health problem. Softening (lime or IX) removes hardness for industrial/domestic convenience. There's actually evidence that moderate hardness is protective against cardiovascular disease — soft water deficient in Ca/Mg may be slightly riskier. The regulatory focus on hardness is operational, not health.
