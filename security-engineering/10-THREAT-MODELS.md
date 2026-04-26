# Threat Models in Depth: Zero Trust, Authentication Ladders, Authorization Engines, Supply Chain

## Sentinel Context

This guide extends `01-THREAT-MODELING.md` (STRIDE/DREAD/PASTA) and `05-IDENTITY-ACCESS.md` (OAuth/OIDC/RBAC) by going deeper on the structural threat models that define modern security posture. Where those guides cover the *tools* (STRIDE categories, OAuth flows), this guide covers the *architectures* --- the end-to-end models for how trust is established, verified, and maintained across every layer of a system.

The Sentinel principle --- *no single point of trust* --- is the zero-trust thesis stated differently. This guide makes that architectural.

---

## The Big Picture

```
THREAT MODEL ARCHITECTURE — THE TRUST STACK
═══════════════════════════════════════════════════════════════════════

  ADVERSARY MODEL (who are you defending against?)
  ┌─────────────────────────────────────────────────────────────┐
  │ Nation-state    APT28/29, Lazarus, Hafnium                  │
  │ Cybercrime     Ransomware gangs, credential markets         │
  │ Supply chain   SolarWinds, codecov, event-stream            │
  │ Insider        Privileged user, disgruntled engineer        │
  │ Opportunistic  Script kiddies, automated scanners           │
  └──────────────────────────┬──────────────────────────────────┘
                             │
               "Defend against ALL of these with..."
                             │
                             ▼
  ARCHITECTURAL POSTURE (how do you structure defense?)
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  PERIMETER (legacy)           ZERO TRUST (modern)           │
  │  ┌───────────────────┐       ┌───────────────────┐          │
  │  │ Trust the network │       │ Trust nothing     │         │
  │  │ VPN = inside      │       │ Verify every      │         │
  │  │ Firewall = safe   │       │ request           │         │
  │  │ Internal = trusted│       │ Identity = the    │         │
  │  │                   │       │ new perimeter     │         │
  │  └───────────────────┘       └───────────────────┘         │
  │                                                             │
  └──────────────────────────┬──────────────────────────────────┘
                             │
                  "Implemented via..."
                             │
                             ▼
  CONTROL LAYERS
  ┌─────────────────────────────────────────────────────────────┐
  │ Authentication  │ Who are you?         (FIDO2, passkeys)    │
  │ Authorization   │ What can you do?     (OPA, Cedar, ReBAC)  │
  │ Supply Chain    │ What code do you run?(SLSA, Sigstore)     │
  │ Observability   │ What happened?       (SIEM, audit logs)   │
  └─────────────────────────────────────────────────────────────┘
```

---

## Part I: Zero-Trust Architecture

### The Death of the Perimeter

The perimeter model assumed a clear boundary: inside the firewall is trusted, outside is untrusted. This assumption broke irreparably when:

```
WHY PERIMETER SECURITY FAILED
┌──────────────────────────────┬──────────────────────────────────┐
│ Assumption                   │ Reality                          │
├──────────────────────────────┼──────────────────────────────────┤
│ Employees are on the LAN     │ Remote work, BYOD, contractors  │
│                              │ access from anywhere             │
├──────────────────────────────┼──────────────────────────────────┤
│ Internal traffic is trusted  │ Lateral movement after initial   │
│                              │ compromise (APT dwell time:      │
│                              │ median 16 days, Mandiant 2023)   │
├──────────────────────────────┼──────────────────────────────────┤
│ VPN grants full access       │ VPN + stolen credentials =       │
│                              │ full network access for attacker │
├──────────────────────────────┼──────────────────────────────────┤
│ Firewalls stop threats       │ Encrypted C2 channels traverse   │
│                              │ firewalls on port 443            │
├──────────────────────────────┼──────────────────────────────────┤
│ Apps are on-premises         │ SaaS, multi-cloud, hybrid.       │
│                              │ No single perimeter to defend.   │
└──────────────────────────────┴──────────────────────────────────┘

THE INCIDENT THAT CHANGED EVERYTHING:
  Google's "Operation Aurora" (2009):
  - APT (attributed to China) compromised Google's internal network
  - Moved laterally using internal trust relationships
  - Accessed Gmail accounts of human rights activists
  - Google's response: BeyondCorp (2011-2014)
```

### BeyondCorp: Google's Zero-Trust Implementation

Google's BeyondCorp is the original production zero-trust architecture. Published in a series of papers (2014-2016), it removed the concept of a privileged internal network.

```
BEYONDCORP ARCHITECTURE

  BEFORE (perimeter model):
  ┌─────────────────────────────────────────────┐
  │             CORPORATE NETWORK               │
  │   ┌──────┐  ┌──────┐  ┌──────┐            │
  │   │App 1 │  │App 2 │  │App 3 │            │
  │   └──────┘  └──────┘  └──────┘            │
  │                                             │
  │   All internal traffic trusted              │
  │   VPN = the only gate                       │
  └──────────────┬──────────────────────────────┘
                 │ VPN
  ┌──────────────┴──────────────────────────────┐
  │              INTERNET                       │
  └─────────────────────────────────────────────┘

  AFTER (BeyondCorp):
  ┌─────────────────────────────────────────────┐
  │              INTERNET                       │
  │   (no privileged network exists)            │
  └──────────────┬──────────────────────────────┘
                 │ HTTPS (every request)
                 ▼
  ┌──────────────────────────────────────────────┐
  │         ACCESS PROXY (policy enforcement)    │
  │                                              │
  │  For EVERY request, check:                   │
  │  ┌─────────────────────────────────────┐     │
  │  │ 1. User identity (SSO, MFA)         │     │
  │  │ 2. Device trust (certificate,       │     │
  │  │    patch level, encryption status)  │     │
  │  │ 3. Context (time, location, risk    │     │
  │  │    score, behavior anomaly)         │     │
  │  │ 4. Application policy (who can      │     │
  │  │    access this specific app?)       │     │
  │  └─────────────────────────────────────┘     │
  │                                              │
  │  Decision: ALLOW / DENY / STEP-UP MFA       │
  └──────────────┬──────────────────────────────┘
                 │
  ┌──────────────┴──────────────────────────────┐
  │   ┌──────┐  ┌──────┐  ┌──────┐            │
  │   │App 1 │  │App 2 │  │App 3 │            │
  │   └──────┘  └──────┘  └──────┘            │
  │   Apps do NOT trust the network.            │
  │   Every app requires authn + authz.         │
  └─────────────────────────────────────────────┘
```

