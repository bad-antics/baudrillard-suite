---
layout: page
title: Spectral - Network Forensics
permalink: /tools/spectral/
---

# Spectral

**Network forensics tool with spectral decomposition for detecting covert channels, protocol anomalies, and hidden data exfiltration patterns.**

<img src="https://img.shields.io/badge/category-forensics-blue?style=flat-square" alt="forensics">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Spectral applies frequency-domain analysis to network traffic, revealing patterns invisible to traditional tools. By transforming packet timing and size data into the spectral domain, it detects:

- **C2 Beaconing** - Periodic communication patterns
- **DNS Tunneling** - Covert data channels via DNS
- **ICMP Exfiltration** - Hidden data in ICMP payloads
- **Protocol Anomalies** - Deviations from expected behavior
- **Encrypted Channel Detection** - High-entropy traffic analysis

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git
pip install -r requirements.txt

# Standalone
pip install baudrillard-spectral
```

### Dependencies
- Python 3.10+
- scapy
- numpy
- matplotlib (optional, for visualization)

---

## Quick Start

```bash
# Basic PCAP analysis
python spectral/spectral.py --pcap capture.pcap

# Full analysis with report
python spectral/spectral.py --pcap capture.pcap --full-analysis --output report/

# Detect covert channels
python spectral/spectral.py --pcap capture.pcap --detect-covert

# Live capture analysis
sudo python spectral/spectral.py --interface eth0 --live
```

---

## Usage

### Basic Analysis

```bash
python spectral/spectral.py --pcap traffic.pcap
```

Output:
```
[*] Loading capture: traffic.pcap
[*] Packets: 45,231 | Duration: 3,600s | Protocols: TCP, UDP, DNS, ICMP

=== TRAFFIC OVERVIEW ===
Top Talkers:
  192.168.1.100 -> 10.0.0.1    : 12,847 packets (28%)
  192.168.1.100 -> 8.8.8.8     : 8,234 packets (18%)
  
Protocol Distribution:
  TCP  : 67%
  UDP  : 28%
  ICMP : 3%
  Other: 2%
```

### Covert Channel Detection

```bash
python spectral/spectral.py --pcap capture.pcap --detect-covert
```

Detects:
- DNS tunneling (iodine, dnscat2, custom)
- ICMP tunneling (icmpsh, custom)
- HTTP(S) covert channels
- Timing-based covert channels

### Spectral Analysis

```bash
python spectral/spectral.py --pcap capture.pcap --spectral --protocol dns
```

Output:
```
=== SPECTRAL ANALYSIS: DNS ===

Dominant Frequencies:
  0.033 Hz (30s period)  - Amplitude: 0.87 ████████░░
  0.017 Hz (60s period)  - Amplitude: 0.45 ████░░░░░░
  0.008 Hz (120s period) - Amplitude: 0.23 ██░░░░░░░░

[!] Strong 30-second periodicity detected
[!] Pattern consistent with: Timed beacon / Data exfiltration
```

### Entropy Analysis

```bash
python spectral/spectral.py --pcap capture.pcap --entropy
```

High entropy in unexpected places indicates:
- Encrypted data where plaintext expected
- Compressed/encoded payloads
- Steganographic content

### Visualization

```bash
python spectral/spectral.py --pcap capture.pcap --visualize --output plots/
```

Generates:
- `timeline.png` - Traffic over time
- `spectrum.png` - Frequency domain analysis
- `entropy_map.png` - Entropy heatmap
- `flow_graph.png` - Communication patterns

---

## Detection Modules

### DNS Analysis

```bash
python spectral/spectral.py --pcap capture.pcap --dns-deep

[*] DNS Deep Analysis
    Queries: 8,234
    Unique domains: 127
    
[!] Anomalies Detected:
    - High subdomain entropy: *.c2.evil.com (7.8 bits/char)
    - Unusual TXT record volume: data.exfil.com
    - Long subdomain labels: aGVsbG8gd29ybGQ.tunnel.net
