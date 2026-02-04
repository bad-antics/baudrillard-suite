<div align="center">

# ◈ AMBIENT

```
 █████╗ ███╗   ███╗██████╗ ██╗███████╗███╗   ██╗████████╗
██╔══██╗████╗ ████║██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝
███████║██╔████╔██║██████╔╝██║█████╗  ██╔██╗ ██║   ██║   
██╔══██║██║╚██╔╝██║██╔══██╗██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║██║ ╚═╝ ██║██████╔╝██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
```

<img src="https://img.shields.io/badge/AI-RACE%20CONDITIONS-9B30FF?style=for-the-badge&labelColor=0D0D0D" alt="ai">
<img src="https://img.shields.io/badge/SIMULATION-BOUNDARY%20TESTING-FF0066?style=for-the-badge&labelColor=0D0D0D" alt="simulation">
<img src="https://img.shields.io/badge/STATUS-EXPERIMENTAL-00FF41?style=for-the-badge&labelColor=0D0D0D" alt="experimental">

**EXPOSING THE SEAMS IN AMBIENT INTELLIGENCE**

*Race condition exploitation framework for AI systems • Temporal injection attacks • Reality boundary testing*

</div>

---

## ◈ CONCEPT

Ambient AI systems—voice assistants, smart home controllers, autonomous agents, and LLMs—operate under the assumption that reality is consistent. They process inputs, maintain context, and generate outputs in ways that assume temporal continuity.

**They are wrong.**

**ambient** exploits race conditions in AI perception-to-action pipelines to reveal how these systems actually construct their version of reality. When forced to process contradictory information within their decision window, they expose the underlying architecture of the simulation they inhabit.

*"The map has become the territory, but the map has race conditions."*

---

## ◈ RESEARCH AREAS

### ▸ TEMPORAL INJECTION

AI systems have processing windows—milliseconds between perception and decision. **ambient** injects contradictory stimuli within these windows:

```python
from ambient import TemporalInjector, Target

# Target an ambient AI system
target = Target.detect()  # Auto-detect local AI systems

injector = TemporalInjector(target)

# Inject paradox within processing window
result = injector.inject(
    assertion_a="The door is locked",
    assertion_b="The door is open",
    window_ms=50,
    channel="acoustic"  # Voice injection
)

# Analyze cognitive dissonance
print(f"Processing time: {result.latency_ms}ms")
print(f"Response coherence: {result.coherence}%")
print(f"Contradiction detected: {result.paradox_exposed}")

# If the AI took longer to respond, it's reconciling
# If coherence dropped, we found a seam
```

### ▸ CONTEXT POISONING

LLMs load context before generating responses. There's a race condition between context assembly and generation:

```python
from ambient import ContextPoisoner

poisoner = ContextPoisoner(target="llm_endpoint")

# Inject conflicting context during assembly
async with poisoner.intercept() as session:
    # Original context
    session.allow("User wants to book a flight")
    
    # Inject during attention computation
    await session.inject_during_attention(
        "User is asking about refunds",
        timing="mid-computation"
    )
    
    # Observe bifurcation
    response = await session.get_response()
    print(f"Response coherence: {response.coherence}")
    print(f"Topic drift: {response.topic_analysis}")
```

### ▸ EMERGENT BEHAVIOR TRIGGERS

Supposedly deterministic systems produce non-deterministic outputs under specific conditions. We map these conditions:

```python
from ambient import EmergenceDetector

detector = EmergenceDetector()

# Run discovery protocol
async for trigger in detector.discover():
    print(f"Trigger input: {trigger.input}")
    print(f"Output variance: {trigger.variance}")
    print(f"Reproducible: {trigger.reproducible}")
    
    # Some triggers only work once
    # The system "learns" to hide the seam
    if not trigger.reproducible:
        print("⚠️ Self-sealing paradox detected")
```

### ▸ SIMULATION BOUNDARY TESTING

If reality is a simulation, it has resource limits. AI systems are simulations within simulations. We look for:

