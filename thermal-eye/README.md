<div align="center">

# ◈ THERMAL-EYE

```
████████╗██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ██╗     
╚══██╔══╝██║  ██║██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     
   ██║   ███████║█████╗  ██████╔╝██╔████╔██║███████║██║     
   ██║   ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║     
   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
                        ███████╗██╗   ██╗███████╗            
                        ██╔════╝╚██╗ ██╔╝██╔════╝            
                        █████╗   ╚████╔╝ █████╗              
                        ██╔══╝    ╚██╔╝  ██╔══╝              
                        ███████╗   ██║   ███████╗            
                        ╚══════╝   ╚═╝   ╚══════╝            
```

<img src="https://img.shields.io/badge/THERMAL-IMAGING-FF4500?style=for-the-badge&labelColor=0D0D0D" alt="thermal">
<img src="https://img.shields.io/badge/ANOMALY-DETECTION-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="anomaly">
<img src="https://img.shields.io/badge/HARDWARE-INTEGRATED-00FF41?style=for-the-badge&labelColor=0D0D0D" alt="hardware">

**SEEING HEAT. FINDING THE INVISIBLE.**

*FLIR/SEEK integration • Anomaly detection AI • Presence identification • Environmental mapping*

</div>

---

## ◈ CONCEPT

Heat reveals truth. Every object, every being, every electronic device leaves a thermal signature. **thermal-eye** integrates with your thermal imaging equipment to detect anomalies that shouldn't exist—heat signatures without sources, cold spots that defy physics, and patterns that suggest hidden presence.

*"In the infrared spectrum, ghosts have nowhere to hide."*

---

## ◈ SUPPORTED HARDWARE

| Device | Connection | Resolution | Features |
|:-------|:-----------|:-----------|:---------|
| FLIR One Pro | USB/Lightning | 160×120 | MSX enhancement, 70mK sensitivity |
| FLIR E8-XT | USB | 320×240 | Extended temp range, WiFi |
| FLIR Lepton 3.5 | SPI/I2C | 160×120 | Embedded integration, radiometric |
| Seek Thermal CompactPRO | USB | 320×240 | Wide FOV, adjustable focus |
| Seek Reveal PRO | USB | 320×240 | Built-in LED, long range |
| InfiRay P2 Pro | USB-C | 256×192 | Macro lens, high sensitivity |
| Custom sensors | GPIO/SPI | Variable | DIY integration support |

---

## ◈ CAPABILITIES

### ▸ REAL-TIME ANOMALY DETECTION

```python
from thermal_eye import ThermalScanner, AnomalyDetector

# Initialize with your device
scanner = ThermalScanner(device="flir_one_pro")
detector = AnomalyDetector(sensitivity="high")

# Real-time scanning with ML anomaly detection
async for frame in scanner.stream():
    analysis = detector.analyze(frame)
    
    for anomaly in analysis.anomalies:
        print(f"▸ {anomaly.type} at {anomaly.location}")
        print(f"  Temperature: {anomaly.temp}°C")
        print(f"  Strangeness: {anomaly.strangeness}%")
        print(f"  Explanation: {anomaly.explanation}")
```

### ▸ PRESENCE DETECTION

Identify heat signatures that indicate hidden presence:
- Human-shaped heat patterns in "empty" rooms
- Residual heat from recent occupation
- Hidden electronics (surveillance devices)
- Animal presence detection

```python
from thermal_eye import PresenceDetector

presence = PresenceDetector()

async for detection in presence.monitor():
    if detection.human_probable:
        print(f"⚠️ Human presence detected")
        print(f"   Location: {detection.grid_location}")
        print(f"   Confidence: {detection.confidence}%")
        print(f"   Motion: {detection.motion_vector}")
```

### ▸ ENVIRONMENTAL MAPPING

Build 3D thermal maps of spaces over time:

```python
from thermal_eye import ThermalMapper

mapper = ThermalMapper()

# Capture thermal panorama
await mapper.capture_panorama()

# Generate 3D thermal model
model = mapper.build_model()
model.export("room_thermal.obj")

# Find anomalous cold/hot spots
anomalies = model.find_anomalies()
for spot in anomalies:
    print(f"Anomaly: {spot.type} at {spot.coords}")
```

### ▸ TEMPORAL ANALYSIS

Track thermal changes over time to detect patterns:

