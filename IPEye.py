import socket
import re
import threading
import time

lock = threading.Lock() 

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        result = f"[OPEN ]Port {port} on {ip}"
        s.close()
    except:
        result = f"[CLOSED ]Port {port} on {ip}"
    finally:
	    with lock:
        	print(result)
        	# Uncomment below lines to save results to a file
            	# with open("scan_results.txt", "a") as f:
           	# f.write(result + "\n")

# Generate list of IPs in a range 
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

# Uncomment the lines below for user input.
# Or leave them commented to use the default values.

#start_ip = input("Enter the starting IP address (e.g. 192.168.1.1): ")
#end_ip = input("Enter the ending IP address (e.g. 192.168.1.5): ")
#start_port = int(input("Enter the startng port number (e.g. 20): "))
#end_port = int(input("Enter the ending port number (e.g. 25): "))

# Optional: validate IP address format
#def is_valid_ip(ip):
#    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
#    return re.match(pattern, ip)

# Ask for Start IP
#while True:
#    start_ip = input("Enter the starting IP address (e.g., 192.168.1.1): ")
#    if is_valid_ip(start_ip):
#        break
#   print("❌ Invalid format. Please enter the IP in the format: 192.168.1.1")

# Ask for End IP
#while True:
#    end_ip = input("Enter the ending IP address (e.g., 192.168.1.5): ")
#    if is_valid_ip(end_ip):
#        break
#    print("❌ Invalid format. Please enter the IP in the format: 192.168.1.5")


# Default values (Customize these as needed)
start_ip = "192.168.1.1"
end_ip = "192.168.1.5"
start_port = 20
end_port = 25
max_threads = 100

ips = ip_range(start_ip, end_ip)

threads = []

open("scan_results.txt", "w").close()  # clear old results

for ip in ips:
    print(f"\nScanning {ip}...\n")
    for port in range(start_port, end_port + 1):
        while threading.active_count() > max_threads:
                time.sleep(0.01)
        t = threading.Thread(target=check_port, args=(ip, port))
        t.start()
        threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print("\n Scanning complete.")
