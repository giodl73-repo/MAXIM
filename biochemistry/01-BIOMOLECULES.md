---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:biomolecules
kind: guide
module: biochemistry
section: biochemistry
title: Biomolecules
status: source-custody
source_custody: partial
current_path: biochemistry/01-BIOMOLECULES.md
canonical_path: biochemistry/01-BIOMOLECULES.md
backsource_ids: [proof-backfill:biochemistry:01-biomolecules, git-history:biochemistry:01-biomolecules]
concepts: [water, pH, carbohydrates, lipids, proteins, nucleic acids, amino acids]
root_concepts: [biomolecules]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Biomolecules — The Four Building Blocks + Water

```
+------------------------------------------------------------------------+
|                  THE MOLECULAR PARTS LIST OF LIFE                      |
|                                                                        |
|   SOLVENT (the substrate everything runs in)                           |
|   .------------------------------------------------------------.       |
|   |  WATER  — polar, H-bonding, sets pH, drives folding        |       |
|   '------------------------------------------------------------'       |
|                                                                        |
|   FOUR MACROMOLECULE CLASSES (monomer -> polymer)                      |
|   .-------------. .-------------. .-------------. .-------------.      |
|   | CARBOHYDRATE| |   LIPID     | |  PROTEIN    | | NUCLEIC ACID|      |
|   | monomer:    | | monomer:    | | monomer:    | | monomer:    |      |
|   | monosacch.  | | fatty acid  | | amino acid  | | nucleotide  |      |
|   | polymer:    | | + glycerol  | | polymer:    | | polymer:    |      |
|   | glycogen,   | | (not a true | | polypeptide | | DNA / RNA   |      |
|   | starch,     | |  polymer)   | |             | |             |      |
|   | cellulose   | |             | |             | |             |      |
|   | ROLE: fuel +| | ROLE:       | | ROLE: do    | | ROLE: store |      |
|   | structure   | | membranes + | | everything  | | + transmit  |      |
|   |             | | energy store| | (catalysis) | | information |      |
|   '-------------' '-------------' '-------------' '-------------'      |
|                                                                        |
|   BUILT BY:  condensation (lose H2O)   BROKEN BY: hydrolysis (add H2O) |
+------------------------------------------------------------------------+
```

Four polymer families, one solvent. Carbohydrates and lipids are mostly **energy
and structure**, proteins are the **machines**, nucleic acids are the
**information store**. Polymers are assembled by **condensation** (a bond forms,
a water leaves) and disassembled by **hydrolysis** (water is added, the bond
breaks). That single bidirectional rule covers digestion, synthesis, and turnover.

---

## Water and pH — The Substrate Layer

Water is not a passive background; it is an active component of every reaction. A
software analogy: water is the **runtime environment** — its properties determine
what runs and how.

```
+------------------------------------------------------------------------+
|   WATER IS POLAR                                                       |
|                                                                        |
|        H   (+)                                                         |
|         \                                                              |
|          O (-)   <- oxygen hogs electrons => partial charges           |
|         /                                                              |
|        H   (+)                                                         |
|                                                                        |
|   CONSEQUENCES:                                                        |
|   - Hydrogen bonds form between molecules (cohesion, high boiling pt)  |
|   - Dissolves ions and polar molecules ("hydrophilic")                 |
|   - EXCLUDES nonpolar molecules ("hydrophobic effect")                 |
|     -> this exclusion is what folds proteins and forms membranes       |
+------------------------------------------------------------------------+
```

The **hydrophobic effect** is the single most important consequence: water's
drive to maximize its own hydrogen bonding pushes oily molecules together to get
them out of the way. This is not an attraction between the oily molecules — it is
water organizing itself. That entropic shove is what folds a protein's greasy core
inward and what spontaneously assembles a lipid bilayer.

### pH: the proton concentration knob

