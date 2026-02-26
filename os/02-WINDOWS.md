# 02 — Windows OS — Developer Reference

## The Big Picture

```
Windows Architecture — Full Stack (from silicon to your app)
=============================================================

  +------------------------------------------------------------------+
  |  YOUR APPLICATION LAYER                                          |
  |  WinForms / WPF / WinUI 3 / MAUI / Console / ASP.NET            |
  +------------------------------------------------------------------+
  |  .NET RUNTIME (CLR / CoreCLR)                                    |
  |  BCL, GC, JIT (RyuJIT), type system, P/Invoke bridge            |
  +------------------------------------------------------------------+
  |  WINDOWS RUNTIME (WinRT) — COM-based, projectable to .NET/JS/C++|
  |  UWP APIs, WinApp SDK APIs, sensor/device APIs                   |
  +------------------------------------------------------------------+
  |  WIN32 API / Windows API                                         |
  |  CreateProcess, CreateFile, VirtualAlloc, WaitForSingleObject    |
  |  The 30-year stable ABI layer. Everything reaches down to here.  |
  +------------------------------------------------------------------+
  |  WINDOWS SUBSYSTEM (CSR / CSRSS)                                 |
  |  User-mode side of Win32 personality (console, session mgmt)     |
  +------------------------------------------------------------------+
  |  NT EXECUTIVE (ring 0)                                           |
  |  +-----------+ +-----------+ +-----------+ +-----------+         |
  |  | Object    | | Process / | | I/O       | | Security  |         |
  |  | Manager   | | Thread    | | Manager   | | Reference |         |
  |  +-----------+ +-----------+ +-----------+ | Monitor   |         |
  |  +-----------+ +-----------+ +-----------+ +-----------+         |
  |  | Memory    | | Cache     | | Plug&Play | | Power     |         |
  |  | Manager   | | Manager   | | Manager   | | Manager   |         |
  |  +-----------+ +-----------+ +-----------+ +-----------+         |
  |  win32k.sys (GDI, USER, DWM) — kernel-mode graphics              |
  +------------------------------------------------------------------+
  |  NT KERNEL (ntoskrnl.exe)                                        |
  |  Scheduler, interrupt dispatch, synchronization, DPC/APC         |
  +------------------------------------------------------------------+
  |  KERNEL-MODE DRIVERS (ring 0)                                    |
  |  WDM/KMDF drivers, filter drivers, miniport drivers              |
  +------------------------------------------------------------------+
  |  HAL (Hardware Abstraction Layer)                                 |
  |  hal.dll — normalizes chipset/ACPI/interrupt controller diffs     |
  +------------------------------------------------------------------+
  |  UEFI / FIRMWARE                                                 |
  +------------------------------------------------------------------+
  |  HARDWARE                                                        |
  +------------------------------------------------------------------+

Key design principle: Windows NT is a hybrid kernel.
"Executive" services run in ring 0 but are structured as loosely coupled
managers communicating through object handles — not a true microkernel,
but not a monolith either. Dave Cutler's VAX/VMS heritage shows here.
```

---

## Section 1 — NT Kernel Architecture: Quick Orientation

You know this. This is the 2-minute calibration of what changed.

```
Ring Model on Windows
=====================

  Ring 3 (User Mode)              Ring 0 (Kernel Mode)
  ──────────────────              ────────────────────
  Your app                        ntoskrnl.exe
  .NET CLR                        hal.dll
  Win32 DLLs (kernel32, user32)  win32k.sys
  CSRSS (console subsystem)       KM drivers
  LSASS (auth subsystem)
  Services.exe

  Crossing the boundary = syscall (INT 2Eh / SYSFAST)
  Expensive: the .NET JIT batch-groups P/Invoke calls to minimize crossings.
```

```
Object Handle Model — the kernel's universal glue
==================================================

  All kernel resources are Objects: processes, threads, files,
  mutexes, events, sections, tokens, I/O completion ports.

  User mode gets a HANDLE (index into per-process handle table).
  Kernel Object Manager maintains reference counts.
  CloseHandle → decrements refcount → GC'd when zero.

  This is literally .NET's IDisposable/SafeHandle story,
  but at the kernel level. SafeHandle wraps a HANDLE.
```

### Win32 → WinRT → WinUI layering

```
API Genealogy
=============

  1985  Win16 (16-bit, segmented memory, Windows 1.x–3.x)
          │
  1993  Win32 (flat 32-bit, NT 3.1) — THE stable ABI
          │
  2002  .NET 1.0 / CLR — managed wrapper over Win32
          │         │
          │    WinForms (Win32 wrappers)
          │         │
  2006  WPF (milcore/DirectX-backed, XAML, separate from Win32 GDI)
          │
  2012  WinRT (COM-based, projectable to C++/C#/JS, UWP sandboxed)
          │
  2021  WinApp SDK + WinUI 3
          Decoupled from OS shipping cycle
          WinRT APIs without UWP sandbox
          Works in packaged or unpackaged mode
          │
        MAUI (.NET 6+)
          Cross-platform: Windows/Mac/iOS/Android
          Wraps WinUI 3 on Windows
```

### PE Format & DLL Evolution

```
PE (Portable Executable) Format — still the same since NT 3.1
==============================================================

  PE Header
  ├─ DOS stub ("This program cannot be run in DOS mode")
  ├─ COFF Header (machine type, section count, timestamp)
  ├─ Optional Header (ImageBase, EntryPoint, Subsystem: GUI/CUI)
  └─ Section Table
      ├─ .text   — executable code
      ├─ .rdata  — read-only data, import/export tables
      ├─ .data   — initialized globals
      ├─ .reloc  — base relocation table
      └─ .rsrc   — resources (icons, manifests, strings)

DLL Hell Problem → Side-by-Side Assemblies → MSIX
==================================================

  DLL Hell (Win9x era)
    "Last installer wins" — shared DLLs in System32
    App A needs msvcp.dll 6.0, App B installs 5.0 → App A breaks

  Side-by-Side (WinSxS) — XP/Vista
    Multiple versions in C:\Windows\WinSxS
    Manifest in PE says exactly which version to bind
    Fusion loader (SxS loader) resolves at runtime
    Problem: WinSxS bloat, complex manifests, still in-proc shared DLLs

  .NET GAC — same idea for managed assemblies
    C:\Windows\Microsoft.NET\assembly\GAC_MSIL\
    Strong-named assemblies, version-specific binding
    .NET Core/5+ killed the GAC — everything is local now

  MSIX (2018+)
    Container-like: app gets its own virtual file system + registry view
    Installed to C:\Program Files\WindowsApps\<package>\
    OS merges app's virtual FS with real FS at runtime
    Uninstall is clean — no registry/file debris
    AppX manifests declare capabilities, version, dependencies
    WinGet delivers MSIX packages
```

---

## Section 2 — Windows Desktop App Development: The Modern Picture

### The Full Genealogy

```
Desktop App Framework Timeline
================================

  2002  WinForms 1.0
        ├─ Win32 control wrappers (Button → CreateWindowEx("BUTTON"...))
        ├─ Designer-based, drag-drop UI
        ├─ GDI rendering
        ├─ Event model: delegates/events
        └─ Status 2024: SUPPORTED, shipping in .NET 8/9 on Windows only
                        Not deprecated. Massive enterprise install base.

  2006  WPF 3.0
        ├─ XAML markup + code-behind
        ├─ DirectX/milcore rendering (GPU-accelerated, independent of GDI)
        ├─ Data binding, styles, templates, animations
        ├─ MVVM pattern (INotifyPropertyChanged, ICommand)
        ├─ Dependency properties + routed events
        └─ Status 2024: SUPPORTED, shipping in .NET 8/9 on Windows only
                        Not deprecated. Best choice for rich desktop on Windows.

  2012  UWP / WinRT
        ├─ Sandboxed (AppContainer), store-only distribution
        ├─ WinRT APIs (COM projection)
        ├─ XAML UI (different namespace from WPF XAML)
        ├─ Fluent Design System
        └─ Status 2024: MAINTENANCE MODE — Microsoft moved on
                        Do not start new UWP projects.

  2021  WinUI 3 + WinApp SDK
        ├─ WinRT APIs decoupled from Windows shipping cycle (NuGet-distributed)
        ├─ Fluent Design, modern controls
        ├─ Packaged (MSIX) or Unpackaged (no sandbox, no store required)
        ├─ XAML Islands: embed WinUI 3 controls in WPF/WinForms
        └─ Status 2024: ACTIVE — Microsoft's strategic bet for new Windows UI

  2022  .NET MAUI (Multi-platform App UI)
        ├─ Successor to Xamarin.Forms
        ├─ Single codebase: Windows/macOS/iOS/Android
        ├─ Renders to native controls on each platform
        ├─ WinUI 3 on Windows, AppKit on macOS, UIKit on iOS
        └─ Status 2024: ACTIVE — best choice if cross-platform required
```

### WPF — What You Need to Remember

You know WPF. These are the pieces that matter for picking it back up in 2024.

```
WPF Architecture
================

  Your XAML + C#
         │
  ┌──────▼──────────────────────────────────┐
  │  PresentationFramework.dll              │
  │  Controls, data binding, MVVM support   │
  │  INotifyPropertyChanged, ObservableCollection│
  │  XAML parser → visual tree              │
  └──────┬──────────────────────────────────┘
         │
  ┌──────▼──────────────────────────────────┐
  │  milcore.dll (Media Integration Layer)  │
  │  Composition engine, animation, layout  │
  │  Retained-mode scene graph              │
  └──────┬──────────────────────────────────┘
         │
  ┌──────▼──────────────────────────────────┐
  │  DirectX / D3D                          │
  │  Actual GPU rendering                   │
  └─────────────────────────────────────────┘
```

```
MVVM Wiring in WPF (the pattern you know — quick recap)
=======================================================

  View (.xaml)              ViewModel (C#)           Model (C#)
  ────────────              ──────────────           ──────────
  DataContext = VM          : INotifyPropertyChanged  Domain objects
                            ObservableCollection<T>  Repository/service
  {Binding Property}   ◄──► public string Property   Business logic
  {Binding Command}    ◄──► ICommand SaveCommand
  DataTrigger, Style        RaisePropertyChanged()

Modern: Community Toolkit MVVM (NuGet: CommunityToolkit.Mvvm)
  [ObservableProperty]  → generates INPC boilerplate
  [RelayCommand]        → generates ICommand
  Source generators at build time — no reflection overhead.
```

