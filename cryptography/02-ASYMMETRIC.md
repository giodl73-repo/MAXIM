# 02 — Asymmetric Cryptography

## RSA, Diffie-Hellman, Elliptic Curves, Pairings, KEM-DEM

---

## Big Picture: Asymmetric Crypto Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    ASYMMETRIC CRYPTOGRAPHY MAP                           │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HARDNESS PROBLEMS                                                       │
│  ┌────────────────────────┬───────────────────────────────────────────┐  │
│  │ INTEGER FACTORING      │ DISCRETE LOGARITHM                        │  │
│  │  RSA, Rabin, Paillier   │  DH, DSA (ℤₚ*), ECDH, ECDSA (EC group) │    │
│  │  n=pq → factor n hard   │  given g^x, find x hard                 │   │
│  │  Best: GNFS (~2¹¹²/2048)│  DLOG ℤₚ*: index calculus sub-exp      │    │
│  │                         │  DLOG EC: no sub-exp known → ECC smaller│   │
│  └────────────────────────┴───────────────────────────────────────────┘  │
│                                                                          │
│  CONSTRUCTIONS                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │  PKE (public-key encryption):                                    │    │
│  │    RSA-OAEP (factoring), ECIES (ECDH + AEAD), HPKE (RFC 9180)    │    │
│  │  Digital signatures:                                             │    │
│  │    RSA-PSS (factoring), ECDSA (ECDLP), Ed25519 (safe EdDSA)      │    │
│  │  Key exchange (KEM):                                             │    │
│  │    ECDH / X25519, X448; also RSA-KEM; KEM-DEM hybrid             │    │
│  │  Advanced (pairings):                                            │    │
│  │    BLS (aggregatable sigs), IBE, attribute-based enc, zk-SNARKs  │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  KEY SIZES (128-bit security target)                                     │
│   RSA-3072 / DH-3072 / DSA-3072 ≈ AES-128 ≈ SHA-256 ≈ P-256           │
│   ECC curves: 256-bit ≈ 128-bit security (smaller than RSA/DH)          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. RSA — Key Generation and Basic Operations

```
KEY GENERATION:
  1. Pick large primes p, q (each ~1536-bit for RSA-3072)
  2. n = p × q                               (public modulus)
  3. λ(n) = lcm(p-1, q-1)                   (Carmichael's totient; or φ(n)=(p-1)(q-1))
  4. Choose e: 1 < e < λ(n); gcd(e, λ(n))=1 (public exponent; common: e=65537 = 2¹⁶+1)
  5. d = e⁻¹ mod λ(n)                       (private exponent; extended Euclidean)
  Public key: (n, e);  Private key: (n, d) or (p, q, d, dp, dq, qInv)

  Why e=65537? Small; odd; exactly 17 bits (efficient square-and-multiply); large enough
    not to be broken by small-exponent attacks; standard since RFC 4870

ENCRYPTION / DECRYPTION (textbook RSA):
  Encrypt: c = mᵉ mod n
  Decrypt: m = cᵈ mod n

CORRECTNESS — Euler's Theorem:
  m^{φ(n)} ≡ 1 (mod n)  when gcd(m, n) = 1  [Euler]
  m^{λ(n)} ≡ 1 (mod n)  [Carmichael; generalization]
  So: c^d = (m^e)^d = m^{ed} = m^{1 + k·λ(n)} = m · (m^{λ(n)})^k = m · 1 = m (mod n)

TEXTBOOK RSA IS INSECURE:
  1. Deterministic: same message → same ciphertext → NOT IND-CPA
  2. Homomorphic: E(m₁) × E(m₂) = E(m₁m₂); chosen-ciphertext attacks
  3. Small exponent: if e=3 and m is small → m³ < n → trivially decrypt via cube root
  4. Multiplicative structure: c' = r^e × c → decrypt c' → m'=rm → m = m'/r

CRT OPTIMIZATION FOR DECRYPTION:
  dp = d mod (p-1);  dq = d mod (q-1);  qInv = q⁻¹ mod p
  Decrypt: mp = c^{dp} mod p;  mq = c^{dq} mod q
  CRT recombine: m = mp + p × qInv × (mq - mp) mod n
  Speedup: ~4× faster than direct m = c^d mod n
  Security: must verify dp, dq, qInv to prevent fault injection attack (Bellcore)

FACTORING ALGORITHMS:
  Trial division: O(√n); only for small primes up to ~10^6
  Pollard ρ: O(n^{1/4}); birthday paradox on function iteration; good up to ~10^20
  Elliptic curve method (ECM): O(exp(√(2 log p log log p))); depends on small factor p
  Quadratic sieve (QS): O(exp(√(log n log log n))); practical to ~110-bit n
  General Number Field Sieve (GNFS): asymptotically fastest; O(exp((64/9)^{1/3} · (log n)^{1/3} · (log log n)^{2/3}))
  Record: RSA-250 (829-bit) factored 2020; RSA-2048 (617-digit): estimated 10^20 core-years with GNFS
```

