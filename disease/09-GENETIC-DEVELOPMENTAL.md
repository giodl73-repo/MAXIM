# 09 — Genetic & Developmental Disease

## Chromosomal Abnormalities, Inheritance Patterns, Single-Gene Disorders, Birth Defects

---

## Big Picture: Genetic Disease Taxonomy

```
┌──────────────────────────────────────────────────────────────────────────┐
│               GENETIC DISEASE CLASSIFICATION                             │
├─────────────────────┬────────────────────────────────────────────────────┤
│ CHROMOSOMAL         │ Numerical: aneuploidy (trisomy/monosomy/polyploidy)│
│ (karyotype visible) │ Structural: deletion, duplication, translocation,  │
│                     │   inversion, ring chromosome, isochromosome        │
├─────────────────────┼────────────────────────────────────────────────────┤
│ SINGLE GENE         │ Autosomal dominant (AD)                            │
│ (Mendelian)         │ Autosomal recessive (AR)                           │
│                     │ X-linked recessive (XLR)                           │
│                     │ X-linked dominant (XLD)                            │
│                     │ Y-linked (holandric)                               │
├─────────────────────┼────────────────────────────────────────────────────┤
│ EPIGENETIC /        │ Genomic imprinting (Prader-Willi, Angelman)        │
│ NON-MENDELIAN       │ Mitochondrial (maternal inheritance, heteroplasmy) │
│                     │ Triplet repeat expansion (anticipation)            │
│                     │ Uniparental disomy (UPD)                           │
├─────────────────────┼────────────────────────────────────────────────────┤
│ MULTIFACTORIAL /    │ Polygenic + environment: T2DM, CAD, schizophrenia, │
│ COMPLEX             │   cleft lip, NTDs, congenital heart defects        │
├─────────────────────┼────────────────────────────────────────────────────┤
│ SOMATIC / ACQUIRED  │ Mosaicism, cancer (see 04-CANCER.md)               │
└─────────────────────┴────────────────────────────────────────────────────┘

Scale of defect: chromosome → region → gene → codon → trinucleotide repeat
Diagnostic tools: karyotype → chromosomal microarray → gene panel → WES/WGS
```

---

<!-- @editor[bridge/P2]: No old-world bridge -- genetic disease taxonomy (chromosomal -> single gene -> epigenetic -> multifactorial -> somatic) maps to defect granularity (platform failure -> module failure -> configuration error -> multi-factor degradation -> runtime corruption) -->

## 1. Chromosomal Disorders — Numerical

### Meiotic Non-Disjunction Mechanics

```
Normal meiosis:
   Meiosis I: homologous chromosomes separate
   Meiosis II: sister chromatids separate
   Result: haploid gametes (n=23)

Non-disjunction at Meiosis I:
   Both homologs → same cell → one gamete has 2 copies, one has 0
   Results in ALL cells affected after fertilization

Non-disjunction at Meiosis II:
   Sister chromatids → same cell → same outcome
   More likely to result in viable products (e.g., trisomy 21)

Trisomy = 2n + 1 = 47 chromosomes
Monosomy = 2n − 1 = 45 chromosomes
```

### Key Trisomies

| Trisomy | Name | Incidence | Key Features | Survival |
|---------|------|-----------|--------------|----------|
| 21 | Down syndrome | 1/700 | Intellectual disability, flat facies, hypotonia, simian crease, endocardial cushion defects (AV canal), duodenal atresia, early Alzheimer's (3× APP), ↑ leukemia risk | Adulthood common; ~60 yr median |
| 18 | Edwards syndrome | 1/5000 | IUGR, clenched fists (overlapping fingers), rocker-bottom feet, VSD, choroid plexus cysts, omphalocele | 50% die <1 week; rare >1 yr |
| 13 | Patau syndrome | 1/10,000 | HPE (holoprosencephaly — midline fusion failure), midline facial defects (cyclopia→cleft), polydactyly, microcephaly, CNS malformations | 80% die <1 month |

