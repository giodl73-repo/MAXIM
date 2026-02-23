# Operating Systems — Universal Cheat Sheet & Vocabulary Load-In

## Master Comparison Matrix

| Topic | Windows | Linux (Ubuntu/Debian) | Linux (RHEL/Fedora) | macOS | iOS | Android |
|-------|---------|-----------------------|---------------------|-------|-----|---------|
| **Kernel** | NT (hybrid) | Linux 6.x (monolithic) | Linux 6.x | XNU (Mach+BSD hybrid) | XNU (same) | Linux (modified) |
| **Init / PID 1** | smss.exe → wininit | systemd | systemd | launchd | launchd | init → Zygote |
| **Shell default** | PowerShell (pwsh) | bash / zsh | bash | zsh | none (no CLI) | sh (via adb) |
| **Package install** | winget / choco | apt install | dnf install | brew install | App Store only | Play Store / adb |
| **Service manage** | Get-Service, sc.exe | systemctl | systemctl | launchctl | (managed) | adb shell am |
| **Process list** | Get-Process / tasklist | ps / htop / top | ps / htop | ps / Activity Monitor | Instruments | adb shell ps |
| **Network info** | ipconfig / Get-NetIPAddress | ip a / ss | ip a / ss | ifconfig / networksetup | Settings only | adb shell ip |
| **Disk usage** | Get-PSDrive / du | df / du | df / du | df / du | Settings only | adb shell df |
| **Firewall** | netsh advfirewall / New-NetFirewallRule | ufw / iptables / nftables | firewalld | pfctl (pf) | managed | managed |
| **File system** | NTFS / ReFS | ext4 / XFS / btrfs | XFS / ext4 | APFS | APFS | ext4 / f2fs |
| **Dynamic lib** | .dll (PE format) | .so (ELF) | .so (ELF) | .dylib (Mach-O) | .dylib (Mach-O) | .so (ELF in APK) |
| **Executable** | .exe (PE) | (no ext, ELF) | (no ext, ELF) | (Mach-O, in .app) | (Mach-O, in .ipa) | classes.dex in APK |
| **Debug symbols** | .pdb | DWARF (in .so) | DWARF | .dSYM bundle | .dSYM bundle | .sym / tombstone |
| **Code signing** | Authenticode (signtool) | GPG (packages) | RPM GPG | Developer ID + notarize | App Store cert | Keystore (.jks) |
| **App bundle** | .msix / .exe / .msi | .deb / snap / flatpak | .rpm / snap | .app bundle / .dmg | .ipa | .apk / .aab |
| **Config location** | Registry (HKCU/HKLM) | /etc/ + ~/.config/ | /etc/ + ~/.config/ | plist in ~/Library | plist in sandbox | SharedPreferences |
| **Log location** | Event Viewer / ETW | journalctl / /var/log | journalctl / /var/log | Console.app / ~/Library/Logs | Xcode Organizer | logcat |
| **Env variables** | $env:VAR (PS) / %VAR% | $VAR / export VAR | $VAR / export VAR | $VAR | injected at runtime | build config |
| **User data dir** | %APPDATA% | ~/.local/share (XDG) | ~/.local/share | ~/Library/App Support | NSDocumentDirectory | getFilesDir() |
| **Temp dir** | %TEMP% | /tmp (tmpfs) | /tmp (tmpfs) | /tmp → /private/tmp | NSTemporaryDirectory() | getCacheDir() |
| **Virtualization** | Hyper-V | KVM + QEMU | KVM + QEMU | Virtualization.framework | (none) | (none) |
| **Container runtime** | Docker Desktop (Hyper-V/WSL2) | Docker (native) | Podman (rootless) | Docker Desktop (Virt.fw) | (none) | (none) |

---

## Per-OS Vocabulary Cards

### WINDOWS — Terms to Load In

