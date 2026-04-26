# Antimicrobial Resistance

## The Big Picture

```
ANTIMICROBIAL RESISTANCE: THE EVOLUTION CRISIS
================================================

  SCALE OF THE PROBLEM:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Deaths attributable to AMR:  1.27 million/year (2019, Lancet)  │
  │  Deaths associated with AMR:  4.95 million/year (2019)          │
  │  Projected (if unaddressed):  10 million/year by 2050 (O'Neill) │
  │  Economic cost:               ~$100 trillion cumulative by 2050 │
  │                                                                 │
  │  NEW ANTIBIOTICS APPROVED (US FDA):                             │
  │  1980s: ~20 new approvals per decade                            │
  │  1990s: ~8 new approvals                                        │
  │  2000s: ~5 new approvals                                        │
  │  2010s: ~8 new approvals (mostly variations of existing classes)│
  │  Since 1990: No new class with novel mechanism widely deployed  │
  │  → Discovery void of ~30+ years for truly novel classes         │
  │                                                                 │
  │  WHO PRIORITY PATHOGENS (ESKAPE organisms):                     │
  │  E - Enterococcus faecium (VRE)                                 │
  │  S - Staphylococcus aureus (MRSA)                               │
  │  K - Klebsiella pneumoniae (carbapenem-resistant)               │
  │  A - Acinetobacter baumannii (pan-resistant strains exist)      │
  │  P - Pseudomonas aeruginosa (multi-drug resistant)              │
  │  E - Enterobacter spp. (ESBL/carbapenem-resistant)              │
  └─────────────────────────────────────────────────────────────────┘

  FUNDAMENTAL EVOLUTIONARY TRUTH:
  Any antibiotic use creates selective pressure for resistance.
  This is unavoidable — evolution happens.
  Goal: Slow resistance evolution; preserve antibiotic efficacy.
  This is a commons problem: individual benefit vs. collective harm.
```

---

## Resistance Mechanisms

