# Autoimmune and Inflammatory Disease

## The Big Picture: Self-Tolerance Failure

```
AUTOIMMUNE DISEASE: adaptive immune response against self-antigens

MECHANISMS OF TOLERANCE FAILURE:
┌──────────────────────────────────────────────────────────────────┐
│  MOLECULAR MIMICRY                                               │
│  Pathogen antigen similar to self-antigen → cross-reactive T/B  │
│  cells initially activated against pathogen persist vs self      │
│  Examples: GAS M protein → cardiac tissue (rheumatic fever)     │
│            Campylobacter gangliosides → nerve gangliosides (GBS)│
├──────────────────────────────────────────────────────────────────┤
│  BYSTANDER ACTIVATION                                            │
│  Inflammation damages local tissue → releases self-antigens     │
│  normally sequestered → presented to autoreactive T cells        │
│  that escaped negative selection                                 │
├──────────────────────────────────────────────────────────────────┤
│  EPITOPE SPREADING                                               │
│  Initial response to one self-antigen → tissue damage → new     │
│  antigens released → response broadens to additional epitopes   │
│  → explains why autoimmune diseases progress over time           │
├──────────────────────────────────────────────────────────────────┤
│  LOSS OF REGULATORY T CELLS (Treg)                               │
│  FoxP3 mutations → IPEX syndrome (immune dysregulation,          │
│  polyendocrinopathy, enteropathy, X-linked)                      │
│  Treg suppression of autoreactive T cells fails                  │
├──────────────────────────────────────────────────────────────────┤
│  DEFECTIVE APOPTOSIS                                             │
│  Fas/FasL deficiency → ALPS (autoimmune lymphoproliferative)     │
│  Accumulation of self-reactive lymphocytes                       │
└──────────────────────────────────────────────────────────────────┘
```

### HLA Associations (Key Board of Governors-level relationships)

| HLA Allele | Associated Disease | Mechanism |
|------------|-------------------|-----------|
| HLA-B27 | Ankylosing spondylitis, Reactive arthritis, Psoriatic arthritis, IBD-associated arthropathy | Arthritogenic peptide theory / aberrant protein folding |
| HLA-DR4 | Rheumatoid arthritis (shared epitope in DRB1 position 70-74) | Citrullinated peptide presentation |
| HLA-DR3/DQ2 | SLE, Sjögren's, T1DM (DR3+DR4), celiac (DQ2) | High-affinity autoantigen presentation |
| HLA-DR2 | SLE, Multiple sclerosis, Goodpasture | Autoreactive T cell selection |
| HLA-DQ2/DQ8 | Celiac disease (> 99% carry DQ2 or DQ8) | Gliadin peptide presentation (DQ2 prefers negatively charged) |
| HLA-DRB1*04 | Pemphigus vulgaris | Desmoglein peptide presentation |

HLA is necessary but not sufficient: identical twin concordance typically 25-50% → non-HLA genetic + environmental factors required.

---

<!-- @editor[bridge/P2]: No old-world bridge -- autoimmune disease as type system failure (self/non-self discrimination breaking down); molecular mimicry is literally a hash collision between pathogen and self-antigen -->

## Rheumatoid Arthritis (RA)

```
PATHOGENESIS:
  Trigger: smoking, infections → protein citrullination in lung/joint
  Citrullinated proteins (cyclic citrullinated peptides = CCPs): collagen, fibronectin, vimentin
  Anti-CCP antibodies (ACPA): highly specific for RA (95% specific) and appear YEARS before symptoms
  Rheumatoid factor (RF): IgM anti-IgG Fc — 70-80% sensitivity, low specificity (10% of normal population)

  Joint pathology:
    CD4+ Th1/Th17 cells: IFN-γ + IL-17 → activate synovial fibroblasts + macrophages
    TNF-α (macrophage main source) + IL-1β + IL-6: key cytokines → synovial inflammation
    Pannus formation: aggressive fibroblast-like synoviocyte (FLS) + macrophage layer invades cartilage + bone
    RANKL ↑ (from T cells + FLS): activates osteoclasts → erosion of juxta-articular bone
    "Marginal erosions" on X-ray: pathognomonic for RA

CLINICAL:
  Symmetric polyarthritis: MCP, PIP (not DIP), wrist, MTP (proximal joints)
  Morning stiffness > 1 hour (inflammatory — contrast OA which is brief)
  Extra-articular: pulmonary (ILD, pleuritis, nodules), cardiovascular (↑ CVD risk), ocular (scleritis)
  Felty's syndrome: RA + splenomegaly + neutropenia (severe, long-standing RA)
  Caplan syndrome: RA + pneumoconiosis → multiple lung nodules

TREATMENT:
  Early aggressive: MTX (methotrexate) — cornerstone, anti-folate + other mechanisms; hepatotoxicity + teratogenic
  + HCQ (hydroxychloroquine): antimalarial, blocks TLR signaling in endosomes
  + SSZ (sulfasalazine)
  Inadequate response → Biologics:
    TNF inhibitors: etanercept (soluble TNF-R), infliximab/adalimumab/certolizumab/golimumab (anti-TNF mAbs)
    IL-6R inhibitor: tocilizumab, sarilumab
    CD80/86 blocker (co-stimulation): abatacept (CTLA-4-Ig)
    B cell depletion: rituximab (anti-CD20)
  JAK inhibitors (small molecule, oral): tofacitinib, baricitinib, upadacitinib
    Block JAK1/JAK3 → disrupt IFN, IL-6, IL-17 signaling; ↑ risk VTE + malignancy (boxed warning)
```

