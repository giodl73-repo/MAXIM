# The Periodic Table — Overview & Framework

## The Big Picture

The periodic table is the single most compressed encoding of matter's behavior: 118 elements arranged
so that **every column shares a chemical personality** and **every row shares a quantum shell**.

```
                          THE PERIODIC TABLE — BLOCK MAP
 ┌────┬──────────────────────────────────────────────────────────────────────┬────────────────────┐
 │ s  │                                                                        │       p-block      │
 │    │                         d-block (transition metals)                   │                    │
 │blk │                                                                        │                    │
 ├────┼────┬────────────────────────────────────────────────────────────────┬─┴──┬──┬──┬──┬──┬────┤
 │ 1  │ H  │                                                                │ He │
 ├────┼────┤                                                                ├────┼──┼──┼──┼──┼────┤
 │ 2  │Li  │Be                                                              │ B  │C │N │O │F │Ne  │
 ├────┼────┤                                                                ├────┼──┼──┼──┼──┼────┤
 │ 3  │Na  │Mg                  Sc Ti V  Cr Mn Fe Co Ni Cu Zn              │ Al │Si│P │S │Cl│Ar  │
 ├────┼────┤                                                                ├────┼──┼──┼──┼──┼────┤
 │ 4  │K   │Ca                  Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd             │ In │Sn│Sb│Te│I │Xe  │
 ├────┼────┤                                                                ├────┼──┼──┼──┼──┼────┤
 │ 5  │Rb  │Sr                  Hf Ta W  Re Os Ir Pt Au Hg                │ Tl │Pb│Bi│Po│At│Rn  │
 ├────┼────┤                                                                ├────┼──┼──┼──┼──┼────┤
 │ 6  │Cs  │Ba  ──lanthanides── (La-Lu)                                   │ Nh │Fl│Mc│Lv│Ts│Og  │
 ├────┼────┤                                                                └────┴──┴──┴──┴──┴────┘
 │ 7  │Fr  │Ra  ──actinides──── (Ac-Lr)
 └────┴────┘
         │
         └── f-block (lanthanides + actinides, usually pulled below)

 BLOCKS:  s = Groups 1-2        p = Groups 13-18
          d = Groups 3-12       f = lanthanides + actinides
```

---

## Periodic Law

**Original (Mendeleev, 1869):** Properties of elements are a periodic function of their atomic weight.
**Modern:** Properties are a periodic function of their **atomic number** (proton count).

The modern restatement fixed Mendeleev's ordering anomalies (e.g., Te before I despite higher mass —
tellurium has 52 protons, iodine 53; the *number* of protons always gives the right ordering).

### The Prediction Story

Mendeleev left **gaps** for elements he predicted must exist based on pattern breaks in his table:

| Mendeleev's name | Predicted (1871) | Element discovered | Year |
|-----------------|-----------------|-------------------|------|
| eka-boron | At. wt ~44, metallic oxide X₂O₃ | Scandium (Sc, Z=21) | 1879 |
| eka-aluminium | At. wt ~68, liquid metal | Gallium (Ga, Z=31) | 1875 |
| eka-silicon | At. wt ~72, semiconductor | Germanium (Ge, Z=32) | 1886 |

He predicted density, melting point, and likely compounds — with remarkable accuracy. This is why
the periodic table is considered one of science's greatest predictive frameworks.

---

## Electron Configuration

### Quantum Numbers Recap

```
n  = principal quantum number  (shell: 1, 2, 3, ...)
l  = angular momentum          (subshell: 0→s, 1→p, 2→d, 3→f)
mₗ = magnetic quantum number   (-l to +l: orbital orientation)
mₛ = spin                      (+½ or -½)

Subshell capacities:
  s → 1 orbital  → 2 electrons
  p → 3 orbitals → 6 electrons
  d → 5 orbitals → 10 electrons
  f → 7 orbitals → 14 electrons
```

### Aufbau Filling Order

