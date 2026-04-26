# Water Quality: Chemistry, Indicator Species, Monitoring Standards

## The Big Picture

Water quality monitoring translates complex ecological and chemical information into usable metrics for regulation, management, and public health. Three approaches are complementary: physical/chemical parameters (what the water contains), biological indicators (how organisms respond), and combined indices (integrating both into single scores).

```
WATER QUALITY MONITORING FRAMEWORK

  PHYSICAL/CHEMICAL           BIOLOGICAL               COMBINED INDICES
  MONITORING                  INDICATORS               +------------------+
  +------------------+        +------------------+     | EPT Index        |
  | Dissolved O2     |        | Macroinvertebrates|     | IBI (fish)      |
  | BOD / COD        |  --->  | Algae (diatoms)  |  -> | Diatom Index     |
  | Nutrients (N, P) |        | Fish             |     | WQI (composite)  |
  | Temperature      |        | Macrophytes      |     | EU WFD classes   |
  | pH, conductivity |        | Amphibians       |     +------------------+
  | Turbidity        |        +------------------+
  | Metals / toxics  |
  +------------------+
          |
          v
  REGULATORY STANDARDS
  WHO Guidelines (drinking water)
  EPA Primary/Secondary Standards (US)
  EU Water Framework Directive
  National surface water quality criteria
```

---

## Section 1 — Physical Parameters

### Temperature

```
  TEMPERATURE THRESHOLDS FOR FRESHWATER ORGANISMS:

  < 10°C:   Cold-water specialist zone; salmonids, stone flies
  10–15°C:  Cold-cool water transition; brook trout upper limit
  15–20°C:  Cool water fish zone; most trout species
  20–25°C:  Warm water fish zone; bass, perch, sunfish
  25–30°C:  Thermal stress for most temperate species
  > 30°C:   Lethal for most sensitive species

  THERMAL CRITERIA (regulatory):
  Coldwater fishery: daily maximum < 19°C (most US states)
  Trout streams: < 20°C (some states < 18°C)
  Warmwater fishery: < 32°C

  MEASUREMENT: continuous data loggers preferred (HOBO, YSI)
  Temperature fluctuation patterns matter as much as maxima
  Daily maximum + minimum + rate of change are all ecologically relevant
```

### Dissolved Oxygen (DO)

```
  DO MEASUREMENT AND INTERPRETATION:

  MEASUREMENT: Winkler titration (historical, accurate), YSI polarographic probe,
               optical (luminescent) DO sensor (modern standard)

  SATURATION CONCENTRATION (100% DO):
  Depends on temperature, altitude, salinity
  At 20°C, sea level: 9.1 mg/L = 100% saturation
  At 10°C, sea level: 11.3 mg/L = 100% saturation

  BIOLOGICAL THRESHOLDS:
  > 8 mg/L: optimal for coldwater fish; EPA "class A" streams
  6–8 mg/L: suitable for most fish
  4–6 mg/L: suboptimal; behavioral avoidance; some invertebrate mortality
  2–4 mg/L: acute stress; fish kills if prolonged; invertebrate community impacts
  < 2 mg/L: hypoxic; most fish avoid or cannot survive
  0 mg/L:   anoxic; only anaerobic organisms

  DIURNAL VARIATION: In productive shallow systems, DO fluctuates 4–8 mg/L
  daytime peak (photosynthesis) to pre-dawn minimum (respiration only)
  24-hr monitoring required to capture this; spot checks misleading
```

---

## Section 2 — Biochemical Oxygen Demand (BOD) and Chemical Oxygen Demand (COD)

### BOD (Biochemical Oxygen Demand)

BOD measures the O2 consumed by microorganisms decomposing organic matter in a sample over a specified time. It is the fundamental measure of organic pollution.

