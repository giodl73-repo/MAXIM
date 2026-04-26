# Cross-Platform Development Reference

```
OS-LEVEL DIVERGENCE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  PROCESS MODEL               FILESYSTEM                    IPC / ASYNC
  ─────────────────────────   ─────────────────────────     ─────────────────────────
  Windows                     Windows                       Windows
  CreateProcess()             C:\foo\bar (backslash)        Named pipe \\.\pipe\name
  No fork() — fresh           Drive letters (C:, D:)        IOCP (completion-based)
  process from scratch        NTFS: case-insensitive        Winsock TCP/UDP
  Explicit handle inherit     MAX_PATH=260 (legacy)
  Job Objects for groups      CRLF line endings

  Linux                       Linux                         Linux
  fork() + exec()             /foo/bar (forward slash)      Unix domain socket /tmp/x.sock
  COW clone then replace      No drive letters              epoll / io_uring (readiness)
  All fds inherited           ext4: case-sensitive          POSIX sockets TCP/UDP
  unless O_CLOEXEC            LF line endings               Netlink (kernel ↔ userspace)
  clone() for threads         No max path (POSIX: 4096)     D-Bus (desktop services)

  macOS                       macOS                         macOS
  posix_spawn() preferred     /foo/bar                      Unix domain socket (same as Linux)
  fork() works but restricted APFS: case-insensitive        kqueue (readiness, plus file watch)
  in sandboxed/App Store apps by default                    Mach ports (XPC services)
  Same fd inherit as Linux    LF line endings               XPC (high-level Mach IPC)
                              HFS+: NFD Unicode normalize

  UNICODE / ENCODING          SIGNALS                       CONFIG STORE
  ─────────────────────────   ─────────────────────────     ─────────────────────────
  Windows: UTF-16 internal    Windows: no POSIX signals     Windows: Registry (binary DB)
  NFKC normalization          SetConsoleCtrlHandler         Linux: /etc text files
  char = UTF-16 in Win32 API  (Ctrl+C only)                macOS: .plist files
  Filenames: Unicode (UTF-16) WM_CLOSE for GUI windows      Both: env vars for 12-factor

  Linux: no normalization     Linux: full POSIX signals
  Bytes on disk               SIGTERM/SIGKILL/SIGHUP etc.
  Filename: byte strings      signalfd for event-loop
  (usually UTF-8 by convention but not enforced)

  macOS: NFC (HFS+ uses NFD)  macOS: POSIX signals + kqueue
  Same filename, different    EVFILT_SIGNAL preferred
  byte representation than    in multi-threaded apps
  Linux (NFD) for some chars
```

## OS-Level Portability — Where Code Breaks Across Platforms

### Filesystem Path Differences

```
PATH DIFFERENCES — PRODUCTION BUGS HIDING HERE
═══════════════════════════════════════════════════════════════════════════

  Attribute          Windows                Linux / most POSIX    macOS
  ──────────         ─────────────────────  ──────────────────    ──────────────────────
  Separator          \  (backslash)          /  (forward slash)    /  (forward slash)
  Alt separator      /  (also accepted       (none)                (none)
                      by most Windows APIs)
  Drive letters      C:\, D:\, \\server\sh  No                    No
  Root               C:\  or \\server\share  /                     /
  Case sensitivity   Insensitive+preserving  Sensitive (ext4)      Insensitive by default
                     (NTFS default)          Sensitive (xfs, btrfs) Can be formatted sensitive
  Max path length    260 chars (legacy)      ~4096 bytes           ~1024 bytes
                     32767 with \\?\ prefix  per component: 255    per component: 255
  Null char in path  Not allowed             Not allowed           Not allowed
  Other reserved     CON, PRN, AUX, NUL,    No reserved names     No reserved names
  names              COM1-9, LPT1-9
                     Cannot be filenames
  Trailing spaces    Stripped silently       Valid (unusual)        Valid (unusual)
  Symlinks           Require Admin or        Standard               Standard; /etc → /private/etc
                     Developer Mode; are
                     not followed by all
                     tools (Explorer hides)

  Path separator in code — the right way:
    Python:    pathlib.Path('a') / 'b' / 'c'  (OS-native, correct everywhere)
    .NET:      Path.Combine("a", "b", "c")     (correct; avoids \ vs / issue)
    Node.js:   path.join('a', 'b', 'c')        (correct)
    Wrong:     "a" + "/" + "b"                  (fails on Windows if dir has C:\)
    Also wrong: "a\\b"                          (fails on Linux/macOS)

  Max path gotcha on Windows:
    Legacy Win32 APIs enforce MAX_PATH=260.
    Opt-in to long paths: HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\
      LongPathsEnabled=1  (Windows 10 1607+)
    OR use \\?\ prefix: \\?\C:\very\long\path
    .NET: automatically uses \\?\ prefix for long paths in .NET 6+
    Docker on Windows: /var/lib/docker paths can exceed 260 — enable long paths
```

### Line Endings — CRLF vs LF

```
LINE ENDING SEMANTICS
═══════════════════════════════════════════════════════════════════════════

  Windows:  \r\n  (CRLF, 0x0D 0x0A)  — text mode default since MS-DOS
  Linux:    \n    (LF, 0x0A)          — POSIX standard
  macOS:    \n    (LF, 0x0A)          — changed from \r in OS X 10.0
  Old Mac:  \r    (CR, 0x0D)          — pre-OS X; still used by some Excel exports

  The production bug:
    Developer on Windows checks in shell script
    git config core.autocrlf = true (Windows default in Git for Windows)
    Git converts LF → CRLF on checkout
    Script.sh checked out on Windows → contains CRLF
    CI runs in Docker (Linux) → #!/bin/bash\r — shebang has trailing \r
    bash: cannot execute: No such file  (or similar cryptic error)

  Fix: .gitattributes (committed to repo, overrides local config)
    # .gitattributes
    * text=auto                   # auto-detect text files, normalize to LF in repo
    *.sh text eol=lf              # always LF for shell scripts
    *.bat text eol=crlf           # always CRLF for batch files
    *.ps1 text eol=crlf           # PowerShell on Windows wants CRLF
    *.sln text eol=crlf           # Visual Studio solution files
    *.png binary                  # no conversion for binary files

  git config audit:
    git config core.autocrlf      # true (Win) / input (Mac/Linux) / false (no convert)
    git config core.eol           # lf / crlf / native

  Check for CRLFs in existing files:
    file script.sh                # "with CRLF line terminators" if CRLF
    cat -A script.sh | head       # ^M at end of lines = CR (\r)

  Fix CRLFs in place:
    sed -i 's/\r//' script.sh      # Linux/macOS
    dos2unix script.sh             # if dos2unix installed
```

### Case Sensitivity Bugs

