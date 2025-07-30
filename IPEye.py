import socket
import threading
import re
import sys
import json
import platform
import time
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ------------------ Banner ------------------

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
 ██▓ ██▓███  ▓█████ ▓██   ██▓▓█████
▓██▒▓██░  ██▒▓█   ▀  ▒██  ██▒▓█   ▀ 
▒██▒▓██░ ██▓▒▒███     ▒██ ██░▒███   
░██░▒██▄█▓▒ ▒▒▓█  ▄   ░ ▐██▓░▒▓█  ▄ 
░██░▒██▒ ░  ░░▒████▒  ░ ██▒▓░░▒████▒
░▓  ▒▓▒░ ░  ░░░ ▒░ ░   ██▒▒▒ ░░ ▒░ ░
 ▒ ░░▒ ░      ░ ░  ░ ▓██ ░▒░  ░ ░  ░
 ▒ ░░░          ░    ▒ ▒ ░░     ░   
 ░              ░  ░░ ░        ░  ░
                    ░ ░             
                                v1.0        
          IPEye - IP and Port Scanner
          Author: Lamia Lathif

""" + Style.RESET_ALL)

banner()

# ANSI color codes for terminal output
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

lock = threading.Lock()
open_ports_count = {}
open_ports_result = []

COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

# ------------------ Helper Functions ------------------

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False

def ip_to_num(ip):
    parts = list(map(int, ip.split('.')))
    return parts[0]*256**3 + parts[1]*256**2 + parts[2]*256 + parts[3]

def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start.copy()
    ip_list = [start_ip]

    while temp != end:
        temp[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_list.append(".".join(map(str, temp)))
    return ip_list

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        service = COMMON_SERVICES.get(port, "Unknown")
        result = f"{GREEN}[OPEN   ]{RESET} Port {port} ({service}) on {ip}"
        s.close()
        show_result = True
        with lock:
            open_ports_count[ip] = open_ports_count.get(ip, 0) + 1
            open_ports_result.append({"ip": ip, "port": port, "service": service})
            if save_txt:
                with open("scan_results.txt", "a") as f:
                    f.write(f"OPEN: Port {port} ({service}) on {ip}\n")
    except:
        result = f"{RED}[CLOSED ]{RESET} Port {port} on {ip}"
        show_result = (show_only_open == 'n')
        if show_result and save_txt:
            with lock:
                with open("scan_results.txt", "a") as f:
                    f.write(f"CLOSED: Port {port} on {ip}\n")
    finally:
        if show_result:
            with lock:
                print(result)

# ---------------------- MAIN ----------------------

print(f"{CYAN}{BOLD}\nScanner Configuration:{RESET}")

while True:
    choice = input(f"{BOLD} [1] Scan Single IP\n [2] Scan IP Range\n{YELLOW}Select mode:{RESET} ").strip()
    if choice in ["1", "2"]:
        break
    print(f"{RED}❌ Invalid input. Please choose 1 or 2.{RESET}")

while True:
    show_only_open = input(f"{BOLD}Show only open ports? [y/n]: {RESET}").strip().lower()
    if show_only_open in ["y", "n"]:
        break
    print(f"{RED}❌ Please enter 'y' or 'n'.{RESET}")

while True:
    save_txt = input(f"{BOLD}Save output to TXT file? [y/n]: {RESET}").strip().lower()
    if save_txt in ["y", "n"]:
        save_txt = (save_txt == "y")
        break
    print(f"{RED}❌ Please enter 'y' or 'n'.{RESET}")

while True:
    save_json = input(f"{BOLD}Save output to JSON file? [y/n]: {RESET}").strip().lower()
    if save_json in ["y", "n"]:
        save_json = (save_json == "y")
        break
    print(f"{RED}❌ Please enter 'y' or 'n'.{RESET}")

if choice == "1":
    while True:
        ip = input(f"{BOLD}Enter IP address to scan: {RESET}").strip()
        if is_valid_ip(ip):
            break
        print(f"{RED}❌ Invalid IP format.{RESET}")
    ips = [ip]

elif choice == "2":
    while True:
        start_ip = input(f"{BOLD}Start IP address: {RESET}").strip()
        if not is_valid_ip(start_ip):
            print(f"{RED}❌ Invalid format.{RESET}")
            continue

        end_ip = input(f"{BOLD}End IP address: {RESET}").strip()
        if not is_valid_ip(end_ip):
            print(f"{RED}❌ Invalid format.{RESET}")
            continue

        if ip_to_num(end_ip) < ip_to_num(start_ip):
            print(f"{RED}❌ End IP must be equal to or greater than Start IP.{RESET}")
            continue

        break
    ips = ip_range(start_ip, end_ip)

while True:
    try:
        start_port = int(input(f"{BOLD}Start port [default: 0]: {RESET}") or "0")
        end_port = int(input(f"{BOLD}End port [default: 1023]: {RESET}") or "1023")
        if 0 <= start_port <= end_port <= 65535:
            break
        else:
            raise ValueError
    except:
        print(f"{RED}❌ Invalid port range.{RESET}")

max_threads = 100

if save_txt:
    open("scan_results.txt", "w").close()

# ------------------ Scanning ------------------

for ip in ips:
    print(f"\n{BOLD}🔍 Scanning {ip} [ports {start_port}-{end_port}]...{RESET}\n")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_port, ip, port)

    if open_ports_count.get(ip, 0) == 0:
        print(f"\n{YELLOW}⚠️  No open ports found on {ip}.{RESET}")

# ------------------ Summary ------------------

print(f"\n{CYAN}{BOLD}📊 Scan Summary:{RESET}")
for ip, count in open_ports_count.items():
    print(f" - {ip}: {count} open port(s)")

if save_txt:
    print(f"\n{GREEN}📂 TXT results saved to 'scan_results.txt'{RESET}")

if save_json:
    with open("scan_results.json", "w") as f:
        json.dump(open_ports_result, f, indent=4)
    print(f"{GREEN}📂 JSON results saved to 'scan_results.json'{RESET}")


print(f"\n{GREEN}✅ Scanning complete.{RESET}")
