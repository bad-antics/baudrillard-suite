---
layout: page
title: Ambient - Wireless Analysis
permalink: /tools/ambient/
---

# Ambient

**Wireless environment analysis and monitoring toolkit for WiFi, Bluetooth, and RF signals.**

<img src="https://img.shields.io/badge/category-wireless-green?style=flat-square" alt="wireless">
<img src="https://img.shields.io/badge/platform-linux-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Ambient provides passive wireless reconnaissance and environment mapping. Named after Baudrillard's concept of ambient power - the invisible forces that shape behavior without explicit control.

**Features:**
- WiFi network discovery and analysis
- Bluetooth/BLE device enumeration
- Client device tracking
- Rogue access point detection
- Signal strength mapping
- Historical pattern analysis

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git
pip install scapy

# Standalone
pip install baudrillard-wireless
```

### Requirements
- Linux (monitor mode required)
- Wireless adapter supporting monitor mode
- Root privileges

### Supported Adapters
- Alfa AWUS036ACH
- Alfa AWUS036ACM
- TP-Link Archer T2U Plus
- Most Atheros/Ralink chipsets

---

## Quick Start

```bash
# Enable monitor mode
sudo python ambient/ambient.py --interface wlan0 --monitor-mode

# Basic WiFi scan
sudo python ambient/ambient.py --interface wlan0mon --scan

# Continuous monitoring
sudo python ambient/ambient.py --interface wlan0mon --monitor --duration 3600
```

---

## WiFi Analysis

### Network Discovery

```bash
sudo python ambient/ambient.py --interface wlan0mon --scan

=== WiFi NETWORKS ===

SSID                    BSSID              CH  ENC     SIGNAL  CLIENTS
--------------------------------------------------------------------------------
CorporateWiFi           AA:BB:CC:11:22:33  6   WPA2    -45dBm  23
GuestNetwork            AA:BB:CC:11:22:34  6   WPA2    -48dBm  7
NETGEAR-5G              DD:EE:FF:44:55:66  36  WPA2    -62dBm  3
linksys                 11:22:33:44:55:66  11  WEP     -71dBm  1  [!] WEAK
HiddenNetwork           (hidden)           1   WPA2    -55dBm  5

Total: 47 networks | 2.4GHz: 31 | 5GHz: 16
```

### Detailed Network Analysis

```bash
sudo python ambient/ambient.py --interface wlan0mon --target "CorporateWiFi"

=== NETWORK ANALYSIS: CorporateWiFi ===

Access Points:
  AA:BB:CC:11:22:33  CH 6   -45dBm  (primary)
  AA:BB:CC:11:22:44  CH 6   -52dBm  (secondary)
  AA:BB:CC:11:22:55  CH 11  -61dBm  (tertiary)

Security:
  Encryption: WPA2-Enterprise
  Authentication: 802.1X (EAP-TLS likely)
  PMF: Required
  
Vendor: Cisco Systems

Connected Clients: 23
  - Apple devices: 12
  - Windows: 8
  - Android: 3
  
Traffic Analysis:
  Peak usage: 14:00-16:00
  Avg throughput: 45 Mbps
```

### Client Tracking

```bash
sudo python ambient/ambient.py --interface wlan0mon --clients

=== CLIENT DEVICES ===

MAC                 VENDOR          SIGNAL  ASSOCIATED TO       PROBES
--------------------------------------------------------------------------------
AA:11:22:33:44:55   Apple           -42dBm  CorporateWiFi       -
BB:22:33:44:55:66   Samsung         -55dBm  GuestNetwork        HomeWiFi, Hotel
CC:33:44:55:66:77   Intel           -61dBm  (not associated)    CoffeeShop, Airport
DD:44:55:66:77:88   Apple           -48dBm  CorporateWiFi       -

[!] Device CC:33:44:55:66:77 probing for: CoffeeShop, Airport_Free, Hotel_Guest
```

### Probe Request Analysis

```bash
sudo python ambient/ambient.py --interface wlan0mon --probes

=== PROBE REQUESTS ===

Top Probed SSIDs:
  1. xfinitywifi          (847 probes, 23 devices)
  2. ATT-WiFi             (654 probes, 18 devices)
  3. Starbucks            (432 probes, 31 devices)
  4. CorporateWiFi        (398 probes, 45 devices)
  5. Hotel_Guest          (287 probes, 12 devices)
  
Device Movement Patterns:
  Device AA:11:22:33:44:55:
    08:00 - Probed: HomeWiFi
    09:15 - Probed: Starbucks, CoffeeShop
    09:45 - Associated: CorporateWiFi
    18:30 - Probed: GymWiFi