```
  pH = -log10[H+]          (concentration of hydrogen ions)

  pH 0 ------------- 7 ------------- 14
   acidic         neutral         basic
   high [H+]    [H+]=[OH-]      low [H+]

  Each pH unit = 10x change in [H+]   (it's a log scale, like decibels)

  Blood is held at pH 7.35-7.45 — a tighter tolerance than most
  build pipelines allow for any single metric.
```

pH matters because proton concentration changes the **charge** on molecules, and
charge changes shape and reactivity. An enzyme's active site has acidic and basic
groups whose protonation state — and therefore whether they can catalyze — depends
on pH. Move pH a couple of units and the machine stops working.

**Buffers** resist pH change. A buffer is a weak acid plus its conjugate base
(e.g., H2CO3 / HCO3- — the bicarbonate system that keeps blood near 7.4). When
acid is added, the base mops up protons; when base is added, the acid releases
them. This is **negative feedback applied to a single scalar** — a PID controller
holding a setpoint. The **Henderson-Hasselbalch equation** quantifies it:
pH = pKa + log([A-]/[HA]). Buffering capacity is maximal when pH = pKa
(equal acid and base forms).

### pKa — the bridge to titration

Every ionizable group has a **pKa**: the pH at which it is half-protonated. Below
pKa it holds its proton; above pKa it gives it up. You will see pKa again for
amino acid side chains (file 02) — the charge on a protein at a given pH is just
the sum over all its groups' protonation states.

---

## Carbohydrates — Fuel and Scaffolding

```
+------------------------------------------------------------------------+
|   MONOSACCHARIDE   ->   DISACCHARIDE   ->   POLYSACCHARIDE             |
|   (single sugar)        (two, joined)       (many, joined)             |
|                                                                        |
|   glucose C6H12O6       sucrose             starch  (plant fuel store) |
|   fructose              (glucose+fructose) glycogen(animal fuel store) |
|   galactose             lactose            cellulose (plant structure) |
|                         (glucose+galactose)                            |
|                         maltose                                        |
|                                                                        |
|   Joined by GLYCOSIDIC bonds (condensation; lose one H2O per bond)     |
+------------------------------------------------------------------------+
```

**Glucose (C6H12O6)** is the universal currency sugar — the molecule glycolysis
starts from. Sugars beyond a handful of carbons are stored as polymers.

The fascinating bit is that **starch, glycogen, and cellulose are all polymers of
the same glucose monomer** — they differ only in the bond geometry:

| Polymer | Linkage | Branching | Function | Digestible by humans? |
|---|---|---|---|---|
| **Starch** (amylose) | α-1,4 | little | plant energy store | yes |
| **Glycogen** | α-1,4 + α-1,6 | heavy | animal energy store | yes |
| **Cellulose** | β-1,4 | none | plant cell wall | no |

The α vs β distinction is a single stereochemical flip at one carbon, yet humans
have α-glucosidases but no β-glucosidase — so we can eat potatoes (starch) but not
wood (cellulose), even though both are "just glucose." This is the biochemical
version of two files with identical bytes but incompatible encodings: the
**enzyme is the decoder**, and we only ship the α decoder.

Glycogen's **heavy branching** is a deliberate engineering choice: branches create
many free ends, and enzymes only add/remove glucose at ends, so branching lets the
cell deposit or mobilize glucose fast — like sharding a queue for parallel access.

---

## Lipids — Membranes and Dense Energy

Lipids are defined by behavior, not structure: they are **hydrophobic** (water-
insoluble). That single property gives them two jobs — energy storage and barriers.

```
+--------------------------------------------------------------------------+
|   FATTY ACID:   COOH--CH2-CH2-...-CH3  (carboxyl head, hydrocarbon tail) |
|                  hydrophilic            hydrophobic                      |
|                                                                          |
|   SATURATED   : all C-C single bonds -> straight -> packs tight -> solid |
|                 (butter, lard)                                           |
|   UNSATURATED : has C=C double bond -> kinked -> packs loose -> liquid   |
|                 (olive oil; the kink is why oils stay liquid)            |
|                                                                          |
|   TRIGLYCERIDE: glycerol + 3 fatty acids  = the body's fat depot         |
|                 ~9 kcal/g vs ~4 kcal/g for carbs/protein (2x density)    |
+--------------------------------------------------------------------------+
```

