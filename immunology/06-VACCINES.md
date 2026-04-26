# Vaccines and Vaccination

## The Big Picture

```
VACCINE TYPES: AN EVOLUTIONARY TAXONOMY
=========================================

  GENERATION 1: WHOLE PATHOGEN (1796–present)
  ────────────────────────────────────────────
  Live-attenuated: Weakened version of pathogen
  Inactivated: Killed pathogen (whole particle)
  Pros: Strong immune response; cross-reactive epitopes
  Cons: Manufacturing complexity; safety risk; cold chain

  GENERATION 2: SUBUNIT / PURIFIED (1980s–present)
  ──────────────────────────────────────────────────
  Subunit: Purified protein(s) from pathogen
  VLP: Virus-like particles (protein shell, no genome)
  Conjugate: Polysaccharide + carrier protein
  Pros: Safe; defined antigen; no live pathogen
  Cons: Less immunogenic (need adjuvants); manufacturing complex

  GENERATION 3: NUCLEIC ACID (1990s–present, scaled 2020)
  ──────────────────────────────────────────────────────────
  DNA vaccines: Plasmid DNA expressing antigen
  mRNA vaccines: mRNA encoding antigen (in LNP)
  Pros: Rapid design (sequence → vaccine in weeks); no pathogen
  Cons: Requires delivery vehicle; cold chain (mRNA)
        mRNA: formerly poor delivery → LNP solved this

  GENERATION 4: VIRAL VECTOR (1990s–present)
  ────────────────────────────────────────────
  Adenoviral vector: Non-replicating adenovirus carrying antigen gene
  Pros: Strong cellular immunity; no live attenuated pathogen
  Cons: Pre-existing immunity to vector; manufacturing scale

  ┌──────────────────────────────────────────────────────────────────┐
  │ VACCINE          EXAMPLES             KEY INNOVATION             │
  │                                                                  │
  │ Live-attenuated  MMR, Yellow fever,   Most immunogenic vaccine   │
  │                  OPV, Varicella       type; mimics infection     │
  │                                                                  │
  │ Inactivated      Flu (IPV), Hep A,    Safer than live; needs     │
  │                  Rabies, IPV          boosters; adjuvant often   │
  │                                                                  │
  │ Subunit          Hep B, Pertussis,    Defined antigens; adjuvant │
  │                  HBsAg (recombinant)  critical                   │
  │                                                                  │
  │ VLP              HPV (Gardasil),       Mimics virus structure;   │
  │                  Hep B                no genetic material        │
  │                                                                  │
  │ Conjugate        PCV, MenACWY,        Polysaccharide + protein   │
  │                  Hib, MenB            → T cell help for memory   │
  │                                                                  │
  │ mRNA+LNP         COVID-19 (Pfizer,    Fastest design ever;       │
  │                  Moderna), Influenza   programmable platform     │
  │                                                                  │
  │ Adenoviral       COVID-19 (AZ, J&J),  Strong T cell response     │
  │ vector           Ebola, HIV trials     Pre-existing immunity risk │
  └──────────────────────────────────────────────────────────────────┘
```

---

## mRNA Vaccines: Deep Dive

