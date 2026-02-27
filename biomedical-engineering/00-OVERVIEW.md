# Biomedical Engineering — Landscape Overview

<!-- @editor[bridge/P2]: No signal processing bridge — biomedical signals (ECG, EEG, EMG) are sampled time-series data processed with the same FIR/IIR filters, FFT, and Nyquist-sampling constraints any DSP engineer knows. Add a one-sentence bridge when signals first appear in the landscape diagram description. -->
<!-- @editor[bridge/P2]: No control theory bridge — key physiological systems are feedback control loops (baroreceptor reflex ≈ proportional controller, glucose-insulin axis ≈ PI controller with dead time). Engineers with control systems background map this structure immediately; it belongs in the overview framing. -->
<!-- @editor[bridge/P2]: Medical imaging never framed as inverse problems — CT reconstruction is Radon transform inversion; MRI k-space is Fourier reconstruction. This is one of the most powerful conceptual bridges for an engineer with signal processing or numerical methods background. At minimum, add a note in the landscape diagram. -->
## The Big Picture

Biomedical engineering applies engineering principles to biology and medicine. Six subdisciplines
compose the field, each with distinct physics, methods, and regulatory touch points. All of them
feed into the medical device lifecycle — from bench to bedside — governed by the FDA and
international equivalents.

```
+---------------------------------------------------------------------+
|              BIOMEDICAL ENGINEERING — FIELD MAP                     |
+---------------------------------------------------------------------+
|                                                                     |
|  BIOMECHANICS        BIOMATERIALS        MEDICAL IMAGING            |
|  (forces & motion)   (implant materials) (non-invasive view)        |
|  Bone, cartilage,    Metals, ceramics,   MRI, CT, PET,             |
|  muscle, gait,       polymers, composites,ultrasound, SPECT         |
|  FEA, fatigue        biocompatibility                               |
|       |                    |                    |                   |
|       v                    v                    v                   |
|  +-----------------------------------------------------------+      |
|  |          MEDICAL DEVICE LIFECYCLE                         |      |
|  |  Research -> Design -> V&V -> Regulatory -> Clinical ->   |      |
|  |  Post-Market Surveillance -> CAPA -> Iteration            |      |
|  +-----------------------------------------------------------+      |
|       ^                    ^                    ^                   |
|       |                    |                    |                   |
|  BIOSENSORS/DIAG     NEURAL INTERFACES    TISSUE ENGINEERING        |
|  (detect & measure)  (brain-machine)      (grow it back)           |
|  Electrochemical,    EEG, Utah array,     Scaffolds, iPSC,         |
|  optical, CGM,       BCI, DBS,            bioreactors,             |
|  lateral flow,       cochlear implants    3D bioprinting            |
|  CRISPR diagnostics                                                 |
+---------------------------------------------------------------------+

  CROSS-CUTTING: ISO 13485 (QMS) | ISO 14971 (Risk) | ISO 10993 (Biocompat)
                 FDA / CE marking / PMDA | UDI | CAPA | Design Controls
```

---

## FDA Device Classification — Risk-Stratified Regulation

The FDA classifies medical devices by risk. Same technology, different risk profile = different
class and different regulatory pathway.

```
+-------------------------------------------------------------+
|  FDA DEVICE CLASSIFICATION                                  |
|                                                             |
|  CLASS I          CLASS II           CLASS III              |
|  (Low Risk)       (Moderate Risk)    (High Risk)            |
|  General          General +          General +              |
|  Controls         Special Controls   Special Controls +     |
|  only                                Premarket Approval     |
|                                                             |
|  510(k) EXEMPT    510(k) REQUIRED    PMA REQUIRED           |
|  (~47% of devices)(most devices)     (life-sustaining or    |
|                                       life-supporting)      |
|                                                             |
|  Examples:        Examples:          Examples:              |
|  Tongue           Blood pressure     Pacemakers             |
|  depressors       monitors           Heart valves           |
|  Bandages         Infusion pumps     Cochlear implants      |
|  Exam gloves      Glucose meters     LVADs                  |
|  Stethoscopes     Endoscopes         Deep brain stim.       |
|                   Surgical robots    Neurovascular stents   |
+-------------------------------------------------------------+
```

### 510(k) — Predicate Clearance (Class II, most common path)

The 510(k) is not approval — it is *clearance*. The standard is **substantial equivalence** to
a legally marketed predicate device.

