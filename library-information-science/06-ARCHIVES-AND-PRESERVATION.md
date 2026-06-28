---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:archives-and-preservation
kind: guide
module: library-information-science
section: language-communication
title: Archives and Preservation - Provenance, Original Order, OAIS
status: source-custody
source_custody: partial
current_path: library-information-science/06-ARCHIVES-AND-PRESERVATION.md
canonical_path: library-information-science/06-ARCHIVES-AND-PRESERVATION.md
backsource_ids: [proof-backfill:library-information-science:06-archives, git-history:library-information-science:06-archives]
concepts: [archives, provenance, original order, respect des fonds, digital preservation, OAIS, fixity, migration, emulation]
root_concepts: [archival science]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Archives & Preservation — Keeping the Record Authentic

Libraries collect *published* items, each one of many copies, organized by subject.
Archives keep *unique* records — the unpublished, one-of-a-kind documentary residue
of an organization or person — and their governing concern is not subject access but
**authenticity over time**: proving that a record is what it claims to be, has not
been altered, and is still readable decades later. Archival science is, in software
terms, the discipline of **immutable lineage and long-term durability**.

```
+======================================================================================+
|                  ARCHIVES vs LIBRARIES, AND THE PRESERVATION STACK                   |
+======================================================================================+
|                                                                                      |
|   LIBRARY                              ARCHIVE                                       |
|   -------                              -------                                       |
|   published, many copies               unique, unpublished records                   |
|   item-level description by SUBJECT    aggregate description by PROVENANCE           |
|   you can re-buy a lost book           a lost record is gone forever                 |
|                                                                                      |
|   TWO BEDROCK PRINCIPLES (archival arrangement):                                     |
|   .---------------------------.   .-----------------------------------.              |
|   | PROVENANCE                |   | ORIGINAL ORDER                    |              |
|   | (respect des fonds):      |   | (registraturprinzip):             |              |
|   | keep one creator's        |   | preserve the order the creator    |              |
|   | records together, do NOT  |   | kept them in -- the arrangement   |              |
|   | merge across creators     |   | itself is evidence                |              |
|   '---------------------------'   '-----------------------------------'              |
|                                                                                      |
|   PRESERVATION CONCERNS (orthogonal, apply to both):                                 |
|   physical decay  |  format obsolescence  |  bit rot  |  authenticity / fixity       |
+======================================================================================+
```

---

## The Two Bedrock Principles

Archival arrangement rests on two 19th-century French/Prussian principles that
together are called **respect des fonds**. They are the archival equivalents of "do
not rewrite history" and "preserve the audit trail in order."

```
+----------------------------------------------------------------------------+
|  PROVENANCE (respect des fonds)                                            |
+----------------------------------------------------------------------------+
|   Records are grouped by their CREATOR / source, never merged with         |
|   records from another creator -- even if they share a subject.            |
|                                                                            |
|   Why: the body of records of one creator is itself evidence of that       |
|   creator's activity. Mixing them destroys that evidential value.          |
|                                                                            |
|   = partition by source / tenant; never co-mingle lineages.                |
+----------------------------------------------------------------------------+
|                                                                            |
+----------------------------------------------------------------------------+
|  ORIGINAL ORDER (registraturprinzip)                                       |
+----------------------------------------------------------------------------+
|   Keep records in the sequence/arrangement the creator used. Do NOT        |
|   re-sort alphabetically or by date for the archivist's convenience.       |
|                                                                            |
|   Why: the ORDER encodes information (which memo answered which, what      |
|   the creator filed together). Re-sorting erases that context.             |
|                                                                            |
|   = preserve insertion order / the original sequence as data.              |
+----------------------------------------------------------------------------+
```

A data engineer will read these as: **partition by source and never merge tenants**
(provenance), and **the ordering is itself a column — do not normalize it away**
(original order). The arrangement is not metadata about the records; it *is* evidence,
the way a commit graph's structure is evidence beyond the diffs themselves.

