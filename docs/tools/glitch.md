---
layout: page
title: Glitch - Fuzzer
permalink: /tools/glitch/
---

# Glitch

**Mutation-based fuzzer with entropy analysis and spectral feedback loops for finding crashes and vulnerabilities.**

<img src="https://img.shields.io/badge/category-fuzzing-red?style=flat-square" alt="fuzzing">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Glitch is a smart fuzzer that uses entropy analysis and spectral feedback to guide mutation strategies. Unlike dumb fuzzers that randomly mutate inputs, Glitch learns which mutations produce interesting behavior and adapts.

**Key Features:**
- Smart mutation strategies based on input structure
- Coverage-guided fuzzing with feedback loops
- Crash deduplication and root cause analysis
- Protocol-aware fuzzing for network services
- Parallel execution support
- Minimal dependencies

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git

# Standalone
pip install baudrillard-glitch
```

---

## Quick Start

```bash
# Create corpus directory with seed inputs
mkdir corpus crashes
echo "test input" > corpus/seed.txt

# Basic fuzzing
python glitch/glitch.py --input corpus/ --output crashes/ --target ./vulnerable_app

# With coverage guidance
python glitch/glitch.py --input corpus/ --output crashes/ --target ./app --coverage

# Protocol fuzzing
python glitch/glitch.py --target tcp://localhost:8080 --protocol http
```

---

## Usage

### Basic File Fuzzing

```bash
python glitch/glitch.py \
    --input corpus/ \
    --output crashes/ \
    --target ./binary \
    --iterations 100000
```

### Coverage-Guided Mode

Requires compilation with coverage instrumentation:

```bash
# Compile target with coverage
clang -fsanitize=fuzzer-no-link -fsanitize=address ./target.c -o target

# Run glitch
python glitch/glitch.py \
    --input corpus/ \
    --output crashes/ \
    --target ./target \
    --coverage \
    --sanitizer asan
```

### Network Protocol Fuzzing

```bash
# HTTP fuzzing
python glitch/glitch.py \
    --target tcp://localhost:8080 \
    --protocol http \
    --output crashes/

# Custom protocol
python glitch/glitch.py \
    --target tcp://localhost:9999 \
    --protocol-spec protocol.json \
    --output crashes/
```

### Structured Input Fuzzing

```bash
# JSON fuzzing
python glitch/glitch.py \
    --input corpus/ \
    --output crashes/ \
    --target ./json_parser \
    --format json

# XML fuzzing
python glitch/glitch.py \
    --input corpus/ \
    --output crashes/ \
    --target ./xml_parser \
    --format xml
```

---

## Mutation Strategies

Glitch uses multiple mutation strategies:

### Bit Flipping
```
Original: Hello World
Mutated:  Hdllo World (single bit flip)
```

### Byte Insertion
```
Original: Hello World
Mutated:  HelXXXlo World (byte insertion)
```

### Arithmetic Mutations
```
Original: length=100
Mutated:  length=4294967295 (integer overflow)
```

### Structure-Aware
```
Original: {"key": "value"}
Mutated:  {"key": "value", "key": "value2"} (duplicate keys)
```

### Dictionary-Based
```
# Uses known interesting values
%n%n%n%n     # format string
../../../etc/passwd  # path traversal
<script>     # XSS
```

---

## Output

### Crash Directory Structure

```
crashes/
├── crash_001_SIGSEGV_0x41414141/
│   ├── input.bin          # Crashing input
│   ├── stacktrace.txt     # Stack trace
│   ├── minimized.bin      # Minimized input
│   └── analysis.json      # Root cause analysis
├── crash_002_SIGABRT/
│   └── ...
└── hangs/
    └── hang_001/
        └── ...
```

### Statistics

```
=== GLITCH STATISTICS ===
Runtime: 01:23:45
Executions: 1,247,832
Exec/sec: 251
Coverage: 67.3% (2,341 / 3,478 edges)

Crashes: 7 (3 unique)
Hangs: 2
New paths: 847

Top mutations:
  arithmetic: 234 new paths
  bitflip: 189 new paths
  havoc: 156 new paths
```

---

## Crash Triage

### Automatic Deduplication

Glitch deduplicates crashes by:
1. Stack trace hash
2. Crash address
3. Signal type

### Minimization

```bash
# Minimize a crashing input
python glitch/glitch.py --minimize crashes/crash_001/input.bin --target ./app
```

### Root Cause Analysis

```bash
python glitch/glitch.py --analyze crashes/crash_001/

=== CRASH ANALYSIS ===
Signal: SIGSEGV
Address: 0x41414141 (controlled)
Type: Write-what-where

Stack:
  #0 strcpy() at /lib/libc.so.6
  #1 parse_input() at vulnerable.c:47
  #2 main() at vulnerable.c:12

Root Cause: Stack buffer overflow in parse_input()
Exploitability: HIGH - controlled EIP
```

---

## Configuration

### Config File

`glitch.yml`:

```yaml
mutations:
  bitflip: true
  arithmetic: true
  havoc: true
  dictionary: wordlist.txt
  
execution:
  timeout: 5000  # ms
  memory_limit: 512  # MB
  
coverage:
  type: edge
  
output:
  minimize: true
  deduplicate: true
```

### Command Line Options

```
--input DIR          Input corpus directory
--output DIR         Output directory for crashes
--target PATH        Target binary or URL
--iterations N       Number of iterations (default: unlimited)
--timeout MS         Execution timeout in milliseconds
--coverage           Enable coverage-guided fuzzing
--parallel N         Number of parallel workers
--format TYPE        Input format (raw, json, xml, http)
--dictionary FILE    Dictionary file for mutations
--minimize           Minimize crashing inputs
--analyze            Analyze crashes for root cause
```

---

## Protocol Fuzzing

### HTTP

```bash
python glitch/glitch.py \
    --target http://localhost:8080/api \
    --protocol http \
    --method POST \
    --headers "Content-Type: application/json" \
    --body-format json
```

### Custom Protocol Specification

```json
{
  "protocol": "custom",
  "fields": [
    {"name": "magic", "type": "fixed", "value": "0x1337"},
    {"name": "length", "type": "int", "size": 4},
    {"name": "data", "type": "bytes", "length_field": "length"}
  ]
}
```

---

## API Usage

```python
from baudrillard.glitch import Fuzzer, Corpus, Mutator

# Create fuzzer
fuzzer = Fuzzer(
    target="./vulnerable",
    corpus="corpus/",
    output="crashes/"
)

# Custom mutation
@fuzzer.mutator
def my_mutation(data):
    # Insert interesting value
    pos = random.randint(0, len(data))
    return data[:pos] + b"\xff\xff\xff\xff" + data[pos:]

# Run
fuzzer.run(iterations=100000)

# Check results
for crash in fuzzer.crashes:
    print(f"Crash: {crash.signal} at {crash.address}")
    print(f"Input: {crash.input_path}")
```

---

## Tips

### Creating Good Seed Corpus

1. **Variety** - Include different valid input types
2. **Edge cases** - Empty, minimal, maximal inputs
3. **Structure** - Inputs that exercise different code paths

### Improving Coverage

```bash
# Check current coverage
python glitch/glitch.py --coverage-report

# Add inputs that increase coverage
python glitch/glitch.py --corpus-minimize
```

### Parallel Fuzzing

```bash
# Use all CPU cores
python glitch/glitch.py --parallel $(nproc)

# Distributed across machines
python glitch/glitch.py --distributed --coordinator tcp://master:5000
```

---

## See Also

- [Fatal](/tools/fatal/) - For exploit development from crashes
- [Spectral](/tools/spectral/) - For network protocol analysis
