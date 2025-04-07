
# 🧰 FlexiToolkit: Lightweight Digital Forensics Toolkit for Cybercrime Investigation

FlexiToolkit is a modular Python-based digital forensics suite designed for students, educators, and professionals to perform lightweight cybercrime investigations. This toolkit supports multiple forensic areas such as memory analysis, disk imaging, log inspection, network packet capture, and hash validation.

---

## 📦 Modules Overview

### 🔹 Disk Forensics
- Create forensic disk images using `shutil.copy2`
- Generate SHA256 hashes to verify integrity
- Script: `disk_imager.py`

### 🔹 Memory Forensics
- Analyze memory dumps using **Volatility 3**
- Run plugins such as `windows.info`, `pslist`, etc.
- Script: `vol_tool.py`
- Requires: `volatility3` cloned and installed

### 🔹 Log Analysis
- Detect failed login attempts
- Extract attacker IPs from log files
- Script: `log_tool.py`

### 🔹 Network Analysis
- Live packet sniffing (top 10 packets)
- Offline `.pcap` file analysis using **PyShark**
- Script: `network_sniffer.py`
- Requires: `TShark` (via Wireshark) and `Npcap` (Windows)

### 🔹 Utility Tools
- Check file hashes (MD5 or SHA256)
- Script: `hash_checker.py`

---

## 📁 Folder Structure

FlexiToolkit/
│
├── disk_forensics/
│   └── disk_imager.py
│
├── log_analysis/
│   └── log_tool.py
│
├── memory_forensics/
│   └── vol_tool.py
│
├── network_analysis/
│   └── network_sniffer.py
│
├── utils/
│   └── hash_checker.py
│
├── main.py
├── LICENSE
└── README.md


---

## 🛠 Requirements

- Python 3.8+
- Volatility 3
- TShark (via Wireshark)
- Npcap (for packet sniffing on Windows)
- PyShark

Install dependencies:
pip install pyshark

Set up Volatility 3:
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python -m venv venv
source venv/Scripts/activate  # or venv/bin/activate on Linux/Mac
pip install -e .

---

## 🚀 How to Use

Each module runs independently. Example usage:

cd log_analysis
python log_tool.py

cd memory_forensics
python vol_tool.py

cd disk_forensics
python disk_imager.py

cd utils
python hash_checker.py

cd network_analysis
python network_sniffer.py

---

## 👩‍💻 Author

Sonam Choeki  
Capstone Project | Box Hill Institute  
GitHub: https://github.com/Schoeki

---

## 📜 License

This project is licensed under the MIT License – see the `LICENSE` file for details.