```
KERNEL & RUNTIME
─────────────────
ntoskrnl.exe    The NT kernel image (ring 0)
hal.dll         Hardware Abstraction Layer — isolates kernel from hardware
smss.exe        Session Manager Subsystem — first user-mode process
csrss.exe       Client/Server Runtime (Win32 subsystem) — one per session
lsass.exe       Local Security Authority — credentials, tokens, domain auth
services.exe    Service Control Manager host
svchost.exe     Generic service host — groups many services for efficiency
conhost.exe     Console host — handles terminal I/O
winlogon.exe    Login process; watches for Ctrl+Alt+Del
dwm.exe         Desktop Window Manager — compositor

HANDLES & OBJECTS
─────────────────
HANDLE          Integer index into a process's handle table (not a pointer)
Object Manager  NT kernel component — all resources are "objects" with refcounts
Duplicate       Copy a handle between processes: DuplicateHandle()
KernelObject    Kernel-mode objects: Process, Thread, File, Event, Mutex, Semaphore
UserObject      User32 objects: Window, Menu, Cursor (not ref-counted the same way)

SECURITY
─────────────────
SID             Security Identifier — binary value identifying user/group
DACL            Discretionary ACL — who can access this object (allow/deny ACEs)
SACL            System ACL — audit entries
ACE             Access Control Entry — one rule in a DACL/SACL
Token           Security context attached to process/thread (SIDs + privileges)
Impersonation   Thread uses a different token than its process (service patterns)
UAC             User Account Control — admin gets two tokens; elevation = new process
Integrity Level Low(untrusted) < Medium(normal) < High(elevated) < System
Privilege       Named capability in token: SeDebugPrivilege, SeShutdownPrivilege etc
AppContainer    Sandboxed token for UWP apps — very restricted capabilities

MEMORY
─────────────────
VirtualAlloc    Reserve/commit virtual pages — bottom-level memory API
HeapAlloc       Win32 heap (on top of VirtualAlloc) — for small allocations
AWE             Address Windowing Extensions — map >4GB in 32-bit process (legacy)
Working Set     Pages currently in RAM for a process
Commit charge   Total committed (may be in page file) across all processes
PageFile.sys    Windows virtual memory paging file
Section         Kernel object for shared memory / memory-mapped files
PEB             Process Environment Block — user-mode process metadata
TEB             Thread Environment Block — per-thread metadata (TLS, stack bounds)

REGISTRY
─────────────────
HKEY_LOCAL_MACHINE (HKLM)   Machine-wide settings (requires admin to write)
HKEY_CURRENT_USER  (HKCU)   Current user settings
HKEY_CLASSES_ROOT  (HKCR)   COM registration, file associations (merged HKLM+HKCU)
HKEY_USERS         (HKU)    All users' hives
Hive file          HKLM\SYSTEM → %SystemRoot%\System32\Config\SYSTEM on disk
REG_SZ             String value
REG_DWORD          32-bit integer
REG_BINARY         Raw binary
REG_MULTI_SZ       Multi-string (array of strings)
reg.exe            CLI: reg query HKLM\... / reg add / reg delete
Get-ItemProperty   PowerShell equivalent

SERVICES
─────────────────
SCM             Service Control Manager — manages service lifecycle
sc.exe          CLI: sc query / sc start myService / sc config
Get-Service     PowerShell equivalent
ServiceType     Win32OwnProcess / Win32ShareProcess / KernelDriver / FileSystemDriver
StartType       Automatic / AutomaticDelayed / Manual / Disabled
Recovery action On failure: restart / run program / reboot
SYSTEM account  NT AUTHORITY\SYSTEM — no network identity (use gMSA instead)
gMSA            Group Managed Service Account — domain account with auto-rotating password
LocalService    Limited SYSTEM account — lower privileges, can access network as null session
NetworkService  Like LocalService but presents machine credentials on network

DEBUGGING
─────────────────
WinDbg          Primary Windows debugger — user mode + kernel mode
PDB             Program DataBase — debug symbols (symbol server: https://msdl.microsoft.com/...)
!analyze -v     WinDbg command — auto-analyze crash dump
Process Monitor Sysinternals — file/registry/process/network activity
Process Explorer Sysinternals — Task Manager replacement with full process tree
ETW             Event Tracing for Windows — kernel-level tracing framework
WPA             Windows Performance Analyzer — ETW visualization
perfview        .NET-specific ETW viewer (GC, JIT, CPU sampling)
Minidump        Small crash dump (thread state + exception) vs full dump (all memory)
DebugBreak()    Programmatic breakpoint (raises STATUS_BREAKPOINT)
EXCEPTION_RECORD    Structured Exception Handling — Windows' own try/except in C
```