---

## 2. RSA-OAEP and Padding Security

```
PKCS#1 v1.5 (the dangerous padding — BLEICHENBACHER 1998):
  Padding: 0x00 || 0x02 || non-zero random bytes || 0x00 || message
  Decrypt: check pad structure → if valid padding, continue; else error
  Bleichenbacher '98 attack:
    Adaptive chosen-ciphertext: send c' = s^e × c (mod n) for chosen s
    Observe padding oracle: does server return valid vs invalid padding error?
    After ~10^6 queries: recover original message m entirely
    "ROBOT" (2017): 27 top sites still vulnerable; F5, Citrix, Cisco, Radware
    DROWN (2016): SSLv2 padding oracle can attack TLS sessions via cross-protocol attack
  Fix: use RSA-OAEP or ECDH (avoid RSA encryption entirely for key exchange)

OAEP (Optimal Asymmetric Encryption Padding — Bellare-Rogaway 1994):
  Based on two hash/PRF primitives: H: {0,1}* → {0,1}^{hLen}, G: {0,1}^{hLen} → {0,1}^{k-hLen-1}

  Encoding (before RSA exponentiation):
    r ← random {0,1}^{hLen}
    maskedSeed = seed ⊕ G(r)  where seed = H(label) || 0-padding || 0x01 || message
    Actually: X = (seed ⊕ MGF(r)) || (r ⊕ MGF(seed))
    Textbook: m' = X → c = m'^e mod n

  OAEP security (ROM):
    IND-CCA2 secure IF RSA is one-way AND H, G are random oracles
    Reduction: A that breaks IND-CCA2 of OAEP → B that inverts RSA
    Proof: OAEP structure prevents padding oracle — invalid ciphertext → fails MGF extraction

  RSA-PSS (probabilistic signature scheme):
    Digital signature analog of OAEP; also Bellare-Rogaway
    sUF-CMA (strong unforgeability) in ROM
    PKCS#1 v1.5 signatures: deterministic; length-extension; still widely deployed (TLS)
    RSA-PSS: preferred for new systems; required in FIPS 186-4 for new applications

BLEICHENBACHER vs MODERN:
  RSA-PKCS1v15 for key encapsulation: do not use; retire in all new systems
  RSA-PSS for signatures: OK (not vulnerable to Bleichenbacher style)
  ECDH: no analogous oracle attack; preferred for key exchange
```

---

## 3. Discrete Logarithm and Diffie-Hellman

