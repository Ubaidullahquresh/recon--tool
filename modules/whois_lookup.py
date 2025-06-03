
import subprocess

def run_whois(target):
    try:
        result = subprocess.check_output(["whois", target], stderr=subprocess.DEVNULL)
        return result.decode()
    except Exception as e:
        return f"[!] WHOIS Error: {e}"