### WinUI 3 + WinApp SDK — the Delta from WPF/UWP

```
WinApp SDK vs UWP vs WPF
========================

  Feature               WPF         UWP         WinUI 3 / WinApp SDK
  ─────────────────     ───         ───         ────────────────────
  Runs on .NET 8        YES         No          YES
  Runs unpackaged       YES         No          YES (unpackaged mode)
  MSIX packaging        Optional    Required    Optional
  Win32 API access      Full        Restricted  Full
  XAML dialect          WPF XAML    UWP XAML    WinUI XAML (≈ UWP)
  Fluent controls       Via library Built-in    Built-in (latest)
  XAML Islands          N/A         N/A         Host WinUI in WPF
  Shipping cadence      .NET cycle  OS cycle    NuGet (decoupled)
  Store distribution    Via Bridge  Native      Native
  Use for               Existing    Legacy      New UI projects
                        enterprise  (avoid)
```

### Packaging: msix vs installer vs winget

```
Distribution Options in 2024
=============================

  ┌────────────────┬──────────────────────────────────────────────────┐
  │ Method         │ Details                                          │
  ├────────────────┼──────────────────────────────────────────────────┤
  │ MSIX           │ Containerized install, clean uninstall, signed   │
  │                │ Required for Store. Supported by winget.         │
  │                │ .msixbundle for multi-arch. Best choice for new. │
  ├────────────────┼──────────────────────────────────────────────────┤
  │ Traditional    │ NSIS, WiX, InstallShield                         │
  │ Installer      │ Still valid for legacy apps, driver installs,    │
  │                │ anything needing deep system access              │
  ├────────────────┼──────────────────────────────────────────────────┤
  │ ClickOnce      │ .NET-era web-based deployment                    │
  │                │ Still works. Not recommended for new projects.   │
  ├────────────────┼──────────────────────────────────────────────────┤
  │ Portable       │ xcopy install — no installer at all              │
  │ (xcopy)        │ Works if app is fully self-contained             │
  │                │ dotnet publish --self-contained                  │
  ├────────────────┼──────────────────────────────────────────────────┤
  │ winget manifest│ YAML in winget-pkgs repo on GitHub               │
  │                │ Points to your installer/MSIX URL                │
  │                │ winget install YourApp.YourApp                   │
  └────────────────┴──────────────────────────────────────────────────┘
```

---

## Section 3 — Windows Services & Background Processing

### Windows Service Lifecycle

```
Windows Service Lifecycle
==========================

  SCM (Services Control Manager — services.exe)
         │
         │  StartService()
         ▼
  ┌──────────────────────────────────────────┐
  │  SERVICE_START_PENDING                   │
  │  OnStart() called — do setup, return fast│
  └──────────────────┬───────────────────────┘
                     │ SetServiceStatus(RUNNING)
                     ▼
  ┌──────────────────────────────────────────┐
  │  SERVICE_RUNNING                         │
  │  Main work happens on background threads │
  └──────┬──────────────────────────────────┘
         │ StopService() / shutdown
         ▼
  ┌──────────────────────────────────────────┐
  │  SERVICE_STOP_PENDING                    │
  │  OnStop() — signal threads, cleanup      │
  └──────────────────┬───────────────────────┘
                     ▼
              SERVICE_STOPPED

  Recovery Actions (per-failure config in SCM):
    First failure:   Restart the service
    Second failure:  Restart the service
    Subsequent:      Run a program / Reboot
```

### Worker Service — The Modern Replacement

```
Old World → New World: Windows Services
========================================

  Old World (.NET Framework)          New World (.NET 5+)
  ──────────────────────────          ──────────────────
  System.ServiceProcess               Microsoft.Extensions.Hosting
  ServiceBase derived class           IHostedService / BackgroundService
  OnStart() / OnStop()                StartAsync() / StopAsync()
  InstallUtil.exe to register         sc.exe create OR MSIX OR systemd
  App.config                          appsettings.json + IConfiguration
  Manual DI wiring                    Built-in DI (IServiceCollection)
  No cancellation token               CancellationToken throughout
```

```
Worker Service Pattern (.NET 6+)
=================================

  // Program.cs — the whole host setup
  IHost host = Host.CreateDefaultBuilder(args)
      .UseWindowsService()                    // SCM integration on Windows
      .ConfigureServices(services =>
      {
          services.AddHostedService<MyWorker>();
          services.AddSingleton<IMyService, MyService>();
      })
      .Build();

  await host.RunAsync();

  // MyWorker.cs
  public class MyWorker : BackgroundService
  {
      protected override async Task ExecuteAsync(CancellationToken ct)
      {
          while (!ct.IsCancellationRequested)
          {
              await DoWorkAsync();
              await Task.Delay(TimeSpan.FromMinutes(1), ct);
          }
      }
  }

  // Register with SCM:
  sc create MyWorker binpath= "C:\MyApp\MyWorker.exe"
  sc start MyWorker
```

### Service Account Types

```
Service Account Selection
==========================

  Account             Network Access   Local Privs   Use When
  ───────             ──────────────   ───────────   ────────
  LocalSystem         YES (machine)    FULL          Avoid — over-privileged
  LocalService        Limited          Low           No network needed
  NetworkService      YES (machine)    Low           Network, minimal local
  gMSA                YES              Configurable  Enterprise — BEST CHOICE
  (group Managed                                     Auto-rotating password
   Service Account)                                  No password mgmt burden
  Named user          YES (creds)      Configurable  Legacy, avoid if possible

  For new services in AD environments: always gMSA.
  gMSA setup: New-ADServiceAccount, Install-ADServiceAccount, set in SCM.
```

### Service Management Commands

```
Service Management
==================

  sc.exe (Win32)                   PowerShell equivalent
  ──────────────                   ─────────────────────
  sc query MyService               Get-Service MyService
  sc start MyService               Start-Service MyService
  sc stop  MyService               Stop-Service MyService
  sc config MyService start=auto   Set-Service MyService -StartupType Automatic
  sc failure MyService             (use sc.exe — no PS equivalent)
    reset=86400 actions=restart/5000
  sc delete MyService              Remove-Service MyService  (.NET 6 PS only)
  sc qc MyService                  Get-Service | Format-List *

  Dependencies:
    sc config MyService depend=MSSQLSERVER  (depends on SQL)
    sc config MyService depend=              (clear deps)
```

---

## Section 4 — PowerShell: The Real Windows CLI

### Shell Landscape

```
Shell Comparison
=================

  Shell            Type         Use When
  ─────            ────         ────────
  cmd.exe          Text pipe    Legacy scripts, batch files (.bat/.cmd)
                                Batch for loops, basic file ops
                                Fastest startup, always present

  PowerShell 5.1   Object pipe  Windows-only, built into Win10/11/Server
  (powershell.exe) .NET FW      Admin scripts, full WMI/COM access
                                All Windows admins have this

  PowerShell 7     Object pipe  Cross-platform (Win/Mac/Linux)
  (pwsh.exe)       .NET 8+      Install separately (winget/MSI)
                                New features, parallel foreach, etc.
                                Prefer for new scripts

  Git Bash         Text pipe    Git operations from a Unix-like env
  (bash via MSYS2) POSIX-ish    Not for Windows admin — weak Win integration

  WSL2 bash        Text pipe    Real Linux. Full Linux toolchain.
                                Build/test Linux targets on Windows
                                Docker, make, gcc, etc.

  Rule of thumb:
    Windows admin scripts   → PowerShell 7 (or 5.1 if portability needed)
    Git operations          → Git Bash or PowerShell
    Linux build toolchain   → WSL2
    Legacy automation       → cmd.exe batch (maintain, don't write new)
```

### Object Pipeline — the key insight

```
PowerShell Object Pipeline vs Bash Text Pipeline
=================================================

  Bash (text):                     PowerShell (objects):
  ────────────                     ─────────────────────
  ps aux | grep myapp              Get-Process | Where-Object Name -eq myapp
  | awk '{print $2}'               | Select-Object Id, CPU, WorkingSet

  ps aux outputs TEXT              Get-Process outputs Process[] objects
  grep does text matching          Where-Object filters on .Name property
  awk parses column positions      Select-Object picks properties by name

  Bash: fragile to column changes  PowerShell: schema-stable, type-safe

  Practical consequence:
    $procs = Get-Process | Where CPU -gt 10
    $procs[0].Id                    # direct property access, no parsing
    $procs | Stop-Process           # pipe objects directly to next cmdlet
```

### Essential Command Reference

```
Process & System
  Get-Process                      # all processes (like tasklist)
  Get-Process -Name chrome         # filter by name
  Stop-Process -Id 1234
  Stop-Process -Name notepad -Force
  Start-Process notepad.exe
  Start-Process cmd -Verb RunAs    # run elevated (UAC prompt)

Services
  Get-Service                      # all services
  Get-Service -Name W32Time
  Start-Service W32Time
  Stop-Service W32Time
  Restart-Service W32Time
  Set-Service W32Time -StartupType Disabled

Files & Paths
  Test-Path C:\Logs\app.log        # returns $true/$false
  Get-Item C:\Logs\app.log
  Get-ChildItem C:\Logs -Recurse -Filter *.log
  New-Item -Path C:\Logs -Name app.log -ItemType File
  Remove-Item C:\Logs\old.log
  Copy-Item src.txt dest.txt
  Move-Item old.txt new.txt
  Get-Content C:\Logs\app.log      # like cat
  Get-Content app.log -Tail 50     # like tail -n 50
  Select-String "ERROR" app.log    # like grep

Network
  Get-NetIPAddress                 # all IPs (like ipconfig)
  Get-NetIPAddress -AddressFamily IPv4
  Test-NetConnection google.com -Port 443   # like telnet
  Test-NetConnection google.com -TraceRoute # like tracert
  Resolve-DnsName google.com
  Get-NetTCPConnection -State Listen        # like netstat -an | grep LISTEN

Registry
  Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
  Set-ItemProperty HKLM:\... -Name MyVal -Value "data"
  New-Item HKLM:\SOFTWARE\MyApp
  Remove-ItemProperty HKLM:\SOFTWARE\MyApp -Name OldVal

Events
  Get-EventLog -LogName Application -Newest 50
  Get-WinEvent -LogName Application -MaxEvents 50
  Get-WinEvent -FilterHashtable @{LogName='System'; Level=2; StartTime=(Get-Date).AddHours(-24)}

Misc
  $PSVersionTable                  # version info
  Get-ExecutionPolicy
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  Get-Command *process*            # discover commands
  Get-Help Get-Process -Examples
  Get-Member                       # inspect object properties: $proc | Get-Member
```

