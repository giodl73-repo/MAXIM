# Macroeconomics — GDP, Monetary Policy, Growth, Business Cycles

---

## Big Picture

<!-- @editor[diagram/P2]: Diagram lists key questions and analysis levels but doesn't show how the macro framework connects — e.g., how IS-LM produces AD, how AS-AD determines short-run output, how monetary policy feeds through the Taylor rule into IS-LM, how Solow determines long-run potential -->
```
MACROECONOMICS: aggregate phenomena — entire economies, not individual agents

KEY QUESTIONS:
  Why do countries grow rich or stay poor? (Growth theory)
  Why do economies boom and bust? (Business cycle theory)
  What should central banks do? (Monetary policy)
  How much should governments tax and spend? (Fiscal policy)
  Why is unemployment persistent? (Labor markets)
  What determines exchange rates? (International macro)

LEVELS OF ANALYSIS:
  Short run: prices sticky → output determined by demand
  Medium run: wages/prices adjust → output returns to potential
  Long run: capital accumulation and technology determine potential output
```

---

## National Income Accounting

### GDP and Its Components

```
GDP = C + I + G + NX   (expenditure approach)

C  = private consumption (households: food, cars, services)
I  = private investment (firms: equipment, buildings, inventories; households: homes)
G  = government purchases (not transfer payments)
NX = net exports = Exports - Imports

ALTERNATIVE MEASURES:
  GNP = GDP + income earned abroad by residents - income earned domestically by foreigners
  GNI = GNP (modern term)
  NDP = GDP - depreciation
  National income ≈ GNP - depreciation - indirect taxes + subsidies

GDP DEFLATOR = (Nominal GDP / Real GDP) × 100
Real GDP: values output at constant base-year prices (removes inflation)

CPI (Consumer Price Index): price of fixed basket of consumer goods
  Inflation rate: π = (CPI_t - CPI_{t-1})/CPI_{t-1}
  PCE deflator: Fed prefers this (broader, adjusts for substitution)

UNEMPLOYMENT RATE = Unemployed / Labor Force × 100
  Labor force = employed + actively looking (not discouraged workers)
  NAIRU: non-accelerating inflation rate of unemployment (~4-5% in US)
  Okun's law: 1% below NAIRU → ~2% above potential GDP
```

---

## National Savings and Investment Identity

```
CLOSED ECONOMY:
  Y = C + I + G   (GDP identity)
  Y - C - G = I
  S_private + S_govt = I
  (Y - C - T) + (T - G) = I
  Private saving + Public saving = Investment

OPEN ECONOMY: Y = C + I + G + NX
  S - I = NX   (current account = savings surplus)
  When S > I: country lends abroad (capital outflow), NX > 0
  When S < I: country borrows abroad (capital inflow), NX < 0
  US: chronically NX < 0 → trade deficit = capital account surplus (foreigners invest in US)
```

---

## IS-LM Model (Short Run, Closed Economy)

### IS Curve (Investment = Saving)

```
Y = C(Y-T) + I(r) + G

Where C'(·) = marginal propensity to consume (MPC, 0 < MPC < 1)
      I'(r) < 0: investment decreases as real interest rate r increases

EQUILIBRIUM: goods market clears → Y determined
IS curve: downward sloping in (Y, r) space
  (Higher r → lower I → lower Y; or lower G shifts IS left)

MULTIPLIER: ΔY = ΔG × 1/(1-MPC)
  MPC=0.8 → multiplier = 5 (but Ricardian equivalence argues it may be near 1)
```

### LM Curve (Money Market)

```
M/P = L(Y, r)   (money demand = money supply)

M = money supply (controlled by central bank)
P = price level (fixed in short run)
L = liquidity demand: L_Y > 0 (more income → more transactions → more money needed)
                      L_r < 0 (higher r → more attractive to hold bonds → less cash)

LM curve: upward sloping in (Y, r) space
  (Higher Y → more money demand → higher r to equilibrate; or ↑M shifts LM right)

LIQUIDITY TRAP: r at zero lower bound → LM horizontal
  Monetary policy (increase M) ineffective → fiscal policy needed (IS shift)
  Japan 1990s-2000s, US/EU 2008-2015
```