```
  510(k) SUBSTANTIAL EQUIVALENCE DECISION TREE
  =============================================

  YOUR DEVICE
      |
      v
  Same intended use as predicate? ----NO----> Different class or De Novo
      |
      YES
      v
  Same technological characteristics? ----YES----> SUBSTANTIALLY EQUIVALENT
      |                                             (cleared)
      NO
      v
  New questions of safety/efficacy raised?
      |                    |
      NO                   YES
      v                    v
  SUBSTANTIALLY      Not substantially equivalent
  EQUIVALENT         -> PMA track or De Novo
  (can still clear)

  Timeline: 90 days statutory, ~180 days in practice
  Special 510(k): streamlined path for design changes to your own cleared device
  De Novo: novel moderate-risk device, no valid predicate -> creates new classification
           -> that De Novo can then serve as predicate for future 510(k)s
```

### PMA — Premarket Approval (Class III)

PMA requires clinical evidence of both safety AND effectiveness. No predicate game — you prove
it with data.

```
  PMA PATHWAY
  ===========

  IDE (Investigational Device Exemption)
      |
      |  Authorized to conduct clinical investigation
      v
  Clinical Trial (Phase II/III equivalent)
      |
      |  Statistical endpoints pre-specified and met
      v
  PMA Application
  - Clinical data (pivotal study)
  - Preclinical data (bench testing, animal studies)
  - Manufacturing information (facility inspection)
  - Labeling
      |
      |  FDA Review (~180 days statutory, often 1-2+ years actual)
      v
  PMA Approval + Advisory Committee vote (often required)

  Post-approval requirements:
  - PMA Supplements for changes to design, manufacturing, labeling
  - Annual reports
  - Post-market studies frequently mandated
  - MDR (Medical Device Reporting) for adverse events
```

### IDE — Investigational Device Exemption

Any US clinical study with a non-cleared device that poses significant risk requires an IDE
before enrolling the first subject. Non-significant-risk devices are automatically approved under
IRB oversight.

---

## EU MDR — CE Marking

EU Medical Device Regulation (EU MDR 2017/745) replaced MDD in 2021. Stricter than MDD —
clinical evidence requirements now resemble PMA for high-risk devices.

```
+-------------------------------------------------------------+
|  EU MDR DEVICE CLASSIFICATION                               |
|                                                             |
|  Class I      Class IIa      Class IIb      Class III       |
|  (Lowest)                                   (Highest)       |
|                                                             |
|  Self-declare  Notified Body  Notified Body  Notified Body  |
|  CE (some NB   review         full review    + clinical     |
|  for sterile/                               evidence        |
|  measuring)                                                 |
|                                                             |
|  CE Mark = Declaration of Conformity + Technical File       |
|            + Notified Body Certificate (IIa and above)      |
+-------------------------------------------------------------+

  EU MDR vs FDA comparison:
  +---------------------------+----------------------------+
  | FDA                       | EU MDR                     |
  +---------------------------+----------------------------+
  | Government agency review  | Notified Body (private)    |
  | Predicate system (510k)   | GSPR conformity            |
  | PMA for Class III         | Clinical evaluation + NB   |
  | UDI system                | EUDAMED + UDI              |
  | MAUDE adverse event DB    | National competent auth.   |
  | MDR reporting             | Vigilance reporting        |
  +---------------------------+----------------------------+
```

---

## ISO 13485 — Medical Device Quality Management System

ISO 13485 is the QMS standard for medical device manufacturers. ISO 9001 with device-specific
additions and regulatory teeth — required for CE marking and strongly expected by FDA.

```
  ISO 13485 STRUCTURE
  ===================

  +------------------------------------------------------+
  |  QUALITY MANAGEMENT SYSTEM                           |
  |                                                      |
  |  Management Responsibility                           |
  |  -> Quality policy, objectives, management review    |
  |                                                      |
  |  Resource Management                                 |
  |  -> Personnel competence, infrastructure             |
  |                                                      |
  |  Product Realization  <--- THE CORE                  |
  |  -> Design Controls (21 CFR 820.30)                  |
  |  -> Risk Management (ISO 14971)                      |
  |  -> Supplier qualification and purchasing controls   |
  |  -> Production and service controls                  |
  |  -> Traceability (lot/serial records)                |
  |  -> Sterile device controls                          |
  |                                                      |
  |  Measurement, Analysis, Improvement                  |
  |  -> CAPA (corrective and preventive action)          |
  |  -> Internal audits                                  |
  |  -> Post-market surveillance                         |
  +------------------------------------------------------+
```

