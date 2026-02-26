# Operating Systems — Taxonomy, Genealogy & Core Abstractions

## The OS Family Tree

```
                         UNIX (AT&T Bell Labs, 1969)
                              │
              ┌───────────────┼───────────────┐
              │               │               │
           BSD (1977)    System V (1983)    Minix (1987)
         ┌───┴───┐           │                    │
      FreeBSD  OpenBSD    Solaris            Linux (1991, Torvalds)
         │       │                          ┌─────┼──────┬────────┐
    Darwin/XNU  ──────────────────     Ubuntu  Fedora  Arch  Android
    (Apple 2000)                            │           │
         │                            Debian family  RHEL family
    ┌────┴────┐                        (apt)          (dnf/yum)
  macOS 10.x  iOS/iPadOS
  (Aqua UI)   (SpringBoard)


                         CP/M → MS-DOS (1981)
                              │
                    Windows 9x (Win32 + DOS, 1993-2000)
                              │
                    Windows NT 3.1 (1993) ─── COMPLETELY different kernel
                         │  (HAL + Executive + subsystems)
               ┌─────────┴──────────┐
          NT 4 → 2000 → XP → Vista  Windows CE / Mobile
               │                         │
           Win 7/8/10/11            Windows Phone (dead)
               │
          Windows Server 2019/2022
               │
          WSL2 (Linux kernel in VM, 2019) ─── Linux apps on Windows
```

**Key insight**: macOS and iOS share the same XNU kernel. Android and Ubuntu share the same Linux kernel. Windows NT is completely unrelated to Unix — clean-room design from Dave Cutler (ex-DEC VMS).

---

## Kernel Architecture Taxonomy

```
MONOLITHIC                    HYBRID                      MICROKERNEL
─────────────                 ─────────────               ─────────────
Everything in ring 0          Core in ring 0,             Minimal kernel,
                              servers in user space        services as user procs

Linux                         Windows NT                  Mach (inside XNU)
│                             │                           QNX, L4
├─ VFS                        ├─ HAL                      (macOS uses Mach for
├─ Memory mgr                 ├─ Executive (ring 0)       IPC/memory/tasks but
├─ Scheduler                  │   ├─ I/O Manager          BSD for most else)
├─ Network stack              │   ├─ Object Manager
├─ Device drivers             │   ├─ Security Reference
└─ Filesystems                │   ├─ Process Manager
                              │   └─ Memory Manager
  Pros: fast (no IPC          ├─ Kernel Mode Drivers      Pros: isolation, safety
  overhead), simple           └─ Win32k.sys (GDI/User)    Cons: IPC overhead
  Cons: one bug = panic
                              Subsystems (user mode):     Reality: pure microkernels
  Fast crashes: "kernel       ├─ Win32 subsystem           slow in practice —
  panic", OOM kill            ├─ POSIX subsystem (WSL)    XNU and NT both hybrid
                              └─ WoW64 (32-bit compat)
```

---

## The Five Universal Abstractions

Every OS provides these. The vocabulary differs; the concept doesn't.

### 1. Process

```
Windows                     Linux                       macOS
─────────────               ─────────────               ─────────────
PROCESS (kernel obj)        task_struct                 proc (BSD)
Handle table                File descriptor table       File descriptor table
Virtual address space       mm_struct                   vm_map
Token (security context)    credentials (uid/gid/caps)  security label (sandbox)
Job Object (group)          cgroup (group)              App Sandbox (group)

PID                         PID                         PID
PPID (parent)               PPID                        PPID
Thread = separate obj       Thread = clone() child      Thread = pthread
Fiber = user-mode coop      green thread = userspace    dispatch queue (GCD)

Create:                     Create:                     Create:
CreateProcess()             fork() + exec()             posix_spawn() or fork/exec
OpenProcess(PID, rights)    /proc/PID/...               sysctl(KERN_PROC, PID)

View:                       View:                       View:
Task Manager                ps, top, htop               Activity Monitor
Get-Process (PowerShell)    /proc/<pid>/status          ps, top
```

### Handle / fd / Port — The Kernel Resource Reference Model

Every OS gives userspace an opaque, revokable reference to kernel-managed resources. The mechanism is universal; the semantics differ significantly.