### Policy Effects (IS-LM)

```
FISCAL EXPANSION (↑G or ↓T): IS shifts right
  → Higher Y and higher r (partial crowding out of investment)
  Crowding out: government spending raises r → reduces private I → partial offset

MONETARY EXPANSION (↑M): LM shifts right
  → Higher Y and lower r
  Effective unless liquidity trap

MUNDELL-FLEMING (open economy IS-LM):
  Fixed exchange rate: monetary policy ineffective (sterilization required)
  Floating exchange rate: fiscal policy ineffective (crowded out by exchange rate)
  → Open economy complicates policy
```

---

## AS-AD Model (Short and Medium Run)

### Aggregate Demand (AD)

```
From IS-LM: as P falls, M/P rises → LM shifts right → Y increases
AD curve: downward sloping in (Y, P) space

Shifts: fiscal expansion (G↑) or monetary expansion (M↑) → AD shifts right
```

### Aggregate Supply (AS)

```
SHORT-RUN AS (SRAS): upward sloping in (Y, P) space
  Wages sticky in short run → firms respond to price increases by raising output
  SRAS: P = P^e + (1/α)(Y - Ȳ)   (price = expected price + output gap term)
  At Y = Ȳ (potential output): P = P^e

LONG-RUN AS (LRAS): vertical at Ȳ
  In long run: wages/prices fully adjust → output returns to potential regardless of P
  Ȳ determined by capital, labor, technology (production function)
```

### Short-Run Stabilization

```
NEGATIVE DEMAND SHOCK (e.g., financial crisis):
  AD shifts left → Y falls below Ȳ → recession
  Short run: P falls, Y < Ȳ (unemployment above NAIRU)
  Medium run: wages fall (workers accept lower wages) → SRAS shifts right → Y → Ȳ
  → Self-correcting mechanism (but SLOW: Keynes: "in the long run we are all dead")

POLICY OPTIONS:
  Wait for self-correction (small government approach)
  Fiscal expansion (larger G or lower T): shift AD right
  Monetary expansion (lower r via ↑M): shift AD right

SUPPLY SHOCK (e.g., oil price spike):
  SRAS shifts left → higher P AND lower Y ("stagflation")
  Painful: tightening policy reduces inflation but worsens recession
  Accommodating: keep Y stable → inflation persists → need later painful disinflation
```

---

## Monetary Policy

### Money Supply and Money Multiplier

```
CENTRAL BANK CREATES HIGH-POWERED MONEY (monetary base):
  H = currency in circulation + bank reserves

MONEY MULTIPLIER:
  M = H / (c + θ(1-c))
  c = currency-deposit ratio (public behavior)
  θ = reserve ratio (banks keep fraction θ of deposits as reserves)
  If θ=0.1, c=0.2: multiplier = 1/(0.2 + 0.1×0.8) = 1/0.28 ≈ 3.6

QUANTITATIVE EASING (QE):
  Central bank buys long-term bonds → increases H → shifts LM right
  Also reduces long-term rates directly (not just overnight rates)
  Fed balance sheet: $900B pre-2008 → $8.9T post-2020 QE
```

### Taylor Rule

Empirical description of how Fed sets interest rates:

```
i = r* + π + 0.5(π - π*) + 0.5(Y - Ȳ)/Ȳ

i = nominal federal funds rate
r* = neutral real rate (~2% pre-2008, possibly lower now)
π = current inflation
π* = inflation target (2% in US)
First 0.5: respond to inflation gap
Second 0.5: respond to output gap

If π = 5%, π* = 2%, Y = Ȳ:
i = 2 + 5 + 0.5(5-2) + 0 = 8.5% (roughly what Fed did in 2022-2023)

INFLATION EXPECTATION MANAGEMENT:
  π^e matters: high expected inflation → workers demand higher wages → actual inflation rises
  Central bank credibility: if people trust 2% target → self-fulfilling
  Inflation targeting (BoE, ECB, Fed post-2012): explicit 2% target → anchors expectations
```

