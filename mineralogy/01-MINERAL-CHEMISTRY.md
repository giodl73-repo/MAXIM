# Mineral Chemistry and Bonding

## The Big Picture

```
+------------------------------------------------------------------+
|              MINERAL CHEMISTRY: THE LANDSCAPE                    |
|                                                                  |
|  COMPOSITION                    STRUCTURE                        |
|  (what atoms)                   (how arranged)                   |
|                                                                  |
|  Fixed formula ————————————————→ Crystal lattice                |
|   e.g., SiO₂                     e.g., hexagonal (quartz)       |
|                                   or amorphous (opal)            |
|                                                                  |
|  Solid solution ————————————————→ Same structure, variable X    |
|   e.g., (Mg,Fe)₂SiO₄ olivine     Fe-Mg swap continuously       |
|                                                                  |
|  Same composition —— POLYMORPHS → Different structures          |
|   C       → diamond (cubic) or graphite (hexagonal)             |
|   CaCO₃   → calcite (trigonal) or aragonite (orthorhombic)     |
|   SiO₂    → quartz / tridymite / cristobalite / coesite / ...  |
+------------------------------------------------------------------+
```

---

## Chemical Bonding in Minerals

The four bonding types produce drastically different mineral properties:

```
BONDING TYPES AND THEIR MINERAL CONSEQUENCES
+------------------------------------------------------------------+
|                                                                  |
|  IONIC BONDING                                                   |
|  Electrons fully transferred between atoms                       |
|  Electrostatic attraction between +/- ions                      |
|  → Moderately hard, brittle, good cleavage, dissolves in water  |
|  Examples: Halite (NaCl), fluorite (CaF₂), calcite (CaCO₃)    |
|                                                                  |
|  COVALENT BONDING                                                |
|  Electrons shared between atoms                                  |
|  → Very hard, poor cleavage, insoluble                          |
|  Examples: Diamond (C-C in 3D), quartz (Si-O), corundum (Al-O) |
|  Note: Diamond is the hardest mineral → purely covalent 3D net  |
|                                                                  |
|  METALLIC BONDING                                                |
|  Delocalized electron sea                                        |
|  → Soft to moderate, ductile, malleable, opaque, shiny         |
|  Examples: Native gold, copper, silver, platinum                 |
|                                                                  |
|  VAN DER WAALS (molecular) BONDING                              |
|  Weak intermolecular forces between layers                       |
|  → Very soft, perfect basal cleavage, greasy feel              |
|  Examples: Graphite (C layers), talc (Mg silicate sheets)       |
|                                                                  |
|  MIXED BONDING (most minerals)                                   |
|  Silicates: covalent Si-O + ionic Ca²⁺, Mg²⁺, etc.            |
|  Sulfides: largely covalent with metallic character             |
+------------------------------------------------------------------+
```

---

## Pauling's Rules — Why Mineral Structures Work

Linus Pauling (1929) derived five rules from electrostatics that predict stable ionic crystal structures. These govern most oxide, carbonate, phosphate, and silicate minerals.

**Rule 1: Radius Ratio Principle**

The coordination number (how many anions surround a cation) depends on the ratio of ionic radii:

```
CATION/ANION RADIUS RATIO → COORDINATION NUMBER
+--------------------------------------------------+
| r_c/r_a ratio  | Coord. # | Geometry            |
+--------------------------------------------------+
| 0.155–0.225    |    3     | Triangular (CO₃²⁻)  |
| 0.225–0.414    |    4     | Tetrahedral (SiO₄)  |
| 0.414–0.732    |    6     | Octahedral (MgO₆)   |
| 0.732–1.000    |    8     | Cubic               |
| ≥ 1.000        |   12     | Cuboctahedral       |
+--------------------------------------------------+

Si⁴⁺ in O²⁻: r_c/r_a ≈ 0.26 → tetrahedral coordination
→ This is why SiO₄ tetrahedra are the universal silicate building block
```

**Rules 2–5**: govern how polyhedra share corners/edges/faces; face-sharing destabilizes structures (reduces coordination); the principle of parsimony (few distinct cation environments per structure). These rules predict stability without quantum chemistry.

---

## Solid Solution Series

Minerals can substitute chemically similar ions within the same crystal structure up to certain limits. The substitution is controlled by:
- Similar ionic radius (within ~15%)
- Same valence, OR charge-coupled substitution

