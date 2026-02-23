# 03 — Cryptographic Protocols

## TLS 1.3, SSH, Signal Protocol, Noise Framework, Key Management

---

## Big Picture: Protocol Composition

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PROTOCOL STACK                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  APPLICATION LAYER                                                      │
│   HTTPS (TLS 1.3), SMTP/IMAP+TLS, QUIC+TLS 1.3, gRPC/TLS             │
│   SSH (remote access, SCP/SFTP), WireGuard (Noise-based VPN)           │
│   Signal (E2E messaging), WhatsApp/iMessage (Signal-derived)            │
│                                                                         │
│  HANDSHAKE LAYER (key establishment)                                    │
│   TLS 1.3: ECDHE + signature-based auth + HKDF key schedule            │
│   SSH: DH/ECDH key exchange + host key authentication                  │
│   X3DH (Signal): multi-key DH for asynchronous key establishment       │
│   Noise: composable pattern framework; WireGuard = Noise_IKpsk2        │
│                                                                         │
│  KEY DERIVATION + RATCHETING                                            │
│   HKDF-based key schedule (TLS 1.3; section labels = domain separation)│
│   Double Ratchet (Signal): per-message forward secrecy + recovery      │
│                                                                         │
│  RECORD/DATA LAYER                                                      │
│   AEAD: AES-128-GCM, AES-256-GCM, ChaCha20-Poly1305 (TLS 1.3)        │
│   Sequence number → nonce anti-replay                                  │
│                                                                         │
│  TRUST LAYER (authentication)                                           │
│   PKI: X.509 certificates + certificate authorities + CT logs           │
│   TOFU: Trust On First Use (SSH default)                                │
│   Web of trust: PGP; forward-secret ratchet (Signal)                   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. TLS 1.3 Handshake (Full Transcript)

```
TLS 1.3 OVERVIEW:
  RFC 8446; 1-RTT full handshake; 0-RTT resumption; AEAD-only; no static RSA
  Always forward-secret: ephemeral (EC)DHE required; no static DH or RSA key exchange
  Removed from TLS 1.3: RSA key exchange, CBC+HMAC suites, RC4, 3DES, SHA-1, MD5, NULL

1-RTT HANDSHAKE:
  Client ──────────────────────────────────────────────────────────► Server

  ClientHello:
    client_random (32 bytes)
    legacy_session_id (for middlebox compat; ignored in TLS 1.3)
    cipher_suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,
                   TLS_CHACHA20_POLY1305_SHA256
    extensions:
      supported_versions: [TLS 1.3, TLS 1.2]  (TLS 1.3 indicated here)
      key_share: [(X25519, client_ec_pub), (P-256, ...)]
      supported_groups: X25519, P-256, X448, P-384
      signature_algorithms: ecdsa_secp256r1_sha256, ed25519, rsa_pss_rsae_sha256, ...
      server_name: "example.com"  (SNI — Server Name Indication)
      early_data (optional for 0-RTT)

  ServerHello:
    server_random (32 bytes)
    cipher_suite: TLS_AES_128_GCM_SHA256
    extensions:
      supported_versions: TLS 1.3
      key_share: (X25519, server_ec_pub)   ← ephemeral key pair generated per handshake

  ──── Both sides compute ECDH shared secret Z = ECDH(client_priv, server_pub) ────
  ──── Key schedule begins (all further messages encrypted) ────

  EncryptedExtensions (encrypted):    additional server extensions
  Certificate (encrypted):            server's X.509 cert chain
  CertificateVerify (encrypted):      signature over handshake transcript
    sign(server_private_key, "TLS 1.3, server CertificateVerify" || transcript_hash)
  Finished (encrypted):               HMAC over handshake transcript with server_finished_key

  Client ◄───────────────────────────────────────────────────────── Server

  Client verifies Certificate chain, CertificateVerify signature, Finished MAC
  Client sends Finished (HMAC with client_finished_key)
  Total RTT: 1 full round trip; symmetric keys available before Finished

0-RTT (Early Data):
  Resumed session; client can send application data with ClientHello
  Uses resumption_secret from previous session → PSK
  Security: 0-RTT is NOT forward-secret (PSK is reused)
  Replay vulnerability: server sees early data before verifying; no replay protection
    0-RTT data must be idempotent (GET requests; not financial transactions)
  0-RTT is optional; servers can reject; limited use cases
```

---

## 2. TLS 1.3 Key Schedule

