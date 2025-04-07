# FlexiToolkit | Log Analysis Module

This module detects suspicious failed login attempts from server log files. It is part of the FlexiToolkit forensic suite.

## Features
- ✅ Detects failed login attempts
- ✅ Displays total log entries
- ✅ Identifies IPs with failed login attempts
- ✅ Helps spot potential brute-force attackers

## How to Use

1. Place your log file (e.g., `sample_log.txt`) in the same directory.
2. Run the script:

```bash
python log_tool.py
```

3. When prompted, enter the filename (e.g., `sample_log.txt`).

## Example Output

```
=== FlexiToolkit | Log Analysis ===
Total log lines: 3
Suspicious failed login attempts: 2
Possible attacker IPs:
 - 192.168.1.101
 - 10.0.0.5
```

## Sample Log Format

```
[INFO] User admin logged in from 192.168.1.100
[WARNING] Failed login attempt from 192.168.1.101
[WARNING] Failed login attempt from 10.0.0.5
```
