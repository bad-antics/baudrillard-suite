---
layout: page
title: Transparency - OSINT
permalink: /tools/transparency/
---

# Transparency

**OSINT aggregation and exposure analysis for understanding digital footprints.**

<img src="https://img.shields.io/badge/category-osint-blue?style=flat-square" alt="osint">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Transparency aggregates open-source intelligence from multiple sources to reveal the complete digital footprint of a target. Named after Baudrillard's concept of "the transparency of evil" - in the hyperreal world, everything is visible yet nothing is seen.

**Features:**
- Domain and infrastructure reconnaissance
- Email and credential breach checking
- Social media enumeration
- Document and metadata extraction
- Technology stack identification
- Historical data via web archives

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git

# Standalone
pip install baudrillard-osint
```

### API Keys (Enhance Capabilities)

```bash
export SHODAN_API_KEY="your_key"
export HUNTER_API_KEY="your_key"
export VIRUSTOTAL_API_KEY="your_key"
export SECURITYTRAILS_API_KEY="your_key"
```

---

## Quick Start

```bash
# Domain reconnaissance
python transparency/transparency.py --domain example.com

# Full analysis
python transparency/transparency.py --domain example.com --full --output report/

# Person search
python transparency/transparency.py --person "John Smith" --location "New York"
```

---

## Domain Intelligence

### Basic Scan

```bash
python transparency/transparency.py --domain target.com

=== DOMAIN INTELLIGENCE: target.com ===

Registration:
  Registrar: GoDaddy
  Created: 2010-03-15
  Expires: 2026-03-15
  
DNS Records:
  A:     93.184.216.34
  MX:    mail.target.com (10)
  TXT:   v=spf1 include:_spf.google.com ~all
  NS:    ns1.target.com, ns2.target.com
  
Infrastructure:
  IP: 93.184.216.34
  ASN: AS15133 (Edgecast)
  Location: Los Angeles, US
  
Technology:
  Web Server: nginx/1.18
  Framework: React (detected)
  CDN: Cloudflare
  Email: Google Workspace
```

### Subdomain Enumeration

```bash
python transparency/transparency.py --domain target.com --subdomains

=== SUBDOMAINS ===

Found 47 subdomains:

Active:
  www.target.com        93.184.216.34
  mail.target.com       93.184.216.35
  api.target.com        93.184.216.36
  dev.target.com        93.184.216.37  [!] Development
  staging.target.com    93.184.216.38  [!] Staging
  admin.target.com      93.184.216.39  [!] Admin panel
  vpn.target.com        93.184.216.40
  
Historical (no longer resolving):
  old.target.com        (last seen: 2024-01)
  beta.target.com       (last seen: 2023-06)
```

### Certificate Transparency

```bash
python transparency/transparency.py --domain target.com --certificates

=== CERTIFICATE TRANSPARENCY ===

