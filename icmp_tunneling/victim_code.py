from scapy.all import sniff, IP, ICMP

def extract_data(packet):
    # Check if the packet has an ICMP layer and is an echo request
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # Echo request
        payload = bytes(packet[ICMP].payload).decode(errors="ignore")  # Extract payload
        print(f"Received covert message: {payload}")

# Sniff for incoming ICMP packets and process them with extract_data function
sniff(filter="icmp", prn=extract_data, store=0)