```
  mRNA VACCINE PLATFORM
  ======================

  DESIGN SEQUENCE (from antigen sequence to vaccine):
  ┌────────────────────────────────────────────────────────────────┐
  │ 1. Pathogen genome sequenced (SARS-CoV-2: Jan 10, 2020)      │
  │ 2. Select target antigen (spike protein)                       │
  │ 3. Codon-optimize for human expression                         │
  │ 4. Stability modifications (proline substitutions in S2P)    │
  │ 5. In vitro transcription: DNA template → mRNA (IVT)         │
  │ 6. Encapsulate in LNP                                          │
  │ 7. First human dose: Day 66 after sequence release             │
  │    (Moderna Phase I: March 16, 2020)                           │
  └────────────────────────────────────────────────────────────────┘

  mRNA STRUCTURAL MODIFICATIONS:
  ┌────────────────────────────────────────────────────────────────┐
  │ 5' CAP (Cap1 modification):                                    │
  │   Required for ribosome recruitment + inhibits innate sensing  │
  │                                                                │
  │ 5' UTR: Optimized for translation initiation (alpha-globin)    │
  │                                                                │
  │ CODING SEQUENCE:                                               │
  │   Codon optimized for high human expression                    │
  │   Proline substitutions (K986P/V987P for BNT162b2):          │
  │   Locks spike in prefusion conformation (more immunogenic)     │
  │                                                                │
  │ 3' UTR: Stability elements (human beta-globin); multiple)      │
  │                                                                │
  │ POLY-A TAIL: Stability (100–120 A residues)                    │
  │                                                                │
  │ N1-METHYLPSEUDOURIDINE (m1Ψ) substitution:                     │
  │   All uridines replaced with m1Ψ                               │
  │   Dramatically reduces innate immune sensing via TLR7/8        │
  │   Increases translation efficiency ~10-fold                    │
  │   KEY INNOVATION by Karikó & Weissman (Nobel Prize 2023)       │
  └────────────────────────────────────────────────────────────────┘

  LNP (LIPID NANOPARTICLE) DELIVERY:
  ┌────────────────────────────────────────────────────────────────┐
  │ COMPOSITION (BNT162b2 example):                                │
  │   ALC-0315: Ionizable lipid (≈50 mol%)                         │
  │     - Neutral at pH 7.4 (blood) — reduces toxicity             │
  │     - Cationic at pH 4 (endosome) — helps endosomal escape   │
  │   DSPC: Phospholipid stabilizer (≈10 mol%)                     │
  │   Cholesterol: Membrane stability (≈38 mol%)                   │
  │   PEG-DMG: Steric stabilization, prevents aggregation (≈2%)    │
  │   mRNA: Encapsulated in core                                   │
  │   Size: ~80–100 nm nanoparticle                                │
  │                                                                │
  │ ENDOSOMAL ESCAPE MECHANISM:                                    │
  │   LNP internalized by macropinocytosis/receptor-mediated       │
  │   In endosome (pH drops): ionizable lipid protonated           │
  │   → disrupts endosomal membrane → mRNA released to cytoplasm   │
  │   mRNA translated by ribosomes → spike protein produced        │
  │   Spike protein: Displayed on cell surface (MHC I + surface) │
  │   → CD8 T cell recognition + antibody production             │
  └────────────────────────────────────────────────────────────────┘

  INNATE IMMUNE SENSING OF mRNA:
  ┌────────────────────────────────────────────────────────────────┐
  │ This is both the challenge AND part of why mRNA works:         │
  │                                                                │
  │ SENSING RECEPTORS:                                             │
  │   TLR7 (endosomal): ssRNA → detect mRNA in endosome          │
  │   TLR8 (endosomal): ssRNA → similar to TLR7                  │
  │   RIG-I (cytoplasmic): Detects dsRNA contaminants            │
  │   MDA5 (cytoplasmic): Long dsRNA (IVT byproducts)            │
  │                                                                │
  │ RESPONSE: Type I IFN + proinflammatory cytokines               │
  │   → Activation of DCs at injection site                        │
  │   → Innate immune activation → ADJUVANT EFFECT               │
  │                                                                │
  │ m1Ψ modification: Reduces TLR7/8 sensing → less innate alarm │
  │ BUT: LNP itself (ionizable lipid + PEG) still acts as adjuvant│
  │   → IL-6, TNF at injection site → local reaction (arm pain)  │
  │                                                                │
  │ NET RESULT: Controlled innate activation → DC maturation       │
  │   → T cell priming WITHOUT overwhelming inflammation           │
  └────────────────────────────────────────────────────────────────┘
```

---

## Adjuvants

