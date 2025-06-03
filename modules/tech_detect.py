import subprocess

def run_tech_detect(target):
    try:
        result = subprocess.check_output(['whatweb', target])
        return result.decode()
    except Exception as e:
        return f"[!] Tech Detect Error: {e}"
