import hashlib 
import shutil

# Function to calculate SHA256 hash
def calculate_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Function to create a disk image
def create_disk_image(source_path, dest_path):
    try:
        print("[*] Creating disk image...")
        shutil.copy2(source_path, dest_path)  # Copies the file to the new location
        print("[✓] Disk image created successfully!")

        print("[*] Calculating SHA256 hash of image...")
        image_hash = calculate_sha256(dest_path)  # Calculate the SHA256 hash
        print(f"[✓] SHA256 Hash: {image_hash}")

    except FileNotFoundError:
        print("[-] Source file not found.")
    except PermissionError:
        print("[-] Permission denied. Try running as admin.")
    except Exception as e:
        print(f"[-] Error: {str(e)}")

# Main function to prompt user for file paths
def run():
    src = input("Enter the source file path: ")  # Source file path
    dest = input("Enter the destination image path (e.g., image.dd): ")  # Destination path for image
    create_disk_image(src, dest)  # Create the disk image and calculate the hash

if __name__ == "__main__":
    run()  # Run the function when this file is executed directly
