<div align="center">

```
 ██████╗ ██████╗  ██████╗ ██╗         ███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗ ██╗███████╗███████╗
██╔════╝██╔═══██╗██╔═══██╗██║         ████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗██║██╔════╝██╔════╝
██║     ██║   ██║██║   ██║██║         ██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝██║█████╗  ███████╗
██║     ██║   ██║██║   ██║██║         ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗██║██╔══╝  ╚════██║
╚██████╗╚██████╔╝╚██████╔╝███████╗    ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║██║███████╗███████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                              ◈ Fragmentary Truth ◈
```

<p><em>"Cool Memories: that is to say, the photographic memories of a world without affect."</em></p>

<p>
  <img src="https://img.shields.io/badge/baudrillard-suite-9B30FF?style=for-the-badge" alt="suite">
  <img src="https://img.shields.io/badge/cool--memories-forensic%20logging-FF0066?style=for-the-badge" alt="cool-memories">
  <img src="https://img.shields.io/badge/rust-1.70+-00FF41?style=for-the-badge&logo=rust&logoColor=white" alt="rust">
</p>

**Encrypted Forensic Journaling - Memories that cannot be falsified**

</div>

---

## 🔮 Concept

Baudrillard's "Cool Memories" were fragmentary observations—truths scattered across time without narrative coherence. **Cool-Memories** applies this to forensic logging.

Traditional logging: Linear, complete, easily manipulated
Cool-Memories: Fragmentary, cryptographically immutable, self-authenticating

Each fragment proves the others existed. Delete one, and the absence becomes visible.

---

## ⚡ Core Features

### 🔗 Hash-Chain Immutability
Every entry is cryptographically linked to all previous entries. Modify the past, and the future breaks.

### 🧩 Fragmentary Storage
Logs are shattered across multiple storage locations. No single compromise reveals the truth.

### ⏰ Temporal Proofs
Each entry proves it existed at a specific time using external timestamp authorities.

### 👁️ Witness Protocol
Entries are silently witnessed by distributed nodes. Even the logger can't falsify history.

### 🔐 Plausible Deniability
Multiple encryption layers with different keys reveal different "truths"

---

## 🛠️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         COOL-MEMORIES                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Event → Encrypt → Fragment → Hash-Chain → Witness → Store    │
│                                                                 │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│   │Fragment1│    │Fragment2│    │Fragment3│    │Fragment4│     │
│   │ (local) │    │ (cloud) │    │(witness)│    │ (cold)  │     │
│   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
│        │              │              │              │           │
│        └──────────────┴──────────────┴──────────────┘           │
│                         │                                       │
│                   ┌─────┴─────┐                                 │
│                   │ Hash Root │                                 │
│                   │ (immutable)│                                │
│                   └───────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📖 Usage

```bash
# Initialize cool-memories vault
cool-memories init --fragments 4 --threshold 3

# Log an event
cool-memories log "User admin logged in from 10.0.0.1"

# Log with metadata
cool-memories log --severity critical --tags "auth,breach" "Failed auth attempt"

# Log with automatic screenshot
cool-memories log --capture-screen "Suspicious activity observed"

# Verify log integrity
cool-memories verify --full

# Export for legal proceedings
cool-memories export --format legal --prove-timeline

# Search memories
cool-memories search "authentication" --timerange "2026-01-01..now"
```

---

## 📊 Output Example

```
 ██████╗ ██████╗  ██████╗ ██╗         ███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗ ██╗███████╗███████╗
[REMEMBERING] Loading fragmentary truth...

◈ MEMORY VERIFICATION REPORT ◈

Vault: /var/lib/cool-memories/primary
Entries: 47,291
Timespan: 2025-06-15 → 2026-02-03

┌─────────────────────────────────────────────────────────────────────┐
│ INTEGRITY CHECK                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ Hash chain:       ████████████████████████████████ VALID            │
│ Witness sigs:     ████████████████████████████████ VALID            │
│ Timestamp proofs: ████████████████████████████████ VALID            │
│ Fragment quorum:  4/4 fragments available                           │
│                                                                     │
│ Overall integrity: 100%                                             │
│ Tampering detected: NONE                                            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ RECENT MEMORIES                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ [2026-02-03 14:23:17.847] [INFO] [hash:0x7a3f...]                   │
│   "System boot completed"                                           │
│   Witnesses: 3/3 ✓  Timestamp: RFC3161 ✓                           │
│                                                                     │
│ [2026-02-03 14:24:02.129] [WARN] [hash:0x8b4c...]                   │
│   "Failed SSH attempt from 45.33.32.156"                            │
│   Witnesses: 3/3 ✓  Timestamp: RFC3161 ✓                           │
│   Attachment: network_capture.pcap (encrypted)                      │
│                                                                     │
│ [2026-02-03 14:24:03.001] [CRIT] [hash:0x9c5d...]                   │
│   "Brute force pattern detected"                                    │
│   Witnesses: 3/3 ✓  Timestamp: RFC3161 ✓                           │
│   Attachment: screenshot.png (encrypted)                            │
│   Auto-response: Firewall rule added                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ TEMPORAL PROOF CHAIN                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ Entry 47289 ←─┐                                                     │
│   │           │ proves                                              │
│ Entry 47290 ←─┼──── Entry 47291 existed at 14:24:03                 │
│   │           │                                                     │
│ Entry 47291 ──┘                                                     │
│                                                                     │
│ External anchors:                                                   │
│   Bitcoin block 892,471 (merkle root includes our hash)             │
│   Ethereum block 19,847,221 (commitment published)                  │
│   RFC3161 timestamp: DigiCert authority                             │
│                                                                     │
│ Temporal proof confidence: ABSOLUTE                                 │
│ (Would require breaking Bitcoin to falsify)                         │
└─────────────────────────────────────────────────────────────────────┘

◈ MEMORY STATUS ◈
"The past is never dead. It's not even past." 
— But now we can prove it.
```

---

## 🔒 Security Model

### Threat: Attacker compromises logging server
**Mitigation**: Fragments distributed across 4+ locations. Need 3/4 to reconstruct.

### Threat: Attacker tries to modify past logs
**Mitigation**: Hash chain breaks. Witnesses have independent copies.

### Threat: Attacker denies logs existed
**Mitigation**: Blockchain anchors prove existence at specific times.

### Threat: Legal compulsion to reveal logs
**Mitigation**: Plausible deniability keys reveal innocent-looking decoy logs.

---

## 🚀 Installation

```bash
git clone https://github.com/bad-antics/cool-memories
cd cool-memories
cargo build --release
sudo ./install.sh
cool-memories init
```

---

<div align="center">
  <img src="https://img.shields.io/badge/made%20for-immutable%20truth-9B30FF?style=for-the-badge" alt="truth">
  <p><em>"Memory is the only paradise from which we cannot be expelled."</em></p>
</div>
