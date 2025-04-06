import hashlib

def calculate_hash(filepath, algo="sha256"):
    try:
        if algo == "md5":
            hasher = hashlib.md5()
        elif algo == "sha256":
            hasher = hashlib.sha256()
        else:
            return "Unsupported hash type!"

        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)

        return hasher.hexdigest()
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    path = input("Enter the path of the file: ")
    hash_type = input("Enter hash type (md5/sha256): ").lower()
    result = calculate_hash(path, hash_type)
    print(f"{hash_type.upper()} Hash: {result}")
