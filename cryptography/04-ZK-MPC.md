# 04 — Zero-Knowledge Proofs & Multi-Party Computation

## Interactive Proofs, Schnorr, SNARKs/STARKs, Garbled Circuits, Secret Sharing

---

## Big Picture: ZK and MPC Landscape

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       ZK / MPC LANDSCAPE                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  COMPLEXITY FOUNDATIONS                                                 │
│   IP = PSPACE; MIP = NEXPTIME; PCP theorem; AM/MA hierarchy            │
│   ZK proofs: completeness + soundness + zero-knowledge (simulator)     │
│                                                                         │
│  INTERACTIVE ZK (Σ-protocols)                                           │
│   Schnorr identification (DLP); Pedersen commitment (homomorphic)      │
│   Fiat-Shamir: interactive → non-interactive (NIZK) via random oracle  │
│                                                                         │
│  PROOF SYSTEMS FOR CIRCUITS                                             │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  zkSNARKs (Groth16, Plonk):                                     │    │
│  │    Succinct (O(1) proof); fast verify; needs trusted setup      │    │
│  │    Pairing-based; not post-quantum                              │    │
│  │  zkSTARKs (StarkWare):                                          │    │
│  │    No trusted setup; post-quantum; larger proof (~100KB)        │    │
│  │    FRI (Fast Reed-Solomon IOPP)                                 │    │
│  │  Bulletproofs:                                                  │    │
│  │    No trusted setup; logarithmic proof size; slow verify        │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  MULTI-PARTY COMPUTATION (MPC)                                          │
│   Secret sharing: Shamir; additive; VSS                                 │
│   Garbled circuits: Yao's; Boolean; 2-party                            │
│   GMW / BGW: n-party; honest majority; arithmetic circuits             │
│   Oblivious transfer: building block; OT extension                     │
│                                                                         │
│  APPLICATIONS                                                           │
│   zkRollups (Ethereum L2); anonymous credentials; PSI; e-voting        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Interactive Proof Systems

```
COMPLEXITY BACKGROUND (MIT TCS bridge):
  NP: efficient verifier; witness provided by prover; deterministic verification
  IP (Interactive Polynomial): multi-round interaction; randomized verifier; BPP ⊆ IP
  Arthur-Merlin (AM): public coins; Merlin = computationally unbounded prover; Arthur = probabilistic poly verifier
  IP = PSPACE (Shamir 1992): remarkable — graph non-isomorphism (in coNP \ P believed) has interactive proof!
  MIP (multiple provers): MIP = NEXPTIME; multiple non-communicating provers share no state

INTERACTIVE PROOF PROTOCOL:
  Prover P: computationally unbounded (or efficient for specific relation)
  Verifier V: probabilistic polynomial-time
  Protocol: multiple rounds of challenge-response
  Completeness: if statement true, honest prover convinces verifier with prob ≥ 2/3
  Soundness: if statement false, no prover can convince verifier with prob > 1/3
    (errors reducible to negligible by repetition)
  Amplification: k parallel repetitions → error ≤ (1/3)^k

ZERO-KNOWLEDGE DEFINITION (Goldwasser-Micali-Rackoff 1985):
  Perfect ZK: ∃ simulator S such that {View_V(P(x,w) ↔ V(x))} ≡ {S(x)} (identically distributed)
  Statistical ZK: distributions statistically indistinguishable (SD negligible)
  Computational ZK: distributions computationally indistinguishable (PPT can't distinguish)

  Simulator paradigm: if a simulator can produce views (without the witness) that are
    indistinguishable from real proofs, then the verifier "could have generated it themselves"
    → interaction revealed nothing about witness

HONEST-VERIFIER vs MALICIOUS-VERIFIER ZK:
  Honest-verifier ZK (HVZK): only holds if verifier follows protocol (sends random challenges)
  Malicious-verifier ZK: holds even if verifier chooses challenges adversarially (stronger)
  Σ-protocols: typically HVZK; convert to malicious-verifier via compiler (e.g., CDS composition)
  Fiat-Shamir: removes verifier entirely (hash replaces interaction) → NIZK

PROOF OF KNOWLEDGE (PoK):
  Stronger than just proving statement true: prover "knows" a witness
  Knowledge extractor: PPT algorithm E with black-box access to prover that extracts witness
  Special soundness: 2 accepting transcripts with same commitment → extractor works
  Knowledge soundness: computational variant (extractable only from efficient provers)
```

