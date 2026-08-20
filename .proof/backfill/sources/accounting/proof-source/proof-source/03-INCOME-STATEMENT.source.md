---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-INCOME-STATEMENT.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:income-statement
kind: guide
module: accounting
section: accounting
title: The Income Statement - The Period Delta
status: source-custody
source_custody: partial
current_path: accounting/03-INCOME-STATEMENT.md
canonical_path: accounting/03-INCOME-STATEMENT.md
backsource_ids: [proof-backfill:accounting:03-income-statement, git-history:accounting:03-income-statement]
concepts: [income statement, revenue recognition, COGS, gross margin, operating margin, EPS]
root_concepts: [income statement]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Income Statement — The Period Delta

## The Big Picture

If the balance sheet is state, the income statement is the **delta applied over a period**.
It answers one question: *did we make money between two dates, and how?* It starts at the
top with revenue and subtracts cost layers in a strict order, exposing a margin at each
level. Its bottom line — net income — flows into retained earnings on the balance sheet.

```
+--------------------------------------------------------------------------+
|              INCOME STATEMENT  —  for a PERIOD (e.g. FY2026)             |
|                                                                          |
|   REVENUE (net sales)                                       1,000        |
|     - Cost of Goods Sold (COGS)                              (400)        |
|   ============================================                           |
|   GROSS PROFIT                                                600  (60%) |
|     - Operating expenses (SG&A, R&D, depreciation)          (350)        |
|   ============================================                           |
|   OPERATING INCOME (EBIT)                                     250  (25%) |
|     - Interest expense                                        (40)        |
|     + Other income / (expense)                                 10         |
|   ============================================                           |
|   PRE-TAX INCOME (EBT)                                        220         |
|     - Income tax expense (e.g. 21%)                           (46)        |
|   ============================================                           |
|   NET INCOME                                                  174  (17%) |
|   ============================================                           |
|     / weighted-avg shares (e.g. 100)                                     |
|   EARNINGS PER SHARE (EPS)                                   $1.74        |
+--------------------------------------------------------------------------+
                              |
                              v
              flows into RETAINED EARNINGS (balance sheet)
```

**Read it top-down as a waterfall**: each line strips out one category of cost and reveals a
profitability level. The order is fixed and meaningful — gross before operating before net.

---

## The Margin Waterfall (the conceptual spine)

Each subtotal isolates a different driver of profitability. Knowing *which* margin moved
tells you *what* changed in the business.

```
   REVENUE
      |  minus the direct cost of what you sold
      v
   GROSS PROFIT  ---- gross margin = how much each sale contributes
      |               before running the company
      |  minus the cost of running the company (sales, admin, R&D)
      v
   OPERATING INCOME (EBIT) ---- operating margin = core-business
      |                          profitability, financing-neutral
      |  minus financing cost (interest) +/- non-core items
      v
   PRE-TAX INCOME (EBT)
      |  minus taxes
      v
   NET INCOME  ---- net margin = what's left for owners
```

| Margin | Formula | Tells you |
|--------|---------|-----------|
| Gross margin | Gross profit / Revenue | Pricing power & production efficiency |
| Operating margin | Operating income / Revenue | Core operating efficiency (financing-neutral) |
| Net margin | Net income / Revenue | Overall bottom-line profitability |

**Why EBIT matters:** operating income is *before* interest and tax, so it compares two
firms' operating performance independent of how they're financed or taxed. `finance/` uses
EBIT and EBITDA heavily in valuation multiples for exactly this reason.

---

## Revenue Recognition — The Hard Part

Revenue is recognized when **earned**, not when cash arrives (the accrual principle, file
05). The modern standard — **ASC 606** (US GAAP) / **IFRS 15**, substantially converged — is
a single **five-step model**:

```
   +----------------------------------------------------------------+
   |  ASC 606 / IFRS 15  —  THE FIVE STEPS                          |
   |                                                                |
   |  1. Identify the CONTRACT with the customer                    |
   |  2. Identify the PERFORMANCE OBLIGATIONS (distinct promises)   |
   |  3. Determine the TRANSACTION PRICE                            |
   |  4. ALLOCATE the price to each obligation                      |
   |  5. RECOGNIZE revenue as each obligation is SATISFIED          |
   +----------------------------------------------------------------+
```

The principle: recognize revenue when **control transfers to the customer** — either at a
point in time (ship the box) or over time (deliver a service across months).

### Worked example — a software bundle

```
   DEAL: $1,200 paid up front for a 12-month SaaS subscription
         + a one-time $300 setup service delivered in month 1.
         Total contract = $1,500.

   Step 2: two performance obligations — setup (point in time) and
           subscription (over time).
   Step 4: allocate $300 to setup, $1,200 to subscription.
   Step 5:
     Month 1:  recognize $300 setup + $100 (1/12 of subscription) = $400
     Months 2-12: recognize $100/month subscription

   At signing (cash received, nothing earned yet):
     DR Cash               1,500
        CR Deferred revenue       1,500     <- liability, not revenue

   Each month as earned:
     DR Deferred revenue    100 (+300 in month 1)
        CR Revenue                100 (+300 in month 1)
```

The $1,500 cash hits the bank on day one, but only $400 is *revenue* in month 1. The rest
sits as **deferred revenue** (a balance-sheet liability, file 02) and is released monthly.
This is the single most important revenue concept for a subscription business.

