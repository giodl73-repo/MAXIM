# Organogenesis: How Organs Form

## The Big Picture

Organogenesis (Weeks 4-8 in humans) is when specific organ structures form from the three germ layers. Each organ involves: specification of a progenitor field, inductive interactions between tissue layers, branching morphogenesis, and refinement by apoptosis and mechanical forces.

```
+──────────────────────────────────────────────────────────────────+
|              ORGANOGENESIS OVERVIEW                              |
|                                                                  |
|  GERM LAYER → ORGAN SYSTEM DERIVATION                           |
|                                                                  |
|  ECTODERM ──────────────────────────────────────────────────►  |
|  (outer)    Brain, spinal cord, PNS, skin, eye lens, ear         |
|             Neural crest → PNS, craniofacial, melanocytes        |
|                                                                  |
|  MESODERM ──────────────────────────────────────────────────►  |
|  (middle)   Heart, blood vessels, kidneys, skeleton, muscle,     |
|             spleen, gonads, connective tissue (dermis)           |
|             ↑ receives inductive signals from endoderm (heart)   |
|             ↑ and from ectoderm (limb)                           |
|                                                                  |
|  ENDODERM ──────────────────────────────────────────────────►  |
|  (inner)    Gut epithelium, liver, pancreas, lungs, thyroid,     |
|             thymus, bladder lining                               |
|                                                                  |
|  CORE PRINCIPLES (shared across all organs)                     |
|  1. INDUCTION: epithelium ↔ mesenchyme reciprocal signaling      |
|  2. PATTERNING: morphogen gradients encode positional identity   |
|  3. BRANCHING: recursive bifurcation (FGF/Wnt on, BMP off tip)  |
|  4. APOPTOSIS: sculpts cavities, digit separation, valves        |
|  5. MECHANICS: ECM stiffness, actomyosin tension shape 3D form  |
|                                                                  |
|  TIMELINE: Week 4 = rudiments form; Week 5-8 = morphogenesis;   |
|            Week 8 = embryo→fetus; Week 9-40 = growth+maturation |
+──────────────────────────────────────────────────────────────────+
```

---

## Engineering Bridge: Organogenesis as Protocol Handshakes and Recursive Algorithms

Two of the most universal concepts in organogenesis — reciprocal induction and branching morphogenesis — map directly onto distributed protocols and recursive algorithms.

```
  ORGANOGENESIS                 CS / ENGINEERING PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Reciprocal induction          Two-way handshake protocol:
  (ureteric bud ↔ metanephric   Each side waits for the other's signal
  mesenchyme)                   before committing and proceeding.
    UB → GDNF receptor (RET)    1. Mesenchyme secretes GDNF
    Mesenchyme → FGF signals    2. UB binds GDNF → branches (ACK)
    → UB branches (ACK)         3. UB secretes FGF, WNT → mesenchyme
    → Mesenchyme condenses (ACK)   condenses (ACK)
                                If either signal is absent → both sides
                                abort (renal agenesis). Classic 3-way
                                handshake with mutual dependency.

  Branching morphogenesis       Recursive tree construction:
  (lung: ~23 generations)       Base case: airway sac (alveolus).
  FGF10 at tip → grow;          Recursive case: tip cell receives FGF10
  BMP4 at tip → inhibit         → branches into two daughter buds.
  adjacent; stalk stable        Termination condition: FGF10 decreases
                                below threshold (BMP4 inhibition) → stop.
                                The 23-generation binary tree of airways
                                is built from this 3-rule L-system.

  Digit formation by apoptosis  Sculpting by selective deletion:
  (interdigital web removal)    Not: grow fingers separately. Instead:
                                grow a solid limb paddle, then delete the
                                web between digits via BMP-induced apoptosis.
                                This is rendering by subtraction — like
                                sculpting from a block by removing material,
                                not by additive construction.

  Morphogen gradient → organ    Spatial lookup table → module assignment:
  size control (organ stopping  Growth terminates when cells sense they
  at correct size)              have filled their positional domain.
                                Hippo pathway: cell density → YAP/TAZ
                                nuclear exit → growth arrest. Mechanical
                                sensing of organ boundary.
  ──────────────────────────────────────────────────────────────────────
```

