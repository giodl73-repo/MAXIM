# macOS Developer Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          macOS SYSTEM LAYERS                                │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  Applications (SwiftUI / AppKit / Electron / CLI tools)              │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  High-Level Frameworks                                               │  │
│  │  SwiftUI · AppKit · CoreData · CloudKit · StoreKit · WatchKit        │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Mid-Level Frameworks                                                │  │
│  │  Foundation (ObjC/Swift) · CoreFoundation (C) · CoreGraphics         │  │
│  │  CoreText · CoreImage · AVFoundation · CoreLocation · Security       │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  libSystem  (libc + libpthread + libm + libdispatch + libobjc)       │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Darwin Userland  (launchd · dyld · shell · BSD tools)              │   │
│  └────────────────────────────┬────────────────────────────────────────┘   │
│                               │                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  XNU Kernel                                                         │   │
│  │  ┌──────────────┐  ┌──────────────────┐  ┌────────────────────┐   │   │
│  │  │  Mach Layer  │  │   BSD Layer       │  │  IOKit (Drivers)   │   │   │
│  │  │  tasks       │  │  POSIX syscalls   │  │  C++ OOP in kernel │   │   │
│  │  │  threads     │  │  VFS              │  │  IOService tree    │   │   │
│  │  │  ports       │  │  networking       │  │  IORegistry        │   │   │
│  │  │  messages    │  │  process model    │  │  kext / DriverKit  │   │   │
│  │  └──────────────┘  └──────────────────┘  └────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                               │                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Hardware  (Apple Silicon SoC / Intel)                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. XNU Architecture

XNU = "X is Not Unix". Hybrid kernel combining Mach microkernel, BSD layer, and IOKit.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            XNU KERNEL                                       │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  MACH LAYER  (Carnegie Mellon Mach 3.0 heritage)                     │  │
│  │                                                                      │  │
│  │  Task          — heavyweight resource container (address space, ports)│  │
│  │  Thread        — execution unit within a task                        │  │
│  │  Port          — protected message queue; THE IPC primitive          │  │
│  │  Message       — typed data transferred between ports                │  │
│  │  Right         — send right / receive right / send-once right        │  │
│  │                                                                      │  │
│  │  Everything is a Mach port under the hood:                           │  │
│  │    process ──► task port (privileged handle to a task)               │  │
│  │    XPC service ──► built on Mach ports + launchd name server         │  │
│  │    IOKit user-client ──► Mach port                                   │  │
│  │    NSMachPort / CFMachPort ──► raw Mach port wrappers                │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  BSD LAYER  (FreeBSD heritage)                                       │  │
│  │                                                                      │  │
│  │  POSIX syscall interface (read/write/open/fork/exec/wait/signal)     │  │
│  │  VFS (Virtual File System) — abstraction over APFS, HFS+, FAT, etc.  │  │
│  │  BSD networking stack (TCP/IP, sockets, TUN/TAP)                     │  │
│  │  Process model: fork() + exec() — standard POSIX heritage            │  │
│  │  Signals: SIGKILL, SIGTERM, SIGHUP — all work as expected            │  │
│  │  Security: mandatory access control (MAC framework), sandbox         │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  IOKIT  (C++ OOP driver framework)                                   │  │
│  │                                                                      │  │
│  │  C++ in kernel — unusual; uses a restricted subset (no exceptions,   │  │
│  │  no RTTI, no STL); IOObject reference counting                       │  │
│  │  IOService: base class for all drivers                               │  │
│  │  IORegistry: device tree (like Windows Device Manager)               │  │
│  │  DriverKit (macOS 10.15+): drivers in user space — much safer        │  │
│  │  kext (kernel extension): legacy; Apple discouraging; SIP restricts  │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Mach Port as Universal IPC Primitive

```
Producer                Bootstrap Server               Consumer
(server app)            (launchd name server)          (client app)
    │                         │                              │
    │  mach_port_allocate()   │                              │
    │  create receive right   │                              │
    │─────────────────────────►                              │
    │  bootstrap_register()   │                              │
    │  "com.myapp.service"    │                              │
    │                         │                              │
    │                         │◄── bootstrap_look_up() ─────│
    │                         │    "com.myapp.service"       │
    │                         │──── send right ────────────►│
    │◄─────────── mach_msg() ─────────────────────────────── │
    │    message received                                     │
    │────────────────────────────── reply ──────────────────►│
```

Darwin = XNU + BSD userland (shell, coreutils, etc.) — this portion is open source at
`github.com/apple/darwin-xnu`. The AppKit/UIKit/Swift layers are closed source.

---

## 2. macOS SDK Onion

```
┌──────────────────────────────────────────────────────────────────────┐
│  App  (your code: Swift / ObjC / Rust / Go / C++)                    │
├──────────────────────────────────────────────────────────────────────┤
│  AppKit / SwiftUI                                                     │
│  NSWindow, NSView, NSApplication    (ObjC + Swift overlay)           │
├──────────────────────────────────────────────────────────────────────┤
│  Foundation  (ObjC/Swift)                                            │
│  NSString, NSArray, NSFileManager, NSURLSession                      │
│  URLSession, Data, FileManager, Date — Swift value-type wrappers     │
├──────────────────────────────────────────────────────────────────────┤
│  CoreFoundation  (C API — CFString, CFArray, CFRunLoop)              │
│  "toll-free bridged" to Foundation ObjC classes                      │
├──────────────────────────────────────────────────────────────────────┤
│  libSystem  (the stable ABI boundary)                                │
│  libc · libpthread · libm · libdispatch (GCD) · libobjc              │
├──────────────────────────────────────────────────────────────────────┤
│  Darwin / XNU                                                        │
├──────────────────────────────────────────────────────────────────────┤
│  Hardware                                                            │
└──────────────────────────────────────────────────────────────────────┘

CF ──► toll-free bridge ──► NS objects
CFStringRef  ←──────────────►  NSString *
CFArrayRef   ←──────────────►  NSArray *
CFRunLoopRef ←──────────────►  NSRunLoop *
Cast with __bridge, __bridge_transfer, __bridge_retained (ARC era)
In Swift: as CFString, as! NSString — same bridge, type-safe
```

### Framework Bundle Layout

Every macOS framework is a directory bundle (not a .dll or .lib):

```
Cocoa.framework/
├── Cocoa                      ← the actual Mach-O dylib (symlink)
├── Headers/                   ← public headers (for C/ObjC)
├── Modules/
│   └── module.modulemap       ← Swift module interface
├── Resources/
│   ├── Info.plist
│   └── ...
└── Versions/
    └── A/
        ├── Cocoa              ← actual binary
        └── Headers/
```

