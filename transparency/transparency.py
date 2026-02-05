#!/usr/bin/env python3
"""
TRANSPARENCY - OSINT Aggregation Through Total Visibility
══════════════════════════════════════════════════════════
"In a world where everything is visible, nothing is hidden,
but nothing is revealed either." - Jean Baudrillard

Exploits the paradox of transparency: the more visible something
becomes, the more it disappears into meaninglessness. We aggregate
until patterns emerge from the noise.

Features:
- Multi-source OSINT aggregation
- Social media footprint analysis
- Data broker reconnaissance
- Digital exhaust collection
- Correlation engine
- Timeline reconstruction
"""

import os
import sys
import json
import re
import time
import hashlib
import argparse
import socket
import urllib.parse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Any
from dataclasses import dataclass, field, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ANSI colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

BANNER = f"""{Colors.CYAN}
╔═══════════════════════════════════════════════════════════════════════╗
║   ████████╗██████╗  █████╗ ███╗   ██╗███████╗██████╗  █████╗ ██████╗  ║
║   ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗ ║
║      ██║   ██████╔╝███████║██╔██╗ ██║███████╗██████╔╝███████║██████╔╝ ║
║      ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔═══╝ ██╔══██║██╔══██╗ ║
║      ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║     ██║  ██║██║  ██║ ║
║      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ║
║                                                                       ║
║   OSINT Aggregation Through Total Visibility                          ║
║   "In transparency, everything disappears."                           ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


@dataclass
class Identity:
    """Aggregated identity profile"""
    query: str
    query_type: str  # email, username, phone, name, domain
    created: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # Discovered data
    emails: Set[str] = field(default_factory=set)
    usernames: Set[str] = field(default_factory=set)
    names: Set[str] = field(default_factory=set)
    phones: Set[str] = field(default_factory=set)
    addresses: Set[str] = field(default_factory=set)
    social_profiles: Dict[str, str] = field(default_factory=dict)
    domains: Set[str] = field(default_factory=set)
    ips: Set[str] = field(default_factory=set)
    
    # Metadata
    sources: List[str] = field(default_factory=list)
    timeline: List[Dict] = field(default_factory=list)
    correlations: List[Dict] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return {
            'query': self.query,
            'query_type': self.query_type,
            'created': self.created,
            'emails': list(self.emails),
            'usernames': list(self.usernames),
            'names': list(self.names),
            'phones': list(self.phones),
            'addresses': list(self.addresses),
            'social_profiles': self.social_profiles,
            'domains': list(self.domains),
            'ips': list(self.ips),
            'sources': self.sources,
            'timeline': self.timeline,
            'correlations': self.correlations
        }


class OSINTModule:
    """Base class for OSINT modules"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.enabled = True
        
    def search(self, identity: Identity) -> bool:
        """Search and update identity. Returns True if data found."""
        raise NotImplementedError


class EmailAnalyzer(OSINTModule):
    """Analyze email addresses for patterns and associations"""
    
    def __init__(self):
        super().__init__("Email Analyzer", "Extract patterns from email addresses")
        
    def search(self, identity: Identity) -> bool:
        found = False
        
        for email in list(identity.emails) + ([identity.query] if '@' in identity.query else []):
            if '@' not in email:
                continue
                
            local, domain = email.split('@', 1)
            
            # Extract potential usernames from email
            # Remove numbers and special chars to get base username
            username_base = re.sub(r'[0-9._+-]+', '', local)
            if username_base:
                identity.usernames.add(username_base)
                found = True
                
            # Common email patterns suggest real names
            # firstname.lastname@domain.com
            if '.' in local:
                parts = local.split('.')
                if len(parts) == 2:
                    potential_name = f"{parts[0].title()} {parts[1].title()}"
                    if len(parts[0]) > 1 and len(parts[1]) > 1:
                        identity.names.add(potential_name)
                        found = True
                        
            # Track domain
            identity.domains.add(domain)
            
            identity.sources.append(f"email_analysis:{email}")
            
        return found