```
  ADJUVANTS: THE DANGER SIGNAL COMPONENT
  =========================================

  PROBLEM: Purified protein alone → poor immunogenicity
  REASON: No PAMPs → innate not activated → DC doesn't mature
          → no co-stimulatory molecules → T cell anergy

  SOLUTION: Adjuvant = artificial "danger signal" to activate innate
            → DC maturation → co-stimulation → strong adaptive response

  ADJUVANT MECHANISMS:
  ┌──────────────────────────────────────────────────────────────┐
  │ DEPOT EFFECT: Hold antigen at injection site                 │
  │   Alum crystals: Antigen adsorbs → slow release              │
  │   → prolonged antigen availability to APCs                   │
  │                                                              │
  │ DIRECT INNATE ACTIVATION:                                    │
  │   Alum: Activates NLRP3 inflammasome → IL-1β               │
  │   MPLA (Monophosphoryl lipid A): TLR4 agonist (non-toxic LPS)│
  │   CpG ODN: TLR9 agonist → Th1 response                     │
  │   QS-21 (saponin): Unknown mechanism → strong CD8 T cells  │
  │                                                              │
  │ FORMULATION EFFECTS:                                         │
  │   Oil emulsions (MF59, AS03): Activates NLRP3, recruits      │
  │   monocytes/DCs → stronger than alum for flu               │
  └──────────────────────────────────────────────────────────────┘

  MAJOR ADJUVANT SYSTEMS:
  ┌────────────────────────────────────────────────────────────────┐
  │ ALUM (aluminum salts):  Most widely used; safe; Th2 bias     │
  │   Used in: HBV, Hep A, HPV (Gardasil), DTP                  │
  │                                                                │
  │ AS01B (GSK):           MPL (TLR4) + QS-21 (saponin)         │
  │   Used in: RTS,S (malaria), SHINGRIX (VZV subunit)           │
  │   Very strong T cell + antibody response                     │
  │                                                                │
  │ AS04 (GSK):            Alum + MPL                            │
  │   Used in: Cervarix (HPV), HBsAg (hepatitis B)               │
  │                                                                │
  │ MF59 (Seqirus):        Squalene emulsion                     │
  │   Used in: Fluad (elderly flu vaccine)                       │
  │   Stronger immune response than alum                         │
  │                                                                │
  │ AS03 (GSK):            Squalene + α-tocopherol               │
  │   Used in: Pandemic flu vaccines (H1N1 2009); COVID-19       │
  │                                                                │
  │ LNP (lipid nanoparticle): mRNA vaccines — LNP acts as adjuv. │
  │   Ionizable lipid → IL-6 at injection site → DC activation  │
  └────────────────────────────────────────────────────────────────┘
```

---

## Vaccine Immunology: How Immunity Develops

```
  VACCINE-INDUCED IMMUNITY TIMELINE
  ===================================

  PRIME (1st dose):
  Day 0: Antigen + adjuvant injected
  Hour 0–24: Innate activation at injection site
    Local DC maturation; cytokine/chemokine release
  Day 1–4: DC migration to draining lymph node
    Antigen presentation to naïve T and B cells
  Day 4–7: Clonal expansion of antigen-specific T and B cells
  Day 7–14: Germinal center formation; IgM → IgG class switch
  Day 14: Antibody titer begins to rise
  Day 28: Peak primary response (antibody + T cells)
  Day 28–60: Contraction; most effectors die
  Month 2+: Memory cells + long-lived plasma cells persist

  BOOST (2nd dose, often day 21–28):
  Antigen seen by large pool of primed cells
  Rapid GC reaction → affinity maturation continues
  1,000x more memory cells than pre-prime
  Antibody titer 10–100x higher than after prime
  Isotype shift: IgG4 fraction increases (less inflammatory)

  CORRELATES OF PROTECTION:
  Not all vaccines have well-defined correlates.
  ┌────────────────────────────────────────────────────────────┐
  │ Measles: IgG >200 mIU/mL → protected                     │
  │ HBV: Anti-HBsAg >10 mIU/mL → protected                   │
  │ Flu: Hemagglutination inhibition (HI) titer >1:40 → 50%  │
  │ COVID: No single threshold; neutralization titers proxy    │
  │ Pertussis: Unclear; cellular immunity may matter more      │
  └────────────────────────────────────────────────────────────┘
```

---

## Herd Immunity

