---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-ACID-BASE-SOLUTION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:acid-base-solution
kind: guide
module: chemistry
section: chemistry
title: Acid-Base Theory and Solution Equilibria
status: source-custody
source_custody: partial
current_path: chemistry/02-ACID-BASE-SOLUTION.md
canonical_path: chemistry/02-ACID-BASE-SOLUTION.md
backsource_ids: [mdloom-backfill:chemistry:02-acid-base-solution, git-history:chemistry:02-acid-base-solution]
concepts: [acid-base, hsab, buffers, solubility, complexation]
root_concepts: [solution-equilibria]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Acid-Base Theory and Solution Equilibria

**This guide owns** the three acid-base models (Brønsted, Lewis, HSAB), polyprotic
and buffer equilibria with capacity, solubility (Ksp) and selective precipitation,
and complexation (formation constants, EDTA conditional constants). **It builds on**
`natural-sciences/03` (ΔG, K, Le Chatelier) — which it will not re-derive — and
feeds `04-ANALYTICAL-QUANTITATIVE` (titrimetry is applied solution equilibria).
The shift from gen chem: stop memorizing "strong vs weak" and start *predicting*
which equilibrium dominates and how buffered the system is.

```
THREE LENSES ON ACID-BASE, ONE SOLUTION
==========================================================================
  BRONSTED-LOWRY        LEWIS                 HSAB (Pearson)
  proton transfer       electron-pair         hard/soft matching
  HA + B <=> A- + HB+   A + :B -> A-B         "like binds like"
        |                     |                     |
        v                     v                     v
              EVERYTHING THAT HAPPENS IN SOLUTION

  [ pH / buffers ]   [ solubility ]    [ complexation ]   [ precipitation ]
   Ka, Kb, Kw         Ksp, common       Kf, beta_n,        selective /
   H-H eqn, beta      ion effect        EDTA K'f           fractional

  MASTER VARIABLE: pH sets the speciation of every weak acid/base,
  which sets solubility, which sets what precipitates, which sets
  what a titration or an ISE actually measures.
==========================================================================
```

---

## The Three Models

**Brønsted-Lowry** — proton donor/acceptor; every acid has a conjugate base.
The bookkeeping identity is **K_a · K_b = K_w = 1.0×10⁻¹⁴** (25 °C), so a strong
acid necessarily has a negligibly weak conjugate base. In water the strongest acid
that can exist is H₃O⁺ and the strongest base is OH⁻ — the **leveling effect**.
To distinguish acids stronger than H₃O⁺ you must move to a less basic solvent
(differentiating solvent), e.g., acetic acid or liquid SO₂.

**Lewis** — electron-pair acceptor (acid) / donor (base). This subsumes
Brønsted (H⁺ is one Lewis acid) and covers everything with no proton: BF₃ + NH₃,
metal-ligand bonds (`01`), and most catalysis. Every coordination bond is a
Lewis acid-base adduct.

**HSAB (Pearson hard-soft acid-base)** — ranks *which* Lewis pairs are stable.
**Hard** = small, high charge density, low polarizability. **Soft** = large,
polarizable, often low oxidation state. The rule: **hard acids bind hard bases;
soft acids bind soft bases.**

| | Hard | Borderline | Soft |
|---|---|---|---|
| Acids | H⁺, Li⁺, Na⁺, Mg²⁺, Al³⁺, Fe³⁺, Ti⁴⁺, BF₃ | Fe²⁺, Ni²⁺, Cu²⁺, Zn²⁺, Pb²⁺, SO₂ | Cu⁺, Ag⁺, Au⁺, Hg²⁺, Pd²⁺, Pt²⁺, BH₃ |
| Bases | F⁻, OH⁻, O donors (H₂O, ROH, RCOO⁻), NH₃, NO₃⁻ | Br⁻, N₃⁻, pyridine, SO₃²⁻ | I⁻, S donors (RSH, S²⁻), CN⁻, CO, R₃P, alkenes |

HSAB explains, at a glance: why **Hg²⁺ and Cd²⁺ poison enzymes at thiol (–SH)
sites** (soft-soft) rather than at O/N sites; why AgI is far less soluble than AgF;
why hard Fe³⁺ prefers O-donor chelators (siderophores, EDTA) while soft Pt²⁺
prefers S/N; and why Class-A (hard) vs Class-B (soft) metals sort the whole
periodic table of aqueous cations.

---

## Weak-Acid Equilibria, Buffers, and Capacity

