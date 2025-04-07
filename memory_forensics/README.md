# 🧠 FlexiToolkit | Memory Forensics Module

This module provides tools for analyzing volatile memory (RAM) from compromised systems using the **Volatility 3** framework. It helps investigators extract valuable forensic artifacts such as processes, drivers, open sockets, and encryption keys from memory dumps.

📂 Script: `memory_forensics/volatility_runner.py`

---

## 🧰 Features

- ✅ Compatible with **Volatility 3**
- ✅ Supports `.vmem`, `.raw`, and `.bin` memory dumps
- ✅ Helps extract:
  - Active processes
  - Registry keys
  - Network connections
  - Malware traces

---

## 📦 Requirements

- Python 3.8+
- Volatility 3 (installed locally or in virtual environment)

Install Volatility 3:
```bash
pip install volatility3
```

Or clone from GitHub for development:
```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip install -e .
```

---

## 🚀 How to Use

```bash
python volatility_runner.py
```

You will be prompted for:
- Memory dump file path
- Plugin to run (e.g., `windows.pslist`, `windows.netscan`, `windows.registry.hivelist`)

---

## 💡 Example Output

```
Enter path to memory image: C:\dumps\memdump.raw
Enter plugin name (e.g., windows.pslist): windows.pslist

[+] Running plugin windows.pslist...
Offset(V)  Name             PID   PPID ...
0x123456   explorer.exe     1234  567
0x789abc   cmd.exe          4321  1234
```

---

## 📁 Files

- `volatility_runner.py` – script wrapper for running Volatility 3 commands
- `README.md` – this documentation

---

## 🔒 Notes

- Ensure symbol files are available for the OS you're analyzing
- For best results, use clean memory images and verified plugins

---

## 👤 Author

Sonam Choeki  
BIT302 Capstone Project – FlexiToolkit