---

### LINUX — Terms to Load In

```
KERNEL INTERNALS
─────────────────
vmlinuz         Compressed kernel image
initramfs       Initial RAM filesystem — early boot environment
/proc           Virtual filesystem — kernel data structures as files (/proc/PID/maps)
/sys (sysfs)    Kernel device/driver model as files — configure drivers at runtime
/dev            Device files — char (serial) + block (disk) devices
udev            Userspace device manager — creates /dev nodes dynamically
dmesg           Kernel ring buffer — boot messages + driver output
kthread         Kernel threads (show up in ps with [brackets])
OOM killer      Out-of-memory killer — picks a process to kill when RAM exhausted
cgroups         Control groups — limit/account CPU/memory/IO per process group
namespaces      Isolate: pid, net, mnt, uts, ipc, user — the Docker substrate
seccomp-bpf     Syscall filter — whitelist allowed syscalls per process (Chrome, Docker)
BPF/eBPF        Extended Berkeley Packet Filter — JIT code injected into kernel for
                tracing, networking, security (replaces many kernel modules)

FILESYSTEM
─────────────────
VFS             Virtual File System — abstraction layer, all FS implement same ops
inode           Metadata struct for a file/dir (permissions, size, timestamps, not name)
dentry          Directory entry — maps filename to inode (cached in dentry cache)
page cache      Disk data cached in RAM — Linux aggressively uses free RAM for this
dirty page      Page in cache modified but not yet written to disk
/               Root mount
/bin, /usr/bin  System executables (modern: /bin → symlink to /usr/bin)
/etc            Configuration files (system-wide)
/var            Variable data: logs (/var/log), spool, cache
/home           User home directories
/tmp            Temporary files — tmpfs (RAM-backed, cleared on boot)
/opt            Optional packages (not managed by distro package manager)
/run            Runtime data — PIDs, sockets (tmpfs, cleared on boot)
/proc           Process + kernel virtual FS
/sys            Kernel/device virtual FS
mount           Attach filesystem to tree: mount /dev/sdb1 /mnt/data
bind mount      Mount a directory at another location (Docker volume mechanism)
tmpfs           In-memory filesystem
overlayfs       Union mount — upper (writable) + lower (read-only) — Docker layers

PROCESSES
─────────────────
PID 1           init / systemd — all processes are children of this
fork()          Copy process — child inherits parent's FDs, memory (copy-on-write)
exec()          Replace process image — used after fork() to run new program
wait()          Parent waits for child exit (otherwise: zombie)
zombie          Process exited but parent hasn't called wait() — stays in table
orphan          Process whose parent died — reparented to PID 1
nice            Priority adjustment: -20 (highest prio) to +19 (lowest)
renice          Change nice of running process
kill -9         SIGKILL — force kill, cannot be caught or ignored
kill -15        SIGTERM — polite terminate, can be caught (default for kill)
kill -1         SIGHUP — reload config (convention: daemons reload on SIGHUP)
strace          Trace system calls a process makes
ltrace          Trace library calls
/proc/PID/fd    Open file descriptors for a process
lsof            List open files (file descriptors) — who has what open
fuser           Which processes are using a file or port

SYSTEMD
─────────────────
unit file       /etc/systemd/system/myapp.service — service definition
ExecStart       Command to run
ExecReload      Command to reload (usually kill -HUP $MAINPID)
WantedBy        Target to attach to (multi-user.target = normal boot)
After           Ordering: start after network.target
Requires        Hard dependency: fail if dep fails
Type=simple     (default) main process = ExecStart PID
Type=forking    Old-style: ExecStart forks, parent exits
Type=notify     Service sends sd_notify() when ready (most modern)
Type=oneshot    Run once and exit (e.g., setup tasks)
systemctl       CLI: start/stop/restart/status/enable/disable/reload
journalctl      Log viewer: journalctl -u myservice -f (follow) --since "1 hour ago"
journald        Systemd journal daemon — structured binary log storage
socket activate Service starts on first connection — faster boot

NETWORKING
─────────────────
ip a            Show interfaces + addresses (replaces ifconfig)
ip r            Show routing table (replaces route)
ss              Socket statistics (replaces netstat)
ss -tlnp        TCP listening ports with process names
nftables        Modern packet filtering (replaces iptables in RHEL9+/Ubuntu22+)
iptables        Legacy packet filter — still widely documented
netfilter       Kernel framework that iptables/nftables use
/etc/resolv.conf   DNS servers
/etc/hosts      Static hostname→IP mappings
NetworkManager  Daemon managing network connections on desktops
systemd-networkd  Server-side network config alternative to NM

PERMISSIONS
─────────────────
rwxr-xr-x      user/group/other — 3 triplets of read/write/execute
chmod 755       u=rwx,g=rx,o=rx
chmod +x        Add execute bit for all
chown alice:dev Set owner:group
umask           Default permission mask for new files (022 → new files 644, dirs 755)
sticky bit      On directory: only owner can delete files (like /tmp)
setuid bit      Execute with owner's privileges (e.g., /usr/bin/passwd runs as root)
setgid bit      Execute with group's privileges / inherit group for new dir files
sudo            Run as root (configured via /etc/sudoers)
su              Switch user
capabilities    Fine-grained root powers: CAP_NET_BIND_SERVICE (bind port <1024 as non-root)
```

