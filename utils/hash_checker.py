import hashlib

# Function to calculate SHA256 hash
def calculate_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Run function to check hash of a file
def run():
    print("[*] Running Hash Checker Tool...")
    
    # Ask for the file path to check
    file_path = input("Enter the file path to check hash: ")
    
    try:
        # Calculate the hash for the provided file
        file_hash = calculate_sha256(file_path)
        print(f"[✓] SHA256 Hash of the file: {file_hash}")
    
    except FileNotFoundError:
        print("[-] The specified file was not found.")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
