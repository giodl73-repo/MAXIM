# Construction Materials — Portland Cement and Concrete

## The Big Picture: The Portland Cement System

```
PORTLAND CEMENT TO CONCRETE TO STRUCTURE
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  INPUTS                    CLINKER PRODUCTION              CEMENT            │
│  ──────────────────────    ────────────────────────────    ───────────────   │
│  Limestone (CaCO₃) 75%     → rotary kiln 1450°C           → grind clinker    │
│  Clay / shale 20%            CaCO₃ → CaO + CO₂             + gypsum (CaSO₄)  │
│  Iron ore / silica  5%       CaO + SiO₂+Al₂O₃ → clinker   → Portland OPC     │
│                                                                              │
│  CLINKER PHASES (Bogue equations):                                           │
│  C₃S  (alite)    50–70%  → fast strength; main phase                         │
│  C₂S  (belite)   15–25%  → slow strength; lower heat                         │
│  C₃A  (aluminate) 5–10%  → very fast; high heat; sulfate attack risk         │
│  C₄AF (ferrite)  5–15%  → low strength; grey colour                          │
│                                                                              │
│  CEMENT + SCMs + WATER + ADMIXTURES + AGGREGATE = CONCRETE                   │
│                                                                              │
│  HYDRATION → C-S-H GEL (strength) + Ca(OH)₂ (portlandite)                    │
│                                                                              │
│  CONCRETE IN STRUCTURE:                                                      │
│  Plain → columns/walls in compression                                        │
│  RC (reinforced) → beams, slabs, frames                                      │
│  PC (prestressed) → long-span; thin elements                                 │
│  UHPC → fibre-reinforced; near-steel performance                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Portland Cement Chemistry: From First Principles

### Raw Materials and Kiln Chemistry

```
CEMENT KILN ZONES (SIMPLIFIED)
──────────────────────────────────────────────────────────────────────────────
  ZONE          TEMP RANGE    REACTION
  ─────────────────────────────────────────────────────────────────────────────
  Preheater      150–800°C    Raw meal drying; clay dehydration
  Calcining      800–900°C    CaCO₃ → CaO + CO₂  (calcination — 60% of CO₂)
  Transition     900–1300°C   Solid-state reactions: CaO + SiO₂ → C₂S (belite)
  Burning zone   1300–1450°C  Liquid phase: C₂S + CaO → C₃S (alite forms)
  Cooling        1450–1200°C  Rapid quench → clinker nodules; C₃A/C₄AF crystallize

  CEMENT NOTATION (shorthand used universally):
    C = CaO    S = SiO₂    A = Al₂O₃    F = Fe₂O₃    H = H₂O
    C₃S = 3CaO·SiO₂     (tricalcium silicate, alite)
    C₂S = 2CaO·SiO₂     (dicalcium silicate, belite)
    C₃A = 3CaO·Al₂O₃    (tricalcium aluminate)
    C₄AF = 4CaO·Al₂O₃·Fe₂O₃  (tetracalcium aluminoferrite)

  BOGUE EQUATIONS (% by mass from oxide analysis):
    C₃S  = 4.07C − 7.60S − 6.72A − 1.43F − 2.85S̄  (S̄ = SO₃)
    C₂S  = 2.87S − 0.754(C₃S)
    C₃A  = 2.65A − 1.69F
    C₄AF = 3.04F
    → used to predict phase composition from XRF oxide analysis
