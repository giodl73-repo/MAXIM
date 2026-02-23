# 04 — Zero-Knowledge Proofs & MPC

## Interactive Proofs, Schnorr, SNARKs/STARKs, Garbled Circuits, Secret Sharing

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Interactive proof systems: completeness, soundness, computational vs statistical soundness; IP complexity class (IP = PSPACE); AM vs MA; interactive proofs as complexity-theoretic foundation for ZK
- Zero-knowledge definitions: perfect ZK vs computational ZK vs statistical ZK; simulator paradigm (if verifier can simulate the interaction without the witness, the proof reveals nothing); honest-verifier vs malicious-verifier ZK
- Sigma protocols (Σ-protocols): commit → challenge → response structure; Schnorr identification (DLP-based), Pedersen commitment scheme (homomorphic!); special soundness (two transcripts → witness extraction); honest-verifier ZK → ZK via Fiat-Shamir transform
- Fiat-Shamir heuristic: replace interactive verifier with hash function in ROM; makes interactive proofs non-interactive; security in ROM vs standard model; applications in SNARKs
- Commitment schemes: hiding + binding, Pedersen (computationally binding/perfectly hiding), hash-based (perfectly binding/computationally hiding); vector commitments, KZG polynomial commitments
- zkSNARKs: arithmetic circuit satisfiability, R1CS constraints, QAP (quadratic arithmetic programs), Groth16 (three-element proof, pairing check, trusted setup); Plonk (universal trusted setup); why SNARKs need trusted setup
- zkSTARKs: no trusted setup (transparent), uses collision-resistant hash only (post-quantum!), FRI (Fast Reed-Solomon IOP), larger proof size than SNARKs; StarkWare applications
- Secret sharing: Shamir (k,n)-threshold scheme (polynomial interpolation over finite field, information-theoretically secure), additive secret sharing; verifiable secret sharing (VSS)
- Multi-Party Computation (MPC): Yao's garbled circuits (boolean circuits, evaluator gets output without learning inputs), GMW protocol (secret sharing + OT), Beaver triples for multiplication; honest majority vs dishonest majority protocols
- Applications: zkRollups (Ethereum scaling), anonymous credentials, verifiable shuffle (e-voting), private set intersection, federated learning with MPC
