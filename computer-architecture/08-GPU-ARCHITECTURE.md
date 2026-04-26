# GPU Architecture and SIMT Execution Model

## The Core Difference

A CPU is optimized for LATENCY — minimize the time to complete a single instruction stream. It has a few powerful cores, large caches, deep OOO pipelines. A GPU is optimized for THROUGHPUT — maximize the total amount of work done per second, even if individual threads take longer. It has thousands of simple cores, small caches, in-order execution, and relies on switching between many threads to hide memory latency.

```
+-----------------------------------------------------------------------+
|                    CPU vs GPU ARCHITECTURE                            |
|                                                                       |
|  CPU (Intel i9 / Apple M4)         GPU (NVIDIA H100 / AMD MI300X)     |
|  -------------------------         --------------------------------   |
|  8–32 cores (P+E)                  ~10,000 CUDA cores / shader procs  |
|  Large L1/L2/L3 caches            Small per-SM cache                  |
|  Deep OOO pipeline (600 ROB)       In-order execution                 |
|  Branch prediction                 Simple warp scheduler              |
|  Low latency (4 cycles for L1)     Hide latency via switching warps   |
|  Few, complex threads              Thousands of simple threads        |
|  Strong memory model (TSO)         Weak memory model                  |
|                                                                       |
|  BEST FOR:                         BEST FOR:                          |
|  Irregular computation             Regular, data-parallel computation |
|  Pointer chasing                   Arrays, matrices, tensors          |
|  Branchy code                      SIMD-friendly loops                |
|  OS tasks, databases               ML training, rendering, physics    |
|  Single-threaded apps              Batch processing                   |
+-----------------------------------------------------------------------+
```

---

## GPU Hardware Hierarchy (NVIDIA Terminology)

```
  FULL GPU (e.g., H100 SXM5):
  +──────────────────────────────────────────────────────────+
  |  GPU Die                                                 |
  |  144 SM (Streaming Multiprocessors) on H100              |
  |  HBM3 memory (80 GB at 3.35 TB/s)                        |
  |  L2 cache: 50 MB (shared)                                |
  +──────────────────────────────────────────────────────────+

  STREAMING MULTIPROCESSOR (SM):
  +──────────────────────────────────────────────────────────+
  |  SM (one of 144)                                         |
  |  128 CUDA cores (FP32)                                   |
  |  4 warp schedulers                                       |
  |  4 dispatch units                                        |
  |  Register file: 65,536 × 32-bit registers                |
  |  L1 cache / Shared Memory: 256 KB (configurable split)   |
  |  Tensor Core units                                       |
  +──────────────────────────────────────────────────────────+

  WARP: 32 threads executing the SAME instruction (SIMT)
  BLOCK: Up to 1024 threads sharing the SM's shared memory
  GRID: All blocks executing the same kernel

  HIERARCHY:
  Thread < Warp (32 threads) < Block < Grid

  OCCUPANCY: fraction of max warps active on an SM.
  High occupancy → more warps available to hide latency.
  Limited by: register usage, shared memory, block size.
```

---

## SIMT Execution Model

Single Instruction, Multiple Threads — GPU's version of SIMD.

### How SIMT Works

```
  SIMD (CPU AVX):
  One instruction, one vector register, N data elements.
  AVX-512: 1 instruction × 16 float32 = 16 operations.
  ALL 16 elements execute the same operation, unconditionally.

  SIMT (GPU):
  One instruction, N threads (warp = 32 threads).
  EACH THREAD has its own register file.
  ALL 32 threads execute the same instruction per cycle,
  but ON DIFFERENT DATA (each thread has its own index i).

  WARP EXECUTION:
  Warp scheduler picks a warp ready to execute.
  All 32 threads in the warp execute the same instruction.
  Each thread has its own registers, so results differ per thread.
  Next cycle: another warp may be scheduled (or same if still ready).

  THREAD INDEPENDENCE vs SIMD:
  SIMD: all elements share one PC, one set of control flow.
        Predication masks out inactive elements.
  SIMT: each thread has its own PC (conceptually).
        Thread divergence: some threads take if-branch, others else.
        The warp SERIALIZES both paths with masks.
```

### Thread Divergence

