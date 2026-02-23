# Bacterial Disease

## The Big Picture: Classification by Cell Wall

```
BACTERIA
┌──────────────────────────────┬────────────────────────────────┐
│  GRAM-POSITIVE               │  GRAM-NEGATIVE                 │
│  Crystal violet retained     │  Counterstain (safranin) pink  │
│  Thick peptidoglycan (PG)    │  Thin PG + outer membrane (OM) │
│  No outer membrane           │  OM: LPS (lipopolysaccharide)  │
│  Teichoic acids in PG        │  = endotoxin                   │
│                              │                                │
│  Target of β-lactams,        │  OM barrier: excludes many     │
│  vancomycin, daptomycin      │  antibiotics; efflux pumps     │
│                              │                                │
│  Examples:                   │  Examples:                     │
│  Staph, Strep, Bacillus,     │  E. coli, Salmonella, N. gonor-│
│  Clostridium, Listeria,      │  rhoeae, Pseudomonas, H. pylori│
│  Enterococcus, Actinomyces   │  Klebsiella, H. influenzae,    │
│                              │  Bordetella, Campylobacter     │
└──────────────────────────────┴────────────────────────────────┘

NEITHER (atypical — no cell wall or unique structure):
  Mycobacteria: acid-fast (mycolic acid-rich waxy wall; neither Gram+/−)
  Mycoplasma: NO cell wall at all → β-lactams useless
  Spirochetes: coiled (Treponema, Leptospira, Borrelia) — too thin to Gram stain well
  Rickettsia/Chlamydia/Coxiella: obligate intracellular
```

---

## Bacterial Structure and Virulence Factors

### Cell Envelope

```
GRAM-POSITIVE:
  Cytoplasm → Plasma membrane → Thick PG (20–80 nm) → surface proteins
  Teichoic acids: interspersed in PG → facilitate biofilm, drug binding
  Some have capsule (outer, polysaccharide) — antiphagocytic

GRAM-NEGATIVE:
  Cytoplasm → Plasma membrane → Thin PG (2–7 nm) → Periplasm → Outer membrane
  Outer membrane:
    Inner leaflet: phospholipid
    Outer leaflet: LPS (lipopolysaccharide)
      Lipid A: embedded in OM, toxic endotoxin moiety — triggers TLR4 → TNF/IL-1 cascade → sepsis
      Core polysaccharide: structural
      O-antigen: highly variable polysaccharide chain → serotyping target (O antigen in E. coli O157:H7)
  Porins (OmpC, OmpF): protein channels in OM for small molecule diffusion
  Efflux pumps: span OM + PG + PM → pump out antibiotics
```

### Virulence Factors

| Factor | Mechanism | Examples |
|--------|-----------|---------|
| Capsule | Antiphagocytic (hides PAMPs from phagocyte PRRs) | S. pneumoniae, H. influenzae type b, N. meningitidis, K. pneumoniae |
| Adhesins | Bind host cell receptors — required for colonization | Pili/fimbriae (UPEC mannose-binding type 1 pili → uroepithelium), M protein (GAS) |
| Biofilm | Matrix-enclosed community; ↑↑ antibiotic resistance (~1,000×); immune evasion | S. epidermidis on catheters, P. aeruginosa in CF lungs, S. aureus on prosthetics |
| Exotoxins | Protein toxins secreted by bacteria | See below |
| Endotoxin (LPS) | Gram-negative OM component, not secreted; TLR4 agonist → cytokine storm | All gram-negatives; sepsis driver |
| Superantigens | Bypass normal MHC/TCR specificity → massive T cell activation → cytokine storm | TSST-1 (S. aureus), SpeA (S. pyogenes) → toxic shock |
| Siderophores | Iron chelators — compete for host iron (iron is limiting in host) | Enterobactin (E. coli), pyoverdine (Pseudomonas) |
| Type III Secretion System (T3SS) | Molecular syringe — injects effector proteins directly into host cell cytoplasm | Salmonella (vacuole survival), Shigella (intracellular motility), EPEC (pedestal formation) |

---

## Exotoxin Mechanisms

### A-B Toxins (most important class)

