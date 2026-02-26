# 06 — Mitigation & Geoengineering

## Renewables, Grid Decarbonization, CDR, Solar Radiation Management

---

## The Big Picture: Decarbonization Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MITIGATION + INTERVENTION LANDSCAPE                      │
│                                                                             │
│  MITIGATION (reduce emissions)                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ ENERGY SUPPLY     TRANSPORT       INDUSTRY        LAND USE           │ │
│  │                                                                       │ │
│  │ Solar PV ─────    BEV cars ────   Green steel ─   Deforest. halt─    │ │
│  │ Wind ──────────   E-buses ─────   Green cement ─  Reforestation─     │ │
│  │ Nuclear (firm)─   Rail ────────   Industrial heat─ Soil carbon ─     │ │
│  │ Hydro (existing)  Shipping ────   Green hydrogen─  Agriculture ──    │ │
│  │ Grid storage ──   Aviation ────                                       │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  CARBON DIOXIDE REMOVAL (remove CO₂ from atmosphere)                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ NATURAL                          │  ENGINEERED                     │   │
│  │ Afforestation/Reforestation      │  Direct Air Capture (DAC)       │   │
│  │ Soil carbon sequestration        │  BECCS                          │   │
│  │ Peatland/wetland restoration     │  Enhanced weathering            │   │
│  │ Ocean fertilization (speculative)│  Ocean alkalinization           │   │
│  └─────────────────────────────────┴─────────────────────────────────┘   │
│                                                                             │
│  SOLAR RADIATION MANAGEMENT (reflect sunlight — buys time, does not remove │
│  CO₂, does not address ocean acidification)                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Stratospheric Aerosol Injection (SAI)  │  Marine Cloud Brightening │   │
│  │ Cirrus cloud thinning                  │  Space reflectors (R&D)   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Solar Photovoltaics — Physics and Economics

### The Photoelectric Effect and P-N Junction

```
  PHOTON ABSORPTION:

  Photon (hν) strikes semiconductor (silicon)
         ↓
  If hν ≥ bandgap energy (Eg) → electron promoted from valence to conduction band
  If hν < Eg → photon not absorbed (transparent to that wavelength)
  If hν >> Eg → excess energy dissipated as heat

  Silicon Eg = 1.1 eV → absorbs visible + part of NIR

  P-N JUNCTION:

  p-type (holes) | n-type (electrons)
                 ├── depletion region (built-in electric field)
                 │
  Excited electron → swept by built-in field toward n-side
  Remaining hole  → swept toward p-side
  Net: electron current flows out the n-side contact → external circuit
```

### Shockley-Queisser Limit

Fundamental thermodynamic limit on single-junction solar cell efficiency.

```
  Maximum theoretical efficiency for single-junction = ~33%
  at optimal bandgap ~1.3 eV for AM1.5 solar spectrum

  Why not 100%?
  1. Sub-bandgap photons: not absorbed (~20% of spectrum)
  2. Thermalization loss: photons above bandgap — excess energy → heat (~30%)
  3. Radiative recombination: unavoidable electron-hole recombination
  4. Voltage/fill factor losses

  REAL-WORLD EFFICIENCIES:
  ┌──────────────────────────────────────┬────────────┬──────────────┐
  │ Technology                           │ Commercial │ Lab Record   │
  ├──────────────────────────────────────┼────────────┼──────────────┤
  │ Monocrystalline silicon (PERC/TOPCon)│ 21-23%     │ 26.8% (Si)  │
  │ Polycrystalline silicon              │ 17-19%     │ —            │
  │ Thin film CdTe (First Solar)         │ 18-19%     │ 22.1%        │
  │ CIGS                                 │ 15-17%     │ 23.4%        │
  │ Perovskite (emerging)                │ 20-24%     │ 26.0%        │
  │ GaAs (aerospace, III-V)              │ 28-30%     │ 29.1%        │
  │ Multi-junction III-V (concentrating) │ 35-40%     │ 47.1%        │
  └──────────────────────────────────────┴────────────┴──────────────┘

  Multi-junction exceeds S-Q for single junction by stacking cells with
  different bandgaps: each layer absorbs a different part of the spectrum.
  CPV (concentrating) uses lenses to intensify sunlight on expensive cells.
```

