# 00 — Cryptography Overview

## Security Definitions, Computational Assumptions, Cryptographic Primitives

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Security definitions: IND-CPA (indistinguishability under chosen-plaintext attack), IND-CCA2 (adaptive chosen-ciphertext), EUF-CMA (existential unforgeability under chosen-message attack); why formal definitions matter (avoid "it feels secure" arguments)
- Computational assumptions hierarchy: one-way functions (if they exist → P≠NP, but stronger), pseudorandom generators, pseudorandom functions, trapdoor permutations; assumptions underlying standard constructions
- Random Oracle Model (ROM): hash functions as ideal random functions, ROM proofs vs standard model proofs, what ROM captures/misses
- Hybrid arguments: computational indistinguishability, hybrid game sequence, how reduction proofs work (adversary A breaks scheme → adversary B solves hard problem)
- Cryptographic primitives taxonomy: symmetric (block/stream ciphers, MACs, hash functions, KDFs) → asymmetric (PKE, digital signatures, key exchange) → advanced (ZK, MPC, FHE, IBE)
- Security parameters: λ (security parameter), asymptotic vs concrete security, bit-security levels (128-bit security standard), how to read security claims
- Perfect secrecy vs computational security: information-theoretic (Shannon, one-time pad) vs computational (polynomial-time adversary bounded); why computational is necessary for practical crypto
- Standard bodies and algorithm selection: NIST FIPS/SPs, IETF RFCs, ETSI standards; algorithm agility as engineering requirement
- Index of modules: symmetric, asymmetric, protocols, ZK/MPC, post-quantum
