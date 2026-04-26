# Biosensors and Diagnostics

## The Big Picture

A biosensor converts a biological signal into a measurable physical output. The architecture
is always three layers: bioreceptor (specificity) + transducer (conversion) + signal processor
(output). The rest is optimization of sensitivity, selectivity, and real-world robustness.

```
+---------------------------------------------------------------------+
|              BIOSENSOR ARCHITECTURE                                 |
+---------------------------------------------------------------------+
|                                                                     |
|  BIORECEPTOR          TRANSDUCER             SIGNAL PROCESSING      |
|  (specificity layer)  (conversion)           (output)               |
|                                                                     |
|  Enzyme               Electrochemical        Analog conditioning    |
|  Antibody             (amperometric,         ADC / digital         |
|  Aptamer              potentiometric,        Calibration            |
|  Nucleic acid         impedimetric)          Alarm/display         |
|  Whole cell                                                         |
|  Molecularly          Optical                                       |
|  imprinted            (SPR, fluorescence,                           |
|  polymer (MIP)        LSPR)                                         |
|                                                                     |
|                       Piezoelectric                                 |
|                       (QCM, SAW)                                    |
+---------------------------------------------------------------------+

  APPLICATIONS SPECTRUM:
  Lab (central)    -> Point-of-care      -> Continuous wearable
  High accuracy       Rapid, portable       Real-time monitoring
  Slow turnaround     Minutes to result     CGM, ECG patches
  Gold standard       LFT, i-STAT           No lab required
```

---

## Transduction Mechanisms

### Electrochemical — Amperometric

Apply fixed potential, measure current. Current is proportional to analyte concentration.
The original glucose sensor (Leland Clark, 1962) is amperometric.

```
  AMPEROMETRIC BIOSENSOR
  ======================

  Applied potential V (fixed, anodic or cathodic)
       |
       v
  Working electrode surface
       |
       |  Redox reaction: A -> B + ne-
       v
  Electron transfer to/from electrode
       |
       v
  Current i measured (nA to μA range)
  i is proportional to concentration [A] (at low concentrations)
  Governed by Cottrell equation for diffusion-limited systems

  GLUCOSE OXIDASE MECHANISM (glucose sensor):
  Step 1: GOx (glucose oxidase) oxidizes glucose to gluconolactone
          Glucose + O2 -> Gluconolactone + H2O2  (1st gen: oxygen mediator)
          Glucose + mediator_ox -> Gluconolactone + mediator_red (2nd gen)
          Glucose + electrode -> Gluconolactone + 2H+ + 2e- (3rd gen: direct)

  1st gen: measure H2O2 oxidation (or O2 depletion) — oxygen-dependent
  2nd gen: synthetic mediator (ferrocene, osmium complex) shuttles electrons
           to electrode — oxygen-independent, lower applied potential
  3rd gen: direct electron transfer — no mediator needed — ideal but
           difficult because GOx active site is buried deep in protein

  Modern CGMs (continuous glucose monitors):
  - 2nd generation amperometric
  - Subcutaneous insertion ~5-7mm
  - Glucose diffuses through outer membrane (rate-limiting)
  - GOx in enzyme layer
  - Mediator transports electrons to electrode
  - Platinum working electrode at ~0.5V vs. Ag/AgCl reference
```

### Electrochemical — Potentiometric

Measure voltage at zero current. Ion concentration drives equilibrium potential via Nernst
equation.

```
  POTENTIOMETRIC BIOSENSOR (ION-SELECTIVE ELECTRODE)
  ===================================================

  E = E° + (RT/nF) * ln([analyte])
       Nernst equation

  E° = standard potential
  R = gas constant (8.314 J/mol·K)
  T = temperature (K)
  n = charge of ion
  F = Faraday constant (96485 C/mol)

  At 37°C:
  For monovalent ion (H+): slope = 61.5 mV/decade
  For divalent ion (Ca2+): slope = 30.7 mV/decade

  pH electrode (glass pH electrode):
  Special glass membrane (LaFeSi2O6) selectively permeable to H+
  -> Nernstian response to pH, slope ~59 mV/pH at 25°C

  FET-BASED (ISFET — Ion Sensitive FET):
  Gate oxide replaced with ion-selective membrane
  -> gate voltage modulated by ion concentration
  -> output: drain current
  Integrated circuits possible -> miniaturization -> lab-on-chip

  CLINICAL: i-STAT (Abbott) uses potentiometric sensors for
  Na+, K+, Cl-, Ca2+, pH, PCO2, PO2 in a credit-card-sized
  single-use cartridge. Point-of-care blood gas + electrolytes
  in 2 minutes.
```