```
Structure: B subunit (Binding) + A subunit (Active enzymatic moiety)
B binds host receptor → endocytosis → A subunit translocates into cytoplasm → action

CHOLERA TOXIN (Vibrio cholerae):
  A subunit: ADP-ribosylates Gsα (locks Gs in "always on" state)
  → Adenylyl cyclase constitutively active → ↑↑↑ cAMP
  → PKA → CFTR Cl⁻ channel open → massive Cl⁻ (+ Na⁺, water) secretion into gut lumen
  → Rice-water diarrhea (up to 20 L/day) → dehydration/death if untreated
  Mechanism: same as "activating mutation" in GPCR pathway

DIPHTHERIA TOXIN (Corynebacterium diphtheriae):
  A subunit: ADP-ribosylates EF-2 (elongation factor 2)
  → Protein synthesis stops → cell death
  → Pseudomembrane in pharynx + myocarditis + neuropathy

BOTULINUM TOXIN (Clostridium botulinum):
  A subunit: Zn²⁺-dependent protease → cleaves SNARE proteins (synaptobrevin/SNAP-25)
  → ACh vesicles cannot fuse at NMJ → flaccid paralysis (descending, cranial nerves first)
  Most potent toxin known (~1 ng/kg lethal)
  Clinical use: therapeutic (cosmetic, dystonia, migraine, achalasia)

TETANUS TOXIN (Clostridium tetani):
  Also cleaves SNARE proteins — but retrograde transport to spinal cord
  Blocks GABA/glycine release from inhibitory interneurons → disinhibition
  → Spastic paralysis (risus sardonicus, opisthotonus) — opposite of botulism
  Lock jaw (trismus), risus sardonicus, arched back

ANTHRAX TOXIN (Bacillus anthracis):
  Three components: PA (protective antigen) + EF (edema factor) + LF (lethal factor)
  PA (B component) binds ANTXR → pore → delivers EF or LF
  EF: adenylyl cyclase → ↑ cAMP → edema
  LF: MAPKK protease → disrupts MAPK signaling → macrophage apoptosis, tissue destruction

PERTUSSIS TOXIN (Bordetella pertussis):
  ADP-ribosylates Giα → Gi locked "off" → Gs unopposed → ↑ cAMP in multiple cells
  Also: tracheal cytotoxin destroys ciliated cells → classic "whoop" + inability to clear secretions
```

### Pore-Forming Toxins

```
Staphylococcal α-toxin (alpha-hemolysin): heptameric pore in RBC/leukocyte membranes → lysis
Streptococcal streptolysin O/S: cholesterol-dependent cytolysins → RBC + immune cell lysis
  → Antistreptolysin O (ASO) titer: marker of recent Strep pyogenes infection
Clostridium perfringens α-toxin: phospholipase C → hydrolyzes membrane phospholipids → gas gangrene
```

---

## Key Pathogens by System

### Respiratory

| Organism | Gram | Key features | Disease |
|----------|------|-------------|---------|
| S. pneumoniae | + cocci (diplococci) | Capsule (85 serotypes), optochin-sensitive, bile-soluble | Lobar pneumonia, meningitis, otitis media, sinusitis |
| S. pyogenes (GAS) | + cocci (chains) | M protein, streptolysin, DNase; antigen → ASO titer | Pharyngitis, scarlet fever, rheumatic fever, necrotizing fasciitis |
| M. tuberculosis | Acid-fast bacillus | Cord factor (trehalose dimycolate), caseous granuloma; PPD/IGRA test | TB (primary, reactivation, miliary, extrapulmonary) |
| B. pertussis | − coccobacillus | Pertussis toxin, tracheal cytotoxin, filamentous hemagglutinin | Whooping cough (paroxysmal cough + "whoop") |
| Legionella pneumophila | − rod (requires cysteine for culture) | Aerosolized water droplets; intracellular (alveolar macrophages); Legionella antigen in urine | Legionnaire's disease (atypical pneumonia) |
| H. influenzae | − coccobacillus | Type b: capsule (anti-Hib vaccine); nontypeable: common in COPD exacerbations | Epiglottitis (type b), otitis media, pneumonia |

### GI