**Key principle**: An employee sitting at their desk in a Google office gets the same access as an employee at a coffee shop. Network location grants zero additional trust.

### NIST SP 800-207: Zero Trust Architecture (2020)

NIST formalized zero trust into a reference architecture.

```
NIST SP 800-207 — ZERO TRUST TENETS

  1. All data sources and computing services are considered RESOURCES.
     (not just servers — every API, database, SaaS app, file share)

  2. All communication is secured REGARDLESS OF NETWORK LOCATION.
     (internal network traffic encrypted + authenticated, same as external)

  3. Access to individual enterprise resources is granted on a
     PER-SESSION basis.
     (no persistent "you're on the VPN so you can access everything")

  4. Access is determined by DYNAMIC POLICY.
     (user identity + device state + behavioral + environmental attributes)

  5. The enterprise monitors and measures the integrity and security
     posture of ALL owned and associated assets.
     (continuous, not one-time; devices and users continuously evaluated)

  6. All resource authentication and authorization are DYNAMIC and
     STRICTLY ENFORCED before access is allowed.
     (no cached decisions; re-evaluate on every request)

  7. The enterprise collects as much information as possible about
     the current state of assets, network, communications and uses
     it to improve security posture.
     (feedback loop: every decision informs the risk model)
```

### NIST Zero Trust Reference Architecture

```
NIST ZTA REFERENCE ARCHITECTURE

  ┌──────────┐            ┌────────────────────────┐
  │  Subject │            │  POLICY ENGINE (PE)    │
  │  (user + │            │  Decision point.       │
  │  device) │            │  Evaluates trust score │
  │          │            │  from all inputs.      │
  └────┬─────┘            └────────┬───────────────┘
       │                           │
       │ access request            │ grant/deny
       │                           │
       ▼                           ▼
  ┌────────────────────────────────────────────┐
  │      POLICY ENFORCEMENT POINT (PEP)        │
  │      (reverse proxy, API gateway, ZTNA)    │
  │                                            │
  │      Intercepts all requests.              │
  │      Consults PE for every request.        │
  │      Enforces the decision.                │
  └────────────────────┬───────────────────────┘
                       │ allowed traffic only
                       ▼
  ┌────────────────────────────────────────────┐
  │              RESOURCE                      │
  │      (application, API, database)          │
  └────────────────────────────────────────────┘

  TRUST INPUTS TO POLICY ENGINE:
  ┌────────────────────────────────────────────┐
  │ Identity Provider     → user identity      │
  │ Device Management     → device health/trust │
  │ Threat Intelligence   → known bad IPs/IOCs │
  │ SIEM / Analytics      → behavioral anomaly │
  │ Data Classification   → sensitivity level  │
  │ Activity Logs         → previous actions   │
  └────────────────────────────────────────────┘
```

### Azure AD Conditional Access (Microsoft's ZTA Implementation)

```
AZURE AD CONDITIONAL ACCESS — MICROSOFT'S ZERO TRUST

  CONDITION SIGNALS:                     POLICY DECISIONS:
  ┌──────────────────────┐              ┌──────────────────────┐
  │ User / group         │              │ Block access         │
  │ Cloud app or action  │              │ Grant access:        │
  │ Device platform      │─── POLICY ──>│   Require MFA        │
  │ Location (IP/named)  │              │   Require compliant  │
  │ Client app           │              │   device             │
  │ Sign-in risk (ML)    │              │   Require Intune     │
  │ User risk (ML)       │              │   managed app        │
  │ Device state         │              │   Require password   │
  └──────────────────────┘              │   change             │
                                        │   Session controls:   │
                                        │     App enforced      │
                                        │     restrictions      │
                                        │     MCAS in-session   │
                                        │     monitoring        │
                                        └──────────────────────┘

  EXAMPLE POLICIES (production):
  ┌────────────────────────────────────────────────────────────┐
  │ 1. All users → all cloud apps → require MFA                │
  │    (baseline: no access without MFA, period)               │
  │                                                            │
  │ 2. All users → Azure Management → require compliant device │
  │    (cannot manage Azure from an unmanaged machine)         │
  │                                                            │
  │ 3. Risky sign-in (medium+) → require password change + MFA│
  │    (ML detects: new location, impossible travel, tor exit) │
  │                                                            │
  │ 4. Guest users → specific apps only → session limit 1hr    │
  │    (vendors/contractors get scoped, time-limited access)   │
  │                                                            │
  │ 5. Service principals → from specific IPs only → grant     │
  │    (CI/CD service principal locked to GitHub runner IPs)   │
  └────────────────────────────────────────────────────────────┘

  SIGN-IN RISK SIGNALS (Azure AD Identity Protection):
  ┌────────────────────────────────────────────────────────────┐
  │ Impossible travel      Two logins from geographically      │
  │                        impossible locations within         │
  │                        the time window                     │
  │ Anonymous IP           Login from known VPN/Tor exit node  │
  │ Unfamiliar properties  Browser, OS, or location never      │
  │                        seen for this user before           │
  │ Malware-linked IP      IP associated with known botnet     │
  │ Leaked credentials     Credential found in dark web dump   │
  │ Password spray         Multiple failed logins across many  │
  │                        accounts from same IP               │
  └────────────────────────────────────────────────────────────┘
```

---

