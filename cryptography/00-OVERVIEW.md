# 00 — Cryptography Overview

## Security Definitions, Computational Assumptions, Cryptographic Primitives

---

## Big Picture: The Cryptographic Stack

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         CRYPTOGRAPHY FRAMEWORK                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  HARDNESS ASSUMPTIONS (complexity-theoretic foundation)                    │
│   One-way functions (OWF) — minimal assumption for symmetric               │
│   Factoring (RSA), discrete log (DL/EC), LWE/SIS (lattice) — asymmetric   │
│   Hash functions modeled as random oracles (ROM proofs)                    │
│                                                                            │
│  CRYPTOGRAPHIC PRIMITIVES                                                  │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Symmetric (shared key)             │  Asymmetric (public key)      │  │
│  │  Block ciphers: AES                 │  PKE: RSA-OAEP, ECIES         │  │
│  │  Stream ciphers: ChaCha20           │  Signatures: RSA-PSS, ECDSA   │  │
│  │  MACs: HMAC, Poly1305, CMAC         │  Key exchange: DH, ECDH       │  │
│  │  Hash: SHA-2/3, BLAKE3              │  IBE, ABE (advanced)          │  │
│  │  AEAD: AES-GCM, ChaCha20-Poly1305   │  Pairings: BLS, zk-SNARK      │  │
│  │  KDF: HKDF, Argon2id               │                               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  SECURITY DEFINITIONS                                                      │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Confidentiality: IND-CPA, IND-CCA1, IND-CCA2                       │  │
│  │  Integrity/Auth: EUF-CMA, sUF-CMA                                   │  │
│  │  Authenticated Encryption: AEAD = IND-CCA2 + INT-CTXT              │  │
│  │  ZK: completeness + soundness + zero-knowledge                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  PROTOCOLS (compose primitives with security reduction proofs)             │
│  TLS 1.3, Signal, SSH, Noise framework, certificate transparency          │
│                                                                            │
│  ADVANCED (ZK, MPC, FHE, post-quantum)                                    │
│  SNARKs/STARKs, garbled circuits, Kyber/Dilithium, LWE                    │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Perfect Secrecy vs Computational Security

```
PERFECT (INFORMATION-THEORETIC) SECURITY — Shannon 1949:
  Adversary has unbounded computation; security must hold against any algorithm
  One-time pad: K ∈ {0,1}ⁿ uniform; C = M ⊕ K
    Perfect secrecy: Pr[M=m | C=c] = Pr[M=m] for all m, c
    Proof: each ciphertext c corresponds to exactly one plaintext per key choice;
      since K uniform, all plaintexts equally likely → |C(m,k)| = 1 unique k → uniform
  Shannon's theorem: perfect secrecy → |K| ≥ |M| (key as long as message)
  Consequence: one-time pad is impractical (key management = message management)

  Other IT-secure primitives: secret sharing, information-theoretic MACs
  Information theory bridge: perfect secrecy ↔ H(M|C) = H(M)  (entropy of M given C = entropy of M)

COMPUTATIONAL SECURITY:
  Restrict adversary to probabilistic polynomial-time (PPT) Turing machines
  Security = advantage of best PPT adversary is negligible in security parameter λ
  negligible(λ): function ε(λ) such that ∀c > 0, ∃N: ∀λ>N, ε(λ) < 1/λ^c
  Concrete: "128-bit security" = no attacker running 2¹²⁸ operations can distinguish

  MIT TCS bridge: PPT ↔ class BPP; negligible ↔ below any inverse polynomial;
    computational indistinguishability = BPP can't tell apart → statistical distance negligible

WHY COMPUTATIONAL SECURITY IS SUFFICIENT:
  Running 2¹²⁸ operations at 10¹⁸ operations/sec (1 EFlop/s) = 10²⁰ years
  All known cryptanalysis against 256-bit AES: ~2¹¹⁵ for 9-round reduced (not full)
  Full 256-bit AES: no known attack better than 2¹²⁸; safe margin
```

