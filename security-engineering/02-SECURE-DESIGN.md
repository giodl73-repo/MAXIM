# Secure Design Principles: Least Privilege, Defense in Depth, Zero Trust

## The Big Picture

Secure design principles are the axioms that should guide architecture and engineering decisions. They are not rules about specific technologies — they are principles that apply across all layers of a system.

```
SECURE DESIGN PRINCIPLES OVERVIEW
+-----------------------------------------------------------------------+
|                                                                       |
|  SALTZER & SCHROEDER (1975)          MODERN ADDITIONS                 |
|  +---------------------------------+ +-----------------------------+  |
|  | Economy of Mechanism           | | Zero Trust Architecture     |  |
|  | Fail-Safe Defaults             | | Supply Chain Security (SLSA)|  |
|  | Complete Mediation             | | Privacy by Design           |  |
|  | Open Design                    | | Shift Left                  |  |
|  | Separation of Privilege        | | Immutable Infrastructure    |  |
|  | Least Privilege                | |                             |  |
|  | Least Common Mechanism         | |                             |  |
|  | Psychological Acceptability    | |                             |  |
|  | Work Factor                    | |                             |  |
|  | Compromise Recording           | |                             |  |
|  +---------------------------------+ +-----------------------------+  |
|                                                                       |
|  ARCHITECTURAL PATTERNS                                               |
|  +----------------------------------------------------------------+   |
|  | Defense in Depth                                               |  |
|  | Zero Trust Network Access                                      |  |
|  | Attack Surface Reduction                                       |  |
|  | Secure Defaults                                                |  |
|  +----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

---

## Saltzer and Schroeder's 8 Design Principles (1975)

Jerome Saltzer and Michael Schroeder's 1975 paper "The Protection of Information in Computer Systems" defined the foundational principles. They remain as valid today as they were 50 years ago.

### 1. Economy of Mechanism (Keep It Simple)

> Keep the design of security mechanisms as simple and small as possible.

Every line of security-critical code is a line that can have a bug. Every configuration option is an option that can be misconfigured.

**Application**: Do not build custom cryptography. Use library functions (OpenSSL, .NET System.Security.Cryptography). Do not implement your own authentication — use OAuth 2.0 + OIDC. Fewer moving parts = smaller attack surface.

### 2. Fail-Safe Defaults

> Base access decisions on permission rather than exclusion. Default should be no access.

If the authorization check fails, default to deny — not permit. If a whitelist is incomplete, deny the unmatched request — do not fall through to allow.

```
WRONG:
  if (isAdmin) { allow }
  else if (isOwner) { allow }
  // else: falls through, allows by default ← vulnerability

CORRECT:
  if (isAdmin || isOwner) { allow }
  else { deny }  ← explicit default deny
```

**Azure RBAC**: Default is deny. You grant permissions; you don't revoke them from a default-allow state.

### 3. Complete Mediation

> Every access to every object must be checked for authority.

Do not cache authorization decisions unless you have a way to invalidate the cache when permissions change. Do not check authorization at the entry point and then bypass it internally.

**Anti-pattern**: Check auth at the API gateway, then call internal services without auth. An attacker who gains internal network access (or lateral movement from a compromised service) can call those internal services without authorization.

**Pattern**: Service-to-service calls should also be authenticated and authorized, even within a VNet. This is a core zero trust principle.

### 4. Open Design

> The design should not be secret. Security should not depend on the attacker not knowing the mechanism.

Security through obscurity is not security. If your security depends on an attacker not knowing your algorithm or protocol, it is fragile. Use publicly reviewed cryptographic algorithms and protocols.

**Kerckhoffs's principle** (1883, same idea): A cryptographic system should be secure even if everything about the system, except the key, is public knowledge.

**Application**: Use AES, RSA, TLS 1.3. Do not invent proprietary encryption. Do not use secret URL paths as the only access control.

### 5. Separation of Privilege

> A protection mechanism that requires two keys to unlock is more robust and flexible than one that allows access to the presenter of only a single key.

Require multiple conditions for sensitive operations:
- Two-person integrity for production deployments
- MFA for privileged access (not just password)
- Require both API key and IP allowlist for high-value endpoints

**Azure example**: Privileged Identity Management (PIM) — access to production requires approval from a second party + time-limited elevation.

### 6. Least Privilege

> Every program and every user of the system should operate using the least set of privileges necessary to complete the job.

This is the most commonly violated principle in practice.

```
LEAST PRIVILEGE IN PRACTICE

