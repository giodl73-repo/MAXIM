# Medical Devices — Regulatory Framework and Key Device Classes

## The Big Picture

Medical devices span everything from tongue depressors to implantable cardiac defibrillators.
The FDA's risk-stratified classification system determines the regulatory burden — which drives
development cost, timeline, and market strategy. Understanding this system is prerequisite to
understanding anything about medical device development.

```
+---------------------------------------------------------------------+
|              MEDICAL DEVICE REGULATORY FRAMEWORK                   |
+---------------------------------------------------------------------+
|                                                                     |
|  DEVICE CLASSIFICATION        MARKET ACCESS PATHWAY                 |
|                                                                     |
|  Class I                      510(k) Exempt                         |
|  (Low Risk)                   Establish design controls, QMS        |
|  ~47% of devices              File Technical File                   |
|                                                                     |
|  Class II                     510(k) or De Novo                     |
|  (Moderate Risk)              Demonstrate substantial equivalence    |
|  ~43% of devices              to predicate device                   |
|                                                                     |
|  Class III                    PMA (Premarket Approval)              |
|  (High Risk)                  Clinical evidence of safety+efficacy  |
|  ~10% of devices              IDE for clinical trials               |
|                                                                     |
|       +-------------------------------------------+                |
|       | POST-MARKET: MDR reporting, recalls, PMS  |                |
|       | UDI, MAUDE, CAPA, 21 CFR 820 QMS          |                |
|       +-------------------------------------------+                |
+---------------------------------------------------------------------+
```

---

## 510(k) Pathway in Depth

### Substantial Equivalence Framework

The 510(k) is a market access pathway, not a safety approval. The FDA is not certifying the
device is safe — it is finding it "substantially equivalent" to a device already on the market.

```
  510(k) SUBSTANTIAL EQUIVALENCE DECISION TREE
  =============================================

  STEP 1: Identify predicate(s)
  Predicate must be legally marketed:
  - Cleared via 510(k) (any year)
  - Exempt Class I/II (legally marketed before 1976)
  - Preamendment device (on market before May 28, 1976)
  NOT a valid predicate: pending 510(k), recalled, fraudulent

  STEP 2: Same intended use?
  +-- YES --> Continue
  +-- NO  --> Substantially NOT equivalent -> consider Class III

  STEP 3: Same technological characteristics?
  +-- YES --> Substantially equivalent. Done.
  +-- NO  --> Does the difference raise new safety/efficacy questions?
              +-- NO  --> Substantially equivalent (can use different tech)
              +-- YES --> Must show performance data:
                          Bench testing, animal, clinical
                          If data demonstrates safe -> SE
                          If not -> NSE (not substantially equivalent)

  REVIEW TIMELINE:
  Traditional 510(k): 90 days target, ~200 days actual
  Special 510(k): 30 days target for design changes to own cleared device
  Abbreviated 510(k): uses guidance documents, recognized standards
  De Novo: 120 days target (novel, no predicate, moderate risk)

  WHAT GOES IN A 510(k):
  Device description + substantial equivalence comparison
  Labeling (draft IFU, indications, contraindications, warnings)
  Biocompatibility (ISO 10993 data or justification)
  Performance testing (per applicable FDA guidance documents)
  Software documentation (IEC 62304 compliance if applicable)
  Sterility (if sterile device)
  Electrical safety (IEC 60601 if powered)
  EMC (IEC 60601-1-2)
```

### Predicate Strategy

```
  PREDICATE SELECTION STRATEGY
  ==============================

  Multiple predicates are allowed (and common):
  Split-predicates: intended use from Predicate A + tech from Predicate B
  Predicate chains: cleared device that used a cleared device as predicate

  PREDICATE DAISY-CHAIN CONCERNS:
  If every 510(k) clears based on predicate which itself
  predicated on an older device, technology drift occurs.
  FDA 2020: "Safety concerns about predicates" -> De Novo more enforced

  PRACTICAL STRATEGY:
  1. Search 510(k) database (FDA.gov) for competitors' cleared devices
  2. Identify their predicates from their 510(k) summaries
  3. Build a predicate tree showing lineage
  4. Choose most recent directly analogous cleared device
  5. Engage FDA via Q-sub (pre-submission meeting) before submitting
     to confirm predicate acceptance and testing approach

  Q-SUBMISSION (Pre-Sub):
  Voluntary meeting request with FDA
  Ask specific questions: Is Predicate X acceptable?
  What testing is needed for substantial equivalence?
  FDA responds in ~60 days
  Critical for novel or borderline devices — sets expectations
```

