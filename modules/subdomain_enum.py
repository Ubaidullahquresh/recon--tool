import requests

def run_subdomain_enum(domain):
    try:
        domain = domain.strip().lower().rstrip(".")  # normalize domain
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                sub = sub.strip().lower()
                # Check if sub ends with the domain (handle cases like www.domain.com)
                if sub.endswith(domain):
                    # Optional: also exclude entries where the domain is part of a longer suffix
                    # For example, if domain is example.com, exclude notexample.com
                    if sub == domain or sub.endswith("." + domain):
                        subdomains.add(sub)
        return "\n".join(sorted(subdomains)) if subdomains else "No subdomains found."
    except Exception as e:
        return f"[!] Subdomain Enumeration Error: {e}"
