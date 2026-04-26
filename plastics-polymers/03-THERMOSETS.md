# Thermosets: Epoxies, Polyurethanes, Phenolics

## The Big Picture

```
+------------------------------------------------------------------+
|                THERMOSET ARCHITECTURE                            |
|                                                                  |
|   TWO-COMPONENT     PRECURSORS      CURE REACTION    NETWORK     |
|   ─────────────     ──────────      ────────────     ───────     |
|   Resin + Hardener  Low-MW liquid   Exothermic       3D cross-   |
|   OR monomer +                      irreversible     linked      |
|   catalyst                          permanent        covalent    |
|                                                                  |
|   Once set, cannot melt or dissolve in most solvents             |
|   Properties: high Tg, low creep, dimensional stability          |
|                                                                  |
|   MAJOR FAMILIES:                                                |
|   Epoxy    Polyurethane    Phenolic    Unsaturated PE            |
|   Vinyl ester   Melamine   Cyanate ester   BMI                   |
+------------------------------------------------------------------+
```

The defining distinction from thermoplastics: covalent cross-links between
chains, not just entanglements. Once formed, the 3D network cannot be un-made
by heat. "Thermoset" = set by heat (or catalyst + heat).

---

## Crosslink Density and Tg

Crosslink density = moles of crosslinks per unit volume (ν_e).

```
   LOW CROSSLINK DENSITY         HIGH CROSSLINK DENSITY
   ─────────────────────         ──────────────────────
   ~~~|~~~                       ~|~|~|~
   ~~~~~                         ~|~|~
   ~~~|~~~                       ~|~|~|~
   Flexible rubber               Rigid glassy
   EPDM, silicone                Epoxy, phenolic
   Swells in solvent             Barely swells

   Tg increases with crosslink density (Flory-Fox relation):
   Tg = Tg∞ - K/Mc   (Mc = MW between crosslinks)
```

A highly crosslinked epoxy (Tg = 180°C) vs. a lightly crosslinked
polyurethane elastomer (Tg = –40°C) are both "thermosets" — the crosslink
density differs by ~100×.

---

## Epoxy Resins

### Chemistry

Most common: diglycidyl ether of bisphenol A (DGEBA) + amine hardener.

```
   DGEBA (the resin):
   CH2-CH-CH2-O-[BPA]-O-CH2-CH-CH2
      \O/                   \O/
   epoxide rings            epoxide rings

   Curing with amine hardener (e.g., TETA, DDM):
   Epoxide + R-NH2 → β-hydroxylamine linkage
   Each amine H reacts with one epoxide ring
   Two-component stoichiometry is critical
```

### Cure Chemistry and Stoichiometry

```
   Epoxide : Amine stoichiometry:
   ─────────────────────────────
   Too little hardener:  under-cured, low Tg, tacky
   Exact stoichiometry:  maximum crosslink density, maximum Tg
   Too much hardener:    excess amine, reduced Tg and strength

   Amine equivalent weight (AEW) = MW / number of active H
   Epoxide equivalent weight (EEW) = MW / number of epoxide groups
   Mix ratio = EEW / AEW by weight
```

### Hardener Types and Their Effects

| Hardener | Cure T | Tg range | Pot life | Notes |
|----------|--------|----------|----------|-------|
| Aliphatic amine (TETA, DETA) | RT–60°C | 80–120°C | 30–90 min | Fast, yellows |
| Cycloaliphatic amine (IPDA) | RT–80°C | 100–140°C | 60–180 min | Outdoor stable |
| Aromatic amine (DDM, DDS) | 120–180°C | 160–220°C | Hours–days | High-performance |
| Anhydride | 120–180°C | 120–180°C | Days | Low exotherm |
| Dicyandiamide (DICY) | 160–180°C | 120–150°C | Months | Latent, prepreg |
| Imidazole | 120–180°C | 140–180°C | Weeks | Catalytic + coreact |

### Epoxy Applications

```
   STRUCTURAL ADHESIVE      — 3M DP420, Huntsman Araldite
   PCB/ELECTRONICS          — FR4 laminate substrate
   AEROSPACE MATRIX         — carbon fiber prepreg systems
   TOOLING AND MOLDS        — precision tools, patterns
   COATINGS                 — marine, industrial, food-grade
   FLOOR COATINGS           — industrial warehouse floors
   POTTING/ENCAPSULATION    — electronic component protection
   WIND TURBINE BLADES      — infused with amine or anhydride cure
```

