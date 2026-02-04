<div align="center">

# ◈ SPECTRAL

```
███████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ ██╗     
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝███████║██║     
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║██║     
███████║██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║███████╗
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
```

<img src="https://img.shields.io/badge/LIMINAL-DETECTION-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="liminal">
<img src="https://img.shields.io/badge/MULTI-MODAL-FF0066?style=for-the-badge&labelColor=0D0D0D" alt="multimodal">
<img src="https://img.shields.io/badge/ANOMALY-RESEARCH-00FF41?style=for-the-badge&labelColor=0D0D0D" alt="anomaly">

**LISTENING TO THE SPACES BETWEEN**

*EMF analysis • Acoustic detection • Network phantoms • Cross-modal correlation*

</div>

---

## ◈ CONCEPT

Ghosts, by definition, exist at the threshold—neither fully present nor fully absent. They occupy liminal spaces. **spectral** detects anomalies across multiple sensory modalities: electromagnetic fields that fluctuate without cause, sounds below human hearing, network packets from hosts that don't exist.

*"The ghost is not what haunts us—it is what we fail to see."*

---

## ◈ DETECTION MODALITIES

### ▸ ELECTROMAGNETIC

Detect unexplained EMF fluctuations using device sensors or external hardware:

```python
from spectral import EMFScanner

emf = EMFScanner()

# Use device magnetometer
emf.use_device_sensor()

# Or external hardware
# emf.use_hardware("emf-sensor-001")

async for reading in emf.monitor():
    if reading.anomalous:
        print(f"▸ EMF ANOMALY")
        print(f"  Field strength: {reading.microtesla}µT")
        print(f"  Baseline: {reading.baseline}µT")
        print(f"  Deviation: {reading.deviation_sigma}σ")
        print(f"  Duration: {reading.duration_ms}ms")
        print(f"  Strangeness: {reading.strangeness}%")
```

### ▸ ACOUSTIC

Detect infrasonic (< 20Hz) and ultrasonic (> 20kHz) signals:

```python
from spectral import AcousticScanner

acoustic = AcousticScanner()

# Configure frequency ranges
acoustic.enable_infrasonic(min_hz=0.1, max_hz=20)
acoustic.enable_ultrasonic(min_hz=20000, max_hz=48000)

async for event in acoustic.listen():
    if event.type == "infrasonic":
        print(f"▸ INFRASONIC DETECTION")
        print(f"  Frequency: {event.frequency}Hz")
        print(f"  Duration: {event.duration}s")
        print(f"  Note: 18.9Hz associated with unease/hallucination")
    
    elif event.type == "ultrasonic":
        print(f"▸ ULTRASONIC DETECTION")
        print(f"  Frequency: {event.frequency}Hz")
        print(f"  Pattern: {event.pattern}")
```

### ▸ NETWORK PHANTOMS

Detect impossible network activity—responses from non-existent hosts:

```python
from spectral import NetworkPhantomScanner

scanner = NetworkPhantomScanner()

# Scan for phantoms
async for phantom in scanner.hunt():
    print(f"▸ NETWORK PHANTOM")
    print(f"  IP: {phantom.ip}")
    print(f"  Responded: {phantom.responded}")
    print(f"  Host exists: {phantom.host_exists}")
    print(f"  ARP entry: {phantom.arp_exists}")
    print(f"  Timestamp anomaly: {phantom.timestamp_future}")
```

### ▸ ENVIRONMENTAL

Temperature, pressure, humidity anomalies:

```python
from spectral import EnvironmentalScanner

env = EnvironmentalScanner()

async for reading in env.monitor():
    for anomaly in reading.anomalies:
        print(f"▸ {anomaly.type.upper()} ANOMALY")
        print(f"  Value: {anomaly.value}")
        print(f"  Expected: {anomaly.expected}")
        print(f"  Location: {anomaly.location}")
```

---

## ◈ CROSS-MODAL CORRELATION

The most significant anomalies manifest across multiple modalities:

```python
from spectral import MultiModalScanner, CorrelationEngine

scanner = MultiModalScanner()
scanner.enable_emf()
scanner.enable_acoustic()
scanner.enable_network()
scanner.enable_environmental()

correlator = CorrelationEngine()

async for event_group in scanner.unified_scan():
    correlations = correlator.analyze(event_group)
    
    if correlations.significant:
        print(f"▸ MULTI-MODAL ANOMALY CLUSTER")
        print(f"  Correlation coefficient: {correlations.r}")
        print(f"  Modalities: {', '.join(correlations.modalities)}")
        print(f"  Temporal alignment: {correlations.temporal_sync_ms}ms")
        print(f"  Strangeness: {correlations.combined_strangeness}%")
        
        # These are the interesting ones
        if correlations.combined_strangeness > 80:
            print(f"  ⚠️ HIGH STRANGENESS EVENT")
```

---

## ◈ SAMPLE OUTPUT

```
◈ SPECTRAL v2.0 › LIMINAL ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHANNELS OPEN

▸ EMF SPECTRUM
  Baseline: 47.2µT (Earth's field normal)
  Current: 52.8µT
  Deviation: 2.3σ
  ⚡ Unexplained fluctuation detected
  Strangeness ████████░░ 79%

▸ ACOUSTIC LAYER
  Infrasonic: 18.9Hz continuous
  Duration: 47 minutes
  Amplitude: Below perception threshold
  ⚠️ 18.9Hz associated with optical hallucination
  Strangeness ███████░░░ 68%

▸ NETWORK PHANTOMS
  10.0.0.47 › Responded to ping
  Host verification: FAILED (no such host)
  ARP table: EMPTY for this IP
  Timestamp: 3 minutes IN THE FUTURE
  Strangeness █████████░ 94%

▸ ENVIRONMENTAL
  Temperature: Localized cold spot (-4.2°C delta)
  Location: Grid C7
  Duration: 12 minutes
  No HVAC explanation
  Strangeness ███████░░░ 71%

▸ CORRELATION ANALYSIS
  EMF ↔ Temperature: r=0.87 (Strong)
  EMF ↔ Acoustic: r=0.34 (Weak)
  Temporal sync: All events within 2.4s window

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANOMALIES: 7 • HIGH STRANGENESS: 2 • LIMINAL INDEX: ELEVATED
```

---

## ◈ MOBILE APPLICATION

Real-time anomaly detection using your phone's sensors:

**iOS/Android Features:**
- Magnetometer for EMF fluctuations
- Microphone for infra/ultrasonic
- Camera for visual anomaly detection
- Accelerometer for vibration
- GPS for location tagging
- Background monitoring

```
◈ SPECTRAL MOBILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EMF ████████░░ 52.8µT (+5.6)
ACOUSTIC ░░░░░░░░░░ Silent
TEMP ██████░░░░ 18.4°C
MOTION ░░░░░░░░░░ Stable

▸ Recording • GPS: 47.6205, -122.3493
▸ 2 anomalies logged this session

ANOMALY LOG
  14:23:07 EMF spike +12µT (3.2s)
  14:31:44 Infrasonic 17.4Hz (8s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ◈ DESKTOP APPLICATION

Native Tauri app with:
- Real-time multi-modal dashboard
- Historical anomaly visualization
- Correlation analysis graphs
- Location-based anomaly mapping
- Session recording and export

---

## ◈ HARDWARE INTEGRATION

External sensors for enhanced detection:

| Device | Type | Integration |
|:-------|:-----|:------------|
| K-II EMF | EMF | USB/Bluetooth |
| Mel Meter | EMF/Temp | USB |
| Trifield | EMF | USB |
| Custom Arduino | Multi | USB/Serial |
| Raspberry Pi Pico | Multi | USB |

---

## ◈ INSTALLATION

```bash
pip install baudrillard-spectral

# Mobile apps
cd apps/spectral-mobile
npm install && npx expo build

# Desktop app
cd apps/spectral-desktop
npm install && npm run tauri build
```

---

<div align="center">

*"Between presence and absence lies the space where ghosts dwell."*

**BAUDRILLARD SUITE**

</div>
