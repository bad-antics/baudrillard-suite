---
layout: page
title: Seduction - Social Engineering
permalink: /tools/seduction/
---

# Seduction

**Social engineering reconnaissance framework for target profiling, pretext generation, and campaign management.**

<img src="https://img.shields.io/badge/category-social--engineering-orange?style=flat-square" alt="social-engineering">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Seduction automates the reconnaissance phase of social engineering engagements. Based on Baudrillard's theory of seduction - the symbolic exchange that precedes and enables manipulation.

**Features:**
- OSINT aggregation from multiple sources
- Organizational structure mapping
- Employee profiling and relationship analysis
- Pretext generation based on gathered intelligence
- Phishing campaign templating
- Ethical boundaries and scope enforcement

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git

# Standalone
pip install baudrillard-social
```

### API Keys (Optional but Recommended)

```bash
export HUNTER_API_KEY="your_key"
export LINKEDIN_COOKIE="li_at=..."
export SHODAN_API_KEY="your_key"
```

---

## Quick Start

```bash
# Basic company reconnaissance
python seduction/seduction.py --target "Acme Corporation"

# Deep profile with employee mapping
python seduction/seduction.py --target "Acme Corporation" --depth 3 --employees

# Generate pretexts from gathered intel
python seduction/seduction.py --profile acme_profile.json --generate-pretexts
```

---

## Reconnaissance

### Company Profiling

```bash
python seduction/seduction.py --target "Target Company" --output profile.json

=== COMPANY PROFILE: Target Company ===

Basic Information:
  Domain: targetcompany.com
  Industry: Financial Services
  Employees: 500-1000 (LinkedIn)
  Headquarters: New York, NY
  
Online Presence:
  Website: targetcompany.com
  LinkedIn: linkedin.com/company/targetcompany
  Twitter: @TargetCompany
  Glassdoor: 3.8/5 (47 reviews)
  
Technology Stack:
  - Microsoft 365 (MX records)
  - Salesforce (subdomain)
  - AWS (IP ranges)
  - Okta (SSO discovery)
  
Recent News:
  - "Target Company announces Q4 earnings" (2 days ago)
  - "New CTO appointed at Target Company" (2 weeks ago)
```

### Employee Discovery

```bash
python seduction/seduction.py --target "Target Company" --employees --depth 2

=== EMPLOYEE DISCOVERY ===

Found 47 employees:

Leadership:
  John Smith - CEO
    Email: jsmith@targetcompany.com (verified)
    LinkedIn: linkedin.com/in/johnsmith
    Twitter: @jsmith_ceo
    
  Sarah Johnson - CTO (NEW - 2 weeks)
    Email: sjohnson@targetcompany.com (pattern)
    LinkedIn: linkedin.com/in/sarahjohnson
    Previous: TechCorp Inc (5 years)

IT Department:
  Mike Brown - IT Director
    Email: mbrown@targetcompany.com (verified)
    GitHub: github.com/mikebrown
    Interests: Kubernetes, AWS, Security
    
  [... 44 more employees ...]
```

### Relationship Mapping

```bash
python seduction/seduction.py --target "Target Company" --relationships

=== RELATIONSHIP MAP ===

External Vendors:
  - CloudProvider Inc (AWS partner)
  - SecurityCo (MSSP - mentioned in job posting)
  - LegalFirm LLP (SEC filings)

Recent Departures:
  - Amy Chen (former IT Manager) -> Now at CompetitorCo
  - Bob Davis (former Developer) -> Startup XYZ

Social Connections:
  - CEO follows: 3 board members, 2 investors
  - CTO follows: 5 tech influencers, previous colleagues
```

---

## Pretext Generation

Based on gathered intelligence, generate contextual pretexts:

```bash
python seduction/seduction.py --profile profile.json --generate-pretexts

=== GENERATED PRETEXTS ===

Pretext 1: IT Support
  Context: They use Microsoft 365 + Okta
  Scenario: "Hi, this is Mike from IT. We're rolling out a 
            security update to the Okta integration. I need 
            you to verify your credentials at this link..."
  Target: Non-technical employees
  Confidence: HIGH