```
  BRANCHY CODE ON GPU:

  if (threadIdx.x < 16) {
      // Path A
  } else {
      // Path B
  }

  Warp 0: threads 0–31
  Threads 0–15: take if-branch (Path A)
  Threads 16–31: take else-branch (Path B)

  EXECUTION:
  Step 1: Execute Path A with threads 0–15 active, 16–31 masked off.
  Step 2: Execute Path B with threads 16–31 active, 0–15 masked off.
  Total: 2 passes × warp execution time.
  DIVERGENCE PENALTY: 2× slower than if all threads took same path.

  WORST CASE: 32 divergent paths = 32× slowdown.
  (In practice, GPUs handle some forms of reconvergence efficiently.)

  BEST PRACTICE: Minimize branching, ensure threads within a warp
  take the same path.
  Data layout often matters: sorting data so similar elements
  land in the same warp eliminates divergence.

  FULL WARP DIVERGENCE vs HALF-WARP:
  Older GPUs: a warp can only reconverge after the entire
  if-else block completes.
  Volta+ GPUs: independent thread scheduling — threads can
  diverge and reconverge more flexibly via barrier operations.
  But the fundamental penalty for divergence remains.
```

---

## GPU Memory Hierarchy

```
  THREAD LOCAL:
  Registers (65,536 per SM, 32-bit each)
  Fast: 0 cycles. Limited: runs out → "register spill" to local memory.
  Local memory (overflow from registers)
  Slow: same as global memory. Avoid register pressure!

  BLOCK SHARED:
  +───────────────────────────────────────+
  | SHARED MEMORY (~128KB per SM max)     |
  | = user-controlled L1-like memory      |
  | Accessible to ALL threads in a block  |
  | L1 speed: ~5 cycles latency           |
  | 128-bit wide: 4 × float32 in 1 cycle  |
  +───────────────────────────────────────+
  Explicit management: __shared__ in CUDA.
  Bank conflicts: shared memory is organized in 32 4-byte banks.
  If multiple threads in a warp access the same bank → serialized.
  Optimal: each thread accesses a different bank (stride-1 access).

  SM LOCAL:
  L1 cache: split from shared memory pool (configurable).
  Caches global memory accesses (read-only by default).

  GLOBAL (DEVICE MEMORY):
  +───────────────────────────────────────+
  | HBM3 (H100): 80 GB, 3.35 TB/s         |
  | GDDR7 (desktop): 16–24 GB, ~900 GB/s|
  | Latency: ~600–800 cycles              |
  +───────────────────────────────────────+
  Key optimization: MEMORY COALESCING.
  Threads in a warp should access CONTIGUOUS addresses.
  If warp requests addresses in one 128-byte cache line →
  1 memory transaction serves all 32 threads.
  If warp requests 32 scattered addresses → 32 transactions.
  32× bandwidth waste!

  CONSTANT MEMORY: 64 KB, cached, broadcast to whole warp.
  Ideal for: kernel parameters, lookup tables read by all threads.

  TEXTURE MEMORY: Cached with 2D spatial locality optimization.
  Ideal for: image processing, physics simulations with 2D access.
```

---

## Latency Hiding: Why Many Threads Are Necessary

```
  FUNDAMENTAL GPU STRATEGY: hide latency through thread switching.

  On a GPU, a DRAM access takes ~600 cycles.
  If a warp stalls on memory, the warp scheduler switches to
  another ready warp INSTANTLY (0 overhead).

  TO HIDE 600-CYCLE LATENCY AT 1 WARP/CYCLE THROUGHPUT:
  Need ~600 cycles / cycles per warp instruction = many warps.

  If each warp does 10 instructions per memory access:
  Need 600/10 = 60 warps to hide latency.
  At 32 threads per warp: 60 × 32 = 1920 threads.
  That is why CUDA kernels are typically launched with thousands of threads.

  OCCUPANCY vs PERFORMANCE:
  High occupancy (many active warps) = better latency hiding.
  BUT: more warps = more registers + shared memory used.
  If a kernel uses 64 registers per thread:
  Max threads = 65536 / 64 = 1024 threads = 32 warps.
  Low occupancy → gaps in warp scheduler → inefficiency.
  Must balance: fewer registers per thread = higher occupancy.

  NVCC --ptxas-options=-v shows register and smem usage.
  CUDA Occupancy Calculator: given register + smem use → max occupancy.
```

---

## Tensor Cores and Matrix Operations

Modern GPU accelerators include specialized hardware for matrix multiplication — the dominant operation in deep learning.

