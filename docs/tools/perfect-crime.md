---
layout: page
title: Perfect-Crime - Steganography
permalink: /tools/perfect-crime/
---

# Perfect-Crime

**Advanced steganography toolkit for hiding and detecting data in images, audio, and network protocols.**

<img src="https://img.shields.io/badge/category-steganography-purple?style=flat-square" alt="steganography">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Perfect-Crime provides both offensive (hide) and defensive (detect) steganography capabilities. Named after Baudrillard's concept of the "perfect crime" - one that leaves no trace because the evidence itself is the concealment.

**Capabilities:**
- **Hide**: Embed data in images, audio, video, and network protocols
- **Detect**: Analyze files for hidden content
- **Extract**: Retrieve hidden data from carriers
- **Multiple Methods**: LSB, DCT, spread spectrum, protocol-based

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git
pip install pillow numpy scipy

# Standalone
pip install baudrillard-stego
```

### Dependencies
- Python 3.10+
- Pillow (image processing)
- NumPy (numerical operations)
- SciPy (signal processing, optional)

---

## Quick Start

```bash
# Hide data in an image
python perfect-crime/perfect-crime.py hide \
    --data secret.txt \
    --cover image.png \
    --output stego.png

# Extract hidden data
python perfect-crime/perfect-crime.py extract \
    --input stego.png \
    --output recovered.txt

# Detect steganography
python perfect-crime/perfect-crime.py detect --input suspicious.png
```

---

## Hiding Data

### LSB (Least Significant Bit)

Classic technique - hides data in the least significant bits of pixels.

```bash
python perfect-crime/perfect-crime.py hide \
    --method lsb \
    --data secret.txt \
    --cover photo.png \
    --output hidden.png
```

**Capacity**: ~12.5% of image size (1 bit per channel per pixel)

### DCT Domain

Hides data in DCT coefficients (survives JPEG compression).

```bash
python perfect-crime/perfect-crime.py hide \
    --method dct \
    --data secret.txt \
    --cover photo.jpg \
    --output hidden.jpg
```

**Capacity**: Lower, but more robust

### Spread Spectrum

Spreads data across frequency domain - harder to detect.

```bash
python perfect-crime/perfect-crime.py hide \
    --method spread \
    --data secret.txt \
    --cover photo.png \
    --output hidden.png \
    --key "encryption_key"
```

### Audio Steganography

```bash
python perfect-crime/perfect-crime.py hide \
    --method audio-lsb \
    --data secret.txt \
    --cover audio.wav \
    --output hidden.wav
```

### Protocol Steganography

Hide data in network protocol headers/timing.

```bash
# DNS-based
python perfect-crime/perfect-crime.py hide \
    --method dns \
    --data secret.txt \
    --domain cover-domain.com \
    --output dns_queries.txt

# ICMP-based  
python perfect-crime/perfect-crime.py hide \
    --method icmp \
    --data secret.txt \
    --destination 10.0.0.1
```

---

## Extracting Data

```bash
# Basic extraction
python perfect-crime/perfect-crime.py extract \
    --input stego.png \
    --output secret.txt

# With password
python perfect-crime/perfect-crime.py extract \
    --input stego.png \
    --key "password" \
    --output secret.txt

# Auto-detect method
python perfect-crime/perfect-crime.py extract \
    --input stego.png \
    --auto
```

---

## Detecting Steganography

### Single File Analysis

```bash
python perfect-crime/perfect-crime.py detect --input suspicious.png

=== STEGANOGRAPHY ANALYSIS ===
File: suspicious.png
Size: 1,024 x 768 (2.4 MB)

LSB Analysis:
  Chi-square: 0.89 (normal: ~1.0)
  [!] LSB plane shows non-random distribution
  
Histogram Analysis:
  Pairs of adjacent values: ANOMALOUS
  [!] Characteristic "staircase" pattern detected
  
Bit Plane Analysis:
  Plane 0 entropy: 7.92 bits (expected: 7.95)
  [!] Slightly reduced entropy suggests embedded data

VERDICT: HIGH PROBABILITY of LSB steganography
Estimated hidden capacity used: ~34 KB
```

### Batch Analysis

```bash
python perfect-crime/perfect-crime.py detect \
    --directory /path/to/images/ \
    --output report.json \
    --threshold 0.7