For a weak acid, the working equation is **Henderson-Hasselbalch**:

```
   pH = pKa + log([A-]/[HA])         valid when both species are >~ 10% present
                                     (not at the extremes, where you solve the
                                      full Ka expression or account for water)
```

A **buffer** resists pH change; its **capacity β** quantifies how much:

```
   β = dC_base/dpH  ~=  2.303 * C_total * ( Ka[H+] / (Ka + [H+])^2 )

   MAX at pH = pKa   ->   beta_max = 2.303 * C_total / 4  =  0.576 * C_total
   USEFUL RANGE:   pKa +/- 1   (ratio 10:1 to 1:10)
```

Two design levers, independent: **pKa** picks the *center* of the buffering
window (choose a buffer whose pKa is within ~1 unit of your target pH), and
**total concentration** sets the *depth* (β scales linearly with C_total). To
design a HEPES buffer at pH 7.5: HEPES pKa ≈ 7.55, so you need nearly 1:1
acid:base — mix the free acid and its sodium salt in roughly equal amounts, then
adjust to pH 7.5; concentration (e.g., 25–50 mM) sets capacity, and any added
inert salt sets ionic strength (which shifts the *apparent* pKa — see `09` on
activity).

### Polyprotic systems

Phosphoric acid is the canonical triprotic: **pKa1 = 2.15, pKa2 = 7.20,
pKa3 = 12.35**. An **amphoteric** intermediate (H₂PO₄⁻, HPO₄²⁻) is both acid and
base; the pH where it dominates — the equivalence point between two dissociations
— is the average of the flanking pKa's:

```
   H3PO4  --(pKa1=2.15)-->  H2PO4-  --(pKa2=7.20)-->  HPO4^2-  --(pKa3=12.35)--> PO4^3-
                    |                        |                         |
   1st eq pt ~ (2.15+7.20)/2 = 4.68   2nd eq pt ~ (7.20+12.35)/2 = 9.78
```

The same math gives an amino acid's **isoelectric point** pI = ½(pKa1 + pKa2) for
a simple diprotic amino acid, the pH of zero net charge used in electrophoresis and
protein purification (`05`).

---

## Solubility and Selective Precipitation

For a sparingly soluble salt M_aX_b: **Ksp = [Mⁿ⁺]ᵃ[Xᵐ⁻]ᵇ**. Two levers move it:

- **Common-ion effect** — adding a shared ion suppresses solubility (Le Chatelier).
  A solution 0.02 M in SO₄²⁻ holds only [Ca²⁺] = Ksp/[SO₄²⁻] = 4.9×10⁻⁵ / 0.02 ≈
  **2.5×10⁻³ M** before CaSO₄ precipitates.
- **pH** — anions of weak acids (S²⁻, OH⁻, CO₃²⁻, F⁻) protonate as pH drops,
  raising solubility. This makes **selective sulfide precipitation** possible:
  controlling [H⁺] tunes [S²⁻] over many orders of magnitude, so metals precipitate
  in Ksp order — the basis of classical qualitative-analysis cation groups.

**Fractional precipitation:** when two cations share a precipitant, the one with
the smaller Ksp drops first; separation is clean if the Ksp values differ enough
that the first is >99.9% removed before the second begins. Quantify with the ratio
of ion concentrations at the onset of the second precipitate.

---

## Complexation and the EDTA Conditional Constant

Metal + ligand equilibria use **stepwise** constants K₁, K₂, … and **overall**
constants βₙ = K₁K₂…Kₙ. For the analytical workhorse **EDTA** (hexadentate,
1:1 with essentially every metal), the catch is that only the fully deprotonated
**Y⁴⁻** form chelates, and its fraction α_{Y⁴⁻} is strongly pH-dependent. Hence the
**conditional (effective) formation constant**:

```
   K'f = alpha_Y4- * Kf        alpha_Y4- = fraction of total EDTA present as Y4-

   pH      2       4       6       8      10      12
   alpha  4e-14   4e-9    2e-5    5e-3    0.35    0.98
```

Because α collapses at low pH, a metal with a modest Kf can only be titrated with
EDTA in a **buffered** window: Ca²⁺ (log Kf = 10.7) needs pH ≈ 10 (ammonia buffer);
Fe³⁺ (log Kf = 25.1) is so strong it titrates even at pH 2, which is exactly how you
titrate Fe³⁺ *selectively* in the presence of Ca²⁺/Mg²⁺. This single idea — tune pH
to switch a chelation on or off — underlies water-hardness titrations, masking
agents, and metal separations.

