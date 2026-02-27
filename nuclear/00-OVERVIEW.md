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

<!-- @editor[structure/P1]: Missing Decision Cheat Sheet — the "Decision Guide" below is a module routing flowchart, not a decision table. Needs a "use X when Y" table: e.g., "when studying reactor stability → reactivity coefficients in 02; when comparing reactor types → 04; when analyzing safety margins → DNBR in 03; when evaluating waste management → 05." The overview should close with a quick-reference table, not just navigation bullets. -->
<!-- @editor[structure/P2]: Missing Common Confusion Points at the overview level. The cross-cutting gotchas (criticality ≠ danger, decay heat ≠ fission, containment ≠ reactor vessel, k_eff = 1 is normal operation) are distributed across the individual module files. A brief field-level confusion section here would orient the reader before they encounter the technical depth. -->
## Decision Guide

```
WHAT NUCLEAR QUESTION?
        │
        ├─ What is the physics of the chain reaction?
        │   └─► 01-NUCLEAR-PHYSICS + 02-REACTOR-PHYSICS
        │
        ├─ How is heat removed and what limits power?
        │   └─► 03-THERMAL-HYDRAULICS
        │
        ├─ Which reactor design and why?
        │   └─► 04-REACTOR-TYPES
        │
        └─ How are accidents prevented and what happened in past accidents?
            └─► 05-SAFETY-SYSTEMS
```
