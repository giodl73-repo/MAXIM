# Additives: Stabilizers, Plasticizers, Fillers

## The Big Picture

```
+------------------------------------------------------------------+
|                 THE ADDITIVE UNIVERSE                            |
|                                                                  |
|   BASE POLYMER  +  ADDITIVES  =  COMPOUND                        |
|   ───────────────────────────────────────────────────────────    |
|                                                                  |
|   STABILIZERS                                                    |
|   Antioxidants · UV stabilizers · Heat stabilizers · Hydrolysis  |
|   → Prevent degradation during processing and service            |
|                                                                  |
|   PLASTICIZERS                                                   |
|   Phthalates · Citrates · Adipates · Polymeric                   |
|   → Soften and increase flexibility; lower Tg                    |
|                                                                  |
|   FILLERS AND REINFORCEMENTS                                     |
|   Carbon black · Silica · Talc · CaCO3 · Glass fiber · Mica    |
|   → Modify stiffness, strength, cost, color, conductivity        |
|                                                                  |
|   FUNCTIONAL ADDITIVES                                           |
|   Flame retardants · Colorants · Lubricants · Blowing agents     |
|   Coupling agents · Antistatic · Antimicrobial                   |
+------------------------------------------------------------------+
```

Real-world plastics are almost never pure polymer. Even "neat" PP contains
antioxidant packages (~0.1–0.3%). Complex compounds may have 15+ additive
components. Compounding is its own specialized discipline.

Units: phr = parts per hundred rubber/resin (mass basis).
       wt% = weight percent of total formulation.

---

## Stabilizers

### Antioxidants

Polymers degrade by oxidative chain scission or cross-linking. During melt
processing (200–320°C), thermal oxidation is the primary risk.

```
   OXIDATION MECHANISM (simplified):
   ──────────────────────────────────
   R-H + O2 → R• + HOO•         (initiation by heat/UV/metal ions)
   R• + O2  → ROO•              (peroxy radical)
   ROO• + R-H → ROOH + R•       (chain propagation — autocatalytic)
   ROOH → RO• + •OH             (hydroperoxide decomposition)
```

Two classes of antioxidants work complementarily:

```
   PRIMARY ANTIOXIDANTS (Hindered Phenols)
   ──────────────────────────────────────
   Irganox 1010, 1076, 1330, etc.
   Donate H• to peroxy radicals → terminate chain
   AO + ROO• → AO(-H)• + ROOH → stable products
   Used: 0.05–0.5 phr
   Long-term thermal stability

   SECONDARY ANTIOXIDANTS (Phosphites, Thiosynergists)
   ────────────────────────────────────────────────────
   Irgafos 168, DLTDP, DSTDP
   Decompose hydroperoxides before they generate radicals
   ROOH → ROH (phosphite: 1 P reduces 2 ROOH)
   Used: 0.05–0.5 phr
   Most active during processing (high-T)

   SYNERGISTIC BLENDS: Irganox 1010 + Irgafos 168 (1:2 to 1:3 ratio)
   Standard for polyolefins — protect both during processing and service
```

### UV Stabilizers

For outdoor applications, UV photons break C-C and C-O bonds.

```
   UV ABSORBERS (UVA)
   ─────────────────
   Benzophenones (BP-12), benzotriazoles (Tinuvin 327, 328)
   Absorb UV (290–400 nm) → convert to heat
   Used: 0.1–1 phr
   Must be in UV-exposed layer
   Leach out slowly — not permanent

   HINDERED AMINE LIGHT STABILIZERS (HALS)
   ────────────────────────────────────────
   Tinuvin 622, 770, Chimassorb 944
   Radical scavengers — catalytic mechanism (Denisov cycle)
   Not consumed in reaction — extremely long-lived
   Used: 0.1–0.5 phr
   Gold standard for outdoor polyolefins
   Cannot use in PVC (basic HALS reacts with HCl)

   COMBINATION UVA+HALS: complementary — UVA intercepts photons,
   HALS scavenges any radicals that form
```

### PVC Heat Stabilizers

PVC unique case: HCl release above ~100°C requires dedicated stabilizer system.

| Stabilizer type | Performance | Region |
|----------------|-------------|--------|
| Ca/Zn (calcium-zinc) | Good, food-contact approved | EU preferred |
| Organotin (DBTL, DOTE) | Excellent, transparent | EU (restricted in some) |
| Ba/Zn | Good, lowest cost | Non-food applications |
| Lead compounds | Best, cheapest | Banned EU 2015, declining globally |
| OBS (organic-based) | Emerging | Premium food/medical |

