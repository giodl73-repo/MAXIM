# 17 — Organic Chemistry

## Functional Groups, Reaction Mechanisms, Stereochemistry, Synthesis

---

## Big Picture: Carbon's Uniqueness

```
WHY CARBON DOMINATES LIFE AND CHEMISTRY
─────────────────────────────────────────────────────────────────────
  Carbon: 4 valence electrons, can bond to itself indefinitely
           Small enough for strong C-C bonds (83 kcal/mol)
           Large enough for 4 stable bonds (not H₂'s problem)
           Stable C-C, C=C, C≡C, C-N, C-O, C-S, C-H

HYBRIDIZATION → GEOMETRY
  sp³ → tetrahedral    (109.5°)   alkanes, alcohols, amines
  sp² → trigonal planar (120°)   alkenes, carbonyls, aromatics
  sp  → linear         (180°)   alkynes, nitriles, ketenes

          sp³                    sp²                  sp
    H   H                       H
    |   |                       |
H—C—C—H          H—C═CH₂         H—C≡C—H
    |   |               |
    H   H               (π bond above/below plane)

ORBITAL VIEW:
  sp³: σ bonds only, no π system, free rotation
  sp²: 1 π bond from unhybridized p orbitals, restricted rotation
  sp:  2 π bonds, cylindrical π electron density
  π + π conjugation → delocalization → lower energy, new reactivity

FUNCTIONAL GROUP REACTIVITY HIERARCHY (high → low)
  Acyl halides (RCOCl) > Anhydrides > Carboxylic acids (RCOOH)
  > Esters (RCOOR') > Amides (RCONH₂) > Aldehydes (RCHO)
  > Ketones (RCOR') > Alcohols (ROH) > Ethers (ROR')
  > Alkenes/alkynes > Alkanes
─────────────────────────────────────────────────────────────────────
```

---

## Functional Group Taxonomy

```
CLASS        STRUCTURE     FUNCTIONAL GROUP       KEY REACTIONS
──────────────────────────────────────────────────────────────────
Alkane       C-C-C         —CH₃, —CH₂—, >CH—     Free radical halogenation
Alkene       C=C           C═C                    Electrophilic addition, oxidation
Alkyne       C≡C           C≡C                    Addition (Markovnikov/anti), reduction
Aromatic     benzene ring  Ar                     Electrophilic/nucleophilic aromatic sub.
Alcohol      R-OH          —OH (hydroxyl)         Dehydration, oxidation, esterification
Ether        R-O-R'        C-O-C                  Lewis base, acid cleavage, peroxide risk
Aldehyde     RCHO          —CHO                   Nucleophilic addition, oxidation
Ketone       RCOR'         C═O (ketone)           Nucleophilic addition (less reactive)
Carboxylic   RCOOH         —COOH                  Acyl substitution, esterification
acid
Ester        RCOOR'        —COO—                  Saponification, transesterification
Amide        RCONH₂        —CONH—                 Most stable acyl derivative
Amine        R-NH₂         —NH₂, >NH, >N—         Base, nucleophile, acylation
Nitrile      RC≡N          —C≡N                   Hydrolysis → acid, reduction → amine
Thiol        R-SH          —SH                    Oxidation → disulfide, metal binding
Halide       R-X (X=F,Cl   C-X                    SN1/SN2 substitution, E1/E2 elimination
             Br,I)
```

---

## Stereochemistry

```
CHIRALITY
  A carbon with 4 different substituents is a stereocenter (chiral center)
  Enantiomers: non-superimposable mirror images — same connectivity, different handedness
  Diastereomers: stereoisomers that are NOT mirror images
  Meso compound: has stereocenters but an internal plane of symmetry → achiral overall

CIP PRIORITY RULES (Cahn-Ingold-Prelog):
  1. Higher atomic number = higher priority
  2. Tie: go to next atoms (breadth-first traversal)
  3. Phantom atoms for double/triple bonds (duplicated atoms, Z=0 for phantom)
  Examples:
    -OH > -NH₂ > -CH₃ > -H       (O>N>C>H by atomic number)
    -CH₂OH > -CH₃                 (O branching gives higher priority)
    -CHO > -CH₂OH                 (CHO: carbon bonded to O,O,H vs CH₂OH: C bonded to O,H,H)

R/S ASSIGNMENT:
  1. Assign priorities 1-4 to substituents
  2. Orient so priority 4 points away from you
  3. Trace 1→2→3:  clockwise = R (rectus)
                   counterclockwise = S (sinister)

E/Z (formerly cis/trans) for alkenes:
  E (Entgegen, "opposite"): higher priority groups on opposite sides of double bond
  Z (Zusammen, "together"): higher priority groups on same side

    H   CH₃          H   Cl
     \ /               \ /
      C═C   → (E)        C═C   → depends on priority of all 4 groups
     / \               / \
   Cl   CH₂CH₃       Cl   CH₃   → (Z) if Cl > H and Cl > CH₃

OPTICAL ACTIVITY:
  Enantiomers rotate plane-polarized light equal amounts, opposite directions
  (+) or (d) = dextrorotatory     (−) or (l) = levorotatory
  Racemate (50/50 mixture) = no net rotation
  Note: R/S (configuration) ≠ (+)/(−) (optical rotation) — empirical relationship
```

