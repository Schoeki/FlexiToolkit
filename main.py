from disk_forensics import disk_imaging  # Import disk forensics module
from memory_forensics import volatility  # Import memory forensics module
from network_analysis import pyshark    # Import network analysis module
from log_analysis import log_parser     # Import log analysis module
from utils import hash_checker          # Import hash checker module

def display_menu():
    print("Welcome to FlexiToolkit - Lightweight Forensics Tool")
    print("Select the module you want to use:")
    print("1. Disk Forensics")
    print("2. Log Analysis")
    print("3. Memory Forensics")
    print("4. Network Analysis")
    print("5. Hash Checker")
    print("6. Exit")

def run_disk_forensics():
    print("Running Disk Forensics Tool...")
    disk_imaging.run()  # Call the run function from disk_forensics module

def run_log_analysis():
    print("Running Log Analysis Tool...")
    log_parser.run()  # Call the run function from log_analysis module

def run_memory_forensics():
    print("Running Memory Forensics Tool...")
    volatility.run()  # Call the run function from memory_forensics module

def run_network_analysis():
    print("Running Network Analysis Tool...")
    pyshark.run()  # Call the run function from network_analysis module

def run_hash_checker():
    print("Running Hash Checker Tool...")
    hash_checker.run()  # Call the run function from utils hash_checker module

def main():
    while True:
        display_menu()  # Display the options in the CLI menu
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            run_disk_forensics()  # Call the disk forensics function
        elif choice == '2':
            run_log_analysis()  # Call the log analysis function
        elif choice == '3':
            run_memory_forensics()  # Call the memory forensics function
        elif choice == '4':
            run_network_analysis()  # Call the network analysis function
        elif choice == '5':
            run_hash_checker()  # Call the hash checker function
        elif choice == '6':
            print("Exiting... Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid input handling

if __name__ == "__main__":
    main()  # Run the main program


