# Quality Systems: SPC, Six Sigma, ISO 9001

## The Big Picture

Quality systems span three levels: philosophical frameworks (how you think about quality), statistical methods (tools for analysis and control), and management standards (what you document and audit). They compose, they don't substitute.

```
QUALITY SYSTEM HIERARCHY
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  QUALITY PHILOSOPHY / FRAMEWORK                                  │
│  Deming (System of Profound Knowledge)                          │
│  Juran (Quality Trilogy: planning / control / improvement)      │
│  Crosby (Zero Defects, cost of quality)                         │
│  Taguchi (Robust design, loss function)                         │
├─────────────────────────────────────────────────────────────────┤
│  STATISTICAL METHODS (what to measure, how to analyze)           │
│  SPC (Statistical Process Control)                              │
│  MSA (Measurement System Analysis / Gage R&R)                   │
│  DOE (Design of Experiments — Taguchi arrays, factorial)        │
│  FMEA (Failure Mode and Effects Analysis)                        │
├─────────────────────────────────────────────────────────────────┤
│  MANAGEMENT SYSTEMS (what to document, audit, certify)           │
│  ISO 9001:2015        Generic QMS                               │
│  IATF 16949           Automotive (extends ISO 9001)             │
│  AS9100D              Aerospace/defense (extends ISO 9001)      │
│  ISO 13485            Medical devices                           │
│  GMP / 21 CFR Part 11 Pharma, FDA-regulated                     │
└─────────────────────────────────────────────────────────────────┘
```

---

<!-- @editor[bridge/P2]: Missing bridge from software monitoring/observability to manufacturing SPC — learner calibration explicitly states "knows statistical process control from software." The bridge should go the other direction here: manufacturing SPC is the origin; software SRE metrics (P99 latency, error rate control charts, anomaly detection) are the derived version. The parallel is direct: control chart → time-series anomaly detection, UCL/LCL → alert thresholds, special cause → incident, common cause → baseline noise, Cpk → process capability as a service-level metric. A "if you know software monitoring, here's what maps to manufacturing SPC" table would immediately orient this learner. -->

## Statistical Process Control (SPC)

### The Core Concept

SPC distinguishes two sources of variation:
- **Common cause (natural) variation**: inherent to the process, random, predictable distribution
- **Special cause variation**: assignable to specific event (tool wear, material change, operator error)

```
CONTROL CHART STRUCTURE
──────────────────────────────────────────────────────────────────
Measurement plotted over time:

  UCL ─────────────────────────────────────────── Upper Control Limit
        .   .                                      (μ + 3σ)
  +2σ ───────────────────────────────────────────
       . . . .
  CLn ─────────────────────────────────────────── Centerline (mean)
       . . .     .
  -2σ ───────────────────────────────────────────
           .   .
  LCL ─────────────────────────────────────────── Lower Control Limit
                                                  (μ − 3σ)

  Point outside UCL/LCL = special cause, investigate immediately
  Patterns within limits = special cause (Western Electric rules)
```

### Western Electric (Nelson) Rules

```
Process is out of control if any rule triggers:
──────────────────────────────────────────────────────────────────
Rule 1: One point beyond 3σ (UCL or LCL)
Rule 2: Two of three consecutive points beyond 2σ (same side)
Rule 3: Four of five consecutive points beyond 1σ (same side)
Rule 4: Eight consecutive points on same side of centerline
Rule 5: Six consecutive points steadily increasing or decreasing (trend)
Rule 6: Fifteen points in a row within ±1σ (too good — suspicious)
Rule 7: Fourteen points alternating up and down
```

### Common Control Charts

| Chart | What it monitors | Subgroup size |
|-------|-----------------|---------------|
| X̄-R (Xbar-R) | Mean and range of subgroups | 2–10 |
| X̄-S (Xbar-S) | Mean and std dev of subgroups | >10 |
| I-MR (Individuals-Moving Range) | Individual measurements | 1 |
| p-chart | Proportion defective | Variable |
| np-chart | Count of defectives | Fixed |
| c-chart | Count of defects per unit | Fixed |
| u-chart | Defects per unit | Variable |

### Process Capability Indices

```
CAPABILITY INDICES
──────────────────────────────────────────────────────────────────
Cp = (USL − LSL) / 6σ
  Measures spread of process relative to tolerance
  Does NOT account for centering

Cpk = min[(USL − μ)/3σ, (μ − LSL)/3σ]
  Accounts for centering
  Takes the more restrictive limit

Cp = Cpk = process perfectly centered
Cp > Cpk = process off-center (Cp = potential, Cpk = actual)

Acceptance levels:
  Cpk < 1.0   Not capable (defects inevitable)
  Cpk = 1.0   Barely capable (2700 ppm = 0.27%)
  Cpk = 1.33  4σ — minimum for most general production
  Cpk = 1.67  5σ — automotive standard (AIAG)
  Cpk = 2.0   6σ — Six Sigma goal (3.4 DPMO with 1.5σ shift)

Pp and Ppk = preliminary (short-term sample)
Cp and Cpk = ongoing (long-term, stable process)
```

