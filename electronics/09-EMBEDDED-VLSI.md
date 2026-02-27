# 09 — Embedded Systems and VLSI Design

```
EMBEDDED / VLSI LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  EMBEDDED SYSTEMS                        VLSI DESIGN
  ─────────────────────────────────────   ─────────────────────────────────────
  Programming close to the metal           Designing the metal itself

  MCU/MPU + RTOS + peripherals       →    RTL description → synthesis →
  C/C++ with HAL or register-direct        place-and-route → tapeout → silicon

  Abstraction levels:                      Design levels:
  Application code                         Algorithm / architecture
  RTOS (FreeRTOS, Zephyr)                  RTL (SystemVerilog, VHDL)
  HAL / device drivers                     Gate-level netlist
  Peripheral registers                     Physical layout (GDSII)
  Interrupt vectors                        Foundry fabrication
  Bare metal / startup code

  BRIDGE TO SOFTWARE BACKGROUND:
  MCU bare-metal ≈ kernel development (no OS, direct hardware access)
  RTOS ≈ user-space OS with cooperative/preemptive scheduling
  VLSI flow ≈ compiler toolchain: RTL→netlist is "compile", P&R is "link"
  FPGA ≈ ASIC prototype: same RTL, reconfigurable fabric instead of fixed silicon
```

---

## Part 1: Embedded Systems

### MCU vs MPU — Core Distinction

```
  MCU (Microcontroller Unit)              MPU (Microprocessor Unit)
  ─────────────────────────────────────   ─────────────────────────────────────
  CPU + RAM + Flash + peripherals         CPU only — memory and peripherals
  all on ONE chip                         are external

  Self-contained                          Needs: external DRAM, Flash/eMMC,
  Boot from internal Flash                PMIC (power management), boot ROM
  No OS typically (or lightweight RTOS)   Runs Linux, RTOS, or bare-metal

  ARM Cortex-M series:                    ARM Cortex-A series:
    M0/M0+: ultra-low-power, IoT            A53/A55: efficiency cores (mobile)
    M4: FPU, DSP instructions, sensors      A72/A76/A78: performance cores
    M7: dual-issue, branch pred, TCM        A510/A715: Armv9, modern SoC
    M33/M55: TrustZone, Helium DSP         Apple M-series: custom Arm cores
    M85: Armv8.1-M, MVE vector engine     RISC-V: U74 (SiFive), CV72 (Andes)
                                          x86: Intel Atom for embedded

  Examples by use case:
  STM32F4 (M4):   sensor fusion, motor ctrl   Raspberry Pi (A72): Linux SBC
  ESP32 (Xtensa): WiFi/BLE IoT device         i.MX8 (A72+M4): automotive MCU
  RP2040 (M0+×2): maker boards, custom PIO    NVIDIA Jetson: GPU+A57 for AI
  nRF52840 (M4):  BLE mesh, Nordic SDK        BeagleBone (A8): industrial Linux
```

### Memory Hierarchy in Embedded

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  CPU REGISTERS         ~32 × 32-bit          0-cycle access             │
  │  Cortex-M: R0-R12, SP, LR, PC, PSR          inside CPU core            │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  TCM (Tightly Coupled Memory)     64KB–1MB   1-cycle                    │
  │  Cortex-M7+: ITCM/DTCM mapped    deterministic — use for ISRs          │
  │  directly, no cache uncertainty   and real-time control loops           │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  SRAM (on-chip)                   4KB–4MB    2-5 cycles                 │
  │  Variables, stack, heap           Fast, volatile                        │
  │  CCM (Core-Coupled Memory) on STM32: DMA cannot reach it                │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Flash (program storage, on-chip) 32KB–2MB   3-10 cycles (with cache)  │
  │  Non-volatile; .text and .rodata  ART Accelerator (STM32) = 0-wait     │
  │  Erase in pages (512B–128KB)      ~100K erase cycles lifetime           │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  External DRAM (SDRAM, PSRAM)     8MB–4GB    ~100 cycles                │
  │  Flexible Memory Controller (FMC) On MPU systems only                   │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  External Flash (QSPI, eMMC, SD)  MBs–TBs    very slow (µs+ erase)     │
  │  Firmware OTA storage             Not XiP (execute in place) unless QSPI│
  └─────────────────────────────────────────────────────────────────────────┘