### Zero Lower Bound and Unconventional Monetary Policy

```
NOMINAL INTEREST RATES cannot go significantly below zero (cash holding)
  → Constrains monetary policy in severe recessions

UNCONVENTIONAL TOOLS:
  Forward guidance: "keep rates near zero for extended period" → shift long-term expectations
  QE (Quantitative Easing): buy long bonds → lower long-term rates
  Yield curve control (Japan): target specific yield on 10-year bond
  Negative interest rates (ECB, Japan): charge banks for reserves → incentivize lending

EFFECTIVENESS DEBATE: QE worked in 2009 to stabilize financial system;
  effectiveness at boosting real economy more disputed
  Portfolio balance channel: push investors from safe assets to riskier → lower credit spreads
```

---

## Growth Theory

### Solow Model (1956, Nobel 1987)

```
PRODUCTION FUNCTION: Y = F(K, AL) = (AL)^{1-α} K^α   (Cobb-Douglas with technology A)
  K = capital, L = labor, A = technology (labor-augmenting)
  Effective labor = AL; α ≈ 1/3

CAPITAL ACCUMULATION:
  K̇ = sY - δK   (savings minus depreciation)
  s = savings rate (0 < s < 1), δ = depreciation rate

IN PER EFFECTIVE WORKER TERMS (k = K/AL, y = Y/AL):
  k̇ = sy - (δ + n + g)k   (n = population growth, g = technology growth)
  sy = sf(k) = sk^α    (savings per effective worker)
  (δ+n+g)k = "break-even investment" (maintain k constant)

STEADY STATE k*: sy = (δ+n+g)k → k* = (s/(δ+n+g))^{1/(1-α)}

GOLDEN RULE k_gold: maximize consumption per worker
  MPK = δ+n+g → c_max at MPK = break-even investment slope
  For Cobb-Douglas: k_gold = (αs_gold/(δ+n+g))^{1/(1-α)}, s_gold = α

CONVERGENCE: Poor countries grow faster than rich countries (conditional on same parameters)
  Evidence: conditional convergence within OECD; unconditional convergence not universal

LIMITS OF SOLOW: Technology growth (g) is exogenous — "manna from heaven"
  Does NOT explain why some countries have higher A
  → Endogenous growth theory
```

### Endogenous Growth

```
AK MODEL: Y = AK (no diminishing returns to capital)
  Possible if: K includes human capital (Lucas) or knowledge (Romer)
  K̇ = sAK - δK → Y/Y = sA - δ = constant growth without diminishing returns

ROMER MODEL (1990, Nobel 2018):
  Growth driven by IDEAS (nonrival goods: one person's use doesn't reduce others')
  Monopolistic competition in ideas: firms invest in R&D for temporary monopoly profit
  Growth rate: g ∝ R&D investment, number of researchers
  Policy implications: subsidize R&D, education → increase g (not just level)

WHY COUNTRIES DIFFER:
  Institutions (Acemoglu, Robinson Nobel 2024): secure property rights, rule of law
    → Extractive vs inclusive institutions
    → Colonial history: extractive institutions → persistent poverty
  Human capital (education, health)
  Geography (disease burden, trade costs)
  Culture (Guido Tabellini)
```

---

## Business Cycles

### RBC vs Keynesian

```
REAL BUSINESS CYCLE (RBC, Kydland-Prescott 1982, Nobel 2004):
  Business cycles = optimal responses to technology shocks
  Prices/wages fully flexible at all times
  Fluctuations: NOT market failures → no policy intervention needed
  Evidence: too simple; fails to match many empirical regularities

NEW KEYNESIAN:
  Sticky prices + wages (menu costs, implicit contracts, efficiency wages)
  Monetary policy has real effects in short run
  Optimal policy: stabilize output + inflation (Taylor rule)
  DSGE (Dynamic Stochastic General Equilibrium): NK workhorse model
  Shocks: demand (preference), supply (technology), financial (credit), policy

2008 FINANCIAL CRISIS:
  Credit channel: financial system amplifies (Bernanke Nobel 2022)
  Zero lower bound: conventional monetary policy constrained → QE, fiscal stimulus
  Balance sheet recession (Koo): private sector deleveraging → secular stagnation
```

