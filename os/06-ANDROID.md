# Android Developer Reference

## The Android Stack — Big Picture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          YOUR APP                                    │
│   Activities · Fragments · Services · BroadcastReceivers · Providers│
└────────────────────────────┬────────────────────────────────────────┘
                             │ calls
┌────────────────────────────▼────────────────────────────────────────┐
│                     ANDROID FRAMEWORK                                │
│  ActivityManager · WindowManager · PackageManager · NotificationMgr │
│  ContentResolver · TelephonyManager · LocationManager · etc.        │
└────────────────────────────┬────────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────────┐
│               ANDROID RUNTIME (ART) + CORE LIBRARIES                │
│  ART: AOT compilation + JIT profiling + GC                          │
│  Java API layer: java.*, android.*, androidx.*                       │
│  Native libs: OpenGL ES, libc (Bionic), media, SQLite, WebKit       │
└────────────┬───────────────────────────┬────────────────────────────┘
             │                           │
┌────────────▼──────────┐   ┌────────────▼────────────────────────────┐
│   HAL (Hardware       │   │  NATIVE DAEMONS                         │
│   Abstraction Layer)  │   │  SurfaceFlinger (compositor)            │
│   camera.default.so   │   │  AudioFlinger (audio mixer)             │
│   gps.default.so      │   │  ServiceManager (Binder registry)       │
│   sensors.default.so  │   │  Zygote (app spawner)                   │
└────────────┬──────────┘   └────────────┬────────────────────────────┘
             │                           │
┌────────────▼───────────────────────────▼────────────────────────────┐
│                   LINUX KERNEL (modified)                            │
│  Binder IPC driver · Wakelocks · Low Memory Killer (LMK)            │
│  Ashmen (shared memory) · ION allocator · USB Gadget driver         │
└─────────────────────────────────────────────────────────────────────┘
```

**Android is NOT standard Linux.**  Key divergences:

| Aspect               | Standard Linux            | Android                              |
|----------------------|---------------------------|--------------------------------------|
| IPC mechanism        | Unix domain sockets       | Binder (kernel driver, one-copy IPC) |
| C library            | glibc                     | Bionic (lighter, BSD-derived)        |
| Init                 | systemd / SysVinit        | init → Zygote → SystemServer         |
| Display server       | X11 / Wayland             | SurfaceFlinger (no X11 ever)         |
| App isolation        | uid/gid only              | uid per-app + SELinux + seccomp      |
| Package manager      | apt/rpm                   | PackageManager service               |
| Log system           | syslog / journald         | logd + logcat (circular ring buffer) |

---

## Android Runtime (ART) — How Apps Actually Execute

```
  Source: .java / .kt
        │
        ▼ (kotlinc / javac)
  .class bytecode
        │
        ▼ (d8 / R8 in AGP)
  .dex (Dalvik EXecutable) — inside .apk / .aab
        │
        ▼ (at install time)
  ┌─────────────────────────────────────────────┐
  │  ART  (Android Runtime)                     │
  │                                             │
  │  AOT: dex2oat → .oat (native machine code) │
  │       compiled at install / after boot      │
  │                                             │
  │  JIT: profile-guided; hotspot methods       │
  │       compiled during first run sessions    │
  │       profile saved to /data/misc/profiles/ │
  │                                             │
  │  GC: Concurrent Copying GC (CC) — low pause│
  └─────────────────────────────────────────────┘
```

**Profile-guided compilation** — the real story:
1. First install: mostly interpreted + JIT
2. Device charges at night → `speed-profile` compilation via `BackgroundDexOptService`
3. Subsequent boots: hotspot code runs as pre-compiled native code
4. On-device profiles also uploaded (with consent) → used to pre-optimize Play-distributed APKs at install

**Zygote — the app spawning model:**
```
  boot
   │
   ▼
  init → Zygote starts
          │  pre-loads: Android framework classes, common resources
          │  opens a socket: /dev/socket/zygote
          │
          │  ActivityManager requests new app
          ▼
      fork()  ← copy-on-write; near-instant; shared framework pages
          │
          ▼
      new process: your app
          │  copy-on-write pages diverge only when written
          ▼
      Application.onCreate() → Activity.onCreate()
```

**Why this matters:** App cold starts in ~50-100ms because the JVM and framework are already loaded. The fork cost is nearly zero. Compare to .NET: every process boots the CLR fresh — no Zygote equivalent.

**SystemServer** — spawned from Zygote on boot, runs all Android services:
- ActivityManagerService (app lifecycle)
- WindowManagerService (window stacking, input dispatch)
- PackageManagerService (APK installation, queries)
- PowerManagerService (wakelocks, screen off)
- ~50 more services — all in one process, communicate via Binder

---

## The Four App Components (+ two supporting mechanisms)

Android apps are not monolithic executables. The OS **assembles** an app from declared components.

```
  ┌──────────────────────────────────────────────────────────────┐
  │  Your App Process                                            │
  │                                                              │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
  │  │ Activity │  │ Fragment │  │ Service  │  │ Broadcast  │  │
  │  │ (screen) │  │ (UI unit)│  │ (bg work)│  │ Receiver   │  │
  │  └──────────┘  └──────────┘  └──────────┘  └───────────┘  │
  │        ▲                                          │         │
  │        │ resolves to                              │ fires   │
  │  ┌─────┴──────────────────────────────────────────▼──────┐  │
  │  │                      Intent                           │  │
  │  │  (the Android message bus — all component wiring)     │  │
  │  └──────────────────────────────────────────────────────┘  │
  │                                                              │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  ContentProvider  (structured data sharing via URI)  │   │
  │  └──────────────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────┘
