# FlexiToolkit | Network Analysis Module

This module allows forensic analysts to capture live network traffic or analyze previously recorded `.pcap` files using PyShark.

---

## 🔍 Features

✅ Live network packet capture using a selected network interface  
✅ Offline `.pcap` file analysis with summary of protocol and IP traffic  
✅ Simple and interactive command-line interface  
✅ Automatically limits to top 10 packets for performance and preview

---

## 🧰 How It Works

The script uses PyShark (Python wrapper for TShark/Wireshark) to:
- Capture packets from an active network interface
- Analyze `.pcap` files for key protocol and IP metadata

---

## 🧪 How to Use

```bash
python network_sniffer.py
```

You will be prompted to choose:

- (1) Live Capture – enter your interface (e.g., `Wi-Fi`, `Ethernet`, or `\Device\NPF_Loopback`)  
- (2) Analyze PCAP – enter full path to a `.pcap` file

---

## 💡 Example Output

```
=== FlexiToolkit | Network Packet Sniffer ===
Choose mode - (1) Live Capture, (2) Analyze PCAP file: 2
Enter path to .pcap file: sample.pcap
[+] DNS | 192.168.1.10 -> 8.8.8.8
[+] TCP  | 10.0.0.5 -> 192.168.1.101
...
```

---

## 📦 Requirements

- Python 3.8+
- [PyShark](https://github.com/KimiNewt/pyshark)
- [Npcap](https://npcap.com/) for live capture (Windows only)

Install dependencies:
```bash
pip install pyshark
```

---

## 📁 Files

- `network_sniffer.py` – main script for capture and analysis  
- `README.md` – module documentation

---

## 👤 Author

Sonam Choeki  
BIT302 Capstone Project – FlexiToolkit