---

## PMA Pathway in Depth

### Clinical Investigation Requirements

```
  PMA — CLINICAL EVIDENCE STANDARDS
  ===================================

  PRIMARY ENDPOINT: must be pre-specified, FDA-agreed
  Examples:
  - LVAD: survival at 2 years (vs. optimal medical management)
  - Spinal implant: VAS pain score at 12 months
  - Coronary stent: MACE at 12 months (major adverse cardiac events)

  STUDY DESIGN OPTIONS:
  Randomized controlled trial (RCT): gold standard, required when
  feasible. Control arm = standard of care or sham procedure.
  Historically controlled: when RCT is not feasible
  (e.g., no standard therapy for severe condition)
  Objective performance criterion (OPC): compare to literature-
  derived performance benchmark (for device classes with
  established benchmarks)

  IDE TYPES:
  Significant Risk (SR) Study:
  -> Full IDE application to FDA required
  -> IRB approval at each site
  -> FDA holds 30 days before enrollment begins
  -> Annual reports, adverse event reporting

  Non-Significant Risk (NSR) Study:
  -> No FDA IDE application needed
  -> IRB approval still required
  -> Record keeping and labeling requirements still apply
  -> NSR determination made by sponsor + IRB

  PIVOTAL vs. FEASIBILITY STUDIES:
  Feasibility (pilot): small, demonstrate can be done safely,
                       collect preliminary data, refine design
  Pivotal: statistically powered, endpoints pre-agreed with FDA,
           used in PMA submission
```

### PMA Application Structure

```
  PMA APPLICATION MODULES
  ========================

  Modular PMA (common approach):
  Module 1: Device Description
  Module 2: Non-Clinical Tests (bench, animal studies)
  Module 3: Manufacturing Information (facilities, processes)
  Module 4: Clinical Data (pivotal study results)
  Module 5: Labeling
  Module 6: Summary of Safety and Effectiveness Data (SSED)

  Review process:
  Filing review (45 days): complete or refuse to file?
  Substantive review (90-180 days): FDA reviewer + 2nd reviewer
  Advisory Committee meeting (optional but common for novel devices)
  FDA inspection of manufacturing facility
  Approval letter or approval with conditions

  FAILURE MODES IN PMA:
  Not approvable letter: significant deficiencies, need more data
  Approvable letter: minor issues, specific conditions to address
  Complete Response Letter: most common form, request more info
  Approval order: cleared to market with labeling as approved
```

---

## Design Controls — 21 CFR 820.30

Design controls are the regulatory heart of device development. The FDA can inspect your
Design History File (DHF) at any time.

```
  DESIGN CONTROLS DETAILED — 21 CFR 820.30
  =========================================

  (a) GENERAL: requires design control procedures for Class II/III
               Class I: generally exempt from design controls

  (b) DESIGN AND DEVELOPMENT PLANNING:
      Plans must identify responsible staff, interfaces,
      controlled documents, schedule. Living document.

  (c) DESIGN INPUT:
      User needs -> formal design requirements
      Physical, performance, safety requirements
      Regulatory requirements
      Standards compliance
      Must be documented and reviewed

  (d) DESIGN OUTPUT:
      Device drawings, specs, software, manufacturing procedures
      Must meet design inputs
      Must identify critical characteristics (acceptance criteria)

  (e) DESIGN REVIEW:
      Formal reviews at major design phases
      Multi-disciplinary team (must include independent reviewer)
      Results documented in DHF

  (f) DESIGN VERIFICATION:
      Testing that design outputs meet design inputs
      "Did we build it according to the spec?"
      Test reports signed by appropriate authority

  (g) DESIGN VALIDATION:
      Test against actual or simulated user needs
      "Did we build the right thing?"
      Must include simulated or actual use conditions
      Human factors validation (21 CFR 820.30(g), HE75)

  (h) DESIGN TRANSFER:
      Ensures manufacturing can reproduce the design
      Production specifications = design outputs

  (i) DESIGN CHANGES:
      All changes require formal review and approval
      Assess if change requires new verification/validation
      Re-submit 510(k) if change affects safety/efficacy

  (j) DESIGN HISTORY FILE (DHF):
      The auditable package of all the above
      FDA inspectors will ask for DHF
      Must be organized, indexed, retrievable
      Bridge: DHF = formalized git blame + spec docs + test reports
              + sign-offs in an auditable package
```