---

### MACOS — Terms to Load In

```
KERNEL & DARWIN
─────────────────
XNU             "X is Not Unix" — the macOS/iOS kernel
                Mach (microkernel IPC + VM) + BSD (POSIX + filesystems) + IOKit (drivers)
Darwin          Open-source base of macOS = XNU kernel + userland tools
Mach port       Fundamental IPC primitive in XNU (message-passing endpoints)
Mach trap       Low-level system call into Mach layer
BSD syscall     Standard POSIX syscalls (open, read, fork etc) — go through BSD layer
dyld            Dynamic linker/loader — loads .dylib dependencies, initializes ObjC runtime
dyld shared cache  All system frameworks pre-linked into one file for startup perf
IOKit           C++ driver framework in kernel (object-oriented, unusual)
kext            Kernel Extension — macOS driver (deprecated → use DriverKit)
DriverKit       User-space driver framework (macOS 10.15+) — safer than kext
SIP             System Integrity Protection — protects /System, /usr, /bin, /sbin
                even from root. Disable only in Recovery mode (don't).
APFS            Apple File System: COW, snapshots, clones, encryption, sparse files
Rosetta 2       Dynamic binary translator — runs x86-64 on Apple Silicon (arm64)
Universal binary    Fat binary containing both x86_64 + arm64 slices

FRAMEWORKS (the SDK onion)
─────────────────
CoreFoundation  C-level base layer (CF types: CFString, CFArray etc) — bridges to Foundation
Foundation      Obj-C/Swift base framework: NSString, NSArray, NSDictionary, NSData,
                URLSession, OperationQueue, NotificationCenter, UserDefaults
AppKit          macOS UI framework (NSWindow, NSView, NSViewController)
UIKit           iOS/iPadOS/tvOS UI framework (UIWindow, UIView, UIViewController)
SwiftUI         Declarative UI — works on macOS + iOS (wraps AppKit/UIKit)
Core Data       ORM / persistence framework — SQLite or in-memory
Core ML         On-device ML inference
Metal           GPU compute + rendering API (Apple's answer to OpenGL/Vulkan)
AVFoundation    Audio/video playback, recording, processing
Core Bluetooth  BLE API
WKWebView       Embedded browser (WebKit — same engine as Safari)
Combine         Reactive streams framework (like RxSwift but first-party)
Swift Concurrency   async/await + actors (macOS 12+ / iOS 15+ to use everywhere)

LAUNCHD
─────────────────
launchd         macOS PID 1 — replaces cron, xinetd, init, inetd all at once
plist           Property list (XML or binary) — macOS config format everywhere
Launch Daemon   System-wide service: /Library/LaunchDaemons/*.plist (root-owned)
Launch Agent    User-level service: ~/Library/LaunchAgents/*.plist (user-owned)
launchctl load  Register a plist with launchd
launchctl start Start a registered job by label
launchctl list  Show all registered jobs + status
launchctl print system/com.example.myservice — detailed status

APP BUNDLE
─────────────────
.app bundle     Directory that looks like a file: MyApp.app/
Contents/         macOS structure
  Info.plist      App metadata: bundle ID, version, required capabilities
  MacOS/          Executable(s)
  Frameworks/     Embedded frameworks
  Resources/      Assets, nibs, storyboards
  CodeSignature/  Signing data
CFBundleIdentifier  com.company.appname — globally unique ID (reverse DNS)
UTI             Uniform Type Identifier — com.adobe.pdf, public.image etc
NSPrincipalClass   Entry point class declared in Info.plist

SIGNING & DISTRIBUTION
─────────────────
Apple Developer Program  $99/year for iOS/macOS distribution
Development cert     Signs app for testing on your own devices
Distribution cert    Signs app for App Store or direct distribution
Provisioning profile  Binds: cert + app ID + device list (development) + entitlements
Entitlements         Per-app capability grants: network server, keychain group,
                     iCloud, HealthKit, push notifications etc
Hardened Runtime     macOS security flag — disables JIT, unsigned memory, DYLD injection
Notarization         Apple scans app for malware (automated); required for Gatekeeper
Gatekeeper           macOS gate: blocks apps not signed/notarized from launching
codesign -dv --verbose=4 ./MyApp.app   Inspect signing
spctl --assess --type exec ./MyApp.app  Test Gatekeeper acceptance

HOMEBREW
─────────────────
brew install <pkg>     Install package
brew services start <name>   Manage via launchd
brew tap <user/repo>   Add third-party formula repository
Cellar             /opt/homebrew/Cellar (Apple Silicon) / /usr/local/Cellar (Intel)
Formula            Ruby script defining how to install a package
Cask               Formula for GUI apps (.dmg/.pkg install)
keg-only           Package installed but not symlinked (avoid conflicting with system)
```

