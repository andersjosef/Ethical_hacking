from scapy.all import TCP, IP, sr1
import time
import random

target_ip = "192.168.64.11"
target_port_range = [port for port in range(1, 1023+1)] # Check all known ports for simplicity and main importance

def check_port(target_port):

    # Create segment
    segment = IP(dst=target_ip) / TCP(sport=8080, dport=target_port, flags="S") #S for SYN

    # Send packet and wait for a response
    response = sr1(segment, timeout=1, verbose=0)

    # Analyze the response
    if response:
        if response.haslayer(TCP):
            tcp_layer = response.getlayer(TCP)
            if tcp_layer.flags == 0x12:  # SYN-ACK response
                print(f"Port {target_port} is open.")
    else:
        print(f"Port {target_port} no response.")
    

for port in target_port_range:
    time.sleep(0.001 + random.random() / 2) # Will sleep for a random up to a certain max
    check_port(port)
