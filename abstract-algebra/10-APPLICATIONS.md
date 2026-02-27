# Applications of Abstract Algebra

## The Big Picture

```
+====================================================================+
|           ABSTRACT ALGEBRA IN THE WORLD                            |
+====================================================================+
|                                                                    |
|  ERROR-CORRECTING CODES                                           |
|  Linear codes = subspaces of F_q^n                                |
|  Cyclic codes = ideals in F_q[x]/(x^n-1)                          |
|  Reed-Solomon = polynomial evaluation codes over F_q              |
|  Used in: CDs, DVDs, RAID-6, QR codes, deep space comm.           |
|                                                                    |
|  CRYSTALLOGRAPHY                                                   |
|  17 plane groups (wallpaper), 230 space groups                    |
|  Determine all possible crystal structures in 3D                  |
|  Used in: X-ray crystallography, drug design, materials science   |
|                                                                    |
|  PUBLIC-KEY CRYPTOGRAPHY                                          |
|  Group theory: DH in (Z/pZ)*, ECDH in E(F_p)                     |
|  Ring theory: RSA in Z/nZ, NTRU in Z[x]/(x^n-1)                  |
|  Module theory: LWE over R_q = Z_q[x]/(x^n+1)                    |
|                                                                    |
|  PHYSICS                                                          |
|  Symmetry groups: SO(3) rotations, SU(2) spin, SU(3) quarks      |
|  Noether's theorem: continuous symmetry → conservation law        |
|  Classification of particles: irreps of Poincaré group           |
+====================================================================+
```

---

## Error-Correcting Codes

### Why Algebra?

```
A code C ⊆ F_q^n encodes k-symbol messages as n-symbol codewords.
RATE = k/n (fraction of useful information).
MINIMUM DISTANCE d = min{wt(c₁-c₂) : c₁,c₂ ∈ C, c₁≠c₂}.
  where wt = Hamming weight (number of nonzero entries).

SINGLETON BOUND: d ≤ n - k + 1.
CODES ACHIEVING SINGLETON BOUND: MDS (Maximum Distance Separable) codes.
  Reed-Solomon = MDS codes over large alphabets.

CAPABILITIES:
  Detect up to d-1 errors.
  Correct up to ⌊(d-1)/2⌋ errors.
```

### Linear Codes

```
LINEAR CODE: C is a k-dimensional subspace of F_q^n.
  Specified by generator matrix G (k×n): rows span C.
  Or parity-check matrix H (r×n, r=n-k): C = ker(H).

ENCODING: message m ∈ F_q^k ↦ codeword mG ∈ F_q^n.
SYNDROME: for received word y, syndrome = Hy.
  If Hy = 0: no detectable error (or undetectable error).
  Hy = He where e is the error pattern → error correction via lookup table.

MINIMUM DISTANCE of linear code = minimum Hamming weight of nonzero codeword.
  (Since C is a subspace: min dist = min nonzero wt.)

IMPORTANT LINEAR CODES:
  Hamming codes: [n, n-r, 3] for n=2^r-1. Perfect 1-error-correcting.
  Reed-Muller codes: [2^m, C(m,r), 2^{m-r}]. Used in early space probes.
  Golay codes: [23,12,7] and [24,12,8]. Perfect 3-error-correcting.
    Used in Voyager 1/2 deep space communication.
  BCH codes: cyclic codes with designed minimum distance. Used in flash storage.
  LDPC codes: near Shannon-capacity on Gaussian channel. Used in 5G, Wi-Fi 6.
```

### Reed-Solomon Codes

```
CONSTRUCTION: Fix n ≤ q, evaluation points α₁,...,αₙ ∈ F_q (distinct).

  RS(n,k) = {(f(α₁),...,f(αₙ)) : f ∈ F_q[x], deg(f) < k}

  Message = polynomial f of degree < k.
  Codeword = evaluations of f at n points.
  Rate = k/n.
  Minimum distance = n - k + 1.  ← Achieves Singleton bound! MDS code.

WHY: If f,g are distinct (deg < k), f-g has at most k-1 roots, so they agree
  on at most k-1 points → differ on at least n-(k-1) = n-k+1 points.

ERROR CORRECTION: Can correct up to ⌊(n-k)/2⌋ erasures/errors.
  Berlekamp-Welch algorithm: O(n³) decoding.
  Guruswami-Sudan: list decoding beyond n-k+1 bound.

APPLICATIONS:
  CD: two interleaved RS codes over GF(2^8).
    Outer: RS(28,24) — corrects 2 errors per 28-byte block.
    Inner: RS(32,28) — corrects 2 errors.
    Together: corrects 4000 consecutive error bytes (a 2.5mm scratch).
  DVD: similar but larger Reed-Solomon codes.
  QR codes: RS over GF(2^8), error correction levels L/M/Q/H (7%/15%/25%/30% of data).
  RAID-6: XOR (RAID-5) + second RS codeword over GF(2^8). Survives 2 disk failures.
  Cloud storage (Google, Azure): erasure coding = systematic RS or LRC codes.
    Azure: LRC (locally recoverable codes) — proprietary variant.
  Deep space: Cassini, Voyager — concatenated RS + convolutional codes.
```