### Remoting

```
PowerShell Remoting
===================

  Prerequisites:
    Enable-PSRemoting         # on target machine (sets up WinRM)
    # Firewall rule: TCP 5985 (HTTP) or 5986 (HTTPS)

  Interactive session:
    Enter-PSSession -ComputerName server01
    Enter-PSSession -ComputerName server01 -Credential domain\user
    exit  # to leave

  Run command remotely:
    Invoke-Command -ComputerName server01 -ScriptBlock { Get-Service }
    Invoke-Command -ComputerName srv1,srv2,srv3 -ScriptBlock { ... }  # parallel

  Persistent session:
    $s = New-PSSession -ComputerName server01
    Invoke-Command -Session $s -ScriptBlock { $x = 5 }
    Invoke-Command -Session $s -ScriptBlock { $x * 2 }   # $x persists
    Remove-PSSession $s
```

### PowerShell 5.1 vs 7 Differences

```
PS 5.1 vs PS 7 — What Changed
==============================

  Feature                  PS 5.1              PS 7
  ─────────────────────    ──────              ────
  Runtime                  .NET Framework 4.x  .NET 8+
  OS                       Windows only        Win/Mac/Linux
  Startup exe              powershell.exe      pwsh.exe
  Parallel ForEach         Runspaces (manual)  ForEach-Object -Parallel
  Null coalescing          No                  $x ??= 'default'
  Ternary operator         No                  $a ? $b : $c
  Pipeline chain ops       No                  cmd && cmd || cmd
  ErrorView                CategoryView        ConciseView (cleaner)
  PSReadLine               Optional            Built-in
  SSH remoting             No                  Yes (SSH transport)
  COM object access        Full                Full
  WMI (Get-WmiObject)      Yes                 Use Get-CimInstance instead
  Module compat            Full Windows        Some Win-only modules work via
                                               Windows Compatibility layer

  In your scripts: prefer Get-CimInstance over Get-WmiObject.
  CimCmdlets work in both 5.1 and 7.
```

---

## Section 5 — WSL2: Linux on Windows

### Architecture

```
WSL2 Architecture
==================

  Windows Host
  ┌───────────────────────────────────────────────────────┐
  │                                                       │
  │   Windows processes     Hyper-V Utility VM            │
  │   ┌─────────────┐       ┌──────────────────────────┐  │
  │   │ VS Code     │       │  Real Linux kernel        │  │
  │   │ Docker Desk │◄─────►│  (Microsoft fork of       │  │
  │   │ Windows app │  9P   │   mainline kernel)        │  │
  │   └─────────────┘  FS   │                           │  │
  │                    proto│  Ubuntu / Debian / etc.   │  │
  │   ┌─────────────┐       │  (full distro userland)   │  │
  │   │ wsl.exe     │       │                           │  │
  │   └──────┬──────┘       │  /mnt/c → Windows C:\    │  │
  │          │  shell →     └──────────────────────────┘  │
  │          └──────────────────────────────────────────►  │
  │                                                       │
  └───────────────────────────────────────────────────────┘

  Key facts:
  - Real Linux kernel (not a compatibility layer like WSL1)
  - Full syscall compatibility (unlike WSL1 which translated syscalls)
  - Separate network namespace (has its own IP on 172.x.x.x)
  - Windows ↔ Linux filesystem access via Plan 9 (9P) protocol
  - WSLg: Wayland/X11 server built into Windows for GUI apps
```

### Filesystem Performance Caveat

```
WSL2 Filesystem Access — Know This
====================================

  Scenario                      Performance    Recommendation
  ────────                      ───────────    ──────────────
  Linux files in WSL2            Fast           ~/projects/ — keep here
  (ext4 inside the VHDX)

  Windows files via /mnt/c       SLOW           Avoid for build output
  (9P network protocol)          (~3-5x slower) Don't put node_modules here

  Windows files via \\wsl$\     Reasonable     OK for occasional access
  (Windows accessing WSL2 FS)    Fast reads

  Rule: If you're doing Linux builds, keep the source in WSL2 filesystem.
  Only use /mnt/c for git checkout if your Windows tools also need the files.
```

### Essential WSL Commands

```
WSL Management (run from Windows PowerShell/cmd)
=================================================

  wsl                          # launch default distro
  wsl -d Ubuntu-22.04          # launch specific distro
  wsl --list --verbose         # list distros + state + version
  wsl --list --online          # available distros from store
  wsl --install Ubuntu-22.04   # install a distro
  wsl --shutdown               # stop all running distros
  wsl --terminate Ubuntu       # stop specific distro
  wsl --export Ubuntu ubuntu.tar    # backup
  wsl --import Ubuntu C:\wsl ubuntu.tar  # restore
  wsl --set-version Ubuntu 2        # upgrade WSL1→WSL2
  wsl --set-default-version 2       # new installs default to WSL2
  wsl --update                      # update WSL kernel

  From inside WSL2:
  explorer.exe .               # open Windows Explorer in current Linux dir
  notepad.exe myfile.txt       # open Windows app on Linux file
  /mnt/c/Windows/System32/...  # access Windows executables
  wslpath -w ~/projects        # convert WSL path to Windows path
```

### Docker Desktop + WSL2

```
Docker Desktop WSL2 Backend
============================

  Old (Hyper-V backend):         New (WSL2 backend):
  ──────────────────────         ──────────────────
  Separate Hyper-V VM            Docker engine runs inside WSL2 VM
  4GB+ RAM reserved upfront      Memory dynamically allocated
  Slow filesystem mounts         Linux containers mount from WSL2 FS (fast)
  Poor Linux compat              Full Linux kernel compatibility

  After enabling WSL2 backend in Docker Desktop:
    - Docker daemon runs in WSL2
    - docker CLI works from both Windows PowerShell AND WSL2 bash
    - docker run mounts volumes faster (staying in Linux FS)
    - Named distros can use Docker: wsl --list shows docker-desktop VMs
```

### WSL2 vs Alternatives

```
Which Shell/Environment To Use
================================

  Need                              Use
  ────                              ───
  Windows admin scripting           PowerShell 7
  Run Linux build tools (make,gcc)  WSL2
  Git on Windows                    Git for Windows (git bash) or WSL2
  Docker containers (Linux)         Docker Desktop + WSL2 backend
  POSIX scripting on Windows        WSL2 (bash in Linux)
  Cross-compile for Linux           WSL2
  Windows-only tools (MSBuild etc)  Windows PowerShell / native
  Port Unix scripts to Windows      WSL2 — don't port, just run there
  Terminal emulator                 Windows Terminal (tabbed, all shells)
```

---

## Section 6 — Windows Security Model

### Token Anatomy

```
Access Token — What "who are you" means to the kernel
=======================================================

  Every process/thread has an access token (kernel object).

  Token fields:
  ┌─────────────────────────────────────────────────────────┐
  │  User SID        S-1-5-21-<domain>-<RID>               │
  │  Group SIDs      [Domain Users, Administrators, ...]    │
  │  Privileges      [SeDebugPrivilege, SeShutdownPrivilege] │
  │  Integrity Level [Low | Medium | High | System]          │
  │  Session ID      1 (interactive) or 0 (services)        │
  │  LogonSession    reference to logon session in LSASS    │
  │  Token Type      Primary (process) or Impersonation     │
  └─────────────────────────────────────────────────────────┘

  SID anatomy:  S-1-5-21-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXX-RID
                  │ │  │  └──────────────────────────────────── domain
                  │ │  └─ NT Authority identifier
                  │ └── revision (always 1)
                  └─ SID prefix

  Well-known SIDs:
    S-1-5-18    LocalSystem
    S-1-5-19    LocalService
    S-1-5-20    NetworkService
    S-1-1-0     Everyone
    S-1-5-32-544  BUILTIN\Administrators
```

### UAC Flow

```
UAC: Filtered Token vs Linked Token
=====================================

  User logs in as local Administrator:

  LSASS creates TWO tokens:
  ┌─────────────────────────┐   ┌─────────────────────────┐
  │  Filtered Token         │   │  Full Token (linked)    │
  │  ─────────────          │   │  ──────────────────      │
  │  Admin SID stripped     │   │  Admin SID present      │
  │  Privileges stripped    │   │  All privileges         │
  │  Integrity: Medium      │   │  Integrity: High        │
  └──────────┬──────────────┘   └──────────┬──────────────┘
             │ used by default              │ used after consent prompt
             ▼                              ▼
      Normal processes               Elevated processes
      (Explorer, apps)               (mmc.exe, regedit as admin)

  When you click "Run as Administrator":
    AppInfo service receives request
    Credential/consent prompt (consent.exe on secure desktop)
    User approves → full token used for new process
    Full token = High integrity level

  Why integrity levels matter:
    Low   = IE Protected Mode, sandboxed processes
    Medium = normal user apps
    High  = admin apps (after UAC)
    System = services, kernel drivers

  A Medium integrity process CANNOT write to a High integrity process's memory.
  This is why malware injecting into elevated processes requires UAC bypass.
```

### LSASS and Credential Security

```
LSASS (Local Security Authority Subsystem Service)
===================================================

  What it holds:
  ┌────────────────────────────────────────────────────────┐
  │  LSA process (lsass.exe)                               │
  │  ├─ Kerberos tickets (TGT + service tickets)           │
  │  ├─ NTLM hashes (WDigest when enabled — legacy)        │
  │  ├─ Logon sessions (linked to tokens)                  │
  │  ├─ Cached credentials (domain logon cache)            │
  │  └─ LSA secrets (service account passwords, etc.)      │
  └────────────────────────────────────────────────────────┘

  Mimikatz attack: dump LSASS memory → extract cleartext creds
    sekurlsa::logonpasswords   (WDigest — requires WDigest enabled)
    sekurlsa::tickets          (Kerberos tickets — pass-the-ticket)
    lsadump::sam               (local SAM hashes)

  Defenses:
  ┌──────────────────────────────────────────────────────────────┐
  │  Credential Guard (Win10 1511+)                              │
  │  ──────────────────────────────                              │
  │  Moves credential material into isolated VBS (Virtualization │
  │  Based Security) container — separate Hyper-V partition.     │
  │  LSASS runs as "protected process" — no memory read even as  │
  │  SYSTEM. Kerberos/NTLM hashes never in normal kernel memory. │
  │                                                              │
  │  PPL (Protected Process Light) for LSASS                     │
  │  Prevents even admin processes from injecting into LSASS.    │
  │  Set via: HKLM\SYSTEM\CurrentControlSet\Control\Lsa          │
  │           RunAsPPL = 1                                       │
  └──────────────────────────────────────────────────────────────┘
```

