"""
Not noticed by SNORT with community rules
"""

import random
from scapy.all import IP, TCP, fragment, send

target_IP = "192.168.64.11"

def send_icmp():
    # Create TCP segment with SYN flag
    # packet = IP(dst=target_IP, src=f"192.168.64.{random.randrange(1, 254)}") / TCP(dport=22, sport=8080, flags="S") # S FOR SYN
    packet = IP(dst=target_IP) / TCP(dport=22, sport=8080, flags="S") # S FOR SYN

    # Fragment the segment making 8 bytes of payload
    fragments = fragment(packet, fragsize=8)
    for frag in fragments:
        send(frag)

for _ in range(100):
    send_icmp()