```
  TENSOR CORE (NVIDIA, Volta+):
  A hardware unit performing D = A×B + C for small matrices
  in a single "instruction."

  H100 Tensor Core (FP16):
  16×16×16 matmul in 1 cycle.
  = 16^3 × 2 = 8192 MADs per cycle per tensor core.
  H100 SXM5 has 528 tensor cores.
  Peak: 989 TFLOPS FP16 (with sparsity: 1979 TFLOPS)

  MATRIX FORMAT REQUIREMENTS:
  Input matrices must be in specific formats and alignments.
  CUDA WMMA API (Warp Matrix Multiply Accumulate):
  wmma::load_matrix_sync(A, ptr, stride, wmma::mem_row_major);
  wmma::mma_sync(D, A, B, C);

  CUBLAS / cuDNN exploit tensor cores automatically for appropriate sizes.

  TRANSFORMER ATTENTION = matrix multiplications.
  ML training = chains of matrix multiplications.
  This is why NVIDIA's GPU roadmap is essentially:
  "make tensor cores faster and larger every generation."

  INTEL AMX (Advanced Matrix Extensions, x86):
  Tiles: 2D register blocks (up to 1 KB each, e.g., 16×32 int8)
  TMUL instruction: tile matrix multiply.
  = Intel's tensor core equivalent, on the CPU.
  Useful for inference workloads that fit in CPU cache.

  ARM SME (Scalable Matrix Extension):
  ZA array register (up to 4 KB): 2D accumulator.
  Outer product instructions.
  Target: edge inference, mobile ML.
```

---

## Programming Models

```
  CUDA (NVIDIA-specific):
  __global__ void kernel(float* a, float* b, float* c, int N) {
      int i = blockIdx.x * blockDim.x + threadIdx.x;
      if (i < N) c[i] = a[i] + b[i];
  }
  // Launch: kernel<<<numBlocks, threadsPerBlock>>>(a, b, c, N);

  THREAD INDEXING:
  threadIdx.x: thread index within block (0 to blockDim.x-1)
  blockIdx.x:  block index within grid  (0 to gridDim.x-1)
  Global index: blockIdx.x * blockDim.x + threadIdx.x

  OPENCL (cross-vendor):
  Similar model; "work items" instead of threads.
  Less vendor optimization; more portable.
  Used for: AMD GPU compute, Intel GPU, FPGAs.

  SYCL (modern C++, cross-vendor):
  C++17/20 based; Intel's DPC++.
  Used in: Intel oneAPI, some AMD support.

  METAL (Apple Silicon):
  Apple's GPU API. Unified memory with CPU on M-series.
  Metal Shading Language (MSL): C++-like.
  No PCIe transfer needed: CPU and GPU share the same RAM.
  = Eliminates the biggest GPU bottleneck for many workloads.

  HLSL/GLSL/WGSL (graphics shaders):
  HLSL: DirectX (Windows, Xbox, Azure GPU nodes)
  GLSL: OpenGL/Vulkan
  WGSL: WebGPU (browser GPU compute)
  These are primarily graphics-oriented but compute shaders
  in these APIs power browser-side ML inference.
```

---

## GPU Cluster Scaling

