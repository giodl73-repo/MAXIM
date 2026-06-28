---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-DEBUG-AND-TOOLCHAIN.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:debug-and-toolchain
kind: guide
module: embedded-systems
section: embedded-systems
title: Debug and Toolchain - JTAG/SWD, Cross-Compilation, HAL, Testing, OTA
status: source-custody
source_custody: partial
current_path: embedded-systems/09-DEBUG-AND-TOOLCHAIN.md
canonical_path: embedded-systems/09-DEBUG-AND-TOOLCHAIN.md
backsource_ids: [proof-backfill:embedded-systems:09-debug-and-toolchain, git-history:embedded-systems:09-debug-and-toolchain]
concepts: [jtag, swd, cross-compilation, hal, testing, ota updates, bootloader]
root_concepts: [embedded toolchain]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Debug and Toolchain — JTAG/SWD, Cross-Compilation, HAL, Testing, OTA

## The Big Picture

The embedded development loop is fundamentally split across two machines: you
*build* on a powerful host and *run* on a resource-starved target, with a
hardware debug probe bridging them. There's no terminal on the MCU, no `gdb`
running locally, no package manager on the device. Everything — compiling,
flashing, debugging, testing, and field updates — is shaped by that host/target
split. This file is the production reality that decides whether firmware ships.

```
+-----------------------------------------------------------------------+
|                  THE HOST / TARGET DEVELOPMENT LOOP                   |
|                                                                       |
|  HOST (your PC)                          TARGET (the MCU board)       |
|  .-------------------------.             .------------------------.   |
|  | cross-compiler          |             | Cortex-M core          |   |
|  | arm-none-eabi-gcc       |  .elf/.bin  | flash + SRAM           |   |
|  | linker + linker script  |------------>| your firmware runs     |   |
|  | gdb (host side)         |             | (no OS, no shell)      |   |
|  '-----------.-------------'             '-----------.------------'   |
|              |                                       ^                |
|              |        .-------------------.          | SWD/JTAG       |
|              +------->|  DEBUG PROBE       |----------+ (2-5 wires)   |
|              gdb      |  ST-Link/J-Link/   |  flash, halt, step,      |
|              remote   |  CMSIS-DAP         |  read memory/registers   |
|                       '-------------------'                           |
+-----------------------------------------------------------------------+
```

**Read it left-to-right: two computers, one wire.** The compiler runs on the
host but emits code for a *different* architecture (cross-compilation). The
probe is the only window into the target — it flashes the binary and lets
host-side gdb halt and inspect a chip with no console of its own.

---

## Cross-Compilation — Building for a Machine You're Not On

You compile on x86-64 (or ARM Mac) and produce ARM Cortex-M machine code. The
toolchain is a *cross*-toolchain: it runs on the host but targets a different
ISA. The canonical one is GNU Arm Embedded (`arm-none-eabi-*`).

```
  ANATOMY OF THE TARGET TRIPLE: arm-none-eabi-gcc
  +----------------------------------------------------------+
  | arm   | target architecture (ARM)                        |
  | none  | no OS ("bare metal" -- no Linux/vendor kernel)   |
  | eabi  | Embedded Application Binary Interface            |
  +----------------------------------------------------------+
  Contrast: arm-linux-gnueabihf  = ARM + Linux + glibc (an MPU/SoC,
  not bare metal). The "none" is what says "there is no OS here."

  BUILD PIPELINE
  .c/.cpp ---compile---> .o ---link(+linker script)---> .elf
                                                          |
                              objcopy --> .bin / .hex (raw image to flash)
```

| Tool | Role |
|------|------|
| `arm-none-eabi-gcc` | Cross-compiler (host → Cortex-M) |
| `arm-none-eabi-ld` | Linker (places sections per linker script, `02`) |
| `arm-none-eabi-objcopy` | .elf → raw .bin/.hex for flashing |
| `arm-none-eabi-gdb` | Host-side debugger, talks to the probe |
| `newlib` / `newlib-nano` | Slimmed C library for tiny targets |
| CMSIS | ARM's standard core/peripheral definitions (`01`) |