```
Concept          Windows HANDLE              POSIX fd (int)         Mach port right
────────────     ──────────────              ──────────────         ──────────────
What it is       Index into per-process      Small integer          Capability token with
                 handle table; kernel obj    (0,1,2,...), index     send/receive rights;
                 pointer stored in table     into process fd table  first-class kernel obj

Table lives      Per-process handle table    Per-process fd table   Per-task port namespace
                 (stored in EPROCESS)        (files_struct)         (ipc_space)

Refcounting      Kernel Object refcount;     File description        Port reference count;
                 CloseHandle() dec count     refcount shared via     mach_port_deallocate()
                 → GC when zero             dup()/fork()

Inheritance      opt-in: SECURITY_ATTRS      all fds unless          explicit port rights
                 bInheritHandle = TRUE       FD_CLOEXEC is set       transferred via
                                             (set by default in Go)  mach_msg()

Passing across   DuplicateHandle()           SCM_RIGHTS cmsg via     mach_port_insert_right()
process boundary creates new handle in       Unix domain socket;     or task_get_special_port()
                 target process; source      fd is transplanted      Mach message body
                 handle stays valid          into receiver's table

Typed?           Yes — Object type stored    No — fd is an int;      Partially — send vs
                 in Object Header;           kernel knows type via   receive vs send-once
                 OpenProcess ≠ OpenFile      struct file * in table  rights are distinct

Revocation       CloseHandle() — immediate   close() — immediate     mach_port_destroy() or
                                             but dup'd copies live   mach_port_deallocate()

Security         Token check on Open         DAC check at open();    Capability model —
                 (access check at open       fd itself is unforgeable  having the port IS
                 time + object ACL)          but untyped             the permission
```

**The non-obvious cross-OS gotcha:** On Linux, `dup2()` and `fork()` both copy fd integers but share the underlying `struct file` (offset, flags). On Windows, `DuplicateHandle()` creates a new kernel handle pointing to the same object — semantically equivalent but syntactically different. On macOS/iOS, Mach port rights are typed capabilities: holding a send right IS permission to send to that port. There is no separate access check.

### 2. Virtual Memory

```
Windows terms          Linux terms            macOS terms
──────────────         ──────────────         ──────────────
Virtual Alloc          mmap / brk             vm_allocate
Working Set            RSS (Resident Set)     RSIZE (resident)
Page File              Swap space             Swap file (APFS)
Committed pages        Anonymous pages        Anonymous mapping
Section object         mmap file              vm_map_entry
Memory-mapped file     mmap(fd, ...)          mmap(fd, ...)
Protected memory       PROT_READ/WRITE        VM_PROT_READ/WRITE
DEP (no-execute)       NX bit                 NX bit (XD on Intel)
ASLR                   ASLR                   ASLR + PIE mandatory
```

### 3. File System

```
Windows (NTFS/ReFS)        Linux (ext4/XFS/btrfs)     macOS (APFS)
───────────────────        ──────────────────────     ─────────────
C:\Users\alice\docs        /home/alice/docs           /Users/alice/docs
Drive letters (C:, D:)     Single tree, mount points  Single tree, mount points
Backslash separator \      Forward slash /            Forward slash /
Case-insensitive (NTFS)    Case-sensitive             Case-insensitive (default)
NTFS streams (ADS)         xattrs                     xattrs + resource forks
ACL: DACL/SACL             DAC: owner/group/other     POSIX + ACL + sandbox
Permissions: SDDL          chmod 755, umask           chmod + sandbox profiles
Hardlinks + junctions      hardlinks + symlinks       hardlinks + symlinks
NTFS compression           btrfs/ext4 compression     APFS native compression
Volume Shadow Copy         LVM snapshots / btrfs      APFS snapshots (Time Machine)

Key locations:
%SYSTEMROOT%\System32      /usr/bin, /usr/lib         /usr/bin (SIP protected)
%APPDATA%                  ~/.config (XDG)            ~/Library/Application Support
%PROGRAMFILES%             /opt, /usr/local            /Applications
%TEMP%                     /tmp (tmpfs)               /tmp → /private/tmp
HKCU/HKLM (registry)       No registry — files only   plist files (~/Library/Preferences)
```

### 4. Inter-Process Communication (IPC)