### Windows Defender & Code Integrity

```
Windows Defender Stack
=======================

  ┌─────────────────────────────────────────────────────────┐
  │  Microsoft Defender Antivirus (MDAV)                    │
  │  Real-time file scan (AMSI), cloud-based detonation     │
  ├─────────────────────────────────────────────────────────┤
  │  Attack Surface Reduction (ASR) Rules                   │
  │  Block Office macros spawning child processes           │
  │  Block credential stealing from LSASS                   │
  │  Block unsigned executables from USB/network            │
  │  ~20 rules — configurable via Intune/GP/PowerShell      │
  ├─────────────────────────────────────────────────────────┤
  │  WDAC (Windows Defender Application Control)            │
  │  Kernel-level code integrity policy                     │
  │  Replaces AppLocker (more secure — can't be bypassed by │
  │  admin without reboot)                                  │
  │  Allow-list: only signed/known code runs                │
  │  Policy files: .xml → compiled .p7b → deployed via GP   │
  ├─────────────────────────────────────────────────────────┤
  │  Secure Boot + UEFI firmware protection                 │
  │  VBS (Virtualization Based Security)                    │
  │  HVCI (Hypervisor-Protected Code Integrity)             │
  └─────────────────────────────────────────────────────────┘

  ASR rule quick deploy (PowerShell, MDE/Intune):
    Set-MpPreference -AttackSurfaceReductionRules_Ids <GUID> `
                     -AttackSurfaceReductionRules_Actions Enabled
```

### Windows Hello for Business

```
WHfB — FIDO2 on Windows
========================

  Traditional password auth:
    User → LSASS → DC (Kerberos AS-REQ with password hash)
    Password hash in memory → Mimikatz risk

  WHfB auth:
    User → PIN/biometric unlocks TPM-bound private key
    TPM creates signature → presented to DC as Kerberos proof
    Private key NEVER leaves TPM → no hash in memory
    PIN is local gesture, not transmitted anywhere

  Deployment: Azure AD joined or Hybrid (requires PKI for hybrid)
  Hardware: TPM 2.0 required (all Win11 devices have this)

  For your environment (Microsoft IT): already deployed, you're using it.
  When building enterprise apps: don't force password auth — rely on
  Windows-integrated auth (Negotiate/Kerberos) which WHfB satisfies.
```

### Group Policy / Intune

```
Enterprise Management Layer
============================

  Group Policy (on-prem / hybrid)      Intune (cloud / MDM)
  ─────────────────────────────        ─────────────────────
  AD-backed, GPO objects               Entra ID backed
  Machine + User policy                Machine + User policy
  Applies at logon / refresh (90min)   Applies via MDM check-in
  gpedit.msc (local)                   portal.azure.com
  gpupdate /force                      Sync-MDMPolicy (PowerShell)
  gpresult /r                          Intune Management Extension logs
  Thousands of settings                Subset + custom OMA-URI/ADMX
  LAPS integration (on-prem LAPS)      LAPS cloud (2023)

  Reading applied policy:
    gpresult /h report.html            # full HTML policy report
    rsop.msc                           # Resultant Set of Policy GUI
    Get-GPResultantSetOfPolicy         # PowerShell
```

---

## Section 7 — Registry Deep Dive

### Hive Files on Disk

```
Registry Hive → File Mapping
==============================

  Registry Hive          File on Disk
  ─────────────────      ─────────────────────────────────────────────
  HKLM\SAM               C:\Windows\System32\config\SAM
  HKLM\SECURITY          C:\Windows\System32\config\SECURITY
  HKLM\SOFTWARE          C:\Windows\System32\config\SOFTWARE
  HKLM\SYSTEM            C:\Windows\System32\config\SYSTEM
  HKLM\HARDWARE          In-memory only (rebuilt at boot from hardware scan)
  HKU\.DEFAULT           C:\Windows\System32\config\DEFAULT
  HKU\<SID>              C:\Users\<username>\NTUSER.DAT
  HKCU                   Alias → HKU\<current-user-SID>
  HKCR                   Merged view: HKLM\SOFTWARE\Classes + HKCU\SOFTWARE\Classes

  Files are in proprietary binary format (not text).
  reg.exe export → .reg file (text representation)
  Offline access: reg load, reg unload (mount foreign hive)
    reg load HKLM\TEMP C:\Users\olduser\NTUSER.DAT
    reg query HKLM\TEMP\...
    reg unload HKLM\TEMP
```

### What Lives Where

```
HKLM vs HKCU vs HKCR
======================

  HKLM (HKEY_LOCAL_MACHINE) — machine-wide
  ├─ HARDWARE\    — current hardware (volatile, rebuilt at boot)
  ├─ SAM\         — local accounts DB (only accessible as SYSTEM)
  ├─ SECURITY\    — LSA secrets, policy (only accessible as SYSTEM)
  ├─ SOFTWARE\    — machine-wide app settings, installed software
  │   ├─ Microsoft\Windows NT\CurrentVersion\  — OS info, ProfileList
  │   ├─ Microsoft\Windows\CurrentVersion\Run\ — system-wide autostart
  │   └─ Classes\  — machine-wide COM registration, file associations
  └─ SYSTEM\      — device drivers, services, boot config
      └─ CurrentControlSet\Services\ — every service/driver config

  HKCU (HKEY_CURRENT_USER) — per-user, maps to NTUSER.DAT
  ├─ SOFTWARE\    — per-user app settings
  ├─ SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ — user autostart
  ├─ SOFTWARE\Classes\  — per-user file associations (overrides HKLM)
  └─ Environment\ — user environment variables

  HKCR (HKEY_CLASSES_ROOT) — merged view
    Read:  merge of HKCU\SOFTWARE\Classes over HKLM\SOFTWARE\Classes
    Write: goes to HKCU\SOFTWARE\Classes (UAC protected)
    Used for: COM ProgID lookup, file extension handlers
```

### Registry Virtualization and WOW64

```
Two Important Redirections
===========================

  1. UAC Registry Virtualization (Vista+)
     ─────────────────────────────────────
     Non-elevated 32/64-bit apps writing to HKLM\SOFTWARE get
     silently redirected to:
       HKCU\SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\

     The app thinks it wrote to HKLM but actually wrote to HKCU.
     Purpose: old apps that assumed they ran as admin still work.
     Applies only to legacy apps without a requestedExecutionLevel
     manifest. Any app with a manifest gets real access denied.

  2. WOW64 Registry Redirection (32-bit apps on 64-bit Windows)
     ─────────────────────────────────────────────────────────────
     32-bit process writes to HKLM\SOFTWARE → redirected to:
       HKLM\SOFTWARE\Wow6432Node\

     64-bit process writes to HKLM\SOFTWARE → goes to real path

     Why: 32-bit and 64-bit COM registrations need to coexist.

     Gotcha: If your build pipeline runs 32-bit MSBuild and reads
     registry for a 64-bit installed tool, it may find nothing.
     Fix: explicitly open Wow6432Node or use RegOpenKeyEx with
     KEY_WOW64_64KEY flag.

     Shared keys (not redirected): HKLM\SYSTEM, HKLM\HARDWARE,
     HKLM\SOFTWARE\Microsoft\Windows NT
```

### Autostart Locations

```
Autostart Registry Keys — Admin + Security Awareness
======================================================

  Key                                                    Scope
  ───                                                    ─────
  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run    Machine (all users)
  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce Machine (runs once, deletes)
  HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run    User
  HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce User (runs once, deletes)
  HKLM\SYSTEM\CurrentControlSet\Services                Services + drivers
  HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\
    Winlogon\Shell                                       Shell (default: explorer.exe)
    Winlogon\Userinit                                    Logon script
  HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\
    Explorer\Shell Folders                               User shell folders

  Tooling:
    Autoruns (Sysinternals) — the definitive tool to see everything
    that runs at startup across all these locations + services + tasks

  PowerShell check:
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    Get-ItemProperty "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
```

### Registry Commands

```
Registry CLI Tools
==================

  reg.exe (built-in):
    reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion /v ProductName
    reg add HKCU\SOFTWARE\MyApp /v Setting /t REG_SZ /d "value" /f
    reg delete HKCU\SOFTWARE\MyApp /v OldSetting /f
    reg export HKCU\SOFTWARE\MyApp backup.reg
    reg import backup.reg
    reg load HKLM\TEMP ntuser.dat      # mount foreign hive
    reg unload HKLM\TEMP

  PowerShell:
    Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
    Get-ItemPropertyValue HKLM:\SOFTWARE\... -Name ProductName
    Set-ItemProperty HKCU:\SOFTWARE\MyApp -Name Setting -Value "value"
    New-ItemProperty HKCU:\SOFTWARE\MyApp -Name New -Value 1 -PropertyType DWORD
    Remove-ItemProperty HKCU:\SOFTWARE\MyApp -Name Old
    New-Item HKCU:\SOFTWARE\MyApp -Force    # create key
    Remove-Item HKCU:\SOFTWARE\MyApp -Recurse -Force  # delete key tree

  Note: PowerShell registry path uses : not \ before the hive:
    HKLM:\ not HKLM\  (the : makes it a PSDrive)