```

### Bare-Metal Programming

The embedded boot sequence — what happens before `main()`:

```
  POWER-ON RESET
       │
       ▼
  RESET VECTOR (address 0x00000004 on Cortex-M)
  Vector table at start of Flash:
    [0]: initial stack pointer value
    [1]: Reset_Handler address  ← CPU jumps here
    [2]: NMI_Handler
    [3]: HardFault_Handler
    ...
    [n]: IRQn_Handler
       │
       ▼
  Reset_Handler (startup_stm32xxx.s or equivalent)
    1. Copy .data section from Flash to SRAM  (initialized globals)
    2. Zero-fill .bss section in SRAM         (zero-initialized globals)
    3. Initialize heap pointer (if using malloc)
    4. Configure FPU enable (if Cortex-M4/M7)
    5. Call SystemInit() → PLL setup, clock tree
    6. Call main()
       │
       ▼
  main()
```

Linker script memory regions (what the `.ld` file controls) — this is the embedded equivalent of the PE/ELF section table: .text maps to the code section (rx), .data to initialized data (copied from Flash to SRAM at startup, just as the PE loader copies initialized data from disk to memory), and .bss to the zero-initialized segment (not stored in the binary, zeroed at startup):

```
  MEMORY {
    FLASH (rx)  : ORIGIN = 0x08000000, LENGTH = 2048K
    SRAM (xrw)  : ORIGIN = 0x20000000, LENGTH = 192K
    DTCMRAM(xrw): ORIGIN = 0x20000000, LENGTH = 128K  /* Cortex-M7 */
  }
  SECTIONS {
    .text   → FLASH   /* code, constants, vector table */
    .data   → SRAM    /* initialized globals; LMA in Flash, VMA in SRAM */
    .bss    → SRAM    /* uninitialized globals, zero at startup */
    .stack  → SRAM    /* grows downward */
    .heap   → SRAM    /* grows upward; optional */
  }
  Bridge: LMA (Load Memory Address) = where it's stored (Flash)
          VMA (Virtual Memory Address) = where CPU expects it (SRAM)
          Startup code does the Flash→SRAM copy for .data
```

---

### RTOS Concepts

```
  RTOS CORE STRUCTURE
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  APPLICATION TASKS                                                       │
  │  Task A (priority 3)   Task B (priority 2)   Task C (priority 1)        │
  │  [Stack] [TCB]         [Stack] [TCB]         [Stack] [TCB]              │
  │                                                                          │
  │  TCB (Task Control Block): stack pointer, priority, state,              │
  │  task name, run-time stats, list links                                   │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  SCHEDULER                                                               │
  │  Preemptive priority: highest-priority ready task always runs           │
  │  Tick interrupt (e.g., 1 kHz = 1ms tick): drives time slicing           │
  │  Context switch: save registers to TCB stack, load next task's          │
  │  registers — Cortex-M uses PendSV exception for this                    │
  │  Context switch cost: ~100-300ns (Cortex-M4 at 168 MHz, FreeRTOS)      │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  IPC PRIMITIVES                                                          │
  │  Queue: thread-safe FIFO, blocks producer if full, consumer if empty    │
  │  Semaphore: counting or binary; counts available resources              │
  │  Mutex: binary + priority inheritance; prevents priority inversion      │
  │  Event flags: 32-bit flags, task waits for bit pattern                  │
  │  Stream buffer / message buffer (FreeRTOS 10+): lockless for 1P/1C     │
  └─────────────────────────────────────────────────────────────────────────┘
```

FreeRTOS critical API:

```c
  // Task creation
  xTaskCreate(vMyTask,          // function pointer
              "Task Name",       // debug name
              512,               // stack size in words (not bytes)
              pvParams,          // parameter passed to task
              tskIDLE_PRIORITY+2,// priority
              &xTaskHandle);     // handle for deletion/suspend

  // Delay (yields CPU, NOT busy-wait)
  vTaskDelay(pdMS_TO_TICKS(100));          // 100 ms delay
  vTaskDelayUntil(&xLastWakeTime, period); // periodic: drift-free

  // Queue
  xQueueSend(xQueue, &data, portMAX_DELAY);    // block until space
  xQueueReceive(xQueue, &data, portMAX_DELAY); // block until item

  // Mutex (always release in same task that acquired)
  xSemaphoreTake(xMutex, portMAX_DELAY);
  // ... critical section ...
  xSemaphoreGive(xMutex);
