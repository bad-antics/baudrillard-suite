#!/usr/bin/env python3
"""
HYPERREAL - Network Traffic Amplification Analysis
===================================================
"The territory no longer precedes the map, nor does it survive it.
It is the map that precedes the territory."
— Jean Baudrillard

Analyzes network traffic to find signals more real than reality.
Detects patterns that exist only in the simulation.
"""

import os
import sys
import json
import time
import socket
import struct
import argparse
from datetime import datetime
from collections import defaultdict

BANNER = """
██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗ █████╗ ██╗     
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║     
███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝█████╗  ███████║██║     
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██║     
██║  ██║   ██║   ██║     ███████╗██║  ██║██║  ██║███████╗██║  ██║███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
            [ NETWORK REALITY AMPLIFIER | baudrillard-suite ]
"""

class HyperrealAnalyzer:
    """Detect patterns more real than real in network traffic"""
    
    def __init__(self):
        self.packets = []
        self.patterns = defaultdict(int)
        self.anomalies = []
        self.reality_index = 1.0  # Measure of hyperreality
        
    def analyze_pcap(self, pcap_file):
        """Analyze pcap file for hyperreal patterns"""
        try:
            import scapy.all as scapy
            packets = scapy.rdpcap(pcap_file)
            
            for pkt in packets:
                self._process_packet(pkt)
                
        except ImportError:
            print("[!] Scapy not installed, using mock analysis")
            self._mock_analysis()
            
    def _process_packet(self, pkt):
        """Extract hyperreal signatures from packet"""
        try:
            if pkt.haslayer('IP'):
                src = pkt['IP'].src
                dst = pkt['IP'].dst
                
                # Track connection patterns
                key = f"{src}->{dst}"
                self.patterns[key] += 1
                
                # Detect timing anomalies (hyperreal precision)
                if hasattr(pkt, 'time'):
                    self._check_timing_anomaly(pkt.time)
                    
                # Check for simulated traffic patterns
                if self._is_simulated(pkt):
                    self.anomalies.append({
                        'type': 'simulated_traffic',
                        'src': src,
                        'dst': dst,
                        'confidence': self._simulation_confidence(pkt)
                    })
        except Exception:
            pass
            
    def _check_timing_anomaly(self, timestamp):
        """Detect impossibly precise timing (simulation artifact)"""
        # In hyperreality, timing is too perfect
        frac = timestamp - int(timestamp)
        if frac == 0.0 or str(frac).endswith('000000'):
            self.reality_index *= 0.95  # Decrease reality
            
    def _is_simulated(self, pkt):
        """Check if traffic appears simulated"""
        # Simulated traffic often has patterns
        if hasattr(pkt, 'load'):
            payload = bytes(pkt.load) if pkt.load else b''
            # Check for repeating patterns
            if len(payload) > 16:
                chunk = payload[:8]
                if payload.count(chunk) > 2:
                    return True
        return False
        
    def _simulation_confidence(self, pkt):
        """Calculate confidence that traffic is simulated"""
        score = 0.5
        if hasattr(pkt, 'ttl') and pkt.ttl in [64, 128, 255]:
            score += 0.1
        if hasattr(pkt, 'len') and pkt.len % 64 == 0:
            score += 0.1
        return min(score, 1.0)
        
    def _mock_analysis(self):
        """Generate mock hyperreal analysis"""
        mock_ips = [
            '192.168.1.1', '10.0.0.1', '172.16.0.1',
            '8.8.8.8', '1.1.1.1', '192.168.1.100'
        ]
        
        import random
        for _ in range(100):
            src = random.choice(mock_ips)
            dst = random.choice(mock_ips)
            if src != dst:
                key = f"{src}->{dst}"
                self.patterns[key] += random.randint(1, 50)
                
        self.anomalies = [
            {'type': 'perfect_timing', 'confidence': 0.87},
            {'type': 'pattern_repetition', 'confidence': 0.72},
            {'type': 'synthetic_entropy', 'confidence': 0.65}
        ]
        self.reality_index = 0.73
        
    def generate_report(self):
        """Generate hyperreality analysis report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'reality_index': self.reality_index,
            'interpretation': self._interpret_reality(),
            'top_flows': self._top_flows(10),
            'anomalies': self.anomalies,
            'hyperreal_indicators': self._hyperreal_indicators()
        }
        return report
        
    def _interpret_reality(self):
        """Interpret the reality index"""
        if self.reality_index > 0.9:
            return "Traffic appears grounded in base reality"
        elif self.reality_index > 0.7:
            return "Second-order simulacra detected - reality masked"
        elif self.reality_index > 0.5:
            return "Third-order simulacra - absence of reality masked"
        else:
            return "Fourth-order hyperreality - pure simulation detected"
            
    def _top_flows(self, n):
        """Get top N traffic flows"""
        sorted_flows = sorted(
            self.patterns.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        return [{'flow': f, 'count': c} for f, c in sorted_flows[:n]]
        
    def _hyperreal_indicators(self):
        """Identify specific hyperreal indicators"""
        indicators = []
        
        # Check for unnaturally regular patterns
        counts = list(self.patterns.values())
        if counts:
            avg = sum(counts) / len(counts)
            variance = sum((c - avg) ** 2 for c in counts) / len(counts)
            if variance < avg * 0.1:  # Too regular
                indicators.append({
                    'type': 'statistical_regularity',
                    'description': 'Traffic variance impossibly low',
                    'severity': 'high'
                })
                
        # Check for simulation markers
        if len(self.anomalies) > 5:
            indicators.append({
                'type': 'simulation_markers',
                'description': 'Multiple simulation artifacts detected',
                'severity': 'critical'
            })
            
        return indicators


def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description="Hyperreal - Network Reality Amplifier"
    )
    parser.add_argument("-p", "--pcap", help="PCAP file to analyze")
    parser.add_argument("-i", "--interface", help="Live capture interface")
    parser.add_argument("-o", "--output", help="Output JSON file")
    parser.add_argument("--mock", action="store_true", 
                       help="Run mock analysis (no network)")
    
    args = parser.parse_args()
    
    analyzer = HyperrealAnalyzer()
    
    if args.pcap:
        print(f"[*] Analyzing PCAP: {args.pcap}")
        analyzer.analyze_pcap(args.pcap)
    elif args.mock:
        print("[*] Running mock hyperreal analysis...")
        analyzer._mock_analysis()
    else:
        print("[!] Specify --pcap or --mock for analysis")
        sys.exit(1)
        
    report = analyzer.generate_report()
    
    print("\n" + "="*60)
    print("HYPERREAL ANALYSIS REPORT")
    print("="*60)
    print(f"\n[REALITY INDEX] {report['reality_index']:.2f}")
    print(f"[INTERPRETATION] {report['interpretation']}")
    
    print("\n[TOP FLOWS]")
    for flow in report['top_flows'][:5]:
        print(f"  {flow['flow']}: {flow['count']} packets")
        
    print("\n[ANOMALIES]")
    for anomaly in report['anomalies']:
        print(f"  • {anomaly['type']}: {anomaly.get('confidence', 'N/A')}")
        
    print("\n[HYPERREAL INDICATORS]")
    for ind in report['hyperreal_indicators']:
        print(f"  ⚠ {ind['type']}: {ind['description']} [{ind['severity']}]")
        
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n[*] Report saved: {args.output}")


if __name__ == "__main__":
    main()