## Part II: Authentication Depth — The Phishing Resistance Ladder

Authentication has evolved through distinct generations, each addressing the failures of the previous one. The key metric is **phishing resistance** --- can an attacker trick a user into handing over their credential?

```
AUTHENTICATION EVOLUTION — THE PHISHING RESISTANCE LADDER

  PHISHING RESISTANCE
  ▲
  │
  │  ████████████████████  FIDO2 / Passkeys
  │  ████████████████████  (domain-bound, no shared secret,
  │  ████████████████████   hardware-backed, phishing-proof)
  │
  │  ██████████████████    Hardware security key (YubiKey)
  │  ██████████████████    (physical presence required,
  │  ██████████████████     FIDO U2F protocol)
  │
  │  ████████████████      App-based push (MS Authenticator number match)
  │  ████████████████      (phishing resistant IF number matching enabled;
  │  ████████████████       MFA fatigue attacks possible without it)
  │
  │  ██████████████        TOTP (Google Authenticator, Authy)
  │  ██████████████        (6-digit code, 30s window;
  │  ██████████████         phishable: user enters code on fake site)
  │
  │  ████████████          SMS OTP
  │  ████████████          (SIM swap attacks, SS7 interception,
  │  ████████████           phishable: attacker proxies code)
  │
  │  ██████████            Password only
  │  ██████████            (credential stuffing, phishing,
  │  ██████████             brute force, reuse across sites)
  │
  └──────────────────────────────────────────────────────> Time
       2000    2010    2013    2016    2019    2022    2024
```

### Password Authentication (and Why It Fails)

```
PASSWORD ATTACK SURFACE

  ATTACK                 DEFENSE                   EFFECTIVENESS
  ┌──────────────────────┬─────────────────────────┬────────────┐
  │ Credential stuffing  │ Unique passwords per    │ Moderate   │
  │ (reused passwords    │ site (password manager) │ (requires  │
  │ from breach dumps)   │                         │ user       │
  │                      │                         │ adoption)  │
  ├──────────────────────┼─────────────────────────┼────────────┤
  │ Phishing             │ URL inspection, security │ Low        │
  │ (fake login page)    │ training                 │ (humans    │
  │                      │                          │ are bad    │
  │                      │                          │ at this)   │
  ├──────────────────────┼─────────────────────────┼────────────┤
  │ Brute force          │ Rate limiting, lockout, │ High       │
  │                      │ Argon2id hashing        │            │
  ├──────────────────────┼─────────────────────────┼────────────┤
  │ Password spraying    │ Lockout with per-IP      │ Moderate   │
  │ (common passwords    │ tracking, Azure AD Smart │            │
  │ across many accounts)│ Lockout                  │            │
  ├──────────────────────┼─────────────────────────┼────────────┤
  │ Keylogging           │ OS-level security,      │ Low        │
  │                      │ endpoint detection      │ (defeats   │
  │                      │                          │ everything)│
  └──────────────────────┴─────────────────────────┴────────────┘

  THE FUNDAMENTAL PROBLEM WITH PASSWORDS:
  A password is a SHARED SECRET between the user and the server.
  Any attack that extracts the secret (phishing, breach, keylogger)
  gives the attacker the same access as the user.
  No amount of complexity requirements fixes this.
```

### FIDO2 / WebAuthn / Passkeys — Why They Are Phishing-Proof

```
FIDO2/WEBAUTHN PROTOCOL

  ┌──────────────────────────────────────────────────────────┐
  │  REGISTRATION (one-time setup)                           │
  │                                                          │
  │  Browser              Authenticator         Server       │
  │     │                    │                    │          │
  │     │<── challenge ──────────────────────────│           │
  │     │                    │                    │          │
  │     │── create(rp_id, ──>│                    │          │
  │     │   user, challenge) │                    │          │
  │     │                    │                    │          │
  │     │   Authenticator:   │                    │          │
  │     │   1. Generate keypair (pk, sk)          │          │
  │     │   2. Store sk bound to rp_id            │          │
  │     │   3. Sign challenge with sk             │          │
  │     │                    │                    │          │
  │     │<── (pk, signed  ───│                    │          │
  │     │    attestation)    │                    │          │
  │     │                    │                    │          │
  │     │── pk + attestation ────────────────────>│          │
  │     │                                    store pk        │
  └──────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────┐
  │  AUTHENTICATION (every login)                            │
  │                                                          │
  │  Browser              Authenticator         Server       │
  │     │                    │                    │          │
  │     │<── challenge + rp_id ──────────────────│           │
  │     │                    │                    │          │
  │     │── get(rp_id,  ────>│                    │          │
  │     │   challenge)       │                    │          │
  │     │                    │                    │          │
  │     │   Authenticator:   │                    │          │
  │     │   1. Look up sk for rp_id              │           │
  │     │   2. Verify user (biometric/PIN)       │           │
  │     │   3. Sign challenge with sk             │          │
  │     │                    │                    │          │
  │     │<── signed assertion│                    │          │
  │     │                    │                    │          │
  │     │── assertion ───────────────────────────>│          │
  │     │                                    verify with pk  │
  └──────────────────────────────────────────────────────────┘

  WHY IT IS PHISHING-PROOF:
  ┌──────────────────────────────────────────────────────────┐
  │ The authenticator binds the private key to the rp_id     │
  │ (Relying Party ID = the domain, e.g., "login.microsoft.com")│
  │                                                          │
  │ If the user visits a phishing site (evil-login.com):     │
  │   Browser sends rp_id = "evil-login.com"                 │
  │   Authenticator has NO key for "evil-login.com"          │
  │   Authentication FAILS silently — nothing to phish.      │
  │                                                          │
  │ The private key NEVER LEAVES the authenticator.          │
  │ There is NO shared secret that can be stolen.            │
  │ The server stores only the public key.                   │
  │ Even a server breach reveals nothing useful.             │
  └──────────────────────────────────────────────────────────┘
```