---

## 2. Sigma Protocols (Σ-protocols)

```
Σ-PROTOCOL STRUCTURE:
  Three-move: Commit (a) → Challenge (e) → Response (z)
  P → V: commitment a    (prover commits to randomness)
  V → P: challenge e ← {0,1}^t   (t-bit random challenge)
  P → V: response z
  V accepts if Verify(x, a, e, z) = 1

SCHNORR IDENTIFICATION (Claus Schnorr 1989):
  Proves knowledge of discrete log x such that y = g^x (in prime-order group)
  Statement: "I know x such that y = g^x"
  Not: "here is x" — prover convinces verifier without revealing x

  Protocol:
    P: r ← ℤ_q uniformly; a = g^r  → send a to V
    V: e ← ℤ_q random              → send e to P
    P: z = r + x·e mod q            → send z to V
    V: verify g^z = a · y^e ?

  Correctness: g^z = g^{r+xe} = g^r · g^{xe} = a · y^e ✓
  HVZK simulator: choose z, e randomly; compute a = g^z · y^{-e}
    Transcript (a, e, z) distributed identically to real transcript
  Special soundness: two accepting transcripts (a, e₁, z₁) and (a, e₂, z₂) with e₁≠e₂:
    g^{z₁} = a·y^{e₁};  g^{z₂} = a·y^{e₂}
    g^{z₁-z₂} = y^{e₁-e₂} → x = (z₁-z₂)/(e₁-e₂) mod q  (extract witness)

NON-INTERACTIVE VIA FIAT-SHAMIR (ROM):
  Replace V's challenge with hash: e = H(g, y, a) (or H(stmt || a))
  Prover computes: a = g^r; e = H(g, y, a); z = r + x·e mod q
  Proof: (a, z)   [e implicitly deterministic from hash]
  NIZK: no interaction; verifier re-computes e' = H(g, y, a); checks g^z = a·y^{e'}
  Security: secure in ROM; cannot extract randomness r from hash challenge
  Fiat-Shamir security failure in standard model: known attacks on Σ-protocols without ROM

PEDERSEN COMMITMENT:
  Setup: G, H = [t]G where t unknown (discrete log of H w.r.t. G unknown to all)
  Commit(m, r) = [m]G + [r]H   (m = message, r = random blinding)
  Binding: can't open to two different values → requires solving DLP
  Hiding: perfectly hiding — commitment reveals nothing about m (for any m, any commitment
    matches some random r; discrete log assumption not needed for hiding)

  Homomorphic: C(m₁,r₁) + C(m₂,r₂) = C(m₁+m₂, r₁+r₂)
    Enables proofs about sums without revealing values (Confidential Transactions, range proofs)
  Opening proof: Pedersen commitment can be opened via Schnorr PoK of (m, r)

COMPOSITION: CONJUNCTIONS AND DISJUNCTIONS:
  AND of two Σ-protocols: run them in parallel; share challenge
  OR of two (prove one of two statements without revealing which):
    CDS construction (Cramer-Damgård-Schoenmakers): simulate one branch; prove other
    One real transcript + one simulated transcript → share overall challenge
    → "proof that x₁ OR x₂ holds" without revealing which
  Applications: anonymous credentials (prove attribute matches one of N without saying which)

```
ANONYMOUS CREDENTIALS — ZK PRIMITIVE TO DEPLOYED SYSTEM MAP:

  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │  System      │ ZK Primitive            │ Selective  │ Unlinkable │ Issuer-hiding    │
  │              │                         │ Disclosure │            │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │  BBS+        │ Pairing-based Σ-proto   │ Yes (any   │ Yes (per-  │ No (issuer pub   │
  │  (W3C VC DI) │ on BLS12-381; Pedersen  │ attribute  │ show proof │ key visible)     │
  │              │ commitment per attr)    │ subset)    │ randomized)│                  │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │  iDemix      │ Camenisch-Lysyanskaya   │ Yes        │ Yes (fresh │ No               │
  │  (Hyperledger│ (CL) signatures; RSA-   │            │ pseudonym  │                  │
  │  Fabric)     │ based commitments       │            │ per show)  │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │  U-Prove     │ Discrete-log blind sig; │ Yes (token │ Partial    │ No               │
  │  (Microsoft) │ Schnorr-style; one-show │ per show;  │ (one-show  │                  │
  │  Research    │ tokens                  │ selective) │ tokens)    │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────┤
  │  zk-SNARK    │ Groth16/Plonk circuit   │ Yes (any   │ Yes        │ Yes (circuit     │
  │  based ID    │ for credential checks   │ predicate) │            │ can hide issuer) │
  └─────────────────────────────────────────────────────────────────────────────────────┘

  Key ZK primitive in BBS+: prover holds Schnorr-style proof of knowledge of signature
    without revealing which attributes were signed or which presentation corresponds to
    which credential issuance → unlinkability from issuer and between presentations.

  W3C Verifiable Credentials ecosystem:
    Credential: JSON-LD document; issuer signs with BBS+ or Ed25519
    Presentation: holder produces selective-disclosure proof; verifier checks
    BBS+ advantage over plain EdDSA signatures: EdDSA reveals full credential on presentation;
      BBS+ proves "I hold a valid credential with age ≥ 18" without showing full credential or
      creating a linkable identifier between presentations.

  EU Digital Identity Wallet (ARF spec): mandates selective disclosure credentials;
    likely BBS+ or SD-JWT (a lighter-weight standard without full unlinkability).
    SD-JWT: not ZK-based; issuer pre-commits to attribute hash set; holder reveals subset;
    simpler but presentations are linkable (no Σ-protocol blindness).