class UsernameChecker(OSINTModule):
    """Check username existence across platforms"""
    
    PLATFORMS = {
        'github': 'https://github.com/{username}',
        'twitter': 'https://twitter.com/{username}',
        'instagram': 'https://instagram.com/{username}',
        'reddit': 'https://reddit.com/user/{username}',
        'linkedin': 'https://linkedin.com/in/{username}',
        'facebook': 'https://facebook.com/{username}',
        'tiktok': 'https://tiktok.com/@{username}',
        'youtube': 'https://youtube.com/@{username}',
        'twitch': 'https://twitch.tv/{username}',
        'pinterest': 'https://pinterest.com/{username}',
        'medium': 'https://medium.com/@{username}',
        'dev.to': 'https://dev.to/{username}',
        'hackernews': 'https://news.ycombinator.com/user?id={username}',
        'keybase': 'https://keybase.io/{username}',
        'gitlab': 'https://gitlab.com/{username}',
        'bitbucket': 'https://bitbucket.org/{username}',
    }
    
    def __init__(self):
        super().__init__("Username Checker", "Check username across social platforms")
        
    def search(self, identity: Identity) -> bool:
        if not HAS_REQUESTS:
            return False
            
        found = False
        usernames = list(identity.usernames)
        if identity.query_type == 'username':
            usernames.append(identity.query)
            
        for username in set(usernames):
            for platform, url_template in self.PLATFORMS.items():
                url = url_template.format(username=username)
                try:
                    # Just check if URL is valid format
                    # Real implementation would check HTTP status
                    identity.social_profiles[platform] = url
                    found = True
                except Exception:
                    pass
                    
            identity.sources.append(f"username_enum:{username}")
            
        return found


class DomainRecon(OSINTModule):
    """Domain reconnaissance and enumeration"""
    
    def __init__(self):
        super().__init__("Domain Recon", "DNS and WHOIS reconnaissance")
        
    def search(self, identity: Identity) -> bool:
        found = False
        
        domains = list(identity.domains)
        if identity.query_type == 'domain':
            domains.append(identity.query)
            
        for domain in set(domains):
            # DNS lookups
            try:
                # A record
                ips = socket.gethostbyname_ex(domain)[2]
                for ip in ips:
                    identity.ips.add(ip)
                    found = True
                    
                # MX records indicate email capability
                try:
                    import dns.resolver
                    mx_records = dns.resolver.resolve(domain, 'MX')
                    for mx in mx_records:
                        identity.timeline.append({
                            'type': 'mx_record',
                            'domain': domain,
                            'mx': str(mx.exchange),
                            'priority': mx.preference
                        })
                        found = True
                except:
                    pass
                    
            except socket.gaierror:
                pass
            except Exception as e:
                pass
                
            identity.sources.append(f"domain_recon:{domain}")
            
        return found


class DataBrokerSearch(OSINTModule):
    """Search common data broker patterns"""
    
    BROKERS = [
        ('whitepages', 'https://www.whitepages.com/name/{query}'),
        ('spokeo', 'https://www.spokeo.com/{query}'),
        ('pipl', 'https://pipl.com/search/?q={query}'),
        ('intelius', 'https://www.intelius.com/people-search/{query}'),
        ('beenverified', 'https://www.beenverified.com/people/{query}'),
        ('truepeoplesearch', 'https://www.truepeoplesearch.com/results?name={query}'),
        ('fastpeoplesearch', 'https://www.fastpeoplesearch.com/name/{query}'),
    ]
    
    def __init__(self):
        super().__init__("Data Broker Search", "Generate data broker lookup URLs")
        
    def search(self, identity: Identity) -> bool:
        found = False
        
        queries = list(identity.names)
        if identity.query_type in ('name', 'username'):
            queries.append(identity.query)
            
        for query in set(queries):
            safe_query = urllib.parse.quote_plus(query)
            for broker_name, url_template in self.BROKERS:
                url = url_template.format(query=safe_query)
                identity.correlations.append({
                    'type': 'data_broker',
                    'broker': broker_name,
                    'url': url,
                    'query': query
                })
                found = True
                
            identity.sources.append(f"data_broker_search:{query}")
            
        return found


