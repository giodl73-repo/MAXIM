# Clinical Full-Module R1 - Expert Skeptic

## Judgment

The full 12-guide `clinical-medicine/` module **holds the non-advice contract**: across all
twelve guides the voice is third-person descriptive, no drug doses/titration/routes or
step-by-step procedures appear, acute content (guide 05) stays conceptual (no first-aid/CPR/
self-treatment), capacity (guide 10) is framed as *how clinicians assess* rather than a reader
self-test, and numeric thresholds are labeled illustrative and attributed/dated. **No advice-creep
BLOCK** was found. The findings below are **conservative and nonblocking** — a missing resource
caveat in three care-architecture guides plus four hedging/voice/attribution notes. All are
repaired.

## Findings

### ES-01 - WARN: Care-architecture guides assume a resourced system without a local caveat

Files: `clinical-medicine/05-ACUTE-AND-CHRONIC-CARE.md`,
`clinical-medicine/07-CARE-TRANSITIONS.md`, `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md`

Finding: Guides 05, 07, and 11 model care in a resourced system — continuous monitoring and a
full registry (05), an EHR with electronic result routing and a reachable integrator (07), and
CPOE/CDS/closed-loop result management (11) — without a guide-local caveat naming *which
invariants survive* when those are absent. This is exactly the resourced-system assumption flagged
in `MAXIM-CLIN-22`; guide 08 already handles it well (its §7/§10 alternate topologies), but 05, 07,
and 11 neither flagged the assumption nor pointed to that treatment, so each read as if the
resourced shape were universal.

Fix: Added a concise **Resource and geographic caveat** to each of the three guides, stating that
the load-bearing invariants are *implementation-independent* and survive without
EHR/CPOE/continuous monitoring/specialist access — acute triage-by-acuity and the chronic
monitor→adjust loop (05); structured serialization, explicit acknowledgment, reconciliation, the
three continuities, and the named-owner closed loop (07); defense-in-depth, just culture,
measurement, and the named-owner closed loop (11) — with only the *mechanism* changing (paper log,
intermittent checks, teleconsult/task-shifted escalation). Each caveat points to guide 08's
alternate interface topologies (§7, §10), and each guide remains independently readable.

### ES-02 - NOTE: Disclosure-standard wording overstated a contested, jurisdiction-varying picture

File: `clinical-medicine/10-ETHICS-CONSENT-CAPACITY.md`

Finding: The consent section stated the *reasonable-person* disclosure standard "has largely
displaced the older *professional* standard in many places." That overstates a legal picture that
still varies by jurisdiction — some retain a professional/physician standard, and others apply a
more patient-specific standard.

Fix: Hedged to note that disclosure standards *vary by jurisdiction and remain contested* —
reasonable-person, professional, and patient-specific standards all in use, several jurisdictions
trending patient-centered, none universal — with the legal detail still deferred to `law/`.

### ES-03 - NOTE: "Appreciation most often selectively lost" is an unsupported superlative

File: `clinical-medicine/10-ETHICS-CONSENT-CAPACITY.md`

Finding: The capacity section asserted appreciation "is the ability **most often** selectively
lost." The clinical point (understanding-in-the-abstract can dissociate from appreciation-of-self,
e.g., in denial or delusion) is sound, but the empirical superlative is not cleanly supportable.

Fix: Hedged to "APPRECIATION is **frequently** the ability selectively lost — and often the one
hardest to detect," aligning the reader task's wording as well; the clinical mechanism is retained.

### ES-04 - NOTE: Second-person software aside in guide 11 breaks the third-person voice

File: `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md`

Finding: The opening systems bridge read "**If you have run an incident review, you already know**
the shape" — a second-person aside inconsistent with the module's third-person, non-imperative
convention (even as a software analogy, not advice).

Fix: Recast to third person: "**Anyone who has run an incident review will recognize** the shape;
medicine adds the constraint that the 'service' is a person."

### ES-05 - NOTE: Four-level prevention presented without its conventional-framing relationship

File: `clinical-medicine/09-PREVENTION-AND-SCREENING.md`

Finding: Section 1 presented primary/secondary/tertiary/quaternary as one taxonomy and noted
"Quaternary prevention (Jamoulle) is the newest framing," but did not situate the four-level model
against the **conventional three-level public-health framing** (Leavell & Clark), which could read
as if four levels were the settled standard.

Fix: Framed the conventional taxonomy as **three levels** (primary/secondary/tertiary), with
**quaternary as Marc Jamoulle's later extension**, so the four-level table is explicitly an
*extension* of the standard model rather than a universally settled one; population-scale ownership
still deferred to `public-health/`.

## Advice-Creep Checklist (all 12 guides)

| Check | Result |
|---|---|
| Third-person descriptive voice (no second-person imperative) | Pass (guide-11 aside recast, ES-04) |
| No drug doses / titration / routes | Pass |
| No step-by-step procedure/technique instructions | Pass |
| Acute content conceptual only (no CPR/first-aid/self-treatment) | Pass (guide 05) |
| Screening as reasoning; thresholds attributed and dated | Pass (guide 09) |
| Capacity as *how clinicians assess*, not a reader tool | Pass (guide 10) |
| Every numeric threshold labeled illustrative / as-of-date | Pass |
| Emergency framing routed to local services, not reader instruction | Pass (banners) |

No imperative-mood treatment/emergency instruction was found in any guide; the advice-creep gate is
**not triggered**.