```

### Hydration Reactions

```
HYDRATION CHEMISTRY
──────────────────────────────────────────────────────────────────────────────
  PRINCIPAL REACTION (alite, C₃S → main strength phase):

    2C₃S + 6H  →  C₃S₂H₃ + 3CH
    (alite) (water) → (C-S-H gel) + (portlandite Ca(OH)₂)

  C-S-H gel: calcium silicate hydrate
    → no fixed stoichiometry (amorphous gel; C/S ratio ≈ 1.7 in OPC)
    → nano-scale interlocking fibrils → source of concrete strength
    → specific surface area: 100–700 m²/g (nanoporous)
    → density: ~2,000–2,500 kg/m³

  Ca(OH)₂ (portlandite):
    → hexagonal crystal plates; ~20–25% of hydration products
    → high pH (pKa ~12.5) → passivates steel reinforcement
    → soluble → leaches; reactive → pozzolanic reactions

  Belite (C₂S) hydration:
    C₂S + 4H → C-S-H + CH    (same products; much slower)
    C₂S: 90% hydrated by 1 year vs C₃S: 90% hydrated by 28 days
    → high C₂S cements: lower early strength; lower heat; better durability

  C₃A hydration (fast; dangerous without gypsum):
    C₃A + 6H → C₃AH₆  (flash set — instant stiffening without strength)
    Gypsum (CaSO₄·2H₂O) added in cement grinding → reacts with C₃A first:
    C₃A + 3CSH₂ + 26H → C₆AS₃H₃₂  (ettringite — fills space; then converts)
    → ettringite formation delays C₃A hydration → controls set time
```

### Water-Cement Ratio: Abrams' Law

```
ABRAMS' LAW: compressive strength = A / B^(w/c)
  where A ≈ 97 MPa, B ≈ 8.2 (empirical constants for normal concrete)
  → strength decreases approximately exponentially with increasing w/c

  PRACTICAL:
  w/c = 0.30:  f_ck ≈ 60–70 MPa  (high-performance concrete)
  w/c = 0.40:  f_ck ≈ 45–55 MPa  (good normal concrete)
  w/c = 0.50:  f_ck ≈ 30–40 MPa  (standard C30 concrete)
  w/c = 0.65:  f_ck ≈ 15–25 MPa  (weak/low quality)

  WHY EXCESS WATER REDUCES STRENGTH:
  Chemically, C₃S + C₂S require only w/c ≈ 0.23 for complete hydration
  Any water above w/c ≈ 0.23 → excess water fills capillary pores
  As concrete dries → pores empty → become voids → weaker, more permeable
  → minimum water principle: use only what's needed chemically + workability
  → superplasticizers break electrostatic particle clusters → reduce water need

  Durability also improved by low w/c:
    Permeability: K ≈ 10⁻¹⁰ to 10⁻¹² m/s (good concrete) vs 10⁻⁸ (poor)
    → lower permeability → less chloride/CO₂ ingress → less rebar corrosion
    → EN 1992 (Eurocode 2): w/c limits by exposure class (XC, XD, XS, XF, XA)
```

---

## Supplementary Cementitious Materials (SCMs)

```
SCM COMPARISON
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SCM         SOURCE              MECHANISM     REPLACEMENT  CO₂ SAVING       │
│  ─────────────────────────────────────────────────────────────────────────   │
│  Fly ash     Coal power station  Pozzolanic:   20–40%       ~30–40%          │
│  (Class F)   Siliceous FA        Ca(OH)₂ +                                   │
│                                  SiO₂ → C-S-H                                │
│                                  Slower; 56-day strength                     │
│                                                                              │
│  GGBS        Blast furnace slag  Latent hydraulic: 30–70%   ~40–60%          │
│  (ground     (iron-making)       reacts with water                           │
│  granulated)                     + alkali activator                          │
│                                  → similar C-S-H                             │
│                                  Slower early; better                        │
│                                  long-term; low heat                         │
│                                                                              │
│  Silica fume Ferrochrome smelter Ultra-fine SiO₂ 5–15%     ~10–15%           │
│  (CSF)       industry            Highly reactive                             │
│  (≈ 150,000  off-gas             pozzolanic                                  │
│   m²/kg BET)                     Fills capillary pores                       │
│                                  Strength bonus                              │
│                                  Very sticky mix                             │
│                                                                              │
│  Metakaolin  Calcined kaolin     Reactive alumino-  10–20%  ~15–20%          │
│              clay (650°C)        silicate; pozzolanic                        │
│                                  Cleaner (white) concrete                    │
│                                                                              │
│  Limestone   Quarry dust         Filler + nucleation   Up to 15%  ~15%       │
│  filler      (CaCO₃ fine)        Not truly reactive                          │
│                                  EN 197: "Portland                           │
│                                  limestone cement"                           │
│                                                                              │
│  LIMITS ON REPLACEMENT:                                                      │
│  High FA or GGBS → slower early strength → later stripping of formwork       │
│  Carbonation resistance may decrease (less Ca(OH)₂ buffer)                   │
│  Alkali-silica reaction (ASR) risk: FA/GGBS REDUCES ASR risk                 │
│  Always verify with mix design testing at target w/b ratio                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Concrete Mix Design

