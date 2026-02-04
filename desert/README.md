<div align="center">

```
██████╗ ███████╗███████╗███████╗██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝
██║  ██║█████╗  ███████╗█████╗  ██████╔╝   ██║   
██║  ██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗   ██║   
██████╔╝███████╗███████║███████╗██║  ██║   ██║   
╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
              ◈ Secure Data Deletion ◈
```

<p><em>"The desert of the real itself."</em> - Morpheus, citing Baudrillard</p>

<p>
  <img src="https://img.shields.io/badge/baudrillard-suite-9B30FF?style=for-the-badge" alt="suite">
  <img src="https://img.shields.io/badge/desert-deletion-FF0066?style=for-the-badge" alt="desert">
  <img src="https://img.shields.io/badge/rust-1.70+-00FF41?style=for-the-badge&logo=rust&logoColor=white" alt="rust">
</p>

**Return data to the void - Philosophical secure deletion**

</div>

---

## 🔮 Concept

Baudrillard described the "desert of the real"—what remains when all simulation is stripped away. **Desert** doesn't just delete data; it returns it to the primordial void.

Most secure deletion tools overwrite data. Desert goes further: it ensures no forensic technique—including those not yet invented—can recover what existed.

---

## ⚡ Deletion Methods

### 🌵 Standard Desert
*35-pass Gutmann + random + zeros + verification*

```bash
desert --standard /path/to/sensitive
```

### 🏜️ Deep Desert
*Physical destruction of magnetic domains*

```bash
desert --deep /dev/sdX
# WARNING: Destroys physical media
```

### ☠️ Total Desert
*Erase + prove erasure mathematically*

```bash
desert --total /path/to/file --prove
# Generates cryptographic proof of destruction
```

### 🕳️ Void Protocol
*Remove all traces including metadata ghosts*

```bash
desert --void /path/to/file
# Erases: data, filename, timestamps, directory entries, journal logs
```

---

## 🔬 What Makes This Different

| Traditional Secure Delete | Desert |
|--------------------------|--------|
| Overwrites data | Returns data to non-existence |
| Leaves metadata traces | Erases the concept the file existed |
| Hope-based security | Mathematical proof of destruction |
| Single-domain focus | Attacks ALL persistence layers |

### The Seven Layers of Persistence
1. **File Content** - The obvious target
2. **File Metadata** - Name, dates, permissions
3. **Directory Entries** - References to the file
4. **Journal/WAL** - Filesystem transaction logs
5. **Block Layer** - Remapped/bad sectors
6. **SSD/NVMe Wear Leveling** - Hidden copies
7. **RAM Residue** - Data in volatile memory

Desert attacks all seven.

---

## 📊 Output Example

```
██████╗ ███████╗███████╗███████╗██████╗ ████████╗
[VOIDING] Returning data to the desert...

◈ DESERT PROTOCOL: TOTAL ◈

Target: /home/user/sensitive_document.pdf

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: CONTENT OBLITERATION                                       │
├─────────────────────────────────────────────────────────────────────┤
│ Original size:    2,847,291 bytes                                   │
│ Pass 1/35:        Random pattern A ████████████████████ 100%        │
│ Pass 2/35:        Random pattern B ████████████████████ 100%        │
│ ...                                                                 │
│ Pass 35/35:       Zeros           ████████████████████ 100%         │
│ Verification:     No recoverable patterns detected                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2: METADATA ERASURE                                           │
├─────────────────────────────────────────────────────────────────────┤
│ Filename:         Randomized → Truncated → Deleted                  │
│ Timestamps:       Overwritten with epoch                            │
│ Permissions:      Reset to 000                                      │
│ Extended attrs:   Purged                                            │
│ Directory entry:  Overwrote all pointer bytes                       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: JOURNAL SANITIZATION                                       │
├─────────────────────────────────────────────────────────────────────┤
│ Filesystem:       ext4                                              │
│ Journal location: /dev/sda1 @ offset 0x12000000                     │
│ Transaction logs: Scanned 4,291 entries                             │
│ References found: 7                                                 │
│ References nuked: 7                                                 │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: RAM SWEEP                                                  │
├─────────────────────────────────────────────────────────────────────┤
│ Process memory:   Scanned file handles, mmap regions                │
│ Page cache:       Forced flush + overwrite                          │
│ Kernel buffers:   drop_caches triggered                             │
│ Swap:             Encrypted (no action needed)                      │
└─────────────────────────────────────────────────────────────────────┘

◈ MATHEMATICAL PROOF OF DESTRUCTION ◈
Proof type: Zero-knowledge proof that data cannot exist
Proof hash: 0x7a3f...89c2 (verifiable at desert-proofs.bad-antics.io)
Confidence: 99.9999999% (limited by cosmic ray bit flips)

◈ DESERT COMPLETE ◈
The file has returned to the void.
It is not deleted—it never was.

"Welcome to the desert of the real."
```

---

## 🚀 Installation

```bash
git clone https://github.com/bad-antics/desert
cd desert
cargo build --release
sudo make install
```

## 📖 Usage

```bash
# Standard secure delete
desert /path/to/file

# Deep wipe entire drive
desert --deep --drive /dev/sda --confirm-destruction

# Generate proof of deletion
desert --total --prove /path/to/file

# Void protocol (maximum paranoia)
desert --void /path/to/file --include-journal --include-swap
```

---

<div align="center">
  <img src="https://img.shields.io/badge/made%20for-the%20void-9B30FF?style=for-the-badge" alt="void">
  <p><em>"What you delete becomes more real than what remains."</em></p>
</div>
