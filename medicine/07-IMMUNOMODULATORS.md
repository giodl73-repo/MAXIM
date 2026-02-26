# 07 — Immunomodulators

## Biologics (mAbs/Fusion Proteins), Transplant Immunosuppression, JAK Inhibitors, IVIG, Complement

---

<!-- @editor[bridge/P2]: No CS bridge -- immune system is distributed autonomous agent network with self/non-self classification (type system), tolerance (allowlisting), autoimmunity (false positive); immunosuppression is access control policy modification -->

## Big Picture: Immunomodulation Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                  IMMUNOMODULATOR TARGETS                                 │
├────────────────────────┬─────────────────────────────────────────────────┤
│ TRANSPLANT             │ Calcineurin inhibitors (↓ IL-2)                 │
│ IMMUNOSUPPRESSION      │ mTOR inhibitors (↓ T-cell proliferation)        │
│                        │ Mycophenolate (↓ purine synthesis in lymphocytes)│
│                        │ Steroids (broad anti-inflammatory)               │
│                        │ Induction agents (anti-thymocyte globulin)       │
├────────────────────────┼─────────────────────────────────────────────────┤
│ TNF-α BLOCKADE         │ Infliximab, adalimumab, certolizumab (mAb/Fab)   │
│                        │ Etanercept (TNFR2-Fc fusion protein)             │
├────────────────────────┼─────────────────────────────────────────────────┤
│ IL-6 BLOCKADE          │ Tocilizumab, sarilumab (anti-IL-6R)             │
│                        │ Siltuximab (anti-IL-6 ligand)                   │
├────────────────────────┼─────────────────────────────────────────────────┤
│ IL-17/IL-23            │ Secukinumab, ixekizumab (anti-IL-17A)           │
│                        │ Guselkumab, risankizumab, ustekinumab (anti-IL-23)│
├────────────────────────┼─────────────────────────────────────────────────┤
│ IL-4/13, IgE, IL-5     │ Dupilumab, omalizumab, mepolizumab             │
├────────────────────────┼─────────────────────────────────────────────────┤
│ T-CELL COSTIMULATION   │ Abatacept (CTLA-4-Fc → ↓ CD28 activation)      │
│ / B-CELL DEPLETION     │ Rituximab, ocrelizumab (anti-CD20)              │
│                        │ Belimumab (anti-BAFF → ↓ B-cell survival)       │
├────────────────────────┼─────────────────────────────────────────────────┤
│ JAK PATHWAY            │ JAK1/2/3 inhibitors (tofacitinib, baricitinib)  │
│ (INTRACELLULAR)        │ JAK1-selective (upadacitinib, filgotinib)        │
├────────────────────────┼─────────────────────────────────────────────────┤
│ POOLED IMMUNOGLOBULIN  │ IVIG (pooled IgG) — immunodeficiency + autoimmune│
├────────────────────────┼─────────────────────────────────────────────────┤
│ COMPLEMENT             │ Eculizumab, ravulizumab (anti-C5)               │
│                        │ Avacopan (C5aR1 antagonist)                     │
└────────────────────────┴─────────────────────────────────────────────────┘
```

---

## 1. Transplant Immunosuppression

### Overview: Induction → Maintenance → Rejection Treatment

```
INDUCTION (peritransplant — high immunologic risk period):
  Anti-thymocyte globulin (ATG): rabbit (thymoglobulin) or equine (ATGAM)
    Polyclonal antibody against T-cell surface antigens → T-cell depletion
    Binds many antigens including CD2, CD3, CD4, CD8, CD11a, CD16, CD25, CD28, CD45
    → Profound T-cell depletion + functional inhibition
  Basiliximab (Simulect): chimeric anti-CD25 (IL-2 receptor α-chain) mAb
    ↓ IL-2 signaling → ↓ T-cell expansion; less myelosuppression than ATG; no serum sickness

