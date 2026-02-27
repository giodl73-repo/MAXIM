# Construction Materials — Overview

## The Big Picture: Material Families × Structural Roles × Time

```
TIMELINE ─────────────────────────────────────────────────────────────────────►

 10,000 BCE    3,000 BCE     1000 CE      1800s        1900s         2000s+
     │             │            │            │             │              │
  EARTH &       MASONRY       GOTHIC       IRON &        CONCRETE     ENGINEERED
  ORGANIC       SYSTEMS       TIMBER       STEEL         SYSTEMS      COMPOSITES
     │             │            │            │             │              │
  Thatch       Mud brick    Cruck frame  Cast iron    RC frames      CLT panels
  Adobe        Fired brick  Half-timber  Wrought iron  Prestressed   CFRP tendons
  Wattle       Cut stone    Gothic arch  Bessemer      Curtain wall  Geopolymers
  Post+beam    Roman conc.  Flying butt  Wide flange   Unitized      Mass timber
  Dry stone    Arches/vaults Lime mortar  Riveted conn  HPC/UHPC     Bio-based
     │             │            │            │             │              │
  Compressive   Compressive   Comp +       Tension +     Both (RC)    Tailored
  only          + arching     tension      compression   controls     anisotropy
```

```
MATERIAL FAMILIES AND STRUCTURAL ROLES
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  EARTH / ORGANIC           MASONRY                METALS                    │
│  ┌───────────────┐         ┌───────────────┐      ┌───────────────────────┐ │
│  │ Adobe/rammed  │         │ Brick/stone   │      │ Cast iron   wrought   │ │
│  │ earth         │         │ Roman conc.   │      │ iron        steel     │ │
│  │ Thatch/straw  │         │ Fired brick   │      │ Stainless   aluminium │ │
│  │ Sawn timber   │         │ Lime mortar   │      │ High-str.   grades    │ │
│  └───────────────┘         └───────────────┘      └───────────────────────┘ │
│  Compression OK            Compression +++        Tension +++ Shear +++     │
│  Tension weak              Tension poor           Compression ++ ductile    │
│                                                                              │
│  CEMENTITIOUS              GLASS                  ENGINEERED WOOD           │
│  ┌───────────────┐         ┌───────────────┐      ┌───────────────────────┐ │
│  │ Portland OPC  │         │ Float glass   │      │ Plywood  LVL         │ │
│  │ Fly ash blend │         │ Tempered      │      │ Glulam   CLT         │ │
│  │ UHPC          │         │ Laminated     │      │ Mass timber hybrids  │ │
│  │ Geopolymer    │         │ IGU systems   │      │                      │ │
│  └───────────────┘         └───────────────┘      └───────────────────────┘ │
│  Compression +++           Compression +          Compression + Tension +   │
│  Tension poor (RC fixes)   Tension ~zero          Bending ++ biaxial (CLT)  │
│                                                                              │
│  POLYMERS / COMPOSITES     BIO-BASED              SMART / PHASE-CHANGE      │
│  ┌───────────────┐         ┌───────────────┐      ┌───────────────────────┐ │
│  │ GFRP/CFRP    │         │ Hempcrete     │      │ PCM wallboard        │ │
│  │ AFRP tendons │         │ Straw bale    │      │ Self-healing conc.   │ │
│  │ GRC panels   │         │ Bamboo        │      │ Aerogel insulation   │ │
│  └───────────────┘         └───────────────┘      └───────────────────────┘ │
│  Tension +++ (fiber)       Thermal mass ++        Thermal buffering +       │
│  Tailored anisotropy       Insulation ++          Carbon-negative poss.     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

**Reliability engineering framing**: Each durability mechanism (carbonation, chloride ingress, ASR, freeze-thaw, creep) is a competing failure mode with a time-to-threshold distribution — carbonation depth follows d = k*sqrt(t), chloride ingress follows erfc profiles (Fick's 2nd law). Service-life specifications (50 or 100 years) are reliability targets. Cover rules and concrete mix specs are the engineering controls ensuring these MTTF targets are met.

## Why Materials Change: The Driving Forces

Materials adoption is never just "better technology discovered." It is a conjunction
of resource availability, energy cost, urban requirements, and regulatory pressure.

```
  DRIVING FORCE              HISTORICAL TRIGGER              EXAMPLE
  ─────────────────────────────────────────────────────────────────────────
  Resource depletion         Forest clearance → brick         Medieval England
  Energy availability        Coal → ironmaking at scale        Industrial Revolution
  Urban density              Height requirements → steel       Chicago 1880s
  Span requirements          Train sheds → wrought iron        Crystal Palace 1851
  Fire events                Great Fire of London 1666         Brick+tile mandated
  War damage + rebuild       WWII → prefab concrete            European postwar
  Carbon pricing             Net-zero mandates → CLT           2010s–present
  Code evolution             Seismic codes → ductile steel     California 1971
  Labor cost                 Site → factory → unitized         Postwar unionization
  Supply chain               Local vernacular → global         Containerization 1960s
  Speed of construction      Prefabrication → structural steel Modern commercial
  Environmental regulation   VOC limits → water-based coatings 1990s US/EU