The `.elf` carries debug symbols (used by gdb); the `.bin`/`.hex` is the raw
bytes that go to flash. You build flags for your exact core (`-mcpu=cortex-m4
-mfpu=fpv4-sp-d16 -mfloat-abi=hard`) so the compiler uses the FPU and the right
instruction set. (Bridge: the host/target split and target triples are the same
concept as cross-compiling Go or Rust for another platform — `GOOS`/`GOARCH`,
Rust target triples — just aimed at a chip with no OS.)

---

## JTAG and SWD — The Debug Window

With no console on the target, a hardware debug interface is how you flash code,
halt the core, single-step, set breakpoints, and read memory/registers — all
from host gdb. Two standards.

```
  JTAG (older, 4-5 wires)            SWD (ARM, 2 wires)
  ----------------------             ------------------
  TCK  test clock                    SWCLK  clock
  TMS  mode select                   SWDIO  bidirectional data
  TDI  data in                       (+ optional SWO trace out)
  TDO  data out
  (+ optional TRST)
  daisy-chains many chips            point-to-point, fewer pins
  industry-standard, universal       ARM's pin-efficient replacement
```

| Capability | JTAG | SWD |
|------------|------|-----|
| Wires | 4–5 | 2 (+1 for trace) |
| Flash the chip | Yes | Yes |
| Halt / step / breakpoint | Yes | Yes |
| Read/write memory + registers live | Yes | Yes |
| Multi-device daisy-chain | Yes | No (point-to-point) |
| Trace output (SWO/ITM) | Via extra pins | SWO single-wire |
| Dominant on Cortex-M | Supported | **Preferred** (pin-efficient) |

SWD is the Cortex-M default: two pins do everything JTAG does for a single chip.
Common probes: **ST-Link** (STMicro boards), **J-Link** (SEGGER, premium),
**CMSIS-DAP** (open standard, on many dev boards). They all expose a gdb-server
the host gdb connects to (`target remote :3333`), turning a chip with no OS into
something you can breakpoint like a local process.

### Printf-debugging without a UART: SWO/ITM and RTT

Since the MCU has no console, getting "print" output traditionally meant wiring
a UART. Two better paths over the debug link:

- **SWO + ITM**: the Cortex-M's Instrumentation Trace Macrocell streams
  `printf`-style data out the single SWO pin to the probe — no UART needed,
  minimal CPU cost.
- **SEGGER RTT**: a ring buffer in target RAM that the J-Link reads over SWD
  while the core runs — very fast, non-intrusive logging with no dedicated pin.

These replace the UART-console habit and don't perturb timing the way a blocking
UART `printf` (or semihosting) does — important when you're chasing a real-time
bug (`07`).

---

## The HAL — Taming Vendor Registers

Writing raw register code (`02`) is precise but verbose and non-portable across
vendors. A Hardware Abstraction Layer wraps the registers in typed functions so
application code reads at the level of "configure UART" rather than "set bits in
these four registers." It's the embedded analogue of a driver/SDK layer.

```
  THE ABSTRACTION LADDER (high -> low)
  +------------------------------------------------------------+
  | Application firmware                                       |
  +------------------------------------------------------------+
  | RTOS / middleware (FreeRTOS, lwIP, USB stack)              |
  +------------------------------------------------------------+
  | HAL  (vendor: STM32 HAL, nRF SDK; or Zephyr's device API)  |
  |   HAL_UART_Transmit(&huart1, buf, len, timeout);           |
  +------------------------------------------------------------+
  | CMSIS  (ARM-standard core + peripheral register structs)  |
  |   USART1->DR = byte;   NVIC_EnableIRQ(USART1_IRQn);        |
  +------------------------------------------------------------+
  | Registers / silicon  (the actual MMIO addresses)           |
  +------------------------------------------------------------+
```

