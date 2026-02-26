# Systems and OS Pioneers — Thompson, Ritchie, Kernighan, Stallman, Torvalds

## Era Overview

```
UNIX AND ITS DESCENDANTS: 1965–2000
=====================================

  1965 ─── MULTICS: Bell Labs + MIT + GE. Too ambitious. Cancelled 1969.
           Thompson and Ritchie wanted something simpler.

  1969 ─── THOMPSON: First Unix on a PDP-7. Written to play Space Travel.
           Key insight: one small team, one machine, clean design.

  1970 ─── Unix named ("Unics" → "Unix" — a pun on Multics).

  1971 ─── Unix Version 1. PDP-11. Written in assembly.

  1972 ─── RITCHIE: C language developed (from Thompson's B).

  1973 ─── Unix rewritten in C. First OS written in a high-level language.
           Portability suddenly possible: same OS, different hardware.

  1974 ─── "The Unix Time-Sharing System" paper (CACM).
           Marks the beginning of Unix spreading outside Bell Labs.

  1975–78: Unix licensed to universities. BSD born at Berkeley.

  1983 ─── STALLMAN: GNU project announced. Free software movement.
  1984 ─── GNU begins producing Unix-compatible tools (gcc, emacs, etc.)

  1987 ─── TANENBAUM: MINIX for education. Inspires Torvalds.

  1991 ─── TORVALDS: Linux kernel announced on comp.os.minix.

  1992 ─── Linux + GNU tools = working free OS. GNU/Linux.

  1993 ─── FreeBSD, NetBSD released (BSD Unix fully free).

  2000s ─── Linux dominates servers, embedded systems.
           macOS (Darwin) is BSD Unix under the hood.
           Android is Linux kernel.
           Windows NT's design influenced by Unix (Dave Cutler,
           who also designed VMS for DEC).
```

---

## Ken Thompson (1943–present) and Dennis Ritchie (1941–2011)

### Bio Snapshot

**Thompson**: Bell Labs from 1966. Co-invented Unix, B language, C (with Ritchie). At Google from 2006 — co-designed the Go programming language with Rob Pike and Robert Griesemer. Turing Award 1983 (shared with Ritchie).

**Ritchie**: Bell Labs from 1967. Designed the C language. Co-authored "The C Programming Language" (K&R, 1978) with Brian Kernighan. Died October 2011 — one week after Steve Jobs, received comparatively little media attention. Turing Award 1983 (shared with Thompson).

### Why Unix

**Multics (1965–1969)**: The predecessor attempt by MIT, Bell Labs, and GE aimed to be a fully general "computation utility" — like an electric utility, users would access computing power via terminals. The design was so ambitious that it was late, slow, expensive, and over-engineered. Bell Labs withdrew in 1969.

Thompson wanted to write a video game (Space Travel) that ran fast. He had a spare PDP-7 minicomputer. He wrote a minimal operating system to support it:

```
UNIX DESIGN PRINCIPLES (as they emerged)
==========================================

  1. Write programs that do ONE thing and do it well.
  2. Write programs to work together (pipes).
  3. Write programs to handle text streams (universal interface).
  4. Everything is a file.
  5. The kernel does as little as possible.
  6. Policy separate from mechanism.

  EVERYTHING IS A FILE:
  ┌────────────────────────────────────────────────────────┐
  │  Regular file     /home/user/doc.txt                   │
  │  Directory        /usr/bin/                            │
  │  Block device     /dev/sda1  (hard disk partition)     │
  │  Character device /dev/tty   (terminal)                │
  │  Network socket   (file descriptor after accept())     │
  │  Pipe             (file descriptor pair)               │
  │  /proc entry      /proc/1234/status  (process state)   │
  └────────────────────────────────────────────────────────┘
  Same read()/write()/close() API for all of them.
  A program doesn't need to know what it's reading from.

  PIPES (Thompson's invention, 1972):
  program1 | program2 | program3
  Each program reads stdin, writes stdout.
  Pipe connects stdout of one to stdin of next.
  Compose complex behavior from simple programs.

  ls -l | grep "^d" | sort -k5 -n | tail -10
  (list dirs sorted by size, largest 10)
  No program knows about the others.
```

### Unix Rewritten in C

The decision to rewrite Unix in C (1973) was arguably the most consequential engineering decision in software history:

```
BEFORE: Unix in assembly (PDP-11)
  - Runs only on PDP-11
  - Change hardware → rewrite OS from scratch
  - Maintenance: requires assembly expertise

AFTER: Unix in C
  - Port the C compiler to new hardware
  - Recompile Unix
  - New hardware has Unix

  UNIX PORTABILITY IN PRACTICE:
  PDP-11 → VAX → 68000 → SPARC → MIPS → x86 → ARM → ...
  The same OS, recompiled, on each new architecture.

  This is still the model: Linux runs on x86, ARM, MIPS, RISC-V,
  PowerPC, S/390 — same source code, recompiled.
  Windows NT: same source code built for x86, ARM.
```

### C Language

Ritchie designed C from Thompson's B language, which was derived from Martin Richards' BCPL. The lineage: BCPL → B → C.

