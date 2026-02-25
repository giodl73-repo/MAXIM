# Mechanics

*14 directories · ~1,000 pages · M·I, M·II, M·III, M·IV*

Classical engineering — from antiquity through the Industrial Revolution. Mechanics covers the manipulation of force, energy, matter, and material across every domain that predates the electronic age: the lever and the arch, the steam turbine and the bridge girder, the heat exchanger and the municipal water main.

The word is ancient: *mēkhanikē* (Greek) — the art of machines. By the 19th century Mechanics Institutes and university departments formalized it. MIT named itself "Institute of Technology" (1861) to signal that it would teach both the classical mechanical tradition and whatever came next. This section is the classical tradition.

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                  MECHANICS                                  │
│         Classical engineering — antiquity through Industrial Revolution     │
└─────────────────────────────────────────────────────────────────────────────┘

 SOLID MECHANICS TRACK
 ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────────────────┐
 │  mechanical/    │   │  structural/    │   │      aeronautics/           │
 │  statics        │   │  beams/trusses  │   │  aerodynamics               │
 │  dynamics       │   │  frames/shells  │   │  propulsion (Brayton)       │
 │  stress/strain  │   │  column buckling│   │  6-DOF flight mechanics     │
 │  machine elem.  │   │  seismic loads  │   │  avionics · aeroelasticity  │
 │  tribology      │   │  load paths     │   └─────────────────────────────┘
 └─────────────────┘   └─────────────────┘

 PROCESS & ENERGY TRACK
 ┌──────────────┐  ┌───────────┐  ┌──────────────────┐  ┌──────────────────┐
 │ chemical-eng/│  │  nuclear/ │  │  energy-systems/ │  │ electrical-grid/ │
 │  transport   │  │  fission/ │  │  fossil/nuke/    │  │  generation      │
 │  phenomena   │  │  fusion   │  │  renewable gen   │  │  transmission    │
 │  reaction    │  │  reactor  │  │  grid integration│  │  distribution    │
 │  engineering │  │  physics  │  │  storage         │  │  SCADA · protect │
 │  separations │  │  shielding│  │  transitions     │  │  smart grid      │
 └──────────────┘  └───────────┘  └──────────────────┘  └──────────────────┘

 BUILT ENVIRONMENT TRACK
 ┌──────────┐  ┌────────────┐  ┌────────────────────┐
 │   hvac/  │  │ plumbing/  │  │ construction-      │
 │  thermo  │  │  supply/   │  │ materials/         │
 │  refrig. │  │  DWV       │  │  concrete · steel  │
 │  heat    │  │  pipe mat. │  │  wood · masonry    │
 │  pumps   │  │  codes     │  │  composites        │
 │  controls│  │  quality   │  └────────────────────┘
 └──────────┘  └────────────┘

 WAVE & PRODUCTION TRACK
 ┌────────────┐  ┌──────────┐  ┌───────────────────────┐  ┌──────────────────────┐
 │ acoustics/ │  │ optics/  │  │    transportation/    │  │   manufacturing/     │
 │  wave prop │  │  geo/    │  │  modes · infra        │  │  GD&T · machining    │
 │  room acst │  │  phys    │  │  logistics · AV       │  │  CNC · additive      │
 │  noise ctrl│  │  laser   │  │  policy · funding     │  │  lean · TPS · SPC    │
 │  transducrs│  │  fiber   │  └───────────────────────┘  └──────────────────────┘
 └────────────┘  └──────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| [`mechanical/`](../mechanical/00-OVERVIEW.md) | Statics, dynamics, stress/strain, machine elements, tribology, thermodynamic cycles | `01-STATICS.md` | `structural/` · `materials/` |
