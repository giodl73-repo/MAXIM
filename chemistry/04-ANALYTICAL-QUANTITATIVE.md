---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:analytical-quantitative
kind: guide
module: chemistry
section: chemistry
title: Analytical and Quantitative Chemistry
status: source-custody
source_custody: partial
current_path: chemistry/04-ANALYTICAL-QUANTITATIVE.md
canonical_path: chemistry/04-ANALYTICAL-QUANTITATIVE.md
backsource_ids: [proof-backfill:chemistry:04-analytical-quantitative, git-history:chemistry:04-analytical-quantitative]
concepts: [titration, gravimetry, voltammetry, calibration, method-validation]
root_concepts: [analytical-chemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Analytical and Quantitative Chemistry

**This guide owns** *how much* questions: gravimetry, the four titration families,
electroanalytical methods (potentiometry, cyclic and pulse voltammetry), and the
calibration/validation framework that turns an instrument signal into a number with
error bars. **It builds on** `02-ACID-BASE-SOLUTION` (titrimetry is applied
equilibria — read 02 first) and `natural-sciences/05` (Nernst, cell EMF), and hands
uncertainty rigor to `11-MEASUREMENT-AND-SAFETY`. Separation-based quantitation
(HPLC, GC) lives in `05`.

```
QUANTITATION PIPELINE: SAMPLE -> SIGNAL -> NUMBER +/- U
==========================================================================
  SAMPLE
     | sampling + prep (dissolve, digest, extract -> 05)
     v
  MEASUREMENT PRINCIPLE (pick one)
     [ CLASSICAL ]         [ ELECTROANALYTICAL ]   [ INSTRUMENTAL ]
      gravimetry            potentiometry           spectro -> 07,
      titrimetry            voltammetry             chromato -> 05
      (absolute)            (relative)              (relative)
            |                    |                       |
            v                    v                       v
  CALIBRATION  (external | internal std | standard addition)
            v
  RESULT +/- UNCERTAINTY  (LOD, LOQ, recovery, validation)
==========================================================================
```

Two philosophies run through the field. **Absolute methods** — gravimetry and
titrimetry — need no calibration curve *of the analyte*; the answer comes from
reaction stoichiometry and a measured mass or volume. That independence is
conditional, not magic: titrimetry still needs a **titrant of known concentration**,
established by standardization against a **primary standard** (e.g., KHP for NaOH,
Na₂CO₃ or Tris for acids, As₂O₃ for oxidants), and gravimetry assumes **complete,
pure precipitation with exact, known stoichiometry**. The metrological label
"primary (ratio) method" applies only when those conditions hold — known
stoichiometry, quantitative reaction, characterized purity, and traceable mass/
volume. **Relative methods** — nearly all instrumental techniques — produce a signal
proportional to concentration and *must* be calibrated. Knowing which class you are
in tells you where the error comes from.

---

## Gravimetry and the Four Titrations

**Gravimetric analysis:** precipitate the analyte quantitatively, filter, dry/ignite
to a known stoichiometry, weigh. Accuracy rests on complete, pure precipitation
(controlled by supersaturation, digestion, and washing) and a defined final formula
(e.g., Ba²⁺ as BaSO₄, Ni²⁺ as the dimethylglyoxime chelate). Slow, but — given that
complete/pure precipitation and defined stoichiometry — an absolute method traceable
to a balance, with no analyte calibration standard.

**Titrimetry:** add a standardized titrant until stoichiometric equivalence; detect
the **endpoint** (indicator or instrument) as close as possible to the true
**equivalence point**. The families differ by the reaction that drives them:

| Titration | Reaction | Endpoint detection | Example |
|---|---|---|---|
| Acid-base | H⁺ transfer | pH indicator / pH meter | HCl vs NaOH; Kjeldahl N |
| Redox | electron transfer | potentiometric / redox indicator | Fe²⁺ vs MnO₄⁻ / Ce⁴⁺; iodometry |
| Complexometric | metal + chelate | metal-ion indicator (EBT, murexide) | Ca²⁺/Mg²⁺ vs EDTA (water hardness) |
| Precipitation | insoluble salt | Mohr / Volhard / Fajans | Cl⁻ vs AgNO₃ |

### Titration-curve logic

A titration curve is the master-variable (pH, or electrode potential) plotted vs
titrant volume; the **equivalence point** is the steepest inflection. For a weak
acid titrated by strong base there are four regions: initial (weak-acid pH), buffer
(Henderson-Hasselbalch, flattest at the half-equivalence point where pH = pKa),
equivalence (salt hydrolysis), and excess-base (dominated by [OH⁻]).

Worked equivalence point — **25.00 mL of 0.100 M acetic acid titrated with 0.100 M
NaOH**: at equivalence all acid is converted to acetate, diluted to 50.0 mL →
[OAc⁻] = 0.0500 M. Acetate is a weak base, K_b = K_w/K_a = 10⁻¹⁴/1.8×10⁻⁵ =
5.6×10⁻¹⁰. Then [OH⁻] = √(K_b·C) = √(5.6×10⁻¹⁰ × 0.0500) ≈ 5.3×10⁻⁶ M → pOH = 5.28
→ **pH ≈ 8.7**. The equivalence point of a weak-acid/strong-base titration is
*basic*, so you pick phenolphthalein, not methyl red — indicator choice follows the
equivalence pH, not the reagents' labels.

**EDTA (complexometric)** titrations require the pH control from `02`: the
conditional constant K'f = α_{Y⁴⁻}·Kf must be large (≳10⁸) for a sharp break, so
Ca²⁺/Mg²⁺ hardness is run at pH 10 with an ammonia buffer and Eriochrome Black T,
which is wine-red when bound to metal and blue when free.

---

## Electroanalytical Methods

### Potentiometry and ion-selective electrodes (ISE)

Measure a cell potential at (essentially) zero current; the analyte activity sets
the membrane potential via a Nernstian response:

```
   E = const +/- (2.303 RT / zF) * log a_ion
       at 25 C:  2.303 RT / F  =  59.16 mV  per decade, divided by charge z
   -> a monovalent ion (glass pH electrode, F- ISE): ~59 mV per 10x activity
   -> a divalent ion (Ca2+ ISE): ~29.6 mV per decade
```

The pH glass electrode is the ubiquitous ISE. Key practical points: ISEs respond to
**activity, not concentration** (calibrate in matched ionic strength — see `09`),
suffer **selectivity-coefficient** interferences (the Nikolsky-Eisenman correction),
and need frequent two-point calibration because the slope drifts.

### Voltammetry (current vs applied potential)

Sweep the working-electrode potential and record current. **Cyclic voltammetry
(CV)** is the diagnostic workhorse. For a reversible one-electron couple the peak
current follows the **Randles-Sevcik** equation:

```
   i_p = 2.69e5 * n^(3/2) * A * D^(1/2) * C * v^(1/2)      (Randles-Sevcik, 25 C)
        UNITS FOR THIS EXACT CONSTANT:  i_p in A ; n dimensionless ;
        A in cm^2 ; D in cm^2/s ; C in mol/cm^3 (NOT mol/L) ; v in V/s
        the 2.69e5 = 0.4463 (F^3/RT)^(1/2), units C mol^-1 V^-1/2 at 298 K

   REVERSIBILITY DIAGNOSTICS (reversible couple):
     dEp = |Epa - Epc| = 59/n mV     and     i_pa / i_pc = 1     (scan-rate indep.)
```

Because i_p ∝ v^(1/2), **doubling the scan rate multiplies the peak current by √2
(≈1.41)** — a linear i_p-vs-√v plot confirms a diffusion-controlled (not
adsorption-controlled) process and yields D. Mind the units on the 2.69×10⁵
constant: it is written for **C in mol cm⁻³** (not mol L⁻¹), A in cm², D in cm² s⁻¹,
and v in V s⁻¹, giving i_p in amperes. Increasing ΔEp with scan rate signals
**quasi-reversibility** (slow electron transfer). **Differential pulse voltammetry
(DPV)** and square-wave voltammetry subtract charging current to reach nM–pM
detection limits, and **anodic stripping voltammetry** preconcentrates trace metals
onto the electrode for ultratrace analysis.

---

## Calibration: Turning Signal into Concentration

| Method | How | Use when |
|---|---|---|
| External standard | build curve from pure standards; read unknown against it | matrix is clean/reproducible |
| Internal standard | add fixed amount of a reference compound; use signal ratio | to cancel injection/drift variance (GC/LC-MS) |
| **Standard addition** | spike the *sample itself* with known analyte increments; extrapolate | strong, unknown **matrix effects** |

**Standard addition** is the answer to the "blood-plasma drug assay" problem: when
the sample matrix suppresses or enhances the signal in a way pure standards can't
mimic, you spike the real matrix with known analyte and extrapolate the line back to
zero signal. The intercept on the concentration axis (|x-intercept|) is the original
analyte concentration — the matrix effect is present in every point equally, so it
cancels. The cost is that you *extrapolate* (less precise than interpolating a
normal curve) and consume more sample.

**Detection limits** from the calibration:

```
   LOD = 3 * sigma_blank / m        LOQ = 10 * sigma_blank / m
        sigma_blank = SD of blank (or of the intercept);  m = calibration slope
   Linear dynamic range: LOQ up to the point where the curve bends (saturation).
```

Spike-**recovery** (analyte added to matrix, measured back; target ~85–115%) checks
accuracy in the real matrix; **blank correction** removes reagent background.

---

## Method Validation (ICH Q2(R2), coordinated with Q14)

Before a quantitative method is trusted, validate the parameters below. This is the
regulatory contract that makes a number defensible (and the analytical face of GLP,
`11`). The current ICH reference is **Q2(R2)** (adopted 2023), which revised and
replaced the long-standing **Q2(R1)**, and it is written to be used **together with
Q14** on *analytical procedure development* (the lifecycle/enhanced, QbD-style
approach). The core parameter set below is stable across the revision; Q2(R2)/Q14
add explicit development, robustness-by-design, and lifecycle-management
expectations (and broaden coverage toward newer techniques).

| Parameter | Question it answers | Typical evidence |
|---|---|---|
| Specificity/selectivity | Does anything else respond? | resolution from interferents, peak purity |
| Linearity & range | Signal ∝ conc over what span? | r² and residual plot over ≥5 levels |
| Accuracy | Right value? | spike recovery, reference material |
| Precision | Reproducible? | repeatability, intermediate, reproducibility (RSD) |
| LOD / LOQ | Smallest detectable/quantifiable? | 3σ/m and 10σ/m |
| Robustness | Survives small deliberate changes? | vary pH, T, flow; monitor response |

Precision is layered: **repeatability** (same analyst/day/instrument),
**intermediate precision** (different days/analysts, same lab), and
**reproducibility** (different labs). Reporting one RSD without saying which level is
a common way to overstate a method.

---

## Reader Tasks

1. **pH at the equivalence point of 25.00 mL 0.100 M acetic acid vs 0.100 M NaOH?**
   All acid → 0.0500 M acetate; K_b = 5.6×10⁻¹⁰; [OH⁻] = √(K_b·C) ≈ 5.3×10⁻⁶ →
   **pH ≈ 8.7** (basic → use phenolphthalein).
2. **What does doubling the CV scan rate do to peak current?** i_p ∝ √v, so it rises
   by **√2 ≈ 1.41×**; a straight i_p-vs-√v line confirms diffusion control.
3. **Why standard addition for a plasma drug assay?** The plasma matrix alters
   response unpredictably; spiking the real sample makes the matrix effect common to
   all points, so extrapolation to the x-intercept cancels it.
4. **How do you know an electron transfer is reversible by CV?** ΔEp ≈ 59/n mV,
   independent of scan rate, with i_pa/i_pc ≈ 1. Growing ΔEp with v → quasi-reversible.
5. **Which titration and indicator for total water hardness?** Complexometric EDTA at
   pH 10 (ammonia buffer) with Eriochrome Black T; the wine-red→blue transition marks
   the endpoint.

## Decision Cheat Sheet

| Situation | Choose |
|---|---|
| Need an absolute answer, have time | gravimetry or titrimetry (no analyte curve; titrant standardized vs a primary standard) |
| Weak-acid/strong-base titration | expect basic equivalence pH → phenolphthalein |
| Metal-ion quantitation | EDTA complexometric, pH-buffered for K'f |
| Continuous ion monitoring | ISE / potentiometry (calibrate for activity) |
| Redox couple mechanism/kinetics | cyclic voltammetry (ΔEp, i_p vs √v) |
| Trace-level electroactive analyte | DPV / square-wave / stripping voltammetry |
| Strong matrix interference | **standard addition** |
| Cancel injection/drift error | internal standard |
| Report a defensible method | validate per ICH Q2(R2) (developed under Q14) |

## Common Confusion Points

- **Endpoint ≠ equivalence point.** The indicator changes at the endpoint; the
  titration error is how far that sits from true equivalence. Pick an indicator whose
  transition brackets the equivalence pH/potential.
- **Equivalence-point pH is not 7 in general.** Weak-acid/strong-base → basic;
  weak-base/strong-acid → acidic. Only strong/strong is neutral.
- **ISEs measure activity, not concentration.** At high ionic strength the two
  diverge; calibrate in a matched matrix or use a total-ionic-strength adjustment
  buffer.
- **"Reversible" in CV is electrochemical, not thermodynamic.** It means fast
  electron transfer (Nernstian at the electrode), diagnosed by ΔEp and peak ratios.
- **LOD is not the lowest number you can report.** Between LOD and LOQ you can detect
  but not reliably *quantify*; report quantitative results only at/above LOQ.
- **Standard addition extrapolates.** It trades precision for freedom from matrix
  bias; don't use it when a clean external calibration would serve.