MAINTENANCE (long-term triple therapy standard):
  Calcineurin inhibitor (CNI): tacrolimus (preferred) or cyclosporine
  Antimetabolite: mycophenolate mofetil (MMF) or azathioprine
  Corticosteroid: prednisone (often tapered/withdrawn after 1 year in low-risk patients)

REJECTION TREATMENT:
  Acute cellular rejection (T-cell mediated): high-dose IV methylprednisolone ("pulse steroids")
    If steroid-resistant: ATG
  Antibody-mediated rejection (AMR): IVIG + rituximab + plasmapheresis ± complement inhibitors
```

### Calcineurin Inhibitors (CNIs)

```
TACROLIMUS (FK506):
  Binds FKBP12 (FK506-binding protein) → complex inhibits calcineurin (serine/threonine phosphatase)
  Calcineurin normally dephosphorylates NFAT (nuclear factor of activated T cells)
  → NFAT enters nucleus → drives IL-2 transcription → T-cell proliferation
  CNI blockade → NFAT stays phosphorylated → stays in cytoplasm → ↓ IL-2 → ↓ T-cell activation/proliferation

  vs. Cyclosporine: same target (calcineurin), different binding protein (cyclophilin for CsA)
    Tacrolimus: 100× more potent; better rejection prevention; more nephrotoxicity/CNS toxicity/DM
    Cyclosporine: ↑ gingival hyperplasia, ↑ hirsutism; less diabetogenic

