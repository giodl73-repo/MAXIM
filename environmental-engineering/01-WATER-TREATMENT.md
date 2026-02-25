# Drinking Water Treatment

## The Big Picture

Drinking water treatment is a sequence of unit processes — each one removes a different
class of contaminants. Design is driven by source water quality and regulatory requirements.

```
SURFACE WATER TREATMENT TRAIN (conventional)

  Source       Coagulation   Flocculation  Sedimentation  Filtration  Disinfection
  Water        (rapid mix)   (slow mix)    (clarifier)    (sand/      (Cl₂, UV,
  Intake                                                  anthracite) ozone)
    |               |              |              |            |           |
    v               v              v              v            v           v
  +------+      +-------+      +-------+      +-------+   +------+   +------+
  |Screen|  →   |Coag.  |  →   |Floccu-|  →   |Sedim. | → |Filter| → |Cl₂   | →  To
  |Intake|      |Basin  |      |lation |      |Basin  |   |      |   |CT    |   Distrib.
  |      |      |Alum/  |      |G=20-80|      |SOR    |   |2-5   |   |Residual   System
  +------+      |FeCl₃  |      |Gθ=    |      |0.5-1.0|   |gpm/  |   |      |
                |pH 6.5-|      |40k-   |      |gpm/ft²|   |ft²   |   +------+
                |7.5    |      |100k   |      |       |   |      |
                +-------+      +-------+      +-------+   +------+

                ←——— removes turbidity, colloids, algae ———→     → removes DBP
                                                                    precursors,
                                                                    pathogens

GROUNDWATER TREATMENT TRAIN (simpler — no turbidity burden)

  Well → Aeration (if Fe/Mn/H₂S) → Filtration → Disinfection → Distribution
  Possible additions: softening, nitrate removal, arsenic treatment
```

Regulatory driver: Safe Drinking Water Act (SDWA, 1974 + 1986/1996 amendments).
Primary regulations: NPDWRs (National Primary Drinking Water Regulations) — MCLs and
treatment technique (TT) requirements. Surface Water Treatment Rule (SWTR) mandates
99.99% Giardia removal (4-log) and 99.999% virus removal/inactivation (5-log).

---

## Source Water Characterization

Treatment train design starts with source water quality. Know your water before sizing anything.

```
  +------------------+--------------------+----------------------+
  | Parameter        | Surface Water      | Groundwater          |
  +------------------+--------------------+----------------------+
  | Turbidity        | Variable, 1–1000   | Typically <1 NTU     |
  |                  | NTU (storms spike) | (no treatment needed)|
  +------------------+--------------------+----------------------+
  | Color/NOM        | High (humic/fulvic | Generally lower      |
  |                  | acids → DBP precur)|                      |
  +------------------+--------------------+----------------------+
  | Pathogens        | Giardia, Crypto,   | Generally absent     |
  |                  | enteric viruses    | unless GWUDI         |
  +------------------+--------------------+----------------------+
  | Temperature      | Seasonal variation | Stable (≈mean        |
  |                  | affects coag/filt  | annual air temp)     |
  +------------------+--------------------+----------------------+
  | Hardness         | Varies             | Often high (limestone|
  |                  |                    | aquifers → CaCO₃ Sat)|
  +------------------+--------------------+----------------------+
  | Fe / Mn          | Low (aerobic)      | Often elevated       |
  |                  |                    | (reducing conditions)|
  +------------------+--------------------+----------------------+
  | Arsenic          | Generally low      | Geogenic — can be    |
  |                  |                    | high (>10 ppb) in    |
  |                  |                    | certain geologies    |
  +------------------+--------------------+----------------------+
  | PFAS             | Present near       | Present near AFFF    |
  |                  | industrial/AFFF    | sites, landfills     |
  +------------------+--------------------+----------------------+
```

GWUDI (groundwater under the direct influence of surface water): hydraulically connected to
surface water. Treated as surface water for regulatory purposes — requires full SWTR compliance
including filtration and CT disinfection.

---

## Coagulation