```

---

## Section 8 — Windows Event Log & ETW

### Event Log Architecture

```
Windows Event Log Architecture
================================

  ┌──────────────────────────────────────────────────────────┐
  │                  Event Log Consumers                      │
  │   Event Viewer  wevtutil  Get-WinEvent  SIEM/Splunk      │
  └───────────────────────────┬──────────────────────────────┘
                              │  Windows Event Log API
  ┌───────────────────────────▼──────────────────────────────┐
  │                  Windows Event Log Service                │
  │   Manages .evtx files, subscriptions, forwarding         │
  └───────────────────────────┬──────────────────────────────┘
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
  ┌────────────────┐  ┌────────────────┐  ┌────────────────────────────┐
  │ Windows Logs   │  │ App & Services │  │ ETW Providers              │
  │ ─────────────  │  │ Logs           │  │ ─────────────              │
  │ Application    │  │ ─────────────  │  │ .NET CLR, ASPNET,          │
  │ Security       │  │ Microsoft/     │  │ WinHTTP, DNS Client,       │
  │ System         │  │ Windows/...    │  │ Kernel, Storage, etc.      │
  │ Setup          │  │ PowerShell     │  │                            │
  │ Forwarded      │  │ TaskScheduler  │  │ Write-EventLog /           │
  │ Events         │  │ DHCP Client    │  │ EventSource (managed)      │
  └────────────────┘  └────────────────┘  └────────────────────────────┘

  .evtx file location: C:\Windows\System32\winevt\Logs\
  Security log size: check + set via Event Viewer → Log Properties
  Security audit: gpedit → Security Settings → Advanced Audit Policy
```

### ETW — Event Tracing for Windows

```
ETW Architecture — the instrumentation substrate
==================================================

  ┌──────────────────────────────────────────────────────────┐
  │  ETW PROVIDER (writes events)                            │
  │  .NET: EventSource derived class                         │
  │  Native: TRACELOGGING_DECLARE_PROVIDER or classic ETW    │
  │  Kernel: built-in providers (Process, Thread, Disk, etc.)│
  └────────────────────────┬─────────────────────────────────┘
                           │ ETW kernel buffer (per-CPU ring buffers)
  ┌────────────────────────▼─────────────────────────────────┐
  │  ETW SESSION (what you create to collect)                │
  │  xperf, PerfView, logman, WPR                            │
  │  Circular buffer or file mode                            │
  └────────────────────────┬─────────────────────────────────┘
                           │
  ┌────────────────────────▼─────────────────────────────────┐
  │  ETW CONSUMER (reads / analyzes)                         │
  │  PerfView — .NET GC/JIT/allocations, thread time         │
  │  WPA (Windows Performance Analyzer) — system-wide        │
  │  xperf / xperfview — low-level kernel events             │
  │  Your code via TraceEvent NuGet                          │
  └──────────────────────────────────────────────────────────┘

  Real-time production tracing: zero allocation when disabled.
  ETW events are dropped if no session subscribes — no overhead.
```

### PerfView for .NET Analysis

```
PerfView Quick Reference
=========================

  Download: github.com/microsoft/perfview (free, Microsoft tool)
  PerfView is the definitive .NET performance tool — ETW-based.

  Collect a trace:
    Collect → Accept (30-60 sec capture) → Stop

  What to look at:
    GC Heap Alloc Stacks   → where are you allocating?
    Thread Time Stacks     → where is wall-clock time going?
    JIT Stats              → startup JIT cost
    GC Stats               → GC pause times, Gen0/1/2 counts
    Events                 → raw ETW events

  CPU sampling:
    Events → CPU Stacks → flame graph via "Flame Graph" button

  Memory investigation:
    Memory → Heap Snapshots (requires snapshot collection)
    Memory → GC Heap Alloc Stacks (allocation traces)

  For production profiling without stopping the process:
    dotnet-trace (built into .NET SDK):
      dotnet trace collect -p <PID> --profile gc-verbose
      dotnet trace convert --format Speedscope trace.nettrace
```

### Event Log Commands

```
Event Log Commands
==================

  wevtutil (built-in, XML-aware):
    wevtutil el                              # enumerate logs
    wevtutil gl Application                  # get log config
    wevtutil qe Application /c:10 /f:text   # query last 10 events
    wevtutil qe Security /q:"*[System[EventID=4624]]" /f:text  # XPath
    wevtutil cl Application                  # clear log (admin)
    wevtutil epl Application C:\backup.evtx # export log

  PowerShell (Get-WinEvent — preferred over Get-EventLog):
    # Last 50 errors from System log:
    Get-WinEvent -LogName System -MaxEvents 50 |
        Where-Object LevelDisplayName -eq Error

    # Filter by time + event ID:
    $filter = @{
        LogName   = 'Security'
        Id        = 4624           # successful logon
        StartTime = (Get-Date).AddHours(-1)
    }
    Get-WinEvent -FilterHashtable $filter

    # All Application errors in last hour:
    Get-WinEvent -FilterHashtable @{
        LogName = 'Application'
        Level = 2  # Error
        StartTime = (Get-Date).AddHours(-1)
    } | Select-Object TimeCreated, ProviderName, Message

    # Search message text:
    Get-WinEvent -LogName Application |
        Where-Object Message -match "connection refused"
```

### Modern .NET Logging → ETW

```
Microsoft.Extensions.Logging → ETW
=====================================

  In .NET apps (ASP.NET, Worker Service):

  // Program.cs
  builder.Logging.AddEventLog(settings =>
  {
      settings.SourceName = "MyApp";    // creates source in Application log
  });

  // Or ETW provider via EventSource:
  [EventSource(Name = "MyCompany-MyApp")]
  class AppEventSource : EventSource
  {
      public static readonly AppEventSource Log = new();

      [Event(1, Level = EventLevel.Informational)]
      public void RequestStart(string path) =>
          WriteEvent(1, path);
  }

  // Consume with PerfView or dotnet-trace during development.
  // In production: forward Windows Event Log to Azure Monitor.

  Azure Monitor → Windows Event Log forwarding:
    Azure Monitor Agent (AMA) replaces MMA/OMS agent
    Data Collection Rule (DCR) specifies which logs to ship
    Destination: Log Analytics Workspace
    Query: KQL in Azure Monitor Logs
```

---

## Section 9 — Windows Networking

### Network Stack Architecture

```
Windows Network Stack
======================

  User Mode                          Kernel Mode
  ─────────                          ────────────
  Your app (WinSock API)             AFD.sys (Ancillary Function Driver)
  ws2_32.dll (WinSock 2)      ───►   TCPIP.sys (TCP/IP stack)
  mswsock.dll (WinSock SPI)          NDIS (Network Driver Interface)
                                     NIC Driver
  Named Pipes:
  kernel32.dll (CreateNamedPipe)     NPFS.sys (Named Pipe FS)

  HTTP.sys (kernel HTTP stack):
  Used by IIS, WCF, HttpListener, ASP.NET Core (Kestrel delegates to OS TLS)
  Allows multiple apps to share port 80/443 via URL reservation:
    netsh http add urlacl url=http://+:8080/ user=DOMAIN\svcaccount
```

### Named Pipes and AF_UNIX

```
IPC Options on Modern Windows
===============================

  Mechanism        Where        Use
  ─────────        ─────        ───
  Named Pipes      \\.\pipe\    Traditional Windows IPC, fast same-machine
                                Cross-process, language-neutral
                                Used by SQL Server, ADO.NET local connections

  AF_UNIX sockets  Since 1803   POSIX-compatible unix domain sockets
                                Works between WSL2 and Windows processes
                                Same API as Linux — no refactoring needed

  gRPC via TCP     Loopback     Modern IPC, proto3, cross-language
                                Slightly more overhead than named pipes
                                But: streaming, bidirectional, .NET/Java/Go all speak it

  Memory-Mapped    Section obj  Shared memory, fastest for large data
  Files            (kernel)     Use with Mutex/EventWaitHandle for signaling

  WCF was often named pipes locally — gRPC is the modern replacement for that.
```

### Key Network Diagnostics

```
Network Diagnostics Commands
=============================

  IP configuration:
    Get-NetIPAddress                              # all adapters, all IPs
    Get-NetIPAddress -AddressFamily IPv4          # IPv4 only
    Get-NetAdapter                                # adapter list + status
    ipconfig /all                                 # old-school, still useful
    ipconfig /flushdns                            # flush DNS resolver cache
    ipconfig /displaydns                          # show cached DNS entries

  Connectivity testing:
    Test-NetConnection google.com                 # ICMP ping test
    Test-NetConnection 10.0.0.1 -Port 1433        # TCP port test (like telnet)
    Test-NetConnection google.com -TraceRoute      # tracert
    Resolve-DnsName myserver.contoso.com           # DNS lookup
    nslookup myserver.contoso.com 8.8.8.8         # DNS query specific server

  Active connections:
    Get-NetTCPConnection                          # all TCP connections
    Get-NetTCPConnection -State Listen            # listening ports
    Get-NetTCPConnection -LocalPort 5000          # specific port
    netstat -ano                                  # old-school with PIDs

  Route table:
    Get-NetRoute                                  # routing table
    route print                                   # old-school

  Packet capture:
    netsh trace start capture=yes                 # built-in capture (.etl)
    netsh trace stop                              # produces .etl + .cab
    # Convert: Convert .etl with Message Analyzer (deprecated) or Wireshark
    # Wireshark is better: install + run directly
```

### Windows Firewall

```
Windows Firewall Architecture
==============================

  Profiles:
    Domain   — applies when connected to corporate domain network
    Private  — home/trusted network
    Public   — untrusted network (coffee shop wifi)

  Each profile has independent inbound/outbound rule sets.
  Rules evaluated top-down, first match wins.

  PowerShell management:
    # Show all enabled inbound rules:
    Get-NetFirewallRule -Direction Inbound -Enabled True |
        Select DisplayName, Action, Profile

    # Create inbound allow rule:
    New-NetFirewallRule -DisplayName "Allow MyApp" `
        -Direction Inbound -Protocol TCP `
        -LocalPort 8080 -Action Allow `
        -Profile Domain,Private

    # Block outbound by default, allow specific:
    Set-NetFirewallProfile -Profile Domain -DefaultOutboundAction Block

    # Test if rule blocks a port:
    Test-NetConnection -ComputerName localhost -Port 8080

  netsh (old-school, still useful in scripts):
    netsh advfirewall show allprofiles state
    netsh advfirewall firewall add rule name="MyApp" `
        dir=in action=allow protocol=TCP localport=8080