```
Mechanism      Windows                  Linux                macOS
─────────────────────────────────────────────────────────────────────
Pipes          Named pipes (\\.\pipe\)  Named + anonymous    Named pipes
               AnonymousPipe            FIFO (mkfifo)        FIFO
Sockets        Winsock (IANA compat)    POSIX sockets        POSIX sockets
               Unix domain sockets      Unix domain sockets  Unix domain sockets
Shared mem     CreateFileMapping        shm_open / mmap      shm_open / mmap
               MapViewOfFile            shmget (SysV)        Mach shared memory
Message queue  MSMQ / Service Bus       POSIX mq_open        No built-in mq
               (legacy: WM_* messages)  D-Bus (user space)
RPC            COM / DCOM / RPC         D-Bus / gRPC         XPC (Mach-based)
               WCF (high-level)         GRPC                 NSXPCConnection
Events         CreateEvent / WaitFor*   eventfd / signalfd   dispatch_semaphore
Signals        (no direct equivalent)   SIGTERM/SIGKILL etc  SIGTERM/SIGKILL etc
               WM_CLOSE for windows
Clipboard      OpenClipboard            X11 selections /     NSPasteboard
                                        Wayland wl_data_dev
```

### 5. Scheduling

```
All modern OSes: preemptive, priority-based, time-sliced

Windows                    Linux                      macOS
──────────────             ──────────────             ──────────────
32 priority levels         nice -20 to +19            QoS classes
0-15: normal               CFS (Completely Fair        (background/utility/
16-31: real-time           Scheduler) — virtual        default/user-interactive/
                           runtime, red-black tree     user-initiated)

Quantum: ~15ms             CFS: proportional          GCD (Grand Central Dispatch)
                           time slices                 = work queue on top of
                                                       kernel threads

Thread pool: ThreadPool    io_uring (async I/O)        dispatch_queue_t
Task Parallel Library      epoll (event I/O)           DispatchQueue.global()
async/await → TPL          libevent / libuv            async/await → Swift concurrency
```

### Async I/O Model — OS Notification Mechanisms