### Passkeys: FIDO2 for the Mass Market

```
PASSKEYS (2022+) — FIDO2 made consumer-friendly

  PROBLEM: FIDO2 security keys (YubiKey) require hardware purchase.
           ~$25-50 per key. Low consumer adoption.

  SOLUTION: Passkeys — FIDO2 credentials stored in platform
            authenticators (OS keychain, cloud-synced).

  PASSKEY STORAGE:
  ┌────────────────────────────────────────────────────────────┐
  │ Platform          Storage           Sync                   │
  ├────────────────────────────────────────────────────────────┤
  │ Apple             iCloud Keychain   Across Apple devices   │
  │ Google            Google Password   Across Android/Chrome  │
  │                   Manager                                  │
  │ Microsoft         Windows Hello     Across Windows devices │
  │ 1Password/Bitwarden  Vault         Cross-platform          │
  └────────────────────────────────────────────────────────────┘

  PASSKEYS vs. HARDWARE KEYS:
  ┌──────────────────┬──────────────────────┬──────────────────┐
  │                  │ Passkey (synced)     │ Hardware key     │
  │                  │                      │ (YubiKey)        │
  ├──────────────────┼──────────────────────┼──────────────────┤
  │ Phishing-proof   │ Yes (rp_id bound)   │ Yes              │
  │ Discoverable     │ Yes (autofill)      │ No (must insert) │
  │ Multi-device     │ Yes (cloud sync)    │ No (per key)     │
  │ Lost device      │ Recover from cloud  │ Need backup key  │
  │ Extraction risk  │ Cloud account       │ None (tamper-    │
  │                  │ compromise          │  resistant HW)   │
  │ Enterprise grade │ Depends on policy   │ Yes              │
  │ NIST AAL         │ AAL2               │ AAL3             │
  └──────────────────┴──────────────────────┴──────────────────┘

  ENTERPRISE POLICY:
  For sensitive operations (Azure admin, production access):
    → Require hardware security key (AAL3)
  For daily operations (email, Teams, Office):
    → Allow passkeys or push MFA (AAL2)
  For external contractors:
    → Require MFA, any method (AAL1+)
```

### MFA Fatigue Attacks and Number Matching

```
MFA FATIGUE ATTACK (2022 — Uber, Cisco, Twilio breaches)

  ATTACK:
  1. Attacker has stolen username + password (from phishing or breach)
  2. Attacker repeatedly triggers MFA push to victim's phone
  3. Victim gets dozens of "Approve sign-in?" notifications
  4. Victim eventually taps "Approve" (fatigue, confusion, annoyance)
  5. Attacker is in.

  DEFENSE — NUMBER MATCHING (Microsoft Authenticator):
  ┌────────────────────────────────────────────────────────────┐
  │ Login screen shows:  "Enter the number: 42"                │
  │ Phone prompt shows:  "What number is shown on screen?"     │
  │ User types: 42 → approved                                  │
  │                                                            │
  │ If attacker triggers login:                                │
  │ Attacker's screen shows: "Enter the number: 73"            │
  │ Victim's phone: "What number is shown on screen?"          │
  │ Victim does NOT see 73 → cannot approve                    │
  │ Attack fails.                                              │
  └────────────────────────────────────────────────────────────┘

  MICROSOFT MANDATED number matching for all Authenticator push
  notifications as of February 2023. This is the minimum viable
  push MFA posture. Plain "approve/deny" push is insecure.
```

---

## Part III: Authorization Models — RBAC, ABAC, ReBAC, Policy Engines

`05-IDENTITY-ACCESS.md` introduces these models. Here we go deeper into the architectural trade-offs and policy engines.

### Authorization Model Evolution

```
AUTHORIZATION MODEL EVOLUTION

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  ACL (1970s)     RBAC (1992)     ABAC (2005)    ReBAC     │
  │  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐│
  │  │ Per-      │   │ Role →   │   │ Policy   │   │ Graph   ││
  │  │ resource  │   │ Perms    │   │ evaluates│   │ of      ││
  │  │ list of   │──>│ User →   │──>│ subject, │──>│ relation││
  │  │ who can   │   │ Role     │   │ resource,│   │ ships   ││
  │  │ do what   │   │          │   │ env attrs│   │         ││
  │  └──────────┘   └──────────┘   └──────────┘   └─────────┘│
  │                                                             │
  │  EXPRESSIVENESS ──────────────────────────────────────>     │
  │  COMPLEXITY     ──────────────────────────────────────>     │
  │  AUDIT EASE     <──────────────────────────────────────     │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

### RBAC: Where It Works, Where It Breaks

```
RBAC — ROLE-BASED ACCESS CONTROL

  MODEL:  Subject ──has──> Role ──grants──> Permission ──on──> Resource

  EXAMPLE (Azure RBAC):
    Jane ──has──> Contributor ──grants──> Read,Write ──on──> RG-Production
    Bob  ──has──> Reader      ──grants──> Read       ──on──> RG-Production
    Ops  ──has──> Owner       ──grants──> *          ──on──> Subscription

  WHERE RBAC WORKS:
    - Stable organizational hierarchy
    - Well-defined role categories (Admin, Editor, Viewer)
    - Moderate number of resources (hundreds to low thousands)
    - Azure subscriptions, Kubernetes namespaces, GitHub repos

  WHERE RBAC BREAKS — ROLE EXPLOSION:
    "Jane can edit documents in Project Alpha but only view in Project Beta"
    → Need: Editor-Alpha, Viewer-Beta roles

    "Bob can approve expenses under $10K but not over"
    → Need: Approver-Under-10K role (RBAC cannot express conditions)

    "Any team member can edit their own team's data"
    → Need: TeamA-Editor, TeamB-Editor, TeamC-Editor...

    At scale (Google, Facebook): millions of resources, billions of
    relationship combinations → RBAC role count explodes exponentially.

  ROLE EXPLOSION METRICS:
    Small org (50 users, 20 apps):       ~30 roles   ← manageable
    Medium org (5,000 users, 200 apps):  ~500 roles  ← straining
    Large org (100K users, 1000 apps):   ~10K+ roles ← unmanageable

    When role count exceeds ~200, humans cannot reason about
    who has access to what. Audit becomes impossible.
    → Switch to ABAC or ReBAC.
