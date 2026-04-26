# Pathogen Mechanisms and Virulence

## The Big Picture

```
PATHOGEN MECHANISMS: HOW MICROBES CAUSE DISEASE
=================================================

  NOT ACCIDENT — Virulence is evolved strategy: pathogens manipulate
  host biology with molecular precision. Most mechanisms are acquired
  via horizontal gene transfer (pathogenicity islands).

  FRAMEWORK: INFECTION = SEQUENCE OF STEPS
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  1. ENCOUNTER   → Exposure to pathogen (transmission)           │
  │        ↓                                                        │
  │  2. COLONIZATION → Adhere to host surface (adhesins)            │
  │        ↓                                                        │
  │  3. INVASION    → Enter host cells or tissues (invasins)        │
  │        ↓                                                        │
  │  4. DAMAGE      → Toxins, direct killing, immune-mediated       │
  │        ↓                                                        │
  │  5. IMMUNE      → Evade or subvert immune response              │
  │     EVASION                                                     │
  │        ↓                                                        │
  │  6. SPREAD      → Dissemination; or chronic infection           │
  │                                                                 │
  │  DIFFERENT PATHOGENS FAIL DIFFERENTLY:                          │
  │  Toxin-mediated: Colonize surface only → toxin does the work    │
  │    (Cholera, C. diff, diphtheria)                               │
  │  Intracellular: Must invade; hide from immune system            │
  │    (Mycobacterium, Salmonella, Chlamydia, Listeria)             │
  │  Extracellular: Invade tissue; resist phagocytosis              │
  │    (Streptococcus pneumoniae, Staphylococcus aureus)            │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Koch's Postulates and Their Limits

```
  KOCH'S POSTULATES (1884)
  ========================

  Robert Koch established causality criteria for infectious disease:

  1. Organism must be present in all cases of the disease
  2. Organism must be isolated from diseased host + grown in pure culture
  3. Cultured organism must cause disease when introduced into healthy host
  4. Organism must be re-isolated from experimentally infected host

  HISTORICAL IMPORTANCE:
  Proven TB causation (Mycobacterium tuberculosis, 1882)
  Anthrax causation (Bacillus anthracis)
  Established experimental standards for all of infectious disease

  MODERN LIMITATIONS AND FAILURES:
  ┌────────────────────────────────────────────────────────────────┐
  │ FAILURE MODE            EXAMPLE                                │
  │                                                                │
  │ Non-culturable          ~99% of soil bacteria can't be grown   │
  │                         Tropheryma whipplei (Whipple's disease)│
  │                         Discovered via PCR only                │
  │                                                                │
  │ Healthy carriers        H. pylori: ~50% of world asymp. carrier│
  │ (Postulate 1 violated) V. cholerae: Present without disease    │
  │                                                                │
  │ Animal model failure    H. pylori: Only infects humans/monkeys │
  │ (Postulate 3)          Treponema pallidum (syphilis): No easy  │
  │                         animal model                           │
  │                                                                │
  │ Polymicrobial disease   Periodontal disease: No single agent   │
  │                         BV: Polymicrobial dysbiosis            │
  │                                                                │
  │ Viral diseases          Viruses can't be "cultured" classically│
  │                         HIV: Satisfies in modified form        │
  └────────────────────────────────────────────────────────────────┘

  MOLECULAR KOCH'S POSTULATES (Falkow, 1988):
  1. Virulence gene found in pathogen, not commensal strains
  2. Inactivation reduces virulence
  3. Re-introduction restores virulence
  → More rigorous; identifies specific virulence factors
  → Still challenged by multifactorial virulence
```

---

## Adhesins and Colonization

```
  HOW PATHOGENS STICK
  ====================

  ADHESIN CLASSES:
  ┌────────────────────────────────────────────────────────────────┐
  │ PILI / FIMBRIAE                                                │
  │   Type I pili (E. coli): Mannose-binding FimH adhesin          │
  │   → Binds uroepithelium → UTI (uropathogenic E. coli, UPEC)    │
  │   P pili (UPEC): Gal-Gal binding; upper UTI/pyelonephritis     │
  │   Type IV pili (N. gonorrhoeae, P. aeruginosa):                │
  │   → Retractile: Pull cell forward (twitching motility)         │
  │   → Retract with 100+ pN force                                 │
  │                                                                │
  │ OUTER MEMBRANE ADHESINS                                        │
  │   Invasin (Yersinia): Binds β1-integrin on M cells             │
  │   Intimin (EPEC): Tir receptor injection then intimin binding  │
  │   (EPEC injects its own receptor via T3SS, then binds to it!)  │
  │                                                                │
  │ AFIMBRIAL ADHESINS                                             │
  │   Dr adhesins (UPEC): DAF (decay-accelerating factor) binding  │
  │                                                                │
  │ HEMAGGLUTININS                                                 │
  │   Influenza HA: Binds sialic acid (N-acetylneuraminic acid)    │
  │   HA with α2-3 linkage: Avian tropism (respiratory epithelium) │
  │   HA with α2-6 linkage: Human tropism (upper respiratory)      │
  │   → Pandemic risk: Virus switching receptor binding            │
  └────────────────────────────────────────────────────────────────┘

  ANTI-ADHESION THERAPEUTICS:
  ─ FimH inhibitors: Mannosides; clinical trials for UPEC UTI
  ─ Zanamivir/oseltamivir: Target neuraminidase but affects HA function
  ─ Probiotics: Competitive exclusion — Lactobacillus blocks uropathogen adhesion
```

---

## Toxins: The Molecular Weapons

```
  BACTERIAL TOXINS
  =================

  CLASSIFICATION:
  ┌────────────────────────────────────────────────────────────────┐
  │ EXOTOXINS: Secreted proteins; highly specific; often binary    │
  │   Heat-labile; neutralized by antibodies (toxoids for vaccines)│
  │                                                                │
  │ ENDOTOXIN: LPS from Gram-negative cell wall                    │
  │   Heat-stable; not protein; not neutralized by antibodies      │
  │   TLR4 agonist → endotoxic shock at systemic concentrations    │
  │   (See 01-BACTERIAL-BIOLOGY.md)                                │
  └────────────────────────────────────────────────────────────────┘

  A-B TOXIN STRUCTURE (most classical toxins):
  ┌────────────────────────────────────────────────────────────────┐
  │   B subunit (Binding): Binds specific receptor on target cell  │
  │   → Endocytosis or channel formation                           │
  │                                                                │
  │   A subunit (Active): Catalytic; crosses into cytoplasm        │
  │   → Enzymatic modification of host target                      │
  │   → Often NAD⁺-dependent (ADP-ribosyltransferases)             │
  └────────────────────────────────────────────────────────────────┘

  MAJOR TOXIN EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────┐
  │ TOXIN              ORGANISM        MECHANISM                     │
  │                                                                  │
  │ Cholera toxin (CT) V. cholerae     B5: GM1 ganglioside binding   │
  │                                    A: ADP-ribosylates Gαs        │
  │                                    → Permanently activates AC    │
  │                                    → cAMP↑↑ → Cl⁻/water efflux   │
  │                                    → Rice-water diarrhea         │
  │                                    Up to 20 L/day fluid loss     │
  │                                                                  │
  │ Diphtheria toxin   C. diphtheriae  Phage-encoded (β-phage)       │
  │                                    B: HB-EGF receptor binding    │
  │                                    A: ADP-ribosylates EF-2       │
  │                                    → Halts protein synthesis     │
  │                                    → Myocarditis, nerve damage   │
  │                                                                  │
  │ Botulinum toxin    C. botulinum    7 serotypes (A–G)             │
  │                                    B: SV2/synaptotagmin binding  │
  │                                    A: Metalloprotease; cleaves   │
  │                                    SNAP-25 or VAMP (SNAREs)      │
  │                                    → No ACh vesicle fusion       │
  │                                    → Flaccid paralysis           │
  │                                    LD₅₀ ~1 ng/kg — most toxic    │
  │                                    substance known               │
  │                                                                  │
  │ Tetanus toxin      C. tetani       Travels retrogradely up axon  │
  │                                    Cleaves VAMP in inhibitory    │
  │                                    neurons → blocks Gly/GABA     │
  │                                    → Spastic paralysis           │
  │                                    (opposite of botulinum)       │
  │                                                                  │
  │ Shiga toxin        STEC (E. coli)  Phage-encoded (like diphther)│
  │ (Stx1, Stx2)       S. dysenteriae  B5: Gb3 glycolipid binding    │
  │                                    A: Cleaves 28S rRNA (N-glycos)│
  │                                    → Halts ribosomes → cell death│
  │                                    → HUS (hemolytic-uremic synd.)│
  │                                    Endothelial damage → TMA      │
  │                                                                  │
  │ Anthrax toxin      B. anthracis    Binary (two-part):            │
  │                                    PA (protective antigen):      │
  │                                    Binds ANTXR1/2; heptamer pore │
  │                                    LF (lethal factor):           │
  │                                    MAPKK metalloprotease → death │
  │                                    EF (edema factor):            │
  │                                    Adenylate cyclase (calmodulin │
  │                                    activated) → cAMP ↑ → edema   │
  │                                                                  │
  │ TSST-1             S. aureus       SUPERANTIGEN                  │
  │ Staphylococcal     S. aureus       Bridges MHC II outside groove │
  │ enterotoxins       S. pyogenes     to TCR outside groove         │
  │ SPE-A, SPE-C       (also SAgs)     → Non-specific T cell         │
  │                                    activation (5–25% of all T    │
  │                                    cells vs. 0.001% normally)    │
  │                                    → Cytokine storm → TSS        │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Invasion Strategies

```
  HOW PATHOGENS INVADE HOST CELLS AND TISSUES
  =============================================

  TYPE III SECRETION SYSTEM (T3SS): The bacterial syringe
  ┌────────────────────────────────────────────────────────────────┐
  │ Apparatus: Needle complex spanning both bacterial membranes    │
  │ Injects: Effector proteins directly into host cell cytoplasm   │
  │ No endocytosis needed — direct cytoplasmic delivery            │
  │                                                                │
  │ Salmonella T3SS (SPI-1): Entry                                 │
  │   SopE: GEF for Rac1/Cdc42 → actin polymerization → ruffles    │
  │   → Macropinocytosis → "Salmonella-containing vacuole" (SCV)   │
  │                                                                │
  │ Yersinia T3SS (Ysc): Anti-phagocytic                           │
  │   YopH: Tyrosine phosphatase → dephosphorylates focal adhesion │
  │   → Disrupts phagocytic cup → resists uptake                   │
  │   YopE, YopT: Inactivate Rac1/RhoA → actin collapse            │
  └────────────────────────────────────────────────────────────────┘

  TYPE IV SECRETION SYSTEM (T4SS):
  ─ Translocates DNA and proteins (homologous to conjugation pili)
  ─ H. pylori CagA: Injected into gastric epithelial cells
    → Dephosphorylated by SHP-2 → cell proliferation, oncogenic
    → cagA+ strains: Higher gastric cancer risk
  ─ Legionella pneumophila: T4SS (Dot/Icm) delivers ~300 effectors
    → Remodels phagosome → avoids lysosomal fusion → Legionella-containing vacuole

  ZIPPER ENTRY (receptor-mediated):
  ─ Listeria monocytogenes: InlA binds E-cadherin (intestinal entry)
    InlB binds c-Met receptor (hepatocyte entry)
    → Phagocytosis-like but NOT phagosomal death → see below

  TRIGGER MECHANISM (macropinocytosis):
  ─ Salmonella, Shigella: Inject actin-modulating effectors
    → Massive membrane ruffles → macropinosome → bacteria inside
```

---

## Intracellular Pathogens

```
  INTRACELLULAR SURVIVAL: HIDING FROM IMMUNITY
  ==============================================

  WHY GO INTRACELLULAR?
  ─ Immune evasion: Antibodies can't reach intracellular bacteria
  ─ Access to nutrients: Rich intracellular environment
  ─ Long-term persistence: Granulomas, latent infections

  STRATEGIES:
  ┌────────────────────────────────────────────────────────────────┐
  │ PHAGOSOMAL ESCAPE:                                             │
  │   Listeria monocytogenes (gold standard model organism)        │
  │   LLO (listeriolysin O): Pore-forming toxin; dissolves phagosome│
  │   → Bacteria in cytoplasm → ActA (actin polymerizing protein)  │
  │   → Arp2/3-mediated actin rocket → propels through cell        │
  │   → Protrusions → taken up by neighboring cells                │
  │   → Never exposed to extracellular antibodies                  │
  │                                                                │
  │   Shigella: IpaB/IpaC (T3SS) → phagosomal lysis                │
  │   → Cytoplasmic actin motility (IcsA protein)                  │
  │                                                                │
  │ PHAGOLYSOSOMAL FUSION BLOCK:                                   │
  │   Mycobacterium tuberculosis:                                  │
  │   ManLAM on surface → blocks Ca²⁺ signaling → no Ca²⁺/CaM      │
  │   → PI3P stays low → EEA1 not recruited → no fusion            │
  │   Vacuole maturation arrested at "early endosome" stage        │
  │   → Bacteria in comfortable mycobacterial phagosome            │
  │   SapM phosphatase: Dephosphorylates PI3P directly             │
  │                                                                │
  │   Legionella: T4SS → recruits ER-derived membranes             │
  │   → Legionella-replicative vacuole (LRV) ≠ lysosome            │
  │                                                                │
  │   Salmonella: SCV — acidified but not lysosomally fused        │
  │   SPI-2 T3SS effectors maintain SCV identity                   │
  │                                                                │
  │ LYSOSOMAL SURVIVAL:                                            │
  │   Coxiella burnetii: Requires acidified phagolysosome to grow  │
  │   → Opposite of most — NEEDS the harsh environment             │
  │   Leishmania: Survives lysosomal acid/hydrolases in macrophages│
  └────────────────────────────────────────────────────────────────┘

  LATENCY:
  ─ M. tuberculosis: Can form latent infection in granuloma for decades
    ~25% of world population has latent TB (LTBI)
    Reactivates when immunity wanes (HIV co-infection, immunosuppressives)
  ─ Herpes simplex virus: Latent in trigeminal ganglia; reactivates under stress
  ─ Varicella-zoster: Primary (chickenpox) → latent → reactivation (shingles)
  ─ HIV: Latent reservoir in resting CD4 T cells; barrier to cure
```

---

## Immune Evasion

```
  PATHOGEN IMMUNE EVASION STRATEGIES
  ====================================

  1. CAPSULE — ANTI-PHAGOCYTIC COATING:
  ┌────────────────────────────────────────────────────────────────┐
  │ Streptococcus pneumoniae: 100+ capsule serotypes (polysacch.)  │
  │ → Blocks phagocytosis (no complement receptor engagement)      │
  │ → Vaccines target capsule: PCV13, PCV20, PPSV23                │
  │                                                                │
  │ Cryptococcus neoformans: GXM (glucuronoxylomannan) capsule     │
  │ → Anti-phagocytic; also anti-inflammatory (anti-complement)    │
  │                                                                │
  │ Klebsiella pneumoniae: Hypermucoviscous capsule (hvKP strains) │
  │ → String test positive; liver abscess; emerging pathogen       │
  └────────────────────────────────────────────────────────────────┘

  2. ANTIGENIC VARIATION:
  ─ Trypanosoma brucei: VSG (variant surface glycoprotein) switching
    ~10⁷ variants; switches every few divisions; exhausts immune response
    (Covered in detail: 03-ARCHAEA-EUKARYOTIC-MICROBES.md)
  ─ Neisseria gonorrhoeae: Opa protein phase variation (ON/OFF)
    Pilus antigenic variation (pilE recombination with silent copies)
  ─ Borrelia burgdorferi: VlsE (VMP-like sequence E) antigenic variation
    → Lyme disease persistent infection despite immune response
  ─ Influenza: Antigenic drift (HA/NA mutation) + shift (reassortment)
    (Covered: 02-VIRAL-BIOLOGY.md)

  3. IgA PROTEASES:
  ─ N. meningitidis, N. gonorrhoeae, H. influenzae, S. pneumoniae
  ─ Specifically cleave secretory IgA1 (mucosal antibody) at hinge region
  ─ Why? IgA is the primary mucosal defense; cleavage = direct antibody destruction

  4. COMPLEMENT EVASION:
  ─ C1q inhibitors: Some bacteria secrete proteins that block complement activation
  ─ Factor H binding: S. aureus Sbi, ClfA, Efb bind Factor H
    → Negative complement regulator recruited to surface → inhibits opsonization
  ─ C5a peptidase (ScpA, S. pyogenes): Degrades C5a → no neutrophil recruitment

  5. INTRACELLULAR HIDING:
  ─ Already covered above (avoid antibodies, complement)

  6. NEUTROPHIL KILLING RESISTANCE:
  ─ S. aureus PVL (Panton-Valentine leukocidin): Pore-forming toxin that kills neutrophils
  ─ S. pyogenes SpeB: Protease that degrades neutrophil extracellular traps (NETs)
  ─ Staphyloxanthin (golden color): Carotenoid quenches reactive oxygen species

  7. NK CELL EVASION:
  ─ CMV UL18 (MHC I homolog): Binds inhibitory receptor LIR-1 on NK cells
  ─ M. tuberculosis: Inhibits NK-activating ligand NKG2D upregulation
  ─ "Stealth" approach: Don't trigger activating signals

  8. T CELL SUBVERSION:
  ─ M. tuberculosis: Modulates antigen presentation; delayed T cell priming
  ─ HIV: CD4 and CD8 receptor downregulation (Nef protein) → T cell evasion
  ─ Helicobacter pylori: Promotes regulatory T cell induction → suppress effectors
  ─ CTLA-4 mimics: Some viruses encode CTLA-4-like proteins to inhibit T cells
```

---

## Pathogenicity Islands and Virulence Gene Acquisition

```
  PATHOGENICITY ISLANDS (PAIs)
  =============================

  Pathogenicity Island = genomic island encoding clustered virulence genes
  acquired by horizontal gene transfer (HGT)

  HALLMARKS:
  ─ Distinct GC% from rest of chromosome (acquired from different organism)
  ─ Often flanked by IS elements or direct repeats (mobile element footprints)
  ─ Often near tRNA genes (integration sites for mobile elements)
  ─ Encode: T3SS/T4SS, toxins, adhesins, iron acquisition systems
  ─ Can be lost (instability): Some can be excised + retransferred

  KEY EXAMPLES:
  ┌────────────────────────────────────────────────────────────────┐
  │ SALMONELLA PATHOGENICITY ISLANDS:                              │
  │ SPI-1: T3SS for intestinal invasion (SopE, SipA, SipB)         │
  │ SPI-2: T3SS for intracellular survival (maintains SCV)         │
  │ SPI-3/4/5: Iron acquisition, additional effectors              │
  │ Without SPI-1 + SPI-2: Salmonella is non-pathogenic E. coli    │
  │                                                                │
  │ LEE (Locus of Enterocyte Effacement) — EPEC/EHEC:              │
  │ T3SS + Tir (receptor injection) + intimin + EspAB effectors    │
  │ → Attaching-and-effacing lesion on intestinal epithelium       │
  │ → Destroys microvilli; causes diarrhea                         │
  │                                                                │
  │ S. aureus PATHOGENICITY ISLANDS (SaPI):                        │
  │ SaPIbov1: Encodes toxic shock syndrome toxin (TSST-1)          │
  │ SaPI2: TSST-1 variant + other toxins                           │
  │ Unique: SaPI is ALSO a phage-parasitizing island               │
  │ → Hijacks helper phage for its own spread (brilliant)          │
  └────────────────────────────────────────────────────────────────┘

  LYSOGENIC CONVERSION: PHAGE ENCODES VIRULENCE
  ─ Diphtheria toxin: Encoded by corynephage β (phage)
    C. diphtheriae without phage → not virulent
  ─ Cholera toxin: Encoded by CTXφ phage
    V. cholerae without CTXφ → non-toxigenic (El Tor biotype in 7th pandemic)
  ─ Shiga toxin: stx1/stx2 genes on lambda-like phages in E. coli
    → Can transfer between E. coli strains → new STEC strains emerge
  ─ Botulinum toxin: Phage-encoded in some C. botulinum types
  Implication: Virulence can be acquired by any bacterium gaining the phage
```

---

## Decision Cheat Sheet

| Concept | Key Detail |
|---------|-----------|
| Koch's postulate failure | Non-culturable, healthy carriers, animal model gaps |
| Molecular Koch's postulates | Gene knockout → reduced virulence + complementation |
| Cholera toxin target | Gαs ADP-ribosylation → cAMP ↑↑ → water secretion |
| Botulinum vs. tetanus | Both cleave SNAREs; botulinum flaccid (NMJ), tetanus spastic (inhibitory neuron) |
| Superantigen mechanism | Cross-links MHC II to TCR outside normal groove → massive T cell activation |
| T3SS function | Molecular syringe; injects effectors directly into host cytoplasm |
| Listeria cytoplasmic escape | Listeriolysin O (LLO) pore-forming toxin; then actin rocket (ActA) |
| M. tuberculosis phagosome | Blocks phagolysosomal fusion; arrested at early endosome stage |
| Capsule function | Anti-phagocytic; also anti-complement; vaccine target (PCV) |
| VSG switching | Trypanosoma brucei; ~10⁷ variants; exhausts antibody response |
| Lysogenic conversion | Phage encodes virulence (diphtheria, cholera, Shiga toxins) |
| Pathogenicity island origin | HGT; distinct GC%; flanked by IS elements; near tRNA genes |

---

## Common Confusion Points

**Exotoxin vs. endotoxin**: Exotoxins are secreted proteins (heat-labile, specific receptors, neutralizable by antibodies, great vaccine targets). Endotoxin is LPS (heat-stable, not a protein, TLR4 agonist, not neutralized by antitoxin antibodies). They cause disease by completely different mechanisms.

**Flaccid vs. spastic paralysis in clostridial toxins**: Botulinum toxin and tetanus toxin are both SNARE-cleaving metalloproteases. Botulinum acts at the neuromuscular junction (peripheral) → blocks ACh release → FLACCID paralysis (can't contract). Tetanus toxin travels up the motor neuron, crosses the synapse to inhibitory interneurons → blocks glycine/GABA release → loss of inhibition → SPASTIC paralysis and convulsions.

**Why can't you target pathogenicity islands therapeutically?**: In principle anti-virulence drugs targeting T3SS would be great (selective pressure against virulence, not survival). In practice: clinical trials have been challenging because (1) bacteria survive and evolve, (2) rapid resistance to most inhibitors found, (3) no selective pressure (bacteria still grow). Still an active research area.

**Latent TB and "sterilizing" vs. "functional" cure**: ~25% of the world carries latent M. tuberculosis. The bacteria are alive in granulomas, not replicating much, controlled by T cell immunity. Reactivation occurs when immunity falls. Current TB drugs sterilize active infection but don't reliably clear latent disease. This is why new treatments and better diagnostics are needed.