---

## Reaction Mechanisms

```
CURVED ARROW FORMALISM:
  Arrow tail: where electrons come from (lone pair or bond)
  Arrow head: where electrons go (new bond or charge center)
  Half-headed (fishhook) arrow: single electron movement (radical)

FOUR MECHANISM TYPES:
  1. Nucleophilic:  Nu: attacks electrophile (C⁺, C-LG)
  2. Electrophilic: E⁺ attacks π system or lone pair
  3. Radical:       homolytic cleavage, one electron at a time
  4. Pericyclic:    concerted cyclic TS, no intermediates

NUCLEOPHILICITY vs BASICITY:
  Basicity:       thermodynamic, affinity for proton (equilibrium pKa)
  Nucleophilicity: kinetic, rate of attack on carbon
  General trend:   same group → more basic = more nucleophilic
  Exceptions:      steric effects reduce nucleophilicity (tBuO⁻: strong base, poor Nu)
                   polarizability: large/soft nucleophiles better in SN2
                   Iodide I⁻: weak base but excellent nucleophile (polarizable)

LEAVING GROUPS (LG) — ranked by ability:
  Best LG: I⁻ > Br⁻ > Cl⁻ > F⁻ (matches base strength inverse)
           TsO⁻ (tosylate), MsO⁻ (mesylate) — excellent LG for alcohols
  The LG departs with both electrons → C remains electrophilic
  F⁻ is the worst LG despite being most electronegative
  (C-F bond very strong, high BDE — ΔG‡ too high)

CARBOCATION STABILITY:
  3° > 2° > 1° > methyl  (hyperconjugation + induction from alkyl groups)
  Allylic ≈ benzylic > 3° (resonance delocalization)
  Vinyl, aryl carbocations: very unstable (no good resonance/hyperconjugation)

RADICAL STABILITY (same order as carbocations):
  3° > 2° > 1° > methyl  (hyperconjugation)
  Allylic ≈ benzylic > 3° (resonance delocalization)
```

---

## Substitution and Elimination

