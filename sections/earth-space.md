# Earth & Space

14 directories · planetary deep time through operational weather forecasting — from solar system formation to biosignature detection

---

## Landscape

```
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║  COSMIC / PLANETARY SCALE                                                             ║
║                                                                                       ║
║  ┌──────────────────────────┐   ┌──────────────────────────┐                         ║
║  │  astronomy/              │   │  geology/                 │                         ║
║  │  Earth's motions         │   │  plate tectonics          │                         ║
║  │  Milankovitch cycles     │──▶│  rock cycle               │                         ║
║  │  celestial mechanics     │   │  stratigraphy             │                         ║
║  │  stellar physics         │   │  volcanology              │                         ║
║  │  cosmology               │   │  geomorphology            │                         ║
║  └──────────────────────────┘   │  economic geology         │                         ║
║         orbital forcing ──────▶ └──────────────┬────────────┘                         ║
║                                                │ record of                             ║
║                                                ▼                                      ║
║  ┌─────────────────────────────────────────────────────────┐                         ║
║  │  paleontology/                                          │                         ║
║  │  fossil record · stratigraphy correlation · mass        │                         ║
║  │  extinctions · paleoecology · evolution evidence        │                         ║
║  └─────────────────────────────────────────────────────────┘                         ║
╠═══════════════════════════════════════════════════════════════════════════════════════╣
║  ATMOSPHERE / OCEAN SYSTEM        ← carbon, heat, and moisture move across all three ║
║                                                                                       ║
║  ┌──────────────────────┐   ┌──────────────────────┐   ┌───────────────────────┐    ║
║  │  meteorology/        │   │  climate-science/     │   │  oceanography/        │    ║
║  │  atmosphere structure│   │  carbon cycle         │   │  thermohaline circ.   │    ║
║  │  synoptic weather    │◀──│  GCMs & feedbacks     │──▶│  tides · waves        │    ║
║  │  mesoscale dynamics  │   │  tipping points       │   │  marine chemistry     │    ║
║  │  tropical cyclones   │   │  SSP pathways         │   │  deep sea             │    ║
║  │  NWP                 │   │  mitigation & geo-eng.│   │  ocean-atm coupling   │    ║
║  └──────────────────────┘   └──────────────────────┘   └───────────────────────┘    ║
║         ▲                           │                            │                    ║
║         │ feeds forecasts           │ CO₂ budget                 │ AMOC / ENSO        ║
╠═════════╪═══════════════════════════▼════════════════════════════▼════════════════════╣
║  LAND / WATER SYSTEMS                                                                 ║
║                                                                                       ║
║  ┌──────────────────────┐   ┌──────────────────────┐   ┌───────────────────────┐    ║
║  │  geography/          │   │  hydrology/           │   │  agriculture/         │    ║
║  │  physical geography  │   │  water cycle          │   │  soil science         │    ║
║  │  climate zones       │   │  surface hydrology    │   │  crop production      │    ║
║  │  ocean-atm coupling  │◀──│  groundwater          │──▶│  irrigation           │    ║
║  │  biogeography        │   │  flood hydrology      │   │  pest management      │    ║
║  │  geopolitics         │   │  water resources mgmt │   │  food systems         │    ║
║  │  economic geography  │   │                       │   │  precision agriculture│    ║
║  └──────────────────────┘   └──────────────────────┘   └───────────────────────┘    ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝

  Time axis: geology/paleontology (Ga–Ma) → astronomy (Ga–Gyr) → climate (ka–centuries)
                              → meteorology (hours–seasons) → hydrology/agriculture (days–decades)
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `astronomy/` | Earth's rotational and orbital mechanics (precession, obliquity, eccentricity), Milankovitch cycles and their climate forcing, celestial mechanics, stellar evolution (HR diagram through nucleosynthesis), cosmology (inflation, CMB, large-scale structure) | `01-EARTH-MOTIONS.md` — the planetary anchor before stellar physics; no 00-OVERVIEW | `geology/` (orbital forcing → ice ages → sea-level → stratigraphy), `climate-science/` (Milankovitch ↔ GCM boundary conditions), `physics/` (orbital mechanics, stellar interiors) |
| `geology/` | Plate tectonics (Wilson cycle, subduction, rifting), rock cycle and petrogenesis (igneous/sedimentary/metamorphic), stratigraphic principles, volcanology (eruption types, volcanic hazards), geomorphology (erosion, landscape evolution), economic geology (ore deposits, petroleum systems) | `01-PLATE-TECTONICS.md` — the structural frame everything else builds on | `astronomy/` (impact craters, planetary differentiation), `paleontology/` (stratigraphy is the shared language), `hydrology/` (rock type controls aquifer behavior), `climate-science/` (CO₂ volcanic outgassing vs. silicate weathering) |
| `meteorology/` | Atmospheric structure (troposphere–thermosphere), synoptic-scale weather analysis (fronts, pressure systems), mesoscale dynamics (convection, MCSs), tropical cyclone physics and forecasting, numerical weather prediction (NWP) — model types, data assimilation, ensemble methods | `01-ATMOSPHERE-STRUCTURE.md` — vertical structure is prerequisite for all dynamics | `climate-science/` (weather vs. climate boundary; GCMs descend from NWP models), `oceanography/` (SST forcing of ENSO, monsoons), `hydrology/` (precipitation inputs to catchment models) |
| `climate-science/` | Global carbon cycle (reservoirs, fluxes, residence times), General Circulation Models (GCM architecture, parameterizations, validation), climate feedbacks (Planck, lapse-rate, ice-albedo, cloud), tipping point cascades, IPCC SSP scenario framework, mitigation pathways, geoengineering proposals (SAI, DAC) | `01-CARBON-CYCLE.md` — the quantitative backbone before model architecture | `meteorology/` (GCMs are the physical core of NWP extended out), `oceanography/` (ocean heat uptake, carbonate chemistry), `geology/` (long-term carbon sinks), `astronomy/` (solar forcing as external driver) |
| `oceanography/` | Ocean general circulation (gyres, western boundary currents), thermohaline circulation / AMOC, tides and wave dynamics, marine chemistry (carbonate system, pH, oxygen), biological pump, deep-sea environments (hadal zones, hydrothermal vents) | `01-OCEAN-CIRCULATION.md` — circulation before chemistry or biology | `climate-science/` (AMOC as tipping element, ocean heat content), `meteorology/` (ENSO, Indian Ocean Dipole, SST teleconnections), `geology/` (mid-ocean ridges, seafloor spreading) |
| `hydrology/` | Global and catchment water cycle, surface hydrology (runoff generation, hydrograph analysis), groundwater systems (Darcy's law, aquifer types, recharge), flood hydrology (return periods, extreme value statistics), integrated water resources management | `01-WATER-CYCLE.md` — mass balance framing before process detail | `geology/` (aquifer lithology, karst), `meteorology/` (precipitation inputs), `agriculture/` (irrigation demand), `climate-science/` (drought, flood frequency shifts under warming) |
| `paleontology/` | Fossil preservation and taphonomy, biostratigraphy and index fossils, mass extinction events (Big Five + K-Pg), macroevolutionary patterns, paleoecology and ancient food webs, fossil record as evolution evidence | `01-FOSSIL-RECORD.md` — what the record preserves and what it misses, before stratigraphy | `geology/` (stratigraphy is the dating framework), `astronomy/` (bolide impact at K-Pg), `biology/` (evolutionary theory reads the paleontological record), `ecology/` (ancient community ecology) |
| `geography/` | Physical geography (landforms, climate controls, soil formation), Köppen and Thornthwaite climate zone systems, ocean-atmosphere coupling as geographic driver, biogeography (species distribution, island biogeography theory), geopolitical geography, economic geography (agglomeration, trade patterns) | `01-PHYSICAL-GEOGRAPHY.md` — the abiotic framework before biotic or human geography | `ecology/` (biome distribution = physical geography + biology), `climate-science/` (regional climate projections), `hydrology/` (watershed geography), `historical-geography/` (political boundaries over geophysical constraints) |
| `agriculture/` | Soil science (horizons, texture, CEC, organic matter dynamics), crop physiology and production systems (cereals, legumes, root crops), irrigation methods and water-use efficiency, integrated pest management, food systems analysis (supply chains, food security metrics), precision agriculture (remote sensing, variable-rate application) | `01-SOIL-SCIENCE.md` — soils underlie all crop and ecosystem productivity | `hydrology/` (irrigation, water-use efficiency, soil-water relations), `botany/` (crop physiology shares plant biology), `ecology/` (agroecosystems as modified ecosystems), `climate-science/` (agricultural vulnerability under warming scenarios) |
| `mineralogy/` | Mineral chemistry and bonding, seven crystal systems and space groups (Bragg's law / XRD), silicate framework classification (nesosilicates through tectosilicates — the rock-forming minerals), oxide/sulfide ore minerals, carbonate/phosphate minerals, physical identification properties (Mohs hardness, cleavage, luster), gemology (4Cs extensions, treatments, synthetics), economic geology (ore deposit types, critical minerals), identification methods (XRD/EMPA/polarizing microscopy) | `01-MINERAL-CHEMISTRY.md` — bonding and composition before classification | `geology/` (mineralogy is the foundation of petrology); Mathematics & Physics `materials/` (crystal structure shared language); Natural World `periodic-table/` (element distribution in minerals); Material Culture `jewelry/` (gemstones as minerals) |
| `planetary-science/` | The solar system as a comparative laboratory: solar system formation models (solar nebula theory, Nice model for outer planet migration, Grand Tack for inner system), terrestrial planet comparative planetology (Venus, Earth, Mars, Mercury — same building blocks, radically different outcomes), Venus as climate cautionary tale (runaway greenhouse mechanism), Mars geology and habitability history (liquid water evidence, magnetic field loss), giant and ice planets, small bodies (asteroid families, comets as primitive material, Kuiper Belt), exoplanet detection methods and demographics from Kepler/TESS (occurrence rates, super-Earths, hot Jupiters), habitability frameworks (circumstellar HZ, subsurface oceans) | `01-SOLAR-SYSTEM-FORMATION.md` — formation models establish the initial conditions | `astronomy/` (solar system in cosmological context); `geochemistry/` (planetary differentiation); `astrobiology/` (habitability assessment) |
| `geochemistry/` | Chemistry of the solid Earth and its record-keeping in isotopes: element distribution between crust/mantle/core (Goldschmidt classification: lithophile/siderophile/chalcophile/atmophile), radiogenic isotope systems (U-Pb geochronology as the most precise geological clock, Sm-Nd and Rb-Sr for crustal evolution, Ar-Ar for thermal history), stable isotope proxies (δ¹⁸O as a paleothermometer — how ice cores read ancient temperatures, δ¹³C as a carbon cycle tracer), carbon isotope excursions at mass extinction boundaries, hydrothermal geochemistry (black smokers, VMS deposits, seafloor spreading chemistry), weathering and soil geochemistry, ocean chemistry evolution through time | `01-ELEMENT-DISTRIBUTION.md` — Goldschmidt classification and reservoir framing | `geology/` (petrology uses geochemistry throughout); `paleontology/` (isotope excursions record extinction events); `oceanography/` (marine geochemistry) |
| `space-exploration/` | The physics and economics of getting to space and staying there: the Tsiolkovsky rocket equation (why spaceflight is exponentially hard — the tyranny of the rocket equation), specific impulse as the figure of merit for propulsion efficiency, launch vehicle staging (why staging works, expendable vs. reusable tradeoffs), chemical propulsion (hypergolics, cryogenics, solid motors), electric propulsion (ion/Hall thrusters — why they're efficient in deep space), SpaceX reusability revolution (Falcon 9 economics, Starship architecture), spacecraft systems (ADCS, power, thermal, comms, GNC), mission design (Hohmann transfers, gravity assists, interplanetary superhighway), human spaceflight physiology and life support, the commercial space economy | `01-ORBITAL-MECHANICS.md` — rocket equation and orbital mechanics before hardware | `astronomy/` for the destinations; `physics/` (Math & Physics) for the orbital mechanics; `planetary-science/` for mission targets |
| `astrobiology/` | The science of life's cosmic context: origin of life theories (RNA world hypothesis — the chicken-and-egg problem solved; hydrothermal vent model vs. warm little pond; LUCA), extremophile biology (thermophiles, acidophiles, xerophiles — the envelope for life), habitable environments in the solar system (Europa subsurface ocean, Enceladus plumes, Titan chemistry, Mars subsurface), biosignature detection (what to look for: disequilibrium gases, chirality, morphological fossils), JWST atmospheric characterization (transmission spectroscopy, what O₂/O₃/CH₄ together would mean), the Fermi paradox and its responses (Great Filter, rare Earth, dark forest, transcension), SETI methodology | `01-ORIGIN-OF-LIFE.md` — RNA world and the origin problem before extremophile or planetary habitability | `planetary-science/` (habitable environments); `geochemistry/` (hydrothermal vent chemistry); Life Sciences `evolutionary-biology/` (earliest evolution) |

---

## Paths

### Deep Time to Present Climate
`astronomy/` → `geology/` → `paleontology/` → `climate-science/`
*Orbital forcing establishes glacial cycles; geology reads the rock record; paleontology reconstructs past biospheres through extinctions; climate science extracts the quantitative signal and projects it forward — the complete paleo-to-future arc.*

### The Coupled Earth System
`meteorology/` → `oceanography/` → `climate-science/`
*Weather physics scales into ocean-atmosphere coupling, which drives the multi-decadal variability that climate science must separate from forced trends — the three-layer hierarchy from forecast to projection.*

### Water from Sky to Aquifer to Crop
`meteorology/` → `hydrology/` → `agriculture/`
*Precipitation from synoptic and convective systems is the input; hydrological routing determines what reaches rivers and groundwater; agriculture uses that water resource and returns evapotranspiration back to the atmosphere — a closed loop.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Life Sciences | `ecology/` ↔ `geography/` — biome geography and biogeography are shared territory; `climate-science/` and `oceanography/` ↔ biology via marine and terrestrial primary productivity, species range shifts, and coral bleaching |
| History & Ideas | `paleontology/` ↔ `history-of-science/` — Lyell's uniformitarianism, Cuvier's catastrophism, and Darwin's geological reading are foundational intellectual history; `geology/` ↔ `economic-history/` via coal, oil, and mineral resource extraction as engines of industrialization |
| Social Sciences | `climate-science/` ↔ `public-health/` (heat stress, vector-borne disease range expansion) and `economics/` (carbon pricing, damage functions, discount rate debates); `agriculture/` ↔ `demography/` (Malthusian limits, food security, land-use change) |
| Engineering | `hydrology/` and `geology/` ↔ civil and geotechnical engineering; `climate-science/` ↔ energy-systems engineering; `meteorology/` ↔ wind and solar resource assessment |