---

## Systemic Lupus Erythematosus (SLE)

```
PATHOGENESIS:
  DEFECTIVE CLEARANCE OF APOPTOTIC DEBRIS:
    DNase I deficiency → apoptotic cell DNA not cleared → NETs (neutrophil extracellular traps) persist
    C1q, C4, CR2 deficiencies → impaired phagocytosis of apoptotic material
    Self-DNA/RNA exposed → activates TLR7 (ssRNA) + TLR9 (CpG DNA) → innate activation
    → Type I interferons (IFN-α/β) from plasmacytoid DCs → "interferon signature" (elevated in 60-80% of SLE)
    → autoreactive B cells not eliminated → autoantibodies to nuclear antigens

AUTOANTIBODIES:
  Anti-dsDNA: highly specific for SLE (~70% sensitivity, >95% specificity); correlates with disease activity/nephritis
  Anti-Sm (Smith): highly specific (25-30% sensitivity, ~99% specific — pathognomonic if present)
  ANA (antinuclear antibody): > 97% sensitive (screening test); not specific (positive in many conditions)
  Anti-Ro/SSA + anti-La/SSB: Sjögren's overlap; neonatal lupus (heart block from placental transfer)
  Anti-histone: drug-induced lupus (procainamide, hydralazine, TNF inhibitors)
  Antiphospholipid antibodies: anticardiolipin, anti-β2-GP1, lupus anticoagulant → antiphospholipid syndrome

CLINICAL (SLICC 2012 criteria — 11 clinical + 6 immunological):
  Butterfly (malar) rash: over cheeks + nasal bridge, sparing nasolabial folds (photosensitive)
  Discoid rash: scarring photosensitive plaques
  Photosensitivity, oral ulcers, non-scarring alopecia
  Serositis: pleuritis, pericarditis
  Lupus nephritis: most serious manifestation — WHO Class I-VI; Class III/IV (proliferative) → most aggressive
  Neuropsychiatric: psychosis, cognitive dysfunction, seizures, CNS vasculitis
  Hematologic: hemolytic anemia, thrombocytopenia, leukopenia

COMPLEMENT CONSUMPTION:
  SLE activates classical complement (immune complexes → C1q) → ↓ C3, ↓ C4
  Low complement + ↑ anti-dsDNA + ↑ urinary protein → active nephritis flare

TREATMENT:
  All SLE: HCQ (hydroxychloroquine) — reduces flares + mortality; antithrombotic
  Mild-moderate: NSAIDs, low-dose steroids, MMF, azathioprine
  Severe (nephritis, CNS): high-dose steroids + MMF or cyclophosphamide (IV pulse)
  Biologics: belimumab (anti-BLyS/BAFF — B cell survival factor); voclosporin + MMF for nephritis
  Avoid sun, monitor blood counts + renal function + anti-dsDNA/complement
```

---

## Multiple Sclerosis (MS)

