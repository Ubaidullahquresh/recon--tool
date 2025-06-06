Recon-Tool
Overview

Recon-Tool is a lightweight, modular reconnaissance tool designed for penetration testers and red teamers to automate initial information gathering.
It supports passive and active recon with detailed, easy-to-read reports.
Features

    WHOIS Lookup

    DNS Enumeration (A, MX, TXT, NS records)

    Subdomain Enumeration (crt.sh API)

    Port Scanning (common ports)

    Banner Grabbing

    Technology Detection (via WhatWeb)

    Generates reports in .txt or .html formats

    Modular CLI with command-line flags

    Logging with verbosity levels

Installation

1.    Clone the repository:
  
git clone https://github.com/yourusername/recon-tool.git
cd recon-tool

2.   Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate


3.   Install required packages:

pip install -r requirements.txt

4.   (Optional) Install WhatWeb (for technology detection):

sudo apt install whatweb

Usage

Run the tool with your desired modules:

python3 main.py --target example.com --whois --dns --subdomains --portscan --banner --tech --report html --verbose


Available flags:

    --whois: WHOIS lookup

    --dns: DNS enumeration

    --subdomains: Subdomain enumeration

    --portscan: Port scanning

    --banner: Banner grabbing

    --tech: Technology detection

    --report [txt|html]: Report format (default: txt)

    --verbose: Show detailed logs



    Reporting

Recon-Tool generates detailed reports in either plain text (.txt) or rich HTML (.html) format.

    TXT reports: Simple text files viewable in any text editor or terminal pager (e.g., nano, less).

    HTML reports: Fully formatted web pages stored locally. Open them in any web browser to see a clean, professional layout with sections, colors, and easy navigation.

How to view your HTML report:

    1. Run Recon-Tool with the HTML report option:

python3 main.py --target example.com --whois --dns --subdomains --portscan --banner --tech --report html


   2. Open the generated report in a browser (Firefox example):

firefox reports/example_com_report.html &

   3. Your browser will display the report as a neat web page—no internet required!

Sample Report Screenshot

    1. Generate your report (run your tool with the --report flag on a test domain).

    2. View the report in your preferred app:

        If .html, open with Firefox (or any browser):

        firefox reports/sample_report.html &
        
        If.txt, open with nano or less.

   Take a screenshot to include in your README or presentation:

    3. Install scrot if needed:

       sudo apt install scrot
   
   Take screenshot:

      scrot reports/sample_report_screenshot.png

   4. Your screenshot will be saved inside the reports/ folder.

   5. Reference it in your README like this:

License

MIT License
Author

Ubaidullah Qureshi