```
DISCRETE LOG PROBLEM (DLOG):
  Group (G, ·); generator g; given h = g^x, find x ∈ ℤ_|G|
  DLOG in ℤₚ* (multiplicative group mod prime p):
    Baby-step-giant-step: O(√p) time + O(√p) space
    Pohlig-Hellman: if |G| = ∏ qᵢ^eᵢ, reduces to DLOG in each prime-order subgroup
      → must use prime-order group or check for smooth order
    Index calculus: sub-exponential; O(L_p[1/2, c]) where L_p[α,c] = exp(c·(log p)^α·(log log p)^{1-α})
    → for 128-bit security in ℤₚ*: need p ~ 3072 bits (same as RSA)

  DLOG in elliptic curve groups (ECDLP):
    No sub-exponential algorithm known for general elliptic curves
    Pohlig-Hellman: still applicable → use prime-order curves (Curve25519, P-256)
    MOV attack: applies to supersingular curves and anomalous curves (embedding to ℤₚ*)
    → specific vulnerable curves; standard curves immune
    Generic: Baby-step-giant-step O(√|G|) → need |G| ~ 2²⁵⁶ for 128-bit security
    Result: 256-bit ECC ≈ 3072-bit RSA/DH for 128-bit security

DIFFIE-HELLMAN (1976):
  Setup: prime p, generator g ∈ ℤₚ*
  Alice: a ← ℤₚ*, send A = g^a mod p
  Bob:   b ← ℤₚ*, send B = g^b mod p
  Shared secret: K = B^a = A^b = g^{ab} mod p

  DH is NOT authenticated: man-in-the-middle can substitute their own values
    Mallory sends A' to Bob, B' to Alice → two separate DH sessions
    Fix: sign the DH values (STS protocol, TLS signed DH, Noise_XX, etc.)

  CDH: Computational DH: given g^a, g^b, compute g^{ab}  (hard if DLOG is hard)
  DDH: Decisional DH: distinguish (g^a, g^b, g^{ab}) from (g^a, g^b, g^c)  [c random]
    DDH is stronger assumption; CDH ← DDH in generic groups

X25519 (Curve25519 ECDH, RFC 7748):
  Montgomery curve: y² = x³ + 486662x² + x over 𝔽_{2²⁵⁵-19}
  x-coordinate only: scalar multiplication uses only x-coordinate (Montgomery ladder)
  Private key: 32 random bytes (with specific clamping: set bit 255, clear bits 0/1/2)
  Public key: DH_base_point × private_key (x-coordinate only)
  ECDH: K = scalar_mult(my_private, their_public) → 32-byte shared secret
  Advantages: no cofactor issues; Montgomery ladder constant-time; no special cases
  Performance: ~100 µs per key exchange on 64-bit hardware; very fast
```

---

## 4. Elliptic Curves

```
SHORT WEIERSTRASS FORM:
  y² = x³ + ax + b  over 𝔽ₚ (prime field)
  Requirements: 4a³ + 27b² ≠ 0 (non-singular; no cusps/self-intersections)
  Points: {(x,y) | x,y ∈ 𝔽ₚ, y² = x³+ax+b} ∪ {∞} where ∞ is point at infinity

GROUP LAW (chord-and-tangent):
  P + Q where P = (x₁,y₁), Q = (x₂,y₂):
    If P = ∞: P + Q = Q  (identity element)
    If P = (x₁, y₁) and Q = (x₁, -y₁): P + Q = ∞  (inverse points)
    Otherwise:
      λ = (y₂-y₁)/(x₂-x₁)  if P≠Q;  λ = (3x₁²+a)/(2y₁)  if P=Q (tangent)
      x₃ = λ² - x₁ - x₂
      y₃ = λ(x₁-x₃) - y₁
  Group axioms: closure ✓, associativity ✓, identity (∞) ✓, inverse ✓
  → Elliptic curve over 𝔽ₚ is an abelian group

SCALAR MULTIPLICATION:
  [k]P = P + P + ... + P  (k times) — "discrete exponentiation" in additive group
  Double-and-add: O(log k) point additions
  Constant-time: Montgomery ladder computes both [k]P and [k+1]P together; select based on bit
    CRITICAL: naive square-and-multiply on secret k leaks via timing/power side-channel

ECDSA (NIST FIPS 186):
  Setup: curve with prime-order subgroup of order n; generator G
  Key gen: private k ∈ [1, n-1]; public Q = [k]G

  Sign(m, k_priv):
    r_nonce ← random [1, n-1]    ← MUST BE TRULY RANDOM AND UNIQUE
    R = [r_nonce]G; r = R.x mod n
    s = r_nonce⁻¹ · (H(m) + k · r) mod n
    Signature: (r, s)

  Verify(m, Q_pub, (r,s)):
    w = s⁻¹ mod n
    u₁ = H(m)·w mod n;  u₂ = r·w mod n
    X = [u₁]G + [u₂]Q_pub
    Accept if X.x mod n = r

  CRITICAL SECURITY REQUIREMENT: r_nonce must be uniformly random and NEVER reused
    If same nonce reused for two messages (r same):
      s₁ - s₂ = r_nonce⁻¹ · (H(m₁) - H(m₂)) → r_nonce = (H(m₁)-H(m₂))/(s₁-s₂) → k recovered
    Sony PS3 hack (2010): used constant r_nonce → all games signed → cracked
    Android Bitcoin wallet (2013): weak random → nonce reuse → key theft

ED25519 (EdDSA on Edwards curve — Bernstein et al. 2011):
  Twisted Edwards curve: -x² + y² = 1 - (121665/121666)x²y²  over 𝔽_{2²⁵⁵-19}
  Deterministic nonce: r = H(k_priv_half || m) mod ℓ (where ℓ = group order)
    → No random number generator needed; nonce reuse impossible by construction
  Complete addition formulas: no special cases (avoids implementation errors)
  Performance: ~10% faster than ECDSA P-256; simpler, safer implementation
  Batch verification: verify n signatures faster than n individual verifications
  RFC 8032; preferred for new systems

CURVE COMPARISON:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Curve     │ Field     │ Security │ Standard │ Issues             │     │
  ├─────────────────────────────────────────────────────────────────────────┤
  │  P-256     │ 𝔽_p (256) │ 128-bit  │ NIST     │ Alleged backdoor?  │     │
  │  P-384     │ 𝔽_p (384) │ 192-bit  │ NIST     │ Rigid but opaque   │     │
  │  Curve25519│ 𝔽_{2²⁵⁵} │ 128-bit  │ IETF RFC │ Clean; Bernstein   │     │
  │  X448      │ 𝔽_{2⁴⁴⁸} │ 224-bit  │ IETF RFC │ Clean; higher sec  │     │
  │  brainpool │ 𝔽_p var.  │ various  │ BSI/ETSI │ German std; slower │     │
  └─────────────────────────────────────────────────────────────────────────┘
  P-256 alleged backdoor: NIST curve seeds are unexplained SHA-1 hashes; Bernstein/Lange
    concern: if seeds chosen to have trapdoors, curves could be weak. No confirmed exploit.
  Curve25519: parameters deliberately simple (a=-1); prime 2²⁵⁵-19 for fast arithmetic;
    Bernstein published derivation methodology transparently → "nothing up my sleeve"
```