```

Priority inversion: low-priority task holds mutex needed by high-priority task;
medium-priority task preempts low-priority task → high-priority task starves.
Solution: priority inheritance mutex (FreeRTOS default mutex includes this).

Stack overflow detection: `configCHECK_FOR_STACK_OVERFLOW = 2` in FreeRTOS
fills stack with watermark pattern 0xA5A5A5A5; `vApplicationStackOverflowHook`
called if stack pointer exits bounds. Always size stack generously — stack
overflows are silent corruption bugs in bare-metal contexts.

---

### Peripheral Interfaces

```
  INTERFACE COMPARISON
  ┌──────────────┬────────────────┬──────────────┬───────────────────────────┐
  │ Interface    │ Wires          │ Speed        │ Notes                     │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ SPI          │ 4: SCLK,MOSI,  │ 1–100 MHz    │ Full-duplex; master       │
  │              │ MISO,CS        │              │ selects slave via CS pin  │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ I²C          │ 2: SDA, SCL    │ 100k/400k/   │ Multi-master; 7-bit addr; │
  │              │ (open-drain)   │ 1M/3.4MHz    │ ACK/NACK; clock stretch  │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ UART         │ 2: TX, RX      │ 9.6k–5Mbps   │ Async; start/stop bits;  │
  │              │ (+RTS/CTS opt) │              │ no clock; must match baud │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ CAN bus      │ 2: CAN_H/L     │ 1 Mbps       │ Differential; multi-node; │
  │              │ (differential) │ (CAN-FD 8M)  │ arbitration; auto. ACK   │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ USB 2.0 FS   │ D+/D- (diff)   │ 12 Mbps      │ Host/device; enumeration; │
  │              │ + VBUS + GND   │              │ protocol stack required   │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ USB 3.2      │ D+/D- + TX/RX  │ 10 Gbps      │ SuperSpeed; separate      │
  │              │ differential   │              │ SuperSpeed lanes           │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ I²S          │ SCK,WS,SD      │ to 100 MHz   │ Audio serial; word-select │
  │              │                │              │ sets L/R channel          │
  ├──────────────┼────────────────┼──────────────┼───────────────────────────┤
  │ SDIO/SD      │ CLK,CMD,D0-D3  │ 25–208 MHz   │ SD card, eMMC, WiFi module│
  └──────────────┴────────────────┴──────────────┴───────────────────────────┘
```

### Power Management

```
  MCU POWER STATES (STM32 as example — similar across MCUs)
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  RUN mode         CPU + all peripherals on        10–100 mA @ 3.3V      │
  │    ↓ sleep entry  WFI / WFE instruction                                  │
  │  SLEEP mode       CPU halted; peripherals + RAM on  5–50 mA             │
  │    ↓ stop entry   peripheral clocks off                                  │
  │  STOP mode        CPU + most clocks off; RAM retained  1–300 µA         │
  │    ↓ standby      SRAM off; RTC still on                                 │
  │  STANDBY mode     Almost everything off; RTC on       1–10 µA           │
  │    ↓ shutdown                                                            │
  │  SHUTDOWN mode    Only WKUP pin and tamper detection  ~100 nA            │
  └──────────────────────────────────────────────────────────────────────────┘

  Wakeup sources: external interrupt (EXTI), RTC alarm, UART activity,
  comparator event, USB detect, ADC watchdog threshold cross

  Energy calculation: E = ∫ P(t) dt
  Typical IoT duty cycle:  sleep 9.9s at 2µA + wake 100ms at 20mA
  Average I = (2µA × 9.9 + 20mA × 0.1) / 10 = 1.99µA + 200µA/10 = 21.99µA
  At 3V with 1000mAh battery: ~3V × 1Ah = 3 Wh / (3V × 21.99µA) ≈ 4.5 years
