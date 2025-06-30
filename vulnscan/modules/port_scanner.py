# modules/port_scanner.py
def scan_ports(target):
    import socket
    print("[*] Running port scan...")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]
    open_ports = []
    for port in common_ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            open_ports.append(port)
            sock.close()
        except:
            continue
    print(f"[+] Open ports found: {open_ports}")
    return open_ports
