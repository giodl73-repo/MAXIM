# Wastewater Treatment

## The Big Picture

Wastewater treatment mimics and accelerates natural decomposition — using microorganisms
to consume organic matter and nutrients under controlled conditions before discharge.

```
  WASTEWATER TREATMENT TRAIN

  Influent  → Primary  → Secondary  → (Tertiary) → Effluent → Receiving
  (raw      → Screen/  → Biological → Sand filt/ →         → Water Body
  sewage)   → Grit rm  → (activated → UV/Cl₂    →         → (NPDES limit)
              → Primary → sludge,    → Membrane  →
              → clarif. → nitrif/    → (for reuse)
                        → denitrif.) →

            ↓ sludge         ↓ wasted sludge (WAS)
            Primary     ──── Gravity thickening
            sludge       ↘   or DAF
                          ↘
                     Anaerobic digestion (AD)
                           ↓              ↓
                       Biogas           Digestate
                     (to CHP or        (to land
                       flare)           application
                                        or dewatering)
```

Design is regulated by NPDES (National Pollutant Discharge Elimination System) permits
under the Clean Water Act. Every discharge point has numeric effluent limits — the
treatment train must be designed to meet them.

---

## Wastewater Characterization

Before sizing any unit process, quantify what you are treating.

```
  TYPICAL DOMESTIC WASTEWATER CONCENTRATIONS (mg/L unless noted)

  ┌──────────────────┬────────────┬────────────────────────────────┐
  │ Parameter        │ Typical    │ Notes                          │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ BOD₅             │ 200–250    │ 5-day biochemical oxygen       │
  │                  │            │ demand — biodegradable organic │
  │                  │            │ matter proxy                   │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ COD              │ 400–500    │ Chemical oxygen demand — all   │
  │                  │            │ oxidizable carbon; COD:BOD     │
  │                  │            │ ~2:1 for domestic sewage;      │
  │                  │            │ >2.5 indicates less            │
  │                  │            │ biodegradable waste            │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ TSS              │ 200–250    │ Total suspended solids         │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ TKN              │ 35–50      │ Total Kjeldahl nitrogen        │
  │                  │            │ (organic N + NH₃) —            │
  │                  │            │ eutrophication driver          │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ TP (Total P)     │ 4–10       │ Phosphorus — eutrophication    │
  │                  │            │ driver (often the limiting     │
  │                  │            │ nutrient in freshwater)        │
  ├──────────────────┼────────────┼────────────────────────────────┤
  │ Pathogens        │ 10⁶–10⁸   │ Fecal coliforms (CFU/100 mL);   │
  │                  │ CFU/100 mL │ Giardia, Crypto, enteric virus │
  └──────────────────┴────────────┴────────────────────────────────┘
```

Industrial wastewater can have orders-of-magnitude higher BOD (food processing, paper mills,
pharmaceutical). The design must account for peak day and peak hour loadings, not just
averages.

---

## Primary Treatment

Removes settleable and floatable solids by physical separation — no biology, no chemicals.

```
  PRIMARY TREATMENT UNIT PROCESSES

  ┌──────────────┬────────────────────────────────────────────────┐
  │ Process      │ Function / Design                              │
  ├──────────────┼────────────────────────────────────────────────┤
  │ Bar screens  │ Coarse screening — removes rags, plastics,    │
  │              │ grit protects downstream equipment            │
  │              │ Mechanically raked; 3/4" to 2" openings       │
  ├──────────────┼────────────────────────────────────────────────┤
  │ Fine screens │ 1–6 mm openings — alternative to primary       │
  │              │ clarifier at smaller plants                    │
  ├──────────────┼────────────────────────────────────────────────┤
  │ Grit chamber │ Removes sand/grit/gravel (ρ ≈ 2.65 g/cm³)    │
  │              │ without removing organics (ρ ≈ 1.02 g/cm³)   │
  │              │ Aerated grit chamber: differential settling   │
  │              │ Vortex grit: centrifugal separation           │
  ├──────────────┼────────────────────────────────────────────────┤
  │ Primary      │ Gravity sedimentation:                         │
  │ clarifier    │ SOR: 400–600 gpd/ft² (16–24 m/d)               │
  │              │ HRT: 1.5–2.5 hours                             │
  │              │ Removal: 50–65% TSS, 25–40% BOD₅               │
  │              │ Produces primary sludge (2–6% solids)          │
  └──────────────┴────────────────────────────────────────────────┘
```

---

## Secondary Treatment: Activated Sludge

