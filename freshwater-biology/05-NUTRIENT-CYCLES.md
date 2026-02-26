# Nutrient Cycling: Nitrogen, Phosphorus, and Silicon in Freshwater

## The Big Picture

Freshwater nutrient cycles differ fundamentally from marine biogeochemistry in three key ways: (1) P is typically the primary limiting nutrient (not N as in the ocean), (2) N-fixation cannot bypass P limitation, so P is the true bottleneck in most lakes, and (3) the watershed/catchment is the primary driver of loading — you cannot understand a lake's chemistry without understanding its watershed.

```
FRESHWATER NUTRIENT SYSTEM

  WATERSHED INPUT                   IN-LAKE PROCESSES            EXPORT
  +------------------+              +------------------+          +------+
  | Atmospheric dep. |              | Primary prod.    |          | To   |
  | Agricultural     | --> N, P --> | Nutrient uptake  | --> -->  | outlet|
  | Runoff           |     Si       | Internal loading |          | stream|
  | Point sources    |              | Sedimentation    |          +------+
  | Groundwater      |              | Denitrification  |
  +------------------+              | Nutrient cycling |
                                    | (biotic + abiotic)|
                                    +------------------+

  MASTER QUESTION FOR EACH LAKE:
  What is limiting primary production: N, P, or light?
  --> Determines which nutrient controls eutrophication risk
  --> Determines which nutrient to target for management
```

---

## Section 1 — Phosphorus: The Primary Limiting Nutrient in Freshwater

### Why P Limits Most Freshwater Systems

```
  MARINE vs. FRESHWATER LIMITING NUTRIENT:

  OCEAN: N is often limiting (Redfield N:P = 16:1 by atoms; N often < 16× P)
         Reason: no N-fixation at rate sufficient to compensate N losses
                 N-fixation by cyanobacteria can supplement N supply
                 --> but P unavailability still limits cyanobacteria too
                 --> ultimate limitation: P (on longer timescales)

  FRESHWATER: P almost always limiting
         Reason 1: N enters from atmosphere (N2 fixation, atmospheric deposition)
                   P has NO atmospheric reservoir
         Reason 2: Watershed input of N typically exceeds P (agriculture)
         Reason 3: N:P ratio in most lake water >> 16:1 (P-depleted)
         Reason 4: Cyanobacteria can fix N2 when N limits, but cannot fix P
         --> When N depleted, cyanobacteria bloom; when P depleted, nothing blooms

  LIEBIG'S LAW OF THE MINIMUM:
  Growth rate controlled by the most limiting resource
  Add the non-limiting nutrient: no response
  Add the limiting nutrient: growth increase proportional to addition

  DIAGNOSTIC TEST:
  N:P ratio by mass: < 7 --> N-limited; > 14 --> P-limited; 7–14 --> colimitation
  (Atomic ratio thresholds: N:P < 10 = N-limited; > 17 = P-limited)
```

### Phosphorus Biogeochemistry

```
  P SPECIATION IN WATER:

  TOTAL PHOSPHORUS (TP) = all forms in filtered + unfiltered water
  TOTAL DISSOLVED P = passes through 0.45 µm filter
  SOLUBLE REACTIVE P (SRP) = orthophosphate (PO4³-) = immediately bioavailable
  DISSOLVED ORGANIC P (DOP) = must be hydrolyzed before uptake
  PARTICULATE P = in organisms, detritus, sediment particles

  P SORPTION TO Fe(OH)3 (ferrihydrite):
  Oxic conditions: PO4³- adsorbed to Fe(OH)3 surface -- mobile P removed from water
  Fe(OH)3 + 3H+ + e- --> Fe2+ + 3H2O + PO4³- released (under anoxia)
  This Fe-P coupling is the key mechanism for internal loading (see Guide 01/06)

  P SOURCES TO FRESHWATER:
  Point: Wastewater treatment plant effluent (historically dominated)
  Diffuse: Agricultural runoff (fertilizer P, manure); urban stormwater
  Atmospheric: Minor contribution (< 1% total)
  Geogenic: Rock weathering; usually minor except in volcanic watersheds
```

### Phosphorus Loading Models

Vollenweider (1968) model — the foundation of lake management:

```
  VOLLENWEIDER MODEL:

  [P] = L_P / (q_s × (1 + √(T_W / T_W)))

  Simplified form: [P] ≈ L_P / (z/T_W + v_s)

  Where:
    [P]  = in-lake TP concentration (g/m³)
    L_P  = areal P loading (g/m²/yr) from watershed
    z    = mean lake depth (m)
    T_W  = hydraulic residence time (yr) = volume / outflow rate
    v_s  = P settling velocity (~10 m/yr as rule of thumb)

  KEY INSIGHT: Deep lakes with short residence time are more resilient
               Shallow lakes with long residence time are most vulnerable

  CRITICAL LOADING CONCEPT:
  Vollenweider established empirical threshold L_P levels that predict
  mesotrophic vs. eutrophic transitions
  Used globally for determining acceptable P loads from point sources
```

