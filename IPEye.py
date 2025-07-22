import socket
import threading
import re

lock = threading.Lock()
open_ports_count = {}  # Track open ports per IP

# Validate IPv4 format
def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False

# Convert IP string to a number for comparison
def ip_to_num(ip):
    parts = list(map(int, ip.split('.')))
    return parts[0]*256**3 + parts[1]*256**2 + parts[2]*256 + parts[3]

# Generate list of IPs in range
def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start.copy()
    ip_list = []

    ip_list.append(start_ip)
    while temp != end:
        temp[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_list.append(".".join(map(str, temp)))
    return ip_list

# Port scanner function
def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        result = f"[OPEN   ] Port {port} on {ip}"
        s.close()
        show_result = True
        with lock:
            open_ports_count[ip] = open_ports_count.get(ip, 0) + 1
    except:
        result = f"[CLOSED ] Port {port} on {ip}"
        show_result = (show_only_open == 'n')
    finally:
        if show_result:
            with lock:
                print(result)
                # Uncomment below to save results to a file
                # with open("scan_results.txt", "a") as f:
                #     f.write(result + "\n")

# --------------------- MAIN ---------------------

print("Select scanning mode:")
print("1. Scan a Single IP")
print("2. Scan a Range of IPs")

while True:
    choice = input("Enter 1 or 2: ").strip()
    if choice in ["1", "2"]:
        break
    print("❌ Invalid choice. Please enter 1 or 2.")

# Ask whether to show only open ports
while True:
    show_only_open = input("Do you want to display only open ports? (y/n): ").strip().lower()
    if show_only_open in ["y", "n"]:
        break
    print("❌ Please enter 'y' or 'n'.")

if choice == "1":
    # Single IP mode
    while True:
        ip = input("Enter IP address to scan: ").strip()
        if is_valid_ip(ip):
            break
        print("❌ Invalid IP format.")
    ips = [ip]

elif choice == "2":
    # Range mode with validation
    while True:
        start_ip = input("Enter starting IP address: ").strip()
        if not is_valid_ip(start_ip):
            print("❌ Invalid IP format.")
            continue

        end_ip = input("Enter ending IP address: ").strip()
        if not is_valid_ip(end_ip):
            print("❌ Invalid IP format.")
            continue

        if ip_to_num(end_ip) < ip_to_num(start_ip):
            print("❌ Wrong IP range! Ending IP must be equal to or higher than starting IP.")
            continue

        break

    ips = ip_range(start_ip, end_ip)

# Start scanning
start_port = 0
end_port = 1023
max_threads = 100

open("scan_results.txt", "w").close()  # Clear previous results

for ip in ips:
    print(f"\n🔍 Scanning well-known ports on {ip}...\n")
    threads = []  # Reset threads list per IP

    for port in range(start_port, end_port + 1):
        while threading.active_count() > max_threads:
            pass  # Wait if too many threads
        t = threading.Thread(target=check_port, args=(ip, port))
        t.start()
        threads.append(t)

    # Wait for all ports on this IP to finish
    for t in threads:
        t.join()

    # Now check and print if no open ports for this IP
    if open_ports_count.get(ip, 0) == 0:
        print(f"\nℹ️ No open ports found on {ip}.")

print("\n✅ Scanning complete.")