---

## Six Sigma

### DMAIC Framework

```
DMAIC — the improvement methodology
──────────────────────────────────────────────────────────────────
D — DEFINE
  Problem statement, project scope, goal, stakeholders
  SIPOC diagram (Suppliers-Inputs-Process-Outputs-Customers)
  Voice of Customer (VOC) → Critical to Quality (CTQ) tree

M — MEASURE
  Baseline current performance (DPMO, Cpk)
  MSA: verify measurement system is capable (Gage R&R)
  Data collection plan

A — ANALYZE
  Root cause analysis
  Tools: 5 Why, Ishikawa (fishbone), regression, DOE
  Validate root cause with data (not just hypothesis)

I — IMPROVE
  Propose and test countermeasures
  DOE to find optimal settings
  Pilot implementation

C — CONTROL
  Implement control plan
  Update SOPs (standard operating procedures)
  Hand off to process owner
  Verify improvement sustained (30–90 days)

DFSS (Design for Six Sigma) uses DMADV:
  Define → Measure → Analyze → Design → Verify
  For new products/processes, not improvement of existing
```

### Statistical Tools in Six Sigma

```
BASIC SEVEN QUALITY TOOLS (Ishikawa's original)
  1. Flowchart / Process map
  2. Check sheet (tally of defect types)
  3. Histogram (distribution of measurements)
  4. Pareto chart (80/20 — which defects dominate?)
  5. Cause-and-effect (Ishikawa / Fishbone) diagram
  6. Scatter plot (correlation between variables)
  7. Control chart (process stability over time)

ADVANCED TOOLS
  FMEA            Failure mode risk prioritization
  DOE             Factorial experiments, find interactions
  Response Surface Optimization of multiple factors
  Regression      Correlation → prediction models
  Hypothesis test  t-test, ANOVA, chi-square (is difference real?)
  Box Plot         Compare distributions across groups
  MSA / Gage R&R   Is your measurement valid?
```

### Gage R&R (Measurement System Analysis)

```
GAGE R&R CONCEPT
──────────────────────────────────────────────────────────────────
Total variation observed = Part variation + Measurement variation

Measurement variation has two components:
  Repeatability (R): same operator, same gauge, same part → variation
  Reproducibility (R): different operators, same gauge, same part → variation

R&R study:
  10 parts × 3 operators × 2 replications = 60 measurements
  ANOVA or average/range method
  Calculate %GRR = (measurement variation / total variation) × 100%

Acceptance criteria:
  %GRR < 10%:  Acceptable gauge system
  %GRR 10–30%: Conditionally acceptable (use with caution)
  %GRR > 30%:  Unacceptable — fix gauge before interpreting data

ndc (number of distinct categories) ≥ 5: gauge can discriminate
```

---

## Measurement System Analysis (MSA)

### Beyond Gage R&R

```
FULL MSA COMPONENTS
──────────────────────────────────────────────────────────────────
Bias          Mean measurement vs true value (accuracy)
              Corrected by calibration

Stability     Bias over time (does gauge drift?)
              Detected by control chart on reference standard

Linearity     Bias consistent across measurement range?
              Important if gauge used from small to large values

Repeatability Equipment variation (EV)
Reproducibility Appraiser variation (AV)

%GRR = √(EV² + AV²) / Total variation
```

---

## ISO 9001:2015 Structure

### High-Level Structure (HLS/Annex SL)

```
ISO 9001:2015 CLAUSE MAP
──────────────────────────────────────────────────────────────────
Clause 4: Context of the Organization
  4.1 Understanding the organization and context
  4.2 Needs of interested parties
  4.3 Scope of QMS
  4.4 QMS and its processes

Clause 5: Leadership
  5.1 Leadership and commitment (top management accountable)
  5.2 Quality Policy
  5.3 Roles, responsibilities, authorities

Clause 6: Planning
  6.1 Actions to address risks and opportunities
  6.2 Quality objectives
  6.3 Planning changes

Clause 7: Support
  7.1 Resources (people, infrastructure, environment, monitoring equip)
  7.2 Competence
  7.3 Awareness
  7.4 Communication
  7.5 Documented information

Clause 8: Operation (where product is made)
  8.1 Operational planning and control
  8.2 Customer requirements
  8.3 Design and development
  8.4 External providers (purchasing, subcontractors)
  8.5 Production and service provision
  8.6 Release of products
  8.7 Control of nonconforming outputs

Clause 9: Performance Evaluation
  9.1 Monitoring, measurement, analysis
  9.2 Internal audit
  9.3 Management review

Clause 10: Improvement
  10.1 General
  10.2 Nonconformity and corrective action
  10.3 Continual improvement
```

### Risk-Based Thinking (ISO 9001:2015 key change)

2015 revision replaced "preventive action" with risk-based thinking throughout. No longer requires a separate preventive action procedure. Instead: identify risks in context (clause 4), plan actions to address risks (clause 6), control adequacy of actions.

