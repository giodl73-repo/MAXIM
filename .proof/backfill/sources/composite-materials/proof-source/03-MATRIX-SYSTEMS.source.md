---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-MATRIX-SYSTEMS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:composite-materials:matrix-systems
kind: guide
module: composite-materials
section: composite-materials
title: Matrix Systems: Thermoset and Thermoplastic
status: source-custody
source_custody: partial
current_path: composite-materials/03-MATRIX-SYSTEMS.md
canonical_path: composite-materials/03-MATRIX-SYSTEMS.md
backsource_ids: [proof-backfill:composite-materials:03-matrix-systems, git-history:composite-materials:03-matrix-systems]
concepts: [matrix, systems]
root_concepts: [matrix, systems]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Matrix Systems: Thermoset and Thermoplastic

## The Big Picture

```
+------------------------------------------------------------------+
|              COMPOSITE MATRIX LANDSCAPE                          |
|                                                                  |
|   THERMOSET (dominant, ~70% of composites matrix)                |
|   ────────────────────────────────────────────────               |
|   Epoxy         Vinyl ester    Phenolic        Cyanate ester     |
|   Benzoxazine   Bismaleimide   Polyimide (PMR-15)                |
|                                                                  |
|   Advantages:                  Disadvantages:                    |
|   Low viscosity (infusion)     Cannot re-melt or recycle         |
|   Good fiber wet-out           Long cure cycles                  |
|   High Tg possible             Brittle (toughening needed)       |
|   Stable shelf life            Exotherm risk in thick parts      |
|                                                                  |
|   THERMOPLASTIC (~30% and growing)                               |
|   ────────────────────────────────                               |
|   PEEK, PPS    PP, PA          PEKK, PAEK                        |
|                                                                  |
|   Advantages:                  Disadvantages:                    |
|   Recyclable                   High processing T (>300°C)        |
|   Toughness                    High melt viscosity               |
|   Fast consolidation           Expensive (PEEK)                  |
|   Weld-able parts              Fiber-matrix bonding challenge    |
+------------------------------------------------------------------+
```

---

## Epoxy — The Aerospace Standard

Epoxy thermosets dominate structural composites for aerospace, wind, marine,
and motorsport. Covered in depth in plastics-polymers/03-THERMOSETS.md.
Focus here on composite-specific aspects.

### Toughness and the Brittle Matrix Problem

Pure epoxy is brittle: fracture toughness KIc ~ 0.5–0.8 MPa·m^0.5.
Under cyclic loading, cracks propagate at low stress intensity. This limits
interlaminar fracture toughness of the composite.

```
   TOUGHENING MECHANISMS FOR COMPOSITE EPOXY:
   ─────────────────────────────────────────────
   1. RUBBER PARTICLE TOUGHENING:
      CTBN (carboxyl-terminated butadiene-nitrile) rubber dispersed in epoxy
      Phase-separates during cure → 1–5 µm rubber particles
      Crack tip: rubber particles cavitate and shear → absorb energy
      KIc improvement: 0.8 → 2.0 MPa·m^0.5 (+150%)
      Trade-off: reduced Tg, slightly lower modulus

   2. THERMOPLASTIC INTERLEAVES:
      Thin (25–75 µm) thermoplastic veils between prepreg plies
      PEI, polyamide, PSF particles or woven fabric
      Crack must propagate through these toughened interlayers
      GIc improvement: 200 → 600–1,000 J/m² (3–5×)
      Used: Hexcel 8552, Toray 3900-series prepregs
      Current aerospace standard for primary structure

   3. HYBRID RESIN SYSTEMS:
      Epoxy + bismaleimide (BMI) blends
      Epoxy + cyanate ester blends
      Fine-tune Tg, toughness, moisture resistance
```

### Key Aerospace Epoxy Systems