```
SN1 — UNIMOLECULAR NUCLEOPHILIC SUBSTITUTION
  Mechanism: 2 steps
    Step 1: R-LG → R⁺ + LG⁻   (rate-determining, ionization)
    Step 2: R⁺ + Nu⁻ → R-Nu    (fast)
  Rate: rate = k[R-LG]          (first order — depends only on substrate)
  Stereochemistry: flat carbocation → racemization (some inversion bias from ion pair)
  Substrate:  3° >> 2° >> 1° (must stabilize carbocation)
  Solvent:    polar protic (stabilizes ions by solvation: water, alcohols)
  Rearrangements possible: 1,2-hydride/methyl shifts to more stable carbocation

SN2 — BIMOLECULAR NUCLEOPHILIC SUBSTITUTION
  Mechanism: 1 concerted step
    Nu⁻ + R-LG → [Nu···C···LG]‡ → Nu-R + LG⁻
  Rate: rate = k[Nu][R-LG]       (second order)
  Stereochemistry: backside attack → INVERSION (Walden inversion)

         Nu:     LG                Nu     :LG
          \      /     →      C        +
           C →  C        (inversion of configuration)
          / \  /         at the stereocenter

  Substrate:  1° >> 2° >> 3° (steric accessibility required)
  Solvent:    polar aprotic (DMSO, DMF, acetone — solvates cation not anion)
  Nucleophile: strong, unhindered Nu needed (CN⁻, I⁻, RS⁻, N₃⁻)

COMPETITION:
  3° substrate + strong Nu/base → E2 preferred (bulky base → Hofmann alkene)
  3° substrate + weak base/good Nu → SN1
  1° substrate + strong Nu → SN2
  1° substrate + strong bulky base → E2

E1 — UNIMOLECULAR ELIMINATION
  Mechanism: same ionization as SN1 → then β-H removed
  Conditions: same as SN1 (3°, weak/no base, polar protic, heat)
  Products: more substituted alkene (Zaitsev) usually
  Stereochemistry: no geometric requirement (carbocation is flat)

E2 — BIMOLECULAR ELIMINATION
  Mechanism: concerted — base removes β-H as LG departs

         B:     H                 B-H
              |                    |
         C──C──LG  →    C═C    +  LG⁻
              |

  Anti-periplanar geometry required (H and LG 180° dihedral — eclipsed dihedral)
  Rate: rate = k[Base][R-LG]
  Regioselectivity:
    Zaitsev: most substituted = thermodynamic (more stable) alkene (normal base)
    Hofmann: least substituted alkene (bulky base like tBuO⁻ — kinetic)

──────────────────────────────────────────────────────────────────
DECISION TREE: SN1/SN2/E1/E2
  Is the substrate primary?
    YES → SN2 (strong Nu) or E2 (strong hindered base)
  Is the substrate tertiary?
    + strong base → E2 (Zaitsev or Hofmann)
    + weak base, polar protic → SN1/E1 (heat → E1)
    + polar aprotic → mostly SN1
  Is the substrate secondary?
    + strong unhindered base → E2 vs SN2 competition
    + weak base polar protic → SN1/E1
──────────────────────────────────────────────────────────────────
```

---

## Alkene and Carbonyl Additions

```
ELECTROPHILIC ADDITION TO ALKENES
  General: π electrons attack electrophile → carbocation → nucleophile attacks

  Markovnikov's Rule (H adds to LESS substituted carbon):
    Electrophile adds to give MORE STABLE carbocation intermediate
    H-X adds across double bond: X ends up on more substituted carbon
    Mechanistic basis: more substituted carbocation more stable

  HBr + peroxide (anti-Markovnikov, radical mechanism):
    Br• adds to less hindered carbon (giving more stable radical)
    Result: Br on less substituted carbon → anti-Markovnikov

  Halogenation (Br₂, Cl₂):
    Cyclic halonium ion intermediate
    Nucleophile attacks anti → anti addition → trans product
    Br₂ + alkene → trans-dibromide

  Hydration (H₂O/H⁺):
    Markovnikov (OH on more substituted carbon)
    Via carbocation → rearrangements possible

  Oxymercuration-demercuration: Markovnikov, no rearrangement
  Hydroboration-oxidation: anti-Markovnikov, syn addition of H and OH

  Ozonolysis: cleaves double bond → two carbonyl fragments
    O₃ then (CH₃)₂S (reductive) → aldehydes/ketones
    O₃ then H₂O₂ (oxidative) → carboxylic acids

NUCLEOPHILIC ADDITION TO CARBONYLS
  π* (LUMO) of C=O attacked by nucleophile (Nu: → C)
  Tetrahedral intermediate forms → protonation gives product

  Aldehydes > Ketones (less steric, more electrophilic)

  Nu:           Reagent               Product
  ──────────────────────────────────────────────────────
  H⁻ (hydride)  NaBH₄ (ketone/ald)    alcohol
  H⁻ (hydride)  LiAlH₄ (+ esters)    primary alcohol
  R-MgBr        Grignard             alcohol (new C-C)
  R-Li          Organolithium        alcohol (new C-C)
  CN⁻           HCN/KCN              cyanohydrin
  R-C≡C⁻        acetylide            propargylic alcohol
  RNH₂          amine                imine (Schiff base)
  ROH           alcohol              hemiacetal → acetal
  Wittig ylide  Ph₃P=CR₂             alkene (removes O)

ACYL SUBSTITUTION
  Carboxylic acid derivatives (least → most reactive to Nu):
  Amide < Ester < Carboxylic acid < Anhydride < Acyl halide

  All share same mechanism: tetrahedral intermediate → collapse
  More reactive: better leaving group attached to carbonyl
  Cl⁻ >> RCOO⁻ >> RO⁻ >> HO⁻ >> NH₂⁻ (leaving group ability)

  Saponification: ester + NaOH → carboxylate + alcohol (irreversible)
  Fischer esterification: acid + alcohol ⇌ ester + H₂O (reversible, acid catalyst)
```

