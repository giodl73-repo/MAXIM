# iOS Developer Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          iOS SYSTEM LAYERS                                  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  Your App (SwiftUI / UIKit)                                          │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Cocoa Touch Frameworks                                              │  │
│  │  UIKit · SwiftUI · WatchKit · tvOS · WidgetKit · StoreKit            │  │
│  │  CoreData · CloudKit · CoreLocation · HealthKit · ARKit              │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Media + Graphics                                                    │  │
│  │  CoreGraphics · CoreText · CoreImage · AVFoundation · Metal          │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Core Services                                                       │  │
│  │  Foundation · CoreFoundation · Security · CFNetwork · SQLite         │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  libSystem  (libc + libpthread + libdispatch + libobjc)              │  │
│  └────────────────────────────┬─────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  XNU Kernel + Darwin (same base as macOS)                            │  │
│  │  Mach · BSD · IOKit · Sandbox (every app, always)                    │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                               │                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Apple Silicon SoC (A-series / M-series on iPad)                     │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. iOS Architecture

### XNU on iOS: Key Differences from macOS

| Feature | macOS | iOS |
|---------|-------|-----|
| `fork()` | Yes (POSIX) | No — not allowed in sandboxed apps |
| `exec()` | Yes | No |
| JIT compilation | Yes (with entitlement) | No (prior to iOS 14.2); restricted even now |
| Multiple user accounts | Yes | No (single user; enterprise managed) |
| Unsigned code execution | Yes (without SIP) | Never — all code must be signed |
| Dynamic library loading | Yes (developer dylibs) | No — only system dylibs; app frameworks must be embedded |
| Terminal / shell access | Yes | No |
| Sandbox | Optional (App Store only) | Mandatory — every app, always |
| GUI customization | Menubar, Dock, etc. | Fixed: SpringBoard controls all |

### SpringBoard

SpringBoard is the iOS "shell" — it IS the home screen, the app launcher, the notification center, and the control center. It is the only process that can draw outside an app's window.

```
SpringBoard (com.apple.springboard)
├── Home Screen grid of app icons
├── Notification Center
├── Control Center
├── Lock Screen
├── App switcher
└── Manages app lifecycle signals → your app's UIApplicationDelegate
```

### App Lifecycle State Machine

```
┌──────────────────────────────────────────────────────────────────────┐
│                    APP LIFECYCLE STATES                              │
│                                                                      │
│  ┌─────────────┐                                                     │
│  │ Not Running │  ← fresh install, crashed, explicitly quit         │
│  └──────┬──────┘                                                     │
│         │ user taps icon / URL scheme / notification                 │
│         ▼                                                            │
│  ┌─────────────┐                                                     │
│  │  Inactive   │  ← in foreground but not receiving events           │
│  │             │    (phone call, Notification Center pull-down)      │
│  └──────┬──────┘                                                     │
│         │ OS hands events to app                                     │
│         ▼                                                            │
│  ┌─────────────┐  applicationDidBecomeActive(_:)                    │
│  │   Active    │  ← receiving touch events, running                 │
│  └──────┬──────┘  applicationWillResignActive(_:)                   │
│         │ user presses Home / other app comes foreground            │
│         ▼                                                            │
│  ┌─────────────┐  applicationDidEnterBackground(_:)                 │
│  │ Background  │  ← ~5 seconds to finish work                       │
│  │             │    beginBackgroundTask() buys 30 more seconds      │
│  └──────┬──────┘                                                     │
│         │ OS decides (low memory, time limit)                        │
│         ▼                                                            │
│  ┌─────────────┐                                                     │
│  │  Suspended  │  ← frozen in RAM; no CPU time; can be killed        │
   │  └─────────────┘    without notification (jetsam)                 │
   │                                                                   │
   │  SwiftUI equivalent:  @Environment(\.scenePhase)                  │
   │    .active / .inactive / .background                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Memory Pressure and Jetsam

iOS has no swap. Under memory pressure, the OS kills suspended apps silently (jetsam).
Your app receives no signal when killed by jetsam — it just restarts next time.
State restoration is how you recover from this gracefully.

```swift
// In UIApplicationDelegate (UIKit)
func applicationDidReceiveMemoryWarning(_ application: UIApplication) {
    // Drop caches, release large images, etc.
}

