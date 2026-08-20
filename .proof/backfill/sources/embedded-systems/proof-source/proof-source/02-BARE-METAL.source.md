---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-BARE-METAL.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:bare-metal
kind: guide
module: embedded-systems
section: embedded-systems
title: Bare Metal - Registers, GPIO, volatile, Startup and Linker
status: source-custody
source_custody: partial
current_path: embedded-systems/02-BARE-METAL.md
canonical_path: embedded-systems/02-BARE-METAL.md
backsource_ids: [proof-backfill:embedded-systems:02-bare-metal, git-history:embedded-systems:02-bare-metal]
concepts: [bare metal, memory-mapped io, volatile, gpio, startup code, linker script]
root_concepts: [bare metal]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Bare Metal — Registers, GPIO, volatile, Startup and Linker

## The Big Picture

"Bare metal" means there is no operating system between your code and the
silicon. You are the OS. From the reset vector to the control loop, every
instruction is yours. There is no `printf` unless you wrote the UART driver,
no scheduler, no heap unless you provided one. The path below is the entire
life of a bare-metal program — and every box is code you (or your startup
file) authored.

```
+-----------------------------------------------------------------------+
|                  LIFE OF A BARE-METAL PROGRAM                         |
|                                                                       |
|  POWER ON / RESET                                                     |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | 1. Hardware loads SP from vector[0], PC from vector[1]      |      |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | 2. Reset_Handler (startup.s / startup.c)                    |      |
|  |    - copy .data  flash -> SRAM                              |      |
|  |    - zero .bss                                              |      |
|  |    - set clocks (PLL), enable FPU if present                |      |
|  |    - call __libc_init / C++ static ctors                    |      |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | 3. main()                                                   |      |
|  |    - init peripherals (write registers)                     |      |
|  |    - for(;;){ poll; compute; act; }   <- super-loop         |      |
|  |    - interrupts fire ON TOP of this                         |      |
|  '------------------------------------------------------------'       |
+-----------------------------------------------------------------------+
```