---

## Section 2 — Nitrogen Cycle in Freshwater

### Nitrogen Transformation Pathways

```
  NITROGEN CYCLE (freshwater lake/stream):

  ATMOSPHERE (N2: 78% of air)
         |
         | BIOLOGICAL N2 FIXATION (nitrogenase enzyme; anaerobic reaction)
         | Organisms: Anabaena, Aphanizomenon (cyanobacteria in lake surface)
         |            Azotobacter, Clostridium (sediment, soils)
         | Rate: 0.1–10 mg N/m²/day in bloom conditions
         v
  ORGANIC N (proteins, nucleic acids in living biomass)
         |
         | AMMONIFICATION (mineralization)
         | Heterotrophic bacteria decompose organic N --> NH4+
         | Rate: depends on temperature, C:N ratio of substrate
         v
  AMMONIUM (NH4+)
         |
         | NITRIFICATION (aerobic; two-step)
         | Step 1: NH4+ + O2 --> NO2- + H2O (Nitrosomonas, Nitrospira)
         | Step 2: NO2- + O2 --> NO3- (Nitrobacter, Nitrospira)
         | Inhibited by: low pH, low O2, high NH4+, temperature < 5°C
         v
  NITRATE (NO3-)
         |
         | PLANT/ALGAL UPTAKE          | DENITRIFICATION (anaerobic)
         | (both NO3- and NH4+)        | NO3- --> NO2- --> NO --> N2O --> N2
         | Algae prefer NH4+           | Bacteria: Pseudomonas, Paracoccus
         v                             | Requires: anoxic conditions + organic C
  ORGANIC N (back to top)             | Occurs: in sediment, anoxic hypolimnion
                                       v
                                  N2 LOST TO ATMOSPHERE
                                  (also N2O greenhouse gas; ~300× CO2 GWP)
```

### N:P Stoichiometry — Redfield Ratio in Freshwater

```
  MARINE REDFIELD RATIO: C:N:P = 106:16:1 (by atoms)
  This reflects the average elemental composition of marine phytoplankton

  FRESHWATER ANALOG:
  Freshwater phytoplankton: C:N:P approximately 106:16:1 to 166:20:1
  But more variable than marine; algal stoichiometry adjusts to nutrient supply

  THRESHOLD ELEMENTAL RATIO (TER) -- Freshwater key values:
  For most phytoplankton: N:P > 22:1 (by mass) --> P-limited
  For most phytoplankton: N:P < 8:1 (by mass)  --> N-limited
  Intermediate: colimitation possible

  CYANOBACTERIA N:P THRESHOLD:
  N:P < 10:1 (by mass) in water --> cyanobacteria competitively favored
  (they can fix N2; advantage disappears when N:P > ~30:1)

  DIAGNOSTIC TOOL:
  If lake water N:P >> 30:1: adding P will cause eutrophication
  If lake water N:P << 10:1: adding N (or losing N via denitrification) may
                              favor cyanobacteria bloom

  THE DOUBLE-CONTROL DEBATE:
  Some researchers advocate dual N+P control (not P alone)
  Rationale: N-fixing cyanobacteria are sometimes not the bloom-formers;
             direct N reduction can help
  Counter: P control is necessary AND sufficient in most lake systems;
           N control supplements but is not a substitute
```

---

## Section 3 — Silicon Cycle

Silicon (Si) is the only major nutrient with a fully biogenic component in freshwater — controlled almost entirely by diatom production and dissolution.

```
  SILICON CYCLE IN A LAKE:

  INPUTS:
  Watershed weathering (primary source): ~2–10 mg Si/L in most stream water
  Precipitation: < 0.1 mg Si/L (negligible)
  Benthic dissolution: from biogenic silica (BSi) in sediments

  IN-LAKE PROCESSING:
  DSi (dissolved silica) --> DIATOM UPTAKE --> BSi (frustule silica)
  Spring diatom bloom can deplete epilimnion DSi to near zero
  Depleted DSi --> diatom decline --> replacement by non-siliceous algae

  DISSOLUTION:
  Dead diatom frustules sink; dissolve in hypolimnion and sediments
  BSi dissolution rate: ~1–5% per day at ambient temperatures
  Deep lakes: most BSi reaches sediment intact and dissolves slowly
  Shallow lakes: more rapid recycling

  DAMS AND Si:
  Dams trap Si-bearing sediment (silt, clay)
  Reservoir phytoplankton bloom depletes DSi
  Result: reduced Si export from dammed rivers
  CONSEQUENCE: downstream lake/estuary diatom communities impacted
  Example: Danube dam (Iron Gate): Si flux to Black Sea dropped 50%;
           Black Sea diatom bloom decline; jellyfish increase

  TYPICAL DSi CONCENTRATIONS:
  Undisturbed forest streams: 3–8 mg Si/L (as SiO2)
  Lake epilimnion post-bloom: < 0.5 mg Si/L (diatom-depleted)
  Hypolimnion (dissolution zone): 5–15 mg Si/L
```

