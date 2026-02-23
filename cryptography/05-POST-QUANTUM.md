# 05 — Post-Quantum Cryptography

## Lattice Hardness, Kyber/Dilithium, Hash-Based, NIST PQC, Quantum Threat

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Quantum threat: Shor's algorithm breaks RSA/ECDH/ECDSA in polynomial time on a quantum computer; Grover's algorithm gives √ speedup for symmetric (double key lengths for 128-bit quantum security); timeline estimates (2030-2040 cryptographically relevant QC, high uncertainty)
- Harvest-now-decrypt-later (HNDL) attacks: adversaries capturing encrypted traffic today to decrypt post-quantum; why migration urgency exists now for long-lived secrets
- Lattice problems: Short Integer Solution (SIS), Learning With Errors (LWE — Regev 2005), Ring-LWE, Module-LWE; worst-case to average-case reduction (LWE as hard as worst-case lattice problems — GapSVP); parameter selection
- Kyber (ML-KEM, NIST FIPS 203): Module-LWE based KEM; three parameter sets (512/768/1024 — security levels 1/3/5); key sizes vs RSA comparison; encapsulation/decapsulation mechanism
- Dilithium (ML-DSA, NIST FIPS 204): Module-LWE + Module-SIS based signature; Fiat-Shamir with aborts construction; deterministic vs randomized signing; key/signature sizes
- SPHINCS+ (SLH-DSA, NIST FIPS 205): stateless hash-based signatures, hypertree structure (FORS + XMSS layers), post-quantum security based only on hash function security; large signatures (~8-50KB) are the downside
- BIKE/HQC/Classic McEliece: code-based candidates, code-based cryptography background (Goppa codes), large key sizes; why not in primary NIST standards
- Migration strategy: hybrid schemes (classical + PQC KEM in TLS/SSH — NIST recommendation), algorithm agility as architectural requirement, X.509 certificate dual-key support
- NIST PQC status (2024): ML-KEM/ML-DSA/SLH-DSA finalized as FIPS; ongoing evaluation of additional signatures (FALCON/MAYO/UOV); CNSA 2.0 (US gov requirements timeline)