### Cyclic Codes

```
CYCLIC CODE: C ⊆ F_q^n closed under cyclic shift.
  (c₀,c₁,...,c_{n-1}) ∈ C → (c_{n-1},c₀,...,c_{n-2}) ∈ C.

ALGEBRAIC STRUCTURE:
  Identify codewords with polynomials in F_q[x]/(x^n-1).
  Cyclic shift = multiplication by x.
  Cyclic code = ideal in F_q[x]/(x^n-1).
  (An ideal I is closed under multiplication by x — cyclic shift.)

GENERATOR POLYNOMIAL: Every cyclic code has a unique monic generator g(x)
  with g | (x^n-1) and C = (g) = ideal generated by g.

BCH CODES (Bose-Chaudhuri-Hocquenghem):
  Choose g(x) such that d consecutive powers of a primitive element are roots.
  Designed minimum distance ≥ d.
  Used in: flash memory (NAND), QR codes, hard drives.

GOPPA CODES:
  More general algebraic construction. Includes binary Goppa codes.
  Used in McEliece cryptosystem (post-quantum).
```

---

## Crystallography

```
CRYSTAL SYMMETRY GROUP = set of all rigid motions (rotations, reflections,
  translations, glide reflections, screw axes) that map a crystal to itself.

CLASSIFICATION:
  2D: 17 WALLPAPER GROUPS (plane crystallographic groups).
    Classified in 1891 by Fedorov and Schönflies.
    Types: 5 Bravais lattices + point symmetries.

  3D: 230 SPACE GROUPS.
    Classified 1891-1894.
    32 point groups + 14 Bravais lattices + screw axes + glide reflections.

POINT GROUP: the rotational/reflection symmetry of a crystal.
  In 3D: 32 crystallographic point groups.
  Subgroups of O(3) compatible with periodicity.
  RESTRICTION: only 1-fold, 2-fold, 3-fold, 4-fold, 6-fold rotations allowed
    (not 5-fold, 7-fold, etc.) — why? The unit cell must tile space.
  Proof: rotation by 2π/n. For lattice compatibility: 2 cos(2π/n) must be integer.
    Only n ∈ {1,2,3,4,6} give integer. ← No 5-fold or 7-fold!

QUASICRYSTALS:
  5-fold symmetry observed by Shechtman (1984). Nobel Prize 2011.
  NOT a periodic crystal; uses Penrose tiling (quasiperiodic).
  Diffraction pattern: icosahedral symmetry (5-fold). Not a space group.

X-RAY CRYSTALLOGRAPHY:
  Crystal structure determined by Fourier analysis of diffraction pattern.
  F(h) = Σ_j f_j exp(2πi h·r_j) (structure factor = Fourier transform of atom positions).
  Space group determines which F(h) must vanish (systematic absences).
  This allows determination of crystal structure from diffraction data.
  Application: protein structure determination (key for drug design).
    COVID spike protein structure: X-ray crystallography guided vaccine design.
```

---

## Algebraic Cryptography