```

---

## Part 2: VLSI Design Flow

### The Complete Flow

```
  SPECIFICATION
  (performance, area, power, interface, process node)
         │
         ▼
  ARCHITECTURE DESIGN
  (datapath width, pipeline stages, memory hierarchy, ISA)
         │
         ▼
  RTL DESIGN  ──────────── testbench ───────┐
  SystemVerilog / VHDL                       │
  (logic behavior description)               ▼
         │                           RTL SIMULATION
         │                           (ModelSim, Questa, VCS)
         │                           Functional verification
         │                           Formal verification (JasperGold)
         ▼
  LOGIC SYNTHESIS  (Design Compiler, Yosys)
  RTL → gate-level netlist
  Technology mapping: logic → standard cells
  Timing constraints (.sdc file)
  Area / power / timing (APT) optimization
         │
         ▼
  GATE-LEVEL SIMULATION + STA
  Static Timing Analysis: check all setup/hold across all paths
  Gate-level simulation: confirm netlist matches RTL behavior
         │
         ▼
  PHYSICAL DESIGN (Place & Route)  (Cadence Innovus, Synopsys ICC2)
  ┌─────────────────────────────────────────────────────────┐
  │  Floorplanning: macro placement, I/O ring, power domain │
  │  Power planning: VDD/GND grid, IR drop analysis         │
  │  Placement: standard cells into rows                    │
  │  CTS: Clock Tree Synthesis — buffers to minimize skew   │
  │  Routing: global → detailed → DRC fix                   │
  │  Filler cells: fill empty rows (well continuity)        │
  └─────────────────────────────────────────────────────────┘
         │
         ▼
  SIGNOFF CHECKS
  DRC (Design Rule Check): minimum spacing, width, via rules
  LVS (Layout vs Schematic): layout connectivity matches netlist
  ERC (Electrical Rule Check): floating nodes, shorts
  IR drop / EM (electromigration) analysis
  Timing signoff: PrimeTime — corner analysis (worst-case: SS/0.9V/125°C)
         │
         ▼
  TAPEOUT → GDS II file to foundry
  Re-spin economics: a mask set at 5nm costs $25M–$30M and adds 3–6 months.
  Every bug caught before tapeout is free; every bug caught after costs millions.
  This is why verification (RTL sim, gate-level sim, formal, STA at all PVT
  corners) consumes 60–70% of the total design effort.
         │
         ▼
  FABRICATION (TSMC, Samsung, GlobalFoundries, Intel Foundry)
  ~3-6 months turnaround at advanced nodes
         │
         ▼
  SILICON BRING-UP
  Scan test, JTAG debug, ATE (Automated Test Equipment)
  Board bring-up, driver development
```

### RTL Design Patterns

```systemverilog
  // Combinational logic
  always_comb begin
    case (opcode)
      ADD:  result = a + b;
      SUB:  result = a - b;
      AND:  result = a & b;
      default: result = '0;
    endcase
  end

  // Sequential logic (registers)
  always_ff @(posedge clk or posedge rst) begin
    if (rst) q <= '0;
    else     q <= d;
  end

  // Pipeline register (adds latency, increases throughput)
  always_ff @(posedge clk) begin
    stage1_out <= stage1_in;   // register between stages
    stage2_out <= stage1_out;  // pipelined: result every cycle after fill
  end

  // FSM: one-hot encoding (preferred for synthesis timing)
  typedef enum logic [3:0] {
    IDLE  = 4'b0001,
    FETCH = 4'b0010,
    EXEC  = 4'b0100,
    WB    = 4'b1000
  } state_t;
  state_t state, next_state;
```

### Timing Analysis

```
  SETUP TIME CONSTRAINT
  ┌────────────────────────────────────────────────────────────────────────┐
  │  Clock period T ≥ t_clk_to_Q + t_combinational + t_setup              │
  │                                                                        │
  │  Clock edge                                  Next clock edge           │
  │       │                                           │                   │
  │       │  t_clk_to_Q    t_comb          t_setup    │                   │
  │       │◄────────────►◄───────────────►◄─────────►│                   │
  │       │                                           │                   │
  │       ▼                                           ▼                   │
  │  FF1 output        logic propagation         FF2 must be stable       │
  │                                                                        │
  │  Critical path: the combinational path with maximum propagation delay  │
  │  Clock frequency = 1/T_critical_path (after meeting all timing)        │
  │                                                                        │
  │  HOLD TIME CONSTRAINT (independent of frequency!)                      │
  │  t_clk_to_Q + t_comb_min ≥ t_hold                                     │
  │  Hold violation: data changes too fast → metastability at FF2          │
  │  Fix: add buffer/delay on data path (NOT by slowing clock)             │
  └────────────────────────────────────────────────────────────────────────┘

  CLOCK DOMAIN CROSSING (CDC)
  Two FFs driven by different clocks → metastability risk
  Fix: 2-flop synchronizer (for single-bit), gray-coded counter (for bus),
       asynchronous FIFO (for burst data)
  Never use a combinational mux between clock domains.

  PVT CORNERS in signoff:
  SS (Slow-Slow) / 0.9V / 125°C  → worst-case setup (slowest silicon)
  FF (Fast-Fast) / 1.1V / -40°C  → worst-case hold (fastest silicon)
  Typical: TT / 1.0V / 25°C      → nominal simulation
