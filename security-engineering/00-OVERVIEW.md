# Security Engineering: Threat, Design, Response — Landscape

## Sentinel Context

This directory is one of three in the Sentinel triad (K-Spade C-IV). The thesis: *no single point of truth, no single point of trust, no single point of failure.*

```
THE SENTINEL TRIAD — Security Engineering View
═══════════════════════════════════════════════════════════════════

              Byzantine Fault Tolerance (1982)
              "A compromised node is indistinguishable
               from a Byzantine fault."
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌────────────┐   ╔═══════════╗   ┌──────────────┐
  │ DISTRIBUTED│   ║ SECURITY  ║   │ CLOUD        │
  │ SYSTEMS    │   ║ ENG.      ║   │ ARCHITECTURE │
  │            │   ║           ║   │              │
  │ "Who has   │   ║ "Who do   ║   │ "Where do    │
  │  the       │   ║  you      ║   │  you put     │
  │  truth?"   │   ║  trust?"  ║   │  the truth?" │
  └─────┬──────┘   ╚═════╤═════╝   └──────┬───────┘
        │                │                │
        └────────────────┴────────────────┘
                         │
              Zero trust as design posture
```

Security engineering provides the **adversary model** for the entire volume. Distributed systems assumes crash faults or Byzantine faults in the abstract; security engineering names the actual adversaries --- nation-states, criminal orgs, insider threats, supply-chain attacks --- and builds the verification, authentication, and authorization controls that make consensus meaningful in a hostile world. Zero-trust architecture is the security posture that treats every component as potentially Byzantine: verify every call, encrypt every channel, audit every action. Without this layer, the consensus protocols from distributed systems and the infrastructure patterns from cloud architecture operate on blind faith.

**See also:**
- `../computing/00-SENTINEL-THESIS.md` — Volume thesis: the Sentinel principle and constraint stack
- `../distributed-systems/00-OVERVIEW.md` — Consensus: the theoretical floor that security controls must respect
- `../cloud-architecture/00-OVERVIEW.md` — Infrastructure: where security controls are deployed and enforced

---

## The Big Picture

Security engineering is the discipline of designing, building, and operating systems that remain secure against adversaries. It differs from cryptography (mathematical primitives) and compliance (regulatory checklists) — it is the engineering practice that applies both to build systems that are actually hard to break.

```
SECURITY ENGINEERING LANDSCAPE
+-----------------------------------------------------------------------+
|                                                                       |
|  PROACTIVE (prevent)              REACTIVE (detect and respond)      |
|  +---------------------------+    +-------------------------------+   |
|  | Threat Modeling           |    | Monitoring / SIEM             |   |
|  | Secure Design Principles  |    | Incident Response             |   |
|  | Vulnerability Management  |    | Forensics                     |   |
|  | Secure SDLC (SDL)         |    | Red/Blue Team                 |   |
|  | Identity & Access         |    | Threat Hunting                |   |
|  | Network Security          |    | Post-Incident Review          |   |
|  +---------------------------+    +-------------------------------+   |
|                                                                       |
|  ORGANIZATIONAL                   REGULATORY                         |
|  +---------------------------+    +-------------------------------+   |
|  | Security Champions        |    | SOC 2                         |   |
|  | Security Training         |    | ISO 27001                     |   |
|  | Bug Bounty Programs       |    | FedRAMP                       |   |
|  | SSIRT / CERT              |    | GDPR / CCPA                   |   |
|  +---------------------------+    | PCI DSS                       |   |
|                                   +-------------------------------+   |
+-----------------------------------------------------------------------+

ADVERSARY MODEL
+-----------------------------------------------------------------------+
| Nation-state      | Years of access, supply chain attacks, zero-days  |
| Criminal org      | Ransomware, data theft, financial fraud            |
| Hacktivist        | DDoS, defacement, data exposure                    |
| Insider threat    | Privileged access misuse, accidental exfiltration  |
| Script kiddie     | Known CVEs, commodity tools, opportunistic         |
+-----------------------------------------------------------------------+
```

---

## Security as a Quality Attribute

Security is not a feature added at the end — it is a quality attribute of the system, like performance or reliability. The cost of fixing a vulnerability follows the same rule as other bugs: it is cheapest at design time, most expensive in production.

```
COST OF FIXING SECURITY ISSUES BY PHASE
          |
          |         ████
  Cost    |        ████████
          |       ██████████
          |      ████████████
          |  █   ██████████████
          |  █████████████████████
          +---+-----+------+------+------> Phase
           Req Design Code  Test  Prod

Design-time fix: 1x cost
Production fix:  30–100x cost (+ reputational, regulatory)
```

---

## Microsoft SDL: The Canonical Enterprise Process

You ran teams that built to SDL requirements. The SDL (Security Development Lifecycle) is Microsoft's process for integrating security into every phase of software development, created after the Windows XP security crisis (2002).

