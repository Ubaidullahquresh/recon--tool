import socket

def run_port_scan(target):
    open_ports = []
    for port in [21, 22, 23, 25, 53, 80, 443, 8080]:
        try:
            sock = socket.create_connection((target, port), timeout=1)
            open_ports.append(port)
            sock.close()
        except:
            continue
    return f"Open Ports: {open_ports}"