---

## Plasticizers

### Function

Plasticizers lower Tg by increasing free volume between polymer chains — small
molecules that insert between chains, reducing chain-chain interaction.

```
   PVC without plasticizer:  Tg ~ 80°C, rigid, brittle at RT
   PVC + 30 phr DEHP:        Tg ~ +5°C, flexible, leathery
   PVC + 60 phr DEHP:        Tg ~ –20°C, very soft, gel-like
```

Fox equation applies: 1/Tg(blend) = w_PVC/Tg_PVC + w_plast/Tg_plast

### Major Plasticizer Types

```
   PHTHALATES (most-used historically)
   ──────────────────────────────────
   DOP/DEHP (di-2-ethylhexyl phthalate): general purpose, low cost
   DINP, DIDP: higher MW, lower volatility, toys/food applications
   DINCH: non-phthalate, medical/food-contact, EU approved
   Concern: DEHP/DBP/BBP listed as endocrine disruptors → REACH restrictions

   TRIMELLITATES
   ─────────────
   TOTM (tri-2-ethylhexyl trimellitate)
   Low volatility, high-temperature wire insulation (125°C rating)

   ADIPATES and AZELATES
   ─────────────────────
   DOA (dioctyl adipate): food film, low-temperature flexibility
   Better Tg depression at low fractions than phthalates

   CITRATES
   ────────
   Triethyl citrate (TEC), acetyl tributyl citrate (ATBC)
   Food-contact, medical, non-toxic
   Higher cost than phthalates

   POLYMERIC PLASTICIZERS
   ──────────────────────
   Polyester type (adipic acid / glycol)
   Very low migration, low volatility
   Used in medical tubing (blood bags)
   Higher cost, harder to process
```

### Migration — The Core Problem

```
   PLASTICIZER MIGRATION MECHANISM:
   ──────────────────────────────────
   Small plasticizer molecules → not chemically bonded to PVC
   → diffuse to surface → evaporate or extract into contact media

   Effects:
   - Stiffening over time (loss of flexibility)
   - Odor / fogging (interior automotive)
   - Surface tackiness
   - Contamination of food, blood, drugs

   Solutions:
   - Higher MW plasticizers (lower diffusion coefficient)
   - Polymeric plasticizers (essentially non-migratory)
   - Cross-linking PVC (complicates processing)
   - Switch to polymeric TPE (TPU, SEBS) for critical applications
```

---

## Fillers and Reinforcements

### Distinction

```
   FILLER                          REINFORCEMENT
   ──────                          ─────────────
   Reduces cost, modifies texture  Significantly improves mechanical
   Minor effect on strength        properties
   CaCO3, talc (untreated)         Glass fiber, carbon black,
                                    surface-treated talc, clay
```

### Carbon Black

The most important filler in rubber and plastics:
- Primary particle: 10–500 nm diameter
- Structure: aggregates and agglomerates of primary particles
- Surface area: 30–1000 m²/g

```
   REINFORCING (high-surface-area, small particle):
   N110, N220, N330, N550 in tire nomenclature
   In rubber: doubles tensile strength, 4× abrasion resistance
   In PE/PP: UV protection (light barrier), black coloration

   CONDUCTIVE grades: provide electrical conductivity
   Carbon black percolation threshold: ~2–5 wt%
   Used: antistatic packaging, conductive cable jacket

   UV PROTECTION: 2–3% CB in PE pipe → ~50 yr outdoor lifetime
   Without CB: PE pipe fails in UV in 2–5 years
```

### Calcium Carbonate (CaCO3)

Most widely used filler by volume. Ground (GCC) or precipitated (PCC).

```
   UNTREATED CaCO3: poor adhesion to polymer, acts as stress concentrator
   STEARIC ACID COATED: improved dispersion, slight property improvement
   NANO-SIZED (PCC): genuine reinforcement — toughening PP/PET compounds

   Applications:
   PVC: window profile compounds (up to 80 phr) — reduce cost
   PP: automotive compounds (10–30%) — moderate stiffness, cost
   Rubber: extend carbon black (cheaper, lighter color possible)
```

### Talc (Mg3Si4O10(OH)2)

Platy particles (aspect ratio 5–20). Stiffens and improves heat distortion.

