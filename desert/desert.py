#!/usr/bin/env python3
"""
DESERT OF THE REAL - System Entropy Analyzer
=============================================
"Welcome to the desert of the real."
— Jean Baudrillard (via The Matrix)

Measures the entropy and authenticity of system states.
Finds where reality has been replaced by simulation.
"""

import os
import sys
import math
import json
import hashlib
import argparse
from datetime import datetime
from pathlib import Path
from collections import Counter

BANNER = """
██████╗ ███████╗███████╗███████╗██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝
██║  ██║█████╗  ███████╗█████╗  ██████╔╝   ██║   
██║  ██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗   ██║   
██████╔╝███████╗███████║███████╗██║  ██║   ██║   
╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
    [ SYSTEM ENTROPY ANALYZER | baudrillard-suite ]
"""

class DesertAnalyzer:
    """Analyze system entropy to find the desert of the real"""
    
    def __init__(self):
        self.findings = []
        self.entropy_scores = {}
        self.simulation_markers = []
        
    def calculate_entropy(self, data):
        """Calculate Shannon entropy of data"""
        if not data:
            return 0.0
        counter = Counter(data)
        length = len(data)
        entropy = 0.0
        for count in counter.values():
            if count > 0:
                prob = count / length
                entropy -= prob * math.log2(prob)
        return entropy
        
    def analyze_file(self, filepath):
        """Analyze single file for simulation markers"""
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
        except Exception as e:
            return None
            
        entropy = self.calculate_entropy(data)
        hash_val = hashlib.sha256(data).hexdigest()
        
        result = {
            'path': str(filepath),
            'size': len(data),
            'entropy': entropy,
            'hash': hash_val,
            'simulation_score': self._simulation_score(data, entropy)
        }
        
        # Check for known simulation patterns
        if self._check_synthetic(data):
            result['synthetic'] = True
            self.simulation_markers.append(filepath)
            
        return result
        
    def _simulation_score(self, data, entropy):
        """Calculate how likely data is simulated"""
        score = 0.0
        
        # Very low or very high entropy is suspicious
        if entropy < 1.0:
            score += 0.3  # Too ordered
        elif entropy > 7.5:
            score += 0.2  # Too random (likely encrypted/compressed)
            
        # Check for null byte patterns
        null_ratio = data.count(b'\x00') / len(data) if data else 0
        if null_ratio > 0.5:
            score += 0.2
            
        # Check for repeating patterns
        if len(data) > 100:
            chunk_size = 16
            chunks = [data[i:i+chunk_size] for i in range(0, len(data)-chunk_size, chunk_size)]
            unique_ratio = len(set(chunks)) / len(chunks) if chunks else 1
            if unique_ratio < 0.1:
                score += 0.3
                
        return min(score, 1.0)
        
    def _check_synthetic(self, data):
        """Check for synthetic/generated data markers"""
        markers = [
            b'JFIF',      # JPEG
            b'PNG',       # PNG  
            b'GIF8',      # GIF
            b'%PDF',      # PDF
            b'PK\x03\x04', # ZIP
        ]
        
        # Not synthetic if it's a known format
        for marker in markers:
            if data.startswith(marker):
                return False
                
        # Check for suspiciously regular patterns
        if len(data) > 256:
            # Sample every 64 bytes
            samples = [data[i] for i in range(0, min(len(data), 4096), 64)]
            if len(set(samples)) < 5:
                return True
                
        return False
        
    def analyze_directory(self, dirpath, recursive=True):
        """Analyze all files in directory"""
        results = []
        
        path = Path(dirpath)
        pattern = '**/*' if recursive else '*'
        
        for filepath in path.glob(pattern):
            if filepath.is_file():
                result = self.analyze_file(filepath)
                if result:
                    results.append(result)
                    self.entropy_scores[str(filepath)] = result['entropy']
                    
        return results
        
    def analyze_memory(self):
        """Analyze /proc for memory simulation markers"""
        results = []
        
        if not os.path.exists('/proc'):
            return results
            
        # Check /proc/meminfo
        try:
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                
            lines = meminfo.strip().split('\n')
            mem_data = {}
            for line in lines:
                if ':' in line:
                    key, val = line.split(':', 1)
                    mem_data[key.strip()] = val.strip()
                    
            # Check for VM signatures
            total = int(mem_data.get('MemTotal', '0').split()[0])
            if total % 1048576 == 0:  # Exactly divisible by 1GB
                results.append({
                    'type': 'memory_alignment',
                    'description': 'Memory size suspiciously aligned (VM?)',
                    'value': total
                })
                
        except Exception:
            pass
            
        # Check /proc/cpuinfo for hypervisor
        try:
            with open('/proc/cpuinfo', 'r') as f:
                cpuinfo = f.read().lower()
                
            vm_markers = ['hypervisor', 'vmware', 'virtualbox', 'kvm', 'qemu', 'xen']
            for marker in vm_markers:
                if marker in cpuinfo:
                    results.append({
                        'type': 'hypervisor_detected',
                        'description': f'Running in simulation: {marker}',
                        'value': marker
                    })
                    
        except Exception:
            pass
            
        return results
        
    def generate_report(self):
        """Generate desert of the real report"""
        memory_analysis = self.analyze_memory()
        
        avg_entropy = (sum(self.entropy_scores.values()) / 
                      len(self.entropy_scores)) if self.entropy_scores else 0
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'files_analyzed': len(self.entropy_scores),
            'average_entropy': avg_entropy,
            'simulation_markers': len(self.simulation_markers),
            'memory_analysis': memory_analysis,
            'entropy_distribution': self._entropy_distribution(),
            'reality_assessment': self._assess_reality(memory_analysis)
        }
        
        return report
        
    def _entropy_distribution(self):
        """Categorize entropy scores"""
        dist = {'low': 0, 'medium': 0, 'high': 0, 'maximum': 0}
        for entropy in self.entropy_scores.values():
            if entropy < 2:
                dist['low'] += 1
            elif entropy < 5:
                dist['medium'] += 1
            elif entropy < 7:
                dist['high'] += 1
            else:
                dist['maximum'] += 1
        return dist
        
    def _assess_reality(self, memory_analysis):
        """Final assessment of reality status"""
        score = 100
        
        # Deduct for simulation markers
        score -= len(self.simulation_markers) * 5
        
        # Deduct for VM detection
        score -= len(memory_analysis) * 15
        
        # Deduct for entropy anomalies
        dist = self._entropy_distribution()
        if dist['low'] > dist['medium']:
            score -= 10
            
        score = max(0, score)
        
        if score > 80:
            return f"Reality Index: {score}% - Likely base reality"
        elif score > 50:
            return f"Reality Index: {score}% - Possible simulation layer"
        elif score > 20:
            return f"Reality Index: {score}% - Probable simulation"
        else:
            return f"Reality Index: {score}% - Welcome to the desert of the real"


