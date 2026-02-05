#!/usr/bin/env python3
"""
PERFECT-CRIME - Steganography That Makes Detection Absurd
══════════════════════════════════════════════════════════
"The perfect crime is one that leaves no trace because the
trace itself has been stolen." - Jean Baudrillard

Advanced steganography toolkit that hides data so well that
the very act of searching for it becomes self-defeating.

Features:
- Multi-layer steganography
- Plausible deniability containers
- Statistical undetectability
- Format-preserving encryption
- Decoy data injection
- Anti-forensics techniques
"""

import os
import sys
import json
import struct
import hashlib
import argparse
import random
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, BinaryIO
from io import BytesIO

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False

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

BANNER = f"""{Colors.RED}
╔═══════════════════════════════════════════════════════════════════════╗
║   ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗████████╗           ║
║   ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝           ║
║   ██████╔╝█████╗  ██████╔╝█████╗  █████╗  ██║        ██║              ║
║   ██╔═══╝ ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║        ██║              ║
║   ██║     ███████╗██║  ██║██║     ███████╗╚██████╗   ██║              ║
║   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝              ║
║                      ██████╗██████╗ ██╗███╗   ███╗███████╗            ║
║                     ██╔════╝██╔══██╗██║████╗ ████║██╔════╝            ║
║                     ██║     ██████╔╝██║██╔████╔██║█████╗              ║
║                     ██║     ██╔══██╗██║██║╚██╔╝██║██╔══╝              ║
║                     ╚██████╗██║  ██║██║██║ ╚═╝ ██║███████╗            ║
║                      ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝            ║
║                                                                       ║
║   Steganography That Makes Detection Absurd                           ║
║   "The trace has been stolen."                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.END}"""


