# FlexiToolkit | Disk Forensics Module

This module helps forensic analysts create bit-for-bit disk image copies and generate a **SHA256 hash** to ensure forensic integrity.

---

## ✅ Features

- Read-only disk image creation using `shutil.copy2()`
- SHA256 hash generation for verifying integrity
- Lightweight and suitable for field use
- Ensures evidence remains unmodified (for court admissibility)

---

## 🧪 How to Use

1. Place the file or disk image to be copied in an accessible location.
2. Run the script:

```bash
python disk_tool.py
```

3. You’ll be prompted for:
- The **source file path** (e.g., `C:/Users/sonam/Desktop/source.txt`)
- The **destination disk image path** (e.g., `C:/Users/sonam/Desktop/image.dd`)

---

## 💻 Example Run

```
[*] Creating disk image...
[✔] Disk image created successfully!
[*] Calculating SHA256 hash of image...
[✔] SHA256: 6f3e9ba6f7354d7d41ab34c93e0d943e26e2dbeec5b35d3e3827c6d1b7af0629
```

---

## 📝 Sample Code Snippet (inside `disk_tool.py`)

```python
def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()
```

---

## 📌 Notes

- Use for forensic imaging of files or logical drives.
- Always verify hashes to maintain **chain of custody**.
- Works best on small to medium-size files for quick field use.

---

## 👤 Author

Sonam Choeki  
BIT302 Capstone Project – FlexiToolkit  
Box Hill Institute  
