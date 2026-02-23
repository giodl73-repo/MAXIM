# 03 — Cryptographic Protocols

## TLS 1.3, SSH, Signal Protocol, Noise Framework

> **STUB** — outline only, content to be authored

**Planned coverage:**
- TLS 1.3 handshake (full transcript): ClientHello (key_share + supported_groups + cipher_suites) → ServerHello (key_share selection) → {EncryptedExtensions + Certificate + CertificateVerify + Finished} → {Finished} → application data; 1-RTT vs 0-RTT (replay risks)
- TLS 1.3 cryptography: HKDF-based key schedule (handshake/application/resumption secrets), AEAD-only (AES-GCM-128/256, ChaCha20-Poly1305), forward secrecy (DHE required, no static RSA/DH)
- TLS certificate chain: X.509 structure, certificate authorities, OCSP/CRL revocation, OCSP stapling, certificate transparency (CT logs + SCTs), CAA DNS records; let's Encrypt as DV CA
- SSH protocol: architecture (transport/authentication/connection layers), host key verification (TOFU vs CA), public key auth (challenge-response with Ed25519/RSA), certificate-based SSH (openssh certificates vs X.509)
- Signal Protocol: X3DH (Extended Triple Diffie-Hellman) for initial key establishment (identity/signed prekey/one-time prekeys), Double Ratchet Algorithm (symmetric-key ratchet + DH ratchet), forward secrecy + break-in recovery, sealed sender
- Noise Protocol Framework: handshake patterns (NN/NK/NX/KK/KX/XX/IX), message patterns, prologue/payload, composability; WireGuard as Noise IKpsk2 instantiation
- Authentication protocols: challenge-response, SCRAM, SRP (Secure Remote Password — PAKE), FIDO2/WebAuthn (hardware authenticators, public key ceremony, attestation)
- Key management: key lifecycle (generation/distribution/storage/rotation/revocation/destruction), HSMs (hardware security modules), key wrapping, PKCS#11 API
- Protocol composition: Needham-Schroeder attack (why you must include identity in handshake), Lowe fix, formal verification tools (Tamarin/ProVerif/Verifpal) for protocol analysis
