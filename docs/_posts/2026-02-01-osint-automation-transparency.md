---
layout: post
title: "Automating OSINT Workflows with Transparency"
date: 2026-02-01
categories: [osint, reconnaissance]
tags: [transparency, osint, automation, reconnaissance]
author: bad-antics
---

# Automating OSINT Workflows with Transparency

Open Source Intelligence gathering is often tedious—manually querying APIs, correlating data across platforms, and documenting findings. **transparency.py** automates these workflows while maintaining operational security through proxy rotation and rate limiting.

## The OSINT Challenge

Modern investigations require data from dozens of sources:
- Domain registrars and DNS history
- Social media platforms
- Public records and breach databases
- Geolocation services
- Archive services

Manually querying each source is slow and error-prone. Automation solves this, but introduces risks:
- **Rate limiting**—Aggressive queries get blocked
- **Attribution**—Your investigation becomes visible
- **Data overload**—Too much noise, not enough signal

## Transparency's Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Target    │────▶│  Transparency │────▶│   Output    │
│  (domain,   │     │              │     │  (JSON,     │
│   email,    │     │  ┌────────┐  │     │   HTML,     │
│   person)   │     │  │Modules │  │     │   Graph)    │
└─────────────┘     │  └────────┘  │     └─────────────┘
                    │       │      │
                    │  ┌────▼────┐ │
                    │  │ Proxy   │ │
                    │  │ Rotator │ │
                    │  └─────────┘ │
                    └──────────────┘
```

## Quick Start

### Domain Investigation

```bash
# Full domain reconnaissance
python transparency.py --domain example.com --all

# Specific modules
python transparency.py --domain example.com \
    --whois --dns --subdomains --certificates --wayback
```

Output includes:
- WHOIS history and registrant changes
- Complete DNS records (A, AAAA, MX, TXT, CNAME, NS)
- Subdomain enumeration (passive + active)
- SSL certificate history
- Wayback Machine snapshots

### Email Investigation

```bash
# Investigate an email address
python transparency.py --email target@example.com --all

# Check specific sources
python transparency.py --email target@example.com \
    --breaches --social --reputation
```

### Person Investigation

```bash
# Search by name
python transparency.py --person "John Smith" --location "New York" \
    --social --records --images

# Search by username (cross-platform)
python transparency.py --username johndoe123 --platforms all
```

## Module Deep-Dives

### Subdomain Enumeration

Transparency combines multiple techniques:

```bash
# Passive enumeration (no target contact)
python transparency.py --domain example.com --subdomains --passive-only

# Active enumeration (DNS brute-force)
python transparency.py --domain example.com --subdomains \
    --wordlist ./subdomains-top1mil.txt --threads 50

# Certificate transparency logs
python transparency.py --domain example.com --subdomains --ct-logs
```

Sources queried:
- Certificate Transparency logs (crt.sh, Censys)
- DNS aggregators (SecurityTrails, VirusTotal)
- Search engine dorking
- Wayback Machine URL extraction

### Breach Database Integration

Check if credentials have been exposed:

```bash
# Check email against breach databases
python transparency.py --email user@example.com --breaches

# Check domain (all associated emails)
python transparency.py --domain example.com --breaches --domain-wide

# Output format
python transparency.py --email user@example.com --breaches --format json
```

Sample output:
```json
{
  "email": "user@example.com",
  "breaches": [
    {
      "name": "LinkedIn 2021",
      "date": "2021-06-22",
      "records": 700000000,
      "data_types": ["email", "name", "phone", "employer"]
    }
  ],
  "pastes": 3,
  "first_seen": "2019-03-15"
}
```

### Social Media Discovery

Find accounts across platforms:

```bash
# Username search
python transparency.py --username targetuser --platforms all

# Supported platforms
python transparency.py --username targetuser \
    --platforms twitter,instagram,linkedin,github,reddit,tiktok

# Include archived/deleted content
python transparency.py --username targetuser --include-archives
```

### Geolocation

Extract location data from various sources:

```bash
# IP geolocation
python transparency.py --ip 203.0.113.50 --geo

# Image EXIF extraction
python transparency.py --image photo.jpg --exif --geo