---

## Cardiovascular Devices

### Coronary Stents

```
  CORONARY STENTS
  ================

  BARE METAL STENT (BMS):
  316L SS or CoCrMo metallic scaffold
  Deployed via balloon catheter in coronary artery
  Opens blocked artery, holds lumen patent
  Problem: restenosis (re-narrowing) in 20-30% at 6 months
  Mechanism: neointimal hyperplasia (smooth muscle cell proliferation)
  BMS now largely replaced by DES except specific indications

  DRUG-ELUTING STENT (DES) — current standard:
  Metal scaffold + polymer coating + antiproliferative drug

  STENT DESIGN ANATOMY:
  Strut thickness: 60-100 μm (thinner = less inflammation = less restenosis)
  Metal: CoCrMo (higher radial strength at thinner struts than SS)
  Polymer: biodegradable (PLGA) or durable (fluoropolymer)
  Drug: sirolimus (rapamycin) — mTOR inhibitor, blocks cell cycle
        paclitaxel — stabilizes microtubules, blocks mitosis
        zotarolimus, everolimus — sirolimus derivatives

  DES MECHANISM:
  Drug elutes over 30-90 days (biphasic: burst + sustained)
  Inhibits smooth muscle cell migration and proliferation
  -> near-zero restenosis (<5%) vs. BMS ~20-30%

  LATE STENT THROMBOSIS:
  DES risk: delayed endothelialization of struts
  -> bare metal on strut surface -> thrombogenic
  Managed with DAPT (dual antiplatelet therapy) for 1-12 months
  First-gen DES: higher late thrombosis risk (thick polymer, high drug dose)
  Second-gen (current): thinner struts, biocompatible polymer -> safer

  BIORESORBABLE VASCULAR SCAFFOLD (BVS):
  PLLA scaffold + drug coating -> absorbs over 3 years
  Concept: restore vasomotion, avoid permanent foreign body
  Abbott Absorb BVS: approved, then voluntarily recalled (2017)
  -> higher late thrombosis and stent fracture vs. DES
  Still active research; newer designs in trials

  FDA REGULATION: Class III PMA for coronary DES
```

### Pacemakers

```
  PACEMAKERS
  ==========

  INDICATION:
  Bradycardia: heart rate too slow
  AV block: electrical conduction block between atria and ventricles
  Sick sinus syndrome

  PACEMAKER TYPES:
  Single-chamber (VVIR): right ventricle lead only
  Dual-chamber (DDDR): right atrium + right ventricle leads
  Biventricular (CRT — Cardiac Resynchronization Therapy):
    RV + LV + RA leads: for heart failure with LBBB (dyssynchrony)
    Resynchronizes ventricular contraction -> improved EF
  Leadless pacemaker: Medtronic Micra — capsule deployed directly
    into RV via catheter (no leads, no pocket needed)

  PACEMAKER FUNCTION:
  Sensing: detects native cardiac depolarizations
  Pacing: delivers electrical stimulus when no native beat detected
  Demand mode: paces only when needed (inhibited by native beats)
  Rate response: increases rate with activity (accelerometer, minute ventilation)

  LEAD DESIGN:
  Active fixation: helical screw extends from tip into myocardium
  Passive fixation: tines or fins catch in trabeculae
  Bipolar: tip + ring electrode on same lead (better sensing)
  Unipolar: tip electrode + can (housing) as return (larger pacing radius)

  SENSING THRESHOLDS:
  P-wave: >1.5 mV (atrial sensing), >2 mV preferred
  R-wave: >5 mV (ventricular sensing), >7 mV preferred
  Pacing threshold: <1.5 V @ 0.4 ms (energy efficiency)

  PACEMAKER SYNDROME: AV dyssynchrony from single-chamber pacing
  Solution: dual-chamber or biventricular pacing

  FDA REGULATION: Class III PMA
```

### ICD — Implantable Cardioverter-Defibrillator

