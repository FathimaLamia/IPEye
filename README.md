
# 🔍 IPEye - IP and Port Scanner

IPEye is a multi-threaded Python-based IP and Port Scanner designed for quick and efficient scanning of IP ranges and port ranges. It's perfect for network administrators, penetration testers, and cybersecurity learners who want a lightweight and flexible scanning utility.

# 🌐 What is IPEye?

IPEye allows users to scan:

- A **single IP** or a **range of IP addresses**
- All **well-known TCP ports (1–1023)**
- Optionally display **only open ports** or **both open and closed**

# 🚀 Features

- Scan **single IP** or **IP ranges**
- Auto-scans **ports 1–1023** (well-known ports)
- Multi-threaded for fast scanning
- Option to view only open ports or all
- Error handling for invalid IP ranges
- Output to terminal and to `scan_results.txt`
- Shows "No open ports" if nothing is found
- Neatly formatted results for easy reading

# 📁 File Contents

- `IPEye.py` – The main Python script containing the scanner code.
- `scan_results.txt` – Auto-generated file containing the scan output.

# 📝 Installation & Requirements

1. Python 3 must be installed. Use the following to check:

```python
python3 --version
```

2. Run the script:

```python
python3 IPEye.py
```

# ⚙️ Settings & Input

The script starts by asking you:

1. Do you want to scan a single IP or a range of IPs?

2. Do you want to display only open ports or both open and closed?

It then performs threaded scans across the IP(s) and ports (1–1023).

Invalid IP ranges are caught with an error message.

# 💾 Output

By default, scan results are printed to the terminal.

To also save the results to a file (`scan_results.txt`), uncomment the following lines in the code inside the `check_port` function:

```python
with open("scan_results.txt", "a") as f:
    f.write(result + "\n")
```

Example output: 

```python
🔍 Scanning well-known ports on 192.168.1.1...

[OPEN ] Port 53 on 192.168.1.1

[OPEN ] Port 80 on 192.168.1.1

[OPEN ] Port 443 on 192.168.1.1

🔍 Scanning well-known ports on 192.168.1.2...

No open ports found on 192.168.1.2.

🔍 Scanning well-known ports on 192.168.1.3...

No open ports found on 192.168.1.3.

✅ Scanning complete.

```

# 💡 How It Works

- IP Range Generator: Iterates from start IP to end IP

- Threaded Scanning: Each port check runs on a thread

- Port Range: Scans TCP ports from 1 to 1023

- Timeout Control: 1 second socket timeout

- Thread Lock: Ensures clean terminal and file output

- Validation: Prevents invalid IP ranges from running silently

# ⚠️ Legal & Ethical Use

- Use IPEye only on networks you own or have explicit permission to scan.

- Unauthorized scanning may violate network policies or laws.

# 👩‍💻 Author

Lamia Lathif

A dedicated cybersecurity learner focused on building practical tools for real-world problem solving.

# 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork this project, enhance it, and share your improvements.