| Layer | What it gives you | Cost |
|-------|-------------------|------|
| Bare registers (`02`) | Total control, smallest, fastest | Verbose, vendor-locked, error-prone |
| CMSIS | Portable core access, typed register structs | Still register-level |
| Vendor HAL | "Configure peripheral" API, portability within vendor | Larger, sometimes slow/heavy |
| RTOS HAL (Zephyr) | Cross-vendor device API + drivers | Bigger footprint |

The trade is **abstraction vs. control/size**. A vendor HAL accelerates bring-up
and is portable across that vendor's parts, but it can be heavyweight and
occasionally hides timing you need in a real-time path. Mature teams often mix:
HAL for non-critical setup, hand-written register code for the hot/real-time
path. (Bridge: same tension as ORM vs. raw SQL — convenience and portability
against control and predictability.)

---

## Testing Embedded Code — Without (Mostly) the Hardware

You can't unit-test on a coin-cell sensor with no console, and hardware-in-the-
loop is slow and scarce. The strategy is to push as much logic as possible into
*hardware-independent* code you test on the host, and reserve the target for
integration.

```
+-----------------------------------------------------------------------+
|                  THE EMBEDDED TEST PYRAMID                            |
|                                                                       |
|        /\        HIL: a few tests on real hardware                    |
|       /  \       (timing, peripherals, the actual chip)               |
|      /----\                                                           |
|     /      \     ON-TARGET: run test firmware on the board/           |
|    /        \    QEMU/Renode emulator (some integration)              |
|   /----------\                                                        |
|  /            \  HOST UNIT TESTS: pure logic compiled for the         |
| /              \ host, hardware mocked behind interfaces              |
| /--------------\  <- put MOST of your logic here                      |
+-----------------------------------------------------------------------+
```

| Technique | Where it runs | Catches |
|-----------|---------------|---------|
| Host unit tests | Your PC (logic compiled native) | Algorithms, state machines, parsers |
| Hardware mocking | Host (fake register layer) | Driver logic without the chip |
| Emulation (QEMU, **Renode**) | Host (simulated MCU + peripherals) | Integration, even multi-node, in CI |
| On-target tests | The board | Real peripheral + timing behavior |
| Hardware-in-the-loop (HIL) | Board + signal rigs | End-to-end, analog, timing margins |

The enabling discipline is the same one good systems engineers use everywhere:
**separate logic from I/O behind an interface.** A protocol parser that takes
bytes and returns messages is pure and host-testable; only the thin layer that
pulls bytes from the actual UART register touches hardware. Renode (and QEMU for
some cores) can even simulate a whole board — and a network of boards — in CI, so
integration tests run without a lab. This maps directly onto the test-pyramid and
dependency-inversion thinking from server engineering; embedded just makes the
"slow, scarce, real" tier *literally a physical board*.

---

## Bootloaders and OTA — Updating Firmware in the Field

A shipped device must be updatable without a debug probe — over UART, USB, BLE,
or the network. That's the job of a **bootloader**: a small, rarely-changed
program that runs first, can receive a new application image, write it to flash,
verify it, and jump to it. Getting this *atomic and recoverable* is critical: a
power loss mid-update must not brick the device.

```
+-----------------------------------------------------------------------+
|              FLASH LAYOUT FOR SAFE OTA (A/B / dual-bank)              |
|                                                                       |
|  .----------------.  bootloader: tiny, immutable, verifies + swaps    |
|  | BOOTLOADER     |  runs first; never updated OTA (or rarely)        |
|  |----------------|                                                   |
|  | SLOT A (active)|  current firmware -- running now                  |
|  |----------------|                                                   |
|  | SLOT B (spare) |  new image is written HERE while A runs           |
|  |----------------|                                                   |
|  | metadata/      |  version, CRC/signature, "boot which slot" flag   |
|  | rollback flag  |                                                   |
|  '----------------'                                                   |
|                                                                       |
|  UPDATE FLOW:                                                         |
|  1. download new image into SLOT B (A keeps running -> no downtime)   |
|  2. verify B's signature + CRC                                        |
|  3. set boot flag -> B; reset                                         |
|  4. bootloader validates B; if it fails to confirm healthy,           |
|     ROLL BACK to A. Power loss anytime = still a valid A or B.        |
+-----------------------------------------------------------------------+
```