// In SwiftUI
.onReceive(NotificationCenter.default.publisher(
    for: UIApplication.didReceiveMemoryWarningNotification)) { _ in
    // purge caches
}
```

---

## 2. Xcode Build System

### Project Hierarchy

```
MyWorkspace.xcworkspace          ← optional; groups multiple projects
└── MyApp.xcodeproj              ← the project file (actually a directory)
    ├── project.pbxproj          ← the actual build graph (Xcode's Makefile; never edit by hand)
    ├── MyApp.xcscheme           ← scheme: ties build/run/test/profile/archive
    └── xcshareddata/

Swift Packages (SPM):
  Package.swift                  ← no .xcodeproj; Xcode imports it directly
  Sources/
  Tests/
```

### Target Types

| Target | Output | Key Info |
|--------|--------|----------|
| App | .app bundle | Main product |
| Framework | .framework | Reusable code; embedded in app |
| Static Library | .a | No resources; linked at build time |
| App Extension | .appex | Runs in host process's sandbox |
| Unit Test Bundle | .xctest | XCTest framework; runs in-process |
| UI Test Bundle | .xctest | Runs in separate process; drives app via XCUIApplication |
| Watch App | .app | Requires companion iOS app target |
| Widget Extension | .appex | WidgetKit; displayed in Home Screen |
| Notification Service Ext | .appex | Modify push before display |
| Share Extension | .appex | Appears in share sheet |

### Scheme and Actions

```
Scheme "MyApp"
├── Build         ← which targets to build and in what order
├── Run           ← target + arguments + environment + launch via Xcode vs system
├── Test          ← test targets + test plan
├── Profile       ← launch under Instruments (Allocations, Time Profiler, etc.)
├── Analyze       ← Clang static analyzer
└── Archive       ← production build → IPA for TestFlight / App Store
```

### Build Settings Inheritance

```
Project-level (xcconfig or project settings)
    ↑ overridden by
Target-level settings
    ↑ overridden by
xcconfig file (if assigned)
    ↑ overridden by
Build phase environment

Practical use:
  Base.xcconfig          ← shared settings (SWIFT_VERSION, IPHONEOS_DEPLOYMENT_TARGET)
  Debug.xcconfig         ← SWIFT_OPTIMIZATION_LEVEL = -Onone; DEBUG=1
  Release.xcconfig       ← SWIFT_OPTIMIZATION_LEVEL = -O; ENABLE_BITCODE = NO

Assign in Xcode: Project → Info → Configurations → set xcconfig for Debug/Release
```

### Build Phases

```
1. Compile Sources          ← .swift, .m, .c, .cpp  →  .o object files
2. Link Binary with Libraries  ← ld64 links objects + frameworks → Mach-O binary
3. Copy Bundle Resources    ← assets, nibs, storyboards, Info.plist
4. Embed Frameworks         ← copies .framework bundles into app bundle
5. Run Script               ← arbitrary shell: SwiftGen, Sourcery, versioning, etc.

Key Build Setting → Value pairs:
  SWIFT_VERSION                   = 5.9
  IPHONEOS_DEPLOYMENT_TARGET      = 17.0
  PRODUCT_BUNDLE_IDENTIFIER       = com.myco.myapp
  CODE_SIGN_IDENTITY              = Apple Distribution
  PROVISIONING_PROFILE_SPECIFIER  = MyApp Distribution Profile
  ENABLE_TESTABILITY              = YES   (debug; allows @testable import)
  SWIFT_OPTIMIZATION_LEVEL        = -O    (release)
```

### Swift Package Manager

```swift
// Package.swift
// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "MyLibrary",
    platforms: [.iOS(.v16), .macOS(.v13)],
    products: [
        .library(name: "MyLibrary", targets: ["MyLibrary"]),
    ],
    dependencies: [
        .package(url: "https://github.com/Alamofire/Alamofire", from: "5.8.0"),
        .package(url: "https://github.com/apple/swift-algorithms", .upToNextMajor(from: "1.2.0")),
    ],
    targets: [
        .target(
            name: "MyLibrary",
            dependencies: [
                "Alamofire",
                .product(name: "Algorithms", package: "swift-algorithms"),
            ]
        ),
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]
        ),
    ]
)
```

```bash
# CLI workflow
swift build                     # build all targets
swift test                      # run all test targets
swift package resolve           # fetch dependencies (creates Package.resolved)
swift package update            # update to latest compatible versions
swift package show-dependencies # dependency graph
swift run MyExecutable          # run an executable target
```

---

## 3. Provisioning, Certificates, and Signing

This is the most confusing part of iOS for newcomers. Here is the full model.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               WHAT MUST ALL LINE UP TO INSTALL ON A DEVICE                  │
│                                                                             │
│  1. Certificate  — proves you are who you say (trusted by Apple)            │
│     Generated on your Mac (private key in Keychain)                         │
│     Apple signs the public key → certificate                                │
│                                                                             │
│  2. App ID       — identifier: com.myco.myapp (explicit or wildcard)        │
│     Registered on developer.apple.com                                       │
│     Enables specific capabilities: push, iCloud, HealthKit, etc.            │
│                                                                             │
│  3. Device UDID  — 40-char hex ID unique to each physical device            │
│     Must be registered in developer portal (development only)               │
│     Ad Hoc profiles: up to 100 registered UDIDs                             │
│                                                                             │
│  4. Provisioning Profile — a signed bag containing:                         │
│       { certificate + app ID + device list + entitlements + expiry }        │
│     Lives in ~/Library/MobileDevice/Provisioning Profiles/                  │
│     Embedded in the .ipa at build time                                      │
│                                                                             │
│  5. Entitlements — the capability list your app actually claims             │
│     Must be a subset of what the provisioning profile allows                │
│                                                                             │
│  codesign writes: binary + entitlements + profile seal → verifiable IPA     │
└─────────────────────────────────────────────────────────────────────────────┘

Windows bridge:
  Certificate + private key in Keychain  ↔  cert in Windows cert store (Personal)
  Provisioning profile                   ↔  ClickOnce/MSIX deployment manifest signed by cert
  Entitlements                           ↔  app manifest requested execution level / capabilities
```

### Profile Types

