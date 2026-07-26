---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-CASH-FLOW-STATEMENT.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:cash-flow-statement
kind: guide
module: accounting
section: accounting
title: The Cash Flow Statement - Following the Money
status: source-custody
source_custody: partial
current_path: accounting/04-CASH-FLOW-STATEMENT.md
canonical_path: accounting/04-CASH-FLOW-STATEMENT.md
backsource_ids: [mdloom-backfill:accounting:04-cash-flow-statement, git-history:accounting:04-cash-flow-statement]
concepts: [cash flow statement, operating activities, investing, financing, indirect method, free cash flow]
root_concepts: [cash flow statement]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Cash Flow Statement — Following the Money

## The Big Picture

The income statement is computed on accruals (file 05), so net income is *not* cash. The cash
flow statement (CFS) exists to **reconcile accrual profit to the actual movement of cash**
and to bucket that movement into three activities. Its bottom line is the change in the cash
balance — which must equal the difference between the cash line on this period's balance
sheet and last period's. That tie-out is the articulation property that makes the three
statements one system.

```
+--------------------------------------------------------------------------+
|              CASH FLOW STATEMENT  —  for a PERIOD                        |
|                                                                          |
|   +------------------------------------------------------------------+  |
|   | OPERATING (CFO)   cash from running the core business            |  |
|   |   Net income, +/- non-cash items, +/- working-capital changes    |  |
|   +------------------------------------------------------------------+  |
|                              +                                          |
|   +------------------------------------------------------------------+  |
|   | INVESTING (CFI)   cash for long-term assets                      |  |
|   |   - capex, - acquisitions, + asset sales, +/- securities         |  |
|   +------------------------------------------------------------------+  |
|                              +                                          |
|   +------------------------------------------------------------------+  |
|   | FINANCING (CFF)   cash with capital providers                    |  |
|   |   + borrow, - repay debt, + issue stock, - buybacks, - dividends |  |
|   +------------------------------------------------------------------+  |
|                              =                                          |
|   NET CHANGE IN CASH                                                     |
|   + Beginning cash                                                       |
|   = Ending cash    <-- MUST equal the cash line on the balance sheet    |
+--------------------------------------------------------------------------+
```

**Read it as three buckets summing to the cash delta.** Operating is the engine; investing is
the spend on the future; financing is dealings with lenders and owners.

---

## The Three Activities (what belongs where)

```
                        ALL CASH MOVEMENTS
                               |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
   +-----------+         +-----------+         +-----------+
   | OPERATING |         | INVESTING |         | FINANCING |
   +-----------+         +-----------+         +-----------+
   running the          buying/selling        raising/returning
   business             long-term assets      capital
   ---------            -----------------      ----------------
   collect from         buy PP&E (capex)       borrow / repay debt
    customers           buy/sell investments   issue / buy back stock
   pay suppliers        acquire companies      pay dividends
   pay employees        sell a division        (interest: usually CFO
   pay taxes                                    under GAAP)
   pay interest*
```

| Activity | Sign convention | Healthy pattern (mature firm) |
|----------|----------------|-------------------------------|
| **Operating (CFO)** | Inflow positive | Strongly positive — the engine works |
| **Investing (CFI)** | Outflow negative | Negative — investing in growth (capex) |
| **Financing (CFF)** | Either | Often negative — returning cash (dividends, buybacks, debt paydown) |

A textbook-healthy mature company shows **+CFO, −CFI, −CFF**: it generates cash, reinvests
some, and returns the rest. A startup often shows −CFO, −CFI, +CFF (burning cash, investing,
raising money). The *pattern* is diagnostic.

---

## Direct vs Indirect Method

There are two ways to present **operating** cash flow. Investing and financing are identical
under both.