```
  BOD STANDARD TEST:
  BOD5 = O2 consumed in 5 days at 20°C in dark (standard)
  BOD20 = approximate "ultimate" BOD (full decomposition)
  BOD5 typically ≈ 65–70% of ultimate BOD for municipal sewage

  UNITS: mg O2/L (= mg/L = ppm)

  BOD THRESHOLDS:
  Clean river:     1–2 mg/L
  Slightly polluted: 2–5 mg/L
  Moderately polluted: 5–10 mg/L
  Heavily polluted: 10–20 mg/L
  Raw sewage:      150–300 mg/L
  Food processing effluent: 500–2000 mg/L
  Silage effluent: 30,000–80,000 mg/L (most concentrated organic effluent)

  OXYGEN SAG CURVE (Streeter-Phelps, 1925):
  Below a point source discharge:

  DO
  |
  | ─── ─── ─── ─── ─── ──── ─── ─ saturation
  |   \                          /
  |    \                        /
  |     \                      /
  |      \    sag curve       /
  |       \                  /
  |        \________________/ <-- oxygen sag (critical deficit point)
  +------+-----+---------+-------> Distance downstream
  Point  Zone of Zone of  Zone of
  source degradation recovery cleaner water

  Time to recovery depends on: BOD load, flow velocity, temperature,
  reaeration coefficient (k2), and initial O2 deficit
```

### COD (Chemical Oxygen Demand)

COD measures total oxidizable material (both biologically degradable AND refractory) using strong chemical oxidant (dichromate).

```
  COD vs. BOD RATIO:
  COD > BOD always (COD oxidizes everything; BOD only what bacteria can process)

  COD/BOD ratio interpretation:
  < 2:  mostly biodegradable organic matter
  2–5:  mix of biodegradable and refractory
  > 5:  large refractory fraction (industrial effluent, some agricultural runoff)

  COD is used when:
  +-- BOD is unreliable (toxic inhibition of bacteria)
  +-- Quick results needed (2 hr vs. 5 days)
  +-- Industrial effluent monitoring
  +-- Wastewater plant performance monitoring
```

---

## Section 3 — Nutrients and pH

| Parameter | Clean River | Mesotrophic Lake | Eutrophic Lake | Units |
|-----------|------------|-----------------|----------------|-------|
| Total Phosphorus (TP) | < 0.02 | 0.01–0.035 | > 0.035 | mg P/L |
| Total Nitrogen (TN) | 0.2–0.5 | 0.5–1.5 | > 1.5 | mg N/L |
| Nitrate (NO3-N) | < 1 | 1–3 | > 3 | mg N/L |
| Ammonium (NH4-N) | < 0.1 | 0.1–0.5 | > 0.5 | mg N/L |
| pH | 6.5–8.5 | 7–9 | 7–10 | — |

### pH and Alkalinity

```
  pH ECOLOGY:
  < 4.5: Highly acidic; very few species; acid-tolerant Sphagnum; some Diptera
  4.5–6.0: Acidic; reduced diversity; brown trout can survive; salmonid eggs fail
  6.0–7.5: Near-neutral; optimal for most freshwater species
  7.5–9.0: Slightly alkaline; normal for hard water lakes; photosynthesis raises pH
  > 9.0: Elevated pH during algal bloom; NH4+ --> NH3 (toxic); carbonate precipitation

  ALKALINITY (buffering capacity):
  Total alkalinity = HCO3- + CO3²- + OH- - H+ (approximately = HCO3-)
  Units: mg CaCO3/L or meq/L

  Low alkalinity (< 10 mg/L CaCO3): poorly buffered; vulnerable to acid deposition
  Moderate (20–100 mg/L): typical temperate softwater; moderate buffering
  High (> 100 mg/L): hardwater; strong buffering; carbonates precipitate at high pH

  ACID DEPOSITION IMPACT:
  SO4²- + NO3- deposition + weak buffering capacity --> acidified lakes
  Norway/Sweden: 10,000+ lakes acidified by 1980s (pre-LRTAP abatement)
  Recovery: ~50% recovery since SO2 reductions; NO3 deposition still issue
```

---

## Section 4 — Biological Indicator Systems

### EPT (Ephemeroptera-Plecoptera-Trichoptera) Index