```
```

---

## 3. KZG Commitments and Polynomial IOP

```
KZG POLYNOMIAL COMMITMENT (Kate-Zaverucha-Goldberg 2010):
  Trusted setup: SRS (Structured Reference String) = [1]₁, [τ]₁, [τ²]₁,...,[τᵈ]₁, [τ]₂
    τ is toxic waste — must be destroyed; if known, proofs can be forged
  Commit to polynomial f(x) = Σ fᵢ xⁱ:
    C = Σ fᵢ [τⁱ]₁ = [f(τ)]₁  (pairing-curve group element)
  Opening proof at point z: prove f(z) = y
    Witness polynomial: q(x) = (f(x) - y) / (x - z)  (division without remainder if f(z)=y)
    Proof: π = [q(τ)]₁
  Verification (using pairing): e(C - [y]₁, [1]₂) = e(π, [τ]₂ - [z]₂)
    Verifies: f(τ) - y = q(τ)·(τ - z) without revealing f

  Properties:
    Succinct: proof is 1 group element (48 bytes on BLS12-381)
    Evaluation binding: can't produce different y for same z with same C (under DL assumption)
    Requires trusted setup (τ must be unknown; multi-party ceremony)
  Use: Plonk, zkEVM; EIP-4844 (proto-danksharding) for Ethereum DA blobs
```

---

## 4. zkSNARKs

```
SNARK = Succinct Non-interactive ARgument of Knowledge

CIRCUIT SATISFIABILITY:
  Arithmetic circuit over 𝔽: ADD gates and MUL gates; wires carry field elements
  Public inputs (x) + private witness (w) → circuit satisfied if all gate constraints hold
  Relation R: (x, w) ∈ R iff circuit C(x, w) = 0
  Goal: prove C(x, w) = 0 without revealing w

R1CS (Rank-1 Constraint System):
  Constraint: (A·z) ○ (B·z) = C·z  where z = [1 | public | witness]
  ○ = element-wise product; A, B, C are matrices with ≤1 nonzero per column (ideally)
  Each multiplication gate becomes one R1CS constraint
  Addition gates: free (linear constraints absorbed into matrices)

QAP (Quadratic Arithmetic Program) — Gennaro-Gentry-Parno-Raykova 2013:
  Encode R1CS constraints as polynomial divisibility check:
    Encode each wire assignment as polynomial evaluation
    Constraints satisfied ↔ target polynomial T(x) divides h(x) = A'(x)·B'(x) - C'(x)
  This encoding allows Fiat-Shamir-style non-interactive proofs via polynomial commitments

GROTH16 (2016) — most efficient zkSNARK:
  Proof: 3 group elements (~192 bytes on BN-254 curve)
  Verify: 3 pairing operations (~1.5ms)
  Security: under q-PKE (q-Power Knowledge of Exponent) + q-SDH assumptions in GM
  Trusted setup: circuit-specific; must re-run ceremony for each different circuit
  Applications: Zcash Sapling (before Groth16 → uses Groth16 in Sapling), StarkWare, zkEVM

PLONK (Permutation-based SNARK, Gabizon-Williamson-Ciobotaru 2019):
  Universal trusted setup: one ceremony covers all circuits of bounded size
  Verification: ~2 pairings; proof ~3-4× larger than Groth16
  Programming model: PLONK arithmetization; custom gates (plookup, range checks)
  Used in: Aztec, Polygon zkEVM, zkSync, many zkRollup systems
  Variants: TurboPlonk (custom gates), UltraPlonk (lookup tables), HyperPlonk

TRUSTED SETUP CEREMONIES:
  Powers of Tau: multi-party computation where each contributor adds randomness to τ
  Security: if ANY ONE participant is honest and destroys their randomness → τ unknown
  Zcash Powers of Tau 2017: 87 participants; elaborate theatrics to destroy toxic waste
  Aztec "Ignition" 2019: 176 participants
  Problem: anyone who can recover τ from the ceremony can forge proofs
```