```
   Aspect ratio effect:
   Platy talc → aligns in flow → highest stiffness in flow direction
   PP + 20% talc: HDT 110°C vs. unfilled 100°C
                  Tensile modulus: 2.5 GPa vs. 1.5 GPa (unfilled)
   Trade-off: reduced impact strength, increased density
   Applications: automotive bumpers, dashboard panels, dishwasher parts
```

### Glass Fiber Reinforcement

Short glass fiber (chopped, 3–6 mm) or long glass (10–25 mm pellets) in
injection-molding compounds. Aspect ratio after molding: 10:1 to 50:1.

```
   PP + 30% GF (glass fiber):
   Tensile modulus:   5–7 GPa   (vs. 1.5 GPa unfilled)
   Tensile strength:  80–120 MPa (vs. 35 MPa unfilled)
   HDT:               145°C      (vs. 100°C unfilled)
   Shrinkage:         0.3–0.5%   (vs. 1.5–2.5% unfilled)
   Impact (notched):  8–15 kJ/m² (lower than unfilled in notched tests)

   Fiber orientation effect:
   Fibers align in flow direction → anisotropic properties
   In-flow tensile >> cross-flow tensile
   Must account in structural FEA (use fiber orientation tensors)
```

---

## Flame Retardants

Polymers are organic, hence flammable. Flame retardants (FRs) required for
electrical/electronic, building, automotive, textile sectors.

```
   HALOGENATED FR (most efficient):
   ─────────────────────────────────
   Brominated: TBBPA, PBDE (some banned), HBCDD
   Chlorinated: chlorinated paraffins
   Mechanism: gas-phase radical quenching of flame
   Synergy with Sb2O3 (antimony trioxide)
   Concerns: toxicity, persistence, EU RoHS restrictions

   PHOSPHORUS-BASED FR:
   ─────────────────────
   Ammonium polyphosphate (APP), red phosphorus, IFR systems
   Mechanism: char formation (condensed-phase barrier)
   APP + pentaerythritol: intumescent system → foam char layer
   Used in polyolefins, PU, coatings
   Good for halogen-free requirements

   MINERAL HYDRATES:
   ──────────────────
   ATH (aluminium trihydrate) and MDH (magnesium dihydroxide)
   Mechanism: endothermic dehydration, dilution with steam
   Al(OH)3 → Al2O3 + 3H2O  (absorbs 280 kJ/mol — at ~210°C)
   High loading needed: 40–65 wt% → reduces mechanical properties
   Halogen-free, low smoke — required for cable/wire in transit
```

---

## Lubricants and Mold Release

Internal lubricants: mix into polymer matrix to reduce melt viscosity and
chain-chain friction. Stearic acid, fatty acid amides (erucamide, oleamide).

External lubricants: migrate to surface to reduce polymer-metal friction.
Calcium stearate, PE wax, PTFE powder.

Anti-blocking agents (for film): SiO2 or talc particles in film surface — prevent
stacked film layers from sticking together.

Slip agents: erucamide, oleamide — bloom to film surface for smooth handling.

---

## Additive Interaction Matrix (Key Conflicts)

| Additive A | Additive B | Interaction |
|------------|------------|-------------|
| Halogenated FR | HALS UV stabilizer | Conflict — HX deactivates HALS |
| ATH | Processing above 210°C | ATH decomposes — cannot use in PP/PC |
| Lead stabilizer (PVC) | Modern compounds | Banned in EU/many markets |
| DEHP plasticizer | Medical / food contact | Regulatory restrictions |
| Carbon black | Photocatalytic TiO2 | CB absorbs UV → protects TiO2 |
| Acid scavenger (CaCO3) | Phosphite AO | Synergistic — CaCO3 scavenges HCl |

---

## Coupling Agents

Coupling agents are bifunctional molecules that chemically bridge the interface between inorganic filler/fiber and organic polymer matrix. Without them, glass-fiber or mineral-filled compounds have poor fiber-matrix adhesion and significantly lower mechanical properties.

