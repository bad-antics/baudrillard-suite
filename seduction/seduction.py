#!/usr/bin/env python3
"""
SEDUCTION - Social Engineering Phrase Generator
================================================
"Seduction is always more singular and sublime than sex."
— Jean Baudrillard

Generates persuasive text using psychological principles.
Creates compelling social engineering templates.
"""

import os
import sys
import random
import argparse
import json
from datetime import datetime

BANNER = """
███████╗███████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗█████╗  ██║  ██║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██╔══╝  ██║  ██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
███████║███████╗██████╔╝╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
          [ SOCIAL ENGINEERING TOOLKIT | baudrillard-suite ]
"""

class SeductionEngine:
    """Generate persuasive social engineering content"""
    
    def __init__(self):
        self.principles = {
            'urgency': [
                "Your immediate attention is required",
                "Time-sensitive action needed",
                "This expires in 24 hours",
                "Act now before it's too late",
                "Limited time opportunity"
            ],
            'authority': [
                "As per company policy",
                "The IT department requires",
                "Management has requested",
                "Per security guidelines",
                "Executive mandate"
            ],
            'scarcity': [
                "Only a few spots remaining",
                "Exclusive access for select users",
                "Limited availability",
                "While supplies last",
                "Rare opportunity"
            ],
            'social_proof': [
                "Other team members have already",
                "Most employees prefer",
                "Join the majority who",
                "As recommended by peers",
                "Following industry best practices"
            ],
            'reciprocity': [
                "In return for your cooperation",
                "To thank you for your time",
                "As a gesture of appreciation",
                "We'd like to offer you",
                "Your help will be rewarded"
            ],
            'liking': [
                "We value your contributions",
                "Your expertise is appreciated",
                "As a valued member",
                "We've noticed your dedication",
                "Your input matters"
            ]
        }
        
        self.templates = {
            'phishing': {
                'subject_lines': [
                    "Action Required: Account Security Update",
                    "Important: Verify Your Information",
                    "Your Session Has Expired",
                    "Unusual Activity Detected",
                    "Document Shared With You"
                ],
                'openings': [
                    "We noticed unusual activity on your account.",
                    "Your password is scheduled to expire.",
                    "A document requires your review and signature.",
                    "Your account has been temporarily limited.",
                    "Please verify your identity to continue."
                ],
                'calls_to_action': [
                    "Click here to verify your account",
                    "Review the document now",
                    "Confirm your identity",
                    "Update your credentials",
                    "Secure your account"
                ]
            },
            'vishing': {
                'openings': [
                    "Hello, this is {name} from IT support.",
                    "Good afternoon, I'm calling from the help desk.",
                    "Hi, this is the security team following up.",
                    "Hello, we're conducting a system audit.",
                    "This is {name} from corporate security."
                ],
                'pretexts': [
                    "We've detected a security issue with your workstation.",
                    "Your computer has been flagged for a mandatory update.",
                    "We need to verify your credentials for the new system.",
                    "There's been unauthorized access to your account.",
                    "We're rolling out new security measures."
                ]
            },
            'pretexting': {
                'roles': [
                    "IT Support Technician",
                    "Security Auditor", 
                    "Vendor Representative",
                    "New Employee",
                    "Building Maintenance"
                ],
                'scenarios': [
                    "Scheduled maintenance check",
                    "Emergency repair needed",
                    "Compliance audit in progress",
                    "Equipment delivery/pickup",
                    "Fire safety inspection"
                ]
            }
        }
        
    def generate_phishing_email(self, target_company="Company", target_name="User"):
        """Generate a phishing email template"""
        subject = random.choice(self.templates['phishing']['subject_lines'])
        opening = random.choice(self.templates['phishing']['openings'])
        urgency = random.choice(self.principles['urgency'])
        authority = random.choice(self.principles['authority'])
        cta = random.choice(self.templates['phishing']['calls_to_action'])
        
        email = f"""
Subject: {subject}

Dear {target_name},

{opening}

{authority}, {urgency.lower()}.

{random.choice(self.principles['social_proof'])}.

[{cta}]

{random.choice(self.principles['reciprocity'])}.

Best regards,
{target_company} Security Team

---
This is an automated message. Do not reply.
        """
        return email.strip()
        
    def generate_vishing_script(self, caller_name="John"):
        """Generate a vishing (voice phishing) script"""
        opening = random.choice(self.templates['vishing']['openings']).format(name=caller_name)
        pretext = random.choice(self.templates['vishing']['pretexts'])
        
        script = f"""
VISHING SCRIPT
==============

OPENING:
"{opening}"

PRETEXT:
"{pretext}"

BUILD RAPPORT:
- "{random.choice(self.principles['liking'])}"
- Reference specific details about their role/department

CREATE URGENCY:
- "{random.choice(self.principles['urgency'])}"
- Mention potential consequences

ESTABLISH AUTHORITY:
- "{random.choice(self.principles['authority'])}"
- Use technical jargon appropriately

REQUEST:
"I'll need you to [specific action] so we can resolve this quickly."

OBJECTION HANDLING:
- "I completely understand your concern..."
- "Let me give you our ticket number: [fake number]"
- "Feel free to call the help desk to verify, but this is urgent..."

CLOSING:
"Thank you for your cooperation. This will help keep everyone secure."
        """
        return script.strip()
        
    def generate_pretext_scenario(self):
        """Generate a physical social engineering scenario"""
        role = random.choice(self.templates['pretexting']['roles'])
        scenario = random.choice(self.templates['pretexting']['scenarios'])
        
        pretext = f"""
PRETEXT SCENARIO
================

ROLE: {role}
SCENARIO: {scenario}

APPEARANCE:
- Appropriate uniform/attire for role
- Visible ID badge (can be fake/borrowed)
- Relevant props (clipboard, toolbox, laptop bag)

ENTRY APPROACH:
1. Arrive with confidence and purpose
2. {random.choice(self.principles['authority'])}
3. Have a plausible reason for access

VERBAL CUES:
- "{random.choice(self.principles['urgency'])}"
- Reference specific names/departments if known
- Use insider terminology

IF CHALLENGED:
- Stay calm and maintain character
- "{random.choice(self.principles['social_proof'])}"
- Offer to "verify" with a confederate phone number

EXIT STRATEGY:
- Complete "work" quickly
- Thank staff for cooperation
- Leave without drawing attention
        """
        return pretext.strip()
        
    def analyze_text(self, text):
        """Analyze text for persuasion techniques"""
        found = []
        text_lower = text.lower()
        
        technique_keywords = {
            'urgency': ['immediate', 'urgent', 'now', 'expire', 'limited', 'deadline'],
            'authority': ['official', 'department', 'policy', 'require', 'mandate'],
            'scarcity': ['limited', 'exclusive', 'rare', 'only', 'few'],
            'social_proof': ['others', 'everyone', 'most', 'popular', 'recommended'],
            'reciprocity': ['free', 'gift', 'offer', 'reward', 'bonus'],
            'fear': ['warning', 'risk', 'threat', 'danger', 'suspend']
        }
        
        for technique, keywords in technique_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found.append({
                        'technique': technique,
                        'keyword': keyword,
                        'description': f"Uses {technique} principle via '{keyword}'"
                    })
                    break
                    
        return found


