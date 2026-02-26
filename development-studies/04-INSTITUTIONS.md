# Institutions and Governance: Acemoglu/Robinson, Property Rights, Rule of Law

## The Big Picture

The institutional turn in development economics (1990s–2000s) produced the field's most influential explanatory framework: institutions — the rules of the game — are the proximate cause of prosperity differences across nations. Geography, culture, and history matter mainly through their effects on institutions.

```
+--------------------------------------------------------------------------+
|                    INSTITUTIONS IN DEVELOPMENT                            |
+--------------------------------------------------------------------------+
|                                                                          |
|  WHAT ARE INSTITUTIONS?                                                  |
|  North (1990): Rules of the game                                        |
|    ├── Formal rules: constitutions, laws, property rights,              |
|    │   contracts, regulations                                            |
|    ├── Informal norms: culture, customs, trust, conventions              |
|    └── Enforcement mechanisms: courts, police, reputation               |
|                                                                          |
|  WHY DO THEY MATTER?                                                     |
|  Institutions → Incentives → Investment → Growth                        |
|                                                                          |
|  KEY DEBATES:                                                            |
|  1. Institutions vs. Geography (Acemoglu vs. Sachs)                     |
|  2. Which institutions? Property rights vs. rule of law vs. democracy   |
|  3. How do good institutions emerge? (Endogeneity problem)              |
|  4. Inclusive vs. extractive: the political economy of institutions      |
|  5. Commons governance: Ostrom vs. Hardin's tragedy                     |
|                                                                          |
|  KEY AUTHORS:                                                            |
|  North (transactions costs, institutional theory)                       |
|  Acemoglu-Johnson-Robinson (colonialism as instrument)                   |
|  Ostrom (governing the commons, polycentric governance)                  |
|  Hall-Soskice (Varieties of Capitalism: LME vs. CME)                    |
+--------------------------------------------------------------------------+
```

---

## 1. North's Institutional Theory

Douglass North (*Institutions, Institutional Change and Economic Performance*, 1990; Nobel 1993):

**Institutions as transactions cost reducers**:
```
EXCHANGE WITHOUT INSTITUTIONS:
  Every transaction requires:
    - Verifying partner's identity
    - Assessing quality/authenticity of goods
    - Enforcing contract terms
    - Protection from theft/violence
  → High transaction costs → trade limited to personal networks
    → Thin markets → inefficient allocation

EXCHANGE WITH INSTITUTIONS:
  Contract law → third-party enforcement
  Property rights → investment protection
  Money → reduces barter search costs
  Courts → reduces bilateral enforcement costs
  Reputation systems → reduce information asymmetry
  → Lower transaction costs → impersonal exchange → markets → growth
```

**Coase theorem connection**: Coase showed that in a world of zero transaction costs, initial property rights allocation doesn't matter — parties will bargain to the efficient outcome. North's insight: transaction costs are never zero; institutions determine their magnitude; poor institutions → high transaction costs → inefficient outcomes persist.

**Formal vs. informal institutions**:
```
FORMAL:
  Constitution, laws, regulations, property rights,
  electoral rules, judicial independence
  Change: through legislation or force
  Speed: can change quickly (but often doesn't stick)

INFORMAL:
  Culture, conventions, norms, ideologies, beliefs
  "How things are done here" (grease payments vs. kickbacks)
  Change: generational, very slow
  Speed: decades to centuries

KEY TENSION:
  You can write a new constitution in a day.
  You cannot change informal norms in a generation.
  Formal institutional reform often fails because
  informal norms undermine it (Russia 1990s privatization:
  formal ownership rights without protection norms → oligarchy)
```

---

## 2. Property Rights and Growth

Hernando de Soto (*The Mystery of Capital*, 2000): the poor in developing countries have assets but lack formal property rights to leverage them:

```
DE SOTO'S ARGUMENT:

  Peruvian slum dweller owns house worth $30,000
  But: no formal title deed
     → Cannot use as collateral for business loan
     → Cannot sell easily (buyer has no legal protection)
     → Cannot bequeath with legal certainty
     → Cannot attract investment in neighborhood
        (no clear ownership → no one invests)

  Same asset with title:
     → Collateral → credit → capital → business
     → "Dead capital" becomes live capital

  Global estimate (2000): ~$9.3 trillion in "dead capital"
  in developing world = assets without formal property rights
```

**Property rights and investment**:
```
PROPERTY RIGHT SECURITY → INVESTMENT:

  If you can be expropriated:
    → Short-term extraction (take what you can now)
    → No investment in fixed assets (can't recover)
    → No technology adoption (not worth cost)

  Secure property rights:
    → Long-term investment
    → Fixed capital formation
    → Technology adoption
    → Contracting with strangers (impersonal markets)

Besley and Burgess (2000): India land reform tenure security
→ agricultural investment; multiple studies confirm relationship
```

**The complications**:
- Property rights can entrench inequality (colonial land grants, enclosures)
- Formal titling sometimes displaces indigenous commons management
- Property rights without enforcement are worthless (Latin America: many rights on paper, weak courts)
- Intellectual property: strong IP rights may reduce innovation diffusion in poor countries

---

## 3. The AJR Framework: Colonialism as Instrument

Acemoglu, Johnson, Robinson (*The Colonial Origins of Comparative Development*, AER 2001):

**The identification challenge**: Every institutional measure correlates with income. How do you establish causation? Countries with good institutions might just be richer, and richer countries can afford better institutions.

**The instrument**:
```
AJR CAUSAL CHAIN:

Disease environment → Colonization strategy → Institutions today → Income today
(in 1500s: yellow     (settler vs. extractive)  (property rights,
fever, malaria)                                   rule of law)

SETTLER COLONIES (low mortality: US, Canada, Australia, NZ):
  Europeans settled in large numbers
  Built institutions for settlers' benefit:
    Property rights, rule of law, representative government
  These institutions persisted → good institutions today

EXTRACTIVE COLONIES (high mortality: Congo, Ivory Coast):
  Europeans couldn't settle — died of disease
  Set up extractive institutions to drain resources:
    Forced labor, plantation systems, no property rights for locals
    Minimal rule of law, autocratic control
  These institutions persisted → bad institutions today

WHY SETTLER MORTALITY IS A VALID INSTRUMENT:
  Settler mortality in 1500s affects income in 2000 ONLY through
  colonization type → institutions. It doesn't directly affect
  income 500 years later (malaria is now mostly treatable).
  → Valid exclusion restriction (more or less)
```

**Results (AJR 2001)**:
```
First stage: settler mortality → institutional quality (strong)
Second stage: institutional quality → log GDP per capita (large effect)
IV estimate: moving from bottom to top 25th percentile of institutions
             → 6-7× higher income
             R² ≈ 0.52 (institutions explain ~52% of income variation)
```

**Robinson and Acemoglu continued** in *Why Nations Fail* (2012):

```
INCLUSIVE vs. EXTRACTIVE INSTITUTIONS:

  INCLUSIVE POLITICAL             EXTRACTIVE POLITICAL
  INSTITUTIONS                    INSTITUTIONS
  ──────────────────              ──────────────────────
  Pluralistic power               Concentrated power
  Rule of law                     Above-the-law elites
  Free press, free elections      Controlled information

        ↓                                ↓

  INCLUSIVE ECONOMIC             EXTRACTIVE ECONOMIC
  INSTITUTIONS                    INSTITUTIONS
  ──────────────────              ──────────────────────
  Property rights                 Property for elite only
  Competitive markets             Monopolies, entry barriers
  Freedom to contract             Forced labor, tribute
  Public education                Education for few
  Financial access                Credit for connected

        ↓                                ↓

  Creative destruction            Incumbent protection
  Innovation rewarded             Innovation suppressed
  Long-run growth                 Stagnation / extraction

VIRTUOUS CYCLE:
  Inclusive institutions → growth → middle class →
  demands accountability → more inclusive institutions

VICIOUS CYCLE:
  Extractive institutions → elite captures gains →
  elite strengthens extractive institutions to protect rents
```