```
CASE SENSITIVITY TRAP
═══════════════════════════════════════════════════════════════════════════

  Windows (NTFS):  case-insensitive, case-preserving
    FOO.TXT and foo.txt are the SAME file — last write wins
  Linux (ext4):    case-sensitive
    FOO.TXT and foo.txt are DIFFERENT files — can coexist
  macOS (APFS):    case-insensitive by default
    Same as Windows by default; developer machines can run case-sensitive APFS

  The bug pattern:
    Developer on Windows or macOS: import './Utils'
    utils.ts exists on disk as utils.ts (lowercase)
    Works: Windows/macOS filesystem resolves 'Utils' → 'utils.ts'
    Fails: Linux CI (Docker, GitHub Actions Ubuntu) — 'Utils' ≠ 'utils.ts'

  Detectors:
    TypeScript: "forceConsistentCasingInFileNames": true  in tsconfig.json
    ESLint: import/no-unresolved (with case-sensitive resolver)
    CI: run on Linux even if devs use Windows/Mac

  Docker on Windows:
    Docker Desktop mounts C:\ via VirtioFS / Hyper-V 9P
    The container filesystem IS case-sensitive (Linux ext4)
    Code that works when run natively on Windows may fail in your Docker container

  Git case sensitivity:
    git mv Readme.md README.md   # might silently do nothing on case-insensitive FS
    Use: git mv Readme.md tmp && git mv tmp README.md  (two-step)
    Or:  git config core.ignorecase false  (use carefully)
```

### Unicode Normalization — The Silent Gotcha

```
UNICODE NORMALIZATION ACROSS OSes
═══════════════════════════════════════════════════════════════════════════

  Forms:
    NFC  (Canonical Decomposition + Canonical Composition)    — used by Windows, Linux common
    NFD  (Canonical Decomposition)                            — used by macOS HFS+ filesystem
    NFKC (Compatibility Decomposition + Composition)          — Windows Registry, some Win32 APIs
    NFD  and NFC differ for composed characters like é:
      NFC: U+00E9 (single code point: é)
      NFD: U+0065 U+0301 (e + combining acute accent — two code points)

  macOS HFS+ (legacy, not APFS): stores filenames in NFD
  macOS APFS: preserves whatever form you write (no normalization)
  Linux: no normalization — bytes in, bytes out
  Windows: NTFS stores as UTF-16, no normalization enforced

  The bug:
    File created on macOS HFS+ with filename "café" → stored as NFD on disk
    Copied to Linux (rsync, scp) → arrives as NFD byte sequence
    Linux program: filename == "café" (NFC comparison) → NOT EQUAL
    Strings look identical on screen, compare unequal in code

  Fix in code:
    Python:  unicodedata.normalize('NFC', filename)
    JS/TS:   filename.normalize('NFC')
    .NET:    string.Normalize(NormalizationForm.FormC)

  Practical rule: normalize to NFC at IO boundaries
  (when reading filenames, user input, or data from other systems)
```

### Process Creation Model — Cross-OS Bridge

```
PROCESS CREATION MODELS
═══════════════════════════════════════════════════════════════════════════

  Windows: CreateProcess()          Linux: fork() + exec()        macOS: posix_spawn() preferred
  ─────────────────────────         ─────────────────────────     ───────────────────────────────
  Fresh process from scratch         Clone current process          Combination: avoids full fork
  No fork() at all                   (COW copy of address space)    overhead; preferred on Apple
  All handles must be explicit:       → exec() replaces image        Silicon and in sandboxed apps
    bInheritHandle = TRUE on          All fds inherited unless       (fork is restricted in some
    SECURITY_ATTRIBUTES, or           O_CLOEXEC set at open time     App Store / sandbox contexts)
    UpdateProcThreadAttribute()       (or SOCK_CLOEXEC, etc.)       iOS: fork() not available at all
    for handle list

  Security context:                  Security context:              Security context:
    Token explicitly specified         uid/gid inherited from parent  uid/gid inherited; can setuid
    or inherits calling process token  setuid executable changes uid  posix_spawn actions can
    CreateProcessAsUser() for           post-exec                      chdir, dup2, close fds
    impersonation

  fd/handle inheritance:             fd inheritance:                fd inheritance:
    Explicit opt-in per handle         All fds unless O_CLOEXEC       posix_spawn_file_actions:
    DuplicateHandle() to share          (Python subprocess,            explicit file action list
    across non-related processes        subprocess32, Go exec.Cmd      (not inherited by default
                                        all set O_CLOEXEC by default)   without explicit action)

  Env vars:                          Env vars:                      Env vars:
    lpEnvironment param or inherit     environ[] inherited           Same as Linux fork/exec
    CreateProcess always starts fresh   (unless execve() with new env)(posix_spawn with new env)

  Process group / session:           Process group / session:       Same as Linux
    Job Objects (Windows-specific)     setsid() / setpgid()          setpgid() / setsid()
    → CPU/memory limits per group      process groups for signal      (no Job Objects)
    → on child, kill all               delivery to group

  Security implication of no fork on Windows:
    Every new process starts clean — no accidental fd/secret inheritance
    Explicit handle list forces developer to think about what is shared
    Linux/macOS: a fd opened before fork() is silently inherited by child
    unless O_CLOEXEC was set — common security bug in servers that use fork()

  Cross-platform process launcher libraries:
    Python:     subprocess.Popen() — handles all three platforms
    Node.js:    child_process.spawn() — handles all three
    Rust:       std::process::Command — handles all three
    .NET:       Process.Start(ProcessStartInfo) — handles all three
    Go:         os/exec.Command — handles all three
    All abstract fork+exec (Unix) or CreateProcess (Windows) behind one API.
```

### Cross-Platform IPC — Named Pipes vs Unix Domain Sockets

```
LOCAL IPC MECHANISMS — CROSS-PLATFORM COMPARISON
═══════════════════════════════════════════════════════════════════════════

  Windows Named Pipe               Unix Domain Socket (Linux + macOS)
  ────────────────────────────     ────────────────────────────────────────
  Address: \\.\pipe\myserver       Address: /tmp/myserver.sock  (filesystem path)
  or \\hostname\pipe\myserver      (no remote addressing for AF_UNIX)

  API:                             API:
    Server: CreateNamedPipe()        Server: socket(AF_UNIX, SOCK_STREAM, 0)
    Client: CreateFile(\\.\pipe\...) bind(/tmp/sock) → listen() → accept()
    Both: ReadFile() / WriteFile()   Client: connect(/tmp/sock)
    Async: overlapped I/O + IOCP     Both: read() / write() / send() / recv()
                                     Async: epoll / kqueue / io_uring

  .NET:                            .NET (5+):
    NamedPipeServerStream            UnixDomainSocketEndPoint
    NamedPipeClientStream            Same Socket API as TCP

  Permissions:                     Permissions:
    ACL on pipe object               Filesystem permissions on socket path
    OpenNamedPipe with access flags  chmod / chown on /tmp/sock
                                     (directory execute bit needed too)

  Visual Studio / VS Code use case:
    Language Server Protocol (LSP) must support both:
    Windows:  \\.\pipe\vscode-<extension>
    Linux:    /tmp/vscode-<extension>.sock
    macOS:    /tmp/vscode-<extension>.sock (same as Linux)

  Cross-platform server that supports both:
  ```
  if platform == 'win32':
      server = NamedPipeServer('\\\\.\\pipe\\myapp')
  else:
      server = UnixSocketServer('/tmp/myapp.sock')
  ```
  Or use TCP loopback (127.0.0.1:PORT) — works everywhere, no platform-specific code,
  slight overhead but avoids the named-pipe/Unix-socket split entirely.
  gRPC defaults to TCP; language servers often offer TCP as fallback.

  Passing file descriptors cross-platform:
    Linux/macOS: SCM_RIGHTS over AF_UNIX socket (sendmsg with ancillary data)
    Windows:     DuplicateHandle() — requires target process handle
    No universal API — platform detection required
```

