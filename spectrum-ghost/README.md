<div align="center">

# ◈ SPECTRUM-GHOST

```
███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ██╗   ██╗███╗   ███╗
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗ ████║
███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝██║   ██║██╔████╔██║
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║
███████║██║     ███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
           ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗                 
          ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝                 
          ██║  ███╗███████║██║   ██║███████╗   ██║                    
          ██║   ██║██╔══██║██║   ██║╚════██║   ██║                    
          ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║                    
           ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                    
```

<img src="https://img.shields.io/badge/SOFTWARE--DEFINED-RADIO-00D4FF?style=for-the-badge&labelColor=0D0D0D" alt="sdr">
<img src="https://img.shields.io/badge/RF-ANOMALY%20HUNTING-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="rf">
<img src="https://img.shields.io/badge/SIGNAL-ARCHAEOLOGY-FF0066?style=for-the-badge&labelColor=0D0D0D" alt="signal">

**LISTENING TO FREQUENCIES THAT SHOULDN'T EXIST**

*HackRF/RTL-SDR integration • Phantom carrier detection • Signal archaeology • RF fingerprinting*

</div>

---

## ◈ CONCEPT

The electromagnetic spectrum is crowded with signals—radio, WiFi, cellular, satellite. But sometimes there are signals that have no registered source. Carriers with no modulation. Frequencies that respond to nothing. **spectrum-ghost** hunts these phantom signals.

*"The ghost in the machine speaks on frequencies we forgot to listen to."*

---

## ◈ SUPPORTED HARDWARE

| Device | Frequency Range | Bandwidth | TX | Notes |
|:-------|:----------------|:----------|:---|:------|
| HackRF One | 1MHz - 6GHz | 20MHz | ✓ | Full duplex, portable |
| RTL-SDR v3 | 24MHz - 1.7GHz | 2.4MHz | ✗ | Low cost, great for beginners |
| RTL-SDR v4 | 500kHz - 1.7GHz | 2.4MHz | ✗ | Direct sampling mode |
| Airspy HF+ | 9kHz - 31MHz | 768kHz | ✗ | HF specialist, high dynamic range |
| Airspy Mini | 24MHz - 1.8GHz | 6MHz | ✗ | Compact, high performance |
| LimeSDR | 100kHz - 3.8GHz | 61.44MHz | ✓ | Research grade, MIMO |
| USRP B210 | 70MHz - 6GHz | 56MHz | ✓ | Professional, high precision |
| PlutoSDR | 325MHz - 3.8GHz | 20MHz | ✓ | Affordable TX/RX |

---

## ◈ CAPABILITIES

### ▸ PHANTOM CARRIER DETECTION

Hunt for unregistered signals across the spectrum:

```python
from spectrum_ghost import SpectrumScanner, PhantomDetector

scanner = SpectrumScanner(device="hackrf")
detector = PhantomDetector()

# Full spectrum sweep
async for sweep in scanner.sweep(1e6, 6e9, step=1e6):
    phantoms = detector.analyze(sweep)
    
    for phantom in phantoms:
        print(f"▸ PHANTOM at {phantom.frequency/1e6:.3f} MHz")
        print(f"  Power: {phantom.power_dbm} dBm")
        print(f"  Bandwidth: {phantom.bandwidth/1e3:.1f} kHz")
        print(f"  Modulation: {phantom.modulation or 'NONE'}")
        print(f"  Registered source: {phantom.registered or 'NONE'}")
        print(f"  Strangeness: {phantom.strangeness}%")
```

### ▸ SIGNAL ARCHAEOLOGY

Recover and analyze signals that have been absorbed, reflected, or partially occluded:

```python
from spectrum_ghost import SignalArchaeologist

archaeologist = SignalArchaeologist()

# Recover signal from environmental reflections
recovered = await archaeologist.recover(
    frequency=433.92e6,
    duration_seconds=60,
    method="multipath_reconstruction"
)

print(f"Recovered signal confidence: {recovered.confidence}%")
print(f"Original source bearing: {recovered.bearing}°")
print(f"Time offset: {recovered.time_offset_us}µs")

# Decode if modulation detected
if recovered.decodable:
    data = archaeologist.decode(recovered)
    print(f"Recovered data: {data}")
```

### ▸ RF FINGERPRINTING

Every transmitter has a unique RF fingerprint—slight imperfections in the hardware that create identifiable patterns:

```python
from spectrum_ghost import RFFingerprinter

fingerprinter = RFFingerprinter()

# Capture and fingerprint a signal
signature = await fingerprinter.capture(frequency=915e6)

# Check against database
match = fingerprinter.identify(signature)

if match:
    print(f"Identified device: {match.device_type}")
    print(f"Manufacturer: {match.manufacturer}")
    print(f"Confidence: {match.confidence}%")
    print(f"Previous sightings: {match.sighting_count}")
else:
    print("Unknown device - adding to database")
    fingerprinter.add_unknown(signature)
```

