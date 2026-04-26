# Threat Modeling: STRIDE, DREAD, Attack Trees, PASTA

## The Big Picture

Threat modeling is the structured process of identifying, enumerating, and prioritizing threats to a system. Done at design time, it surfaces the threats you need to address before they become vulnerabilities in production.

```
THREAT MODELING PROCESS
+-----------------------------------------------------------------------+
|                                                                       |
|  DECOMPOSE          IDENTIFY          PRIORITIZE        MITIGATE      |
|  +-----------+     +----------+      +----------+      +----------+   |
|  | What are  |     | What can |      | Which    |      | What     |  |
|  | the       | --> | go wrong | -->  | threats  | -->  | controls |  |
|  | components|     | with     |      | matter   |      | address  |  |
|  | and data  |     | each     |      | most?    |      | each?    |  |
|  | flows?    |     | piece?   |      | (DREAD,  |      | (Accept, |  |
|  | (DFD)     |     | (STRIDE) |      |  risk)   |      |  Fix,    |  |
|  |           |     |          |      |          |      |  Transfer)|  |
|  +-----------+     +----------+      +----------+      +----------+  |
|                                                                      |
|  INPUT:                             OUTPUT:                          |
|  Architecture diagram               Threat model document            |
|  Data flow diagram (DFD)            Threat list with risk scores     |
|  Trust boundary definitions         Mitigations per threat           |
|  Component inventory                Open items tracked in backlog    |
+-----------------------------------------------------------------------+
```

---

## STRIDE: Threat Categories

STRIDE is a mnemonic for 6 categories of threats. Developed at Microsoft for the SDL. For each component and data flow in your DFD, ask: which STRIDE categories apply?

### S — Spoofing

**Definition**: Attacker impersonates another identity (user, service, or system).

**Examples**:
- User submits forged cookie to impersonate another user
- Service calls an API pretending to be a trusted microservice
- Attacker serves a malicious endpoint that looks like a legitimate service (ARP spoofing, DNS hijacking)
- Phishing: user clicks link to attacker-controlled site that looks like the real login page

**Countermeasures**: Authentication (passwords, MFA, certificates, mutual TLS), cryptographic signatures, certificate pinning.

### T — Tampering

**Definition**: Attacker modifies data in transit or at rest without authorization.

**Examples**:
- Man-in-the-middle modifies HTTP request/response
- Attacker modifies log files to hide intrusion evidence
- SQL injection modifies database records
- Attacker modifies build artifact after CI produces it (supply chain)
- Memory corruption modifies program state at runtime

**Countermeasures**: Integrity checking (HMAC, signatures, checksums), TLS for transit, access controls on data stores, immutable audit logs, signed build artifacts (SLSA).

### R — Repudiation

**Definition**: Actor denies having performed an action; system cannot prove otherwise.

**Examples**:
- User transfers funds, claims they did not — no audit trail
- Admin modifies config, no logging of the change
- Service processes message but no record of receipt

**Countermeasures**: Tamper-evident audit logging, digital signatures on actions (non-repudiation), secure log storage (write-once logs), centralized SIEM that aggregates before logs can be deleted.

### I — Information Disclosure

**Definition**: Attacker gains access to data they should not see.