Colloidal particles in water are stabilized by electrostatic repulsion (negative surface charge).
Coagulation destabilizes them so they can aggregate.

```
  MECHANISM OF COAGULATION

  Colloid particles: negatively charged → repel each other → stable suspension

  Two destabilization mechanisms:

  1. CHARGE NEUTRALIZATION (dominant at lower doses)
     Al³⁺ or Fe³⁺ adsorb on particle surface → compress double layer
     → reduce repulsion → particles approach → van der Waals attraction
     takes over → aggregate

  2. SWEEP FLOC (dominant at higher doses — conventional treatment)
     Al(OH)₃(s) precipitate forms as amorphous floc
     → enmeshes and sweeps colloidal particles as it settles
     → less sensitive to exact dose — more robust for variable water quality

  Coagulants:
  ┌──────────────────────┬────────────────────────────────────────────┐
  │ Coagulant            │ Notes                                      │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Alum                 │ Al₂(SO₄)₃·14H₂O — most common,           │
  │ (aluminum sulfate)   │ lowers pH (consume alkalinity)             │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Ferric sulfate       │ Fe₂(SO₄)₃ — effective at wider pH range   │
  │                      │ than alum; produces denser sludge          │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Ferric chloride      │ FeCl₃ — similar to ferric sulfate         │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ PACl (polyaluminum   │ Pre-polymerized — less pH depression,     │
  │ chloride)            │ effective in cold water                    │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Cationic polymer     │ Used as primary coagulant or coagulant aid │
  │                      │ — expensive but no sludge increase         │
  └──────────────────────┴────────────────────────────────────────────┘

  Optimal pH: 6.5–7.5 for alum; 5.5–7.5 for ferric.
  Jar test: bench-scale optimization of dose, pH, and mixing —
  determines the coagulant dose before full-scale implementation.
```

---

## Flocculation

After charge destabilization, slow mixing grows the floc particles to a settleable size.

```
  MIXING INTENSITY — CAMP NUMBER

  G = velocity gradient (s⁻¹) = √(P / μV)
    P = power input (W), μ = dynamic viscosity (Pa·s), V = tank volume (m³)

  Rapid mix (coagulant addition): G = 300–800 s⁻¹, t = 10–60 sec
  Flocculation:                   G = 20–80 s⁻¹,  t = 15–30 min

  Camp number (dimensionless): Gt = G × detention time
  Design range for conventional flocculation: Gt = 40,000–100,000

  Too high G: shears floc apart (floc breakup > floc growth)
  Too low G:  slow particle collision rate, inefficient aggregation
  Optimal: tapered mixing — decreasing G as floc grows through tank stages
```

---

## Sedimentation

Floc particles settle by gravity. Design is governed by overflow rate (also called surface
loading rate, SLR), not detention time.

```
  SETTLING THEORY (Stokes' Law)

  v_s = g(ρ_p - ρ_w)d² / 18μ

    v_s = settling velocity (m/s)
    g   = gravitational acceleration
    ρ_p = particle density, ρ_w = water density
    d   = particle diameter
    μ   = dynamic viscosity

  KEY DESIGN INSIGHT: A particle is removed if v_s ≥ Q/A_s
    (overflow rate = flow / surface area)
  Doubling tank area — not depth — doubles removal.

  OVERFLOW RATE (SOR / SLR):
  Conventional horizontal flow:  0.5–1.0 gpm/ft² (1.2–2.5 m/h)
  High-rate settlers:            2–4 gpm/ft² (5–10 m/h)

  HIGH-RATE SETTLING OPTIONS:
  ┌──────────────────┬─────────────────────────────────────────────┐
  │ Type             │ Mechanism                                   │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ Tube settlers    │ Inclined tubes (60°) increase effective     │
  │                  │ settling area 5–10× per footprint          │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ Plate settlers   │ Parallel inclined plates — same principle  │
  │ (lamella)        │                                             │
  ├──────────────────┼─────────────────────────────────────────────┤
  │ DAF              │ Dissolved air flotation — low-density       │
  │                  │ particles (algae, oil) rise rather than     │
  │                  │ settle; air bubbles attach and float floc  │
  └──────────────────┴─────────────────────────────────────────────┘
```

