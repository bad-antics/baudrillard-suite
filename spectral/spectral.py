#!/usr/bin/env python3
"""
SPECTRAL - The Ghost in the Network
════════════════════════════════════
"Ghosts are not dead people. They are people who have
never been born." - Jean Baudrillard

Advanced network presence analyzer that detects phantom
devices, ghost connections, and spectral anomalies in
network traffic. Sometimes what's NOT there is more
important than what IS.

Features:
- Ghost device detection
- Phantom connection tracking
- ARP ghost analysis
- Invisible host discovery
- Spectral traffic patterns
- Residual presence detection
"""

import os
import sys
import json
import socket
import struct
import argparse
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field, asdict
from collections import defaultdict
from pathlib import Path

try:
    import scapy.all as scapy
    HAS_SCAPY = True
except ImportError:
    HAS_SCAPY = False

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
║     ███████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ ██╗      ║
║     ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║      ║
║     ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝███████║██║      ║
║     ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║██║      ║
║     ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║███████╗ ║
║     ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ║
║                                                                       ║
║     The Ghost in the Network                                          ║
║     "What is NOT there is more important than what IS."               ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


@dataclass
class Ghost:
    """A phantom network entity"""
    ip: str
    mac: Optional[str] = None
    hostname: Optional[str] = None
    first_seen: datetime = field(default_factory=datetime.now)
    last_seen: datetime = field(default_factory=datetime.now)
    times_seen: int = 1
    ghost_score: float = 0.0
    anomalies: List[str] = field(default_factory=list)
    associated_macs: Set[str] = field(default_factory=set)
    services: List[int] = field(default_factory=list)
    ghost_type: str = "unknown"


@dataclass
class SpectralAnomaly:
    """An unexplained network phenomenon"""
    anomaly_type: str
    description: str
    timestamp: datetime
    source_ip: Optional[str] = None
    dest_ip: Optional[str] = None
    evidence: Dict = field(default_factory=dict)
    severity: str = "medium"


class ARPGhostDetector:
    """Detect ghosts in ARP tables"""
    
    def __init__(self):
        self.arp_history: Dict[str, List[Tuple[str, datetime]]] = defaultdict(list)
        self.gratuitous_arps: List[Dict] = []
        
    def analyze_arp_table(self) -> List[Ghost]:
        """Analyze system ARP table for ghosts"""
        ghosts = []
        
        try:
            # Read ARP cache (Linux)
            with open('/proc/net/arp', 'r') as f:
                lines = f.readlines()[1:]  # Skip header
                
            seen_ips = {}
            seen_macs = {}
            
            for line in lines:
                parts = line.split()
                if len(parts) >= 4:
                    ip = parts[0]
                    mac = parts[3]
                    
                    if mac == '00:00:00:00:00:00':
                        # Ghost entry - incomplete ARP
                        ghost = Ghost(
                            ip=ip,
                            mac=None,
                            ghost_type="incomplete_arp",
                            ghost_score=0.7,
                            anomalies=["Incomplete ARP entry - device mentioned but never responded"]
                        )
                        ghosts.append(ghost)
                        continue
                        
                    # Track for duplicate detection
                    if mac in seen_macs:
                        # Same MAC, different IP - possible ghost
                        ghost = Ghost(
                            ip=ip,
                            mac=mac,
                            ghost_type="duplicate_mac",
                            ghost_score=0.8,
                            anomalies=[f"MAC {mac} also assigned to {seen_macs[mac]}"]
                        )
                        ghosts.append(ghost)
                    else:
                        seen_macs[mac] = ip
                        
                    seen_ips[ip] = mac
                    
        except FileNotFoundError:
            pass  # Non-Linux system
            
        return ghosts
        
    def detect_arp_spoofing(self, packets: List[Dict]) -> List[SpectralAnomaly]:
        """Detect ARP spoofing from packet captures"""
        anomalies = []
        ip_to_mac = {}
        
        for pkt in packets:
            if pkt.get('type') == 'arp':
                src_ip = pkt.get('src_ip')
                src_mac = pkt.get('src_mac')
                
                if src_ip in ip_to_mac:
                    if ip_to_mac[src_ip] != src_mac:
                        anomaly = SpectralAnomaly(
                            anomaly_type="arp_spoof",
                            description=f"IP {src_ip} changed MAC from {ip_to_mac[src_ip]} to {src_mac}",
                            timestamp=datetime.now(),
                            source_ip=src_ip,
                            evidence={'old_mac': ip_to_mac[src_ip], 'new_mac': src_mac},
                            severity="high"
                        )
                        anomalies.append(anomaly)
                        
                ip_to_mac[src_ip] = src_mac
                
        return anomalies