---

## Heart Development

```
HEART: FIRST ORGAN TO FUNCTION (Week 4)
─────────────────────────────────────────
  Origin: Lateral plate mesoderm (splanchnic layer) — two sources:
    First Heart Field (FHF): left ventricle, atria, part of right ventricle
    Second Heart Field (SHF): right ventricle, outflow tract, great vessels

  TIMELINE
  Day 18-19: Cardiac crescent forms (horseshoe-shaped cardiac progenitors)
  Day 19-20: Cardiac progenitors migrate to midline → linear heart tube
  Day 20-22: Heart tube beats (FIRST CARDIAC CONTRACTIONS)
  Day 22-28: Heart looping: tube loops RIGHT (rightward = d-loop = normal)
             Left-right asymmetry from Nodal signaling (Module 02)
  Week 4-7:  Septation: atrial + ventricular septa form
             Four chambers + outflow tract separation

  SEPTATION MECHANISMS
  ─────────────────────
  ATRIAL SEPTUM:
    Septum primum grows down → foramen primum (closes)
    Fenestrations in septum primum → foramen secundum (stays open)
    Septum secundum grows alongside → leaves foramen ovale (fetal shunt)
    At birth: ↑left atrial pressure → closes foramen ovale

  VENTRICULAR SEPTUM:
    Muscular septum grows up from apex
    Membranous septum closes last (neural crest contribution)
    VSD (ventricular septal defect): most common CHD; often membranous

  ENDOCARDIAL CUSHIONS:
    Form atrioventricular (AV) valves and outflow tract valves
    Neural crest cells critical for conotruncal septation

  CONGENITAL HEART DISEASE MECHANISMS
  - TGA (transposition): Outflow tract doesn't spiral correctly → aorta/PA reversed
  - Tetralogy of Fallot: VSD + pulmonary stenosis + RV hypertrophy + overriding aorta
  - DiGeorge syndrome: 22q11 deletion → neural crest → conotruncal defects
```

---

## Lung Development

```
LUNG DEVELOPMENT STAGES
──────────────────────────
  Origin: Respiratory diverticulum from ventral foregut endoderm (Week 4)
  Signaling: FGF10 from mesenchyme → FGFR2b on endoderm → branching

  STAGE               TIMING      KEY EVENTS
  ──────────────────  ──────────  ──────────────────────────────────────
  Embryonic           Week 4-7    Respiratory diverticulum branches 1-4×
                                  Primary bronchi, lobar bronchi, segmental
  Pseudoglandular     Week 7-16   Conducting airways form; gland-like appearance
                                  No alveoli yet; not viable
  Canalicular         Week 16-26  Air sacs canalize; capillary invasion
                                  Gas exchange becomes possible at ~22-24 weeks
  Saccular            Week 26-36  Terminal sacs multiply; surfactant production begins
  Alveolar            Week 36-   True alveoli form; most alveolar development
                      2-3 yr     occurs AFTER birth

  SURFACTANT (Module relevant to neonatal medicine)
  Type II pneumocytes produce surfactant (dipalmitoyl-phosphatidylcholine, DPPC).
  Onset: ~Week 22-24; adequate levels: ~Week 34-36.
  Function: Reduce alveolar surface tension → prevent alveolar collapse.
  Deficiency → Respiratory Distress Syndrome (RDS) in premature infants.
  Treatment: Maternal betamethasone (induces surfactant) + postnatal surfactant therapy.

BRANCHING MORPHOGENESIS (lungs)
  FGF10 from mesenchyme → tip of endodermal bud
  BMP4 in tip → Sprouty inhibitor → restrains FGF response
  Net: FGF10 drives tip extension; BMP4 limits branching
  Result: stereotyped branching tree → ~23 generations of airways
  Mouse lungs: 3D light-sheet imaging shows completely stereotyped branching
  Human lungs: similar program with minor variations
```

---

## Kidney Development

