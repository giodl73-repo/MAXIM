# Nuclear Engineering — Landscape & Field Taxonomy

## The Big Picture

Nuclear engineering harnesses the energy released by **rearranging nuclei** — fission releases
~200 MeV per event vs ~4 eV for chemical combustion: a factor of 50 million. The engineering
challenge is not generating heat (that's easy) but **controlling it safely**, removing decay heat
that persists after shutdown, and managing radioactive materials across their entire lifecycle.

```
NUCLEAR PHYSICS
  Binding energy, cross sections, decay, fission chain reaction
        │
        ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  REACTOR PHYSICS (NEUTRONICS)                                            │
│  Criticality k_eff, neutron transport, flux distribution, kinetics      │
├─────────────────────────────────────────────────────────────────────────┤
│  THERMAL HYDRAULICS                                                      │
│  Heat removal from fuel, coolant flow, DNB, reactivity feedback         │
├─────────────────────────────────────────────────────────────────────────┤
│  REACTOR TYPES                                                           │
│  PWR, BWR, CANDU, SMR, Gen IV concepts                                  │
├─────────────────────────────────────────────────────────────────────────┤
│  SAFETY SYSTEMS & ACCIDENT ANALYSIS                                      │
│  Defense in depth, ECCS, LOCA, accident lessons                         │
├─────────────────────────────────────────────────────────────────────────┤
│  FUEL CYCLE                                                              │
│  Mining → enrichment → fabrication → reactor → spent fuel → waste       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Module Map

| Module | Core Topic | Key Concepts | Real Application |
|--------|-----------|-------------|-----------------|
| `01-NUCLEAR-PHYSICS` | Binding energy, fission, decay | Q-values, σ, β, T½ | Core physics input |
| `02-REACTOR-PHYSICS` | Criticality, neutron economy | k_eff, four factors, kinetics | Reactor design/operation |
| `03-THERMAL-HYDRAULICS` | Heat removal, coolant flow | DNB, DNBR, natural circulation | Safety limits |
| `04-REACTOR-TYPES` | Design variants | PWR/BWR/CANDU/Gen IV | Technology selection |
| `05-SAFETY-SYSTEMS` | Defense in depth | ECCS, LOCA, TMI/Chernobyl/Fukushima | Licensing, accidents |

---

## The Energy Scale

```
Reaction type        Energy per event     Fuel density
──────────────────────────────────────────────────────────────────
Chemical (coal)      ~4 eV/atom           3 MJ/kg
Nuclear fission      ~200 MeV/event       80,000,000 MJ/kg U-235
Nuclear fusion (D-T) ~17.6 MeV/event     ~340,000,000 MJ/kg D

1 kg U-235 fissioned completely → 83 TJ ≈ 1 coal train car per gram
1 PWR fuel assembly (500 kg UO₂, 4% enriched) → ~14 TJ per reload
```

---

## Worldwide Nuclear Fleet (2024)

```
~440 operating reactors in ~30 countries
~400 GWe installed capacity (~10% of world electricity)

Breakdown by type:
  PWR:   ~70%  (most common, US/France/China/Russia)
  BWR:   ~15%  (US/Japan)
  PHWR:  ~10%  (CANDU, India/Canada)
  Other:  ~5%  (RBMK, VVER, research reactors)

Countries by share of electricity from nuclear:
  France: ~70%, Ukraine: ~55%, Slovakia: ~60%, Belgium: ~50%
  US: ~20%, UK: ~16%, Russia: ~20%, China: ~5% (growing fast)
```

---

## Connection to Other Fields

| Nuclear concept | Parallel in other fields |
|----------------|-------------------------|
| Neutron diffusion equation | Same math as heat conduction (Fourier) |
| Reactivity feedback | Control theory (feedback, stability, PID) |
| Thermal hydraulics | Mechanical engineering heat transfer (03-HEAT-TRANSFER.md) |
| Fission product decay heat | Time-constant system like RC circuit |
| Monte Carlo neutron transport | Statistical sampling: same technique as GPU ray tracing |
| Nuclear fuel burnup | ODE integration (Bateman equations) |
| PRA (Probabilistic Risk Assessment) | Fault trees → same as reliability engineering, FMEA |

---

## Decision Cheat Sheet

| When you need to...                                    | Go to                       | Key concepts                                          |
|--------------------------------------------------------|-----------------------------|-------------------------------------------------------|
| Understand fission physics and cross sections          | 01-NUCLEAR-PHYSICS          | Binding energy curve, cross sections, decay chains    |
| Analyze reactor stability and criticality              | 02-REACTOR-PHYSICS          | Six-factor formula, reactivity coefficients, xenon    |
| Evaluate thermal safety margins                        | 03-THERMAL-HYDRAULICS       | DNBR, CHF correlations, hot channel factors           |
| Compare reactor designs and their trade-offs           | 04-REACTOR-TYPES            | PWR vs BWR vs CANDU vs Gen IV; coolant/moderator matrix|
| Analyze safety systems and accident scenarios          | 05-SAFETY-SYSTEMS           | Defense-in-depth, ECCS, PRA/CDF, TMI/Chernobyl/Fukushima |
| Understand why k_eff must be held at exactly 1.000     | 02 (reactivity control)     | Delayed neutrons provide the ~100s response margin    |
| Understand why decay heat persists after shutdown       | 01 (fission products)       | Fission products continue beta/gamma decay for years  |
| Evaluate waste and fuel cycle options                  | 04 (fuel cycle section)     | Once-through vs reprocessing; geological disposal     |

---

## Common Confusion Points

**Criticality does NOT mean danger.** A reactor at k_eff = 1.000 is "critical" — this is normal, steady-state operation. "Supercritical" (k_eff slightly > 1) is routine during a controlled power increase. "Prompt critical" (k_eff > 1 + beta_eff) is the dangerous threshold where the reactor period drops to milliseconds.

**Decay heat is NOT fission.** After shutdown (k_eff < 1, chain reaction stops), fission products continue emitting beta and gamma radiation as they decay. This generates ~7% of rated power immediately after shutdown, declining to ~1% after 1 hour and ~0.1% after 1 week. This is why cooling must continue indefinitely — Fukushima was a decay heat removal failure, not a criticality event.

**Containment is NOT the reactor vessel.** The reactor pressure vessel (RPV) contains the core and coolant at high pressure/temperature. The containment structure is a separate, much larger building surrounding the RPV, designed to confine radioactive material if the RPV fails. They serve different functions at different scales.

**k_eff = 1 is the operating point, not a safety margin.** The safety margin is in the reactivity feedback coefficients (Doppler, moderator temperature coefficient) — both must be negative so that any temperature rise reduces reactivity, driving k_eff back below 1. This is inherent negative feedback, not active control.

---

## Decision Guide

```
WHAT NUCLEAR QUESTION?
        |
        +-- What is the physics of the chain reaction?
        |   --> 01-NUCLEAR-PHYSICS + 02-REACTOR-PHYSICS
        |
        +-- How is heat removed and what limits power?
        |   --> 03-THERMAL-HYDRAULICS
        |
        +-- Which reactor design and why?
        |   --> 04-REACTOR-TYPES
        |
        +-- How are accidents prevented and what happened in past accidents?
            --> 05-SAFETY-SYSTEMS
```
