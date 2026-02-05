---
layout: page
title: Quick Start
permalink: /quickstart/
---

# Quick Start Guide

Get up and running with Baudrillard Suite in under 5 minutes.

---

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git

### Optional Dependencies
- **Scapy** - For network analysis tools (spectral, ambient)
- **Pillow** - For image steganography (perfect-crime)
- **pwntools** - For exploit development (fatal)

---

## Installation

### Option 1: Clone Repository (Recommended)

```bash
# Clone the suite
git clone https://github.com/bad-antics/baudrillard-suite.git
cd baudrillard-suite

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows

# Install core dependencies
pip install -r requirements.txt
```

### Option 2: pip Install

```bash
# Full suite
pip install baudrillard-suite

# Or individual tools
pip install baudrillard-spectral
pip install baudrillard-glitch
pip install baudrillard-fatal
```

---

## First Run Examples

### 1. Analyze a PCAP File (Spectral)

```bash
# Basic analysis
python spectral/spectral.py --pcap traffic.pcap

# Full forensic analysis with visualization
python spectral/spectral.py --pcap traffic.pcap --analyze --output report/

# Detect covert channels
python spectral/spectral.py --pcap traffic.pcap --detect-covert
```

### 2. Fuzz a Binary (Glitch)

```bash
# Create test corpus
mkdir corpus crashes
echo "seed input" > corpus/seed.txt

# Run fuzzer
python glitch/glitch.py --input corpus/ --output crashes/ --target ./vulnerable_app
```

### 3. Hide Data in an Image (Perfect-Crime)

```bash
# Encode secret message
echo "secret data" > secret.txt
python perfect-crime/perfect-crime.py hide \
    --data secret.txt \
    --cover innocent.png \
    --output hidden.png

# Decode
python perfect-crime/perfect-crime.py extract --input hidden.png
```

### 4. OSINT Reconnaissance (Transparency)

```bash
# Domain analysis
python transparency/transparency.py --domain target.com

# Full exposure analysis
python transparency/transparency.py --domain target.com --full --output report.json
```

### 5. Social Engineering Recon (Seduction)

```bash
# Target profiling
python seduction/seduction.py --target "Acme Corporation" --depth 2

# Generate pretext
python seduction/seduction.py --profile profile.json --generate-pretext
```

### 6. Wireless Environment Scan (Ambient)

```bash
# Requires monitor mode interface
sudo python ambient/ambient.py --interface wlan0mon --scan

# Passive monitoring
sudo python ambient/ambient.py --interface wlan0mon --monitor --duration 60
```

---

## Common Workflows

### Red Team: Initial Access

```bash
# 1. OSINT gathering
python transparency/transparency.py --domain target.com --output intel.json

# 2. Social engineering prep
python seduction/seduction.py --company "Target Corp" --employees

# 3. Payload development
python fatal/fatal.py --generate-payload --format exe --output payload.exe

# 4. Data exfiltration prep
python perfect-crime/perfect-crime.py template --protocol dns
```

### Blue Team: Incident Response

```bash
# 1. Capture traffic
tcpdump -i eth0 -w incident.pcap

# 2. Analyze for anomalies
python spectral/spectral.py --pcap incident.pcap --detect-all --output ir_report/

# 3. Check for stego in extracted files
python perfect-crime/perfect-crime.py detect --directory extracted_files/
```

### Research: Fuzzing Campaign

```bash
# 1. Generate initial corpus
python glitch/glitch.py --generate-corpus --format json --count 1000

# 2. Run coverage-guided fuzzing
python glitch/glitch.py \
    --input corpus/ \
    --output crashes/ \
    --target ./app \
    --coverage \
    --iterations 1000000

# 3. Analyze crashes
python glitch/glitch.py --triage crashes/
```

---

## Configuration

### Global Config File

Create `~/.baudrillard/config.yml`:

```yaml
# API Keys
shodan_key: "your-key-here"
virustotal_key: "your-key-here"
hunter_key: "your-key-here"

# Defaults
output_format: json
verbose: true
color: true

# Tool-specific
spectral:
  default_protocol: tcp
  entropy_threshold: 7.5

glitch:
  mutations_per_input: 100
  timeout: 5
```

### Environment Variables

```bash
export BAUDRILLARD_OUTPUT=/path/to/output
export BAUDRILLARD_VERBOSE=1
export SHODAN_API_KEY=your-key
```

---

## Getting Help

```bash
# Any tool
python <tool>/<tool>.py --help

# Examples
python spectral/spectral.py --help
python glitch/glitch.py --help
python fatal/fatal.py --help
```

---

## Next Steps

- Read individual [tool documentation](/tools/)
- Check out [example workflows](/examples/)
- Join [GitHub Discussions](https://github.com/bad-antics/baudrillard-suite/discussions)
- Report issues on [GitHub Issues](https://github.com/bad-antics/baudrillard-suite/issues)
