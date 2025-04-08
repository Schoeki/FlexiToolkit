import re

# Function to analyze the log for failed logins
def analyze_log(file_path):
    try:
        with open(file_path, 'r') as f:
            logs = f.readlines()

        failed_logins = [line for line in logs if "failed" in line.lower()]
        suspicious_ips = set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ' '.join(failed_logins)))

        print("=== FlexiToolkit | Log Analysis ===")
        print(f"Total log lines: {len(logs)}")
        print(f"Suspicious failed login attempts: {len(failed_logins)}")
        print("Possible attacker IPs:")
        for ip in suspicious_ips:
            print(f" - {ip}")

    except FileNotFoundError:
        print("[-] Log file not found!")

# Define the run function
def run():
    log_path = input("Enter full path to log file: ")
    analyze_log(log_path)  # Call the analyze_log function with the log file path
