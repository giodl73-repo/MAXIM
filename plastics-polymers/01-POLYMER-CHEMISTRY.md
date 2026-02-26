# Polymer Chemistry: Chains, Mw/Mn, and Tg

## The Big Picture

```
+----------------------------------------------------------------------+
|               POLYMER CHAIN ARCHITECTURE                             |
|                                                                      |
|   MONOMER → POLYMERIZATION → CHAIN → BULK MATERIAL PROPERTIES       |
|                                                                      |
|   Monomer    Chain topology    Interactions     Observable           |
|   -------    --------------   ------------     ----------           |
|   Ethylene   Linear           van der Waals    Tg, Tm, E-modulus   |
|   Propylene  Branched         H-bonding        tensile strength     |
|   Styrene    Cross-linked     Pi stacking      creep, solubility    |
|   MMA        Block/graft      dipole           barrier properties   |
+----------------------------------------------------------------------+
```

Polymer chemistry is a structure-property discipline. The covalent structure of
the chain (monomer identity, stereoregularity, MW distribution) controls the
secondary and tertiary organization, which controls the macroscopic properties
you see in a datasheet.

---

## Polymerization Mechanisms

### Addition (Chain-Growth) Polymerization

Monomer adds to a growing chain end one unit at a time. No small-molecule
byproduct. High molecular weight builds quickly.

```
INITIATION    I* + CH2=CH2 → I-CH2-CH2*   (radical, cation, or anion)
                                   |
PROPAGATION   + n CH2=CH2  → I-(CH2-CH2)n*  (fast, repeating)
                                   |
TERMINATION   combination or disproportionation → dead chain
```

Three variants:

| Mechanism | Initiator | PDI | MW control | Examples |
|-----------|-----------|-----|------------|---------|
| Free radical (FRP) | Peroxides, AIBN | 1.5–3 | Poor | PS, PVC, LDPE, PMMA |
| Anionic | BuLi | ~1.05 | Excellent | SBS block copolymer, narrow-PDI PS |
| Cationic | Lewis acid, H+ | 1.5–2.5 | Moderate | PIB, POM |
| ATRP/RAFT (controlled) | CuBr/ligand | 1.1–1.3 | Good | Block copolymers, star polymers |

### Condensation (Step-Growth) Polymerization

Two functional groups react, expelling a small molecule (H2O, HCl, methanol).
MW builds slowly — need high conversion (>99%) to get high MW.

```
HO-R-COOH + HO-R-COOH → HO-R-CO-O-R-COOH + H2O   (ester)
HO-R-NH2  + HOOC-R-COOH → ...                       (amide = nylon)
```

Carothers equation: Xn = 1/(1-p) where p = fractional conversion.
At p = 0.99 (99%), Xn = 100 (still short).
At p = 0.999, Xn = 1000. This is why nylon/PET synthesis requires careful
water removal.

| Polymer | Reaction | Byproduct |
|---------|----------|-----------|
| PET | Terephthalic acid + ethylene glycol | H2O |
| Nylon 66 | Adipic acid + hexamethylenediamine | H2O |
| Polycarbonate | BPA + phosgene | HCl |
| Silicone | Dichlorosilane hydrolysis | HCl |

---

## Molecular Weight: Mw, Mn, and PDI

Every synthetic polymer is a mixture of chains of different lengths. We
describe the distribution statistically.

```
     MOLECULAR WEIGHT DISTRIBUTION

     (fraction)
        |    ___
        |   /   \
        |  /     \____
        | /           \___
        +---------------------> MW
              ^    ^
              Mn   Mw
```

**Number-average Mw (Mn)**: Arithmetic mean of all chains.
  Mn = Σ(Ni × Mi) / Σ(Ni)
  Sensitive to presence of short chains.
  Measured by osmometry, end-group analysis.

**Weight-average Mw (Mw)**: Each chain weighted by its mass.
  Mw = Σ(Ni × Mi²) / Σ(Ni × Mi)
  Sensitive to high-MW tail (long chains dominate viscosity).
  Measured by light scattering, SEC-MALS.

**PDI (Polydispersity Index)** = Mw/Mn

| PDI | Distribution | Typical source |
|-----|-------------|----------------|
| 1.0 | Monodisperse (theoretical) | Proteins — all identical |
| 1.05–1.15 | Very narrow | Anionic polymerization, ATRP |
| 1.5–2.0 | Moderate | Free radical in solution |
| 2.0 | Theoretical FRP limit (Flory) | Chain-transfer limited |
| 3–15 | Broad | LDPE (branching), coordinated Ziegler-Natta |
| >15 | Very broad | Degraded or multimodal blends |