### Cost Decline: The Learning Curve

Wright's Law governs solar PV costs: every doubling of cumulative production yields a roughly constant percentage cost reduction — the same phenomenon as Moore's Law but for manufacturing cost per unit rather than transistor density. Solar's learning rate (~20-25% cost reduction per production doubling) has been stable for four decades, making its cost trajectory one of the most accurately predicted in energy economics. The difference from Moore's Law: solar improvements come from manufacturing scale and process optimization, not from miniaturization hitting physical limits.

```
  Solar PV module cost:

  2010: ~$2.00/Wp (watts-peak)
  2015: ~$0.60/Wp
  2020: ~$0.25/Wp
  2023: ~$0.15-0.18/Wp (utility scale)

  ~88% cost reduction in 13 years

  Wright's Law (learning curve): every doubling of cumulative production
  → ~20-25% cost reduction (solar historical learning rate)

  LCOE (Levelized Cost of Electricity):
  2010: $350/MWh (utility scale solar)
  2023: $30-50/MWh (sunniest regions), $50-80/MWh (moderate insolation)

  Comparison:
  New coal: $65-150/MWh
  New natural gas (CCGT): $45-80/MWh
  New nuclear: $80-150/MWh (developed economies)

  Solar is now cheapest electricity source in history in most regions.
  The remaining challenge is integration, not generation cost.
```

---

## 2. Wind Energy — Physics and Economics

### Betz Limit

```
  FUNDAMENTAL PHYSICS: why can't we extract 100% of wind energy?

  If wind completely stopped at turbine → no airflow through turbine at all
  → no energy extraction (zero flow rate = zero power)

  Trade-off: must allow air to continue flowing (downwind air must move
  faster than if turbine removed all energy)

  BETZ (1919): theoretical maximum = 16/27 = 59.3% of wind kinetic energy

  Wind power equation:
  P = ½ × ρ × A × v³ × Cp

  Where:
  ρ = air density (1.225 kg/m³ at sea level, 15°C)
  A = rotor swept area (πr²) — why bigger rotors matter
  v³ = wind speed cubed — why high-wind sites are SO much better
  Cp = power coefficient (max 0.59, real turbines 0.35-0.50)

  v³ rule: doubling wind speed → 8× power potential
  A rule: doubling rotor diameter → 4× swept area → 4× power

  This is why offshore wind is valuable: higher, more consistent wind speeds
```

### Capacity Factor and Grid Integration

```
  Capacity factor = actual energy produced / nameplate capacity × 100%

  Onshore wind:   30-40% (site-dependent; 35% typical)
  Offshore wind:  40-55% (45% typical; some sites >55%)
  Solar PV:       15-30% (15% UK, 25% US Southwest, 30% desert regions)
  Nuclear:        90-95% (runs continuously)
  Natural gas:    40-55% (flexible)

  Implication: 1 GW offshore wind ≠ 1 GW nuclear
  1 GW offshore (45% CF) = 0.45 GW average
  1 GW nuclear (92% CF) = 0.92 GW average
  → Need ~2× nameplate capacity of offshore to match nuclear average output

  VARIABILITY CHALLENGE:

  Wind and solar output varies on:
  - Seconds/minutes (turbulence)     → grid frequency response
  - Hours/days (weather systems)     → storage or backup required
  - Seasons (UK: peak wind winter,   → seasonal storage challenge
             peak solar summer)

  Integration solutions (portfolio approach):
  ┌───────────────┬──────────────────────────────────────────────┐
  │ Solution      │ Role                                         │
  ├───────────────┼──────────────────────────────────────────────┤
  │ Transmission  │ Geographic diversity — calm in one region,  │
  │ (HVDC links)  │ windy in another; smooths aggregate output  │
  ├───────────────┼──────────────────────────────────────────────┤
  │ Storage       │ Time-shift surplus → cover deficit          │
  │ (batteries,   │ Batteries: hours; pumped hydro: days;       │
  │ pumped hydro) │ hydrogen: seasonal                          │
  ├───────────────┼──────────────────────────────────────────────┤
  │ Demand        │ Move flexible loads to times of surplus     │
  │ response      │ (EV charging, industrial processes)         │
  ├───────────────┼──────────────────────────────────────────────┤
  │ Firm power    │ Nuclear, hydro, gas + CCS as backup         │
  │ (dispatchable)│ "when the wind doesn't blow, sun doesn't   │
  │               │ shine" — firm capacity required for         │
  │               │ reliability                                 │
  └───────────────┴──────────────────────────────────────────────┘
```

