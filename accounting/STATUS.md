# accounting/ — Status

**10 files | Complete ✅**

## Files

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | The accounting landscape: transactions → ledger → statements → analysis | ✅ |
| `01-DOUBLE-ENTRY.md` | Accounting equation, debits/credits, journal→ledger→trial balance as an invariant | ✅ |
| `02-BALANCE-SHEET.md` | Assets/liabilities/equity, classification, worked example | ✅ |
| `03-INCOME-STATEMENT.md` | Revenue recognition, COGS, gross/operating/net margin, EPS | ✅ |
| `04-CASH-FLOW-STATEMENT.md` | Operating/investing/financing, direct vs indirect, reconciliation to net income | ✅ |
| `05-ACCRUAL-VS-CASH.md` | Matching principle, deferrals/accruals, why accrual ≠ cash | ✅ |
| `06-COST-ACCOUNTING.md` | Fixed/variable, contribution margin, break-even, allocation, ABC | ✅ |
| `07-MANAGERIAL-ACCOUNTING.md` | Budgeting, variance analysis, transfer pricing, decision-relevant costs | ✅ |
| `08-FINANCIAL-ANALYSIS.md` | Ratio analysis: liquidity/leverage/profitability/efficiency, DuPont | ✅ |
| `09-AUDIT-AND-CONTROLS.md` | Internal controls, SOX, GAAP vs IFRS, revenue standards, manipulations | ✅ |

## Coverage Notes

Accounting **fundamentals** — the formal system by which economic activity is recorded,
summarized, and audited. Framed for a TCS reader: double-entry is an invariant-preserving
ledger (Assets = Liabilities + Equity holds after every transaction), the general ledger is
an append-only log, the trial balance is a consistency check, and reconciliation is
cross-replica agreement. Distinct from `finance/` (markets, derivatives, portfolio theory,
risk models) and `economics/` (theory — micro/macro, game theory, mechanism design). This
directory does not duplicate markets material: it covers the measurement and reporting
layer that sits *underneath* finance.

Key connections: `finance/` (financial statements feed valuation and ratio inputs;
cost of capital), `economics/` (depreciation as capital theory; transfer pricing as
internal-market mechanism design), `behavioral-economics/` (earnings management, anchoring
on round-number EPS, escalation of commitment in capital budgeting).