### dyld Shared Cache

All Apple system frameworks are pre-linked into a single large file:
`/System/Library/dyld/dyld_shared_cache_arm64e`

Benefits: mmap'd once, shared across all processes; faster launch.
Consequence: you cannot find system dylibs on disk by path at runtime — they
exist only in the cache. `dyld_shared_cache_extract` can dump them for inspection.

### dyld Path Variables

```
@executable_path   →  directory of the main executable
@loader_path       →  directory of the binary containing this reference
@rpath             →  search list; set via LC_RPATH in Mach-O load commands

Typical framework embed:
  Install name:  @rpath/MyFramework.framework/Versions/A/MyFramework
  App RPATH:     @executable_path/../Frameworks

Inspect with:
  otool -L MyApp           # show linked dylibs
  otool -l MyApp | grep -A2 LC_RPATH
  install_name_tool -add_rpath @executable_path/../Frameworks MyApp
```

Windows/.NET bridge:
- .framework bundle ↔ .dll + manifest + resources directory
- dyld shared cache ↔ GAC (Global Assembly Cache) — both pre-register system libs
- @rpath ↔ probing directories in AssemblyResolve
- otool -L ↔ Dependency Walker / fuslogvw

---

## 3. The App Bundle

```
MyApp.app/                          ← looks like a directory; OS treats as atom
└── Contents/
    ├── MacOS/
    │   └── MyApp                   ← Mach-O executable (the entry point)
    ├── Frameworks/                 ← embedded dylibs and .framework bundles
    │   └── MyFramework.framework/
    ├── Resources/                  ← localized strings, images, .nib/.xib files
    │   ├── en.lproj/
    │   │   └── Localizable.strings
    │   └── Assets.car              ← compiled asset catalog
    ├── PlugIns/                    ← app extensions, XPC services
    │   └── MyExtension.appex/
    ├── Info.plist                  ← the manifest (bridge: .NET AssemblyInfo)
    └── _CodeSignature/
        └── CodeResources           ← signed file list + hashes (seal)
```

### Info.plist Key Reference

| Key | Type | Example | Purpose |
|-----|------|---------|---------|
| `CFBundleIdentifier` | String | `com.mycompany.myapp` | Unique app ID (reverse DNS) |
| `CFBundleExecutable` | String | `MyApp` | Name of executable in MacOS/ |
| `CFBundleShortVersionString` | String | `2.3.1` | Marketing version (user-visible) |
| `CFBundleVersion` | String | `451` | Build number (monotonically increasing) |
| `LSMinimumSystemVersion` | String | `13.0` | Minimum macOS requirement |
| `NSPrincipalClass` | String | `NSApplication` | The app delegate host class |
| `CFBundleURLTypes` | Array | `[{URLSchemes:[myapp]}]` | Custom URL scheme registration |
| `CFBundleDocumentTypes` | Array | see UTI section | File type associations |
| `NSHumanReadableCopyright` | String | `© 2026 MyCo` | About box text |
| `LSUIElement` | Boolean | `YES` | Agent app (no Dock icon) |

### UTI (Uniform Type Identifier)

Type system for file/data types — everything in drag-and-drop, Share Sheet, QuickLook uses UTIs.

```
public.data (root)
├── public.text
│   ├── public.plain-text
│   │   └── public.utf8-plain-text
│   └── public.source-code
│       ├── public.swift-source
│       └── public.c-source
├── public.image
│   ├── public.png
│   └── public.jpeg
└── public.archive
    └── com.pkware.zip-archive
        └── com.apple.bundle          ← .app/.framework are ZIP-based UTIs
```

Declare file type association in Info.plist `CFBundleDocumentTypes`:
```xml
<dict>
    <key>CFBundleTypeName</key>      <string>My Document</string>
    <key>LSItemContentTypes</key>    <array><string>com.myco.mydoc</string></array>
    <key>CFBundleTypeRole</key>      <string>Editor</string>
</dict>
```

Declare a custom UTI in `UTExportedTypeDeclarations`:
```xml
<dict>
    <key>UTTypeIdentifier</key>      <string>com.myco.mydoc</string>
    <key>UTTypeConformsTo</key>      <array><string>public.data</string></array>
    <key>UTTypeTagSpecification</key>
    <dict><key>public.filename-extension</key><array><string>mydoc</string></array></dict>
</dict>
```

---

## 4. launchd — macOS Init and Service Management

launchd is PID 1. It replaces: init, cron, inetd, xinetd, rc scripts.
Everything that needs to run as a service, on a schedule, or on-demand goes through launchd.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          launchd DOMAIN MODEL                               │
│                                                                             │
│  System Domain (PID 1 owns)                                                 │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  /System/Library/LaunchDaemons/   ← Apple's own daemons (SIP-sealed)│  │
│  │  /Library/LaunchDaemons/          ← third-party system daemons      │  │
│  │  Run as specified UserName (often root)                              │  │
│  │  Start before any user logs in                                       │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  User Domain (one per logged-in user)                                      │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  /System/Library/LaunchAgents/    ← Apple's own agents               │  │
│  │  /Library/LaunchAgents/           ← third-party, all users           │  │
│  │  ~/Library/LaunchAgents/          ← per-user agents                  │  │
│  │  Run as the logged-in user                                           │  │
│  │  Have access to user session, GUI, Keychain                          │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘

Windows bridge:
  LaunchDaemon  ↔  Windows Service (runs as SYSTEM or specific account)
  LaunchAgent   ↔  Scheduled Task with "run only when user is logged on"
  launchctl     ↔  sc.exe + schtasks.exe combined
```

### Plist Format (LaunchDaemon Example)

`/Library/LaunchDaemons/com.mycompany.myservice.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.mycompany.myservice</string>          <!-- must match filename -->

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/myservice</string>
        <string>--port</string>
        <string>8080</string>
    </array>

    <key>RunAtLoad</key>        <true/>               <!-- start immediately on load -->
    <key>KeepAlive</key>        <true/>               <!-- restart on crash -->

    <!-- OR conditional keep-alive: -->
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>  <false/>           <!-- restart unless clean exit -->
    </dict>

    <key>StartCalendarInterval</key>                  <!-- cron replacement -->
    <dict>
        <key>Hour</key>    <integer>3</integer>
        <key>Minute</key>  <integer>30</integer>
    </dict>

    <key>EnvironmentVariables</key>
    <dict>
        <key>MY_ENV_VAR</key>  <string>value</string>
    </dict>

    <key>UserName</key>         <string>_myservice</string>
    <key>StandardOutPath</key>  <string>/var/log/myservice.log</string>
    <key>StandardErrorPath</key><string>/var/log/myservice-error.log</string>

    <key>ThrottleInterval</key> <integer>10</integer> <!-- min seconds between restarts -->
