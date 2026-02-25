# Viral Replication Cycles

## The Big Picture

All viral replication cycles share the same phases: attachment, entry, uncoating,
genome expression, genome replication, assembly, and release. The specifics differ
dramatically by Baltimore class and host cell compartment.

```
┌──────────────────────────────────────────────────────────────────┐
│                UNIVERSAL REPLICATION CYCLE                        │
│                                                                    │
│  1. ATTACHMENT  ────→  Viral surface protein binds host receptor  │
│                                                                    │
│  2. ENTRY       ────→  Membrane fusion or endocytosis             │
│                                                                    │
│  3. UNCOATING   ────→  Genome released into cytoplasm/nucleus     │
│                                                                    │
│  4. GENE        ────→  Early genes: replication enzymes,          │
│     EXPRESSION          immune evasion                            │
│                         Late genes: structural proteins           │
│                                                                    │
│  5. GENOME      ────→  Replication using viral enzymes + host     │
│     REPLICATION         (location depends on Baltimore class)     │
│                                                                    │
│  6. ASSEMBLY    ────→  Capsid + genome packaging                  │
│                                                                    │
│  7. RELEASE     ────→  Lysis (non-enveloped) or budding           │
│                         (enveloped)                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Detailed Cycle 1: Herpesvirus (dsDNA, Class I)

HSV-1 as the paradigm for nuclear-replicating dsDNA virus.

```
  ATTACHMENT & ENTRY:
  ────────────────────
  Virion surface: gC/gB binds heparan sulfate (initial tethering)
                  gD binds entry receptors: nectin-1, HVEM, or 3-O-sulfated HS
  Fusion: gB + gH/gL complex catalyze membrane fusion at plasma membrane (neurons)
          or in endosome (non-neuronal cells)
  After fusion: capsid + tegument proteins released into cytoplasm

  TRANSPORT TO NUCLEUS:
  ──────────────────────
  Capsid travels on microtubules (dynein motor) toward nucleus
  Capsid docks at nuclear pore complex
  Viral DNA injected into nucleus (capsid remains outside — "docking")

  NUCLEAR GENE EXPRESSION — THREE KINETIC WAVES:
  ─────────────────────────────────────────────────
  Immediate early (IE, α): 0-2 hours post-infection
    Activated by VP16 tegument protein (comes in with virion)
    ICP4: master transactivator; ICP0: counteracts host restriction
    Function: prepare nucleus for viral takeover; evade restriction factors

  Early (E, β): 2-6 hours
    DNA replication enzymes: viral DNA pol (UL30), helicase-primase,
    UL12 (DNase), thymidine kinase (HSV TK — target of acyclovir)
    Function: replicate viral DNA

  Late (L, γ): 6-18 hours
    Structural proteins: VP5 (capsid), gB, gC, gD, gH, gL, etc.
    Depends on DNA replication (γ1: partially dependent; γ2: strictly dependent)

  DNA REPLICATION:
  ──────────────────
  Origin of replication: oriS or oriL on the viral genome
  Rolling circle amplification: linear genome circularizes → rolling circle
  → concatemers of tandemly repeated genomes → cleaved during packaging

  CAPSID ASSEMBLY & NUCLEAR EGRESS:
  ────────────────────────────────────
  Capsid assembled in nucleus around scaffold proteins
  DNA packaged by terminase complex (cleaves concatemers at packaging signal)
  Primary envelopment: capsid buds through inner nuclear membrane
  De-envelopment: fuses with outer nuclear membrane
  Secondary envelopment: tegument + envelope acquired in trans-Golgi network
  Vesicle transport to plasma membrane → exocytosis

  Timeline: ~18-24 hours full cycle; ~1,000-5,000 virions per cell

  LATENCY:
  ─────────
  In sensory neurons: viral DNA maintains as episome (not integrated, not replicating)
  Only LAT (latency-associated transcript) expressed
  Reactivation: triggered by stress, UV, fever, immunosuppression
  VP16 re-enters, IE genes activated → lytic cycle restarts in neuron →
  anterograde transport to skin/mucosa → recurrent lesion