```
  HERD IMMUNITY THRESHOLD
  =========================

  CONCEPT: If enough individuals are immune, transmission chain
           breaks → pathogen cannot sustain outbreak.

  BASIC REPRODUCTIVE NUMBER (R₀): Average infections per case
  in fully susceptible population.

  HERD IMMUNITY THRESHOLD (HIT):
  HIT = 1 - (1/R₀)

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────┐
  │ Pathogen       R₀ (range)   HIT          Notes              │
  │ Measles        12–18        ~92–94%       Very hard to reach│
  │ Mumps          4–7          ~75–86%                         │
  │ Rubella        5–7          ~80–86%                         │
  │ Smallpox       5–7          ~80–86%      Eradicated 1980    │
  │ COVID-19       2–6 (alpha)  ~50–83%      Variants changed R₀│
  │ Influenza      1.2–3        ~17–67%       Annual vaccine    │
  │ Polio          5–7          ~80–86%       Near eradication  │
  └─────────────────────────────────────────────────────────────┘

  VACCINE EFFICACY vs. VACCINE EFFECTIVENESS:
  Efficacy: Controlled trial; VE = 1 - (ARR/ARU) (controlled)
  Effectiveness: Real-world population surveillance
  Efficacy ≥ effectiveness (real world: heterogeneous pop, waning)

  WANING IMMUNITY:
  All vaccines have some degree of waning.
  Influenza: Wanes within one season → annual vaccine
  COVID-19: Neutralizing Abs wane 3–6 months; T/B cell memory persists
  HBV: Booster often not needed (B cell memory responds if titer drops)
  Waning of serum Ab ≠ loss of protection — memory matters
```

---

## Vaccine Failure Modes

```
  WHY VACCINES FAIL (SOMETIMES)
  ================================

  PRIMARY FAILURE: Vaccine never induced immunity
  ─ Recipient: immunocompromised, maternally-derived Ab interference
  ─ Vaccine: cold chain break, poor adjuvant, wrong antigen

  SECONDARY FAILURE (WANING): Immunity was induced, then waned
  ─ Antibody decay below protective threshold
  ─ Memory cells still present; response on re-exposure (faster)
  ─ Pertussis: Acellular vaccine protection wanes faster than whole-cell

  ANTIGENIC VARIATION / ESCAPE:
  ─ Pathogen mutates antigens targeted by vaccine-induced Abs
  ─ Influenza: Rapid HA/NA evolution → annual reformulation
  ─ COVID: Omicron BA.4/5 → significant neutralization escape
  ─ HIV: Hypervariable envelope → no effective vaccine yet

  IMMUNOSENESCENCE:
  ─ Elderly people respond poorly to vaccines (thymic involution)
  ─ Solution: Higher-dose influenza vaccine for >65 yr
             Adjuvants (MF59 in Fluad) to boost response
             AS01B in SHINGRIX (97% efficacy even in >80 yr)

  ORIGINAL ANTIGENIC SIN:
  ─ Memory from first exposure dominates future responses
  ─ Exposure to related strain → boosts memory to ORIGINAL strain
  ─ Problem for universal flu vaccine design
```

---

## Decision Cheat Sheet

| Scenario | Vaccine Approach |
|----------|-----------------|
| Need durable sterilizing immunity | Live-attenuated (if safe) |
| Immunocompromised recipient | Inactivated or subunit (no live) |
| Need rapid design for new pathogen | mRNA+LNP platform |
| Strong cellular (T cell) immunity | Viral vector or mRNA |
| Mucosal immunity (respiratory tract) | Intranasal, oral (if available) |
| Polysaccharide antigen (encapsulated bacteria) | Conjugate vaccine |
| Need AS01B-level T cell response | AS01B adjuvant system |
| Elderly population, poor response | Higher-dose or adjuvanted formulation |
| Pregnancy (maternal Abs to neonate) | IgG-generating vaccine (e.g., RSV mRNA) |
| Waning immunity issue | Annual booster or reformulation |

---

## mRNA Platform and Adjuvants as Programmable Systems

