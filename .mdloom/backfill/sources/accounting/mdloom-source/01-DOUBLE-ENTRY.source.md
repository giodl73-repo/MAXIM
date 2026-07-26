---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-DOUBLE-ENTRY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:double-entry
kind: guide
module: accounting
section: accounting
title: Double-Entry Bookkeeping - The Ledger Invariant
status: source-custody
source_custody: partial
current_path: accounting/01-DOUBLE-ENTRY.md
canonical_path: accounting/01-DOUBLE-ENTRY.md
backsource_ids: [mdloom-backfill:accounting:01-double-entry, git-history:accounting:01-double-entry]
concepts: [double-entry, accounting equation, debits, credits, journal, ledger, trial balance]
root_concepts: [double-entry bookkeeping]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Double-Entry Bookkeeping — The Ledger Invariant

## The Big Picture

Double-entry is a 500-year-old (Pacioli, 1494) error-detecting code for a ledger. The whole
system is built to keep one equation true after every recorded event:

```
+-------------------------------------------------------------------------+
|                       THE FUNDAMENTAL INVARIANT                         |
|                                                                         |
|              ASSETS  =  LIABILITIES  +  EQUITY                          |
|              (own)      (owe others)    (owe owners)                    |
|                                                                         |
|   Every transaction is a balanced mutation: it changes >=2 accounts     |
|   such that the equation STILL holds afterward.                         |
|                                                                         |
|   total DEBITS posted  ==  total CREDITS posted   (always, forever)     |
+-------------------------------------------------------------------------+
                                  |
          +-----------------------+------------------------+
          |                       |                        |
          v                       v                        v
   +-------------+        +---------------+        +----------------+
   |  JOURNAL    |  -->   |   LEDGER      |  -->   | TRIAL BALANCE  |
   | (the log)   | post   | (per-account  | sum    | (consistency   |
   | chronolog.  |        |  T-accounts)  |        |  check)        |
   | balanced    |        | running bal.  |        | DR total ==    |
   | entries     |        | per account   |        |  CR total      |
   +-------------+        +---------------+        +----------------+
```

**Read top-to-bottom:** the invariant constrains every entry; entries are appended to the
journal (the log); the journal is posted into per-account ledgers (T-accounts); the trial
balance sums all ledger balances and verifies debits = credits. If it doesn't balance, you
have a bug, and you find it before producing statements.

---

## Why Two Entries? The Error-Detecting Code View

A single-entry system (a checkbook register) records *one* number per event. There is no
internal check: a typo just produces a wrong total and nobody knows.

Double-entry records every event as **at least two entries that must sum to zero** (debits
positive, credits negative). This is a parity / checksum: if the two sides don't match, the
system is provably inconsistent. It does not catch *all* errors (a correctly-balanced entry
to the wrong account still balances), but it catches every transposition, omission, and
one-sided slip — the most common ones.

```
   Single-entry (no check):          Double-entry (self-checking):
   +------------------+              +----------------------------------+
   | -500  rent paid  |              | DR Rent Expense  500             |
   +------------------+              |    CR Cash            500        |
   one number, trust me             | check: 500 == 500  OK            |
                                     +----------------------------------+
```

**Bridge (TCS):** this is exactly a balanced-transaction constraint with an invariant
checked at commit. The journal is your write-ahead log; posting is applying the log to
state; the trial balance is replaying the log and asserting the invariant.

---

## Debits and Credits: Drop Your Intuition

Debit (DR) and credit (CR) are **left** and **right**. That is *all they mean*. They carry
no inherent good/bad or increase/decrease sense. The sign depends on the account type.

```
                 A T-ACCOUNT (any account)
              +---------------------------+
              |   account name            |
              +-------------+-------------+
              |   DEBIT     |   CREDIT    |
              |   (left)    |   (right)   |
              +-------------+-------------+
```

The rule that ties type to direction comes straight from the equation. Assets are on the
left of `A = L + E`; liabilities and equity on the right. **Left-side accounts increase with
debits; right-side accounts increase with credits.**

```
        A      =      L     +      E
   +---------+   +---------+   +---------+
   | DR | CR |   | DR | CR |   | DR | CR |
   | +  | -  |   | -  | +  |   | -  | +  |
   +---------+   +---------+   +---------+
   normal: DR    normal: CR    normal: CR
```

Now extend to the temporary accounts. Revenue *increases* equity, so it behaves like equity
(credit increases it). Expenses and dividends *decrease* equity, so they behave oppositely
(debit increases them).

### The full debit/credit table — memorize this one table

