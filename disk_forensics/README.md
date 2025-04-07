  # FlexiToolkit | Disk Forensics Module

This module provides functionality to create disk image copies and verify their integrity using SHA256 hashing. It is helpful in digital forensics when making bit-by-bit copies of drives or files while preserving original evidence.

## Features

✅ Create disk image copies using `shutil.copy2`  
✅ Generate and verify SHA256 hash of disk images  
✅ Error handling for missing or protected files  
✅ User-friendly console prompts

---

## 🛠 Tool Used

**`disk_imager.py`**  
- Core script for disk image creation  
- Calculates SHA256 hash  
- Includes interactive prompts for input/output paths  

The older `disk_tool.py` has been deprecated and removed.

---

## 🔧 How to Use

1. Navigate to the `disk_forensics` directory:
```bash
cd disk_forensics
```

2. Run the tool:
```bash
python disk_imager.py
```

3. Provide:
- **Source path**: File to image (e.g., `E:\evidence.dd`)
- **Destination path**: Location to save the copy (e.g., `C:\images\copy.dd`)

---

## 🧪 Sample Output

```plaintext
[*] Creating disk image...
[✓] Disk image created successfully!
[*] Calculating SHA256 hash of image...
[✓] SHA256: 2a3f324b17ee... (hash value)
```

---

## Requirements

- Python 3.x
- No external libraries required (uses built-in `shutil` and `hashlib`)

---

## 📁 Files

- `disk_imager.py` — main tool for disk imaging  
- `README.md` — this file

