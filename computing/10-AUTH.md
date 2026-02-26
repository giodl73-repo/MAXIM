# Auth & Security — A Layered Guide

## The Big Picture

Auth has two distinct problems that are often conflated. Get the distinction clear first — everything else follows from it.

```
+------------------------------------------------------------------+
|                    AUTH LANDSCAPE                                |
|                                                                  |
|  AUTHN (Authentication)          AUTHZ (Authorization)          |
|  "Who are you?"                  "What can you do?"             |
|  ------------------              -------------------------       |
|  Verify identity                 Enforce permissions            |
|  Login / credential check        Role checks, scopes            |
|  Sessions, tokens, certs         RBAC, ABAC, policies           |
|                                                                  |
|  PROTOCOLS / STANDARDS                                           |
|  ----------------------                                          |
|  OAuth 2.0     Authorization framework (not AuthN!)             |
|  OIDC          Identity layer on top of OAuth2 (adds AuthN)     |
|  SAML          Enterprise SSO (XML-based, older, still alive)   |
|  JWT           Token format (used by OAuth2/OIDC)               |
|                                                                  |
|  STORAGE MODELS                                                  |
|  --------------                                                  |
|  Sessions      Server stores state. Client holds session ID.    |
|  Tokens (JWT)  Server stateless. Client holds signed token.     |
|                                                                  |
|  PROVIDERS (managed auth services)                               |
|  ----------------------------------                              |
|  Auth0    Clerk    NextAuth.js    Supabase    Azure Entra ID     |
+------------------------------------------------------------------+
```

**Bridge from .NET**: You know this domain from the server side — Windows Auth, ADFS, Azure AD, Claims Identity, `[Authorize]`, WCF WS-Security. The concepts are identical. The protocols (OAuth2, OIDC, JWT) are the open standards that replaced proprietary Microsoft stack — and that Microsoft itself adopted. Entra ID IS an OIDC provider.

### Kerberos / NTLM → OAuth2 / OIDC Bridge

OAuth2's authorization code flow is architecturally isomorphic to Kerberos. The mental model transfers directly:

```
  KERBEROS (Windows Auth)          OAuth2 AUTHORIZATION CODE FLOW
  -----------------------          ------------------------------
  Client authenticates to KDC      User redirects to Authorization Server
  (Key Distribution Center)        (Google, GitHub, Azure Entra)

  KDC issues Ticket-Granting       Auth Server issues authorization code
  Ticket (TGT) — short-lived,      — short-lived, single-use,
  cryptographically signed         cryptographically bound (PKCE)

  Client presents TGT to KDC       Client exchanges auth code at
  to request Service Ticket        token endpoint for access_token
  for a specific resource

  Client presents Service Ticket   Client presents access_token in
  to Resource Server               Authorization: Bearer header
  (e.g., file server)              to Resource Server (API)

  Resource Server verifies         Resource Server verifies JWT
  ticket with KDC (or locally      signature (no network call for
  if it has the session key)       RS256 — just verifies with public key)

  KEY STRUCTURAL SIMILARITY:
  Both involve a trusted third party (KDC / Auth Server).
  Both issue short-lived tickets/tokens that prove identity.
  Both let resource servers verify without storing credentials.
  Both support delegation (service-to-service).

  KEY DIFFERENCES:
  Kerberos is intranet-only (requires KDC reachability).
  OAuth2 is cross-domain by design — works over the public internet.
  Kerberos tickets are binary, encrypted, Kerberos-specific.
  OAuth2 tokens are JWTs — base64 JSON, signed, human-readable.
  PKCE replaces Kerberos's session key exchange for public clients.
  OAuth2 has explicit consent model; Kerberos is transparent (SSO).

  NTLM is a different lineage entirely — challenge-response, no
  redirect, no third party, connection-based. There is no modern
  web equivalent; OAuth2/OIDC descends from the Kerberos model
  (trusted third-party ticket), not NTLM.
```

---

## Sessions vs Tokens — The Fundamental Choice

### Session-Based Auth (Stateful)

