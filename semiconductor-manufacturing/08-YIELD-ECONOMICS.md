# Yield and Economics — A Layered Guide

## The Big Picture

Semiconductor economics is dominated by yield — the fraction of good dies per wafer.
A leading-edge fab costing $20B produces wafers at $20,000 each. Die yield converts
that wafer cost into cost per die. Learning curves drive yield up over time, making
newer nodes economical as the fab "learns."

```
SEMICONDUCTOR COST EQUATION
════════════════════════════════════════════════════════════════════

Wafer cost
──────────── × (1/Yield) = Cost per die
Dies per wafer

DRIVERS:
                   ┌─── Fab depreciation (~$20B / 10 yr → $2B/yr)
Wafer Cost ────────┤─── Materials (chemicals, gases, slurries)
                   └─── Labor, energy, maintenance

                   ┌─── Die area (larger die → fewer per wafer)
Dies per Wafer ────┤─── Wafer diameter (300 mm → ~700 gross 1 cm² dies)
                   └─── Edge exclusion (15-20 mm perimeter unusable)

                   ┌─── Defect density (D₀ defects/cm²)
Yield ─────────────┤─── Die area (larger die → more chances for defect)
                   └─── Process maturity (improves over time)

TYPICAL NUMBERS (3 nm node, 1 cm² die, 2024):
  Wafer cost:        ~$20,000
  Dies per wafer:    ~450 (gross ~630, edge loss ~180)
  Yield:             ~80% at mature N3, lower at introduction
  Cost per die:      $20,000 / (450 × 0.80) = ~$56 per die
  (Plus assembly/test/packaging: +$5-30 more for total finished cost)
```

---

<!-- @editor[bridge/P2]: Missing yield curve → software reliability engineering bridge — Murphy's model produces a yield-vs-die-area curve with the same shape as a software reliability bathtub curve: high early failure rate (new process, D₀ high), rapid improvement on the learning curve, eventual steady-state; die yield binning (speed/power grades sorted by measured performance) is directly analogous to A/B testing by latent quality metric, and the yield ramp learning curve (Brice's law: yield doubles per doubling of cumulative volume) mirrors software cost curves; this is territory the learner owns from VSTS/Azure infrastructure SLA modeling -->

## Yield Models

```
DEFECT DENSITY BASICS

DEFECT TYPES:
  Critical defects: cause immediate failure (short, open, wrong Vt)
  Non-critical: don't affect functionality at first (may affect reliability)
  Random defects: particles, contamination — distributed across wafer
  Systematic defects: design-rule violations, process interactions — location-specific

DEFECT DENSITY D₀:
  D₀ = total critical defects per unit area (defects/cm²)
  Modern leading-edge: D₀ ≈ 0.05-0.5 defects/cm² (depending on process maturity)
  New process introduction: D₀ may start at 2-5 defects/cm²

CRITICAL AREA ANALYSIS (Ac):
  Not all area is equally vulnerable — only regions where a defect causes failure
  Ac(r) = area where defect of radius r causes failure
  Integrate over defect size distribution → effective critical area per layer

YIELD MODELS:

1. POISSON MODEL (simple, theoretical):
   Y = e^(-D₀·A)
   Assumes: Poisson-distributed defects; uniform sensitivity
   Problem: overestimates yield impact (actual defects cluster → some dies have many, most have none)

2. MURPHY'S MODEL (1964, industry standard):
   Y = [(1 - e^(-D₀·A)) / (D₀·A)]²
   Accounts for: defect clustering (Gaussian distribution of defect density)
   Better fit to real data; widely used for yield projection

3. SEEDS MODEL:
   Y = 1 / (1 + D₀·A)
   Simple form; good for early yield estimate

4. NEGATIVE BINOMIAL MODEL (more accurate):
   Y = (1 + D₀·A/α)^(-α)
   α = clustering parameter (α→∞ → Poisson; α small → highly clustered)
   Widely used by yield engineers, fits real data well

EXAMPLE CALCULATION (Murphy's):
  D₀ = 0.1 defects/cm², A = 2 cm² (large GPU die)
  D₀·A = 0.2
  Y = [(1 - e^(-0.2)) / 0.2]² = [(1 - 0.819) / 0.2]² = [0.905]² ≈ 82%

  Same D₀, A = 4 cm²:
  D₀·A = 0.4
  Y = [(1 - e^(-0.4)) / 0.4]² = [(0.33) / 0.4]² ≈ 68%
  → Yield drops fast with die area
```

---

## Dies Per Wafer