---

## 5. Pairing-Based Cryptography

```
BILINEAR PAIRING:
  e: G₁ × G₂ → Gₜ  (map from two additive groups to one multiplicative group)
  Properties:
    Bilinear: e([a]P, [b]Q) = e(P, Q)^{ab}
    Non-degenerate: e(G₁_gen, G₂_gen) ≠ 1_Gₜ
    Efficiently computable: Tate, Weil, ate pairings on pairing-friendly curves
  Typical instantiation: BN-256 or BLS12-381 curves (pairing-friendly)

BLS SIGNATURES (Boneh-Lynn-Shacham 2004):
  Signature: σ = [sk]H(m)  (hash to curve, then scalar multiply)
  Verification: e(σ, G₂_gen) = e(H(m), pk)  (pairing check)
  Signature aggregation: σ_agg = Σ σᵢ;  verify: e(σ_agg, G₂_gen) = Π e(H(mᵢ), pkᵢ)
    One pairing operation per signer + one pairing for aggregate → huge savings for n signers
  Applications: Ethereum 2.0 (BLS12-381); distributed validator tech; threshold schemes
  BLS12-381: 381-bit curve; 128-bit security; embedded in Zcash, Ethereum

IDENTITY-BASED ENCRYPTION (IBE — Boneh-Franklin 2001):
  Key idea: public key = identity string (email, phone number); no PKI certificates needed
  Setup: PKG (Private Key Generator) generates master secret msk; publishes mpk
  Extract: PKG computes private key sk_ID = [msk]H(ID) for identity ID
  Encrypt to email@example.com: c = IBE.Enc(mpk, "email@example.com", m)
  Decrypt: IBE.Dec(sk_ID, c)
  Security: BDH (Bilinear Diffie-Hellman) assumption
  Limitation: PKG escrow issue (PKG knows all private keys → key escrow problem)
  Applications: email encryption without prior key exchange; enterprise PKI alternatives

GROTH16 / PLONK / SNARK connections:
  zk-SNARKs (see 04-ZK-MPC) use pairings for the proof verification:
    Verifier computes pairing checks: e(A, B) = e(C, G) type equations
    Concretely: Groth16 proofs use BN-128 or BLS12-381; ~3 pairing operations per verify
  See 04-ZK-MPC for ZK proof details
```