The workhorse of wastewater treatment. Microorganisms consume dissolved and colloidal
organic matter in an aeration basin, then settle in a secondary clarifier.

```
  ACTIVATED SLUDGE SYSTEM

  Influent  →  Aeration Basin  →  Secondary  →  Effluent
  (after       (microorganisms    Clarifier      (BOD, TSS
   primary)     oxidize BOD)      |              reduced)
                ↑                 ↓ RAS (return activated sludge)
                |                 ↓ WAS (waste activated sludge)
                └─── RAS ─────────┘
                        recycle maintains MLSS

  ENGINEERING BRIDGE — ACTIVATED SLUDGE AS FEEDBACK CONTROL:
  ─────────────────────────────────────────────────────────────────
  Controlled variable:  MLSS (mixed liquor suspended solids, mg/L)
  Setpoint:             SRT (solids retention time, days)
  Actuator:             WAS rate (waste activated sludge pump speed)
  Feedback signal:      RAS return (recycle loop shown above)
  Disturbance:          Influent flow and BOD load variations

  The RAS loop IS a negative feedback control system.
  Increase WAS → decrease MLSS → decrease SRT.
  Decrease WAS → increase MLSS → increase SRT.
  Modern plants use DO probes + ammonia sensors in closed-loop
  PID control of aeration blowers and WAS pumps.
  ─────────────────────────────────────────────────────────────────

  KEY DESIGN VARIABLES:
  ├── SRT (sludge retention time / solids retention time / MCRT)
  │     = (mass VSS in system) / (mass VSS wasted per day)
  │     Typical: 5–20 days (conventional); >20 days (nitrification)
  │     SRT controls: effluent quality, oxygen demand, sludge production
  │     Longer SRT → better effluent + more stable + less sludge,
  │                  but larger aeration tank required
  │
  ├── HRT (hydraulic retention time)
  │     = aeration tank volume / average influent flow
  │     Typical: 4–8 hours for BOD removal
  │
  ├── MLSS (mixed liquor suspended solids) — operating biomass concentration
  │     Typical: 2,000–4,000 mg/L (conventional)
  │            : 8,000–12,000 mg/L (MBR)
  │
  ├── F/M ratio (food-to-microorganism)
  │     = BOD loading (lb BOD/day) / MLVSS in system (lb VSS)
  │     Typical: 0.05–0.4 d⁻¹
  │     Low F/M → endogenous respiration → low effluent BOD
  │     High F/M → log growth → poor settling (bulking risk)
  │
  └── SVI (sludge volume index) — settleability indicator
        SVI = (settled sludge volume in 30 min, mL/L) / (MLSS, g/L)
        Target: SVI <150 mL/g for good settling
        Filamentous bulking: SVI >200 mL/g — worst operational problem
```

### Monod Kinetics (Lawrence/McCarty Model)

The theoretical basis for activated sludge design:

```
  Substrate removal:    dS/dt = -(μ_max · S · X) / (Y(K_s + S))
  Biomass growth:       dX/dt = Y · (-dS/dt) - k_d · X
    μ_max = maximum specific growth rate (d⁻¹)
    K_s   = half-saturation constant (mg/L BOD)
    Y     = yield coefficient (g VSS / g BOD)
    k_d   = endogenous decay rate (d⁻¹)

  Effluent quality as function of SRT:
  S_e = K_s(1 + k_d·SRT) / (SRT(μ_max - k_d) - 1)

  Key insight: Effluent BOD is controlled by SRT, not HRT.
  Longer SRT → lower S_e. This is why operators set a target SRT
  and control by wasting a specific volume of sludge per day.
```

---

## Aeration

Aeration provides oxygen for microbial metabolism and maintains solids suspension.
It is typically 50–70% of total WWTP energy consumption.

```
  OXYGEN DEMAND CALCULATION

  O₂ required ≈ 1.0 × BOD removed + 4.57 × TKN nitrified
                - 2.86 × NO₃ denitrified - 1.42 × biomass wasted

  AERATION SYSTEMS:
  ┌────────────────┬──────────────────────────────────────────────┐
  │ Type           │ SOTR / Notes                                 │
  ├────────────────┼──────────────────────────────────────────────┤
  │ Fine bubble    │ 6–8% O₂ transfer per meter submergence;     │
  │ diffusers      │ high efficiency (~2 kg O₂/kWh);            │
  │                │ most common for energy efficiency            │
  ├────────────────┼──────────────────────────────────────────────┤
  │ Coarse bubble  │ 3–5% transfer efficiency; less fouling;      │
  │ diffusers      │ less efficient — used where fouling risk     │
  │                │ is high (thickened sludge)                   │
  ├────────────────┼──────────────────────────────────────────────┤
  │ Surface        │ Mechanical splash aerators;                  │
  │ aerators       │ 1.2–2.4 kg O₂/kWh; smaller plants,        │
  │ (floating)     │ oxidation ditches                            │
  └────────────────┴──────────────────────────────────────────────┘
  SOTE (standard oxygen transfer efficiency) must be derated to
  field conditions (AOTE) accounting for wastewater characteristics
  and submergence depth.
```