**Why MW matters for properties**:

```
     PROPERTY vs. MOLECULAR WEIGHT

     Tensile strength  ____/‾‾‾‾‾‾‾‾‾     (plateaus at entanglement limit)
     Viscosity (melt)  ____________/         (~MW^3.4 above entanglement)
     Impact strength   ___/‾‾‾‾‾‾‾‾‾
     Ease of process   ‾‾‾\____________     (lower MW = easier flow)
                            ↑
                        critical Mw (entanglement threshold)
```

Typical Mc (entanglement MW): PE ~2,000 g/mol, PS ~31,000, PMMA ~30,000.
Above ~2–4× Mc: mechanical properties saturate; viscosity keeps climbing.

---

## Chain Stereoregularity (Tacticity)

For polymers with pendant groups (–CHR–CH2–)n, the spatial arrangement of R
groups relative to the backbone determines packing and crystallinity.

```
   ISOTACTIC:    all R on same side
   ...CH2-CHR-CH2-CHR-CH2-CHR...
                R   R   R

   SYNDIOTACTIC: R groups alternating
   ...CH2-CHR-CH2-CHR-CH2-CHR...
                R       R

   ATACTIC:      random R placement
   ...CH2-CHR-CH2-CHR-CH2-CHR...
                R   R
                        R
```

| Tacticity | Crystallinity | Properties | Example |
|-----------|---------------|------------|---------|
| Isotactic | High | Stiff, high Tm, opaque | iPP (commercial PP) |
| Syndiotactic | High | Stiff, high Tm | sPP (specialty) |
| Atactic | None (amorphous) | Flexible, transparent, lower Tm | aPP, PS, PMMA |

Ziegler-Natta catalysts produce isotactic PP (iPP). Free radical produces
atactic PP (useless waxy solid) — this is why FRP can't make useful PP.

---

## Glass Transition Temperature (Tg)

Tg is the most important single number for an amorphous or semi-crystalline
polymer's use temperature.

```
   PROPERTY vs. TEMPERATURE (amorphous polymer)

   E (modulus)
   |
   1000 MPa  |----\
             |     \      GLASSY       RUBBERY
             |      \     REGION       REGION
             |       \____
   1 MPa     |            ‾‾‾‾‾‾‾‾‾
             |
             +---------------------> T
                           ^ Tg
```

**Physical meaning of Tg**: Below Tg, chain segments cannot rotate on the
timescale of the measurement — frozen. Above Tg, cooperative segmental motion
unfreezes — the material flows, creeps, and dissipates energy.

Not a true thermodynamic phase transition — it's kinetic. Tg shifts with:
- **Cooling rate**: faster cooling → higher apparent Tg
- **MW**: lower MW → lower Tg (chain ends act as free volume plasticizers)
- **Plasticizers**: lower Tg (increases free volume)
- **Cross-linking**: raises Tg (restricts mobility)
- **Stiff backbone**: raises Tg (benzene rings in PC, PSU, PI → high Tg)
- **Flexible backbone**: lowers Tg (silicones, PDMS → Tg = –123°C)

Fox equation for copolymers / blends:
  1/Tg = w1/Tg1 + w2/Tg2   (weight fractions)

### Key Tg Values

| Polymer | Tg (°C) | Tm (°C) | Notes |
|---------|---------|---------|-------|
| PDMS (silicone) | –123 | –40 | Most flexible backbone |
| NR (natural rubber) | –73 | — | Below Tg at room T → elastic |
| LDPE | –100 to –80 | 110 | Mostly crystalline |
| PP (isotactic) | –10 | 165 | Semi-crystalline |
| PET | 80 | 260 | Semi-crystalline when oriented |
| Nylon 66 | 50–70 | 265 | Moisture-sensitive |
| ABS | 100–110 | — | Amorphous blend |
| PS | 100 | — | Amorphous |
| PMMA | 105 | — | Amorphous |
| PC | 147 | — | Amorphous (mostly) |
| PPS | 85 | 280 | Semi-crystalline, high-perf |
| PEEK | 143 | 343 | Semi-crystalline, highest class |
| Polyimide (PI) | >300 | — | Amorphous, extreme temp |

---

## Crystallinity

Some polymers organize into ordered lamella crystallites — but never 100%
crystalline (chain ends, entanglements, and defects always remain amorphous).

```
     SEMI-CRYSTALLINE STRUCTURE

     [amorphous]  [crystallite]  [amorphous]  [crystallite]

         ~~~~~    |=======|    ~~~~~~~~~    |=======|
         ~~~~~    |=======|    ~~~~~~~~~    |=======|
                  lamella               lamella
                  (folded chains)
```