```
PATHOGENESIS:
  CNS-specific autoimmune demyelination
  CD4+ Th1 + Th17 cells: autoreactive against myelin antigens (MBP, MOG, PLP)
  Cross BBB → activate microglia + macrophages → demyelinating plaques
  Oligodendrocyte damage → axonal loss (permanent deficit accumulates)
  Astrogliosis → sclerotic plaques (hence "sclerosis")

LESION CHARACTERISTICS:
  Periventricular white matter (80% in periventricular zones — Dawson's fingers)
  Optic nerve, brainstem, spinal cord, cerebellum
  MRI: T2/FLAIR hyperintensities; Gd-enhancing = active inflammation (breakdown of BBB)
  Old inactive lesions: T1 "black holes" = axonal loss

CLINICAL TYPES:
  RRMS (Relapsing-Remitting, 85%): discrete attacks → full or partial recovery; inflammation-driven
  SPMS (Secondary Progressive): RRMS eventually transitions; neurodegeneration accumulates
  PPMS (Primary Progressive, 15%): steady accumulation from onset; older, male, spinal cord
  Clinically Isolated Syndrome (CIS): first demyelinating event; risk of conversion to RRMS if MRI lesions

CSF:
  Oligoclonal IgG bands: distinct bands in CSF not in serum (90-95% of MS patients)
  ↑ IgG index (intrathecal Ig synthesis)
  Mild lymphocytosis possible

DISEASE-MODIFYING THERAPIES (DMTs) — efficacy vs risk stratification:
  Moderate efficacy (first-line): IFN-β (↑ T-reg, ↓ T cell trafficking), glatiramer acetate, dimethyl fumarate
  High efficacy: natalizumab (anti-VLA-4 — blocks T cell entry into CNS), fingolimod (S1P receptor modulator — traps lymphocytes in lymph nodes), alemtuzumab (anti-CD52, T + B cell depletion), ocrelizumab (anti-CD20, B cell depletion)
  PPMS: ocrelizumab (only approved for PPMS)
  Key risk: PML (progressive multifocal leukoencephalopathy) with natalizumab (JCV reactivation); requires JCV Ab testing
```

---

## Inflammatory Bowel Disease (IBD)

### Crohn's vs Ulcerative Colitis

```
FEATURE           CROHN'S DISEASE (CD)         ULCERATIVE COLITIS (UC)
Location          Anywhere GI (mouth-anus)     Colon only (rectum always involved)
                  Terminal ileum + ileocecum   Continuous from rectum proximally
                  most common
Extent            Skip lesions (normal +        Continuous mucosal involvement
                  abnormal alternating)
Depth             TRANSMURAL (all layers)       MUCOSAL only
Histology         Non-caseating GRANULOMAS     Crypt abscesses, goblet cell depletion
                  (pathognomonic for CD)        NO granulomas
Symptoms          RLQ pain, diarrhea (may be   Bloody diarrhea, urgency, tenesmus
                  non-bloody), weight loss
Anal disease      Fistulae, perianal abscess,  Rare
                  tags (30-50%)
Strictures        Common → obstruction         Less common
Cancer risk       ↑ (SB + colon)              ↑↑ (especially pancolitis > 8 years)
Smoking           Worsens disease              May be protective (paradoxical — ↓ disease)
Surgery           NOT curative (can recur)     CURATIVE (total proctocolectomy)
ANCA/ASCA        ASCA (+) in ~60-70%         p-ANCA (+) in ~60-70%
```

### IBD Pathogenesis

```
MICROBIOME DYSBIOSIS + EPITHELIAL BARRIER FAILURE:
  NOD2 mutations (Crohn's): ↓ innate bacterial sensing → impaired Paneth cell function
    → inadequate antimicrobial peptide production → dysbiosis → bacterial translocation
  Epithelial tight junction dysfunction (UC): genetic variants in E-cadherin, claudins
    → mucosal permeability → luminal antigen exposure

IMMUNE ACTIVATION:
  Crohn's: Th1 (IFN-γ) + Th17 (IL-17, IL-23) pathway dominant
  UC: Th2-like (IL-5, IL-13) + innate
  Both: TNF-α central mediator

IBD TREATMENT LADDER:
  5-ASA (mesalamine): topical anti-inflammatory for mild UC (no benefit in CD)
  Corticosteroids: induction (not maintenance — long-term toxicity)
  Immunomodulators: azathioprine/6-MP (TPMT testing), MTX
  Biologics:
    Anti-TNF: infliximab, adalimumab, certolizumab (CD), golimumab (UC)
    Anti-IL-12/23: ustekinumab (both CD + UC)
    Anti-IL-23: risankizumab (CD), mirikizumab (UC)
    Anti-integrin (gut-selective): vedolizumab (blocks α4β7 → gut lymphocyte trafficking)
  JAK inhibitors: tofacitinib, upadacitinib (UC)
```

---

## Psoriasis