---

## Biological Nutrient Removal (BNR)

Nitrification + denitrification remove nitrogen. EBPR removes phosphorus.
Regulators increasingly require nutrient limits to prevent eutrophication.

```
  NITROGEN CYCLE IN ACTIVATED SLUDGE

  TKN (org N + NH₃)  →  Nitrification  →  Nitrate (NO₃⁻)
                                           |
                          Denitrification  ↓
                          (anoxic zone)   N₂ gas (out of solution)

  NITRIFICATION:
  NH₄⁺ + 1.5 O₂  →  NO₂⁻ + H₂O + 2H⁺  (Nitrosomonas)
  NO₂⁻ + 0.5 O₂  →  NO₃⁻               (Nitrobacter)
  Net: consumes 4.57 g O₂ per g N nitrified
  Requirements: aerobic (DO >1–2 mg/L), SRT >8–12 days, pH 7–8, temp >10°C
  Nitrifiers are slow-growing (μ_max ≈ 0.5 d⁻¹ vs. 6 d⁻¹ for heterotrophs)
  → SRT governs — if SRT is too short, nitrifiers wash out

  DENITRIFICATION:
  NO₃⁻ + organic carbon  →  N₂ + CO₂ + H₂O
  (anoxic — no dissolved oxygen, but nitrate as electron acceptor)
  Carbon source: raw wastewater (MLE), endogenous respiration, methanol
  2.86 g O₂ equivalent "recovered" per g NO₃ denitrified
  (reduces aeration demand — important for energy balance)

  BNR CONFIGURATIONS:
  ┌──────────────────┬─────────────────────────────────────────────┐
  │ Config           │ Zones (Anaerobic / Anoxic / Aerobic)        │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ MLE              │ Anoxic → Aerobic → clarifier               │
  │ (Modified        │ Internal recycle from aerobic to anoxic    │
  │ Ludzack-         │ Good TN removal; no P removal              │
  │ Ettinger)        │                                             │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ A²/O             │ Anaerobic → Anoxic → Aerobic                │
  │                  │ TN + TP removal; most common BNR config     │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ Bardenpho        │ 5-stage: Anaerobic/Anoxic/Aerobic/         │
  │ (5-stage)        │ Anoxic/Aerobic — very low effluent TN      │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ UCT              │ Modified A²/O — prevents nitrate in RAS     │
  │ (Univ. of Cape   │ from disrupting anaerobic zone for EBPR     │
  │ Town)            │                                             │
  └──────────────────┴─────────────────────────────────────────────┘
```

### Biological Phosphorus Removal (EBPR)

```
  EBPR — Enhanced Biological Phosphorus Removal

  PAOs (polyphosphate-accumulating organisms) exploit alternating
  anaerobic/aerobic conditions:

  ANAEROBIC ZONE:
  PAOs release stored polyphosphate → phosphate to solution
  PAOs take up VFAs (from fermentation) → store as PHB

  AEROBIC ZONE:
  PAOs oxidize PHB → release energy → take up phosphate from solution
  (more P removed from solution than released in anaerobic phase)
  → "luxury uptake"
  Net: P concentrated in biomass → removed via WAS

  Requirements:
  ├── VFAs (volatile fatty acids) in anaerobic zone — fermented organics
  ├── Nitrate-free return to anaerobic zone (NO₃ competes with PAOs)
  └── P:VSS in WAS ≈ 5–7% (vs. 1.5% for ordinary heterotrophs)

  Chemical backup: if EBPR is insufficient or upset, add alum or FeCl₃
  to precipitate phosphate as AlPO₄ or FePO₄ and remove in secondary
  clarifier or sludge
```

---

## Alternative Secondary Processes