---

## 3. Grid Decarbonization

### Energy Storage Technologies

```
  ┌───────────────────────────────────────────────────────────────────────┐
  │ STORAGE TECHNOLOGY COMPARISON                                         │
  ├────────────────────┬──────────────┬──────────────┬───────────────────┤
  │ Technology         │ Scale        │ Duration     │ Best Use          │
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Li-ion (LFP/NMC)  │ kWh-GWh      │ 2-8 hours    │ Daily cycling,    │
  │                    │              │              │ frequency response │
  │                    │              │              │ Declining cost:   │
  │                    │              │              │ ~$150/kWh (2023)  │
  │                    │              │              │ vs $1,200/kWh(2010│
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Pumped hydro       │ GWh-TWh      │ Hours-days   │ Long duration,    │
  │                    │ (largest     │              │ ~90% of deployed  │
  │                    │ existing     │              │ grid storage today│
  │                    │ systems)     │              │ Geography-limited │
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Flow batteries     │ MWh-GWh      │ 4-12 hours   │ Long duration,   │
  │ (vanadium redox)   │              │              │ 20,000+ cycles,   │
  │                    │              │              │ electrolyte reuse │
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Compressed air     │ GWh          │ Hours-weeks  │ Geological storage│
  │ (CAES)             │              │              │ Salt caverns      │
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Green hydrogen     │ TWh-scale    │ Weeks-months │ Seasonal storage, │
  │ (electrolysis +    │ potential    │              │ industrial        │
  │ underground H₂     │              │              │ feedstock,        │
  │ storage)           │              │              │ shipping fuel     │
  ├────────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Thermal storage    │ MWh-GWh      │ Hours-days   │ CSP plants,       │
  │ (molten salt, ice) │              │              │ industrial heat,  │
  │                    │              │              │ building cooling  │
  └────────────────────┴──────────────┴──────────────┴───────────────────┘
```

### Nuclear as Firm Power

Nuclear doesn't fit the "cheap new electrons" story but fills a different need: always-on,
high energy density, zero-operational-carbon. Current context:
- Existing fleet: cheapest dispatchable generation in US (fully amortized capital)
- New builds: FOAK (first of a kind) cost overruns (Vogtle, Hinkley Point C)
- SMRs (small modular reactors): NuScale, GE-Hitachi BWRX-300 — factory fabrication
  model intended to address cost problem; still unproven at scale
- Role: provides firm capacity → reduces storage requirements → enables higher VRE penetration

---

## 4. Hard-to-Decarbonize Sectors

### Steel

```
  CONVENTIONAL STEEL (Basic Oxygen Furnace / Blast Furnace):
  Iron ore (Fe₂O₃) + coke (C) → pig iron + CO₂
  Coke is both fuel AND reducing agent → CO₂ is chemically unavoidable
  ~1.8 tonnes CO₂ per tonne steel (world average)
  Steel = ~7% of global CO₂ emissions

  GREEN STEEL PATHWAY (Hydrogen Direct Reduction):

  1. Green H₂ produced via electrolysis (renewable electricity + water)
  2. H₂ replaces coke as reducing agent:
     Fe₂O₃ + 3H₂ → 2Fe + 3H₂O  (water, not CO₂)
  3. Direct reduced iron (DRI) fed to electric arc furnace (EAF)
  4. EAF powered by renewable electricity

  NET: zero CO₂ (if H₂ is green)

  Status: HYBRIT (SSAB/LKAB/Vattenfall, Sweden) — first commercial green
          steel delivered to Volvo in 2021; Salzgitter (Germany) scaling
  Challenge: green H₂ cost + electrolyzer scale + DRI conversion capital
  Timeline: competitive at ~$1.50-2.00/kg green H₂ (current: ~$3-6/kg in
            most regions; declining on electrolyzer cost learning curve)
```

### Cement