## The Landscape — Big Picture

```
  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  Target Platforms                                                           │
  │                                                                             │
  │  iOS ──────────────────────────────────────────────────────┐                │
  │  Android ──────────────────────────────────────────────────┤                │
  │  Windows ──────────────────────────────────────────────────┤                │
  │  macOS ────────────────────────────────────────────────────┤                │
  │  Linux ────────────────────────────────────────────────────┤                │
  │  Web ──────────────────────────────────────────────────────┘                │
  │                         ▲                                                   │
  │  ONE CODEBASE ───────────┘ (aspiration)                                     │
  │                                                                             │
  │  ┌─────────────┬──────────────┬─────────────┬────────────┬───────────┐      │
  │  │  .NET MAUI  │ React Native │   Flutter   │  Electron  │   Tauri   │    │
  │  │  C# / XAML  │  JS / TS     │    Dart     │  JS + Node │  JS + Rust│    │
  │  │  iOS/And/   │  iOS/Android │  iOS/And/   │  Windows/  │  Win/Mac/ │    │
  │  │  Win/macOS  │  Web(limited)│  Win/Mac/   │  macOS/    │  Linux    │    │
  │  │             │              │  Linux/Web  │  Linux     │           │    │
  │  └─────────────┴──────────────┴─────────────┴────────────┴───────────┘    │
  │                                                                             │
  │  ┌──────────────────────────────────────────────────────────────────────┐  │
  │  │  Capacitor / Ionic — web app wrapped in native shell                 │  │
  │  └──────────────────────────────────────────────────────────────────────┘  │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Abstraction Spectrum

```
  FULLY NATIVE ◄─────────────────────────────────────────────► WEBVIEW WRAPPER
  100% native perf                                              pure web in shell
  most code                                                     least code
  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────────┐
  │ Swift    │   │ Flutter  │   │  MAUI    │   │  React   │   │  Electron /  │
  │ Kotlin   │   │          │   │          │   │  Native  │   │  Capacitor / │
  │ (native) │   │ Custom   │   │ Handler- │   │          │   │  Tauri       │
  │          │   │ renderer │   │ mapped   │   │ Native   │   │              │
  │ 2 repos  │   │ (Skia/   │   │ native   │   │ widgets  │   │ Chromium /   │
  │ 2 teams  │   │ Impeller)│   │ widgets  │   │ via JS   │   │ OS webview   │
  │          │   │          │   │          │   │ bridge   │   │              │
  │ All APIs │   │ Any look │   │ Natve    │   │ Mostly   │   │ Web APIs     │
  │ day one  │   │ cross-   │   │ look on  │   │ native   │   │ + some       │
  │          │   │ platform │   │ each OS  │   │ feel     │   │ native APIs  │
  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────────┘

  Trade-off axis:
  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  ←── higher: performance, API access, native feel, new OS feature support   │
  │  ←── lower:  code sharing, hiring pool, iteration speed, cost               │
  │                                                                             │
  │  →── higher: code sharing %, web skills leverage, prototype speed           │
  │  →── lower:  performance, native API coverage, platform authenticity        │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## Cross-Platform Decision Matrix

| Attribute | .NET MAUI | React Native | Flutter | Electron | Tauri | Capacitor/Ionic |
|-----------|-----------|--------------|---------|----------|-------|-----------------|
| **Language** | C# | JS / TypeScript | Dart | JS / TypeScript | JS + Rust | JS / TypeScript |
| **UI approach** | Handler-mapped native widgets | Native widgets via JS bridge / JSI | Custom renderer (Skia/Impeller) | HTML/CSS in Chromium | HTML/CSS in OS webview | HTML/CSS in native webview |
| **Targets: Mobile** | iOS, Android | iOS, Android | iOS, Android | No | No | iOS, Android |
| **Targets: Desktop** | Windows (WinUI 3), macOS (Mac Catalyst) | No (limited) | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux | No |
| **Targets: Web** | Blazor Hybrid (partial) | Experimental | Flutter Web | No | No | Yes (it IS a web app) |
| **Code sharing** | ~80-90% | ~70-85% | ~85-95% | ~95% | ~90% | ~95% |
| **Performance** | Near-native | Good (JSI) / was poor (bridge) | Near-native (custom renderer) | Heavy (Chromium per window) | Good (native webview, Rust core) | Web perf |
| **Native look & feel** | Yes (per-platform widgets) | Mostly yes | No (consistent custom look) | No | No | No |
| **Microsoft support** | First-party | Community + Meta | Community + Google | Community | Community | Community |
| **Maturity** | Medium (2022; replaces Xamarin) | High (2015, Meta-backed) | High (2017, Google-backed) | Very high (2013, Slack/VS Code) | Growing (2022) | Medium |
| **Ecosystem / packages** | NuGet + .NET ecosystem | npm + React ecosystem | pub.dev (growing) | npm + Node ecosystem | Cargo + npm | npm + web ecosystem |
| **Team profile** | .NET / C# team | React / JS team | Any (Dart is learnable) | Web / Node team | Web + Rust team | Web team |
| **Install size** | ~30-80 MB | ~10-30 MB | ~10-25 MB | 50-200 MB | 3-10 MB | ~5-15 MB |
| **Primary weakness** | Mac Catalyst limitations; not SwiftUI | New Architecture migration complexity | No native widgets (platform-purists object) | Size + memory (Chromium per window) | Webview inconsistency across OS; Rust barrier | WebView is not native; browser engine limits |
| **Best for** | .NET enterprise teams; Windows + mobile from one codebase | React teams going mobile; apps with heavy web component | Consistent custom design; high-quality cross-platform | VS Code-style desktop tools; developer tools; productivity apps | New desktop app; size/security-conscious; OK with Rust | Existing web app needs native packaging |

---

## .NET MAUI — Microsoft's Cross-Platform Answer

### Architecture

```
  ┌───────────────────────────────────────────────────────────────────┐
  │  Your MAUI App (C# / XAML)                                        │
  │  ┌──────────────────────────────────────────────────────────┐     │
  │  │  MAUI Shell: navigation, tabs, flyout menu              │     │
  │  │  ContentPage, ContentView, DataTemplate, ControlTemplate│     │
  │  └──────────────────────────────────────────────────────────┘     │
  │  ┌──────────────────────────────────────────────────────────┐     │
  │  │  Handlers (new in MAUI — replace Xamarin Renderers)      │     │
  │  │  Button handler → UIButton (iOS) / android.Button (And)  │     │
  │  │  Label handler  → UILabel  (iOS) / android.TextView      │     │
  │  │  Custom handlers: override per platform                  │     │
  │  └──────────────────────────────────────────────────────────┘     │
  │                                                                   │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
  │  │  iOS     │  │ Android  │  │ Windows  │  │ macOS (Catalyst) │ │
  │  │  .NET    │  │  .NET    │  │  .NET    │  │  .NET            │ │
  │  │  for iOS │  │  for And │  │  for Win │  │  for macOS       │ │
  │  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘ │
  └───────────────────────────────────────────────────────────────────┘

  Single project with platform folders:
  MyApp/
  ├── MyApp.csproj    ← multi-targeted: net8.0-ios; net8.0-android; net8.0-windows; net8.0-maccatalyst
  ├── Platforms/
  │   ├── Android/    ← AndroidManifest.xml, MainActivity.cs, platform code
  │   ├── iOS/        ← Info.plist, AppDelegate.cs, platform code
  │   ├── Windows/    ← Package.appxmanifest, App.xaml, platform code
  │   └── MacCatalyst/
  ├── Resources/
  │   ├── Images/     ← single source image, MAUI generates all densities
  │   ├── Fonts/
  │   └── Raw/
  └── ViewModels/, Views/, Models/, Services/
```