```
  INTRA-NODE SCALING (multiple GPUs, one server):

  PCIe (baseline — all GPU servers):
    GPU ↔ CPU: PCIe 4.0 ×16 = 64 GB/s, PCIe 5.0 ×16 = 128 GB/s
    GPU ↔ GPU via PCIe switch: same bandwidth, shared
    Bottleneck: any operation that must move data through the CPU
                or PCIe bus (e.g., all-reduce in distributed training)

  NVLink (NVIDIA high-end):
    Direct GPU-to-GPU interconnect, bypasses PCIe for GPU↔GPU traffic
    NVLink 4.0 (H100 SXM5): 900 GB/s per GPU pair (bidirectional)
    vs PCIe 5.0: 7× higher bandwidth for GPU-to-GPU
    NVSwitch: a dedicated chip allowing any-to-any full-bandwidth
              GPU communication within a node (DGX H100: 8 GPUs, NVSwitch)
    Apple Silicon alternative: Unified Memory — CPU+GPU share same
              physical DRAM, PCIe bottleneck eliminated entirely

  INTER-NODE SCALING (multiple servers, a cluster):

  InfiniBand (dominant in HPC/AI clusters):
    HDR InfiniBand: 200 Gbps per port
    NDR InfiniBand: 400 Gbps per port (H100 cluster configs)
    RDMA: GPU-to-GPU across nodes without CPU involvement
    Fat-tree topology: non-blocking, every GPU pair gets full bandwidth

  RoCE (RDMA over Converged Ethernet):
    RDMA semantics over standard Ethernet infrastructure
    400GbE / 800GbE (emerging): approaches InfiniBand bandwidth
    Lower infrastructure cost; slightly higher latency
    Cloud providers often use RoCE internally (AWS EFA, GCP GNIC)

  VRAM CAPACITY PLANNING (universal — cloud or on-prem):

  Rule of thumb: FP16 model weights ≈ 2 bytes × parameter count
    7B parameter model  (FP16): ~14 GB — fits in single A100/H100
    13B parameter model (FP16): ~26 GB — fits in single A100/H100
    70B parameter model (FP16): ~140 GB — needs 2× H100 (80 GB each)
    GPT-3 175B         (FP16): ~350 GB — needs 5× A100 80GB minimum

  Quantization changes the math:
    INT8 quantization: ~1 byte/parameter → 70B fits in single 80 GB GPU
    INT4 quantization: ~0.5 bytes/param → 70B fits in 40 GB GPU
    BF16 training: must keep FP32 optimizer state → 4-6× weight size

  Tensor parallelism: split a single layer across N GPUs (needs NVLink)
  Pipeline parallelism: split model by layers across nodes (tolerates
    lower bandwidth; inter-node okay)

  THE PCIe BOTTLENECK:
  On a conventional server, data must travel:
    DRAM → CPU → PCIe → GPU VRAM (upload)
    GPU VRAM → PCIe → CPU → DRAM (download)
  PCIe 5.0 ×16 = 128 GB/s. GPU HBM3 = 3.35 TB/s.
  CPU-GPU transfer is 26× slower than GPU-internal bandwidth.
  Minimize host↔GPU transfers in GPU-bound workloads.
  CUDA pinned memory (page-locked) enables DMA and is faster
  than pageable transfers.

  CLOUD GPU INSTANCES (illustrative — all major clouds have similar):

  AWS:   p4d.24xlarge — 8× A100 80 GB, 400 Gbps EFA (RoCE)
         p5.48xlarge  — 8× H100 80 GB, 3200 Gbps EFA
  GCP:   a3-highgpu-8g — 8× H100 80 GB, 200 Gbps GNIC
  Azure: ND H100 v5   — 8× H100 80 GB, 400 Gbps InfiniBand
         ND A100 v4   — 8× A100 80 GB, 400 Gbps InfiniBand
         NCasT4_v3    — 4× T4 16 GB, inference-focused (cost-efficient)

  GRACE HOPPER (H200) — eliminates PCIe bottleneck at package level:
  ARM Neoverse CPU + H100 GPU on same package.
  HBM3e: 141 GB at 4.8 TB/s.
  CPU-GPU communication via NVLink-C2C (900 GB/s).
  Available on: AWS p6e, GCP A4, Azure ND H200 v5 (roadmap).
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is a warp? | 32 threads executing the same instruction simultaneously (SIMT) |
| What is thread divergence? | Threads in a warp taking different branches — GPU serializes both paths |
| Why launch thousands of threads? | To hide ~600-cycle DRAM latency via warp switching |
| What is memory coalescing? | 32 threads in a warp accessing contiguous addresses → 1 memory transaction |
| What is shared memory? | Fast, user-managed per-block cache (~128 KB per SM); must be explicitly used |
| What are tensor cores? | Specialized hardware for matrix multiply: 16×16×16 matmul per cycle |
| Why does Apple Silicon GPU differ? | Unified memory — CPU and GPU share the same physical RAM, no PCIe transfer |

---

## Common Confusion Points

**SIMT ≠ SIMD (exactly)**: CPU SIMD operates on one thread with a wide vector register. GPU SIMT operates on 32 independent threads sharing an instruction stream. SIMD: one PC, one set of data elements in a vector. SIMT: 32 PCs (conceptually) executing in lockstep. Thread divergence is possible in SIMT; in pure SIMD it is not.

**Shared memory ≠ L1 cache automatically**: Shared memory is a software-managed scratchpad. L1 cache is hardware-managed. On modern NVIDIA GPUs, they share the same physical SRAM but are configured as separate regions. You must explicitly use `__shared__` to put data in shared memory; otherwise the compiler uses L1 as a cache.

**High occupancy ≠ best performance always**: Sometimes a kernel with fewer but larger warps is faster because each warp needs more registers (fewer spills → less global memory traffic). High occupancy is a heuristic, not an absolute goal. Profile with actual workloads.

**GPU memory bandwidth ≠ CPU memory bandwidth**: H100 has 3.35 TB/s HBM3 bandwidth. A DDR5 server has ~100–400 GB/s DRAM bandwidth. This 10–30× difference is why GPUs can do so many FLOPS — the compute units are fed fast enough. The GPU's memory bandwidth is the primary bottleneck, not compute, for memory-bound workloads.

**CUDA cores ≠ full CPU cores**: A CUDA core is a single-precision FP32/INT32 compute element — not a full pipeline with branch prediction, OOO execution, large caches. Comparing "10,000 GPU cores" to "16 CPU cores" is misleading. The GPU cores are simple; the CPU cores are complex. This is the throughput vs latency tradeoff embodied in hardware.