```
  PROCESS COMPARISON

  ┌──────────────────┬──────────┬───────────────────────────────────┐
  │ Process          │ Capital  │ Notes                             │
  ├──────────────────┼──────────┼───────────────────────────────────┤
  │ Activated sludge │ Moderate │ Dominant technology; flexible     │
  │ (conventional)   │          │ SRT control; secondary clarifier  │
  │                  │          │ is the weak link (bulking)        │
  ├──────────────────┼──────────┼───────────────────────────────────┤
  │ Trickling filter │ Low      │ Fixed-film (biofilm on media);    │
  │                  │          │ robust; less operator attention;  │
  │                  │          │ lower efficiency than AS;         │
  │                  │          │ odors; older technology           │
  ├──────────────────┼──────────┼───────────────────────────────────┤
  │ MBBR (moving bed │ Low-Mod  │ Plastic carriers provide biofilm  │
  │ biofilm reactor) │          │ surface; no return sludge;       │
  │                  │          │ flexible loading; upgrade-        │
  │                  │          │ friendly for existing plants      │
  ├──────────────────┼──────────┼───────────────────────────────────┤
  │ MBR (membrane    │ High     │ Activated sludge + UF membrane    │
  │ bioreactor)      │          │ replaces secondary clarifier;     │
  │                  │          │ high MLSS (8–12 g/L);             │
  │                  │          │ excellent effluent quality;       │
  │                  │          │ reuse-ready; high energy + O&M    │
  └──────────────────┴──────────┴───────────────────────────────────┘
```

---

## Solids Handling

Secondary treatment produces sludge (waste activated sludge + primary sludge).
Sludge handling is typically 30–50% of total WWTP capital cost.

```
  SOLIDS HANDLING TRAIN

  Primary sludge (2–5% solids)  ──┐
                                   ├──> Thickening ──> Anaerobic ──> Dewatering
  WAS (0.5–1.5% solids)        ──┘    (to 4–8%)      Digestion     (to 20–35%)
                                                          ↓              ↓
                                                       Biogas        Biosolids
                                                       (CH₄/CO₂)    (land appl.
                                                       to CHP/flare  or landfill)

  THICKENING:
  ├── Gravity thickening (primary sludge): SOR 50–100 gpd/ft²
  └── DAF (dissolved air flotation) for WAS:
      micro-bubbles attach to solids → float to surface → skim

  ANAEROBIC DIGESTION (AD):
  ├── Purpose: stabilize biosolids, destroy pathogens, produce biogas
  ├── Process stages:
  │   1. Hydrolysis: polymers (proteins, lipids, carbs) → monomers
  │   2. Acidogenesis: monomers → VFAs + H₂ + CO₂
  │   3. Acetogenesis: VFAs → acetate + H₂ + CO₂
  │   4. Methanogenesis: acetate + H₂/CO₂ → CH₄ + CO₂
  │      (rate-limiting step — methanogens are slow, pH sensitive)
  ├── Operating conditions:
  │   Mesophilic: 35°C, SRT 20–30 days
  │   Thermophilic: 55°C, SRT 10–15 days, Class A pathogen reduction
  ├── Biogas: ~50–65% CH₄, ~35–50% CO₂, traces H₂S
  │   Yield: ~0.35–0.55 m³ CH₄ / kg VS destroyed
  │   Energy content: ~22 MJ/m³ CH₄
  └── VS (volatile solids) reduction: 45–65%

  BIOGAS UTILIZATION:
  ├── Flare (baseline — no energy recovery)
  ├── CHP (combined heat and power — engine/generator): 30–35% electrical
  │   efficiency; waste heat recovers digester heating demand
  └── RNG (renewable natural gas): clean biogas → pipeline injection;
      highest value but capital-intensive
```

### Biosolids and EPA 503

```
  EPA 503 REGULATION (40 CFR Part 503)

  Class B biosolids:
  ├── Meet fecal coliform density <2×10⁶ MPN/g TS (or equivalent)
  ├── Can be land applied with site restrictions (buffer zones,
  │   grazing restrictions, harvest waiting periods)
  └── Most commonly produced biosolids

  Class A biosolids:
  ├── Pathogen reduction to below detection for Salmonella, enteric viruses,
  │   helminth ova — equivalent to compost
  ├── Land application with fewer restrictions
  └── Achieved via: thermophilic digestion, composting, pasteurization

  Land application provides: organic matter, macronutrients (N, P, K),
  micronutrients. Track: heavy metals (Pb, Cd, Hg, Mo, Se, Zn, Cu, Ni)
  must be below 503 cumulative loading rates.
  Emerging issue: PFAS in biosolids from industrial/AFFF sources —
  EPA developing limits; some states already restricting.
```

---

## Water Reuse

Treated wastewater as a deliberate water supply source — closing the loop.