```
  LOGIN:
  Browser                          Server
  -------                          ------
  POST /login { email, password }
                              -->  Verify credentials
                                   Create session in DB/Redis:
                                   sessions["abc123"] = { userId: 1, role: "admin" }
                              <--  Set-Cookie: sessionId=abc123; HttpOnly; Secure

  SUBSEQUENT REQUESTS:
  Cookie: sessionId=abc123    -->  Look up sessions["abc123"]
                                   Found: { userId: 1, role: "admin" }
                                   Authorize request
                              <--  Response

  LOGOUT:
  POST /logout                -->  DELETE sessions["abc123"]
                              <--  Clear-Cookie

  CHARACTERISTICS:
  + Instant revocation (delete the session)
  + Small cookie payload (just an opaque ID)
  + Server controls session lifetime
  - Server must store sessions (memory/Redis/DB)
  - Horizontal scaling requires shared session store
  - Doesn't work well for APIs consumed by non-browsers
```

### Token-Based Auth (Stateless)

```
  LOGIN:
  Browser                          Server
  -------                          ------
  POST /login { email, password }
                              -->  Verify credentials
                                   Sign JWT: { userId: 1, role: "admin", exp: ... }
                              <--  { accessToken: "eyJ...", refreshToken: "..." }

  SUBSEQUENT REQUESTS:
  Authorization: Bearer eyJ...-->  Verify JWT signature (no DB lookup!)
                                   Decode claims: { userId: 1, role: "admin" }
                                   Authorize request
                              <--  Response

  LOGOUT:
  Client deletes token             Server does nothing
  (stateless — server has no record to delete)

  CHARACTERISTICS:
  + Server stateless — no session store needed
  + Scales horizontally (any server can verify any token)
  + Works for APIs, mobile, microservices
  - Can't revoke tokens before expiry (without a blocklist)
  - If stolen: valid until expiry
```

---

## JWT — JSON Web Tokens

The dominant token format. Three base64url-encoded parts separated by dots.

```
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9
  .
  eyJ1c2VySWQiOjEsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcwODU5NDgwMCwiZXhwIjoxNzA4NTk4NDAwfQ
  .
  [signature]

  PART 1: Header
  { "alg": "RS256", "typ": "JWT" }

  PART 2: Payload (claims)
  {
    "sub": "1",                       subject (user ID)
    "email": "alice@example.com",
    "role": "admin",
    "iat": 1708594800,                issued at (Unix timestamp)
    "exp": 1708598400,                expires at
    "iss": "https://auth.myapp.com",  issuer
    "aud": "https://api.myapp.com"    audience
  }

  PART 3: Signature
  RSASHA256(base64(header) + "." + base64(payload), privateKey)

  IMPORTANT: The payload is BASE64 ENCODED, NOT ENCRYPTED.
  Anyone can read a JWT's claims. Do not put secrets in JWTs.
  The signature only proves the token wasn't tampered with.
```

### Signing Algorithms

```
  HS256 (HMAC-SHA256)     Symmetric. Same secret signs and verifies.
                          Simple. Only for single-service use.
                          If the secret leaks → all tokens forgeable.

  RS256 (RSA-SHA256)      Asymmetric. Private key signs. Public key verifies.
                          Any service can verify without the private key.
                          Standard for OAuth2/OIDC providers.
                          Azure Entra, Auth0, Google all use RS256.

  ES256 (ECDSA-SHA256)    Asymmetric. Smaller keys than RSA. More modern.

  Use RS256 or ES256 for any token verified by multiple services.
  Use HS256 only for simple single-server scenarios.
```

### JWT in Node.js

```typescript
  import jwt from 'jsonwebtoken'

  // SIGN (on login)
  const token = jwt.sign(
    { userId: user.id, role: user.role },
    process.env.JWT_SECRET!,
    { expiresIn: '1h', issuer: 'myapp', audience: 'myapp-api' }
  )

  // VERIFY (on each request)
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET!, {
      algorithms: ['HS256'],   // always specify — prevents "none" attack
      issuer: 'myapp',
      audience: 'myapp-api'
    }) as { userId: number; role: string }
  } catch (err) {
    // TokenExpiredError, JsonWebTokenError
    res.status(401).json({ error: 'Invalid token' })
  }
```

### Access Tokens + Refresh Tokens