### The phospholipid and the membrane

A **phospholipid** swaps one fatty acid for a charged phosphate head, making it
**amphipathic** — one end loves water, the other hates it. In water, these
self-assemble into a **bilayer**: tails inward (hiding from water), heads outward.

```
   WATER (outside)
   O O O O O O O O O O O O    <- hydrophilic phosphate heads
   | | | | | | | | | | | |
   | | | | tails | | | | |    <- hydrophobic interior (the barrier)
   | | | | | | | | | | | |
   O O O O O O O O O O O O    <- hydrophilic heads
   WATER (inside)
```

The membrane is a **self-healing, self-assembling barrier** driven entirely by the
hydrophobic effect — no template, no enzyme required. It is the original
"infrastructure as data": the structure emerges from the molecules' properties.
Membrane detail (transport, channels) lives in `biology/`; here we just note that
the same hydrophobic logic builds both fat droplets and cell boundaries.

| Lipid type | Structure | Role |
|---|---|---|
| **Triglyceride** | glycerol + 3 fatty acids | energy storage (fat) |
| **Phospholipid** | glycerol + 2 FA + phosphate | membranes |
| **Sterol** (cholesterol) | fused-ring scaffold | membrane fluidity, hormone precursor |
| **Eicosanoid** | 20-carbon FA derivative | local signaling (e.g., prostaglandins) |

---

## Proteins — A First Look (Full Detail in File 02)

Proteins are polymers of **amino acids**. There are **20 standard amino acids**,
all sharing one backbone and differing only in the **side chain (R group)**.

```
+------------------------------------------------------------------------+
|   AMINO ACID GENERAL STRUCTURE                                         |
|                                                                        |
|            H   R   (side chain — the only part that varies)            |
|            |   |                                                       |
|       H2N--C---C--COOH                                                 |
|            |                                                           |
|            (alpha carbon)                                              |
|       amino       carboxyl                                             |
|       group       group                                                |
|                                                                        |
|   PEPTIDE BOND: carboxyl of one + amino of next, lose H2O ->           |
|       --N-C-C(=O)-N-C-C(=O)--   forms the polypeptide backbone         |
+------------------------------------------------------------------------+
```

The 20 side chains span the full chemical alphabet — charged, polar, hydrophobic,
and special-case. This table is reference material you will use in file 02:

| Class | Amino acids (3-letter) | Key trait |
|---|---|---|
| **Nonpolar / hydrophobic** | Gly, Ala, Val, Leu, Ile, Pro, Phe, Met, Trp | bury in core |
| **Polar uncharged** | Ser, Thr, Cys, Tyr, Asn, Gln | H-bond, surface |
| **Acidic (negative)** | Asp, Glu | carboxyl side chain |
| **Basic (positive)** | Lys, Arg, His | amino/guanidino side chain |

Notes worth carrying forward: **Glycine** has just an H side chain (maximally
flexible); **Proline** rings back to its own backbone (a rigid kink, breaks
helices); **Cysteine** can form **disulfide bonds** (covalent cross-links that
staple a fold); **Histidine** has a pKa near 6, so it can be protonated or not at
physiological pH — which makes it the workhorse acid/base group in enzyme active
sites.

Proteins do nearly every active job: catalysis (enzymes), structure (collagen),
transport (hemoglobin), signaling (receptors), motion (myosin), defense
(antibodies). File 02 covers how the linear sequence becomes a 3D machine.

---

## Nucleic Acids — A First Look (Central Dogma in biology/)

Nucleic acids store and transmit information. Their monomer is the **nucleotide**:
a sugar + a phosphate + a nitrogenous base.

