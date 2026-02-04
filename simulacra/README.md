<div align="center">

# ◈ SIMULACRA

```
███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗  ██████╗██████╗  █████╗ 
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
███████╗██║██╔████╔██║██║   ██║██║     ███████║██║     ██████╔╝███████║
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║██║     ██╔══██╗██╔══██║
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║╚██████╗██║  ██║██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

<img src="https://img.shields.io/badge/PROCESS-AUTHENTICATION-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="process">
<img src="https://img.shields.io/badge/ONTOLOGICAL-ANALYSIS-FF0066?style=for-the-badge&labelColor=0D0D0D" alt="ontological">
<img src="https://img.shields.io/badge/ROOTKIT-DETECTION-00FF41?style=for-the-badge&labelColor=0D0D0D" alt="rootkit">

**DETECTING COPIES WITHOUT ORIGINALS**

*Ontological process verification • Genealogical tracing • Temporal drift analysis • Order classification*

</div>

---

## ◈ CONCEPT

Baudrillard argued that in hyperreality, the distinction between original and copy becomes meaningless—there are only simulacra: copies without originals. In computing, this manifests as processes that shouldn't exist. Rootkits, injected code, hijacked threads—all are simulacra.

**simulacra** performs ontological analysis on running processes. It doesn't just ask "is this process malicious?" It asks "does this process have a right to exist?"

*"The simulacrum is never what hides the truth—it is truth that hides the fact that there is none."*

---

## ◈ ORDERS OF SIMULACRA

Baudrillard defined four orders of simulacra. We apply them to process analysis:

| Order | Description | Computing Equivalent |
|:------|:------------|:---------------------|
| **1st Order** | Faithful copy of reality | Legitimate process, proper chain |
| **2nd Order** | Copy that masks reality | Process hiding its true purpose |
| **3rd Order** | Copy with no original | Injected code, hijacked thread |
| **4th Order** | Fractal, self-referential | Self-modifying malware, AI payloads |

---

## ◈ ANALYSIS METHODS

### ▸ GENEALOGICAL TRACING

Every legitimate process has a birth story. **simulacra** traces this lineage:

```python
from simulacra import ProcessAnalyzer

analyzer = ProcessAnalyzer()

# Trace genealogy of a process
genealogy = analyzer.trace_genealogy(pid=3847)

print(f"Process: {genealogy.name}")
print(f"Parent chain: {' → '.join(genealogy.ancestors)}")
print(f"Birth method: {genealogy.spawn_method}")
print(f"Legitimacy: {genealogy.legitimacy_score}%")

if genealogy.paradox_detected:
    print(f"⚠️ PARADOX: {genealogy.paradox_description}")
```

### ▸ ONTOLOGICAL SCANNING

Full system scan questioning the existence of every process:

```python
from simulacra import OntologicalScanner

scanner = OntologicalScanner()

# Question reality
async for result in scanner.question_reality():
    if result.order > 1:
        print(f"▸ {result.pid} › {result.name}")
        print(f"  Order: {result.order} ({result.order_name})")
        print(f"  Authenticity: {result.authenticity}%")
        print(f"  Drift: {result.temporal_drift}")
```

### ▸ TEMPORAL DRIFT ANALYSIS

Processes exist in time. Their timestamps should be consistent. **simulacra** detects temporal violations:

```python
from simulacra import TemporalAnalyzer

temporal = TemporalAnalyzer()

anomalies = temporal.detect_drift()

for a in anomalies:
    print(f"▸ PID {a.pid}: {a.name}")
    print(f"  Expected start: {a.expected_start}")
    print(f"  Actual start: {a.actual_start}")
    print(f"  Drift: {a.drift_seconds}s")
    print(f"  Explanation: {a.explanation}")
```

### ▸ MEMORY AUTHENTICITY

Compare process memory against known-good binaries:

```python
from simulacra import MemoryVerifier

verifier = MemoryVerifier()

for process in verifier.scan_all():
    if process.modified_sections:
        print(f"▸ {process.name} [{process.pid}]")
        for section in process.modified_sections:
            print(f"  Section: {section.name}")
            print(f"  Expected hash: {section.expected_hash[:16]}...")
            print(f"  Actual hash: {section.actual_hash[:16]}...")
            print(f"  Modification: {section.modification_type}")
```

---

## ◈ SAMPLE OUTPUT

```
◈ SIMULACRA v2.0 › ONTOLOGICAL SCAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTIONING REALITY...

▸ PID 1 › systemd
  Order: 1st (AUTHENTIC)
  Genealogy: GENESIS (init)
  Authenticity ██████████ 100%
  Drift: NONE

▸ PID 847 › sshd
  Order: 1st (AUTHENTIC)
  Genealogy: systemd → sshd
  Authenticity ██████████ 99%
  Drift: NONE

▸ PID 2341 › nginx
  Order: 2nd (MASKED)
  Genealogy: systemd → nginx
  Authenticity ████████░░ 78%
  Drift: LOW
  Note: Memory section .text differs from binary

▸ PID 3392 › kworker/0:1  ⚠️ ALERT
  Order: 3rd (SIMULACRUM)
  Genealogy: PARADOX
  Authenticity ███░░░░░░░ 31%
  Parent PID 2 never spawned this thread
  Temporal anomaly: Start time predates parent
  ROOTKIT PROBABILITY: HIGH

▸ PID 4501 › chrome-helper
  Order: 4th (FRACTAL)
  Genealogy: chrome → helper (self-spawned recursively)
  Authenticity ████████░░ 82%
  Self-reference detected in memory
  Pattern: Benign (browser behavior)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCESSES: 247 • AUTHENTIC: 243 • SIMULACRA: 3 • ALERT: 1
REALITY INTEGRITY: 98.8%
```

---

## ◈ DESKTOP APPLICATION

Native Tauri app with:
- Real-time process tree visualization
- Authenticity heat map
- Genealogy graph explorer
- Alert notifications
- Historical analysis

---

## ◈ INTEGRATION

### With hyperreal

Deep memory forensics on suspicious processes:

```python
from simulacra import OntologicalScanner
from hyperreal import MemoryForensics

scanner = OntologicalScanner()
forensics = MemoryForensics()

for process in scanner.question_reality():
    if process.order >= 3:
        # Deep analysis
        deep = await forensics.analyze(process.pid)
        print(f"Palimpsest layers: {deep.palimpsest_count}")
        print(f"Hidden code: {deep.hidden_code_detected}")
```

### With cool-memories

Immutable logging of detections:

```python
from simulacra import OntologicalScanner
from cool_memories import ImmutableLog

log = ImmutableLog()
scanner = OntologicalScanner()

async for detection in scanner.question_reality():
    if detection.order >= 2:
        await log.record(
            event_type="simulacrum_detected",
            data=detection.to_dict(),
            severity="high" if detection.order >= 3 else "medium"
        )
```

---

## ◈ INSTALLATION

```bash
pip install baudrillard-simulacra

# Desktop app
cd apps/simulacra-desktop
npm install && npm run tauri build
```

---

<div align="center">

*"The map precedes the territory—sometimes the process precedes itself."*

**BAUDRILLARD SUITE**

</div>