**The critical juncture concept**: Inclusive institutions emerge at historical junctures when power is contested and challengers can force inclusive arrangements (England 1688 Glorious Revolution; US independence). Extractive institutions persist when elites face no credible challenge.

---

## 4. State Capacity vs. Rule of Law

A crucial distinction often collapsed:

```
TWO DIMENSIONS OF INSTITUTIONAL QUALITY:

         High Rule of Law
               │
  Denmark  ●   │   ● Singapore
  Sweden   ●   │   ● China (limited)
               │
Low ───────────┼────────────── High
State          │               State
Capacity       │               Capacity
               │
  Somalia  ●   │   ● Russia
               │   ● Venezuela
         Low Rule of Law

QUADRANT ANALYSIS:
  High capacity + high rule of law = Denmark model
  High capacity + low rule of law = developmental state (Singapore, China)
  Low capacity + high rule of law = weak state (some Latin America)
  Low capacity + low rule of law = failed state (Somalia)

IMPLICATION:
  Rule of law without state capacity = law on paper, unenforceable
  State capacity without rule of law = capable but predatory
  You need both — but building them simultaneously is hard
```

**Francis Fukuyama's institutional triad** (*Political Order and Political Decay*, 2014):
1. State capacity (can the government deliver services?)
2. Rule of law (is government itself constrained by law?)
3. Accountability (are citizens and opposition groups able to check government?)

All three needed; historical sequencing matters (China built state capacity first; US/UK built rule of law first).

---

## 5. Elinor Ostrom: Governing the Commons

Ostrom's *Governing the Commons* (1990; Nobel 2009) demolished both the "tragedy of the commons" (Hardin 1968) and the implied solutions.

**Hardin's tragedy** (1968): Shared pasture → each herder adds animals to maximize private gain → overgrazing → destruction. Conclusion: privatize or regulate.

**Ostrom's empirical counter**: Thousands of communities around the world have sustainably managed common pool resources (CPRs) for generations without privatization or external regulation:

```
OSTROM'S DESIGN PRINCIPLES FOR SUSTAINABLE CPR INSTITUTIONS:

1. Clearly defined boundaries
   Who has rights to use the resource; who is excluded

2. Rules match local conditions
   Rules are appropriate to local ecology and social context
   (not one-size-fits-all from outside)

3. Collective choice arrangements
   Most affected individuals can participate in modifying rules

4. Monitoring
   Monitors are accountable to resource users (not just external)

5. Graduated sanctions
   Rule violators face escalating penalties (not immediate punishment)

6. Conflict resolution mechanisms
   Rapid, low-cost local arenas for resolving disputes

7. Recognition of rights
   External government recognizes community's right to organize

8. Nested enterprises (for larger systems)
   Multiple layers of governance for larger, complex CPRs
```

**Polycentricity**: Ostrom's broader framework — governance should occur at multiple overlapping scales, not be centralized or purely privatized. Each CPR has different characteristics requiring different governance. No single optimal institution type.

---

## 6. Corruption and Rent-Seeking

**Rent-seeking** (Krueger 1974; Tullock 1967): spending resources to obtain government-created privileges (monopolies, subsidies, contracts) rather than creating value:

```
RENT-SEEKING MECHANISM:

  Government creates monopoly license (e.g., import permit)
  Value of monopoly = supernormal profits
  Firms spend up to that value competing for the license
    → resources spent on lobbying, bribes, political connections
    → resources NOT spent on production, innovation

  Social cost = resources wasted in competition
              + productive inefficiency from monopoly
              + distorted incentives for subsequent actors

  In weak-institution states, entire sectors can become
  rent-seeking oriented rather than productive.
```

