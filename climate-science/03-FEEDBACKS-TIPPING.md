# Feedbacks & Tipping Points

## Climate Feedbacks, Tipping Elements, Hysteresis, Cascade Risk

## The Big Picture: Feedback Framework

```
CLIMATE FEEDBACK STRUCTURE

  Initial forcing (e.g., CO₂ doubling → +3.7 W/m² → +1.2°C no-feedback)
         ↓
  Feedback loop #1: Water vapor
  More heat → more evaporation → more H₂O in troposphere
  → more infrared absorption → more heat (AMPLIFYING, +)
         ↓
  Feedback loop #2: Ice-albedo
  Warming → ice/snow melts → darker ocean/land exposed
  → more solar absorption → more warming (AMPLIFYING, +)
         ↓
  Feedback loop #3: Planck (mandatory stabilizer)
  More heat → more IR emitted (T⁴) → negative feedback (STABILIZING, -)
         ↓
  Feedback loop #4: Lapse rate
  Warming changes temperature profile with altitude
  → complex: negative in tropics, positive in high latitudes
         ↓
  Feedback loop #5: Clouds
  Do clouds increase or decrease as climate warms?
  → UNCERTAIN SIGN: different cloud types respond differently
         ↓
  NET RESULT: ECS ~ 3°C (per CO₂ doubling)

MATH:
  ECS = ΔF_2×CO₂ / (-λ)  where λ = net feedback parameter
  λ = λ_Planck + λ_WV + λ_LR + λ_albedo + λ_cloud
  λ_Planck ≈ -3.2 W/m²/K  (stabilizing)
  Σ(others) ≈ +1.6 to +2.3 W/m²/K  (amplifying)
  Net λ ≈ -0.8 to -1.5 W/m²/K  → ECS = 2.5–4.6°C
```

---

## Climate Feedbacks — Summary

| Feedback | Sign | Magnitude (W/m²/K) | Confidence | Key uncertainty |
|----------|------|-------------------|------------|-----------------|
| Planck (OLR ∝ T⁴) | − (stabilizing) | −3.2 | Very high | None — fundamental thermodynamics |
| Water vapor | + (amplifying) | +1.5 to +2.0 | High | Upper tropospheric humidity distribution |
| Lapse rate | − (net) | −0.4 | Medium-high | Tropical hot-spot observational evidence |
| Surface albedo (ice) | + (amplifying) | +0.3 to +0.5 | High | Sea ice loss directly observed |
| Cloud (net) | + to − | −0.4 to +0.8 | Low | Low cloud response to warming |

**Net feedback parameter λ ≈ −0.8 to −1.5 W/m²/K → ECS = 3.7/|λ| ≈ 2.5–4.6°C**

---

## The Major Feedbacks

### Planck Response: The Fundamental Stabilizer

```
  PHYSICS:
    Stefan-Boltzmann: OLR ∝ T⁴
    Any warming increases outgoing radiation
    → self-limiting (more energy out as temperature rises)
    ALWAYS negative (stabilizing)
    Well-quantified: -3.2 W/m²/K

  WITHOUT PLANCK RESPONSE:
    Earth would be unstable — any forcing would runaway
    Venus likely had some runaway process early in history
    Planck response is why Earth has been stable for 4 billion years

  TEMPERATURE DEPENDENCE:
    On colder planets: Planck response is weaker (lower T → less OLR
    sensitivity) → warmer planets stabilize faster
    On cooler background: same forcing causes more warming
    This is why early Earth (fainter Sun) was still warm enough for life
    with slightly different atmospheric composition
```

### Water Vapor Feedback: The Strongest Amplifier

```
  MECHANISM:
    Initial warming → surface evaporation increases
    Clausius-Clapeyron equation: saturation vapor pressure rises ~7%/K
    Atmospheric water vapor content rises proportionally
    (atmosphere maintains approximately constant relative humidity)
    More H₂O → stronger greenhouse effect → more warming → more H₂O

    ΔLn(e_sat)/ΔT ≈ 7%/K  (Clausius-Clapeyron)

  FEEDBACK VALUE: +1.5 to +2.0 W/m²/K
    IPCC AR6 best estimate: +1.77 W/m²/K
    Well-constrained (atmospheric thermodynamics is well-understood)

  SPATIAL STRUCTURE:
    Strongest in tropics (warm → large absolute humidity increase)
    Upper troposphere moistening is critical (where CO₂ absorption is)
    "Hot Spot": models predict upper tropospheric warming should be
    amplified in tropics — observational evidence mixed (radiosonde vs satellite)

  WITHOUT WATER VAPOR FEEDBACK:
    ECS would be ~1.2°C (Planck response only)
    Water vapor roughly doubles the equilibrium sensitivity
    This is well-established physics, not controversial
```