```

### Activity — A Screen With UI

```
           onCreate()   ← Bundle savedInstanceState (rotation/kill)
               │
           onStart()    ← visible but not interactive
               │
           onResume()   ← foreground, interactive ← ── ┐
               │                                        │
           [user navigates away]                        │
               │                                        │
           onPause()    ← partially hidden              │ returns
               │         save quick state here          │
           onStop()     ← fully hidden                  │
               │         can be killed here (no callback│
           onDestroy()  ← rotating, finishing, killed   │
                                                   onRestart()
```

**Configuration changes** (rotation, locale): default kills + recreates Activity. Override with `android:configChanges="orientation|screenSize"` in manifest — then `onConfigurationChanged()` fires instead. ViewModel survives rotation automatically — use that.

### Activity Lifecycle — Universal Resource-Scoped Lifecycle Bridge

```
RESOURCE-SCOPED LIFECYCLE — CROSS-PLATFORM COMPARISON
════════════════════════════════════════════════════════════════════════════

  Android Activity        iOS UIViewController     ASP.NET Controller        Node.js Express route
  ──────────────────      ─────────────────────    ──────────────────────    ─────────────────────
  onCreate()              init()                   constructor               (route handler called)
  onStart()               viewDidLoad()            (no equiv — stateless)    (no equiv)
  onResume()              viewWillAppear()          before_action filters     middleware chain
  [user interacts]        [visible + interactive]  [handler executes]        [handler executes]
  onPause()               viewWillDisappear()       after_action filters      (response sent)
  onStop()                viewDidDisappear()        Dispose() if IDisposable  (GC)
  onDestroy()             deinit                   (GC)                      (GC)

  Key: Android Activity is stateful (survives orientation via ViewModel);
  web controllers are stateless (new instance per request).
  The "pause/stop" callbacks have no web equivalent.

  Universal pattern across all:
    acquire resources (DB connections, file handles) at start/create
    release resources (unsubscribe, close) at stop/destroy
    Never hold resources across the pause/stop boundary
    Never do slow work in onCreate/init — defer to background
```

### Binder IPC — Universal Typed RPC Bridge

```
TYPED IPC / RPC MECHANISMS — CROSS-PLATFORM COMPARISON
═══════════════════════════════════════════════════════════════════════════════

  Android Binder        Windows COM/DCOM          D-Bus (Linux desktop)      gRPC (any platform)
  ──────────────────    ──────────────────────     ────────────────────────    ──────────────────────
  Kernel driver         COM+ / DCOM via            IPC daemon                  Language-neutral IDL
  (/dev/binder)         NT LPC + RPC runtime       (message daemon)            over HTTP/2 + TLS

  IDL: AIDL             IDL: MIDL / TypeLib        IDL: XML introspection     IDL: Protocol Buffers
  .aidl file → Java/Kt  .idl/.tlb → proxy stubs   D-Bus introspection XML    .proto → generated stubs

  Transport: 1 copy      Transport: LRPC (in-proc)  Transport: Unix socket     Transport: HTTP/2
  (kernel maps one buf)  or TCP/IP for remote        or TCP/IP                  (any network)

  Identity/security:    Identity: SID/token         Identity: Unix uid/gid     Identity: TLS certs /
  uid + selinux label   Access: COM permissions      Access: polkit rules        JWT / mTLS
  (enforced by kernel)  (HKCR\CLSID ACLs)           (user must auth action)

  Async model:          Async: COM apartments        Async: async_call()        Async: streaming RPCs
  oneway (fire-forget)  STA/MTA thread model         (rarely used)              (bidirectional streams)
  synchronous default   (causes UI deadlocks)

  Discovery:            Discovery: CoCreateInstance   Discovery: dbus-send       Discovery: service mesh /
  ServiceManager        HKCR\CLSID\{...} registry     --dest=com.x.y            DNS-SD / Kubernetes SVC
  + AIDL interface name  (in-process: DLL load)

  The universal pattern:
  1. Define interface (AIDL / MIDL / D-Bus XML / .proto)
  2. Generate client proxy + server stub from IDL
  3. Client calls proxy as if local object
  4. Framework serializes call, transports to server, deserializes, invokes
  5. Server returns result; framework serializes back to client

  Binder-specific advantages over generic Unix domain sockets:
    - One kernel copy (vs two for socket: sender→kernel→receiver)
    - Caller UID/PID automatically verified (cannot be spoofed by client)
    - Works with Android's per-app UID security model natively
    - Death notifications: linkToDeath() — know when server process dies
```

### WorkManager — Universal Deferred Job Queue Bridge

```
DEFERRED JOB QUEUE — CROSS-PLATFORM COMPARISON
═══════════════════════════════════════════════════════════════════════════

  Android WorkManager    Linux systemd timer     Python Celery         Java Quartz
  ──────────────────     ───────────────────     ─────────────────     ───────────────────
  OneTimeWorkRequest     .service + .timer       @app.task (async)     @DisallowConcurrent
  PeriodicWorkRequest    OnCalendar / OnUnitActiveSec  beat schedule   CronTrigger

  Guarantee:             Guarantee:              Guarantee:            Guarantee:
  EXACTLY_ONCE on device At-least-once           At-least-once         At-least-once
  (works across reboots  (persistent timer)      (depends on broker)   (JDBC store)
   and app restarts)

  Constraints:           Constraints:            Constraints:          Constraints:
  NetworkType.CONNECTED  After=network.target    (queue routing)       (no built-in)
  requiresCharging()     Requires=power.target   priority routing      (implement in job)
  requiresStorageNotLow()

  Chaining:              No native chaining      Chord, Chain          JobChainingJobDetail
  WorkContinuation       (use ExecStartPre)      (group of subtasks)   Chaining API

  All share the same mental model:
  1. Define work unit with inputs
  2. Attach constraints / schedule
  3. Enqueue to a persistent store
  4. Worker execution engine runs it when constraints met
  5. Results returned via output / callback
```

**Task and back stack:** Activities stack per task. `Intent.FLAG_ACTIVITY_NEW_TASK`, `FLAG_ACTIVITY_CLEAR_TOP`, `FLAG_ACTIVITY_SINGLE_TOP` control stack behavior.

### Fragment — Reusable UI Unit

```kotlin
class MyFragment : Fragment(R.layout.fragment_my) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // view is ready — bind UI here
        // Do NOT start coroutines in onCreate; view may not exist yet
    }

    override fun onDestroyView() {
        super.onDestroyView()
        // view destroyed but fragment instance may survive
        // null out any view references to avoid leaks
    }
}
```

Fragment lifecycle is more complex than Activity — the view lifecycle is separate from the fragment lifecycle. Key rule: collect Flows in `viewLifecycleOwner`, not `this` (fragment).

**FragmentManager back stack:** `addToBackStack("name")` when committing — back button pops it.

### Service — Background Work

```
  ┌─────────────────┬──────────────────────────────────────────┐
  │ Service Type    │ Description                              │
  ├─────────────────┼──────────────────────────────────────────┤
  │ Started         │ startService() / startForegroundService() │
  │                 │ runs until stopSelf() or stopService()   │
  ├─────────────────┼──────────────────────────────────────────┤
  │ Bound           │ bindService() — client/server IPC        │
  │                 │ destroyed when last client unbinds       │
  ├─────────────────┼──────────────────────────────────────────┤
  │ Foreground      │ MUST show persistent notification        │
  │                 │ protected from LMK; required for music,  │
  │                 │ GPS tracking, file download              │
  ├─────────────────┼──────────────────────────────────────────┤
  │ IntentService   │ DEPRECATED — use WorkManager instead     │
  └─────────────────┴──────────────────────────────────────────┘
