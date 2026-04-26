# Secure SDLC: SDL at Microsoft, DevSecOps, SBOM, Secret Scanning

## The Big Picture

A Secure Software Development Lifecycle integrates security practices into every phase of development — requirements through response. The goal is not to slow down development but to move security feedback left, where it is cheapest to fix.

```
SECURE SDLC LIFECYCLE
+-----------------------------------------------------------------------+
|                                                                       |
|  REQUIREMENTS   DESIGN   IMPLEMENT   VERIFY   RELEASE   RESPOND     |
|  +-----------+ +------+ +--------+ +------+ +-------+ +--------+   |
|  | Security  | |Threat| |Banned  | |SAST  | |FSR    | |MSRC    |   |
|  | & privacy | |model | |API list| |DAST  | |sign-  | |process |   |
|  | require-  | |Attack| |Crypto  | |Fuzz  | |off    | |patch   |   |
|  | ments     | |surface|approved | |review| |       | |deploy  |   |
|  |           | |review| |only    | |SCA   | |       | |        |   |
|  +-----------+ +------+ +--------+ +------+ +-------+ +--------+   |
|                                                                       |
|  SHIFT LEFT: Problems found in requirements cost 1x                  |
|              Problems found in production cost 30-100x               |
|                                                                       |
|  DEVOPS INTEGRATION (DevSecOps):                                      |
|  Every commit: SAST scan, secret scan, SCA                         |
|  Every PR: security gate (no new high/critical issues)             |
|  Every merge: container scan, IaC scan                             |
|  Every release: FSR or automated equivalents                       |
+-----------------------------------------------------------------------+
```

---

## Microsoft SDL: Phase by Phase

Microsoft SDL (Security Development Lifecycle) was created in 2002 following a Bill Gates memo declaring that Windows security failures required a fundamental process change. SDL is the industry reference for enterprise secure SDLC.

### Phase 1: Training

All engineers receive mandatory security training, role-specific:
- Developers: secure coding practices, OWASP Top 10, cryptographic API usage
- Program managers: privacy requirements, threat modeling
- Testers: security test techniques, fuzzing methodology
- Management: security ROI, escalation paths

### Phase 2: Requirements

Security and privacy requirements are defined alongside functional requirements:

```
SECURITY REQUIREMENTS EXAMPLES:
  "Authentication: All API endpoints require OAuth 2.0 bearer token"
  "Authorization: Users may only access their own resources (no IDOR)"
  "Cryptography: TLS 1.2 minimum, TLS 1.3 preferred"
  "Logging: All auth events logged with user ID, timestamp, IP"
  "Data at rest: PII encrypted with approved algorithm"

QUALITY GATES DEFINED HERE:
  "No P1/P2 security bugs at ship"
  "Threat model required and approved before design is finalized"
  "Static analysis clean at required warning level"
```

### Phase 3: Design

- Threat model created (STRIDE + DFD — see 01-THREAT-MODELING.md)
- Attack surface review: minimize exposed interfaces
- Privacy impact assessment: data classification, PII handling
- Principle of least privilege applied to component design

### Phase 4: Implementation

**Banned API list**: Microsoft maintains a list of functions that must not be used in SDL-compliant code. These are functions with known security issues that have safe replacements:

```
BANNED IN C/C++:
  strcpy   → use strcpy_s (bounds-checking)
  strcat   → use strcat_s
  gets     → use gets_s
  sprintf  → use sprintf_s
  strlen on untrusted input → use strnlen
  _alloca  → (stack allocation, stack overflow risk)
  IsBadWritePtr, IsBadReadPtr → (unreliable, avoid)

BANNED IN .NET (OACR / Roslyn analyzer):
  MD5     → use SHA-256 or SHA-3
  SHA1    → use SHA-256 or SHA-3
  DES/3DES → use AES-256-GCM
  RC4     → do not use
  RNGCryptoServiceProvider (legacy) → use RandomNumberGenerator (static)
  Marshal.Copy without bounds check → validate lengths
```

**Cryptography rules**: Only MSRC-approved algorithms may be used:
- Symmetric encryption: AES-256 (GCM mode preferred)
- Asymmetric: RSA-2048+ or ECC P-256+
- Hashing: SHA-256, SHA-384, SHA-512
- Key exchange: ECDH P-256, X25519
- No custom crypto, no MD5 for security, no SHA-1 for security

### Phase 5: Verification