### Ice-Albedo Feedback

```
  MECHANISM:
    Initial warming → sea ice and snow cover retreat
    Ice and snow: albedo ~0.85 (reflects 85% of solar)
    Open ocean: albedo ~0.06 (reflects 6% of solar)
    Ocean/land exposed: much more solar absorbed → more warming

  ARCTIC AMPLIFICATION:
    Arctic warming 2-4× global average rate
    Ice-albedo feedback operates maximally at poles
    Summer Arctic sea ice loss since 1979: >40% area reduction
    Arctic sea ice extent in September (minimum): record lows 2012, 2020

  FEEDBACK VALUE: +0.3 to +0.5 W/m²/K
    Smaller than water vapor but well-measured
    Directly observable from satellite

  SEA ICE TIPPING:
    Perennial Arctic sea ice may reach a tipping point
    Ice-free Arctic summers possibly within 10-30 years
    ONCE GONE: self-reinforcing loss; dark ocean retains heat summer
    → difficulty re-freezing in autumn
```

### Lapse Rate Feedback

```
  THE LAPSE RATE:
    Rate of temperature decrease with altitude: ~6.5°C/km (moist)

  TROPICS:
    Convection maintains moist adiabatic lapse rate
    Warming in tropics: upper troposphere warms MORE than surface
    (following moist adiabat: warmer → more H₂O → more latent heat
    release at higher altitudes)
    More upper tropospheric warming → more OLR → NEGATIVE feedback

  HIGH LATITUDES:
    Warming concentrated in lower troposphere (polar amplification)
    Little warming aloft → OLR from cooler levels → POSITIVE feedback

  NET EFFECT: approximately -0.4 W/m²/K globally
    Partially offsets water vapor feedback in tropics
    Combined WV + LR: approximately +1.3 W/m²/K (less than WV alone)
```

### Cloud Feedback: The Primary Uncertainty

```
  WHY CLOUDS ARE DIFFICULT:
    Low clouds (marine stratus/stratocumulus):
      SW cooling effect: -47 W/m² (reflect sunlight)
      LW warming effect: small (low altitude → warm → emit much OLR)
      Net: strong cooling
      QUESTION: Do they increase or decrease with warming?
      Different models answer differently → large ECS spread

    High clouds (cirrus):
      SW effect: modest (thin; transparent to some solar)
      LW warming: +26 W/m² (cold; emit little OLR)
      Net: warming
      QUESTION: Do they rise (maintaining relative temperature) or spread?

  EVIDENCE FROM OBSERVATIONS:
    Sherwood et al. (2020, Nature): atmosphere mixing (convective mixing
    and boundary layer drying) observed from soundings
    → constrains low cloud behavior
    → ECS almost certainly > 2.5°C (eliminates low-sensitivity models)

    CERES satellite (2000-present):
    → Measures TOA radiative fluxes
    → Shows cloud radiative effect in present climate well
    → But doesn't directly measure CHANGE in cloud feedback

  CLOUD FEEDBACK VALUE:
    CMIP6 models: -0.4 to +0.8 W/m²/K (wide range)
    Constrained estimate: 0 to +0.5 W/m²/K (mostly positive)
    THIS uncertainty is why ECS range spans 2.5-4.0°C
```

---

## Carbon Cycle Feedbacks