class PhantomScanner:
    """Scan for phantom hosts that shouldn't exist"""
    
    def __init__(self, network: str):
        self.network = network
        self.discovered: Dict[str, Ghost] = {}
        
    def passive_discovery(self, duration: int = 30) -> List[Ghost]:
        """Passively listen for network ghosts"""
        ghosts = []
        
        if not HAS_SCAPY:
            print(f"{Colors.YELLOW}[!] Scapy not available, using passive methods{Colors.END}")
            return self._passive_socket_scan()
            
        print(f"{Colors.CYAN}[*] Passive listening for {duration} seconds...{Colors.END}")
        
        seen_hosts: Dict[str, Dict] = {}
        start_time = time.time()
        
        def packet_handler(pkt):
            if time.time() - start_time > duration:
                return True  # Stop sniffing
                
            # Extract source information
            if scapy.IP in pkt:
                src_ip = pkt[scapy.IP].src
                
                if src_ip not in seen_hosts:
                    seen_hosts[src_ip] = {
                        'first_seen': datetime.now(),
                        'protocols': set(),
                        'ports': set(),
                        'mac': None
                    }
                    
                seen_hosts[src_ip]['last_seen'] = datetime.now()
                
                if scapy.TCP in pkt:
                    seen_hosts[src_ip]['protocols'].add('TCP')
                    seen_hosts[src_ip]['ports'].add(pkt[scapy.TCP].sport)
                elif scapy.UDP in pkt:
                    seen_hosts[src_ip]['protocols'].add('UDP')
                    seen_hosts[src_ip]['ports'].add(pkt[scapy.UDP].sport)
                    
                if scapy.Ether in pkt:
                    seen_hosts[src_ip]['mac'] = pkt[scapy.Ether].src
                    
        try:
            scapy.sniff(timeout=duration, prn=packet_handler, store=False)
        except PermissionError:
            print(f"{Colors.RED}[!] Need root privileges for packet capture{Colors.END}")
            
        # Convert to ghosts
        for ip, data in seen_hosts.items():
            ghost = Ghost(
                ip=ip,
                mac=data['mac'],
                first_seen=data['first_seen'],
                last_seen=data['last_seen'],
                services=list(data['ports']),
                ghost_type="passive_discovery"
            )
            ghosts.append(ghost)
            
        return ghosts
        
    def _passive_socket_scan(self) -> List[Ghost]:
        """Passive discovery without scapy"""
        ghosts = []
        
        # Check common broadcast/multicast addresses
        multicast_addrs = [
            '224.0.0.1',   # All hosts
            '224.0.0.251', # mDNS
            '239.255.255.250',  # SSDP
        ]
        
        for addr in multicast_addrs:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(2)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
                # Try to detect responses
                ghost = Ghost(
                    ip=addr,
                    ghost_type="multicast_endpoint",
                    ghost_score=0.3,
                    anomalies=[f"Multicast address {addr} active"]
                )
                ghosts.append(ghost)
                sock.close()
            except:
                pass
                
        return ghosts
        
    def detect_ip_conflicts(self, interface: str = None) -> List[SpectralAnomaly]:
        """Detect IP address conflicts - two hosts claiming same IP"""
        anomalies = []
        
        if not HAS_SCAPY:
            return anomalies
            
        print(f"{Colors.CYAN}[*] Scanning for IP conflicts...{Colors.END}")
        
        # Send gratuitous ARP for all IPs in range
        # and watch for duplicate responses
        
        ip_responses: Dict[str, List[str]] = defaultdict(list)
        
        try:
            # Get local IP to determine range
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
            s.close()
            
            # Scan /24 network
            base = '.'.join(local_ip.split('.')[:-1])
            
            for i in range(1, 255):
                target = f"{base}.{i}"
                ans, _ = scapy.srp(
                    scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=target),
                    timeout=0.1,
                    verbose=False
                )
                
                for _, rcv in ans:
                    mac = rcv.hwsrc
                    ip_responses[target].append(mac)
                    
            # Check for conflicts
            for ip, macs in ip_responses.items():
                if len(set(macs)) > 1:
                    anomaly = SpectralAnomaly(
                        anomaly_type="ip_conflict",
                        description=f"IP {ip} claimed by multiple MACs: {set(macs)}",
                        timestamp=datetime.now(),
                        source_ip=ip,
                        evidence={'macs': list(set(macs))},
                        severity="critical"
                    )
                    anomalies.append(anomaly)
                    
        except Exception as e:
            print(f"{Colors.RED}[!] Error detecting conflicts: {e}{Colors.END}")
            
        return anomalies


