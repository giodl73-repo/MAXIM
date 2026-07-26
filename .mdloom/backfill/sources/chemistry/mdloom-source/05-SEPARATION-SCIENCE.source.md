---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-SEPARATION-SCIENCE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:separation-science
kind: guide
module: chemistry
section: chemistry
title: Separation Science - Chromatography, Extraction, Electrophoresis
status: source-custody
source_custody: partial
current_path: chemistry/05-SEPARATION-SCIENCE.md
canonical_path: chemistry/05-SEPARATION-SCIENCE.md
backsource_ids: [mdloom-backfill:chemistry:05-separation-science, git-history:chemistry:05-separation-science]
concepts: [chromatography, hplc, gas-chromatography, electrophoresis, extraction]
root_concepts: [separation-science]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Separation Science — Chromatography, Extraction, Electrophoresis

**This guide owns** analytical-scale separations: the plate/rate theory that
governs all chromatography, GC, HPLC, TLC, capillary electrophoresis, sample-prep
extraction (LLE/SPE), and the hyphenated GC-MS / LC-MS interfaces. **It defers**
process-scale distillation, absorption, and membrane separations to
`chemical-eng/04`; the MS half of the hyphenated methods is detailed in `07`. The
unifying idea: exploit a **differential partition** between a moving phase and a
stationary phase so components travel at different speeds and resolve in time or
space.

```
ALL CHROMATOGRAPHY IS DIFFERENTIAL MIGRATION
==========================================================================
  inject mixture --> [ mobile phase pushes | stationary phase retards ]

  analyte A (low affinity for stationary)  ====fast====>   elutes first
  analyte B (high affinity)                =slow=>          elutes later

  detector trace:        A        B
                       __/\______/\____   t
                       :  :      :  :
                      tR_A       tR_B

  THE TWO KNOBS:
    SELECTIVITY (alpha) = k'_B/k'_A = (tR_B-t0)/(tR_A-t0)  <- chemistry
        t0 = dead/hold-up time (elution time of an unretained solute)
    EFFICIENCY  (N)     = sharpness of peaks  <- physics: van Deemter
  RESOLUTION Rs combines both -> baseline separation at Rs >= 1.5
==========================================================================
```

---

## Plate Theory and the van Deemter Equation

Peaks broaden as they travel. **Plate number N** measures efficiency (equivalent
theoretical plates), **plate height H = L/N** measures broadening per unit length:

```
   N = 16 (tR / W)^2  =  5.54 (tR / W_1/2)^2       (W = baseline / half-height width)
   RESOLUTION:  Rs = 2 (tR_B - tR_A) / (W_A + W_B) ;  Rs >= 1.5 = baseline

   PURNELL master equation (what to tune):
      Rs = (sqrt(N)/4) * ((alpha - 1)/alpha) * (k/(1+k))
              efficiency    selectivity        retention
```

Selectivity (α, the chemistry of phase choice) is by far the strongest lever;
retention factor k should sit in the sweet spot k ≈ 2–10; efficiency helps only as
√N. Define the terms precisely against the **dead time t₀** (hold-up time, the
elution time of an unretained solute, t_M): the retention factor is
k′ = (t_R − t₀)/t₀, and **selectivity is a ratio of retention factors, not of raw
retention times** — α = k′_B/k′_A = (t_R,B − t₀)/(t_R,A − t₀), with B the more
retained peak so α ≥ 1. Using t_R,B/t_R,A instead silently folds in the dead time
and mis-states α. **Van Deemter** explains where efficiency comes from as a function of mobile-
phase velocity u:

```
   H = A + B/u + C*u
       |    |      |
       |    |      +-- C: mass-transfer resistance (slow equilibration) -> big at HIGH u
       |    +--------- B: longitudinal diffusion (spreads at LOW u)
       +------------- A: eddy diffusion / multipath (packing) ; ~0 for open capillaries

   OPTIMUM velocity:  u_opt = sqrt(B/C)   ->   H_min = A + 2 sqrt(BC)
```

This is the answer to "why does pushing the pump harder hurt?": **above u_opt the
C·u (mass-transfer) term dominates**, plates broaden, N falls, and resolution
degrades. Below u_opt, longitudinal diffusion (B/u) dominates. The classic
van Deemter curve is the U-shaped H-vs-u plot. Sub-2-µm UHPLC particles flatten the
C term (shorter diffusion path), which is why UHPLC can run fast *and* efficient.

