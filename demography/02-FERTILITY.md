# Fertility

## Fertility Measurement Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FERTILITY MEASUREMENT HIERARCHY                           │
│                                                                               │
│  CRUDE MEASURE          PERIOD MEASURES         COHORT MEASURES             │
│  ──────────────         ───────────────         ───────────────             │
│  CBR (crude birth rate) ASFR by age             Completed cohort fertility  │
│  General Fertility Rate GFR                     Cohort NRR                  │
│  (children per 100      TFR (Total Fertility    (follows one birth cohort   │
│   women 15-49)          Rate)                    to end of reproduction)    │
│                         NRR (Net Reproduction   Parity progression ratios   │
│                         Rate)                   (prob. of having n+1 given n)│
│                         GRR (Gross Reprod. Rate)                            │
│                                                                               │
│  BEHAVIORAL FRAMEWORK: BONGAARTS PROXIMATE DETERMINANTS MODEL               │
│  Decompose fertility into biological/behavioral intermediate variables       │
│                                                                               │
│  TRANSITION THEORIES: Why does fertility fall?                              │
│  Demographic transition theory, wealth flows theory, second DT              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Period Fertility Measures

```
AGE-SPECIFIC FERTILITY RATE (ASFR):
  ASFR_x = (Births to women aged x) / (Women aged x) × 1000
  Units: births per 1,000 women aged x per year

TOTAL FERTILITY RATE (TFR):
  TFR = Σ ASFR_x × n / 1000   (summed over all reproductive ages, n = interval width)
  For 5-year age groups (15-19, 20-24, ..., 45-49):
  TFR = 5 × Σ ASFR_i / 1000   (i = 7 age groups × 5 years)

  INTERPRETATION:
  Average number of children a woman would have if she experienced
  the current age-specific fertility rates throughout her reproductive life.
  This is a SYNTHETIC COHORT measure — no real woman experiences this.

  REPLACEMENT-LEVEL TFR:
  The TFR at which each generation exactly replaces itself.
  In low-mortality populations: ≈2.1 (slightly above 2 due to sex ratio
  at birth ~1.05 males/female and mortality before reproductive age)
  In high-mortality settings: >2.5-3.0 (more women die before completing reproduction)

### TFR Global Reference Values (2023)

| Country / Region | TFR | Note |
|---|---|---|
| Niger | 6.9 | Highest globally |
| Somalia | 6.0 | |
| Mali | 5.9 | |
| Sub-Saharan Africa | 4.5 | Range 3.5–7.0 |
| India | 2.0 | Below replacement; crossed milestone ~2021 |
| United States | 1.62 | |
| Germany | 1.46 | |
| Italy | 1.24 | |
| Japan | 1.20 | |
| South Korea | 0.72 | Lowest ever recorded for a country (2023) |

GROSS REPRODUCTION RATE (GRR):
  GRR = TFR × (proportion of births that are female)
  ≈ TFR × 0.4878  (using sex ratio at birth of 1.05)
  GRR = average daughters per woman (ignoring mortality)

NET REPRODUCTION RATE (NRR):
  NRR = Σ ASFR_x × l(x) × (proportion female)
  = average daughters per woman, accounting for mortality of women
    before they reach each age x

  NRR = 1: replacement (stationary population in long run)
  NRR > 1: growing
  NRR < 1: declining (below replacement)

  NRR = GRR × average survival to reproductive age
  In low-mortality countries: NRR ≈ GRR × 0.98 ≈ GRR (mortality adjustment small)
  In high-mortality countries: NRR << GRR (many women die before reproducing)
```

## Quantum vs. Tempo Effects

One of the most important methodological distinctions in fertility analysis:

```
QUANTUM: How many children do women ultimately have?
         = completed cohort fertility
         The fundamental biological/behavioral quantity.

TEMPO:   WHEN do women have their children?
         = timing/spacing of births
         Can distort period measures without changing quantum.

TEMPO DISTORTION OF PERIOD TFR:
  If women delay births (increase mean age at childbearing):
  → In any given year, fewer births than expected
  → Period TFR understates true cohort quantum
  This is called "tempo distortion" or "tempo effect."

  Bongaarts-Feeney Tempo-Adjusted TFR:
  TFR* = TFR / (1 − r̄)
  where r̄ = annual change in mean age at childbearing

  Example: TFR = 1.5, mean age increasing by 0.1 year/year
  r̄ = 0.1
  TFR* = 1.5 / (1 − 0.1) = 1.5 / 0.9 = 1.67

  IMPLICATION: European period TFRs of ~1.5 may reflect cohort fertility
  of ~1.7-1.8 once tempo adjustment is made.
  Some forecast: fertility will "bounce back" as timing shifts end.
  Others: quantum genuinely below replacement in many countries.

EMPIRICAL TEST:
  Compare period TFR to completed cohort fertility for cohorts
  who have finished reproduction. If cohort > period, tempo distortion confirmed.
  For Germany/Italy: cohort completed fertility (1965-70 birth cohorts) ≈ 1.6-1.7
  vs. period TFR ~1.4-1.5 in 1990s-2000s → large tempo distortion confirmed.
```

## Bongaarts Proximate Determinants Framework

```
BONGAARTS MODEL (1978):
  Decomposes total fertility into biological maximum × inhibiting factors.

  TFR = TN × Cm × Cc × Ca × Ci

  where TN = total natural fertility (no deliberate fertility control)
        ≈ 15-17 births per woman in absence of contraception, marriage delay, etc.

  FOUR PROXIMATE DETERMINANTS:

  Cm = index of marriage (or proportion partnered/exposed):
       = fraction in marital/sexual union in reproductive years
       Range: 0 (nobody married) to 1 (all married)
       Current global variation: 0.5 (some low-marriage East Asian countries) to 0.9+

  Cc = index of contraception:
       = 1 − 1.08 × u × e
       where u = prevalence of contraceptive use, e = method effectiveness
       Range: 0 (perfect contraception) to 1 (no use)

  Ca = index of induced abortion:
       = TF / (TF + 0.4 × (1 + u) × TA)
       where TF = total natural fertility, TA = total abortion rate
       Typically close to 1 in low-abortion settings; can be 0.7-0.9 in China

  Ci = index of postpartum infecundability:
       = 20 / (18.5 + i)
       where i = mean duration of postpartum infecundability in months
       (primarily driven by breastfeeding duration)
       Range: ~0.5 to ~0.9

  TYPICAL DECOMPOSITION (developing country):
  TFR decline from 6 to 3 attributed to:
    Contraception: ~50-60% of decline
    Later marriage: ~20-30%
    Abortion: ~10-15%
    Reduced breastfeeding: slightly increases fertility (counteracts others)
```

## Parity Progression Ratios

```
PARITY PROGRESSION RATIO (PPR):
  PPRₙ = Probability that a woman with n children has at least one more child
  P₀ = Probability of having at least 1 child (given in population)
  P₁ = Probability of having at least 2 (given already have 1)
  P₂ = Probability of having at least 3 (given already have 2)

  TFR = Σ P₀ × P₁ × ... × Pₙ

  USEFULNESS:
  Reveals WHICH parity drives fertility change.
  Fertility decline in Europe: primarily from P₂ and P₃ declining
  (stopping after 2 children, fewer 3+ child families)
  Japan low fertility: driven by delay of P₀ (fewer women having any child)
  South Korea: extreme delay of P₀ + high P₀ to P₁ conditional probability
    → many childless + the few who have children have 1-2
```

## Theories of Fertility Transition

```
CLASSICAL DEMOGRAPHIC TRANSITION THEORY:
  Modernization → development → fertility decline.
  Causal mechanism:
  Economic development → lower child mortality (less "insurance" fertility needed)
  Urbanization → children shift from economic asset to economic cost
  Education (especially women's) → opportunity cost of childbearing rises
  Female labor force participation → opportunity cost rises
  Secularization → weakened religious pronatalism
  Evidence: broadly confirmed; universal pattern across developed countries

WEALTH FLOWS THEORY (Caldwell 1976):
  Fertility is rational response to intergenerational wealth flows direction.
  High fertility rational when children contribute labor early + support elderly parents
  (net wealth flows from children to parents = upward flows)
  Low fertility rational when children consume resources for long period
  (net flows from parents to children = downward flows)
  Modern education and nuclear families shift flows from upward to downward.
  Transition occurs when downward flows become dominant in family calculations.

IDEATIONAL THEORY:
  Ideas, not just economics, drive fertility.
  Diffusion of low-fertility norms from developed regions.
  Media exposure → adoption of small-family norms.
  Evidence: some African countries with high infant mortality already adopting
  low-fertility ideals — driven by globalization/media, not development.

SECOND DEMOGRAPHIC TRANSITION (SDT, van de Kaa & Lesthaeghe 1986):
  Post-WWII Europe: second fertility decline below replacement.
  Characterized by:
  - Rise of cohabitation (vs. marriage)
  - Delayed marriage and first birth
  - Increased non-marital births
  - Fertility below replacement
  - Diverse family forms (single parents, same-sex couples, childlessness)
  Driver: individualization, autonomy, self-realization values
  (Maslow's hierarchy: from security needs → self-actualization)
  SDT is about values, not just economics.
  Spreading globally: South Korea, Japan, China show SDT patterns.
```