**MAUI vs Xamarin.Forms — what changed:**

| Aspect | Xamarin.Forms | .NET MAUI |
|--------|---------------|-----------|
| Project structure | 1 shared + N platform projects | Single project, multi-targeted |
| Foundation | Mono runtime (separate from .NET) | .NET 6+ unified runtime |
| Renderers | Full class per control per platform | Handlers (lighter, partial class overrides) |
| Hot reload | Limited | Full XAML hot reload + C# hot reload |
| Web integration | WebView only | BlazorWebView (run Blazor components natively) |
| .NET version | Xamarin.* packages | Microsoft.Maui.* NuGet packages |

**MVVM with CommunityToolkit.Mvvm (source-generated, no reflection):**
```csharp
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

// [ObservableProperty] generates: property, backing field, OnXChanged partial method,
// INotifyPropertyChanged notifications — all via source generator
[ObservableObject]
public partial class UserViewModel
{
    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(FullName))]   // also notifies FullName
    [NotifyCanExecuteChangedFor(nameof(SaveCommand))]  // revalidates command
    private string _firstName = string.Empty;

    [ObservableProperty]
    private string _lastName = string.Empty;

    public string FullName => $"{FirstName} {LastName}";

    // [RelayCommand] generates ICommand property with execute + canExecute wiring
    [RelayCommand(CanExecute = nameof(CanSave))]
    private async Task SaveAsync(CancellationToken cancellationToken)
    {
        await _userService.SaveAsync(new User(FirstName, LastName), cancellationToken);
    }

    private bool CanSave() => !string.IsNullOrWhiteSpace(FirstName);
}
```

**MAUI Shell — navigation pattern:**
```xaml
<Shell xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
       x:Class="MyApp.AppShell">

    <Shell.FlyoutHeader>
        <Label Text="MyApp" />
    </Shell.FlyoutHeader>

    <FlyoutItem Title="Home" Icon="home.png">
        <ShellContent ContentTemplate="{DataTemplate views:HomePage}" Route="home" />
    </FlyoutItem>

    <FlyoutItem Title="Settings">
        <ShellContent ContentTemplate="{DataTemplate views:SettingsPage}" Route="settings" />
    </FlyoutItem>

    <TabBar>
        <Tab Title="Feed">
            <ShellContent ContentTemplate="{DataTemplate views:FeedPage}" Route="feed" />
        </Tab>
        <Tab Title="Profile">
            <ShellContent ContentTemplate="{DataTemplate views:ProfilePage}" Route="profile" />
        </Tab>
    </TabBar>
</Shell>
```

```csharp
// Navigate
await Shell.Current.GoToAsync("//feed");
await Shell.Current.GoToAsync($"detail?id={itemId}");
await Shell.Current.GoToAsync("..");  // pop

// Register routes (not in Shell hierarchy)
Routing.RegisterRoute("detail", typeof(DetailPage));
```

**Blazor Hybrid — run web components in native app:**
```xml
<!-- In MAUI page -->
<BlazorWebView HostPage="wwwroot/index.html">
    <BlazorWebView.RootComponents>
        <RootComponent Selector="#app" ComponentType="{x:Type blazor:Main}" />
    </BlazorWebView.RootComponents>
</BlazorWebView>
```
```csharp
// In Blazor component — can call native services injected via MAUI DI
@inject IUserService UserService  // injected from MAUI's DI container
@inject NavigationManager Nav

@code {
    private async Task NavigateToSettings()
    {
        // Can navigate MAUI shell from Blazor
        await Shell.Current.GoToAsync("settings");
    }
}
```

**Blazor Hybrid use case:** Reuse existing Blazor web components in a MAUI native app. One component library runs in: ASP.NET Core web app, MAUI Android/iOS app, MAUI Windows/macOS app. Share component code across web + native.

**MAUI limitations — be clear-eyed:**
- **Mac Catalyst**: iOS app running under Catalyst emulation — not a native macOS app; AppKit APIs not accessible; App Store review applies iOS rules
- **Vendor control**: MAUI is Microsoft; if a new iOS/Android API ships, you wait for MAUI team to expose it
- **Community size**: smaller ecosystem than React Native or Flutter; fewer third-party controls
- **Not SwiftUI**: if you need deep iOS integration, you're fighting platform conventions

---

## React Native

### Architecture

**Old Architecture (bridge — mostly legacy):**
```
  JS Thread                    Bridge                   Native Thread
  ┌─────────────────┐         ┌─────────────────┐       ┌──────────────────┐
  │  React + JS     │ async   │ JSON serialized │ async │  iOS / Android   │
  │  business logic │────────▶│ message queue   │──────▶│  UI rendering    │
  │                 │◀────────│                 │◀──────│  Native modules  │
  └─────────────────┘         └─────────────────┘       └──────────────────┘
  Problem: every UI update = serialization + async round-trip = jank
```

**New Architecture (JSI — JavaScript Interface):**
```
  JS Thread                              Native Thread
  ┌──────────────────────────────┐       ┌──────────────────────────────┐
  │  Hermes JS Engine            │       │  Fabric (new renderer)       │
  │  + JSI (C++ bindings)        │──────▶│  Synchronous UI updates      │
  │                              │       │                              │
  │  TurboModules                │──────▶│  TurboModules: lazy-load,    │
  │  (typed, lazy native mods)   │       │  direct C++ access, typed    │
  └──────────────────────────────┘       └──────────────────────────────┘
  Result: synchronous JS→native calls, no serialization overhead
```

**Expo — the recommended starting point:**
```
  ┌──────────────────────────────────────────────────────────────────┐
  │  Expo SDK                                                        │
  │  ├── Managed workflow: expo prebuild generates native code       │
  │  │   No Xcode/Android Studio needed for most development         │
  │  │   Expo Go app: instant preview on device without build        │
  │  │                                                               │
  │  ├── Bare workflow: ejected, full native project access          │
  │  │   Run: npx expo prebuild → generates ios/ and android/        │
  │  │                                                               │
  │  └── EAS (Expo Application Services)                             │
  │      ├── EAS Build: cloud build for iOS + Android                │
  │      ├── EAS Submit: automated App Store + Play Store submission │
  │      └── EAS Update: OTA updates to JS bundle (no store review)  │
  └──────────────────────────────────────────────────────────────────┘
```