```
SDL PHASES

1. TRAINING
   Mandatory security training for all engineers
   Role-specific: developer, PM, test, management

2. REQUIREMENTS
   Security and privacy requirements definition
   Quality gates (security bugs = ship blockers)

3. DESIGN
   Threat model (STRIDE analysis)
   Attack surface review (minimize exposed interfaces)
   Privacy impact assessment

4. IMPLEMENTATION
   Banned API list (strcpy → strcpy_s, etc.)
   Static analysis tools (PREfast, Roslyn analyzers)
   Approved cryptography only (no homegrown crypto)

5. VERIFICATION
   Fuzz testing (required for network-facing components)
   Dynamic analysis (ASan, Application Verifier)
   Manual code review for high-risk components

6. RELEASE
   Final Security Review (FSR) — sign-off by security team
   Security response plan in place

7. RESPONSE
   SSIRT (Security Response Center / MSRC)
   Coordinated disclosure process
   Patch release procedures

MANDATORY SDL DELIVERABLES:
  - Threat model document
  - No banned APIs in code
  - Static analysis passing at required warning level
  - Fuzz results documented
  - Crypto review (approved algorithms only)
  - FSR sign-off
```

---

## The Engineering Discipline vs. Cryptography Theory

Cryptography (`cryptography/` directory) provides the mathematical primitives: AES, RSA, elliptic curves, hash functions, key exchange protocols. Security engineering is what you do with those primitives:

```
CRYPTOGRAPHY PROVIDES:             SECURITY ENGINEERING ASKS:
  AES-256-GCM encryption             Are you using it correctly?
  RSA key exchange                   Are keys stored safely?
  TLS 1.3 protocol                   Is certificate pinning appropriate?
  SHA-3 hashing                      Where in the system is it applied?
  Argon2id password hashing          Is it used consistently everywhere?
                                      What happens if a key is compromised?
                                      How do you rotate credentials?
                                      Who has access to the key material?
```

---

## Threat Surface vs. Attack Surface

```
THREAT SURFACE: Everything that could potentially be attacked
  All input entry points, all auth mechanisms, all data stores,
  all network interfaces, all dependencies, all human actors

ATTACK SURFACE: The subset exposed to attackers
  → Security engineering aims to MINIMIZE the attack surface

ATTACK SURFACE REDUCTION:
  Close unused ports / disable unused features
  Remove debug endpoints before release
  Restrict API access to authenticated clients only
  Use private endpoints instead of public ones
  Minimize privilege (service account has read-only where possible)
  Remove dev/test credentials from production config
```

---

## Guide Map

```
00-OVERVIEW.md             ← you are here
01-THREAT-MODELING.md      ← STRIDE, DREAD, attack trees, PASTA
02-SECURE-DESIGN.md        ← Saltzer-Schroeder, zero trust, SLSA
03-VULNERABILITY-MGMT.md   ← CVE/CVSS, patch SLAs, scanner types
04-SECURE-SDLC.md          ← SDL, DevSecOps, SBOM, secret scanning
05-IDENTITY-ACCESS.md      ← OAuth 2.0, OIDC, PAM, managed identity
06-NETWORK-SECURITY.md     ← segmentation, NGFW, ZTNA, DNSSEC
07-INCIDENT-RESPONSE.md    ← NIST 800-61, SIEM, forensics, postmortem
08-RED-BLUE-TEAM.md        ← red team, pen test, purple team, ATT&CK
09-COMPLIANCE.md           ← SOC 2, ISO 27001, FedRAMP, GDPR, PCI
```

---

## Common Confusion Points

**"Security = compliance"**
Compliance is the floor, not the ceiling. Passing a SOC 2 audit does not mean you are secure — it means you met the audit criteria at a point in time. Attackers do not read compliance checklists. Security engineering is what keeps you secure between audits.

**"Security is the security team's job"**
Security teams own security architecture, threat modeling guidance, incident response, and red team exercises. Security implementation is every engineer's responsibility. The SDL exists precisely because Microsoft learned this lesson after major Windows security failures.

**"Encryption solves security"**
Encryption protects data in transit and at rest. It does not protect against: SQL injection (app-layer), privilege escalation (identity layer), misconfigured access controls (IAM layer), supply chain attacks (dependency layer), or insider threats (human layer). Encryption is one control in a layered defense.

**"We're too small to be a target"**
Commodity attacks (ransomware, credential stuffing) are not targeted — they are automated and scan the entire internet. Being small does not protect you from opportunistic attackers. The question is not "are we a target?" but "are we harder to compromise than average?"

---

## Decision Cheat Sheet

| Concern | Primary Guide |
|---------|--------------|
| "We need to threat model our new service" | 01-THREAT-MODELING.md |
| "What security principles should architecture follow?" | 02-SECURE-DESIGN.md |
| "We have 500 open CVEs — how to prioritize?" | 03-VULNERABILITY-MGMT.md |
| "How do we integrate security into CI/CD?" | 04-SECURE-SDLC.md |
| "OAuth scopes and service accounts confuse our team" | 05-IDENTITY-ACCESS.md |
| "Network segmentation architecture review" | 06-NETWORK-SECURITY.md |
| "We had an incident — what's the process?" | 07-INCIDENT-RESPONSE.md |
| "Planning our first red team exercise" | 08-RED-BLUE-TEAM.md |
| "SOC 2 audit is in 6 months" | 09-COMPLIANCE.md |