```
  THE FOUR MECHANISMS OF ANTIBIOTIC RESISTANCE
  ==============================================

  1. ENZYMATIC INACTIVATION
  ┌────────────────────────────────────────────────────────────────┐
  │ β-LACTAMASES (most important class):                           │
  │   Cleave the β-lactam ring → inactivates all β-lactams         │
  │   Class A (serine-based): TEM-1, SHV, CTX-M (ESBL)             │
  │   Class B (metalloβ-lactamases): NDM-1, VIM, IMP               │
  │   → Use Zn²⁺; cleave carbapenems → pan-β-lactam resistance     │
  │   Class C (cephalosporinases): AmpC (inducible in Enterobacter)│
  │   Class D (OXA-type): OXA-48; carbapenem-hydrolyzing           │
  │                                                                │
  │ ESBLs (Extended-Spectrum β-Lactamases):                        │
  │   Mutant TEM/SHV or acquired CTX-M enzymes                     │
  │   → Cleave cephalosporins (not just penicillins)               │
  │   CTX-M-15: Most common ESBL globally; plasmid-borne           │
  │   Treatment: Carbapenems (if carbapenemase-negative)           │
  │                                                                │
  │ CPE (Carbapenemase-Producing Enterobacteriaceae):              │
  │   KPC (Klebsiella pneumoniae carbapenemase): Class A           │
  │   NDM-1 (New Delhi Metallo-β-lactamase): Class B; emerged 2009 │
  │   OXA-48: Class D; Mediterranean region + spreading globally   │
  │   Treatment: Ceftazidime-avibactam, meropenem-vaborbactam      │
  │   (avibactam: non-β-lactam β-lactamase inhibitor)              │
  │                                                                │
  │ AMINOGLYCOSIDE-MODIFYING ENZYMES:                              │
  │   APH (phosphotransferases), AAC (acetyltransferases),         │
  │   ANT (nucleotidyltransferases)                                │
  │   → Modify -OH or -NH₂ groups → disrupts ribosome binding      │
  └────────────────────────────────────────────────────────────────┘

  2. TARGET SITE MODIFICATION
  ┌────────────────────────────────────────────────────────────────┐
  │ MRSA (Methicillin-Resistant S. aureus):                        │
  │   Acquired mecA gene (SCCmec — staphylococcal cassette)        │
  │   Encodes PBP2a: Modified transpeptidase with low β-lactam     │
  │   affinity (Kd ~1,000x higher than normal PBPs)                │
  │   → ALL β-lactams ineffective (penicillin, methicillin, even   │
  │     "anti-MRSA" cephalosporins used for susceptible Staph)     │
  │   Treatment: Vancomycin, daptomycin, linezolid, ceftaroline    │
  │                                                                │
  │ VRE (Vancomycin-Resistant Enterococcus):                       │
  │   vanA/vanB genes: Modify peptidoglycan terminus               │
  │   Normal: D-Ala-D-Ala (vancomycin binds with high affinity)    │
  │   VanA: D-Ala-D-Lac (depsipeptide) → 1,000x reduced affinity   │
  │   VanB: D-Ala-D-Ser → ~7x reduced affinity (moderate level)    │
  │   Treatment: Linezolid, daptomycin, tigecycline                │
  │                                                                │
  │ RIFAMPICIN RESISTANCE (M. tuberculosis):                       │
  │   rpoB mutations: 81 bp core region of RNA polymerase β-sub.   │
  │   S531L most common → ~3x larger Km for rifampicin             │
  │   Rifampicin resistance = MDR-TB marker (implies INH res. too) │
  │                                                                │
  │ FLUOROQUINOLONE RESISTANCE:                                    │
  │   QRDR mutations: gyrA (DNA gyrase), parC (topoisomerase IV)   │
  │   S83L in GyrA most common in E. coli                          │
  │   QNRB (plasmid-mediated): Protects quinolone targets from     │
  │   quinolone binding                                            │
  └────────────────────────────────────────────────────────────────┘

  3. REDUCED DRUG ACCUMULATION (Efflux + Reduced Uptake)
  ┌────────────────────────────────────────────────────────────────┐
  │ EFFLUX PUMPS (major resistance mechanism):                     │
  │                                                                │
  │ 5 superfamilies:                                               │
  │   MFS (Major Facilitator Superfamily): TetA/TetB (tetracycline)│
  │   RND (Resistance-Nodulation-Division): Most important Gram-   │
  │   MATE (Multidrug/Oligo Exporter)                              │
  │   ABC (ATP-Binding Cassette): Uses ATP hydrolysis              │
  │   SMR (Small Multidrug Resistance): 4-helix; small molecules   │
  │                                                                │
  │ KEY EXAMPLES:                                                  │
  │ MexAB-OprM (P. aeruginosa): RND pump; broad spectrum           │
  │   Export: β-lactams, fluoroquinolones, aminoglycosides, biocide│
  │   Overexpressed in clinical isolates → multidrug resistance    │
  │                                                                │
  │ AcrAB-TolC (E. coli): Primary intrinsic MDR pump               │
  │   Constitutively expressed; overexpressed by marA regulator    │
  │                                                                │
  │ NorA (S. aureus): MFS pump; quinolone efflux                   │
  │                                                                │
  │ PORIN LOSS:                                                    │
  │   Gram-negative outer membrane porins (OmpF, OmpC in E. coli)  │
  │   Loss/downregulation → reduced drug entry                     │
  │   Combined with β-lactamase → high-level carbapenem resistance │
  └────────────────────────────────────────────────────────────────┘

  4. BYPASS / ALTERNATIVE PATHWAY
  ─ MRSA: Uses PBP2a → bypass normal PBPs that are β-lactam targets
  ─ Sulfonamide resistance: Acquire plasmid-encoded DHPS with low affinity
    OR overexpress normal DHPS (chromosomal promoter mutation)
  ─ Trimethoprim resistance: Acquire dhfr gene encoding low-affinity DHFR
    (dfr genes: >40 variants circulating globally on plasmids)
```

---

## Horizontal Gene Transfer and Resistance Spread

