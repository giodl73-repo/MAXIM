# embedded-systems/ — Status

## Files

| File                             | Topic                                                       | Status |
|----------------------------------|-------------------------------------------------------------|--------|
| 00-OVERVIEW.md                   | The Embedded Landscape; MCU/MPU/SoC; bare-metal vs RTOS     | ✅ |
| 01-MICROCONTROLLERS.md           | MCU/MPU/SoC, ARM Cortex-M family, the memory map            | ✅ |
| 02-BARE-METAL.md                 | Registers, MMIO, volatile, GPIO, startup/linker, super-loop | ✅ |
| 03-INTERRUPTS-AND-TIMERS.md      | NVIC, ISR discipline, interrupt latency, timers/PWM         | ✅ |
| 04-RTOS.md                       | Tasks, scheduling, rate-monotonic/EDF, priority inversion   | ✅ |
| 05-MEMORY-AND-DMA.md             | Flash/RAM, stack/heap, DMA, cache coherence on MCUs         | ✅ |
| 06-PERIPHERALS-AND-BUSES.md      | UART/SPI/I2C/CAN/USB, ADC/DAC                                | ✅ |
| 07-REAL-TIME-CONSTRAINTS.md      | Hard vs soft real-time, WCET, schedulability, jitter        | ✅ |
| 08-POWER-MANAGEMENT.md           | Sleep modes, clock gating, energy budgets, battery, watchdog | ✅ |
| 09-DEBUG-AND-TOOLCHAIN.md        | JTAG/SWD, cross-compilation, HAL, testing, OTA updates      | ✅ |

## Coverage Notes

Embedded / bare-metal / real-time layer of the library. Covers the MCU as a
chip (Cortex-M, fixed memory map), no-OS programming (memory-mapped I/O,
`volatile`, GPIO, startup code, linker scripts), interrupts (NVIC, ISR rules,
latency, tail-chaining) and timers/PWM, the RTOS world (fixed-priority
preemptive scheduling, rate-monotonic with the ~0.693 utilization bound, EDF,
priority inversion and inheritance with the Mars Pathfinder case), memory and
DMA (flash/SRAM constraints, static allocation, ping-pong DMA, the M7
cache/DMA coherence trap), board-level buses (UART/SPI/I2C/CAN/USB signaling,
ADC/DAC), real-time theory (hard/firm/soft, WCET, utilization bound + exact
response-time analysis worked example, jitter), power (sleep ladder, clock
gating, DVFS, energy budgeting, watchdog), and the toolchain (cross-compilation,
SWD/JTAG, HAL layering, host/emulator testing, A/B OTA with rollback).

Cross-references `computer-architecture/` (ISA, pipeline, cache coherence,
memory hierarchy), `os/` (virtual memory, full schedulers, Linux), `robotics/`
(actuators, control, ROS), `electronics/` (signal conditioning, open-drain,
push-pull), and `energy-storage/` (battery chemistry and capacity). Stays on
the MCU / bare-metal / RTOS side of the line — defers general OS and CPU
microarchitecture rather than duplicating them.