Description follows arrangement: archives are described **hierarchically** from the
whole down to the part — fonds -> series -> file -> item — encoded today in **EAD**
(Encoded Archival Description, an XML standard) and governed by **ISAD(G)** (the
international description standard) and **DACS** (the US content standard). This is a
tree of aggregates, not a flat per-item catalog; you describe the box, then the
folder, then occasionally the document.

---

## The Preservation Threat Model

Preservation is a threat model. Three distinct failure modes attack a record over
time, and they need different defenses.

```
+---------------------------------------------------------------------------+
|  THREE THREATS TO A DIGITAL RECORD                                        |
+---------------------------------------------------------------------------+
|                                                                           |
|  1. MEDIA DECAY (the carrier dies)                                        |
|     magnetic tape demagnetizes, optical discs delaminate, drives fail.    |
|     Defense: replication + media refresh (copy to new carriers).          |
|                                                                           |
|  2. FORMAT OBSOLESCENCE (the reader dies)                                 |
|     the bits survive but no software can interpret them (WordStar files,  |
|     a dead codec). Defense: MIGRATION or EMULATION (below).               |
|                                                                           |
|  3. BIT ROT / TAMPERING (the bits change)                                 |
|     silent corruption or alteration. Defense: FIXITY -- checksums         |
|     verified on a schedule (a record's content hash).                     |
+---------------------------------------------------------------------------+
```

**Fixity** is the archival word for a content hash. You compute a checksum (MD5/
SHA-256) when a record enters custody and re-verify it on a schedule; a mismatch
signals corruption or tampering. This is exactly content-addressable integrity — the
same mechanism Git uses to guarantee a blob is unaltered. The archival principle is
that authenticity must be *provable*, not asserted, and a verified hash chain is the
proof.

The two responses to format obsolescence are a classic engineering fork:

| | Migration | Emulation |
|---|---|---|
| Strategy | Convert the file to a current format | Recreate the old environment to run the old file |
| Analogy | Port the code to a new platform | Run it in a VM/container of the old platform |
| Risk | Each conversion may lose fidelity | Emulator complexity; legal/licensing of old software |
| Best for | Documents, images (open, simple formats) | Software, games, complex interactive objects |
| Cumulative | Yes — migrate again each format cycle | No — emulate the original once |

---

## OAIS — The Reference Architecture (ISO 14721)

The **Open Archival Information System (OAIS)** reference model (ISO 14721, from the
space-data community, CCSDS) is the standard architecture for a trusted digital
repository. It is a clean pipeline-and-store design that any systems architect will
recognize, built around three **Information Package** types.

```
+=======================================================================================+
|                      THE OAIS FUNCTIONAL MODEL (ISO 14721)                            |
+=======================================================================================+
|                                                                                       |
|  PRODUCER                                                          CONSUMER           |
|     |                                                                 ^               |
|     | SIP                                                             | DIP           |
|     v                                                                 |               |
|  .--------.    .------------.    .-------------.    .--------.    .---------.         |
|  | INGEST |--->| ARCHIVAL   |--->|  STORAGE    |--->| ACCESS |--->| (deliver|         |
|  |        |    | STORAGE    |    |  (AIP held) |    |        |    |  to user)|        |
|  '--------'    '------------'    '-------------'    '--------'    '---------'         |
|     |               |                  |                |                             |
|     | validates     | manages          | fixity         | builds the                  |
|     | the SIP,      | the AIP over      | checks,        | DIP on request             |
|     | builds AIP    | time              | refresh        |                            |
|                                                                                       |
|  Cross-cutting: DATA MANAGEMENT | PRESERVATION PLANNING | ADMINISTRATION              |
+=======================================================================================+
|                                                                                       |
|  THE THREE INFORMATION PACKAGES:                                                      |
|    SIP  Submission Information Package -- what the producer hands in                  |
|    AIP  Archival Information Package   -- what is preserved long-term (+ metadata)    |
|    DIP  Dissemination Information Pkg  -- what the consumer receives                  |
+=======================================================================================+
```

