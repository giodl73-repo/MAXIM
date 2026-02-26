# 01 — Symmetric Cryptography

## AES Internals, Modes of Operation, Authenticated Encryption, Hash Functions, KDFs

---

## Big Picture: Symmetric Primitive Stack

```
┌───────────────────────────────────────────────────────────────────────────┐
│                     SYMMETRIC CRYPTOGRAPHY STACK                          │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  APPLICATION LAYER                                                        │
│   Disk encryption: AES-XTS (dm-crypt/LUKS, BitLocker)                    │
│   Network encryption: AES-GCM or ChaCha20-Poly1305 (TLS 1.3)             │
│   Database field encryption: AES-SIV (nonce-misuse resistant)            │
│   Password storage: Argon2id                                              │
│                              │                                            │
│                              ▼                                            │
│  AEAD (AUTHENTICATED ENCRYPTION WITH ASSOCIATED DATA)                     │
│   AES-256-GCM: NIST standard; hardware acceleration (AES-NI + CLMUL)     │
│   ChaCha20-Poly1305 (RFC 8439): software-fast; no timing side-channel     │
│   AES-SIV (RFC 5297): nonce-misuse resistant (deterministic)              │
│   AES-CCM: older; NIST; used in some constrained environments             │
│                              │                                            │
│                              ▼                                            │
│  BUILDING BLOCKS                                                          │
│   Block cipher: AES-128/192/256 (SP-network; FIPS 197)                   │
│   Stream cipher: ChaCha20 (ARX design; RFC 8439)                         │
│   Universal hash: GHASH (GF(2¹²⁸)); Poly1305 (GF(2¹³⁰-5))              │
│   Cryptographic hash: SHA-2/3, BLAKE3                                    │
│                              │                                            │
│                              ▼                                            │
│  KEY DERIVATION                                                           │
│   HKDF: extract-then-expand from high-entropy secrets (RFC 5869)         │
│   Argon2id: memory-hard password hashing (PHC winner 2015)               │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 1. AES Mathematical Foundation

```
FINITE FIELD GF(2⁸):
  Elements: polynomials of degree ≤ 7 with binary coefficients
  = {a₇x⁷ + a₆x⁶ + ... + a₁x + a₀  |  aᵢ ∈ {0,1}}
  Represent as byte: {a₇,a₆,...,a₀} ↔ 0x00-0xFF

  Reduction polynomial: m(x) = x⁸ + x⁴ + x³ + x + 1  (FIPS 197; irreducible over GF(2))
  Addition: XOR of polynomial coefficients (no carry)
  Multiplication: polynomial multiply mod m(x); efficient via carry-less multiply (PCLMULQDQ)

SHANNON'S CONFUSION AND DIFFUSION:
  Confusion: each ciphertext bit depends on multiple key bits (S-box provides this)
  Diffusion: changing 1 plaintext bit → ~50% ciphertext bits change (MixColumns provides this)
  AES: substitution-permutation network (SPN) — alternating S-layers (SubBytes) and P-layers
    (ShiftRows + MixColumns); key mixed at each round (AddRoundKey)

AES STATE:
  128-bit block arranged as 4×4 matrix of bytes:
  ┌──┬──┬──┬──┐
  │s₀│s₄│s₈│s₁₂│
  │s₁│s₅│s₉│s₁₃│
  │s₂│s₆│s₁₀│s₁₄│
  │s₃│s₇│s₁₁│s₁₅│
  └──┴──┴──┴──┘
  Columns are primary unit; rows are secondary
```

---

## 2. AES Round Operations

```
ROUND STRUCTURE:
  AES-128: 10 rounds;  AES-192: 12 rounds;  AES-256: 14 rounds
  Each round (except last): SubBytes → ShiftRows → MixColumns → AddRoundKey
  Final round: SubBytes → ShiftRows → AddRoundKey  (no MixColumns)
  Key expansion: generates round keys; described in §3