```
  WATER REUSE SPECTRUM

  Level of Treatment Required:

  Secondary  →  Non-potable  →  Indirect Potable  →  Direct Potable
  (WWTP       reuse              Reuse (IPR)           Reuse (DPR)
  effluent)   (irrigation,
              industrial)

  Non-potable: Title 22 (California, widely adopted) — secondary +
               filtration + disinfection; UV 10 mJ/cm²; TC <2.2/100 mL

  IPR: Advanced treatment (MF/UF + RO + UV/AOP or O₃/BAC), then
       environmental buffer (groundwater injection or reservoir augmentation)
       Required log removal/inactivation:
       Giardia: 12 log; Crypto: 10 log; Virus: 12 log (CA DDW)
       Examples: Orange County Water District (GWRS), Singapore NEWater

  DPR: Same advanced treatment but directly injected into potable supply
       without environmental buffer; emerging in Texas (Big Spring), CA
       Requires robust monitoring (online TOC, conductivity, pathogens)
       and public acceptance programs
```

---

## NPDES Permits

Every WWTP discharge to surface water requires an NPDES permit.

```
  NPDES PERMIT STRUCTURE

  ├── Technology-based limits:
  │   BPT (best practicable technology) — secondary treatment = 30 mg/L BOD,
  │   30 mg/L TSS (30-day average); equivalent to activated sludge performance
  │   BCT, BAT for toxics and industrial categories
  │
  ├── Water quality-based limits (WQBEL):
  │   If technology-based limits are not protective of receiving water,
  │   water quality standards drive stricter limits (nutrient limits,
  │   priority pollutants, toxics)
  │
  ├── Effluent monitoring: flow, BOD, TSS, pH, DO, nutrients, pathogens,
  │   toxics as required by permit; CEMS optional but increasing
  │
  └── Permit cycle: 5-year permit renewal; public notice and comment
```

---

## Decision Cheat Sheet

| Design Question | Answer |
|----------------|--------|
| Primary purpose of secondary treatment | Reduce dissolved BOD via biological oxidation — activated sludge is the standard approach |
| Key design variable for effluent quality | SRT controls effluent BOD and whether nitrification occurs; longer SRT = better quality |
| Need to achieve <10 mg/L TN in effluent | BNR required — A²/O or Bardenpho; also need adequate SRT for nitrification (>10 days) |
| Phosphorus limit in permit (<1 mg/L TP) | EBPR first; chemical backup (alum) for reliability; tertiary sand filter or membrane polishing |
| Plant wants to minimize energy cost | Optimize aeration (DO control, fine bubble diffusers, demand-based DO setpoint); biogas CHP recovery |
| Wastewater reuse for landscape irrigation | Secondary treatment + filtration + disinfection (Title 22 equivalent) |
| Site constrained — can't expand footprint | MBR eliminates secondary clarifier; MBBR retrofit increases capacity in existing aeration tanks |
| Biosolids cannot be land applied (PFAS) | Dewatering + thermal drying + incineration or co-combustion at permitted facility |

---

## Common Confusion Points

**BOD vs. COD**: BOD₅ only measures biodegradable organic matter that oxidizes in 5 days
(~65–70% of ultimate BOD for domestic sewage). COD measures all oxidizable carbon, including
refractory compounds. High COD:BOD ratio (>2.5) indicates poorly biodegradable waste —
needs pretreatment or longer SRT. NPDES permits usually specify BOD₅ limits.

**SRT vs. HRT**: These are independent design variables. SRT controls biology (effluent
quality, nitrification). HRT controls the physical tank volume. An MBR can operate at
very short HRT with very long SRT simultaneously — this is its key advantage.

**RAS vs. WAS**: Return activated sludge (RAS) goes back to the aeration basin to maintain
MLSS. Waste activated sludge (WAS) is the biomass removed to maintain SRT. Operators control
SRT by adjusting WAS rate — if too little is wasted, MLSS climbs and SRT extends; if too
much is wasted, SRT drops and effluent quality degrades.

**Nitrification washout**: If SRT drops below the minimum needed for nitrifiers (>8–12 days
at 20°C, longer at lower temperatures), nitrifiers wash out and ammonia spikes in the
effluent. This is an operational failure mode — once washout occurs, re-seeding takes weeks.

**Anaerobic digestion pH sensitivity**: Methanogens are highly sensitive to pH (<6.5 → failure).
Acid accumulation from acidogenesis can crash the digester if organic loading exceeds
methanogenic capacity. VFA/alkalinity ratio monitoring is the early warning — target <0.25.
