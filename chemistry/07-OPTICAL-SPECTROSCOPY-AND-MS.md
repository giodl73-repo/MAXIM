---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:optical-spectroscopy-and-ms
kind: guide
module: chemistry
section: chemistry
title: Optical Spectroscopy and Mass Spectrometry for Identification
status: source-custody
source_custody: partial
current_path: chemistry/07-OPTICAL-SPECTROSCOPY-AND-MS.md
canonical_path: chemistry/07-OPTICAL-SPECTROSCOPY-AND-MS.md
backsource_ids: [proof-backfill:chemistry:07-optical-spectroscopy-and-ms, git-history:chemistry:07-optical-spectroscopy-and-ms]
concepts: [infrared, uv-vis, photochemistry, mass-spectrometry, structure-elucidation]
root_concepts: [molecular-spectroscopy]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Optical Spectroscopy and Mass Spectrometry for Identification

**This guide owns** the *interpretation* layer: reading IR for functional groups,
UV-Vis/fluorescence for chromophores, photochemical reaction types, and — the big
library-wide gap — **mass-spectral fragmentation** for structure and formula. **It
defers the physics** (Beer-Lambert law, IR vs Raman selection rules, the Jablonski
diagram, spectrometer optics) to `optics/07`; this guide does not re-derive them. It
fuses with `06` (NMR) into a combined structure-elucidation workflow.

```
THREE PROBES, THREE ANSWERS, ONE STRUCTURE
==========================================================================
  IR (vibrations)      UV-Vis / fluor.      MASS SPECTROMETRY
  "what groups?"       "what chromophore?"  "what formula + skeleton?"
        |                     |                     |
  C=O 1715 -> ketone    conjugation ->        M+ = formula (exact mass)
  broad OH -> alcohol   lambda_max shift      isotopes -> Cl/Br/S
  C=O 1740, no OH ->    fluorescence ->       fragments -> connectivity
     ester              quantum yield
        |                     |                     |
        v                     v                     v
             COMBINED ELUCIDATION (with NMR from 06):
             MS formula -> IR groups -> NMR connectivity -> XRD (08)
==========================================================================
```

---

## Infrared: Functional-Group Fingerprints

IR absorption frequency ≈ a bond's mechanical resonance (`optics/07` derives it from
the harmonic oscillator). For *identification*, memorize the diagnostic region
(4000–1500 cm⁻¹); the fingerprint region below 1500 cm⁻¹ is for library matching,
not by-eye assignment.

| Group | ν (cm⁻¹) | Shape / note |
|---|---|---|
| O–H (alcohol) | 3200–3550 | broad (H-bonded) |
| O–H (carboxylic acid) | 2500–3300 | very broad, on top of C–H |
| N–H | 3300–3500 | 1 band (2° amine), 2 bands (1° amine) |
| C–H | 2850–3100 | sp³ below 3000, sp²/sp above |
| C≡N / C≡C | 2100–2260 | sharp, weak |
| **C=O** | **1650–1800** | strong; exact value assigns the carbonyl |
| C=C (alkene) / aromatic | 1600–1680 / ~1600, 1475 | |

The carbonyl position is the most information-dense number in IR:

```
   CARBONYL ANATOMY (cm^-1)
   anhydride ~1760 & 1810 (two bands) | ester ~1735-1750 | aldehyde ~1725
   ketone ~1715 | carboxylic acid ~1710 (+ broad OH) | amide ~1650 (lowest)
   conjugation and ring strain SHIFT these: conjugation lowers, small rings raise.
```

So a strong band at **1740 cm⁻¹ with no O–H stretch** rules out a carboxylic acid
and points to an **ester** (or, at 1715–1725, a ketone/aldehyde); the presence or
absence of the broad acid O–H is the discriminator. This is exactly the kind of
either/or IR answers this guide is for.

---

## UV-Vis, Fluorescence, Photochemistry

**UV-Vis** probes electronic transitions of chromophores: π→π* (intense, ε ~10⁴) and
n→π* (weak, ε ~10–100). Extending **conjugation raises λ_max** (bathochromic/red
shift) and ε — the basis of dye color and of tracking conjugated-system growth in a
synthesis. Woodward-Fieser rules estimate λ_max additively for dienes/enones.
Beer-Lambert quantitation (A = εbc) is `optics/07`; here UV-Vis is a *diagnostic* for
"is there a conjugated/aromatic system, and did the reaction change it?"