**Core React Native:**
```tsx
import React, { useState, useEffect } from 'react';
import {
  View, Text, FlatList, TouchableOpacity,
  StyleSheet, ActivityIndicator, Platform
} from 'react-native';

// Platform-specific code
const buttonStyle = Platform.select({
  ios: { borderRadius: 12 },
  android: { borderRadius: 4 },
});

// Component — same React patterns as web
function UserList({ navigation }) {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers().then(data => {
      setUsers(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <ActivityIndicator style={styles.center} />;

  return (
    <FlatList
      data={users}
      keyExtractor={item => item.id}
      renderItem={({ item }) => (
        <TouchableOpacity
          style={styles.row}
          onPress={() => navigation.navigate('Detail', { userId: item.id })}
        >
          <Text style={styles.name}>{item.name}</Text>
        </TouchableOpacity>
      )}
    />
  );
}

// StyleSheet.create — NOT CSS; maps to native layout (Yoga flex engine)
const styles = StyleSheet.create({
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  row: { padding: 16, borderBottomWidth: StyleSheet.hairlineWidth },
  name: { fontSize: 16, fontWeight: '600' },
});
```

**React Navigation:**
```tsx
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function HomeTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Feed" component={FeedScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeTabs} options={{ headerShown: false }} />
        <Stack.Screen name="Detail" component={DetailScreen} />
        <Stack.Screen name="Settings" component={SettingsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

**When React Native makes sense:**
- You have a React web team that needs to ship mobile
- Heavy shared business logic with a web app (custom hooks, state stores, API clients)
- Timeline pressure — web React devs are productive in RN within days
- You need Web + iOS + Android from one team

**React Native limitations:**
- Complex animations can still stutter if not using Reanimated properly
- New Architecture adoption is ongoing — some third-party libraries lag
- Debug experience is multi-layer (JS + native) — harder to diagnose native crashes
- Custom native UI components require iOS/Android knowledge

---

## Flutter

### Architecture

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Your Dart Code                                                      │
  │  Widget tree: everything is a widget                                 │
  │  StatelessWidget / StatefulWidget / InheritedWidget                  │
  └─────────────────────────────────────┬────────────────────────────────┘
                                        │ compiled to
  ┌─────────────────────────────────────▼────────────────────────────────┐
  │  Dart VM (debug) / AOT native code (release)                         │
  │  Dart → arm64 / x86_64 machine code via dart2native                  │
  └─────────────────────────────────────┬────────────────────────────────┘
                                        │ calls
  ┌─────────────────────────────────────▼────────────────────────────────┐
  │  Flutter Engine (C++)                                                │
  │  Skia (older) / Impeller (newer, iOS default, Android GA in 3.x)     │
  │  Text layout, image decoding, canvas API                             │
  └─────────────────────────────────────┬────────────────────────────────┘
                                        │ renders to
  ┌─────────────────────────────────────▼────────────────────────────────┐
  │  Platform Canvas                                                     │
  │  iOS: Metal surface  │  Android: Vulkan/GL surface  │  Web: Canvas   │
  └──────────────────────┴────────────────────────────────┴──────────────┘

  KEY INSIGHT: Flutter bypasses the OS's native widget system entirely.
  It draws every pixel itself. Your app looks identical on iOS and Android.
  This is a design choice — platform purists object; designers love it.
```

**Widget tree — the mental model:**
```dart
// Everything is immutable configuration (Widget)
// Flutter diffs the widget tree → generates Element tree → renders RenderObject tree

class UserCard extends StatelessWidget {
  const UserCard({
    super.key,
    required this.user,
    required this.onFollow,
  });

  final User user;
  final VoidCallback onFollow;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(user.name, style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 8),
            Text(user.bio),
            ElevatedButton(
              onPressed: onFollow,
              child: const Text('Follow'),
            ),
          ],
        ),
      ),
    );
  }
}

// StatefulWidget — for local mutable state
class Counter extends StatefulWidget {
  const Counter({super.key});
  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _count = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_count'),
        ElevatedButton(
          onPressed: () => setState(() => _count++),  // setState triggers rebuild
          child: const Text('Increment'),
        ),
      ],
    );
  }
}
```

**State management evolution in Flutter:**
```
  setState (trivial)
  │ → fine for local UI state within one widget
  │
  InheritedWidget (manual)
  │ → Flutter's built-in prop drilling solution; low-level
  │
  Provider (simple)
  │ → ChangeNotifier + ChangeNotifierProvider; beginner-friendly
  │
  Riverpod (intermediate — recommended for most apps)
  │ → type-safe, testable, no BuildContext required for providers
  │ → ref.watch(), ref.read(), AsyncNotifierProvider
  │
  Bloc (large teams / complex apps)
  │ → Events in → States out; strict unidirectional data flow
  │ → BlocBuilder, BlocListener, BlocConsumer
  └─ most predictable; most boilerplate; best for regulated industries
```

**Riverpod pattern:**
```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';

// Provider definition — lives outside widget tree
@riverpod
Future<List<User>> users(UsersRef ref) async {
  final repo = ref.watch(userRepositoryProvider);
  return repo.getUsers();
}

// Widget consumes provider
class UserListScreen extends ConsumerWidget {
  const UserListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final usersAsync = ref.watch(usersProvider);

    return usersAsync.when(
      loading: () => const CircularProgressIndicator(),
      error: (error, stack) => Text('Error: $error'),
      data: (users) => ListView.builder(
        itemCount: users.length,
        itemBuilder: (context, index) => UserCard(
          user: users[index],
          onFollow: () => ref.read(usersProvider.notifier).followUser(users[index].id),
        ),
      ),
    );
  }
}
```

**Platform channels — calling native code from Dart:**
```dart
// Dart side
static const platform = MethodChannel('com.example.myapp/native');

Future<String> getBatteryLevel() async {
  try {
    final level = await platform.invokeMethod<int>('getBatteryLevel');
    return 'Battery: $level%';
  } on PlatformException catch (e) {
    return 'Failed: ${e.message}';
  }
}
```

```kotlin
// Android side (Kotlin)
MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.myapp/native")
    .setMethodCallHandler { call, result ->
        if (call.method == "getBatteryLevel") {
            val level = getBatteryLevel()
            if (level != -1) result.success(level)
            else result.error("UNAVAILABLE", "Battery level not available", null)
        } else {
            result.notImplemented()
        }
    }
```

**Dart Isolates — concurrency without shared memory:**
```dart
// Dart is single-threaded per isolate — like JS but explicit
// For CPU-heavy work, spawn an isolate (separate memory heap, message-passing)

import 'dart:isolate';

Future<int> computeInBackground(int input) async {
  return await Isolate.run(() {
    // This runs in a new isolate — no shared memory with main
    return expensiveComputation(input);
  });
}

// Flutter's compute() is a convenience wrapper:
final result = await compute(myHeavyFunction, inputData);
```

**Hot reload vs hot restart:**
```
  Hot reload   (r)  — inject updated Dart code into running VM; preserves state
                       works for: UI changes, logic changes (not class structure)
  Hot restart  (R)  — restart Dart VM, lose state, re-run from main()
                       works for: anything, including class structure changes
```

**Flutter strengths:**
- Pixel-perfect custom designs that look identical on all platforms
- Very fast development iteration (hot reload)
- Strong Google backing; Material 3 built-in; Cupertino widgets for iOS look
- Growing — large pub.dev package ecosystem
- Web and desktop targets maturing

**Flutter weaknesses:**
- Does not use native widgets — accessibility can lag platform standards
- Dart is a niche language — smaller hiring pool than TS/Swift/Kotlin
- Impeller rendering engine still maturing on some targets
- Bundle size: Flutter engine adds ~4-7MB to app

