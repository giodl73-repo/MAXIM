# Engineering

23 directories · Applied physical and systems engineering — from structural mechanics to autonomous systems

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                    ENGINEERING                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘

 CLASSICAL MECHANICS TRACK
 ┌────────────────┐   ┌────────────────┐   ┌──────────────────────────┐
 │  mechanical/   │   │  structural/   │   │      aeronautics/        │
 │  statics       │   │  beams/trusses │   │  aerodynamics            │
 │  dynamics      │   │  frames        │   │  Brayton cycle           │
 │  stress/strain │   │  buckling      │   │  6-DOF flight mechanics  │
 │  machine elem. │   │  seismic       │   │  avionics · aeroelastic  │
 │  tribology     │   │  load paths    │   └──────────────────────────┘
 └────────────────┘   └────────────────┘
          │                   │
          └─────────┬─────────┘
                    ▼
 ENERGY & SYSTEMS TRACK
 ┌──────────────┐  ┌────────────┐  ┌──────────────────┐  ┌──────────────────┐
 │ chemical-eng/│  │  nuclear/  │  │  energy-systems/ │  │  electrical-grid/│
 │  transport   │  │  fission / │  │  fossil/nuke/    │  │  generation      │
 │  phenomena   │  │  fusion    │  │  renewable gen   │  │  transmission    │
 │  reaction    │  │  reactor   │  │  grid integration│  │  distribution    │
 │  engineering │  │  physics   │  │  storage         │  │  SCADA · protect │
 │  separations │  │  shielding │  │  transitions     │  │  smart grid      │
 └──────────────┘  └────────────┘  └──────────────────┘  └──────────────────┘

 BUILT ENVIRONMENT TRACK
 ┌──────────┐  ┌────────────┐  ┌─────────────────────┐  ┌───────────────────┐
 │   hvac/  │  │ plumbing/  │  │ construction-       │  │  urban-planning/  │
 │  thermo  │  │  supply/   │  │ materials/          │  │  land use/zoning  │
 │  refrig. │  │  DWV       │  │  concrete · steel   │  │  transportation   │
 │  heat    │  │  pipe mat. │  │  wood · masonry     │  │  planning         │
 │  pumps   │  │  codes     │  │  composites         │  │  housing          │
 │  controls│  │  quality   │  └─────────────────────┘  └───────────────────┘
 └──────────┘  └────────────┘
 ┌───────────────────────────┐  ┌──────────────────────────────────────────┐
 │      transportation/      │  │        environmental-engineering/        │
 │  modes · infrastructure   │  │  water/air treatment · remediation       │
 │  logistics · AV · policy  │  │  sustainability · LCA                    │
 └───────────────────────────┘  └──────────────────────────────────────────┘

 SIGNALS & SYSTEMS TRACK
 ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────┐  ┌────────┐
 │ semiconductor-       │  │  telecommunications/ │  │ acoustics│  │ optics/│
 │ manufacturing/       │  │  protocols           │  │  wave    │  │  geo/  │
 │  fab · lithography   │  │  modulation          │  │  prop.   │  │  phys  │
 │  CMOS · packaging    │  │  fiber · wireless    │  │  room    │  │  laser │
 │  Moore's Law econ.   │  │  5G · net arch.      │  │  trans-  │  │  fiber │
 └──────────────────────┘  └──────────────────────┘  │  ducers  │  │  photo-│
                                                      └──────────┘  │  nics  │
                                                                     └────────┘
 EMERGING ENGINEERING
 ┌─────────────────────────────┐  ┌──────────────────────────────┐  ┌────────────────────┐
 │         robotics/           │  │   biomedical-engineering/    │  │  formal-methods/   │
 │  kinematics · dynamics      │  │  biomechanics · devices      │  │  logic · model     │
 │  sensors/actuators          │  │  imaging · biosignals        │  │  checking          │
 │  control · ROS              │  │  tissue engineering          │  │  theorem proving   │
 │  manipulation · autonomous  │  └──────────────────────────────┘  │  type theory       │
 └─────────────────────────────┘                                     │  verification     │
                                                                      └────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| [mechanical/](../mechanical/00-OVERVIEW.md) | Statics (free body diagrams, equilibrium), dynamics (kinematics, Newton-Euler), stress/strain (Hooke's law, Mohr's circle), machine elements (gears, bearings, fasteners), tribology, thermodynamic cycles | [01-THERMODYNAMICS.md](../mechanical/01-THERMODYNAMICS.md) — forces, moments, trusses | `structural/` for applied load analysis; `materials/` for material selection |