| Account type | Normal balance | Debit does | Credit does | Lives on statement |
|--------------|---------------|------------|-------------|--------------------|
| **Asset** | Debit | Increase | Decrease | Balance sheet |
| **Liability** | Credit | Decrease | Increase | Balance sheet |
| **Equity** (contributed, retained) | Credit | Decrease | Increase | Balance sheet |
| **Revenue** | Credit | Decrease | Increase | Income statement |
| **Expense** | Debit | Increase | Decrease | Income statement |
| **Dividends / Draws** | Debit | Increase | Decrease | Equity (contra) |
| **Contra-asset** (accum. deprec., allowance) | Credit | Decrease | Increase | Balance sheet (subtracts) |
| **Contra-revenue** (returns, discounts) | Debit | Increase | Decrease | Income statement (subtracts) |

Mnemonic that actually encodes the equation, not folklore: **DEAD CLIC** —
**D**ebits increase **E**xpenses, **A**ssets, **D**ividends; **C**redits increase
**L**iabilities, **I**ncome (revenue), **C**apital (equity).

```
   D-E-A-D            C-L-I-C
   Debit increases    Credit increases
   Expenses           Liabilities
   Assets             Income (revenue)
   Dividends          Capital (equity)
```

---

## The Expanded Accounting Equation

The five types collapse back into the master equation. Revenue/expense/dividends are
temporary windows onto equity:

```
  ASSETS = LIABILITIES + EQUITY
                            |
   EQUITY = Contributed Capital + Retained Earnings
                                       |
   Retained Earnings(end) = RE(begin) + Net Income - Dividends
                                              |
   Net Income = Revenue - Expenses
                                       |
  ASSETS = LIABILITIES
         + Contributed Capital
         + Beginning Retained Earnings
         + Revenue - Expenses - Dividends
```

Rearranged so every term is on a side where its *normal balance* keeps it positive:

```
   ASSETS + EXPENSES + DIVIDENDS   =   LIABILITIES + EQUITY + REVENUE
   \________ normal DEBIT ________/     \________ normal CREDIT _______/
```

This is why a trial balance balances: every debit-normal account is on the left, every
credit-normal account on the right, and the equation forces equality.

---

## The Journal: The Append-Only Log

A journal entry has a date, the accounts touched, the debit/credit amounts, and (good
practice) a memo. **Debits are listed first and left-aligned; credits indented.** The entry
is atomic — you post all lines or none.

```
   2026-03-14   DR  Equipment            10,000
                    CR  Cash                       4,000
                    CR  Notes Payable              6,000
                (Bought a server: $4k cash down, $6k financed)

   check:  debits 10,000  ==  credits 10,000   OK
```

Note this is a **compound entry** (more than two lines) — perfectly legal, as long as total
DR = total CR. The rule is never "exactly one debit and one credit"; it is "sum of debits =
sum of credits."

**No-erasure rule (immutability):** you never edit or delete a posted entry. To fix a
mistake you post a **reversing entry** (a compensating transaction), then the correct one.
This preserves the audit trail — the same reason event-sourced systems never mutate the log.

```
   Wrong:  edit the bad entry in place        <- destroys audit trail
   Right:  post reversal + post correction     <- full history retained
```

---

## The Ledger: Posting to T-Accounts

Posting takes each journal line and appends it to that account's T-account (its
per-account view of the log). The account's balance is the running net.

```
   After the equipment entry above:

      Cash                  Equipment            Notes Payable
   +---------+           +---------+           +---------+
   | DR | CR |           | DR | CR |           | DR | CR |
   |    |4000|           |10000|  |           |    |6000|
   +---------+           +---------+           +---------+
   bal: -4000(CR side)   bal: 10000 DR         bal: 6000 CR
```

**Bridge:** the journal is the global, chronological log; the ledger is the same data
**re-indexed by account** — a set of materialized per-key views. Both contain identical
information; the ledger just answers "what is the balance of account X" in O(1).

---

## The Trial Balance: The Consistency Check

At period end, list every account with its balance in the correct column. If the columns
are equal, the log is internally consistent (no one-sided postings).

```
   TRIAL BALANCE — 2026-03-31
   Account                  Debit      Credit
   ----------------------   --------   --------
   Cash                      26,000
   Accounts Receivable        8,000
   Inventory                  5,000
   Equipment                 10,000
   Accumulated Deprec.                    2,000   <- contra-asset (credit)
   Accounts Payable                       4,000
   Notes Payable                          6,000
   Common Stock                          20,000
   Retained Earnings                      9,000
   Revenue                               40,000
   COGS                      18,000
   Salaries Expense          12,000
   Depreciation Expense       2,000
   ----------------------   --------   --------
   TOTALS                    81,000     81,000   <- EQUAL => consistent
```

What the trial balance **does not** catch (the residual error class):

| Caught | Not caught |
|--------|-----------|
| One-sided entry (only DR or only CR) | Entry posted to the wrong account (both sides) |
| Unequal DR/CR amounts | Entry omitted entirely (both sides missing) |
| Transposition that breaks balance | Compensating errors that happen to cancel |
| Math/summation slips | A correct-looking but economically wrong entry |