---

## 5. zkSTARKs

```
STARK = Scalable Transparent ARgument of Knowledge
  Transparent: no trusted setup; public verifiable randomness (hash-based)
  Post-quantum: security based on collision-resistant hash functions only (no pairings)
  Trade-off: larger proofs (~100KB vs ~200 bytes for Groth16) but faster prover

CONCEPTUAL STRUCTURE:
  Encode computation as polynomial; check polynomial properties via IOP

FRI (Fast Reed-Solomon IOPP — Interactive Oracle Proof of Proximity):
  Prove: polynomial f of degree ≤ d is "close to" a degree-d Reed-Solomon codeword
  Protocol: recursive halving — f(x) → split into even/odd coefficients → new poly of degree d/2
  Verifier queries small number of positions; soundness via list-decoding bounds
  Logarithmic rounds; logarithmic proof size relative to circuit; quasi-linear prover

ARITHMETIZATION:
  AIR (Algebraic Intermediate Representation): trace constraints on computation
  STARK traces: column per register; row per time step; boundary + transition constraints
  Encode execution trace as polynomial evaluations over evaluation domain
  Constraint polynomial must vanish on domain → check via FRI

COMPARISON: SNARK vs STARK:
  ┌────────────────────────────────────────────────────────────────────────┐
  │  Property       │ Groth16        │ Plonk         │ STARKs              │
  ├────────────────────────────────────────────────────────────────────────┤
  │  Proof size     │ 192 bytes      │ ~1.5 KB       │ ~100-500 KB       │
  │  Verify time    │ ~1.5ms (3 prs) │ ~2ms          │ ~10-50ms          │
  │  Prove time     │ Moderate       │ Moderate      │ Faster for large  │
  │  Trusted setup  │ Circuit-specific│ Universal    │ None (transparent) │
  │  Post-quantum?  │ No             │ No            │ Yes               │
  │  Assumption     │ Pairings + q-PKE│ Pairings + AGM│ Collision-resist. │
  └────────────────────────────────────────────────────────────────────────┘

STARKNET / STARKWARE:
  ZK-rollup on Ethereum using STARKs
  Cairo: programming language → compiles to AIR trace → STARK proof
  Recursive proofs: prove a proof verifier; verify many sub-proofs in one STARK
  EVM verification: STARK proof that Ethereum transactions executed correctly → post to L1
```

---

## 6. Secret Sharing

