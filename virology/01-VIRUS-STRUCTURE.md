# Virus Structure and Genome Organization

## The Big Picture

Viruses are minimal nucleic acid delivery systems. Structure is tightly optimized
for: genome protection, receptor recognition, membrane penetration, and immune
evasion. Everything else is stripped out.

```
┌──────────────────────────────────────────────────────────────────┐
│                VIRUS STRUCTURAL HIERARCHY                        │
│                                                                  │
│  GENOME                                                          │
│  ─────── DNA or RNA, ss or ds, linear or circular, segmented     │
│     │                                                            │
│     ▼                                                            │
│  CAPSID SHELL                                                    │
│  ──────────── Protein coat: icosahedral / helical / complex      │
│     │                                                            │
│     ▼ (in enveloped viruses)                                     │
│  MATRIX PROTEINS (some viruses)                                  │
│  ──────────────────────────────                                  │
│     │                                                            │
│     ▼ (in enveloped viruses)                                     │
│  LIPID ENVELOPE                                                  │
│  ────────────── Stolen from host membrane                        │
│     │                                                            │
│     ▼ (in enveloped viruses)                                     │
│  SURFACE GLYCOPROTEINS                                           │
│  ─────────────────────── Receptor binding, membrane fusion       │
└──────────────────────────────────────────────────────────────────┘
```

---

## Capsid Geometry

### Icosahedral Capsids

The most common geometry. A regular icosahedron has:
- 20 equilateral triangular faces
- 12 vertices
- 30 edges
- Symmetry: 2-3-5 rotational symmetry axes

Why icosahedral? It is the geometry that maximizes enclosed volume per unit capsid
material while allowing self-assembly from identical protein subunits. It is the
thermodynamic minimum-energy packing arrangement.

```
  TRIANGULATION NUMBER T:
  ────────────────────────
  Describes how many capsomers tile each triangular face.
  T = h² + hk + k²   (where h and k are non-negative integers, k ≤ h)

  T = 1:   12 pentamers only (smallest icosahedron)
           Example: Cowpea mosaic virus capsid
  T = 3:   12 pentamers + 20 trimers = 180 subunits
           Example: Tomato bushy stunt virus
  T = 7:   12 pentamers + 60 hexamers = 420 subunits
           Example: Adenovirus, some phages
  T = 13:  12 pentamers + 80 hexamers = 780 subunits
           Example: some phages, giant viruses

  Larger T → larger capsid → can accommodate larger genome
  Herpesvirus T=16 → 162 capsomers → 162 nm diameter capsid
```

### Helical Capsids

Capsomers (usually single protein type) arrange around the nucleic acid in a helix.
The capsid diameter is determined by the capsomer and the helix parameters; the length
is determined by the genome length.

```
  TOBACCO MOSAIC VIRUS (TMV) — the paradigm:
  ───────────────────────────────────────────
  17.4 protein subunits per helical turn
  2040 identical coat protein subunits total
  ssRNA 6.4 kb: lies in a groove on the inner surface of the helix
  Diameter: 18 nm, Length: 300 nm (proportional to genome)
  Self-assembles from denatured state in vitro (first virus assembled in test tube)

  INFLUENZA NUCLEOCAPSID:
  ─────────────────────────
  8 genome segments, each independently helical (ribonucleoprotein, RNP)
  NP protein coats each RNA segment
  Surrounded by matrix protein M1, then lipid envelope
```

### Complex Capsids

```
  BACTERIOPHAGE T4:
  ──────────────────
  Prolate icosahedral head (elongated) + tail assembly
  Head: 166 nm × 111 nm, T=13 hexagonal grid on head body
  Tail: central tube (DNA injection), contractile sheath, tail fibers (recognition)
  Baseplate: activated upon attachment → tail sheath contracts → DNA injected

  This is basically a molecular syringe — mechanical engineering at 10 nm scale.
  Bridge: Phage T4 injection mechanism is a nanomachine more sophisticated than
  anything human nanotechnology has yet built.

  POXVIRUSES (e.g., smallpox, vaccinia):
  ─────────────────────────────────────
  Brick-shaped, ~200-300 nm × 250-350 nm
  Not classically icosahedral or helical
  Contain their own transcription machinery (unusual: most DNA viruses use host)
  Two forms: intracellular mature virion (IMV) and extracellular enveloped virion (EEV)
```

---

## The Lipid Envelope

Enveloped viruses acquire a membrane during budding from the host cell (or nuclear
membrane). The envelope lipid composition reflects the host membrane but is enriched
in the viral glycoproteins.

```
  ENVELOPED VIRUS CROSS-SECTION:
  ─────────────────────────────────────────────────────────────
  Surface glycoproteins  ←─── gp120/gp41 (HIV), HA/NA (flu),
  (projecting outward)          S protein (SARS-CoV-2)
         │
  ───────┼─────────────────────────────── lipid bilayer
         │         ↑ host-derived membrane
  Matrix protein (inside face of envelope; M protein in flu)
         │
  Capsid/nucleocapsid (innermost)
  └─ Genome inside
  ─────────────────────────────────────────────────────────────

  KEY SURFACE PROTEINS (by virus):
  ──────────────────────────────────
  HIV:           gp120 (CD4/CCR5 binding), gp41 (membrane fusion)
  Influenza:     HA (hemagglutinin; sialic acid binding + fusion)
                 NA (neuraminidase; cleaves sialic acid → release)
  SARS-CoV-2:    S (spike; ACE2 binding + furin cleavage + fusion)
  Ebola:         GP (glycoprotein; NPC1 receptor in late endosome)
  Herpesvirus:   gB + gH-gL complex (core fusion machinery)
```

