---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:organic-synthesis
kind: guide
module: chemistry
section: chemistry
title: Organic Synthesis - Design, Named Reactions, Retrosynthesis, Green Chemistry
status: source-custody
source_custody: partial
current_path: chemistry/03-ORGANIC-SYNTHESIS.md
canonical_path: chemistry/03-ORGANIC-SYNTHESIS.md
backsource_ids: [proof-backfill:chemistry:03-organic-synthesis, git-history:chemistry:03-organic-synthesis]
concepts: [retrosynthesis, named-reactions, pericyclic, asymmetric-synthesis, green-chemistry]
root_concepts: [organic-synthesis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Organic Synthesis — Design, Named Reactions, Retrosynthesis, Green Chemistry

**This guide owns** the *design* layer of organic chemistry: retrosynthetic
analysis, the named-reaction toolkit organized by the bond they make, pericyclic
selection rules, protecting-group strategy, asymmetric methods, and green-chemistry
metrics. **It assumes** `natural-sciences/17` (functional groups, stereochemistry,
SN1/SN2/E1/E2) and does not re-teach mechanism basics. Polymerization enters
here only as a *reaction class* — bulk polymer processing, Tg/Mw, and material
properties are `plastics-polymers/`; and structure-activity optimization of a
synthesized drug candidate is `pharmacology/`. Think of it as the
**compiler-optimization pass** of chemistry: given a target molecule, rewrite it
into buildable precursors and choose transformations that maximize yield,
selectivity, and atom economy.

```
THE SYNTHESIS LOOP: TARGET -> PLAN -> BUILD -> VERIFY
==========================================================================
  TARGET molecule
     |
     v   RETROSYNTHESIS (think backwards)
  [ disconnect strategic bonds ] --> SYNTHONS (idealized fragments)
     |                                    |
     |                                    v
     |                          SYNTHETIC EQUIVALENTS (real reagents)
     v                                    |
  simpler precursors  <--- FGI (functional group interconversion)
     |
     v   FORWARD SYNTHESIS (build)
  [ C-C bond | redox | protect/deprotect | set stereochem ]
     |
     v   VERIFY  ->  NMR (06) + MS/IR (07) + XRD (08)

  OPTIMIZE AGAINST: yield x selectivity x atom economy x E-factor
==========================================================================
```

---

## Retrosynthetic Analysis (Corey's formalism)

Draw the **open arrow** (⇒, "is made from") and cut bonds that maximize
simplification. A disconnection yields **synthons** — idealized charged fragments —
which you map to real **synthetic equivalents**.

```
TARGET:  R-CH(OH)-CH2-C(=O)-R'   (a beta-hydroxy ketone)
                  ^ disconnect the C-C bond alpha to the carbonyl
                  |
  SYNTHONS:   R-CHO  +  [ -CH2-C(=O)-R' ]   (an acyl-anion-stabilized enolate)
  EQUIVALENTS: aldehyde  +  enolate of R'-CO-CH3   ==>  ALDOL disconnection
```

Core heuristics:

- **Disconnect at heteroatoms and next to carbonyls** — that is where polarity
  makes a real reaction exist (C–N, C–O, C–X, and the α/β C–C of carbonyls).
- **Recognize the carbonyl as the master functional group**: it is an electrophile
  at C and, as its enolate, a nucleophile at Cα. Most C–C disconnections route
  through it (aldol, Claisen, Michael, Mannich).
- **Umpolung** when natural polarity is wrong: reverse a carbon's donor/acceptor
  character (dithianes as acyl-anion equivalents; the benzoin/Stetter reactions via
  NHC catalysis) to enable otherwise-impossible disconnections.
- **Convergent > linear**: build large fragments separately and join them late; a
  10-step linear route at 80%/step gives 11% overall, but two 5-step arms joined once
  give ~26%. Yield compounds like interest.

---

## Named Reactions, Organized by the Bond They Make

Stop memorizing names; index by *outcome*.

### Make a C–C bond

| Reaction | Combine | Gives | Note |
|---|---|---|---|
| Grignard / organolithium | RMgX + C=O | alcohol | strong nucleophile; no protic/acidic groups |
| Aldol | enolate + aldehyde | β-hydroxy carbonyl | the workhorse; controllable stereochem |
| Claisen condensation | 2 esters | β-keto ester | ester version of aldol |
| Michael addition | enolate + enone | 1,5-dicarbonyl | conjugate (1,4) addition |
| Wittig | R₃P=CHR' + C=O | **alkene** | stabilized ylide → E; non-stabilized → Z |
| Diels-Alder | diene + dienophile | cyclohexene | [4+2], builds 2 bonds + ring + up to 4 stereocenters |
| Pd cross-coupling | R–X + R'–[M] | R–R' | see `01`; biaryls, C–N (Suzuki/Negishi/Buchwald) |
| Olefin metathesis | 2 alkenes | new alkenes | Grubbs Ru; ring-closing (RCM) is powerful |

### Change oxidation state (redox toolkit)

```
REDUCTIONS (add H / remove O)              chemoselectivity
  NaBH4        aldehyde, ketone -> alcohol  (mild; leaves esters, acids)
  LiAlH4       ester/acid/amide/nitrile     (strong; reduces almost everything)
  DIBAL-H      ester -> ALDEHYDE (1 equiv, -78 C; stops at aldehyde)
  H2 / Pd-C    alkene, alkyne; hydrogenolysis of Bn
  CBS / (R)- or (S)- oxazaborolidine        ENANTIOSELECTIVE ketone -> alcohol

OXIDATIONS (remove H / add O)
  PCC, Dess-Martin (DMP), Swern            1o alcohol -> ALDEHYDE (stops there)
  Jones (CrO3/H2SO4), KMnO4                1o alcohol -> carboxylic acid
  mCPBA                                    alkene -> epoxide; Baeyer-Villiger
  OsO4                                     alkene -> cis-diol
```

The single most useful distinction: **NaBH₄ is chemoselective** (touches aldehydes/
ketones, ignores esters and acids), while **LiAlH₄ is a sledgehammer** (reduces
esters, acids, amides, nitriles — and reacts violently with water). **DIBAL-H at
−78 °C** is the trick for stopping an ester at the aldehyde.

---

## Pericyclic Reactions: FMO and Woodward-Hoffmann

Pericyclic reactions have cyclic transition states and are governed by orbital
symmetry, not by nucleophile/electrophile logic. **Frontier Molecular Orbital
(FMO)** theory: reaction is controlled by the HOMO–LUMO interaction of the partners.

**Diels-Alder** ([4+2] cycloaddition) is the paradigm: 6 π electrons, thermally
allowed suprafacial-suprafacial. FMO explains everything about it:

- **Rate**: electron-poor dienophile (LUMO lowered) + electron-rich diene (HOMO
  raised) → smaller gap → faster (normal-demand).
- **Regiochemistry** ("ortho/para" rule): the atoms with the **largest HOMO/LUMO
  coefficients** pair up.
- **Stereochemistry**: *syn* addition is suprafacial on both components → cis
  substituents stay cis; the **endo rule** (kinetic) favors the endo adduct via
  secondary orbital overlap.

**Woodward-Hoffmann selection rules** — allowed/forbidden by electron count and
activation mode:

| Reaction class | Electrons | Thermal | Photochemical |
|---|---|---|---|
| Cycloaddition (e.g., Diels-Alder [4+2]) | 4n+2 | allowed (supra/supra) | forbidden |
| Cycloaddition [2+2] | 4n | forbidden thermally | **allowed** (photo) |
| Electrocyclic ring closure | 4n | **conrotatory** | disrotatory |
| Electrocyclic ring closure | 4n+2 | **disrotatory** | conrotatory |
| Sigmatropic [3,3] (Cope, Claisen) | 6 | allowed, suprafacial | — |

This table is why [2+2] photocycloadditions need light (thermal is forbidden), why
the Nazarov and other electrocyclizations rotate the way they do, and why the
Claisen/Cope [3,3] shifts run cleanly on heating.

---

## Protecting Groups and Orthogonality

When a reagent would hit the wrong functional group, mask it, react, then unmask.
The key property is **orthogonality**: groups removed by *independent* conditions,
so you can deprotect one in the presence of another.

| Protects | Group | Installed | Removed by | Orthogonal to |
|---|---|---|---|---|
| Amine | **Boc** | Boc₂O | acid (TFA) | Cbz, Fmoc |
| Amine | **Cbz** | Cbz-Cl | H₂/Pd (hydrogenolysis) | Boc, Fmoc |
| Amine | **Fmoc** | Fmoc-Cl | base (piperidine) | Boc, Cbz — SPPS standard |
| Alcohol | **TBS** | TBSCl | fluoride (TBAF) | acid/base-labile groups |
| Alcohol | **Bn** | BnBr | H₂/Pd | acid/fluoride groups |
| Alcohol | THP, MOM | DHP / MOMCl | mild acid | fluoride/hydrogenolysis |
| Diol / carbonyl | acetal | diol / HC(OR)₃ | aqueous acid | base/hydrogenolysis |

Orthogonality is **condition-dependent, not a property you can read off a label.**
A worked *non-example*: a substrate carrying a **Boc**-amine and a **TBS**-ether is
often cited as orthogonal, but standard Boc removal uses **TFA**, which is acidic —
and TBS silyl ethers are acid-labile. TFA frequently cleaves a TBS ether as well
(especially primary/less-hindered silyl ethers at the usual 25–50% TFA), so
"strip Boc, keep TBS" is **not** reliably clean; whether it survives depends on the
silyl group's steric bulk and the acid strength/time/temperature (and scavengers).
The reverse direction *is* clean — fluoride (TBAF) removes TBS and leaves Boc
untouched — so this pair is at best *one-way* selective. Genuinely two-way
orthogonal pairs use *independent* chemistry: e.g., **Fmoc**-amine (removed by base,
piperidine) with a **TBS**-ether (removed by fluoride, TBAF), since base and fluoride
ignore each other's group; or **Cbz**-amine (hydrogenolysis) with a TBS-ether
(fluoride). Solid-phase peptide synthesis is built on exactly this independence:
Fmoc (base-off) / side-chain-tBu (acid-off) orthogonality.

---

## Asymmetric Synthesis

Making one enantiomer preferentially. Metrics: **enantiomeric excess** ee =
|%R − %S|; equivalently enantiomeric ratio er. Four strategies, cheapest first:

| Strategy | Idea | Exemplars |
|---|---|---|
| Chiral pool | start from nature's enantiopure feedstock | amino acids, sugars, terpenes |
| Chiral auxiliary | attach, react diastereoselectively, remove | Evans oxazolidinones |
| **Chiral catalyst** | sub-stoichiometric chirality, amplified | Noyori BINAP hydrogenation; Sharpless epoxidation & dihydroxylation; Jacobsen epoxidation/HKR; CBS reduction |
| Organocatalysis | small-molecule chiral catalyst | proline aldol; MacMillan iminium |

Catalytic asymmetric methods are the prize (three shared the 2001 Nobel: Knowles,
Noyori, Sharpless; List & MacMillan won 2021 for organocatalysis) because one
chiral catalyst sets the configuration of thousands of product molecules. Sharpless
epoxidation of allylic alcohols with Ti(OiPr)₄ / tartrate is the textbook case —
the tartrate enantiomer *predicts which face* is epoxidized.

---

## Worked Case: End-to-End Retrosynthesis of a β-Hydroxy Aryl Ketone

Design a route to **T = 1-(4-hydroxyphenyl)-3-hydroxybutan-1-one** — a β-hydroxy
aryl ketone that also carries a phenol and one new stereocenter. This target is a
good teaching case because two very different disconnections genuinely compete, a
protecting group is unavoidable, and the stereocenter forces a chemoselectivity and
asymmetric-method decision.

```
TARGET  T:  HO-C6H4-C(=O)-CH2-CH(OH)-CH3   [Ar = 4-hydroxyphenyl]
            a beta-hydroxy aryl ketone with a phenol; one stereocenter (*)

  Disconnection A  (aldol, the Ca-Cb bond next to the carbonyl):
     Ar-C(=O)-CH3   +   CH3-CHO
     aryl methyl ketone   acetaldehyde        -> 1 C-C bond, convergent
     (enolate = Nu)       (electrophile)

  Disconnection B  (FGI: oxidation-level up at Cb -> a 1,3-diketone):
     Ar-C(=O)-CH2-C(=O)-CH3  --[reduce the ALIPHATIC C=O]-->  T
     1-(4-hydroxyphenyl)butane-1,3-dione     (chemo- + enantioselective)
```

**Competing disconnections and a rejected one.**

| Route | Key step(s) | Strengths | Weaknesses |
|---|---|---|---|
| **A — Aldol** (Cα–Cβ) | (protected) 4′-hydroxyacetophenone enolate + acetaldehyde | convergent, one C–C bond, high atom economy | acetaldehyde self-condenses; an *asymmetric* aldol onto so small an aldehyde is low-ee and finicky |
| **B — 1,3-diketone → reduce** | crossed Claisen acylation of a protected aryl methyl ketone with an acetate equivalent gives Ar–CO–CH₂–CO–CH₃; a substrate-validated asymmetric catalyst or ketoreductase then targets one carbonyl | stereocenter is set after the carbon skeleton exists; catalyst/enzyme screening can optimize site- and enantioselectivity | one extra oxidation-state manipulation; 1-aryl-1,3-diketones are heavily enolized/chelated, so selective monoreduction is a development problem, not a default reagent rule |
| *(rejected)* **Friedel–Crafts** on the Ar–CO bond | acylate the arene with a 3-oxo/3-hydroxybutanoyl equivalent | — | free phenol clashes with the Lewis acid (O-acylation/complexation); a β-oxygenated acyl chloride eliminates (enone/ketene); no stereocontrol |

**Rejected alternatives and why.** The **Friedel–Crafts** construction of the aryl
ketone fails on three counts above — a good reminder that a "valid-looking"
disconnection can be defeated by reagent stability and substrate electronics. Equally,
running *any* enolate or organometallic step with the **phenol unprotected** wastes
reagent: the acidic phenol O–H (pKa ≈ 10) quenches the strong base/nucleophile and
the resulting phenolate interferes — so the phenol must be masked first.

**Protecting-group reasoning (and the orthogonality lesson).** Protect the phenol as
a **silyl ether (TBS/TBDPS)** before the basic/organometallic chemistry. Crucially,
choose the deprotection by the *whole* condition set, not a table label: the product
is a β-hydroxy ketone, which is sensitive to strong acid **and** base (retro-aldol,
or dehydration to the enone). That rules out a harsh-acid deprotection — and, per the
Boc/TBS caution above, strong acid would in any case also strip an acid-labile silyl
group. The clean move is to remove the silyl phenol ether with **fluoride (TBAF)**,
which is orthogonal to both the carbonyl chemistry and the fragile β-hydroxy ketone.
(A benzyl phenol ether removed by hydrogenolysis is an alternative, but H₂/Pd risks
touching other reducible handles — decide per the rest of the molecule.)

**Sequencing and chemoselectivity.** The order is: **protect phenol → crossed
Claisen acylation to the 1,3-diketone → identify a site-selective reduction system →
set the stereocenter → deprotect last.** A concrete Route B begins from protected
4-hydroxyacetophenone: its enolate is acylated with an acetate ester to give the
protected 1-aryl-1,3-butanedione. That intermediate is then screened against
enantioselective transfer-hydrogenation catalysts or ketoreductases for reduction at
the aliphatic carbonyl. The enolized, chelating diketone means **neither NaBH₄ nor a
generic CBS/Noyori label guarantees monoreduction at C3**; site selectivity must be
demonstrated analytically for this substrate. This is the honest development lesson:
the disconnection is valid, but the selectivity claim belongs to measured reaction
performance, not to a reagent mnemonic.

**Route comparison / verdict.** Route A is shorter and more atom-economical (an aldol
is an addition, ~100% atom economy for the C–C step), but its stereocenter is hard to
set well and acetaldehyde misbehaves. Route B spends one extra oxidation-state step to
*buy reliable stereocontrol*: asymmetric ketone reduction is far more mature and
higher-ee than a small-aldehyde asymmetric aldol, and the diketone is a robust
intermediate. **For an enantiopure target, Route B usually wins; if racemate is
fine, Route A's convergence and atom economy win.** Note the honest trade-off the
Green-Chemistry section formalizes next: Route A's high *atom economy* can be undercut
by the extra steps/auxiliaries needed for ee, which inflate its *PMI/E-factor* — the
whole-process numbers, not the single-step ideal, decide the greener route.

---

## Green Chemistry Metrics

Anastas & Warner's **12 Principles** (1998) reframed "good synthesis" to include
waste and hazard. The quantitative core:

```
ATOM ECONOMY  =  (MW of desired product / sum of MW of all reactants) x 100%
   -> a DESIGN metric: addition/rearrangement ~100%; substitution/elimination lose
      atoms as stoichiometric byproducts.  Diels-Alder = 100% atom economy.

E-FACTOR  =  kg waste / kg product        (Sheldon)
   bulk chemicals ~ <1-5 | fine chemicals ~5-50 | pharma ~25->100

PMI (Process Mass Intensity) = total mass in (incl. solvent, water) / mass product
   -> the honest number; solvent usually dominates it.
```

Atom economy is intrinsic to the *reaction chosen* (a catalytic addition beats a
Wittig that ejects Ph₃P=O); E-factor and PMI capture the *whole process* including
solvent and workup, which is where most real waste hides. Catalysis, solvent
reduction, and avoiding protecting groups are the three biggest levers.

---

## Reader Tasks

1. **Disconnect a β-hydroxy carbonyl.** The C–C bond α to the carbonyl is the
   **aldol** disconnection → an aldehyde synthon + an enolate synthon (equivalents:
   an aldehyde + a ketone/ester enolate).
2. **Predict Diels-Alder regiochemistry.** Match the largest FMO coefficients: a
   1-substituted (electron-rich) diene with a mono-substituted dienophile gives the
   "ortho/para" product; endo is the kinetic major adduct.
3. **Choose an orthogonal protecting-group pair.** To expose an alcohol while keeping
   an amine masked, **TBS** (alcohol, removed by fluoride/TBAF) with **Boc** (amine)
   works *in that direction* — TBAF leaves Boc untouched. But the pair is only
   one-way clean: removing Boc with acid (TFA) would also cleave the acid-labile TBS,
   so for two-way independence pick truly orthogonal chemistry (e.g., Fmoc/base +
   TBS/fluoride, or Cbz/hydrogenolysis + TBS/fluoride).
4. **Stop an ester at the aldehyde.** Use **DIBAL-H, 1 equiv, −78 °C** (LiAlH₄ would
   over-reduce to the alcohol; NaBH₄ won't touch the ester at all).
5. **Compute an E-factor.** Sum all input masses minus product mass, divide by
   product mass; a route with a stoichiometric metal oxidant and lots of solvent will
   have a high E-factor even at good yield — motivating a catalytic redesign.

## Decision Cheat Sheet

| Need | Reagent / tactic | Watch out for |
|---|---|---|
| Make a C–C bond to a carbonyl | aldol / Grignard | Grignard: no OH/NH/acidic H present |
| Make an alkene from a carbonyl | Wittig | ylide type sets E/Z |
| Build a ring + stereocenters | Diels-Alder | endo kinetic; regiochem from FMO |
| Reduce ketone, keep ester | NaBH₄ | LiAlH₄ would hit the ester |
| Ester → aldehyde | DIBAL-H, −78 °C | 1 equiv; warm-up over-reduces |
| 1° alcohol → aldehyde (stop) | DMP / Swern / PCC | Jones/KMnO₄ overshoot to acid |
| Set one enantiomer catalytically | Sharpless / Noyori / CBS | match catalyst enantiomer to target |
| Mask an amine for SPPS | Fmoc | base-labile; orthogonal to tBu |
| Improve "greenness" | catalysis, cut solvent | PMI is solvent-dominated |

## Common Confusion Points

- **Retrosynthesis arrows point backward.** ⇒ means "is made from"; do not read it
  as a forward reaction. Synthons are fictional; you build with their real
  equivalents.
- **Endo/exo vs cis/trans.** Endo is a transition-state (kinetic) preference about
  orientation to the diene; it is not the same axis as the retained cis/trans
  relationship of substituents.
- **Thermal [2+2] is forbidden, not merely slow.** Orbital symmetry forbids it;
  that is why [2+2] cycloadditions require photochemistry (or a metal template).
- **NaBH₄ ≠ LiAlH₄.** Reaching for the strong hydride when you needed
  chemoselectivity destroys esters and generates H₂ on contact with water.
- **Atom economy ≠ yield.** A reaction can be 95% yield yet 40% atom-economical
  (half the reactant mass leaves as byproduct). Green metrics and yield are
  independent knobs.
- **Protecting groups are a tax, not a strategy.** Each add/remove pair costs two
  steps and atoms; a protecting-group-free route is greener when achievable.
