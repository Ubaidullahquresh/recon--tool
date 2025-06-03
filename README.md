# Recon-Tool

## Overview
Recon-Tool is a lightweight, modular reconnaissance tool designed for penetration testers and red teamers to automate initial information gathering.  
It supports passive and active recon with detailed reports.

---

## Features

- WHOIS Lookup
- DNS Enumeration (A, MX, TXT, NS records)
- Subdomain Enumeration (crt.sh API)
- Port Scanning (common ports)
- Banner Grabbing
- Technology Detection (via WhatWeb)
- Generates reports in `.txt` or `.html`
- Modular CLI with command-line flags
- Logging with verbosity levels

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recon-tool.git
   cd recon-tool
2. Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

3. Install required packages:

pip install -r requirements.txt


4. (Optional) Install WhatWeb:

sudo apt install whatweb



Usage

Run the tool with your desired modules:

python3 main.py --target example.com --whois --dns --subdomains --portscan --banner --tech --report txt --verbose



Available flags:

    --whois: WHOIS lookup

    --dns: DNS enumeration

    --subdomains: Subdomain enumeration

    --portscan: Port scanning

    --banner: Banner grabbing

    --tech: Technology detection

    --report [txt|html]: Report format (default txt)

    --verbose: Show detailed logs




Sample Report Screenshot

(Add your screenshot here)
License

MIT License
Author

Ubaidullah Qureshi


4. Save and exit nano: Press `Ctrl+O` (Enter to confirm), then `Ctrl+X`.

---

# Step 1.1: Add a Screenshot of Your Report

1. Generate your report (run your tool with the `--report` flag on a test domain).

2. View the report in your preferred app:
   - If `.html`, open with Firefox:  
     ```bash
     firefox reports/sample_report.html &
     ```
   - If `.txt`, open with `nano` or `less`.

3. Take a screenshot:

- Install `scrot` if you don’t have it:

  ```bash
  sudo apt install scrot




Run:	scrot reports/sample_report_screenshot.png



4.     Your screenshot will be saved inside the reports/ folder.

5.     You can reference this screenshot in your README.md later, like:

![Sample Report Screenshot](reports/sample_report_screenshot.png)



