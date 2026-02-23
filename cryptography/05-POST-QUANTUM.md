# 05 — Post-Quantum Cryptography

## Quantum Threat, Lattice Problems, NIST PQC Standards, Migration

---

## Big Picture: Quantum Threat and PQC Landscape

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    POST-QUANTUM CRYPTOGRAPHY MAP                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  QUANTUM THREAT ASSESSMENT                                              │
│   Shor's: breaks RSA/ECDH/ECDSA in poly time (quantum circuits)        │
│   Grover's: √-speedup on symmetric — AES-128 → ~64-bit quantum sec     │
│   Timeline: CRQC likely 2030-2040 range (wide uncertainty)             │
│   HNDL: harvest now, decrypt later — urgent for long-lived secrets     │
│                                                                         │
│  PQC HARDNESS ASSUMPTIONS                                               │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  Lattice:   SIS (Short Integer Solution)                        │    │
│  │             LWE, Ring-LWE, Module-LWE                           │    │
│  │             Worst-case to avg-case reduction (Regev 2005)       │    │
│  │  Hash:      One-way function only; symmetric-crypto assumptions │    │
│  │  Code:      Syndrome decoding (McEliece, BIKE, HQC)            │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  NIST PQC STANDARDS (2024)                                              │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  FIPS 203: ML-KEM (Kyber) — lattice KEM                        │    │
│  │  FIPS 204: ML-DSA (Dilithium) — lattice signature              │    │
│  │  FIPS 205: SLH-DSA (SPHINCS+) — hash-based signature           │    │
│  │  FN-DSA (FALCON, NIST IR 8413): lattice signature (2024 final) │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  MIGRATION STRATEGY                                                     │
│   Hybrid KEM (classical + PQC): TLS, SSH NOW                           │
│   Algorithm agility: critical architectural requirement                │
│   CNSA 2.0: US government timeline for transition                      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Quantum Threat: Shor's and Grover's Algorithms

```
SHOR'S ALGORITHM (1994) — kills asymmetric crypto:
  Quantum algorithm running in polynomial time O(log³ n) on a QC
  Factors n = pq → breaks RSA
  Computes discrete log → breaks DH, DSA, ECDH, ECDSA, EdDSA
  Affected: ALL algorithms based on factoring or discrete log (classical or elliptic curve)

  Mechanism (simplified):
    Quantum period finding: find period r of f(x) = g^x mod n
    Shor reduces factoring to period finding via modular exponentiation
    QFT (Quantum Fourier Transform): finds period in O(log n) qubit operations
    r found → extract factors via gcd(a^{r/2} ± 1, n) with high probability
    Circuit depth: O(log³ n); number of (high-quality) qubits: ~2n for n-bit RSA

  What Shor's requires:
    Logically perfect qubits (fault-tolerant): ~millions of physical qubits for RSA-2048
    Physical qubit quality: ~0.1% error rate needed per gate; current best ~0.5%
    Error correction overhead: surface codes need ~1000 physical per logical qubit
    2024 state of art: ~1000-2000 noisy qubits (Quantinuum, IBM, Google); far from CRQC

  Timeline estimates (high uncertainty):
    Mosca's theorem: Pr[QC threat within X+Y years] × cost of migration Y → quantify urgency
    IBM: "relevant QC in ~10 years" (2022); many caveats
    NSA/CISA: CRQC expected "in 10-20 years" (2022)
    Most experts: 2030-2040 range; some think never at RSA-2048 scale
    Key insight: uncertainty is large; migrate now for long-lived secrets (HNDL)

GROVER'S ALGORITHM (1996) — weakens symmetric crypto:
  General unstructured search: find x such that f(x) = target in O(√N) quantum evaluations
  Classical search: O(N); Grover: O(√N) → QUADRATIC speedup (not exponential)
  Applied to AES key search: AES-128 (2¹²⁸ classical) → ~2⁶⁴ quantum operations
  Applied to hash preimage: SHA-256 (2²⁵⁶ classical) → ~2¹²⁸ quantum

  Mitigation: DOUBLE key lengths
    AES-128 → use AES-256 (provides ~128-bit quantum security)
    SHA-256 → use SHA-384 or SHA-512 (provides ~192/256-bit quantum security)
    HMAC-SHA256 → HMAC-SHA384 for quantum resistance
  Already done by most systems that care about long-term security

HARVEST NOW, DECRYPT LATER (HNDL):
  Adversary records TLS ciphertext today; stores for future quantum decryption
  Currently impractical to decrypt; post-CRQC: any session protected only by ECDH → breakable
  TLS without forward secrecy (static RSA): all recorded traffic decryptable
  TLS 1.3 with ECDHE: ephemeral keys; but ECDHE also broken by Shor's
  Urgency: secrets that must remain confidential for 10+ years → migrate NOW
  Examples: state secrets, health records, financial data, IP with long value horizon

QUANTUM-SAFE vs POST-QUANTUM:
  "Post-quantum" = secure against quantum computers (used by NIST)
  "Quantum-safe" = same; more colloquial
  "Quantum-resistant" = same
  NOT "quantum encryption" = quantum key distribution (QKD; different; based on physics)
```

