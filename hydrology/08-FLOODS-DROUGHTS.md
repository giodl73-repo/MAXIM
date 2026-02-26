# Floods and Droughts — Flood Frequency Analysis, Return Periods, Drought Indices (PDSI/SPI), Early Warning

## The Big Picture

```
+===========================================================================+
|                  EXTREMES OF THE WATER CYCLE                               |
|         Flood = too much water too fast; Drought = too little too long    |
+===========================================================================+
|                                                                           |
|  FLOOD                                  DROUGHT                          |
|  ──────────────────────                 ────────────────────              |
|  Excess water beyond capacity           Deficit of precipitation          |
|  Fast-onset (hours–days)                Slow-onset (weeks–months)         |
|  Visible, sudden                        Invisible, gradual                |
|  Fatalities: direct (drowning)          Fatalities: indirect (food)       |
|  Property damage dominant              Economic damage cumulative         |
|  Caused by: heavy rain, snowmelt,       Caused by: low precipitation,     |
|  dam break, storm surge                 high temperature/ET, poor mgmt    |
|                                                                           |
|  COMMON THREAD: both are statistical distributions                        |
|  Return period is a probabilistic concept, not a prediction of timing     |
+===========================================================================+
```

---

## Flood Frequency Analysis

### Statistical Foundation

```
ANNUAL MAXIMUM SERIES (AMS):
  Record maximum discharge for each year → n-year dataset
  Assume: each annual maximum is an independent sample from a stationary distribution
  Fit a probability distribution → estimate return periods for unobserved events

PARTIAL DURATION SERIES (PDS) / PEAKS OVER THRESHOLD (POT):
  Include all peaks above a threshold (not just annual maxima)
  Better for: shorter records, high-frequency events (< 10-yr)
  AMS 2-yr event ≈ PDS 1.16-yr event (correction factor for high-frequency range)

KEY DISTRIBUTIONS FOR FLOOD FREQUENCY:
  Log-Pearson Type III (LP3):    US standard (Bulletin 17C, USGS)
    log(Q) follows Pearson Type III distribution
    Parameters: mean, variance, skewness of log-transformed flows
    Skewness: weighted average of station + regional skewness (GEV regions)

  Generalized Extreme Value (GEV):
    Family includes Gumbel (ξ=0), Fréchet (ξ>0), Weibull (ξ<0)
    European standard; fits with L-moments (more robust than ML for small samples)
    ξ (shape parameter) controls tail behavior: ξ > 0 → heavy tail (more extreme events)

  Gumbel (Extreme Value Type I):
    P(X ≤ x) = exp(-exp(-(x-μ)/β))
    Good for: flood maxima with moderate skewness
    Theoretical basis: asymptotic extreme value distribution

  Log-normal:
    Simpler; often adequate for moderate-skew flood data

METHOD OF FITTING:
  Method of moments (MOM): match distribution moments to sample moments
  Maximum likelihood (ML): maximize likelihood of observed data
  L-moments: linear combinations of order statistics; more robust for small n
```

### Return Period and Exceedance Probability

