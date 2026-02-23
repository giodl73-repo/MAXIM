# Session 15 — Materials Science & Engineering

**Date:** 2026-02-22
**Track:** Engineering Sciences — Foundations

---

## What This Session Covers

Materials science is the bridge between physics/chemistry at the atomic scale and engineering at the human scale. The central theme is **structure ↔ properties ↔ processing**: you cannot understand why steel is hard, why silicon is a transistor, or why a polymer creeps under load without understanding the atomic-to-microstructure hierarchy.

---

## Module Index

| File | Topic | Status |
|------|-------|--------|
| `materials/00-OVERVIEW.md` | Four materials families, Ashby charts, property space, characterization methods | ✅ |
| `materials/01-CRYSTAL-STRUCTURE.md` | Bravais lattices, Miller indices, XRD, all defect types, Hall-Petch | ✅ |
| `materials/02-BONDING-BANDS.md` | Ionic/covalent/metallic bonding, free electron model, band theory, phonons, superconductivity | ✅ |
| `materials/03-SEMICONDUCTORS.md` | p-n junction, MOSFET physics, BJT, photovoltaics, LEDs | ✅ |
| `materials/04-METALS-ALLOYS.md` | Phase diagrams, Fe-C system, heat treatment, strengthening mechanisms, fracture | ✅ |
| `materials/05-POLYMERS.md` | Chain architecture, T_g/T_m, rubber elasticity, WLF equation, viscoelasticity | ✅ |
| `materials/06-NANOMATERIALS-QUANTUM.md` | Quantum confinement, graphene, CNTs, plasmonics, spintronics, topological materials | ✅ |

---

## Learning Arc

```
Atomic bonding (02)
      │
      ├─→ Crystalline order (01) ──→ Defects → Strengthening (04)
      │
      ├─→ Electronic structure (02) ──→ Semiconductors (03)
      │
      ├─→ Thermodynamics of mixing (04) ──→ Phase diagrams → Microstructure
      │
      ├─→ Chain statistics (05) ──→ Polymer mechanics
      │
      └─→ Confinement at nm scale (06) ──→ Quantum materials
```

---

## Key Mental Models

**Ashby charts:** Every material occupies a point in property space (E vs density, K_IC vs strength). Design is selecting the region that meets constraints and optimizing objectives.

**Structure-property link:** Same composition, different processing → very different properties. Fe-0.8%C can be soft pearlite (annealed) or hard martensite (quenched). The phase diagram tells you what is thermodynamically stable; the TTT diagram tells you what you actually get at a given cooling rate.

**Quantization at the nanoscale:** When structure size < Bohr radius or de Broglie wavelength, electronic properties become size-dependent and continuously tunable (quantum dots, CNTs, 2D materials).

---

## MIT / Physics Connections

- **Bloch's theorem** (QM periodicity) → band structure of all crystalline materials
- **Statistical mechanics** → Fermi-Dirac distribution, phonon heat capacity, polymer rubber elasticity
- **Thermodynamics** → phase diagrams, Gibbs phase rule, driving forces for phase transformation
- **Electrostatics** → p-n junction depletion physics, MOSFET threshold voltage, DLVO colloidal stability
- **Topology** → Z₂ topological invariants, Dirac cones in graphene and topological insulators

---

## Bridges to Engineering

| Materials concept | Engineering consequence |
|-------------------|------------------------|
| Dislocation motion | Plastic deformation, yield strength design |
| Grain boundary Hall-Petch | HSLA steels, grain refinement via TMCP |
| TTT / CCT diagrams | Heat treatment protocols for spring steel, gears, bearings |
| Precipitation hardening | 7075-T6 aircraft structure, Ni superalloy turbine blades |
| Band gap engineering | LED wavelength selection, solar cell spectrum matching |
| MOSFET scaling limits | FinFET → GAA → 2D materials for sub-3nm nodes |
| TMR in MTJs | Hard disk read heads (since ~1997), MRAM |
| BCP self-assembly | Next-generation lithography at sub-20 nm pitch |