**Maternal age effect:** Non-disjunction ↑ dramatically with age (oocytes arrested in prophase I for decades → ↑ cohesin degradation → premature chromosome separation). Trisomy 21 rate at 20 yrs = 1/1500; at 45 yrs = 1/30.

**Down syndrome genetic mechanisms:**
```
Full trisomy 21 (94%): standard non-disjunction
Robertsonian translocation (5%): chr 21 fused to chr 14 (or 13/15)
   Carrier parent: 46 chromosomes (balanced) but 21 attached to 14
   Offspring risk: 33% theoretical; ~10–15% actual (meiotic selection)
   Important: NO maternal age effect — check parent karyotype
Mosaic (1%): post-fertilization non-disjunction; milder phenotype
```

### Sex Chromosome Aneuploidies

| Karyotype | Name | Features |
|-----------|------|---------|
| 45,X | Turner syndrome | Webbed neck, lymphedema, shield chest, coarctation of aorta, streak gonads (primary amenorrhea), short stature, normal IQ (often) |
| 47,XXY | Klinefelter syndrome | Tall, small testes, ↓ testosterone, gynecomastia, infertility, ↑ risk autoimmune; often diagnosed at fertility workup |
| 47,XYY | Jacob syndrome | Tall, usually normal fertility; behavioral issues debated (historical bias in data) |
| 47,XXX | Triple X | Usually normal; mild language delay; fertility often intact |

**Turner mosaic (45,X/46,XX):** Milder phenotype; critical period is intrauterine (lymphedema at birth = cystic hygroma).

---

## 2. Chromosomal Disorders — Structural

```
Deletion: loss of chromosomal segment
   ─────────────────────────
   Cri-du-chat: del(5p) — cat-like cry, microcephaly, ID
   DiGeorge/22q11.2: del(22q11.2) — conotruncal heart defects, hypocalcemia
     (parathyroid aplasia), T-cell deficiency (thymic aplasia), cleft palate;
     CATCH-22: Cardiac, Abnormal facies, Thymic aplasia, Cleft palate, Hypocalcemia

Duplication: extra copy of a region
   ─────────────────────────────
   Charcot-Marie-Tooth 1A: dup(17p12) — peripheral neuropathy

Translocation:
   Reciprocal: exchange between non-homologs; balanced carrier = normal phenotype
   Robertsonian: centromere fusion of acrocentric chromosomes (13,14,15,21,22)
     ─ Balanced carrier: 45 chromosomes, normal phenotype
     ─ Unbalanced offspring: risk of trisomy or monosomy

Inversion:
   Pericentric: includes centromere; may alter gene dosage at breakpoints
   Paracentric: same arm; carrier at risk for recombinant chromosomes

Ring chromosome: telomeres fuse; unstable; variable deletion
Isochromosome: duplication of one arm + deletion of other (e.g., i(17q) in medulloblastoma)
Microdeletion/duplication syndromes: too small for standard karyotype
   → chromosomal microarray (CMA) detects CNVs ≥50 kb
```

---

## 3. Inheritance Patterns

### Pattern Recognition

```
AUTOSOMAL DOMINANT (AD):
  ▪ Every generation affected (vertical pedigree)
  ▪ Affected parent has 50% risk offspring
  ▪ Males = females equally
  ▪ New mutations common in severe lethal cases (achondroplasia ~85% de novo)
  ▪ Variable expressivity, incomplete penetrance possible

AUTOSOMAL RECESSIVE (AR):
  ▪ Often skips generations (carrier parents × carrier parents → 25% affected)
  ▪ More common with consanguinity
  ▪ Males = females equally
  ▪ Carrier frequency = √disease frequency (Hardy-Weinberg)

X-LINKED RECESSIVE (XLR):
  ▪ Affected males >> females (females need 2 copies)
  ▪ No male-to-male transmission (fathers give Y to sons)
  ▪ Carrier mothers: 50% sons affected, 50% daughters carriers
  ▪ Lyon hypothesis: X-inactivation → female carriers can show mild features

X-LINKED DOMINANT (XLD):
  ▪ Heterozygous female affected; hemizygous male often lethal
  ▪ Examples: Rett syndrome (MECP2), incontinentia pigmenti

MITOCHONDRIAL:
  ▪ Maternal inheritance (all mtDNA from oocyte cytoplasm)
  ▪ ALL children of affected mother affected (to varying degree)
  ▪ Father never transmits
  ▪ Heteroplasmy: mixture of normal/mutant mtDNA in cells → variable phenotype

CODOMINANT:
  ▪ Both alleles expressed; heterozygote shows both phenotypes
  ▪ ABO blood groups, HLA, sickle-cell trait (HbAS — some protection, no disease)
```