```
  CEMENT CO₂ SOURCES:

  ~40% from energy (kiln combustion → can decarbonize with green energy)
  ~60% from calcination → CANNOT be avoided by energy switching:

  CaCO₃ (limestone) → CaO (quicklime) + CO₂

  This CO₂ is from the carbonate chemistry, not combustion.
  ~0.5-0.6 tonnes CO₂ per tonne cement (calcination alone)
  Cement = ~8% of global CO₂ emissions

  MITIGATION STRATEGIES:
  1. Carbon capture at cement plant (capture calcination CO₂, store or use)
  2. Supplementary cementitious materials (SCMs): replace clinker with fly ash,
     GGBFS (ground granulated blast furnace slag), calcined clay
     → Reduces clinker per m³ concrete, reduces calcination CO₂
  3. Alkali-activated materials (geopolymers): no Portland clinker;
     activates blast furnace slag or fly ash with alkali
     → Near-zero process CO₂; not yet mainstream
  4. Re-absorption: cured concrete slowly reabsorbs CO₂ from air (re-carbonation)
     over decades; meaningful at portfolio scale
```

### Aviation

```
  AVIATION DECARBONIZATION OPTIONS:

  Near-term:
  - Sustainable Aviation Fuel (SAF): biomass-derived jet fuel
    Lifecycle: ~70-80% CO₂ reduction vs fossil jet fuel (full lifecycle)
    Problem: ~3-5× cost of fossil jet fuel; feedstock limited; slow scaling
    Blending mandates: EU ReFuelEU requires 2% SAF by 2025, 70% by 2050

  Medium-term:
  - Power-to-liquid (PtL / e-kerosene): green H₂ + captured CO₂ → synthetic
    jet fuel via Fischer-Tropsch. Fully circular carbon if CO₂ from air.
    Cost: ~$5-8/liter currently (fossil jet ~$0.5-0.8/liter)

  Long-term (uncertain):
  - Hydrogen aircraft: H₂ combustion or fuel cells; requires cryogenic
    fuel storage, aircraft redesign; Airbus ZEROe studies (2035 target
    for short-haul); range and infrastructure challenges
  - Battery aircraft: energy density gap too large for commercial aviation
    (today's batteries carry ~100× less energy per kg than jet fuel)

  Non-CO₂ effects: contrails + NOₓ + water vapor cause ~2-4× warming
  effect beyond CO₂ alone (non-CO₂ radiative forcing). Major uncertainty.
```

---

## 5. Carbon Dioxide Removal (CDR)

All credible 1.5-2°C scenarios require both emission reductions AND CDR.
The math: cumulative CO₂ already in atmosphere requires removal; residual emissions
from hard-to-decarbonize sectors require compensation.

```
  CDR PORTFOLIO:

  ┌──────────────────────────────────────────────────────────────────────┐
  │ METHOD          POTENTIAL     COST           PERMANENCE  RISKS       │
  ├─────────────────┬────────────┬───────────────┬───────────┬──────────┤
  │ Afforestation/  │1-3 GtCO₂/yr│ $5-50/tCO₂   │ Decades   │ Wildfire │
  │ Reforestation   │            │               │ (not      │ drought  │
  │                 │            │               │ permanent)│ land use │
  ├─────────────────┼────────────┼───────────────┼───────────┼──────────┤
  │ Soil carbon     │1-3 GtCO₂/yr│ $10-100/tCO₂ │ Decades   │ Reversal │
  │ (regen ag)      │            │               │ (can      │ with land │
  │                 │            │               │ reverse)  │ mgmt chg │
  ├─────────────────┼────────────┼───────────────┼───────────┼──────────┤
  │ BECCS           │1-5 GtCO₂/yr│ $100-200/tCO₂│ Centuries │ Land use │
  │ (Bioenergy +    │(theoretical│ (incl. energy │ (if       │ water    │
  │  CCS)           │ high end)  │ value credit) │ stored)   │ food     │
  ├─────────────────┼────────────┼───────────────┼───────────┼──────────┤
  │ Direct Air      │ Uncapped   │ $300-1000/    │ Permanent │ Energy   │
  │ Capture (DAC)   │ (limited by│ tCO₂ (today) │ (if       │ intensive│
  │                 │ energy +   │ ~$50-100/t    │ stored    │ scaling  │
  │                 │ capital)   │ theoretical   │ geologic) │ challenge│
  │                 │            │ minimum       │           │          │
  ├─────────────────┼────────────┼───────────────┼───────────┼──────────┤
  │ Enhanced        │1-4 GtCO₂/yr│ $50-200/tCO₂ │ Permanent │ Spreading│
  │ weathering      │            │               │ (mineral  │ scale    │
  │ (basalt, etc.)  │            │               │ carbonates│ unknowns │
  ├─────────────────┼────────────┼───────────────┼───────────┼──────────┤
  │ Ocean           │0.1-1 GtCO₂/│ Unknown       │ Uncertain │ Ecosystem│
  │ alkalinization  │ yr (current│               │           │ impacts  │
  │                 │ knowledge) │               │           │ unknowns │
  └─────────────────┴────────────┴───────────────┴───────────┴──────────┘
```