The SIP/AIP/DIP split is request/storage/response with explicit transformation at
each boundary — the same shape as a write path that validates and enriches input
(SIP -> AIP) and a read path that projects stored data into a delivery format (AIP ->
DIP). Critically, OAIS mandates that the AIP carry its own **Preservation Description
Information**: provenance, fixity (the checksums), context, and reference identifiers,
so the package is self-describing and its authenticity is self-provable. An AIP is
an immutable, integrity-stamped, self-documenting record — the archival analog of a
signed, content-addressed artifact in an immutable store.

**Preservation Planning** is the cross-cutting function that watches for format
obsolescence and schedules migrations before a format dies. It is monitoring plus a
remediation plan — exactly the operational posture you would design for any system
that must outlive its own technology stack.

---

## Old World → New World

| Archival concept | Software equivalent |
|---|---|
| Provenance (respect des fonds) | Partition by source; never merge tenants |
| Original order | Insertion order preserved as data |
| Fixity / checksum | Content hash (SHA-256), integrity verification |
| Authenticity chain | Immutable audit log / signed lineage |
| Migration | Porting to a new format/platform |
| Emulation | Running legacy software in a VM/container |
| AIP (self-describing package) | Content-addressed artifact with embedded metadata |
| OAIS SIP/AIP/DIP | Ingest / store / deliver pipeline with transforms |
| Preservation planning | Obsolescence monitoring + remediation runbook |

---

## Decision Cheat Sheet

| Situation | Approach |
|---|---|
| Organizing one creator's unique records | Respect provenance — keep them together |
| Tempted to re-sort records "logically" | Don't — preserve original order |
| Detecting silent corruption | Schedule fixity (checksum) verification |
| A file format is going obsolete (simple doc) | Migrate to a current open format |
| A complex interactive object is obsolete | Emulate the original environment |
| Designing a trusted digital repository | Follow OAIS (ISO 14721) |
| Describing a large body of records | Hierarchical: fonds -> series -> file -> item (EAD) |
| Proving a record is unaltered | Verified fixity + provenance chain |

---

## Common Confusion Points

### "Archive vs. backup — same thing?"

No, and conflating them is a real failure. A backup is a recent copy for disaster
recovery, expected to be overwritten and short-lived. An archive is the authoritative
long-term record, kept indefinitely with provenance, fixity, and a preservation plan.
A backup answers "can I recover yesterday's state?"; an archive answers "can I prove
this record is authentic in fifty years?"

### "Why preserve 'original order' — wouldn't sorting be more useful?"

Because the order itself is evidence. Which documents the creator filed together,
the sequence of a correspondence, what answered what — re-sorting alphabetically
destroys that context permanently. The arrangement is data, not packaging. (You
would not re-sort a commit history into alphabetical order either.)

### "Migration vs. emulation — which is correct?"

Neither is universally correct; it is the same port-vs-virtualize choice you know.
Migrate simple, open formats (each cycle risks small fidelity loss but keeps content
natively usable). Emulate complex, interactive, or software objects (preserve the
original bits once, recreate the environment to run them). Many repositories do both
and keep the original alongside migrated copies.

### "Isn't fixity just a checksum — why the special word?"

It is a checksum, but the archival point is the *practice*: compute on ingest, store
in the package's preservation metadata, and re-verify on a schedule so corruption is
caught and provable, not discovered too late. Same mechanism as content-addressed
integrity; the discipline is what makes it preservation rather than a one-time hash.

### "Does OAIS require specific software?"

No — OAIS is a *reference model*, an abstract architecture (functions, packages,
responsibilities), not an implementation. Repositories like Archivematica, Preservica,
or a Fedora-based stack are OAIS-conformant designs. It defines the shape (SIP/AIP/DIP,
the functional entities), and you choose the implementation — the way a reference
architecture constrains the design without dictating the stack.
