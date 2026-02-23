# Session 6 — Operating Systems

**Date**: 2026-02-22
**Directory**: `os/`
**Status**: COMPLETE — 8 files

---

## What Was Built

A full OS developer reference series covering the five major platforms as development targets. Windows is the home base; each other OS is approached as "here's what maps to what you know."

### Files Created

| File | Lines | Core Coverage |
|------|-------|---------------|
| `os/00-OVERVIEW.md` | ~300 | OS genealogy tree (Unix/BSD/Darwin/Linux/NT), kernel architectures (monolithic/hybrid/microkernel), 5 universal abstractions (process/VM/FS/IPC/scheduling) with cross-OS vocabulary, privilege rings (ring 0-3 + VMX + SGX), security models compared, full boot sequences (Windows/Linux/macOS/iOS/Android), cross-OS "same thing" vocabulary table |
| `os/01-CHEATSHEET.md` | ~400 | Universal matrix: Windows/Linux(Ubuntu)/Linux(RHEL)/macOS/iOS/Android × 20 topics; per-OS vocabulary load-in cards (Windows/Linux/macOS/iOS/Android — the "terms to load when switching contexts"); dev environment setup scripts for each platform |
| `os/02-WINDOWS.md` | ~1,926 | NT kernel architecture (HAL/Executive/subsystems), WinForms→WPF→WinUI3→MAUI genealogy with status, MVVM with CommunityToolkit.Mvvm, Windows Service→Worker Service migration, PowerShell (object pipeline, remoting, PS5.1 vs PS7), WSL2 architecture + filesystem caveat, UAC token model + Credential Guard, registry deep dive (hive files, WOW64 redirection, virtualization), ETW + PerfView, networking (WinSock/named pipes/AF_UNIX), WinGet/Choco/Scoop, SDK-style csproj + dotnet CLI |
| `os/03-LINUX.md` | ~1,599 | Linux kernel stack (VFS/scheduler/memory/network), distro families (Debian/RHEL/Arch/Immutable/Azure Linux CBL-Mariner), FHS annotated, systemd unit anatomy + journal + timers + security hardening, containers as Linux primitives (namespaces × 8, cgroups v1/v2, overlayfs), eBPF (bpftrace one-liners, production tools: Cilium/Falco/Tetragon), process management (ps/strace/lsof/ss), bash essentials (set -euo pipefail, loops, functions), permissions + PAM + ACLs, networking (iproute2 suite, nftables, ufw, ssh ProxyJump), storage (LVM, Azure disk tiers), SELinux/AppArmor/auditd/fail2ban |
| `os/04-MACOS.md` | ~1,297 | XNU = Mach + BSD + IOKit (port/message IPC, Mach traps, BSD syscalls), SDK onion (CoreFoundation→Foundation→AppKit/SwiftUI + dyld shared cache), app bundle (.app structure, Info.plist, UTI, URL schemes), launchd domain model (daemon vs agent, kickstart, XPC services), signing pipeline (CSR→cert→entitlements→codesign→notarize→staple→Gatekeeper), APFS (container/volume/firm links/quarantine xattr/SIP), Xcode+Instruments+LLDB, SwiftUI vs AppKit (with WPF bridge), Apple Silicon (P/E cores, Rosetta 2, Universal binary lipo, unified memory Metal) |
| `os/05-IOS.md` | ~1,520 | Xcode build system (targets/schemes/xcconfig/SPM Package.swift), provisioning trust chain (why profiles exist, all 4 profile types, entitlements XML), App Sandbox + privacy (container directories, TCC, 18 privacy strings), UIKit vs SwiftUI (NavigationStack, UIViewRepresentable interop, when UIKit still needed), Swift concurrency (async/await, @MainActor, actor isolation, Sendable), URLSession background transfers, BGTaskScheduler (BGAppRefreshTask/BGProcessingTask), APNs (auth key, payload, Notification Service Extension), TestFlight (internal/external, phased release, dSYM crash symbolication) |
| `os/06-ANDROID.md` | ~1,288 | Android stack (ART AOT+JIT, Zygote fork model, Binder IPC, SurfaceFlinger, Bionic libc), four app components (Activity lifecycle, Fragment, Foreground Service, BroadcastReceiver, ContentProvider, Intent/PendingIntent), AndroidManifest (permissions tiers, queries API 30+, android:exported API 31+), Gradle AGP + version catalog (libs.versions.toml), Jetpack Compose (state, remember/derivedStateOf, side effects, Navigation), MVVM + Jetpack (ViewModel/StateFlow/Room/Hilt scopes/WorkManager), Kotlin coroutines (Dispatchers, repeatOnLifecycle, Flow/StateFlow/Channel), Retrofit + OkHttp + kotlinx.serialization, Android Keystore + BiometricPrompt, ADB 20+ commands, APK/AAB + Play App Signing |
| `os/07-CROSS-PLATFORM.md` | ~1,148 | Abstraction spectrum (native→custom renderer→webview), decision matrix (6 frameworks × 15 attributes), .NET MAUI (handlers replacing renderers, BlazorWebView hybrid, CommunityToolkit.Mvvm), React Native (old bridge vs New Architecture JSI, Expo managed/bare/EAS, React Navigation), Flutter (custom renderer owns pixels, Riverpod AsyncNotifier, platform channels, Dart Isolates), Electron (main/preload/renderer 3-process model, contextBridge security, electron-builder signing, auto-update), Tauri (OS webview, Rust #[tauri::command], Tauri 2.0 mobile), Capacitor (web→native bridge, live OTA updates), code sharing monorepo strategies (Turborepo JS + .NET multi-targeting) |

---

## Key Themes

**The vocabulary load-in** (`01-CHEATSHEET.md`) is the session's anchor — it's the "what do I need to know before I touch this platform" reference. Per-OS vocabulary cards for all 5 platforms.

**Windows as home base** — `02-WINDOWS.md` is the most detailed (nearly 2,000 lines) because the learner knows this platform deeply. It maps old knowledge (WPF → WinUI3, Windows Service → Worker Service, MSBuild → SDK-style) rather than teaching from scratch.

**Linux = containers + servers** — `03-LINUX.md` is oriented toward Azure/server usage. Deep eBPF coverage because that's the future of Kubernetes observability at Microsoft.

**macOS/iOS chain** — `04-MACOS.md` and `05-IOS.md` are tightly linked (same XNU kernel). Signing/entitlements/provisioning explained end-to-end because it's the steepest learning curve for non-Apple developers.

**Android = its own world** — Emphasizes the four-component model (fundamentally different from iOS), Kotlin coroutines (different from Swift async/await despite surface similarity), and Gradle's complexity.

**Cross-platform** — `07-CROSS-PLATFORM.md` is the decision guide. The recommendation for someone with a .NET background is MAUI-first for enterprise, then Flutter for consumer mobile if design consistency matters.

---

## Bridges Used

| Their World | Mapped To |
|-------------|-----------|
| WPF/XAML | WinUI 3 (different XAML dialect), SwiftUI (declarative model) |
| Windows Service + SCM | Worker Service (.NET Generic Host), systemd unit, launchd daemon |
| DPAPI / Windows Credential Manager | macOS Keychain, iOS Keychain, Android Keystore |
| Visual Studio + MSBuild | Xcode, Android Studio, Gradle |
| Registry | Nothing on Linux/macOS — it's files (the key mental shift) |
| IIS/web.config | launchd plist, systemd unit, Kubernetes pod spec |
| .NET async/await | Swift async/await (similar), Kotlin coroutines (different model) |
| NuGet | Swift Package Manager, Gradle deps, CocoaPods/Carthage |
| WinGet | Homebrew (macOS), apt/dnf (Linux) |

---

## Next Session Candidates

- `os/08-EMBEDDED.md` — RTOS (FreeRTOS, Zephyr), bare-metal, device drivers, bootloaders
- More `data-science/` modules (sklearn, PyTorch)
- `os/` additions: ChromeOS, Windows on ARM, server-specific Linux (RHEL deep dive)
