# Fertilization, Cleavage, and Blastulation

## The Big Picture

The first developmental events — fertilization, cleavage, and blastulation — transform a single diploid cell into a multicellular structure with its first differentiated cell populations. The key transitions: activation of the embryonic genome, establishment of embryonic vs extraembryonic lineages, and formation of the pluripotent inner cell mass.

```
+──────────────────────────────────────────────────────────────────+
|          FERTILIZATION → CLEAVAGE → BLASTULATION                 |
|                                                                  |
|  FERTILIZATION     CLEAVAGE          BLASTULATION               |
|  Day 0             Days 1-3           Days 3-5                  |
|  ─────────────     ──────────────     ──────────────────         |
|  Sperm + egg →     Mitotic divisions  Morula → Blastocyst       |
|  Zygote            No cell growth     Compaction (E-cadherin)   |
|  Egg activation    Rapid cycling      ICM (embryo) vs TE        |
|  Meiosis II        Totipotent → ?     (placenta)                |
|  completion        maternal → zyg.    Cavitation → blastocoel   |
|                    genome transition  Implantation Day 5-7       |
+──────────────────────────────────────────────────────────────────+
```

---

<!-- @editor[bridge/P2]: No CS/engineering bridge anywhere in this guide. The maternal-to-zygotic transition is a natural "bootstrap loader" analogy — maternal mRNA is firmware, EGA is the OS kernel taking over. The polyspermy block maps to mutex / lock acquisition. Even one bridge paragraph would connect this material to the learner's mental model. -->
## Gamete Structure and Function

```
SPERMATOZOON
──────────────
  HEAD:   Acrosome (enzyme package for zona pellucida penetration)
           Haploid nucleus (23 chromosomes including X or Y)
  MIDPIECE: Mitochondria → ATP for motility
  TAIL:   Flagellum — axoneme (9+2 microtubule structure)
           CatSper channel: Ca²+ entry → hyperactivated motility near oocyte

MATURE OOCYTE (Metaphase II arrest)
  ~100 μm diameter (1000× sperm head volume)
  Arrested at Metaphase II — meiosis paused until fertilization
  Surrounding structures:
    Zona pellucida (ZP): glycoprotein shell (ZP1, ZP2, ZP3)
                         ZP3 = primary sperm receptor
    Corona radiata: cumulus cells adherent to zona
  Maternal mRNA: stored, not translated until after fertilization
  Cortical granules: sub-membrane vesicles; critical for polyspermy block
```

---

## Fertilization: Molecular Events

```
ACROSOME REACTION
──────────────────
  Sperm binds ZP3 → GPCR signal → ↑intracellular Ca²+ →
  Acrosome exocytosis → releases:
    Acrosin (serine protease): partially digests zona
    Hyaluronidase: disperses cumulus cells
  Sperm-zona binding: now to ZP2 (secondary receptor, post-acrosome reaction)

SPERM-EGG MEMBRANE FUSION
<!-- @editor[content/P1]: Claim may be incorrect — verify: JUNO was identified by Bianchi et al. 2014, not Imai et al. 2014. IZUMO1 was identified by Inoue et al. 2005. Also "both named after Shinto gods" is imprecise — JUNO is named after the Roman goddess of fertility, not a Shinto god. -->
  Sperm IZUMO1 protein + egg JUNO protein: fusion mediators (required)
  Both proteins named after Shinto gods (Imai et al. 2014)

FAST BLOCK TO POLYSPERMY (immediate, seconds)
  Sperm entry → depolarization of egg plasma membrane
  Resting potential: ~-70 mV → +20 mV briefly
  Positive membrane potential prevents additional sperm fusion
  Duration: minutes; transient

SLOW BLOCK TO POLYSPERMY (permanent, seconds to minutes)
  IP3 wave (Ca²+ release from ER) → cortical granule exocytosis
  → Hardens zona pellucida (zona reaction)
  → Releases ovastacin: cleaves ZP2 → no more sperm binding
  Permanent — prevents polyspermy even after membrane repolarizes

CALCIUM OSCILLATIONS
  Fertilization triggers repeated intracellular Ca²+ waves.
  Each wave correlates with a mitotic division.
  Ca²+ oscillations triggered by sperm PLCZ1 (phospholipase Cζ)
  → IP3 → ER Ca²+ release.
  Clinically: if no Ca²+ oscillations → fertilization may fail.
  IVF: artificial Ca²+ ionophore treatment can rescue failed fertilizations.
```