# Social media post locations
python transparency.py --username targetuser --geo-history
```

## Workflow Automation

### Custom Pipelines

Chain modules together:

```yaml
# investigation.yaml
name: "Full Target Profile"
steps:
  - module: domain
    input: ${TARGET_DOMAIN}
    output: domain_info
    
  - module: subdomains
    input: ${TARGET_DOMAIN}
    output: subdomains
    
  - module: emails
    input: ${subdomains}
    extract: "mx_records"
    output: email_addresses
    
  - module: breaches
    input: ${email_addresses}
    output: breach_data
    
  - module: social
    input: ${email_addresses}
    output: social_profiles
```

```bash
python transparency.py --pipeline investigation.yaml --var TARGET_DOMAIN=example.com
```

### Scheduled Monitoring

Track changes over time:

```bash
# Monitor domain for changes
python transparency.py --domain example.com --monitor \
    --interval 24h --alert-webhook https://slack.example.com/webhook

# Monitor person/username
python transparency.py --username targetuser --monitor \
    --interval 12h --output ./monitoring/
```

## Operational Security

### Proxy Rotation

Never query directly:

```bash
# Use proxy list
python transparency.py --domain example.com --all \
    --proxy-file ./proxies.txt --rotate-interval 10

# Tor routing
python transparency.py --domain example.com --all --tor

# Commercial proxy service
python transparency.py --domain example.com --all \
    --proxy-api "https://proxy.example.com/api?key=${KEY}"
```

### Rate Limiting

Avoid detection and bans:

```bash
# Conservative rate limiting
python transparency.py --domain example.com --all \
    --rate-limit 1/s --jitter 0.5

# Per-source limits
python transparency.py --domain example.com --all \
    --rate-config ./rate_limits.yaml
```

### Identity Separation

```bash
# Use separate API keys per investigation
python transparency.py --domain example.com --all \
    --config ./investigation_001/config.yaml

# Randomize user agents
python transparency.py --domain example.com --all --random-ua
```

## Output and Visualization

### Report Generation

```bash
# HTML report
python transparency.py --domain example.com --all \
    --report html --output report.html

# Markdown (for documentation)
python transparency.py --domain example.com --all \
    --report markdown --output findings.md

# JSON (for processing)
python transparency.py --domain example.com --all \
    --report json --output data.json
```

### Graph Visualization

Visualize entity relationships:

```bash
# Generate relationship graph
python transparency.py --domain example.com --all \
    --graph --output network.html

# Export for Maltego
python transparency.py --domain example.com --all \
    --export maltego --output entities.mtgx

# Export for Neo4j
python transparency.py --domain example.com --all \
    --export neo4j --neo4j-uri bolt://localhost:7687
```

## API Integration

Use Transparency programmatically:

```python
from transparency import Investigator

inv = Investigator(config_path="./config.yaml")

# Domain investigation
domain_data = inv.investigate_domain("example.com", modules=[
    "whois", "dns", "subdomains", "certificates"
])

# Email investigation
email_data = inv.investigate_email("user@example.com", modules=[
    "breaches", "social", "reputation"
])

# Correlate findings
graph = inv.build_graph([domain_data, email_data])
graph.export("network.json")
```

## Practical Example: Corporate Reconnaissance

```bash
# 1. Map the target's digital footprint
python transparency.py --domain target-corp.com --all \
    --output ./recon/phase1/ --format json

# 2. Extract employee emails from LinkedIn
python transparency.py --company "Target Corp" --linkedin \
    --output ./recon/employees.json

# 3. Check employees against breach databases
python transparency.py --email-list ./recon/employees.json --breaches \
    --output ./recon/breaches.json

# 4. Find personal accounts linked to work emails
python transparency.py --email-list ./recon/employees.json --social \
    --output ./recon/social.json

# 5. Generate comprehensive report
python transparency.py --aggregate ./recon/ \
    --report html --output ./recon/final_report.html
```

## Conclusion

OSINT automation transforms hours of manual research into minutes of structured data collection. Transparency provides the framework while maintaining operational discipline through proxy rotation, rate limiting, and identity separation.

Remember:
1. **Passive first**—Exhaust non-contact sources before active enumeration
2. **Document everything**—Reproducibility matters for legal proceedings
3. **Respect boundaries**—OSINT ≠ hacking; stay within legal limits
4. **Verify findings**—Automated tools make mistakes; validate critical data

---

*Learn more: [Transparency Documentation](/baudrillard-suite/tools/transparency)*