---

## Genome Organization

### Genome Types

```
  PROPERTY              OPTIONS                     EXAMPLES
  ────────              ───────                     ────────
  Nucleic acid          DNA or RNA                  All viruses
  Strandedness          Single (ss) or double (ds)  Most RNA = ss; most DNA = ds
  Sense                 + (same as mRNA) or         Coronaviruses = +ssRNA
                        – (complement of mRNA)      Influenza = –ssRNA
                        Ambisense (both on same seg) Phleboviruses
  Topology              Linear or circular          Herpesviruses = linear
                                                    Papillomaviruses = circular
  Segmentation          Non-segmented or            Influenza = 8 segments
                        segmented (multiple pieces)  Reovirus = 10-12 segments
```

### Genome Size and Information Density

```
  VIRUS SIZE SPECTRUM:
  ─────────────────────
  Circovirus (porcine):  1.7 kb,  2 ORFs       Smallest known
  Poliovirus:            7.5 kb,  1 polyprotein
  HIV:                   9.7 kb,  9 genes
  Influenza A:           13.6 kb, 8 segments, 10-14 proteins
  Herpes simplex 1:     152 kb,  74 ORFs
  Megavirus chilensis:   1.26 Mb, >1000 ORFs
  Pandoravirus salinus:  2.47 Mb, ~2,500 ORFs

  OVERLAPPING READING FRAMES:
  ─────────────────────────────
  RNA viruses especially compact: multiple ORFs may overlap
  HIV: 9.7 kb genome encodes 15 proteins via:
  - Alternative splicing
  - Frameshift signals (ribosomal frameshifting)
  - Regulatory/non-structural proteins with multiple functions

  Bridge: viral genome compactness is a constraint-satisfaction problem.
  Given limited genome space, encoding more proteins requires overlapping
  frames, polyprotein processing (one ORF → many proteins via protease),
  and read-through strategies. RNA viruses are the most information-dense
  coding sequences known.
```

---

## Capsid Self-Assembly

Capsid proteins spontaneously self-assemble in vitro. This was first demonstrated
with TMV in 1955 (Fraenkel-Conrat and Williams) — the first proof that biological
self-assembly was chemically deterministic.

```
  TMV self-assembly pathway:
  ──────────────────────────
  1. RNA molecule folds into specific conformation
  2. Coat protein discs (17 subunits, 2 rings) recognize internal RNA signal
     (origin of assembly sequence)
  3. RNA threads through disc central hole
  4. Additional discs add, elongating helix in both directions
  5. Result: complete helical nucleocapsid

  HIV capsid (cone-shaped):
  ──────────────────────────
  Hexamers of CA (capsid protein) + 12 pentamers at cone ends
  Cone = ~216 hexamers + 7 pentamers (one end) + 5 pentamers (other end)
  Fullerene geometry: different from icosahedral or helical
  Mature conical core forms from spherical immature capsid after budding
  (HIV maturation requires PR protease → cleavage of Gag polyprotein →
   capsid reassembles into cone — this is the target of protease inhibitors)
```

---

## Viral Accessory Proteins

Beyond structural proteins, most complex viruses encode non-structural proteins:

```
  CATEGORY          FUNCTION                    EXAMPLES
  ────────          ────────                    ────────
  Replicase         Copy genome                 RdRp (RNA viruses), T-antigen
  Protease          Process polyproteins        HIV PR, HCV NS3/4A
  Integrase         Insert into host genome     HIV IN
  Immune evasion    Block innate/adaptive       HSV ICP47, HIV Vpu
  Cell cycle manip. Keep cells alive or drive   HPV E7 (Rb binding)
                    division
  Spread            Cell-to-cell movement       TMV MP, HSV UL31/34
  Transactivator    Activate viral gene exprs.  HIV Tat, HTLV-1 Tax
```

---

## Decision Cheat Sheet

| Question | Key point |
|----------|-----------|
| Why icosahedral geometry? | Maximum volume/subunit by symmetric self-assembly |
| How does capsid size scale? | Triangulation number T: more subunits = larger T |
| Why are enveloped viruses fragile? | Lipid bilayer destroyed by soap, UV, drying |
| Why do RNA viruses have small genomes? | RNA is chemically unstable; error rate limits genome size |
| Why do some viruses have segmented genomes? | Allows reassortment (key for flu evolution) |
| What determines host range? | Surface glycoprotein–receptor compatibility |

---

## Common Confusion Points

**Capsid ≠ envelope.** Non-enveloped viruses have only a capsid. Enveloped viruses
have both a capsid (inner) and a lipid envelope (outer). The distinction matters
enormously for transmission and drug susceptibility.

**Viral "size" refers to the whole virion, not the genome.** A 100 nm diameter virus
(influenza) has a 13.6 kb genome. A 200 nm herpesvirus has a 152 kb genome. Genome
size and virion size loosely correlate but are not proportional.

**+ssRNA viruses can directly serve as mRNA.** When +ssRNA virus enters a cell, the
genome itself can be translated by host ribosomes immediately. This is one reason
+ssRNA viruses often have faster replication cycles than −ssRNA or dsDNA viruses.

**Self-assembly does not require any cellular energy.** Capsid assembly is driven
by thermodynamics — the assembled state has lower free energy than the disassembled
state. No ATP is consumed in the assembly process itself (though cellular transport
and budding may require energy).