---

## 2. Security Definitions (Game-Based)

```
SECURITY GAMES: adversary A interacts with challenger C; A wins if distinguishes or forges
  A's advantage: Adv[A] = |Pr[A wins] - 1/2| (for distinguishing games)
  Scheme is secure if Adv[A] is negligible for all PPT A

IND-CPA — INDISTINGUISHABILITY UNDER CHOSEN-PLAINTEXT ATTACK:
  1. Challenger generates (pk, sk) or derives key
  2. Adversary A queries encryption oracle (adaptive; polynomially many queries)
  3. A submits challenge pair (m₀, m₁)
  4. Challenger encrypts mb (b ← {0,1}) → returns ciphertext c*
  5. A outputs b' ∈ {0,1}
  Adv_CPA[A] = |Pr[b'=b] - 1/2|

  Necessary condition: encryption must be randomized (or stateful)
    Deterministic cipher CANNOT be IND-CPA (repeat query → replay attack)
  Sufficient for confidentiality in most practical settings
  Not sufficient against active attackers who modify ciphertexts

IND-CCA2 — ADAPTIVE CHOSEN-CIPHERTEXT ATTACK:
  Same as CPA, but: A also has decryption oracle before AND AFTER challenge
  Only restriction: A cannot query c* itself to decryption oracle
  "Adaptive" = after seeing c*, A can query other ciphertexts related to c*
  CCA2 is the gold standard for PKE: captures adaptive adversaries

  Important: IND-CCA2 ≠ INT-CTXT (does not prevent ciphertext forgery per se;
    but INT-CTXT + IND-CPA → IND-CCA2 for AEAD)

EUF-CMA — EXISTENTIAL UNFORGEABILITY UNDER CHOSEN-MESSAGE ATTACK:
  1. Adversary A has signing oracle (sign any messages of choice)
  2. A outputs (m*, σ*) where m* is NOT in set of signed messages
  3. A wins if σ* is a valid signature on m*
  EUF-CMA secure signature: no PPT A wins with non-negligible advantage

  Existential: A can choose which message to forge (not predefined)
  Stronger: strong EUF-CMA (sUF-CMA) — A cannot even produce new valid
    (message, signature) pair for previously signed messages (matters when
    multiple valid signatures can exist per message, e.g., malleability)

INT-CTXT — INTEGRITY OF CIPHERTEXTS:
  Adversary cannot produce valid ciphertext that decrypts to any message
  (even if forged message appears trivially modified)
  AEAD = IND-CPA + INT-CTXT → automatically IND-CCA2
```

---

## 3. Hardness Assumptions Hierarchy