```
HKDF-BASED KEY SCHEDULE (RFC 8446 §7.1):
  Uses HKDF-Extract and HKDF-Expand-Label throughout
  Label format: HKDF-Expand-Label(secret, label, context, length)
    = HKDF-Expand(secret, "tls13 " + label, context, length)

  Secret derivation flow:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Early Secret = HKDF-Extract(0, PSK or 0)                          │
  │                    │                                               │
  │  Handshake Secret = HKDF-Extract(Derive-Secret(Early, "derived"), │
  │                                  ECDHE shared secret Z)           │
  │                    │                                               │
  │  client_handshake_traffic_secret ← HKDF-Expand-Label(HS,"c hs traffic",H)│
  │  server_handshake_traffic_secret ← HKDF-Expand-Label(HS,"s hs traffic",H)│
  │  client/server AEAD keys ← Expand from traffic secrets             │
  │                    │                                               │
  │  Master Secret = HKDF-Extract(Derive-Secret(HS, "derived"), 0)    │
  │                    │                                               │
  │  client_application_traffic_secret_0 ← Expand-Label(MS,"c ap traffic")  │
  │  server_application_traffic_secret_0 ← Expand-Label(MS,"s ap traffic")  │
  │  resumption_master_secret ← Expand-Label(MS,"res master", H(full handshake))│
  └─────────────────────────────────────────────────────────────────────┘

  H = transcript hash (running SHA-256 or SHA-384 depending on cipher suite)
  Each secret derives separate client/server keys + IVs

FORWARD SECRECY ANALYSIS:
  ECDHE: ephemeral key pair destroyed after handshake
  Attacker records ciphertext; later compromises server's certificate key
  But: server cert key only used in CertificateVerify signature; not used for AEAD
  Symmetric keys derived from ECDHE secret → gone when ephemeral key erased
  Result: past sessions safe even with server certificate compromise

KEY UPDATES:
  RFC 8446 §4.6.3: KeyUpdate message; both sides can initiate mid-session
  Derive new application_traffic_secret from old via HKDF-Expand-Label
  Provides forward secrecy within session (old keys can't decrypt new data after update)
```

---

## 3. TLS Certificates and PKI

```
X.509 CERTIFICATE STRUCTURE:
  TBSCertificate:
    version: v3
    serialNumber: CA-assigned unique number
    signature: algorithm (e.g., ecdsa-with-SHA256)
    issuer: CA's Distinguished Name (DN)
    validity: notBefore + notAfter (timestamps)
    subject: entity's DN (or empty for SAN-only cert)
    subjectPublicKeyInfo: algorithm + key bytes
    extensions:
      Subject Alt Name (SAN): dns:example.com, dns:*.example.com
      Key Usage: digitalSignature, keyEncipherment
      Extended Key Usage: serverAuth, clientAuth, codeSigning
      CRL Distribution Points: URL for certificate revocation list
      Authority Information Access (AIA): OCSP URL + issuer cert URL
      Subject Key Identifier, Authority Key Identifier
      CA Basic Constraints: pathLen constraint

CERTIFICATE CHAIN:
  Root CA (self-signed; in browser/OS trust store) → Intermediate CA → Server cert
  Chain validation: verify each signature up to trusted root; check validity dates; check revocation

REVOCATION:
  CRL (Certificate Revocation List): list of revoked serial numbers; published by CA
    Stale: updated only periodically; potentially hours-old
  OCSP (Online Certificate Status Protocol): real-time check per certificate
    Privacy issue: CA learns which sites you visit (OCSP queries per connection)
  OCSP Stapling: server fetches its own OCSP response; staples to TLS handshake
    Server sends cached OCSP response → client doesn't query CA → privacy preserved
  CRLite / OCSP Must-Staple: Firefox-specific; pre-download CRL bloom filters

CERTIFICATE TRANSPARENCY (CT):
  RFC 9162; all public certificates must be logged in CT logs (append-only Merkle trees)
  Signed Certificate Timestamps (SCTs): log inclusion proof; included in TLS handshake
  Browsers (Chrome 2018+): require SCTs from 2+ independent CT logs; reject otherwise
  Benefit: CA misissuance is publicly visible; *.google.com cert by DH attack on DigiNotar (2011)
    would be caught by CT monitoring
  CT log structure: Merkle hash tree; inclusion proofs in O(log n)

LET'S ENCRYPT (ACME):
  Automated Certificate Management Environment (RFC 8555)
  DV (Domain Validation) only: proves domain control via HTTP-01 or DNS-01 challenge
  Free certificates; 90-day validity; automated renewal (certbot, ACME clients)
  Replaced: expensive manual DV/OV certs; nearly all web TLS now DV via Let's Encrypt/ZeroSSL

CAA DNS RECORDS:
  CAA (Certification Authority Authorization; RFC 8659): DNS records limiting which CAs can issue
  "issue: letsencrypt.org" → only Let's Encrypt can issue for this domain
  Ignored by historical CAs until violation; now enforced
```