```
   DIRECT METHOD                       INDIRECT METHOD
   (list actual cash flows)            (reconcile from net income)
   --------------------------          ----------------------------
   Cash from customers     1,050       Net income                 174
   Cash to suppliers        (600)      + Depreciation              60
   Cash to employees        (200)      + Stock comp                20
   Cash for interest         (40)      - Increase in AR           (50)
   Cash for taxes            (46)      + Increase in AP            30
   -----------------------------       - Increase in inventory    (40)
   CFO                       164       + Increase in def. revenue  25
                                       -----------------------------
                                       CFO                        219
   (different numbers above are        (this method dominates in
    illustrative of layout only)        practice — >95% of filers)
```

| | Direct | Indirect |
|--|--------|----------|
| Starts from | Actual cash receipts/payments | Net income |
| Readability | Intuitive (where cash came/went) | Requires understanding the reconciliation |
| Usage | Rare (extra disclosure burden) | Near-universal (GAAP & IFRS allow both) |
| Reconciliation to NI | Required as a supplement anyway | Built in |

Both standards *prefer* direct but *permit* indirect, and almost everyone files indirect
because it reuses numbers already on the income statement and balance sheet.

---

## The Indirect Method, Mechanically

This is the part worth understanding deeply, because it *is* the accrual-to-cash bridge. Two
kinds of adjustment turn net income into operating cash:

```
   NET INCOME (accrual)
      |
      | (1) Add back NON-CASH expenses
      |     + Depreciation & amortization   (expensed, no cash left)
      |     + Stock-based compensation       (expensed, no cash left)
      |     + Impairments / write-downs      (non-cash)
      |     +/- Deferred taxes               (timing, non-cash)
      |     - Gains on asset sales           (the cash is in INVESTING)
      |
      | (2) Adjust for WORKING-CAPITAL changes
      |     - Increase in AR        (sold but not yet collected)
      |     - Increase in inventory (cash tied up in stock)
      |     + Increase in AP        (received but not yet paid)
      |     + Increase in deferred revenue (collected, not yet earned)
      v
   OPERATING CASH FLOW (cash)
```

The rule of thumb for working capital:

```
   Asset goes UP   -> cash went OUT (SUBTRACT)    [AR up = uncollected]
   Asset goes DOWN -> cash came IN (ADD)
   Liab. goes UP   -> cash came IN (ADD)          [AP up = unpaid]
   Liab. goes DOWN -> cash went OUT (SUBTRACT)
```

**Bridge (TCS):** the indirect method is a *diff* between two accounting models. Net income is
the accrual model's output; CFO is the cash model's output; the adjustments are the per-line
reconciliation between the two replicas. Deferred revenue and AR are exactly the
eventual-consistency lag between "earned" and "settled."

---

## Worked Example — Net Income to Cash (it reconciles)

```
   GIVEN (from files 02-03):
     Net income                              174
     Depreciation expense                     60
     Stock-based compensation                 20
     Accounts receivable    rose by           50   (asset up  -> subtract)
     Inventory              rose by           40   (asset up  -> subtract)
     Accounts payable       rose by           30   (liab up   -> add)
     Deferred revenue       rose by           25   (liab up   -> add)

   OPERATING ACTIVITIES (indirect):
     Net income                              174
     + Depreciation                           60
     + Stock comp                             20
     - Increase in AR                        (50)
     - Increase in inventory                 (40)
     + Increase in AP                         30
     + Increase in deferred revenue           25
     ---------------------------------------------
     CFO                                      219

   INVESTING ACTIVITIES:
     Capex (bought equipment)               (150)
     ---------------------------------------------
     CFI                                    (150)

   FINANCING ACTIVITIES:
     Borrowed on note                        100
     Issued stock                              0
     Dividends paid                          (20)
     ---------------------------------------------
     CFF                                      80

   NET CHANGE IN CASH = 219 - 150 + 80    =  149
     + Beginning cash                         86
     = Ending cash                           235  <- equals balance-sheet cash
```

The ending cash (235) ties exactly to the cash line on the balance sheet (file 02). That
tie-out is the integrity check on the whole statement set — if it doesn't reconcile, there's
an error somewhere in the three statements.

---

## Free Cash Flow — The Number Owners Care About