</dict>
</plist>
```

### launchctl Commands

```bash
# Load/enable a service
sudo launchctl load /Library/LaunchDaemons/com.mycompany.myservice.plist
sudo launchctl enable system/com.mycompany.myservice    # persist across reboots

# Unload/disable
sudo launchctl unload /Library/LaunchDaemons/com.mycompany.myservice.plist
sudo launchctl disable system/com.mycompany.myservice

# Start/stop a loaded service
sudo launchctl start com.mycompany.myservice
sudo launchctl stop  com.mycompany.myservice

# Modern bootstrap subcommands (macOS 10.11+)
sudo launchctl bootstrap system /Library/LaunchDaemons/com.mycompany.myservice.plist
sudo launchctl bootout  system/com.mycompany.myservice

# Inspect
launchctl list                                           # all services in current domain
launchctl list | grep mycompany
launchctl print system/com.mycompany.myservice           # full status + PID + exit code
launchctl print-disabled system                          # see what's disabled

# Force start (even if conditions not met)
sudo launchctl kickstart -k system/com.mycompany.myservice
# -k = kill existing instance first

# User domain (no sudo needed)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.me.agent.plist
launchctl print gui/$(id -u)/com.me.agent
```

### XPC Services

Lightweight launchd agents bundled inside an app, used for privilege separation and crash isolation.

```
MyApp.app/
└── Contents/
    └── PlugIns/
        └── com.mycompany.myapp.helper.xpc/
            └── Contents/
                ├── MacOS/
                │   └── com.mycompany.myapp.helper
                └── Info.plist

App side:
  let connection = NSXPCConnection(serviceName: "com.mycompany.myapp.helper")
  connection.remoteObjectInterface = NSXPCInterface(with: MyProtocol.self)
  connection.resume()
  let proxy = connection.remoteObjectProxy as! MyProtocol
  proxy.doWork { result in ... }

XPC service side:
  class MyServiceDelegate: NSObject, NSXPCListenerDelegate, MyProtocol {
      func listener(_ listener: NSXPCListener,
                    shouldAcceptNewConnection conn: NSXPCConnection) -> Bool {
          conn.exportedInterface = NSXPCInterface(with: MyProtocol.self)
          conn.exportedObject = self
          conn.resume()
          return true
      }
  }
```

XPC vs NSXPCConnection vs low-level xpc_connection_t:
- `xpc_connection_t` — C API, lowest level
- `NSXPCConnection` — ObjC wrapper, type-safe proxy via protocols
- Both built on Mach ports via launchd brokering

---

## 5. Signing, Notarization, and Gatekeeper

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNING + DISTRIBUTION PIPELINE                          │
│                                                                             │
│  Developer Machine                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  1. Generate CSR (Keychain Access or: certtool / security)          │   │
│  │  2. Submit CSR to developer.apple.com → Apple issues certificate    │   │
│  │  3. Certificate lives in login Keychain with private key            │   │
│  │  4. codesign signs app with that cert + entitlements                │   │
│  └─────────────────────┬───────────────────────────────────────────────┘   │
│                         │                                                   │
│  ┌─────────────────────▼───────────────────────────────────────────────┐   │
│  │  5. xcrun notarytool submit --wait MyApp.zip                        │   │
│  │     Apple scans for malware; returns ticket                         │   │
│  │  6. xcrun stapler staple MyApp.app                                  │   │
│  │     Ticket embedded; works offline                                  │   │
│  └─────────────────────┬───────────────────────────────────────────────┘   │
│                         │                                                   │
│  End User Machine        │                                                  │
│  ┌─────────────────────▼───────────────────────────────────────────────┐   │
│  │  7. Gatekeeper (syspolicyd) assesses app on first launch            │   │
│  │     Checks: signature valid? notarized? quarantine xattr?           │   │
│  │  8. App runs or user sees "cannot be opened" dialog                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘

Windows bridge:
  codesign + notarize  ↔  Authenticode signing + SmartScreen
  Apple Root CA chain  ↔  Microsoft Root CA / EV cert chain
  Gatekeeper           ↔  SmartScreen / Mark-of-the-Web
  Entitlements plist   ↔  Requested Execution Level in app manifest (.exe.manifest)
```

### Certificate Types

| Certificate Type | Where Used | Distribution Channel |
|-----------------|------------|---------------------|
| Apple Development | Debug builds on own devices | Local only |
| Apple Distribution | Production builds | App Store |
| Developer ID Application | Direct download (outside App Store) | Web, your own server |
| Developer ID Installer | Signing .pkg installers | Web distribution |
| Mac Installer Distribution | Mac App Store .pkg | App Store |

### Entitlements

Entitlements gate OS capabilities. Embedded by codesign at signing time.

```xml
<!-- MyApp.entitlements -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- Hardened Runtime -->
    <key>com.apple.security.cs.allow-jit</key>           <true/>
    <key>com.apple.security.cs.disable-library-validation</key> <true/>

    <!-- App Sandbox (required for Mac App Store) -->
    <key>com.apple.security.app-sandbox</key>            <true/>
    <key>com.apple.security.network.client</key>         <true/>
    <key>com.apple.security.network.server</key>         <true/>
    <key>com.apple.security.files.user-selected.read-write</key> <true/>

    <!-- Keychain sharing -->
    <key>keychain-access-groups</key>
    <array><string>$(AppIdentifierPrefix)com.myco.myapp</string></array>

    <!-- iCloud -->
    <key>com.apple.developer.icloud-container-identifiers</key>
    <array><string>iCloud.com.myco.myapp</string></array>
</dict>
</plist>
```

### codesign Commands

```bash
# Sign an app (Developer ID, with hardened runtime, with entitlements)
codesign --sign "Developer ID Application: My Name (TEAMID)" \
          --entitlements MyApp.entitlements \
          --options runtime \
          --deep \
          --force \
          MyApp.app

# --deep: recursively sign nested bundles/frameworks (use with caution; prefer manual order)
# --options runtime: enable Hardened Runtime (required for notarization)
# --force: re-sign even if already signed

# Verify signature
codesign --verify --verbose MyApp.app
codesign -dv --verbose=4 MyApp.app                      # full dump
codesign --display --entitlements :- MyApp.app           # show embedded entitlements

# Check with Gatekeeper
spctl --assess --verbose MyApp.app
spctl --assess --type install MyPackage.pkg
```

### Notarization (xcrun notarytool)