```
  THE EARTH SYSTEM SENSITIVITY CONCEPT:
    ECS as measured: physical feedbacks only
    Earth System Sensitivity: + carbon cycle feedbacks

  LAND CARBON FEEDBACKS:
    Q₁₀ parameter: sensitivity of soil respiration to temperature
    Typical: Q₁₀ ~ 2 (10°C warming → ~2× soil CO₂ release)
    As planet warms: soil respiration accelerates → more atmospheric CO₂
    → amplifying feedback on top of physical ECS

  TROPICAL FORESTS:
    CO₂ fertilization: higher CO₂ → faster plant growth → carbon sink
    Drought stress: higher temperature + drought → forest mortality → carbon source
    Amazon: ~2-3°C + continued deforestation → may cross tipping point
    Transition: tropical rainforest → savanna/cerrado
    CO₂ release: ~90 GtC from vegetation + soil carbon
    Regional rainfall: reduced evapotranspiration → further drying
    (the "moisture pump" collapses with the forest)

  PERMAFROST FEEDBACK (the sleeping giant):
    ~1,500 GtC frozen in permafrost (more than all atmospheric CO₂)
    As temperatures rise: active layer deepens; taliks (unfrozen zones) grow
    Aerobic conditions: microbial decomposition → CO₂
    Anaerobic (waterlogged): methanogenesis → CH₄ (more potent short-term)
    RATE: slow-onset; decades for deep permafrost to fully thaw
    NOT included in full in most IPCC projections
    → "committed" warming from permafrost even at stabilized temperatures
```

---

## Tipping Points: Theory

### The Bifurcation Framework

Tipping elements are physical systems undergoing saddle-node bifurcations. You know the framework from nonlinear dynamics: as a control parameter (temperature) increases, a stable fixed point and an unstable fixed point approach each other, collide, and annihilate — the system then falls to the only remaining attractor (a qualitatively different state). The hysteresis loop follows directly: the return path lies on a different branch, so restoring the original state requires decreasing the parameter far below the forward tipping threshold. Early warning signals (critical slowing down — recovery from small perturbations becomes exponentially slower as the bifurcation approaches) are in principle detectable from time-series statistics.

```
  DYNAMICAL SYSTEMS CONCEPT:
    Climate components have stable states (attractors)
    As forcing increases: stability changes
    At tipping point: system shifts to new attractor

  BIFURCATION DIAGRAM:
  State
  (e.g., ice coverage)
    │
    │ ─────────────────────────→  (stable ice branch)
    │                   ╲
    │                    ╲  ← tipping point
    │                     ╲
    │                      ───────────────  (ice-free branch)
    │
    └──────────────────────────────────────────────→  Temperature (forcing)

  KEY FEATURES:
    Tipping occurs at a THRESHOLD (not gradual)
    System moves to new state quickly (on geological timescale)
    HYSTERESIS: recovery path is different from forward path
    → to restore original state: must reduce forcing BELOW
       where tipping occurred (lower than where you tipped)
    Some tipping elements: recovery requires forcing many degrees
    LOWER than current — effectively irreversible on human timescales
```

---

| Tipping element | Threshold (°C above pre-industrial) | Timescale to full impact | SLR contribution | Reversibility |
|----------------|--------------------------------------|--------------------------|-----------------|---------------|
| Greenland Ice Sheet (GIS) | ~1.5–2.0 | Centuries–millennia | +7 m | Effectively irreversible |
| West Antarctic Ice Sheet (WAIS) | ~1.5 (possibly crossed) | Centuries–millennia | +3–5 m | Effectively irreversible |
| East Antarctic Ice Sheet (EAIS) | ~3–5 | Millennia | +26 m | Irreversible |
| AMOC collapse | ~1.5–4 (uncertain) | Decades onset; centuries full | +20–30 cm (US East Coast only) | Centuries |
| Amazon dieback | ~2–3 + deforestation | Decades | 0 (SLR); 90 GtC to atm. | Decades–centuries |
| Permafrost (thermokarst) | ~1.5 (initiating) | Decades–centuries | 0 (SLR); adds CO₂/CH₄ | Millennia |
| Boreal forest dieback | ~4 | Decades | 0 (SLR); large CO₂ | Centuries |
| Coral reef system | ~1.5 | Decades | 0 (SLR); ecosystem loss | Unknown |

---

### Greenland Ice Sheet