def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description="Seduction - Social Engineering Toolkit"
    )
    parser.add_argument("--phish", action="store_true",
                       help="Generate phishing email template")
    parser.add_argument("--vish", action="store_true",
                       help="Generate vishing script")
    parser.add_argument("--pretext", action="store_true",
                       help="Generate pretext scenario")
    parser.add_argument("--analyze", type=str,
                       help="Analyze text for persuasion techniques")
    parser.add_argument("--company", default="Acme Corp",
                       help="Target company name")
    parser.add_argument("--name", default="Valued Customer",
                       help="Target name")
    parser.add_argument("-o", "--output", help="Output file")
    
    args = parser.parse_args()
    
    engine = SeductionEngine()
    output = []
    
    if args.phish:
        email = engine.generate_phishing_email(args.company, args.name)
        print("\n" + "="*60)
        print("PHISHING EMAIL TEMPLATE")
        print("="*60)
        print(email)
        output.append(('phishing', email))
        
    if args.vish:
        script = engine.generate_vishing_script()
        print("\n" + "="*60)
        print(script)
        output.append(('vishing', script))
        
    if args.pretext:
        scenario = engine.generate_pretext_scenario()
        print("\n" + "="*60)
        print(scenario)
        output.append(('pretext', scenario))
        
    if args.analyze:
        results = engine.analyze_text(args.analyze)
        print("\n" + "="*60)
        print("PERSUASION ANALYSIS")
        print("="*60)
        print(f"\nText: {args.analyze[:100]}...")
        print(f"\nTechniques Found: {len(results)}")
        for r in results:
            print(f"  • {r['technique'].upper()}: {r['description']}")
            
    if not any([args.phish, args.vish, args.pretext, args.analyze]):
        print("\n[*] Use --phish, --vish, --pretext, or --analyze")
        print("[*] Example: seduction.py --phish --company 'Target Corp'")
        
    print("\n" + "="*60)
    print("⚠️  FOR AUTHORIZED SECURITY TESTING ONLY")
    print("="*60)
    
    if args.output and output:
        with open(args.output, 'w') as f:
            for type_, content in output:
                f.write(f"=== {type_.upper()} ===\n")
                f.write(content + "\n\n")
        print(f"\n[*] Output saved: {args.output}")


if __name__ == "__main__":
    main()