## Fertility Globally — Current Patterns

### Regional Fertility (TFR, 2023 Estimates)

| Region | TFR | Trend / Key variation |
|---|---|---|
| Sub-Saharan Africa | 4.5 | Declining but slowly; high-fertility outlier |
| Middle East & N. Africa | 2.7 | Rapid decline in progress |
| South Asia | 2.1 | India just below replacement |
| Southeast Asia | 2.1 | Wide variation: Philippines 2.8, Thailand 1.3 |
| Latin America | 1.8 | Below replacement in most countries |
| Europe | 1.5 | Wide variation: France 1.68, Spain 1.16 |
| North America | 1.7 | US 1.62, Canada 1.4 |
| East Asia | 1.2 | Extreme low: South Korea 0.72, Japan 1.2, China ~1.0 |

Convergence toward low fertility is real but incomplete. East Asia shows unprecedented below-replacement fertility with no recovery in sight. The **low-fertility trap** hypothesis: once TFR falls below ~1.5, population momentum and cultural entrenchment make return to replacement difficult.

**Lowest-low fertility (<1.3)** — South Korea, Singapore, Taiwan, China, Spain, Italy, Poland: driven by extreme housing and education costs, labor market insecurity, and gender inequality at home (women face the double burden of full employment plus primary household labor). Pronatalist policies (maternity leave, childcare subsidies) achieve modest TFR recovery in France and Nordic countries (~1.6-1.9), but South Korea has the world's most generous childcare subsidy with TFR still declining. Economic factors and cultural values interact; no simple policy lever exists.

## Decision Cheat Sheet

| Fertility question | Measure/method |
|---|---|
| Summary fertility level for a country | TFR (period) |
| Long-run replacement-level assessment | NRR (Net Reproduction Rate); NRR = 1 = replacement |
| Is low period TFR real or timing artifact? | Compare to tempo-adjusted TFR*; compare to cohort completed fertility |
| What factors inhibit fertility below maximum? | Bongaarts decomposition: marriage × contraception × abortion × breastfeeding |
| Which birth orders are declining? | Parity progression ratios (PPRₙ) |
| Why did fertility decline historically? | Demographic transition theory + wealth flows theory |
| Why does East Asia have ultra-low fertility? | Second demographic transition + housing/education costs + gender inequality |

## Common Confusion Points

**TFR is a synthetic cohort measure**: No real woman experiences the TFR. It's a hypothetical constructed from one year's age-specific rates. Like a snapshot price index — useful summary but not a direct description of any individual's experience.

**Below-replacement TFR ≠ immediate population decline**: Due to momentum and age structure, a country can have TFR < 2.1 for decades before population starts falling. Germany: below replacement since 1970, but population didn't peak until ~2003 (with immigration) or start falling until recently. Japan: below replacement since 1974, population peaked 2008.

**NRR vs. TFR for replacement**: TFR ≈ 2.1 = replacement in low-mortality settings. NRR = 1.0 = replacement always (by definition). NRR is the more theoretically correct measure but TFR is more commonly cited because it's not mortality-dependent and easier to interpret.

**Contraceptive prevalence ≠ fertility control**: Unmet need for contraception (women who want to limit/space births but aren't using contraception) is often 10-30% in Sub-Saharan Africa. But total demand for large families also remains high. In many high-fertility settings, couples want 4-6 children — the constraint is not access to contraception but desired family size.
