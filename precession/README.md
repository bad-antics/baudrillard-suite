<div align="center">

```
██████╗ ██████╗ ███████╗ ██████╗███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
██████╔╝██████╔╝█████╗  ██║     █████╗  ███████╗███████╗██║██║   ██║██╔██╗ ██║
██╔═══╝ ██╔══██╗██╔══╝  ██║     ██╔══╝  ╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║     ██║  ██║███████╗╚██████╗███████╗███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                     ◈ The Map Precedes the Territory ◈
```

<p><em>"The territory no longer precedes the map... It is the map that engenders the territory."</em></p>

<p>
  <img src="https://img.shields.io/badge/baudrillard-suite-9B30FF?style=for-the-badge" alt="suite">
  <img src="https://img.shields.io/badge/precession-threat--modeling-00FF41?style=for-the-badge" alt="precession">
  <img src="https://img.shields.io/badge/python-3.10+-FF0066?style=for-the-badge&logo=python&logoColor=white" alt="python">
</p>

**Predictive Threat Modeling - Threats that exist before they happen**

</div>

---

## 🔮 Concept

Baudrillard's "precession of simulacra" describes how models now precede reality—the map creates the territory. **Precession** applies this to threat modeling.

Traditional threat modeling: "What threats exist?"
Precession: "What threats WILL exist when we build this?"

By modeling threats before systems exist, we create threats that are born into existence with their vulnerabilities already known.

---

## ⚡ Core Philosophy

### The Precession Principle
1. **Design a system** → Model all possible threats
2. **Threats become real** → Because the system exists
3. **We predicted them** → Before they were threats
4. **The model preceded reality**

### Predictive vs Reactive

| Traditional | Precession |
|-------------|------------|
| System exists → Find threats | Model threats → System exists |
| Penetration testing | Threat anticipation |
| "What went wrong?" | "What will go wrong?" |
| Forensics | Prophecy |

---

## 🛠️ Modules

### 🔮 oracle
*Predict threats from architecture*

```bash
precession oracle --architecture system.yaml
```

- Analyzes system design before implementation
- Predicts attack vectors from components
- Generates threat timeline (what will be discovered when)
- Outputs pre-emptive mitigations

### 🌀 emergence
*Model threats that don't exist yet*

```bash
precession emergence --technology "quantum computing" --domain "finance"
```

- Projects future threat landscapes
- Models attacks using technologies that don't fully exist
- Predicts exploit development timelines
- Generates defensive R&D priorities

### 📊 territory
*Create the threat before it's real*

```bash
precession territory --target competitor.com --scope ethical
```

- Maps attack surface of target
- Predicts which vulnerabilities they'll discover
- Models their incident response
- Generates engagement timeline

### 🎯 prophecy
*Generate specific threat predictions*

```bash
precession prophecy --system production-api --horizon 90d
```

- Concrete predictions with confidence intervals
- Expected CVE timeline
- Attack probability modeling
- Defender preparation checklist

---

## 📊 Output Example

```
██████╗ ██████╗ ███████╗ ██████╗███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
[FORESEEING] The map is being drawn...

◈ THREAT PRECESSION REPORT ◈

Target: New Financial API (pre-launch)
Architecture: microservices, Kubernetes, Go backend, React frontend
Analysis Date: 2026-02-03
Prediction Horizon: 180 days post-launch

┌─────────────────────────────────────────────────────────────────────┐
│ PREDICTED THREAT TIMELINE                                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ Day 0-7: Launch                                                     │
│   → Automated scanners will find: exposed /metrics endpoint (94%)   │
│   → Expected CVE publication: none (too new)                        │
│   → Attack probability: LOW                                         │
│                                                                     │
│ Day 7-30: Discovery Phase                                           │
│   → Researchers will report: JWT algorithm confusion (78%)          │
│   → IDOR in user profile endpoint (82%)                             │
│   → Rate limiting bypass in login (67%)                             │
│   → Expected bug bounty submissions: 12-18                          │
│                                                                     │
│ Day 30-90: Weaponization                                            │
│   → PoC exploit for JWT issue (if unpatched): Day 45 ± 10           │
│   → First automated exploitation attempt: Day 60 ± 15               │
│   → Integration into exploit kits: Day 75 ± 20                      │
│                                                                     │
│ Day 90-180: Maturity                                                │
│   → Nation-state interest probability: 23%                          │
│   → Data breach probability (if no patches): 67%                    │
│   → Compliance violation discovery: 89%                             │
│                                                                     │
│ Confidence: ████████░░ 81%                                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ SPECIFIC VULNERABILITY PREDICTIONS                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ VULN-001: JWT Algorithm Confusion                                   │
│   Component:        /api/auth/verify                                │
│   Attack Vector:    Change alg:RS256 to alg:HS256                   │
│   Discovery:        Day 12 ± 5                                      │
│   CVSS Prediction:  8.1 (High)                                      │
│   Mitigation:       Hardcode algorithm, reject others               │
│   Mitigation Cost:  4 engineer-hours                                │
│                                                                     │
│ VULN-002: IDOR in Profile Endpoint                                  │
│   Component:        /api/users/{id}/profile                         │
│   Attack Vector:    Increment user ID                               │
│   Discovery:        Day 8 ± 3                                       │
│   CVSS Prediction:  6.5 (Medium)                                    │
│   Mitigation:       Verify ownership, use UUID                      │
│   Mitigation Cost:  8 engineer-hours                                │
│                                                                     │
│ VULN-003: GraphQL Introspection Exposure                            │
│   Component:        /graphql                                        │
│   Attack Vector:    Query __schema                                  │
│   Discovery:        Day 3 ± 1                                       │
│   CVSS Prediction:  4.3 (Medium)                                    │
│   Mitigation:       Disable introspection in production             │
│   Mitigation Cost:  1 engineer-hour                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PRE-EMPTIVE ACTION PLAN                                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ BEFORE LAUNCH (Total: 24 engineer-hours)                            │
│   ☐ Implement JWT algorithm pinning              [4h] [Critical]    │
│   ☐ Add ownership verification to all endpoints  [8h] [High]        │
│   ☐ Disable GraphQL introspection               [1h] [Medium]       │
│   ☐ Add anomaly detection on auth endpoints     [6h] [High]         │
│   ☐ Implement proper rate limiting              [5h] [High]         │
│                                                                     │
│ Investment: 24 hours now                                            │
│ Saves: ~340 hours incident response + reputational damage           │
│ ROI: 1,316%                                                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

◈ PROPHECY SUMMARY ◈
Predicted vulnerabilities: 7
Critical pre-launch fixes: 3
Expected CVEs prevented: 2
Breach probability reduction: 67% → 12%

"The future is already here—it's just not evenly distributed."
```

---

## 🚀 Installation

```bash
git clone https://github.com/bad-antics/precession
cd precession
pip install -e .
precession --awaken
```

---

<div align="center">
  <img src="https://img.shields.io/badge/made%20for-prophecy-9B30FF?style=for-the-badge" alt="prophecy">
  <p><em>"The model is more real than what it models."</em></p>
</div>
