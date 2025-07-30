# 🔭 IPEye

**IPEye** is a fast, multi-threaded IP and Port Scanner written in **Python**. Built for both beginners and cybersecurity professionals, IPEye makes scanning single IPs or ranges easy, efficient, and interactive through a clean terminal interface.

---

## 🌐 What is IPEye?

IPEye helps you scan and detect open ports on a single IP or a range of IP addresses. It identifies common services, supports custom port ranges, and saves results in both TXT and JSON formats. Whether you're auditing your own network or learning ethical hacking, IPEye simplifies port scanning with clarity and speed.

---

## 🚀 Features

- Scan single IP or a range of IPs
- Define custom port ranges (e.g., 0–1023)
- Multi-threaded scanning (fast performance)
- Color-coded output: Easily distinguish open/closed ports
- Service identification for common ports (HTTP, SSH, FTP, etc.)
- Option to save results in:
  - `scan_results.txt`
  - `scan_results.json`
- Interactive, user-driven prompts
- Beginner-friendly and portable (Linux, macOS, Windows)

---

## 📥 Installation

### Prerequisites

Make sure Python 3 and `colorama` are installed:

```bash
sudo apt update
sudo apt install python3 pip
pip install colorama
```
### Clone the repository
```python
git clone https://github.com/FathimaLamia/IPEye.git
cd IPEye
```
### Run the tool
```python
python3 scanner.py
```
---

## 📝 Usage Instructions
1. Start the tool
   Run python3 `scanner.py` in your terminal.

2. Select mode
   Choose to scan:

   - A single IP

   - A range of IPs

3. Enter IP(s)
   Enter the IP address or start/end of the IP range.

4. Set port range
   Specify starting and ending port numbers (0–65535).

5. Output options

   - Choose to display only open ports or all results.

   - Save results to TXT and/or JSON.

6. View results

   - Open ports are displayed with service names.

   - Results are saved to `scan_results.txt` and/or `scan_results.json` if selected.
  
---

## 🔍 Output Sample

```python
[OPEN   ] Port 22 (SSH) on 192.168.1.1
[CLOSED ] Port 80 on 192.168.1.1
```

📁 Files saved as:

 - `scan_results.txt`
 - `scan_results.json`

 ---
   
## 🛠️ How It Works
| Feature             | Description                                      |
| ------------------- | ------------------------------------------------ |
| Single IP scan      | Scans one IP address over the specified ports    |
| IP Range scan       | Scans all IPs in a range (e.g., 192.168.1.1–10)  |
| Port detection      | Identifies open ports using TCP connect scanning |
| Service mapping     | Maps known ports to services (e.g., 22 → SSH)    |
| Multi-threaded      | Uses ThreadPoolExecutor for high performance     |
| Customizable output | Save to `.txt` or `.json`, or view in terminal   |

---

## ⚠️ Legal & Ethical Notice
Ethical Usage: Use IPEye only on systems you own or have permission to scan.

Liability: The author is not responsible for misuse or illegal activities.

---

## 🧑‍💻 Author
Lamia Lathif
A passionate developer building accessible cybersecurity tools.

---

## 🤝 Contributing
Pull requests and feature suggestions are welcome! Help improve IPEye by contributing your ideas or code.