```
mRNA VACCINE PLATFORM ↔ PROGRAMMABLE BUILD SYSTEM
──────────────────────────────────────────────────────────────────────────────
TRADITIONAL VACCINE (whole pathogen/protein):
  = Bespoke compiled artifact
  Each vaccine is a separate manufacturing effort tied to a specific pathogen
  Requires growing the pathogen or expressing the protein — different build chain
  per target
  Time to first dose: years

mRNA PLATFORM (BNT162b2, mRNA-1273, Spikevax):
  = Programmable compiler + runtime
  The delivery system (LNP + mRNA backbone + modifications) is fixed
  Only the CODING SEQUENCE changes per target
  New pathogen → sequence it → design spike CDS → synthesize mRNA → done
  Time to first human dose for COVID-19: 66 days from genome publication

  ANALOGY:
  LNP + backbone    ↔  Build toolchain (compiler + runtime + standard library)
  mRNA CDS          ↔  Source file (.cpp → compile → executable antigen)
  Codon optimization ↔  Profile-guided optimization for target expression system
  N1-methylpseudo-U ↔  Flag to suppress immune detection of the build artifact
                        (like signing + obfuscation to bypass AV heuristics)
  Proline mutations  ↔  Structural constraint at compile time (prefusion lock)
  5'/3' UTR         ↔  Startup/shutdown hooks; polyA tail = cache lifetime hint

  DEPLOYMENT:
  LNP = container image with runtime; mRNA = the payload
  Injection site = production deployment; endosome = package manager install
  Ionizable lipid (pH-dependent) = auto-shutdown after delivery (LNP dissociates)

  SCALING ADVANTAGE:
  Once you have the platform, incremental new targets are O(days) not O(years)
  This is the platform vs. bespoke software engineering distinction
  BioNTech now has mRNA pipeline for flu, HIV, cancer (neoantigen), CMV, RSV

ADJUVANTS ↔ DEPENDENCY INJECTION OF RUNTIME CONTEXT
──────────────────────────────────────────────────────────────────────────────
PROBLEM:
  Pure protein antigen → no PAMP → innate receptors not triggered → DCs
  don't mature → no co-stimulation → T cell anergy (Signal 2 missing)
  The payload (antigen) cannot generate its own activation context

SOLUTION — ADJUVANT = INJECTED DEPENDENCY:
  Adjuvant provides the "danger signal" context that the antigen payload
  cannot generate itself
  DC = the dependent service that requires activation context to function
  Adjuvant = config/environment injection at deploy time

  ALUM:
    NLRP3 inflammasome activation → IL-1β
    Depot effect: antigen slow-release from alum crystal surface
    = Configuration: long-running process with state (antigen cache)

  AS01B (MPL + QS-21):
    TLR4 agonist + saponin → very strong Th1 + CD8 response
    = Two-dependency injection: TLR4 pathway + NLRP3/unknown QS-21 pathway
    = Constructor injection with two required dependencies

  LNP (mRNA vaccine adjuvant):
    Ionizable lipid → IL-6 at injection site → DC activation
    The delivery vehicle IS the adjuvant — bundled as inseparable module
    = In-process dependency: no need to inject separately; part of the artifact

  THEORETICAL PERFECT ADJUVANT = dependency injection framework:
    Inject exactly the innate activation context needed for the desired response
    (Th1 vs. Th2 vs. CD8 vs. mucosal) without excess systemic inflammation
    Current adjuvants: somewhat blunt; AS01B is the precision leader
──────────────────────────────────────────────────────────────────────────────
```

## Common Confusion Points

**mRNA vaccines don't alter DNA**: mRNA is translated in the cytoplasm by ribosomes. It cannot enter the nucleus (mRNA is inherently unstable and rapidly degraded — typical cellular mRNA half-life is minutes to hours). There is no mechanism by which mRNA could integrate into genomic DNA in the absence of reverse transcriptase (which mRNA vaccines don't include).

**Live-attenuated vaccines in immunocompromised**: A vaccine strain that is harmless in immunocompetent people can cause severe disease in those with T cell or combined immunodeficiency. MMR, VZV, OPV, and YF vaccines are contraindicated in severe immunodeficiency. This is not just caution — vaccine-derived polio paralysis occurs in immunodeficient people given OPV.

**Herd immunity threshold assumes homogeneous mixing**: The simple HIT = 1 - 1/R₀ formula assumes random mixing. Real populations have: network structure, superspreaders, age-stratified contact, geographic clustering. Effective herd immunity can be achieved at lower apparent coverage if the vaccinated population is strategically distributed, or requires higher coverage if clusters of unvaccinated individuals form.

**IgM first vs. IgG later**: Primary response = IgM first, then class switch to IgG. Secondary response (vaccine boost or re-infection) = rapid IgG (memory B cells are already isotype-switched). Measuring only IgG in a post-vaccine titer study at 4 weeks will show IgG from the primary response, not just IgM — the switch happens by then.
