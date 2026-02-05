#!/usr/bin/env python3
"""
AMBIENT - Environmental Intelligence Gathering
═══════════════════════════════════════════════
"We live in a world where there is more and more
information, and less and less meaning."
- Jean Baudrillard

Passive environmental intelligence gathering through
ambient signals - WiFi, Bluetooth, sound, light, and
electromagnetic emissions. The environment speaks
if you know how to listen.

Features:
- WiFi passive reconnaissance
- Bluetooth device tracking
- Ambient signal analysis
- Environmental fingerprinting
- Temporal pattern detection
- Location inference
"""

import os
import sys
import json
import struct
import socket
import argparse
import threading
import time
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from collections import defaultdict

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

BANNER = f"""{Colors.BLUE}
╔═══════════════════════════════════════════════════════════════════════╗
║       █████╗ ███╗   ███╗██████╗ ██╗███████╗███╗   ██╗████████╗        ║
║      ██╔══██╗████╗ ████║██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝        ║
║      ███████║██╔████╔██║██████╔╝██║█████╗  ██╔██╗ ██║   ██║           ║
║      ██╔══██║██║╚██╔╝██║██╔══██╗██║██╔══╝  ██║╚██╗██║   ██║           ║
║      ██║  ██║██║ ╚═╝ ██║██████╔╝██║███████╗██║ ╚████║   ██║           ║
║      ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝           ║
║                                                                       ║
║      Environmental Intelligence Gathering                             ║
║      "More information, less meaning."                                ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


@dataclass
class WiFiNetwork:
    """Detected WiFi network"""
    bssid: str
    ssid: str
    channel: int
    signal: int
    encryption: str
    first_seen: datetime = field(default_factory=datetime.now)
    last_seen: datetime = field(default_factory=datetime.now)
    times_seen: int = 1
    clients: Set[str] = field(default_factory=set)
    vendor: Optional[str] = None


@dataclass
class BluetoothDevice:
    """Detected Bluetooth device"""
    address: str
    name: Optional[str] = None
    device_class: Optional[str] = None
    rssi: Optional[int] = None
    first_seen: datetime = field(default_factory=datetime.now)
    last_seen: datetime = field(default_factory=datetime.now)
    times_seen: int = 1
    services: List[str] = field(default_factory=list)


@dataclass
class AmbientSignature:
    """Environmental signature"""
    timestamp: datetime
    wifi_networks: int
    bluetooth_devices: int
    unique_ssids: List[str]
    signal_profile: Dict[str, int]
    location_hint: Optional[str] = None


class OUILookup:
    """MAC address vendor lookup"""
    
    # Common OUI prefixes
    OUI_DB = {
        '00:00:0c': 'Cisco',
        '00:1a:2b': 'Ayecom Technology',
        '00:50:56': 'VMware',
        '08:00:27': 'VirtualBox',
        '00:0c:29': 'VMware',
        'b8:27:eb': 'Raspberry Pi',
        'dc:a6:32': 'Raspberry Pi',
        'e4:5f:01': 'Raspberry Pi',
        '00:1e:c9': 'Dell',
        'f4:5c:89': 'Apple',
        '00:25:00': 'Apple',
        '3c:22:fb': 'Apple',
        '88:e9:fe': 'Apple',
        'ac:bc:32': 'Apple',
        '00:11:22': 'Cimsys',
        'aa:bb:cc': 'Test',
        '00:1b:63': 'Apple',
        '00:03:93': 'Apple',
        '00:17:f2': 'Apple',
        '00:1c:b3': 'Apple',
        '00:1d:4f': 'Apple',
        '00:1e:52': 'Apple',
        '00:1f:5b': 'Apple',
        '00:1f:f3': 'Apple',
        '00:21:e9': 'Apple',
        '00:22:41': 'Apple',
        '00:23:12': 'Apple',
        '00:23:32': 'Apple',
        '00:23:6c': 'Apple',
        '00:23:df': 'Apple',
        '00:24:36': 'Apple',
        '00:25:4b': 'Apple',
        '00:25:bc': 'Apple',
        '00:26:08': 'Apple',
        '00:26:4a': 'Apple',
        '00:26:b0': 'Apple',
        '00:26:bb': 'Apple',
        'f0:18:98': 'Apple',
        '48:d7:05': 'Apple',
        '00:0d:93': 'Apple',
        '00:14:51': 'Apple',
        '00:16:cb': 'Apple',
        '00:19:e3': 'Apple',
        '94:94:26': 'Samsung',
        'f4:42:8f': 'Samsung',
        '00:26:37': 'Samsung',
        '5c:f9:38': 'Samsung',
        'e4:7c:f9': 'Samsung',
    }
    
    @classmethod
    def lookup(cls, mac: str) -> Optional[str]:
        """Lookup vendor for MAC address"""
        prefix = mac.lower()[:8]
        return cls.OUI_DB.get(prefix)


class WiFiScanner:
    """Passive WiFi reconnaissance"""
    
    def __init__(self, interface: str = None):
        self.interface = interface or self._detect_interface()
        self.networks: Dict[str, WiFiNetwork] = {}
        self.clients: Dict[str, Set[str]] = defaultdict(set)
        
    def _detect_interface(self) -> str:
        """Detect wireless interface"""
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True, timeout=5)
            for line in result.stdout.split('\n'):
                if 'IEEE 802.11' in line:
                    return line.split()[0]
        except:
            pass
            
        # Common interface names
        for iface in ['wlan0', 'wlp2s0', 'wlp3s0', 'wlan1', 'wlx']:
            if Path(f'/sys/class/net/{iface}').exists():
                return iface
                
        return 'wlan0'
        
    def scan_networks(self) -> List[WiFiNetwork]:
        """Scan for WiFi networks using iwlist"""
        networks = []
        
        try:
            result = subprocess.run(
                ['sudo', 'iwlist', self.interface, 'scan'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            current_network = {}
            
            for line in result.stdout.split('\n'):
                line = line.strip()
                
                if 'Cell' in line and 'Address:' in line:
                    if current_network.get('bssid'):
                        networks.append(self._create_network(current_network))
                    current_network = {'bssid': line.split('Address:')[1].strip()}
                    
                elif 'ESSID:' in line:
                    ssid = line.split('ESSID:')[1].strip('"')
                    current_network['ssid'] = ssid if ssid else '<hidden>'
                    
                elif 'Channel:' in line:
                    current_network['channel'] = int(line.split('Channel:')[1])
                    
                elif 'Signal level=' in line:
                    # Parse signal level
                    match = re.search(r'Signal level[=:](-?\d+)', line)
                    if match:
                        current_network['signal'] = int(match.group(1))
                        
                elif 'Encryption key:' in line:
                    current_network['encrypted'] = 'on' in line.lower()
                    
                elif 'WPA' in line or 'WPA2' in line:
                    current_network['encryption'] = 'WPA2' if 'WPA2' in line else 'WPA'
                    
            if current_network.get('bssid'):
                networks.append(self._create_network(current_network))
                
        except subprocess.TimeoutExpired:
            print(f"{Colors.YELLOW}[!] Scan timeout{Colors.END}")
        except PermissionError:
            print(f"{Colors.RED}[!] Need root privileges for WiFi scanning{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Scan error: {e}{Colors.END}")
            
        return networks
        
    def _create_network(self, data: Dict) -> WiFiNetwork:
        """Create WiFiNetwork from scan data"""
        bssid = data.get('bssid', 'unknown')
        
        # Update existing or create new
        if bssid in self.networks:
            net = self.networks[bssid]
            net.last_seen = datetime.now()
            net.times_seen += 1
            if 'signal' in data:
                net.signal = data['signal']
            return net
            
        network = WiFiNetwork(
            bssid=bssid,
            ssid=data.get('ssid', '<hidden>'),
            channel=data.get('channel', 0),
            signal=data.get('signal', -100),
            encryption=data.get('encryption', 'Open' if not data.get('encrypted') else 'WEP'),
            vendor=OUILookup.lookup(bssid)
        )
        
        self.networks[bssid] = network
        return network
        
    def continuous_scan(self, duration: int, callback=None) -> List[WiFiNetwork]:
        """Continuously scan for the specified duration"""
        start = time.time()
        all_networks = []
        
        while time.time() - start < duration:
            networks = self.scan_networks()
            all_networks.extend(networks)
            
            if callback:
                callback(networks)
                
            time.sleep(2)  # Avoid hammering the interface
            
        return list(self.networks.values())


class BluetoothScanner:
    """Bluetooth device discovery"""
    
    def __init__(self):
        self.devices: Dict[str, BluetoothDevice] = {}
        
    def scan(self, duration: int = 10) -> List[BluetoothDevice]:
        """Scan for Bluetooth devices"""
        devices = []
        
        # Try hcitool
        try:
            result = subprocess.run(
                ['hcitool', 'scan', '--length', str(duration)],
                capture_output=True,
                text=True,
                timeout=duration + 5
            )
            
            for line in result.stdout.split('\n')[1:]:  # Skip header
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    addr = parts[0]
                    name = parts[1] if len(parts) > 1 else None
                    
                    device = self._create_device(addr, name)
                    devices.append(device)
                    
        except Exception as e:
            print(f"{Colors.YELLOW}[!] Bluetooth scan error: {e}{Colors.END}")
            
        # Try BLE scan
        devices.extend(self._ble_scan(duration))
        
        return devices
        
    def _ble_scan(self, duration: int) -> List[BluetoothDevice]:
        """Scan for BLE devices"""
        devices = []
        
        try:
            result = subprocess.run(
                ['timeout', str(duration), 'hcitool', 'lescan'],
                capture_output=True,
                text=True
            )
            
            seen = set()
            for line in result.stdout.split('\n'):
                parts = line.strip().split()
                if len(parts) >= 1:
                    addr = parts[0]
                    if addr not in seen and ':' in addr:
                        seen.add(addr)
                        name = ' '.join(parts[1:]) if len(parts) > 1 else None
                        device = self._create_device(addr, name)
                        devices.append(device)
                        
        except Exception:
            pass  # BLE scan failed silently
            
        return devices
        
    def _create_device(self, address: str, name: str = None) -> BluetoothDevice:
        """Create or update Bluetooth device"""
        if address in self.devices:
            dev = self.devices[address]
            dev.last_seen = datetime.now()
            dev.times_seen += 1
            if name and not dev.name:
                dev.name = name
            return dev
            
        device = BluetoothDevice(
            address=address,
            name=name
        )
        self.devices[address] = device
        return device


class EnvironmentProfiler:
    """Create environmental profiles from ambient signals"""
    
    def __init__(self):
        self.signatures: List[AmbientSignature] = []
        self.wifi_scanner = WiFiScanner()
        self.bt_scanner = BluetoothScanner()
        
    def capture_signature(self) -> AmbientSignature:
        """Capture current environmental signature"""
        # Scan WiFi
        wifi_networks = self.wifi_scanner.scan_networks()
        
        # Scan Bluetooth
        bt_devices = self.bt_scanner.scan(5)
        
        # Build signal profile
        signal_profile = {
            net.bssid: net.signal
            for net in wifi_networks
        }
        
        # Get unique SSIDs
        unique_ssids = list(set(net.ssid for net in wifi_networks if net.ssid != '<hidden>'))
        
        # Try to infer location
        location_hint = self._infer_location(wifi_networks)
        
        signature = AmbientSignature(
            timestamp=datetime.now(),
            wifi_networks=len(wifi_networks),
            bluetooth_devices=len(bt_devices),
            unique_ssids=unique_ssids,
            signal_profile=signal_profile,
            location_hint=location_hint
        )
        
        self.signatures.append(signature)
        return signature
        
    def _infer_location(self, networks: List[WiFiNetwork]) -> Optional[str]:
        """Infer location from WiFi signatures"""
        # Look for common location indicators in SSIDs
        location_keywords = {
            'starbucks': 'Coffee Shop (Starbucks)',
            'mcdonalds': 'Fast Food (McDonalds)',
            'airport': 'Airport',
            'hotel': 'Hotel',
            'library': 'Library',
            'university': 'University/College',
            'hospital': 'Hospital',
            'guest': 'Guest Network (Unknown Venue)',
            'free': 'Public WiFi',
        }
        
        for net in networks:
            ssid_lower = net.ssid.lower()
            for keyword, location in location_keywords.items():
                if keyword in ssid_lower:
                    return location
                    
        # Check for residential vs commercial based on network count
        if len(networks) > 20:
            return 'High-density area (commercial/urban)'
        elif len(networks) < 5:
            return 'Low-density area (residential/rural)'
            
        return None
        
    def compare_signatures(self, sig1: AmbientSignature, sig2: AmbientSignature) -> float:
        """Compare two signatures and return similarity (0-1)"""
        # Compare SSIDs
        ssids1 = set(sig1.unique_ssids)
        ssids2 = set(sig2.unique_ssids)
        
        if not ssids1 or not ssids2:
            return 0.0
            
        intersection = len(ssids1 & ssids2)
        union = len(ssids1 | ssids2)
        jaccard = intersection / union if union > 0 else 0
        
        # Compare signal profiles
        common_bssids = set(sig1.signal_profile.keys()) & set(sig2.signal_profile.keys())
        
        if common_bssids:
            signal_diffs = [
                abs(sig1.signal_profile[b] - sig2.signal_profile[b])
                for b in common_bssids
            ]
            avg_diff = sum(signal_diffs) / len(signal_diffs)
            signal_similarity = max(0, 1 - (avg_diff / 50))  # 50 dBm difference = 0 similarity
        else:
            signal_similarity = 0
            
        # Combined similarity
        return (jaccard * 0.6) + (signal_similarity * 0.4)


class AmbientIntelligence:
    """Main ambient intelligence engine"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.profiler = EnvironmentProfiler()
        self.history_file = Path.home() / '.ambient_history.json'
        self.history = self._load_history()
        
    def _load_history(self) -> Dict:
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except:
            return {'signatures': [], 'known_locations': {}}
            
    def _save_history(self):
        # Convert signatures to serializable format
        history = {
            'signatures': [
                {
                    'timestamp': s.timestamp.isoformat(),
                    'wifi_networks': s.wifi_networks,
                    'bluetooth_devices': s.bluetooth_devices,
                    'unique_ssids': s.unique_ssids,
                    'signal_profile': s.signal_profile,
                    'location_hint': s.location_hint
                }
                for s in self.profiler.signatures[-100:]  # Keep last 100
            ],
            'known_locations': self.history.get('known_locations', {})
        }
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
            
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[AMBIENT]{Colors.END} {msg}")
            
    def scan(self) -> Dict:
        """Perform ambient scan"""
        self.log("Capturing environmental signature...")
        
        signature = self.profiler.capture_signature()
        
        results = {
            'timestamp': signature.timestamp.isoformat(),
            'wifi': {
                'networks': signature.wifi_networks,
                'ssids': signature.unique_ssids,
                'signal_profile': signature.signal_profile
            },
            'bluetooth': {
                'devices': signature.bluetooth_devices
            },
            'location_hint': signature.location_hint,
            'environment_hash': self._hash_signature(signature)
        }
        
        self._save_history()
        return results
        
    def _hash_signature(self, sig: AmbientSignature) -> str:
        """Create unique hash for environment"""
        import hashlib
        data = json.dumps(sorted(sig.unique_ssids)).encode()
        return hashlib.sha256(data).hexdigest()[:16]
        
    def monitor(self, duration: int, interval: int = 30):
        """Monitor environment over time"""
        start = time.time()
        
        while time.time() - start < duration:
            results = self.scan()
            yield results
            time.sleep(interval)
            
    def detect_changes(self) -> List[Dict]:
        """Detect environmental changes since last scan"""
        if len(self.profiler.signatures) < 2:
            return []
            
        changes = []
        current = self.profiler.signatures[-1]
        previous = self.profiler.signatures[-2]
        
        # New networks
        current_ssids = set(current.unique_ssids)
        previous_ssids = set(previous.unique_ssids)
        
        new_ssids = current_ssids - previous_ssids
        gone_ssids = previous_ssids - current_ssids
        
        if new_ssids:
            changes.append({
                'type': 'new_networks',
                'networks': list(new_ssids)
            })
            
        if gone_ssids:
            changes.append({
                'type': 'networks_disappeared',
                'networks': list(gone_ssids)
            })
            
        # Significant signal changes
        for bssid in set(current.signal_profile.keys()) & set(previous.signal_profile.keys()):
            diff = current.signal_profile[bssid] - previous.signal_profile[bssid]
            if abs(diff) > 20:
                changes.append({
                    'type': 'signal_change',
                    'bssid': bssid,
                    'change': diff
                })
                
        return changes