---

## 4. Autosomal Dominant Diseases

| Disease | Gene | Mechanism | Hallmarks |
|---------|------|-----------|-----------|
| Huntington's | HTT | Toxic gain of function (polyQ) | Chorea, dementia, psychiatric; anticipation |
| Marfan's | FBN1 (fibrillin-1) | Structural ECM; ↑ TGF-β signaling | Arachnodactyly, lens dislocation, aortic root dilation (dissection risk) |
| NF1 | NF1 (neurofibromin, RAS GAP) | Tumor suppressor loss → ↑ RAS | Cafe-au-lait spots (>6), neurofibromas, Lisch nodules, optic glioma |
| NF2 | NF2 (merlin) | Tumor suppressor | Bilateral vestibular schwannomas (NF2 = "2" bilateral "2"nd cranial nerve) |
| ADPKD | PKD1 (85%), PKD2 | Polycystin dysfunction → cyst expansion | Flank pain, hematuria, HTN, renal failure; berry aneurysms (8-10%); hepatic cysts |
| Familial hypercholesterolemia | LDLR (mostly) | ↓ LDL receptor → ↑ plasma LDL | Tendon xanthomas, premature CAD; homozygous → childhood MI |
| Achondroplasia | FGFR3 | Activating mutation → ↓ chondrocyte proliferation | Rhizomelic dwarfism, large head, spinal stenosis; ~85% de novo |
| BRCA1/BRCA2 | BRCA1/2 | Tumor suppressor (HR repair) | AD risk allele; heterozygote: ↑ breast/ovarian/prostate cancer (second hit needed) |

**Variable expressivity vs incomplete penetrance:**
- Variable expressivity: gene expressed but phenotype severity differs (NF1 cafe-au-lait vs glioma)
- Incomplete penetrance: gene present but no phenotype at all; penetrance = fraction of carriers showing phenotype (BRCA1 ~70% lifetime breast cancer risk → 30% penetrance failure)

---

## 5. Autosomal Recessive Diseases

### Cystic Fibrosis

```
CFTR (cystic fibrosis transmembrane conductance regulator)
  Chr 7q31; encodes ATP-gated Cl⁻ channel in epithelial apical membrane
  Most common lethal AR disease in European populations (~1/3200)
  Carrier frequency: ~1/25 in Northern European

ΔF508 mutation (deletion of Phe508, exon 10):
  Class II mutation: protein misfolded → retained in ER → ↑ proteasomal degradation
  Other mutation classes:
    Class I: no protein (nonsense/splice) — e.g., G542X
    Class III: gating defect (CFTR reaches surface but doesn't open) — G551D
    Class IV: decreased conductance
    Class V: reduced production
    Class VI: decreased stability

Pathophysiology:
  Cl⁻ secretion blocked → Na⁺ and water follow → viscous secretions
  Airways: thick mucus → impaired mucociliary clearance → Pseudomonas/Staph colonization → bronchiectasis
  Pancreas: blocked ducts → autodigestion → exocrine insufficiency (malabsorption), diabetes (CFRD)
  Intestine: meconium ileus (15% newborns)
  Reproductive: vas deferens obstruction (CBAVD) → male infertility (99%)

Diagnosis: Newborn screening (IRT) → sweat chloride test >60 mmol/L → CFTR genotyping

CFTR modulators (precision medicine by mutation class):
  Ivacaftor (potentiator): opens gating-defective CFTR (G551D, Class III)
  Lumacaftor/tezacaftor (correctors): ↑ folding/trafficking of ΔF508
  Elexacaftor/tezacaftor/ivacaftor (triple combo = Trikafta): ~90% CF patients
    → FEV1 ↑14%, sweat Cl⁻ normalized — transformative treatment
```