```

Background execution limits (API 26+): apps in background can't start services freely. Use:
- **WorkManager**: deferrable, guaranteed, battery-friendly
- **ForegroundService**: for user-facing ongoing ops
- **JobScheduler / WorkManager**: for deferred background work

### BroadcastReceiver — System + App Events

```kotlin
// Dynamic registration (in Activity/Fragment)
val receiver = object : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // runs on main thread — do minimal work
        // launch a Service or WorkManager task for real work
    }
}
registerReceiver(receiver, IntentFilter(Intent.ACTION_BATTERY_LOW))
// Must unregister in onStop/onDestroy to avoid leaks

// Static registration in manifest — receives when app is not running
// but most system broadcasts removed from static registration (API 26+)
```

**Ordered broadcasts:** sent to receivers in declared priority order. Each can consume or modify.

### ContentProvider — Structured Data Sharing

```
  App A                              App B
  ┌──────────────────┐               ┌──────────────────────────┐
  │  ContentResolver │               │  ContentProvider         │
  │                  │               │  authority: com.b.data   │
  │  query(          │  Binder IPC   │                          │
  │   content://     │──────────────▶│  query()                 │
  │   com.b.data/    │               │  insert()                │
  │   items/42       │               │  update()                │
  │  )               │◀──────────────│  delete()                │
  └──────────────────┘  Cursor       │  getType() → MIME        │
                                     └──────────────────────────┘
```

Permissions: `android:readPermission` + `android:writePermission` on the `<provider>` element. FileProvider (from Jetpack) is the standard way to share files — maps filesystem paths to `content://` URIs.

### Intent — The Message Bus

```
  Explicit Intent                    Implicit Intent
  ┌────────────────────────────┐    ┌────────────────────────────┐
  │ Intent(this,               │    │ Intent(Intent.ACTION_VIEW) │
  │   DetailActivity::class)   │    │  .setData(Uri.parse(url))  │
  │ startActivity(intent)      │    │ startActivity(intent)      │
  └────────────────────────────┘    └────────────┬───────────────┘
                                                 │
                                    PackageManager resolves via
                                    IntentFilter matching:
                                    - action: VIEW
                                    - category: BROWSABLE
                                    - data scheme: https
                                    → Chrome, Firefox, your custom browser
```

**IntentFilter** in manifest declares what implicit intents a component can handle. Multiple apps can match — user picks (or default set). Critical for deep links: `action=VIEW, category=BROWSABLE, data=scheme/host/path`.

**PendingIntent** — a token representing a future Intent execution with your app's permissions:
```kotlin
// Required for: Notifications, AlarmManager, Widgets
val intent = Intent(context, MyActivity::class.java)
val pending = PendingIntent.getActivity(
    context,
    requestCode,
    intent,
    PendingIntent.FLAG_IMMUTABLE  // required API 31+; use FLAG_MUTABLE only if needed
)
```

---

## AndroidManifest.xml — The App's Contract With the OS

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest
    package="com.example.myapp"
    xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Permissions you need -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />  <!-- dangerous -->
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />  <!-- dangerous -->

    <!-- Apps you intend to interact with (API 30+ package visibility) -->
    <queries>
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
        </intent>
        <package android:name="com.specific.app" />
    </queries>

    <uses-sdk
        android:minSdkVersion="24"
        android:targetSdkVersion="34" />
    <!-- compileSdkVersion goes in build.gradle, not here -->

    <application
        android:name=".MyApplication"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.MyApp">

        <activity
            android:name=".MainActivity"
            android:exported="true"   <!-- required API 31+ if has intent-filter -->
            android:launchMode="singleTop">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <!-- Deep link -->
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="https" android:host="example.com" android:pathPrefix="/app/" />
            </intent-filter>
        </activity>

        <service
            android:name=".DownloadService"
            android:exported="false"
            android:foregroundServiceType="dataSync" />  <!-- required API 34+ -->

        <receiver
            android:name=".BootReceiver"
            android:exported="false">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
            </intent-filter>
        </receiver>

        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="${applicationId}.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>

    </application>
</manifest>
```

**Permission tiers:**

| Tier        | Examples                          | Grant method                        |
|-------------|-----------------------------------|-------------------------------------|
| Normal      | INTERNET, VIBRATE, NFC            | Granted at install, no dialog       |
| Dangerous   | CAMERA, LOCATION, CONTACTS, MIC   | Runtime dialog (API 23+)            |
| Signature   | BIND_ACCESSIBILITY_SERVICE        | Only granted to apps signed with same key |
| Special     | MANAGE_EXTERNAL_STORAGE, OVERLAY  | User navigates to Settings manually |

**Runtime permission pattern (API 23+):**
```kotlin
// In Activity/Fragment — use Activity Result API (not deprecated requestPermissions)
val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { isGranted ->
    if (isGranted) doTheThing()
    else showRationale()
}