---

## 2. Lattice Problems

```
LATTICES:
  Lattice L = {Σ bᵢ·zᵢ | zᵢ ∈ ℤ} for basis vectors {b₁,...,bₙ} in ℝⁿ
  Fundamental domain (parallelepiped); determinant det(L) = |det(B)| where B = basis matrix
  Shortest Vector Problem (SVP): find shortest nonzero vector in L
  Closest Vector Problem (CVP): given target t ∈ ℝⁿ, find closest lattice point

HARDNESS:
  SVP/CVP: NP-hard to approximate within constant factor; believed hard for all polytime algorithms
  Best known classical: BKZ lattice reduction; exponential time sub-exponential in dimension
  Best known quantum: no significant improvement over classical for SVP/CVP
    Quantum speedup on BKZ oracle: minor (Grover-assisted basis reduction → small constant factor)
  Why lattices: quantum computers offer no polynomial speedup

SIS (Short Integer Solution):
  Given matrix A ∈ ℤ_q^{n×m}, find short nonzero x ∈ ℤ^m with Ax = 0 mod q
  "Short": ||x|| ≤ β for some bound β
  Security: SIS_{n,m,q,β} is hard if approximating SVP in n-dim lattice is hard
  Binding property of hash functions: H(x) = Ax mod q is collision-resistant if SIS is hard
  Used in: Dilithium (signature), FALCON (signature)

LWE (Learning With Errors — Regev 2005):
  Distinguishing problem: given many samples (aᵢ, bᵢ = aᵢ·s + eᵢ mod q):
    s ∈ ℤ_q^n secret; aᵢ ∈ ℤ_q^n uniform random; eᵢ small error from distribution χ
    Is this real (LWE sample) or completely random?
  Decision LWE: distinguish LWE samples from uniform random pairs
  Search LWE: find s from samples

  Regev reduction: LWE is as hard as GapSVP on n-dim lattice (worst-case!)
    "Average-case hardness" — not just worst-case like NP-hardness
    Any efficient algorithm for LWE → efficient algorithm for GapSVP (quantum reduction)
    This is the KEY property distinguishing LWE from factoring (factoring has no such reduction)

RING-LWE (Ring Learning With Errors):
  LWE over polynomial ring R_q = ℤ_q[x]/(x^n + 1)
  Secret s ∈ R_q; noise e ∈ R_q (small); sample b = a·s + e for a ∈ R_q
  Efficiency: n² → n·log(n) (polynomial ring multiplication = NTT = fast)
  Key size: O(n) instead of O(n²) for matrix LWE
  Security: reduction to lattice problems on ideal lattices (slightly more structure; more assumptions)

MODULE-LWE (Module Learning With Errors):
  Generalization: over module M = R_q^k (k copies of R_q)
  A ∈ R_q^{k×k}; s ∈ R_q^k; b = As + e
  Parameter: k (module rank); k=1 → Ring-LWE; k→∞ → plain LWE
  Security: reduces to lattice problems on module lattices
  Tradeoff: k chosen for desired security level; Kyber uses k=2,3,4

PARAMETER SELECTION:
  n = LWE dimension; q = modulus; χ = error distribution (discrete Gaussian, σ)
  Security parameter: β = ||s||, ||e||; q/β ratio affects security
  Kyber-768: n=256, k=3, q=3329; σ≈1; provides ~NIST Level 3 (~AES-192 equiv)
  Best known attacks: primal attack (BKZ reduction), dual attack; require β-SVP of dimension ~n
```

---

## 3. ML-KEM (Kyber, NIST FIPS 203)