### Sickle Cell Disease

```
HBB gene (β-globin), chr 11p
Glutamate → Valine at position 6 (GAG → GTG)
HbS: α2β2(s); under deoxygenation → polymerizes → "sickling"

Sickling cascade:
  Low O₂ (or acidosis/dehydration/cold/infection)
  → HbS polymerization → rigid rod-like fibers → RBC distortion
  → ↑ membrane fragility → hemolysis (MCHC ↑ in SS disease)
  → ↑ adhesion to endothelium (via VLA-4, ICAM-1) → vaso-occlusion
  → ischemia → inflammation → more sickling (positive feedback)

Clinical manifestations:
  Vaso-occlusive crisis (bone pain — most common reason for ER)
  ACS (acute chest syndrome): new infiltrate + respiratory symptoms → leading cause of death
  Stroke: childhood + adult; TCD screening → hydroxyurea or transfusion
  Splenic sequestration/autosplenectomy → functional asplenia → encapsulated organisms
    (Strep pneumoniae, H. influenzae, N. meningitidis) → vaccinate + prophylactic penicillin
  Dactylitis (hand-foot syndrome): earliest presentation in infants
  Priapism, retinopathy, AVN of femoral head, nephropathy

Treatment:
  Hydroxyurea: ↑ HbF production (γ-globin) → HbF inhibits HbS polymerization
  Voxelotor: allosteric Hb stabilizer → binds oxy form → ↓ polymerization
  Crizanlizumab: anti-P-selectin → ↓ adhesion → ↓ VOC frequency
  Exchange transfusion: ACS/stroke prevention/acute stroke
  Curative: allogeneic HSCT (matched sibling); gene therapy (betibeglogene/exa-cel)
```

### Lysosomal Storage Diseases

```
All AR; enzyme deficiency → substrate accumulates in lysosomes
Glucocerebrosidase deficiency → Gaucher's (substrate: glucocerebroside)
  Type 1 (non-neuronopathic): HSM, bone marrow infiltration, cytopenias — treatable
  Treatment: ERT (imiglucerase) or substrate reduction (eliglustat)

Sphingomyelinase deficiency → Niemann-Pick A/B (sphingomyelin → ceramide)
β-hexosaminidase A deficiency → Tay-Sachs (GM2 ganglioside)
  Ashkenazi Jewish: 1/30 carrier; cherry-red spot on macula, severe ND in infancy
α-galactosidase A → Fabry disease (globotriaosylceramide) — X-linked
  Neuropathic pain (small fiber), angiokeratomas, cardiomyopathy, renal failure
Iduronate-2-sulfatase → Hunter syndrome (MPS II, dermatan/heparan sulfate) — X-linked
α-L-iduronidase → Hurler syndrome (MPS I, dermatan/heparan sulfate) — AR
  Coarse facies, HSM, corneal clouding, developmental regression
```

### Other Key AR Diseases