---

## Egg Activation and Meiosis Completion

```
MEIOTIC MATURATION
───────────────────
  GERMINAL VESICLE (GV) stage: Primary oocyte, arrested in Prophase I
  LH surge → Resumption of meiosis → Metaphase I → Anaphase I
  First polar body extrusion → Haploid secondary oocyte
  Arrest at Metaphase II — maintained by CSF (cytostatic factor: c-Mos/MAPK/Emi2)

  FERTILIZATION RELEASES MEIOTIC ARREST
  Ca²+ oscillations → Calmodulin kinase II → Emi2 destruction
  → APC/C activation → cyclin B degradation → MPF inactivation
  → Meiosis II resumes → extrusion of second polar body
  → Haploid egg nucleus (female pronucleus)

  PRONUCLEI FORMATION
  Female pronucleus + male pronucleus (sperm chromatin decondensed)
  → Syngamy: pronuclei migrate toward each other
  → S-phase (DNA replication) occurs BEFORE nuclear envelope breakdown
  → First mitotic cleavage: chromosomes from both pronuclei meet at metaphase plate
```

---

## Cleavage: Properties and Stages

```
UNIQUE PROPERTIES OF CLEAVAGE
────────────────────────────────
  No growth: Cell cycle is S-phase → M-phase → S-phase → M-phase ...
             No G1 or G2. Cells get SMALLER with each division.
  Rapid: ~12-24 hours between divisions (vs 24 hours in typical somatic cells)
  Mechanisms: Pre-loaded maternal mRNAs + proteins drive early divisions
              No new transcription needed (initially)

CLEAVAGE STAGING
  Zygote (1-cell) → Day 0-1
  2-cell → Day 1-2    ← Embryonic genome activation begins here in humans
  4-cell → Day 2      ← Primary EGA (minor)
  8-cell → Day 2-3    ← Major EGA (embryonic genome fully active)
  16-cell (morula) → Day 3-4  ← Compaction begins
  Blastocyst → Day 4-5

RADIAL vs SPIRAL CLEAVAGE
  Radial (vertebrates including humans):
    Cells divide perpendicular or parallel to axis.
    Regulative development: blastomeres can replace each other.
  Spiral (many invertebrates):
    Mosaic development: each cell has fixed fate from start.
    Cannot replace lost blastomeres.

MATERNAL-TO-ZYGOTIC TRANSITION (MZT)
  Early cleavage driven by maternal mRNA and proteins (deposited in oocyte).
  In humans: EGA initiates at 4-8 cell stage.
  Maternal mRNAs degraded; embryo begins transcribing own genome.
  Transition is coordinated and critical — failure → developmental arrest.
```

---

## Compaction and Blastocyst Formation