```python
from thermal_eye import TemporalAnalyzer

analyzer = TemporalAnalyzer()

# Record thermal timelapse
await analyzer.record(duration_hours=24)

# Analyze patterns
patterns = analyzer.find_patterns()

for pattern in patterns:
    print(f"Pattern: {pattern.description}")
    print(f"Recurrence: {pattern.period}")
    print(f"Correlation: {pattern.correlation}")
```

---

## ◈ ANOMALY TYPES

```
◈ THERMAL-EYE v2.0 › LIVE SCAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVICE: FLIR One Pro
RESOLUTION: 160×120 @ 9 FPS
SENSITIVITY: 70mK

ANOMALIES DETECTED

▸ COLD SPOT [A1]
  Grid: 47,82 • Size: 23px² • Temp: 12.4°C
  Ambient: 21.3°C • Delta: -8.9°C
  Classification: UNEXPLAINED
  Physics violation: Localized cold without source
  Strangeness ████████░░ 84%

▸ HEAT RESIDUE [A2]
  Grid: 112,45 • Size: 187px² • Temp: 28.7°C
  Pattern: Humanoid silhouette
  Decay rate: Slower than expected
  Last occupied: ~47 minutes ago
  Strangeness ███████░░░ 71%

▸ PHANTOM HEAT [A3]
  Grid: 89,67 • Size: 12px² • Temp: 34.2°C
  No visible source • Stationary
  Duration: 12 minutes continuous
  Strangeness █████████░ 91%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCAN ACTIVE • ANOMALIES: 3 • HIGH STRANGENESS: 2
```

---

## ◈ INTEGRATION WITH BAUDRILLARD SUITE

### With spectral

Correlate thermal anomalies with EMF readings:

```python
from thermal_eye import ThermalScanner
from spectral import EMFScanner
from baudrillard.correlation import MultiModalAnalyzer

thermal = ThermalScanner()
emf = EMFScanner()

analyzer = MultiModalAnalyzer()

# Synchronous multi-modal scan
async for t_frame, e_frame in zip(thermal.stream(), emf.stream()):
    correlations = analyzer.correlate(t_frame, e_frame)
    
    if correlations.significant:
        print(f"Correlated anomaly detected!")
        print(f"Thermal: {correlations.thermal}")
        print(f"EMF: {correlations.emf}")
        print(f"Correlation: {correlations.coefficient}")
```

### With cool-memories

Automatically log thermal anomalies:

```python
from thermal_eye import ThermalScanner
from cool_memories import ImmutableLog

log = ImmutableLog()
scanner = ThermalScanner()

async for frame in scanner.stream():
    for anomaly in frame.anomalies:
        if anomaly.strangeness > 70:
            await log.record(
                event_type="thermal_anomaly",
                data=anomaly.to_dict(),
                attachment=frame.raw_data,
                timestamp=frame.timestamp
            )
```

---

## ◈ DESKTOP APPLICATION

Native Tauri app with:
- Real-time thermal video feed
- Anomaly highlighting and tracking
- Historical analysis dashboard
- Multi-camera support
- Recording and export

```
◈ THERMAL-EYE DESKTOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

     LIVE FEED                      ANALYSIS
  ╔═══════════════╗           Anomalies: 3
  ║ ▓▓▓░░░▒▒▓▓▓  ║           Strangeness: 74%
  ║ ▓▒▒░░░░░▒▓▓  ║           Recording: 00:14:37
  ║ ▓▒▒▒░A1░░▒▓  ║           
  ║ ▓▓▒▒░░░▒▒▓▓  ║           TEMPERATURE
  ║ ▓▓▓▓▒▒▒▓▓▓▓  ║           Min: 14.2°C
  ╚═══════════════╝           Max: 31.7°C
                              Ambient: 21.4°C
▸ Recording    ▸ Screenshot    ▸ Export

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLIR One Pro • Connected • 9 FPS
```

---

## ◈ MOBILE APPLICATION

Thermal scanning on the go with phone-compatible devices:

- FLIR One (iOS/Android)
- Seek Thermal (iOS/Android)
- InfiRay (Android)

Features:
- Live anomaly detection
- GPS-tagged recordings
- Cloud sync with desktop
- Share findings to community

---

## ◈ INSTALLATION

```bash
# Core library
pip install baudrillard-thermal-eye

# Desktop app
cd apps/thermal-eye-desktop
npm install && npm run tauri build

# Device drivers
sudo apt install libusb-1.0-0-dev
pip install pyflir pyseekit
```

---

<div align="center">

*"Heat is the signature of existence. The absence of heat where heat should be is the signature of something else."*

**BAUDRILLARD SUITE**

</div>