---

## Electron — Desktop via Web Technologies

### Architecture

```
  ┌───────────────────────────────────────────────────────────────────────┐
  │  Electron Application                                                 │
  │                                                                       │
  │  ┌─────────────────────────────────────────────────────────────┐      │
  │  │  Main Process  (Node.js)                                    │     │
  │  │  app.ts / main.ts                                          │     │
  │  │  ├── BrowserWindow management                              │     │
  │  │  ├── Native menus, system tray, notifications              │     │
  │  │  ├── File system, OS APIs                                  │     │
  │  │  ├── Auto-updater                                          │     │
  │  │  └── ipcMain.handle('channel', handler)                    │     │
  │  └──────────────────────────┬──────────────────────────────────┘     │
  │                             │  IPC (inter-process communication)      │
  │  ┌──────────────────────────▼──────────────────────────────────┐     │
  │  │  Preload Script  (bridge — runs in renderer, has Node access)│    │
  │  │  contextBridge.exposeInMainWorld('api', {                   │     │
  │  │    readFile: (path) => ipcRenderer.invoke('read-file', path)│     │
  │  │  })                                                         │     │
  │  └──────────────────────────┬──────────────────────────────────┘     │
  │                             │  contextIsolation boundary              │
  │  ┌──────────────────────────▼──────────────────────────────────┐     │
  │  │  Renderer Process  (Chromium — one per BrowserWindow)       │     │
  │  │  Your React / Vue / Svelte / vanilla web app                │     │
  │  │  window.api.readFile(path)  ← uses exposed API only         │     │
  │  │  NO direct Node access (contextIsolation = true)            │     │
  │  └─────────────────────────────────────────────────────────────┘     │
  └───────────────────────────────────────────────────────────────────────┘
```

**The security model — contextBridge is non-negotiable:**
```typescript
// preload.ts — runs in renderer context WITH Node access
// This is the ONLY safe way to expose native APIs
import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('api', {
  // Only expose what you need — principle of least privilege
  readFile: (path: string) => ipcRenderer.invoke('read-file', path),
  writeFile: (path: string, data: string) => ipcRenderer.invoke('write-file', path, data),
  openFile: () => ipcRenderer.invoke('open-file-dialog'),
  onUpdateAvailable: (cb: () => void) => ipcRenderer.on('update-available', cb),
});

// main.ts — main process handles the IPCs
import { ipcMain, dialog, app } from 'electron';
import { readFile, writeFile } from 'fs/promises';

ipcMain.handle('read-file', async (event, path: string) => {
  return readFile(path, 'utf-8');
});

ipcMain.handle('open-file-dialog', async () => {
  const result = await dialog.showOpenDialog({
    properties: ['openFile'],
    filters: [{ name: 'Text Files', extensions: ['txt', 'md'] }]
  });
  return result.filePaths[0];
});
```

**BrowserWindow creation pattern:**
```typescript
import { app, BrowserWindow } from 'electron';
import path from 'path';

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,   // MUST be true (default since Electron 12)
      nodeIntegration: false,   // MUST be false — no Node in renderer
      sandbox: true,            // additional isolation
    },
  });

  // Dev: load Vite dev server
  // Prod: load built index.html
  if (process.env.NODE_ENV === 'development') {
    win.loadURL('http://localhost:5173');
    win.webContents.openDevTools();
  } else {
    win.loadFile(path.join(__dirname, 'renderer/index.html'));
  }
}

app.whenReady().then(createWindow);
```

**Packaging and code signing:**
```bash
# electron-builder config in package.json
"build": {
  "appId": "com.example.myapp",
  "mac": {
    "category": "public.app-category.productivity",
    "hardenedRuntime": true,
    "entitlements": "entitlements.mac.plist",
    "sign": "Developer ID Application: Your Name (TEAMID)"
  },
  "win": {
    "certificateFile": "cert.pfx",
    "certificatePassword": "...",
    "signingHashAlgorithms": ["sha256"]
  },
  "nsis": { "oneClick": false, "allowToChangeInstallationDirectory": true },
  "publish": [{ "provider": "github" }]
}
```

**Auto-update (electron-updater):**
```typescript
import { autoUpdater } from 'electron-updater';

autoUpdater.checkForUpdatesAndNotify();

autoUpdater.on('update-available', (info) => {
  // send to renderer via ipcMain.emit or BrowserWindow.webContents.send
});

autoUpdater.on('update-downloaded', () => {
  autoUpdater.quitAndInstall();  // or prompt user
});
```

**Why Electron despite its size:** VS Code, Slack, Discord, Figma, 1Password, GitHub Desktop, Notion — these are all Electron. The model works. The 100MB size complaint matters less as SSDs dominate. The development speed advantage is massive. The existing Chromium engine means predictable, well-tested rendering.

**Electron vs NW.js vs other web desktop tools:**

| Tool | Main distinction |
|------|-----------------|
| Electron | Node in main, Chromium in renderer; most mature ecosystem |
| NW.js | Node + Chromium merged (less isolation); older; less popular |
| Tauri | Rust core + OS webview; much smaller; see below |
| neutralinojs | Lightweight; OS webview; simpler feature set |

---

## Tauri — Modern Electron Alternative

### Architecture

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Tauri Application                                                   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐     │
  │  │  Rust Core                                                  │    │
  │  │  src-tauri/src/main.rs                                     │    │
  │  │  ├── #[tauri::command] fn my_command() → exposed to JS     │    │
  │  │  ├── App state management (Arc<Mutex<T>>)                   │    │
  │  │  ├── File system, OS APIs                                   │    │
  │  │  └── tauri-plugin-* (fs, http, notification, shell, store) │    │
  │  └──────────────────────────┬──────────────────────────────────┘    │
  │                             │  invoke() / Tauri IPC                  │
  │  ┌──────────────────────────▼──────────────────────────────────┐    │
  │  │  OS WebView (no bundled Chromium)                           │    │
  │  │  macOS: WKWebView                                           │    │
  │  │  Windows: WebView2 (Edge/Chromium-based, ships with Win 11) │    │
  │  │  Linux: webkit2gtk                                          │    │
  │  │                                                             │    │
  │  │  Your web app: React / Vue / Svelte / Solid / vanilla       │    │
  │  └─────────────────────────────────────────────────────────────┘    │
  └──────────────────────────────────────────────────────────────────────┘

  Size comparison:
  Electron: 50-150 MB install (bundles Chromium)
  Tauri:     3-10 MB install  (uses OS webview)
```

**Tauri commands — the IPC pattern:**
```rust
// src-tauri/src/main.rs

use tauri::State;
use std::sync::Mutex;

struct AppState {
    counter: Mutex<i32>,
}

// #[tauri::command] exposes this function to the frontend
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! From Rust.", name)
}

#[tauri::command]
async fn read_large_file(path: String) -> Result<String, String> {
    tokio::fs::read_to_string(&path)
        .await
        .map_err(|e| e.to_string())
}

#[tauri::command]
fn increment(state: State<AppState>) -> i32 {
    let mut counter = state.counter.lock().unwrap();
    *counter += 1;
    *counter
}