```
SPECIATION LOGIC (the through-line of this guide)
   set pH  ->  fixes alpha of every weak acid/base and of Y4-
           ->  fixes free [M(n+)] and [ligand]
           ->  fixes what dissolves, what precipitates, what a titration sees
```

---

## Superacids (the far end of the scale)

Beyond 100% H₂SO₄, acidity is measured by the **Hammett acidity function H₀**
(more negative = stronger). **Superacids** are stronger than pure H₂SO₄
(H₀ = −12). **Magic acid** (HSO₃F·SbF₅) reaches H₀ ≈ −20 to −24; **fluoroantimonic
acid** (HF·SbF₅) reaches **H₀ ≈ −28**, ~10¹⁶× stronger than concentrated H₂SO₄.
They are strong enough to protonate alkanes and generate persistent carbocations
(Olah's Nobel work) — the reason they matter for mechanism (`03`) and petroleum
cracking. The conjugate bases (SbF₆⁻, and weakly-coordinating anions generally) are
so non-nucleophilic that otherwise-impossible cations become bench-stable.

---

## Reader Tasks

1. **Why does Hg²⁺ bind cysteine –SH rather than water?** HSAB: Hg²⁺ is a soft acid,
   sulfur is a soft base → strong soft-soft affinity; hard O of water is a poor
   match. This is the molecular basis of heavy-metal enzyme toxicity.
2. **pH at the second equivalence point of an H₃PO₄ titration?** ≈ ½(pKa2 + pKa3) =
   ½(7.20 + 12.35) = **9.78**, the amphoteric HPO₄²⁻ point.
3. **What [Ca²⁺] coexists with 0.02 M SO₄²⁻?** [Ca²⁺] = Ksp/[SO₄²⁻] ≈
   4.9×10⁻⁵/0.02 ≈ **2.5×10⁻³ M** before CaSO₄ precipitates (common-ion effect).
4. **Design a pH 7.5 buffer with real capacity.** Pick a buffer with pKa ≈ 7.5
   (HEPES, pKa 7.55) at ~1:1 acid:base; set total concentration for the capacity you
   need (β_max ≈ 0.58·C_total); note ionic strength shifts apparent pKa.
5. **Can you titrate Fe³⁺ with EDTA in the presence of Ca²⁺?** Yes — at pH ≈ 2,
   α_{Y⁴⁻} is tiny so K'f for Ca (log Kf 10.7) is too small to react, but Fe³⁺
   (log Kf 25.1) still has an adequate conditional constant. pH masks the calcium.

## Decision Cheat Sheet

| Goal | Use | Key relation |
|---|---|---|
| Predict which Lewis pair is stable | HSAB | hard–hard, soft–soft |
| Find buffer pH | Henderson-Hasselbalch | pH = pKa + log([A⁻]/[HA]) |
| Choose a buffer | pKa within ±1 of target pH | max β at pH = pKa |
| Get buffer strength | scale C_total | β_max ≈ 0.58·C_total |
| Solubility with shared ion | common-ion Ksp | [M] = Ksp/[X] |
| Separate two cations | fractional precipitation | smaller Ksp drops first |
| Titrate a metal with EDTA | conditional constant | K'f = α_{Y⁴⁻}·Kf; pick pH |
| Protonate an alkane | superacid | H₀ ≤ −20 |

## Common Confusion Points

- **K_a·K_b = K_w only for a conjugate *pair*.** Don't multiply a random acid's Ka
  by an unrelated base's Kb.
- **Henderson-Hasselbalch fails at the extremes.** Near pure HA or pure A⁻, or in
  very dilute solution, use the full equilibrium (and include water autoionization).
- **Buffer capacity is not the same as buffer range.** Range is set by pKa (±1);
  depth is set by concentration. A dilute buffer at exactly its pKa still has poor
  absolute capacity.
- **Ksp is not "solubility."** Molar solubility is derived from Ksp *and* the
  stoichiometry *and* the common-ion/pH conditions; comparing Ksp values across
  different stoichiometries directly is a classic error.
- **EDTA "log K = 16" is the ideal Kf, not what you get.** The *conditional* K'f at
  your working pH — often orders of magnitude smaller — governs whether the titration
  is sharp.
- **"Strong acid" is solvent-relative.** In water everything above H₃O⁺ is leveled;
  ranking HCl vs HBr vs HClO₄ requires a differentiating solvent.