| [`structural/`](../structural/00-OVERVIEW.md) | Beam theory, truss/frame analysis, column buckling, seismic loads, load path tracing | `01-BEAMS.md` | `mechanical/` · `construction-materials/` |
| [`aeronautics/`](../aeronautics/00-OVERVIEW.md) | Aerodynamics, Brayton propulsion, 6-DOF flight mechanics, avionics, aeroelasticity | `01-AERODYNAMICS.md` | `mechanical/` · `physics/` |
| [`chemical-eng/`](../chemical-eng/00-OVERVIEW.md) | Transport phenomena, reaction engineering (CSTR/PFR), separation processes, process control | `01-TRANSPORT.md` | `materials/` · `nuclear/` |
| [`nuclear/`](../nuclear/00-OVERVIEW.md) | Fission/fusion physics, reactor neutronics, thermal-hydraulics, shielding, waste | `01-FISSION-FUSION.md` | `physics/` · `chemical-eng/` |
| [`energy-systems/`](../energy-systems/00-OVERVIEW.md) | Fossil/nuclear/renewable generation, grid integration, energy storage, energy transitions | `01-FOSSIL-GENERATION.md` | `electrical-grid/` · `chemical-eng/` |
| [`electrical-grid/`](../electrical-grid/00-OVERVIEW.md) | Power generation coupling, AC/DC transmission, SCADA/EMS, smart grid, protection systems | `01-GENERATION.md` | `energy-systems/` · `electronics/` |
| [`hvac/`](../hvac/00-OVERVIEW.md) | Psychrometrics, refrigeration cycle, heat pumps, AHU/VAV systems, building automation | `01-PSYCHROMETRICS.md` | `mechanical/` · `plumbing/` |
| [`plumbing/`](../plumbing/00-OVERVIEW.md) | Water supply, DWV design, pipe materials, water quality, plumbing codes | `01-SUPPLY-SYSTEMS.md` | `hvac/` · `environmental-engineering/` |
| [`construction-materials/`](../construction-materials/00-OVERVIEW.md) | Concrete, structural steel, timber, masonry, fiber-reinforced composites | `01-CONCRETE.md` | `structural/` · `materials/` |
| [`acoustics/`](../acoustics/00-OVERVIEW.md) | Wave propagation, room acoustics (RT60), noise control, transducers, psychoacoustics | `01-WAVE-PROPAGATION.md` | `signal-processing/` · `physics/` |
| [`optics/`](../optics/00-OVERVIEW.md) | Geometrical and physical optics, laser physics, fiber optics, imaging systems, photonics | `01-GEOMETRICAL-OPTICS.md` | `physics/` · `telecommunications/` |
| [`transportation/`](../transportation/00-OVERVIEW.md) | Modes, infrastructure design, logistics, autonomous vehicles, transportation policy | `01-MODES.md` | `urban-planning/` · `robotics/` |
| [`manufacturing/`](../manufacturing/00-OVERVIEW.md) | GD&T/tolerancing, machining, CNC/CAM, additive manufacturing, lean/TPS, Industry 4.0 | `01-GDT-TOLERANCING.md` | `materials-processing/` · `robotics/` |

---

## Volume Plan

| Volume | Directories | Target |
|--------|-------------|--------|
| M·I | mechanical/ · structural/ · aeronautics/ | ~260 pp |
| M·II | chemical-eng/ · nuclear/ · energy-systems/ | ~260 pp |
| M·III | electrical-grid/ · hvac/ · plumbing/ · construction-materials/ | ~260 pp |
| M·IV | acoustics/ · optics/ · transportation/ · manufacturing/ | ~260 pp |

---

## Paths

### Infrastructure vertical
`mechanical/` → `structural/` → `construction-materials/` → `manufacturing/`
*The mechanics of individual elements compose into buildings, which require controlled material production — this traces how engineering decisions propagate from force analysis to factory floor.*

### Energy system chain
`physics/` (Math & Physics) → `chemical-eng/` → `energy-systems/` → `electrical-grid/`
*Thermodynamic first principles through process engineering through generation through delivery — combustion or fission to a socket.*

### Acoustic/optical physics to engineering
`physics/` → `acoustics/` → `optics/` → `telecommunications/` (Technology)
*Wave mechanics applied: sound rooms and noise cancellation, laser physics, fiber optics, and ultimately the telecom stack.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Mathematics & Physics | `signal-processing/` is the mathematical substrate for `acoustics/` and `optics/`. `control-theory/` drives process control in `chemical-eng/` and `electrical-grid/`. `physics/` provides field equations for wave mechanics throughout. |
| Technology | Technology picks up where Mechanics leaves off — the electronic age. `semiconductor-manufacturing/` is downstream of `electrical-grid/`. `robotics/` consumes `manufacturing/` and `transportation/` context. |
| Earth & Space | `environmental-engineering/` (Technology) connects to hydrology and atmospheric chemistry here. `energy-systems/` connects to climate science and resource geology. |