```
PATHOGENESIS:
  Th17 → IL-17A (+ IL-22): drives keratinocyte hyperproliferation
  IL-23 (from DCs, macrophages) → Th17 differentiation + survival
  KC-DC-T cell feedback loop → chronic inflammation
  Epidermal turnover: ~4 days (vs 28 days normal)
  → Parakeratosis (nuclei retained in stratum corneum), acanthosis, tortuous vessels in papillary dermis

CLINICAL:
  Plaque psoriasis (most common, 90%): well-demarcated erythematous plaques + silvery-white scale
    Auspitz sign: pinpoint bleeding on scale removal (exposed dermal papillae)
    Koebner phenomenon: new lesions at sites of trauma
  Psoriatic arthritis (PsA): ~30% of psoriasis patients — asymmetric oligoarthritis or DIP involvement
    "Pencil-in-cup" deformity on X-ray; HLA-B27 association (axial disease)
  Guttate: small droplet lesions, triggered by Strep pharyngitis (molecular mimicry)
  Pustular / erythrodermic: severe systemic variants

TREATMENT:
  Topical: corticosteroids, vitamin D analogs (calcipotriene), coal tar, retinoids
  Phototherapy: narrowband UVB — standard for moderate disease
  Systemic: MTX, acitretin, cyclosporine
  Biologics: target the IL-23/IL-17 axis (most effective for skin):
    Anti-TNF: etanercept, adalimumab, infliximab (↓ use for skin alone now)
    Anti-IL-17: secukinumab, ixekizumab, bimekizumab (IL-17A/F)
    Anti-IL-23: guselkumab, risankizumab, tildrakizumab (p19 subunit)
    Anti-IL-12/23: ustekinumab (p40 subunit, both)
  IL-17 inhibitors: most effective for skin (90+ PASI90 response rates)
```

---

## Ankylosing Spondylitis (AS)

```
PROTOTYPE HLA-B27 DISEASE:
  94% of AS patients are HLA-B27+ (but only 5% of HLA-B27+ develop AS)

PATHOGENESIS THEORIES:
  Arthritogenic peptide: HLA-B27 presents bacterial peptide cross-reactive with self (Chlamydia, Klebsiella)
  HLA-B27 misfolding: abnormal folding → ER stress → UPR → IL-23 production → Th17
  Free heavy chain hypothesis: HLA-B27 dimers at cell surface → activate NK/T cells

CLINICAL:
  Sacroiliitis: inflammatory buttock pain + morning stiffness relieved by exercise (not rest)
  Gradual spinal fusion: syndesmophytes → "bamboo spine" on X-ray
  Enthesitis: inflammation at tendon/ligament insertion points (Achilles, plantar fascia, rib attachments)
  Extra-articular: anterior uveitis (25-40%), aortitis, inflammatory bowel
  Modified New York Criteria: bilateral grade ≥ 2 or unilateral grade ≥ 3 sacroiliitis on X-ray + clinical criteria

IMAGING:
  X-ray: late (syndesmophytes, bamboo spine)
  MRI STIR/fat-sat: early (bone marrow edema at SI joints)

TREATMENT:
  NSAIDs: first-line (remarkable efficacy + possibly disease-modifying)
  Biologics (if inadequate NSAID response):
    Anti-TNF: first approved (etanercept, adalimumab, infliximab, certolizumab, golimumab)
    Anti-IL-17: secukinumab, ixekizumab (equal to anti-TNF; no IL-17 benefit in IBD-associated AS)
    Anti-IL-23: not effective for axial AS (paradoxically effective in PsA and IBD-associated)
```

---

## Celiac Disease

```
MECHANISM:
  Dietary gliadin (α, ω fractions of gluten from wheat/barley/rye)
  Tissue transglutaminase 2 (tTG2): deamidates gliadin → negatively charged peptides
  HLA-DQ2 (most common) / DQ8: present deamidated gliadin to CD4+ T cells
  → Th1 + Th2 activation → mucosal inflammation + autoantibody production
  → Villous atrophy + crypt hyperplasia → malabsorption

SEROLOGY:
  Anti-tTG2 IgA (most sensitive + specific; check total IgA — 2-3% of celiac have IgA deficiency → false negative)
  Anti-endomysial IgA: highly specific
  Anti-deamidated gliadin peptide IgG/IgA: useful when IgA-deficient

CLINICAL:
  Classical (GI): diarrhea, steatorrhea, abdominal bloating, weight loss
  Non-classical: atypical (constipation, iron deficiency anemia, ↑ liver enzymes, short stature, infertility, peripheral neuropathy)
  Dermatitis herpetiformis: intensely pruritic papulovesicular rash on extensor surfaces; gluten-sensitive
  Refractory celiac disease: no response to gluten-free diet → risk of enteropathy-associated T-cell lymphoma (EATL)

COMPLICATIONS: ↑ risk of GI cancers (EATL, small bowel adenocarcinoma)

DIAGNOSIS: serology + duodenal biopsy (gold standard: Marsh grade 3 = subtotal/total villous atrophy)
TREATMENT: strict lifelong gluten-free diet (only treatment; no medication as effective)
```

