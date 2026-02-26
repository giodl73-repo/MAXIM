# 01 — Antibiotics

## Antibiotic Targets, Drug Classes, Resistance Mechanisms, Stewardship

---

**Systems Bridge:** Antibiotic resistance is an adversarial system where the defender (antibiotic) has a specific attack surface (the drug target), and the adversary (bacteria) evolves countermeasures through both vertical transmission (mutation under selective pressure) and horizontal propagation (lateral transfer of resistance genes via plasmids — the biological equivalent of a zero-day exploit shared across unrelated systems). The four resistance mechanisms map directly to defensive strategies in security: enzymatic inactivation = exploit neutralization before it reaches the target; target modification = patching the vulnerability so the exploit no longer works (MRSA's PBP2a); reduced permeability = network-level filtering so the attack payload never reaches the system; efflux pumps = active ejection before the payload can act. Plasmid-mediated horizontal gene transfer is the most dangerous because a single conjugation event can transfer a suite of resistance genes across bacterial species in a single step — equivalent to a shared exploit toolkit propagating across unrelated codebases. Antibiotic stewardship is defense-in-depth: narrow-spectrum preferred when possible (reduce selection pressure on off-target organisms), shortest effective duration (minimize evolutionary pressure duration), de-escalation on culture results (don't maintain broad pressure once the specific adversary is identified). The analogy to not keeping unused ports open or running unnecessary services is direct.

## Big Picture: Antibiotic Target Map

```
┌──────────────────────────────────────────────────────────────────────────┐
│                 BACTERIAL ANTIBIOTIC TARGETS                             │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  CELL WALL SYNTHESIS                                                     │
│    β-lactams: PBP binding → transpeptidation inhibition                 │
│    Glycopeptides: D-Ala-D-Ala binding → transglycosylation inhibition   │
│    Fosfomycin: MurA inhibition (PEP analog)                             │
│                                                                          │
│  CELL MEMBRANE                                                           │
│    Polymyxins (B, E/colistin): LPS displacement → pore formation        │
│    Daptomycin: Ca²⁺-dependent membrane depolarization                   │
│                                                                          │
│  PROTEIN SYNTHESIS — 30S ribosome                                       │
│    Aminoglycosides: 30S decoding site → misreading                      │
│    Tetracyclines: 30S A-site → block tRNA delivery                      │
│                                                                          │
│  PROTEIN SYNTHESIS — 50S ribosome                                       │
│    Macrolides: 23S rRNA peptide exit tunnel → premature dissociation     │
│    Chloramphenicol: 50S peptidyltransferase → ↓ elongation              │
│    Linezolid/tedizolid: 23S rRNA → prevents 70S initiation complex      │
│    Clindamycin: 23S rRNA (same site as macrolides) → dissociation       │
│                                                                          │
│  DNA REPLICATION / TRANSCRIPTION                                        │
│    Fluoroquinolones: DNA gyrase (GyrAB) + Topo IV (ParCE)               │
│    Metronidazole: DNA strand breaks via free radical                     │
│    Rifamycins: RNA polymerase β-subunit (rpoB)                          │
│                                                                          │
│  FOLATE SYNTHESIS                                                        │
│    Sulfonamides: DHPS inhibition (competes with PABA)                   │
│    Trimethoprim: DHFR inhibition → ↓ THF → ↓ nucleotides               │
│    TMP-SMX: double block (synergistic bactericidal at urinary levels)    │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. β-Lactams

### Mechanism

```
Peptidoglycan synthesis:
  Cytoplasm: MurA-G enzymes → UDP-MurNAc-pentapeptide (ending D-Ala-D-Ala)
  Membrane: lipid carrier → flipped to periplasm
  Cell wall: transglycosylase (polymerizes) + transpeptidase (cross-links)

β-lactam ring: structural analog of D-Ala-D-Ala terminus
  → Covalently binds PBP (penicillin-binding protein = transpeptidase)
  → Irreversible inhibition → ↓ cross-linking → weakened peptidoglycan
  → Autolysis (cellular hydrolases activated) → bactericidal

Time-dependent killing: efficacy depends on time above MIC (T>MIC)
  Optimal when drug concentration > MIC for 40–70% of dosing interval
  → Frequent dosing or extended infusions (β-lactam continuous infusion for resistant organisms)