```
+------------------------------------------------------------------------+
|   NUCLEOTIDE = phosphate -- sugar -- base                              |
|                                                                        |
|   DNA sugar: deoxyribose      RNA sugar: ribose (extra -OH)            |
|                                                                        |
|   BASES:   A  T  G  C   (DNA)      A  U  G  C   (RNA; U replaces T)    |
|            purines:  A, G   (two rings)                                |
|            pyrimidines: C, T, U   (one ring)                           |
|                                                                        |
|   PAIRING (the information mechanism):  A=T (2 H-bonds)                |
|                                         G=C (3 H-bonds, stronger)      |
+------------------------------------------------------------------------+
```

Two roles of the same chemistry, worth flagging because they cross into other
files:

- **DNA** — double-stranded, stable, the archival store (the "disk"). Structure,
  replication, repair: `biology/` and `genomics/`.
- **RNA** — single-stranded, transient, the working copy and also an enzyme
  (ribozymes). Transcription and translation: `biology/`.

Note the **A1Z26-style elegance**: the entire information system runs on a
**4-symbol alphabet** with **complementary pairing** as its built-in error-check
and copy mechanism — A always pairs with T, G with C. That base-pairing *is* the
copy primitive; replication just reads one strand and writes its complement. We
hand off the information machinery to `biology/` and stay on the chemistry here.

**ATP is also a nucleotide** (adenine + ribose + 3 phosphates) — the same
adenine that pairs in DNA is, with extra phosphates bolted on, the cell's energy
currency. One chemical scaffold, two completely different jobs.

---

## Decision Cheat Sheet

| I need to know... | Look at |
|---|---|
| Why pH must be controlled | Water/pH section — charge state of groups |
| Why oily things clump in water | Hydrophobic effect (water organizing itself) |
| Why we digest starch but not wood | α vs β glycosidic linkage; we lack the β decoder |
| Why fat stores more energy than sugar | ~9 vs ~4 kcal/g; reduced hydrocarbon = more electrons |
| Why membranes form by themselves | Amphipathic phospholipids + hydrophobic effect |
| The 20 amino acids and their classes | Proteins section table |
| Why DNA pairs A-T, G-C | H-bond complementarity; copy/error-check primitive |
| ATP's chemical identity | A nucleotide (adenine-ribose) + 3 phosphates |

---

## Common Confusion Points

### "Is a lipid a polymer like the others?"

No — and it's a common slip. Triglycerides and phospholipids are **assemblies**
(glycerol + a few fatty acids), not long chains of repeating monomers. Lipids are
grouped by their shared **hydrophobic behavior**, not by a common polymer
structure. The other three classes are true polymers.

### "Condensation vs. hydrolysis — which builds, which breaks?"

```
  CONDENSATION (dehydration): bond FORMS, water LEAVES   -> builds polymer
  HYDROLYSIS:                 water ADDED, bond BREAKS    -> breaks polymer
```

Every polymer in biology is built one way and digested the other. Digestion in
your gut is just mass hydrolysis; biosynthesis is condensation paid for with ATP.

### "Why are there exactly 20 amino acids?"

It is a frozen historical accident locked in by the genetic code: 3-base codons
give 64 combinations that map onto 20 amino acids + stop signals. There is nothing
chemically magic about 20; a few organisms even use a 21st/22nd
(selenocysteine, pyrrolysine). The code is in `biology/`/`genomics/`; for
biochemistry, treat 20 as the standard side-chain palette.

### "NADH, ATP, DNA all contain adenine — coincidence?"

Not coincidence — it's reuse. Adenine-ribose (adenosine) is a cheap, ancient
scaffold the cell repurposes everywhere: as an energy carrier (ATP/ADP), as part
of electron carriers (NAD, FAD, coenzyme A all contain an adenosine), and as a
genetic letter. Evolution bolts new function onto an existing part rather than
inventing a new chassis each time — the biochemical equivalent of a shared base
library.
