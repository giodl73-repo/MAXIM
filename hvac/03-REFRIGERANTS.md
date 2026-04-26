# Refrigerants

## The Big Picture

Refrigerant selection is driven by three competing concerns: thermodynamic performance,
safety (flammability/toxicity), and environmental impact (ozone depletion and climate).
The industry has been forced through three major transitions in 40 years, with a fourth
underway now.

```
+----------------------------------------------------------------------+
|                    REFRIGERANT TRANSITION TIMELINE                   |
|                                                                      |
|  1930s–1980s:  CFCs dominant (R-12, R-11, R-502)                     |
|                Great thermodynamics, zero flammability               |
|                → Discovered: destroys stratospheric ozone            |
|                                                                      |
|  1987:   Montreal Protocol → CFC phaseout mandate                    |
|  1996:   R-12 production ends in developed nations                   |
|                                                                      |
|  1990s–2000s:  HCFCs as transition (R-22 dominant)                   |
|                Lower ODP than CFCs, still good thermodynamics        |
|                → Also ozone-depleting (less so), and high GWP        |
|                                                                      |
|  2010:   R-22 new equipment banned in US                             |
|  2020:   R-22 new production/import banned in US                     |
|                                                                      |
|  2006–2024:  HFCs dominant (R-410A, R-134a, R-404A)                  |
|                ODP=0, excellent thermodynamics                       |
|                → High GWP (climate forcing)                          |
|                                                                      |
|  2016:   Kigali Amendment to Montreal Protocol → HFC phasedown       |
|  2025:   US GWP cap: new residential AC/HP must use ≤700 GWP         |
|                                                                      |
|  2025+:  A2L refrigerants (R-32, R-454B, R-466A) + naturals          |
|                Low GWP, mildly flammable (A2L class)                 |
+----------------------------------------------------------------------+
```

---

## Section 1: Refrigerant Naming Conventions

The R-### numbering system encodes molecular structure. You don't need to memorize
the formula, but understanding the naming helps decode the letter prefixes:

```
  CFC  = Chlorofluorocarbon     (ex: R-12, R-11, R-502)
         Chlorine + Fluorine + Carbon
         ODP ≠ 0 (chlorine → catalytic ozone destruction)

  HCFC = Hydrochlorofluorocarbon (ex: R-22, R-123)
         Hydrogen + Chlorine + Fluorine + Carbon
         Lower ODP than CFC (hydrogen reduces atmospheric lifetime)

  HFC  = Hydrofluorocarbon      (ex: R-410A, R-134a, R-32)
         Hydrogen + Fluorine + Carbon — NO chlorine
         ODP = 0, but high GWP

  HFO  = Hydrofluoroolefin      (ex: R-1234yf, R-1234ze)
         Contains C=C double bond → short atmospheric lifetime → low GWP
         ODP = 0, GWP < 10

  Naturals: CO₂ (R-744), Propane (R-290), Ammonia (R-717), Isobutane (R-600a)

  Blends: letter suffix indicates specific blend composition
  R-410A = 50% R-32 + 50% R-125 (zeotropic blend)
  R-454B = 68.9% R-32 + 31.1% R-1234yf (designed as R-410A replacement)
```

---

## Section 2: Safety Classifications (ASHRAE Standard 34)

```
  LETTER (Toxicity):  A = lower acute toxicity risk
                      B = higher toxicity risk (ammonia = B1)

  NUMBER (Flammability):
  1  = Nonflammable (no propagation under any test conditions)
  2L = Weakly flammable (burns but needs ignition source, slow flame speed)
  2  = Flammable (burns readily)
  3  = Highly flammable (like propane — explosive)

  ┌─────┬─────────────────────────────────────────────────────────────┐
  │Class│ Examples / Notes                                            │
  ├─────┼─────────────────────────────────────────────────────────────┤
  │ A1  │ R-410A, R-134a, R-404A — nonflammable, lower toxicity      │
  │     │ No flammability concerns in field                           │
  ├─────┼─────────────────────────────────────────────────────────────┤
  │ A2L │ R-32, R-454B, R-466A — mildly flammable                     │
  │     │ Requires: ventilation, leak detection in some applications  │
  │     │ Flame speed <10 cm/s (vs propane ~46 cm/s)                  │
  │     │ Major transition class for new US equipment 2025+           │
  ├─────┼─────────────────────────────────────────────────────────────┤
  │ A2  │ R-152a — flammable. Limited use.                           │
  ├─────┼─────────────────────────────────────────────────────────────┤
  │ A3  │ R-290 (propane), R-600a (isobutane) — highly flammable      │
  │     │ Limited charge size (<150g per circuit in residential)      │
  │     │ Explosion-proof controls required                           │
  ├─────┼─────────────────────────────────────────────────────────────┤
  │ B1  │ R-717 (ammonia) — toxic but nonflammable                   │
  │     │ Industrial refrigeration, large chillers                    │
  └─────┴─────────────────────────────────────────────────────────────┘
```