### ▸ TEMPORAL SIGNAL ANALYSIS

Signals that appear and disappear on schedules, or that correlate with other events:

```python
from spectrum_ghost import TemporalAnalyzer

analyzer = TemporalAnalyzer()

# Monitor for 24 hours
await analyzer.record(
    frequency_range=(400e6, 500e6),
    duration_hours=24
)

# Find patterns
patterns = analyzer.find_patterns()

for pattern in patterns:
    print(f"▸ Pattern: {pattern.description}")
    print(f"  Frequency: {pattern.frequency/1e6:.3f} MHz")
    print(f"  Schedule: {pattern.schedule}")
    print(f"  Correlation: {pattern.correlation}")
```

---

## ◈ SAMPLE OUTPUT

```
◈ SPECTRUM-GHOST v2.0 › RF HUNT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVICE: HackRF One
RANGE: 1MHz → 6GHz
MODE: Phantom Detection

SWEEP PROGRESS ████████████░░░░░░░░ 60%

PHANTOMS DETECTED

▸ PHANTOM #1 [433.847 MHz]
  Power: -67 dBm • BW: 12 kHz
  Modulation: NONE (carrier only)
  Registered: ISM band, no active license
  Duration: 47 minutes continuous
  Behavior: Responds to nothing
  Strangeness ████████░░ 83%

▸ PHANTOM #2 [1.42 GHz]
  Power: -112 dBm (below noise floor?)
  Modulation: Unknown pulsed pattern
  Registered: Hydrogen line (natural)
  Anomaly: Artificial modulation on natural frequency
  Strangeness █████████░ 94%

▸ PHANTOM #3 [2.847 GHz]
  Power: -78 dBm • BW: 847 kHz
  Modulation: OFDM-like structure
  Registered: NONE
  Movement: Signal source appears to be mobile
  Bearing: 247° ± 15°
  Strangeness ███████░░░ 71%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCAN ACTIVE • PHANTOMS: 3 • UNEXPLAINED: 2
```

---

## ◈ INTEGRATION WITH BAUDRILLARD SUITE

### With spectral

Combine RF analysis with EMF and acoustic:

```python
from spectrum_ghost import SpectrumScanner
from spectral import MultiModalScanner

scanner = MultiModalScanner()
scanner.add_rf(SpectrumScanner("hackrf"))
scanner.add_emf()
scanner.add_acoustic()

# Correlate all anomalies
async for event in scanner.unified_scan():
    if event.multi_modal_correlation > 0.7:
        print(f"Multi-modal anomaly!")
        print(f"RF: {event.rf}")
        print(f"EMF: {event.emf}")
        print(f"Acoustic: {event.acoustic}")
```

### With thermal-eye

Correlate RF sources with thermal signatures:

```python
from spectrum_ghost import DirectionFinder
from thermal_eye import ThermalScanner

df = DirectionFinder()
thermal = ThermalScanner()

# Find RF source direction
bearing = await df.locate(frequency=915e6)

# Look for thermal source in that direction
thermal_sources = await thermal.scan_direction(bearing)

for source in thermal_sources:
    print(f"Possible transmitter: {source.description}")
    print(f"Temperature: {source.temp}°C")
```

---

## ◈ ADVANCED FEATURES

### ▸ DISTRIBUTED SENSING

Multiple SDRs working together for enhanced detection:

```python
from spectrum_ghost import DistributedNetwork

network = DistributedNetwork()
network.add_node("hackrf@192.168.1.10")
network.add_node("rtlsdr@192.168.1.11")
network.add_node("rtlsdr@192.168.1.12")

# Triangulation mode
source = await network.triangulate(frequency=433.92e6)
print(f"Source location: {source.lat}, {source.lon}")
print(f"Accuracy: ±{source.accuracy_m}m")
```

### ▸ WATERFALL ARCHAEOLOGY

Recover historical signals from long recordings:

```python
from spectrum_ghost import WaterfallArchaeologist

wa = WaterfallArchaeologist()

# Load historical recording
wa.load("spectrum_24h.raw")

# Find signals that no longer exist
historical = wa.find_departed()

for signal in historical:
    print(f"Signal last seen: {signal.last_seen}")
    print(f"Frequency: {signal.frequency/1e6:.3f} MHz")
    print(f"Duration: {signal.total_duration}")
```

---

## ◈ DESKTOP APPLICATION

Native Tauri app with:
- Real-time spectrum waterfall display
- Phantom signal highlighting
- Signal recording and playback
- Direction finding visualization
- Multi-SDR support

---

## ◈ INSTALLATION

```bash
# Core library
pip install baudrillard-spectrum-ghost

# Desktop app
cd apps/spectrum-ghost-desktop
npm install && npm run tauri build

# SDR drivers
sudo apt install libhackrf-dev rtl-sdr librtlsdr-dev
```

---

<div align="center">

*"Every frequency has a story. Some stories were never meant to be told."*

**BAUDRILLARD SUITE**

</div>