```
RETURN PERIOD T vs. EXCEEDANCE PROBABILITY p:
  T = 1/p   (T in years, p = annual exceedance probability)

  100-year flood: p = 0.01 = 1% per year
  50-year flood:  p = 0.02 = 2% per year
  10-year flood:  p = 0.10 = 10% per year

  PROBABILITY OF OCCURRENCE IN N YEARS:
    P(≥1 occurrence in N yr) = 1 - (1-p)^N = 1 - (1 - 1/T)^N

    100-yr flood in 100 years: P = 1 - (0.99)^100 = 0.634 (63.4%)
    100-yr flood in 30 years:  P = 1 - (0.99)^30  = 0.260 (26%)
    100-yr flood in 500 years: P = 1 - (0.99)^500 = 0.993 (99.3%)

  PRACTICAL INTERPRETATION:
    "100-year event" does NOT mean:
      × "Occurs exactly once per century"
      × "Safe for 100 years after it occurs"
      × "The largest possible event"
    It MEANS: 1% probability of being equaled or exceeded in any given year.

    Two 100-year floods can occur in consecutive years.
    100-year flood can occur in year 1 of a 100-year record.
    100-year flood designation is about probability, not schedule.

PLOTTING POSITIONS (empirical frequency):
  For n data points ranked in ascending order (rank m):
  Weibull:       P(X ≤ x_m) = m/(n+1)        (simple, no bias for median)
  Hazen:         P = (m-0.5)/n                (unbiased for range of distributions)
  Blom:          P = (m-0.375)/(n+0.25)       (approximately unbiased for normal)
  Gringorten:    P = (m-0.44)/(n+0.12)        (appropriate for Gumbel)

  Plot on probability paper (Gumbel, log-normal, etc.) → fit line → extrapolate to T
```

---

## Flood Frequency Under Non-Stationarity

```
STATIONARITY ASSUMPTION:
  Traditional frequency analysis assumes: statistics (mean, variance) don't change over time
  "Stationarity is dead" (Milly et al., 2008, Science): climate change violates assumption

  NON-STATIONARITY SOURCES:
    Climate change: shifting precipitation intensity, temperature, snowmelt timing
    Land use change: urbanization, deforestation → altered runoff
    River engineering: channelization, levees, dam operations
    Long-term variability: PDO, AMO cycles overlay 30–60 yr trends

  APPROACHES TO NON-STATIONARY FREQUENCY ANALYSIS:
    Time-varying distributions: parameters μ(t), σ(t) as function of time or covariates
    Covariate models: P(X > x) = f(climate index, land use, T_global)
    Ensemble approaches: use climate model projections to shift distribution forward
    Expected annual damage (EAD): integrate damage × probability over shifted distribution

  PRACTICAL IMPACT:
    A structure designed for 100-yr return period in 1970
    May now be providing only 50-yr protection (due to increased precipitation)
    Future design should account for ~20–40% increase in extreme precipitation
    in many regions (thermodynamic scaling: ~7% increase per °C of warming)
```

---

## Flood Types and Processes

```
FLASH FLOODS:
  Short duration, high intensity rainfall → rapid runoff in small steep basins
  Time to peak: minutes to hours
  Warning time: very short (impossible to forecast >1–2 hr in advance in many cases)
  Most deadly flood type worldwide (~60% of flood fatalities)
  Classic example: Johnstown Flood (1889), Big Thompson Canyon (1976)

RIVERINE FLOODS:
  Large river, large watershed, slower response
  Time to peak: hours to days
  Warning time: days to weeks (adequate for evacuation)
  Mississippi 1993, Missouri 2011: weeks of flooding
  Driven by: long-duration storm systems, saturated antecedent conditions, snowmelt

SNOWMELT FLOODS:
  Rapid spring warmth → fast snowmelt → saturated soils (still frozen) → flood
  "Freshet": annual spring snowmelt flood in Northern rivers
  Rain-on-snow events: double trouble — rain + melt simultaneously
  Example: Red River of the North floods (Fargo-Moorhead): annual spring event

COASTAL/STORM SURGE FLOODS:
  See oceanography/10-SEA-LEVEL-CLIMATE.md
  Compound: tidal + surge + wave + riverine all simultaneous

ICE JAM FLOODS:
  River ice breaks up in spring → transported downstream → jams at constrictive sections
  → Rapid backwater rise upstream of jam
  → Also: sudden release when jam breaks → flood wave downstream
  Common: Yukon, Mackenzie, Amur, Siberian rivers
  Extremely difficult to predict and manage
```

---

## Design Storm and Design Flood