```

### FPGA vs ASIC

```
  FPGA (Field-Programmable Gate Array)    ASIC (Application-Specific IC)
  ─────────────────────────────────────   ─────────────────────────────────────
  Reconfigurable LUT-based fabric         Fixed silicon; custom design

  Architecture:                           Process:
    LUT4/6: n-input truth table           Full VLSI flow as above
    FF: flip-flop after each LUT          Tapeout cost: $5M–$100M+ NRE
    DSP48: hard multiply-accumulate       (mask set at 5nm: ~$30M)
    BRAM: dual-port 36Kb block RAM
    Routing: programmable interconnect    Performance/Power/Area (PPA):
                                          ~10× better than FPGA at same node
  Power: ~5–10× worse than ASIC
  Speed: ~5–10× slower than ASIC         Production cost: ~$1–$50/unit (volume)
  NRE cost: $0 (just buy FPGA)
  Unit cost: $10 (Spartan) – $10k (HBM)  Lead time: 3–6 months for tapeout

  Xilinx/AMD: Artix (low-cost) → Kintex (mid) → Virtex/Ultrascale+ (high)
  Intel: Cyclone → Arria → Stratix → Agilex (AI-enhanced)
  Microchip: PolarFire (RISC-V hard core)
  Lattice: iCE40 (ultra-low-power), ECP5, Nexus

  HLS (High-Level Synthesis):
  Vitis HLS (AMD/Xilinx), Catapult (Mentor), Stratus: C/C++ → RTL
  Tradeoff: faster design but worse PPA than hand-written RTL
  Useful for: DSP kernels, control algorithms, ML accelerators
```

### Physical Design Details

**Software-visible consequence of IR drop:** When all cores are active, current draw peaks and the resistive power grid causes IR drop — the voltage at transistor gates falls below nominal. Lower gate voltage means slower switching (reduced gate overdrive), which erodes timing margin. If IR drop exceeds the ~5% budget, the chip faces STA violations at those corners. This is why CPUs throttle frequency under heavy all-core load even when thermally within limits — the voltage regulator and power grid cannot maintain nominal VDD at peak current. The DVFS mechanism visible from software (frequency stepping down under load) is the direct consequence of this physical IR drop constraint.

```
  POWER GRID
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Metal 8 (top): wide VDD/GND straps (horizontal)                        │
  │  Metal 7: wide straps (vertical)                                        │
  │  ...                                                                     │
  │  Metal 3-4: intermediate routing                                        │
  │  Metal 1-2: signal routing + local power rails                          │
  │  Standard cell row: VDD rail at top, GND rail at bottom                 │
  │                                                                          │
  │  IR drop: ΔV = I·R_grid_path; budget typically < 5% of VDD             │
  │  EM: current density > limit → metal void over time (failure)           │
  └─────────────────────────────────────────────────────────────────────────┘

  CLOCK TREE SYNTHESIS (CTS) GOAL:
  All FF clock pins arrive at (nearly) same time
    → minimize skew: σ < 50 ps (typical goal)
    → balanced H-tree or fishbone topology
    → clock buffers (high drive strength, low jitter) inserted
  Clock gating: AND gate before clock enable → power saving (clock off = no FF toggling)
  ICG (Integrated Clock Gating cell): standard cell with latch + AND gate,
    avoids glitch on enable input

  FINSET TECHNOLOGY NODES (marketing names vs reality)
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Node name    Fin pitch    Gate pitch    Density (MTx/mm²)  Foundry  │
  │  "5nm"        27 nm        48 nm         ~171               TSMC N5  │
  │  "3nm"        21 nm        48 nm         ~292               TSMC N3E │
  │  "2nm"        ~18 nm       ~45 nm        ~350+              TSMC N2  │
  │  "7nm"        30 nm        57 nm         ~96                TSMC N7  │
  │                                                                       │
  │  Node names are marketing; actual gate length is ~2-3× smaller        │
  │  than node name implies. N3 gate length ≈ 12-15 nm.                  │
  │  Power density becomes the bottleneck — more transistors, more heat   │
  └──────────────────────────────────────────────────────────────────────┘

  CHIPLETS AND 3D:
  Monolithic: everything on one die (area yield drops exponentially)
  Chiplets: separate dies in same package (HBM + logic, AMD EPYC MCM)
  3D stacking: SRAM on top of logic (TSMC SoIC, Intel Foveros)
    → SRAM latency drops 3-5× vs off-die; bandwidth ~10 TB/s
  TSMC CoWoS (Chip on Wafer on Substrate): HBM + GPU in silicon interposer
    → H100: 814mm² die + 6× HBM3 = 3.35 TB/s bandwidth