```bash
# Store credentials (one-time)
xcrun notarytool store-credentials "myprofile" \
    --apple-id myemail@example.com \
    --team-id MYTEAMID \
    --password "@keychain:AC_PASSWORD"   # app-specific password from appleid.apple.com

# Notarize (zip first for apps; dmg/pkg can be submitted directly)
ditto -c -k --keepParent MyApp.app MyApp.zip
xcrun notarytool submit MyApp.zip \
    --keychain-profile "myprofile" \
    --wait

# Check submission history
xcrun notarytool history --keychain-profile "myprofile"
xcrun notarytool info SUBMISSION-UUID --keychain-profile "myprofile"

# Staple notarization ticket onto app/dmg/pkg
xcrun stapler staple MyApp.app

# Validate stapling
xcrun stapler validate MyApp.app
```

### Hardened Runtime Exceptions (when you need them)

| Entitlement | When Needed |
|-------------|-------------|
| `cs.allow-jit` | JavaScript engines (V8, JavaScriptCore with JIT on) |
| `cs.allow-unsigned-executable-memory` | Code that generates and runs native code |
| `cs.disable-library-validation` | Plugins/dylibs not signed by same team |
| `cs.allow-dyld-environment-variables` | `DYLD_*` env vars (e.g., DYLD_LIBRARY_PATH) |

### App Sandbox Boundaries

```
Without sandbox:             With sandbox:
  full filesystem R/W   →      ~/Library/Containers/com.bundle.id/ only
  all network          →      must declare .network.client / .network.server
  all devices          →      must declare camera / mic / bluetooth etc.
  all keychain         →      own keychain group only

Powerbox (NSOpenPanel / NSSavePanel): user explicitly grants access to files
           outside the container — OS remembers these "security-scoped bookmarks"
```

---

## 6. APFS and macOS Filesystem

### Filesystem Feature Cross-OS Bridge

```
FILESYSTEM METADATA FEATURES — CROSS-PLATFORM COMPARISON
═══════════════════════════════════════════════════════════════════════════════

  Feature              NTFS (Windows)           ext4/xfs (Linux)         APFS (macOS)
  ─────────────        ───────────────────       ─────────────────        ──────────────────
  Extended attrs       Alternate Data Streams    xattrs                   xattrs + resource forks
                       file.txt:ADS_NAME         getxattr/setxattr        getxattr/setxattr
                       (same inode, hidden        attr -s name -V val      xattr -l, xattr -w
                        stream)                   max: varies by FS        (quarantine is a key xattr)

  Sparse files         Yes — NTFS native          Yes — file has holes     Yes — APFS native
                       File appears large but      seek past end, write     Treated as holes in
                       physical blocks only        → hole = no blocks       block allocation
                       allocated where written    allocated for zeros      fallocate(FALLOC_FL_PUNCH_HOLE)
                       DeviceIoControl             (ext4: FALLOC punch)    ftruncate to sparse

  Case sensitivity     Insensitive, preserving    Case-sensitive           Case-insensitive by default
                       FOO.TXT == foo.txt          FOO.TXT ≠ foo.txt       Per-Container setting
                       Registry: always            (ext4; configurable      Case-sensitive APFS:
                       insensitive                 per-dir in ext4 5.2+)   required for some dev tools

  Resource forks       No equivalent              No equivalent            Yes — legacy HFS+ feature
                       (ADS is closest)           (xattrs hold some        macOS keeps resource forks
                                                   metadata)                for some file types
                                                                           file/rsrc (path syntax)
                                                                           Can confuse Linux tools via SMB

  Clone semantics      ReFS has clones             No standard clone        cp on APFS = instant COW clone
  (instant copy)       (NTFS: no)                 btrfs has reflinks       zero extra space until write
                       NTFS: full copy on cp        (cp --reflink=auto)     cross-tool: tar/rsync don't
                                                                            preserve clone relationships

  Cross-platform gotchas:
    1. Case sensitivity: code working on macOS (CI runs on macOS) may break on Linux CI
       import './Utils' succeeds on case-insensitive APFS, fails on ext4
    2. Resource forks: tar from macOS creates ._filename dot-underscore files on Linux
       Use GNU tar (gtar on macOS) or tar --disable-copyfile
    3. xattr quarantine: files downloaded on macOS get com.apple.quarantine xattr
       Tools that copy files via rsync/scp lose this xattr (expected)
       xattr -dr com.apple.quarantine /path/to/app  → clears for distribution
    4. ADS on Windows: NTFS streams survive copy within NTFS but are stripped by
       most network file copies; cross-platform file transfer tools ignore ADS
```

### APFS Architecture

```
Physical Disk
└── APFS Container  (partition; handles space sharing)
    ├── Macintosh HD Volume Group
    │   ├── Macintosh HD      (root / — System, sealed snapshot)
    │   └── Macintosh HD - Data  (user data, writable)
    ├── Preboot Volume       (boot files)
    ├── Recovery Volume      (macOS recovery)
    └── VM Volume            (swap)

Key features:
  Copy-on-Write (COW): modifying a file never overwrites in place
  Clones:             cp on APFS is instant + zero additional space until modified
  Snapshots:          point-in-time read-only views (Time Machine uses these)
  Space sharing:      all volumes in container share pool, no fixed partition sizes
  Native encryption:  per-file keys; FileVault is just APFS volume-level encryption
  Atomic safe-save:   rename() is atomic on APFS
```

### Key Directory Locations

```
/                        ← root (SIP-sealed cryptographic snapshot)
├── System/              ← Apple OS files; SIP-protected; read-only
│   └── Library/
│       ├── Frameworks/  ← system frameworks
│       ├── LaunchDaemons/
│       └── CoreServices/
├── usr/                 ← POSIX standard bins/libs; SIP-protected
│   ├── bin/
│   └── lib/
├── Library/             ← system-wide app support; writable by admin
│   ├── LaunchDaemons/
│   ├── LaunchAgents/
│   └── Application Support/
├── Applications/        ← user-installed apps
├── Users/
│   └── username/
│       ├── Library/     ← per-user app support (hidden in Finder)
│       │   ├── Application Support/
│       │   ├── Preferences/    ← .plist files (bridge: HKCU registry)
│       │   ├── Caches/
│       │   ├── LaunchAgents/
│       │   └── Containers/     ← sandboxed app containers
│       └── Documents/
├── opt/
│   └── homebrew/        ← Homebrew root (Apple Silicon)
│       ├── bin/
│       ├── lib/
│       └── Cellar/
├── private/
│   ├── var/             ← variable data (logs, databases)
│   │   ├── folders/     ← temp dirs per user session
│   │   └── log/
│   └── tmp/             ← temporary files
└── Volumes/             ← mount points for other disks

Note: /etc, /tmp, /var are symlinks to /private/etc, /private/tmp, /private/var
```