```

### ABAC: Attribute-Based Access Control

```
ABAC — ATTRIBUTE-BASED ACCESS CONTROL

  MODEL: Access = Policy(subject_attrs, resource_attrs, env_attrs, action)

  EXAMPLE POLICY (in pseudo-code):
    ALLOW IF:
      subject.department == resource.owner_department
      AND subject.clearance >= resource.classification
      AND environment.time BETWEEN "09:00" AND "17:00"
      AND action IN ["read", "list"]

  ABAC ENABLES:
  ┌────────────────────────────────────────────────────────────────┐
  │ Dynamic conditions    "Only during business hours"             │
  │ Attribute matching    "Same department as resource owner"      │
  │ Risk-based            "If risk_score < 0.3"                    │
  │ Data classification   "If document is CONFIDENTIAL, require    │
  │                        clearance >= SECRET"                    │
  │ Context-aware         "If accessing from corporate network,    │
  │                        allow; else require MFA step-up"        │
  └────────────────────────────────────────────────────────────────┘

  ABAC CHALLENGES:
  ┌────────────────────────────────────────────────────────────────┐
  │ Policy complexity     Policies are programs. Programs have bugs.│
  │ Audit difficulty      "Who can access resource X?" requires    │
  │                       evaluating all policies against all      │
  │                       possible attribute combinations.         │
  │ Testing               Combinatorial explosion of test cases.   │
  │ Attribute management  Attributes must be accurate and current. │
  │                       Stale attributes = wrong access decisions.│
  └────────────────────────────────────────────────────────────────┘
```

### ReBAC: Relationship-Based Access Control (Google Zanzibar)

```
ReBAC — RELATIONSHIP-BASED ACCESS CONTROL

  MODEL: Access is a graph query.
         "Can user U perform action A on resource R?"
         = "Is there a path in the relationship graph from U to R
            through relations that grant action A?"

  ZANZIBAR TUPLE MODEL (Google, 2019):
    Stored as tuples: (object, relation, subject)

    Examples:
    (doc:budget.xlsx,  viewer,  user:jane)
    (doc:budget.xlsx,  editor,  group:finance-team)
    (group:finance-team, member, user:jane)
    (group:finance-team, member, user:bob)
    (folder:finance,   parent,  doc:budget.xlsx)
    (folder:finance,   viewer,  group:all-employees)

  PERMISSION EVALUATION:
    Check: can user:alice view doc:budget.xlsx?

    1. Direct: (doc:budget.xlsx, viewer, user:alice)? → NO
    2. Via group: alice ∈ group:finance-team?
       (group:finance-team, member, user:alice)? → NO
    3. Via folder: (folder:finance, parent, doc:budget.xlsx) → YES
       (folder:finance, viewer, group:all-employees) → YES
       alice ∈ group:all-employees? → YES
    4. RESULT: ALLOW (alice can view via folder inheritance)

  GRAPH TRAVERSAL:
    user:alice
         │
         │ member
         ▼
    group:all-employees
         │
         │ viewer
         ▼
    folder:finance
         │
         │ parent (viewer inherits)
         ▼
    doc:budget.xlsx ← ALLOW (viewer)
```

### Policy Engines: OPA/Rego and Cedar

```
POLICY ENGINE LANDSCAPE

  ┌─────────────────────────────────────────────────────────────┐
  │ Engine       │ Model │ Language │ Backed by │ Use case      │
  ├─────────────────────────────────────────────────────────────┤
  │ OPA          │ ABAC  │ Rego     │ CNCF      │ K8s, APIs,  │
  │ (Open Policy │       │ (Datalog │           │ Terraform,  │
  │  Agent)      │       │  variant)│           │ microservices│
  ├─────────────────────────────────────────────────────────────┤
  │ Cedar        │ ABAC+ │ Cedar    │ AWS       │ Amazon        │
  │              │ ReBAC │ (purpose │           │ Verified      │
  │              │       │  built)  │           │ Permissions   │
  ├─────────────────────────────────────────────────────────────┤
  │ SpiceDB      │ ReBAC │ Schema + │ AuthZed   │ Google Docs  │
  │              │       │ API      │           │ -style sharing│
  ├─────────────────────────────────────────────────────────────┤
  │ OpenFGA      │ ReBAC │ Schema + │ Auth0/Okta│ Document /    │
  │              │       │ API      │           │ resource      │
  │              │       │          │           │ sharing       │
  └─────────────────────────────────────────────────────────────┘
```

#### OPA / Rego Example

```
OPA (OPEN POLICY AGENT) — REGO POLICY EXAMPLE

  # Policy: only allow container images from approved registries
  package kubernetes.admission

  deny[msg] {
    input.request.kind.kind == "Pod"
    container := input.request.object.spec.containers[_]
    not startswith(container.image, "gcr.io/my-org/")
    not startswith(container.image, "docker.io/library/")
    msg := sprintf("container %s: image from unapproved registry",
                   [container.name])
  }

  # Policy: require resource limits on all containers
  deny[msg] {
    input.request.kind.kind == "Pod"
    container := input.request.object.spec.containers[_]
    not container.resources.limits.memory
    msg := sprintf("container %s: must set memory limit",
                   [container.name])
  }

  HOW OPA WORKS:
  ┌─────────┐     ┌──────────┐     ┌──────────┐
  │ Request │────>│ OPA      │────>│ Decision │
  │ (JSON)  │     │ Engine   │     │ allow/   │
  │         │     │ + Rego   │     │ deny     │
  └─────────┘     │ policies │     └──────────┘
                  └──────────┘
                       ▲
                  ┌────┴────┐
                  │ Data    │
                  │ (JSON)  │
                  │ roles,  │
                  │ config  │
                  └─────────┘

  DEPLOYMENT PATTERNS:
    Sidecar:   OPA runs as sidecar next to each service
    Library:   OPA compiled into application (Go only)
    Central:   OPA as shared decision service (REST API)
    K8s:       Gatekeeper (OPA + admission webhook)
