# Computing & Software

10 directories · The full modern software engineering stack — from bare metal to intelligence layer

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         COMPUTING & SOFTWARE                                    │
└─────────────────────────────────────────────────────────────────────────────────┘

 FOUNDATION LAYER                     SYSTEMS LAYER
 ┌──────────────────┐                 ┌──────────────────────────────────────────┐
 │   languages/     │                 │              computing/                  │
 │  16 languages    │────────────────▶│  packages · containers · CI/CD · cloud   │
 │  type systems    │                 │  distributed · observability · security   │
 │  reference cards │                 │  (28 files — the master engineering track)│
 └──────────────────┘                 └──────────────────────┬───────────────────┘
         │                                                   │
 ┌──────────────────┐                                       │
 │   scripting/     │                                       ▼
 │  Bash/PS/Batch   │            INTELLIGENCE LAYER
 │  AWK/sed/Perl    │            ┌──────────────────────────────────────────────┐
 │  Fish/Zsh        │            │              ai-engineering/                 │
 └──────────────────┘            │  LLMs · transformers · RAG · fine-tuning     │
         │                       │  alignment · model families · evals          │
 ┌──────────────────┐            └──────────────────────────────────────────────┘
 │      os/         │
 │  Linux/Win/macOS │            DATA LAYER
 │  kernel · fs     │            ┌──────────────────┐  ┌───────────────────────┐
 │  process model   │            │  data-science/   │  │   query-languages/    │
 └──────────────────┘            │  NumPy · Pandas  │◀─▶│  SQL · T-SQL · KQL   │
                                 │  ML pipeline     │  │  DuckDB · PostgreSQL  │
                                 │  stats           │  │  analytical SQL       │
                                 └──────────────────┘  └───────────────────────┘

 SECURITY CROSS-CUT  (applies to all layers above)
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │  cryptography/  ·  symmetric · asymmetric · TLS 1.3 · Signal protocol      │
 │                 ·  zero-knowledge proofs · post-quantum (ML-KEM/SLH-DSA)   │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `computing/` | Modern engineering stack end-to-end: package managers, containers, Kubernetes, CI/CD, cloud architecture, distributed systems, observability (OTel/Prometheus/Grafana), security hardening | `01-PACKAGE.md` — package ecosystem taxonomy | `os/` for runtime substrate; `ai-engineering/` for ML infra patterns |
| `ai-engineering/` | LLM architecture (Transformer internals, tokenization, attention), RAG pipelines, fine-tuning, RLHF, alignment, major model families, eval harnesses | `01-LLM-CONCEPTS.md` — tokens through model families | `data-science/` for ML pipeline; `computing/` for serving infra |
| `data-science/` | NumPy/Pandas/Polars, SQL-Python integration, classical ML pipeline (sklearn to XGBoost), statistical foundations, experiment design | `01-NUMPY.md` — array model and broadcasting semantics | `query-languages/` for SQL side; `ai-engineering/` for deep learning |
| `languages/` | 16 languages surveyed across 10 axes (type systems, equality, null handling, error model, collections, closures). C# as home base throughout | `00-OVERVIEW.md` — type system taxonomy and language genealogy | `scripting/` for shell-tier languages; `computing/` for ecosystem context |
| `query-languages/` | SQL fundamentals through engine-specific dialects: T-SQL, PostgreSQL, MySQL, SQLite, KQL (Azure Monitor), DuckDB, analytical SQL (window functions, CTEs) | `00-OVERVIEW.md` — query language landscape | `data-science/` for Python-SQL integration; `computing/` for DB ops |
| `scripting/` | Shell-tier languages: Bash, PowerShell, Batch, Zsh, Fish, AWK, sed, Perl. Landscape, POSIX spectrum, 8-language × 12-topic cheatsheet | `00-OVERVIEW.md` — genealogy and POSIX spectrum | `os/` for kernel interfaces; `languages/` for where scripting fits |
| `os/` | Linux/Windows/macOS internals: kernel architecture, process/thread model, virtual memory, file systems, IPC, system calls, scheduling | `01-LINUX.md` — Linux kernel model and userland | `computing/` for containers-on-OS; `languages/` for runtime models |
| `cryptography/` | Symmetric (AES-GCM internals), asymmetric (RSA/ECC/OAEP), TLS 1.3 handshake, Signal X3DH/Double Ratchet, Noise/WireGuard, SNARKs/STARKs, post-quantum standards | `01-SYMMETRIC.md` — block ciphers and stream ciphers | `computing/25-SECURITY.md` for applied; `number-theory/` for math |
| `computer-architecture/` | ISA/microarchitecture split in depth: x86-64 (legacy compatibility and modern extensions), ARM (A-profile AArch64, Thumb-2), RISC-V (open ISA philosophy), pipelining (stages, hazards, forwarding, branch prediction), memory hierarchy (cache organization, MESI protocol, NUMA), superscalar/OOO execution, GPU architecture and the SIMT execution model, accelerators (TPUs, NPUs) | `01-ISA-FUNDAMENTALS.md` — RISC vs. CISC and the ISA/microarchitecture split | `electronics/` (Math & Physics) for device physics; `os/` for the software-hardware interface; `semiconductor-manufacturing/` for the physical layer |
| `machine-learning-theory/` | The theoretical foundations below the engineering of ML: PAC learning (Valiant's framework — sample complexity, efficient learnability), VC dimension and the Fundamental Theorem of Statistical Learning, Rademacher complexity and uniform convergence bounds, bias-variance decomposition, kernel methods and RKHS, neural tangent kernel (infinite-width NNs as kernel machines), double descent and the modern ML phenomenology, open problems | `01-PAC-LEARNING.md` — PAC learning establishes the formal vocabulary for all bounds that follow | `ai-engineering/` for practical ML engineering; `probability-statistics/` (Math & Physics) for the measure-theoretic substrate; `data-science/` for the applied pipeline |

---

## Paths

### General software engineering ramp
`os/` → `languages/` → `scripting/` → `computing/`
*Ground yourself in the runtime substrate, then the language landscape, then automation, then the full modern stack — this is the order competence compounds.*

### Data and ML engineering
`query-languages/` → `data-science/` → `ai-engineering/`
*Start with the query mental model you already own (SQL), extend it into the Python data stack, then into LLM-era engineering — each step has a natural on-ramp from the previous.*

### Applied security track
`cryptography/` → `computing/25-SECURITY.md` → `ai-engineering/`
*Cryptographic primitives first, then how they compose into production security posture, then adversarial ML and model supply-chain threats — the modern threat surface spans all three.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Mathematics & Physics | `information-theory/` underpins compression, entropy, and channel capacity — directly relevant to LLM tokenization and coding theory. `signal-processing/` sits beneath audio/image ML pipelines. `number-theory/` and `abstract-algebra/` are the mathematical substrate for everything in `cryptography/`. |
| Engineering | `semiconductor-manufacturing/` is the physical layer that computing runs on — Moore's Law economics, lithography, CMOS logic. `telecommunications/` explains the network substrate that distributed systems assume. `formal-methods/` connects type theory (from `languages/`) to software verification. |
| Mathematics & Physics → Quantum | `quantum-computing/` is the successor architecture to classical computing; `cryptography/` post-quantum track is the direct response. |