| Disease | Gene | Defect | Notes |
|---------|------|--------|-------|
| PKU | PAH (phenylalanine hydroxylase) | ↓ Phe→Tyr | Untreated: severe ID; Phe-restricted diet + tetrahydrobiopterin (BH4) |
| Wilson's | ATP7B (copper transporter) | Cu accumulation in liver/brain | KF rings (cornea), liver disease, neuropsychiatric; treat with chelation |
| Hemochromatosis | HFE (C282Y homozygous most common) | ↑ iron absorption | Bronze diabetes (DM + skin pigment + cirrhosis); phlebotomy |
| α1-antitrypsin deficiency | SERPINA1 | Z allele → misfolded, ER retention in liver | Emphysema (↑ elastase in lung) + liver disease (misfolded protein toxicity) |
| PKDH (Autosomal Recessive Polycystic Kidney Disease) | PKHD1 (fibrocystin) | Ductal plate malformation | Presents in infancy/childhood; pulmonary hypoplasia, CHF |

---

## 6. X-Linked Recessive Diseases

| Disease | Gene | Mechanism | Clinical |
|---------|------|-----------|---------|
| DMD (Duchenne MD) | DMD (dystrophin) | Frameshift → no dystrophin | Onset <5yr; Gowers' sign; pseudohypertrophy calves; cardiomyopathy; CK ↑↑↑ |
| BMD (Becker MD) | DMD | In-frame deletion → truncated dystrophin | Later onset, milder |
| Hemophilia A | F8 (factor VIII) | ↓ VIII → impaired intrinsic pathway | Hemarthroses, deep muscle bleeds; prolonged aPTT; treat with FVIII or emicizumab |
| Hemophilia B | F9 (factor IX) | ↓ IX | Same as A; treat with FIX or fitusiran |
| G6PD deficiency | G6PD | ↓ NADPH → ↓ glutathione → oxidative hemolysis | Triggered by fava beans/primaquine/dapsone/nitrofurantoin/infection |
| Fragile X | FMR1 (CGG repeat) | >200 repeats → methylation → gene silencing → ↓ FMRP | Most common inherited ID in males; macroorchidism, autism features, FXTAS (premutation tremor/ataxia) |

**Dystrophin reading frame rule (Monaco rule):**
- Frame-disrupting (out-of-frame) mutation → no protein → Duchenne (severe)
- In-frame deletion → truncated but partially functional protein → Becker (mild)
- Exon-skipping therapy (eteplirsen, viltolarsen): converts out-of-frame to in-frame → converts DMD phenotype toward BMD

---

## 7. Genomic Imprinting

**Concept:** Parent-of-origin-specific gene expression — one allele silenced by methylation (epigenetic). Both alleles present but only one expressed.

```
Chromosome 15q11-q13 imprinted region:
  Paternal chromosome 15: expresses SNRPN + other genes; silences UBE3A
  Maternal chromosome 15: expresses UBE3A; silences SNRPN cluster

Prader-Willi Syndrome (PWS): loss of PATERNAL 15q11-q13
  ├── Deletion 15q11 (paternal): 70%
  ├── Maternal UPD 15 (both chr 15 from mother): 25%
  └── Imprinting center mutation: 5%
  Features: hypotonia + feeding difficulty (infant) → hyperphagia + obesity (child)
           hypogonadism, short stature (↓ GH), behavioral issues, ID

Angelman Syndrome (AS): loss of MATERNAL 15q11-q13 (UBE3A)
  ├── Deletion 15q11 (maternal): 70%
  ├── Paternal UPD 15: 5%
  ├── Imprinting center mutation: 3%
  └── UBE3A mutation: 11%
  Features: severe ID, absent speech, happy affect, seizures, ataxic gait
            "Happy puppet" syndrome

Memory trick: Paternal → PWS (Prader-Willi); mAternal → Angelman
```

**Beckwith-Wiedemann Syndrome (BWS):** Chr 11p15 imprinting; ↑ IGF-2 (paternal)/↓ CDKN1C → overgrowth, macroglossia, omphalocele, hypoglycemia, Wilms tumor risk.

---

## 8. Mitochondrial Diseases