```

---

## Structural Principles: Load Paths

Every material choice cascades from what loads the element must carry and the failure
mode when capacity is exceeded.

```
LOAD TYPES AND STRUCTURAL ELEMENTS
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  GRAVITY LOADS: Dead (permanent) + Live (occupancy / snow / wind uplift)    │
│                                                                              │
│  Beam in bending:                                                            │
│  Load → ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓                                              │
│         ══════════════════════════                                           │
│         ↑ support            support ↑                                       │
│                                                                              │
│  Stress across cross-section:                                                │
│  ┌──────────────────────────┐                                                │
│  │  ──── compression (top) ─│                                                │
│  │  ─ ─  neutral axis ─ ─ ─│  zero stress, N.A. at centroid (elastic)      │
│  │  ════ tension (bottom) ══│                                                │
│  └──────────────────────────┘                                                │
│                                                                              │
│  Wood/steel/RC: handle both — steel rebar takes tension in RC               │
│  Plain concrete/masonry: must be in compression only                        │
│  Prestress: pre-compresses bottom fiber to cancel service tension           │
│                                                                              │
│  Column in compression:                                                      │
│  Short column: material crushing  σ > f'c (stocky, L/r < 20)               │
│  Slender column: Euler buckling   P_cr = π²EI / L_eff²                     │
│    → slenderness ratio L/r governs; same material, different failure mode   │
│                                                                              │
│  Arch: converts vertical load → axial compression along arch curve          │
│    → Roman/Gothic masonry: only compression → ideal for stone/brick         │
│    → Catenary arch: inverted hanging chain → pure compression everywhere    │
│                                                                              │
│  Hanging cable: converts load → axial tension along cable profile           │
│    → suspension bridges, cable-stayed structures                            │
│                                                                              │
│  LATERAL LOADS: Wind + Seismic                                               │
│                                                                              │
│  Shear wall:    in-plane stiffness resists lateral drift                    │
│  Moment frame:  beam-column connections carry bending moments               │
│  Braced frame:  diagonal braces work in tension (and compression)           │
│  Core:          RC or CLT core provides torsional + lateral stiffness       │
│                                                                              │
│  Diaphragm: floor plate transfers horizontal load to vertical elements      │
│    → RC flat slab: inherent diaphragm                                       │
│    → CLT floor: needs connections at panel edges for diaphragm action       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### The Fundamental Tension: Compressive vs. Tensile Capacity