```
  HOW RESISTANCE GENES TRAVEL: THE MOBILE RESISTOME
  ===================================================

  RESISTANCE GENE MOBILITY HIERARCHY:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  INTEGRONS:          Capture gene cassettes (attI × attC)      │
  │  Class 1 integrons:  Most clinically important                 │
  │  → Can accumulate multiple resistance genes in tandem          │
  │                      ↓                                         │
  │  TRANSPOSONS:        Move integrons (+ other genes)            │
  │  Tn3 family, Tn10, Tn916: Cut-and-paste or copy-and-paste      │
  │  → Can relocate between plasmid ↔ chromosome                   │
  │                      ↓                                         │
  │  PLASMIDS:           Carry transposons; transfer by conjugation│
  │  Resistance plasmids: IncF, IncI, IncL/M, IncN types           │
  │  Conjugative plasmids: Self-transmissible (pKPN3, pOXA-48)     │
  │  Non-conjugative: Transfer via co-resident conjugative plasmid │
  │                      ↓                                         │
  │  CONJUGATION:        Plasmid → new bacterial cell              │
  │  Inter-species: E. coli → Klebsiella → Acinetobacter           │
  │  Rate: Can be minutes; faster than cell division               │
  │  Single conjugation event can make new host fully resistant    │
  └────────────────────────────────────────────────────────────────┘

  THE CTX-M STORY (historical example of resistance spread):
  ─ CTX-M β-lactamase: Originally from Kluyvera spp. chromosome
  ─ Mobilized onto plasmid → E. coli (1980s, South America)
  ─ IncF plasmid spread globally; CTX-M-15 variant emerged
  ─ By 2005: Most common ESBL globally in E. coli
  ─ Now: CTX-M-15 found in community UTI isolates worldwide
  ─ Timeline: ~20 years from obscure chromosomal gene → pandemic resistance

  NDM-1 (New Delhi Metallo-β-lactamase):
  ─ First identified 2009 (Swedish patient, Klebsiella from India)
  ─ Plasmid-borne (IncA/C, IncF types)
  ─ Transferred to E. coli, Klebsiella, Acinetobacter, Pseudomonas
  ─ Found on chromosome AND plasmid in Acinetobacter
  ─ Within 5 years: Global spread (50+ countries)
  ─ Plasmid carries: NDM-1 + ESBL + aminoglycoside resistance + more

  THE RESISTOME CONCEPT (D'Costa 2011):
  ─ Resistome = all resistance genes in all microbes (not just pathogens)
  ─ Natural antibiotic producers (Streptomyces) have self-resistance genes
  ─ Environmental bacteria carry resistance genes as normal function
    (housekeeping enzymes that happen to inactivate antibiotics)
  ─ These environmental resistance genes are the SOURCE of clinical genes
  ─ Soil β-lactamases predate clinical antibiotic use (ancient)
  ─ Implication: Resistance is not created by antibiotic use — it is SELECTED
```

---

## Specific Drug-Resistance Mechanisms by Drug Class