---

## 4. SSH Protocol

```
SSH LAYERED ARCHITECTURE (RFC 4251-4254):
  Transport layer: TCP → SSH-TRANS; key exchange, host authentication, encryption setup
  User authentication layer: SSH-USERAUTH; username + auth method (password, pubkey, etc.)
  Connection layer: SSH-CONNECT; multiplexed channels (interactive shell, port forwarding, SCP)

TRANSPORT KEY EXCHANGE:
  Client and server negotiate: kex_algo (curve25519-sha256, diffie-hellman-group14-sha256)
  Ephemeral key exchange: ECDH or DH → shared secret → keys
  Server sends host key signature: sign(host_private_key, H(client_nonce || server_nonce || DH_info))
  Client verifies host key against known_hosts (TOFU or CA-signed)

HOST KEY VERIFICATION:
  TOFU (Trust On First Use):
    First connection: accept host key; store in ~/.ssh/known_hosts
    Subsequent: verify host key matches; error if changed ("WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED")
    Risk: first connection is unauthenticated (MITM possible)
  CA-signed host certificates:
    SSH supports X.509-like certificates for host keys
    ssh-keygen -s CA_key -I "host-cert-id" -h server.pub → server-cert.pub
    Client trusts CA public key (@cert-authority in known_hosts) → automatically verifies new hosts
    Better security posture for organizations; eliminates TOFU problem

USER AUTHENTICATION METHODS:
  Password: plaintext password in encrypted SSH channel; server checks against system auth
    Risks: brute force; credential stuffing; phishing; best: disable entirely
  Public key:
    Prerequisite: client public key in server ~/.ssh/authorized_keys
    Protocol: server sends challenge; client signs with private key; server verifies
    challenge = hash(session_id || "ssh-connection" || username || service || "publickey" || ...)
    Ed25519 preferred: small key (64 bytes), fast, deterministic signatures
  FIDO2/U2F: hardware security key (YubiKey) stores private key; requires physical presence
    sk-ed25519 key type: resident key in FIDO2 authenticator; PIN/touch required

SSH CONFIG HARDENING:
  Disable: PasswordAuthentication no; PermitRootLogin no; X11Forwarding no
  Allow: PubkeyAuthentication yes; UsePAM yes (for 2FA); AllowGroups ssh-users
  Key algorithms: HostKeyAlgorithms ssh-ed25519, rsa-sha2-512 (remove ssh-rsa SHA-1)
```

---

## 5. Signal Protocol: X3DH + Double Ratchet