```
KYBER OVERVIEW:
  Based on Module-LWE; KEM (Key Encapsulation Mechanism)
  Replaces: ECDH/X25519 for key exchange; RSA-KEM for key transport
  FIPS 203 (2024): standardized as ML-KEM

PARAMETER SETS:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Variant     │ k │ Security  │ PK size │ SK size │ CT size │ SecLevel│
  ├──────────────────────────────────────────────────────────────────────┤
  │  ML-KEM-512  │ 2 │ ≈AES-128  │  800 B  │  1632 B │  768 B  │  1      │
  │  ML-KEM-768  │ 3 │ ≈AES-192  │ 1184 B  │  2400 B │ 1088 B  │  3      │
  │  ML-KEM-1024 │ 4 │ ≈AES-256  │ 1568 B  │  3168 B │ 1568 B  │  5      │
  └──────────────────────────────────────────────────────────────────────┘
  Compare: X25519 (Curve25519): 32-byte public key; 32-byte shared secret
  Kyber-768: 1184-byte public key — significant increase but manageable

KEY GENERATION:
  (ρ, σ) ← random seed
  A ← {expand seed ρ to matrix A ∈ R_q^{k×k}} (deterministic)
  s, e ← sample from error distribution χ^k (centered binomial)
  t = As + e  (public key "LWE sample")
  Public key: (ρ, t);  Private key: s

ENCAPSULATION (generates shared secret + ciphertext for recipient's public key):
  r ← random;  (r', key) = H(H(pk) || r)   (for implicit rejection)
  r₂, e₁, e₂ ← sample from χ^k using r' as seed
  u = Aᵀr₂ + e₁;  v = tᵀr₂ + e₂ + ⌊q/2⌋·m  (m = encoded key material)
  Ciphertext: (u, v) compressed;  Shared secret: KDF(key)

DECAPSULATION:
  Decrypt: m' = v - sᵀu ≈ v - sᵀ(Aᵀr₂ + e₁) ≈ tᵀr₂ + e₂ + ⌊q/2⌋m - sᵀAᵀr₂
           ≈ (As+e)ᵀr₂ + e₂ + ⌊q/2⌋m - sᵀAᵀr₂
           ≈ sᵀAᵀr₂ + eᵀr₂ + e₂ + ⌊q/2⌋m - sᵀAᵀr₂
           ≈ ⌊q/2⌋m + small noise
  Round to recover m' → re-derive key

FUJISAKI-OKAMOTO (FO) TRANSFORM:
  Basic Kyber is CPA-secure; add FO transform → CCA-secure KEM
  Re-encapsulate with recovered m'; compare with received ciphertext
  If mismatch: return pseudorandom output (implicit rejection; not decryption error)
  Security: IND-CCA2 in ROM assuming Module-LWE hardness
```

---

## 4. ML-DSA (Dilithium, NIST FIPS 204)

```
DILITHIUM OVERVIEW:
  Based on Module-LWE + Module-SIS; digital signature
  Replaces: ECDSA, Ed25519, RSA-PSS for digital signatures
  FIPS 204 (2024): standardized as ML-DSA; three parameter sets

PARAMETER SETS:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Variant     │ Security │ PK size │ SK size │ Sig size │ Level    │
  ├────────────────────────────────────────────────────────────────────┤
  │  ML-DSA-44   │ ≈AES-128 │ 1312 B  │  2528 B │  2420 B  │  2       │
  │  ML-DSA-65   │ ≈AES-192 │ 1952 B  │  4000 B │  3293 B  │  3       │
  │  ML-DSA-87   │ ≈AES-256 │ 2592 B  │  4864 B │  4595 B  │  5       │
  └────────────────────────────────────────────────────────────────────┘
  Compare: Ed25519: 32-byte public key, 64-byte signature
  Dilithium-65: 3293-byte signatures — significant increase

FIAT-SHAMIR WITH ABORTS:
  Design principle: Schnorr-like Fiat-Shamir but with rejection sampling for ZK property
  Naive F-S lattice signature leaks information about s in response z = r + s·c
    (z distribution depends on s → leaks secret)
  REJECTION SAMPLING: abort and retry if z is outside target distribution
    Repeat until z is "indistinguishable" from random within bounds
    Expected iterations: ~4-7; adds slight overhead but prevents leakage

SIGNING PROTOCOL (sketch):
  r ← small random poly; w = Ar (commitment)
  c = H(μ || w)  (challenge hash; μ = message hash)
  z = r + sc  (response)
  if ||z||∞ > γ₁ - β: ABORT; retry with new r
  Signature: (z, c, hints for decompression)

VERIFICATION:
  Recompute w' = Az - tc (where t = As+e from key gen)
  Check: H(μ || w') = c AND ||z||∞ ≤ γ₁ - β

SECURITY:
  Signing: Module-LWE (for ZK of s via Fiat-Shamir) + Module-SIS (unforgeability)
  EUF-CMA in ROM assuming both Module-LWE and Module-SIS hardness
  Deterministic signing supported (use PRF for randomness) — good for firmware w/o CSPRNG
```