| Organism | Key mechanism | Disease |
|----------|--------------|---------|
| Salmonella typhi | Intracellular macrophage survival (Vi capsule); fecal-oral | Typhoid fever: sustained bacteremia, rose spots, splenomegaly |
| Salmonella non-typhi | Invades gut epithelium, inflammatory diarrhea | Salmonellosis (poultry/eggs) |
| Shigella | T3SS + Shiga toxin → colonic epithelium invasion + Stx → bloody diarrhea (dysentery) | Very low infective dose (~10 organisms) |
| Campylobacter jejuni | Comma-shaped; poultry source; guillain-barré post-infection | Bloody diarrhea; GBS trigger (anti-ganglioside antibodies) |
| H. pylori | Urease + VacA + CagA; colonizes gastric mucus; 70% of peptic ulcers | PUD, gastric adenocarcinoma, MALT lymphoma |
| ETEC | Heat-labile (LT = cholera-like) + heat-stable (ST = ↑ cGMP) toxins | "Traveler's diarrhea" — watery, non-bloody |
| EPEC | T3SS + intimin: pedestals on enterocytes, effacement of microvilli | Infantile diarrhea (developing countries) |
| EHEC (O157:H7) | Shiga toxin 1+2 → endothelial injury → HUS (HUS = hemolytic uremic syndrome) | Bloody diarrhea + HUS; hamburger disease; NO antibiotics (↑ Stx release) |
| C. difficile | Toxin A (enterotoxin) + Toxin B (cytotoxin) after antibiotic disruption of microbiome | Antibiotic-associated diarrhea, pseudomembranous colitis; treatment: vancomycin or fidaxomicin; recurrent: FMT |

### Neurological / Meningitis

| Organism | Age group | Key feature |
|----------|-----------|-------------|
| N. meningitidis | Teens/young adults (college) | Serogroups A/B/C/W/Y; petechial/purpuric rash; treat empirically with ceftriaxone |
| S. pneumoniae | Elderly/asplenic | Most common bacterial meningitis overall in adults |
| Listeria monocytogenes | Neonates, immunocompromised, pregnant, elderly | Unpasteurized dairy; use ampicillin (resistant to cephalosporins) |
| T. pallidum (syphilis) | Variable | Tertiary: tabes dorsalis (demyelination posterior columns), general paresis; CSF VDRL |
| Borrelia burgdorferi | Northeast US | Lyme disease — EM rash, Bannwarth syndrome (CNS), AV block, arthritis |

### Skin/Soft Tissue and Systemic

| Organism | Disease | Key mechanism |
|----------|---------|--------------|
| S. aureus | Impetigo, cellulitis, abscess, bacteremia, endocarditis, osteomyelitis | PVL toxin; Protein A (blocks IgG Fc); TSST-1 (toxic shock) |
| MRSA | S. aureus with mecA gene (PBP2a — altered penicillin-binding protein) | Resistant to all β-lactams; treat with vancomycin, daptomycin, linezolid |
| S. epidermidis | Prosthetic valve endocarditis, catheter infections | Biofilm; coagulase negative |
| Clostridium perfringens | Gas gangrene (myonecrosis) | α-toxin (phospholipase) + rapid tissue spread |
| Clostridium tetani | Tetanus | Tetanospasmin: blocks inhibitory interneurons (see above) |
| Vibrio vulnificus | Wound infection from seawater/raw shellfish | Necrotizing fasciitis; high mortality in liver disease |

---

## Antibiotic Resistance Mechanisms

```
FOUR MAIN MECHANISMS:

1. ENZYMATIC INACTIVATION:
   β-lactamases: hydrolyze β-lactam ring → penicillins/cephalosporins/carbapenems inactive
     ESBL (extended-spectrum β-lactamase): destroys 3rd-gen cephalosporins (E. coli, Klebsiella)
     KPC (Klebsiella pneumoniae carbapenemase): destroys carbapenems — "last resort" antibiotics
     MBL (metallo-β-lactamase): e.g., NDM-1 — destroys almost all β-lactams
   Aminoglycoside-modifying enzymes: acetylation, phosphorylation, adenylation

2. TARGET MODIFICATION:
   PBP2a (mecA gene in MRSA): altered penicillin-binding protein → β-lactams can't bind → no cell wall inhibition
   Ribosome methylation (erm genes): 23S rRNA methylated → macrolides + clindamycin can't bind
   DNA gyrase mutation (gyrA): quinolones can't bind → fluoroquinolone resistance
   VanA/VanB (vancomycin-resistant Enterococcus — VRE): D-Ala-D-Ala changed to D-Ala-D-Lac → vancomycin can't bind

3. REDUCED PERMEABILITY:
   Loss/downregulation of outer membrane porins in Gram-negatives → carbapenem resistance
   Especially P. aeruginosa (OprD loss) + Acinetobacter

4. ACTIVE EFFLUX:
   MexAB-OprM (Pseudomonas): multi-drug efflux pump spanning OM → pumps out β-lactams, fluoroquinolones, tetracyclines
   AcrAB-TolC (E. coli): similar broad-spectrum efflux

PLASMID TRANSFER:
  Resistance genes on plasmids → horizontal gene transfer via conjugation (F-pilus)
  Single plasmid can carry multiple resistance determinants → pan-resistance in one step
```