### Epoxy Property Ranges

| Property | Typical range |
|----------|--------------|
| Tg | 80–220°C (unreinforced) |
| Tensile modulus | 3–5 GPa |
| Tensile strength | 60–90 MPa |
| Compressive strength | 100–200 MPa |
| Elongation to break | 1–8% (brittle) |
| Fracture toughness K_Ic | 0.5–2.0 MPa·m^0.5 |
| Shrinkage on cure | 2–5% (volume) |

Brittleness is the main weakness. Tougheners: CTBN rubber (carboxyl-terminated
butadiene-acrylonitrile) particles, thermoplastic additions, or reactive
diluents can raise K_Ic to 3–5 MPa·m^0.5.

---

## Polyurethanes (PU)

### Chemistry: The Isocyanate Reaction

```
   R-NCO  +  HO-R'  →  R-NH-CO-O-R'
   isocyanate  polyol    urethane linkage

   The reaction is fast, exothermic, and moisture-sensitive:
   R-NCO  +  H2O  →  R-NH2 + CO2  (foam blowing reaction)
```

### The PU Family Tree

PU chemistry is enormously flexible because you control properties by
choosing the isocyanate and polyol types and MW:

```
   ISOCYANATE                POLYOL              → PRODUCT
   ──────────                ──────              ─────────
   TDI (2,4 / 2,6)          Polyether, MW 2000–6000  → Flexible foam
   MDI (4,4')                Polyether, MW 6000+      → Rigid foam
   MDI (4,4')                Short-chain diol, MW 400 → Elastomer
   HDI, IPDI (aliphatic)     Polyester polyol         → Coating, adhesive
   MDI prepolymer            Polyether diol           → Shoe sole TPU
```

### Flexible Foam

~35% of all PU. Mattresses, furniture cushions, automotive seating.

```
   MDI or TDI + High-MW polyether polyol (Mw ~ 3000–6000)
   + Water (blowing agent — CO2 from NCO + H2O reaction)
   + Amine / tin catalyst
   + Surfactant (cell stabilizer)
   ──────────────────────────────────────────────────────
   Rise time: 30–120 seconds
   Tack-free: 3–10 minutes
   Open-cell foam: density 15–60 kg/m³
```

### Rigid Foam

~25% of all PU. Insulation panels, refrigerator walls, spray-applied roofing.

```
   MDI + Low-MW polyol (Mw ~ 400–800, high OH number)
   + Physical blowing agent (HFCs, CO2, pentane)
   + Catalyst
   ────────────────────────────────────────────────
   Closed-cell foam: density 30–100 kg/m³
   λ thermal: 0.020–0.025 W/(m·K)  — better than EPS (0.033)
   Long-term insulation relies on trapped blowing agent gas
```

### Thermoplastic Polyurethane (TPU)

Linear PU, no cross-links. Can be melt-processed. Hard/soft block structure:

```
   [HARD SEGMENT]  [SOFT SEGMENT]  [HARD SEGMENT]
   MDI + chain     Polyether or    MDI + chain
   extender (BDO)  polyester diol  extender
   "physical x-link"               aggregates restrict
                                   soft segment flow
```

TPU is the basis of most premium shoe soles (Nike Air, Adidas Boost beads are
eTPU = expanded TPU), hose, film, TPU-coated fabrics.

---

## Phenolic Resins (Phenol-Formaldehyde)

### Historical Significance

**Bakelite (1907)**: First fully synthetic plastic. Leo Baekeland's phenol +
formaldehyde condensation under heat/pressure. Every early radio, telephone,
and electrical switch was phenolic. Still one of the largest-volume thermosets.

### Chemistry: Resole vs. Novolac

```
   RESOLE (base-catalyzed, F/P > 1)           NOVOLAC (acid-catalyzed, F/P < 1)
   ────────────────────────────────           ──────────────────────────────────
   Methylol groups on ring                    No methylol groups
   Self-condensing on heat/acid               Requires hexamine crosslinker
   One-step cure (heat alone)                 Two-step: make + cure separately
   Used: bonded composites, laminates         Used: molding compounds,
         plywood (resorcinol resol)                  brake pads, abrasive wheels
```

### PF Applications