### DAC Deep Dive

Direct Air Capture is the only scalable CDR with permanent geological storage that
doesn't compete for land (if collocated with underground CO₂ storage sites).

```
  DAC PROCESSES:

  1. LIQUID SOLVENT (Carbon Engineering / Oxy):
     Air → potassium hydroxide (KOH) liquid contactors
     CO₂ + 2KOH → K₂CO₃ + H₂O
     K₂CO₃ → limestone kiln (regenerates KOH, releases pure CO₂)
     Energy: ~1.5 GJ heat + ~0.4 GWh electricity per tCO₂

  2. SOLID SORBENT (Climeworks / Global Thermostat):
     Air → amine-functionalized solid sorbent
     CO₂ adsorbs to sorbent
     Heat to ~80-120°C → CO₂ desorbs, collected
     Solid sorbent regenerated, repeat
     Energy: ~5-10 GJ per tCO₂ (lower grade heat = more flexible sourcing)

  CURRENT SCALE:
  Climeworks Mammoth (Iceland, 2024): 36,000 tCO₂/yr capacity
  (global emissions: ~37 billion tCO₂/yr → scale difference = 10⁶)

  COST TRAJECTORY:
  Current: $400-1,000/tCO₂ (depending on source)
  IPCC scenarios: need $50-100/tCO₂ at scale for significant deployment
  IEA Net Zero: 1 GtCO₂/yr DAC by 2050 (from near-zero today)
```

### BECCS

Bioenergy with Carbon Capture and Storage. In theory, plants absorb CO₂ as they grow
(biogenic), then that biomass is burned for energy, and the released CO₂ is captured
and stored geologically — net negative.

**Why it appears in almost every IPCC 1.5°C scenario:**
The math is attractive — energy output PLUS carbon removal. Integrated Assessment
Models (IAMs) use it heavily because it's cheap and energy-generating.

**Why it's contested:**
- Land: growing bioenergy crops competes with food production and forests
- Water: energy crops require irrigation in many scenarios
- Permanence of biological carbon (fire, disease, land use change risks)
- CCS infrastructure requirement same as for fossil CCS
- Only "negative" if biomass genuinely additive (not displacing existing forest)

Credible potential: ~1-3 GtCO₂/yr globally under sustainability constraints.
IAM models often assume 5-10 GtCO₂/yr — likely infeasible without unacceptable
land use trade-offs.

---

## 6. Solar Radiation Management (SRM)

SRM does not remove CO₂. It reduces incoming solar radiation to offset radiative
forcing from CO₂. Critically: if SRM deployed and then stopped, CO₂ remains at
elevated levels and temperature rebounds rapidly — "termination shock."

### Stratospheric Aerosol Injection (SAI)

```
  MECHANISM:

  Analogous to large volcanic eruptions:

  Mt. Pinatubo (1991):
  - 20 Mt SO₂ injected to stratosphere
  - Converted to H₂SO₄/sulfate aerosol droplets
  - Increased Earth's albedo
  - Global temperature: −0.5°C for ~2 years

  SAI concept:
  - Inject SO₂ or other aerosol precursors at ~20 km altitude
  - Stratospheric transport spreads globally within weeks-months
  - Particles settle out over 1-2 years (continuous injection required)
  - Scale to achieve −1°C: ~1-5 Mt SO₂/yr (compared to Pinatubo's 20 Mt for
    a single 2-year event)

  PROPOSED DELIVERY MECHANISMS:
  - High-altitude aircraft (purpose-built; existing aircraft can't reach 20 km)
  - High-altitude balloons
  - Stratospheric hose (SPICE project, never implemented)
  - Artillery/rockets (expensive)

  ESTIMATED COST: very cheap relative to mitigation
  SCoPEx (Harvard research program, canceled outdoor experiments):
  modeled cost ~$2-8 billion/year for 1-2°C offset
  Compare to global climate finance flows of $600+ billion/year
```

