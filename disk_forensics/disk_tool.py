import shutil
import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def create_disk_image(source_path, dest_path):
    try:
        print("[*] Creating disk image...")
        shutil.copy2(source_path, dest_path)
        print("[✔] Disk image created successfully!")

        print("[*] Calculating SHA256 hash of image...")
        hash_value = calculate_sha256(dest_path)
        print(f"[✔] SHA256: {hash_value}")

    except FileNotFoundError:
        print("[-] Source file not found.")