fn main() {
    tauri::Builder::default()
        .manage(AppState { counter: Mutex::new(0) })
        .invoke_handler(tauri::generate_handler![greet, read_large_file, increment])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```typescript
// Frontend (React)
import { invoke } from '@tauri-apps/api/core';

// Call Rust command
const greeting = await invoke<string>('greet', { name: 'Alice' });
const count = await invoke<number>('increment');

// tauri-plugin-fs
import { readTextFile, writeTextFile } from '@tauri-apps/plugin-fs';
const content = await readTextFile('/path/to/file.txt');

// tauri-plugin-dialog
import { open, save } from '@tauri-apps/plugin-dialog';
const selected = await open({ multiple: false, directory: false });
```

**Tauri 2.0 — mobile support:**
Tauri 2.0 adds iOS and Android targets (still maturing). Same Rust backend, same webview frontend, now can deploy to mobile. This positions Tauri as a full cross-platform alternative for web teams comfortable with Rust.

**Tauri vs Electron decision:**

| Factor | Electron | Tauri |
|--------|----------|-------|
| Install size | 50-150 MB | 3-10 MB |
| Memory | 100-300 MB baseline | 30-100 MB |
| Runtime consistency | Bundled Chromium = identical | OS webview = differences between Win/Mac/Linux |
| Backend language | Node.js (JS/TS) | Rust |
| Security model | Explicit contextIsolation | Rust memory safety + stricter capability model |
| Maturity | Very high | Medium (2.0 released 2024) |
| Team requirement | Any web developer | Web dev + Rust knowledge (or learn it) |
| When to choose | Known quantity; fast to ship | New app; size matters; willing to learn Rust |

---

## Capacitor / Ionic

### Architecture

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Capacitor Application                                               │
  │                                                                      │
  │  Your Web App (React / Vue / Angular / Svelte / plain HTML)          │
  │  ┌──────────────────────────────────────────────────────────────┐    │
  │  │  Web assets (index.html, JS bundle, CSS)                    │   │
  │  └──────────────────────────────┬───────────────────────────────┘   │
  │                                 │                                    │
  │  ┌──────────────────────────────▼───────────────────────────────┐   │
  │  │  Capacitor Bridge (JS ↔ Native)                              │   │
  │  │  @capacitor/core  — plugin API surface                       │   │
  │  │  @capacitor/camera, @capacitor/filesystem, @capacitor/push   │   │
  │  └─────┬───────────────────────────────────────────────────┬───┘    │
  │        │                                                   │        │
  │  ┌─────▼────────────────┐                    ┌────────────▼──────┐ │
  │  │  iOS Native Shell    │                    │ Android Native    │ │
  │  │  WKWebView           │                    │ Shell             │ │
  │  │  CapacitorPlugin.m   │                    │ WebView           │ │
  │  │                      │                    │ CapacitorPlugin.kt│ │
  │  └──────────────────────┘                    └───────────────────┘ │
  └──────────────────────────────────────────────────────────────────────┘
```

**Capacitor usage pattern:**
```typescript
import { Camera, CameraResultType } from '@capacitor/camera';
import { Filesystem, Directory } from '@capacitor/filesystem';
import { PushNotifications } from '@capacitor/push-notifications';
import { Capacitor } from '@capacitor/core';

// Platform detection
if (Capacitor.isNativePlatform()) {
  // running in iOS / Android native shell
} else {
  // running in browser
}

// Camera — same API on iOS, Android, and web (uses getUserMedia on web)
const photo = await Camera.getPhoto({
  resultType: CameraResultType.DataUrl,
  quality: 90,
});

// File system
await Filesystem.writeFile({
  path: 'user-data.json',
  data: JSON.stringify(userData),
  directory: Directory.Documents,
});

// Push notifications
await PushNotifications.requestPermissions();
await PushNotifications.register();
PushNotifications.addListener('registration', (token) => {
  sendTokenToServer(token.value);
});
```

**Ionic UI components** (optional but common with Capacitor):
```tsx
// Ionic components adapt to platform look
import { IonContent, IonHeader, IonList, IonItem, IonLabel, IonPage, IonToolbar } from '@ionic/react';

function UserListPage() {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Users</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonList>
          {users.map(user => (
            <IonItem key={user.id} routerLink={`/user/${user.id}`}>
              <IonLabel>{user.name}</IonLabel>
            </IonItem>
          ))}
        </IonList>
      </IonContent>
    </IonPage>
  );
}
// IonList, IonItem, etc. render with iOS or Material styling depending on platform
```

**Capacitor Live Update (formerly Ionic Appflow):**
```
  Capacitor Live Update allows you to push JS/CSS/HTML changes to
  production apps WITHOUT going through App Store / Play Store review.

  This works because:
  - App Store rules allow updating JS bundles (interpreted code)
  - Only native code changes require store review

  Workflow:
  npm run build → npx cap sync → upload bundle → users get update on next app launch

  Restriction: Cannot change native code (Swift/Kotlin/plugins) via live update
```

**When Capacitor is the right call:**
- You have an existing web app (React/Angular/Vue) and need to ship to mobile
- Your team is 100% web; learning Swift/Kotlin/Dart has too high a cost
- Rapid prototype or MVP — get to market quickly, native later if needed
- The app is essentially a web experience (dashboards, content readers, forms)
- You need live update capability for fast iteration post-launch

**When NOT to use Capacitor:**
- Complex animations with 60fps requirement (WebView perf ceiling)
- Camera/AR/ML features that need deep native access
- Gaming
- Demanding on hardware acceleration

---

## Code Sharing Strategies

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  What you CAN share across platforms                               │
  │                                                                    │
  │  ┌────────────────────────────────────────────────────────────┐    │
  │  │  Business Logic (the most valuable)                        │   │
  │  │  - API clients (Retrofit/Axios/fetch wrappers)             │   │
  │  │  - Data models / DTOs                                      │   │
  │  │  - Validation rules                                        │   │
  │  │  - Calculation / domain logic                             │   │
  │  │  - State management (Redux store, ViewModel logic)        │   │
  │  └────────────────────────────────────────────────────────────┘   │
  │  ┌────────────────────────────────────────────────────────────┐   │
  │  │  Infrastructure                                            │   │
  │  │  - Authentication flow                                     │   │
  │  │  - Analytics events                                        │   │
  │  │  - Feature flags                                           │   │
  │  │  - Error tracking setup                                    │   │
  │  └────────────────────────────────────────────────────────────┘   │
  └────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────┐
  │  What you should NOT share (or share only thinly)                  │
  │                                                                    │
  │  - UI components (each platform has different idioms)              │
  │  - Navigation (Stack vs NavController vs NavHost differ)           │
  │  - Platform-specific APIs (camera, biometrics, push notifications)│
  │  - Styling (iOS HIG vs Material Design vs Win Fluent)              │
  └────────────────────────────────────────────────────────────────────┘
```

**Monorepo for JS/TS cross-platform sharing (Turborepo):**
```
  apps/
  ├── web/              ← Next.js or Vite web app
  ├── mobile/           ← React Native / Expo app
  └── desktop/          ← Electron or Tauri app

  packages/
  ├── api-client/       ← shared: typed API client (axios + zod schemas)
  ├── state/            ← shared: Zustand stores + hooks
  ├── validation/       ← shared: zod schemas (same schemas on web + mobile)
  ├── ui-web/           ← web-specific: shadcn/ui components
  └── ui-mobile/        ← mobile-specific: RN components
```