### SIP (System Integrity Protection)

```bash
# Check SIP status
csrutil status
# System Integrity Protection status: enabled.

# SIP protects:
#   /System, /usr, /bin, /sbin
#   System-installed apps in /Applications
#   Boot args / NVram vars
#   kext loading (only Apple-signed kexts)

# SIP CANNOT be disabled by root — requires reboot into Recovery Mode
# csrutil disable  (run in Terminal in Recovery Mode, not production)
```

### Quarantine Extended Attribute

```bash
# Downloaded files get tagged automatically by the OS
xattr -l ~/Downloads/SomeApp.dmg
# com.apple.quarantine: 0083;63abc123;Safari;XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

# Remove quarantine (what "Open Anyway" does in System Preferences)
xattr -d com.apple.quarantine ~/Downloads/SomeApp.app

# List all xattrs on a file
xattr -l /path/to/file

# Remove ALL xattrs
xattr -c /path/to/file
```

### Useful Filesystem Commands

```bash
# APFS snapshots
tmutil listlocalsnapshots /
tmutil localsnapshots /

# diskutil
diskutil list
diskutil apfs list
diskutil info /

# Disk Images
hdiutil attach MyDMG.dmg
hdiutil create -size 100m -fs APFS -volname "MyDisk" MyDisk.dmg
hdiutil detach /Volumes/MyDisk

# Find file by UTI
mdls -name kMDItemContentType somefile.pdf
# kMDItemContentType = "com.adobe.pdf"

# Spotlight index search (metadata)
mdfind -name "report" -onlyin ~/Documents
mdfind "kMDItemContentType == 'com.adobe.pdf'"
```

---

## 7. macOS Development Tools

### Xcode and CLT

```bash
# Install Command Line Tools (sufficient for most non-GUI dev)
xcode-select --install

# Check active Xcode / CLT
xcode-select -p
# /Applications/Xcode.app/Contents/Developer

# Switch between multiple Xcode installations
sudo xcode-select -s /Applications/Xcode-15.app/Contents/Developer
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer

# Accept Xcode license (required for first use / after update)
sudo xcodebuild -license accept

# Show SDK paths
xcrun --show-sdk-path
xcrun --sdk macosx --show-sdk-path
xcrun --sdk iphoneos --show-sdk-path

# Run any Xcode tool without full path
xcrun swift --version
xcrun clang --version
xcrun simctl list devices
xcrun notarytool history --keychain-profile myprofile
```

### xcrun Tool Reference

| Command | What it Does |
|---------|-------------|
| `xcrun swift` | Swift compiler + REPL |
| `xcrun swiftc` | Swift compiler directly |
| `xcrun clang` | C/C++/ObjC compiler |
| `xcrun lldb` | LLDB debugger |
| `xcrun simctl` | Simulator control |
| `xcrun notarytool` | Notarization |
| `xcrun stapler` | Staple notarization tickets |
| `xcrun actool` | Asset catalog compiler |
| `xcrun ibtool` | Interface Builder tool |
| `xcrun dsymutil` | dSYM symbol bundle generator |
| `xcrun xctrace` | Instruments from CLI |
| `xcrun xcodebuild` | Build Xcode projects from CLI |

### Instruments / xctrace

```bash
# List available templates
xcrun xctrace list templates

# Record a Time Profiler trace (10 seconds)
xcrun xctrace record \
    --template "Time Profiler" \
    --duration 10 \
    --launch -- /path/to/MyApp

# Record for a running process (PID)
xcrun xctrace record \
    --template "Allocations" \
    --attach $(pgrep MyApp)

# Output file is .trace; open with Instruments.app
open recording.trace

# Key templates:
#   Time Profiler    — CPU sampling, call stacks (bridge: VS Profiler sampling)
#   Allocations      — heap allocation timeline, retain cycles
#   Leaks            — memory leak detection
#   Network          — all URLSession requests + response times
#   System Trace     — scheduler, VM faults, syscalls (bridge: PerfView / ETW)
#   Energy Log       — battery drain attribution
```

### LLDB

macOS does not use GDB. LLDB is the debugger.

```bash
# Attach to a running process
lldb -p $(pgrep MyApp)

# Launch under lldb
lldb -- /path/to/MyApp arg1 arg2

# Common LLDB commands
(lldb) process attach --name MyApp
(lldb) breakpoint set --name viewDidLoad
(lldb) breakpoint set --file MyViewController.swift --line 42
(lldb) run
(lldb) continue    # or: c
(lldb) next        # or: n   (step over)
(lldb) step        # or: s   (step into)
(lldb) finish      # or: f   (step out)
(lldb) frame variable          # locals in current frame
(lldb) po myObject             # print description (calls debugDescription)
(lldb) expr myVar = 99         # modify variable
(lldb) bt                      # backtrace
(lldb) thread list
(lldb) thread select 3
(lldb) memory read 0x00007fff5fbff800

# Conditional breakpoints
(lldb) breakpoint set --name doWork --condition 'count > 10'
(lldb) breakpoint command add 1   # add commands to run at breakpoint

# watchpoint (data breakpoint — bridge: VS "watch" window)
(lldb) watchpoint set variable self->_count
```

### Homebrew

```bash
# Install (one-liner from brew.sh)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Paths
# Apple Silicon: /opt/homebrew/   (in PATH via /opt/homebrew/bin)
# Intel:         /usr/local/

# Basic usage
brew install ripgrep
brew install node
brew install postgresql@16
brew uninstall ripgrep
brew upgrade               # upgrade all outdated
brew update                # update Homebrew itself + formula index
brew doctor                # diagnose issues
brew list                  # installed packages
brew info postgresql@16    # details, caveats, service info

# Homebrew Services (wraps launchctl)
brew services start postgresql@16
brew services stop  postgresql@16
brew services list

# Casks (GUI apps)
brew install --cask visual-studio-code
brew install --cask iterm2
brew install --cask docker

# Taps (third-party formula repos)
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

---

## 7b. GCD, Swift Concurrency, and Async Model Bridges

### GCD → Swift Concurrency — The Layering

```
CONCURRENCY LAYER ARCHITECTURE (macOS / iOS)
═════════════════════════════════════════════════════════════════════

  Swift async/await + Actors (Swift 5.5+, macOS 12+)
  ┌──────────────────────────────────────────────────────────────┐
  │  Task { ... }                  async-let x = fetch()         │
  │  await someActor.method()      for await item in stream      │
  │  @MainActor func updateUI()    Actor: isolated state         │
  └──────────────────────┬───────────────────────────────────────┘
                         │  Swift runtime schedules on:
                         ▼
  GCD (Grand Central Dispatch) — the cooperative thread pool
  ┌──────────────────────────────────────────────────────────────┐
  │  DispatchQueue.main (serial, main thread)                    │
  │  DispatchQueue.global(qos: .userInitiated) (concurrent)      │
  │  DispatchQueue.global(qos: .background) (concurrent)         │
  │  DispatchQueue(label: "com.app.serial", .serial)             │
  └──────────────────────┬───────────────────────────────────────┘
                         │  GCD manages:
                         ▼
  Kernel thread pool (pthreads, POSIX)
