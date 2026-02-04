<div align="center">

```
 ██████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ ██╗     
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
╚█████╗ ██████╔╝█████╗  ██║        ██║   ██████╔╝███████║██║     
 ╚═══██╗██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║██║     
██████╔╝██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║███████╗
╚═════╝ ╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                    ◈ Liminal Signal Analysis ◈
```

<p><em>"Ghosts are never present themselves, but only by their effects."</em></p>

<p>
  <img src="https://img.shields.io/badge/baudrillard-suite-9B30FF?style=for-the-badge" alt="suite">
  <img src="https://img.shields.io/badge/spectral-analysis-00FF41?style=for-the-badge" alt="spectral">
  <img src="https://img.shields.io/badge/rust-1.70+-FF0066?style=for-the-badge&logo=rust&logoColor=white" alt="rust">
</p>

**Multi-Dimensional Anomaly Detection - Finding what shouldn't exist**

</div>

---

## 🌌 Concept

**Spectral** operates in the liminal space between signal and noise, presence and absence. It's not a ghost hunter—it's an anomaly archaeologist that excavates signals from the gaps in our instrumentation.

Baudrillard wrote about the "spectral" nature of information—how signs circulate without referents, how meaning haunts the networks. Spectral takes this literally: detecting electromagnetic, acoustic, network, and data anomalies that exist in the spaces our tools normally ignore.

---

## ⚡ Unique Detection Modes

### 👻 EMF Spectral Analysis (Hardware Mode)
*Requires: RTL-SDR, HackRF, or compatible SDR*

```python
# Detect unaccounted electromagnetic presence
spectral --haunt --spectrum 1MHz-6GHz
```

- **Interstitial Frequencies**: Signals in bands "nothing should use"
- **Phantom Carriers**: RF signatures with no legitimate source
- **Temporal Echoes**: Repeating patterns suggesting recording/playback
- **Presence Gradients**: EMF fluctuations correlating with physical space

### 🔊 Acoustic Archaeology
*Detects signals hidden in audio/silence*

- **Infrasonic Presence**: Sub-20Hz vibrations (classic "haunted" frequencies)
- **Ultrasonic Data**: Hidden communications above human hearing
- **Silence Analysis**: What exists in the "gaps" between sounds
- **Resonance Anomalies**: Unexpected room modes/standing waves

### 📡 Network Phantoms
*Traffic that shouldn't exist*

- **Phantom Routes**: Packets traversing impossible network paths
- **Temporal Displacement**: Traffic with anachronistic timestamps
- **Spectral Hosts**: Responses from IPs that don't exist
- **Protocol Ghosts**: Valid-seeming data in invalid protocol states

### 💾 Data Revenants
*Information that keeps returning*

- **Deletion Echoes**: Traces of data that "won't stay dead"
- **Reincarnation Patterns**: Same data appearing across unrelated files
- **Entropy Anomalies**: Regions of unexpected order in randomness
- **Temporal Artifacts**: Files with impossible modification histories

---

## 🚀 Installation

```bash
git clone https://github.com/bad-antics/spectral
cd spectral
cargo build --release

# Optional: Install SDR support
./install-sdr-support.sh

# Optional: Install acoustic analysis
pip install spectral-audio
```

## 📖 Usage

```bash
# Full spectrum sweep (all modes)
sudo spectral --manifest

# EMF anomaly detection (requires SDR)
sudo spectral --haunt --sdr hackrf

# Network phantom hunter
sudo spectral --exorcise --interface eth0

# Audio anomaly analysis
spectral --listen --input microphone --duration 3600

# Data archaeology
spectral --excavate /path/to/investigate

# Real-time monitoring dashboard
spectral --vigil --dashboard
```

---

## 🎯 Detection Philosophy

| Traditional IDS/Scanner | Spectral |
|------------------------|----------|
| Looks for known signatures | Finds unknown anomalies |
| Binary: threat/safe | Spectrum of strangeness |
| Ignores "noise" | The noise IS the signal |
| Single-domain analysis | Multi-dimensional correlation |
| Assumes physics is complete | Explores the gaps |

---

## 📊 Output Example

```
 ██████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ ██╗     
[MANIFESTING] Opening liminal channels...

◈ SPECTRAL ANALYSIS ◈

┌─────────────────────────────────────────────────────────────────────┐
│ EMF ANOMALY DETECTED                                                │
├─────────────────────────────────────────────────────────────────────┤
│ Frequency:        433.847 MHz (interstitial band)                   │
│ Signal Type:      Coherent carrier, no modulation                   │
│ Duration:         Intermittent, 3.7s bursts                         │
│ Source Direction: 127° (azimuth), -12° (elevation)                  │
│ Correlation:      85% match with previous anomaly (2 days ago)      │
│ Classification:   PHANTOM CARRIER - No registered transmitter       │
│ Strangeness:      ████████░░ 82%                                    │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ NETWORK PHANTOM                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ Source IP:        10.0.0.47 (NO HOST AT THIS ADDRESS)               │
│ Protocol:         TCP SYN to port 31337                             │
│ MAC Address:      00:00:00:00:00:00 (null)                          │
│ TTL Analysis:     Impossible - suggests negative hop count          │
│ Temporal:         Timestamp is 3 minutes IN THE FUTURE              │
│ Classification:   TEMPORAL DISPLACEMENT                             │
│ Strangeness:      ██████████ 97%                                    │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ ACOUSTIC ANOMALY                                                    │
├─────────────────────────────────────────────────────────────────────┤
│ Frequency:        18.9 Hz (infrasonic)                              │
│ Duration:         Continuous, 47 minutes                            │
│ Amplitude:        -42 dB (below perception threshold)               │
│ Correlation:      Room resonance mode NOT matching room dimensions  │
│ Note:             18.9 Hz is associated with optical hallucination  │
│ Classification:   PRESENCE GRADIENT                                 │
│ Strangeness:      ███████░░░ 71%                                    │
└─────────────────────────────────────────────────────────────────────┘

◈ SUMMARY ◈
Anomalies detected: 7
High strangeness events: 3
Correlation clusters: 2
Liminal activity index: ELEVATED

"What haunts are not the dead, but the gaps left within us."
```

---

## �� Research Applications

- **Paranormal Investigation**: Scientific approach to anomaly detection
- **RF Security**: Find covert transmitters and bugs
- **Network Security**: Detect sophisticated C2 channels
- **Data Forensics**: Recover "deleted" information patterns
- **Acoustic Analysis**: Infrasound research, room acoustics
- **Simulation Research**: Detect "glitches in the matrix"

---

## 🔗 Part of the Baudrillard Suite

| Tool | Concept | Status |
|------|---------|--------|
| [simulacra](../simulacra) | Ontological process authentication | 🟢 Active |
| **spectral** | Liminal signal analysis | 🟢 Active |
| [hyperreal](../hyperreal) | Memory forensics | 🟡 Building |
| [fatal](../fatal) | Exploit framework | 🟡 Building |
| [seduction](../seduction) | Social engineering | 🟡 Building |

---

<div align="center">
  <img src="https://img.shields.io/badge/made%20for-the%20liminal%20space-9B30FF?style=for-the-badge" alt="liminal">
  <p><em>"The ghost is the sign that circulates without a referent."</em></p>
</div>