---

## Gas Chromatography (GC)

Volatile, thermally stable analytes; mobile phase is an inert carrier gas.

- **Columns:** capillary WCOT (wall-coated open-tubular), 15–60 m. Stationary phase
  polarity picks selectivity: nonpolar **dimethylpolysiloxane** (DB-1/HP-1),
  5%-phenyl (DB-5, the default), polar **polyethylene glycol** (Carbowax) for
  H-bonding analytes.
- **Carrier gas:** He (standard), H₂ (faster, flatter van Deemter — flammable), N₂
  (cheap, narrow optimum).
- **Temperature programming:** ramp oven T to elute a wide boiling range in one run
  (the GC analog of an HPLC gradient); **Kováts retention index** normalizes
  retention against n-alkanes for library matching.
- **Detectors:**

| Detector | Responds to | Strength |
|---|---|---|
| **FID** | C–H (combustible organics) | near-universal, wide linear range, destructive |
| **TCD** | any thermal-conductivity difference | universal, non-destructive, less sensitive |
| **ECD** | electronegative groups (halogens, nitro) | ultra-sensitive & selective for these |
| **MS** | mass spectrum of each peak | identification, not just detection (`07`) |

**ECD vs FID for chlorinated pesticides:** the electron-capture detector is orders
of magnitude more sensitive *and* selective to the electronegative Cl atoms, so it
sees trace organochlorines a flame-ionization detector would bury in the matrix. Use
FID for general organics, ECD when the target carries halogens/nitro.

---

## High-Performance Liquid Chromatography (HPLC)

Non-volatile, thermally fragile, or high-MW analytes; a high-pressure liquid mobile
phase. The mode is chosen by the analyte's polarity, charge, or size:

| Mode | Stationary / mobile | Retains by | Typical use |
|---|---|---|---|
| **Reversed-phase (RP)** | C18 (nonpolar) / polar aqueous-organic | hydrophobicity | the default — >70% of methods |
| Normal-phase | silica (polar) / nonpolar | polarity/H-bonding | isomers, very nonpolar |
| HILIC | polar / high-organic | polar/hydrophilic | sugars, very polar metabolites |
| Ion-exchange (IEX) | charged resin / buffer | net charge | ions, proteins, charged drugs |
| Size-exclusion (SEC/GPC) | porous gel / — | hydrodynamic size | polymer MW, protein aggregation |
| Affinity | immobilized ligand / — | specific binding | antibody/protein capture |

**Isocratic vs gradient:** hold mobile-phase composition constant (isocratic) or
increase organic strength over time (gradient) to elute a wide polarity range.
Detectors: UV/DAD (workhorse), fluorescence (sensitive/selective), ELSD/CAD
(non-chromophores), and MS (LC-MS/MS for identification and trace quant).

**The pKa/pH problem (a basic drug, pKa 9.5, at pH 7 mobile phase):** at pH 7 the
base is >99% protonated (cationic, BH⁺). On bare RP-C18 a charged analyte is poorly,
irreproducibly retained and tails. Two clean fixes: (1) run **cation-exchange**,
which retains the permanently cationic species by charge; or (2) keep RP but add an
**ion-pairing** reagent, or move to a high-pH-stable phase and raise pH ≳ pKa+2 so
the base is neutral and hydrophobic again. The decision is driven entirely by the
analyte's charge state at the working pH — always compute it from pKa (`02`) first.

---

## TLC and Capillary Electrophoresis

**Thin-layer chromatography (TLC):** cheap planar screening on silica; retention is
the **retardation factor** R_f = (distance analyte)/(distance solvent front),
0 < R_f < 1. Used for reaction monitoring, quick purity checks, and preparative
scale-up; a well-chosen TLC solvent system predicts an RP/normal-phase column method.

**Capillary electrophoresis (CE):** separation in a narrow fused-silica capillary
under a high electric field — not a partition method but a *mobility* method.

```
   CE modes:
   CZE  (zone electrophoresis): separates by charge-to-size; neutral species
        co-migrate with the electroosmotic flow (EOF) and do NOT resolve.
   MEKC (micellar EK chromatography): add SDS micelles as a pseudo-stationary
        phase -> now NEUTRAL analytes partition and separate too.
```

CE delivers extremely high efficiency (10⁵–10⁶ plates, far above HPLC) with tiny
sample volumes, dominating DNA sequencing and many chiral/protein separations.