---

### iOS — Terms to Load In

```
XCODE & BUILD
─────────────────
Xcode           Apple's IDE — only on macOS; required for iOS builds
Target          Build artifact (app, framework, test bundle, extension)
Scheme          Named build configuration: what to build + run + test + profile + archive
Build Setting   Per-target compiler/linker settings (SWIFT_VERSION, PRODUCT_BUNDLE_ID etc)
xcworkspace     Workspace containing multiple projects (CocoaPods creates this)
xcodeproj       Single project (without CocoaPods)
Simulator       x86-64 or arm64 emulated iOS environment on Mac — fast, no certs needed
Device          Physical iPhone/iPad — requires provisioning profile

IDENTITY & SIGNING
─────────────────
Bundle ID       com.company.app — unique identifier, matches App Store Connect record
Team ID         10-char alphanumeric ID for your Apple Developer account
Signing Identity    Certificate in Keychain: "Apple Development: Alice (TEAMID)"
Provisioning Profile  .mobileprovision file embedded in app — links cert + bundle ID + devices
Entitlements    XML plist embedded by codesign — declares permissions: push, iCloud etc
App Groups      com.company.group — shared container between app + extensions
Associated Domains  Branch/Deeplink: applinks:example.com requires Apple CDN record
App Attest      iOS 14+ hardware attestation — prove request came from unmodified app

ARCHITECTURE
─────────────────
UIScene         iOS 13+ — one app can have multiple scenes (windows on iPad)
AppDelegate     Application lifecycle callbacks (pre-iOS 13 entry point)
SceneDelegate   Scene lifecycle (iOS 13+)
@main / @UIApplicationMain  Entry point annotation
Storyboard      XML UI definition (older) — visual layout, segues between VCs
XIB (nib)       Single-view XML (less context than storyboard)
SwiftUI         Declarative — no storyboard; previews in Xcode
Auto Layout     Constraint-based layout engine (NSLayoutConstraint)
UIViewController  Controller in MVC — manages a "screen" or a portion of it
UIView          Base class for all visual elements
Responder chain  Event routing: UIView → UIViewController → UIWindow → UIApplication

MEMORY
─────────────────
ARC             Automatic Reference Counting — compile-time retain/release insertion
                (not a GC — deterministic deallocation)
retain cycle    A→B→A strong references — memory leak; use weak
weak            Non-owning reference — nil when object deallocated
unowned         Non-owning, non-optional — crash if accessed after dealloc
@escaping       Closure outlives the function — captured vars must be careful
Instruments/Leaks   Find retain cycles + leaked objects
Instruments/Allocations  Memory growth over time

CONCURRENCY
─────────────────
GCD             Grand Central Dispatch — queue-based thread pool
DispatchQueue.main  UI queue (serial, main thread)
DispatchQueue.global()  Background concurrent queues (QoS: userInitiated/utility/background)
DispatchGroup   Wait for multiple async tasks to complete
async/await     Swift 5.5+ structured concurrency (iOS 15+ without backport)
@MainActor      Isolate to main thread (replaces DispatchQueue.main.async)
Task { }        Structured concurrency context — child task of current context
Task.detached   Unstructured task — not bound to current context

DISTRIBUTION
─────────────────
TestFlight      Beta distribution — up to 10,000 external testers, requires App Store Connect
App Store Connect   Apple's portal for managing apps, versions, metadata, pricing
App Review      Human + automated review — typically 24-48 hours for iOS apps
IPA             iOS Package Archive — the signed app bundle (.ipa file)
Archive         Xcode action: build optimized + sign for distribution
Export options  Development / Ad-Hoc / App Store / Enterprise
Ad-Hoc          Distribute to specific devices (up to 100/year) without App Store
Enterprise      In-house distribution (requires $299/year Apple Enterprise Program)
MDM             Mobile Device Management — enterprise device enrollment
Push cert / APNs certificate   Required for sending push notifications (auth key recommended)

KEY APIS
─────────────────
URLSession      HTTP client (replaces deprecated NSURLConnection)
async/await URLSession  Swift 5.5 modern: try await URLSession.shared.data(from: url)
UserDefaults    Key-value store for preferences (persists across launches)
Core Data       ORM: define entities in .xcdatamodeld → NSManagedObject subclasses
SwiftData       Swift 5.9+ successor to Core Data (iOS 17+)
Keychain        Secure credential storage — encrypted by hardware
NotificationCenter  In-process event bus (not push notifications)
UNUserNotificationCenter  Push + local notifications
HealthKit / CoreMotion / CoreLocation   Hardware capability frameworks
ARKit           Augmented reality
Vision          Image analysis / ML inference on images
```