GAAP doesn't define free cash flow, but it's the most-watched derived figure and the basis
for DCF valuation in `finance/`:

```
   FREE CASH FLOW (FCF) = Operating cash flow (CFO) - Capital expenditures

   From the example:  219 - 150 = 69
```

FCF is the cash left after keeping the business running and investing in it — available to
pay down debt, pay dividends, buy back stock, or accumulate. **Bridge to `finance/`:** the
DCF model discounts projected FCF; this is the input that connects accounting to valuation.

| Variant | Definition | Used for |
|---------|-----------|----------|
| FCF (to firm) | CFO − capex (sometimes + after-tax interest) | Enterprise valuation |
| FCF to equity | FCF − net debt repayment | Equity valuation |
| Unlevered FCF | EBIT(1−tax) + D&A − capex − ΔWC | DCF starting point |

---

## Why Cash Flow Catches Fraud the Income Statement Misses

Net income is the most *manipulable* number (file 09) — revenue recognition timing,
estimates, accruals. Cash is far harder to fake. A persistent gap where **net income grows
but CFO stagnates or falls** is a classic warning sign of aggressive revenue recognition or
channel stuffing. Analysts compute the **accruals ratio** = (Net income − CFO) / assets;
high values predict earnings quality problems. This is why the CFS is the auditor's and the
short-seller's favorite statement.

---

## Old World → New World Bridges

| Prior art | Cash flow concept |
|-----------|------------------|
| Reconciling two replicas / diff | Indirect method (accrual model vs cash model) |
| Eventual-consistency lag | AR / deferred revenue (earned vs settled gap) |
| Add-back of non-cash bookkeeping | Depreciation, stock comp, impairments |
| Capacity spend vs run cost | Investing (capex) vs operating (run the business) |
| Returning resources to the pool | Financing (dividends, buybacks, debt repayment) |
| End-to-end integrity checksum | Ending cash ties to balance-sheet cash line |
| Anomaly detection on a metric | NI-vs-CFO divergence (earnings-quality red flag) |

---

## Decision Cheat Sheet

| I want to know... | Look at |
|-------------------|---------|
| Does the core business actually generate cash? | Operating cash flow (CFO) |
| How much is being reinvested? | Investing (capex) |
| Is the firm raising or returning capital? | Financing (sign of CFF) |
| Cash available to owners after reinvestment | Free cash flow (CFO − capex) |
| Whether reported profit is "real" | NI vs CFO gap; accruals ratio |
| Is a startup's burn sustainable? | CFO + CFI vs cash on hand and runway |
| Input for a DCF valuation | Free cash flow (hand to `finance/`) |

---

## Common Confusion Points

### "Why add depreciation *back*? It's a real cost."

Depreciation is a real *expense* but not a *cash outflow this period* — the cash left when
the asset was bought (that's in investing, as capex, in the year of purchase). It was
subtracted to compute net income, so to get back to cash you add it back. You are undoing a
non-cash bookkeeping entry, not claiming depreciation is free.

### "Operating cash flow should equal net income"

Almost never. They differ by every non-cash item and every working-capital change. A growing
company building inventory and receivables routinely has CFO well *below* net income; a
declining one liquidating working capital can have CFO *above* it. The gap is informative,
not an error.

### "Negative investing cash flow is bad"

Usually the opposite — negative CFI means the firm is **buying** long-term assets (capex,
acquisitions), i.e. investing in its future. *Positive* CFI can be a warning: it may mean the
firm is selling off assets to raise cash.

### "Interest paid is a financing activity"

Under **US GAAP**, interest paid and received are classified in **operating** activities.
Under **IFRS**, the firm may classify interest paid in either operating or financing (and
interest received in operating or investing) — a real cross-standard difference that affects
reported CFO comparability (file 09).

### "Free cash flow is a GAAP line item"

No — FCF is not defined by GAAP or IFRS; it's a derived analyst figure (CFO − capex, with
variants). Read the definition any source uses; firms compute "adjusted FCF" with their own
add-backs, which can be self-serving.