```
  ANTIBIOTIC CLASS RESISTANCE REFERENCE
  =======================================

  ┌──────────────────────────────────────────────────────────────────┐
  │ DRUG CLASS          MECHANISM                   KEY GENES        │
  │                                                                  │
  │ Penicillins/         β-lactamases (hydrolysis)  blaTEM, blaSHV   │
  │ Cephalosporins       PBP modification (MRSA)     mecA (PBP2a)    │
  │                      Porin loss + ESBL                           │
  │                                                                  │
  │ Carbapenems          Carbapenemases              blaKPC, blaNDM  │
  │                      Porin loss + AmpC           blaOXA-48       │
  │                                                                  │
  │ Glycopeptides        Target modification         vanA, vanB      │
  │ (Vancomycin)         (D-Ala-D-Ala → D-Ala-D-Lac)                 │
  │                                                                  │
  │ Fluoroquinolones     QRDR mutations (GyrA/ParC)  gyrA S83L       │
  │                      Efflux pump                 qnrB (plasmid)  │
  │                      QNRB (protects gyrase)                      │
  │                                                                  │
  │ Aminoglycosides      AMEs (modifying enzymes)    aac, aph, ant   │
  │                      16S rRNA methylases          armA, rmtB     │
  │                      (pan-aminoglycoside resist.)                │
  │                                                                  │
  │ Macrolides           23S rRNA methylation         erm genes      │
  │                      Efflux                       msrA           │
  │                      Target mutation                             │
  │                                                                  │
  │ Tetracyclines        Efflux                       tetA, tetB     │
  │                      Ribosomal protection         tetM, tetO     │
  │                      (TetM: GTPase mimics EF-G)                  │
  │                                                                  │
  │ Chloramphenicol      Acetyltransferase (CAT)      cat genes      │
  │                                                                  │
  │ Linezolid            23S rRNA mutation            G2576T         │
  │                      rRNA methylase               cfr            │
  │                                                                  │
  │ Colistin/Polymyxins  LPS modification (add        mcr-1 (2015)   │
  │ (last resort)        phosphoethanolamine to        plasmid-medi  │
  │                      lipid A)                     historic: PmrA │
  │                      mcr-1: First mobile colistin resistance     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## One Health and the Global Resistance Ecosystem

```
  ONE HEALTH FRAMEWORK
  =====================

  ONE HEALTH: Human health, animal health, environmental health are interconnected.
  Resistance does not respect these boundaries.

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │   HUMANS                    ANIMALS                            │
  │   (clinical use)            (veterinary + agriculture)         │
  │        ↕                          ↕                            │
  │            ENVIRONMENT                                         │
  │       (soil, water, food chain)                                │
  │                                                                │
  │   Resistance genes circulate through all three sectors         │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘

  AGRICULTURAL ANTIBIOTIC USE:
  ─ ~73% of global antibiotic consumption: Animals (WHO 2017)
  ─ Sub-therapeutic use (growth promotion): Banned in EU, US (since 2017)
    Still common in many countries
  ─ Veterinary therapeutics: Still major pressure
  ─ ESBL E. coli: Identical plasmids found in human clinical + poultry isolates
  ─ mcr-1 (colistin resistance): First found in Chinese pigs (2015)
    → Colistin used massively in Chinese veterinary medicine (growth promotion)
    → Within months: Found in human clinical isolates globally

  WASTEWATER AND ENVIRONMENTAL RESERVOIRS:
  ─ Hospital effluent: High concentration antibiotics + resistant bacteria
  ─ Wastewater treatment: Does NOT remove resistance genes reliably
  ─ Activated sludge: Hotspot for conjugation (HGT amplification)
  ─ Agricultural runoff: Antibiotics + resistant bacteria → soil → water
  ─ Rivers near industrial antibiotic production (India, China): Drug concentrations
    high enough to select resistance in environmental bacteria
  ─ NDM-1: Found in New Delhi municipal water supply (Walsh 2011)

  TRAVEL AND GLOBAL SPREAD:
  ─ Medical tourism: Common source of imported CPE
  ─ ESKAPE organisms: Travel faster than surveillance can track
  ─ ECDC data: Every EU country has CPE; ICU colonization rates rising
  ─ Air travel: Single traveler can import a new resistance gene

  ANTIMICROBIAL STEWARDSHIP (AMS):
  ─ Goal: Right drug, right dose, right duration, right indication
  ─ Key interventions: Diagnostic stewardship (test before treating)
    Formulary restriction, pre-authorization for broad-spectrum agents
    De-escalation when culture available (narrow based on sensitivities)
    Duration guidelines (5-day courses vs. historical 10–14 days)
  ─ Evidence: AMS programs reduce CDI rates, MRSA rates, resistance rates
  ─ Challenge: Physician behavior change; fear of undertreating
```

---

## Drug Development Pipeline Crisis

```
  WHY AREN'T THERE NEW ANTIBIOTICS?
  ===================================

  ECONOMIC MODEL FAILURE:
  ┌────────────────────────────────────────────────────────────────┐
  │ DEVELOPMENT COST:  $1–2 billion per approved antibiotic        │
  │ REVENUE PROBLEM:                                               │
  │   1. Usage should be MINIMAL (stewardship) → low sales volume  │
  │   2. New antibiotics are "last resort" → <5 years first line   │
  │   3. Short treatment courses (days, not lifetime like statins) │
  │   4. Rapidly developing resistance → short commercial life     │
  │   → RESULT: Economics don't work; no market incentive to invest│
  │                                                                │
  │ COMPARISON:                                                    │
  │   Statins (cholesterol): Daily, lifetime, $5/pill × millions   │
  │   Antibiotics: 7 days, once in 5 years, $10/course             │
  │   → No pharmaceutical incentive to develop new antibiotics     │
  └────────────────────────────────────────────────────────────────┘

  SCIENTIFIC CHALLENGES:
  ─ Easy targets taken: Most tractable bacterial targets already exploited
  ─ Gram-negative penetration: Outer membrane is extremely effective barrier
    Most compounds inhibit targets in vitro but can't reach them in vivo
  ─ Selectivity: Human cells have similar targets (ribosomes, DNA replication)
    Need pathogen-specific differences; hard to find novel ones

  PROPOSED SOLUTIONS:
  ┌────────────────────────────────────────────────────────────────┐
  │ PUSH INCENTIVES (government pays for R&D):                     │
  │   BARDA, CARB-X, GARDP: Public funding for early pipeline      │
  │   Billion-dollar grants to consortium (biopharmaceuticals)     │
  │                                                                │
  │ PULL INCENTIVES (guaranteed revenue):                          │
  │   UK NICE subscription model (2020s): Pay for access,          │
  │   not per-unit-sold; first-of-kind globally                    │
  │   US PASTEUR Act: Proposed subscription model                  │
  │                                                                │
  │ ALTERNATIVE STRATEGIES:                                        │
  │   Phage therapy: Bacteriophage cocktails; personalized for     │
  │   individual infection; FDA Expanded Access used in crisis     │
  │   Phase 1/2 trials ongoing                                     │
  │   Anti-virulence: Target virulence factors not growth          │
  │   → Less selective pressure (bacteria survive w/o virulence)   │
  │   CRISPR-based killing: Sequence-specific; antimicrobial use   │
  │   (see genomics/07-CRISPR.md for CRISPR technology)            │
  │   Antimicrobial peptides: Host defense peptides; synthetic     │
  │   Biofilm-specific: Quorum quenching (QQ) enzymes              │
  │                                                                │
  │ CURRENT PIPELINE:                                              │
  │   ~40 antibiotics in clinical development (2024)               │
  │   Most: Derivatives of existing classes                        │
  │   Truly novel mechanisms: Zoliflodacin (topoisomerase II       │
  │   inhibitor, different binding site from quinolones),          │
  │   Gepotidacin (similar); ALS-4                                 │
  └────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Concept | Key Point |