---

### ANDROID — Terms to Load In

```
PLATFORM INTERNALS
─────────────────
Android Runtime (ART)   Successor to Dalvik — AOT compilation + JIT + GC
Zygote          Pre-forked JVM process — every app forks from Zygote for fast start
Binder IPC      Android's primary IPC mechanism (not Unix sockets) — efficient cross-process
AIDL            Android Interface Definition Language — defines Binder interfaces
HAL             Hardware Abstraction Layer — vendor-specific drivers
SELinux         Mandatory access control on all Android (enforcing mode, not permissive)
Verified Boot   Chain of trust from bootloader → kernel → system
SafetyNet / Play Integrity  Google's attestation API — verify device unmodified

APP COMPONENTS (the four building blocks)
─────────────────
Activity        Single screen with UI (like UIViewController on iOS)
Fragment        Reusable UI portion within an Activity
Service         Background work with no UI (music playback, sync)
BroadcastReceiver  React to system/app broadcasts (battery low, SMS received)
ContentProvider  Structured data sharing between apps (contacts, photos)
Intent          Message object — start Activity/Service, deliver broadcast
Explicit Intent  Intent with specific component class name
Implicit Intent  Intent with action string — system finds matching component
IntentFilter    Declares what implicit Intents a component handles

MANIFEST & BUILD
─────────────────
AndroidManifest.xml  Declares: app components, permissions, features, min SDK
package attr    com.company.app — application ID (also used as default namespace)
applicationId   Gradle build.gradle: overrides manifest package (can differ)
minSdk          Minimum Android API level to install on
targetSdk       API level app is designed for (affects behavior compat)
compileSdk      API level used to compile (latest recommended)
Gradle          Build system — build.gradle (Groovy) or build.gradle.kts (Kotlin DSL)
module          Gradle project unit: :app, :feature:home, :core:data
AGP             Android Gradle Plugin — the Android-specific Gradle extension
ProGuard/R8     Code shrinking + obfuscation — R8 is the modern replacement

PROJECT STRUCTURE
─────────────────
app/
  src/
    main/
      java/        (or kotlin/) — source code
      res/         — resources
        layout/    XML layouts (View system)
        drawable/  Images/vectors
        values/    strings.xml, colors.xml, themes.xml
        mipmap/    Launcher icons (multiple densities)
      AndroidManifest.xml
    test/          Unit tests (JVM)
    androidTest/   Instrumentation tests (run on device/emulator)
  build.gradle.kts
build.gradle.kts  (project-level)
settings.gradle.kts  Module declarations

UI FRAMEWORKS
─────────────────
View system     Legacy XML-defined UI (LinearLayout, RecyclerView, etc.)
ViewBinding     Replaces findViewById() — type-safe generated binding class
DataBinding     Two-way binding in XML — heavier than ViewBinding
Jetpack Compose  Declarative UI (Kotlin) — Android's SwiftUI equivalent (preferred now)
@Composable     Annotation for Compose functions
remember { }    Compose state that survives recomposition
LazyColumn      Compose equivalent of RecyclerView
ConstraintLayout  Flexible flat layout for View system (GPU-efficient)
RecyclerView    Efficient scrolling list — replaces ListView
DiffUtil / ListAdapter  Efficient RecyclerView item diffing

ARCHITECTURE (Jetpack components)
─────────────────
ViewModel       Survives rotation — holds UI state
LiveData        Observable data holder — lifecycle-aware (older pattern)
StateFlow/Flow  Kotlin coroutines replacement for LiveData (modern)
Room            SQLite ORM — @Entity, @Dao, @Database annotations
WorkManager     Guaranteed background work (replaces JobScheduler + AlarmManager)
Hilt            Dependency injection (built on Dagger) — @HiltViewModel etc
Navigation      Nav graph + NavController — type-safe fragment/composable navigation
Paging 3        Paginated data loading (RecyclerView or Compose)
Retrofit        HTTP client with interface-based API definition + Gson/Moshi/kotlinx.json
OkHttp          HTTP client underpinning Retrofit — also interceptors for logging/auth

DISTRIBUTION
─────────────────
APK             Android Package — zip of classes.dex + resources + manifest + lib/
AAB             Android App Bundle — upload format to Play; Google builds device-specific APKs
Keystore        JKS or PKCS12 file containing signing key
jarsigner       Sign APK (legacy)
apksigner       Sign APK (modern — v1/v2/v3 signature schemes)
Play App Signing  Google holds your key; you upload with an upload key (safer)
adb install -r myapp.apk   Sideload to connected device
ProGuard mapping.txt  Map obfuscated names back to original (keep this!)

ADB CHEAT SHEET
─────────────────
adb devices              List connected devices/emulators
adb -s <serial> shell    Shell into specific device
adb install app.apk      Install APK
adb push local remote    Copy file to device
adb pull remote local    Copy file from device
adb logcat               Stream logs (filter: adb logcat *:W MyTag:V)
adb logcat -c            Clear log buffer
adb shell am start -n com.example/.MainActivity   Launch activity
adb shell am force-stop com.example              Kill app
adb shell dumpsys activity activities            Show activity stack
adb shell dumpsys meminfo com.example            Memory breakdown
adb shell pm list packages    List installed packages
adb forward tcp:8080 tcp:8080   Port forward (debug servers in app)
```