---

## Filtration

Filtration is the polishing step — removes residual turbidity, floc, Giardia cysts, and
Cryptosporidium oocysts that pass through sedimentation.

```
  RAPID SAND FILTRATION (most common)

  Media cross-section (dual media, top to bottom):
  ┌──────────────────────────────────┐
  │ Anthracite coal  18–24"          │ ES 0.8–1.4 mm, UC <1.6
  │ (coarse, light)                  │ Captures large floc first
  ├──────────────────────────────────┤
  │ Sand             8–12"           │ ES 0.45–0.55 mm, UC <1.6
  │ (fine, dense)                    │ Final polishing
  ├──────────────────────────────────┤
  │ Gravel support layers            │
  └──────────────────────────────────┘
  Underdrain (perforated laterals or nozzles)

  DESIGN PARAMETERS:
  ├── Loading rate: 2–5 gpm/ft² (5–12 m/h)
  ├── Run length: 24–72 hours before backwash
  ├── Effluent turbidity target: <0.1 NTU (Crypto credit requires)
  └── Backwash: reverse flow at 12–20 gpm/ft² for 5–15 min to
      expand and clean media; surface wash assists

  FILTRATION MODES:
  ┌──────────────┬──────────┬─────────────────────────────────────┐
  │ Mode         │ Loading  │ When Used                           │
  ├──────────────┼──────────┼─────────────────────────────────────┤
  │ Conventional │ 2–5      │ After coag/floc/sed — standard      │
  │ filtration   │ gpm/ft²  │ surface water treatment             │
  ├──────────────┼──────────┼─────────────────────────────────────┤
  │ Direct       │ 2–5      │ High-quality source water — skip    │
  │ filtration   │ gpm/ft²  │ sedimentation; low turbidity source │
  ├──────────────┼──────────┼─────────────────────────────────────┤
  │ Slow sand    │ 0.05–0.1 │ Small systems; biological skin      │
  │              │ gpm/ft²  │ (schmutzdecke) does the work;      │
  │              │          │ excellent Giardia/virus removal;    │
  │              │          │ limited turbidity tolerance         │
  └──────────────┴──────────┴─────────────────────────────────────┘
```

---

## Disinfection

Disinfection kills or inactivates pathogens — the final barrier before distribution.
The key concept is CT: the product of concentration (C, mg/L) and time (T, min).

```
  CT CONCEPT

  Chick's Law: N_t = N_0 · exp(-k·t)
    N_t = pathogen concentration at time t
    k   = inactivation rate constant (depends on disinfectant + organism)

  Inactivation = exp(-k·C·t)  → depends on C×t = CT

  SWTR and LT2ESWTR specify required CT for each pathogen:
  Giardia 3-log: CT varies by temp and pH
    e.g., Cl₂ at pH 7, 15°C: CT = 73 mg·min/L
  Crypto 2-log (LT2): Cl₂ barely works; UV preferred
    UV dose for 2-log Crypto: 5.8 mJ/cm²
    UV dose for 4-log Crypto: 22 mJ/cm²
  Viruses 4-log: free chlorine very effective (CT ~6 at pH 6, 10°C)

  DISINFECTION OPTIONS:
  ┌──────────────┬─────────────────┬──────────────────────────────┐
  │ Disinfectant │ Pros            │ Cons                         │
  ├──────────────┼─────────────────┼──────────────────────────────┤
  │ Free         │ Effective, cheap│ THMs + HAA5s (DBPs);         │
  │ chlorine     │ residual in     │ less effective vs. Crypto;   │
  │ (Cl₂)        │ distribution    │ taste/odor at high doses     │
  ├──────────────┼─────────────────┼──────────────────────────────┤
  │ Chloramines  │ Lower DBP       │ Nitrification risk in dist.; │
  │ (NH₂Cl)      │ formation;      │ less virucidal than free Cl₂;│
  │              │ persistent resi-│ NDMA formation potential;    │
  │              │ dual in distrib │ "chloramine taste"           │
  ├──────────────┼─────────────────┼──────────────────────────────┤
  │ UV           │ No DBPs;        │ No residual — must combine   │
  │              │ excellent Crypto│ with Cl₂/chloramine;         │
  │              │ inactivation    │ turbidity must be low (<1 NTU│
  ├──────────────┼─────────────────┼──────────────────────────────┤
  │ Ozone        │ Powerful        │ Bromate formation (bromide   │
  │              │ oxidant; Crypto  │ in source water + O₃);      │
  │              │ effective;       │ no distribution residual;   │
  │              │ destroys taste/ │ high capital cost            │
  │              │ odor compounds  │                              │
  └──────────────┴─────────────────┴──────────────────────────────┘
```

