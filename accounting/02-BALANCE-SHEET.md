---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:balance-sheet
kind: guide
module: accounting
section: accounting
title: The Balance Sheet - State Snapshot
status: source-custody
source_custody: partial
current_path: accounting/02-BALANCE-SHEET.md
canonical_path: accounting/02-BALANCE-SHEET.md
backsource_ids: [proof-backfill:accounting:02-balance-sheet, git-history:accounting:02-balance-sheet]
concepts: [balance sheet, assets, liabilities, equity, working capital, classification]
root_concepts: [balance sheet]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Balance Sheet — State Snapshot

## The Big Picture

The balance sheet is a **snapshot of the firm's state at one instant** — "as of Dec 31."
It is the accounting equation made literal: everything the firm controls (assets) equals the
claims against it (liabilities + equity). It is the **persistent state** of the ledger; the
income and cash-flow statements are the per-period deltas that move it from one snapshot to
the next.

```
+--------------------------------------------------------------------------+
|                   BALANCE SHEET  —  as of a POINT IN TIME                |
|                                                                          |
|         ASSETS              =        LIABILITIES   +   EQUITY            |
|       (what we control)            (creditor claims)  (owner claims)     |
|                                                                          |
|   +--------------------+        +--------------------------------------+ |
|   | CURRENT (<1 yr)    |        | CURRENT LIABILITIES (<1 yr)          | |
|   |  Cash              |        |  Accounts payable                    | |
|   |  Marketable secs   |        |  Accrued expenses                    | |
|   |  Accounts recv.    |        |  Deferred revenue                    | |
|   |  Inventory         |        |  Current portion of LT debt          | |
|   |  Prepaid expenses  |        +--------------------------------------+ |
|   +--------------------+        | NON-CURRENT LIABILITIES (>1 yr)      | |
|   | NON-CURRENT (>1 yr)|        |  Long-term debt / bonds              | |
|   |  PP&E (net)        |        |  Deferred tax liability              | |
|   |  Intangibles       |        |  Pension obligations                 | |
|   |  Goodwill          |        +--------------------------------------+ |
|   |  LT investments    |        | EQUITY                               | |
|   |                    |        |  Common stock + APIC (contributed)   | |
|   |                    |        |  Retained earnings (accumulated)     | |
|   |                    |        |  Treasury stock (contra, subtracts)  | |
|   |                    |        |  Accum. other comprehensive income   | |
|   +--------------------+        +--------------------------------------+ |
|                                                                          |
|        TOTAL ASSETS         ==      TOTAL LIAB. + TOTAL EQUITY            |
|        (these two numbers are EQUAL — that is why it "balances")          |
+--------------------------------------------------------------------------+
```

**Read it as two columns that must match:** the left is resources; the right is who funded
them. The bottom-line totals are identical by construction (the invariant from file 01).

---

## The Three Sections in Order

### Assets — resources controlled, ordered by liquidity

Assets are listed **most-liquid first**. The cut at one year (or one operating cycle, if
longer) splits current from non-current.

| Asset | What it is | Current? | Measurement basis |
|-------|-----------|----------|-------------------|
| Cash & equivalents | Money + <90-day instruments | Current | Face value |
| Marketable securities | Tradable short-term investments | Current | Fair value |
| Accounts receivable | Money owed by customers | Current | Net of allowance |
| Inventory | Goods to sell (raw/WIP/finished) | Current | Lower of cost or market |
| Prepaid expenses | Paid-ahead costs (insurance, rent) | Current | Unamortized cost |
| PP&E | Property, plant, equipment | Non-current | Cost − accum. depreciation |
| Intangibles | Patents, software, licenses | Non-current | Cost − amortization |
| Goodwill | Premium paid in acquisitions | Non-current | Cost − impairment (no amort.) |
| Long-term investments | Strategic stakes, held bonds | Non-current | Varies |

**Key measurement principle: historical cost, not market value.** PP&E sits at what you
paid minus depreciation, even if the building is now worth triple. Only certain financial
instruments are marked to fair value. This is the central limitation of the balance sheet
(see Common Confusion Points).

### Liabilities — claims by creditors, ordered by maturity

