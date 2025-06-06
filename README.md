🔍 Recon-Tool
Overview

Recon-Tool is a lightweight, modular reconnaissance tool designed for penetration testers and red teamers to automate initial information gathering during security assessments. It supports both passive and active recon techniques, with clear reporting features.


Key Features

    ✅ WHOIS Lookup

    ✅ DNS Enumeration (A, MX, TXT, NS records)

    ✅ Subdomain Enumeration (API-based + wordlist-based)

    ✅ Port Scanning (common ports using sockets)

    ✅ Banner Grabbing

    ✅ Technology Detection (via WhatWeb)

    ✅ Modular CLI using command-line flags

    ✅ TXT/HTML Report generation

    ✅ Logging with verbosity levels


Passive Recon Modules

    --whois → Fetch domain registration info

    --dns → Enumerate A, MX, TXT, NS records

    --subdomains → Subdomain discovery using APIs like crt.sh and OTX


Recommended Test Commands:

    python3 main.py --target example.com --whois  
    python3 main.py --target example.com --dns  
    python3 main.py --target example.com --subdomains  

    # Bonus (Full Passive Recon)
    python3 main.py --target example.com --whois --dns --subdomains


Active Recon Modules

    --portscan → Scan for open ports

    --banner → Grab HTTP banner (default: port 80 or specify with --port)

    --tech → Identify technologies with WhatWeb


Recommended Test Commands:

    python3 main.py --target testphp.vulnweb.com --portscan  
    python3 main.py --target testphp.vulnweb.com --banner --port 80  
    python3 main.py --target testphp.vulnweb.com --tech


Reporting

Reports are generated in either .txt or .html formats under the reports/ folder.

Command: 

    python3 main.py --target example.com --whois --dns --subdomains --report html

To view:

    # TXT
    less reports/example_com_report.txt

    # HTML
    firefox reports/example_com_report.html &


Optional Screenshot:

    sudo apt install scrot
    scrot reports/sample_report_screenshot.png


 Installation Guide

    # 1. Clone
    git clone https://github.com/yourusername/recon-tool.git  
    cd recon-tool

    # 2. Create virtual environment
    python3 -m venv venv  
    source venv/bin/activate  

    # 3. Install dependencies
    pip install -r requirements.txt  

    # 4. (Optional) Install WhatWeb
    sudo apt install whatweb  

Modularity & CLI Usage
All modules can be triggered independently using flags:

    python3 main.py --target example.com --whois --dns --subdomains --portscan --banner --tech --report html --verbose

Author

👨‍💻 Name: Ubaidullah Qureshi
🎓 Internship: ITSOLERA – Cyber Department
🛠️ Task: Offensive Security (Tool Development)