```

### Detection Methods

| Method | Detects | Accuracy |
|--------|---------|----------|
| Chi-square | LSB embedding | High |
| RS Analysis | LSB modifications | High |
| Histogram | Value pair anomalies | Medium |
| DCT Analysis | Frequency domain hiding | Medium |
| Entropy | Compressed/encrypted data | Low-Medium |

---

## Evasion Techniques

For red team use, Perfect-Crime includes evasion features:

### Adaptive Embedding

```bash
python perfect-crime/perfect-crime.py hide \
    --method lsb \
    --adaptive \
    --data secret.txt \
    --cover photo.png \
    --output hidden.png
```

Embeds preferentially in noisy regions where changes are less detectable.

### Encryption Before Embedding

```bash
python perfect-crime/perfect-crime.py hide \
    --data secret.txt \
    --cover photo.png \
    --encrypt aes256 \
    --key "strong_password" \
    --output hidden.png
```

### Spread Across Multiple Files

```bash
python perfect-crime/perfect-crime.py hide \
    --data large_secret.zip \
    --cover-dir photos/ \
    --distribute \
    --output stego_photos/
```

---

## Capacity Calculator

```bash
python perfect-crime/perfect-crime.py capacity --input cover.png

=== CAPACITY ANALYSIS ===
File: cover.png
Dimensions: 1920 x 1080
Color depth: 24-bit RGB

Method Capacities:
  LSB-1bit:  259,200 bytes (253 KB)
  LSB-2bit:  518,400 bytes (506 KB)
  DCT:       ~50,000 bytes (49 KB)
  Spread:    ~25,000 bytes (24 KB)
  
Recommended for:
  Small files (<50KB): DCT or Spread (more secure)
  Medium files (<250KB): LSB-1bit
  Large files: LSB-2bit or multiple carriers
```

---

## Configuration

### Config File

`~/.baudrillard/perfect-crime.yml`:

```yaml
defaults:
  method: lsb
  encrypt: true
  cipher: aes256
  
detection:
  chi_threshold: 0.95
  entropy_threshold: 7.9
  
evasion:
  adaptive: true
  add_noise: false
```

---

## API Usage

```python
from baudrillard.perfect_crime import Steganographer, Detector

# Hide data
stego = Steganographer(method='lsb')
stego.hide(
    data=b"secret message",
    cover="photo.png",
    output="hidden.png",
    key="optional_password"
)

# Extract data
data = stego.extract("hidden.png", key="optional_password")

# Detect
detector = Detector()
result = detector.analyze("suspicious.png")
print(f"Stego probability: {result.probability}")
print(f"Detected method: {result.likely_method}")
```

---

## Use Cases

### Red Team: Data Exfiltration

```bash
# Compress and encrypt sensitive data
tar czf - /sensitive/data | \
    openssl enc -aes256 -pass pass:secret > data.enc

# Hide in innocent-looking images
python perfect-crime/perfect-crime.py hide \
    --data data.enc \
    --cover vacation_photo.jpg \
    --output vacation_edited.jpg

# Upload to allowed service (social media, cloud storage)
```

### Blue Team: Detection

```bash
# Scan all images in user directory
python perfect-crime/perfect-crime.py detect \
    --directory /home/user/Pictures \
    --recursive \
    --output scan_report.json

# Alert on high-probability detections
python perfect-crime/perfect-crime.py detect \
    --directory /shared/uploads \
    --threshold 0.8 \
    --alert webhook:https://siem.internal/alert
```

### Forensics: Analysis

```bash
# Deep analysis of suspect file
python perfect-crime/perfect-crime.py analyze \
    --input evidence.png \
    --deep \
    --output analysis_report/

# Try extraction with common passwords
python perfect-crime/perfect-crime.py bruteforce \
    --input evidence.png \
    --wordlist rockyou.txt
```

---

## Limitations

1. **Lossy formats**: JPEG recompression destroys LSB data
2. **Social media**: Platforms often re-encode images
3. **Capacity**: Limited by carrier file size
4. **Detection**: No steganography is truly undetectable

---

## See Also

- [Spectral](/tools/spectral/) - For protocol steganography detection
- [Transparency](/tools/transparency/) - For OSINT and exposure analysis