```
SHAMIR (k, n)-THRESHOLD SECRET SHARING:
  Share secret s among n parties; any k can reconstruct; fewer than k learn nothing
  Construction over finite field 𝔽_p (p > n, p > s):
    Choose random polynomial f(x) = s + a₁x + a₂x² + ... + a_{k-1}x^{k-1} over 𝔽_p
    Share i: (i, f(i)) for i = 1, ..., n
  Reconstruction: Lagrange interpolation from any k shares
    f(0) = s = Σᵢ f(xᵢ) · Πⱼ≠ᵢ (0 - xⱼ)/(xᵢ - xⱼ) (mod p)
  Information-theoretic security: any k-1 shares reveal NOTHING about s
    (any value of s consistent with any k-1 shares — polynomial not determined)

ADDITIVE SECRET SHARING:
  2-party: s₁ ← 𝔽_p random; s₂ = s - s₁ mod p; reconstruct: s₁ + s₂ = s
  n-party: s₁,...,s_{n-1} random; sₙ = s - Σᵢ sᵢ
  Simpler than Shamir; only (n,n) threshold (need ALL shares)
  Used in: GMW MPC protocol; MPC additions over additive shares are "free"

VERIFIABLE SECRET SHARING (VSS):
  Dealer may be malicious; share must be verifiable without revealing secret
  Feldman VSS: Pedersen commitment to polynomial coefficients; parties verify their share
    Setup: publish {[a₀]G, [a₁]G, ..., [a_{k-1}]G} (commitments to polynomial coefficients)
    Share i: f(i); verify [f(i)]G = Σⱼ [aⱼ]G · i^j (check against commitments)
  Pedersen VSS: perfectly hiding (Feldman VSS is computationally hiding)
  Applications: distributed key generation (DKG) for threshold signatures; TSS (threshold ECDSA/BLS)
```

---

## 7. Multi-Party Computation (MPC)

```
MPC GOAL:
  n parties with private inputs x₁,...,xₙ compute f(x₁,...,xₙ) together
  Correctness: output is correct
  Privacy: each party learns only output (and what output implies about others' inputs)
  No trusted third party; semi-honest vs malicious adversary model

YAO'S GARBLED CIRCUITS (2-party, semi-honest, 1982):
  Reduce any function to Boolean circuit; circuit garbled by one party
  Garbler G: for each gate, encrypt truth table with random wire labels
    Each wire has two random labels: W_0 and W_1  (representing 0 and 1)
    AND gate truth table: 4 ciphertexts = {Enc_{W_a || W_b}(W_c) for all a,b ∈ {0,1}}
    Shuffle to hide which entry is which
  Evaluator E: has actual input wire labels; evaluates gates via decryption
    Can only decrypt ONE entry per gate (the one matching its wire labels)
  Oblivious Transfer (OT): evaluator gets correct input wire labels without garbler learning inputs
  Output: evaluator gets output labels; garbler reveals which labels = 0/1

  Complexity: O(|C| · λ) bits; C = circuit size; λ = security parameter
  Improvements: Free XOR (XOR gates free — just XOR wire labels), half-gates, 3-halving

OBLIVIOUS TRANSFER (OT):
  1-of-2 OT: sender has (m₀, m₁); receiver has bit b; receiver gets m_b; sender learns nothing
  Foundational primitive for MPC (GMW completeness result)
  Construction from ECC: ElGamal-style; sender generates (c₀, c₁); receiver decodes m_b only
  OT Extension (Beaver 1996; IKNP 2003): extend k OTs into m OTs using symmetric crypto
    Reduces: m OTs → k base OTs + O(m·k) symmetric ops; far more efficient

GMW PROTOCOL (Goldreich-Micali-Wigderson 1987):
  n-party; any function; based on secret sharing + OT
  Addition gates: parties locally add their shares (no interaction)
  Multiplication gates: require communication — protocol uses Beaver multiplication triples
  Security: if < n/2 semi-honest corruptions → information-theoretically secure
  Malicious: need authentication (MACs over shares); SPDZ/TinyOT extend GMW for malicious

BEAVER MULTIPLICATION TRIPLES:
  Pre-computation: dealer generates (a, b, c) where c = a·b (in 𝔽_p or ℤ₂)
    Share all three values: [a], [b], [c]
  Online multiplication of [x] and [y]:
    Open [x-a] = ε and [y-b] = δ (both public after opening)
    [z] = [c] + δ[a] + ε[b] + εδ   (no interaction except the two openings)
  Beaver triples enable: 1 multiplication = 2 openings (network round) + local arithmetic

THRESHOLD SIGNATURES (ECDSA/BLS MPC):
  Threshold-t ECDSA: t-of-n parties jointly sign without any party knowing full key
    Key generation: DKG (Distributed Key Generation via VSS); parties share secret key
    Signing: MPC protocol computes ECDSA signature; reveals only (r, s) signature
    Protocols: GG18 (Gennaro-Goldfeder), CGGMP21, DKLS18 (most efficient for 2-party)
  BLS threshold: simpler due to BLS aggregation; each party signs locally; aggregate
  Applications: multi-sig wallets (Coinbase, Fireblocks); distributed CA signing

PRIVATE SET INTERSECTION (PSI):
  Alice has set X, Bob has set Y; both learn X ∩ Y; reveal nothing else
  Construction (DH-PSI): based on 2-key OPRF (Oblivious PRF)
    Alice: OPRF_k_A(x) for each x ∈ X; Bob: OPRF_k_B(y) for each y ∈ Y
    Intersection: where pseudorandom outputs match
  Applications: contact discovery (WhatsApp, Google), ad attribution without revealing data
```