```
DIES PER WAFER

FORMULA:
  DPW = (π·(d/2)² - π·d·e) / A_die

  Simplified with edge exclusion:
  DPW = π·(d - 2e)² / (4·A_die) - π·(d - 2e) / √(2·A_die)

  d = wafer diameter (300 mm)
  e = edge exclusion (typically 3 mm)
  A_die = die area (cm²)

APPROXIMATE (for rough estimates):
  DPW ≈ (Wafer area - Edge loss) / Die area
  Usable 300 mm wafer area ≈ 706 cm² - 15 cm² edge ≈ 690 cm²

DIE AREA vs DPW TABLE (300 mm wafer, 3 mm edge):
  A_die    Gross DPW    Edge-corrected DPW
  ─────────────────────────────────────
  0.1 cm²  ~7,000       ~6,800
  0.5 cm²  ~1,400       ~1,300
  1.0 cm²  ~700         ~630
  2.0 cm²  ~350         ~300
  4.0 cm²  ~175         ~145
  8.0 cm²  ~87          ~70
  15 cm²   ~47          ~38
  35 cm²   ~20          ~16   (H100 die)
  50 cm²   ~14          ~11   (theoretical maximum reticle = 26×33 mm ≈ 8.6 cm²)

RETICLE LIMIT:
  Maximum single die: reticle field = 26 mm × 33 mm = 8.58 cm²
  Larger dies: use stitching (seams visible) — not standard for logic
  Intel Ponte Vecchio: >50 cm² equivalent via chiplets (not monolithic)
  Cerebras WSE-3: ~8,400 cm² — the entire 300 mm wafer as one chip

AREA EFFICIENCY:
  Not all die area is active — bond pads, power rings, guard rings, PHY
  Core utilization: 60-80% of die area actually doing computation
```

---

## Cost Per Die

```
COST PER DIE — DETAILED MODEL

TOTAL COST PER GOOD DIE:
  Cpd = (Wafer Cost) / (DPW × Die Yield × Test Yield × Package Yield)

WAFER COST COMPONENTS:
  Capital depreciation: $20B fab / 8 yr / 50,000 WPM ≈ $4,000/wafer
  Materials: chemicals, gases, photoresist, CMP slurries ≈ $1,500-3,000/wafer
  Labor, energy, facility: ≈ $1,000-2,000/wafer
  Mask set amortized: 80-100 masks × $10K-20K each = $1M-2M per design
    Spread over 50,000 wafers → $20-40 per wafer per product

MASK COST (non-recurring engineering, NRE):
  Leading-edge mask set (3 nm): $20-30M total NRE
  This is why low-volume products (ASICs) are expensive
  A 5,000-unit run at 3 nm: $20M NRE ÷ 5,000 = $4,000 per chip NRE alone

TEST COST:
  Wafer sort (probe): ~$500-2,000/wafer at leading-edge
  Package final test: $0.50-5 per device depending on speed grade testing
  Burn-in (reliability screen): additional $1-3 per device

BINNING:
  Same wafer → grade devices by frequency (fmax) and power
  Premium bin (fastest): highest price, limited supply
  Standard bin: volume product
  Downbin: slower/higher voltage → sold as cheaper part
  Example: TSMC N3 CPU wafer → i9 (>4 GHz), i7 (>3.5 GHz), i5 (>3 GHz) from same silicon
  Binning monetizes the yield distribution: not all dies are equal

ECONOMICS EXAMPLE (GPU, $25K compute card):
  NVIDIA H100:
    Die: 4.1 nm TSMC, ~80 cm² equivalent (SXM5)
    Actually GH100 ≈ 35 cm² SoC die
    Wafer cost: ~$20,000
    DPW: ~35-40
    Die yield: ~70% (early, large die)
    Good dies per wafer: ~25-28
    Die cost: ~$700
    CoWoS packaging + HBM: ~$2,000-3,000
    Total COGS: ~$3,500-4,000
    Sale price: $25,000 → ~6-7× margin (covers R&D amortization, support, etc.)
```

---

## Learning Curves

