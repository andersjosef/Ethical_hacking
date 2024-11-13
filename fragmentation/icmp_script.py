"""
VERY OBVIOUS FOR THE SNORT
"""

from scapy.all import IP, ICMP, fragment, send

target_IP = "192.168.64.11"

def send_icmp():
    packet = IP(dst=target_IP) / ICMP()

    fragments = fragment(packet, fragsize=1)
    for frag in fragments:
        send(frag)

for _ in range(100):
    send_icmp()



