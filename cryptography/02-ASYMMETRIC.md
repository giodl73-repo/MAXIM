# 02 — Asymmetric Cryptography

## RSA, Diffie-Hellman, Elliptic Curves, Pairings

> **STUB** — outline only, content to be authored

**Planned coverage:**
- RSA: key generation (pick primes p,q; n=pq; φ(n)=(p-1)(q-1); choose e coprime to φ(n); d=e⁻¹ mod φ(n)), encryption (c=mᵉ mod n), decryption (m=cᵈ mod n); correctness via Fermat/Euler theorem; why textbook RSA is insecure
- RSA-OAEP: OAEP padding scheme, reduction proof (IND-CCA2 secure in ROM if RSA is one-way), why PKCS#1 v1.5 padding is dangerous (BLEICHENBACHER '98 attack, still active in 2023 as "ROBOT")
- Integer factorization: trial division → Pollard rho → quadratic sieve → general number field sieve; current records (~829 bits RSA-768 factored 2009, RSA-2048 still safe); key size recommendations (3072-bit RSA ≈ 128-bit symmetric)
- Discrete logarithm: DLOG in ℤₚ*, baby-step-giant-step, index calculus; DLOG in elliptic curve groups (no subexponential algorithm known — why ECC keys can be smaller)
- Diffie-Hellman: classic (ℤₚ* group), security based on CDH/DDH assumptions, key exchange (not authentication!), authenticated key exchange as additional requirement
- Elliptic curves: Weierstrass form y²=x³+ax+b over 𝔽ₚ, group law (chord-and-tangent), ECDH (replace ℤₚ* with EC group), ECDSA (signature scheme), Ed25519 (Edwards curve, faster and safer implementation)
- Curve selection: P-256/P-384/P-521 (NIST curves — alleged backdoor concerns), Curve25519/Ed25519 (Bernstein — clean design, no suspicious parameters), security parameters comparison
- Pairing-based cryptography: bilinear pairings e: G₁×G₂→Gₜ, Weil/Tate/ate pairings; BLS signatures (aggregatable), identity-based encryption (Boneh-Franklin), zk-SNARKs (Groth16 uses pairings)
- Hybrid encryption: use asymmetric only for key encapsulation (KEM), then symmetric (DEM); KEM-DEM framework; why you never encrypt large data with RSA directly