### Mix Proportions

```
TYPICAL CONCRETE MIX PROPORTIONS (C30/37, w/c = 0.50)
──────────────────────────────────────────────────────────────────────────────
  Component            Typical quantity        Function
  ───────────────────  ─────────────────────   ──────────────────────────────
  Portland cement      280–350 kg/m³           Binder (with water: strength)
  Fly ash (optional)   70–100 kg/m³  (≈25%)    Pozzolanic SCM; reduce OPC
  Water                150–170 kg/m³           Hydration + workability
  Fine aggregate       700–800 kg/m³           Fills voids; workability
  Coarse aggregate     900–1100 kg/m³          Structural skeleton (10–20mm)
  Superplasticizer     2–5 L/m³                Workability without extra water
  Air entraining (if frost exposure): 4–6% air void content

  w/c = water / cement = 160/320 = 0.50 → C30/37 target

  FRESH CONCRETE TESTS:
  Slump test (EN 12350-2): 0 (S1) to 220 mm (S5) — workability measure
  Flow test (EN 12350-5): for self-compacting concrete (SCC)
  Air content (EN 12350-7): pressure meter for frost-resistant mixes

  HARDENED TESTS:
  Cube strength (EN 12390-3): 150mm cubes at 28 days
  Cylinder strength (ASTM): 150mm dia × 300mm; f_ck = 0.8 × cube strength
```

### Admixtures

| Admixture | Mechanism | Effect | When to use |
|---|---|---|---|
| Superplasticizer | Disperses cement particles | +150 mm slump at same w/c | Always (modern concrete) |
| Water reducer (normal) | As above, lower dose | +30–60 mm slump | Standard workability |
| Retarder | Delays C₃A and C₃S hydration | Extra working time | Hot weather; large pours |
| Accelerator (CaCl₂) | Promotes C₃S hydration | Early strength | Cold weather (not RC — chlorides attack steel) |
| Air entrainer | Surfactant → micro-bubbles | Freeze-thaw resistance | Exposed horizontal concrete |
| Shrinkage reducer | Reduces pore surface tension | -20–50% drying shrinkage | Slabs; restrained elements |
| Crystalline waterproofing | Seals capillaries | Low permeability | Basement walls; water-retaining |
| Set retarder (admixture) | As above | Ready-mix control | Long haulage distances |

---

## Reinforced Concrete: Structural Behaviour

### RC Beam: Bending Stress Distribution

