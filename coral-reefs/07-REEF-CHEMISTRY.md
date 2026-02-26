# Reef Chemistry: Aragonite Saturation, Ocean Acidification, CO₂ Equilibria

## The Big Picture

Ocean acidification is the second great chemical threat to coral reefs (after thermal bleaching). It operates through a different mechanism — not heat but dissolution chemistry — and on a longer timescale. Understanding it requires the CO₂ equilibrium system: a set of coupled reactions that determine whether calcium carbonate precipitates or dissolves, and whether corals can build their skeletons at all.

```
CO₂ ABSORPTION AND CARBONATE CHEMISTRY CASCADE
================================================

Atmosphere CO₂ (now ~420 ppm; pre-industrial ~280 ppm)
      |
      | CO₂ dissolves in seawater
      v
  CO₂(aq)  +  H₂O  ⇌  H₂CO₃  (carbonic acid)
                              |
                              | fast dissociation
                              v
                    H₂CO₃  ⇌  H⁺  +  HCO₃⁻  (bicarbonate)
                                            |
                                            | second dissociation (slower)
                                            v
                                  HCO₃⁻  ⇌  H⁺  +  CO₃²⁻  (carbonate)

NET EFFECT of adding CO₂:
  + CO₂ dissolved
  + H⁺ produced (pH drops = acidification)
  - CO₃²⁻ consumed (carbonate ion decreases)

For coral calcification: Ca²⁺ + CO₃²⁻ → CaCO₃ (aragonite)
   ↑
   If CO₃²⁻ drops, this reaction slows or reverses
```

---

## The Carbonate System — Quantitative

```
SEAWATER CARBONATE CHEMISTRY
==============================

The system has 6 variables; measuring any 2 determines the rest:
  Total alkalinity (TA)
  Dissolved inorganic carbon (DIC)
  pH
  pCO₂ (partial pressure CO₂)
  [HCO₃⁻]
  [CO₃²⁻]

Typical pre-industrial surface ocean:
  pH:         8.20
  pCO₂:       280 μatm
  [HCO₃⁻]:   1,800 μmol/kg
  [CO₃²⁻]:   280 μmol/kg
  Ωarag:      ~3.0

Current surface ocean (2020s):
  pH:         8.08 (−0.12 units = 32% more acidic in [H⁺] terms)
  pCO₂:       ~410 μatm
  [HCO₃⁻]:   1,920 μmol/kg (higher — HCO₃⁻ is the dominant form)
  [CO₃²⁻]:   210 μmol/kg (−25% from pre-industrial)
  Ωarag:      ~2.5

Note: pH is logarithmic. -0.12 pH units = 32% increase in [H⁺]
      This is misleadingly understated in public discourse
```

---

## Aragonite Saturation State (Ωarag)

The key metric for coral calcification risk:

```
ARAGONITE SATURATION STATE
============================

Ωarag = [Ca²⁺] × [CO₃²⁻] / Ksp(aragonite)

Where Ksp(aragonite) is the solubility product of aragonite
at a given temperature, salinity, and pressure

INTERPRETATION:
  Ωarag > 1.0:  Seawater supersaturated with aragonite
                CaCO₃ tends to precipitate spontaneously
  Ωarag = 1.0:  Saturation — equilibrium; no net dissolution or precipitation
  Ωarag < 1.0:  Seawater undersaturated — aragonite dissolves

For coral reef building:
  Ωarag > ~3.0: Historical typical surface tropics; vigorous calcification
  Ωarag 2–3:    Reduced calcification rates; still net accretion
  Ωarag 1.5–2:  Significant calcification impairment; net erosion risk
  Ωarag < 1.5:  Severe impairment; dissolution exceeds accretion on many reefs
  Ωarag < 1.0:  Aragonite dissolves — no functional reef possible

CURRENT STATE:
  Global mean surface Ωarag ~2.5 (from ~3.0 pre-industrial)
  Projected at 2×CO₂ (~550 ppm): Ωarag ~1.5–2.0
  Projected at 3×CO₂ (~800 ppm): Ωarag ~1.0–1.5
```

---