```

#### Cedar (AWS)

```
CEDAR POLICY LANGUAGE (AWS)

  # Cedar is formally verified: policies always terminate,
  # and the semantics are mathematically proven correct.

  # Allow editors to update documents they own
  permit(
    principal in Group::"editors",
    action in [Action::"update", Action::"read"],
    resource in Folder::"shared"
  ) when {
    resource.owner == principal
  };

  # Deny access to classified documents without clearance
  forbid(
    principal,
    action,
    resource
  ) when {
    resource.classification == "SECRET" &&
    !(principal.clearance >= "SECRET")
  };

  CEDAR PROPERTIES:
  ┌──────────────────────────────────────────────────────────────┐
  │ Analyzable     Cedar policies can be statically analyzed:    │
  │                "Is there any input where this policy allows  │
  │                access to SECRET documents?"                  │
  │                                                              │
  │ Terminating    Every policy evaluation terminates (no loops) │
  │                                                              │
  │ Deterministic  Same input → same output, always              │
  │                                                              │
  │ Fast           Sub-millisecond evaluation (designed for      │
  │                inline authorization in every API call)       │
  └──────────────────────────────────────────────────────────────┘

  CEDAR vs. OPA/REGO:
  ┌────────────────────┬───────────────────┬────────────────────┐
  │                    │ Cedar             │ OPA / Rego         │
  ├────────────────────┼───────────────────┼────────────────────┤
  │ Language           │ Purpose-built,    │ Datalog-derived,   │
  │                    │ constrained       │ general-purpose    │
  ├────────────────────┼───────────────────┼────────────────────┤
  │ Formal verification│ Yes (proven sound)│ No                 │
  ├────────────────────┼───────────────────┼────────────────────┤
  │ Policy analysis    │ Built-in          │ Third-party tools │
  ├────────────────────┼───────────────────┼────────────────────┤
  │ Expressiveness     │ Intentionally     │ Turing-complete    │
  │                    │ limited (safe)    │ (powerful, risky)  │
  ├────────────────────┼───────────────────┼────────────────────┤
  │ Ecosystem          │ AWS (newer)       │ CNCF (mature)     │
  └────────────────────┴───────────────────┴────────────────────┘
```

---

## Part IV: Supply Chain Security

### The Supply Chain Attack Landscape

```
SUPPLY CHAIN ATTACK TAXONOMY

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  SOURCE CODE ATTACKS                                        │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │ Compromised developer account                         │  │
  │  │   → codecov (2021): attacker modified Bash Uploader   │  │
  │  │ Malicious commit to open-source dependency            │  │
  │  │   → event-stream (2018): npm package backdoored       │  │
  │  │ Typosquatting (publish malicious package with         │  │
  │  │   similar name: lodash → lodahs)                      │  │
  │  └───────────────────────────────────────────────────────┘  │
  │                                                             │
  │  BUILD SYSTEM ATTACKS                                       │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │ Compromised CI/CD pipeline                            │  │
  │  │   → SolarWinds (2020): build system injected backdoor │  │
  │  │     into signed Orion update                          │  │
  │  │ Tampered build environment / toolchain                │  │
  │  │   → XcodeGhost (2015): modified Xcode distributed     │  │
  │  │     through Chinese mirrors                           │  │
  │  └───────────────────────────────────────────────────────┘  │
  │                                                             │
  │  DEPENDENCY ATTACKS                                         │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │ Dependency confusion / substitution                   │  │
  │  │   → Alex Birsan (2021): published internal package    │  │
  │  │     names to public npm/PyPI. Package managers prefer │  │
  │  │     public over private → attacker code runs in CI.   │  │
  │  │ Abandoned package takeover                            │  │
  │  │   → ua-parser-js (2021): popular npm package          │  │
  │  │     compromised after maintainer account takeover     │  │
  │  └───────────────────────────────────────────────────────┘  │
  │                                                             │
  │  DISTRIBUTION ATTACKS                                       │
  │  ┌───────────────────────────────────────────────────────┐  │
  │  │ Registry compromise (PyPI, npm, Docker Hub)           │  │
  │  │ CDN compromise (serve tampered artifacts)             │  │
  │  │ Mirror poisoning (corrupted mirror serves bad package)│  │
  │  └───────────────────────────────────────────────────────┘  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

### SLSA Framework (Supply-chain Levels for Software Artifacts)