---

## Enolates and Aldol Chemistry

```
ENOLS AND ENOLATES
  Carbonyl compound with α-hydrogen → can form enol (keto-enol tautomerism)
  Under base: α-H removed → enolate (resonance-stabilized carbanion)
  Under acid: O-protonated → enol

           O                  O⁻                OH
           ‖                  |                  |
    H—C—CH₂—   ⇌    C═CH—   ⇌    C═CH—
  ketone/aldehyde   enolate      enol

  Kinetic vs thermodynamic enolate:
    Kinetic (LDA, −78°C): sterically hindered base, less substituted, faster deprotonation
    Thermodynamic (NaH, equilibrating): more stable, more substituted enolate

ALDOL CONDENSATION
  Step 1: enolate (α-carbon nucleophile) attacks aldehyde/ketone carbonyl
  Step 2: tetrahedral alkoxide → protonation → β-hydroxy carbonyl (aldol product)
  Step 3 (optional): dehydration with heat → α,β-unsaturated carbonyl (aldol condensation)

       O                    O    OH               O
       ‖                    ‖    |                ‖
  CH₃-C-CH₃  →  enolate    → aldol   → heat →  C═C-CHO
  (acetone)     attacks               -H₂O    (mesityl oxide)

MICHAEL ADDITION:
  1,4-addition (conjugate addition) of soft nucleophile to α,β-unsaturated carbonyl
  Enolate + chalcone → 1,5-dicarbonyl product
  Mechanistic: Nu attacks β-carbon of C=C-C=O (softer site)

ROBINSON ANNULATION:
  Michael addition + aldol → 6-membered ring (classic steroid synthesis strategy)
```

---

## Aromatic Chemistry

```
AROMATICITY — HÜCKEL'S RULE
  Criteria: planar, fully conjugated ring, 4n+2 π electrons (n=0,1,2,...)
  n=0: 2 π e⁻  — cyclopropene cation
  n=1: 6 π e⁻  — benzene (the archetype), pyridine, pyrrole, furan, thiophene
  n=2: 10 π e⁻ — naphthalene, azulene
  Anti-aromatic: 4n π electrons (cyclobutadiene 4 π e⁻, cyclopentadienyl cation)

  Heterocycles:
    Pyridine: N lone pair perpendicular to ring (not in π system) → sp² N, basic
    Pyrrole:  N lone pair in π system (contributes 2) → not basic at N, aromatic
    Furan:    O lone pair contributes 2 → aromatic (weaker than benzene)

ELECTROPHILIC AROMATIC SUBSTITUTION (EAS)
  Mechanism: addition-elimination
    Step 1: electrophile attacks π ring → arenium ion (Wheland intermediate, σ complex)
    Step 2: proton loss restores aromaticity

  Key reactions:
    Nitration:        ArH + HNO₃/H₂SO₄  → Ar-NO₂ + H₂O
    Halogenation:     ArH + Br₂/FeBr₃  → Ar-Br + HBr
    Friedel-Crafts A: ArH + RCl/AlCl₃  → Ar-R + HCl  (alkylation)
    Friedel-Crafts K: ArH + RCOCl/AlCl₃ → Ar-COR + HCl  (acylation)
    Sulfonation:      ArH + SO₃/H₂SO₄  → Ar-SO₃H  (reversible)

DIRECTING EFFECTS:
  o/p directors (EDG — electron-donating groups):
    Activating: -OH, -OR, -NH₂, -NHR, -NR₂, -NHCOR
    Weakly activating: -alkyl, -Ph (hyperconjugation/mild induction)
  m directors (EWG — electron-withdrawing groups, all deactivating):
    -NO₂, -CN, -CHO, -COR, -COOR, -COOH, -SO₃H, -NR₃⁺, -CF₃

  Mechanism of direction:
    EDG: ortho/para carbons have higher electron density (resonance donation)
    EWG: ortho/para carbons depleted → meta attack faster (least electron-poor)
    Halogens: deactivating (inductive) but o/p directing (resonance donation via lone pairs)

NUCLEOPHILIC AROMATIC SUBSTITUTION (NAS)
  Requires: strong electron-withdrawing groups ortho/para to leaving group
  Mechanism: addition-elimination (Meisenheimer complex intermediate)
    Nu attacks → Meisenheimer σ complex → LG departs
  Classic: 2,4-dinitrochlorobenzene + MeO⁻ → 2,4-dinitroanisole
```