```

---

## Detailed Cycle 2: Coronavirus / SARS-CoV-2 (+ssRNA, Class IV)

```
  ATTACHMENT:
  ──────────
  Spike (S) protein: S1 subunit binds ACE2 (angiotensin-converting enzyme 2)
  ACE2 expressed on: lung alveolar type II cells, intestinal enterocytes,
  nasal epithelium, cardiac endothelium, kidney
  This distribution predicts organ tropism (lung, gut, cardiovascular)

  ENTRY PATHWAY:
  ──────────────
  Route 1 (surface fusion, preferred): TMPRSS2 serine protease cleaves S at
    S2' site → membrane fusion at plasma membrane → fast, efficient
  Route 2 (endosomal): endocytosis → cathepsin L/B cleave S in late endosome →
    slower; used when TMPRSS2 absent

  GENOME RELEASE & TRANSLATION:
  ───────────────────────────────
  +ssRNA genome (29.9 kb for SARS-CoV-2) released into cytoplasm
  Ribosome translates ORF1ab immediately:
  - ORF1a: pp1a polyprotein (~500 kDa)
  - ORF1ab: pp1ab (~800 kDa) via ribosomal -1 frameshift at a specific slippery sequence
  3CL protease (Mpro, nsp5) and PL protease (nsp3) cleave polyprotein into 16 nsps

  KEY NSPs:
  ──────────
  nsp3: papain-like protease (PLpro) — deubiquitinase, interferon antagonist
  nsp5: 3CL protease (Mpro) — main protease, cleaves polyprotein — TARGET OF PAXLOVID
  nsp12: RNA-dependent RNA polymerase (RdRp) — TARGET OF REMDESIVIR
  nsp13: helicase
  nsp14: N7-methyltransferase + 3'-5' exonuclease (proofreading — unusual for RNA virus)
  nsp15: endonuclease (immune evasion: cleaves dsRNA to avoid MDA5 detection)

  REPLICATION COMPLEX FORMATION:
  ───────────────────────────────
  nsp3, nsp4, nsp6 remodel ER membranes → double-membrane vesicles (DMVs)
  DMVs serve as replication organelles (shield dsRNA from cytosolic sensors)
  RdRp in DMV synthesizes -strand from +strand → dsRNA
  -strand serves as template → new +strand genomes

  SUBGENOMIC mRNAs (sgRNAs):
  ──────────────────────────
  Coronavirus uses discontinuous transcription (unique mechanism):
  Short sgRNAs encode structural (S, E, M, N) and accessory proteins
  Each sgRNA has identical 5' leader + unique body
  Mechanism: RdRp "jumps" from body transcription-regulatory sequence (TRS)
  to 5' leader TRS → produces nested set of sgRNAs
  Approximately 9 sgRNAs in SARS-CoV-2

  ASSEMBLY AND BUDDING:
  ──────────────────────
  Nucleocapsid (N protein + genomic RNA) assembled in cytoplasm
  S, E, M glycoproteins targeted to ER-Golgi intermediate compartment (ERGIC)
  Budding occurs into ERGIC lumen (internal budding)
  → Vesicle transport to plasma membrane → exocytosis

  SARS-CoV-2 specific: Spike furin cleavage site (PRRAR↓S) between S1 and S2
  Furin is ubiquitous → wider cell tropism vs. SARS-CoV-1 (no furin site)

  Timeline: ~8-12 hours replication cycle; ~10²-10⁶ particles per cell
