---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-ACCRUAL-VS-CASH.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:accrual-vs-cash
kind: guide
module: accounting
section: accounting
title: Accrual vs Cash - Event-Time vs Settlement-Time
status: source-custody
source_custody: partial
current_path: accounting/05-ACCRUAL-VS-CASH.md
canonical_path: accounting/05-ACCRUAL-VS-CASH.md
backsource_ids: [proof-backfill:accounting:05-accrual-vs-cash, git-history:accounting:05-accrual-vs-cash]
concepts: [accrual accounting, cash accounting, matching principle, deferrals, accruals, adjusting entries]
root_concepts: [accrual accounting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Accrual vs Cash — Event-Time vs Settlement-Time

## The Big Picture

There are two clocks an accounting system can run on. **Cash basis** records a transaction
when money moves. **Accrual basis** records it when the economic *event* occurs — the sale is
made, the cost is incurred — regardless of when cash settles. GAAP and IFRS require accrual
for any non-trivial entity, because cash basis misstates performance whenever timing of cash
and timing of activity diverge (which is always).

```
+--------------------------------------------------------------------------+
|             TWO CLOCKS FOR THE SAME TRANSACTION                          |
|                                                                          |
|   EVENT TIMELINE:                                                        |
|                                                                          |
|     Order      Deliver      Invoice      Customer pays                   |
|     placed     goods        sent         (60 days later)                 |
|       |          |            |               |                          |
|   ----+----------+------------+---------------+--------------> time       |
|                  ^                            ^                          |
|                  |                            |                          |
|         ACCRUAL recognizes here       CASH recognizes here              |
|         (revenue EARNED on delivery)  (revenue when CASH arrives)        |
|                                                                          |
|   ACCRUAL = event-time semantics   |   CASH = settlement-time semantics  |
+--------------------------------------------------------------------------+
```

**Bridge (TCS):** this is precisely the **event-time vs processing-time** distinction in
stream processing. Accrual processes by event time (when did the economic thing happen);
cash processes by arrival/settlement time. Accrual then needs **deferrals and accruals** as
the watermark/buffering machinery to align reality with the books at period boundaries.

---

## The Two Principles That Define Accrual

Accrual accounting rests on two recognition rules:

```
   +-----------------------------------------------------------------+
   |  REVENUE RECOGNITION:  recognize revenue when EARNED            |
   |    (obligation satisfied / control transferred — ASC 606),      |
   |    not when cash is received.                                   |
   +-----------------------------------------------------------------+
   |  MATCHING PRINCIPLE:   recognize expenses in the SAME period    |
   |    as the revenue they helped generate, not when cash is paid.  |
   +-----------------------------------------------------------------+
```

**Matching** is the deep idea: costs follow the revenue they produce. If you buy inventory in
March and sell it in June, the cost (COGS) hits June — matched to the sale — not March when
you paid for it. Depreciation is matching writ large: a machine bought once is expensed over
all the years it generates revenue.

```
   PAY CASH (March)              EARN REVENUE (June)
        |                              |
        |  cost parked as ASSET        |  cost released as EXPENSE
        |  (inventory / prepaid)       |  (COGS), MATCHED to revenue
        +------------------------------+
              the asset is a BUFFER that holds the cost
              until the matching revenue event fires
```

---

## The Four Timing Cases (the 2x2)

Every accrual adjustment is one of four cases, defined by whether cash leads or lags the
economic event. Two are **deferrals** (cash first, event later) and two are **accruals**
(event first, cash later).

```
                    |  CASH BEFORE event     |  CASH AFTER event
   -----------------+------------------------+------------------------
   REVENUE side     |  DEFERRED REVENUE      |  ACCRUED REVENUE
   (you earn)       |  (unearned)            |  (earned, unbilled)
                    |  got cash, owe service |  did work, awaiting cash
                    |  -> LIABILITY          |  -> ASSET (receivable)
   -----------------+------------------------+------------------------
   EXPENSE side     |  PREPAID EXPENSE       |  ACCRUED EXPENSE
   (you incur)      |  (deferred cost)       |  (payable)
                    |  paid ahead            |  used, not yet paid
                    |  -> ASSET              |  -> LIABILITY
```

| Case | Cash vs event | Created as | Example |
|------|--------------|-----------|---------|
| **Deferred revenue** | Cash before earning | Liability | Annual SaaS paid upfront |
| **Prepaid expense** | Cash before incurring | Asset | Insurance paid for the year |
| **Accrued revenue** | Earned before cash | Asset (receivable) | Work done, not yet invoiced |
| **Accrued expense** | Incurred before cash | Liability (payable) | Wages earned, paid next period |

```
   DEFERRALS  =  cash FIRST, recognition LATER   (buffer it on the BS)
   ACCRUALS   =  recognition FIRST, cash LATER    (record the receivable/payable)
```

---

## Adjusting Entries — Aligning the Books at Period End

At each period boundary, the books must be brought to accrual truth. **Adjusting entries**
are the period-end watermark flush: for every timing gap, move the right amount from buffer
to recognition. They never touch cash (cash already moved or hasn't yet); they always touch
one income-statement account and one balance-sheet account.

### Deferred revenue — release as earned

```
   At sale (Jan 1):  collected $1,200 for a 12-month service
     DR Cash                1,200
        CR Deferred revenue       1,200     (liability)

   Adjusting entry each month (earn 1/12):
     DR Deferred revenue      100
        CR Revenue                  100     (recognize as earned)
```

### Prepaid expense — expense as consumed

```
   At payment (Jan 1):  paid $1,200 for a year of insurance
     DR Prepaid insurance   1,200      (asset)
        CR Cash                    1,200

   Adjusting entry each month (consume 1/12):
     DR Insurance expense     100
        CR Prepaid insurance       100
```

### Accrued revenue — record the unbilled receivable

```
   Did $500 of consulting in December, will invoice in January:
     DR Accrued revenue (receivable)   500    (asset)
        CR Revenue                            500
   Next period when billed/collected, reverse the receivable.
```

### Accrued expense — record the unpaid obligation

```
   Employees earned $800 of wages in the last days of December,
   paid in January:
     DR Wages expense        800
        CR Wages payable           800       (liability)
```

Each adjusting entry preserves the invariant (`A = L + E`) and moves recognition to the
correct period. Without them, the income statement would lag or lead reality by the
cash-timing offset.

---

## Why Accrual ≠ Cash — A Worked Period

Same business, same events, one period — see how the two clocks report differently.

```
   EVENTS in Q1:
   - Delivered $1,000 of services; collected $600, $400 still owed (AR)
   - Collected $300 upfront for Q2 work (not yet earned -> deferred)
   - Incurred $500 of costs; paid $350, $150 still owed (AP)
   - Paid $240 for a 12-month insurance policy (only $60 is Q1's share)

                                CASH BASIS        ACCRUAL BASIS
   --------------------------   ----------        -------------
   Revenue                      600 + 300 = 900   1,000  (earned only)
   Expenses                     350 + 240 = 590   500 + 60 = 560
   --------------------------   ----------        -------------
   "Profit"                     310               440

   Balance-sheet residue (accrual only):
     Accounts receivable     +400   (earned, uncollected)
     Deferred revenue        +300   (collected, unearned)
     Accounts payable        +150   (incurred, unpaid)
     Prepaid insurance       +180   (paid, unconsumed)
```

Cash basis reports $310; accrual reports $440 — a $130 difference in the *same quarter* for
the *same activity*. Cash basis wrongly counts the $300 Q2 prepayment as Q1 income and
ignores the $400 earned-but-uncollected revenue. Accrual gives the economically faithful
picture; the **cash flow statement (file 04)** then reconciles accrual profit back to the
$310 of actual cash so you also see liquidity.

---

## When Cash Basis Is Acceptable

| Context | Basis | Why |
|---------|-------|-----|
| Public companies, audited entities | Accrual (required) | Faithful performance; GAAP/IFRS mandate |
| Large private firms (above thresholds) | Accrual (required) | Tax/reporting rules |
| Very small businesses, sole proprietors | Cash often allowed | Simplicity; tax cash-basis below size thresholds |
| Internal cash-management / treasury | Cash view used alongside | You still need to know real liquidity |

Even accrual-basis firms watch cash obsessively — accrual tells you if you're *profitable*,
cash tells you if you'll *survive*. Both are needed; that's why there are separate
statements.

---

## Old World → New World Bridges

| Prior art | Accrual concept |
|-----------|----------------|
| Event-time vs processing-time | Accrual (event-time) vs cash (settlement-time) |
| Watermarks / windowed aggregation | Period-end adjusting entries flush the timing buffer |
| Buffering events until trigger fires | Prepaid/deferred parked on the balance sheet |
| Eventual consistency (lagged settle) | AR / AP / deferred revenue (the earn-vs-settle gap) |
| Amortizing a one-time cost over uses | Matching (depreciation, prepaid consumption) |
| Reconciling two consistency models | Cash flow statement (accrual → cash, file 04) |
| Idempotent reversal at boundary | Reversing entries for accruals next period |

---

## Decision Cheat Sheet

| Situation | Treatment | Account created |
|-----------|-----------|-----------------|
| Collected cash before delivering | Defer | Deferred revenue (liability) |
| Paid cash before consuming | Defer | Prepaid expense (asset) |
| Earned revenue, not yet billed | Accrue | Accrued revenue (asset) |
| Incurred cost, not yet paid | Accrue | Accrued expense / payable (liability) |
| Bought a long-lived asset | Capitalize + depreciate | Asset → expense over life (matching) |
| Want true profitability | Read accrual income statement | — |
| Want survival / liquidity | Read cash flow statement (file 04) | — |

---

## Common Confusion Points

### "Accrual accounting is just a more complicated way to track cash"

No — it answers a *different* question. Cash basis answers "did money move?"; accrual answers
"did we create economic value this period?" They genuinely disagree (the $310 vs $440 above).
Accrual is required precisely because cash timing distorts performance.

### "If we're profitable, we have the cash"

The single most dangerous misconception, and the reason businesses fail while profitable.
Profit can be locked in receivables and inventory; you can owe suppliers cash you haven't
collected from customers. This is why the cash flow statement (file 04) exists and why
working capital (file 02) matters.

### "Deferred revenue and accrued revenue are the same"

Opposite cases. **Deferred** revenue = cash *before* earning → a liability (you owe service).
**Accrued** revenue = earning *before* cash → an asset (you're owed money). One is on the
right side of the balance sheet, the other on the left.

### "Prepaid expense is an expense"

It starts as an **asset** (you bought future benefit) and is *converted* to expense as
consumed via adjusting entries. Prepaying a year of insurance is buying an asset that
amortizes monthly — it doesn't all hit the income statement on the payment date.

### "Adjusting entries move cash around"

They never touch cash. Cash already moved (deferrals) or hasn't yet (accruals). Adjusting
entries move amounts between a balance-sheet buffer and an income-statement recognition
account — they realign *timing*, not money.