**Mitochondrial genetics:**
```
mtDNA: 16,569 bp circular; 37 genes (13 OXPHOS subunits, 22 tRNAs, 2 rRNAs)
37 gene products + ~1500 nuclear-encoded proteins make up the mitochondrial proteome
Maternal inheritance: sperm mitochondria degraded after fertilization
Heteroplasmy: cells contain mix of normal + mutant mtDNA
  High mutation load (>70-90%) → disease threshold (varies by tissue/energy demand)
  Stochastic sorting at cell division → variable phenotype within family
```

**Key diseases:**
| Disease | Mutation | Features |
|---------|---------|---------|
| MELAS | m.3243A>G (MT-TL1, tRNA-Leu) | Mitochondrial Encephalomyopathy, Lactic Acidosis, Stroke-like episodes |
| MERRF | m.8344A>G (MT-TK, tRNA-Lys) | Myoclonic Epilepsy with Ragged Red Fibers |
| Leber's Hereditary Optic Neuropathy (LHON) | ND4/ND1/ND6 mutations (CI) | Bilateral painless optic atrophy, young males; maternal but male predominance (nuclear modifiers) |
| Kearns-Sayre Syndrome | Large deletion | Ophthalmoplegia, pigmentary retinopathy, heart block (requires pacemaker) |

**Ragged red fibers:** Gomori trichrome stain; mitochondria accumulate under sarcolemma → red fiber edge. Pathognomonic for mitochondrial myopathy.

---

## 9. Triplet Repeat Expansion Disorders

```
Normal gene: (CTG)ₙ or (CAG)ₙ or (CGG)ₙ — stable short repeat
Premutation: moderately expanded — may manifest some phenotype (premutation carrier)
Full mutation: large expansion → gene silenced or toxic protein

ANTICIPATION: repeat expands on transmission → earlier/more severe disease next generation
  Especially paternal transmission in HD, polyQ diseases
  Especially maternal transmission in myotonic dystrophy (DM1)
```

| Disease | Gene | Repeat | Normal | Full mutation | Mechanism |
|---------|------|--------|--------|---------------|-----------|
| Huntington's | HTT | CAG | <26 | ≥40 | Toxic polyQ gain-of-function |
| Fragile X | FMR1 | CGG | <45 | >200 | Gene methylation/silencing (loss of FMRP) |
| Myotonic Dystrophy 1 | DMPK | CTG | <37 | >50 | RNA gain-of-function (toxic CUG hairpins sequester MBNL splicing factor) |
| Friedreich's Ataxia | FXN (frataxin) | GAA (intron 1) | <33 | >100 | Heterochromatin silencing → ↓ frataxin → ↓ Fe-S clusters → mitochondrial Fe toxicity |
| SBMA (Kennedy) | AR | CAG | <36 | >38 | Toxic polyQ androgen receptor (motor neuron + sensory) |

---

## 10. Developmental Birth Defects

### Neural Tube Defects (NTDs)

```
Neural tube closure: days 22–28 post-fertilization
  Anterior neuropore closes day 25 → failure → anencephaly (lethal)
  Posterior neuropore closes day 27 → failure → spina bifida

Spina bifida spectrum:
  Spina bifida occulta: bony defect, meninges/cord intact; hair tuft/dimple
  Meningocele: meninges herniate; cord intact; good prognosis
  Myelomeningocele: cord + roots exposed → paralysis, bladder/bowel, Chiari II
    (cerebellar herniation through foramen magnum → hindbrain dysfunction)

SHH (sonic hedgehog) signaling: dorsoventral patterning of neural tube
  Loss → holoprosencephaly (HPE) — failure of forebrain division; trisomy 13

Folic acid:
  400 μg/day preconception → prevents 50–70% NTDs
  Mechanism: 1-carbon metabolism (MTHFR pathway); folate for nucleotide synthesis
  MTHFR C677T polymorphism (↓ folate metabolism) → ↑ risk
  Folate fortification of flour in US (1998) → 28% reduction in NTD rate
```

### Cardiac Malformations