```
C'S DESIGN PRINCIPLES
=======================

  Thin abstraction over hardware:
    No runtime (no GC, no exceptions, no bounds checking)
    Pointers = machine addresses
    sizeof() returns bytes
    Undefined behavior = trust the programmer

  Direct hardware access:
    Bitwise operations (& | ^ << >>)
    Pointer arithmetic
    Explicit memory management (malloc/free)
    volatile for hardware registers

  Portability through abstraction:
    int, long, char — size defined relative to platform
    (a design flaw, addressed by stdint.h later: int32_t, etc.)
    #include <stdio.h> — standard library, implemented per platform

  THE LINEAGE:
  C (1972)
  ├── C++ (Stroustrup, 1983) — adds OOP, templates, RAII
  │     └── Java (Gosling, 1995) — GC, no pointers, JVM
  │           └── C# (Hejlsberg, 2000) — Java++, CLR
  │                 └── everything you write at Microsoft
  └── Objective-C (Cox, 1983) — C + Smalltalk OOP
        └── Swift (Lattner, 2014) — modern iOS/macOS language
  C (1972)
  └── Go (Pike, Griesemer, Thompson, 2007) — C philosophy, modern
```

---

## Brian Kernighan (1942–present)

### Bio Snapshot

Canadian computer scientist. Bell Labs 1967–2000. Princeton. Contributed to Unix tools — AWK (Aho, Weinberger, Kernighan), sed, many others. Co-authored "The C Programming Language" (K&R) with Ritchie, the most influential programming book ever written. Also wrote "Software Tools" (with Plauger), "The Unix Programming Environment" (with Pike), and "The Practice of Programming."

### K&R C

"The C Programming Language" (1978, second edition 1988) is the reference against which every other programming language book is measured:

```
K&R C — WHY IT MATTERS
========================

  Short: 272 pages in first edition.
  Complete: covers the entire language.
  Example-driven: programs as short, complete, useful examples.
  Introduced: the famous "hello, world" program.

  #include <stdio.h>
  main() {
      printf("hello, world\n");
  }

  This was the first thing millions of programmers typed.
  The "hello world" convention originated here.

  K&R defined "C" informally until the ANSI C standard (1989).
  "K&R C" and "ANSI C" are still meaningful distinctions
  in discussions of legacy code.
```

**AWK** (Aho, Weinberger, Kernighan, 1977): a pattern-scanning language that processes text line by line, matching patterns and executing actions. Still the fastest way to process structured text files. `awk '{sum += $3} END {print sum}'` — sum the third column of any whitespace-delimited file. One of the original Unix tools.

---

## Richard Stallman (1953–present)

### Bio Snapshot

MIT AI Lab programmer from 1971. Founded the Free Software Foundation (FSF) in 1985. Wrote GNU Emacs, the first version of GCC (GNU C Compiler), and the GNU General Public License (GPL). Resigned from MIT and FSF positions in 2019 amid controversy, returned to FSF board 2021. Perpetually polarizing.

### The GNU Project

**Context**: In 1983, software had transitioned from being freely shared (1950s–1970s, when the norm at universities and Bell Labs was sharing source code) to proprietary (commercial vendors locked up source code). Stallman, having experienced the open sharing culture at MIT AI Lab, saw this as a moral problem.

```
GNU PROJECT ARCHITECTURE
=========================

  GOAL: a complete Unix-compatible operating system with
        source code freely available.

  WHAT GNU PRODUCED:
    GCC         — C/C++ compiler (later LLVM took over; GCC still dominant)
    GNU Emacs   — editor / operating system disguised as editor
    GNU binutils — assembler, linker
    GNU libc    — standard C library
    GNU coreutils — ls, cp, mv, rm, cat, sort, uniq, grep, etc.
    GNU bash    — the shell (Bourne Again Shell)
    GNU make    — build system
    GNU tar     — archive tool
    GNU autoconf/automake — build configuration

  WHAT GNU LACKED (until 1991):
    A kernel. GNU's kernel project (HURD) was notoriously behind schedule.

  1991: Torvalds contributes a kernel.
  GNU tools + Linux kernel = working free OS.
  Stallman insists it should be called "GNU/Linux." Almost no one does.
```

### The GPL

The GNU General Public License (GPL) is Stallman's legal invention — it uses copyright law to enforce openness rather than restrict it. The mechanism is called "copyleft":

```
GPL COPYLEFT MECHANISM
========================

  Standard copyright: you may not copy/distribute without permission.

  GPL: you may copy/modify/distribute, BUT:
    1. You must provide source code.
    2. Any derivative work must also be GPL-licensed.
    3. You cannot add restrictions.

  "Viral" nature: if you link GPL code into your program,
  your program must also be GPL (if distributed).

  GPL variants:
    GPLv2 (1991): original. Linux kernel uses this.
    GPLv3 (2007): adds anti-tivoization, patent clauses.
    LGPL: Lesser GPL. Libraries: you can link without going GPL.
    AGPL: Affero GPL. Covers network-accessible software.

  Effect:
    Anyone can use Linux, GCC, Bash, etc. for free.
    Anyone who modifies and distributes must share their changes.
    Red Hat, SUSE, Ubuntu — all distribute Linux, all share kernel changes.
    Google (Android Linux kernel): shares kernel changes, not Android apps.
```