```
  ICD — IMPLANTABLE CARDIOVERTER-DEFIBRILLATOR
  ==============================================

  INDICATION:
  Primary prevention: ejection fraction <35% (at risk for SCD)
  Secondary prevention: survived VF or hemodynamically unstable VT

  ICD THERAPY HIERARCHY:
  1. ATP (Anti-Tachycardia Pacing): rapid burst or ramp pacing
     -> terminates monomorphic VT ~75-90% of the time painlessly
  2. Low-energy cardioversion (1-15 J): for VT not responding to ATP
  3. High-energy defibrillation (up to 40 J): for VF
     The shock is PAINFUL — equivalent to kick in chest
     -> programming to maximize ATP use and minimize shocks

  DETECTION ZONES:
  VT zone (150-200 bpm): ATP first, then shock if needed
  VF zone (>200 bpm): immediate shock

  SPURIOUS SHOCKS:
  T-wave oversensing: high T-wave amplitude detected as R -> double counts
  Supraventricular tachycardia (SVT): AF, SVT misdetected as VT
  Lead fracture: noise detected as VF -> inappropriate shock
  Discrimination algorithms: PR Logic, Wavelet, SVT-VT discrimination
  Rate + morphology + onset + stability to distinguish SVT from VT

  S-ICD (Subcutaneous ICD — Boston Scientific):
  No intravascular leads — electrode on thorax
  Senses surface ECG analog, delivers 80 J shock through chest wall
  No pacing capability (unless combined with leadless pacemaker)
  Advantage: no vascular access, no lead complications, removable
  Limitation: no ATP, no pacing, sensing affected by patient movement

  FDA REGULATION: Class III PMA
```

### LVAD — Left Ventricular Assist Device

```
  LVAD — LEFT VENTRICULAR ASSIST DEVICE
  ======================================

  INDICATION:
  Bridge to transplant (BTT): keep patient alive until donor heart
  Bridge to candidacy: deteriorating patient may become transplant eligible
  Destination therapy (DT): permanent implant for ineligible-for-transplant

  PHYSIOLOGY:
  Cannula in LV apex -> pump -> outflow graft to ascending aorta
  Pump augments (not replaces) LV output
  Reduces LV filling pressure, increases forward flow
  Some myocardial recovery possible (bridge to recovery — rare)

  PUMP TYPES:
  GENERATION 1: pulsatile (pneumatic or electric) — HeartMate XVE
  Large, heavy, wear on moving parts, loud. Replaced.

  GENERATION 2: axial continuous flow — HeartMate II (still widely used)
  Single moving part (impeller on bearings/jewel bearings)
  Smaller, quieter, better 2-year survival vs Gen 1
  Risk: pump thrombosis at bearings -> strokes, pump failure

  GENERATION 3: centrifugal flow, magnetically levitated — HeartMate 3
  Impeller suspended magnetically (no contact bearings)
  Wide gap minimizes blood cell damage (hemolysis)
  Artificial pulse: programmed speed modulation
  HeartMate 3: best 2-year outcomes of any LVAD (MOMENTUM 3 trial)
  Medtronic HVAD: centrifugal, wearable — withdrawn 2021 (stroke risk)

  COMPLICATIONS:
  Stroke (ischemic and hemorrhagic) — leading cause of morbidity
  Gastrointestinal bleeding (acquired vWF deficiency from shear)
  Driveline infection (percutaneous cable)
  Right heart failure (increased LVAD flow -> RV volume overload)
  Pump thrombosis (HM2 more than HM3)

  MANAGEMENT:
  INR 2.0-3.0 (anticoagulation)
  Antiplatelet (aspirin) in addition
  BP management (mean arterial pressure 70-90 mmHg)
  Continuous flow: no pulsatile BP -> MAP measured, not systolic/diastolic

  FDA REGULATION: Class III PMA (HeartMate 3 PMA P160054)
```

---

## Infusion Pumps

```
  INFUSION PUMPS
  ==============

  TYPES:
  +-------------------+------------------------------------------------+
  | Syringe pump      | Syringe driven by stepper motor               |
  |                   | Very precise, low flow rates (0.1-300 mL/hr)   |
  |                   | ICU/OR for vasoactive drugs, opioids           |
  +-------------------+------------------------------------------------+
  | Volumetric pump   | Peristaltic cassette mechanism                 |
  | (general purpose) | 1-999 mL/hr. IV fluids, antibiotics, chemo    |
  +-------------------+------------------------------------------------+
  | PCA pump          | Patient-controlled analgesia                   |
  | (patient-control) | Patient button triggers dose within limits     |
  |                   | Lockout interval prevents overdose             |
  +-------------------+------------------------------------------------+
  | Ambulatory pump   | Small, wearable (CADD, Walkmed)                |
  |                   | Home chemo, total parenteral nutrition          |
  +-------------------+------------------------------------------------+
  | Insulin pump      | Continuous subcutaneous insulin infusion (CSII)|
  |                   | Basal + bolus. Medtronic MiniMed 780G,         |
  |                   | Insulet Omnipod 5 (tubeless, patch pump)       |
  +-------------------+------------------------------------------------+

  SAFETY ARCHITECTURE:
  DERS (Drug Error Reduction Software = Drug Library):
  Pre-programmed drug library with soft limits (warnings) and
  hard limits (cannot be overridden) for each drug
  Pump alerts if programmed dose exceeds drug library limit
  Interoperability: BCMA (barcode medication administration) + pump
  -> EHR verifies drug and links to pump program

  OCCLUSION DETECTION:
  Downstream occlusion: pressure rises -> alarm
  Air-in-line detection: ultrasonic or optical air detector
  Free-flow prevention: anti-free-flow mechanism (clamp)

  FDA CLASSIFICATION: Class II (510(k))
  FDA has issued many recall notices for infusion pump software
  -> high-profile safety concern (insulin pump recalls)
  Device software under IEC 62304 + 21 CFR 820
```

