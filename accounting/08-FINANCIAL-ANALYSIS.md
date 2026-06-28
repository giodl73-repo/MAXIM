---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:financial-analysis
kind: guide
module: accounting
section: accounting
title: Financial Statement Analysis - Ratios and DuPont
status: source-custody
source_custody: partial
current_path: accounting/08-FINANCIAL-ANALYSIS.md
canonical_path: accounting/08-FINANCIAL-ANALYSIS.md
backsource_ids: [proof-backfill:accounting:08-financial-analysis, git-history:accounting:08-financial-analysis]
concepts: [financial analysis, ratio analysis, liquidity, leverage, profitability, efficiency, DuPont]
root_concepts: [financial analysis]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Financial Statement Analysis — Ratios and DuPont

## The Big Picture

Ratio analysis turns the three statements into **comparable, dimensionless metrics** that
let you judge a firm against its own history, its peers, and benchmarks. Raw numbers are
unitful and scale-dependent (a $10M profit means nothing without context); ratios normalize
them. They cluster into four families — liquidity, leverage, profitability, efficiency — and
the **DuPont decomposition** stitches profitability into a single causal tree.

```
+--------------------------------------------------------------------------+
|                    FOUR RATIO FAMILIES                                  |
|                                                                          |
|   LIQUIDITY            LEVERAGE           PROFITABILITY    EFFICIENCY    |
|   "can it pay          "how much debt,    "does it make    "how hard do  |
|    near-term?"          can it service?"   money?"          assets work?"|
|   ----------           ---------------    -------------    ------------- |
|   Current ratio        Debt-to-equity     Gross margin     Asset turnover|
|   Quick ratio          Debt-to-assets     Operating margin Inventory t/o |
|   Cash ratio           Interest coverage  Net margin       Receivables   |
|                        (times interest)   ROA, ROE, ROIC   turnover (DSO)|
|        |                     |                  |               |        |
|        v                     v                  v               v        |
|   from BALANCE         from BS + IS        from INCOME      from IS + BS  |
|   SHEET               (coverage from IS)    STATEMENT       (flow / state)|
|                                                                          |
|              All four converge in DUPONT (decomposes ROE)               |
+--------------------------------------------------------------------------+
```

**Read it as four lenses on one firm.** Liquidity = short-term survival; leverage = solvency
and risk; profitability = does it create value; efficiency = how productively it uses assets.
DuPont (below) shows they're not independent.

---

## Family 1: Liquidity — Can It Pay Near-Term?

Liquidity ratios test whether liquid assets cover near-term obligations. All come from the
balance sheet (file 02).

| Ratio | Formula | Reads as |
|-------|---------|----------|
| **Current ratio** | Current assets / Current liabilities | Broad short-term cushion |
| **Quick ratio (acid test)** | (Current assets − Inventory) / Current liabilities | Cushion *excluding* hard-to-sell inventory |
| **Cash ratio** | (Cash + equivalents) / Current liabilities | Most conservative — cash only |

```
   Tightening the test:
   Current  >  Quick  >  Cash
   (includes        (drops          (only
    inventory)       inventory)      cash)

   Current ratio 2.0, quick ratio 0.5  -> liquidity is mostly INVENTORY.
   If that inventory is stale, the firm is less liquid than current
   ratio suggests. Always check the gap.
```

A current ratio around 1.5–2.0 is conventionally healthy, but it's industry-dependent (a
grocer turns inventory fast and runs lean; a heavy manufacturer holds more). The *quick
ratio* is the sharper instrument because inventory is the least-liquid current asset and the
easiest to overstate.

---

## Family 2: Leverage — How Much Debt, Can It Service?

Leverage (solvency) ratios test long-run survival and financial risk. They mix the balance
sheet (debt levels) with the income statement (ability to cover interest).

| Ratio | Formula | Reads as |
|-------|---------|----------|
| **Debt-to-equity** | Total debt / Total equity | $ of debt per $ of equity |
| **Debt-to-assets** | Total debt / Total assets | Fraction of assets funded by debt |
| **Interest coverage (TIE)** | EBIT / Interest expense | How many times earnings cover interest |
| **Net debt / EBITDA** | (Debt − Cash) / EBITDA | Years of earnings to repay net debt |

```
   LEVERAGE is a double-edged amplifier:

   More debt  -> magnifies ROE when returns > cost of debt   (good)
              -> magnifies losses & default risk in downturns (bad)

   Interest coverage of 8x = comfortable.
   Interest coverage of 1.5x = fragile; a small EBIT dip -> can't pay.
```

