#!/usr/bin/env python3
"""
GLITCH - Reality Corruption Engine
═══════════════════════════════════
"The only revolution is the corruption of the real."
- Jean Baudrillard

Fuzzing and corruption toolkit that introduces calculated
chaos into systems to reveal their true nature. Sometimes
breaking things shows you how they really work.

Features:
- Smart fuzzing engine
- Protocol mutation
- Format corruption
- Entropy injection
- Crash analysis
- Pattern-based glitching
"""

import os
import sys
import json
import struct
import random
import argparse
import hashlib
import time
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Callable, Any
from dataclasses import dataclass, field
from io import BytesIO

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

BANNER = f"""{Colors.MAGENTA}
╔═══════════════════════════════════════════════════════════════════════╗
║          ██████╗ ██╗     ██╗████████╗ ██████╗██╗  ██╗                  ║
║         ██╔════╝ ██║     ██║╚══██╔══╝██╔════╝██║  ██║                  ║
║         ██║  ███╗██║     ██║   ██║   ██║     ███████║                  ║
║         ██║   ██║██║     ██║   ██║   ██║     ██╔══██║                  ║
║         ╚██████╔╝███████╗██║   ██║   ╚██████╗██║  ██║                  ║
║          ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝                  ║
║                                                                       ║
║         Reality Corruption Engine                                     ║
║         "The only revolution is the corruption of the real."          ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


@dataclass
class Mutation:
    """A single mutation operation"""
    offset: int
    original: bytes
    mutated: bytes
    strategy: str
    description: str


@dataclass
class GlitchResult:
    """Result of a glitch operation"""
    input_hash: str
    output_hash: str
    mutations: List[Mutation]
    crashed: bool = False
    crash_info: Optional[str] = None
    interesting: bool = False
    timestamp: datetime = field(default_factory=datetime.now)


class MutationStrategy:
    """Base class for mutation strategies"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    def mutate(self, data: bytes, position: int) -> Tuple[bytes, Mutation]:
        raise NotImplementedError


class BitFlip(MutationStrategy):
    """Flip random bits"""
    
    def __init__(self):
        super().__init__("BitFlip", "Flip individual bits")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        data = bytearray(data)
        if position is None:
            position = random.randint(0, len(data) - 1)
            
        bit = random.randint(0, 7)
        original = bytes([data[position]])
        data[position] ^= (1 << bit)
        mutated = bytes([data[position]])
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=mutated,
            strategy=self.name,
            description=f"Flipped bit {bit} at offset {position}"
        )
        
        return bytes(data), mutation


class ByteOverwrite(MutationStrategy):
    """Overwrite bytes with interesting values"""
    
    INTERESTING_BYTES = [
        0x00, 0x01, 0x7f, 0x80, 0xff,
        0x41,  # 'A'
        0x0a, 0x0d,  # newlines
        0x20,  # space
    ]
    
    def __init__(self):
        super().__init__("ByteOverwrite", "Replace bytes with interesting values")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        data = bytearray(data)
        if position is None:
            position = random.randint(0, len(data) - 1)
            
        original = bytes([data[position]])
        new_byte = random.choice(self.INTERESTING_BYTES)
        data[position] = new_byte
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=bytes([new_byte]),
            strategy=self.name,
            description=f"Overwrote byte at {position} with 0x{new_byte:02x}"
        )
        
        return bytes(data), mutation


class IntegerBoundary(MutationStrategy):
    """Replace integers with boundary values"""
    
    BOUNDARIES = [
        (0, 1, b'\x00'),
        (0, 1, b'\xff'),
        (0, 2, b'\x00\x00'),
        (0, 2, b'\xff\xff'),
        (0, 4, b'\x00\x00\x00\x00'),
        (0, 4, b'\xff\xff\xff\xff'),
        (0, 4, b'\x7f\xff\xff\xff'),  # INT_MAX
        (0, 4, b'\x80\x00\x00\x00'),  # INT_MIN
    ]
    
    def __init__(self):
        super().__init__("IntegerBoundary", "Replace integers with boundary values")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        data = bytearray(data)
        _, size, value = random.choice(self.BOUNDARIES)
        
        if position is None:
            position = random.randint(0, max(0, len(data) - size))
            
        if position + size > len(data):
            size = len(data) - position
            value = value[:size]
            
        original = bytes(data[position:position + size])
        data[position:position + size] = value
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=value,
            strategy=self.name,
            description=f"Replaced {size} bytes at {position} with boundary value"
        )
        
        return bytes(data), mutation