```
THREAT MODEL FOR SIGNAL:
  E2E: server cannot read messages
  Forward secrecy: compromise of long-term key doesn't expose past messages
  Break-in recovery: if session keys compromised, future messages become safe again
  Sealed sender: server doesn't know who sent a message (separate from X3DH)

X3DH — EXTENDED TRIPLE DIFFIE-HELLMAN (Marlinspike/Perrin):
  Alice wants to initiate with Bob asynchronously (Bob offline)
  Bob publishes to Signal server:
    IK_B: identity key (long-term Ed25519)
    SPK_B: signed prekey (medium-term; rotated ~weekly; signed by IK_B)
    OPK_B: one-time prekey set (fresh keys per session; prevents replay)

  Alice fetches Bob's keys; computes 4 DH values:
    DH1 = DH(IK_A.priv, SPK_B.pub)     ← Alice identity + Bob signed prekey
    DH2 = DH(EK_A.priv, IK_B.pub)      ← Alice ephemeral + Bob identity
    DH3 = DH(EK_A.priv, SPK_B.pub)     ← Alice ephemeral + Bob signed prekey
    DH4 = DH(EK_A.priv, OPK_B.pub)     ← Alice ephemeral + Bob one-time prekey (if available)

  Master secret: KDF(DH1 || DH2 || DH3 || DH4 || KDF_info)
  → generates initial symmetric root key + chain keys

  Security properties:
    Auth: if attacker steals DH1/DH2/DH3 → can't compute without IK_A (Alice's identity)
    Forward secrecy: EK_A ephemeral; erased after use
    One-time prekey: prevents replay of session establishment
    Works offline: Alice can encrypt to Bob without Bob being online

DOUBLE RATCHET ALGORITHM (Trevor Perrin / Moxie Marlinspike 2016):
  Two interlocked ratchets:
  ┌─────────────────────────────────────────────────────────────────┐
  │  KDF CHAIN RATCHET (symmetric):                                 │
  │    chain_key → KDF → (chain_key_next, message_key)              │
  │    Each message: advance chain → new message key                │
  │    Forward secrecy: delete old chain key + message keys         │
  │                                                                 │
  │  DIFFIE-HELLMAN RATCHET:                                        │
  │    Each side sends new DH public key with each message          │
  │    Receiving a new DH key → advance DH ratchet → new root key   │
  │    → reseeds the KDF chain ratchet                              │
  └─────────────────────────────────────────────────────────────────┘

  FORWARD SECRECY: each message has unique key; prior keys deleted after use
  BREAK-IN RECOVERY: DH ratchet introduces fresh entropy every 2 messages
    If attacker captures current session state: waits for first new DH message pair
    → new root key derived from fresh DH → attacker's captured keys useless for future

  Out-of-order messages: message keys can be cached briefly (skipped messages)
  Header encryption: DH ratchet public keys encrypted so metadata protected

SEALED SENDER:
  Normal Signal: server knows Alice → Bob metadata (who messages whom)
  Sealed sender: message encrypted with sealed sender cert
    No cleartext sender identity; server only sees recipient
  Server verifies encrypted certificate prevents spam (anonymous delivery still authenticated)
  Trade-off: slightly more complex key management; some metadata reduction
```

---

## 6. Noise Protocol Framework

```
NOISE OVERVIEW (Trevor Perrin):
  Composable framework for building handshake protocols
  Defines: pattern naming, message format, secret derivation, transport
  Security properties proven for each pattern
  WireGuard, WebRTC DTLS alternative, some IoT protocols use Noise

NAMING CONVENTION: Noise_XX_25519_AESGCM_SHA256
  Handshake pattern: XX (both authenticate each other)
  DH function: 25519 (Curve25519 ECDH)
  AEAD: AESGCM or ChaChaPoly
  Hash: SHA256, SHA512, or BLAKE2

PATTERNS (initiator I, responder R; s=static key, e=ephemeral key, ee/es/se/ss=DH ops):
  NN: neither side has static keys; mutual anonymous ephemeral DH
  NK: responder's static key known to initiator; server auth only
  NX: responder sends static key; server auth negotiated
  KK: both static keys known a priori; mutual auth; fewest messages
  KX: initiator has responder static key; responder discovers initiator static key
  XX: both exchange static keys mid-handshake; mutual authentication; most common

XX PATTERN (mutual authentication — most common):
  -> e                      (initiator sends ephemeral)
  <- e, ee, s, es           (responder sends ephem + static; DH(e,e) + DH(e,s_I))
  -> s, se                  (initiator sends static; DH(s_I, e_R))

  "ee" means: DH(e_initiator, e_responder) → mix into chain key
  "es" means: DH(e_initiator, s_responder) → mix into chain key
  "se" means: DH(s_initiator, e_responder) → mix into chain key
  Each mix provides: forward secrecy (from ephemeral) + authentication (from static)

WIREGUARD — Noise_IKpsk2:
  IK pattern + pre-shared key (psk)
  Both parties have static keys known a priori (registered in WireGuard config)
  Handshake: 1 initiation message + 1 response = 2 messages (1-RTT)
  Transport: 32-byte symmetric keys; AES-256-GCM or ChaCha20-Poly1305
  Under 4000 lines of code; formally verified (using Tamarin); in Linux kernel 5.6+
  Session keys rotate every 3 minutes or 2^60 packets (whichever comes first)

PROLOGUE / PAYLOAD / AAD:
  Prologue: hash of anything before handshake; ensures parties agreed on same context
  Handshake payload: can include application data in handshake messages
  Transport messages: AEAD with nonces derived from internal state

CryptoState object per Noise session:
  (k, n): AEAD key + nonce (incrementing counter)
  Derive new (k, n) pair after each handshake phase
  Handshake hash (h): running transcript hash; provides channel binding
```

---

## 7. Authentication and Key Management