---

## APQP and PPAP (Automotive)

```
APQP (Advanced Product Quality Planning)
──────────────────────────────────────────────────────────────────
5-phase process used in automotive supply chain (IATF 16949):

Phase 1: Plan and Define Program
  Voice of Customer, product/process benchmarking, quality goals

Phase 2: Product Design and Development
  DFMEA, design verification, design review

Phase 3: Process Design and Development
  PFMEA, floor plan, control plan, process FMEA

Phase 4: Product and Process Validation
  Production trial run, MSA, capability (Ppk > 1.67), PPAP

Phase 5: Launch, Feedback, Assessment, Corrective Action
  Production launch, lessons learned

PPAP (Production Part Approval Process)
  Documentation package submitted to customer before production:
  - Part drawing with dimensions
  - PFMEA
  - Control plan
  - MSA results
  - Capability study (Ppk ≥ 1.67)
  - Sample parts
  18 elements total (levels 1–5 based on risk/newness)
```

---

## Corrective and Preventive Action (CAPA)

```
8D (Eight Disciplines) — Common CAPA Format
──────────────────────────────────────────────────────────────────
D0: Emergency Response (if immediate containment needed)
D1: Team Formation
D2: Problem Description (5W2H: Who, What, Where, When, Why, How, How Many)
D3: Interim Containment Action (ICA) — stop the bleeding
D4: Root Cause Analysis (5 Why, fishbone, is/is-not analysis)
D5: Permanent Corrective Action (PCA) — fix the root cause
D6: Implement and Validate PCA
D7: Prevent Recurrence (update FMEA, control plan, procedures, standards)
D8: Team Recognition

Used by Ford, many automotive suppliers, defense contractors.
```

---

## Cost of Quality (COQ)

```
COQ = Prevention + Appraisal + Internal Failure + External Failure

Prevention costs:    Training, process design, poka-yoke, audits
                     Cheapest per defect prevented

Appraisal costs:     Inspection, test, calibration, CMM time
                     Finds defects before leaving facility

Internal failure:    Rework, scrap, reinspection
                     More expensive than prevention

External failure:    Customer returns, warranty, field fixes, recalls
                     Most expensive — 5–10× internal failure cost

Optimal quality cost:
  ┌───────────────────────────────────────────────────────┐
  │ Cost                                                   │
  │    │   Total COQ                                       │
  │    │     ╲                                            │
  │    │      ╲      Internal + External failure          │
  │    │       ╲____                                       │
  │    │       /    ────────────────────────               │
  │    │      / Prevention + Appraisal                    │
  │    │     /                                             │
  │    └──────────────────────────────── Quality level    │
  │              Optimal                                   │
  └───────────────────────────────────────────────────────┘
  Old (Juran) model shows optimum; Crosby argued zero defects
  always cheaper — debate continues in industry.
```

---

## Decision Cheat Sheet

| Need | Tool |
|------|------|
| Is my process stable (no special causes)? | Control chart (I-MR or Xbar-R) |
| Is my process capable? | Cpk / Ppk calculation |
| Is my measurement system trustworthy? | Gage R&R (MSA) |
| Where are most of my defects coming from? | Pareto chart |
| What causes this defect? | 5 Why + Ishikawa diagram |
| How do process factors interact? | DOE (factorial experiment) |
| What are the risks in my process? | PFMEA |
| Correct a customer complaint formally | 8D corrective action |
| Certify QMS for automotive supply chain | IATF 16949 + PPAP |
| Certify QMS generically | ISO 9001:2015 |

---

## Common Confusion Points

**Cpk vs Ppk**: Both measure process capability. Cpk uses within-subgroup standard deviation (short-term, common cause only). Ppk uses overall standard deviation (all variation including between-subgroup shifts). Ppk ≤ Cpk always. Use Cpk for ongoing control (stable process). Use Ppk for preliminary capability studies (new process, short-term data).

**SPC vs inspection**: SPC is proactive — monitor the process to prevent defects. Inspection is reactive — screen output after the fact. Deming: "You cannot inspect quality into a product." SPC improves the process; inspection merely sorts good from bad.

**Six Sigma defect rate math**: Six Sigma (Cpk = 2.0) is 3.4 DPMO, not the 0.001 PPM you'd calculate from a 6σ normal distribution. The discrepancy is Motorola's "1.5σ shift" — empirical observation that long-term processes drift by ±1.5σ from short-term capability. This is controversial; some practitioners reject it.

**ISO 9001 does not guarantee good products**: ISO 9001 certifies you have a documented quality management system and follow it. A company can be ISO 9001 certified and consistently produce mediocre products, as long as they document what they do and do what they document. The system requires continual improvement clauses, but the bar is set internally.

**MSA before SPC**: A control chart is meaningless if the measurement system variation is larger than the process variation. Always run Gage R&R before interpreting SPC data. %GRR > 30% means your chart is plotting mostly noise.