def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description="Desert - System Entropy Analyzer"
    )
    parser.add_argument("-d", "--directory", help="Directory to analyze")
    parser.add_argument("-f", "--file", help="Single file to analyze")
    parser.add_argument("-m", "--memory", action="store_true",
                       help="Analyze system memory/VM status")
    parser.add_argument("-o", "--output", help="Output JSON file")
    parser.add_argument("-r", "--recursive", action="store_true",
                       help="Recursive directory scan")
    
    args = parser.parse_args()
    
    analyzer = DesertAnalyzer()
    
    if args.file:
        result = analyzer.analyze_file(args.file)
        if result:
            print(f"\n[FILE] {result['path']}")
            print(f"  Entropy: {result['entropy']:.4f}")
            print(f"  Simulation Score: {result['simulation_score']:.2f}")
            print(f"  SHA256: {result['hash'][:32]}...")
            
    elif args.directory:
        print(f"[*] Analyzing directory: {args.directory}")
        results = analyzer.analyze_directory(args.directory, args.recursive)
        print(f"[*] Analyzed {len(results)} files")
        
    if args.memory or not (args.file or args.directory):
        print("\n[*] Analyzing system memory...")
        
    report = analyzer.generate_report()
    
    print("\n" + "="*60)
    print("DESERT OF THE REAL - ANALYSIS REPORT")
    print("="*60)
    
    print(f"\n{report['reality_assessment']}")
    
    print(f"\n[FILES] {report['files_analyzed']} analyzed")
    print(f"[ENTROPY] Average: {report['average_entropy']:.4f}")
    print(f"[MARKERS] {report['simulation_markers']} simulation markers")
    
    if report['memory_analysis']:
        print("\n[MEMORY ANALYSIS]")
        for finding in report['memory_analysis']:
            print(f"  ⚠ {finding['type']}: {finding['description']}")
            
    print("\n[ENTROPY DISTRIBUTION]")
    for level, count in report['entropy_distribution'].items():
        bar = '█' * min(count, 30)
        print(f"  {level:8}: {bar} ({count})")
        
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n[*] Report saved: {args.output}")


if __name__ == "__main__":
    main()