```
COMPACTION (8-16 cell stage)
──────────────────────────────
  Cells flatten and maximize surface contact with each other.
  Driven by E-cadherin upregulation + PKC signaling.
  Creates morula: compact ball of cells, indistinguishable from outside.
  After compaction: inside vs outside positions become distinct.

POSITION DETERMINES FATE
  Outside cells → Trophectoderm (TE) → placenta, chorion
  Inside cells → Inner Cell Mass (ICM) → embryo proper, amnion, yolk sac

  FIRST CELL FATE DECISION
  This is the first time in mammalian development that cells have
  genuinely different fates (ICM vs TE).

  Key transcription factors:
    ICM: Oct4, Sox2, Nanog (pluripotency factors)
    TE: Cdx2, Tead4 (trophectoderm factors)

  Mutual repression: Oct4 represses Cdx2; Cdx2 represses Oct4
  → Bistable switch → inside stays ICM, outside becomes TE.

BLASTOCYST CAVITATION
  Na+/K+-ATPase in TE pumps Na+ into intercellular space.
  Water follows osmotically.
  Creates blastocoel (fluid-filled cavity).
  ICM pushed to one pole of blastocyst.

  BLASTOCYST STRUCTURE
  ─────────────────────
  Zona pellucida (thin glycoprotein coat)
     │
  ┌──┴──────────────────────────────────────┐
  │ Trophectoderm (outer epithelial layer)  │
  │                                         │
  │  ┌───────┐                             │
  │  │  ICM  │   ← Embryonic pole          │
  │  └───────┘                             │
  │                                         │
  │           Blastocoel (fluid cavity)     │
  │                                         │
  └─────────────────────────────────────────┘
```

---

## ICM Differentiation: Epiblast vs Hypoblast

```
SECOND CELL FATE DECISION: ICM → EPIBLAST + PRIMITIVE ENDODERM
─────────────────────────────────────────────────────────────────
  The ICM is not uniform — it differentiates into:

  EPIBLAST (EPI): gives rise to all fetal tissues + amnion
    Transcription factors: Oct4, Sox2, Nanog
    These are the "core pluripotency factors"
    Epiblast cells = the embryonic stem cell source (ESC)

  PRIMITIVE ENDODERM (PE) = Hypoblast: gives rise to yolk sac
    Transcription factors: Gata6, Sox17
    Mutual inhibition with epiblast factors
    The "salt and pepper" model: initially Nanog(high) vs Gata6(high) cells
    interdigitated → sorted into layers by differential adhesion

  TIMELINE (mouse):
    E3.5: ICM present; uniform Nanog + Gata6 expression
    E4.0: Salt-and-pepper mixed cells
    E4.5: Sorted into epiblast (inner) + primitive endoderm (surface of ICM)
    E5.0: Implantation + primitive endoderm spreads to line blastocoel

  KEY SIGNAL: FGF/ERK pathway
    Gata6 → FGF receptor signaling → ERK activation → PE fate
    Nanog → FGF4 production (signals to neighbors → PE fate)
    This is a feed-forward community signal that sorts the salt-and-pepper.
```

---

## Implantation

```
IMPLANTATION (Day 5-10 in humans)
────────────────────────────────────
  Blastocyst must break out of zona pellucida ("hatching"):
    Enzymatic dissolution (strypsin) + expansion from blastocoel pressure.

  Adhesion to uterine epithelium:
    Blastocyst ICM/embryonic pole contacts endometrium.
    Initial adhesion: selectins, MUC1 shedding.
    Firm adhesion: integrins (blastocyst) + fibronectin, osteopontin (endometrium).

  Invasion:
    Trophectoderm differentiates into:
    Cytotrophoblast (inner, proliferative)
    Syncytiotrophoblast (outer, invasive, multinucleated)
    → Syncytiotrophoblast invades maternal decidua → anchors placenta
    → Secretes hCG (human chorionic gonadotropin) → maintains corpus luteum
    → hCG = the pregnancy test signal

  IMPLANTATION WINDOW
    Days 20-24 of 28-day cycle (7-9 days after ovulation).
    Progesterone-dependent endometrial transformation (decidualization).
    Outside this window → implantation fails → embryo lost.
    Most early pregnancy losses are implantation failures (often undetected).

ECTOPIC PREGNANCY
  Blastocyst implants outside uterus (usually fallopian tube).
  Trophoblast invades → growing mass → eventual rupture → hemorrhage.
  Risk factors: previous tubal surgery, PID, IVF.
  Treatment: methotrexate (anti-proliferative) or surgery.
```

