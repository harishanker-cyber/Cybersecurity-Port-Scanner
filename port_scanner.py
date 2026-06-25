import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    except KeyboardInterrupt:
        print("\nScan stopped.")
        exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()

    except socket.error:
        print("Server not responding.")
        exit()

target = input("Enter IP Address or Domain: ")

print(f"\nScanning Target: {target}")
print("-" * 40)

for port in range(1, 1025):
    scan_port(target, port)

print("\nScan Completed.")