class ResidualPresenceAnalyzer:
    """Analyze residual presence - devices that were here but are gone"""
    
    def __init__(self, history_file: str = None):
        self.history_file = history_file or Path.home() / '.spectral_history.json'
        self.history: Dict[str, Dict] = self._load_history()
        
    def _load_history(self) -> Dict:
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except:
            return {'devices': {}, 'last_scan': None}
            
    def _save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2, default=str)
            
    def update_presence(self, ghosts: List[Ghost]):
        """Update presence history with current scan"""
        now = datetime.now().isoformat()
        
        current_ips = set()
        
        for ghost in ghosts:
            current_ips.add(ghost.ip)
            
            if ghost.ip not in self.history['devices']:
                self.history['devices'][ghost.ip] = {
                    'mac': ghost.mac,
                    'first_seen': now,
                    'last_seen': now,
                    'times_seen': 1,
                    'hostname': ghost.hostname
                }
            else:
                self.history['devices'][ghost.ip]['last_seen'] = now
                self.history['devices'][ghost.ip]['times_seen'] += 1
                if ghost.mac:
                    self.history['devices'][ghost.ip]['mac'] = ghost.mac
                    
        self.history['last_scan'] = now
        self._save_history()
        
        return current_ips
        
    def find_missing(self, current_ips: Set[str], max_age_days: int = 7) -> List[Ghost]:
        """Find devices that used to be present but are now gone"""
        missing_ghosts = []
        cutoff = datetime.now() - timedelta(days=max_age_days)
        
        for ip, data in self.history['devices'].items():
            if ip not in current_ips:
                last_seen = datetime.fromisoformat(data['last_seen'])
                
                if last_seen > cutoff:
                    ghost = Ghost(
                        ip=ip,
                        mac=data.get('mac'),
                        hostname=data.get('hostname'),
                        first_seen=datetime.fromisoformat(data['first_seen']),
                        last_seen=last_seen,
                        times_seen=data['times_seen'],
                        ghost_type="residual",
                        ghost_score=0.9,
                        anomalies=[f"Device was present {data['times_seen']} times but now missing"]
                    )
                    missing_ghosts.append(ghost)
                    
        return missing_ghosts