### ESKAPE Pathogens

WHO priority drug-resistant organisms:

```
E — Enterococcus faecium (VRE)
S — Staphylococcus aureus (MRSA)
K — Klebsiella pneumoniae (ESBL/KPC/MBL)
A — Acinetobacter baumannii (pan-resistant strains)
P — Pseudomonas aeruginosa (innately resistant + acquires more)
E — Enterobacter species (chromosomal AmpC induction)
```

---

## Bacterial Genetics: Resistance Spread

```
VERTICAL TRANSMISSION: mutation → selection by antibiotics
HORIZONTAL GENE TRANSFER (more clinically important):
  Conjugation: physical contact via pilus → plasmid transfer (resistance plasmids)
  Transduction: bacteriophage carries DNA between bacteria
  Transformation: naked DNA uptake from environment (competent bacteria)
  Transposons ("jumping genes"): move resistance genes between chromosomes/plasmids

ANTIBIOTIC STEWARDSHIP:
  Antibiotic exposure is evolutionary pressure for resistance
  Narrow-spectrum preferred when possible
  Duration: shortest effective course (reduces selection pressure)
  De-escalation: broad → narrow once culture + sensitivities known
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Gram+ thick wall: which antibiotics blocked by OM? | β-lactams work well on Gram+; Gram− OM is a barrier to many (only small/hydrophilic pass porins) |
| MRSA mechanism? | mecA → PBP2a: altered transpeptidase, still cross-links cell wall, β-lactam ring can't bind |
| Cholera toxin: why massive watery diarrhea? | Locks Gsα on → ↑↑ cAMP → CFTR permanently open → isotonic secretion into gut lumen |
| Why no antibiotics in EHEC O157? | Stx phage induction — antibiotics → bacterial lysis → phage release → ↑↑ Shiga toxin → HUS |
| What's different about Listeria that changes treatment? | Intrinsically resistant to cephalosporins (all standard "covers" meningitis); need ampicillin + gentamicin |
| Biofilm resistance mechanism? | Physical matrix limits antibiotic diffusion; metabolically dormant (persister) cells not killed by most antibiotics; efflux pump upregulation |

---

## Common Confusion Points

**Bactericidal vs bacteriostatic: clinically matters less than people think**
- Bactericidal: kills bacteria (β-lactams, fluoroquinolones, aminoglycosides, vancomycin)
- Bacteriostatic: inhibits growth, relies on host immune clearance (tetracyclines, macrolides, clindamycin, chloramphenicol, sulfonamides)
- In immunocompromised patients: bactericidal preferred (no immune system to finish the job)
- In endocarditis/meningitis: bactericidal required

**LPS (endotoxin) vs exotoxin: not same thing**
- LPS: structural component of Gram-negative OM, lipid A is the toxic part; TLR4 agonist; triggers cytokine storm; not directly secreted
- Exotoxin: protein toxin actively secreted by bacteria; more potent; neutralized by antibodies more readily

**Gram staining is not infallible**
- Old cultures, antibiotic-treated, or lysed bacteria stain poorly
- Mycobacteria, Chlamydia, Rickettsia, Mycoplasma don't Gram stain properly
- Spirochetes too thin for light microscopy (dark field or silver stain)

**S. aureus vs S. epidermidis distinction**
- S. aureus: coagulase-positive; causes aggressive infection
- S. epidermidis: coagulase-negative; usually commensal; pathogenic mainly on implanted devices via biofilm
- Novobiocin-sensitive (S. epidermidis) vs novobiocin-resistant (S. saprophyticus — UTIs in young women)
