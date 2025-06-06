import requests
import re

def run_subdomain_enum(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())
        return "\n".join(sorted(subdomains)) if subdomains else "No subdomains found."
    except Exception as e:
        return f"[!] Subdomain Enumeration Error: {e}"