| System | Tg (dry) | Tg (wet) | Cure T | Toughness | Use |
|--------|---------|---------|--------|----------|-----|
| Hexcel 8552 | 200°C | 150°C | 180°C | High (interleaved) | A380, 787 primary |
| Toray 3900-2 | 185°C | 140°C | 180°C | Very high | 777 skin |
| Cycom 5215 | 160°C | 120°C | 135°C | Medium | Secondary structure |
| RTM6 (Hexcel) | 190°C | 145°C | 180°C | Medium | Resin infusion |
| Infumax (Solvay) | 200°C | 155°C | 180°C | High | Wind + aerospace RTM |

Tg (wet) = Tg after saturation in water at 70°C/14 days (critical for design)
Design must use wet Tg, not dry Tg, for elevated temperature allowables.

---

## Vinyl Ester

Hybrid between epoxy and unsaturated polyester. Epoxy oligomer chain with
methacrylate end groups. Cured by free radical polymerization (same as UPE).

```
   VINYL ESTER vs. UPE vs. EPOXY:
   ─────────────────────────────────
   Property       UPE    Vinyl Ester  Epoxy
   ─────────────────────────────────────────
   Tg (°C)        80–120  100–150      120–220
   Tensile (MPa)  45–75   65–90        65–90
   Elongation     1–3%    2–4%         1–8%
   Chem resist    Poor    Very good    Good
   Moisture res   Poor    Good         Good
   Shrinkage      High    Medium       Low
   Cost           Low     Medium       High
   Cure method    Peroxide Peroxide    Amine/anhydride
```

Applications: marine (fiberglass boat hulls where chemical and water resistance
needed), chemical processing FRP tanks and pipes, automotive panels where
polyester insufficient. Better than UPE for below-waterline marine.

---

## Phenolic Resin in Composites

Key advantage: phenolic composites are naturally flame-retardant with low
smoke and toxicity — critical for aircraft interiors, train interiors, mine shafts.

```
   PHENOLIC COMPOSITE PROPERTIES:
   ─────────────────────────────────
   Tg: 150–300°C (depending on formulation and cure)
   Tensile: 40–60 MPa (lower than epoxy)
   Compression: 80–150 MPa
   Heat release rate (HRR): very low — meets FAR 25.853
   LOI: 40–60% (excellent self-extinguishing)

   CHALLENGES:
   ────────────
   Cure byproduct: water (condensation reaction)
   → Volatile → void formation in thick sections
   → Must cure under high pressure (1.5–7 MPa) to suppress voids
   → Cannot infuse — only prepreg/press or hot press
   Color: brown/dark — cannot produce white or pastel composites
   Brittleness: lower toughness than epoxy
   Odor: formaldehyde residual during processing

   APPLICATIONS:
   ──────────────
   Aircraft floor panels (FAR 25.853 compliance)
   Rail vehicle interior panels (EN 45545 fire standard)
   Mining equipment (underground fire risk)
   Commercial kitchen equipment
```

---

## Bismaleimide (BMI)

Intermediate between epoxy and high-temperature polyimides.

```
   CHEMISTRY:
   ──────────
   Bis-maleimide + aromatic amine or allyl co-reactant
   Addition cure (no byproduct) → better void control than phenolic
   Requires high cure T: 160–200°C + post-cure at 200–230°C

   PROPERTIES:
   ────────────
   Dry Tg: 230–320°C
   Wet Tg: 180–270°C
   Tensile: 50–80 MPa
   Elongation: 1–3% (brittle)
   Chemical resistance: very good
   Cost: $30–80/kg resin

   WHERE EPOXY IS INSUFFICIENT:
   ──────────────────────────────
   Supersonic aircraft (fuselage surface at Mach 2–3: 150–200°C sustained)
   Hot section engine surrounds
   Stealth aircraft (special processing requirements)
   F/A-22 Raptor, F-35 (elevated T + chemical environment)
```

---

## Cyanate Ester

High-Tg, low moisture absorption — niche but growing in spacecraft.