---

## Dev Environment Setup — Quick Reference

### Windows Dev Box (fresh setup)
```powershell
# Package manager: winget (built-in Windows 11) or choco
winget install Git.Git
winget install Microsoft.VisualStudioCode
winget install Microsoft.DotNet.SDK.8
winget install OpenJS.NodeJS.LTS
winget install Python.Python.3.12
winget install Rustlang.Rustup

# Windows Terminal (if not installed)
winget install Microsoft.WindowsTerminal

# WSL2 (Linux on Windows)
wsl --install                   # Installs Ubuntu by default
wsl --install -d Ubuntu-22.04

# Docker Desktop
winget install Docker.DockerDesktop
```

### Linux Dev Box (Ubuntu)
```bash
# Core tools
sudo apt update && sudo apt install -y \
  build-essential git curl wget \
  python3 python3-pip python3-venv \
  nodejs npm

# Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER   # Add self to docker group (re-login)

# Node version manager (prefer nvm over system node)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install --lts

# Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### macOS Dev Box (fresh)
```bash
# Install Homebrew first
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Core tools
brew install git node python@3.12 rustup-init
brew install --cask visual-studio-code docker

# Xcode (iOS/macOS dev) — from App Store or:
xcode-select --install   # CLI tools only

# Node version manager
brew install nvm
# or: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Rosetta 2 (needed for some x86 tools on Apple Silicon)
softwareupdate --install-rosetta
```

### Android Dev Setup
```bash
# Install Android Studio (handles SDK, emulator, ADB)
# https://developer.android.com/studio

