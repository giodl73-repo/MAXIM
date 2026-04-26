# 03 — Linux OS: Developer Reference

## The Big Picture — Linux System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         USERSPACE                                           │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐ │
│  │  systemd     │  │  bash / zsh  │  │  Docker /    │  │  Your App      │ │
│  │  (PID 1)     │  │  (shell)     │  │  containerd  │  │  (Node, Python,│ │
│  │  services,   │  │  scripts,    │  │  (container  │  │  .NET, etc.)   │ │
│  │  timers,     │  │  job ctrl    │  │  runtime)    │  │                │ │
│  │  journald    │  │              │  │              │  │                │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └───────┬────────┘ │
│         │                 │                  │                  │          │
│  ┌──────┴─────────────────┴──────────────────┴──────────────────┴────────┐ │
│  │                    glibc / musl (C standard library)                  │ │
│  │   open(), read(), write(), fork(), mmap(), socket(), ...              │ │
│  │   Wraps raw syscall numbers with portable function calls              │ │
│  └───────────────────────────────────┬───────────────────────────────────┘ │
└──────────────────────────────────────┼──────────────────────────────────────┘
                           SYSCALL BOUNDARY (ring 3 → ring 0)
                    (x86-64: SYSCALL instruction; ARM64: SVC #0)
┌──────────────────────────────────────┼──────────────────────────────────────┐
│                         KERNEL SPACE │                                      │
│                                      ▼                                      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                       LINUX KERNEL (monolithic)                       │  │
│  │                                                                       │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌─────────────────┐ │  │
│  │  │ Scheduler  │  │  Memory    │  │  VFS       │  │  Network Stack  │ │  │
│  │  │            │  │  Manager   │  │ (Virtual   │  │                 │ │  │
│  │  │ CFS        │  │            │  │ Filesystem)│  │  TCP/IP, UDP    │ │  │
│  │  │ real-time  │  │  mmap      │  │            │  │  Netfilter      │ │  │
│  │  │ deadline   │  │  brk/sbrk  │  │  ext4 xfs  │  │  nftables       │ │  │
│  │  │ FIFO/RR    │  │  OOM kill  │  │  btrfs     │  │  eBPF hooks     │ │  │
│  │  │ cgroups    │  │  huge pages│  │  overlayfs │  │  AF_UNIX        │ │  │
│  │  └────────────┘  └────────────┘  │  /proc /sys│  └─────────────────┘ │  │
│  │                                  │  /dev      │                       │  │
│  │  ┌────────────┐  ┌────────────┐  └────────────┘  ┌─────────────────┐ │  │
│  │  │  Namespaces│  │  cgroups   │                  │ Device Drivers  │ │  │
│  │  │  pid net   │  │  v2 unified│                  │                 │ │  │
│  │  │  mnt uts   │  │  hierarchy │                  │  block (disk)   │ │  │
│  │  │  ipc user  │  │  (container│                  │  char (tty)     │ │  │
│  │  │  cgroup    │  │  isolation)│                  │  net (NIC)      │ │  │
│  │  └────────────┘  └────────────┘                   └─────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  ┌──────────────────────────── HARDWARE ─────────────────────────────────┐  │
│  │  CPU + MMU     RAM (DRAM)     NVMe / SSD      NIC          GPU        │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘

Everything is a file:
  /proc/PID/     — process internals exposed as files (no disk I/O)
  /sys/          — kernel object model (devices, drivers) as a live filesystem
  /dev/          — device nodes (read /dev/urandom, write /dev/null)
  Unix sockets   — IPC via filesystem paths (/run/docker.sock)
  pipes          — anonymous files connecting stdout→stdin
```

**The key mental shift from Windows**: There is no registry, no COM object model, no Win32 API surface. Everything — config, hardware access, process info, kernel parameters — is exposed as files in a tree. You read `/proc/sys/net/ipv4/ip_forward` to see a kernel setting; you write `1` to it to enable IP forwarding. This is the "everything is a file" philosophy in practice.

---

## Distro Families — Know Which One You're On

Before you type a single command, you need to know your distro family. Package managers, file paths, init behavior, and default tools differ.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LINUX DISTRO LANDSCAPE                              │
│                                                                             │
│  DEBIAN FAMILY               RHEL FAMILY              ARCH FAMILY           │
│  ─────────────               ───────────              ───────────           │
│  Debian (upstream)           RHEL (Red Hat, $)        Arch Linux            │
│   └─ Ubuntu                   └─ CentOS Stream         └─ Manjaro           │
│       ├─ Ubuntu Server         └─ Rocky Linux           └─ EndeavourOS      │
│       ├─ Ubuntu Desktop        └─ AlmaLinux             └─ Garuda           │
│       └─ Mint, Pop!_OS         └─ Fedora (upstream)    AUR = community pkgs │
│                                └─ Amazon Linux 2023                         │
│  Package: .deb                 └─ Azure Linux (CBL)    Package: pkg.tar.zst │
│  Tool: apt + dpkg             Package: .rpm            Tool: pacman         │
│  Repo: /etc/apt/sources.list  Tool: dnf / yum                               │
│                               Repo: /etc/yum.repos.d/                       │
│                                                                             │
│  IMMUTABLE / CONTAINER-FIRST                                                │
│  ────────────────────────────                                               │
│  Fedora Silverblue   — rpm-ostree atomic updates, Flatpak for apps          │
│  NixOS               — declarative entire system in Nix expressions         │
│  Flatcar             — designed for containers only (runs on AKS nodes)     │
│  Azure Linux         — Microsoft's CBL-Mariner, used for AKS + Azure VMs    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quick ID: What distro am I on?

```bash
cat /etc/os-release          # NAME, VERSION_ID, ID, ID_LIKE
lsb_release -a               # if lsb_release is installed
uname -r                     # kernel version
```

### Distro Key Differences

| Attribute         | Debian/Ubuntu          | RHEL/Rocky/Fedora      | Arch                | Azure Linux         |
|-------------------|------------------------|------------------------|---------------------|---------------------|
| Package format    | .deb                   | .rpm                   | .pkg.tar.zst        | .rpm                |
| Package tool      | apt, dpkg              | dnf (yum alias exists) | pacman              | tdnf (tiny dnf)     |
| Package query     | dpkg -l, dpkg -S       | rpm -qa, rpm -qf       | pacman -Q           | tdnf list           |
| Repo config       | /etc/apt/sources.list  | /etc/yum.repos.d/*.repo| /etc/pacman.conf    | /etc/yum.repos.d/   |
| Default shell     | bash                   | bash                   | bash                | bash                |
| Init system       | systemd                | systemd                | systemd             | systemd             |
| Firewall tool     | ufw (wraps nftables)   | firewalld              | iptables/nftables   | none (use NSG)      |
| SELinux/AppArmor  | AppArmor               | SELinux                | neither (opt-in)    | SELinux             |
| Where used        | Ubuntu VMs, Debian k8s | Enterprise, AWS, AKS   | Desktop, rolling    | AKS nodes, Azure    |

### Essential Package Commands Side-by-Side

```
Task                    apt (Debian/Ubuntu)           dnf (RHEL/Fedora)
────────────────────    ──────────────────────────    ─────────────────────────
Install                 apt install nginx             dnf install nginx
Remove                  apt remove nginx              dnf remove nginx
Remove + config         apt purge nginx               dnf remove nginx (purges)
Update metadata         apt update                    dnf check-update
Upgrade all             apt upgrade                   dnf upgrade
Search                  apt search nginx              dnf search nginx
Show package info       apt show nginx                dnf info nginx
List installed          dpkg -l                       rpm -qa
Which pkg owns file     dpkg -S /usr/bin/nginx        rpm -qf /usr/bin/nginx
List pkg files          dpkg -L nginx                 rpm -ql nginx
Add repo (apt)          add-apt-repository ppa:...    dnf config-manager --add-repo URL
Add repo (manual)       /etc/apt/sources.list.d/      /etc/yum.repos.d/custom.repo
```

---

## Filesystem Hierarchy Standard (FHS)

```
/
├── bin  ─── (symlink → /usr/bin on modern distros)
├── sbin ─── (symlink → /usr/sbin on modern distros)
├── lib  ─── (symlink → /usr/lib on modern distros)
│
├── usr/                   The real programs
│   ├── bin/               All user-runnable binaries: bash, ls, python3
│   ├── sbin/              System admin binaries: sshd, iptables, fdisk
│   ├── lib/               Shared libraries (.so files — Linux's .dll equivalent)
│   ├── lib64/             64-bit libs on mixed systems
│   ├── include/           C header files
│   ├── share/             Architecture-independent data (man pages, locales)
│   └── local/             Admin-installed programs (not managed by package manager)
│       ├── bin/           Your compiled tools, scripts
│       └── lib/
│
├── etc/                   All system configuration — text files, no registry
│   ├── hostname           One line: the machine's hostname
│   ├── hosts              Static DNS overrides (like C:\Windows\System32\drivers\etc\hosts)
│   ├── resolv.conf        DNS server list (may be managed by systemd-resolved)
│   ├── fstab              Filesystem mount table (like Windows disk management, but text)
│   ├── passwd             User accounts (no passwords here — they moved to shadow)
│   ├── shadow             Hashed passwords (root-only readable)
│   ├── group              Group definitions
│   ├── sudoers            sudo rules (edit with visudo — validates before saving)
│   ├── ssh/sshd_config    SSH server config
│   └── systemd/system/    Unit files for locally installed services
│
├── var/                   Variable data — changes at runtime
│   ├── log/               Traditional log files (syslog, auth.log, etc.)
│   ├── spool/             Print queues, mail queues
│   ├── lib/               Persistent app data (databases, package manager state)
│   └── cache/             Cached data (apt downloads, etc.)
│
├── run/                   Runtime data — tmpfs, cleared on boot
│   ├── docker.sock        Docker daemon Unix socket
│   ├── systemd/           systemd runtime state
│   └── *.pid              PID files for running daemons
│
├── proc/                  NOT on disk — kernel exposes process/system info here
│   ├── <PID>/             One directory per running process
│   │   ├── cmdline        Full command line (null-separated)
│   │   ├── environ        Environment variables
│   │   ├── maps           Memory map (VMA layout)
│   │   ├── fd/            Open file descriptors (symlinks to actual files)
│   │   ├── status         Human-readable process status
│   │   └── net/tcp        TCP connections this process has
│   ├── cpuinfo            CPU model, cores, flags
│   ├── meminfo            RAM stats (like Task Manager → Performance)
│   ├── sys/               Kernel parameters (readable/writable — sysctl lives here)
│   │   └── net/ipv4/      e.g., ip_forward, tcp_keepalive_time
│   └── loadavg            1m, 5m, 15m load averages
│
├── sys/                   Kernel device model — sysfs
│   ├── block/             Block devices (disks)
│   ├── bus/               PCI, USB, etc.
│   ├── class/net/         Network interfaces
│   └── fs/cgroup/         cgroup v2 hierarchy (container resource limits)
│
├── dev/                   Device files — I/O to hardware via read/write
│   ├── sda, nvme0n1       Block devices (disks)
│   ├── tty0, pts/0        Terminals
│   ├── null               Discard everything written, return EOF on read
│   ├── zero               Infinite stream of null bytes
│   ├── urandom            Cryptographically secure random bytes
│   └── loop0, loop1       Loop devices (mount disk images as if real disks)
│
├── home/                  User home directories: /home/alice, /home/bob
├── root/                  root user's home (NOT /home/root)
├── tmp/                   Tmpfs — cleared on reboot; world-writable with sticky bit
├── opt/                   Vendor-installed monolithic packages (Oracle, IBM, etc.)
├── srv/                   Data served by this machine (web roots, FTP roots)
└── boot/                  Kernel images, initramfs, GRUB config
```

### File Types (ls -la shows them)

```
-  regular file          (-rwxr-xr-x)
d  directory             (drwxr-xr-x)
l  symbolic link         (lrwxrwxrwx → target)
c  character device      (crw-rw-rw-  /dev/urandom — stream I/O)
b  block device          (brw-rw----  /dev/sda     — seekable I/O)
s  Unix domain socket    (srw-rw-rw-  /run/docker.sock)
p  named pipe (FIFO)     (prw-r--r--  used for inter-process pipe with persistence)
```

---

## systemd — The Full Story

systemd is PID 1. It replaces old-world init scripts (SysV `/etc/init.d/` shell scripts) with declarative unit files. This is analogous to replacing `net start` and batch files with Windows Service Manager + structured service configuration.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     SYSTEMD OBJECT MODEL                                 │
│                                                                          │
│  Unit Types:                                                             │
│  .service   — a daemon process (nginx, sshd, your app)                   │
│  .timer     — scheduled work (replaces cron)                             │
│  .socket    — socket-activated service (starts on first connection)      │
│  .mount     — filesystem mount point                                     │
│  .target    — group of units / runlevel equivalent                       │
│  .path      — watch a filesystem path, start service on change           │
│  .slice     — cgroup hierarchy node for resource limits                  │
│                                                                          │
│  Unit file locations (in priority order, last wins):                     │
│  /usr/lib/systemd/system/    ← package-installed (don't edit)            │
│  /etc/systemd/system/        ← admin overrides — this is yours           │
│  /etc/systemd/system/foo.service.d/override.conf  ← drop-in overrides    │
│  ~/.config/systemd/user/     ← user services (run without root)          │
│                                                                          │
│  Config override pattern (preferred over editing package files):         │
│  systemctl edit nginx    ← creates .d/override.conf automatically        │
└──────────────────────────────────────────────────────────────────────────┘
```

### Service Unit File Anatomy

```ini
# /etc/systemd/system/myapp.service

[Unit]
Description=My Application Server
Documentation=https://myapp.example.com/docs
# Dependencies — start after network and database are up
After=network-online.target postgresql.service
Wants=network-online.target
Requires=postgresql.service        # hard dep — fail if postgres fails

[Service]
# Service type — how systemd knows the process is "ready"
Type=notify                        # process calls sd_notify(READY=1) when ready
# Type=simple   — default; exec'd process IS the service
# Type=forking  — old-school double-fork daemon; systemd waits for parent to exit
# Type=oneshot  — runs and exits; stays "active" until ExecStop
# Type=idle     — like simple but waits until all jobs dispatched

User=myapp                         # run as this user (not root)
Group=myapp
WorkingDirectory=/opt/myapp

# The command to run
ExecStart=/opt/myapp/bin/server --port 8080
ExecStop=/opt/myapp/bin/server --shutdown
ExecReload=/bin/kill -HUP $MAINPID   # SIGHUP = reload config without restart

# Environment
Environment=NODE_ENV=production
EnvironmentFile=/etc/myapp/env       # key=value file; like .env but system-managed
                                     # Windows equivalent: HKLM\SYSTEM\CurrentControlSet\Services\<svc>\Environment

# Restart behavior
Restart=on-failure                   # always | on-failure | on-abnormal | no
RestartSec=5s
StartLimitIntervalSec=60s
StartLimitBurst=3                    # only restart 3 times per 60s

# Resource limits (enforced by cgroups v2)
CPUQuota=50%                         # max 50% of one CPU
MemoryMax=512M                       # OOM kill if exceeded
MemorySwapMax=0                      # no swap
LimitNOFILE=65536                    # open file descriptor limit (ulimit -n)
TasksMax=256                         # max threads/processes (like Win IOCP thread pool limit)

# Security hardening — run this block in production
NoNewPrivileges=yes                  # process cannot gain more privileges via setuid
PrivateTmp=yes                       # gets its own /tmp — other processes can't see it
PrivateNetwork=no                    # set yes to completely isolate from network
ProtectSystem=strict                 # /usr, /boot, /etc read-only
ProtectHome=yes                      # /home and /root inaccessible
ReadWritePaths=/var/lib/myapp        # exception: this path is writable
CapabilityBoundingSet=CAP_NET_BIND_SERVICE  # only allow binding port <1024
AmbientCapabilities=CAP_NET_BIND_SERVICE

[Install]
WantedBy=multi-user.target           # enabled when entering multi-user mode
```

### Essential systemctl Commands

```bash
# Service lifecycle
systemctl start myapp            # start now
systemctl stop myapp             # stop now
systemctl restart myapp          # stop + start
systemctl reload myapp           # send SIGHUP (if ExecReload defined)
systemctl status myapp           # show status + last log lines

# Enable/disable (persistent across boots)
systemctl enable myapp           # create symlink → starts on boot
systemctl disable myapp          # remove symlink
systemctl enable --now myapp     # enable AND start immediately

# Inspection
systemctl list-units --type=service --state=running
systemctl list-units --failed    # what's broken
systemctl list-dependencies myapp
systemctl cat myapp              # show resolved unit file
systemctl show myapp             # all properties (machine-readable)

# Config reload
systemctl daemon-reload          # REQUIRED after editing unit files
systemctl daemon-reexec          # restart systemd itself (rare)

# Targets (runlevels)
systemctl get-default                      # what target boots to
systemctl set-default multi-user.target    # change default
systemctl isolate emergency.target         # drop to emergency shell NOW
```

### Targets (systemd's runlevel equivalent)

```
SysV runlevel → systemd target
────────────────────────────────────────────────────────────
0  (halt)         → poweroff.target
1  (single user)  → rescue.target
3  (multi-user)   → multi-user.target    ← servers live here
5  (graphical)    → graphical.target     ← desktops
6  (reboot)       → reboot.target

Azure VMs and containers boot to multi-user.target.
No display manager. No GUI. That's correct.
```

### journald — Structured Log Storage

journald replaces flat `/var/log/syslog` with a structured binary journal. All stdout/stderr from systemd services goes here automatically — no log4j configuration required.

```bash
# Basic queries
journalctl -u nginx                     # logs for nginx unit
journalctl -u nginx -f                  # follow (like tail -f)
journalctl -u nginx --since "1 hour ago"
journalctl -u nginx --since "2024-01-15 10:00" --until "2024-01-15 11:00"
journalctl -u nginx -n 100              # last 100 lines
journalctl -u nginx -p err              # priority: emerg alert crit err warning notice info debug

# Output formats
journalctl -u nginx -o json-pretty      # structured JSON — pipe to jq
journalctl -u nginx -o cat              # plain message text only

# System-wide
journalctl --since today                # everything today
journalctl -p warning --since today     # warnings and above today
journalctl -k                           # kernel messages (dmesg equivalent)
journalctl --disk-usage                 # how much space the journal uses
journalctl --vacuum-size=500M           # trim to 500MB

# Windows bridge: Event Viewer → journalctl; ETW → systemd journal structured fields
```

### Timer Units (Replace Cron)

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup timer

[Timer]
OnCalendar=daily                    # or: *-*-* 02:30:00 (Cron: 30 2 * * *)
OnCalendar=Mon..Fri 09:00          # weekdays at 9am
OnBootSec=5min                     # run 5min after boot
RandomizedDelaySec=30min           # add jitter (avoids thundering herd on VMs)
Persistent=true                    # run missed timer if machine was off

[Install]
WantedBy=timers.target

# Also create backup.service that does the actual work
# systemctl list-timers --all   ← see all timers + next run time
```

### Boot Performance Analysis

```bash
systemd-analyze                         # total boot time
systemd-analyze blame                   # each unit's startup time, sorted
systemd-analyze critical-chain          # the critical path (what's blocking what)
systemd-analyze plot > boot.svg         # visual timeline (open in browser)

# Windows bridge: Event Viewer → "Diagnostics-Performance" for boot events
# Azure VMs: boot diagnostics blade in portal shows serial console output
```

---

## Containers = Linux Primitives

Docker is not magic. It's a user-friendly wrapper around kernel features that have existed since Linux 3.8. Understanding the primitives explains why Docker runs natively on Linux but needs a VM on Windows/macOS.

```
docker run --rm -p 8080:80 nginx
   │
   ├─► clone() with flags:
   │     CLONE_NEWPID   ─── new PID namespace (container's nginx is PID 1)
   │     CLONE_NEWNET   ─── new network namespace (container gets eth0)
   │     CLONE_NEWNS    ─── new mount namespace (container's own / filesystem)
   │     CLONE_NEWUTS   ─── new UTS namespace (container gets its own hostname)
   │     CLONE_NEWIPC   ─── new IPC namespace (isolated shared memory, semaphores)
   │     CLONE_NEWUSER  ─── user namespace (map container root → unprivileged host uid)
   │     CLONE_NEWCGROUP─── new cgroup namespace
   │
   ├─► cgroup v2:
   │     /sys/fs/cgroup/docker/<container-id>/
   │     cpu.max        = "500000 1000000"  (CPUQuota=50%)
   │     memory.max     = "536870912"       (512MB)
   │     pids.max       = 256
   │
   ├─► overlayfs mount:
   │     Lower layers:  nginx image layers (read-only)
   │     Upper layer:   container-specific changes (read-write)
   │     Work dir:      overlayfs scratch space
   │     Result:        appears to container as normal / filesystem
   │
   ├─► seccomp-bpf filter:
   │     Blocks ~40 dangerous syscalls (mount, kexec_load, ptrace, etc.)
   │     Container cannot load kernel modules or reboot host
   │
   └─► capabilities drop:
         Default: only CAP_NET_BIND_SERVICE and ~14 safe caps remain
         Dropped: CAP_SYS_ADMIN, CAP_NET_ADMIN, CAP_SYS_MODULE, etc.
         --privileged: restore ALL caps (essentially root on host — never in prod)
         --cap-add CAP_NET_BIND_SERVICE: add one specific cap back
```

### Namespaces — What Each Isolates

| Namespace | Flag               | Isolates                                               | Example impact                             |
|-----------|--------------------|--------------------------------------------------------|--------------------------------------------|
| pid       | CLONE_NEWPID       | Process ID numbers                                     | Container's process is PID 1, not 47382   |
| net       | CLONE_NEWNET       | Network interfaces, routing, firewall rules            | Container has its own eth0, 172.17.0.x    |
| mnt       | CLONE_NEWNS        | Filesystem mount points                                | Container sees its image as /             |
| uts       | CLONE_NEWUTS       | Hostname and domain name                               | Container can have hostname "webapp-1"     |
| ipc       | CLONE_NEWIPC       | POSIX message queues, SysV IPC, shared memory          | Container IPC can't reach host IPC        |
| user      | CLONE_NEWUSER      | UID/GID mapping                                        | Container root (uid 0) = host uid 65534   |
| cgroup    | CLONE_NEWCGROUP    | cgroup root                                            | Container can't see host cgroup hierarchy |
| time      | CLONE_NEWTIME      | System clock offsets (Linux 5.6+)                      | Each container can have different clock   |

### cgroups v1 vs v2

```
cgroups v1 (legacy — still present, avoid for new work)
─────────────────────────────────────────────────────
Multiple hierarchies — each resource controller (cpu, memory, blkio)
has its own separate tree. You can attach a process to different
positions in different trees. Powerful, but complex and inconsistent.

/sys/fs/cgroup/memory/docker/<id>/memory.limit_in_bytes
/sys/fs/cgroup/cpu/docker/<id>/cpu.cfs_quota_us
/sys/fs/cgroup/blkio/docker/<id>/blkio.throttle.read_bps_device

cgroups v2 (unified — use this)
─────────────────────────────────────────────────────
Single unified hierarchy. All controllers under one tree.
Consistent semantics. Required for rootless containers.
Enabled by default: Ubuntu 22.04+, Fedora 31+, RHEL 9+, AKS 1.25+

/sys/fs/cgroup/docker/<id>/
  memory.max        (hard limit — OOM kill)
  memory.high       (soft limit — throttle before kill)
  cpu.max           (quota/period format: "500000 1000000" = 50%)
  io.max            (IOPS and bandwidth limits per device)
  pids.max          (process/thread count limit)

Check which you have:
  stat -fc %T /sys/fs/cgroup/   # "tmpfs" = v1, "cgroup2fs" = v2
```

### overlayfs — How Image Layers Work

```
Image on disk:               What container sees:
─────────────                ────────────────────
Layer 3 (your app)           /app/server.js       ← from layer 3 (upper)
Layer 2 (node_modules)       /app/node_modules/   ← from layer 2
Layer 1 (node:20 base)       /usr/local/bin/node  ← from layer 1
Layer 0 (debian base)        /bin/bash            ← from layer 0

Container writes /etc/hosts  → goes into ephemeral upper layer (lost on container exit)
Container writes /data/db    → if /data is a volume mount, goes to host filesystem

This is why:
  - docker pull is fast (reuse layers)
  - "container is read-only" advice — mutations lost on container stop
  - volumes exist — to persist data across container restarts
```

---

## eBPF — The Modern Linux Superpower

eBPF (extended Berkeley Packet Filter) lets you run sandboxed programs inside the kernel, triggered by events — without loading a kernel module, without rebooting, without risking a kernel panic.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         eBPF ARCHITECTURE                                │
│                                                                          │
│  Your tool (bpftrace script, Cilium, Falco)                              │
│       │                                                                  │
│       ▼                                                                  │
│  BPF bytecode  ──► Verifier (safety check: no loops, bounded mem access) │
│       │                                                                  │
│       ▼                                                                  │
│  JIT compiler  ──► native CPU instructions                               │
│       │                                                                  │
│       ▼                                                                  │
│  Attached to hook:                                                       │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐           │
│  │  kprobe      │  tracepoint  │  XDP         │  tc (traffic │          │
│  │  (kernel fn  │  (kernel     │  (earliest   │  control)    │          │
│  │  entry/exit) │  static pts) │  network     │  (ingress/   │          │
│  │              │              │  hook)       │  egress)     │          │
│  │  uprobe      │  USDT        │  socket      │  cgroup sock │          │
│  │  (user fn)   │  (user-space │  filter      │  (per cgroup │          │
│  │              │  tracepoints)│              │  filtering)  │          │
│  └──────────────┴──────────────┴──────────────┴──────────────┘          │
│       │                                                                   │
│       ▼                                                                   │
│  BPF Maps (shared memory between kernel BPF prog and user-space tool)    │
│  hash, array, ringbuf, lpm_trie, perf_event_array, ...                   │
└──────────────────────────────────────────────────────────────────────────┘
```

### eBPF Use Cases — What's Using It Right Now in Azure/Kubernetes

| Tool       | What it does                                              | Layer          |
|------------|-----------------------------------------------------------|----------------|
| Cilium     | eBPF-based CNI for Kubernetes; replaces iptables routing  | K8s networking |
| Pixie      | Zero-instrumentation app observability (HTTP, SQL traces) | Observability  |
| Falco      | Runtime security; alerts on unexpected syscalls           | Security       |
| Tetragon   | Network + process execution policy enforcement in K8s     | Security       |
| bpftrace   | Dynamic tracing scripts (production debugging)            | Dev tooling    |
| Hubble     | Network flow visibility built on Cilium                   | Networking     |

**Azure-specific**: AKS with Azure CNI Powered by Cilium uses eBPF for all network policy enforcement, replacing the iptables rules that traditional kube-proxy generates. This is why large-scale AKS clusters don't hit iptables rule limits.

### bpftrace One-Liners

```bash
# Trace all syscalls made by a specific PID
bpftrace -e 'tracepoint:raw_syscalls:sys_enter /pid == 12345/ { printf("%s\n", comm); }'

# Profile CPU — which functions are hot?
bpftrace -e 'profile:hz:99 { @[kstack] = count(); }'

# Trace file opens system-wide
bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'

# Trace TCP connections being established
bpftrace -e 'kprobe:tcp_connect { printf("connect: %s\n", comm); }'

# Count syscalls by process name
bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'

# Trace slow disk I/O (>1ms)
bpftrace -e 'kprobe:blk_account_io_start { @start[arg0] = nsecs; }
             kprobe:blk_account_io_done /@start[arg0]/
             { $lat = (nsecs - @start[arg0]) / 1000; if ($lat > 1000) { printf("%d us\n", $lat); } }'
```

### bcc Tools (Higher-Level eBPF)

```bash
# Requires: apt install bpfcc-tools  OR  dnf install bcc-tools
execsnoop-bpfcc       # trace new process executions (which programs are spawning?)
opensnoop-bpfcc       # trace file opens
tcplife-bpfcc         # TCP connection lifespan + bytes
tcptop-bpfcc          # top TCP connections by bandwidth
runqlat-bpfcc         # scheduler latency (how long processes wait for CPU)
offcputime-bpfcc      # where processes are sleeping/blocked
```

---

## Process Management

### Seeing What's Running

```bash
# Static snapshot
ps aux              # BSD syntax: a=all users, u=user-oriented format, x=no-tty filter
ps -ef              # SysV syntax: -e=all, -f=full format; shows PPID (parent PID)
ps -eo pid,ppid,user,%cpu,%mem,vsz,rss,comm   # custom columns

# Column meanings (ps aux):
# USER  PID  %CPU  %MEM   VSZ    RSS   TTY   STAT  START  TIME  COMMAND
# root    1   0.0   0.3  168292  9744  ?     Ss   Jan15   0:03  /sbin/init
#
# VSZ = virtual size (all mapped memory, including not-yet-loaded)
# RSS = resident set size (actually in RAM right now)
# STAT: S=sleeping, R=running, Z=zombie, T=stopped, D=uninterruptible wait
#       s=session leader, l=multi-threaded, +=foreground

# Interactive
top           # built-in, always present
htop          # better UI, tree view, color; apt install htop
btop          # best UI, shows containers; apt install btop

# Load average (in top/htop header and uptime command):
# "load average: 0.52, 1.23, 0.89" = 1min, 5min, 15min
# On a 4-CPU machine: load < 4.0 means not overloaded
# CPU steal % in VMs = time your VM WANTED the CPU but hypervisor gave it to another VM
# High steal on Azure = neighboring tenant contention; upgrade to dedicated instances
```

### Finding and Signaling Processes

```bash
# Find by name
pgrep nginx                     # returns PIDs
pgrep -l nginx                  # PIDs + names
pgrep -a nginx                  # PIDs + full command line
pidof nginx                     # returns PIDs (simpler, exact name match)

# Kill
kill 12345                      # send SIGTERM (15) — graceful shutdown request
kill -9 12345                   # send SIGKILL — unblockable immediate kill
kill -HUP 12345                 # SIGHUP — reload config (nginx, sshd respond to this)
kill -USR1 12345                # SIGUSR1 — app-defined (nginx: reopen logs)
killall nginx                   # kill by name
pkill -f "python worker.py"     # kill by full command match (-f = full command)

# Signal reference:
# SIGTERM (15) — please shut down gracefully       → handle in app
# SIGKILL  (9) — forced immediate kill             → cannot be caught/ignored
# SIGHUP   (1) — terminal hangup / reload config   → nginx reloads on HUP
# SIGINT   (2) — Ctrl+C                            → handle in app
# SIGQUIT  (3) — Ctrl+\ (core dump)
# SIGUSR1/2    — application-defined
# SIGSTOP     — pause process (Ctrl+Z sends SIGTSTP, similar)
```

### Inspecting a Process via /proc

```bash
PID=12345

cat /proc/$PID/cmdline | tr '\0' ' '   # full command line (null-separated → space)
cat /proc/$PID/environ | tr '\0' '\n'  # environment variables
cat /proc/$PID/status                  # human-readable status (VmRSS, VmSize, threads)
ls -la /proc/$PID/fd/                  # open file descriptors → symlinks to files
cat /proc/$PID/maps                    # virtual memory map (all mapped regions)
cat /proc/$PID/net/tcp                 # TCP connections (hex-encoded)

# More convenient tools:
lsof -p $PID                   # all open files for PID
lsof -i :8080                  # what process is listening on port 8080
ss -tlnp                       # all listening TCP sockets with PIDs (preferred over netstat)
ss -tulnp                      # TCP + UDP listening
ss -s                          # summary statistics

# Trace syscalls of running process (like Process Monitor on Windows)
strace -p $PID                 # attach and stream syscalls
strace -p $PID -e trace=network  # only network syscalls
strace -p $PID -c              # count syscalls, show stats on exit
strace -tt -p $PID             # with timestamps
```

### Keep Processes Running After Logout

```bash
# nohup — ignore SIGHUP (sent when terminal closes)
nohup ./server.sh > server.log 2>&1 &   # run in background, output to file

# screen — terminal multiplexer (older, always installed)
screen                          # start new session
screen -S mysession             # named session
Ctrl+A, D                       # detach (leave running)
screen -r mysession             # reattach
screen -ls                      # list sessions

# tmux — modern screen replacement (preferred)
tmux new -s mysession           # new named session
Ctrl+B, D                       # detach
tmux attach -t mysession        # reattach
tmux ls                         # list sessions
tmux new-window                 # Ctrl+B, C — new window
tmux split-pane                 # Ctrl+B, %  — vertical split

# On Azure VMs, use tmux. screen is fine too.
# Both persist across SSH disconnections.
```

---

## Shell — bash/zsh Essentials

### Object Pipeline vs Text Pipeline — The Fundamental Mental Shift

```
POWERSHELL (OBJECT PIPELINE)            BASH (TEXT PIPELINE)
════════════════════════════            ════════════════════

  Every value is a typed .NET object.   Every value is a string (bytes).
  Cmdlets receive + emit objects.        Commands produce text; tools parse it.

  Get-Process |                          ps aux |
    Where-Object { $_.CPU -gt 10 } |       awk '$3 > 10' |
    Sort-Object CPU -Descending |          sort -t' ' -k3 -rn |
    Select-Object -First 5 |              head -5 |
    Format-Table Name, CPU, WorkingSet    awk '{print $11, $3, $6}'

  Filtering:  $_.PropertyName            Filtering: field position or regex
  .CPU is a float — comparison is typed  $3 is a string — must know the column
  Type error if property doesn't exist   No error — wrong column = wrong output

  Composition:  $result = Get-X | Where  Composition: result=$(cmd | grep | awk)
    $result is still a typed collection    $result is a string (newline-separated)

  Structured output always available:   Structure is by convention:
    ConvertTo-Json / ConvertTo-Csv         ps, ls, netstat output format varies
    Select-Object produces new objects     jq parses JSON; awk parses columns

  Error handling:                        Error handling:
    $ErrorActionPreference = "Stop"        set -e  (exit on error)
    try/catch works as expected            pipefail: bash -o pipefail
    $LASTEXITCODE for native commands      $? = exit code of last command

  Cross-OS note:                         Shell portability:
    pwsh (PowerShell 7+) runs on Linux/    bash ≠ sh ≠ zsh ≠ dash
    macOS — identical behavior             #!/bin/sh runs dash on Ubuntu
    PS objects work identically            Many bash features absent in sh
```

**The practical shift:** In PowerShell, you query objects: `$proc.CPU`. In bash, you parse text: `awk '{print $3}'`. When you move from PS to bash, you're trading type safety for composability with any text-producing tool. The gain: every command that produces output is automatically pipeable. The cost: you're always parsing, and column positions change between OS versions, distros, and flags.

**Defensive bash patterns (peer-level):**

```bash
#!/usr/bin/env bash
set -euo pipefail               # e=exit on error, u=error on unset var, o pipefail=pipe errors

# trap: cleanup on exit (like C# using/finally for shell)
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT    # runs on normal exit, signal, or error

# $(...) vs backticks: $(...) is nestable; backticks are not
result=$(echo $(date +%Y))      # nested — works fine
# result=`echo `date +%Y``     # backtick nested form — BROKEN

# [[ vs [: prefer [[; it handles spaces in vars, no word splitting, regex support
[[ -f "$path" ]]                # safe even if $path contains spaces
[[ "$str" =~ ^[0-9]+$ ]]       # regex match — only in [[

# Quoting: always quote $variables unless you want word splitting + glob expansion
files=$(ls *.txt)               # WRONG: breaks on spaces in filenames
files=( *.txt )                 # RIGHT: array glob expansion
for f in "${files[@]}"; do      # iterate array safely
    process "$f"
done

# Exit code vs output: separate concerns
if output=$(some_command 2>&1); then   # capture stdout+stderr, check exit code
    echo "success: $output"
else
    echo "failed: $output" >&2
    exit 1
fi
```

### Redirects and Pipes

```bash
# File descriptors: 0=stdin, 1=stdout, 2=stderr
command > file          # redirect stdout to file (overwrite)
command >> file         # redirect stdout to file (append)
command 2> err.log      # redirect stderr to file
command 2>&1            # redirect stderr to same place as stdout
command > out.log 2>&1  # both stdout and stderr to file
command &> out.log      # shorthand for above (bash 4+)
command > /dev/null     # discard stdout
command > /dev/null 2>&1  # discard everything

# Pipes
cmd1 | cmd2             # stdout of cmd1 → stdin of cmd2
cmd1 | tee file | cmd2  # stdout to both file AND cmd2

# Process substitution — treat command output as a file
diff <(sort file1) <(sort file2)    # diff sorted versions without temp files
cat <(ls /etc) <(ls /var)           # concatenate two command outputs
command > >(tee file1) 2> >(tee file2)  # split stdout and stderr to different places
```

### Job Control

```bash
command &               # start in background
Ctrl+Z                  # suspend foreground job (SIGTSTP)
Ctrl+C                  # kill foreground job (SIGINT)
Ctrl+D                  # send EOF to stdin (closes shell if at prompt)
jobs                    # list background/suspended jobs
fg %1                   # bring job 1 to foreground
bg %1                   # resume suspended job in background
wait                    # wait for all background jobs to finish
wait $!                 # wait for last backgrounded PID
disown %1               # detach job from shell (won't be killed when shell exits)
```

### Variables, Arrays, Arithmetic

```bash
# Variables — no spaces around =
NAME="Alice"
echo "$NAME"            # always quote variables to handle spaces
echo "${NAME}s"         # use braces when concatenating

# Default values
echo "${VAR:-default}"  # use "default" if VAR is unset or empty
echo "${VAR:=default}"  # set VAR to "default" if unset
echo "${VAR:?error}"    # error and exit if VAR is unset

# String manipulation
echo "${NAME,,}"        # lowercase (bash 4+)
echo "${NAME^^}"        # uppercase
echo "${NAME:0:3}"      # substring: offset 0, length 3
echo "${NAME#prefix}"   # strip shortest prefix match
echo "${NAME##*/}"      # strip longest prefix (get filename from path)
echo "${NAME%suffix}"   # strip shortest suffix match
echo "${NAME%.*}"       # strip extension

# Arrays
arr=(one two three)
echo "${arr[0]}"        # first element
echo "${arr[@]}"        # all elements
echo "${#arr[@]}"       # array length
arr+=("four")           # append

# Arithmetic
echo $((2 + 2))
echo $(( i++ ))
let "x = 5 * 3"
result=$(( (a + b) * c ))
```

### Conditionals

```bash
# [[ ]] is bash's extended test — prefer over [ ] (no word splitting, no glob)
[[ -f "$path" ]]        # is a regular file
[[ -d "$path" ]]        # is a directory
[[ -e "$path" ]]        # exists (any type)
[[ -r "$path" ]]        # readable
[[ -x "$path" ]]        # executable
[[ -z "$var" ]]         # string is empty
[[ -n "$var" ]]         # string is non-empty
[[ "$a" == "$b" ]]      # string equality
[[ "$a" != "$b" ]]      # string inequality
[[ "$a" =~ ^[0-9]+$ ]] # regex match (bash 3.2+)
[[ $n -eq 5 ]]          # numeric equality
[[ $n -lt 10 ]]         # numeric less than
[[ $n -ge 1 ]]          # numeric greater-or-equal
[[ -f "$f" && -r "$f" ]]  # AND
[[ -z "$a" || -z "$b" ]]  # OR

if [[ -f "$config" ]]; then
    echo "config exists"
elif [[ -d "$config" ]]; then
    echo "config is a directory"
else
    echo "config not found"
fi
```

### Loops

```bash
# For each file matching glob
for f in /var/log/*.log; do
    echo "Processing $f"
    gzip "$f"
done

# For each line of a file (correct handling of spaces)
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/hosts

# For each line of command output
while IFS= read -r pid; do
    echo "Killing $pid"
    kill "$pid"
done < <(pgrep -f "old_process")

# C-style numeric loop
for ((i=0; i<10; i++)); do
    echo "$i"
done

# Loop over array
for item in "${arr[@]}"; do
    echo "$item"
done
```

### Functions

```bash
# Define
my_function() {
    local arg1="$1"           # local = scoped to function (critical: prevents leaking)
    local arg2="${2:-default}" # with default
    echo "Got: $arg1 and $arg2"
    return 0                  # 0 = success; non-zero = failure (convention)
}

# Call
my_function "hello" "world"
result=$(my_function "hello")   # capture output

# Check return code
if ! my_function "arg"; then
    echo "function failed" >&2
    exit 1
fi
```

### Production Script Header

```bash
#!/usr/bin/env bash
# #!/usr/bin/env bash = find bash on PATH (portable across distros)
# #!/bin/bash         = hardcoded path (fine if you know your environment)

set -e          # exit immediately on any command failure (like throw-on-error)
set -u          # treat unset variables as errors (catches typos)
set -o pipefail # catch failures in pipelines (cmd1 | cmd2 fails if cmd1 fails)
# Combined idiom:
set -euo pipefail

# Trap for cleanup on exit
cleanup() {
    rm -f "$tmpfile"
    echo "Cleaned up"
}
trap cleanup EXIT     # runs on any exit (normal, error, signal)
trap cleanup INT TERM # also on Ctrl+C and SIGTERM

tmpfile=$(mktemp)     # /tmp/tmp.XXXXXXXXXX — safe temp file
```

### Shell Init Files — Which Runs When

```
Login shell (ssh login, su -, sudo -i):
  /etc/profile       ← system-wide; sources /etc/profile.d/*.sh
  ~/.bash_profile    ← user; if not found, tries ~/.bash_login, then ~/.profile

Interactive non-login shell (new terminal in GUI, bash in bash):
  /etc/bash.bashrc   ← system-wide interactive config
  ~/.bashrc          ← user interactive config

Non-interactive shell (shell scripts, cron jobs):
  Nothing sourced by default
  $BASH_ENV          ← if set, this file is sourced

Practical rule:
  Put PATH changes and exports → ~/.bash_profile (runs on SSH login)
  Put aliases and functions    → ~/.bashrc (runs in interactive shells)
  Source ~/.bashrc from ~/.bash_profile to get both in login shells:
    [[ -f ~/.bashrc ]] && source ~/.bashrc
```

---

## Permissions and Users

### Permission Model Comparison — Windows vs Linux vs macOS

```
PERMISSION MODELS AT A GLANCE
═══════════════════════════════════════════════════════════════════════

  Layer            Windows (NTFS)              Linux POSIX            Linux Extended (optional)
  ──────────       ────────────────────────    ──────────────────     ─────────────────────────
  DAC model        Full ACL: per-user/group    3-bucket: owner/       POSIX ACL (getfacl/setfacl)
                   allow AND deny ACEs         group/other            Adds per-user entries but
                   Any SID can get an ACE      No deny entries in     still no audit entries
                   in DACL                     standard POSIX
  Deny ACEs        Yes — explicit deny wins    No — cannot deny a     ACL mask concept only
                   over allow for same SID     specific user          (no explicit deny)
  Audit entries    SACL — separate from DACL   auditd rules on        auditd + inotify
                   Each ACE is audited         file path              (separate from permissions)
  Inherit          Yes — directory ACEs        umask applies to       setfacl --default
                   propagate to children       new files; no          sets default ACEs
                   (with propagation flags)    per-entry inherit      for new files in dir
  Identity         SID (binary, stable across  uid/gid (integer,      uid/gid + name lookup
                   renames + moves)            per-machine unless     via LDAP/SSSD)
                                               LDAP/AD)
  Check on open    Full access check at open   Owner check at open    Same as POSIX
  (not on read)    against token + DACL        (rwx vs uid/gid)
  Elevation path   UAC → new elevated token    setuid bit / sudo      same
  Mandatory        Integrity Levels            SELinux / AppArmor     (MAC, separate layer)
  (MAC)            (Low/Med/High/System)       (optional)

Key gap: Linux POSIX has no per-user deny. If alice is in a group that
has read access, you cannot deny alice specifically in POSIX mode.
You need POSIX ACLs (setfacl) or SELinux policy for that.
```

### Linux Capabilities — Fine-Grained root Powers

```
CAPABILITIES VS WINDOWS PRIVILEGES
════════════════════════════════════

  Universal concept: instead of all-or-nothing root, split privileges
  into capabilities (Linux) / privileges (Windows) that can be granted individually.

  Key Linux capabilities:
    CAP_NET_BIND_SERVICE  Bind to ports < 1024 without root
                          Windows equiv: SeNetworkLogonRight (network logon)
    CAP_NET_ADMIN         Configure network interfaces, routes, iptables
    CAP_SYS_ADMIN         Broad admin: mount, chroot, ptrace, many more
                          (often the "catch-all" — avoid if possible)
    CAP_SYS_PTRACE        Trace other processes (strace, gdb attach)
                          Windows equiv: SeDebugPrivilege
    CAP_DAC_OVERRIDE      Bypass file read/write/execute permission checks
    CAP_DAC_READ_SEARCH   Bypass file read + dir execute checks
    CAP_SETUID/SETGID     Set arbitrary UID/GID (used by container runtimes)
    CAP_KILL              Send signals to any process
    CAP_NET_RAW           Raw socket access (ping, tcpdump, ARP spoof)

  Managing capabilities on binaries:
    getcap /usr/bin/ping                    # see what caps a binary has
    setcap cap_net_raw+ep /usr/bin/ping     # grant raw socket cap (no setuid needed)
    setcap -r /usr/bin/ping                 # revoke
    capsh --print                           # current process capabilities

  Container implications:
    docker run --cap-drop ALL --cap-add NET_BIND_SERVICE ...  # minimal caps
    Kubernetes securityContext.capabilities.drop/add
    Never run containers with CAP_SYS_ADMIN unless truly necessary

  MAC layers (orthogonal to capabilities + POSIX):
    SELinux: labels on every file + process; policy governs what label X can do to label Y
             enforcing mode = blocks + logs; permissive = logs only
             Equivalent mental model: Windows Mandatory Integrity + AppLocker combined
    AppArmor: path-based profiles per executable
              simpler than SELinux; less fine-grained
              Ubuntu/Debian default; Chrome sandbox uses AppArmor profiles
    Precedence: MAC is checked AFTER DAC — a process needs both DAC and MAC permission
```

### The Permission Model

```
ls -la /etc/shadow
-rw-r----- 1 root shadow 1234 Jan 15 10:00 /etc/shadow
│├┤├┤├┤    │ │    │
││ │ │ │   │ │    └── group name
││ │ │ └── other: --- (no permissions)
││ │ └──── group: r-- (read only)
││ └────── owner: rw- (read + write)
│└──────── file type: - = regular file
└───────── (just the dash at position 0)

Permission bits: r=4, w=2, x=1
chmod 755 = rwxr-xr-x = owner:7 group:5 other:5
chmod 644 = rw-r--r-- = standard for config files
chmod 600 = rw------- = SSH private keys (MUST be this)
chmod 777 = rwxrwxrwx = never in production

chmod u+x script.sh     # add execute for owner (symbolic)
chmod go-w file         # remove write for group and other
chown alice:devs file   # change owner AND group
chown alice file        # change owner only
chgrp devs file         # change group only
chown -R alice /var/app # recursive
```

### Special Bits

```
setuid (chmod u+s, 4xxx): executable runs as file OWNER regardless of who executes
  /usr/bin/passwd  = setuid root — allows any user to change their own password
  rws in owner execute bit: rwsr-xr-x
  Security risk: attackers look for misconfigured setuid binaries

setgid (chmod g+s, 2xxx): executable runs as file GROUP; on directory = new files inherit group
  Useful: shared project directory where all files should belong to same group
  rws in group execute bit

sticky bit (chmod +t, 1xxx): on directory, only file owner/root can delete
  /tmp: drwxrwxrwt — world-writable but you can only delete YOUR files
  t in other execute bit

find / -perm -4000 -type f 2>/dev/null   # find all setuid binaries (security audit)
```

### sudo

```bash
# sudo — run as another user (default: root)
sudo command              # run as root
sudo -u alice command     # run as alice
sudo -i                   # interactive root login shell (sources /root/.bash_profile)
sudo -s                   # root shell, keep current environment
sudo -l                   # list what you can sudo

# /etc/sudoers — edit ONLY with visudo (validates syntax before saving)
# Syntax: WHO WHERE = (AS_WHOM) WHAT

# User rules
alice ALL=(ALL) ALL               # alice can run anything as anyone from anywhere
bob   ALL=(ALL) NOPASSWD: ALL     # bob: no password prompt (common in automation)

# Command-specific
deploy ALL=(root) /usr/bin/systemctl restart myapp   # can only restart this service
ops    ALL=(root) /usr/bin/journalctl                # read-only log access

# Group rules (%group syntax)
%wheel  ALL=(ALL) ALL             # RHEL convention: wheel group = admin
%sudo   ALL=(ALL:ALL) ALL         # Ubuntu convention: sudo group = admin

# Drop-in files (preferred — don't edit /etc/sudoers directly)
/etc/sudoers.d/deploy-user        # one file per purpose
```

### sudo vs su variants

```
su -           → switch to root with full login shell (reads /root/.bash_profile)
su alice       → switch to alice, keep current environment (not recommended)
su - alice     → switch to alice with full login shell
sudo -i        → root login shell via sudo (respects sudoers, logged)
sudo -s        → root shell, keep your environment, no login files
sudo su -      → same as sudo -i but calls su explicitly (legacy habit)

Prefer sudo -i over su - on modern systems. sudo is logged; su is not.
```

### PAM (Pluggable Authentication Modules)

PAM is where password checking, 2FA, LDAP auth, and limits plug in. You don't interact with it directly often, but it explains why changing the PAM stack can enable LDAP auth, TOTP, etc.

```
/etc/pam.d/sshd         ← PAM stack for SSH authentication
/etc/pam.d/sudo         ← PAM stack for sudo
/etc/pam.d/login        ← PAM stack for console login
/etc/pam.d/common-auth  ← Debian: shared auth rules
/etc/pam.d/system-auth  ← RHEL: shared auth rules

Modules:
pam_unix.so       — standard Unix password check (/etc/shadow)
pam_ldap.so       — LDAP/Active Directory (Azure AD → pam_aad or sssd)
pam_google_authenticator.so  — TOTP (Google Authenticator)
pam_limits.so     — enforce limits from /etc/security/limits.conf
pam_env.so        — set environment from /etc/security/pam_env.conf
pam_sss.so        — System Security Services Daemon (SSSD for AD integration)

Azure AD Join → use sssd + realm join for on-prem AD;
Azure AD SSH extension for Azure VMs → installs pam_aad
```

### ACLs — Beyond owner/group/other

```bash
# Standard chmod only has owner, group, other — ACLs add per-user/per-group entries
getfacl /var/www/html           # show current ACLs
setfacl -m u:alice:rw file.txt  # give alice read+write
setfacl -m g:devs:r- file.txt   # give devs group read
setfacl -m o::- file.txt        # remove all perms from "other"
setfacl -R -m u:alice:rX /var/www  # recursive, X = execute only if dir or already executable
setfacl -x u:alice file.txt     # remove alice's ACL entry
setfacl -b file.txt             # remove all ACL entries

# Default ACLs on directories (inherited by new files)
setfacl -d -m u:alice:rw /shared   # new files in /shared will give alice rw

ls -la shows + if ACL exists: -rw-rw-r--+ alice alice 0 file.txt
```

---

## Networking

### The iproute2 Suite (Replace ifconfig/route)

```bash
# Network interfaces
ip a                        # show all interfaces with IPs (ip addr show)
ip a show eth0              # specific interface
ip link show                # show interface state (up/down, MAC, MTU)
ip link set eth0 up         # bring interface up
ip link set eth0 down       # bring interface down

# Routing
ip r                        # routing table (ip route show)
ip r get 8.8.8.8            # which interface/gateway would reach this IP
ip r add default via 10.0.0.1 dev eth0   # add default route
ip r del default            # delete default route

# Temporary IP (lost on reboot — use NetworkManager or netplan for persistent)
ip addr add 10.0.0.10/24 dev eth0
ip addr del 10.0.0.10/24 dev eth0

# ARP cache
ip neigh show               # ARP table
ip neigh flush all          # clear ARP cache

# Old commands → new commands
ifconfig -a     →  ip a
ifconfig eth0   →  ip a show eth0
route -n        →  ip r
arp -n          →  ip neigh show
netstat -tlnp   →  ss -tlnp
```

### ss — Socket Statistics

```bash
ss -tlnp        # TCP (-t) listening (-l) numeric (-n) with process (-p)
ss -tulnp       # TCP + UDP listening
ss -tp          # TCP connections (established) with processes
ss -s           # summary statistics
ss -o state established '( dport = :https or dport = :http )'
ss -tnp dst 10.0.0.5    # connections to specific host

# Column meanings in ss -tlnp output:
# State   Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
# LISTEN  0      128    0.0.0.0:22           0.0.0.0:*         users:(("sshd",pid=1234,fd=3))
```

### DNS Configuration

```
Modern Ubuntu/Debian: systemd-resolved (DO NOT edit /etc/resolv.conf directly)
  /etc/resolv.conf → symlink to /run/systemd/resolve/stub-resolv.conf
  resolvectl status          ← show current DNS servers per-link
  resolvectl query hostname  ← DNS lookup via resolved
  resolvectl flush-caches    ← clear DNS cache (like ipconfig /flushdns on Windows)

  Edit DNS: /etc/netplan/*.yaml (Ubuntu), or NetworkManager connection config

RHEL/Rocky: NetworkManager manages /etc/resolv.conf
  nmcli dev show | grep DNS
  nmcli connection modify eth0 ipv4.dns "8.8.8.8 1.1.1.1"

/etc/hosts:
  127.0.0.1   localhost
  ::1         localhost
  10.0.0.5    mydb.internal    ← static override, consulted before DNS
  Equivalent to C:\Windows\System32\drivers\etc\hosts

  On Azure VMs: Azure DNS is 168.63.129.16 — DO NOT block this IP;
  it provides DHCP, DNS, health probe, and IMDS connectivity.
```

### Firewall — nftables and ufw

```bash
# nftables — the modern kernel packet filtering framework
# (replaces iptables, ip6tables, arptables, ebtables with one unified tool)
nft list ruleset                         # show all current rules
nft list tables                          # show tables
nft add rule inet filter input tcp dport 443 accept
nft -f /etc/nftables.conf               # load from file (persistent)

# Check if using nftables vs iptables:
nft list ruleset 2>/dev/null | head -5   # nftables
iptables -L -n                           # iptables (may be compat layer)

# ufw — Ubuntu's firewall wrapper (hides nftables/iptables complexity)
ufw status verbose              # is it running? what rules?
ufw enable                      # turn on (off by default on fresh Ubuntu)
ufw allow 22/tcp                # allow SSH
ufw allow 80/tcp                # allow HTTP
ufw allow 443/tcp               # allow HTTPS
ufw allow from 10.0.0.0/8      # allow from subnet
ufw deny 8080/tcp               # deny port
ufw delete allow 80/tcp         # remove rule
ufw reset                       # nuclear: remove all rules and disable

# Azure VMs: NSG (Network Security Group) is the outer firewall.
# ufw/nftables is a second layer inside the VM. If port is blocked at NSG,
# nothing gets to the VM-level firewall. Check NSG rules in Portal first.
```

### Packet Capture and Diagnostics

```bash
# tcpdump — packet capture
tcpdump -i eth0                           # capture all traffic on eth0
tcpdump -i eth0 port 80                   # only port 80
tcpdump -i eth0 host 10.0.0.5            # only traffic to/from host
tcpdump -i eth0 -w capture.pcap          # write to file (open in Wireshark)
tcpdump -i eth0 -nn port 80              # -n=no DNS lookup, -nn=also no port name

# curl with verbose
curl -v https://api.example.com/         # full request/response headers
curl -I https://example.com              # HEAD request only
curl -o /dev/null -w "%{http_code}\n" https://example.com  # just status code
curl -s --max-time 5 http://localhost:8080/health || echo "FAIL"

# netcat — TCP/UDP Swiss army knife
nc -l 8080                    # listen on port 8080
nc hostname 8080              # connect to port
nc -zv hostname 80 443 8080  # port scan (check if ports open)
echo "GET / HTTP/1.0" | nc example.com 80  # raw HTTP

# SSH config — ~/.ssh/config
Host bastion
    HostName bastion.example.com
    User azureuser
    IdentityFile ~/.ssh/id_rsa

Host prod-web
    HostName 10.0.1.10         # private IP — not directly reachable
    User deploy
    ProxyJump bastion          # tunnel through bastion (like Azure Bastion, but SSH native)
    IdentityFile ~/.ssh/id_rsa

# Then: ssh prod-web  (automatically jumps through bastion)

# SSH hardening (more detail in Security section)
ssh-copy-id user@host         # install your public key on remote host
ssh-keygen -t ed25519         # generate modern key (prefer over rsa)
```

---

## Storage

### Block Devices and Partitions

```bash
# Inventory
lsblk                    # tree view: disk → partition → mount point
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE,UUID
fdisk -l                 # detailed partition table (all disks)
df -h                    # disk space per mounted filesystem
df -hT                   # include filesystem type
du -sh /var/log          # total size of directory
du -sh /var/log/*        # size of each item in directory

# Partition table tools
fdisk /dev/sdb           # MBR partitions (interactive — legacy)
gdisk /dev/sdb           # GPT partitions (interactive)
parted /dev/sdb          # both MBR/GPT, scriptable

# Format
mkfs.ext4 /dev/sdb1      # ext4 — default on Ubuntu, reliable, journaled
mkfs.xfs /dev/sdb1       # XFS — preferred on RHEL, better for large files
mkfs.btrfs /dev/sdb1     # btrfs — snapshots, checksums, subvolumes

# Mount
mount /dev/sdb1 /mnt/data             # temporary mount
mount -o ro /dev/sdb1 /mnt/data       # read-only
mount -o remount,rw /mnt/data         # remount with different options

# Persistent mounts via /etc/fstab
# device          mountpoint   fstype  options         dump  pass
UUID=abc-123      /data        ext4    defaults         0     2
tmpfs             /tmp         tmpfs   defaults,noexec  0     0
//server/share    /mnt/cifs    cifs    credentials=/etc/cifs.creds 0 0

# Get UUID (use UUID in fstab — device names like /dev/sdb can change on reboot)
blkid /dev/sdb1
```

### LVM — Logical Volume Manager

LVM adds a virtualization layer between physical disks and filesystems. Windows Storage Spaces is the closest equivalent.

```
Physical World:              LVM World:
──────────────               ──────────
/dev/sdb (100GB)    ──►  PV (Physical Volume)
/dev/sdc (200GB)    ──►  PV
                          │
                          ▼
                     VG (Volume Group) = pool of all PV space
                          │
                    ┌─────┴─────┐
                    ▼           ▼
                    LV          LV       (Logical Volumes — like partitions but flexible)
                  /data (150GB) /backup (100GB)
                    │           │
                 mkfs.ext4   mkfs.xfs
                    │
                 mount → /data

Benefits: resize live, snapshots, span multiple disks, RAID within LVM
```

```bash
# Setup new LVM
pvcreate /dev/sdb /dev/sdc              # create PVs
vgcreate datavg /dev/sdb /dev/sdc       # create VG from PVs
lvcreate -L 150G -n datalv datavg       # create 150GB LV
mkfs.ext4 /dev/datavg/datalv            # format
mount /dev/datavg/datalv /data          # mount

# Inspect
pvs / pvdisplay           # physical volumes
vgs / vgdisplay           # volume groups
lvs / lvdisplay           # logical volumes

# Extend LV online (no downtime for ext4/xfs)
lvextend -L +50G /dev/datavg/datalv     # add 50GB to LV
resize2fs /dev/datavg/datalv            # grow ext4 filesystem to fill LV
xfs_growfs /data                        # grow XFS (uses mount point, not device)

# Snapshot (useful before risky changes)
lvcreate -L 10G -s -n snap1 /dev/datavg/datalv
```

### Azure-Specific Storage

```
Azure VM Disk Types:
─────────────────────────────────────────────────────────────────────
Ultra Disk      — sub-ms latency, configurable IOPS; databases only
Premium SSD v2  — best general purpose; flexible IOPS/throughput
Premium SSD     — predictable performance; most prod workloads
Standard SSD    — dev/test, infrequent access
Standard HDD    — backup, archival, tolerates high latency

Azure VM disk caching (set per disk in Portal or CLI):
  None          — write-through; safe for database data files
  ReadOnly      — cache reads; great for OS disk, read-heavy data
  ReadWrite     — cache reads and writes; ONLY for OS disk (risky for data)

Temporary disk (/dev/sdb → /mnt on Ubuntu Azure VMs):
  D: drive equivalent. Data is LOST when VM is deallocated or resized.
  Use only for scratch space, temp files, swap.
  Size depends on VM SKU.

Azure Files (SMB/NFS): mount as CIFS or NFS
  mount -t cifs //storage.file.core.windows.net/share /mnt/share \
    -o vers=3.0,username=...,password=...,dir_mode=0777,file_mode=0777
```

---

## Security

### SELinux (RHEL-family)

SELinux is mandatory access control. Every process and file has a label. The policy dictates what labels can access what. Think of it as a second permission system on top of Unix permissions — both must allow an action.

```bash
# Check status
getenforce              # Enforcing | Permissive | Disabled
sestatus                # detailed status
cat /etc/selinux/config # persistent setting

# Temporary mode change (doesn't survive reboot)
setenforce 0            # permissive — log but don't block (debug mode)
setenforce 1            # enforcing

# Labels
ls -Z /var/www/html     # show SELinux context
ps -eZ | grep nginx     # show process context
stat --format="%C" /etc/passwd  # context for a file

# Context format: user:role:type:level
# Example: system_u:object_r:httpd_sys_content_t:s0
#           ^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^
#           SELinux  role     type (most important)    sensitivity level
#           user

# Fix wrong context (nginx can't read files with wrong type)
restorecon -v /var/www/html/index.html     # restore default context
restorecon -Rv /var/www/html               # recursive
chcon -t httpd_sys_content_t /srv/myapp    # manually set type

# Policy booleans (toggle features without writing policy)
getsebool -a | grep httpd         # see all httpd booleans
setsebool httpd_can_network_connect on    # allow nginx to make outbound connections
setsebool -P httpd_can_network_connect on  # -P = persistent

# When things break: check audit log
ausearch -m AVC -ts recent        # recent SELinux denials
ausearch -m AVC -c nginx          # denials by nginx
journalctl | grep -i selinux      # systemd journal

# Generate policy from denials (use in dev, review before production)
ausearch -m AVC -ts recent | audit2allow    # shows what policy to add
ausearch -m AVC -ts recent | audit2allow -M mypolicy  # create .te file
semodule -i mypolicy.pp           # install the policy module
```

### AppArmor (Ubuntu)

AppArmor uses file paths instead of labels (simpler than SELinux, less powerful).

```bash
# Status
aa-status                         # show loaded profiles and confined processes
systemctl status apparmor         # is it running?

# Profile modes
aa-enforce /etc/apparmor.d/usr.sbin.nginx   # enforcing
aa-complain /etc/apparmor.d/usr.sbin.nginx  # complain only (log, don't block)
aa-disable /etc/apparmor.d/usr.sbin.nginx   # disable profile

# Reload profiles after editing
apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx

# Logs
journalctl | grep -i apparmor
grep -i apparmor /var/log/syslog

# Profiles live in:
ls /etc/apparmor.d/            # system profiles
# Docker runs with its own AppArmor profile: docker-default
# Kubernetes pods can specify AppArmor profiles via annotations
```

### auditd — Compliance Logging

auditd is the Linux audit subsystem. Equivalent to Windows Security Event Log + auditing GPO.

```bash
# Status
systemctl status auditd
auditctl -l              # list current rules
auditctl -s              # show audit status

# Add rules (temporary — add to /etc/audit/rules.d/audit.rules for persistence)
auditctl -w /etc/passwd -p wa -k passwd_changes    # watch passwd for writes
auditctl -w /etc/sudoers -p rwa -k sudoers_mod     # watch sudoers
auditctl -a always,exit -F arch=b64 -S execve -k process_exec  # log all exec

# Query logs
ausearch -k passwd_changes          # events with key "passwd_changes"
ausearch -m LOGIN -ts today         # login events today
ausearch -ua alice -ts recent       # recent events for user alice
ausearch -x /bin/su                 # events involving /bin/su executable
aureport --auth                     # authentication summary report
aureport --failed                   # failed event summary
aureport --executable               # executable summary

# Log file: /var/log/audit/audit.log (raw) or ausearch/aureport for queries
```

### SSH Hardening

```bash
# /etc/ssh/sshd_config — key settings
# Edit, then: systemctl restart sshd (or reload for graceful)

PermitRootLogin no                  # NEVER allow direct root SSH
PasswordAuthentication no           # key-only auth (must set up keys first)
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
AllowUsers alice bob deploy         # whitelist (only these users can SSH in)
# AllowGroups sshusers              # alternative: group-based
Port 2222                           # non-standard port (minor obscurity — reduces log noise)
MaxAuthTries 3                      # lock out after 3 failed attempts
ClientAliveInterval 300             # disconnect idle clients after 5min
ClientAliveCountMax 2
X11Forwarding no                    # disable unless needed
AllowTcpForwarding no               # disable unless needed (allow port tunneling)
Banner /etc/ssh/banner.txt          # legal banner before login

# Test config before restarting (avoid locking yourself out)
sshd -t                             # test config syntax
sshd -T | grep -i passwordauth      # show effective value

# Azure: use SSH keys via Azure Portal (key stored in VM metadata)
# Or: Azure AD SSH extension for Azure AD identity-based auth
# The temporary port 22 NSG inbound rule trick: add/remove via Portal
```

### Fail2ban — Brute Force Protection

```bash
# Install + start
apt install fail2ban    OR   dnf install fail2ban
systemctl enable --now fail2ban

# Config: /etc/fail2ban/jail.local (override jail.conf — don't edit jail.conf)
[DEFAULT]
bantime  = 1h           # ban duration
findtime = 10m          # window for counting failures
maxretry = 5            # failures before ban

[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log    # Ubuntu
# logpath = /var/log/secure   # RHEL

# Status
fail2ban-client status          # list jails
fail2ban-client status sshd     # status of SSH jail (banned IPs)
fail2ban-client set sshd unbanip 1.2.3.4   # manually unban

# On Azure VMs: Fail2ban + NSG is a good belt-and-suspenders combo.
# NSG blocks at vNet level; fail2ban bans at OS level.
```

### AIDE — File Integrity Monitoring

```bash
# AIDE = Advanced Intrusion Detection Environment
# Equivalent to Windows File Integrity Monitoring in Defender for Endpoint

apt install aide    OR    dnf install aide

# Initialize database (captures current known-good state)
aide --init
mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db

# Check for changes
aide --check        # compare current state against database
aide --update       # update database (after intentional changes)

# Typical systemd timer or cron to check daily:
# 0 3 * * * /usr/bin/aide --check | mail -s "AIDE report" admin@example.com
```

### Security Quick-Reference

```
Task                              Command
───────────────────────────────────────────────────────────────────────────
Find world-writable files         find / -perm -0002 -not -path "*/proc/*" 2>/dev/null
Find setuid binaries              find / -perm -4000 -type f 2>/dev/null
Check listening ports             ss -tlnp
Check logged-in users             who, w, last
Check failed logins               lastb, faillog, ausearch -m FAILED_LOGIN
Check sudo usage                  ausearch -m USER_CMD -ts today
Check recently modified files     find /etc -mtime -1 -type f
Show user's groups                groups alice, id alice
Check passwd/shadow integrity     pwck, grpck
Verify package integrity (RPM)    rpm -Va
Verify package integrity (deb)    debsums -c
Check open files by user          lsof -u alice
View kernel security params       sysctl -a | grep -E "(randomize|dmesg|kptr|ptrace)"
```

---

## Filesystem Event Watching — inotify / fanotify

Every `--watch` flag in every dev tool (webpack, jest, tsc, cargo watch) is inotify underneath. Understanding the abstraction unlocks debugging `ENOSPC` on inotify limits, slow reloads, and missed events.

```
FILESYSTEM NOTIFICATION APIs
═════════════════════════════════════════════════════════════════════════

  Linux                          Windows                        macOS
  ──────────────────────         ──────────────────────         ──────────────────────
  inotify (since 2.6.13)         ReadDirectoryChangesW()        FSEvents (high-level)
  fanotify (since 2.6.36)        FileSystemWatcher (.NET)       kqueue EVFILT_VNODE

  Model:                         Model:                         Model:
    inotify_create() → fd          open handle with             FSEventStreamCreate()
    inotify_add_watch(fd, path,      FILE_FLAG_OVERLAPPED        → callback with event
      IN_MODIFY|IN_CREATE|...)      + FILE_LIST_DIRECTORY      kqueue: per-inode watch
    poll/select/epoll on fd        ReadDirectoryChangesW()
    read(fd) → inotify_event        (overlapped)

  Granularity:                   Granularity:                   Granularity:
    inotify: file-level events     directory-level only          FSEvents: path-based
    fanotify: filesystem-wide      (reports path, not inode)     coalesced (may batch)
    (used by AV, audit daemons)    can miss renames in rapid     kqueue: single file/dir

  Limits (common pain point):    No such limits                 No such limits
    /proc/sys/fs/inotify/
      max_user_watches (default 8192)
      max_user_instances (128)
      max_queued_events (16384)
    Fix for IDE / container dev:
      echo fs.inotify.max_user_watches=524288 >> /etc/sysctl.conf
      sysctl -p

  fanotify vs inotify:
    fanotify: intercept + allow/deny (used by antivirus)
    fanotify: global mount-point scope, not per-path
    fanotify: needs CAP_SYS_ADMIN
    inotify: simpler, per-path, no privileges needed

Watch events (inotify):
  IN_ACCESS       file read
  IN_MODIFY       file written (content changed)
  IN_CLOSE_WRITE  file closed after write (more reliable than IN_MODIFY for full writes)
  IN_CREATE       file/dir created in watched directory
  IN_DELETE       file/dir deleted
  IN_MOVED_FROM / IN_MOVED_TO   rename (paired by cookie field)
  IN_ATTRIB       metadata changed (chmod, chown, xattr)
```

```bash
# Command-line inotify consumer
inotifywait -r -m /var/www/html -e modify,create,delete
# -r = recursive, -m = monitor (don't exit after first event)

# In scripts: act on changes
inotifywait -r -m /etc/app/ -e close_write --format '%w%f' |
while read file; do
    systemctl reload myapp
done
```

## Linux Memory Model — Production Tuning Depth

### RSS vs VSZ vs PSS vs USS

```
MEMORY METRIC DEFINITIONS
════════════════════════════════════════════════════════════════════

  Metric   What it measures                          When to use
  ──────   ──────────────────────────────────────    ──────────────────────────
  VSZ      Virtual address space size                Meaningless for memory pressure;
  (VIRT)   Total mapped: code+heap+stack+mmap        a 100GB mmap has huge VSZ but
           Includes not-yet-faulted pages            uses no RAM
           Includes shared libs (full size counted)

  RSS      Resident Set Size: pages currently in RAM  Rough estimate; double-counts
  (RES)    Includes shared libs (counted per proc)    shared pages
           Does NOT include swapped-out pages         Sum of all RSS > physical RAM
           top/htop show this as "RES"                is normal (shared libs)

  PSS      Proportional Set Size                     Best for "how much does this
           RSS but shared pages divided by           process actually cost?"
           number of sharers                         sum(PSS for all procs) ≈ total used
           /proc/PID/smaps_rollup → Pss field

  USS      Unique Set Size: pages unique to this     Best for finding memory leaks
           process (not shared with anyone)          USS grows = this process is leaking
           /proc/PID/smaps → Private_Clean + Private_Dirty

  Practical hierarchy:
    VSZ ≥ RSS ≥ PSS ≥ USS
    For memory leak investigation: watch USS
    For capacity planning: PSS
    For quick eyeball: RSS (but don't sum it)
```

```bash
# Get PSS and USS for a process
cat /proc/$(pgrep myapp)/smaps_rollup | grep -E "(Pss:|Private_)"

# smem tool: shows PSS/USS per process (apt install smem)
smem -s pss -r

# Process memory breakdown
cat /proc/$(pgrep myapp)/status | grep -E "VmRSS|VmPeak|VmSize"
```

### OOM Killer

```
LINUX OOM KILLER ALGORITHM
════════════════════════════

  When physical RAM + swap is exhausted, OOM killer selects a victim.

  Scoring algorithm (simplified):
    oom_score = (process_RSS_in_pages / total_RAM_pages) * 1000
    Adjusted by:  oom_score_adj  (range: -1000 to +1000)
      -1000 = never kill this process (OOM immune)
        0   = default scoring
      +1000 = kill this first (highest badness)

  Who sets oom_score_adj:
    systemd: OOMScoreAdjust= in service unit
    Kubernetes: sets -999 for kubelet itself, 1000 for BestEffort pods
    Docker: --oom-score-adj flag on docker run

  Check current score:
    cat /proc/$(pgrep nginx)/oom_score       # current calculated score
    cat /proc/$(pgrep nginx)/oom_score_adj   # adjustment value

  Protect a critical process (careful — can cause system deadlock):
    echo -1000 > /proc/$(pgrep myapp)/oom_score_adj
    # or systemd: OOMScoreAdjust=-1000

  Make a process be killed first (useful for memory hog workers):
    echo 1000 > /proc/$(pgrep myworker)/oom_score_adj

  OOM events in logs:
    journalctl -k | grep -i "oom\|kill"      # kernel OOM messages
    dmesg | grep "Out of memory"
```

### Huge Pages

```
HUGE PAGES — WHEN AND WHY
══════════════════════════

  Standard page: 4KB (x86-64 default)
  Huge page:     2MB (standard huge page) or 1GB (gigantic page)

  Why they matter:
    TLB (Translation Lookaside Buffer) has limited entries (~1500 on modern Intel)
    4KB pages → 1500 TLB entries → covers 6MB of address space
    2MB pages → 1500 TLB entries → covers 3GB of address space
    For large working sets (databases, ML): huge pages eliminate TLB misses
    Real-world impact: PostgreSQL, Redis, JVM GC heap — 5-20% throughput gain

  Two mechanisms:

  1. Transparent Huge Pages (THP) — kernel decides automatically
     /sys/kernel/mm/transparent_hugepage/enabled
       [always] madvise never
     madvise = only when process explicitly requests via madvise(MADV_HUGEPAGE)

     THP gotcha: can cause latency spikes on write (page split + promote)
     Redis/MongoDB/Cassandra documentation says: set THP to madvise or never
     echo madvise > /sys/kernel/mm/transparent_hugepage/enabled

  2. Explicit huge pages — pre-allocated, reserved
     sysctl vm.nr_hugepages=1024       # reserve 1024 × 2MB = 2GB
     cat /proc/meminfo | grep Huge     # HugePages_Total / Free / Reserved
     Applications: mmap with MAP_HUGETLB, or mount hugetlbfs

  Check THP activity:
    grep -i huge /proc/vmstat          # thp_fault_alloc, thp_collapse_alloc
    numastat -m                        # NUMA node memory breakdown
```

## Decision Cheat Sheet

| You want to...                                   | Use                                                          |
|--------------------------------------------------|--------------------------------------------------------------|
| Start/stop/restart a daemon                      | `systemctl start/stop/restart <service>`                     |
| See why a service failed                         | `systemctl status <svc>` then `journalctl -u <svc> -n 50`   |
| Add a service that starts on boot                | `systemctl enable --now <svc>`                               |
| Run a script on a schedule (replace cron)        | systemd timer unit (`.timer` + `.service` pair)              |
| See all listening ports with owning process      | `ss -tlnp`                                                   |
| Find which process is using port 8080            | `ss -tlnp | grep 8080` or `lsof -i :8080`                    |
| See CPU/memory/load in real time                 | `htop` or `btop`                                             |
| Kill a stuck process                             | `kill <pid>` (SIGTERM); if unresponsive: `kill -9 <pid>`     |
| See what files a process has open                | `lsof -p <pid>`                                              |
| Trace syscalls of a running process              | `strace -p <pid>`                                            |
| Find which package owns a file                   | `dpkg -S /path` (Debian) or `rpm -qf /path` (RHEL)          |
| Install a package                                | `apt install <pkg>` (Debian) or `dnf install <pkg>` (RHEL)  |
| Find where a binary came from                    | `which nginx`, `type nginx`, `command -v nginx`              |
| Check disk space                                 | `df -h`                                                      |
| Find what's eating disk space                    | `du -sh /var/*` then drill down                              |
| Resize a filesystem without downtime             | LVM: `lvextend` + `resize2fs` or `xfs_growfs`               |
| See kernel messages / hardware errors            | `dmesg -T | tail -50` or `journalctl -k`                     |
| Debug DNS resolution                             | `resolvectl query hostname` or `dig hostname @8.8.8.8`       |
| Check if a port is open on remote host           | `nc -zv host port` or `curl -m 3 http://host:port`           |
| Capture network traffic                          | `tcpdump -i eth0 -w /tmp/cap.pcap` → open in Wireshark      |
| Debug container permission issues               | `docker inspect <ctr>`, check SELinux/AppArmor denials       |
| Enable IP forwarding (routing between NICs)      | `echo 1 > /proc/sys/net/ipv4/ip_forward`; persist in sysctl  |
| See container resource usage                     | `docker stats` (user-facing) or inspect cgroup directly      |
| Profile CPU in production (no restart)           | `bpftrace -e 'profile:hz:99 { @[kstack]=count(); }'`         |
| Trace file opens system-wide                     | `opensnoop-bpfcc` or bpftrace openat tracepoint               |
| Add a firewall rule (Ubuntu)                     | `ufw allow 443/tcp`                                          |
| Add a firewall rule (RHEL)                       | `firewall-cmd --add-port=443/tcp --permanent && firewall-cmd --reload` |
| Give a user sudo access                          | Add to `/etc/sudoers.d/username` via `visudo -f`             |
| Change file permissions                          | `chmod 644 file`, `chown user:group file`                    |
| Check what distro you're on                      | `cat /etc/os-release`                                        |
| Check kernel version                             | `uname -r`                                                   |
| Check system uptime and load                     | `uptime` or `w`                                              |
| Keep a process running after logout              | `tmux` session, or `nohup cmd &`                             |
| See boot time breakdown                          | `systemd-analyze blame`                                      |
| Check SELinux denials (RHEL)                     | `ausearch -m AVC -ts recent`                                 |
| Allow a service through SELinux (RHEL)           | `setsebool -P httpd_can_network_connect on`                  |

---

## Common Confusion Points

**`/proc` and `/sys` are not on disk.** They look like directories with files, but they're virtual filesystems that the kernel generates on-demand. Reading `/proc/meminfo` runs kernel code that formats current memory stats into text. Writing to `/proc/sys/net/ipv4/ip_forward` directly modifies a kernel variable. This is not magic — it's the "everything is a file" abstraction enabling shell scripts to configure the kernel.

**systemd journal vs /var/log files.** systemd captures all service stdout/stderr in the journal automatically. But many applications also write to `/var/log/*.log` themselves. You may need to check both. `journalctl -u nginx` shows what systemd captured; `/var/log/nginx/error.log` shows what nginx wrote directly. They can differ.

**`systemctl daemon-reload` is mandatory after editing unit files.** systemd caches unit files in memory. If you edit `/etc/systemd/system/myapp.service` and then try to `systemctl restart myapp`, you will restart the OLD version. Run `systemctl daemon-reload` first.

**cgroups v1 vs v2 on your cluster nodes.** If you're debugging container resource limits, first check which version is active (`stat -fc %T /sys/fs/cgroup/`). cgroup v1 is still present on older AKS node pools. The paths differ significantly between v1 and v2. AKS 1.25+ uses cgroup v2 by default.

**Package manager installed vs locally compiled.** Packages from apt/dnf go into `/usr/`. Manual installs should go into `/usr/local/`. Docker-style single-binary vendor drops often land in `/opt/`. If you have two versions of a tool, `which tool` tells you which one is first on PATH; `type -a tool` shows all of them.

**`kill -9` does not clean up.** SIGKILL is delivered directly to the kernel's process accounting — the process never runs again and its signal handlers never execute. The process cannot flush buffers, close database connections, or delete temp files. Only use SIGKILL when SIGTERM has failed after a reasonable wait. For services: `systemctl stop` sends SIGTERM then SIGKILL after `TimeoutStopSec` (default 90s).

**Azure VM's temp disk (`/mnt` or `/dev/sdb`) is ephemeral.** Deallocate the VM (not just restart — DEALLOCATE), and the temp disk is wiped and re-provisioned from scratch. Never store anything there you need to keep. This is by design — it's local storage on the physical host, not on your managed disk. The swap file on Azure VMs is typically configured on the temp disk via `waagent.conf` for this same reason (swap is ephemeral by nature).

**SELinux `permissive` is not `disabled`.** Permissive mode logs denials but doesn't block them. This is how you debug SELinux issues: switch to permissive, exercise the code path, then `ausearch -m AVC -ts recent` to see what would have been blocked. Then create the appropriate policy or boolean. Never leave a production system permanently in permissive mode.

**`sudo -i` vs `sudo su -` vs `sudo bash`.** `sudo -i` invokes a login shell as root (reads `/root/.profile`, `/root/.bash_profile`). `sudo su -` does the same thing but via an extra process. `sudo bash` gives you a root bash but does NOT source login files — PATH and other profile-set variables may differ. `sudo -i` is the clean modern approach.

**eBPF requires kernel 4.4+ for basics, 5.x+ for advanced features.** bpftrace works well on kernel 4.9+. cgroup v2 eBPF attachments need 5.2+. BTF (BPF Type Format — CO-RE portability) needs 5.4+. Azure VMs run Ubuntu 22.04 (kernel 5.15) or later, so you generally have full eBPF capability. Check: `uname -r`.

**Namespaces give isolation; cgroups give resource limits. They are orthogonal.** A container is a process in multiple namespaces (isolation) with cgroup limits applied (resources). You can use namespaces without cgroups and vice versa. `unshare --pid --fork --mount-proc bash` gives you a PID-namespace-isolated bash with no cgroup constraints.

**`/etc/resolv.conf` on Ubuntu is a symlink.** On Ubuntu 18.04+, `/etc/resolv.conf` is symlinked to `/run/systemd/resolve/stub-resolv.conf` which points to systemd-resolved's local stub resolver (`127.0.0.53`). Editing it directly is wrong and will be overwritten. Use `resolvectl` or Netplan to configure DNS. On Azure VMs this matters because Azure's DNS at `168.63.129.16` is configured via DHCP, which feeds into systemd-resolved.