**Fuzzing (required for SDL)**: Network-facing components must be fuzz-tested. Fuzzing sends malformed, random, and boundary inputs to find crashes, hangs, and assertion failures that indicate vulnerabilities.

```
FUZZING APPROACHES:
  Black-box fuzzing: generate random inputs, observe crashes
  Grammar-based: fuzz within structure of protocol/format
    (more efficient: knows valid envelope, mutates content)
  Coverage-guided (libFuzzer, AFL, HonggFuzz):
    instrument code, prefer inputs that reach new code paths
    → most efficient: finds deep bugs, not just surface crashes

FUZZING IN CI:
  OSS-Fuzz: Google-managed continuous fuzzing for open source
  Azure DevOps: custom fuzzing jobs in pipeline
  LibFuzzer: runs as unit test, LLVM-based instrumentation
  AFL (American Fuzzy Lop): popular, binary-mode capability
```

**Application Verifier and AddressSanitizer**:
- Application Verifier (Windows): runtime heap corruption detection, handle leak detection
- AddressSanitizer (ASan): compiler-instrumented detection of buffer overflow, use-after-free, double-free

### Phase 6: Release — Final Security Review (FSR)

Before shipping, a security team member reviews:
- All SDL deliverables are complete
- No P1/P2 security bugs open
- Threat model is current with implementation
- Crypto review approved
- Fuzz testing completed
- Penetration test findings addressed

**FSR sign-off**: explicit go/no-go gate. In VSTS/ADO you would have had this as a checklist item before release branch promotion.

### Phase 7: Response

- Security Response Plan in place before release (who gets called when?)
- MSRC-style intake process for external vulnerability reports
- Patch development and release process defined
- Customer notification procedure for security bulletins

---

## DevSecOps: Integrating SDL into CI/CD

DevSecOps moves SDL checks into the automated pipeline:

```
AZURE DEVOPS PIPELINE INTEGRATION

PR TRIGGER (every pull request):
  +-- SAST scan (CodeQL, Semgrep)
  |    Block merge if new HIGH/CRITICAL findings
  +-- Secret scanning (GitHub Advanced Security, truffleHog)
  |    Block merge if secret detected in diff
  +-- SCA / Dependabot
  |    Notify on new CVEs in added dependencies
  +-- IaC scanning (Checkov, TFSec)
       Check Bicep/Terraform for misconfigurations

BUILD TRIGGER (on merge to main):
  +-- Container image build
  +-- Container image scan (Trivy, Defender for Containers)
  |    Block push to registry if CRITICAL CVEs in OS packages
  +-- SBOM generation (attached to artifact)
  +-- Artifact signing (sigstore/cosign or Microsoft notation)

RELEASE TRIGGER (pre-deploy):
  +-- DAST scan against staging environment
  +-- Smoke test security controls (auth, encryption headers)
  +-- Deploy to canary → promote on pass
```

---

## SBOM: Software Bill of Materials

A Software Bill of Materials is a formal inventory of all components in a software artifact — libraries, packages, dependencies, their versions, and their licenses.

```
SBOM MINIMUM ELEMENTS (NTIA):
  Supplier name
  Component name
  Version
  Unique identifier (package URL, hash)
  Dependency relationship (component A depends on B)
  Author of SBOM data
  Timestamp

FORMATS:
  SPDX (Linux Foundation): JSON, YAML, RDF, XML
  CycloneDX (OWASP): XML, JSON — more security-focused
  Microsoft uses CycloneDX internally

GENERATION TOOLS:
  syft (Anchore): generates SBOM from container images, directories
  cdxgen: CycloneDX generator for multiple package ecosystems
  dotnet sbom-tool (Microsoft): .NET SBOM generation
  GitHub Actions: SBOM generation in workflows

WHY SBOM MATTERS:
  Log4Shell (2021): organizations didn't know which of their apps
  used Log4j because they had no component inventory. SBOM would have
  immediately answered: "Is Log4j 2.x in any of our deployed artifacts?"

  Executive Order 14028 (2021, US): requires SBOM for software sold
  to US federal government

USAGE:
  Store SBOM alongside artifact in registry
  At incident response: query SBOM for affected components
  Continuous: scan new CVEs against SBOM inventory (Dependency-Track)
```

---

## Secret Scanning

Accidentally committed secrets are a pervasive and catastrophic class of vulnerability. Secrets in git are effectively public — anyone with repo access, or any attacker who gains repo access, can read them.