```

### Beacon Detection

```bash
python spectral/spectral.py --pcap capture.pcap --detect-beacons

[*] Beacon Analysis
    
[!] Potential Beacon Detected:
    Source: 192.168.1.50
    Destination: 45.33.32.156:443
    Interval: 60.2s (σ=5.1s)
    Jitter: 8.5%
    Pattern: Cobalt Strike (default)
    Confidence: 91%
```

### Flow Analysis

```bash
python spectral/spectral.py --pcap capture.pcap --flows

[*] Flow Analysis

Suspicious Flows:
  192.168.1.50 -> 45.33.32.156:443
    - Duration: 3,542s
    - Packets: 847 (out) / 1,203 (in)
    - Ratio: 0.70 (unusual for HTTPS)
    - Timing: Highly periodic
```

---

## Output Formats

```bash
# JSON report
python spectral/spectral.py --pcap capture.pcap --output report.json --format json

# CSV timeline
python spectral/spectral.py --pcap capture.pcap --output timeline.csv --format csv

# Markdown report
python spectral/spectral.py --pcap capture.pcap --output report.md --format markdown

# STIX 2.1 indicators
python spectral/spectral.py --pcap capture.pcap --export stix --output indicators.json
```

---

## Integration

### With Zeek

```bash
# Analyze Zeek logs
python spectral/spectral.py --zeek-logs /var/log/zeek/

# Export as Zeek script
python spectral/spectral.py --pcap capture.pcap --generate-zeek
```

### With Suricata

```bash
# Generate Suricata rules from detected patterns
python spectral/spectral.py --pcap capture.pcap --generate-suricata
```

### With Timesketch

```bash
# Export timeline for Timesketch
python spectral/spectral.py --pcap capture.pcap --export timesketch
```

---

## Configuration

### Config File

`~/.baudrillard/spectral.yml`:

```yaml
defaults:
  entropy_threshold: 7.0
  beacon_confidence: 0.8
  min_packets: 100

dns:
  subdomain_entropy_alert: 6.0
  txt_record_alert: true

visualization:
  theme: dark
  dpi: 150
```

### Environment Variables

```bash
export SPECTRAL_OUTPUT_DIR=/path/to/output
export SPECTRAL_VERBOSE=1
```

---

## Examples

### Incident Response Workflow

```bash
# 1. Quick triage
python spectral/spectral.py --pcap incident.pcap --quick

# 2. Focus on suspicious period
python spectral/spectral.py --pcap incident.pcap \
    --start "2026-02-05 14:00:00" \
    --end "2026-02-05 16:00:00" \
    --full-analysis

# 3. Generate IOCs
python spectral/spectral.py --pcap incident.pcap --extract-iocs --output iocs.json
```

### Threat Hunting

```bash
# Hunt for beacons across multiple captures
for pcap in /captures/*.pcap; do
    python spectral/spectral.py --pcap "$pcap" --detect-beacons --quiet
done

# Hunt for DNS tunneling
python spectral/spectral.py --pcap capture.pcap \
    --hunt "dns_tunnel" \
    --threshold 0.7
```

---

## API Usage

```python
from baudrillard.spectral import SpectralAnalyzer

# Load capture
analyzer = SpectralAnalyzer("capture.pcap")

# Run analysis
results = analyzer.analyze(
    detect_beacons=True,
    detect_tunnels=True,
    spectral=True
)

# Access results
for beacon in results.beacons:
    print(f"Beacon: {beacon.src} -> {beacon.dst}")
    print(f"  Interval: {beacon.interval}s")
    print(f"  Confidence: {beacon.confidence}")

# Export
results.to_json("report.json")
```

---

## See Also

- [Blog: Network Forensics with Spectral Decomposition](/blog/network-forensics-spectral-decomposition/)
- [Perfect-Crime](/tools/perfect-crime/) - For steganography detection
- [Ambient](/tools/ambient/) - For wireless analysis