**Fluorescence** (emission after excitation) is far more sensitive and selective than
absorption; the **Stokes shift** (emission at longer λ than absorption) and quantum
yield Φ are the working parameters (physics in `optics/07`). It underlies trace
assays, molecular sensors, and the fluorophore tags used across `05` and biology.

**Photochemistry** — reactions driven by an excited state, obeying different rules
than ground-state chemistry (recall the photochemical flips in the Woodward-Hoffmann
table, `03`). The named carbonyl photoreactions:

```
   NORRISH TYPE I : alpha-cleavage of the C-C bond next to C=O -> two radicals
   NORRISH TYPE II: gamma-H abstraction -> 1,4-biradical -> cleaves to
                    an alkene + an enol (a fragmentation, not a cleavage at C=O)
   [2+2] photocycloaddition: thermally forbidden, PHOTOchemically allowed (03)
```

The **quantum yield** Φ = (events)/(photons absorbed) measures photochemical
efficiency and can exceed 1 for chain processes; it is the key metric for
photocatalysis and photoinitiators.

---

## Mass Spectrometry: Formula and Skeleton

MS measures mass-to-charge (m/z) of ions produced from the analyte. **Ionization**
sets how much fragmentation you get:

| Source | Hardness | Gives | Best for |
|---|---|---|---|
| EI (electron ionization) | hard | M⁺• + rich fragments | small volatiles; library search (GC-MS) |
| ESI (electrospray) | soft | [M+H]⁺/[M−H]⁻, multiply charged | polar, large, LC-MS; proteins |
| APCI | soft | [M+H]⁺ | mid-polarity LC-MS |
| MALDI | soft | [M+H]⁺, singly charged | polymers, biomolecules |

### Reading the molecular-ion region

- **Nitrogen rule:** an odd nominal M⁺ means an **odd number of nitrogens** (for
  CHNOPS-type molecules). Even M with no N is the common case.
- **Isotope pattern** reveals heteroatoms from the M+2 intensity:

```
   M+2 ~ 33% of M   -> ONE chlorine   (35Cl:37Cl = 100:32)
   M+2 ~ 98% of M   -> ONE bromine    (79Br:81Br = 100:98)  (M, M+2 near-equal)
   M+2 ~ 4.4% of M  -> ONE sulfur      ; M+1 ~ 1.1% per carbon (count C from 13C)
```

- **Exact mass (HRMS)** resolves the molecular *formula*. Nominal-mass degeneracy is
  broken by high resolution: at nominal 60, **C₃H₈O = 60.0575** vs **C₂H₄O₂ =
  60.0211** — a 0.036-Da gap a high-res instrument measures easily. Match the measured
  exact mass to a candidate formula, then check **degrees of unsaturation**
  (rings + π bonds) = (2C + 2 + N − H − X)/2.

### Fragmentation logic

Fragments map the skeleton. The mechanisms worth knowing on sight:

| Fragmentation | Where | Diagnostic |
|---|---|---|
| **α-cleavage** | next to C=O, N, O, halogen | acylium R–C≡O⁺; forms at the heteroatom's neighbor |
| **McLafferty rearrangement** | carbonyl with a γ-H | 6-membered TS; loses a neutral alkene → even-mass enol cation |
| benzylic / allylic | next to ring/double bond | stabilized cation (tropylium m/z 91 from toluene) |
| retro-Diels-Alder | cyclohexenes | reverses the [4+2] |
| common neutral losses | anywhere | 15 (CH₃), 18 (H₂O), 28 (CO), 31 (OCH₃), 45 (COOH) |

**Worked McLafferty — 2-hexanone (CH₃COCH₂CH₂CH₂CH₃, M = 100):** a γ-hydrogen (on the
chain three carbons from the carbonyl) transfers to the carbonyl oxygen through a
six-membered transition state; the β C–C bond breaks, expelling neutral propene
(C₃H₆, 42) and leaving the **enol radical cation of acetone at m/z 58**. Separately,
**α-cleavage** gives the acetyl cation CH₃C≡O⁺ at **m/z 43** (and loss of CH₃ →
m/z 85). Seeing 58 + 43 together is the signature of a methyl ketone with a
McLafferty-capable chain.

---

## Combined Structure Elucidation