```
SECRET TYPES TO DETECT:
  API keys (AWS access keys, GitHub tokens, Azure storage keys)
  Connection strings (database passwords, Redis/service bus keys)
  Private keys (RSA PEM blocks, SSH keys)
  Certificate files (.pfx, .p12)
  JWT signing secrets
  OAuth client secrets
  .env files with populated values

SCANNING TOOLS:
  GitHub Secret Scanning: built-in, covers 100+ providers
    Push protection: blocks push if secret detected (configurable)
  truffleHog: historical scan of git history, regex + entropy
  GitGuardian: continuous monitoring with incident dashboard
  gitleaks: fast, pattern-based, CI-friendly
  detect-secrets (Yelp): pre-commit hook, baseline management

RESPONSE WHEN SECRET FOUND IN HISTORY:
  1. Assume compromised immediately — rotation first, history second
  2. Rotate the credential (new API key, revoke old)
  3. Audit access logs: was old credential used after intended scope?
  4. Remove from git history (git filter-repo or BFG Repo Cleaner)
     → This requires force-push, notifying all contributors
     → NOT sufficient alone — rotation is the mandatory step
  5. Post-mortem: how did it get committed? Add pre-commit hook to prevent recurrence

PREVENTION:
  Pre-commit hook (gitleaks, detect-secrets)
  IDE plugins that warn before commit
  .gitignore covering .env, *.key, *.pem, appsettings.Production.json
  Use Azure Key Vault / AWS Secrets Manager — no secrets in config files
  Managed identities — no secrets at all for Azure resource access
```

---

## OWASP SAMM: Alternative Framework

OWASP Software Assurance Maturity Model provides a maturity model for secure SDLC (vs. SDL which is a prescriptive process):

```
OWASP SAMM DOMAINS AND PRACTICES

GOVERNANCE          DESIGN           IMPLEMENTATION   VERIFICATION   OPERATIONS
Strategy &          Threat           Secure           Architecture   IM&VM
Metrics             Assessment       Build            Assessment     Environment
Policy &            Security         Defect           Requirements-  Operational
Compliance          Requirements     Management       Driven Testing  Management
Education &         Security         Secure           Security       Incident
Guidance            Architecture     Deployment       Testing        Management

MATURITY LEVELS 0–3:
  0: No practice in place
  1: Ad hoc, some practice
  2: Defined, repeatable
  3: Optimized, measured

USE: SAMM is useful for measuring organizational maturity and creating
     a roadmap. SDL is useful for per-project process gates.
```

---

## Common Confusion Points

**"DevSecOps = just add a scan to the pipeline"**
DevSecOps is a cultural and process shift — security ownership is distributed to development teams, not centralized in a security team. Pipeline scans are a tool, not the practice. Developers need training, security champions, easy remediation paths, and security integrated into acceptance criteria.

**"SAST will catch everything"**
SAST has significant false positive rates (typically 20–80%) and misses runtime issues (logic flaws, configuration errors, issues that require execution context). SAST is one layer of a defense-in-depth strategy.

**"SBOM is only for compliance"**
SBOM is a practical incident response tool. When a zero-day hits a widely-used library, having a current SBOM lets you answer "which of our 200 services is affected?" in hours instead of days of manual inventory.

**"Removing a secret from git history is enough"**
Git history rewrite requires coordinating with all contributors, force-pushing, and invalidating all clones. But even with a perfect history rewrite, any clone or fork that existed during the window of exposure may still have the secret. Rotation is the only reliable remediation.

---

## Decision Cheat Sheet

| Security Activity | Phase | Tool/Method | Gate |
|-------------------|-------|-------------|------|
| Threat model | Design | Microsoft TM Tool | Required before design finalizes |
| SAST | Implement | CodeQL, Semgrep, Roslyn | Block PR on new HIGH+ |
| Secret scanning | Implement | GitHub Secret Scanning | Block push on detection |
| Dependency scanning | Implement | Dependabot, Snyk | Alert on new CVEs |
| Fuzz testing | Verify | libFuzzer, AFL | Required for network components |
| Container scanning | Build | Trivy, Defender | Block registry push on CRITICAL |
| SBOM generation | Build | syft, cdxgen | Attach to every artifact |
| IaC scanning | Implement | Checkov, TFSec | Block PR on misconfigurations |
| DAST | Verify | OWASP ZAP, Burp | Run on staging before release |
| FSR | Release | Manual review | Go/no-go gate |