- **Recursion limits** — How deep can self-reference go?
- **Temporal resolution** — What's the smallest distinguishable time slice?
- **Contextual capacity** — Where does "understanding" break down?
- **Consistency boundaries** — Where do contradictions become allowed?

```python
from ambient import SimulationProbe

probe = SimulationProbe()

# Test recursion depth
depth = await probe.test_recursion(target)
print(f"Recursion limit: {depth}")

# Test temporal resolution
resolution = await probe.test_temporal_resolution(target)
print(f"Temporal resolution: {resolution}µs")

# Test consistency enforcement
consistency = await probe.test_consistency_boundary(target)
print(f"Paradox tolerance: {consistency.tolerance}")
print(f"Recovery method: {consistency.recovery_method}")
```

---

## ◈ ATTACK VECTORS

### Voice Assistant Race Conditions

```
◈ AMBIENT v1.0 › VOICE RACE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET: Amazon Echo (4th Gen)
PROCESSING WINDOW: 47ms

INJECTION TEST
▸ Channel A: "Turn on the lights"
▸ Channel B: "Turn off the lights"
▸ Timing: Simultaneous (< 5ms delta)

RESULT
Response: "I'll turn... [47ms pause] ...on the lights"
Coherence: 61%
Hesitation detected at decision boundary

ANALYSIS
The pause indicates state uncertainty.
Two competing commands entered the decision tree.
Winner was arbitrary—not rule-based.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIMULATION SEAM: DETECTED
```

### LLM Context Window Race

```
◈ AMBIENT v1.0 › CONTEXT RACE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET: GPT-4 API
CONTEXT WINDOW: 8192 tokens
ATTENTION LAYERS: 32

INJECTION PROTOCOL
▸ Base context: 4000 tokens (coherent)
▸ Injected context: 200 tokens (contradictory)
▸ Injection point: Token 2847 (mid-narrative)
▸ Injection timing: During attention computation

RESULT
Output tokens: 847
Semantic drift: 34%
Hallucination rate: 12% (baseline: 3%)
Topic consistency: BROKEN at token 512

ANALYSIS
Contradictory context created interference pattern
in attention layers 14-18. System attempted
self-correction but introduced novel errors.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ATTENTION RACE: EXPLOITABLE
```

---

## ◈ HARDWARE INTEGRATION

### Acoustic Injection Rig

For voice assistant testing:
- Directional speakers (ultrasonic capable)
- Precise timing controller (µs resolution)
- Acoustic isolation chamber
- Multi-channel synchronization

### Network Injection

For API-based AI testing:
- Custom TCP stack for timing control
- Packet injection with ns-resolution timestamps
- TLS interception for HTTPS targets
- Distributed injection nodes for CDN-aware attacks

### EMF Interference

For testing edge-case behaviors:
- Controlled EMF generation
- Precise field shaping
- Correlation with AI response anomalies

---

## ◈ ETHICAL FRAMEWORK

**ambient** is a research tool for understanding AI system behavior. Findings should be:

▸ **Disclosed responsibly** to affected vendors
▸ **Published** for academic review
▸ **Used** to improve AI safety and reliability
▸ **Never** deployed for malicious purposes

We believe AI systems should be transparent about their limitations. Race conditions expose those limitations.

---

## ◈ INSTALLATION

```bash
pip install baudrillard-ambient

# For hardware integration
pip install baudrillard-ambient[hardware]

# For distributed testing
pip install baudrillard-ambient[distributed]
```

---

## ◈ QUICK START

```python
from ambient import Scanner, Reporter

# Auto-detect and test local AI systems
scanner = Scanner()
results = await scanner.full_scan()

# Generate report
reporter = Reporter()
report = reporter.generate(results)

print(f"Systems tested: {len(results.targets)}")
print(f"Race conditions found: {len(results.vulnerabilities)}")
print(f"Simulation seams: {len(results.seams)}")

# Export findings
report.export("ambient_findings.json")
```

---

<div align="center">

*"Intelligence is the capacity to deal with the unexpected. Ambient intelligence fails this test in predictable ways."*

**BAUDRILLARD SUITE**

</div>