---

## Section 3: Environmental Metrics

```
  ODP (Ozone Depletion Potential):
  Reference compound: R-11 (ODP = 1.0)
  CFC R-12: ODP = 1.0 (catastrophic)
  HCFC R-22: ODP = 0.05 (less, but still significant)
  HFC R-410A: ODP = 0 (no chlorine)
  HFO/naturals: ODP = 0

  GWP (Global Warming Potential):
  Reference compound: CO₂ over 100-year horizon (GWP = 1)
  R-22: GWP = 1,760
  R-410A: GWP = 2,088
  R-404A: GWP = 3,922 (used in commercial refrigeration)
  R-32: GWP = 675
  R-454B: GWP = 466
  R-1234yf: GWP < 1
  CO₂ (R-744): GWP = 1
  Propane (R-290): GWP = 3
  Ammonia (R-717): GWP = 0

  GWP perspective: 1 lb of R-410A released to atmosphere
  ≡ 2,088 lbs of CO₂ (nearly 1 ton of CO₂ per pound of refrigerant)
  Typical 3-ton AC system: ~5 lbs R-410A
  If fully released: ~10,000 lbs CO₂ equivalent
```

---

## Section 4: Refrigerant Profiles — Key Systems

### R-12 (Freon, CFC-12) — Historical Context

```
  Chemical: CCl₂F₂ (dichlorodifluoromethane)
  ODP: 1.0    GWP: 10,200    Safety: A1

  - The original Freon. Dominated household refrigeration and car AC 1930s–1990s
  - Excellent properties: low boiling point, stable, zero flammability
  - CFC → catalytic ozone destruction discovered by Molina & Rowland (1974 Nobel)
  - Montreal Protocol 1987: production phaseout mandate
  - Developed nations: R-12 production ended 1996
  - Car AC retrofit target: R-134a (drop-in with oil change)
  - No new R-12 equipment anywhere. Historical knowledge only.
```

### R-22 (HCFC-22) — The Dominant Legacy Refrigerant

```
  Chemical: CHClF₂ (chlorodifluoromethane)
  ODP: 0.05   GWP: 1,760    Safety: A1

  - Replaced R-12 for residential and commercial AC from 1970s
  - Still in millions of operating systems in US (installed 1985–2010)
  - Equipment ban: 2010 (no new R-22 equipment)
  - Production/import ban: 2020 (US EPA Section 608)
  - Post-2020: only reclaimed/recycled R-22 legal for service
  - R-22 price spike: $5–10/lb pre-2020 → $50–80+/lb after 2020
  - At some price point, replacement is economical vs. repair

  RETROFIT OPTIONS for R-22 systems:
  ┌──────────────┬──────────────────────────────────────────────────────┐
  │ R-407C       │ Drop-in; similar pressures; lower capacity; requires │
  │              │ oil change; acceptable efficiency                    │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ R-422D       │ True drop-in (compatible with mineral oil); lower    │
  │              │ capacity and efficiency; temporary measure           │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Full replace │ New R-410A or R-32/R-454B equipment; proper          │
  │ equipment    │ solution; qualifies for IRA tax credits              │
  └──────────────┴──────────────────────────────────────────────────────┘
```

### R-410A (Puron) — The Recent Standard

```
  Chemical: 50% R-32 + 50% R-125 (blend)
  ODP: 0    GWP: 2,088    Safety: A1    Pressures: ~70% higher than R-22

  - Replaced R-22 in US residential AC/HP systems starting ~2006
  - NOT interchangeable with R-22: different operating pressures, different oil
  - Equipment cannot be retrofitted between the two
  - Excellent thermodynamic properties; high operating pressure requires robust components
  - Now being phased down under AIM Act / EPA rules
  - US GWP cap: ≤700 GWP required for new residential AC/HP as of Jan 1, 2025
  - R-410A systems manufactured before 2025 can still be serviced with R-410A
  - Refrigerant will be available for service for years (reclaimed supply)
```

### R-32 — The Transition Refrigerant