```
RC BEAM: CRACKED SECTION ANALYSIS
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  UNCRACKED (elastic, before cracking):                                       │
│  ─────────────────────────────────── compression (top)                       │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ neutral axis                              │
│  ─────────────────────────────────── tension (bottom — concrete can carry)   │
│                                                                              │
│  AT CRACKING: concrete tensile strength ~3 MPa reached                       │
│  Cracks form at bottom fiber where tension is maximum                        │
│                                                                              │
│  CRACKED SECTION (in service):                                               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    compression block (concrete)             │
│  N.A. moves up (concrete below N.A. cracked; only steel works)               │
│  ═════════════════════════════════    steel rebar (in tension)               │
│                                                                              │
│  FORCE COUPLE (simplified):                                                  │
│  C = 0.85 f'c × b × a   (compression in concrete block)                      │
│  T = As × fy             (tension in steel)                                  │
│  C = T  →  solve for a (depth of compression block)                          │
│  M_n = T × (d - a/2)    (nominal moment capacity)                            │
│                                                                              │
│  DUCTILITY REQUIREMENT (ACI 318 / EN 1992):                                  │
│  Maximum reinforcement ratio ρ < 0.75 ρ_bal (ACI) or ε_s > 0.0025 (EC2)      │
│  → ensures steel yields before concrete crushes → ductile failure            │
│  → wide cracks give warning before collapse                                  │
│  → seismic: ρ further limited to ensure large ductility                      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Cover Requirements

```
CONCRETE COVER TO REINFORCEMENT (EN 1992-1-1)
──────────────────────────────────────────────────────────────────────────────
  COVER = minimum clear distance from rebar surface to outer concrete face
  FUNCTIONS:
    1. Fire protection: concrete insulates steel; specified fire resistance period
    2. Durability: prevents CO₂/Cl⁻ reaching steel before end of service life
    3. Bond: development length requires cover ≥ bar diameter

  EXPOSURE CLASSES (selected):
    XC1 (dry or permanently wet): cover ≥ 15 mm + ΔC_dev (10 mm)
    XC2 (wet/dry cycling):        cover ≥ 25 mm + ΔC_dev
    XC3/XC4 (carbonation risk):   cover ≥ 30–35 mm
    XD1 (chloride from road salt): cover ≥ 35 mm
    XD3 (high chloride):           cover ≥ 45 mm
    XS3 (marine splash zone):      cover ≥ 50 mm

  CARBONATION DEPTH MODEL:
    d(t) = k_c × √t   (Fick's 1st law simplified)
    k_c ≈ 1–3 mm/yr^0.5 for C30, normal exposure
    → 50-year carbonation depth: 1.5 × √50 ≈ 10 mm (good concrete)
    → 50-year depth in poor concrete: 3 × √50 ≈ 21 mm
    → 50-year cover must exceed carbonation depth with margin
```

### Shear Reinforcement (Stirrups)

```
SHEAR FAILURE MODES AND PREVENTION
──────────────────────────────────────────────────────────────────────────────
  DIAGONAL TENSION CRACKING:
  Shear + bending → principal tension at ~45° angle → crack propagates
    ╲  ╲  ╲  ╲  ╲ ← inclined cracks at 45° to beam axis
     ╲  ╲  ╲  ╲  ╲
  ═══════════════════
  ← stirrups cross these cracks → tension in stirrups → shear resistance

  STIRRUP FUNCTION:
  V_s = A_v × f_yt × d / s    (shear capacity from stirrups)
    A_v = stirrup area (both legs)
    f_yt = stirrup yield strength
    d = effective depth
    s = stirrup spacing

  FAILURE MODE WITHOUT STIRRUPS:
  Diagonal tension crack → splits beam → sudden (brittle) failure
  → no warning → catastrophic
  → minimum stirrups always required by code even if V_u < V_c (concrete capacity)

  IN SEISMIC ZONES (special moment frame beams, EN 1998):
  Close stirrup spacing ("seismic ties") throughout the plastic hinge region
  → confines concrete core → prevents core crush → maintains moment capacity
  → Eurocode: s ≤ min(8φ_l; 175 mm; bw/2) in critical zone
```

---

## Prestressed Concrete

Prestress is pre-induced compression that cancels service tension. The concrete never
sees net tension → no cracking → far better than RC for long spans and thin sections.

```
PRE-TENSIONING vs POST-TENSIONING
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  PRE-TENSIONING (factory, precast):                                          │
│  ─────────────────────────────────                                           │
│  1. Stress high-tensile steel strands between abutments                      │
│     f_pi = 0.75 f_pu = 0.75 × 1860 = 1395 MPa (typ. strand f_pu)             │
│  2. Pour concrete around strands; cure                                       │
│  3. Release strand → strand tries to shorten → bond transfers                │
│     compression to concrete → concrete pre-compressed (f_pe ≈ 1100–1200 MPa)│
│  Typical products: hollowcore slabs, bridge beams, railway sleepers          │
│                                                                              │
│  POST-TENSIONING (in situ or precast):                                       │
│  ──────────────────────────────────                                          │
│  1. Cast concrete with plastic ducts embedded (no strand yet)                │
│  2. Cure to target strength (usually f_ck ≥ 20 MPa before stressing)         │
│  3. Thread strands (tendons) through ducts                                   │
│  4. Jack against anchors cast into concrete ends → elongate tendons          │
│  5. Lock off jack → tendon force transferred via anchor plates               │
│  6. Grout ducts (bonded) or leave accessible (unbonded flat duct)            │
│  Applications: flat slabs (post-tensioned flat plate — most common in US/UK)│
│    large-span bridge decks, transfer plates, water-retaining structures      │
│                                                                              │
│  EFFECT OF PRESTRESS:                                                        │
│  Consider mid-span section under full service load:                          │
│  Without prestress:  bottom fiber in tension → CRACK                         │
│  With prestress:     prestress adds compression → net stress ≥ 0 → NO CRACK│
│                                                                              │
│  f_bottom = -P/A - P×e×c/I + M_applied×c/I                                   │
│    P = prestress force; e = eccentricity; A,I = section properties           │
│    → choose P and e so f_bottom ≥ -0.5√f_ck (tension limit under service)    │
│                                                                              │
│  LOSSES (significant; must account for):                                     │
│  Elastic shortening:    concrete shortens as force applied → strand follows  │
│  Friction (PT only):    duct wall friction reduces force along tendon        │
│  Anchorage draw-in:     strand slips slightly on locking off jack            │
│  Relaxation:            steel creeps under sustained tension → Δf_p = 2–5%   │
│  Creep:                 concrete creeps → shortens → strand loses tension    │
│  Shrinkage:             drying shrinkage → shortening → tension loss         │
│  Total long-term losses: typically 15–25% of initial jacking force           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Concrete Durability: Mechanisms of Deterioration

Durability is **reliability engineering for material degradation pathways**. Each mechanism below is a competing failure mode with a time-to-threshold distribution driven by mix quality, cover depth, and exposure environment. EN 1992 cover rules are reliability targets: ensure all failure-mode distributions have acceptably low probability of reaching the critical threshold within the specified service life (typically 50 or 100 years).

### Carbonation

```
CARBONATION MECHANISM AND CONSEQUENCES
──────────────────────────────────────────────────────────────────────────────
  Normal concrete pore solution pH: ~12.5–13.5
  → passive oxide film on steel: Fe → Fe₃O₄ (stable)

  Carbonation: CO₂ (atmospheric) diffuses into concrete pores
    CO₂ + Ca(OH)₂ → CaCO₃ + H₂O
    → pH drops from 12.5 to 9–10 in carbonated zone
    → passive film on steel dissolves → corrosion initiates

  Carbonation front: moves inward from surface with d = k√t
  Rate factors:
    High w/c → higher porosity → faster carbonation
    High SCM replacement → less Ca(OH)₂ buffer → faster carbonation
    Cyclic wet/dry → fastest carbonation rate
    Permanently submerged → essentially no carbonation (no CO₂ diffusion)

  Time to corrosion initiation:
    Service life model (fib MC2010): t_i = (c_nom/k_c)²
    → cover c governs; doubling cover → 4× longer initiation time
```

### Chloride Attack

```
CHLORIDE-INDUCED CORROSION
──────────────────────────────────────────────────────────────────────────────
  Sources: marine environment, de-icing salts on roads and car parks
  Mechanism:
    Cl⁻ ions diffuse through concrete pores
    At rebar surface: Cl⁻ concentration > threshold (≈ 0.4–0.6% of cement mass)
    → passive film breaks down locally → pitting corrosion initiates
    Fe → Fe²⁺ → Fe(OH)₂ → Fe₂O₃·H₂O (rust) → volume expansion ×3–6
    → splitting pressure → delamination → spalling → exposed rebar

  Diffusion: Fick's 2nd law
    C(x,t) = C_s × [1 - erf(x / 2√(D_cl × t))]
    D_cl = chloride diffusion coefficient (m²/s)
      Good concrete (low w/c, GGBS): D_cl ~ 1×10⁻¹² m²/s
      Poor concrete: D_cl ~ 1×10⁻¹⁰ m²/s → 100× faster ingress

  Protection strategies:
    Low w/c + GGBS or silica fume → reduced D_cl
    Increased cover (e.g., 50 mm in XS3 zone)
    Stainless steel or GFRP rebar (not affected by chlorides)
    Cathodic protection (applied current → suppress corrosion)
    Epoxy-coated rebar (NB: unreliable if coating damaged)
```

### Alkali-Silica Reaction (ASR)

```
ASR: THE CONCRETE CANCER
──────────────────────────────────────────────────────────────────────────────
  MECHANISM:
  Alkalis (Na₂O, K₂O) in cement → high pH pore solution
  Reactive silica in aggregates (chert, certain flints, opal, strained quartz)
  → at high pH: silica dissolves → silica gel forms around aggregate particles
  → gel absorbs water → swells → expansion pressure → map cracking (crazing)

  DIAGNOSIS: characteristic pattern called "map cracking" or "crocodile skin"
    Confirmatory: petrographic examination; gel under UV fluorescence
    Accelerated ASR test: 80°C in alkali solution; expansion measured

  PREVENTION (specified at mix design stage):
    Use low-alkali cement (Na₂O equivalent < 0.60%)
    Use pozzolanic SCMs: fly ash or GGBS → consumes alkalis + reduces pH
    Minimize cement content
    Avoid reactive aggregates (aggregate testing per BS 812-104)
    Once ASR starts: no cure; only structural assessment and management
```

---

## High-Performance and Ultra-High-Performance Concrete

```
HPC AND UHPC: WHAT CHANGES
──────────────────────────────────────────────────────────────────────────────
  NORMAL CONCRETE (C20–C40):  f_ck = 20–40 MPa; w/c = 0.45–0.65
  HIGH PERFORMANCE (HPC, C60–C100):  f_ck = 60–100 MPa; w/c = 0.25–0.40
    → silica fume (5–10%) fills capillary pores
    → superplasticizer maintains workability
    → aggregate selection critical (aggregate must not be weaker than paste)
    → denser microstructure → better durability; lower permeability

  ULTRA-HIGH-PERFORMANCE (UHPC):  f_ck = 150–200 MPa
    Ingredients:
      OPC: 700–900 kg/m³
      Silica fume: 200–250 kg/m³ (25–30% of cement)
      Steel fibers: 120–200 kg/m³ (1–3% by volume)
      Quartz sand: fine only (no coarse aggregate)
      Superplasticizer: 30–50 L/m³ (very high dose)
      w/b ≈ 0.15–0.22
    Thermal treatment at 90°C for 48 hours (accelerated curing)

    Properties:
      f_ck:     150–200 MPa compression
      Tensile:  8–25 MPa (steel fibers bridge cracks) → can replace rebar for small elements
      E:        ~50–60 GPa
      Permeability: essentially impermeable (chloride coefficient ~10⁻¹⁴ m²/s)
      Durability: 100-year + service life in aggressive environments

    Applications: bridge girders (Seonyu bridge, Seoul, 2002 — first UHPC footbridge);
      thin façade panels; joints between precast elements; complex thin-shell forms
```

---

## Concrete Pathologies Reference

| Problem | Cause | Signature | Solution |
|---|---|---|---|
| Carbonation corrosion | CO₂ → pH drop | Cracks parallel to rebar (delamination) | Increase cover; cathodic protection |
| Chloride corrosion | Salt ingress | Deep pitting; staining at cracks | Cathodic protection; sacrificial anode |
| ASR | Alkali + reactive silica | Map cracking; exuded gel | Structural assessment; control moisture |
| Delayed ettringite | High curing temperature + SO₄ | Internal swelling; cracking | Avoid >70°C curing; use low-C₃A cement |
| Freeze-thaw scaling | Water saturation + cycling | Surface scaling; aggregate pop-out | Air entrainment; low w/c; curing |
| Plastic settlement crack | Settlement of fresh concrete | Horizontal cracks over rebar | Reduce w/c; increase cover; revibrate |
| Plastic shrinkage crack | Surface drying before set | Random diagonal surface cracks | Curing compound; wind breaks; early cover |
| Bleed water channels | Bleed water migrates up | Vertical permeability channels | Reduce w/c; minimize bleed |
| Honeycombing | Poor compaction | Voids visible at surface or core | Proper vibration; revised mix |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| w/c = 0.60 vs 0.45 — same cement — strength difference? | Abrams' law: ~30–40% strength reduction; also much higher permeability |
| Use GGBS to 60% replacement — what changes? | Lower early strength; lower heat of hydration; better long-term durability; less CO₂ |
| Post-tension vs pre-tension — which for in situ slab? | Post-tension (tendons cast in, jacked after cure); pre-tension is factory only |
| Chloride environment — normal rebar or GFRP? | GFRP if severe (XS3/XD3); normal rebar if good cover and low w/c |
| Concrete spalling on soffits of 1960s car park — cause? | Carbonation + possibly chlorides from de-icing → rebar corrosion → spalling |
| Silica fume vs fly ash — key difference? | Silica fume: very fine, high reactivity, high strength; fly ash: cheaper, slower, lower strength gain |
| C₃A content — when does it matter? | Sulfate attack environments: use low-C₃A cement (SRPC: sulfate-resisting PC) |
| Prestress jacking force — why not just use higher force? | Tendon breaking load limit; concrete bearing capacity at anchor plates; losses are % of initial |

---

## Common Confusion Points

**Concrete strength is measured at 28 days — but it continues to increase.** The 28-day
cylinder/cube strength is the design reference. With GGBS, 90-day strength may be
20–40% higher than 28-day. C₂S hydration continues for years. OPC concrete at 10 years
may be 15–25% stronger than at 28 days — but this is not relied upon in design.

**The compression block in RC beam analysis is rectangular (simplified) not parabolic.**
The actual stress-strain curve of concrete in compression is parabolic. The Whitney
stress block (ACI 318) approximates this as a rectangle 0.85f'c deep to factor a = β₁×c.
Eurocode 2 uses a parabola-rectangle. For typical structural calculations, both give
the same moment capacity within 5%.

**Prestress eccentricity at the end of a beam causes problems.** At mid-span, the
prestress tendon is at maximum eccentricity (below N.A.) to maximize hog counter-
moment. At the beam ends, zero external moment → prestress with eccentricity → hogging
→ excessive camber and top fiber tension. Solution: either debond tendons at ends
(pre-tensioned) or profile the tendon up to end anchorage (post-tensioned).

**SCM replacement reduces Ca(OH)₂ — this is a durability trade-off.** Less portlandite
means less CO₂ buffering → faster carbonation front → less safe cover margin. High GGBS
(>70%) concretes in dry internal environments have faster carbonation; this is accepted
because the overall permeability reduction more than compensates in external/wet
environments. The exposure class dictates whether this trade-off is acceptable.

**Creep and shrinkage are not the same thing.** Shrinkage is time-dependent volume
change without load (drying shrinkage, autogenous shrinkage). Creep is additional
strain under sustained load. Both cause long-term deflection in RC beams. The total
long-term deflection multiplier is (1 + creep coefficient × load-dependent factor) for
creep, applied separately from shrinkage calculations.