### SAI Risks and Uncertainties

```
  KNOWN RISKS:

  1. TERMINATION SHOCK
     SAI must continue indefinitely once started
     If stopped (war, economic collapse, political disruption):
     CO₂ still at high levels → rapid warming at rate ~0.1-0.5°C/decade
     Ecosystem shock from fast temperature change may be worse than
     the slower warming SAI was preventing

  2. PRECIPITATION PATTERN CHANGES
     Pinatubo 1991 associated with:
     - Weakened Asian and African monsoons (~5-10% reduction)
     - Drought in Sahel
     Modeled SAI also shows regional precipitation shifts
     Monsoon disruption → billions of people, agriculture

  3. OZONE DEPLETION
     Sulfate aerosols provide surface for heterogeneous chemistry
     → activates chlorine → catalytic ozone destruction
     Delays recovery of ozone hole

  4. DIFFUSE LIGHT (impact on ecosystems and solar PV)
     Aerosol scattering converts direct beam to diffuse radiation
     - Reduces output of concentrating solar (CSP), negligible effect on flat PV
     - Changes plant photosynthesis (diffuse light can increase canopy penetration)

  5. SKY COLOR
     Milky, whitened sky (Pinatubo's sunsets were famously colorful)
     Estimated to reduce starlight visibility significantly

  WHAT IT DOES NOT ADDRESS:
  - Ocean acidification (CO₂ chemistry unaffected)
  - CO₂ fertilization effects
  - Long-term warming (only masks, doesn't reverse)
```

### Marine Cloud Brightening (MCB)

Spray sea salt particles into marine low clouds → more cloud condensation nuclei →
smaller droplets → brighter clouds → higher albedo. More localized than SAI.

```
  MECHANISM:
  Twomey effect — marine cloud droplets:

  Few CCN: fewer, larger drops, lower albedo
  Many CCN: more, smaller drops, higher albedo (same liquid water content)

  Status: small-scale field trials (University of Washington/CALFIN);
  scaling physics uncertain; regional rather than global effect
  Advantage over SAI: reversible, no stratospheric chemistry effects
  Disadvantage: localized effects, may affect rainfall downwind
```

### SRM Governance

```
  GOVERNANCE GAP:

  No international framework exists for:
  - Research authorization
  - Small-scale outdoor experiments
  - Large-scale deployment
  - Consent from affected nations
  - Liability for impacts

  Fundamental problem:
  - SAI would be transboundary by definition — aerosols spread globally
  - Country A deploys SAI → benefits Country A; potentially harms Country B
    (altered monsoon)
  - No mechanism for consent, compensation, or control

  Moral hazard debate:
  - "If SRM is available, will it reduce pressure to cut emissions?"
  - The "insurance analogy": having a fire extinguisher doesn't mean you stop
    fireproofing the building — it's an emergency backup
  - Counter: political psychology ≠ engineering logic; moral hazard is real

  Current governance approaches:
  - "Research governance" frameworks: SCoPEx (Harvard), DEGREES Initiative
  - UNEA Resolution on SRM (discussed but not adopted)
  - Calls for UN-level deliberative process before any deployment

  CURRENT CONSENSUS: outdoor SAI experiments require broad governance framework
  first. Indoor/modeling research broadly accepted. No responsible actor
  advocates unilateral deployment.
```

---

## 7. The Portfolio Problem