---

## 5. FALCON and SLH-DSA (SPHINCS+)

```
FALCON (NIST FIPS 203 companion — FN-DSA):
  Based on NTRU lattices (different from Module-LWE/SIS)
  NTRU: uses polynomial ring Z[x]/(x^n-1); special structure; very efficient
  Gaussian sampling: sample from discrete Gaussian conditioned on a lattice; "trapdoor"
  Smallest signatures among NIST standards: Falcon-512 → 666 bytes; Falcon-1024 → 1280 bytes
  Limitation: complex implementation; Gaussian sampler is tricky for side-channel safety
  Use case: bandwidth-constrained applications where signature size matters more than complexity

SPHINCS+ (SLH-DSA, NIST FIPS 205):
  Hash-based: security relies ONLY on cryptographic hash function (OWF)
  No lattice; no number theory; no new mathematical assumptions
  Quantum security: Grover on hash → double output length; SHA3-256 → 128-bit quantum security

  STRUCTURE (Hypertree):
    FORS (Forest Of Random Subsets): one-time signature at leaf; signs message digest parts
    XMSS tree: few-time signature; certifies FORS keys
    Hypertree: layers of XMSS trees; root signs sub-roots; certifies whole hierarchy
    Top-level XMSS: signed by long-term key (hyptertree root = actual public key)

  Variants:
    SLH-DSA-SHA2-128f/s: fast (many-layer) vs small (few-layer); SHA-2 based
    SLH-DSA-SHAKE-128f/s: SHAKE-based
    128/192/256 = security level

  Key/Signature sizes:
    SLH-DSA-128f: PK = 32 bytes; SK = 64 bytes; Sig = 17,088 bytes (fast variant)
    SLH-DSA-128s: Sig = 7,856 bytes (small/slow variant — smaller sig, slower sign)
  Trade-off: large signatures; stateless (vs XMSS which is stateful)

  Stateless vs Stateful:
    XMSS/LMS (RFC 8391/8554): stateful hash-based; track which one-time keys used
      Smaller signatures (~2500 bytes); requires persistent state → risk of reuse on reset
    SPHINCS+: stateless; randomly chosen one-time keys + randomized message hashing
      Larger signatures; safer operationally (no state to maintain or lose)
```

---

## 6. Code-Based and Other Candidates

```
CLASSIC McELIECE (NIST finalist, not yet standardized as FIPS):
  Based on syndrome decoding problem (NP-complete)
  Goppa code: binary Goppa code; decoder = trapdoor
  Key generation: encode Goppa code; scramble matrix multiplication
  Encrypt: add controlled errors to codeword; decrypt: find codeword via decoder
  Security: oldest PQC assumption (1978 McEliece scheme)
  Problem: PUBLIC KEY is enormous: ~1 MB for Classic McEliece 460896
  Advantage: ciphertext and shared secret are small; well-studied; conservative

BIKE (Bit Flipping Key Encapsulation):
  Quasi-Cyclic MDPC codes (QC-MDPC); sparse parity check matrix
  Keys: ~3 KB; ciphertext: ~1.5 KB; much better than Classic McEliece
  Security concern: decryption failure probability (small but non-zero) + correlation attacks
  Status: NIST round 4 alternate candidate

HQC (Hamming Quasi-Cyclic):
  Similar to BIKE; different code family; better decryption failure analysis
  NIST round 4 alternate candidate alongside BIKE

CODE-BASED SUMMARY:
  Classic McEliece: extremely conservative but impractically large public keys
  BIKE/HQC: practical key sizes but younger security analysis; NIST round 4
  None yet as primary FIPS standard (lattice-based took primary slots)
```

---

## 7. Migration Strategy