**Most common congenital anomaly (1% of live births):**
```
Transcription factors:
  NKX2.5: atrial septation, AV node
  GATA4: atrial/ventricular septation
  TBX1 (22q11 deletion): conotruncal outflow tract

Cyanotic CHD (right-to-left shunt → unoxygenated blood in systemic circulation):
  Tetralogy of Fallot (ToF): RVOT obstruction + VSD + overriding aorta + RVH
    "Tet spell" → squatting (↑ SVR → reverses shunt)
  Transposition of great arteries (TGA): aorta from RV, PA from LV → parallel circuits
    Incompatible with life unless mixing (ASD/PDA/VSD); prostaglandin E1 (keep PDA open)
  Truncus arteriosus, TAPVR, tricuspid atresia

Acyanotic CHD (left-to-right shunt → ↑ pulmonary flow):
  VSD (most common CHD overall)
  ASD: often silent; fixed split S2
  PDA: continuous "machinery" murmur; indomethacin to close (premature infants)
  Coarctation of aorta: HTN in arms, weak femoral pulses, rib notching
    Turner syndrome association; bicuspid aortic valve (BAV) in 50–80%

Eisenmenger physiology: chronic L→R shunt → pulmonary HTN → shunt reversal → cyanosis
```

### Teratogens — Mechanism and Windows

```
Teratogen: agent causing structural malformation in developing embryo
Critical period: organogenesis weeks 3–8; most susceptible
After 8 weeks: growth + function affected, not gross morphology
```

| Teratogen | Mechanism | Effects | Sensitive Period |
|-----------|-----------|---------|------------------|
| Thalidomide | Inhibits cereblon (↓ VEGF, ↓ FGF) → limb bud vascularity | Phocomelia (flipper limbs), ear/eye defects, cardiac | Weeks 4–8 |
| Isotretinoin (Accutane) | Retinoic acid excess → disrupts RA signaling | CNS, craniofacial, heart defects; iPLEDGE program | Weeks 4–7+ |
| Alcohol (FASD) | Oxidative stress, folate antagonism, epigenetic | FAS: facial dysmorphia (smooth philtrum, thin lip, small palpebral fissures) + CNS + IUGR; spectrum → pAE (no dysmorphia but CNS) | All trimesters (CNS all, facial wks 7–10) |
| Rubella (virus) | Direct cytopathic; endothelial damage | Cataracts, deafness, cardiac (PDA), blueberry muffin | First trimester (weeks 1–8 worst) |
| Toxoplasma | Direct tissue destruction | Chorioretinitis, hydrocephalus, intracranial calcifications (periventricular) | 2nd-3rd trimester (worse if early) |
| CMV | Cytopathic | Sensorineural hearing loss (most common prenatal cause), periventricular calcifications, microcephaly | All trimesters |
| Valproate | HDAC inhibition → epigenetic; folate antagonism | Neural tube, craniofacial, cognitive | Weeks 3–5 (NTD), all (cognitive) |
| ACE inhibitors | ↓ fetal renal perfusion → ↓ urine → oligohydramnios | Renal tubular dysgenesis, skull hypoplasia, limb contractures | 2nd-3rd trimester |
| Warfarin | Inhibits γ-carboxylation of Gla proteins including matrix Gla protein | Chondrodysplasia punctata (stippled epiphyses), nasal hypoplasia | Weeks 6–12 |

---

## 11. Newborn Screening

**Wilson-Jungner criteria for screening:** Disease important, recognizable, treatable, test sensitive/specific, economical.

**Tandem mass spectrometry (MS/MS):** Single dried blood spot → detects >50 inborn errors simultaneously.

**Core US panel (RUSP — Recommended Uniform Screening Panel): 35 core conditions**

