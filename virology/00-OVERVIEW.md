# Virology — Landscape and Taxonomy

## The Big Picture

Viruses are obligate intracellular parasites — they have no metabolism of their own,
no ribosomes, and cannot reproduce outside a host cell. They are not alive in the
traditional sense; they are sophisticated nucleic acid delivery systems with protein
shells. This distinction shapes everything about virology.

```
┌──────────────────────────────────────────────────────────────────┐
│                    VIROLOGY LANDSCAPE                             │
│                                                                    │
│  WHAT VIRUSES ARE:                 WHAT VIRUSES ARE NOT:         │
│  ─────────────────                 ─────────────────────         │
│  Nucleic acid (RNA or DNA)         Not cells                     │
│  + protein coat (capsid)           No ribosomes                  │
│  + sometimes a lipid envelope      No ATP synthesis              │
│  Obligate intracellular            No protein synthesis outside  │
│  Genome 2-200 kb range            host                           │
│                                    Not universally "alive"       │
│                                                                    │
│  CLASSIFICATION:                                                  │
│  ─────────────────                                               │
│  Baltimore system (1971) — based on genome type + replication    │
│  7 classes: I-VII (dsDNA → ssRNA → retroviruses → dsRNA)         │
│                                                                    │
│  HOST RANGE:                                                      │
│  ─────────────                                                    │
│  Bacteriophage (bacteria) · Animal viruses · Plant viruses       │
│  Archaeal viruses · Giant viruses (Mimivirus, ~1.2 Mb genome)   │
└──────────────────────────────────────────────────────────────────┘
```

---

## What Makes Viruses Unique

### No Ribosomes, No Metabolism

```
  LIVING CELL:                    VIRUS:
  ──────────────                  ───────
  Ribosomes: yes                  Ribosomes: no
  ATP synthesis: yes              ATP synthesis: no
  Self-replication: yes           Self-replication: no (needs host)
  Cell division: yes              No cell division
  Homeostasis: yes                No homeostasis
  Response to environment: yes    Passive until inside host

  → Viruses are molecular parasites of cellular life, not a fourth domain
  → They can only replicate by hijacking host ribosomes, energy, and
    sometimes host DNA replication machinery
```

### The Minimal Virus Problem

A minimal virus must encode:
1. Capsid proteins (self-assembly)
2. Some replication machinery (unless relying entirely on host)
3. Proteins for entry (receptor binding, membrane fusion if enveloped)
4. Proteins for immune evasion (optional in some viruses)

Smallest known: Circovirus (porcine) — 1.7 kb ssDNA, encodes 3 proteins.
Largest known: Pandoravirus (~2.4 Mb dsDNA) — more protein-coding genes than
some bacteria.

---

## Baltimore Classification

The organizing framework for all of virology:

```
  CLASS   GENOME         REPLICATION STRATEGY          EXAMPLES
  ─────   ──────         ──────────────────────        ────────
  I       dsDNA          Nucleus: host DNA pol         Herpesviruses, poxvox,
                         (or viral pol for poxvirus)   adenovirus
  II      ssDNA          Rolling circle or             Parvoviruses, circoviruses
                         ss→ds→ss via host pol
  III     dsRNA          Viral RNA-dependent           Reoviruses, rotavirus
                         RNA polymerase (RdRp)
  IV      +ssRNA         RdRp synthesizes –strand      Coronaviruses, Flaviviruses,
                         template then +strand copies  Picornaviruses
  V       –ssRNA         Viral RdRp makes +strand      Influenza, Ebola, Rabies,
                         then genomic –strands         Measles
  VI      ssRNA-RT       Reverse transcriptase:        HIV (retroviruses)
          (retroviruses) RNA → DNA → integration
  VII     dsDNA-RT       Partial dsDNA; RT involved    Hepatitis B (hepadnaviruses)
          (hepadna)      in replication cycle
```

**Why this matters**: Baltimore class predicts:
- Whether antiviral drugs targeting RdRp will work (Class III-V)
- Whether reverse transcriptase inhibitors will work (Class VI-VII)
- Whether nuclear entry is required (Class I vs. others)
- Speed of evolution (RNA viruses: higher mutation rate than DNA viruses)

---

## Virus Structure Overview