```
  POTENTIAL TIPPING THRESHOLD: ~1.5-2°C global warming
  (above pre-industrial)

  MECHANISM:
    Greenland ice surface below 2,000 m elevation: melt feedback
    As ice thins, surface moves to lower altitude → warmer air
    → more melt → more thinning → lower altitude → more warming
    Self-reinforcing loss at lower elevations

    Marine ice sheet instability at margins:
    Ice streams flow to ocean; warmer ocean melts floating ice shelves
    Ice shelves buttress glaciers; removal → glaciers accelerate
    MARINE ICE CLIFF INSTABILITY: tall ice cliffs calve rapidly
    (physics-based maximum stable ice cliff height)

  SEA LEVEL:
    Full Greenland deglaciation: +7 m sea level rise
    TIMESCALE: centuries to millennia (not instantaneous)
    COMMITTED: once past threshold, commitment exists even if
               temperatures later reduced

  CURRENT STATUS:
    Greenland net mass loss since 1990s
    Acceleration observed
    Whether overall sheet has crossed threshold: uncertain
    Individual drainage basins may have
```

### West Antarctic Ice Sheet (WAIS)

```
  POTENTIAL TIPPING THRESHOLD: ~1.5°C (possibly already crossed)

  MECHANISM — MARINE ICE SHEET INSTABILITY (MISI):
    West Antarctic rests on bedrock BELOW sea level
    (retrograde bed: slopes downward toward interior)
    Warm ocean water can access under ice shelf
    → melt floating ice → unground grounded ice
    → retrograde bed causes acceleration (deeper water → more melt)
    → irreversible once grounding line retreats past overdeepened bed

  THWAITES GLACIER (the "Doomsday Glacier"):
    Size: Florida; losing mass at accelerating rate
    UK-US "MELT" project (2019-2023): warm water under Thwaites confirmed
    Thwaites alone: +60 cm SLR if fully lost; blocks more ice behind it
    "Eastern ice shelf": shows cracking; could fail within decade
    → Unplug → rapid Thwaites retreat → adjacent glaciers accelerate

  SEA LEVEL:
    WAIS destabilization: +3-5 m sea level (over centuries-millennia)
    Combined with Greenland: +10+ m potential

  CURRENT STATUS:
    Strong evidence MISI process is underway for Thwaites
    Whether full irreversible tipping has been triggered: uncertain
    Committed to substantial retreat regardless of future emissions
```

### AMOC: Atlantic Meridional Overturning Circulation

```
  WHAT IT IS:
    Global thermohaline conveyor belt component
    Warm surface water flows north (Gulf Stream → North Atlantic Drift)
    → Cools, sinks at high latitudes (dense cold saline water)
    → Returns south as deep cold current
    → Resurfaces, warms, repeats

  WHY IT MATTERS:
    Redistributes ~1.3 PW of heat poleward
    Keeps Northern Europe 5-10°C warmer than it "should" be
    Affects ITCZ position → African/Asian monsoons
    Atlantic hurricane activity linked to AMOC state

  TIPPING MECHANISM:
    Freshwater injection (Greenland melt, increased precipitation)
    → Reduces surface water density → disrupts sinking
    → If flux exceeds threshold: AMOC weakens rapidly
    → Could collapse to weak state (bifurcation)

  EVIDENCE:
    AMOC has slowed ~15% since mid-20th century (proxy + direct measures)
    Direct measurements (RAPID array, 2004-): significant variability;
    trend toward weakening
    Boers (2021, Nature): fingerprinting suggests AMOC approaching
    critical transition — debated

  IMPACTS OF COLLAPSE:
    Northern Europe: cooling 5-10°C (partially offsetting global warming)
    US East Coast: sea level rise 20-30 cm additional
    Amazon/Sahel: precipitation pattern shifts
    AMOC has collapsed in past: Younger Dryas (~12,900 years ago)
    — Greenland cooled ~10°C in ~10 years

  THRESHOLD: uncertain; possibly 1.5-4°C
  TIMESCALE: decades for onset; centuries for full response
```

### Amazon Dieback

```
  THRESHOLD: ~2-3°C global warming + continued deforestation

  MECHANISM:
    Amazon rainforest generates its own rainfall
    (evapotranspiration: trees pump water from soil → atmosphere
     → "flying rivers" of water vapor)
    Deforestation → less evapotranspiration → less rainfall → drought
    Drought → tree mortality → less evapotranspiration → more drought
    Fire → rapid conversion from forest to savanna

  CURRENT STATE:
    ~20% of Amazon deforested (threshold estimates: ~20-25%)
    Southern/eastern Amazon already showing "savannification"
    2010, 2015, 2020: severe Amazon droughts; tree mortality spikes
    2023: worst Amazon drought on record

  CARBON RELEASE:
    ~90-100 GtC in Amazon vegetation + soil
    Full dieback = ~90 GtCO₂ equivalent release
    = ~2+ decades of current global emissions

  REGIONAL IMPACTS:
    Water cycle disruption in South America
    Agricultural collapse (Brazil is global food exporter)
    Monsoon shifts affecting Andes ice caps
```

