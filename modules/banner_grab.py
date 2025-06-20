import socket

def run_banner_grab(target, port=80):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        s.send(b'HEAD / HTTP/1.1\r\nHost: %s\r\n\r\n' % target.encode())
        banner = s.recv(1024).decode()
        return banner
    except Exception as e:
        return f"[!] Banner Grab Error: {e}"