```
MIGRATION TIMELINE DRIVERS:
  Harvest now, decrypt later: migrate KEM/KEX immediately for forward secrecy
  Long-lived certificates: if cert valid 10 years → start issuing PQC certs now
  Firmware/embedded: long development + deployment cycles; start PQC design now
  CNSA 2.0 (NSA, 2022): US national security systems timeline:
    2025: begin testing PQC software implementations
    2030: only allow PQC for new capabilities in most systems
    2033: full transition completed for most systems

HYBRID SCHEMES (classical + PQC combined):
  Rationale: ML-KEM is new; may have undiscovered weaknesses; classical ECDH is well-studied
    Combine: if either component is secure → combined KEM is secure
  IETF RFC 9496 (hybrid KEM): X25519 + ML-KEM-768 → shared secret = KDF(X25519_secret || ML-KEM_secret)
  TLS 1.3 key_share extension: clients send both X25519 AND ML-KEM key_share
    Google Chrome 2023: X25519Kyber768 (hybrid); Firefox 2024: similar
  SSH: OpenSSH 9.0+ supports mlkem768x25519 (hybrid KEM)
  OpenPGP: draft extension for PQC (hybrid ML-KEM + X25519; Dilithium + Ed25519)

X.509 CERTIFICATE TRANSITION:
  Current: ECDSA P-256 certificates; ~100 bytes signature; ~200 bytes cert overhead
  PQC cert: Dilithium-65 signature → 3293 bytes additional per cert; significant overhead
  Dual-key certificates: contain both classical key (for backward compat) + PQC key
    Larger cert; complexity; tooling support incomplete
  Certificate transparency: CT logs already handle large certs; latency impact minimal
  CA/Browser Forum: working on PQC certificate profiles (2024+)

CRYPTO AGILITY — ARCHITECTURAL REQUIREMENT:
  Never hard-code: don't encode "ECDH" or "SHA-256" in binary protocols without version field
  Design pattern: algorithm identifier in every message + key material
    ┌──────────────────────────────────────────────────────────────┐
    │  DO:   alg_id = "ML-KEM-768"; key_material = <bytes>        │
    │  DON'T: implicit assumption that all keys are 32-byte X25519 │
    └──────────────────────────────────────────────────────────────┘
  TLS: cipher suite negotiation → already agile
  HTTP security headers: HPKP (removed); Certificate Transparency → flexible
  Azure/AWS KMS: plan for algorithm versioning in all key management APIs

PRACTICAL MIGRATION PRIORITIES:
  ┌───────────────────────────────────────────────────────────────────────┐
  │  Tier │ System                │ Action                │ Urgency       │
  ├───────────────────────────────────────────────────────────────────────┤
  │  1    │ TLS key exchange      │ Add hybrid KEM now    │ Immediate     │
  │  1    │ Long-lived secrets    │ Reencrypt with PQC    │ Immediate     │
  │  2    │ TLS certificates      │ Plan dual-key certs   │ 2025-2027     │
  │  2    │ Code signing          │ Add Dilithium         │ 2025-2027     │
  │  3    │ Full PQC migration    │ Remove classical      │ 2030+         │
  │  3    │ Embedded/firmware     │ Start design now      │ Begin 2024    │
  └───────────────────────────────────────────────────────────────────────┘
```

---

## 8. Quantum Key Distribution (QKD) — Not PQC

```
QKD — WHAT IT IS AND ISN'T:
  Physics-based: uses quantum states (photon polarization) to distribute key
  Security: based on no-cloning theorem (can't copy quantum state → eavesdrop detection)
  Protocol: BB84 (Bennett-Brassard 1984); E91 (Ekert 1991)

  INFORMATION-THEORETICALLY SECURE key distribution (in theory)
  But: authenticated classical channel required (still needs classical crypto for authentication!)
  Physical limitations:
    Distance: optical fiber ~500 km max (attenuation + noise); requires trusted relay nodes
    Rate: ~10 kbps at 100 km; far less than TLS key establishment
    Hardware: dedicated quantum hardware required; not software-upgradable
    Cost: ~$100K-$1M per link
    Side-channel attacks: physical implementation attacks on QKD hardware (common in practice)

  NSA position: "QKD does not scale; PQC is the correct approach for US government"
  NIST: same; NSA CNSA 2.0 explicitly does NOT include QKD
  Conclusion: QKD is interesting physics; not the practical solution to quantum threat
    PQC (mathematical) is the practical, scalable solution

DO NOT CONFUSE QKD AND PQC:
  PQC: classical computers; software; scales to any internet protocol
  QKD: quantum hardware; point-to-point; doesn't scale; authentication still needed
```

