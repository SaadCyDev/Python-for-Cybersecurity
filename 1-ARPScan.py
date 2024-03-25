import sys
from scapy.all import *

if len(sys.argv) != 2:
    print("Usage: python script.py <IP address>")
    sys.exit(1)

ip_range = sys.argv[1]
print(sys.argv[0])

try:
    alive, dead = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range), timeout=2, verbose=0)
    print("Devices found:")
    print("MAC-IP")
    for packet in alive:
        mac = packet[1].hwsrc
        ip = packet[1].psrc
        print(f"{mac} -- {ip}")
except Exception as e:
    print(f"An error occurred: {e}")