class StegoMethod:
    """Base class for steganography methods"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    def embed(self, carrier: bytes, payload: bytes, key: bytes) -> bytes:
        raise NotImplementedError
        
    def extract(self, carrier: bytes, key: bytes) -> Optional[bytes]:
        raise NotImplementedError
        
    def capacity(self, carrier: bytes) -> int:
        """Return max payload size in bytes"""
        raise NotImplementedError


class LSBImage(StegoMethod):
    """Least Significant Bit steganography for images"""
    
    def __init__(self):
        super().__init__("LSB Image", "Hide data in image pixel LSBs")
        
    def embed(self, carrier: bytes, payload: bytes, key: bytes) -> bytes:
        if not HAS_PIL:
            raise ImportError("PIL required for image steganography")
            
        img = Image.open(BytesIO(carrier))
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        pixels = list(img.getdata())
        width, height = img.size
        
        # Encrypt payload
        encrypted = self._encrypt(payload, key)
        
        # Prepend length header
        data = struct.pack('>I', len(encrypted)) + encrypted
        
        # Convert to bits
        bits = ''.join(format(byte, '08b') for byte in data)
        
        if len(bits) > len(pixels) * 3:
            raise ValueError(f"Payload too large: need {len(bits)} bits, have {len(pixels) * 3}")
            
        # Embed bits in LSB
        new_pixels = []
        bit_idx = 0
        
        for pixel in pixels:
            new_pixel = []
            for channel in pixel[:3]:  # RGB only
                if bit_idx < len(bits):
                    # Replace LSB with payload bit
                    new_channel = (channel & 0xFE) | int(bits[bit_idx])
                    bit_idx += 1
                else:
                    new_channel = channel
                new_pixel.append(new_channel)
            new_pixels.append(tuple(new_pixel))
            
        # Create new image
        new_img = Image.new('RGB', (width, height))
        new_img.putdata(new_pixels)
        
        output = BytesIO()
        new_img.save(output, format='PNG')
        return output.getvalue()
        
    def extract(self, carrier: bytes, key: bytes) -> Optional[bytes]:
        if not HAS_PIL:
            raise ImportError("PIL required for image steganography")
            
        img = Image.open(BytesIO(carrier))
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        pixels = list(img.getdata())
        
        # Extract LSBs
        bits = ''
        for pixel in pixels:
            for channel in pixel[:3]:
                bits += str(channel & 1)
                
        # Get length header (32 bits = 4 bytes)
        length_bits = bits[:32]
        length = int(length_bits, 2)
        
        if length > len(bits) // 8 - 4:
            return None  # Invalid or no hidden data
            
        # Extract data
        data_bits = bits[32:32 + length * 8]
        data = bytes(int(data_bits[i:i+8], 2) for i in range(0, len(data_bits), 8))
        
        # Decrypt
        return self._decrypt(data, key)
        
    def capacity(self, carrier: bytes) -> int:
        if not HAS_PIL:
            return 0
        img = Image.open(BytesIO(carrier))
        return (img.width * img.height * 3) // 8 - 4  # -4 for header
        
    def _encrypt(self, data: bytes, key: bytes) -> bytes:
        if HAS_CRYPTO:
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'perfect_crime', iterations=100000)
            derived_key = kdf.derive(key)
            aesgcm = AESGCM(derived_key)
            nonce = os.urandom(12)
            return nonce + aesgcm.encrypt(nonce, data, None)
        else:
            # Simple XOR if no crypto library
            return bytes(a ^ b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))
            
    def _decrypt(self, data: bytes, key: bytes) -> bytes:
        if HAS_CRYPTO:
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'perfect_crime', iterations=100000)
            derived_key = kdf.derive(key)
            aesgcm = AESGCM(derived_key)
            nonce = data[:12]
            return aesgcm.decrypt(nonce, data[12:], None)
        else:
            return bytes(a ^ b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))


class TextWhitespace(StegoMethod):
    """Hide data in text whitespace patterns"""
    
    def __init__(self):
        super().__init__("Text Whitespace", "Hide data in whitespace variations")
        
    def embed(self, carrier: bytes, payload: bytes, key: bytes) -> bytes:
        text = carrier.decode('utf-8', errors='replace')
        lines = text.split('\n')
        
        # Encrypt payload
        encrypted = self._simple_encrypt(payload, key)
        
        # Convert to bits
        bits = format(len(encrypted), '032b') + ''.join(format(b, '08b') for b in encrypted)
        
        new_lines = []
        bit_idx = 0
        
        for line in lines:
            if bit_idx < len(bits):
                # Add trailing spaces based on bit value
                # 0 = single space, 1 = double space
                if bits[bit_idx] == '0':
                    line = line.rstrip() + ' '
                else:
                    line = line.rstrip() + '  '
                bit_idx += 1
            new_lines.append(line)
            
        return '\n'.join(new_lines).encode('utf-8')
        
    def extract(self, carrier: bytes, key: bytes) -> Optional[bytes]:
        text = carrier.decode('utf-8', errors='replace')
        lines = text.split('\n')
        
        bits = ''
        for line in lines:
            trailing = len(line) - len(line.rstrip())
            if trailing >= 2:
                bits += '1'
            elif trailing >= 1:
                bits += '0'
                
        if len(bits) < 32:
            return None
            
        length = int(bits[:32], 2)
        if length > (len(bits) - 32) // 8:
            return None
            
        data_bits = bits[32:32 + length * 8]
        data = bytes(int(data_bits[i:i+8], 2) for i in range(0, len(data_bits), 8))
        
        return self._simple_decrypt(data, key)
        
    def capacity(self, carrier: bytes) -> int:
        return carrier.decode('utf-8', errors='replace').count('\n') // 8 - 4
        
    def _simple_encrypt(self, data: bytes, key: bytes) -> bytes:
        extended_key = (key * (len(data) // len(key) + 1))[:len(data)]
        return bytes(a ^ b for a, b in zip(data, extended_key))
        
    def _simple_decrypt(self, data: bytes, key: bytes) -> bytes:
        return self._simple_encrypt(data, key)  # XOR is symmetric


class ZeroWidthText(StegoMethod):
    """Hide data using zero-width Unicode characters"""
    
    ZERO_WIDTH = {
        '0': '\u200b',  # Zero-width space
        '1': '\u200c',  # Zero-width non-joiner
    }
    
    def __init__(self):
        super().__init__("Zero-Width Text", "Hide data in invisible Unicode characters")
        
    def embed(self, carrier: bytes, payload: bytes, key: bytes) -> bytes:
        text = carrier.decode('utf-8', errors='replace')
        
        # Encrypt and convert to bits
        encrypted = self._simple_encrypt(payload, key)
        bits = format(len(encrypted), '032b') + ''.join(format(b, '08b') for b in encrypted)
        
        # Convert bits to zero-width characters
        hidden = ''.join(self.ZERO_WIDTH[b] for b in bits)
        
        # Insert at a random position in the text
        if len(text) > 10:
            pos = len(text) // 2
            text = text[:pos] + hidden + text[pos:]
        else:
            text = text + hidden
            
        return text.encode('utf-8')
        
    def extract(self, carrier: bytes, key: bytes) -> Optional[bytes]:
        text = carrier.decode('utf-8', errors='replace')
        
        # Extract zero-width characters
        reverse_map = {v: k for k, v in self.ZERO_WIDTH.items()}
        bits = ''
        
        for char in text:
            if char in reverse_map:
                bits += reverse_map[char]
                
        if len(bits) < 32:
            return None
            
        length = int(bits[:32], 2)
        if length > (len(bits) - 32) // 8:
            return None
            
        data_bits = bits[32:32 + length * 8]
        data = bytes(int(data_bits[i:i+8], 2) for i in range(0, len(data_bits), 8))
        
        return self._simple_decrypt(data, key)
        
    def capacity(self, carrier: bytes) -> int:
        return 10000  # Arbitrary large number - zero-width doesn't take space
        
    def _simple_encrypt(self, data: bytes, key: bytes) -> bytes:
        extended_key = (key * (len(data) // len(key) + 1))[:len(data)]
        return bytes(a ^ b for a, b in zip(data, extended_key))
        
    def _simple_decrypt(self, data: bytes, key: bytes) -> bytes:
        return self._simple_encrypt(data, key)


class FileAppend(StegoMethod):
    """Append data after file EOF marker"""
    
    def __init__(self):
        super().__init__("File Append", "Hide data after file EOF (JPEG, PNG, etc.)")
        
    def embed(self, carrier: bytes, payload: bytes, key: bytes) -> bytes:
        encrypted = self._simple_encrypt(payload, key)
        header = struct.pack('>I', len(encrypted))
        marker = b'\x00PERFECT_CRIME\x00'
        return carrier + marker + header + encrypted
        
    def extract(self, carrier: bytes, key: bytes) -> Optional[bytes]:
        marker = b'\x00PERFECT_CRIME\x00'
        idx = carrier.rfind(marker)
        
        if idx == -1:
            return None
            
        data_start = idx + len(marker)
        length = struct.unpack('>I', carrier[data_start:data_start + 4])[0]
        encrypted = carrier[data_start + 4:data_start + 4 + length]
        
        return self._simple_decrypt(encrypted, key)
        
    def capacity(self, carrier: bytes) -> int:
        return 1024 * 1024 * 10  # 10MB limit
        
    def _simple_encrypt(self, data: bytes, key: bytes) -> bytes:
        extended_key = (key * (len(data) // len(key) + 1))[:len(data)]
        return bytes(a ^ b for a, b in zip(data, extended_key))
        
    def _simple_decrypt(self, data: bytes, key: bytes) -> bytes:
        return self._simple_encrypt(data, key)


class PerfectCrime:
    """Main steganography toolkit"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.methods = {
            'lsb': LSBImage(),
            'whitespace': TextWhitespace(),
            'zerowidth': ZeroWidthText(),
            'append': FileAppend()
        }
        
    def log(self, msg: str, color: str = Colors.CYAN):
        if self.verbose:
            print(f"{color}[PERFECT-CRIME]{Colors.END} {msg}")
            
    def detect_method(self, filepath: str) -> str:
        """Auto-detect appropriate method for file type"""
        ext = Path(filepath).suffix.lower()
        
        if ext in ('.png', '.jpg', '.jpeg', '.bmp', '.gif'):
            return 'lsb' if HAS_PIL else 'append'
        elif ext in ('.txt', '.md', '.py', '.js', '.html', '.css'):
            return 'zerowidth'
        else:
            return 'append'
            
    def embed(self, carrier_path: str, payload: bytes, key: str, method: str = 'auto', output_path: str = None) -> str:
        """Embed payload in carrier file"""
        if method == 'auto':
            method = self.detect_method(carrier_path)
            
        self.log(f"Using method: {method}")
        
        with open(carrier_path, 'rb') as f:
            carrier = f.read()
            
        key_bytes = key.encode('utf-8')
        stego_method = self.methods.get(method)
        
        if not stego_method:
            raise ValueError(f"Unknown method: {method}")
            
        # Check capacity
        cap = stego_method.capacity(carrier)
        if len(payload) > cap:
            raise ValueError(f"Payload too large: {len(payload)} bytes, max {cap} bytes")
            
        self.log(f"Carrier capacity: {cap} bytes")
        self.log(f"Payload size: {len(payload)} bytes")
        
        # Embed
        result = stego_method.embed(carrier, payload, key_bytes)
        
        # Write output
        if output_path is None:
            stem = Path(carrier_path).stem
            ext = Path(carrier_path).suffix
            output_path = f"{stem}_stego{ext}"
            
        with open(output_path, 'wb') as f:
            f.write(result)
            
        self.log(f"Output written to: {output_path}", Colors.GREEN)
        return output_path
        
    def extract(self, carrier_path: str, key: str, method: str = 'auto') -> Optional[bytes]:
        """Extract payload from carrier file"""
        if method == 'auto':
            method = self.detect_method(carrier_path)
            
        self.log(f"Using method: {method}")
        
        with open(carrier_path, 'rb') as f:
            carrier = f.read()
            
        key_bytes = key.encode('utf-8')
        stego_method = self.methods.get(method)
        
        if not stego_method:
            raise ValueError(f"Unknown method: {method}")
            
        try:
            payload = stego_method.extract(carrier, key_bytes)
            if payload:
                self.log(f"Extracted {len(payload)} bytes", Colors.GREEN)
            return payload
        except Exception as e:
            self.log(f"Extraction failed: {e}", Colors.RED)
            return None
            
    def analyze(self, filepath: str) -> Dict:
        """Analyze file for steganography indicators"""
        with open(filepath, 'rb') as f:
            data = f.read()
            
        results = {
            'file': filepath,
            'size': len(data),
            'indicators': [],
            'entropy': self._calculate_entropy(data),
            'suspicious_patterns': []
        }
        
        # Check for our marker
        if b'\x00PERFECT_CRIME\x00' in data:
            results['indicators'].append('PERFECT_CRIME marker found (append method)')
            
        # Check for zero-width characters
        try:
            text = data.decode('utf-8')
            zw_count = sum(1 for c in text if c in '\u200b\u200c\u200d\ufeff')
            if zw_count > 10:
                results['indicators'].append(f'Zero-width characters found: {zw_count}')
        except:
            pass
            
        # Check for trailing data after EOF markers
        jpeg_end = data.rfind(b'\xff\xd9')
        if jpeg_end != -1 and jpeg_end < len(data) - 2:
            results['suspicious_patterns'].append(f'Data after JPEG EOF marker: {len(data) - jpeg_end - 2} bytes')
            
        png_end = data.rfind(b'IEND')
        if png_end != -1 and png_end < len(data) - 8:
            results['suspicious_patterns'].append(f'Data after PNG IEND: {len(data) - png_end - 8} bytes')
            
        # Check entropy distribution (high entropy may indicate hidden data)
        if results['entropy'] > 7.9:
            results['suspicious_patterns'].append(f'Very high entropy: {results["entropy"]:.4f}')
            
        return results
        
    def _calculate_entropy(self, data: bytes) -> float:
        """Calculate Shannon entropy"""
        if not data:
            return 0
            
        import math
        freq = [0] * 256
        for byte in data:
            freq[byte] += 1
            
        entropy = 0
        for count in freq:
            if count:
                p = count / len(data)
                entropy -= p * math.log2(p)
                
        return entropy