Every high-performance server framework (Node.js, Tokio, .NET, Netty, libuv) sits on top of one OS async I/O primitive. The same conceptual split: **readiness-based** (tell me when fd is ready; I'll do the I/O) vs **completion-based** (I'll start the I/O; tell me when it's done).

```
                  ASYNC I/O LANDSCAPE
                  ═══════════════════

  READINESS-BASED                         COMPLETION-BASED
  "fd is ready to read/write"             "I/O operation has completed"
  ─────────────────────────────           ──────────────────────────────
  epoll (Linux 2.5.44+)                   IOCP (Windows NT 3.5+)
  kqueue (BSD / macOS 10.3+)              io_uring (Linux 5.1+)
  poll / select (POSIX, ancient)

  Mechanism: register interest            Mechanism: post work item;
  in fd; wait for event;                  OS completes I/O in kernel;
  then call read/write yourself           OS queues completion to port

  Model:                                  Model:
    register(fd, READ)                      begin_read(buf, overlapped)
    events = wait()                         completions = dequeue()
    for ev in events:                       for c in completions:
      data = read(ev.fd)                      process(c.result)

  Edge-triggered (ET) vs                  Zero-copy: kernel fills buffer
  Level-triggered (LT):                   directly; userspace never calls
  ET: event once when state changes        read() explicitly
  LT: event on every poll while ready

  Scalability: O(1) vs select's O(N)      Windows async sockets, file I/O,
  epoll scales to 100k+ fds               pipes all use IOCP natively
```

```
Feature          select/poll         epoll (Linux)       kqueue (BSD/macOS)   IOCP (Windows)      io_uring (Linux 5.1+)
─────────────    ──────────────      ──────────────      ──────────────────   ──────────────      ──────────────────────
Model            Readiness           Readiness           Readiness            Completion          Completion (+ readiness)
Syscall count    1 per wait          O(1) wait           O(1) wait            dequeue only        near zero (SQ/CQ rings)
Max fds          1024 (FD_SETSIZE)   millions            millions             unlimited           unlimited
Edge trigger     No                  Yes (EPOLLET)       Yes (EV_CLEAR)       N/A                 N/A
File I/O         No (only sockets)   No                  Yes (vnode filter)   Yes (native AIO)    Yes (full file I/O)
Kernel version   Ancient             2.5.44 (2002)       FreeBSD 4.1 (2000)   NT 3.5 (1994)       5.1 (2019)
Used by          Legacy only         libuv, epoll mode   macOS / BSD apps     .NET, Windows WS    io_uring in Rust/Go
.NET mapping     —                   SocketAsyncEngine   SocketAsyncEngine    IOCP ThreadPool     via P/Invoke
```

**The completion-vs-readiness conceptual gap:** With epoll, you get notified "fd is readable" — you still call `read()`. With IOCP, you initiate `ReadFile(overlapped)` and get notified "your read finished, here's the data." io_uring bridges both: submit I/O operations to a submission queue ring, harvest completions from a completion queue ring — all via shared memory with the kernel, eliminating most syscall overhead.

---

### IPC Performance & Semantics — Not Flat Equivalents

```
Mechanism        Latency        Copy semantics           Cross-process resource passing
───────────      ──────────     ─────────────────────    ──────────────────────────────
AF_UNIX socket   ~1 µs          kernel copies data       SCM_RIGHTS: pass open fd to
(Linux/macOS)                   send → kernel buf         another process via ancillary
                                 → recv                   data; receiver gets new fd
                                                          pointing to same file description

Named pipe       ~2-5 µs        kernel buffers data       Windows: no fd passing; use
(Windows)        (kernel buf)   WriteFile → buf           DuplicateHandle() to duplicate
\\.\pipe\name                   → ReadFile                a HANDLE into another process
                                                          (requires PROCESS_DUP_HANDLE)

Mach message     ~3-10 µs       small msgs: copied        mach_port_insert_right():
(macOS/iOS)      (IPC trap)     large msgs: OOL (out-     transplant port right into
                                of-line) via COW page     target task; XPC is built on
                                mapping — zero copy        this; entire IPC security
                                for large payloads         model is capability-based

Shared memory    <1 µs          zero copy: processes      Must pass fd/handle OOB;
mmap / MapView   (no kernel     map same physical         no built-in synchronization —
                 copy path)     pages; you manage         need semaphore/mutex/eventfd
                                sync yourself             separately
```

**Container and multi-process dev implication:** When you split a monolith into processes, or write a language server / debug adapter, the IPC choice determines both your security model and your performance ceiling. Linux `SCM_RIGHTS` fd passing is how container runtimes hand off network namespaces. Windows `DuplicateHandle` is how the CLR debugger attaches. Mach `mach_port_insert_right` is how every XPC service call works under the hood.

## Privilege Rings (x86)

```
Ring 0 ──── Kernel                  (OS core, drivers)
Ring 1 ──── (unused by modern OSes)
Ring 2 ──── (unused by modern OSes)
Ring 3 ──── User space              (all apps)

Syscall / int 0x80 / SYSCALL instruction = user→kernel transition
  Windows: NtXxx functions in ntdll.dll (undocumented) → kernel
  Linux:   syscall table in arch/x86/entry/syscalls/
  macOS:   BSD syscalls + Mach traps (two separate tables)

Modern additions:
  VMX (VT-x) = Ring -1: hypervisor level (Hyper-V, KVM, VMware)
  SGX         = Ring -2: enclaves (trusted execution)
  SMM         = Ring -3: system management mode (firmware)

Windows VBS (Virtualization-Based Security):
  Credential Guard runs in Ring -1 (Secure World)
  Isolated from even the OS kernel
```

---

## Security Models Compared

```
Concept          Windows                    Linux                  macOS/iOS
──────────────────────────────────────────────────────────────────────────────
Identity         SID (binary GUID-like)     uid/gid (integer)      uid/gid + entitlements
Capabilities     Privileges in Token        POSIX capabilities     Entitlements (plist)
                 SeDebugPrivilege           CAP_NET_ADMIN etc      com.apple.security.*
Mandatory         Integrity Levels           SELinux / AppArmor    Sandbox (iOS: all apps)
access control   Low/Medium/High/System     (labels on files)     macOS: opt-in signing
Elevation        UAC prompt → new token     sudo (NOPASSWD/TTY)    sudo / AuthorizationRef
App sandbox      AppContainer (UWP)         seccomp-bpf filters   iOS: mandatory
                 WSL2 uses LinuxKernel      Flatpak/Snap sandbox  macOS: Hardened Runtime
Code signing     Authenticode (signtool)    GPG package signing   Apple Developer ID
                 Required for drivers       Optional for apps     Required for distribution
Attestation      Secure Boot + UEFI         Secure Boot           Notarization (Gatekeeper)
```

---

## Bootloader to Shell (Same Concept, Different Stack)

```
Power on
  ↓
UEFI firmware (all modern platforms)
  ↓
Bootloader
  Windows: Windows Boot Manager → winload.exe → ntoskrnl.exe
  Linux:   GRUB2 → linux kernel image → initramfs → init=/sbin/init
  macOS:   boot.efi → kernel cache (prelinked) → launchd (PID 1)
  iOS:     iBoot (Apple secure boot chain) → XNU → launchd
  Android: aboot/LK → Linux kernel → init → Zygote (app mother process)
  ↓
PID 1 / init process
  Windows: smss.exe (Session Manager) → csrss.exe + wininit.exe
  Linux:   systemd (PID 1) — unit files, socket activation
  macOS:   launchd (PID 1) — plist jobs in /Library/LaunchDaemons
  iOS:     launchd (same as macOS)
  Android: init → Zygote (pre-forked JVM for fast app launch)
  ↓
User session
  Windows: winlogon.exe → explorer.exe (shell)
  Linux:   getty → login → bash/zsh + optional display manager (GDM/SDDM)
  macOS:   loginwindow → Aqua Dock/Finder
  iOS:     SpringBoard (the home screen IS the shell)
  Android: SystemServer → ActivityManagerService → Launcher
```

---

## Package Management at a Glance

```
Scope          Windows              Linux (Debian)    Linux (RHEL)   macOS        iOS          Android
────────────────────────────────────────────────────────────────────────────────────────────────────
System pkgs    WinGet / MSIX        apt               dnf/yum        Homebrew     (locked)     APK via
               Chocolatey           dpkg              rpm            MacPorts     App Store    Play Store
               Scoop (portable)     snap/flatpak      snap/flatpak   (no Brew     only         APK direct
                                                                     on iOS)                   sideload
Dev tools      winget / choco       apt-get install   dnf install    brew         Xcode only   gradle
Language       pip, npm, cargo,     same              same           same         pip in       pip/npm in
pkgs           nuget, gem                                            (Homebrew    Pythonista   Termux
                                                                     wraps them)
Config store   Registry             /etc/*.conf       /etc/*.conf    plist files  plist files  shared
               HKLM/HKCU            ~/.config/        ~/.config/     ~/Library/   (in app      prefs XML
               GPO for policy       (XDG Base Dir)                  Preferences  container)
```

---

## "Same Thing" Vocabulary Cross-Reference

| Concept | Windows | Linux | macOS | iOS | Android |
|---------|---------|-------|-------|-----|---------|
| Service / daemon | Windows Service (SCM) | systemd unit | launchd agent/daemon | launchd daemon | Android Service component |
| Config store | Registry | /etc files + ~/.config | plist files | plist (in sandbox) | SharedPreferences / SQLite |
| Scheduled task | Task Scheduler (.xml) | cron / systemd timer | launchd StartCalendarInterval | Background fetch | WorkManager / JobScheduler |
| Crash dump | .dmp (WinDbg) | core dump (/var/crash) | .crash (~/Library/Logs) | crash log (Xcode Organizer) | tombstone (/data/tombstones) |
| Package format | .msi / .msix / .exe | .deb / .rpm / snap | .pkg / .dmg / .app | .ipa | .apk / .aab |
| App manifest | AppxManifest.xml | (none standard) | Info.plist | Info.plist + entitlements | AndroidManifest.xml |
| Font/resource dir | C:\Windows\Fonts | /usr/share/fonts | /System/Library/Fonts | (embedded in bundle) | assets/ in APK |
| Dynamic library | .dll (PE format) | .so (ELF format) | .dylib (Mach-O) | .dylib (Mach-O) | .so (ELF, loaded by ART) |
| Executable format | PE (Portable Executable) | ELF | Mach-O | Mach-O | ELF inside APK |
| Debug symbols | .pdb (Program Database) | DWARF (in ELF) | dSYM bundle | dSYM bundle | .sym (symbol table) |
| Env variable | $env:VAR (PS) / %VAR% | $VAR | $VAR | (runtime injection) | (build config / Intent) |
| Temp dir | %TEMP% | /tmp (tmpfs) | /tmp → /private/tmp | NSTemporaryDirectory() | getCacheDir() |
| User data dir | %APPDATA% | ~/.local/share | ~/Library/Application Support | NSDocumentDirectory | getFilesDir() |
| Log location | Event Viewer / ETW | journalctl / /var/log | Console.app / ~/Library/Logs | Xcode Organizer | logcat / /data/anr |
| Network config | ipconfig, netsh | ip, ss, nmcli | ifconfig, networksetup | (no direct CLI) | adb shell ifconfig |
| Firewall | Windows Firewall (netsh) | iptables/nftables | pfctl (pf) | (managed by iOS) | (managed by Android) |

---

## Decision Cheat Sheet — Platform Targets

| You want to... | Use |
|----------------|-----|
| Ship a native Windows desktop app (.NET, modern UI) | WinUI 3 + WinApp SDK or WPF (if legacy OK) |
| Ship a cross-platform desktop (Win/Mac/Linux) | Electron (JS) or Tauri (Rust+webview) or .NET MAUI |
| Ship a Linux server daemon | systemd service + Docker container |
| Ship an iOS app to App Store | Swift + SwiftUI, Xcode, Apple Developer Program |
| Ship an Android app to Play Store | Kotlin + Jetpack Compose, Android Studio, Play Console |
| Ship a cross-platform mobile app | React Native or Flutter (if not Apple Silicon perf critical) |
| Automate Windows admin | PowerShell (pwsh) — not cmd, not bash |
| Automate Linux/macOS admin | bash/zsh + Python for complex logic |
| Debug a Windows process crash | WinDbg + PDB symbols + !analyze -v |
| Debug a Linux kernel crash | crash + vmcore + DWARF symbols |
| Understand why an app is slow on macOS | Instruments (Time Profiler / Allocations) |
| Understand why an app is slow on Android | Android Studio Profiler + systrace |
| Debug a Linux kernel crash | crash + vmcore + DWARF symbols |

## Decision Cheat Sheet — OS Primitives

| You need... | Linux | Windows | macOS |
|-------------|-------|---------|-------|
| Async I/O at scale | epoll / io_uring | IOCP (I/O Completion Ports) | kqueue |
| Watch filesystem for changes | inotify / fanotify | ReadDirectoryChangesW | kqueue EVFILT_VNODE |
| Pass fd/handle to another process | SCM_RIGHTS via AF_UNIX | DuplicateHandle() | mach_port_insert_right() |
| Signal a different process | kill(pid, sig) | (no direct equiv) / WM_CLOSE for windows | kill(pid, sig) |
| Shared memory between processes | shm_open + mmap | CreateFileMapping + MapViewOfFile | shm_open + mmap |
| Enforce per-process resource limits | cgroups v2 | Job Object limits | Resource limits + App Sandbox |
| Run code in reduced privilege | seccomp-bpf + capabilities | AppContainer / Integrity Level Low | Sandbox + entitlements |
| Periodic scheduled work | systemd timer or cron | Task Scheduler | launchd StartCalendarInterval |

---

## Common Confusion Points

**Windows Subsystem for Linux (WSL2)** — WSL2 runs a real Linux kernel inside a lightweight Hyper-V VM. Your Linux processes are real Linux processes. But the Windows filesystem (C:\) is mounted at `/mnt/c` with 9P protocol overhead — do disk-heavy work inside the Linux filesystem (`~/`), not on `/mnt/c/`.

**macOS is not a full-POSIX Linux clone** — It passes the POSIX certification but `/usr/bin` is SIP-protected, `brew` installs to `/opt/homebrew` (Apple Silicon) or `/usr/local` (Intel), and many GNU tools are BSD variants (e.g., `sed -i` needs an empty string argument on macOS).

**Android's Linux kernel ≠ desktop Linux** — Android uses a highly modified Linux kernel with Binder IPC replacing Unix sockets for most IPC, a custom libc (Bionic instead of glibc), and no X11/Wayland display server — framebuffer via SurfaceFlinger.

**iOS processes can't fork()** — POSIX fork() is unavailable in iOS apps (security sandbox). All concurrency is via GCD/async-await/NSOperationQueue. This is intentional isolation.

**Windows Registry vs Linux /etc** — The Registry is a hierarchical database that stores all system + app configuration in binary hives (HKLM\SOFTWARE, HKCU\...). Linux has no equivalent — each app owns its config files in `/etc/` or `~/.config/`. This is a fundamental design philosophy difference, not a quirk.