**Turborepo config for selective builds:**
```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["^build"]
    }
  }
}
```

```bash
# Build only affected packages
turbo build --filter=mobile...   # mobile + all its dependencies
turbo test --filter=[HEAD^1]     # only changed since last commit
```

**.NET multi-targeting for MAUI + shared logic:**
```xml
<!-- Shared.Core.csproj — pure .NET, no UI -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <!-- Targets all MAUI platforms + ASP.NET server + tests -->
    <TargetFrameworks>net8.0;net8.0-ios;net8.0-android;net8.0-windows10.0.19041.0</TargetFrameworks>
  </PropertyGroup>
</Project>

<!-- MyApp.csproj — MAUI UI layer -->
<Project Sdk="Microsoft.NET.Sdk.Maui">
  <ItemGroup>
    <ProjectReference Include="..\Shared.Core\Shared.Core.csproj" />
  </ItemGroup>
</Project>

<!-- MyApi.csproj — ASP.NET backend -->
<Project Sdk="Microsoft.NET.Sdk.Web">
  <ItemGroup>
    <ProjectReference Include="..\Shared.Core\Shared.Core.csproj" />
  </ItemGroup>
</Project>
```

**Kotlin Multiplatform (KMP) — honorable mention:**
```
  Not covered in depth above but relevant to .NET audience:

  KMP allows sharing Kotlin business logic between:
  - Android (Kotlin native)
  - iOS (compiles to native framework via Kotlin/Native)
  - JVM (backend)
  - Web (Kotlin/JS)

  UI: NOT shared — you write SwiftUI on iOS, Compose on Android
  Logic: shared via expect/actual mechanism

  expect fun getPlatform(): String  // declaration
  actual fun getPlatform() = "Android ${Build.VERSION.SDK_INT}"  // Android
  actual fun getPlatform() = UIDevice.currentDevice.systemName  // iOS

  Compose Multiplatform: JetBrains' effort to share Compose UI across platforms
  (stable for desktop, improving for iOS)
```

---

## Decision Cheat Sheet

| Scenario | Recommendation | Rationale |
|----------|----------------|-----------|
| **Existing .NET/C# team, need iOS + Android + Windows** | .NET MAUI | First-party Microsoft support; full .NET ecosystem; Blazor Hybrid for web component reuse; single language for the whole team |
| **Existing React/TypeScript web team, need iOS + Android** | React Native + Expo | Same React patterns; fastest ramp-up; EAS for build + OTA; largest mobile JS ecosystem |
| **Custom design system, pixel-perfect on all platforms** | Flutter | Owns the canvas; looks identical everywhere; Material 3 + Cupertino included |
| **Desktop developer tool (IDE-like, VS Code-like)** | Electron | Proven at VS Code scale; web tech; large ecosystem; acceptable size for dev tools |
| **New desktop app, size/memory matters, OK with Rust** | Tauri | 10x smaller than Electron; Rust backend security; Tauri 2.0 adds mobile |
| **Existing web app needs iOS/Android native packaging** | Capacitor | Wrap your existing web app; no rewrite; live updates; native API access |
| **Performance-critical native features (AR, Camera ML, Complex animation)** | Swift (iOS) + Kotlin (Android) native | No abstraction layer; day-one API access; platform idioms |
| **Enterprise internal app, heavy forms + data, fast delivery** | Capacitor / Ionic | Web devs productive; Ionic components adaptive; store packaging with live updates |
| **Shared backend + mobile logic, native UI** | Kotlin Multiplatform | Share Kotlin domain layer; native SwiftUI + Compose for UI; no UI compromise |
| **Google/Firebase ecosystem, need Android + iOS + web** | Flutter | Google-first integrations; large firebase_flutter ecosystem; Flutter Web maturing |
| **Microsoft shop: web + Azure + mobile from one team** | MAUI + Blazor Hybrid | Azure MAUI integrations (MSAL, App Center, Azure DevOps); Blazor for web; C# throughout |

---

## Common Confusion Points

**"Cross-platform" means different things for different tools:**
```
  React Native: cross-platform mobile (iOS + Android). Desktop is minimal.
  Flutter:      cross-platform all-targets (mobile + desktop + web). Still maturing outside mobile.
  MAUI:         cross-platform all-targets (mobile + desktop). Web via Blazor Hybrid.
  Electron:     cross-platform desktop only. Not mobile.
  Tauri:        cross-platform desktop + mobile (2.0). Maturing.
  Capacitor:    cross-platform mobile + web. Desktop via Electron (separate).
```

**Flutter does NOT use native widgets — this is intentional, not a bug:**
Flutter draws every pixel using its own engine. A Button on Flutter is not a UIButton or android.widget.Button. This means:
- Consistent look across platforms (feature for design teams)
- Not automatically OS-update-aware (a new iOS button animation won't appear automatically)
- Accessibility requires explicit attention — screen readers work via Flutter's semantic layer
- Platform purists dislike it; product teams often love the design consistency

**React Native bridge vs JSI — they are not the same:**
Old RN (bridge): JS → serialize to JSON → async queue → deserialize → native. Every UI update is async.
New RN (JSI): JS → C++ bindings → direct synchronous native calls. No serialization. Much faster.
Expo SDK 50+ uses New Architecture by default. Old bridge is legacy — stop reading articles about it.

**MAUI and Xamarin.Forms are NOT the same:**
Xamarin.Forms used Renderers (full class per control per platform). MAUI uses Handlers (lighter, interceptable, platform-customizable). They look similar in XAML but are architecturally different. Xamarin.Forms is deprecated. MAUI is the replacement.

**Electron contextIsolation must be true:**
Pre-Electron 12, `nodeIntegration: true` was common. This means the renderer (your React app, loaded from remote URLs in older apps) had full Node.js access — massive security hole. Modern Electron: `contextIsolation: true`, `nodeIntegration: false`, expose only specific APIs via contextBridge. Any tutorial using `nodeIntegration: true` is out of date.

**Capacitor is not Cordova, but it replaces it:**
Cordova (Apache) was the original webview-based mobile platform. Capacitor (Ionic team) is its modern successor with: TypeScript-first, async/await plugin API, better native build tool integration, and Capacitor 3+ supporting the modern Gradle/Xcode project structures. If you see Cordova in a codebase, plan to migrate to Capacitor.

**Tauri's OS webview inconsistency is the real trade-off:**
Electron bundles Chromium — your app runs identically on Windows, macOS, Linux.
Tauri uses WKWebView (macOS), WebView2 (Windows), webkit2gtk (Linux) — all different engines, different CSS support levels, different JavaScript behavior edge cases. You must test on all three. For most apps this is fine; for apps with complex CSS (advanced grid, specific filter effects, obscure JS APIs), it can be painful.

**"Code sharing %" figures are aspirational, not guaranteed:**
Saying "Flutter shares 95% of code" means the Flutter widget code is shared. The native plugin code (platform channels), build configurations, CI pipeline, and platform-specific test setup are not shared. The 5-20% that IS platform-specific tends to be the hardest, most time-consuming code to write (biometrics, camera, push notifications, deep links, widgets/home screen extensions). Factor this into estimates.
