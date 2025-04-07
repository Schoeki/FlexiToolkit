import pyshark

def live_capture():
    print("=== FlexiToolkit | Network Packet Sniffer ===")
    interface = input("Enter network interface (default: Wi-Fi): ") or "Wi-Fi"
    capture = pyshark.LiveCapture(interface=interface)

    print("[*] Capturing packets... (Press Ctrl+C to stop)")
    try:
        for i, packet in enumerate(capture.sniff_continuously(packet_count=10)):
            print(f"\nPacket #{i + 1}: {packet.highest_layer}")
            if 'IP' in packet:
                print(f"From {packet.ip.src} → To {packet.ip.dst}")
    except KeyboardInterrupt:
        print("\n[✓] Capture stopped.")

def read_pcap_file():
    print("=== FlexiToolkit | PCAP File Analysis ===")
    file_path = input("Enter path to .pcap file: ")
    try:
        cap = pyshark.FileCapture(file_path)
        print("[*] Displaying top 10 packets:")
        for i, packet in enumerate(cap):
            print(f"\nPacket #{i + 1}: {packet.highest_layer}")
            if 'IP' in packet:
                print(f"From {packet.ip.src} → To {packet.ip.dst}")
            if i == 9:
                break
    except Exception as e:
        print(f"[!] Error reading file: {e}")

def main():
    print("=== FlexiToolkit | Network Analysis ===")
    print("1. Live Packet Capture")
    print("2. Analyze .pcap File")
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        live_capture()
    elif choice == "2":
        read_pcap_file()
    else:
        print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