---

## Pericyclic Reactions

```
WOODWARD-HOFFMANN ORBITAL SYMMETRY RULES
  Concerted reactions — thermal vs photochemical allowed/forbidden
  Governed by frontier molecular orbital (FMO) theory:
    HOMO of nucleophile must match symmetry of LUMO of electrophile

  THERMAL vs PHOTOCHEMICAL:
    Thermal:  lowest energy (ground state) orbital symmetry governs
    Photo:    one electron promoted → excited state HOMO changes symmetry

DIELS-ALDER [4+2] CYCLOADDITION
  Diene (4π) + dienophile (2π) → 6-membered ring (σ bond formation ×2)
  Thermal: ALLOWED (thermal [4s+2s])

  Requirements:
    Diene: must adopt s-cis conformation (open-chain) or locked-s-cis
    Dienophile: electron-poor (normal demand): C=C-EWG, C=O, C=N
    Electron-rich diene + electron-poor dienophile = most reactive

  Stereochemistry:
    Suprafacial on both components → retains cis/trans geometry
    Endo rule: endo transition state favored (max secondary orbital interaction)
    Endo product kinetically favored; exo thermodynamically (larger substituents exo)

     diene       +    dienophile     →   cyclohexene

   CH₂                 CHO                     CHO
   |                   |                       |
   CH   CH₂         H-C              →    six-membered ring
   ‖                   ‖
   CH   CH₂        H-C   (CHCHO)
   |
   CH₂

[2+2] CYCLOADDITION
  Thermal: FORBIDDEN (orbital symmetry mismatch)
  Photochemical: ALLOWED
  Used to make cyclobutanes: ketones + alkenes under hν (Paternò-Büchi)

ELECTROCYCLIC REACTIONS
  Ring closure/opening of conjugated polyenes
  4π: conrotatory (thermal) / disrotatory (photochemical)
  6π: disrotatory (thermal) / conrotatory (photochemical)
  Rule: thermal and photochemical are opposite for same π-system

SIGMATROPIC REARRANGEMENTS
  [1,5]-H shift: thermal allowed (suprafacial)
  [3,3]-Claisen rearrangement: allyl vinyl ether → γ,δ-unsaturated carbonyl
  [3,3]-Cope rearrangement: 1,5-hexadiene → 1,5-hexadiene (degenerate)
  Thermal [1,3]-H shift: forbidden (requires inversion at migrating carbon)
```

---

## Organometallic Reactions

```
GRIGNARD REAGENT (RMgBr, RMgCl)
  Preparation: R-X + Mg(0)/ether  → R-MgX
  Reactivity:  R⁻ equivalent (carbanion character) — strong nucleophile and base

  Reactions:
    HCHO → 1° alcohol
    RCHO → 2° alcohol
    RCOR' → 3° alcohol
    CO₂ → carboxylic acid (RCOOH)
    Esters → 3° alcohol (2 equiv Grignard)
    Nitriles → ketone (after hydrolysis)

  Incompatible: water, alcohols, acids, any X-H (will protonate Grignard immediately)
  Must use dry ethereal solvent (Et₂O, THF)

WITTIG REACTION
  Ph₃P + R-X → Ph₃P⁺-R X⁻ (phosphonium salt)
  Base → ylide: Ph₃P=CR'₂ (stabilized or unstabilized)
  Ylide + carbonyl → [4-membered betaine] → C=C + Ph₃P=O
  Converts C=O → C=C  (replaces oxygen with alkene — complement to ozonolysis)
  Stabilized ylides: EWG adjacent → E-alkenes (thermodynamic)
  Unstabilized ylides: no EWG → Z-alkenes (kinetic, Wittig)

PALLADIUM-CATALYZED CROSS-COUPLING
  General: R-X + R'-M → R-R'  (Pd catalyst)
  M = B(OH)₂ (Suzuki), SnR₃ (Stille), ZnX (Negishi), SiR₃ (Hiyama)
  Heck: ArX + alkene → Ar-alkene (no organometallic)

  Catalytic cycle:
    Oxidative addition: Pd(0) + R-X → R-Pd(II)-X
    Transmetalation: R-Pd-X + R'-M → R-Pd-R' + MX
    Reductive elimination: R-Pd-R' → R-R' + Pd(0)

  Suzuki scope: aryl halides/triflates + ArB(OH)₂ → biaryl products
  Nobel Prize 2010: Heck, Negishi, Suzuki for Pd-catalyzed cross-coupling
```