Application service accounts:
  WRONG:  Service account has db_owner or sysadmin
  CORRECT: Service account has SELECT on specific tables needed

Azure managed identities:
  WRONG:  Identity has Contributor on subscription
  CORRECT: Identity has Storage Blob Data Reader on specific storage account

Kubernetes pod RBAC:
  WRONG:  Pod runs as root with cluster-admin
  CORRECT: Pod runs as non-root user, specific ClusterRole with minimum verbs

Developer access:
  WRONG:  All developers have production DB read access
  CORRECT: Production access requires JIT elevation with approval and logging
```

### 7. Least Common Mechanism

> Minimize the amount of mechanisms common to more than one user and depended on by all users.

Shared mechanisms are shared attack surfaces. If one service's DB credentials are compromised, those credentials should not unlock other services' data.

**Application**: Separate credentials, separate databases, separate encryption keys per service. Do not share a single "master key" across all services.

### 8. Psychological Acceptability

> It is essential that the human interface be designed for ease of use, so that users routinely and automatically apply the protection mechanisms correctly.

Security mechanisms that are hard to use will be circumvented. If developers find the secure pattern too complex, they will find a workaround.

**Examples of acceptability failures**:
- Password complexity rules that lead to Post-it note passwords
- MFA that is bypassed because engineers share accounts to avoid the friction
- Certificate management so complex that engineers use self-signed certs everywhere

**Modern application**: Managed identities (no credential to manage), certificate auto-rotation, password managers — remove the friction of security so the secure path is the easy path.

### 9. Work Factor (Saltzer extended)

> Compare the cost of circumventing the mechanism with the resources of a potential attacker.

Choosing key sizes, algorithm iterations, password hashing work factors — balance computational cost (for the attacker) vs. performance (for the system). Argon2id parameters are tuned so brute-force is expensive; password checking is fast.

### 10. Compromise Recording (Saltzer extended)

> It is sometimes desirable to record that a compromise has occurred, even if it cannot be prevented.

Even if you cannot prevent every attack, ensure you can detect it after the fact. Non-repudiable audit logs, write-once storage for logs, alerting on anomalies.

---

## Zero Trust Architecture (NIST SP 800-207)

Zero trust (Forrester 2010, NIST formalized 2020) replaces the "castle and moat" perimeter model with "never trust, always verify."

### The Old Model vs. Zero Trust

```
OLD "CASTLE AND MOAT" MODEL:
  Internet  ─── Firewall ─── Internal Network
  (untrusted)               (trusted)
  "If you're inside the network, you're trusted"

  FAILURE MODE: Once attacker gets inside (VPN compromise, phishing,
  lateral movement), they have access to everything on the internal network

ZERO TRUST MODEL:
  Every request authenticated (user, device, service)
  Every request authorized (least privilege, every time)
  Every request inspected (data exfiltration prevention)
  No implicit trust based on network location
  "Assume breach" posture

ZERO TRUST TENETS (NIST SP 800-207):
  1. All data sources and services are resources
  2. All communication is secured regardless of network location
  3. Access is granted on a per-session basis
  4. Access policy determined by dynamic analysis of client,
     user identity, behavioral attributes
  5. No enterprise-owned infrastructure is inherently trusted
  6. Authentication and authorization are dynamic, strictly enforced
```

### Microsegmentation

```
OLD APPROACH (flat VNet):
  VNet 10.0.0.0/16: all services can talk to all services
  Compromised payment service → can reach all other services

MICROSEGMENTATION:
  Payment service subnet: 10.0.1.0/24
  Order service subnet:   10.0.2.0/24
  User service subnet:    10.0.3.0/24

  NSG rule: Payment ← Order (explicit allow, specific port)
  NSG rule: Payment → DB (explicit allow)
  All other: DENY by default

  Compromised payment service → cannot reach user service,
  cannot reach order DB, cannot reach admin subnet
```

### Continuous Validation

Zero trust does not authenticate once at login and trust forever. It continuously validates:
- Token expiry and rotation (short-lived tokens preferred)
- Device compliance (MDM policy: patch level, encryption, certificate)
- Behavioral analysis (unusual access time, volume, pattern → step-up auth)
- Conditional access policies (Azure AD Conditional Access, Entra ID)

---

## Defense in Depth

Defense in depth places multiple independent security controls at each layer, so that bypass of one control does not compromise the system.

```
DEFENSE IN DEPTH LAYERS