### Electrochemical — Impedimetric (EIS)

Apply AC voltage, measure impedance across frequency spectrum. Binding events change the
capacitance and resistance of the electrode-solution interface.

```
  ELECTROCHEMICAL IMPEDANCE SPECTROSCOPY (EIS)
  =============================================

  Apply: V(t) = V0 * sin(ωt)
  Measure: I(t) = I0 * sin(ωt + φ)
  Z = V/I = |Z| * exp(jφ) = R + jX

  Equivalent circuit (Randles):
  Rs (solution resistance)
  Cdl (double-layer capacitance)
  Rct (charge transfer resistance) — binding changes this!
  Zw (Warburg impedance — diffusion)

  BIOSENSING: antibody on electrode surface
  Before binding: given Rct
  After target binding: Rct increases (blocked electron transfer)
  Delta Rct proportional to surface coverage -> concentration

  Advantages: label-free (no fluorescent tag needed)
  Disadvantages: matrix effects, non-specific binding
  Applications: immunosensors, DNA hybridization detection,
  bacterial detection, cell monitoring
```

### Optical — Surface Plasmon Resonance (SPR)

SPR is the gold standard for label-free kinetic measurement of molecular interactions.

```
  SURFACE PLASMON RESONANCE (SPR)
  ================================

  PHYSICS:
  Thin gold film (~50nm) on glass prism
  Monochromatic light incident at angle θ
  At specific angle θSPR: evanescent field couples to plasmons
  -> resonance -> sharp dip in reflected light intensity

  SENSING PRINCIPLE:
  Refractive index n at gold surface changes when molecules bind
  -> shifts θSPR
  -> monitors binding in real-time without labels

  SENSORGRAM:
  Response (RU)
    ^
    |              plateau (saturation)
    |         /----\
    |        /      \  dissociation
    |       / assoc  \
    |      /          \
    |_____/            \________
    +-------------------------> time
    inject                 regenerate

  Association phase: ka (on-rate, M^-1 s^-1)
  Dissociation phase: kd (off-rate, s^-1)
  KD = kd / ka (equilibrium dissociation constant)
  Biacore (Cytiva) is the dominant instrument.

  1 RU = change in refractive index corresponding to
         ~1 pg/mm2 protein surface coverage

  Applications: drug-target interaction kinetics,
  antibody characterization, early lead selection in pharma R&D
```

### Piezoelectric — Quartz Crystal Microbalance (QCM-D)

```
  QCM-D (Quartz Crystal Microbalance with Dissipation)
  =====================================================

  AT-cut quartz crystal oscillates in shear mode at resonant frequency f0
  (~5 MHz common). Binding of mass to surface -> frequency decrease:

  Sauerbrey equation (rigid thin film):
  Δf = -C * Δm / A
  C = 17.7 ng cm^-2 Hz^-1 at 5 MHz

  Mass sensitivity: ~1 ng/cm2

  Dissipation (D) monitoring:
  Viscoelastic films (hydrogels, cells) cause energy dissipation
  ΔD = stored energy / dissipated energy per cycle
  High ΔD/Δf ratio = soft, viscoelastic layer
  Low ΔD/Δf ratio = rigid layer

  Applications: thin film deposition, lipid bilayer formation,
  protein-surface adsorption, drug membrane interactions,
  cell adhesion monitoring
```

---

## Continuous Glucose Monitors (CGM)

CGMs are the most commercially successful implantable biosensors — Abbott Libre and Dexcom G7
each have >$1B annual revenue.

