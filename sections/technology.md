# Technology

*9 directories current + Batch 12 · ~870 pp current · T·I, T·II, T·III, T·IV*

Modern engineering — the electronic age through the systems age. Technology covers the disciplines that emerged or were transformed by electronics, computation, and large-scale systems thinking: the semiconductor fab, the 5G protocol stack, the autonomous robot, the medical scanner, and the software verification proof.

The word became a department name when the disciplines it covered were too new for classical "Mechanics" to encompass. Where Mechanics built with force and heat, Technology builds with signal, information, and coordinated complexity. The boundary is roughly 1900 — the year the electron was confirmed (J. J. Thomson, 1897) and the vacuum tube was on the horizon.

*Batch 12 will add: nanotechnology/ · energy-storage/ · infrastructure-systems/*

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                 TECHNOLOGY                                  │
│            Modern engineering — electronic age through systems age          │
└─────────────────────────────────────────────────────────────────────────────┘

 SILICON & SIGNALS TRACK
 ┌───────────────────────┐  ┌────────────────────────┐  ┌──────────────────┐
 │ semiconductor-        │  │  telecommunications/   │  │   robotics/      │
 │ manufacturing/        │  │  OSI as engineering    │  │  kinematics/DH   │
 │  fab · lithography    │  │  modulation · fiber    │  │  sensors/actuate │
 │  CMOS · packaging     │  │  wireless · 5G         │  │  control · ROS   │
 │  Moore's Law econ.    │  │  network slicing       │  │  autonomous sys  │
 └───────────────────────┘  └────────────────────────┘  └──────────────────┘

 SYSTEMS ENGINEERING TRACK
 ┌────────────────────────┐  ┌────────────────────────┐  ┌────────────────────┐
 │  biomedical-           │  │   formal-methods/      │  │ systems-           │
 │  engineering/          │  │  logic · model check   │  │ engineering/       │
 │  biomechanics · devices│  │  SAT/SMT solvers       │  │  SE process/MBSE   │
 │  imaging · biosignals  │  │  Hoare logic           │  │  requirements      │
 │  tissue engineering    │  │  proof assistants      │  │  V-model · FMEA    │
 └────────────────────────┘  └────────────────────────┘  └────────────────────┘

 INFRASTRUCTURE & ENVIRONMENT TRACK
 ┌────────────────────────┐  ┌──────────────────────────────────────────────┐
 │   urban-planning/      │  │        environmental-engineering/            │
 │  land use/zoning       │  │  water/air treatment · remediation           │
 │  transportation plan.  │  │  sustainability · LCA · climate metrics      │
 │  housing · design      │  └──────────────────────────────────────────────┘
 └────────────────────────┘
 ┌────────────────────────────────────────────────────────────────────────────┐
 │                         materials-processing/                              │
 │  TTT/CCT diagrams · heat treatment · solidification · fracture mechanics  │
 │  fatigue · deformation processing · surface treatments · characterization │
 └────────────────────────────────────────────────────────────────────────────┘

 BATCH 12 (planned)
 ┌───────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐
 │  nanotechnology/  │  │  energy-storage/ │  │  infrastructure-systems/ │
 │  nanofab · MEMS   │  │  batteries · H2  │  │  grid · water · telecom  │
 │  nanomaterials    │  │  supercapacitors │  │  resilience · interdep.  │
 └───────────────────┘  └──────────────────┘  └──────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| [`semiconductor-manufacturing/`](../semiconductor-manufacturing/00-OVERVIEW.md) | Fab process flow, photolithography/EUV, CMOS device physics, advanced packaging (chiplets/HBM), Moore's Law economics | [`01-FAB-PROCESS.md`](../semiconductor-manufacturing/01-FAB-PROCESS.md) | `electronics/` · `computing/` |
| [`telecommunications/`](../telecommunications/00-OVERVIEW.md) | OSI as engineering substrate, modulation (QAM/OFDM), fiber optics (WDM), wireless (MIMO), 4G/5G, network slicing | [`01-OSI-ENGINEERING.md`](../telecommunications/01-OSI-ENGINEERING.md) | `signal-processing/` · `electrical-grid/` |
| [`robotics/`](../robotics/00-OVERVIEW.md) | Kinematics (DH parameters), rigid body dynamics, sensors/actuators, control (PID→MPC), ROS, manipulation, autonomous systems | [`01-KINEMATICS.md`](../robotics/01-KINEMATICS.md) | `control-theory/` · `signal-processing/` |
| [`biomedical-engineering/`](../biomedical-engineering/00-OVERVIEW.md) | Biomechanics, medical device design (regulatory/biocompatibility), medical imaging (X-ray/CT/MRI/US), biosignals, tissue engineering | [`01-BIOMECHANICS.md`](../biomedical-engineering/01-BIOMECHANICS.md) | `mechanical/` · `electronics/` · `medicine/` |
| [`formal-methods/`](../formal-methods/00-OVERVIEW.md) | Propositional/predicate logic, temporal logic (LTL/CTL), model checking, SAT/SMT, Hoare logic, proof assistants (Coq/Lean) | [`01-LOGIC.md`](../formal-methods/01-LOGIC.md) | `mathematics/` · `languages/` · `computing/` |
| [`systems-engineering/`](../systems-engineering/00-OVERVIEW.md) | SE process/lifecycle, requirements engineering, system architecture/trade studies, V-model, SysML, FMEA, MBSE | [`01-SE-PROCESS.md`](../systems-engineering/01-SE-PROCESS.md) | `formal-methods/` · `robotics/` |
| [`urban-planning/`](../urban-planning/00-OVERVIEW.md) | Land use/zoning (Euclidean→form-based), transportation planning (LOS/VMT), housing policy, urban design | [`01-LAND-USE.md`](../urban-planning/01-LAND-USE.md) | `transportation/` · `environmental-engineering/` |
| [`environmental-engineering/`](../environmental-engineering/00-OVERVIEW.md) | Water/wastewater treatment, air pollution control, site remediation, lifecycle assessment (LCA), sustainability metrics | [`01-WATER-TREATMENT.md`](../environmental-engineering/01-WATER-TREATMENT.md) | `chemical-eng/` · `urban-planning/` |
| [`materials-processing/`](../materials-processing/00-OVERVIEW.md) | TTT/CCT diagrams, heat treatment, solidification, fracture mechanics, fatigue, deformation processing, surface treatments, characterization | [`01-PHASE-TRANSFORMATIONS.md`](../materials-processing/01-PHASE-TRANSFORMATIONS.md) | `materials/` · `manufacturing/` |

---

## Volume Plan

| Volume | Directories | Target |
|--------|-------------|--------|
| T·I | semiconductor-manufacturing/ · telecommunications/ · robotics/ | ~240 pp |
| T·II | biomedical-engineering/ · formal-methods/ · systems-engineering/ | ~220 pp |
| T·III | urban-planning/ · environmental-engineering/ · materials-processing/ | ~210 pp |
| T·IV | *Batch 12: nanotechnology/ · energy-storage/ · infrastructure-systems/* | ~200 pp |

---

## Paths

### Silicon to systems
`semiconductor-manufacturing/` → `telecommunications/` → `robotics/` → `systems-engineering/`
*The transistor enables the wireless protocol enables the autonomous robot — and systems engineering is what keeps the whole stack coherent as complexity scales.*

### Formal correctness track
`formal-methods/` → `systems-engineering/` → `robotics/`
*Logic and proof theory applied to system verification, then to the design of complex engineered systems, then to autonomous robots where correctness is safety-critical.*

### Built-environment sustainability
`urban-planning/` → `environmental-engineering/` → `materials-processing/`
*Planning cities requires designing their environmental infrastructure; building that infrastructure requires understanding how materials behave under processing and service conditions.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Mechanics | Technology picks up where Mechanics ends. `semiconductor-manufacturing/` is downstream of `electrical-grid/`. `robotics/` builds on `mechanical/` dynamics and `transportation/` AV context. `materials-processing/` extends `construction-materials/` into metallurgical depth. |
| Mathematics & Physics | `control-theory/` is the mathematical engine inside `robotics/` and process control. `signal-processing/` underlies `telecommunications/` and sensor fusion in `robotics/`. `formal-methods/` connects directly to mathematical logic. |
| Computing & Software | `semiconductor-manufacturing/` is the physical layer `computing/` runs on. `formal-methods/` connects to type theory in `languages/` and software verification in `computing/`. `robotics/` consumes the software stack (ROS, real-time OS, sensor fusion). |