---

## Mechanical Ventilators

```
  MECHANICAL VENTILATORS
  =======================

  MODES OF VENTILATION:
  +---------------------+----------------------------------------------+
  | Volume Control (VC) | Set tidal volume VT delivered each breath    |
  |                     | Pressure varies (risk: high pressure = barotrauma)|
  |                     | Set: VT, RR, FiO2, PEEP                     |
  +---------------------+----------------------------------------------+
  | Pressure Control    | Set inspiratory pressure (PC above PEEP)     |
  | (PC)                | Volume varies (depends on compliance)         |
  |                     | Better for non-uniform lung disease           |
  +---------------------+----------------------------------------------+
  | SIMV                | Synchronized intermittent mandatory vent.    |
  |                     | Delivers set number of mandatory breaths      |
  |                     | Patient can breathe spontaneously between     |
  +---------------------+----------------------------------------------+
  | PSV (Pressure       | Patient-triggered, pressure-supported         |
  | Support)            | Patient determines RR and VT within limits   |
  |                     | Standard for weaning from ventilator          |
  +---------------------+----------------------------------------------+

  KEY PARAMETERS:
  FiO2: fraction of inspired O2 (0.21 = room air to 1.0 = 100% O2)
  PEEP (Positive End-Expiratory Pressure): maintains alveoli open
        at end of expiration. Prevents derecruitment.
        Normal: 5 cmH2O. ARDS: 8-20 cmH2O.
  Tidal volume (VT): normal physiology ~7 mL/kg. ARDS: 4-6 mL/kg IBW
  Plateau pressure (Pplat): proxy for alveolar pressure (barotrauma risk)
        Target <30 cmH2O; ARDSNet protocol targets <30 cmH2O

  LUNG-PROTECTIVE VENTILATION (ARDSNet protocol):
  Low VT (6 mL/kg IBW) + high PEEP + permissive hypercapnia
  Reduces volutrauma and barotrauma
  Proven to reduce mortality in ARDS (ARMA trial 2000)

  COVID-19 VENTILATOR SUPPLY CHAIN CRISIS (2020):
  ARDS in COVID required positive pressure ventilation
  US/global supply ~170,000 ventilators (needed: 750,000 estimate)
  Emergency manufacturing: GM, Ford, GE partnered with Ventec, Hamilton
  FDA issued EUA (Emergency Use Authorization) for modified/simplified vents
  Key lesson: Class III device supply chains are as critical as software infrastructure
  -> CAPA and post-market supply monitoring matter for national security

  FDA CLASSIFICATION: Class II (510(k)) for many; Class III (PMA) for high-risk ICU vents
```

---

## Combination Products

```
  COMBINATION PRODUCTS
  ====================

  A combination product has:
  - Drug + device (drug-eluting stent: sirolimus in polymer on metallic scaffold)
  - Device + biologic (bone graft + collagen scaffold)
  - Drug + biologic + device

  FDA LEAD CENTER ASSIGNMENT:
  Office of Combination Products (OCP) determines which center leads review:
  CDRH: Center for Devices and Radiological Health
  CDER: Center for Drug Evaluation and Research
  CBER: Center for Biologics Evaluation and Research

  LEAD CENTER = PRIMARY MODE OF ACTION:
  Drug-eluting stent: device primary (mechanically holds lumen open)
    -> CDRH leads, CDER consults on drug
  Drug-device combination (e.g., drug-coated balloon):
    -> CDRH leads typically
  Autologous cell therapy on scaffold:
    -> CBER leads (biological component is primary)

  EXAMPLES:
  +----------------------------+--------+-----------------------------+
  | Product                    | Class  | Lead Center                |
  +----------------------------+--------+-----------------------------+
  | Drug-eluting stent         | III PMA| CDRH leads / CDER consult  |
  | Drug-coated balloon        | III PMA| CDRH                       |
  | Antibiotic-eluting nail    | II/III | CDRH / CDER                |
  | Cellular bone matrix       | ---    | CBER                       |
  | Insulin + pump (combo app) | II/III | CDRH for device piece      |
  +----------------------------+--------+-----------------------------+
```