### Permafrost Abrupt Thaw

```
  TWO MECHANISMS:
  1. GRADUAL THAW:
     Active layer deepening each summer
     Slow but predictable; currently modeled in IPCC scenarios

  2. ABRUPT THAW (THERMOKARST):
     Ground subsidence when ice-rich permafrost melts
     → Thermokarst lakes form
     → Lakes concentrate heat → very fast thaw below
     → CH₄ ebullition from anaerobic lake sediments
     → Amplified warming → more thermokarst
     NOT currently in IPCC models at full magnitude

  CARBON RELEASE RATE:
    Abrupt thaw: could release equivalent of additional 30-60 GtCO₂
    over 21st century (comparable to additional decade of emissions)
    NOT yet included in IPCC scenario budgets
    → This is a known underestimation in carbon budget calculations
```

---

## Tipping Cascades

```
  THE CASCADE HYPOTHESIS (Steffen et al. 2018, PNAS):
    Tipping elements are not independent
    Greenland melt → AMOC weakening
    AMOC weakening → Amazon drought → Amazon dieback
    Amazon dieback → more warming → more permafrost thaw
    Permafrost thaw → more warming → more ice loss
    ...

  "HOTHOUSE EARTH" SCENARIO:
    If cascades trigger at ~2°C: Earth may follow self-reinforcing path
    to 4-5°C regardless of further human emissions
    NOT INEVITABLE: uncertainties large; cascade thresholds uncertain
    But: sufficient risk to treat as serious concern for policy

  PRECAUTIONARY PRINCIPLE:
    Tipping point thresholds and cascade dynamics are:
    - Poorly constrained
    - Irreversible if crossed
    - Potentially larger than point-by-point estimates
    → Risk management argument for aggressive emissions reduction
       independent of best-guess ECS

  THE ASYMMETRY:
    If climate sensitivity is low AND tipping points don't cascade:
    → Aggressive mitigation: spent resources on decarbonization (recoverable)
    If climate sensitivity is high AND cascades trigger:
    → Insufficient mitigation: potentially irreversible planetary change
    → Asymmetric payoff favors caution
```

---

## Decision Cheat Sheet

| I want to understand... | Section |
|---|---|
| Why ECS is ~3°C not 1.2°C | Feedback overview + water vapor |
| Why cloud feedback matters | Cloud feedback section |
| Arctic sea ice loss physics | Ice-albedo feedback |
| Why AMOC collapse would cool Europe | AMOC section |
| Permafrost risk to carbon budget | Permafrost tipping section |
| Whether tipping points can cascade | Cascade section |
| Why 1.5°C target matters | Tipping thresholds + cascade risk |

---

## Common Confusion Points

**Tipping points don't mean cliff edges in time**: A "tipping point" in the dynamical systems sense means a threshold of FORCING that triggers a transition — not an instantaneous event. Greenland ice sheet tipping means committing to loss that unfolds over centuries. The "point" refers to where the system crosses into a self-reinforcing mode, not a single catastrophic moment.

**AMOC "collapse" doesn't mean worldwide cooling**: Regional effects dominate — Northern Europe cooler, US East Coast higher sea level, monsoon shifts. It would PARTIALLY offset (not reverse) global warming in Europe, while making conditions worse in many other regions.

**Positive feedback ≠ good feedback**: In systems science, "positive" means amplifying (the feedback reinforces the initial change). "Negative" means stabilizing (feedback opposes the change). Water vapor feedback is "positive" (amplifying) which is bad; Planck response is "negative" (stabilizing) which is stabilizing. Nothing to do with good/bad.

**We don't know exact tipping thresholds**: The ranges given (1.5°C for GIS, etc.) are scientific estimates with substantial uncertainty. Some elements may have already crossed thresholds; others may have higher thresholds than currently estimated. The precautionary logic is about irreversibility, not certainty.