```
KEY SOLID SOLUTION SERIES
+------------------------------------------------------------------+
|  OLIVINE SERIES: (Mg,Fe)₂SiO₄                                  |
|  Forsterite ————————————————————→ Fayalite                     |
|  Mg₂SiO₄           continuous         Fe₂SiO₄                  |
|  (pale green)                          (black)                   |
|  Mg²⁺ and Fe²⁺ have nearly identical radii (0.72 vs 0.78 Å)    |
|                                                                  |
|  FELDSPAR SERIES: Two distinct series                           |
|  Albite ————————————————————→ Anorthite   (Plagioclase)        |
|  NaAlSi₃O₈                    CaAl₂Si₂O₈                      |
|  Na⁺ + Si⁴⁺ ↔ Ca²⁺ + Al³⁺  (charge-coupled substitution)     |
|                                                                  |
|  GARNET GROUP: Many end-members                                 |
|  Pyrope (Mg) ↔ Almandine (Fe) ↔ Spessartine (Mn)              |
|  Grossular (Ca-Al) ↔ Andradite (Ca-Fe) ↔ Uvarovite (Ca-Cr)    |
|                                                                  |
|  TOURMALINE: Most complex solid solution in common minerals     |
|  X Y₃ Z₆ (BO₃)₃ Si₆O₁₈ (OH,F)₄   where X,Y,Z have many sub. |
+------------------------------------------------------------------+
```

**Practical consequence**: A "mineral" like plagioclase feldspar has no fixed formula. XRF measurements give a composition; the name (albite/oligoclase/andesine/labradorite/bytownite/anorthite) is just a segment of the continuous series.

---

## Polymorphism — Same Formula, Different Structure

This is the mineralogical version of software abstraction: same interface, different implementation, dramatically different behavior.

```
POLYMORPHIC PAIRS AND TRIPLETS
+------------------------------------------------------------------+
|  CARBON (C)                                                      |
|  Diamond: cubic, each C bonded to 4 others in 3D tetrahedral    |
|    → Hardest natural substance (Mohs 10), electrically insulating|
|  Graphite: hexagonal layers, each C bonded to 3 in plane       |
|    → Softest sheet structure (Mohs 1–2), electrically conducting |
|  Lonsdaleite: hexagonal diamond — meteorite impacts only        |
|  Fullerene/nanotube: non-mineral but same element               |
|                                                                  |
|  CALCIUM CARBONATE (CaCO₃)                                      |
|  Calcite: trigonal; stable at Earth surface conditions          |
|    → Limestone, chalk, marble; biogenic shells                  |
|  Aragonite: orthorhombic; stable at high pressure               |
|    → Nacre (mother of pearl), some shells; converts to calcite  |
|    → Fossil shells: preservation means Ca-carbonate survived,   |
|       recrystallized form tells P-T history                     |
|                                                                  |
|  SILICON DIOXIDE (SiO₂)                                         |
|  Quartz: stable below 573°C, hexagonal; common everywhere       |
|  Tridymite: 573°C–870°C, hexagonal with different topology     |
|  Cristobalite: 870°C–1723°C (melting point)                    |
|  Coesite: very high pressure (>3 GPa); marker of meteor impact |
|  Stishovite: >10 GPa; Si in 6-fold coordination (not 4-fold)   |
|  Opal: amorphous (non-crystalline) — technically a mineraloid  |
|                                                                  |
|  ALUMINUM SILICATE (Al₂SiO₅)                                    |
|  Kyanite: high P/low T → bladed blue crystals                  |
|  Sillimanite: high P/high T → fibrous needles                  |
|  Andalusite: low P/low T → blocky prismatic crystals           |
|  Stability fields map directly to metamorphic P-T conditions    |
+------------------------------------------------------------------+
```

The Al₂SiO₅ polymorphs are metamorphic P-T indicators — which one is present tells you the pressure and temperature of metamorphism.

---

## Ionic Radii and Why They Matter

