# 🔐 FlexiToolkit | Hash Checker Utility (MD5 & SHA256)

This utility helps forensic investigators verify the integrity of files by computing their cryptographic hash values. It supports both **MD5** and **SHA256** algorithms and is used to ensure that files have not been altered.

📂 Script: `utils/hash_checker.py`

---

## 🧰 Features

- ✅ Supports **MD5** and **SHA256**
- ✅ Verifies file integrity during forensic investigations
- ✅ Clear command-line interface for user input
- ✅ Handles common errors (file not found, invalid input)

---

## 🚀 How to Use

```bash
python hash_checker.py
```

### Example Walkthrough:

1. You will be prompted:
   - `Enter the path of the file:`
   - `Enter hash type (md5/sha256):`

2. Example Input:
   ```
   Enter the path of the file: evidence.img
   Enter hash type (md5/sha256): sha256
   ```

3. Output:
   ```
   SHA256 Hash: a5d4c8f0e32ba29d3f...
   ```

---

## ❗ Notes

- Ensure the file exists and you have read permission.
- Use lowercase for hash type (`md5` or `sha256`).
- This tool is part of the **FlexiToolkit** forensic suite under the `utils/` module.

---

## 📄 License

MIT License  
(C) 2025 FlexiToolkit Contributors