// Check before requesting
if (ContextCompat.checkSelfPermission(this, CAMERA) == PERMISSION_GRANTED) {
    doTheThing()
} else {
    requestPermissionLauncher.launch(CAMERA)
}
```

---

## Gradle Build System

```
  project/
  ├── settings.gradle(.kts)       ← project name + module list
  ├── build.gradle(.kts)          ← project-level: classpath deps (AGP, Kotlin plugin)
  ├── gradle/
  │   ├── wrapper/
  │   │   └── gradle-wrapper.properties  ← pin Gradle version
  │   └── libs.versions.toml      ← version catalog (modern)
  ├── app/
  │   └── build.gradle(.kts)      ← module-level: android{} + dependencies
  └── feature-login/
      └── build.gradle(.kts)      ← another module
```

**Module-level build.gradle (Kotlin DSL):**
```kotlin
plugins {
    alias(libs.plugins.android.application)  // com.android.application
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.hilt)
    alias(libs.plugins.ksp)                  // Kotlin Symbol Processing (replaces kapt)
}

android {
    namespace = "com.example.myapp"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 26
        targetSdk = 35
        versionCode = 42
        versionName = "3.1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-debug"
            isDebuggable = true
        }
        release {
            isMinifyEnabled = true        // R8 / ProGuard obfuscation + shrinking
            isShrinkResources = true      // remove unused resources
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            signingConfig = signingConfigs.getByName("release")
        }
    }

    flavorDimensions += "tier"
    productFlavors {
        create("free") { dimension = "tier" }
        create("paid") {
            dimension = "tier"
            applicationIdSuffix = ".paid"
        }
    }
    // Build variants = free-debug, free-release, paid-debug, paid-release

    buildFeatures {
        compose = true
        buildConfig = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = libs.versions.composeCompiler.get()
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.viewmodel.ktx)
    implementation(platform(libs.androidx.compose.bom))  // BOM manages compose versions
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.material3)
    implementation(libs.hilt.android)
    ksp(libs.hilt.compiler)

    // Scope qualifiers:
    // implementation    — available to this module, NOT exposed to modules depending on this
    // api               — available to this module AND exposed to dependents (use sparingly)
    // runtimeOnly       — only at runtime (not compile time) — JDBC drivers, logging impls
    // testImplementation — test source set only
    // androidTestImplementation — instrumented test source set only
    // debugImplementation — debug build type only
}
```

**Version catalog (gradle/libs.versions.toml):**
```toml
[versions]
agp = "8.5.0"
kotlin = "2.0.0"
compose-bom = "2024.09.00"
hilt = "2.51.1"
room = "2.6.1"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "kotlin" }
hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-compiler", version.ref = "hilt" }
androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
```

**Old world bridge:** Gradle is to Android what MSBuild is to .NET. The `.gradle` / `.gradle.kts` files are like `.csproj` files. AGP (Android Gradle Plugin) is the equivalent of the .NET SDK / Microsoft.CSharp.targets. The `libs.versions.toml` catalog is like `Directory.Packages.props` (central package management in .NET).

---

## Jetpack Compose — Modern UI

```
  Traditional Android (Views)          Compose
  ┌───────────────────────────┐        ┌───────────────────────────────┐
  │ XML layout inflation      │        │ @Composable functions         │
  │ View.findViewById()       │        │ State → UI (pure function)    │
  │ Adapter + RecyclerView    │        │ LazyColumn (same concept)     │
  │ ViewHolder pattern        │        │ No XML, no inflation          │
  │ setText(), setVisibility()│        │ Recomposition on state change │
  └───────────────────────────┘        └───────────────────────────────┘
```

**The mental model:** Composable functions are pure functions from state to UI description. When state changes, Compose re-runs only the affected composables (smart recomposition).

```kotlin
@Composable
fun UserCard(
    user: User,
    onFollow: (User) -> Unit,   // events flow UP (state hoisting)
    modifier: Modifier = Modifier
) {
    Card(modifier = modifier.padding(16.dp)) {
        Column {
            Text(text = user.name, style = MaterialTheme.typography.titleMedium)
            Text(text = user.bio)
            Button(onClick = { onFollow(user) }) {
                Text("Follow")
            }
        }
    }
}

// State lives in ViewModel, flows down
@Composable
fun UserListScreen(viewModel: UserViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    when (uiState) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> LazyColumn {
            items(uiState.users, key = { it.id }) { user ->
                UserCard(
                    user = user,
                    onFollow = viewModel::followUser
                )
            }
        }
        is UiState.Error -> Text("Error: ${uiState.message}")
    }
}
```

**State management in Compose:**
```kotlin
// Local UI state — simple, stays in composable
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    Button(onClick = { count++ }) { Text("Count: $count") }
}

// remember: survives recomposition, NOT rotation
// rememberSaveable: survives recomposition AND rotation (uses Bundle)

// Derived state — recomputes only when dependency changes
val expensiveResult by remember {
    derivedStateOf { items.filter { it.isActive }.size }
}
```

**Side effects — running non-UI code from composables:**
```kotlin
// LaunchedEffect: launch a coroutine when key changes
LaunchedEffect(userId) {
    viewModel.loadUser(userId)  // re-runs if userId changes
}

// DisposableEffect: cleanup when leaving composition
DisposableEffect(lifecycle) {
    val observer = LifecycleEventObserver { _, event -> /* ... */ }
    lifecycle.addObserver(observer)
    onDispose { lifecycle.removeObserver(observer) }
}