```
  CGM SYSTEM ARCHITECTURE
  =======================

  Subcutaneous sensor (7-15 day wear)
  +----------------------------------+
  | Outer membrane (glucose limiting)|  Rate-limiting diffusion
  | Enzyme layer (GOx immobilized)   |  Enzymatic oxidation
  | Inner membrane (H2O2 limiting)   |  (1st gen systems)
  | Working electrode (Pt or C)      |  Amperometric detection
  | Reference electrode (Ag/AgCl)    |  vs. reference
  +----------------------------------+
           |  (transcutaneous wire)
           v
  Electronics patch (worn on skin)
  +----------------------------------+
  | ADC (analog-to-digital)          |
  | Microcontroller                  |
  | Calibration algorithm            |
  | Bluetooth LE radio               |
  +----------------------------------+
           |  Bluetooth
           v
  Smartphone app or receiver
  Glucose trend + alarms

  PERFORMANCE METRICS:
  MARD = Mean Absolute Relative Difference
       = mean |CGM_reading - reference| / reference × 100%
  Abbott Libre 3: MARD ~7.9%
  Dexcom G7:      MARD ~8.2%
  FDA accuracy requirement: <15% for CGM clearance

  CALIBRATION:
  Factory-calibrated (Libre 3, Dexcom G7): no fingerstick needed
  User-calibrated (older Dexcom): 2 fingersticks/day

  CLINICALLY IMPORTANT DIFFERENCES:
  Abbott Libre: factory calibrated, reader required originally,
                sensor applied in back of upper arm, 60-min
                warm-up, 8-15 day wear
  Dexcom G7: factory calibrated, 30-min warm-up, direct phone
              integration, predictive alerts, 10-day wear
  Both integrated with insulin pumps for closed-loop ("artificial pancreas")

  Lag time: ISF glucose lags blood glucose by ~5-15 minutes
  -> algorithms predict blood glucose from ISF trend
```

---

## Lateral Flow Assays (LFA)

The technology behind every pregnancy test and COVID antigen test. Simple, cheap, rapid (~15 min),
works without power or equipment.

```
  LATERAL FLOW ASSAY — MECHANISM
  ================================

  STRIP ARCHITECTURE:
  +-------+----------+--------+---------+--------+
  | Sample |  Conj.  |  Test  | Control |  Absorp|
  | pad   |  pad     |  line  |  line   |  pad   |
  +-------+----------+--------+---------+--------+
    Add      Colloidal  Capture  Validates  Excess
    sample   gold-Ab    Ab       strip      fluid
    here     released             function  wicks

  SANDWICH FORMAT (for larger antigens like proteins):
  1. Sample added to sample pad
  2. Analyte flows into conjugate pad
  3. Colloidal gold-labeled antibody (detector Ab) binds analyte
  4. Complex flows along nitrocellulose membrane
  5. Test line: capture Ab immobilized -> captures analyte-gold complex
     -> visible line if analyte present
  6. Control line: anti-species antibody -> always captures excess gold-Ab
     -> always forms line (validates strip function)

  Result: 2 lines = POSITIVE (test + control)
          1 line (control only) = NEGATIVE
          0 lines = INVALID

  COMPETITIVE FORMAT (for small molecules like drugs, hormones):
  Small analyte in sample competes with immobilized analyte-conjugate
  on test line for limited gold-labeled antibody.
  Result: 2 lines = NEGATIVE (no analyte -> all antibody captured at test line)
          1 line = POSITIVE (analyte in sample -> fewer gold captured at test line)
  COUNTERINTUITIVE — darker test line = more negative

  QUANTIFICATION:
  Reader devices (Sofia, Quidel; Cube, LumiraDx) use reflectance
  photometry to quantify test line intensity.
  Dynamic range limited vs. lab assay; CV ~10-20%.

  COVID-19 ANTIGEN TEST EXAMPLE:
  Detects SARS-CoV-2 nucleocapsid protein
  Sensitivity: ~65-90% (vs. RT-PCR)
  Specificity: ~99%
  Best when viral load high (early symptomatic infection)
  PPV depends heavily on prevalence (Bayes theorem applies)
```

---

## CRISPR-Based Diagnostics

CRISPR diagnostics exploit the collateral cleavage activity of Cas12 and Cas13 —
properties not used in gene editing applications.

```
  CRISPR DIAGNOSTIC MECHANISM (SHERLOCK, DETECTR)
  ================================================

  Cas13a collateral cleavage (SHERLOCK):
  Cas13a + guide RNA (gRNA) + target RNA
  -> Cas13a:gRNA recognizes and cleaves target RNA (cis-cleavage)
  -> Activated Cas13a also cleaves nearby non-target RNAs (TRANS-cleavage)
  -> Reporter: ssRNA labeled with fluorophore-quencher pair
  -> Trans-cleavage separates F from Q -> fluorescent signal

  Cas12a collateral cleavage (DETECTR):
  Same principle but recognizes DNA targets and cleaves ssDNA reporters.
  Combined with LAMP or RPA for isothermal pre-amplification.

  SENSITIVITY:
  Without amplification: ~100 fM (attomolar with digital readout)
  With LAMP pre-amplification: single copy level (aM)
  Comparable to RT-PCR in optimized formats.

  SELECTIVITY:
  Single nucleotide discrimination possible (mismatch detection)
  -> can distinguish pathogen strains, drug resistance mutations

  SHERLOCK vs DETECTR:
  SHERLOCK: Cas13 + RPA + T7 transcription -> RNA target
  DETECTR:  Cas12 + LAMP -> DNA target -> faster workflow

  COMMERCIAL STATUS (2026):
  Sherlock Biosciences: FDA-authorized COVID test (EUA, 2020)
  Abbott ID Now (LAMP-based, not CRISPR): rapid flu/RSV/COVID
  Mammoth Biosciences: CRISPR diagnostics platform
  Still mostly research/limited commercial vs LFA ubiquity.
```