```
SLSA LEVELS (pronounced "salsa")
Developed by Google, adopted by OpenSSF.

  ┌────────────────────────────────────────────────────────────┐
  │ Level │ Description                     │ Protects Against │
  ├───────┼─────────────────────────────────┼──────────────────┤
  │   0   │ No guarantees                   │ Nothing          │
  │       │ (most open source today)        │                  │
  ├───────┼─────────────────────────────────┼──────────────────┤
  │   1   │ Build process documented        │ Accidental       │
  │       │ Provenance exists (unsigned)    │ tampering        │
  │       │ "We know how it was built"      │                  │
  ├───────┼─────────────────────────────────┼──────────────────┤
  │   2   │ Build service generates +       │ Tampering after  │
  │       │ signs provenance                │ build            │
  │       │ "Build service vouches for      │                  │
  │       │  how it was built"              │                  │
  ├───────┼─────────────────────────────────┼──────────────────┤
  │   3   │ Hardened build platform         │ Tampering        │
  │       │ Isolated, ephemeral builders    │ during build     │
  │       │ "Tamper-resistant build"        │ (SolarWinds      │
  │       │                                 │  -class)         │
  └───────┴─────────────────────────────────┴──────────────────┘

  SLSA PROVENANCE ATTESTATION (what it contains):
  {
    "builder": {
      "id": "https://github.com/actions/runner/v2.3"
    },
    "buildType": "https://slsa.dev/provenance/v1",
    "invocation": {
      "configSource": {
        "uri": "git+https://github.com/my-org/my-repo@refs/heads/main",
        "digest": { "sha1": "abc123..." },
        "entryPoint": ".github/workflows/build.yml"
      }
    },
    "materials": [
      {
        "uri": "pkg:npm/express@4.18.2",
        "digest": { "sha256": "def456..." }
      }
    ]
  }

  THIS ANSWERS:
    - WHO built it? (GitHub Actions runner v2.3)
    - FROM WHAT source? (git commit abc123 on main branch)
    - USING WHAT build recipe? (build.yml workflow)
    - WITH WHAT inputs? (express@4.18.2 with hash def456)
```

### Sigstore: Keyless Code Signing

```
SIGSTORE — KEYLESS SIGNING FOR OPEN SOURCE

  PROBLEM: Signing artifacts requires managing private keys.
           Key management is hard. Most open source does not sign.

  SIGSTORE SOLUTION: Ephemeral keys + transparency log.
    No long-lived keys to manage, lose, or have stolen.

  COMPONENTS:
  ┌──────────────────────────────────────────────────────────────┐
  │ Fulcio (CA)         Issues short-lived signing certificates  │
  │                     bound to OIDC identity (GitHub, Google)  │
  │                                                              │
  │ Rekor (log)         Immutable transparency log of all        │
  │                     signing events (append-only Merkle tree) │
  │                                                              │
  │ Cosign (tool)       CLI for signing + verifying containers,  │
  │                     blobs, and SBOM attestations             │
  └──────────────────────────────────────────────────────────────┘

  SIGNING FLOW:
  Developer              Fulcio (CA)        Rekor (log)     Registry
      │                     │                   │              │
      │── OIDC token ──────>│                   │              │
      │   (prove identity)  │                   │              │
      │                     │                   │              │
      │<── ephemeral cert ──│                   │              │
      │   (valid ~10 min)   │                   │              │
      │                     │                   │              │
      │── sign artifact ────────────────────────────────────>  │
      │                     │                   │              │
      │── record signing ───────────────────>   │              │
      │   event in Rekor    │              (immutable entry)   │
      │                     │                   │              │
      │   DISCARD private key (ephemeral)       │              │
      │                     │                   │              │

  VERIFICATION:
  Consumer                             Rekor (log)     Registry
      │                                    │              │
      │── pull artifact ──────────────────────────────>   │
      │<── artifact + signature ──────────────────────    │
      │                                    │              │
      │── verify:                          │              │
      │   1. Check signature with cert     │              │
      │   2. Check cert was valid at       │              │
      │      signing time (Rekor log)      │              │
      │   3. Check identity in cert        │              │
      │      matches expected signer       │              │
      │                                    │              │
```

### SBOM (Software Bill of Materials)

```
SBOM — WHAT'S IN YOUR SOFTWARE?

  An SBOM lists every component (direct + transitive) in a
  software artifact, with versions and hashes.

  FORMATS:
  ┌──────────────────────┬────────────────────────────────────┐
  │ SPDX                 │ ISO standard (ISO/IEC 5962:2021)   │
  │ (Linux Foundation)   │ Widely used in compliance          │
  ├──────────────────────┼────────────────────────────────────┤
  │ CycloneDX            │ OWASP standard. More security-     │
  │ (OWASP)              │ focused (VEX, vulnerability data)  │
  └──────────────────────┴────────────────────────────────────┘

  SBOM USE CASES:
  ┌────────────────────────────────────────────────────────────┐
  │ Vulnerability response  "We heard log4j is vulnerable.     │
  │                          Do we use it? Where?"             │
  │                          → Search SBOM: instant answer.    │
  │                                                            │
  │ License compliance      "Do we have any GPL dependencies   │
  │                          in our commercial product?"       │
  │                          → Search SBOM: instant answer.    │
  │                                                            │
  │ Procurement             Government (EO 14028) requires     │
  │                          SBOM for all software sold to     │
  │                          federal agencies.                 │
  └────────────────────────────────────────────────────────────┘

  EXECUTIVE ORDER 14028 (May 2021):
    US government requires SBOMs for all software purchased by
    federal agencies. This is driving SBOM adoption industry-wide.
    NIST guidance (SP 800-218): SSDF (Secure Software Development
    Framework) includes SBOM generation as a requirement.
```

### Dependency Confusion Attack — Detailed

```
DEPENDENCY CONFUSION — HOW IT WORKS

  SETUP:
    Your company uses internal packages (e.g., "my-company-utils")
    hosted on a private npm/PyPI registry.

  ATTACK:
    1. Attacker discovers internal package name
       (from leaked package.json, error messages, job postings)
    2. Attacker publishes "my-company-utils" v99.0.0 to PUBLIC npm
    3. Developer runs `npm install`
    4. npm resolves "my-company-utils":
       - Private registry: v2.3.1
       - Public npm: v99.0.0  ← higher version wins
    5. npm installs v99.0.0 from public registry
    6. Attacker's code runs in your CI/CD pipeline

  DEFENSE:
  ┌────────────────────────────────────────────────────────────┐
  │ 1. Scope packages       Use @my-company/utils (scoped)     │
  │                         Scoped packages can only be        │
  │                         published by scope owner           │
  │                                                            │
  │ 2. Pin registries       .npmrc: registry=https://private   │
  │                         Only allow specific registries     │
  │                                                            │
  │ 3. Lockfile integrity   npm ci (not npm install)           │
  │                         Lockfile pins exact versions +     │
  │                         integrity hashes                   │
  │                                                            │
  │ 4. Claim internal names Register internal package names    │
  │                         on public registry as placeholders │
  └────────────────────────────────────────────────────────────┘
```