```
SELECTED IONIC RADII (in Ångströms)
+--------------------------------------------------+
| Ion      | Radius (Å) | Common coordination      |
+--------------------------------------------------+
| Si⁴⁺     |   0.26     | 4 (tetrahedral)          |
| Al³⁺     |   0.54     | 4 or 6 (can sub for Si)  |
| Fe³⁺     |   0.65     | 6 (octahedral)           |
| Fe²⁺     |   0.78     | 6 (octahedral)           |
| Mg²⁺     |   0.72     | 6 (octahedral)           |
| Ca²⁺     |   1.00     | 8                        |
| Na⁺      |   1.02     | 6–8                      |
| K⁺       |   1.38     | 8–12                     |
| O²⁻      |   1.40     | varies                   |
+--------------------------------------------------+

Mg²⁺ and Fe²⁺ (0.72 vs 0.78 Å) → substitutable → olivine solid solution
Si⁴⁺ and Al³⁺ (0.26 vs 0.54 Å) → substitute in tetrahedral sites only,
  but charge imbalance must be compensated (feldspars, micas)
Ca²⁺ and Na⁺ (1.00 vs 1.02 Å) → substitutable with charge coupling → plagioclase
```

**Incompatible elements**: elements too large (Rb⁺, Cs⁺, Ba²⁺) or too small/high charge to fit common mineral sites concentrate in late-stage melts and hydrothermal fluids → enriched in granites and ore deposits.

---

## Isomorphism vs. Polymorphism

```
+------------------------------------------+
|  ISOMORPHISM: same structure, different  |
|  chemical composition                    |
|                                          |
|  Mg₂SiO₄ and Fe₂SiO₄                   |
|  Both olivine structure — solid solution |
+------------------------------------------+

+------------------------------------------+
|  POLYMORPHISM: same composition,         |
|  different structure                     |
|                                          |
|  Diamond vs. graphite: both pure C       |
|  Calcite vs. aragonite: both CaCO₃      |
+------------------------------------------+
```

---

## Mineral Formulas — Reading Them

| Formula | Meaning | Mineral |
|---------|---------|---------|
| SiO₂ | 1 Si, 2 O | Quartz |
| NaAlSi₃O₈ | Na, Al, 3 Si, 8 O | Albite feldspar |
| (Mg,Fe)₂SiO₄ | Mg and Fe freely substitute | Olivine series |
| Ca(Mg,Fe)Si₂O₆ | Ca fixed, Mg/Fe vary | Diopside/hedenbergite |
| KAl₂(AlSi₃)O₁₀(OH)₂ | K in interlayer, Al-Si in tetrahedral sheets | Muscovite mica |
| Ca₅(PO₄)₃(F,OH,Cl) | F, OH, Cl substitute at one site | Apatite group |

**Parentheses** = elements substituting for each other at that structural site. **Brackets** = octahedral coordination site in some notations.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is diamond so hard? | Pure covalent 3D network — hardest possible bonding arrangement |
| Why is graphite a lubricant? | Van der Waals bonds between layers → layers slide easily |
| What controls which polymorph forms? | P-T conditions at time of crystallization; metastability common |
| What allows solid solution? | Similar ionic radius ± charge-coupled substitution |
| Why do some minerals dissolve in water? | Ionic bonding → water dipoles break the lattice apart |
| What does "Mg-rich olivine" mean thermally? | Forsterite has higher melting point than fayalite → crystallizes first from mafic melt |

---

## Common Confusion Points

**Allotropy vs. polymorphism**: In chemistry, allotropy is used for elements (diamond/graphite/fullerene are allotropes of carbon). In mineralogy, polymorphism covers both elements and compounds. Same concept, different vocabulary by discipline.

**Solid solution vs. intergrowth**: Solid solution means atoms substitute at the atomic scale — the lattice is uniform. Intergrowth (exsolution) means two distinct phases separate into lamellae — visible under microscope. Alkali feldspar can exsolve from a homogeneous high-T solid solution into alternating Na-rich and K-rich lamellae (perthite).

**Variable formula minerals**: Many minerals have formulas with parentheses indicating solid solution. The IMA species definition allows a certain compositional range. A mineral name like "actinolite" implies a composition range, not a single compound.

**Al in silicates**: Al³⁺ is unusual — it can substitute for Si⁴⁺ in tetrahedral sites (AlSi substitution), requiring charge compensation elsewhere. This creates the entire aluminum silicate/aluminosilicate family (feldspars, micas, zeolites, clays). Al can also occupy octahedral sites when not replacing Si.