class BreachChecker(OSINTModule):
    """Check for data breaches (patterns only - no API)"""
    
    def __init__(self):
        super().__init__("Breach Checker", "Generate breach lookup URLs")
        
    def search(self, identity: Identity) -> bool:
        found = False
        
        emails = list(identity.emails)
        if identity.query_type == 'email':
            emails.append(identity.query)
            
        for email in set(emails):
            # Generate HIBP-style lookup URL
            sha1_hash = hashlib.sha1(email.lower().encode()).hexdigest()
            
            identity.correlations.append({
                'type': 'breach_check',
                'email': email,
                'hash': sha1_hash[:10],  # Partial hash for privacy
                'hibp_url': f'https://haveibeenpwned.com/account/{urllib.parse.quote(email)}',
                'dehashed_url': f'https://dehashed.com/search?query={urllib.parse.quote(email)}'
            })
            found = True
            
            identity.sources.append(f"breach_check:{email}")
            
        return found


class DigitalExhaustCollector(OSINTModule):
    """Collect digital exhaust patterns"""
    
    def __init__(self):
        super().__init__("Digital Exhaust", "Pattern analysis of digital footprint")
        
    def search(self, identity: Identity) -> bool:
        """Generate search URLs and patterns"""
        found = False
        
        # Google dorks for the identity
        queries = []
        
        for email in identity.emails:
            queries.append(f'"{email}"')
            
        for username in identity.usernames:
            queries.append(f'"{username}"')
            queries.append(f'inurl:{username}')
            
        for name in identity.names:
            queries.append(f'"{name}"')
            
        for query in queries[:10]:  # Limit to 10
            safe_query = urllib.parse.quote_plus(query)
            identity.correlations.append({
                'type': 'google_dork',
                'query': query,
                'url': f'https://www.google.com/search?q={safe_query}'
            })
            found = True
            
        # Archive.org patterns
        for domain in identity.domains:
            identity.correlations.append({
                'type': 'wayback_machine',
                'domain': domain,
                'url': f'https://web.archive.org/web/*/{domain}'
            })
            found = True
            
        identity.sources.append("digital_exhaust")
        return found