```
KIDNEY: THREE SUCCESSIVE KIDNEY FORMS
────────────────────────────────────────
  Three kidney structures form sequentially in humans:

  PRONEPHROS (Week 4): Rudimentary; involutes; functional in fish/frogs.
  MESONEPHROS (Week 4-8): Transient kidney of the embryo. Contributes to
    male genital ducts (Wolffian/mesonephric duct → vas deferens, epididymis).
    Regresses in females.
  METANEPHROS (Week 5 → permanent kidney):
    Ureteric bud from Wolffian duct + metanephric mesenchyme.
    Reciprocal inductive interaction is the classic case study.

URETERIC BUD ↔ METANEPHRIC MESENCHYME INDUCTION
  ─────────────────────────────────────────────────
  Metanephric mesenchyme secretes GDNF (Glial cell-derived neurotrophic factor)
  → GDNF binds RET receptor on Wolffian duct epithelium
  → Ureteric bud branches out toward mesenchyme.

  Ureteric bud secretes WNT9b + FGF
  → WNT9b activates β-catenin in mesenchyme
  → Mesenchyme-to-epithelium transition (MET)
  → Mesenchymal cells condense → form renal vesicle → nephron epithelium

  NEPHRON NUMBER
  Each branching event of ureteric bud can induce new nephrons from surrounding mesenchyme.
  Humans: ~800,000 to 1,000,000 nephrons/kidney.
  Determined by the branching period + mesenchyme availability.
  Low nephron number (born premature, poor maternal nutrition) → CKD risk in adulthood.

KIDNEY DEFECTS
  Renal agenesis: GDNF or RET mutation → no ureteric bud outgrowth → no kidney.
  Bilateral renal agenesis → Potter sequence (oligohydramnios → limb compression,
    pulmonary hypoplasia) → lethal.
  Horseshoe kidney: Lower poles fuse across midline during ascent.
    Migration arrested at inferior mesenteric artery.
    Usually asymptomatic but higher risk of ureteropelvic junction obstruction.
  Polycystic kidney disease (ADPKD): PKD1/PKD2 (polycystins in primary cilia)
    → cyst formation; progressive.
```

---

## Limb Development

```
LIMB BUD FORMATION AND PATTERNING
────────────────────────────────────
  Lateral plate mesoderm + surface ectoderm → limb bud (Week 4)
  Position: determined by Hox gene expression in lateral plate mesoderm

  THREE ORGANIZING REGIONS:

  1. APICAL ECTODERMAL RIDGE (AER)
     Thickened epithelium at distal tip of limb bud.
     Secretes FGF4, FGF8 → maintains progress zone (rapidly dividing mesenchyme)
     AER-removal experiment: proximal limb forms, distal limb truncated.
     AER = required for distal outgrowth.

  2. ZONE OF POLARIZING ACTIVITY (ZPA)
     Posterior mesenchyme of limb bud.
     Secretes Shh → anterior-posterior positional identity.
     High Shh (posterior) → digit 4/5 (little finger)
     Low Shh (anterior) → digit 1 (thumb)
     ZPA transplant → mirror image limb (already discussed in HOX module).

  3. DORSAL ECTODERM
     Wnt7a from dorsal ectoderm → LMX1B in dorsal mesenchyme → dorsal fate (back of hand)
     BMP from ventral ectoderm → Engrailed-1 → ventral fate (palm)
     Dorsal-ventral axis = Wnt7a gradient.

DIGIT SEPARATION: APOPTOSIS
  Interdigital mesenchyme: programmed apoptosis removes tissue between digits.
  Signals: BMP2/4/7 → Caspase-3 activation → death of interdigital mesenchyme.
  BMP inhibition (Noggin) → syndactyly (fused digits).
  Programmed death is required for normal digit separation.

  WEBBED FINGERS (syndactyly): Failure of interdigital apoptosis.
  Extra fingers (polydactyly): ZPA or SHH gain-of-function.
  Thalidomide: disrupts limb bud FGF signaling Week 4-8 → phocomelia.
```

---

## Pancreas Development