```
  IPCC AR6 — What's required for 1.5°C:

  ┌────────────────────────────────────────────────────────────────┐
  │ BY 2030 (7-8 years from now):                                 │
  │ - Global CO₂ emissions ~43% below 2019 levels                │
  │ - Roughly: eliminate all coal power, cut oil use ~20%,        │
  │   triple renewables, major efficiency improvements            │
  ├────────────────────────────────────────────────────────────────┤
  │ BY 2050:                                                       │
  │ - Net zero CO₂ globally (all sectors)                        │
  │ - Roughly: 0 coal, near-0 fossil gas (CCS or H₂), near-0     │
  │   oil, all electricity low-carbon, green steel/cement, CDR   │
  ├────────────────────────────────────────────────────────────────┤
  │ CDR ROLE:                                                      │
  │ - 100-1000 GtCO₂ CDR this century depending on scenario      │
  │ - Even most ambitious mitigation needs CDR for:              │
  │   (a) past emissions overshoot correction                    │
  │   (b) residual emissions from aviation/cement/agriculture    │
  └────────────────────────────────────────────────────────────────┘

  KEY INSIGHT: There is no single solution. The mitigation portfolio is:

  Near-term, proven, scaling: Solar PV + Wind + EV + efficiency
  Medium-term, proven, scaling: Green H₂ + green steel + grid storage
  Near-term CDR, limited: Afforestation, soil carbon, BECCS (constrained)
  Long-term CDR, needed: DAC at scale ($100/t target), enhanced weathering
  Contingency/risk: SRM (only if emissions fail catastrophically AND governance)
```

---

## Decision Cheat Sheet

| Technology/Approach | Role | Current Status | Key Constraint |
|--------------------|------|----------------|----------------|
| Solar PV | Main emissions reduction | Cheapest electricity ever; scaling fast | Intermittency; integration |
| Onshore wind | Main emissions reduction | Proven, cheap | Siting/permitting |
| Offshore wind | Firm-ish renewable | Scaling; higher CF | Cost; supply chain |
| Li-ion storage | Short-duration integration | Rapid cost decline | Duration (hours only) |
| Pumped hydro | Long-duration storage | Proven; most storage today | Geography limited |
| Nuclear | Firm zero-carbon power | Existing fleet: yes; new: cost challenge | New build cost; FOAK |
| Green hydrogen | Hard-sector + seasonal | Early; high cost | H₂ cost; efficiency |
| Green steel (H₂-DRI) | Industry decarbonization | First commercial plants | H₂ cost + DRI capex |
| Green cement | Industry decarbonization | SCMs proven; geopolymer emerging | Calcination CO₂ fundamental |
| SAF / PtL | Aviation | SAF scaling; PtL prototype | Cost: 3-5× fossil |
| Afforestation | CDR, near-term | Proven biology | Permanence; land use |
| BECCS | CDR + energy | Scenarios use heavily | Land/water; credibility |
| DAC | Permanent CDR, scalable | Early; $400-1000/tCO₂ now | Cost; energy; scale |
| SAI | SRM emergency option | Research only; governance absent | Termination shock; governance |

---

## Common Confusion Points

**"Renewables need 100% backup from gas"**
False for all but very high penetrations. At 30-40% VRE on a grid, storage + demand
response + transmission covers most variability. At 80%+ VRE, firm backup matters.
Current UK grid: 45%+ renewables share with existing gas backup + interconnects.

**"Germany proves renewables don't work — high prices and high CO₂"**
Germany's Energiewende context: it shut down nuclear (political decision post-Fukushima)
while building out renewables — the nuclear shutdown was the driver of the CO₂ and
price issues, not the renewables. Countries with hydro-backed renewables (Norway,
Iceland, Costa Rica) show 95-100% clean electricity is achievable.

**"We can just plant trees and solve climate change"**
Global afforestation potential: ~1-3 GtCO₂/yr under realistic land use constraints.
Global emissions: ~37 GtCO₂/yr. Trees help at the margin; they don't come close to
compensating for continued fossil fuel use.

**"DAC is science fiction"**
Commercial DAC plants exist and operate. Climeworks' Mammoth plant in Iceland (2024)
captures 36,000 tCO₂/yr for $400-800/tCO₂ and stores it geologically via CarbFix.
It's real, expensive, and small. The question is whether cost comes down fast enough.

**"SAI would fix climate change"**
SAI would temporarily mask warming but: doesn't reduce CO₂ (ocean acidification
continues), requires permanent maintenance, creates termination shock risk, doesn't
address long-term CO₂ trajectory. It's a tourniquet, not surgery. The IPCC frames
it as a potential risk-reduction tool for the most severe near-term impacts, not
as an alternative to mitigation.