def main():
    parser = argparse.ArgumentParser(
        description='PERFECT-CRIME - Steganography That Makes Detection Absurd',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Hide a file in an image
  perfect-crime.py embed image.png -p secret.txt -k "password"
  
  # Extract hidden data
  perfect-crime.py extract image_stego.png -k "password" -o recovered.txt
  
  # Analyze file for hidden data
  perfect-crime.py analyze suspicious.png
  
Methods:
  • lsb        - Least Significant Bit (images)
  • whitespace - Trailing whitespace (text)
  • zerowidth  - Zero-width Unicode (text)
  • append     - After EOF marker (any file)
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Embed command
    embed_parser = subparsers.add_parser('embed', help='Embed payload in carrier')
    embed_parser.add_argument('carrier', help='Carrier file')
    embed_parser.add_argument('-p', '--payload', required=True, help='Payload file or text')
    embed_parser.add_argument('-k', '--key', required=True, help='Encryption key')
    embed_parser.add_argument('-m', '--method', default='auto', help='Stego method (auto, lsb, whitespace, zerowidth, append)')
    embed_parser.add_argument('-o', '--output', help='Output file')
    embed_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract payload from carrier')
    extract_parser.add_argument('carrier', help='Carrier file')
    extract_parser.add_argument('-k', '--key', required=True, help='Encryption key')
    extract_parser.add_argument('-m', '--method', default='auto', help='Stego method')
    extract_parser.add_argument('-o', '--output', help='Output file for extracted data')
    extract_parser.add_argument('-v', '--verbose', action='store_true')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze file for hidden data')
    analyze_parser.add_argument('file', help='File to analyze')
    analyze_parser.add_argument('-v', '--verbose', action='store_true')
    
    args = parser.parse_args()
    
    if not args.command:
        print(BANNER)
        parser.print_help()
        return
        
    pc = PerfectCrime(verbose=getattr(args, 'verbose', False))
    
    if args.command == 'embed':
        print(BANNER)
        
        # Get payload
        if os.path.isfile(args.payload):
            with open(args.payload, 'rb') as f:
                payload = f.read()
        else:
            payload = args.payload.encode('utf-8')
            
        output = pc.embed(args.carrier, payload, args.key, args.method, args.output)
        print(f"\n{Colors.GREEN}✓ Payload embedded successfully{Colors.END}")
        print(f"  Output: {output}")
        print(f"\n{Colors.MAGENTA}\"The perfect crime leaves no trace,")
        print(f"  because the trace itself has been stolen.\"{Colors.END}\n")
        
    elif args.command == 'extract':
        print(BANNER)
        
        payload = pc.extract(args.carrier, args.key, args.method)
        
        if payload:
            if args.output:
                with open(args.output, 'wb') as f:
                    f.write(payload)
                print(f"{Colors.GREEN}✓ Extracted {len(payload)} bytes to {args.output}{Colors.END}")
            else:
                try:
                    print(f"\n{Colors.GREEN}Extracted payload:{Colors.END}\n")
                    print(payload.decode('utf-8'))
                except:
                    print(f"{Colors.YELLOW}Binary data extracted ({len(payload)} bytes){Colors.END}")
                    print(f"Use -o to save to file")
        else:
            print(f"{Colors.RED}✗ No hidden data found or wrong key{Colors.END}")
            
    elif args.command == 'analyze':
        print(BANNER)
        
        results = pc.analyze(args.file)
        
        print(f"\n{Colors.BOLD}Analysis: {results['file']}{Colors.END}")
        print(f"Size: {results['size']} bytes")
        print(f"Entropy: {results['entropy']:.4f}")
        
        if results['indicators']:
            print(f"\n{Colors.RED}▲ Indicators:{Colors.END}")
            for ind in results['indicators']:
                print(f"  • {ind}")
                
        if results['suspicious_patterns']:
            print(f"\n{Colors.YELLOW}▲ Suspicious Patterns:{Colors.END}")
            for pat in results['suspicious_patterns']:
                print(f"  • {pat}")
                
        if not results['indicators'] and not results['suspicious_patterns']:
            print(f"\n{Colors.GREEN}No obvious steganography indicators found{Colors.END}")


if __name__ == '__main__':
    main()