---

## 6. KEM-DEM Hybrid Encryption

```
WHY NOT ENCRYPT WITH RSA DIRECTLY:
  RSA block size: RSA-3072 encrypts ≤ 384 bytes; for OAEP actual limit ~342 bytes
  Multiple RSA applications → each independent encryption → no semantic security across msgs
  Slow: RSA/EC operations ~1000× slower than AES
  KEM-DEM: standard pattern for asymmetric encryption of arbitrary-length data

KEM-DEM FRAMEWORK:
  KEM (Key Encapsulation Mechanism): asymmetric; encapsulates a symmetric key
    ek, K ← KEM.Encap(pk)    (encapsulation; output: ciphertext ek + key K)
    K ← KEM.Decap(sk, ek)    (decapsulation; recover key K)

  DEM (Data Encapsulation Mechanism): symmetric (AEAD)
    ct ← DEM.Enc(K, m, aad)
    m  ← DEM.Dec(K, ct, aad)

  Combined ciphertext: (ek || ct)
  Security: IND-CCA2 KEM + authenticated DEM → IND-CCA2 hybrid scheme

INSTANTIATIONS:
  ECIES (Elliptic Curve Integrated Encryption Scheme):
    KEM: ECDH ephemeral key exchange; DEM: AES-GCM
    Alice: ephemeral (ek_priv, ek_pub); K = ECDH(ek_priv, Bob_pub)
    Send: (ek_pub || AES-GCM(K, m))
    Bob: K = ECDH(Bob_priv, ek_pub); decrypt AES-GCM

  HPKE (Hybrid Public Key Encryption — RFC 9180):
    Standardizes KEM-DEM; multiple KEM choices (ECDH variants, post-quantum)
    KEM: X25519-HKDF-SHA256 or P-256-HKDF-SHA256 or post-quantum
    KDF: HKDF
    AEAD: AES-128-GCM or ChaCha20-Poly1305
    Additional: auth modes (sender auth); info string for domain separation
    Used in: TLS ECH (Encrypted Client Hello), MLS (Messaging Layer Security), OHTTP

  RSA-KEM:
    KEM: ek = r^e mod n (r random); K = KDF(r); Decap: r = ek^d mod n; K = KDF(r)
    More secure than RSA-OAEP in some analyses; less deployment
    Post-quantum threat: broken by Shor's; migrating to HPKE with ML-KEM

```
HPKE MODES (RFC 9180) — SENDER AUTHENTICATION:

  mode_base:    anonymous sender; receiver can't verify who sent
    ks, enc = SetupBaseS(receiver_pub, info)   -- sender
    ks = SetupBaseR(enc, receiver_priv, info)  -- receiver

  mode_auth:    sender-authenticated; receiver verifies sender's static key
    ks, enc = SetupAuthS(receiver_pub, info, sender_priv)
    ks = SetupAuthR(enc, receiver_priv, info, sender_pub)
    Extra DH: DH(sender_priv, receiver_pub) mixed into key schedule → binds sender identity

  mode_psk:     pre-shared key binds both parties; no identity public key needed
  mode_auth_psk: combined: PSK + sender static key authentication (highest binding)

  TLS ECH (Encrypted Client Hello — RFC draft):
    Problem: TLS SNI (server name) is cleartext; leaks which server client is connecting to
    Solution: client encrypts ClientHello with server's published HPKE public key (in DNS HTTPS record)
    Mode: mode_base (client anonymous; server identified by HPKE public key in DNS)
    Wire: ECHClientHello extension = enc || HPKE-sealed inner ClientHello
    Server: decrypts with its HPKE private key; routes to inner server name
    Key rotation: server publishes multiple HPKE public keys (for rotation) in HTTPS DNS records

  MLS (Messaging Layer Security — RFC 9420):
    HPKE used for Welcome messages: encrypt new member's leaf secret in the ratchet tree
    Mode: mode_base (key package public key as receiver; sender = existing group member)
    HPKE info string = group_id || epoch — domain-separates different groups and epochs
    Each group member has a KeyPackage containing their HPKE public key (for leaf key derivation)