### Disinfection Byproducts (DBPs)

DBPs form when disinfectants react with natural organic matter (NOM) in source water.

```
  NOM (humic/fulvic acids)  +  Cl₂  →  THMs  +  HAA5s  +  other DBPs

  TTHM (total trihalomethanes): MCL = 80 μg/L
    Chloroform (CHCl₃), bromodichloromethane, dibromochloromethane, bromoform
  HAA5 (five haloacetic acids):  MCL = 60 μg/L
    Monochloroacetic, dichloroacetic, trichloroacetic, mono/dibromoacetic

  Control strategies (DBP Rule compliance):
  ├── Reduce NOM before disinfection: coagulation (enhanced coag at lower pH),
  │   GAC adsorption, membranes
  ├── Move disinfection point later in train (after NOM removal)
  ├── Switch from Cl₂ to chloramine or UV (lower THM/HAA formation)
  └── Optimize distribution residence time (water age → DBP accumulation)
```

---

## Membrane Treatment

Membranes are defined by pore size and removal mechanism. Energy requirement increases
dramatically with tighter membranes.

```
  MEMBRANE SPECTRUM

  Pore size:   0.1 μm        0.01 μm      0.001 μm      0.0001 μm
               ┌──────────┬──────────────┬─────────────┬──────────┐
  Process:     │    MF    │      UF      │     NF      │    RO    │
               └──────────┴──────────────┴─────────────┴──────────┘
  Removes:     Turbidity   Turbidity+     NOM, divalent  Dissolved
               Cysts       viruses        ions, hardness  salts, PFAS
               Bacteria    Bacteria       (partial TDS)  TDS, nitrate

  Mechanism:   Size        Size           Size + charge  Diffusion
               exclusion   exclusion      exclusion      (dense membrane)

  Pressure:    5–30 psi    5–60 psi       50–150 psi    150–1000 psi

  Energy:      Low         Low            Moderate       High
               (gravity    (low pump)     (1–3 kWh/m³)  (3–10 kWh/m³)
               possible)

  Key metrics:
  ├── Recovery = Q_permeate / Q_feed  (typical RO: 75–85%)
  ├── Rejection = 1 - (C_permeate / C_feed)  × 100%
  └── Concentrate/brine: the rejected fraction must be managed
      (disposal options: sewer, deep injection well, evaporation pond,
       zero liquid discharge ZLD if geography requires)
```

### Reverse Osmosis in Data Center Context

Microsoft data centers in water-stressed regions (Phoenix, Singapore, Netherlands) use
RO-treated water for humidification and cooling tower makeup. Key considerations:

```
  ┌──────────────────────────────────────────────────────────────┐
  │ WATER BALANCE: DATA CENTER EVAPORATIVE COOLING              │
  │                                                              │
  │ Municipal  →  Pretreatment  →  RO  →  Cooling tower         │
  │ supply         (antiscalant,    ↓      makeup water          │
  │                softening)    Brine →  sewer or reuse         │
  │                              (15-25%)                        │
  │                                                              │
  │ Cycles of concentration (CoC): how many times minerals       │
  │ concentrate before blowdown                                   │
  │ CoC = TDS_blowdown / TDS_makeup                              │
  │ Higher CoC → less blowdown → less water wasted              │
  │ Limit: scaling (CaCO₃, SiO₂) and corrosion                  │
  │                                                              │
  │ Microsoft "Water Positive": consume less fresh water than    │
  │ returned/recharged in same basin — requires detailed water   │
  │ balance accounting per AWWA methodology                      │
  └──────────────────────────────────────────────────────────────┘
```