```
  ACCESS TOKEN          SHORT-LIVED (15min - 1hr)
  Sent with every API request.
  Stateless verification.
  If stolen: expires soon.

  REFRESH TOKEN         LONG-LIVED (days - weeks)
  Stored in HttpOnly cookie.
  Used ONLY to get new access tokens.
  Rotated on use (old refresh token invalidated on server).
  CAN be revoked because it's tracked server-side.

  FLOW:
  1. Login → access token (1hr) + refresh token (30 days, HttpOnly cookie)
  2. Use access token for API calls
  3. Access token expires → POST /auth/refresh with refresh cookie
  4. Server validates refresh token, issues new access + refresh tokens
  5. Logout → server invalidates refresh token
  6. Access token still technically valid for up to 1hr after logout
     (acceptable trade-off for stateless scaling)
```

---

## OAuth 2.0

OAuth2 is an **authorization framework** — not an authentication protocol. It lets users grant third-party apps limited access to their data without sharing their password.

```
  THE PROBLEM OAUTH2 SOLVES:

  Without OAuth2:
  "Sign in with Google" = give us your Google password. No.

  With OAuth2:
  App redirects to Google. You log in there (app never sees password).
  You consent to specific scopes ("read your email").
  Google gives the app a scoped token. App uses it. Nothing else.

  ROLES:
  Resource Owner    You (the user)
  Client            The app requesting access
  Authorization     Google / GitHub / Azure Entra (identity provider)
  Server
  Resource Server   Gmail API / GitHub API (where data lives)
```

### Authorization Code Flow + PKCE

The correct flow for web and mobile apps.

```
  YOUR APP           BROWSER           AUTH SERVER
  --------           -------           -----------

  1. Generate code_verifier (random)
     code_challenge = SHA256(code_verifier)

  2. Redirect browser:
     https://accounts.google.com/o/oauth2/auth
       ?client_id=YOUR_ID
       &redirect_uri=https://yourapp.com/callback
       &response_type=code
       &scope=openid email profile
       &code_challenge=abc123
       &code_challenge_method=S256

                      3. User logs in, consents to scopes

                      4. Auth server redirects to callback:
                         /callback?code=AUTH_CODE

  5. Exchange code for tokens (server-to-server):
     POST /token
       code=AUTH_CODE
       code_verifier=ORIGINAL_VERIFIER  ← proves you started flow
       client_secret=YOUR_SECRET

                      6. Returns: { access_token, refresh_token, id_token }

  7. Store tokens. User is authenticated.
```

**Why PKCE exists — the threat model**: PKCE (Proof Key for Code Exchange, RFC 7636) was designed to prevent authorization code interception attacks. Without PKCE:

```
  WITHOUT PKCE:
  Attacker registers a malicious app with the same redirect_uri,
  or intercepts the redirect at the OS level (mobile deep link hijack).

  Auth server sends:  /callback?code=AUTH_CODE
  Attacker intercepts: gets AUTH_CODE
  Attacker POSTs:      /token { code: AUTH_CODE, client_id: ... }
  Auth server:         ✓ valid code → issues access_token to attacker

  The auth code alone is enough to get tokens.

  WITH PKCE:
  1. Legitimate client generates code_verifier (random, ≥43 chars)
     and sends code_challenge = SHA256(code_verifier) at step 1.

  2. Attacker intercepts AUTH_CODE at step 4 — same as before.

  3. Attacker POSTs: /token { code: AUTH_CODE, client_id: ... }
     Auth server:    "Where's the code_verifier?"
     Attacker:       doesn't have it (was never transmitted)
     Auth server:    ✗ rejects the exchange

  The code_verifier was never sent over the wire — only its hash
  (code_challenge) was. Intercepting the auth code is useless
  without the original verifier that only the legitimate client holds.

  Auth server checks: SHA256(verifier_submitted) == challenge_stored
  This check is unforgeable without the original verifier.

  PKCE is now required for all public clients (SPAs, mobile apps)
  and recommended for confidential clients (server-side apps) too.
```

### Client Credentials Flow

Machine-to-machine. No user involved.

```
  SERVICE A                           AUTH SERVER
  ---------                           -----------
  POST /token
    grant_type=client_credentials
    client_id=service-a
    client_secret=secret
    scope=read:orders
                                  --> Verify credentials
                                  <-- { access_token, expires_in }

  SERVICE A → SERVICE B:
  GET /orders
  Authorization: Bearer eyJ...

  SERVICE B verifies JWT. No browser. No user.
  This is how Azure service principals work.
  Same concept, now standardized as OAuth2.
```

### Device Authorization Flow

For devices that cannot launch a browser (CLI tools, IoT, smart TVs, Azure CLI, GitHub CLI). Defined in RFC 8628.