```
DESIGN EVENT SELECTION:
  Regulatory/infrastructure standard → target return period
  Consequences of failure → risk tolerance

  US REGULATORY STANDARDS:
    Urban drainage (minor system): 2–10 yr
    Urban drainage (major system): 25–100 yr
    Stormwater detention: pre/post-development 2-yr and 10-yr peaks
    FEMA regulatory floodplain: 100-yr (1% AEP)
    NFIP mandatory insurance: 100-yr floodplain
    Critical facilities (hospitals, emergency response): 500-yr
    Dams (high-hazard): PMF (Probable Maximum Flood)

DESIGN STORM METHODS:
  IDF-based (single storm): rational method or SCS 24-hr storm
  Historical event: use actual storm as design event (common for calibration)
  Continuous simulation: run continuous long-term simulation → extract design conditions

  INDEX FLOOD METHOD (regional):
    Flood quantile at ungauged site = index flood × dimensionless growth curve
    Index flood = median or mean annual flood from regression
    Q_T = Q_2 × f(T, region)
    Used when no gauge data available
```

---

## Drought Concepts and Types

```
DROUGHT TAXONOMY:
  Meteorological drought: precipitation deficit (2+ months below normal)
  Hydrological drought: streamflow and groundwater below normal
    Lags meteorological drought by weeks to months
  Agricultural drought: soil moisture deficit affecting crop growth
    Most sensitive to short-duration events during critical growth periods
  Socioeconomic drought: supply-demand balance disrupted
    Depends on water management as much as hydrology

DROUGHT CASCADES:
  Rainfall deficit
       ↓ (1–4 weeks)
  Reduced soil moisture → agricultural drought
       ↓ (1–3 months)
  Reduced streamflow → hydrological drought
       ↓ (3–12 months)
  Reduced reservoir storage and groundwater
       ↓ (months–years)
  Water supply shortage → socioeconomic drought

  RECOVERY ALSO FOLLOWS THIS SEQUENCE:
  Normal rain returns → soil moisture recovers first
  Streamflow recovers more slowly
  Groundwater slowest (months–years for deep aquifers)
```

---

## Drought Indices

### Palmer Drought Severity Index (PDSI)

```
PDSI (Palmer, 1965):
  Physically-based moisture accounting model
  Inputs: precipitation, temperature (for PET calculation), soil water capacity
  Core: water balance model tracking:
    AWC (available water capacity) = two soil layers
    Recharge, Runoff, Loss (ET), Potential values of each component

  PDSI CALCULATION:
    d = P - P_hat
    where P = actual precipitation, P_hat = "climatically appropriate precipitation"
    (computed from prior moisture conditions + seasonal averages)

    X_t = 0.897 X_{t-1} + (1/3) Z_t
    Z_t = K × d  (Z-index, monthly anomaly)
    K = climate characteristic factor (normalizes for regional seasonality)

    PDSI CATEGORIES:
    > +4.0:  Extremely wet
    +3 to +4: Very wet
    +2 to +3: Moderately wet
    -1 to +1: Near normal
    -2 to -3: Moderate drought
    -3 to -4: Severe drought
    < -4.0:  Extreme drought

  STRENGTHS: physically based, long historical record (US back to 1895), widely used
  WEAKNESSES:
    Monthly timestep (misses sub-monthly variability)
    Original PET from Thornthwaite (temperature-based only) → underestimates PET under warming
    sc-PDSI (self-calibrating): removes some regional calibration inconsistencies
    PDSI only covers US; Palmer never published full methodology → DIFFICULT to reproduce exactly
```

### Standardized Precipitation Index (SPI)

