import volatility3 
from volatility3.framework import contexts
from volatility3.plugins.windows import psscan  # Change to psscan plugin for process scanning

def run():
    print("[*] Running Memory Forensics Tool...")
    
    # Ask for the memory dump file path (just like the other tools)
    memory_file = input("Enter full path to the memory dump file: ")
    
    # Set up the volatility context (configure for your use case, OS, etc.)
    context = contexts.Context()

    # Use psscan plugin instead of pslist
    try:
        print("[*] Analyzing memory dump...")
        plugin = psscan.PSScan(context, memory_file)
        plugin.run()  # This will analyze the memory dump for processes
        print("[✓] Memory analysis completed successfully!")
    except Exception as e:
        print(f"[-] Error during memory forensics: {e}")