```

```
ASYNC MODEL BRIDGE: .NET → Swift
════════════════════════════════════════════════════════════════════

  .NET concept                     Swift equivalent
  ──────────────────────────────   ─────────────────────────────────────────
  Task<T>                          Task<T>  (Swift.Task — same name, different type)
  ValueTask<T>                     (no direct equiv; Swift Task is always heap)
  Task.Run { }                     Task.detached { ... }  (unstructured)
  async/await                      async/await  (same syntax, different runtime)
  ConfigureAwait(false)            (no equivalent; Swift actors handle context)
  CancellationToken                Task.cancel() + withTaskCancellationHandler
  IAsyncEnumerable<T>              AsyncSequence protocol
  Parallel.ForEach                 withTaskGroup(of:) { group in group.addTask {} }
  ThreadPool.QueueUserWorkItem      Task.detached { } or GCD DispatchQueue.async
  SynchronizationContext           @MainActor annotation + actor isolation
  INotifyPropertyChanged           @Observable macro (Swift 5.9+) or @Published
  Task.WhenAll                     await withTaskGroup + collect results

  Key conceptual differences:
  ├─ Swift actors prevent data races at compile time — @MainActor is a type annotation
  │  .NET: SynchronizationContext is a runtime mechanism; actors are a library pattern
  ├─ Swift structured concurrency: Task tree — cancellation propagates to children
  │  .NET TPL: CancellationTokenSource/Token is explicitly threaded through calls
  ├─ Swift async context: continuation automatically resumes on same executor
  │  .NET: ConfigureAwait(false) is needed to escape SynchronizationContext
  └─ Swift Task.detached: explicitly unstructured — must manage lifetime manually
     .NET Task.Run: similar — detached from current context
```

### POSIX Signals — macOS Caveats and kqueue Bridge

```
SIGNAL HANDLING: LINUX vs MACOS vs WINDOWS
════════════════════════════════════════════════════════════════════

  Concept           Linux                     macOS                     Windows
  ──────────        ──────────────────         ─────────────────────     ──────────────────
  Signal delivery   Any thread can receive     Main thread constraint:    No signals
  to threads        (by default to any         signals in AppKit apps     SetConsoleCtrlHandler
                    eligible thread)           should be handled in       for Ctrl+C (console)
                                               the main thread; some       WM_CLOSE for GUI windows
                                               signals cause issues if
                                               delivered to NSRunLoop

  Blocking signals   sigprocmask(2)            same POSIX API            N/A
                     per-thread sigprocmask
                     (pthread_sigmask)

  Signal as fd       signalfd(2) — get a fd    NOT available on macOS     N/A
  (event-driven)     you can read/poll for     (Linux-only syscall)
                     signal delivery           Use kqueue instead

  kqueue signals     Not applicable            kqueue EVFILT_SIGNAL:      N/A
  (macOS/BSD)                                  kevent with filter=
                                               EVFILT_SIGNAL, ident=
                                               SIGTERM → readable when
                                               SIGTERM delivered
                                               Works with main run loop
                                               Does NOT consume the signal
                                               (process still gets it)

  Daemon SIGHUP      Standard: reload config   Standard: same             No convention;
  pattern            trap it in signal handler  but use kqueue EVFILT_     use Service
                     or signalfd               SIGNAL in server code       OnCustomCommand

  SIGPIPE            Write to closed pipe      Same; extra caveat:        No equivalent
                     → SIGPIPE (default: exit)  Darwin may deliver to       (write returns error)
                     Fix: signal(SIGPIPE,        random thread in multi-
                       SIG_IGN) or              threaded app
                       SO_NOSIGPIPE on socket

  Cross-platform server pattern (handles both Linux signalfd and macOS kqueue):
    Use libuv (Node.js), libevent, or Tokio — these abstract the OS difference
    libuv: uv_signal_t works on both (uses kqueue on macOS, signalfd on Linux)
    Tokio: tokio::signal::ctrl_c() + tokio::signal::unix::signal()
    If writing C: detect at compile time with #ifdef __APPLE__ / #ifdef __linux__
```

## 8. SwiftUI vs AppKit

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    UI FRAMEWORK LANDSCAPE                                   │
│                                                                             │
│  AppKit (macOS 10.0, 1999)          SwiftUI (macOS 10.15, 2019)             │
│  ┌─────────────────────────────┐    ┌─────────────────────────────────┐   │
│  │ NSApplication               │    │ @main struct MyApp: App { }      │   │
│  │ NSWindow + NSWindowDelegate │    │ WindowGroup { ContentView() }    │   │
│  │ NSViewController            │    │ View protocol + body: some View  │   │
│  │ NSView (manual layout)      │    │ Declarative; no subclassing      │   │
│  │ Auto Layout (NSLayoutAnchor)│    │ Layout: HStack/VStack/ZStack     │   │
│  │ NSTableView / NSOutlineView │    │ List, LazyVStack, Grid           │   │
│  │ NSMenu / NSMenuItem         │    │ Commands { }  (menu builder)     │   │
│  │ Target-action pattern       │    │ @State, @Binding, @StateObject   │   │
│  │ Delegate pattern            │    │ onChange, onTapGesture closures  │   │
│  └─────────────────────────────┘    └─────────────────────────────────┘   │
│                                                                             │
│  Windows bridge:                                                            │
│    AppKit NSWindow  ↔  WPF Window                                          │
│    NSView           ↔  WPF UserControl / FrameworkElement                  │
│    NSViewController ↔  WPF ViewModel (sort of) + code-behind               │
│    Auto Layout      ↔  WPF Grid with ColumnDefinitions + binding sizes     │
│    SwiftUI @State   ↔  WPF INotifyPropertyChanged + DependencyProperty    │
│    SwiftUI previews ↔  WPF XAML Designer hot reload                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### AppKit Quick Reference

```swift
// Minimal AppKit app
import AppKit

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        window = NSWindow(
            contentRect: NSMakeRect(0, 0, 800, 600),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )
        window.center()
        window.title = "My App"
        window.contentViewController = MyViewController()
        window.makeKeyAndOrderFront(nil)
    }
}