---

## Retrosynthetic Analysis

```
RETROSYNTHESIS (Corey's disconnection approach)
  Work backwards: target → simpler intermediates → available starting materials
  Key operation: disconnection (break a bond in imagination → synthons)
  Synthon: idealized fragment; corresponds to real reagent (synthetic equivalent)

  Double-headed arrow ⟹ means "can be made from" (retrosynthetic arrow)

  FUNCTIONAL GROUP INTERCONVERSION (FGI):
    alcohol ⟹ ketone/aldehyde (oxidation)
    alkene ⟹ alcohol (elimination)
    amine ⟹ amide → amine (reduction)
    nitrile → carboxylic acid (hydrolysis)

  KEY DISCONNECTIONS:
    C-C next to C=O → aldol
    C-C via Michael → 1,5-dicarbonyl
    C-C via Grignard → alcohol (α to OH disconnect)
    Aromatic ring-C → Friedel-Crafts or coupling
    Cyclopentane/cyclohexane → Diels-Alder

PROTECTING GROUPS
  Concept: temporarily mask a functional group to allow selective reaction elsewhere

  Common protecting groups:
    Alcohol: TMS ether (R-OTMS), TBS ether (silyl, acid-labile),
             MOM ether (base-stable), Bn ether (H₂/Pd labile)
    Carbonyl: acetal/ketal (diol + acid → acetal, base-stable)
    Amine:   Boc (tBuOCO, TFA labile), Cbz (H₂/Pd labile), Fmoc (base labile)
    Carboxylic acid: methyl/ethyl ester (base hydrolysis)

  Green chemistry concern: protecting groups → extra steps, waste
  Modern strategy: use catalytic selectivity to avoid protecting groups entirely
```

---

## Spectroscopic Structure Determination

```
INFRARED SPECTROSCOPY (IR)
  Absorbs IR → molecular vibrations (stretch, bend)
  Functional group region (4000-1500 cm⁻¹) — diagnostic
  Fingerprint region (1500-600 cm⁻¹) — unique to compound

  KEY ABSORPTIONS:
    O-H stretch:  2500-3300 cm⁻¹ (broad)  — carboxylic acid
    O-H stretch:  3200-3600 cm⁻¹ (broad)  — alcohol (H-bonded)
    N-H stretch:  3300-3500 cm⁻¹          — amine/amide
    C-H stretch:  2850-3000 cm⁻¹          — sp³
    ≡C-H:        3300 cm⁻¹               — terminal alkyne
    C═O stretch:  1700-1750 cm⁻¹          — ketone/aldehyde (sharp, strong)
    C═O:         1735 cm⁻¹               — ester
    C═O:         1680 cm⁻¹               — amide (N resonance lowers frequency)
    C═O:         1800 cm⁻¹               — acyl chloride
    C═C stretch:  1620-1680 cm⁻¹          — alkene
    C≡C:         2100-2260 cm⁻¹           — alkyne
    C≡N:         2200-2260 cm⁻¹           — nitrile
    C-O stretch:  1050-1200 cm⁻¹          — ether/ester

¹H NMR (Proton NMR)
  Measures chemical environment of H atoms

  Reference: TMS (tetramethylsilane) = 0 ppm
  Downfield (high ppm) = deshielded (near electronegative atoms)
  Upfield (low ppm) = shielded

  TYPICAL CHEMICAL SHIFTS:
    R-CH₃, R-CH₂, R-CH:  0.8-1.8 ppm   (alkyl)
    Allylic -CH₂-C═C:    1.6-2.6 ppm
    α to C═O:            2.0-2.6 ppm
    Alkyne ≡C-H:         2.5 ppm
    -OCH₃, -OCH₂:       3.3-4.5 ppm   (near O)
    Vinylic ═CH:         4.5-6.5 ppm   (alkene)
    ArH:                 6.5-8.5 ppm   (aromatic)
    RCHO:                9.0-10.0 ppm  (aldehyde H)
    RCOOH, ArOH:         10-12 ppm     (acidic, broad, variable)

  COUPLING (spin-spin splitting — n+1 rule):
    n adjacent H → signal splits into n+1 lines
    Coupling constant J (Hz): magnitude from geometry (vicinal = 6-8 Hz, geminal = 0-3 Hz)
    Integration: height proportional to number of H atoms

¹³C NMR
  Useful ranges:
    Alkyl C:     0-50 ppm
    C-O (sp³):  60-90 ppm
    Alkyne:     60-90 ppm
    Alkene:     100-150 ppm
    Aromatic:   110-160 ppm
    C═O:       160-220 ppm  (distinct region: ester/acid 160-180, ketone/ald 190-220)

MASS SPECTROMETRY
  M⁺ (molecular ion): molecular weight
  M+1: ¹³C content (1.1% per C — counts carbons)
  M+2: ³⁷Cl (33%), ⁷⁹Br (50%) — characteristic isotope patterns
  Common fragments:
    Loss of 15: -CH₃
    Loss of 17: -OH (from alcohol)
    Loss of 29: -CHO (aldehyde)
    McLafferty rearrangement: β-cleavage + γ-H transfer (characteristic of ketones)
```