```

FORWARD SECRECY:
  Static RSA/EC key pair: compromise → all past sessions decryptable (long-term threat)
  Ephemeral ECDH (ECDHE in TLS): new key pair per session → past sessions safe even if long-term key compromised
  Forward secret = compromise of long-term key doesn't expose past session keys
  TLS 1.3: ephemeral only; no static RSA key exchange; always forward secret
  Signal protocol: ratcheting provides per-message forward secrecy (see 03-PROTOCOLS)
```

---

## 6a. Key Storage Formats and HSM Integration

```
KEY STORAGE FORMATS (private key portability vs security tradeoff):

  PEM (Privacy Enhanced Mail — base64-encoded DER with header):
    "-----BEGIN EC PRIVATE KEY-----" / "-----BEGIN RSA PRIVATE KEY-----"
    Unencrypted by default → file permission is only protection
    Encrypted PEM: AES-256-CBC wraps private key; passphrase via PKCS#5 KDF
    Use: web server TLS private keys (nginx/Apache), SSH private keys, CA key files
    Risk: passphrase stored nearby or in memory; whole key exposed if file accessed

  PKCS#12 / PFX (RFC 7292):
    Container: certificate chain + private key + optional chain certs in one file
    Protected: 3DES-CBC (legacy) or AES-256-CBC + HMAC-SHA256 under passphrase
    Use: browser certificate import/export; Windows certificate store; Java keystores
    Export from HSM: HSM may allow export as PKCS#12 for backup (wraps key; not plaintext)
    Risk: passphrase is the only barrier; 3DES in legacy PKCS#12 is weak — use -legacy flag awareness

  JWK (JSON Web Key — RFC 7517):
    JSON format: {"kty": "EC", "crv": "P-256", "x": "...", "y": "...", "d": "..."}
    Private key in "d" field; public key in "x", "y" (EC) or "n", "e" (RSA)
    JWK Set (JWKS): array of keys; URL-served public keys for JWT verification
    Use: REST APIs, OAuth/OIDC (public JWKS URLs), cloud service key management
    Risk: private JWK often stored in config files; easy to accidentally commit to git

  PKCS#8 (RFC 5958):
    DER-encoded private key container (algorithm OID + private key bytes)
    Encrypted PKCS#8: EncryptedPrivateKeyInfo = algorithm + encrypted key
    Use: Java's java.security.PrivateKey serialization; OpenSSL pkcs8 output

KEY STORAGE COMPARISON:
  ┌───────────────────────────────────────────────────────────────────────────┐
  │  Format    │ Portable │ Encrypted │ Includes Cert │ Use Case              │
  ├───────────────────────────────────────────────────────────────────────────┤
  │  PEM       │ Yes      │ Optional  │ No (separate) │ Unix TLS, SSH         │
  │  PKCS#12   │ Yes      │ Yes       │ Yes           │ Browser, Windows      │
  │  JWK       │ Yes      │ Optional  │ No            │ APIs, OAuth, cloud    │
  │  HSM slot  │ No       │ Hardware  │ No            │ Production keys       │
  └───────────────────────────────────────────────────────────────────────────┘

PKCS#11 INTERFACE MODEL (key never leaves HSM):

  Model: application calls crypto operations on HSM via PKCS#11 API;
         private key identified by handle (slot + object ID), never extracted to memory

  C_Initialize() → C_OpenSession(slot, &hSession) → C_Login(hSession, PIN)
  C_FindObjects → hKey (handle to private key object on token)
  C_Sign(hSession, mechanism, hKey, data, &sig)  ← HSM performs signing
  C_Decrypt(hSession, mechanism, hKey, ciphertext, &plaintext)  ← HSM decrypts

  Mechanisms: CKM_RSA_PKCS_OAEP, CKM_ECDSA, CKM_AES_GCM, etc.
  Application only sees: signature bytes, decrypted bytes — private key bytes never returned

  Language bindings following same PKCS#11 model:
    OpenSSL: pkcs11-provider (PKCS#11 engine); configure via openssl.cnf
    Java JCA: SunPKCS11 provider; transparent to application (standard KeyStore API)
    Go: crypto.Signer interface — Sign() method backed by PKCS#11 or cloud KMS
    .NET: CNG (CryptoNG) for TPM/smartcard; PKCS#11 via third-party provider

  HSM vs software key store decision:
    HSM: private key material never in process memory; tamper-evident; FIPS 140-3 validated
    Software: cheaper; faster; acceptable when key is ephemeral or threat model is lower
    Rule of thumb: CA signing keys, TLS server keys for high-value services → HSM
    Cloud HSM: AWS CloudHSM, Azure Dedicated HSM, Google Cloud HSM; PKCS#11 compatible
```

