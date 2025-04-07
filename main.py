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
    # Add code to run disk forensics here

def run_log_analysis():
    print("Running Log Analysis Tool...")
    # Add code to run log analysis here

def run_memory_forensics():
    print("Running Memory Forensics Tool...")
    # Add code to run memory forensics here

def run_network_analysis():
    print("Running Network Analysis Tool...")
    # Add code to run network analysis here

def run_hash_checker():
    print("Running Hash Checker Tool...")
    # Add code to run hash checker here

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            run_disk_forensics()
        elif choice == '2':
            run_log_analysis()
        elif choice == '3':
            run_memory_forensics()
        elif choice == '4':
            run_network_analysis()
        elif choice == '5':
            run_hash_checker()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