```

### Class Progression

```
PENICILLINS:
  Natural: penicillin G (IV), V (PO) — Strep, syphilis, Clostridium
  Antistaphylococcal (penicillinase-resistant): oxacillin/nafcillin/dicloxacillin
    → Block penicillinase active site; bulky side chain prevents hydrolysis
    → Active vs MSSA (NOT MRSA)
  Aminopenicillins: ampicillin/amoxicillin — ↑ gram-neg spectrum (H. flu, E. coli, Listeria)
  Ureidopenicillins: piperacillin-tazobactam (pip/tazo) — anti-pseudomonal + anaerobes

CEPHALOSPORINS (gen 1–5):
  Gen 1 (cefazolin/cefalexin): gram+ cocci (MSSA, Strep); surgical prophylaxis
  Gen 2 (cefuroxime/cefoxitin): ↑ gram-neg; cefoxitin has anaerobic (B. fragilis) coverage
  Gen 3 (ceftriaxone/cefotaxime/ceftazidime): CSF penetration; ceftazidime = anti-Pseudomonas
  Gen 4 (cefepime): anti-Pseudomonas + gram+; Enterobacteriaceae; "Pseudomonas gen 3"
  Gen 5 (ceftaroline): MRSA coverage; anti-PBP2a; used for MRSA pneumonia/skin
  Ceftolozane-tazobactam / ceftazidime-avibactam: ESBL + some carbapenem-resistant Enterobacterales

CARBAPENEMS: imipenem, meropenem, ertapenem, doripenem
  Broadest β-lactam coverage: gram+/−/anaerobes; ESBL coverage
  Imipenem + cilastatin (dehydropeptidase inhibitor to prevent renal inactivation)
  Ertapenem: no anti-pseudomonal activity (unlike the rest)
  Resistance: carbapenemases (KPC, NDM, VIM, OXA-48) — critical ESKAPE issue

MONOBACTAMS: aztreonam
  Only gram-negative aerobic coverage; NO gram+ or anaerobe
  Useful in serious penicillin allergy (minimal cross-reactivity)
```

### β-Lactam Resistance

```
Mechanisms:
1. β-lactamase production (most common):
   Penicillinase: hydrolyzes penicillins (Staph)
   ESBL (extended-spectrum β-lactamase): gen 1–4 cephalosporins + penicillins; TEM/SHV/CTX-M
     → Treat with carbapenems or ceftolozane-tazo/ceftazidime-avibactam
   AmpC: inducible; Enterobacter/Citrobacter/Serratia (HECK YEA organisms — those on "SPACE")
   Carbapenemases: KPC (serine β-lactamase), NDM/VIM (metallo-β-lactamase), OXA-48
     → Often pan-resistant; ceftazidime-avibactam (not NDM), cefiderocol

2. Altered PBPs (MRSA — mecA gene → PBP2a; low affinity for all β-lactams)
3. Porins: ↓ influx (Pseudomonas OprD loss → imipenem resistance)
4. Efflux pumps: MexAB-OprM, MexXY, etc. (Pseudomonas)

β-lactamase inhibitors (BLIs):
  Clavulanic acid: suicide substrate; paired with amoxicillin (Augmentin) or ticarcillin
  Sulbactam: piperacillin not needed; paired with ampicillin; also direct Acinetobacter activity
  Tazobactam: paired with piperacillin
  Avibactam: non-β-lactam BLI; active vs KPC/OXA-48 but NOT NDM
  Relebactam: paired with imipenem/cilastatin (Recarbrio)
  Vaborbactam: paired with meropenem (Vabomere); KPC active
```

### Penicillin Allergy

```
True IgE-mediated (anaphylaxis): <1% of penicillin exposures
  RAST/skin testing available for clarification
  Major determinant: BPO (benzylpenicilloyl) in skin test
  Cross-reactivity with cephalosporins: side-chain similarity matters; ~1–2%
  Cross-reactivity with carbapenems: ~1%
  Cross-reactivity with aztreonam: NO cross-reactivity with penicillin
    Exception: aztreonam shares R1 side chain with ceftazidime → cross-reacts with that