```
SPI (McKee et al., 1993):
  Simpler than PDSI — PRECIPITATION ONLY (no temperature or soil moisture)
  Works at any timescale: 1, 3, 6, 12, 24, 48 months

  CALCULATION:
    1. Fit gamma distribution to long-term precipitation record (30+ years)
       for a given month and accumulation period
    2. Transform to standard normal distribution
    3. SPI = standard normal deviate

    SPI = (x - μ_x) / σ_x  (approximately, after transformation)

  SPI VALUES:
    > +2.0: Extremely wet
    +1.5 to +2.0: Very wet
    -1.0 to +1.0: Near normal
    -1.5 to -2.0: Severely dry
    < -2.0: Extremely dry

  SPI-1: reflects monthly precipitation → rapid onset/end, agricultural drought
  SPI-3: 3-month: soil moisture drought, spring streamflow
  SPI-6: 6-month: medium-term, streamflow, reservoir storage
  SPI-12: annual: groundwater, large reservoirs
  SPI-24: 2-year: major aquifer response

  STANDARDIZED PRECIPITATION-EVAPOTRANSPIRATION INDEX (SPEI):
    Same as SPI but using P - PET (climatic water balance instead of P alone)
    Better under warming (temperature-driven PET increases → drought intensification)
    UN WMO recommends SPEI for climate change contexts
```

### Other Drought Indices

```
STREAMFLOW DROUGHT:
  Streamflow percentile below Q10 (10th percentile) = drought threshold
  Standardized Streamflow Index (SSI): analogous to SPI for streamflow
  7Q10: 7-day low flow with 10-year return period (used for water quality permitting)

GROUNDWATER DROUGHT:
  Groundwater level below seasonally adjusted threshold
  Standardized Groundwater Index (SGI): distribution-fit to monthly groundwater levels
  Responds slowest — can persist 1–2 years after precipitation recovery

USDM (US DROUGHT MONITOR):
  Weekly national synthesis of drought conditions (USDA, NOAA, NDMC)
  D0–D4 scale: Abnormally Dry through Exceptional Drought
  Combines: SPI, PDSI, soil moisture, streamflow, groundwater, crop conditions
  Expert judgment used alongside automated indices
  USDM drives federal drought declarations → $billions in assistance
```

---

## Compound Events

```
COMPOUND EVENTS (concurrent or sequential extremes):
  Flood + drought: Mediterranean drought → desiccated soil → subsequent flash flood
    (dry hard crust → high runoff even from moderate rain)
  Heatwave + drought: elevated temperature → more ET → drought intensification
  Storm surge + river flood: coastal flooding from both ocean and upstream simultaneously
  Wildfire + flood: fire destroys vegetation → increased runoff, debris flows in next rain season

CALIFORNIA COMPOUND SEQUENCE:
  2017: extreme drought → wildfire season
  2017–18: Thomas Fire → 2018 Montecito debris flow (21 deaths)
  Wildfire removes soil-binding vegetation → bare hydrophobic soil → debris flows
  This sequence is a 21st century climate compound event archetype

STATISTICAL APPROACH:
  Joint probability: P(A ∩ B) = P(A) × P(B) if independent
  But: floods and droughts are often correlated
  Copula functions: model joint distribution of two variables with non-Gaussian dependence
    Archimedean copulas (Clayton, Gumbel, Frank): common in hydrology
    Allows: P(flood > x AND surge > y) correctly accounting for correlation
```

---

## Early Warning Systems