// rememberCoroutineScope: get scope tied to composition for event handlers
val scope = rememberCoroutineScope()
Button(onClick = { scope.launch { doAsyncWork() } }) { Text("Go") }
```

**Navigation with Compose:**
```kotlin
@Composable
fun AppNavHost(navController: NavHostController) {
    NavHost(navController, startDestination = "home") {
        composable("home") { HomeScreen(navController) }
        composable(
            "detail/{itemId}",
            arguments = listOf(navArgument("itemId") { type = NavType.IntType })
        ) { backStackEntry ->
            val itemId = backStackEntry.arguments?.getInt("itemId") ?: return@composable
            DetailScreen(itemId, navController)
        }
        composable("settings") { SettingsScreen() }
    }
}
```

---

## Architecture: MVVM + Jetpack

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  UI Layer                                                       │
  │  Activity / Fragment / NavHost                                  │
  │      ↑ render UiState         ↓ user events (clicks, inputs)   │
  │  ┌──────────────────────────────────────────────────────────┐   │
  │  │  ViewModel  (survives rotation, scoped to NavBackStack)  │   │
  │  │  val uiState: StateFlow<UiState>                         │   │
  │  │  fun handleIntent(intent: UserIntent)                    │   │
  │  └────────────────────────────┬─────────────────────────────┘   │
  └───────────────────────────────│─────────────────────────────────┘
                                  │ calls
  ┌───────────────────────────────▼─────────────────────────────────┐
  │  Domain Layer (optional)                                        │
  │  Use cases: GetUserProfileUseCase, FollowUserUseCase            │
  │  Pure Kotlin — no Android imports                               │
  └───────────────────────────────┬─────────────────────────────────┘
                                  │ calls
  ┌───────────────────────────────▼─────────────────────────────────┐
  │  Data Layer                                                     │
  │  ┌─────────────────┐      ┌──────────────────────────────────┐  │
  │  │  Repository     │      │  Data Sources                    │  │
  │  │  UserRepository │─────▶│  Room (local DB)                 │  │
  │  │                 │      │  Retrofit (remote API)           │  │
  │  │  single source  │      │  DataStore (preferences)         │  │
  │  │  of truth       │      └──────────────────────────────────┘  │
  │  └─────────────────┘                                            │
  └─────────────────────────────────────────────────────────────────┘
```

**UiState pattern:**
```kotlin
sealed class UserUiState {
    object Loading : UserUiState()
    data class Success(val user: User, val followers: Int) : UserUiState()
    data class Error(val message: String) : UserUiState()
}

class UserViewModel @HiltViewModel constructor(
    private val getUserProfile: GetUserProfileUseCase,
    savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val userId: String = checkNotNull(savedStateHandle["userId"])

    private val _uiState = MutableStateFlow<UserUiState>(UserUiState.Loading)
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            getUserProfile(userId)
                .onSuccess { user -> _uiState.value = UserUiState.Success(user, user.followerCount) }
                .onFailure { e -> _uiState.value = UserUiState.Error(e.message ?: "Unknown error") }
        }
    }
}
```

**Room — the Android ORM:**
```kotlin
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    val name: String,
    val email: String,
    val cachedAt: Long = System.currentTimeMillis()
)

@Dao
interface UserDao {
    @Query("SELECT * FROM users WHERE id = :userId")
    fun getUserById(userId: String): Flow<UserEntity?>  // Flow = reactive query

    @Query("SELECT * FROM users ORDER BY name ASC")
    suspend fun getAllUsers(): List<UserEntity>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: UserEntity)

    @Delete
    suspend fun deleteUser(user: UserEntity)

    @Transaction  // for complex queries involving multiple tables
    @Query("SELECT * FROM users")
    fun getUsersWithPosts(): Flow<List<UserWithPosts>>
}

@Database(
    entities = [UserEntity::class, PostEntity::class],
    version = 3,
    exportSchema = true  // generates schema JSON for migration validation
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao

    companion object {
        val MIGRATION_2_3 = object : Migration(2, 3) {
            override fun migrate(db: SupportSQLiteDatabase) {
                db.execSQL("ALTER TABLE users ADD COLUMN cachedAt INTEGER NOT NULL DEFAULT 0")
            }
        }
    }
}
```

**Hilt — dependency injection:**
```kotlin
// Module providing dependencies
@Module
@InstallIn(SingletonComponent::class)  // scope: entire app lifetime
object NetworkModule {
    @Provides
    @Singleton
    fun provideRetrofit(okHttpClient: OkHttpClient): Retrofit =
        Retrofit.Builder()
            .baseUrl("https://api.example.com/")
            .client(okHttpClient)
            .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
            .build()

    @Provides
    @Singleton
    fun provideUserApi(retrofit: Retrofit): UserApi = retrofit.create(UserApi::class.java)
}

// ViewModel injection
@HiltViewModel
class UserViewModel @Inject constructor(
    private val repository: UserRepository
) : ViewModel()

// Activity/Fragment injection
@AndroidEntryPoint  // required on Activity/Fragment using @Inject
class MainActivity : ComponentActivity() {
    @Inject lateinit var analytics: AnalyticsTracker
}
```

**Old world bridge:** Hilt is Dagger 2 with Android-specific code generation. Compared to .NET DI: Hilt `@InstallIn(SingletonComponent)` ≈ `AddSingleton()`, `@InstallIn(ActivityRetainedComponent)` ≈ `AddScoped()` (scoped to screen). The `@HiltViewModel` annotation is the Android equivalent of constructor injection in ASP.NET controllers.

---

## Kotlin Coroutines — Android Focus

```
  Dispatcher selection:
  ┌─────────────────┬────────────────────────────────────────────────┐
  │ Dispatchers.Main│ UI thread — must use for UI updates           │
  │ Dispatchers.IO  │ Blocking I/O: network, disk, database         │
  │ Dispatchers.Default│ CPU-intensive: sorting, parsing, crypto   │
  │ Dispatchers.Unconfined│ Inherits caller's thread (rarely useful) │
  └─────────────────┴────────────────────────────────────────────────┘

  Scope selection:
  ┌──────────────────────────┬──────────────────────────────────────┐
  │ viewModelScope           │ cancelled when ViewModel cleared     │
  │ lifecycleScope           │ cancelled when lifecycle destroyed   │
  │ rememberCoroutineScope() │ (Compose) cancelled when leaves comp │
  │ GlobalScope              │ AVOID — app lifetime, not cancellable│
  └──────────────────────────┴──────────────────────────────────────┘
```