```
ASSUMPTION HIERARCHY (stronger assumptions → more efficient schemes; less conservative):

  OWF (one-way function) — minimal assumption:
    f: {0,1}* → {0,1}* easy to compute; hard to invert with non-negl prob
    Believed to exist (equivalent to P ≠ NP is NOT sufficient — OWF existence
      would imply P ≠ NP but is strictly stronger in complexity-theoretic sense)
    OWF → PRG (pseudorandom generator) [Hastad et al.]
    PRG → PRF (pseudorandom function) [GGM construction]
    PRF → PRP (pseudorandom permutation) → PRF ↔ PRP for large block (luby-rackoff)

  FACTORING ASSUMPTION:
    Factor n = p × q (p, q prime, ~2048-bit) in time subexponential is hard
    Best known: GNFS (general number field sieve) = exp(O(n^{1/3} log^{2/3} n))
    2048-bit RSA: ~2¹¹² security; 3072-bit: ~2¹²⁸ NIST SP 800-131A

  DISCRETE LOGARITHM (DL):
    Given g, g^x in group G: find x
    Best known for general group (BSGS): O(√|G|) → need |G| ≈ 2²⁵⁶ for 128-bit security
    Elliptic curves: no sub-exponential algorithm known → 256-bit curve ≈ 128-bit security
    DH assumption: given g^a, g^b → g^{ab} is hard (DDH, CDH variants)

  LATTICE ASSUMPTIONS (post-quantum relevant):
    LWE (Learning With Errors): given A and b = As + e (e small error), find s
    SIS (Short Integer Solution): find short x with Ax = 0 (mod q)
    Quantum computer does NOT help significantly for lattice problems
    Ring-LWE: LWE over polynomial ring R_q = Z_q[x]/(x^n+1) → more efficient

  RANDOM ORACLE MODEL (ROM):
    H: {0,1}* → {0,1}^λ modeled as truly random function
    No efficient algorithm can distinguish H from random oracle
    ROM proofs: strong security guarantees IF model is correct
    Standard model proofs: no ROM assumption; stronger but harder/less efficient

COMPUTATIONAL vs DECISIONAL:
  CDH: given g^a, g^b, compute g^{ab}
  DDH: given g^a, g^b, (g^{ab} or g^c): distinguish c ← ℤ_q randomly
  DDH → CDH (DDH is stronger assumption)
  In elliptic curves: DDH hard in generic groups; DDH may be easy in some pairing-friendly curves
```

---

## 4. Reduction Proofs and Hybrid Arguments

```
SECURITY REDUCTION STRUCTURE:
  To prove scheme S is secure assuming hard problem P:
  Assume: adversary A breaks S with advantage ε
  Construct: reduction B that uses A to solve P

  ┌─────────────────────────────────────────────────────────────────┐
  │  Hard problem P         Scheme S                                │
  │  challenger             reduction B             adversary A     │
  │  ────────────           ───────────             ───────────     │
  │  gives challenge    →   simulates A's           attacks S       │
  │  instance             oracle queries      →   with advantage ε  │
  │                         translates A's                         │
  │  ←─────────────────     A's forgery/          ────────────      │
  │  solves P               distinction                             │
  └─────────────────────────────────────────────────────────────────┘

  If P is hard: ε must be negligible (otherwise B would efficiently solve P)
  "Tight reduction": Adv_P[B] ≥ Adv_S[A] (no loss)
  "Loose reduction": Adv_P[B] ≥ Adv_S[A] / poly(λ) (some loss; affects key lengths)

HYBRID ARGUMENT:
  Sequence of games G₀, G₁, ..., Gₙ
  G₀ = real game; Gₙ = ideal game (trivially secure; distinguishing = trivial)
  Between consecutive games: Pr[A wins Gᵢ] ≈ Pr[A wins Gᵢ₊₁] (indistinguishable)
  Triangle inequality: |Pr[G₀] - Pr[Gₙ]| ≤ Σᵢ |Pr[Gᵢ] - Pr[Gᵢ₊₁]| = negligible

  Example: IND-CPA game for AES-CTR
    G₀: real AES-CTR game
    G₁: replace AES_k with true PRF — indistinguishable if AES is PRF
    G₂: replace PRF output with truly random XOR mask — indistinguishable (random XOR)
    G₂: indistinguishable (A sees random ciphertext) → advantage = 0

MIT TCS bridge:
  Hybrid argument = standard technique in complexity; parallels in randomized complexity
  Computational indistinguishability = statistical distance negligible for PPT samplers
  Same tools: distinguisher D, hybrid sequences, triangle inequality
```

---

## 5. Primitives Taxonomy