def main():
    parser = argparse.ArgumentParser(
        description='AMBIENT - Environmental Intelligence Gathering',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single ambient scan
  ambient.py scan
  
  # Continuous monitoring
  ambient.py monitor --duration 3600 --interval 60
  
  # WiFi only scan
  ambient.py wifi
  
  # Bluetooth only scan
  ambient.py bluetooth
  
  # Export environmental profile
  ambient.py scan -o profile.json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Single ambient scan')
    scan_parser.add_argument('-o', '--output', help='Output JSON file')
    scan_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Continuous monitoring')
    monitor_parser.add_argument('-d', '--duration', type=int, default=3600, help='Duration in seconds')
    monitor_parser.add_argument('-i', '--interval', type=int, default=60, help='Scan interval')
    monitor_parser.add_argument('-v', '--verbose', action='store_true')
    
    # WiFi command
    wifi_parser = subparsers.add_parser('wifi', help='WiFi only scan')
    wifi_parser.add_argument('-c', '--continuous', action='store_true', help='Continuous scan')
    wifi_parser.add_argument('-d', '--duration', type=int, default=30, help='Scan duration')
    wifi_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Bluetooth command
    bt_parser = subparsers.add_parser('bluetooth', help='Bluetooth only scan')
    bt_parser.add_argument('-d', '--duration', type=int, default=10, help='Scan duration')
    bt_parser.add_argument('-v', '--verbose', action='store_true')
    
    args = parser.parse_args()
    
    if not args.command:
        print(BANNER)
        parser.print_help()
        return
        
    print(BANNER)
    
    if args.command == 'scan':
        ambient = AmbientIntelligence(verbose=args.verbose)
        
        print(f"\n{Colors.CYAN}[*] Capturing environmental signature...{Colors.END}\n")
        
        results = ambient.scan()
        
        print(f"{Colors.BOLD}═══ AMBIENT SCAN RESULTS ═══{Colors.END}")
        print(f"\n{Colors.GREEN}WiFi Networks:{Colors.END} {results['wifi']['networks']}")
        
        if results['wifi']['ssids']:
            print(f"  SSIDs:")
            for ssid in results['wifi']['ssids'][:10]:
                print(f"    • {ssid}")
            if len(results['wifi']['ssids']) > 10:
                print(f"    ... and {len(results['wifi']['ssids']) - 10} more")
                
        print(f"\n{Colors.BLUE}Bluetooth Devices:{Colors.END} {results['bluetooth']['devices']}")
        
        if results['location_hint']:
            print(f"\n{Colors.YELLOW}Location Hint:{Colors.END} {results['location_hint']}")
            
        print(f"\n{Colors.DIM}Environment Hash: {results['environment_hash']}{Colors.END}")
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\n{Colors.GREEN}Results saved to {args.output}{Colors.END}")
            
        print(f"\n{Colors.MAGENTA}\"More and more information, less and less meaning.\"{Colors.END}\n")
        
    elif args.command == 'monitor':
        ambient = AmbientIntelligence(verbose=args.verbose)
        
        print(f"{Colors.CYAN}[*] Starting ambient monitoring for {args.duration}s...{Colors.END}")
        print(f"    Scan interval: {args.interval}s")
        print(f"    Press Ctrl+C to stop\n")
        
        try:
            for results in ambient.monitor(args.duration, args.interval):
                changes = ambient.detect_changes()
                
                ts = datetime.now().strftime('%H:%M:%S')
                print(f"[{ts}] WiFi: {results['wifi']['networks']} | BT: {results['bluetooth']['devices']}", end='')
                
                if changes:
                    print(f" | {Colors.YELLOW}Changes: {len(changes)}{Colors.END}")
                    for change in changes:
                        if change['type'] == 'new_networks':
                            print(f"    {Colors.GREEN}+ New: {', '.join(change['networks'][:3])}{Colors.END}")
                        elif change['type'] == 'networks_disappeared':
                            print(f"    {Colors.RED}- Gone: {', '.join(change['networks'][:3])}{Colors.END}")
                else:
                    print()
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[*] Monitoring stopped{Colors.END}")
            
    elif args.command == 'wifi':
        scanner = WiFiScanner()
        
        if args.continuous:
            print(f"{Colors.CYAN}[*] Continuous WiFi scan for {args.duration}s...{Colors.END}")
            networks = scanner.continuous_scan(args.duration)
        else:
            print(f"{Colors.CYAN}[*] Scanning WiFi networks...{Colors.END}")
            networks = scanner.scan_networks()
            
        print(f"\n{Colors.BOLD}Found {len(networks)} networks:{Colors.END}\n")
        
        for net in sorted(networks, key=lambda x: x.signal, reverse=True):
            signal_bar = '█' * max(0, min(5, (net.signal + 100) // 20))
            enc_color = Colors.GREEN if net.encryption == 'Open' else Colors.YELLOW
            
            print(f"  {net.ssid[:20]:<20} {signal_bar:<5} {net.signal:>4}dBm  "
                  f"Ch{net.channel:<2}  {enc_color}{net.encryption:<6}{Colors.END}  {net.bssid}")
            if net.vendor:
                print(f"    {Colors.DIM}Vendor: {net.vendor}{Colors.END}")
                
    elif args.command == 'bluetooth':
        scanner = BluetoothScanner()
        
        print(f"{Colors.CYAN}[*] Scanning Bluetooth devices for {args.duration}s...{Colors.END}")
        devices = scanner.scan(args.duration)
        
        print(f"\n{Colors.BOLD}Found {len(devices)} devices:{Colors.END}\n")
        
        for dev in devices:
            name = dev.name or '<unknown>'
            print(f"  {dev.address}  {name}")


if __name__ == '__main__':
    main()