---

## 8. Applications

```
ZKROLLUPS (ETHEREUM L2 SCALING):
  Problem: Ethereum L1 ~15 TPS; too slow + expensive for applications
  zkRollup: batch thousands of transactions off-chain; post single SNARK/STARK proof to L1
    L1 verifies proof: O(1) verification regardless of batch size
    L1 data availability: either post-chain (zk Rollup) or off-chain (Validium)

  Proof systems in production (2024):
    zkSync Era: Plonk-based custom prover
    Polygon zkEVM: STARKs + SNARKs recursion
    StarkNet: STARKs (Cairo language)
    Linea: Plonk
    Scroll: Plonk zkEVM
    Aztec: Plonk (privacy-first; private transactions)

EIP-4844 (PROTO-DANKSHARDING):
  Introduces blob transactions: off-chain data "blobs" for L2 data availability
  KZG commitments: blob = polynomial; commitment = KZG(blob); rollups post commitment to L1
  Verifiers can check specific positions in blob via KZG opening proof (not entire blob)
  Reduces L2 costs ~10x by cheaper data posting than calldata

ANONYMOUS CREDENTIALS:
  Prove attributes (age ≥ 18, nationality, membership) without revealing identity
  Construction: issuer signs credential; user proves valid signature + attribute via ZK
  ZKVM / zk-ID: prove circuit satisfiability on attribute checks
  iDemix (IBM), U-Prove (Microsoft), BBS+ (now W3C VC draft): production anonymous cred systems

VERIFIABLE SHUFFLE (E-VOTING):
  Re-encryption shuffle: shuffle encrypted votes; prove shuffle is correct permutation (no vote changed)
  Construction: Groth-Lu shuffle proof; verifiable by election observers
  Full protocol: ElGamal encrypt votes; threshold decryption; public transcript

FEDERATED LEARNING WITH MPC / DP:
  Model updates from clients: don't reveal individual user data
  Secure aggregation: MPC to sum gradients without coordinator seeing individuals
  Differential privacy: add calibrated noise to aggregated gradients
  Production: Google Gboard federated learning; Apple keyboard suggestion
```

```
ENTERPRISE ZK/MPC APPLICATIONS (non-blockchain):

  THRESHOLD SIGNING FOR CLOUD KMS:
    Problem: single HSM holds signing key → single point of failure + compromise
    MPC solution: signing key distributed across 2+ parties; any single party cannot sign
    Pattern: 2-of-3 threshold ECDSA; sign requires quorum; no party has full key
    Production: Fireblocks (MPC wallet infrastructure), Coinbase Custody, Azure Managed HSM
      multi-party authorization (requires multiple admin approvals; conceptually MPC-like)
    FROST (RFC 9591): threshold Schnorr/Ed25519; standardized; usable in any signing pipeline
    Use case: code signing where build system + security team must both approve; CA signing key

  PSI IN HEALTHCARE AND AD-TECH:
    Healthcare consortia:
      Hospital A + Hospital B: compute intersection of patient IDs (for cohort studies)
        without either hospital learning patients not in the intersection
      Protocol: DH-PSI (OPRF-based); O(n log n); n = dataset size
      Use: FDA Sentinel Network (safety signal detection); HIPAA-compliant cross-institution studies

    Ad attribution:
      Advertiser has set of users who saw ad; Publisher has set of users who made purchase
      PSI reveals count (or set) of overlap without either party learning the other's full set
      Production: Google PAIR (Publisher Advertiser Identity Reconciliation) uses PSI concepts
      Also: Apple's SKAdNetwork uses aggregation; Meta's Private Lift uses MPC

  ZK PROOFS FOR COMPLIANCE REPORTING:
    Classic problem: prove compliance without disclosing sensitive data
    ZK approach: prove a predicate about your data using a ZK circuit

    Examples:
      "My company holds valid SOC2 certification" (without revealing audit report details)
        → ZK proof that auditor's signature over certification is valid
      "All transactions in this batch are ≤ $10,000" (AML reporting threshold)
        → Range proof (Bulletproofs) proving sum or max without revealing individual values
      "This entity is not on the OFAC sanctions list"
        → ZK set non-membership proof
      EU Digital Identity Wallet: present "age ≥ 18" without revealing date of birth or
        credential identifier (unlinkable across verifiers) — BBS+ selective disclosure

    Current maturity: ZK for compliance is emerging; most production systems still use
      trusted auditors; ZK infrastructure is reaching usability (2024-2026 window).
```