```
SYMMETRIC CRYPTOGRAPHY:
  ┌────────────────────────────────────────────────────────────────┐
  │  Block cipher: AES-128/192/256; output pseudorandom if key unk│
  │  Stream cipher: ChaCha20; keystream XOR'd with plaintext       │
  │  Hash: SHA-2, SHA-3, BLAKE3; collision/preimage resistance     │
  │  MAC: HMAC, CMAC, Poly1305; integrity + authentication         │
  │  AEAD: AES-GCM, ChaCha20-Poly1305; confidentiality + integrity │
  │  KDF: HKDF; derive keying material from high-entropy secret    │
  │  Password hash: Argon2id, scrypt; slow + memory-hard           │
  └────────────────────────────────────────────────────────────────┘

ASYMMETRIC CRYPTOGRAPHY:
  ┌────────────────────────────────────────────────────────────────┐
  │  PKE: RSA-OAEP (factoring), ECIES (ECDH + symmetric)          │
  │  Signatures: RSA-PSS, ECDSA, EdDSA (Ed25519)                  │
  │  Key exchange: Diffie-Hellman (DH), ECDH, X25519              │
  │  IBE: Identity-Based Encryption (pairing-based; Boneh-Franklin)│
  │  Pairings: bilinear maps; e: G₁ × G₂ → Gₜ; BLS signatures    │
  └────────────────────────────────────────────────────────────────┘

ADVANCED PRIMITIVES:
  ┌────────────────────────────────────────────────────────────────┐
  │  Zero-Knowledge: Schnorr, Fiat-Shamir, Pedersen, SNARKs/STARKs│
  │  MPC: garbled circuits, secret sharing, GMW, oblivious transfer│
  │  FHE: fully homomorphic encryption (BFV, CKKS, TFHE)          │
  │  Post-quantum: Kyber (MLWE), Dilithium (MSIS), SPHINCS+        │
  └────────────────────────────────────────────────────────────────┘

SECURITY PROPERTY REQUIREMENTS BY USE CASE:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Use Case               │ Required Primitive  │ Required Property     │
  ├──────────────────────────────────────────────────────────────────────┤
  │  Encrypt stored data    │ AEAD (AES-GCM)      │ IND-CCA2 + INT-CTXT  │
  │  Authenticated channel  │ TLS 1.3             │ Forward secrecy + AE  │
  │  Password storage       │ Argon2id            │ Memory-hard + salted  │
  │  Digital signature      │ Ed25519             │ EUF-CMA               │
  │  Key derivation         │ HKDF                │ PRF security          │
  │  Commitment             │ Pedersen / hash     │ Binding + hiding      │
  │  Anonymous credentials  │ BBS+ / ZK proofs    │ Unlinkability         │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 6. Security Parameter and Concrete Security

## 6a. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Encrypt + authenticate data at rest? | AEAD (AES-256-GCM or ChaCha20-Poly1305); target IND-CCA2 + INT-CTXT |
| Need only integrity, not confidentiality? | HMAC-SHA256 or Poly1305; target EUF-CMA |
| Protocol providing authenticated channel? | TLS 1.3; target forward secrecy + IND-CCA2 per session |
| Sign data for non-repudiation? | Ed25519 (EUF-CMA); sUF-CMA if malleability matters |
| ROM proofs acceptable? | Yes for deployed protocols with no standard-model alternative; ROM proofs are strong evidence — attacks typically require breaking the hash directly |
| Standard model required? | When protocol must be proven secure without hash-function assumptions (e.g., some regulatory contexts); accept less efficient schemes |
| Hardness assumption for new KEM? | Module-LWE (ML-KEM) for PQC-ready systems; ECDH (X25519) for classical-only; hybrid for transition |
| Hardness assumption for new signatures? | Ed25519 (ECDLP) for classical; ML-DSA (Module-LWE + SIS) for PQC; hybrid both |
| Key length for 128-bit security? | AES-128, SHA-256, P-256/X25519, RSA-3072 (classical); ML-KEM-768, ML-DSA-65 (PQC) |
| Key length for 256-bit classical / 128-bit quantum? | AES-256, SHA-512, P-521, RSA-15360; ML-KEM-768 already ~192-bit quantum |
| Algorithm agility requirement? | Always: version field + algorithm ID in any persistent format or protocol wire format |
| Which security definition does CBC achieve? | IND-CPA only (not IND-CCA2); padding oracle attacks break it under active adversaries |
| Which security definition does AEAD achieve? | IND-CCA2 + INT-CTXT simultaneously; the gold standard for symmetric encryption |

---

```
SECURITY PARAMETER λ:
  All algorithms take λ as input (in unary: 1^λ) → key lengths, group sizes scale with λ
  Asymptotic: scheme is secure if Adv[A] is negligible in λ for all PPT A
  Concrete: for specific λ, attacker with specific resources cannot win