---

## Old World → New World Bridges

### For Any Senior Engineer

| Old Security Posture | New Security Posture | Key Shift |
|---------------------|---------------------|-----------|
| Perimeter defense (firewall + VPN) | Zero-trust (identity + device + context) | Location no longer implies trust. Every request is verified. |
| Passwords + complexity rules | Passkeys / FIDO2 | Shared secrets replaced by public-key crypto. Phishing becomes structurally impossible. |
| ACLs on individual resources | Policy engines (OPA, Cedar) | Authorization logic externalized from application code. Policies are auditable, testable, deployable artifacts. |
| "We trust our build system" | SLSA + Sigstore + SBOM | Build provenance is cryptographically attested. SolarWinds-class attacks become detectable. |
| Role-based access (RBAC) | Relationship-based access (ReBAC) | Scales from "admin/editor/viewer" to Google-Docs-style sharing with millions of resources. |

### For the Microsoft / Azure / VSTS Background

| VSTS / Azure Era | Modern Equivalent | What Changed |
|-----------------|-------------------|--------------|
| VPN + Network Security Groups | Azure AD Conditional Access + Zero Trust | Network location is no longer a trust signal. Identity + device health + risk score is the decision input. |
| Active Directory on-prem (Kerberos + NTLM) | Azure AD / Entra ID (OAuth 2.0 + OIDC) | Protocol shift from Kerberos tickets to JWT tokens. Same concepts (authentication, authorization, token lifetime) but cloud-native. |
| VSTS service account with static password | Managed Identity (no credential) | Eliminated the "service account password in config" antipattern entirely. Token obtained from metadata service, auto-rotated. |
| VSTS build agent pulls from NuGet | GitHub Actions with SLSA provenance + Sigstore | Build artifacts now carry cryptographic attestation of how they were built. |
| SDL threat model (Microsoft TM Tool) | STRIDE + attack trees + automated SAST/DAST | Same STRIDE categories; now integrated into CI/CD pipeline rather than standalone SDL deliverable. |
| System Center Operations Manager (SCOM) alerts | Azure AD Identity Protection + SIEM | Risk-based authentication replaces static alerting. ML models detect impossible travel, credential spray, anomalous behavior. |

---

## Common Confusion Points

**"Zero trust means we don't trust anyone"**
Zero trust means we don't grant trust based on network location. Trust is still established --- through identity verification, device attestation, and continuous evaluation. The name is misleading; it should be "verify-everything trust" rather than "zero trust."

**"MFA solves phishing"**
TOTP and SMS MFA are phishable: the attacker proxies the MFA code in real-time through a fake login page. Only FIDO2/WebAuthn/passkeys are truly phishing-resistant because the credential is cryptographically bound to the legitimate domain. Push MFA with number matching is resistant but not proof --- the user must still verify the number.

**"RBAC is enough for enterprise authorization"**
RBAC works well for coarse-grained access (subscription, resource group, namespace). It breaks down for fine-grained, relationship-based access (document sharing, project membership, hierarchical permissions). The pattern in practice: RBAC for infrastructure, ReBAC or ABAC for application-level authorization.

**"SBOM is a compliance checkbox"**
An SBOM that is generated and filed away is useless. An SBOM that is queryable in real-time ("do any of our production services use log4j 2.14?") is a critical incident response capability. The value is in the query, not the document.

**"Supply chain attacks are rare"**
SolarWinds (2020), codecov (2021), ua-parser-js (2021), event-stream (2018), colors/faker (2022), xz-utils (2024). Supply chain attacks are increasing in frequency and sophistication. The xz-utils attack was a multi-year social engineering campaign to gain maintainer trust. Traditional security tools do not detect this class of threat --- only provenance verification (SLSA) and behavioral analysis can.

**"Conditional Access = MFA everywhere"**
MFA everywhere is the baseline, not the goal. Conditional Access evaluates risk signals (impossible travel, device compliance, user risk score) and applies proportional responses: block, allow, require MFA, require compliant device, limit session duration. The sophistication is in the signals and the proportional response, not just "require MFA."

---

## Decision Cheat Sheet

| Situation | Recommended Approach | Why |
|-----------|---------------------|-----|
| Greenfield enterprise architecture | Zero-trust from day 1 (NIST 800-207) | Retrofitting ZTA is 10x harder than building it in |
| Employee authentication | Passkeys (AAL2) + hardware keys for admins (AAL3) | Phishing resistance is the only metric that matters |
| Service-to-service authentication | Managed identity / workload identity federation | No static credentials to leak or rotate |
| Kubernetes admission control | OPA/Gatekeeper | CNCF standard, Rego policies are version-controlled |
| Application-level authorization (simple) | RBAC (Azure RBAC, K8s RBAC) | Sufficient for infra-level and small role sets |
| Application-level authorization (complex) | Cedar (AWS) or OPA for ABAC; SpiceDB/OpenFGA for ReBAC | Choose based on whether your model is attribute-driven or relationship-driven |
| Protecting the build pipeline | SLSA Level 2+ with Sigstore signing | Provenance + keyless signing = minimum viable supply chain security |
| Vulnerability response readiness | Generate SBOM in CI, store queryable | "Do we use log4j?" must be answerable in minutes, not days |
| Dependency management | Scoped packages, lockfile integrity, private registry isolation | Prevents dependency confusion and typosquatting |
| Conditional access policies | Start with "require MFA everywhere" then layer device compliance, risk-based, session limits | Progressive deployment: baseline MFA first, then sophistication |
| Legacy on-prem Active Directory | Hybrid with Azure AD Connect → migrate to cloud-native Entra ID | Kerberos/NTLM → OAuth/OIDC transition is the decade-long migration |