class FormatString(MutationStrategy):
    """Inject format string specifiers"""
    
    FORMAT_STRINGS = [
        b'%s', b'%x', b'%n', b'%d',
        b'%s%s%s%s%s',
        b'AAAA%08x.%08x.%08x.%08x',
        b'%p%p%p%p',
    ]
    
    def __init__(self):
        super().__init__("FormatString", "Inject format string specifiers")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        data = bytearray(data)
        fmt = random.choice(self.FORMAT_STRINGS)
        
        if position is None:
            position = random.randint(0, max(0, len(data) - len(fmt)))
            
        original = bytes(data[position:position + len(fmt)])
        data[position:position + len(fmt)] = fmt
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=fmt,
            strategy=self.name,
            description=f"Injected format string {fmt!r} at {position}"
        )
        
        return bytes(data), mutation


class LengthCorruption(MutationStrategy):
    """Corrupt length fields"""
    
    def __init__(self):
        super().__init__("LengthCorruption", "Corrupt length fields with extreme values")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        data = bytearray(data)
        
        # Try to find potential length fields (small integers followed by data)
        candidates = []
        for i in range(len(data) - 4):
            val = struct.unpack('<I', data[i:i+4])[0]
            if 1 < val < len(data) - i:
                candidates.append(i)
                
        if not candidates and position is None:
            position = random.randint(0, max(0, len(data) - 4))
        elif position is None:
            position = random.choice(candidates)
            
        original = bytes(data[position:position + 4])
        
        # Corrupt with extreme value
        corrupt_value = random.choice([
            0xffffffff,  # Max
            0x7fffffff,  # Signed max
            0,           # Zero
            len(data) + 1000,  # Overflow
        ])
        
        data[position:position + 4] = struct.pack('<I', corrupt_value & 0xffffffff)
        mutated = bytes(data[position:position + 4])
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=mutated,
            strategy=self.name,
            description=f"Corrupted potential length field at {position} to 0x{corrupt_value:08x}"
        )
        
        return bytes(data), mutation


class Truncation(MutationStrategy):
    """Truncate data at random points"""
    
    def __init__(self):
        super().__init__("Truncation", "Truncate data at random positions")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        if position is None:
            position = random.randint(1, len(data) - 1)
            
        original = data[position:]
        truncated = data[:position]
        
        mutation = Mutation(
            offset=position,
            original=original,
            mutated=b'',
            strategy=self.name,
            description=f"Truncated data at position {position} (removed {len(original)} bytes)"
        )
        
        return truncated, mutation


class Duplication(MutationStrategy):
    """Duplicate sections of data"""
    
    def __init__(self):
        super().__init__("Duplication", "Duplicate sections of data")
        
    def mutate(self, data: bytes, position: int = None) -> Tuple[bytes, Mutation]:
        if position is None:
            position = random.randint(0, len(data) - 1)
            
        # Select a chunk to duplicate
        chunk_size = random.randint(1, min(100, len(data) - position))
        chunk = data[position:position + chunk_size]
        
        # Insert duplicate
        insert_pos = random.randint(0, len(data))
        result = data[:insert_pos] + chunk + data[insert_pos:]
        
        mutation = Mutation(
            offset=position,
            original=b'',
            mutated=chunk,
            strategy=self.name,
            description=f"Duplicated {chunk_size} bytes from {position} to {insert_pos}"
        )
        
        return result, mutation