Pretext 2: Vendor Inquiry  
  Context: New CTO, security vendor mentioned in job posting
  Scenario: "Congratulations on the new CTO role! I'm reaching
            out from SecurityCo regarding the security assessment
            we discussed with your predecessor..."
  Target: Sarah Johnson (new CTO)
  Confidence: MEDIUM

Pretext 3: Recruiter
  Context: Recent departures, job openings
  Scenario: "I found your profile while researching Target Company.
            I'm recruiting for a similar role at a competitor and
            wanted to discuss opportunities..."
  Target: IT staff
  Confidence: MEDIUM
```

---

## Campaign Management

### Template Creation

```bash
python seduction/seduction.py --create-template \
    --type phishing \
    --pretext "it_support" \
    --output template.html
```

### Campaign Planning

```bash
python seduction/seduction.py --plan-campaign \
    --profile profile.json \
    --targets employees.csv \
    --output campaign_plan.json

=== CAMPAIGN PLAN ===

Phase 1: Initial Contact (Week 1)
  Target: IT Department (5 people)
  Vector: LinkedIn connection requests
  Pretext: Industry networking
  
Phase 2: Relationship Building (Week 2)
  Target: Connected IT staff
  Vector: LinkedIn messages
  Content: Industry discussion, common interests
  
Phase 3: Delivery (Week 3)
  Target: Engaged contacts
  Vector: Email (using established rapport)
  Payload: Document with macro
```

---

## Ethical Boundaries

Seduction includes built-in scope enforcement:

```bash
# Define scope
python seduction/seduction.py --set-scope scope.yml

# scope.yml
scope:
  domains:
    - targetcompany.com
    - target-subsidiary.com
  exclude:
    - personal email addresses
    - family members
  authorized_by: "John Doe, Security Director"
  engagement_id: "PEN-2026-001"
  
boundaries:
  no_personal_social: true
  no_family: true
  employee_consent: required
```

Out-of-scope actions are blocked:

```bash
python seduction/seduction.py --target "employee@gmail.com"
[!] ERROR: Personal email addresses are out of scope
[!] Scope defined in: scope.yml
[!] Remove boundary or update scope to continue
```

---

## Output Formats

```bash
# JSON profile
python seduction/seduction.py --target "Company" --output profile.json

# Markdown report
python seduction/seduction.py --target "Company" --format markdown --output report.md

# CSV employee list
python seduction/seduction.py --target "Company" --employees --format csv --output employees.csv

# Maltego export
python seduction/seduction.py --target "Company" --export maltego
```

---

## API Usage

```python
from baudrillard.seduction import Profiler, PretextGenerator

# Create profile
profiler = Profiler()
profile = profiler.investigate("Target Company", depth=2)

# Access data
print(f"Domain: {profile.domain}")
print(f"Employees: {len(profile.employees)}")

for employee in profile.employees:
    print(f"  {employee.name} - {employee.role}")
    print(f"    Email: {employee.email}")
    print(f"    LinkedIn: {employee.linkedin}")

# Generate pretexts
generator = PretextGenerator()
pretexts = generator.generate(profile, count=5)

for pretext in pretexts:
    print(f"\n{pretext.name}:")
    print(f"  {pretext.scenario}")
    print(f"  Target: {pretext.target_role}")
```

---

## Data Sources

| Source | Data Type | Requires API |
|--------|-----------|--------------|
| LinkedIn | Employees, roles | Cookie |
| Hunter.io | Email patterns | Yes |
| Shodan | Technology stack | Yes |
| DNS/WHOIS | Infrastructure | No |
| GitHub | Developers, code | No |
| Glassdoor | Culture, reviews | No |
| SEC/EDGAR | Financials, leadership | No |
| Google Dorks | Documents, exposures | No |

---

## Integration

### With Gophish

```bash
# Export campaign for Gophish
python seduction/seduction.py --export gophish \
    --campaign campaign_plan.json \
    --output gophish_import.json
```

### With Cobalt Strike

```bash
# Generate Malleable C2 profile based on target's traffic
python seduction/seduction.py --generate-c2-profile \
    --profile profile.json \
    --output target.profile
```

---

## See Also

- [Transparency](/tools/transparency/) - OSINT aggregation
- [Perfect-Crime](/tools/perfect-crime/) - Data exfiltration techniques