# Or CLI-only (CI):
brew install --cask android-commandlinetools   # macOS
# sdkmanager installed to $ANDROID_HOME

sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"
sdkmanager "emulator" "system-images;android-34;google_apis;x86_64"
avdmanager create avd -n Pixel8 -k "system-images;android-34;google_apis;x86_64"

# Add to PATH:
export ANDROID_HOME=$HOME/Library/Android/sdk    # macOS
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

---

## Decision Cheat Sheet — "What Am I Working With?"

| Signal | What it tells you |
|--------|------------------|
| `HKLM\` or `HKCU\` in configs | Windows Registry — use regedit or reg.exe |
| `.plist` file | macOS/iOS — use PlistBuddy, plutil, or Xcode |
| `build.gradle` or `settings.gradle` | Android Gradle build |
| `xcodeproj` or `xcworkspace` | iOS/macOS Xcode project |
| `AndroidManifest.xml` | Android app |
| `Info.plist` | iOS/macOS app bundle |
| `/etc/systemd/system/` | Linux systemd service |
| `LaunchDaemon` or `LaunchAgent` plist in `/Library/` | macOS launchd service |
| `.msix` or `.appxmanifest` | Windows packaged app (MSIX/UWP/WinUI3) |
| `.ipa` file | iOS app archive |
| `.apk` or `.aab` file | Android app package |
| `smss`, `csrss`, `lsass` in process list | Windows system processes |
| `launchd`, `configd`, `mDNSResponder` | macOS system processes |
| `zygote`, `system_server`, `surfaceflinger` | Android system processes |
| Crash log has `NSException` | iOS/macOS Objective-C exception |
| Crash log has `java.lang.NullPointerException` | Android Java/Kotlin exception |
| `0xC0000005` in crash | Windows Access Violation (NULL deref) |
| `SIGSEGV` in core dump | Linux/macOS segmentation fault |

---

## Common Confusion Points

**`%APPDATA%` vs `%LOCALAPPDATA%`** — APPDATA roams with the user in domain environments (synced); LOCALAPPDATA is local-only. Use LOCALAPPDATA for large caches, APPDATA for config that should follow the user.

**macOS `~/Library` is hidden** — `Library` is hidden in Finder by default. Use `open ~/Library` in Terminal, or Cmd+Shift+G in Finder to navigate there.

**Android `minSdk` vs `targetSdk`** — minSdk = won't install below this. targetSdk = tells Android which behavior compat mode to use. You can target 34 while supporting minSdk 26. The Play Store requires targetSdk to be current.

**iOS Simulator ≠ physical device** — Simulator runs as native macOS process (no ARC trapping, no GPU limits, no memory pressure). Always test on device before submission. Push notifications, HealthKit, CoreNFC, etc. don't work in Simulator.

**Linux `systemd` vs `cron`** — systemd timers are the modern replacement for cron. They integrate with journald (logging), support calendar and monotonic intervals, and run as part of the service framework. Cron still works but has no logs, no dependency handling.

**`adb logcat` is noisy** — Filter aggressively: `adb logcat -s MyTag` for a specific tag, or `adb logcat *:E MyTag:V` for errors-only + verbose for your tag.