```
  THE PROBLEM:
  A CLI tool or IoT device can't do a browser redirect.
  The user can't type a URL and password into a terminal easily.

  DEVICE FLOW (RFC 8628):

  CLI / DEVICE              AUTH SERVER          USER'S BROWSER
  -----------               -----------          --------------

  1. POST /device/code
     client_id=CLI_APP
     scope=read:repos
                        --> Returns:
                            device_code = "GmRh...long opaque..."
                            user_code   = "WDJB-MJHT"  ← short, human-readable
                            verification_uri = "https://github.com/login/device"
                            expires_in  = 900 (15 min)
                            interval    = 5   (poll every 5s)

  2. Show user:
     "Open https://github.com/login/device
      and enter code: WDJB-MJHT"

  3. Start polling:                4. User opens browser,
     POST /token                      enters WDJB-MJHT,
       grant_type=device_code         logs in, approves.
       device_code=GmRh...
       client_id=CLI_APP
                        <-- "authorization_pending"  (keep polling)
                        <-- "authorization_pending"  (keep polling)
                        <-- { access_token, refresh_token }  ← user approved!

  5. CLI has tokens. Proceed.

  SECURITY NOTES:
  - user_code is intentionally short (8 chars) so users can verify
    they're approving the right session — helps against phishing
  - device_code is long and opaque — never shown to user
  - polling interval (5s) enforced by server to prevent brute force
  - expires_in bounds the attack window if user_code is intercepted

  REAL EXAMPLES:
  GitHub CLI:    gh auth login  → opens github.com/login/device
  Azure CLI:     az login       → opens microsoft.com/devicelogin
  Google:        gcloud auth login --no-launch-browser
```

The device flow is in your daily tooling. `az login` and `gh auth login` both use it. The key design insight: the device never handles credentials. It just polls. The auth happens entirely in the user's browser on a trusted device — the CLI cannot intercept it.

---

## OpenID Connect (OIDC)

OIDC = OAuth2 + identity. OAuth2 grants access. OIDC tells you *who the user is*.

```
  OAuth2 gives you: access_token (permission to access resources)
  OIDC adds:        id_token (JWT with user identity claims)

  id_token payload:
  {
    "sub": "10769150350006150715113082367",  ← stable unique user ID
    "email": "alice@gmail.com",
    "name": "Alice Smith",
    "picture": "https://...",
    "iss": "https://accounts.google.com",
    "aud": "YOUR_CLIENT_ID",
    "exp": 1708598400
  }

  OIDC SCOPES:
  openid          Required. Signals OIDC. Returns id_token.
  email           Include email.
  profile         Include name, picture, locale.
  offline_access  Request refresh token.

  PROVIDERS YOU KNOW:
  Azure Entra ID  → OIDC provider. Full OIDC compliance.
  ADFS            → Older. WS-Fed + SAML + OIDC (newer versions).
  Azure AD B2C    → Consumer identity. OIDC + custom user flows.
```

---

## Token Storage — The Security Trade-Off

```
  OPTION 1: localStorage
  ----------------------
  Easy JS access: localStorage.getItem('token')

  RISK: XSS. Any compromised JS on your page can steal the token.
  npm package with malicious code, CDN injection, your own XSS bug.
  Token silently exfiltrated to attacker's server.

  OPTION 2: HttpOnly Cookie
  -------------------------
  Set-Cookie: token=eyJ...; HttpOnly; Secure; SameSite=Strict

  HttpOnly = JavaScript CANNOT read this cookie. Period.
  XSS is neutralized for token theft.

  RISK: CSRF. But SameSite=Strict blocks cross-site requests.
  Modern browsers (2020+): SameSite=Lax is the default.

  RECOMMENDATION:
  Access token  → in-memory JS variable (lost on refresh, that's OK)
  Refresh token → HttpOnly; Secure; SameSite=Strict cookie
  Let your auth library (NextAuth, Clerk) make this decision.
```

---

## Auth Providers

Building auth from scratch is an invitation for subtle security bugs. Use a provider.