BIT SECURITY LEVELS:
  n-bit security: best attack requires ~2ⁿ operations
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Security │ Symmetric     │ RSA / DH      │ ECC          │ Quantum  │
  │  Level    │               │               │              │ safe?    │
  ├──────────────────────────────────────────────────────────────────────┤
  │  80-bit   │ AES-80 (dead) │ RSA-1024      │ P-160 (dead) │  No      │
  │  112-bit  │ 3DES (legacy) │ RSA-2048      │ P-224        │  No      │
  │  128-bit  │ AES-128       │ RSA-3072      │ P-256/X25519 │  No      │
  │  192-bit  │ AES-192       │ RSA-7680      │ P-384        │  No      │
  │  256-bit  │ AES-256       │ RSA-15360     │ P-521        │  ~128 PQ │
  └──────────────────────────────────────────────────────────────────────┘
  Note: AES-256 → ~128-bit security against Grover's quantum algorithm (halves exponent)
  For post-quantum: need 256-bit symmetric / larger lattice params

NIST KEY LENGTH GUIDANCE:
  NIST SP 800-131A: DES deprecated; RSA-1024 disallowed after 2015
  NIST SP 800-57: 112-bit minimum through 2030; 128-bit beyond 2030
  NIST FIPS 140-3: validated implementations required for federal use

ALGORITHM AGILITY:
  Design systems to swap algorithms without re-architecting
  Never hard-code algorithm in persistent format (e.g., "AES128-CBC" in database)
  Use algorithm identifiers (OIDs, string labels) in ciphertexts + key material
  TLS cipher suite negotiation: exemplary agility model
  Lesson: SSL → TLS 1.0 → TLS 1.3 required algorithm agility; non-agile systems forced rewrites
```

```
ENVELOPE ENCRYPTION PATTERN (canonical algorithm-agile design):

  Ciphertext envelope wire format:
  ┌──────────┬────────────┬─────────────┬──────┬─────────────┬─────┐
  │ version  │  alg_id    │ wrapped_key │  iv  │  ciphertext │ tag │
  │ (1 byte) │ (OID/str)  │  (DEK enc.) │(12B) │  (var)      │(16B)│
  └──────────┴────────────┴─────────────┴──────┴─────────────┴─────┘

  DEK  = Data Encryption Key (random per message; AES-256 key)
  KEK  = Key Encryption Key (stored in KMS/HSM; never in envelope)
  alg_id encodes: DEK algorithm (AES-256-GCM) + KEK wrap algorithm (AES-KW or RSA-OAEP)

  Algorithm rotation: increment version; use new alg_id for new DEK encryptions
  Old versions: decrypt using old DEK algorithm (still tagged in envelope); re-encrypt optional
  This pattern is universal: AWS KMS, HashiCorp Vault, Google Tink all follow it
  Key insight: algorithm is committed to in the ciphertext itself → migration path always available