---

## PFAS Treatment

Per- and polyfluoroalkyl substances — the "forever chemicals" — are now regulated
at parts-per-trillion levels, transforming treatment design.

```
  PFAS BACKGROUND
  ├── ~12,000 compounds; PFOA + PFOS most studied
  ├── C-F bond: strongest in organic chemistry — does not degrade naturally
  ├── Bioaccumulative; linked to thyroid, kidney cancer, immunotoxicity
  └── Sources: AFFF (airport/military fire training), industrial discharge,
               landfill leachate, biosolids land application

  2024 PFAS MCL RULE (EPA, April 2024):
  ├── PFOA:  4 ppt (ng/L)  MCL
  ├── PFOS:  4 ppt          MCL
  ├── PFNA, PFHxS: 10 ppt  individual MCLs
  └── PFBS + GenX: hazard index ≤1 (combined)

  TREATMENT TECHNOLOGIES:
  ┌──────────────────┬────────────────────────────────────────────┐
  │ Technology       │ Notes                                      │
  ├──────────────────┼────────────────────────────────────────────┤
  │ GAC (granular    │ Adsorbs PFAS on carbon surface;           │
  │ activated        │ 90–99% removal for long-chain PFAS;       │
  │ carbon)          │ less effective for short-chain (PFBS);    │
  │                  │ exhausted carbon: reactivate or incinerate│
  │                  │ EBCT (empty bed contact time): 10–20 min  │
  ├──────────────────┼────────────────────────────────────────────┤
  │ Ion exchange     │ Single-use (PFAS-selective resin) or      │
  │ (IX resin)       │ regenerable (PFAS then concentrated);     │
  │                  │ very high removal including short-chain;  │
  │                  │ brine concentrate requires destruction     │
  ├──────────────────┼────────────────────────────────────────────┤
  │ High-pressure    │ NF/RO: >95% rejection of PFAS;           │
  │ membranes        │ concentrate problem — does not destroy;   │
  │                  │ used where low TDS is also needed         │
  ├──────────────────┼────────────────────────────────────────────┤
  │ PFAS destruction │ EMERGING: electrochemical oxidation,      │
  │ (emerging)       │ supercritical water oxidation (SCWO),    │
  │                  │ sonochemical, thermal desorption +        │
  │                  │ high-temp incineration (>1100°C)          │
  └──────────────────┴────────────────────────────────────────────┘
```

---

## Distribution System

Treatment plant effluent quality must be maintained through the distribution system to
the customer tap. Two key challenges: chemical stability and microbiological safety.

```
  DISTRIBUTION SYSTEM CHALLENGES

  ┌─────────────────────┬───────────────────────────────────────┐
  │ Challenge           │ Mechanism / Consequence               │
  ├─────────────────────┼───────────────────────────────────────┤
  │ Chlorine decay      │ Chick-Watson: Cl₂ reacts with NOM    │
  │ (residual loss)     │ and biofilm in pipes; minimum         │
  │                     │ residual required at all points:      │
  │                     │ free Cl₂ ≥0.2 mg/L (SDWA)           │
  ├─────────────────────┼───────────────────────────────────────┤
  │ DBP formation       │ Continues in distribution as Cl₂     │
  │ (water age)         │ reacts with residual NOM;             │
  │                     │ LRAA monitoring required               │
  ├─────────────────────┼───────────────────────────────────────┤
  │ Nitrification       │ With chloramine: ammonia released     │
  │                     │ supports nitrifier growth → chloramine│
  │                     │ depleted → loss of residual           │
  ├─────────────────────┼───────────────────────────────────────┤
  │ Lead leaching       │ Lead service lines + lead solder;    │
  │ (Lead & Copper Rule)│ Lead action level: 15 ppb at tap;    │
  │                     │ corrosion control treatment (CCT)     │
  │                     │ required; LSL replacement program     │
  ├─────────────────────┼───────────────────────────────────────┤
  │ Cross-connection    │ Backflow from irrigation, industrial  │
  │                     │ processes into potable system;        │
  │                     │ backflow prevention assemblies (RPZ,  │
  │                     │ double-check valve) required          │
  └─────────────────────┴───────────────────────────────────────┘
```