```
  +------------+--------------------------------------------------+
  | Provider   | Notes                                            |
  +------------+--------------------------------------------------+
  | Auth0      | Mature, full-featured, enterprise-grade.         |
  |            | Free tier. Okta-owned. OIDC compliant.           |
  +------------+--------------------------------------------------+
  | Clerk      | Best DX. Prebuilt React components.              |
  |            | Next.js integration excellent. Organizations.    |
  +------------+--------------------------------------------------+
  | NextAuth.js| Open source. Runs in your app. Own your data.   |
  | (Auth.js)  | 50+ OAuth providers. JWT or DB sessions.         |
  +------------+--------------------------------------------------+
  | Supabase   | Postgres + auth bundle. JWT + RLS integration.   |
  +------------+--------------------------------------------------+
  | Azure      | Enterprise SSO. M365 integration. You know it.  |
  | Entra ID   | Use for internal tools and corporate identity.   |
  +------------+--------------------------------------------------+
```

### NextAuth.js Pattern (Next.js App Router)

```typescript
  // auth.ts
  import NextAuth from 'next-auth'
  import GitHub from 'next-auth/providers/github'
  import MicrosoftEntraID from 'next-auth/providers/microsoft-entra-id'
  import { PrismaAdapter } from '@auth/prisma-adapter'

  export const { handlers, auth, signIn, signOut } = NextAuth({
    adapter: PrismaAdapter(prisma),
    providers: [
      GitHub({
        clientId: process.env.GITHUB_ID!,
        clientSecret: process.env.GITHUB_SECRET!,
      }),
      MicrosoftEntraID({
        clientId: process.env.AZURE_AD_CLIENT_ID!,
        clientSecret: process.env.AZURE_AD_CLIENT_SECRET!,
        tenantId: process.env.AZURE_AD_TENANT_ID!,
      }),
    ],
    callbacks: {
      session({ session, user }) {
        session.user.id = user.id
        return session
      }
    }
  })

  // app/api/auth/[...nextauth]/route.ts
  export { handlers as GET, handlers as POST }

  // Server component — protect a page
  const session = await auth()
  if (!session) redirect('/login')

  // API route — protect an endpoint
  const session = await auth()
  if (!session) return Response.json({ error: 'Unauthorized' }, { status: 401 })
```

---

## Key Security Attacks

```
  XSS (Cross-Site Scripting)
  --------------------------
  Attacker injects JS into your page. Reads tokens, calls APIs.
  Prevention:
  - HttpOnly cookies (JS can't read them)
  - Content Security Policy headers
  - React/Vue auto-escape output (don't use dangerouslySetInnerHTML)
  - Sanitize user HTML with DOMPurify

  CSRF (Cross-Site Request Forgery)
  ---------------------------------
  Malicious site triggers authenticated request via browser cookie.
  Prevention:
  - SameSite=Strict on cookies (modern browsers block cross-site)
  - CSRF tokens for non-SameSite scenarios
  - Check Origin/Referer header on state-changing requests

  JWT NONE ALGORITHM ATTACK
  -------------------------
  Attacker sets alg:"none", removes signature. Vulnerable libs accept it.
  Prevention:
  - Always specify: jwt.verify(token, secret, { algorithms: ['RS256'] })

  TOKEN THEFT
  -----------
  Stolen token used from attacker's machine.
  Prevention:
  - Short access token expiry (15-60 min)
  - Refresh token rotation + reuse detection
  - HttpOnly cookies (XSS can't read them)

  AUTH CODE INTERCEPTION (without PKCE)
  -------------------------------------
  Attacker intercepts authorization code at redirect.
  Exchanges it for tokens before legitimate client can.
  Prevention:
  - PKCE (required for public clients, recommended for all)
  - The code_verifier was never transmitted, so interception is useless
```

---

## Common Confusion Points

### "OAuth2 is an authentication protocol"

```
  No. OAuth2 = authorization. "What can this app do?"
  OIDC = authentication. "Who is this user?"

  When you "Sign in with Google" you're using OIDC.
  Google implements OIDC on top of OAuth2.
  The id_token is OIDC. The access_token is OAuth2.
```

### "The JWT payload is encrypted"

```
  No. Base64-encoded, not encrypted.
  Anyone with the token can decode and read the claims.
  The signature prevents tampering, not reading.

  Don't put secrets, PII beyond what's necessary, or
  sensitive business data in JWT payloads.
  Put only what the server needs: userId, role, scopes.

  If you need confidentiality: use JWE (JSON Web Encryption).
  Most apps don't need it.
```

### "JWT vs sessions — which do I use?"

