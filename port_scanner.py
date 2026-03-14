
import socket

target = "127.0.0.1"
ports = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

print(f"Scanning target: {target}\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    sock.close()
