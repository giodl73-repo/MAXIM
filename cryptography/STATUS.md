# cryptography/ — Status

**6 files | Complete ✅**
*Session 23 — Formal security definitions, ZK proofs, post-quantum, full reduction proofs*
*Bridge: number theory (18), information theory (04-ML-CRYPTOGRAPHY-BRIDGE), computing/25-SECURITY*
*MIT TCS background assumed — goes to full complexity-theoretic reductions*

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | Field map — security definitions (IND-CPA/IND-CCA/EUF-CMA), computational assumptions, random oracle model, hybrid arguments | ✅ complete |
| `01-SYMMETRIC.md` | Symmetric — AES internals (SubBytes/ShiftRows/MixColumns/KeySchedule), modes (GCM/CCM/SIV), ChaCha20-Poly1305, authenticated encryption | ✅ complete |
| `02-ASYMMETRIC.md` | Asymmetric — RSA (full OAEP reduction), Diffie-Hellman, discrete log hardness, elliptic curves (ECDH/ECDSA/Ed25519), pairing-based crypto | ✅ complete |
| `03-PROTOCOLS.md` | Protocols — TLS 1.3 handshake (full transcript), SSH, Signal protocol (X3DH + Double Ratchet), Noise protocol framework, certificate transparency | ✅ complete |
| `04-ZK-MPC.md` | ZK & MPC — interactive proofs (IP=PSPACE), Schnorr/Fiat-Shamir, Pedersen commitments, SNARKs/STARKs (circuit satisfiability), garbled circuits, secret sharing | ✅ complete |
| `05-POST-QUANTUM.md` | Post-quantum — lattice hardness (LWE/SIS/NTRU), Kyber (ML-KEM), Dilithium (ML-DSA), SPHINCS+ (hash-based), NIST PQC round 4, quantum threat timeline | ✅ complete |
