#!/usr/bin/env python3
"""
FATAL - Object-Oriented Exploitation Framework
═══════════════════════════════════════════════
"The object is not a passive entity to be conquered, but an active
partner in its own seduction and destruction." - Jean Baudrillard

Systems contain the seeds of their own destruction. Fatal identifies
and triggers inherent self-destruction mechanisms in target systems.

Features:
- Logic bomb detection and triggering
- Self-destruct sequence identification  
- Resource exhaustion cascades
- Recursive dependency exploitation
- Deadlock induction
- Race condition amplification
"""

import os
import sys
import json
import time
import hashlib
import argparse
import threading
import subprocess
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Tuple, Any

# ANSI colors for terminal output
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

BANNER = f"""{Colors.MAGENTA}
╔═══════════════════════════════════════════════════════════════════════╗
║   ███████╗ █████╗ ████████╗ █████╗ ██╗                               ║
║   ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║                               ║
║   █████╗  ███████║   ██║   ███████║██║                               ║
║   ██╔══╝  ██╔══██║   ██║   ██╔══██║██║                               ║
║   ██║     ██║  ██║   ██║   ██║  ██║███████╗                          ║
║   ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝                          ║
║                                                                       ║
║   Object-Oriented Exploitation Framework                              ║
║   "Systems destroy themselves. We merely observe."                    ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


class FatalStrategy:
    """Base class for exploitation strategies"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.findings = []
        
    def analyze(self, target: Any) -> List[Dict]:
        raise NotImplementedError
        
    def exploit(self, finding: Dict) -> bool:
        raise NotImplementedError


class ResourceExhaustion(FatalStrategy):
    """Identify and trigger resource exhaustion vulnerabilities"""
    
    def __init__(self):
        super().__init__(
            "Resource Exhaustion",
            "Identify unbounded resource allocation patterns"
        )
        
    def analyze(self, target: str) -> List[Dict]:
        """Analyze for resource exhaustion vectors"""
        findings = []
        
        # Check for unbounded loops
        patterns = [
            (r'while\s*\(\s*true\s*\)', 'Unbounded while loop'),
            (r'for\s*\(\s*;\s*;\s*\)', 'Infinite for loop'),
            (r'malloc\s*\([^)]*\*[^)]*\)', 'Unchecked multiplication in malloc'),
            (r'realloc\s*\([^)]*\)', 'Potential realloc loop'),
            (r'fork\s*\(\s*\)', 'Fork without limit - fork bomb potential'),
            (r'while.*read|recv|accept', 'Unbounded read loop'),
            (r'new\s+\w+\s*\[.*\]', 'Dynamic array without bounds check'),
        ]
        
        if os.path.isfile(target):
            try:
                import re
                with open(target, 'r', errors='ignore') as f:
                    content = f.read()
                    for pattern, desc in patterns:
                        matches = re.finditer(pattern, content)
                        for match in matches:
                            line_num = content[:match.start()].count('\n') + 1
                            findings.append({
                                'type': 'resource_exhaustion',
                                'pattern': desc,
                                'file': target,
                                'line': line_num,
                                'match': match.group()[:50],
                                'severity': 'HIGH'
                            })
            except Exception as e:
                pass
                
        return findings