class GlitchEngine:
    """Main fuzzing/glitching engine"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.strategies = [
            BitFlip(),
            ByteOverwrite(),
            IntegerBoundary(),
            FormatString(),
            LengthCorruption(),
            Truncation(),
            Duplication()
        ]
        self.results: List[GlitchResult] = []
        
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[GLITCH]{Colors.END} {msg}")
            
    def glitch(self, data: bytes, num_mutations: int = 1, 
               strategies: List[str] = None) -> Tuple[bytes, GlitchResult]:
        """Apply mutations to data"""
        input_hash = hashlib.sha256(data).hexdigest()[:16]
        mutations = []
        
        # Filter strategies
        if strategies:
            active_strategies = [s for s in self.strategies if s.name.lower() in [x.lower() for x in strategies]]
        else:
            active_strategies = self.strategies
            
        current_data = data
        
        for _ in range(num_mutations):
            strategy = random.choice(active_strategies)
            current_data, mutation = strategy.mutate(current_data)
            mutations.append(mutation)
            self.log(f"Applied {strategy.name}: {mutation.description}")
            
        output_hash = hashlib.sha256(current_data).hexdigest()[:16]
        
        result = GlitchResult(
            input_hash=input_hash,
            output_hash=output_hash,
            mutations=mutations
        )
        
        self.results.append(result)
        return current_data, result
        
    def glitch_file(self, input_path: str, output_path: str = None,
                    num_mutations: int = 1, strategies: List[str] = None) -> GlitchResult:
        """Glitch a file"""
        with open(input_path, 'rb') as f:
            data = f.read()
            
        glitched, result = self.glitch(data, num_mutations, strategies)
        
        if output_path is None:
            stem = Path(input_path).stem
            suffix = Path(input_path).suffix
            output_path = f"{stem}_glitched{suffix}"
            
        with open(output_path, 'wb') as f:
            f.write(glitched)
            
        self.log(f"Glitched file saved to {output_path}", Colors.GREEN)
        return result
        
    def fuzz_loop(self, template: bytes, iterations: int,
                  test_func: Callable[[bytes], bool] = None,
                  crash_dir: str = None) -> List[GlitchResult]:
        """Run continuous fuzzing loop"""
        interesting_results = []
        
        if crash_dir:
            Path(crash_dir).mkdir(parents=True, exist_ok=True)
            
        for i in range(iterations):
            num_mutations = random.randint(1, 5)
            glitched, result = self.glitch(template, num_mutations)
            
            if test_func:
                try:
                    crashed = test_func(glitched)
                    result.crashed = crashed
                    
                    if crashed:
                        result.interesting = True
                        interesting_results.append(result)
                        self.log(f"Iteration {i}: CRASH!", Colors.RED)
                        
                        if crash_dir:
                            crash_path = Path(crash_dir) / f"crash_{result.output_hash}.bin"
                            with open(crash_path, 'wb') as f:
                                f.write(glitched)
                                
                except Exception as e:
                    result.crash_info = str(e)
                    result.crashed = True
                    result.interesting = True
                    interesting_results.append(result)
                    
            if i % 100 == 0:
                print(f"{Colors.DIM}[{i}/{iterations}] {len(interesting_results)} interesting{Colors.END}", end='\r')
                
        return interesting_results
        
    def test_binary(self, binary_path: str, template: bytes, 
                    iterations: int, timeout: int = 2) -> List[GlitchResult]:
        """Fuzz a binary executable"""
        
        def test_func(data: bytes) -> bool:
            # Write to temp file
            import tempfile
            with tempfile.NamedTemporaryFile(delete=False) as f:
                f.write(data)
                temp_path = f.name
                
            try:
                result = subprocess.run(
                    [binary_path, temp_path],
                    timeout=timeout,
                    capture_output=True
                )
                # Check for crash indicators
                return result.returncode in [-11, -6, -4, 139, 134]  # SIGSEGV, SIGABRT, SIGILL
            except subprocess.TimeoutExpired:
                return False
            finally:
                os.unlink(temp_path)
                
        return self.fuzz_loop(template, iterations, test_func)


def main():
    parser = argparse.ArgumentParser(
        description='GLITCH - Reality Corruption Engine',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Glitch a single file
  glitch.py file input.png -n 5 -o output.png
  
  # Fuzz a binary
  glitch.py fuzz ./target template.bin -i 1000
  
  # Generate test cases
  glitch.py generate template.bin -c 100 -o testcases/
  
Strategies:
  • bitflip        - Flip random bits
  • byteoverwrite  - Replace with interesting bytes
  • integerboundary - Corrupt integers with boundary values
  • formatstring   - Inject format string specifiers
  • lengthcorruption - Corrupt length fields
  • truncation     - Truncate data
  • duplication    - Duplicate sections
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # File command
    file_parser = subparsers.add_parser('file', help='Glitch a single file')
    file_parser.add_argument('input', help='Input file')
    file_parser.add_argument('-n', '--mutations', type=int, default=1, help='Number of mutations')
    file_parser.add_argument('-o', '--output', help='Output file')
    file_parser.add_argument('-s', '--strategies', nargs='+', help='Strategies to use')
    file_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Generate command
    gen_parser = subparsers.add_parser('generate', help='Generate multiple test cases')
    gen_parser.add_argument('template', help='Template file')
    gen_parser.add_argument('-c', '--count', type=int, default=10, help='Number of cases')
    gen_parser.add_argument('-n', '--mutations', type=int, default=3, help='Mutations per case')
    gen_parser.add_argument('-o', '--output-dir', default='glitch_cases', help='Output directory')
    gen_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Fuzz command
    fuzz_parser = subparsers.add_parser('fuzz', help='Fuzz a binary')
    fuzz_parser.add_argument('binary', help='Binary to fuzz')
    fuzz_parser.add_argument('template', help='Template file')
    fuzz_parser.add_argument('-i', '--iterations', type=int, default=100, help='Fuzzing iterations')
    fuzz_parser.add_argument('-t', '--timeout', type=int, default=2, help='Execution timeout')
    fuzz_parser.add_argument('-c', '--crash-dir', default='crashes', help='Directory for crash cases')
    fuzz_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze glitched file differences')
    analyze_parser.add_argument('original', help='Original file')
    analyze_parser.add_argument('glitched', help='Glitched file')
    
    args = parser.parse_args()
    
    if not args.command:
        print(BANNER)
        parser.print_help()
        return
        
    print(BANNER)
    engine = GlitchEngine(verbose=getattr(args, 'verbose', False))
    
    if args.command == 'file':
        print(f"\n{Colors.CYAN}[*] Glitching {args.input}...{Colors.END}")
        
        result = engine.glitch_file(
            args.input,
            args.output,
            args.mutations,
            args.strategies
        )
        
        print(f"\n{Colors.GREEN}✓ Glitch complete{Colors.END}")
        print(f"  Input hash:  {result.input_hash}")
        print(f"  Output hash: {result.output_hash}")
        print(f"  Mutations:   {len(result.mutations)}")
        
        for m in result.mutations:
            print(f"    • {m.strategy}: {m.description}")
            
        print(f"\n{Colors.MAGENTA}\"The only revolution is the corruption of the real.\"{Colors.END}\n")
        
    elif args.command == 'generate':
        print(f"\n{Colors.CYAN}[*] Generating {args.count} test cases...{Colors.END}")
        
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
        
        with open(args.template, 'rb') as f:
            template = f.read()
            
        for i in range(args.count):
            glitched, result = engine.glitch(template, args.mutations)
            
            output_path = Path(args.output_dir) / f"case_{i:04d}_{result.output_hash}.bin"
            with open(output_path, 'wb') as f:
                f.write(glitched)
                
            if args.verbose:
                print(f"  Generated: {output_path}")
                
        print(f"\n{Colors.GREEN}✓ Generated {args.count} test cases in {args.output_dir}{Colors.END}")
        
    elif args.command == 'fuzz':
        print(f"\n{Colors.CYAN}[*] Fuzzing {args.binary} with {args.iterations} iterations...{Colors.END}")
        
        with open(args.template, 'rb') as f:
            template = f.read()
            
        interesting = engine.test_binary(
            args.binary,
            template,
            args.iterations,
            args.timeout
        )
        
        print(f"\n\n{Colors.BOLD}═══ FUZZING COMPLETE ═══{Colors.END}")
        print(f"Iterations: {args.iterations}")
        print(f"Interesting cases: {len(interesting)}")
        
        if interesting:
            print(f"\n{Colors.RED}▲ Crashes found:{Colors.END}")
            for result in interesting[:10]:
                print(f"  • {result.output_hash}: {len(result.mutations)} mutations")
                if result.crash_info:
                    print(f"    Info: {result.crash_info}")
                    
        print(f"\nCrash cases saved to: {args.crash_dir}")
        
    elif args.command == 'analyze':
        with open(args.original, 'rb') as f:
            original = f.read()
        with open(args.glitched, 'rb') as f:
            glitched = f.read()
            
        print(f"\n{Colors.BOLD}═══ GLITCH ANALYSIS ═══{Colors.END}")
        print(f"Original size:  {len(original)} bytes")
        print(f"Glitched size:  {len(glitched)} bytes")
        print(f"Size delta:     {len(glitched) - len(original):+d} bytes")
        
        # Find differences
        diffs = []
        min_len = min(len(original), len(glitched))
        
        for i in range(min_len):
            if original[i] != glitched[i]:
                diffs.append((i, original[i], glitched[i]))
                
        print(f"\nByte differences: {len(diffs)}")
        
        if diffs:
            print(f"\n{Colors.YELLOW}First 10 differences:{Colors.END}")
            for offset, orig, glitch in diffs[:10]:
                print(f"  0x{offset:08x}: 0x{orig:02x} -> 0x{glitch:02x}")


if __name__ == '__main__':
    main()
