import volatility3 
from volatility3.framework import contexts
from volatility3.plugins.windows import pslist  # Replaced psscan with pslist

def run():
    print("[*] Running Memory Forensics Tool...")
    
    # Ask for the memory dump file path
    memory_file = input("Enter full path to the memory dump file: ")
    
    # Set up the volatility context
    context = contexts.Context()

    try:
        print("[*] Analyzing memory dump...")
        
        # Initialize Volatility's PSList plugin (lists processes in the memory dump)
        plugin = pslist.PSList(context, memory_file)
        plugin.run()  # This will list the processes in the memory dump
        
        print("[✓] Memory analysis completed successfully!")
    except Exception as e:
        print(f"[-] Error during memory forensics: {e}")