```

---

## Theory → Applied Engineering Bridge

```
SECURITY DEFINITION → WHAT BREAKS WHEN IT'S MISSING:

  IND-CPA missing → CBC without random IV: BEAST attack (TLS 1.0 predictable IVs)
    Deterministic encryption → adversary queries same plaintext → recognizes ciphertext
    Fix: randomize encryption (random IV for CBC; random nonce for GCM)

  IND-CCA2 missing → RSA PKCS#1 v1.5: Bleichenbacher 1998 (10^6 queries → full decryption)
    CBC padding oracle: POODLE, Lucky13 (padding validity as oracle)
    Fix: AEAD modes (GCM, ChaCha20-Poly1305); RSA-OAEP; ECDH instead of RSA encryption

  INT-CTXT missing → Malleable ciphertext: flip bits in ciphertext → controlled plaintext changes
    CTR without MAC: attacker flips bit 0 of KS → flips bit 0 of plaintext
    Fix: encrypt-then-MAC or AEAD (which combines both)

  EUF-CMA missing → Signature forgery: RSA PKCS#1 v1.5 signature malleability (Bitcoin script bugs)
    Fix: RSA-PSS (sUF-CMA in ROM); Ed25519 (deterministic, no nonce reuse failure)

REDUCTION PROOF → CONCRETE PARAMETER CHOICE:

  "AES-128 is IND-CPA secure under PRF assumption" + best known PRF attacks on AES = O(2^128)
    → 128-bit security; adequate for current threat; use AES-256 for post-quantum margin

  "ECDSA is EUF-CMA under ECDLP" + best known ECDLP attacks on P-256 = O(2^128)
    → 128-bit security; but nonce reuse collapses to zero (no reduction needed)
    → In practice: use Ed25519 (deterministic nonce; same hardness assumption; safer implementation)

  "RSA-OAEP is IND-CCA2 under RSA-OWP assumption" + GNFS cost for RSA-2048 = ~2^112
    → 112-bit security (below 128-bit); NIST recommends RSA-3072 for 128-bit
    → X25519 (32-byte key) achieves same 128-bit security at 1/100th the key size

SECURITY GAME → ATTACK SCENARIO (practical mapping):

  IND-CPA game       ↔  passive eavesdropper; can encrypt chosen messages
  IND-CCA2 game      ↔  active attacker with decryption oracle (e.g., padding oracle, timing side-channel)
  EUF-CMA game       ↔  attacker who can obtain signatures on chosen messages (API access)
  sUF-CMA game       ↔  attacker who observes signatures + tries to produce any new (msg, sig) pair
  INT-CTXT           ↔  attacker who injects modified ciphertext and checks if decryption succeeds
```

## 7. Standard Bodies

```
NIST (National Institute of Standards and Technology):
  FIPS 197: AES
  FIPS 180-4: SHA-2 family
  FIPS 202: SHA-3 / Keccak
  FIPS 186-5: Digital Signature Standard (DSS): RSA, DSA, ECDSA, EdDSA
  FIPS 203: ML-KEM (Kyber) — 2024
  FIPS 204: ML-DSA (Dilithium) — 2024
  FIPS 205: SLH-DSA (SPHINCS+) — 2024
  SP 800-38D: GCM mode specification
  SP 800-135: KDF recommendations (HKDF, KBKDF)
  SP 800-186: Recommendations for Discrete Log-based Cryptography (ECC curves)

IETF RFCs (implementation standards):
  RFC 8446: TLS 1.3
  RFC 8032: Ed25519 / EdDSA
  RFC 7748: X25519, X448 (Diffie-Hellman)
  RFC 5869: HKDF
  RFC 8439: ChaCha20-Poly1305
  RFC 9180: HPKE (Hybrid Public Key Encryption) — combines KEM + AEAD