```
LEARNING CURVES

CONCEPT:
  Yield improves as cumulative production increases
  New process: high defect density → yield starts low (60-70%)
  After 12-18 months: yield typically reaches maturity (90-95%)

DEFECT REDUCTION SOURCES:
  Equipment cleaning: identify and eliminate contamination sources
  Recipe optimization: fine-tune process parameters (pressure, T, gas flows)
  Design rules refinement: fix layout patterns that cause systematic failures
  Metrology improvements: better measurement → faster feedback
  Equipment engineering: identify tool-specific yield losers

WRIGHT'S LAW (production learning):
  Cost per unit decreases by a fixed percentage for every doubling of cumulative output
  Semiconductor industry: ~20-30% cost reduction per doubling
  Applies across generations: each new node starts expensive, gets cheaper over time

RAMP TIMELINE:
  Quarter 0 (risk production): first product wafers, yield ~50-70%
  Quarter 2-4: yield ramp, process stabilization
  Quarter 6-8: yield maturity, volume production
  Quarter 12+: sustained production, yield plateau, eventual node end-of-life

TSMC N5 EXAMPLE:
  Introduction: 2020, Apple A14
  Ramp: ~6 months to high volume
  Mature yield: reached ~95% by 2021
  Multiple customers: NVIDIA, Qualcomm, AMD joined after Apple's node-exclusive ended

N+1 NODE ECONOMICS:
  Each new node: wafer cost +30-50% (EUV adoption, more process steps)
  Die area shrinks ~30-40% → offset higher wafer cost
  Net: cost per transistor improves ~20-30% per node
  But: improvement slowing (was 50% per node pre-EUV era)
  TSMC N3 → N2: less area reduction than past transitions → economics tightening
```

---

## Test and Reliability

```
TEST STRATEGY

WAFER SORT (probe test):
  Probe card contacts each die on wafer
  Functional test: does device work? (logic, memory, I/O)
  Parametric: Vt, leakage, frequency
  Marks good/bad dies (ink or map file)
  Capital: probe station ~$500K; test equipment (ATE) ~$2-10M

ATE (Automated Test Equipment):
  Teradyne, Advantest dominate
  SoC tester: $5-10M for leading-edge (high-frequency, high pin count)
  Load board: custom PCB for each device type → $50-200K per design

FINAL TEST (packaged device):
  Speed/frequency binning: run at different frequencies → grade
  Power measurement: verify power management
  Memory test: BIST (built-in self-test) helps reduce external test time
  Hot/cold test: some applications test at -40°C and +125°C

BUILT-IN SELF-TEST (BIST):
  Logic BIST: on-chip test pattern generation + response comparison
  Memory BIST: on-chip memory test engine (walks patterns through all cells)
  Reduces: test time (parallel self-test), pin count needed, ATE cost

BURN-IN:
  Apply elevated voltage + temperature for 8-48 hours
  Accelerated aging: screens out "infant mortality" (early failures)
  Arrhenius acceleration: temp increase 10°C → 2× failure rate for some defects
  Used for: automotive (AEC-Q100), mil-spec, server chips

RELIABILITY SPECIFICATIONS:
  Consumer: 1000 h at 85°C / 85% RH (JEDEC JESD22)
  Automotive: AEC-Q100 Grade 0 (−40 to +150°C junction)
  MTTF (mean time to failure): 10⁶-10⁸ hours design goal for data center chips
```

---

## Decision Cheat Sheet

| Decision | Yield/Economics Principle |
|----------|--------------------------|
| Why chiplets instead of one big die? | Large die yield collapses: 4 cm² × 2 = 8 cm² → yield² instead of yield¹ |
| Choosing node for new design | Newer node: better performance but higher wafer cost, lower initial yield |
| Reducing NRE for ASIC | Use mature node (28 nm): mask cost $1-3M vs $25M at 3 nm |
| Maximizing volume profitability | Ramp yield fast on mature node; high volume amortizes fixed costs |
| Premium product pricing | Bin fastest dies; charge 5-10× for top bin vs slow bin |
| Die size optimization | Minimize area: 10% smaller die → 10% more dies/wafer AND better yield |

---

## Common Confusion Points

**Yield ≠ defect rate in the manufacturing quality sense**: Semiconductor yield is primarily
about random particle defects and process variations causing die failures. A 90% yield die
is perfectly normal — the remaining 10% are just bad luck (particle on a critical wire, for example),
not systematic process failures.

**Wafer cost is not a secret**: Semiconductor analysts publish detailed tear-downs and cost
models. TSMC N3 wafer at ~$20K is well-known. The real proprietary information is the yield
and the process recipe, not the wafer price.

**Large die yield disaster is non-linear**: Murphy's yield model means going from 4 cm² to
8 cm² die doesn't halve yield — it reduces yield dramatically more. At D₀=0.1, 4 cm² → 68%
yield; 8 cm² → 47% yield. This is why NVIDIA splits compute dies into multiple chips for next
generation.

**"Leading edge" doesn't mean "profitable" immediately**: TSMC N5 and N3 both had periods
of high wafer cost + low yield + limited customers. The economics work at scale but not at
introduction. Foundry business requires massive advance orders (Apple's exclusivity contracts)
to justify the investment.