```
   COUPLING AGENT MECHANISM
   ──────────────────────────
   Bifunctional molecule:
   [INORGANIC-REACTIVE END] — [ORGANIC-REACTIVE END]
         bonds to glass/             bonds to or
         mineral surface             compatibilizes
                                     with polymer

   SILANE COUPLING AGENTS (most common):
   General structure: X₃Si-R-Y
   X = hydrolyzable groups (methoxy, ethoxy) → hydrolyze to SiOH
       → condense with glass surface Si-OH groups → Si-O-Si bond to glass
   R = organic spacer (propyl, aminopropyl, etc.)
   Y = functional group reactive with specific polymer system

   SILANE SELECTION BY POLYMER SYSTEM:
   ─────────────────────────────────────
   System                    Silane                  Functional Group (Y)
   Epoxy + glass fiber       γ-GPS (A-187)           Glycidoxy (epoxide)
   Polyester + glass fiber   γ-MPS (A-174)           Methacrylate
   Nylon + glass fiber       γ-APS (A-1100)          Amine (H-bonds to amide)
   PP + glass fiber          γ-APS + MAH-PP          Amine + compatibilizer
   Rubber + silica           TESPT (Si-69)           Polysulfide (vulcanize)
   PVC + CaCO3               Titanate TC-9            Titanate (wet out)

   PROPERTY IMPROVEMENT WITH vs WITHOUT COUPLING AGENT:
   30% glass-fiber nylon 6 (PA6):
     Without coupling agent: tensile 120 MPa, elongation 3%
     With aminosilane:        tensile 185 MPa, elongation 5%
   Improvement: ~55% tensile strength, significantly better fatigue resistance
   Failure mode shift: from interfacial debonding (poor adhesion) to
                       fiber fracture (good adhesion) — the desired failure mode

   TITANATE COUPLING AGENTS:
   Structure: (RO)₄Ti or (RO)₃TiOX (organotitanates)
   Mechanism: react with surface -OH on mineral fillers (CaCO3, BaSO4, talc)
   Advantages vs silane:
     – Process at melt compounding temperature (no pre-treatment needed)
     – Effective on calcium carbonate and sulfates (silanes less effective here)
     – Reduce compound viscosity (better processing with high filler loading)
   Disadvantages:
     – More expensive than silanes
     – Color contribution (titanates can yellow)
     – Less well-characterized than silane-glass systems

   ZIRCONATE COUPLING AGENTS:
   Neoalkoxy zirconates: similar to titanates, higher hydrolytic stability
   Used in water-sensitive environments where titanates may hydrolyze

   PRACTICAL NOTES:
   Silane treatment of glass fiber: applied at fiber manufacturing (sizing)
   Silane treatment of filler: pre-treatment (dry or slurry) or in-situ
   Typical use level: 0.1–1.5 wt% on filler surface
   Verify with supplier: coupling agent must match polymer chemistry exactly
```

## Decision Cheat Sheet

| Need | Additive |
|------|---------|
| Long-term oxidation stability | Hindered phenol + phosphite blend |
| Outdoor UV stability (polyolefin) | HALS (Tinuvin 770/622) |
| Flexible PVC | DINP or DINCH (food/medical), TOTM (high T) |
| Low-cost stiff PP | Talc (10–30%) |
| High-stiffness PA/PP compound | Short glass fiber (30%) |
| UV-stable black PE pipe | 2–3% N330 carbon black |
| Flame retardant wire/cable (halogen-free) | ATH/MDH |
| Flame retardant engineering polymer | Brominated + Sb2O3 or P-based |
| Anti-blocking in film | SiO2 (1,000–3,000 ppm) |
| Antistatic packaging | CB (conducting) or antistatic amines |

---

## Common Confusion Points

**"Stabilized" is not a grade descriptor**: When a plastics distributor says
"UV-stabilized PP," they mean HALS has been added. Without a specific Tinuvin
grade and dosage in the spec, "UV-stabilized" could mean anything from 0.05%
to 0.5% HALS — a 10× range with very different outdoor service lives.

**Plasticizers are not cross-linkers**: They do the opposite — increase
mobility. Cross-linkers (DCP peroxide, sulfur) form covalent bonds. Plasticizers
are physically dispersed, non-reacted small molecules.

**Glass fiber degrades in a recycled melt**: Every extrusion pass breaks glass
fibers shorter. Recycled GF-PP loses ~30–50% of original fiber length per pass.
After 3–5 passes, reinforcing effect is negligible. Track recyclate history.

**Halogen-free doesn't mean toxin-free**: Phosphorus FRs can include TCEP
(known carcinogen). ATH/MDH are benign but heavy. "Halogen-free" is a
regulatory category, not a safety guarantee. Always check the full substance list.