```kotlin
class MyViewModel(private val repo: UserRepository) : ViewModel() {

    // launch = fire and forget, result not needed
    fun deleteUser(id: String) {
        viewModelScope.launch {
            try {
                repo.deleteUser(id)  // suspend function
                _events.emit(UiEvent.ShowSnackbar("Deleted"))
            } catch (e: IOException) {
                _events.emit(UiEvent.ShowSnackbar("Network error"))
            }
        }
    }

    // async/await = need the result; run in parallel
    fun loadDashboard() {
        viewModelScope.launch {
            val usersDeferred = async(Dispatchers.IO) { repo.getUsers() }
            val statsDeferred = async(Dispatchers.IO) { repo.getStats() }
            val users = usersDeferred.await()
            val stats = statsDeferred.await()
            _uiState.value = DashboardState(users, stats)
        }
    }
}
```

**Flow collection — the critical lifecycle pattern:**
```kotlin
// WRONG — collects even when app is in background (battery drain, crashes)
lifecycleScope.launch {
    viewModel.uiState.collect { state -> render(state) }
}

// CORRECT — suspends collection when lifecycle is STOPPED, resumes on START
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state -> render(state) }
    }
}

// In Compose — collectAsStateWithLifecycle() handles this automatically
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

**Flow types:**
```
  Flow (cold)      — starts executing when collected; unicast
  StateFlow (hot)  — always has value; new collectors get current; replays last value
  SharedFlow (hot) — configurable replay; multicast; no initial value required
  Channel          — one-shot events (navigate, show snackbar); each event consumed once
```

**One-shot events via Channel:**
```kotlin
private val _events = Channel<UiEvent>(Channel.BUFFERED)
val events = _events.receiveAsFlow()  // expose as Flow

// In collector (UI):
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.events.collect { event ->
            when (event) {
                is UiEvent.Navigate -> navController.navigate(event.route)
                is UiEvent.ShowSnackbar -> snackbarHostState.showSnackbar(event.message)
            }
        }
    }
}
```

---

## Android Networking

**Retrofit — the standard HTTP client:**
```kotlin
interface UserApi {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") userId: String): UserDto

    @GET("users")
    suspend fun getUsers(
        @Query("page") page: Int,
        @Query("limit") limit: Int = 20
    ): PagedResponse<UserDto>

    @POST("users")
    suspend fun createUser(@Body request: CreateUserRequest): UserDto

    @PUT("users/{id}")
    suspend fun updateUser(
        @Path("id") id: String,
        @Body request: UpdateUserRequest
    ): UserDto

    @Headers("Cache-Control: no-cache")
    @GET("users/{id}/feed")
    suspend fun getFeed(
        @Path("id") id: String,
        @Header("Authorization") token: String  // per-call override
    ): List<PostDto>
}
```

**OkHttp interceptors:**
```kotlin
val loggingInterceptor = HttpLoggingInterceptor().apply {
    level = if (BuildConfig.DEBUG) BODY else NONE
}

val authInterceptor = Interceptor { chain ->
    val request = chain.request().newBuilder()
        .addHeader("Authorization", "Bearer ${tokenStore.getToken()}")
        .build()
    chain.proceed(request)
}

val okHttpClient = OkHttpClient.Builder()
    .addInterceptor(authInterceptor)
    .addInterceptor(loggingInterceptor)
    .connectTimeout(30, TimeUnit.SECONDS)
    .readTimeout(30, TimeUnit.SECONDS)
    .build()
```

**Serialization — prefer kotlinx.serialization:**
```kotlin
@Serializable
data class UserDto(
    val id: String,
    val name: String,
    @SerialName("email_address") val email: String,  // JSON field name mapping
    val createdAt: String? = null  // nullable with default
)

// Retrofit converter factory:
Json { ignoreUnknownKeys = true }.asConverterFactory("application/json".toMediaType())
```

**Network security config** (`res/xml/network_security_config.xml`):
```xml
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2025-12-31">
            <pin digest="SHA-256">base64encodedPubKeyHash</pin>
            <pin digest="SHA-256">backupPinHash</pin>  <!-- always have backup -->
        </pin-set>
    </domain-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />  <!-- trust user-installed CAs in debug only -->
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

---

## Security on Android

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  Security Layers                                                 │
  │                                                                  │
  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐ │
  │  │  App sandbox   │  │  Permissions   │  │  Android Keystore  │ │
  │  │  (uid per app) │  │  system        │  │  (HW-backed keys)  │ │
  │  └────────────────┘  └────────────────┘  └────────────────────┘ │
  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐ │
  │  │  SELinux       │  │  Biometric     │  │  Play Integrity    │ │
  │  │  (mandatory    │  │  Prompt        │  │  (device attest.)  │ │
  │  │   access ctrl) │  │                │  │                    │ │
  │  └────────────────┘  └────────────────┘  └────────────────────┘ │
  └──────────────────────────────────────────────────────────────────┘
```

**Android Keystore — hardware-backed key storage:**
```kotlin
// Generate a key in the Keystore (never leaves secure hardware)
val keyGenerator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
keyGenerator.init(
    KeyGenParameterSpec.Builder("myKeyAlias", PURPOSE_ENCRYPT or PURPOSE_DECRYPT)
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
        .setUserAuthenticationRequired(true)  // requires biometric/PIN to use key
        .setUserAuthenticationParameters(300, AUTH_BIOMETRIC_STRONG or AUTH_DEVICE_CREDENTIAL)
        .setStrongBoxBacked(true)  // use StrongBox (dedicated security chip) if available
        .build()
)
val secretKey = keyGenerator.generateKey()
// Now use secretKey in a Cipher — key material never accessible to app code
```

**BiometricPrompt:**
```kotlin
val prompt = BiometricPrompt(
    this,
    executor,
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: AuthenticationResult) {
            val cipher = result.cryptoObject?.cipher  // now usable cipher with HW-backed key
            performEncryption(cipher)
        }
        override fun onAuthenticationError(errorCode: Int, errString: CharSequence) { }
        override fun onAuthenticationFailed() { }
    }
)

val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Confirm identity")
    .setAllowedAuthenticators(BIOMETRIC_STRONG or DEVICE_CREDENTIAL)
    .build()