```
  SIMPLE EPT RICHNESS:
  Count distinct EPT taxa at a site (genus or family level)
  Compare to reference sites in same ecoregion

  EPT RICHNESS SCORING (example, Pacific NW USA):
  Reference streams in ecoregion: 25–35 EPT taxa
  Good: > 20 taxa; some reduction from reference
  Impaired: 10–20 taxa; moderate degradation
  Severely impaired: < 10 taxa

  PERCENT EPT ABUNDANCE (%EPT):
  %EPT = (EPT individuals) / (total individuals) × 100
  Reference: > 70–80% in clean streams
  Impaired: < 30–40%

  RATIO INDICES:
  EPT:C ratio = EPT taxa / Chironomidae (midge) + Oligochaeta taxa
  Chironomidae and Oligochaeta tolerate high BOD; their increase signals degradation
```

### Index of Biotic Integrity (IBI) — Fish-Based

Karr (1981) developed the IBI as a multi-metric fish-based index. The concept has been extended to macroinvertebrates, diatoms, and macrophytes.

```
  IBI STRUCTURE (fish-based):
  6–12 metrics, each scored 1, 3, or 5 based on departure from reference:

  METRIC CATEGORIES:
  +-- Species richness and composition (native species count)
  +-- Trophic composition (proportion of piscivores, omnivores, insectivores)
  +-- Sensitive species (presence/abundance of intolerant species)
  +-- Tolerant species (proportion of pollution-tolerant species)
  +-- Abundance and condition (total fish abundance; incidence of disease/deformity)

  SCORING:
  Each metric scored relative to reference condition:
  Score 5 = within 25% of reference (best)
  Score 3 = 25–75% departure from reference
  Score 1 = > 75% departure from reference (worst)

  COMPOSITE IBI SCORE:
  Sum of metric scores; typically range 12–60 (for 12 metrics)
  60 = reference quality | 12 = very poor / no fish

  IBI CLASSES:
  50–60: Excellent (comparable to reference)
  40–49: Good (minor disturbance)
  30–39: Fair (moderate disturbance)
  20–29: Poor (severe disturbance)
  12–19: Very poor (degraded)
```

---

## Section 5 — WHO and EPA Drinking Water Standards

```
  WHO GUIDELINES FOR DRINKING WATER QUALITY (4th ed. + 2022 updates):

  MICROBIOLOGICAL:
  E. coli (thermotolerant coliforms): 0 CFU/100 mL (total absence required)
  Total coliforms: 0 CFU/100 mL (for treated water)

  CHEMICAL (selected parameters):
  Nitrate:      50 mg NO3-/L (acute infant risk; methemoglobinemia)
  Nitrite:      3 mg NO2-/L (chronic)
  Arsenic:      0.01 mg/L
  Lead:         0.01 mg/L (guideline); 0 in plumbing ideal
  Fluoride:     1.5 mg/L (dental fluorosis above this)
  Chlorine (free): 0.2–0.5 mg/L (residual in distribution)
  Turbidity:    < 1 NTU (for effective disinfection)
  pH:           6.5–9.5 (acceptable range)

  RADIOLOGICAL:
  Total effective dose: < 0.1 mSv/yr

  USA EPA STANDARDS (NPDWR -- primary standards):
  Most parameters similar to WHO; some differences:
  Arsenic: 0.01 mg/L (same as WHO after 2002 revision)
  Lead: Action Level 0.015 mg/L (not MCL; treatment technique)
  Chromium total: 0.1 mg/L
  Nitrate: 10 mg NO3-N/L (= 44.3 mg NO3-/L -- different unit from WHO)
  PFOA + PFOS: 4 ng/L individual; 10 ng/L mixed PFAS (2024 final rule)
```

### Comparison: Surface Water vs. Drinking Water Standards

```
  PARAMETER         SURFACE WATER CRITERION    DRINKING WATER MCL
  (US EPA)          (aquatic life protection)  (human health)
  +---------------+---------------------------+-------------------+
  | Ammonia (NH3) | 0.02 mg/L (acute, pH 7)   | No federal MCL    |
  |               | 0.017 mg/L (chronic)      | (palatability ~35)|
  +---------------+---------------------------+-------------------+
  | Copper        | 0.013 mg/L (hardness 100) | 1.3 mg/L (action) |
  | (aquatic)     | (hardness-dependent)      |                   |
  +---------------+---------------------------+-------------------+
  | Lead          | 0.065 mg/L (hardness 100) | 0.015 mg/L (action|
  +---------------+---------------------------+-------------------+
  | Mercury       | 0.77 µg/L (criterion)     | 0.002 mg/L        |
  +---------------+---------------------------+-------------------+
  | Nitrate       | No aquatic life criterion | 10 mg N/L (as N)  |
  | (eutrophi.)   | (eutrophication concern)  |                   |
  +---------------+---------------------------+-------------------+
  | Chlorine      | 0.011 mg/L (aquatic)      | 4 mg/L (MRDL)     |
  +---------------+---------------------------+-------------------+
```

