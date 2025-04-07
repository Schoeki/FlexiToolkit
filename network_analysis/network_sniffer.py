import pyshark

def analyze_pcap(file_path):
    print(f"\n📂 Analyzing PCAP file: {file_path}")
    try:
        capture = pyshark.FileCapture(file_path, display_filter="ip")
        for packet in capture.sniff_continuously(packet_count=10):
            print(f"[+] {packet.highest_layer} | {packet.ip.src} -> {packet.ip.dst}")
        capture.close()
    except Exception as e:
        print(f"[!] Error: {e}")

def live_capture(interface):
    print(f"\n🛜 Starting live capture on: {interface}")
    try:
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=10):
            print(f"[+] {packet.highest_layer} | {packet.ip.src} -> {packet.ip.dst}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    print("=== FlexiToolkit | Network Packet Sniffer ===")
    mode = input("Choose mode - (1) Live Capture, (2) Analyze PCAP file: ").strip()
    
    if mode == "1":
        interface = input("Enter network interface (default: Wi-Fi): ").strip() or "Wi-Fi"
        live_capture(interface)
    elif mode == "2":
        file_path = input("Enter path to .pcap file: ").strip()
        analyze_pcap(file_path)
    else:
        print("[!] Invalid selection.")
