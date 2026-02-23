# 01 — Symmetric Cryptography

## AES Internals, Modes of Operation, Authenticated Encryption, ChaCha20

> **STUB** — outline only, content to be authored

**Planned coverage:**
- AES internals: 128/192/256-bit keys, 10/12/14 rounds, four operations per round — SubBytes (S-box as GF(2⁸) multiplicative inverse), ShiftRows (byte permutation), MixColumns (GF(2⁸) matrix multiply), AddRoundKey (XOR with round key); key schedule (RotWord/SubWord/Rcon)
- AES mathematical foundation: GF(2⁸) = GF(2)[x]/(x⁸+x⁴+x³+x+1); why finite field arithmetic provides confusion/diffusion (Shannon); AES as a substitution-permutation network
- Block cipher modes: ECB (never use — reveals patterns), CBC (IV randomization, padding oracle vulnerability), CTR (stream cipher from block cipher, parallelizable), GCM (CTR + GHASH authentication — AEAD), CCM, SIV (nonce-misuse resistance)
- Authenticated Encryption (AEAD): encrypt-then-MAC vs MAC-then-encrypt vs Encrypt-and-MAC; why AEAD (GCM/ChaCha20-Poly1305) is the right default; nonce uniqueness requirement in GCM (catastrophic failure on reuse)
- ChaCha20-Poly1305: ARX design (Add-Rotate-XOR), 256-bit key + 96-bit nonce + 32-bit counter, quarter-round function, 20 rounds; Poly1305 MAC (polynomial evaluation over GF(2¹³⁰-5)); why preferred over AES-GCM in software without AES-NI
- Hash functions: SHA-2 (Merkle-Damgård with Davies-Meyer compression), SHA-3/Keccak (sponge construction), BLAKE3 (tree hashing + parallelism), length extension attacks on SHA-2
- MACs: HMAC (hash-based, security reduction from PRF), CMAC (cipher-based), Poly1305 (one-time MAC, universal hash family)
- KDFs and password hashing: HKDF (extract-then-expand), PBKDF2/bcrypt/scrypt/Argon2id — memory-hardness as defense against GPU/ASIC attacks; Argon2id recommended current standard
- Side-channel attacks: timing attacks (AES table lookups), cache attacks (Flush+Reload), countermeasures (constant-time implementations)