```

### Proxy Configuration

```
WINHTTP vs WININET Proxy — the gotcha
========================================

  WININET (Internet Explorer / WinINet stack):
    Used by: IE, old COM-based HTTP, .NET Framework HttpWebRequest (partially)
    Config:  Internet Options → Connections → LAN Settings
             or: netsh winhttp import proxy source=ie (copies IE settings to WinHTTP)
    Registry: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings

  WINHTTP (lower-level Windows HTTP):
    Used by: WinUpdate, BITS, .NET Core HttpClient (on Windows via WinHttpHandler)
             Some enterprise tools, WSUS, etc.
    Config:  netsh winhttp set proxy proxy-server="http=myproxy:8080"
             netsh winhttp show proxy
             netsh winhttp reset proxy

  .NET Core / .NET 5+ HttpClient:
    Uses WINHTTP on Windows by default
    Respects HTTPS_PROXY / HTTP_PROXY env vars (cross-platform)
    Or: set proxy in HttpClientHandler

  Gotcha: "My app works on my machine but not on the server"
    → Server might have no proxy set in WinHTTP
    → Run: netsh winhttp show proxy on the server
    → Fix: netsh winhttp set proxy or set HTTP_PROXY env var
```

---

## Section 10 — Package Management (Modern Windows)

```
Windows Package Manager Landscape
===================================

  Manager     Backed By       Registry              Install Location    Admin?
  ────────    ─────────       ────────              ────────────────    ──────
  winget      Microsoft       WinGet repo +         Varies by package   Varies
              (built-in       MS Store +                                (per-machine
              Win10/11)       custom sources                            = yes)

  choco       Chocolatey      chocolatey.org        Usually Program     Usually
              community       (community)           Files or tools\     yes
                              C4B (enterprise)

  scoop       Community       GitHub buckets        %USERPROFILE%\      NO
                              (JSON manifests)      scoop\apps\         (user-space
                                                                        installs)

  Comparison:
  ┌──────────────────────────────────────────────────────────────────┐
  │  winget install Git.Git              # from winget repo          │
  │  choco install git                   # from chocolatey           │
  │  scoop install git                   # from scoop bucket         │
  └──────────────────────────────────────────────────────────────────┘
  All three install the same git. Pick one.
```

### WinGet Deep Dive

```
WinGet Commands
================

  Search:
    winget search vscode
    winget search --id Microsoft.VisualStudioCode   # exact ID

  Install:
    winget install Microsoft.VisualStudioCode
    winget install --id Microsoft.VisualStudioCode --source winget
    winget install --id 9NKSQGP7F2NH --source msstore  # Store app by ID

  Upgrade:
    winget upgrade                    # list upgradable
    winget upgrade --all              # upgrade everything
    winget upgrade Microsoft.Git

  Manage:
    winget list                       # installed packages
    winget uninstall Microsoft.Teams

  Export/Import (machine bootstrap):
    winget export -o packages.json    # export installed list
    winget import -i packages.json    # install from list (great for new-machine setup)

  Enterprise:
    winget configure                  # DSC (Desired State Config) integration
    winget settings                   # configure winget behavior
    # Custom source: winget source add --name internal --arg https://...
```

### MSIX Packaging

```
Packaging an Existing App as MSIX
===================================

  Tools:
    MSIX Packaging Tool (from Store) — GUI, installs app in capture mode
    WiX v4 → MSIX output (build pipeline)
    Visual Studio → Publish → MSIX

  MSIX structure:
    MyApp.msix (ZIP container)
    ├─ AppxManifest.xml         — identity, capabilities, entry points
    ├─ AppxBlockMap.xml         — content hash map
    ├─ AppxSignature.p7x        — code signing certificate
    ├─ Assets\                  — logos, tiles
    └─ VFS\                     — virtual file system overlay
        ├─ ProgramFilesX64\MyApp\
        └─ Windows\System32\    — any DLLs app needs

  Key manifest elements:
    <Identity Name="Contoso.MyApp" Version="1.0.0.0"
              Publisher="CN=Contoso" ProcessorArchitecture="x64"/>
    <Capabilities>
        <Capability Name="internetClient"/>
        <rescap:Capability Name="runFullTrust"/>   ← for unpackaged-style access
    </Capabilities>

  Signing (required for sideload/enterprise):
    signtool sign /fd SHA256 /a MyApp.msix    # uses cert from store
    # Or: New-SelfSignedCertificate + Export-PfxCertificate for dev
```

---

## Section 11 — Visual Studio + MSBuild → SDK-Style Projects

### The .csproj Evolution

```
Old-Style vs SDK-Style .csproj
================================

  Old-Style (.NET Framework, pre-2017)
  ──────────────────────────────────────
  <?xml version="1.0" encoding="utf-8"?>
  <Project ToolsVersion="15.0" xmlns="...msbuild/2003">
    <Import Project="$(MSBuildExtensionsPath)\...Microsoft.CSharp.targets"/>
    <PropertyGroup>
      <Configuration>Debug</Configuration>
      <Platform>AnyCPU</Platform>
      <OutputType>Library</OutputType>
      <TargetFrameworkVersion>v4.8</TargetFrameworkVersion>
      <AssemblyName>MyLib</AssemblyName>
    </PropertyGroup>
    <ItemGroup>
      <Compile Include="Class1.cs"/>     ← EVERY file listed explicitly
      <Compile Include="Class2.cs"/>
      <Compile Include="Utilities\Helper.cs"/>
    </ItemGroup>
    <ItemGroup>
      <Reference Include="System"/>
      <Reference Include="System.Data"/>
    </ItemGroup>
    <ItemGroup>
      <PackageReference Include="Newtonsoft.Json" Version="13.0.0"/>
    </ItemGroup>
  </Project>

  SDK-Style (.NET Core / .NET 5+)
  ─────────────────────────────────
  <Project Sdk="Microsoft.NET.Sdk">    ← this one line does everything
    <PropertyGroup>
      <OutputType>Library</OutputType>
      <TargetFramework>net8.0</TargetFramework>  ← or net8.0-windows
    </PropertyGroup>
    <ItemGroup>
      <PackageReference Include="Newtonsoft.Json" Version="13.0.3"/>
    </ItemGroup>
  </Project>
  ← No file listing — all .cs in the directory tree are implicitly included
  ← No explicit framework assembly references — implicit by TFM
  ← Entire MSBuild SDK imported by the Sdk= attribute

  Multi-targeting:
    <TargetFrameworks>net8.0;net48;net8.0-windows</TargetFrameworks>
    Build produces one output per TFM. #if NET8_0 / #if WINDOWS in code.
```

### MSBuild Architecture (from your background)

```
MSBuild — What's Still True
=============================

  MSBuild is still the build engine. dotnet build calls MSBuild.

  Key concepts (you know these — vocabulary check):
  ┌───────────────────────────────────────────────────────────────┐
  │  Property    — $(TargetFramework), $(Configuration)           │
  │  Item        — @(Compile), @(Content), @(PackageReference)   │
  │  Target      — named execution unit (BeforeBuild, Build, etc)│
  │  Task        — action within a target (Csc, Copy, Exec, etc) │
  │  Import      — pull in another .props or .targets file       │
  │  SDK         — "Sdk=" attribute = shorthand for SDK import   │
  └───────────────────────────────────────────────────────────────┘

  Build hook points:
    BeforeBuild / AfterBuild  — common extension points
    BeforePublish / AfterPublish
    PrepareForBuild
    CoreCompile  — the actual C# compilation step

  Directory.Build.props / Directory.Build.targets:
    Place in repo root. All projects under it inherit automatically.
    Great for: central version pinning, shared properties, lint rules.

    // Directory.Build.props (at repo root)
    <Project>
      <PropertyGroup>
        <Nullable>enable</Nullable>
        <ImplicitUsings>enable</ImplicitUsings>
        <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
      </PropertyGroup>
    </Project>

  Central Package Management (CPM) — NuGet 6.2+:
    Directory.Packages.props at repo root:
    <Project>
      <PropertyGroup>
        <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
      </PropertyGroup>
      <ItemGroup>
        <PackageVersion Include="Newtonsoft.Json" Version="13.0.3"/>
      </ItemGroup>
    </Project>
    Then in .csproj: <PackageReference Include="Newtonsoft.Json"/> (no Version)
    Single source of truth for all package versions.
```

### NuGet Evolution

```
NuGet: packages.config → PackageReference
==========================================

  packages.config (old)              PackageReference (current)
  ─────────────────────              ──────────────────────────
  Separate XML file                  Inline in .csproj
  References listed in project too   Single entry
  packages\ folder in repo           Global cache (~/.nuget/packages)
  Transitive deps manually managed   Automatic transitive resolution
  Install-Package (PM Console)       Add directly to .csproj or:
                                     dotnet add package Newtonsoft.Json
                                     Right-click → Manage NuGet Packages

  NuGet cache locations:
    %USERPROFILE%\.nuget\packages\    ← global package cache
    %LOCALAPPDATA%\NuGet\v3-cache\    ← HTTP cache

  Useful:
    dotnet nuget locals all --list    ← show cache locations
    dotnet nuget locals all --clear   ← nuke all caches
    dotnet restore --no-cache         ← force redownload
```

### dotnet CLI Reference

```
dotnet CLI Cheat Sheet
=======================

  Project management:
    dotnet new console -n MyApp       # new console app
    dotnet new classlib -n MyLib      # new class library
    dotnet new webapi -n MyApi        # new Web API
    dotnet new worker -n MySvc        # new Worker Service
    dotnet new sln -n MySolution      # new solution
    dotnet sln add MyApp/MyApp.csproj # add project to solution

  Build & run:
    dotnet build                      # build (debug by default)
    dotnet build -c Release
    dotnet run                        # build + run (dev)
    dotnet run --project src/MyApp    # specific project
    dotnet run -- --my-arg value      # args after -- go to app

  Publish:
    dotnet publish -c Release         # framework-dependent
    dotnet publish -c Release -r win-x64 --self-contained true
    dotnet publish -c Release -r win-x64 /p:PublishSingleFile=true
    # Single file + self-contained = one .exe, no dependencies

  Test:
    dotnet test
    dotnet test --filter "FullyQualifiedName~UnitTest"
    dotnet test --collect "Code Coverage"

  Package:
    dotnet pack -c Release            # creates .nupkg
    dotnet nuget push *.nupkg --source https://... --api-key ...

  Tools (global tool installs):
    dotnet tool install -g dotnet-ef           # EF Core CLI
    dotnet tool install -g Microsoft.dotnet-interactive  # Jupyter
    dotnet tool list -g                         # list installed tools
    dotnet tool update -g dotnet-ef

  SDK management:
    dotnet --version                  # current SDK
    dotnet --list-sdks                # all installed SDKs
    dotnet --list-runtimes            # all installed runtimes