---

## Decision Cheat Sheet

| Reaction Goal | Method | Key Condition |
|---------------|--------|---------------|
| Add -OH to alkene (Markovnikov) | Acid-catalyzed hydration or oxymercuration | H₃O⁺ or Hg(OAc)₂/NaBH₄ |
| Add -OH anti-Markovnikov | Hydroboration-oxidation | BH₃·THF then H₂O₂/NaOH |
| Convert C=O → C=C | Wittig | Ph₃P=CR₂, ylide |
| New C-C bond via carbocation | Aldol | Base/enolate |
| New C-C bond via organometallic | Grignard / Suzuki | RMgBr / RB(OH)₂ + Pd |
| Cleave alkene | Ozonolysis | O₃ then reductive (DMS) or oxidative (H₂O₂) |
| Substitute (1°, retention not needed) | SN2 | Polar aprotic, good Nu |
| Eliminate (bulky base) | E2 Hofmann | tBuO⁻K⁺ |
| Nitration of benzene | EAS: HNO₃/H₂SO₄ | Need protonation to form NO₂⁺ |
| [4+2] ring formation | Diels-Alder | EDG diene + EWG dienophile |
| Cyclobutane via photochem | [2+2] cycloaddition | hν (not thermal) |
| Identify carbonyl type | IR | C═O at 1735 (ester), 1700 (ketone), 1680 (amide) |
| Count carbons | ¹³C NMR | Each unique C → one peak |
| Confirm MW | Mass spec | M⁺ peak; M+2 for Br/Cl |

---

## Common Confusion Points

**SN1 rearrangements**: A carbocation intermediate means 1,2-hydride and 1,2-methyl shifts can occur to reach a more stable carbocation. If you see a product with rearranged skeleton, it went through SN1.

**E2 requires anti-periplanar geometry**: Two groups must be 180° apart (anti, not gauche). This means the leaving group and the β-hydrogen must both be axial in cyclohexane conformations for E2 to work.

**Zaitsev vs Hofmann**: Small base (EtO⁻) → Zaitsev (more substituted alkene). Bulky base (tBuO⁻) → Hofmann (less substituted, less hindered β-H). Think about where the base can reach.

**¹H NMR chemical shifts**: Aromatic H at ~7-8 ppm seems high — it's due to ring current (anisotropy from π electrons). Aldehyde H at 9-10 ppm is the most downfield non-acidic H.

**Hückel's rule counts π electrons not carbons**: Cyclopentadienyl anion (5 carbons, 6 π e⁻) is aromatic. Cycloheptatrienyl cation (7 carbons, 6 π e⁻) is aromatic.

**Acetal vs hemiacetal**: Hemiacetal (one OH, one OR) → in equilibrium with carbonyl. Acetal (two OR groups) → stable to base, acid-labile. Acetal = protecting group strategy.

**Grignard incompatibility**: RMgBr is a carbanion equivalent. It will react with ANY proton source (H₂O, ROH, RCOOH, RNH₂). Keep everything dry.

**Wittig replaces C=O with C=C**: Remember that Ph₃P=O is the byproduct (drives equilibrium). Stabilized ylide (EWG adjacent) → E-alkene. Unstabilized → Z-alkene.
