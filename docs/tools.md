---
layout: page
title: Tools
permalink: /tools/
---

# Baudrillard Suite Tools

Complete reference documentation for all tools in the suite.

---

## 🔴 Offensive Tools

### [Fatal - Exploit Framework](fatal/)
Object-oriented exploit development framework based on Baudrillard's "Fatal Strategies" - when objects strike back against subjects.

```bash
python fatal/fatal.py --target 192.168.1.1 --module overflow
```
**Features:** Buffer overflow generation, ROP chain builder, shellcode encoder, format string exploitation

---

### [Glitch - Fuzzer](glitch/)
Mutation-based fuzzer with entropy analysis and spectral feedback loops.

```bash
python glitch/glitch.py --input corpus/ --output crashes/ --mutations 10000
```
**Features:** Smart mutation strategies, crash deduplication, coverage-guided mode, protocol-aware fuzzing

---

### [Seduction - Social Engineering](seduction/)
Social engineering reconnaissance framework for target profiling and campaign management.

```bash
python seduction/seduction.py --target "Company Inc" --depth 3
```
**Features:** OSINT aggregation, relationship mapping, pretext generation, phishing template builder

---

### [Perfect-Crime - Steganography](perfect-crime/)
Advanced steganography toolkit for hiding data in images, audio, and network protocols.

```bash
# Hide data
python perfect-crime/perfect-crime.py hide --input secret.txt --cover image.png --output stego.png

# Extract data  
python perfect-crime/perfect-crime.py extract --input stego.png
```
**Features:** LSB encoding, DCT domain hiding, protocol steganography, detection evasion

---

## 🔵 Defensive Tools

### [Spectral - Network Forensics](spectral/)
Network forensics tool with spectral decomposition for detecting covert channels and anomalies.

```bash
python spectral/spectral.py --pcap capture.pcap --analyze
```
**Features:** 
- Spectral analysis of traffic patterns
- Covert channel detection (DNS tunneling, ICMP exfil)
- Protocol anomaly identification
- Entropy-based encrypted traffic analysis
- Timeline visualization

---

### [Transparency - OSINT Analysis](transparency/)
Exposure analysis and OSINT aggregation for understanding digital footprints.

```bash
python transparency/transparency.py --domain example.com --full
```
**Features:** Domain reconnaissance, breach data correlation, social media enumeration, metadata extraction

---

### [Ambient - Wireless Analysis](ambient/)
Wireless environment analysis and monitoring toolkit.

```bash
python ambient/ambient.py --interface wlan0 --monitor
```
**Features:** WiFi network mapping, Bluetooth enumeration, signal strength analysis, rogue AP detection

---

## 🔬 Research Tools

### Simulacra
Reality/simulation boundary testing framework.

### Hyperreal
Perception manipulation and reality augmentation research.

### Desert
Information entropy analysis in "desert of the real" environments.

### Precession
Cause-effect relationship analysis in complex systems.

---

## Installation Matrix

| Tool | pip install | Standalone | Dependencies |
|------|-------------|------------|--------------|
| Fatal | `baudrillard-fatal` | ✅ | pwntools |
| Glitch | `baudrillard-glitch` | ✅ | - |
| Spectral | `baudrillard-spectral` | ✅ | scapy, numpy |
| Perfect-Crime | `baudrillard-stego` | ✅ | pillow, numpy |
| Transparency | `baudrillard-osint` | ✅ | requests |
| Seduction | `baudrillard-social` | ✅ | requests |
| Ambient | `baudrillard-wireless` | ✅ | scapy |

---

## Platform Support

| Tool | Linux | macOS | Windows |
|------|-------|-------|---------|
| Fatal | ✅ | ✅ | ⚠️ |
| Glitch | ✅ | ✅ | ✅ |
| Spectral | ✅ | ✅ | ✅ |
| Perfect-Crime | ✅ | ✅ | ✅ |
| Transparency | ✅ | ✅ | ✅ |
| Seduction | ✅ | ✅ | ✅ |
| Ambient | ✅ | ⚠️ | ❌ |

✅ Full support | ⚠️ Partial support | ❌ Not supported