## 8a. Library and Framework Bridge

```
ZK/MPC LIBRARY LANDSCAPE — FROM THEORY TO IMPLEMENTATION:

  zkSNARK TOOLCHAINS:
  ┌────────────────────────────────────────────────────────────────────────────────┐
  │  Library / Tool  │ Proof System    │ Language  │ Key Property                  │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  circom + snarkjs│ Groth16         │ JS/TS     │ Widely used; Groth16 (circuit-│
  │                  │                 │           │ specific setup); zkRollup std  │
  │  halo2           │ PLONKish (IPA)  │ Rust      │ No trusted setup; recursive;  │
  │                  │                 │           │ Zcash Orchard, scroll use it  │
  │  arkworks        │ Groth16, Plonk  │ Rust      │ Modular; any curve; research   │
  │                  │                 │           │ + production; full ecosystem   │
  │  gnark           │ Groth16, Plonk  │ Go        │ Fast prover; production use   │
  │                  │                 │           │ in ConsenSys zkEVM             │
  │  bellman         │ Groth16         │ Rust      │ Original Zcash Sapling lib;   │
  │                  │                 │           │ well-audited; more rigid API   │
  └────────────────────────────────────────────────────────────────────────────────┘

  MPC FRAMEWORKS:
  ┌────────────────────────────────────────────────────────────────────────────────┐
  │  Library         │ Protocol        │ Language  │ Key Property                  │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  MP-SPDZ         │ SPDZ, GMW, semi │ C++/Python│ Most protocol variants; used  │
  │                  │ -honest models  │           │ by researchers and industry    │
  │  SCALE-MAMBA     │ SPDZ2k, SPDZ   │ C++       │ Production-ready fork of SPDZ │
  │  Sharemind       │ Additive SS     │ C++       │ Privacy analytics platform;   │
  │                  │                 │           │ enterprise deployment          │
  │  OpenMPC         │ Yao GC + GMW    │ C++       │ Two-party focused; research    │
  └────────────────────────────────────────────────────────────────────────────────┘

  THRESHOLD SIGNATURES (production-ready):
  ┌────────────────────────────────────────────────────────────────────────────────┐
  │  Library         │ Algorithm       │ Language  │ Key Property                  │
  ├────────────────────────────────────────────────────────────────────────────────┤
  │  FROST (RFC 9591)│ Threshold       │ Rust/Go   │ IETF standard; threshold      │
  │                  │ Schnorr/Ed25519 │ (multiple)│ Schnorr with preprocessing    │
  │  tss-lib         │ Threshold ECDSA │ Go        │ GG18 protocol; used in        │
  │  (binance)       │ (GG18)          │           │ Binance Chain, Fireblocks     │
  │  CGGMP21         │ Threshold ECDSA │ Rust      │ Latest ECDSA TSS protocol;    │
  │  (dfns)          │                 │           │ better security than GG18     │
  │  dkls18          │ 2-party ECDSA   │ Go/Rust   │ Most efficient 2-of-2;        │
  │                  │                 │           │ used in MPC wallets            │
  └────────────────────────────────────────────────────────────────────────────────┘

  FROST (RFC 9591) is the clearest starting point for threshold signatures:
    Threshold t-of-n Ed25519 or Schnorr; IETF RFC 9591 (2023)
    DKG phase: parties collectively generate (public_key, shares) without trusted dealer
    Signing: t parties each produce a partial signature; coordinator aggregates
    Binding factor: prevents rogue-key attacks; each party's nonce commits to participant set
    Use case: cloud KMS multi-party authorization, distributed validator technology

  CIRCOM WORKFLOW (most accessible zkSNARK entry point):
    1. Write circuit in circom: template Multiplier() { signal input a; signal input b;
       signal output c; c <== a * b; }
    2. npm install circom snarkjs; circom circuit.circom --r1cs --wasm
    3. snarkjs groth16 setup circuit.r1cs pot12.ptau circuit_0000.zkey (trusted setup)
    4. Generate witness + proof: snarkjs groth16 prove; verify: snarkjs groth16 verify
    5. Generate Solidity verifier: snarkjs zkey export solidityverifier
```