IETF CFRG (Crypto Forum Research Group — the other standards body):
  The CFRG is the IETF working group that standardizes cryptographic primitives for IETF protocols.
  Works independently from NIST; often faster; more willing to adopt Bernstein/Lange designs.
  CFRG outputs (not NIST FIPS):
    RFC 7748: X25519, X448 (ECDH — CFRG standard; NIST added Curve25519 much later in SP 800-186)
    RFC 8032: Ed25519, Ed448 (EdDSA — CFRG standard; NIST added in FIPS 186-5)
    RFC 8439: ChaCha20-Poly1305 (stream cipher AEAD — CFRG; no NIST FIPS equivalent)
    RFC 9180: HPKE — Hybrid Public Key Encryption (CFRG; used in TLS ECH, MLS)
    RFC 9497: OPAQUE — password-authenticated key exchange (CFRG draft → RFC)

  NIST vs CFRG tension:
    NIST: formal FIPS process; federal procurement requirement; P-256/P-384 focus
    CFRG: academic cryptographer input; faster adoption of clean designs (Curve25519, ChaCha20)
    Result: TLS 1.3 uses CFRG primitives (X25519, ChaCha20-Poly1305) that are NOT FIPS-approved
    FIPS-compliant TLS 1.3: must use P-256 (not X25519) and AES-GCM (not ChaCha20); tradeoffs

ETSI / ENISA: European standards; align with NIST; ETSI TS 103 744 on PQC migration

IACR (International Association for Cryptologic Research):
  Crypto, Eurocrypt, Asiacrypt: top venues; full papers freely available
  ePrint: preprint server (eprint.iacr.org) — read this for current state of art
```

---

## 8. Module Map

| Module | Core Content | Key Assumption |
|--------|-------------|----------------|
| 01-SYMMETRIC | AES internals, GCM, ChaCha20, hash, KDF | PRF/PRP security of AES |
| 02-ASYMMETRIC | RSA-OAEP, DH, ECC, pairings | Factoring, ECDLP, DDH |
| 03-PROTOCOLS | TLS 1.3, SSH, Signal/X3DH/Double Ratchet, Noise | Composition theorems, UC security |
| 04-ZK-MPC | Interactive proofs, Schnorr, SNARKs/STARKs, garbled circuits | DL, collision resistance, LWE |
| 05-POST-QUANTUM | LWE/SIS/NTRU, Kyber/Dilithium/SPHINCS+, migration | Lattice hardness; hash OWF |

---

## Common Confusion Points

**IND-CPA ≠ IND-CCA2:** AES-CBC is IND-CPA secure (given random IV) but NOT IND-CCA2 (padding oracle attack — POODLE, Lucky13). The 1998 Bleichenbacher attack on RSA PKCS#1 v1.5 is a CCA2 attack. Modern systems must be CCA2-secure: use OAEP for RSA, AEAD modes for symmetric.

**Semantic security = IND-CPA:** "Semantically secure" is the original Goldwasser-Micali definition (adversary learns nothing about plaintext from ciphertext). It is equivalent to IND-CPA. The game-based IND-CPA formulation is easier to use in proofs.

**Random Oracle Model security ≠ standard model security:** ROM proof says "secure if hash is truly random." No real hash function is truly random — this is a heuristic. However, ROM proofs are valuable: attacks on ROM-secure schemes typically require breaking the hash directly. Sponge construction (SHA-3) comes closest to ideal random oracle behavior.

**OWF existence does NOT follow from P≠NP:** This is a common misconception. P≠NP means NP-hard problems are hard in the worst case; OWFs must be hard on average (for random instances). There is no known implication P≠NP → OWF. OWF existence is a strictly stronger assumption.

**EUF-CMA vs sUF-CMA matters for malleability:** RSA PKCS#1 v1.5 signatures are EUF-CMA (hard to forge on new message) but NOT sUF-CMA (can produce second valid signature for same message due to DER encoding malleability). Bitcoin script bugs have resulted from this distinction.

**"256-bit security" for AES means different things against classical vs quantum:** Classical: 2²⁵⁶ operations (impossible). Quantum: Grover's algorithm gives square-root speedup → 2¹²⁸ operations. Still practically secure against quantum attackers. But RSA-2048 (128-bit classical) → broken in polynomial time by Shor's algorithm. This asymmetry drives the PQC migration.