class SpectralAnalyzer:
    """Main spectral analysis engine"""
    
    def __init__(self, network: str = None, verbose: bool = False):
        self.network = network or self._detect_network()
        self.verbose = verbose
        self.arp_detector = ARPGhostDetector()
        self.phantom_scanner = PhantomScanner(self.network)
        self.residual_analyzer = ResidualPresenceAnalyzer()
        self.ghosts: List[Ghost] = []
        self.anomalies: List[SpectralAnomaly] = []
        
    def _detect_network(self) -> str:
        """Auto-detect local network"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return '.'.join(ip.split('.')[:-1]) + '.0/24'
        except:
            return '192.168.1.0/24'
            
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[SPECTRAL]{Colors.END} {msg}")
            
    def full_scan(self, duration: int = 30) -> Dict:
        """Perform complete spectral analysis"""
        results = {
            'timestamp': datetime.now().isoformat(),
            'network': self.network,
            'ghosts': [],
            'anomalies': [],
            'summary': {}
        }
        
        # ARP ghost detection
        self.log("Analyzing ARP table for ghosts...")
        arp_ghosts = self.arp_detector.analyze_arp_table()
        self.ghosts.extend(arp_ghosts)
        
        # Passive discovery
        self.log(f"Passive listening for {duration}s...")
        passive_ghosts = self.phantom_scanner.passive_discovery(duration)
        self.ghosts.extend(passive_ghosts)
        
        # Residual presence
        self.log("Checking for residual presence...")
        current_ips = self.residual_analyzer.update_presence(passive_ghosts)
        missing_ghosts = self.residual_analyzer.find_missing(current_ips)
        self.ghosts.extend(missing_ghosts)
        
        # IP conflict detection (requires root)
        if os.geteuid() == 0 and HAS_SCAPY:
            self.log("Detecting IP conflicts...")
            conflict_anomalies = self.phantom_scanner.detect_ip_conflicts()
            self.anomalies.extend(conflict_anomalies)
            
        # Prepare results
        results['ghosts'] = [
            {
                'ip': g.ip,
                'mac': g.mac,
                'hostname': g.hostname,
                'ghost_type': g.ghost_type,
                'ghost_score': g.ghost_score,
                'anomalies': g.anomalies,
                'services': g.services,
                'first_seen': g.first_seen.isoformat(),
                'last_seen': g.last_seen.isoformat()
            }
            for g in self.ghosts
        ]
        
        results['anomalies'] = [
            {
                'type': a.anomaly_type,
                'description': a.description,
                'severity': a.severity,
                'timestamp': a.timestamp.isoformat(),
                'source_ip': a.source_ip,
                'evidence': a.evidence
            }
            for a in self.anomalies
        ]
        
        results['summary'] = {
            'total_ghosts': len(self.ghosts),
            'total_anomalies': len(self.anomalies),
            'ghost_types': dict(defaultdict(int, 
                [(g.ghost_type, sum(1 for x in self.ghosts if x.ghost_type == g.ghost_type)) 
                 for g in self.ghosts])),
            'high_severity_anomalies': sum(1 for a in self.anomalies if a.severity in ['high', 'critical'])
        }
        
        return results


def print_ghost(ghost: Ghost):
    """Pretty print a ghost"""
    score_color = Colors.RED if ghost.ghost_score > 0.7 else Colors.YELLOW if ghost.ghost_score > 0.4 else Colors.GREEN
    
    print(f"\n{Colors.BOLD}👻 Ghost: {ghost.ip}{Colors.END}")
    print(f"   Type: {ghost.ghost_type}")
    print(f"   MAC: {ghost.mac or 'unknown'}")
    print(f"   Score: {score_color}{ghost.ghost_score:.2f}{Colors.END}")
    
    if ghost.anomalies:
        print(f"   Anomalies:")
        for anomaly in ghost.anomalies:
            print(f"      • {anomaly}")
            
    if ghost.services:
        print(f"   Services: {', '.join(map(str, ghost.services[:10]))}")


def print_anomaly(anomaly: SpectralAnomaly):
    """Pretty print an anomaly"""
    severity_colors = {
        'low': Colors.GREEN,
        'medium': Colors.YELLOW,
        'high': Colors.RED,
        'critical': Colors.MAGENTA
    }
    color = severity_colors.get(anomaly.severity, Colors.YELLOW)
    
    print(f"\n{color}▲ {anomaly.anomaly_type.upper()}{Colors.END}")
    print(f"   {anomaly.description}")
    print(f"   Severity: {color}{anomaly.severity}{Colors.END}")
    
    if anomaly.source_ip:
        print(f"   Source: {anomaly.source_ip}")


def main():
    parser = argparse.ArgumentParser(
        description='SPECTRAL - The Ghost in the Network',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full spectral scan
  spectral.py scan --duration 60
  
  # Quick ARP ghost check
  spectral.py arp
  
  # Monitor for ghosts continuously
  spectral.py monitor --interval 30
  
  # Export results to JSON
  spectral.py scan -o ghosts.json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Full spectral scan')
    scan_parser.add_argument('-n', '--network', help='Target network (e.g., 192.168.1.0/24)')
    scan_parser.add_argument('-d', '--duration', type=int, default=30, help='Passive scan duration')
    scan_parser.add_argument('-o', '--output', help='Output JSON file')
    scan_parser.add_argument('-v', '--verbose', action='store_true')
    
    # ARP command
    arp_parser = subparsers.add_parser('arp', help='Analyze ARP table for ghosts')
    arp_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Continuous ghost monitoring')
    monitor_parser.add_argument('-i', '--interval', type=int, default=60, help='Scan interval in seconds')
    monitor_parser.add_argument('-v', '--verbose', action='store_true')
    
    args = parser.parse_args()
    
    if not args.command:
        print(BANNER)
        parser.print_help()
        return
        
    print(BANNER)
    
    if args.command == 'scan':
        analyzer = SpectralAnalyzer(
            network=args.network,
            verbose=args.verbose
        )
        
        print(f"\n{Colors.CYAN}[*] Beginning spectral analysis of {analyzer.network}...{Colors.END}\n")
        
        results = analyzer.full_scan(duration=args.duration)
        
        # Print results
        print(f"\n{Colors.BOLD}═══ SPECTRAL ANALYSIS COMPLETE ═══{Colors.END}")
        print(f"\n{Colors.GREEN}Found {len(results['ghosts'])} ghosts and {len(results['anomalies'])} anomalies{Colors.END}")
        
        if results['ghosts']:
            print(f"\n{Colors.BOLD}─── GHOSTS ───{Colors.END}")
            for ghost_data in results['ghosts']:
                ghost = Ghost(**{k: v for k, v in ghost_data.items() 
                               if k in ['ip', 'mac', 'hostname', 'ghost_type', 'ghost_score', 'anomalies', 'services']})
                print_ghost(ghost)
                
        if results['anomalies']:
            print(f"\n{Colors.BOLD}─── ANOMALIES ───{Colors.END}")
            for anomaly_data in results['anomalies']:
                anomaly = SpectralAnomaly(
                    anomaly_type=anomaly_data['type'],
                    description=anomaly_data['description'],
                    timestamp=datetime.now(),
                    severity=anomaly_data['severity'],
                    source_ip=anomaly_data.get('source_ip'),
                    evidence=anomaly_data.get('evidence', {})
                )
                print_anomaly(anomaly)
                
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\n{Colors.GREEN}Results saved to {args.output}{Colors.END}")
            
        print(f"\n{Colors.MAGENTA}\"Ghosts are not dead people.")
        print(f"  They are people who have never been born.\"{Colors.END}\n")
        
    elif args.command == 'arp':
        detector = ARPGhostDetector()
        ghosts = detector.analyze_arp_table()
        
        print(f"\n{Colors.BOLD}─── ARP GHOSTS ───{Colors.END}")
        
        if ghosts:
            for ghost in ghosts:
                print_ghost(ghost)
        else:
            print(f"{Colors.GREEN}No ARP ghosts detected{Colors.END}")
            
    elif args.command == 'monitor':
        print(f"{Colors.CYAN}[*] Starting continuous ghost monitoring (Ctrl+C to stop)...{Colors.END}")
        
        analyzer = SpectralAnalyzer(verbose=args.verbose)
        
        try:
            while True:
                results = analyzer.full_scan(duration=10)
                
                if results['ghosts'] or results['anomalies']:
                    print(f"\n{Colors.RED}[!] {datetime.now().strftime('%H:%M:%S')} - Detected {len(results['ghosts'])} ghosts, {len(results['anomalies'])} anomalies{Colors.END}")
                    
                    for ghost_data in results['ghosts'][-3:]:  # Show last 3
                        print(f"    👻 {ghost_data['ip']} ({ghost_data['ghost_type']})")
                else:
                    print(f"{Colors.DIM}[{datetime.now().strftime('%H:%M:%S')}] Network clear{Colors.END}", end='\r')
                    
                time.sleep(args.interval)
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[*] Monitoring stopped{Colors.END}")


if __name__ == '__main__':
    main()