```
  Default for web apps: sessions via HttpOnly cookies (NextAuth default).
  Simple, instant revocation, no token management.

  Use JWTs when:
  - Multiple services verify tokens independently (microservices)
  - Mobile / native apps (cookies are awkward)
  - Third-party API access tokens (OAuth2)

  The framework usually makes this decision correctly for you.
  NextAuth uses database sessions for web, JWTs for API routes.
```

### "401 vs 403 — which one?"

```
  401 Unauthorized = "I don't know who you are."
      Send credentials. Try again with auth.

  403 Forbidden = "I know who you are. You can't do this."
      Don't retry. You're not allowed regardless of credentials.

  Wrong 401 when you mean 403:
  Client retries login → logs in again → same 401 → infinite loop.
```

---

## Old World → New World Bridge

| .NET / Azure / Microsoft concept | Modern web auth equivalent | Notes |
|---|---|---|
| Windows Authentication | OIDC with Entra ID | Same protocol underneath |
| Kerberos TGT (ticket-granting ticket) | OAuth2 authorization code | Both: redirect to trusted authority, receive short-lived ticket/token, present to resource server |
| Kerberos Service Ticket | OAuth2 access_token | Short-lived credential for one specific resource |
| NTLM challenge-response | No modern web equivalent | NTLM is connection-based; OAuth2/OIDC is redirect-based (Kerberos lineage) |
| ADFS | Azure Entra ID / Auth0 | ADFS is the on-prem predecessor |
| Azure AD / Entra ID | OIDC provider | It IS an OIDC provider |
| WS-Federation / WS-Trust | OAuth2 / OIDC | Replaced by open standards |
| WCF WS-Security | JWT Bearer tokens | `Authorization: Bearer eyJ...` |
| SAML assertions | OIDC id_token | Both carry identity claims; SAML=XML, OIDC=JWT |
| `ClaimsIdentity` / `ClaimsPrincipal` | JWT payload claims | Same concept |
| `ClaimTypes.Role` | `role` claim in JWT | `{ "role": "admin" }` |
| `[Authorize(Roles = "Admin")]` | `requireRole('admin')` middleware | Same gate, different syntax |
| `FormsAuthentication` cookie | HttpOnly session cookie | Same model |
| ASP.NET Identity / Membership | Auth0 / Clerk / NextAuth | Managed identity system |
| `Microsoft.Identity.Web` | NextAuth MicrosoftEntraID provider | MSAL for Next.js |
| Service Principal + secret | Client Credentials OAuth2 flow | M2M auth |
| Managed Identity (Azure) | Workload identity federation | Secretless M2M |
| `HttpContext.User` | `req.user` / `session.user` | Current authenticated user |
| App registration (Entra) | OAuth2 client_id + client_secret | Register app to get credentials |
| Tenant ID | `issuer` / `tenantId` in OIDC config | Identifies the IdP |
| Azure AD B2C | Auth0 / Clerk (consumer identity) | External user sign-up/sign-in |
| `System.IdentityModel.Tokens.Jwt` | `jsonwebtoken` npm package | JWT library |
| Azure CLI `az login` | OAuth2 Device Authorization Flow | Same flow — browse to devicelogin, enter code |
| GitHub CLI `gh auth login` | OAuth2 Device Authorization Flow | Same flow |

---

## Decision Cheat Sheet

| I need... | Use |
|---|---|
| Auth for a new Next.js app | NextAuth.js (Auth.js) |
| Best DX + prebuilt UI components | Clerk |
| Enterprise / B2B with orgs + SSO | Auth0 or Clerk |
| Microsoft 365 / Entra integration | NextAuth MicrosoftEntraID provider |
| Own all data, open source, free | NextAuth.js with Prisma adapter |
| M2M / service-to-service | OAuth2 Client Credentials + JWT |
| CLI tool / device without browser | OAuth2 Device Authorization Flow (RFC 8628) |
| Store tokens securely | HttpOnly cookie (not localStorage) |
| Instant token revocation | Server-side sessions |
| Short-lived access, long-lived refresh | 15-60min access + 30-day HttpOnly refresh |
| Role-based access control | `role` claim in JWT + middleware |
| Social login | NextAuth.js providers |
| Protect a Next.js page | `const session = await auth(); if (!session) redirect('/login')` |
| Protect an API route | Check session, return 401 if missing, 403 if unauthorized |
| Prevent auth code interception | PKCE (always use for public clients) |