```

---

## Detailed Cycle 3: HIV (ssRNA-RT, Class VI)

```
  ATTACHMENT & ENTRY:
  ────────────────────
  gp120 binds CD4 (expressed on CD4+ T cells, macrophages, DCs)
  Co-receptor binding: gp120 conformational change exposes V3 loop
    → Binds CCR5 (macrophages, early HIV) or CXCR4 (late HIV, T cells)
    CCR5Δ32 homozygotes: natural resistance to HIV-1 (Berlin patient)
  gp41 HR1/HR2 hairpin formation → hemifusion → complete membrane fusion

  REVERSE TRANSCRIPTION:
  ───────────────────────
  RT (p66/p51 heterodimer) packaged in virion
  Reverse transcription begins in cytoplasm:
  1. tRNA-Lys3 primed at PBS → minus-strand DNA synthesis (RNase H degrades RNA template)
  2. First strand transfer: minus-strand DNA jumps to 3' end via LTR
  3. Plus-strand synthesis primed by PPT (polypurine tract)
  4. Second strand transfer → complete dsDNA with LTRs at both ends

  Error rate: ~3×10⁻⁵ per base per cycle (no proofreading)
  9,749 bp genome → ~0.3 errors per genome per cycle → nearly every new virus differs slightly

  NUCLEAR IMPORT:
  ────────────────
  HIV pre-integration complex (PIC) actively transported through nuclear pore
  (Unlike murine retroviruses which can only infect dividing cells)
  Enables infection of non-dividing cells (macrophages, neurons)

  INTEGRATION:
  ─────────────
  Integrase (IN): 3'-processing (removes 2 nt from each LTR end)
                 Strand transfer: inserts viral dsDNA into host chromosome
  Integration is semi-random but favors: actively transcribed genes, gene bodies
  (in contrast to gammaretroviruses which favor promoters — relevant for gene therapy safety)

  PROVIRAL TRANSCRIPTION:
  ────────────────────────
  Proviral LTR contains strong promoter with NF-κB and TATA box
  RNA Pol II transcribes the provirus, but produces short abortive transcripts
  Tat protein: binds TAR RNA stem-loop at 5' end of nascent viral RNA
              → Recruits P-TEFb (CDK9/Cyclin T1)
              → Phosphorylates RNAPII CTD → elongation → full-length mRNA
  Without Tat: basal transcription only; this is how latency is maintained
  (resting CD4+ T cells: low NF-κB, low P-TEFb → Tat can't amplify → latent)

  ALTERNATE SPLICING PATTERN:
  ────────────────────────────
  Unspliced (9.4 kb): gag-pol mRNA + genomic RNA
  Singly spliced: env, vif, vpr, vpu mRNAs
  Multiply spliced: tat, rev, nef mRNAs (early, before Rev is made)
  Rev: binds RRE (Rev response element) in unspliced/singly-spliced RNA
       → exports them from nucleus via CRM1
       Without Rev: only multiply-spliced mRNAs exported (regulatory loop)

  ASSEMBLY AND BUDDING:
  ──────────────────────
  Gag polyprotein drives assembly: targets plasma membrane (MA domain + PI(4,5)P2)
  Gag forms spherical immature lattice at membrane
  Two genomic RNA copies packaged (via NC-ψ interaction, packaging signal ψ)
  ESCRT pathway recruited (via Gag p6 PTAP motif) for membrane scission
  After budding: PR (protease) cleaves Gag → MA, CA, NC, p6
  CA reassembles into conical capsid → mature infectious virion
  (HIV maturation inhibitors: lenacapavir — clinically approved)

  Timeline: ~24-48 hours full cycle; ~2,000-10,000 virions per cell per day
  CD4 T cell half-life in HIV infection: ~1 day
  Plasma virus turnover: 10⁹-10¹⁰ virions per day in untreated infection
```

---

## Detailed Cycle 4: Influenza (-ssRNA, Class V, Segmented)

```
  ATTACHMENT:
  ──────────
  HA (hemagglutinin) binds sialic acid residues on surface glycoproteins
  Human flu: α-2,6-linked sialic acid (upper respiratory tract)
  Bird flu: α-2,3-linked sialic acid (lower respiratory, gut)
  This receptor preference explains host range — and why H5N1 and H7N9
  don't spread efficiently between humans (bind only α-2,3 sialic acid in humans)

  ENTRY: ENDOCYTOSIS + MEMBRANE FUSION:
  ───────────────────────────────────────
  Virus endocytosed; endosome acidified
  HA2: pH-dependent conformational change at pH ~5-6
  → Fusion peptide inserts into endosomal membrane → hemifusion → fusion pore
  → Viral RNPs (8 segments, each coated in NP + RdRp complex) released

  NUCLEAR IMPORT AND TRANSCRIPTION:
  ─────────────────────────────────────
  RNPs actively imported into nucleus (NLS on NP)
  Viral RdRp (PA-PB1-PB2 heterotrimer) transcribes each segment:
  PB2: cap-snatching — binds 5' cap of host pre-mRNA → PA endonuclease cuts 10-14 nt
       from host mRNA → viral RdRp uses these as primers for viral mRNA synthesis
       (UNIQUE MECHANISM — disrupts host mRNA maturation; targets nuclear cap-binding)
  Each segment transcribed to polyadenylated mRNA
  PB1-F2: proapoptotic; promotes mitochondrial membrane depolarization
  NS1: interferon antagonist — sequesters dsRNA, inhibits RIG-I, blocks PKR

  REPLICATION (new genomes):
  ──────────────────────────
  NP accumulation → switch from mRNA synthesis to genomic replication
  Template: -strand → +strand (cRNA, not polyadenylated)
  cRNA template → new -strand genomes (packaged in RNPs)

  ASSEMBLY AND BUDDING:
  ──────────────────────
  New RNPs exported from nucleus via CRM1
  HA, NA, M2 targeted to lipid rafts at apical plasma membrane
  M1 (matrix protein) bridges RNPs and membrane
  8 RNPs specifically incorporated (selection signal at each segment end)
  Bud forms; M2 ion channel required for membrane scission (target of amantadine)
  NA cleaves sialic acid from cell surface → allows virion to be released
    (Without NA cleavage: virions aggregate on cell surface → no spread)
    (Oseltamivir/zanamivir inhibit NA → block release)

  REASSORTMENT:
  ──────────────
  Two influenza strains infecting same cell:
  → 8+8 = 16 segment pool → random packaging → 2⁸ = 256 possible combinations
  → Antigenic shift: entirely new HA/NA combination
  1957 H2N2: human H1N1 + avian virus contributed PB1, HA, NA
  1968 H3N2: H2N2 background; avian HA and PB1 genes
  2009 H1N1: 4-way reassortant (human + swine + avian + North American swine)
```

---

## Lytic vs. Lysogenic: Bacteriophage Lambda

```
  LYTIC cycle: phage replicates, lyses cell, releases ~100 phage
  Lysogenic cycle: phage integrates into bacterial chromosome, replicates silently

  DECISION SWITCH (CI/Cro repressors):
  ──────────────────────────────────────
  High CI: lysogenic (CI represses lytic genes including cro)
  High Cro: lytic (Cro represses CI)

  Environmental conditions that favor lysis:
  - Low MOI (multiplicity of infection)
  - High nutrient / fast-growing bacteria
  - UV damage (activates SOS response → RecA cleaves CI → lytic switch)

  Lysogeny favors:
  - High MOI (lytic cycle would re-infect lysogen)
  - Slow-growing, stressed bacteria (better to wait)

  This is a genetic bistable switch — a toggle flip-flop at the molecular level.
  Bridge: CI/Cro switch is one of the original models for bistable gene networks
  in synthetic biology. It was the template for early genetic toggle switch designs
  in the Gardner et al. 2000 Nature paper.
```

---

## Decision Cheat Sheet

| Virus class | Replication location | Key enzyme(s) | Timeline |
|-------------|---------------------|---------------|----------|
| Herpesvirus (dsDNA) | Nucleus | Host RNA pol; viral DNA pol | 18-24 h |
| Poxvirus (dsDNA) | Cytoplasm | Viral RNA pol + DNA pol | 12-24 h |
| Coronavirus (+ssRNA) | Cytoplasm (DMVs) | RdRp, nsp14 ExoN | 8-12 h |
| Poliovirus (+ssRNA) | Cytoplasm | RdRp | ~6 h |
| Influenza (-ssRNA) | Nucleus + cytoplasm | RdRp, cap-snatching | 6-8 h |
| Ebola (-ssRNA) | Cytoplasm | RdRp | 72+ h |
| HIV (ssRNA-RT) | Cytoplasm → nucleus | RT, integrase | 24-48 h |

---

## Common Confusion Points

**Reverse transcription does not occur in the host nucleus.** HIV RT converts RNA to
DNA in the cytoplasm (in the reverse transcription complex). The dsDNA then enters
the nucleus as the pre-integration complex. RT is complete before nuclear entry.

**Influenza replication requires nuclear entry (unlike most RNA viruses).** Because
influenza requires cap-snatching from host pre-mRNAs (which are in the nucleus),
and because new RNPs must return to nucleus for amplification, influenza replication
is nuclear-dependent. Most +ssRNA viruses replicate entirely in the cytoplasm.

**The burst size and replication cycle time are separate concepts.** Poliovirus
completes a cycle in 6 hours (fast); herpes completes in 18-24 hours (slow).
But herpes produces more virions per cell at peak (due to larger genome and more
complex assembly). The quantity of virus in infection depends on both cycle time
and burst size, plus the number of infected cells.

**Latency is not the same as defective infection.** In herpesvirus latency, the virus
is alive, episomal, and capable of reactivation. In HIV latency, the provirus is
integrated and silenced by epigenetic mechanisms. In bacteriophage lysogeny, the
phage DNA is integrated. These are mechanistically different states that all have
in common the absence of active viral replication.