"Penicillin allergy" label causes massive overuse of vancomycin and fluoroquinolones
→ Drives resistance; allergy delabeling programs important (skin testing/graded challenge)
```

---

## 2. Glycopeptides — Vancomycin

**Mechanism:** Binds D-Ala-D-Ala terminus of peptidoglycan precursor → blocks transglycosylase + transpeptidase. Too large to be hydrolyzed by β-lactamases.

**Spectrum:** Gram-positive only (too large to cross gram-negative outer membrane).

**Key uses:** MRSA (IV), C. diff (oral only for GI colonization — not absorbed), VRE-alternative infections, penicillin allergy.

**PK:** Time-dependent; target AUC/MIC ≥400 (trough monitoring being replaced by AUC monitoring). IV only for systemic infections (not absorbed PO).

**Toxicity:** Nephrotoxicity (synergistic with aminoglycosides), "red man syndrome" (rate-related histamine release → not allergy; slow infusion), ototoxicity.

**VRE resistance:**
- vanA (E. faecium, E. faecalis): D-Ala-D-Lac substitution → 1000× ↓ vancomycin affinity
- vanB: similar but not plasmid-mediated
- Treatment: linezolid or daptomycin for VRE

---

## 3. Macrolides

**Mechanism:** Bind 23S rRNA in peptide exit tunnel → premature peptide dissociation; inhibit 50S assembly. Bacteriostatic (mostly); bactericidal at high concentrations vs some.

**Spectrum:** Gram-positive (strep, staph), atypicals (Mycoplasma, Chlamydophila, Legionella), H. pylori (clarithromycin), MAC (azithromycin + ethambutol).

| Drug | Notes |
|------|-------|
| Erythromycin | Original; significant GI side effects (prokinetic effect via motilin); CYP3A4 inhibitor |
| Clarithromycin | ↑ bioavailability, less GI; H. pylori triple therapy; CYP3A4 inhibitor |
| Azithromycin | Z-pack; long t½ (tissue concentration; single 5-day course); no CYP3A4 inhibition; QTc prolongation |

**Drug interactions:** Erythromycin/clarithromycin are potent CYP3A4 inhibitors → statins (myopathy), calcium channel blockers, warfarin. Azithromycin minimal CYP interactions.

**QTc prolongation:** All macrolides (especially azithromycin) extend QTc → torsades de pointes risk with other QTc-prolonging drugs, hypokalemia, bradycardia.

**Resistance:** Methylation of 23S rRNA (erm genes — M phenotype); active efflux (mef genes — MS phenotype). MLSB phenotype: cross-resistance macrolides + lincosamides + streptogramins.

---

## 4. Fluoroquinolones

**Mechanism:** Inhibit DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE) → DNA strand breaks → bactericidal. Concentration-dependent killing (Cmax/MIC predicts efficacy).

| Drug | Spectrum/Niche |
|------|---------------|
| Ciprofloxacin | Gram-negative (best FQ for Pseudomonas); UTI/GI/anthrax; less gram+ |
| Levofloxacin | "Respiratory quinolone"; Strep pneumoniae + atypicals + gram-neg; CAP |
| Moxifloxacin | ↑ anaerobic coverage; NOT for UTI (insufficient urine concentration); QTc ↑↑ |
| Delafloxacin | MRSA-active; skin/lung infections |

**Toxicity:**
- **CNS:** Headache, dizziness, insomnia; psychosis; lowers seizure threshold (especially in theophylline/NSAIDs co-use)
- **Tendinopathy:** Achilles tendon rupture (inhibit tenocyte collagen synthesis); elderly + steroids = ↑ risk; FDA boxed warning
- **QTc prolongation:** Class effect; moxifloxacin >> ciprofloxacin
- **Cartilage:** Avoid in children <18 (except compelling indication); retinal detachment signal
- **Glucose metabolism:** Both hypo and hyperglycemia reported

**Resistance:**
- Target mutations: GyrA/ParC mutations (stepwise → high-level resistance)
- Efflux pumps, porin loss (Pseudomonas especially)
- QRDR (quinolone resistance-determining region) mutations rapidly selected by FQ exposure

---

## 5. Aminoglycosides

**Mechanism:** Bind 16S rRNA of 30S subunit → codon misreading → aberrant protein insertion → membrane disruption → lethal. Require oxygen for uptake (↑ transport in ΔpH) → ineffective in anaerobic environments and abscesses.

**Concentration-dependent killing:** High Cmax/MIC → enhanced efficacy AND PAE (post-antibiotic effect — suppressed regrowth for hours). Once-daily dosing preferred (optimize Cmax, minimize nephrotoxicity).

| Drug | Notes |
|------|-------|
| Gentamicin | Gram-negative (Pseudomonas); synergy with β-lactams for Enterococcus/Strep/Staph endocarditis |
| Tobramycin | ↑ Pseudomonas activity vs gentamicin; inhaled tobramycin (CF) |
| Amikacin | Resistant to most aminoglycoside-modifying enzymes; MDR gram-negatives |
| Streptomycin | TB (second-line); plague/tularemia; gentamicin synergy for Enterococcus |
| Neomycin | Oral (not absorbed) → bowel prep; topical |

**Toxicity (trough-dependent):**
- **Nephrotoxicity:** Proximal tubule accumulation → ATN; reversible; avoid volume depletion; monitor troughs
- **Ototoxicity:** Cochlear (irreversible; hair cell destruction — auditory) and vestibular; cumulative dose-dependent
- **Neuromuscular blockade:** At very high doses → respiratory failure; exacerbates MG

**Synergy with β-lactams:** β-lactam disrupts cell wall → ↑ aminoglycoside uptake into cell → synergistic bactericidal against Enterococcus, viridans streptococci, Staph (endocarditis).

---

## 6. Tetracyclines

**Mechanism:** Bind 16S rRNA of 30S subunit; block aminoacyl-tRNA from binding A-site → static elongation block. Bacteriostatic.

**Spectrum:** Very broad — intracellular (Chlamydia, Rickettsia, Ehrlichia, Anaplasma, Coxiella), atypicals, Lyme disease (Borrelia), spirochetes, Vibrio, gram+ and gram−.

| Drug | Notes |
|------|-------|
| Doxycycline | Workhorse; Lyme, RMSF, atypicals, CAP, MRSA skin/soft tissue, PO + IV |
| Minocycline | Better CNS penetration; MRSA activity; vestibular toxicity |
| Tigecycline | Glycylcycline; ESKAPE organisms except Pseudomonas; ↑ mortality signal in clinical trials |
| Omadacycline | Newer; MRSA skin + CAP; PO/IV |

**Toxicity:** Photosensitivity (use sunscreen), esophagitis (take with water upright), teeth discoloration and bone growth inhibition in children <8 and during pregnancy. Pseudotumor cerebri (rare).

**Resistance:** Efflux pumps (tet genes), ribosomal protection proteins (TetM/TetO). Tigecycline partially overcomes these (bulky glycyl group).

---

## 7. Key Individual Agents

### Clindamycin

**Target:** 23S rRNA 50S (same site as macrolides — MLSB cross-resistance). Bacteriostatic; inhibits transpeptidation.

**Spectrum:** Gram-positive (MRSA SSTIs, strep, anaerobes above diaphragm). Good anaerobic coverage (Bacteroides, Peptostreptococcus). NOT gram-negative aerobes.

**Key uses:** MRSA skin/soft tissue infections (with TMP-SMX or alone), aspiration pneumonia (anaerobes), pelvic infections, toxin suppression in necrotizing fasciitis (↓ toxin production even without killing).

**Toxicity:** C. difficile colitis (disrupts normal flora → C. diff overgrowth). High risk but any antibiotic can cause C. diff.

### Metronidazole

**Mechanism:** Nitroimidazole; undergoes intracellular reduction (by ferredoxin in anaerobes/protozoa) → reactive nitro radical → DNA strand breaks. Selectively toxic to anaerobes and microaerophiles.

**Spectrum:** Anaerobes (Bacteroides fragilis, C. diff, Clostridium), protozoa (Giardia, Trichomonas, Entamoeba histolytica).

**Key uses:** C. diff (moderate-severe; oral preferred), bacterial vaginosis, Giardia, Trichomonas, amebic colitis, anaerobic coverage (abdominal/pelvic infections + β-lactam).

**Toxicity:** Metallic taste, nausea, peripheral neuropathy (prolonged use), disulfiram-like reaction with alcohol (acetaldehyde accumulation).

### TMP-SMX (Trimethoprim-Sulfamethoxazole)

**Sequential folate pathway blockade:**
```
PABA
  │ ← Sulfonamide blocks (DHPS competes with PABA)
  ▼