Degree of crystallinity (χ_c) measured by:
- DSC (compare melting enthalpy to theoretical 100% crystal)
- X-ray diffraction (crystalline peak area / total area)
- Density (ρ_crystal and ρ_amorphous known)

| Polymer | χ_c (%) | Impact on properties |
|---------|---------|---------------------|
| LDPE | 40–55 | Flexible, hazy |
| HDPE | 65–80 | Stiff, opaque, good barrier |
| iPP | 60–70 | Stiff, hazy to opaque |
| PET (quenched) | <5 | Transparent, brittle |
| PET (oriented) | 25–40 | Tough, biaxial film |
| Nylon 66 | 35–45 | Strong, absorbs moisture |
| PEEK | 30–35 | Very stiff and tough |
| PS | 0 | Amorphous — always transparent |
| PC | ~0–5 | Mostly amorphous |

**Key insight**: Crystallinity and Tg interact. In a semi-crystalline polymer,
the crystallites act as physical cross-links, keeping the material stiff even
above Tg. The crystallites melt at Tm, causing the second major softening.

---

## Branching and Network Structure

```
   LINEAR          BRANCHED         CROSS-LINKED (NETWORK)
   ~~~~~~~         ~~~\             ~~~|~~~
   ~~~~~~~          ~~\~~           ~~|~~|~~
   ~~~~~~~            \~~            |~~|~~|
                  (long chain        (covalent network —
                  branches)          thermoset)
```

**LDPE branching**: Free radical at high pressure/temperature creates short-
chain and long-chain branches. Reduces crystallinity (40–55%) vs. HDPE (65–80%).
Long-chain branches dramatically increase melt viscosity at low shear rate
(strain hardening) — essential for film blowing and foam processing.

**HDPE**: Made with Ziegler-Natta or metallocene catalysts. Near-linear. High
crystallinity, higher density (0.95–0.97 g/cm³ vs. LDPE 0.91–0.93).

**Metallocene catalysts**: Single-site catalysts that produce very narrow PDI
(~2.0 or below) and precise control of comonomer incorporation. mLLDPE and
mPP are metallocene grades.

---

## Solution Behavior and Solubility Parameter

Hildebrand solubility parameter δ: square root of cohesive energy density.
"Like dissolves like" made quantitative.

Mixing condition: |δ_polymer − δ_solvent| < ~2 MPa^0.5 for good solubility.

| Polymer | δ (MPa^0.5) | Good solvents |
|---------|-------------|---------------|
| PE | 16 | Decalin (hot), cyclohexane (hot) |
| PS | 18.5 | Toluene, THF |
| PMMA | 19 | Acetone, THF |
| PC | 19.4 | DCM, chloroform |
| Nylon 66 | 27.8 | Formic acid, m-cresol |
| PTFE | 12 | Nothing practical |

PTFE's extreme chemical resistance: δ so low that no common solvent can match.

---

## Decision Cheat Sheet

| Question | Key parameter | How to measure |
|----------|--------------|----------------|
| Will it be brittle at use temperature? | Tg | DSC, DMA |
| Will it crystallize and become stiff? | Tm, χ_c | DSC, XRD |
| Will it flow easily in molding? | Melt Flow Index (MFI), Mw | MFI tester, GPC |
| How narrow is the MW distribution? | PDI = Mw/Mn | GPC (SEC) |
| Will it dissolve in solvent X? | δ, χ parameter | Hildebrand tables |
| Does cross-linking affect Tg? | ΔTg ~ cross-link density | DMA |
| Long-term creep resistance? | Entanglement density, χ_c | Creep test |

---

## Common Confusion Points

**Tg is not Tm**: Tg is a kinetic unfreezing of amorphous regions; Tm is
equilibrium melting of crystallites. PET has both: Tg ~ 80°C (go rubbery),
Tm ~ 260°C (melt crystallites). Above Tg and below Tm, PET is tough and
semi-rigid — exactly why bottles work.

**Higher MW is not always better**: Very high MW means very high melt viscosity.
UHMWPE (Mw > 3 million g/mol) cannot be injection molded — it must be sintered
or ram-extruded. Lower MW grades process easily but wear faster.

**PDI ≠ quality**: Broad PDI (like LDPE's 5–10) can be intentional — the short
chains act as internal lubricant, improving processability. Narrow PDI
(metallocene) gives better mechanical uniformity but may process differently.

**Crystallinity changes during processing**: Quench PET fast → amorphous
transparent. Anneal or orient → crystalline opaque. Same polymer, opposite
appearance. Controlled by cooling rate and draw ratio.