SUBBYTES — CONFUSION:
  Apply S-box to each byte independently
  S-box(b) = GF(2⁸) multiplicative inverse of b, then affine transform over GF(2)
  S-box(0x00) = 0x63 (special case: 0 has no inverse; set by affine transform)
  Key property: no fixed points (S-box(a) ≠ a), algebraic degree high, balancedness
  Implementation: 256-entry lookup table (1 KB) OR compute GF(2⁸) inverse on-the-fly
  Security role: nonlinear layer; prevents linear attacks (algebraic attacks)

SHIFTROWS — BYTE PERMUTATION:
  Row i is rotated left by i positions:
  Row 0: no shift   [s₀, s₄, s₈, s₁₂]  → [s₀, s₄, s₈, s₁₂]
  Row 1: shift 1    [s₁, s₅, s₉, s₁₃]  → [s₅, s₉, s₁₃, s₁]
  Row 2: shift 2    [s₂, s₆, s₁₀, s₁₄] → [s₁₀, s₁₄, s₂, s₆]
  Row 3: shift 3    [s₃, s₇, s₁₁, s₁₅] → [s₁₅, s₃, s₇, s₁₁]
  Purpose: ensures bytes from different columns are mixed in MixColumns

MIXCOLUMNS — DIFFUSION:
  Treats each 4-byte column as polynomial over GF(2⁸) mod (x⁴ + 1)
  Multiply by fixed polynomial: {03}x³ + {01}x² + {01}x + {02}  (hex bytes)
  Matrix form per column:
  ┌b₀┐   ┌02 03 01 01┐ ┌a₀┐
  │b₁│ = │01 02 03 01│ │a₁│  (all arithmetic in GF(2⁸))
  │b₂│   │01 01 02 03│ │a₂│
  └b₃┘   └03 01 01 02┘ └a₃┘
  MDS matrix: maximum distance separable; changing 1 input byte → all 4 output bytes change
  Diffusion: within 2 rounds, every output byte depends on every input byte (wide trail strategy)

ADDROUNDKEY:
  XOR state with round key (same size: 16 bytes = 128 bits)
  Only operation that introduces key material
  Invertible trivially (XOR again)

AVALANCHE EFFECT:
  After 2 rounds: 1 bit change → all 128 bits unpredictably changed
  Strict avalanche criterion: each output bit changes with Prob=0.5 on 1 input bit flip
  Wide trail strategy (Daemen/Rijmen): ShiftRows ensures inter-column diffusion; MixColumns
    provides 4-byte diffusion → after 2 rounds: branch number = 9 (at least 9 active S-boxes)
```

---

## 3. AES Key Schedule

```
KEY SCHEDULE (AES-128; 10 round keys of 16 bytes = 176 bytes total):
  Original key: w[0..3]  (4 words of 4 bytes)
  Round key i: w[4i .. 4i+3]

  Expansion:
    For i = 4 to 43:
      temp = w[i-1]
      if i mod 4 == 0:
        temp = SubWord(RotWord(temp)) ⊕ Rcon[i/4]
      w[i] = w[i-4] ⊕ temp

  RotWord: rotate 4-byte word left 1 byte: [a,b,c,d] → [b,c,d,a]
  SubWord: apply S-box to each byte of 4-byte word
  Rcon[i]: round constant = [2^{i-1} in GF(2⁸), 0, 0, 0]
    Rcon[1]=01, Rcon[2]=02, Rcon[3]=04, Rcon[4]=08, Rcon[5]=10, ...

  AES-256 key schedule: more complex; 14 rounds; SubWord applied more frequently
  Key schedule weakness: related-key attacks exist on AES-192/256 (not on AES-128);
    not relevant in practice (sound key derivation → independent keys)

HARDWARE IMPLEMENTATION (AES-NI):
  Intel/AMD: AESENC, AESENCLAST, AESDEC, AESDECLAST instructions
  Single round: 1-8 cycles depending on architecture (Skylake: 4-cycle throughput, 1-cycle latency)
  Combined with PCLMULQDQ (carry-less multiply for GHASH): full AES-GCM in hardware
  Performance: ~0.5 bytes/cycle throughput on modern CPUs with AES-NI
  ARM: ARM Crypto Extension (AESE, AESMC instructions) — same concept