```
   CYANATE ESTER PROPERTIES:
   ──────────────────────────
   Dry Tg: 250–400°C (highest of any practical composite matrix)
   Moisture absorption: 0.5–2.5% (vs. epoxy: 2–5%, BMI: 2–4%)
   Dielectric properties: εr ~ 2.7, very low loss tangent
   Cost: $50–150/kg

   APPLICATIONS:
   ──────────────
   Spacecraft structures (thermal stability + dimensional stability)
   RADAR and microwave transparent structures
   Millimeter-wave radomes and antenna reflectors
   Extremely low CTE structures for optical telescopes
   Often blended with BMI for balance of Tg + toughness
```

---

## Thermoplastic Matrices: PEEK and PPS

### PEEK (Polyether Ether Ketone) — The Aerospace Thermoplastic

Dominant thermoplastic composite matrix for high-performance applications.

```
   CF/PEEK COMPOSITE ADVANTAGES:
   ──────────────────────────────
   Recyclable (remelt → re-form)
   No cure cycle — consolidate under heat+pressure → cool
   Impact resistance: GIc ~ 1,500–2,000 J/m² (vs. 200–600 for epoxy)
   Fatigue resistance: superior to epoxy
   Chemical resistance: excellent (unlike epoxy)
   Water absorption: <0.5% (vs. epoxy 2–5%)
   Continuous service to 250°C

   CHALLENGES:
   ────────────
   Processing temperature: 380–400°C
   Equipment: requires specialized press or autoclave at high T
   Cooling rate: controlled (crystallization requirement — see 09-ADVANCED-POLYMERS)
   Cost: PEEK resin $80–200/kg, CF/PEEK prepreg $200–400/m²
   Fiber-matrix bonding: requires specific fiber sizing compatible with PEEK

   APPLICATIONS:
   ──────────────
   Airbus A380: ribs, brackets, clips (APC-2/AS4 CF/PEEK)
   A320 family: fire-stop panel areas
   Medical: implantable composite devices
   Racing: brake pads, gear components
   Oil & gas: downhole components
```

### PPS (Polyphenylene Sulfide) — The Affordable Thermoplastic Option

```
   CF/PPS PROPERTIES vs. CF/PEEK:
   ──────────────────────────────────
   Property        CF/PEEK     CF/PPS      CF/epoxy
   ─────────────────────────────────────────────────
   Service T       250°C       200°C       120–180°C
   Processing T    380°C       330°C       120–180°C
   GIc (J/m²)     1,500       800         200–600
   Tg/Tm (°C)     143/343     85/280      120–200 (Tg)
   Chemical res.   Excellent   Excellent   Good
   Cost (resin)    High        Medium      Low-Medium
   Recyclable      Yes         Yes         No

   Applications: Airbus A340/380 clips and brackets, automotive structural,
                 aerospace secondary structure where recyclability needed
```

### PP and PA Thermoplastic Composites (Automotive / Mass Market)

```
   CONTINUOUS FIBER THERMOPLASTIC (CFT) for automotive:
   ──────────────────────────────────────────────────────
   CF or GF + PA6, PA66, or PP matrix
   Consolidation: stamp forming (fast cycle: 1–3 min vs. 30–120 min epoxy)
   Recyclable → meets automotive end-of-life recyclability (85% by weight)

   Processes:
   - Thermoplastic prepreg stamping
   - Organosheet stamping: woven GF/PP or GF/PA sheet

   Applications: door modules, seatback structures, battery enclosures
   Performance: lower than CF/PEEK but acceptable for automotive loads
   Cost: moderate — high capital (stamping press), fast throughput

   Short fiber thermoplastic (SFRTP): GF/PP, GF/PA injection molded
   Very common automotive: not a "composite" in strict sense but overlaps
```

---

## Matrix Selection Decision Map

