import socket
import ssl

def grab_banner(target, port=80, timeout=3):
    try:
        # Create TCP socket
        s = socket.socket()
        s.settimeout(timeout)

        # For HTTPS (port 443), wrap in SSL
        if port == 443:
            context = ssl.create_default_context()
            s = context.wrap_socket(s, server_hostname=target)

        # Connect to target
        s.connect((target, port))

        # Protocol-specific banner grabbing
        if port in [80, 8080, 8000]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n" % target.encode())
        elif port == 443:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n" % target.encode())
        elif port == 21:  # FTP
            return s.recv(1024).decode(errors='ignore')
        elif port == 22:  # SSH
            return s.recv(1024).decode(errors='ignore')
        elif port == 25:  # SMTP
            return s.recv(1024).decode(errors='ignore')
        else:
            s.sendall(b"\r\n")  # Generic probe

        # Receive banner
        banner = s.recv(1024).decode(errors='ignore')
        s.close()
        return banner if banner else "[!] No banner received."

    except Exception as e:
        return f"[!] Banner Grab Failed on port {port}: {e}"

# Example usage:
if __name__ == "__main__":
    target = "testphp.vulnweb.com"
    ports = [80, 443, 21, 22, 25]
    
    print(f"[+] Banner Grabbing for: {target}")
    for port in ports:
        print(f"\n--- Port {port} ---")
        print(grab_banner(target, port))