```
PANCREAS: ENDOCRINE + EXOCRINE FROM FOREGUT
──────────────────────────────────────────────
  Two buds from foregut endoderm (Week 4-5):
    Dorsal bud: body and tail → most islets + acinar cells
    Ventral bud: head of pancreas → fuses with dorsal bud (Week 7)
    Annular pancreas: ventral bud wraps around duodenum → obstruction.

  MASTER TRANSCRIPTION FACTORS
  Pdx1 (IPF1): marks all pancreatic progenitors (dorsal + ventral bud).
    Pdx1-/- mouse: no pancreas.
    Pdx1 haploinsufficiency in humans: MODY4 (maturity-onset diabetes of young).
  Ptf1a: required for exocrine (acinar) fate.
    Ptf1a-/- mouse: no exocrine pancreas; islets form but mislocated.
  Ngn3 (Neurogenin3): endocrine progenitor marker.
    Ngn3+ cells → all islet cell types (α, β, δ, ε, PP cells).
    Ngn3-/- mouse: no endocrine cells → diabetic.

  ENDOCRINE CELL FATE SPECIFICATION
  Beta cells: Pdx1 + Nkx6.1 + Nkx2.2 → insulin+
  Alpha cells: Arx + Pax6 → glucagon+
  Delta cells: Sst → somatostatin+
  Notch off → Ngn3 → endocrine fate
  Notch on → keep acinar/ductal progenitor state

  CLINICAL RELEVANCE: iPSC TO BETA CELLS
  Successful protocol (Pagliuca et al. 2014; Rezania et al. 2014):
    iPSC → definitive endoderm → posterior foregut → pancreatic progenitors
    → endocrine progenitors → beta cells
    Uses: ActivinA/Wnt (endoderm) → FGF10/RA/SB431542 (pancreatic bud)
    → Noggin/EGF/Nicotinamide (endocrine induction) → many more steps
    Result: "SC-beta cells" that can glucose-respond and rescue diabetes in mice.
    Clinical: Vertex's VX-880 / VX-264 clinical trials — encapsulated SC-beta cells.
```

---

## Tooth Development: Classic EMT Induction

```
TOOTH DEVELOPMENT: EPITHELIAL-MESENCHYMAL INDUCTION
──────────────────────────────────────────────────────
Why here: Tooth development is the canonical multi-stage induction example,
with ~20 reciprocal signaling events between oral epithelium and neural
crest-derived mesenchyme. Each stage uses a different signaling pathway.

STAGES (human: Week 6 through childhood)
  1. INITIATION (dental placode):
     BMP4 from mesenchyme + FGF8 from epithelium → thickening of oral epithelium
     Where placode forms: determined by Runx2 expression boundary

  2. BUD STAGE:
     Placode invaginates into underlying mesenchyme.
     Mesenchyme condenses around epithelial bud (like kidney reciprocal induction).
     Wnt pathway specifies number of teeth (Wnt gain → extra teeth;
     loss → tooth agenesis)

  3. CAP STAGE:
     Inner enamel epithelium (IEE) forms → becomes enamel-forming cells (ameloblasts)
     Mesenchyme → dental papilla → dentin-forming cells (odontoblasts)
     Enamel knot forms: signaling center (FGF, BMP, Wnt) that defines cusp number/position
     Enamel knot cells undergo apoptosis after use — consumed signal center

  4. BELL STAGE:
     Cytodifferentiation: ameloblasts vs odontoblasts
     Reciprocal induction: odontoblasts begin dentin → signals ameloblasts to form enamel
     Ameloblasts produce enamel (hardest substance in body: 96% HAP crystal)
     Odontoblasts produce dentin (70% mineral; collagen scaffold)

  5. ROOT FORMATION:
     Hertwig's epithelial root sheath (HERS) shapes root form
     Cementoblasts (neural crest origin) form cementum → anchors to periodontal ligament

DENTAL STEM CELLS AND CLINICAL IMPLICATIONS
  Dental pulp stem cells (DPSCs): can differentiate into odontoblasts, neural cells,
  adipocytes. Potential for bioengineered tooth replacement.
  Stem cells from apical papilla (SCAP): progenitors for root formation.
  Periodontal ligament stem cells (PDLSCs): for attachment apparatus regeneration.

  Congenital tooth anomalies:
    Hypodontia: tooth agenesis (PAX9, MSX1, AXIN2 mutations)
    Supernumerary teeth: excess Wnt signaling
    Amelogenesis imperfecta: enamel defect (AMELX, ENAM mutations)
    Dentinogenesis imperfecta: dentin defect (DSPP mutation)
```