| [structural/](../structural/00-OVERVIEW.md) | Beam theory (Euler-Bernoulli, shear/moment diagrams), truss/frame analysis, column buckling (Euler), seismic loads, load path tracing, code compliance basics | [01-STATICS.md](../structural/01-STATICS.md) — bending, shear, deflection | `mechanical/` for mechanics substrate; `construction-materials/` for material properties |
| [aeronautics/](../aeronautics/00-OVERVIEW.md) | Aerodynamics (lift/drag/boundary layer), propulsion (Brayton cycle, thrust equations), 6-DOF flight mechanics (stability derivatives), avionics architecture, aeroelasticity (flutter) | [01-AERODYNAMICS.md](../aeronautics/01-AERODYNAMICS.md) — airfoil theory through boundary layer | `mechanical/` for dynamics; `physics/` for fluid mechanics foundations |
| [chemical-eng/](../chemical-eng/00-OVERVIEW.md) | Transport phenomena (heat/mass/momentum transfer), reaction engineering (CSTR/PFR), separation processes (distillation, extraction), process control, P&IDs | [01-THERMO.md](../chemical-eng/01-THERMO.md) — the transport analogy across heat/mass/momentum | `materials/` for process-material interaction; `nuclear/` for reactor thermal-hydraulics |
| [nuclear/](../nuclear/00-OVERVIEW.md) | Fission/fusion physics, reactor neutronics (criticality, multiplication factor), thermal-hydraulics, radiation shielding (attenuation, dose), waste classification and disposal | [01-NUCLEAR-PHYSICS.md](../nuclear/01-NUCLEAR-PHYSICS.md) — binding energy through chain reactions | `physics/` for nuclear quantum mechanics; `chemical-eng/` for thermal-hydraulics |
| [energy-systems/](../energy-systems/00-OVERVIEW.md) | Fossil generation (Rankine/Brayton), nuclear generation, renewables (solar PV/CSP, wind, hydro), grid integration challenges, energy storage (batteries, pumped hydro, hydrogen), energy transitions | [01-SOLAR-PV.md](../energy-systems/01-SOLAR-PV.md) — heat engine thermodynamics through plant ops | `electrical-grid/` for transmission/distribution; `chemical-eng/` for process side |
| [electrical-grid/](../electrical-grid/00-OVERVIEW.md) | Power generation coupling, transmission (AC/DC, HVDC), distribution (substations, feeders), SCADA and EMS, smart grid and AMI, protection systems (relays, breakers), power quality | [01-GENERATION.md](../electrical-grid/01-GENERATION.md) — synchronous machines and grid coupling | `energy-systems/` for generation side; `electronics/` (Math & Physics) for circuit foundations |
| [hvac/](../hvac/00-OVERVIEW.md) | Psychrometrics (air-water vapor), refrigeration cycle (vapor compression), heat pump operation, chiller/AHU/VAV system design, ductwork sizing, building automation and controls | [01-THERMODYNAMICS.md](../hvac/01-THERMODYNAMICS.md) — the Mollier diagram and air-water properties | `mechanical/` for thermodynamic cycles; `plumbing/` for hydronic systems |
| [plumbing/](../plumbing/00-OVERVIEW.md) | Water supply systems (pressure, pipe sizing), drain/waste/vent (DWV) design, pipe materials (copper/PEX/CPVC), water quality and treatment, plumbing codes and inspection | [01-HISTORY.md](../plumbing/01-HISTORY.md) — pressure, flow, Bernoulli applied | `hvac/` for hydronic integration; `environmental-engineering/` for water quality |
| [construction-materials/](../construction-materials/00-OVERVIEW.md) | Concrete (Portland cement chemistry, mix design, reinforcement, prestress), structural steel (grades, connections, weld/bolt), timber (grading, engineered wood), masonry, fiber-reinforced composites | [01-PREHISTORIC-VERNACULAR.md](../construction-materials/01-PREHISTORIC-VERNACULAR.md) — Portland cement hydration through structural concrete | `structural/` for structural application; `materials/` (Math & Physics) for materials science substrate |
| [urban-planning/](../urban-planning/00-OVERVIEW.md) | Land use and zoning (Euclidean through form-based), transportation planning (LOS, modal split, VMT), housing policy (supply/demand, affordability, inclusionary), urban design principles | [01-LAND-USE.md](../urban-planning/01-LAND-USE.md) — zoning history through contemporary mixed-use | `transportation/` for mobility systems; `environmental-engineering/` for sustainability overlay |
| [transportation/](../transportation/00-OVERVIEW.md) | Modes and modal comparison (road/rail/air/sea), infrastructure design, logistics and freight, autonomous vehicles (sensor stack, decision layers), transportation policy and funding | [01-RAIL.md](../transportation/01-RAIL.md) — modal characteristics and infrastructure comparison | `urban-planning/` for land-use coupling; `robotics/` for AV systems |
| [environmental-engineering/](../environmental-engineering/00-OVERVIEW.md) | Water treatment (coagulation/filtration/disinfection), wastewater treatment (activated sludge, nutrient removal), air pollution control, site remediation, lifecycle assessment (LCA), sustainability metrics | [01-WATER-TREATMENT.md](../environmental-engineering/01-WATER-TREATMENT.md) — source water through distribution | `chemical-eng/` for process engineering; `urban-planning/` for infrastructure context |
| [semiconductor-manufacturing/](../semiconductor-manufacturing/00-OVERVIEW.md) | Fab process flow (oxidation, lithography, doping, metallization), photolithography and EUV, CMOS device physics, advanced packaging (chiplets, HBM), Moore's Law economics and roadmap | [01-SILICON-SUBSTRATE.md](../semiconductor-manufacturing/01-SILICON-SUBSTRATE.md) — wafer to die process flow overview | `electronics/` (Math & Physics) for device physics; `computing/` (Computing) for the software stack on top |
| [telecommunications/](../telecommunications/00-OVERVIEW.md) | OSI stack as engineering substrate, modulation schemes (QAM, OFDM), fiber optics (single/multi-mode, WDM), wireless fundamentals (path loss, MIMO), 4G/5G architecture, network slicing | [01-ELECTROMAGNETIC-SPECTRUM.md](../telecommunications/01-ELECTROMAGNETIC-SPECTRUM.md) — physical through transport layers as engineering systems | `signal-processing/` (Math & Physics) for modulation math; `electrical-grid/` for infrastructure parallels |
| [acoustics/](../acoustics/00-OVERVIEW.md) | Wave propagation (reflection, refraction, diffraction, absorption), room acoustics (RT60, modes, diffusion), noise control engineering, transducers (microphones/speakers), psychoacoustics | [01-WAVE-PHYSICS.md](../acoustics/01-WAVE-PHYSICS.md) — acoustic wave equation through impedance | `signal-processing/` (Math & Physics) for Fourier treatment of sound; `physics/` for wave mechanics |
| [optics/](../optics/00-OVERVIEW.md) | Geometrical optics (ray tracing, lenses, aberrations), physical optics (interference, diffraction, polarization), laser physics (stimulated emission, cavity modes), fiber optics, imaging systems, photonics | [01-GEOMETRIC-OPTICS.md](../optics/01-GEOMETRIC-OPTICS.md) — Snell's law through first-order system design | `physics/` for electromagnetic wave foundations; `telecommunications/` for fiber application |
| [robotics/](../robotics/00-OVERVIEW.md) | Kinematics (DH parameters, forward/inverse), rigid body dynamics, sensors (LiDAR/IMU/vision), actuators, control architectures (PID through MPC), ROS architecture, manipulation planning, autonomous systems | [01-KINEMATICS.md](../robotics/01-KINEMATICS.md) — rotation matrices through DH convention | `control-theory/` (Math & Physics) for control substrate; `signal-processing/` for sensor fusion |
| [biomedical-engineering/](../biomedical-engineering/00-OVERVIEW.md) | Biomechanics (bone/soft tissue, joint mechanics), medical device design (regulatory pathway, biocompatibility), medical imaging (X-ray/CT/MRI/US physics), biosignals (ECG/EEG/EMG), tissue engineering | [01-BIOMECHANICS.md](../biomedical-engineering/01-BIOMECHANICS.md) — continuum mechanics applied to biological tissues | `mechanical/` for mechanics; `electronics/` for instrumentation; `medicine/` for clinical context |
| [formal-methods/](../formal-methods/00-OVERVIEW.md) | Propositional and predicate logic, temporal logic (LTL/CTL), model checking (SPIN, NuSMV), SAT/SMT solvers, Hoare logic and program verification, dependent type theory, proof assistants (Coq/Lean) | [01-LOGIC-FOUNDATIONS.md](../formal-methods/01-LOGIC-FOUNDATIONS.md) — propositional logic through first-order logic | `mathematics/` (Math & Physics) for formal foundations; `languages/` (Computing) for type systems; `computing/` for software verification application |
| [manufacturing/](../manufacturing/00-OVERVIEW.md) | The science and economics of making things: GD&T and tolerancing (ASME Y14.5 — the language of engineering drawings), machining (chip formation, tool geometry, speeds/feeds), CNC and CAM programming, additive manufacturing (FDM/SLA/DMLS — how each builds layer by layer and what it means for design), casting and bulk forming processes, lean manufacturing and the Toyota Production System (7 wastes, kaizen, JIT), quality systems (SPC, Six Sigma, ISO 9001), Industry 4.0 (cyber-physical systems, digital twin, OPC-UA) | [01-GDT-TOLERANCING.md](../manufacturing/01-GDT-TOLERANCING.md) — GD&T first, the shared language of all manufacturing drawings | `materials-processing/` for the metallurgy that enables heat treatment of manufactured parts; `robotics/` for automation; `systems-engineering/` for the systems context |
| [systems-engineering/](../systems-engineering/00-OVERVIEW.md) | The discipline of designing complex systems: SE process and lifecycle (concept through disposal), requirements engineering (functional/non-functional, DOORS-style management), system architecture and trade studies (Pugh matrix, AHP), the V-model and verification/validation distinction, SysML (block definition diagrams, activity diagrams, parametrics), FMEA and fault tree analysis, interface management and ICDs, MBSE with tools like Cameo/Rhapsody. VP-relevant: systems engineering is how large organizations build discipline around complexity — the same problems as large software systems | [01-SE-PROCESS.md](../systems-engineering/01-SE-PROCESS.md) — the systems engineering process and lifecycle framing | Engineering for implementation; `formal-methods/` for model-checking connections; `robotics/` and `aerospace/` as heavy SE consumers |
| [materials-processing/](../materials-processing/00-OVERVIEW.md) | The bridge between materials science and manufacturing: TTT (time-temperature-transformation) and CCT diagrams for steel heat treatment, heat treatment processes (annealing, normalizing, quenching, tempering — each moves you on the TTT diagram), solidification and casting metallurgy (grain structure, segregation, porosity), deformation processing (why hot rolling produces different microstructure than cold rolling — recrystallization vs. work hardening), fracture mechanics (Griffith criterion, stress intensity factor K, fracture toughness), fatigue (S-N curves, Paris law for crack growth), surface treatments, polymer processing, materials characterization (SEM/XRD/EBSD) | [01-PHASE-TRANSFORMATIONS.md](../materials-processing/01-PHASE-TRANSFORMATIONS.md) — TTT diagrams and why heat treatment works | `materials/` (Math & Physics) for the science substrate; `manufacturing/` for the production context; `construction-materials/` for concrete and steel applications |