| Material | Comp. Strength | Tensile Strength | Ratio C:T | Structural Implication |
|---|---|---|---|---|
| Granite | 160–240 MPa | 7–25 MPa | ~12:1 | Post-and-lintel only; span < 5 m |
| Limestone | 50–170 MPa | 5–10 MPa | ~15:1 | Arch required for larger spans |
| Fired brick | 10–100 MPa | 2–5 MPa | ~20:1 | Mortared; arch construction still preferred |
| Plain concrete C30 | 30 MPa | 3 MPa | 10:1 | Rebar mandatory for bending members |
| UHPC | 150–200 MPa | 8–15 MPa (fiber) | ~15:1 | Steel fiber can substitute for rebar |
| Cast iron | 570 MPa | 140 MPa | 4:1 | Tension members are hazardous |
| Structural steel A36 | 400 MPa | 400 MPa | 1:1 | Isotropic — all-purpose workhorse |
| Softwood (// grain) | 35–50 MPa | 40–80 MPa | ~1:1 | Strong parallel to grain |
| Softwood (⊥ grain) | 5–10 MPa | 1–3 MPa | — | Splitting failure; avoid cross-grain tension |
| CLT in-plane | ~25 MPa | ~14 MPa | — | Orthotropic; two-way plate action |
| CFRP (UD, fiber dir) | 1,200 MPa | 3,500 MPa | — | Extreme tension; use for tendons/cladding |
| Adobe / rammed earth | 1–5 MPa | < 0.5 MPa | > 10:1 | Low-rise walls only; stabilizer helps |

---

## Material Properties Taxonomy

### Mechanical Properties

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  MECHANICAL PROPERTIES                                                       │
│                                                                              │
│  σ_y    Yield strength (MPa)  — stress where permanent deformation begins   │
│          For concrete: compressive cylinder strength f'c (28-day)           │
│          For timber: characteristic value at 5th percentile                 │
│                                                                              │
│  σ_u    Ultimate strength (MPa) — fracture / crushing point                 │
│                                                                              │
│  E      Young's modulus (GPa) — stiffness, independent of strength          │
│          E_steel = 200 GPa  (all grades — changing grade changes σ_y not E) │
│          E_concrete = 25–35 GPa  (≈ 4700√f'c MPa, US customary)            │
│          E_timber (// grain) = 8–15 GPa                                     │
│          E_CFRP (UD) = 70–300 GPa                                           │
│          E_glass = 70 GPa                                                    │
│                                                                              │
│  ρ      Density (kg/m³)                                                      │
│          Steel: 7,850  Concrete: 2,300–2,500  Timber: 400–700              │
│          CFRP: 1,500–1,600  GFRP: 1,600–2,000  Aerogel: 100–200           │
│                                                                              │
│  Specific strength = σ_u / ρ  (strength per unit weight)                   │
│          CFRP >> Steel >> Timber >> Concrete >> Masonry                     │
│                                                                              │
│  ν      Poisson's ratio — lateral strain per unit axial strain              │
│          Steel: 0.30  Concrete: 0.15–0.20  Rubber: ~0.50  Cork: ~0.00      │
│                                                                              │
│  G      Shear modulus = E / [2(1+ν)]                                        │
│          Steel: 77 GPa  Concrete: 10–14 GPa  Timber (// grain): 0.5–1 GPa  │
│                                                                              │
│  CREEP: time-dependent strain under sustained constant stress                │
│          Significant in concrete: creep coefficient φ = 1.5–3.0            │
│          Long-term deflection = elastic × (1 + φ) → pre-camber beams       │
│          Timber: creep factor k_def = 0.6–1.5 per EC5                      │
│                                                                              │
│  SHRINKAGE: volume change without load                                       │
│          Concrete drying shrinkage ε_cs ≈ 300–600 × 10⁻⁶                   │
│          → crack control joints spaced ≤ 5–7 m                             │
│          → minimum ρ (reinforcement ratio) to distribute cracks             │
│                                                                              │
│  FATIGUE: repeated stress cycling reduces failure load                       │
│          S-N (Wöhler) curve: log stress vs log cycles to failure            │
│          Steel: endurance limit ≈ 40% σ_u at ~10⁷ cycles                   │
│          Concrete: no clear endurance limit; each cycle damages             │
│          Composites: delamination fatigue — critical in aerospace           │
│                                                                              │
│  DUCTILITY: ratio of ultimate strain to yield strain (μ = ε_u / ε_y)       │
│          Steel: μ ≈ 10–20 — warning before collapse, absorbs seismic energy │
│          Masonry/glass: μ ≈ 1 — sudden brittle failure                     │
│          → seismic design explicitly requires ductility in primary elements │
│                                                                              │
│  HARDNESS: resistance to surface indentation (Brinell/Vickers/Mohs)        │
│          Relevant for wear, scratch resistance (flooring, worktops)         │
│          Granite Mohs 6–7  Steel Vickers ~200 HV  Concrete ~100 HV         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Thermal Properties

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  THERMAL PROPERTIES                                                          │
│                                                                              │
│  λ (k)  Thermal conductivity (W/mK)  — heat flow through material           │
│          Steel: 50    Concrete: 1.7   Brick: 0.5–1.0  Timber: 0.12         │
│          Mineral wool: 0.035  EPS: 0.038  Aerogel: 0.015                   │
│          → lower = better insulator                                          │
│                                                                              │
│  α      Thermal diffusivity = λ / (ρ × c_p)  (m²/s)                        │
│          High α: fast temperature equalization → poor thermal buffer         │
│          Low α: slow thermal response → good thermal mass buffer            │
│          Stone α ~ 1×10⁻⁶ m²/s  Steel α ~ 12×10⁻⁶ m²/s                    │
│                                                                              │
│  c_p    Specific heat capacity (J/kgK)                                       │
│          Water: 4,186  Concrete: 880  Steel: 490  Timber: 1,700             │
│          → Thermal mass (stored heat) = ρ × c_p × volume                   │
│                                                                              │
│  α_T    Coefficient of thermal expansion (× 10⁻⁶ /°C)                       │
│          Steel: 12   Concrete: 10–12  ← matched → composite works well      │
│          Aluminium: 23  Glass: 8–9   Timber (//) 3–5  Timber (⊥) 30–60     │
│          Mismatch → differential movement → cracking / joint failure        │
│                                                                              │
│  R-value = thickness / λ  (m²K/W, thermal resistance)                       │
│          100 mm mineral wool: 0.1/0.035 = 2.86 m²K/W                       │
│          100 mm concrete: 0.1/1.7 = 0.06 m²K/W                             │
│          → insulation R is ~50× greater per unit thickness                  │
│                                                                              │
│  U-value = 1 / ΣR  (W/m²K, total heat transmission including surface Rsi/o)│
│          Passivhaus wall: U ≤ 0.15 W/m²K                                   │
│          UK Building Regs Part L 2021: wall U ≤ 0.18 W/m²K new build       │
│                                                                              │
│  FIRE BEHAVIOUR:                                                             │
│          Steel: non-combustible; loses ~50% strength at 500–550°C           │
│            → intumescent coating or board/spray fireproofing mandatory      │
│          Concrete: non-combustible; spalling risk at >300°C (steam pressure)│
│          Timber: combustible; chars at ~0.65 mm/min                         │
│            → char layer insulates residual section → predictable behaviour  │
│          Glass: shatters from thermal shock; fire-rated glass uses wire mesh│
│            or specialist composites (e.g., Pyrostop, Contraflam)            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Acoustic Properties

```
  ACOUSTIC PERFORMANCE
  ──────────────────────────────────────────────────────────────────────────
  Rw (dB)   Weighted sound reduction index — airborne sound isolation
             Concrete 150 mm:      Rw ~ 48 dB
             Brick 215 mm:         Rw ~ 50 dB
             CLT 200 mm:           Rw ~ 40–45 dB  ← CLT acoustic challenge
             Stud wall (lined):    Rw ~ 45–60 dB  (decoupled mass)
             Double glazing:       Rw ~ 30–50 dB  (gap + mass critical)
             Acoustic laminated:   Rw ~ 38–48 dB  (PVB interlayer damping)

  LnT,w     Weighted standardized impact sound pressure level (lower = better)
             CLT floors:           LnT,w ~ 60–70 dB  → problem without treatment
             RC slab 200 mm:       LnT,w ~ 75 dB     → better heavy/dense
             Floating floor screed + resilient layer: reduces by 20–30 dB

  NRC       Noise reduction coefficient — absorption (0 = reflective, 1 = absorptive)
             Mineral wool 50 mm:   NRC ~ 0.70–0.95
             Concrete bare:        NRC ~ 0.02
             → absorption ≠ isolation (completely different phenomena)

  Mass law:  Rw (dB) ≈ 20 log₁₀(m) − 47   (m = surface mass, kg/m²)
             Doubling surface mass → +6 dB  (diminishing returns quickly)
             Decoupling (resilient mounts, cavity walls) beats mass law
             easily → stud cavity wall with decoupled skins outperforms
             solid concrete at half the mass

  Coincidence dip: at specific frequency, panel resonates → isolation drops
             → laminated glass + different glass thicknesses avoids coincidence
```

### Hygric Properties

```
  MOISTURE BEHAVIOUR
  ──────────────────────────────────────────────────────────────────────────
  Vapour resistance factor μ:  how much harder than air to diffuse vapour
             Air: μ = 1 (reference)
             Mineral wool: μ ≈ 1  (open to vapour, permeable)
             Concrete: μ = 80–120
             Polyethylene VCL: μ > 100,000  ← vapour control layer
             → VCL placement in wall build-up must be on warm side
               (inside in temperate climates)

  Equilibrium moisture content (EMC) for timber:
             EMC at 65% RH ≈ 12% (softwood)
             EMC changes → dimensional change → swelling/shrinkage
             CLT connections must accommodate moisture-driven movement

  Capillary action in masonry:
             Water rises by capillary suction → damp-proof course (DPC) required
             Cavity wall breaks capillary path → drainage gap with wall ties

  Efflorescence: soluble sulfates/chlorides migrate to surface
             Source: cement binder, aggregates, groundwater
             → unsightly, not structural; avoided by low water/cement ratio

  Carbonation depth in concrete:
             CO₂ + Ca(OH)₂ → CaCO₃ + H₂O
             → pH drops from ~13 to ~9 → steel passivation lost → corrosion
             Depth: d = k√t  where k ≈ 1–4 mm/year^0.5 (indoor exposure)
             → cover rules in EN 1992 based on exposure class + service life
             → high-quality concrete (low w/c, GGBS) slows carbonation
```

---

## The Full Materials Arc

```
MATERIALS EVOLUTION ARC
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  ERA 1: EARTH & ORGANIC  (pre-3000 BCE)                                      │
│  ────────────────────────────────────────────────────────────────────────    │
│  Mud brick → thermal mass; cheap; local; 1–3 storey limit                   │
│  Thatch → lightweight roofing; breathable; renewable                        │
│  Timber → flexible; spans possible; mortise-and-tenon joints                │
│  Dry stone → gravity walls; no binder; earthquake-tolerant                  │
│  Limit: tension weak; weathering; span limit ~5 m; fire risk                │
│                                                                              │
│  ERA 2: FIRED MASONRY & ROMAN CONCRETE  (~3000 BCE – 500 CE)                │
│  ────────────────────────────────────────────────────────────────────────    │
│  Fired brick → consistent; durable; 5–6 storey masonry possible             │
│  Cut stone → monumental; self-compressive                                   │
│  Pozzolana concrete → hydraulic; stronger with age; underwater use          │
│  Voussoir arch → spans masonry beyond lintel limits                         │
│  Dome + vault → enclose space without intermediate supports                 │
│  Limit: zero tension allowed; all structure must be compressive              │
│                                                                              │
│  ERA 3: GOTHIC TIMBER & MASONRY  (~500–1700 CE)                              │
│  ────────────────────────────────────────────────────────────────────────    │
│  Pointed arch → reduces horizontal thrust vs round arch → thinner walls     │
│  Flying buttress → carries thrust outside → interior freed for windows      │
│  Timber roof trusses → span large halls                                     │
│  Lime mortar → self-healing; flexible; breathable                           │
│  Limit: height; fire in timber; lime maintenance                            │
│                                                                              │
│  ERA 4: IRON & STEEL  (~1750–1900)                                            │
│  ────────────────────────────────────────────────────────────────────────    │
│  Cast iron → first cheap structural material; brittle in tension            │
│  Wrought iron → fibrous; better in tension; puddling process                │
│  Bessemer steel → consistent; cheap; strong in tension AND compression      │
│  Skeleton frame → load off walls → curtain walls possible                   │
│  Limit: fire; corrosion; rolling/fabrication limits                         │
│                                                                              │
│  ERA 5: CONCRETE DOMINANCE  (~1900–1990)                                      │
│  ────────────────────────────────────────────────────────────────────────    │
│  RC → cheap; fireproof; mouldable; combines concrete + steel perfectly      │
│  Prestressed/post-tensioned → thin slabs; long spans                       │
│  Curtain wall → glass + aluminium envelope decoupled from structure         │
│  Limit: embodied carbon — Portland cement ≈ 8% of global CO₂               │
│                                                                              │
│  ERA 6: ENGINEERED & COMPOSITE  (~1990–present)                               │
│  ────────────────────────────────────────────────────────────────────────    │
│  CLT/glulam → tall timber; carbon sequestration; biophilic design           │
│  UHPC → ultra-thin; ultra-strong; fibers partially replace rebar            │
│  CFRP → post-tensioning; façade; lightweight repair                         │
│  Geopolymer → cement substitute; 40–80% lower CO₂                          │
│  Aerogel → extreme insulation in thin profiles                              │
│  Limit: cost; supply chains; building codes still catching up               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Why Embodied Carbon Now Matters

```
CARBON BUDGET SHIFT: OPERATIONAL vs EMBODIED
──────────────────────────────────────────────────────────────────────────────
  1980s leaky building (50-year life):
    Operational:  80%  (fossil heating, no insulation)
    Embodied:     20%

  2025 Passivhaus (50-year life):
    Operational:  30–40%  (nearly solved: insulation + MVHR + heat pumps)
    Embodied:     60–70%  ← now the dominant challenge

  Typical new building: embodied carbon by element
    Structural concrete:    30–40% of total embodied carbon
    Structural steel:       15–25%
    Façade + cladding:      10–20%
    MEP systems:             5–10%
    Finishes + fit-out:     10–20%

  Portland cement CO₂ sources:
    Calcination: CaCO₃ → CaO + CO₂  ~0.5 tCO₂/t clinker  ← process, inescapable
    Fuel (kiln):                     ~0.35 tCO₂/t clinker  ← can decarbonise
    Global: ~8% of annual anthropogenic CO₂

  Structural frame comparison (kgCO₂e/m² gross floor area):
    RC flat slab:            100–180 kgCO₂e/m²
    Structural steel:        100–200 kgCO₂e/m²  (EAF recycled steel: ~80)
    Mass timber CLT:          30–80  kgCO₂e/m²  + sequesters ~40–60 kgCO₂/m²
    Geopolymer concrete:      50–100 kgCO₂e/m²  (still maturing)

  CLT carbon logic:
    Timber sequesters ~1 tCO₂ per m³ of wood volume as it grows
    CLT ~0.4–0.5 m³ solid timber per m³ panel
    → biogenic carbon stored in building fabric ← temporary store
    → release on decay/combustion/demolition → carbon bank, not sink
    → valid only with sustainable forest management (FSC/PEFC)
```

---

## Properties Quick Reference Matrix

| Property | Unit | Steel A36 | C30 Concrete | Softwood | Float glass | CLT (5-ply) | CFRP (UD) |
|---|---|---|---|---|---|---|---|
| Comp. strength | MPa | 400 | 30 | 35 | 1,000 | 25 | 1,200 |
| Tensile strength | MPa | 400 | 3 | 60 | 45 | 14 | 3,500 |
| Young's modulus | GPa | 200 | 30 | 11 | 70 | 11 | 230 |
| Density | kg/m³ | 7,850 | 2,400 | 500 | 2,500 | 480 | 1,550 |
| Thermal cond. λ | W/mK | 50 | 1.7 | 0.12 | 1.0 | 0.13 | 2–10 |
| Thermal exp. | ×10⁻⁶/°C | 12 | 11 | 4 | 9 | 5 | 0–3 |
| Density × c_p | kJ/m³K | 3,836 | 2,112 | 850 | 2,200 | 816 | — |
| Embodied C | kgCO₂e/kg | 1.5–2.8 | 0.13 | 0.4 | 0.85 | 30–60 | — |
| Recyclability | — | High | Low | Bio | Partial | Bio | Low |

---

Material specifications (EN 1992, AISC, NDS, EN 15978) are **interface contracts** between designer, fabricator, and inspector — they define the acceptable state space, test protocols, and acceptance criteria. Same mental model as an API contract or type system: the spec defines what each party must guarantee about their deliverable.

## Structural Systems Selection

```
STRUCTURAL SYSTEM SELECTION — MATERIAL MATCH
┌──────────────────────────────────────────────────────────────────────────────┐
│  CONSTRAINT / BUILDING TYPE           PREFERRED STRUCTURAL MATERIAL          │
│  ─────────────────────────────────    ─────────────────────────────────────  │
│  1–3 stories, small span              CLT, timber frame, RC, masonry         │
│  4–12 stories, typical office         Steel frame + RC core (dominant UK/US) │
│  4–12 stories, low-carbon target      Hybrid CLT + glulam + RC core          │
│  > 12 stories, office                 Steel or RC (proven); tall timber 20+  │
│  Long span (> 20 m)                   Steel trusses, PT-RC, glulam           │
│  Long span + minimal weight           Steel cable/tension; CFRP (specialist) │
│  Seismic zone                         Ductile steel MRF or SW + RC core      │
│  Aggressive environment               Stainless; GFRP rebar; UHPC            │
│  Speed of construction                Steel frame; unitized façade; precast  │
│  Low carbon                           CLT; high fly-ash/GGBS; recycled steel │
│  Thermal mass for passive comfort     Adobe; rammed earth; concrete; brick   │
│  Ultra-thin elements                  UHPC; CFRP; GFRC façade panels        │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Masonry or plain concrete, spans > 6 m? | Use arch/vault OR reinforce OR prestress — not plain spans |
| Building > 8 stories? | Steel or RC frame; mass timber possible but specialist design |
| Fire rating 60+ min required? | RC always OK; steel needs intumescent/boarding; CLT with char margin |
| High humidity / aggressive environment? | Stainless fixings; GFRP rebar; UHPC; avoid plain steel |
| Embodied carbon reduction priority? | CLT/glulam; high fly-ash or GGBS concrete; adaptive reuse |
| Thermal mass needed? | Exposed concrete soffit; brick; stone; rammed earth — not timber/steel |
| Acoustic isolation floor to floor? | Mass + decoupling; heavy concrete or CLT + floating screed + resilient |
| Seismic zone, ductility required? | Ductile steel moment frame; ductile RC shear walls |
| Fast on-site erection? | Prefab steel; unitized curtain wall; precast concrete; CLT panels |
| Long span, minimal structural depth? | Post-tensioned flat slab; Vierendeel steel; glulam-steel hybrid |
| No formwork, complex geometry? | Shotcrete; UHPC precast; GFRC; 3D-printed concrete |

---

## Common Confusion Points

**Stiffness ≠ Strength.** E (Young's modulus) measures stiffness — resistance to
deformation. σ_y measures strength — resistance to yielding. Glass is stiffer than
most metals but brittle. High-strength steel (A514) is no stiffer than mild steel (A36)
— both have E = 200 GPa. Stiffness governs deflection and buckling; strength governs
yielding and fracture.

**Insulation ≠ Thermal mass.** Aerogel insulates brilliantly (λ = 0.015 W/mK) but
has negligible thermal mass (low ρ × c_p). Concrete thermal mass is poor insulation
(λ = 1.7 W/mK) but excellent heat storage. A well-designed passive building often
needs BOTH — mass on the warm side to buffer temperature swings, insulation on the
cold side to prevent heat escaping.

**Fire resistance ≠ Non-combustibility.** Steel is non-combustible but loses 50% of
its strength in 15 minutes unprotected in a fire. CLT is combustible but chars
predictably — char at ~0.65 mm/min insulates the inner core. A properly designed
mass timber section can achieve 60 or 90 minutes fire resistance without additional
protection.

**Portland cement ≠ Concrete.** Cement is the binder (~8–12% by weight). Concrete
is 70–80% aggregates + water. Supplementary cementitious materials (SCMs) — fly ash,
GGBS, silica fume — can replace 30–70% of OPC without strength loss. High SCM
replacement lowers CO₂, lowers heat of hydration, and often improves long-term
durability.

**Roman concrete ≠ Modern OPC concrete.** Roman opus caementicium used pozzolana
volcanic ash + lime + seawater. It is hydraulic (sets underwater), contains no steel
reinforcement, is pure compression, and strengthens via ongoing aluminosilicate
reaction over centuries. Modern OPC hydration is largely complete at 28 days. The
two materials share name only.

**Embodied carbon ≠ Operational carbon ≠ Whole-life carbon.** Embodied = A1–A5 in
EN 15978 (product manufacturing + construction). Operational = B6 (energy in use).
Whole-life = A1–A5 + B1–B7 + C1–C4. Net-zero building targets must address all
stages. Early design decisions (structure type, material mix) lock in ~80% of
embodied carbon and cannot be undone.
