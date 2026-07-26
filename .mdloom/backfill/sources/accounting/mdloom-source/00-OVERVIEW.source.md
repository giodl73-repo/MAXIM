---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:overview
kind: guide
module: accounting
section: accounting
title: Accounting - Field Map and Orientation
status: source-custody
source_custody: partial
current_path: accounting/00-OVERVIEW.md
canonical_path: accounting/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:accounting:00-overview, git-history:accounting:00-overview]
concepts: [accounting, ledger, financial statements, double-entry, reporting]
root_concepts: [accounting]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Accounting — Field Map & Orientation

## The Big Picture

Accounting is a **formal system for recording economic events and producing a periodic,
auditable summary of them**. Strip away the vocabulary and it is a ledger with one
invariant — `Assets = Liabilities + Equity` — that must hold after *every* mutation. Every
other rule (debits, accruals, the three statements, GAAP) is machinery for keeping that
invariant true while the underlying reality is messy, continuous, and contested.

For a TCS reader the cleanest mental model: the **general ledger is an append-only log**,
each **journal entry is a transaction** in the database sense (atomic, balanced), the
**trial balance is a consistency check** (does the log replay to a consistent state?), and
**reconciliation is cross-replica agreement** (does our cash ledger match the bank's?).

```
+--------------------------------------------------------------------------+
|                      THE ACCOUNTING PIPELINE                             |
|                                                                          |
|  REALITY            CAPTURE          STORE          SUMMARIZE     ANALYZE |
|  -------            -------          -----          ---------     ------- |
|  Economic     -->   Journal    -->   General  -->   Financial -->  Ratios |
|  events             entries          Ledger         Statements     &      |
|  (sale, pay,        (debit =         (append-       (3 reports)    trends |
|   borrow,            credit)          only log,                           |
|   depreciate)                         per account)                       |
|                                                                          |
|  +----------+    +-----------+    +-----------+   +-----------+  +------+ |
|  | source   |    |  DR / CR  |    | T-accounts|   |  Balance  |  | Liq. | |
|  | document |--->| balanced  |--->| trial     |-->|  Income   |->| Lev. | |
|  | (invoice,|    | entry     |    | balance   |   |  Cash Flow|  | Prof.| |
|  |  receipt)|    | (atomic)  |    | (consist- |   |  (+notes) |  | Eff. | |
|  +----------+    +-----------+    |  ency chk)|   +-----------+  +------+ |
|                                   +-----------+                          |
|                                                                          |
|  INVARIANT enforced at every step:  Assets = Liabilities + Equity        |
+--------------------------------------------------------------------------+
```

**Read this left-to-right**: messy reality is captured as balanced journal entries, posted
to the ledger, summarized into three statements, and analyzed into ratios. The invariant
holds end-to-end. The rest of this directory drills into each stage.

---

## The Two Audiences (and Two Accountings)

The single biggest orientation point: accounting splits by *who reads the output*.

```
                          ACCOUNTING
                              |
            +-----------------+------------------+
            |                                    |
            v                                    v
   +------------------+                +------------------+
   | FINANCIAL ACCT.  |                | MANAGERIAL ACCT. |
   | (external)       |                | (internal)       |
   +------------------+                +------------------+
   | Audience:        |                | Audience:        |
   |  investors,      |                |  managers,       |
   |  lenders, IRS,   |                |  the board, you  |
   |  regulators      |                |                  |
   | Rules: GAAP/IFRS |                | Rules: none —    |
   |  (mandatory)     |                |  whatever helps  |
   | Cadence: quarter |                | Cadence: daily / |
   |  / year          |                |  whenever        |
   | Output: 3 state- |                | Output: budgets, |
   |  ments, audited  |                |  variances,      |
   | Focus: the past, |                |  unit costs      |
   |  whole firm      |                | Focus: future,   |
   |                  |                |  per product/    |
   |                  |                |  segment         |
   +------------------+                +------------------+
   Files 01-05, 09                     Files 06-08
```

Financial accounting is **standardized and adversarial** — it is consumed by people with
money at stake, so it is rule-bound (GAAP/IFRS) and audited. Managerial accounting is
**private and pragmatic** — no external rules, optimized for decisions you actually have to
make (price this product? close this plant? buy or build?). Cost accounting (file 06) is
the measurement engine that feeds managerial decisions.

---

## The Five Account Types (the type system)

Every account in the ledger is exactly one of five types. This is the *type system* of
accounting, and it determines how debits and credits behave (file 01).

```
                    ACCOUNTING EQUATION
       Assets   =   Liabilities   +   Equity
         |              |               |
         |              |               +-- expanded by ops:
         |              |                   Equity = Contributed
         |              |                            + Retained Earnings
         |              |                   Retained = Revenue - Expenses
         |              |                              - Dividends
         v              v                   |            |
   +-----------+  +-----------+        +----------+ +----------+
   |  ASSETS   |  | LIABILITY |        | REVENUE  | | EXPENSE  |
   +-----------+  +-----------+        +----------+ +----------+
   | cash      |  | payables  |        | sales    | | COGS     |
   | AR        |  | debt      |        | interest | | salaries |
   | inventory |  | deferred  |        |  income  | | rent     |
   | PP&E      |  |  revenue  |        | (other)  | | deprec.  |
   | goodwill  |  | accruals  |        +----------+ +----------+
   +-----------+  +-----------+        (raise equity)(lower equity)
   normal: DR     normal: CR           normal: CR    normal: DR
```

The expansion is the key insight: **Revenue and Expense are temporary sub-accounts of
Equity**. They accumulate during a period and "close" into Retained Earnings at period end
(file 03). The income statement is just the per-period delta in equity *excluding* owner
transactions (investments and dividends).

---

## The Three Statements (and what each answers)

| Statement | Question it answers | Time model | Invariant tie |
|-----------|--------------------|--------|---------------|
| **Balance Sheet** | *What do we own and owe — right now?* | Snapshot (point in time) | `A = L + E` literally |
| **Income Statement** | *Did we make money this period?* | Flow (over a period) | Net income → Retained Earnings |
| **Cash Flow Statement** | *Where did the cash actually go?* | Flow (over a period) | Δ Cash on balance sheet |

```
   BALANCE SHEET (Dec 31, 2025)        BALANCE SHEET (Dec 31, 2026)
   +----------------------+            +----------------------+
   | Assets = L + Equity  |            | Assets = L + Equity  |
   +----------------------+            +----------------------+
              |                                   ^
              |   the period 2026 happens         |
              |                                   |
              v                                   |
   +-------------------------+    +-------------------------+
   | INCOME STATEMENT 2026   |    | CASH FLOW 2026          |
   | Revenue - Expenses      |    | Operating + Investing   |
   |  = Net Income           |    |  + Financing = Δ Cash   |
   +-------------------------+    +-------------------------+
        |                                  |
        +-- flows into Retained Earnings --+-- flows into Cash line
                    (part of Equity)            (an Asset)
```

The two flow statements *bridge* the two snapshots. Net income flows into equity; net cash
change flows into the cash asset. This articulation — the statements tie together
arithmetically — is the audit-grade property of the system (file 04, file 09).

---

## Old World → New World Bridges

The learner has deep systems intuition. Accounting maps onto it cleanly.

| Systems / data concept | Accounting analog |
|------------------------|-------------------|
| Append-only event log | General ledger (you never delete; you post a reversing entry) |
| ACID transaction (atomic, balanced) | Journal entry (total debits = total credits, all-or-nothing) |
| Database invariant / constraint | `Assets = Liabilities + Equity` |
| Materialized view over the log | Trial balance / financial statements |
| Replica reconciliation / consensus | Bank reconciliation, intercompany elimination |
| Eventual consistency vs strong | Cash-basis (lagged) vs accrual-basis (recognize at event time) |
| Schema / type system | The five account types and their normal balances |
| Audit log / immutability for compliance | SOX 404 controls, no-erasure rule, audit trail |
| Idempotent compensating transaction | Reversing/correcting entry (never edit a posted entry) |
| Soft delete vs hard delete | Contra-accounts (accumulated depreciation, allowance for doubtful accounts) |

The accrual-vs-cash distinction (file 05) is the **eventual-consistency vs
event-time-semantics** debate in disguise: cash accounting recognizes when money settles
(like waiting for the write to commit on every node); accrual recognizes at the moment the
economic event occurs (event-time processing), then reconciles to cash later.

---

## How a Single Transaction Propagates

One sale touches every layer. This is the worked spine the rest of the directory expands.

```
EVENT: Sell software license for $1,000 cash; your cost to deliver was $300.

STEP 1 — Journal entry (two entries, each balanced):
   (a) DR Cash            1,000
          CR  Revenue           1,000      <- recognize the sale
   (b) DR COGS              300
          CR  Inventory          300       <- match the cost

STEP 2 — Post to ledger (append to each account's log):
   Cash:      +1,000     Revenue:  +1,000
   Inventory:   -300     COGS:       +300

STEP 3 — Trial balance: total DR (1,300) = total CR (1,300)  [consistency OK]

STEP 4 — Statements:
   Income Stmt:   Revenue 1,000 - COGS 300 = Gross profit 700
   Balance Sheet: Cash +1,000, Inventory -300 (assets net +700)
                  Retained Earnings +700 (equity)         [A = L + E holds]
   Cash Flow:     Operating cash +1,000

STEP 5 — Analysis:
   Gross margin = 700 / 1,000 = 70%
```

Invariant check at STEP 4: assets rose by net +700 ($1,000 cash in, $300 inventory out);
equity rose by +700 (retained earnings). Liabilities unchanged. `A = L + E` preserved.

---

## The Directory Map

```
accounting/
|
+-- 00-OVERVIEW.md ............ you are here (the pipeline + invariant)
|
+-- THE FORMAL SYSTEM
|   +-- 01-DOUBLE-ENTRY.md .... equation, DR/CR, journal->ledger->trial balance
|
+-- THE THREE STATEMENTS
|   +-- 02-BALANCE-SHEET.md ... A=L+E, classification, worked example
|   +-- 03-INCOME-STATEMENT.md  revenue recognition, COGS, margins, EPS
|   +-- 04-CASH-FLOW-STATEMENT  operating/investing/financing, indirect method
|
+-- THE TIMING ENGINE
|   +-- 05-ACCRUAL-VS-CASH.md . matching, deferrals/accruals, why they diverge
|
+-- MANAGERIAL (internal)
|   +-- 06-COST-ACCOUNTING.md . fixed/variable, contribution, break-even, ABC
|   +-- 07-MANAGERIAL-ACCT.md . budgeting, variance, transfer pricing, decisions
|
+-- ANALYSIS & ASSURANCE
    +-- 08-FINANCIAL-ANALYSIS.md  liquidity/leverage/profitability/efficiency, DuPont
    +-- 09-AUDIT-AND-CONTROLS.md  internal controls, SOX, GAAP vs IFRS, manipulation
```

**Cross-directory:** `finance/` consumes these statements as valuation inputs (DCF, ratio
screens); `economics/` supplies the theory under depreciation (capital) and transfer
pricing (internal markets); `behavioral-economics/` explains *why* managers manipulate the
numbers (earnings management, anchoring, escalation of commitment).

---

## Decision Cheat Sheet

| I want to know... | Read | Statement / tool |
|---|---|---|
| How the whole system stays consistent | 01 | Double-entry, trial balance |
| What we own and owe right now | 02 | Balance sheet |
| Whether we were profitable this period | 03 | Income statement |
| Where the cash actually went | 04 | Cash flow statement |
| Why profit ≠ cash in the bank | 05 | Accrual vs cash |
| What it costs to make one more unit | 06 | Contribution margin, variable cost |
| Whether to make-or-buy, keep-or-drop | 06, 07 | Relevant costs, contribution |
| Whether the plant beat its budget | 07 | Variance analysis |
| How healthy / leveraged the firm is | 08 | Ratios, DuPont |
| Whether the numbers can be trusted | 09 | Internal controls, audit, GAAP/IFRS |

---

## Common Confusion Points

### "Profit and cash are the same thing"

They are not, and the gap is the entire point of file 05. A firm can be highly profitable
and still go bankrupt (it sold on credit and ran out of cash to pay suppliers), or cash-rich
and unprofitable (it took a big customer deposit for work not yet done). The cash flow
statement (file 04) exists precisely to reconcile the two.

### "Debits are good / increases and credits are bad / decreases"

False — debit and credit are just **left and right**, with no inherent sign. A debit
*increases* an asset but *decreases* a liability. Whether a debit is "good" depends entirely
on the account type (file 01). Drop the everyday-banking intuition entirely; in your bank
statement "credit" means money in because the bank's books mirror yours — your deposit is
the bank's liability to you.

### "GAAP and IFRS are basically the same"

Mostly convergent, but with real, specific differences that change reported numbers:
inventory (IFRS bans LIFO; US GAAP permits it), development costs (IFRS capitalizes
qualifying ones; US GAAP expenses most R&D), asset revaluation (IFRS allows upward
revaluation of PP&E; US GAAP is historical-cost only), and lease/impairment mechanics.
File 09 enumerates the ones that matter.

### "The balance sheet tells me what the company is worth"

No. The balance sheet is at **historical cost** (mostly), not market value. Book equity is
an accounting residual, not a valuation. A company's market cap routinely differs from book
equity by multiples — that gap is intangibles, growth expectations, and the limits of
historical-cost accounting. Valuation lives in `finance/`, not here.