---

## Paths

### Infrastructure systems integration
`mechanical/` → `structural/` → `construction-materials/` → `urban-planning/`
*The mechanics and materials of individual structural elements compose into buildings, which compose into the urban fabric — this path traces how engineering decisions aggregate into cities.*

### Energy system vertical
`physics/` (Math & Physics) → `chemical-eng/` → `energy-systems/` → `electrical-grid/`
*Thermodynamic first principles through process engineering through generation through delivery — the full chain from combustion or fission to a socket.*

### Signals-to-systems track
`semiconductor-manufacturing/` → `electronics/` (Math & Physics) → `telecommunications/` → `robotics/`
*From the transistor to circuits to wireless protocols to autonomous systems that use them — the ascending stack from silicon to autonomy.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Mathematics & Physics | `signal-processing/` is the mathematical substrate for `acoustics/`, `telecommunications/`, and `optics/`. `control-theory/` is the mathematical engine inside `robotics/` and process control in `chemical-eng/`. `physics/` provides the field equations for `electronics/`, `materials/`, and the wave mechanics in `acoustics/` and `optics/`. |
| Computing & Software | `semiconductor-manufacturing/` is the physical layer that `computing/` runs on. `formal-methods/` connects directly to `languages/` type theory and software verification in `computing/`. `robotics/` consumes the software stack — ROS, real-time OS, sensor fusion algorithms. |
| Earth & Space | `environmental-engineering/` shares water cycle and atmospheric chemistry context with Earth sciences. Hydrology and oceanography in that section provide the natural-system context for engineered water and coastal infrastructure. |