```
  Chemical: CH₂F₂ (difluoromethane)
  ODP: 0    GWP: 675    Safety: A2L (mildly flammable)    Pressures: ~similar to R-410A

  - Pure refrigerant (not a blend); better thermodynamic properties than R-410A
  - Widely adopted in Asia and Europe since ~2015
  - Mitsubishi Electric has used R-32 extensively in mini-splits
  - A2L classification: burns slowly; requires updated installation practices
  - ASHRAE 15 and IFC fire code adoption of A2L = key adoption enabler in US
  - Better efficiency than R-410A in similar equipment designs
```

### R-454B (Puron Advance) — The US R-410A Replacement

```
  Chemical: 68.9% R-32 + 31.1% R-1234yf
  ODP: 0    GWP: 466    Safety: A2L

  - Carrier's designated R-410A replacement; meets <700 GWP requirement
  - Operates at similar pressures to R-410A → equipment form factor similar
  - A2L safety: new equipment designs include provisions for mildly flammable refrigerants
  - Other manufacturers use R-32 directly; R-454B competes with R-32
  - R-466A (Chemours/Honeywell A1 candidate — no flammability) competing for market
```

### R-290 (Propane) — The Natural Refrigerant Exception

```
  Chemical: C₃H₈ (propane)
  ODP: 0    GWP: 3    Safety: A3 (highly flammable)

  - Exceptional thermodynamic properties; excellent for commercial refrigeration
  - European window AC units: ≤150g charge per circuit (small enough to be safe)
  - Commercial refrigeration display cases (supermarkets) in Europe
  - Limited charge size per circuit required by US codes for residential
  - Explosion-proof controls, spark-free handling required
  - True environmental winner but A3 rating limits residential adoption
```

### R-744 (CO₂) — The High-Pressure Alternative

```
  Chemical: CO₂
  ODP: 0    GWP: 1    Safety: A1    Pressures: up to 1,500+ PSIA

  - Operates in transcritical cycle (above critical point in condenser) in many applications
  - Critical point: 87.8°F, 1,070 PSIA → above ambient temp in summer → transcritical
  - Requires specialized, high-pressure components
  - European supermarket refrigeration chains: entire store on CO₂ cascade system
  - CO₂ heat pump water heaters: extremely high efficiency (COP 4–5), available in Japan/Europe
  - Not viable for standard residential split systems (pressure too high for existing hardware)
```

---

## Section 5: Regulatory Framework

```
  MONTREAL PROTOCOL (1987):
  └── CFC phaseout → established template for global refrigerant regulation
      └── KIGALI AMENDMENT (2016):
          └── HFC phasedown mandate
          ├── Developed countries: 85% reduction by 2036 (vs 2011–2013 baseline)
          ├── Developing countries: phasedown starting 2024–2028
          └── US ratified: December 2022

  EPA AIM ACT (American Innovation and Manufacturing Act, 2020):
  └── Implements Kigali in US
      ├── HFC phasedown schedule (85% by 2036)
      ├── GWP-based equipment prohibitions
      └── Jan 1, 2025: new residential AC/HP must use ≤700 GWP refrigerant

  EU F-GAS REGULATION:
  └── More aggressive than US; drives European adoption of low-GWP
      └── Automotive: R-134a banned 2017 → R-1234yf (GWP < 1) standard now
```

---

## Decision Cheat Sheet

| Scenario | Refrigerant |
|---|---|
| Existing R-22 system, minor leak | Recharge with reclaimed R-22 (expensive) |
| R-22 system, major failure | Replace equipment with R-32 or R-454B system |
| New residential split system (2025+) | R-32 or R-454B (mandated ≤700 GWP) |
| New residential mini-split | R-32 (dominant in mini-splits) |
| Commercial refrigeration (supermarket) | R-744 (CO₂) cascade, or HFO blends |
| Industrial refrigeration (large) | R-717 (ammonia) + secondary loop |
| Residential refrigerator | R-600a (isobutane, small charge) |

---

## Common Confusion Points

**R-410A is being phased out, not banned**: existing R-410A systems can still be serviced
with reclaimed R-410A. New equipment must use lower-GWP refrigerant. No emergency to
replace a working R-410A system — just don't expect new R-410A units after 2025.

**A2L is not the same as propane flammability**: A2L (mildly flammable) requires ignition
source, burns slowly (flame speed <10 cm/s), and has limits on propagation. It's not the
same risk profile as propane (A3). The industry is adapting installation codes for A2L.

**Drop-in retrofit is a compromise**: no refrigerant is truly a "drop-in" for R-22 without
consequences. Pressure differences, oil compatibility, capacity changes — all require at
minimum an oil flush and system assessment. "Drop-in" usually means "close enough to work."

**GWP accounts for refrigerant leaks, not combustion**: propane's GWP-3 is its GWP as
a refrigerant (atmospheric impact if leaked). Combusting propane produces CO₂, separate issue.
