import requests
import socket

def run_subdomain_enum(domain):
    domain = domain.strip().lower().rstrip(".")
    subdomains = set()

    # First: crt.sh API enumeration
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                sub = sub.strip().lower()
                if sub == domain or sub.endswith("." + domain):
                    subdomains.add(sub)
    except Exception as e:
        # Log error but continue to brute force
        print(f"[!] crt.sh API error: {e}")

    # Second: brute-force with wordlist if crt.sh found nothing
    if not subdomains:
        wordlist = ['www', 'mail', 'ftp', 'test', 'dev']
        for sub in wordlist:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                subdomains.add(f"{subdomain} → {ip}")
            except socket.gaierror:
                continue

    return "\n".join(sorted(subdomains)) if subdomains else "No subdomains found."