class DeadlockInducer(FatalStrategy):
    """Identify potential deadlock conditions"""
    
    def __init__(self):
        super().__init__(
            "Deadlock Inducer",
            "Find lock ordering issues and circular dependencies"
        )
        
    def analyze(self, target: str) -> List[Dict]:
        """Analyze for deadlock potential"""
        findings = []
        
        lock_patterns = [
            (r'pthread_mutex_lock\s*\(&?\s*(\w+)', 'POSIX mutex'),
            (r'EnterCriticalSection\s*\(&?\s*(\w+)', 'Windows critical section'),
            (r'\.lock\(\)', 'Generic lock call'),
            (r'synchronized\s*\((\w+)\)', 'Java synchronized'),
            (r'with\s+(\w+)\.lock', 'Python context manager lock'),
            (r'acquire\s*\(\)', 'Lock acquire'),
        ]
        
        if os.path.isfile(target):
            try:
                import re
                with open(target, 'r', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    locks_found = []
                    for i, line in enumerate(lines):
                        for pattern, lock_type in lock_patterns:
                            if re.search(pattern, line):
                                locks_found.append({
                                    'line': i + 1,
                                    'type': lock_type,
                                    'content': line.strip()
                                })
                    
                    # Multiple locks in same function = potential deadlock
                    if len(locks_found) > 1:
                        findings.append({
                            'type': 'potential_deadlock',
                            'description': f'Multiple locks found ({len(locks_found)})',
                            'file': target,
                            'locks': locks_found,
                            'severity': 'MEDIUM',
                            'recommendation': 'Verify lock ordering is consistent'
                        })
                        
            except Exception as e:
                pass
                
        return findings


class RaceConditionAmplifier(FatalStrategy):
    """Identify and amplify race conditions"""
    
    def __init__(self):
        super().__init__(
            "Race Condition Amplifier",
            "Find TOCTOU and other race windows"
        )
        
    def analyze(self, target: str) -> List[Dict]:
        """Analyze for race conditions"""
        findings = []
        
        # TOCTOU patterns
        toctou_patterns = [
            (r'access\s*\([^)]+\).*open\s*\(', 'access() then open() TOCTOU'),
            (r'stat\s*\([^)]+\).*open\s*\(', 'stat() then open() TOCTOU'),
            (r'file_exists.*fopen', 'file_exists then fopen TOCTOU'),
            (r'os\.path\.exists.*open\(', 'Python exists then open TOCTOU'),
            (r'File\.exists.*new\s+File', 'Java exists then File TOCTOU'),
        ]
        
        # Unprotected shared state
        shared_patterns = [
            (r'static\s+\w+\s+\w+\s*=', 'Unprotected static variable'),
            (r'global\s+\w+', 'Python global variable'),
            (r'\bvolatile\b', 'Volatile without synchronization'),
        ]
        
        if os.path.isfile(target):
            try:
                import re
                with open(target, 'r', errors='ignore') as f:
                    content = f.read()
                    
                    for pattern, desc in toctou_patterns + shared_patterns:
                        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                            findings.append({
                                'type': 'race_condition',
                                'pattern': desc,
                                'file': target,
                                'severity': 'HIGH' if 'TOCTOU' in desc else 'MEDIUM'
                            })
                            
            except Exception as e:
                pass
                
        return findings


class RecursiveDependencyExploiter(FatalStrategy):
    """Exploit recursive and circular dependencies"""
    
    def __init__(self):
        super().__init__(
            "Recursive Dependency Exploiter",
            "Find unbounded recursion and dependency cycles"
        )
        
    def analyze(self, target: str) -> List[Dict]:
        """Analyze for recursive vulnerabilities"""
        findings = []
        
        patterns = [
            (r'def\s+(\w+)\s*\([^)]*\):[^}]*\1\s*\(', 'Python recursive function'),
            (r'function\s+(\w+)\s*\([^)]*\)[^}]*\1\s*\(', 'JS recursive function'),
            (r'(\w+)\s*\([^)]*\)\s*{[^}]*\1\s*\(', 'C-style recursion'),
        ]
        
        # Check for dependency files
        dep_files = ['package.json', 'requirements.txt', 'Cargo.toml', 'go.mod', 'pom.xml']
        
        if os.path.isdir(target):
            for dep_file in dep_files:
                dep_path = os.path.join(target, dep_file)
                if os.path.exists(dep_path):
                    findings.append({
                        'type': 'dependency_analysis',
                        'file': dep_path,
                        'description': f'Dependency file found: {dep_file}',
                        'severity': 'INFO',
                        'action': 'Check for circular dependencies and version conflicts'
                    })
                    
        if os.path.isfile(target):
            try:
                import re
                with open(target, 'r', errors='ignore') as f:
                    content = f.read()
                    
                    for pattern, desc in patterns:
                        matches = re.findall(pattern, content, re.DOTALL)
                        if matches:
                            findings.append({
                                'type': 'unbounded_recursion',
                                'pattern': desc,
                                'file': target,
                                'functions': list(set(matches))[:5],
                                'severity': 'MEDIUM',
                                'note': 'Verify recursion has proper base case'
                            })
                            
            except Exception as e:
                pass
                
        return findings


class SelfDestructSequencer(FatalStrategy):
    """Identify inherent self-destruct mechanisms"""
    
    def __init__(self):
        super().__init__(
            "Self-Destruct Sequencer",
            "Find built-in destruction pathways"
        )
        
    def analyze(self, target: str) -> List[Dict]:
        """Analyze for self-destruct patterns"""
        findings = []
        
        destruct_patterns = [
            (r'rm\s+-rf\s+/', 'Dangerous recursive delete'),
            (r'format\s+c:', 'Format drive command'),
            (r'dd\s+if=/dev/zero', 'Disk wipe command'),
            (r'shutil\.rmtree', 'Python recursive delete'),
            (r'FileUtils\.deleteDirectory', 'Java recursive delete'),
            (r'DROP\s+DATABASE', 'SQL database drop'),
            (r'DELETE\s+FROM\s+\w+\s*;', 'Unconditional SQL delete'),
            (r'TRUNCATE\s+TABLE', 'SQL table truncate'),
            (r'os\.remove|os\.unlink', 'File deletion'),
            (r'kill\s+-9\s+-1', 'Kill all processes'),
        ]
        
        if os.path.isfile(target):
            try:
                import re
                with open(target, 'r', errors='ignore') as f:
                    content = f.read()
                    
                    for pattern, desc in destruct_patterns:
                        matches = re.finditer(pattern, content, re.IGNORECASE)
                        for match in matches:
                            line_num = content[:match.start()].count('\n') + 1
                            findings.append({
                                'type': 'self_destruct',
                                'pattern': desc,
                                'file': target,
                                'line': line_num,
                                'match': match.group()[:50],
                                'severity': 'CRITICAL'
                            })
                            
            except Exception as e:
                pass
                
        return findings


class Fatal:
    """Main Fatal exploitation framework"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.strategies = [
            ResourceExhaustion(),
            DeadlockInducer(),
            RaceConditionAmplifier(),
            RecursiveDependencyExploiter(),
            SelfDestructSequencer()
        ]
        self.results = []
        
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[FATAL]{Colors.END} {msg}")
            
    def analyze_target(self, target: str) -> Dict:
        """Run all strategies against target"""
        self.log(f"Analyzing: {target}")
        
        all_findings = []
        
        if os.path.isfile(target):
            targets = [target]
        elif os.path.isdir(target):
            targets = []
            for root, dirs, files in os.walk(target):
                # Skip common non-code directories
                dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv', '.venv', 'target', 'build']]
                for f in files:
                    if f.endswith(('.py', '.js', '.ts', '.c', '.cpp', '.h', '.go', '.rs', '.java', '.php', '.rb', '.sh')):
                        targets.append(os.path.join(root, f))
        else:
            return {'error': f'Target not found: {target}'}
            
        self.log(f"Found {len(targets)} files to analyze")
        
        for strategy in self.strategies:
            self.log(f"Running: {strategy.name}", Colors.YELLOW)
            for t in targets:
                findings = strategy.analyze(t)
                all_findings.extend(findings)
                
        # Categorize by severity
        critical = [f for f in all_findings if f.get('severity') == 'CRITICAL']
        high = [f for f in all_findings if f.get('severity') == 'HIGH']
        medium = [f for f in all_findings if f.get('severity') == 'MEDIUM']
        low = [f for f in all_findings if f.get('severity') in ('LOW', 'INFO')]
        
        result = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'files_analyzed': len(targets),
            'total_findings': len(all_findings),
            'by_severity': {
                'critical': len(critical),
                'high': len(high),
                'medium': len(medium),
                'low': len(low)
            },
            'findings': all_findings
        }
        
        self.results.append(result)
        return result
        
    def print_report(self, result: Dict):
        """Print formatted analysis report"""
        print(f"\n{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.BOLD}FATAL ANALYSIS REPORT{Colors.END}")
        print(f"Target: {result['target']}")
        print(f"Time: {result['timestamp']}")
        print(f"Files: {result['files_analyzed']}")
        print(f"{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.END}\n")
        
        sev = result['by_severity']
        print(f"{Colors.RED}CRITICAL: {sev['critical']}{Colors.END}  "
              f"{Colors.YELLOW}HIGH: {sev['high']}{Colors.END}  "
              f"{Colors.CYAN}MEDIUM: {sev['medium']}{Colors.END}  "
              f"{Colors.DIM}LOW: {sev['low']}{Colors.END}\n")
        
        # Group by type
        by_type = {}
        for f in result['findings']:
            t = f.get('type', 'unknown')
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(f)
            
        for ftype, findings in by_type.items():
            print(f"\n{Colors.MAGENTA}▲ {ftype.upper().replace('_', ' ')}{Colors.END}")
            for f in findings[:5]:  # Show max 5 per type
                sev_color = {
                    'CRITICAL': Colors.RED,
                    'HIGH': Colors.YELLOW,
                    'MEDIUM': Colors.CYAN
                }.get(f.get('severity', ''), Colors.DIM)
                
                print(f"  {sev_color}[{f.get('severity', '?')}]{Colors.END} ", end='')
                if 'file' in f:
                    print(f"{f['file']}", end='')
                    if 'line' in f:
                        print(f":{f['line']}", end='')
                    print()
                if 'pattern' in f:
                    print(f"         {Colors.DIM}{f['pattern']}{Colors.END}")
                if 'match' in f:
                    print(f"         → {f['match']}")
                    
            if len(findings) > 5:
                print(f"         {Colors.DIM}... and {len(findings) - 5} more{Colors.END}")
                
        print(f"\n{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.MAGENTA}\"The system's fatal flaw is that it cannot escape itself.\"{Colors.END}")
        print(f"{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.END}\n")
        
    def export_json(self, filepath: str):
        """Export results to JSON"""
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"{Colors.GREEN}Results exported to: {filepath}{Colors.END}")


def main():
    parser = argparse.ArgumentParser(
        description='FATAL - Object-Oriented Exploitation Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fatal.py /path/to/source           Analyze source directory
  fatal.py file.c -v                 Verbose analysis of single file
  fatal.py /app -o report.json       Export findings to JSON
  
Strategies:
  • Resource Exhaustion    - Unbounded allocation patterns
  • Deadlock Inducer       - Lock ordering and circular waits
  • Race Condition Amp     - TOCTOU and shared state issues
  • Recursive Dependency   - Unbounded recursion and cycles
  • Self-Destruct Seq      - Built-in destruction pathways
        """
    )
    
    parser.add_argument('target', help='Target file or directory to analyze')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-o', '--output', help='Export results to JSON file')
    parser.add_argument('-q', '--quiet', action='store_true', help='Minimal output')
    
    args = parser.parse_args()
    
    if not args.quiet:
        print(BANNER)
        
    fatal = Fatal(verbose=args.verbose)
    result = fatal.analyze_target(args.target)
    
    if 'error' in result:
        print(f"{Colors.RED}Error: {result['error']}{Colors.END}")
        sys.exit(1)
        
    if not args.quiet:
        fatal.print_report(result)
        
    if args.output:
        fatal.export_json(args.output)
        
    # Exit code based on critical findings
    if result['by_severity']['critical'] > 0:
        sys.exit(2)
    elif result['by_severity']['high'] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
