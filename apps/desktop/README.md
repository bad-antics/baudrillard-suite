<div align="center">

# ◈ BAUDRILLARD DESKTOP

```
██████╗ ███████╗███████╗██╗  ██╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██║ ██╔╝╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║█████╗  ███████╗█████╔╝    ██║   ██║   ██║██████╔╝
██║  ██║██╔══╝  ╚════██║██╔═██╗    ██║   ██║   ██║██╔═══╝ 
██████╔╝███████╗███████║██║  ██╗   ██║   ╚██████╔╝██║     
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     
```

<img src="https://img.shields.io/badge/TAURI-2.0-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="tauri">
<img src="https://img.shields.io/badge/REACT-18-FF0066?style=for-the-badge&labelColor=0D0D0D" alt="react">
<img src="https://img.shields.io/badge/RUST-BACKEND-00FF41?style=for-the-badge&labelColor=0D0D0D" alt="rust">

**NATIVE DESKTOP APPLICATIONS FOR THE BAUDRILLARD SUITE**

*Tauri 2.0 • React + TypeScript • TailwindCSS • SQLite*

</div>

---

## ◈ APPLICATIONS

### simulacra-desktop

Process authentication with real-time visualization.

**Features:**
- Live process tree with authenticity coloring
- Genealogical graph explorer
- Alert system with notifications
- Historical analysis dashboard
- Export to cool-memories

### spectral-desktop

Multi-modal anomaly detection dashboard.

**Features:**
- Real-time sensor visualization
- Cross-modal correlation graphs
- Hardware device management
- Session recording/playback
- Anomaly mapping

### glitch-desktop

Reality inconsistency monitoring.

**Features:**
- Entropy visualization
- Temporal drift graphs
- Synchronicity journal
- Sensor consistency monitor
- Reality confidence meter

### thermal-eye-desktop

Thermal imaging integration.

**Features:**
- Live thermal video feed
- Anomaly highlighting
- Temperature mapping
- Recording/screenshot
- Multi-camera support

### spectrum-ghost-desktop

SDR spectrum analysis.

**Features:**
- Waterfall display
- Phantom signal detection
- Signal recording/playback
- Direction finding
- RF fingerprint database

### command-center

Unified dashboard for all tools.

**Features:**
- All tools in one interface
- Cross-tool correlation
- Unified logging
- System status overview
- Quick actions

---

## ◈ DESIGN SYSTEM

### Colors

| Name | Hex | Usage |
|:-----|:----|:------|
| Electric Purple | `#9B30FF` | Primary accent |
| Matrix Green | `#00FF41` | Status: OK, active |
| Glitch Pink | `#FF0066` | Alerts, warnings |
| Void Black | `#0D0D0D` | Backgrounds |
| Deep Purple | `#1a0a2e` | Secondary background |
| Soft White | `#E0E0E0` | Text |

### Typography

- **Headers:** JetBrains Mono, bold
- **Body:** Inter, regular
- **Code:** JetBrains Mono, regular

### Components

All components follow the design system:
- No box borders (use shadows, gradients)
- Glassmorphism effects
- Smooth animations
- Responsive layout

---

## ◈ ARCHITECTURE

```
apps/desktop/
├── src-tauri/              # Rust backend
│   ├── src/
│   │   ├── main.rs         # Entry point
│   │   ├── commands/       # Tauri commands
│   │   ├── hardware/       # Device interfaces
│   │   └── analysis/       # Core algorithms
│   └── Cargo.toml
│
├── src/                    # React frontend
│   ├── components/         # UI components
│   ├── views/              # Application views
│   ├── stores/             # State management
│   ├── hooks/              # Custom hooks
│   └── styles/             # TailwindCSS
│
├── package.json
└── tauri.conf.json
```

---

## ◈ DEVELOPMENT

```bash
# Install dependencies
npm install

# Run in development mode
npm run tauri dev

# Build for production
npm run tauri build
```

### Prerequisites

- Node.js 18+
- Rust 1.70+
- Tauri prerequisites for your OS

---

## ◈ SCREENSHOTS

```
╔══════════════════════════════════════════════════════════════╗
║  ◈ SPECTRAL DESKTOP                              ─ □ ✕      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    EMF                      ║
║   ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓    52.8µT                    ║
║   ▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓    ████████░░                ║
║   ▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▓▓▓▓▓▓                              ║
║   ▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▓▓▓▓▓    ACOUSTIC                  ║
║   ▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▓▓▓▓▓    Silent                    ║
║   ▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▓▓▓▓▓▓    ░░░░░░░░░░                ║
║   ▓▓▓▓▓▓▓▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓                              ║
║   ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓    NETWORK                   ║
║                                    Phantoms: 2              ║
║   ▸ EMF    ▸ Acoustic    ▸ Network    ▸ Thermal             ║
║                                                              ║
║   ANOMALIES                                                  ║
║   ────────────────────────────────────────────               ║
║   14:23:07  EMF spike +12µT                    [View]        ║
║   14:31:44  Network phantom 10.0.0.47          [View]        ║
║   14:47:22  Infrasonic 18.9Hz                  [View]        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## ◈ PLATFORM SUPPORT

| Platform | Status | Notes |
|:---------|:-------|:------|
| Linux | ✅ | Full support, all features |
| macOS | ✅ | Full support, native look |
| Windows | ✅ | Full support |

---

<div align="center">

*"The interface between reality and simulation"*

**BAUDRILLARD SUITE**

</div>