---

## 9. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| IP complexity class equals? | PSPACE (Shamir 1992) |
| ZK simulator paradigm means? | Verifier can simulate interaction without witness → proof reveals nothing |
| Schnorr proof: what does it prove? | Knowledge of x such that y = g^x (discrete log) without revealing x |
| Fiat-Shamir: what does it replace? | Interactive verifier challenge replaced with H(commitment || statement) in ROM |
| Pedersen commitment: binding vs hiding? | Computationally binding (DL assumption); perfectly hiding |
| Groth16 proof size? | 3 group elements ≈ 192 bytes; 3 pairing verifications |
| Trusted setup ceremony failure? | If any participant's randomness (τ) recovered → proofs can be forged |
| SNARK vs STARK trusted setup? | SNARKs require trusted setup; STARKs are transparent (hash-based only) |
| Shamir (k,n): what k-1 shares reveal? | Nothing (information-theoretically secure) |
| Beaver triple purpose? | Enable multiplication in MPC with just 2 network messages per mult gate |
| OT extension: what does it reduce? | m OTs → k base OTs + cheap symmetric crypto (Beaver/IKNP extension) |
| KZG commitment opens in? | 1 group element proof (48 bytes BLS12-381); constant size |
| FRI in STARKs: what is proven? | Low-degree of polynomial via Reed-Solomon IOP proximity testing |
| BLS threshold simpler than ECDSA? | BLS signatures are aggregatable: each party signs, aggregate; no complex MPC needed |

---

## Common Confusion Points

**ZK proof ≠ proof of correctness:** A ZK proof proves that the prover KNOWS a witness satisfying some relation. It doesn't prove the witness itself. A prover could know x such that y = g^x (Schnorr) without you knowing x. "ZK" means the proof reveals nothing BEYOND the fact that the prover knows the witness.

**"Proof of knowledge" vs "argument of knowledge":** Proof = information-theoretic soundness (even computationally unbounded cheating prover can't succeed). Argument = computational soundness (relies on hardness assumption). SNARKs are technically "arguments," not "proofs" — their soundness relies on computational hardness. The acronym uses "Argument" correctly. For practical purposes, "argument" is fine assuming cryptographic hardness holds.

**Trusted setup ≠ trusted party ongoing:** A trusted setup ceremony happens once and can be distributed (MPC ceremony). After the ceremony, the toxic waste (τ) is destroyed. The resulting SRS can be used by anyone to generate and verify proofs — no ongoing trust. The trust is concentrated in: "was the ceremony run honestly and is τ truly unknown?" Multi-party ceremonies reduce this to: "was at least one participant honest?"

**Garbled circuits evaluate once:** A garbled circuit can only be evaluated on ONE specific set of inputs (the garbled wire labels correspond to specific bits). To evaluate on different inputs, garbler must re-garble. This is fine for 2-party computation where inputs are fixed for the session. Garbled circuits are NOT general-purpose functions you can evaluate repeatedly on different inputs.

**PSI reveals intersection but not membership per se:** In basic DH-PSI, both parties learn the intersection set. This might still reveal more than intended — if the intersection is a single element, Alice knows Bob has exactly that element. "Cardinality PSI" (only reveals |X ∩ Y|) and "PSI-CA" (only reveals count) are variants for different privacy requirements.

**STARK proof size grows with circuit size, SNARK doesn't:** SNARK (Groth16) proof is constant size regardless of circuit. STARK proof size is O(log² n) where n = computation size. For tiny circuits, STARKs have much higher constant overhead. For massive computations (large zkEVM traces), STARKs' better prover performance can outweigh larger proof size. This is why zkRollups choose differently based on their computation profile.
