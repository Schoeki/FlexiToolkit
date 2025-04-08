import pyshark  # PyShark is used for packet capturing

# Function to start network capture
def run():
    print("[*] Running Network Analysis Tool...")
    
    # Ask for the network interface to capture packets (e.g., eth0, wlan0)
    interface = input("Enter the network interface to capture packets (e.g., eth0, wlan0): ")
    
    try:
        # Start capturing packets on the specified interface
        print(f"[*] Capturing packets on {interface}...")
        capture = pyshark.LiveCapture(interface=interface)
        
        # Capture and display packets in real-time
        for packet in capture.sniff_continuously(packet_count=10):  # Adjust packet count as needed
            print(f"Packet: {packet}")
        
        print("[✓] Network analysis completed!")
    
    except Exception as e:
        print(f"[-] Error during network analysis: {e}")