```

### Configuration Files

```
Configuration File Landscape (.NET 6+)
=======================================

  launchSettings.json  (in Properties/)
    Development-only. Sets env vars, URLs, launch profiles.
    Used by 'dotnet run' and VS F5.
    NOT deployed to production.

    {
      "profiles": {
        "http": {
          "commandName": "Project",
          "launchBrowser": true,
          "environmentVariables": {
            "ASPNETCORE_ENVIRONMENT": "Development"
          },
          "applicationUrl": "http://localhost:5000"
        }
      }
    }

  appsettings.json  (deploy WITH the app)
    Base configuration. Overridden by:
    appsettings.Development.json
    appsettings.Production.json
    Environment variables (ASPNETCORE_ prefix for ASP.NET)
    User secrets (dev only, outside repo)
    Azure App Configuration / Key Vault (production)

  User Secrets (dev — never commit credentials):
    dotnet user-secrets init
    dotnet user-secrets set "ConnectionStrings:Db" "Server=.;..."
    dotnet user-secrets list
    Stored: %APPDATA%\Microsoft\UserSecrets\<project-GUID>\secrets.json

  Priority (highest wins):
    Key Vault / App Config → Env vars → appsettings.{env}.json
    → appsettings.json → compiled defaults
```

---

## Decision Cheat Sheet

```
Desktop App Framework — What to Use When
==========================================

  Situation                              Recommendation
  ─────────                              ──────────────
  New rich desktop app, Windows only     WinUI 3 + WinApp SDK
  New app, needs Win + Mac + mobile      MAUI
  Existing WPF app — maintain/extend     Stay WPF (.NET 8+ supported)
  Existing WinForms — maintain/extend    Stay WinForms (.NET 8+ supported)
  Embed modern UI in old WPF             XAML Islands (WinUI in WPF)
  UWP app migration                      WinUI 3 (Microsoft's migration path)
  Cross-platform CLI tool                .NET 8 Console + dotnet publish
  Web app served on Windows              ASP.NET Core (no native UI needed)
```

```
Background Processing — What to Use When
==========================================

  Situation                              Recommendation
  ─────────                              ──────────────
  New Windows background service         Worker Service + UseWindowsService()
  Long-running scheduled work            Worker Service + hosted services
  Maintain old Windows Service           Migrate to Worker Service when touching
  Needs AD/gMSA identity                 Worker Service + gMSA service account
  Scheduled task (not continuous)        Windows Task Scheduler (schtasks.exe)
  Container-based (Docker/K8s)           Worker Service (UseWindowsService() skipped on Linux)
```

```
Shell / Scripting — What to Use When
======================================

  Situation                              Recommendation
  ─────────                              ──────────────
  Windows admin automation               PowerShell 7 (pwsh)
  Legacy script maintenance              PowerShell 5.1 (powershell.exe)
  Quick one-off: services, registry      PowerShell (either version)
  Linux build tools on Windows           WSL2
  Docker Linux containers                Docker Desktop + WSL2 backend
  Git operations                         Git for Windows (any shell) or WSL2
  Cross-platform scripts (Win+Linux)     PowerShell 7 or bash in WSL2
  Old .bat files that work               Leave as cmd.exe, don't rewrite
```

```
IPC / Communication — What to Use When
========================================

  Situation                              Recommendation
  ─────────                              ──────────────
  Same machine, .NET both sides          gRPC over named pipe OR loopback TCP
  Same machine, cross-language           gRPC over loopback TCP or AF_UNIX
  Replacing WCF named pipe binding       gRPC with Named Pipe transport
  Replacing WCF netTcpBinding            gRPC over TCP
  Replacing WCF basicHttpBinding         REST (ASP.NET Core minimal API)
  High-throughput binary same-machine    Memory-mapped file + EventWaitHandle
  Database local connection              Named pipe (SQL Server default)
```

```
Package Distribution — What to Use When
=========================================

  Situation                              Recommendation
  ─────────                              ──────────────
  New app for Store / winget             MSIX
  Enterprise deployment (Intune/SCCM)   MSIX or traditional installer
  Dev tool, no admin required            winget (scoop for user-space)
  Legacy app, complex installer needs   WiX v4 (traditional installer)
  Simple xcopy-deployable .exe           dotnet publish self-contained
  Internal tooling / dev machines        winget + custom source or scoop
```

```
Security Controls — What to Use When
======================================

  Situation                              Use
  ─────────                              ───
  Prevent privileged process access      Credential Guard (VBS)
  Code signing enforcement               WDAC policy
  Reduce attack surface                  ASR rules via Intune
  Service identity management            gMSA (group Managed Service Account)
  Developer workstation password-less    WHfB (already deployed at Microsoft)
  Registry/filesystem audit              Enable Security audit policy + SACL
  App allow-listing                      WDAC (preferred over AppLocker)
```

---

## Common Confusion Points

**WinUI 3 XAML is not WPF XAML.**
They look similar but are different namespaces, different assemblies, different binding syntax details.
You cannot share XAML between WPF and WinUI 3 without modification.
XAML Islands is the bridge: embed WinUI 3 controls inside a WPF window.

**MAUI on Windows uses WinUI 3 under the hood.**
So MAUI = WinUI 3 (Windows) + AppKit (macOS) + UIKit (iOS) + Android views.
If you're Windows-only, WinUI 3 directly gives you more control.

**Worker Service and Windows Service are the same binary.**
`UseWindowsService()` is a NOP on Linux/macOS.
Same code runs as a Windows Service on Windows and a systemd service on Linux — just change the host extension.

**PowerShell 5.1 (powershell.exe) and PowerShell 7 (pwsh.exe) coexist.**
They do not conflict. PS7 is installed separately to Program Files\PowerShell\7\.
Scripts written for 5.1 mostly work in 7 with minor exceptions (some Windows-only modules need the compat layer).

**WSL2's filesystem is NOT your Windows filesystem.**
`/mnt/c/` is a 9P network mount. Running `npm install` in `/mnt/c/Users/you/repo` is slow.
Clone repos into `~/projects/` inside WSL2 for full native Linux filesystem speed.

**WOW64 registry redirection trips up automation scripts.**
If your 64-bit PowerShell reads a registry key and finds nothing, but the 32-bit app writes it there — the 32-bit app wrote to `Wow6432Node`. Check both paths.
`reg query "HKLM\SOFTWARE\Wow6432Node\..."` from 64-bit process.

**UAC registry virtualization hides writes from admins.**
If a non-manifested app writes to `HKLM\SOFTWARE\MyApp` without admin,
it silently goes to `HKCU\SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\MyApp`.
The app reads it back fine. You as admin read `HKLM\SOFTWARE\MyApp` and see nothing.
Use Autoruns / Process Monitor to catch this.

**SDK-style projects include all .cs files automatically.**
If you add a .cs file to the directory, it's automatically in the build.
Old-style projects required you to add it in the .csproj. This trips people up when migrating.

**`dotnet build` and `msbuild` are not the same entry point.**
`dotnet build` bootstraps MSBuild through the .NET SDK and sets up SDK imports automatically.
Bare `msbuild.exe` may not find the .NET SDK targets without explicit import paths.
Always use `dotnet build` for SDK-style projects.

**ETW is always on, zero-cost when not subscribed.**
You can instrument your production app with EventSource today at zero overhead.
The overhead only appears when a session subscribes — which is ad hoc during investigation.
This is the right model: instrument everything, observe on demand.

**LSASS PPL and Credential Guard are different protections.**
PPL = even SYSTEM cannot inject into LSASS (process-level protection).
Credential Guard = credential material never in normal kernel memory (VBS isolation).
Both should be enabled. In enterprise: Credential Guard via Intune → Device Security policy.

**`packages.config` is not just "the old way" — it's a security concern.**
Old projects with packages.config don't get transitive dependency vulnerability scanning
from `dotnet list package --vulnerable`. Migrate to PackageReference.
```

---

## Windows Security Internals — Kernel-Level Architecture

### VBS / HVCI / Credential Guard

```
VIRTUALIZATION-BASED SECURITY (VBS) ARCHITECTURE
══════════════════════════════════════════════════

  Hardware (CPU VT-x / AMD-V + IOMMU)
  │
  ├─ Hyper-V Hypervisor (Ring -1 / VMX root mode)
  │   ├─ Virtual Trust Level 0 (VTL0) — Normal World
  │   │   ├─ NT Kernel (ring 0) — ntoskrnl.exe, drivers
  │   │   └─ User space (ring 3) — your apps, even SYSTEM processes
  │   │
  │   └─ Virtual Trust Level 1 (VTL1) — Secure World
  │       ├─ Secure kernel (securekernel.exe)
  │       ├─ Isolated User Mode (IUM) — trustlets
  │       │   ├─ lsaiso.exe  ← Credential Guard isolate
  │       │   │   Holds NTLM hashes, Kerberos TGTs in VSM
  │       │   │   Even kernel-mode rootkit in VTL0 cannot reach them
  │       │   └─ Other VSM trustlets (TPM virt, attestation)
  │       └─ HVCI enforcement (see below)

HVCI (Hypervisor-Protected Code Integrity):
  The hypervisor controls what code can run in ring 0 (VTL0 kernel)
  Kernel page table enforcement: all kernel-executable pages must be
  signed by WDAC policy — no unsigned kernel memory execution
  Effect: driver signing is not enough; driver code must also be WDAC-approved
  Tools: SiPolicy.p7b / WDAC policy; CiTool.exe; VBSKey events in Event Log
```

### Kernel Patch Protection (KPP / PatchGuard)

```
PATCHGUARD MECHANICS
════════════════════

  PatchGuard protects against runtime kernel patching — the technique used
  by rootkits and (historically) AV vendors to hook kernel structures.

  What it monitors (periodically, randomized interval ~5-15 min):
  ├─ SSDT (System Service Descriptor Table) — syscall dispatch table
  ├─ IDT (Interrupt Descriptor Table) — interrupt handler pointers
  ├─ GDT (Global Descriptor Table)
  ├─ MSRs (Model-Specific Registers) — LSTAR (syscall entry point)
  ├─ Kernel code pages — key ntoskrnl functions
  └─ Critical kernel data structures (KPCR, KPRCB, etc.)

  On violation: immediate BSOD — 0x109 CRITICAL_STRUCTURE_CORRUPTION
  No exceptions. No signed exception. Not bypassable in production.
  Only way to "disable" it: kernel debugger attached (KD) — which flags
  the machine and disables some VBS features.

  Implication for security vendors:
  Before PatchGuard (pre-Vista x64): AV hooks SSDT to intercept syscalls.
  After PatchGuard: must use documented kernel callbacks:
    PsSetCreateProcessNotifyRoutine() — process create/exit
    PsSetCreateThreadNotifyRoutine()  — thread create/exit
    PsSetLoadImageNotifyRoutine()     — image load (DLL, EXE, driver)
    CmRegisterCallback()             — registry operation intercept
    ObRegisterCallbacks()            — object open/duplicate intercept
    MiniFilter (FltRegisterFilter)   — filesystem I/O intercept
  This is how Microsoft Defender and EDR products work post-Vista x64.
```

### PPL (Protected Process Light) Trust Hierarchy

```
WINDOWS PROCESS PROTECTION LEVELS
════════════════════════════════════

  Protection Level    Value   Who runs at this level
  ─────────────────   ─────   ─────────────────────────────────────────
  PP  (full)          Full    wininit.exe, smss.exe, csrss.exe
  PPL WinTcb          High    services.exe, lsass.exe (if PPL configured)
  PPL Windows         Med     spoolsv.exe, taskhostw.exe, audiodg.exe
  PPL Antimalware     AM      AV/EDR kernel driver (special trust chain)
  PPL Store           App     Windows Store app hosts
  None                0       Normal processes (your app)

  Rules:
    Higher protection level process → cannot be opened for memory read/write
    by lower protection level process (even SYSTEM privilege)
    SYSTEM + SeDebugPrivilege does NOT bypass PPL
    WinDbg cannot attach to PP/PPL processes without kernel debugger

  lsass.exe PPL:
    Enabled in Credential Guard scenarios
    Prevents LSASS memory dump attacks (mimikatz targets lsass)
    Even administrator cannot OpenProcess(PROCESS_ALL_ACCESS) on it
    Enable: HKLM\SYSTEM\CurrentControlSet\Control\Lsa → RunAsPPL = 1
    (Requires Secure Boot; otherwise attacker can boot offline and clear it)

  Antimalware PPL:
    AV vendor's kernel driver signs with Microsoft's Early Launch AM cert
    Gets elevated trust to intercept process creation before other drivers
    ELAM driver runs before all 3rd-party drivers at boot
```

### Windows I/O Model — IOCP and Overlapped I/O

```
WINDOWS ASYNC I/O ARCHITECTURE
════════════════════════════════

  COMPLETION-BASED MODEL: initiate I/O, OS does it, notifies you when done.
  Never blocks the issuing thread.

  ┌─────────────────────────────────────────────────────────────────┐
  │                     YOUR APPLICATION                            │
  │                                                                 │
  │  CreateFile(handle, ..., FILE_FLAG_OVERLAPPED)                  │
  │  ReadFile(handle, buf, size, NULL, &overlapped)  ← returns fast │
  │         │                                                       │
  │         │ (I/O queued to kernel; thread continues)              │
  │         ▼                                                       │
  │  GetQueuedCompletionStatus(iocp, &bytes, &key, &overlapped, -1) │
  │         │ ← thread blocks HERE (not during I/O)                 │
  │         ▼                                                       │
  │  Process completion — overlapped.Internal = status              │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │                     KERNEL                                      │
  │                                                                 │
  │  I/O Request Packet (IRP) → I/O Manager → driver stack         │
  │         │                                                       │
  │         │ DMA / hardware completes I/O                          │
  │         ▼                                                       │
  │  I/O completion routine (APC) or IOCP queue                     │
  │  → completion packet queued to IOCP object                      │
  └─────────────────────────────────────────────────────────────────┘

  I/O Completion Port (IOCP):
    CreateIoCompletionPort(handle, iocp, key, threadCount)
    Associates file/socket handle to IOCP
    Multiple threads call GetQueuedCompletionStatus() on same IOCP
    OS wakes only as many threads as there are CPU cores (thundering herd prevention)
    Ideal: threadCount = 0 → use CPU count threads

  .NET mapping:
    ThreadPool sits on IOCP — every await over I/O uses it
    async/await over Socket, Stream, HttpClient → overlapped I/O → IOCP
    No thread consumed during the I/O wait — just an OVERLAPPED struct
    This is why .NET async I/O scales: 10k concurrent requests ≠ 10k threads
```

```
COMPARISON: IOCP vs epoll vs kqueue vs io_uring

  API              IOCP                 epoll              kqueue            io_uring
  ──────────       ──────────────────   ──────────────     ──────────────    ──────────────────
  Model            Completion           Readiness          Readiness         Completion (rings)
  Open file I/O    Yes (FILE_FLAG_OVR)  No (only socket)   Yes (vnode)       Yes (full file AIO)
  Associate        CreateIoCompPort()   epoll_ctl(ADD)     kevent(EVFILT_*)  io_uring_register()
  Wait             GetQueuedCS()        epoll_wait()       kevent()          io_uring_enter()
  Thread model     N workers on 1 port  1 thread / N ports  1 thread / N ports  SQ/CQ ring per thread
  Syscalls/op      0 (work in kernel)   1 per event poll   1 per event poll  ~0 (ring batching)
  .NET backed by   Yes (ThreadPool)     Yes (SocketEngine)  Yes (SocketEngine)  Not yet (.NET 9+)
```

### Configuration Store Cross-OS Bridge

Every OS needs a persistent configuration store. The choice of design (hierarchical DB vs files vs typed plists) has deep architectural consequences.

```
CONFIGURATION STORE COMPARISON
════════════════════════════════════════════════════════════════════

  Windows Registry               Linux /etc + ~/.config         macOS plist
  ────────────────               ──────────────────────         ───────────
  Hierarchical binary DB         Flat text files                Binary or XML property lists
  Stored as "hive" files:        No central store:              CFPreferences layer:
    SYSTEM, SOFTWARE, SAM,         each app owns its files        ~/Library/Preferences/
    SECURITY, DEFAULT              /etc/<app>.conf                  com.apple.Terminal.plist
    (in %SystemRoot%\System32\     ~/.config/<app>/               /Library/Preferences/
     Config\)                      ~/.local/share/<app>/          (machine-wide)
    NTUSER.DAT (per user)          /run/<app>/ (runtime)

  Hive → memory mapping:         No caching layer:              CFPreferences in-memory cache:
    OS maps hive into kernel       cat /etc/nginx.conf            defaults write ... → cache
    memory; reads are fast         reads disk every time          defaults synchronize → flush
                                   (page cache helps)             In-code: must call sync

  Transaction support:           No transactions:               No transactions:
    TxR (Transactional Registry)   Write new file, rename         Write new plist, rename
    KTM + TxF for file+reg         atomically (mv is atomic)      (atomic rename on APFS)
    Rollback on failure            Common pattern:                Common pattern:
    Used by: MSI installer,          write .tmp, rename to real     write to .plist.tmp,
    MSIX install, system updates                                     rename

  Change notification:           inotify / fanotify:            FSEvents / kqueue:
    RegNotifyChangeKeyValue()      inotify_add_watch(fd, path)    FSEventStreamCreate()
    WM_SETTINGCHANGE broadcasts    poll or epoll on inotify fd    kqueue EVFILT_VNODE
    Immediate, in-process          Works for files AND dirs       Works for files AND dirs

  Access control:                File-level DAC:                File-level DAC:
    Per-key ACLs (DACL/SACL)       chmod / chown on /etc files    chmod / chown on plist
    regedit → Permissions menu      No per-key sub-entry ACLs     No sub-entry ACLs
    Group Policy (GPO):             Policy: puppet/ansible/salt    Profile: MDM (Jamf/Intune)
      pushes via HKLM policies        manages /etc files            manages .plist files

  Monitoring / introspection:    Human-readable:                Human-readable (XML):
    regedit, reg.exe, RegEdit32     cat /etc/nginx.conf            plutil -p ~/Library/Preferences/
    Process Monitor (Sysinternals)  grep, sed, awk on configs        com.company.app.plist
    PowerShell: Get-ItemProperty    diff for change review           PlistBuddy -c "Print" ...
    ETW: Microsoft-Windows-Kernel-  git-tracked in /etc             defaults read com.company.app
     Registry provider              (e.g., etckeeper)
```

**The design philosophy gap:** The Registry stores _everything_ — OS settings, app preferences, driver parameters, COM registration, service configuration — in one place. Linux treats configuration as files: each app/service is responsible for its own config files in standard locations, with no central authority. macOS is in between: plist files in standard locations, but with a daemon (`configd`) and API layer (`CFPreferences`) that provides some caching and notification.

**Practical implication when porting software:** A Windows app that reads from `HKCU\Software\Company\App` needs to be rewritten to read from `~/.config/company/app.conf` on Linux or `~/Library/Preferences/com.company.app.plist` on macOS. There is no automatic mapping. The cross-platform configuration library of choice is typically: `platformdirs` (Python), `dirs` crate (Rust), `System.Environment.SpecialFolder` (.NET), or `appdirs` (Go).

## Appendix: Sysinternals Tools Every Windows Developer Should Know

```
Sysinternals Quick Reference (download.sysinternals.com / winget install Sysinternals)
=======================================================================================

  Process Explorer  — Task Manager replacement. Shows DLLs loaded by each process,
                      handles, parent-child tree, company name of each process.
                      Essential for malware triage and "what is this process?"

  Process Monitor   — Real-time file system, registry, process/thread activity.
                      Filter by process name + event type.
                      "What is this app reading/writing to the registry?"

  Autoruns          — Everything that runs at startup: registry, scheduled tasks,
                      services, browser extensions, LSA providers.
                      Gold standard for startup audit.

  PsExec            — Run processes on remote machines, run as SYSTEM locally.
                      psexec -s cmd  → cmd.exe as SYSTEM

  Strings           — Extract printable strings from binaries (like Unix strings).

  Handle            — Show which process has a file locked.
                      handle.exe C:\locked-file.txt

  TCPView           — Real-time TCP/UDP connections + process ownership.
                      GUI version of netstat -b.

  WinObj            — Browse NT Object Manager namespace.
                      See named pipes, sections, device objects, symbolic links.

  AccessChk         — Check effective permissions on files/registry/services.
                      accesschk -l HKLM\SOFTWARE\MyApp
```