### Fiscal Multipliers

```
GOVERNMENT SPENDING MULTIPLIER:
  Keynesian estimate: 1.5-2.5 (crowding in during recession, excess capacity)
  New Classical: 0 (Ricardian equivalence: consumers anticipate future taxes)
  Empirical estimates: 0.5-1.5 depending on state of economy, monetary accommodation

RICARDIAN EQUIVALENCE (Barro):
  Tax cut today = future tax increase (government must repay debt)
  Forward-looking consumers save tax cut → no effect on current demand
  Fails when: liquidity-constrained consumers, distortionary taxes, myopic behavior

DEBT SUSTAINABILITY:
  Primary balance needed: b ≥ d × (r - g)
  d = debt/GDP, r = real interest rate, g = real GDP growth
  r < g: government can sustain stable debt without primary surpluses (Japan, US in 2010s)
  r > g: debt spiral without primary surpluses

2020 COVID: US debt/GDP: 79% → 133% in one year
  Sustainable if r < g holds long-term
  2022: r spiked (Fed tightening) → debt sustainability concerns return
```

---

## International Macro

### Exchange Rates

```
PURCHASING POWER PARITY (PPP):
  Law of one price → S × P* = P (exchange rate S × foreign price = domestic price)
  PPP exchange rate: equalizes purchasing power across countries
  Actual rates deviate from PPP (Balassa-Samuelson: non-tradables cheaper in poor countries)
  Use PPP for comparing living standards across countries

UNCOVERED INTEREST RATE PARITY (UIP):
  E[ΔS] = r - r*
  Expected appreciation = domestic rate - foreign rate
  → Higher domestic rate → currency expected to depreciate (rate differential = risk premium)
  Carry trade: borrow low-rate currency (JPY), invest in high-rate currency (USD/EM)
  UIP often violated in short run (forward premium puzzle)

TRILEMMA (Mundell-Fleming):
  Cannot simultaneously have:
  1. Fixed exchange rate
  2. Free capital mobility
  3. Independent monetary policy
  Choose any two:
  Bretton Woods: 1+3, capital controls
  Euro zone: 1+2, gave up 3 (ECB monetary policy, no national monetary independence)
  US/UK: 2+3, floating exchange rate
```

---

## Decision Cheat Sheet

| Policy tool | Effect | Works best when |
|-------------|--------|----------------|
| Interest rate cut (↓r) | IS-LM: AD right → Y↑, P↑ | Not at ZLB, not liquidity trap |
| Fiscal expansion (↑G) | AD right → Y↑ | Recession with monetary accommodation |
| QE | Lower long rates, support asset prices | ZLB, financial crisis |
| Forward guidance | Shift expectations → lower long rates | ZLB |
| ↑s (savings rate) | Solow: higher k*, higher Y/L | Long run only (transition costs) |
| ↑A (technology) | Endogenous: permanent growth rate ↑ | R&D subsidies, education |

| Concept | Formula | Interpretation |
|---------|---------|----------------|
| GDP | C + I + G + NX | Expenditure approach |
| Multiplier | 1/(1-MPC) | Fiscal stimulus amplification |
| Solow steady state | k* = (s/(δ+n+g))^{1/(1-α)} | Long-run capital per worker |
| Taylor rule | i = r* + π + 0.5(π-π*) + 0.5 gap | Fed funds rate target |
| PPP | S = P/P* | Exchange rate from price parity |
| Debt sustainability | r < g → no primary surplus needed | Fiscal space condition |

<!-- @editor[structure/P2]: Missing Common Confusion Points section — natural gotchas: real vs nominal interest rates, GDP vs GNP vs GNI, CPI vs GDP deflator vs PCE, Ricardian equivalence assumptions, why zero lower bound matters, money multiplier in practice vs theory -->