prompt.authenticate(promptInfo, BiometricPrompt.CryptoObject(cipher))
```

**EncryptedSharedPreferences:**
```kotlin
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val encryptedPrefs = EncryptedSharedPreferences.create(
    context,
    "secure_prefs",
    masterKey,
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)
// Use like normal SharedPreferences
encryptedPrefs.edit().putString("auth_token", token).apply()
```

**Play Integrity API** (replaces SafetyNet):
```kotlin
// Request integrity verdict from Play servers
val integrityManager = IntegrityManagerFactory.create(context)
val nonce = generateNonce()  // fresh nonce from your server

integrityManager.requestIntegrityToken(
    IntegrityTokenRequest.builder()
        .setNonce(nonce)
        .build()
).addOnSuccessListener { response ->
    // Send response.token() to YOUR SERVER for verification
    // Server calls Play Integrity API to decode verdict
    // Verdict contains: APP_RECOGNIZED, DEVICE_MEETS_BASIC_INTEGRITY, etc.
    sendToServer(response.token())
}
```

**R8 / ProGuard — obfuscation and shrinking:**
```
  Source code
      │
      ▼  R8 (enabled with isMinifyEnabled = true)
  ┌──────────────────────────────┐
  │  Shrinking: remove unused classes, methods, fields          │
  │  Obfuscation: rename a.b.c → a.b.x (single letters)        │
  │  Optimization: inlining, dead code elimination              │
  └─────────────────────────────┘
      │
      ▼  releases/mapping.txt
  Keep this file — required to decode obfuscated crash stack traces in Play Console
```

**OWASP Mobile Top 10 (relevant to Android):**

| Risk | Android manifestation | Mitigation |
|------|-----------------------|------------|
| M1: Improper Credential Usage | Hardcoded API keys, keys in git | Android Keystore, secrets.properties, never in code |
| M2: Inadequate Supply Chain | Unvetted third-party SDKs | Dependency auditing, Gradle dependency verification |
| M3: Insecure Auth | Missing cert validation, no pinning | Network security config, OkHttp CertificatePinner |
| M4: Insufficient Input/Output | Implicit intents intercepted | Explicit intents for sensitive operations |
| M5: Insecure Communication | Cleartext HTTP | cleartext disabled in network security config |
| M6: Inadequate Privacy Controls | Logging PII, world-readable files | Filter Logcat, use internal storage, EncryptedPreferences |
| M7: Insufficient Binary Protection | Unobfuscated binaries | R8 minification, anti-tamper checks |
| M8: Security Misconfiguration | android:exported=true unnecessarily | Explicit exported declarations, minimal permissions |
| M9: Insecure Data Storage | SQLite unencrypted, external storage | Room + EncryptedSharedPreferences, internal storage |
| M10: Insufficient Cryptography | MD5/SHA1, ECB mode | AES-256-GCM, RSA-OAEP, Android Keystore |

---

## ADB and Android Studio Tooling

**ADB (Android Debug Bridge) — essential commands:**
```bash
# Device management
adb devices                          # list connected devices/emulators
adb -s emulator-5554 shell          # open shell on specific device

# App management
adb install -r app-debug.apk        # -r = replace existing
adb uninstall com.example.myapp
adb shell pm list packages -f       # list installed packages with APK path
adb shell dumpsys package com.example.myapp  # detailed package info

# File operations
adb push localfile.txt /sdcard/Download/
adb pull /sdcard/Download/file.txt ./

# Logcat
adb logcat                           # all logs (overwhelming)
adb logcat -c                        # clear log buffer
adb logcat MyTag:D *:S              # MyTag at Debug, silence everything else
adb logcat -v threadtime *:E        # errors only with thread+time
adb logcat | grep -i "exception"

# Screen
adb shell screencap -p /sdcard/screen.png && adb pull /sdcard/screen.png
adb shell screenrecord /sdcard/demo.mp4

# Network
adb shell settings put global http_proxy 192.168.1.100:8888  # proxy for inspection
adb reverse tcp:8080 tcp:8080       # forward device port to host (local dev server)

# Performance
adb shell dumpsys meminfo com.example.myapp
adb shell top -n 1 | grep myapp

# Input simulation
adb shell input tap 540 960
adb shell input text "hello"
adb shell input keyevent KEYCODE_BACK
```

**Android Studio profilers:**

```
  ┌────────────────────────────────────────────────────────────────┐
  │  Android Studio Profiler (View > Tool Windows > Profiler)      │
  │                                                                │
  │  CPU Profiler                                                  │
  │  ├── System Trace: full-system view (surfaceflinger, binder)   │
  │  ├── Java/Kotlin Method Trace: call tree, flame chart          │
  │  └── Callstack Sample: sampling profiler (lower overhead)      │
  │                                                                │
  │  Memory Profiler                                               │
  │  ├── Heap dump: snapshot of all live objects                   │
  │  ├── Allocation tracking: record all allocations over time     │
  │  └── GC events: visualize GC pressure                         │
  │                                                                │
  │  Network Profiler                                              │
  │  └── HTTP requests: URL, size, timing, payload inspector       │
  │      (requires OkHttp EventListener or Ktor with plugin)       │
  │                                                                │
  │  Energy Profiler                                               │
  │  └── Visualize CPU, network, location wakelock usage           │
  └────────────────────────────────────────────────────────────────┘
```

**App Inspection (separate from Profiler):**
- **Database Inspector**: browse/query live Room/SQLite database while app runs
- **Network Inspector**: HTTP traffic (requires OkHttp 3.12.1+)
- **Background Task Inspector**: WorkManager task graph and status

**Layout Inspector** (Tools > Layout Inspector):
- Live view of composable/view hierarchy
- See applied modifiers and sizes
- Recomposition counts per composable (identify recomposition hotspots)

---

## Distribution

**APK vs AAB:**
```
  APK (Android Package)          AAB (Android App Bundle)
  ┌─────────────────────┐        ┌─────────────────────────────────┐
  │ Single file         │        │ Describes your app              │
  │ All resources for   │        │ Google Play splits and builds   │
  │ all device configs  │        │ optimized APKs per device:      │
  │                     │        │ - Screen density (hdpi/xxhdpi)  │
  │ ~40% larger than    │        │ - CPU architecture (arm64/x86)  │
  │ AAB-derived APK     │        │ - Language (en/de/zh)          │
  │                     │        │                                 │
  │ Use for: sideload,  │        │ Result: 15-40% smaller download │
  │ enterprise internal │        │ Required for new Play apps      │
  └─────────────────────┘        └─────────────────────────────────┘