```
PAKE — PASSWORD-AUTHENTICATED KEY EXCHANGE:
  Goal: establish session key from a password WITHOUT exposing password to MITM
  SRP (Secure Remote Password; RFC 5054):
    Server stores: salt + v = g^x mod N  (where x = H(salt || password))
    No actual password; no MITM can get password from eavesdropping
    Security: if server compromised, offline dictionary attack on stored v (but can't reverse directly)
    Deprecated: better alternatives now; SRP is slow and complex

  OPAQUE (IETF draft; based on OPRF):
    Oblivious PRF: server evaluates PRF on password without learning password
    Server never sees plaintext password at any point (registration or login)
    Achieves: password breach resistance (even server DB compromise doesn't expose passwords)
    Status: IETF draft; slowly replacing SRP in new deployments

FIDO2 / WEBAUTHN (W3C + FIDO Alliance):
  Hardware authenticator (YubiKey, Titan Key, TPM, biometric platform)
  Registration:
    Server sends challenge; authenticator generates (priv_key, pub_key) per origin
    Attestation: authenticator signs pub_key with factory cert → proves it's a real device
    Server stores pub_key + credential_id
  Authentication:
    Server sends challenge + allowed credential IDs
    Authenticator signs (challenge || client_data) with priv_key; requires PIN or touch
    Server verifies signature with stored pub_key
  Properties: no shared secrets; public keys per origin → no credential stuffing
    User presence: requires physical touch or biometric → phishing-resistant
    Origin binding: credential bound to RP ID (relying party); can't be used across origins

HSM — HARDWARE SECURITY MODULE:
  Physical/logical tamper-resistant device; contains key material
  Operations: sign, encrypt, decrypt, KDF all performed inside HSM; key never exits
  PKCS#11 API: standard interface for crypto tokens and HSMs
  Form factors: USB token (YubiKey, Gemalto), PCIe HSM (Thales HSM), Cloud HSM (AWS CloudHSM)
  Use cases: CA private keys, TLS termination private keys, code signing, payment HSMs

KEY LIFECYCLE:
  Generation: hardware RNG (FIPS 140-2: SP800-90 DRBG); entropy testing
  Distribution: secure channel; key wrapping (encrypt key under another key)
  Storage: HSM (best); encrypted key store (acceptable if key wrapping key is in HSM)
  Rotation: how often? TLS session keys: per session; TLS server cert: 1-2 years; CA root: 10-25 years
  Revocation: CRL/OCSP for TLS; revoke FIDO2 credential on device loss
  Destruction: NIST SP 800-88 media sanitization; HSM zeroization; shredding

KEY WRAPPING (RFC 3394):
  AES Key Wrap: encrypt a key under another key (KEK — key encryption key)
  Output: wrapped key (8 bytes longer than wrapped key)
  Used: PKCS#12 (export private keys); JWK (JSON Web Key); key backup/escrow
```

---

## 8. Protocol Security Analysis

```
NEEDHAM-SCHROEDER ATTACK (Lowe 1995):
  Original NS Public Key Protocol (1978):
    A → B: E_B(Na, A)             (A sends nonce Na encrypted to B)
    B → A: E_A(Na, Nb, B)        (B responds with Na + new nonce Nb)
    A → B: E_B(Nb)               (A confirms Nb)
  GOAL: mutual authentication between A and B

  LOWE ATTACK: Mallory acts as man-in-the-middle:
    A → M: E_M(Na, A)            (A initiates with Mallory)
    M → B: E_B(Na, A)            (Mallory forwards as if from A)
    B → M: E_A(Na, Nb, B)       (B thinks talking to A)
    M → A: E_A(Na, Nb, B)       (Mallory forwards to A)
    A → M: E_M(Nb)               (A confirms; Mallory gets Nb)
    M → B: E_B(Nb)               (Mallory impersonates A to B — B thinks A authenticated)

  FIX: Lowe added identity of B in message 2:
    B → A: E_A(Na, Nb, B)       (already there! but interpretation issue)
    More robustly: include full identity/nonce bindings
  Lesson: always bind identity and intended recipient in authenticated messages

FORMAL VERIFICATION TOOLS:
  ProVerif: π-calculus based; automated; can prove secrecy and authentication
  Tamarin: multiset rewriting rules; very powerful; requires more manual work
    Used for: TLS 1.3 full proof (Cremers et al. 2017); WireGuard; Signal
  Verifpal: simpler; user-friendly; educational; less expressive
  Scyther: bounded session verification; good for finding attacks

TLS 1.3 FORMAL VERIFICATION (Cremers et al. 2017):
  Full Tamarin proof of TLS 1.3 core handshake
  Verified: forward secrecy, mutual authentication, session uniqueness, channel binding
  Found: one minor issue with 0-RTT (replay; already known)
  Significance: largest formally verified protocol to date at time of writing

KEY COMPROMISE IMPERSONATION (KCI):
  If Alice's long-term private key compromised, can attacker impersonate Alice?
  Basic DH with long-term keys: yes (NAXOS approach fixes this)
  TLS 1.3: ephemeral keys prevent KCI in one direction
  Signal X3DH: provides KCI protection via ephemeral keys mixed with identity keys
```