## 7. Integer Factorization Details

```
WHY RSA IS SECURE (current understanding):
  Factoring n → get p, q → compute λ(n) → compute d = e⁻¹ mod λ(n)
  No polynomial-time classical algorithm known; GNFS is sub-exponential

  Alternative attacks:
    Find d directly: equivalent to factoring (Rivest-Adleman theorem: computing d is as hard as factoring)
    Find λ(n) directly: equivalent to factoring (Miller 1975)
    e-th root attacks: if m is small and e is small → mᵉ < n → trivial; OAEP prevents
    Partial key exposure: if bottom 1/4 of d bits known → Coppersmith → factor n; use long d

COPPERSMITH ATTACKS:
  Low public exponent: if mᵉ < n → c = mᵉ exactly → m = c^{1/e} (integer cube root if e=3)
  Hastad's broadcast attack: m sent to 3 parties with different public keys, same e=3
    c₁ = m³ mod n₁, c₂ = m³ mod n₂, c₃ = m³ mod n₃ → CRT → m³ mod n₁n₂n₃ → cube root
    Fix: OAEP randomization ensures different messages sent
  Related messages: if two known functions of m encrypted (linear relationship) → recover m
  Partial key recovery: lattice-based Coppersmith algorithms on polynomials mod n

CURRENT RECORDS (2024):
  RSA-250 (829 bits): factored 2020, ~2700 CPU core-years (GNFS)
  RSA-768 (768 bits): factored 2009
  RSA-2048: estimated 2^{112} CPU core-years; infeasible; safe for foreseeable classical future
  Post-quantum: Shor's algorithm → O((log n)³) quantum operations → must migrate
```

---

## 8. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| RSA-2048 vs RSA-3072 for new systems? | RSA-3072 minimum for 128-bit security; RSA-2048 is 112-bit; use P-256/X25519 instead |
| Why never use PKCS#1 v1.5 RSA encryption? | Bleichenbacher padding oracle; ROBOT attack still active; use RSA-OAEP or ECDH |
| Ed25519 vs ECDSA advantage? | Deterministic nonce (no RNG failure risk); faster; simpler constant-time implementation |
| Why is ECDLP harder than DLOG in ℤₚ*? | No sub-exponential algorithm known for general EC; index calculus doesn't apply |
| KEM-DEM construction purpose? | Use asymmetric only for key exchange; symmetric AEAD for bulk data; hybrid |
| Forward secrecy mechanism? | Ephemeral key pair per session (ECDHE); long-term compromise doesn't expose past sessions |
| Why Curve25519 over P-256? | Clean parameters; no opaque seed; guaranteed prime-order; constant-time by design |
| BLS signatures unique advantage? | Aggregatable: n signatures collapse to one; O(1) verification cost for aggregate |
| What does the pairing e(aP, bQ)=? | e(P, Q)^{ab} — bilinearity is the key property enabling advanced constructions |
| Bleichenbacher's attack requires? | Padding oracle: server reveals whether RSA-decrypted value has valid PKCS#1 v1.5 padding |
| DH without authentication → ? | Man-in-the-middle attack; must sign DH values (STS, TLS, authenticated KEM) |
| RSA-OAEP security model? | IND-CCA2 in ROM assuming RSA is one-way (trapdoor permutation) |
| HPKE RFC number? | RFC 9180; standardizes KEM-DEM with multiple algorithm choices |
| Critical ECDSA nonce requirement? | Must be uniformly random AND unique per signature; reuse → private key recovery |

---

## Common Confusion Points

**RSA decryption private exponent d ≠ "secret key" alone:** The full private key is typically (p, q, d, dp, dq, qInv) using CRT. Only storing d is wasteful and slower. The security of d relies entirely on the hardness of factoring n — anyone who factors n can compute d. So "RSA-2048 security" is the hardness of factoring 2048-bit n, not the size of d.