## Calcification Rate vs. pH — Experimental Evidence

```
CALCIFICATION RESPONSE TO pH
==============================

Lab experiments (various coral species):
  pH 8.2 (pre-industrial): 100% baseline calcification
  pH 8.1 (current):         80–90% of baseline (estimated)
  pH 7.9 (2×CO₂):           ~50–70% of baseline
  pH 7.7 (extreme):          ~10–30% of baseline

Field observation (natural CO₂ vents, Papua New Guinea):
  Natural CO₂ seeps create pH gradient (8.1 → 7.8)
  At pH 7.8: coral community shifts to Massive Porites only
             (Branching Acropora absent; fewer species; less structural complexity)
  At pH 7.7: Only coralline algae and encrusting; no framework corals

CAVEATS:
  - Corals can UP-REGULATE internal pH at calcification site
  - Some species more tolerant than others (Porites > Acropora under acidification)
  - Short-term lab experiments may overestimate long-term effects
  - But: energy cost of pH up-regulation = less energy for growth
  - "Skeletal quality" also degrades under acidification (porous, weaker skeleton)
```

---

## Diurnal and Spatial pH Variation on Reefs

```
pH VARIATION ON A REEF — DIEL CYCLE
=====================================

DAYTIME:
  Zooxanthellae photosynthesis consumes CO₂
  → [CO₂] drops in reef water
  → Carbonate chemistry shifts → pH RISES (may reach 8.4–8.5)
  → Ωarag increases → enhanced calcification environment

NIGHTTIME:
  Coral + algal respiration releases CO₂
  → [CO₂] increases in reef water
  → pH DROPS (may reach 7.9–8.0)
  → Ωarag decreases → calcification-limiting conditions

SPATIAL:
  Enclosed lagoon:
    Daytime high pH (accumulated photosynthesis)
    Nighttime low pH
    Larger swings than open ocean

  Open fore-reef:
    Water exchange with open ocean buffers diel swings
    pH closer to open ocean mean

NET EFFECT:
  Reefs naturally experience pH swings of 0.2–0.4 units daily
  This is within organisms' adaptive range
  PROBLEM: The baseline is shifting downward; the whole range shifts
```

---

## RCP Scenarios and Reef Projections

```
PROJECTION TABLE: OCEAN CHEMISTRY vs. SCENARIO
================================================

Scenario    CO₂ (ppm)  pH (2100)  Ωarag (2100)  Reef Outlook
---------   ---------  ---------  ------------  -----------
RCP 2.6     ~450       ~8.05      ~2.3          Marginal; some reefs viable
(best case) (Paris 2°C)                         with local stress reduction;
                                                  thermotolerant corals
RCP 4.5     ~550       ~7.95      ~1.9          Severely impaired;
(moderate)                                        no functional reef building
                                                  in large areas
RCP 6.0     ~700       ~7.85      ~1.5          Near dissolution threshold
                                                  in many regions;
                                                  carbonate erosion dominant
RCP 8.5     ~900+      ~7.70      ~1.2          Aragonite dissolves globally
(business   (worst case)                          All reef systems in net
 as usual)                                        dissolution; no recovery

Note: RCP 2.6 requires net negative emissions after ~2050
      Current trajectory (2024) tracks between RCP 4.5 and 6.0
```

---

## Calcite vs. Aragonite — Why It Matters

```
CARBONATE MINERAL STABILITY
=============================

ARAGONITE (coral skeleton):
  - Orthorhombic crystal structure
  - More soluble than calcite (dissolves more readily)
  - Ksp = 10⁻⁸·³⁴ at 25°C
  - Reef-building corals use only aragonite
  - First mineral to dissolve as Ωarag drops below 1

CALCITE (some coralline algae, foraminifera, echinoderms):
  - Trigonal/rhombohedral crystal structure
  - Less soluble than aragonite
  - Ksp = 10⁻⁸·⁴⁸ at 25°C
  - High-Mg calcite (used by CCA and echinoderms):
    MOST soluble of all — Mg substitution destabilizes lattice

  Dissolution order as acidification proceeds:
  1. High-Mg calcite (CCA, urchins) → dissolves first
  2. Aragonite (coral skeleton) → second
  3. Low-Mg calcite (most resistant)

  IMPLICATION: CCA (the cement of the reef framework) may be
               more acidification-vulnerable than the corals themselves
```