```

**Signing — the most critical production step:**
```bash
# Create keystore — DO THIS ONCE, BACK UP IMMEDIATELY
keytool -genkey -v \
  -keystore release.jks \
  -keyalg RSA \
  -keysize 4096 \
  -validity 10000 \
  -alias myapp-key

# If you lose your keystore, you CANNOT update your app on the Play Store
# Google Play App Signing solves this: you upload key, Google holds release key
```

**Play App Signing model:**
```
  You                              Google
  ┌────────────────────────┐      ┌─────────────────────────────────┐
  │  Upload key (you hold) │─────▶│  Re-signs with release key      │
  │  Signs your AAB        │      │  (Google holds release key)     │
  │                        │      │                                 │
  │  If upload key lost:   │      │  Users install APK signed with  │
  │  - Request key reset   │      │  Google-managed release key     │
  │    in Play Console     │      │                                 │
  └────────────────────────┘      └─────────────────────────────────┘
```

**Play Console release tracks:**
```
  Internal testing  (up to 100 testers, instant publish, no review)
        │
        ▼
  Closed testing   (alpha, limited testers by email/group)
        │
        ▼
  Open testing     (anyone can opt in, public)
        │
        ▼
  Production       (staged rollout: 1% → 5% → 20% → 100%)
```

**In-app updates (Google Play Core):**
```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

appUpdateManager.appUpdateInfo.addOnSuccessListener { appUpdateInfo ->
    if (appUpdateInfo.updateAvailability() == UPDATE_AVAILABLE) {
        when {
            // Flexible: download in background, user chooses when to apply
            appUpdateInfo.isUpdateTypeAllowed(FLEXIBLE) ->
                appUpdateManager.startUpdateFlowForResult(
                    appUpdateInfo, FLEXIBLE, this, REQUEST_CODE_UPDATE
                )
            // Immediate: full-screen blocking update (for critical security fixes)
            appUpdateInfo.isUpdateTypeAllowed(IMMEDIATE) ->
                appUpdateManager.startUpdateFlowForResult(
                    appUpdateInfo, IMMEDIATE, this, REQUEST_CODE_UPDATE
                )
        }
    }
}
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Which Android API level to target? | minSdk 26 (covers 95%+ devices as of 2024), targetSdk = latest |
| New app: XML Views or Compose? | Compose for all new apps; XML only if large existing View codebase |
| Background work: Service or WorkManager? | WorkManager for deferrable; ForegroundService only for user-facing ongoing ops |
| LiveData or StateFlow? | StateFlow (Kotlin-native, no Android dependency, testable) |
| Kotlin coroutines: launch or async? | launch for fire-and-forget; async when you need the return value |
| Flow collection in Fragment? | repeatOnLifecycle(STARTED) always; collectAsStateWithLifecycle() in Compose |
| DI: Hilt or Koin? | Hilt for new projects (Google-first-party, compile-time validation) |
| JSON parsing: Gson, Moshi, or kotlinx.serialization? | kotlinx.serialization (multiplatform, no reflection, KMP-compatible) |
| Store keys/secrets: SharedPreferences or Keystore? | Keystore for keys, EncryptedSharedPreferences for secrets |
| Distribute: APK or AAB? | Always AAB to Play Store; APK only for sideloading/enterprise |
| Single Activity or Multi-Activity? | Single Activity + Navigation component (standard modern pattern) |
| kapt or KSP? | KSP (faster, Kotlin-native; kapt is deprecated path) |

---

## Common Confusion Points

**minSdk vs targetSdk vs compileSdk — three different things:**
```
  compileSdk: what API level you compile against (access to latest APIs in code)
              → set to latest SDK; never impacts users
  targetSdk:  behavioral compatibility flag (new behaviors opt-in when targetSdk ≥ N)
              → must be ≥ 33 for Play Store requirement (updates annually)
  minSdk:     oldest Android version your app supports (defines your user base)
              → tradeoff: lower minSdk = more users, more compat code needed
```

**ViewModel survives rotation — but not process death:**
```
  Rotation → ViewModel kept, Activity recreated → ViewModel.init() NOT re-run
  Process death (LMK kill) → ViewModel lost → SavedStateHandle needed for critical state
  Back press / finish() → ViewModel cleared → clean up resources in onCleared()
```

**Fragment back stack vs Navigation back stack:**
The FragmentManager has its own back stack. Navigation Component has its own back stack. Do not mix them in the same screen — use one or the other.

**Flow vs Channel for one-shot UI events:**
- StateFlow replay = 1: if user navigates away and returns, they get the last navigation event again → double navigation
- Channel (consumable): each event consumed once → correct for navigation, snackbars
- SharedFlow with replay=0: also works; Channel is simpler

**android:exported is NOT optional since API 31:**
Any Activity/Service/Receiver with an IntentFilter must explicitly declare `android:exported="true"` or `false`. Omitting it crashes the app on API 31+ devices.

**Foreground Service type required since API 34:**
Must declare `android:foregroundServiceType` in manifest and use the typed `startForeground(id, notification, serviceType)` call. Types: `dataSync`, `mediaPlayback`, `location`, `camera`, `microphone`, `health`, `remoteMessaging`.

**ProGuard mapping.txt is a deploy artifact:**
Every release build generates `app/build/outputs/mapping/release/mapping.txt`. Store this with each release. Without it, Play Console crash reports show obfuscated stack traces — unreadable. Treat it like a PDB file in the .NET world.

**BroadcastReceiver.onReceive() runs on main thread with a 10-second timeout:**
Do no blocking work. Start a Service or enqueue WorkManager. If you exceed the time limit: ANR.

**Jetpack Compose recomposition is NOT free:**
`remember {}` prevents expensive recomputation. `key {}` in LazyColumn prevents full list rebind on item change. Profile with Layout Inspector recomposition count. Unstable classes (containing mutable vals, non-Compose-aware lists) cause full recomposition — use `@Stable` or `@Immutable` to hint the compiler.