---

## Section 4 — Carbon Cycle

```
  FRESHWATER CARBON:

  DISSOLVED INORGANIC CARBON (DIC):
  CO2(aq) + H2O <--> H2CO3 <--> HCO3- + H+ <--> CO3²- + 2H+
  pH controls speciation:
    pH < 6.3: CO2(aq) dominant
    pH 6.3–10.3: HCO3- dominant (most natural lakes)
    pH > 10.3: CO3²- dominant (very alkaline)

  DISSOLVED ORGANIC CARBON (DOC):
  Colored humic substances (allochthonous) from terrestrial vegetation
  Absorbs UV/visible light -- turns lakes brown (dystrophic)
  "Browning" of boreal lakes: increasing DOC export with climate change
  DOC concentration: oligotrophic clear: 1–5 mg/L; brown boreal: 15–40 mg/L

  LAKE AS NET SOURCE OR SINK?
  Most lakes are net CO2 sources to atmosphere
  Reason: allochthonous organic C enters (more than autochthonous C fixed)
          heterotrophy exceeds autotrophy in most lakes (P/R < 1)
  Exception: highly productive (eutrophic) lakes may be net CO2 sinks
             when algal production exceeds all decomposition

  GLOBAL FRESHWATER CO2 FLUX:
  Lakes and reservoirs: ~0.6 Gt C/yr to atmosphere
  Rivers and streams: ~1.8 Gt C/yr to atmosphere
  (Compared to ocean uptake of ~2.5 Gt C/yr)
```

---

## Section 5 — Nutrient Loading Calculations

```
  AREAL LOADING CALCULATION:

  L_P = Σ(Q_i × C_i) / A_lake

  Where:
    L_P = areal P loading (g P/m²/yr)
    Q_i = annual volume of inflow from source i (m³/yr)
    C_i = P concentration of source i (g P/m³ = mg P/L)
    A_lake = lake surface area (m²)

  EXAMPLE: Lake with area 10 km² (= 10⁷ m²)
  Tributary 1: Q = 5 × 10⁶ m³/yr; C = 0.1 mg P/L = 0.1 g/m³
    Loading = 5×10⁶ × 0.1 / 10⁷ = 0.05 g/m²/yr
  Tributary 2: Q = 2 × 10⁶ m³/yr; C = 0.8 mg P/L (agricultural)
    Loading = 2×10⁶ × 0.8 / 10⁷ = 0.16 g/m²/yr
  WWTP effluent: Q = 5×10⁵ m³/yr; C = 2.0 mg P/L (pre-treatment)
    Loading = 5×10⁵ × 2.0 / 10⁷ = 0.10 g/m²/yr

  Total L_P = 0.05 + 0.16 + 0.10 = 0.31 g/m²/yr

  Vollenweider critical loading for mesotrophic: ~0.15–0.20 g/m²/yr
  --> This lake is OVER the critical threshold; eutrophication expected
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is P limiting in freshwater but N in marine? | P has no atmospheric reservoir; N can be fixed by cyanobacteria; N:P ratio of inputs typically > Redfield |
| What N:P ratio (by mass) signals P limitation? | N:P > 14 by mass (> 22 conservative) = P limiting |
| What N:P ratio favors cyanobacteria? | N:P < 10:1 by mass in water column |
| What's the direct link between anoxic hypolimnion and bloom size? | Fe-P coupling: anoxia releases Fe-bound P; fall turnover recycles it to surface |
| How do dams affect downstream Si supply? | Trap Si-bearing sediment; reservoir diatoms deplete DSi; less Si to downstream/coastal systems |
| What drives boreal lake "browning"? | Increasing DOC export from watersheds (warmer, wetter conditions mobilize more humic acids) |
| What is internal P loading? | P release from sediment under anoxic conditions; can exceed external load in old eutrophic lakes |

---

## Common Confusion Points

**Controlling N alone will not restore a P-limited lake.**
If the system is P-limited, reducing N input has no effect on algal biomass unless N becomes limiting simultaneously. In most north temperate lakes, P control is necessary and sufficient; N control is supplementary.

**The Redfield ratio is descriptive, not prescriptive.**
The 106:16:1 ratio describes average marine phytoplankton composition — it is empirical, not a fixed biological law. Freshwater algae show wider C:N:P variation (luxury uptake of P when available; N-stress responses).

**Denitrification is a permanent N sink; immobilization is not.**
N incorporated into microbial biomass (immobilization) is temporarily retained but will re-mineralize. N reduced to N2 by denitrification is permanently removed from the catchment-water system (exits to atmosphere as a gas).

**Si limitation is underappreciated but significant.**
Silicon limitation is real and can terminate diatom blooms prematurely, shifting communities toward non-siliceous algae (and potentially cyanobacteria). Reduced Si export from dammed rivers has restructured coastal phytoplankton communities in documented cases.
