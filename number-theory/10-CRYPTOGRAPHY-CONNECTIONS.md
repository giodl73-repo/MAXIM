# Number Theory in Cryptography

## The Big Picture

```
+====================================================================+
|       NUMBER THEORY → CRYPTOGRAPHIC HARDNESS                       |
+====================================================================+
|                                                                    |
|  PROBLEM        CRYPTO USE               HARD BECAUSE              |
|  +-----------+  +--------------------+  +---------------------+   |
|  |Factoring  |  |RSA: factor n=pq    |  |NFS: sub-exp, best   |   |
|  |IFP        |  |to break private key|  |classical alg.       |   |
|  +-----------+  +--------------------+  +---------------------+   |
|  +-----------+  +--------------------+  +---------------------+   |
|  |DLP        |  |Diffie-Hellman      |  |Index calculus:      |   |
|  |(Z/pZ)*    |  |DSKG key exchange   |  |sub-exp, worse bits  |   |
|  +-----------+  +--------------------+  +---------------------+   |
|  +-----------+  +--------------------+  +---------------------+   |
|  |ECDLP      |  |ECDH, ECDSA, EdDSA  |  |Generic attacks only:|   |
|  |E(F_p)     |  |                    |  |O(√p) — no sub-exp   |   |
|  +-----------+  +--------------------+  +---------------------+   |
|  +-----------+  +--------------------+  +---------------------+   |
|  |SVP/CVP    |  |NTRU, Kyber, Falcon |  |NP-hard worst-case;  |   |
|  |lattices   |  |POST-QUANTUM        |  |no quantum speedup   |   |
|  +-----------+  +--------------------+  +---------------------+   |
|                                                                    |
|  ALL of the first three: BROKEN by Shor's quantum algorithm       |
|  SVP/CVP: no known quantum speedup → post-quantum                  |
+====================================================================+
```