```
DISCRETE LOGARITHM GROUP (Z/pZ)*:
  Group: cyclic of order p-1.
  DH key exchange: g^a, g^b → g^{ab} (DLP hardness).
  ElGamal: g^k, m·(g^a)^k → m·g^{ak} (IND-CPA under DDH).
  DSA: Sign with modular arithmetic, verify with modular exponentiation.

ELLIPTIC CURVE GROUPS E(F_p):
  Group law: chord-tangent construction.
  ECDH: scalar multiplication. ECDLP hardness.
  ECDSA, EdDSA: signature schemes.
  Faster per bit than (Z/pZ)*: 256-bit ECC ≈ 3072-bit DH.

RING LEARNING WITH ERRORS (Ring-LWE):
  Ring R = Z_q[x]/(x^n+1) where n = power of 2.
  LWE sample: (a, a·s + e) where s ∈ R (secret), e ∈ R (small error).
  Hardness: worst-case ideal lattice SVP.
  Kyber (ML-KEM): public-key encryption/KEM from Module-LWE.
    Module: small number of Ring-LWE instances → compact keys.

NTRU:
  Ring: R = Z_q[x]/(x^n-1) (for cyclic structure) or Z_q[x]/(x^n+1) (NTRU Prime).
  Key: h = g/f (in R, invertible f and short g).
  Encryption: c = r·h + m (r random, small).
  Decryption: f·c = f·r·h + f·m = r·g + f·m → recover m.
  Hardness: finding short vector in a specific lattice (NTRU lattice).

SUPERSINGULAR ISOGENY-BASED (SIKE):
  Use isogenies between supersingular elliptic curves over F_{p²}.
  Broken in 2022 by Castryck-Decru using unexpected algebraic geometry.
  Teaches: even "hard-looking" problems can fall; new math can break crypto.

<!-- @editor[content/P2]: Pairing-based cryptography is absent — the learner calibration explicitly flags "applications to cryptography (pairing-based)" as a DOES NEED. Weil and Tate pairings on elliptic curves enable: BLS aggregate signatures (used in Ethereum 2.0 consensus), identity-based encryption (Boneh-Franklin), and the core of zk-SNARK constructions (Groth16, PLONK use bilinear pairing groups). The algebraic structure — the pairing e: E[r] × E[r] → μ_r is a Galois-equivariant bilinear map between groups of r-torsion points — is exactly where Galois theory, elliptic curves, and cryptography converge. This section has DH/ECDH/LWE but not pairings, which is a significant gap for the stated audience -->
```

---

## Algebraic Geometry Connections

```
VARIETIES AND RINGS:
  Hilbert's Nullstellensatz: bijection between:
    Radical ideals I ⊆ k[x₁,...,xₙ] ↔ Algebraic varieties V(I) ⊆ kⁿ.
    Prime ideals ↔ Irreducible varieties.
    Maximal ideals ↔ Points.
  The algebra of functions on a variety = coordinate ring.

SCHEME THEORY (Grothendieck 1960s):
  Replace "variety" by "spectrum of a ring" = Spec(R).
  Points of Spec(R) = prime ideals of R.
  Topology: Zariski topology (closed sets = V(I)).
  Structure sheaf: rings of functions.
  Elliptic curves as schemes: E over Z → good reduction for most primes p.
  Weil conjectures (proved by Deligne): Betti numbers of varieties over F_q
    from étale cohomology = "algebraic topology over finite fields."

RIEMANN-ROCH THEOREM:
  For a curve C over F_q and divisor D:
    l(D) - l(K-D) = deg(D) + 1 - g  [g = genus]
  Used in: algebraic geometry codes (Goppa codes), estimates on number of points.

APPLICATIONS TO CODING THEORY:
  Algebraic geometry codes (Tsfasman-Vladut-Zink 1982):
    Beat the Gilbert-Varshamov bound using curves of genus g:
    C = CL(D, G) from divisors D, G on a curve.
    Rate + distance ≥ 1 - 1/√q (exceeds GV bound for q ≥ 49).
```

---

<!-- @editor[content/P2]: Quantum error correction is referenced in the summary table ("GF(4) / stabilizer codes — AA-10") but has no section in this file — the reference points to itself and delivers nothing. Stabilizer codes over GF(4) (Calderbank-Rains-Shor-Sloane formalism), the CSS construction (Calderbank-Shor-Steane), and the connection to classical linear codes over GF(2) and GF(4) are the algebraic core of quantum error correction and deserve their own subsection here -->

## Quantum Groups and Quantum Algebra

```
QUANTUM GROUPS: q-deformations of classical Lie groups/algebras.
  Replace standard algebraic relations by q-deformed versions.
  As q → 1: recover classical structure.

QUANTUM ENVELOPING ALGEBRA U_q(sl₂):
  Standard sl₂: [E,F]=H, [H,E]=2E, [H,F]=-2F.
  Quantum version: E·F - F·E = (q^H - q^{-H})/(q-q^{-1}).
  (As q→1: → standard commutator [E,F]=H.)

APPLICATIONS:
  Knot theory: quantum groups → polynomial invariants of knots (Jones polynomial).
  Jones polynomial V_K(t): from representation of braid group using Hecke algebra,
    which is a q-deformation of the group algebra C[S_n].
    Distinguishes knots that Alexander polynomial cannot.

  Quantum computing:
    Topological quantum computation: anyons in quantum Hall effect.
    Fibonacci anyons: non-Abelian anyons; braiding = quantum gate.
    Mathematical framework: modular tensor categories (quantum group representations).

  Quantum integrability:
    Yang-Baxter equation R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂ in V⊗V⊗V.
    Solutions from quantum groups → exactly solvable models.
```