```
   SELECTION CRITERIA:
   ─────────────────────
   Temperature?
   ├── < 120°C: epoxy (room temp cure), UPE, vinyl ester
   ├── 120–180°C: standard epoxy prepreg (180°C cure)
   ├── 180–250°C: BMI, toughened epoxy (hot/wet allowables)
   ├── 250–300°C: PEEK, PPS (thermoplastic)
   └── > 300°C: cyanate ester, polyimide (BMI/CE blend), CMC

   Cost sensitive?
   ├── Very: UPE + E-glass (hand lay-up)
   ├── Moderate: vinyl ester or epoxy + glass infusion
   ├── Performance: epoxy + carbon prepreg
   └── No limit: PEEK + CF or cyanate ester + CF

   End-of-life recyclability required?
   ├── Yes: PEEK, PPS, PP, PA thermoplastic matrices
   └── No: any thermoset

   Fire performance (aircraft interior, transit)?
   ├── Yes: phenolic or intumescent-modified epoxy
   └── No: standard epoxy adequate

   Moisture resistance (marine, outdoor)?
   ├── Yes: epoxy or vinyl ester (not UPE)
   └── No: UPE acceptable for sheltered / short life
```

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Aerospace primary structure | Evaluate toughened epoxy, hot/wet `Tg`, damage tolerance, prepreg process, certification, and allowables. | Resin choice is inseparable from certified process and environment. |
| Wind-blade infusion | Compare low-viscosity epoxy, vinyl ester, infusion distance, pot life, exotherm, and cost. | A great cured resin can fail manufacturing if viscosity/window are wrong. |
| Marine immersion | Check vinyl ester vs UPE, hydrolysis resistance, osmotic blistering, glass compatibility, and repair. | Below-waterline exposure makes water resistance a primary design requirement. |
| Fire-critical interiors | Compare phenolic, BMI, smoke/toxicity, flame spread, processability, and mechanical tradeoffs. | Fire performance often trades against toughness and processing ease. |
| High-temperature service | Use BMI, cyanate ester, thermoplastic options, dry/wet `Tg`, oxidation, and thermal cycling. | Quote dry and wet `Tg`; moisture plasticization changes design margin. |
| Recyclable or weldable structure | Consider PEEK/PPS thermoplastics, melt processing, welding, impact toughness, and temperature. | Thermoplastics improve recyclability but raise processing temperature and equipment demands. |
| Automotive production | Compare GF/PP stamping, CF/epoxy RTM, cycle time, tooling, cost, and crash requirements. | Mass production rewards cycle time as much as material performance. |
| Low-cost civil composite | Use E-glass/UPE or vinyl ester, durability, UV/water exposure, inspection, and installation labor. | Cheapest resin is not cheapest lifecycle choice if durability fails. |

---

## Cross-References

- `01-FUNDAMENTALS.md` frames matrix systems as the load-transfer and environmental-protection phase.
- `05-MANUFACTURING.md` shows how matrix viscosity, cure, and processing window constrain fabrication.
- `09-END-OF-LIFE.md` follows thermoset and thermoplastic choices into repair, recycling, and disposal.

---

## Common Confusion Points

**Wet Tg is the design Tg**: Epoxy absorbs 2–5% moisture which plasticizes
and lowers Tg by 20–40°C. For an aircraft epoxy composite certified for 120°C
service, the actual Tg (dry) must be ~160–180°C. Always specify dry vs. wet
test conditions when quoting Tg data.

**Thermoplastic "fast processing" still needs high temperatures**: CF/PEEK
stamping at 380°C + tooling at 300°C + rapid cooling requires specialized
equipment. The processing is faster per-cycle than autoclave, but the capital
cost of heated press systems is high. "Fast" is meaningful at automotive volumes
(100,000+ parts/yr), not at aerospace volumes (1,000/yr).

**UPE and vinyl ester are not the same**: Vinyl ester is made from epoxy
oligomers with methacrylate end-caps — it cures the same way as UPE (peroxide)
but has much better chemical and moisture resistance because the reactive
groups are at the chain ends, not distributed throughout the backbone. For
below-waterline marine or chemical tanks, always use vinyl ester over UPE.