<!-- @editor[content/P2]: Cross-reference uses a hardcoded absolute Windows path (`C:\src\reference\cryptography\`). Reference library cross-links should use a relative path or a consistent format that works across environments (e.g., `../cryptography/`). Absolute system paths will break in any non-Windows deployment or if the repo is moved. -->

Cross-reference: `C:\src\reference\cryptography\` covers crypto implementation.
This file covers the number-theoretic foundations and hardness reductions.

---

## RSA — The Full Picture

### Setup and Correctness

```
KEY GENERATION:
  1. Choose distinct primes p, q (each ~1024 bits for RSA-2048)
  2. n = p·q  (the modulus)
  3. φ(n) = (p-1)(q-1)  [or λ(n) = lcm(p-1,q-1)]
  4. Choose e: gcd(e, φ(n)) = 1; typically e = 65537 = 2^{16}+1
  5. Compute d: e·d ≡ 1 (mod φ(n))  [Extended Euclidean]
  Public key: (n, e)    Private key: (n, d)  [or (p, q, d)]

ENCRYPTION:  c = m^e mod n   (m ∈ Z/nZ, m < n)
DECRYPTION:  m = c^d mod n

CORRECTNESS:
  c^d = (m^e)^d = m^{ed} = m^{1+kφ(n)} = m · (m^{φ(n)})^k ≡ m · 1^k = m (mod n)
  [Euler's theorem: m^{φ(n)} ≡ 1 (mod n) when gcd(m,n)=1]
  When gcd(m,n)>1: use CRT argument — still works.
```

### Security Reductions

```
BREAKING RSA (standard assumption):
  Given (n, e, c), find m such that m^e ≡ c (mod n).
  "RSA problem" (RSAP).

RELATIONSHIPS:
  FACTOR(n) → RSAP: if you can factor n=pq, compute φ(n)=(p-1)(q-1),
    then d = e^{-1} mod φ(n), then m = c^d mod n.
  RSAP → FACTOR(n): NOT KNOWN. No reduction proves this.
    RSAP might be easier than factoring. (Believed equivalent, not proved.)

INTEGER FACTORING PROBLEM (IFP):
  Given n = pq, find p (and q).
  Best known: NFS — L_n[1/3, 1.923] ≈ exp(1.923 · (ln n)^{1/3}(ln ln n)^{2/3})
  Status: not in P, not NP-complete, not known quantum-efficient on classical.
  Shor's: O(log³ n) on quantum computer.

PRACTICAL RSA REQUIREMENTS:
  - n = pq, both primes large (~1024 bits each for RSA-2048)
  - p ≠ q (obviously), |p-q| large (prevent Fermat factoring)
  - p-1, q-1 must each have a large prime factor (prevent Pollard p-1)
  - p ≢ 1 (mod small e) and q ≢ 1 (mod small e) (prevent small exponent attack)
  - Use OAEP padding (RSA-OAEP) — textbook RSA is deterministic and insecure
    without padding; same message always gives same ciphertext → chosen-plaintext
    distinguishability attack
```

### Attacks on Specific Parameters

```
SMALL d (private exponent):
  Wiener's attack (1990): if d < n^{1/4}/3, the private exponent is recoverable
  from continued fraction expansion of e/n.
  FIX: don't use small d. Use e = 65537 (small e is fine; small d is not).

SMALL e without padding:
  If e=3 and m < n^{1/3}: m^3 < n, so c = m^3 (exact integer), take cube root.
  FIX: use proper padding (OAEP). Or ensure e=65537.

COMMON MODULUS ATTACK:
  If two parties share modulus n but different (e₁,d₁), (e₂,d₂) and the same m
  is encrypted as both c₁=m^{e₁} and c₂=m^{e₂}:
  If gcd(e₁,e₂)=1: Bezout gives ae₁+be₂=1, so m = c₁^a·c₂^b mod n.
  FIX: Never reuse RSA moduli; always generate fresh key pairs.

TIMING ATTACKS (Kocher 1996):
  Square-and-multiply leaks timing information about bits of d.
  FIX: constant-time implementations, Montgomery multiplication, blinding.
  r = random; compute (rm)^d mod n, then divide by r^d.
```

---

## Diffie-Hellman

### Classic DH (1976)

```
SHARED PARAMETERS: prime p (2048+ bits), generator g (primitive root mod p)

KEY EXCHANGE:
  Alice: choose secret a; send A = g^a mod p
  Bob:   choose secret b; send B = g^b mod p
  Alice: compute B^a = g^{ab} mod p
  Bob:   compute A^b = g^{ab} mod p
  Shared secret: g^{ab} mod p

SECURITY:
  Computational DH problem (CDH): given g, g^a, g^b, find g^{ab}.
  Decisional DH problem (DDH): given g, g^a, g^b, distinguish g^{ab} from random.
  CDH is at least as hard as DLP.
  DDH is at least as hard as CDH.
  CDH → DLP: not known (CDH might be easier).

DLP in (Z/pZ)*:
  Best attack: Number Field Sieve, L_p[1/3, ...] — sub-exponential.
  At p=2048 bits: comparable security to RSA-2048.

PARAMETER CHOICE:
  p should be a "safe prime": p = 2q+1 with q prime.
    → (Z/pZ)* has prime-order subgroup of order q (prevents Pohlig-Hellman).
  Use subgroup of prime order q (not the full (Z/pZ)*).
  g should generate the q-order subgroup.
  DH in this subgroup: DLP takes sub-exp time on q, not p.
```

### ElGamal Encryption

```
Based on DH. Public key: (p, g, g^a) where a is secret.

Encryption of m:
  Choose random k.
  c₁ = g^k mod p
  c₂ = m · (g^a)^k mod p  [= m · shared_secret]

Decryption:
  m = c₂ / c₁^a = m · g^{ak} / g^{ak} = m

Security: IND-CPA under DDH assumption.
Note: Randomized encryption (k is random) → same message gives different ciphertext.
Contrast with textbook RSA: deterministic.
```

---

## Elliptic Curve Cryptography

### Elliptic Curves over Finite Fields

```
E over F_p: y² = x³ + ax + b (mod p), discriminant 4a³+27b² ≢ 0 (mod p).

E(F_p): points (x,y) satisfying the equation, plus the "point at infinity" O.

GROUP LAW (chord-tangent):
  P + Q: draw line through P and Q (or tangent if P=Q).
  It hits E at a third point R. Then P+Q = -R (reflect over x-axis).
  O is the identity.
  -P: reflection of P.

HASSE'S THEOREM: |#E(F_p) - (p+1)| ≤ 2√p
  The curve has between p+1-2√p and p+1+2√p points.

ELLIPTIC CURVE DLP (ECDLP):
  Given curve E/F_p, point P of prime order n, and Q = kP, find k.

ECDLP ATTACKS:
  Baby-step giant-step: O(√n) time and space.
  Pohlig-Hellman: fast if n is smooth (→ choose n prime).
  Index calculus: Does NOT apply to general elliptic curves.
    (No efficient factorization analogues in E(F_p).)

CONSEQUENCE: Need only ~256-bit curves for 128-bit security.
  vs. ~3072-bit modulus for DH/RSA at same security level.
  Smaller keys → faster operations → preferred for modern systems.
```

### Standard Curves

```
P-256 (NIST secp256r1):
  y² = x³ - 3x + b over F_p (256-bit prime p)
  Widely used: TLS 1.3, ECDSA in certificates, JWT signing.

secp256k1:
  y² = x³ + 7 over F_p (Koblitz curve, no random b)
  Used by Bitcoin and Ethereum.
  Slightly faster than P-256 for specific implementations.

Curve25519 (Bernstein 2006):
  Montgomery form: y² = x³ + 486662x² + x over F_p, p = 2^{255}-19
  Designed for constant-time implementation; no known weaknesses.
  x25519: ECDH using Curve25519. Used in TLS 1.3, Signal, WireGuard.

Ed25519:
  Edwards form: -x²+y² = 1 + dx²y² over F_p (isomorphic to Curve25519)
  EdDSA signature scheme. Faster, simpler constant-time implementation.
  Used in: OpenSSH, DNSSEC, Signal.

MALICIOUS CURVES:
  Some NIST curves have seeds that are opaque ("nothing up my sleeve"
  but unexplained). Dual_EC_DRBG was a backdoored PRNG using EC points.
  Curve25519 and Ed25519 are designed with transparent parameters.
```

---

## Lattice Cryptography — Post-Quantum

### The Geometric Setup

```
LATTICE: A discrete subgroup L of R^n of the form
  L = {a₁v₁ + a₂v₂ + ... + aₙvₙ : aᵢ ∈ Z}
  where v₁,...,vₙ are linearly independent vectors (the lattice basis).

HARD LATTICE PROBLEMS:
  SVP (Shortest Vector Problem):
    Find the shortest nonzero vector in L.
    |best classical: LLL approximation; exact: NP-hard in worst case|
    |No known quantum speedup for exact or good approximation|

  CVP (Closest Vector Problem):
    Given a target t ∈ R^n, find the closest lattice point.
    NP-hard. Used in decryption for lattice cryptosystems.

  LWE (Learning With Errors — Regev 2005):
    Distinguish: (a, b = ⟨a,s⟩ + e mod q) from (a, uniform b)
    where s is a secret vector, e is a small error vector.
    Reduction: LWE is at least as hard as worst-case lattice problems.
    This worst-case to average-case reduction is unique to lattices.
```

### LWE and Ring-LWE

```
LWE: vectors in Z_q^n.
Ring-LWE (Lyubashevsky-Peikert-Regev 2010): elements of Z_q[x]/(x^n+1).

Ring-LWE sample: (a(x), b(x) = a(x)·s(x) + e(x)) in Z_q[x]/(f(x))

WHY RING IS BETTER:
  LWE: key size O(n²) — large.
  Ring-LWE: key size O(n) — compact.
  Ring-LWE inherits security from structured lattice problems (SVP on ideal lattices).

CRYSTALS-KYBER (NIST PQC Standard 2022, now ML-KEM / FIPS 203):
  Key encapsulation mechanism based on Module-LWE.
  Module = LWE over a small number of Ring-LWE instances.
  Security: Module-LWE hardness → ideal lattice SVP.
  Key sizes: ~800-1568 bytes (vs RSA-2048: 256 bytes).
  Fast: uses NTT (Number Theoretic Transform) for polynomial multiplication.
```

### NTRU

```
NTRU (Hoffstein-Pipher-Silverman 1998):
  Ring: Z_q[x]/(x^N - 1).
  Private key: f(x), g(x) short polynomials.
  Public key: h(x) = g(x) · f(x)^{-1} mod q.

Encryption of m:
  c(x) = r(x)·h(x) + m(x) mod q  (r random, small)

Decryption:
  f(x)·c(x) = f(x)·r(x)·h(x) + f(x)·m(x)
             = r(x)·g(x) + f(x)·m(x) mod q
  (Both terms are "small" → can recover m by reducing mod p < q.)

Security: Reduces to finding shortest vector in a 2D block-circulant lattice.
NTRU Prime / NTRU (NIST Alt): Finalists in NIST PQC competition.

Connection to algebraic number theory:
  Z[x]/(x^N-1) is the ring of integers of a cyclotomic field (when N is prime).
  Class number of this field affects the security of NTRU variants.
```

### Comparison: Classical vs Post-Quantum

```
+-------------------------------------------------------------------+
| SCHEME       | HARD PROBLEM     | QUANTUM  | KEY SIZE | SPEED     |
+-------------------------------------------------------------------+
| RSA-2048     | Factoring IFP    | BROKEN   | 256 B    | Medium    |
| DH-2048      | DLP (Z/pZ)*      | BROKEN   | 256 B    | Medium    |
| ECDH P-256   | ECDLP            | BROKEN   | 32 B     | Fast      |
| Kyber-768    | Module-LWE       | SAFE     | ~1.2 KB  | Fast(NTT) |
| Dilithium-3  | Module-LWE/SIS   | SAFE     | ~2.7 KB  | Fast(NTT) |
| FALCON-512   | NTRU, SIS on HD  | SAFE     | ~1.3 KB  | Fast      |
| SPHINCS+     | Hash function    | SAFE     | ~8-50 KB | Slower    |
+-------------------------------------------------------------------+

"BROKEN" by Shor means: quantum computer with ~4000 logical qubits.
Current quantum computers (2024): ~1000 physical qubits, not fault-tolerant.
```

---

## Discrete Log Problem Variants

```
GAP-DLP: distinguish (g, g^a, g^b, g^c) from (g, g^a, g^b, random).
DDH (Decisional DH): distinguish g^{ab} from random given g, g^a, g^b.

DDH is FALSE in (Z/pZ)*:
  Given g, g^a, g^b, g^c, check if c ≡ ab (mod p-1):
  Use Legendre symbol: (g/p) is known, (g^a/p) = (g/p)^a.
  If (g^a/p)·(g^b/p) = (g^c/p): c might be ab.
  → DDH in (Z/pZ)* is easy when p-1 = 2q (quadratic residue check).
  FIX: Use a prime-order subgroup of (Z/pZ)* (order q, prime).
       In the q-order subgroup, DDH is believed hard.

DDH is believed TRUE in elliptic curve groups (no subgroup structure exploit).
This is why EC-based ElGamal/ECDH is semantically secure.
```

---

## Number Theory in Symmetric Cryptography

```
AES FINITE FIELD:
  S-box = inversion in GF(2^8) = GF(2)[x]/(x^8+x^4+x^3+x+1)
  MixColumns = multiplication in GF(2^8)^4 as a module over GF(2^8)[x]/(x^4+1)

CRC CHECKSUMS:
  CRC-32: remainder of polynomial division by 0x04C11DB7 over GF(2).
  Used in Ethernet, ZIP, PNG, ZLib — billions of CRC checks per second.
  Detects: all single-bit errors, all 2-bit errors, all odd # bit errors,
           all burst errors of length ≤ 32 bits.

REED-SOLOMON CODES:
  Over GF(2^8) or GF(2^m).
  Message = polynomial f(x) of degree < k.
  Codeword = (f(α⁰), f(α¹), ..., f(α^{n-1})) where α is a primitive element.
  Can correct up to (n-k)/2 symbol errors.
  Used in: CDs (2 RS codes), DVDs, QR codes, RAID-6 (XOR + RS), .NET storage,
           deep space communications (Voyager, Cassini).

HASH FUNCTIONS:
  SHA-256 uses: modular addition mod 2^32, bitwise ops — not subtle NT.
  Multiplicative hashing: h(k) = ⌊m·(kA mod 1)⌋ where A is irrational.
  MurmurHash, xxHash: fast, avalanche properties from number-theoretic mixing.
```

---

## Decision Cheat Sheet

| Cryptographic context | Number theory needed |
|-----------------------|---------------------|
| RSA security | IFP hardness, Euler φ(n), modular inverse |
| RSA correctness | Euler's theorem, CRT for speedup |
| RSA padding (OAEP) | Not NT — hash + XOR mask |
| DH security | DLP in (Z/pZ)*, safe prime parameters |
| ECDH/ECDSA security | ECDLP in E(F_p), Hasse's theorem, prime group order |
| Post-quantum KEM | LWE/Ring-LWE ← SVP/CVP hardness |
| Post-quantum signatures | SIS (Short Integer Solution) ← LWE variant |
| Error-correcting codes | Polynomial arithmetic over GF(2^m) |
| AES internals | GF(2^8) arithmetic, irreducible polynomials |
| Quantum attack | Shor: period-finding ← breaks IFP and DLP |

---

## Common Confusion Points

**"Breaking RSA = solving the integer factoring problem."**
Not exactly. Breaking RSA (recovering m from c,e,n) is the RSA problem (RSAP).
RSAP is no harder than IFP (factoring gives d). But RSAP → IFP is not proved.
In practice: modern RSA with proper parameters (OAEP, large keys) is believed
secure against all known classical attacks.

**"Elliptic curves are harder than RSA."**
Per bit of key, ECC gives better security. RSA-3072 ≈ ECC-256 in security level.
But ECC is NOT harder than RSA in an absolute sense — they're based on different
problems (ECDLP vs IFP) with no known reduction either way.

**"Lattice crypto is secure because no one has attacked it."**
Lattice crypto has provable security: reduction to worst-case lattice problems
(SVP/CVP), which are NP-hard in worst case. This is a MUCH stronger guarantee
than RSA or ECC (which have no such worst-case-to-average-case reduction).
The caveat: actual parameter choices require specific lattice problem hardness
(not just NP-hardness of a general version).

**"Post-quantum means safe from all quantum attacks."**
Post-quantum algorithms resist known quantum attacks (Shor, Grover). Grover's
algorithm gives a quadratic speedup for symmetric and hash algorithms — fixed
by doubling key/output sizes. For lattice-based: no significant quantum speedup
is known. But "no known quantum speedup" ≠ "no quantum speedup exists."