---

## Relevance to IVF and ART

```
IVF CORRELATION WITH DEVELOPMENTAL BIOLOGY
────────────────────────────────────────────
  EGG RETRIEVAL: Oocytes arrested at Metaphase II (or GV) retrieved.
  FERTILIZATION: ICSI (intracytoplasmic sperm injection) introduces sperm directly.
                 Bypasses acrosome reaction, zona binding requirements.
  CULTURE:       Embryos cultured to Day 3 (8-cell) or Day 5-6 (blastocyst).
                 Blastocyst culture preferred (better selection — weaker embryos die).
  TRANSFER:      Blastocyst transferred to uterus (fresh or frozen).

  PREIMPLANTATION GENETIC TESTING (PGT)
  Biopsy trophectoderm cells (not ICM!) at blastocyst stage.
  NGS sequencing: aneuploidy (PGT-A) or specific mutations (PGT-M).
  Safer to biopsy TE — not contributing to fetus.
  Success rate with PGT-A for women > 38: ~60-65% per euploid transfer.

  WHY MOST IVF EMBRYOS FAIL TO IMPLANT
  High aneuploidy rate in human preimplantation embryos:
    Age 35: ~50% of embryos aneuploid
    Age 42: ~80-85% aneuploid
  Aneuploidy usually incompatible with successful implantation.
  This is why human reproductive success per cycle is so low (~20-30%).
```

---

## Decision Cheat Sheet

| Process | Timing (human) | Key Event | Clinical Relevance |
|---------|---------------|-----------|-------------------|
| Fertilization | Day 0 | ZP penetration, Ca²+ oscillations | IVF ICSI bypasses sperm binding |
| Polyspermy block | Seconds-minutes | Cortical reaction, zona hardening | Failure → triploid embryo (incompatible) |
| Meiosis II completion | Minutes post-fertilization | Second polar body extrusion | Confirms normal fertilization |
| Embryonic genome activation | 4-8 cell (Day 2-3) | Maternal→zygotic transition | Cleavage arrest at this stage = EGA failure |
| Compaction | 8-cell (Day 2-3) | E-cadherin; inside/outside position | Outside → TE; Inside → ICM |
| Blastocyst | Day 4-5 | Cavitation; ICM vs TE | Blastocyst transfer preferred in IVF |
| ICM differentiation | Day 4-5 | Epiblast vs primitive endoderm | ESC derived from epiblast |
| Implantation | Day 5-10 | Trophoblast invasion; hCG production | hCG = pregnancy test; ectopic = surgical emergency |

---

## Common Confusion Points

**"The egg is haploid — but has the same DNA as a body cell?"**
Almost right. The oocyte at ovulation has completed meiosis I, with one copy of each chromosome pair (haploid), but each chromosome is a pair of sister chromatids. Strictly it's in Metaphase II — haploid chromosome count (23) but still 46 chromatid equivalents. Only after fertilization does the second polar body extrude, yielding truly 23 single chromosomes.

**"ICM = embryonic stem cells — so IVF embryos are being used for ESCs?"**
Embryonic stem cells in research are derived by isolating ICM from blastocysts and culturing them. In the context of IVF, discarded or surplus blastocysts (usually ones determined to be non-viable or not selected for transfer) have been the source of hESC lines. The iPSC revolution (Module 08) has reduced the demand for and controversy around hESC derivation.

**"Implantation failure is rare — why does IVF have such low success rates?"**
Implantation failure is extremely common — it just usually goes unrecognized. Most embryos lost before clinical recognition of pregnancy are aneuploid and simply don't implant. The natural per-cycle pregnancy rate in healthy young couples is only ~20-25%. Most of this is implantation failure. IVF makes embryos externally visible, revealing the true (high) attrition rate of early embryos.