Attacker → [Physical] → [Network] → [Perimeter] → [Compute] →
             Physical     DDoS        WAF/FW         EDR
             access       protection  TLS             Antivirus
             controls     Firewall    NGFW            Patch mgmt
                          rules                       Hardening

→ [Application] → [Data] → [Identity]
   Input valid.   Encrypt   MFA
   SAST/DAST      at rest   RBAC/ABAC
   OWASP Top10   Mask PII   PAM
   Rate limit    DLP        Audit logs
```

No single layer is assumed to be impenetrable. Multiple independent controls mean an attacker must bypass all layers to succeed.

---

## SLSA: Supply Chain Security

SLSA (Supply-chain Levels for Software Artifacts, pronounced "salsa") is a framework for hardening the software build pipeline against tampering.

```
SLSA LEVELS

LEVEL 0: No guarantees
  Build process not documented, no audit trail

LEVEL 1: Documentation of build process
  Build scripts in version control
  Provenance (metadata about how artifact was built) generated

LEVEL 2: Tamper resistance of build service
  Hosted build service (e.g., GitHub Actions)
  Signed provenance from the build service
  → Attacker would need to compromise build service to tamper

LEVEL 3: Extra resistance to specific threats
  Hardened build platform
  Non-falsifiable provenance (build platform attests artifact)
  Two-party review for source changes

LEVEL 4: Two-person review + hermetic reproducible builds
  Hermetic: build is fully isolated, same inputs always same outputs
  Reproducible: anyone can verify the binary matches the source
  → Even if build service is compromised, tampered artifact detected

SUPPLY CHAIN ATTACKS IN THE WILD:
  SolarWinds (2020): attacker injected backdoor into build pipeline
  event-stream (npm, 2018): maintainer added malicious code to popular package
  3CX (2023): supply chain attack via infected upstream dependency
  → SLSA Level 3+ would have detected these via provenance verification
```

---

## Secure Defaults vs. Opt-In Security

```
OPT-IN SECURITY (wrong approach):
  API is public by default, auth is optional
  Data is unencrypted by default, encryption is a configuration option
  All ports open by default, security rules are added on request

SECURE DEFAULTS (correct):
  API requires auth by default; anonymous access requires explicit allowlist
  Data is encrypted at rest by default; disabling requires override + justification
  All ports closed by default; access rules are additive
  Logging is on by default; disabling requires explicit opt-out

AZURE DEFAULTS (improving over time):
  Storage accounts: HTTPS-only and TLS 1.2 minimum enforced by default
  Azure SQL: TDE (Transparent Data Encryption) on by default
  Azure VMs: disk encryption on by default (managed disks)
  App Service: HTTPS redirect by default
  BUT: Many older services still default to less-secure settings for
       backward compatibility → always check Defender for Cloud score
```

---

## Common Confusion Points

**"Zero trust means no VPN"**
Zero trust replaces the VPN as the security boundary, but it doesn't mean there is no perimeter. It means the perimeter is identity-and-device-based rather than network-location-based. ZTNA (Zero Trust Network Access) solutions replace VPN while enforcing per-application, per-session authorization.

**"Least privilege is too much overhead"**
The overhead of implementing least privilege is paid once. The overhead of recovering from a breach caused by over-privileged accounts is paid repeatedly. Use automation (Azure Policy, Infrastructure as Code) to enforce least privilege at scale.

**"Open design means publish your source code"**
Open design means your security does not depend on hiding the mechanism. Closed-source software can still follow open design principles — they just must not rely on "nobody knows how we encrypt" as a security control.

---

## Decision Cheat Sheet

| Design Decision | Principle |
|-----------------|-----------|
| Default access for new API | Fail-safe defaults (deny) |
| Service account permissions | Least privilege |
| Auth check placement | Complete mediation (every layer) |
| Encryption algorithm choice | Open design (use reviewed algorithms) |
| Production deployment gate | Separation of privilege (two-person) |
| Architecture with many shared keys | Least common mechanism |
| Making MFA not annoying | Psychological acceptability |
| Build pipeline security | SLSA supply chain framework |
| Network architecture | Defense in depth + microsegmentation |
| Trust of internal services | Zero trust (never trust, always verify) |