Fill orbitals from lowest to highest energy. Energy ordering does NOT follow n alone — the (n+l)
rule (Madelung's rule) governs:

```
FILLING ORDER (energy increasing):
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p

Memory device — diagonal arrows:
    1s
    2s  2p
    3s  3p  3d
    4s  4p  4d  4f
    5s  5p  5d  5f
    6s  6p  6d
    7s  7p
    ↗ read diagonals: 1s | 2s | 2p,3s | 3p,4s | 3d,4p,5s | ...
```

### Pauli Exclusion Principle
No two electrons in the same atom can have identical sets of all four quantum numbers.
Each orbital holds exactly **2 electrons**, with opposite spins.

### Hund's Rule
Within a degenerate set of orbitals (same n,l), electrons fill singly before pairing.
Each unpaired electron occupies its own orbital, all with parallel spins.

```
Carbon 1s²2s²2p²:
  2p: [↑][↑][ ]     ← Hund's rule (not [↑↓][ ][ ])
```

### Exceptions to Aufbau (notable)

Half-filled and fully-filled d subshells are extra stable:

| Element | Expected | Actual | Reason |
|---------|----------|--------|--------|
| Cr (24) | [Ar] 3d⁴4s² | [Ar] 3d⁵4s¹ | Half-filled d (5 paired) more stable |
| Cu (29) | [Ar] 3d⁹4s² | [Ar] 3d¹⁰4s¹ | Full d shell more stable |
| Mo (42) | [Kr] 4d⁴5s² | [Kr] 4d⁵5s¹ | Same as Cr |
| Ag (47) | [Kr] 4d⁹5s² | [Kr] 4d¹⁰5s¹ | Same as Cu |

---

## The Four Blocks

```
┌─────────────────────────────────────────────────────────────────────────┐
│  s-BLOCK (Groups 1-2)                                                    │
│  Filling: ns subshell                                                    │
│  Elements: H, He, Li, Na, K, Rb, Cs, Fr (Group 1)                      │
│            Be, Mg, Ca, Sr, Ba, Ra (Group 2)                             │
│  Character: metals (except H/He), low IE, highly reactive               │
├─────────────────────────────────────────────────────────────────────────┤
│  p-BLOCK (Groups 13-18)                                                  │
│  Filling: np subshell                                                    │
│  Elements: B through Rn (and 113-118)                                   │
│  Character: most diverse block — metals, metalloids, nonmetals,         │
│             halogens, noble gases                                        │
├─────────────────────────────────────────────────────────────────────────┤
│  d-BLOCK (Groups 3-12) — Transition Metals                              │
│  Filling: (n-1)d subshell (note: one shell back)                        │
│  Elements: Sc-Zn (3d), Y-Cd (4d), Hf-Hg (5d), Rf-Cn (6d)             │
│  Character: metals, variable oxidation states, colored compounds,       │
│             catalytic activity, d-d transitions                         │
├─────────────────────────────────────────────────────────────────────────┤
│  f-BLOCK (Lanthanides + Actinides)                                      │
│  Filling: (n-2)f subshell (two shells back)                             │
│  Lanthanides: La-Lu (4f)     Actinides: Ac-Lr (5f)                     │
│  Character: very similar chemistry within each series (hard to          │
│             separate), lanthanides mostly +3, actinides more variable   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Periodic Trends — The Seven Core Trends

### 1. Atomic Radius

```
ATOMIC RADIUS trends:

  DECREASES →  across a period (left to right)
  INCREASES ↓  down a group

  Li  Be  B   C   N   O   F
 167 112  87  77  75  73  72  pm (covalent radii, approximate)

  Li
 167
  Na
 190
  K
 243

Why across period: same shell, but Z (nuclear charge) increases → stronger pull → smaller radius
Why down group:    new shell added → more shielding → nucleus farther from valence electrons

EXCEPTION ALERT: Half-filled p shells (N, P, As) are slightly larger than expected
because Hund's rule leaves all p orbitals singly occupied → less electron-electron repulsion.
```

### 2. Ionization Energy (IE)

Energy required to remove the outermost electron from a neutral gaseous atom.

```
  INCREASES →  across a period
  DECREASES ↓  down a group

IE₁ (kJ/mol) across Period 2:
  Li    Be    B     C     N     O     F     Ne
  520   899   801   1086  1402  1314  1681  2081

Notable DIP: Be → B (drops from 899 to 801)
  B's outermost electron is in 2p, higher energy than Be's 2s → easier to remove

Notable DIP: N → O (drops from 1402 to 1314)
  O has two electrons in one 2p orbital (paired) → extra repulsion → easier to remove

Successive IEs jump sharply when you reach a new shell:
  Na: IE₁=496, IE₂=4562 → that's the Na⁺ → Na²⁺ gap (removing from n=2 core)
```

### 3. Electron Affinity (EA)

Energy released when a neutral atom gains one electron.

```
  GENERALLY INCREASES → across a period (more negative EA = more favorable)
  GENERALLY DECREASES ↓ down a group

Exceptions:
  - Group 2 (Be, Mg): completely filled s → negative (unfavorable) EA
  - Group 15 (N, P): half-filled p → negative EA (Hund's rule stability)
  - Group 18: completely filled → near-zero EA

Highest EA: Cl (−349 kJ/mol) — NOT F, because F's small size → electron-electron repulsion
```

### 4. Electronegativity (Pauling Scale)

```
  INCREASES →  across a period
  DECREASES ↓  down a group

  F   O   N   Cl  Br  I   S   C   H   P   Si  B   Ge  As  Al  Na
 3.98 3.44 3.04 3.16 2.96 2.66 2.58 2.55 2.20 2.19 1.90 2.04 2.01 2.18 1.61 0.93

Francium has the lowest: ~0.7
Fluorine has the highest: 3.98

BOND CHARACTER based on ΔEN:
  ΔEN < 0.4   → nonpolar covalent
  0.4–1.7     → polar covalent
  > 1.7       → ionic (approximate threshold)
```

### 5. Metallic Character

```
  DECREASES →  across a period
  INCREASES ↓  down a group

  Metals:     left side + bottom (good conductors, lose electrons, form cations)
  Metalloids: diagonal staircase (B, Si, Ge, As, Sb, Te, Po, At — semiconductor behavior)
  Nonmetals:  top right (gain electrons, form anions or share)

STAIRCASE position (approximate):
   B
  Si  Al is metal (below)
 Ge  As
Sb  Te
 Po  At
 (At is to the right of the staircase but is sometimes listed as metalloid)
```

### 6. Melting/Boiling Point Trends

Unlike the above trends, this one is NOT monotonic — it depends on bonding type:

```
Period 3 melting points (°C):
  Na   Mg   Al   Si   P    S    Cl   Ar
  98  650  660  1414  44  119  -101 -189

Why the peak at Si? Silicon forms a covalent network (diamond-cubic lattice).
Metals peak at Group 6 in d-block (W = 3422°C), then drop.
```

### 7. Oxidation State Range

```
Maximum oxidation state typically = group number (for main-group elements)
Minimum oxidation state typically = group − 8 (for nonmetals)

  Group 1:  +1 only
  Group 2:  +2 only
  Group 17: −1 to +7 (F is exception: only −1, most electronegative)
  Group 16: −2 to +6
  Transition metals: highly variable (Fe: +2/+3/+6, Mn: +2 through +7)
```

---

## Reading Element Data

Every element entry encodes:

```
        12
        C           ← Symbol (1-2 letters, first capitalized)
      Carbon        ← Full name
      12.011        ← Standard atomic weight (weighted average of natural isotopes)

Key data points:
┌──────────────────────────────────────────────────────┐
│  Atomic number (Z)    = number of protons            │
│  Mass number (A)      = protons + neutrons           │
│  Atomic weight        = weighted avg of all isotopes │
│  Electron config      = subshell notation            │
│  Oxidation states     = typical stable charges       │
│  Electronegativity    = Pauling scale                │
│  Ionization energy    = kJ/mol (first)               │
│  Atomic radius        = pm (various definitions)     │
│  Phase at STP         = solid/liquid/gas             │
│  Category             = metal/metalloid/nonmetal     │
└──────────────────────────────────────────────────────┘
```

### Isotope Notation

```
  ᴬ_Z X   or   X-A

  ¹²C  =  C-12  = carbon with 12 nucleons (6p + 6n)  ← 98.9% natural abundance
  ¹³C  =  C-13  = carbon with 13 nucleons (6p + 7n)  ← 1.1% natural abundance
  ¹⁴C  =  C-14  = carbon with 14 nucleons (6p + 8n)  ← trace, radioactive (t½ = 5730 yr)
```

---

## Nuclear Stability Overview

```
CHART OF NUCLIDES (stability landscape):

        ┌─────────────────────────────────────────┐
     N  │  .                                       │
  (neu- │    ..   β⁻ decay region                 │
  trons)│      ....   (too many neutrons)          │
        │         ......                           │
        │            ........  STABLE BAND         │
        │              ..........  ("valley of     │
        │                ..........  stability")   │
        │                  .......                 │
        │                    ..  β⁺/EC region      │
        │                      .  (too few         │
        │                        .  neutrons)      │
        └─────────────────────────────────────────┘
                                                    Z (protons)

Key stability rules:
  • Even Z, even N → most stable (even-even nuclides)
  • Magic numbers: Z or N = 2, 8, 20, 28, 50, 82, 126 → extra stability (closed nuclear shells)
  • Tin (Z=50) has the most stable isotopes: 10
  • No stable isotopes: Tc (Z=43), Pm (Z=61), and all Z > 83

Decay modes:
  α decay:   heavy nuclei, loses ²He → daughter is Z−2, A−4
  β⁻ decay:  neutron → proton + e⁻ + antineutrino → daughter is Z+1
  β⁺/EC:     proton → neutron, daughter is Z−1
  γ emission: nuclear energy state transition, no Z/A change
  fission:    heavy nuclei split (U-235, Pu-239)
```

---

## Full Element Index by Series

```
┌────────────────────────────────────────────────────────────────────────────┐
│  MODULE          ELEMENTS COVERED                       GROUP(S)           │
├────────────────────────────────────────────────────────────────────────────┤
│  01-HYDROGEN     H (1)                                  1 (special)        │
│  02-NOBLE-GASES  He Ne Ar Kr Xe Rn Og (2,10,18,36,54,  18                 │
│                  86,118)                                                    │
│  03-ALKALI       Li Na K Rb Cs Fr (3,11,19,37,55,87)   1                  │
│  04-ALK-EARTH    Be Mg Ca Sr Ba Ra (4,12,20,38,56,88)  2                  │
│  05-HALOGENS     F Cl Br I At Ts (9,17,35,53,85,117)   17                 │
│  06-LIFE-NONMET  C N O P S (6,7,8,15,16)               14,15,16           │
│  07-P-BLOCK      B Al Si Ge As Sb Se Te Po Sn Pb Bi    13-16 (remaining)  │
│                  (5,13,14,32,33,51,34,52,84,50,82,83)                      │
│  08-TRANS-3D     Sc Ti V Cr Mn Fe Co Ni Cu Zn          3-12 (Period 4)    │
│                  (21-30)                                                    │
│  09-TRANS-4D5D   Y-Cd (39-48) + Hf-Hg (72-80)         3-12 (Per 5+6)     │
│  10-LANTHANIDES  La-Lu (57-71)                         f-block            │
│  11-ACTINIDES    Ac-Lr (89-103)                        f-block            │
└────────────────────────────────────────────────────────────────────────────┘

Remaining elements not explicitly covered above:
  Sc (21) — covered in 08-TRANS-3D
  Ga (31), In (49), Tl (81) — in 07-P-BLOCK context (Group 13 below Al)
  Elements 104-118 (Rf-Og) — superheavy, covered in 09/11 context
```

---

## Periodic Trends Cheat Sheet

| Property | Across period (→) | Down group (↓) | Key exception |
|----------|------------------|----------------|---------------|
| Atomic radius | Decreases | Increases | N > O (Hund half-fill) |
| Ionization energy | Increases | Decreases | B < Be; O < N |
| Electron affinity | More negative (more favorable) | Less negative | N, P (half-fill) |
| Electronegativity | Increases | Decreases | F is maximum |
| Metallic character | Decreases | Increases | — |
| Oxidation state max | = group number | Same | F only −1 |
| d-orbital effect | N/A in s/p | d-block anomalies | Lanthanide contraction |

---

## Common Confusion Points

**"Why is the periodic table split into two parts (main table + f-block below)?"**
Pure pragmatics — the f-block has 14 columns and inserting it between Groups 2 and 3 would
make the table ~32 elements wide. The detached format is a printing compromise, not a
statement about chemistry.

**"Why does period 4 have 18 elements but period 2 has only 8?"**
Period 2 fills 2s + 2p = 8 electrons.
Period 4 fills 4s + 3d + 4p = 2 + 10 + 6 = 18 electrons.
The d-block enters at Period 4 (3d) and f-block enters at Period 6 (4f).

**"Hydrogen: Group 1 or Group 17?"**
Neither uniquely. H is placed in Group 1 by convention because it has 1 valence electron.
But its chemistry spans both: it forms H⁺ (like Group 1) and H⁻ (like Group 17), and H₂
behaves like a diatomic nonmetal (like F₂, Cl₂). Some tables place it above both groups or
alone. See 01-HYDROGEN.md.

**"What makes something a 'transition metal'?"**
IUPAC: an element with an incomplete d subshell in one of its common oxidation states.
Zinc (Zn), Cadmium (Cd), Mercury (Hg) are sometimes excluded because their ground state
and ions have full d¹⁰ configurations. The debate is real but mostly definitional.

**"Lanthanide vs rare earth vs REE?"**
Rare earth elements (REE) = lanthanides + Sc + Y (17 elements total).
Despite the name, most are not particularly rare in the crust — they're just hard to
separate because of nearly identical chemistry. China dominates supply (~85%).

**"Why do actinides have more variable chemistry than lanthanides?"**
The 5f orbitals are more spatially extended than 4f — they participate more in bonding.
Lanthanides are almost always +3; actinides range from +2 to +7 (uranium reaches +6 as UO₂²⁺).