---

## 9. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| TLS 1.3 vs TLS 1.2 key exchange? | TLS 1.3: ephemeral ECDHE always; no static RSA or DH; always forward-secret |
| 0-RTT TLS security limitation? | Not forward-secret; replay vulnerable; only for idempotent requests |
| OCSP stapling benefit? | Server fetches own OCSP; client doesn't query CA; privacy preserved + faster |
| Certificate Transparency requirement? | Chrome requires SCTs from 2+ independent CT logs (since 2018) |
| SSH host key TOFU risk? | First connection unauthenticated; MITM possible; use CA-signed host certs in org |
| Signal Double Ratchet advantage? | Per-message forward secrecy + break-in recovery; no other messaging protocol has both |
| Why X3DH uses one-time prekeys? | Prevents replay of session establishment; each OPK used once then discarded |
| WireGuard = which Noise pattern? | Noise_IKpsk2; both parties have pre-registered static keys + optional PSK |
| SRP vs OPAQUE? | SRP: server stores verifier (offline attack possible if breached); OPAQUE: server never sees password |
| FIDO2 vs TOTP? | FIDO2: phishing-resistant (origin-bound); TOTP: phishable (attacker can relay code in real-time) |
| Needham-Schroeder lesson? | Always include intended recipient identity in authenticated messages |
| TLS 1.3 key schedule based on? | HKDF with labeled Expand-Label; separate secrets for handshake + application data |
| PKCS#11 API purpose? | Standard interface for HSMs and crypto tokens; applications talk to token via PKCS#11 |
| Double Ratchet: what triggers DH ratchet? | Receiving a new DH public key from the other party |

---

## Common Confusion Points

**TLS 1.3 "session" resumption ≠ cached session:** TLS 1.3 uses a PSK (pre-shared key) ticket for session resumption (RFC 8446 §4.6.1). Unlike TLS 1.2's session cache, the ticket is encrypted to the server's ticket key — the server doesn't store per-session state. The PSK is derived from the resumption_master_secret of the previous session. 0-RTT uses this PSK as the "early secret."

**Certificate expiry ≠ revocation:** A certificate can expire (past its notAfter date) without being revoked, and a certificate can be revoked before it expires. Expiry is time-based; revocation is explicit (CA adds to CRL / OCSP updates). Expired cert → TLS error. Revoked cert → OCSP/CRL check shows revocation → TLS error. But soft-fail OCSP means many browsers continue if OCSP check fails — problematic.

**Double Ratchet forward secrecy is per-message, not per-session:** TLS 1.3 provides per-session forward secrecy (past sessions are safe). Signal Double Ratchet provides per-message forward secrecy (each message key is deleted after decryption; compromise of current key doesn't expose past messages). This is considerably stronger — relevant for long-lived persistent chat sessions.

**Noise XX ≠ mutually authenticated immediately:** In the Noise XX pattern, initiator's static key is sent in the third message (after receiving the responder's static key). The responder learns the initiator's identity only at the end of the handshake; the initiator learns the responder's identity in the second message. The order of mutual auth differs by pattern — important for protocol analysis.

**FIDO2 attestation vs assertion:** During registration, the authenticator produces an attestation (proof of device type/model + new public key). During authentication, it produces an assertion (signature on challenge with user's private key). Servers typically require attestation only during registration to verify the authenticator is a real FIDO2 device.

**TLS 1.3 transcript hash is cumulative:** The CertificateVerify signature covers a hash of the entire transcript up to that point (ClientHello + ServerHello + EncryptedExtensions + Certificate). This prevents replay attacks and ensures the signature commits to the specific ephemeral key exchange that was performed — binding authentication to the specific session's key material.