| Condition | Metabolite detected | Untreated consequence | Treatment |
|-----------|--------------------|-----------------------|-----------|
| PKU | ↑ Phenylalanine | Severe intellectual disability | Phe-restricted diet ± sapropterin (BH4) |
| Congenital hypothyroidism | ↑ TSH (↓ T4) | Cretinism (irreversible if late) | Levothyroxine (must start <2 weeks) |
| CAH (21-OH deficiency) | ↑ 17-OHP | Salt-wasting crisis, ambiguous genitalia | Hydrocortisone (± fludrocortisone) |
| Galactosemia | ↑ galactose-1-P uridyltransferase | Liver failure, sepsis (E. coli), cataracts | Galactose-free diet |
| MSUD | ↑ Leu/Ile/Val (branched chain) | Encephalopathy, maple syrup odor | BCAA-restricted diet ± thiamine |
| SCID | ↓ TREC (T-cell receptor excision circles) | Life-threatening infections | HSCT (curative) |
| SMA | SMN1 copy number | Progressive motor neuron loss | Nusinersen/onasemnogene (gene therapy) |
| SCD | Hb HPLC fractionation | Vaso-occlusion, stroke | Penicillin prophylaxis, hydroxyurea, vaccinations |

**Critical timing:** Hypothyroidism, MSUD, PKU, galactosemia, CAH — treatment within days prevents irreversible harm. SMA gene therapy best <6 months.

---

## Decision Cheat Sheet

| Pattern | Key Features | Example Diseases |
|---------|-------------|-----------------|
| AD | Every generation; 50% risk; variable expressivity | HD, Marfan, NF1, ADPKD, achondroplasia |
| AR | Carrier parents; 25% affected; consanguinity ↑ | CF, PKU, sickle cell, Tay-Sachs, Gaucher |
| XLR | Males affected; no male-to-male; carrier mothers | DMD, hemophilia A/B, G6PD, fragile X |
| Mitochondrial | Maternal only; heteroplasmy; all children affected (variable) | MELAS, MERRF, LHON, KSS |
| Imprinting | Parent-of-origin matters; same locus, different parent | PWS (paternal loss 15q11), AS (maternal loss 15q11) |
| Trinucleotide | Anticipation; premutation → full mutation | HD (CAG), fragile X (CGG), DM1 (CTG), Friedreich's (GAA) |
| Chromosomal | Non-disjunction; ↑ maternal age for trisomies | Trisomy 21/18/13, Turner (45X), Klinefelter (XXY) |

---

## Common Confusion Points

**Turner vs Klinefelter:** Turner = 45X (female; short stature, coarctation, streak gonads). Klinefelter = 47XXY (male; tall, infertility, gynecomastia). Both have ↓ sex hormone production but opposite sex.

**PWS vs Angelman — same region, opposite parent:**
"P for Paternal = PWS" (lose the paternal 15 → lose SNRPN → PWS).
"A for Angelman, mAternal" (lose maternal 15 → lose UBE3A → AS).
Angelman: happy, seizures, no speech. PWS: hyperphagia, obese, short.

**Down syndrome Robertsonian translocation:** Karyotype = 46 chromosomes (not 47) but 3 copies of chr 21 material. Check parent karyotype — if balanced 14;21 carrier, recurrence risk is ~10-15%, NOT maternal-age-dependent.

**DMD exon skipping:** Out-of-frame deletion → Duchenne (severe). Therapeutic exon skip → restore reading frame → converts to Becker-like. Eteplirsen skips exon 51 → applicable to ~13% of DMD mutations.

**CF mutations and modulator eligibility:**
- G551D → ivacaftor alone (potentiator only)
- ΔF508/ΔF508 → elexacaftor/tezacaftor/ivacaftor (triple)
- Nonsense (Class I, no protein) → modulators don't work; ataluren (readthrough) for some

**Folic acid timing:** Must be taken BEFORE conception to prevent NTDs — tube closes day 25-28, often before pregnancy is confirmed. "Pop it before you plan it."

**Teratogen exposure timing:**
- All-or-nothing period: weeks 1–2 (before implantation; either miscarriage or normal)
- Organogenesis (weeks 3–8): STRUCTURAL defects
- Fetal period (weeks 9+): Growth/functional defects (CNS still vulnerable all trimesters)