Dihydropteroate
  │
  ▼
Dihydrofolate
  │ ← TMP blocks (DHFR inhibitor, selective for bacterial over human DHFR ~100,000x)
  ▼
Tetrahydrofolate → nucleotide synthesis
```

**Spectrum:** Broad; gram-positive (MRSA CA-SSTIs), gram-negative UTI pathogens, Nocardia, Stenotrophomonas maltophilia, Listeria.

**Key uses:** UTI, PCP prophylaxis and treatment (high dose), MRSA skin/soft tissue, Nocardia, Toxoplasma prophylaxis.

**Toxicity:** Allergy (sulfa allergy — rash, SJS/TEN, fever), hyperkalemia (TMP blocks ENaC = similar to K-sparing diuretic), ↑ SCr (TMP blocks creatinine secretion — not true GFR decline), anemia (folate depletion especially in elderly/malnourished).

**Sulfa allergy and antibiotic cross-reactivity:** Sulfonamide antibiotics ≠ sulfonamide non-antibiotics (furosemide, celecoxib, hydrochlorothiazide). Cross-reactivity between groups is minimal to none despite having sulfonamide moiety.

---

## 8. Resistance Mechanisms (Comprehensive)

```
ENZYMATIC INACTIVATION:
  β-lactamases (penicillinase, ESBL, AmpC, carbapenemases)
  Aminoglycoside-modifying enzymes: AAC (acetyltransferases), APH (phosphotransferases),
    ANT (nucleotidyltransferases) → add chemical groups to aminoglycoside → ↓ ribosome binding