| Liability | What it is | Current? |
|-----------|-----------|----------|
| Accounts payable | Owed to suppliers | Current |
| Accrued expenses | Incurred, not yet paid (wages, interest) | Current |
| Deferred / unearned revenue | Cash taken for work not yet done | Current (usually) |
| Current portion of LT debt | Principal due within 12 months | Current |
| Long-term debt / bonds | Borrowings due >1 yr | Non-current |
| Deferred tax liability | Tax timing differences | Non-current |
| Pension / lease obligations | Long-term promises | Non-current |

**Deferred revenue is a liability, not revenue** — a counterintuitive but critical point for
a software business. Cash received for a not-yet-delivered annual license is an *obligation*
to deliver, so it sits on the right side until earned (file 05).

### Equity — the residual owner claim

Equity = Assets − Liabilities. It is a **residual**, not a primary measurement. Its parts:

```
   EQUITY
   +-- Contributed capital
   |     +-- Common stock (par value)
   |     +-- Additional paid-in capital (APIC)  (over par)
   +-- Retained earnings   (cumulative net income - cumulative dividends)
   +-- Treasury stock      (contra: shares bought back, SUBTRACTS)
   +-- Accumulated other comprehensive income (AOCI)
         (FX translation, certain unrealized gains/losses)
```

**Retained earnings is the bridge to the income statement.** Each period's net income flows
in; dividends flow out. It is the running accumulator of all profit ever kept in the
business.

---

## Classification: Why Current vs Non-Current Matters

The current/non-current split exists to answer the solvency question: *can the firm pay
what's due soon with what's liquid soon?* Two derived figures fall straight out of it.

```
   WORKING CAPITAL  =  Current Assets  -  Current Liabilities
                       (cushion of liquidity)

   CURRENT RATIO    =  Current Assets  /  Current Liabilities
                       (>1 generally healthy; analyzed in file 08)
```

```
   CURRENT ASSETS            CURRENT LIABILITIES
   +-----------------+       +-----------------+
   | Cash      40    |       | Payables    30  |
   | AR        50    |       | Accrued     20  |
   | Inventory 30    |       | Def. rev.   10  |
   +-----------------+       +-----------------+
   total     120            total        60
                |                  |
                +-- Working capital = 120 - 60 = 60
                +-- Current ratio   = 120 / 60 = 2.0
```

---

## Worked Example — Building a Balance Sheet (it balances)

Trace a startup's first year of transactions, then assemble the balance sheet.

```
   TRANSACTIONS (Year 1):
   T1  Founders invest $200 cash for stock
   T2  Borrow $100 on a 3-year note
   T3  Buy equipment for $150 cash
   T4  Buy inventory for $80 on account (payable)
   T5  Sell half the inventory ($40 cost) for $90 cash; recognize COGS
   T6  Pay $30 of the payable
   T7  Record $15 depreciation on equipment
   T8  Customer prepays $25 for next year's service (deferred revenue)
```

Effect on the equation (every line keeps `A = L + E`):

```
   #    ASSETS                          =  LIABILITIES        +  EQUITY
   T1   Cash +200                       =                     +  Stock +200
   T2   Cash +100                       =  Note +100          +
   T3   Cash -150, Equip +150           =                     +
   T4   Inventory +80                   =  Payable +80        +
   T5   Cash +90, Inventory -40         =                     +  RE +50 (90-40)
   T6   Cash -30                        =  Payable -30        +
   T7   Equip -15 (accum deprec)        =                     +  RE -15 (deprec exp)
   T8   Cash +25                        =  Def.Rev +25        +
```

Roll up the ledger balances:

```
   Cash:      200+100-150+90-30+25            = 235
   Inventory: 80-40                           = 40
   Equipment: 150 gross, less 15 accum dep    = 135 net
   ----                                         ----
   TOTAL ASSETS                                 410

   Note payable                               = 100
   Accounts payable: 80-30                    = 50
   Deferred revenue                           = 25
   ----                                         ----
   TOTAL LIABILITIES                            175

   Common stock                               = 200
   Retained earnings: +50 -15                 = 35
   ----                                         ----
   TOTAL EQUITY                                 235
```

Assemble and check:

```
   BALANCE SHEET — Dec 31, Year 1
   ASSETS                          LIABILITIES & EQUITY
   ------------------------        ------------------------
   Current assets                  Current liabilities
     Cash             235            Accounts payable    50
     Inventory         40            Deferred revenue    25
                       ---                               ---
     Total current    275            Total current       75
   Non-current                     Non-current liab.
     Equipment (gross)150            Note payable       100
     Less accum dep.  (15)         ------------------------
     Equipment (net)  135          TOTAL LIABILITIES    175
                       ---
                                   Equity
                                     Common stock       200
                                     Retained earnings   35
                                   ------------------------
                                   TOTAL EQUITY         235
   ------------------------        ------------------------
   TOTAL ASSETS       410          TOTAL L + E          410
                      ===                               ===
                          410 == 410   IT BALANCES
```

The check is not luck — double-entry *guarantees* it. If it didn't balance, you'd have a
posting error (file 01).

---

## GAAP vs IFRS on the Balance Sheet

Real, citable differences that change what you see:

| Item | US GAAP | IFRS |
|------|---------|------|
| PP&E measurement | Historical cost only | Cost **or** revaluation model (upward to fair value allowed) |
| Inventory costing | FIFO, LIFO, weighted-avg permitted | **LIFO prohibited**; FIFO/weighted-avg only |
| Development costs | Expensed (most R&D) | Capitalized if criteria met (IAS 38) |
| Ordering | Often current-first (most liquid) | Often non-current-first (IAS 1 permits either) |
| Reversal of impairments | Generally prohibited | Permitted (except goodwill) |
| Terminology | "Balance Sheet" | "Statement of Financial Position" |

The LIFO point has cash-tax consequences (file 03/09): LIFO lowers taxable income when
prices rise, so US firms use it for the tax shield — an option IFRS firms simply do not have.

---

## Old World → New World Bridges

| Prior art | Balance sheet concept |
|-----------|----------------------|
| Persistent state / heap snapshot | The balance sheet itself (state at an instant) |
| Per-frame delta applied to state | Income statement / cash flow move snapshot→snapshot |
| Foreign-key claims on a resource | Liabilities + equity (claims on assets) |
| Residual / computed column | Equity (= assets − liabilities) |
| Soft delete / tombstone | Contra-accounts (accum. deprec., treasury stock) |
| Liquidity tiers (hot/warm/cold storage) | Current vs non-current ordering |
| Deferred obligation / outstanding promise | Deferred revenue (liability until earned) |

---

## Decision Cheat Sheet

| I need to know... | Look at |
|-------------------|---------|
| Can the firm cover near-term bills? | Working capital, current ratio |
| How much is funded by debt vs owners? | Total liabilities vs total equity (leverage, file 08) |
| How much cumulative profit was kept? | Retained earnings |
| Is there acquisition premium on the books? | Goodwill (and its impairment risk) |
| Did they take customer cash in advance? | Deferred revenue (an obligation, not income) |
| Is reported asset value near market? | Usually no — historical cost (use `finance/` for valuation) |
| Buybacks reducing share count? | Treasury stock (contra-equity) |

---

## Common Confusion Points

### "The balance sheet shows what the company is worth"

It shows **book value at historical cost**, not market value. Book equity is an accounting
residual. Market cap diverges because intangibles (brand, talent, network effects), growth
expectations, and internally-generated goodwill are *not on the balance sheet*. Valuation is
a `finance/` exercise, not a balance-sheet read.

### "Retained earnings is a pile of cash"

No. Retained earnings is on the **right** side (a claim), not the left (a resource). Profits
kept in the business were spent on inventory, equipment, paying down debt — they are not
sitting in cash. A firm can have huge retained earnings and almost no cash.

### "Deferred revenue is good news — it's revenue"

It is a **liability** — an obligation to deliver goods/services you've already been paid for.
It becomes revenue only as you fulfill it (file 05). Growing deferred revenue is often a
healthy signal for subscription businesses, but it sits on the right side until earned.

### "Goodwill is an asset I can rely on"

Goodwill is the premium paid over fair value of net assets in an acquisition. Under both GAAP
and IFRS it is **not amortized** but **tested for impairment** — and impairments are large,
lumpy, non-cash writeoffs that signal an acquisition went bad. Treat it as a flag, not a
fortress.

### "If it doesn't balance, pick whichever total looks right"

Never. An imbalance means a real posting error upstream (file 01) — a one-sided entry, a
transposition, a missing line. Find and fix the entry; do not plug the difference.