```
  CAPSID GEOMETRIES:
  ──────────────────
  Icosahedral: most spherical viruses
               20 equilateral triangular faces, 12 vertices, 30 edges
               Efficient self-assembly from identical subunits
               Examples: adenovirus, herpesvirus, poliovirus, HIV

  Helical: capsomers arranged around nucleic acid in a helix
           Often rod-shaped
           Examples: TMV (tobacco mosaic), influenza, rabies (bullet-shaped)

  Complex: combination or unique geometry
           Bacteriophage T4: icosahedral head + helical tail
           Poxvirus: brick-shaped, not truly capsid-based

  ENVELOPE vs. NAKED:
  ────────────────────
  Enveloped: lipid bilayer derived from host membrane
             Contains viral glycoproteins for cell entry
             More fragile outside host; destroyed by detergents
             Examples: influenza (HA, NA spikes), HIV (gp120/gp41), SARS-CoV-2 (S)

  Naked (non-enveloped): protein capsid only
             More stable outside host; survive on surfaces longer
             Entry by direct membrane disruption or endosomal escape
             Examples: poliovirus, adenovirus, rotavirus, norovirus
```

---

## Module Map

| File | Core question |
|------|---------------|
| 01-VIRUS-STRUCTURE.md | What are viruses made of? |
| 02-BALTIMORE-CLASSIFICATION.md | How are viruses classified by genome type? |
| 03-REPLICATION-CYCLES.md | How does each virus class replicate? |
| 04-HOST-INTERACTIONS.md | How do viruses enter cells and spread? |
| 05-IMMUNE-EVASION.md | How do viruses escape immunity? |
| 06-QUASISPECIES.md | How do viral populations evolve? |
| 07-ANTIVIRAL-STRATEGIES.md | How do antiviral drugs work? |
| 08-PANDEMIC-BIOLOGY.md | How do pandemics emerge and spread? |
| 09-APPLICATIONS.md | How are viruses used as tools? |

---

## Key Numbers in Virology

| Parameter | Typical value | Notes |
|-----------|---------------|-------|
| Virus diameter | 20-300 nm | Most viruses; giant viruses ~1 μm |
| Genome size | 2 kb – 2.4 Mb | Circovirus to Pandoravirus |
| Burst size (per cell) | 10-10,000 copies | Depends on virus type |
| Replication cycle | 6-72 hours | Poliovirus 6h; herpesviruses 18-24h |
| HIV reverse transcription error rate | ~3×10⁻⁵/bp/cycle | High — no proofreading |
| Influenza RdRp error rate | ~10⁻⁴/bp/cycle | Very high |
| Human DNA polymerase error rate | ~10⁻⁹/bp/cycle | Proofreading |
| R₀ (SARS-CoV-2 original) | 2.5-3.5 | Basic reproduction number |
| R₀ (measles) | 12-18 | Highest known among human viruses |

---

## Connections to Other Reference Directories

| Virology concept | Where else it appears |
|-----------------|----------------------|
| Viral immune evasion | immunology/ — antigen presentation, interferon |
| Antiviral drugs | pharmacology/ (Batch 10) |
| Epidemic modeling | public-health/, probability-statistics/ |
| RNA virus replication | molecular-biology (natural-sciences/) |
| Viral gene delivery | biomedical-engineering/ |
| Quasispecies theory | evolutionary-biology/03 — molecular evolution |
| Baltimore classification | genomics/ — genome annotation |

---

## Decision Cheat Sheet

| Question | See module |
|----------|-----------|
| What type of genome does virus X have? | 02-BALTIMORE |
| How does an RNA virus replicate? | 02, 03 |
| Why is HIV hard to cure? | 03 (integration), 05 (immune evasion) |
| Why does flu evolve so fast? | 06-QUASISPECIES |
| How does tamiflu work? | 07-ANTIVIRAL |
| What determines pandemic potential? | 08-PANDEMIC |
| Can viruses be engineered for therapy? | 09-APPLICATIONS |

---

## Common Confusion Points

**Viruses are not bacteria.** Bacteria are living cells. Antibiotics do not work on
viruses. This confusion causes overuse of antibiotics for viral respiratory infections.

**RNA viruses evolve faster than DNA viruses.** RNA polymerases have no proofreading.
Error rates ~10⁻⁴/bp/cycle vs. ~10⁻⁹ for cellular DNA polymerase. This 100,000-fold
difference in fidelity means RNA viruses exist as quasispecies (clouds of variants)
rather than defined sequences.

**Enveloped viruses are more fragile.** The lipid envelope is destroyed by detergents
(soap), drying, and UV. SARS-CoV-2, HIV, and influenza are enveloped — they survive
only minutes to hours on surfaces. Norovirus is non-enveloped — it survives much longer.

**A virus "infecting" a cell does not mean it successfully replicates.** Entry and
replication are separate steps. Many viruses enter cells they cannot replicate in
(dead-end infections). Host range is determined by the ability to complete the full
replication cycle, not just cell entry.
