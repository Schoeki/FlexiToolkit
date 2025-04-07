# Memory Forensics Tool (FlexiToolkit)

This module is part of the **FlexiToolkit** and provides memory forensics capabilities using the Volatility 3 framework.

## 🧠 Tool: `vol_tool.py`

A lightweight Python wrapper to run Volatility plugins for RAM analysis.

### ✅ Features:
- Simple command-line interface
- Lets you analyze memory dumps with any Volatility plugin
- Runs directly from FlexiToolkit (assumes Volatility 3 is installed)

---

## 📥 Requirements

- Python 3.8+
- Volatility 3 cloned to: `~/Desktop/volatility3`
- RAM memory image file (e.g., `.vmem`, `.raw`, `.dmp`)

---

## ⚙️ Usage

1. **Activate virtual environment** from the Volatility folder:

```bash
cd ~/Desktop/volatility3
source venv/Scripts/activate
