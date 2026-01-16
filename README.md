# 🧠 Basic Buffer Overflow PoC

Basic Buffer Overflow PoC is a small Python script that demonstrates
how sending an oversized input to a network service can trigger
buffer overflow conditions.

It is intended strictly for learning and controlled testing.

---

## Overview

Buffer overflows occur when a program receives more data than it can safely handle.
In network services, this often happens when input validation is missing
or buffer boundaries are not enforced.

This script:
- Connects to a TCP service
- Sends an intentionally oversized payload
- Closes the connection immediately

The goal is to observe how the target service reacts.

---

## What This PoC Demonstrates

- How socket-based services receive external input
- How oversized payloads are sent over TCP
- Why input size validation is critical
- The first step in understanding memory corruption vulnerabilities

This is a **conceptual demonstration**, not a full exploit.

---

## How It Works

The script:
- Defines a target IP and port
- Creates a payload larger than typical input buffers
- Establishes a TCP connection
- Sends the payload to the service
- Closes the socket

Any crash or unexpected behavior must be observed on the target side.

---

## Usage

Run the script in a controlled environment  
python buffer_overflow_poc.py

Make sure the target service is:
- Running locally or in a lab
- Built intentionally for testing
- Monitored for crashes or exceptions

---

## Requirements

- Python 3.x
- A test TCP service listening on the target port
- A controlled lab environment

---

## Important Notes

- This script does not bypass protections
- It does not perform exploitation
- No shellcode, offsets, or return address manipulation is included
- Modern systems with protections may not crash at all

This PoC is about **understanding behavior**, not exploitation.

---

## Ethical Warning

Run this code only against:
- Your own services
- Intentionally vulnerable lab programs
- Educational environments

Never send oversized payloads to systems you do not own or control.

---

## Final Thoughts

Understanding buffer overflows starts with understanding input size.
This PoC helps visualize that first step in a safe, minimal way.