| OTA requirement | Why it's non-negotiable |
|-----------------|-------------------------|
| **Atomic swap** (A/B slots) | Power loss mid-write must not leave a half-image |
| **Rollback** | A bad update must fall back to the last good image |
| **Integrity** (CRC) | Detect a corrupted download before booting it |
| **Authenticity** (signature) | Only run images signed by you (secure boot) |
| **Versioning / anti-rollback** | Prevent downgrade to a vulnerable old image |
| **Watchdog confirmation** | New image must prove it boots/runs before commit |

The A/B (dual-bank) scheme is the standard: write the new image to the inactive
slot while the active one keeps running (no downtime), verify it, then flip a
pointer. If the new image fails to confirm itself healthy within a watchdog
window (`08`), the bootloader rolls back. Combined with a *signature check*
(secure boot — only run images you signed), this is how a fleet of remote
devices updates safely. (Bridge: it's the embedded analogue of blue-green
deployment with automatic rollback — the same idea you know from cloud, applied
to flash with a power-loss adversary instead of a load balancer.)

> Cryptographic signing, key storage, and secure boot chains lean on
> `cryptography/`; the TrustZone-M / secure-element hardware that protects keys
> is the M23/M33 material from `01`. Here OTA is the *update mechanism* those
> secure those primitives protect.

---

## Common Confusion Points

### "Why can't I just run gcc and gdb on the device?"

There's no OS, no filesystem, kilobytes of RAM, and a different ISA than your
PC. You *cross-compile* on the host (a big machine) for the Cortex-M target, and
gdb runs on the host too — talking to the chip through a debug probe over
SWD/JTAG. The target only runs your firmware image; it has no toolchain.

### "JTAG vs SWD — which do I use?"

On Cortex-M, **SWD** by default: same debug/flash capability as JTAG over two
pins instead of four-plus. Use JTAG when you must daisy-chain multiple devices
or the part predates SWD. Both connect through a probe (ST-Link, J-Link,
CMSIS-DAP) to host gdb.

### "Should I use the vendor HAL or write registers directly?"

Both, by layer. HAL speeds bring-up and is portable within a vendor, but can be
heavy and may obscure timing. Register code is minimal and fully controlled but
verbose and vendor-locked. Common practice: HAL for non-critical init,
hand-written registers for the real-time hot path. It's the ORM-vs-raw-SQL
trade-off in silicon.

### "How do I test firmware without a pile of boards?"

Push logic into hardware-independent modules tested natively on your PC, mock
the register layer, and use an emulator (Renode/QEMU) for integration in CI.
Reserve real hardware for timing-sensitive and analog behavior. Most bugs are in
logic, and logic is host-testable.

### "How do I update devices in the field without bricking them?"

A bootloader with A/B (dual-bank) slots: write the new signed image to the spare
slot while the current one runs, verify integrity and authenticity, flip the
boot pointer, and roll back automatically if the new image doesn't confirm
healthy. Power loss at any point leaves a valid image. Never do an in-place
single-bank overwrite for field updates.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Build firmware for a Cortex-M | `arm-none-eabi-gcc` cross-toolchain |
| Turn an .elf into a flashable image | `objcopy` → .bin / .hex |
| Flash and debug a chip with no console | SWD probe (ST-Link/J-Link) + host gdb |
| Use minimal debug pins on Cortex-M | SWD (2 wires) over JTAG |
| Get printf without a UART | SWO/ITM trace or SEGGER RTT |
| Bring up a peripheral fast, portably | Vendor HAL |
| Squeeze size / control timing exactly | Hand-written register code (`02`) |
| Test most of the firmware logic | Host unit tests + mocked hardware |
| Run integration tests in CI without boards | Renode / QEMU emulation |
| Verify real timing and analog behavior | On-target / hardware-in-the-loop |
| Update firmware in the field safely | Bootloader + A/B slots + sign + rollback |
| Ensure only your firmware runs | Signature check / secure boot (`cryptography/`, M33) |
