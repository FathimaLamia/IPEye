
# 🔍 IPEye - IP and Port Scanner

IPEye is a multi-threaded Python-based IP and Port Scanner designed for quick and efficient scanning of IP ranges and port ranges. It's perfect for network administrators, penetration testers, and cybersecurity learners who want a lightweight and flexible scanning utility.

# 🌐 What is IPEye?

IPEye allows users to scan a range of IP addresses and a range of TCP ports simultaneously. It helps in discovering open ports and live hosts within a specified subnet and is optimized for speed using Python’s threading module.

# 🚀 Features

- Scan multiple IPs and ports simultaneously

- Multi-threaded for fast scanning

- Easy to edit default values

- Thread control to avoid overloading

- Output to terminal and optionally to a file

- Commented user input section for interactive scanning

# 📁 File Contents

- `IPEye.py` – The main Python script containing the scanner code.

# 📝 Installation & Requirements

1. Python 3 must be installed. Use the following to check:

```python
python3 --version
```

2. Run the script:

```python
python3 IPEye.py
```

# ⚙️ Default Settings

By default, the script uses the following hardcoded values:

```python
start_ip = "192.168.1.1"

end_ip = "192.168.1.5"

start_port = 20

end_port = 25
```

To scan different IPs or ports, uncomment the relevant sections of the code:

```python
#start_ip = input("Enter the starting IP address (e.g., 192.168.1.1): ")

#end_ip = input("Enter the ending IP address (e.g., 192.168.1.5): ")

#start_port = int(input("Enter the starting port (e.g., 20): "))

#end_port = int(input("Enter the ending port (e.g., 25): "))
```
You may also want to validate IPs using the commented-out regex section.

# 💾 Output

By default, results are printed to the terminal. To also save results to a file `(scan_results.txt)`, uncomment:

```python
#with open("scan_results.txt", "a") as f:

#f.write(result + "\n")
```

# 💡 How It Works

- IP Range Generator: Iterates from `start_ip` to `end_ip`.
 
- Threaded Scanning: Each port scan runs on a separate thread.

- Timeout Control: Uses a 1 second timeout to avoid hanging.

- Thread Limit: Controls thread count with `max_threads` variable.

# ⚠️ Legal & Ethical Use

- Use IPEye only on networks you own or have explicit permission to scan.

- Unauthorized scanning may violate network policies or laws.

# 👩‍💻 Author

Lamia Lathif

A dedicated cybersecurity learner focused on building practical tools for real-world problem solving.

# 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork this project, enhance it, and share your improvements.