**Bridge to `finance/`:** leverage is the capital-structure question — the Modigliani-Miller
backdrop, the tax shield of debt vs the cost of financial distress. Here you *measure* it;
`finance/` *optimizes* it. **Bridge to `economics/`:** leverage is how the firm amplifies
returns on equity by substituting cheaper debt capital — at the cost of fragility.

---

## Family 3: Profitability — Does It Make Money?

Profitability ratios scale profit by revenue (margins) or by capital (returns).

### Margins (profit per dollar of revenue) — from the income statement (file 03)

| Margin | Formula |
|--------|---------|
| Gross margin | Gross profit / Revenue |
| Operating margin | Operating income (EBIT) / Revenue |
| Net margin | Net income / Revenue |

### Returns (profit per dollar of capital) — IS over BS

| Return | Formula | Measures |
|--------|---------|----------|
| **ROA** | Net income / Total assets | Profit per dollar of assets (operating efficiency) |
| **ROE** | Net income / Shareholders' equity | Profit per dollar of owner capital |
| **ROIC** | NOPAT / Invested capital | Return on capital *actually deployed*, financing-neutral |

```
   ROA < ROE  ALWAYS, for a leveraged firm.
   The gap is LEVERAGE: debt funds assets that earn returns for
   equity holders. More debt -> wider ROE-vs-ROA gap -> more risk.

   ROIC vs cost of capital (WACC) is the real value test:
     ROIC > WACC  -> the firm CREATES value
     ROIC < WACC  -> it DESTROYS value (even if "profitable")
```

ROIC vs WACC is the single most important value question and the bridge to `finance/`:
accounting profitability (positive net income) is not the same as *economic* value creation
(ROIC above cost of capital). A "profitable" firm earning below its cost of capital is
destroying shareholder value.

---

## Family 4: Efficiency — How Hard Do Assets Work?

Efficiency (activity) ratios pair an income-statement *flow* with a balance-sheet *level* to
measure throughput per unit of asset.

| Ratio | Formula | Reads as |
|-------|---------|----------|
| **Asset turnover** | Revenue / Total assets | Revenue generated per $ of assets |
| **Inventory turnover** | COGS / Average inventory | How many times inventory cycles/year |
| **Days inventory (DIO)** | 365 / Inventory turnover | Days to sell inventory |
| **Receivables turnover** | Revenue / Average AR | How fast credit sales are collected |
| **Days sales outstanding (DSO)** | 365 / Receivables turnover | Days to collect a sale |
| **Days payables (DPO)** | 365 / (COGS / Avg AP) | Days you take to pay suppliers |

### The cash conversion cycle (a systems-level efficiency view)

```
   CASH CONVERSION CYCLE = DIO + DSO - DPO

         buy inventory        sell it          collect cash
   --------|-------------------|------------------|---------->
           <------ DIO ------->
                               <----- DSO ------->
   <----------- DPO ----------->
           (you pay suppliers here)

   CCC = how many days your cash is TIED UP in operations.
   Lower is better. Negative CCC (Amazon, Dell) = suppliers
   finance your operations -- you collect before you pay.
```

The cash conversion cycle is the throughput-vs-latency view of working capital: it's how
long a dollar is "in flight" through the operating pipeline. Shortening it frees cash without
raising a dime of capital — the operational lever behind many turnarounds.

---

## DuPont Analysis — Decomposing ROE

DuPont is the unifying framework: it factors **ROE** into the contributions of profitability,
efficiency, and leverage — showing *why* ROE is what it is and *which lever* to pull.

### Three-step DuPont

```
   ROE = Net Profit Margin  x  Asset Turnover  x  Equity Multiplier
       = (NI / Revenue)     x  (Revenue/Assets) x  (Assets / Equity)
          \____________/        \____________/       \____________/
          PROFITABILITY          EFFICIENCY            LEVERAGE
          "earn per sale"        "sweat the assets"    "amplify with debt"

   Note the algebra: Revenue and Assets cancel ->  ROE = NI / Equity.
   The decomposition is an IDENTITY; it just attributes the result.
```

### Worked example

```
   Net income      120     Revenue   1,000   Assets  800   Equity  400

   Net margin      = 120 / 1,000 = 12%
   Asset turnover  = 1,000 / 800 = 1.25x
   Equity multipl. = 800 / 400   = 2.0x

   ROE = 0.12 x 1.25 x 2.0 = 0.30 = 30%
   Check: 120 / 400 = 30%   OK

   Diagnosis: a 30% ROE -- but HALF of it comes from 2x leverage.
   Strip leverage (ROA = margin x turnover = 0.12 x 1.25 = 15%).
   Two firms with identical 30% ROE can be radically different:
   one earns it operationally (high ROA), one borrows it (high multiplier).
```

