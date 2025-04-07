import os

def run_volatility(image_path, plugin="windows.info"):
    print(f"[✓] Running Volatility plugin: {plugin}")
    os.system(f"python ../../volatility3/vol.py -f \"{image_path}\" {plugin}")

if __name__ == "__main__":
    print("=== FlexiToolkit | Volatility Memory Forensics ===")
    image = input("Enter full path to memory image: ")
    plugin = input("Enter Volatility plugin (default: windows.info): ") or "windows.info"
    run_volatility(image, plugin)