| Profile Type | Distribution | Device Restriction |
|-------------|-------------|-------------------|
| Development | Internal dev + testing | Up to 100 registered UDIDs |
| Ad Hoc | Share outside team, testing | Up to 100 registered UDIDs |
| App Store | App Store Connect submission | None (Apple's servers distribute) |
| Enterprise (In-House) | Internal apps (B2B) | None; requires $299/yr enterprise account |

### Xcode Automatic Signing

"Automatically manage signing" in Xcode does:
1. Creates/refreshes a Development provisioning profile
2. Registers the connected device UDID if not registered
3. Creates an App ID if it does not exist
4. Selects the correct certificate from your Keychain
5. Updates the profile when capabilities change

```
When to use manual signing:
  - CI/CD pipelines (no interactive Keychain unlock)
  - Enterprise distribution
  - Multiple certificates (personal vs corporate)
  - Fine-grained entitlement control
  - Using a distribution profile for device testing
```

### Manual Signing Workflow (CI)

```bash
# 1. Export .p12 from Keychain (cert + private key bundle)
#    Keychain Access → My Certificates → right-click → Export

# 2. Import on CI machine
security create-keychain -p "" build.keychain
security import cert.p12 -k build.keychain -P "$P12_PASSWORD" -T /usr/bin/codesign
security set-key-partition-list -S apple-tool:,apple: -s -k "" build.keychain
security list-keychains -d user -s build.keychain login.keychain

# 3. Install provisioning profile
cp MyApp.mobileprovision \
   ~/Library/MobileDevice/Provisioning\ Profiles/$(uuid_from_profile).mobileprovision

# 4. Build + sign
xcodebuild archive \
    -scheme MyApp \
    -archivePath build/MyApp.xcarchive \
    CODE_SIGN_IDENTITY="Apple Distribution: My Name (TEAMID)" \
    PROVISIONING_PROFILE_SPECIFIER="MyApp Distribution"

# 5. Export IPA
xcodebuild -exportArchive \
    -archivePath build/MyApp.xcarchive \
    -exportOptionsPlist ExportOptions.plist \
    -exportPath build/
```

### Entitlements File

```xml
<!-- MyApp.entitlements -->
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <!-- Push notifications -->
    <key>aps-environment</key>
    <string>production</string>            <!-- or: development -->

    <!-- iCloud Documents -->
    <key>com.apple.developer.icloud-container-identifiers</key>
    <array><string>iCloud.com.myco.myapp</string></array>
    <key>com.apple.developer.ubiquity-kvstore-identifier</key>
    <string>$(TeamIdentifierPrefix)com.myco.myapp</string>

    <!-- App Groups (share data with extensions) -->
    <key>com.apple.security.application-groups</key>
    <array><string>group.com.myco.myapp</string></array>

    <!-- HealthKit -->
    <key>com.apple.developer.healthkit</key>            <true/>
    <key>com.apple.developer.healthkit.access</key>
    <array><string>health-records</string></array>

    <!-- Wallet / Apple Pay -->
    <key>com.apple.developer.pass-type-identifiers</key>
    <array><string>pass.com.myco.myapp</string></array>

    <!-- Associated Domains (Universal Links + Sign in with Apple) -->
    <key>com.apple.developer.associated-domains</key>
    <array><string>applinks:myapp.example.com</string></array>

    <!-- Network Extension -->
    <key>com.apple.developer.networking.networkextension</key>
    <array><string>packet-tunnel-provider</string></array>
</dict>
</plist>
```

---

## 4. App Sandbox and Privacy

### iOS Container Structure

```
App Sandbox  (/private/var/mobile/Containers/Data/Application/<UUID>/)
├── Documents/          ← user-created files; visible in Files app if declared
│                          backed up by iCloud/iTunes; persist across updates
├── Library/
│   ├── Application Support/    ← app data files; backed up
│   ├── Caches/                 ← can be purged by OS; not backed up
│   └── Preferences/            ← UserDefaults plist (do not edit directly)
└── tmp/                ← temporary; purged when app not running; not backed up

App Bundle  (/private/var/containers/Bundle/Application/<UUID>/MyApp.app/)
  ← read-only; cannot write here

Shared Container (App Groups)
  ~/Library/Group Containers/group.com.myco.myapp/
  ← R/W; shared between app + extensions with matching app group entitlement
```

### FileManager Path API

```swift
let fm = FileManager.default

// Documents (user files, backed up)
let docs = fm.urls(for: .documentDirectory, in: .userDomainMask).first!

// Library/Application Support (app data, backed up)
let appSupport = fm.urls(for: .applicationSupportDirectory, in: .userDomainMask).first!

// Library/Caches (purgeable)
let caches = fm.urls(for: .cachesDirectory, in: .userDomainMask).first!

// tmp
let temp = URL(fileURLWithPath: NSTemporaryDirectory())

// App Group shared container
let group = fm.containerURL(forSecurityApplicationGroupIdentifier: "group.com.myco.myapp")!

// Exclude from backup (iCloud)
var url = appSupport.appendingPathComponent("big-cache-file")
try url.setResourceValues({ v in v.isExcludedFromBackup = true }())
```

### Privacy Strings (Required in Info.plist)

If you use any of these capabilities without the corresponding key, your app CRASHES on first access.

| Capability | Info.plist Key |
|-----------|---------------|
| Camera | `NSCameraUsageDescription` |
| Photo Library (read) | `NSPhotoLibraryUsageDescription` |
| Photo Library (write) | `NSPhotoLibraryAddUsageDescription` |
| Microphone | `NSMicrophoneUsageDescription` |
| Location (always) | `NSLocationAlwaysAndWhenInUseUsageDescription` |
| Location (when in use) | `NSLocationWhenInUseUsageDescription` |
| Contacts | `NSContactsUsageDescription` |
| Calendars | `NSCalendarsUsageDescription` |
| Reminders | `NSRemindersUsageDescription` |
| Bluetooth | `NSBluetoothAlwaysUsageDescription` |
| Motion (accelerometer) | `NSMotionUsageDescription` |
| Face ID | `NSFaceIDUsageDescription` |
| Health (read) | `NSHealthShareUsageDescription` |
| Health (write) | `NSHealthUpdateUsageDescription` |
| HomeKit | `NSHomeKitUsageDescription` |
| Local Network | `NSLocalNetworkUsageDescription` |
| NFC | `NFCReaderUsageDescription` |

### TCC (Transparency, Consent, Control)

TCC is the permission system. On first access to a protected resource, OS shows an alert with
your usage description string. User grants or denies. Stored in `/private/var/mobile/Library/TCC/`.

```swift
import AVFoundation

// Check current status (do not request — just check)
let status = AVCaptureDevice.authorizationStatus(for: .video)
switch status {
case .authorized:      // good to go
case .denied:          // user said no — direct to Settings
case .restricted:      // parental controls / MDM — cannot change
case .notDetermined:   // not asked yet
    AVCaptureDevice.requestAccess(for: .video) { granted in
        DispatchQueue.main.async { /* update UI */ }
    }
}

// Direct user to Settings after denial
if let url = URL(string: UIApplication.openSettingsURLString) {
    UIApplication.shared.open(url)
}
```

---

## 5. UIKit vs SwiftUI on iOS

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       UI FRAMEWORK COMPARISON                               │
│                                                                             │
│  UIKit                                    SwiftUI                           │
│  ┌──────────────────────────────┐        ┌────────────────────────────┐     │
│  │ UIViewController lifecycle  │        │ View.body computed prop    │   │
│  │   viewDidLoad()             │        │ .onAppear / .onDisappear   │   │
│  │   viewWillAppear()          │        │ @State, @Binding           │   │
│  │   viewDidAppear()           │        │ @StateObject, @ObservedObj │   │
│  │   viewWillDisappear()       │        │ @EnvironmentObject         │   │
│  │   viewDidDisappear()        │        │ @Environment(\.key)        │   │
│  │ UIView subclass + addSubview│        │ View protocol, body prop   │   │
│  │ Auto Layout constraints     │        │ HStack, VStack, ZStack     │   │
│  │ UITableView + dataSource    │        │ List / LazyVStack          │   │
│  │ UICollectionView + layout   │        │ LazyVGrid / LazyHGrid      │   │
│  │ UINavigationController      │        │ NavigationStack (iOS 16+)  │   │
│  │ UITabBarController          │        │ TabView                    │   │
│  │ present() / dismiss()       │        │ .sheet() / .fullScreenCover│   │
│  │ Storyboards / .xib files    │        │ No IB; all in code         │   │
│  └──────────────────────────────┘        └────────────────────────────┘   │
│                                                                             │
│  Universal bridge (any MVC framework):                                      │
│    UIViewController  ↔  any MVC controller (ASP.NET Controller,            │
│                          Android Activity, Rails controller action)         │
│    viewDidLoad()     ↔  constructor / initialize (resource setup)          │
│    viewWillAppear()  ↔  before_action / onResume (pre-render setup)        │
│    viewDidDisappear()↔  cleanup / onPause (teardown)                       │
│    UITableView       ↔  any virtual scroll list (RecyclerView, WPF         │
│                          ListView, ag-Grid)                                 │
│    @EnvironmentObject↔  DI container / ServiceLocator (universal)          │
│    App Sandbox       ↔  containerized process with restricted namespaces   │
│                          (Docker --read-only, k8s securityContext)         │
│                                                                             │
│  Windows bridge:                                                            │
│    UIViewController  ↔  WPF Page / UserControl + code-behind               │
│    Auto Layout       ↔  WPF Grid with star-sizing + margin                 │
│    UITableView       ↔  WPF ListView + ItemsControl                        │
│    UINavigationCtrl  ↔  WPF NavigationWindow / Frame                       │
│    @StateObject      ↔  WPF ViewModel with INotifyPropertyChanged          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### UIViewController Lifecycle — Universal MVC Controller Bridge

```
CONTROLLER LIFECYCLE PATTERN — CROSS-FRAMEWORK
════════════════════════════════════════════════════════════════════════

  Phase            UIViewController     Android Activity     ASP.NET MVC          Rails/Express
  ──────────────   ─────────────────    ─────────────────    ──────────────────   ─────────────────
  Instantiation    init() / initCoder   onCreate()           Controller ctor       initialize
  Resource setup   viewDidLoad()        onCreate() cont.     before_action         before_action
  About to show    viewWillAppear()     onResume()           (no equiv — stateless)(no equiv)
  Shown            viewDidAppear()      (onWindowFocusChanged)(no equiv)           (no equiv)
  About to hide    viewWillDisappear()  onPause()            (no equiv)            after_action
  Hidden           viewDidDisappear()   onStop()             (no equiv)            (no equiv)
  Destroyed        deinit              onDestroy()           Dispose()             (GC)

  The universal pattern:
  1. Constructor / init: inject dependencies, set up stable state
  2. Will-appear / resume: refresh data, register observers/listeners
  3. Did-disappear / pause: save state, unregister observers (prevent leaks)
  4. Destroy / deinit: release resources, close connections

  Why iOS differs from stateless web controllers:
  iOS UIViewController is long-lived and may appear/disappear many times.
  ASP.NET MVC Controller is request-scoped and stateless by default.
  Android Activity is closer to UIViewController (long-lived, state machine).
  The "will/did appear" hooks have no web equivalent because web is stateless.
```

### APNs Universal Push Notification Bridge

```
PUSH NOTIFICATION BROKER COMPARISON
════════════════════════════════════════════════════════════════════

  Concept        APNs (Apple)           FCM (Google/Firebase)     WNS (Windows)
  ──────────     ──────────────────     ──────────────────────     ──────────────────────
  Device token   256-byte token         Registration token         Channel URI (URL)
                 per-device per-app     (string)                   per-device per-app
  Auth           APNs auth key (.p8)    Server key / OAuth 2.0    Client secret + cert
                 or certificate         service account
  Protocol       HTTP/2                 HTTP v1 (REST)             HTTP REST
  Payload        JSON ≤ 4KB             JSON                       XML or JSON ≤ 5KB
  Delivery       At-most-once           At-most-once               At-most-once
  guarantee      (best effort)          (best effort)              (best effort)
  Priority       high / normal          high / normal              high / normal
  TTL / expiry   expiration header      time_to_live (sec)         X-WNS-TTL header
  Badge/sound    Yes (apns-push-type)   Yes (notification obj)     Yes (tile/toast/badge)
  Silent push    content-available: 1   data-only message          (none standard)
  Collapse key   apns-collapse-id       collapse_key               X-WNS-Tag

  All three share the same architecture:
    App server → broker API → broker cloud → device push channel → OS → app

  Cross-platform push library:
    FCM can proxy to APNs — send to FCM, Google delivers to both Android + iOS
    One FCM project token can reach iOS devices (Firebase configures APNs keys)
    WNS is Windows-only; no cross-delivery
    Server: node-apn (Node.js), Firebase Admin SDK, or direct HTTP/2 to each broker
```

### UIKit Navigation Stack

```swift
// UIKit — programmatic navigation
let vc = DetailViewController()
navigationController?.pushViewController(vc, animated: true)
navigationController?.popViewController(animated: true)
navigationController?.popToRootViewController(animated: true)

// Modal presentation
let modal = ModalViewController()
modal.modalPresentationStyle = .pageSheet   // or .fullScreen, .formSheet
present(modal, animated: true)
dismiss(animated: true)

// Tab bar
let tabVC = UITabBarController()
tabVC.viewControllers = [
    UINavigationController(rootViewController: FeedVC()),
    UINavigationController(rootViewController: SearchVC()),
    UINavigationController(rootViewController: ProfileVC()),
]
tabVC.viewControllers?[0].tabBarItem = UITabBarItem(title: "Feed",
    image: UIImage(systemName: "house"), tag: 0)
```

### SwiftUI Navigation (iOS 16+)

```swift
// NavigationStack with typed path (iOS 16+)
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List(items) { item in
                NavigationLink(value: item) {
                    Text(item.title)
                }
            }
            .navigationTitle("Items")
            .navigationDestination(for: Item.self) { item in
                DetailView(item: item)
            }
        }
    }
}

// Deep link: push multiple items at once
path.append(item1)
path.append(item2)        // → navigates two levels deep
path.removeLast(2)        // → pop two levels
path = NavigationPath()   // → pop to root
```

### UIViewRepresentable / UIHostingController Interop

```swift
// Embed UIKit view in SwiftUI
struct MapView: UIViewRepresentable {
    @Binding var region: MKCoordinateRegion

    func makeUIView(context: Context) -> MKMapView {
        let map = MKMapView()
        map.delegate = context.coordinator
        return map
    }

    func updateUIView(_ map: MKMapView, context: Context) {
        map.setRegion(region, animated: true)
    }

    func makeCoordinator() -> Coordinator { Coordinator(self) }

    class Coordinator: NSObject, MKMapViewDelegate {
        var parent: MapView
        init(_ parent: MapView) { self.parent = parent }
        // implement delegate methods
    }
}

// Embed SwiftUI view in UIKit
let swiftUIView = SomeSwiftUIView()
let hosting = UIHostingController(rootView: swiftUIView)
addChild(hosting)
view.addSubview(hosting.view)
hosting.view.frame = view.bounds
hosting.didMove(toParent: self)
```

### When UIKit is Still Necessary

| Scenario | Why UIKit |
|----------|-----------|
| `UITextView` with precise cursor positioning | SwiftUI TextEditor lacks fine control |
| `UICollectionViewLayout` custom layouts | SwiftUI Grid cannot replicate all compositional layouts |
| `UIScrollView` with complex delegate logic | SwiftUI ScrollView has limited customization |
| `UIPageViewController` with gesture interception | Tricky to replicate exactly in SwiftUI |
| Third-party SDKs that provide UIView/UIViewController | Use UIViewRepresentable |
| Complex drag & drop (UIDragInteraction) | Partially available in SwiftUI, gaps remain |

---

## 6. Swift Concurrency

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SWIFT CONCURRENCY MODEL                                  │
│                                                                             │
│  Structured Concurrency  (Swift 5.5+)                                       │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  async func   — can be suspended and resumed                        │  │
│  │  await        — suspension point; thread is freed while waiting     │  │
│  │  Task { }     — unstructured; fire and forget; can cancel           │  │
│  │  async let    — parallel: start multiple async ops, await all       │  │
│  │  TaskGroup    — dynamic number of parallel child tasks              │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  Actors  (data isolation)                                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  actor        — reference type; only one caller at a time inside     │  │
│  │  @MainActor   — global actor pinned to main thread                   │  │
│  │  Sendable     — marker: safe to pass across actor boundaries         │  │
│  │  nonisolated  — method opts out of actor isolation                   │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  Bridge from GCD:                                                           │
│    DispatchQueue.main.async { } → await MainActor.run { }                  │
│    DispatchQueue.global().async { } → Task { } or Task.detached { }        │
│    DispatchGroup → async let / TaskGroup                                    │
│    OperationQueue → structured concurrency (rarely needed now)             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### async/await Patterns

```swift
// Basic async function
func fetchUser(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)
    guard (response as? HTTPURLResponse)?.statusCode == 200 else {
        throw APIError.badStatus
    }
    return try JSONDecoder().decode(User.self, from: data)
}

// Calling from SwiftUI
struct UserView: View {
    @State private var user: User?
    @State private var error: Error?

    var body: some View {
        Group {
            if let user { Text(user.name) }
            else if let error { Text(error.localizedDescription) }
            else { ProgressView() }
        }
        .task {                              // .task is a SwiftUI View modifier
            do { user = try await fetchUser(id: "42") }
            catch { self.error = error }
        }                                    // task is cancelled when view disappears
    }
}

// Parallel fetches with async let
func loadDashboard() async throws -> Dashboard {
    async let user    = fetchUser(id: "42")
    async let posts   = fetchPosts(userId: "42")
    async let friends = fetchFriends(userId: "42")
    // all three started concurrently; await all here
    return Dashboard(
        user: try await user,
        posts: try await posts,
        friends: try await friends
    )
}

// Dynamic parallel work with TaskGroup
func fetchAllImages(urls: [URL]) async throws -> [UIImage] {
    try await withThrowingTaskGroup(of: UIImage.self) { group in
        for url in urls {
            group.addTask { try await downloadImage(from: url) }
        }
        var images: [UIImage] = []
        for try await image in group {
            images.append(image)
        }
        return images
    }
}
```

### @MainActor

```swift
// Mark a class as always running on main thread
@MainActor
class ViewModel: ObservableObject {
    @Published var items: [Item] = []

    func load() async {
        // we're on main actor, but URLSession suspends → releases main thread
        let data = try? await URLSession.shared.data(from: url)
        // resumes on main actor — items update is safe
        items = parse(data)
    }
}

// MainActor.run: explicitly hop to main thread
Task {
    let data = await fetchData()          // off main thread
    await MainActor.run {
        self.label.text = data.title     // on main thread
    }
}

// nonisolated: method does NOT require main thread
@MainActor
class MyClass {
    nonisolated func purePureComputation() -> Int { ... }  // no actor hop needed
}
```

### Actor for Data Isolation

```swift
actor ImageCache {
    private var cache: [URL: UIImage] = [:]

    func image(for url: URL) async -> UIImage? {
        return cache[url]
    }

    func store(_ image: UIImage, for url: URL) {
        cache[url] = image
    }
}

// Usage — cross-actor call requires await
let cache = ImageCache()
await cache.store(image, for: url)
let img = await cache.image(for: url)
```

### Combine (Legacy — Still Relevant)

```swift
import Combine

// Publisher pipeline
let cancellable = URLSession.shared
    .dataTaskPublisher(for: url)
    .map(\.data)
    .decode(type: [User].self, decoder: JSONDecoder())
    .receive(on: DispatchQueue.main)
    .sink(
        receiveCompletion: { completion in
            if case .failure(let error) = completion { print(error) }
        },
        receiveValue: { users in
            self.users = users
        }
    )

// Store cancellables to keep subscriptions alive
var cancellables = Set<AnyCancellable>()
publisher.sink { ... }.store(in: &cancellables)

// PassthroughSubject — imperative event source
let subject = PassthroughSubject<String, Never>()
subject.send("hello")
subject.sink { print($0) }.store(in: &cancellables)

// CurrentValueSubject — has current value + stream
let currentValue = CurrentValueSubject<Int, Never>(0)
currentValue.value = 42
```

---

## 7. Networking on iOS

### URLSession

```swift
// Shared (no configuration; cookies/cache shared with other uses)
let task = URLSession.shared.dataTask(with: url) { data, response, error in }
task.resume()

// Modern async API (preferred)
let (data, response) = try await URLSession.shared.data(from: url)

// Ephemeral (no persistent cache/cookies — good for private sessions)
let config = URLSessionConfiguration.ephemeral
let session = URLSession(configuration: config)

// Background (downloads/uploads survive app suspension)
let bgConfig = URLSessionConfiguration.background(withIdentifier: "com.myco.myapp.bg")
bgConfig.isDiscretionary = true     // OS picks best time (charging, wifi)
let bgSession = URLSession(configuration: bgConfig, delegate: self, delegateQueue: nil)

// Background download task
let task = bgSession.downloadTask(with: url)
task.resume()

// AppDelegate must handle URL session events on relaunch
func application(_ application: UIApplication,
                 handleEventsForBackgroundURLSession identifier: String,
                 completionHandler: @escaping () -> Void) {
    // Recreate the background session, save completionHandler
    // Call completionHandler() when URLSessionDelegate signals done
    backgroundCompletionHandler = completionHandler
}
```

### URLRequest Configuration

```swift
var request = URLRequest(url: URL(string: "https://api.example.com/items")!)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
request.httpBody = try JSONEncoder().encode(payload)
request.timeoutInterval = 30.0
request.cachePolicy = .reloadIgnoringLocalAndRemoteCacheData

let (data, response) = try await URLSession.shared.data(for: request)
let httpResponse = response as! HTTPURLResponse
// httpResponse.statusCode, httpResponse.allHeaderFields
```

### Common NSURLError Codes

| Code | Constant | Meaning |
|------|----------|---------|
| -999 | `cancelled` | Task cancelled by app |
| -1001 | `timedOut` | Request timed out |
| -1003 | `cannotFindHost` | DNS resolution failed |
| -1004 | `cannotConnectToHost` | TCP connection refused |
| -1005 | `networkConnectionLost` | Mid-request disconnect |
| -1009 | `notConnectedToInternet` | No network |
| -1012 | `userAuthenticationRequired` | 407 / HTTP auth |
| -1200 | `secureConnectionFailed` | TLS handshake failed |
| -1202 | `serverCertificateUntrusted` | Self-signed / unknown CA |

### Network Path Monitor

```swift
import Network

// NWPathMonitor replaces SCNetworkReachability + Reachability.swift
let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    switch path.status {
    case .satisfied:
        let isWifi = path.usesInterfaceType(.wifi)
        let isCellular = path.usesInterfaceType(.cellular)
        print("Connected; wifi=\(isWifi) cellular=\(isCellular)")
    case .unsatisfied:
        print("No network")
    case .requiresConnection:
        print("On-demand (VPN?)")
    @unknown default:
        break
    }
}
monitor.start(queue: DispatchQueue.global())

// At app teardown:
monitor.cancel()
```

### App Transport Security (ATS)

```xml
<!-- Info.plist: ATS is on by default (HTTPS required) -->

<!-- Allow specific domain over HTTP (must justify in App Store review) -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>internal-api.myco.com</key>
        <dict>
            <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key> <true/>
            <key>NSTemporaryExceptionMinimumTLSVersion</key> <string>TLSv1.2</string>
        </dict>
    </dict>
</dict>

<!-- Allow arbitrary HTTP (strongly discouraged; requires justification) -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key> <true/>
</dict>
```

---

## 8. Background Execution

iOS is aggressive about CPU/battery — apps do not run freely in the background.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BACKGROUND EXECUTION MODES                              │
│                                                                             │
│  Mode                │ Entitlement            │ Use Case                    │
│  ────────────────────┼────────────────────────┼────────────────────────     │
│  audio               │ UIBackgroundModes      │ Music, podcast, VoIP audio │
│  location            │ UIBackgroundModes      │ Navigation, tracking        │
│  voip                │ UIBackgroundModes      │ Incoming call (deprecated;  │
│                      │                        │ use PushKit instead)        │
│  fetch               │ UIBackgroundModes      │ BGAppRefreshTask            │
│  remote-notification │ UIBackgroundModes      │ Silent push triggers code  │
│  processing          │ UIBackgroundModes      │ BGProcessingTask            │
│  bluetooth-central   │ UIBackgroundModes      │ BLE central in background  │
│  bluetooth-peripheral│ UIBackgroundModes      │ BLE peripheral in bg       │
│  external-accessory  │ UIBackgroundModes      │ MFi accessories            │
│  newsstand-content   │ (deprecated)           │                            │
│  background URLSession── (automatic with bg URLSessionConfiguration)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### BGTaskScheduler (iOS 13+)

```swift
import BackgroundTasks

// AppDelegate.application(_:didFinishLaunchingWithOptions:)
BGTaskScheduler.shared.register(
    forTaskWithIdentifier: "com.myco.myapp.refresh",
    using: nil
) { task in
    handleAppRefresh(task: task as! BGAppRefreshTask)
}

BGTaskScheduler.shared.register(
    forTaskWithIdentifier: "com.myco.myapp.processing",
    using: nil
) { task in
    handleProcessing(task: task as! BGProcessingTask)
}

// Schedule (call from applicationDidEnterBackground or sceneDidEnterBackground)
func scheduleAppRefresh() {
    let request = BGAppRefreshTaskRequest(identifier: "com.myco.myapp.refresh")
    request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60)  // 15 min
    try? BGTaskScheduler.shared.submit(request)
}

func scheduleProcessing() {
    let request = BGProcessingTaskRequest(identifier: "com.myco.myapp.processing")
    request.requiresNetworkConnectivity = true
    request.requiresExternalPower = true               // only when charging
    try? BGTaskScheduler.shared.submit(request)
}

// BGAppRefreshTask: ~30 seconds budget
func handleAppRefresh(task: BGAppRefreshTask) {
    scheduleAppRefresh()   // reschedule for next time

    let operation = RefreshOperation()
    task.expirationHandler = { operation.cancel() }

    operation.completionBlock = {
        task.setTaskCompleted(success: !operation.isCancelled)
    }
    OperationQueue.main.addOperation(operation)
}
```

### beginBackgroundTask (Legacy — Emergency Extra Time)

```swift
var bgTask: UIBackgroundTaskIdentifier = .invalid

func applicationDidEnterBackground(_ application: UIApplication) {
    bgTask = application.beginBackgroundTask(withName: "FinishWork") {
        // expiration handler: called ~30 seconds after entering background
        application.endBackgroundTask(self.bgTask)
        self.bgTask = .invalid
    }

    // Do critical work here (save state, flush logs, etc.)
    DispatchQueue.global().async {
        self.finishCriticalWork()
        application.endBackgroundTask(self.bgTask)
        self.bgTask = .invalid
    }
}

// In UIKit AppDelegate: application.backgroundTimeRemaining → shows seconds left
```

---

## 9. Push Notifications

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       APNs ARCHITECTURE                                     │
│                                                                             │
│  Your Server                  APNs                     Device               │
│  ┌───────────────┐           ┌──────────┐            ┌──────────────────┐   │
│  │               │           │  Apple   │            │  iOS app         │  │
│  │  POST /3/     │  TLS+HTTP2│  Push    │  persistent│  registers:      │  │
│  │  device/token │──────────►│  Notif   │  connection│  deviceToken =   │  │
│  │               │◄──────────│  service │◄───────────│  UIApplication   │  │
│  │  { aps: {     │  200 OK / │          │            │  .registerFor    │  │
│  │    alert: ... │  error    │          │            │  RemoteNotifs()  │  │
│  │  } }          │           │          │            │                  │  │
│  └───────────────┘           └──────────┘            └──────────────────┘  │
│                                                                             │
│  Auth: HTTP/2 bearer JWT (auth key .p8) OR TLS client cert                 │
│  Prefer auth key: doesn't expire; one key for all apps in team             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Device Token Registration

```swift
// AppDelegate
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Request permission
    UNUserNotificationCenter.current().requestAuthorization(
        options: [.alert, .badge, .sound]
    ) { granted, error in
        if granted {
            DispatchQueue.main.async {
                UIApplication.shared.registerForRemoteNotifications()
            }
        }
    }
    return true
}

func application(_ application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02x", $0) }.joined()
    // Send token to your server
    MyAPI.shared.register(pushToken: token)
}

func application(_ application: UIApplication,
                 didFailToRegisterForRemoteNotificationsWithError error: Error) {
    print("Push registration failed: \(error)")
}
```

### Notification Payload Structure

```json
{
  "aps": {
    "alert": {
      "title": "New message",
      "subtitle": "From Alice",
      "body": "Hey, are you free tonight?"
    },
    "badge": 5,
    "sound": "default",
    "thread-id": "conversation-42",
    "category": "MESSAGE",
    "mutable-content": 1,
    "content-available": 1
  },
  "custom-data": {
    "conversation-id": "42",
    "message-id": "99"
  }
}
```

| Field | Purpose |
|-------|---------|
| `alert` | Text displayed in notification |
| `badge` | App icon badge number (0 to clear) |
| `sound` | Audio; "default" or custom filename |
| `content-available: 1` | Silent push — wakes app in background |
| `mutable-content: 1` | Triggers Notification Service Extension |
| `thread-id` | Groups notifications together |
| `category` | Links to UNNotificationCategory for action buttons |

### UNUserNotificationCenter

```swift
import UserNotifications

// Schedule a local notification
let content = UNMutableNotificationContent()
content.title = "Reminder"
content.body = "Check your dashboard"
content.sound = .default
content.badge = 1

let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 60, repeats: false)
// or: UNCalendarNotificationTrigger / UNLocationNotificationTrigger

let request = UNNotificationRequest(identifier: "my-reminder", content: content, trigger: trigger)
UNUserNotificationCenter.current().add(request)

// Handle notification received while app is in foreground
class NotificationDelegate: NSObject, UNUserNotificationCenterDelegate {
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
                                withCompletionHandler completionHandler:
                                    @escaping (UNNotificationPresentationOptions) -> Void) {
        // Show banner even in foreground:
        completionHandler([.banner, .sound, .badge])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
        let id = response.actionIdentifier
        let userInfo = response.notification.request.content.userInfo
        // Handle tap or action button
        completionHandler()
    }
}
```

### Notification Service Extension

Fires when `mutable-content: 1` is set. Has ~30 seconds to modify notification content.

```swift
class NotificationService: UNNotificationServiceExtension {
    var contentHandler: ((UNNotificationContent) -> Void)?
    var bestAttemptContent: UNMutableNotificationContent?

    override func didReceive(_ request: UNNotificationRequest,
                             withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
        self.contentHandler = contentHandler
        bestAttemptContent = request.content.mutableCopy() as? UNMutableNotificationContent

        guard let best = bestAttemptContent,
              let urlString = best.userInfo["image-url"] as? String,
              let url = URL(string: urlString) else {
            contentHandler(request.content)
            return
        }

        // Download attachment
        URLSession.shared.downloadTask(with: url) { tempURL, _, _ in
            if let tempURL,
               let attachment = try? UNNotificationAttachment(identifier: "image",
                                                               url: tempURL) {
                best.attachments = [attachment]
            }
            contentHandler(best)
        }.resume()
    }

    override func serviceExtensionTimeWillExpire() {
        // Called when time is almost up — deliver best effort
        contentHandler?(bestAttemptContent ?? UNNotificationContent())
    }
}
```

---

## 10. TestFlight and App Store Distribution

### Build → Distribution Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DISTRIBUTION PIPELINE                                    │
│                                                                             │
│  Xcode                    App Store Connect           Devices               │
│  ┌──────────────────┐    ┌──────────────────────┐   ┌─────────────────┐     │
│  │ 1. Product →     │    │ 3. Processing (mins) │   │                 │   │
│  │    Archive       │    │ 4. TestFlight tab     │   │ Internal testers│   │
│  │                  │    │    - Internal (≤100)  │──►│ (same org)      │   │
│  │ 2. Distribute    │───►│    - External (≤10k) │──►│ External beta   │   │
│  │    App →         │    │      (Beta Review)    │   │                 │   │
│  │    App Store     │    │ 5. App Store tab       │──►│ All users       │   │
│  │    Connect       │    │    (full review)       │   │                 │   │
│  └──────────────────┘    └──────────────────────┘   └─────────────────┘   │
│                                                                             │
│  Or: xcodebuild archive + xcodebuild -exportArchive (CI)                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### CLI Build + Upload

```bash
# Archive
xcodebuild archive \
    -scheme "MyApp" \
    -archivePath "build/MyApp.xcarchive" \
    -destination "generic/platform=iOS" \
    CODE_SIGN_IDENTITY="Apple Distribution" \
    PROVISIONING_PROFILE_SPECIFIER="MyApp App Store"

# Export IPA
xcodebuild -exportArchive \
    -archivePath "build/MyApp.xcarchive" \
    -exportOptionsPlist "ExportOptions.plist" \
    -exportPath "build/"

# Upload to App Store Connect
xcrun altool --upload-app \
    --type ios \
    --file "build/MyApp.ipa" \
    --apiKey "$ASC_API_KEY_ID" \
    --apiIssuer "$ASC_ISSUER_ID"

# Or with newer notarytool-style uploader:
xcrun altool --upload-app -f build/MyApp.ipa \
    --apiKey "$KEY_ID" --apiIssuer "$ISSUER_ID"
```

### ExportOptions.plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>method</key>
    <string>app-store</string>           <!-- app-store | ad-hoc | development | enterprise -->

    <key>teamID</key>
    <string>MYTEAMID</string>

    <key>signingStyle</key>
    <string>manual</string>              <!-- automatic | manual -->

    <key>provisioningProfiles</key>
    <dict>
        <key>com.myco.myapp</key>
        <string>MyApp App Store Distribution</string>
    </dict>

    <key>uploadSymbols</key>             <true/>
    <key>uploadBitcode</key>             <false/>   <!-- Bitcode deprecated Xcode 14+ -->
    <key>stripSwiftSymbols</key>         <true/>
</dict>
</plist>
```

### TestFlight Notes

| Concept | Detail |
|---------|--------|
| Internal testers | Up to 100; must be in App Store Connect team; available immediately after upload |
| External testers | Up to 10,000; can be anyone with email invite; requires Beta App Review (~1 day) |
| Build expiry | TestFlight builds expire after 90 days |
| Feedback | Testers can send feedback with screenshot from TestFlight app |
| App Store Connect API | Use API key (not Apple ID) for CI to avoid 2FA |

### Phased Release

```
Day 1: 1%     of new app updates
Day 2: 2%
Day 3: 5%
Day 4: 10%
Day 5: 20%
Day 6: 50%
Day 7: 100%

You can pause/halt rollout at any stage in App Store Connect.
Useful for catching crashes before full release.
Does NOT affect first-time downloads — only existing users updating.
```

### Crash Symbolication

```bash
# dSYM: debug symbol file generated during archive
# Xcode uploads dSYM automatically if "Upload symbols" checked in export
# Or manual upload:
xcrun altool --upload-app ...  # handles dSYM too
# OR:
xcrun symbols -noTextInSOD -noDaemon -arch arm64 \
    -symbolsPackageDir ./output MyApp.app.dSYM

# Manually symbolicate a crash report
xcrun symbolicatecrash MyCrash.crash MyApp.app.dSYM > symbolicated.crash

# Get dSYM UUID (must match crash report)
dwarfdump --uuid MyApp.app.dSYM/Contents/Resources/DWARF/MyApp
xcrun dsymutil --show-debug-info-plist MyApp.app.dSYM
```

---

## 11. Debugging and Instruments

### Xcode Debugger

```
Breakpoint types:
  Line breakpoint       — click gutter
  Symbolic breakpoint   — Debug → Breakpoints → Symbolic; break on any -[ClassName method]
  Exception breakpoint  — break on all Objective-C / Swift exceptions (essential)
  Runtime issue         — break on main-thread checker / sanitizer violations
  Watchpoint            — break when memory address changes (Data → right-click var → Watch)

LLDB in Xcode console:
  po self                    — print object description
  p self.count               — print expression (uses LLDB formatter)
  expr self.items = []       — mutate in-flight
  bt                         — full backtrace
  thread info                — current thread details
  frame info                 — current frame's source location

View Hierarchy Debugger:
  Debug → View Debugging → Capture View Hierarchy
  3D exploded view of all views + Auto Layout violations
  Inspect any view's frame, alpha, hidden state

Memory Graph Debugger:
  Debug → Memory Graph Debugger
  Shows all live objects + reference cycles (purple !-badge = leak)
```

### os_log (Production Logging)

```swift
import OSLog

// Create subsystem.category logger — appears in Console.app
private let logger = Logger(subsystem: "com.myco.myapp", category: "networking")

// Log levels:
logger.debug("Request started: \(url, privacy: .public)")    // debug only
logger.info("Response received: \(statusCode)")               // info
logger.notice("Retry attempt \(attempt) of \(maxAttempts)")  // notice (default)
logger.warning("Rate limit approaching: \(remaining)")        // warning
logger.error("Request failed: \(error.localizedDescription)") // error
logger.critical("Database corruption detected")                // fault/critical

// Privacy: .public = shown in log; .private = redacted in release builds
logger.debug("User id: \(userId, privacy: .private)")   // redacted in production

// OSSignposter — for Instruments "Points of Interest" / "Signpost" timeline
private let signposter = OSSignposter(subsystem: "com.myco.myapp", category: "rendering")

let intervalID = signposter.beginInterval("renderFrame", id: signposter.makeSignpostID())
// ... do work ...
signposter.endInterval("renderFrame", intervalID)
```

### Instruments Templates (iOS)

| Template | What It Shows | Key Use Case |
|----------|-------------|-------------|
| Time Profiler | CPU call-stack samples every 1ms | Find slow code |
| Allocations | Heap allocations over time; generation snapshots | Memory growth |
| Leaks | Reference cycles; objects never freed | Retain cycle |
| Network | All URLSession requests + response times | Slow API calls |
| Energy Log | CPU/GPU/network/location wakeups | Battery drain |
| Core Data | Fetches, saves, faults | N+1 fetches |
| System Trace | Thread scheduling, VM faults, syscalls | Deep thread issues |
| SwiftUI | View body calls, attribute graph diff | SwiftUI perf |

```bash
# Record from CLI (CI or remote device)
xcrun xctrace record \
    --template "Time Profiler" \
    --device "My iPhone" \
    --duration 15 \
    --launch -- com.myco.myapp

# Simulator control — useful in CI pipelines
xcrun simctl list devices available       # list simulators
xcrun simctl boot "iPhone 15 Pro"         # boot a simulator
xcrun simctl install booted MyApp.app     # install build
xcrun simctl launch booted com.myco.myapp # launch app
xcrun simctl shutdown "iPhone 15 Pro"
xcrun simctl erase "iPhone 15 Pro"        # factory reset simulator

# Push simulated notification to Simulator
xcrun simctl push booted com.myco.myapp notification.apns
```

### Address Sanitizer (ASan)

```
Enable: Xcode → Edit Scheme → Diagnostics → Address Sanitizer ✓

Catches:
  - Heap buffer overflows
  - Stack buffer overflows
  - Use-after-free
  - Use-after-return
  - Double-free

Performance impact: ~2× slower; not for production.
For Swift, Main Thread Checker catches UI-on-background-thread bugs.
Thread Sanitizer (TSan) catches data races between threads.
```

### Crash Reports

```
Device crash logs location (connected to Mac):
  Xcode → Window → Devices and Simulators → View Device Logs

Programmatic crash reporting:
  App Store Connect → App → Crashes (if dSYM uploaded)
  Or: third-party — Firebase Crashlytics, Sentry, Bugsnag

Crash report structure:
  Incident Identifier   — UUID
  CrashReporter Key     — anonymized device ID
  Hardware Model        — iPhone15,2
  Process               — MyApp [1234]
  Exception Type        — EXC_BAD_ACCESS SIGSEGV / EXC_CRASH SIGABRT
  Exception Subtype     — KERN_INVALID_ADDRESS at 0x0000000000000000
  Thread 0 Crashed:
    frame #0  MyApp  0x000000010001234  MyClass.myMethod() + 48
    frame #1  ...

Symbolicated frame example (after dsymutil):
  frame #0  0x000000010001234  MyClass.myMethod (MyClass.swift:42)
```

---

## Decision Cheat Sheet

| Task | Tool / Approach |
|------|----------------|
| New iOS app, 2025 | SwiftUI + Swift Concurrency (async/await) |
| Complex custom table/collection | UIKit UITableView / UICollectionView |
| Embed UIKit in SwiftUI | `UIViewRepresentable` / `UIViewControllerRepresentable` |
| Embed SwiftUI in UIKit | `UIHostingController` |
| Share data between app + extension | App Group entitlement + shared container |
| Run code when app is suspended | BGAppRefreshTask (30s) or BGProcessingTask (minutes) |
| Download in background | Background URLSessionConfiguration |
| Push notifications | APNs + UNUserNotificationCenter + auth key (.p8) |
| Modify push before display | Notification Service Extension |
| Custom push notification UI | Notification Content Extension |
| Store credentials | Keychain (same API as macOS) |
| Biometric auth | LocalAuthentication (same as macOS) |
| Network connectivity check | NWPathMonitor |
| Network request | URLSession async/await |
| Parallel async work | async let / TaskGroup |
| UI always on main thread | @MainActor |
| Profile CPU | Instruments Time Profiler |
| Find memory leaks | Instruments Leaks + Memory Graph |
| Distribute for beta | TestFlight (internal or external) |
| Build on CI | xcodebuild archive + xcodebuild -exportArchive |
| Symbolicate crashes | xcrun symbolicatecrash + dSYM |
| Control Simulator from CLI | xcrun simctl |
| Log in production | os_log / Logger (not print) |

---

## Common Confusion Points

**1. iOS does not have fork() — no child processes**
Everything runs in a single process (sandbox). If you need isolation, use App Extensions (separate process in same sandbox group) or XPC. You cannot spawn subprocesses with `Process` (which works on macOS but not iOS).

**2. The app is killed silently by jetsam — not by SIGKILL you can catch**
When iOS reclaims memory from a suspended app, there is no signal, no notification, no chance to save state. Your app just restarts cold next launch. Use `UIStateRestoration` or `SceneDelegate`'s state restoration to handle this gracefully.

**3. Provisioning profiles go stale — "No signing certificate" on CI**
Certificates expire yearly. Profiles reference certificates by fingerprint and expire too (1 year for development, 1 or 3 years for distribution). Tools: `fastlane match` stores certs + profiles in a git repo or S3, solves the CI rotation problem.

**4. `content-available` silent push does not guarantee execution**
iOS delivers silent push only when: device is not in Low Power Mode, not in Airplane Mode, app has been launched by user at least once, and the OS decides it is appropriate. Never rely on silent push for time-critical work.

**5. BGAppRefreshTask does not fire on your schedule**
`earliestBeginDate` is a minimum delay, not a guaranteed time. iOS learns usage patterns (on-device ML) and fires tasks when predicted to be convenient. In Simulator, use `e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"com.myco.myapp.refresh"]` to force fire.

**6. App Groups are not the same as Keychain Access Groups**
App Groups: share a `containerURL` (filesystem directory) and UserDefaults. Keychain Access Groups: share Keychain items. Both need the same team ID. Both need entitlements on both targets. They are separate capabilities with separate provisioning requirements.

**7. NavigationView is deprecated in iOS 16 — use NavigationStack**
`NavigationView` still compiles but has well-known layout bugs, especially on iPad. `NavigationStack` (iOS 16+) with typed paths is the correct modern API. `NavigationSplitView` is for iPad/Mac sidebar layouts.

**8. @ObservedObject vs @StateObject**
`@StateObject`: owns the object; created once when view first appears; survives re-renders.
`@ObservedObject`: does not own; assumes parent injected it; recreated if parent re-renders with new instance.
Rule: if your view creates the object, use `@StateObject`. If it receives it from outside, use `@ObservedObject`.

**9. URLSession background tasks need delegate, not completion handlers**
Background download/upload tasks do not support completion-handler-based API. You must set a delegate on the URLSession. The app may be relaunched by the OS; the delegate's `urlSessionDidFinishEvents(forBackgroundURLSession:)` is the cue to call the stored completion handler from `handleEventsForBackgroundURLSession`.

**10. dSYM must match the exact binary**
Each build has a UUID embedded in its Mach-O. The dSYM UUID must match. If you rebuild without archiving (different build), you get a new UUID and the old dSYM cannot symbolicate crashes from new builds. Always archive + upload dSYM together as an atomic operation in CI.