|---------|-----------|
| Most common Gram- resistance mechanism | β-lactamase production (blaTEM, CTX-M, NDM-1) |
| MRSA mechanism | mecA encodes PBP2a; low affinity for all β-lactams |
| VRE mechanism | vanA/vanB: D-Ala-D-Ala → D-Ala-D-Lac; vancomycin can't bind |
| Most dangerous carbapenemase | NDM-1 (metalloenzyme; not inhibited by avibactam) |
| First mobile colistin resistance | mcr-1 (from Chinese pigs; 2015; plasmid-borne) |
| How resistance genes really spread | Integron → transposon → plasmid → conjugation |
| What is the resistome? | All resistance genes in all microbes including environment |
| Agricultural antibiotic share | ~73% of global antibiotic consumption (animals) |
| Why no new antibiotic classes? | Market failure: short courses + stewardship = low revenue |
| UK solution to pipeline crisis | Subscription model: pay for access, not per-unit |
| Efflux pump in P. aeruginosa | MexAB-OprM (RND family); broad-spectrum export |
| Anti-virulence advantage | Less selective pressure; bacteria survive, just can't cause disease |

---

## Common Confusion Points

**Resistance vs. tolerance**: Resistance is genetic (stable minimum inhibitory concentration elevation; heritable). Tolerance is phenotypic (bacteria survive antibiotic exposure but MIC unchanged; not heritable). Biofilm cells and persisters are tolerant, not resistant. After dispersal from biofilm, cells recover normal susceptibility. This distinction matters because tolerance won't be detected by standard susceptibility testing (MIC testing uses actively growing planktonic cells).

**MRSA community vs. hospital strains**: Hospital-acquired MRSA (HA-MRSA) typically carries SCCmec type I-III (large cassettes; often multiply resistant). Community-acquired MRSA (CA-MRSA) carries SCCmec type IV-V (smaller cassettes; less multiply resistant but carries PVL toxin). USA300 is the dominant CA-MRSA clone in the US and causes skin/soft tissue infections in otherwise healthy people. Don't conflate these.

**MCR-1 and the "last resort" problem**: Colistin had essentially no clinical use for 30 years (too toxic) and resistance was only chromosomal (not transferable). Then colistin was heavily used in agriculture → selected mcr-1 on a conjugative plasmid → can now transfer colistin resistance to ANY Gram-negative. Colistin is now used clinically for pan-resistant Gram-negatives. MCR-1 + carbapenemase = pan-resistant E. coli (essentially untreatable).

**Why CTX-M beats TEM**: TEM-1 was the original plasmid-mediated β-lactamase. CTX-M (especially CTX-M-15) emerged from chromosomal gene mobilization and spread on conjugative IncF plasmids. CTX-M hydrolyzes third-generation cephalosporins more efficiently and is more stable on diverse plasmid backgrounds. By ~2010 it had displaced TEM/SHV as the dominant ESBL globally. This illustrates how resistance evolution is not always point mutations — gene transfer from unrelated organisms can bring in entirely novel enzymes.