// View controller
class MyViewController: NSViewController {
    override func loadView() {
        self.view = NSView(frame: NSMakeRect(0, 0, 800, 600))
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        let label = NSTextField(labelWithString: "Hello, macOS")
        label.frame = NSMakeRect(100, 300, 200, 30)
        view.addSubview(label)
    }
}
```

### SwiftUI on macOS Quick Reference

```swift
import SwiftUI

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .commands {
            CommandGroup(replacing: .newItem) {
                Button("New Document") { }
                    .keyboardShortcut("n", modifiers: .command)
            }
        }
        // Settings window
        Settings {
            SettingsView()
        }
    }
}

struct ContentView: View {
    @State private var items = ["Item 1", "Item 2", "Item 3"]
    @State private var selection: String?

    var body: some View {
        NavigationSplitView {
            List(items, id: \.self, selection: $selection) { item in
                Text(item)
            }
            .listStyle(.sidebar)
        } detail: {
            if let sel = selection { Text("Selected: \(sel)") }
            else { Text("Select an item") }
        }
        .frame(minWidth: 600, minHeight: 400)
    }
}
```

### Mac Catalyst

```
iPad app (UIKit)  ────► Mac Catalyst ────► macOS app (UIKit running on AppKit)
                         ~80% automatic
                         remaining: idiom checks + conditional compilation

// Detect Catalyst at runtime
#if targetEnvironment(macCatalyst)
    // Mac-specific code
#endif

// UI idiom check
if UIDevice.current.userInterfaceIdiom == .mac { }
```

Limitations: UIKit assumptions leak through (iPad-sized tap targets, UINavigationController).
Consider native AppKit or SwiftUI instead for heavy macOS apps.

### SwiftUI macOS vs iOS Gotchas

| Behavior | iOS SwiftUI | macOS SwiftUI |
|----------|-------------|---------------|
| Default navigation | `NavigationStack` | `NavigationSplitView` |
| List selection | single tap | click (multi-select with Shift/Cmd) |
| Context menus | long press | right-click |
| `.toolbar` | bottom bar or nav bar | toolbar above content |
| Focus | limited | `@FocusState` + keyboard full support |
| Menu bar | N/A | `MenuBarExtra` (macOS 13+) |
| Window sizing | full screen | `.frame(minWidth:minHeight:)` |

---

## 9. macOS Networking and Security

### Network.framework (Modern)

```swift
import Network

// Client connection
let conn = NWConnection(
    host: "api.example.com",
    port: 443,
    using: .tls   // or .tcp for plain
)
conn.stateUpdateHandler = { state in
    switch state {
    case .ready:
        conn.send(content: data, completion: .contentProcessed { error in })
        conn.receive(minimumIncompleteLength: 1, maximumLength: 65536) { data, _, _, error in }
    case .failed(let error):
        print(error)
    case .cancelled:
        break
    default: break
    }
}
conn.start(queue: .global())

// Server listener
let listener = try NWListener(using: .tcp, on: 8080)
listener.newConnectionHandler = { conn in
    conn.start(queue: .global())
    // handle conn
}
listener.start(queue: .global())

// Path monitor (replaces SCNetworkReachability, Reachability.swift)
let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    if path.status == .satisfied {
        print("Connected; interface: \(path.availableInterfaces)")
    }
}
monitor.start(queue: .global())
```

### Keychain

```swift
import Security

// Store a password
func storePassword(_ password: String, for account: String, service: String) throws {
    let query: [String: Any] = [
        kSecClass as String:       kSecClassGenericPassword,
        kSecAttrService as String: service,
        kSecAttrAccount as String: account,
        kSecValueData as String:   password.data(using: .utf8)!,
        kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlocked
    ]
    let status = SecItemAdd(query as CFDictionary, nil)
    if status == errSecDuplicateItem {
        // Update existing
        let update: [String: Any] = [kSecValueData as String: password.data(using: .utf8)!]
        SecItemUpdate(query as CFDictionary, update as CFDictionary)
    } else if status != errSecSuccess {
        throw NSError(domain: NSOSStatusErrorDomain, code: Int(status))
    }
}

// Read a password
func readPassword(for account: String, service: String) throws -> String? {
    let query: [String: Any] = [
        kSecClass as String:            kSecClassGenericPassword,
        kSecAttrService as String:      service,
        kSecAttrAccount as String:      account,
        kSecReturnData as String:       true,
        kSecMatchLimit as String:       kSecMatchLimitOne
    ]
    var result: AnyObject?
    let status = SecItemCopyMatching(query as CFDictionary, &result)
    guard status == errSecSuccess, let data = result as? Data else { return nil }
    return String(data: data, encoding: .utf8)
}

// Bridge: DPAPI on Windows (CryptProtectData) ↔ kSecAttrAccessible on macOS
// Both tie credentials to OS user session; both transparent to app
// Windows: persisted in HKCU\...\Protect
// macOS: persisted in ~/Library/Keychains/login.keychain-db
```

### LocalAuthentication (Touch ID / Face ID)

```swift
import LocalAuthentication

let context = LAContext()
var error: NSError?

guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
    // no biometrics; fall back to password
    return
}

context.evaluatePolicy(
    .deviceOwnerAuthenticationWithBiometrics,
    localizedReason: "Unlock sensitive data"
) { success, authError in
    DispatchQueue.main.async {
        if success { /* proceed */ }
        else { /* show error */ }
    }
}

// Policy options:
//   .deviceOwnerAuthenticationWithBiometrics  — Touch ID / Face ID only
//   .deviceOwnerAuthentication                — biometrics OR password/passcode
```

---

## 10. Apple Silicon — Developer Notes

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    APPLE SILICON ARCHITECTURE                               │
│                                                                             │
│  Single SoC Package                                                         │
│  ┌────────────────────────────────────────────────────────────────────┐     │
│  │  P-cores (Performance)  │  E-cores (Efficiency)  │  GPU           │    │
│  │  High IPC, high clock   │  Low power, always on  │  Metal GPU     │    │
│  │  (runs your critical    │  (background agents,   │  (shares RAM   │    │
│  │   path code)            │   timer callbacks)     │  with CPU)     │    │
│  ├────────────────────────────────────────────────────────────────────┤    │
│  │  Unified Memory  (CPU + GPU + Neural Engine share one LPDDR pool)  │    │
│  │  No PCIe bus between CPU and GPU — zero-copy GPU data              │    │
│  ├────────────────────────────────────────────────────────────────────┤    │
│  │  Neural Engine  (ANE)  — CoreML inference, accelerated matmul     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Universal Binaries

A "fat binary" (Mach-O universal binary) contains multiple architecture slices.

```bash
# Inspect architectures
lipo -info /usr/bin/file
# Architectures in the fat file: /usr/bin/file are: x86_64 arm64