---

## Section 6 — EU Water Framework Directive (WFD)

The EU WFD (2000/60/EC) is the most comprehensive water legislation framework globally. It requires all water bodies to achieve "good ecological status" by a defined date.

```
  EU WFD STRUCTURE:

  OBJECTIVE: All EU surface and groundwater to achieve "Good Status"
  TOOL: River Basin Management Plans (RBMPs); 6-yr cycles
  ASSESSMENT: Ecological status + chemical status

  ECOLOGICAL STATUS CLASSIFICATION (5 classes):
  HIGH:   Reference conditions; minimal anthropogenic impact
  GOOD:   Slight deviation from reference; minor human impact
  MODERATE: Moderate deviation; noticeable but not severe impact
  POOR:   Major deviation from reference; significantly altered ecosystem
  BAD:    Severe alteration; no or very little biological activity

  BIOLOGICAL QUALITY ELEMENTS (BQEs) assessed:
  Phytoplankton (lakes only)
  Macrophytes / phytobenthos (algae including diatoms)
  Macroinvertebrates (benthic invertebrate fauna)
  Fish

  CHEMICAL STATUS: "Good" or "Fail" (no gradation)
  33 priority substances listed; all must be below EQS (Environmental Quality Standards)
  Priority hazardous substances must achieve below-detection-limit concentrations

  PROGRESS (2022 assessment):
  ~37% EU surface water bodies in good/high ecological status
  60% failing to meet good ecological status
  Main pressures: diffuse agriculture (nutrient + pesticide), hydromorphological
  alteration (dams, channelization), point source pollution (some reduction achieved)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What BOD level indicates a healthy river? | < 2 mg/L; > 10 mg/L = heavily polluted |
| What DO level is lethal for most fish? | < 1–2 mg/L; behavioral avoidance below 4 mg/L |
| What is the EU WFD drinking water nitrate limit? | 50 mg NO3-/L; USA EPA equivalent is 44 mg NO3-/L (both convert to 10 mg N/L) |
| What does EPT richness > 20 indicate? | Good to excellent stream quality; reference-like conditions |
| What is the IBI? | Index of Biotic Integrity; multi-metric fish index scoring departure from reference conditions |
| What is the oxygen sag curve? | Streeter-Phelps model: DO drops below point source discharge, reaches minimum at critical deficit, then recovers via reaeration |
| What EU WFD status do 60% of EU water bodies currently fail? | Good ecological status; primarily agricultural diffuse pollution + hydromorphological alteration |

---

## Common Confusion Points

**BOD5 is not ultimate BOD.**
BOD5 (5-day test) captures 65–70% of total oxidizable organic matter in municipal sewage. For industrial or refractory organic compounds, the 5-day fraction may be much lower. Always specify BOD5 vs. ultimate BOD.

**Conductivity is not a pollutant per se.**
Specific conductance (µS/cm) measures dissolved ion concentration. High conductivity can indicate salinization (irrigation return flow), mine drainage (sulfate + metals), or road salt contamination. Low conductivity can indicate acid-impacted soft water. Context determines interpretation.

**EPA aquatic life criteria and drinking water MCLs are different standards for different purposes.**
Aquatic life criteria protect ecosystem organisms — often at 1–100× stricter than drinking water MCLs. A water body that meets drinking water MCLs may still violate aquatic life criteria for copper, lead, ammonia, or temperature.

**The EU WFD "good ecological status" is defined by departure from reference, not by absolute values.**
A lowland eutrophic river may have a "good" ecological status with higher TP than a mountain stream that is "moderate." The classification is relative to what you would expect under near-natural conditions for that water body type — not a single universal threshold.
