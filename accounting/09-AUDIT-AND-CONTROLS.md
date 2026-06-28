---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:audit-and-controls
kind: guide
module: accounting
section: accounting
title: Audit and Controls - Trust, SOX, GAAP vs IFRS
status: source-custody
source_custody: partial
current_path: accounting/09-AUDIT-AND-CONTROLS.md
canonical_path: accounting/09-AUDIT-AND-CONTROLS.md
backsource_ids: [proof-backfill:accounting:09-audit-and-controls, git-history:accounting:09-audit-and-controls]
concepts: [audit, internal controls, SOX, GAAP, IFRS, revenue recognition, earnings management]
root_concepts: [audit and controls]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Audit and Controls — Trust, SOX, GAAP vs IFRS

## The Big Picture

The financial statements are produced by the people they evaluate — an obvious incentive
problem. The trust infrastructure that makes external accounting credible has three layers:
**standards** (GAAP/IFRS) define what "correct" means; **internal controls** (and SOX) make
the production process tamper-resistant; **audit** independently verifies the output. This is
the security model of accounting — threat model, controls, and an external verifier.

```
+--------------------------------------------------------------------------+
|                   THE TRUST STACK                                       |
|                                                                          |
|   LAYER 3  AUDIT (external verifier)                                     |
|     Independent CPA firm tests evidence, issues an OPINION.             |
|     "Do the statements fairly present, per GAAP/IFRS?"                  |
|              ^                                                          |
|   LAYER 2  INTERNAL CONTROLS  +  SOX (process integrity)               |
|     Segregation of duties, authorization, reconciliation, audit        |
|     trail. SOX 404: management ASSERTS controls work; auditor tests.   |
|              ^                                                          |
|   LAYER 1  STANDARDS: GAAP (US) / IFRS (global)                        |
|     Define recognition, measurement, presentation, disclosure.         |
|              ^                                                          |
|   LAYER 0  DOUBLE-ENTRY (file 01) -- the consistency primitive          |
+--------------------------------------------------------------------------+
```

**Read it bottom-up:** double-entry gives internal consistency; standards give a shared
definition of correct; controls make the process trustworthy; audit verifies. Each layer
assumes the one below. **Bridge (security):** standards = the spec, controls = defense-in-depth
and least-privilege, audit = independent pen-test/attestation.

---

## Layer 1: GAAP vs IFRS — Two Standard-Setters

| | US GAAP | IFRS |
|--|---------|------|
| Setter | FASB (Financial Accounting Standards Board) | IASB (International Accounting Standards Board) |
| Used in | United States | ~140+ countries (EU, UK, much of Asia) |
| Philosophy | **Rules-based** (detailed, bright-line) | **Principles-based** (judgment, substance) |
| Codification | ASC (Accounting Standards Codification) | IAS / IFRS standards |

The rules-vs-principles split is the deep difference. Rules-based GAAP gives bright-line tests
(easier to audit, but gameable by structuring just inside a line — Enron exploited exactly
this). Principles-based IFRS asks for faithful representation of substance (harder to game,
but more judgment and less comparability).

### The differences that actually change the numbers

| Topic | US GAAP | IFRS | Effect |
|-------|---------|------|--------|
| **Inventory (LIFO)** | LIFO permitted | **LIFO prohibited** (IAS 2) | LIFO cuts taxable income when prices rise |
| **R&D / development** | Most R&D expensed | Development costs capitalized if criteria met (IAS 38) | IFRS can show higher assets/profit early |
| **PP&E revaluation** | Historical cost only | Revaluation to fair value allowed (IAS 16) | IFRS can mark assets up |
| **Impairment reversal** | Generally prohibited | Permitted, except goodwill (IAS 36) | IFRS can write back recoveries |
| **Inventory write-down reversal** | Prohibited | Permitted if value recovers | IFRS less sticky |
| **Component depreciation** | Permitted, less emphasized | Required (depreciate parts separately) | IFRS more granular |
| **Interest in cash flow** | Operating | Operating or financing (choice) | Affects CFO comparability (file 04) |

These are real and citable — the LIFO ban (IAS 2), the development-cost capitalization (IAS
38), and the PP&E revaluation option (IAS 16) are the most consequential. Convergence efforts
narrowed many gaps (notably revenue recognition: ASC 606 / IFRS 15 are substantially aligned),
but these remain.

---

## Revenue Recognition: The Highest-Risk Area

Revenue is where most fraud and most honest error live, because it's judgment-heavy and
directly drives the headline number. The converged standard is **ASC 606 / IFRS 15**, the
five-step model from file 03:

```
   1. Identify the contract
   2. Identify performance obligations (distinct promises)
   3. Determine transaction price
   4. Allocate price to obligations
   5. Recognize revenue as each obligation is satisfied
      (point in time OR over time = when CONTROL transfers)
```

Why it's the audit hot spot:

| Manipulation | How it works |
|--------------|--------------|
| **Channel stuffing** | Ship excess product to distributors near period-end to book revenue (returns come back next period) |
| **Premature recognition** | Book revenue before the obligation is satisfied / control transfers |
| **Bill-and-hold abuse** | Invoice for goods not yet delivered, claim revenue |
| **Round-tripping** | Two firms sell to each other to inflate both top lines |
| **Bundling games** | Mis-allocate the transaction price toward delivered obligations |

The "control transfers" principle of ASC 606 is precisely meant to constrain these — you can't
recognize until the customer controls the good/service.

---

## Layer 2: Internal Controls and SOX

Internal controls are the **process safeguards** that prevent and detect errors and fraud
before the statements are issued. The canonical framework is **COSO** (five components:
control environment, risk assessment, control activities, information & communication,
monitoring).

### The core control patterns (map cleanly to security)

```
   SEGREGATION OF DUTIES   -- no one person controls a whole transaction.
     Authorize / Record / Custody of assets / Reconcile = different people.
     (Defeats both error and collusion-free fraud.)  ~ separation of privilege

   AUTHORIZATION           -- transactions need approval at the right level.
                              ~ access control / least privilege

   RECONCILIATION          -- compare independent records (books vs bank).
                              ~ cross-replica consistency check

   AUDIT TRAIL / NO ERASURE -- every entry traceable; reversals not deletes.
                              ~ immutable append-only log (file 01)

   PHYSICAL/LOGICAL ACCESS  -- safeguard assets and the ledger system.
                              ~ access control
```

### Sarbanes-Oxley (SOX), 2002 — the post-Enron law

SOX was the US legislative response to Enron and WorldCom. The provisions that matter:

| Section | Requirement |
|---------|-------------|
| **302** | CEO and CFO **personally certify** the financial statements (criminal liability for knowing falsity) |
| **404** | Management must assess, and the external auditor must attest to, the effectiveness of **internal control over financial reporting (ICFR)** |
| **301 / 201** | Independent audit committee; bars auditors from many non-audit consulting services for clients |
| **PCAOB** | Created the Public Company Accounting Oversight Board to regulate auditors (ended self-regulation) |

SOX 404 is the expensive, VP-relevant one: it forces documented, tested controls over every
process that touches the numbers. **Bridge:** 404 is a compliance-as-code regime — controls
must be defined, evidenced, and independently tested, exactly like SDL/security controls in a
regulated SDLC. The CEO/CFO certification under 302 is signed accountability — no "the system
did it."

---

## Layer 3: The Audit and Its Opinion

An external audit is **reasonable assurance** (not a guarantee) that statements are free of
material misstatement, per GAAP/IFRS. The auditor gathers evidence (sampling, confirmations,
recalculation, analytics) and issues one of four opinions:

```
   +-----------------------------------------------------------+
   | UNQUALIFIED ("clean")  -- fairly presented. The goal.     |
   | QUALIFIED              -- fair EXCEPT for a specific issue |
   | ADVERSE                -- statements are NOT fairly        |
   |                          presented (materially wrong)     |
   | DISCLAIMER             -- auditor cannot form an opinion   |
   |                          (scope limitation, e.g. no       |
   |                           evidence available)             |
   +-----------------------------------------------------------+
```

Key concepts:

| Concept | Meaning |
|---------|---------|
| **Materiality** | A misstatement matters if it could change a user's decision; small errors are tolerated |
| **Reasonable assurance** | High but not absolute — sampling means audit can miss things |
| **Going concern** | Auditor flags substantial doubt the firm survives 12 months |
| **Independence** | Auditor must be independent (SOX limits consulting to clients) |
| **Professional skepticism** | Assume nothing; corroborate management assertions |

The audit is **not** designed to catch all fraud — it provides reasonable assurance against
*material* misstatement. Collusive, well-concealed fraud can pass an audit; that's a limit of
the model, not always a failure.

---

## Common Manipulations (the threat catalog)

Beyond revenue tricks, the recurring schemes — useful as a manager's smell test:

| Scheme | Mechanism | Tell |
|--------|-----------|------|
| **Cookie-jar reserves** | Over-accrue in good years, release in bad ones to smooth earnings | Reserves moving opposite to performance |
| **Big bath** | Pile all bad news into one already-bad quarter (new CEO) | Huge one-time writeoffs at transitions |
| **Capitalizing expenses** | Book operating costs as assets to defer them (WorldCom did this) | Capex rising oddly; margins too smooth |
| **Channel stuffing** | Force product into the channel near period-end | Revenue spikes, AR balloons, returns follow |
| **Off-balance-sheet debt** | Hide liabilities in SPEs/leases (Enron) | Leverage looks too low for the business |
| **Round-number / earnings targets** | Manage to just beat consensus by a cent | Suspiciously exact beats every quarter |

```
   THE UNIVERSAL TELL: net income grows but operating CASH FLOW
   doesn't (file 04). Earnings are accrual and manipulable;
   cash is hard to fake. A widening NI-vs-CFO gap is the single
   best early warning -- the accruals ratio quantifies it.
```

**Bridge to `behavioral-economics/`:** earnings management is driven by anchoring (managing to
a round-number EPS / consensus), loss aversion (smoothing to avoid a reported miss), and
escalation of commitment (covering an earlier shortfall). The fraud triangle — *pressure,
opportunity, rationalization* — is a behavioral, not just a control, model. Controls remove
*opportunity*; culture and incentives address *pressure* and *rationalization*.

---

## Old World → New World Bridges

| Prior art | Audit/controls concept |
|-----------|------------------------|
| Threat model + defense in depth | Internal controls (COSO), control activities |
| Separation of privilege | Segregation of duties (authorize/record/custody/reconcile) |
| Least privilege / access control | Authorization limits, system access controls |
| Immutable append-only log | Audit trail, no-erasure rule (file 01) |
| Cross-replica consistency check | Reconciliation (books vs bank, intercompany) |
| Compliance-as-code, evidenced controls | SOX 404 ICFR (define, evidence, test) |
| Signed release / accountable owner | SOX 302 CEO/CFO certification |
| Independent pen-test / attestation | External audit and its opinion |
| Spec vs implementation conformance | GAAP/IFRS vs the statements produced |

---

## Decision Cheat Sheet

| Question | Where to look |
|----------|---------------|
| Are these numbers trustworthy? | Audit opinion (want unqualified) + internal-control attestation |
| Is the firm a going concern? | Going-concern paragraph in the audit report |
| Is revenue being recognized aggressively? | ASC 606 disclosures; NI-vs-CFO gap; AR growth vs revenue |
| Are earnings being smoothed? | Reserve movements; consistency of "exact" beats |
| Is leverage understated? | Off-balance-sheet items, lease/SPE footnotes |
| GAAP or IFRS firm — comparable? | Check LIFO, R&D, PP&E revaluation choices before comparing |
| Who is personally accountable? | SOX 302 certification (CEO/CFO) |
| Where's the fraud risk concentrated? | Revenue recognition + management estimates |

---

## Common Confusion Points

### "A clean audit opinion means the numbers are guaranteed correct"

No. An audit provides **reasonable assurance** against **material** misstatement, based on
sampling and evidence. Immaterial errors are tolerated, and well-concealed collusive fraud
can evade detection. "Unqualified" means "fairly presented per GAAP," not "guaranteed exact."

### "GAAP and IFRS give the same answer"

They converge on many topics (revenue: ASC 606 / IFRS 15) but diverge on others that move the
numbers: LIFO (GAAP only), development-cost capitalization (IFRS), PP&E revaluation (IFRS),
impairment reversals (IFRS). Never compare a GAAP filer to an IFRS filer without checking
these.

### "Capitalizing a cost is just a bookkeeping choice"

It's a high-risk one. Improperly capitalizing operating expenses turns costs into assets,
inflating both profit and the balance sheet — WorldCom's $3.8B fraud was exactly this. The
test is whether the spend creates a future-benefit asset; if not, it's an expense, period.

### "Internal controls are an accounting / compliance burden, not my problem"

For an exec with budget responsibility under a public company, SOX 404 makes control
effectiveness *your* problem — segregation of duties, authorization, and reconciliation in
every process touching the numbers must be designed, evidenced, and audited. Treat it as
compliance-as-code, not paperwork.

### "Profit smoothing is harmless if it's within GAAP"

Earnings management that stays technically within GAAP still misleads — it's the soft on-ramp
to fraud (cookie-jar reserves, channel stuffing). It distorts the signal investors rely on,
and the NI-vs-CFO divergence usually exposes it eventually. Substance over form is the IFRS
principle precisely because formal compliance can mask economic reality.