---

## Microfluidics — Lab-on-Chip

Microfluidics manipulates sub-microliter volumes in channels 10-1000 μm in dimension.
Physics changes at micro scale: surface forces dominate over gravity, laminar flow (Re < 1).

```
  MICROFLUIDICS FUNDAMENTALS
  ==========================

  REYNOLDS NUMBER: Re = ρvL/μ
  Typical microfluidic Re: 0.001 to 10 (always laminar)
  Laminar flow: mixing only by diffusion -> slow (problem)
  Solutions: chaotic advection (herringbone mixer), droplets

  FABRICATION:
  PDMS (polydimethylsiloxane) soft lithography:
  1. Photolithography: UV expose SU-8 photoresist on Si wafer
     -> master mold with raised features
  2. Pour PDMS prepolymer over master, cure at 70°C, peel off
     -> PDMS chip with channels
  3. Oxygen plasma bond PDMS to glass slide
  4. PDMS is transparent, gas-permeable, cheap, biocompatible
  Limitation: PDMS absorbs small hydrophobic molecules (drug assays)

  Thermoplastics (PMMA, COC, PC): injection molding
  -> mass production, lower absorption than PDMS
  Silicon/glass: best optical properties, hard to fabricate

  DROPLET MICROFLUIDICS:
  Two immiscible fluids (water + oil) at T-junction or flow-focusing
  -> monodisperse droplets (1-100 μm)
  Each droplet = independent reaction vessel
  Digital PCR: partition sample into millions of droplets
  -> Poisson statistics -> absolute quantification
  -> no standard curve required (ddPCR)

  ORGAN-ON-CHIP:
  Multi-layer PDMS chip with tissue cells + fluid channels
  Lung-on-chip (Wyss Institute): alveolar cells + vascular cells
  separated by thin porous membrane, cyclic stretching mimics breathing
  Applications: drug toxicity testing, disease modeling
  Goal: replace animal testing for ADMET studies
```

---

## Point-of-Care Devices

```
  KEY POC PLATFORMS
  =================

  Abbott i-STAT:
  Handheld analyzer, single-use cartridges
  Measures: blood gases (pH, PCO2, PO2), electrolytes (Na+, K+, Cl-, Ca2+),
            glucose, lactate, creatinine, cardiac troponin I, INR/PT
  Technology mix: biosensors (amperometric, potentiometric) + immunosensors
  Result in 2 minutes. FDA cleared. Used in ICU, ED, operating room.

  Cepheid GeneXpert:
  Cartridge-based real-time PCR (RT-PCR)
  Lysis + extraction + amplification + detection all in one cartridge
  Time to result: 45 min for MTB (tuberculosis), flu/COVID, GBS
  Uses: TB diagnosis (Xpert MTB/RIF), COVID, MRSA screening
  GeneXpert Omni: battery-powered, field-deployable version

  BioFire FilmArray (bioMerieux):
  Multiplex PCR: 20-200 pathogens from one sample in one run
  Panels: respiratory (FilmArray RP: flu, RSV, COVID, others),
          blood culture ID (FilmArray BCID), meningitis
  Time: ~1 hour. Used in hospital lab, ED.

  Roche cobas Liat:
  On-demand RT-PCR in 20 minutes (flu/COVID)
  Simple operator interface

  POC Troponin (cardiac biomarker):
  Abbot ARCHITECT STAT, Siemens Atellica VTLi
  High-sensitivity troponin I or T for rapid rule-in/rule-out of AMI
```

---

## Wearable Biosensors

