# Engineering

20 directories · Applied physical and systems engineering — from structural mechanics to autonomous systems

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
 └─────────────────────────────┘                                     │  verification      │
                                                                      └────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `mechanical/` | Statics (free body diagrams, equilibrium), dynamics (kinematics, Newton-Euler), stress/strain (Hooke's law, Mohr's circle), machine elements (gears, bearings, fasteners), tribology, thermodynamic cycles | `01-STATICS.md` — forces, moments, trusses | `structural/` for applied load analysis; `materials/` for material selection |
| `structural/` | Beam theory (Euler-Bernoulli, shear/moment diagrams), truss/frame analysis, column buckling (Euler), seismic loads, load path tracing, code compliance basics | `01-BEAMS.md` — bending, shear, deflection | `mechanical/` for mechanics substrate; `construction-materials/` for material properties |
| `aeronautics/` | Aerodynamics (lift/drag/boundary layer), propulsion (Brayton cycle, thrust equations), 6-DOF flight mechanics (stability derivatives), avionics architecture, aeroelasticity (flutter) | `01-AERODYNAMICS.md` — airfoil theory through boundary layer | `mechanical/` for dynamics; `physics/` for fluid mechanics foundations |
| `chemical-eng/` | Transport phenomena (heat/mass/momentum transfer), reaction engineering (CSTR/PFR), separation processes (distillation, extraction), process control, P&IDs | `01-TRANSPORT.md` — the transport analogy across heat/mass/momentum | `materials/` for process-material interaction; `nuclear/` for reactor thermal-hydraulics |
| `nuclear/` | Fission/fusion physics, reactor neutronics (criticality, multiplication factor), thermal-hydraulics, radiation shielding (attenuation, dose), waste classification and disposal | `01-FISSION-FUSION.md` — binding energy through chain reactions | `physics/` for nuclear quantum mechanics; `chemical-eng/` for thermal-hydraulics |
| `energy-systems/` | Fossil generation (Rankine/Brayton), nuclear generation, renewables (solar PV/CSP, wind, hydro), grid integration challenges, energy storage (batteries, pumped hydro, hydrogen), energy transitions | `01-FOSSIL-GENERATION.md` — heat engine thermodynamics through plant ops | `electrical-grid/` for transmission/distribution; `chemical-eng/` for process side |
| `electrical-grid/` | Power generation coupling, transmission (AC/DC, HVDC), distribution (substations, feeders), SCADA and EMS, smart grid and AMI, protection systems (relays, breakers), power quality | `01-GENERATION.md` — synchronous machines and grid coupling | `energy-systems/` for generation side; `electronics/` (Math & Physics) for circuit foundations |
| `hvac/` | Psychrometrics (air-water vapor), refrigeration cycle (vapor compression), heat pump operation, chiller/AHU/VAV system design, ductwork sizing, building automation and controls | `01-PSYCHROMETRICS.md` — the Mollier diagram and air-water properties | `mechanical/` for thermodynamic cycles; `plumbing/` for hydronic systems |
| `plumbing/` | Water supply systems (pressure, pipe sizing), drain/waste/vent (DWV) design, pipe materials (copper/PEX/CPVC), water quality and treatment, plumbing codes and inspection | `01-SUPPLY-SYSTEMS.md` — pressure, flow, Bernoulli applied | `hvac/` for hydronic integration; `environmental-engineering/` for water quality |
| `construction-materials/` | Concrete (Portland cement chemistry, mix design, reinforcement, prestress), structural steel (grades, connections, weld/bolt), timber (grading, engineered wood), masonry, fiber-reinforced composites | `01-CONCRETE.md` — Portland cement hydration through structural concrete | `structural/` for structural application; `materials/` (Math & Physics) for materials science substrate |
| `urban-planning/` | Land use and zoning (Euclidean through form-based), transportation planning (LOS, modal split, VMT), housing policy (supply/demand, affordability, inclusionary), urban design principles | `01-LAND-USE.md` — zoning history through contemporary mixed-use | `transportation/` for mobility systems; `environmental-engineering/` for sustainability overlay |
| `transportation/` | Modes and modal comparison (road/rail/air/sea), infrastructure design, logistics and freight, autonomous vehicles (sensor stack, decision layers), transportation policy and funding | `01-MODES.md` — modal characteristics and infrastructure comparison | `urban-planning/` for land-use coupling; `robotics/` for AV systems |
| `environmental-engineering/` | Water treatment (coagulation/filtration/disinfection), wastewater treatment (activated sludge, nutrient removal), air pollution control, site remediation, lifecycle assessment (LCA), sustainability metrics | `01-WATER-TREATMENT.md` — source water through distribution | `chemical-eng/` for process engineering; `urban-planning/` for infrastructure context |
| `semiconductor-manufacturing/` | Fab process flow (oxidation, lithography, doping, metallization), photolithography and EUV, CMOS device physics, advanced packaging (chiplets, HBM), Moore's Law economics and roadmap | `01-FAB-PROCESS.md` — wafer to die process flow overview | `electronics/` (Math & Physics) for device physics; `computing/` (Computing) for the software stack on top |
| `telecommunications/` | OSI stack as engineering substrate, modulation schemes (QAM, OFDM), fiber optics (single/multi-mode, WDM), wireless fundamentals (path loss, MIMO), 4G/5G architecture, network slicing | `01-OSI-ENGINEERING.md` — physical through transport layers as engineering systems | `signal-processing/` (Math & Physics) for modulation math; `electrical-grid/` for infrastructure parallels |
| `acoustics/` | Wave propagation (reflection, refraction, diffraction, absorption), room acoustics (RT60, modes, diffusion), noise control engineering, transducers (microphones/speakers), psychoacoustics | `01-WAVE-PROPAGATION.md` — acoustic wave equation through impedance | `signal-processing/` (Math & Physics) for Fourier treatment of sound; `physics/` for wave mechanics |
| `optics/` | Geometrical optics (ray tracing, lenses, aberrations), physical optics (interference, diffraction, polarization), laser physics (stimulated emission, cavity modes), fiber optics, imaging systems, photonics | `01-GEOMETRICAL-OPTICS.md` — Snell's law through first-order system design | `physics/` for electromagnetic wave foundations; `telecommunications/` for fiber application |
| `robotics/` | Kinematics (DH parameters, forward/inverse), rigid body dynamics, sensors (LiDAR/IMU/vision), actuators, control architectures (PID through MPC), ROS architecture, manipulation planning, autonomous systems | `01-KINEMATICS.md` — rotation matrices through DH convention | `control-theory/` (Math & Physics) for control substrate; `signal-processing/` for sensor fusion |
| `biomedical-engineering/` | Biomechanics (bone/soft tissue, joint mechanics), medical device design (regulatory pathway, biocompatibility), medical imaging (X-ray/CT/MRI/US physics), biosignals (ECG/EEG/EMG), tissue engineering | `01-BIOMECHANICS.md` — continuum mechanics applied to biological tissues | `mechanical/` for mechanics; `electronics/` for instrumentation; `medicine/` for clinical context |
| `formal-methods/` | Propositional and predicate logic, temporal logic (LTL/CTL), model checking (SPIN, NuSMV), SAT/SMT solvers, Hoare logic and program verification, dependent type theory, proof assistants (Coq/Lean) | `01-LOGIC.md` — propositional logic through first-order logic | `mathematics/` (Math & Physics) for formal foundations; `languages/` (Computing) for type systems; `computing/` for software verification application |

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
