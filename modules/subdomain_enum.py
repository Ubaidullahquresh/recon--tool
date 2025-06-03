import socket

def run_subdomain_enum(domain):
    subdomains = ['www', 'mail', 'ftp', 'test', 'dev']
    found = []
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found.append(f"{subdomain} → {ip}")
        except socket.gaierror:
            continue
    return "\n".join(found) if found else "No subdomains found."

