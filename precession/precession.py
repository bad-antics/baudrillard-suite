#!/usr/bin/env python3
"""
PRECESSION - DNS/Domain Reality Mapper
======================================
"The map precedes the territory."
— Jean Baudrillard

Maps the DNS landscape to reveal simulated infrastructure.
"""

import os
import sys
import json
import socket
import argparse
from datetime import datetime

BANNER = """
██████╗ ██████╗ ███████╗ ██████╗███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
██████╔╝██████╔╝█████╗  ██║     █████╗  ███████╗███████╗██║██║   ██║██╔██╗ ██║
██╔═══╝ ██╔══██╗██╔══╝  ██║     ██╔══╝  ╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║     ██║  ██║███████╗╚██████╗███████╗███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                 [ DNS REALITY MAPPER | baudrillard-suite ]
"""

class PrecessionMapper:
    """Map DNS to reveal infrastructure simulation"""
    
    def __init__(self):
        self.mappings = []
        self.cdn_markers = {
            'cloudflare': ['cloudflare', '104.16', '172.67', '1.1.1.1'],
            'akamai': ['akamai', 'akam', 'edgekey', 'edgesuite'],
            'cloudfront': ['cloudfront', 'd1', 'd2', 'd3'],
            'fastly': ['fastly', 'global-ssl'],
            'google': ['google', 'gstatic', '1e100'],
            'aws': ['amazonaws', 'aws', 'ec2'],
            'azure': ['azure', 'microsoft', 'windows.net']
        }
        
    def resolve_domain(self, domain):
        """Resolve domain and analyze"""
        result = {
            'domain': domain,
            'timestamp': datetime.now().isoformat(),
            'ipv4': [],
            'ipv6': [],
            'cnames': [],
            'mx': [],
            'txt': [],
            'simulation_indicators': []
        }
        
        # IPv4
        try:
            ipv4_addrs = socket.getaddrinfo(domain, None, socket.AF_INET)
            result['ipv4'] = list(set(addr[4][0] for addr in ipv4_addrs))
        except socket.gaierror:
            pass
            
        # IPv6
        try:
            ipv6_addrs = socket.getaddrinfo(domain, None, socket.AF_INET6)
            result['ipv6'] = list(set(addr[4][0] for addr in ipv6_addrs))
        except socket.gaierror:
            pass
            
        # Detect CDN/cloud simulation
        result['infrastructure'] = self._detect_infrastructure(domain, result)
        
        # Calculate simulation score
        result['simulation_score'] = self._simulation_score(result)
        
        self.mappings.append(result)
        return result
        
    def _detect_infrastructure(self, domain, resolved):
        """Detect CDN and cloud infrastructure"""
        detected = []
        
        # Check resolved IPs against known ranges
        all_ips = ' '.join(resolved['ipv4'] + resolved['ipv6'])
        
        for provider, markers in self.cdn_markers.items():
            for marker in markers:
                if marker in domain.lower() or marker in all_ips.lower():
                    detected.append({
                        'provider': provider,
                        'marker': marker,
                        'type': 'cdn/cloud'
                    })
                    break
                    
        return detected
        
    def _simulation_score(self, result):
        """Calculate how 'simulated' the infrastructure appears"""
        score = 0
        
        # Multiple IPs = load balanced = simulated/abstracted
        if len(result['ipv4']) > 2:
            score += 20
            result['simulation_indicators'].append("Multiple IPs (load balanced)")
            
        # CDN detected = territory hidden behind map
        if result['infrastructure']:
            score += 30
            result['simulation_indicators'].append(
                f"CDN/Cloud: {result['infrastructure'][0]['provider']}"
            )
            
        # Common cloud IP ranges
        for ip in result['ipv4']:
            parts = ip.split('.')
            if len(parts) == 4:
                # Check for common cloud provider ranges
                if parts[0] in ['10', '172', '192']:
                    score += 10
                    result['simulation_indicators'].append("Private IP range")
                    break
                    
        return min(score, 100)
        
    def map_subdomains(self, domain, wordlist=None):
        """Enumerate subdomains"""
        default_words = [
            'www', 'mail', 'ftp', 'admin', 'api', 'dev', 'staging',
            'test', 'beta', 'cdn', 'static', 'assets', 'img', 'images',
            'app', 'mobile', 'portal', 'secure', 'vpn', 'remote',
            'ns1', 'ns2', 'mx', 'smtp', 'imap', 'pop'
        ]
        
        words = wordlist or default_words
        found = []
        
        for word in words:
            subdomain = f"{word}.{domain}"
            try:
                socket.gethostbyname(subdomain)
                found.append(subdomain)
            except socket.gaierror:
                pass
                
        return found
        
    def generate_map(self):
        """Generate ASCII map of infrastructure"""
        if not self.mappings:
            return "No mappings collected"
            
        map_str = """
╔═══════════════════════════════════════════════════════════════════╗
║                   PRECESSION - INFRASTRUCTURE MAP                  ║
╠═══════════════════════════════════════════════════════════════════╣
"""
        
        for m in self.mappings:
            sim_bar = '█' * (m['simulation_score'] // 10)
            map_str += f"""║
║  Domain: {m['domain'][:45]:<45}
║  IPs: {', '.join(m['ipv4'][:3])[:50]:<50}
║  Infrastructure: {', '.join([i['provider'] for i in m['infrastructure']])[:40] or 'Direct':<40}
║  Simulation: [{sim_bar:<10}] {m['simulation_score']}%
║  Indicators: {', '.join(m['simulation_indicators'][:2])[:45]:<45}
"""
        
        map_str += """╚═══════════════════════════════════════════════════════════════════╝"""
        return map_str
        
    def export_report(self, output_file):
        """Export mapping report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_domains': len(self.mappings),
            'mappings': self.mappings,
            'summary': self._summary()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        return output_file
        
    def _summary(self):
        """Generate summary statistics"""
        if not self.mappings:
            return {}
            
        providers = {}
        for m in self.mappings:
            for infra in m['infrastructure']:
                provider = infra['provider']
                providers[provider] = providers.get(provider, 0) + 1
                
        avg_sim = sum(m['simulation_score'] for m in self.mappings) / len(self.mappings)
        
        return {
            'average_simulation_score': avg_sim,
            'providers': providers,
            'highly_simulated': sum(1 for m in self.mappings if m['simulation_score'] > 50)
        }


def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="DNS Reality Mapper")
    parser.add_argument("domains", nargs='*', help="Domains to map")
    parser.add_argument("-f", "--file", help="File with domains (one per line)")
    parser.add_argument("-s", "--subdomains", help="Enumerate subdomains for domain")
    parser.add_argument("-o", "--output", help="Export report to JSON")
    parser.add_argument("--map", action="store_true", help="Show ASCII map")
    
    args = parser.parse_args()
    
    mapper = PrecessionMapper()
    domains = args.domains or []
    
    if args.file:
        with open(args.file) as f:
            domains.extend(line.strip() for line in f if line.strip())
            
    if args.subdomains:
        print(f"[*] Enumerating subdomains for: {args.subdomains}")
        found = mapper.map_subdomains(args.subdomains)
        print(f"[*] Found {len(found)} subdomains")
        domains.extend(found)
        for sub in found:
            print(f"  → {sub}")
            
    if domains:
        print(f"\n[*] Mapping {len(domains)} domain(s)...")
        for domain in domains:
            result = mapper.resolve_domain(domain)
            print(f"\n[{domain}]")
            print(f"  IPs: {', '.join(result['ipv4'][:5])}")
            print(f"  Infrastructure: {[i['provider'] for i in result['infrastructure']] or ['Direct']}")
            print(f"  Simulation Score: {result['simulation_score']}%")
            
    if args.map:
        print(mapper.generate_map())
        
    if args.output:
        mapper.export_report(args.output)
        print(f"\n[*] Report exported: {args.output}")
        
    if not domains and not args.subdomains:
        print("[*] Usage: precession.py example.com google.com")
        print("[*] Example: precession.py -s example.com --map")


if __name__ == "__main__":
    main()