---

## Design Controls — The SDLC Bridge

21 CFR 820.30 mandates design controls for Class II and III devices. This is the FDA's
formalized SDLC — the analogy to software development is direct and intentional.

```
  DESIGN CONTROLS (21 CFR 820.30) <-> SOFTWARE ENGINEERING PARALLEL
  =================================================================

  DESIGN INPUT          = Requirements specification
  (what it must do)       User needs → design requirements

  DESIGN OUTPUT         = Architecture docs + device itself
  (how it does it)        Drawings, specifications, software

  DESIGN VERIFICATION   = Unit and integration testing
  (outputs meet inputs?)  "Did we build it according to spec?"

  DESIGN VALIDATION     = User acceptance testing (UAT)
  (device meets user need)"Did we build the right thing?"
                          Simulated use or actual use studies

  DESIGN REVIEW         = Design review gates
  (formal checkpoints)    Documented, cross-functional

  DESIGN TRANSFER       = DevOps / release engineering
  (R&D -> Manufacturing)  Manufacturing can replicate it

  DESIGN CHANGES        = Change control process
  (controlled iterations) Every change reviewed, tested, documented

  DESIGN HISTORY FILE   = Git blame + spec docs + test results
  (DHF — the audit trail)  Coherent record of the entire design process
                           FDA inspectors pull this first
```

---

## Risk Management — ISO 14971

Every medical device needs a risk management file per ISO 14971. FMEA is the primary tool,
covering the full device lifecycle including intended use, foreseeable misuse, and environment.

```
  ISO 14971 RISK MANAGEMENT PROCESS
  ==================================

  1. RISK ANALYSIS
     Identify hazards (what can go wrong for patient, user, environment?)
     Estimate probability P and severity S
     Risk = P x S

  2. RISK EVALUATION
     Compare to pre-defined acceptability criteria
     Acceptable? -> document and continue
     Not acceptable? -> apply risk controls

  3. RISK CONTROL (priority order — must justify if skipping down)
     a. Inherently safe design (remove the hazard)
     b. Protective measures (guards, alarms, interlocks)
     c. Information for safety (warnings, labeling, IFU)

  4. RESIDUAL RISK EVALUATION
     After controls applied: still acceptable?

  5. RISK-BENEFIT ANALYSIS
     Class III: even high residual risk can be acceptable
     if clinical benefit outweighs it — must be documented

  6. POST-MARKET FEEDBACK LOOP
     Real-world adverse event data updates risk file
     CAPA may be required

  FMEA row structure:
  Function | Failure Mode | Effect | Sev | Prob | RPN | Control | Residual
```

---

## The Medical Device Lifecycle

```
  MEDICAL DEVICE LIFECYCLE
  ========================

  CONCEPT & NEED
  Unmet clinical need, literature review, IP landscape, KOL interviews
      |
      v
  DESIGN & DEVELOPMENT
  Design controls (21 CFR 820.30), bench testing, animal testing (GLP),
  ISO 14971 risk management, design freezes, V&V testing
      |
      |  IDE application (if clinical trial needed for US)
      v
  CLINICAL INVESTIGATION
  Pivotal study or clinical evaluation (EU), IRB/Ethics board,
  informed consent, statistical endpoints, monitoring
      |
      v
  REGULATORY SUBMISSION
  510(k) / De Novo / PMA (US) + CE Mark / MDR (EU) + PMDA (Japan)
  Labeling, UDI, Quality System evidence
      |
      v
  CLEARANCE / APPROVAL
  FDA clearance letter or PMA approval order
  CE certificate from Notified Body
      |
      v
  COMMERCIAL LAUNCH
  Physician training, reimbursement strategy (CPT codes, CMS coverage),
  post-market surveillance plan activated
      |
      v
  POST-MARKET SURVEILLANCE
  MDR adverse event reporting, recalls (Class I/II/III),
  post-market studies (if mandated), CAPA, design iterations
      |
      +------- feedback loop back to DESIGN & DEVELOPMENT -----------+
```

---

## Six Subdisciplines — Cross-Cutting Standards