This is why a clean trial balance is necessary but **not sufficient** — hence audit (file
09). It is a cheap consistency check, not a proof of correctness.

---

## The Full Cycle (the period loop)

```
   +-----------------------------------------------------------------+
   |  1. Transactions occur            (continuous)                  |
   |  2. Journalize                    (append balanced entries)     |
   |  3. Post to ledger                (re-index by account)         |
   |  4. Unadjusted trial balance      (consistency check)           |
   |  5. Adjusting entries             (accruals/deferrals, file 05) |
   |  6. Adjusted trial balance        (re-check)                    |
   |  7. Financial statements          (files 02-04)                 |
   |  8. CLOSING entries               (zero out temp accts ->       |
   |                                    Retained Earnings)           |
   |  9. Post-closing trial balance    (only permanent accts remain) |
   +-----------------------------------------------------------------+
                              |
                        loop to next period
```

**Closing entries** are the period-boundary garbage collection: revenue, expense, and
dividend accounts (temporary) are zeroed and their net swept into Retained Earnings. After
closing, only permanent accounts (assets, liabilities, equity) carry forward — the balance
sheet is the state that persists; the income statement is the per-period delta that gets
folded in and reset.

```
   CLOSING (sweep temp -> permanent):
     DR  Revenue            40,000
         CR  Income Summary        40,000
     DR  Income Summary     32,000
         CR  COGS                  18,000
         CR  Salaries Expense      12,000
         CR  Depreciation Exp.      2,000
     DR  Income Summary      8,000        <- net income
         CR  Retained Earnings      8,000  <- folded into equity
```

---

## Old World → New World Bridges

| Prior art | Double-entry concept |
|-----------|---------------------|
| ACID transaction, all-or-nothing | Atomic journal entry (post all lines or none) |
| Invariant / CHECK constraint | `Assets = Liabilities + Equity`, DR total = CR total |
| Write-ahead log | Journal (chronological, append-only) |
| Materialized per-key views | Ledger / T-accounts (re-indexed by account) |
| Replaying the log to validate state | Trial balance |
| Event sourcing, no in-place mutation | No-erasure rule; reversing entries |
| Parity bit / checksum | The two-sided balance requirement |
| Garbage collection at epoch boundary | Closing entries (zero temporaries) |
| Permanent state vs per-frame delta | Balance sheet (permanent) vs income statement (temporary) |

---

## Decision Cheat Sheet

| Situation | Entry pattern |
|-----------|--------------|
| Buy an asset for cash | DR Asset / CR Cash |
| Buy an asset on credit | DR Asset / CR Accounts Payable |
| Make a sale for cash | DR Cash / CR Revenue |
| Make a sale on credit | DR Accounts Receivable / CR Revenue |
| Collect a receivable | DR Cash / CR Accounts Receivable |
| Pay an expense | DR Expense / CR Cash |
| Borrow money | DR Cash / CR Notes Payable |
| Repay principal | DR Notes Payable / CR Cash |
| Owner invests | DR Cash / CR Common Stock |
| Pay a dividend | DR Dividends / CR Cash |
| Record depreciation | DR Depreciation Exp / CR Accumulated Deprec. |
| Fix a posted error | Reverse the bad entry, then post the correct one |

---

## Common Confusion Points

### "A debit increases everything / decreases everything"

No single rule — it depends on type. Debit increases *debit-normal* accounts (assets,
expenses, dividends) and decreases *credit-normal* ones (liabilities, equity, revenue). Use
DEAD CLIC; do not reason from the everyday banking sense of "credit."

### "My bank statement says 'credit' for deposits — so credit means money in"

That is the bank's books, not yours. Your deposit is the bank's **liability** to you, so on
*their* ledger a deposit is a credit (liability increase). On *your* ledger, cash increasing
is a **debit**. The two ledgers mirror each other; that is why they reconcile.

### "Every entry has exactly one debit and one credit"

Only the simplest do. Compound entries have many lines (the equipment example: one debit,
two credits). The only rule is total debits = total credits.

### "If the trial balance balances, the books are correct"

It only proves *internal consistency* (debits = credits). It cannot detect an entry posted
to the wrong account, an omitted transaction, or two errors that cancel. Correctness needs
adjusting entries (file 05), reconciliation, and audit (file 09).

### "Contra-accounts are just negative assets — why not net them out?"

Because gross + the contra carries information you'd lose by netting. `Equipment 10,000` less
`Accumulated Depreciation 2,000` tells you the asset's original cost *and* how much life is
used up; a single `8,000` net figure hides both. Contra-accounts are the soft-delete /
tombstone pattern: keep the original, record the offset separately.
