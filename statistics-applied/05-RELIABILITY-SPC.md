# 05 — Reliability & Statistical Process Control

## Weibull, MTTF/MTTR/MTBF, Failure Analysis, Control Charts, Cp/Cpk

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Reliability fundamentals: reliability function R(t) = P(T > t), failure rate (hazard function) h(t) = f(t)/R(t), cumulative hazard H(t); bathtub curve (early failure/random/wear-out phases)
- Exponential distribution: constant hazard rate (memoryless property), MTTF = 1/λ; when appropriate (random failures, no wear-out); limitations
- Weibull distribution: shape parameter β (β<1: infant mortality, β=1: exponential/random, β>1: wear-out), scale parameter η (characteristic life = 63.2% failure point); Weibull plot (log-log linearization); MLE estimation; critical for hardware reliability
- System reliability: series (R_sys = ΠRᵢ — weakest link), parallel (R_sys = 1 - Π(1-Rᵢ) — redundancy), k-of-n systems; fault tree analysis; FMEA (Failure Mode and Effects Analysis) — severity × occurrence × detection = RPN
- MTTF/MTTR/MTBF/MTBF: mean time to failure (non-repairable), mean time to repair, mean time between failures (repairable systems), availability = MTBF/(MTBF+MTTR); SLA nines (99.9% = 8.7 hr/yr downtime)
- Software reliability: MTTF in software context, burn-in testing analogy, reliability growth models (Jelinski-Moranda, NHPP models), chaos engineering as reliability improvement
- Statistical Process Control (SPC): Walter Shewhart's contribution; common cause variation vs special cause variation; 3-sigma control limits rationale
- Control charts: X-bar and R charts (sample means and ranges), Individuals and Moving Range (I-MR for single observations), p-chart (proportion defective), c-chart (count of defects); out-of-control signals (Nelson rules/Western Electric rules)
- Process capability: Cp = (USL-LSL)/6σ (capability vs spec width), Cpk = min((USL-μ)/3σ, (μ-LSL)/3σ) (accounts for centering); Six Sigma ↔ 3.4 DPMO ↔ Cpk=1.5 with 1.5σ shift
- Acceptance sampling: MIL-STD-105/ANSI Z1.4, AQL (Acceptable Quality Level), OC curve (operating characteristic); when 100% inspection vs sampling