```
  STANDARD        SCOPE                           APPLIES TO
  ============    ==============================  ==========================
  ISO 10993       Biocompatibility test battery   Any device contacting body
  ISO 13485       QMS for device manufacturers    All regulated manufacturers
  ISO 14971       Risk management                 All medical devices
  ISO 11135       EO sterilization validation     Sterile devices
  ISO 11607       Sterile packaging               Sterile devices
  IEC 60601       Electrical safety (medical)     Powered devices
  IEC 62304       Software lifecycle process      Software in medical devices
  IEC 62366       Usability engineering           All devices (human factors)
  ASTM F2475      Packaging usability             Sterile packaging
  21 CFR 820      FDA Quality System Regulation   US-marketed devices
  EU MDR 2017/745 EU market access                EU-marketed devices
```

IEC 62304 is worth noting for software-oriented readers: it maps directly to standard software
SDLC but adds classification of software components by the severity of harm failure could cause.
Class A (no injury), Class B (non-serious injury), Class C (serious injury or death). Class C
software requires the most rigorous development and testing process.

---

## Career Map

```
  ACADEMIC / RESEARCH        INDUSTRY                    REGULATORY / CLINICAL
  ===================        ========                    ====================
  University labs            R&D Engineer                FDA reviewer / CDRH
  NIH/NSF grants             Systems Engineer            Regulatory Affairs Mgr
  Publication cycle          V&V Engineer                Notified Body assessor
  Technology transfer        Clinical Affairs            RA consultant (ex-FDA)
  SBIR bridge to industry    Quality Engineer            Hospital Clinical Eng.
  Postdoc -> faculty         Medical Science Liaison     Biomedical Technician
                             Product Management          Clinical Scientist
                             VP Engineering              IRB member

  STARTUP PATH
  Founder / CTO / CMO
  NIH SBIR/STTR Phase I ($300k) -> Phase II ($2M)
  Seed round -> Series A (usually post-IDE or post-clearance)
  Common exit: acquisition by Medtronic / Abbott / Stryker / BSN
```

---

## Common Confusion Points

**510(k) "clearance" vs. PMA "approval"**: "FDA-approved" is only technically correct for PMA
devices. 510(k) devices are "FDA-cleared." Labeling a cleared device as "FDA-approved" is a
regulatory violation — FDA warning letters have been issued for this.

**CE marking vs. ISO 13485**: CE marking means the device meets EU MDR conformity requirements.
ISO 13485 certification means the QMS meets the standard. They are different things — you need
both to place most devices on the EU market, but one does not imply the other.

**Verification vs. Validation**: Used precisely in 21 CFR 820. Verification = outputs meet
inputs (spec compliance testing). Validation = device meets user needs (real use testing).
Conflating them in an FDA audit signals QMS misunderstanding.

**IDE for clinical trials**: A cleared device used within its cleared indication does not need
an IDE for clinical studies in most cases. A non-cleared device or cleared device used off-label
for a significant-risk study requires IDE. Enrolling without IDE when required is a major
violation.

**De Novo vs. 510(k)**: When no valid predicate exists for a moderate-risk device, De Novo
creates a new device type. It is slower than 510(k) but faster than PMA. Once granted, the De
Novo device becomes the predicate for future 510(k) submissions in that category.

**IEC 62304 classification**: Software component classification is by *harm potential*, not
software complexity. Simple code that could directly cause serious patient harm = Class C.
Complex code with no direct patient safety connection = Class A.

---

## Decision Cheat Sheet — Regulatory Pathways

| Situation | US Pathway | EU Pathway |
|---|---|---|
| Low-risk device (Class I) | 510(k) exempt; general controls only | Self-declare CE (some need NB for sterile) |
| Moderate risk, has predicate | 510(k) ~90-180 days | Notified Body for IIa/IIb |
| Moderate risk, no predicate | De Novo (new classification) | Notified Body + clinical evaluation |
| High risk / life-sustaining | PMA + IDE clinical trial | Notified Body + clinical evidence |
| Investigational use only | IDE application first | Clinical Trial Authorization |
| Software as Medical Device | SaMD 510(k) or PMA per risk | MDR or IVDR depending on function |
| Combination product | Lead center assignment (CDER/CDRH/CBER) | Competent Authority leads |
| Design change to cleared device | Special 510(k) or letter-to-file | Technical file update |