TARGET MODIFICATION:
  MRSA: mecA → PBP2a → low β-lactam affinity
  VRE: vanA/B → D-Ala-D-Lac substitution → ↓ vancomycin binding
  Fluoroquinolone resistance: GyrA/ParC mutations → drug can't bind effectively
  Linezolid resistance: G2576T in 23S rRNA (rare, selected in prolonged therapy)
  Rifampin resistance: rpoB mutations (single step!) → never use as monotherapy

EFFLUX PUMPS (MDR transporters):
  RND family (gram-neg): MexAB-OprM (Pseudomonas), AcrAB-TolC (E. coli/Klebsiella)
  MFS family: tet genes (tetracycline), norA (S. aureus quinolone resistance)
  MATE family
  → Active efflux → ↓ intracellular drug concentration

REDUCED PERMEABILITY:
  Gram-negative outer membrane: porin mutation (OprD loss → imipenem resistance in Pseudomonas)
  Loss of OmpF/OmpC in Enterobacteriaceae → ↓ carbapenem penetration

BYPASS PATHWAYS:
  Acquired vancomycin resistance in Staph: VISA (vancomycin-intermediate) → thickened cell wall
    traps vancomycin before reaching D-Ala-D-Ala (not the same as VRE mechanism)

HORIZONTAL GENE TRANSFER (amplifies resistance spread):
  Conjugation: plasmids (R plasmids); most dangerous (carries multiple resistance genes)
  Transformation: uptake of environmental DNA (competent organisms: Strep pneumo, H. flu)
  Transduction: bacteriophage-mediated transfer
  Transposons/integrons: mobile genetic elements that "hop" between plasmids/chromosome
```

### ESKAPE Pathogens

```
E — Enterococcus faecium (VRE)
S — Staphylococcus aureus (MRSA)
K — Klebsiella pneumoniae (ESBL, KPC-carbapenemase)
A — Acinetobacter baumannii (pan-resistant; carbapenem + colistin last resort)
P — Pseudomonas aeruginosa (intrinsic resistance + acquired; multiple efflux)
E — Enterobacter species (inducible AmpC; "SPICE" organisms)

Treatment of MRSA:
  SSTI: TMP-SMX, doxycycline, clindamycin (oral); IV: vancomycin
  Bacteremia/endocarditis: vancomycin (IV) or daptomycin; ceftaroline (option)
  Pneumonia: vancomycin or linezolid (better lung penetration/less nephrotoxicity debate)

Treatment of MDR gram-negatives (ESKAPE):
  ESBL: carbapenems; ceftolozane-tazo/ceftazidime-avibactam alternatives
  KPC (Klebsiella): meropenem-vaborbactam, ceftazidime-avibactam, imipenem-cilastatin-relebactam
  NDM (metallo-β-lactamase): ceftazidime-avibactam + aztreonam; cefiderocol
  Acinetobacter: sulbactam-based regimens; polymyxins; cefiderocol
  Pseudomonas MDR: ceftolozane-tazo, ceftazidime-avibactam, imipenem-relebactam