---

## Local Chemistry Modifications

Humans can locally modify reef chemistry to some degree:

```
LOCAL ALKALINITY ENHANCEMENT
==============================

Concept: Add alkalinity to seawater to increase CO₃²⁻ concentration
         and raise Ωarag locally

Methods proposed:
  1. Electrolysis of seawater → produces NaOH → raises pH/alkalinity
  2. Calcium hydroxide Ca(OH)₂ addition
  3. Olivine (Mg₂SiO₄) dissolution — accelerated mineral weathering
  4. Biochar or limestone powder addition

Scale problem:
  Ocean volume requiring treatment: ~3.6 × 10²⁰ liters
  To meaningfully raise Ωarag by 0.5 units globally:
  Required alkalinity addition: ~1,000 Pg CaCO₃ equivalent
  This is orders of magnitude beyond any plausible deployment

LOCAL application to specific reefs:
  Feasible in enclosed areas (lagoons, nurseries)
  Not a global solution
  Proposed for coral nursery systems to enhance growth rate
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the CO₂-carbonate cascade? | CO₂ → H₂CO₃ → HCO₃⁻ + H⁺ → CO₃²⁻ + H⁺; more CO₂ = less CO₃²⁻ = harder calcification |
| What is Ωarag? | Aragonite saturation state: [Ca²⁺][CO₃²⁻] / Ksp; >1 = supersaturated |
| What Ωarag do reefs need? | Historically >3; functional reefs need >~2; dissolution risk below ~1.5 |
| Current ocean Ωarag? | ~2.5 (down from ~3.0 pre-industrial) |
| Current ocean pH? | ~8.08 (down from ~8.20 pre-industrial; 32% more acidic in [H⁺]) |
| pH change at 2× CO₂? | ~7.95; calcification reduced ~30–50% in many species |
| Which carbonate mineral dissolves first? | High-Mg calcite (CCA), then aragonite (coral), then low-Mg calcite |
| Why does daytime reef pH rise? | Zooxanthellae photosynthesis consumes CO₂ from reef water |
| What is local alkalinity enhancement? | Adding alkalinity (Ca(OH)₂, electrolysis) to raise local Ωarag |
| Is acidification separate from bleaching? | Yes — different mechanism (chemistry vs. temperature); both from CO₂ |

---

## Common Confusion Points

**pH is logarithmic — 0.12 units is not trivial.** A pH change from 8.20 to 8.08 represents a 32% increase in hydrogen ion concentration. If reported as "0.12 pH units" in the press it sounds minor. In a system that has been stable at ~8.2 for hundreds of thousands of years, this is a geologically rapid shift.

**Ocean acidification and bleaching both come from CO₂ but via different pathways.** Bleaching is caused by heat from greenhouse warming (all greenhouse gases + CO₂). Acidification is caused specifically by CO₂ dissolving in ocean water regardless of greenhouse effect. They are not the same problem; they compound each other's effects on reefs.

**Corals can buffer calcification short-term.** Corals use ion pumps to raise the pH at their calcification site well above ambient seawater. This metabolic investment buffers against moderate acidification but costs energy (diverted from growth and reproduction). The calcification rate metric misses this trade-off: a coral maintaining its growth rate under acidification may be paying a hidden metabolic cost.

**Aragonite dissolves faster than calcite, but both dissolve.** The common simplification "acidification dissolves coral skeletons" is accurate for long timescales. On short timescales, the bigger effect is reduced calcification rate (new skeleton forms more slowly) rather than dissolution of existing skeleton. Dissolution dominates at Ωarag < 1.

**CCA vulnerability may be the hidden reef killer.** Coralline algae (CCA) cement the reef framework. High-Mg calcite is more soluble than aragonite under acidification. Losing CCA structural integrity could cause reef framework collapse even on reefs where corals are otherwise intact. This is an understudied and underappreciated acidification risk.