```

---

## Decision Cheat Sheet

| You need to... | Use / Know |
|----------------|-----------|
| Run on battery IoT device, simple sensor | ARM Cortex-M0+, FreeRTOS, deep sleep |
| WiFi/BLE connectivity + compute | ESP32 (Xtensa + 2.4GHz radio) |
| Real-time control (motor, servo, hard deadlines) | Cortex-M4/M7, FreeRTOS, bare-metal ISR |
| Run Linux on embedded | Cortex-A + Yocto or buildroot |
| Industrial networking | CAN bus (automotive), Modbus/EtherCAT (factory) |
| Prototype ASIC logic | FPGA + SystemVerilog/VHDL |
| Audio data between chips | I²S |
| Low-speed sensor (temp, IMU, RTC) | I²C |
| High-speed sensor (ADC, display, Flash) | SPI |
| Debug output / terminal | UART |
| Implement your own CPU or accelerator | ASIC flow (RTL→tapeout) |
| Algorithm→hardware with less RTL work | HLS (Vitis/Catapult) |
| Understand why VLSI is at 3nm/2nm | FinFET scaling, chiplets section |
| Understand Apple/AMD chip architecture | VLSI flow + microarch sections |
| Embedded secure boot / firmware security | Cortex-M33 TrustZone, secure element |

---

## Common Confusion Points

**MCU "MHz" vs real throughput — they're not the same thing.**
A Cortex-M4 at 168 MHz can do 210 DMIPS (Dhrystone MIPS) — more than 1 instruction
per clock because of single-cycle multiply, SIMD DSP instructions. But Flash wait
states, instruction cache misses, and bus contention often mean effective throughput
is 30-60% of peak. Benchmark on target hardware; don't trust MHz alone.

**Stack vs heap in embedded — both can overflow silently.**
Heap fragmentation in long-running MCU systems causes hard-to-reproduce crashes.
Many embedded systems avoid `malloc` entirely; use static allocation or FreeRTOS
memory pool allocators. Stack overflows are similarly silent — the CPU just writes
into whatever is below the stack (usually .bss or another task's stack). Size stacks
with watermark analysis, not guesswork.

**FPGA "MHz" is after P&R, not from RTL.**
Your RTL might describe logic that the synthesizer can only implement at 200 MHz
at that process node, even if you constrain to 500 MHz. The synthesis/P&R tools
will warn about timing violations. The constraint file (.sdc) expresses your intent;
the tool decides if it's achievable.

**RTL does not describe time-sequential steps — it describes hardware.**
`always_ff @(posedge clk)` means "this logic is implemented as registers and
combinational logic between them." Writing `always_ff @(posedge clk) begin a = b + c; d = a * e; end`
does NOT mean a is computed first then d. Both assignments happen simultaneously
on the same clock edge (use `<=` non-blocking for FF, `=` in `always_comb` only).

**Setup vs hold — they require different fixes.**
Setup violation (timing): critical path too slow → pipeline, add registers, reduce
combinational depth, or lower clock frequency. Hold violation: data arrives too fast
at the receiving FF → add buffers on the data path. Hold violations cannot be fixed
by slowing the clock (in fact faster clock → more margin for hold on short paths).

**FPGA LUT capacity ≠ ASIC gate count.**
"50K LUT4 FPGA" is roughly equivalent to ~500K NAND2 gates in ASIC — FPGA fabric
has ~10× overhead. An M1 chip has 16B transistors (~4B gates). An FPGA of equivalent
gate count would be the size of a server and cost thousands of dollars.