---

## Summary: Algebra in Modern Computing

```
+--------------------------------------------------------------------+
| COMPUTING USE CASE      | ALGEBRAIC STRUCTURE        | FILE REF.   |
+--------------------------------------------------------------------+
| RSA encryption           | Z/nZ, Euler φ(n)           | NT-10       |
| DH key exchange          | (Z/pZ)*, primitive root    | NT-03       |
| Elliptic curve crypto    | E(F_p) group law           | NT-10       |
| Post-quantum (Kyber)     | Z_q[x]/(x^n+1) module-LWE | NT-06,AA-08 |
| AES byte operations      | GF(2^8) = F_2[x]/(irred.) | AA-05       |
| CRC checksums            | F_2[x] polynomial division | AA-04       |
| Reed-Solomon (RAID,QR)   | F_q[x] eval codes          | AA-10       |
| FFT/NTT                  | Roots of unity in Z/pZ     | NT-03       |
| Hash-to-curve (ECDSA)    | Quadratic residues mod p   | NT-04       |
| Molecular vibration modes| Representation theory      | AA-07       |
| Crystallography          | 230 space groups           | AA-10       |
| Haskell monads           | Monads in endofunctor cat. | AA-09       |
| Type theory              | Cartesian closed categories| AA-09       |
| Persistent homology      | Chain complexes, homology  | Top-07      |
| Quantum error correction | GF(4) / stabilizer codes   | AA-10       |
+--------------------------------------------------------------------+
```

---

## Decision Cheat Sheet

| Need reliability under errors? | Use Reed-Solomon or BCH codes (polynomial rings over F_q) |
|--------------------------------|----------------------------------------------------------|
| Need crystal structure? | Apply space group classification (230 groups) |
| Need efficient key exchange? | ECC (elliptic curve groups) |
| Need post-quantum security? | Ring-LWE (modules over Z_q[x]/(x^n+1)) |
| Need to protect data in storage? | RAID-6 (Reed-Solomon), or erasure codes |
| Need quantum gates? | Topological QC (quantum group representations) |
| Need to classify crystal? | X-ray diffraction + space group determination |

<!-- @editor[content/P2]: Decision Cheat Sheet table uses inconsistent formatting — first column has no header label, and the rows mix "Need X?" format with "Need to X?" format. Also absent from the cheat sheet: pairing-based crypto (BLS/SNARKs), quantum error correction (stabilizer codes over GF(4)), and algebraic geometry codes (Goppa/AG codes that beat the GV bound). The summary table above is excellent; the cheat sheet should match its scope -->

---

## Common Confusion Points

**"Reed-Solomon is just parity bits."**
RS is vastly more powerful than parity. A parity bit detects 1 error. RS over GF(2^8)
with n=32, k=24 corrects 4 symbol errors — up to 4 corrupt bytes. The code lives
in a polynomial ring over a finite field. The decoding algorithm (Berlekamp-Massey
or Euclidean algorithm in F_q[x]) recovers the original polynomial from n-2t
evaluations when t errors occurred.

**"Elliptic curves for crypto are the same as elliptic curves in number theory."**
The same mathematical objects, different parameters. In number theory: curves over Q,
rational points, BSD conjecture. In crypto: curves over F_p with p a 256-bit prime,
the group E(F_p) has order ≈ p, and we solve the ECDLP. The group law is identical;
the field is different.

**"Quantum groups are related to quantum mechanics."**
They're related through physics (quantum integrability, quantum Hall effect), but
quantum groups are a purely mathematical algebraic structure — q-deformations of
classical Lie algebras/groups. The parameter q is complex, not Planck's constant.
The connection to physics is through representation theory of these structures,
appearing in condensed matter physics as symmetries of quantum models.

**"230 space groups are just different lattice shapes."**
The 14 Bravais lattices are the translation subgroups. The 230 space groups also
incorporate point symmetries (rotations, reflections) AND screw axes (rotation +
fractional translation) and glide reflections (reflection + fractional translation).
The additional elements beyond the 32 point groups are what give the full count of 230.