**Bridge:** revenue recognition is *event-time* accounting — you recognize at the moment the
economic obligation is satisfied, not when the payment packet arrives. Cash-basis would be
arrival-time; accrual is event-time with a deferral buffer.

---

## COGS and the Inventory Flow

Cost of Goods Sold is the **direct cost of the units actually sold** this period — matched
against the revenue they generated (the matching principle, file 05). Unsold units stay in
inventory (an asset) until sold.

```
   Beginning inventory          100
   + Purchases / production      400
   = Goods available for sale    500
   - Ending inventory           (150)
   = COGS                        350   <- only the SOLD portion hits the IS
```

When prices change, *which* units are deemed "sold" affects COGS and ending inventory. The
cost-flow assumptions:

| Method | Assumes you sell... | In rising prices → | LIFO allowed? |
|--------|--------------------|--------------------|---------------|
| **FIFO** | Oldest units first | Lower COGS, higher profit, higher tax | Yes (GAAP & IFRS) |
| **LIFO** | Newest units first | Higher COGS, lower profit, lower tax | **GAAP only — IFRS bans it** |
| **Weighted average** | Blended cost | Between FIFO and LIFO | Yes (GAAP & IFRS) |

The LIFO/FIFO choice is a real lever on reported profit and on cash taxes. US firms that
expect inflation often choose LIFO for the tax shield; IFRS firms cannot (IAS 2). This is one
of the most consequential GAAP/IFRS divergences (file 09).

---

## EPS — Per-Share Profitability

Earnings per share normalizes net income by share count so investors can compare across
firms and over time (the denominator in the P/E ratio that `finance/` uses).

```
                    Net income - Preferred dividends
   Basic EPS  =  ---------------------------------------
                   Weighted-average common shares

   Diluted EPS =  same numerator (adjusted)
                  -------------------------------------------------
                  shares + dilutive options/convertibles/RSUs
```

| Concept | Meaning |
|---------|---------|
| Basic EPS | Profit per share actually outstanding |
| Diluted EPS | Worst-case: assumes all options/convertibles exercise — always ≤ basic |
| Weighted-average shares | Shares weighted by how long they were outstanding in the period |

**Why diluted matters to you as a VP:** employee stock options and RSUs are dilutive. Heavy
equity comp shows up as a gap between basic and diluted EPS — the "overhang" that future
issuance will create.

---

## A Subtlety: Net Income vs Comprehensive Income

Some gains/losses bypass net income and go straight to equity (Accumulated Other
Comprehensive Income, file 02): foreign-currency translation, certain pension and hedge
adjustments. **Comprehensive income = net income + OCI.** Net income is what hits EPS and
retained earnings; OCI is parked in AOCI on the balance sheet. It exists so volatile,
unrealized items don't whipsaw reported earnings.

---

## Old World → New World Bridges

| Prior art | Income statement concept |
|-----------|-------------------------|
| Per-frame / per-tick delta | The income statement (period flow vs balance-sheet state) |
| Event-time stream processing | Revenue recognition (recognize at obligation satisfaction) |
| Buffered / windowed events | Deferred revenue released over the subscription window |
| Normalizing a metric per unit | EPS (net income per share) |
| Worst-case capacity planning | Diluted EPS (assume all options exercise) |
| Separating signal from noise | Operating income (strips financing/tax noise from core ops) |
| Cost attribution to a request | Matching COGS to the revenue it generated |

---

## Decision Cheat Sheet

| I want to know... | Line / metric |
|-------------------|---------------|
| Pricing power & unit economics | Gross margin |
| Core operating efficiency (financing-neutral) | Operating margin (EBIT) |
| Overall profitability for owners | Net margin |
| Profit per share / feeds P/E | Basic EPS |
| Effect of options/RSUs on shareholders | Diluted EPS (and the basic-vs-diluted gap) |
| When a subscription's cash becomes profit | Revenue recognition schedule (ASC 606) |
| Effect of inventory method on tax | FIFO vs LIFO (LIFO only under GAAP) |
| Whether earnings are "clean" | Compare net income vs cash flow (file 04); watch one-time items |

---

## Common Confusion Points

### "Revenue is the money we collected this period"

No — revenue is what we **earned** (delivered) this period, regardless of when cash arrives.
A subscription paid annually in advance is earned monthly; a sale on credit is revenue now
even though cash comes later. Cash is the cash flow statement's job (file 04).

### "Net income is the cash we made"

No, and the gap is large and routine. Net income includes non-cash items (depreciation,
stock comp) and excludes cash items (capex, debt repayment, inventory build). A profitable
company can be cash-negative. File 04 reconciles the two.

### "Higher revenue means a better quarter"

Not if margins collapsed. Revenue up 20% with gross margin down from 60% to 40% can mean
*less* gross profit. Always read the margin waterfall, not just the top line.

### "EBITDA is profit"

EBITDA (earnings before interest, taxes, depreciation, amortization) is not a GAAP figure
and is not profit — it deliberately ignores real costs (capex shows up as depreciation;
financing as interest). It's a useful *operating* proxy and a valuation input in `finance/`,
but a capital-intensive business that's "EBITDA-positive" can still be losing money and cash.

### "Deferred revenue is on the income statement"

It is a **balance-sheet liability** (file 02). It only touches the income statement as it is
*released* into revenue over time. The unearned portion never appears as revenue.