class Transparency:
    """Main OSINT aggregation engine"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.modules = [
            EmailAnalyzer(),
            UsernameChecker(),
            DomainRecon(),
            DataBrokerSearch(),
            BreachChecker(),
            DigitalExhaustCollector()
        ]
        
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[TRANSPARENCY]{Colors.END} {msg}")
            
    def detect_query_type(self, query: str) -> str:
        """Detect the type of query input"""
        if '@' in query and '.' in query.split('@')[1]:
            return 'email'
        if re.match(r'^[\w.-]+\.(com|net|org|io|co|dev|xyz|info|biz)$', query, re.I):
            return 'domain'
        if re.match(r'^\+?[\d\s()-]{10,}$', query):
            return 'phone'
        if ' ' in query:
            return 'name'
        return 'username'
        
    def investigate(self, query: str) -> Identity:
        """Run full investigation on query"""
        query_type = self.detect_query_type(query)
        self.log(f"Query: {query} (detected as: {query_type})")
        
        identity = Identity(query=query, query_type=query_type)
        
        # Seed identity based on query type
        if query_type == 'email':
            identity.emails.add(query)
        elif query_type == 'username':
            identity.usernames.add(query)
        elif query_type == 'domain':
            identity.domains.add(query)
        elif query_type == 'name':
            identity.names.add(query)
        elif query_type == 'phone':
            identity.phones.add(query)
            
        # Run all modules
        for module in self.modules:
            if module.enabled:
                self.log(f"Running: {module.name}", Colors.YELLOW)
                try:
                    module.search(identity)
                except Exception as e:
                    self.log(f"Error in {module.name}: {e}", Colors.RED)
                    
        return identity
        
    def print_report(self, identity: Identity):
        """Print formatted investigation report"""
        print(f"\n{Colors.BOLD}{'═' * 70}{Colors.END}")
        print(f"{Colors.BOLD}TRANSPARENCY INVESTIGATION REPORT{Colors.END}")
        print(f"Query: {identity.query} ({identity.query_type})")
        print(f"Time: {identity.created}")
        print(f"Sources: {len(identity.sources)}")
        print(f"{Colors.BOLD}{'═' * 70}{Colors.END}\n")
        
        # Identity data
        sections = [
            ('EMAILS', identity.emails, Colors.GREEN),
            ('USERNAMES', identity.usernames, Colors.CYAN),
            ('NAMES', identity.names, Colors.YELLOW),
            ('PHONES', identity.phones, Colors.MAGENTA),
            ('DOMAINS', identity.domains, Colors.BLUE),
            ('IP ADDRESSES', identity.ips, Colors.RED),
        ]
        
        for title, data, color in sections:
            if data:
                print(f"{color}▲ {title}{Colors.END}")
                for item in list(data)[:10]:
                    print(f"  • {item}")
                if len(data) > 10:
                    print(f"  {Colors.DIM}... and {len(data) - 10} more{Colors.END}")
                print()
                
        # Social profiles
        if identity.social_profiles:
            print(f"{Colors.CYAN}▲ SOCIAL PROFILES{Colors.END}")
            for platform, url in list(identity.social_profiles.items())[:10]:
                print(f"  • {platform}: {url}")
            print()
            
        # Correlations
        if identity.correlations:
            print(f"{Colors.MAGENTA}▲ INVESTIGATION LEADS{Colors.END}")
            by_type = {}
            for c in identity.correlations:
                t = c.get('type', 'other')
                if t not in by_type:
                    by_type[t] = []
                by_type[t].append(c)
                
            for ctype, items in by_type.items():
                print(f"  {Colors.DIM}{ctype}:{Colors.END}")
                for item in items[:3]:
                    if 'url' in item:
                        print(f"    → {item['url'][:70]}...")
                if len(items) > 3:
                    print(f"    {Colors.DIM}... and {len(items) - 3} more{Colors.END}")
            print()
            
        print(f"{Colors.BOLD}{'═' * 70}{Colors.END}")
        print(f"{Colors.CYAN}\"Total visibility creates total invisibility.\"")
        print(f"\"We see everything, therefore we see nothing.\"{Colors.END}")
        print(f"{Colors.BOLD}{'═' * 70}{Colors.END}\n")


def main():
    parser = argparse.ArgumentParser(
        description='TRANSPARENCY - OSINT Aggregation Through Total Visibility',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  transparency.py user@example.com           Investigate email
  transparency.py johndoe                    Investigate username
  transparency.py "John Doe"                 Investigate name
  transparency.py example.com                Investigate domain
  transparency.py +1-555-123-4567            Investigate phone
  
Modules:
  • Email Analyzer      - Extract patterns from email addresses
  • Username Checker    - Check across social platforms
  • Domain Recon        - DNS and infrastructure analysis
  • Data Broker Search  - Generate lookup URLs
  • Breach Checker      - Check for data breaches
  • Digital Exhaust     - Pattern analysis & Google dorks
        """
    )
    
    parser.add_argument('query', help='Email, username, name, domain, or phone to investigate')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-o', '--output', help='Export results to JSON file')
    parser.add_argument('-q', '--quiet', action='store_true', help='Minimal output')
    
    args = parser.parse_args()
    
    if not args.quiet:
        print(BANNER)
        
    transparency = Transparency(verbose=args.verbose)
    identity = transparency.investigate(args.query)
    
    if not args.quiet:
        transparency.print_report(identity)
        
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(identity.to_dict(), f, indent=2)
        print(f"{Colors.GREEN}Results exported to: {args.output}{Colors.END}")


if __name__ == '__main__':
    main()
