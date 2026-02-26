# Human Development: Sen Capabilities Approach, HDI, IHDI, MPI

## The Big Picture

The capabilities approach is a fundamental critique of income-based development metrics. Amartya Sen's insight: income is a means, not an end. Development should be measured by what people can *be* and *do* — their real freedoms — not by the income that partially enables them.

```
+--------------------------------------------------------------------------+
|                    HUMAN DEVELOPMENT FRAMEWORK                            |
+--------------------------------------------------------------------------+
|                                                                          |
|  QUESTION: What is development FOR?                                      |
|                                                                          |
|  INCOME-BASED ANSWER         CAPABILITIES ANSWER (Sen)                  |
|  ──────────────────          ──────────────────────────                  |
|  GDP per capita              Real freedoms / capabilities                |
|  GNI per capita              What people can be and do                  |
|  Consumption expenditure     Set of achievable functionings              |
|                                                                          |
|  THE PROBLEM: Income-to-wellbeing conversion is unequal                 |
|                                                                          |
|  Same income → different capabilities depending on:                     |
|   - Age (elderly need more for same health)                             |
|   - Disability (wheelchairs, care are expensive)                        |
|   - Gender (women may lack control over household income)               |
|   - Disease environment (malaria area → more needed for same health)    |
|   - Social norms (discrimination → income converts poorly)              |
|                                                                          |
|  MEASUREMENT HIERARCHY:                                                  |
|  GDP/GNI → income only                                                  |
|  HDI     → income + health + education (3-dimension index)              |
|  IHDI    → HDI adjusted for within-country inequality                   |
|  GDI     → HDI disaggregated by gender                                  |
|  MPI     → 10-indicator deprivation index (who lacks what)              |
+--------------------------------------------------------------------------+
```

---

## 1. Sen's Capabilities Approach

Amartya Sen developed the capabilities approach in a series of works: *Equality of What?* (Tanner Lecture 1979), *Commodities and Capabilities* (1985), *Development as Freedom* (1999).

**Core distinction**:

```
FUNCTIONINGS vs. CAPABILITIES:

  Functioning = an actual state or activity
    "Being well-nourished"
    "Being able to read"
    "Participating in community life"
    "Moving about freely"

  Capability = the ability to achieve a functioning IF chosen
    "Having the real option of being well-nourished"
    "Having genuine access to literacy"
    "Not being excluded from community life"

  CAPABILITY SET = the full set of achievable functioning combinations
                   (the opportunity space)

  Development = EXPANDING the capability set
              (increasing real freedom, not just income)
```

**Why capabilities, not just resources**:
```
EXAMPLE — Two people with $50,000/year income:

Person A: healthy, educated, lives in stable democratic society
Person B: chronically ill (expensive treatment), lives in
          discriminatory society, no access to education

Person A's capability set >> Person B's capability set
despite identical income.

SEN'S POINT: measuring income misses the actual freedom
to live well. Policy should target the conversion factors
(health, education, social inclusion) not just income.
```

**The conversion factors**:
Sen identifies three types of conversion factors that mediate income-to-capability conversion:
1. **Personal** (metabolism, disability, age, gender)
2. **Social** (public policies, social norms, power structures)
3. **Environmental** (climate, infrastructure, disease burden)

---

## 2. Nussbaum's Central Capabilities

Martha Nussbaum (*Women and Human Development*, 2000; *Creating Capabilities*, 2011) moved the capabilities approach from informational framework to specific list:

**The 10 Central Human Capabilities**:

| # | Capability | Minimum threshold |
|---|-----------|-------------------|
| 1 | Life | Living to normal length; not dying prematurely |
| 2 | Bodily health | Good health; reproductive health; adequate nourishment; shelter |
| 3 | Bodily integrity | Free movement; freedom from violence; reproductive choice |
| 4 | Senses, imagination, thought | Literacy, numeracy; full use of senses; freedom of expression |
| 5 | Emotions | Capacity to love, grieve, feel gratitude; not stunted by fear/anxiety |
| 6 | Practical reason | Forming conception of the good; engaging in critical reflection |
| 7 | Affiliation (A+B) | A: Living with and toward others, empathy; B: non-discrimination, dignity |
| 8 | Other species | Living with and in relation to animals, plants, the natural world |
| 9 | Play | Laughter, recreation, enjoyment |
| 10 | Control over environment | A: political participation; B: property rights, work on human basis |

**Nussbaum vs. Sen**:
- Sen refuses to give a definitive list (capabilities are context-dependent, should emerge from democratic deliberation)
- Nussbaum argues a list is necessary for justiciable rights and legal obligations
- Sen's position: more flexible for cross-cultural application; Nussbaum's: more tractable for policy and law

---

## 3. Human Development Index (HDI)

The HDI was developed by Mahbub ul Haq and Amartya Sen for UNDP's first Human Development Report (1990). It is a deliberate political tool to shift attention from GDP.

**HDI computation (post-2010 formula)**:

```
STEP 1: Normalize each dimension to [0, 1]

  Health Index     = (LE - 20) / (85 - 20)
                     where LE = life expectancy at birth
                     min = 20 years, max = 85 years

  Education Index  = (MYS_index + EYS_index) / 2
                     MYS = mean years of schooling (min 0, max 15)
                     EYS = expected years of schooling (min 0, max 18)

  Income Index     = (ln(GNIpc) - ln(100)) / (ln(75000) - ln(100))
                     GNI per capita PPP USD
                     Logarithm: diminishing returns to income

STEP 2: Geometric mean of the three normalized indices

  HDI = (Health_Index × Education_Index × Income_Index)^(1/3)

  GEOMETRIC mean (vs. arithmetic): if one dimension is zero,
  HDI = 0. Penalizes extreme inequality across dimensions.
  Arithmetic mean would allow one dimension to compensate for another.
```

**Why geometric mean matters**:
```
  Two countries:
  A: Health=0.9, Education=0.9, Income=0.1 → Arithmetic=0.633, Geometric=0.490
  B: Health=0.6, Education=0.6, Income=0.6 → Arithmetic=0.600, Geometric=0.600

  Geometric HDI ranks B above A — penalizes extreme imbalance.
  Arithmetic HDI would rank A above B — allows income to compensate
  for terrible education.
```

**Notable HDI outliers**:

| Country | GDP/capita rank minus HDI rank | Reason |
|---------|-------------------------------|--------|
| Norway | ≈0 (both ~#1) | Balanced development |
| Kerala (India state) | HDI >> GDP | High health + education despite low income |
| Cuba | HDI >> GDP | State investment in health/education; income controlled |
| UAE/Qatar | GDP >> HDI | High income, lagging education + health for migrants |
| South Africa | GDP > HDI | High inequality; HIV epidemic → life expectancy gap |

---

## 4. Inequality-Adjusted HDI (IHDI)

The HDI uses national averages — it ignores inequality within countries. The IHDI (2010) discounts each dimension by its inequality:

```
IHDI FORMULA:

  For each dimension X:
    I_X = X̄ × (1 - A_X)

  where A_X = Atkinson inequality measure for dimension X

  Atkinson measure: A_X = 1 - (geometric mean of X) / (arithmetic mean of X)
  If perfectly equal: geometric mean = arithmetic mean → A_X = 0, no discount
  If very unequal: geometric mean << arithmetic mean → large discount

  IHDI = (I_health × I_education × I_income)^(1/3)

  Loss from inequality = (HDI - IHDI) / HDI

  Global average loss ~20%, higher in unequal countries (Southern Africa,
  Latin America, South Asia)
```

**Interpretation**: If a country's IHDI is much lower than its HDI, inequality is large — the average masks a very unequal distribution of health, education, and income.

---

## 5. Gender Development Index (GDI) and GEM

**GDI**: HDI calculated separately for women and men, then ratioed.
```
GDI = HDI_female / HDI_male

GDI = 1.0: perfect gender equality in human development
GDI < 1.0: women below men (typical)
GDI > 1.0: women above men (rare; some Baltic states in education)
```

**Gender Inequality Index (GII)** — measures loss from gender inequality across:
1. Reproductive health (maternal mortality rate, adolescent birth rate)
2. Empowerment (female vs. male parliamentary seats; secondary education attainment)
3. Labor force (female vs. male participation rate)

---

## 6. Multidimensional Poverty Index (MPI)

Developed by Sabina Alkire and James Foster at OPHI (Oxford Poverty & Human Development Initiative) for UNDP Human Development Report 2010.

**The AF (Alkire-Foster) method**:

```
STEP 1: Choose dimensions, indicators, weights

  DIMENSION      INDICATOR                    WEIGHT
  ─────────────────────────────────────────────────────
  Health         Child mortality              1/6
                 Nutrition                   1/6
  Education      Years of schooling          1/6
                 School attendance           1/6
  Living         Cooking fuel                1/18
  Standards      Sanitation                  1/18
                 Drinking water              1/18
                 Electricity                 1/18
                 Housing                     1/18
                 Assets                      1/18
  ─────────────────────────────────────────────────────
  TOTAL                                      1.0

STEP 2: Identify deprived persons and dimensions

  Person is deprived in dimension d if below threshold:
    Child mortality: any child under 5 has died in family
    Nutrition: any adult/child is undernourished
    Years of schooling: no one in household has 6+ years
    etc.

STEP 3: Count deprivations per person

  c_i = weighted sum of deprivations for person i
  Person is MULTIDIMENSIONALLY POOR if c_i ≥ k (cutoff, typically k=1/3)

STEP 4: MPI = H × A

  H = incidence: share of population that is MPI poor
  A = intensity: average share of deprivations among the poor
  MPI = H × A (ranges 0 to 1)
```

**Why MPI > income poverty headcount**:
```
MPI reveals WHERE poverty is concentrated:
  A household might have income > $2.15/day but:
    - Children not in school
    - No safe drinking water
    - No electricity
    - Undernourished children

  Income poverty would miss this household.
  MPI catches it via direct deprivation measurement.

MPI also reveals COMPOSITION:
  Two countries with MPI = 0.2:
  Country A: mostly health deprivation (nutrition, mortality)
  Country B: mostly living standard deprivation (water, sanitation)
  Same MPI, but completely different policy priorities.
```

---

## 7. Comparing the Measures

```
+------------------+----------+----------+----------+----------+
| Measure          | Captures | Ignores  | Best for | Updated  |
+------------------+----------+----------+----------+----------+
| GDP per capita   | Income   | Non-     | Macro    | Annual   |
|                  | (mean)   | market   | trends,  |          |
|                  |          | goods,   | debt     |          |
|                  |          | distrib. | capacity |          |
+------------------+----------+----------+----------+----------+
| HDI              | Health+  | Distrib. | Broad    | Annual   |
|                  | Educ+    | within   | country  |          |
|                  | Income   | dims,    | rankings |          |
|                  |          | sustain. |          |          |
+------------------+----------+----------+----------+----------+
| IHDI             | HDI +    | Sustain. | Equality | Annual   |
|                  | within-  | Voice,   | analysis |          |
|                  | country  | agency   |          |          |
|                  | inequal. |          |          |          |
+------------------+----------+----------+----------+----------+
| MPI              | Direct   | Subjec-  | Targeting| ~2 years |
|                  | depriva- | tive     | policy,  | (survey  |
|                  | tions ×  | wellbeing| finding  | based)   |
|                  | 10 indic.| inequal. | poorest  |          |
|                  | who/what | of the   |          |          |
|                  |          | poor     |          |          |
+------------------+----------+----------+----------+----------+
```

**Correlation**: HDI and log GDP/capita correlate at ~0.95. The outliers (Kerala, Cuba, Gulf states) are what makes HDI useful — they show that the income-to-development conversion varies enormously.

---

## 8. Capabilities in Practice: The Kerala Model

Kerala (Indian state) is the canonical example of high human development at low income:

```
KERALA METRICS (approx. 2020):
  GDP per capita: ~$2,500 (well below Indian average)
  Life expectancy: 75+ years (comparable to US in 1980)
  Female literacy: 96%+ (highest in India)
  Infant mortality: ~6/1000 (lower than some US states)
  Total fertility rate: 1.6 (below replacement, like Europe)

HOW:
  - Communist party governments (1957, 1967, recurring) invested heavily
    in public health and education
  - Land reform: redistribution broke feudal tenancy
  - Women's education: high female literacy → lower fertility → health dividend
  - Strong union movement → labor standards despite low industrial base
  - Large remittances from Gulf migrants → income floor

LESSON: Human development does not require high income first.
        Social investment can deliver capabilities ahead of income growth.
        (But Kerala's manufacturing stagnation is a real cost.)
```

---

## Decision Cheat Sheet

| Need | Use | Reason |
|------|-----|--------|
| Cross-country ranking for broad development | HDI | Health + education + income; widely comparable |
| Inequality within countries | IHDI | HDI discounted for distributional gaps |
| Who is poor and in what way | MPI | Direct deprivation counts across 10 indicators |
| Gender gap in development | GDI | Separate HDI by sex |
| Policy targeting (which deprivation to address) | MPI decomposition | Shows which dimensions drive poverty in a region |
| Macro economic comparison, debt sustainability | GDP/GNI | Income-based, standard economic use |
| Philosophical framework for what development means | Sen capabilities | Real freedom, not just resources |

---

## Common Confusion Points

**HDI is not the capabilities approach**: HDI is a pragmatic measurement tool inspired by the capabilities approach. Sen himself says HDI is useful but too narrow — it doesn't measure political freedom, voice, social belonging, or environmental sustainability.

**MPI is not a poverty line**: MPI doesn't set a dollar threshold. It identifies people deprived in a weighted count of specific dimensions. Someone can have income above the $2.15/day line but still be MPI poor (no clean water, children not in school). The headcount H and intensity A give different information than a poverty line.

**Functionings are not functionings**: In Sen's framework, functionings are what a person actually achieves (being nourished, reading, participating). Capabilities are the genuine opportunities to achieve functionings. Policy should expand capabilities (opportunities), not force functionings (paternalism).

**The capabilities list debate is real**: Sen's refusal to give a fixed list is a principled philosophical position — capabilities should be identified through democratic deliberation, not expert imposition. Nussbaum's list is for adjudicating constitutional rights claims. The two uses don't conflict; they operate in different domains.

**Kerala's "paradox" is partly explained**: Kerala's low income despite high human development has three components: (1) Indian GDP underestimates informal economy; (2) Gulf remittances are large and go directly to households; (3) public provision of health/education substitutes for private expenditure — the "income" needed for wellbeing is lower when public goods are provided.