No single technique solves a real unknown; they are orthogonal tests that must all
agree — the analytical version of unit + integration + regression tests.

```
   1. HRMS      -> molecular FORMULA + degrees of unsaturation + halogen/S from isotopes
   2. IR        -> which FUNCTIONAL GROUPS are present/absent (C=O type, OH, NH, CN)
   3. 1D NMR    -> H and C inventory (06): counts and environments
   4. 2D NMR    -> CONNECTIVITY graph (COSY/HSQC/HMBC) (06)
   5. MS frags  -> corroborate the skeleton (alpha-cleavage, McLafferty, losses)
   6. UV-Vis    -> confirm conjugation/aromaticity
   7. XRD (08)  -> definitive 3D structure + absolute config when a crystal grows
   CONVERGENCE: every technique must be consistent, or the structure is wrong.
```

The discipline is *falsification*: propose a structure from the formula and NMR, then
require it to predict the observed IR bands and MS fragments. A structure that
"explains" the NMR but not the McLafferty ion is not yet proven.

---

## Reader Tasks

1. **IR: strong C=O at 1740, no O–H — what is it?** Not a carboxylic acid (no broad
   OH); the 1740 value fits an **ester** (a ketone/aldehyde would sit ~1715–1725).
   Confirm with the C–O stretches and NMR.
2. **EI: M⁺ with M+2 ≈ 1/3 intensity — what does that mean, and how do you get the
   formula?** M+2 ≈ 33% signals **one chlorine**; take the exact mass of M⁺ to HRMS,
   match a Cl-containing formula, and check degrees of unsaturation. (M+2 ≈ M would
   instead mean one Br.)
3. **Explain the m/z 58 peak in 2-hexanone's EI spectrum.** **McLafferty
   rearrangement**: γ-H transfer through a 6-membered TS ejects propene (42) → enol
   cation of acetone at m/z 58; the m/z 43 acylium is the α-cleavage companion.
4. **Distinguish C₃H₈O from C₂H₄O₂ (both nominal 60).** HRMS: exact masses 60.0575 vs
   60.0211 differ by 0.036 Da — trivially resolved at high resolution, assigning the
   formula.
5. **Did conjugation increase during a reaction?** A bathochromic (red) shift of
   λ_max with higher ε in UV-Vis indicates extended conjugation; combine with the IR
   C=O shift (conjugation lowers it) to confirm.

## Decision Cheat Sheet

| Need | Technique | Key readout |
|---|---|---|
| Functional groups present | IR | O–H/N–H/C=O region (4000–1500) |
| Which carbonyl? | IR C=O position | ester 1740 / ketone 1715 / amide 1650 |
| Conjugation / aromaticity | UV-Vis | λ_max, ε; red shift = more conjugation |
| Trace / sensitive detection | fluorescence | Stokes shift, Φ |
| Molecular formula | HRMS (exact mass) | match Da + degrees of unsaturation |
| Cl / Br / S present? | MS isotope pattern | M+2 = 33% (Cl), ≈100% (Br), 4.4% (S) |
| Skeleton / connectivity | EI fragments | α-cleavage, McLafferty, neutral losses |
| Polar/large analyte MW | ESI/MALDI (soft) | [M+H]⁺, multiply charged |
| Full structure | fuse MS+IR+NMR(+XRD) | all must agree |

## Common Confusion Points

- **IR C=O value carries the information, not just its presence.** 1650 vs 1715 vs
  1740 vs 1810/1760 distinguishes amide/ketone/ester/anhydride. Read the number.
- **Beer-Lambert and selection rules are `optics/07`.** This guide interprets spectra
  for structure; it does not re-derive the light-matter physics.
- **Hard vs soft ionization changes the spectrum's meaning.** EI gives M⁺• and
  fragments (structure); ESI gives protonated/deprotonated (and multiply charged)
  ions — don't read an ESI m/z as the neutral mass.
- **The nitrogen rule is about *nominal* mass.** Odd nominal M ⇒ odd N. It fails if you
  apply it to exact masses or forget the charge/adduct.
- **McLafferty needs a γ-hydrogen.** No γ-H, no rearrangement peak; its presence is
  structural evidence, its absence is too.
- **M+2 ≈ 100% is bromine, not "two chlorines."** Two Cl gives M+2 ≈ 65% and a
  distinct M+4; one Br gives near-equal M/M+2. Read the whole isotope envelope.