---

## 9. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does Shor's algorithm break? | RSA, DH, ECDH, ECDSA, EdDSA — all public-key based on factoring or discrete log |
| What does Grover's break? | Symmetric (squares workload, doubles required key length); AES-128 → use AES-256 |
| HNDL urgency means? | Migrate key exchange (TLS ECDHE) NOW for long-lived secrets — attackers already capturing traffic |
| NIST PQC primary KEM? | ML-KEM (Kyber), FIPS 203; use ML-KEM-768 for 192-bit equiv security |
| NIST PQC primary signatures? | ML-DSA (Dilithium) FIPS 204; SLH-DSA (SPHINCS+) FIPS 205; FN-DSA (FALCON) |
| LWE worst-case reduction significance? | Hardness of LWE ← hardness of SVP; average-case hard → much stronger than NP-hard |
| Hybrid KEM construction? | KDF(classical_secret || pqc_secret); if either component secure → combined secure |
| Kyber-768 public key size vs X25519? | ML-KEM-768: 1184 bytes vs X25519: 32 bytes — ~37× larger but acceptable |
| Dilithium-65 signature size vs Ed25519? | ML-DSA-65: 3293 bytes vs Ed25519: 64 bytes — ~51× larger |
| SPHINCS+ vs Dilithium trade-off? | SPHINCS+: conservative (hash-only assumption); large sigs (8-50KB); Dilithium: smaller sigs; lattice assumption |
| QKD vs PQC recommendation? | PQC (NSA/NIST position); QKD doesn't scale and still needs classical auth |
| Rejection sampling in Dilithium purpose? | Prevent information leakage about secret key s through signature response distribution |
| Module-LWE vs Ring-LWE vs plain LWE? | Module (k-rank) ⊃ Ring (k=1) ⊃ LWE (module over ℤ); efficiency/assumption tradeoff |
| CNSA 2.0 full transition target year? | 2033 for most NSS (national security systems) |

---

## Common Confusion Points

**Shor's breaks ECC too, not just RSA:** A common misconception is that elliptic curve crypto is somehow "quantum safe" because the math is different. Shor's period-finding generalizes to compute discrete logarithms in ANY cyclic group, including elliptic curve groups. P-256 and X25519 are broken by Shor's just as thoroughly as RSA-2048. Only lattice-based, hash-based, and code-based crypto survive.

**Post-quantum ≠ quantum computing:** PQC uses classical computers; it's ordinary software on ordinary CPUs. "Post-quantum" means "secure against quantum computers." Quantum key distribution (QKD) uses actual quantum hardware for key exchange and is completely different. The confusion arises because both have "quantum" in the name.

**LWE security reduction is not a proof of hardness:** Regev's reduction shows "if you can solve LWE efficiently, you can solve GapSVP efficiently." This is a conditional statement — it doesn't prove LWE is hard. It means LWE is at LEAST as hard as GapSVP, which is believed hard based on ~40 years of lattice research. It provides much stronger evidence than RSA (no equivalent worst-case reduction to average-case for factoring).

**Hybrid KEM security argument:** "If EITHER component is secure, the hybrid is secure" requires careful construction. The simple HKDF combination KDF(k₁ || k₂) achieves this — an adversary must break both to distinguish output from random. This works because KDF is a PRF: if k₁ is pseudorandom (classical KEM secure), then output is pseudorandom even if k₂ is adversarially known (and vice versa). This requires PRF-security of KDF, not just collision resistance.

**SPHINCS+ is stateless but XMSS/LMS are not:** XMSS and LMS (RFC 8391/8554) are older hash-based signatures that are stateful — you must track which one-time keys have been used. If device resets and reuses a one-time key → security broken. SPHINCS+ solves this with randomized message hashing and random tree selection. Stateless = operationally simpler but larger signatures (~3-7KB vs ~1-3KB for XMSS).

**Migration urgency varies by data lifetime:** A TLS session protecting an ephemeral web request has no HNDL risk (who cares about yesterday's cat video?). But: a TLS session carrying health records, corporate secrets, or government communications might still need to be confidential in 2040. The correct question is: "If an adversary records this traffic today, what is the harm if decrypted in 10-20 years?" That answer determines whether to migrate NOW vs 2027 vs 2030.