**Read top-down: this is time.** Nothing runs before the reset handler sets up
memory. `main()` never returns (returning from `main` on bare metal is a bug —
there's nowhere to go). Interrupts (`03`) preempt the super-loop asynchronously.

---

## Memory-Mapped I/O — Hardware Is an Address

The foundational bare-metal idea: peripheral control registers are memory
addresses. To turn on an LED you do not call a function — you *write a value to
an address* and a transistor switches. The CPU's normal load/store instructions
talk to hardware.

```
  C STATEMENT                          WHAT THE SILICON DOES
  -----------                          ---------------------
  *(uint32_t*)0x40020014 = 0x20;       Bus write to 0x40020014.
                                       That address decodes to GPIOA's
                                       output-data register. Bit 5 -> 1.
                                       The pin's drive transistor turns on.
                                       The LED lights. ~Nanoseconds later.

  uint32_t s = *(uint32_t*)0x40020010; Bus read of GPIOA input-data reg.
                                       Returns live pin states as bits.
```

You almost never use raw addresses. Vendors ship a CMSIS header that defines
typed structs overlaid on those addresses:

```c
// From the vendor's stm32f4xx.h (conceptually):
typedef struct {
    volatile uint32_t MODER;    // 0x00 mode register
    volatile uint32_t OTYPER;   // 0x04
    volatile uint32_t OSPEEDR;  // 0x08
    volatile uint32_t PUPDR;    // 0x0C
    volatile uint32_t IDR;      // 0x10 input data
    volatile uint32_t ODR;      // 0x14 output data
    volatile uint32_t BSRR;     // 0x18 bit set/reset
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef*)0x40020000)

GPIOA->ODR |= (1 << 5);   // set PA5 high -- readable, type-checked MMIO
```

The struct's field offsets line up with the hardware register offsets; the
base pointer is the peripheral's address. This is the entire mechanism behind
every HAL — typed access to fixed addresses.

### Old world → MMIO bridge

```
  You know...                          Bare metal...
  ----------                           ------------
  WriteFile(handle, buf, ...)          *REG = value;  (the "syscall" is a store)
  Driver mediates hardware access      YOUR code IS the driver
  Port I/O (in/out on x86)             Memory-mapped: just loads/stores
  Device register via /dev/mem         Direct: there is no kernel to ask
```

---

## `volatile` — The Most Important Keyword in Embedded

The optimizing compiler assumes memory only changes when *your code* changes
it. Hardware registers violate that assumption: an input register changes
because a pin moved; a status flag clears itself when read. Without `volatile`,
the compiler will "optimize away" reads and writes that are load-bearing.

```
  WITHOUT volatile                     WITH volatile
  ----------------                     -------------
  uint32_t *r = (uint32_t*)0x40020010; volatile uint32_t *r = ...;

  while ((*r & FLAG) == 0) {}          while ((*r & FLAG) == 0) {}

  Compiler: "*r never changes in       Compiler: "*r is volatile -- I must
  this loop, so read it ONCE."         re-read it from the address EVERY
  -> reads once, loops FOREVER on      iteration."
     the stale value. DEADLOCK.        -> reads hardware each pass. Works.
```

| Situation | volatile? | Why |
|-----------|-----------|-----|
| Any MMIO register pointer | **Yes** | Hardware changes it; reads/writes have side effects |
| Variable shared with an ISR | **Yes** | ISR mutates it asynchronously |
| Buffer filled by DMA | **Yes** | DMA engine writes it, CPU didn't |
| Plain local computation | No | Pure CPU state, compiler reasoning is valid |

**Critical nuance for a systems peer**: `volatile` guarantees the access *is
not elided and is not reordered relative to other volatile accesses*. It does
**not** provide atomicity, and it does **not** provide cross-core memory
ordering. A `volatile` 32-bit write on a 32-bit core is atomic by virtue of
being a single aligned store, but `flag++` on a volatile is read-modify-write —
three accesses, interruptible. For ISR-shared counters you still need a
critical section or an atomic. `volatile` is about *visibility*, not
*synchronization*. (Bridge: it is the embedded cousin of C#'s `volatile` /
memory-barrier semantics, but even weaker — no happens-before across threads.)

---

## GPIO — The Hello World of Bare Metal

General-Purpose I/O is the simplest peripheral and the template for all
register programming. Configuring one pin touches several registers.

```
+-----------------------------------------------------------------------+
|              BLINKING AN LED ON PA5 (register sequence)               |
|                                                                       |
|  1. ENABLE THE CLOCK to GPIOA                                         |
|     RCC->AHB1ENR |= (1 << 0);   // ungate GPIOA's clock               |
|     (A peripheral with no clock is DEAD -- writes silently no-op.)    |
|                                                                       |
|  2. SET PIN MODE to output                                            |
|     GPIOA->MODER &= ~(3 << (5*2));  // clear 2 mode bits for pin 5    |
|     GPIOA->MODER |=  (1 << (5*2));  // 01 = general purpose output    |
|                                                                       |
|  3. DRIVE THE PIN                                                     |
|     GPIOA->ODR |=  (1 << 5);   // high  -> LED on                     |
|     GPIOA->ODR &= ~(1 << 5);   // low   -> LED off                    |
|     -- or atomically via the set/reset register --                    |
|     GPIOA->BSRR = (1 << 5);        // atomic SET pin 5                |
|     GPIOA->BSRR = (1 << (5+16));   // atomic RESET pin 5              |
+-----------------------------------------------------------------------+
```

Two register idioms worth internalizing:

- **Read-modify-write** (`REG |= bit`) is *not atomic* — it is load, OR, store.
  If an ISR also touches the same register between the load and store, you lose
  the ISR's write. That is the classic GPIO race.
- **Set/reset registers** (`BSRR`) exist precisely to dodge that race: writing
  a 1 to a "set" bit raises that pin and writing to the "reset" half lowers it,
  in a *single store* that touches only the bits you name. No read, no race.

```
  GPIO pin drive modes (configured via OTYPER/PUPDR):
  +----------------+---------------------------------------------+
  | push-pull      | actively drives HIGH and LOW. Normal output |
  | open-drain     | drives LOW only; HIGH = released (needs     |
  |                | a pull-up). Required for I2C, shared lines  |
  | input + pullup | reads pin, internal resistor to VCC         |
  | input + pulldn | reads pin, internal resistor to GND         |
  | analog         | disconnects digital buffer (for ADC pins)   |
  +----------------+---------------------------------------------+
```

> The electrical reality of push-pull vs open-drain, pull-up sizing, and signal
> integrity belongs to `electronics/`. Here we care which *register bits* select
> them.

---

## Startup Code and the C Runtime — What Runs Before main()

`main()` assumes a working C environment: initialized globals, zeroed
statics, a stack, maybe a heap. On a desktop the OS loader provides this. On
bare metal, **the startup code is your loader**, and you ship it.

```
  RESET_HANDLER responsibilities (the "crt0" for MCUs)
  +----------------------------------------------------------+
  | 1. Set up the stack pointer (HW already loaded vector[0])|
  | 2. Copy .data: initialized globals from FLASH to SRAM    |
  |       for (s=_sdata; s<_edata;) *s++ = *flashsrc++;      |
  | 3. Zero .bss: uninitialized globals                      |
  |       for (b=_sbss; b<_ebss;) *b++ = 0;                  |
  | 4. (optional) configure clocks / PLL  SystemInit()       |
  | 5. (optional) enable FPU (CPACR), enable caches (M7)     |
  | 6. Call C++ static constructors (__libc_init_array)      |
  | 7. Branch to main()                                      |
  | 8. If main returns: spin in a while(1) trap              |
  +----------------------------------------------------------+
```

Why `.data` must be copied: an initialized global like `int x = 42;` needs the
value 42 to exist *somewhere non-volatile* (flash) and a *writable* home
(SRAM). The startup loop copies the flash-stored initializer into the SRAM
variable. `.bss` (zero-initialized globals) needs no flash storage — startup
just clears the SRAM region, saving flash.

### The vector table

The vector table is an array of addresses at the start of flash. Entry 0 is the
initial stack pointer (not code — a value); the rest are function pointers to
exception/interrupt handlers.

```
  Flash @ 0x00000000:
  [0]  0x20020000   <- initial Main Stack Pointer (top of SRAM)
  [1]  Reset_Handler
  [2]  NMI_Handler
  [3]  HardFault_Handler
  [4]  MemManage_Handler
  ...
  [16+]  IRQ0_Handler, IRQ1_Handler, ...  (peripheral interrupts)
```

The hardware *literally fetches* [0] into SP and [1] into PC on reset — no code
runs to make that happen. This is why a corrupt vector table bricks boot.

---

## The Linker Script — Placing Code and Data in the Map

The linker script tells the toolchain where each section goes in the MCU's
physical memory map (`01`). On a desktop you never see this; the OS and default
linker script handle it. On bare metal it is load-bearing and you edit it.

```
  MEMORY {
    FLASH (rx)  : ORIGIN = 0x08000000, LENGTH = 512K
    RAM   (rwx) : ORIGIN = 0x20000000, LENGTH = 128K
  }

  SECTIONS {
    .isr_vector : { *(.isr_vector) } > FLASH   <- MUST be first
    .text       : { *(.text*) }       > FLASH   <- code, XIP
    .rodata     : { *(.rodata*) }     > FLASH   <- constants
    .data       : { *(.data*) }       > RAM AT> FLASH  <- copied at boot
    .bss        : { *(.bss*) }        > RAM           <- zeroed at boot
    ._user_heap_stack : ...           > RAM
  }
```

```
  KEY CONCEPT: VMA vs LMA
  +--------------------------------------------------------------+
  | .data has TWO addresses:                                     |
  |   LMA (Load address)   = in FLASH (where the initializer     |
  |                          is stored)                          |
  |   VMA (Virtual/run addr)= in RAM  (where the variable lives  |
  |                          at runtime)                         |
  | The "AT> FLASH" directive sets the LMA. Startup copies       |
  | LMA -> VMA. This is what ">RAM AT>FLASH" encodes.            |
  +--------------------------------------------------------------+
```

The linker also emits the symbols (`_sdata`, `_edata`, `_sbss`, `_ebss`,
`_estack`) that the startup code reads to know what ranges to copy and zero.
Getting LENGTH wrong is how you overflow flash or RAM at link time — a
*good* failure, because it's caught before the chip.

---

## The Super-Loop and Cooperative Structure

Without an RTOS, structure comes from disciplined looping plus interrupts.

```c
int main(void) {
    clock_init();
    gpio_init();
    uart_init();
    timer_init();          // ISR sets a 'tick' flag at fixed rate
    for (;;) {
        if (tick) {        // volatile, set by timer ISR
            tick = 0;
            read_sensors();
            run_control();
            update_outputs();
        }
        service_comms();   // best-effort background work
        // optionally: __WFI();  // sleep until next interrupt
    }
}
```

The pattern: ISRs do the *minimum* (set a flag, stash a byte) and the loop does
the work. `__WFI()` ("wait for interrupt") sleeps the core until the next
interrupt, the bare-metal path to low power (`08`). When this hand-rolled
concurrency gets unwieldy — multiple rates, blocking waits, priorities — you
graduate to an RTOS (`04`).

---

## Common Confusion Points

### "I wrote to the GPIO register but nothing happened"

Almost always a **clock gate**: most MCUs power-gate peripheral clocks at
reset to save energy. A peripheral with no clock ignores register writes
silently — the write lands in a dead bus region. Enable the peripheral's clock
in RCC (or equivalent) *first*. This is the #1 first-bring-up bug.

### "My ISR sets a flag but main() never sees it"

The flag isn't `volatile`, so the compiler cached it in a register inside the
loop and never re-reads memory. Mark any variable shared between an ISR and
mainline `volatile`. (And for multi-byte shared state, also guard against the
ISR firing mid-update.)

### "Why does main() copy globals — can't they just start initialized?"

Because RAM is volatile (loses state at power-off) and your initialized values
live in flash. The variable must live in writable RAM at runtime, but its
initial value must survive power-off in flash. Startup bridges the two by
copying. `.bss` skips this because zero needs no stored initializer.

### "volatile fixed my flag — is it also thread-safe now?"

No. `volatile` only forces real memory access and prevents reordering of
volatile accesses. It gives you *visibility*, not *atomicity* or
*happens-before* ordering across contexts. A `volatile` counter incremented in
both ISR and mainline still races. Use a critical section (disable interrupts
briefly) or a true atomic.

---

## Decision Cheat Sheet

| I need to... | Do this |
|---|---|
| Read/write a hardware register | Typed `volatile` MMIO via CMSIS struct |
| Stop the compiler eliding a register read | Make the pointer `volatile` |
| Set/clear one GPIO bit without a race | Write `BSRR` (atomic set/reset register) |
| Share a variable with an ISR | `volatile` + critical section for RMW |
| Initialize globals before main() | Startup `.data` copy + `.bss` zero |
| Place a function in RAM for speed | Linker section attribute (`.RamFunc`) |
| Fit code into flash / data into RAM | Tune linker script MEMORY lengths |
| Sleep until the next interrupt | `__WFI()` in the super-loop |
| First thing when a peripheral is dead | Check its clock is enabled in RCC |
| Replace printf debugging on bare metal | Semihosting or SWO/ITM trace (`09`) |