This is DuPont's whole value: **two firms with the same ROE can have completely different
risk profiles.** A high ROE driven by leverage is fragile; a high ROE driven by margin and
turnover is durable. The five-step DuPont further splits margin into operating margin × tax
burden × interest burden to isolate the drag of financing and tax.

```
   FIVE-STEP DuPont (extends the margin term):
   ROE = (NI/EBT) x (EBT/EBIT) x (EBIT/Rev) x (Rev/Assets) x (Assets/Eq)
          tax       interest     operating    asset           leverage
          burden    burden       margin       turnover
```

---

## How to Actually Use Ratios

A ratio alone is meaningless. Three comparisons give it meaning:

```
   1. TREND   (this firm over time)     -- is it improving or decaying?
   2. PEER    (vs competitors)          -- relative position in industry
   3. BENCHMARK (vs industry norm/rule) -- absolute health

   Plus: COMMON-SIZE statements
     - Income statement: every line as % of revenue
     - Balance sheet:    every line as % of total assets
     -> makes firms of different SIZE directly comparable
```

**Caveats that matter:** ratios use accounting numbers, so they inherit accounting choices
(LIFO vs FIFO inventory inflates/deflates turnover; off-balance-sheet items hide leverage).
Always check the choices (file 09) before trusting a comparison.

---

## Old World → New World Bridges

| Prior art | Analysis concept |
|-----------|------------------|
| Normalizing metrics (dimensionless) | Ratios (strip scale/units for comparison) |
| Throughput / latency / items-in-flight | Cash conversion cycle (days cash in pipeline) |
| Utilization (work per resource) | Asset turnover, inventory turnover |
| Latency to settle a request | Days sales outstanding (collection latency) |
| Amplifier with gain and instability | Leverage (magnifies ROE and risk) |
| Factoring a metric into causal terms | DuPont decomposition of ROE |
| Benchmarking vs baseline/peers/SLO | Trend / peer / industry-benchmark comparison |
| Return on investment vs cost of capital | ROIC vs WACC (value creation test) |

---

## Decision Cheat Sheet

| Question | Ratio | Healthy direction |
|----------|-------|-------------------|
| Can it pay bills this year? | Current / quick ratio | ≥ ~1.5 / ≥ ~1.0 (industry-dependent) |
| Is inventory propping up liquidity? | Current vs quick gap | Small gap = liquid; large = inventory-heavy |
| How risky is its debt load? | Debt-to-equity, interest coverage | Lower D/E; coverage well above ~3x |
| Does it create real value? | ROIC vs WACC | ROIC > WACC |
| Why is ROE high? | DuPont (margin × turnover × leverage) | Prefer margin/turnover over leverage |
| How fast is cash tied up? | Cash conversion cycle | Lower (or negative) is better |
| Compare firms of different size | Common-size statements | — |

---

## Common Confusion Points

### "Higher ROE is always better"

Not if it's manufactured by leverage. DuPont shows ROE = margin × turnover × *equity
multiplier*. A firm can juice ROE by loading on debt, which also loads on default risk. Strip
to ROA/ROIC to see operational quality; check interest coverage to see if the leverage is
survivable.

### "Positive net income means the firm creates value"

Accounting profit ignores the cost of *equity* capital. A firm earning 5% ROIC against a 10%
WACC is "profitable" on the income statement but destroying value — its equity holders would
do better elsewhere. The economic test is ROIC vs WACC (bridge to `finance/`), not net income.

### "A current ratio above 1 means it's safe"

Current ratio includes inventory and prepaids, which may not convert to cash in time. Check
the quick ratio and the *quality* of the current assets. Conversely, a very *high* current
ratio can signal idle cash or bloated inventory — inefficiency, not just safety.

### "Ratios are objective"

They inherit every accounting choice underneath them. LIFO vs FIFO swings inventory turnover;
operating-lease treatment swings leverage; revenue-recognition timing swings margins. A
peer comparison across firms using different methods is apples-to-oranges until normalized.

### "Inventory turnover up is always good"

Usually it signals efficiency, but extreme turnover can mean understocking and lost sales
(stockouts), and a sudden jump can come from a write-down (lower inventory denominator), not
better sales. Pair it with margins and the days-inventory trend before concluding.