Current Certificates:
  *.target.com (Let's Encrypt, expires 2026-04-01)
  
Historical Certificates (CT Logs):
  2025-01: internal.target.com
  2024-06: test.target.com
  2024-01: dev-api.target.com
  
[!] Discovered via CT logs: 12 additional subdomains
```

---

## Email Intelligence

### Email Discovery

```bash
python transparency/transparency.py --domain target.com --emails

=== EMAIL DISCOVERY ===

Pattern: {first}.{last}@target.com (confidence: 89%)

Discovered Emails:
  john.smith@target.com     (LinkedIn)
  sarah.jones@target.com    (GitHub commit)
  admin@target.com          (WHOIS history)
  support@target.com        (Website)
  
Verification:
  john.smith@target.com  -> VALID (SMTP check)
  admin@target.com       -> VALID
```

### Breach Check

```bash
python transparency/transparency.py --email john@target.com --breaches

=== BREACH CHECK ===

john@target.com found in 3 breaches:

1. LinkedIn (2012)
   Data: Email, Password (SHA1)
   
2. Adobe (2013)
   Data: Email, Password (3DES)
   
3. Collection #1 (2019)
   Data: Email, Password (plaintext)
   
[!] HIGH RISK: Credentials likely compromised
[!] Check: haveibeenpwned.com for latest
```

---

## Social Media

### Profile Discovery

```bash
python transparency/transparency.py --username johndoe --social

=== SOCIAL MEDIA PROFILES ===

Confirmed:
  Twitter:    @johndoe (12.3k followers)
  LinkedIn:   linkedin.com/in/johndoe
  GitHub:     github.com/johndoe (47 repos)
  Instagram:  @johndoe_official
  
Possible (same username):
  Reddit:     u/johndoe
  HackerNews: johndoe
  Medium:     @johndoe
  
Cross-references:
  - Twitter bio links to GitHub ✓
  - LinkedIn photo matches Twitter ✓
```

### Content Analysis

```bash
python transparency/transparency.py --username johndoe --analyze-content

=== CONTENT ANALYSIS ===

Posting Patterns:
  Most active: Weekdays 9am-6pm EST
  Peak day: Wednesday
  
Topics:
  - Cybersecurity (34%)
  - Cloud computing (28%)
  - Python programming (18%)
  - Other (20%)
  
Connections:
  Frequently interacts with: @securityvendor, @cloudcompany
  Mentioned employers: TechCorp Inc, StartupXYZ
```

---

## Document Discovery

### Google Dorking

```bash
python transparency/transparency.py --domain target.com --documents

=== DOCUMENT DISCOVERY ===

Found 23 documents:

PDFs:
  /docs/annual_report_2025.pdf  (2.3 MB)
  /files/employee_handbook.pdf  (890 KB)  [!] Internal
  
Office Documents:
  /shared/budget_2025.xlsx      (156 KB)  [!] Financial
  /docs/org_chart.pptx          (1.1 MB)  [!] Structure
  
Other:
  /backup/db_dump.sql           (45 MB)   [!] DATABASE
  /.git/config                  (234 B)   [!] Git exposed
```

### Metadata Extraction

```bash
python transparency/transparency.py --file document.pdf --metadata

=== METADATA ===

File: document.pdf

Creation:
  Author: John Smith
  Creator: Microsoft Word 2019
  Created: 2025-12-15 14:32:00
  Modified: 2025-12-16 09:15:00
  
Software:
  Producer: Adobe PDF Library 15.0
  
Hidden Data:
  - Previous authors: Sarah Jones, Mike Brown
  - Revision count: 7
  - Total edit time: 4h 32m
  - Printer: HP LaserJet 4th Floor
```

---

## Historical Data

### Wayback Machine

```bash
python transparency/transparency.py --domain target.com --historical

=== HISTORICAL DATA ===

Wayback Machine Snapshots: 234

Interesting Changes:
  2024-06: Admin panel URL changed
  2024-01: Contact page added new email
  2023-08: Employee directory removed [!]
  2023-01: Old login page (potentially vulnerable)
  
Retrieved historical data:
  - 15 email addresses (no longer on site)
  - 3 removed subdomains
  - Previous technology stack (PHP -> React migration)
```

---

## Output Formats

```bash
# JSON
python transparency/transparency.py --domain target.com --output report.json

# Markdown
python transparency/transparency.py --domain target.com --format markdown --output report.md

# HTML
python transparency/transparency.py --domain target.com --format html --output report.html

# CSV (for specific modules)
python transparency/transparency.py --domain target.com --emails --format csv
```

---

## API Usage

```python
from baudrillard.transparency import Investigator

# Create investigator
inv = Investigator()

# Domain investigation
domain_intel = inv.investigate_domain("target.com")
print(f"Subdomains: {domain_intel.subdomains}")
print(f"Technologies: {domain_intel.technologies}")
print(f"Emails: {domain_intel.emails}")

# Person investigation
person = inv.investigate_person("John Smith", location="New York")
print(f"Profiles: {person.social_profiles}")
print(f"Breaches: {person.breaches}")

# Export
domain_intel.to_json("report.json")
```

---

## Configuration

### Rate Limiting

```yaml
# ~/.baudrillard/transparency.yml
rate_limits:
  default: 1  # requests per second
  shodan: 1
  hunter: 2
  google: 0.5

proxies:
  enabled: true
  list:
    - socks5://127.0.0.1:9050  # Tor
    - http://proxy1:8080
```

### Custom Sources

```python
from baudrillard.transparency import Investigator, Source

class MyCustomSource(Source):
    def query(self, target):
        # Custom logic
        return results

inv = Investigator()
inv.add_source(MyCustomSource())
```

---

## See Also

- [Seduction](/tools/seduction/) - For social engineering reconnaissance
- [Spectral](/tools/spectral/) - For network-based intelligence