---

## Linus Torvalds (1969–present)

### Bio Snapshot

Finnish software engineer. Helsinki. Studied under Tanenbaum's MINIX-influenced curriculum. Announced Linux on Usenet in August 1991: "Just a hobby, won't be big and professional like gnu." Now the most widely deployed operating system kernel in history.

### Linux Kernel

```
THE LINUX ANNOUNCEMENT (August 25, 1991)
==========================================

  From: torvalds@klaava.Helsinki.FI (Linus Benedict Torvalds)
  To: comp.os.minix
  Subject: What would you like to see most in minix?

  "Hello everybody out there using minix -

  I'm doing a (free) operating system (just a hobby, won't be big
  and professional like gnu) for 386(486) AT clones. This has been
  brewing since april, and is starting to get ready. I'd like any
  feedback on things people like/dislike in minix, as my OS
  resembles it somewhat..."
```

**What made Linux win**:

```
LINUX'S TECHNICAL ADVANTAGES
==============================

  Monolithic kernel (vs. microkernel):
    All kernel services in one address space.
    Faster IPC between kernel components.
    More complex than microkernels (Mach, HURD) but faster in practice.
    Tanenbaum famously argued monolithic was obsolete (1992 Usenet flame war).
    Torvalds was right in practice.

  Modular design within monolith:
    Loadable kernel modules (LKM): add drivers without rebooting.
    Device drivers as modules, loaded on demand.
    This gives microkernel-like extensibility without IPC overhead.

  Hardware support breadth:
    Linux supports more hardware than any other OS.
    Driven by: large community, GPL (vendors contribute drivers to avoid
    maintaining out-of-tree forks), and Torvalds's acceptance standards.

  Git:
    Torvalds designed Git (2005) for Linux kernel development after
    BitKeeper revoked its free license. Git is now the universal
    version control system. (Covered in computing/ module.)
```

**Linux today**:

```
WHERE LINUX RUNS (2025)
========================

  97% of top 1 million web servers
  100% of top 500 supercomputers
  ~72% of smartphones (Android = Linux kernel)
  All major cloud providers (AWS, Azure, GCP) run Linux VMs
  Embedded: routers, smart TVs, cars, industrial controllers
  Azure itself runs significant Linux workloads
  Windows Subsystem for Linux (WSL2) = Linux kernel inside Windows

  Kernel contributors (all-time):
    Red Hat, Intel, Google, Samsung, SUSE, Linaro, IBM, ...
    Thousands of companies pay engineers to contribute.
```

---

## Comparison Table

| Figure | Life | Key Contribution | Turing Award |
|--------|------|-----------------|--------------|
| Thompson | 1943– | Unix, B language, Go co-designer | 1983 |
| Ritchie | 1941–2011 | C language, Unix co-creator | 1983 |
| Kernighan | 1942– | K&R C book, AWK, Unix tools | — |
| Stallman | 1953– | GNU project, GCC, GPL/copyleft | — |
| Torvalds | 1969– | Linux kernel, Git | — |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Unix operating system | Thompson (+ Ritchie) |
| C language | Ritchie (1972) |
| "Everything is a file" / pipes | Thompson / Unix design |
| "The C Programming Language" (K&R) | Kernighan + Ritchie |
| AWK | Aho + Weinberger + Kernighan (1977) |
| Free software movement | Stallman |
| Copyleft / GPL license | Stallman |
| GCC compiler | Stallman (1987 initial) |
| Linux kernel | Torvalds (1991) |
| Git version control | Torvalds (2005) |

---

## Common Confusion Points

**"Linux is just a kernel."**
Technically correct. What most people call "Linux" is a GNU/Linux distribution (Stallman's point). The kernel (Torvalds) + GNU tools (Stallman) + a package manager + a desktop environment = a usable system. Android uses the Linux kernel but replaces virtually all other components.

**"Unix is open source."**
Unix source code from Bell Labs was licensed (not open) to universities from the late 1970s. The legal status was murky — the Unix wars (BSD vs. AT&T lawsuit, 1992–1994) created years of uncertainty. Modern BSDs (FreeBSD, OpenBSD, NetBSD) emerged from the legal settlement with clean licenses. macOS is based on Darwin, which is BSD-based. The first truly free Unix-like system was GNU/Linux (1992).

**"Windows is not influenced by Unix."**
Windows NT (1993) was designed by Dave Cutler, who came from DEC VMS — which was also influenced by Unix design philosophy. NT's object model and driver model differ from Unix, but the influence is visible. Windows has shipped WSL (Windows Subsystem for Linux) since 2016 — Microsoft now distributes a Linux kernel.

**"Torvalds owns Linux."**
Torvalds holds the trademark on "Linux" and has final say on the kernel, but thousands of contributors hold copyright on their contributions. The GPL ensures that no entity can make Linux proprietary. The Linux Foundation manages the trademark and sponsorship. Torvalds has written that he could step down and the project would continue.