**Corruption types**:
- Petty corruption (bribes to police, customs, license bureaus) → friction, inequality
- Grand corruption (procurement fraud, state capture) → misallocation, legitimacy crisis
- State capture (firms buy the rules themselves) → extractive institutions

**Cross-country measurement challenges**: Corruption Perceptions Index (CPI, Transparency International), World Bank Governance Indicators, ICRG. All are perception-based, not observed-behavior-based. Subject to information availability biases.

---

## 7. Varieties of Capitalism

Hall and Soskice (*Varieties of Capitalism*, 2001) argue that all capitalist economies are not converging to a single model:

```
LIBERAL MARKET ECONOMIES (LMEs)         COORDINATED MARKET ECONOMIES (CMEs)
US, UK, Canada, Australia                Germany, Japan, Sweden, Netherlands

FEATURE            LME                   CME
───────────────────────────────────────────────────────────────
Corporate finance  Equity markets        Patient bank capital
                   (quarterly earnings)  (long-term relationships)

Labor relations    Competitive wages,    Collective bargaining,
                   individual contracts  works councils, codetermination

Vocational         General skills        Specific, industry skills
training           (portable)            (firm/sector investment)

Inter-firm         Arms-length,          Collaborative, non-market
relations          competitive           coordination (associations)

Innovation type    Radical               Incremental
                   (disruption)          (quality improvement)

Comparative        High-tech, finance,   Capital goods, machine tools,
advantage          biotech               specialty chemicals, luxury goods
```

**Institutional complementarities**: LME elements fit together (liquid markets + general skills + radical innovation + flexible wages). CME elements fit together (patient capital + specific skills + incremental innovation + collective bargaining). Mixing them (importing one LME element into CME) can be dysfunctional.

---

## Decision Cheat Sheet

| Question | Framework | Key finding |
|----------|-----------|-------------|
| Why are some countries richer? | AJR + Acemoglu/Robinson | Colonial institutions → property rights → income; R² ≈ 0.52 |
| What are institutions? | North (1990) | Formal rules + informal norms + enforcement |
| Can communities govern shared resources? | Ostrom (1990) | Yes, with her 8 design principles |
| How does corruption harm development? | Rent-seeking theory | Diverts resources to unproductive competition |
| Why do different capitalisms persist? | Hall-Soskice VoC | Institutional complementarities prevent convergence |
| Does property titling help the poor? | de Soto + empirical lit. | Mixed: yes for investment; complications with commons, displacement |
| What's the difference between capacity and rule of law? | Fukuyama's triad | State capacity ≠ rule of law ≠ accountability; need all three |

---

## Common Confusion Points

**Institutions ≠ organizations**: North is explicit — institutions are rules, organizations are players (firms, governments, NGOs). The World Bank is an organization; the rules governing lending are institutions. Confusing these produces category errors in policy.

**AJR is causal identification, not the whole story**: The settler mortality instrument is clever but has limits: (1) applies only to former colonies (~1/3 of world); (2) settler mortality reflects disease ecology, not purely independent of geography (Sachs's counter); (3) the exclusion restriction is debatable (malaria still affects labor productivity directly).

**"Institutions matter" doesn't tell you which institutions to build**: The institutional turn showed correlation between broad institutional quality and development. It is much less informative about what specific institutional reforms to prioritize, in what sequence, in a particular country. Rodrik calls this "deep integration" without a map.

**Ostrom doesn't say privatization never works**: She showed that for CPRs (rivalrous but non-excludable goods like fisheries, groundwater, forests), community governance can outperform both privatization and state management. She does not claim this applies to all goods.

**Varieties of Capitalism is descriptive, not prescriptive**: VoC identifies institutional complementarities but doesn't say one variety is better. The LME/CME distinction is a positive typology, not a normative ranking. Comparative advantage in both is real — German manufacturing and US tech are both world-leading.