file MyApp
# MyApp: Mach-O universal binary with 2 architectures: [x86_64] [arm64]

# Create a fat binary from two separate builds
lipo -create MyApp-x86_64 MyApp-arm64 -output MyApp

# Extract one architecture
lipo -extract arm64 MyApp -output MyApp-arm64

# Check your current architecture
arch
# arm64    (on Apple Silicon)
# i386     (rare; old Intel Mac)
```

### Rosetta 2

Transparent x86_64 → arm64 binary translation, done at first launch (cached afterward).

```bash
# Force x86_64 in Terminal session
arch -x86_64 /bin/bash       # open x86_64 shell
arch -x86_64 brew install …  # install x86 Homebrew formula

# Check if a process is running under Rosetta
sysctl sysctl.proc_translated
# or in code:
var ret: Int32 = 0
var size = MemoryLayout<Int32>.size
sysctlbyname("sysctl.proc_translated", &ret, &size, nil, 0)
// ret == 1 means running under Rosetta

# Homebrew: maintain separate x86_64 install at /usr/local for legacy tools
/usr/local/bin/brew   # Intel Homebrew
/opt/homebrew/bin/brew  # ARM Homebrew
```

### GCD and Core Count

```swift
// GCD routes QoS to correct core type automatically
DispatchQueue.global(qos: .userInteractive).async { }  // → P-cores
DispatchQueue.global(qos: .background).async { }        // → E-cores

// Query core counts
import Darwin
var physicalCores: Int32 = 0
var size = MemoryLayout<Int32>.size
sysctlbyname("hw.physicalcpu", &physicalCores, &size, nil, 0)
// M3 Pro example: 12 physical (6P + 6E), appears as 12 logical
```

### Metal and Unified Memory

```swift
import Metal

let device = MTLCreateSystemDefaultDevice()!
// device.recommendedMaxWorkingSetSize  — how much GPU memory to target

// Zero-copy CPU → GPU buffer (no PCIe bottleneck on Apple Silicon)
let buffer = device.makeBuffer(
    bytes: myData,
    length: myData.count * MemoryLayout<Float>.size,
    options: .storageModeShared   // shared = CPU+GPU accessible, zero-copy
)!
// On Intel Mac with discrete GPU you'd use .storageModeManaged instead
```

---

## Decision Cheat Sheet

| Task | Tool / Approach |
|------|----------------|
| Install CLI tools | `xcode-select --install` (CLT) or Homebrew |
| Install GUI apps | Homebrew Cask, Mac App Store, direct .dmg |
| Run a background daemon | LaunchDaemon plist in `/Library/LaunchDaemons/` |
| Run a per-user background agent | LaunchAgent plist in `~/Library/LaunchAgents/` |
| Replace cron job | `StartCalendarInterval` in launchd plist |
| Crash isolation in app | XPC Service (PlugIns/ subdirectory of app bundle) |
| New macOS app, starting fresh | SwiftUI (cross-platform, previews, modern concurrency) |
| Complex document-based or legacy app | AppKit (full control, decades of APIs) |
| iOS app also on Mac | SwiftUI with platform checks, or Mac Catalyst |
| Sign for outside App Store | Developer ID Application cert + notarize + staple |
| Sign for Mac App Store | Apple Distribution cert + App Sandbox entitlement |
| Store credentials | Keychain (SecItemAdd / SecItemCopyMatching) |
| Biometric auth | LocalAuthentication framework |
| Profile CPU performance | Instruments Time Profiler (xcrun xctrace) |
| Debug memory | Instruments Allocations + Leaks |
| Debug low-level | LLDB (not GDB) |
| Find framework/dylib paths | `otool -L binary` |
| Inspect Mach-O | `otool`, `nm`, `objdump --macho`, `dyld_info` |
| Check signing status | `codesign -dv --verbose=4 MyApp.app` |
| Remove quarantine xattr | `xattr -d com.apple.quarantine file` |
| Build for both architectures | Universal binary via Xcode "Any Mac" destination |
| Force x86_64 (Rosetta) | `arch -x86_64 command` |

---

## Common Confusion Points

**1. /usr vs /opt/homebrew vs /System/Library**
`/usr/bin` and `/usr/lib` are SIP-protected Apple bins. Homebrew on Apple Silicon installs to `/opt/homebrew` to avoid collisions. Never try to write to `/usr/lib` — you'll hit SIP.

**2. launchctl load vs bootstrap**
`launchctl load` is legacy (pre-10.11); still works but shows deprecation warnings.
Modern approach: `launchctl bootstrap system /path/to/plist` and `launchctl bootout system/label`.

**3. codesign --deep is not always right**
`--deep` signs everything in one pass in random order. If a framework has a version symlink structure, order matters. Correct approach: sign inner bundles first (innermost → outward), sign app last. `--deep` is fine for simple apps; unreliable for complex framework trees.

**4. Notarization ≠ App Store review**
Notarization is automated malware scanning (minutes). App Store review is human review (hours to days). Notarization is required for Developer ID (direct download) distribution. You notarize, then staple — the stapled ticket lets Gatekeeper work offline.

**5. @executable_path vs @loader_path**
`@executable_path` is always the main app binary's directory — even inside a framework.
`@loader_path` is the directory of the binary that contains the reference — what you want for frameworks referencing their own dependencies.

**6. Darwin is open source; AppKit is not**
You can read the XNU source at github.com/apple/darwin-xnu. Foundation, AppKit, UIKit, Swift stdlib are not open source (though Swift compiler itself is).

**7. Keychain Access Groups and Team ID prefix**
The `$(AppIdentifierPrefix)` in entitlements expands to your Team ID + ".". Two apps share a Keychain group only if: same Team ID, same group name declared in both entitlements, and sandboxing (if applicable) allows it.

**8. App Sandbox on macOS is optional for Developer ID, required for App Store**
macOS does not sandbox all apps by default (unlike iOS). Developer ID apps can ship without sandboxing. Mac App Store requires it. The sandbox is enforced by the kernel's MAC framework using TCC policy.

**9. Mach-O is not PE/COFF**
Windows uses PE format (.exe, .dll). macOS uses Mach-O. Tools: `otool` (not dumpbin), `nm` (same name, different flags), `lldb` (not windbg). The linker is `ld` (Apple's ld64), not link.exe.

**10. dyld shared cache means you can't find system frameworks on disk**
`/System/Library/Frameworks/Foundation.framework/Foundation` may appear to exist as a file but is actually only in the dyld shared cache. Don't try to `dlopen()` system frameworks by path — link at build time and let dyld resolve.