---

## Eye Development: Classic Induction Example

```
EYE DEVELOPMENT: THE TEXTBOOK INDUCTION
──────────────────────────────────────────
  OPTIC VESICLE INDUCTION (Spemann 1901, before organizer work)
  Neural tube evaginates → optic vesicle contacts surface ectoderm.
  Optic vesicle secretes signals (FGF, BMP) → induces lens placode in ectoderm.
  Lens placode invaginates → lens vesicle.
  Simultaneously: optic vesicle invaginates → optic cup (double-walled).
    Outer layer → retinal pigment epithelium (RPE)
    Inner layer → neural retina

  KEY TFs:
  Pax6: Master eye specification gene.
    "Eyeless" in Drosophila = Pax6 equivalent.
    Pax6 ectopic expression → ectopic eye anywhere (fly legs, wings).
    Aniridia (human): PAX6 heterozygous → iris absence, corneal disease.

  WNT9b, FGF signals from optic vesicle → lens placode induction.
  Without optic vesicle contact: no lens forms.
  The induced lens then sends signals BACK to influence retina patterning.
  Reciprocal induction.

  CLINICAL: Organoids
  Retinal organoids: differentiated from iPSCs using sequential Wnt/BMP/FGF signals.
  Reproduce early eye layers; used for disease modeling (Stargardt, RP) and drug screening.
  Cerebral organoids have spontaneously formed optic cup-like structures (Lancaster 2022).
```

---

## Decision Cheat Sheet

| Organ | Germ Layer Origin | Master Regulator | Key Inductive Signal |
|-------|-----------------|-----------------|---------------------|
| Heart | Lateral plate mesoderm | Nkx2.5, GATA4 | BMP2/4 from pharyngeal endoderm |
| Lungs | Foregut endoderm (surface) + splanchnic mesoderm | Nkx2.1/TTF-1 | FGF10 from mesenchyme |
| Kidney | Intermediate mesoderm (mesenchyme + ureteric bud) | Six2, WT1 | GDNF → RET + Wnt9b |
| Liver | Foregut endoderm | Foxa2, HNF4α | FGF1/2 from cardiac mesoderm |
| Pancreas | Foregut endoderm | Pdx1, Ptf1a, Ngn3 | Notch repression → Ngn3 |
| Limb | Lateral plate + surface ectoderm | Tbx4/5 (leg/arm identity) | FGF10/Wnt2b (bud initiation) |
| Eye | Surface ectoderm (lens) + diencephalon (retina) | Pax6 | Optic vesicle FGF/BMP |

---

## Common Confusion Points

**"Organs form during weeks 4-8 — doesn't that mean damage before week 4 is safe?"**
No — before Week 4, gastrulation and axis specification are occurring. Damage here (teratogens, thalidomide) affects the overall body plan. Weeks 4-8 are the sensitive period for specific organ formation. After Week 8 (fetal period), organs are present but still growing — teratogens still cause damage to specific developing systems. The nervous system is particularly vulnerable throughout fetal life.

**"The ureteric bud ↔ mesenchyme interaction is described as 'reciprocal induction' — what makes it reciprocal?"**
Each tissue requires the other: ureteric bud won't branch without GDNF from mesenchyme; mesenchyme won't undergo MET without Wnt9b from the bud. Remove either: development fails. This mutual dependency is reciprocal induction. In contrast, lens placode induction by optic vesicle is more unidirectional (optic vesicle induces lens, though there is some feedback).

**"Branching morphogenesis produces stereotyped trees — how does the tree know when to stop branching?"**
Termination mechanisms include: FGF/BMP competition (each branch inhibits neighbors via BMP), exhaustion of mesenchymal FGF10, epithelial stiffening, and positional signals that limit the branching domain. In lungs, the 23-generation program is encoded in the initial branching geometry. In the kidney, the mesenchyme becomes exhausted. These are active stop signals, not just passive cessation.
