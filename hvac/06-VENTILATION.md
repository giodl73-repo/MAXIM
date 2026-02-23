# 06 — Ventilation

## ERV, HRV, ASHRAE 62.2, MERV, IAQ

> **STUB** — outline only, content to be authored

**Planned coverage:**
- **Why ventilation**: modern tight construction (blower door result <3 ACH50 in new homes vs >10 ACH50 in older leaky homes) → insufficient natural infiltration for acceptable IAQ; tight envelope is essential for energy efficiency but requires intentional mechanical ventilation; ASHRAE 62.2 (residential) and 62.1 (commercial) specify minimum ventilation rates
- **Infiltration vs ventilation**: infiltration = uncontrolled air leakage through cracks, gaps, penetrations; driven by wind and stack effect (warm air rises, positive pressure at top, negative at bottom of building); unpredictable, energy wasteful; ventilation = intentional, controlled introduction of outdoor air; measured and optimized
- **ASHRAE 62.2 (residential)**: minimum ventilation rate = 0.01 CFM/ft² floor area + 7.5 CFM/person (based on bedrooms +1); typical 1500 ft² 3-bedroom home = ~45-60 CFM whole-house ventilation; requirement = any combination of exhaust, supply, or balanced ventilation that achieves the rate
- **Ventilation strategies**:
  - Exhaust-only: bathroom or kitchen exhaust fan runs continuously or intermittently; creates slightly negative pressure; outdoor air infiltrates through leaks (unpredictable); simplest/cheapest; problem: draws radon, moisture from crawlspace, pollutants from garage if pressure differential pulls from those sources
  - Supply-only: fresh air fan forces outdoor air into return duct or directly; slightly positive pressure; cleaner air path; problem: in cold climates can push moisture into walls
  - Balanced (ERV/HRV): equal exhaust and supply; no pressure imbalance; most controlled; adds cost of equipment
- **HRV (Heat Recovery Ventilator)**: exhausts stale indoor air + supplies fresh outdoor air; heat exchanger in core transfers 70-80% of sensible heat from exhaust to supply; doesn't transfer moisture; ideal for cold, dry climates where moisture transfer undesirable (don't want to bring in outdoor humidity in humid summers, don't want to lose indoor humidity in dry winters); no condensation of moisture in core
- **ERV (Energy Recovery Ventilator)**: transfers both sensible heat AND moisture (enthalpy) between exhaust and supply streams; desiccant wheel or membrane core; ideal for hot/humid climates (summer: removes moisture from incoming hot/humid air before entering building; winter: retains moisture from outgoing exhaust); both HRV and ERV recover ~70-80% of energy that would otherwise be lost; choice depends on climate
- **Filtration — MERV ratings**: Minimum Efficiency Reporting Value (ASHRAE 52.2); scale 1-16; captures particles at specified sizes:
  - MERV 1-4: fiberglass, pollen, dust mites (>10 micron)
  - MERV 5-8: mold spores, dust (3-10 micron) — minimum recommended
  - MERV 9-12: Legionella, lead dust, auto emissions (1-3 micron) — good residential
  - MERV 13-16: bacteria, virus-carrying droplets (0.3-1 micron) — hospital, HVAC-upgraded residential
  - MERV 17+: HEPA (≥99.97% at 0.3 micron) — cleanroom, OR
  - Tradeoff: higher MERV = more pressure drop = more fan energy = must check system can handle restriction; MERV 13 appropriate for most residential with properly sized system
- **IAQ pollutants and monitoring**: CO₂ (proxy for occupancy/ventilation adequacy — above 1000 ppm = inadequate ventilation); CO (carbon monoxide — combustion appliance leak, life-safety); VOCs (off-gassing from materials, cleaning products — TVOC monitoring); PM2.5 (fine particles — outdoor pollution, cooking, wildfire smoke); radon (radioactive gas from soil, 2nd leading cause of lung cancer in US — EPA action level 4 pCi/L); formaldehyde (from composite wood, insulation); humidity (30-50% RH optimal — below = static, cracking, virus survival; above = mold)
- **Demand-controlled ventilation (DCV)**: CO₂ sensor controls ventilation rate; increase ventilation when CO₂ rises (occupied, need more ventilation); reduce when CO₂ low (unoccupied — save energy); ASHRAE 62.1 allows DCV for commercial; IAQ monitoring enables data-driven ventilation; smart ERV/HRV controllers available