TACROLIMUS PK:
  Narrow TI; CYP3A4 + P-gp substrate → major drug interactions
  CYP3A4 inhibitors (azoles, macrolides, diltiazem, grapefruit) → ↑ tacrolimus → nephrotoxicity
  CYP3A4 inducers (rifampin, St. John's wort, phenytoin) → ↓ tacrolimus → rejection
  Target trough levels: early (8–12 ng/mL) → maintenance (4–8 ng/mL); whole blood, HPLC

TACROLIMUS TOXICITY:
  Nephrotoxicity: dose-dependent afferent arteriolar vasoconstriction → ↓ GFR
    Acute: functional (reversible with dose reduction); chronic: structural (interstitial fibrosis)
  Neurotoxicity: tremors (fine; common), headache, insomnia; severe (PRES, seizures, leukoencephalopathy)
  New-onset diabetes after transplant (NODAT): tacrolimus inhibits insulin secretion (FK506 in β-cells)
  HTN; hyperkalemia (↓ aldosterone effect on K secretion)

CNI-SPARING STRATEGIES: important because CNI is primary cause of long-term graft loss (nephrotoxicity)
  Minimize CNI dose; use MMF/mTOR inhibitors to allow lower CNI; belatacept (co-stimulation blockade)
```

### mTOR Inhibitors

**Sirolimus (rapamycin), everolimus:**
- Bind FKBP12 (same as tacrolimus) → FKBP12-sirolimus complex inhibits mTORC1
- mTORC1 inhibition → ↓ p70S6K + ↓ 4E-BP1 → ↓ protein synthesis → ↓ T-cell proliferation
- Also ↓ B-cell function, ↓ smooth muscle proliferation (prevents restenosis → drug-eluting stents)
- **Antiproliferative without nephrotoxicity** (distinct mechanism from CNI) → often used to spare CNI
- **Adverse:** Dyslipidemia (↑ cholesterol + TG), impaired wound healing (avoid early post-transplant), pneumonitis (interstitial), oral ulcers, lymphocele, myelosuppression
- Everolimus + CNI: allow reduction in CNI dose; used in kidney, liver, heart transplant

### Mycophenolate (MMF/EC-MPS)

**Mechanism:** MMF hydrolyzed to mycophenolic acid (MPA) → inhibits IMPDH (inosine monophosphate dehydrogenase), rate-limiting enzyme in de novo guanosine synthesis.

```
Purine synthesis:
  De novo: IMPDH → guanosine (T and B cells LACK salvage pathway for purines → must use de novo)
  Salvage: hypoxanthine + HGPRT → IMP → GMP (most other cells can use this backup)
  → MPA is LYMPHOCYTE-SELECTIVE (T and B cells are uniquely dependent on de novo pathway)

Effect: ↓ lymphocyte proliferation → ↓ rejection + ↓ autoimmune
```

**Adverse:** GI (diarrhea, nausea, cramping — most common side effect; dose-limiting), leukopenia, anemia, teratogenic.

**Drug interactions:** Magnesium/aluminum antacids, cholestyramine → ↓ MMF absorption; tacrolimus may ↑ MPA levels.

---

## 2. TNF-α Inhibitors

### Biology of TNF-α

```
TNF-α: pro-inflammatory cytokine; produced by macrophages, T cells, mast cells
  Binds TNFR1 (ubiquitous, apoptosis + NF-κB) and TNFR2 (mainly immune cells, survival)
  Downstream: NF-κB → ↑ inflammatory gene transcription (IL-1, IL-6, IL-8, COX-2, iNOS, VCAM-1)
  Role in: RA (joint destruction), IBD (mucosal inflammation), psoriasis, AS, reactive arthritis

TNF-α INHIBITORS block TNFR binding → ↓ downstream inflammation
```

| Drug | Type | Indications | Notes |
|------|------|-------------|-------|
| Infliximab (Remicade) | Chimeric mAb (IgG1) | RA, IBD (Crohn's/UC), psoriasis, AS, PsA | IV infusion; mouse-derived variable region → immunogenicity; anti-drug antibodies (ADA) → loss of response |
| Adalimumab (Humira) | Fully human mAb (IgG1) | Same + JIA, uveitis, HS | SC biweekly; first fully human anti-TNF; most prescribed biologic (until biosimilars) |
| Etanercept (Enbrel) | TNFR2-Fc fusion protein | RA, psoriasis, AS, JIA | SC twice weekly; NOT approved for IBD (paradoxical IBD exacerbation); decoy receptor mechanism |
| Certolizumab pegol (Cimzia) | PEGylated Fab' fragment | RA, IBD, PsA, AS | No Fc → no ADCC, no complement; ↓ placental transfer → safest in pregnancy among TNF-i |
| Golimumab (Simponi) | Fully human mAb | RA, AS, PsA, UC | Monthly SC or IV (Simponi Aria) |

**Class adverse effects:**
- **Infection:** ↑ bacterial, fungal (especially granulomatous), and viral infections
- **TB reactivation:** ↑ 5–25× risk vs general population → **mandatory TB screening before starting** (TST or IGRA; if latent TB → treat with INH × 9 months before starting TNF-i)
- Opportunistic infections: histoplasmosis, coccidioidomycosis, listeriosis, aspergillosis
- **Demyelinating disease:** MS worsening or new-onset → contraindicated in MS
- CHF exacerbation (TNFR on cardiomyocytes; infliximab 10mg/kg → ↑ mortality in HF) → avoid in NYHA III-IV
- Hepatitis B reactivation: screen HBsAg, anti-HBc before treatment → if HBsAg+: treat HBV prophylactically
- Lupus-like syndrome (drug-induced lupus): infliximab + adalimumab; anti-dsDNA antibodies
- Malignancy: theoretically ↑ lymphoma; real-world data: uncertain (confounded by underlying disease)
- **Live vaccines contraindicated during TNF-i therapy**

---

## 3. IL-6 Inhibitors

**Tocilizumab (Actemra):** Humanized anti-IL-6R mAb (IgG1); blocks IL-6 signaling (IL-6 is the primary driver of CRP synthesis → tocilizumab dramatically ↓ CRP → may mask fever/infection signs).

**Sarilumab (Kevzara):** Similar mechanism; SC.

**Indications:** RA, GCA (giant cell arteritis), sJIA/pJIA, CAR-T-related CRS (blocks IL-6-mediated cytokine storm), COVID-19 severe (RECOVERY trial: tocilizumab + dexamethasone → ↓ mortality).

**Key adverse effects:** ↑ LDL (IL-6 normally ↑ LDL catabolism), hepatotoxicity (transaminase ↑), GI perforation (↑ risk if IBD/diverticulitis history), neutropenia, ↑ infections.

**IL-6 ligand inhibitor:** Siltuximab (Sylvant) — anti-IL-6 mAb (not receptor); idiopathic multicentric Castleman disease.

---

## 4. IL-17 and IL-23 Inhibitors

### Th17 Pathway in Autoimmunity

```
IL-23 (from DCs/macrophages) → IL-23R on Th17 cells → Th17 expansion + stability
IL-17A/F (from Th17 cells, ILCs) → IL-17RA/RC on keratinocytes/fibroblasts/neutrophils
  → ↑ G-CSF → neutrophil recruitment, ↑ IL-6/IL-8/CXCL1/DEFB4 → skin/joint inflammation

Key in: psoriasis (plaque), psoriatic arthritis, ankylosing spondylitis
NOT effective in IBD (IL-17 inhibition → ↑ IBD paradoxically → contraindicated in Crohn's)
```

**IL-17A inhibitors:**
- Secukinumab (Cosentyx): fully human anti-IL-17A; psoriasis, PsA, AS, nr-axSpA; SC monthly after loading
- Ixekizumab (Taltz): humanized anti-IL-17A; similar indications; faster loading dose schedule
- Bimekizumab: anti-IL-17A + IL-17F; approved psoriasis; possibly more complete blockade

**IL-23 p19 inhibitors (selective IL-23 blockade — leave IL-12 intact):**
- Guselkumab (Tremfya): psoriasis, PsA
- Risankizumab (Skyrizi): psoriasis, PsA, Crohn's disease
- Tildralizumab, mirikizumab (Omvoh): UC (Crohn's for risankizumab)

**IL-12/23 p40 inhibitor (blocks both IL-12 and IL-23):**
- Ustekinumab (Stelara): psoriasis, PsA, Crohn's, UC; older agent; lower infection risk (preserves IL-12 → some Th1)

---

## 5. Other Biologic Targets

### Type 2 Inflammation

**Dupilumab (Dupixent):** Fully human anti-IL-4Rα mAb → blocks both IL-4 and IL-13 signaling (shared receptor subunit).

Indications: atopic dermatitis (moderate-severe), asthma (eosinophilic/type-2), CRSwNP (chronic rhinosinusitis with nasal polyps), eosinophilic esophagitis, prurigo nodularis.

Adverse: conjunctivitis (common in AD patients), injection site reactions; low infection risk (type 2 inflammation ≠ host defense).

**Omalizumab (Xolair):** Anti-IgE (IgE Fc region) → ↓ free IgE → ↓ IgE binding to FcεRI on mast cells/basophils → ↓ mast cell sensitization → ↓ allergic response. Dosing: by IgE level + body weight. Indications: moderate-severe persistent allergic asthma, chronic idiopathic urticaria, food allergy (adjunct). Risk of anaphylaxis — observe 30–60 min post-injection.

**Anti-IL-5 and Anti-IL-5Rα:**
- Mepolizumab (Nucala): anti-IL-5 ligand; eosinophilic asthma, EGPA, HES
- Benralizumab (Fasenra): anti-IL-5Rα; eosinophil depletion via ADCC; eosinophilic asthma
- Reslizumab: anti-IL-5 ligand; IV

**Tezepelumab (Tezspire):** Anti-TSLP (thymic stromal lymphopoietin); upstream of IL-4/5/13 signaling; unselected asthma (not just eosinophilic) — broadest efficacy across phenotypes.

### T-Cell Costimulation Blockade

**Abatacept (Orencia):** CTLA-4-Fc fusion protein → binds CD80/86 on APCs → blocks CD28-B7 co-stimulation → ↓ T-cell activation (requires both TCR + co-stimulation signals for full activation).

Indications: RA, JIA, psoriatic arthritis, lupus nephritis (investigational). Slower onset than TNF-i but good durability. Less infection risk than biologic TNF inhibitors.

Belatacept: CTLA-4-Ig higher affinity version → transplant immunosuppression (alternative to CNI in kidney transplant → avoids nephrotoxicity).

### B-Cell Depletion

**Rituximab (Rituxan):** Chimeric anti-CD20 IgG1; complement-dependent cytotoxicity (CDC) + ADCC + direct apoptosis.
- CD20: expressed on pre-B and mature B cells but not on plasma cells or stem cells
- → B-cell depletion (6–12 months) → ↓ autoantibody production and B-cell antigen presentation

Indications: RA (DMARD-refractory), ANCA vasculitis (GPA/MPA), anti-GBM disease, ITP, autoimmune hemolytic anemia, pemphigus vulgaris, MS (off-label — ocrelizumab preferred), NHL, CLL.

Adverse: infusion reactions (first dose), HBV reactivation, PML (JC virus), hypogammaglobulinemia, delayed neutropenia, rare → pulmonary toxicity.

**Ocrelizumab (Ocrevus):** Humanized anti-CD20 (IgG1); MS (RRMS + PPMS); ↑ ADCC vs rituximab; more complete B-cell depletion; 6-month IV infusion schedule. PML risk (lower than natalizumab but present).

**Belimumab (Benlysta):** Fully human anti-BAFF (B-lymphocyte stimulator/BLyS) mAb → ↓ B-cell survival signal → ↓ autoreactive B-cell survival; SLE (↓ flares, ↓ organ damage); IV or SC.

---

## 6. JAK Inhibitors

### JAK-STAT Signaling

```
Many cytokines (IL-2, IL-4, IL-6, IL-7, IL-12, IL-15, IL-21, IFN-γ, EPO, TPO, G-CSF...)
  → Bind type I/II cytokine receptors (no intrinsic kinase)
  → Receptor-associated JAKs (JAK1, JAK2, JAK3, TYK2) trans-phosphorylate each other
  → STAT proteins recruited + phosphorylated → dimerize → enter nucleus → cytokine-driven gene expression

JAK pairs:
  JAK1/JAK3: γc-chain cytokines (IL-2, IL-4, IL-7, IL-9, IL-15, IL-21)
  JAK1/JAK2: class I cytokines (EPO, GH, IFN-γ)
  JAK1/TYK2: IFN-α/β, IL-10, IL-12, IL-23
  JAK2/JAK2: EPO, TPO, GM-CSF
```

| Drug | JAK Selectivity | Indications | Key Safety Signal |
|------|----------------|-------------|-------------------|
| Tofacitinib (Xeljanz) | JAK1/JAK3 (pan-JAK) | RA, PsA, UC, JIA | VTE/PE (↑ risk vs TNF-i in ORAL Surveillance), MACE, malignancy (FDA boxed warning); herpes zoster |
| Baricitinib (Olumiant) | JAK1/JAK2 | RA, atopic dermatitis, COVID-19 | DVT/PE; herpes zoster; thrombocytosis (JAK2 → ↑ TPO signaling → ↑ platelets transiently) |
| Upadacitinib (Rinvoq) | JAK1-selective | RA, PsA, AS, UC, Crohn's, AD | JAK1-selective → less erythrocytosis (↓ JAK2 effect); herpes zoster; VTE (lesser than pan-JAK) |
| Filgotinib (Jyseleca) | JAK1-selective | RA (EU), UC | Lower spermatogenesis risk concern resolved; herpes zoster |
| Ruxolitinib (Jakafi) | JAK1/JAK2 | Myelofibrosis, PV, GVHD, HSCT, alopecia areata | Anemia/thrombocytopenia (EPO/TPO signaling blocked); abrupt discontinuation → cytokine storm |
| Fedratinib | JAK2-selective | Myelofibrosis | Encephalopathy (Wernicke's — thiamine depletion) → thiamine supplementation required |

**ORAL Surveillance trial (tofacitinib):** FDA required post-marketing safety trial in RA patients ≥50 with ≥1 CV risk factor. Results: tofacitinib ↑ VTE, ↑ MACE, ↑ malignancy vs TNF-i → FDA added boxed warnings to all JAK inhibitors.

**Current position:** JAK inhibitors used when TNF-i fail; some used 1st-line in special scenarios (upadacitinib atopic dermatitis). Avoid in patients with high VTE/CV/malignancy risk.

---

## 7. IVIG (Intravenous Immunoglobulin)

**Composition:** Pooled IgG from >1,000 blood donors → polyvalent IgG (~98% IgG1–4), trace IgM/IgA.

**Mechanisms (multiple, incompletely understood):**
- FcγR saturation on macrophages/NK cells → ↓ autoantibody-mediated cell destruction (ITP, AIHA)
- Anti-idiotypic antibodies → neutralize pathogenic autoantibodies
- ↑ IgG catabolism (FcRn receptor saturation) → ↓ half-life of pathogenic IgG
- Complement neutralization
- ↓ B-cell activation (Fcγ RIIb inhibitory receptor)
- ↑ Treg function
- Anti-viral antibodies (passive immunity in CVID)

**Clinical indications:**
| Indication | Mechanism Being Exploited | Dose |
|-----------|--------------------------|------|
| CVID/primary immunodeficiency | Replacement therapy | 400–600 mg/kg/month |
| ITP | FcγR blockade + anti-idiotypic | 1 g/kg × 2 days |
| GBS | Unknown; anti-idiotypic? | 2 g/kg over 5 days |
| CIDP | Unknown; multiple mechanisms | 2 g/kg over 2–5 days |
| Kawasaki disease | Anti-inflammatory | 2 g/kg single dose + aspirin |
| Multifocal motor neuropathy | Anti-GM1 antibodies (anti-idiotypic?) | 2 g/kg loading |
| Dermatomyositis | Multiple | Induction then monthly |
| Myasthenia gravis crisis | Anti-AChR antibodies (anti-idiotypic?) | 2 g/kg |

**Adverse:** Headache (most common), fever, chills, hypotension (rate-related); anaphylaxis in IgA-deficient patients with anti-IgA antibodies (use IgA-depleted IVIG); thromboembolism (↑ plasma viscosity); hemolysis (ABO blood group antibodies from donors); renal failure (sucrose-stabilized preparations); aseptic meningitis.

---

## 8. Complement Inhibitors

### Complement System Targets

```
C3 ─────────────────────────────► C3a (anaphylatoxin) + C3b (opsonin)
       │
     C5 convertase
       │
       ▼
C5 ─────────────────────────────► C5a (anaphylatoxin, recruits neutrophils) + C5b
                                           │
                                           ▼
                                    C5b-9 (MAC — membrane attack complex) → cell lysis

Eculizumab/ravulizumab: anti-C5 → blocks C5 cleavage → ↓ C5a + MAC
C3 inhibitors (pegcetacoplan): ↑ C3 → blocks at C3 level (broader, covers both C5a and MAC)
C5aR1 antagonist (avacopan): blocks C5a receptor (doesn't prevent MAC, but ↓ neutrophil recruitment)
```

**Eculizumab (Soliris):**
- Humanized anti-C5 mAb; blocks C5 cleavage → ↓ C5a (↓ inflammation) + ↓ C5b-9 (↓ lysis)
- Indications: PNH (paroxysmal nocturnal hemoglobinuria), aHUS (atypical hemolytic uremic syndrome), generalized MG (refractory), neuromyelitis optica spectrum disorder (NMOSD)
- **Critical risk: encapsulated bacteria** (Neisseria meningitidis, Streptococcus pneumoniae, Haemophilus influenzae) — complement blocks them; meningococcal vaccination MANDATORY before treatment, plus antibiotic prophylaxis
- Ravulizumab (Ultomiris): longer-acting eculizumab (every 8 weeks vs 2 weeks); same mechanism + indications

**Avacopan (Tavneos):** Oral C5aR1 antagonist; ANCA vasculitis (GPA/MPA) — adjunct to standard therapy (rituximab or cyclophosphamide), allows steroid taper.

---

## Decision Cheat Sheet

| Disease | Preferred Biologic | Notes |
|---------|-------------------|-------|
| RA (MTX failure) | TNF inhibitor (adalimumab, etanercept) or abatacept | JAK inhibitor if biologic-naive or -experienced |
| RA (biologic failure) | JAK inhibitor or switch biologic class | Upadacitinib; high efficacy |
| Plaque psoriasis | IL-17Ai (secukinumab) or IL-23p19i (risankizumab) | Highest efficacy biologics |
| PsA | IL-17Ai or TNF-i | Both class-leading; IL-17 slightly favored for skin |
| AS / axSpA | IL-17Ai or TNF-i | IL-17Ai for TNF-i failure |
| Crohn's disease | Anti-TNF (infliximab, adalimumab) or vedolizumab or ustekinumab | Risankizumab for maintenance; upadacitinib for moderate-severe |
| Ulcerative colitis | Anti-TNF, vedolizumab, or tofacitinib/upadacitinib | Vedolizumab: gut-selective α4β7-integrin block |
| SLE | Belimumab (anti-BAFF) | Anifrolumab (anti-IFNAR) for active SLE |
| Atopic dermatitis | Dupilumab (moderate-severe) → upadacitinib/tralokinumab | Dupilumab first-line biologic |
| Severe asthma (eosinophilic) | Mepolizumab or benralizumab or dupilumab | Tezepelumab for unselected type-2 |
| Transplant maintenance | Tacrolimus + MMF + prednisone | Standard triple therapy |
| PNH | Eculizumab or ravulizumab | PEGcetacoplan if breakthrough hemolysis |
| GBS / CIDP | IVIG or plasmapheresis (equivalent) | NOT steroids for GBS; steroids for CIDP |
| ITP | IVIG ± anti-D (Rh+) ± TPO-RA | IVIG fastest; rituximab for chronic refractory |

---

## Common Confusion Points

**Etanercept vs infliximab for IBD:** Etanercept does NOT work for Crohn's or UC — paradoxically can cause new-onset IBD. Infliximab and adalimumab are approved; certolizumab (Crohn's only). This is not a class effect; mechanism relates to structural differences (soluble receptor decoy vs IgG mAb).

**Tacrolimus vs cyclosporine — same target, different binding protein:** Both block calcineurin; tacrolimus binds FKBP12, CsA binds cyclophilin. The FKBP12-tacrolimus complex inhibits calcineurin (same end result). Tacrolimus is ~100× more potent. Drug interactions with CYP3A4 inducers/inhibitors affect both equally.

**MMF lymphocyte-selectivity:** Most cells can use the purine salvage pathway (hypoxanthine/guanine → IMP via HGPRT). Lymphocytes almost exclusively use the de novo pathway. MMF inhibits de novo → preferential lymphocyte effect. Same reason azathioprine/6-MP works (TPMT + XO involved; different mechanism).

**IL-17 in IBD — paradoxical:** IL-17 inhibitors are contraindicated in IBD (Crohn's). Blocking IL-17A removes a mucosal barrier cytokine (needed for epithelial defense), leading to IBD exacerbation. Paradoxical because IL-17/IL-23 axis is pro-inflammatory in psoriasis/AS but mucosal-protective in gut.

**JAK inhibitor VTE/malignancy signal:** The ORAL Surveillance trial was the catalyst for FDA warnings on ALL JAK inhibitors. BUT the trial had major confounders (high cardiovascular risk patients; no head-to-head with biologics in lower-risk populations). Real-world data suggest risk is real but modest. Risk-benefit still positive in many patients; avoid in high-risk (prior DVT, malignancy, ≥50 + CV risk factors).

**IVIG mechanism in ITP:** IgG Fc portions saturate FcγRIII on macrophages → macrophages can't bind IgG-coated platelets → platelets not destroyed. Effect is temporary (7–14 days), not curative. Also: anti-idiotypic antibodies against anti-platelet IgG contribute.
