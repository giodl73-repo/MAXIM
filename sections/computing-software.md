# Computing & Software

20 directories · The full modern software engineering stack — from bare metal to the human-interaction layer

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
 │  cryptography/  ·  symmetric · asymmetric · TLS 1.3 · Signal protocol       │
 │                 ·  zero-knowledge proofs · post-quantum (ML-KEM/SLH-DSA)    │
 └─────────────────────────────────────────────────────────────────────────────┘

 HUMAN-INTERACTION LAYER  (the top of the stack — where systems meet people)
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │  human-computer-interaction/  ·  design↔evaluate loop · interaction models  │
 │       ·  I/O modalities · usability evaluation · research methods · IA/viz  │
 │       ·  accessibility · CSCW · emerging interfaces · practice & ethics     │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| [`computing/`](../computing/00-SENTINEL-THESIS.md) | Modern engineering stack end-to-end: package managers, containers, Kubernetes, CI/CD, cloud architecture, distributed systems, observability (OTel/Prometheus/Grafana), security hardening | [`01-PACKAGE.md`](../computing/01-PACKAGE.md) — package ecosystem taxonomy | `os/` for runtime substrate; `ai-engineering/` for ML infra patterns |
| [`ai-engineering/`](../ai-engineering/00-OVERVIEW.md) | LLM architecture (Transformer internals, tokenization, attention), RAG pipelines, fine-tuning, RLHF, alignment, major model families, eval harnesses | [`01-LLM-CONCEPTS.md`](../ai-engineering/01-LLM-CONCEPTS.md) — tokens through model families | `data-science/` for ML pipeline; `computing/` for serving infra |
| [`data-science/`](../data-science/01-NUMPY.md) | NumPy/Pandas/Polars, SQL-Python integration, classical ML pipeline (sklearn to XGBoost), statistical foundations, experiment design | [`01-NUMPY.md`](../data-science/01-NUMPY.md) — array model and broadcasting semantics | `query-languages/` for SQL side; `ai-engineering/` for deep learning |
| [`languages/`](../languages/00-OVERVIEW.md) | 16 languages surveyed across 10 axes (type systems, equality, null handling, error model, collections, closures). C# as home base throughout | [`00-OVERVIEW.md`](../languages/00-OVERVIEW.md) — type system taxonomy and language genealogy | `scripting/` for shell-tier languages; `computing/` for ecosystem context |
| [`query-languages/`](../query-languages/00-OVERVIEW.md) | SQL fundamentals through engine-specific dialects: T-SQL, PostgreSQL, MySQL, SQLite, KQL (Azure Monitor), DuckDB, analytical SQL (window functions, CTEs) | [`00-OVERVIEW.md`](../query-languages/00-OVERVIEW.md) — query language landscape | `data-science/` for Python-SQL integration; `computing/` for DB ops |
| [`scripting/`](../scripting/00-OVERVIEW.md) | Shell-tier languages: Bash, PowerShell, Batch, Zsh, Fish, AWK, sed, Perl. Landscape, POSIX spectrum, 8-language × 12-topic cheatsheet | [`00-OVERVIEW.md`](../scripting/00-OVERVIEW.md) — genealogy and POSIX spectrum | `os/` for kernel interfaces; `languages/` for where scripting fits |
| [`os/`](../os/00-OVERVIEW.md) | Linux/Windows/macOS internals: kernel architecture, process/thread model, virtual memory, file systems, IPC, system calls, scheduling | [`01-CHEATSHEET.md`](../os/01-CHEATSHEET.md) — Linux kernel model and userland | `computing/` for containers-on-OS; `languages/` for runtime models |
| [`cryptography/`](../cryptography/00-OVERVIEW.md) | Symmetric (AES-GCM internals), asymmetric (RSA/ECC/OAEP), TLS 1.3 handshake, Signal X3DH/Double Ratchet, Noise/WireGuard, SNARKs/STARKs, post-quantum standards | [`01-SYMMETRIC.md`](../cryptography/01-SYMMETRIC.md) — block ciphers and stream ciphers | `computing/25-SECURITY.md` for applied; `number-theory/` for math |
| [`computer-architecture/`](../computer-architecture/00-OVERVIEW.md) | ISA/microarchitecture split in depth: x86-64 (legacy compatibility and modern extensions), ARM (A-profile AArch64, Thumb-2), RISC-V (open ISA philosophy), pipelining (stages, hazards, forwarding, branch prediction), memory hierarchy (cache organization, MESI protocol, NUMA), superscalar/OOO execution, GPU architecture and the SIMT execution model, accelerators (TPUs, NPUs) | [`01-ISA-FUNDAMENTALS.md`](../computer-architecture/01-ISA-FUNDAMENTALS.md) — RISC vs. CISC and the ISA/microarchitecture split | `electronics/` (Math & Physics) for device physics; `os/` for the software-hardware interface; `semiconductor-manufacturing/` for the physical layer |
| [`machine-learning-theory/`](../machine-learning-theory/00-OVERVIEW.md) | The theoretical foundations below the engineering of ML: PAC learning (Valiant's framework — sample complexity, efficient learnability), VC dimension and the Fundamental Theorem of Statistical Learning, Rademacher complexity and uniform convergence bounds, bias-variance decomposition, kernel methods and RKHS, neural tangent kernel (infinite-width NNs as kernel machines), double descent and the modern ML phenomenology, open problems | [`01-PAC-LEARNING.md`](../machine-learning-theory/01-PAC-LEARNING.md) — PAC learning establishes the formal vocabulary for all bounds that follow | `ai-engineering/` for practical ML engineering; `probability-statistics/` (Math & Physics) for the measure-theoretic substrate; `data-science/` for the applied pipeline |
| [`networking/`](../networking/00-OVERVIEW.md) | The layered network model end to end: link layer (Ethernet, MAC, VLANs, ARP), IP and routing (IPv4/IPv6, CIDR, BGP, OSPF), transport (TCP state machine, UDP, QUIC), congestion control (Reno/CUBIC/BBR, bufferbloat), DNS, TLS 1.3, NAT and firewalls, load balancing and CDNs, datacenter fabrics (leaf-spine, VXLAN, RDMA) | [`01-LINK-LAYER.md`](../networking/01-LINK-LAYER.md) — frames, MAC, and switching | `distributed-systems/` for what runs on top; `telecommunications/` (Math & Physics) for the physical layer; `cryptography/` for TLS internals |
| [`database-systems/`](../database-systems/00-OVERVIEW.md) | Database engine internals below the SQL surface: storage engines (B-tree vs LSM, buffer pool, write/read/space amplification), indexing, cost-based query optimization and join algorithms, transactions and MVCC, the four isolation levels and the anomalies each does and does not prevent, WAL and ARIES recovery, replication, sharding and 2PC, distributed/NewSQL systems | [`01-STORAGE-ENGINES.md`](../database-systems/01-STORAGE-ENGINES.md) — B-tree vs LSM-tree and the amplification tradeoffs | `query-languages/` for the SQL surface; `distributed-systems/` for consensus and CAP |
| [`graph-algorithms/`](../graph-algorithms/00-OVERVIEW.md) | Combinatorial graph algorithms with exact preconditions and bounds: representations, traversal (BFS/DFS, topological sort, components), shortest paths (Dijkstra, Bellman-Ford, Floyd-Warshall, A*), minimum spanning trees (Prim/Kruskal, union-find), strong connectivity (Tarjan/Kosaraju, 2-SAT), max-flow/min-cut and bipartite matching, NP-hard graph problems and approximation, spectral methods (Laplacian, PageRank), planarity | [`02-TRAVERSAL.md`](../graph-algorithms/02-TRAVERSAL.md) — BFS/DFS as the substrate for everything | `computing/` for the broader algorithms survey; `operations-research/` (Math & Physics) for the LP/flow view |
| [`algorithms/`](../algorithms/00-OVERVIEW.md) | General algorithms and data structures: asymptotic analysis and recurrences (Master theorem, amortized), sorting and searching, divide-and-conquer, dynamic programming, greedy methods, core data structures (heaps, balanced BSTs, hash tables, Fenwick/segment trees), union-find, string algorithms (KMP, Rabin-Karp, suffix structures), and P/NP/approximation | [`01-ANALYSIS.md`](../algorithms/01-ANALYSIS.md) — asymptotics, recurrences, amortized analysis | `graph-algorithms/` for graph-specific algorithms; `operations-research/` (Math & Physics) for optimization |
| [`compilers/`](../compilers/00-OVERVIEW.md) | Compiler construction in depth: lexing (regex→NFA→DFA), parsing (LL vs LR/LALR), semantic analysis and type checking, intermediate representation and SSA, dataflow analysis (lattices, dominators), optimization passes (GVN, LICM, inlining), register allocation (graph coloring vs linear scan), code generation and ABI, and runtime/garbage collection | [`04-INTERMEDIATE-REPRESENTATION.md`](../compilers/04-INTERMEDIATE-REPRESENTATION.md) — three-address code, CFG, and SSA | `programming-language-theory/` for type theory; `computing/22-COMPILERS.md` for the survey; `computer-architecture/` for codegen targets |
| [`computer-graphics/`](../computer-graphics/00-OVERVIEW.md) | Rendering from first principles: homogeneous transforms and projection, rasterization (z-buffer, perspective-correct interpolation), ray tracing and acceleration structures, shading and physically-based lighting (BRDFs, the rendering equation), texturing and sampling (mipmaps, antialiasing), the GPU pipeline and shaders (SIMT), geometry and meshes, color science, and real-time pipelines | [`01-TRANSFORMS-AND-PROJECTION.md`](../computer-graphics/01-TRANSFORMS-AND-PROJECTION.md) — homogeneous coordinates and the MVP transform | `colors/` (Arts) for color science; `mathematics/` for linear algebra; `computer-architecture/` for the GPU |
| [`computer-vision/`](../computer-vision/00-OVERVIEW.md) | Vision from image formation to deep models: the pinhole camera model and intrinsics/extrinsics, filtering and features (convolution, edges, Harris/SIFT/ORB), segmentation, classical recognition (HOG, bag-of-words, Viola-Jones), deep vision (CNNs, ResNet/ViT, transfer learning), multiview geometry (epipolar constraint, fundamental/essential matrices, RANSAC, triangulation), detection and tracking (R-CNN/YOLO, NMS, IoU/mAP, Kalman/optical flow), 3D and SLAM (structure-from-motion, bundle adjustment, NeRF), and applications | [`01-IMAGE-FORMATION.md`](../computer-vision/01-IMAGE-FORMATION.md) — the pinhole model and camera matrix | `ai-engineering/`/`machine-learning-theory/` for the ML core; `signal-processing/` for filtering; `computer-graphics/` for the inverse problem |
| [`embedded-systems/`](../embedded-systems/00-OVERVIEW.md) | Bare-metal and real-time systems: microcontrollers (MCU/MPU/SoC, ARM Cortex-M, the memory map), bare-metal programming (registers, GPIO, `volatile`, startup/linker), interrupts and timers (NVIC, ISR discipline, latency), RTOS (tasks, rate-monotonic vs EDF scheduling, priority inversion/inheritance), memory and DMA, peripherals and buses (UART/SPI/I2C/CAN/USB), hard/soft real-time constraints and WCET, power management (sleep modes, energy budgets), and the debug toolchain (JTAG/SWD, OTA) | [`04-RTOS.md`](../embedded-systems/04-RTOS.md) — schedulers, the RM utilization bound, and priority inversion | `computer-architecture/` for the CPU; `os/` for general scheduling; `robotics/` and `electronics/` for the physical layer |
| [`reinforcement-learning/`](../reinforcement-learning/00-OVERVIEW.md) | Learning to act from reward: MDP foundations and the Bellman equations, dynamic programming (policy/value iteration), Monte-Carlo and temporal-difference learning (TD(λ), the bias/variance trade-off), model-free control (SARSA vs Q-learning, exploration), function approximation (the deadly triad, DQN), policy gradients (the policy gradient theorem, REINFORCE, actor-critic, GAE), deep RL (TRPO/PPO, DDPG/TD3, SAC), model-based RL and planning (Dyna, MCTS, AlphaZero/MuZero), and frontiers (offline RL, multi-agent, RLHF) | [`01-MDP-FOUNDATIONS.md`](../reinforcement-learning/01-MDP-FOUNDATIONS.md) — MDPs, value functions, and the Bellman equations | `machine-learning-theory/` and `ai-engineering/` for the ML core; `operations-research/` for MDP/DP; `control-theory/` for optimal control |
| [`human-computer-interaction/`](../human-computer-interaction/00-OVERVIEW.md) | The interaction layer of the computing vertical: the design↔evaluate lifecycle plus cross-cutting concerns — interaction models (Norman's gulfs applied to computing), I/O modalities (Fitts/Hick applied), the design process, usability evaluation (heuristics vs measurement, SUS limits, the sample-size ceiling), HCI research methods, information architecture & interactive visualization, interactive accessibility (WCAG dated/bounded, the accessibility tree, conformance≠usability), sociotechnical/CSCW, emerging interfaces under an evidence bar, and professional practice & ethics (recognize-and-refuse dark patterns) | [`00-OVERVIEW.md`](../human-computer-interaction/00-OVERVIEW.md) — discipline map, ownership/defer matrix, and the design↔evaluate loop | `cognitive-science/` (Life Sciences) for the mechanisms/laws; `industrial-design/` (Arts) for the product-level action model; `statistics-applied/` for study statistics |

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
| Life Sciences & Arts | `human-computer-interaction/` bridges *out* of this section: it **defers** cognitive mechanisms and the psychophysical laws (Fitts, Hick, Miller, GOMS) to `cognitive-science/09-APPLIED-BRIDGE` (Life Sciences) and the product-level Norman action model / ergonomics to `industrial-design/` (Arts & Culture), while owning the design and evaluation of interactive computing systems. |
