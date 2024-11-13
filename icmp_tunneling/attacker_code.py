from scapy.all import IP, ICMP, send

# Target IP
target_ip = "192.168.64.11" 

# Message to send through the ICMP payload
message = "Covert Channel Using ICMP"

# Craft and send ICMP packet with the message in the payload
packet = IP(dst=target_ip) / ICMP(type="echo-request") / message
send(packet)
print(f"Sent ICMP packet with message: {message}")