```
FLOOD EARLY WARNING SYSTEM (EWS) COMPONENTS:

1. MONITORING:
   Dense rain gauge + stream gauge networks (telemetry → real-time)
   Radar QPE (quantitative precipitation estimation): 5–15 min update
   Satellite: PERSIANN, IMERG for remote/ungauged areas

2. HYDROLOGICAL FORECASTING:
   Rainfall-runoff model: NWS RDHM (Research Distributed Hydrologic Model)
   European: GloFAS (Global Flood Awareness System, Copernicus/ECMWF)
   Ensemble forecasting: 50 ensembles of NWP input → flood probability forecast

   FORECAST LEAD TIMES:
     Flash flood: 0–6 hr (model-based), potentially 0–1 hr (observed-based)
     Riverine flood: 1–7 days for large rivers
     Seasonal: 1–3 months (for planning, not direct action)

3. THRESHOLD DETERMINATION:
   Flood guidance: compare forecast flow with bankfull/threshold flow at locations
   NWS action/flood/major flood stages at each gauge
   Impact-based thresholds: tie stages to specific impacts (road flooding, structure damage)

4. DISSEMINATION:
   NWS products: watches (conditions favorable), warnings (imminent/occurring)
   WEA (Wireless Emergency Alerts): Flash flood warnings to mobile phones
   Social media: supplementary distribution
   Community-based: local networks for rural/developing-world gaps

DROUGHT EARLY WARNING:
  USDM weekly monitoring
  ENSO forecasts: El Niño → drought in SE US, E. Africa; La Niña → wet in SE US
  Seasonal outlooks: CPC 90-day precipitation/temperature outlooks
  Groundwater level monitoring: lag indicator for recovery
  Reservoir storage levels: operational indicator
  Agricultural indicators: normalized difference vegetation index (NDVI) from satellites
```

---

<!-- @editor[bridge/P2]: No bridge section — extreme value theory (GEV) is the tail-distribution counterpart to CLT; L-moments are robust alternatives to ML estimation; copulas model non-Gaussian joint distributions; SPI is a z-score transform — all concepts the MIT-trained learner owns but may not recognize in hydrological clothing without an explicit bridge -->

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is a 100-year flood? | 1% annual exceedance probability; 63% chance of occurring in any 100-year period |
| What distribution is US standard for flood frequency? | Log-Pearson Type III (LP3) per USGS Bulletin 17C |
| Why is stationarity "dead"? | Climate change and land use alter statistical properties of floods over time |
| What is the PDSI? | Monthly water balance model; calibrated to regional mean; -4 = extreme drought, +4 = extremely wet |
| What is SPI-12? | Standardized Precipitation Index at 12-month accumulation; tracks groundwater/reservoir drought |
| Why use SPI over PDSI? | SPI is simpler, more transparent, works at multiple timescales, comparable across regions |
| What is SPEI vs SPI? | SPEI uses P - PET instead of just P; accounts for temperature-driven evaporation |
| What is a compound event? | Multiple extreme events occurring concurrently or sequentially, often with amplified impacts |

---

## Common Confusion Points

**"100-year flood" is not a 100-year guarantee**: After a 100-year flood occurs, the probability next year is still 1%. The events are statistically independent. A flood of that magnitude can happen in consecutive years or skip 200 years. The return period reflects long-run frequency, not intervals.

**PDSI does not compare across regions without calibration**: The original PDSI uses fixed calibration values that reflect US climate patterns. A PDSI of -3 in Arizona vs. -3 in Georgia does not mean the same severity of impact because the baseline climate differs. The self-calibrating PDSI (sc-PDSI) addresses this by using regional median values.

**Drought is not absence of rain**: Drought is defined relative to expected conditions for the region and season. 50 mm of rain in January in the UK is normal; 50 mm in the Australian Outback in July is extremely wet. An index compares observed conditions to historical baseline — drought = anomaly below normal, not absolute dryness.

**The design flood is not the worst possible flood**: PMF (Probable Maximum Flood) is the theoretical maximum, not the "worst possible." PMF is derived from PMP (Probable Maximum Precipitation) × runoff factors — the theoretical upper bound given atmospheric physics. Actual floods exceeding PMF have been recorded in locations where PMP was poorly estimated. Treat PMF as a very high upper bound, not an absolute ceiling.

**Flash flood vs. dam break flood**: Flash floods from rainfall are stochastic; dam break floods are determined by dam geometry, failure mode, and downstream topography. Dam break floods (HEC-RAS dambreak modeling) generate very steep, fast-moving flood waves — often worse than natural flash floods for downstream communities near the dam. Dam safety regulations are stricter precisely because failure is catastrophic.