---

## UDI — Unique Device Identifier

```
  UDI SYSTEM (21 CFR 830)
  =======================

  Every medical device must bear a UDI label (phased in by class):
  Class III: required since 2014
  Class II: since 2016
  Class I: since 2020

  UDI FORMAT: two components
  Device Identifier (DI): identifies device manufacturer + model
  Production Identifier (PI): specific production info
    -> lot/batch number
    -> serial number
    -> manufacturing date
    -> expiration date
    -> distinct identification code (for HCT/P)

  BARCODE FORMATS:
  GS1-128 (linear), HIBCC (linear), ISBT 128 (blood)
  DataMatrix (2D), QR (2D)

  GUDID (Global UDI Database):
  FDA's public searchable database of all device UDI records
  Manufacturers must register each device model in GUDID

  CLINICAL USE:
  EMR integration: scan device barcode at implantation -> auto-
    populates implant record. Enables recall management.
  Recall: FDA issues recall for specific DI/PI range ->
    hospitals can quickly identify affected inventory

  EU: EUDAMED serves analogous function for CE-marked devices
```

---

## Common Confusion Points

**Class I vs. "exempt from 510(k)"**: All Class I devices must still comply with general controls
(labeling, registration, QMS records). "Exempt from 510(k)" means no premarket submission is
required — not exempt from all regulation. Class II devices may also be "510(k) exempt" if a
special controls guidance establishes they don't need a 510(k) (e.g., some accessories).

**510(k) is NOT a safety certification**: The FDA's clearance letter specifically states the
device is "substantially equivalent" — it does not state the device is safe or effective. This
has regulatory and marketing implications. Saying "FDA-certified" or "FDA-approved" for a
510(k) device is false and potentially misleading. The FDA has issued warning letters for this.

**DES late thrombosis**: Drug-eluting stents prevent restenosis by inhibiting smooth muscle
proliferation, but the same mechanism delays endothelialization of the metallic struts.
Uncovered metal is thrombogenic. DAPT (dual antiplatelet therapy) bridges this gap. Stopping
DAPT early is a major cause of late stent thrombosis — a potentially fatal complication.

**LVAD "destination therapy" is not palliation**: In FDA regulatory language, destination therapy
(DT) means permanent implant for patients not eligible for cardiac transplant — it is *definitive
treatment*, not bridge therapy. Outcomes for DT with HeartMate 3 at 2 years exceed what was
historically achievable even as BTT.

**Infusion pump drug library is not foolproof**: Soft limits can be overridden by clinicians
(after acknowledgment). Hard limits cannot. The drug library requires ongoing pharmacy
management — out-of-date libraries, wrong concentrations, or missing drugs are common
implementation failures. ISMP publishes many infusion-pump-related medication error reports.

---

## Decision Cheat Sheet — Regulatory Strategy

| Device type and situation | Regulatory approach |
|---|---|
| Novel Class I, straightforward | 510(k) exempt; register device, comply with QMS |
| Similar to cleared competitor | 510(k); use competitor's device as predicate |
| Novel technology, moderate risk, no predicate | De Novo request; creates new classification |
| Life-sustaining novel device | PMA; plan 3-5 years from IDE to approval |
| Design change to own cleared device | Special 510(k) if safety/effectiveness unaffected |
| Significant change (material, software class C) | Traditional 510(k) or letter-to-file assessment |
| Investigational use in US | IDE (significant risk) or IRB-only (non-sig risk) |
| Drug-device combination | Office of Combination Products letter; CDRH usually leads |
| SaMD (Software as Medical Device) | SaMD 510(k) per DeNovo or cleared class; SaMD predetermination pathway |
| International + US simultaneous | ISO 13485 QMS + MDSAP audit covers FDA/EU/CA/AU |