```

---

## Bluetooth/BLE Analysis

```bash
sudo python ambient/ambient.py --interface hci0 --bluetooth

=== BLUETOOTH DEVICES ===

Classic Bluetooth:
  AA:BB:CC:DD:EE:FF   "John's AirPods"      Audio       -52dBm
  11:22:33:44:55:66   "Bose QC35"           Audio       -61dBm
  
BLE (Low Energy):
  AA:BB:CC:DD:EE:00   Apple Watch           Wearable    -45dBm
  BB:CC:DD:EE:FF:11   Tile Tracker          Tracker     -72dBm
  CC:DD:EE:FF:00:22   Unknown               Unknown     -68dBm
  
[!] BLE device CC:DD:EE:FF:00:22 advertising suspicious services
```

---

## Rogue AP Detection

```bash
sudo python ambient/ambient.py --interface wlan0mon --rogue-detect

=== ROGUE AP DETECTION ===

Baseline loaded: corporate_networks.yml

[!] ALERT: Rogue AP Detected!
    SSID: CorporateWiFi (matches legitimate)
    BSSID: XX:YY:ZZ:11:22:33 (UNKNOWN)
    Channel: 11 (legitimate on 6)
    Encryption: WPA2-PSK (legitimate uses WPA2-Enterprise)
    Signal: -35dBm (unusually strong)
    
    Assessment: EVIL TWIN ATTACK (HIGH CONFIDENCE)
    
[!] ALERT: Suspicious AP
    SSID: Free_CorporateWiFi
    Similar to: CorporateWiFi
    Assessment: POSSIBLE PHISHING AP
```

---

## Signal Mapping

```bash
# Generate heatmap
sudo python ambient/ambient.py --interface wlan0mon \
    --heatmap \
    --target "CorporateWiFi" \
    --output heatmap.html

# Walk survey mode
sudo python ambient/ambient.py --interface wlan0mon \
    --survey \
    --gps /dev/ttyUSB0 \
    --output survey_data.csv
```

---

## Continuous Monitoring

```bash
# Monitor with alerting
sudo python ambient/ambient.py --interface wlan0mon \
    --monitor \
    --duration 86400 \
    --alert-webhook https://slack.webhook/xxx \
    --baseline corporate_baseline.yml

# Alerts on:
# - New networks appearing
# - Rogue APs
# - Deauth attacks
# - Unusual client behavior
```

---

## Output Formats

```bash
# JSON
sudo python ambient/ambient.py --interface wlan0mon --scan --output scan.json

# CSV
sudo python ambient/ambient.py --interface wlan0mon --clients --format csv

# Kismet compatible
sudo python ambient/ambient.py --interface wlan0mon --export kismet

# Wigle compatible
sudo python ambient/ambient.py --interface wlan0mon --export wigle
```

---

## API Usage

```python
from baudrillard.ambient import WirelessScanner

# Create scanner
scanner = WirelessScanner(interface="wlan0mon")

# Scan networks
networks = scanner.scan(duration=30)
for net in networks:
    print(f"{net.ssid}: {net.signal_strength}dBm")
    print(f"  Clients: {len(net.clients)}")

# Monitor for events
def on_new_client(client):
    print(f"New client: {client.mac}")

scanner.monitor(
    duration=3600,
    on_new_client=on_new_client,
    on_deauth=lambda e: print(f"Deauth attack: {e}")
)
```

---

## Configuration

```yaml
# ~/.baudrillard/ambient.yml
interface:
  default: wlan0
  monitor_mode: auto

scanning:
  hop_interval: 0.5  # seconds per channel
  channels: [1, 6, 11, 36, 40, 44, 48]  # 2.4 + 5 GHz

alerts:
  rogue_ap: true
  deauth_threshold: 10  # packets/min
  webhook: https://hooks.slack.com/xxx

baseline:
  corporate_ssids:
    - CorporateWiFi
    - GuestNetwork
  corporate_bssids:
    - AA:BB:CC:*
```

---

## Security Considerations

⚠️ **Legal Notice**: Wireless monitoring may be subject to local laws. Ensure you have authorization before scanning networks you don't own.

- Only scan networks you own or have explicit permission to test
- Passive monitoring is generally legal; active attacks are not
- Some jurisdictions require consent for client tracking
- Corporate environments should have documented policies

---

## See Also

- [Spectral](/tools/spectral/) - For wired network analysis
- [Transparency](/tools/transparency/) - For correlating wireless with OSINT