---

## Regulatory Summary

```
  RULE                   KEY REQUIREMENT
  ----                   ---------------
  SDWA (1974/1996)       Authorizes MCLs and TT requirements; primacy to states
  SWTR (1989)            4-log Giardia, 5-log virus log removal/inactivation;
                         turbidity <0.3 NTU in 95% of samples
  LT2ESWTR (2006)        Crypto-specific risk; additional log credit via UV or ozone
  DBP Rule Stage 2       LRAA (locational running annual average) monitoring;
  (2006)                 TTHM 80 μg/L, HAA5 60 μg/L
  Lead & Copper Rule     90th percentile lead ≤15 ppb; CCT; LSL inventory + replacement
  (1991/2021 Rev.)
  PFAS MCL Rule          PFOA/PFOS MCL = 4 ppt; PFNA/PFHxS = 10 ppt (April 2024)
  (2024)
  GWUDI                  GW hydraulically connected to SW → full SWTR compliance
```

---

## Decision Cheat Sheet

| Design Question | Answer |
|----------------|--------|
| Source water turbidity spikes to 500 NTU during storms | Conventional treatment (coag/floc/sed/filt) required; direct filtration not appropriate |
| Cold water (5°C) — coagulant choice | PACl over alum — more effective at low temp |
| Crypto in source water — disinfection credit | UV (5.8 mJ/cm² for 2-log) is most efficient; ozone works; free Cl₂ requires very high CT |
| PFAS detected at 8 ppt — treatment needed | GAC (EBCT 10–20 min) or PFAS-selective IX resin; RO if TDS reduction also needed |
| Hardness problem — best treatment | Lime softening (precipitation) or NF/RO membranes |
| DBP precursors high — how to reduce formation | Enhanced coagulation (lower coagulation pH) to remove NOM first; move Cl₂ addition point post-filtration |
| Distribution system lead problem | Corrosion control (pH/alkalinity adjustment, orthophosphate dosing); lead service line replacement |
| Small system (<500 connections) — simplest treatment train | Slow sand filtration + chlorination if source water quality permits |
| Sizing the sedimentation basin | Overflow rate controls — not detention time. Add tube/plate settlers to increase capacity without new basin |

---

## Common Confusion Points

**CT applies to the disinfection basin, not the whole plant**: CT credit is for the contact
chamber volume, not the total retention time in the plant. The 10% volume rule (T10) — the
time for 10% of a tracer to exit — accounts for short-circuiting. Regulators require
baffling factor demonstration.

**Turbidity vs. particle count**: Turbidity (NTU) is a surrogate for particles but is not
a direct measure. At low turbidities, particle counting (particles/mL) is more sensitive
for Crypto/Giardia breakthrough detection.

**RO brine is not "treated"**: RO produces clean permeate but concentrates everything into
a brine stream (15–25% of feed). That brine must be managed — it cannot simply be
discharged without an NPDES permit or other approved disposal pathway.

**Chloramine vs. free chlorine in distribution**: Switching to chloramine to reduce DBPs
at the plant does not eliminate all DBPs — some HAAs form faster with chloramines under
certain conditions. Nitrification risk increases. The tradeoff must be evaluated for the
specific distribution system.

**PFAS "removal" by treatment is really concentration/transfer**: GAC and IX resin
adsorb PFAS — they do not destroy it. The exhausted media then contains concentrated
PFAS and must itself be properly disposed (high-temperature incineration >1100°C or
permitted landfill). Treatment shifts the problem, it does not eliminate it.