**ECC "256-bit key" vs "256-bit security" are different things:** A 256-bit elliptic curve key provides ~128-bit security (BSGS attacks are O(√|G|) = O(2¹²⁸)). Contrast: AES-256 key provides ~256-bit classical security. So "256-bit ECC key ≈ 128-bit AES" for security. For post-quantum: Shor breaks ECC in polynomial time; Grover reduces AES-256 to ~128-bit. At equivalent protection, need 512-bit ECC or switch to post-quantum.

**ECDH is not a signature — cannot be used for authentication directly:** ECDH produces a shared secret; it doesn't authenticate either party. An ephemeral ECDH is anonymous key exchange. Adding authentication requires signing the ECDH public keys (as in TLS with certificate-signed server key). Confusion of ECDH with ECDSA is common.

**Pairing-based crypto: not every elliptic curve supports pairings:** Only pairing-friendly curves (BN-256, BLS12-381, BLS12-377, etc.) have efficiently computable pairings. P-256 and Curve25519 are NOT pairing-friendly. Using pairings requires selecting a specific curve that supports them; this comes with different security parameters and performance characteristics.

**IBE solves one problem but creates another:** IBE eliminates certificate management (no need to distribute public key certificates). But it requires a trusted Key Generation Authority (KGA/PKG) that generates all private keys. This is inherent key escrow — the KGA can decrypt any message to any identity. Enterprise IBE often accepts this tradeoff; internet-scale IBE typically does not.

**"RSA-PSS" vs "RSA-PKCS1v15" signatures:** Both use RSA math; the difference is the padding around the hash. PKCS1v15 is older, deterministic, widely deployed (TLS, X.509 certs). PSS is randomized, provably secure in ROM, required by FIPS 186-4 for new applications. Both are EUF-CMA; PSS is additionally sUF-CMA (no signature malleability). For new systems: RSA-PSS or Ed25519.

## Post-Quantum Migration Map

```
CLASSICAL → PQC TRANSITION TABLE (see 05-POST-QUANTUM.md for full detail):

  ┌────────────────────────────────────────────────────────────────────────────────┐
  │  Classical Primitive    │ Broken by  │ PQC Replacement      │ Transition Path  │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  ECDH / X25519 (KEM)    │ Shor's     │ ML-KEM (FIPS 203)    │ Hybrid: X25519 + │
  │                         │            │ Kyber-768 preferred  │ ML-KEM-768 NOW   │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  ECDSA P-256            │ Shor's     │ ML-DSA (FIPS 204)    │ Dual-sign during │
  │                         │            │ Dilithium-65         │ transition       │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  Ed25519 (EdDSA)        │ Shor's     │ ML-DSA or FN-DSA     │ FN-DSA (FALCON)  │
  │                         │            │ FALCON-512 smaller   │ if size matters  │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  RSA-PSS (signatures)   │ Shor's     │ ML-DSA (FIPS 204)    │ ML-DSA-44 for    │
  │                         │            │ or FN-DSA (FALCON)   │ 128-bit equiv    │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  RSA-OAEP (encryption)  │ Shor's     │ ML-KEM (FIPS 203)    │ Replace with     │
  │                         │            │ via HPKE (RFC 9180)  │ HPKE + ML-KEM    │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  BLS12-381 (pairings)   │ Shor's*    │ No direct equiv yet  │ Active research; │
  │                         │ *harder    │ (BLS advantage lost) │ avoid new PQC    │
  │                         │ for EC     │                      │ pairing designs  │
  └────────────────────────────────────────────────────────────────────────────────┘

  Size impact at 128-bit security:
    KEM:       X25519 pub = 32B → ML-KEM-768 pub = 1184B  (+37×)
    Signature: Ed25519 sig = 64B → ML-DSA-65 sig = 3293B  (+51×)
    Signature: Ed25519 sig = 64B → FALCON-512 sig = 666B  (+10×; if complexity acceptable)

  Hybrid strategy (transition period):
    KEM:  X25519Kyber768 (RFC 9496 / TLS draft) — Chrome + Firefox shipping now
    Sig:  dual-sign (both classical + PQC); verify either is sufficient
    Timeline: remove classical component ~2030+ when confidence in PQC is established
```