**Examples**:
- Verbose error messages expose stack traces, internal paths, credentials
- Unencrypted data in transit (HTTP vs. HTTPS)
- Overly permissive access controls (reads other users' data)
- Log files contain PII or secrets
- API returns more data than needed (over-fetching)
- Side-channel attacks (timing, memory)

**Countermeasures**: Encryption at rest and in transit, least-privilege access, sanitize error messages, output encoding, data classification.

### D — Denial of Service

**Definition**: Attacker degrades or prevents legitimate users from accessing the service.

**Examples**:
- Network-level DDoS (volumetric: exhaust bandwidth)
- Application-level DoS (algorithmic: slow regex, zip bomb, expensive query)
- Resource exhaustion (fill disk, exhaust connection pool, OOM)
- Hash collision attacks on HashMap (algorithmic DoS — fixed in Java/Python)
- ReDoS: regex with exponential backtracking

**Countermeasures**: Rate limiting, input validation (size limits, complexity limits), resource quotas, circuit breakers, CDN / DDoS protection (Azure DDoS Standard), connection pool limits.

### E — Elevation of Privilege

**Definition**: Attacker gains capabilities beyond what they were authorized for.

**Examples**:
- Horizontal: user A accesses user B's data (IDOR — Insecure Direct Object Reference)
- Vertical: unprivileged user gains admin access
- SQL injection that runs as DBA role
- Container escape from pod to node
- Local privilege escalation via vulnerable SUID binary

**Countermeasures**: Authorization checks (not just authentication), parameter validation, least privilege, input validation, security boundaries (containers, VMs), regular privilege reviews.

---

## STRIDE-per-Element Methodology

Apply STRIDE to each element in the data flow diagram:

```
DATA FLOW DIAGRAM ELEMENTS AND APPLICABLE THREATS
+-----------------------------------------------------------------------+
| DFD Element              | Applicable STRIDE Threats                  |
+-----------------------------------------------------------------------+
| External entities        | Spoofing, Repudiation                       |
| (users, external systems)|                                             |
+-----------------------------------------------------------------------+
| Processes                | Spoofing, Tampering, Repudiation,          |
| (services, APIs)         | Info Disclosure, DoS, Elevation            |
+-----------------------------------------------------------------------+
| Data flows               | Tampering, Info Disclosure, DoS              |
| (HTTP, gRPC, queue msgs) |                                             |
+-----------------------------------------------------------------------+
| Data stores              | Tampering, Repudiation, Info Disclosure,   |
| (DBs, caches, files)     | DoS (store exhaustion)                     |
+-----------------------------------------------------------------------+
| Trust boundaries         | Spoofing, Tampering, Elevation              |
| (the line between trust  |                                             |
| zones)                   |                                             |
+-----------------------------------------------------------------------+
```

---

## DREAD Scoring

DREAD is a risk scoring system for prioritizing identified threats. It has been de-emphasized in recent SDL practice (too subjective) but remains useful for relative ranking.

| Factor | Description | Score Range |
|--------|-------------|-------------|
| **D**amage | How severe if exploited? (financial, reputational, regulatory) | 1–10 |
| **R**eproducibility | How reliably can the attacker exploit it? | 1–10 |
| **E**xploitability | How difficult to exploit? (skill required) | 1–10 |
| **A**ffected users | How many users are impacted? | 1–10 |
| **D**iscoverability | How likely is the attacker to find this? | 1–10 |

**Total DREAD score** = sum or average of the five factors.

**Criticism**: DREAD scores are highly subjective and different people score the same threat very differently. CVSS (Common Vulnerability Scoring System) is more reproducible for vulnerabilities. For threat models, CVSS-inspired scoring is preferred over DREAD.

**Practical use of DREAD**: Rank threats relative to each other within a single model, not for comparison across models or teams.

---

## Attack Trees

Attack trees represent all known paths to achieving an attacker's goal.

```
ATTACK TREE: Steal customer payment data from Order Service

[ROOT GOAL] Steal payment data
          │
    ┌─────┴─────┐
    │           │
  [OR]        [OR]
    │           │
Exfiltrate   Access DB
from app     directly
    │           │
  ┌─┴──┐      ┌─┴──┐
  │    │      │    │
SQL  API    Creds  Net
Inj  resp   dump   attack
    leak
              │
          ┌───┴───┐
          │       │
       [AND]     [AND]
          │       │
       Find    Break
       creds   into
       in log  network

NOTATION:
  [OR]  node: any child sufficient to reach parent
  [AND] node: all children required to reach parent

LEAF NODES: concrete attacker actions
  Assign probability, difficulty, cost to each leaf
  Roll up to root: what is overall attack difficulty?
```

Attack trees help enumerate all paths to a goal (not just the obvious ones) and quantify the relative difficulty.

---

## PASTA: Process for Attack Simulation and Threat Analysis

PASTA is a risk-centric framework (vs. STRIDE which is threat-centric). 7 stages:

```
PASTA 7 STAGES
+------------------------------------------------------------------+
| Stage 1: DEFINE OBJECTIVES                                       |
|   Business objectives, security objectives, compliance needs     |
|   Who are we protecting? What is the business impact of breach?  |
+------------------------------------------------------------------+
| Stage 2: DEFINE TECHNICAL SCOPE                                   |
|   Components, technologies, interfaces, dependencies             |
+------------------------------------------------------------------+
| Stage 3: DECOMPOSE APPLICATION                                   |
|   Data flow diagrams, use cases, trust boundaries                |
+------------------------------------------------------------------+
| Stage 4: THREAT ANALYSIS                                          |
|   Threat intelligence (current threat landscape)                 |
|   Attack scenarios relevant to the application type             |
+------------------------------------------------------------------+
| Stage 5: VULNERABILITY AND WEAKNESS ANALYSIS                     |
|   Map existing vulnerabilities to identified threats             |
|   SAST results, pen test findings, known CVEs in dependencies    |
+------------------------------------------------------------------+
| Stage 6: ATTACK ENUMERATION AND SIMULATION                        |
|   Attack trees for each threat                                   |
|   Simulate attacker steps                                        |
+------------------------------------------------------------------+
| Stage 7: RISK AND IMPACT ANALYSIS                                |
|   Risk = likelihood × impact                                     |
|   Prioritize mitigations by business risk                        |
|   Output: risk register with treatment decisions                 |
+------------------------------------------------------------------+
```

**PASTA vs. STRIDE**: STRIDE is faster and more developer-accessible. PASTA is more rigorous for high-risk systems and produces a business-risk-aligned output. Most engineering teams use STRIDE; security teams on critical systems may use PASTA.

---

## Microsoft Threat Modeling Tool

Microsoft provides a free GUI threat modeling tool that:
- Accepts stencil-based DFD diagrams (drag and drop components)
- Automatically generates STRIDE threats per element
- Tracks mitigation status (mitigated, not applicable, needs investigation)
- Exports threat model document (SDL mandatory deliverable)

```
TOOL WORKFLOW:
  1. Create DFD using built-in stencils (process, data store, actor, flow)
  2. Mark trust boundaries (dashed lines around trust zones)
  3. Tool auto-generates: "Spoofing of the external actor User"
  4. For each generated threat: mark as Mitigated / Not Applicable / Needs Review
  5. Export report → attach to SDL deliverable
  6. Review with security champion before design is finalized
```

**SDL requirement**: Threat model must be created during design phase, not retrospectively. Changes to DFD (new component, new data flow) require threat model update.

---

## When to Threat Model

```
ALWAYS THREAT MODEL:
  New product or service (before first line of code)
  New authentication or authorization mechanism
  New network interface or protocol
  New data store containing sensitive data
  New external integration or partner connection
  Architectural change that crosses trust boundaries

OPTIONAL (but valuable):
  Significant refactor of existing security-critical component
  New deployment model (on-prem → cloud, monolith → microservices)

ANTI-PATTERN — doing it wrong:
  Threat modeling after code is written
  Threat modeling as a checkbox (generate threats, mark all "mitigated")
  No tracking of open threats in the backlog
  Threat model that is never updated when design changes
```

---

## Common Confusion Points

**"Threat modeling is a security team activity"**
Threat modeling is most effective when done by the feature team (architects, senior engineers) with security team guidance. Feature engineers understand the design; security engineers know the threat categories. Both together produce the most complete result.

**"STRIDE generates the mitigations"**
STRIDE identifies threats. Countermeasures must still be designed. A common mistake is running STRIDE and stopping — the output is threats, not solutions.

**"Threat modeling = pen test"**
Threat modeling is proactive (design time). Pen tests are reactive (validate an existing system). They are complementary: threat models identify what to test; pen tests validate whether mitigations work.

**"I need PASTA for enterprise threat models"**
PASTA's rigor has diminishing returns for most service-level threat models. STRIDE + DFD is appropriate for most teams. Use PASTA when business risk quantification is needed for executive-level risk decisions.

---

## Decision Cheat Sheet

| Situation | Recommended Approach |
|-----------|---------------------|
| New service, dev team owns it | STRIDE + Microsoft TM Tool, SDL deliverable |
| High-risk payment / auth system | PASTA (risk-centric business alignment) |
| Visual representation of all attack paths | Attack trees |
| Quick team threat brainstorm | STRIDE categories on whiteboard |
| Prioritizing 20 threats for backlog | DREAD scoring (relative, same reviewer) |
| Validating mitigations in production | Pen test (08-RED-BLUE-TEAM.md) |