```

---

## 4. Block Cipher Modes

```
ECB (Electronic Codebook) — NEVER USE:
  C[i] = AES_k(P[i])   (independent block encryption)
  Fatal flaw: identical plaintext blocks → identical ciphertext blocks
  Pattern leakage: PNG image encrypted with ECB shows image outline
  No randomness; deterministic; trivially distinguishable

CBC (Cipher Block Chaining):
  C[0] = AES_k(P[0] ⊕ IV)  ;  C[i] = AES_k(P[i] ⊕ C[i-1])
  IV must be random (unpredictable) per message → IND-CPA requires it
  Sequential encryption (cannot parallelize); parallel decryption
  PKCS#7 padding required for non-block-aligned plaintexts
  PADDING ORACLE ATTACK:
    If decryption oracle leaks whether padding is valid:
    Attacker can decrypt any ciphertext 1 byte at a time via chosen-ciphertext queries
    POODLE (CBC over SSL 3.0): exploits CBC padding oracle
    TLS 1.0 BEAST attack: predictable IV in CBC stream
    Fix: authenticated encryption (don't use bare CBC for confidentiality+integrity)

CTR (Counter mode):
  KS[i] = AES_k(nonce || counter_i)  ;  C[i] = P[i] ⊕ KS[i]
  Turns block cipher into stream cipher
  Fully parallelizable (encrypt + decrypt both); no padding needed
  CRITICAL: (key, nonce) pair must NEVER be reused
    Reuse: C₁ = P₁ ⊕ KS; C₂ = P₂ ⊕ KS → C₁ ⊕ C₂ = P₁ ⊕ P₂ (plaintexts XOR'd; fatal)
  CTR alone: no authentication → malleable (flip bits in KS to flip plaintext bits)

GCM (Galois/Counter Mode) = AEAD:
  Encryption: CTR mode (AES_k(J₀+i) for counter sequence)
  Authentication: GHASH over (AAD || ciphertext || lengths)
  Tag: T = GHASH(H, AAD||C) ⊕ AES_k(J₀)  where H = AES_k(0)
  GHASH: polynomial hash over GF(2¹²⁸) with key H
    GHASH(H, X) = (X₁·H^m + X₂·H^{m-1} + ... + Xₘ·H) mod poly(2¹²⁸)

  Properties:
    IND-CCA2 + INT-CTXT: provides full AEAD security
    Nonce must be unique: 96-bit nonce (recommended); 12 bytes
    GCM nonce reuse catastrophe: if two messages use same (key, nonce):
      attacker gets H (GHASH key) and can forge tags on any ciphertext
    Standard: 96-bit random nonce → 2³² messages per key at <2⁻³² forgery prob
    Limit: encrypt at most 2³⁶ bytes per (key, nonce); rekey after 2³² messages

CCM (Counter with CBC-MAC):
  NIST SP 800-38C; older; CBC-MAC then CTR encrypt; two passes
  Limitation: must know message length before starting (unlike GCM)
  Used in: 802.11i (WPA2 CCMP), 802.15.4, CoAP/DTLS for IoT

SIV (Synthetic IV / AES-SIV, RFC 5297):
  Nonce-misuse resistant: even if nonce repeated, only leaks message equality
  Not random but synthetic IV = PRF over message + AAD + nonce
  Security: IND-CPA even if nonce reused (only distinguishes same msg vs different)
  Use case: database field encryption where nonce management is error-prone
  Cost: 2 passes (slower than GCM); two keys required

XTS (XEX-based Tweaked CodeBook, IEEE 1619):
  Disk encryption: not AEAD; no authentication; sector-level tweak
  Tweakable block cipher: E(key, tweak, plaintext) where tweak = sector number
  Does not provide integrity (acceptable for disk encryption: hardware can't tamper)
  Used: dm-crypt/LUKS on Linux, FileVault on macOS, BitLocker on Windows
```

---

## 5. ChaCha20 and Poly1305

```
CHACHA20 (Bernstein 2008):
  ARX design: Add-Rotate-XOR only; no S-boxes → no lookup table → no timing side-channel
  State: 4×4 matrix of 32-bit words (512-bit state):
  ┌──────┬──────┬──────┬──────┐
  │ "exp"│ "and"│ "d s"│ "ixe"│  ← constants "expand 32-byte k"
  │ k0   │ k1   │ k2   │ k3   │  ← key (256-bit = 8 words)
  │ k4   │ k5   │ k6   │ k7   │  ← key continued
  │ ctr  │ n0   │ n1   │ n2   │  ← counter (32-bit) + nonce (96-bit)
  └──────┴──────┴──────┴──────┘

QUARTER ROUND (core operation):
  a += b; d ^= a; d <<<= 16;
  c += d; b ^= c; b <<<= 12;
  a += b; d ^= a; d <<<= 8;
  c += d; b ^= c; b <<<= 7;
  Applied to 4 words; 20 rounds = 10 double-rounds (column round + diagonal round)
  Mix function: 64 words after 80 quarter rounds; add initial state → 64-byte block

KEYSTREAM GENERATION:
  ChaCha20(key, nonce, counter): run 20-round mixing; add initial state; output 64 bytes
  C[i] = P[i] ⊕ ChaCha20(key, nonce, i)   (counter increments per 64-byte block)
  Seek: can generate block N without computing 0..N-1 (counter is part of state)

CHACHA20 vs AES-CTR:
  Performance without AES-NI: ChaCha20 ~3× faster (ARX vs S-box lookup)
  Performance with AES-NI: AES-GCM wins; single-cycle pipeline
  Side-channel: ChaCha20 constant-time by construction; AES table lookups vulnerable
  Usage: TLS 1.3 prefers ChaCha20 on platforms without AES-NI; RFC 8439

POLY1305 MAC (Bernstein 2005):
  One-time MAC: unique key per message (r, s) where r is clamped, s is pad
  Polynomial evaluation over GF(2¹³⁰-5):
    Divide message into 16-byte blocks; each block = n₁, n₂, ..., nₗ (with top bit set)
    MAC = (n₁r^ℓ + n₂r^{ℓ-1} + ... + nₗr) + s  mod (2¹³⁰-5)
  Security: universally hash family; MAC key is derived fresh per message (from ChaCha20 stream)
  "One-time" key (r, s) derived as: first 32 bytes of ChaCha20 keystream with counter=0
  Then message encrypted with ChaCha20 counter=1 onward
  Tag: last 16 bytes = Poly1305(one-time-key, ciphertext || AAD || lengths)
```

---

## 6. Cryptographic Hash Functions

```
REQUIREMENTS:
  Preimage resistance: given h, hard to find m with H(m) = h     [one-way]
  Second preimage resistance: given m, hard to find m' ≠ m with H(m')=H(m)
  Collision resistance: hard to find any (m, m') with H(m)=H(m')  [strongest]
  Random oracle (ideal): output indistinguishable from random for new inputs

SHA-2 FAMILY (FIPS 180-4):
  SHA-256: Merkle-Damgård (MD) construction; Davies-Meyer compression function
    Compression: f: {0,1}²⁵⁶ × {0,1}⁵¹² → {0,1}²⁵⁶
    Padding: message length appended (Merkle-Damgård strengthening)
    State: h₀..h₇ (8 × 32-bit words); initial values = square roots of primes
    Constants: 64 rounds using cube roots of primes

  Length Extension Attack on SHA-2:
    MD construction vulnerable: given H(m), can compute H(m || padding || m') without knowing m
    Affected: SHA-1, SHA-256, SHA-512 (all plain MD hash)
    Fix: use HMAC (nested construction prevents extension); or SHA-3 (sponge; not vulnerable)
    NEVER compute H(key || message) for MAC (vulnerable to extension); use HMAC

SHA-3 / KECCAK (FIPS 202):
  Sponge construction — fundamentally different from Merkle-Damgård:
    Rate r + capacity c = 1600 bits (state); f = Keccak-f[1600] permutation
    Absorb: XOR input chunks (rate-sized) into state, apply f
    Squeeze: output r bits of state; repeat if more output needed
  Not vulnerable to length extension (capacity c not accessible externally)
  SHA3-256: r=1088, c=512; SHA3-512: r=576, c=1024
  SHAKE128/256: extendable output functions (XOF); arbitrary output length

BLAKE3 (2020):
  Tree hashing: parallelizable over message chunks
  Based on: BLAKE2 compression function (ARX design from ChaCha)
  Single algorithm: hash, KDF, MAC, PRF (via keyed mode + context strings)
  Performance: ~2-5× faster than SHA-256 in software; SIMD-friendly
  Not yet a FIPS standard; widely used in practice (Cargo, Bao)

HASH COMPARISON:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Hash     │ Output │ Speed     │ Side-ch  │ Length ext │ Status   │
  ├────────────────────────────────────────────────────────────────────┤
  │  SHA-256  │ 256b   │ Medium    │ OK       │ Vulnerable │ FIPS std │
  │  SHA-512  │ 512b   │ Fast 64b  │ OK       │ Vulnerable │ FIPS std │
  │  SHA3-256 │ 256b   │ Slow SW   │ OK       │ Safe       │ FIPS std │
  │  SHA3-512 │ 512b   │ Slow SW   │ OK       │ Safe       │ FIPS std │
  │  BLAKE3   │ any    │ Fast++    │ OK       │ Safe       │ Non-FIPS │
  └────────────────────────────────────────────────────────────────────┘
```

---

## 7. MACs

```
HMAC (RFC 2104):
  HMAC_k(m) = H((k ⊕ opad) || H((k ⊕ ipad) || m))
  ipad = 0x36...36; opad = 0x5C...5C (64-byte XOR patterns)
  Inner hash: H(k_ipad || m); outer hash: H(k_opad || inner_hash)
  Security: if H is PRF → HMAC is PRF; resistant to length extension

  Why two nesting levels?
    HMAC-inner: binds key + message; produces PRF output even if H is MD construction
    HMAC-outer: provides additional separation between inner key and outer key
    Resist multi-collision attacks: inner hash can have collisions; outer layer prevents exploitation

CMAC (NIST SP 800-38B):
  CBC-MAC variant; CBC chain over message with key-derived subkeys at end
  Fixes plain CBC-MAC length extension: subkey derivation encodes message length
  Used in: AES-CMAC (RFC 4493); common in hardware tokens, TLS 1.0 HMAC alternative

HMAC vs CMAC vs Poly1305:
  HMAC: general purpose; any hash function; widely deployed
  CMAC: AES-hardware optimized; hardware tokens; FIPS-approved
  Poly1305: fastest in software; one-time key; used only as part of ChaCha20-Poly1305

MAC SECURITY — INT-PTXT AND INT-CTXT:
  INT-PTXT: no forgery of new valid (message, tag) pair
  INT-CTXT: no forgery of new valid ciphertext (even producing identical plaintext)
  INT-CTXT ⊃ INT-PTXT; AEAD provides INT-CTXT
```

---

## 8. Key Derivation Functions

```
HKDF — HMAC-BASED KDF (RFC 5869):
  Two-phase construction: Extract → Expand

  Extract: PRK = HMAC(salt, IKM)
    IKM = input key material (e.g., DH shared secret — NOT uniformly random)
    salt = random or zero (public); concentrates entropy into PRK
    PRK: pseudorandom key of HMAC output length (32 or 64 bytes)

  Expand: OKM = HMAC(PRK, info || counter)  (repeated for more output)
    info: context string (binds derived key to its purpose; prevents cross-protocol attacks)
    counter: 1, 2, 3, ... per 32/64-byte output block
    OKM: output keying material of desired length

  Use: TLS 1.3 key schedule (multiple HKDF-Extract + HKDF-Expand calls for each key)
  Why not just H(secret)? Hash is not a KDF: doesn't handle non-uniform IKM; no domain separation

PBKDF2 (RFC 8018):
  PBKDF2(password, salt, iterations, dkLen) = PRF output iterated `iterations` times
  Designed for slow key derivation from low-entropy passwords
  Weakness: parallelizable on GPU/ASIC (PBKDF2-SHA256 can run millions of iterations/sec on GPUs)
  Still used: FIPS-compliant (SP 800-132); Windows BitLocker; iOS < 10; legacy systems
  Minimum: 600,000 iterations for PBKDF2-SHA256 (OWASP 2023 recommendation)

BCRYPT:
  Blowfish-based; expensive key schedule + expensive block encryption rounds
  Parameter b (cost factor): 2^b iterations; b=12 → ~250ms on modern CPU
  Output fixed 60-char string with salt embedded
  Limitation: max 72 bytes of password input; bcrypt(sha256(password)) pattern for long passwords
  Not GPU-parallelizable as well as PBKDF2 (Blowfish key schedule is expensive per instance)

SCRYPT (RFC 7914):
  Memory-hard: requires large memory as well as computation
  Parameters: N (memory factor), r (block size), p (parallelism factor)
  N=2²⁰ (1M blocks), r=8, p=1 → 1 GB memory required
  Memory-hardness: makes GPU/FPGA attacks more expensive (memory expensive on hardware)
  Used: Litecoin, some SSH key files, some password managers

ARGON2ID (RFC 9106; PHC 2015 winner — current standard):
  Three variants: Argon2d (data-dependent; cache attacks), Argon2i (data-independent; better for passwords), Argon2id (hybrid; recommended for general use)
  Parameters: t (time iterations), m (memory KiB), p (parallelism)
  OWASP recommendation: t=2, m=65536 (64 MB), p=1 minimum; prefer t=3 m=65536
  NIST SP 800-63B: recommends memory-hard functions for password storage
  Why id: Argon2d is faster but vulnerable to timing side-channels; Argon2i is slower in first pass; id does both
  Security analysis: best known attacks require Ω(m × t) time; memory-hardness theoretically grounded
```

---

## 9. Side-Channel Attacks

```
TIMING ATTACKS ON AES:
  Table-lookup AES (pre-AES-NI):
    SubBytes + MixColumns often merged into 4 T-tables (1 KB each → 4 KB)
    T₀[a] = {a₀, a₀², ..., a₀·e₃} merged lookup; one table access per byte per round
    Cache side-channel: which cache line accessed → leaks plaintext or key material
    Bernstein 2005: timing attacks via remote network timing (DNS cache timing)
    Fix: AES-NI instructions (operate entirely in registers; no cache-based lookup)

  CONSTANT-TIME REQUIREMENT:
    All cryptographic operations must run in time independent of secret values
    Branches on secret bits: if (key_bit == 1) → timing leak
    Table lookups with secret indices: leaks accessed cache lines
    Multiplication timing: variable-time multiply with secret multiplier on some CPUs

  FLUSH+RELOAD / PRIME+PROBE:
    Shared memory cache attacks between processes (or VMs)
    Flush+Reload: flush cache line; victim accesses it; measure reload time
    Works across VMs in some cloud configurations
    Fix: process isolation; HyperThreading disabled for high-security contexts

POWER ANALYSIS (hardware):
  Simple Power Analysis (SPA): visual inspection of power trace → operation sequence
  Differential Power Analysis (DPA): statistical correlation of power with intermediate values
  Countermeasures: masking (XOR with random mask throughout computation), power flattening

FAULT INJECTION:
  Induce computational errors via voltage/clock glitching or EM pulses
  Differential Fault Analysis (DFA): compare correct vs faulty outputs → key recovery
  Protection: redundant computation + comparison; error detection codes

CONSTANT-TIME IMPLEMENTATION PATTERNS:
  Branchless selection: result = (cond * a) + ((1-cond) * b)  — no branch
  Lookup via CMOV: use conditional move (CMOV) instruction on x86
  OpenSSL constant_time_select, libsodium: standardized constant-time utilities
  Compiler danger: compiler may optimize out "useless" constant-time constructs → use barriers
```

```
CONSTANT-TIME COMPARISON — UNIVERSAL LIBRARY REFERENCE:

  The pattern: never use memcmp() or == for comparing MACs, tags, or secret-derived values.
  Variable-time comparison short-circuits on first mismatch → timing oracle → auth bypass.

  ┌────────────────────────────────────────────────────────────────────────────────────────┐
  │  Library / Language  │ Function                         │ Notes                        │
  ├────────────────────────────────────────────────────────────────────────────────────────┤
  │  libsodium           │ crypto_verify_16(a, b)           │ 16-byte constant-time compare │
  │                      │ crypto_verify_32(a, b)           │ 32-byte; returns 0 if equal  │
  │                      │ sodium_memcmp(a, b, n)           │ arbitrary length              │
  │  OpenSSL / BoringSSL │ CRYPTO_memcmp(a, b, n)           │ returns 0 if equal; any len   │
  │  Go                  │ subtle.ConstantTimeCompare(a, b) │ crypto/subtle; returns 1 if = │
  │  Rust (ring)         │ ring::constant_time::verify_slices_are_equal(a, b) │ returns Ok   │
  │  Java (JCA)          │ MessageDigest.isEqual(a, b)      │ Java 6+; constant-time        │
  │  Python (hmac)       │ hmac.compare_digest(a, b)        │ Python 3.3+; use this, not == │
  │  .NET                │ CryptographicOperations.FixedTimeEquals(a, b) │ .NET 5+ (System.Security.Cryptography) │
  └────────────────────────────────────────────────────────────────────────────────────────┘

  Compiler hazard: constant-time code can be optimized away — use memory barriers or
    platform intrinsics. libsodium/BoringSSL implementations handle this.
    In C: volatile + barrier; in Rust/Go: compiler-aware intrinsics.
  Rule: always compare MAC/tag output with constant-time compare; never short-circuit.
```

```
AEAD NONCE GENERATION AT SCALE — BIRTHDAY BOUND MATH:

  Random nonce collision probability (birthday paradox):
    n = messages encrypted under one key; nonce space = 2^96 (AES-GCM standard)
    Pr[collision] ≈ n² / (2 × 2^96)
    At n = 2^32 messages:  Pr ≈ 2^64 / 2^97 = 2^{-33}  (~1 in 8 billion) — acceptable
    At n = 2^48 messages:  Pr ≈ 2^96 / 2^97 = 0.5       — 50% collision rate; catastrophic
    NIST SP 800-38D limit: 2^32 random nonces per key (Pr of any collision < 2^{-32})

  Counter-based nonces (deterministic; no birthday bound):
    Nonce = 96-bit counter starting at 0; increment per message
    Safe: zero collision probability by construction; 2^96 messages before wrap
    Problem in distributed systems: multiple nodes must coordinate counters
    Failure mode: node restart resets counter → nonce reuse if state lost

  Counter + random hybrid (distributed services pattern):
    Nonce = [32-bit node ID || 64-bit counter per node]
    Node ID assigned at deploy time (or random at startup); counter in persistent state
    Result: each node has its own safe counter space; no cross-node coordination needed
    Used by: most cloud KMS implementations internally

  Random + epoch hybrid:
    Nonce = [32-bit unix_timestamp || 64-bit random]
    Guarantees temporal separation; reduces per-epoch collision probability to 2^{-32}
    Risk: timestamp clock skew; multiple messages per second in same epoch

  Recommendation by use case:
    Single service, low volume (< 2^28 msgs/key): random nonces; safe
    Single service, high volume: counter in persistent state (accept coordination cost)
    Distributed: node-ID + counter hybrid; OR rekey frequently (per 2^32 messages)
    Nonce-misuse risk: use AES-SIV (synthetic IV; deterministic; only leaks message equality on reuse)
```

---

## 10. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| AES mode for general encryption? | AES-256-GCM (AEAD); nonce random 96-bit; rekey after 2³² messages |
| Best mode without AES-NI? | ChaCha20-Poly1305 (RFC 8439); constant-time by design |
| Never use which mode? | ECB (pattern leakage); CBC without authentication (padding oracle) |
| Nonce reuse in GCM consequence? | Catastrophic: attacker recovers GHASH key H → can forge any ciphertext |
| Nonce-misuse resistant mode? | AES-SIV (RFC 5297); uses synthetic IV; 2-pass; deterministic |
| Password storage: which hash? | Argon2id (t=3, m=64MB, p=1); never plain SHA/MD5/bcrypt for new systems |
| Key derivation from DH secret? | HKDF (extract + expand); DH output is not uniformly random → needs extraction |
| Length extension attack affects? | SHA-1, SHA-256, SHA-512 (Merkle-Damgård); NOT SHA-3, HMAC, BLAKE3 |
| GF(2⁸) reduction polynomial? | x⁸ + x⁴ + x³ + x + 1 (AES irreducible polynomial; FIPS 197) |
| AES-NI provides what? | Hardware instructions for AES round functions; eliminates timing side-channel |
| When use PBKDF2 over Argon2id? | Only when FIPS compliance required; prefer Argon2id otherwise |
| sUF-CMA requirement? | Use Ed25519 or RSA-PSS; ECDSA is EUF-CMA but has malleability |
| AEAD = ? | AES-GCM provides: IND-CPA (CTR mode) + INT-CTXT (GHASH MAC) → IND-CCA2 |
| ChaCha20 key+nonce size? | 256-bit key + 96-bit nonce + 32-bit counter = 480 bits of block function input |

---

## Common Confusion Points

**AES-GCM nonce ≠ IV:** Nonce must be unique per (key, message); never repeat. AES-CBC IV must be unpredictable (random). These are different requirements. GCM nonce can be a counter (predictable) as long as it's unique; CBC IV must be random (attacker shouldn't be able to predict the next IV — BEAST attack exploited predictable IVs in TLS 1.0).

**GHASH is not a hash in the collision-resistant sense:** GHASH is a universal hash family used for authentication; it uses a secret key H = AES_k(0). It provides MAC security (unforgeability), not collision resistance. You can compute GHASH(H, m1) = GHASH(H, m2) for m1 ≠ m2 easily IF you know H — but H is secret in GCM. Nonce reuse leaks H, making GHASH trivially invertable.

**MixColumns operates on columns, ShiftRows on rows:** After SubBytes (byte substitution in place), ShiftRows rotates rows to scatter bytes to different columns. Then MixColumns mixes each column. Together, these provide diffusion: after 2 rounds, every output byte depends on every input byte. If MixColumns came before ShiftRows, diffusion would be only within columns.

**Poly1305 requires a fresh key per message:** Poly1305 is a one-time MAC — the (r, s) key pair must never be reused across messages. When used as ChaCha20-Poly1305, ChaCha20 derives a fresh Poly1305 key from the first 32 bytes of the keystream (counter=0) for each (key, nonce) pair. Since ChaCha20 nonces must be unique anyway, this is automatically satisfied.

**Argon2 parameters must match your threat model:** t=2, m=64MB is a starting point. High-value secrets (master passwords, HSM PINs) warrant t=3 or higher and larger memory. But don't reduce memory below 64 MB just because servers are "slow" — memory cost is the defense. The whole point of Argon2 is that GPUs can't parallelize across Argon2 instances as efficiently as PBKDF2.

**AES-256 is not twice as secure as AES-128:** Against classical attacks, AES-128 provides ~128-bit security and AES-256 provides ~256-bit security. Against quantum (Grover): AES-128 → ~64-bit, AES-256 → ~128-bit. The key schedule for AES-256 is slightly more complex (some minor known attack reductions exist on reduced-round AES-256 that don't apply to AES-128). Use AES-256 for future-proofing against quantum adversaries.