```

---

## 9. Antibiotic Stewardship

```
4D Framework: right Drug / Dose / Duration / De-escalation

Principles:
  1. Culture before treatment (blood cultures before antibiotics in suspected bacteremia)
  2. Empiric based on syndrome + local epidemiology (antibiogram)
  3. De-escalate on day 2–3 when cultures return
  4. Shortest effective duration (reduces resistance, C. diff, side effects)
  5. IV-to-PO switch when tolerating oral and infection improving

Duration evidence:
  Uncomplicated CAP: 5 days (IDSA guidelines)
  Community UTI: 3 days (TMP-SMX), 5 days (nitrofurantoin)
  Bacteremia without source/endocarditis: 14 days minimum
  Staph bacteremia: 14 days (no endocarditis); 6 weeks (endocarditis)
  Sepsis: culture-guided; no benefit >7 days for most gram-neg sepsis

Procalcitonin (PCT): biomarker for bacterial infection
  ↑ in bacterial sepsis; low in viral infections, autoimmune
  PCT-guided algorithms: ↓ antibiotic duration in sepsis, pneumonia
  Not useful for localized infections (appendicitis, osteomyelitis)

C. difficile risk: clindamycin > fluoroquinolones > cephalosporins/penicillins > carbapenems
  Minimize broad-spectrum antibiotics; fidaxomicin or vancomycin to treat CDI
```

---

## Decision Cheat Sheet

| Clinical Scenario | Empiric Coverage | Drug of Choice |
|------------------|-----------------|----------------|
| MSSA bacteremia | Anti-staphylococcal penicillin or cefazolin | Nafcillin/cefazolin |
| MRSA bacteremia | Glycopeptide or lipopeptide | Vancomycin or daptomycin |
| Strep pneumo meningitis | 3rd gen ceph + vancomycin | Ceftriaxone + vancomycin (↑ resistance) |
| CAP (outpatient) | Macrolide or respiratory FQ | Azithromycin or levofloxacin |
| CAP (inpatient, ICU) | β-lactam + macrolide or FQ | Ceftriaxone + azithromycin |
| Intra-abdominal | Gram-neg + anaerobe coverage | Pip/tazo or carbapenems |
| UTI uncomplicated | Gram-neg urinary | TMP-SMX or nitrofurantoin |
| Anthrax prophylaxis | FQ or tetracycline | Ciprofloxacin or doxycycline |
| MDR Pseudomonas | Antipseudomonal β-lactam | Ceftolozane-tazo or pip/tazo |
| VRE | Oxazolidinone or lipopeptide | Linezolid or daptomycin |

---

## Common Confusion Points

**Cephalosporins and penicillin allergy:** Cross-reactivity is ~1–2% based on side-chain similarity, not the β-lactam ring. Cefazolin is safe in most penicillin allergies (different side chain from amoxicillin). Most "penicillin allergies" are not IgE-mediated — allergy testing/delabeling is underutilized.

**Macrolides: azithromycin is NOT a CYP3A4 inhibitor.** Erythromycin and clarithromycin are. Don't extrapolate drug interactions from "macrolide class" to azithromycin.

**Aminoglycoside once-daily dosing:** Once-daily is preferred for concentration-dependent killing + PAE. Reduces nephrotoxicity by allowing renal tubular recovery during low trough phase. Monitor troughs when dosing >5 days.

**Vancomycin AUC monitoring vs trough:** Old paradigm was targeting trough 15–20 mg/L. New guidelines target AUC/MIC ≥400 (measured AUC not simulated) — reduces nephrotoxicity with equivalent efficacy.

**Bacteriostatic vs bactericidal distinction clinically:** Mostly irrelevant for most infections (immune system clears bacteria). Bactericidal preferred for: endocarditis, meningitis, immunocompromised patients. Linezolid (bacteriostatic for Staph) is considered inferior to vancomycin for bacteremia/endocarditis.

**TMP-SCr rise:** TMP blocks creatinine secretion via OAT2 → apparent ↑ SCr of ~0.1–0.2 mg/dL. NOT true GFR decline. Don't stop TMP-SMX for this artifact. True nephrotoxicity is rare.