```
  WEARABLE BIOSENSOR LANDSCAPE
  =============================

  OPTICAL (PPG — Photoplethysmography):
  LED illuminates skin -> photodetector measures backscattered light
  Blood volume changes with heartbeat -> oscillating signal
  Heart rate: peak detection in PPG signal
  SpO2 (blood oxygen): ratio of red (660nm) to IR (940nm) PPG
      Hb absorbs more red, HbO2 absorbs more IR -> SpO2 ratio
      Typical accuracy: ±2% at SpO2 >90%
  Wrist (Apple Watch, Fitbit): motion artifact is major challenge
  Finger (pulse ox): more accurate, clinical grade (SpO2 certified)
  Continuous blood pressure: in-development (calibration remains unsolved)

  ECG PATCHES:
  Zio (iRhythm): adhesive patch, 14-day Holter equivalent
  -> remote cardiac rhythm monitoring
  Electrode pair on skin -> differential amplifier -> filtered ECG
  AI-annotated arrhythmia report to cardiologist
  FDA cleared (Class II) for atrial fibrillation detection

  Apple Watch ECG: lead-I equivalent (finger to watch case)
  FDA cleared for AFib detection

  SWEAT SENSORS (research -> early commercial):
  Electrochemical sensors integrated in wristband/patch
  Measure: Na+, K+, Cl-, glucose, lactate, cortisol in sweat
  Challenge: sweat is highly variable in composition and rate
  Not clinical grade; wellness/research applications
  FIDO Biosciences, Eccrine Systems: early commercial stage

  CONTINUOUS BLOOD GLUCOSE (non-invasive):
  Multiple approaches (NIR spectroscopy, Raman, microwave, US)
  None have achieved FDA clearance as of 2026
  Samsung Galaxy watches promote "metabolic health" measures —
  regulatory status varies; not cleared for clinical decisions
  Abbott Libre Sense: interstitial fluid glucose via NFC, launched EU
  CGM remains gold standard
```

---

## Common Confusion Points

**Sensitivity vs. LOD**: Analytical sensitivity is the slope of the calibration curve (signal
per unit concentration). Limit of detection (LOD) is the minimum detectable concentration
(typically 3σ above blank). High sensitivity (steep slope) enables low LOD but they are not
the same thing. Clinical sensitivity/specificity are diagnostic performance metrics (different
concept entirely — TP/(TP+FN) and TN/(TN+FP)).

**Lateral flow test reading**: A faint test line IS positive. Any visible line, however faint,
indicates analyte presence. "No line" is invalid (control line must always appear). This is
confusing because intensity intuitively suggests amount, but the binary read is line/no line.

**CRISPR diagnostics vs. CRISPR editing**: The same Cas proteins are used very differently.
In genome editing, a precisely designed guide RNA directs Cas9 to cut one specific location.
In diagnostics, the target-activated collateral cleavage (Cas12/Cas13 property that is
deliberately avoided in editing) is the signal amplification mechanism. Completely different
applications of the same enzyme family.

**CGM measures interstitial glucose, not blood glucose**: The sensor is in subcutaneous tissue,
measuring glucose in interstitial fluid (ISF), not blood. ISF glucose lags blood glucose by
5-15 minutes, particularly during rapid glucose changes (after meals, exercise). This "lag" is
physiological, not a device error. Clinical decisions (e.g., insulin dosing during hypoglycemia)
should confirm with fingerstick blood glucose.

**QCM vs. SPR**: Both are label-free surface binding sensors. QCM measures mass (frequency
shift). SPR measures refractive index change (related to mass but also molecular structure).
SPR (Biacore) has higher sensitivity for small molecules and gives clean kinetic data. QCM-D
adds viscoelastic information, critical for hydrogels and cell layers. For typical antibody-
antigen kinetics in pharma, SPR is the standard.

---

## Decision Cheat Sheet

| Sensing need | Transduction mechanism | Platform |
|---|---|---|
| Glucose (continuous in vivo) | Amperometric enzymatic | CGM (Dexcom, Libre) |
| Rapid antigen (virus, bacteria) | Immunochromatography | Lateral flow assay |
| Protein kinetics (kon, koff) | SPR optical | Biacore (Cytiva) |
| Pathogen nucleic acid | RT-PCR or CRISPR | GeneXpert, SHERLOCK |
| Electrolytes at point of care | Potentiometric ISE | i-STAT (Abbott) |
| Thin film mass deposition | Piezoelectric QCM | QCM-D (Biolin Q-Sense) |
| Cardiac rhythm (ambulatory) | ECG electrodes | Zio patch, Apple Watch |
| Blood oxygen | PPG optical | Pulse oximeter |
| Drug-target binding affinity | Label-free SPR | Biacore or LSPR |
| Cell signaling, metabolites | Impedimetric or optical | Lab-on-chip, organ-on-chip |
| Multiplexed pathogen panel | PCR microfluidics | BioFire FilmArray |