---

## Sjögren's Syndrome

```
PATHOGENESIS:
  Autoimmune exocrine gland destruction (salivary + lacrimal glands primarily)
  CD4+ T cells + B cells infiltrate gland acini → lymphocytic sialadenitis
  Anti-Ro/SSA + anti-La/SSB antibodies: found in 50-70%
  Can be primary (alone) or secondary (with RA, SLE, systemic sclerosis)

CLINICAL:
  Sicca symptoms: keratoconjunctivitis sicca (dry eyes: gritty, burning) + xerostomia (dry mouth: dysphagia, dental caries)
  Parotid enlargement
  Extraglandular: skin (annular erythema), joint (arthralgia), pulmonary (ILD), renal (tubular acidosis — distal RTA type 1), peripheral neuropathy, vasculitis
  Lymphoma risk: 44× ↑ (MALT lymphoma of salivary glands or diffuse large B cell)

DIAGNOSIS: European League Against Rheumatism/ACR criteria 2016; lip biopsy (minor salivary gland) — focal lymphocytic sialadenitis (focus score ≥ 1/4mm²)
TREATMENT: artificial tears/saliva; pilocarpine (M3 agonist → gland stimulation); hydroxychloroquine; rituximab for systemic disease
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| RA: RF+ or anti-CCP+, which is more specific? | Anti-CCP: ~95% specific (vs ~80% for RF). Anti-CCP appears years before symptoms — can help diagnose early and predict erosive disease. |
| SLE kidney: why check complement + anti-dsDNA? | Active nephritis typically shows low C3/C4 (consumed by immune complex activation) + rising anti-dsDNA. Useful for monitoring without repeat biopsy. |
| MS relapse treatment vs DMT: different goals | Relapse (acute attack): IV methylprednisolone → speeds recovery but doesn't change long-term outcome. DMTs: prevent future relapses and slow disability accumulation (no effect on acute relapse). |
| Crohn's vs UC: who gets surgery as cure? | Only UC total proctocolectomy is curative. Crohn's can recur at any GI site; surgery reserved for complications (obstruction, fistula, refractory disease). |
| Anti-TNF: which condition is it dangerous in? | Active TB (reactivation risk), active infections, CHF (moderate-severe), demyelinating disease, prior lymphoma. Screen with PPD/IGRA + CXR before starting. |
| HLA-B27: how does it cause joint inflammation? | Multiple theories (arthritogenic peptide, ER stress, free heavy chain); no single consensus. Present in ~8% of white population but only ~5% of B27+ develop AS. |

---

## Common Confusion Points

**Primary vs secondary Sjögren's**
Primary: stands alone. Secondary: overlaps with RA, SLE, systemic sclerosis, etc. Same antibody profile (anti-Ro/La) but secondary is far more common than primary when sicca symptoms appear in context of established connective tissue disease.

**Biologics: why different targets for different IBD subtypes?**
Anti-IL-17 works for AS, psoriasis, PsA — but can WORSEN Crohn's. IL-17 suppression in gut impairs mucosal barrier → paradoxically worse IBD. Anti-IL-23 (p19-specific) works in CD + UC but not axial AS. Biology drives targeted therapy differences.

**SLE anticoagulation (antiphospholipid syndrome)**
APL antibodies (anticardiolipin, anti-β2GP1, lupus anticoagulant) → THROMBOSIS (arterial and venous) despite the name "anticoagulant" (lupus anticoagulant prolongs PTT in vitro but causes clotting in vivo). Triple positive APL (all three markers) → highest risk. Treatment: long-term anticoagulation with warfarin (DOACs controversial in triple-positive APS).

**Reactive arthritis (formerly Reiter's syndrome) vs RA vs AS**
Reactive: post-infectious (Chlamydia, GI pathogens: Salmonella, Shigella, Yersinia, Campylobacter) → HLA-B27 associated → asymmetric oligoarthritis. Classic triad: arthritis + urethritis + conjunctivitis ("can't see, can't pee, can't climb a tree"). Self-limited usually. Not the same as RA or AS.