---

## Sample Preparation: Extraction

Before the column, isolate/concentrate the analyte:

- **Liquid-liquid extraction (LLE):** partition between immiscible solvents;
  governed by the distribution ratio **D = [A]_org/[A]_aq**. For an ionizable
  analyte D is pH-tunable (extract the *neutral* form) — the same speciation logic as
  `02`. Fraction extracted per stage = D·V_org/(D·V_org + V_aq); multiple small
  extractions beat one large one.
- **Solid-phase extraction (SPE):** pass sample through a small sorbent bed (C18,
  ion-exchange, mixed-mode), wash away matrix, elute the analyte in a small volume —
  cleaner and more automatable than LLE, and the standard front-end for LC-MS/MS
  bioanalysis.

---

## Hyphenated Methods (GC-MS, LC-MS/MS)

Coupling a separation to a mass spectrometer gives a **second, orthogonal
dimension**: retention time *and* mass spectrum per component. GC-MS uses electron-
ionization with searchable spectral libraries (NIST); LC-MS/MS uses soft ionization
(ESI/APCI) and tandem MS for selective, ultratrace quantitation. The interface
matters: GC's gas-phase effluent enters the source directly; LC must strip solvent
and ionize at atmospheric pressure. Fragmentation and interpretation are the subject
of `07`; here the point is that the separation delivers *clean, time-resolved*
packets to the detector, which is what makes trace identification in complex
matrices possible.

---

## Reader Tasks

1. **Why does raising HPLC flow past the van Deemter optimum lower plate count?**
   Above u_opt the mass-transfer term **C·u** dominates H, so plates broaden, N and
   resolution fall. Efficiency peaks at u_opt = √(B/C).
2. **RP or ion-exchange for a basic drug (pKa 9.5) at pH 7?** At pH 7 it is cationic;
   **cation-exchange** retains it cleanly (or RP with ion-pairing / a high-pH phase
   that neutralizes it). Bare RP-C18 gives poor, tailing retention.
3. **ECD or FID for chlorinated pesticides?** **ECD** — far more sensitive and
   selective to the electronegative Cl atoms; FID would lose the trace signal.
4. **Baseline resolution criterion?** R_s ≥ 1.5; improve it most cheaply by changing
   selectivity α (phase/mobile-phase chemistry), since Rs only grows as √N.
5. **Why do multiple small LLE extractions beat one big one?** Each stage removes the
   same *fraction* D·V/(D·V+V_aq); repeating compounds the removal, so n small
   portions extract more total analyte than one portion of the same solvent volume.

## Decision Cheat Sheet

| Analyte / goal | Method |
|---|---|
| Volatile, thermally stable | GC (FID general; ECD for halogens; MS to ID) |
| Non-volatile / thermolabile / large | HPLC |
| Hydrophobic small molecule | RP-C18, the default |
| Charged/ionizable at working pH | ion-exchange, or fix pH/ion-pair for RP |
| Polymer or protein MW distribution | SEC/GPC |
| Very polar (sugars, metabolites) | HILIC |
| Ultra-high efficiency, tiny sample | capillary electrophoresis |
| Neutral analytes by CE | MEKC (add SDS micelles) |
| Quick purity / reaction check | TLC (R_f) |
| Clean up a biological matrix | SPE (front-end for LC-MS/MS) |
| Identify each component | hyphenate to MS (`07`) |

## Common Confusion Points

- **Selectivity beats efficiency.** Rs grows only as √N but linearly with the
  (α−1)/α term; a longer column is the *last* thing to try, not the first.
- **Retention factor k, not retention time, is transferable.** k = (t_R − t_0)/t_0 is
  flow- and length-independent; compare methods with k, not raw t_R.
- **"Reversed-phase" names the polarity inversion,** not a direction. Normal phase =
  polar stationary/nonpolar mobile (the original); reversed = the now-dominant
  opposite.
- **GC needs volatility.** Non-volatile or thermally labile analytes require
  derivatization (e.g., silylation) or belong on HPLC — not the GC injector.
- **CE separates neutrals only with a pseudo-phase.** In plain CZE all neutrals
  co-elute with the EOF; you need MEKC micelles to resolve them.
- **The van Deemter A-term ≈ 0 for open-tubular columns.** Capillary GC uses the
  Golay form (no packing multipath); don't carry the packed-column A-term intuition
  into capillary work.