```
   PLYWOOD BINDER          — interior and exterior grades (phenol resol)
   PCB SUBSTRATE (paper)   — FR1, FR2 (cheaper than epoxy/glass)
   BRAKE PADS              — novolac + graphite + friction modifiers
   ABRASIVE WHEELS         — novolac bonded grinding wheels
   MOLDING COMPOUNDS       — electrical switchgear, oven handles
   FIBERGLASS INSULATION   — glass wool binder (PFUF)
   RUBBER COMPOUNDS        — adhesion promoter for tire steel cord
   FOUNDRY BINDERS         — sand cores for casting
```

### Properties

```
   Phenolic thermoset:
   Tg: 150–350°C (depending on formulation)
   Tensile: 40–60 MPa
   Compressive: 100–200 MPa
   Excellent fire resistance (low smoke)
   Brown/black only (can't pigment)
   Water absorption: moderate
   Dimensional stability: excellent
```

---

## Unsaturated Polyester (UPE)

Not to be confused with saturated PET. UPE contains C=C double bonds in the
backbone:

```
   UPE backbone: ...–OOC-CH=CH-COO-(CH2)2–...
                           ^  reactive double bonds

   + Styrene monomer (40–60 wt%) = reactive diluent + co-monomer
   + Peroxide initiator (MEKP, BPO)
   → Free radical copolymerization through double bonds
   → Rigid cross-linked network
```

UPE is the workhorse of the marine/construction composites market (fiberglass
boats, bath surrounds, countertops, SMC/BMC automotive panels). Cheaper than
epoxy but lower performance — higher shrinkage, lower Tg (~80–120°C), higher
water absorption.

---

## Vinyl Ester

A hybrid: epoxy oligomer end-capped with methacrylate groups. Combines epoxy's
chemical resistance with UPE's styrene/peroxide cure. Higher cost than UPE but
better chemical resistance and toughness. Used in chemical processing equipment,
marine, and high-performance SMC.

---

## Thermoset Comparison

| Property | Epoxy | PU rigid | Phenolic | UPE | Vinyl ester |
|----------|-------|----------|----------|-----|-------------|
| Tg (°C) | 80–220 | 100–180 | 150–300 | 80–120 | 100–150 |
| Tensile (MPa) | 60–90 | 50–80 | 40–60 | 40–75 | 65–90 |
| Elongation (%) | 1–8 | 2–5 | 0.5–1 | 1–3 | 2–4 |
| K_Ic (MPa·m^0.5) | 0.5–2 | 0.5–1 | 0.3–0.7 | 0.3–0.6 | 0.5–1.0 |
| Shrinkage | Low | Low | High | High | Medium |
| Fire resistance | Moderate | Poor–mod | Excellent | Poor | Poor |
| Cost (relative) | High | Medium | Low | Low | Medium |
| Moisture resist. | Good | Moderate | Moderate | Poor | Good |

---

## Decision Cheat Sheet

| Need | Choose |
|------|--------|
| Structural adhesive (metal, concrete) | Epoxy |
| Aerospace matrix (carbon fiber) | Epoxy (amine or anhydride cure) |
| PCB substrate | Epoxy/glass FR4 |
| Flexible foam (cushion, mattress) | PU flexible foam |
| Rigid foam insulation | PU rigid foam or PIR (polyisocyanurate) |
| Shoe sole / athletic foam | TPU or eTPU |
| Plywood / particle board binder | Phenolic (resole) or UF resin |
| Brake pads / abrasive wheels | Phenolic (novolac) |
| Fiberglass boat / bath surround | UPE + glass fiber |
| Chemical storage tank (FRP) | Vinyl ester + glass fiber |
| Extreme temperature (>200°C) | Cyanate ester, BMI, polyimide |

---

## Common Confusion Points

**"Polyurethane" is not one material**: Flexible foam mattress, rigid foam wall
panel, TPU shoe sole, and PU floor coating are all "polyurethane" with radically
different properties. The word says nothing about the final property set.

**Stoichiometry matters for epoxy**: This is not like mixing paint. Off-
stoichiometry by 10% → significant Tg reduction (~20–40°C) and strength loss.
Always calculate by equivalent weight, not by intuition or convenience.

**Phenolic is the original and still dominant thermoset by volume**: People
associate thermosets with epoxy (aerospace, electronics). But phenolic (plywood,
brake pads, abrasive wheels) exceeds epoxy in global tonnage by a wide margin.

**UPE cure is inhibited by oxygen**: Oxygen at the surface scavenges the free
radicals, leaving a tacky surface after cure. Solution: add wax (migrates to
surface and excludes air) or use a peel ply in laminating.
